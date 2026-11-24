#!/usr/bin/env python3
"""Exact audit for C-PHOTON-POLYMER-TREE-ACTIVITY-N.

PUBLIC, NON-CANONICAL. Standard library only.
Author: A. M. Thorn <thorn@twistj.com>
License: Apache-2.0.

Scientific scope and the frozen certificate grid are in PREREG.md.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


Vec = tuple[int, int, int, int]
Axes2 = tuple[int, int]
Axes3 = tuple[int, int, int]
Face = tuple[Vec, Axes2]
Cell = tuple[Vec, Axes3]


def shift(x: Vec, axis: int, amount: int) -> Vec:
    return tuple(v + (amount if i == axis else 0) for i, v in enumerate(x))  # type: ignore[return-value]


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


def root_candidates():
    root: Cell = ((0, 0, 0, 0), (0, 1, 2))
    faces = tuple(sorted(cell_faces(root)))
    by_face: list[tuple[Cell, ...]] = []
    seen: set[Cell] = set()
    for face in faces:
        inc = set(incident_cells(face))
        assert root in inc
        inc.remove(root)
        assert len(inc) == 3
        children = tuple(sorted(inc))
        assert not (seen & set(children))
        seen.update(children)
        by_face.append(children)
    assert len(seen) == 18
    return root, faces, tuple(by_face)


def conflict_masks(candidates: tuple[Cell, ...]) -> tuple[int, ...]:
    faces = [cell_faces(c) for c in candidates]
    masks = [0] * len(candidates)
    for i, j in combinations(range(len(candidates)), 2):
        if faces[i] & faces[j]:
            masks[i] |= 1 << j
            masks[j] |= 1 << i
    return tuple(masks)


def independent_set_poly(candidates: tuple[Cell, ...]) -> tuple[int, ...]:
    conflicts = conflict_masks(candidates)
    counts = [0] * (len(candidates) + 1)
    for mask in range(1 << len(candidates)):
        ok = True
        rest = mask
        while rest:
            low = rest & -rest
            i = low.bit_length() - 1
            if conflicts[i] & mask:
                ok = False
                break
            rest ^= low
        if ok:
            counts[mask.bit_count()] += 1
    while counts and counts[-1] == 0:
        counts.pop()
    assert counts and counts[0] == 1
    return tuple(counts)


def conflict_edge_count(candidates: tuple[Cell, ...]) -> int:
    masks = conflict_masks(candidates)
    return sum(mask.bit_count() for mask in masks) // 2


def cubical_local_audit():
    root, faces, by_face = root_candidates()
    assert len(faces) == 6
    assert all(len(incident_cells(face)) == 4 for face in faces)

    root_candidates_flat = tuple(c for group in by_face for c in group)
    assert len(root_candidates_flat) == 18
    assert len(set(root_candidates_flat)) == 18

    p6 = independent_set_poly(root_candidates_flat)
    e6 = conflict_edge_count(root_candidates_flat)

    planted = []
    p5s = []
    e5s = []
    for parent_index in range(6):
        candidates = tuple(
            c for face_index, group in enumerate(by_face)
            if face_index != parent_index
            for c in group
        )
        assert len(candidates) == 15
        assert len(set(candidates)) == 15
        planted.append(candidates)
        p5s.append(independent_set_poly(candidates))
        e5s.append(conflict_edge_count(candidates))

    assert all(poly == p5s[0] for poly in p5s)
    assert all(edges == e5s[0] for edges in e5s)

    p5 = p5s[0]

    # At most one child can be selected across a fixed face because all three
    # candidates there share that root plaquette.
    for group in by_face:
        g = tuple(group)
        masks = conflict_masks(g)
        assert all(mask.bit_count() == 2 for mask in masks)

    print(f"LOCAL_CELLS PASS root_faces=6 incident_per_face=4 root_children=18 planted_children=15")
    print(f"CONFLICTS root_edges={e6} planted_edges={e5s[0]}")
    print("P6 " + ",".join(str(x) for x in p6))
    print("P5 " + ",".join(str(x) for x in p5))
    return p5, p6


def series_add(a: list[int], b: list[int], n: int) -> list[int]:
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n + 1)]


def series_mul(a: list[int], b: list[int], n: int) -> list[int]:
    out = [0] * (n + 1)
    for i, ai in enumerate(a[: n + 1]):
        if not ai:
            continue
        for j, bj in enumerate(b[: n + 1 - i]):
            if bj:
                out[i + j] += ai * bj
    return out


def series_pow(a: list[int], power: int, n: int) -> list[int]:
    out = [0] * (n + 1)
    out[0] = 1
    base = a[:]
    p = power
    while p:
        if p & 1:
            out = series_mul(out, base, n)
        p >>= 1
        if p:
            base = series_mul(base, base, n)
    return out


def compose_poly(coeffs: tuple[int, ...], t: list[int], n: int) -> list[int]:
    out = [0] * (n + 1)
    for power, coefficient in enumerate(coeffs):
        if not coefficient:
            continue
        term = series_pow(t, power, n)
        for i in range(n + 1):
            out[i] += coefficient * term[i]
    return out


def shifted_by_z(a: list[int], n: int) -> list[int]:
    return [0] + a[:n]


def recursive_series_audit(p5: tuple[int, ...], p6: tuple[int, ...], n: int = 12):
    t = [0] * (n + 1)
    for _ in range(n + 1):
        t = shifted_by_z(compose_poly(p5, t, n), n)

    h = shifted_by_z(compose_poly(p6, t, n), n)

    assert h[1] == 1
    for k in range(2, n + 1):
        path_descriptions = 18 * 15 ** (k - 2)
        assert h[k] >= path_descriptions

    print("SERIES PASS degree=12")
    print("H_COEFF " + ",".join(str(h[k]) for k in range(1, n + 1)))
    return h


def polynomial_scaled_numerator(coeffs: tuple[int, ...], m: int, qden: int) -> tuple[int, int]:
    """Return P(m/qden) as numerator/denominator without reduction."""
    degree = len(coeffs) - 1
    numerator = 0
    for i, a in enumerate(coeffs):
        numerator += a * (m ** i) * (qden ** (degree - i))
    denominator = qden ** degree
    return numerator, denominator


def cert_holds(coeffs: tuple[int, ...], y: Fraction, m: int, qden: int = 4096) -> bool:
    pnum, pden = polynomial_scaled_numerator(coeffs, m, qden)
    # z=(y/16); require z*P(q) <= q=m/qden.
    return y.numerator * pnum * qden <= 16 * y.denominator * m * pden


def poly_eval_fraction(coeffs: tuple[int, ...], q: Fraction) -> Fraction:
    out = Fraction(0)
    power = Fraction(1)
    for a in coeffs:
        out += a * power
        power *= q
    return out


Y_CANDIDATES = (
    Fraction(2, 1),
    Fraction(3, 2),
    Fraction(5, 4),
    Fraction(9, 8),
    Fraction(17, 16),
    Fraction(33, 32),
    Fraction(65, 64),
    Fraction(129, 128),
    Fraction(257, 256),
)


def certificate_audit(p5: tuple[int, ...], p6: tuple[int, ...]):
    qden = 4096
    best = None
    for y in Y_CANDIDATES:
        found = None
        for m in range(1, 32768 + 1):
            if cert_holds(p5, y, m, qden):
                found = m
                break
        if found is not None:
            best = (y, Fraction(found, qden))
            break

    if best is None:
        print("LOCAL_TREE_CERTIFICATE NONE")
        print("AUDIT PASS; local_majorant=NO_CERTIFICATE; Xi=OPEN; P1=OPEN")
        return None

    y, q = best
    z = y / 16
    assert z * poly_eval_fraction(p5, q) <= q
    root_bound = z * poly_eval_fraction(p6, q)
    probability_prefactor = root_bound / 2
    assert y > 1
    assert probability_prefactor > 0

    print(
        "LOCAL_TREE_CERTIFICATE PASS "
        f"y={y} q={q} tail_factor={Fraction(1, 1) / y} "
        f"probability_prefactor={probability_prefactor}"
    )
    print(
        "TAIL_FORM "
        "P(k>=R,rooted_face_simple_tree_boundary)<="
        f"{probability_prefactor}*({Fraction(1,1)/y})^R"
    )
    print("AUDIT PASS; face_simple_tree_tail=CERTIFIED; Xi=OPEN; P1=OPEN")
    return best


def main() -> None:
    p5, p6 = cubical_local_audit()
    recursive_series_audit(p5, p6)
    certificate_audit(p5, p6)


if __name__ == "__main__":
    main()
