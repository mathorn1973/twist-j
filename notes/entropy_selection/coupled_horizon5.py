"""Exact coupled optimum for the fixed-``r=2`` horizon ``2..5``.

NON-CANONICAL LOCAL ANALYSIS.  The full 3125-state point domains of the 624
ordinary blocks and the residual special block retract equivariantly to their
five-state anchor fibres.  Exact min-sum elimination then proves scaled block
minima 70 and 90.  A structured family with unchanged cell assignments attains
all 625 minima simultaneously, so zero assignment prices close the coupled
root at ``43770 / (24*3125) = 1459/2500``.

The lower calculation deliberately relaxes the shared-cell and ``S_5``
conditions after splitting a block into point coordinates.  Retraction need
only preserve point equalities.  The matching upper witness is separately
required to reassemble and to satisfy every all-different condition.

This is only the named frozen level-2 boundary and finite horizon.  It gives no
inverse-limit, entropy, measure, selection, or Canon authority.
Optimized Python (``-O``) is refused because the independent special-block
audit retains explicit assertion gates inherited from its frozen checker.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass, replace
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from functools import lru_cache

try:
    from . import horizon5_ordinary as ordinary
    from .basins import family_signature
    from .bounds import (
        SPECIAL_BLOCK,
        BlockLabel,
        _advance_label,
        _expected_half,
        _label_mismatches,
        _solver,
        constraint_graph,
    )
    from .collars import collar_graph, refinement_incidence
    from .growing import (
        BoundaryFamily,
        FiniteHorizonOptimizer,
        StructuredMap,
        default_collar,
        source_blocks,
    )
    from .path_bounds import (
        _anchor_data,
        _forward_anchor,
        _reverse_anchor,
        _terminal_label,
        anchor_terminals,
    )
except ImportError:  # Direct execution from this directory.
    import horizon5_ordinary as ordinary  # type: ignore[no-redef]
    from basins import family_signature  # type: ignore[no-redef]
    from bounds import (  # type: ignore[no-redef]
        SPECIAL_BLOCK,
        BlockLabel,
        _advance_label,
        _expected_half,
        _label_mismatches,
        _solver,
        constraint_graph,
    )
    from collars import collar_graph, refinement_incidence  # type: ignore[no-redef]
    from growing import (  # type: ignore[no-redef]
        BoundaryFamily,
        FiniteHorizonOptimizer,
        StructuredMap,
        default_collar,
        source_blocks,
    )
    from path_bounds import (  # type: ignore[no-redef]
        _anchor_data,
        _forward_anchor,
        _reverse_anchor,
        _terminal_label,
        anchor_terminals,
    )


DOMAIN = 3125
SCALE = 24
FIBER_SIZE = 3125
BLOCK_COUNT = 625
ORDINARY_BLOCK_COUNT = 624
OBJECTIVE_SCALE = SCALE * FIBER_SIZE
IDENTITY = tuple(range(DOMAIN))
NODE_COUNT = 28
PAIR_COUNT = 44
PIN_COUNT = 12
EDGE_COUNT = PAIR_COUNT + PIN_COUNT


@dataclass(frozen=True, slots=True)
class RetractionReport:
    variable_count: int
    pair_count: int
    pin_count: int
    cycle_rank: int
    holonomy_classes: int
    orbit_count: int
    orbit_size: int
    failed_orbit_maps: int
    commutation_checks: int
    fixed_pin_checks: int


@dataclass(frozen=True, slots=True)
class OrdinaryMinimumReport:
    retraction: RetractionReport
    condition_variables: tuple[int, int]
    elimination_order: tuple[int, ...]
    condition_minima: tuple[int, ...]
    maximum_width: int
    peak_union_entries: int
    peak_message_entries: int
    union_entries_per_case: int
    optimum: int
    assignment: tuple[int, ...]
    violated_records: tuple[int, ...]
    assignment_sha256: str


@dataclass(frozen=True, slots=True)
class SpecialMinimumReport:
    retraction: RetractionReport
    elimination_order: tuple[int, ...]
    coordinate_optima: tuple[int, ...]
    maximum_width: int
    table_census: tuple[tuple[int, int], ...]
    total_optimum: int
    assignments: tuple[tuple[int, ...], ...]


@dataclass(frozen=True, slots=True)
class CoupledHorizon5Witness:
    families: tuple[BoundaryFamily, ...]
    family_signatures: tuple[str, ...]
    combined_signature_sha256: str
    per_block_scaled_costs: tuple[int, ...]
    transition_distances: tuple[Fraction, ...]
    objective: Fraction
    cell_changes: int
    ordinary_permutation_changes: int
    special_permutation_changes: int
    stability_changes: int


@dataclass(frozen=True, slots=True)
class ExactCoupledHorizon5Certificate:
    minimum_level: int
    maximum_level: int
    seed: str
    lift_phase: int
    ordinary: OrdinaryMinimumReport
    special: SpecialMinimumReport
    block_minima: tuple[int, ...]
    assignment_price: Fraction
    assignment_minima: tuple[int, ...]
    scaled_lower_bound: int
    witness: CoupledHorizon5Witness
    scaled_upper_bound: int
    optimum: Fraction
    root_nodes: int
    branched_nodes: int
    fathomed_by_bound: int

EXPECTED_NODES = (
    (3, (0, 0, 1)),
    (3, (0, 1, 0)),
    (3, (0, 1, 1)),
    (3, (1, 0, 0)),
    (3, (1, 0, 1)),
    (3, (1, 1, 0)),
    (4, (0, 0, 1, 0)),
    (4, (0, 0, 1, 1)),
    (4, (0, 1, 0, 0)),
    (4, (0, 1, 0, 1)),
    (4, (0, 1, 1, 0)),
    (4, (1, 0, 0, 1)),
    (4, (1, 0, 1, 0)),
    (4, (1, 0, 1, 1)),
    (4, (1, 1, 0, 0)),
    (4, (1, 1, 0, 1)),
    (5, (0, 0, 1, 0, 1)),
    (5, (0, 0, 1, 1, 0)),
    (5, (0, 1, 0, 0, 1)),
    (5, (0, 1, 0, 1, 1)),
    (5, (0, 1, 1, 0, 0)),
    (5, (0, 1, 1, 0, 1)),
    (5, (1, 0, 0, 1, 0)),
    (5, (1, 0, 0, 1, 1)),
    (5, (1, 0, 1, 0, 0)),
    (5, (1, 0, 1, 1, 0)),
    (5, (1, 1, 0, 0, 1)),
    (5, (1, 1, 0, 1, 0)),
)

EXPECTED_EDGE_SHIFTS = (
    0, 1, 0, 1, 0, 1, 0, 1, 0, 4, 0, 4, 0, 1, 0, 1, 0, 1, 0, 1,
    0, 3, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3,
    0, 3, 0, 3,
)
EXPECTED_EDGE_WEIGHTS = (
    1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1,
)
EXPECTED_PIN_GRID = (
    (4, 3, 4, 3, 4, 3, 0, 0, 0, 0, 1, 1),
    (0, 4, 0, 4, 0, 4, 1, 1, 1, 1, 2, 2),
    (1, 0, 1, 0, 1, 0, 2, 2, 2, 2, 3, 3),
    (2, 1, 2, 1, 2, 1, 3, 3, 3, 3, 4, 4),
    (3, 2, 3, 2, 3, 2, 4, 4, 4, 4, 0, 0),
)
EXPECTED_GAUGED_PIN_GRID = (
    (4, 3, 3, 2, 3, 2, 0, 0, 3, 3, 1, 1),
    (0, 4, 4, 3, 4, 3, 1, 1, 4, 4, 2, 2),
    (1, 0, 0, 4, 0, 4, 2, 2, 0, 0, 3, 3),
    (2, 1, 1, 0, 1, 0, 3, 3, 1, 1, 4, 4),
    (3, 2, 2, 1, 2, 1, 4, 4, 2, 2, 0, 0),
)
EXPECTED_TREE_EDGES = (
    5, 7, 9, 10, 12, 1, 2, 4, 6, 8, 11, 28, 33, 16, 18, 21, 23,
    24, 26, 29, 31, 32, 34, 37, 39, 40, 42,
)
EXPECTED_NONIDENTITY_EDGES = (0, 3, 13, 15, 20, 22, 25, 36, 38, 41)
ELIMINATION_ORDER = (
    16, 24, 17, 25, 18, 26, 19, 27, 20, 21, 22, 23,
    1, 14, 4, 7, 6, 8, 13, 2, 0, 5, 3, 9, 10, 11, 12, 15,
)
EXPECTED_TABLE_CENSUS = Counter({25: 13, 125: 9, 625: 4, 5: 1, 1: 1})

EXPECTED_DP_ASSIGNMENTS = (
    (3, 4, 4, 0, 0, 1, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0),
    (0, 0, 0, 1, 1, 2, 4, 4, 0, 0, 2, 1, 0, 0, 0, 0, 2, 2, 1, 1, 0, 0, 0, 0, 2, 2, 1, 1),
    (0, 1, 1, 1, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2),
    (1, 2, 2, 2, 3, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3),
    (2, 3, 3, 3, 4, 0, 2, 2, 2, 2, 4, 4, 2, 2, 2, 2, 4, 4, 4, 4, 2, 2, 2, 2, 4, 4, 4, 4),
)
EXPECTED_DP_BAD = (
    (0, 1, 2, 3, 8, 9, 12, 13, 14, 15, 44, 47, 49),
    (0, 1, 2, 3, 5, 7, 8, 12, 14, 17, 19, 45, 47, 49),
    (3, 8, 15, 44, 47, 49, 50, 51, 54, 55),
    (3, 8, 15, 44, 47, 49, 50, 51, 54, 55),
    (0, 2, 3, 8, 12, 14, 15, 44, 47, 49, 50, 51),
)
REASSEMBLY_OFFSETS = EXPECTED_DP_ASSIGNMENTS[0]
EXPECTED_REASSEMBLED_BAD = (0, 1, 2, 3, 8, 9, 12, 13, 14, 15, 44, 47, 49)

ORDINARY_CONDITION_VARIABLES = (50, 4)
EXPECTED_ORDINARY_CONDITION_MINIMA = (
    71, 72, 75, 75, 75,
    73, 70, 75, 75, 75,
    75, 74, 75, 77, 77,
    75, 74, 77, 75, 77,
    73, 72, 75, 75, 73,
)
EXPECTED_ORDINARY_ORDER_SHA256 = (
    "ec22792c8c4623a5e39f03fd49332e1d013eda763360050b99273b80f333f249"
)
EXPECTED_ORDINARY_ASSIGNMENT = (
    3, 0, 0, 1, 1, 1, 1, 3, 0, 4, 2, 1, 3, 0, 0, 1, 0, 2, 2, 4,
    3, 0, 0, 2, 4, 1, 1, 3, 2, 4, 0, 0, 2, 1, 3, 0, 0, 2, 1, 3,
    3, 0, 0, 1, 1, 3, 0, 0, 2, 1, 1, 3, 0, 2, 1, 3, 0, 0, 2, 1,
    1, 3, 0, 4, 1, 0, 0, 2, 1, 3, 3, 0, 2, 1, 1, 3, 0, 2, 2, 1,
    1, 3, 0, 2, 1, 1, 3, 0, 2, 1, 3, 0, 0, 2, 1, 3, 0, 0, 2, 1,
    1, 3, 0, 4, 1, 1, 3, 0, 4, 1, 3, 0, 0, 2, 1, 3, 0, 0, 2, 1,
    1, 3, 0, 2, 1, 1, 3, 0, 2, 1, 3, 0, 0, 2, 1, 3, 0, 0, 2, 1,
)
EXPECTED_ORDINARY_ASSIGNMENT_SHA256 = (
    "fe694ad9efe0c035f380ad830c6250915727654444507656405020b48c461e75"
)
ORDINARY_BAD_BASE_EDGES = (0, 1, 2, 3, 8, 9, 12, 13, 14, 15)
EXPECTED_ORDINARY_VIOLATED_RECORDS = tuple(
    5 * edge + position
    for edge in ORDINARY_BAD_BASE_EDGES
    for position in range(5)
) + tuple(220 + position for position in range(5))

ORDINARY_PATCH_WORDS = ((0, 0, 1, 0), (0, 0, 1, 1), (1, 0, 1, 1))
ORDINARY_PATCH_PERMUTATION = (4, 0, 1, 2, 3)
BASELINE_FAMILY_SIGNATURES = (
    "c06fda5221cdcdd7859e9e3fc3ae648790b7c44d4adf18af5eaabd919b4eda02",
    "87267a244739791e9dc6ba6b5d5e4c09dda4d7964f4ee0a60e195025f3c66425",
    "32eb822dcb2377691e3947fab8ecccc645698d9af38b49011a77092b11dbc648",
    "4d492e391b3771ffbf7b62c3ace92a1a28490dd25df9278ad0778a499bf64338",
)
COUPLED_FAMILY_SIGNATURES = (
    "c06fda5221cdcdd7859e9e3fc3ae648790b7c44d4adf18af5eaabd919b4eda02",
    "96d4d0172d9205324cc8cbb02ec1636a5dbf71689fbdc46be9a9c9cee6c37209",
    "28e0c77e0efac9f3039c86ce5d52650dfd30cf407ef0d2e3355ab239a75c9121",
    "1b8a6737319f2ec94285c07e2e614f9943818a491763f7f73606fd5b4a082b37",
)
EXPECTED_COMBINED_SIGNATURE_SHA256 = (
    "964052c773890dbf45955b4d364805af3714e836ebf53c3cd36e20aefe358086"
)


def _require_assertion_gates() -> None:
    if not __debug__:
        raise RuntimeError("optimized Python disables required assertion gates")


def _encode_state(node, cell: int, xi: int) -> int:
    if type(xi) is not int or not 0 <= xi < 5:
        raise ValueError("point coordinate must lie in F_5")
    cells = _solver().model.cells_by_half[_expected_half(node)]
    try:
        local_cell = cells.index(cell)
    except ValueError as exc:
        raise ValueError("point cell lies in the wrong living half") from exc
    return 5 * local_cell + xi


def inverse(permutation: tuple[int, ...]) -> tuple[int, ...]:
    result = [-1] * len(permutation)
    for source, target in enumerate(permutation):
        result[target] = source
    return tuple(result)


def compose(after: tuple[int, ...], before: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(after[before[state]] for state in range(DOMAIN))


def _build_special_transports():
    graph = constraint_graph(3, 5)
    assert graph.nodes == EXPECTED_NODES
    solver = _solver()
    node_id = {node: index for index, node in enumerate(graph.nodes)}
    transports = []
    for edge in graph.edges:
        upper_cells = solver.model.cells_by_half[_expected_half(edge.upper)]
        lower_cells = solver.model.cells_by_half[_expected_half(edge.lower)]
        lower_id = {cell: index for index, cell in enumerate(lower_cells)}
        actions = (
            {
                cell: solver.reduced.block_action(edge.lower_level, edge.letter, cell)
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
    assert shifts == EXPECTED_EDGE_SHIFTS
    assert all(
        tuple(transport[2][xi] for xi in range(5))
        == tuple((xi + shifts[index]) % 5 for xi in range(5))
        for index, transport in enumerate(transports)
    )
    weights = tuple(int(edge.weight * SCALE) for edge in graph.edges)
    assert weights == EXPECTED_EDGE_WEIGHTS
    return graph, node_id, tuple(transports), weights


def _special_pin_data(graph, node_id):
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
            assert 0 <= state < 5
            row.append(state)
        rows.append(tuple(row))
    result = tuple(rows)
    assert result == EXPECTED_PIN_GRID
    assert all(int(terminal.weight * SCALE) == 2 for terminal in anchor_terminals())
    return result


def _build_special_retraction(graph, node_id, transports, pins):
    adjacency = [[] for _ in graph.nodes]
    for edge_id, (upper, lower, forward, reverse) in enumerate(transports):
        adjacency[upper].append((lower, edge_id, forward))
        adjacency[lower].append((upper, edge_id, reverse))
    gauge: list[tuple[int, ...] | None] = [None] * NODE_COUNT
    gauge[0] = IDENTITY
    parent_edge: list[int | None] = [None] * NODE_COUNT
    queue = deque((0,))
    while queue:
        upper = queue.popleft()
        assert gauge[upper] is not None
        for lower, edge_id, transport in sorted(
            adjacency[upper], key=lambda item: (item[0], item[1])
        ):
            if gauge[lower] is None:
                gauge[lower] = compose(transport, gauge[upper])
                parent_edge[lower] = edge_id
                queue.append(lower)
    assert all(item is not None for item in gauge)
    gauges = tuple(gauge)  # type: ignore[arg-type]
    assert tuple(parent_edge[1:]) == EXPECTED_TREE_EDGES
    inverse_gauges = tuple(inverse(item) for item in gauges)

    holonomies = []
    holonomy_edges = []
    for edge_id, (upper, lower, forward, _) in enumerate(transports):
        holonomy = compose(
            inverse_gauges[lower], compose(forward, gauges[upper])
        )
        if holonomy != IDENTITY:
            holonomy_edges.append(edge_id)
            holonomies.append(holonomy)
    assert tuple(holonomy_edges) == EXPECTED_NONIDENTITY_EDGES
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
    valid_choice_census = Counter()
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
        valid_choice_census[len(valid_maps)] += 1
        assert tuple(item[0] for item in valid_maps) == orbits[0]
        chosen = valid_maps[0][1]  # Canonical source minimum -> target zero.
        for source, target in chosen.items():
            root_retraction[source] = target
    assert valid_choice_census == Counter({5: 625})
    assert all(state >= 0 for state in root_retraction)
    root_retraction = tuple(root_retraction)
    assert root_retraction[:5] == (0, 1, 2, 3, 4)

    node_retractions = tuple(
        tuple(
            gauges[node][root_retraction[inverse_gauges[node][state]]]
            for state in range(DOMAIN)
        )
        for node in range(NODE_COUNT)
    )
    assert all(set(row) == set(range(5)) for row in node_retractions)
    for upper, lower, forward, _ in transports:
        assert all(
            node_retractions[lower][forward[state]]
            == forward[node_retractions[upper][state]]
            for state in range(DOMAIN)
        )
    gauged_pin_grid = []
    terminals = anchor_terminals()
    for coordinate, row in enumerate(pins):
        gauged_row = []
        for terminal, state in zip(terminals, row):
            node = node_id[terminal.parent]
            gauged_row.append(inverse_gauges[node][state])
            assert node_retractions[node][state] == state
        gauged_pin_grid.append(tuple(gauged_row))
    assert tuple(gauged_pin_grid) == EXPECTED_GAUGED_PIN_GRID
    report = RetractionReport(
        variable_count=NODE_COUNT,
        pair_count=PAIR_COUNT,
        pin_count=5 * PIN_COUNT,
        cycle_rank=PAIR_COUNT - NODE_COUNT + 1,
        holonomy_classes=len(set(holonomies) | {IDENTITY}),
        orbit_count=len(orbits),
        orbit_size=5,
        failed_orbit_maps=0,
        commutation_checks=PAIR_COUNT * DOMAIN,
        fixed_pin_checks=5 * PIN_COUNT,
    )
    return node_retractions, report


def _solve_special_coordinate(graph, node_id, transports, weights, pins, coordinate):
    factors = []
    for edge_id, (upper, lower, forward, _) in enumerate(transports):
        table = {
            (left, right): weights[edge_id] * (right != forward[left])
            for left in range(5)
            for right in range(5)
        }
        factors.append(((upper, lower), table))
    for terminal, target in zip(anchor_terminals(), pins[coordinate]):
        node = node_id[terminal.parent]
        factors.append(
            ((node,), {(state,): 2 * (state != target) for state in range(5)})
        )

    backtrack = []
    table_census = Counter()
    maximum_scope = 0
    for eliminated in ELIMINATION_ORDER:
        selected = [factor for factor in factors if eliminated in factor[0]]
        factors = [factor for factor in factors if eliminated not in factor[0]]
        scope = tuple(sorted(set().union(*(set(item[0]) for item in selected))))
        maximum_scope = max(maximum_scope, len(scope))
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
        table_census[len(new_table)] += 1
        factors.append((remaining, new_table))
        backtrack.append((eliminated, remaining, argmin))
    assert maximum_scope == 5
    assert table_census == EXPECTED_TABLE_CENSUS
    assert all(not scope for scope, _ in factors)
    optimum = sum(table[()] for _, table in factors)
    assignment = {}
    for eliminated, remaining, argmin in reversed(backtrack):
        assignment[eliminated] = argmin[
            tuple(assignment[node] for node in remaining)
        ]
    assignment_tuple = tuple(assignment[node] for node in range(NODE_COUNT))

    bad = []
    for edge_id, (upper, lower, forward, _) in enumerate(transports):
        if assignment_tuple[lower] != forward[assignment_tuple[upper]]:
            bad.append(edge_id)
    for terminal, target in zip(anchor_terminals(), pins[coordinate]):
        if assignment_tuple[node_id[terminal.parent]] != target:
            bad.append(PAIR_COUNT + terminal.id)
    assert optimum == 18
    assert assignment_tuple == EXPECTED_DP_ASSIGNMENTS[coordinate]
    assert tuple(bad) == EXPECTED_DP_BAD[coordinate]
    return optimum, assignment_tuple, tuple(bad)


def _verify_special_reassembled_witness(graph, node_id, weights, pins):
    assignments = tuple(
        tuple((offset + coordinate) % 5 for offset in REASSEMBLY_OFFSETS)
        for coordinate in range(5)
    )
    assert all(
        sorted(assignments[coordinate][node] for coordinate in range(5))
        == list(range(5))
        for node in range(NODE_COUNT)
    )
    labels = tuple(
        BlockLabel(
            _solver().model.cells_by_half[_expected_half(graph.nodes[node])][0],
            tuple(assignments[coordinate][node] for coordinate in range(5)),
        )
        for node in range(NODE_COUNT)
    )
    bad = []
    mismatch_sum = 0
    for edge in graph.edges:
        label = labels[node_id[edge.upper]]
        if edge.phase:
            label = _advance_label(
                SPECIAL_BLOCK, label, edge.lower_level, edge.letter
            )
        mismatch = _label_mismatches(label, labels[node_id[edge.lower]])
        mismatch_sum += weights[edge.id] * mismatch
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
        mismatch_sum += 2 * mismatch
        if mismatch:
            assert mismatch == 5
            bad.append(PAIR_COUNT + terminal.id)
    assert tuple(bad) == EXPECTED_REASSEMBLED_BAD
    assert mismatch_sum == 90
    payload = {
        "offsets": REASSEMBLY_OFFSETS,
        "bad": bad,
        "cost": mismatch_sum,
        "labels": [(item.cell, item.permutation) for item in labels],
    }
    digest = sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return labels, tuple(bad), mismatch_sum, digest


@lru_cache(maxsize=1)
def _compute_special_minimum() -> SpecialMinimumReport:
    graph, node_id, transports, weights = _build_special_transports()
    pins = _special_pin_data(graph, node_id)
    _, retraction = _build_special_retraction(
        graph, node_id, transports, pins
    )
    results = tuple(
        _solve_special_coordinate(
            graph, node_id, transports, weights, pins, coordinate
        )
        for coordinate in range(5)
    )
    _, bad, cost, digest = _verify_special_reassembled_witness(
        graph, node_id, weights, pins
    )
    if (
        tuple(item[0] for item in results) != (18,) * 5
        or cost != 90
        or bad != EXPECTED_REASSEMBLED_BAD
        or digest
        != "8bdc17135dfe9a116bb416d21e50b3935230662435d0f066a82d9785a105c7c2"
    ):
        raise AssertionError("special horizon-5 minimum changed")
    return SpecialMinimumReport(
        retraction=retraction,
        elimination_order=ELIMINATION_ORDER,
        coordinate_optima=tuple(item[0] for item in results),
        maximum_width=4,
        table_census=tuple(sorted(EXPECTED_TABLE_CENSUS.items())),
        total_optimum=sum(item[0] for item in results),
        assignments=tuple(item[1] for item in results),
    )


def build_special_minimum() -> SpecialMinimumReport:
    _require_assertion_gates()
    return _compute_special_minimum()


def _verify_retraction_types(report: RetractionReport) -> bool:
    return type(report) is RetractionReport and all(
        type(value) is int
        for value in (
            report.variable_count,
            report.pair_count,
            report.pin_count,
            report.cycle_rank,
            report.holonomy_classes,
            report.orbit_count,
            report.orbit_size,
            report.failed_orbit_maps,
            report.commutation_checks,
            report.fixed_pin_checks,
        )
    )


def verify_special_minimum(report: SpecialMinimumReport) -> bool:
    return (
        __debug__
        and type(report) is SpecialMinimumReport
        and _verify_retraction_types(report.retraction)
        and type(report.elimination_order) is tuple
        and all(type(value) is int for value in report.elimination_order)
        and type(report.coordinate_optima) is tuple
        and all(type(value) is int for value in report.coordinate_optima)
        and type(report.maximum_width) is int
        and type(report.table_census) is tuple
        and all(
            type(item) is tuple
            and len(item) == 2
            and all(type(value) is int for value in item)
            for item in report.table_census
        )
        and type(report.total_optimum) is int
        and type(report.assignments) is tuple
        and all(
            type(assignment) is tuple
            and all(type(value) is int for value in assignment)
            for assignment in report.assignments
        )
        and report == _compute_special_minimum()
    )


@lru_cache(maxsize=1)
def _compute_ordinary_minimum() -> OrdinaryMinimumReport:
    graph, node_id, edges = ordinary.build_point_bundle()
    transports, inverses, tree_edges = ordinary.canonical_gauge(edges)
    chord_count, shifts = ordinary.verify_holonomy_and_retraction(
        edges, transports, inverses, tree_edges
    )
    fibers, pin_pattern = ordinary.ordinary_pin_data(
        graph, node_id, transports, inverses
    )
    factors, records = ordinary.build_reduced_factors(
        edges, transports, inverses, pin_pattern
    )
    order, degrees, union_entries = ordinary.elimination_order(factors, graph)

    grid = []
    peak_message = 0
    for first in range(5):
        for second in range(5):
            optimum, _, peak = ordinary.solve_conditioned(
                factors,
                order,
                {
                    ordinary.CONDITION_VARS[0]: first,
                    ordinary.CONDITION_VARS[1]: second,
                },
            )
            grid.append(optimum)
            peak_message = max(peak_message, peak)
    if tuple(grid) != EXPECTED_ORDINARY_CONDITION_MINIMA:
        raise AssertionError("ordinary horizon-5 condition grid changed")
    if min(grid) != 70 or grid.index(70) != 6:
        raise AssertionError("ordinary horizon-5 optimum changed")

    fixed = {
        ordinary.CONDITION_VARS[0]: 1,
        ordinary.CONDITION_VARS[1]: 1,
    }
    optimum, history, traced_peak = ordinary.solve_conditioned(
        factors, order, fixed, trace=True
    )
    assignment = ordinary.reconstruct_assignment(history, fixed)
    violations, _, witness_cost = ordinary.replay_witness(assignment, records)
    ordinary.verify_lifted_reassembly(
        graph, transports, fibers, assignment
    )
    if (
        chord_count != 81
        or shifts != tuple(range(5))
        or len(fibers) != ORDINARY_BLOCK_COUNT
        or optimum != 70
        or witness_cost != 70
        or assignment != EXPECTED_ORDINARY_ASSIGNMENT
        or violations != EXPECTED_ORDINARY_VIOLATED_RECORDS
        or sha256(bytes(order)).hexdigest()
        != EXPECTED_ORDINARY_ORDER_SHA256
        or sha256(bytes(assignment)).hexdigest()
        != EXPECTED_ORDINARY_ASSIGNMENT_SHA256
        or max(degrees) != 8
        or peak_message != 5**8
        or traced_peak != 5**8
        or union_entries != 4_444_930
    ):
        raise AssertionError("ordinary horizon-5 replay changed")
    return OrdinaryMinimumReport(
        retraction=RetractionReport(
            variable_count=140,
            pair_count=220,
            pin_count=60,
            cycle_rank=chord_count,
            holonomy_classes=len(shifts),
            orbit_count=625,
            orbit_size=5,
            failed_orbit_maps=0,
            commutation_checks=220 * DOMAIN,
            fixed_pin_checks=60,
        ),
        condition_variables=ORDINARY_CONDITION_VARIABLES,
        elimination_order=order,
        condition_minima=tuple(grid),
        maximum_width=max(degrees),
        peak_union_entries=5**9,
        peak_message_entries=peak_message,
        union_entries_per_case=union_entries,
        optimum=optimum,
        assignment=assignment,
        violated_records=violations,
        assignment_sha256=sha256(bytes(assignment)).hexdigest(),
    )


def build_ordinary_minimum() -> OrdinaryMinimumReport:
    _require_assertion_gates()
    return _compute_ordinary_minimum()


def verify_ordinary_minimum(report: OrdinaryMinimumReport) -> bool:
    return (
        __debug__
        and type(report) is OrdinaryMinimumReport
        and _verify_retraction_types(report.retraction)
        and type(report.condition_variables) is tuple
        and all(type(value) is int for value in report.condition_variables)
        and type(report.elimination_order) is tuple
        and all(type(value) is int for value in report.elimination_order)
        and type(report.condition_minima) is tuple
        and all(type(value) is int for value in report.condition_minima)
        and all(
            type(value) is int
            for value in (
                report.maximum_width,
                report.peak_union_entries,
                report.peak_message_entries,
                report.union_entries_per_case,
                report.optimum,
            )
        )
        and type(report.assignment) is tuple
        and all(type(value) is int for value in report.assignment)
        and type(report.violated_records) is tuple
        and all(type(value) is int for value in report.violated_records)
        and type(report.assignment_sha256) is str
        and report == _compute_ordinary_minimum()
    )


@lru_cache(maxsize=1)
def _baseline_families() -> tuple[BoundaryFamily, ...]:
    optimizer = FiniteHorizonOptimizer(
        2,
        5,
        solver=_solver(),
        seed="tree",
        lift_phase=1,
        freeze_minimum=True,
    )
    report = optimizer.optimize(20)
    if report.final_objective != Fraction(10631, 15000):
        raise AssertionError("deterministic 2..5 baseline changed")
    families = tuple(optimizer.family(level) for level in range(2, 6))
    if tuple(family_signature(family) for family in families) != (
        BASELINE_FAMILY_SIGNATURES
    ):
        raise AssertionError("deterministic 2..5 signatures changed")
    return families


@lru_cache(maxsize=1)
def _patched_families() -> tuple[BoundaryFamily, ...]:
    graph = constraint_graph(3, 5)
    offsets = dict(zip(graph.nodes, REASSEMBLY_OFFSETS, strict=True))
    families: list[BoundaryFamily] = []
    for family in _baseline_families():
        maps = []
        for word, mapping in zip(
            collar_graph(family.spec).vertices, family.maps, strict=True
        ):
            permutations = list(mapping.permutations)
            if family.level == 4 and word in ORDINARY_PATCH_WORDS:
                if set(permutations[:SPECIAL_BLOCK]) != {(1, 2, 3, 4, 0)}:
                    raise AssertionError("ordinary horizon-5 patch base changed")
                permutations[:SPECIAL_BLOCK] = [
                    ORDINARY_PATCH_PERMUTATION
                ] * SPECIAL_BLOCK
            if family.level >= 3:
                offset = offsets[(family.level, word)]
                permutations[SPECIAL_BLOCK] = tuple(
                    (offset + coordinate) % 5 for coordinate in range(5)
                )
            maps.append(
                StructuredMap(mapping.half, mapping.cells, tuple(permutations))
            )
        families.append(replace(family, maps=tuple(maps)))

    # The ordinary L5 labels are the exact child-zero lift of the patched L4
    # labels.  Direct edge replay below checks the paired child-one equations.
    level4 = families[2]
    level5 = families[3]
    level4_maps = dict(
        zip(collar_graph(level4.spec).vertices, level4.maps, strict=True)
    )
    incidence = refinement_incidence(default_collar(5), default_collar(4))
    maps = []
    for atom, mapping in zip(incidence.atoms, level5.maps, strict=True):
        child = level4_maps[atom.child0]
        if mapping.cells[:SPECIAL_BLOCK] != child.cells[:SPECIAL_BLOCK]:
            raise AssertionError("ordinary child-zero cell lift changed")
        permutations = list(mapping.permutations)
        permutations[:SPECIAL_BLOCK] = child.permutations[:SPECIAL_BLOCK]
        maps.append(StructuredMap(mapping.half, mapping.cells, tuple(permutations)))
    families[3] = replace(level5, maps=tuple(maps))
    result = tuple(families)
    if tuple(family_signature(family) for family in result) != (
        COUPLED_FAMILY_SIGNATURES
    ):
        raise AssertionError("coupled horizon-5 signatures changed")
    return result


def _maps_by_node(
    families: tuple[BoundaryFamily, ...],
) -> dict[tuple[int, tuple[int, ...]], StructuredMap]:
    return {
        (family.level, word): mapping
        for family in families[1:]
        for word, mapping in zip(
            collar_graph(family.spec).vertices, family.maps, strict=True
        )
    }


def _scaled_edge_weights() -> tuple[int, ...]:
    graph = constraint_graph(3, 5)
    result = tuple(int(edge.weight * SCALE) for edge in graph.edges) + tuple(
        int(terminal.weight * SCALE) for terminal in anchor_terminals()
    )
    if Counter(result) != Counter({1: 40, 2: 16}):
        raise AssertionError("horizon-5 scaled edge census changed")
    return result


def _edge_mismatch_from_maps(
    maps: dict[tuple[int, tuple[int, ...]], StructuredMap],
    block_id: int,
    edge_id: int,
) -> int:
    graph = constraint_graph(3, 5)
    if edge_id < PAIR_COUNT:
        edge = graph.edges[edge_id]
        upper = maps[edge.upper]
        lower = maps[edge.lower]
        label = BlockLabel(
            upper.cells[block_id], upper.permutations[block_id]
        )
        if edge.phase:
            label = _advance_label(
                block_id, label, edge.lower_level, edge.letter
            )
        return _label_mismatches(
            label,
            BlockLabel(lower.cells[block_id], lower.permutations[block_id]),
        )
    terminal = anchor_terminals()[edge_id - PAIR_COUNT]
    upper = maps[terminal.parent]
    label = _forward_anchor(
        terminal,
        block_id,
        BlockLabel(upper.cells[block_id], upper.permutations[block_id]),
    )
    target = _anchor_data()[1][terminal.id]
    return _label_mismatches(
        label,
        BlockLabel(target.cells[block_id], target.permutations[block_id]),
    )


def per_block_scaled_costs(
    families: tuple[BoundaryFamily, ...],
) -> tuple[int, ...]:
    maps = _maps_by_node(families)
    weights = _scaled_edge_weights()
    return tuple(
        sum(
            weights[edge_id]
            * _edge_mismatch_from_maps(maps, block_id, edge_id)
            for edge_id in range(EDGE_COUNT)
        )
        for block_id in range(BLOCK_COUNT)
    )


@lru_cache(maxsize=1)
def build_coupled_witness() -> CoupledHorizon5Witness:
    solver = _solver()
    base = _baseline_families()
    families = _patched_families()
    if any(not solver.validate_family(family) for family in families):
        raise AssertionError("patched horizon-5 family is not bijective")
    reports = tuple(
        solver.refinement_report(families[index], families[index - 1])
        for index in range(1, 4)
    )
    costs = per_block_scaled_costs(families)
    if Counter(costs) != Counter({70: 624, 90: 1}):
        raise AssertionError("coupled horizon-5 block-cost census changed")

    cell_changes = 0
    ordinary_changes = 0
    special_changes = 0
    for old_family, new_family in zip(base, families, strict=True):
        for old, new in zip(old_family.maps, new_family.maps, strict=True):
            cell_changes += sum(a != b for a, b in zip(old.cells, new.cells))
            ordinary_changes += sum(
                a != b
                for a, b in zip(
                    old.permutations[:SPECIAL_BLOCK],
                    new.permutations[:SPECIAL_BLOCK],
                )
            )
            special_changes += (
                old.permutations[SPECIAL_BLOCK]
                != new.permutations[SPECIAL_BLOCK]
            )

    optimizer = FiniteHorizonOptimizer(
        2,
        5,
        solver=solver,
        seed="tree",
        lift_phase=1,
        freeze_minimum=True,
    )
    optimizer.maps = {
        family.level: list(family.maps) for family in families
    }
    stability = optimizer.optimize(1).sweeps[0].changed_nodes
    signatures = tuple(family_signature(family) for family in families)
    combined = sha256("".join(signatures).encode("ascii")).hexdigest()
    witness = CoupledHorizon5Witness(
        families=families,
        family_signatures=signatures,
        combined_signature_sha256=combined,
        per_block_scaled_costs=costs,
        transition_distances=tuple(report.distance for report in reports),
        objective=sum((report.distance for report in reports), Fraction(0)),
        cell_changes=cell_changes,
        ordinary_permutation_changes=ordinary_changes,
        special_permutation_changes=special_changes,
        stability_changes=stability,
    )
    if not verify_coupled_witness(witness):
        raise AssertionError("new coupled horizon-5 witness failed replay")
    return witness


def verify_coupled_witness(witness: CoupledHorizon5Witness) -> bool:
    if (
        type(witness) is not CoupledHorizon5Witness
        or type(witness.families) is not tuple
        or type(witness.family_signatures) is not tuple
        or type(witness.combined_signature_sha256) is not str
        or type(witness.per_block_scaled_costs) is not tuple
        or type(witness.transition_distances) is not tuple
        or type(witness.objective) is not Fraction
        or any(type(value) is not int for value in witness.per_block_scaled_costs)
        or any(type(value) is not Fraction for value in witness.transition_distances)
        or any(
            type(value) is not int
            for value in (
                witness.cell_changes,
                witness.ordinary_permutation_changes,
                witness.special_permutation_changes,
                witness.stability_changes,
            )
        )
        or len(witness.families) != 4
    ):
        return False
    try:
        solver = _solver()
        signatures = tuple(
            family_signature(family) for family in witness.families
        )
        reports = tuple(
            solver.refinement_report(
                witness.families[index], witness.families[index - 1]
            )
            for index in range(1, 4)
        )
        costs = per_block_scaled_costs(witness.families)
        maps = _maps_by_node(witness.families)
        weights = _scaled_edge_weights()
        families_valid = all(
            solver.validate_family(family) for family in witness.families
        )
        ordinary_mismatches = tuple(
            _edge_mismatch_from_maps(maps, 0, edge_id)
            for edge_id in range(EDGE_COUNT)
        )
        special_mismatches = tuple(
            _edge_mismatch_from_maps(maps, SPECIAL_BLOCK, edge_id)
            for edge_id in range(EDGE_COUNT)
        )
    except (
        AssertionError,
        AttributeError,
        IndexError,
        KeyError,
        TypeError,
        ValueError,
    ):
        return False
    ordinary_bad = tuple(
        edge_id for edge_id, value in enumerate(ordinary_mismatches) if value
    )
    special_bad = tuple(
        edge_id for edge_id, value in enumerate(special_mismatches) if value
    )
    return (
        families_valid
        and signatures == witness.family_signatures == COUPLED_FAMILY_SIGNATURES
        and sha256("".join(signatures).encode("ascii")).hexdigest()
        == witness.combined_signature_sha256
        == EXPECTED_COMBINED_SIGNATURE_SHA256
        and costs == witness.per_block_scaled_costs == (70,) * 624 + (90,)
        and witness.transition_distances
        == tuple(report.distance for report in reports)
        == (Fraction(209, 2500), Fraction(1, 2), Fraction(0))
        and witness.objective == Fraction(1459, 2500)
        and sum(costs) == OBJECTIVE_SCALE * witness.objective == 43770
        and (
            witness.cell_changes,
            witness.ordinary_permutation_changes,
            witness.special_permutation_changes,
            witness.stability_changes,
        )
        == (0, 5616, 25, 0)
        and ordinary_bad == ORDINARY_BAD_BASE_EDGES + (44,)
        and special_bad == EXPECTED_REASSEMBLED_BAD
        and all(ordinary_mismatches[edge_id] == 5 for edge_id in ordinary_bad)
        and all(special_mismatches[edge_id] == 5 for edge_id in special_bad)
        and sum(
            weights[edge_id] * 5 for edge_id in ordinary_bad
        )
        == 70
        and sum(
            weights[edge_id] * 5 for edge_id in special_bad
        )
        == 90
    )


@lru_cache(maxsize=1)
def build_exact_coupled_horizon5() -> ExactCoupledHorizon5Certificate:
    _require_assertion_gates()
    ordinary_report = build_ordinary_minimum()
    special_report = build_special_minimum()
    block_minima = (ordinary_report.optimum,) * ORDINARY_BLOCK_COUNT + (
        special_report.total_optimum,
    )
    witness = build_coupled_witness()
    scaled = sum(block_minima)
    certificate = ExactCoupledHorizon5Certificate(
        minimum_level=2,
        maximum_level=5,
        seed="tree",
        lift_phase=1,
        ordinary=ordinary_report,
        special=special_report,
        block_minima=block_minima,
        assignment_price=Fraction(0),
        assignment_minima=(0,) * NODE_COUNT,
        scaled_lower_bound=scaled,
        witness=witness,
        scaled_upper_bound=sum(witness.per_block_scaled_costs),
        optimum=Fraction(scaled, OBJECTIVE_SCALE),
        root_nodes=1,
        branched_nodes=0,
        fathomed_by_bound=1,
    )
    if not verify_exact_coupled_horizon5(certificate):
        raise AssertionError("new coupled horizon-5 certificate failed replay")
    return certificate


def verify_exact_coupled_horizon5(
    certificate: ExactCoupledHorizon5Certificate,
) -> bool:
    if (
        not __debug__
        or type(certificate) is not ExactCoupledHorizon5Certificate
        or type(certificate.minimum_level) is not int
        or type(certificate.maximum_level) is not int
        or type(certificate.seed) is not str
        or type(certificate.lift_phase) is not int
        or type(certificate.block_minima) is not tuple
        or any(type(value) is not int for value in certificate.block_minima)
        or type(certificate.assignment_price) is not Fraction
        or type(certificate.assignment_minima) is not tuple
        or any(type(value) is not int for value in certificate.assignment_minima)
        or type(certificate.scaled_lower_bound) is not int
        or type(certificate.scaled_upper_bound) is not int
        or type(certificate.optimum) is not Fraction
        or any(
            type(value) is not int
            for value in (
                certificate.root_nodes,
                certificate.branched_nodes,
                certificate.fathomed_by_bound,
            )
        )
    ):
        return False
    try:
        ordinary_valid = verify_ordinary_minimum(certificate.ordinary)
        special_valid = verify_special_minimum(certificate.special)
        witness_valid = verify_coupled_witness(certificate.witness)
    except (AssertionError, IndexError, TypeError, ValueError):
        return False
    expected_blocks = (70,) * ORDINARY_BLOCK_COUNT + (90,)
    return (
        (certificate.minimum_level, certificate.maximum_level)
        == (2, 5)
        and certificate.seed == "tree"
        and certificate.lift_phase == 1
        and ordinary_valid
        and special_valid
        and certificate.ordinary.optimum == 70
        and certificate.special.total_optimum == 90
        and certificate.block_minima == expected_blocks
        and certificate.assignment_price == 0
        and certificate.assignment_minima == (0,) * NODE_COUNT
        and certificate.scaled_lower_bound
        == sum(certificate.assignment_minima) + sum(certificate.block_minima)
        == 43770
        and witness_valid
        and certificate.witness.per_block_scaled_costs
        == certificate.block_minima
        and certificate.scaled_upper_bound
        == sum(certificate.witness.per_block_scaled_costs)
        == certificate.scaled_lower_bound
        and certificate.optimum
        == Fraction(certificate.scaled_lower_bound, OBJECTIVE_SCALE)
        == certificate.witness.objective
        == Fraction(1459, 2500)
        and (
            certificate.root_nodes,
            certificate.branched_nodes,
            certificate.fathomed_by_bound,
        )
        == (1, 0, 1)
    )


def format_exact_report(
    certificate: ExactCoupledHorizon5Certificate,
) -> str:
    if not verify_exact_coupled_horizon5(certificate):
        raise ValueError("cannot format an invalid coupled horizon-5 certificate")
    return "\n".join(
        (
            "EXACT COUPLED HORIZON 2..5",
            "  scope=fixed-r2 structured finite boundary; seed=tree; phase=1",
            "  ordinary full-domain retraction: vars=140 pairs=220 pins=60 "
            "orbits=625x5 checks=687500",
            "  ordinary DP: conditions=(50,4) cases=25 width=8 "
            "union-peak=1953125 message-peak=390625 optimum=70",
            "  special full-domain retraction: vars=28 pairs=44 coordinates=5 "
            "orbits=625x5 checks=137500",
            "  special DP: width=4 optima=(18,18,18,18,18) total=90",
            "  zero-price block dual: histogram={70:624,90:1} scaled=43770",
            "  coupled witness: transitions=(209/2500,1/2,0) "
            "cells-changed=0 sweep-changes=0",
            "  lower=43770 upper=43770 root=(1,0,1)",
            "  RESULT optimum=1459/2500 [NON-CANONICAL finite-horizon only]",
        )
    )


def main() -> int:
    print("ENTROPY-SELECTION COUPLED EXACT CHECK")
    print("NON-CANONICAL / NON-FORMAL / NO CLAIM STATUS")
    print(format_exact_report(build_exact_coupled_horizon5()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
