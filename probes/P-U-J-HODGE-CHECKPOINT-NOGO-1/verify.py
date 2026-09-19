#!/usr/bin/env python3
"""Exact finite certificates for the proof in PROOF.md; no native time sweep."""
from fractions import Fraction as Q
from itertools import combinations

PAIRS = tuple(combinations(range(4), 2))


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def zero(n):
    return [[Q(0) for _ in range(n)] for _ in range(n)]


def add(a, b):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scale(c, a):
    return [[c * x for x in r] for r in a]


def sub(a, b):
    return add(a, scale(Q(-1), b))


def mul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(r) for r in zip(*a)]


def power(a, n):
    result = eye(len(a))
    while n:
        if n & 1:
            result = mul(result, a)
        a = mul(a, a)
        n //= 2
    return result


def trace(a):
    return sum((a[i][i] for i in range(len(a))), Q(0))


def rank(a):
    a = [[Q(x) for x in row] for row in a]
    m, n, r = len(a), len(a[0]), 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        value = a[r][c]
        a[r] = [x / value for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                value = a[i][c]
                a[i] = [x - value * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def exterior_square(a):
    return [[a[i][k] * a[j][l] - a[i][l] * a[j][k]
             for k, l in PAIRS] for i, j in PAIRS]


def poly(a, coefficients):
    """Coefficients in increasing degree, evaluated by Horner's rule."""
    result = zero(len(a))
    for c in reversed(coefficients):
        result = add(mul(result, a), scale(Q(c), eye(len(a))))
    return result


def main():
    h = [[Q(1 + (i == j)) for j in range(4)] for i in range(4)]
    c = [[Q(x) for x in row] for row in
         ((-1, -1, -1, -1), (1, 0, 0, 0),
          (0, 1, 0, 0), (0, 0, 1, 0))]
    m = add(eye(4), power(c, 2))
    a, l, g = map(exterior_square, (c, m, h))
    b = zero(6)
    for i, ij in enumerate(PAIRS):
        for j, kl in enumerate(PAIRS):
            indices = ij + kl
            if len(set(indices)) == 4:
                inversions = sum(indices[u] > indices[v]
                                 for u in range(4) for v in range(u + 1, 4))
                b[i][j] = Q((-1) ** inversions)
    k = mul(b, g)
    t = scale(Q(1, 5), sum_matrices([power(a, j) for j in range(5)]))
    r = sub(eye(6), t)
    pl, ql = poly(l, (1, -3, 1)), poly(l, (1, -1, 1, -1, 1))
    commutator = sub(mul(k, l), mul(l, k))
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    check("G1_marked_A4", power(c, 5) == eye(4)
          and mul(mul(transpose(c), h), c) == h and rank(l) == 6)
    check("G2_integral_Hodge", all(x.denominator == 1 for row in k for x in row)
          and mul(k, k) == scale(Q(5), eye(6)))
    check("G3_primary_projectors", mul(t, t) == t and mul(r, r) == r
          and mul(t, r) == zero(6) and rank(t) == 2 and rank(r) == 4
          and mul(l, r) == mul(r, l) and mul(k, r) == mul(r, k))
    check("G4_exact_factors", mul(pl, t) == zero(6)
          and mul(ql, r) == zero(6) and mul(pl, ql) == zero(6))
    check("G5_periodic_target", mul(power(l, 5), r) == scale(Q(-1), r)
          and mul(power(l, 10), r) == r
          and rank(sub(power(l, 10), eye(6))) == 2
          and all(rank(mul(sub(power(l, d), eye(6)), r)) == 4
                  for d in (1, 2, 5)))
    check("G6_Hodge_intersection", trace(mul(k, r)) == 0
          and mul(r, commutator) == zero(6))

    periodic = [[r[i][0]] for i in range(6)]
    hyperbolic = [[5 * t[i][0]] for i in range(6)]
    orbit = [mul(power(l, j), periodic) for j in range(11)]
    check("G7_finite_rotor_control", rank(periodic) == 1
          and orbit[0] == orbit[10]
          and len({tuple(row[0] for row in v) for v in orbit[:10]}) == 10)
    check("G8_hyperbolic_control", rank(hyperbolic) == 1
          and mul(pl, hyperbolic) == [[Q(0)] for _ in range(6)]
          and mul(power(l, 10), hyperbolic) != hyperbolic)

    print("P-U-J-HODGE-CHECKPOINT-NOGO-1")
    for name, passed in checks:
        print(name + ": " + ("PASS" if passed else "FIRED_NEGATIVE"))
    if all(ok for _, ok in checks):
        print("primary dimensions: hyperbolic=2 periodic=4")
        print("nonzero periodic target order: 10")
        print("periodic part of E_J: dimension 2")
    print("finite-reader and fixed-code universal clauses: PROOF.md")
    print("VERDICT: " + ("PASS" if all(ok for _, ok in checks) else "FIRED_NEGATIVE"))


def sum_matrices(matrices):
    result = zero(len(matrices[0]))
    for matrix in matrices:
        result = add(result, matrix)
    return result


if __name__ == "__main__":
    main()
