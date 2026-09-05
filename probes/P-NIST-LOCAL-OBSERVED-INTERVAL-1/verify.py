#!/usr/bin/env python3
"""Exact finite audit of a causal record adapter, with pinned runtime imports.

No scientific import, acquisition, fixture evaluation or record transformation
occurs before main().  Full archive custody is inherited unchanged.  Digests
compact the transcript; direct indexed-word comparisons audit row ownership.
"""

from collections import Counter, deque
import hashlib
import importlib.util
from itertools import islice, product
import json
import os
from pathlib import Path, PurePosixPath
import re
import struct
import sys
import tempfile
import zipfile
import zlib


MANIFEST_SHA256 = "99875763b8b918ed951534ad0128e09813084aa685482e7579d32b13cfd06dd0"
RECORD_CAP = 1_048_576
CHECKPOINTS = (0, 1, 2, 3, 7, 31, 127, 1023, 8191, 65535, 262143)
CHUNK_CYCLE = (31,)
ALPHABET = (0, 2, 4, 5, 6, 64, 99)
WITNESS_CAP = 8
GATES = ("G01_SYNTHETIC_REFERENCE", "G02_ACTUAL_LOSSLESS",
         "G03_ACTUAL_PREFIX_CHUNKING", "G04_ACTUAL_DERIVED_REFERENCE")
EXPECTED_PATHS = {
    "adapter": "probes/P-NIST-LOCAL-OBSERVED-INTERVAL-1/adapter.py",
    "source_verifier": "probes/P-NIST-RAW-RECORD-QUALIFICATION-1/verify.py",
    "source_manifest": "probes/P-NIST-RAW-RECORD-QUALIFICATION-1/SOURCE.json",
    "notice": "notes/NIST-RAW-CUSTODY-1.md",
}


class FatalError(Exception):
    pass


class DataViolation(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise FatalError(reason)


def canonical(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=True,
                       separators=(",", ":"), allow_nan=False) + "\n").encode("ascii")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def is_sha(value):
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def load_dependencies():
    root = Path(__file__).resolve().parent.parent.parent
    data = (Path(__file__).resolve().parent / "DEPENDENCIES.json").read_bytes()
    require(is_sha(MANIFEST_SHA256), "DEPENDENCY_PIN_NOT_SET")
    require(sha(data) == MANIFEST_SHA256, "DEPENDENCY_MANIFEST_HASH_MISMATCH")
    manifest = json.loads(data)
    require(isinstance(manifest, dict)
            and manifest.get("schema") == "nist-local-interval-dependencies/1",
            "DEPENDENCY_SCHEMA_MISMATCH")
    files = manifest.get("files")
    require(isinstance(files, list) and len(files) == 4, "FOUR_DEPENDENCIES_REQUIRED")
    checked = {}
    for item in files:
        require(isinstance(item, dict), "INVALID_DEPENDENCY_RECORD")
        role = item.get("role")
        require(role in EXPECTED_PATHS and role not in checked, "INVALID_DEPENDENCY_ROLE")
        require(item.get("path") == EXPECTED_PATHS[role], "DEPENDENCY_PATH_MISMATCH")
        require(is_sha(item.get("sha256")) and type(item.get("bytes")) is int
                and item["bytes"] >= 0, "INVALID_DEPENDENCY_IDENTITY")
        path = root / item["path"]
        payload = path.read_bytes()
        require(len(payload) == item["bytes"] and sha(payload) == item["sha256"],
                "DEPENDENCY_IDENTITY_MISMATCH_" + role.upper())
        checked[role] = (path, item)
    return checked


def import_pinned(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, "MODULE_SPEC_UNAVAILABLE")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class Gate:
    def __init__(self):
        self.conditions = 0
        self.failures = 0
        self.first = []

    def check(self, condition, reason, location=None):
        self.conditions += 1
        if not condition:
            self.failures += 1
            if len(self.first) < WITNESS_CAP:
                self.first.append({"reason": reason, "location": location})

    def report(self):
        return {"status": "FIRED" if self.failures else "PASS",
                "checked_conditions": self.conditions, "failed_conditions": self.failures,
                "first8_failures": self.first}


