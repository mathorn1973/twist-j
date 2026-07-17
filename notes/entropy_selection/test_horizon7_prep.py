"""Replay tests for the horizon-7 preparation layer (NON-CANONICAL).

Cost note: the special-block DP at induced width 8 runs about three
minutes once per process; every test below shares that single cached
build.
"""

from __future__ import annotations

import io
import subprocess
import sys
import unittest
from collections import Counter
from contextlib import redirect_stdout
from dataclasses import replace
from math import lcm

try:
    from . import horizon7_prep as prep
    from .bounds import constraint_graph
    from .coupled_horizon5 import EXPECTED_PIN_GRID
    from .path_bounds import anchor_terminals
except ImportError:  # Direct execution from this directory.
    import horizon7_prep as prep  # type: ignore[no-redef]
    from bounds import constraint_graph  # type: ignore[no-redef]
    from coupled_horizon5 import EXPECTED_PIN_GRID  # type: ignore[no-redef]
    from path_bounds import anchor_terminals  # type: ignore[no-redef]


class Horizon7StructureTests(unittest.TestCase):
    def test_node_and_edge_census(self) -> None:
        graph = constraint_graph(3, 7)
        self.assertEqual(len(graph.nodes), prep.NODE_COUNT7)
        self.assertEqual(
            tuple(sorted(Counter(level for level, _ in graph.nodes).items())),
            prep.EXPECTED_NODE_CENSUS7,
        )
        self.assertEqual(len(graph.edges), prep.PAIR_COUNT7)
        self.assertEqual(
            tuple(
                sorted(
                    Counter(edge.lower_level for edge in graph.edges).items()
                )
            ),
            prep.EXPECTED_TRANSITION_PAIRS7,
        )

    def test_scale_stays_48(self) -> None:
        graph = constraint_graph(3, 7)
        denominators = [edge.weight.denominator for edge in graph.edges] + [
            terminal.weight.denominator for terminal in anchor_terminals()
        ]
        self.assertEqual(lcm(*denominators), prep.SCALE7)
        self.assertTrue(
            all(int(edge.weight * prep.SCALE7) > 0 for edge in graph.edges)
        )
        truncated = [
            edge.id for edge in graph.edges if int(edge.weight * 24) == 0
        ]
        # At 2..7 the 1/48 weights are no longer confined to the 5 -> 6
        # transition: 16 sit at lower level 5 and 32 at lower level 6.
        self.assertEqual(len(truncated), 48)
        self.assertEqual(
            {edge.lower_level for edge in graph.edges if edge.id in set(truncated)},
            {5, 6},
        )
        self.assertEqual(
            Counter(
                edge.lower_level
                for edge in graph.edges
                if edge.id in set(truncated)
            ),
            Counter({5: 16, 6: 32}),
        )

    def test_scale48_is_horizon_local_not_asymptotic(self) -> None:
        def exact_scale(maximum_level: int) -> int:
            graph = constraint_graph(3, maximum_level)
            denominators = [
                edge.weight.denominator for edge in graph.edges
            ] + [
                terminal.weight.denominator
                for terminal in anchor_terminals()
            ]
            return lcm(*denominators)

        self.assertEqual(
            tuple(exact_scale(level) for level in (5, 7, 9, 10, 18)),
            (24, 48, 48, 96, 192),
        )

    def test_isolated_transition_slices_have_zero_holonomy(self) -> None:
        graph, _, transports, _ = prep._graph_and_transports()
        replay = []
        for lower_level in (4, 5, 6):
            edge_ids = tuple(
                edge_id
                for edge_id, edge in enumerate(graph.edges)
                if edge.lower_level == lower_level
            )
            vertices = {
                vertex
                for edge_id in edge_ids
                for vertex in transports[edge_id][:2]
            }
            adjacency = {vertex: [] for vertex in vertices}
            for edge_id in edge_ids:
                upper, lower, forward, reverse = transports[edge_id]
                adjacency[upper].append((lower, edge_id, forward))
                adjacency[lower].append((upper, edge_id, reverse))

            gauges: dict[int, tuple[int, ...]] = {}
            components = 0
            inconsistencies = 0
            for root in sorted(vertices):
                if root in gauges:
                    continue
                components += 1
                gauges[root] = prep.IDENTITY
                queue = [root]
                while queue:
                    here = queue.pop(0)
                    for neighbor, edge_id, transport in sorted(
                        adjacency[here], key=lambda item: (item[0], item[1])
                    ):
                        candidate = prep.compose(transport, gauges[here])
                        if neighbor not in gauges:
                            gauges[neighbor] = candidate
                            queue.append(neighbor)
                        elif gauges[neighbor] != candidate:
                            inconsistencies += 1

            replay.append(
                (
                    lower_level,
                    len(edge_ids),
                    len(vertices),
                    components,
                    len(edge_ids) - len(vertices) + components,
                    inconsistencies,
                )
            )

        self.assertEqual(
            tuple(replay),
            (
                (4, 24, 22, 4, 6, 0),
                (5, 32, 28, 6, 10, 0),
                (6, 40, 36, 6, 10, 0),
            ),
        )

    def test_thue_morse_complexity_matches_node_census(self) -> None:
        self.assertEqual(
            prep.thue_morse_complexity((3, 4, 5, 6, 7)),
            tuple(count for _, count in prep.EXPECTED_NODE_CENSUS7),
        )


