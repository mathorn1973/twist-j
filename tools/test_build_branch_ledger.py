#!/usr/bin/env python3
"""Focused tests for branch-name parsing in the retention ledger."""

from __future__ import annotations

import unittest

from build_branch_ledger import parse_branch_names


LISTING = "\n".join(
    (
        "refs/remotes/origin/HEAD",
        "refs/remotes/origin/main",
        "refs/remotes/origin/probe/P-EXAMPLE-1",
        "refs/remotes/origin/notes/c-example-1-n",
    )
)


class ParseBranchNamesTests(unittest.TestCase):
    def test_symbolic_head_is_skipped(self) -> None:
        self.assertNotIn("HEAD", parse_branch_names(LISTING, "origin"))

    def test_no_empty_name_is_produced(self) -> None:
        # refs/remotes/origin/HEAD has the short name "origin", so a filter
        # written against short names yields "" here and then asks git about
        # refs/remotes/origin/, which fails.
        self.assertNotIn("", parse_branch_names(LISTING, "origin"))

    def test_slashes_in_branch_names_survive(self) -> None:
        names = parse_branch_names(LISTING, "origin")
        self.assertIn("probe/P-EXAMPLE-1", names)
        self.assertIn("notes/c-example-1-n", names)

    def test_result_is_sorted_and_complete(self) -> None:
        self.assertEqual(
            parse_branch_names(LISTING, "origin"),
            ["main", "notes/c-example-1-n", "probe/P-EXAMPLE-1"],
        )

    def test_other_remotes_are_ignored(self) -> None:
        listing = LISTING + "\nrefs/remotes/upstream/main"
        # Only the upstream ref belongs to this remote; the four origin refs
        # in LISTING must not leak into the result.
        self.assertEqual(parse_branch_names(listing, "upstream"), ["main"])

    def test_leading_dash_name_is_kept_and_stays_prefixed(self) -> None:
        # git update-ref accepts refs/heads/-x even though git branch refuses
        # it. The name is reported as-is; every git call built from it is
        # prefixed with refs/remotes/<remote>/, so it can never be read as an
        # option.
        listing = "refs/remotes/origin/-x"
        self.assertEqual(parse_branch_names(listing, "origin"), ["-x"])

    def test_blank_lines_are_ignored(self) -> None:
        self.assertEqual(parse_branch_names("\n\n", "origin"), [])


if __name__ == "__main__":
    unittest.main()
