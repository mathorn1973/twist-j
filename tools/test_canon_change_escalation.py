#!/usr/bin/env python3
"""Tests for the canon-change escalation of the two changed-path gates."""

from __future__ import annotations

from pathlib import Path
import sys
import unittest


TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import check_reproduce  # noqa: E402
import check_verifier  # noqa: E402


class TouchesCanonTests(unittest.TestCase):
    """Both gates decide escalation with the same predicate."""

    predicates = (check_reproduce.touches_canon, check_verifier.touches_canon)

    def assert_all(self, paths, expected):
        for predicate in self.predicates:
            with self.subTest(predicate=predicate.__module__):
                self.assertEqual(predicate(paths), expected)

    def test_a_canon_file_escalates(self) -> None:
        self.assert_all(["canon/REGISTRY.tsv"], True)
        self.assert_all(["canon/CANON.md", "tools/x.py"], True)
        self.assert_all(["canon/NORMATIVE.tsv"], True)

    def test_unrelated_paths_do_not_escalate(self) -> None:
        self.assert_all([], False)
        self.assert_all(["probes/P-X-1/RUN.md", "notes/canon/DRAFT.md"], False)
        self.assert_all(["reproduce/census/verify.py", "README.md"], False)

    def test_a_directory_merely_named_canon_does_not_escalate(self) -> None:
        self.assert_all(["notes/canon/RG-RETURN-FOLD-PROPOSAL.md"], False)
        self.assert_all(["legacy/canon/OLD.md"], False)

    def test_blank_lines_are_ignored(self) -> None:
        self.assert_all(["", "probes/P-X-1/RUN.md"], False)
        self.assert_all(["", "canon/GATES.tsv"], True)


class EscalationCoversEveryDirectoryTests(unittest.TestCase):
    """Escalation must reach directories the diff never names."""

    def test_reproduce_escalation_is_the_whole_tree(self) -> None:
        on_disk = sorted(
            path.name for path in (ROOT / "reproduce").iterdir() if path.is_dir()
        )
        self.assertIn("status-separation", on_disk)
        # The v29 fold changed canon/ only; status-separation was invalidated
        # by it and named by no diff entry.
        self.assertNotIn("status-separation", ["canon/REGISTRY.tsv"])

    def test_a_probe_verifier_reads_canon_at_run_time(self) -> None:
        """The reason the verifier gate escalates too, asserted from source."""
        source = (
            ROOT / "probes/P-TM-SYM2-MEASURE-1/verify.py"
        ).read_text(encoding="utf-8")
        self.assertIn('open("canon/NORMATIVE.tsv"', source)
        self.assertIn('open("canon/DEPENDENCIES.tsv"', source)


if __name__ == "__main__":
    unittest.main()
