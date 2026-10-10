#!/usr/bin/env python3
"""Tests for full replay selection by the two changed-path gates."""

from __future__ import annotations

from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


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


class ChangedPathSelectionTests(unittest.TestCase):
    """Exercise actual selection without executing scientific verifiers."""

    gates = (
        (check_verifier, "PROBES", "probes", "changed_probes"),
        (check_reproduce, "REPRODUCE", "reproduce", "changed_reproductions"),
    )

    def check_selection(self, changes, selected):
        for module, attribute, directory, function in self.gates:
            with self.subTest(gate=function), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                inventory = root / directory
                inventory.mkdir()
                for name in ("P-A", "P-B"):
                    (inventory / name).mkdir()
                (inventory / "not-a-directory.md").write_text("fixture")
                paths = [path.format(directory=directory) for path in changes]
                result = subprocess.CompletedProcess([], 0, "\n".join(paths), "")
                with patch.object(module, "ROOT", root), \
                     patch.object(module, attribute, inventory), \
                     patch.object(module.subprocess, "run", return_value=result) as diff, \
                     redirect_stdout(StringIO()):
                    actual = getattr(module, function)("a" * 40)
                self.assertEqual(actual, [inventory / name for name in selected])
                diff.assert_called_once()
                self.assertEqual(diff.call_args.args[0],
                                 ["git", "diff", "--name-only", "a" * 40 + "...HEAD"])

    def test_workflow_only_change_selects_the_whole_inventory(self):
        self.check_selection([".github/workflows/policy.yml"], ["P-A", "P-B"])

    def test_canon_change_still_selects_the_whole_inventory(self):
        self.check_selection(["canon/CORE.md"], ["P-A", "P-B"])

    def test_workflow_and_one_changed_directory_include_untouched_directory(self):
        self.check_selection(
            [".github/workflows/policy.yml", "{directory}/P-A/verify.py"],
            ["P-A", "P-B"],
        )

    def test_ordinary_changes_keep_their_narrow_selection(self):
        self.check_selection(["{directory}/P-A/verify.py"], ["P-A"])
        self.check_selection(["README.md", "notes/.github/workflows/policy.yml"], [])

    def test_workflow_escalation_cannot_bypass_one_probe_per_pull_request(self):
        result = subprocess.CompletedProcess(
            [], 0, ".github/workflows/policy.yml\n"
            "probes/P-A/verify.py\nprobes/P-B/verify.py\n", ""
        )
        with tempfile.TemporaryDirectory() as temp, \
             patch.object(check_verifier, "PROBES", Path(temp)), \
             patch.object(check_verifier.subprocess, "run", return_value=result), \
             redirect_stdout(StringIO()) as output, \
             self.assertRaises(SystemExit) as stopped:
            check_verifier.changed_probes("a" * 40)
        self.assertEqual(stopped.exception.code, 1)
        self.assertIn("only one probe directory", output.getvalue())


if __name__ == "__main__":
    unittest.main()
