#!/usr/bin/env python3
"""Exact audit for C-PHOTON-POLYMER-CONTEXT-GRAMMAR-N.

PUBLIC, NON-CANONICAL. Standard library only.
Author: A. M. Thorn <thorn@twistj.com>
License: Apache-2.0.

All scientific scope, grid and limits are frozen in PREREG.md.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations


Vec = tuple[int, int, int, int]
Axes2 = tuple[int, int]
Axes3 = tuple[int, int, int]
Face = tuple[Vec, Axes2]
Cell = tuple[Vec, Axes3]
State = tuple[Cell, Cell, tuple[Cell, ...]]

STATE_CAP = 20_000
Q = 1 << 18
ITER_CAP = 256
COORD_CAP_INT = 8 * Q

Y_CANDIDATES = (
    Fraction(17, 16),
    Fraction(33, 32),
    Fraction(65, 64),
    Fraction(129, 128),
    Fraction(257, 256),
    Fraction(513, 512),
    Fraction(1025, 1024),
    Fraction(1, 1),
)


def shift(x: Vec, axis: int, amount: int) -> Vec:
    return tuple(v + (amount if i == axis else 0) for i, v in enumerate(x))  # type: ignore[return-value]


def translate_cell(c: Cell, delta: Vec) -> Cell:
    x, axes = c
    return (tuple(x[i] + delta[i] for i in range(4)), axes)  # type: ignore[return-value]


def cell_faces(cell: Cell) -> frozenset[Face]:
    x, axes = cell
    out: set[Face] = set()
    for axis in axes:
        pair = tuple(a for a in axes if a != axis)
        assert len(pair) == 2
        out.add((x, pair))
        out.add((shift(x, axis, 1), pair))
    assert len(out) == 6
    return frozenset(out)


def incident_cells(face: Face) -> frozenset[Cell]:
    x, pair = face
    complement = tuple(a for a in range(4) if a not in pair)
    assert len(complement) == 2
    out: set[Cell] = set()
    for axis in complement:
        axes = tuple(sorted(pair + (axis,)))
        out.add((x, axes))
        out.add((shift(x, axis, -1), axes))
    assert len(out) == 4
    return frozenset(out)


def child_groups(parent: Cell) -> tuple[tuple[Face, tuple[Cell, ...]], ...]:
    groups = []
    seen: set[Cell] = set()
    for face in sorted(cell_faces(parent)):
        inc = set(incident_cells(face))
        assert parent in inc
        inc.remove(parent)
        assert len(inc) == 3
        children = tuple(sorted(inc))
        assert not (seen & set(children))
        seen.update(children)
        groups.append((face, children))
    assert len(groups) == 6
    assert len(seen) == 18
    return tuple(groups)


def candidates_excluding_interface(current: Cell, parent: Cell) -> tuple[Cell, ...]:
    shared = cell_faces(current) & cell_faces(parent)
    assert len(shared) == 1
    interface = next(iter(shared))
    out: list[Cell] = []
    for face, group in child_groups(current):
        if face != interface:
            out.extend(group)
    assert len(out) == 15
    assert len(set(out)) == 15
    return tuple(sorted(out))


def conflict_masks(candidates: tuple[Cell, ...]) -> tuple[int, ...]:
    fs = [cell_faces(c) for c in candidates]
    out = [0] * len(candidates)
    for i, j in combinations(range(len(candidates)), 2):
        if fs[i] & fs[j]:
            out[i] |= 1 << j
            out[j] |= 1 << i
    return tuple(out)


@lru_cache(None)
def independent_masks_for(candidates: tuple[Cell, ...]) -> tuple[int, ...]:
    conflicts = conflict_masks(candidates)

    @lru_cache(None)
    def rec(mask: int) -> tuple[int, ...]:
        if mask == 0:
            return (0,)
        low = mask & -mask
        v = low.bit_length() - 1
        without = rec(mask ^ low)
        allowed = mask & ~low & ~conflicts[v]
        with_v = tuple(m | low for m in rec(allowed))
        return without + with_v

    masks = rec((1 << len(candidates)) - 1)
    assert len(masks) == len(set(masks))
    return masks


def normalize_state(parent: Cell, current: Cell, uncles: tuple[Cell, ...]) -> State:
    x, _ = current
    delta = tuple(-v for v in x)
    p = translate_cell(parent, delta)
    c = translate_cell(current, delta)
    us = tuple(sorted(translate_cell(u, delta) for u in uncles))
    state = (p, c, us)
    validate_state(state)
    return state


def validate_state(state: State) -> None:
    parent, current, uncles = state
    assert current[0] == (0, 0, 0, 0)
    assert len(cell_faces(parent) & cell_faces(current)) == 1
    assert len(set(uncles)) == len(uncles)
    assert parent not in uncles and current not in uncles
    assert len(uncles) <= 5

    for uncle in uncles:
        assert len(cell_faces(parent) & cell_faces(uncle)) == 1
        assert not (cell_faces(current) & cell_faces(uncle))

    for i, j in combinations(range(len(uncles)), 2):
        assert not (cell_faces(uncles[i]) & cell_faces(uncles[j]))


def state_survivors(state: State) -> tuple[Cell, ...]:
    parent, current, uncles = state
    raw = candidates_excluding_interface(current, parent)
    out = tuple(
        child
        for child in raw
        if all(not (cell_faces(child) & cell_faces(uncle)) for uncle in uncles)
    )
    assert len(out) <= 15
    return out


def state_term_keys(state: State) -> tuple[tuple[State, ...], ...]:
    parent, current, _ = state
    survivors = state_survivors(state)
    masks = independent_masks_for(survivors)
    terms: list[tuple[State, ...]] = []

    for mask in masks:
        selected = tuple(survivors[i] for i in range(len(survivors)) if mask & (1 << i))
        next_states = []
        for child in selected:
            uncles = tuple(c for c in selected if c != child)
            next_states.append(normalize_state(current, child, uncles))
        terms.append(tuple(sorted(next_states)))

    return tuple(terms)


def root_term_keys() -> tuple[tuple[State, ...], ...]:
    root: Cell = ((0, 0, 0, 0), (0, 1, 2))
    candidates = tuple(c for _, group in child_groups(root) for c in group)
    assert len(candidates) == 18
    masks = independent_masks_for(candidates)
    terms: list[tuple[State, ...]] = []

    for mask in masks:
        selected = tuple(candidates[i] for i in range(18) if mask & (1 << i))
        next_states = []
        for child in selected:
            uncles = tuple(c for c in selected if c != child)
            next_states.append(normalize_state(root, child, uncles))
        terms.append(tuple(sorted(next_states)))

    assert len(terms) == 1240
    return tuple(terms)


def build_grammar():
    states: list[State] = []
    index: dict[State, int] = {}

    def get_id(state: State) -> int:
        if state in index:
            return index[state]
        if len(states) >= STATE_CAP:
            raise AssertionError("state cap exceeded")
        i = len(states)
        index[state] = i
        states.append(state)
        return i

    root_keys = root_term_keys()
    root_counter: Counter[tuple[int, ...]] = Counter()
    for term in root_keys:
        ids = tuple(sorted(get_id(s) for s in term))
        root_counter[ids] += 1

    transitions: list[Counter[tuple[int, ...]]] = []
    cursor = 0
    max_uncles = 0
    max_survivors = 0
    max_children = 0

    while cursor < len(states):
        state = states[cursor]
        validate_state(state)
        max_uncles = max(max_uncles, len(state[2]))
        survivors = state_survivors(state)
        max_survivors = max(max_survivors, len(survivors))
        term_keys = state_term_keys(state)
        counter: Counter[tuple[int, ...]] = Counter()

        for term in term_keys:
            ids = tuple(sorted(get_id(s) for s in term))
            max_children = max(max_children, len(ids))
            counter[ids] += 1

        transitions.append(counter)
        cursor += 1

    assert len(transitions) == len(states)

    # Full post-closure readback of state and transition invariants.
    for sid, state in enumerate(states):
        validate_state(state)
        for term, multiplicity in transitions[sid].items():
            assert multiplicity >= 1
            assert len(term) <= 5
            for tid in term:
                assert 0 <= tid < len(states)

    for term, multiplicity in root_counter.items():
        assert multiplicity >= 1
        assert len(term) <= 6
        for tid in term:
            assert 0 <= tid < len(states)

    root_monomials = sum(root_counter.values())
    transition_monomials = sum(sum(c.values()) for c in transitions)
    assert root_monomials == 1240

    print(
        "GRAMMAR PASS "
        f"states={len(states)} root_monomials={root_monomials} "
        f"transition_monomials={transition_monomials} "
        f"unique_transition_terms={sum(len(c) for c in transitions)} "
        f"max_uncles={max_uncles} max_survivors={max_survivors} "
        f"max_children={max_children} candidate_graphs={independent_masks_for.cache_info().currsize}"
    )
    return states, transitions, root_counter


def map_coordinate_int(
    counter: Counter[tuple[int, ...]],
    q: list[int],
    y: Fraction,
) -> int:
    # Non-root terms have at most five children.
    total = 0
    for term, multiplicity in counter.items():
        b = len(term)
        product_int = 1
        for tid in term:
            product_int *= q[tid]
        total += multiplicity * product_int * (Q ** (5 - b))

    # F(q/Q)*Q = y_num*total / (16*y_den*Q^4).
    denominator = 16 * y.denominator * (Q**4)
    numerator = y.numerator * total
    return (numerator + denominator - 1) // denominator


def exact_component_holds(
    counter: Counter[tuple[int, ...]],
    q: list[int],
    y: Fraction,
    bound_int: int,
) -> bool:
    total = 0
    for term, multiplicity in counter.items():
        b = len(term)
        product_int = 1
        for tid in term:
            product_int *= q[tid]
        total += multiplicity * product_int * (Q ** (5 - b))
    # F <= bound_int/Q iff y_num*total <=16*y_den*Q^4*bound_int.
    return y.numerator * total <= 16 * y.denominator * (Q**4) * bound_int


def root_bound(
    root_counter: Counter[tuple[int, ...]],
    q: list[int],
    y: Fraction,
) -> Fraction:
    total = 0
    for term, multiplicity in root_counter.items():
        b = len(term)
        product_int = 1
        for tid in term:
            product_int *= q[tid]
        total += multiplicity * product_int * (Q ** (6 - b))
    return Fraction(y.numerator * total, 16 * y.denominator * (Q**6))


def certificate_search(
    transitions: list[Counter[tuple[int, ...]]],
    root_counter: Counter[tuple[int, ...]],
):
    for y in Y_CANDIDATES:
        q = [0] * len(transitions)
        disposition = "ITER_LIMIT"
        fixed_iteration = None

        for iteration in range(1, ITER_CAP + 1):
            nxt = [map_coordinate_int(counter, q, y) for counter in transitions]
            assert all(nxt[i] >= q[i] for i in range(len(q)))

            if max(nxt, default=0) > COORD_CAP_INT:
                disposition = "COORD_CAP"
                break

            if nxt == q:
                disposition = "FIXED"
                fixed_iteration = iteration
                break

            q = nxt

        print(
            "Y_ATTEMPT "
            f"y={y} disposition={disposition} iterations={fixed_iteration or iteration} "
            f"max_q={Fraction(max(q, default=0), Q)}"
        )

        if disposition != "FIXED":
            continue

        assert all(
            exact_component_holds(counter, q, y, q[sid])
            for sid, counter in enumerate(transitions)
        )

        h_bound = root_bound(root_counter, q, y)
        prefactor = h_bound / 2

        if y > 1:
            print(
                "CONTEXT_GRAMMAR_CERTIFICATE PASS "
                f"y={y} tail_factor={1/y} root_bound={h_bound} "
                f"probability_prefactor={prefactor} iterations={fixed_iteration}"
            )
            print(
                "TAIL_FORM "
                "P(k>=R,rooted_face_simple_tree_boundary)<="
                f"{prefactor}*({1/y})^R"
            )
            print("AUDIT PASS; context_tree_tail=CERTIFIED; Xi=OPEN; P1=OPEN")
        else:
            print(
                "CONTEXT_GRAMMAR_CERTIFICATE FINITE_ONLY "
                f"root_bound={h_bound} probability_prefactor={prefactor} "
                f"iterations={fixed_iteration}"
            )
            print("AUDIT PASS; context_tree_total=FINITE_NO_MARGIN; Xi=OPEN; P1=OPEN")
        return

    print("CONTEXT_GRAMMAR_CERTIFICATE NONE")
    print("AUDIT PASS; context_grammar_protocol=NO_CERTIFICATE; Xi=OPEN; P1=OPEN")


def main() -> None:
    _, transitions, root_counter = build_grammar()
    certificate_search(transitions, root_counter)


if __name__ == "__main__":
    main()
