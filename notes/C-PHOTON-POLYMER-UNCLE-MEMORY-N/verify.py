#!/usr/bin/env python3
"""Exact audit for C-PHOTON-POLYMER-UNCLE-MEMORY-N.

PUBLIC, NON-CANONICAL. Standard library only.
Author: A. M. Thorn <thorn@twistj.com>
License: Apache-2.0.

The scope and frozen supersolution family are in PREREG.md.
"""

from __future__ import annotations

from functools import lru_cache
from fractions import Fraction
from itertools import combinations
from math import lcm


Vec = tuple[int, int, int, int]
Axes2 = tuple[int, int]
Axes3 = tuple[int, int, int]
Face = tuple[Vec, Axes2]
Cell = tuple[Vec, Axes3]


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
    for face in sorted(cell_faces(parent)):
        inc = set(incident_cells(face))
        assert parent in inc
        inc.remove(parent)
        assert len(inc) == 3
        groups.append((face, tuple(sorted(inc))))
    assert len(groups) == 6
    flat = [c for _, group in groups for c in group]
    assert len(flat) == 18
    assert len(set(flat)) == 18
    return tuple(groups)


def candidates_excluding_interface(current: Cell, parent: Cell) -> tuple[Cell, ...]:
    shared = cell_faces(current) & cell_faces(parent)
    assert len(shared) == 1
    interface = next(iter(shared))
    out = []
    for face, group in child_groups(current):
        if face == interface:
            continue
        out.extend(group)
    assert len(out) == 15
    assert len(set(out)) == 15
    return tuple(out)


def conflict_masks(candidates: tuple[Cell, ...]) -> tuple[int, ...]:
    faces = [cell_faces(c) for c in candidates]
    masks = [0] * len(candidates)
    for i, j in combinations(range(len(candidates)), 2):
        if faces[i] & faces[j]:
            masks[i] |= 1 << j
            masks[j] |= 1 << i
    return tuple(masks)


def independent_masks(conflicts: tuple[int, ...]):
    n = len(conflicts)
    for mask in range(1 << n):
        rest = mask
        ok = True
        while rest:
            low = rest & -rest
            i = low.bit_length() - 1
            if conflicts[i] & mask:
                ok = False
                break
            rest ^= low
        if ok:
            yield mask


