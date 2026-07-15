#!/usr/bin/env python3
"""Exact gates for context-dependent growing-optimizer basins."""

from __future__ import annotations

import unittest
from fractions import Fraction

try:
    from .basins import (
        DEFAULT_SEEDS,
        audit_seeds,
        diversify_family,
        explore_basins,
        family_distance,
        family_signature,
        global_block_relabeling,
        initialize_optimizer,
        relative_context_orbit,
    )
    from .collars import CollarSpec
    from .growing import FiniteHorizonOptimizer, GrowingContextSolver
except ImportError:  # Direct execution from this directory.
    from basins import (  # type: ignore[no-redef]
        DEFAULT_SEEDS,
        audit_seeds,
        diversify_family,
        explore_basins,
        family_distance,
        family_signature,
        global_block_relabeling,
        initialize_optimizer,
        relative_context_orbit,
    )
    from collars import CollarSpec  # type: ignore[no-redef]
    from growing import (  # type: ignore[no-redef]
        FiniteHorizonOptimizer,
        GrowingContextSolver,
    )


class BasinSeedTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.solver = GrowingContextSolver()
        cls.free_level = 3
        cls.free_spec = CollarSpec.symmetric(1)
        cls.reference = cls.solver.tree_family(cls.free_level, cls.free_spec)

    def test_context_seeds_are_reproducible_bijective_and_separated(self) -> None:
        audit = audit_seeds(
            self.solver,
            self.free_level,
            self.free_spec,
            reference=self.reference,
        )
        self.assertTrue(audit.passed)
        self.assertEqual(audit.minimum_pairwise_distance, Fraction(1))
        self.assertEqual(audit.minimum_reference_distance, Fraction(1))
        self.assertTrue(
            all(distance == 1 for _, _, distance in audit.pairwise_distances)
        )

    def test_no_single_global_block_permutation_explains_a_seed(self) -> None:
        signatures = []
        for seed in DEFAULT_SEEDS:
            candidate = diversify_family(self.reference, seed)
            orbit = relative_context_orbit(self.reference, candidate)
            self.assertIsNone(
                global_block_relabeling(self.reference, candidate)
            )
            self.assertFalse(orbit.global_block_relabeling)
            self.assertGreater(orbit.distinct_block_permutations, 1)
            self.assertEqual(set(orbit.cycle_signatures), {((5, 125),)})
            signatures.append(orbit.signature)
        self.assertEqual(len(set(signatures)), len(DEFAULT_SEEDS))

    def test_initializer_preserves_tree_anchor_and_separates_free_maps(self) -> None:
        optimizers = []
        initializations = []
        anchor_signatures = []
        for seed in DEFAULT_SEEDS[:2]:
            optimizer = FiniteHorizonOptimizer(
                2,
                4,
                solver=self.solver,
                seed="tree",
                lift_phase=0,
                freeze_minimum=True,
            )
            tree_anchor = optimizer.family(2)
            anchor_signatures.append(family_signature(tree_anchor))
            initialized = initialize_optimizer(
                optimizer, seed, anchor=tree_anchor
            )
            self.assertEqual(
                family_signature(optimizer.family(2)),
                family_signature(tree_anchor),
            )
            self.assertEqual(initialized.baseline_distance, Fraction(1))
            self.assertTrue(
                all(
                    not orbit.global_block_relabeling
                    for orbit in initialized.relative_orbits
                )
            )
            optimizers.append(optimizer)
            initializations.append(initialized)
        self.assertEqual(len(set(anchor_signatures)), 1)
        self.assertNotEqual(
            initializations[0].free_signature,
            initializations[1].free_signature,
        )
        for level in (3, 4):
            self.assertEqual(
                family_distance(
                    optimizers[0].family(level), optimizers[1].family(level)
                ),
                1,
            )
        for optimizer in optimizers:
            initial = optimizer.objective()
            report = optimizer.optimize(1)
            self.assertTrue(report.minimum_level_frozen)
            self.assertLessEqual(report.final_objective, initial)

    def test_bounded_basin_report_never_mixes_tree_boundaries(self) -> None:
        arguments = dict(
            minimum_level=2,
            maximum_level=3,
            maximum_sweeps=1,
            seeds=DEFAULT_SEEDS[:2],
            lift_phases=(0,),
            solver=self.solver,
        )
        first = explore_basins(**arguments)
        second = explore_basins(**arguments)
        self.assertEqual(first, second)
        self.assertEqual(len(first.runs), 2)
        self.assertEqual(
            {run.anchor_signature for run in first.runs},
            {first.boundary_problem_signature},
        )
        self.assertEqual(first.distinct_initial_free_signatures, 2)
        self.assertEqual(first.distinct_context_orbit_signatures, 2)
        self.assertGreaterEqual(first.distinct_final_free_signatures, 1)
        self.assertTrue(
            all(run.report.minimum_level_frozen for run in first.runs)
        )

    def test_level_five_exposes_distinct_terminal_diagnostics(self) -> None:
        report = explore_basins(
            minimum_level=2,
            maximum_level=5,
            maximum_sweeps=2,
            seeds=DEFAULT_SEEDS[:2],
            lift_phases=(0,),
            solver=self.solver,
        )
        self.assertEqual(
            {run.anchor_signature for run in report.runs},
            {report.boundary_problem_signature},
        )
        self.assertEqual(report.distinct_diagnostic_signatures, 2)
        self.assertEqual(report.distinct_objectives, 2)
        self.assertEqual(report.distinct_final_free_signatures, 2)
        self.assertEqual(
            {run.final_objective for run in report.runs},
            {Fraction(1477, 1500), Fraction(70123, 75000)},
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
