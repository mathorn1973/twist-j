#!/usr/bin/env python3
"""Tests for deterministic generated Canon views."""

from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from tools.generate_canon_views import apply_views, generated_views
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
            self.assertNotIn("two_arch_claims_complete", views["STATUS_COUNTS.tsv"])
            self.assertNotIn("two_arch_claims_pending", views["STATUS_COUNTS.tsv"])
            self.assertIn("Registry snapshot: 2 claims", views["CHANGELOG_COUNTS.md"])

    def test_views_are_byte_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = LedgerFixture(root)
            fixture.write()
            (root / "reproduce").mkdir()
            self.assertEqual(generated_views(root), generated_views(root))

    def test_apply_replaces_only_declared_views(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = LedgerFixture(root)
            fixture.write()
            (root / "reproduce").mkdir()
            (root / "canon" / "FRONTIER.md").write_text("manual\n", encoding="utf-8")
            (root / "canon" / "CORE.md").write_text(
                "# Core\n\nStable orientation results:\n\nmanual\n\nTime is a counter.\n",
                encoding="utf-8",
            )
            (root / "canon" / "CHANGELOG.md").write_text(
                "# Changelog\n\n## Public Canon v1\n\nNarrative.\n",
                encoding="utf-8",
            )
            views = generated_views(root)
            apply_views(root, views)
            self.assertEqual(
                (root / "canon" / "FRONTIER.md").read_text(encoding="utf-8"),
                views["FRONTIER.md"],
            )
            self.assertIn(views["CORE_CLAIMS.md"].rstrip(), (root / "canon" / "CORE.md").read_text(encoding="utf-8"))
            self.assertIn(views["CHANGELOG_COUNTS.md"].rstrip(), (root / "canon" / "CHANGELOG.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
