#!/usr/bin/env python3
"""Frozen construction and arithmetic skeleton for the artisanal F8 attack.

Pre-lock safety properties:

* this module imports no project/source parser;
* it opens no files;
* it contains no golden tensor data;
* its CLI never constructs or contracts a target tensor;
* the post-lock contraction entry point deliberately raises NotImplementedError.

The pure functions below freeze conventions that a later verifier must use.
Defining a construction is not an evaluation of any LU invariant.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
import itertools
from typing import Iterable, Iterator, Sequence


DIMENSION = 6
XI_ORDER = 120
K120_DEGREE = 32
LOCATOR_PRIME = 241
LOCATOR_XI = 3

# Low-to-high coefficients of
# Phi_120(X)=X^32+X^28-X^20-X^16-X^12+X^4+1.
PHI120 = (
    1,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    -1,
    0,
    0,
    0,
    -1,
    0,
    0,
    0,
    -1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
)

ID4 = (0, 1, 2, 3)
DESCRIPTORS = (
    ((1, 0, 3, 2), (2, 3, 0, 1), (3, 2, 1, 0)),
    ((1, 0, 3, 2), (2, 3, 1, 0), (3, 2, 0, 1)),
    ((1, 2, 3, 0), (2, 3, 0, 1), (3, 0, 1, 2)),
    ((1, 2, 3, 0), (3, 0, 1, 2), (2, 3, 0, 1)),
)

# Fixed generic binary contraction path.  B means a conjugate tensor factor.
JOIN_PLAN = (
    ("A0", "B3"),
    ("A3", "B2"),
    ("$0", "$1"),
    ("A2", "B1"),
    ("$2", "$3"),
    ("$4", "B0"),
    ("$5", "A1"),
)


def polynomial_divexact(dividend: Sequence[int], divisor: Sequence[int]) -> tuple[int, ...]:
    """Exact low-to-high division by a monic integer polynomial."""

    remainder = list(dividend)
    quotient = [0] * (len(dividend) - len(divisor) + 1)
    while len(remainder) >= len(divisor):
        degree = len(remainder) - len(divisor)
        coefficient = remainder[-1]
        quotient[degree] = coefficient
        for offset, value in enumerate(divisor):
            remainder[degree + offset] -= coefficient * value
        while remainder and remainder[-1] == 0:
            remainder.pop()
    if remainder:
        raise AssertionError("non-exact cyclotomic polynomial division")
    return tuple(quotient)


@lru_cache(maxsize=None)
def cyclotomic_coefficients(order: int) -> tuple[int, ...]:
    """Derive Phi_order from x^order-1 without a CAS."""

    polynomial = (-1,) + (0,) * (order - 1) + (1,)
    for divisor in range(1, order):
        if order % divisor == 0:
            polynomial = polynomial_divexact(polynomial, cyclotomic_coefficients(divisor))
    return polynomial


def inverse_permutation(p: Sequence[int]) -> tuple[int, ...]:
    out = [0] * len(p)
    for i, value in enumerate(p):
        out[value] = i
    return tuple(out)


def phi120_eval(value: int, modulus: int | None = None) -> int:
    total = sum(coefficient * value**power for power, coefficient in enumerate(PHI120))
    return total if modulus is None else total % modulus


def multiplicative_order(value: int, prime: int) -> int:
    if value % prime == 0:
        raise ValueError("zero has no multiplicative order")
    current = 1
    for order in range(1, prime):
        current = current * value % prime
        if current == 1:
            return order
    raise AssertionError("F_p^* order search failed")


def reduce_k120(coefficients: Iterable[Fraction | int]) -> tuple[Fraction, ...]:
    """Reduce a polynomial to the frozen rational power basis of K120."""

    values = [Fraction(x) for x in coefficients]
    if len(values) < K120_DEGREE:
        values.extend([Fraction(0)] * (K120_DEGREE - len(values)))
    for degree in range(len(values) - 1, K120_DEGREE - 1, -1):
        lead = values[degree]
        if not lead:
            continue
        values[degree] = 0
        # X^32 = -X^28+X^20+X^16+X^12-X^4-1.
        values[degree - 4] -= lead
        values[degree - 12] += lead
        values[degree - 16] += lead
        values[degree - 20] += lead
        values[degree - 28] -= lead
        values[degree - 32] -= lead
    return tuple(values[:K120_DEGREE])


def reduce_p_integral_rational(value: Fraction, prime: int = LOCATOR_PRIME) -> int:
    """Reduce a p-integral rational; reject a denominator divisible by p."""

    denominator = value.denominator % prime
    if denominator == 0:
        raise ValueError("coefficient is not p-integral")
    return value.numerator % prime * pow(denominator, -1, prime) % prime


def reduce_k120_mod_locator(coefficients: Iterable[Fraction | int]) -> int:
    """Apply the frozen reduction xi -> 3 in F_241.

    This is a homomorphism from the 241-integral localized cyclotomic order,
    not a field homomorphism Q(zeta_120) -> F_241.
    """

    reduced = reduce_k120(coefficients)
    total = 0
    power = 1
    for coefficient in reduced:
        total += reduce_p_integral_rational(coefficient) * power
        power = power * LOCATOR_XI % LOCATOR_PRIME
    return total % LOCATOR_PRIME


@dataclass(frozen=True)
class QZeta6Numerator:
    """Integer numerator a+b*w in basis (1,w), w=zeta_6.

    Artisanal U_lambda entries are instances of this class divided by six.
    The identities are w^2=w-1 and conjugate(w)=1-w.
    """

    a: int
    b: int

    def __add__(self, other: "QZeta6Numerator") -> "QZeta6Numerator":
        return QZeta6Numerator(self.a + other.a, self.b + other.b)

    def __mul__(self, other: "QZeta6Numerator") -> "QZeta6Numerator":
        return QZeta6Numerator(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a + self.b * other.b,
        )

    def conjugate(self) -> "QZeta6Numerator":
        return QZeta6Numerator(self.a + self.b, -self.b)


ZETA6_POWERS = (
    QZeta6Numerator(1, 0),
    QZeta6Numerator(0, 1),
    QZeta6Numerator(-1, 1),
    QZeta6Numerator(-1, 0),
    QZeta6Numerator(0, -1),
    QZeta6Numerator(1, -1),
)


def crt_coordinates(value: int) -> tuple[int, int]:
    """The fixed Z_6 -> Z_3 x Z_2 coordinate map."""

    value %= 6
    return value % 3, value % 2


def gl2_f3() -> tuple[tuple[tuple[int, int], tuple[int, int]], ...]:
    """Frozen lexicographic row-major enumeration of GL(2,F_3)."""

    matrices = []
    for a, b, c, d in itertools.product(range(3), repeat=4):
        if (a * d - b * c) % 3:
            matrices.append(((a, b), (c, d)))
    return tuple(matrices)


def lifted_gl_transpose_action(
    matrix: tuple[tuple[int, int], tuple[int, int]], p: int, q: int
) -> tuple[int, int]:
    """Apply hat(G)^T, hat(G)=4G+3I modulo six (paper Lemma 18)."""

    lifted = tuple(
        tuple((4 * matrix[row][column] + 3 * (row == column)) % 6 for column in range(2))
        for row in range(2)
    )
    return (
        (lifted[0][0] * p + lifted[1][0] * q) % 6,
        (lifted[0][1] * p + lifted[1][1] * q) % 6,
    )


def artisanal_phase_exponent(kind: str, p: int, q: int) -> int:
    """Return phi(p,q) in F_3 for the two frozen Theorem-1 reps."""

    if kind not in {"sym", "sparse"}:
        raise ValueError("kind must be 'sym' or 'sparse'")
    k, x = crt_coordinates(p)
    ell, y = crt_coordinates(q)
    base = k * k + ell * ell
    if (x, y) == (1, 1):
        return base % 3
    m = (x - y) % 3
    if kind == "sym":
        correction = -(k + ell + m) ** 2
    elif kind == "sparse":
        correction = (ell + m) ** 2
    return (base + correction) % 3


def artisanal_entry_numerator(
    kind: str, i: int, j: int, k: int, ell: int
) -> QZeta6Numerator | None:
    """Construct the numerator of a direct U_lambda matrix entry.

    Return None for structural zero.  Otherwise the actual tensor entry is
    the returned `(a+b*zeta_6)/6`.  Indices use row=6*i+j, col=6*k+ell.
    This freezes Eq. (4), rather than substituting the Theorem-2 Hadamard G.
    """

    q = (i - j) % 6
    if q != (k - ell) % 6:
        return None
    total = QZeta6Numerator(0, 0)
    for p in range(6):
        phi = artisanal_phase_exponent(kind, p, q)
        exponent = (2 * phi + p * (i - k)) % 6
        total += ZETA6_POWERS[exponent]
    return total


def iter_artisanal_tensor_entries(kind: str) -> Iterator[tuple[tuple[int, ...], QZeta6Numerator]]:
    """Yield nonzero direct-U entries; definition only, never called by CLI."""

    for i in range(6):
        for j in range(6):
            for k in range(6):
                for ell in range(6):
                    numerator = artisanal_entry_numerator(kind, i, j, k, ell)
                    if numerator is not None and numerator != QZeta6Numerator(0, 0):
                        yield (i, j, k, ell), numerator


def factor_wire_labels(descriptor: Sequence[Sequence[int]]) -> dict[str, tuple]:
    """Return the eight rank-four factor label tuples for one descriptor."""

    matchings = (ID4,) + tuple(tuple(p) for p in descriptor)
    inverses = tuple(inverse_permutation(p) for p in matchings)
    labels: dict[str, tuple] = {}
    for r in range(4):
        labels[f"A{r}"] = tuple((colour, r) for colour in range(4))
    for s in range(4):
        labels[f"B{s}"] = tuple(
            (colour, inverses[colour][s]) for colour in range(4)
        )
    return labels


def audit_join_plan(descriptor: Sequence[Sequence[int]]) -> tuple[int, int]:
    """Return (maximum boundary rank, dense multiply-add count)."""

    tables = {name: frozenset(labels) for name, labels in factor_wire_labels(descriptor).items()}
    results: list[frozenset] = []
    maximum_rank = max(map(len, tables.values()))
    operation_count = 0

    def resolve(name: str) -> frozenset:
        return results[int(name[1:])] if name.startswith("$") else tables[name]

    for left_name, right_name in JOIN_PLAN:
        left = resolve(left_name)
        right = resolve(right_name)
        shared = left & right
        if not shared:
            raise AssertionError("frozen join plan contains an outer product")
        output = left ^ right
        operation_count += DIMENSION ** (len(output) + len(shared))
        results.append(output)
        maximum_rank = max(maximum_rank, len(output))
    if results[-1]:
        raise AssertionError("frozen join plan did not close to a scalar")
    return maximum_rank, operation_count


def party_invariant_fingerprint(values: Sequence):
    """Return (v0,e1,e2,e3) from (v0,v1,v2,v3)."""

    if len(values) != 4:
        raise ValueError("four descriptor values required")
    v0, v1, v2, v3 = values
    return (
        v0,
        v1 + v2 + v3,
        v1 * v2 + v1 * v3 + v2 * v3,
        v1 * v2 * v3,
    )


def contract_target_postlock(*args, **kwargs):
    """Deliberately absent before the public lock."""

    raise NotImplementedError(
        "post-lock only: implement from the public prereg without changing conventions"
    )


def self_test() -> None:
    """Test frozen arithmetic/labels only; construct and contract no target."""

    if len(PHI120) != 33 or PHI120[-1] != 1:
        raise AssertionError("bad Phi_120 coefficient vector")
    if cyclotomic_coefficients(XI_ORDER) != PHI120:
        raise AssertionError("Phi_120 does not match the exact cyclotomic derivation")
    if phi120_eval(LOCATOR_XI, LOCATOR_PRIME) != 0:
        raise AssertionError("locator is not a root of Phi_120")
    if multiplicative_order(LOCATOR_XI, LOCATOR_PRIME) != XI_ORDER:
        raise AssertionError("locator does not have order 120")
    if any(
        multiplicative_order(candidate, LOCATOR_PRIME) == XI_ORDER
        for candidate in range(1, LOCATOR_XI)
    ):
        raise AssertionError("locator is not the least positive order-120 element")
    golden_a_denominator = (
        pow(LOCATOR_XI, 6, LOCATOR_PRIME)
        + pow(LOCATOR_XI, -6, LOCATOR_PRIME)
    ) % LOCATOR_PRIME
    if golden_a_denominator != 207 or golden_a_denominator == 0:
        raise AssertionError("golden amplitude denominator is bad at locator")
    if pow(LOCATOR_XI, -1, LOCATOR_PRIME) != 161:
        raise AssertionError("conjugate locator image is wrong")
    if reduce_k120_mod_locator(PHI120) != 0:
        raise AssertionError("cyclotomic relation does not reduce to zero")
    w = QZeta6Numerator(0, 1)
    if w * w != QZeta6Numerator(-1, 1):
        raise AssertionError("zeta_6 multiplication convention failed")
    if w.conjugate() != QZeta6Numerator(1, -1):
        raise AssertionError("zeta_6 conjugation convention failed")
    if len(gl2_f3()) != 48:
        raise AssertionError("GL(2,F_3) census failed")
    for descriptor in DESCRIPTORS:
        labels = factor_wire_labels(descriptor)
        if set(labels) != {f"A{i}" for i in range(4)} | {f"B{i}" for i in range(4)}:
            raise AssertionError("factor label construction failed")
        wire_counts = Counter(wire for factor in labels.values() for wire in factor)
        if len(wire_counts) != 16 or set(wire_counts.values()) != {2}:
            raise AssertionError("closed factor graph is not a pairing")
        if audit_join_plan(descriptor) != (8, 122_053_392):
            raise AssertionError("frozen join-plan audit failed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        print("ARTISAN_F8_CONSTRUCTION_SKELETON_V1")
        print("FIELD=Q(zeta_120)_POWER_BASIS_DEGREE_32")
        print("REDUCTION=Z_(241)[xi,(xi6+xi-6)^-1]_TO_F241_XI_MAPS_TO_3")
        print("ORDER_F241_OF_3=120")
        print("CONJUGATE_XI_MAPS_TO_161")
        print("GOLDEN_A_DENOMINATOR_MOD241=207")
        print("GENERIC_JOIN_MAX_RANK=8")
        print("GENERIC_JOIN_MULTIPLY_ADDS=122053392")
        print("SOURCE_IO=NONE")
        print("TARGET_CONSTRUCTION=NOT_EXECUTED")
        print("TARGET_INVARIANT=NOT_COMPUTED")
        print("STATUS=PASS")
    else:
        print("SKELETON_ONLY: use --self-test; post-lock contraction is intentionally absent")


if __name__ == "__main__":
    main()
