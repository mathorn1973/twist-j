#!/usr/bin/env python3
"""Same-session cross-check via Q(phi)[j], not blind independent review.

NON-CANONICAL candidate-C. Does not import verify.py or run an E6 proof.
Here j^2=(phi-1)j-1. Real order uses certified rational root isolation.
"""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import product
import json

R = tuple[Q, Q]
C = tuple[R, R]
R0: R = (Q(0), Q(0))
R1: R = (Q(1), Q(0))
PHI_R: R = (Q(0), Q(1))
TRACE_J: R = (Q(-1), Q(1))
ZERO: C = (R0, R0)
ONE: C = (R1, R0)
ROOT: C = (R0, R1)
PHI: C = (PHI_R, R0)


def radd(x: R, y: R) -> R:
    return x[0] + y[0], x[1] + y[1]


def rneg(x: R) -> R:
    return -x[0], -x[1]


def rsub(x: R, y: R) -> R:
    return radd(x, rneg(y))


def rmul(x: R, y: R) -> R:
    a, b = x
    c, d = y
    return a * c + b * d, a * d + b * c + b * d


def rinv(x: R) -> R:
    a, b = x
    denominator = a * a + a * b - b * b
    if not denominator:
        raise ZeroDivisionError('zero real scalar')
    return (a + b) / denominator, -b / denominator


def add(x: C, y: C) -> C:
    return radd(x[0], y[0]), radd(x[1], y[1])


def neg(x: C) -> C:
    return rneg(x[0]), rneg(x[1])


def sub(x: C, y: C) -> C:
    return add(x, neg(y))


def scalar(x: Q | int) -> C:
    return (Q(x), Q(0)), R0


def mul(x: C, y: C) -> C:
    a, b = x
    c, d = y
    bd = rmul(b, d)
    return (rsub(rmul(a, c), bd),
            radd(radd(rmul(a, d), rmul(b, c)), rmul(TRACE_J, bd)))


def bar(x: C) -> C:
    return radd(x[0], rmul(TRACE_J, x[1])), rneg(x[1])


def norm(x: C) -> C:
    return mul(x, bar(x))


def inverse(x: C) -> C:
    conjugate = bar(x)
    n = mul(x, conjugate)
    assert n[1] == R0
    reciprocal = rinv(n[0])
    return rmul(conjugate[0], reciprocal), rmul(conjugate[1], reciprocal)


def power(x: C, n: int) -> C:
    if n < 0:
        x, n = inverse(x), -n
    result = ONE
    for _ in range(n):
        result = mul(result, x)
    return result


def coefficients(x: C) -> tuple[Q, Q, Q, Q]:
    # phi=-j^2-j^3 and phi*j=1+j+j^2.
    (a, b), (c, d) = x
    return a + d, c + d, d - b, -b


def residue(x: C) -> int:
    (a, b), (c, d) = x
    value = a + 3 * b + c + 3 * d
    assert value.denominator % 5
    return value.numerator * pow(value.denominator, -1, 5) % 5


def sign(x: C) -> int:
    assert x[1] == R0
    a, b = x[0]
    if not b:
        return (a > 0) - (a < 0)
    lower, upper = Q(1), Q(2)
    for _ in range(1024):
        lo, hi = sorted((a + b * lower, a + b * upper))
        if lo > 0:
            return 1
        if hi < 0:
            return -1
        mid = (lower + upper) / 2
        if mid * mid - mid - 1 < 0:
            lower = mid
        else:
            upper = mid
    raise AssertionError('rational root isolation budget exhausted')


def encoded(x: C) -> list[list[int]]:
    return [[a.numerator, a.denominator] for a in coefficients(x)]


