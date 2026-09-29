#!/usr/bin/env python3
"""Exact local audit for C-PHOTON-POLE-S1-S7-N; no phase simulation.

Standard library only. The arbitrary-volume argument belongs to TRANSFER.md.
This program audits finite premises and explicit negative controls, not the
spectrum of a many-link lattice or the actual photon residue.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from typing import Sequence

R = tuple[int, int, int, int]
ZERO: R = (0, 0, 0, 0)
ONE: R = (1, 0, 0, 0)
J: R = (0, 1, 0, 0)


def add(a: R, b: R) -> R:
    return tuple(x + y for x, y in zip(a, b))  # type: ignore[return-value]


def scale(n: int, a: R) -> R:
    return tuple(n * x for x in a)  # type: ignore[return-value]


def sub(a: R, b: R) -> R:
    return add(a, scale(-1, b))


def mul(a: R, b: R) -> R:
    c = [0] * 7
    for i in range(4):
        for k in range(4):
            c[i + k] += a[i] * b[k]
    for d in range(6, 3, -1):
        t = c[d]
        for k in range(d - 4, d):
            c[k] -= t
        c[d] = 0
    return tuple(c[:4])  # type: ignore[return-value]


def power(n: int) -> R:
    ans = ONE
    for _ in range(n % 5):
        ans = mul(ans, J)
    return ans


def rsum(xs: Sequence[R]) -> R:
    ans = ZERO
    for x in xs:
        ans = add(ans, x)
    return ans


def conjugate(a: R) -> R:
    return rsum([scale(a[k], power(-k)) for k in range(4)])


def dft(xs: Sequence[R]) -> list[R]:
    return [rsum([mul(xs[a], power(-r * a)) for a in range(5)])
            for r in range(5)]


def matmul(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def rank(a: list[list[F]]) -> int:
    b = [row[:] for row in a]
    r = 0
    for c in range(len(b[0])):
        pivot = next((i for i in range(r, len(b)) if b[i][c]), None)
        if pivot is None:
            continue
        b[r], b[pivot] = b[pivot], b[r]
        p = b[r][c]
        b[r] = [x / p for x in b[r]]
        for i in range(len(b)):
            if i != r:
                q = b[i][c]
                b[i] = [x - q * y for x, y in zip(b[i], b[r])]
        r += 1
        if r == len(b):
            break
    return r


def target_projector(n: tuple[F, F, F]) -> tuple[list[list[F]], list[list[F]]]:
    assert sum(x * x for x in n) == 1
    p = [[F(i == j) - n[i] * n[j] for j in range(3)] for i in range(3)]
    x, y, z = n
    c = [[F(0), -z, y], [z, F(0), -x], [-y, x, F(0)]]
    t = [[F(0) for _ in range(6)] for _ in range(6)]
    for i in range(3):
        for j in range(3):
            t[i][j] = p[i][j] / 2
            t[i][j + 3] = -c[i][j] / 2
            t[i + 3][j] = c[i][j] / 2
            t[i + 3][j + 3] = p[i][j] / 2
    return t, c


def check_junction() -> None:
    n = 3
    start = (0, 0, 0)
    finish = (1, 0, 0)
    paths = [((0, 1),), ((1, 1), (0, 1), (1, -1)),
             ((1, -1), (0, 1), (1, 1)),
             ((2, 1), (0, 1), (2, -1)),
             ((2, -1), (0, 1), (2, 1))]
    flow: dict[tuple[tuple[int, int, int], int], int] = {}
    for path in paths:
        pos = list(start)
        for axis, sign in path:
            if sign == -1:
                pos[axis] = (pos[axis] - 1) % n
            key = (tuple(pos), axis)
            assert key not in flow, "paths must be edge disjoint"
            flow[key] = sign
            if sign == 1:
                pos[axis] = (pos[axis] + 1) % n
        assert tuple(pos) == finish
    assert len(flow) == 13 and set(flow.values()) == {-1, 1}
    boundary = {x: 0 for x in product(range(n), repeat=3)}
    for (x, axis), value in flow.items():
        y = list(x)
        y[axis] = (y[axis] + 1) % n
        boundary[x] -= value
        boundary[tuple(y)] += value
    assert boundary[start] == -5 and boundary[finish] == 5
    assert all(v == 0 for x, v in boundary.items() if x not in (start, finish))
    assert all(v % 5 == 0 for v in boundary.values())
    assert any(v != 0 for v in boundary.values())


def main() -> None:
    assert power(5) == ONE and rsum([power(k) for k in range(5)]) == ZERO
    sqrt5 = add(ONE, scale(2, add(power(1), power(-1))))
    assert mul(sqrt5, sqrt5) == scale(5, ONE)
    w = [add(scale(2, ONE), add(power(a), power(-a))) for a in range(5)]
    g2 = add(scale(2, ONE), sqrt5)
    g = [ZERO, ONE, g2, scale(-1, g2), scale(-1, ONE)]
    s = [sub(power(-a), power(a)) for a in range(5)]
    wh, sh = dft(w), dft(s)
    assert wh == [scale(k, ONE) for k in (10, 5, 0, 0, 5)]
    assert sh == [scale(k, ONE) for k in (0, -5, 0, 0, 5)]
    # -i*kappa=(1-j)/(1+j): verify WG relation without division.
    for a in range(5):
        assert mul(sub(ONE, J), mul(w[a], g[a])) == mul(add(ONE, J), s[a])
    assert mul(w[1], w[2]) == ONE and sub(w[1], w[2]) == sqrt5
    print('PASS G1: five exact W, G and scaled-insertion Fourier identities')

    for r in range(5):
        for ap in range(5):
            for kernel, eigenvalues in ((w, wh), (s, sh)):
                lhs = rsum([mul(kernel[(ap - a) % 5], power(r * a))
                            for a in range(5)])
                assert lhs == mul(eigenvalues[r], power(r * ap))
        assert wh[r][0] >= 0
        assert -wh[r][0] <= sh[r][0] <= wh[r][0]
    assert all(w[-a % 5] == conjugate(w[a]) for a in range(5))
    assert all(s[-a % 5] == conjugate(s[a]) for a in range(5))
    print('PASS G2: complete one-link kernel eigenvectors, support and order bounds')

    permitted = set()
    stars = 0
    for rs in product((-1, 0, 1), repeat=6):
        div = sum(rs[3:]) - sum(rs[:3])
        gauge_sum = rsum([power(t * div) for t in range(5)])
        assert gauge_sum == (scale(5, ONE) if div % 5 == 0 else ZERO)
        if div % 5 == 0:
            permitted.add(div)
        stars += 1
    assert stars == 729 and permitted == {-5, 0, 5}
    print('PASS G3: all 729 star labels; gauge projection is mod five only')

    check_junction()
    print('PASS G4: N=3 edge-disjoint 13-link junction with boundary -5,+5')

    normals = [(F(1), F(0), F(0)), (F(0), F(1), F(0)),
               (F(0), F(0), F(1)), (F(1, 3), F(2, 3), F(2, 3)),
               (F(2, 7), F(3, 7), F(6, 7))]
    for normal in normals:
        t, c = target_projector(normal)
        assert matmul(t, t) == t and rank(t) == 2
        assert sum(t[i][i] for i in range(6)) == 2
        assert all(t[i][j] == t[j][i] for i in range(6) for j in range(6))
        for col in range(6):
            electric = [t[i][col] for i in range(3)]
            magnetic = [t[i + 3][col] for i in range(3)]
            assert sum(normal[i] * electric[i] for i in range(3)) == 0
            assert sum(normal[i] * magnetic[i] for i in range(3)) == 0
            assert [sum(c[i][k] * electric[k] for k in range(3))
                    for i in range(3)] == magnetic
    print('PASS G5: five rational directions of TARGET rank-two EM projector only')

    # A Hermitian but forbidden +/-2 insertion destroys support compatibility.
    wrong = [add(s[a], add(power(2 * a), power(-2 * a))) for a in range(5)]
    wrongh = dft(wrong)
    assert wh[2] == ZERO and wrongh[2] == scale(5, ONE)
    assert wh[2][0] - wrongh[2][0] < 0
    # Dropping the gauge average would admit this nonconserved local label.
    assert rsum([power(t) for t in range(5)]) == ZERO and wh[1][0] > 0
    # Reversing the electric sign fails the frozen sign convention, even
    # though some unsigned spectral and rank tests would still pass.
    assert scale(-1, sh[1]) != scale(-5, ONE)
    print('PASS G6: forbidden-charge, absent-gauge and wrong-sign controls detected')
    print('ALL 6 EXACT AUDIT GROUPS PASS; no many-link spectrum or phase computed')


if __name__ == '__main__':
    main()
