#!/usr/bin/env python3
"""Temporary prep-only prepatch for Public Canon v47.

Runs before the v47 builder in unittest discovery. It patches exactly one
Registry evidence field in the workspace, updates the release-level status
separation reproduction for v47, replaces the builder's history step with an
idempotent latest-snapshot update, upgrades the generated CORE release identity,
disambiguates one historical status token in CANON.md, and emits concise GitHub
annotations for failures. Historical seq1/seq2 are never rewritten. Removed
before the final content tree is frozen.
"""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
PATH = ROOT / "canon" / "REGISTRY.tsv"
EVIDENCE = ROOT / "canon" / "EVIDENCE.tsv"
HISTORY = ROOT / "canon" / "HISTORY.tsv"
CORE = ROOT / "canon" / "CORE.md"
CANON_MD = ROOT / "canon" / "CANON.md"
STATUS_VERIFY = ROOT / "reproduce" / "status-separation" / "verify.py"
STATUS_EXPECTED = ROOT / "reproduce" / "status-separation" / "EXPECTED.txt"
STATUS_README = ROOT / "reproduce" / "status-separation" / "README.md"
CLAIM = "TM-SYM2-PHYSICAL-MEASURE"
PROBE = "probes/P-TM-SYM2-BORN-HALVING-1"
EVIDENCE_ID = "EV-TM-SYM2-PHYSICAL-MEASURE"
BUNDLE_SHA = "acc598e670eb7e57f689a6ecc970438ce7211d1a097514a78847100e8871fa59"
SCOPE_SHA = "f9ad8efe676d58a167f84d3ccfb873e511945fd0a7c301a1113aa275032278d0"

if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
import test_000_v47_builder as builder  # noqa: E402

ORIGINAL_WRITE_SHA256S = builder.write_sha256s
ORIGINAL_RUN_CHECKED = builder.run_checked
ORIGINAL_PATCH_CANON = builder.patch_canon

_ORIGINAL_ADD_FAILURE = unittest.TextTestResult.addFailure
_ORIGINAL_ADD_ERROR = unittest.TextTestResult.addError


def _annotation_message(result, test, err) -> str:
    text = result._exc_info_to_string(err, test)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    tail = " | ".join(lines[-14:]) if lines else "unknown failure"
    msg = f"{test.id()} | {tail}"
    return msg.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")[:7000]


def _annotating_add_failure(self, test, err):
    print(f"::error title=V47_TEST_FAILURE::{_annotation_message(self, test, err)}")
    return _ORIGINAL_ADD_FAILURE(self, test, err)


def _annotating_add_error(self, test, err):
    print(f"::error title=V47_TEST_ERROR::{_annotation_message(self, test, err)}")
    return _ORIGINAL_ADD_ERROR(self, test, err)


unittest.TextTestResult.addFailure = _annotating_add_failure
unittest.TextTestResult.addError = _annotating_add_error


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_tsv(path: Path):
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or ()), list(reader)


