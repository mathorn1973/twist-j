#!/usr/bin/env python3
"""Exact coupled optimum and conflict-core branch-and-bound for ``2..4``.

NON-CANONICAL LOCAL ANALYSIS.  The earlier anchor-to-anchor path packing gives
the scaled lower bound

``24 * 3125 * objective >= 624 * 40 + 60 = 25020``.

This module restores the all-different target-cell conditions at all sixteen
free nodes.  They turn out to be inactive at the optimum: a feasible coupled
family, obtained by changing only eight special-block permutations and no
cell assignments, attains the same value ``417/1250``.

The special block is also solved by an exact conflict-core deletion
branch-and-bound.  Its five source positions are fixed by every relevant
dyadic J-power, so the five point coordinates separate.  Each coordinate is a
16-variable functional-equality CSP with the same 20 pair constraints and 12
fixed anchor constraints.  The branch-and-bound proves exact scaled cost 12
per coordinate; the five witnesses reassemble into one common cell and an
``S_5`` permutation at every free node.

This closes only the named fixed-level-2 structured finite horizon.  It gives
no inverse-limit, entropy, measure, or Canon authority.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache

try:
    from .basins import family_signature
    from .bounds import (
        FIBER_SIZE,
        SPECIAL_BLOCK,
        BlockLabel,
        Node,
        _advance_label,
        _expected_half,
        _label_mismatches,
        _solver,
        constraint_graph,
    )
    from .growing import (
        BoundaryFamily,
        FiniteHorizonOptimizer,
        StructuredMap,
        default_collar,
        source_blocks,
    )
    from .path_bounds import (
        CAPACITY_SCALE,
        EDGE_COUNT,
        PathCertificate,
        _anchor_data,
        _forward_anchor,
        _reverse_anchor,
        _terminal_label,
        anchor_terminals,
        augmented_edge_weights,
        build_path_certificate,
        path_block_mismatches,
        path_edge_ids,
        verify_path_certificate,
    )
    from .collars import collar_graph
except ImportError:  # Direct execution from this directory.
    from basins import family_signature  # type: ignore[no-redef]
    from bounds import (  # type: ignore[no-redef]
        FIBER_SIZE,
        SPECIAL_BLOCK,
        BlockLabel,
        Node,
        _advance_label,
        _expected_half,
        _label_mismatches,
        _solver,
        constraint_graph,
    )
    from growing import (  # type: ignore[no-redef]
        BoundaryFamily,
        FiniteHorizonOptimizer,
        StructuredMap,
        default_collar,
        source_blocks,
    )
    from path_bounds import (  # type: ignore[no-redef]
        CAPACITY_SCALE,
        EDGE_COUNT,
        PathCertificate,
        _anchor_data,
        _forward_anchor,
        _reverse_anchor,
        _terminal_label,
        anchor_terminals,
        augmented_edge_weights,
        build_path_certificate,
        path_block_mismatches,
        path_edge_ids,
        verify_path_certificate,
    )
    from collars import collar_graph  # type: ignore[no-redef]


BLOCK_COUNT = 625
FREE_NODE_COUNT = 16
PAIR_CONSTRAINT_COUNT = 20
ANCHOR_CONSTRAINT_COUNT = 12
POINT_DOMAIN_SIZE = 3125
OBJECTIVE_SCALE = CAPACITY_SCALE * FIBER_SIZE
FULL_CONSTRAINT_MASK = (1 << EDGE_COUNT) - 1
EXPECTED_REMOVED_CONSTRAINTS = (0, 2, 8, 12, 14, 20, 23, 25)
EXPECTED_COORDINATE_CALLS = 22852
EXPECTED_COORDINATE_MASKS = 5126
BASELINE_FAMILY_SIGNATURES = (
    "c06fda5221cdcdd7859e9e3fc3ae648790b7c44d4adf18af5eaabd919b4eda02",
    "87267a244739791e9dc6ba6b5d5e4c09dda4d7964f4ee0a60e195025f3c66425",
    "d54117e0e4d1d40c5391d58e22f3da2e3f953aacf215278719a0a39a318aa452",
)
COUPLED_FAMILY_SIGNATURES = (
    "c06fda5221cdcdd7859e9e3fc3ae648790b7c44d4adf18af5eaabd919b4eda02",
    "96d4d0172d9205324cc8cbb02ec1636a5dbf71689fbdc46be9a9c9cee6c37209",
    "67d03d7a4b43dbe41a7f3d01de124a32128fb857b8f2a516f44c5d3c901fc887",
)


@dataclass(frozen=True, slots=True)
class PointConstraint:
    """One exact point-coordinate equality in the special-block CSP."""

    id: int
    weight: int
    upper: int | None
    lower: int | None
    forward: tuple[int, ...]
    reverse: tuple[int, ...]
    node: int | None
    target: int | None

    @property
    def is_pair(self) -> bool:
        return self.upper is not None


@dataclass(frozen=True, slots=True)
class CoordinateBnbResult:
    coordinate: int
    optimum: int
    active_mask: int
    removed_constraints: tuple[int, ...]
    assignment: tuple[int, ...]
    calls: int
    unique_masks: int


@dataclass(frozen=True, slots=True)
class PointBnbReport:
    results: tuple[CoordinateBnbResult, ...]
    total_optimum: int
    total_calls: int
    total_unique_masks: int


@dataclass(frozen=True, slots=True)
class CoupledBlockDualCertificate:
    """Zero-price lift of the blockwise path dual to the coupled problem.

    ``assignment_price`` is the compressed value of every assignment-dual
    multiplier ``lambda[v, block, cell]``.  At zero price, every free-node
    bijection has assignment minimum zero; the block minima are exactly those
    certified by the path packing.
    """

    assignment_price: Fraction
    node_assignment_minima: tuple[int, ...]
    block_minima: tuple[int, ...]
    scaled_value: int


@dataclass(frozen=True, slots=True)
class CoupledWitness:
    families: tuple[BoundaryFamily, ...]
    family_signatures: tuple[str, ...]
    per_block_scaled_costs: tuple[int, ...]
    first_transition: Fraction
    second_transition: Fraction
    objective: Fraction
    cell_changes: int
    ordinary_permutation_changes: int
    special_permutation_changes: int
    maximum_path_slack: int
    stability_changes: int


@dataclass(frozen=True, slots=True)
class ExactCoupledCertificate:
    minimum_level: int
    maximum_level: int
    seed: str
    lift_phase: int
    coupled_dual: CoupledBlockDualCertificate
    path_certificate: PathCertificate
    bnb: PointBnbReport
    witness: CoupledWitness
    scaled_lower_bound: int
    scaled_upper_bound: int
    optimum: Fraction
    root_nodes: int
    branched_nodes: int
    fathomed_by_bound: int


@dataclass(frozen=True, slots=True)
class _OracleResult:
    satisfiable: bool
    core: tuple[int, ...]
    assignment: tuple[int, ...]


def _scaled_weights() -> tuple[int, ...]:
    result = []
    for weight in augmented_edge_weights():
        scaled = weight * CAPACITY_SCALE
        if scaled.denominator != 1 or scaled <= 0:
            raise AssertionError("point-CSP edge weights did not scale to integers")
        result.append(scaled.numerator)
    if len(result) != EDGE_COUNT:
        raise AssertionError("point-CSP weight census changed")
    return tuple(result)


@lru_cache(maxsize=1)
def _base_families() -> tuple[BoundaryFamily, ...]:
    """Reconstruct the deterministic coordinate-local family being patched."""

    optimizer = FiniteHorizonOptimizer(
        2,
        4,
        solver=_solver(),
        seed="tree",
        lift_phase=1,
        freeze_minimum=True,
    )
    report = optimizer.optimize(20)
    if report.final_objective != Fraction(626, 1875):
        raise AssertionError("deterministic 2..4 baseline regression changed")
    families = tuple(optimizer.family(level) for level in range(2, 5))
    if tuple(family_signature(family) for family in families) != (
        BASELINE_FAMILY_SIGNATURES
    ):
        raise AssertionError("deterministic 2..4 baseline signatures changed")
    return families


def _encode_state(node: Node, cell: int, xi: int) -> int:
    if not 0 <= xi < 5:
        raise ValueError("point coordinate must lie in F_5")
    solver = _solver()
    half = _expected_half(node)
    try:
        local_cell = solver.model.cells_by_half[half].index(cell)
    except ValueError as exc:
        raise ValueError("point cell lies in the wrong living half") from exc
    return 5 * local_cell + xi


def _decode_state(node: Node, state: int) -> tuple[int, int]:
    if type(state) is not int or not 0 <= state < POINT_DOMAIN_SIZE:
        raise ValueError("encoded point state left the declared domain")
    local_cell, xi = divmod(state, 5)
    half = _expected_half(node)
    return _solver().model.cells_by_half[half][local_cell], xi


@lru_cache(maxsize=1)
def _pair_constraints() -> tuple[PointConstraint, ...]:
    solver = _solver()
    graph = constraint_graph(3, 4)
    node_id = {node: index for index, node in enumerate(graph.nodes)}
    weights = _scaled_weights()
    result = []
    for edge in graph.edges:
        upper_half = _expected_half(edge.upper)
        lower_half = _expected_half(edge.lower)
        upper_cells = solver.model.cells_by_half[upper_half]
        lower_cells = solver.model.cells_by_half[lower_half]
        lower_local = {cell: index for index, cell in enumerate(lower_cells)}
        forward = [-1] * POINT_DOMAIN_SIZE
        for upper_local, cell in enumerate(upper_cells):
            action = (
                solver.reduced.block_action(
                    edge.lower_level, edge.letter, cell
                )
                if edge.phase
                else None
            )
            for xi in range(5):
                source = 5 * upper_local + xi
                if edge.phase == 0:
                    target_cell = cell
                    target_xi = xi
                else:
                    if action is None:
                        raise AssertionError("phase-one edge lost its block action")
                    target_cell = action.target_cell
                    target_xi = action.apply_xi(xi)
                try:
                    target_local = lower_local[target_cell]
                except KeyError as exc:
                    raise AssertionError(
                        "point transport left the lower living half"
                    ) from exc
                forward[source] = 5 * target_local + target_xi
        if sorted(forward) != list(range(POINT_DOMAIN_SIZE)):
            raise AssertionError("point edge transport is not bijective")
        reverse = [-1] * POINT_DOMAIN_SIZE
        for source, target in enumerate(forward):
            reverse[target] = source
        result.append(
            PointConstraint(
                id=edge.id,
                weight=weights[edge.id],
                upper=node_id[edge.upper],
                lower=node_id[edge.lower],
                forward=tuple(forward),
                reverse=tuple(reverse),
                node=None,
                target=None,
            )
        )
    if len(result) != PAIR_CONSTRAINT_COUNT:
        raise AssertionError("point-CSP pair census changed")
    return tuple(result)


@lru_cache(maxsize=None)
def point_constraints(coordinate: int) -> tuple[PointConstraint, ...]:
    """Build the 20 pair and 12 unary constraints for one special coordinate."""

    if type(coordinate) is not int or not 0 <= coordinate < 5:
        raise ValueError("special coordinate must be an exact integer in 0..4")
    solver = _solver()
    special = solver._source_positions(3, source_blocks()[SPECIAL_BLOCK])
    if special != (0, 1, 2, 3, 4):
        raise AssertionError("special source block no longer separates by coordinate")
    graph = constraint_graph(3, 4)
    node_id = {node: index for index, node in enumerate(graph.nodes)}
    weights = _scaled_weights()
    result = list(_pair_constraints())
    for terminal in anchor_terminals():
        label = _reverse_anchor(
            terminal,
            SPECIAL_BLOCK,
            _terminal_label(terminal.id, SPECIAL_BLOCK),
        )
        constraint_id = PAIR_CONSTRAINT_COUNT + terminal.id
        result.append(
            PointConstraint(
                id=constraint_id,
                weight=weights[constraint_id],
                upper=None,
                lower=None,
                forward=(),
                reverse=(),
                node=node_id[terminal.parent],
                target=_encode_state(
                    terminal.parent, label.cell, label.permutation[coordinate]
                ),
            )
        )
    if tuple(item.id for item in result) != tuple(range(EDGE_COUNT)):
        raise AssertionError("point-CSP constraint ids are not canonical")
    return tuple(result)


def _tree_path_edges(
    node: int,
    parent_node: dict[int, int | None],
    parent_edge: dict[int, int],
) -> tuple[int, ...]:
    result = []
    while True:
        parent = parent_node[node]
        if parent is None:
            break
        result.append(parent_edge[node])
        node = parent
    return tuple(result)


def _constraint_satisfaction(
    coordinate: int, active_mask: int
) -> _OracleResult:
    """Return SAT assignment or one replayable inconsistent active core."""

    if type(active_mask) is not int or not 0 <= active_mask <= FULL_CONSTRAINT_MASK:
        raise ValueError("active constraint mask left the 32-bit scope")
    constraints = point_constraints(coordinate)
    adjacency: list[list[tuple[int, int, bool]]] = [
        [] for _ in range(FREE_NODE_COUNT)
    ]
    pins: list[list[tuple[int, int]]] = [[] for _ in range(FREE_NODE_COUNT)]
    for constraint in constraints:
        if not active_mask & (1 << constraint.id):
            continue
        if constraint.is_pair:
            upper = constraint.upper
            lower = constraint.lower
            if upper is None or lower is None:
                raise AssertionError("pair constraint lost an endpoint")
            adjacency[upper].append((constraint.id, lower, True))
            adjacency[lower].append((constraint.id, upper, False))
        else:
            if constraint.node is None or constraint.target is None:
                raise AssertionError("unary constraint lost its fixed target")
            pins[constraint.node].append((constraint.id, constraint.target))
    for row in adjacency:
        row.sort()
    for row in pins:
        row.sort()

    unseen = set(range(FREE_NODE_COUNT))
    full_assignment = [-1] * FREE_NODE_COUNT
    while unseen:
        component_root = min(unseen)
        component = {component_root}
        queue = deque((component_root,))
        while queue:
            node = queue.popleft()
            for _, neighbor, _ in adjacency[node]:
                if neighbor not in component:
                    component.add(neighbor)
                    queue.append(neighbor)
        unseen.difference_update(component)
        component_pins = sorted(
            pin for node in component for pin in pins[node]
        )

        def propagate(
            root_node: int, root_state: int, root_pin: int | None
        ) -> tuple[bool, tuple[int, ...], dict[int, int]]:
            values = {root_node: root_state}
            parent_node: dict[int, int | None] = {root_node: None}
            parent_edge: dict[int, int] = {}
            work = deque((root_node,))
            while work:
                node = work.popleft()
                for pin_id, target in pins[node]:
                    if values[node] != target:
                        core = set(_tree_path_edges(node, parent_node, parent_edge))
                        core.add(pin_id)
                        if root_pin is not None:
                            core.add(root_pin)
                        return False, tuple(sorted(core)), values
                for edge_id, neighbor, forward_direction in adjacency[node]:
                    constraint = constraints[edge_id]
                    predicted = (
                        constraint.forward[values[node]]
                        if forward_direction
                        else constraint.reverse[values[node]]
                    )
                    if neighbor not in values:
                        values[neighbor] = predicted
                        parent_node[neighbor] = node
                        parent_edge[neighbor] = edge_id
                        work.append(neighbor)
                    elif values[neighbor] != predicted:
                        core = set(
                            _tree_path_edges(node, parent_node, parent_edge)
                        )
                        core.update(
                            _tree_path_edges(neighbor, parent_node, parent_edge)
                        )
                        core.add(edge_id)
                        if root_pin is not None:
                            core.add(root_pin)
                        return False, tuple(sorted(core)), values
            return True, (), values

        if component_pins:
            root_pin, root_state = component_pins[0]
            root_node = constraints[root_pin].node
            if root_node is None:
                raise AssertionError("chosen root pin is not unary")
            sat, core, values = propagate(root_node, root_state, root_pin)
            if not sat:
                if not core or any(
                    not active_mask & (1 << edge_id) for edge_id in core
                ):
                    raise AssertionError("conflict oracle returned an inactive core")
                return _OracleResult(False, core, ())
        else:
            sat = False
            values: dict[int, int] = {}
            for root_state in range(POINT_DOMAIN_SIZE):
                candidate, _, candidate_values = propagate(
                    component_root, root_state, None
                )
                if candidate:
                    sat = True
                    values = candidate_values
                    break
            if not sat:
                core = tuple(
                    constraint.id
                    for constraint in constraints[:PAIR_CONSTRAINT_COUNT]
                    if active_mask & (1 << constraint.id)
                    and constraint.upper in component
                )
                if not core:
                    raise AssertionError("unanchored conflict has no active pair core")
                return _OracleResult(False, core, ())
        for node, value in values.items():
            full_assignment[node] = value

    if any(value < 0 for value in full_assignment):
        raise AssertionError("conflict oracle left a free node unassigned")
    assignment = tuple(full_assignment)
    for constraint in constraints:
        if not active_mask & (1 << constraint.id):
            continue
        if constraint.is_pair:
            upper = constraint.upper
            lower = constraint.lower
            if upper is None or lower is None:
                raise AssertionError("pair replay lost an endpoint")
            if assignment[lower] != constraint.forward[assignment[upper]]:
                raise AssertionError("SAT oracle returned a violated active pair")
        else:
            if constraint.node is None or constraint.target is None:
                raise AssertionError("unary replay lost its target")
            if assignment[constraint.node] != constraint.target:
                raise AssertionError("SAT oracle returned a violated active pin")
    return _OracleResult(True, (), assignment)


@lru_cache(maxsize=5)
def _solve_coordinate(coordinate: int) -> CoordinateBnbResult:
    constraints = point_constraints(coordinate)
    weights = tuple(constraint.weight for constraint in constraints)
    seed_removed = EXPECTED_REMOVED_CONSTRAINTS + (21,)
    seed_mask = FULL_CONSTRAINT_MASK ^ sum(1 << item for item in seed_removed)
    seed_cost = sum(weights[item] for item in seed_removed)
    seed = _constraint_satisfaction(coordinate, seed_mask)
    if not seed.satisfiable or seed_cost != 14:
        raise AssertionError("point B&B lost its verified feasible incumbent")
    best = seed_cost
    best_mask: int | None = seed_mask
    best_assignment: tuple[int, ...] | None = seed.assignment
    calls = 0
    seen: set[int] = set()

    def search(mask: int, cost: int) -> None:
        nonlocal best, best_mask, best_assignment, calls
        calls += 1
        if cost >= best or mask in seen:
            return
        seen.add(mask)
        result = _constraint_satisfaction(coordinate, mask)
        if result.satisfiable:
            best = cost
            best_mask = mask
            best_assignment = result.assignment
            return
        for constraint_id in sorted(
            result.core, key=lambda item: (weights[item], item)
        ):
            search(
                mask & ~(1 << constraint_id),
                cost + weights[constraint_id],
            )

    search(FULL_CONSTRAINT_MASK, 0)
    if best_mask is None or best_assignment is None:
        raise AssertionError("coordinate branch-and-bound found no feasible deletion")
    removed = tuple(
        constraint_id
        for constraint_id in range(EDGE_COUNT)
        if not best_mask & (1 << constraint_id)
    )
    if sum(weights[item] for item in removed) != best:
        raise AssertionError("coordinate deletion cost does not match its mask")
    actual_violations = []
    for constraint in constraints:
        if constraint.is_pair:
            upper = constraint.upper
            lower = constraint.lower
            if upper is None or lower is None:
                raise AssertionError("pair violation replay lost an endpoint")
            satisfied = (
                best_assignment[lower]
                == constraint.forward[best_assignment[upper]]
            )
        else:
            if constraint.node is None or constraint.target is None:
                raise AssertionError("unary violation replay lost its target")
            satisfied = best_assignment[constraint.node] == constraint.target
        if not satisfied:
            actual_violations.append(constraint.id)
    if tuple(actual_violations) != removed:
        raise AssertionError("optimal deletion mask contains a redundant constraint")
    return CoordinateBnbResult(
        coordinate=coordinate,
        optimum=best,
        active_mask=best_mask,
        removed_constraints=removed,
        assignment=best_assignment,
        calls=calls,
        unique_masks=len(seen),
    )


@lru_cache(maxsize=1)
def build_point_bnb_report() -> PointBnbReport:
    results = tuple(_solve_coordinate(coordinate) for coordinate in range(5))
    report = PointBnbReport(
        results=results,
        total_optimum=sum(item.optimum for item in results),
        total_calls=sum(item.calls for item in results),
        total_unique_masks=sum(item.unique_masks for item in results),
    )
    if not verify_point_bnb_report(report):
        raise AssertionError("new point-coordinate B&B report failed replay")
    return report


def verify_point_bnb_report(report: PointBnbReport) -> bool:
    if (
        type(report) is not PointBnbReport
        or type(report.results) is not tuple
        or type(report.total_optimum) is not int
        or type(report.total_calls) is not int
        or type(report.total_unique_masks) is not int
        or len(report.results) != 5
    ):
        return False
    for coordinate, result in enumerate(report.results):
        if (
            type(result) is not CoordinateBnbResult
            or type(result.coordinate) is not int
            or type(result.optimum) is not int
            or type(result.active_mask) is not int
            or type(result.removed_constraints) is not tuple
            or any(type(item) is not int for item in result.removed_constraints)
            or type(result.assignment) is not tuple
            or len(result.assignment) != FREE_NODE_COUNT
            or any(type(item) is not int for item in result.assignment)
            or type(result.calls) is not int
            or type(result.unique_masks) is not int
            or result.coordinate != coordinate
            or result.optimum != 12
            or result.removed_constraints != EXPECTED_REMOVED_CONSTRAINTS
            or result.active_mask
            != (
                FULL_CONSTRAINT_MASK
                ^ sum(1 << item for item in EXPECTED_REMOVED_CONSTRAINTS)
            )
            or result.calls != EXPECTED_COORDINATE_CALLS
            or result.unique_masks != EXPECTED_COORDINATE_MASKS
        ):
            return False
        try:
            replay = _constraint_satisfaction(coordinate, result.active_mask)
        except (AssertionError, IndexError, KeyError, TypeError, ValueError):
            return False
        if (
            not replay.satisfiable
            or replay.assignment != result.assignment
            or result != _solve_coordinate(coordinate)
        ):
            return False
    return (
        report.total_optimum == sum(item.optimum for item in report.results) == 60
        and report.total_calls
        == sum(item.calls for item in report.results)
        == 5 * EXPECTED_COORDINATE_CALLS
        and report.total_unique_masks
        == sum(item.unique_masks for item in report.results)
        == 5 * EXPECTED_COORDINATE_MASKS
    )


def _labels_from_bnb(report: PointBnbReport) -> tuple[BlockLabel, ...]:
    if not verify_point_bnb_report(report):
        raise ValueError("cannot reconstruct labels from an invalid B&B report")
    graph = constraint_graph(3, 4)
    labels = []
    for node_id, node in enumerate(graph.nodes):
        decoded = tuple(
            _decode_state(node, result.assignment[node_id])
            for result in report.results
        )
        cells = {cell for cell, _ in decoded}
        permutation = tuple(xi for _, xi in decoded)
        if len(cells) != 1 or set(permutation) != set(range(5)):
            raise AssertionError("coordinate witnesses do not reassemble to one label")
        labels.append(BlockLabel(next(iter(cells)), permutation))
    return tuple(labels)


def _replace_special(mapping: StructuredMap, label: BlockLabel) -> StructuredMap:
    if mapping.cells[SPECIAL_BLOCK] != label.cell:
        raise AssertionError("coupled patch attempted to change a target cell")
    permutations = list(mapping.permutations)
    permutations[SPECIAL_BLOCK] = label.permutation
    return StructuredMap(mapping.half, mapping.cells, tuple(permutations))


@lru_cache(maxsize=1)
def _patched_families() -> tuple[BoundaryFamily, ...]:
    base = _base_families()
    labels = _labels_from_bnb(build_point_bnb_report())
    graph = constraint_graph(3, 4)
    by_node = {node: label for node, label in zip(graph.nodes, labels)}
    result = [base[0]]
    for family in base[1:]:
        words = collar_graph(family.spec).vertices
        maps = tuple(
            _replace_special(mapping, by_node[(family.level, word)])
            for word, mapping in zip(words, family.maps)
        )
        result.append(
            BoundaryFamily(
                level=family.level,
                spec=family.spec,
                maps=maps,
                origin="exact-coupled-block-bnb",
            )
        )
    families = tuple(result)
    if tuple(family_signature(family) for family in families) != (
        COUPLED_FAMILY_SIGNATURES
    ):
        raise AssertionError("exact coupled witness signatures changed")
    return families


def _maps_by_node(families: tuple[BoundaryFamily, ...]) -> dict[Node, StructuredMap]:
    result: dict[Node, StructuredMap] = {}
    for family in families[1:]:
        for word, mapping in zip(collar_graph(family.spec).vertices, family.maps):
            result[(family.level, word)] = mapping
    return result


def _edge_mismatch_from_maps(
    maps: dict[Node, StructuredMap], block_id: int, edge_id: int
) -> int:
    if edge_id < PAIR_CONSTRAINT_COUNT:
        edge = constraint_graph(3, 4).edges[edge_id]
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
    terminal = anchor_terminals()[edge_id - PAIR_CONSTRAINT_COUNT]
    upper = maps[terminal.parent]
    label = _forward_anchor(
        terminal,
        block_id,
        BlockLabel(upper.cells[block_id], upper.permutations[block_id]),
    )
    terminal_map = _anchor_data()[1][terminal.id]
    return _label_mismatches(
        label,
        BlockLabel(
            terminal_map.cells[block_id],
            terminal_map.permutations[block_id],
        ),
    )


def _edge_mismatch(
    families: tuple[BoundaryFamily, ...], block_id: int, edge_id: int
) -> int:
    return _edge_mismatch_from_maps(
        _maps_by_node(families), block_id, edge_id
    )


def per_block_scaled_costs(
    families: tuple[BoundaryFamily, ...]
) -> tuple[int, ...]:
    weights = _scaled_weights()
    maps = _maps_by_node(families)
    return tuple(
        sum(
            weights[edge_id]
            * _edge_mismatch_from_maps(maps, block_id, edge_id)
            for edge_id in range(EDGE_COUNT)
        )
        for block_id in range(BLOCK_COUNT)
    )


def _path_scaled_lower_by_block(
    certificate: PathCertificate,
) -> tuple[int, ...]:
    result = [Fraction(0) for _ in range(BLOCK_COUNT)]
    for path in certificate.paths:
        mismatches = path_block_mismatches(path.path)
        for block_id in path.block_ids:
            result[block_id] += (
                CAPACITY_SCALE * path.allocation * mismatches[block_id]
            )
    if any(value.denominator != 1 for value in result):
        raise AssertionError("path dual did not have integral scaled block values")
    return tuple(value.numerator for value in result)


def build_coupled_block_dual(
    path_certificate: PathCertificate | None = None,
) -> CoupledBlockDualCertificate:
    """Lift the exact block relaxation bound with an all-zero price tensor."""

    path = build_path_certificate() if path_certificate is None else path_certificate
    if not verify_path_certificate(path):
        raise ValueError("cannot lift an invalid path certificate")
    block_minima = _path_scaled_lower_by_block(path)
    certificate = CoupledBlockDualCertificate(
        assignment_price=Fraction(0),
        node_assignment_minima=(0,) * FREE_NODE_COUNT,
        block_minima=block_minima,
        scaled_value=sum(block_minima),
    )
    if not verify_coupled_block_dual(certificate, path):
        raise AssertionError("new coupled block dual failed exact replay")
    return certificate


def verify_coupled_block_dual(
    certificate: CoupledBlockDualCertificate,
    path_certificate: PathCertificate,
) -> bool:
    """Replay the zero-price assignment minima and the path block minima."""

    if (
        type(certificate) is not CoupledBlockDualCertificate
        or type(certificate.assignment_price) is not Fraction
        or type(certificate.node_assignment_minima) is not tuple
        or any(
            type(value) is not int
            for value in certificate.node_assignment_minima
        )
        or type(certificate.block_minima) is not tuple
        or any(type(value) is not int for value in certificate.block_minima)
        or type(certificate.scaled_value) is not int
        or type(path_certificate) is not PathCertificate
        or len(certificate.node_assignment_minima) != FREE_NODE_COUNT
        or len(certificate.block_minima) != BLOCK_COUNT
        or not verify_path_certificate(path_certificate)
    ):
        return False
    try:
        expected_blocks = _path_scaled_lower_by_block(path_certificate)
    except (AssertionError, IndexError, TypeError, ValueError):
        return False
    return (
        certificate.assignment_price == 0
        and certificate.node_assignment_minima == (0,) * FREE_NODE_COUNT
        and certificate.block_minima == expected_blocks
        and Counter(certificate.block_minima) == Counter({40: 624, 60: 1})
        and certificate.scaled_value
        == sum(certificate.node_assignment_minima)
        + sum(certificate.block_minima)
        == 25020
    )


def _path_slack_maximum(
    families: tuple[BoundaryFamily, ...], certificate: PathCertificate
) -> int:
    maximum = 0
    maps = _maps_by_node(families)
    for path in certificate.paths:
        defects = path_block_mismatches(path.path)
        edges = path_edge_ids(path.path)
        for block_id in path.block_ids:
            slack = sum(
                _edge_mismatch_from_maps(maps, block_id, edge_id)
                for edge_id in edges
            ) - defects[block_id]
            if slack < 0:
                raise AssertionError("path triangle inequality became negative")
            maximum = max(maximum, slack)
    return maximum


@lru_cache(maxsize=1)
def build_coupled_witness() -> CoupledWitness:
    solver = _solver()
    base = _base_families()
    families = _patched_families()
    if any(not solver.validate_family(family) for family in families):
        raise AssertionError("patched coupled family is not structured-bijective")
    reports = (
        solver.refinement_report(families[1], families[0]),
        solver.refinement_report(families[2], families[1]),
    )
    costs = per_block_scaled_costs(families)

    cell_changes = 0
    ordinary_changes = 0
    special_changes = 0
    for old_family, new_family in zip(base, families):
        for old, new in zip(old_family.maps, new_family.maps):
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
        4,
        solver=solver,
        seed="tree",
        lift_phase=1,
        freeze_minimum=True,
    )
    optimizer.maps = {
        family.level: list(family.maps) for family in families
    }
    stability = optimizer.optimize(1).sweeps[0].changed_nodes

    witness = CoupledWitness(
        families=families,
        family_signatures=tuple(family_signature(family) for family in families),
        per_block_scaled_costs=costs,
        first_transition=reports[0].distance,
        second_transition=reports[1].distance,
        objective=reports[0].distance + reports[1].distance,
        cell_changes=cell_changes,
        ordinary_permutation_changes=ordinary_changes,
        special_permutation_changes=special_changes,
        maximum_path_slack=_path_slack_maximum(
            families, build_path_certificate()
        ),
        stability_changes=stability,
    )
    if not verify_coupled_witness(witness, build_point_bnb_report()):
        raise AssertionError("new coupled witness failed exact replay")
    return witness


def verify_coupled_witness(
    witness: CoupledWitness, bnb: PointBnbReport
) -> bool:
    if (
        type(witness) is not CoupledWitness
        or type(witness.families) is not tuple
        or type(witness.family_signatures) is not tuple
        or type(witness.per_block_scaled_costs) is not tuple
        or any(type(value) is not int for value in witness.per_block_scaled_costs)
        or any(
            type(value) is not Fraction
            for value in (
                witness.first_transition,
                witness.second_transition,
                witness.objective,
            )
        )
        or type(witness.cell_changes) is not int
        or type(witness.ordinary_permutation_changes) is not int
        or type(witness.special_permutation_changes) is not int
        or type(witness.maximum_path_slack) is not int
        or type(witness.stability_changes) is not int
        or len(witness.families) != 3
        or len(witness.family_signatures) != 3
        or len(witness.per_block_scaled_costs) != BLOCK_COUNT
        or not verify_point_bnb_report(bnb)
    ):
        return False
    try:
        solver = _solver()
        if any(not solver.validate_family(family) for family in witness.families):
            return False
        tree = solver.tree_family(2, default_collar(2))
        if (
            witness.families[0].level != tree.level
            or witness.families[0].spec != tree.spec
            or witness.families[0].maps != tree.maps
        ):
            return False
        if witness.family_signatures != tuple(
            family_signature(family) for family in witness.families
        ):
            return False
        if witness.families != _patched_families():
            return False
        costs = per_block_scaled_costs(witness.families)
        reports = (
            solver.refinement_report(witness.families[1], witness.families[0]),
            solver.refinement_report(witness.families[2], witness.families[1]),
        )
        slack = _path_slack_maximum(
            witness.families, build_path_certificate()
        )
        special_mismatches = tuple(
            _edge_mismatch(witness.families, SPECIAL_BLOCK, edge_id)
            for edge_id in range(EDGE_COUNT)
        )
    except (AssertionError, IndexError, KeyError, TypeError, ValueError):
        return False
    return (
        witness.per_block_scaled_costs == costs
        and Counter(costs) == Counter({40: 624, 60: 1})
        and sum(costs) == 25020
        and witness.first_transition == reports[0].distance == Fraction(209, 2500)
        and witness.second_transition == reports[1].distance == Fraction(1, 4)
        and witness.objective
        == reports[0].distance + reports[1].distance
        == Fraction(417, 1250)
        and witness.cell_changes == 0
        and witness.ordinary_permutation_changes == 0
        and witness.special_permutation_changes == 8
        and witness.maximum_path_slack == slack == 0
        and witness.stability_changes == 0
        and tuple(
            edge_id
            for edge_id, mismatches in enumerate(special_mismatches)
            if mismatches
        )
        == EXPECTED_REMOVED_CONSTRAINTS
        and all(
            special_mismatches[edge_id] == 5
            for edge_id in EXPECTED_REMOVED_CONSTRAINTS
        )
    )


@lru_cache(maxsize=1)
def build_exact_coupled_certificate() -> ExactCoupledCertificate:
    path = build_path_certificate()
    dual = build_coupled_block_dual(path)
    bnb = build_point_bnb_report()
    witness = build_coupled_witness()
    certificate = ExactCoupledCertificate(
        minimum_level=2,
        maximum_level=4,
        seed="tree",
        lift_phase=1,
        coupled_dual=dual,
        path_certificate=path,
        bnb=bnb,
        witness=witness,
        scaled_lower_bound=dual.scaled_value,
        scaled_upper_bound=sum(witness.per_block_scaled_costs),
        optimum=witness.objective,
        root_nodes=1,
        branched_nodes=0,
        fathomed_by_bound=1,
    )
    if not verify_exact_coupled_certificate(certificate):
        raise AssertionError("new exact coupled certificate failed replay")
    return certificate


def verify_exact_coupled_certificate(
    certificate: ExactCoupledCertificate,
) -> bool:
    if (
        type(certificate) is not ExactCoupledCertificate
        or type(certificate.minimum_level) is not int
        or type(certificate.maximum_level) is not int
        or type(certificate.seed) is not str
        or type(certificate.lift_phase) is not int
        or type(certificate.coupled_dual) is not CoupledBlockDualCertificate
        or type(certificate.path_certificate) is not PathCertificate
        or type(certificate.bnb) is not PointBnbReport
        or type(certificate.witness) is not CoupledWitness
        or type(certificate.scaled_lower_bound) is not int
        or type(certificate.scaled_upper_bound) is not int
        or type(certificate.optimum) is not Fraction
        or type(certificate.root_nodes) is not int
        or type(certificate.branched_nodes) is not int
        or type(certificate.fathomed_by_bound) is not int
        or certificate.minimum_level != 2
        or certificate.maximum_level != 4
        or certificate.seed != "tree"
        or certificate.lift_phase != 1
    ):
        return False
    if not verify_path_certificate(certificate.path_certificate):
        return False
    if not verify_coupled_block_dual(
        certificate.coupled_dual, certificate.path_certificate
    ):
        return False
    if not verify_point_bnb_report(certificate.bnb):
        return False
    if not verify_coupled_witness(certificate.witness, certificate.bnb):
        return False
    block_lower = _path_scaled_lower_by_block(certificate.path_certificate)
    return (
        Counter(block_lower) == Counter({40: 624, 60: 1})
        and certificate.coupled_dual.block_minima == block_lower
        and certificate.coupled_dual.assignment_price == 0
        and certificate.bnb.total_optimum == 60
        and certificate.scaled_lower_bound == sum(block_lower) == 25020
        and certificate.scaled_upper_bound
        == sum(certificate.witness.per_block_scaled_costs)
        == 25020
        and certificate.optimum
        == Fraction(certificate.scaled_lower_bound, OBJECTIVE_SCALE)
        == certificate.witness.objective
        == Fraction(417, 1250)
        and certificate.root_nodes == 1
        and certificate.branched_nodes == 0
        and certificate.fathomed_by_bound == 1
    )


def format_exact_report(certificate: ExactCoupledCertificate) -> str:
    histogram = Counter(certificate.witness.per_block_scaled_costs)
    removed = certificate.bnb.results[0].removed_constraints
    return "\n".join(
        (
            "anchored structured horizon=2..4 exact coupled optimum",
            "  scaled lower=upper=%d objective=%s"
            % (certificate.scaled_lower_bound, certificate.optimum),
            "  zero assignment multiplier=%s per-block costs=%s"
            % (
                certificate.coupled_dual.assignment_price,
                dict(sorted(histogram.items())),
            ),
            "  point B&B coordinates=5 optimum=%d removed=%s calls=%d masks=%d"
            % (
                certificate.bnb.total_optimum,
                removed,
                certificate.bnb.total_calls,
                certificate.bnb.total_unique_masks,
            ),
            "  patch: cells=%d ordinary-perms=%d special-perms=%d path-slack=%d"
            % (
                certificate.witness.cell_changes,
                certificate.witness.ordinary_permutation_changes,
                certificate.witness.special_permutation_changes,
                certificate.witness.maximum_path_slack,
            ),
            "  root B&B nodes=%d branched=%d fathomed-by-bound=%d"
            % (
                certificate.root_nodes,
                certificate.branched_nodes,
                certificate.fathomed_by_bound,
            ),
            "  scope: fixed-r2 structured 625-block/S5 horizon only",
        )
    )


def main() -> int:
    print("ENTROPY-SELECTION exact coupled 2..4 certificate")
    print("NON-CANONICAL / NON-FORMAL / NO CLAIM STATUS")
    print(format_exact_report(build_exact_coupled_certificate()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "CoordinateBnbResult",
    "CoupledBlockDualCertificate",
    "CoupledWitness",
    "ExactCoupledCertificate",
    "PointBnbReport",
    "PointConstraint",
    "build_coupled_block_dual",
    "build_coupled_witness",
    "build_exact_coupled_certificate",
    "build_point_bnb_report",
    "format_exact_report",
    "per_block_scaled_costs",
    "point_constraints",
    "verify_coupled_witness",
    "verify_coupled_block_dual",
    "verify_exact_coupled_certificate",
    "verify_point_bnb_report",
]