def raw_tuple(row):
    return (row.index, row.channel, row.word2, row.transfer)


def encode_owned(rows):
    for row in rows:
        yield struct.pack("<QQQ", row[1], row[2], row[3])


def reference_packet(stream_id, kind, owned, right, emitted_at):
    """Independent field reference over plain tuples, not adapter views."""
    by_channel = {}
    for row in owned:
        by_channel.setdefault(row[1], []).append(row)
    settings = [row for row in owned if row[1] == 2 or row[1] == 4]
    detectors = by_channel.get(0, [])
    n0, n1 = len(by_channel.get(2, [])), len(by_channel.get(4, []))
    if n0 and n1:
        tag = "BOTH"
    elif n0:
        tag = "ONEHOT_0" if n0 == 1 else "REPEATED_0"
    elif n1:
        tag = "ONEHOT_1" if n1 == 1 else "REPEATED_1"
    else:
        tag = "MISSING"
    left = owned[0] if owned and kind in ("CLOSED_INTERVAL", "PENDING_SUFFIX") else None
    unique = settings[0] if n0 + n1 == 1 else None
    detector_tag = {0: "NO_RECORDED_DETECTOR_ROW",
                    1: "SINGLE_RECORDED_DETECTOR_ROW"}.get(
                        len(detectors), "MULTIPLE_RECORDED_DETECTOR_ROWS")
    return {
        "stream_id": stream_id, "kind": kind, "emitted_at": emitted_at,
        "owned_rows": [list(row) for row in owned],
        "left_sync_reference_index": left[0] if left is not None else None,
        "right_sync_reference": list(right) if right is not None else None,
        "right_sync_reference_is_nonowning": True,
        "right_minus_left_sync_ticks": right[2] - left[2]
            if left is not None and right is not None else None,
        "setting_tag": tag, "setting_counts": [n0, n1],
        "settings": [{"row_index": row[0], "recorded_setting_code": {2: 0, 4: 1}[row[1]],
                      "delta_from_left_sync_ticks": row[2] - left[2] if left is not None else None}
                     for row in settings],
        "unique_setting_reference_index": unique[0] if unique is not None else None,
        "detector_tag": detector_tag,
        "detectors": [{"row_index": row[0],
                       "delta_from_left_sync_ticks": row[2] - left[2] if left is not None else None,
                       "delta_from_unique_setting_ticks": row[2] - unique[2]
                           if unique is not None else None} for row in detectors],
        "calendar_metadata": [{"row_index": row[0], "calendar_word": row[2]}
                              for row in by_channel.get(64, [])],
        "pps_row_indices": [row[0] for row in by_channel.get(5, [])],
        "physical_time_row_indices": [row[0] for row in owned if row[1] in (0, 2, 4, 5, 6)],
        "unknown_row_indices": [row[0] for row in owned if row[1] not in (0, 2, 4, 5, 6, 64)],
        "physical_trial_or_calibrated_no_click_claim": False,
    }


def reference_batch(stream_id, rows):
    """Find all sync indices first, then slice; no streaming transition reuse."""
    syncs = [index for index, row in enumerate(rows) if row[1] == 6]
    if not syncs:
        return [], reference_packet(stream_id, "UNANCHORED", rows, None, None)
    emitted = []
    if syncs[0] > 0:
        right = rows[syncs[0]]
        emitted.append(reference_packet(stream_id, "PREFIX", rows[:syncs[0]], right, right[0]))
    for start, stop in zip(syncs, syncs[1:]):
        right = rows[stop]
        emitted.append(reference_packet(stream_id, "CLOSED_INTERVAL",
                                        rows[start:stop], right, right[0]))
    return emitted, reference_packet(stream_id, "PENDING_SUFFIX", rows[syncs[-1]:], None, None)


