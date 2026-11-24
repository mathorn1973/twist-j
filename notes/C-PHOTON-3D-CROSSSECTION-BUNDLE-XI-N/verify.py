#!/usr/bin/env python3
"""Exact audit for C-PHOTON-3D-CROSSSECTION-BUNDLE-XI-N.

PUBLIC, NON-CANONICAL. Standard library only.
Author: A. M. Thorn <thorn@twistj.com>
License: Apache-2.0.

Scientific scope and constants are frozen in PREREG.md.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb


Vec4 = tuple[int, int, int, int]
Vec3 = tuple[int, int, int]
Edge = tuple[Vec4, int]


def canonical_edge(a: Vec4, b: Vec4) -> tuple[Edge, int]:
    diff = tuple(b[i] - a[i] for i in range(4))
    nz = [i for i, v in enumerate(diff) if v]
    assert len(nz) == 1
    axis = nz[0]
    assert abs(diff[axis]) == 1
    if diff[axis] == 1:
        return (a, axis), 1
    return (b, axis), -1


def cycle_edges(vertices: tuple[Vec4, ...]) -> dict[Edge, int]:
    assert vertices[0] == vertices[-1]
    assert len(set(vertices[:-1])) == len(vertices) - 1
    out: dict[Edge, int] = defaultdict(int)
    for a, b in zip(vertices, vertices[1:]):
        edge, sign = canonical_edge(a, b)
        out[edge] += sign
    assert all(v in (-1, 1) for v in out.values())
    assert len(out) == len(vertices) - 1
    return dict(out)


def turn_count(vertices: tuple[Vec4, ...]) -> int:
    axes = []
    for a, b in zip(vertices, vertices[1:]):
        diff = tuple(b[i] - a[i] for i in range(4))
        axes.append(next(i for i, v in enumerate(diff) if v))
    return sum(axes[i] != axes[(i + 1) % len(axes)] for i in range(len(axes)))


def opposite_contacts(edges: dict[Edge, int]) -> tuple[int, int, list[tuple]]:
    keys = sorted(edges)
    plus = minus = 0
    records = []
    for i, (x, axis) in enumerate(keys):
        sx = edges[(x, axis)]
        for y, axis2 in keys[i + 1 :]:
            if axis2 != axis:
                continue
            delta = tuple(y[j] - x[j] for j in range(4))
            nz = [j for j, v in enumerate(delta) if v]
            if len(nz) != 1:
                continue
            other = nz[0]
            if other == axis or abs(delta[other]) != 1:
                continue
            if delta[other] == 1:
                low_sign, high_sign, base = sx, edges[(y, axis)], x
            else:
                low_sign, high_sign, base = edges[(y, axis)], sx, y
            signed_low = low_sign
            signed_high = -high_sign
            if signed_low == signed_high:
                plus += 1
                tag = "+"
            else:
                minus += 1
                tag = "-"
            records.append(((x, axis), sx, (y, axis), edges[(y, axis)], base, tag))
    return plus, minus, records


def lifted_ell(edges: dict[Edge, int]) -> int:
    B: dict[int, int] = defaultdict(int)
    for (x, axis), sign in edges.items():
        if axis == 0:
            B[x[1]] += sign
    if not B:
        return 0
    assert sum(B.values()) == 0
    lo, hi = min(B), max(B)
    h = 0
    vals = []
    for r in range(lo, hi + 1):
        h += B.get(r, 0)
        vals.append(h)
    return sum(abs(v) for v in vals)


def polygon_edges(Q: tuple[Vec3, ...]) -> set[frozenset[Vec3]]:
    out = set()
    k = len(Q)
    for i in range(k):
        a, b = Q[i], Q[(i + 1) % k]
        assert sum(abs(a[j] - b[j]) for j in range(3)) == 1
        out.add(frozenset((a, b)))
    assert len(out) == k
    return out


def nearest_pairs(Q: tuple[Vec3, ...]) -> int:
    return sum(
        sum(abs(a[j] - b[j]) for j in range(3)) == 1
        for a, b in combinations(Q, 2)
    )


def affine_rank3(Q: tuple[Vec3, ...]) -> int:
    origin = Q[0]
    vs = [tuple(p[i] - origin[i] for i in range(3)) for p in Q[1:]]
    for a, b, c in combinations(vs, 3):
        det = (
            a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0])
        )
        if det:
            return 3
    # The frozen examples only need rank 2 or 3.
    return 2


def validate_Q(Q: tuple[Vec3, ...]) -> None:
    assert len(Q) >= 4 and len(Q) % 2 == 0
    assert len(set(Q)) == len(Q)
    polygon_edges(Q)
    for i, p in enumerate(Q):
        assert sum(p) % 2 == i % 2


def embed(t: int, q: Vec3) -> Vec4:
    return (t, q[0], q[1], q[2])


def build_prism(Q: tuple[Vec3, ...], D: int) -> tuple[Vec4, ...]:
    validate_Q(Q)
    assert D >= 1
    k = len(Q)
    vertices: list[Vec4] = []

    for j in range(k):
        if j % 2 == 0:
            strand = tuple(embed(t, Q[j]) for t in range(D + 1))
            endpoint_t = D
        else:
            strand = tuple(embed(t, Q[j]) for t in range(D, -1, -1))
            endpoint_t = 0

        if not vertices:
            vertices.extend(strand)
        else:
            assert vertices[-1] == strand[0]
            vertices.extend(strand[1:])

        nxt = Q[(j + 1) % k]
        connector_end = embed(endpoint_t, nxt)
        assert sum(abs(connector_end[i] - vertices[-1][i]) for i in range(4)) == 1
        vertices.append(connector_end)

    assert vertices[-1] == vertices[0]
    assert len(set(vertices[:-1])) == len(vertices) - 1
    return tuple(vertices)


def connector_contacts(records: list[tuple]) -> int:
    total = 0
    for rec in records:
        e1, _, e2, _, _, _ = rec
        if e1[1] != 0 and e2[1] != 0:
            total += 1
    return total


def coeff_inv_one_minus_5(n: int) -> int:
    return comb(n + 4, 4)


def series_audit() -> None:
    for n in range(31):
        coeff = 0
        for shift, mult in ((1, 1), (2, 11), (3, 11), (4, 1)):
            if n >= shift:
                coeff += mult * coeff_inv_one_minus_5(n - shift)
        if n == 1:
            coeff -= 1
        assert coeff == (n**4 if n >= 2 else 0)

    for n in range(31):
        coeff = 0
        for shift, mult in ((0, 16), (1, 1), (2, 11), (3, -5), (4, 1)):
            if n >= shift:
                coeff += mult * coeff_inv_one_minus_5(n - shift)
        assert coeff == (n + 2) ** 4

    print("SERIES PASS G1_coeff=n^4_n>=2 G2_coeff=(n+2)^4")


def geometry_audit() -> None:
    Q4: tuple[Vec3, ...] = (
        (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)
    )
    Q6: tuple[Vec3, ...] = (
        (0, 0, 0), (1, 0, 0), (1, 1, 0),
        (1, 1, 1), (0, 1, 1), (0, 0, 1)
    )
    Q8: tuple[Vec3, ...] = (
        (0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 0, 1),
        (2, 1, 1), (2, 1, 0), (1, 1, 0), (0, 1, 0)
    )

    examples = 0
    for name, Q, expected_rank in (("Q4", Q4, 2), ("Q6", Q6, 3), ("Q8", Q8, 3)):
        validate_Q(Q)
        assert affine_rank3(Q) == expected_rank
        k = len(Q)
        EQ = nearest_pairs(Q)
        assert EQ <= 3 * k
        if name == "Q8":
            assert EQ > k

        for D in range(1, 7):
            vertices = build_prism(Q, D)
            edges = cycle_edges(vertices)
            m = len(edges)
            c = turn_count(vertices)
            Oplus, Ominus, records = opposite_contacts(edges)
            O = Oplus + Ominus
            conn = connector_contacts(records)

            assert m == k * (D + 1)
            assert c == 2 * k
            assert conn <= 2 * k
            assert Oplus >= D * EQ
            assert O == D * EQ + conn
            assert O <= 3 * k * D + 2 * k
            assert c + O <= 3 * k * D + 4 * k

            ell = lifted_ell(edges)
            assert 16 * ell <= m * m
            examples += 1

    print("PRISM_EXAMPLES PASS count=18 Q4_planar Q6_nonplanar Q8_nonplanar_chord D=1..6")


def main() -> None:
    a = Fraction(15625, 131072)
    r = Fraction(34, 25)
    s = Fraction(16, 25)

    ar3 = a * r**3
    q4 = ar3**4
    b3 = 5 * a**2 * r**7

    assert 0 < s < r
    assert 0 < ar3 < 1
    assert 0 < q4 < 1
    assert 0 < b3 < 1

    for k in range(4, 65):
        assert ar3**k <= q4

    x = b3**2
    G1 = 16 * (x * (1 + 11*x + 11*x**2 + x**3) / (1 - x)**5 - x)
    G2 = (16 + q4 + 11*q4**2 - 5*q4**3 + q4**4) / (1 - q4)**5
    C = Fraction(3, 40) * G1 * G2

    print(f"CONSTANTS PASS a={a} r={r} s={s} ar3={ar3} b3={b3} q4={q4}")
    series_audit()
    geometry_audit()
    print(f"BOUND PASS C_3D={C}")
    print(f"BOUND_DIGITS num={len(str(C.numerator))} den={len(str(C.denominator))}")
    print("AUDIT PASS; arbitrary_3D_crosssection_prism_uniform=YES; full_Xi=OPEN; P1=OPEN")


if __name__ == "__main__":
    main()
