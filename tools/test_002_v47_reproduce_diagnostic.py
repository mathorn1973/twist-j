#!/usr/bin/env python3
"""Temporary prep-only diagnostic for the v47 reproduction sweep."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
BASE = "2e4194fff467d91117d4884b502a05d1fd2d40e8"


class V47ReproduceDiagnostic(unittest.TestCase):
    def test_status_separation_direct(self) -> None:
        result = subprocess.run(
            [sys.executable, "reproduce/status-separation/verify.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        if result.returncode:
            lines = (result.stdout + "\n" + result.stderr).splitlines()
            self.fail("V47_STATUS_SEPARATION_FAILURE\n" + "\n".join(lines[-45:]))
        self.assertIn("RESULT 32/32 ALL PASS", result.stdout)

    def test_full_reproduction_sweep(self) -> None:
        result = subprocess.run(
            [sys.executable, "tools/check_reproduce.py", "--base", BASE],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        if result.returncode:
            lines = (result.stdout + "\n" + result.stderr).splitlines()
            tail = "\n".join(lines[-30:])
            self.fail("V47_REPRODUCE_FAILURE\n" + tail)
        self.assertIn("REPRODUCE FULL SWEEP canon change", result.stdout)


if __name__ == "__main__":
    unittest.main()
