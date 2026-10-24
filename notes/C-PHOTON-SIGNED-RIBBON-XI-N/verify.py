#!/usr/bin/env python3
"""Exact audit for C-PHOTON-SIGNED-RIBBON-XI-N.

PUBLIC, NON-CANONICAL. Standard library only.
Author: A. M. Thorn <thorn@twistj.com>
License: Apache-2.0.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb


Point = tuple[int, int, int, int]
EdgeKey = tuple[Point, int]


def add(p: Point, s: Point) -> Point:
    return tuple(p[i] + s[i] for i in range(4))  # type: ignore[return-value]


def unit(axis: int, sign: int = 1) -> Point:
    return tuple(sign if i == axis else 0 for i in range(4))  # type: ignore[return-value]


def constants():
    a = Fraction(15625, 177147)
    r = Fraction(41, 25)
    q = a * a * r * (1 + 4 * r * r)
    assert 0 < q < 1
    print(f"CONSTANTS PASS a={a} r={r} q_rib={q}")
    return a, r, q


def ribbon_sum(q: Fraction) -> Fraction:
    return (
        (16 + q + 11*q*q - 5*q**3 + q**4) / (1-q)**5
        - 16
    )


def series_audit(q: Fraction) -> None:
    # Independent coefficient check:
    # sum_{D>=1}(D+1)^4 q^(D-1) has the displayed rational form before -16.
    # Coefficient of q^k in the rational numerator/(1-q)^5.
    num = (16, 1, 11, -5, 1)
    for k in range(20):
        coeff = 0
        for j, c in enumerate(num):
            if k >= j:
                coeff += c * comb(k-j+4, 4)
        assert coeff == (k+2)**4
    assert ribbon_sum(q) > 0
    print("SERIES PASS coefficients_k0_to_19=(k+2)^4")


def cycle_edges(vertices: tuple[Point, ...]) -> dict[EdgeKey, int]:
    assert len(vertices) == len(set(vertices))
    n = len(vertices)
    edges: dict[EdgeKey, int] = {}
    for i, p in enumerate(vertices):
        q = vertices[(i+1) % n]
        diff = tuple(q[j]-p[j] for j in range(4))
        axes = [j for j, d in enumerate(diff) if d]
        assert len(axes) == 1
        axis = axes[0]
        assert abs(diff[axis]) == 1
        if diff[axis] == 1:
            key, coeff = (p, axis), 1
        else:
            key, coeff = (q, axis), -1
        assert key not in edges
        edges[key] = coeff
    return edges


def plaquette_boundary(base: Point, a: int, b: int) -> dict[EdgeKey, int]:
    assert a < b
    ea, eb = unit(a), unit(b)
    return {
        (add(base, ea), b): 1,
        (base, b): -1,
        (add(base, eb), a): -1,
        (base, a): 1,
    }


def contact_counts(vertices: tuple[Point, ...]) -> tuple[int, int]:
    edges = list(cycle_edges(vertices).items())
    op = om = 0
    for i, ((x, axis), cx) in enumerate(edges):
        for (y, axis2), cy in edges[i+1:]:
            if axis != axis2:
                continue
            diff = tuple(y[k]-x[k] for k in range(4))
            nz = [k for k, d in enumerate(diff) if d]
            if len(nz) != 1:
                continue
            b = nz[0]
            if b == axis or abs(diff[b]) != 1:
                continue
            low = x if diff[b] == 1 else y
            aa, bb = sorted((axis, b))
            bd = plaquette_boundary(low, aa, bb)
            kx, ky = (x, axis), (y, axis)
            sx = cx * bd[kx]
            sy = cy * bd[ky]
            if sx == sy:
                op += 1
            else:
                om += 1
    return op, om


def turn_count(vertices: tuple[Point, ...]) -> int:
    n = len(vertices)
    axes = []
    for i, p in enumerate(vertices):
        q = vertices[(i+1)%n]
        diff = tuple(q[j]-p[j] for j in range(4))
        axes.append(next(j for j,d in enumerate(diff) if d))
    return sum(axes[i] != axes[i-1] for i in range(n))


def ell_axis01(vertices: tuple[Point, ...]) -> int:
    edges = cycle_edges(vertices)
    x1s = [p[1] for p in vertices]
    lo, hi = min(x1s), max(x1s)
    L = 2*len(vertices)+7
    offset = len(vertices)+2-lo
    B = [0]*L
    for (x, axis), coeff in edges.items():
        if axis == 0:
            B[x[1]+offset] += coeff
    assert sum(B) == 0
    H = [0]*L
    for r in range(1,L):
        H[r] = H[r-1] + B[r]
    assert H[0]-H[-1] == B[0]
    med = sorted(H)[L//2]
    return sum(abs(v-med) for v in H)


def make_ribbon(D: int, bent: bool) -> tuple[Point, ...]:
    assert D >= 2
    b = 1
    p: list[Point] = [(0,0,0,0)]
    if not bent:
        steps = [0]*D
    else:
        assert D >= 3
        first = D//2
        steps = [0]*first + [2]*(D-first)

    cur = p[0]
    for ax in steps:
        cur = add(cur, unit(ax))
        p.append(cur)

    eb = unit(b)
    translated = [add(x, eb) for x in p]
    vertices = tuple(p + list(reversed(translated)))
    # p includes both endpoints; concatenation gives connector at far end
    # and cyclic closing edge gives near connector.
    assert len(vertices) == 2*(D+1)
    return vertices


def example_audit() -> None:
    count = 0
    for D in range(2,9):
        for bent in ((False, True) if D>=3 else (False,)):
            cyc = make_ribbon(D,bent)
            edges = cycle_edges(cyc)
            assert len(edges) == 2*D+2
            op, om = contact_counts(cyc)
            c = turn_count(cyc)
            cp = 1 if bent else 0
            assert op == D
            assert om == 0
            assert c == 2*cp + 4
            ell = ell_axis01(cyc)
            m = len(cyc)
            assert 16*ell <= m*m
            count += 1
    print(f"RIBBON_EXAMPLES PASS count={count} D=2..8 straight_and_one_turn")


def outside_sc_audit(r: Fraction) -> None:
    tau = Fraction(73,70)
    first = None
    for D in range(2,10000):
        if r**D > tau**(2*D+2):
            first = D
            break
    assert first is not None
    print(f"SC_COMPLEMENT PASS first_D={first} r^D>tau^(2D+2)")


def bound_audit(a: Fraction, r: Fraction, q: Fraction) -> None:
    C = 6 * a**4 * r**5 * ribbon_sum(q)
    assert C > 0
    print(f"BOUND PASS C_rib={C}")
    print(f"BOUND_DIGITS num={len(str(C.numerator))} den={len(str(C.denominator))}")


def main() -> None:
    a,r,q = constants()
    series_audit(q)
    example_audit()
    outside_sc_audit(r)
    bound_audit(a,r,q)
    print("AUDIT PASS; high_contact_ribbon_uniform=YES; full_Xi=OPEN; P1=OPEN")


if __name__ == "__main__":
    main()
