#!/usr/bin/env python3
"""Exact gates for the NON-CANONICAL finite-horizon lower bounds."""

from __future__ import annotations

import unittest
from dataclasses import replace
from fractions import Fraction

try:
    from .bounds import (
        bound_report,
        build_certificate,
        constraint_graph,
        fundamental_cycles,
        verify_certificate,
    )
    from .growing import FiniteHorizonOptimizer, GrowingContextSolver
except ImportError:  # Direct execution from this directory.
    from bounds import (  # type: ignore[no-redef]
        bound_report,
        build_certificate,
        constraint_graph,
        fundamental_cycles,
        verify_certificate,
    )
    from growing import (  # type: ignore[no-redef]
        FiniteHorizonOptimizer,
        GrowingContextSolver,
    )


class CertifiedFiniteHorizonBoundTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Build the larger certificate first; all exhaustive holonomy minima
        # are cached and reused by the individual replay tests.
        cls.bound4 = build_certificate(4, "tree")
        cls.bound5 = build_certificate(5, "tree")

    def test_constraint_graph_cycle_ranks_are_exact(self) -> None:
        graph4 = constraint_graph(3, 4)
        graph5 = constraint_graph(3, 5)
        self.assertEqual((len(graph4.nodes), len(graph4.edges)), (16, 20))
        self.assertEqual((len(graph5.nodes), len(graph5.edges)), (28, 44))
        self.assertEqual(len(fundamental_cycles(3, 4)), 5)
        self.assertEqual(len(fundamental_cycles(3, 5)), 17)

    def test_anchor_is_the_exact_one_transition_minimum(self) -> None:
        self.assertEqual(self.bound4.anchor_bound, Fraction(209, 2500))
        one_transition = FiniteHorizonOptimizer(
            2,
            3,
            solver=GrowingContextSolver(),
            seed="tree",
            lift_phase=1,
        ).optimize(5)
        self.assertEqual(one_transition.final_objective, self.bound4.anchor_bound)
        self.assertEqual(one_transition.sweeps[-1].changed_nodes, 0)

    def test_horizon_2_4_certificate_and_gap(self) -> None:
        certificate = self.bound4
        self.assertTrue(verify_certificate(certificate))
        self.assertEqual(certificate.cycle_bound, Fraction(1, 15000))
        self.assertEqual(certificate.lower_bound, Fraction(251, 3000))
        self.assertEqual(
            tuple(cycle.basis_index for cycle in certificate.cycles),
            (0,),
        )
        cycle = certificate.cycles[0]
        self.assertEqual(
            (
                cycle.ordinary_minimum_mismatches,
                cycle.special_minimum_mismatches,
            ),
            (0, 5),
        )
        report = bound_report(4, "tree", 1)
        self.assertEqual(report.incumbent, Fraction(626, 1875))
        self.assertEqual(report.gap, Fraction(1251, 5000))
        self.assertFalse(report.meets_incumbent)

    def test_horizon_2_5_certificate_and_gap(self) -> None:
        certificate = self.bound5
        self.assertTrue(verify_certificate(certificate))
        self.assertEqual(certificate.cycle_bound, Fraction(26, 625))
        self.assertEqual(certificate.lower_bound, Fraction(313, 2500))
        self.assertEqual(
            tuple(cycle.basis_index for cycle in certificate.cycles),
            (3,),
        )
        cycle = certificate.cycles[0]
        self.assertEqual(
            (
                cycle.ordinary_minimum_mismatches,
                cycle.special_minimum_mismatches,
            ),
            (5, 0),
        )
        report = bound_report(5, "tree", 1)
        self.assertEqual(report.incumbent, Fraction(10631, 15000))
        self.assertEqual(report.gap, Fraction(8753, 15000))
        self.assertFalse(report.meets_incumbent)

    def test_selected_cycles_are_edge_disjoint(self) -> None:
        for certificate in (self.bound4, self.bound5):
            used: set[int] = set()
            for cycle in certificate.cycles:
                edges = {step.edge for step in cycle.steps}
                self.assertEqual(len(edges), len(cycle.steps))
                self.assertTrue(used.isdisjoint(edges))
                used.update(edges)

    def test_checker_rejects_a_strengthened_claim(self) -> None:
        forged = replace(
            self.bound5,
            lower_bound=self.bound5.lower_bound + Fraction(1, 15000),
        )
        self.assertFalse(verify_certificate(forged))

    def test_scope_rejects_unimplemented_horizons(self) -> None:
        with self.assertRaises(ValueError):
            build_certificate(6, "tree")


if __name__ == "__main__":
    unittest.main(verbosity=2)
