#!/usr/bin/env python3
"""Exact ordinary-block certificate for coupled horizon ``2..6``.

NON-CANONICAL LOCAL ANALYSIS.  This standard-library verifier rebuilds the
full 220-variable point bundle, verifies the commuting ``3125 -> 5``
retraction, replays an integral local-polytope dual of value ``190``, and
lifts the matching primal assignment through all 624 ordinary fibers.  The
two JSON files are data-only certificates: every inequality and every primal
constraint is reconstructed from the public definitions in this package.

Nothing in this module earns Canon, entropy, measure, or selection status.
Optimized Python (``-O``) is refused because the audit uses assertion gates.
"""

from __future__ import annotations

from array import array
from collections import Counter, deque
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path

try:
    from .bounds import (
        BlockLabel,
        ConstraintGraph,
        _advance_label,
        _expected_half,
        _label_mismatches,
        _solver,
        constraint_graph,
    )
    from .growing import source_blocks
    from .path_bounds import (
        _reverse_anchor,
        _terminal_label,
        anchor_terminals,
    )
except ImportError:  # Direct execution from this directory.
    from bounds import (  # type: ignore[no-redef]
        BlockLabel,
        ConstraintGraph,
        _advance_label,
        _expected_half,
        _label_mismatches,
        _solver,
        constraint_graph,
    )
    from growing import source_blocks  # type: ignore[no-redef]
    from path_bounds import (  # type: ignore[no-redef]
        _reverse_anchor,
        _terminal_label,
        anchor_terminals,
    )


DOMAIN = 3125
POINTS = 5
BLOCK_COUNT = 625
ORDINARY_BLOCK_COUNT = 624
ROOT_CELL = 2
MINIMUM_LEVEL = 3
MAXIMUM_LEVEL = 6
SCALE = 48

NODE_COUNT = 44
VARIABLE_COUNT = POINTS * NODE_COUNT
BASE_PAIR_COUNT = 76
PAIR_COUNT = POINTS * BASE_PAIR_COUNT
PIN_COUNT = 60
TREE_EDGE_COUNT = VARIABLE_COUNT - 1
CYCLE_RANK = PAIR_COUNT - TREE_EDGE_COUNT
COMMUTATION_CHECKS = PAIR_COUNT * DOMAIN
DUAL_CHECK_COUNT = VARIABLE_COUNT * POINTS + PAIR_COUNT * POINTS * POINTS
EXPECTED_OPTIMUM = 190

EXPECTED_POINT_WEIGHT_CENSUS = ((1, 80), (2, 280), (4, 20))
EXPECTED_PIN_WEIGHT_CENSUS = ((4, 60),)
EXPECTED_HOLONOMY_SHIFTS = (0, 2, 3)
EXPECTED_PIN_PATTERN_SHA256 = (
    "7b7f53c050ca256db9722692491db7c12b1940d56f4f1db6f87f353d3865d0ec"
)
EXPECTED_ASSIGNMENT_SHA256 = (
    "28e91f3b2d5bd2436b1be23c52140dd8ecea90c2df1326fbd4ebddebb6f5c0e0"
)
EXPECTED_DUAL_SHA256 = (
    "370b2e9a73b1a336375f79d46ff94cf0bcefba3271eeba1f15b573b9fe0d5b30"
)
EXPECTED_SOLUTION_SHA256 = (
    "270134c19eb8fc9d2fd701e738fb6e822a2fc973507d882bcfbc2c6f4d367820"
)
DUAL_FILENAME = "horizon6_ordinary_dual.json"
SOLUTION_FILENAME = "horizon6_ordinary_solution.json"


@dataclass(frozen=True, slots=True)
class PointEdge:
    upper: int
    lower: int
    forward: array
    reverse: array
    base_edge: int
    source_position: int
    weight: int


@dataclass(frozen=True, slots=True)
class PairRecord:
    upper: int
    lower: int
    delta: int
    weight: int
    base_edge: int
    source_position: int


