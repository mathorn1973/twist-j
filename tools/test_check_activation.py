#!/usr/bin/env python3
"""Focused tests for activation-only blockers."""

from __future__ import annotations

import csv
from pathlib import Path
import tempfile
import unittest

from tools.check_activation import (
    EVIDENCE_FIELDS,
    activation_delta_blockers,
    architecture_blockers,
    artifact_blockers,
    post_content_path_allowed,
    publication_tag_blocker,
    release_identity,
    view_blockers,
)
from tools.generate_canon_views import generated_views
from tools.test_check_ledger import LedgerFixture


def write_tsv(path: Path, fields: tuple[str, ...], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


class ActivationTests(unittest.TestCase):
    def test_release_identity_uses_positive_whole_canon_number(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "canon").mkdir()
            (root / "canon" / "CANON.md").write_text(
                "# TWIST-J Public Canon v12\n", encoding="utf-8"
            )
            self.assertEqual(
                release_identity(root),
                ("12", "Public Canon v12", "canon-v12"),
            )
            (root / "canon" / "CANON.md").write_text(
                "# TWIST-J Public Canon v12.1\n", encoding="utf-8"
            )
            with self.assertRaisesRegex(ValueError, "whole-number title"):
                release_identity(root)

    def test_publication_tag_must_equal_declared_whole_number_tag(self) -> None:
        self.assertIsNone(publication_tag_blocker("canon-v2", "canon-v2"))
        self.assertIn(
            "invalid", publication_tag_blocker("canon-v2", "canon-v2.1") or ""
        )
        self.assertIn(
            "differs", publication_tag_blocker("canon-v2", "canon-v3") or ""
        )
        self.assertIn(
            "requires", publication_tag_blocker("canon-v2", None) or ""
        )

    def test_active_release_delta_is_exactly_three_metadata_files(self) -> None:
        exact = ["STATUS.md", "README.md", "CITATION.cff"]
        self.assertEqual(activation_delta_blockers(exact, dry_run=False), [])
        self.assertEqual(activation_delta_blockers([], dry_run=True), [])
        blockers = activation_delta_blockers(exact + ["canon/CANON.md"], dry_run=False)
        self.assertIn("extra canon/CANON.md", blockers[0])

    def test_content_commit_allowlist_is_exact(self) -> None:
        record = "reproduce/kernel/RUNS/x86_64.md"
        self.assertTrue(post_content_path_allowed(record, dry_run=True))
        self.assertFalse(post_content_path_allowed("data/EXTERNAL_SOURCES.tsv", dry_run=True))
        self.assertFalse(post_content_path_allowed("tools/check_activation.py", dry_run=False))
        self.assertFalse(post_content_path_allowed("STATUS.md", dry_run=True))
        self.assertTrue(post_content_path_allowed("STATUS.md", dry_run=False))

    def test_missing_two_architecture_records_block(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            reproduction = root / "reproduce" / "fixture"
            reproduction.mkdir(parents=True)
            (reproduction / "verify.py").write_text("print('PASS')\n", encoding="utf-8")
            (reproduction / "EXPECTED.txt").write_text("PASS\n", encoding="utf-8")
            rows = [{
                "claim_id": "T-FIXTURE", "evidence_id": "EV-T-FIXTURE",
                "evidence_kind": "REPRODUCTION", "location": "reproduce/fixture",
                "sha256": "0" * 64, "hash_mode": "bundle-manifest-sha256-v1",
                "architecture_requirement": "two-architecture",
            }]
            write_tsv(root / "canon" / "EVIDENCE.tsv", EVIDENCE_FIELDS, rows)
            blockers = architecture_blockers(root)
            self.assertEqual(len(blockers), 2)
            self.assertIn("aarch64 formal record", blockers[0])
            self.assertIn("x86_64 formal record", blockers[1])

    def test_generated_views_are_activation_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = LedgerFixture(root)
            fixture.write()
            (root / "reproduce").mkdir()
            views = generated_views(root)
            (root / "canon" / "FRONTIER.md").write_text(views["FRONTIER.md"], encoding="utf-8")
            (root / "canon" / "CORE.md").write_text(views["CORE_CLAIMS.md"], encoding="utf-8")
            (root / "canon" / "CHANGELOG.md").write_text(views["CHANGELOG_COUNTS.md"], encoding="utf-8")
            (root / "canon" / "STATUS_COUNTS.tsv").write_text(views["STATUS_COUNTS.tsv"], encoding="utf-8")
            self.assertEqual(view_blockers(root), [])
            (root / "canon" / "FRONTIER.md").write_text("manual drift\n", encoding="utf-8")
            self.assertIn("not the generated registry view", view_blockers(root)[0])

    def test_duplicate_generated_block_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = LedgerFixture(root)
            fixture.write()
            (root / "reproduce").mkdir()
            views = generated_views(root)
            (root / "canon" / "FRONTIER.md").write_text(views["FRONTIER.md"], encoding="utf-8")
            (root / "canon" / "CORE.md").write_text(views["CORE_CLAIMS.md"] * 2, encoding="utf-8")
            (root / "canon" / "CHANGELOG.md").write_text(views["CHANGELOG_COUNTS.md"], encoding="utf-8")
            (root / "canon" / "STATUS_COUNTS.tsv").write_text(views["STATUS_COUNTS.tsv"], encoding="utf-8")
            self.assertTrue(any("core claim block" in item for item in view_blockers(root)))

    def test_missing_aarch64_package_is_explicit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            blockers = artifact_blockers(Path(temporary))
            self.assertGreaterEqual(len(blockers), 10)
            self.assertTrue(all(blocker.startswith("missing Genesis artifact") for blocker in blockers))


if __name__ == "__main__":
    unittest.main()