def main() -> None:
    j = ROOT
    J = add(ONE, mul(j, j))
    assert power(j, 5) == ONE and j != ONE
    phi5 = ZERO
    for k in range(5):
        phi5 = add(phi5, power(j, k))
    assert phi5 == ZERO
    assert mul(PHI, PHI) == add(ONE, PHI)
    assert inverse(PHI) == sub(PHI, ONE)
    assert inverse(J) == neg(add(j, power(j, 2)))
    assert power(sub(J, ONE), 3) == j
    assert mul(J, PHI) == j
    polynomial = power(J, 4)
    polynomial = sub(polynomial, mul(scalar(3), power(J, 3)))
    polynomial = add(polynomial, mul(scalar(4), power(J, 2)))
    polynomial = sub(polynomial, mul(scalar(2), J))
    assert add(polynomial, ONE) == ZERO

    points = []
    for k in range(5):
        value = ZERO
        for a in range(k):
            value = add(value, power(j, a))
        points.append(value)
    pairs = []
    for a in range(5):
        for b in range(a + 1, 5):
            distance = norm(sub(points[a], points[b]))
            assert distance == (ONE if b - a in (1, 4) else add(ONE, PHI))
            pairs.append([a, b, encoded(distance)])
    residues = [residue(x) for x in points]
    assert residues == [0, 1, 2, 3, 4]
    palette = [0, 1, 0, 1, 2]
    for a in range(5):
        for b in range(5):
            delta = (b - a) % 5
            if delta in (1, 4):
                assert palette[a] != palette[b]
            if delta in (2, 3):
                assert palette[3 * a % 5] != palette[3 * b % 5]

    basis = [power(j, k) for k in range(4)]
    solutions = []
    trials = 0
    for row in product(range(5), repeat=4):
        if not any(row):
            continue
        images = [sum(row[i] * value for i, value in
                      enumerate(coefficients(mul(J, e)))) % 5 for e in basis]
        for t in range(5):
            trials += 1
            if images == [t * a % 5 for a in row]:
                solutions.append({'row': list(row), 't': t})
    assert solutions == [{'row': [a, a, a, a], 't': 2} for a in (1, 2, 3, 4)]
    assert trials == 3120

    cases = 0
    for n in range(-8, 9):
        for k in range(5):
            positive = mul(power(PHI, n), power(j, k))
            for value in (neg(positive), positive):
                assert norm(value) == power(PHI, 2 * n)
                r = residue(value)
                assert r in ((1, 4) if n % 2 == 0 else (2, 3))
                cases += 1
    assert cases == 170

    u = mul(add(scalar(2), j), inverse(add(scalar(2), bar(j))))
    assert norm(u) == ONE
    assert any(a.denominator > 1 for a in coefficients(u))
    assert residue(u) == 1

    previous = ZERO
    for n in range(1, 33):
        d = sub(ONE, power(PHI, -4 * n))
        assert residue(d) == 0
        assert sign(d) == 1 and sign(sub(d, ONE)) == -1
        assert sign(sub(d, previous)) == 1
        assert norm(d) == mul(d, d)
        previous = d
    windows = []
    for r in range(1, 13):
        n = 2 * r
        epsilon = Q(1, 10 ** r)
        tail = power(PHI, -4 * n)
        assert sign(tail) == 1
        assert sign(sub(tail, scalar(epsilon))) == -1
        d = sub(ONE, tail)
        assert sign(sub(d, scalar(1 - epsilon))) == 1
        assert sign(sub(d, scalar(1 + epsilon))) == -1
        assert residue(d) == 0
        windows.append([r, n])

    certificate = {
        'candidate': 'C-J-EUCLIDEAN-COLOR-BOUNDARY-N',
        'status': 'NON-CANONICAL candidate-C finite audit',
        'anchor_checks': 'PASS',
        'pentagon_residues': residues,
        'pentagon_squared_distances': pairs,
        'covariance_trials': trials,
        'covariant_readers': solutions,
        'unit_cases': cases,
        'rational_norm_one': {'coordinates': encoded(u), 'residue': residue(u)},
        'annular_cases': 32,
        'annular_windows_r_n': windows,
        'external_E6': 'NOT TESTED',
        'infinite_graph_proofs': 'NOT REPLACED BY THIS AUDIT',
    }
    print(json.dumps(certificate, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