@dataclass(frozen=True, slots=True)
class PinRecord:
    node: int
    target: int
    weight: int
    terminal: int
    source_position: int


@dataclass(frozen=True, slots=True)
class RetractionHorizon6Report:
    variable_count: int
    pair_count: int
    pin_count: int
    tree_edge_count: int
    cycle_rank: int
    holonomy_shifts: tuple[int, ...]
    generated_shift_count: int
    orbit_count: int
    orbit_size: int
    commutation_checks: int
    fixed_pin_checks: int
    pin_pattern_sha256: str


@dataclass(frozen=True, slots=True)
class OrdinaryHorizon6Report:
    retraction: RetractionHorizon6Report
    assignment: tuple[int, ...]
    assignment_sha256: str
    violated_records: tuple[int, ...]
    violation_weight_census: tuple[tuple[int, int], ...]
    optimum: int
    dual_denominator: int
    dual_objective: int
    dual_check_count: int
    dual_sha256: str
    solution_sha256: str
    lifted_block_count: int
    lifted_cost_census: tuple[tuple[int, int], ...]


def _require_assertion_gates() -> None:
    if not __debug__:
        raise RuntimeError("optimized Python disables required assertion gates")


def _inverse(permutation: array) -> array:
    result = array("H", [0]) * DOMAIN
    for source, target in enumerate(permutation):
        result[target] = source
    return result


def _point_transport(base_edge) -> tuple[array, array]:
    solver = _solver()
    upper_cells = solver.model.cells_by_half[_expected_half(base_edge.upper)]
    lower_cells = solver.model.cells_by_half[_expected_half(base_edge.lower)]
    lower_local = {cell: index for index, cell in enumerate(lower_cells)}
    forward = array("H", [0]) * DOMAIN
    for upper_local, cell in enumerate(upper_cells):
        action = (
            solver.reduced.block_action(
                base_edge.lower_level, base_edge.letter, cell
            )
            if base_edge.phase
            else None
        )
        for xi in range(POINTS):
            if action is None:
                target_cell = cell
                target_xi = xi
            else:
                target_cell = action.target_cell
                target_xi = action.apply_xi(xi)
            forward[POINTS * upper_local + xi] = (
                POINTS * lower_local[target_cell] + target_xi
            )
    if sorted(forward) != list(range(DOMAIN)):
        raise AssertionError("point transport is not bijective")
    return forward, _inverse(forward)


@lru_cache(maxsize=1)
def _point_bundle() -> tuple[
    ConstraintGraph, dict[tuple[int, tuple[int, ...]], int], tuple[PointEdge, ...]
]:
    solver = _solver()
    graph = constraint_graph(MINIMUM_LEVEL, MAXIMUM_LEVEL)
    blocks = source_blocks()
    block = blocks[0]
    expected_positions = {
        level: solver._source_positions(level, block)
        for level in range(2, MAXIMUM_LEVEL)
    }
    if any(
        solver._source_positions(level, candidate) != expected_positions[level]
        for candidate in blocks[:ORDINARY_BLOCK_COUNT]
        for level in expected_positions
    ):
        raise AssertionError("ordinary source-position actions are not homogeneous")
    if len(graph.nodes) != NODE_COUNT or len(graph.edges) != BASE_PAIR_COUNT:
        raise AssertionError("horizon-6 base graph census changed")

    node_id = {node: index for index, node in enumerate(graph.nodes)}
    edges: list[PointEdge] = []
    transport_cache: dict[int, tuple[array, array]] = {}
    for base_edge in graph.edges:
        forward, reverse = transport_cache.setdefault(
            base_edge.id, _point_transport(base_edge)
        )
        position_map = (
            solver._source_positions(base_edge.lower_level, block)
            if base_edge.phase
            else tuple(range(POINTS))
        )
        scaled = base_edge.weight * SCALE
        if scaled.denominator != 1 or scaled.numerator not in (1, 2, 4):
            raise AssertionError("unexpected scaled point-edge weight")
        for source_position, target_position in enumerate(position_map):
            edges.append(
                PointEdge(
                    upper=POINTS * node_id[base_edge.upper] + source_position,
                    lower=POINTS * node_id[base_edge.lower] + target_position,
                    forward=forward,
                    reverse=reverse,
                    base_edge=base_edge.id,
                    source_position=source_position,
                    weight=scaled.numerator,
                )
            )
    if len(edges) != PAIR_COUNT:
        raise AssertionError("ordinary point-pair census changed")
    if tuple(sorted(Counter(edge.weight for edge in edges).items())) != (
        EXPECTED_POINT_WEIGHT_CENSUS
    ):
        raise AssertionError("ordinary point-weight census changed")
    return graph, node_id, tuple(edges)


