#!/usr/bin/env python3
"""Exact finite audit by polynomial arithmetic. NON-CANONICAL, candidate-C.

This script does not prove the infinite-graph bounds or the external E6
hypothesis. See PROOF.md. Standard-library rational arithmetic only.
"""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import product
import json

V = tuple[Q, Q, Q, Q]
ZERO: V = (Q(0), Q(0), Q(0), Q(0))
ONE: V = (Q(1), Q(0), Q(0), Q(0))
JROOT: V = (Q(0), Q(1), Q(0), Q(0))
PHI: V = (Q(0), Q(0), Q(-1), Q(-1))


def add(x: V, y: V) -> V:
    return tuple(a + b for a, b in zip(x, y))


def neg(x: V) -> V:
    return tuple(-a for a in x)


def sub(x: V, y: V) -> V:
    return add(x, neg(y))


def scalar(a: Q | int) -> V:
    return (Q(a), Q(0), Q(0), Q(0))


def mul(x: V, y: V) -> V:
    c = [Q(0)] * 7
    for i, a in enumerate(x):
        for k, b in enumerate(y):
            c[i + k] += a * b
    for k in range(6, 3, -1):
        for offset in range(1, 5):
            c[k - offset] -= c[k]
        c[k] = Q(0)
    return tuple(c[:4])


def inv(x: V) -> V:
    if x == ZERO:
        raise ZeroDivisionError('zero cyclotomic scalar')
    basis = [tuple(Q(i == k) for i in range(4)) for k in range(4)]
    columns = [mul(x, e) for e in basis]
    rows = [[columns[k][i] for k in range(4)] + [ONE[i]]
            for i in range(4)]
    for k in range(4):
        pivot = next(i for i in range(k, 4) if rows[i][k])
        rows[k], rows[pivot] = rows[pivot], rows[k]
        divisor = rows[k][k]
        rows[k] = [a / divisor for a in rows[k]]
        for i in range(4):
            if i != k:
                coefficient = rows[i][k]
                rows[i] = [a - coefficient * b
                           for a, b in zip(rows[i], rows[k])]
    return tuple(rows[i][4] for i in range(4))


def power(x: V, n: int) -> V:
    if n < 0:
        return power(inv(x), -n)
    answer = ONE
    while n:
        if n & 1:
            answer = mul(answer, x)
        x = mul(x, x)
        n //= 2
    return answer


def bar(x: V) -> V:
    result = ZERO
    for k, a in enumerate(x):
        result = add(result, mul(scalar(a), power(JROOT, (-k) % 5)))
    return result


def norm(x: V) -> V:
    return mul(x, bar(x))


def residue(x: V) -> int:
    assert all(a.denominator % 5 for a in x), 'not this local chart'
    return sum(a.numerator * pow(a.denominator, -1, 5) for a in x) % 5


def real_pair(x: V) -> tuple[Q, Q]:
    assert x[1] == 0 and x[2] == x[3], 'not real'
    return x[0], -x[2]


def sign(x: V) -> int:
    # 2(a+b*phi)=(2a+b)+b*sqrt(5); compare only rational squares.
    a, b = real_pair(x)
    u, v = 2 * a + b, b
    if not v:
        return (u > 0) - (u < 0)
    if not u:
        return (v > 0) - (v < 0)
    if u > 0 and v > 0:
        return 1
    if u < 0 and v < 0:
        return -1
    difference = u * u - 5 * v * v
    assert difference != 0
    return ((difference > 0) - (difference < 0)) * (1 if u > 0 else -1)


def encoded(x: V) -> list[list[int]]:
    return [[a.numerator, a.denominator] for a in x]


def main() -> None:
    j = JROOT
    J = add(ONE, power(j, 2))
    assert power(j, 5) == ONE and j != ONE
    phi5 = ZERO
    for k in range(5):
        phi5 = add(phi5, power(j, k))
    assert phi5 == ZERO
    assert mul(PHI, PHI) == add(PHI, ONE)
    assert inv(PHI) == sub(PHI, ONE)
    assert mul(J, neg(add(j, power(j, 2)))) == ONE
    assert power(sub(J, ONE), 3) == j
    assert mul(J, PHI) == j
    polynomial = ZERO
    for k, a in enumerate((1, -2, 4, -3, 1)):
        polynomial = add(polynomial, mul(scalar(a), power(J, k)))
    assert polynomial == ZERO

    points = [ZERO]
    for k in range(4):
        points.append(add(points[-1], power(j, k)))
    pairs = []
    for a in range(5):
        for b in range(a + 1, 5):
            distance = norm(sub(points[a], points[b]))
            expected = ONE if (b - a) in (1, 4) else power(PHI, 2)
            assert distance == expected
            pairs.append([a, b, encoded(distance)])
    residues = [residue(x) for x in points]
    assert residues == list(range(5))
    colors = (0, 1, 0, 1, 2)
    for r in range(5):
        for step in (1, -1):
            assert colors[r] != colors[(r + step) % 5]
        for step in (2, -2):
            assert colors[(3 * r) % 5] != colors[(3 * (r + step)) % 5]

    basis = [tuple(Q(i == k) for i in range(4)) for k in range(4)]
    columns = [mul(J, e) for e in basis]
    solutions = []
    trials = 0
    for row in product(range(5), repeat=4):
        if row == (0, 0, 0, 0):
            continue
        for t in range(5):
            trials += 1
            if all((sum(row[i] * columns[k][i] for i in range(4))
                    - t * row[k]) % 5 == 0 for k in range(4)):
                solutions.append({'row': list(row), 't': t})
    assert solutions == [{'row': [b] * 4, 't': 2} for b in range(1, 5)]
    assert trials == 3120

    cases = 0
    for n in range(-8, 9):
        for k in range(5):
            for s in (-1, 1):
                u = mul(scalar(s), mul(power(PHI, n), power(j, k)))
                assert norm(u) == power(PHI, 2 * n)
                r = residue(u)
                assert r != 0
                assert r * r % 5 == (1 if n % 2 == 0 else 4)
                cases += 1
    assert cases == 170

    u = mul(add(scalar(2), j), inv(add(scalar(2), power(j, 4))))
    assert norm(u) == ONE
    assert any(a.denominator != 1 for a in u)
    assert residue(u) == 1

    previous = ZERO
    for n in range(1, 33):
        tail = power(PHI, -4 * n)
        d = sub(ONE, tail)
        assert residue(d) == 0
        assert sign(d) > 0 and sign(sub(ONE, d)) > 0
        assert sign(sub(d, previous)) > 0
        assert norm(d) == mul(d, d)
        previous = d
    windows = []
    for r in range(1, 13):
        epsilon = Q(1, 10 ** r)
        n = 2 * r
        tail = power(PHI, -4 * n)
        d = sub(ONE, tail)
        assert sign(tail) > 0 and sign(sub(scalar(epsilon), tail)) > 0
        assert sign(sub(d, scalar(1 - epsilon))) > 0
        assert sign(sub(scalar(1 + epsilon), d)) > 0
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
