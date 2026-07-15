"""Exact Thue--Morse language censuses and cylinder frequencies.

NON-CANONICAL LOCAL ANALYSIS.  This module supplies exact finite data for the
growing-context entropy-selection experiments.  It deliberately avoids
empirical prefix stabilization:

* every binary pair occurs in ``sigma^3(0)``;
* if ``2^k >= n - 1``, every length-n factor is contained in
  ``sigma^k(ab)`` for one legal pair ``ab``;
* the converse is immediate because every such pair is legal.

Cylinder frequencies use the unique shift-invariant measure of the primitive
constant-length substitution ``sigma(0)=01, sigma(1)=10``.  Splitting output
positions into their even and odd substitution phases gives an exact recursive
formula over :class:`fractions.Fraction`; no floating point or sampling enters.
These local calculations do not create Canon or probe authority.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from typing import Iterable, Mapping


BitWord = tuple[int, ...]


def _word(bits: Iterable[int]) -> BitWord:
    result = tuple(bits)
    if not result or any(bit not in (0, 1) for bit in result):
        raise ValueError("a cylinder word must be a non-empty binary word")
    return result


def substitute(word: Iterable[int], levels: int = 1) -> BitWord:
    """Apply ``0 -> 01, 1 -> 10`` exactly ``levels`` times."""

    if levels < 0:
        raise ValueError("substitution level must be non-negative")
    current = tuple(word)
    if any(bit not in (0, 1) for bit in current):
        raise ValueError("Thue--Morse letters must be 0 or 1")
    for _ in range(levels):
        output: list[int] = []
        for bit in current:
            output.extend((bit, 1 - bit))
        current = tuple(output)
    return current


def _windows(word: BitWord, length: int) -> frozenset[BitWord]:
    return frozenset(
        word[start : start + length]
        for start in range(len(word) - length + 1)
    )


# The prefix sigma^3(0)=01101001 contains all four binary pairs.  Positions are
# zero based and serve as short, directly checkable legality witnesses.
PAIR_WITNESSES: Mapping[BitWord, int] = {
    (0, 0): 5,
    (0, 1): 0,
    (1, 0): 2,
    (1, 1): 1,
}
LEGAL_PAIRS: tuple[BitWord, ...] = tuple(sorted(PAIR_WITNESSES))


def pair_witness_word() -> BitWord:
    """Return the common finite witness ``sigma^3(0)`` for legal pairs."""

    return substitute((0,), 3)


def closure_level(length: int) -> int:
    """Least k for which a length-n window meets at most two k-supertiles."""

    if length < 1:
        raise ValueError("factor length must be positive")
    level = 0
    block_size = 1
    while block_size < length - 1:
        level += 1
        block_size *= 2
    return level


@dataclass(frozen=True, slots=True)
class FactorCensus:
    """Finite completeness certificate for one factor length."""

    length: int
    supertile_level: int
    supertile_size: int
    factors: tuple[BitWord, ...]

    @property
    def complexity(self) -> int:
        return len(self.factors)

    def verify(self, *, extensions: bool = True) -> bool:
        """Check witnesses, exact pair images, and optional extendability."""

        if self.length < 1:
            return False
        if self.supertile_level != closure_level(self.length):
            return False
        if self.supertile_size != 1 << self.supertile_level:
            return False
        if self.supertile_size < self.length - 1:
            return False

        witness = pair_witness_word()
        for pair, position in PAIR_WITNESSES.items():
            if witness[position : position + 2] != pair:
                return False

        generated: set[BitWord] = set()
        for pair in LEGAL_PAIRS:
            generated.update(
                _windows(substitute(pair, self.supertile_level), self.length)
            )
        if self.factors != tuple(sorted(generated)):
            return False

        if extensions:
            longer = factor_census(self.length + 1).factors
            left = {word[1:] for word in longer}
            right = {word[:-1] for word in longer}
            if set(self.factors) != left or set(self.factors) != right:
                return False
        return True


@lru_cache(maxsize=None)
def factor_census(length: int) -> FactorCensus:
    """Return the exact substitution-closure census at ``length``.

    Completeness is finite: choose k with ``2^k >= length-1``.  In a
    substituted bi-infinite point a window of this length crosses at most one
    k-supertile boundary, so it lies in ``sigma^k(ab)``.  All four pairs ``ab``
    are legal, with witnesses stored in :data:`PAIR_WITNESSES`.
    """

    level = closure_level(length)
    generated: set[BitWord] = set()
    for pair in LEGAL_PAIRS:
        generated.update(_windows(substitute(pair, level), length))
    return FactorCensus(
        length=length,
        supertile_level=level,
        supertile_size=1 << level,
        factors=tuple(sorted(generated)),
    )


def factors(length: int) -> tuple[BitWord, ...]:
    """Convenience view of :func:`factor_census`."""

    return factor_census(length).factors


def _solve_square(
    matrix: list[list[Fraction]], right_hand_side: list[Fraction]
) -> tuple[Fraction, ...]:
    """Solve a nonsingular square rational system by exact elimination."""

    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise ValueError("expected a non-empty square matrix")
    if len(right_hand_side) != size:
        raise ValueError("right-hand side has the wrong dimension")
    augmented = [row[:] + [right_hand_side[index]] for index, row in enumerate(matrix)]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if augmented[row][column]),
            None,
        )
        if pivot is None:
            raise ValueError("frequency system is singular")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [entry / scale for entry in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            scale = augmented[row][column]
            if scale:
                augmented[row] = [
                    entry - scale * pivot_entry
                    for entry, pivot_entry in zip(
                        augmented[row], augmented[column], strict=True
                    )
                ]
    return tuple(augmented[row][-1] for row in range(size))


@lru_cache(maxsize=None)
def _frequency_items(length: int) -> tuple[tuple[BitWord, Fraction], ...]:
    language = factors(length)
    if length == 1:
        return (((0,), Fraction(1, 2)), ((1,), Fraction(1, 2)))

    if length == 2:
        # At even output positions a pair is the full image of one letter.  At
        # odd positions it crosses a substitution boundary and maps source pair
        # (a,b) to (1-a,b).  The averaged phase equation is (I-P/2)f=b.
        index = {word: position for position, word in enumerate(language)}
        matrix = [
            [Fraction(int(row == column)) for column in range(len(language))]
            for row in range(len(language))
        ]
        for source_index, source in enumerate(language):
            crossing = (1 - source[0], source[1])
            matrix[index[crossing]][source_index] -= Fraction(1, 2)
        right_hand_side = [Fraction(0) for _ in language]
        for letter, frequency in _frequency_items(1):
            image = substitute(letter)
            right_hand_side[index[image]] += frequency / 2
        solution = _solve_square(matrix, right_hand_side)
        return tuple(zip(language, solution, strict=True))

    # A length-n output window beginning in phase r depends on exactly
    # ceil((n+r)/2) source letters.  Averaging phases r=0,1 gives the invariant
    # cylinder measure recursively in strictly shorter word lengths.
    totals = {word: Fraction(0) for word in language}
    for phase in (0, 1):
        source_length = (length + phase + 1) // 2
        for source, frequency in _frequency_items(source_length):
            image = substitute(source)
            target = image[phase : phase + length]
            if len(target) != length or target not in totals:
                raise AssertionError("substitution phase left the exact language")
            totals[target] += frequency / 2
    return tuple((word, totals[word]) for word in language)


def factor_frequencies(length: int) -> dict[BitWord, Fraction]:
    """Exact frequencies of every legal factor of a fixed length."""

    if length < 1:
        raise ValueError("factor length must be positive")
    return dict(_frequency_items(length))


def cylinder_frequency(word: Iterable[int]) -> Fraction:
    """Return the exact invariant measure of a binary cylinder.

    A binary word outside the Thue--Morse language has measure zero.  Empty or
    non-binary inputs are rejected because their cylinder convention would be
    ambiguous here.
    """

    cylinder = _word(word)
    return factor_frequencies(len(cylinder)).get(cylinder, Fraction(0))


@dataclass(frozen=True, slots=True)
class ContextMeasure:
    """Exact vertex and edge weights for a width-w Rauzy context graph."""

    width: int
    vertices: tuple[tuple[BitWord, Fraction], ...]
    edges: tuple[tuple[BitWord, Fraction], ...]

    def verify(self) -> bool:
        if self.width < 1:
            return False
        vertex_weights = dict(self.vertices)
        edge_weights = dict(self.edges)
        if sum(vertex_weights.values(), Fraction(0)) != 1:
            return False
        if sum(edge_weights.values(), Fraction(0)) != 1:
            return False
        for vertex, weight in vertex_weights.items():
            outgoing = sum(
                (edge_weight for edge, edge_weight in edge_weights.items() if edge[:-1] == vertex),
                Fraction(0),
            )
            incoming = sum(
                (edge_weight for edge, edge_weight in edge_weights.items() if edge[1:] == vertex),
                Fraction(0),
            )
            if outgoing != weight or incoming != weight:
                return False
        return True


@lru_cache(maxsize=None)
def context_measure(width: int) -> ContextMeasure:
    """Return exact cylinder weights for context vertices and their edges."""

    if width < 1:
        raise ValueError("context width must be positive")
    return ContextMeasure(
        width=width,
        vertices=_frequency_items(width),
        edges=_frequency_items(width + 1),
    )


@dataclass(frozen=True, slots=True)
class MeasureAudit:
    """Summary of exact closure and consistency gates through a maximum length."""

    maximum_length: int
    complexities: tuple[int, ...]
    maximum_denominators: tuple[int, ...]
    passed: bool


def audit(maximum_length: int = 20) -> MeasureAudit:
    """Run exact language, positivity, symmetry, and marginal checks."""

    if maximum_length < 1:
        raise ValueError("maximum length must be positive")
    complexities: list[int] = []
    denominators: list[int] = []
    passed = True
    for length in range(1, maximum_length + 1):
        census = factor_census(length)
        frequencies = factor_frequencies(length)
        complexities.append(census.complexity)
        denominators.append(max(value.denominator for value in frequencies.values()))
        passed &= census.verify()
        passed &= tuple(frequencies) == census.factors
        passed &= sum(frequencies.values(), Fraction(0)) == 1
        passed &= all(value > 0 for value in frequencies.values())
        for word, value in frequencies.items():
            passed &= frequencies.get(tuple(1 - bit for bit in word)) == value
            passed &= frequencies.get(tuple(reversed(word))) == value
        if length > 1:
            shorter = factor_frequencies(length - 1)
            for word, value in shorter.items():
                left = sum(
                    (
                        frequency
                        for longer, frequency in frequencies.items()
                        if longer[:-1] == word
                    ),
                    Fraction(0),
                )
                right = sum(
                    (frequency for longer, frequency in frequencies.items() if longer[1:] == word),
                    Fraction(0),
                )
                passed &= left == value and right == value
    return MeasureAudit(
        maximum_length=maximum_length,
        complexities=tuple(complexities),
        maximum_denominators=tuple(denominators),
        passed=bool(passed),
    )


__all__ = [
    "BitWord",
    "ContextMeasure",
    "FactorCensus",
    "LEGAL_PAIRS",
    "MeasureAudit",
    "PAIR_WITNESSES",
    "audit",
    "closure_level",
    "context_measure",
    "cylinder_frequency",
    "factor_census",
    "factor_frequencies",
    "factors",
    "pair_witness_word",
    "substitute",
]
