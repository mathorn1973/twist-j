#!/usr/bin/env python3
"""Full-domain ordinary-block minimum for coupled horizon ``2..5``.

NON-CANONICAL LOCAL ANALYSIS.  This standard-library checker constructs the
140-variable point bundle, proves an equivariant ``3125 -> 5`` retraction,
and solves the reduced problem by conditioned exact min-sum elimination.
"""

from __future__ import annotations

from array import array
from collections import Counter, deque
from dataclasses import dataclass
from hashlib import sha256

try:
    from .bounds import (
        BlockLabel,
        _expected_half,
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
        _expected_half,
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
ORDINARY_BLOCKS = 624
ROOT_CELL = 2
ROOT_ORBIT = tuple(POINTS * ROOT_CELL + q for q in range(POINTS))
CONDITION_VARS = (50, 4)
EXPECTED_OPTIMUM = 70
EXPECTED_ORDER_SHA256 = (
    "ec22792c8c4623a5e39f03fd49332e1d013eda763360050b99273b80f333f249"
)
EXPECTED_GRID = (
    71, 72, 75, 75, 75,
    73, 70, 75, 75, 75,
    75, 74, 75, 77, 77,
    75, 74, 77, 75, 77,
    73, 72, 75, 75, 73,
)
EXPECTED_GRID_SHA256 = (
    "6496c92f884de1aec36933354583ec313d93e3d974daf875986b5115cc0c42d1"
)
EXPECTED_PIN_PATTERN_SHA256 = (
    "236dfaa3172464c4ba269379e4f763547db1b1fdf4af1780efb242d0ee8a89af"
)
EXPECTED_ASSIGNMENT_SHA256 = (
    "fe694ad9efe0c035f380ad830c6250915727654444507656405020b48c461e75"
)
EXPECTED_ASSIGNMENT = (
    3, 0, 0, 1, 1, 1, 1, 3, 0, 4,
    2, 1, 3, 0, 0, 1, 0, 2, 2, 4,
    3, 0, 0, 2, 4, 1, 1, 3, 2, 4,
    0, 0, 2, 1, 3, 0, 0, 2, 1, 3,
    3, 0, 0, 1, 1, 3, 0, 0, 2, 1,
    1, 3, 0, 2, 1, 3, 0, 0, 2, 1,
    1, 3, 0, 4, 1, 0, 0, 2, 1, 3,
    3, 0, 2, 1, 1, 3, 0, 2, 2, 1,
    1, 3, 0, 2, 1, 1, 3, 0, 2, 1,
    3, 0, 0, 2, 1, 3, 0, 0, 2, 1,
    1, 3, 0, 4, 1, 1, 3, 0, 4, 1,
    3, 0, 0, 2, 1, 3, 0, 0, 2, 1,
    1, 3, 0, 2, 1, 1, 3, 0, 2, 1,
    3, 0, 0, 2, 1, 3, 0, 0, 2, 1,
)
EXPECTED_BASE_VIOLATIONS = (0, 1, 2, 3, 8, 9, 12, 13, 14, 15, 44)


@dataclass(frozen=True, slots=True)
class PointEdge:
    upper: int
    lower: int
    forward: array
    reverse: array
    base_edge: int
    source_position: int
    weight: int


@dataclass(slots=True)
class Factor:
    scope: tuple[int, ...]
    values: array


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


def build_point_bundle():
    solver = _solver()
    graph = constraint_graph(3, 5)
    blocks = source_blocks()
    block = blocks[0]
    expected_positions = {
        level: solver._source_positions(level, block) for level in (2, 3, 4)
    }
    if any(
        solver._source_positions(level, candidate) != expected_positions[level]
        for candidate in blocks[:ORDINARY_BLOCKS]
        for level in expected_positions
    ):
        raise AssertionError("ordinary source-position actions are not homogeneous")
    node_id = {node: index for index, node in enumerate(graph.nodes)}
    edges: list[PointEdge] = []
    for base_edge in graph.edges:
        forward, reverse = _point_transport(base_edge)
        position_map = (
            solver._source_positions(base_edge.lower_level, block)
            if base_edge.phase
            else tuple(range(POINTS))
        )
        scaled = base_edge.weight * 24
        if scaled.denominator != 1 or scaled.numerator not in (1, 2):
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
    if len(graph.nodes) != 28 or len(edges) != 220:
        raise AssertionError("ordinary point-bundle census changed")
    return graph, node_id, tuple(edges)


def canonical_gauge(edges: tuple[PointEdge, ...]):
    variable_count = 140
    adjacency: list[list[tuple[int, int, bool]]] = [
        [] for _ in range(variable_count)
    ]
    for edge_id, edge in enumerate(edges):
        adjacency[edge.upper].append((edge_id, edge.lower, True))
        adjacency[edge.lower].append((edge_id, edge.upper, False))
    parent = [-1] * variable_count
    parent_edge = [-1] * variable_count
    parent_forward = [False] * variable_count
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
    if len(discovery) != variable_count:
        raise AssertionError("ordinary point bundle is disconnected")

    transports: list[array | None] = [None] * variable_count
    inverses: list[array | None] = [None] * variable_count
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
    if len(result_t) != variable_count or len(result_i) != variable_count:
        raise AssertionError("gauge lost a point variable")
    tree_edges = frozenset(parent_edge[1:])
    return result_t, result_i, tree_edges


def verify_holonomy_and_retraction(edges, transports, inverses, tree_edges):
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
    if chord_count != 81 or shifts != set(range(POINTS)):
        raise AssertionError("ordinary holonomy census changed")

    # rho_v = T_v rho T_v^-1, rho(5*c+q)=10+q.
    for edge in edges:
        upper_t = transports[edge.upper]
        upper_i = inverses[edge.upper]
        lower_t = transports[edge.lower]
        lower_i = inverses[edge.lower]
        for state in range(DOMAIN):
            left_state = edge.forward[state]
            left = lower_t[POINTS * ROOT_CELL + lower_i[left_state] % POINTS]
            retracted = upper_t[POINTS * ROOT_CELL + upper_i[state] % POINTS]
            right = edge.forward[retracted]
            if left != right:
                raise AssertionError("node retraction does not commute")
    return chord_count, tuple(sorted(shifts))


def ordinary_pin_data(graph, node_id, transports, inverses):
    solver = _solver()
    terminals = anchor_terminals()
    fibers = []
    common_pattern = None
    representative_targets = []
    for block_id in range(ORDINARY_BLOCKS):
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
        fiber = next(iter(cells))
        fibers.append(fiber)
        if common_pattern is None:
            common_pattern = pattern
            representative_targets = local_targets
        elif pattern != common_pattern:
            raise AssertionError("ordinary reduced pin patterns differ")
    if common_pattern is None:
        raise AssertionError("ordinary pin census is empty")
    if len(set(fibers)) != ORDINARY_BLOCKS or set(range(BLOCK_COUNT)) - set(
        fibers
    ) != {0}:
        raise AssertionError("ordinary anchor-fiber coverage changed")
    if fibers[0] != ROOT_CELL:
        raise AssertionError("representative ordinary root fiber changed")
    if sha256(bytes(common_pattern)).hexdigest() != EXPECTED_PIN_PATTERN_SHA256:
        raise AssertionError("ordinary reduced pin pattern changed")
    for variable, target in representative_targets:
        root = inverses[variable][target]
        fixed = transports[variable][POINTS * ROOT_CELL + root % POINTS]
        if fixed != target:
            raise AssertionError("representative pin is not fixed by retraction")
    return tuple(fibers), common_pattern


def build_reduced_factors(edges, transports, inverses, pin_pattern):
    factors: list[Factor] = []
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
            raise AssertionError("reduced edge left the target orbit")
        residues = tuple(image % POINTS for image in images)
        delta = residues[0]
        if residues != tuple((value + delta) % POINTS for value in range(POINTS)):
            raise AssertionError("reduced edge is not a Z5 translation")
        table = array("H", [edge.weight]) * (POINTS * POINTS)
        for value in range(POINTS):
            table[POINTS * value + (value + delta) % POINTS] = 0
        if edge.upper < edge.lower:
            scope = (edge.upper, edge.lower)
        else:
            scope = (edge.lower, edge.upper)
            table = array(
                "H",
                (
                    table[POINTS * right + left]
                    for left in range(POINTS)
                    for right in range(POINTS)
                ),
            )
        factors.append(Factor(scope, table))
        records.append(
            PairRecord(
                edge.upper,
                edge.lower,
                delta,
                edge.weight,
                edge.base_edge,
                edge.source_position,
            )
        )
    terminals = anchor_terminals()
    if len(pin_pattern) != len(terminals) * POINTS:
        raise AssertionError("reduced pin count changed")
    for terminal in terminals:
        for source_position in range(POINTS):
            variable = POINTS * constraint_graph(3, 5).nodes.index(
                terminal.parent
            ) + source_position
            target = pin_pattern[POINTS * terminal.id + source_position]
            scaled = terminal.weight * 24
            if scaled.denominator != 1 or scaled.numerator != 2:
                raise AssertionError("anchor pin weight changed")
            table = array("H", [scaled.numerator]) * POINTS
            table[target] = 0
            factors.append(Factor((variable,), table))
            records.append(
                PinRecord(
                    variable,
                    target,
                    scaled.numerator,
                    terminal.id,
                    source_position,
                )
            )
    if len(factors) != 280 or len(records) != 280:
        raise AssertionError("reduced factor census changed")
    pair_weights = Counter(
        record.weight for record in records if isinstance(record, PairRecord)
    )
    if pair_weights != Counter({1: 200, 2: 20}):
        raise AssertionError("reduced pair-weight census changed")
    return factors, tuple(records)


def elimination_order(factors: list[Factor], graph):
    adjacency = [set() for _ in range(140)]
    for factor in factors:
        if len(factor.scope) == 2:
            left, right = factor.scope
            adjacency[left].add(right)
            adjacency[right].add(left)
    alive = set(range(140)) - set(CONDITION_VARS)
    order = []
    degrees = []
    level_five = sorted(
        variable
        for variable in alive
        if graph.nodes[variable // POINTS][0] == 5
    )
    for variable in level_five:
        neighbors = adjacency[variable] & alive
        degrees.append(len(neighbors))
        for neighbor in neighbors:
            adjacency[neighbor].update(neighbors - {neighbor})
        alive.remove(variable)
        order.append(variable)
    while alive:
        choices = []
        for variable in alive:
            neighbors = adjacency[variable] & alive
            fill = sum(
                1
                for left in neighbors
                for right in neighbors
                if left < right and right not in adjacency[left]
            )
            choices.append(((fill, len(neighbors), variable), variable, neighbors))
        _, variable, neighbors = min(choices)
        degrees.append(len(neighbors))
        for neighbor in neighbors:
            adjacency[neighbor].update(neighbors - {neighbor})
        alive.remove(variable)
        order.append(variable)
    digest = sha256(bytes(order)).hexdigest()
    if digest != EXPECTED_ORDER_SHA256:
        raise AssertionError("conditioned elimination order changed")
    if max(degrees) != 8 or Counter(degrees) != Counter(
        {0: 1, 1: 7, 2: 63, 3: 24, 4: 25, 5: 8, 6: 4, 7: 5, 8: 1}
    ):
        raise AssertionError("conditioned elimination width changed")
    union_entries = sum(POINTS ** (degree + 1) for degree in degrees)
    if union_entries != 4_444_930:
        raise AssertionError("conditioned DP table census changed")
    return tuple(order), tuple(degrees), union_entries


def _restrict_factor(factor: Factor, fixed: dict[int, int]) -> Factor:
    scope = factor.scope
    if len(scope) == 0:
        return Factor(scope, array("H", factor.values))
    if len(scope) == 1:
        variable = scope[0]
        if variable in fixed:
            return Factor((), array("H", (factor.values[fixed[variable]],)))
        return Factor(scope, array("H", factor.values))
    if len(scope) != 2:
        raise AssertionError("only initial unary/pair factors may be restricted")
    left, right = scope
    if left in fixed and right in fixed:
        return Factor(
            (),
            array("H", (factor.values[POINTS * fixed[left] + fixed[right]],)),
        )
    if left in fixed:
        start = POINTS * fixed[left]
        return Factor((right,), array("H", factor.values[start : start + POINTS]))
    if right in fixed:
        return Factor(
            (left,),
            array(
                "H",
                (factor.values[POINTS * value + fixed[right]] for value in range(POINTS)),
            ),
        )
    return Factor(scope, array("H", factor.values))


def _merge_same_scope(factors: list[Factor]) -> list[Factor]:
    merged: dict[tuple[int, ...], array] = {}
    for factor in factors:
        previous = merged.get(factor.scope)
        if previous is None:
            merged[factor.scope] = array("H", factor.values)
            continue
        if len(previous) != len(factor.values):
            raise AssertionError("same-scope factors have different table sizes")
        for index, value in enumerate(factor.values):
            previous[index] += value
    return [Factor(scope, values) for scope, values in sorted(merged.items())]


def _eliminate(variable: int, bucket: list[Factor], trace: bool):
    union = tuple(sorted({item for factor in bucket for item in factor.scope}))
    if variable not in union:
        raise AssertionError("elimination bucket lost its variable")
    output_scope = tuple(item for item in union if item != variable)
    output_size = POINTS ** len(output_scope)
    positions = {item: index for index, item in enumerate(output_scope)}
    factor_values = [factor.values for factor in bucket]
    variable_strides = []
    coefficients = []
    for factor in bucket:
        axis = factor.scope.index(variable)
        variable_strides.append(POINTS ** (len(factor.scope) - 1 - axis))
        row = []
        for item in output_scope:
            if item not in factor.scope:
                row.append(0)
            else:
                factor_axis = factor.scope.index(item)
                row.append(POINTS ** (len(factor.scope) - 1 - factor_axis))
        coefficients.append(row)
    del positions  # The sorted scopes above are the canonical axis map.

    result = array("H")
    argmins = array("B") if trace else None
    digits = [0] * len(output_scope)
    bases = [0] * len(bucket)
    for _ in range(output_size):
        best = 65535
        best_value = 0
        for value in range(POINTS):
            total = 0
            for factor_index, table in enumerate(factor_values):
                total += table[
                    bases[factor_index] + value * variable_strides[factor_index]
                ]
            if total < best:
                best = total
                best_value = value
        result.append(best)
        if argmins is not None:
            argmins.append(best_value)

        position = len(output_scope) - 1
        while position >= 0:
            digits[position] += 1
            for factor_index in range(len(bucket)):
                bases[factor_index] += coefficients[factor_index][position]
            if digits[position] < POINTS:
                break
            digits[position] = 0
            for factor_index in range(len(bucket)):
                bases[factor_index] -= (
                    POINTS * coefficients[factor_index][position]
                )
            position -= 1
    return Factor(output_scope, result), argmins


def solve_conditioned(
    initial_factors: list[Factor],
    order: tuple[int, ...],
    fixed: dict[int, int],
    trace: bool = False,
):
    factors = _merge_same_scope(
        [_restrict_factor(factor, fixed) for factor in initial_factors]
    )
    history = []
    peak_output = 0
    for variable in order:
        bucket = [factor for factor in factors if variable in factor.scope]
        factors = [factor for factor in factors if variable not in factor.scope]
        message, argmins = _eliminate(variable, bucket, trace)
        peak_output = max(peak_output, len(message.values))
        factors.append(message)
        factors = _merge_same_scope(factors)
        if trace:
            if argmins is None:
                raise AssertionError("trace elimination lost its argmins")
            history.append((variable, message.scope, argmins))
    if any(factor.scope for factor in factors):
        raise AssertionError("conditioned DP left a non-scalar factor")
    optimum = sum(factor.values[0] for factor in factors)
    return optimum, history, peak_output


def reconstruct_assignment(history, fixed):
    assignment = dict(fixed)
    for variable, scope, argmins in reversed(history):
        index = 0
        for item in scope:
            index = POINTS * index + assignment[item]
        assignment[variable] = argmins[index]
    if set(assignment) != set(range(140)):
        raise AssertionError("DP traceback left a point variable unassigned")
    result = tuple(assignment[index] for index in range(140))
    if result != EXPECTED_ASSIGNMENT:
        raise AssertionError("deterministic ordinary DP witness changed")
    if sha256(bytes(result)).hexdigest() != EXPECTED_ASSIGNMENT_SHA256:
        raise AssertionError("ordinary DP witness signature changed")
    return result


def replay_witness(assignment, records):
    violations = []
    cost = 0
    aggregate = Counter()
    for record_id, record in enumerate(records):
        if isinstance(record, PairRecord):
            satisfied = assignment[record.lower] == (
                assignment[record.upper] + record.delta
            ) % POINTS
            base_id = record.base_edge
        else:
            satisfied = assignment[record.node] == record.target
            base_id = 44 + record.terminal
        if not satisfied:
            violations.append(record_id)
            cost += record.weight
            aggregate[base_id] += record.weight
    expected_records = tuple(
        point_id
        for base_id in EXPECTED_BASE_VIOLATIONS[:-1]
        for point_id in range(POINTS * base_id, POINTS * base_id + POINTS)
    ) + tuple(range(220, 225))
    if tuple(violations) != expected_records or cost != EXPECTED_OPTIMUM:
        raise AssertionError("ordinary reduced witness cost changed")
    if tuple(sorted(aggregate)) != EXPECTED_BASE_VIOLATIONS:
        raise AssertionError("ordinary base violation support changed")
    return tuple(violations), tuple(sorted(aggregate.items())), cost


def verify_lifted_reassembly(graph, transports, fibers, assignment):
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
    if any(len(cells) != ORDINARY_BLOCKS for cells in node_cells):
        raise AssertionError("ordinary lifted cells violate all-different")
    if len(ordinary_labels) != ORDINARY_BLOCKS:
        raise AssertionError("ordinary lifted-label census changed")
    return tuple(ordinary_labels), tuple(frozenset(cells) for cells in node_cells)


def main() -> int:
    graph, node_id, edges = build_point_bundle()
    transports, inverses, tree_edges = canonical_gauge(edges)
    chord_count, shifts = verify_holonomy_and_retraction(
        edges, transports, inverses, tree_edges
    )
    fibers, pin_pattern = ordinary_pin_data(
        graph, node_id, transports, inverses
    )
    factors, records = build_reduced_factors(
        edges, transports, inverses, pin_pattern
    )
    order, degrees, union_entries = elimination_order(factors, graph)

    grid = []
    peak_output = 0
    for first in range(POINTS):
        for second in range(POINTS):
            optimum, _, peak = solve_conditioned(
                factors,
                order,
                {CONDITION_VARS[0]: first, CONDITION_VARS[1]: second},
            )
            grid.append(optimum)
            peak_output = max(peak_output, peak)
    if tuple(grid) != EXPECTED_GRID:
        raise AssertionError("ordinary condition grid changed")
    if sha256(bytes(grid)).hexdigest() != EXPECTED_GRID_SHA256:
        raise AssertionError("ordinary condition-grid signature changed")
    if min(grid) != EXPECTED_OPTIMUM or grid.index(EXPECTED_OPTIMUM) != 6:
        raise AssertionError("ordinary reduced optimum changed")

    optimum, history, traced_peak = solve_conditioned(
        factors,
        order,
        {CONDITION_VARS[0]: 1, CONDITION_VARS[1]: 1},
        trace=True,
    )
    if optimum != EXPECTED_OPTIMUM:
        raise AssertionError("ordinary traced optimum changed")
    assignment = reconstruct_assignment(
        history, {CONDITION_VARS[0]: 1, CONDITION_VARS[1]: 1}
    )
    violations, aggregate, witness_cost = replay_witness(assignment, records)
    verify_lifted_reassembly(graph, transports, fibers, assignment)

    if max(degrees) != 8 or peak_output != POINTS**8 or traced_peak != POINTS**8:
        raise AssertionError("ordinary DP peak table changed")
    print("H5 ORDINARY EXACT VERIFIER")
    print("  point bundle: vars=140 pairs=220 pins=60 chords=%d" % chord_count)
    print("  holonomy: shifts=%s orbits=625x5 retraction=PASS" % (shifts,))
    print("  ordinary fibers: count=624 missing=(0,) common-pins=PASS")
    print(
        "  DP: conditions=(50,4) cases=25 width=8 peak=%d entries/case=%d"
        % (peak_output, union_entries)
    )
    print("  condition minima: %s" % (tuple(grid),))
    print("  optimum: scaled=%d assignment=%s" % (optimum, EXPECTED_ASSIGNMENT_SHA256))
    print(
        "  witness: violations=%d base=%s cost=%d reassembly=PASS all-different=PASS"
        % (len(violations), aggregate, witness_cost)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
