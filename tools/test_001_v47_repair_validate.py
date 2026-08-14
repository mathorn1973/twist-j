#!/usr/bin/env python3
"""Prep-only v47 repair/validator after the deterministic builder.

The builder has already produced the candidate content bytes before its ledger
check. This test preserves historical seq1/seq2 and makes only the current
seq3 snapshot agree byte-for-byte with the current EVIDENCE row, then reruns
the repository ledger and Canon checks and emits the transport package.
Removed before the final release content commit.
"""

from __future__ import annotations

import csv
from pathlib import Path
import subprocess
import sys
import unittest

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
CANON = ROOT / "canon"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import test_000_v47_builder as builder  # noqa: E402


def read_tsv(path: Path):
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or ()), list(reader)


def write_tsv(path: Path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=fields, delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def run_checked(*args: str) -> str:
    result = subprocess.run(
        [sys.executable, *args], cwd=ROOT, capture_output=True, text=True
    )
    if result.returncode:
        raise AssertionError(
            f"command failed: {' '.join(args)}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )
    return result.stdout


class V47RepairValidate(unittest.TestCase):
    def test_repair_latest_history_snapshot_and_validate(self):
        e_fields, evidence = read_tsv(CANON / "EVIDENCE.tsv")
        self.assertTrue(e_fields)
        current = next(row for row in evidence if row["claim_id"] == builder.CLAIM)
        expected = (
            current["evidence_id"],
            current["location"],
            current["sha256"],
        )
        self.assertEqual(
            expected,
            (builder.EVIDENCE_ID, builder.PROBE, builder.BUNDLE_SHA),
        )

        h_fields, history = read_tsv(CANON / "HISTORY.tsv")
        own = sorted(
            (row for row in history if row["claim_id"] == builder.CLAIM),
            key=lambda row: int(row["event_sequence"]),
        )
        seq = [int(row["event_sequence"]) for row in own]
        if seq == [1, 2]:
            row = {field: "" for field in h_fields}
            row.update(
                event_id="CANON47-STATUS-TM-SYM2-PHYSICAL-MEASURE-3",
                event_sequence="3",
                event_date="2026-08-14",
                release="canon-v47",
                claim_id=builder.CLAIM,
                event_type="STATUS_CHANGE",
                previous_status="O",
                new_status="D",
                scope_sha256=builder.SCOPE_SHA,
                evidence_id=expected[0],
                evidence_location=expected[1],
                evidence_sha256=expected[2],
                rationale=builder.RATIONAL,
            )
            history.append(row)
        elif seq == [1, 2, 3]:
            row = own[-1]
            self.assertEqual(row["event_id"], "CANON47-STATUS-TM-SYM2-PHYSICAL-MEASURE-3")
            row.update(
                event_date="2026-08-14",
                release="canon-v47",
                event_type="STATUS_CHANGE",
                previous_status="O",
                new_status="D",
                scope_sha256=builder.SCOPE_SHA,
                evidence_id=expected[0],
                evidence_location=expected[1],
                evidence_sha256=expected[2],
                rationale=builder.RATIONAL,
            )
        else:
            self.fail(f"unexpected history chain {seq}")
        write_tsv(CANON / "HISTORY.tsv", h_fields, history)

        ledger = run_checked(str(TOOLS / "check_ledger.py"))
        self.assertIn("claims=241", ledger)
        self.assertIn("items=259", ledger)
        self.assertIn("dependencies=384", ledger)
        self.assertIn("evidence=241", ledger)
        self.assertIn("history=756", ledger)
        self.assertIn("gates=10", ledger)

        builder.temporary_release_form()
        canon_check = run_checked(str(TOOLS / "check_canon.py"))
        self.assertIn("CANON PASS v47 claims=241", canon_check)

        print("V47_REPAIR_LEDGER=" + ledger.strip())
        print("V47_REPAIR_CANON=" + canon_check.strip())
        builder.print_transport_package()


if __name__ == "__main__":
    unittest.main()
