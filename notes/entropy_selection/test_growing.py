#!/usr/bin/env python3
"""Exact gates for the NON-CANONICAL growing-context optimizer."""

from __future__ import annotations

import unittest
from fractions import Fraction

try:
    from .collars import CollarSpec
    from .growing import (
        FiniteHorizonOptimizer,
        GrowingContextSolver,
        source_blocks,
    )
    from .lambda5 import j_permutation
    from .morse import supertile
    from .tower import LexicographicTowerBaseline
except ImportError:  # Direct execution from this directory.
    from collars import CollarSpec  # type: ignore[no-redef]
    from growing import (  # type: ignore[no-redef]
        FiniteHorizonOptimizer,
        GrowingContextSolver,
        source_blocks,
    )
    from lambda5 import j_permutation  # type: ignore[no-redef]
    from morse import supertile  # type: ignore[no-redef]
    from tower import LexicographicTowerBaseline  # type: ignore[no-redef]


class GrowingContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.solver = GrowingContextSolver()

    def test_source_blocks_partition_the_full_carrier(self) -> None:
        blocks = source_blocks()
        self.assertEqual(len(blocks), 625)
        self.assertEqual(tuple(len(block.points) for block in blocks), (5,) * 625)
        self.assertEqual(
            {point for block in blocks for point in block.points},
            set(range(3125)),
        )
        self.assertEqual(blocks[-1].kind, "J-power-fixed-block")

    def test_structured_lexicographic_map_matches_materialized_baseline(self) -> None:
        level = 2
        previous = 0
        structured = self.solver.lexicographic_map(level, previous)
        baseline = LexicographicTowerBaseline(self.solver.model)
        self.assertEqual(
            self.solver.decode(structured),
            baseline.lexicographic_boundary_map(level, previous),
        )

    def test_advance_retreat_and_full_equation_orientation(self) -> None:
        level = 2
        letter = 1
        mapping = self.solver.lexicographic_map(level, previous=0)
        advanced = self.solver.advance(mapping, level, letter)
        self.assertEqual(
            self.solver.retreat(advanced, level, letter, mapping.half),
            mapping,
        )
        source = self.solver.decode(mapping)
        target = self.solver.decode(advanced)
        j_power = tuple(range(3125))
        j_map = j_permutation()
        for _ in range(1 << level):
            j_power = tuple(j_map[point] for point in j_power)
        for y in range(0, 3125, 37):
            state = source[y]
            for epsilon in supertile(letter, level):
                state = self.solver.model.tick_state(epsilon, state)
            self.assertEqual(target[j_power[y]], state)

    def test_exact_weighted_lexicographic_refinement_regression(self) -> None:
        pair = CollarSpec(1, 0)
        lower = self.solver.lexicographic_family(2, pair)
        upper = self.solver.lexicographic_family(3, pair)
        report = self.solver.refinement_report(upper, lower)
        self.assertEqual(report.first_child_distance, 0)
        self.assertEqual(report.second_child_distance, Fraction(209, 1250))
        self.assertEqual(report.distance, Fraction(209, 1250))

    def test_maximum_weight_tree_family_satisfies_selected_edges(self) -> None:
        family = self.solver.tree_family(2, CollarSpec.symmetric(1))
        report = self.solver.family_report(family)
        self.assertEqual(report.selected_tree_edges, report.vertices - 1)
        self.assertGreaterEqual(report.zero_defect_edges, report.selected_tree_edges)
        self.assertGreaterEqual(report.zero_defect_weight, report.selected_tree_weight)

    def test_coordinate_update_fixes_a_unanimous_map(self) -> None:
        mapping = self.solver.lexicographic_map(2, previous=0)
        optimizer = FiniteHorizonOptimizer(2, 3, solver=self.solver)
        self.assertEqual(
            optimizer.coordinate_best(((Fraction(1), mapping),)),
            mapping,
        )

    def test_small_horizon_monotonic_exact_regression(self) -> None:
        optimizer = FiniteHorizonOptimizer(
            2,
            4,
            solver=self.solver,
            seed="tree",
            lift_phase=1,
        )
        report = optimizer.optimize(5)
        self.assertEqual(report.final_objective, Fraction(626, 1875))
        self.assertLessEqual(report.final_objective, report.initial_objective)
        self.assertTrue(
            all(
                sweep.objective_after <= sweep.objective_before
                for sweep in report.sweeps
            )
        )
        self.assertEqual(report.sweeps[-1].changed_nodes, 0)
        self.assertLessEqual(report.maximum_matching_component, 2)
        self.assertTrue(report.minimum_level_frozen)

    def test_all_levels_free_diagnostic_updates_the_minimum_level(self) -> None:
        anchored = FiniteHorizonOptimizer(
            2,
            4,
            solver=self.solver,
            seed="tree",
            lift_phase=1,
        ).optimize(5)
        free = FiniteHorizonOptimizer(
            2,
            4,
            solver=self.solver,
            seed="tree",
            lift_phase=1,
            freeze_minimum=False,
        ).optimize(5)
        self.assertFalse(free.minimum_level_frozen)
        self.assertLess(free.final_objective, anchored.final_objective)
        self.assertEqual(free.sweeps[-1].changed_nodes, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
