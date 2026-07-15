"""Exact two-sided collars and substitution-refinement incidence.

NON-CANONICAL LOCAL ANALYSIS.  A collar is anchored at coordinate zero and
records positions ``-left .. right`` in the two-sided Thue--Morse subshift.
Refinement atoms retain one common admissible extension for both substitution
children; treating the two child marginals independently would lose their
correlation and give an incorrect Cauchy objective.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache

try:
    from .measure import BitWord, cylinder_frequency, factors
except ImportError:  # Direct execution from this directory.
    from measure import BitWord, cylinder_frequency, factors  # type: ignore[no-redef]


@dataclass(frozen=True, order=True, slots=True)
class CollarSpec:
    """Coordinates retained around an anchored current letter."""

    left: int
    right: int

    def __post_init__(self) -> None:
        if self.left < 0 or self.right < 0:
            raise ValueError("collar radii must be non-negative")

    @classmethod
    def symmetric(cls, radius: int) -> CollarSpec:
        return cls(radius, radius)

    @property
    def length(self) -> int:
        return self.left + 1 + self.right

    @property
    def start(self) -> int:
        return -self.left

    @property
    def stop(self) -> int:
        return self.right

    def index(self, coordinate: int) -> int:
        if not self.start <= coordinate <= self.stop:
            raise IndexError("coordinate lies outside the collar")
        return coordinate + self.left


@dataclass(frozen=True, slots=True)
class AnchoredContext:
    spec: CollarSpec
    word: BitWord

    def __post_init__(self) -> None:
        if len(self.word) != self.spec.length:
            raise ValueError("context word has the wrong collar length")
        if self.word not in factors(self.spec.length):
            raise ValueError("context word is not in the Thue--Morse language")

    @property
    def current(self) -> int:
        return self.word[self.spec.left]

    def at(self, coordinate: int) -> int:
        return self.word[self.spec.index(coordinate)]


@dataclass(frozen=True, slots=True)
class RefinementAtom:
    """One joint parent-to-two-children refinement hyperatom."""

    parent: BitWord
    extension: BitWord
    extension_spec: CollarSpec
    child0: BitWord
    child1: BitWord
    frequency: Fraction

    @property
    def branch_weight(self) -> Fraction:
        return self.frequency / 2


@dataclass(frozen=True, slots=True)
class RefinementIncidence:
    parent_spec: CollarSpec
    child_spec: CollarSpec
    atoms: tuple[RefinementAtom, ...]

    def verify(self) -> bool:
        parents = factors(self.parent_spec.length)
        children = factors(self.child_spec.length)
        if sum((atom.frequency for atom in self.atoms), Fraction(0)) != 1:
            return False
        if sum((2 * atom.branch_weight for atom in self.atoms), Fraction(0)) != 1:
            return False

        for parent in parents:
            total = sum(
                (
                    atom.frequency
                    for atom in self.atoms
                    if atom.parent == parent
                ),
                Fraction(0),
            )
            if total != cylinder_frequency(parent):
                return False

        # A fixed substitution phase need not itself have the shift-invariant
        # distribution.  The invariant lower measure is the equal mixture of
        # the two child phases.
        for child in children:
            total = sum(
                (
                    atom.branch_weight
                    for atom in self.atoms
                    for candidate in (atom.child0, atom.child1)
                    if candidate == child
                ),
                Fraction(0),
            )
            if total != cylinder_frequency(child):
                return False

        for atom in self.atoms:
            if len(atom.extension) != atom.extension_spec.length:
                return False
            if atom.frequency != cylinder_frequency(atom.extension):
                return False
            if atom.parent != _extract(
                atom.extension,
                atom.extension_spec,
                self.parent_spec.start,
                self.parent_spec.stop,
            ):
                return False
            if atom.child0 != refine_word(
                atom.extension, atom.extension_spec, self.child_spec, 0
            ):
                return False
            if atom.child1 != refine_word(
                atom.extension, atom.extension_spec, self.child_spec, 1
            ):
                return False
            if atom.child0[1:] != atom.child1[:-1]:
                return False
            parent_current = atom.parent[self.parent_spec.left]
            if atom.child0[self.child_spec.left] != parent_current:
                return False
            if atom.child1[self.child_spec.left] != 1 - parent_current:
                return False
            complement = tuple(1 - bit for bit in atom.extension)
            partner = next(
                (
                    candidate
                    for candidate in self.atoms
                    if candidate.extension == complement
                    and candidate.extension_spec == atom.extension_spec
                ),
                None,
            )
            if partner is None or partner.frequency != atom.frequency:
                return False
        return True


@dataclass(frozen=True, slots=True)
class CollarEdge:
    id: int
    source: int
    target: int
    word: BitWord
    current: int
    weight: Fraction


@dataclass(frozen=True, slots=True)
class CollarGraph:
    """Exact weighted Rauzy graph for one anchored collar specification."""

    spec: CollarSpec
    vertices: tuple[BitWord, ...]
    edges: tuple[CollarEdge, ...]
    outgoing: tuple[tuple[int, ...], ...]
    incoming: tuple[tuple[int, ...], ...]

    def verify(self) -> bool:
        if self.spec.left < 1:
            return False
        if sum((edge.weight for edge in self.edges), Fraction(0)) != 1:
            return False
        for vertex_id, vertex in enumerate(self.vertices):
            weight = cylinder_frequency(vertex)
            outgoing = sum(
                (self.edges[edge_id].weight for edge_id in self.outgoing[vertex_id]),
                Fraction(0),
            )
            incoming = sum(
                (self.edges[edge_id].weight for edge_id in self.incoming[vertex_id]),
                Fraction(0),
            )
            if outgoing != weight or incoming != weight:
                return False
        return True


def _extract(
    extension: BitWord,
    extension_spec: CollarSpec,
    start: int,
    stop: int,
) -> BitWord:
    return extension[
        extension_spec.index(start) : extension_spec.index(stop) + 1
    ]


def refine_word(
    extension: BitWord,
    extension_spec: CollarSpec,
    child_spec: CollarSpec,
    phase: int,
) -> BitWord:
    """Return the lower collar anchored at child phase 0 or 1.

    If ``x`` is the coarse sequence, its substituted sequence satisfies
    ``z[2i]=x[i]`` and ``z[2i+1]=1-x[i]``.  Hence a lower coordinate ``t`` in
    child phase ``c`` reads coarse coordinate ``floor((c+t)/2)`` and is
    complemented exactly when ``c+t`` is odd.
    """

    if phase not in (0, 1):
        raise ValueError("child phase must be 0 or 1")
    if len(extension) != extension_spec.length:
        raise ValueError("extension word has the wrong collar length")
    result = []
    for coordinate in range(child_spec.start, child_spec.stop + 1):
        shifted = phase + coordinate
        coarse_coordinate = shifted // 2
        bit = extension[extension_spec.index(coarse_coordinate)]
        result.append(bit ^ (shifted % 2))
    return tuple(result)


@lru_cache(maxsize=None)
def collar_graph(spec: CollarSpec) -> CollarGraph:
    """Build the exact weighted shift graph for an anchored collar."""

    if spec.left < 1:
        raise ValueError("a block-boundary collar must retain its previous letter")
    vertices = factors(spec.length)
    vertex_id = {word: index for index, word in enumerate(vertices)}
    edges = []
    outgoing: list[list[int]] = [[] for _ in vertices]
    incoming: list[list[int]] = [[] for _ in vertices]
    for word in factors(spec.length + 1):
        source = vertex_id[word[:-1]]
        target = vertex_id[word[1:]]
        edge = CollarEdge(
            id=len(edges),
            source=source,
            target=target,
            word=word,
            current=word[spec.left],
            weight=cylinder_frequency(word),
        )
        edges.append(edge)
        outgoing[source].append(edge.id)
        incoming[target].append(edge.id)
    result = CollarGraph(
        spec=spec,
        vertices=vertices,
        edges=tuple(edges),
        outgoing=tuple(tuple(row) for row in outgoing),
        incoming=tuple(tuple(row) for row in incoming),
    )
    if not result.verify():
        raise AssertionError("weighted collar graph failed exact invariants")
    return result


@lru_cache(maxsize=None)
def refinement_incidence(
    parent_spec: CollarSpec,
    child_spec: CollarSpec,
) -> RefinementIncidence:
    """Enumerate the exact weighted joint refinement incidence."""

    required_start = (-child_spec.left) // 2
    required_stop = (1 + child_spec.right) // 2
    union_start = min(parent_spec.start, required_start)
    union_stop = max(parent_spec.stop, required_stop)
    extension_spec = CollarSpec(-union_start, union_stop)
    atoms = []
    for extension in factors(extension_spec.length):
        parent = _extract(
            extension,
            extension_spec,
            parent_spec.start,
            parent_spec.stop,
        )
        atoms.append(
            RefinementAtom(
                parent=parent,
                extension=extension,
                extension_spec=extension_spec,
                child0=refine_word(
                    extension, extension_spec, child_spec, 0
                ),
                child1=refine_word(
                    extension, extension_spec, child_spec, 1
                ),
                frequency=cylinder_frequency(extension),
            )
        )
    result = RefinementIncidence(parent_spec, child_spec, tuple(atoms))
    if not result.verify():
        raise AssertionError("refinement incidence failed exact invariants")
    return result


__all__ = [
    "AnchoredContext",
    "CollarEdge",
    "CollarGraph",
    "CollarSpec",
    "RefinementAtom",
    "RefinementIncidence",
    "collar_graph",
    "refine_word",
    "refinement_incidence",
]
