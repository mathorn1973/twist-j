"""Preparation layer for the exact coupled horizon ``2..6``.

NON-CANONICAL LOCAL ANALYSIS, PREPARATION GRADE.  This module extends the
horizon-5 full-domain retraction machinery to the ``2..6`` later graph and
closes the SPECIAL block exactly.  It deliberately does NOT build the
ordinary-block DP, the coupled witness, or a coupled certificate: those are
outside this preparation module.  Nothing here earns claim status.

Certified here (assertion-gated, replayed by ``test_horizon6_prep.py``):

1.  Scale correction.  The ``5 -> 6`` transition carries exact edge weights
    ``1/48``, so the horizon-5 constant ``SCALE = 24`` silently truncates
    sixteen level-6 edges to weight zero under ``int(weight * 24)``.  The
    correct integral scale for ``2..6`` is ``48`` (the least common multiple
    of all weight denominators), with ``OBJECTIVE_SCALE = 48 * 3125``.
    Horizon-5 quantities double in these units (25020 -> 50040,
    43770 -> 87540).
2.  Graph census.  Nodes per level ``{3: 6, 4: 10, 5: 12, 6: 16}`` (the
    Thue--Morse factor complexity, cross-checked independently), 76 pair
    edges (20 + 24 + 32 per transition), the unchanged 12 level-3 anchors.
3.  Retraction extension.  The canonical tree gauge (43 tree edges, cycle
    rank 33, 25 nonidentity chord holonomies) again produces exactly 625
    orbits of size 5 with a five-fold canonical-map choice per orbit; the
    node retractions commute on all ``76 * 3125 = 237500`` edge-state pairs
    and fix all anchor pins.  The pin grid equals the horizon-5 grid (the
    anchors live at level 3 and do not move).
4.  Special block closed at ``220`` (scale 48).  Exact min-sum elimination
    with a deterministic min-fill order (maximum union scope 7, standard
    induced width 6) gives coordinate optima ``(44, 44, 44, 44, 44)``; the
    cyclic reassembly of the
    coordinate-0 assignment is a valid all-different label family of exact
    replayed cost ``220``.  Lower equals upper, so the special block is
    fathomed for ``2..6``.
5.  Marginal-uniformity refutation.  From ``2..4`` to ``2..5`` every block
    minimum rose by exactly ``+30`` (scale 24; ``+60`` in scale 48), special
    included.  The uniform continuation predicted special ``240`` at
    ``2..6``; the exact closure gives ``220`` (marginal ``+40`` in scale
    48).  The uniform-marginal hypothesis is therefore REFUTED before
    freezing, and no replacement prediction for the ordinary block is
    frozen here: the exact ordinary DP decides between the open candidate
    patterns (see ``PREP_HORIZON6.md``).

Outside this preparation module: the ordinary-block point bundle and exact
minimum for ``2..6`` (the horizon-5 analogue lives in
``horizon5_ordinary``), the structured coupled witness, the coupled
certificate, and any readback.  Their later closure does not retroactively
turn this special-block preparation report into a formal run.
Optimized Python (``-O``) is refused because the audit relies on assertion
gates.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from fractions import Fraction
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
    from path_bounds import (  # type: ignore[no-redef]
        _reverse_anchor,
        _terminal_label,
        anchor_terminals,
    )


DOMAIN = 3125
SCALE6 = 48
OBJECTIVE_SCALE6 = SCALE6 * DOMAIN
MINIMUM_LEVEL = 3
MAXIMUM_LEVEL = 6
NODE_COUNT6 = 44
PAIR_COUNT6 = 76
PIN_COUNT = 12
IDENTITY = tuple(range(DOMAIN))

EXPECTED_NODE_CENSUS = ((3, 6), (4, 10), (5, 12), (6, 16))
EXPECTED_TRANSITION_PAIRS = ((3, 20), (4, 24), (5, 32))
EXPECTED_WEIGHT_CENSUS6 = ((1, 16), (2, 56), (4, 4))
EXPECTED_ANCHOR_SCALED6 = 4
EXPECTED_SCALE24_TRUNCATED = 16
EXPECTED_SHIFT_CENSUS = ((0, 50), (1, 8), (3, 16), (4, 2))
EXPECTED_CYCLE_RANK = 33
EXPECTED_NONIDENTITY_CHORDS = 25
EXPECTED_COMMUTATION_CHECKS = PAIR_COUNT6 * DOMAIN

EXPECTED_MINFILL_ORDER = (
    28, 35, 29, 30, 39, 40, 31, 32, 41, 42, 33, 37, 34, 38, 36, 43,
    1, 16, 24, 2, 3, 4, 19, 27, 17, 20, 25, 18, 26, 21, 5, 12, 6,
    22, 23, 7, 0, 8, 9, 10, 11, 13, 14, 15,
)
EXPECTED_SPECIAL_WIDTH6 = 6
EXPECTED_SPECIAL_UNION_SCOPE6 = 7
EXPECTED_COORDINATE_OPTIMA6 = (44, 44, 44, 44, 44)
EXPECTED_SPECIAL_TOTAL6 = 220
EXPECTED_COORD0_ASSIGNMENT = (
    3, 4, 2, 0, 0, 1, 1, 1, 3, 1, 1, 3, 3, 1, 3, 4, 1, 1, 3, 3, 3,
    3, 1, 1, 0, 1, 3, 3, 1, 0, 0, 3, 3, 3, 1, 1, 3, 3, 1, 0, 0, 3,
    3, 3,
)
EXPECTED_COORD0_SHA256 = (
    "fb3879b15a806e8444292aa6480f89ed66925eadd7a538f3491da7634af47057"
)
EXPECTED_REASSEMBLED_BAD6 = (
    1, 3, 6, 8, 10, 12, 13, 15, 18, 19, 21, 36, 76, 79, 80, 81,
)

HORIZON5_SPECIAL_SCALE48 = 180          # 90 in scale 24
HORIZON5_ORDINARY_SCALE48 = 140         # 70 in scale 24
REFUTED_UNIFORM_SPECIAL_PREDICTION = 240  # 180 + 60; the exact value is 220
SPECIAL_MARGINAL_SCALE48 = EXPECTED_SPECIAL_TOTAL6 - HORIZON5_SPECIAL_SCALE48

ORDINARY_VARIABLES6 = 5 * NODE_COUNT6
ORDINARY_PAIRS6 = 5 * PAIR_COUNT6
ORDINARY_PINS6 = 5 * PIN_COUNT


@dataclass(frozen=True, slots=True)
class Horizon6StructureReport:
    node_census: tuple[tuple[int, int], ...]
    transition_pairs: tuple[tuple[int, int], ...]
    weight_census: tuple[tuple[int, int], ...]
    anchor_scaled: int
    scale: int
    scale24_truncated_edges: int
    tm_complexity: tuple[int, ...]
    cycle_rank: int
    nonidentity_chords: int
    shift_census: tuple[tuple[int, int], ...]
    orbit_count: int
    orbit_size: int
    commutation_checks: int
    pins_equal_horizon5: bool
    pins_fixed: bool


@dataclass(frozen=True, slots=True)
class SpecialHorizon6Report:
    structure: Horizon6StructureReport
    elimination_order: tuple[int, ...]
    maximum_width: int
    coordinate_optima: tuple[int, ...]
    scaled_lower_bound: int
    reassembled_cost: int
    reassembled_bad: tuple[int, ...]
    coord0_assignment_sha256: str
    closed: bool
    refuted_uniform_prediction: int
    special_marginal_scale48: int


def _require_assertion_gates() -> None:
    if not __debug__:
        raise RuntimeError("optimized Python disables required assertion gates")


def thue_morse_complexity(lengths: tuple[int, ...]) -> tuple[int, ...]:
    """Independent factor-complexity crosscheck for the collar node census."""

    word = [0]
    while len(word) < 4096 + max(lengths):
        word += [1 - bit for bit in word]
    return tuple(
        len({tuple(word[i : i + n]) for i in range(4096)}) for n in lengths
    )


@lru_cache(maxsize=1)
def _graph_and_transports():
    graph = constraint_graph(MINIMUM_LEVEL, MAXIMUM_LEVEL)
    node_id = {node: index for index, node in enumerate(graph.nodes)}
    assert len(graph.nodes) == NODE_COUNT6
    assert (
        tuple(sorted(Counter(level for level, _ in graph.nodes).items()))
        == EXPECTED_NODE_CENSUS
    )
    assert (
        tuple(
            sorted(
                Counter(edge.lower_level for edge in graph.edges).items()
            )
        )
        == EXPECTED_TRANSITION_PAIRS
    )
    denominators = [edge.weight.denominator for edge in graph.edges] + [
        terminal.weight.denominator for terminal in anchor_terminals()
    ]
    assert lcm(*denominators) == SCALE6
    weights = tuple(edge.weight * SCALE6 for edge in graph.edges)
    assert all(weight == int(weight) for weight in weights)
    weights = tuple(int(weight) for weight in weights)
    assert tuple(sorted(Counter(weights).items())) == EXPECTED_WEIGHT_CENSUS6
    assert sum(
        1 for edge in graph.edges if int(edge.weight * 24) == 0
    ) == EXPECTED_SCALE24_TRUNCATED
    assert {
        int(terminal.weight * SCALE6) for terminal in anchor_terminals()
    } == {EXPECTED_ANCHOR_SCALED6}

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
    shifts = tuple(item[2][0] for item in transports)
    assert all(
        tuple(transport[2][xi] for xi in range(5))
        == tuple((xi + shifts[index]) % 5 for xi in range(5))
        for index, transport in enumerate(transports)
    )
    assert tuple(sorted(Counter(shifts).items())) == EXPECTED_SHIFT_CENSUS
    return graph, node_id, tuple(transports), weights


@lru_cache(maxsize=1)
def _retraction():
    graph, node_id, transports, weights = _graph_and_transports()
    adjacency = [[] for _ in graph.nodes]
    for edge_id, (upper, lower, forward, reverse) in enumerate(transports):
        adjacency[upper].append((lower, edge_id, forward))
        adjacency[lower].append((upper, edge_id, reverse))
    gauge: list[tuple[int, ...] | None] = [None] * NODE_COUNT6
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
    assert len(holonomies) == EXPECTED_NONIDENTITY_CHORDS
    assert PAIR_COUNT6 - NODE_COUNT6 + 1 == EXPECTED_CYCLE_RANK
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
        for node in range(NODE_COUNT6)
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
                    (state,): EXPECTED_ANCHOR_SCALED6 * (state != target)
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
    assert maximum_width <= EXPECTED_SPECIAL_WIDTH6
    optimum = sum(table[()] for _, table in factors)
    assignment = {}
    for eliminated, remaining, argmin in reversed(backtrack):
        assignment[eliminated] = argmin[
            tuple(assignment[node] for node in remaining)
        ]
    return optimum, tuple(assignment[node] for node in range(NODE_COUNT6)), maximum_width


def _reassembled_witness(offsets):
    graph, node_id, transports, weights = _graph_and_transports()
    solver = _solver()
    assignments = tuple(
        tuple((offsets[node] + coordinate) % 5 for node in range(NODE_COUNT6))
        for coordinate in range(5)
    )
    assert all(
        sorted(assignments[coordinate][node] for coordinate in range(5))
        == list(range(5))
        for node in range(NODE_COUNT6)
    )
    labels = tuple(
        BlockLabel(
            solver.model.cells_by_half[_expected_half(graph.nodes[node])][0],
            tuple(assignments[coordinate][node] for coordinate in range(5)),
        )
        for node in range(NODE_COUNT6)
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
        cost += EXPECTED_ANCHOR_SCALED6 * mismatch
        if mismatch:
            assert mismatch == 5
            bad.append(PAIR_COUNT6 + terminal.id)
    return cost, tuple(bad)


@lru_cache(maxsize=1)
def _compute_special_horizon6() -> SpecialHorizon6Report:
    graph, node_id, transports, weights = _graph_and_transports()
    node_retractions = _retraction()
    pins = _pins()
    order = _minfill_order(
        NODE_COUNT6, [(upper, lower) for upper, lower, _, _ in transports]
    )
    assert order == EXPECTED_MINFILL_ORDER
    results = tuple(_solve_coordinate(order, coordinate) for coordinate in range(5))
    optima = tuple(item[0] for item in results)
    width = max(item[2] for item in results)
    if optima != EXPECTED_COORDINATE_OPTIMA6 or width != EXPECTED_SPECIAL_WIDTH6:
        raise AssertionError("special horizon-6 coordinate solve changed")
    coord0 = results[0][1]
    if (
        coord0 != EXPECTED_COORD0_ASSIGNMENT
        or sha256(bytes(coord0)).hexdigest() != EXPECTED_COORD0_SHA256
    ):
        raise AssertionError("special horizon-6 coordinate-0 assignment changed")
    cost, bad = _reassembled_witness(coord0)
    if cost != EXPECTED_SPECIAL_TOTAL6 or bad != EXPECTED_REASSEMBLED_BAD6:
        raise AssertionError("special horizon-6 reassembly changed")
    structure = Horizon6StructureReport(
        node_census=EXPECTED_NODE_CENSUS,
        transition_pairs=EXPECTED_TRANSITION_PAIRS,
        weight_census=EXPECTED_WEIGHT_CENSUS6,
        anchor_scaled=EXPECTED_ANCHOR_SCALED6,
        scale=SCALE6,
        scale24_truncated_edges=EXPECTED_SCALE24_TRUNCATED,
        tm_complexity=thue_morse_complexity((3, 4, 5, 6)),
        cycle_rank=EXPECTED_CYCLE_RANK,
        nonidentity_chords=EXPECTED_NONIDENTITY_CHORDS,
        shift_census=EXPECTED_SHIFT_CENSUS,
        orbit_count=625,
        orbit_size=5,
        commutation_checks=EXPECTED_COMMUTATION_CHECKS,
        pins_equal_horizon5=pins == EXPECTED_PIN_GRID,
        pins_fixed=True,
    )
    if structure.tm_complexity != tuple(count for _, count in EXPECTED_NODE_CENSUS):
        raise AssertionError("Thue-Morse complexity crosscheck failed")
    return SpecialHorizon6Report(
        structure=structure,
        elimination_order=order,
        maximum_width=width,
        coordinate_optima=optima,
        scaled_lower_bound=sum(optima),
        reassembled_cost=cost,
        reassembled_bad=bad,
        coord0_assignment_sha256=sha256(bytes(coord0)).hexdigest(),
        closed=sum(optima) == cost,
        refuted_uniform_prediction=REFUTED_UNIFORM_SPECIAL_PREDICTION,
        special_marginal_scale48=cost - HORIZON5_SPECIAL_SCALE48,
    )


def build_special_horizon6() -> SpecialHorizon6Report:
    _require_assertion_gates()
    return _compute_special_horizon6()


def _verify_structure_types(structure: Horizon6StructureReport) -> bool:
    pair_tables = (
        structure.node_census,
        structure.transition_pairs,
        structure.weight_census,
        structure.shift_census,
    )
    return (
        type(structure) is Horizon6StructureReport
        and all(
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
                structure.scale24_truncated_edges,
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


def verify_special_horizon6(report: SpecialHorizon6Report) -> bool:
    return (
        __debug__
        and type(report) is SpecialHorizon6Report
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
        and type(report.refuted_uniform_prediction) is int
        and type(report.special_marginal_scale48) is int
        and report == _compute_special_horizon6()
        and report.closed
        and report.scaled_lower_bound
        == report.reassembled_cost
        == EXPECTED_SPECIAL_TOTAL6
        != report.refuted_uniform_prediction
    )


def format_prep_report(report: SpecialHorizon6Report) -> str:
    if not verify_special_horizon6(report):
        raise ValueError("cannot format an invalid horizon-6 prep report")
    return "\n".join(
        (
            "HORIZON 2..6 PREPARATION (special block closed; ordinary open)",
            "  scope=fixed-r2 structured finite boundary; scale=48"
            " (int(w*24) would zero 16 level-6 edges)",
            "  graph: nodes={3:6,4:10,5:12,6:16} pairs=76 (20+24+32)"
            " anchors=12 cycle-rank=33",
            "  retraction: orbits=625x5 chords=25 checks=237500"
            " pins=horizon-5 grid, fixed",
            "  special DP: width=6 union-scope=7"
            " optima=(44,44,44,44,44) total=220",
            "  special reassembly: all-different OK cost=220 bad-edges=16",
            "  special CLOSED: lower=upper=220; marginal +40 (scale 48)",
            "  uniform-marginal prediction 240 REFUTED by exact closure",
            "  ordinary block: vars=220 pairs=380 pins=60 -- OUTSIDE THIS"
            " PREP MODULE",
            "  RESULT special=220/150000-scale [NON-CANONICAL prep only]",
        )
    )


def main() -> int:
    print("ENTROPY-SELECTION HORIZON-6 PREP CHECK")
    print("NON-CANONICAL / NON-FORMAL / NO CLAIM STATUS")
    print(format_prep_report(build_special_horizon6()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
