#!/usr/bin/env python3
"""Focused gates for the NON-CANONICAL entropy-selection solvers."""

from __future__ import annotations

import unittest
from fractions import Fraction

try:
    from .block_solver import (
        ReducedBlockSolver,
        five_permutations,
        solve_permutation_cocycle,
        source_delta,
        source_sectors,
        verify_source_split,
    )
    from .living import reconstruct, self_checks
    from .morse import context_graph, factors, refinement_parent, supertile
    from .tower import LexicographicTowerBaseline
except ImportError:  # Direct execution from this directory.
    from block_solver import (  # type: ignore[no-redef]
        ReducedBlockSolver,
        five_permutations,
        solve_permutation_cocycle,
        source_delta,
        source_sectors,
        verify_source_split,
    )
    from living import reconstruct, self_checks  # type: ignore[no-redef]
    from morse import (  # type: ignore[no-redef]
        context_graph,
        factors,
        refinement_parent,
        supertile,
    )
    from tower import LexicographicTowerBaseline  # type: ignore[no-redef]


class MorseTowerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.model = reconstruct()
        cls.solver = ReducedBlockSolver(cls.model)
        cls.approximant = LexicographicTowerBaseline(cls.model)

    def test_actual_thue_morse_language_and_context_graph(self) -> None:
        self.assertEqual(
            factors(3),
            (
                (0, 0, 1),
                (0, 1, 0),
                (0, 1, 1),
                (1, 0, 0),
                (1, 0, 1),
                (1, 1, 0),
            ),
        )
        graph = context_graph(3)
        self.assertEqual((len(graph.vertices), len(graph.edges)), (6, 10))
        self.assertTrue(graph.is_strongly_connected())
        self.assertTrue(all(edge.word in factors(4) for edge in graph.edges))

    def test_exact_tower_refinement_map(self) -> None:
        self.assertEqual(refinement_parent(0, 1, 0, 8), (1, 1, 0))
        self.assertEqual(refinement_parent(0, 1, 7, 8), (1, 1, 7))
        self.assertEqual(refinement_parent(0, 1, 8, 8), (1, 0, 0))
        self.assertEqual(refinement_parent(0, 1, 15, 8), (1, 0, 7))

    def test_source_sector_split_and_dyadic_carry(self) -> None:
        sectors = source_sectors()
        self.assertEqual(sum(len(sector.points) == 5 for sector in sectors), 624)
        self.assertEqual(sum(len(sector.points) == 1 for sector in sectors), 5)
        self.assertEqual(
            tuple(source_delta(level) for level in range(2, 10)),
            (1, 2, 4, 3, 1, 2, 4, 3),
        )
        for level in range(2, 10):
            self.assertTrue(verify_source_split(level))

    def test_living_kernel_reconstruction_gates(self) -> None:
        checks = self_checks(self.model)
        self.assertEqual(len(checks), 8)
        self.assertTrue(all(check.passed for check in checks))

    def test_level_two_block_actions_are_translations(self) -> None:
        graph = context_graph(3)
        sections = self.solver.cell_sections(2, graph)
        self.assertEqual(len(sections), 625)
        multipliers = {
            self.solver.edge_action(2, edge, section.cells[edge.source]).multiplier
            for section in sections
            for edge in graph.edges
        }
        self.assertEqual(multipliers, {1})

    def test_small_exact_context_ansatz_is_empty(self) -> None:
        report = self.solver.report(2, 3)
        self.assertEqual(report.source_non_singlets, 624)
        self.assertEqual(report.source_singlets, 5)
        self.assertEqual(report.target_non_singlets, 624)
        self.assertEqual(report.cell_consistent_non_singlets, 624)
        self.assertEqual(report.affine_consistent_non_singlets, 0)
        self.assertEqual(len(five_permutations()), 120)
        self.assertEqual(report.permutation_cycle_cells, 0)
        self.assertEqual(report.permutation_fixed_cells, 0)
        self.assertEqual(report.permutation_cycle_solution_count, 0)
        self.assertEqual(report.permutation_fixed_solution_count, 0)
        self.assertEqual(report.singlet_consistent_root_values, ())
        self.assertEqual(report.all_block_multipliers, (1,))
        self.assertFalse(report.reduced_transfer_exists)

    def test_positive_permutation_cocycle_orientation(self) -> None:
        graph = context_graph(3)
        delta = 2
        actions = ((1, delta),) * len(graph.edges)
        solutions = solve_permutation_cocycle(graph, actions, delta)
        self.assertEqual(len(solutions), 5)
        identity = tuple(range(5))
        identity_solution = next(
            solution
            for solution in solutions
            if solution.root_permutation == identity
        )
        self.assertTrue(
            all(permutation == identity for permutation in identity_solution.permutations)
        )

    def test_explicit_tower_approximant(self) -> None:
        boundary = self.approximant.lexicographic_boundary_map(2, 0)
        self.assertEqual(len(boundary), 3125)
        report = self.approximant.report(2)
        self.assertTrue(report.interior_equation)
        self.assertTrue(report.fiber_bijections)
        self.assertEqual(
            {defect.fraction for defect in report.roof_defects},
            {Fraction(1, 625), Fraction(1)},
        )
        self.assertEqual(report.roof_error_upper_bound, Fraction(1, 4))
        self.assertIn(
            Fraction(1),
            {defect.fraction for defect in report.refinement_defects},
        )

    def test_tower_fill_matches_closed_formula_on_a_sample(self) -> None:
        level = 3
        previous, current = (0, 1)
        maps = self.approximant.tower_maps(level, previous, current)
        word = supertile(current, level)
        for y in range(0, 3125, 211):
            source = y
            target = self.approximant.lexicographic_boundary_map(
                level, previous
            )[y]
            for position in range(1, len(word)):
                source = self.approximant.j_map[source]
                target = self.model.tick_state(word[position - 1], target)
                self.assertEqual(maps[position][source], target)


if __name__ == "__main__":
    unittest.main(verbosity=2)
