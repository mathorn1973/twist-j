#!/usr/bin/env python3
"""Reproduce archived, result-exposed evidence; no new scientific gate."""
from __future__ import annotations

import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
PAIRS = (
    ("audit.py", "ACTUAL.txt"),
    ("conjugation_audit.py", "CONJUGATION-ACTUAL.txt"),
    ("supplement.py", "SUPPLEMENT-ACTUAL.txt"),
)


def main() -> int:
    for line in (ROOT / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        digest, name = line.split("  ", 1)
        if Path(name).name != name:
            raise ValueError("Manifest entries must be local basenames")
        if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != digest:
            raise RuntimeError(f"Manifest mismatch: {name}")
    print("PUBLICATION MANIFEST PASS", flush=True)
    with tempfile.TemporaryDirectory(prefix="seam41-replay-") as directory:
        work = Path(directory)
        for script, _ in PAIRS:
            shutil.copyfile(ROOT / script, work / script)
        for script, expected in PAIRS:
            completed = subprocess.run(
                [sys.executable, "-B", script], cwd=work, capture_output=True,
                timeout=300, check=False,
            )
            if completed.returncode != 0 or completed.stderr:
                raise RuntimeError(
                    f"{script}: exit={completed.returncode}; "
                    f"stderr_bytes={len(completed.stderr)}"
                )
            if completed.stdout != (ROOT / expected).read_bytes():
                raise RuntimeError(f"{script}: archived stdout mismatch")
            print(f"REPLAY PASS {script} bytes={len(completed.stdout)}", flush=True)
    print("STATUS NON-CANONICAL; reproduction only; no independent confirmation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
