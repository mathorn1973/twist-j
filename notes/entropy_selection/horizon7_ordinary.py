#!/usr/bin/env python3
"""Exact ordinary-block certificate for coupled horizon ``2..7``.

NON-CANONICAL LOCAL ANALYSIS.  This standard-library verifier rebuilds the
full 320-variable point bundle, verifies the commuting ``3125 -> 5``
retraction, replays an exact branch-and-bound certificate excluding cost
``<= 219`` on every reassemblable branch, and lifts the matching primal
assignment through all 624 ordinary fibers.  The
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
MAXIMUM_LEVEL = 7
SCALE = 48

NODE_COUNT = 64
VARIABLE_COUNT = POINTS * NODE_COUNT
BASE_PAIR_COUNT = 116
PAIR_COUNT = POINTS * BASE_PAIR_COUNT
PIN_COUNT = 60
TREE_EDGE_COUNT = VARIABLE_COUNT - 1
CYCLE_RANK = PAIR_COUNT - TREE_EDGE_COUNT
COMMUTATION_CHECKS = PAIR_COUNT * DOMAIN
STRUCTURE_TABLE_CHECKS = BLOCK_COUNT * VARIABLE_COUNT * POINTS
EXPECTED_OPTIMUM = 220
BNB_THRESHOLD = 219

EXPECTED_POINT_WEIGHT_CENSUS = ((1, 240), (2, 320), (4, 20))
EXPECTED_PIN_WEIGHT_CENSUS = ((4, 60),)
EXPECTED_HOLONOMY_SHIFTS = (0, 2, 3)
EXPECTED_PIN_PATTERN_SHA256 = (
    "3fdc3cbc20099787b468764a2a0de2b55ee58c75b19a60d7cb24917fe569720f"
)
EXPECTED_ASSIGNMENT_SHA256 = (
    "821531f74d3ef86f0f8b5087c6e4f7a763dded1fb928d755837298c6ceaebd42"
)
EXPECTED_DECODED_MAP_SHA256 = (
    "946b079084b27b0ef51cc220de08f6d5f1969ee0bcb208b429dba7dffe914987"
)
EXPECTED_STRUCTURE_TABLE_SHA256 = (
    "7e6b33a78920aa6124dd7e237c710f3fd134073da3adb12feaf92226fe59c14b"
)
EXPECTED_SOLUTION_SHA256 = (
    "af60a50bb0afaa1d81456d53289df591f38e30529c8b4f7b5b16535793a1c8e8"
)
EXPECTED_BNB_SHA256 = (
    "5f3c2ce879bc79d16a67c9b2098787d5afb5f3bd5bac8dc83cf1e3dd0e4e29e8"
)
EXPECTED_MODEL_SHA256 = (
    "fad578943e6ff40179359592820b6117837aaa924b1a1f38d61723889d1abb3d"
)
EXPECTED_BNB_BYTES = 394_650
EXPECTED_BNB_NODE_COUNT = 1_181
EXPECTED_BNB_BRANCH_COUNT = 236
EXPECTED_BNB_DUAL_LEAF_COUNT = 190
EXPECTED_BNB_INVALID_LEAF_COUNT = 755
EXPECTED_BNB_ROW_COUNT = 2_013
EXPECTED_BNB_DUAL_COUNT = 190
EXPECTED_BNB_MAX_DEPTH = 11
EXPECTED_BNB_DUAL_CHECKS = 2_911_700
EXPECTED_BNB_DENOMINATOR_CENSUS = ((1, 163), (2, 21), (3, 5), (4, 1))
BNB_FILENAME = "horizon7_ordinary_bnb.json"
SOLUTION_FILENAME = "horizon7_ordinary_solution.json"


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
class RetractionHorizon7Report:
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
    structure_table_checks: int
    structure_table_sha256: str
    pin_pattern_sha256: str


@dataclass(frozen=True, slots=True)
class BnbHorizon7Report:
    node_count: int
    branch_count: int
    dual_leaf_count: int
    invalid_leaf_count: int
    row_count: int
    dual_count: int
    max_depth: int
    dual_check_count: int
    denominator_census: tuple[tuple[int, int], ...]
    minimum_bound: Fraction
    model_sha256: str
    certificate_sha256: str


@dataclass(frozen=True, slots=True)
class OrdinaryHorizon7Report:
    retraction: RetractionHorizon7Report
    assignment: tuple[int, ...]
    assignment_sha256: str
    violated_records: tuple[int, ...]
    violation_weight_census: tuple[tuple[int, int], ...]
    optimum: int
    bnb: BnbHorizon7Report
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
        raise AssertionError("horizon-7 base graph census changed")

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
    pin_pattern_sha256 = sha256(bytes(common_pattern)).hexdigest()
    if pin_pattern_sha256 != EXPECTED_PIN_PATTERN_SHA256:
        raise AssertionError(
            "ordinary horizon-7 pin pattern changed: " + pin_pattern_sha256
        )
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
def _retraction_report() -> RetractionHorizon7Report:
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
        raise AssertionError("ordinary horizon-7 holonomy census changed")
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
    _decoded_maps()
    return RetractionHorizon7Report(
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
        structure_table_checks=STRUCTURE_TABLE_CHECKS,
        structure_table_sha256=EXPECTED_STRUCTURE_TABLE_SHA256,
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


def _exact_int_list(
    value: object, length: int | None, name: str
) -> tuple[int, ...]:
    if (
        type(value) is not list
        or (length is not None and len(value) != length)
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
    violated = _exact_int_list(data["violated_records"], 100, "violated_records")
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
        raise AssertionError("ordinary horizon-7 primal replay changed")
    singleton_domains = tuple(1 << value for value in assignment)
    if _first_hall_violation(singleton_domains) is not None:
        raise AssertionError("ordinary horizon-7 witness does not reassemble")
    return assignment, violated, cost


@lru_cache(maxsize=1)
def _decoded_maps() -> tuple[tuple[int, ...], ...]:
    transports, _, _ = _canonical_gauge()
    result = tuple(
        tuple(
            transports[variable][POINTS * ROOT_CELL + value] % POINTS
            for value in range(POINTS)
        )
        for variable in range(VARIABLE_COUNT)
    )
    if any(tuple(sorted(row)) != tuple(range(POINTS)) for row in result):
        raise AssertionError("ordinary decoded-value map is not bijective")
    if sha256(bytes(value for row in result for value in row)).hexdigest() != (
        EXPECTED_DECODED_MAP_SHA256
    ):
        raise AssertionError("ordinary decoded-value map changed")
    checks = 0
    table_digest = sha256()
    node_cells: list[list[int]] = [[] for _ in range(NODE_COUNT)]
    for fibre in range(BLOCK_COUNT):
        for node in range(NODE_COUNT):
            common_cell = None
            for position in range(POINTS):
                variable = POINTS * node + position
                for value in range(POINTS):
                    state = transports[variable][POINTS * fibre + value]
                    table_digest.update(state.to_bytes(2, "little"))
                    cell, decoded = divmod(state, POINTS)
                    if common_cell is None:
                        common_cell = cell
                    elif cell != common_cell:
                        raise AssertionError(
                            "ordinary gauge orbit does not reassemble to one cell"
                        )
                    if decoded != result[variable][value]:
                        raise AssertionError(
                            "ordinary decoded-value map depends on the gauge fibre"
                        )
                    checks += 1
            if common_cell is None:
                raise AssertionError("ordinary gauge orbit is empty")
            node_cells[node].append(common_cell)
    if checks != STRUCTURE_TABLE_CHECKS:
        raise AssertionError("ordinary structure-table census changed")
    if any(sorted(cells) != list(range(BLOCK_COUNT)) for cells in node_cells):
        raise AssertionError("ordinary fibre-to-cell map is not bijective")
    if table_digest.hexdigest() != EXPECTED_STRUCTURE_TABLE_SHA256:
        raise AssertionError("ordinary structure table changed")
    return result


def _domain_values(mask: int) -> tuple[int, ...]:
    if type(mask) is not int or not 0 < mask < 1 << POINTS:
        raise AssertionError("B&B domain mask left nonempty F5")
    return tuple(value for value in range(POINTS) if mask & (1 << value))


def _first_hall_violation(
    domains: tuple[int, ...],
) -> tuple[int, int, int] | None:
    if (
        type(domains) is not tuple
        or len(domains) != VARIABLE_COUNT
        or any(type(mask) is not int or not 0 < mask < 1 << POINTS for mask in domains)
    ):
        raise AssertionError("B&B domains have the wrong exact type")
    decoded = _decoded_maps()
    for node in range(NODE_COUNT):
        decoded_domains = []
        for position in range(POINTS):
            variable = POINTS * node + position
            mask = 0
            for value in _domain_values(domains[variable]):
                mask |= 1 << decoded[variable][value]
            decoded_domains.append(mask)
        for subset in range(1, 1 << POINTS):
            union = 0
            for position in range(POINTS):
                if subset & (1 << position):
                    union |= decoded_domains[position]
            if union.bit_count() < subset.bit_count():
                return node, subset, union
    return None


@lru_cache(maxsize=1)
def _dual_model() -> tuple[
    tuple[tuple[int, ...], ...],
    tuple[tuple[int, ...], ...],
    tuple[tuple[int, ...], ...],
]:
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
    return (
        tuple(tuple(row) for row in unary),
        tuple(tuple(row) for row in outgoing),
        tuple(tuple(row) for row in incoming),
    )


def _canonical_json_bytes(value: object) -> bytes:
    return (
        json.dumps(value, separators=(",", ":"), sort_keys=True) + "\n"
    ).encode("utf-8")


@lru_cache(maxsize=1)
def _model_sha256() -> str:
    records = _records()
    model = {
        "pairs": [
            [record.upper, record.lower, record.delta, record.weight]
            for record in records[:PAIR_COUNT]
        ],
        "pins": [
            [record.node, record.target, record.weight]
            for record in records[PAIR_COUNT:]
        ],
    }
    digest = sha256(_canonical_json_bytes(model)).hexdigest()
    if digest != EXPECTED_MODEL_SHA256:
        raise AssertionError("ordinary horizon-7 reduced model changed")
    return digest


def _replay_leaf_dual(
    denominator: int,
    row_ids: tuple[int, ...],
    rows: tuple[tuple[int, ...], ...],
    domains: tuple[int, ...],
) -> tuple[Fraction, int, frozenset[int]]:
    if type(denominator) is not int or denominator <= 0:
        raise AssertionError("leaf dual denominator is not positive")
    if len(row_ids) != PAIR_COUNT:
        raise AssertionError("leaf dual row count changed")
    beta = tuple(rows[row_id] for row_id in row_ids)
    records = _records()
    unary, outgoing, incoming = _dual_model()
    gamma = []
    checks = 0
    for edge_id, record in enumerate(records[:PAIR_COUNT]):
        upper_values = _domain_values(domains[record.upper])
        lower_values = _domain_values(domains[record.lower])
        if beta[edge_id][upper_values[0]] != 0 or any(
            beta[edge_id][value] != 0
            for value in range(POINTS)
            if value not in upper_values
        ):
            raise AssertionError("leaf beta row is not in canonical gauge")
        edge_gamma = []
        for lower_value in range(POINTS):
            if lower_value in lower_values:
                edge_gamma.append(
                    min(
                        denominator
                        * record.weight
                        * (
                            lower_value
                            != (upper_value + record.delta) % POINTS
                        )
                        - beta[edge_id][upper_value]
                        for upper_value in upper_values
                    )
                )
            else:
                edge_gamma.append(0)
        gamma.append(tuple(edge_gamma))
        for upper_value in upper_values:
            for lower_value in lower_values:
                left = (
                    beta[edge_id][upper_value]
                    + gamma[edge_id][lower_value]
                )
                right = denominator * record.weight * (
                    lower_value != (upper_value + record.delta) % POINTS
                )
                if left > right:
                    raise AssertionError("leaf pair-dual inequality failed")
                checks += 1

    alpha = []
    for variable in range(VARIABLE_COUNT):
        values = _domain_values(domains[variable])
        right_sides = tuple(
            denominator * unary[variable][value]
            + sum(beta[edge][value] for edge in outgoing[variable])
            + sum(gamma[edge][value] for edge in incoming[variable])
            for value in values
        )
        alpha.append(min(right_sides))
        if any(alpha[-1] > right for right in right_sides):
            raise AssertionError("leaf unary-dual inequality failed")
        checks += len(values)
    bound = Fraction(sum(alpha), denominator)
    if bound <= BNB_THRESHOLD:
        raise AssertionError("leaf dual does not exclude the target threshold")
    return bound, checks, frozenset(row_ids)


@lru_cache(maxsize=1)
def _bnb_data() -> BnbHorizon7Report:
    path = Path(__file__).with_name(BNB_FILENAME)
    if path.stat().st_size != EXPECTED_BNB_BYTES:
        raise AssertionError("B&B certificate byte count changed")
    data = _read_certificate(BNB_FILENAME, EXPECTED_BNB_SHA256)
    if set(data) != {
        "duals",
        "format",
        "model_sha256",
        "nodes",
        "root",
        "rows",
        "threshold",
    }:
        raise AssertionError("B&B certificate keys changed")
    if data["format"] != "twist-j-horizon7-bnb-v2":
        raise AssertionError("B&B certificate format changed")
    if data["model_sha256"] != _model_sha256():
        raise AssertionError("B&B certificate names the wrong reduced model")
    if type(data["threshold"]) is not int or data["threshold"] != BNB_THRESHOLD:
        raise AssertionError("B&B threshold changed")
    if type(data["root"]) is not int or data["root"] != 0:
        raise AssertionError("B&B root changed")

    raw_rows = data["rows"]
    if type(raw_rows) is not list or len(raw_rows) != EXPECTED_BNB_ROW_COUNT:
        raise AssertionError("B&B row dictionary count changed")
    rows = tuple(
        _exact_int_list(row, POINTS, f"B&B row {index}")
        for index, row in enumerate(raw_rows)
    )
    if len(set(rows)) != len(rows):
        raise AssertionError("B&B row dictionary contains duplicates")

    raw_duals = data["duals"]
    if type(raw_duals) is not list or len(raw_duals) != EXPECTED_BNB_DUAL_COUNT:
        raise AssertionError("B&B dual dictionary count changed")
    duals = []
    for dual_id, raw_dual in enumerate(raw_duals):
        if type(raw_dual) is not list or len(raw_dual) != 2:
            raise AssertionError(f"B&B dual {dual_id} has the wrong shape")
        denominator = raw_dual[0]
        if type(denominator) is not int or denominator <= 0:
            raise AssertionError("B&B dual denominator is not positive")
        row_ids = _exact_int_list(
            raw_dual[1], PAIR_COUNT, f"B&B dual {dual_id} row ids"
        )
        if any(not 0 <= row_id < len(rows) for row_id in row_ids):
            raise AssertionError("B&B dual row id left the dictionary")
        duals.append((denominator, row_ids))
    if len(set(duals)) != len(duals):
        raise AssertionError("B&B dual dictionary contains duplicates")

    nodes = data["nodes"]
    if type(nodes) is not list or len(nodes) != EXPECTED_BNB_NODE_COUNT:
        raise AssertionError("B&B node count changed")
    visited: set[int] = set()
    used_duals: set[int] = set()
    used_rows: set[int] = set()
    branch_count = 0
    dual_leaf_count = 0
    invalid_leaf_count = 0
    max_depth = 0
    dual_checks = 0
    denominator_census: Counter[int] = Counter()
    bounds = []
    stack = [(0, (31,) * VARIABLE_COUNT, 0)]
    while stack:
        node_id, domains, depth = stack.pop()
        if type(node_id) is not int or not 0 <= node_id < len(nodes):
            raise AssertionError("B&B child id left the node list")
        if node_id in visited:
            raise AssertionError("B&B node has more than one parent or a cycle")
        visited.add(node_id)
        max_depth = max(max_depth, depth)
        node = nodes[node_id]
        if type(node) is not list or not node or type(node[0]) is not str:
            raise AssertionError("B&B node has the wrong exact shape")
        if node[0] == "b":
            if len(node) != 3 or type(node[1]) is not int:
                raise AssertionError("B&B branch node has the wrong shape")
            variable = node[1]
            children = node[2]
            if (
                not 0 <= variable < VARIABLE_COUNT
                or type(children) is not list
                or not children
            ):
                raise AssertionError("B&B branch left the finite domain")
            parent_mask = domains[variable]
            union = 0
            pending = []
            for child in children:
                if (
                    type(child) is not list
                    or len(child) != 2
                    or type(child[0]) is not int
                    or type(child[1]) is not int
                ):
                    raise AssertionError("B&B child has the wrong exact shape")
                mask, child_id = child
                if (
                    mask == 0
                    or mask == parent_mask
                    or mask & ~parent_mask
                    or mask & union
                ):
                    raise AssertionError("B&B children are not a proper partition")
                union |= mask
                child_domains = list(domains)
                child_domains[variable] = mask
                pending.append((child_id, tuple(child_domains), depth + 1))
            if union != parent_mask:
                raise AssertionError("B&B children do not exhaust their parent")
            stack.extend(reversed(pending))
            branch_count += 1
        elif node[0] == "x":
            if (
                len(node) != 4
                or any(type(value) is not int for value in node[1:])
                or _first_hall_violation(domains) != tuple(node[1:])
            ):
                raise AssertionError("B&B Hall leaf is not an exact falsifier")
            invalid_leaf_count += 1
        elif node[0] == "l":
            if (
                len(node) != 2
                or type(node[1]) is not int
                or not 0 <= node[1] < len(duals)
            ):
                raise AssertionError("B&B dual leaf has the wrong shape")
            dual_id = node[1]
            denominator, row_ids = duals[dual_id]
            bound, checks, leaf_rows = _replay_leaf_dual(
                denominator, row_ids, rows, domains
            )
            bounds.append(bound)
            dual_checks += checks
            used_duals.add(dual_id)
            used_rows.update(leaf_rows)
            denominator_census[denominator] += 1
            dual_leaf_count += 1
        else:
            raise AssertionError("B&B node tag changed")

    if visited != set(range(len(nodes))):
        raise AssertionError("B&B certificate contains unreachable nodes")
    if used_duals != set(range(len(duals))) or used_rows != set(range(len(rows))):
        raise AssertionError("B&B certificate contains unused dictionaries")
    report = BnbHorizon7Report(
        node_count=len(nodes),
        branch_count=branch_count,
        dual_leaf_count=dual_leaf_count,
        invalid_leaf_count=invalid_leaf_count,
        row_count=len(rows),
        dual_count=len(duals),
        max_depth=max_depth,
        dual_check_count=dual_checks,
        denominator_census=tuple(sorted(denominator_census.items())),
        minimum_bound=min(bounds),
        model_sha256=_model_sha256(),
        certificate_sha256=EXPECTED_BNB_SHA256,
    )
    if (
        report.node_count != EXPECTED_BNB_NODE_COUNT
        or report.branch_count != EXPECTED_BNB_BRANCH_COUNT
        or report.dual_leaf_count != EXPECTED_BNB_DUAL_LEAF_COUNT
        or report.invalid_leaf_count != EXPECTED_BNB_INVALID_LEAF_COUNT
        or report.row_count != EXPECTED_BNB_ROW_COUNT
        or report.dual_count != EXPECTED_BNB_DUAL_COUNT
        or report.max_depth != EXPECTED_BNB_MAX_DEPTH
        or report.dual_check_count != EXPECTED_BNB_DUAL_CHECKS
        or report.denominator_census != EXPECTED_BNB_DENOMINATOR_CENSUS
        or report.minimum_bound != EXPECTED_OPTIMUM
    ):
        raise AssertionError("ordinary horizon-7 B&B census changed")
    return report


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
def _compute_ordinary_horizon7() -> OrdinaryHorizon7Report:
    retraction = _retraction_report()
    assignment, violated, optimum = _solution_data()
    bnb = _bnb_data()
    lifted_census = _lifted_cost_census()
    records = _records()
    weight_census = tuple(
        sorted(Counter(records[index].weight for index in violated).items())
    )
    if optimum != bnb.minimum_bound:
        raise AssertionError("ordinary horizon-7 lower and upper bounds differ")
    return OrdinaryHorizon7Report(
        retraction=retraction,
        assignment=assignment,
        assignment_sha256=sha256(bytes(assignment)).hexdigest(),
        violated_records=violated,
        violation_weight_census=weight_census,
        optimum=optimum,
        bnb=bnb,
        solution_sha256=EXPECTED_SOLUTION_SHA256,
        lifted_block_count=ORDINARY_BLOCK_COUNT,
        lifted_cost_census=lifted_census,
    )


def build_ordinary_horizon7() -> OrdinaryHorizon7Report:
    _require_assertion_gates()
    return _compute_ordinary_horizon7()


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


def verify_ordinary_horizon7(report: OrdinaryHorizon7Report) -> bool:
    try:
        if type(report) is not OrdinaryHorizon7Report:
            return False
        retraction = report.retraction
        if type(retraction) is not RetractionHorizon7Report:
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
                retraction.structure_table_checks,
            )
        ):
            return False
        if not _exact_int_tuple(retraction.holonomy_shifts):
            return False
        if not all(
            type(value) is str
            for value in (
                retraction.structure_table_sha256,
                retraction.pin_pattern_sha256,
            )
        ):
            return False
        if not _exact_int_tuple(report.assignment, VARIABLE_COUNT):
            return False
        if not _exact_int_tuple(report.violated_records):
            return False
        if not _exact_int_pair_tuple(report.violation_weight_census):
            return False
        if not _exact_int_pair_tuple(report.lifted_cost_census):
            return False
        if not all(type(value) is int for value in (report.optimum, report.lifted_block_count)):
            return False
        bnb = report.bnb
        if type(bnb) is not BnbHorizon7Report:
            return False
        if not all(
            type(value) is int
            for value in (
                bnb.node_count,
                bnb.branch_count,
                bnb.dual_leaf_count,
                bnb.invalid_leaf_count,
                bnb.row_count,
                bnb.dual_count,
                bnb.max_depth,
                bnb.dual_check_count,
            )
        ):
            return False
        if not _exact_int_pair_tuple(bnb.denominator_census):
            return False
        if type(bnb.minimum_bound) is not Fraction:
            return False
        if not all(
            type(value) is str
            for value in (bnb.model_sha256, bnb.certificate_sha256)
        ):
            return False
        if not all(
            type(value) is str
            for value in (
                report.assignment_sha256,
                report.solution_sha256,
            )
        ):
            return False
        return __debug__ and report == _compute_ordinary_horizon7()
    except (AssertionError, AttributeError, KeyError, TypeError, ValueError):
        return False


def format_ordinary_report(report: OrdinaryHorizon7Report) -> str:
    if not verify_ordinary_horizon7(report):
        raise ValueError("cannot format an invalid horizon-7 ordinary report")
    return "\n".join(
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
            + report.assignment_sha256,
            "  lift: ordinary-blocks=624 reassembly=PASS all-different=PASS"
            " label-costs={220:624}",
            "  RESULT ordinary=220 [NON-CANONICAL finite-horizon only]",
        )
    )


def main() -> int:
    print("ENTROPY-SELECTION HORIZON-7 ORDINARY CHECK")
    print("NON-CANONICAL / NON-FORMAL / NO CLAIM STATUS")
    print(format_ordinary_report(build_ordinary_horizon7()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
