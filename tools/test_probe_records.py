#!/usr/bin/env python3
"""Focused tests for the probe record-shape rule."""

from __future__ import annotations

import unittest

from probe_records import declares_abandoned, problems


COMPLETE = {"PREREG.md", "verify.py", "RESULT.md", "EXPECTED.txt", "RUN.md"}
PIN_ONLY = {"PREREG.md", "verify.py", "RESULT.md"}
ABANDONED = "# Result\n\nStatus: `ABANDONED`. The formal gate never ran.\n"
SCIENTIFIC = "# Result\n\nStatus: SCIENTIFIC RESULT; GATE PASS\n"


class DeclaresAbandonedTests(unittest.TestCase):
    def test_backticked_status_is_recognised(self) -> None:
        self.assertTrue(declares_abandoned(ABANDONED))

    def test_plain_status_is_recognised(self) -> None:
        self.assertTrue(declares_abandoned("Status: ABANDONED / pin closed\n"))

    def test_scientific_result_is_not_abandoned(self) -> None:
        self.assertFalse(declares_abandoned(SCIENTIFIC))

    def test_missing_result_is_not_abandoned(self) -> None:
        self.assertFalse(declares_abandoned(None))

    def test_word_must_stand_alone(self) -> None:
        self.assertFalse(declares_abandoned("Status: NOTABANDONEDX\n"))

    def test_word_outside_a_status_line_does_not_count(self) -> None:
        text = "# Result\n\nThe route was ABANDONED upstream.\nStatus: PASS\n"
        self.assertFalse(declares_abandoned(text))

    def test_abandoned_must_be_the_status_value(self) -> None:
        for text in (
            "Status: NOT ABANDONED\n",
            "Status: FAILED; predecessor ABANDONED\n",
            "Status: PASS / ABANDONED was considered\n",
        ):
            with self.subTest(text=text):
                self.assertFalse(declares_abandoned(text))


class ProblemsTests(unittest.TestCase):
    def test_complete_probe_passes(self) -> None:
        self.assertEqual(problems(COMPLETE, SCIENTIFIC), [])

    def test_abandoned_pin_passes_without_run_artefacts(self) -> None:
        self.assertEqual(problems(PIN_ONLY, ABANDONED), [])

    def test_incomplete_probe_without_marker_still_fails(self) -> None:
        found = problems(PIN_ONLY, SCIENTIFIC)
        self.assertEqual(len(found), 2)
        self.assertTrue(any("EXPECTED.txt" in item for item in found))
        self.assertTrue(any("RUN.md" in item for item in found))

    def test_abandoned_may_not_carry_a_run_record(self) -> None:
        found = problems(PIN_ONLY | {"RUN.md"}, ABANDONED)
        self.assertEqual(len(found), 1)
        self.assertIn("RUN.md", found[0])

    def test_abandoned_may_not_carry_expected_output(self) -> None:
        found = problems(PIN_ONLY | {"EXPECTED.txt"}, ABANDONED)
        self.assertEqual(len(found), 1)
        self.assertIn("EXPECTED.txt", found[0])

    def test_abandoned_still_requires_the_pin_and_verifier(self) -> None:
        found = problems({"RESULT.md"}, ABANDONED)
        self.assertEqual(len(found), 2)
        self.assertTrue(any("PREREG.md" in item for item in found))
        self.assertTrue(any("verify.py" in item for item in found))


class SharedPredicateTests(unittest.TestCase):
    """Exercise the record-shape predicate shared by both public gates."""

    def test_skippable_shape_is_exactly_the_valid_abandoned_shape(self) -> None:
        # What check_verifier skips
        skippable = declares_abandoned(ABANDONED) and not problems(
            PIN_ONLY, ABANDONED
        )
        # What check_policy accepts
        accepted = problems(PIN_ONLY, ABANDONED) == []
        self.assertTrue(skippable)
        self.assertTrue(accepted)

    def test_run_artefacts_block_the_skip(self) -> None:
        for extra in ("EXPECTED.txt", "RUN.md"):
            present = PIN_ONLY | {extra}
            skippable = declares_abandoned(ABANDONED) and not problems(
                present, ABANDONED
            )
            self.assertFalse(skippable, f"{extra} must block the skip")

    def test_ordinary_probe_is_never_skippable(self) -> None:
        skippable = declares_abandoned(SCIENTIFIC) and not problems(
            COMPLETE, SCIENTIFIC
        )
        self.assertFalse(skippable)


if __name__ == "__main__":
    unittest.main()
