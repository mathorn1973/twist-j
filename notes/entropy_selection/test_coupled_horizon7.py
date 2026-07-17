#!/usr/bin/env python3
"""Exact gates for the NON-CANONICAL coupled horizon ``2..7``."""

from __future__ import annotations

from collections import Counter
from dataclasses import replace
from fractions import Fraction
import subprocess
import sys
import unittest

try:
    from . import coupled_horizon7 as exact
except ImportError:  # Direct execution from this directory.
    import coupled_horizon7 as exact  # type: ignore[no-redef]


class ExactCoupledHorizon7Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = exact.build_exact_coupled_horizon7()

    def test_ordinary_exact_lower_and_lifted_reassembly(self) -> None:
        report = self.certificate.ordinary
        self.assertTrue(exact.ordinary.verify_ordinary_horizon7(report))
        self.assertEqual(report.optimum, 220)
        self.assertEqual(report.lifted_block_count, 624)
        self.assertEqual(dict(report.lifted_cost_census), {220: 624})
        self.assertEqual(report.retraction.variable_count, 320)
        self.assertEqual(report.retraction.pair_count, 580)
        self.assertEqual(report.retraction.pin_count, 60)
        self.assertEqual(report.retraction.orbit_count, 625)
        self.assertEqual(report.retraction.orbit_size, 5)

    def test_special_exact_lower_and_reassembly(self) -> None:
        report = self.certificate.special
        self.assertTrue(exact.prep.verify_special_horizon7(report))
        self.assertTrue(report.closed)
        self.assertEqual(report.coordinate_optima, (52,) * 5)
        self.assertEqual(report.scaled_lower_bound, 260)
        self.assertEqual(report.reassembled_cost, 260)
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
            Counter({220: 624, 260: 1}),
        )
        self.assertEqual(
            witness.transition_distances,
            (
                Fraction(209, 2500),
                Fraction(3751, 7500),
                Fraction(937, 3750),
                Fraction(1, 12),
                Fraction(0),
            ),
        )
        self.assertEqual(witness.objective, Fraction(6877, 7500))

    def test_root_closes_only_at_exact_lower_upper_equality(self) -> None:
        certificate = self.certificate
        self.assertTrue(exact.verify_exact_coupled_horizon7(certificate))
        self.assertEqual(certificate.assignment_price, 0)
        self.assertEqual(certificate.assignment_minima, (0,) * 64)
        self.assertEqual(
            certificate.block_minima,
            certificate.witness.per_block_scaled_costs,
        )
        self.assertEqual(
            (certificate.scaled_lower_bound, certificate.scaled_upper_bound),
            (137540, 137540),
        )
        self.assertEqual(certificate.optimum, Fraction(6877, 7500))
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
            exact.ordinary.verify_ordinary_horizon7(
                replace(ordinary, optimum=ordinary.optimum + 1)
            )
        )
        self.assertFalse(
            exact.ordinary.verify_ordinary_horizon7(
                replace(ordinary, optimum=220.0)
            )
        )
        special = certificate.special
        self.assertFalse(
            exact.prep.verify_special_horizon7(
                replace(special, reassembled_cost=260.0)
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
                replace(witness, families=(None,) * 6)  # type: ignore[arg-type]
            )
        )
        minima = list(certificate.block_minima)
        minima[0] += 1
        self.assertFalse(
            exact.verify_exact_coupled_horizon7(
                replace(certificate, block_minima=tuple(minima))
            )
        )
        self.assertFalse(
            exact.verify_exact_coupled_horizon7(
                replace(certificate, assignment_price=0.0)
            )
        )
        self.assertFalse(
            exact.verify_exact_coupled_horizon7(
                replace(certificate, root_nodes=True)
            )
        )

    def test_report_is_deterministic_and_optimized_python_is_refused(self) -> None:
        report = exact.format_exact_report(self.certificate)
        self.assertIn("histogram={220:624,260:1}", report)
        self.assertIn("RESULT optimum=6877/7500", report)
        run = subprocess.run(
            (
                sys.executable,
                "-O",
                "-c",
                "from notes.entropy_selection.coupled_horizon7 import "
                "build_exact_coupled_horizon7; build_exact_coupled_horizon7()",
            ),
            capture_output=True,
            check=False,
            text=True,
        )
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("optimized Python disables required assertion gates", run.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