@lru_cache(maxsize=1)
def _canonical_gauge() -> tuple[
    tuple[array, ...], tuple[array, ...], frozenset[int]
]:
    _, _, edges = _point_bundle()
    adjacency: list[list[tuple[int, int, bool]]] = [
        [] for _ in range(VARIABLE_COUNT)
    ]
    for edge_id, edge in enumerate(edges):
        adjacency[edge.upper].append((edge_id, edge.lower, True))
        adjacency[edge.lower].append((edge_id, edge.upper, False))

    parent = [-1] * VARIABLE_COUNT
    parent_edge = [-1] * VARIABLE_COUNT
    parent_forward = [False] * VARIABLE_COUNT
    parent[0] = 0
    queue = deque((0,))
    discovery = [0]
    while queue:
        here = queue.popleft()
        for edge_id, neighbor, forward in sorted(adjacency[here]):
            if parent[neighbor] >= 0:
                continue
            parent[neighbor] = here
            parent_edge[neighbor] = edge_id
            parent_forward[neighbor] = forward
            queue.append(neighbor)
            discovery.append(neighbor)
    if len(discovery) != VARIABLE_COUNT:
        raise AssertionError("ordinary point bundle is disconnected")

    transports: list[array | None] = [None] * VARIABLE_COUNT
    inverses: list[array | None] = [None] * VARIABLE_COUNT
    transports[0] = array("H", range(DOMAIN))
    inverses[0] = array("H", range(DOMAIN))
    for node in discovery[1:]:
        previous = parent[node]
        edge = edges[parent_edge[node]]
        permutation = edge.forward if parent_forward[node] else edge.reverse
        previous_transport = transports[previous]
        if previous_transport is None:
            raise AssertionError("gauge parent was not initialized")
        transport = array("H", (permutation[x] for x in previous_transport))
        transports[node] = transport
        inverses[node] = _inverse(transport)
    result_t = tuple(item for item in transports if item is not None)
    result_i = tuple(item for item in inverses if item is not None)
    if len(result_t) != VARIABLE_COUNT or len(result_i) != VARIABLE_COUNT:
        raise AssertionError("gauge lost a point variable")
    tree_edges = frozenset(parent_edge[1:])
    if len(tree_edges) != TREE_EDGE_COUNT:
        raise AssertionError("ordinary gauge tree census changed")
    return result_t, result_i, tree_edges


