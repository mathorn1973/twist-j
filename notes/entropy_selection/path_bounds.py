#!/usr/bin/env python3
"""Exact anchor-to-anchor path duals for the fixed ``2..4`` horizon.

NON-CANONICAL LOCAL ANALYSIS.  This module strengthens the earlier cycle-only
relaxation without changing its scope.  The level-2 tree family is frozen,
the structured level-3 and level-4 maps are free, and the all-different
coupling between the 625 source blocks is dropped.

For each source block the objective is a 28-node, 32-edge gain graph: the
existing 16 free nodes and 20 later refinement edges, plus 12 terminal leaves
carrying the two fixed level-2 occurrences at each level-3 context.  Every
edge transport is an isometry of the five-point block label.  Consequently a
terminal-to-terminal walk gives the exact triangle inequality

``sum_e n_e(P) m_e >= m(H_P(a_start), a_stop)``.

Allocated path inequalities may be added while their load stays below every
objective-edge weight, separately for every source block.  The frozen witness
below uses ten paths and saturates all 32 capacities.  A second, independent
dual checks optimality inside the declared catalog of all 622 terminal paths
with simple free-node interiors together with the 20 simple later cycles.

The result is a lower bound only for the named fixed-boundary structured
finite problem.  It is not an entropy obstruction, an inverse-limit result,
or authority for a public claim.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache

try:
    from .bounds import (
        FIBER_SIZE,
        ORDINARY_BLOCKS,
        SPECIAL_BLOCK,
        BlockLabel,
        CycleStep,
        Node,
        _advance_label,
        _cycle_minimum_steps,
        _expected_half,
        _label_mismatches,
        _retreat_label,
        _step_start,
        _step_stop,
        _transport,
        _verify_ordinary_block_homogeneity,
        constraint_graph,
        simple_cycles,
    )
    from .collars import collar_graph, refinement_incidence
    from .growing import StructuredMap, default_collar
except ImportError:  # Direct execution from this directory.
    from bounds import (  # type: ignore[no-redef]
        FIBER_SIZE,
        ORDINARY_BLOCKS,
        SPECIAL_BLOCK,
        BlockLabel,
        CycleStep,
        Node,
        _advance_label,
        _cycle_minimum_steps,
        _expected_half,
        _label_mismatches,
        _retreat_label,
        _step_start,
        _step_stop,
        _transport,
        _verify_ordinary_block_homogeneity,
        constraint_graph,
        simple_cycles,
    )
    from collars import collar_graph, refinement_incidence  # type: ignore[no-redef]
    from growing import StructuredMap, default_collar  # type: ignore[no-redef]


BLOCK_COUNT = 625
LATER_EDGE_COUNT = 20
ANCHOR_EDGE_COUNT = 12
EDGE_COUNT = LATER_EDGE_COUNT + ANCHOR_EDGE_COUNT
CAPACITY_SCALE = 24
ALL_BLOCKS = tuple(range(BLOCK_COUNT))


@dataclass(frozen=True, slots=True)
class AnchorTerminal:
    """One fixed level-2 occurrence attached to a free level-3 node."""

    id: int
    atom_index: int
    phase: int
    parent: Node
    child: tuple[int, ...]
    lower_level: int
    letter: int
    weight: Fraction

    @property
    def edge_id(self) -> int:
        return LATER_EDGE_COUNT + self.id


@dataclass(frozen=True, slots=True)
class TerminalPath:
    """A canonical terminal path with its two anchor edges implicit."""

    start_terminal: int
    end_terminal: int
    steps: tuple[CycleStep, ...]


@dataclass(frozen=True, slots=True)
class PathAllocation:
    """One exact path inequality allocated on named source blocks."""

    block_ids: tuple[int, ...]
    path: TerminalPath
    allocation: Fraction
    mismatch_histogram: tuple[tuple[int, int], ...]
    total_mismatches: int
    contribution: Fraction


@dataclass(frozen=True, slots=True)
class PathCertificate:
    """Replayable lower-bound witness for the anchored ``2..4`` problem."""

    minimum_level: int
    maximum_level: int
    seed: str
    paths: tuple[PathAllocation, ...]
    lower_bound: Fraction


@dataclass(frozen=True, slots=True)
class CatalogDualCertificate:
    """Upper dual for the declared blockwise simple-path/cycle catalog.

    Prices use the scaled primal variable ``y = 24 * allocation``.  Hence the
    final objective is divided by ``24 * 3125``.
    """

    path_count: int
    cycle_count: int
    ordinary_prices: tuple[Fraction, ...]
    special_prices: tuple[Fraction, ...]
    ordinary_scaled_bound: Fraction
    special_scaled_bound: Fraction
    scaled_bound: Fraction
    bound: Fraction


@lru_cache(maxsize=1)
def _anchor_data() -> tuple[
    tuple[AnchorTerminal, ...], tuple[StructuredMap, ...]
]:
    """Reconstruct the twelve occurrence terminals from the frozen tree seed."""

    try:
        from .bounds import _solver
    except ImportError:  # Direct execution from this directory.
        from bounds import _solver  # type: ignore[no-redef]

    solver = _solver()
    lower_level = 2
    upper_level = 3
    lower_spec = default_collar(lower_level)
    upper_spec = default_collar(upper_level)
    lower = solver.tree_family(lower_level, lower_spec)
    lower_graph = collar_graph(lower_spec)
    lower_id = {word: index for index, word in enumerate(lower_graph.vertices)}
    incidence = refinement_incidence(upper_spec, lower_spec)
    expected_parents = collar_graph(upper_spec).vertices
    if tuple(atom.parent for atom in incidence.atoms) != expected_parents:
        raise AssertionError("anchor atoms left canonical level-3 context order")

    terminals: list[AnchorTerminal] = []
    maps: list[StructuredMap] = []
    for atom_index, atom in enumerate(incidence.atoms):
        parent: Node = (upper_level, atom.parent)
        letter = atom.parent[upper_spec.left]
        for phase, child in enumerate((atom.child0, atom.child1)):
            terminal_id = len(terminals)
            terminals.append(
                AnchorTerminal(
                    id=terminal_id,
                    atom_index=atom_index,
                    phase=phase,
                    parent=parent,
                    child=child,
                    lower_level=lower_level,
                    letter=letter,
                    weight=atom.branch_weight,
                )
            )
            maps.append(lower.maps[lower_id[child]])
    if len(terminals) != ANCHOR_EDGE_COUNT:
        raise AssertionError("fixed anchor did not produce twelve occurrences")
    return tuple(terminals), tuple(maps)


def anchor_terminals() -> tuple[AnchorTerminal, ...]:
    return _anchor_data()[0]


def augmented_edge_weights() -> tuple[Fraction, ...]:
    graph = constraint_graph(3, 4)
    return tuple(edge.weight for edge in graph.edges) + tuple(
        terminal.weight for terminal in anchor_terminals()
    )


def _terminal_label(terminal_id: int, block_id: int) -> BlockLabel:
    mapping = _anchor_data()[1][terminal_id]
    return BlockLabel(mapping.cells[block_id], mapping.permutations[block_id])


def _reverse_anchor(
    terminal: AnchorTerminal, block_id: int, label: BlockLabel
) -> BlockLabel:
    if terminal.phase == 0:
        return label
    return _retreat_label(
        block_id,
        label,
        terminal.lower_level,
        terminal.letter,
        _expected_half(terminal.parent),
    )


def _forward_anchor(
    terminal: AnchorTerminal, block_id: int, label: BlockLabel
) -> BlockLabel:
    if terminal.phase == 0:
        return label
    return _advance_label(
        block_id,
        label,
        terminal.lower_level,
        terminal.letter,
    )


def _validate_path(path: TerminalPath) -> None:
    if type(path) is not TerminalPath or type(path.steps) is not tuple:
        raise TypeError("terminal path must use the exact frozen data types")
    terminals = anchor_terminals()
    if not (
        type(path.start_terminal) is int
        and type(path.end_terminal) is int
        and 0 <= path.start_terminal < path.end_terminal < len(terminals)
    ):
        raise ValueError("terminal path needs two canonical distinct terminal ids")
    graph = constraint_graph(3, 4)
    current = terminals[path.start_terminal].parent
    visited = {current}
    for step in path.steps:
        if (
            type(step) is not CycleStep
            or type(step.edge) is not int
            or type(step.forward) is not bool
            or not 0 <= step.edge < len(graph.edges)
        ):
            raise ValueError("terminal path uses an unknown later edge")
        edge = graph.edges[step.edge]
        if _step_start(edge, step) != current:
            raise ValueError("terminal path is not orientation-continuous")
        current = _step_stop(edge, step)
        if current in visited:
            raise ValueError("catalog terminal paths need simple free-node interiors")
        visited.add(current)
    if current != terminals[path.end_terminal].parent:
        raise ValueError("terminal path stops at the wrong anchor parent")


def path_edge_ids(path: TerminalPath) -> tuple[int, ...]:
    """Return all objective edges in traversal order, including both leaves."""

    _validate_path(path)
    return (
        LATER_EDGE_COUNT + path.start_terminal,
        *(step.edge for step in path.steps),
        LATER_EDGE_COUNT + path.end_terminal,
    )


@lru_cache(maxsize=None)
def _path_block_mismatches_cached(path: TerminalPath) -> tuple[int, ...]:
    _validate_path(path)
    terminals = anchor_terminals()
    start = terminals[path.start_terminal]
    stop = terminals[path.end_terminal]
    graph = constraint_graph(3, 4)
    result = []
    for block_id in ALL_BLOCKS:
        label = _terminal_label(start.id, block_id)
        label = _reverse_anchor(start, block_id, label)
        for step in path.steps:
            label = _transport(graph, step, block_id, label)
        label = _forward_anchor(stop, block_id, label)
        mismatch = _label_mismatches(
            label, _terminal_label(stop.id, block_id)
        )
        if not 0 <= mismatch <= 5:
            raise AssertionError("terminal path produced an invalid block mismatch")
        result.append(mismatch)
    return tuple(result)


def path_block_mismatches(path: TerminalPath) -> tuple[int, ...]:
    """Replay one terminal path on all 625 fixed source-block labels.

    Validate before entering the cache: Python deliberately equates ``False``
    with ``0``, so a numeric-lookalike step must not alias a canonical cached
    path before its exact types have been checked.
    """

    _validate_path(path)
    return _path_block_mismatches_cached(path)


def analyze_path(
    block_ids: tuple[int, ...],
    path: TerminalPath,
    allocation: Fraction,
) -> PathAllocation:
    """Reconstruct one exact allocated path term from public inputs."""

    if type(allocation) is not Fraction:
        raise TypeError("path allocation must be an exact Fraction")
    if allocation <= 0:
        raise ValueError("path allocation must be positive")
    if (
        type(block_ids) is not tuple
        or not block_ids
        or any(type(block) is not int for block in block_ids)
        or tuple(sorted(set(block_ids))) != block_ids
        or block_ids[0] < 0
        or block_ids[-1] >= BLOCK_COUNT
    ):
        raise ValueError("path block ids must be a nonempty canonical subset")
    mismatches = path_block_mismatches(path)
    selected = tuple(mismatches[block] for block in block_ids)
    histogram = tuple(sorted(Counter(selected).items()))
    total = sum(selected)
    return PathAllocation(
        block_ids=block_ids,
        path=path,
        allocation=allocation,
        mismatch_histogram=histogram,
        total_mismatches=total,
        contribution=allocation * Fraction(total, FIBER_SIZE),
    )


@lru_cache(maxsize=None)
def _simple_internal_paths(start: Node, stop: Node) -> tuple[
    tuple[CycleStep, ...], ...
]:
    graph = constraint_graph(3, 4)
    if start not in graph.nodes or stop not in graph.nodes:
        raise ValueError("terminal attachment left the later graph")
    if start == stop:
        return ((),)
    adjacency: dict[Node, list[tuple[int, Node, bool]]] = {
        node: [] for node in graph.nodes
    }
    for edge in graph.edges:
        adjacency[edge.upper].append((edge.id, edge.lower, True))
        adjacency[edge.lower].append((edge.id, edge.upper, False))
    for row in adjacency.values():
        row.sort()

    found: list[tuple[CycleStep, ...]] = []

    def visit(
        current: Node,
        visited: frozenset[Node],
        steps: tuple[CycleStep, ...],
    ) -> None:
        for edge_id, neighbor, forward in adjacency[current]:
            if neighbor in visited:
                continue
            step = CycleStep(edge_id, forward)
            if neighbor == stop:
                found.append(steps + (step,))
            else:
                visit(neighbor, visited | {neighbor}, steps + (step,))

    visit(start, frozenset((start,)), ())
    return tuple(
        sorted(
            found,
            key=lambda steps: tuple((step.edge, step.forward) for step in steps),
        )
    )


@lru_cache(maxsize=1)
def simple_terminal_paths() -> tuple[TerminalPath, ...]:
    """Enumerate all terminal paths with a simple free-node interior."""

    terminals = anchor_terminals()
    result = []
    for start in range(len(terminals)):
        for stop in range(start + 1, len(terminals)):
            for steps in _simple_internal_paths(
                terminals[start].parent, terminals[stop].parent
            ):
                path = TerminalPath(start, stop, steps)
                _validate_path(path)
                result.append(path)
    paths = tuple(result)
    if len(paths) != 622 or len(set(paths)) != len(paths):
        raise AssertionError("simple terminal-path catalog census changed")
    return paths


_FROZEN_PATHS = (
    # Two scaled units on each of the first two paths.
    (2, 7, ((8, False), (9, True)), Fraction(1, 12)),
    (0, 1, (), Fraction(1, 12)),
    # Four more full-defect paths, one scaled unit each.
    (9, 11, ((3, False), (2, True)), Fraction(1, 24)),
    (9, 10, ((15, False), (14, True)), Fraction(1, 24)),
    (6, 10, ((13, False), (12, True)), Fraction(1, 24)),
    (6, 11, ((1, False), (0, True)), Fraction(1, 24)),
    # Four special-block defects complete the exact packing.
    (
        3,
        8,
        (
            (5, False),
            (4, True),
            (18, False),
            (19, True),
            (11, False),
            (10, True),
        ),
        Fraction(1, 24),
    ),
    (5, 8, ((11, False), (10, True)), Fraction(1, 24)),
    (4, 5, (), Fraction(1, 24)),
    (
        3,
        4,
        ((17, False), (16, True), (6, False), (7, True)),
        Fraction(1, 24),
    ),
)


@lru_cache(maxsize=1)
def build_path_certificate() -> PathCertificate:
    """Build the frozen ten-path lower-bound witness."""

    paths = tuple(
        analyze_path(
            ALL_BLOCKS,
            TerminalPath(
                start,
                stop,
                tuple(CycleStep(edge, forward) for edge, forward in steps),
            ),
            allocation,
        )
        for start, stop, steps, allocation in _FROZEN_PATHS
    )
    lower_bound = sum((path.contribution for path in paths), Fraction(0))
    certificate = PathCertificate(
        minimum_level=2,
        maximum_level=4,
        seed="tree",
        paths=paths,
        lower_bound=lower_bound,
    )
    if not verify_path_certificate(certificate):
        raise AssertionError("new anchor-to-anchor certificate failed replay")
    return certificate


def _validate_allocation_types(claimed: PathAllocation) -> None:
    if (
        type(claimed) is not PathAllocation
        or type(claimed.block_ids) is not tuple
        or type(claimed.path) is not TerminalPath
        or type(claimed.allocation) is not Fraction
        or type(claimed.mismatch_histogram) is not tuple
        or type(claimed.total_mismatches) is not int
        or type(claimed.contribution) is not Fraction
    ):
        raise TypeError("path allocation contains a noncanonical data type")
    if any(
        type(row) is not tuple
        or len(row) != 2
        or type(row[0]) is not int
        or type(row[1]) is not int
        for row in claimed.mismatch_histogram
    ):
        raise TypeError("path mismatch histogram must contain exact integer pairs")


def certificate_edge_loads(
    certificate: PathCertificate,
) -> tuple[tuple[Fraction, ...], ...]:
    """Return the exact per-block loads after validating every path term."""

    loads = [
        [Fraction(0) for _ in range(EDGE_COUNT)] for _ in range(BLOCK_COUNT)
    ]
    for claimed in certificate.paths:
        _validate_allocation_types(claimed)
        expected = analyze_path(
            claimed.block_ids, claimed.path, claimed.allocation
        )
        if claimed != expected:
            raise ValueError("path allocation metadata failed exact replay")
        for block_id in claimed.block_ids:
            for edge_id in path_edge_ids(claimed.path):
                loads[block_id][edge_id] += claimed.allocation
    return tuple(tuple(row) for row in loads)


def verify_path_certificate(certificate: PathCertificate) -> bool:
    """Replay terminal labels, transports, defects, and all 20,000 capacities."""

    if (
        type(certificate) is not PathCertificate
        or type(certificate.minimum_level) is not int
        or type(certificate.maximum_level) is not int
        or type(certificate.seed) is not str
        or type(certificate.paths) is not tuple
        or certificate.minimum_level != 2
        or certificate.maximum_level != 4
        or certificate.seed != "tree"
        or type(certificate.lower_bound) is not Fraction
    ):
        return False
    try:
        loads = certificate_edge_loads(certificate)
        weights = augmented_edge_weights()
    except (AssertionError, IndexError, KeyError, TypeError, ValueError):
        return False
    if len(weights) != EDGE_COUNT:
        return False
    if any(
        load > weights[edge_id]
        for row in loads
        for edge_id, load in enumerate(row)
    ):
        return False
    contribution = sum(
        (path.contribution for path in certificate.paths), Fraction(0)
    )
    return certificate.lower_bound == contribution


@lru_cache(maxsize=1)
def direct_anchor_bound() -> Fraction:
    """Reproduce the old exact first-transition minimum inside this graph."""

    terms = []
    terminals = anchor_terminals()
    for atom in range(6):
        start = 2 * atom
        path = TerminalPath(start, start + 1, ())
        terms.append(analyze_path(ALL_BLOCKS, path, terminals[start].weight))
    result = sum((term.contribution for term in terms), Fraction(0))
    if result != Fraction(209, 2500):
        raise AssertionError("direct terminal paths lost the exact anchor bound")
    return result


def _dual_prices() -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    ordinary = [Fraction(0) for _ in range(EDGE_COUNT)]
    for edge_id in (0, 2, 8, 12, 14, 20):
        ordinary[edge_id] = Fraction(5)

    special = [Fraction(0) for _ in range(EDGE_COUNT)]
    for edge_id in (0, 2, 12, 14):
        special[edge_id] = Fraction(5)
    for edge_id in (8, 10, 20, 21, 22, 23, 24, 25):
        special[edge_id] = Fraction(5, 2)
    return tuple(ordinary), tuple(special)


@lru_cache(maxsize=1)
def build_catalog_dual() -> CatalogDualCertificate:
    """Build the exact two-row dual for all simple paths and simple cycles."""

    ordinary, special = _dual_prices()
    scaled_capacities = tuple(
        weight * CAPACITY_SCALE for weight in augmented_edge_weights()
    )
    ordinary_bound = sum(
        (capacity * price for capacity, price in zip(scaled_capacities, ordinary)),
        Fraction(0),
    )
    special_bound = sum(
        (capacity * price for capacity, price in zip(scaled_capacities, special)),
        Fraction(0),
    )
    scaled = ORDINARY_BLOCKS * ordinary_bound + special_bound
    certificate = CatalogDualCertificate(
        path_count=len(simple_terminal_paths()),
        cycle_count=len(simple_cycles(3, 4)),
        ordinary_prices=ordinary,
        special_prices=special,
        ordinary_scaled_bound=ordinary_bound,
        special_scaled_bound=special_bound,
        scaled_bound=scaled,
        bound=scaled / (CAPACITY_SCALE * FIBER_SIZE),
    )
    if not verify_catalog_dual(certificate):
        raise AssertionError("new simple-path catalog dual failed replay")
    return certificate


def verify_catalog_dual(certificate: CatalogDualCertificate) -> bool:
    """Check every path/cycle inequality against both exact block classes."""

    if (
        type(certificate) is not CatalogDualCertificate
        or type(certificate.path_count) is not int
        or type(certificate.cycle_count) is not int
        or type(certificate.ordinary_prices) is not tuple
        or type(certificate.special_prices) is not tuple
        or certificate.path_count != 622
        or certificate.cycle_count != 20
        or len(certificate.ordinary_prices) != EDGE_COUNT
        or len(certificate.special_prices) != EDGE_COUNT
        or any(
            type(value) is not Fraction or value < 0
            for value in (
                certificate.ordinary_prices + certificate.special_prices
            )
        )
        or any(
            type(value) is not Fraction
            for value in (
                certificate.ordinary_scaled_bound,
                certificate.special_scaled_bound,
                certificate.scaled_bound,
                certificate.bound,
            )
        )
    ):
        return False
    try:
        paths = simple_terminal_paths()
        cycles = simple_cycles(3, 4)
        weights = augmented_edge_weights()
    except (AssertionError, IndexError, KeyError, TypeError, ValueError):
        return False
    scaled_capacities = tuple(weight * CAPACITY_SCALE for weight in weights)
    if any(capacity.denominator != 1 for capacity in scaled_capacities):
        return False
    ordinary_bound = sum(
        (
            capacity * price
            for capacity, price in zip(
                scaled_capacities, certificate.ordinary_prices
            )
        ),
        Fraction(0),
    )
    special_bound = sum(
        (
            capacity * price
            for capacity, price in zip(
                scaled_capacities, certificate.special_prices
            )
        ),
        Fraction(0),
    )
    if (
        ordinary_bound != certificate.ordinary_scaled_bound
        or special_bound != certificate.special_scaled_bound
    ):
        return False

    for path in paths:
        try:
            edges = path_edge_ids(path)
            mismatches = path_block_mismatches(path)
        except (AssertionError, IndexError, KeyError, TypeError, ValueError):
            return False
        ordinary_cost = sum(
            (certificate.ordinary_prices[edge] for edge in edges), Fraction(0)
        )
        special_cost = sum(
            (certificate.special_prices[edge] for edge in edges), Fraction(0)
        )
        if any(mismatch > ordinary_cost for mismatch in mismatches[:ORDINARY_BLOCKS]):
            return False
        if mismatches[SPECIAL_BLOCK] > special_cost:
            return False

    if not _verify_ordinary_block_homogeneity(3, 4):
        return False
    for cycle in cycles:
        ordinary_cost = sum(
            (
                certificate.ordinary_prices[step.edge]
                for step in cycle
            ),
            Fraction(0),
        )
        special_cost = sum(
            (certificate.special_prices[step.edge] for step in cycle),
            Fraction(0),
        )
        try:
            ordinary_defect = _cycle_minimum_steps(3, 4, cycle, 0)[0]
            special_defect = _cycle_minimum_steps(
                3, 4, cycle, SPECIAL_BLOCK
            )[0]
        except (AssertionError, IndexError, KeyError, TypeError, ValueError):
            return False
        if ordinary_defect > ordinary_cost or special_defect > special_cost:
            return False

    scaled = ORDINARY_BLOCKS * ordinary_bound + special_bound
    return (
        certificate.ordinary_scaled_bound == 40
        and certificate.special_scaled_bound == 60
        and certificate.scaled_bound == scaled == 25020
        and certificate.bound
        == scaled / (CAPACITY_SCALE * FIBER_SIZE)
    )


def format_path_report(
    certificate: PathCertificate,
    dual: CatalogDualCertificate | None = None,
) -> str:
    lines = [
        "anchored structured horizon=2..4 anchor-to-anchor path dual",
        "  paths=%d certified lower bound=%s"
        % (len(certificate.paths), certificate.lower_bound),
        "  direct-anchor regression=%s" % direct_anchor_bound(),
    ]
    if dual is not None:
        lines.append(
            "  all-simple catalog paths=%d cycles=%d primal=dual=%s"
            % (dual.path_count, dual.cycle_count, dual.bound)
        )
    lines.append(
        "  scope: fixed-r2 structured 625-block/S5 ansatz; relaxation only"
    )
    return "\n".join(lines)


def main() -> int:
    print("ENTROPY-SELECTION anchor-to-anchor path dual")
    print("NON-CANONICAL / NON-FORMAL / NO CLAIM STATUS")
    print(format_path_report(build_path_certificate(), build_catalog_dual()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "ALL_BLOCKS",
    "AnchorTerminal",
    "CatalogDualCertificate",
    "PathAllocation",
    "PathCertificate",
    "TerminalPath",
    "analyze_path",
    "anchor_terminals",
    "augmented_edge_weights",
    "build_catalog_dual",
    "build_path_certificate",
    "certificate_edge_loads",
    "direct_anchor_bound",
    "format_path_report",
    "path_block_mismatches",
    "path_edge_ids",
    "simple_terminal_paths",
    "verify_catalog_dual",
    "verify_path_certificate",
]
