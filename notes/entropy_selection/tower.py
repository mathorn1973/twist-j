#!/usr/bin/env python3
"""Explicit Rokhlin-tower transfer approximants for entropy selection.

NON-CANONICAL LOCAL ANALYSIS.  Every approximant below is an actual family of
3125-point bijections.  It obeys the desired skew equation at every interior
level of a dyadic Thue--Morse supertile.  No claim is made at the roofs, and a
roof error of order 2^-r alone is not evidence for a measurable solution.

The purpose of this baseline is constructive: it gives future optimization
and Cauchy/refinement solvers concrete permutations to improve, rather than a
cardinality or cycle-spectrum surrogate.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

try:
    from .block_solver import source_sectors
    from .lambda5 import SIZE, j_permutation
    from .living import LivingKernel, reconstruct
    from .morse import factors, last_symbol, refinement_parent, supertile
except ImportError:  # Direct execution from this directory.
    from block_solver import source_sectors  # type: ignore[no-redef]
    from lambda5 import SIZE, j_permutation  # type: ignore[no-redef]
    from living import LivingKernel, reconstruct  # type: ignore[no-redef]
    from morse import (  # type: ignore[no-redef]
        factors,
        last_symbol,
        refinement_parent,
        supertile,
    )


Permutation = tuple[int, ...]


@dataclass(frozen=True, slots=True)
class RoofDefect:
    context: tuple[int, int, int]
    mismatches: int
    carrier: int

    @property
    def fraction(self) -> Fraction:
        return Fraction(self.mismatches, self.carrier)


@dataclass(frozen=True, slots=True)
class RefinementDefect:
    parent_context: tuple[int, int]
    child_context: tuple[int, int]
    child: int
    mismatches: int
    comparisons: int

    @property
    def fraction(self) -> Fraction:
        return Fraction(self.mismatches, self.comparisons)


@dataclass(frozen=True, slots=True)
class TowerReport:
    level: int
    height: int
    interior_equation: bool
    fiber_bijections: bool
    roof_defects: tuple[RoofDefect, ...]
    roof_error_upper_bound: Fraction
    refinement_defects: tuple[RefinementDefect, ...]


def _inverse(permutation: Permutation) -> Permutation:
    inverse = [-1] * len(permutation)
    for source, target in enumerate(permutation):
        if not 0 <= target < len(permutation) or inverse[target] >= 0:
            raise ValueError("mapping is not a permutation")
        inverse[target] = source
    return tuple(inverse)


class LexicographicTowerBaseline:
    """A transparent ordered sector-to-cell matching and its tower fill."""

    def __init__(self, model: LivingKernel | None = None) -> None:
        self.model = model if model is not None else reconstruct()
        self.j_map = j_permutation()
        self.j_inverse = _inverse(self.j_map)
        self._boundary_cache: dict[tuple[int, int], Permutation] = {}
        self._tower_cache: dict[tuple[int, int, int], tuple[Permutation, ...]] = {}

    def lexicographic_boundary_map(self, level: int, previous: int) -> Permutation:
        """Match ordered source sectors to ordered target cells at a roof base."""

        if level < 2 or previous not in (0, 1):
            raise ValueError("tower boundaries require level>=2 and a bit")
        key = (level, previous)
        cached = self._boundary_cache.get(key)
        if cached is not None:
            return cached
        half = last_symbol(previous, level)
        non_singlet_cells = tuple(
            cell
            for cell in self.model.cells_by_half[half]
            if self.model.pentagons[cell].component != self.model.singlet_component
        )
        five_sectors = tuple(
            sector for sector in source_sectors() if len(sector.points) == 5
        )
        if len(non_singlet_cells) != 624 or len(five_sectors) != 624:
            raise AssertionError("source-sector/target-cell census mismatch")
        mapping = [-1] * SIZE
        for sector, cell_id in zip(five_sectors, non_singlet_cells):
            target = self.model.pentagons[cell_id]
            for q, point in enumerate(sector.points):
                mapping[point] = target.state_by_q[q]

        singletons = sorted(
            (sector for sector in source_sectors() if len(sector.points) == 1),
            key=lambda sector: sector.points[0],
        )
        singlet_cell = self.model.component_cells(
            self.model.singlet_component, half
        )[0]
        singlet = self.model.pentagons[singlet_cell]
        for q, sector in enumerate(singletons):
            mapping[sector.points[0]] = singlet.state_by_q[q]

        result = tuple(mapping)
        if -1 in result or set(result) != set(self.model.halves[half]):
            raise AssertionError("lexicographic boundary map is not a fiber bijection")
        self._boundary_cache[key] = result
        return result

    def tower_maps(
        self, level: int, previous: int, current: int
    ) -> tuple[Permutation, ...]:
        """Fill one tower by ``B_j=F_prefix(j) X J^(-j)``."""

        if (previous, current) not in factors(2):
            raise ValueError("the requested desubstituted pair is not admissible")
        key = (level, previous, current)
        cached = self._tower_cache.get(key)
        if cached is not None:
            return cached
        word = supertile(current, level)
        boundary = self.lexicographic_boundary_map(level, previous)
        maps = [boundary]
        for letter in word[:-1]:
            source_map = maps[-1]
            target_map = [-1] * SIZE
            # B_(j+1)(J y) = F_letter(B_j(y)).
            for y, target_state in enumerate(source_map):
                target_map[self.j_map[y]] = self.model.tick_state(letter, target_state)
            maps.append(tuple(target_map))
        result = tuple(maps)
        if len(result) != len(word):
            raise AssertionError("tower fill has the wrong height")
        self._tower_cache[key] = result
        return result

    def check_tower(self, level: int, previous: int, current: int) -> tuple[bool, bool]:
        """Check every interior equation and every fiber bijection exactly."""

        maps = self.tower_maps(level, previous, current)
        word = supertile(current, level)
        interior = all(
            maps[position + 1][self.j_map[y]]
            == self.model.tick_state(word[position], maps[position][y])
            for position in range(len(word) - 1)
            for y in range(SIZE)
        )
        fiber_bijections = True
        for position, mapping in enumerate(maps):
            previous_fine = (
                last_symbol(previous, level)
                if position == 0
                else word[position - 1]
            )
            fiber_bijections = fiber_bijections and (
                set(mapping) == set(self.model.halves[previous_fine])
            )
        return interior, fiber_bijections

    def roof_defects(self, level: int) -> tuple[RoofDefect, ...]:
        """Compare the last tick with the next actual desubstituted context."""

        defects = []
        for left, current, right in factors(3):
            maps = self.tower_maps(level, left, current)
            word = supertile(current, level)
            next_boundary = self.lexicographic_boundary_map(level, current)
            mismatches = sum(
                next_boundary[self.j_map[y]]
                != self.model.tick_state(word[-1], maps[-1][y])
                for y in range(SIZE)
            )
            defects.append(
                RoofDefect(
                    context=(left, current, right),
                    mismatches=mismatches,
                    carrier=SIZE,
                )
            )
        return tuple(defects)

    def refinement_defects(self, level: int) -> tuple[RefinementDefect, ...]:
        """Compare this lexicographic level with its exact level+1 refinement.

        Fractions are reported separately by admissible parent pair and child;
        they are not averaged with invented uniform context weights.
        """

        if level < 2:
            raise ValueError("refinement comparison starts at level 2")
        height = 1 << level
        defects = []
        for previous, current in factors(2):
            upper = self.tower_maps(level + 1, previous, current)
            for child in (0, 1):
                position = child * height
                parent_previous, parent_current, parent_position = refinement_parent(
                    previous, current, position, height
                )
                lower = self.tower_maps(level, parent_previous, parent_current)
                mismatches = sum(
                    upper[position + offset][y] != lower[parent_position + offset][y]
                    for offset in range(height)
                    for y in range(SIZE)
                )
                defects.append(
                    RefinementDefect(
                        parent_context=(previous, current),
                        child_context=(parent_previous, parent_current),
                        child=child,
                        mismatches=mismatches,
                        comparisons=height * SIZE,
                    )
                )
        return tuple(defects)

    def report(self, level: int, include_refinement: bool = True) -> TowerReport:
        """Run exact construction gates for all admissible pair contexts."""

        checks = tuple(
            self.check_tower(level, previous, current)
            for previous, current in factors(2)
        )
        roofs = self.roof_defects(level)
        height = 1 << level
        # A roof occupies exactly one level out of every height-level tower.
        # Taking the worst carrier defect avoids assuming context frequencies.
        roof_upper = max((defect.fraction for defect in roofs), default=Fraction(0))
        roof_upper /= height
        refinements = self.refinement_defects(level) if include_refinement else ()
        return TowerReport(
            level=level,
            height=height,
            interior_equation=all(check[0] for check in checks),
            fiber_bijections=all(check[1] for check in checks),
            roof_defects=roofs,
            roof_error_upper_bound=roof_upper,
            refinement_defects=refinements,
        )


def format_tower_report(report: TowerReport) -> str:
    roof_fractions = sorted({defect.fraction for defect in report.roof_defects})
    refinement_fractions = sorted(
        {defect.fraction for defect in report.refinement_defects}
    )
    return "\n".join(
        (
            "level=%d height=%d interior=%s fiber-bijections=%s"
            % (
                report.level,
                report.height,
                report.interior_equation,
                report.fiber_bijections,
            ),
            "  roof carrier-defect fractions=%s"
            % ([str(value) for value in roof_fractions],),
            "  invariant-measure roof-error upper bound <= %s"
            % (report.roof_error_upper_bound,),
            "  lexicographic refinement-defect fractions=%s"
            % ([str(value) for value in refinement_fractions],),
            "  guard: shrinking roofs alone do not imply a Cauchy transfer",
        )
    )


__all__ = [
    "LexicographicTowerBaseline",
    "RefinementDefect",
    "RoofDefect",
    "TowerReport",
    "format_tower_report",
]
