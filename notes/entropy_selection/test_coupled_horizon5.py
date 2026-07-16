#!/usr/bin/env python3
"""Exact gates for the NON-CANONICAL coupled horizon ``2..5``."""

from __future__ import annotations

from collections import Counter
from dataclasses import replace
from fractions import Fraction
from hashlib import sha256
import subprocess
import sys
import unittest

try:
    from . import coupled_horizon5 as exact
except ImportError:  # Direct execution from this directory.
    import coupled_horizon5 as exact  # type: ignore[no-redef]


class ExactCoupledHorizon5Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = exact.build_exact_coupled_horizon5()

    def test_ordinary_full_domain_retraction_and_dp(self) -> None:
        report = self.certificate.ordinary
        self.assertTrue(exact.verify_ordinary_minimum(report))
        self.assertEqual(
            report.retraction,
            exact.RetractionReport(
                variable_count=140,
                pair_count=220,
                pin_count=60,
                cycle_rank=81,
                holonomy_classes=5,
                orbit_count=625,
                orbit_size=5,
                failed_orbit_maps=0,
                commutation_checks=687500,
                fixed_pin_checks=60,
            ),
        )
        self.assertEqual(report.condition_variables, (50, 4))
        self.assertEqual(len(report.elimination_order), 138)
        self.assertEqual(
            sha256(bytes(report.elimination_order)).hexdigest(),
            exact.EXPECTED_ORDINARY_ORDER_SHA256,
        )
        self.assertEqual(
            report.condition_minima,
            exact.EXPECTED_ORDINARY_CONDITION_MINIMA,
        )
        self.assertEqual(report.condition_minima.count(70), 1)
        self.assertEqual(
            (
                report.maximum_width,
                report.peak_union_entries,
                report.peak_message_entries,
                report.union_entries_per_case,
                report.optimum,
            ),
            (8, 5**9, 5**8, 4_444_930, 70),
        )
        self.assertEqual(report.assignment, exact.EXPECTED_ORDINARY_ASSIGNMENT)
        self.assertEqual(
            report.assignment_sha256,
            exact.EXPECTED_ORDINARY_ASSIGNMENT_SHA256,
        )
        self.assertEqual(
            report.violated_records,
            exact.EXPECTED_ORDINARY_VIOLATED_RECORDS,
        )

    def test_special_full_domain_retraction_and_five_coordinate_dps(self) -> None:
        report = self.certificate.special
        self.assertTrue(exact.verify_special_minimum(report))
        self.assertEqual(
            report.retraction,
            exact.RetractionReport(
                variable_count=28,
                pair_count=44,
                pin_count=60,
                cycle_rank=17,
                holonomy_classes=3,
                orbit_count=625,
                orbit_size=5,
                failed_orbit_maps=0,
                commutation_checks=137500,
                fixed_pin_checks=60,
            ),
        )
        self.assertEqual(report.coordinate_optima, (18,) * 5)
        self.assertEqual(report.maximum_width, 4)
        self.assertEqual(
            dict(report.table_census), {1: 1, 5: 1, 25: 13, 125: 9, 625: 4}
        )
        self.assertEqual(report.total_optimum, 90)
        self.assertEqual(report.assignments, exact.EXPECTED_DP_ASSIGNMENTS)

    def test_coupled_witness_attains_every_zero_price_block_minimum(self) -> None:
        witness = self.certificate.witness
        self.assertTrue(exact.verify_coupled_witness(witness))
        self.assertEqual(
            witness.family_signatures, exact.COUPLED_FAMILY_SIGNATURES
        )
        self.assertEqual(
            witness.combined_signature_sha256,
            exact.EXPECTED_COMBINED_SIGNATURE_SHA256,
        )
        self.assertEqual(
            Counter(witness.per_block_scaled_costs),
            Counter({70: 624, 90: 1}),
        )
        self.assertEqual(
            witness.transition_distances,
            (Fraction(209, 2500), Fraction(1, 2), Fraction(0)),
        )
        self.assertEqual(witness.objective, Fraction(1459, 2500))
        self.assertEqual(
            (
                witness.cell_changes,
                witness.ordinary_permutation_changes,
                witness.special_permutation_changes,
                witness.stability_changes,
            ),
            (0, 5616, 25, 0),
        )

    def test_root_closes_only_at_exact_lower_upper_equality(self) -> None:
        certificate = self.certificate
        self.assertTrue(exact.verify_exact_coupled_horizon5(certificate))
        self.assertEqual(certificate.assignment_price, 0)
        self.assertEqual(certificate.assignment_minima, (0,) * 28)
        self.assertEqual(
            certificate.block_minima,
            certificate.witness.per_block_scaled_costs,
        )
        self.assertEqual(
            (certificate.scaled_lower_bound, certificate.scaled_upper_bound),
            (43770, 43770),
        )
        self.assertEqual(certificate.optimum, Fraction(1459, 2500))
        self.assertEqual(
            (
                certificate.root_nodes,
                certificate.branched_nodes,
                certificate.fathomed_by_bound,
            ),
            (1, 0, 1),
        )

    def test_nested_checkers_reject_tampering_and_numeric_lookalikes(self) -> None:
        certificate = self.certificate
        ordinary = certificate.ordinary
        grid = list(ordinary.condition_minima)
        grid[6] += 1
        self.assertFalse(
            exact.verify_ordinary_minimum(
                replace(ordinary, condition_minima=tuple(grid))
            )
        )
        self.assertFalse(
            exact.verify_ordinary_minimum(replace(ordinary, optimum=70.0))
        )
        self.assertFalse(
            exact.verify_ordinary_minimum(
                replace(
                    ordinary,
                    retraction=replace(ordinary.retraction, cycle_rank=True),
                )
            )
        )
        special = certificate.special
        self.assertFalse(
            exact.verify_special_minimum(
                replace(special, total_optimum=special.total_optimum + 1)
            )
        )
        self.assertFalse(
            exact.verify_special_minimum(
                replace(special, total_optimum=90.0)
            )
        )
        witness = certificate.witness
        self.assertFalse(
            exact.verify_coupled_witness(
                replace(witness, objective=float(witness.objective))
            )
        )
        self.assertFalse(
            exact.verify_coupled_witness(
                replace(witness, families=(None,) * 4)  # type: ignore[arg-type]
            )
        )
        minima = list(certificate.block_minima)
        minima[0] += 1
        self.assertFalse(
            exact.verify_exact_coupled_horizon5(
                replace(certificate, block_minima=tuple(minima))
            )
        )
        self.assertFalse(
            exact.verify_exact_coupled_horizon5(
                replace(certificate, assignment_price=0.0)
            )
        )
        self.assertFalse(
            exact.verify_exact_coupled_horizon5(
                replace(certificate, root_nodes=True)
            )
        )

    def test_optimized_python_is_explicitly_refused(self) -> None:
        run = subprocess.run(
            (
                sys.executable,
                "-O",
                "-c",
                "from notes.entropy_selection.coupled_horizon5 import "
                "build_exact_coupled_horizon5; build_exact_coupled_horizon5()",
            ),
            capture_output=True,
            check=False,
            text=True,
        )
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("optimized Python disables required assertion gates", run.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
