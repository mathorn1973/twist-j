"""Nonce commitments and all-at-once verdict locking; no local time witness."""

from dataclasses import dataclass
from hashlib import sha256
import secrets
from typing import Protocol
from schema import VERSION, canonical, digest, hash_object, keys, opaque, require

DOMAIN = b"TWIST-J/C96/bundle/1\x00"
OUTCOMES = {"SATISFIED", "FAILED", "INDETERMINATE"}
FINDINGS = {"FRAME_ROSTER", "READ_GRID", "FIRST_WORK_MISSING", "ABS_WORK_MISSING", "LOCAL_PORTS_MISSING",
            "MISSING", "SATURATION", "TIMING", "INVALID_POINTER", "SYNTHETIC"}


def fresh_nonce():
    return secrets.token_bytes(32)


def fresh_presentation(roster_size=400):
    require(roster_size == 400, "forward roster is exactly 400")
    ids = set()
    while len(ids) != roster_size:
        ids.add(secrets.token_hex(16))
    result = sorted(ids)
    secrets.SystemRandom().shuffle(result)
    return result


def framed_commitment(files, nonce):
    """Length framing binds name, bytes and secret independently random nonce.

    File names and nonce stay sealed until disclosure. Sorting defines one
    byte order; prefixes or concatenation collisions cannot reinterpret a file.
    """
    require(type(nonce) is bytes and len(nonce) == 32, "secret 256-bit nonce required")
    require(type(files) is dict and files, "nonempty bundle")
    h = sha256(DOMAIN)
    def field(data):
        require(type(data) is bytes, "bytes required")
        h.update(len(data).to_bytes(8, "big"))
        h.update(data)
    field(nonce)
    h.update(len(files).to_bytes(8, "big"))
    for name in sorted(files):
        require(type(name) is str and name and "\x00" not in name, "bundle member name")
        field(name.encode("utf-8"))
        field(files[name])
    return h.hexdigest()


def verify_commitment(files, nonce, expected):
    digest(expected)
    require(secrets.compare_digest(framed_commitment(files, nonce), expected), "commitment mismatch")


@dataclass(frozen=True)
class Witnessed:
    digest: str
    purpose: str
    timestamp_ns: int
    witness_identity: str


class IndependentWitness(Protocol):
    """Trust configured OUTSIDE committed data by independent custody owners.

    A production implementation must authenticate independently held timestamp
    receipts (e.g. pinned TSA chain + policy) and check revocation/time policy.
    Setting a boolean in a JSON document is not an implementation.
    """
    def verify(self, receipt: bytes, expected_digest: str, purpose: str) -> Witnessed: ...


class IndependentAcquisitionWitness(Protocol):
    """Authenticate actual acquisition event times and final corpus binding.

    A production verifier must link an independently retained acquisition
    session's start/end events to the preparation, complete roster and final
    raw corpus. Its returned timestamps are authenticated event times, not
    caller assertions or the later time at which a manifest was signed.
    A plain TSA receipt over a caller-supplied historical interval is not
    sufficient. No production implementation is supplied by this package.
    """
    def verify(self, receipt: bytes, expected_digest: str, purpose: str) -> Witnessed: ...


def witnessed(provider, receipt, expected, purpose):
    require(provider is not None, "independent witness provider unavailable")
    require(type(receipt) is bytes and receipt, "authenticated receipt bytes required")
    attestation = provider.verify(receipt, expected, purpose)
    require(isinstance(attestation, Witnessed) and attestation.digest == expected and
            attestation.purpose == purpose and type(attestation.timestamp_ns) is int and
            attestation.timestamp_ns >= 0 and type(attestation.witness_identity) is str and
            bool(attestation.witness_identity), "invalid independently verified receipt")
    return attestation


def validate_roster(roster):
    require(type(roster) is list and len(roster) == 400 and len(set(roster)) == 400, "exact unique 400 forward IDs required")
    for item in roster:
        opaque(item)


def corpus_manifest(roster, records, source, version, license_id):
    """Commit missing records as missing; do not quietly replace initiated runs."""
    validate_roster(roster)
    require(type(records) is list and len(records) == 400 and
            {v.get("id") for v in records} == set(roster), "complete raw roster including failures")
    require(bool(source) and bool(version) and bool(license_id), "external corpus manifest metadata")
    for item in records:
        keys(item, ("id", "origin", "raw_sha256", "status"))
        require(item["origin"] in ("MEASURED", "SYNTHETIC"), "raw origin")
        require(item["status"] in ("RECORDED", "FAILED", "MISSING"), "raw status")
        if item["status"] == "MISSING":
            require(item["raw_sha256"] is None, "missing record cannot have invented raw")
        else:
            digest(item["raw_sha256"])
    return {"schema": VERSION, "kind": "COMPLETE_RAW_ROSTER_400", "source": source,
            "version": version, "license": license_id,
            "records": sorted(records, key=lambda r: r["id"])}


