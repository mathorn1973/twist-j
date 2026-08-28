#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import gcd

PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))

OMEGA1 = (1, 0, 0, 1, 0, 1)
OMEGA2 = (0, 1, -1, 0, 1, 0)

MJ = (
    (1, 0, -1, 1),
    (0, 1, -1, 0),
    (1, 0, 0, 0),
    (0, 1, -1, 1),
)

MZ = (
    (0, 0, 0, -1),
    (1, 0, 0, -1),
    (0, 1, 0, -1),
    (0, 0, 1, -1),
)


def ident(n: int) -> list[list[int]]:
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def transpose(a):
    return [list(row) for row in zip(*a)]


def matsub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matpow(a, n: int):
    out = ident(len(a))
    base = [list(row) for row in a]
    while n:
        if n & 1:
            out = matmul(out, base)
        base = matmul(base, base)
        n >>= 1
    return out


def det(a):
    m = [[Fraction(x) for x in row] for row in a]
    n = len(m)
    sign = 1
    out = Fraction(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if m[r][col] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
            sign *= -1
        p = m[col][col]
        out *= p
        for r in range(col + 1, n):
            if m[r][col] == 0:
                continue
            f = m[r][col] / p
            for c in range(col, n):
                m[r][c] -= f * m[col][c]
    return sign * out


def rref(a):
    m = [[Fraction(x) for x in row] for row in a]
    rows = len(m)
    cols = len(m[0]) if rows else 0
    pivots = []
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if m[i][c] != 0), None)
        if p is None:
            continue
        m[r], m[p] = m[p], m[r]
        z = m[r][c]
        m[r] = [x / z for x in m[r]]
        for i in range(rows):
            if i == r or m[i][c] == 0:
                continue
            z = m[i][c]
            m[i] = [m[i][j] - z * m[r][j] for j in range(cols)]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return m, pivots


def nullspace(a):
    rr, pivots = rref(a)
    cols = len(a[0])
    free = [c for c in range(cols) if c not in pivots]
    out = []
    for f in free:
        v = [Fraction(0) for _ in range(cols)]
        v[f] = 1
        for row, p in enumerate(pivots):
            v[p] = -rr[row][f]
        out.append(tuple(v))
    return out


def rank_rows(rows) -> int:
    if not rows:
        return 0
    return len(rref(rows)[1])


def coeffs_to_matrix(w):
    out = [[0] * 4 for _ in range(4)]
    for x, (i, j) in zip(w, PAIRS):
        out[i][j] = x
        out[j][i] = -x
    return out


def matrix_to_coeffs(w):
    return tuple(w[i][j] for i, j in PAIRS)


def pullback(a, w):
    return matmul(transpose(a), matmul(w, a))


def wedge2(a):
    cols = []
    for i, j in PAIRS:
        u = [a[r][i] for r in range(4)]
        v = [a[r][j] for r in range(4)]
        cols.append(tuple(u[p] * v[q] - u[q] * v[p] for p, q in PAIRS))
    return [list(row) for row in zip(*cols)]


def gcd_all(xs) -> int:
    d = 0
    for x in xs:
        d = gcd(d, abs(x))
    return d


def egcd_pos(a: int, b: int):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t


def bezout_vector(xs):
    coeff = [0] * len(xs)
    d = 0
    for i, x in enumerate(xs):
        ax = abs(x)
        if d == 0 and ax == 0:
            continue
        g, s, t = egcd_pos(d, ax)
        coeff = [s * c for c in coeff]
        coeff[i] += t * (1 if x >= 0 else -1)
        d = g
    return d, tuple(coeff)


def cm_coeffs(a: int, b: int):
    return (a, b, -b, a, b, a)


def q(a: int, b: int) -> int:
    return a * a - a * b - b * b


def biv_pf(c) -> int:
    return c[0] * c[5] - c[1] * c[4] + c[2] * c[3]


def transvection(w, k: int):
    v = [1 if i == k else 0 for i in range(4)]
    wv = [sum(w[i][j] * v[j] for j in range(4)) for i in range(4)]
    t = ident(4)
    for i in range(4):
        for j in range(4):
            t[i][j] += v[i] * wv[j]
    return t


def gate_1_period_gcd() -> None:
    count = 0
    for w in product(range(-2, 3), repeat=6):
        d = gcd_all(w)
        g, c = bezout_vector(w)
        assert g == d
        assert sum(x * y for x, y in zip(w, c)) == d
        if d:
            assert all(x % d == 0 for x in w)
        else:
            assert w == (0, 0, 0, 0, 0, 0)
        count += 1
    assert count == 15625
    print("G1 PASS  period subgroup is coefficient-gcd times Z; 15625 exact tuples audited")


