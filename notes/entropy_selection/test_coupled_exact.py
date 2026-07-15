#!/usr/bin/env python3
"""Exact gates for the NON-CANONICAL coupled ``2..4`` certificate."""

from __future__ import annotations

import unittest
from collections import Counter
from dataclasses import replace
from fractions import Fraction

try:
    from . import coupled_exact as exact
except ImportError:  # Direct execution from this directory.
    import coupled_exact as exact  # type: ignore[no-redef]


class ExactCoupledCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = exact.build_exact_coupled_certificate()

    def test_point_constraint_census_and_transports(self) -> None:
        first = exact.point_constraints(0)
        last = exact.point_constraints(4)
        self.assertEqual(tuple(item.id for item in first), tuple(range(32)))
        self.assertEqual(Counter(item.weight for item in first), Counter({1: 16, 2: 16}))
        self.assertEqual(first[:20], last[:20])
        self.assertEqual(sum(item.is_pair for item in first), 20)
        for constraint in first[:20]:
            self.assertEqual(
                sorted(constraint.forward),
                list(range(exact.POINT_DOMAIN_SIZE)),
            )
            for state in (0, 1, exact.POINT_DOMAIN_SIZE - 1):
                self.assertEqual(
                    constraint.reverse[constraint.forward[state]], state
                )

    def test_conflict_core_branch_and_bound_is_replayed_exactly(self) -> None:
        report = self.certificate.bnb
        self.assertTrue(exact.verify_point_bnb_report(report))
        self.assertEqual(
            (report.total_optimum, report.total_calls, report.total_unique_masks),
            (60, 114260, 25630),
        )
        expected_assignments = (
            (3, 4, 4, 0, 0, 1, 4, 4, 3, 3, 1, 0, 4, 4, 3, 3),
            (4, 0, 0, 1, 1, 2, 0, 0, 4, 4, 2, 1, 0, 0, 4, 4),
            (0, 1, 1, 2, 2, 3, 1, 1, 0, 0, 3, 2, 1, 1, 0, 0),
            (1, 2, 2, 3, 3, 4, 2, 2, 1, 1, 4, 3, 2, 2, 1, 1),
            (2, 3, 3, 4, 4, 0, 3, 3, 2, 2, 0, 4, 3, 3, 2, 2),
        )
        for coordinate, result in enumerate(report.results):
            self.assertEqual(result.optimum, 12)
            self.assertEqual(result.active_mask, 0xFD6FAEFA)
            self.assertEqual(
                result.removed_constraints,
                exact.EXPECTED_REMOVED_CONSTRAINTS,
            )
            self.assertEqual(result.assignment, expected_assignments[coordinate])
            self.assertEqual(
                (result.calls, result.unique_masks), (22852, 5126)
            )
            replay = exact._constraint_satisfaction(
                coordinate, result.active_mask
            )
            self.assertTrue(replay.satisfiable)
            self.assertEqual(replay.assignment, result.assignment)

    def test_oracle_conflicts_and_input_guards(self) -> None:
        self.assertEqual(
            exact._constraint_satisfaction(0, exact.FULL_CONSTRAINT_MASK).core,
            (20, 21),
        )
        pair_of_pins = (1 << 20) | (1 << 21)
        self.assertEqual(
            exact._constraint_satisfaction(0, pair_of_pins).core, (20, 21)
        )
        best = self.certificate.bnb.results[0].active_mask
        for constraint_id in exact.EXPECTED_REMOVED_CONSTRAINTS:
            self.assertFalse(
                exact._constraint_satisfaction(
                    0, best | (1 << constraint_id)
                ).satisfiable
            )
        for coordinate in (-1, 5, False, 0.0):
            with self.assertRaises(ValueError):
                exact.point_constraints(coordinate)  # type: ignore[arg-type]
        for mask in (-1, 1 << 32, False, 0.0):
            with self.assertRaises(ValueError):
                exact._constraint_satisfaction(0, mask)  # type: ignore[arg-type]

    def test_zero_price_coupled_dual_and_matching_primal(self) -> None:
        certificate = self.certificate
        dual = certificate.coupled_dual
        witness = certificate.witness
        self.assertTrue(
            exact.verify_coupled_block_dual(dual, certificate.path_certificate)
        )
        self.assertEqual(dual.assignment_price, 0)
        self.assertEqual(dual.node_assignment_minima, (0,) * 16)
        self.assertEqual(Counter(dual.block_minima), Counter({40: 624, 60: 1}))
        self.assertEqual(dual.block_minima, witness.per_block_scaled_costs)
        self.assertEqual(dual.scaled_value, 25020)

    def test_coupled_witness_is_bijective_and_attains_every_block_bound(self) -> None:
        witness = self.certificate.witness
        self.assertTrue(
            exact.verify_coupled_witness(witness, self.certificate.bnb)
        )
        self.assertEqual(
            witness.family_signatures, exact.COUPLED_FAMILY_SIGNATURES
        )
        self.assertEqual(
            witness.per_block_scaled_costs, (40,) * 624 + (60,)
        )
        self.assertEqual(
            (witness.first_transition, witness.second_transition, witness.objective),
            (Fraction(209, 2500), Fraction(1, 4), Fraction(417, 1250)),
        )
        self.assertEqual(
            (
                witness.cell_changes,
                witness.ordinary_permutation_changes,
                witness.special_permutation_changes,
                witness.maximum_path_slack,
                witness.stability_changes,
            ),
            (0, 0, 8, 0, 0),
        )
        special = tuple(
            exact._edge_mismatch(
                witness.families, exact.SPECIAL_BLOCK, edge_id
            )
            for edge_id in range(exact.EDGE_COUNT)
        )
        self.assertEqual(
            tuple(edge for edge, value in enumerate(special) if value),
            exact.EXPECTED_REMOVED_CONSTRAINTS,
        )
        self.assertTrue(
            all(special[edge] == 5 for edge in exact.EXPECTED_REMOVED_CONSTRAINTS)
        )

    def test_root_is_closed_only_by_exact_lower_upper_equality(self) -> None:
        certificate = self.certificate
        self.assertTrue(exact.verify_exact_coupled_certificate(certificate))
        self.assertEqual(
            (certificate.scaled_lower_bound, certificate.scaled_upper_bound),
            (25020, 25020),
        )
        self.assertEqual(certificate.optimum, Fraction(417, 1250))
        self.assertEqual(
            (
                certificate.root_nodes,
                certificate.branched_nodes,
                certificate.fathomed_by_bound,
            ),
            (1, 0, 1),
        )

    def test_bnb_checker_rejects_forged_search_and_assignments(self) -> None:
        report = self.certificate.bnb
        first = report.results[0]
        forged_result = replace(first, calls=-1, unique_masks=-1)
        forged = replace(
            report,
            results=(forged_result,) + report.results[1:],
            total_calls=report.total_calls - first.calls - 1,
            total_unique_masks=report.total_unique_masks - first.unique_masks - 1,
        )
        self.assertFalse(exact.verify_point_bnb_report(forged))
        assignment = list(first.assignment)
        assignment[0] = float(assignment[0])
        forged_result = replace(first, assignment=tuple(assignment))
        self.assertFalse(
            exact.verify_point_bnb_report(
                replace(report, results=(forged_result,) + report.results[1:])
            )
        )
        forged_result = replace(first, active_mask=first.active_mask ^ 1)
        self.assertFalse(
            exact.verify_point_bnb_report(
                replace(report, results=(forged_result,) + report.results[1:])
            )
        )

    def test_nested_checkers_reject_tampering_and_numeric_lookalikes(self) -> None:
        certificate = self.certificate
        dual = certificate.coupled_dual
        self.assertFalse(
            exact.verify_coupled_block_dual(
                replace(dual, assignment_price=0.0),
                certificate.path_certificate,
            )
        )
        minima = list(dual.block_minima)
        minima[0] += 1
        self.assertFalse(
            exact.verify_coupled_block_dual(
                replace(dual, block_minima=tuple(minima), scaled_value=25021),
                certificate.path_certificate,
            )
        )
        witness = certificate.witness
        signatures = list(witness.family_signatures)
        signatures[-1] = "0" * 64
        self.assertFalse(
            exact.verify_coupled_witness(
                replace(witness, family_signatures=tuple(signatures)),
                certificate.bnb,
            )
        )
        self.assertFalse(
            exact.verify_coupled_witness(
                replace(witness, objective=float(witness.objective)),
                certificate.bnb,
            )
        )
        family = witness.families[1]
        mapping = family.maps[0]
        cells = list(mapping.cells)
        cells[1] = cells[0]
        with self.assertRaises(ValueError):
            replace(mapping, cells=tuple(cells))
        self.assertFalse(
            exact.verify_exact_coupled_certificate(
                replace(certificate, scaled_upper_bound=25021)
            )
        )
        self.assertFalse(
            exact.verify_exact_coupled_certificate(
                replace(certificate, root_nodes=True)
            )
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
