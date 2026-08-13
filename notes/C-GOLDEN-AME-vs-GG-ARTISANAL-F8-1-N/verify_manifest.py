#!/usr/bin/env python3
"""Verify every entry in MANIFEST.sha256 using only the standard library."""

from hashlib import sha256
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
manifest = ROOT / "MANIFEST.sha256"
failures = []
count = 0
for raw_line in manifest.read_text("utf-8").splitlines():
    if not raw_line:
        continue
    expected, relative = raw_line.split("  ", 1)
    path = ROOT / relative
    actual = sha256(path.read_bytes()).hexdigest() if path.is_file() else "MISSING"
    count += 1
    if actual != expected:
        failures.append((relative, expected, actual))

if failures:
    for relative, expected, actual in failures:
        print(f"FAIL {relative} expected={expected} actual={actual}")
    sys.exit(1)
print(f"MANIFEST_PASS files={count}")
