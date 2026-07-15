#!/usr/bin/env python3
"""Exact gates for the NON-CANONICAL anchor-to-anchor path dual."""

from __future__ import annotations

import unittest
from collections import Counter
from dataclasses import replace
from fractions import Fraction

try:
    from .bounds import CycleStep, anchor_terms
    from .path_bounds import (
        ALL_BLOCKS,
        TerminalPath,
        analyze_path,
        anchor_terminals,
        augmented_edge_weights,
        build_catalog_dual,
        build_path_certificate,
        certificate_edge_loads,
        direct_anchor_bound,
        simple_terminal_paths,
        verify_catalog_dual,
        verify_path_certificate,
    )
except ImportError:  # Direct execution from this directory.
    from bounds import CycleStep, anchor_terms  # type: ignore[no-redef]
    from path_bounds import (  # type: ignore[no-redef]
        ALL_BLOCKS,
        TerminalPath,
        analyze_path,
        anchor_terminals,
        augmented_edge_weights,
        build_catalog_dual,
        build_path_certificate,
        certificate_edge_loads,
        direct_anchor_bound,
        simple_terminal_paths,
        verify_catalog_dual,
        verify_path_certificate,
    )


class AnchorToAnchorPathBoundTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = build_path_certificate()

    def test_augmented_graph_census_and_direct_anchor_regression(self) -> None:
        terminals = anchor_terminals()
        self.assertEqual(len(terminals), 12)
        self.assertEqual(tuple(terminal.id for terminal in terminals), tuple(range(12)))
        self.assertEqual(
            tuple(terminal.parent[1] for terminal in terminals[::2]),
            ((0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0)),
        )
        self.assertEqual({terminal.weight for terminal in terminals}, {Fraction(1, 12)})
        self.assertEqual(len(augmented_edge_weights()), 32)
        self.assertEqual(direct_anchor_bound(), Fraction(209, 2500))
        legacy = anchor_terms("tree")
        replayed = tuple(
            analyze_path(
                ALL_BLOCKS,
                TerminalPath(2 * atom, 2 * atom + 1, ()),
                terminals[2 * atom].weight,
            )
            for atom in range(6)
        )
        self.assertEqual(
            tuple(Fraction(term.total_mismatches, 3125) for term in replayed),
            tuple(term.desired_map_distance for term in legacy),
        )
        self.assertEqual(
            tuple(term.contribution for term in replayed),
            tuple(term.contribution for term in legacy),
        )

    def test_all_simple_terminal_path_catalog_is_deterministic(self) -> None:
        paths = simple_terminal_paths()
        self.assertEqual(len(paths), 622)
        self.assertEqual(len(set(paths)), len(paths))
        self.assertEqual(
            Counter(len(path.steps) + 2 for path in paths),
            Counter({2: 6, 4: 40, 6: 64, 8: 96, 10: 160, 12: 256}),
        )

    def test_ten_path_certificate_closes_the_catalog(self) -> None:
        certificate = self.certificate
        self.assertTrue(verify_path_certificate(certificate))
        self.assertEqual(len(certificate.paths), 10)
        self.assertEqual(certificate.lower_bound, Fraction(417, 1250))
        self.assertEqual(
            Counter(path.total_mismatches for path in certificate.paths),
            Counter({3125: 6, 5: 4}),
        )
        self.assertEqual(
            Counter(path.allocation for path in certificate.paths),
            Counter({Fraction(1, 24): 8, Fraction(1, 12): 2}),
        )
        incumbent = Fraction(626, 1875)
        self.assertEqual(incumbent - certificate.lower_bound, Fraction(1, 3750))

    def test_every_block_edge_capacity_is_saturated(self) -> None:
        loads = certificate_edge_loads(self.certificate)
        weights = augmented_edge_weights()
        self.assertEqual(len(loads), 625)
        self.assertTrue(all(row == weights for row in loads))

    def test_blockwise_catalog_dual_matches_the_primal(self) -> None:
        dual = build_catalog_dual()
        self.assertTrue(verify_catalog_dual(dual))
        self.assertEqual((dual.path_count, dual.cycle_count), (622, 20))
        self.assertEqual(dual.ordinary_scaled_bound, 40)
        self.assertEqual(dual.special_scaled_bound, 60)
        self.assertEqual(dual.scaled_bound, 25020)
        self.assertEqual(dual.bound, self.certificate.lower_bound)

    def test_checker_rejects_a_strengthened_claim(self) -> None:
        forged = replace(
            self.certificate,
            lower_bound=self.certificate.lower_bound + Fraction(1, 75000),
        )
        self.assertFalse(verify_path_certificate(forged))

    def test_checker_rejects_an_exact_edge_overload(self) -> None:
        first = self.certificate.paths[0]
        overloaded = analyze_path(
            first.block_ids,
            first.path,
            first.allocation + Fraction(1, 24),
        )
        paths = (overloaded,) + self.certificate.paths[1:]
        forged = replace(
            self.certificate,
            paths=paths,
            lower_bound=sum((path.contribution for path in paths), Fraction(0)),
        )
        self.assertFalse(verify_path_certificate(forged))

    def test_checker_rejects_tampered_path_metadata(self) -> None:
        first = self.certificate.paths[0]
        forged_first = replace(
            first,
            total_mismatches=first.total_mismatches + 1,
        )
        forged = replace(
            self.certificate,
            paths=(forged_first,) + self.certificate.paths[1:],
        )
        self.assertFalse(verify_path_certificate(forged))

    def test_checker_rejects_inexact_float_data(self) -> None:
        first = self.certificate.paths[0]
        forged_first = replace(
            first,
            allocation=float(first.allocation),
            contribution=float(first.contribution),
        )
        forged = replace(
            self.certificate,
            paths=(forged_first,) + self.certificate.paths[1:],
            lower_bound=float(self.certificate.lower_bound),
        )
        self.assertFalse(verify_path_certificate(forged))

    def test_checker_rejects_numeric_lookalike_metadata(self) -> None:
        first = self.certificate.paths[0]
        float_total = replace(first, total_mismatches=float(first.total_mismatches))
        self.assertFalse(
            verify_path_certificate(
                replace(
                    self.certificate,
                    paths=(float_total,) + self.certificate.paths[1:],
                )
            )
        )
        self.assertFalse(
            verify_path_certificate(replace(self.certificate, minimum_level=2.0))
        )
        bad_step = replace(first.path.steps[0], forward=0)
        bad_path = replace(
            first.path,
            steps=(bad_step,) + first.path.steps[1:],
        )
        with self.assertRaises(ValueError):
            analyze_path(ALL_BLOCKS, bad_path, Fraction(1, 24))

    def test_path_analyzer_rejects_bad_blocks_and_discontinuity(self) -> None:
        with self.assertRaises(ValueError):
            analyze_path((0, 0), self.certificate.paths[0].path, Fraction(1, 24))
        bad = TerminalPath(0, 2, (CycleStep(0, True),))
        with self.assertRaises(ValueError):
            analyze_path(ALL_BLOCKS, bad, Fraction(1, 24))

    def test_catalog_dual_rejects_a_cheaper_price_claim(self) -> None:
        dual = build_catalog_dual()
        prices = list(dual.ordinary_prices)
        prices[20] -= Fraction(1, 2)
        forged = replace(dual, ordinary_prices=tuple(prices))
        self.assertFalse(verify_catalog_dual(forged))
        self.assertFalse(verify_catalog_dual(replace(dual, path_count=622.0)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
