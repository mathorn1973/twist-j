#!/usr/bin/env python3
"""
Exact verifier for P-SO3-FINITE-ANISOTROPY-DEPTH-1.

Scientific target:
  For the polyhedral finite rotation groups in SO(3), compute the first
  nonzero invariant harmonic degree by exact character averaging. Independently
  compute the polynomial Molien series from conjugacy-class rotation angles,
  compare the harmonic decomposition, and verify the A5 golden trace field.

The infinite C_n and D_n families are discharged by the proof in PREREG.md.
This script audits the polyhedral arithmetic only.

Standard library only. Exact arithmetic only.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable


@dataclass(frozen=True)
class Q5:
    """a + b*sqrt(5), with a,b in Q."""

    a: Fraction
    b: Fraction = Fraction(0)

    @staticmethod
    def coerce(x: "Q5 | Fraction | int") -> "Q5":
        if isinstance(x, Q5):
            return x
        return Q5(Fraction(x), Fraction(0))

    def __add__(self, other: "Q5 | Fraction | int") -> "Q5":
        o = Q5.coerce(other)
        return Q5(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self) -> "Q5":
        return Q5(-self.a, -self.b)

    def __sub__(self, other: "Q5 | Fraction | int") -> "Q5":
        return self + (-Q5.coerce(other))

    def __rsub__(self, other: "Q5 | Fraction | int") -> "Q5":
        return Q5.coerce(other) - self

    def __mul__(self, other: "Q5 | Fraction | int") -> "Q5":
        o = Q5.coerce(other)
        return Q5(
            self.a * o.a + 5 * self.b * o.b,
            self.a * o.b + self.b * o.a,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: "Q5 | Fraction | int") -> "Q5":
        o = Q5.coerce(other)
        den = o.a * o.a - 5 * o.b * o.b
        if den == 0:
            raise ZeroDivisionError
        return Q5(
            (self.a * o.a - 5 * self.b * o.b) / den,
            (self.b * o.a - self.a * o.b) / den,
        )

    def as_integer(self) -> int:
        if self.b != 0 or self.a.denominator != 1:
            raise AssertionError(f"not an integer: {self}")
        return int(self.a)


ZERO = Q5(Fraction(0))
ONE = Q5(Fraction(1))


def q(a: int | Fraction, b: int | Fraction = 0) -> Q5:
    return Q5(Fraction(a), Fraction(b))


# c(theta) = 2 cos(theta)
C_ID = q(2)
C_PI = q(-2)
C_2PI3 = q(-1)
C_PI2 = q(0)
C_2PI5 = q(Fraction(-1, 2), Fraction(1, 2))
C_4PI5 = q(Fraction(-1, 2), Fraction(-1, 2))

CLASSES = {
    "A4": ((1, C_ID), (3, C_PI), (8, C_2PI3)),
    "S4": ((1, C_ID), (9, C_PI), (8, C_2PI3), (6, C_PI2)),
    "A5": (
        (1, C_ID),
        (15, C_PI),
        (20, C_2PI3),
        (12, C_2PI5),
        (12, C_4PI5),
    ),
}
ORDERS = {"A4": 12, "S4": 24, "A5": 60}


def harmonic_character(c: Q5, ell: int) -> Q5:
    """
    Character of H_ell(R^3) at a rotation with c = 2 cos(theta):
      chi_ell = 1 + 2 sum_{k=1}^ell cos(k theta).
    The terms a_k = 2 cos(k theta) obey a_k = c a_(k-1) - a_(k-2).
    """
    if ell == 0:
        return ONE
    a_prev = q(2)
    a_cur = c
    total = ONE + a_cur
    for _k in range(2, ell + 1):
        a_next = c * a_cur - a_prev
        total = total + a_next
        a_prev, a_cur = a_cur, a_next
    return total


def invariant_harmonic_multiplicities(group: str, ell_max: int) -> list[int]:
    out: list[int] = []
    for ell in range(ell_max + 1):
        total = ZERO
        for size, c in CLASSES[group]:
            total = total + size * harmonic_character(c, ell)
        out.append((total / ORDERS[group]).as_integer())
    return out


def first_positive_degree(values: list[int]) -> int:
    for ell, value in enumerate(values[1:], start=1):
        if value > 0:
            return ell
    raise AssertionError("no positive invariant degree in audited range")


Poly = list[Q5]


def ptrim(p: Poly) -> Poly:
    out = list(p)
    while len(out) > 1 and out[-1] == ZERO:
        out.pop()
    return out


def padd(p: Poly, r: Poly) -> Poly:
    n = max(len(p), len(r))
    out = [ZERO for _ in range(n)]
    for i in range(n):
        out[i] = (p[i] if i < len(p) else ZERO) + (
            r[i] if i < len(r) else ZERO
        )
    return ptrim(out)


def pscale(p: Poly, scalar: Q5 | Fraction | int) -> Poly:
    s = Q5.coerce(scalar)
    return ptrim([x * s for x in p])


def pmul(p: Poly, r: Poly) -> Poly:
    out = [ZERO for _ in range(len(p) + len(r) - 1)]
    for i, x in enumerate(p):
        for j, y in enumerate(r):
            out[i + j] = out[i + j] + x * y
    return ptrim(out)


def one_minus_t_power(k: int) -> Poly:
    out = [ZERO for _ in range(k + 1)]
    out[0] = ONE
    out[k] = -ONE
    return out


def class_denominator(c: Q5) -> Poly:
    # det(I - t R_theta) = (1-t)(1-c t+t^2)
    return pmul([ONE, -ONE], [ONE, -c, ONE])


def add_rational_terms(
    terms: Iterable[tuple[int, Poly, Poly]]
) -> tuple[Poly, Poly]:
    numerator: Poly = [ZERO]
    denominator: Poly = [ONE]
    for weight, n_i, d_i in terms:
        numerator = padd(
            pmul(numerator, d_i),
            pscale(pmul(n_i, denominator), weight),
        )
        denominator = pmul(denominator, d_i)
    return ptrim(numerator), ptrim(denominator)


def molien_rational(group: str) -> tuple[Poly, Poly]:
    terms = (
        (size, [ONE], class_denominator(c))
        for size, c in CLASSES[group]
    )
    numerator, denominator = add_rational_terms(terms)
    return pscale(numerator, Fraction(1, ORDERS[group])), denominator


def target_molien_rational(group: str) -> tuple[Poly, Poly]:
    if group == "A4":
        numerator = [ONE] + [ZERO] * 5 + [ONE]
        denominator = pmul(
            pmul(one_minus_t_power(2), one_minus_t_power(3)),
            one_minus_t_power(4),
        )
    elif group == "S4":
        numerator = [ONE] + [ZERO] * 8 + [ONE]
        denominator = pmul(
            pmul(one_minus_t_power(2), one_minus_t_power(4)),
            one_minus_t_power(6),
        )
    elif group == "A5":
        numerator = [ONE] + [ZERO] * 14 + [ONE]
        denominator = pmul(
            pmul(one_minus_t_power(2), one_minus_t_power(6)),
            one_minus_t_power(10),
        )
    else:
        raise AssertionError(group)
    return numerator, denominator


def rational_functions_equal(
    left: tuple[Poly, Poly], right: tuple[Poly, Poly]
) -> bool:
    n1, d1 = left
    n2, d2 = right
    return ptrim(pmul(n1, d2)) == ptrim(pmul(n2, d1))


def class_series(c: Q5, n_max: int) -> list[Q5]:
    """
    Coefficients of 1 / ((1-t)(1-c t+t^2)).
    """
    b = [ONE]
    if n_max >= 1:
        b.append(c)
    for _n in range(2, n_max + 1):
        b.append(c * b[-1] - b[-2])
    out: list[Q5] = []
    partial = ZERO
    for x in b:
        partial = partial + x
        out.append(partial)
    return out


def molien_coefficients(group: str, n_max: int) -> list[int]:
    sums = [ZERO for _ in range(n_max + 1)]
    for size, c in CLASSES[group]:
        series = class_series(c, n_max)
        for n, value in enumerate(series):
            sums[n] = sums[n] + size * value
    return [(x / ORDERS[group]).as_integer() for x in sums]


def check(label: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"{label} PASS")


def main() -> int:
    print("P-SO3-FINITE-ANISOTROPY-DEPTH-1")

    h_a4 = invariant_harmonic_multiplicities("A4", 16)
    h_s4 = invariant_harmonic_multiplicities("S4", 16)
    h_a5 = invariant_harmonic_multiplicities("A5", 16)

    check("G01 A4 harmonic depth=3", first_positive_degree(h_a4) == 3)
    check("G02 S4 harmonic depth=4", first_positive_degree(h_s4) == 4)
    check("G03 A5 harmonic void degrees 1..5", h_a5[1:6] == [0, 0, 0, 0, 0])
    check("G04 A5 harmonic degree 6 multiplicity=1", h_a5[6] == 1)

    check(
        "G05 A4 Molien identity",
        rational_functions_equal(molien_rational("A4"), target_molien_rational("A4")),
    )
    check(
        "G06 S4 Molien identity",
        rational_functions_equal(molien_rational("S4"), target_molien_rational("S4")),
    )
    check(
        "G07 A5 Molien identity",
        rational_functions_equal(molien_rational("A5"), target_molien_rational("A5")),
    )

    molien = {
        group: molien_coefficients(group, 16)
        for group in ("A4", "S4", "A5")
    }
    harmonic = {"A4": h_a4, "S4": h_s4, "A5": h_a5}
    agree = True
    for group in ("A4", "S4", "A5"):
        for ell in range(17):
            radial = molien[group][ell - 2] if ell >= 2 else 0
            if molien[group][ell] - radial != harmonic[group][ell]:
                agree = False
    check("G08 character-Molien harmonic agreement through degree 16", agree)

    a5_expected = [1, 0, 1, 0, 1, 0, 2, 0, 2, 0, 3, 0, 4, 0, 4, 1, 5]
    check("G09 A5 Molien coefficients degree 0..16", molien["A5"] == a5_expected)

    trace_5a = ONE + C_2PI5
    trace_5b = ONE + C_4PI5
    phi = q(Fraction(1, 2), Fraction(1, 2))
    one_minus_phi = q(Fraction(1, 2), Fraction(-1, 2))
    check(
        "G10 A5 order-5 traces are phi and 1-phi",
        trace_5a == phi and trace_5b == one_minus_phi,
    )
    check(
        "G11 A5 order-5 trace field is Q(sqrt5)",
        trace_5a - trace_5b == q(0, 1),
    )

    print("ALL PASS 11/11")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
