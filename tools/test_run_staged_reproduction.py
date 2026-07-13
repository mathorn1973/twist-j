#!/usr/bin/env python3
"""Focused tests for atomic cross-architecture batch selection."""

from __future__ import annotations

import csv
from pathlib import Path
import tempfile
import unittest

from tools.run_staged_reproduction import (
    EVIDENCE_FIELDS,
    two_architecture_reproductions,
)


class StagedBatchTests(unittest.TestCase):
    def test_selects_unique_two_architecture_reproductions(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "canon" / "EVIDENCE.tsv"
            path.parent.mkdir(parents=True)
            rows = [
                {
                    "claim_id": "T-A", "evidence_id": "EV-T-A",
                    "evidence_kind": "REPRODUCTION", "location": "reproduce/zeta",
                    "sha256": "0" * 64, "hash_mode": "bundle-manifest-sha256-v1",
                    "architecture_requirement": "two-architecture",
                },
                {
                    "claim_id": "T-B", "evidence_id": "EV-T-B",
                    "evidence_kind": "REPRODUCTION", "location": "reproduce/zeta",
                    "sha256": "1" * 64, "hash_mode": "bundle-manifest-sha256-v1",
                    "architecture_requirement": "two-architecture",
                },
                {
                    "claim_id": "C-C", "evidence_id": "EV-C-C",
                    "evidence_kind": "REPRODUCTION", "location": "reproduce/alpha",
                    "sha256": "2" * 64, "hash_mode": "bundle-manifest-sha256-v1",
                    "architecture_requirement": "one-architecture",
                },
            ]
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(
                    handle, delimiter="\t", fieldnames=EVIDENCE_FIELDS,
                    lineterminator="\n",
                )
                writer.writeheader()
                writer.writerows(rows)
            self.assertEqual(two_architecture_reproductions(root), ["zeta"])


if __name__ == "__main__":
    unittest.main()
