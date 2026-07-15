#!/usr/bin/env python3
"""Certified lower bounds for bounded growing-context objectives.

NON-CANONICAL LOCAL ANALYSIS.  The bound in this module is deliberately a
relaxation of the structured 625-block/S_5 finite-horizon problem.  It has two
disjoint parts:

* the exact minimum of the first adjacent distance with the declared level-2
  boundary family frozen;
* holonomy-cycle bounds on all later adjacent distances after dropping the
  all-different coupling between source blocks.  Horizon ``2..4`` uses a
  replayable fractional packing of every positive-defect simple cycle;
  horizon ``2..5`` keeps the smaller edge-disjoint fundamental-cycle
  certificate.

For one source block, every refinement edge is an isometry of the label space
``(target cell, S_5 permutation)``.  Around a cycle, the weighted triangle
inequality gives

``sum_e w_e d_e >= min_e(w_e) d(x, H(x))``.

The right side is minimized exhaustively over all ``625 * 120`` block labels.
The 624 ordinary J-five-sectors have the same source-position action and are
therefore represented by one exhaustive calculation; the residual
``J^(2^r)``-fixed block is checked separately.  Cycle inequalities may be
added fractionally while their total load on each objective edge stays below
that edge's exact weight.  Different source blocks may be added because they
are disjoint coordinates of the 3125-point Hamming distance.

The resulting number is a rigorous lower bound only for the named anchored
finite horizon and structured ansatz.  It is not a global optimum certificate,
an entropy obstruction, or a statement about arbitrary measurable transfers.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache

try:
    from .block_solver import five_permutations
    from .collars import collar_graph, refinement_incidence
    from .growing import (
        FiniteHorizonOptimizer,
        GrowingContextSolver,
        default_collar,
        source_blocks,
    )
    from .morse import last_symbol
except ImportError:  # Direct execution from this directory.
    from block_solver import five_permutations  # type: ignore[no-redef]
    from collars import (  # type: ignore[no-redef]
        collar_graph,
        refinement_incidence,
    )
    from growing import (  # type: ignore[no-redef]
        FiniteHorizonOptimizer,
        GrowingContextSolver,
        default_collar,
        source_blocks,
    )
    from morse import last_symbol  # type: ignore[no-redef]


MODULUS = 5
FIBER_SIZE = 3125
ORDINARY_BLOCKS = 624
SPECIAL_BLOCK = 624
Permutation5 = tuple[int, int, int, int, int]
Node = tuple[int, tuple[int, ...]]


@dataclass(frozen=True, order=True, slots=True)
class BlockLabel:
    """One relaxed source-block label at a boundary node."""

    cell: int
    permutation: Permutation5


@dataclass(frozen=True, slots=True)
class ConstraintEdge:
    """One weighted adjacent-level equality term.

    The stored orientation is always ``upper -> lower``.  Phase zero transports
    a label identically; phase one transports it by the exact block advance.
    """

    id: int
    upper: Node
    lower: Node
    lower_level: int
    phase: int
    letter: int
    weight: Fraction


@dataclass(frozen=True, slots=True)
class ConstraintGraph:
    minimum_level: int
    maximum_level: int
    nodes: tuple[Node, ...]
    edges: tuple[ConstraintEdge, ...]


@dataclass(frozen=True, slots=True)
class CycleStep:
    edge: int
    forward: bool


@dataclass(frozen=True, order=True, slots=True)
class CycleWitness:
    cell: int
    permutation: Permutation5


@dataclass(frozen=True, slots=True)
class CycleCertificate:
    basis_index: int
    steps: tuple[CycleStep, ...]
    minimum_edge_weight: Fraction
    ordinary_minimum_mismatches: int
    special_minimum_mismatches: int
    ordinary_witness: CycleWitness
    special_witness: CycleWitness
    contribution: Fraction


@dataclass(frozen=True, slots=True)
class FractionalCycleCertificate:
    """One explicitly weighted simple-cycle term in a fractional packing."""

    cycle_index: int
    steps: tuple[CycleStep, ...]
    allocation: Fraction
    ordinary_minimum_mismatches: int
    special_minimum_mismatches: int
    ordinary_witness: CycleWitness
    special_witness: CycleWitness
    contribution: Fraction


@dataclass(frozen=True, slots=True)
class AnchorTerm:
    parent: tuple[int, ...]
    extension: tuple[int, ...]
    branch_weight: Fraction
    desired_map_distance: Fraction
    contribution: Fraction


@dataclass(frozen=True, slots=True)
class BoundCertificate:
    """Fully replayable certificate for one anchored lower bound."""

    minimum_level: int
    maximum_level: int
    seed: str
    anchor_terms: tuple[AnchorTerm, ...]
    anchor_bound: Fraction
    cycles: tuple[CycleCertificate, ...]
    fractional_cycles: tuple[FractionalCycleCertificate, ...]
    cycle_bound: Fraction
    lower_bound: Fraction


@dataclass(frozen=True, slots=True)
class BoundReport:
    certificate: BoundCertificate
    incumbent: Fraction
    gap: Fraction
    meets_incumbent: bool
    incumbent_seed: str
    incumbent_lift_phase: int


@lru_cache(maxsize=1)
def _solver() -> GrowingContextSolver:
    return GrowingContextSolver()


def _expected_half(node: Node) -> int:
    level, word = node
    spec = default_collar(level)
    return last_symbol(word[spec.left - 1], level)


@lru_cache(maxsize=None)
def constraint_graph(minimum_level: int, maximum_level: int) -> ConstraintGraph:
    """Build the later-edge graph used by the cycle relaxation.

    ``minimum_level`` is normally three: transition 2 -> 3 is reserved for the
    exact anchored term, so the returned edges start with transition 3 -> 4.
    """

    if minimum_level < 2 or maximum_level <= minimum_level:
        raise ValueError("cycle graph needs at least two adjacent levels")
    nodes = tuple(
        (level, word)
        for level in range(minimum_level, maximum_level + 1)
        for word in collar_graph(default_collar(level)).vertices
    )
    edges: list[ConstraintEdge] = []
    for lower_level in range(minimum_level, maximum_level):
        upper_level = lower_level + 1
        upper_spec = default_collar(upper_level)
        lower_spec = default_collar(lower_level)
        for atom in refinement_incidence(upper_spec, lower_spec).atoms:
            upper = (upper_level, atom.parent)
            letter = atom.parent[upper_spec.left]
            edges.append(
                ConstraintEdge(
                    id=len(edges),
                    upper=upper,
                    lower=(lower_level, atom.child0),
                    lower_level=lower_level,
                    phase=0,
                    letter=letter,
                    weight=atom.branch_weight,
                )
            )
            edges.append(
                ConstraintEdge(
                    id=len(edges),
                    upper=upper,
                    lower=(lower_level, atom.child1),
                    lower_level=lower_level,
                    phase=1,
                    letter=letter,
                    weight=atom.branch_weight,
                )
            )
    result = ConstraintGraph(minimum_level, maximum_level, nodes, tuple(edges))
    node_set = set(nodes)
    if any(edge.upper not in node_set or edge.lower not in node_set for edge in edges):
        raise AssertionError("constraint edge left the declared horizon")
    return result


def _advance_label(
    block_id: int,
    label: BlockLabel,
    level: int,
    letter: int,
) -> BlockLabel:
    solver = _solver()
    block = source_blocks()[block_id]
    action = solver.reduced.block_action(level, letter, label.cell)
    positions = solver._source_positions(level, block)
    target = [-1] * MODULUS
    for old_position, new_position in enumerate(positions):
        target[new_position] = action.apply_xi(label.permutation[old_position])
    return BlockLabel(action.target_cell, tuple(target))  # type: ignore[arg-type]


def _retreat_label(
    block_id: int,
    label: BlockLabel,
    level: int,
    letter: int,
    source_half: int,
) -> BlockLabel:
    solver = _solver()
    block = source_blocks()[block_id]
    inverse = solver._inverse_cells(level, letter, source_half)
    source_cell, inverse_multiplier, offset = inverse[label.cell]
    positions = solver._source_positions(level, block)
    source = [-1] * MODULUS
    for old_position, new_position in enumerate(positions):
        source[old_position] = (
            inverse_multiplier * (label.permutation[new_position] - offset)
        ) % MODULUS
    return BlockLabel(source_cell, tuple(source))  # type: ignore[arg-type]


def _transport(
    graph: ConstraintGraph,
    step: CycleStep,
    block_id: int,
    label: BlockLabel,
) -> BlockLabel:
    edge = graph.edges[step.edge]
    if edge.phase == 0:
        return label
    if step.forward:
        return _advance_label(block_id, label, edge.lower_level, edge.letter)
    return _retreat_label(
        block_id,
        label,
        edge.lower_level,
        edge.letter,
        _expected_half(edge.upper),
    )


def _step_start(edge: ConstraintEdge, step: CycleStep) -> Node:
    return edge.upper if step.forward else edge.lower


def _step_stop(edge: ConstraintEdge, step: CycleStep) -> Node:
    return edge.lower if step.forward else edge.upper


@lru_cache(maxsize=None)
def fundamental_cycles(
    minimum_level: int, maximum_level: int
) -> tuple[tuple[CycleStep, ...], ...]:
    """Return a deterministic fundamental-cycle basis of the constraint graph."""

    graph = constraint_graph(minimum_level, maximum_level)
    adjacency: dict[Node, list[tuple[int, Node]]] = {
        node: [] for node in graph.nodes
    }
    for edge in graph.edges:
        adjacency[edge.upper].append((edge.id, edge.lower))
        adjacency[edge.lower].append((edge.id, edge.upper))
    for row in adjacency.values():
        row.sort()

    root = graph.nodes[0]
    parent: dict[Node, Node | None] = {root: None}
    parent_edge: dict[Node, int] = {}
    queue = deque((root,))
    while queue:
        node = queue.popleft()
        for edge_id, neighbor in adjacency[node]:
            if neighbor not in parent:
                parent[neighbor] = node
                parent_edge[neighbor] = edge_id
                queue.append(neighbor)
    if len(parent) != len(graph.nodes):
        raise AssertionError("later-edge constraint graph is disconnected")
    tree_edges = set(parent_edge.values())

    def tree_path(start: Node, stop: Node) -> tuple[CycleStep, ...]:
        ancestors: set[Node] = set()
        node: Node | None = start
        while node is not None:
            ancestors.add(node)
            node = parent[node]
        tail: list[tuple[Node, Node, int]] = []
        node = stop
        while node not in ancestors:
            previous = parent[node]
            if previous is None:
                raise AssertionError("tree path lost its common ancestor")
            tail.append((node, previous, parent_edge[node]))
            node = previous
        common = node

        steps: list[CycleStep] = []
        node = start
        while node != common:
            previous = parent[node]
            if previous is None:
                raise AssertionError("tree path ended before its ancestor")
            edge = graph.edges[parent_edge[node]]
            steps.append(
                CycleStep(edge.id, node == edge.upper and previous == edge.lower)
            )
            node = previous
        for child, previous, edge_id in reversed(tail):
            edge = graph.edges[edge_id]
            steps.append(
                CycleStep(edge.id, previous == edge.upper and child == edge.lower)
            )
        return tuple(steps)

    cycles = []
    for edge in graph.edges:
        if edge.id in tree_edges:
            continue
        steps = (CycleStep(edge.id, True),) + tree_path(edge.lower, edge.upper)
        current = _step_start(graph.edges[steps[0].edge], steps[0])
        origin = current
        for step in steps:
            constraint = graph.edges[step.edge]
            if _step_start(constraint, step) != current:
                raise AssertionError("fundamental cycle is not continuous")
            current = _step_stop(constraint, step)
        if current != origin or len({step.edge for step in steps}) != len(steps):
            raise AssertionError("fundamental cycle failed closure or simplicity")
        cycles.append(steps)
    expected_rank = len(graph.edges) - len(graph.nodes) + 1
    if len(cycles) != expected_rank:
        raise AssertionError("fundamental-cycle census has the wrong rank")
    return tuple(cycles)


@lru_cache(maxsize=None)
def simple_cycles(
    minimum_level: int, maximum_level: int
) -> tuple[tuple[CycleStep, ...], ...]:
    """Enumerate every undirected simple cycle in the audited ``3..4`` graph.

    The start vertex is the least vertex on the cycle, and the order of its
    two neighbours removes the reverse duplicate.  Keeping this deliberately
    narrow prevents an accidental exponential search at larger horizons.
    """

    if (minimum_level, maximum_level) != (3, 4):
        raise ValueError("simple-cycle enumeration is audited only for levels 3..4")
    graph = constraint_graph(minimum_level, maximum_level)
    node_index = {node: index for index, node in enumerate(graph.nodes)}
    adjacency: dict[Node, list[tuple[int, Node]]] = {
        node: [] for node in graph.nodes
    }
    for edge in graph.edges:
        adjacency[edge.upper].append((edge.id, edge.lower))
        adjacency[edge.lower].append((edge.id, edge.upper))
    for row in adjacency.values():
        row.sort()

    found: list[tuple[CycleStep, ...]] = []
    for start in graph.nodes:
        start_index = node_index[start]

        def visit(
            current: Node,
            nodes: tuple[Node, ...],
            edge_ids: tuple[int, ...],
        ) -> None:
            for edge_id, neighbor in adjacency[current]:
                if edge_ids and edge_id == edge_ids[-1]:
                    continue
                if neighbor == start:
                    if (
                        len(nodes) >= 4
                        and node_index[nodes[1]] < node_index[nodes[-1]]
                    ):
                        closed = nodes + (start,)
                        steps = []
                        for used_edge, here, there in zip(
                            edge_ids + (edge_id,), closed, closed[1:]
                        ):
                            edge = graph.edges[used_edge]
                            if {here, there} != {edge.upper, edge.lower}:
                                raise AssertionError("simple-cycle edge is discontinuous")
                            steps.append(CycleStep(used_edge, here == edge.upper))
                        found.append(tuple(steps))
                    continue
                if node_index[neighbor] < start_index or neighbor in nodes:
                    continue
                visit(neighbor, nodes + (neighbor,), edge_ids + (edge_id,))

        visit(start, (start,), ())

    result = tuple(
        sorted(found, key=lambda cycle: tuple((step.edge, step.forward) for step in cycle))
    )
    keys = {
        tuple(sorted(step.edge for step in cycle))
        for cycle in result
    }
    if len(keys) != len(result):
        raise AssertionError("simple-cycle enumeration produced a duplicate")
    for cycle in result:
        if len({step.edge for step in cycle}) != len(cycle):
            raise AssertionError("simple cycle repeats an edge")
        current = _step_start(graph.edges[cycle[0].edge], cycle[0])
        origin = current
        for step in cycle:
            edge = graph.edges[step.edge]
            if _step_start(edge, step) != current:
                raise AssertionError("simple-cycle orientation is discontinuous")
            current = _step_stop(edge, step)
        if current != origin:
            raise AssertionError("simple cycle does not close")
    return result


def _label_mismatches(left: BlockLabel, right: BlockLabel) -> int:
    if left.cell != right.cell:
        return MODULUS
    return sum(a != b for a, b in zip(left.permutation, right.permutation))


@lru_cache(maxsize=None)
def _cycle_minimum_steps(
    minimum_level: int,
    maximum_level: int,
    steps: tuple[CycleStep, ...],
    block_id: int,
) -> tuple[int, CycleWitness]:
    graph = constraint_graph(minimum_level, maximum_level)
    first_edge = graph.edges[steps[0].edge]
    start = _step_start(first_edge, steps[0])
    half = _expected_half(start)
    best = MODULUS + 1
    witness: CycleWitness | None = None
    for cell in _solver().model.cells_by_half[half]:
        for permutation in five_permutations():
            initial = BlockLabel(cell, permutation)  # type: ignore[arg-type]
            image = initial
            for step in steps:
                image = _transport(graph, step, block_id, image)
            mismatches = _label_mismatches(initial, image)
            candidate = CycleWitness(cell, permutation)  # type: ignore[arg-type]
            if mismatches < best or (
                mismatches == best and (witness is None or candidate < witness)
            ):
                best = mismatches
                witness = candidate
            if best == 0:
                return best, witness
    if witness is None or not 0 <= best <= MODULUS:
        raise AssertionError("cycle minimum enumeration failed")
    return best, witness


@lru_cache(maxsize=None)
def _cycle_minimum(
    minimum_level: int,
    maximum_level: int,
    basis_index: int,
    block_id: int,
) -> tuple[int, CycleWitness]:
    steps = fundamental_cycles(minimum_level, maximum_level)[basis_index]
    return _cycle_minimum_steps(minimum_level, maximum_level, steps, block_id)


@lru_cache(maxsize=None)
def _verify_ordinary_block_homogeneity(
    minimum_level: int, maximum_level: int
) -> bool:
    solver = _solver()
    blocks = source_blocks()
    for level in range(minimum_level, maximum_level):
        representative = solver._source_positions(level, blocks[0])
        if any(
            solver._source_positions(level, block) != representative
            for block in blocks[:ORDINARY_BLOCKS]
        ):
            return False
    return True


@lru_cache(maxsize=None)
def analyze_cycle(
    minimum_level: int,
    maximum_level: int,
    basis_index: int,
) -> CycleCertificate:
    """Exhaustively certify one fundamental holonomy-cycle contribution."""

    graph = constraint_graph(minimum_level, maximum_level)
    cycles = fundamental_cycles(minimum_level, maximum_level)
    if not 0 <= basis_index < len(cycles):
        raise IndexError("cycle basis index is out of range")
    if not _verify_ordinary_block_homogeneity(minimum_level, maximum_level):
        raise AssertionError("ordinary source blocks have different J-power actions")
    steps = cycles[basis_index]
    ordinary, ordinary_witness = _cycle_minimum(
        minimum_level, maximum_level, basis_index, 0
    )
    special, special_witness = _cycle_minimum(
        minimum_level, maximum_level, basis_index, SPECIAL_BLOCK
    )
    minimum_weight = min(graph.edges[step.edge].weight for step in steps)
    contribution = minimum_weight * Fraction(
        ORDINARY_BLOCKS * ordinary + special,
        FIBER_SIZE,
    )
    return CycleCertificate(
        basis_index=basis_index,
        steps=steps,
        minimum_edge_weight=minimum_weight,
        ordinary_minimum_mismatches=ordinary,
        special_minimum_mismatches=special,
        ordinary_witness=ordinary_witness,
        special_witness=special_witness,
        contribution=contribution,
    )


@lru_cache(maxsize=None)
def analyze_fractional_cycle(
    cycle_index: int,
    allocation: Fraction,
) -> FractionalCycleCertificate:
    """Exhaustively certify one allocated simple-cycle contribution."""

    if type(allocation) is not Fraction:
        raise TypeError("fractional cycle allocation must be an exact Fraction")
    if allocation <= 0:
        raise ValueError("fractional cycle allocation must be positive")
    cycles = simple_cycles(3, 4)
    if not 0 <= cycle_index < len(cycles):
        raise IndexError("simple cycle index is out of range")
    if not _verify_ordinary_block_homogeneity(3, 4):
        raise AssertionError("ordinary source blocks have different J-power actions")
    steps = cycles[cycle_index]
    ordinary, ordinary_witness = _cycle_minimum_steps(3, 4, steps, 0)
    special, special_witness = _cycle_minimum_steps(
        3, 4, steps, SPECIAL_BLOCK
    )
    contribution = allocation * Fraction(
        ORDINARY_BLOCKS * ordinary + special,
        FIBER_SIZE,
    )
    return FractionalCycleCertificate(
        cycle_index=cycle_index,
        steps=steps,
        allocation=allocation,
        ordinary_minimum_mismatches=ordinary,
        special_minimum_mismatches=special,
        ordinary_witness=ordinary_witness,
        special_witness=special_witness,
        contribution=contribution,
    )


@lru_cache(maxsize=1)
def _fractional_simple_cycle_packing() -> tuple[FractionalCycleCertificate, ...]:
    """Build a deterministic feasible packing of all positive ``3..4`` cycles."""

    graph = constraint_graph(3, 4)
    cycles = simple_cycles(3, 4)
    unit_analyses = tuple(
        analyze_fractional_cycle(index, Fraction(1))
        for index in range(len(cycles))
    )
    positive = tuple(item for item in unit_analyses if item.contribution > 0)
    if not positive:
        return ()

    incidence = [0] * len(graph.edges)
    for item in positive:
        for step in item.steps:
            incidence[step.edge] += 1
    allocation = min(
        graph.edges[edge_id].weight / count
        for edge_id, count in enumerate(incidence)
        if count
    )
    packed = tuple(
        analyze_fractional_cycle(item.cycle_index, allocation)
        for item in positive
    )
    loads = [Fraction(0)] * len(graph.edges)
    for item in packed:
        for step in item.steps:
            loads[step.edge] += item.allocation
    if any(load > edge.weight for load, edge in zip(loads, graph.edges)):
        raise AssertionError("fractional simple-cycle packing exceeds an edge weight")
    return packed


def _best_edge_disjoint_cycles(
    minimum_level: int, maximum_level: int
) -> tuple[CycleCertificate, ...]:
    analyses = tuple(
        analyze_cycle(minimum_level, maximum_level, index)
        for index in range(len(fundamental_cycles(minimum_level, maximum_level)))
    )
    positive = tuple(item for item in analyses if item.contribution > 0)
    edge_masks = {
        item.basis_index: sum(1 << step.edge for step in item.steps)
        for item in positive
    }
    best_weight = Fraction(-1)
    best_indices: tuple[int, ...] | None = None

    def search(
        position: int,
        used: int,
        weight: Fraction,
        chosen: tuple[int, ...],
    ) -> None:
        nonlocal best_weight, best_indices
        if position == len(positive):
            if weight > best_weight or (
                weight == best_weight
                and (best_indices is None or chosen < best_indices)
            ):
                best_weight = weight
                best_indices = chosen
            return
        item = positive[position]
        search(position + 1, used, weight, chosen)
        mask = edge_masks[item.basis_index]
        if not used & mask:
            search(
                position + 1,
                used | mask,
                weight + item.contribution,
                chosen + (item.basis_index,),
            )

    search(0, 0, Fraction(0), ())
    if best_indices is None:
        raise AssertionError("cycle packing search returned no state")
    by_index = {item.basis_index: item for item in analyses}
    return tuple(by_index[index] for index in best_indices)


@lru_cache(maxsize=None)
def anchor_terms(seed: str = "tree") -> tuple[AnchorTerm, ...]:
    """Return the exact first-transition minimum for a frozen level-2 seed."""

    solver = _solver()
    lower_level = 2
    upper_level = 3
    lower_spec = default_collar(lower_level)
    upper_spec = default_collar(upper_level)
    if seed == "tree":
        lower = solver.tree_family(lower_level, lower_spec)
    elif seed == "lexicographic":
        lower = solver.lexicographic_family(lower_level, lower_spec)
    else:
        raise ValueError("seed must be 'tree' or 'lexicographic'")
    lower_graph = collar_graph(lower_spec)
    lower_id = {word: index for index, word in enumerate(lower_graph.vertices)}
    incidence = refinement_incidence(upper_spec, lower_spec)
    parents = tuple(atom.parent for atom in incidence.atoms)
    if len(set(parents)) != len(parents) or set(parents) != set(
        collar_graph(upper_spec).vertices
    ):
        raise AssertionError(
            "the exact anchor minimum requires one joint atom per upper context"
        )
    terms = []
    for atom in incidence.atoms:
        child0 = lower.maps[lower_id[atom.child0]]
        child1 = lower.maps[lower_id[atom.child1]]
        source_half = last_symbol(atom.parent[upper_spec.left - 1], upper_level)
        desired1 = solver.retreat(
            child1,
            lower_level,
            atom.parent[upper_spec.left],
            source_half,
        )
        distance = child0.distance(desired1)
        terms.append(
            AnchorTerm(
                parent=atom.parent,
                extension=atom.extension,
                branch_weight=atom.branch_weight,
                desired_map_distance=distance,
                contribution=atom.branch_weight * distance,
            )
        )
    return tuple(terms)


@lru_cache(maxsize=None)
def build_certificate(
    maximum_level: int,
    seed: str = "tree",
) -> BoundCertificate:
    """Build a replayable bound certificate for anchored horizons 2..4 or 2..5."""

    if maximum_level not in (4, 5):
        raise ValueError("the audited bound scope is limited to horizons 2..4 and 2..5")
    terms = anchor_terms(seed)
    anchor = sum((term.contribution for term in terms), Fraction(0))
    if maximum_level == 4:
        cycles = ()
        fractional_cycles = _fractional_simple_cycle_packing()
    else:
        cycles = _best_edge_disjoint_cycles(3, maximum_level)
        fractional_cycles = ()
    cycle_bound = sum(
        (cycle.contribution for cycle in cycles), Fraction(0)
    ) + sum(
        (cycle.contribution for cycle in fractional_cycles), Fraction(0)
    )
    certificate = BoundCertificate(
        minimum_level=2,
        maximum_level=maximum_level,
        seed=seed,
        anchor_terms=terms,
        anchor_bound=anchor,
        cycles=cycles,
        fractional_cycles=fractional_cycles,
        cycle_bound=cycle_bound,
        lower_bound=anchor + cycle_bound,
    )
    if not verify_certificate(certificate):
        raise AssertionError("newly built lower-bound certificate failed replay")
    return certificate


def verify_certificate(certificate: BoundCertificate) -> bool:
    """Replay exact arithmetic, cycle minima, and edge-capacity gates."""

    if certificate.minimum_level != 2 or certificate.maximum_level not in (4, 5):
        return False
    if any(
        type(value) is not Fraction
        for value in (
            certificate.anchor_bound,
            certificate.cycle_bound,
            certificate.lower_bound,
        )
    ):
        return False
    try:
        expected_terms = anchor_terms(certificate.seed)
        graph = constraint_graph(3, certificate.maximum_level)
        basis = fundamental_cycles(3, certificate.maximum_level)
    except (AssertionError, IndexError, KeyError, ValueError):
        return False
    if certificate.anchor_terms != expected_terms:
        return False
    anchor = sum((term.contribution for term in expected_terms), Fraction(0))
    if certificate.anchor_bound != anchor:
        return False
    edge_loads = [Fraction(0)] * len(graph.edges)
    cycle_sum = Fraction(0)
    seen_indices: set[int] = set()
    for claimed in certificate.cycles:
        if claimed.basis_index in seen_indices:
            return False
        if not 0 <= claimed.basis_index < len(basis):
            return False
        expected = analyze_cycle(3, certificate.maximum_level, claimed.basis_index)
        if claimed != expected or claimed.steps != basis[claimed.basis_index]:
            return False
        edges = {step.edge for step in claimed.steps}
        if len(edges) != len(claimed.steps):
            return False
        if any(not 0 <= edge < len(graph.edges) for edge in edges):
            return False
        for edge in edges:
            edge_loads[edge] += claimed.minimum_edge_weight
        cycle_sum += claimed.contribution
        seen_indices.add(claimed.basis_index)

    if certificate.maximum_level != 4 and certificate.fractional_cycles:
        return False
    seen_fractional: set[int] = set()
    simple = simple_cycles(3, 4) if certificate.maximum_level == 4 else ()
    for claimed in certificate.fractional_cycles:
        if claimed.cycle_index in seen_fractional:
            return False
        if (
            not 0 <= claimed.cycle_index < len(simple)
            or type(claimed.allocation) is not Fraction
            or claimed.allocation <= 0
        ):
            return False
        expected = analyze_fractional_cycle(
            claimed.cycle_index, claimed.allocation
        )
        if claimed != expected or claimed.steps != simple[claimed.cycle_index]:
            return False
        edges = {step.edge for step in claimed.steps}
        if len(edges) != len(claimed.steps):
            return False
        for edge in edges:
            edge_loads[edge] += claimed.allocation
        cycle_sum += claimed.contribution
        seen_fractional.add(claimed.cycle_index)
    if any(load > edge.weight for load, edge in zip(edge_loads, graph.edges)):
        return False
    if certificate.cycle_bound != cycle_sum:
        return False
    return certificate.lower_bound == anchor + cycle_sum


@lru_cache(maxsize=None)
def bound_report(
    maximum_level: int,
    seed: str = "tree",
    lift_phase: int = 1,
) -> BoundReport:
    """Compare the bound with one deterministic coordinate-sweep reference."""

    certificate = build_certificate(maximum_level, seed)
    reference_report = FiniteHorizonOptimizer(
        2,
        maximum_level,
        solver=_solver(),
        seed=seed,
        lift_phase=lift_phase,
        freeze_minimum=True,
    ).optimize(10)
    if not reference_report.minimum_level_frozen:
        raise AssertionError(
            "coordinate reference unexpectedly released its anchor"
        )
    reference = reference_report.final_objective
    if certificate.lower_bound > reference:
        raise AssertionError("claimed lower bound exceeds a feasible reference")
    return BoundReport(
        certificate=certificate,
        incumbent=reference,
        gap=reference - certificate.lower_bound,
        meets_incumbent=certificate.lower_bound == reference,
        incumbent_seed=seed,
        incumbent_lift_phase=lift_phase,
    )


def format_report(report: BoundReport) -> str:
    certificate = report.certificate
    return "\n".join(
        (
            "anchored structured horizon=2..%d seed=%s"
            % (certificate.maximum_level, certificate.seed),
            "  anchor bound=%s cycle-packing bound=%s"
            % (certificate.anchor_bound, certificate.cycle_bound),
            "  certified lower bound=%s" % certificate.lower_bound,
            "  coordinate-sweep feasible reference=%s gap=%s meets=%s"
            % (
                report.incumbent,
                report.gap,
                report.meets_incumbent,
            ),
            "  selected fundamental cycles=%s fractional simple cycles=%s"
            % (
                [cycle.basis_index for cycle in certificate.cycles],
                [
                    (cycle.cycle_index, cycle.allocation)
                    for cycle in certificate.fractional_cycles
                ],
            ),
            "  scope: fixed-r2 structured 625-block/S5 ansatz; relaxation only",
        )
    )


def main() -> int:
    print("ENTROPY-SELECTION finite-horizon certified lower bounds")
    print("NON-CANONICAL / NON-FORMAL / NO CLAIM STATUS")
    for maximum_level in (4, 5):
        print()
        print(format_report(bound_report(maximum_level)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "AnchorTerm",
    "BlockLabel",
    "BoundCertificate",
    "BoundReport",
    "ConstraintEdge",
    "ConstraintGraph",
    "CycleCertificate",
    "CycleStep",
    "CycleWitness",
    "FractionalCycleCertificate",
    "analyze_cycle",
    "analyze_fractional_cycle",
    "anchor_terms",
    "bound_report",
    "build_certificate",
    "constraint_graph",
    "format_report",
    "fundamental_cycles",
    "main",
    "simple_cycles",
    "verify_certificate",
]
