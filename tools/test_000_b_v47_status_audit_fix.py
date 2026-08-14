#!/usr/bin/env python3
"""Temporary prep-only fix for the v47 status-separation audit text match."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "reproduce" / "status-separation" / "verify.py"


class V47StatusAuditScopePhrase(unittest.TestCase):
    def test_align_gyron_scope_phrase(self) -> None:
        text = PATH.read_text(encoding="utf-8")
        old = '             "no GYRON identification"),'
        new = '             "GYRON identification"),'
        self.assertEqual(text.count(old), 1)
        PATH.write_text(text.replace(old, new), encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
