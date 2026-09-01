#!/usr/bin/env python3
"""Fail-closed L<=4 trajectory parity fixture for crosscheck2_engine.

The fixture compares the successor executable directly with the pinned
P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1 executable on two nonformal
development trajectories.  It never constructs an L=6 or L=8 lattice.  The
eight formal seed tokens are submitted only to the successor development CLI,
which must reject them before SectorEngine construction.
"""

from __future__ import annotations

import argparse
import base64
import binascii
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from typing import Any, Sequence


EXPECTED_REPORT_SHA256 = "2f1f1a0f38dd63c7054d19896e06486dc711b4d098fc9ba5d8e82837e67a97ba"
DOMAIN = "photon-z5-dual-mobility-qualification-1"
ENCODING = "2bit-site-major-pairs-v1"
FORMAL_SEEDS = (
    "0xbc2def7bcee975913c3b3b3999e83ad3",
    "0x1a7ab1ad0011b62c04dcf48da9be3403",
    "0x5f0f36673dd145755b9a49e703aef3d6",
    "0x2b19daecb5c523f30bee3be7c047eb40",
    "0x46ba01f80aec780ff9cc8b7e876c700c",
    "0x2e0ccaa683e5f39f1237f05193b299c4",
    "0xf8f631709b4b9ce34f8a658bef3e1d0a",
    "0xfcd563ecc8bf8179b96c20db2c388307",
)
SPECS = (
    (3, "cold", "0x000102030405060708090a0b0c0d0e0f", 12, 24, 3),
    (4, "stratified", "0x0f0e0d0c0b0a09080706050403020100", 16, 24, 4),
)
SUCCESSOR_RUN_ONLY = {
    "state_encoding",
    "state_packed_bytes",
    "state_unpacked_bytes",
}
SUCCESSOR_CHECKPOINT_ONLY = {"packed_state_sha256", "state_2bit_base64"}
SUCCESSOR_SELFTEST_ONLY = {"formal_firewall", "state_2bit_base64"}
PREDECESSOR_SUMMARY_ONLY = {
    "distinct_nonzero_current_hashes",
    "nonzero_current_hashes",
    "state_hashes",
}
SUCCESSOR_SUMMARY_ONLY = {
    "distinct_checkpoint_nonzero_current_hashes",
    "checkpoint_nonzero_current_hashes",
    "checkpoint_state_hashes",
}


class FixtureError(RuntimeError):
    pass


def strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise FixtureError(f"duplicate_json_key:{key}")
        result[key] = value
    return result


def parse_jsonl(payload: bytes, label: str) -> list[dict[str, Any]]:
    if not payload.endswith(b"\n") or b"\r" in payload or b"\0" in payload:
        raise FixtureError(f"noncanonical_jsonl_bytes:{label}")
    records: list[dict[str, Any]] = []
    for number, raw in enumerate(payload.splitlines(), 1):
        try:
            text = raw.decode("ascii")
            value = json.loads(text, object_pairs_hook=strict_object)
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise FixtureError(f"invalid_json:{label}:{number}") from error
        if not isinstance(value, dict):
            raise FixtureError(f"record_not_object:{label}:{number}")
        records.append(value)
    return records