def synthetic_audit(adapter):
    gate = Gate()
    cases = 0
    prefix_checks = 0
    split_checks = 0
    fixtures_hash = hashlib.sha256()
    for length in range(5):
        for channels in product(ALPHABET, repeat=length):
            rows = [(index, channel,
                     20250918000300 + index if channel == 64 else
                     ((channel + 3) * (length - index + 1) + index * index) % 23,
                     (length - index) % 3) for index, channel in enumerate(channels)]
            fixtures_hash.update(canonical(rows))
            typed = [adapter.RawRow(*row) for row in rows]
            state = adapter.LocalObservedInterval("synthetic")
            packets = []
            for prefix in range(length + 1):
                if prefix:
                    arrived = typed[prefix - 1]
                    new = state.feed(arrived)
                    gate.check(all(packet.emitted_at == arrived.index
                                   and packet.right_sync_reference == arrived
                                   and arrived.channel == 6 for packet in new),
                               "SYNTHETIC_CAUSAL_EMISSION", [cases, prefix])
                    packets.extend(new)
                reference_emitted, reference_pending = reference_batch("synthetic", rows[:prefix])
                observed = [adapter.packet_object(packet) for packet in packets]
                before = state.next_index
                snapshot = state.snapshot()
                snapshot_again = state.snapshot()
                gate.check(state.next_index == before == prefix and snapshot == snapshot_again,
                           "SYNTHETIC_SNAPSHOT_MUTATION", [cases, prefix])
                gate.check(observed == reference_emitted
                           and adapter.packet_object(snapshot) == reference_pending,
                           "SYNTHETIC_BATCH_PREFIX", [cases, prefix])
                gate.check([adapter.packet_bytes(packet) for packet in packets]
                           == [canonical(packet) for packet in reference_emitted]
                           and adapter.packet_bytes(snapshot) == canonical(reference_pending),
                           "SYNTHETIC_CANONICAL_OR_PERSISTENCE", [cases, prefix])
                owners = [raw_tuple(row) for packet in packets + [snapshot]
                          for row in packet.owned_rows]
                gate.check(owners == rows[:prefix], "SYNTHETIC_EXACT_OWNERSHIP", [cases, prefix])
                prefix_checks += 1
            final_ref, final_pending = reference_batch("synthetic", rows)
            for split in range(length + 1):
                chunked = adapter.LocalObservedInterval("synthetic")
                chunk_packets = list(chunked.feed_many(typed[:split]))
                before_snapshot = chunked.snapshot()
                gate.check(before_snapshot == chunked.snapshot() and chunked.next_index == split,
                           "SYNTHETIC_CHUNK_SNAPSHOT", [cases, split])
                chunk_packets.extend(chunked.feed_many(typed[split:]))
                gate.check([adapter.packet_object(packet) for packet in chunk_packets] == final_ref
                           and adapter.packet_object(chunked.snapshot()) == final_pending,
                           "SYNTHETIC_TWO_CHUNK_REFERENCE", [cases, split])
                split_checks += 1
            cases += 1
    gate.check(cases == 2801, "SYNTHETIC_FAMILY_SIZE")
    return {"gate": gate.report(), "cases": cases, "alphabet": list(ALPHABET),
            "lengths": [0, 1, 2, 3, 4], "all_prefix_checks": prefix_checks,
            "all_two_chunk_split_checks": split_checks,
            "fixture_rows_sha256": fixtures_hash.hexdigest()}


def histogram_summary(counter):
    ordered = sorted(counter.items())
    digest = hashlib.sha256()
    for value, count in ordered:
        digest.update(f"{value}\t{count}\n".encode("ascii"))
    return {"count": sum(counter.values()), "support_size": len(ordered),
            "minimum": ordered[0][0] if ordered else None,
            "maximum": ordered[-1][0] if ordered else None,
            "complete_histogram_sha256": digest.hexdigest(),
            "hash_encoding": "ASCII ascending signed integer, TAB count, LF per bin",
            "top8_by_count_then_value": [list(item) for item in
                                        sorted(ordered, key=lambda item: (-item[1], item[0]))[:8]]}


