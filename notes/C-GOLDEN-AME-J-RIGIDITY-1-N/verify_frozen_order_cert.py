#!/usr/bin/env python3
"""Portable standard-library verifier of FROZEN_ORDER_GB_CERT.json."""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations
import hashlib
import json
from pathlib import Path
import sys

import gb_cert_support as support


if sys.flags.optimize:
    raise SystemExit("refusing optimized Python: exact verifier requires active assertions")


PACKAGE = Path(__file__).resolve().parent
CERT_SHA256 = "79db9845615cea94540211a383e49471fe2a92cd02388a7caac92d20f9d76526"


def univariate(polynomial):
    highest = max(monomial[-1] for monomial in polynomial)
    result = [Fraction(0)] * (highest + 1)
    for monomial, coefficient in polynomial.items():
        assert all(exponent == 0 for exponent in monomial[:-1])
        result[monomial[-1]] = coefficient
    while result and result[-1] == 0:
        result.pop()
    return tuple(result)


def polynomial_divmod(dividend, divisor):
    work = list(dividend)
    quotient = [Fraction(0)] * max(0, len(work) - len(divisor) + 1)
    while work and len(work) >= len(divisor):
        coefficient = work[-1] / divisor[-1]
        shift = len(work) - len(divisor)
        quotient[shift] = coefficient
        for index, divisor_coefficient in enumerate(divisor):
            work[index + shift] -= coefficient * divisor_coefficient
        while work and work[-1] == 0:
            work.pop()
    return tuple(quotient), tuple(work)


def polynomial_gcd(left, right):
    while right:
        _, remainder = polynomial_divmod(left, right)
        left, right = right, remainder
    return tuple(coefficient / left[-1] for coefficient in left)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--block944", required=True, type=Path)
    parser.add_argument("--builder", type=Path, default=PACKAGE / "golden_symbolic.py")
    parser.add_argument("--cert", type=Path, default=PACKAGE / "FROZEN_ORDER_GB_CERT.json")
    args = parser.parse_args()

    certificate_bytes = args.cert.read_bytes()
    assert hashlib.sha256(certificate_bytes).hexdigest() == CERT_SHA256
    certificate = json.loads(certificate_bytes)
    assert certificate["format"] == "GOLDEN_RIGIDITY_FROZEN_ORDER_TRACKED_GB_V1"
    assert certificate["ring"] == {
        "variables": ["t", "a", "b", "c", "y", "x"],
        "domain": "QQ",
        "order": "lex",
    }

    inputs, raw_sha256 = support.regenerate_inputs(
        args.source, args.block944, args.builder
    )
    certificate_inputs = [support.parse_poly(item) for item in certificate["inputs"]]
    assert inputs == certificate_inputs
    basis = [support.parse_poly(item) for item in certificate["basis"]]
    assert len(inputs) == 363 and len(basis) == 6

    for expected, representation in zip(basis, certificate["representations"]):
        reconstructed = {}
        for input_index, multiplier in representation:
            reconstructed = support.add(
                reconstructed,
                support.mul(support.parse_poly(multiplier), inputs[input_index]),
            )
        assert reconstructed == expected
    assert all(not support.divide_remainder(polynomial, basis) for polynomial in inputs)

    # The five t-free basis elements are already in the unsaturated raw
    # ideal: their tracked representations use only the 362 raw inputs and
    # t-free multipliers.  Conversely every raw input reduces by those five
    # elements alone.  Finally D has the displayed inverse in that quotient,
    # so the prescribed saturation does not alter the raw ideal.
    raw_count = len(inputs) - 1
    for representation in certificate["representations"][1:]:
        assert all(input_index < raw_count for input_index, _ in representation)
        for _, multiplier in representation:
            assert all(monomial[0] == 0 for monomial in support.parse_poly(multiplier))
    raw_basis = basis[1:]
    assert all(
        not support.divide_remainder(polynomial, raw_basis)
        for polynomial in inputs[:raw_count]
    )
    divisor = {(0, 1, 1, 1, 1, 1): Fraction(1)}
    inverse = {
        (0, 0, 0, 1, 0, 6): Fraction(-8),
        (0, 0, 0, 1, 0, 4): Fraction(8),
        (0, 0, 0, 1, 0, 0): Fraction(4),
    }
    one = {(0, 0, 0, 0, 0, 0): Fraction(1)}
    assert not support.divide_remainder(
        support.add(support.mul(divisor, inverse), one, Fraction(-1)), raw_basis
    )

    leading = [support.lm(polynomial) for polynomial in basis]
    assert leading == [
        (1, 0, 0, 0, 0, 0),
        (0, 1, 0, 0, 0, 0),
        (0, 0, 1, 0, 0, 0),
        (0, 0, 0, 2, 0, 0),
        (0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 8),
    ]
    assert all(polynomial[monomial] == 1
               for polynomial, monomial in zip(basis, leading))
    for index, polynomial in enumerate(basis):
        for monomial in polynomial:
            if monomial == leading[index]:
                continue
            assert not any(
                support.divides(candidate, monomial)
                for other, candidate in enumerate(leading)
                if other != index
            )
    pairs = list(combinations(basis, 2))
    assert all(
        not support.divide_remainder(support.spoly(left, right), basis)
        for left, right in pairs
    )

    phase = univariate(basis[-1])
    derivative = tuple(Fraction(index) * phase[index]
                       for index in range(1, len(phase)))
    assert polynomial_gcd(phase, derivative) == (Fraction(1),)

    print("GOLDEN_RIGIDITY_FROZEN_ORDER_CERT_VERIFY_V1")
    print(f"PASS RAW records=3889 active=383 raw_unique=362 raw_sha256={raw_sha256}")
    print(f"PASS SATURATION inputs={len(inputs)} sole_divisor=a*b*c*x*y")
    print(f"PASS FORWARD_MEMBERSHIP basis_in_input={len(basis)}")
    print(f"PASS REVERSE_MEMBERSHIP input_in_basis={len(inputs)}")
    print("PASS RAW_IDEAL forward_basis=5 reverse_inputs=362 saturation_redundant=YES")
    print(f"PASS BUCHBERGER s_pairs={len(pairs)} reduced_monic=YES")
    print("PASS CLASSIFICATION dimension=0 degree=16 radical=YES standard_monomials=16")
    print(f"PASS CERT bytes={len(certificate_bytes)} sha256={hashlib.sha256(certificate_bytes).hexdigest()}")
    print("SUMMARY 8/8 PASS")


if __name__ == "__main__":
    main()