def write_tsv(path: Path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise AssertionError(f"{label} replacement count={count}")
    return text.replace(old, new)


def patch_status_separation_audit() -> None:
    text = STATUS_VERIFY.read_text(encoding="utf-8")
    replacements = (
        (
            '"registry and companion-ledger counts match Public Canon v46"',
            '"registry and companion-ledger counts match Public Canon v47"',
            "status count label",
        ),
        (
            'expected_counts = {"T": 135, "D": 41, "C": 27, "F": 13,\n'
            '                       "O": 23, "H": 2}',
            'expected_counts = {"T": 135, "D": 42, "C": 27, "F": 13,\n'
            '                       "O": 22, "H": 2}',
            "status counts",
        ),
        ('and len(normative) == 257', 'and len(normative) == 259', "normative count"),
        ('and len(dependencies) == 376', 'and len(dependencies) == 384', "dependency count"),
        ('and two_architecture == 160', 'and two_architecture == 161', "two-architecture count"),
        ('and len(history) == 755', 'and len(history) == 756', "history count"),
        (
            '    physical_owner = "TM-SYM2-PHYSICAL-MEASURE"\n'
            '    selector_gate = "GATE-L1-L5-TM-SYM2-SELECTOR-STREAM"',
            '    physical_owner = "TM-SYM2-PHYSICAL-MEASURE"\n'
            '    orientation_source = "DEF-TM-SYM2-ORIENTATION-SOURCE"\n'
            '    monomial_lift = "DEF-TM-SYM2-MONOMIAL-VERB-LIFT"\n'
            '    selector_gate = "GATE-L1-L5-TM-SYM2-SELECTOR-STREAM"',
            "TM definition names",
        ),
        (
            '        physical_owner: {\n'
            '            ("DEF-ARCHITECTURE", "REQUIRES"),\n'
            '            ("DEF-ACTION-LAYERS", "REQUIRES"),\n'
            '            ("GOLDEN-SIX-LINE-SYM2-FRAME", "REQUIRES"),\n'
            '            ("GYRON-DENSITY", "REQUIRES"),\n'
            '            ("MEASURE-BORN-VERB", "REQUIRES"),\n'
            '            (projective, "BOUNDED_BY"),\n'
            '            (semilinear, "BOUNDED_BY"),\n'
            '            (reversal, "BOUNDED_BY"),\n'
            '            (spectral, "BOUNDED_BY"),\n'
            '        },',
            '        orientation_source: {\n'
            '            (projective, "REQUIRES"),\n'
            '            (semilinear, "REQUIRES"),\n'
            '            (reversal, "REQUIRES"),\n'
            '        },\n'
            '        monomial_lift: {\n'
            '            ("J-UNIT", "REQUIRES"),\n'
            '            ("J-GOLDEN-BRIDGE", "REQUIRES"),\n'
            '        },\n'
            '        physical_owner: {\n'
            '            ("DEF-ARCHITECTURE", "REQUIRES"),\n'
            '            ("DEF-ACTION-LAYERS", "REQUIRES"),\n'
            '            ("GOLDEN-SIX-LINE-SYM2-FRAME", "REQUIRES"),\n'
            '            (projective, "REQUIRES"),\n'
            '            (orientation_source, "REQUIRES"),\n'
            '            (monomial_lift, "REQUIRES"),\n'
            '            ("MEASURE-BORN-VERB", "REQUIRES"),\n'
            '            ("ABELIAN-FACE-DICTIONARY", "REQUIRES"),\n'
            '            (frozen_owner, "BOUNDED_BY"),\n'
            '            (semilinear, "BOUNDED_BY"),\n'
            '            (reversal, "BOUNDED_BY"),\n'
            '            (spectral, "BOUNDED_BY"),\n'
            '        },',
            "TM dependencies",
        ),
        (
            '        "four closed exact classifications stay T; fired selector and physical successor stay separated",',
            '        "four exact classifications stay T; fired selector stays F; physical successor closes only at D",',
            "TM output label",
        ),
        ('        and has_status(index, physical_owner, "O")', '        and has_status(index, physical_owner, "D")', "TM owner status"),
        ('        and normative.get(physical_owner, {}).get("item_type") == "OBLIGATION"', '        and normative.get(physical_owner, {}).get("item_type") == "DICTIONARY"', "TM owner type"),
        (
            '        and normative.get(physical_owner, {}).get("gate_ids") == born_gate\n'
            '        and scope_contains_all(',
            '        and normative.get(physical_owner, {}).get("gate_ids") == born_gate\n'
            '        and normative.get(orientation_source, {}).get("item_type") == "DEFINITION"\n'
            '        and normative.get(orientation_source, {}).get("layer") == "L5"\n'
            '        and normative.get(monomial_lift, {}).get("item_type") == "DEFINITION"\n'
            '        and normative.get(monomial_lift, {}).get("layer") == "L5"\n'
            '        and index.get(physical_owner, {}).get("evidence") == "probes/P-TM-SYM2-BORN-HALVING-1"\n'
            '        and evidence.get(physical_owner, {}).get("evidence_id") == "EV-TM-SYM2-PHYSICAL-MEASURE"\n'
            '        and evidence.get(physical_owner, {}).get("evidence_kind") == "PUBLIC_PROBE"\n'
            '        and evidence.get(physical_owner, {}).get("location") == "probes/P-TM-SYM2-BORN-HALVING-1"\n'
            '        and evidence.get(physical_owner, {}).get("sha256") == "acc598e670eb7e57f689a6ecc970438ce7211d1a097514a78847100e8871fa59"\n'
            '        and evidence.get(physical_owner, {}).get("hash_mode") == "bundle-manifest-sha256-v1"\n'
            '        and evidence.get(physical_owner, {}).get("architecture_requirement") == "two-architecture"\n'
            '        and scope_contains_all(',
            "TM definitions and evidence",
        ),
        (
            '            ("epsilon_read = chi_Q chi_F as typed L5 data",\n'
            '             "rather than quotienting it", "coherence across all 48 selectors",\n'
            '             "mu_i = 1/6", "M_TM = (1/3)P1 + (2/15)P5",\n'
            '             "is an outcome of the bridge and is not required of it",\n'
            '             "comparison actions only", "enlarge no postcomposition gauge",\n'
            '             "select no representative among the 48 selectors"),',
            '            ("owner-approved typed L5-to-L6 physical dictionary bridge",\n'
            '             "C_sel = Sel_class/G with four classes",\n'
            '             "epsilon_read = chi_Q chi_F", "omega(a,b,c) = c-a",\n'
            '             "separately frozen monomial verb-lift class",\n'
            '             "same normalized two-sheet law for every t",\n'
            '             "six equal line weights 1/6 only as an output",\n'
            '             "no selector representative is chosen",\n'
            '             "no postcomposition gauge is enlarged",\n'
            '             "same-modulus nonmonomial lift has unequal coefficient Born weights",\n'
            '             "no uniqueness among all amplitude lifts",\n'
            '             "no GYRON identification"),',
            "TM D scope",
        ),
        ('        and gates.get(born_gate, {}).get("gate_kind") == "OPEN_LIFT"', '        and gates.get(born_gate, {}).get("gate_kind") == "DICTIONARY_LIFT"', "TM gate kind"),
        (
            '        and "reading orientation retained as typed data"\n'
            '        in gates.get(born_gate, {}).get("decision_condition", "")',
            '        and "complete orientation-retaining L5 source"\n'
            '        in gates.get(born_gate, {}).get("decision_condition", "")',
            "TM gate decision",
        ),
        (
            '        and programs.get(physical_owner, {}).get("program_id") == "MEASURE"\n'
            '        and programs.get(physical_owner, {}).get("queue_role") == "ROOT"\n'
            '        and programs.get(physical_owner, {}).get("work_state") == "STOP"\n'
            '        and programs.get(physical_owner, {}).get("work_mode") == "FORMAL"',
            '        and physical_owner not in programs',
            "TM frontier retirement",
        ),
    )
    for old, new, label in replacements:
        text = replace_once(text, old, new, label)
    STATUS_VERIFY.write_text(text, encoding="utf-8")

    expected = STATUS_EXPECTED.read_text(encoding="utf-8")
    expected = replace_once(
        expected,
        "PASS 01 COUNTS     registry and companion-ledger counts match Public Canon v46",
        "PASS 01 COUNTS     registry and companion-ledger counts match Public Canon v47",
        "expected count line",
    )
    expected = replace_once(
        expected,
        "PASS 19 TM-SYM2    four closed exact classifications stay T; fired selector and physical successor stay separated",
        "PASS 19 TM-SYM2    four exact classifications stay T; fired selector stays F; physical successor closes only at D",
        "expected TM line",
    )
    STATUS_EXPECTED.write_text(expected, encoding="utf-8")

    readme = STATUS_README.read_text(encoding="utf-8")
    readme = replace_once(
        readme,
        "the TM-SYM2 split between four closed exact classifications, the\n"
        "fired frozen selector, and the distinct open physical-measure successor, plus",
        "the TM-SYM2 split between four exact classifications, the fired frozen\n"
        "selector, and the distinct dictionary-grade physical-measure successor closed\n"
        "at D by the orientation-retaining source and monomial Born lift, plus",
        "README TM fold",
    )
    readme += (
        "\nThe v47 count and TM-SYM2 checks additionally require the two new L5 "
        "definition rows, the retired MEASURE frontier entry, the DICTIONARY_LIFT "
        "gate, the public Born-halving probe evidence, and the explicit absence of "
        "GYRON-DENSITY as a dependency of the physical six-line measure.\n"
    )
    STATUS_README.write_text(readme, encoding="utf-8")


def idempotent_patch_history() -> None:
    e_fields, evidence = read_tsv(EVIDENCE)
    if not e_fields:
        raise AssertionError("missing evidence header")
    current = [row for row in evidence if row["claim_id"] == CLAIM]
    if len(current) != 1:
        raise AssertionError(f"evidence rows={len(current)}")
    current = current[0]
    expected = (current["evidence_id"], current["location"], current["sha256"])
    if expected != (EVIDENCE_ID, PROBE, BUNDLE_SHA):
        raise AssertionError(f"unexpected current evidence {expected}")

    fields, rows = read_tsv(HISTORY)
    own = sorted((row for row in rows if row["claim_id"] == CLAIM), key=lambda row: int(row["event_sequence"]))
    seq = [int(row["event_sequence"]) for row in own]
    if seq == [1, 2]:
        row = {field: "" for field in fields}
        row.update(
            event_id="CANON47-STATUS-TM-SYM2-PHYSICAL-MEASURE-3",
            event_sequence="3",
            event_date="2026-08-14",
            release="canon-v47",
            claim_id=CLAIM,
            event_type="STATUS_CHANGE",
            previous_status="O",
            new_status="D",
            scope_sha256=SCOPE_SHA,
            evidence_id=expected[0],
            evidence_location=expected[1],
            evidence_sha256=expected[2],
            rationale=builder.RATIONAL,
        )
        rows.append(row)
    elif seq == [1, 2, 3]:
        row = own[-1]
        if row["event_id"] != "CANON47-STATUS-TM-SYM2-PHYSICAL-MEASURE-3":
            raise AssertionError("unexpected seq3 event id")
        row.update(
            event_date="2026-08-14",
            release="canon-v47",
            event_type="STATUS_CHANGE",
            previous_status="O",
            new_status="D",
            scope_sha256=SCOPE_SHA,
            evidence_id=expected[0],
            evidence_location=expected[1],
            evidence_sha256=expected[2],
            rationale=builder.RATIONAL,
        )
    else:
        raise AssertionError(f"unexpected history chain {seq}")
    write_tsv(HISTORY, fields, rows)


def patch_canon_with_historical_status_disambiguation() -> None:
    ORIGINAL_PATCH_CANON()
    text = CANON_MD.read_text(encoding="utf-8")
    old = (
        "Public Canon v28 also amends the scope and falsifier of\n"
        "TM-SYM2-PHYSICAL-MEASURE [O]."
    )
    new = (
        "Public Canon v28 also amends the scope and falsifier of\n"
        "TM-SYM2-PHYSICAL-MEASURE, which was O at that release."
    )
    text = replace_once(text, old, new, "historical v28 status sentence")
    CANON_MD.write_text(text, encoding="utf-8")


def write_sha256s_with_v47_core() -> None:
    text = CORE.read_text(encoding="utf-8")
    if "Public Canon v47" not in text:
        if "Public Canon v46" not in text:
            raise AssertionError("CORE release identity drift")
        text = text.replace("Public Canon v46", "Public Canon v47")
        CORE.write_text(text, encoding="utf-8")
    import re
    versions = set(re.findall(r"Public Canon v([1-9][0-9]*)", text))
    if versions != {"47"}:
        raise AssertionError(f"CORE mixed versions: {sorted(versions)}")
    ORIGINAL_WRITE_SHA256S()


def concise_run_checked(*args: str) -> str:
    try:
        output = ORIGINAL_RUN_CHECKED(*args)
    except AssertionError as exc:
        lines = str(exc).splitlines()
        tail = "\n".join(lines[-25:])
        raise AssertionError("V47_CONCISE_CHECK_FAILURE\n" + tail) from None
    if args and str(args[0]).endswith("generate_canon_views.py") and "CANON VIEWS APPLIED" in output:
        output += "GENERATED VIEWS UPDATED\n"
    return output


def diagnostic_print_transport_package() -> None:
    for relative in builder.OUTPUT_FILES:
        data = (ROOT / relative).read_bytes()
        print(f"V47_DIAG_FILE {relative} bytes={len(data)} sha256={sha256(data)}")
    for relative in (
        "reproduce/status-separation/verify.py",
        "reproduce/status-separation/EXPECTED.txt",
        "reproduce/status-separation/README.md",
    ):
        data = (ROOT / relative).read_bytes()
        print(f"V47_DIAG_FILE {relative} bytes={len(data)} sha256={sha256(data)}")


class V47RegistryEvidencePatch(unittest.TestCase):
    def test_patch_registry_evidence_and_builder_hooks(self) -> None:
        patch_status_separation_audit()
        with PATH.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            fields = list(reader.fieldnames or ())
            rows = list(reader)
        hits = 0
        for row in rows:
            if row["claim_id"] != CLAIM:
                continue
            hits += 1
            self.assertEqual(row["status"], "D")
            self.assertEqual(sha256(row["scope"].encode("utf-8")), SCOPE_SHA)
            self.assertEqual(row["evidence"], "inline")
            row["evidence"] = PROBE
        self.assertEqual(hits, 1)
        with PATH.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

        builder.patch_history = idempotent_patch_history
        builder.patch_canon = patch_canon_with_historical_status_disambiguation
        builder.write_sha256s = write_sha256s_with_v47_core
        builder.run_checked = concise_run_checked
        builder.print_transport_package = diagnostic_print_transport_package

        data = PATH.read_bytes()
        print(f"V47_REGISTRY_BYTES={len(data)}")
        print(f"V47_REGISTRY_SHA256={sha256(data)}")


if __name__ == "__main__":
    unittest.main()
