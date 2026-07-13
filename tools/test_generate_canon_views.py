#!/usr/bin/env python3
"""Tests for deterministic generated Canon views."""

from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from tools.generate_canon_views import generated_views
from tools.test_check_ledger import LedgerFixture


class GeneratedViewTests(unittest.TestCase):
    def test_views_are_registry_derived(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = LedgerFixture(root)
            fixture.write()
            (root / "reproduce").mkdir()
            views = generated_views(root)
            self.assertIn("O-CLAIM [O]: open fixture gate", views["FRONTIER.md"])
            self.assertIn("T-CLAIM [T]: exact fixture theorem", views["CORE_CLAIMS.md"])
            self.assertIn("claims\t2", views["STATUS_COUNTS.tsv"])
            self.assertIn("live_H_O\t1", views["STATUS_COUNTS.tsv"])

    def test_views_are_byte_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = LedgerFixture(root)
            fixture.write()
            (root / "reproduce").mkdir()
            self.assertEqual(generated_views(root), generated_views(root))


if __name__ == "__main__":
    unittest.main()