@lru_cache(maxsize=1)
def _pin_data() -> tuple[tuple[int, ...], tuple[int, ...], int]:
    graph, node_id, _ = _point_bundle()
    transports, inverses, _ = _canonical_gauge()
    solver = _solver()
    terminals = anchor_terminals()
    fibers = []
    common_pattern = None
    representative_targets = []
    for block_id in range(ORDINARY_BLOCK_COUNT):
        normalized = []
        local_targets = []
        for terminal in terminals:
            label = _reverse_anchor(
                terminal,
                block_id,
                _terminal_label(terminal.id, block_id),
            )
            parent_id = node_id[terminal.parent]
            local_cell = solver.model.cells_by_half[
                _expected_half(terminal.parent)
            ].index(label.cell)
            for source_position in range(POINTS):
                variable = POINTS * parent_id + source_position
                target = POINTS * local_cell + label.permutation[source_position]
                root_state = inverses[variable][target]
                normalized.append(root_state)
                local_targets.append((variable, target))
        cells = {state // POINTS for state in normalized}
        pattern = tuple(state % POINTS for state in normalized)
        if len(cells) != 1 or set(pattern) != set(range(POINTS)):
            raise AssertionError("ordinary pins left one five-state orbit")
        fibers.append(next(iter(cells)))
        if common_pattern is None:
            common_pattern = pattern
            representative_targets = local_targets
        elif pattern != common_pattern:
            raise AssertionError("ordinary reduced pin patterns differ")
    if common_pattern is None:
        raise AssertionError("ordinary pin census is empty")
    if len(set(fibers)) != ORDINARY_BLOCK_COUNT or set(range(BLOCK_COUNT)) - set(
        fibers
    ) != {0}:
        raise AssertionError("ordinary anchor-fiber coverage changed")
    if fibers[0] != ROOT_CELL:
        raise AssertionError("representative ordinary root fiber changed")
    if sha256(bytes(common_pattern)).hexdigest() != EXPECTED_PIN_PATTERN_SHA256:
        raise AssertionError("ordinary horizon-6 pin pattern changed")
    fixed_checks = 0
    for variable, target in representative_targets:
        root = inverses[variable][target]
        fixed = transports[variable][POINTS * ROOT_CELL + root % POINTS]
        if fixed != target:
            raise AssertionError("representative pin is not fixed by retraction")
        fixed_checks += 1
    if fixed_checks != PIN_COUNT:
        raise AssertionError("ordinary fixed-pin census changed")
    return tuple(fibers), common_pattern, fixed_checks


@lru_cache(maxsize=1)
def _records() -> tuple[PairRecord | PinRecord, ...]:
    graph, node_id, edges = _point_bundle()
    transports, inverses, _ = _canonical_gauge()
    _, pin_pattern, _ = _pin_data()
    records: list[PairRecord | PinRecord] = []
    for edge in edges:
        images = tuple(
            inverses[edge.lower][
                edge.forward[
                    transports[edge.upper][POINTS * ROOT_CELL + value]
                ]
            ]
            for value in range(POINTS)
        )
        if any(image // POINTS != ROOT_CELL for image in images):
            raise AssertionError("reduced pair edge left the target orbit")
        residues = tuple(image % POINTS for image in images)
        delta = residues[0]
        if residues != tuple((value + delta) % POINTS for value in range(POINTS)):
            raise AssertionError("reduced pair edge is not a Z5 translation")
        records.append(
            PairRecord(
                upper=edge.upper,
                lower=edge.lower,
                delta=delta,
                weight=edge.weight,
                base_edge=edge.base_edge,
                source_position=edge.source_position,
            )
        )
    terminals = anchor_terminals()
    if len(pin_pattern) != PIN_COUNT:
        raise AssertionError("reduced pin count changed")
    for terminal in terminals:
        scaled = terminal.weight * SCALE
        if scaled.denominator != 1 or scaled.numerator != 4:
            raise AssertionError("anchor pin weight changed")
        for source_position in range(POINTS):
            variable = POINTS * graph.nodes.index(terminal.parent) + source_position
            records.append(
                PinRecord(
                    node=variable,
                    target=pin_pattern[POINTS * terminal.id + source_position],
                    weight=scaled.numerator,
                    terminal=terminal.id,
                    source_position=source_position,
                )
            )
    if len(records) != PAIR_COUNT + PIN_COUNT:
        raise AssertionError("ordinary reduced-record census changed")
    if not all(type(record) is PairRecord for record in records[:PAIR_COUNT]):
        raise AssertionError("pair records are not first in canonical order")
    if not all(type(record) is PinRecord for record in records[PAIR_COUNT:]):
        raise AssertionError("pin records are not last in canonical order")
    if tuple(
        sorted(Counter(record.weight for record in records[PAIR_COUNT:]).items())
    ) != EXPECTED_PIN_WEIGHT_CENSUS:
        raise AssertionError("ordinary pin-weight census changed")
    return tuple(records)


@lru_cache(maxsize=1)
def _retraction_report() -> RetractionHorizon6Report:
    _, _, edges = _point_bundle()
    transports, inverses, tree_edges = _canonical_gauge()
    shifts = set()
    chord_count = 0
    for edge_id, edge in enumerate(edges):
        if edge_id in tree_edges:
            continue
        chord_count += 1
        shift = None
        upper_t = transports[edge.upper]
        lower_i = inverses[edge.lower]
        for state in range(DOMAIN):
            image = lower_i[edge.forward[upper_t[state]]]
            if image // POINTS != state // POINTS:
                raise AssertionError("chord holonomy moved a root cell")
            candidate = (image - state) % POINTS
            if shift is None:
                shift = candidate
            elif candidate != shift:
                raise AssertionError("chord holonomy is not a uniform shift")
        if shift is None:
            raise AssertionError("empty chord permutation")
        shifts.add(shift)
    if chord_count != CYCLE_RANK or tuple(sorted(shifts)) != (
        EXPECTED_HOLONOMY_SHIFTS
    ):
        raise AssertionError("ordinary horizon-6 holonomy census changed")
    generated = {0}
    while True:
        enlarged = {
            (left + right) % POINTS for left in generated for right in shifts
        } | generated
        if enlarged == generated:
            break
        generated = enlarged
    if generated != set(range(POINTS)):
        raise AssertionError("ordinary holonomies do not generate Z5")

    checks = 0
    for edge in edges:
        upper_t = transports[edge.upper]
        upper_i = inverses[edge.upper]
        lower_t = transports[edge.lower]
        lower_i = inverses[edge.lower]
        for state in range(DOMAIN):
            left_state = edge.forward[state]
            left = lower_t[
                POINTS * ROOT_CELL + lower_i[left_state] % POINTS
            ]
            retracted = upper_t[
                POINTS * ROOT_CELL + upper_i[state] % POINTS
            ]
            right = edge.forward[retracted]
            if left != right:
                raise AssertionError("node retraction does not commute")
            checks += 1
    if checks != COMMUTATION_CHECKS:
        raise AssertionError("ordinary commutation-check census changed")
    _, pin_pattern, fixed_checks = _pin_data()
    return RetractionHorizon6Report(
        variable_count=VARIABLE_COUNT,
        pair_count=PAIR_COUNT,
        pin_count=PIN_COUNT,
        tree_edge_count=TREE_EDGE_COUNT,
        cycle_rank=CYCLE_RANK,
        holonomy_shifts=tuple(sorted(shifts)),
        generated_shift_count=len(generated),
        orbit_count=DOMAIN // POINTS,
        orbit_size=POINTS,
        commutation_checks=checks,
        fixed_pin_checks=fixed_checks,
        pin_pattern_sha256=sha256(bytes(pin_pattern)).hexdigest(),
    )


def _read_certificate(filename: str, expected_sha256: str) -> dict[str, object]:
    path = Path(__file__).with_name(filename)
    raw = path.read_bytes()
    if sha256(raw).hexdigest() != expected_sha256:
        raise AssertionError(f"{filename} hash changed")
    try:
        data = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise AssertionError(f"{filename} is not canonical JSON data") from error
    if type(data) is not dict or any(type(key) is not str for key in data):
        raise AssertionError(f"{filename} top level is not an exact object")
    return data


def _exact_int_list(value: object, length: int, name: str) -> tuple[int, ...]:
    if (
        type(value) is not list
        or len(value) != length
        or any(type(item) is not int for item in value)
    ):
        raise AssertionError(f"{name} is not an exact integer list")
    return tuple(value)


@lru_cache(maxsize=1)
def _solution_data() -> tuple[tuple[int, ...], tuple[int, ...], int]:
    data = _read_certificate(SOLUTION_FILENAME, EXPECTED_SOLUTION_SHA256)
    if set(data) != {"assignment", "violated_records"}:
        raise AssertionError("solution certificate keys changed")
    assignment = _exact_int_list(data["assignment"], VARIABLE_COUNT, "assignment")
    if any(value not in range(POINTS) for value in assignment):
        raise AssertionError("solution assignment left Z5")
    if sha256(bytes(assignment)).hexdigest() != EXPECTED_ASSIGNMENT_SHA256:
        raise AssertionError("solution assignment signature changed")
    violated = _exact_int_list(data["violated_records"], 80, "violated_records")
    if tuple(sorted(set(violated))) != violated or any(
        item not in range(PAIR_COUNT + PIN_COUNT) for item in violated
    ):
        raise AssertionError("solution violation support is not canonical")

    replayed = []
    cost = 0
    records = _records()
    for record_id, record in enumerate(records):
        if type(record) is PairRecord:
            satisfied = assignment[record.lower] == (
                assignment[record.upper] + record.delta
            ) % POINTS
        else:
            satisfied = assignment[record.node] == record.target
        if not satisfied:
            replayed.append(record_id)
            cost += record.weight
    if tuple(replayed) != violated or cost != EXPECTED_OPTIMUM:
        raise AssertionError("ordinary horizon-6 primal replay changed")
    return assignment, violated, cost


@lru_cache(maxsize=1)
def _dual_data() -> tuple[int, int, int]:
    data = _read_certificate(DUAL_FILENAME, EXPECTED_DUAL_SHA256)
    if set(data) != {"alpha", "beta", "denominator", "gamma"}:
        raise AssertionError("dual certificate keys changed")
    denominator = data["denominator"]
    if type(denominator) is not int or denominator <= 0:
        raise AssertionError("dual denominator is not a positive exact integer")
    alpha = _exact_int_list(data["alpha"], VARIABLE_COUNT, "alpha")
    beta = _exact_int_list(data["beta"], PAIR_COUNT * POINTS, "beta")
    gamma = _exact_int_list(data["gamma"], PAIR_COUNT * POINTS, "gamma")

    records = _records()
    unary = [[0] * POINTS for _ in range(VARIABLE_COUNT)]
    outgoing: list[list[int]] = [[] for _ in range(VARIABLE_COUNT)]
    incoming: list[list[int]] = [[] for _ in range(VARIABLE_COUNT)]
    for record_id, record in enumerate(records):
        if type(record) is PairRecord:
            outgoing[record.upper].append(record_id)
            incoming[record.lower].append(record_id)
        else:
            for value in range(POINTS):
                if value != record.target:
                    unary[record.node][value] += record.weight

    checks = 0
    for variable in range(VARIABLE_COUNT):
        for value in range(POINTS):
            left = alpha[variable]
            left -= sum(beta[POINTS * edge + value] for edge in outgoing[variable])
            left -= sum(gamma[POINTS * edge + value] for edge in incoming[variable])
            if left > denominator * unary[variable][value]:
                raise AssertionError("dual y-feasibility inequality failed")
            checks += 1
    for edge_id, record in enumerate(records[:PAIR_COUNT]):
        if type(record) is not PairRecord:
            raise AssertionError("dual pair ordering changed")
        for upper_value in range(POINTS):
            for lower_value in range(POINTS):
                pair_cost = record.weight * (
                    lower_value != (upper_value + record.delta) % POINTS
                )
                left = (
                    beta[POINTS * edge_id + upper_value]
                    + gamma[POINTS * edge_id + lower_value]
                )
                if left > denominator * pair_cost:
                    raise AssertionError("dual z-feasibility inequality failed")
                checks += 1
    if checks != DUAL_CHECK_COUNT:
        raise AssertionError("dual inequality census changed")
    objective = Fraction(sum(alpha), denominator)
    if objective.denominator != 1 or objective.numerator != EXPECTED_OPTIMUM:
        raise AssertionError("ordinary horizon-6 dual objective changed")
    return denominator, objective.numerator, checks


@lru_cache(maxsize=1)
def lifted_ordinary_labels() -> tuple[
    ConstraintGraph,
    tuple[tuple[BlockLabel, ...], ...],
    tuple[frozenset[int], ...],
]:
    """Lift the certified reduced assignment through all ordinary fibers."""

    _require_assertion_gates()
    graph, _, _ = _point_bundle()
    transports, _, _ = _canonical_gauge()
    fibers, _, _ = _pin_data()
    assignment, _, _ = _solution_data()
    solver = _solver()
    node_cells = [set() for _ in graph.nodes]
    ordinary_labels = []
    for block_id, fiber in enumerate(fibers):
        block_labels = []
        for node_index, node in enumerate(graph.nodes):
            decoded = []
            for source_position in range(POINTS):
                variable = POINTS * node_index + source_position
                state = transports[variable][
                    POINTS * fiber + assignment[variable]
                ]
                local_cell, xi = divmod(state, POINTS)
                cell = solver.model.cells_by_half[_expected_half(node)][local_cell]
                decoded.append((cell, xi))
            cells = {cell for cell, _ in decoded}
            permutation = tuple(xi for _, xi in decoded)
            if len(cells) != 1 or set(permutation) != set(range(POINTS)):
                raise AssertionError("ordinary reduced points do not reassemble")
            cell = next(iter(cells))
            node_cells[node_index].add(cell)
            block_labels.append(BlockLabel(cell, permutation))
        ordinary_labels.append(tuple(block_labels))
    if len(ordinary_labels) != ORDINARY_BLOCK_COUNT or any(
        len(cells) != ORDINARY_BLOCK_COUNT for cells in node_cells
    ):
        raise AssertionError("ordinary lifted cells violate all-different")
    return (
        graph,
        tuple(ordinary_labels),
        tuple(frozenset(cells) for cells in node_cells),
    )


@lru_cache(maxsize=1)
def _lifted_cost_census() -> tuple[tuple[int, int], ...]:
    graph, labels, _ = lifted_ordinary_labels()
    node_id = {node: index for index, node in enumerate(graph.nodes)}
    costs = []
    for block_id, block_labels in enumerate(labels):
        cost = 0
        for edge in graph.edges:
            label = block_labels[node_id[edge.upper]]
            if edge.phase:
                label = _advance_label(
                    block_id, label, edge.lower_level, edge.letter
                )
            mismatch = _label_mismatches(
                label, block_labels[node_id[edge.lower]]
            )
            scaled = edge.weight * SCALE
            if scaled.denominator != 1:
                raise AssertionError("lifted pair weight is not integral")
            cost += scaled.numerator * mismatch
        for terminal in anchor_terminals():
            target = _reverse_anchor(
                terminal,
                block_id,
                _terminal_label(terminal.id, block_id),
            )
            mismatch = _label_mismatches(
                block_labels[node_id[terminal.parent]], target
            )
            scaled = terminal.weight * SCALE
            if scaled.denominator != 1:
                raise AssertionError("lifted pin weight is not integral")
            cost += scaled.numerator * mismatch
        costs.append(cost)
    census = tuple(sorted(Counter(costs).items()))
    if census != ((EXPECTED_OPTIMUM, ORDINARY_BLOCK_COUNT),):
        raise AssertionError("ordinary lifted label-level cost changed")
    return census


@lru_cache(maxsize=1)
def _compute_ordinary_horizon6() -> OrdinaryHorizon6Report:
    retraction = _retraction_report()
    assignment, violated, optimum = _solution_data()
    denominator, dual_objective, dual_checks = _dual_data()
    lifted_census = _lifted_cost_census()
    records = _records()
    weight_census = tuple(
        sorted(Counter(records[index].weight for index in violated).items())
    )
    if optimum != dual_objective:
        raise AssertionError("ordinary horizon-6 lower and upper bounds differ")
    return OrdinaryHorizon6Report(
        retraction=retraction,
        assignment=assignment,
        assignment_sha256=sha256(bytes(assignment)).hexdigest(),
        violated_records=violated,
        violation_weight_census=weight_census,
        optimum=optimum,
        dual_denominator=denominator,
        dual_objective=dual_objective,
        dual_check_count=dual_checks,
        dual_sha256=EXPECTED_DUAL_SHA256,
        solution_sha256=EXPECTED_SOLUTION_SHA256,
        lifted_block_count=ORDINARY_BLOCK_COUNT,
        lifted_cost_census=lifted_census,
    )


def build_ordinary_horizon6() -> OrdinaryHorizon6Report:
    _require_assertion_gates()
    return _compute_ordinary_horizon6()


def _exact_int_tuple(value: object, length: int | None = None) -> bool:
    return (
        type(value) is tuple
        and (length is None or len(value) == length)
        and all(type(item) is int for item in value)
    )


def _exact_int_pair_tuple(value: object) -> bool:
    return (
        type(value) is tuple
        and all(
            type(item) is tuple
            and len(item) == 2
            and type(item[0]) is int
            and type(item[1]) is int
            for item in value
        )
    )


def verify_ordinary_horizon6(report: OrdinaryHorizon6Report) -> bool:
    try:
        if type(report) is not OrdinaryHorizon6Report:
            return False
        retraction = report.retraction
        if type(retraction) is not RetractionHorizon6Report:
            return False
        if not all(
            type(value) is int
            for value in (
                retraction.variable_count,
                retraction.pair_count,
                retraction.pin_count,
                retraction.tree_edge_count,
                retraction.cycle_rank,
                retraction.generated_shift_count,
                retraction.orbit_count,
                retraction.orbit_size,
                retraction.commutation_checks,
                retraction.fixed_pin_checks,
            )
        ):
            return False
        if not _exact_int_tuple(retraction.holonomy_shifts):
            return False
        if type(retraction.pin_pattern_sha256) is not str:
            return False
        if not _exact_int_tuple(report.assignment, VARIABLE_COUNT):
            return False
        if not _exact_int_tuple(report.violated_records):
            return False
        if not _exact_int_pair_tuple(report.violation_weight_census):
            return False
        if not _exact_int_pair_tuple(report.lifted_cost_census):
            return False
        if not all(
            type(value) is int
            for value in (
                report.optimum,
                report.dual_denominator,
                report.dual_objective,
                report.dual_check_count,
                report.lifted_block_count,
            )
        ):
            return False
        if not all(
            type(value) is str
            for value in (
                report.assignment_sha256,
                report.dual_sha256,
                report.solution_sha256,
            )
        ):
            return False
        return __debug__ and report == _compute_ordinary_horizon6()
    except (AssertionError, AttributeError, KeyError, TypeError, ValueError):
        return False


def format_ordinary_report(report: OrdinaryHorizon6Report) -> str:
    if not verify_ordinary_horizon6(report):
        raise ValueError("cannot format an invalid horizon-6 ordinary report")
    return "\n".join(
        (
            "HORIZON 2..6 ORDINARY EXACT CERTIFICATE",
            "  point bundle: vars=220 pairs=380 pins=60 tree=219 chords=161",
            "  retraction: shifts=(0,2,3) generates=Z5 orbits=625x5"
            " checks=1187500 pins-fixed=60",
            "  local-polytope dual: denominator=1 inequalities=10600"
            " objective=190",
            "  primal replay: cost=190 violated=80 assignment="
            + report.assignment_sha256,
            "  lift: ordinary-blocks=624 reassembly=PASS all-different=PASS"
            " label-costs={190:624}",
            "  RESULT ordinary=190 [NON-CANONICAL finite-horizon only]",
        )
    )


def main() -> int:
    print("ENTROPY-SELECTION HORIZON-6 ORDINARY CHECK")
    print("NON-CANONICAL / NON-FORMAL / NO CLAIM STATUS")
    print(format_ordinary_report(build_ordinary_horizon6()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