def gate_2_cm_primitive_period() -> None:
    found = 0
    for a in range(-250, 251):
        for b in range(-250, 251):
            assert gcd_all(cm_coeffs(a, b)) == gcd(abs(a), abs(b))
            if q(a, b) in (-1, 1):
                found += 1
                assert gcd(abs(a), abs(b)) == 1
    assert found > 0
    print("G2 PASS  CM period subgroup is gcd(a,b)Z; every audited unimodular rung has generator 1")


def gate_3_pullback_invariance() -> None:
    w1 = coeffs_to_matrix(OMEGA1)
    ts = [transvection(w1, k) for k in range(4)]
    shear = ident(4)
    shear[0][1] = 1
    swap = ident(4)
    swap[0], swap[1] = swap[1], swap[0]
    family = [MJ, MZ, shear, swap] + ts
    assert all(abs(det(a)) == 1 for a in family)

    samples = []
    for n in range(15625):
        x = n
        w = []
        for _ in range(6):
            w.append((x % 5) - 2)
            x //= 5
        samples.append(tuple(w))

    for a in family:
        for w in samples:
            wp = matrix_to_coeffs(pullback(a, coeffs_to_matrix(w)))
            assert gcd_all(wp) == gcd_all(w)

    for a in range(-100, 101):
        for b in range(-100, 101):
            ap, bp = a - b, -a + 2 * b
            direct = matrix_to_coeffs(pullback(MJ, coeffs_to_matrix(cm_coeffs(a, b))))
            assert direct == cm_coeffs(ap, bp)
            assert gcd(abs(ap), abs(bp)) == gcd(abs(a), abs(b))
    print("G3 PASS  GL4(Z) pullback period invariance audited; J preserves the CM primitive period")


def gate_4_transvection_nonselection() -> None:
    w = coeffs_to_matrix(OMEGA1)
    ts = [transvection(w, k) for k in range(4)]
    for t in ts:
        assert det(t) == 1
        assert pullback(t, w) == w

    equations = []
    for t in ts:
        m = matsub(wedge2(t), ident(6))
        equations.extend(m)
    ns = nullspace(equations)
    assert len(ns) == 1
    pi = (Fraction(1), Fraction(0), Fraction(1), Fraction(0), Fraction(0), Fraction(1))
    assert ns[0] == pi
    assert gcd_all(tuple(int(x) for x in pi)) == 1
    assert sum(x * y for x, y in zip(OMEGA1, pi)) == 2
    print("G4 PASS  four Omega1-transvections fix exactly Z(1,0,1,0,0,1), whose period is 2")


def gate_5_root_kernel_no_decomposable_cell() -> None:
    assert det(MZ) == 1
    assert matpow(MZ, 5) == ident(4)
    assert pullback(MZ, coeffs_to_matrix(OMEGA1)) == coeffs_to_matrix(OMEGA1)
    assert pullback(MZ, coeffs_to_matrix(OMEGA2)) == coeffs_to_matrix(OMEGA2)

    m2 = wedge2(MZ)
    fixed = matsub(m2, ident(6))
    ns = nullspace(fixed)
    assert len(ns) == 2
    v1 = (0, 1, 0, 1, 1, 0)
    v2 = (1, 0, 1, 0, 0, 1)
    assert all(sum(fixed[i][j] * v1[j] for j in range(6)) == 0 for i in range(6))
    assert all(sum(fixed[i][j] * v2[j] for j in range(6)) == 0 for i in range(6))
    assert rank_rows([v1, v2] + [list(v) for v in ns]) == 2

    for a in range(-100, 101):
        for b in range(-100, 101):
            c = (b, a, b, a, a, b)
            assert biv_pf(c) == -q(a, b)
            if biv_pf(c) == 0:
                assert (a, b) == (0, 0)

    # Written all-rational proof reduces a hypothetical nonzero rational
    # solution to a coprime integer solution. Then a|b^2 and b|a^2 force
    # |a|=|b|=1, and the four sign pairs are not zeros of q.
    assert all(q(a, b) != 0 for a in (-1, 1) for b in (-1, 1))
    print("G5 PASS  zeta5-fixed bivectors form rank 2 and contain no nonzero decomposable rational cell")


def gate_6_pell_and_j_controls() -> None:
    for a in range(-200, 201):
        for b in range(-200, 201):
            d = gcd(abs(a), abs(b))
            sa, sb = a + b, a
            ja, jb = a - b, -a + 2 * b
            assert gcd(abs(sa), abs(sb)) == d
            assert gcd(abs(ja), abs(jb)) == d
            assert q(sa, sb) == -q(a, b)
            assert q(ja, jb) == q(a, b)
    print("G6 PASS  Pell shift and J-pullback preserve the period subgroup; only Pell flips Pfaffian sign")


def main() -> int:
    gate_1_period_gcd()
    gate_2_cm_primitive_period()
    gate_3_pullback_invariance()
    gate_4_transvection_nonselection()
    gate_5_root_kernel_no_decomposable_cell()
    gate_6_pell_and_j_controls()
    print("ALL PASS CM-PERIOD-LATTICE-NONSELECTION exact L1 audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
