#!/usr/bin/env python3
"""Tests for the non-normative architecture-map ledger report."""

from __future__ import annotations

import contextlib
import io
from pathlib import Path
import sys
import unittest


TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import architecture_map_report as architecture  # noqa: E402


class ArchitectureMapReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = architecture.audit(ROOT)

    def test_anchored_counts_match_the_public_summary(self) -> None:
        self.assertEqual(self.report.claims, 239)
        self.assertEqual(
            self.report.status_counts,
            {"C": 27, "D": 41, "F": 13, "H": 2, "O": 23, "T": 133},
        )
        self.assertEqual(
            self.report.evidence_counts,
            {
                "none": 41,
                "one-architecture": 9,
                "recorded-audit": 31,
                "two-architecture": 158,
            },
        )
        self.assertFalse(self.report.count_mismatches)

    def test_architecture_is_a_hub_not_the_only_non_algebraic_root(self) -> None:
        self.assertEqual(len(self.report.direct_architecture_requires), 175)
        self.assertEqual(
            len(self.report.transitive_architecture_dependents), 194
        )
        self.assertEqual(len(self.report.dependency_terminals), 22)
        self.assertNotIn(
            "KERNEL-Z6-SYNCHRONIZATION",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "KERNEL-Z6-SYNCHRONIZATION",
            self.report.transitive_architecture_dependents,
        )
        self.assertIn(
            "GYRON-DISCREPANCY-LOG",
            self.report.direct_architecture_requires,
        )
        self.assertIn(
            "METRO-REDUCTION-ARROWS",
            self.report.direct_architecture_requires,
        )
        self.assertIn(
            "METRO-REDUCTION-ARROWS",
            self.report.transitive_architecture_dependents,
        )
        self.assertIn(
            "TM-PAIR-SUBSTITUTION-FIXED-POINT",
            self.report.direct_architecture_requires,
        )
        self.assertIn(
            "MINIMAL-READ-DERIVATION",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "OBSERVER-WRITE-PORT",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "OBSERVER-WRITE-PORT",
            self.report.transitive_architecture_dependents,
        )
        self.assertIn(
            "TM-SYM2-SPECTRAL-COHERENCE",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "DRIFT-IS-THE-READ",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "COLOR-CM-2I-SEMILINEAR-PAIR",
            self.report.direct_architecture_requires,
        )
        self.assertIn(
            "COLOR-CM-2I-SEMILINEAR-PAIR",
            self.report.transitive_architecture_dependents,
        )
        self.assertNotIn(
            "CENTRAL-LIFT-PHASE",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "CENTRAL-LIFT-PHASE",
            self.report.transitive_architecture_dependents,
        )
        self.assertNotIn(
            "QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS",
            self.report.direct_architecture_requires,
        )
        self.assertIn(
            "QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS",
            self.report.transitive_architecture_dependents,
        )
        self.assertNotIn(
            "ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM",
            self.report.transitive_architecture_dependents,
        )
        self.assertNotIn(
            "CM-ALTERNATING-PENCIL",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "CM-ALTERNATING-PENCIL",
            self.report.transitive_architecture_dependents,
        )
        self.assertNotIn(
            "J-HARMONIC-SEAM",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "J-HARMONIC-SEAM",
            self.report.transitive_architecture_dependents,
        )
        self.assertNotIn(
            "MOBIUS-TM-PRIME2-BRIDGE",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "MOBIUS-TM-PRIME2-BRIDGE",
            self.report.transitive_architecture_dependents,
        )
        self.assertIn(
            "MOBIUS-TM-PRIME2-BRIDGE", self.report.dependency_terminals
        )
        self.assertNotIn(
            "TM-MULTIPLICATION-CARRY-DEFECT",
            self.report.direct_architecture_requires,
        )
        self.assertNotIn(
            "TM-MULTIPLICATION-CARRY-DEFECT",
            self.report.transitive_architecture_dependents,
        )
        self.assertIn(
            "TM-MULTIPLICATION-CARRY-DEFECT",
            self.report.dependency_terminals,
        )
        for claim in (
            "TM-HANKEL-DIVISOR-BRIDGE",
            "TM-HANKEL-SQUAREFUL-RANK-NOGO",
            "TM-HANKEL-EXTREMAL-WITT-SKELETON",
            "TM-HANKEL-K2-TRANSFER",
            "TM-HANKEL-K3-UNIVERSAL-TRANSFER",
            "TM-HANKEL-K3-TWO-SCALAR-CLASSIFICATION",
            "TM-HANKEL-K3-QUADRATIC-INVARIANT-SUFFICIENCY",
            "ARITHMETIC-RAPIDITY-DECOMPOSITION",
            "SPLIT-PRIME-RAPIDITY-CLASS",
            "SPLIT-PRIME-RAPIDITY-CONSTRUCTION-AGREEMENT",
        ):
            self.assertIn(claim, self.report.dependency_terminals)
            self.assertNotIn(claim, self.report.direct_architecture_requires)
            self.assertNotIn(
                claim, self.report.transitive_architecture_dependents
            )
        for claim in (
            "DRIFT-IS-THE-READ",
            "COIN-SELECTION-CONDITIONAL",
            "COIN-MINIMAL-READ",
            "MINIMAL-READ-DERIVATION",
        ):
            self.assertIn(
                claim, self.report.transitive_architecture_dependents
            )
        self.assertIn("ANCHOR-ELECTRON-MASS", self.report.dependency_terminals)
        self.assertIn(
            "METRO-FINITE-STATE-RATIONALITY", self.report.dependency_terminals
        )

    def test_section_16_wall_is_mixed(self) -> None:
        self.assertIn(
            "P5-ROOT-SELECTION", self.report.wall_architecture_dependent
        )
        self.assertIn(
            "J-LI-E8-SHELL-MULTIPLICITY-NOGO",
            self.report.wall_architecture_dependent,
        )
        self.assertIn(
            "MCKAY-THETA-FUNCTIONAL-CALCULUS-CARRIER",
            self.report.wall_architecture_dependent,
        )
        self.assertIn(
            "PENTAGON-NORMALIZATION", self.report.wall_architecture_free
        )
        self.assertIn("WALL-LI2-RUNG", self.report.wall_architecture_free)
        self.assertIn(
            "WALL-CIRCLE-LEMMA", self.report.wall_architecture_free
        )
        self.assertIn("J-LI-TORAL-HAAR-NOGO", self.report.wall_architecture_free)
        self.assertTrue(self.report.wall_architecture_dependent)
        self.assertTrue(self.report.wall_architecture_free)

    def test_census_edges_are_missing_or_honest_bounds(self) -> None:
        expected_missing = tuple(
            item
            for item in architecture.CENSUS_CONSUMERS
            if not self.report.census_edges[item]
        )
        self.assertEqual(self.report.census_missing, expected_missing)
        for relations in self.report.census_edges.values():
            self.assertNotIn("REQUIRES", relations)
            if relations:
                self.assertIn("BOUNDED_BY", relations)

    def test_census_debt_messages_distinguish_missing_bound_and_premise(self) -> None:
        def make_report(relations: tuple[str, ...]) -> architecture.AuditReport:
            edges = {item: relations for item in architecture.CENSUS_CONSUMERS}
            missing = tuple(item for item, values in edges.items() if not values)
            wrong = tuple(
                item
                for item, values in edges.items()
                if values and "BOUNDED_BY" not in values
            )
            return architecture.AuditReport(
                claims=0,
                status_counts={},
                evidence_counts={},
                direct_architecture_requires=(),
                transitive_architecture_dependents=(),
                dependency_terminals=(),
                wall_architecture_dependent=("BOUND",),
                wall_architecture_free=("FREE",),
                census_edges=edges,
                census_missing=missing,
                census_wrong_relation=wrong,
                count_mismatches=(),
            )

        self.assertIn("missing CENSUS-313 bounds", make_report(()).debt[0])
        self.assertFalse(make_report(("BOUNDED_BY",)).debt)
        self.assertIn("must include BOUNDED_BY", make_report(("REQUIRES",)).debt[0])

    def test_cli_exit_codes_distinguish_report_from_gate(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            default_code = architecture.main(["--root", str(ROOT)])
            strict_code = architecture.main(["--root", str(ROOT), "--strict"])
        self.assertEqual(default_code, 0)
        self.assertEqual(strict_code, 1 if self.report.debt else 0)
        if self.report.debt:
            self.assertIn("Debt", output.getvalue())


if __name__ == "__main__":
    unittest.main()
