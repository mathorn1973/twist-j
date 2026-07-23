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
        self.assertEqual(self.report.claims, 200)
        self.assertEqual(
            self.report.status_counts,
            {"C": 22, "D": 40, "F": 10, "H": 4, "O": 21, "T": 103},
        )
        self.assertEqual(
            self.report.evidence_counts,
            {
                "none": 39,
                "one-architecture": 8,
                "recorded-audit": 31,
                "two-architecture": 122,
            },
        )
        self.assertFalse(self.report.count_mismatches)

    def test_architecture_is_a_hub_not_the_only_non_algebraic_root(self) -> None:
        self.assertEqual(len(self.report.direct_architecture_requires), 166)
        self.assertEqual(
            len(self.report.transitive_architecture_dependents), 179
        )
        self.assertGreater(len(self.report.dependency_terminals), 2)
        self.assertIn("ANCHOR-ELECTRON-MASS", self.report.dependency_terminals)

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
