#!/usr/bin/env python3
# P-FINITE-PRIME-SUPPORT-DILATIONS-1 verify.py
# Exact finite audit for the proof-first finite-prime-support dilation theorem.
#
# Universal statement carried by PREREG.md:
#   for finite prime support P, prime q outside P, and S subset S_P with 1 in S,
#   r_q = g_q-(1/q)g_1 is orthogonal to closure span{g_s:s in S}, and
#   dist^2 = (1/12)(1-1/q^2), uniquely projected to (1/q)g_1.
#
# Python standard library only. Fraction arithmetic. No float anywhere.

from __future__ import annotations

import sys
from fractions import Fraction
from itertools import product
from math import gcd

assert len(sys.argv) == 1

checks = 0


def gate(name: str, condition: bool) -> None:
    global checks
    assert condition, name
    checks += 1
    print(f"{name} PASS")


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def gram_formula(m: int, n: int) -> Fraction:
    assert m >= 1 and n >= 1
    return Fraction(gcd(m, n) ** 2, 12 * m * n)


def gram_integral(m: int, n: int) -> Fraction:
    """Exact integral of (frac(mx)-1/2)(frac(nx)-1/2) on [0,1]."""
    points = sorted(
        set(
            [Fraction(i, m) for i in range(m + 1)]
            + [Fraction(j, n) for j in range(n + 1)]
        )
    )
    total = Fraction(0)
    for left, right in zip(points, points[1:]):
        if left == right:
            continue
        mid = (left + right) / 2
        a = floor_fraction(m * mid)
        b = floor_fraction(n * mid)
        # (m x-a-1/2)(n x-b-1/2) = A x^2 + B x + C.
        A = Fraction(m * n)
        B = -(
            Fraction(m) * (b + Fraction(1, 2))
            + Fraction(n) * (a + Fraction(1, 2))
        )
        C = (a + Fraction(1, 2)) * (b + Fraction(1, 2))
        total += (
            A * (right**3 - left**3) / 3
            + B * (right**2 - left**2) / 2
            + C * (right - left)
        )
    return total


def residual_inner(q: int, s: int) -> Fraction:
    return gram_formula(q, s) - Fraction(1, q) * gram_formula(1, s)


def residual_norm(q: int) -> Fraction:
    return (
        gram_formula(q, q)
        - Fraction(2, q) * gram_formula(q, 1)
        + Fraction(1, q * q) * gram_formula(1, 1)
    )


def target_norm(q: int) -> Fraction:
    return Fraction(1, 12) * (1 - Fraction(1, q * q))


def prime_support(n: int) -> frozenset[int]:
    assert n >= 1
    support: set[int] = set()
    d = 2
    value = n
    while d * d <= value:
        while value % d == 0:
            support.add(d)
            value //= d
        d += 1
    if value > 1:
        support.add(value)
    return frozenset(support)


def smooth_numbers(primes: tuple[int, ...], max_exponent: int) -> tuple[int, ...]:
    values = {
        product_value
        for exponents in product(range(max_exponent + 1), repeat=len(primes))
        for product_value in [
            __import__("functools").reduce(
                lambda acc, pair: acc * pair[0] ** pair[1],
                zip(primes, exponents),
                1,
            )
        ]
    }
    return tuple(sorted(values))


def generated_semigroup_box(
    generators: tuple[int, ...], max_exponent: int
) -> tuple[int, ...]:
    values = {
        product_value
        for exponents in product(range(max_exponent + 1), repeat=len(generators))
        for product_value in [
            __import__("functools").reduce(
                lambda acc, pair: acc * pair[0] ** pair[1],
                zip(generators, exponents),
                1,
            )
        ]
    }
    return tuple(sorted(values))


