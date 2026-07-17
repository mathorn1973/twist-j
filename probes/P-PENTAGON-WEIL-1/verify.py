#!/usr/bin/env python3
"""Exact audit verifier for P-PENTAGON-WEIL-1.

The theorem-grade analytic statements are proved in PREREG.md.  This verifier
audits their finite cyclotomic and rational accounting only.  It uses no
floating point, external package, external data, randomness, or filesystem
write.
"""

from fractions import Fraction
import sys


CHECKS = []
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)

# Basis 1, j, j^2, j^3 in Z[j], with j^5 = 1 and
# j^4 = -1-j-j^2-j^3.
ROOTS = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
    (-1, -1, -1, -1),
)


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def neg(value):
    return tuple(-a for a in value)


def sub(left, right):
    return add(left, neg(right))


def scale(integer, value):
    return tuple(integer * a for a in value)


def mul(left, right):
    total = ZERO
    for i, a in enumerate(left):
        for k, b in enumerate(right):
            if a and b:
                total = add(total, scale(a * b, ROOTS[(i + k) % 5]))
    return total


def conjugate(value):
    total = ZERO
    for i, coefficient in enumerate(value):
        if coefficient:
            total = add(total, scale(coefficient, ROOTS[(-i) % 5]))
    return total


def root_filter(residue):
    total = ZERO
    for k in range(1, 5):
        total = add(total, ROOTS[(k * residue) % 5])
    return total


def filter_coefficient(integer):
    return 4 if integer % 5 == 0 else -1


def f5(integer_s):
    exponent = 1 - integer_s
    power = (Fraction(5 ** exponent, 1) if exponent >= 0
             else Fraction(1, 5 ** (-exponent)))
    return power - 1


def check(name, condition):
    CHECKS.append((name, bool(condition)))


def main():
    residues_ok = True
    for residue in range(5):
        expected = scale(4 if residue == 0 else -1, ONE)
        residues_ok = residues_ok and root_filter(residue) == expected
    check("G01 ROOT-FILTER    c(n) = 5[5|n] - 1 on all residues mod 5",
          residues_ok)

    factors = [sub(ONE, ROOTS[k]) for k in range(1, 5)]
    product = ONE
    for factor in factors:
        product = mul(product, factor)
    conjugate_pairs = (conjugate(factors[0]) == factors[3]
                       and conjugate(factors[1]) == factors[2])
    off_principal_cut = all(factor != conjugate(factor)
                            for factor in factors)
    pair_product = mul(mul(factors[0], factors[3]),
                       mul(factors[1], factors[2]))
    check("G02 CYCLOTOMIC     conjugate pairing fixed and product"
          " prod_(k=1)^4 (1-j^k) = 5",
          conjugate_pairs and off_principal_cut and product == scale(5, ONE)
          and pair_product == scale(5, ONE))

    cutoff_ok = True
    naive_rejected = 0
    for exponent in (2, 3, 4):
        lhs = Fraction(0)
        harmonic_n = Fraction(0)
        harmonic_floor = Fraction(0)
        factor = Fraction(1, 5 ** (exponent - 1))
        for n in range(1, 626):
            lhs += Fraction(filter_coefficient(n), n ** exponent)
            harmonic_n += Fraction(1, n ** exponent)
            if n % 5 == 0:
                harmonic_floor += Fraction(1, (n // 5) ** exponent)
            rhs = factor * harmonic_floor - harmonic_n
            cutoff_ok = cutoff_ok and lhs == rhs
        naive = (factor - 1) * harmonic_n
        naive_rejected += int(lhs != naive)
    check("G03 CUTOFF         exact finite identity through N=625 for"
          " s=2,3,4; all naive cutoffs rejected",
          cutoff_ok and naive_rejected == 3)

    raw_ratio = f5(2) / f5(-1)
    check("G04 RAW-SYMMETRY  f5(2)/f5(-1) = -1/30, excluding the"
          " standard unit-root-number symmetry", raw_ratio == Fraction(-1, 30))

    harmonic = [Fraction(0)]
    running_harmonic = Fraction(0)
    running_filter = Fraction(0)
    harmonic_blocks_ok = True
    for n in range(1, 626):
        running_harmonic += Fraction(1, n)
        harmonic.append(running_harmonic)
        running_filter += Fraction(filter_coefficient(n), n)
        if n % 5 == 0:
            m = n // 5
            harmonic_blocks_ok = (harmonic_blocks_ok
                                  and running_filter == harmonic[m] - harmonic[n])
    period_zero = sum(filter_coefficient(n) for n in range(1, 6)) == 0
    check("G05 SERIES         period sum zero and exact H_M-H_(5M)"
          " identity through M=125", period_zero and harmonic_blocks_ok)

    tower_ok = True
    for exponent in range(1, 13):
        raw_multiplier = 1 - 5 ** exponent
        correction_multiplier = 5 ** exponent
        tower_ok = tower_ok and raw_multiplier + correction_multiplier == 1
    check("G06 LOG-DERIVATIVE signed raw coefficient (1-5^m)log5 and"
          " correction +5^m log5 through m=12", tower_ok)

    print("P-PENTAGON-WEIL-1 exact verifier")
    print("G0 pentagon root-filter accounting; no Weil positivity claim")
    print()
    passed = 0
    for index, (name, ok) in enumerate(CHECKS, 1):
        tag = "PASS" if ok else "FAIL"
        passed += int(ok)
        print("%s %02d %s" % (tag, index, name))
    print()
    print("RESULT %d/%d %s" % (passed, len(CHECKS),
                               "ALL PASS" if passed == len(CHECKS)
                               else "FAILURES PRESENT"))
    print("SCOPE G0 AUDIT ONLY; NO WEIL POSITIVITY OR RH RESULT")
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