class PassAudit:
    def __init__(self, adapter, stream_id):
        self.adapter = adapter
        self.stream_id = stream_id
        self.state = adapter.LocalObservedInterval(stream_id)
        self.input_hash = hashlib.sha256()
        self.owner_hash = hashlib.sha256()
        self.packet_hash = hashlib.sha256()
        self.raw_pending = deque()
        self.input_count = 0
        self.expected_consumed = 0
        self.reconstructed_count = 0
        self.has_sync = False
        self.packet_count = 0
        self.closed_count = 0
        self.closed_settings = Counter()
        self.closed_detectors = Counter()
        self.left_deltas = Counter()
        self.setting_deltas = Counter()
        self.undefined_setting_deltas = 0
        self.witnesses = []
        self.persistent_witnesses = []
        self.checkpoint_reports = []
        self.lossless = Gate()
        self.prefix = Gate()
        self.derived = Gate()

    def receive_raw(self, row, original_bytes):
        self.raw_pending.append(row)
        self.input_hash.update(original_bytes)
        self.input_count += 1
        self.has_sync = self.has_sync or row[1] == 6

    def consume(self, packet, actual_right):
        # The expected owned slice comes from original input, independently of
        # the adapter packet's proposed ownership or derived field dictionary.
        count = actual_right[0] - self.expected_consumed
        self.lossless.check(count > 0, "NONEMPTY_EMITTED_OWNER_RANGE", actual_right[0])
        expected = tuple(islice(self.raw_pending, max(0, count)))
        self.lossless.check(len(expected) == count, "RAW_REFERENCE_RANGE_AVAILABLE", actual_right[0])
        actual = tuple(raw_tuple(row) for row in packet.owned_rows)
        self.lossless.check(actual == expected, "EXACT_INDEXED_OWNED_WORDS", actual_right[0])
        self.prefix.check(actual_right[1] == 6 and packet.emitted_at == actual_right[0]
                          and packet.right_sync_reference is not None
                          and raw_tuple(packet.right_sync_reference) == actual_right,
                          "RIGHT_SYNC_ARRIVAL_REFERENCE", actual_right[0])
        expected_kind = "CLOSED_INTERVAL" if expected and expected[0][1] == 6 else "PREFIX"
        reference = reference_packet(self.stream_id, expected_kind, expected,
                                     actual_right, actual_right[0])
        observed = self.adapter.packet_object(packet)
        self.derived.check(observed == reference, "INDEPENDENT_PACKET_FIELDS", actual_right[0])
        for _ in expected:
            self.raw_pending.popleft()
        self.expected_consumed += len(expected)
        for record in actual:
            self.owner_hash.update(struct.pack("<QQQ", record[1], record[2], record[3]))
        self.reconstructed_count += len(actual)
        encoded = canonical(observed)
        self.packet_hash.update(encoded)
        if len(self.witnesses) < WITNESS_CAP:
            self.witnesses.append({
                "packet_ordinal": self.packet_count, "kind": observed["kind"],
                "emitted_at": observed["emitted_at"], "owned_rows": len(actual),
                "setting_tag": observed["setting_tag"], "detector_tag": observed["detector_tag"],
                "canonical_packet_sha256": sha(encoded),
            })
            self.persistent_witnesses.append((packet, encoded))
        self.packet_count += 1
        if observed["kind"] == "CLOSED_INTERVAL":
            self.closed_count += 1
            self.closed_settings[observed["setting_tag"]] += 1
            self.closed_detectors[observed["detector_tag"]] += 1
            for detector in observed["detectors"]:
                delta = detector["delta_from_left_sync_ticks"]
                self.derived.check(type(delta) is int, "CLOSED_DETECTOR_LEFT_DELTA_DEFINED",
                                   detector["row_index"])
                if type(delta) is int:
                    self.left_deltas[delta] += 1
                setting_delta = detector["delta_from_unique_setting_ticks"]
                if setting_delta is None:
                    self.undefined_setting_deltas += 1
                else:
                    self.setting_deltas[setting_delta] += 1

    def checkpoint(self):
        before = self.state.next_index
        snapshot = self.state.snapshot()
        second = self.state.snapshot()
        self.prefix.check(snapshot == second and before == self.state.next_index == self.input_count,
                          "NONMUTATING_PENDING_SNAPSHOT", self.input_count)
        self.prefix.check(snapshot.emitted_at is None and snapshot.right_sync_reference is None,
                          "SNAPSHOT_NOT_TERMINAL_EVENT", self.input_count)
        actual = tuple(raw_tuple(row) for row in snapshot.owned_rows)
        expected = tuple(self.raw_pending)
        self.lossless.check(actual == expected, "EXACT_PENDING_INDEXED_WORDS", self.input_count)
        self.lossless.check(self.reconstructed_count + len(actual) == self.input_count,
                            "EXACT_OWNER_COUNT_AT_PREFIX", self.input_count)
        pending_kind = "PENDING_SUFFIX" if self.has_sync else "UNANCHORED"
        reference = reference_packet(self.stream_id, pending_kind, expected, None, None)
        observed = self.adapter.packet_object(snapshot)
        self.derived.check(observed == reference, "INDEPENDENT_PENDING_FIELDS", self.input_count)
        reconstructed = self.owner_hash.copy()
        for encoded_row in encode_owned(actual):
            reconstructed.update(encoded_row)
        self.lossless.check(reconstructed.hexdigest() == self.input_hash.hexdigest(),
                            "RECONSTRUCTED_RAW_PREFIX_HASH", self.input_count)
        self.prefix.check(all(self.adapter.packet_bytes(packet) == encoded
                              for packet, encoded in self.persistent_witnesses),
                          "FIRST8_EMITTED_PACKETS_PERSIST", self.input_count)
        result = {
            "prefix_rows": self.input_count, "emitted_packets": self.packet_count,
            "emitted_packet_stream_sha256": self.packet_hash.hexdigest(),
            "pending_kind": observed["kind"], "pending_owned_rows": len(actual),
            "pending_packet_sha256": sha(canonical(observed)),
            "raw_prefix_sha256": self.input_hash.hexdigest(),
            "reconstructed_prefix_sha256": reconstructed.hexdigest(),
        }
        self.checkpoint_reports.append(result)

    def report(self):
        return {
            "rows": self.input_count, "emitted_packets": self.packet_count,
            "closed_intervals": self.closed_count,
            "emitted_packet_stream_sha256": self.packet_hash.hexdigest(),
            "raw_prefix_sha256": self.input_hash.hexdigest(),
            "checkpoints": self.checkpoint_reports,
            "closed_setting_tags": dict(sorted(self.closed_settings.items())),
            "closed_detector_tags": dict(sorted(self.closed_detectors.items())),
            "closed_detector_delta_from_left_sync_ticks": histogram_summary(self.left_deltas),
            "closed_detector_delta_from_unique_setting_ticks": histogram_summary(self.setting_deltas),
            "closed_detector_setting_delta_undefined": self.undefined_setting_deltas,
            "first8_emitted_packet_witnesses": self.witnesses,
            "gates": {GATES[1]: self.lossless.report(), GATES[2]: self.prefix.report(),
                      GATES[3]: self.derived.report()},
        }