class Horizon7SpecialBlockTests(unittest.TestCase):
    def test_special_block_closed_and_verified(self) -> None:
        report = prep.build_special_horizon7()
        self.assertTrue(prep.verify_special_horizon7(report))
        self.assertTrue(report.closed)
        self.assertEqual(report.coordinate_optima, (52,) * 5)
        self.assertEqual(report.scaled_lower_bound, 260)
        self.assertEqual(report.reassembled_cost, 260)
        self.assertEqual(report.maximum_width, prep.EXPECTED_SPECIAL_WIDTH7)
        self.assertEqual(
            report.reassembled_bad, prep.EXPECTED_REASSEMBLED_BAD7
        )
        self.assertEqual(len(report.reassembled_bad), 22)

    def test_retraction_and_pins(self) -> None:
        report = prep.build_special_horizon7()
        structure = report.structure
        self.assertEqual(structure.orbit_count, 625)
        self.assertEqual(structure.orbit_size, 5)
        self.assertEqual(structure.commutation_checks, 116 * 3125)
        self.assertTrue(structure.pins_equal_horizon5)
        self.assertTrue(structure.pins_fixed)
        self.assertEqual(structure.cycle_rank, 53)
        self.assertEqual(structure.nonidentity_chords, 39)
        self.assertEqual(prep._pins(), EXPECTED_PIN_GRID)

    def test_marginal_ladder_two_consecutive_forties(self) -> None:
        report = prep.build_special_horizon7()
        self.assertEqual(
            report.special_minima_scale48, (120, 180, 220, 260)
        )
        self.assertEqual(report.special_marginals_scale48, (60, 40, 40))
        # Geometric decay of the special marginal is refuted: 5/6 of 40
        # is not an integer step and the exact step is again 40.
        self.assertEqual(
            report.special_minima_scale48[-1]
            - report.special_minima_scale48[-2],
            40,
        )

    def test_report_format_is_frozen(self) -> None:
        report = prep.build_special_horizon7()
        expected = "\n".join(
            (
                "HORIZON 2..7 PREPARATION (special block closed; ordinary open)",
                "  scope=fixed-r2 structured finite boundary; scale=48"
                " (no new denominator at 6->7)",
                "  graph: nodes={3:6,4:10,5:12,6:16,7:20} pairs=116"
                " (20+24+32+40) anchors=12 cycle-rank=53",
                "  retraction: orbits=625x5 chords=39 checks=362500"
                " pins=horizon-5 grid, fixed",
                "  special DP: width=8 optima=(52,52,52,52,52) total=260",
                "  special reassembly: all-different OK cost=260 bad-edges=22",
                "  special CLOSED: lower=upper=260; marginal +40 (scale 48)",
                "  special minima ladder 120,180,220,260:"
                " marginals +60,+40,+40",
                "  ordinary block: vars=320 pairs=580 pins=60 -- OUTSIDE THIS"
                " PREP MODULE",
                "  RESULT special=260/150000-scale [NON-CANONICAL prep only]",
            )
        )
        self.assertEqual(
            prep.format_prep_report(report), expected
        )

        stream = io.StringIO()
        with redirect_stdout(stream):
            self.assertEqual(prep.main(), 0)
        self.assertEqual(
            stream.getvalue(),
            "ENTROPY-SELECTION HORIZON-7 PREP CHECK\n"
            "NON-CANONICAL / NON-FORMAL / NO CLAIM STATUS\n"
            + expected
            + "\n",
        )

    def test_verifier_rejects_exact_type_lookalikes(self) -> None:
        report = prep.build_special_horizon7()
        self.assertFalse(
            prep.verify_special_horizon7(replace(report, maximum_width=8.0))
        )
        self.assertFalse(
            prep.verify_special_horizon7(
                replace(
                    report,
                    structure=replace(report.structure, orbit_count=625.0),
                )
            )
        )
        self.assertFalse(
            prep.verify_special_horizon7(
                replace(
                    report,
                    structure=replace(report.structure, scale=48.0),
                )
            )
        )
        self.assertFalse(
            prep.verify_special_horizon7(
                replace(report, structure=None)  # type: ignore[arg-type]
            )
        )
        self.assertFalse(
            prep.verify_special_horizon7(
                replace(
                    report,
                    structure=replace(
                        report.structure,
                        node_census=((3, 6.0),)
                        + report.structure.node_census[1:],
                    ),
                )
            )
        )
        self.assertFalse(
            prep.verify_special_horizon7(
                replace(
                    report,
                    structure=replace(
                        report.structure,
                        tm_complexity=(6.0,)
                        + report.structure.tm_complexity[1:],
                    ),
                )
            )
        )
        self.assertFalse(
            prep.verify_special_horizon7(
                replace(
                    report,
                    structure=replace(report.structure, pins_fixed=1),
                )
            )
        )
        self.assertFalse(
            prep.verify_special_horizon7(
                replace(
                    report,
                    coordinate_optima=(52, 52, 52, 52, True),
                )
            )
        )
        with self.assertRaises(ValueError):
            prep.format_prep_report(replace(report, maximum_width=8.0))

    def test_optimized_python_is_explicitly_refused(self) -> None:
        run = subprocess.run(
            (
                sys.executable,
                "-O",
                "-c",
                "from notes.entropy_selection.horizon7_prep import "
                "build_special_horizon7; build_special_horizon7()",
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
    unittest.main()