def solve_exact(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    size = len(matrix)
    assert size == len(vector)
    augmented = [row[:] + [vector[i]] for i, row in enumerate(matrix)]
    for col in range(size):
        pivot = next(row for row in range(col, size) if augmented[row][col] != 0)
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        pivot_value = augmented[col][col]
        augmented[col] = [entry / pivot_value for entry in augmented[col]]
        for row in range(size):
            if row == col or augmented[row][col] == 0:
                continue
            factor = augmented[row][col]
            augmented[row] = [
                entry - factor * pivot_entry
                for entry, pivot_entry in zip(augmented[row], augmented[col])
            ]
    return [augmented[row][size] for row in range(size)]


print("P-FINITE-PRIME-SUPPORT-DILATIONS-1 verify")

# FP1: independent exact integration of the public Gram formula.
fp1_pairs = [(m, n) for m in range(1, 11) for n in range(m, 11)]
fp1_pairs += [(2, 25), (3, 32), (5, 49), (7, 81), (11, 125), (13, 210)]
fp1_bad = [
    (m, n)
    for m, n in fp1_pairs
    if gram_integral(m, n) != gram_formula(m, n)
]
gate(
    f"FP1 exact piecewise integration equals gcd(m,n)^2/(12mn) on {len(fp1_pairs)} pairs",
    not fp1_bad,
)

# FP2: broad exact residual grid. The prime q is tested only against s coprime to q.
fp2_primes = (2, 3, 5, 7, 11, 13, 17, 19)
fp2_pairs = [
    (q, s)
    for q in fp2_primes
    for s in range(1, 121)
    if gcd(q, s) == 1
]
fp2_ok = all(residual_inner(q, s) == 0 for q, s in fp2_pairs)
fp2_ok = fp2_ok and all(
    residual_norm(q) == target_norm(q) > 0 for q in fp2_primes
)
gate(
    f"FP2 residual orthogonality on {len(fp2_pairs)} coprime pairs and exact positive norm for 8 primes",
    fp2_ok,
)

# FP3: finite-prime-support smooth families, including the empty and multi-prime cases.
fp3_cases = (
    ((), 2, 0),
    ((5,), 2, 6),
    ((2, 5), 3, 4),
    ((2, 3, 5), 7, 3),
    ((2, 3, 5, 7), 11, 2),
)
fp3_ok = True
fp3_total = 0
for primes, q, max_exponent in fp3_cases:
    family = smooth_numbers(primes, max_exponent)
    fp3_total += len(family)
    support_ok = all(prime_support(s) <= set(primes) for s in family)
    outside_ok = q not in primes and all(gcd(q, s) == 1 for s in family)
    orthogonal_ok = all(residual_inner(q, s) == 0 for s in family)
    fp3_ok = fp3_ok and support_ok and outside_ok and orthogonal_ok
    print(
        "  P = {%s}, q = %d: |S_box| = %d, dist^2 = %s"
        % (",".join(str(p) for p in primes), q, len(family), target_norm(q))
    )
gate(
    f"FP3 finite-prime-support controls cover {fp3_total} exact smooth indices",
    fp3_ok,
)

# FP4: exact normal-equation solutions on selected finite spans.
fp4_cases = (
    ((1, 5, 25, 125), 2),
    ((1, 2, 4, 5, 8, 10, 20), 3),
    ((1, 6, 10, 15, 30, 60), 7),
    ((1, 14, 21, 35, 70), 11),
)
fp4_ok = True
for family, q in fp4_cases:
    matrix = [[gram_formula(m, n) for n in family] for m in family]
    cross = [gram_formula(s, q) for s in family]
    coefficients = solve_exact(matrix, cross)
    expected = [Fraction(1, q)] + [Fraction(0)] * (len(family) - 1)
    distance = gram_formula(q, q) - sum(
        coefficient * inner for coefficient, inner in zip(coefficients, cross)
    )
    fp4_ok = fp4_ok and coefficients == expected and distance == target_norm(q)
gate(
    "FP4 exact finite projections give (1/q)g_1 and the frozen deficiency in 4 multi-prime spans",
    fp4_ok,
)

# FP5: finitely generated semigroup boxes have no prime outside generator support.
fp5_cases = (
    ((5,), 2, 7),
    ((6, 10), 7, 4),
    ((4, 9, 25), 7, 3),
    ((6, 35), 11, 4),
    ((10, 21, 44), 13, 3),
)
fp5_ok = True
fp5_total = 0
for generators, q, max_exponent in fp5_cases:
    family = generated_semigroup_box(generators, max_exponent)
    support = set().union(*(prime_support(g) for g in generators))
    fp5_total += len(family)
    semigroup_support_ok = all(prime_support(s) <= support for s in family)
    outside_ok = q not in support and all(gcd(q, s) == 1 for s in family)
    residual_ok = all(residual_inner(q, s) == 0 for s in family)
    fp5_ok = fp5_ok and semigroup_support_ok and outside_ok and residual_ok
    print(
        "  generators = %s, support = {%s}, q = %d, box = %d"
        % (generators, ",".join(str(p) for p in sorted(support)), q, len(family))
    )
gate(
    f"FP5 finitely generated semigroup controls cover {fp5_total} exact indices with no support leakage",
    fp5_ok,
)

# FP6: scope-negative controls. Once q is in the support, orthogonality must fail somewhere.
fp6_controls = (
    ((2,), 2),
    ((3, 5), 3),
    ((2, 5, 7), 5),
    ((2, 3, 5, 7), 7),
)
fp6_ok = True
for primes, q in fp6_controls:
    family = smooth_numbers(primes, 2)
    failures = [s for s in family if residual_inner(q, s) != 0]
    fp6_ok = fp6_ok and q in primes and bool(failures)
gate(
    "FP6 negative controls detect non-orthognality whenever q is admitted into the support",
    fp6_ok,
)

# FP7: predecessor five-tower slice, exactly recovered.
fp7_qs = (2, 3, 7, 11, 13)
fp7_ok = all(
    residual_inner(q, 5**a) == 0
    and residual_norm(q) == target_norm(q)
    for q in fp7_qs
    for a in range(0, 9)
)
fp7_ok = fp7_ok and target_norm(2) == Fraction(1, 16)
fp7_ok = fp7_ok and target_norm(3) == Fraction(2, 27)
gate(
    "FP7 predecessor P={5} slice recovered, including witnesses 1/16 and 2/27",
    fp7_ok,
)

print(
    "DECISION: every finite-prime-support dilation family misses each outside prime direction by an exact positive rational"
)
print(f"RESULT {checks}/{checks} ALL PASS")
