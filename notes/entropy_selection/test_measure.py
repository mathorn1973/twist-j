#!/usr/bin/env python3
"""Exact gates for NON-CANONICAL Thue--Morse context measures."""

from __future__ import annotations

import unittest
from fractions import Fraction

try:
    from .measure import (
        LEGAL_PAIRS,
        PAIR_WITNESSES,
        audit,
        closure_level,
        context_measure,
        cylinder_frequency,
        factor_census,
        factor_frequencies,
        pair_witness_word,
    )
except ImportError:  # Direct execution from this directory.
    from measure import (  # type: ignore[no-redef]
        LEGAL_PAIRS,
        PAIR_WITNESSES,
        audit,
        closure_level,
        context_measure,
        cylinder_frequency,
        factor_census,
        factor_frequencies,
        pair_witness_word,
    )


class ExactThueMorseMeasureTests(unittest.TestCase):
    def test_all_pairs_have_short_legality_witnesses(self) -> None:
        witness = pair_witness_word()
        self.assertEqual(witness, (0, 1, 1, 0, 1, 0, 0, 1))
        self.assertEqual(LEGAL_PAIRS, ((0, 0), (0, 1), (1, 0), (1, 1)))
        for pair, position in PAIR_WITNESSES.items():
            self.assertEqual(witness[position : position + 2], pair)

    def test_closure_levels_cover_windows_with_two_supertiles(self) -> None:
        self.assertEqual(
            tuple(closure_level(length) for length in range(1, 21)),
            (0, 0, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5),
        )
        for length in range(1, 21):
            census = factor_census(length)
            self.assertGreaterEqual(census.supertile_size, length - 1)
            self.assertTrue(census.verify())

    def test_exact_factor_complexities_through_twenty(self) -> None:
        report = audit(20)
        self.assertTrue(report.passed)
        self.assertEqual(
            report.complexities,
            (2, 4, 6, 10, 12, 16, 20, 22, 24, 28, 32, 36, 40, 42, 44, 46, 48, 52, 56, 60),
        )

    def test_pair_and_triple_frequencies_are_exact(self) -> None:
        self.assertEqual(
            factor_frequencies(2),
            {
                (0, 0): Fraction(1, 6),
                (0, 1): Fraction(1, 3),
                (1, 0): Fraction(1, 3),
                (1, 1): Fraction(1, 6),
            },
        )
        self.assertEqual(
            set(factor_frequencies(3).values()),
            {Fraction(1, 6)},
        )

    def test_non_language_binary_cylinder_has_zero_measure(self) -> None:
        self.assertEqual(cylinder_frequency((0, 0, 0)), 0)
        with self.assertRaises(ValueError):
            cylinder_frequency(())
        with self.assertRaises(ValueError):
            cylinder_frequency((0, 2))

    def test_context_vertex_and_edge_weights_balance_exactly(self) -> None:
        for width in range(1, 20):
            self.assertTrue(context_measure(width).verify())

    def test_frequency_support_and_marginals_through_twenty(self) -> None:
        for length in range(1, 21):
            frequencies = factor_frequencies(length)
            self.assertEqual(tuple(frequencies), factor_census(length).factors)
            self.assertEqual(sum(frequencies.values()), 1)
            self.assertTrue(all(value > 0 for value in frequencies.values()))
            for word, value in frequencies.items():
                self.assertEqual(
                    frequencies[tuple(1 - bit for bit in word)], value
                )
                self.assertEqual(frequencies[tuple(reversed(word))], value)


if __name__ == "__main__":
    unittest.main(verbosity=2)