def add_polys(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def shift_poly(a: tuple[int, ...]) -> tuple[int, ...]:
    return (0,) + a


def independent_set_poly_from_conflicts(conflicts: tuple[int, ...]) -> tuple[int, ...]:
    @lru_cache(None)
    def rec(mask: int) -> tuple[int, ...]:
        if mask == 0:
            return (1,)
        low = mask & -mask
        v = low.bit_length() - 1
        without_v = rec(mask ^ low)
        without_closed_neighborhood = rec(mask & ~low & ~conflicts[v])
        return add_polys(without_v, shift_poly(without_closed_neighborhood))

    poly = rec((1 << len(conflicts)) - 1)
    assert sum(poly) == sum(1 for _ in independent_masks(conflicts))
    return poly


POLY_CACHE: dict[tuple[Cell, ...], tuple[int, ...]] = {}


def normalized_candidates(current: Cell, candidates: tuple[Cell, ...]) -> tuple[Cell, ...]:
    x, _ = current
    delta = tuple(-v for v in x)
    return tuple(sorted(translate_cell(c, delta) for c in candidates))


def cached_poly(current: Cell, candidates: tuple[Cell, ...]) -> tuple[int, ...]:
    key = normalized_candidates(current, candidates)
    if key not in POLY_CACHE:
        POLY_CACHE[key] = independent_set_poly_from_conflicts(conflict_masks(key))
    return POLY_CACHE[key]


def pad6(poly: tuple[int, ...]) -> tuple[int, ...]:
    assert len(poly) <= 6
    return poly + (0,) * (6 - len(poly))


def componentwise_max(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    aa, bb = pad6(a), pad6(b)
    return tuple(max(x, y) for x, y in zip(aa, bb))


def context_tables():
    root: Cell = ((0, 0, 0, 0), (0, 1, 2))
    groups = child_groups(root)
    root_candidates = tuple(c for _, group in groups for c in group)
    p6 = independent_set_poly_from_conflicts(conflict_masks(root_candidates))
    assert p6 == (1, 18, 111, 308, 429, 294, 79)

    per_entry_tables = []
    per_entry_counts = []
    unique_before = len(POLY_CACHE)

    for entry_index in range(6):
        parent_candidates = tuple(
            c
            for i, (_, group) in enumerate(groups)
            if i != entry_index
            for c in group
        )
        assert len(parent_candidates) == 15
        pconf = conflict_masks(parent_candidates)

        table = [(0, 0, 0, 0, 0, 0) for _ in range(5)]
        counts = [0] * 5

        for mask in independent_masks(pconf):
            b = mask.bit_count()
            if b == 0:
                continue
            selected_indices = [i for i in range(15) if mask & (1 << i)]
            selected = [parent_candidates[i] for i in selected_indices]

            for current in selected:
                uncles = tuple(c for c in selected if c != current)
                u = len(uncles)
                assert 0 <= u <= 4
                candidates = candidates_excluding_interface(current, root)
                survivors = tuple(
                    child
                    for child in candidates
                    if all(not (cell_faces(child) & cell_faces(uncle)) for uncle in uncles)
                )
                poly = pad6(cached_poly(current, survivors))
                table[u] = componentwise_max(table[u], poly)
                counts[u] += 1

        assert all(count > 0 for count in counts)
        per_entry_tables.append(tuple(table))
        per_entry_counts.append(tuple(counts))

    assert all(table == per_entry_tables[0] for table in per_entry_tables)
    assert all(counts == per_entry_counts[0] for counts in per_entry_counts)

    B = per_entry_tables[0]
    counts = per_entry_counts[0]

    # Root six-child contexts have five uncles per child. They are special
    # because non-root cubes have at most five available exit faces.
    rconf = conflict_masks(root_candidates)
    root5_max = (0, 0, 0, 0, 0, 0)
    root5_contexts = 0
    for mask in independent_masks(rconf):
        if mask.bit_count() != 6:
            continue
        selected = [root_candidates[i] for i in range(18) if mask & (1 << i)]
        assert len(selected) == 6
        for current in selected:
            uncles = tuple(c for c in selected if c != current)
            assert len(uncles) == 5
            candidates = candidates_excluding_interface(current, root)
            survivors = tuple(
                child
                for child in candidates
                if all(not (cell_faces(child) & cell_faces(uncle)) for uncle in uncles)
            )
            poly = pad6(cached_poly(current, survivors))
            root5_max = componentwise_max(root5_max, poly)
            root5_contexts += 1

    assert root5_contexts == 6 * p6[6]
    assert all(root5_max[i] <= B[4][i] for i in range(6))

    print(
        "CONTEXTS PASS "
        f"per_entry={sum(counts)} by_type={','.join(str(x) for x in counts)} "
        f"unique_filtered_graphs={len(POLY_CACHE)-unique_before}"
    )
    for u, row in enumerate(B):
        print(f"B{u} " + ",".join(str(x) for x in row))
    print("ROOT5 " + ",".join(str(x) for x in root5_max) + f" contexts={root5_contexts}")
    print("P6 " + ",".join(str(x) for x in p6))
    return B, p6


R_CANDIDATES = (
    Fraction(15, 16),
    Fraction(7, 8),
    Fraction(13, 16),
    Fraction(3, 4),
    Fraction(11, 16),
    Fraction(5, 8),
    Fraction(9, 16),
    Fraction(1, 2),
    Fraction(7, 16),
    Fraction(3, 8),
    Fraction(5, 16),
    Fraction(1, 4),
)

Y_CANDIDATES = (
    Fraction(17, 16),
    Fraction(33, 32),
    Fraction(65, 64),
    Fraction(129, 128),
    Fraction(257, 256),
    Fraction(1, 1),
)


def build_integer_polynomial(row: tuple[int, ...], r: Fraction, qden: int = 4096):
    # F_u(q-vector) before multiplying by z:
    # row[0] + sum_b row[b] * (q*r^(b-1))^b.
    fractions = [Fraction(row[0], 1)]
    for b in range(1, 6):
        fractions.append(Fraction(row[b], qden**b) * (r ** (b * (b - 1))))
    common = 1
    for c in fractions:
        common = lcm(common, c.denominator)
    ints = tuple(c.numerator * (common // c.denominator) for c in fractions)
    return ints, common


def eval_int_poly(coeffs: tuple[int, ...], m: int) -> int:
    total = 0
    for coefficient in reversed(coeffs):
        total = total * m + coefficient
    return total


def component_holds(
    row_poly: tuple[int, ...],
    common: int,
    u: int,
    y: Fraction,
    r: Fraction,
    m: int,
    qden: int = 4096,
) -> bool:
    value_num = eval_int_poly(row_poly, m)
    # z*F <= (m/qden)*r^u, z=y/16.
    left = y.numerator * value_num * qden * (r.denominator**u)
    right = 16 * y.denominator * common * m * (r.numerator**u)
    return left <= right


def frac_row_value(row: tuple[int, ...], qvec: tuple[Fraction, ...]) -> Fraction:
    out = Fraction(row[0], 1)
    for b in range(1, 6):
        out += row[b] * (qvec[b - 1] ** b)
    return out


def certificate_search(B: tuple[tuple[int, ...], ...], p6: tuple[int, ...]):
    qden = 4096
    found = None

    for y in Y_CANDIDATES:
        z = y / 16
        for r in R_CANDIDATES:
            compiled = [build_integer_polynomial(B[u], r, qden) for u in range(5)]
            for m in range(1, 32768 + 1):
                if all(
                    component_holds(poly, common, u, y, r, m, qden)
                    for u, (poly, common) in enumerate(compiled)
                ):
                    found = (y, r, Fraction(m, qden))
                    break
            if found is not None:
                break
        if found is not None:
            break

    if found is None:
        print("UNCLE_MEMORY_CERTIFICATE NONE")
        print("AUDIT PASS; uncle_memory_ansatz=NO_CERTIFICATE; Xi=OPEN; P1=OPEN")
        return None

    y, r, q = found
    z = y / 16
    qvec = tuple(q * (r**u) for u in range(5))

    for u in range(5):
        assert z * frac_row_value(B[u], qvec) <= qvec[u]

    root_inner = Fraction(p6[0], 1)
    for b in range(1, 6):
        root_inner += p6[b] * (qvec[b - 1] ** b)
    root_inner += p6[6] * (qvec[4] ** 6)
    root_bound = z * root_inner
    prefactor = root_bound / 2

    if y > 1:
        print(
            "UNCLE_MEMORY_CERTIFICATE PASS "
            f"y={y} r={r} q={q} tail_factor={1/y} "
            f"probability_prefactor={prefactor}"
        )
        print(
            "TAIL_FORM "
            "P(k>=R,rooted_face_simple_tree_boundary)<="
            f"{prefactor}*({1/y})^R"
        )
        print("AUDIT PASS; uncle_memory_tree_tail=CERTIFIED; Xi=OPEN; P1=OPEN")
    else:
        print(
            "UNCLE_MEMORY_CERTIFICATE FINITE_ONLY "
            f"y=1 r={r} q={q} probability_prefactor={prefactor}"
        )
        print("AUDIT PASS; uncle_memory_total_activity=FINITE_NO_MARGIN; Xi=OPEN; P1=OPEN")
    return found


def main() -> None:
    B, p6 = context_tables()
    certificate_search(B, p6)


if __name__ == "__main__":
    main()
