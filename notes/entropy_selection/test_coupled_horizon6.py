#!/usr/bin/env python3
"""Exact gates for the NON-CANONICAL coupled horizon ``2..6``."""

from __future__ import annotations

from collections import Counter
from dataclasses import replace
from fractions import Fraction
import subprocess
import sys
import unittest

try:
    from . import coupled_horizon6 as exact
except ImportError:  # Direct execution from this directory.
    import coupled_horizon6 as exact  # type: ignore[no-redef]


class ExactCoupledHorizon6Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = exact.build_exact_coupled_horizon6()

    def test_ordinary_exact_lower_and_lifted_reassembly(self) -> None:
        report = self.certificate.ordinary
        self.assertTrue(exact.ordinary.verify_ordinary_horizon6(report))
        self.assertEqual(report.optimum, 190)
        self.assertEqual(report.lifted_block_count, 624)
        self.assertEqual(dict(report.lifted_cost_census), {190: 624})
        self.assertEqual(report.retraction.variable_count, 220)
        self.assertEqual(report.retraction.pair_count, 380)
        self.assertEqual(report.retraction.pin_count, 60)
        self.assertEqual(report.retraction.orbit_count, 625)
        self.assertEqual(report.retraction.orbit_size, 5)

    def test_special_exact_lower_and_reassembly(self) -> None:
        report = self.certificate.special
        self.assertTrue(exact.prep.verify_special_horizon6(report))
        self.assertTrue(report.closed)
        self.assertEqual(report.coordinate_optima, (44,) * 5)
        self.assertEqual(report.scaled_lower_bound, 220)
        self.assertEqual(report.reassembled_cost, 220)
        self.assertEqual(report.reassembled_bad, exact.EXPECTED_SPECIAL_BAD)

    def test_coupled_witness_attains_every_zero_price_block_minimum(self) -> None:
        witness = self.certificate.witness
        self.assertTrue(exact.verify_coupled_witness(witness))
        self.assertEqual(
            witness.family_signatures,
            exact.COUPLED_FAMILY_SIGNATURES,
        )
        self.assertEqual(
            witness.combined_signature_sha256,
            exact.EXPECTED_COMBINED_SIGNATURE_SHA256,
        )
        self.assertEqual(
            Counter(witness.per_block_scaled_costs),
            Counter({190: 624, 220: 1}),
        )
        self.assertEqual(
            witness.transition_distances,
            (
                Fraction(313, 1875),
                Fraction(573, 1250),
                Fraction(1249, 7500),
                Fraction(0),
            ),
        )
        self.assertEqual(witness.objective, Fraction(5939, 7500))

    def test_root_closes_only_at_exact_lower_upper_equality(self) -> None:
        certificate = self.certificate
        self.assertTrue(exact.verify_exact_coupled_horizon6(certificate))
        self.assertEqual(certificate.assignment_price, 0)
        self.assertEqual(certificate.assignment_minima, (0,) * 44)
        self.assertEqual(
            certificate.block_minima,
            certificate.witness.per_block_scaled_costs,
        )
        self.assertEqual(
            (certificate.scaled_lower_bound, certificate.scaled_upper_bound),
            (118780, 118780),
        )
        self.assertEqual(certificate.optimum, Fraction(5939, 7500))
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
        self.assertFalse(
            exact.ordinary.verify_ordinary_horizon6(
                replace(ordinary, optimum=ordinary.optimum + 1)
            )
        )
        self.assertFalse(
            exact.ordinary.verify_ordinary_horizon6(
                replace(ordinary, optimum=190.0)
            )
        )
        special = certificate.special
        self.assertFalse(
            exact.prep.verify_special_horizon6(
                replace(special, reassembled_cost=220.0)
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
                replace(witness, families=(None,) * 5)  # type: ignore[arg-type]
            )
        )
        minima = list(certificate.block_minima)
        minima[0] += 1
        self.assertFalse(
            exact.verify_exact_coupled_horizon6(
                replace(certificate, block_minima=tuple(minima))
            )
        )
        self.assertFalse(
            exact.verify_exact_coupled_horizon6(
                replace(certificate, assignment_price=0.0)
            )
        )
        self.assertFalse(
            exact.verify_exact_coupled_horizon6(
                replace(certificate, root_nodes=True)
            )
        )

    def test_report_is_deterministic_and_optimized_python_is_refused(self) -> None:
        report = exact.format_exact_report(self.certificate)
        self.assertIn("histogram={190:624,220:1}", report)
        self.assertIn("RESULT optimum=5939/7500", report)
        run = subprocess.run(
            (
                sys.executable,
                "-O",
                "-c",
                "from notes.entropy_selection.coupled_horizon6 import "
                "build_exact_coupled_horizon6; build_exact_coupled_horizon6()",
            ),
            capture_output=True,
            check=False,
            text=True,
        )
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("optimized Python disables required assertion gates", run.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
