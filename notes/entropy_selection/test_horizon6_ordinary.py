#!/usr/bin/env python3
"""Exact gates for the NON-CANONICAL horizon-6 ordinary certificate."""

from __future__ import annotations

from collections import Counter
from dataclasses import replace
from hashlib import sha256
from pathlib import Path
import subprocess
import sys
import unittest

try:
    from . import horizon6_ordinary as ordinary
except ImportError:  # Direct execution from this directory.
    import horizon6_ordinary as ordinary  # type: ignore[no-redef]


class Horizon6OrdinaryCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = ordinary.build_ordinary_horizon6()

    def test_full_bundle_retraction_and_pin_contract(self) -> None:
        report = self.report.retraction
        self.assertEqual(
            report,
            ordinary.RetractionHorizon6Report(
                variable_count=220,
                pair_count=380,
                pin_count=60,
                tree_edge_count=219,
                cycle_rank=161,
                holonomy_shifts=(0, 2, 3),
                generated_shift_count=5,
                orbit_count=625,
                orbit_size=5,
                commutation_checks=1_187_500,
                fixed_pin_checks=60,
                pin_pattern_sha256=ordinary.EXPECTED_PIN_PATTERN_SHA256,
            ),
        )
        records = ordinary._records()
        self.assertEqual(len(records), 440)
        self.assertTrue(
            all(type(record) is ordinary.PairRecord for record in records[:380])
        )
        self.assertTrue(
            all(type(record) is ordinary.PinRecord for record in records[380:])
        )
        self.assertEqual(
            Counter(record.weight for record in records[:380]),
            Counter({1: 80, 2: 280, 4: 20}),
        )
        self.assertEqual(
            Counter(record.weight for record in records[380:]),
            Counter({4: 60}),
        )

    def test_integral_dual_equals_primal_replay(self) -> None:
        report = self.report
        self.assertTrue(ordinary.verify_ordinary_horizon6(report))
        self.assertEqual(report.dual_denominator, 1)
        self.assertEqual(report.dual_check_count, 10_600)
        self.assertEqual(report.dual_objective, 190)
        self.assertEqual(report.optimum, 190)
        self.assertEqual(report.violation_weight_census, ((2, 65), (4, 15)))
        self.assertEqual(len(report.violated_records), 80)
        self.assertEqual(
            sha256(bytes(report.assignment)).hexdigest(),
            ordinary.EXPECTED_ASSIGNMENT_SHA256,
        )

    def test_certificate_files_are_exactly_pinned(self) -> None:
        directory = Path(ordinary.__file__).parent
        self.assertEqual(
            sha256((directory / ordinary.DUAL_FILENAME).read_bytes()).hexdigest(),
            ordinary.EXPECTED_DUAL_SHA256,
        )
        self.assertEqual(
            sha256(
                (directory / ordinary.SOLUTION_FILENAME).read_bytes()
            ).hexdigest(),
            ordinary.EXPECTED_SOLUTION_SHA256,
        )

    def test_violation_support_is_full_five_orbits(self) -> None:
        pair_support = [
            item for item in self.report.violated_records if item < 380
        ]
        pin_support = [
            item - 380 for item in self.report.violated_records if item >= 380
        ]
        pair_groups = Counter(item // 5 for item in pair_support)
        pin_groups = Counter(item // 5 for item in pin_support)
        self.assertEqual(len(pair_groups), 14)
        self.assertEqual(set(pair_groups.values()), {5})
        self.assertEqual(pin_groups, Counter({0: 5, 1: 5}))
        self.assertEqual(
            pair_support,
            [5 * group + point for group in sorted(pair_groups) for point in range(5)],
        )

    def test_all_ordinary_fibers_reassemble_and_replay_at_190(self) -> None:
        graph, labels, node_cells = ordinary.lifted_ordinary_labels()
        self.assertEqual((len(graph.nodes), len(graph.edges)), (44, 76))
        self.assertEqual(len(labels), 624)
        self.assertTrue(all(len(block_labels) == 44 for block_labels in labels))
        self.assertEqual(len(node_cells), 44)
        self.assertEqual({len(cells) for cells in node_cells}, {624})
        self.assertTrue(
            all(
                set(label.permutation) == set(range(5))
                for block_labels in labels
                for label in block_labels
            )
        )
        self.assertEqual(self.report.lifted_block_count, 624)
        self.assertEqual(self.report.lifted_cost_census, ((190, 624),))

    def test_report_format_is_frozen(self) -> None:
        expected = "\n".join(
            (
                "HORIZON 2..6 ORDINARY EXACT CERTIFICATE",
                "  point bundle: vars=220 pairs=380 pins=60 tree=219 chords=161",
                "  retraction: shifts=(0,2,3) generates=Z5 orbits=625x5"
                " checks=1187500 pins-fixed=60",
                "  local-polytope dual: denominator=1 inequalities=10600"
                " objective=190",
                "  primal replay: cost=190 violated=80 assignment="
                + ordinary.EXPECTED_ASSIGNMENT_SHA256,
                "  lift: ordinary-blocks=624 reassembly=PASS all-different=PASS"
                " label-costs={190:624}",
                "  RESULT ordinary=190 [NON-CANONICAL finite-horizon only]",
            )
        )
        self.assertEqual(ordinary.format_ordinary_report(self.report), expected)

    def test_verifier_rejects_tampering_and_numeric_lookalikes(self) -> None:
        report = self.report
        self.assertFalse(
            ordinary.verify_ordinary_horizon6(replace(report, optimum=190.0))
        )
        assignment = list(report.assignment)
        assignment[0] = True
        self.assertFalse(
            ordinary.verify_ordinary_horizon6(
                replace(report, assignment=tuple(assignment))
            )
        )
        self.assertFalse(
            ordinary.verify_ordinary_horizon6(
                replace(
                    report,
                    retraction=replace(report.retraction, cycle_rank=161.0),
                )
            )
        )
        self.assertFalse(
            ordinary.verify_ordinary_horizon6(
                replace(report, violation_weight_census=((2, 65), (4, True)))
            )
        )
        self.assertFalse(
            ordinary.verify_ordinary_horizon6(
                replace(report, violated_records=(None,) * 80)  # type: ignore[arg-type]
            )
        )

    def test_optimized_python_is_explicitly_refused(self) -> None:
        run = subprocess.run(
            (
                sys.executable,
                "-O",
                "-c",
                "from notes.entropy_selection.horizon6_ordinary import "
                "build_ordinary_horizon6; build_ordinary_horizon6()",
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
