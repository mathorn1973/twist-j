#!/usr/bin/env python3
"""Focused tests for the sentence-local status-label gate."""

from __future__ import annotations

import unittest

from check_status_labels import findings


CLAIMS = {
    "EXACT-ONE": "T",
    "DERIVED-ONE": "D",
    "LIVE-ONE": "O",
    "LOCKED-ONE": "T-LOCK",
}


class StatusLabelGateTests(unittest.TestCase):
    def test_local_matching_identifier_passes(self) -> None:
        self.assertEqual(findings("Exact (EXACT-ONE) [T].", CLAIMS), [])

    def test_identifier_in_previous_sentence_does_not_cover(self) -> None:
        problems = findings("EXACT-ONE [T]. Another assertion [T].", CLAIMS)
        self.assertEqual(len(problems), 1)
        self.assertEqual(problems[0].sentence, "Another assertion [T].")

    def test_wrong_registered_status_fails(self) -> None:
        problems = findings("EXACT-ONE [D].", CLAIMS)
        self.assertEqual(problems[0].missing_statuses, ("D",))

    def test_mixed_statuses_require_both_identifiers(self) -> None:
        problems = findings("EXACT-ONE carries layers [T, D].", CLAIMS)
        self.assertEqual(problems[0].missing_statuses, ("D",))
        self.assertEqual(
            findings("EXACT-ONE and DERIVED-ONE carry layers [T, D].", CLAIMS), []
        )

    def test_measured_comparison_is_not_formal(self) -> None:
        self.assertEqual(findings("Value 1.23 [measured comparison].", CLAIMS), [])

    def test_live_and_lock_statuses_are_distinct(self) -> None:
        self.assertEqual(findings("LIVE-ONE [O]. LOCKED-ONE [T-LOCK].", CLAIMS), [])
        self.assertEqual(
            findings("LOCKED-ONE [T].", CLAIMS)[0].missing_statuses, ("T",)
        )

    def test_prose_status_is_checked(self) -> None:
        self.assertEqual(findings("EXACT-ONE stands at T.", CLAIMS), [])
        self.assertEqual(
            findings("An unnamed value stands at O.", CLAIMS)[0].missing_statuses,
            ("O",),
        )


if __name__ == "__main__":
    unittest.main()
