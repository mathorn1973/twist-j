"""Preparation layer for the exact coupled horizon ``2..7``.

NON-CANONICAL LOCAL ANALYSIS, PREPARATION GRADE.  This module extends the
full-domain retraction machinery to the ``2..7`` later graph and closes the
SPECIAL block exactly.  The ordinary block, the coupled witness, and any
certificate or readback are outside this module.  Nothing here earns claim
status, and a later closure of the remaining objects does not retroactively
turn this report into a formal run.

Certified here (assertion-gated, replayed by ``test_horizon7_prep.py``):

1.  Scale stability.  Unlike the ``5 -> 6`` step, the ``6 -> 7`` transition
    introduces no new weight denominator: the lcm over all ``2..7`` edge and
    anchor weights is still ``48``, with ``OBJECTIVE_SCALE = 48 * 3125``.
    The ``int(weight * 24)`` truncation trap now covers forty-eight edges
    (sixteen at lower level 5 and thirty-two at lower level 6): scale 24
    is wrong for every horizon from ``2..6`` on.
2.  Graph census.  Nodes per level ``{3: 6, 4: 10, 5: 12, 6: 16, 7: 20}``
    (the Thue--Morse factor complexity, cross-checked independently),
    116 pair edges (20 + 24 + 32 + 40 per transition), the unchanged 12
    level-3 anchors; scale-48 weight census ``{1: 48, 2: 64, 4: 4}``.
3.  Retraction extension.  The canonical tree gauge (63 tree edges, cycle
    rank 53, 39 nonidentity chord holonomies) again produces exactly 625
    orbits of size 5 with a five-fold canonical-map choice per orbit; the
    node retractions commute on all ``116 * 3125 = 362500`` edge-state
    pairs and fix all anchor pins; the pin grid equals the horizon-5 grid
    (the anchors live at level 3 and do not move).
4.  Special block closed at ``260`` (scale 48).  Exact min-sum elimination
    with the deterministic min-fill order pinned below (standard induced
    width 8) gives coordinate optima ``(52, 52, 52, 52, 52)``; the cyclic
    reassembly of the coordinate-0 assignment is a valid all-different
    label family of exact replayed cost ``260`` with 22 bad edges.
    Lower equals upper, so the special block is fathomed for ``2..7``.
5.  Marginal record.  The special-block minima now read (scale 48)
    ``120, 180, 220, 260`` for horizons ``2..4`` to ``2..7``: marginals
    ``+60, +40, +40``.  Two consecutive ``+40`` steps are evidence for a
    positive constant floor rather than decay; the dichotomy consequence
    is stated in ``ENTROPY-DICHOTOMY.md`` and no asymptotic claim is made
    here.

Cost note: the special DP at induced width 8 takes on the order of three
minutes of exact Fraction-free integer elimination; the replay test module
pays this once per process via the build cache.  Optimized Python (``-O``)
is refused because the audit relies on assertion gates.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import lcm

try:
    from .bounds import (
        SPECIAL_BLOCK,
        BlockLabel,
        _advance_label,
        _expected_half,
        _label_mismatches,
        _solver,
        constraint_graph,
    )
    from .coupled_horizon5 import (
        EXPECTED_PIN_GRID,
        _encode_state,
        compose,
        inverse,
    )
    from .horizon6_prep import thue_morse_complexity
    from .path_bounds import (
        _reverse_anchor,
        _terminal_label,
        anchor_terminals,
    )
except ImportError:  # Direct execution from this directory.
    from bounds import (  # type: ignore[no-redef]
        SPECIAL_BLOCK,
        BlockLabel,
        _advance_label,
        _expected_half,
        _label_mismatches,
        _solver,
        constraint_graph,
    )
    from coupled_horizon5 import (  # type: ignore[no-redef]
        EXPECTED_PIN_GRID,
        _encode_state,
        compose,
        inverse,
    )
    from horizon6_prep import thue_morse_complexity  # type: ignore[no-redef]
    from path_bounds import (  # type: ignore[no-redef]
        _reverse_anchor,
        _terminal_label,
        anchor_terminals,
    )


DOMAIN = 3125
SCALE7 = 48
OBJECTIVE_SCALE7 = SCALE7 * DOMAIN
MINIMUM_LEVEL = 3
MAXIMUM_LEVEL = 7
NODE_COUNT7 = 64
PAIR_COUNT7 = 116
PIN_COUNT = 12
IDENTITY = tuple(range(DOMAIN))

EXPECTED_NODE_CENSUS7 = ((3, 6), (4, 10), (5, 12), (6, 16), (7, 20))
EXPECTED_TRANSITION_PAIRS7 = ((3, 20), (4, 24), (5, 32), (6, 40))
EXPECTED_WEIGHT_CENSUS7 = ((1, 48), (2, 64), (4, 4))
EXPECTED_ANCHOR_SCALED7 = 4
EXPECTED_CYCLE_RANK7 = 53
EXPECTED_NONIDENTITY_CHORDS7 = 39
EXPECTED_COMMUTATION_CHECKS7 = PAIR_COUNT7 * DOMAIN

EXPECTED_MINFILL_ORDER7 = (
    44, 45, 46, 59, 60, 47, 48, 61, 62, 49, 50, 51, 52, 53, 54, 55,
    56, 57, 58, 63, 1, 2, 3, 4, 28, 29, 39, 30, 40, 31, 41, 32, 42,
    38, 0, 5, 34, 35, 27, 21, 20, 26, 19, 37, 36, 7, 12, 25, 6, 17,
    16, 11, 23, 22, 8, 9, 10, 13, 14, 15, 18, 24, 33, 43,
)
EXPECTED_SPECIAL_WIDTH7 = 8
EXPECTED_COORDINATE_OPTIMA7 = (52, 52, 52, 52, 52)
EXPECTED_SPECIAL_TOTAL7 = 260
EXPECTED_COORD0_ASSIGNMENT7 = (
    3, 3, 4, 0, 0, 1, 3, 4, 1, 3, 3, 0, 1, 3, 0, 1, 3, 3, 0, 0, 1,
    1, 3, 3, 2, 3, 0, 1, 3, 2, 2, 0, 0, 1, 3, 3, 1, 1, 3, 2, 2, 0,
    0, 0, 0, 0, 0, 3, 3, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 3, 3,
    2,
)
EXPECTED_COORD0_SHA256_7 = (
    "38d3d0c06cf2f286b07292a7daae31e913e068e87caac6ad158242b3975818ee"
)
EXPECTED_REASSEMBLED_BAD7 = (
    0, 1, 2, 4, 5, 9, 13, 14, 15, 16, 17, 18, 19, 21, 27, 36, 42,
    61, 74, 116, 118, 121,
)

SPECIAL_MINIMA_SCALE48 = (120, 180, 220, 260)   # horizons 2..4, 2..5, 2..6, 2..7
SPECIAL_MARGINALS_SCALE48 = (60, 40, 40)


@dataclass(frozen=True, slots=True)
class Horizon7StructureReport:
    node_census: tuple[tuple[int, int], ...]
    transition_pairs: tuple[tuple[int, int], ...]
    weight_census: tuple[tuple[int, int], ...]
    anchor_scaled: int
    scale: int
    tm_complexity: tuple[int, ...]
    cycle_rank: int
    nonidentity_chords: int
    orbit_count: int
    orbit_size: int
    commutation_checks: int
    pins_equal_horizon5: bool
    pins_fixed: bool


@dataclass(frozen=True, slots=True)
class SpecialHorizon7Report:
    structure: Horizon7StructureReport
    elimination_order: tuple[int, ...]
    maximum_width: int
    coordinate_optima: tuple[int, ...]
    scaled_lower_bound: int
    reassembled_cost: int
    reassembled_bad: tuple[int, ...]
    coord0_assignment_sha256: str
    closed: bool
    special_minima_scale48: tuple[int, ...]
    special_marginals_scale48: tuple[int, ...]


def _require_assertion_gates() -> None:
    if not __debug__:
        raise RuntimeError("optimized Python disables required assertion gates")


@lru_cache(maxsize=1)
def _graph_and_transports():
    graph = constraint_graph(MINIMUM_LEVEL, MAXIMUM_LEVEL)
    node_id = {node: index for index, node in enumerate(graph.nodes)}
    assert len(graph.nodes) == NODE_COUNT7
    assert (
        tuple(sorted(Counter(level for level, _ in graph.nodes).items()))
        == EXPECTED_NODE_CENSUS7
    )
    assert (
        tuple(sorted(Counter(edge.lower_level for edge in graph.edges).items()))
        == EXPECTED_TRANSITION_PAIRS7
    )
    denominators = [edge.weight.denominator for edge in graph.edges] + [
        terminal.weight.denominator for terminal in anchor_terminals()
    ]
    assert lcm(*denominators) == SCALE7
    weights = tuple(edge.weight * SCALE7 for edge in graph.edges)
    assert all(weight == int(weight) for weight in weights)
    weights = tuple(int(weight) for weight in weights)
    assert tuple(sorted(Counter(weights).items())) == EXPECTED_WEIGHT_CENSUS7
    assert {
        int(terminal.weight * SCALE7) for terminal in anchor_terminals()
    } == {EXPECTED_ANCHOR_SCALED7}

    solver = _solver()
    transports = []
    for edge in graph.edges:
        upper_cells = solver.model.cells_by_half[_expected_half(edge.upper)]
        lower_cells = solver.model.cells_by_half[_expected_half(edge.lower)]
        lower_id = {cell: index for index, cell in enumerate(lower_cells)}
        actions = (
            {
                cell: solver.reduced.block_action(
                    edge.lower_level, edge.letter, cell
                )
                for cell in upper_cells
            }
            if edge.phase
            else {}
        )
        forward = []
        for cell in upper_cells:
            for xi in range(5):
                if edge.phase:
                    action = actions[cell]
                    target_cell = action.target_cell
                    target_xi = action.apply_xi(xi)
                else:
                    target_cell = cell
                    target_xi = xi
                forward.append(5 * lower_id[target_cell] + target_xi)
        forward = tuple(forward)
        assert sorted(forward) == list(range(DOMAIN))
        transports.append(
            (node_id[edge.upper], node_id[edge.lower], forward, inverse(forward))
        )
    return graph, node_id, tuple(transports), weights


@lru_cache(maxsize=1)
def _retraction():
    graph, node_id, transports, weights = _graph_and_transports()
    adjacency = [[] for _ in graph.nodes]
    for edge_id, (upper, lower, forward, reverse) in enumerate(transports):
        adjacency[upper].append((lower, edge_id, forward))
        adjacency[lower].append((upper, edge_id, reverse))
    gauge: list[tuple[int, ...] | None] = [None] * NODE_COUNT7
    gauge[0] = IDENTITY
    queue = deque((0,))
    while queue:
        upper = queue.popleft()
        for lower, edge_id, transport in sorted(
            adjacency[upper], key=lambda item: (item[0], item[1])
        ):
            if gauge[lower] is None:
                gauge[lower] = compose(transport, gauge[upper])
                queue.append(lower)
    assert all(item is not None for item in gauge)
    gauges = tuple(gauge)  # type: ignore[arg-type]
    inverse_gauges = tuple(inverse(item) for item in gauges)

    holonomies = []
    for edge_id, (upper, lower, forward, _) in enumerate(transports):
        holonomy = compose(inverse_gauges[lower], compose(forward, gauges[upper]))
        if holonomy != IDENTITY:
            holonomies.append(holonomy)
    assert len(holonomies) == EXPECTED_NONIDENTITY_CHORDS7
    assert PAIR_COUNT7 - NODE_COUNT7 + 1 == EXPECTED_CYCLE_RANK7
    generators = tuple(holonomies) + tuple(inverse(item) for item in holonomies)

    unseen = set(range(DOMAIN))
    orbits = []
    while unseen:
        seed = min(unseen)
        orbit = {seed}
        queue = deque((seed,))
        while queue:
            state = queue.popleft()
            for generator in generators:
                target = generator[state]
                if target not in orbit:
                    orbit.add(target)
                    queue.append(target)
        unseen.difference_update(orbit)
        orbits.append(tuple(sorted(orbit)))
    assert Counter(map(len, orbits)) == Counter({5: 625})
    assert orbits[0] == (0, 1, 2, 3, 4)

    root_retraction = [-1] * DOMAIN
    choice_census = Counter()
    for orbit in orbits:
        source_seed = orbit[0]
        valid_maps = []
        for target_seed in orbits[0]:
            mapping = {source_seed: target_seed}
            queue = deque((source_seed,))
            valid = True
            while queue and valid:
                source = queue.popleft()
                target = mapping[source]
                for generator in generators:
                    new_source = generator[source]
                    new_target = generator[target]
                    old = mapping.get(new_source)
                    if old is None:
                        mapping[new_source] = new_target
                        queue.append(new_source)
                    elif old != new_target:
                        valid = False
                        break
            if valid:
                valid_maps.append((target_seed, mapping))
        choice_census[len(valid_maps)] += 1
        for source, target in valid_maps[0][1].items():
            root_retraction[source] = target
    assert choice_census == Counter({5: 625})
    root_retraction = tuple(root_retraction)
    assert root_retraction[:5] == (0, 1, 2, 3, 4)

    node_retractions = tuple(
        tuple(
            gauges[node][root_retraction[inverse_gauges[node][state]]]
            for state in range(DOMAIN)
        )
        for node in range(NODE_COUNT7)
    )
    for upper, lower, forward, _ in transports:
        assert all(
            node_retractions[lower][forward[state]]
            == forward[node_retractions[upper][state]]
            for state in range(DOMAIN)
        )
    return node_retractions


@lru_cache(maxsize=1)
def _pins():
    graph, node_id, transports, _ = _graph_and_transports()
    node_retractions = _retraction()
    rows = []
    for coordinate in range(5):
        row = []
        for terminal in anchor_terminals():
            label = _reverse_anchor(
                terminal,
                SPECIAL_BLOCK,
                _terminal_label(terminal.id, SPECIAL_BLOCK),
            )
            state = _encode_state(
                terminal.parent, label.cell, label.permutation[coordinate]
            )
            assert node_retractions[node_id[terminal.parent]][state] == state
            row.append(state)
        rows.append(tuple(row))
    result = tuple(rows)
    assert result == EXPECTED_PIN_GRID
    return result


def _minfill_order(count: int, pairs) -> tuple[int, ...]:
    neighbours = [set() for _ in range(count)]
    for left, right in pairs:
        neighbours[left].add(right)
        neighbours[right].add(left)
    order = []
    alive = set(range(count))
    while alive:
        best = None
        for vertex in alive:
            local = [item for item in neighbours[vertex] if item in alive]
            fill = sum(
                1
                for i in range(len(local))
                for j in range(i + 1, len(local))
                if local[j] not in neighbours[local[i]]
            )
            key = (fill, len(local), vertex)
            if best is None or key < best[0]:
                best = (key, vertex, local)
        _, vertex, local = best
        order.append(vertex)
        alive.remove(vertex)
        for i in range(len(local)):
            for j in range(i + 1, len(local)):
                neighbours[local[i]].add(local[j])
                neighbours[local[j]].add(local[i])
    return tuple(order)


def _solve_coordinate(order, coordinate):
    graph, node_id, transports, weights = _graph_and_transports()
    pins = _pins()
    factors = []
    for edge_id, (upper, lower, forward, _) in enumerate(transports):
        table = {
            (left, right): weights[edge_id] * (right != forward[left])
            for left in range(5)
            for right in range(5)
        }
        factors.append(((upper, lower), table))
    for terminal, target in zip(anchor_terminals(), pins[coordinate]):
        factors.append(
            (
                (node_id[terminal.parent],),
                {
                    (state,): EXPECTED_ANCHOR_SCALED7 * (state != target)
                    for state in range(5)
                },
            )
        )
    backtrack = []
    maximum_width = 0
    for eliminated in order:
        selected = [factor for factor in factors if eliminated in factor[0]]
        factors = [factor for factor in factors if eliminated not in factor[0]]
        scope = tuple(sorted(set().union(*(set(item[0]) for item in selected))))
        maximum_width = max(maximum_width, len(scope) - 1)
        remaining = tuple(node for node in scope if node != eliminated)
        new_table = {}
        argmin = {}
        for values in product(range(5), repeat=len(remaining)):
            fixed = dict(zip(remaining, values))
            best_cost = None
            best_value = None
            for value in range(5):
                assignment = fixed | {eliminated: value}
                cost = sum(
                    table[tuple(assignment[node] for node in factor_scope)]
                    for factor_scope, table in selected
                )
                if best_cost is None or cost < best_cost:
                    best_cost = cost
                    best_value = value
            new_table[values] = best_cost
            argmin[values] = best_value
        factors.append((remaining, new_table))
        backtrack.append((eliminated, remaining, argmin))
    assert maximum_width <= EXPECTED_SPECIAL_WIDTH7
    optimum = sum(table[()] for _, table in factors)
    assignment = {}
    for eliminated, remaining, argmin in reversed(backtrack):
        assignment[eliminated] = argmin[
            tuple(assignment[node] for node in remaining)
        ]
    return (
        optimum,
        tuple(assignment[node] for node in range(NODE_COUNT7)),
        maximum_width,
    )


def _reassembled_witness(offsets):
    graph, node_id, transports, weights = _graph_and_transports()
    solver = _solver()
    assignments = tuple(
        tuple((offsets[node] + coordinate) % 5 for node in range(NODE_COUNT7))
        for coordinate in range(5)
    )
    assert all(
        sorted(assignments[coordinate][node] for coordinate in range(5))
        == list(range(5))
        for node in range(NODE_COUNT7)
    )
    labels = tuple(
        BlockLabel(
            solver.model.cells_by_half[_expected_half(graph.nodes[node])][0],
            tuple(assignments[coordinate][node] for coordinate in range(5)),
        )
        for node in range(NODE_COUNT7)
    )
    cost = 0
    bad = []
    for edge in graph.edges:
        label = labels[node_id[edge.upper]]
        if edge.phase:
            label = _advance_label(
                SPECIAL_BLOCK, label, edge.lower_level, edge.letter
            )
        mismatch = _label_mismatches(label, labels[node_id[edge.lower]])
        cost += weights[edge.id] * mismatch
        if mismatch:
            assert mismatch == 5
            bad.append(edge.id)
    for terminal in anchor_terminals():
        target = _reverse_anchor(
            terminal,
            SPECIAL_BLOCK,
            _terminal_label(terminal.id, SPECIAL_BLOCK),
        )
        mismatch = _label_mismatches(labels[node_id[terminal.parent]], target)
        cost += EXPECTED_ANCHOR_SCALED7 * mismatch
        if mismatch:
            assert mismatch == 5
            bad.append(PAIR_COUNT7 + terminal.id)
    return cost, tuple(bad)


@lru_cache(maxsize=1)
def _compute_special_horizon7() -> SpecialHorizon7Report:
    graph, node_id, transports, weights = _graph_and_transports()
    _retraction()
    pins = _pins()
    order = _minfill_order(
        NODE_COUNT7, [(upper, lower) for upper, lower, _, _ in transports]
    )
    assert order == EXPECTED_MINFILL_ORDER7
    results = tuple(_solve_coordinate(order, coordinate) for coordinate in range(5))
    optima = tuple(item[0] for item in results)
    width = max(item[2] for item in results)
    if optima != EXPECTED_COORDINATE_OPTIMA7 or width != EXPECTED_SPECIAL_WIDTH7:
        raise AssertionError("special horizon-7 coordinate solve changed")
    coord0 = results[0][1]
    if (
        coord0 != EXPECTED_COORD0_ASSIGNMENT7
        or sha256(bytes(coord0)).hexdigest() != EXPECTED_COORD0_SHA256_7
    ):
        raise AssertionError("special horizon-7 coordinate-0 assignment changed")
    cost, bad = _reassembled_witness(coord0)
    if cost != EXPECTED_SPECIAL_TOTAL7 or bad != EXPECTED_REASSEMBLED_BAD7:
        raise AssertionError("special horizon-7 reassembly changed")
    structure = Horizon7StructureReport(
        node_census=EXPECTED_NODE_CENSUS7,
        transition_pairs=EXPECTED_TRANSITION_PAIRS7,
        weight_census=EXPECTED_WEIGHT_CENSUS7,
        anchor_scaled=EXPECTED_ANCHOR_SCALED7,
        scale=SCALE7,
        tm_complexity=thue_morse_complexity((3, 4, 5, 6, 7)),
        cycle_rank=EXPECTED_CYCLE_RANK7,
        nonidentity_chords=EXPECTED_NONIDENTITY_CHORDS7,
        orbit_count=625,
        orbit_size=5,
        commutation_checks=EXPECTED_COMMUTATION_CHECKS7,
        pins_equal_horizon5=pins == EXPECTED_PIN_GRID,
        pins_fixed=True,
    )
    if structure.tm_complexity != tuple(
        count for _, count in EXPECTED_NODE_CENSUS7
    ):
        raise AssertionError("Thue-Morse complexity crosscheck failed")
    if SPECIAL_MINIMA_SCALE48 != (120, 180, 220, cost):
        raise AssertionError("special minima ladder changed")
    return SpecialHorizon7Report(
        structure=structure,
        elimination_order=order,
        maximum_width=width,
        coordinate_optima=optima,
        scaled_lower_bound=sum(optima),
        reassembled_cost=cost,
        reassembled_bad=bad,
        coord0_assignment_sha256=sha256(bytes(coord0)).hexdigest(),
        closed=sum(optima) == cost,
        special_minima_scale48=SPECIAL_MINIMA_SCALE48,
        special_marginals_scale48=tuple(
            b - a
            for a, b in zip(SPECIAL_MINIMA_SCALE48, SPECIAL_MINIMA_SCALE48[1:])
        ),
    )


def build_special_horizon7() -> SpecialHorizon7Report:
    _require_assertion_gates()
    return _compute_special_horizon7()


def _verify_structure_types(structure: object) -> bool:
    if type(structure) is not Horizon7StructureReport:
        return False
    pair_tables = (
        structure.node_census,
        structure.transition_pairs,
        structure.weight_census,
    )
    return (
        all(
            type(table) is tuple
            and all(
                type(item) is tuple
                and len(item) == 2
                and all(type(value) is int for value in item)
                for item in table
            )
            for table in pair_tables
        )
        and type(structure.tm_complexity) is tuple
        and all(type(value) is int for value in structure.tm_complexity)
        and all(
            type(value) is int
            for value in (
                structure.anchor_scaled,
                structure.scale,
                structure.cycle_rank,
                structure.nonidentity_chords,
                structure.orbit_count,
                structure.orbit_size,
                structure.commutation_checks,
            )
        )
        and type(structure.pins_equal_horizon5) is bool
        and type(structure.pins_fixed) is bool
    )


def verify_special_horizon7(report: SpecialHorizon7Report) -> bool:
    return (
        __debug__
        and type(report) is SpecialHorizon7Report
        and _verify_structure_types(report.structure)
        and type(report.elimination_order) is tuple
        and all(type(value) is int for value in report.elimination_order)
        and type(report.maximum_width) is int
        and type(report.coordinate_optima) is tuple
        and all(type(value) is int for value in report.coordinate_optima)
        and type(report.scaled_lower_bound) is int
        and type(report.reassembled_cost) is int
        and type(report.reassembled_bad) is tuple
        and all(type(value) is int for value in report.reassembled_bad)
        and type(report.coord0_assignment_sha256) is str
        and type(report.closed) is bool
        and type(report.special_minima_scale48) is tuple
        and all(type(value) is int for value in report.special_minima_scale48)
        and type(report.special_marginals_scale48) is tuple
        and all(
            type(value) is int for value in report.special_marginals_scale48
        )
        and report == _compute_special_horizon7()
        and report.closed
        and report.scaled_lower_bound
        == report.reassembled_cost
        == EXPECTED_SPECIAL_TOTAL7
        and report.special_marginals_scale48 == SPECIAL_MARGINALS_SCALE48
    )


def format_prep_report(report: SpecialHorizon7Report) -> str:
    if not verify_special_horizon7(report):
        raise ValueError("cannot format an invalid horizon-7 prep report")
    return "\n".join(
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
            "  special minima ladder 120,180,220,260: marginals +60,+40,+40",
            "  ordinary block: vars=320 pairs=580 pins=60 -- OUTSIDE THIS"
            " PREP MODULE",
            "  RESULT special=260/150000-scale [NON-CANONICAL prep only]",
        )
    )


def main() -> int:
    print("ENTROPY-SELECTION HORIZON-7 PREP CHECK")
    print("NON-CANONICAL / NON-FORMAL / NO CLAIM STATUS")
    print(format_prep_report(build_special_horizon7()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
