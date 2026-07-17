#!/usr/bin/env python3
"""Exact gates for the NON-CANONICAL horizon-7 ordinary certificate."""

from __future__ import annotations

from collections import Counter
from dataclasses import replace
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import subprocess
import sys
import unittest

try:
    from . import horizon7_ordinary as ordinary
except ImportError:  # Direct execution from this directory.
    import horizon7_ordinary as ordinary  # type: ignore[no-redef]


class Horizon7OrdinaryCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = ordinary.build_ordinary_horizon7()

    def test_full_bundle_retraction_and_pin_contract(self) -> None:
        report = self.report.retraction
        self.assertEqual(
            report,
            ordinary.RetractionHorizon7Report(
                variable_count=320,
                pair_count=580,
                pin_count=60,
                tree_edge_count=319,
                cycle_rank=261,
                holonomy_shifts=(0, 2, 3),
                generated_shift_count=5,
                orbit_count=625,
                orbit_size=5,
                commutation_checks=1_812_500,
                fixed_pin_checks=60,
                structure_table_checks=1_000_000,
                structure_table_sha256=ordinary.EXPECTED_STRUCTURE_TABLE_SHA256,
                pin_pattern_sha256=ordinary.EXPECTED_PIN_PATTERN_SHA256,
            ),
        )
        records = ordinary._records()
        self.assertEqual(len(records), 640)
        self.assertTrue(
            all(type(record) is ordinary.PairRecord for record in records[:580])
        )
        self.assertTrue(
            all(type(record) is ordinary.PinRecord for record in records[580:])
        )
        self.assertEqual(
            Counter(record.weight for record in records[:580]),
            Counter({1: 240, 2: 320, 4: 20}),
        )
        self.assertEqual(
            Counter(record.weight for record in records[580:]),
            Counter({4: 60}),
        )

    def test_exact_bnb_closes_every_reassemblable_branch(self) -> None:
        bnb = self.report.bnb
        self.assertEqual(
            bnb,
            ordinary.BnbHorizon7Report(
                node_count=1_181,
                branch_count=236,
                dual_leaf_count=190,
                invalid_leaf_count=755,
                row_count=2_013,
                dual_count=190,
                max_depth=11,
                dual_check_count=2_911_700,
                denominator_census=((1, 163), (2, 21), (3, 5), (4, 1)),
                minimum_bound=Fraction(220),
                model_sha256=ordinary.EXPECTED_MODEL_SHA256,
                certificate_sha256=ordinary.EXPECTED_BNB_SHA256,
            ),
        )
        self.assertEqual(self.report.optimum, 220)
        self.assertEqual(self.report.violation_weight_census, ((2, 90), (4, 10)))
        self.assertEqual(len(self.report.violated_records), 100)
        self.assertTrue(ordinary.verify_ordinary_horizon7(self.report))

    def test_hall_leaves_are_a_required_reassembly_gate(self) -> None:
        valid_domains = tuple(1 << value for value in self.report.assignment)
        self.assertIsNone(ordinary._first_hall_violation(valid_domains))
        invalid_domains = (1,) * ordinary.VARIABLE_COUNT
        violation = ordinary._first_hall_violation(invalid_domains)
        self.assertIsNotNone(violation)
        node, subset, union = violation  # type: ignore[misc]
        self.assertLess(union.bit_count(), subset.bit_count())
        self.assertIn(node, range(ordinary.NODE_COUNT))

    def test_certificate_files_are_exactly_pinned(self) -> None:
        directory = Path(ordinary.__file__).parent
        bnb = (directory / ordinary.BNB_FILENAME).read_bytes()
        solution = (directory / ordinary.SOLUTION_FILENAME).read_bytes()
        self.assertEqual(len(bnb), ordinary.EXPECTED_BNB_BYTES)
        self.assertEqual(sha256(bnb).hexdigest(), ordinary.EXPECTED_BNB_SHA256)
        self.assertEqual(
            sha256(solution).hexdigest(), ordinary.EXPECTED_SOLUTION_SHA256
        )
        self.assertEqual(
            sha256(bytes(self.report.assignment)).hexdigest(),
            ordinary.EXPECTED_ASSIGNMENT_SHA256,
        )

    def test_violation_support_is_full_five_orbits(self) -> None:
        pair_support = [
            item for item in self.report.violated_records if item < 580
        ]
        pin_support = [
            item - 580 for item in self.report.violated_records if item >= 580
        ]
        pair_groups = Counter(item // 5 for item in pair_support)
        pin_groups = Counter(item // 5 for item in pin_support)
        self.assertEqual(len(pair_groups), 19)
        self.assertEqual(set(pair_groups.values()), {5})
        self.assertEqual(pin_groups, Counter({0: 5}))
        self.assertEqual(
            pair_support,
            [5 * group + point for group in sorted(pair_groups) for point in range(5)],
        )

    def test_all_ordinary_fibers_reassemble_and_replay_at_220(self) -> None:
        graph, labels, node_cells = ordinary.lifted_ordinary_labels()
        self.assertEqual((len(graph.nodes), len(graph.edges)), (64, 116))
        self.assertEqual(len(labels), 624)
        self.assertTrue(all(len(block_labels) == 64 for block_labels in labels))
        self.assertEqual(len(node_cells), 64)
        self.assertEqual({len(cells) for cells in node_cells}, {624})
        self.assertTrue(
            all(
                set(label.permutation) == set(range(5))
                for block_labels in labels
                for label in block_labels
            )
        )
        self.assertEqual(self.report.lifted_block_count, 624)
        self.assertEqual(self.report.lifted_cost_census, ((220, 624),))

    def test_report_format_is_frozen(self) -> None:
        expected = "\n".join(
            (
                "HORIZON 2..7 ORDINARY EXACT CERTIFICATE",
                "  point bundle: vars=320 pairs=580 pins=60 tree=319 chords=261",
                "  retraction: shifts=(0,2,3) generates=Z5 orbits=625x5"
                " checks=1812500 pins-fixed=60 structure-table=1000000",
                "  exact B&B: nodes=1181 branches=236 dual-leaves=190"
                " Hall-leaves=755 depth=11",
                "  exact leaf replay: inequalities=2911700 min-bound=220"
                " denominators={1:163,2:21,3:5,4:1}",
                "  primal replay: cost=220 violated=100 assignment="
                + ordinary.EXPECTED_ASSIGNMENT_SHA256,
                "  lift: ordinary-blocks=624 reassembly=PASS all-different=PASS"
                " label-costs={220:624}",
                "  RESULT ordinary=220 [NON-CANONICAL finite-horizon only]",
            )
        )
        self.assertEqual(ordinary.format_ordinary_report(self.report), expected)

    def test_verifier_rejects_tampering_and_numeric_lookalikes(self) -> None:
        report = self.report
        self.assertFalse(
            ordinary.verify_ordinary_horizon7(replace(report, optimum=220.0))
        )
        assignment = list(report.assignment)
        assignment[0] = True
        self.assertFalse(
            ordinary.verify_ordinary_horizon7(
                replace(report, assignment=tuple(assignment))
            )
        )
        self.assertFalse(
            ordinary.verify_ordinary_horizon7(
                replace(report, bnb=replace(report.bnb, max_depth=11.0))
            )
        )
        self.assertFalse(
            ordinary.verify_ordinary_horizon7(
                replace(report, violation_weight_census=((2, 90), (4, True)))
            )
        )
        self.assertFalse(
            ordinary.verify_ordinary_horizon7(
                replace(report, violated_records=(None,) * 100)  # type: ignore[arg-type]
            )
        )

    def test_optimized_python_is_explicitly_refused(self) -> None:
        run = subprocess.run(
            (
                sys.executable,
                "-O",
                "-c",
                "from notes.entropy_selection.horizon7_ordinary import "
                "build_ordinary_horizon7; build_ordinary_horizon7()",
            ),
            capture_output=True,
            check=False,
            text=True,
        )
        self.assertNotEqual(run.returncode, 0)
        self.assertIn(
            "optimized Python disables required assertion gates", run.stderr
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
