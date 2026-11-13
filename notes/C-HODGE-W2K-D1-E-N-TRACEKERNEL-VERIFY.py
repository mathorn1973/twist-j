#!/usr/bin/env python3
"""NON-CANONICAL integer audit, not a computation of geometric Ext ranks.

The proof supplies the normal-form ranks. This script audits their exact
linear algebra, every relevant first-page term, and the outer polynomial.
Standard library only. No random sampling and no floating point.
"""
from fractions import Fraction
from itertools import product


def rank(matrix):
    a = [list(map(Fraction, row)) for row in matrix]
    if not a:
        return 0
    row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        scale = a[row][col]
        a[row] = [v / scale for v in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                scale = a[i][col]
                a[i] = [v - scale * w for v, w in zip(a[i], a[row])]
        row += 1
        if row == len(a):
            break
    return row


def curve_normal_form(u):
    assert u in (1, 2)
    a = [[0] * 6 for _ in range(u + 5)]
    # First two columns are Picard directions; the middle two move the
    # curve normally to Y1; the last two move it inside Y1.
    if u == 2:
        a[0][0] = 1
    a[u - 1][2] = 1
    a[u][3] = 1
    return a


def block_diagonal(a, b):
    return [row + [0] * len(b[0]) for row in a] + [
        [0] * len(a[0]) + row for row in b
    ]


def source_profiles(u_a, u_b, m, twisted):
    fa = (u_a, u_a + 5, 0, 0, 0)
    fb = (0, u_b + 5, u_b, 0, 0)
    curve = (1, 6, 10, 6, 1)
    cc = (0, m, 2 * m, m, 0)
    # Filtration order B[-1], F, A[-1]. Entry (i,j) is from i to j.
    return {
        (0, 0): curve, (1, 1): ((0, 5, 0, 5, 0) if twisted else (1, 12, 12, 12, 1)),
        (2, 2): curve,
        (1, 2): fa, (2, 1): fa[::-1],
        (1, 0): fb, (0, 1): fb[::-1],
        (0, 2): cc, (2, 0): cc,
    }


def term(h, i, j, n):
    shifts = (-1, 0, -1)
    k = n + shifts[j] - shifts[i]
    return h[i, j][k] if 0 <= k <= 4 else 0


def diagonal_total(h, n, predicate=lambda i, j: True):
    return sum(term(h, i, j, n) for i, j in h if predicate(i, j))


# Polynomial ring Z[r,x1,x2,y1,y2].
ZERO = (0,) * 5

def const(n):
    return {ZERO: n} if n else {}


def var(i):
    e = [0] * 5
    e[i] = 1
    return {tuple(e): 1}


def plus(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c}


def times(a, b):
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            e = tuple(x + y for x, y in zip(ea, eb))
            out[e] = out.get(e, 0) + ca * cb
    return {e: c for e, c in out.items() if c}


def scale(c, a):
    return {e: c * v for e, v in a.items() if c * v}


def coefficient_product(a, b, n):
    return sum(a[i] * b[n-i] for i in range(len(a)) if 0 <= n-i < len(b))


def main():
    assert rank([[-1, 1, 0], [0, -1, 1]]) == 2
    assert rank([[1, 0], [0, 1]]) == 2
    for u_a, u_b in product((1, 2), repeat=2):
        tau = u_a + u_b
        ell = rank(block_diagonal(curve_normal_form(u_a), curve_normal_form(u_b)))
        assert ell == tau + 2
        h = source_profiles(u_a, u_b, 2, False)
        ht = source_profiles(u_a, u_b, 2, True)
        assert diagonal_total(h, 0) == 3
        assert diagonal_total(ht, 0) == 2
        assert diagonal_total(h, 1) == 28 + tau
        assert diagonal_total(ht, 1) == 21 + tau
        assert diagonal_total(ht, 1, lambda i, j: j >= i) == 19 + tau
        assert diagonal_total(ht, 2, lambda i, j: j-i == 1) == tau + 10
        assert term(ht, 0, 2, 2) == 4
        for n in range(-5, 1):
            assert diagonal_total(ht, n, lambda i, j: j < i) == 0
        for n in range(-5, 0):
            assert diagonal_total(h, n) == diagonal_total(ht, n) == 0
        self_upper = diagonal_total(h, 1) - 2 - ell
        cross_upper = diagonal_total(ht, 1) - 2 - ell
        cross_lower = diagonal_total(ht, 1, lambda i, j: j >= i) - 2 - (ell + 5) - 4
        assert (self_upper, cross_lower, cross_upper) == (24, 6, 17)
        print(f'uA={u_a} uB={u_b}: ell={ell}; r<=24; 6<=dk<=17')

    r, x1, x2, y1, y2 = [var(i) for i in range(5)]
    a1, a2, b1, b2 = [plus(const(6), p) for p in (x1, x2, y1, y2)]
    c1 = plus(const(10), a1, b1)
    c2 = plus(const(10), a2, b2)
    n = plus(times(c1, c2), times(a1, b2), times(b1, a2))
    capacity = plus(c1, c2, times(r, plus(a1, a2)), scale(6, r))
    kernel = plus(n, scale(-1, capacity))
    expected = plus(
        const(512), scale(-18, r),
        times(plus(const(27), scale(-1, r)), plus(x1, x2)),
        scale(27, plus(y1, y2)),
        times(x1, x2), scale(2, times(x1, y2)),
        scale(2, times(y1, x2)), times(y1, y2),
    )
    assert kernel == expected
    print('exact polynomial identity: PASS')
    print('K=512-18r+(27-r)(x1+x2)+27(y1+y2)+x1*x2+2*x1*y2+2*y1*x2+y1*y2')
    print('r<=24, xi,yi>=0: all residual coefficients nonnegative; K>=80')

    minimum = None
    minimum21 = None
    count = 0
    for r0 in range(8, 25):
        selfp = (1, r0, 8+2*r0, r0, 1)
        for a, b, c, d in product(range(6, 18), repeat=4):
            m1 = (0, a, 10+a+b, b, 0)
            m2 = (0, c, 10+c+d, d, 0)
            corner = coefficient_product(m1, m2, 4)
            adjacent = coefficient_product(m1, selfp, 2) + coefficient_product(selfp, m2, 2)
            k0 = corner - adjacent - 6*r0
            assert corner == m1[2]*m2[2] + a*d + b*c
            assert adjacent == m1[2] + m2[2] + r0*(a+c)
            assert k0 >= 512-18*r0 >= 80
            point = (k0, r0, a, b, c, d)
            minimum = point if minimum is None or point < minimum else minimum
            if r0 == 21:
                minimum21 = point if minimum21 is None or point < minimum21 else minimum21
            count += 1
    assert minimum == (80, 24, 6, 6, 6, 6)
    assert minimum21 == (134, 21, 6, 6, 6, 6)
    print(f'ordered dimension controls: {count}')
    print(f'relaxed minimum (K,r,a1,b1,a2,b2): {minimum}')
    print(f'r=21 relaxed minimum: {minimum21}')
    print('These minima are bounds, not realized geometric dimensions.')
    print('RESULT: arithmetic PASS; conditional geometric family fails full semiregularity')
    print('Exact r, dk, full Ext2, full trace-kernel dimension and basis: NOT COMPUTED')

if __name__ == '__main__':
    main()
