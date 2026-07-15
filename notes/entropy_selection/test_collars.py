#!/usr/bin/env python3
"""Exact gates for NON-CANONICAL growing-collar incidence."""

from __future__ import annotations

import unittest
from fractions import Fraction

try:
    from .collars import CollarSpec, collar_graph, refinement_incidence
except ImportError:  # Direct execution from this directory.
    from collars import (  # type: ignore[no-redef]
        CollarSpec,
        collar_graph,
        refinement_incidence,
    )


class CollarRefinementTests(unittest.TestCase):
    def test_pair_refinement_is_the_known_tower_parent_map(self) -> None:
        pair = CollarSpec(1, 0)
        incidence = refinement_incidence(pair, pair)
        self.assertTrue(incidence.verify())
        self.assertEqual(len(incidence.atoms), 4)
        rows = {
            atom.parent: (atom.child0, atom.child1, atom.branch_weight)
            for atom in incidence.atoms
        }
        self.assertEqual(
            rows,
            {
                (0, 0): ((1, 0), (0, 1), Fraction(1, 12)),
                (0, 1): ((1, 1), (1, 0), Fraction(1, 6)),
                (1, 0): ((0, 0), (0, 1), Fraction(1, 6)),
                (1, 1): ((0, 1), (1, 0), Fraction(1, 12)),
            },
        )

    def test_ambiguous_extension_keeps_children_joint(self) -> None:
        parent = CollarSpec(1, 0)
        child = CollarSpec.symmetric(1)
        incidence = refinement_incidence(parent, child)
        rows = tuple(
            atom
            for atom in incidence.atoms
            if atom.parent == (0, 1)
        )
        self.assertEqual(
            {(atom.extension, atom.child0, atom.child1) for atom in rows},
            {
                ((0, 1, 0), (1, 1, 0), (1, 0, 0)),
                ((0, 1, 1), (1, 1, 0), (1, 0, 1)),
            },
        )
        self.assertEqual({atom.frequency for atom in rows}, {Fraction(1, 6)})

    def test_only_the_half_mixture_of_child_phases_is_invariant(self) -> None:
        pair = CollarSpec(1, 0)
        incidence = refinement_incidence(pair, pair)
        phase0 = {
            child: sum(
                atom.frequency
                for atom in incidence.atoms
                if atom.child0 == child
            )
            for child in ((0, 0), (0, 1), (1, 0), (1, 1))
        }
        phase1 = {
            child: sum(
                atom.frequency
                for atom in incidence.atoms
                if atom.child1 == child
            )
            for child in ((0, 0), (0, 1), (1, 0), (1, 1))
        }
        self.assertEqual(
            phase0,
            {
                (0, 0): Fraction(1, 3),
                (0, 1): Fraction(1, 6),
                (1, 0): Fraction(1, 6),
                (1, 1): Fraction(1, 3),
            },
        )
        self.assertEqual(
            phase1,
            {
                (0, 0): 0,
                (0, 1): Fraction(1, 2),
                (1, 0): Fraction(1, 2),
                (1, 1): 0,
            },
        )

    def test_symmetric_growing_collars_have_exact_marginals(self) -> None:
        for parent_radius in range(1, 7):
            for child_radius in range(1, 7):
                incidence = refinement_incidence(
                    CollarSpec.symmetric(parent_radius),
                    CollarSpec.symmetric(child_radius),
                )
                self.assertTrue(incidence.verify())
                self.assertEqual(
                    sum(atom.frequency for atom in incidence.atoms),
                    1,
                )

    def test_weighted_collar_graph_balances_exactly(self) -> None:
        for radius in range(1, 9):
            graph = collar_graph(CollarSpec.symmetric(radius))
            self.assertTrue(graph.verify())
            self.assertEqual(sum(edge.weight for edge in graph.edges), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
