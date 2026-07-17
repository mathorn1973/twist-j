"""Replay tests for the horizon-6 preparation layer (NON-CANONICAL)."""

from __future__ import annotations

import unittest
from collections import Counter
from dataclasses import replace
from math import lcm

try:
    from . import horizon6_prep as prep
    from .bounds import constraint_graph
    from .coupled_horizon5 import EXPECTED_PIN_GRID
    from .path_bounds import anchor_terminals
except ImportError:  # Direct execution from this directory.
    import horizon6_prep as prep  # type: ignore[no-redef]
    from bounds import constraint_graph  # type: ignore[no-redef]
    from coupled_horizon5 import EXPECTED_PIN_GRID  # type: ignore[no-redef]
    from path_bounds import anchor_terminals  # type: ignore[no-redef]


class Horizon6StructureTests(unittest.TestCase):
    def test_node_and_edge_census(self) -> None:
        graph = constraint_graph(3, 6)
        self.assertEqual(len(graph.nodes), prep.NODE_COUNT6)
        self.assertEqual(
            tuple(sorted(Counter(level for level, _ in graph.nodes).items())),
            prep.EXPECTED_NODE_CENSUS,
        )
        self.assertEqual(len(graph.edges), prep.PAIR_COUNT6)
        self.assertEqual(
            tuple(
                sorted(
                    Counter(edge.lower_level for edge in graph.edges).items()
                )
            ),
            prep.EXPECTED_TRANSITION_PAIRS,
        )

    def test_scale_is_48_and_scale24_truncates(self) -> None:
        graph = constraint_graph(3, 6)
        denominators = [edge.weight.denominator for edge in graph.edges] + [
            terminal.weight.denominator for terminal in anchor_terminals()
        ]
        self.assertEqual(lcm(*denominators), prep.SCALE6)
        truncated = [
            edge.id for edge in graph.edges if int(edge.weight * 24) == 0
        ]
        self.assertEqual(len(truncated), prep.EXPECTED_SCALE24_TRUNCATED)
        self.assertTrue(
            all(int(edge.weight * prep.SCALE6) > 0 for edge in graph.edges)
        )
        self.assertEqual(
            {edge.lower_level for edge in graph.edges if edge.id in set(truncated)},
            {5},
        )

    def test_thue_morse_complexity_matches_node_census(self) -> None:
        self.assertEqual(
            prep.thue_morse_complexity((3, 4, 5, 6)),
            tuple(count for _, count in prep.EXPECTED_NODE_CENSUS),
        )


class Horizon6SpecialBlockTests(unittest.TestCase):
    def test_special_block_closed_and_verified(self) -> None:
        report = prep.build_special_horizon6()
        self.assertTrue(prep.verify_special_horizon6(report))
        self.assertTrue(report.closed)
        self.assertEqual(report.coordinate_optima, (44,) * 5)
        self.assertEqual(report.scaled_lower_bound, 220)
        self.assertEqual(report.reassembled_cost, 220)
        self.assertEqual(report.maximum_width, prep.EXPECTED_SPECIAL_WIDTH6)
        self.assertEqual(
            report.reassembled_bad, prep.EXPECTED_REASSEMBLED_BAD6
        )

    def test_retraction_and_pins(self) -> None:
        report = prep.build_special_horizon6()
        structure = report.structure
        self.assertEqual(structure.orbit_count, 625)
        self.assertEqual(structure.orbit_size, 5)
        self.assertEqual(structure.commutation_checks, 76 * 3125)
        self.assertTrue(structure.pins_equal_horizon5)
        self.assertTrue(structure.pins_fixed)
        self.assertEqual(structure.cycle_rank, 33)
        self.assertEqual(structure.nonidentity_chords, 25)
        self.assertEqual(prep._pins(), EXPECTED_PIN_GRID)

    def test_uniform_marginal_prediction_refuted(self) -> None:
        report = prep.build_special_horizon6()
        # From 2..4 to 2..5 every block minimum rose by +60 in scale 48
        # (40 -> 70 and 60 -> 90 in scale 24).  The uniform continuation
        # predicted special 180 + 60 = 240 at 2..6; the exact closure is 220.
        self.assertEqual(report.refuted_uniform_prediction, 240)
        self.assertEqual(report.reassembled_cost, 220)
        self.assertNotEqual(
            report.reassembled_cost, report.refuted_uniform_prediction
        )
        self.assertEqual(report.special_marginal_scale48, 40)

    def test_report_formatting_is_deterministic(self) -> None:
        report = prep.build_special_horizon6()
        expected = "\n".join(
            (
                "HORIZON 2..6 PREPARATION (special block closed; ordinary open)",
                "  scope=fixed-r2 structured finite boundary; scale=48"
                " (int(w*24) would zero 16 level-6 edges)",
                "  graph: nodes={3:6,4:10,5:12,6:16} pairs=76"
                " (20+24+32) anchors=12 cycle-rank=33",
                "  retraction: orbits=625x5 chords=25 checks=237500"
                " pins=horizon-5 grid, fixed",
                "  special DP: width=6 union-scope=7"
                " optima=(44,44,44,44,44) total=220",
                "  special reassembly: all-different OK cost=220"
                " bad-edges=16",
                "  special CLOSED: lower=upper=220; marginal +40 (scale 48)",
                "  uniform-marginal prediction 240 REFUTED by exact closure",
                "  ordinary block: vars=220 pairs=380 pins=60 -- OUTSIDE THIS"
                " PREP MODULE",
                "  RESULT special=220/150000-scale [NON-CANONICAL prep only]",
            )
        )
        self.assertEqual(
            prep.format_prep_report(report), expected
        )
        self.assertIn("special CLOSED", prep.format_prep_report(report))
        self.assertIn("REFUTED", prep.format_prep_report(report))

    def test_verifier_rejects_exact_type_lookalikes(self) -> None:
        report = prep.build_special_horizon6()
        self.assertFalse(
            prep.verify_special_horizon6(replace(report, maximum_width=6.0))
        )
        self.assertFalse(
            prep.verify_special_horizon6(
                replace(report, special_marginal_scale48=40.0)
            )
        )
        self.assertFalse(
            prep.verify_special_horizon6(
                replace(
                    report,
                    structure=replace(report.structure, orbit_count=625.0),
                )
            )
        )


if __name__ == "__main__":
    unittest.main()
