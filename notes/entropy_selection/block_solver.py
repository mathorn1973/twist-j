#!/usr/bin/env python3
"""Reduced exact-cylinder solvers for the entropy-selection recon.

NON-CANONICAL LOCAL ANALYSIS.  This module does not prove or disprove the
measurable entropy bridge.  It solves one explicit ansatz: on a finite
desubstituted Thue--Morse context, a source J-sector is sent to a target
pentagon.  Both affine maps over F_5 and all 120 unrestricted five-point
bijections are decided.

The solver never closes a supertile periodically.  Its vertices and roof
transitions are factors of the actual Thue--Morse language.  Cycles of the
Rauzy graph impose consistency of shared cylinder variables only.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from functools import lru_cache
from itertools import permutations
from typing import Iterable

try:
    from .lambda5 import j_orbits, j_permutation
    from .living import LivingAddress, LivingKernel, reconstruct
    from .morse import ContextEdge, ContextGraph, context_graph, last_symbol, supertile
except ImportError:  # Direct execution from this directory.
    from lambda5 import j_orbits, j_permutation  # type: ignore[no-redef]
    from living import LivingAddress, LivingKernel, reconstruct  # type: ignore[no-redef]
    from morse import (  # type: ignore[no-redef]
        ContextEdge,
        ContextGraph,
        context_graph,
        last_symbol,
        supertile,
    )


MODULUS = 5


@dataclass(frozen=True, slots=True)
class SourceSector:
    """One invariant source sector at a fixed mod-4 odometer phase."""

    kind: str
    orbit: int
    residue: int
    points: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class BlockCellAction:
    """Exact action of one dyadic supertile on a target pentagon."""

    level: int
    letter: int
    source_cell: int
    target_cell: int
    multiplier: int
    offset: int

    def apply_xi(self, xi: int) -> int:
        return (self.multiplier * xi + self.offset) % MODULUS


@dataclass(frozen=True, slots=True)
class AffineSection:
    """One solution ``xi_v = slopes[v] q + offsets[v]``."""

    root_slope: int
    root_offset: int
    slopes: tuple[int, ...]
    offsets: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class CellSection:
    """A context-consistent target cell selected from one root cell."""

    root_cell: int
    cells: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class PermutationSection:
    """One unrestricted five-point transfer section on the context graph."""

    root_permutation: tuple[int, ...]
    permutations: tuple[tuple[int, ...], ...]


@dataclass(frozen=True, slots=True)
class SolverReport:
    """Complete result for one level and one finite context width."""

    level: int
    width: int
    vertices: int
    edges: int
    source_delta: int
    source_non_singlets: int
    source_singlets: int
    target_non_singlets: int
    cell_consistent_non_singlets: int
    affine_consistent_non_singlets: int
    affine_solution_count: int
    root_slope_histogram: tuple[tuple[int, int], ...]
    permutation_cycle_cells: int
    permutation_fixed_cells: int
    permutation_cycle_solution_count: int
    permutation_fixed_solution_count: int
    singlet_consistent_root_values: tuple[int, ...]
    all_block_multipliers: tuple[int, ...]
    reduced_transfer_exists: bool


@lru_cache(maxsize=1)
def source_sectors() -> tuple[SourceSector, ...]:
    """Split J-orbits using the invariant orbit-position residue modulo 4.

    At a level-r boundary with r>=2, J^(2^r) preserves each returned sector.
    Every 20-cycle gives four oriented five-point sectors.  The four points
    of the unique 4-cycle and the zero fixed point give five singletons.
    """

    sectors: list[SourceSector] = []
    orbit_number = {4: 0, 20: 0}
    for cycle in j_orbits():
        length = len(cycle)
        if length == 20:
            number = orbit_number[20]
            orbit_number[20] += 1
            for residue in range(4):
                sectors.append(
                    SourceSector(
                        kind="five",
                        orbit=number,
                        residue=residue,
                        points=tuple(cycle[residue + 4 * q] for q in range(5)),
                    )
                )
        elif length == 4:
            number = orbit_number[4]
            orbit_number[4] += 1
            for residue, point in enumerate(cycle):
                sectors.append(
                    SourceSector(
                        kind="singleton-4cycle",
                        orbit=number,
                        residue=residue,
                        points=(point,),
                    )
                )
        elif length == 1:
            sectors.append(
                SourceSector(
                    kind="singleton-zero",
                    orbit=0,
                    residue=0,
                    points=(cycle[0],),
                )
            )
        else:
            raise AssertionError("unexpected J-orbit length")
    return tuple(sectors)


def source_delta(level: int) -> int:
    """Return the q increment of J^(2^level) on every five-sector."""

    if level < 2:
        raise ValueError("the mod-4 sector reduction starts at level 2")
    return pow(2, level - 2, MODULUS)


@lru_cache(maxsize=1)
def five_permutations() -> tuple[tuple[int, ...], ...]:
    """Return all 120 bijections of one source sector to one pentagon."""

    return tuple(permutations(range(MODULUS)))


def solve_permutation_cocycle(
    graph: ContextGraph,
    actions: Iterable[tuple[int, int]],
    delta: int,
) -> tuple[PermutationSection, ...]:
    """Solve ``X_v(q+delta)=T_e(X_u(q))`` for all root permutations.

    ``actions[e] = (alpha,b)`` represents ``T_e(x)=alpha*x+b``.  Keeping this
    graph solver independent of the living kernel permits positive synthetic
    regression tests of the equation orientation, not only empty instances.
    """

    if not 0 <= delta < MODULUS:
        raise ValueError("source increment must lie in F_5")
    rules = tuple(actions)
    if len(rules) != len(graph.edges):
        raise ValueError("one affine action is required per context edge")
    if any(alpha % MODULUS == 0 for alpha, _ in rules):
        raise ValueError("target edge actions must be bijective")

    def apply(edge_id: int, value: int) -> int:
        alpha, offset = rules[edge_id]
        return (alpha * value + offset) % MODULUS

    children: list[list[int]] = [[] for _ in graph.vertices]
    for vertex, edge_id in enumerate(graph.tree_edges):
        if edge_id is not None:
            children[graph.edges[edge_id].source].append(vertex)
    solutions = []
    for root_permutation in five_permutations():
        transfer: list[tuple[int, ...] | None] = [None] * len(graph.vertices)
        transfer[graph.root] = root_permutation
        queue = deque((graph.root,))
        while queue:
            source_vertex = queue.popleft()
            source_transfer = transfer[source_vertex]
            if source_transfer is None:
                raise AssertionError("permutation tree reached an unset vertex")
            for target_vertex in children[source_vertex]:
                edge_id = graph.tree_edges[target_vertex]
                if edge_id is None:
                    raise AssertionError("non-root tree vertex has no edge")
                target_transfer = tuple(
                    apply(edge_id, source_transfer[(q - delta) % MODULUS])
                    for q in range(MODULUS)
                )
                transfer[target_vertex] = target_transfer
                queue.append(target_vertex)
        resolved = tuple(value for value in transfer if value is not None)
        if len(resolved) != len(graph.vertices):
            raise AssertionError("permutation tree did not cover every vertex")
        consistent = all(
            resolved[edge.target][(q + delta) % MODULUS]
            == apply(edge.id, resolved[edge.source][q])
            for edge in graph.edges
            for q in range(MODULUS)
        )
        if consistent:
            solutions.append(
                PermutationSection(
                    root_permutation=root_permutation,
                    permutations=resolved,
                )
            )
    return tuple(solutions)


def verify_source_split(level: int) -> bool:
    """Check the sector census and the asserted J block action directly."""

    if level < 2:
        raise ValueError("the mod-4 sector reduction starts at level 2")
    sectors = source_sectors()
    five = tuple(sector for sector in sectors if len(sector.points) == 5)
    singles = tuple(sector for sector in sectors if len(sector.points) == 1)
    if len(five) != 624 or len(singles) != 5:
        return False
    j_map = j_permutation()
    exponent = 1 << level

    def advance(point: int) -> int:
        for _ in range(exponent):
            point = j_map[point]
        return point

    delta = source_delta(level)
    return all(
        advance(point) == sector.points[(q + delta) % MODULUS]
        for sector in five
        for q, point in enumerate(sector.points)
    ) and all(advance(sector.points[0]) == sector.points[0] for sector in singles)


class ReducedBlockSolver:
    """Exact solver backed by one reconstructed finite living kernel."""

    def __init__(self, model: LivingKernel | None = None) -> None:
        self.model = model if model is not None else reconstruct()
        self._block_cache: dict[tuple[int, int, int], BlockCellAction] = {}
        self._permutation_cache: dict[
            tuple[int, int, int, tuple[tuple[int, int], ...]],
            tuple[PermutationSection, ...],
        ] = {}

    def block_action(
        self, level: int, letter: int, source_cell: int
    ) -> BlockCellAction:
        """Return the exact affine action of ``sigma^level(letter)``."""

        if level < 0 or letter not in (0, 1):
            raise ValueError("invalid dyadic block")
        key = (level, letter, source_cell)
        cached = self._block_cache.get(key)
        if cached is not None:
            return cached
        source = self.model.pentagons[source_cell]
        images = tuple(
            self.model.apply_word(
                supertile(letter, level),
                LivingAddress(source.component, source.half, source.local, xi),
            )
            for xi in range(MODULUS)
        )
        target_cell = self.model.cell_id(
            images[0].component, images[0].half, images[0].cell
        )
        if any(
            self.model.cell_id(image.component, image.half, image.cell) != target_cell
            for image in images
        ):
            raise AssertionError("a block failed to preserve a target pentagon")
        offset = images[0].q
        multiplier = (images[1].q - offset) % MODULUS
        if multiplier == 0 or any(
            image.q != (multiplier * xi + offset) % MODULUS
            for xi, image in enumerate(images)
        ):
            raise AssertionError("block action is not affine over F_5")
        result = BlockCellAction(
            level=level,
            letter=letter,
            source_cell=source_cell,
            target_cell=target_cell,
            multiplier=multiplier,
            offset=offset,
        )
        self._block_cache[key] = result
        return result

    def edge_action(
        self, level: int, edge: ContextEdge, source_cell: int
    ) -> BlockCellAction:
        return self.block_action(level, edge.current, source_cell)

    def _propagate_cells(
        self, level: int, graph: ContextGraph, root_cell: int
    ) -> CellSection | None:
        cells: list[int | None] = [None] * len(graph.vertices)
        cells[graph.root] = root_cell
        outgoing_edges: list[list[int]] = [[] for _ in graph.vertices]
        for edge in graph.edges:
            outgoing_edges[edge.source].append(edge.id)
        queue = deque((graph.root,))
        while queue:
            source_vertex = queue.popleft()
            source_cell = cells[source_vertex]
            if source_cell is None:
                raise AssertionError("tree propagation reached an unset cell")
            for edge_id in outgoing_edges[source_vertex]:
                edge = graph.edges[edge_id]
                if graph.tree_edges[edge.target] != edge_id:
                    continue
                target_cell = self.edge_action(level, edge, source_cell).target_cell
                if cells[edge.target] is not None:
                    raise AssertionError("context tree assigned a vertex twice")
                cells[edge.target] = target_cell
                queue.append(edge.target)
        if any(cell is None for cell in cells):
            raise AssertionError("context tree did not cover every vertex")
        resolved = tuple(int(cell) for cell in cells)
        for edge in graph.edges:
            if self.edge_action(level, edge, resolved[edge.source]).target_cell != resolved[
                edge.target
            ]:
                return None
        return CellSection(root_cell=root_cell, cells=resolved)

    def cell_sections(
        self, level: int, graph: ContextGraph
    ) -> tuple[CellSection, ...]:
        """Return all context-consistent cell sections at one scale."""

        root_previous = graph.vertices[graph.root][0]
        root_half = last_symbol(root_previous, level)
        sections = []
        for root_cell in self.model.cells_by_half[root_half]:
            section = self._propagate_cells(level, graph, root_cell)
            if section is not None:
                sections.append(section)
        return tuple(sections)

    def affine_sections(
        self,
        level: int,
        graph: ContextGraph,
        cell_section: CellSection,
    ) -> tuple[AffineSection, ...]:
        """Solve all root-normalized affine F_5 transfer equations.

        Both root slope and root offset are enumerated.  Thus the result stays
        valid if a future scale has a non-translation target block; at the
        present levels all multipliers are checked rather than assumed to be 1.
        """

        delta = source_delta(level)
        solutions: list[AffineSection] = []
        tree_order = sorted(
            (edge_id, vertex)
            for vertex, edge_id in enumerate(graph.tree_edges)
            if edge_id is not None
        )
        # Edge identifiers happen to follow factor order, not tree depth.
        # Propagate with a queue to avoid depending on that order.
        children: list[list[int]] = [[] for _ in graph.vertices]
        for vertex, edge_id in enumerate(graph.tree_edges):
            if edge_id is not None:
                children[graph.edges[edge_id].source].append(vertex)
        del tree_order

        for root_slope in range(1, MODULUS):
            for root_offset in range(MODULUS):
                slopes: list[int | None] = [None] * len(graph.vertices)
                offsets: list[int | None] = [None] * len(graph.vertices)
                slopes[graph.root] = root_slope
                offsets[graph.root] = root_offset
                queue = deque((graph.root,))
                while queue:
                    source_vertex = queue.popleft()
                    source_slope = slopes[source_vertex]
                    source_offset = offsets[source_vertex]
                    if source_slope is None or source_offset is None:
                        raise AssertionError("affine tree reached an unset vertex")
                    for target_vertex in children[source_vertex]:
                        edge_id = graph.tree_edges[target_vertex]
                        if edge_id is None:
                            raise AssertionError("non-root tree vertex has no edge")
                        edge = graph.edges[edge_id]
                        action = self.edge_action(
                            level, edge, cell_section.cells[source_vertex]
                        )
                        target_slope = action.multiplier * source_slope % MODULUS
                        target_offset = (
                            action.multiplier * source_offset
                            + action.offset
                            - target_slope * delta
                        ) % MODULUS
                        slopes[target_vertex] = target_slope
                        offsets[target_vertex] = target_offset
                        queue.append(target_vertex)
                resolved_slopes = tuple(int(value) for value in slopes)
                resolved_offsets = tuple(int(value) for value in offsets)
                consistent = True
                for edge in graph.edges:
                    action = self.edge_action(
                        level, edge, cell_section.cells[edge.source]
                    )
                    expected_slope = (
                        action.multiplier * resolved_slopes[edge.source]
                    ) % MODULUS
                    expected_offset = (
                        action.multiplier * resolved_offsets[edge.source]
                        + action.offset
                        - expected_slope * delta
                    ) % MODULUS
                    if (
                        resolved_slopes[edge.target] != expected_slope
                        or resolved_offsets[edge.target] != expected_offset
                    ):
                        consistent = False
                        break
                if consistent:
                    solutions.append(
                        AffineSection(
                            root_slope=root_slope,
                            root_offset=root_offset,
                            slopes=resolved_slopes,
                            offsets=resolved_offsets,
                        )
                    )
        return tuple(solutions)

    def permutation_sections(
        self,
        level: int,
        graph: ContextGraph,
        cell_section: CellSection,
        delta: int,
    ) -> tuple[PermutationSection, ...]:
        """Solve the same section with an unrestricted root permutation.

        ``delta`` is 1..4 for a source five-cycle and 0 for the five labeled
        fixed points.  This 120-state enumeration prevents an affine ansatz
        from being mistaken for the full cell-sector decision problem.
        """

        if not 0 <= delta < MODULUS:
            raise ValueError("source increment must lie in F_5")
        signature = tuple(
            (
                action.multiplier,
                action.offset,
            )
            for edge in graph.edges
            for action in (
                self.edge_action(
                    level, edge, cell_section.cells[edge.source]
                ),
            )
        )
        cache_key = (level, graph.width, delta, signature)
        cached = self._permutation_cache.get(cache_key)
        if cached is not None:
            return cached
        result = solve_permutation_cocycle(graph, signature, delta)
        self._permutation_cache[cache_key] = result
        return result

    def singlet_root_values(
        self, level: int, graph: ContextGraph
    ) -> tuple[int, ...]:
        """Solve the five singleton-source sections in the target singlet."""

        root_previous = graph.vertices[graph.root][0]
        root_half = last_symbol(root_previous, level)
        root_cell = self.model.component_cells(
            self.model.singlet_component, root_half
        )[0]
        cell_section = self._propagate_cells(level, graph, root_cell)
        if cell_section is None:
            return ()

        children: list[list[int]] = [[] for _ in graph.vertices]
        for vertex, edge_id in enumerate(graph.tree_edges):
            if edge_id is not None:
                children[graph.edges[edge_id].source].append(vertex)
        survivors = []
        for root_value in range(MODULUS):
            values: list[int | None] = [None] * len(graph.vertices)
            values[graph.root] = root_value
            queue = deque((graph.root,))
            while queue:
                source_vertex = queue.popleft()
                source_value = values[source_vertex]
                if source_value is None:
                    raise AssertionError("singlet tree reached an unset vertex")
                for target_vertex in children[source_vertex]:
                    edge_id = graph.tree_edges[target_vertex]
                    if edge_id is None:
                        raise AssertionError("non-root tree vertex has no edge")
                    edge = graph.edges[edge_id]
                    action = self.edge_action(
                        level, edge, cell_section.cells[source_vertex]
                    )
                    values[target_vertex] = action.apply_xi(source_value)
                    queue.append(target_vertex)
            resolved = tuple(int(value) for value in values)
            if all(
                self.edge_action(
                    level, edge, cell_section.cells[edge.source]
                ).apply_xi(resolved[edge.source])
                == resolved[edge.target]
                for edge in graph.edges
            ):
                survivors.append(root_value)
        return tuple(survivors)

    def report(self, level: int, width: int) -> SolverReport:
        """Run the complete reduced exact-context decision procedure."""

        if level < 2:
            raise ValueError("the reduced solver starts at level 2")
        graph = context_graph(width)
        if not verify_source_split(level):
            raise AssertionError("source sector decomposition failed")
        source = source_sectors()
        source_non_singlets = sum(len(sector.points) == 5 for sector in source)
        source_singlets = sum(len(sector.points) == 1 for sector in source)
        root_previous = graph.vertices[graph.root][0]
        root_half = last_symbol(root_previous, level)
        target_non_singlets = sum(
            self.model.pentagons[cell].component != self.model.singlet_component
            for cell in self.model.cells_by_half[root_half]
        )

        sections = self.cell_sections(level, graph)
        nonsinglet_sections = tuple(
            section
            for section in sections
            if self.model.pentagons[section.root_cell].component
            != self.model.singlet_component
        )
        affine_by_cell = tuple(
            (section, self.affine_sections(level, graph, section))
            for section in nonsinglet_sections
        )
        affine_consistent = sum(bool(solutions) for _, solutions in affine_by_cell)
        slope_histogram: Counter[int] = Counter()
        affine_solution_count = 0
        for _, solutions in affine_by_cell:
            affine_solution_count += len(solutions)
            slope_histogram.update(solution.root_slope for solution in solutions)

        permutation_cycle = tuple(
            (
                section,
                self.permutation_sections(
                    level, graph, section, source_delta(level)
                ),
            )
            for section in sections
        )
        permutation_fixed = tuple(
            (section, self.permutation_sections(level, graph, section, 0))
            for section in sections
        )
        cycle_compatible_cells = {
            section.root_cell
            for section, solutions in permutation_cycle
            if solutions
        }
        fixed_compatible_cells = {
            section.root_cell
            for section, solutions in permutation_fixed
            if solutions
        }
        all_root_cells = {section.root_cell for section in sections}
        target_root_cells = set(self.model.cells_by_half[root_half])
        assignment_exists = (
            all_root_cells == target_root_cells
            and any(
                all_root_cells - {fixed_cell} <= cycle_compatible_cells
                for fixed_cell in fixed_compatible_cells
            )
        )

        singlet_values = self.singlet_root_values(level, graph)
        multipliers = {
            self.edge_action(level, edge, section.cells[edge.source]).multiplier
            for section in sections
            for edge in graph.edges
        }
        reduced_transfer_exists = assignment_exists
        return SolverReport(
            level=level,
            width=width,
            vertices=len(graph.vertices),
            edges=len(graph.edges),
            source_delta=source_delta(level),
            source_non_singlets=source_non_singlets,
            source_singlets=source_singlets,
            target_non_singlets=target_non_singlets,
            cell_consistent_non_singlets=len(nonsinglet_sections),
            affine_consistent_non_singlets=affine_consistent,
            affine_solution_count=affine_solution_count,
            root_slope_histogram=tuple(sorted(slope_histogram.items())),
            permutation_cycle_cells=len(cycle_compatible_cells),
            permutation_fixed_cells=len(fixed_compatible_cells),
            permutation_cycle_solution_count=sum(
                len(solutions) for _, solutions in permutation_cycle
            ),
            permutation_fixed_solution_count=sum(
                len(solutions) for _, solutions in permutation_fixed
            ),
            singlet_consistent_root_values=singlet_values,
            all_block_multipliers=tuple(sorted(multipliers)),
            reduced_transfer_exists=reduced_transfer_exists,
        )


def format_report(report: SolverReport) -> str:
    """Render a stable, compact, human-auditable report."""

    return "\n".join(
        (
            "level=%d width=%d vertices=%d edges=%d delta=%d"
            % (
                report.level,
                report.width,
                report.vertices,
                report.edges,
                report.source_delta,
            ),
            "  source sectors: five=%d singleton=%d; target five-cells=%d"
            % (
                report.source_non_singlets,
                report.source_singlets,
                report.target_non_singlets,
            ),
            "  cell sections=%d/%d; affine sections=%d/%d; affine maps=%d"
            % (
                report.cell_consistent_non_singlets,
                report.target_non_singlets,
                report.affine_consistent_non_singlets,
                report.target_non_singlets,
                report.affine_solution_count,
            ),
            "  root-slope histogram=%s; block multipliers=%s"
            % (dict(report.root_slope_histogram), report.all_block_multipliers),
            "  unrestricted S5 cells: cycle=%d/625 fixed=%d/625; maps=(%d,%d)"
            % (
                report.permutation_cycle_cells,
                report.permutation_fixed_cells,
                report.permutation_cycle_solution_count,
                report.permutation_fixed_solution_count,
            ),
            "  singlet root values=%s (%d/5)"
            % (
                report.singlet_consistent_root_values,
                len(report.singlet_consistent_root_values),
            ),
            "  REDUCED EXACT-CONTEXT TRANSFER %s"
            % ("SURVIVES" if report.reduced_transfer_exists else "EMPTY"),
        )
    )


__all__ = [
    "AffineSection",
    "BlockCellAction",
    "CellSection",
    "PermutationSection",
    "ReducedBlockSolver",
    "SolverReport",
    "SourceSector",
    "format_report",
    "five_permutations",
    "source_delta",
    "source_sectors",
    "solve_permutation_cocycle",
    "verify_source_split",
]