def invoke(executable: Path, arguments: Sequence[str], label: str) -> bytes:
    try:
        completed = subprocess.run(
            [str(executable), *arguments],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=120,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        raise FixtureError(f"engine_invocation_failed:{label}") from error
    if completed.returncode != 0 or completed.stderr:
        raise FixtureError(
            f"engine_failed:{label}:returncode={completed.returncode}:"
            f"stderr={completed.stderr.decode('ascii', 'backslashreplace').strip()}"
        )
    return completed.stdout


def require_rejection(executable: Path, arguments: Sequence[str], message: str) -> None:
    try:
        completed = subprocess.run(
            [str(executable), *arguments],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        raise FixtureError(f"firewall_invocation_failed:{message}") from error
    expected = f"ERROR {message}\n".encode("ascii")
    stderr = completed.stderr.replace(b"\r\n", b"\n")
    if b"\r" in stderr or completed.returncode != 2 or completed.stdout or stderr != expected:
        raise FixtureError(f"firewall_rejection_mismatch:{message}")


def run_arguments(
    L: int,
    start: str,
    seed: str,
    warm: int,
    checkpoints: int,
    thin: int,
) -> list[str]:
    return [
        "--development",
        "--L",
        str(L),
        "--seed",
        seed,
        "--start",
        start,
        "--warm-bottom",
        str(warm),
        "--checkpoints",
        str(checkpoints),
        "--thin",
        str(thin),
        "--validation-stride",
        str(thin),
        "--transition-cap",
        "2000000",
    ]


def shared(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    keys = set(left) & set(right)
    for key in keys:
        if left[key] != right[key]:
            raise FixtureError(f"trajectory_field_mismatch:{key}")
    return {key: left[key] for key in sorted(keys)}


def decode_frame(record: dict[str, Any], L: int, checkpoint: int) -> bytes:
    token = record.get("state_2bit_base64")
    if not isinstance(token, str) or not token.isascii():
        raise FixtureError(f"state_base64_type:L{L}:{checkpoint}")
    try:
        packed = base64.b64decode(token, validate=True)
    except (ValueError, binascii.Error) as error:
        raise FixtureError(f"state_base64_decode:L{L}:{checkpoint}") from error
    if base64.b64encode(packed).decode("ascii") != token:
        raise FixtureError(f"state_base64_noncanonical:L{L}:{checkpoint}")
    count = 6 * L**4
    if len(packed) != (count + 3) // 4:
        raise FixtureError(f"state_packed_length:L{L}:{checkpoint}")
    if count % 4 and packed[-1] & ((1 << (2 * (4 - count % 4))) - 1):
        raise FixtureError(f"state_tail_bits:L{L}:{checkpoint}")
    unpacked = bytearray()
    residues = (0, 1, 4)
    for index in range(count):
        code = (packed[index // 4] >> (6 - 2 * (index % 4))) & 3
        if code == 3:
            raise FixtureError(f"state_forbidden_code:L{L}:{checkpoint}")
        unpacked.append(residues[code])
    if hashlib.sha256(packed).hexdigest() != record.get("packed_state_sha256"):
        raise FixtureError(f"packed_state_sha256:L{L}:{checkpoint}")
    if hashlib.sha256(unpacked).hexdigest() != record.get("state_sha256"):
        raise FixtureError(f"state_sha256:L{L}:{checkpoint}")
    return packed


def parity_report(successor: Path, predecessor: Path) -> bytes:
    successor_selftest = parse_jsonl(invoke(successor, ["--selftest"], "successor_selftest"), "successor_selftest")
    predecessor_selftest = parse_jsonl(invoke(predecessor, ["--selftest"], "predecessor_selftest"), "predecessor_selftest")
    if len(successor_selftest) != 1 or successor_selftest[0].get("type") != "selftest":
        raise FixtureError("successor_selftest_schema")
    if len(predecessor_selftest) != 1 or predecessor_selftest[0].get("type") != "selftest":
        raise FixtureError("predecessor_selftest_schema")
    if set(successor_selftest[0]) - set(predecessor_selftest[0]) != SUCCESSOR_SELFTEST_ONLY:
        raise FixtureError("selftest_successor_fields")
    if set(predecessor_selftest[0]) - set(successor_selftest[0]):
        raise FixtureError("selftest_predecessor_fields")
    shared(predecessor_selftest[0], successor_selftest[0])
    if any(successor_selftest[0].get(key) != "PASS" for key in SUCCESSOR_SELFTEST_ONLY):
        raise FixtureError("successor_selftest_extension_failed")

    lines = ["ENGINE_SELFTEST status=PASS"]
    for L, start, seed, warm, checkpoint_count, thin in SPECS:
        arguments = run_arguments(L, start, seed, warm, checkpoint_count, thin)
        old_records = parse_jsonl(invoke(predecessor, arguments, f"predecessor_L{L}"), f"predecessor_L{L}")
        new_records = parse_jsonl(invoke(successor, arguments, f"successor_L{L}"), f"successor_L{L}")
        if len(old_records) != checkpoint_count + 2 or len(new_records) != checkpoint_count + 2:
            raise FixtureError(f"record_count:L{L}")
        if old_records[0].get("type") != "run" or new_records[0].get("type") != "run":
            raise FixtureError(f"run_record:L{L}")
        if old_records[-1].get("type") != "summary" or new_records[-1].get("type") != "summary":
            raise FixtureError(f"summary_record:L{L}")
        if set(new_records[0]) - set(old_records[0]) != SUCCESSOR_RUN_ONLY:
            raise FixtureError(f"run_successor_fields:L{L}")
        if set(old_records[0]) - set(new_records[0]):
            raise FixtureError(f"run_predecessor_fields:L{L}")
        if new_records[0].get("bitstream_domain") != DOMAIN:
            raise FixtureError(f"bitstream_domain:L{L}")
        if new_records[0].get("state_encoding") != ENCODING:
            raise FixtureError(f"state_encoding:L{L}")
        if new_records[0].get("state_unpacked_bytes") != 6 * L**4:
            raise FixtureError(f"state_unpacked_bytes:L{L}")
        if new_records[0].get("state_packed_bytes") != (6 * L**4 + 3) // 4:
            raise FixtureError(f"state_packed_bytes:L{L}")

        common_checkpoints: list[dict[str, Any]] = []
        packed_stream = hashlib.sha256()
        checkpoint_hashes: set[str] = set()
        nonzero_hashes: set[str] = set()
        for index in range(1, checkpoint_count + 1):
            old = old_records[index]
            new = new_records[index]
            if old.get("type") != "checkpoint" or new.get("type") != "checkpoint":
                raise FixtureError(f"checkpoint_type:L{L}:{index}")
            if old.get("checkpoint") != index or new.get("checkpoint") != index:
                raise FixtureError(f"checkpoint_index:L{L}:{index}")
            if set(new) - set(old) != SUCCESSOR_CHECKPOINT_ONLY:
                raise FixtureError(f"checkpoint_successor_fields:L{L}:{index}")
            if set(old) - set(new):
                raise FixtureError(f"checkpoint_predecessor_fields:L{L}:{index}")
            common_checkpoints.append(shared(old, new))
            packed_stream.update(decode_frame(new, L, index))
            checkpoint_hashes.add(str(new["state_sha256"]))
            if new.get("current_nonzero") == 1:
                nonzero_hashes.add(str(new["current_hash"]))

        old_summary = old_records[-1]
        new_summary = new_records[-1]
        if set(old_summary) - set(new_summary) != PREDECESSOR_SUMMARY_ONLY:
            raise FixtureError(f"summary_predecessor_fields:L{L}")
        if set(new_summary) - set(old_summary) != SUCCESSOR_SUMMARY_ONLY:
            raise FixtureError(f"summary_successor_fields:L{L}")
        common_payload = {
            "run": shared(old_records[0], new_records[0]),
            "checkpoints": common_checkpoints,
            "summary": shared(old_summary, new_summary),
        }
        if new_summary.get("checkpoint_state_hashes") != len(checkpoint_hashes):
            raise FixtureError(f"checkpoint_state_hashes:L{L}")
        if new_summary.get("checkpoint_nonzero_current_hashes") != sorted(nonzero_hashes):
            raise FixtureError(f"checkpoint_nonzero_current_hashes:L{L}")
        if new_summary.get("distinct_checkpoint_nonzero_current_hashes") != len(nonzero_hashes):
            raise FixtureError(f"distinct_checkpoint_nonzero_current_hashes:L{L}")
        common_bytes = json.dumps(common_payload, sort_keys=True, separators=(",", ":")).encode("ascii")
        lines.append(
            f"ENGINE_PARITY L={L} start={start} checkpoints={checkpoint_count} "
            f"common_sha256={hashlib.sha256(common_bytes).hexdigest()} "
            f"packed_stream_sha256={packed_stream.hexdigest()} status=PASS"
        )

    minimal = run_arguments(3, "cold", FORMAL_SEEDS[0], 0, 1, 1)
    for seed in FORMAL_SEEDS:
        arguments = minimal.copy()
        arguments[arguments.index("--seed") + 1] = seed
        require_rejection(successor, arguments, "development_forbids_formal_seed")
    for alias in (FORMAL_SEEDS[0][2:], "0X" + FORMAL_SEEDS[0][2:].upper()):
        arguments = minimal.copy()
        arguments[arguments.index("--seed") + 1] = alias
        require_rejection(successor, arguments, "development_forbids_formal_seed")
    require_rejection(
        successor,
        run_arguments(6, "cold", "0x00000000000000000000000000000001", 0, 1, 1),
        "development_L_must_be_3_or_4",
    )
    require_rejection(
        successor,
        run_arguments(8, "cold", "0x00000000000000000000000000000001", 0, 1, 1),
        "development_L_must_be_3_or_4",
    )
    lines.append("ENGINE_FIREWALL formal_seed_values=8 alias_spellings=2 development_L_max=4 status=PASS")
    return ("\n".join(lines) + "\n").encode("ascii")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", type=Path, required=True)
    parser.add_argument("--qualification-engine", type=Path, required=True)
    arguments = parser.parse_args(argv)
    for label, path in (("engine", arguments.engine), ("qualification_engine", arguments.qualification_engine)):
        if not path.is_file():
            raise FixtureError(f"missing_{label}:{path}")
    report = parity_report(arguments.engine.resolve(), arguments.qualification_engine.resolve())
    observed_sha256 = hashlib.sha256(report).hexdigest()
    if observed_sha256 != EXPECTED_REPORT_SHA256:
        raise FixtureError(
            "fixture_expected_mismatch:"
            f"actual_sha256={observed_sha256}:"
            f"expected_sha256={EXPECTED_REPORT_SHA256}"
        )
    sys.stdout.buffer.write(report)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except FixtureError as error:
        print(f"ERROR {error}", file=sys.stderr)
        raise SystemExit(2)