def selected_rows(member, number, complete):
    index = 0
    while index < number:
        count = min(8192, number - index)
        block = member.read(count * 24)
        if len(block) != count * 24:
            raise DataViolation("SELECTED_PREFIX_TRUNCATED")
        view = memoryview(block)
        for offset, (channel, word2, transfer) in enumerate(struct.iter_unpack("<QQQ", block)):
            yield (index, channel, word2, transfer), view[offset * 24:(offset + 1) * 24]
            index += 1
    if complete and member.read(1):
        raise DataViolation("MEMBER_EXCEEDS_DECLARED_SIZE")


def audit_pass(archive, info, number, complete, adapter, stream_id, mode):
    audit = PassAudit(adapter, stream_id)
    checkpoints = sorted({value for value in CHECKPOINTS if value <= number} | {number})
    audit.checkpoint()
    next_checkpoint = 1
    cycle_index = 0
    with archive.open(info, mode="r") as member:
        iterator = iter(selected_rows(member, number, complete))
        position = 0
        while position < number:
            width = 1 if mode == "continuous" else CHUNK_CYCLE[cycle_index % len(CHUNK_CYCLE)]
            cycle_index += 1
            width = min(width, number - position, checkpoints[next_checkpoint] - position)
            batch = []
            for _ in range(width):
                raw, original_bytes = next(iterator)
                audit.receive_raw(raw, original_bytes)
                batch.append((raw, adapter.RawRow(*raw)))
            if mode == "continuous":
                for packet in audit.state.feed(batch[0][1]):
                    audit.consume(packet, batch[0][0])
            else:
                for packet in audit.state.feed_many(row for _, row in batch):
                    index = packet.emitted_at
                    in_batch = type(index) is int and position <= index < position + width
                    audit.prefix.check(in_batch, "CHUNK_EMISSION_WITHIN_ARRIVALS", position)
                    actual_right = batch[index - position][0] if in_batch else batch[-1][0]
                    audit.consume(packet, actual_right)
            position += width
            if position == checkpoints[next_checkpoint]:
                audit.checkpoint()
                next_checkpoint += 1
        try:
            next(iterator)
        except StopIteration:
            pass
        else:
            raise DataViolation("EXCESS_SELECTED_RECORD")
    return audit.report()