def lock_verdicts(roster, verdicts, contract_sha256):
    validate_roster(roster)
    digest(contract_sha256)
    require(type(verdicts) is list and len(verdicts) == 400, "cannot label 399 COMPLETE_400")
    require({v.get("id") for v in verdicts} == set(roster), "verdict roster mismatch")
    for item in verdicts:
        keys(item, ("id", "packet_sha256", "contract_sha256", "positive", "null", "findings"))
        digest(item["packet_sha256"])
        require(item["contract_sha256"] == contract_sha256, "one frozen predicate contract")
        require(item["positive"] in OUTCOMES and item["null"] in OUTCOMES, "both tri-state verdicts required")
        require(type(item["findings"]) is list and item["findings"] == sorted(set(item["findings"]))
                and set(item["findings"]) <= FINDINGS, "closed assessor findings")
    return {"schema": VERSION, "kind": "COMPLETE_400", "roster_sha256": hash_object(sorted(roster)),
            "contract_sha256": contract_sha256, "verdicts": sorted(verdicts, key=lambda v: v["id"])}


def acquisition_binding(roster, commitments):
    """Bind both independently attested event receipts to this exact corpus."""
    validate_roster(roster)
    keys(commitments, ("PREPARATION", "RAW_CORPUS", "VERDICTS"))
    for value in commitments.values():
        digest(value)
    return hash_object({"schema": VERSION, "kind": "ACQUISITION_SESSION_BINDING",
                        "preparation_commitment": commitments["PREPARATION"],
                        "raw_commitment": commitments["RAW_CORPUS"],
                        "roster_sha256": hash_object(sorted(roster))})


def release_permit(roster, locked, commitments, receipts, provider, acquisition_receipts,
                   acquisition_provider, incidents, inverse_records_still_sealed):
    """Verify chronological custody before releasing ANY revealing record.

    Returns a hash-bound permit; this module does not possess/release keys.
    Caller/key custodian must enforce the permit at its access boundary.
    """
    require(not incidents, "custody/blinding incident blocks valid blind confirmation")
    require(inverse_records_still_sealed is True, "inverse records revealed before forward lock")
    expected = lock_verdicts(roster, locked["verdicts"], locked["contract_sha256"])
    require(locked == expected, "changed or incomplete locked verdicts")
    keys(commitments, ("PREPARATION", "RAW_CORPUS", "VERDICTS"))
    keys(receipts, commitments)
    require(commitments["VERDICTS"] == hash_object(locked), "locked output digest mismatch")
    times = {}
    for purpose, value in commitments.items():
        digest(value)
        times[purpose] = witnessed(provider, receipts[purpose], value, purpose).timestamp_ns
    keys(acquisition_receipts, ("ACQUISITION_START", "ACQUISITION_END"))
    binding = acquisition_binding(roster, commitments)
    acquisition_start_ns = witnessed(acquisition_provider, acquisition_receipts["ACQUISITION_START"],
                                     binding, "ACQUISITION_START").timestamp_ns
    acquisition_end_ns = witnessed(acquisition_provider, acquisition_receipts["ACQUISITION_END"],
                                   binding, "ACQUISITION_END").timestamp_ns
    require(times["PREPARATION"] < acquisition_start_ns <= acquisition_end_ns < times["RAW_CORPUS"] < times["VERDICTS"], "witness chronology")
    return {"kind": "RELEASE_PERMIT", "locked_sha256": hash_object(locked),
            "preparation_commitment": commitments["PREPARATION"], "raw_commitment": commitments["RAW_CORPUS"],
            "acquisition_binding_sha256": binding,
            "acquisition_start_ns": acquisition_start_ns, "acquisition_end_ns": acquisition_end_ns}


def campaign_target_decision(locked, assignments, origins, incidents):
    """Target decision ONLY, deliberately not an overall campaign PASS."""
    validate_roster(list(assignments))
    require(set(origins) == set(assignments), "origin roster mismatch")
    require(locked == lock_verdicts(list(assignments), locked["verdicts"], locked["contract_sha256"]), "lock altered")
    labels = [assignments[item] for item in assignments]
    require(set(labels) == {"positive", "offimage", "cut0", "cut1"}
            and all(labels.count(label) == 100 for label in set(labels)), "100 trials per configuration")
    if incidents or any(v != "MEASURED" for v in origins.values()) or any("SYNTHETIC" in v["findings"] for v in locked["verdicts"]):
        return "NOT_CONFIRMATORY"
    statuses = [v["positive"] if assignments[v["id"]] == "positive" else v["null"] for v in locked["verdicts"]]
    return "TARGET_SATISFIED_PENDING_FULL_AUDIT" if all(s == "SATISFIED" for s in statuses) else "CAMPAIGN_REJECTED"
