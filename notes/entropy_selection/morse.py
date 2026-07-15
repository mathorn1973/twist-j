"""Exact finite language and substitution towers for the Thue--Morse base.

NON-CANONICAL LOCAL ANALYSIS.  The context graphs below are finite clopen/SFT
approximants to the aperiodic substitution system.  A graph cycle is a
consistency condition for a context-dependent transfer; it is never reported
as a periodic point of the Thue--Morse subshift.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from functools import lru_cache
from typing import Iterable


BitWord = tuple[int, ...]


def substitute(word: Iterable[int]) -> BitWord:
    """Apply ``0 -> 01, 1 -> 10`` once."""

    output: list[int] = []
    for bit in word:
        if bit not in (0, 1):
            raise ValueError("Thue--Morse letters must be 0 or 1")
        output.extend((bit, 1 - bit))
    return tuple(output)


@lru_cache(maxsize=None)
def supertile(letter: int, level: int) -> BitWord:
    """Return the exact level-``level`` supertile of ``letter``."""

    if letter not in (0, 1):
        raise ValueError("supertile letter must be 0 or 1")
    if level < 0:
        raise ValueError("supertile level must be non-negative")
    word: BitWord = (letter,)
    for _ in range(level):
        word = substitute(word)
    return word


def last_symbol(letter: int, level: int) -> int:
    """Last fine letter in a level-r supertile."""

    if letter not in (0, 1) or level < 0:
        raise ValueError("invalid supertile identity")
    return letter ^ (level & 1)


def thue_morse_prefix(length: int) -> BitWord:
    """Return the distinguished forward prefix without recursion state."""

    if length < 0:
        raise ValueError("prefix length must be non-negative")
    return tuple(index.bit_count() & 1 for index in range(length))


@lru_cache(maxsize=None)
def factors(length: int) -> tuple[BitWord, ...]:
    """Census the finite Thue--Morse language at one word length.

    The census is enlarged until it is unchanged through three successive
    substitution doublings.  A final two-level look-ahead is checked before
    returning.  This is local recon infrastructure, not a public proof of a
    general factor-complexity formula.
    """

    if length < 1:
        raise ValueError("factor length must be positive")
    word: BitWord = (0,)
    previous: frozenset[BitWord] | None = None
    stable = 0
    for _level in range(1, 26):
        word = substitute(word)
        if len(word) < max(64, 16 * length):
            continue
        current = frozenset(
            word[start : start + length]
            for start in range(len(word) - length + 1)
        )
        if current == previous:
            stable += 1
        else:
            stable = 0
            previous = current
        if stable >= 3:
            lookahead = substitute(substitute(word))
            checked = frozenset(
                lookahead[start : start + length]
                for start in range(len(lookahead) - length + 1)
            )
            if checked != current:
                stable = 0
                previous = checked
                word = lookahead
                continue
            return tuple(sorted(current))
    raise RuntimeError("Thue--Morse factor census did not stabilize")


@dataclass(frozen=True, slots=True)
class ContextEdge:
    id: int
    source: int
    target: int
    word: BitWord
    current: int
    appended: int


@dataclass(frozen=True)
class ContextGraph:
    """Rauzy context graph for transfer maps constant on finite factors.

    A vertex word is read as ``(previous, current, future...)``.  Along an
    edge, the block cocycle is therefore selected by ``word[1]`` and the
    target vertex has that current symbol as its previous symbol.
    """

    width: int
    vertices: tuple[BitWord, ...]
    edges: tuple[ContextEdge, ...]
    outgoing: tuple[tuple[int, ...], ...]
    incoming: tuple[tuple[int, ...], ...]
    root: int
    tree_edges: tuple[int | None, ...]

    def is_strongly_connected(self) -> bool:
        vertices = set(range(len(self.vertices)))
        return (
            _reachable(self.outgoing, self.root) == vertices
            and _reachable(self.incoming, self.root) == vertices
        )


def _reachable(adjacency: tuple[tuple[int, ...], ...], root: int) -> set[int]:
    seen = {root}
    queue = deque((root,))
    while queue:
        vertex = queue.popleft()
        for neighbor in adjacency[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return seen


@lru_cache(maxsize=None)
def context_graph(width: int) -> ContextGraph:
    """Build the exact censused context graph at width at least two."""

    if width < 2:
        raise ValueError("a transfer context needs previous and current letters")
    vertices = factors(width)
    vertex_id = {word: index for index, word in enumerate(vertices)}
    long_words = factors(width + 1)
    edges: list[ContextEdge] = []
    outgoing_edges: list[list[int]] = [[] for _ in vertices]
    outgoing_vertices: list[list[int]] = [[] for _ in vertices]
    incoming_vertices: list[list[int]] = [[] for _ in vertices]
    for long_word in long_words:
        source_word = long_word[:-1]
        target_word = long_word[1:]
        source = vertex_id[source_word]
        target = vertex_id[target_word]
        edge = ContextEdge(
            id=len(edges),
            source=source,
            target=target,
            word=long_word,
            current=source_word[1],
            appended=long_word[-1],
        )
        edges.append(edge)
        outgoing_edges[source].append(edge.id)
        outgoing_vertices[source].append(target)
        incoming_vertices[target].append(source)

    root = 0
    tree_edges: list[int | None] = [None] * len(vertices)
    seen = {root}
    queue = deque((root,))
    while queue:
        source = queue.popleft()
        for edge_id in outgoing_edges[source]:
            target = edges[edge_id].target
            if target not in seen:
                seen.add(target)
                tree_edges[target] = edge_id
                queue.append(target)
    if len(seen) != len(vertices):
        raise ValueError("context graph is not reachable from its root")

    graph = ContextGraph(
        width=width,
        vertices=vertices,
        edges=tuple(edges),
        outgoing=tuple(tuple(row) for row in outgoing_vertices),
        incoming=tuple(tuple(row) for row in incoming_vertices),
        root=root,
        tree_edges=tuple(tree_edges),
    )
    if not graph.is_strongly_connected():
        raise ValueError("Thue--Morse context graph is not strongly connected")
    return graph


def refinement_parent(
    previous: int, current: int, position: int, lower_height: int
) -> tuple[int, int, int]:
    """Map a level-r+1 tower atom to its level-r parent atom.

    For the first child of ``sigma(current)``, the preceding lower-level
    supertile is the last child ``1-previous`` of ``sigma(previous)``.  The
    second child ``1-current`` is preceded by the first child ``current``.
    """

    if previous not in (0, 1) or current not in (0, 1):
        raise ValueError("tower types must be binary")
    if lower_height < 1 or not 0 <= position < 2 * lower_height:
        raise ValueError("position is outside the refined tower")
    if position < lower_height:
        return (1 - previous, current, position)
    return (current, 1 - current, position - lower_height)


__all__ = [
    "BitWord",
    "ContextEdge",
    "ContextGraph",
    "context_graph",
    "factors",
    "last_symbol",
    "refinement_parent",
    "substitute",
    "supertile",
    "thue_morse_prefix",
]
