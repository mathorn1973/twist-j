#!/usr/bin/env python3
"""Growing-context finite-horizon optimizer for entropy selection.

NON-CANONICAL LOCAL ANALYSIS.  Boundary bijections are represented exactly as
625 source five-blocks matched to 625 target pentagons, with one internal S_5
permutation per block.  Adjacent-level costs use exact Thue--Morse cylinder
weights and the joint two-child refinement incidence.

The optimizer is coordinate-exact for the declared finite horizon: with all
neighboring boundary maps fixed, each update maximizes weighted pointwise
agreement by an exact sparse bipartite matching.  It is not a certificate of
the global optimum, an infinite compatible chain, or a measurable selector.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import lcm
from typing import Iterable

try:
    from .block_solver import ReducedBlockSolver, five_permutations, source_sectors
    from .collars import (
        CollarGraph,
        CollarSpec,
        collar_graph,
        refinement_incidence,
    )
    from .lambda5 import SIZE, j_permutation
    from .living import LivingKernel, reconstruct
    from .morse import last_symbol
except ImportError:  # Direct execution from this directory.
    from block_solver import (  # type: ignore[no-redef]
        ReducedBlockSolver,
        five_permutations,
        source_sectors,
    )
    from collars import (  # type: ignore[no-redef]
        CollarGraph,
        CollarSpec,
        collar_graph,
        refinement_incidence,
    )
    from lambda5 import SIZE, j_permutation  # type: ignore[no-redef]
    from living import LivingKernel, reconstruct  # type: ignore[no-redef]
    from morse import last_symbol  # type: ignore[no-redef]


MODULUS = 5
BLOCK_COUNT = 625
Permutation5 = tuple[int, int, int, int, int]


@dataclass(frozen=True, slots=True)
class SourceBlock:
    id: int
    kind: str
    points: tuple[int, int, int, int, int]


@lru_cache(maxsize=1)
def source_blocks() -> tuple[SourceBlock, ...]:
    """Return the 624 J five-sectors and the residual J^(2^r)-fixed block."""

    five = tuple(sector for sector in source_sectors() if len(sector.points) == 5)
    singles = sorted(
        (sector.points[0] for sector in source_sectors() if len(sector.points) == 1)
    )
    if len(five) != 624 or len(singles) != 5:
        raise AssertionError("unexpected source-sector census")
    blocks = [
        SourceBlock(index, "J-five-cycle", sector.points)
        for index, sector in enumerate(five)
    ]
    blocks.append(
        SourceBlock(
            624,
            "J-power-fixed-block",
            tuple(singles),  # type: ignore[arg-type]
        )
    )
    return tuple(blocks)


@dataclass(frozen=True, slots=True)
class StructuredMap:
    """One sector/cell preserving 3125-point boundary bijection."""

    half: int
    cells: tuple[int, ...]
    permutations: tuple[Permutation5, ...]

    def __post_init__(self) -> None:
        if self.half not in (0, 1):
            raise ValueError("living half must be 0 or 1")
        if len(self.cells) != BLOCK_COUNT or len(self.permutations) != BLOCK_COUNT:
            raise ValueError("a structured boundary map needs 625 source blocks")
        if len(set(self.cells)) != BLOCK_COUNT:
            raise ValueError("target cells must form a bijective assignment")
        expected = set(range(MODULUS))
        if any(set(permutation) != expected for permutation in self.permutations):
            raise ValueError("every internal block map must lie in S_5")

    def agreement(self, other: StructuredMap) -> int:
        """Count equal target states on the full 3125-point source fiber."""

        if self.half != other.half:
            return 0
        return sum(
            sum(left_q == right_q for left_q, right_q in zip(left, right))
            for left_cell, right_cell, left, right in zip(
                self.cells,
                other.cells,
                self.permutations,
                other.permutations,
            )
            if left_cell == right_cell
        )

    def distance(self, other: StructuredMap) -> Fraction:
        return Fraction(SIZE - self.agreement(other), SIZE)


@dataclass(frozen=True, slots=True)
class BoundaryFamily:
    level: int
    spec: CollarSpec
    maps: tuple[StructuredMap, ...]
    origin: str
    tree_edges: tuple[int, ...] = ()


@dataclass(frozen=True, slots=True)
class FamilyReport:
    level: int
    spec: CollarSpec
    vertices: int
    edges: int
    origin: str
    selected_tree_edges: int
    selected_tree_weight: Fraction
    zero_defect_edges: int
    zero_defect_weight: Fraction
    conditional_roof_defect: Fraction
    full_equation_error: Fraction
    maximum_edge_defect: Fraction


@dataclass(frozen=True, slots=True)
class RefinementReport:
    lower_level: int
    upper_level: int
    lower_spec: CollarSpec
    upper_spec: CollarSpec
    atoms: int
    first_child_distance: Fraction
    second_child_distance: Fraction
    distance: Fraction
    maximum_branch_distance: Fraction


@dataclass(frozen=True, slots=True)
class HorizonSweep:
    number: int
    changed_nodes: int
    objective_before: Fraction
    objective_after: Fraction


@dataclass(frozen=True, slots=True)
class HorizonReport:
    minimum_level: int
    maximum_level: int
    specs: tuple[tuple[int, CollarSpec], ...]
    initial_objective: Fraction
    final_objective: Fraction
    sweeps: tuple[HorizonSweep, ...]
    refinements: tuple[RefinementReport, ...]
    family_reports: tuple[FamilyReport, ...]
    maximum_matching_component: int
    minimum_level_frozen: bool


def default_collar(level: int) -> CollarSpec:
    """Grow alternate left/right radii while retaining the previous letter."""

    if level < 2:
        raise ValueError("entropy tower levels start at 2")
    length = level
    left = length // 2
    right = length - left - 1
    return CollarSpec(left, right)


def _permutation_power(permutation: tuple[int, ...], exponent: int) -> tuple[int, ...]:
    result = tuple(range(len(permutation)))
    base = permutation
    while exponent:
        if exponent & 1:
            result = tuple(base[result[index]] for index in range(len(base)))
        base = tuple(base[base[index]] for index in range(len(base)))
        exponent >>= 1
    return result


class GrowingContextSolver:
    """Exact structured cocycle operations and finite-family diagnostics."""

    def __init__(self, model: LivingKernel | None = None) -> None:
        self.model = model if model is not None else reconstruct()
        self.reduced = ReducedBlockSolver(self.model)
        self._j_power_cache: dict[int, tuple[int, ...]] = {}
        self._source_position_cache: dict[
            tuple[int, int], tuple[int, ...]
        ] = {}
        self._inverse_cell_cache: dict[
            tuple[int, int, int], dict[int, tuple[int, int, int]]
        ] = {}

    def _j_power(self, level: int) -> tuple[int, ...]:
        cached = self._j_power_cache.get(level)
        if cached is None:
            cached = _permutation_power(j_permutation(), 1 << level)
            self._j_power_cache[level] = cached
        return cached

    def _source_positions(self, level: int, block: SourceBlock) -> tuple[int, ...]:
        key = (level, block.id)
        cached = self._source_position_cache.get(key)
        if cached is not None:
            return cached
        positions = {point: position for position, point in enumerate(block.points)}
        j_power = self._j_power(level)
        result = tuple(positions[j_power[point]] for point in block.points)
        self._source_position_cache[key] = result
        return result

    def _inverse_cells(
        self, level: int, letter: int, source_half: int
    ) -> dict[int, tuple[int, int, int]]:
        """Map target cell to ``(source_cell, inverse_multiplier, offset)``."""

        key = (level, letter, source_half)
        cached = self._inverse_cell_cache.get(key)
        if cached is not None:
            return cached
        inverse: dict[int, tuple[int, int, int]] = {}
        for source_cell in self.model.cells_by_half[source_half]:
            action = self.reduced.block_action(level, letter, source_cell)
            if action.target_cell in inverse:
                raise AssertionError("block cell action is not injective")
            inverse[action.target_cell] = (
                source_cell,
                pow(action.multiplier, -1, MODULUS),
                action.offset,
            )
        if len(inverse) != BLOCK_COUNT:
            raise AssertionError("block cell action does not cover a living half")
        self._inverse_cell_cache[key] = inverse
        return inverse

    def validate_map(self, mapping: StructuredMap) -> bool:
        return set(mapping.cells) == set(self.model.cells_by_half[mapping.half])

    def lexicographic_map(self, level: int, previous: int) -> StructuredMap:
        """The transparent ordered seed used by the earlier tower baseline."""

        half = last_symbol(previous, level)
        nonsinglet = tuple(
            cell
            for cell in self.model.cells_by_half[half]
            if self.model.pentagons[cell].component != self.model.singlet_component
        )
        singlet = self.model.component_cells(self.model.singlet_component, half)[0]
        result = StructuredMap(
            half=half,
            cells=nonsinglet + (singlet,),
            permutations=(tuple(range(MODULUS)),) * BLOCK_COUNT,  # type: ignore[arg-type]
        )
        if not self.validate_map(result):
            raise AssertionError("lexicographic structured map is not bijective")
        return result

    def decode(self, mapping: StructuredMap) -> tuple[int, ...]:
        """Materialize the structured map as a 3125-state target tuple."""

        result = [-1] * SIZE
        for block, cell_id, permutation in zip(
            source_blocks(), mapping.cells, mapping.permutations
        ):
            cell = self.model.pentagons[cell_id]
            for position, point in enumerate(block.points):
                result[point] = cell.state_by_q[permutation[position]]
        if -1 in result or set(result) != set(self.model.halves[mapping.half]):
            raise AssertionError("decoded structured map is not a fiber bijection")
        return tuple(result)

    def advance(
        self, mapping: StructuredMap, level: int, letter: int
    ) -> StructuredMap:
        """Return ``Y`` satisfying ``Y J^(2^r) = Phi_letter^r X``."""

        target_cells = [-1] * BLOCK_COUNT
        target_permutations: list[Permutation5 | None] = [None] * BLOCK_COUNT
        for block, source_cell, permutation in zip(
            source_blocks(), mapping.cells, mapping.permutations
        ):
            action = self.reduced.block_action(level, letter, source_cell)
            source_positions = self._source_positions(level, block)
            target_permutation = [-1] * MODULUS
            for old_position, new_position in enumerate(source_positions):
                target_permutation[new_position] = action.apply_xi(
                    permutation[old_position]
                )
            target_cells[block.id] = action.target_cell
            target_permutations[block.id] = tuple(target_permutation)  # type: ignore[assignment]
        target_half = self.model.pentagons[target_cells[0]].half
        result = StructuredMap(
            half=target_half,
            cells=tuple(target_cells),
            permutations=tuple(target_permutations),  # type: ignore[arg-type]
        )
        if not self.validate_map(result):
            raise AssertionError("advanced structured map is not bijective")
        return result

    def retreat(
        self,
        mapping: StructuredMap,
        level: int,
        letter: int,
        source_half: int,
    ) -> StructuredMap:
        """Invert :meth:`advance` for one declared source half."""

        inverse_cells = self._inverse_cells(level, letter, source_half)
        source_cells = [-1] * BLOCK_COUNT
        source_permutations: list[Permutation5 | None] = [None] * BLOCK_COUNT
        for block, target_cell, target_permutation in zip(
            source_blocks(), mapping.cells, mapping.permutations
        ):
            source_cell, inverse_multiplier, offset = inverse_cells[target_cell]
            source_positions = self._source_positions(level, block)
            source_permutation = [-1] * MODULUS
            for old_position, new_position in enumerate(source_positions):
                source_permutation[old_position] = (
                    inverse_multiplier
                    * (target_permutation[new_position] - offset)
                ) % MODULUS
            source_cells[block.id] = source_cell
            source_permutations[block.id] = tuple(source_permutation)  # type: ignore[assignment]
        result = StructuredMap(
            half=source_half,
            cells=tuple(source_cells),
            permutations=tuple(source_permutations),  # type: ignore[arg-type]
        )
        if not self.validate_map(result) or self.advance(result, level, letter) != mapping:
            raise AssertionError("structured block retreat failed roundtrip")
        return result

    def validate_family(self, family: BoundaryFamily) -> bool:
        graph = collar_graph(family.spec)
        if family.level < 2 or len(family.maps) != len(graph.vertices):
            return False
        for word, mapping in zip(graph.vertices, family.maps):
            previous = word[family.spec.left - 1]
            expected_half = last_symbol(previous, family.level)
            if mapping.half != expected_half or not self.validate_map(mapping):
                return False
        return True

    def lexicographic_family(self, level: int, spec: CollarSpec) -> BoundaryFamily:
        graph = collar_graph(spec)
        family = BoundaryFamily(
            level=level,
            spec=spec,
            maps=tuple(
                self.lexicographic_map(level, word[spec.left - 1])
                for word in graph.vertices
            ),
            origin="lexicographic",
        )
        if not self.validate_family(family):
            raise AssertionError("lexicographic family failed validation")
        return family

    @staticmethod
    def maximum_weight_tree(graph: CollarGraph) -> tuple[int, ...]:
        """Kruskal tree maximizing the exact total cylinder weight."""

        parent = list(range(len(graph.vertices)))

        def root(vertex: int) -> int:
            while parent[vertex] != vertex:
                parent[vertex] = parent[parent[vertex]]
                vertex = parent[vertex]
            return vertex

        selected = []
        for edge in sorted(
            graph.edges,
            key=lambda item: (-item.weight, item.word, item.id),
        ):
            left = root(edge.source)
            right = root(edge.target)
            if left == right:
                continue
            parent[left] = right
            selected.append(edge.id)
        if len(selected) != len(graph.vertices) - 1:
            raise AssertionError("collar graph is not connected")
        return tuple(sorted(selected))

    def tree_family(self, level: int, spec: CollarSpec) -> BoundaryFamily:
        """Satisfy a maximum-weight spanning tree of context equations exactly."""

        graph = collar_graph(spec)
        tree_edges = self.maximum_weight_tree(graph)
        adjacency: list[list[tuple[int, int]]] = [[] for _ in graph.vertices]
        for edge_id in tree_edges:
            edge = graph.edges[edge_id]
            adjacency[edge.source].append((edge_id, edge.target))
            adjacency[edge.target].append((edge_id, edge.source))
        maps: list[StructuredMap | None] = [None] * len(graph.vertices)
        root = 0
        maps[root] = self.lexicographic_map(
            level, graph.vertices[root][spec.left - 1]
        )
        queue = deque((root,))
        while queue:
            vertex = queue.popleft()
            current_map = maps[vertex]
            if current_map is None:
                raise AssertionError("tree reached an unset context map")
            for edge_id, neighbor in adjacency[vertex]:
                if maps[neighbor] is not None:
                    continue
                edge = graph.edges[edge_id]
                if edge.source == vertex:
                    maps[neighbor] = self.advance(current_map, level, edge.current)
                else:
                    source_word = graph.vertices[edge.source]
                    source_half = last_symbol(source_word[spec.left - 1], level)
                    maps[neighbor] = self.retreat(
                        current_map,
                        level,
                        edge.current,
                        source_half,
                    )
                queue.append(neighbor)
        family = BoundaryFamily(
            level=level,
            spec=spec,
            maps=tuple(maps),  # type: ignore[arg-type]
            origin="maximum-weight-tree",
            tree_edges=tree_edges,
        )
        if not self.validate_family(family):
            raise AssertionError("tree family failed validation")
        if any(self.edge_defect(family, edge_id) for edge_id in tree_edges):
            raise AssertionError("selected tree equation is not exact")
        return family

    def edge_defect(self, family: BoundaryFamily, edge_id: int) -> Fraction:
        graph = collar_graph(family.spec)
        edge = graph.edges[edge_id]
        expected = self.advance(
            family.maps[edge.source], family.level, edge.current
        )
        return expected.distance(family.maps[edge.target])

    def family_report(self, family: BoundaryFamily) -> FamilyReport:
        graph = collar_graph(family.spec)
        defects = tuple(self.edge_defect(family, edge.id) for edge in graph.edges)
        conditional = sum(
            (edge.weight * defect for edge, defect in zip(graph.edges, defects)),
            Fraction(0),
        )
        zero_weight = sum(
            (
                edge.weight
                for edge, defect in zip(graph.edges, defects)
                if defect == 0
            ),
            Fraction(0),
        )
        return FamilyReport(
            level=family.level,
            spec=family.spec,
            vertices=len(graph.vertices),
            edges=len(graph.edges),
            origin=family.origin,
            selected_tree_edges=len(family.tree_edges),
            selected_tree_weight=sum(
                (graph.edges[edge_id].weight for edge_id in family.tree_edges),
                Fraction(0),
            ),
            zero_defect_edges=sum(defect == 0 for defect in defects),
            zero_defect_weight=zero_weight,
            conditional_roof_defect=conditional,
            full_equation_error=conditional / (1 << family.level),
            maximum_edge_defect=max(defects, default=Fraction(0)),
        )

    def refinement_report(
        self, upper: BoundaryFamily, lower: BoundaryFamily
    ) -> RefinementReport:
        if upper.level != lower.level + 1:
            raise ValueError("refinement families must be on adjacent levels")
        incidence = refinement_incidence(upper.spec, lower.spec)
        upper_graph = collar_graph(upper.spec)
        lower_graph = collar_graph(lower.spec)
        upper_id = {word: index for index, word in enumerate(upper_graph.vertices)}
        lower_id = {word: index for index, word in enumerate(lower_graph.vertices)}
        first = Fraction(0)
        second = Fraction(0)
        maximum = Fraction(0)
        for atom in incidence.atoms:
            upper_map = upper.maps[upper_id[atom.parent]]
            child0 = lower.maps[lower_id[atom.child0]]
            child1 = lower.maps[lower_id[atom.child1]]
            distance0 = upper_map.distance(child0)
            current = atom.parent[upper.spec.left]
            midpoint = self.advance(upper_map, lower.level, current)
            distance1 = midpoint.distance(child1)
            first += atom.branch_weight * distance0
            second += atom.branch_weight * distance1
            maximum = max(maximum, distance0, distance1)
        return RefinementReport(
            lower_level=lower.level,
            upper_level=upper.level,
            lower_spec=lower.spec,
            upper_spec=upper.spec,
            atoms=len(incidence.atoms),
            first_child_distance=first,
            second_child_distance=second,
            distance=first + second,
            maximum_branch_distance=maximum,
        )


class FiniteHorizonOptimizer:
    """Coordinate descent for an exact weighted growing-context horizon.

    The minimum level is an anchored boundary by default.  Setting
    ``freeze_minimum=False`` instead optimizes every level of the finite
    horizon; the latter is a sensitivity diagnostic, not an inverse-limit
    boundary condition.
    """

    def __init__(
        self,
        minimum_level: int = 2,
        maximum_level: int = 5,
        solver: GrowingContextSolver | None = None,
        seed: str = "lexicographic",
        lift_phase: int = 0,
        freeze_minimum: bool = True,
    ) -> None:
        if minimum_level < 2 or maximum_level <= minimum_level:
            raise ValueError("finite horizon needs at least two levels from level 2")
        self.solver = solver if solver is not None else GrowingContextSolver()
        self.minimum_level = minimum_level
        self.maximum_level = maximum_level
        self.specs = {
            level: default_collar(level)
            for level in range(minimum_level, maximum_level + 1)
        }
        if seed == "lexicographic":
            seed_family = self.solver.lexicographic_family(
                minimum_level, self.specs[minimum_level]
            )
        elif seed == "tree":
            seed_family = self.solver.tree_family(
                minimum_level, self.specs[minimum_level]
            )
        else:
            raise ValueError("seed must be 'lexicographic' or 'tree'")
        if lift_phase not in (0, 1):
            raise ValueError("lift_phase must be 0 or 1")
        self.seed = seed
        self.lift_phase = lift_phase
        self.freeze_minimum = freeze_minimum
        self.maps: dict[int, list[StructuredMap]] = {
            minimum_level: list(seed_family.maps)
        }
        self.maximum_matching_component = 0
        for level in range(minimum_level + 1, maximum_level + 1):
            self.maps[level] = list(self._child_lift(level, lift_phase))

    def family(self, level: int) -> BoundaryFamily:
        return BoundaryFamily(
            level=level,
            spec=self.specs[level],
            maps=tuple(self.maps[level]),
            origin=(
                "fixed-%s-seed" % self.seed
                if level == self.minimum_level and self.freeze_minimum
                else "finite-horizon-coordinate"
            ),
        )

    def _child_lift(
        self, level: int, phase: int
    ) -> tuple[StructuredMap, ...]:
        upper_spec = self.specs[level]
        lower_spec = self.specs[level - 1]
        incidence = refinement_incidence(upper_spec, lower_spec)
        lower_graph = collar_graph(lower_spec)
        lower_id = {word: index for index, word in enumerate(lower_graph.vertices)}
        by_parent: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
        for atom in incidence.atoms:
            by_parent.setdefault(atom.parent, set()).add(
                (atom.child0, atom.child1)[phase]
            )
        result = []
        for parent in collar_graph(upper_spec).vertices:
            children = by_parent[parent]
            if len(children) != 1:
                raise ValueError("chosen collar schedule has an ambiguous lift")
            child = next(iter(children))
            lower_map = self.maps[level - 1][lower_id[child]]
            if phase == 0:
                result.append(lower_map)
            else:
                source_half = last_symbol(parent[upper_spec.left - 1], level)
                result.append(
                    self.solver.retreat(
                        lower_map,
                        level - 1,
                        parent[upper_spec.left],
                        source_half,
                    )
                )
        return tuple(result)

    def objective(self) -> Fraction:
        return sum(
            (
                self.solver.refinement_report(
                    self.family(level + 1), self.family(level)
                ).distance
                for level in range(self.minimum_level, self.maximum_level)
            ),
            Fraction(0),
        )

    def _votes(
        self, level: int, word: tuple[int, ...]
    ) -> tuple[tuple[Fraction, StructuredMap], ...]:
        votes: list[tuple[Fraction, StructuredMap]] = []
        spec = self.specs[level]
        if level > self.minimum_level:
            lower_spec = self.specs[level - 1]
            lower_graph = collar_graph(lower_spec)
            lower_id = {context: index for index, context in enumerate(lower_graph.vertices)}
            source_half = last_symbol(word[spec.left - 1], level)
            for atom in refinement_incidence(spec, lower_spec).atoms:
                if atom.parent != word:
                    continue
                child0 = self.maps[level - 1][lower_id[atom.child0]]
                child1 = self.maps[level - 1][lower_id[atom.child1]]
                votes.append((atom.branch_weight, child0))
                votes.append(
                    (
                        atom.branch_weight,
                        self.solver.retreat(
                            child1,
                            level - 1,
                            word[spec.left],
                            source_half,
                        ),
                    )
                )
        if level < self.maximum_level:
            upper_spec = self.specs[level + 1]
            upper_graph = collar_graph(upper_spec)
            upper_id = {context: index for index, context in enumerate(upper_graph.vertices)}
            for atom in refinement_incidence(upper_spec, spec).atoms:
                upper_map = self.maps[level + 1][upper_id[atom.parent]]
                if atom.child0 == word:
                    votes.append((atom.branch_weight, upper_map))
                if atom.child1 == word:
                    votes.append(
                        (
                            atom.branch_weight,
                            self.solver.advance(
                                upper_map,
                                level,
                                atom.parent[upper_spec.left],
                            ),
                        )
                    )
        if not votes:
            raise AssertionError("an optimized horizon node has no neighbors")
        half = votes[0][1].half
        if any(vote.half != half for _, vote in votes):
            raise AssertionError("neighbor votes target different living halves")
        return tuple(votes)

    @staticmethod
    def _score(
        mapping: StructuredMap,
        votes: Iterable[tuple[Fraction, StructuredMap]],
    ) -> Fraction:
        return sum(
            (weight * mapping.agreement(vote) for weight, vote in votes),
            Fraction(0),
        )

    @staticmethod
    def _best_internal_signature(
        signature: tuple[tuple[int, Permutation5], ...],
    ) -> tuple[int, Permutation5]:
        """Solve one weighted 5x5 assignment using integer vote weights."""

        matrix = [[0] * MODULUS for _ in range(MODULUS)]
        for weight, vote in signature:
            for position, target in enumerate(vote):
                matrix[position][target] += weight
        best_score = -1
        best_permutation: Permutation5 | None = None
        for permutation in five_permutations():
            score = sum(
                matrix[position][target]
                for position, target in enumerate(permutation)
            )
            if score > best_score or (
                score == best_score
                and (best_permutation is None or permutation < best_permutation)
            ):
                best_score = score
                best_permutation = permutation  # type: ignore[assignment]
        if best_permutation is None:
            raise AssertionError("S_5 enumeration is empty")
        return best_score, best_permutation

    def _matching_components(
        self, candidates: tuple[dict[int, tuple[int, Permutation5]], ...]
    ) -> tuple[tuple[tuple[int, ...], tuple[int, ...]], ...]:
        cell_to_blocks: dict[int, set[int]] = {}
        for block, row in enumerate(candidates):
            for cell in row:
                cell_to_blocks.setdefault(cell, set()).add(block)
        unseen = {block for block, row in enumerate(candidates) if row}
        components = []
        while unseen:
            first = min(unseen)
            blocks = {first}
            cells: set[int] = set()
            queue = deque(((0, first),))
            while queue:
                side, item = queue.popleft()
                if side == 0:
                    unseen.discard(item)
                    for cell in candidates[item]:
                        if cell not in cells:
                            cells.add(cell)
                            queue.append((1, cell))
                else:
                    for block in cell_to_blocks[item]:
                        if block not in blocks:
                            blocks.add(block)
                            queue.append((0, block))
            components.append((tuple(sorted(blocks)), tuple(sorted(cells))))
        return tuple(components)

    @staticmethod
    def _component_partial_matching(
        blocks: tuple[int, ...],
        cells: tuple[int, ...],
        candidates: tuple[dict[int, tuple[int, Permutation5]], ...],
    ) -> tuple[tuple[int, int], ...]:
        """Exact maximum-weight partial matching by bitmask DP."""

        if len(cells) > 18:
            raise RuntimeError(
                "positive matching component exceeds exact local scope (18 cells)"
            )
        cell_position = {cell: position for position, cell in enumerate(cells)}
        states: dict[int, tuple[int, tuple[tuple[int, int], ...]]] = {
            0: (0, ())
        }
        for block in blocks:
            updated = dict(states)
            for mask, (score, pairs) in states.items():
                for cell, (edge_score, _) in candidates[block].items():
                    bit = 1 << cell_position[cell]
                    if mask & bit:
                        continue
                    candidate = (score + edge_score, pairs + ((block, cell),))
                    previous = updated.get(mask | bit)
                    if previous is None or candidate[0] > previous[0] or (
                        candidate[0] == previous[0] and candidate[1] < previous[1]
                    ):
                        updated[mask | bit] = candidate
            states = updated
        return max(
            states.values(),
            key=lambda item: (
                item[0],
                tuple(-value for pair in item[1] for value in pair),
            ),
        )[1]

    def coordinate_best(
        self, votes: tuple[tuple[Fraction, StructuredMap], ...]
    ) -> StructuredMap:
        """Return the globally best structured map for fixed neighbor votes."""

        half = votes[0][1].half
        denominator = lcm(*(weight.denominator for weight, _ in votes))
        integer_votes = tuple(
            (int(weight * denominator), vote) for weight, vote in votes
        )
        best_cache: dict[
            tuple[tuple[int, Permutation5], ...], tuple[int, Permutation5]
        ] = {}
        candidates: list[dict[int, tuple[int, Permutation5]]] = []
        for block in range(BLOCK_COUNT):
            cells = sorted({vote.cells[block] for _, vote in integer_votes})
            row = {}
            for cell in cells:
                signature = tuple(
                    (weight, vote.permutations[block])
                    for weight, vote in integer_votes
                    if vote.cells[block] == cell
                )
                cached = best_cache.get(signature)
                if cached is None:
                    cached = self._best_internal_signature(signature)
                    best_cache[signature] = cached
                score, permutation = cached
                if score > 0:
                    row[cell] = (score, permutation)
            candidates.append(row)
        candidate_tuple = tuple(candidates)
        components = self._matching_components(candidate_tuple)
        self.maximum_matching_component = max(
            self.maximum_matching_component,
            max((len(cells) for _, cells in components), default=0),
        )
        selected: dict[int, int] = {}
        for blocks, cells in components:
            for block, cell in self._component_partial_matching(
                blocks, cells, candidate_tuple
            ):
                selected[block] = cell

        used_cells = set(selected.values())
        remaining_blocks = [
            block for block in range(BLOCK_COUNT) if block not in selected
        ]
        remaining_cells = sorted(
            set(self.solver.model.cells_by_half[half]) - used_cells
        )
        if len(remaining_blocks) != len(remaining_cells):
            raise AssertionError("partial matching cannot be completed bijectively")
        selected.update(zip(remaining_blocks, remaining_cells))
        identity: Permutation5 = (0, 1, 2, 3, 4)
        assignments = tuple(selected[block] for block in range(BLOCK_COUNT))
        internal = tuple(
            candidate_tuple[block].get(assignments[block], (0, identity))[1]
            for block in range(BLOCK_COUNT)
        )
        result = StructuredMap(half, assignments, internal)
        if not self.solver.validate_map(result):
            raise AssertionError("coordinate matching did not produce a bijection")
        return result

    def optimize(self, maximum_sweeps: int = 20) -> HorizonReport:
        if maximum_sweeps < 1:
            raise ValueError("maximum_sweeps must be positive")
        initial = self.objective()
        sweeps = []
        for number in range(1, maximum_sweeps + 1):
            before = self.objective()
            changed = 0
            first_level = (
                self.minimum_level + 1
                if self.freeze_minimum
                else self.minimum_level
            )
            order = list(range(first_level, self.maximum_level + 1))
            order += list(range(self.maximum_level - 1, first_level - 1, -1))
            for level in order:
                graph = collar_graph(self.specs[level])
                for vertex, word in enumerate(graph.vertices):
                    votes = self._votes(level, word)
                    current = self.maps[level][vertex]
                    candidate = self.coordinate_best(votes)
                    if self._score(candidate, votes) > self._score(current, votes):
                        self.maps[level][vertex] = candidate
                        changed += 1
            after = self.objective()
            if after > before:
                raise AssertionError("coordinate sweep increased the exact objective")
            sweeps.append(HorizonSweep(number, changed, before, after))
            if changed == 0:
                break
        families = tuple(
            self.family(level)
            for level in range(self.minimum_level, self.maximum_level + 1)
        )
        refinements = tuple(
            self.solver.refinement_report(families[index + 1], families[index])
            for index in range(len(families) - 1)
        )
        reports = tuple(self.solver.family_report(family) for family in families)
        return HorizonReport(
            minimum_level=self.minimum_level,
            maximum_level=self.maximum_level,
            specs=tuple(sorted(self.specs.items())),
            initial_objective=initial,
            final_objective=sum(
                (report.distance for report in refinements), Fraction(0)
            ),
            sweeps=tuple(sweeps),
            refinements=refinements,
            family_reports=reports,
            maximum_matching_component=self.maximum_matching_component,
            minimum_level_frozen=self.freeze_minimum,
        )


def format_horizon_report(report: HorizonReport) -> str:
    lines = [
        "finite horizon levels=%d..%d boundary=%s initial=%s final=%s"
        % (
            report.minimum_level,
            report.maximum_level,
            (
                "fixed-r%d" % report.minimum_level
                if report.minimum_level_frozen
                else "all-levels-free"
            ),
            report.initial_objective,
            report.final_objective,
        ),
        "  collars="
        + ", ".join(
            "r%d:[-%d,+%d]" % (level, spec.left, spec.right)
            for level, spec in report.specs
        ),
        "  maximum positive matching component=%d"
        % report.maximum_matching_component,
    ]
    for sweep in report.sweeps:
        lines.append(
            "  sweep=%d changed=%d objective=%s -> %s"
            % (
                sweep.number,
                sweep.changed_nodes,
                sweep.objective_before,
                sweep.objective_after,
            )
        )
    for refinement in report.refinements:
        lines.append(
            "  D_%d=%s (child0=%s child1=%s max-branch=%s)"
            % (
                refinement.lower_level,
                refinement.distance,
                refinement.first_child_distance,
                refinement.second_child_distance,
                refinement.maximum_branch_distance,
            )
        )
    for family in report.family_reports:
        lines.append(
            "  r=%d contexts=%d roof=%s full-error=%s zero-weight=%s"
            % (
                family.level,
                family.vertices,
                family.conditional_roof_defect,
                family.full_equation_error,
                family.zero_defect_weight,
            )
        )
    return "\n".join(lines)


__all__ = [
    "BLOCK_COUNT",
    "BoundaryFamily",
    "FamilyReport",
    "FiniteHorizonOptimizer",
    "GrowingContextSolver",
    "HorizonReport",
    "HorizonSweep",
    "RefinementReport",
    "SourceBlock",
    "StructuredMap",
    "default_collar",
    "format_horizon_report",
    "source_blocks",
]
