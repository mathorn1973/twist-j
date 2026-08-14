#!/usr/bin/env python3
"""Temporary prep-only Registry patch for Public Canon v47.

Runs before the v47 builder in unittest discovery, patches exactly one evidence
field in the workspace, and emits a compressed byte package. Removed before the
final content tree is frozen.
"""

from __future__ import annotations

import base64
import csv
import hashlib
import json
from pathlib import Path
import unittest
import zlib

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "canon" / "REGISTRY.tsv"
CLAIM = "TM-SYM2-PHYSICAL-MEASURE"
PROBE = "probes/P-TM-SYM2-BORN-HALVING-1"
SCOPE_SHA = "f9ad8efe676d58a167f84d3ccfb873e511945fd0a7c301a1113aa275032278d0"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class V47RegistryEvidencePatch(unittest.TestCase):
    def test_patch_registry_evidence(self) -> None:
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
            writer = csv.DictWriter(
                handle, fieldnames=fields, delimiter="\t", lineterminator="\n"
            )
            writer.writeheader()
            writer.writerows(rows)
        data = PATH.read_bytes()
        payload = json.dumps(
            {"canon/REGISTRY.tsv": base64.b64encode(data).decode("ascii")},
            sort_keys=True,
            separators=(",", ":"),
        ).encode("ascii")
        packed = base64.b64encode(zlib.compress(payload, 9)).decode("ascii")
        print(f"V47_REGISTRY_BYTES={len(data)}")
        print(f"V47_REGISTRY_SHA256={sha256(data)}")
        print("V47_REGISTRY_PACKAGE_BEGIN")
        for i in range(0, len(packed), 1600):
            print(packed[i:i+1600])
        print("V47_REGISTRY_PACKAGE_END")


if __name__ == "__main__":
    unittest.main()
