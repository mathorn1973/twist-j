#!/usr/bin/env python3
"""No-argument deterministic verifier for the committed mobility result."""

from __future__ import annotations

import re
from pathlib import Path
import subprocess
import sys


PIN_RE = re.compile(r"^pin_commit: ([0-9a-f]{40})$", re.MULTILINE)
RECEIPT_RE = re.compile(
    r"^pin_receipt: (https://github\.com/mathorn1973/twist-j/issues/756#issuecomment-[0-9]+)$",
    re.MULTILINE,
)


def main() -> int:
    if len(sys.argv) != 1:
        print("VERIFY_ERROR expected_no_arguments", file=sys.stderr)
        return 64
    base = Path(__file__).resolve().parent
    try:
        expected_path = base / "EXPECTED.txt"
        if expected_path.is_symlink() or not expected_path.is_file():
            raise RuntimeError("EXPECTED.txt regular-file contract")
        expected = expected_path.read_bytes()
        if b"\r" in expected or not expected.endswith(b"\n"):
            raise RuntimeError("EXPECTED.txt newline contract")
        expected.decode("ascii")
        run_path = base / "RUN.md"
        if run_path.is_symlink() or not run_path.is_file():
            raise RuntimeError("RUN.md regular-file contract")
        run_raw = run_path.read_bytes()
        if b"\r" in run_raw or not run_raw.endswith(b"\n"):
            raise RuntimeError("RUN.md newline contract")
        run_text = run_raw.decode("ascii")
        pin_matches = PIN_RE.findall(run_text)
        receipt_matches = RECEIPT_RE.findall(run_text)
        if len(pin_matches) != 1 or len(receipt_matches) != 1:
            raise RuntimeError("RUN.md pin fields")
        completed = subprocess.run(
            (
                sys.executable,
                "-B",
                str(base / "qualification_run.py"),
                "--replay",
                "--pin-commit",
                pin_matches[0],
                "--pin-receipt",
                receipt_matches[0],
            ),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            cwd=base.parent.parent,
        )
        if completed.returncode or completed.stderr:
            raise RuntimeError(
                f"replay process rc={completed.returncode} stderr={completed.stderr!r}"
            )
        if b"\r" in completed.stdout or not completed.stdout.endswith(b"\n"):
            raise RuntimeError("replay stdout newline contract")
        completed.stdout.decode("ascii")
        if completed.stdout != expected:
            raise RuntimeError("replay stdout differs from EXPECTED.txt")
        sys.stdout.buffer.write(completed.stdout)
        return 0
    except (OSError, RuntimeError, UnicodeError, subprocess.SubprocessError) as error:
        print(f"VERIFY_ERROR {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