def combine_gate_reports(reports):
    if not reports or any(item.get("status") == "NOT_EVALUATED" for item in reports):
        if not any(item.get("status") == "FIRED" for item in reports):
            return {"status": "NOT_EVALUATED", "checked_conditions": 0,
                    "failed_conditions": 0, "first8_failures": []}
    failures = sum(item.get("failed_conditions", 0) for item in reports)
    return {"status": "FIRED" if failures else "PASS",
            "checked_conditions": sum(item.get("checked_conditions", 0) for item in reports),
            "failed_conditions": failures,
            "first8_failures": [witness for item in reports
                               for witness in item.get("first8_failures", [])][:WITNESS_CAP]}


def analyse_archive(path, obj, source, adapter):
    result = {"id": obj["id"], "station": obj["station"], "role": obj["role"],
              "archive_sha256": obj["sha256"], "archive_bytes": obj["archive_bytes"],
              "qualification": "QUALIFIED", "qualification_failures": []}
    with path.open("rb") as stream:
        source.verify_archive_bytes(stream, obj)
        result["full_archive_verified_before_zip_access"] = True
        try:
            with zipfile.ZipFile(stream, "r") as archive:
                infos = archive.infolist()
                if len(infos) > source.MAX_ZIP_ENTRIES:
                    raise DataViolation("ZIP_ENTRY_LIMIT")
                matches = [info for info in infos
                           if PurePosixPath(info.filename).name == obj["member_basename"]]
                if len(matches) != 1:
                    raise DataViolation("EXPECTED_MEMBER_NOT_UNIQUE")
                info = matches[0]
                if info.is_dir() or info.flag_bits & 1:
                    raise DataViolation("MEMBER_NOT_UNENCRYPTED_FILE")
                if info.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED):
                    raise DataViolation("UNSUPPORTED_COMPRESSION")
                if info.file_size > source.MAX_MEMBER_BYTES or info.file_size % 24:
                    raise DataViolation("MEMBER_SIZE_INCOMPATIBLE")
                number = min(RECORD_CAP, info.file_size // 24)
                complete = number * 24 == info.file_size
                result["member"] = {
                    "name": info.filename, "uncompressed_bytes_declared_by_zip": info.file_size,
                    "selected_rows": number, "scope": "FULL_MEMBER" if complete else "PREFIX_ONLY",
                    "unread_tail_interpreted": False,
                }
                continuous = audit_pass(archive, info, number, complete, adapter, obj["id"], "continuous")
                chunked = audit_pass(archive, info, number, complete, adapter, obj["id"], "chunked")
                comparison = Gate()
                # Both passages compare raw rows directly.  Canonical digests
                # are the bounded transcript of their full packet prefixes.
                keys = [key for key in continuous if key != "gates"]
                for key in keys:
                    comparison.check(continuous[key] == chunked[key],
                                     "CONTINUOUS_CHUNKED_" + key.upper(), obj["id"])
                result["audit"] = {key: continuous[key] for key in keys}
                result["member"]["full_member_crc_verified_each_pass"] = complete
                result["member"]["passes"] = 2
                result["gates"] = {}
                for gate in GATES[1:]:
                    parts = [continuous["gates"][gate], chunked["gates"][gate]]
                    if gate == GATES[2]:
                        parts.append(comparison.report())
                    result["gates"][gate] = combine_gate_reports(parts)
        except DataViolation as exc:
            result["qualification_failures"].append(str(exc))
        except (zipfile.BadZipFile, zipfile.LargeZipFile, zlib.error, EOFError, UnicodeDecodeError):
            result["qualification_failures"].append("CORRUPT_ZIP_STRUCTURE_OR_CONTENT")
        except NotImplementedError:
            result["qualification_failures"].append("UNSUPPORTED_ZIP_COMPRESSION")
    if result["qualification_failures"]:
        result["qualification"] = "QUALIFICATION_FAILED"
        result["gates"] = {gate: {"status": "NOT_EVALUATED"} for gate in GATES[1:]}
    return result


def claim_status(gates, names, qualification):
    if any(gates[name]["status"] == "FIRED" for name in names):
        return "FIRED"
    if qualification != "QUALIFIED" or any(gates[name]["status"] != "PASS" for name in names):
        return "NOT_EVALUATED"
    return "CONFIRMED"


def main():
    require(len(sys.argv) == 1, "ARGUMENTS_NOT_ACCEPTED")
    dependencies = load_dependencies()
    source = import_pinned("_twistj_nist_source_qualification", dependencies["source_verifier"][0])
    adapter = import_pinned("_twistj_nist_local_adapter", dependencies["adapter"][0])
    try:
        source_manifest, notice = source.load_source()
        require(source.RECORD_LIMIT == RECORD_CAP
                and source_manifest["record_cap_per_object"] == RECORD_CAP,
                "INHERITED_RECORD_CAP_CHANGED")
        synthetic = synthetic_audit(adapter)
        reports = []
        cache_hint = os.environ.get("TWISTJ_NIST_CACHE_DIR")
        cache = Path(cache_hint) if cache_hint else None
        with tempfile.TemporaryDirectory(prefix="twistj-nist-local-") as directory:
            temporary = Path(directory)
            (temporary / "NOTICE.md").write_bytes(notice)
            for obj in source_manifest["objects"]:
                cached = cache / (obj["id"] + ".zip") if cache is not None else None
                if cached is not None and cached.exists():
                    path = cached
                else:
                    path = temporary / (obj["id"] + ".zip")
                    source.download_archive(obj, path)
                reports.append(analyse_archive(path, obj, source, adapter))
    except source.FatalError as exc:
        raise FatalError("INHERITED_" + str(exc)) from exc
    gates = {GATES[0]: synthetic["gate"]}
    for gate in GATES[1:]:
        gates[gate] = combine_gate_reports([report["gates"][gate] for report in reports])
    qualification = ("QUALIFIED" if all(report["qualification"] == "QUALIFIED" for report in reports)
                     else "QUALIFICATION_FAILED")
    output = {
        "schema": "nist-local-observed-interval-audit/1",
        "dependencies_sha256": MANIFEST_SHA256,
        "source_manifest_sha256": dependencies["source_manifest"][1]["sha256"],
        "adapter_sha256": dependencies["adapter"][1]["sha256"],
        "notice_sha256": dependencies["notice"][1]["sha256"],
        "data_qualification": qualification,
        "claim_A": claim_status(gates, (GATES[0], GATES[1], GATES[3]), qualification),
        "claim_B": claim_status(gates, (GATES[0], GATES[2], GATES[3]), qualification),
        "gates": gates, "synthetic": synthetic, "objects": reports,
        "record_cap_per_object": RECORD_CAP, "chunk_cycle": list(CHUNK_CYCLE),
        "packet_serialization": "compact sorted-key ASCII JSON plus LF per packet",
        "raw_serialization": "<QQQ in original row ownership order; nonowning references omitted",
        "pending_snapshot_is_not_an_emitted_event": True,
        "physical_trial_calibrated_no_click_bell_or_born_claim": False,
        "prior_source_prefix_exposure_declared": True,
    }
    print(json.dumps(output, sort_keys=True, indent=2, ensure_ascii=True, allow_nan=False))


if __name__ == "__main__":
    try:
        main()
    except FatalError as exc:
        sys.stderr.write("VERIFIER_ERROR " + str(exc) + "\n")
        sys.exit(2)
    except OSError:
        sys.stderr.write("VERIFIER_ERROR ENVIRONMENT_IO_FAILED\n")
        sys.exit(2)
    except Exception as exc:
        sys.stderr.write("VERIFIER_ERROR INTERNAL_" + type(exc).__name__ + "\n")
        sys.exit(2)
