#!/usr/bin/env python3
"""Temporary prep-only emitter for byte-exact v47 generated content."""

from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path
import zlib
import unittest

ROOT = Path(__file__).resolve().parents[1]
FILES = (
    "canon/CANON.md",
    "canon/CORE.md",
    "canon/FRONTIER.md",
    "canon/CHANGELOG.md",
    "canon/SHA256SUMS",
    "canon/EVIDENCE.tsv",
    "canon/HISTORY.tsv",
    "canon/STATUS_COUNTS.tsv",
    "reproduce/status-separation/verify.py",
    "reproduce/status-separation/EXPECTED.txt",
    "reproduce/status-separation/README.md",
)


class V47GeneratedPackage(unittest.TestCase):
    def test_emit_generated_package(self) -> None:
        payload = {}
        manifest = {}
        for relative in FILES:
            data = (ROOT / relative).read_bytes()
            payload[relative] = data.decode("utf-8")
            manifest[relative] = {
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
            }
        raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        packed = zlib.compress(raw, 9)
        encoded = base64.b64encode(packed).decode("ascii")
        chunk_size = 7000
        chunks = [encoded[i:i + chunk_size] for i in range(0, len(encoded), chunk_size)]
        meta = {
            "files": manifest,
            "raw_bytes": len(raw),
            "raw_sha256": hashlib.sha256(raw).hexdigest(),
            "packed_bytes": len(packed),
            "packed_sha256": hashlib.sha256(packed).hexdigest(),
            "chunks": len(chunks),
        }
        meta_text = json.dumps(meta, sort_keys=True, separators=(",", ":"))
        print(f"::notice title=V47_PACKAGE_META::{meta_text}")
        for index, chunk in enumerate(chunks, start=1):
            print(f"::notice title=V47_PACKAGE_{index:04d}_OF_{len(chunks):04d}::{chunk}")
        self.assertLessEqual(len(chunks), 45)
        self.fail("V47_PACKAGE_EMITTED")


if __name__ == "__main__":
    unittest.main()
