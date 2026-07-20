#!/usr/bin/env python3
"""Pinned exact-interval N2 verifier for C-LI-Q-MOMENT-1.

This verifier derives the sigma_4 row from the frozen Stieltjes convention,
refreshes gamma_0 through gamma_3 with one outward-rounded B4
Euler--Maclaurin calculation, and decides the shifted Hankel determinant

    SH-1' = qw_1 * qw_3 - qw_2^2.

It also proves algebraically that SH-1' is the determinant of the
antisymmetric 2 by 2 block of the Li Toeplitz matrix T_3.  That junction is
not a proof that the whole T_3 is positive.

Only Python's standard library is used.  Every asserted numerical value is
an integer fixed-point interval.  There are no decimal imports, zero lists,
prime tables, Li tables, files, network calls, subprocesses, random inputs,
or floating-point operations.  Passing this reference-side calibration does
not construct a J-native moment functional and does not prove RH.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", newline="\n", write_through=True)


S = 10**24
N = 200_000
LOG_TERMS = 32
GAMMA3_MAX_WIDTH = 10**7  # 1e-17 at scale 1e24, frozen before first run.

FAILED: list[str] = []


def floor_frac(q: Fraction) -> int:
    return q.numerator * S // q.denominator


def ceil_frac(q: Fraction) -> int:
    return -((-q.numerator * S) // q.denominator)


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def fmt_scaled(v: int, digits: int = 24) -> str:
    sign = "-" if v < 0 else ""
    whole, frac = divmod(abs(v), S)
    return sign + f"{whole}.{frac:024d}"[: len(str(whole)) + 1 + digits]


@dataclass(frozen=True)
class I:
    lo: int
    hi: int

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError((self.lo, self.hi))

    @staticmethod
    def exact_int(n: int) -> "I":
        return I(n * S, n * S)

    @staticmethod
    def from_fraction(q: Fraction) -> "I":
        return I(floor_frac(q), ceil_frac(q))

    def __add__(self, other: "I") -> "I":
        return I(self.lo + other.lo, self.hi + other.hi)

    def __sub__(self, other: "I") -> "I":
        return I(self.lo - other.hi, self.hi - other.lo)

    def __neg__(self) -> "I":
        return I(-self.hi, -self.lo)

    def mul(self, other: "I") -> "I":
        corners = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return I(min(corners) // S, ceil_div(max(corners), S))

    def div_int(self, n: int) -> "I":
        assert n > 0
        return I(self.lo // n, ceil_div(self.hi, n))

    def mul_int(self, n: int) -> "I":
        if n >= 0:
            return I(self.lo * n, self.hi * n)
        return I(self.hi * n, self.lo * n)

    def square(self) -> "I":
        if self.lo >= 0:
            return I(
                (self.lo * self.lo) // S,
                ceil_div(self.hi * self.hi, S),
            )
        if self.hi <= 0:
            return I(
                (self.hi * self.hi) // S,
                ceil_div(self.lo * self.lo, S),
            )
        return I(0, ceil_div(max(self.lo**2, self.hi**2), S))

    def pow_int(self, n: int) -> "I":
        assert n >= 0
        out = I.exact_int(1)
        base = self
        exponent = n
        while exponent:
            if exponent & 1:
                out = out.mul(base)
            exponent >>= 1
            if exponent:
                base = base.mul(base)
        return out

    def positive(self) -> bool:
        return self.lo > 0

    def negative(self) -> bool:
        return self.hi < 0

    def subset_of(self, other: "I") -> bool:
        return other.lo <= self.lo and self.hi <= other.hi

    def overlaps(self, other: "I") -> bool:
        return max(self.lo, other.lo) <= min(self.hi, other.hi)

    def width(self) -> int:
        return self.hi - self.lo

    def fmt(self, digits: int = 24) -> str:
        return f"[{fmt_scaled(self.lo, digits)}, {fmt_scaled(self.hi, digits)}]"


def log_unit_rational(num: int, den: int, terms: int = LOG_TERMS) -> I:
    """Rigorous log(num/den) for 1 <= num/den <= 2 via atanh."""
    assert den > 0 and den <= num <= 2 * den
    a = num - den
    b = num + den
    if a == 0:
        return I(0, 0)

    a2 = a * a
    b2 = b * b
    ap = a
    bp = b
    lo_sum = 0
    hi_sum = 0
    for k in range(terms):
        odd = 2 * k + 1
        denominator = bp * odd
        lo_sum += (S * ap) // denominator
        hi_sum += ceil_div(S * ap, denominator)
        ap *= a2
        bp *= b2

    power = 2 * terms + 1
    tail_num = 2 * pow(a, power) * b2
    tail_den = power * pow(b, power) * (b2 - a2)
    tail_hi = ceil_div(S * tail_num, tail_den)
    return I(2 * lo_sum, 2 * hi_sum + tail_hi)


LOG2 = log_unit_rational(2, 1)


def log_integer(k: int) -> I:
    assert k >= 1
    exponent = k.bit_length() - 1
    base = 1 << exponent
    return LOG2.mul_int(exponent) + log_unit_rational(k, base)


def arctan_inv_bounds(q: int, terms: int) -> I:
    partials: list[Fraction] = [Fraction(0)]
    total = Fraction(0)
    for k in range(terms + 1):
        term = Fraction(1, (2 * k + 1) * pow(q, 2 * k + 1))
        total = total + term if k % 2 == 0 else total - term
        partials.append(total)
    left = partials[terms]
    right = partials[terms + 1]
    lo, hi = (left, right) if left <= right else (right, left)
    return I(floor_frac(lo), ceil_frac(hi))


def pi_interval() -> I:
    return (
        arctan_inv_bounds(5, 22).mul_int(16)
        - arctan_inv_bounds(239, 7).mul_int(4)
    )


def finite_sum_intervals(n: int) -> tuple[list[I], I]:
    """Return sum(log(k)^p/k), p=0..3, and sum(1/k^3)."""
    lo = [0, 0, 0, 0]
    hi = [0, 0, 0, 0]
    z3_lo = z3_hi = 0

    for k in range(1, n + 1):
        powers = [I.exact_int(1)]
        logk = log_integer(k)
        powers.append(logk)
        powers.append(logk.square())
        powers.append(powers[2].mul(logk))
        for p, value in enumerate(powers):
            lo[p] += value.lo // k
            hi[p] += ceil_div(value.hi, k)

        cube = k**3
        z3_lo += S // cube
        z3_hi += ceil_div(S, cube)

    return [I(lo[p], hi[p]) for p in range(4)], I(z3_lo, z3_hi)


def derivative_polynomial(power: int, order: int) -> list[int]:
    """P with d^order(log(x)^power/x)=P(log(x))/x^(order+1)."""
    coefficients = [0] * power + [1]
    for r in range(order):
        derivative = [
            (i + 1) * coefficients[i + 1]
            for i in range(len(coefficients) - 1)
        ] + [0]
        coefficients = [
            derivative[i] - (r + 1) * coefficients[i]
            for i in range(len(coefficients))
        ]
    return coefficients


def polynomial_derivative(coefficients: list[int]) -> list[int]:
    if len(coefficients) <= 1:
        return [0]
    return [(i + 1) * coefficients[i + 1] for i in range(len(coefficients) - 1)]


def polynomial_fraction_value(coefficients: list[int], x: Fraction) -> Fraction:
    out = Fraction(0)
    for coefficient in reversed(coefficients):
        out = out * x + coefficient
    return out


def polynomial_interval_value(coefficients: list[int], x: I) -> I:
    out = I.exact_int(0)
    for coefficient in reversed(coefficients):
        out = out.mul(x) + I.exact_int(coefficient)
    return out


def derivative_interval(power: int, order: int, n: int, logn: I) -> I:
    numerator = polynomial_interval_value(derivative_polynomial(power, order), logn)
    return numerator.div_int(n ** (order + 1))


def em4_shape_gate(power: int, logn: I) -> bool:
    """Prove f'''<0 and f''''>0 on [N,infinity)."""
    p3 = derivative_polynomial(power, 3)
    p4 = derivative_polynomial(power, 4)
    if polynomial_interval_value(p3, logn).hi >= 0:
        return False

    # Every Taylor coefficient of P4 about this rational lower bound is
    # positive, hence P4(l)>0 for every l>=log(N).
    lower = Fraction(logn.lo, S)
    current = p4
    while current != [0]:
        if polynomial_fraction_value(current, lower) <= 0:
            return False
        current = polynomial_derivative(current)
    return True


def stieltjes_em4_interval(power: int, n: int, logn: I, partial: I) -> tuple[I, I]:
    """B4 Euler--Maclaurin enclosure for gamma_power.

    A=sum(log(k)^p/k)-log(N)^(p+1)/(p+1).  With f=log(x)^p/x,

      gamma_p=A-f(N)/2-f'(N)/12+f'''(N)/720+R,
      |R|<=-f'''(N)/720,

    after the separately checked tail shape f'''<0, f''''>0.
    """
    assert em4_shape_gate(power, logn)
    a_n = partial - logn.pow_int(power + 1).div_int(power + 1)
    f0 = derivative_interval(power, 0, n, logn)
    f1 = derivative_interval(power, 1, n, logn)
    f3 = derivative_interval(power, 3, n, logn)
    assert f3.negative()

    center = a_n - f0.div_int(2) - f1.div_int(12) + f3.div_int(720)
    radius = (-f3).div_int(720)
    return I(center.lo - radius.hi, center.hi + radius.hi), radius


def zeta3_interval(n: int, partial_sum: I) -> I:
    lower_tail = I.from_fraction(Fraction(1, 2 * (n + 1) ** 2))
    upper_tail = I.from_fraction(Fraction(1, 2 * n**2))
    return I(
        partial_sum.lo + lower_tail.lo,
        partial_sum.hi + upper_tail.hi,
    )


def log_4pi_interval(pi: I) -> I:
    lo = log_unit_rational(pi.lo, 2 * S)
    hi = log_unit_rational(pi.hi, 2 * S)
    return LOG2.mul_int(3) + I(lo.lo, hi.hi)


Poly = dict[tuple[int, ...], Fraction]


def poly_constant(dimension: int, value: Fraction) -> Poly:
    return {(0,) * dimension: value} if value else {}


def poly_variable(dimension: int, index: int) -> Poly:
    exponent = [0] * dimension
    exponent[index] = 1
    return {tuple(exponent): Fraction(1)}


def poly_add(a: Poly, b: Poly) -> Poly:
    out = dict(a)
    for monomial, coefficient in b.items():
        out[monomial] = out.get(monomial, Fraction(0)) + coefficient
        if out[monomial] == 0:
            del out[monomial]
    return out


def poly_scale(a: Poly, c: Fraction) -> Poly:
    return {m: c * v for m, v in a.items() if c * v != 0}


def poly_mul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            monomial = tuple(x + y for x, y in zip(ma, mb))
            out[monomial] = out.get(monomial, Fraction(0)) + ca * cb
            if out[monomial] == 0:
                del out[monomial]
    return out


def poly_pow(a: Poly, n: int) -> Poly:
    dimension = len(next(iter(a))) if a else 1
    out = poly_constant(dimension, Fraction(1))
    for _ in range(n):
        out = poly_mul(out, a)
    return out


def sigma4_derivation_gate() -> bool:
    """Derive [t^4] log(t*zeta(1+t)) and the gamma-factor row."""
    dimension = 5  # gamma, gamma1, gamma2, gamma3, pi^4
    gamma = poly_variable(dimension, 0)
    gamma1 = poly_variable(dimension, 1)
    gamma2 = poly_variable(dimension, 2)
    gamma3 = poly_variable(dimension, 3)
    pi4 = poly_variable(dimension, 4)

    a1 = gamma
    a2 = poly_scale(gamma1, Fraction(-1))
    a3 = poly_scale(gamma2, Fraction(1, 2))
    a4 = poly_scale(gamma3, Fraction(-1, 6))
    log_zeta_t4 = poly_add(
        poly_add(a4, poly_scale(poly_mul(a1, a3), Fraction(-1))),
        poly_add(
            poly_scale(poly_mul(a2, a2), Fraction(-1, 2)),
            poly_add(
                poly_mul(poly_mul(a1, a1), a2),
                poly_scale(poly_pow(a1, 4), Fraction(-1, 4)),
            ),
        ),
    )

    coefficient_t4 = poly_add(
        poly_add(poly_constant(dimension, Fraction(-1, 4)), poly_scale(pi4, Fraction(1, 384))),
        log_zeta_t4,
    )
    derived = poly_scale(coefficient_t4, Fraction(-4))
    expected = poly_add(
        poly_add(poly_constant(dimension, Fraction(1)), poly_pow(gamma, 4)),
        poly_add(
            poly_scale(poly_mul(poly_pow(gamma, 2), gamma1), Fraction(4)),
            poly_add(
                poly_scale(poly_pow(gamma1, 2), Fraction(2)),
                poly_add(
                    poly_scale(poly_mul(gamma, gamma2), Fraction(2)),
                    poly_add(
                        poly_scale(gamma3, Fraction(2, 3)),
                        poly_scale(pi4, Fraction(-1, 96)),
                    ),
                ),
            ),
        ),
    )
    return derived == expected


def third_junction_gate() -> bool:
    """SH-1' equals the determinant of the antisymmetric T3 block."""
    dimension = 4
    s1, s2, s3, s4 = [poly_variable(dimension, i) for i in range(4)]
    qw1 = poly_add(poly_scale(s1, Fraction(2)), s2)
    qw2 = poly_add(poly_add(poly_scale(s1, Fraction(6)), poly_scale(s2, Fraction(3))), s3)
    qw3 = poly_add(
        poly_add(poly_scale(s1, Fraction(20)), poly_scale(s2, Fraction(10))),
        poly_add(poly_scale(s3, Fraction(4)), s4),
    )
    direct = poly_add(poly_mul(qw1, qw3), poly_scale(poly_mul(qw2, qw2), Fraction(-1)))

    c0 = poly_scale(s1, Fraction(2))
    c1 = poly_scale(s2, Fraction(-1))
    c2 = poly_add(poly_scale(s2, Fraction(-1)), s3)
    c3 = poly_add(
        poly_add(poly_scale(s2, Fraction(-1)), poly_scale(s3, Fraction(2))),
        poly_scale(s4, Fraction(-1)),
    )
    anti00 = poly_add(c0, poly_scale(c3, Fraction(-1)))
    anti01 = poly_add(c1, poly_scale(c2, Fraction(-1)))
    anti11 = poly_add(c0, poly_scale(c1, Fraction(-1)))
    anti_det = poly_add(
        poly_mul(anti00, anti11),
        poly_scale(poly_mul(anti01, anti01), Fraction(-1)),
    )
    return direct == anti_det


def gate(name: str, condition: bool) -> None:
    print(("PASS " if condition else "FAIL ") + name)
    if not condition:
        FAILED.append(name)


def main() -> int:
    # Frozen N1 comparator intervals, represented exactly at scale 1e24.
    n1_sigma1 = I(23095708965079367097561, 23095708971329335948397)
    n1_sigma2 = I(-46154317344901637723149, -46154317237087378863919)
    n1_sigma3 = I(-111158665537209572582, -111157790857999161284)

    pi = pi_interval()
    logn = log_integer(N)
    sums, zeta3_partial = finite_sum_intervals(N)
    gammas: list[I] = []
    radii: list[I] = []
    for power in range(4):
        gamma_power, radius = stieltjes_em4_interval(power, N, logn, sums[power])
        gammas.append(gamma_power)
        radii.append(radius)
    gamma, gamma1, gamma2, gamma3 = gammas
    zeta3 = zeta3_interval(N, zeta3_partial)
    log4pi = log_4pi_interval(pi)

    one = I.exact_int(1)
    sigma1 = one + gamma.div_int(2) - log4pi.div_int(2)
    sigma2 = one + gamma.square() + gamma1.mul_int(2) - pi.square().div_int(8)
    sigma3 = (
        one
        + gamma.pow_int(3)
        + gamma.mul(gamma1).mul_int(3)
        + gamma2.mul_int(3).div_int(2)
        - zeta3.mul_int(7).div_int(8)
    )
    sigma4 = (
        one
        + gamma.pow_int(4)
        + gamma.square().mul(gamma1).mul_int(4)
        + gamma1.square().mul_int(2)
        + gamma.mul(gamma2).mul_int(2)
        + gamma3.mul_int(2).div_int(3)
        - pi.pow_int(4).div_int(96)
    )

    qw1 = sigma1.mul_int(2) + sigma2
    qw2 = sigma1.mul_int(6) + sigma2.mul_int(3) + sigma3
    qw3 = sigma1.mul_int(20) + sigma2.mul_int(10) + sigma3.mul_int(4) + sigma4
    sh1p_direct = qw1.mul(qw3) - qw2.square()
    sh1p_t3 = qw1.mul(qw1 + sigma4 - sigma3.mul_int(2)) - sigma3.square()

    print("C-LI-Q-MOMENT-1 N2 exact-interval verifier")
    print(f"scale=10^24  N={N}  log_terms={LOG_TERMS}")
    print("EM4 radii " + " ".join(f"g{p}={r.fmt()}" for p, r in enumerate(radii)))
    print(f"gamma_0   {gamma.fmt()}")
    print(f"gamma_1   {gamma1.fmt()}")
    print(f"gamma_2   {gamma2.fmt()}")
    print(f"gamma_3   {gamma3.fmt()}")
    print(f"g3 width  {fmt_scaled(gamma3.width())}")
    print(f"sigma_1   {sigma1.fmt()}")
    print(f"sigma_2   {sigma2.fmt()}")
    print(f"sigma_3   {sigma3.fmt()}")
    print(f"sigma_4   {sigma4.fmt()}")
    print(f"qw_1      {qw1.fmt()}")
    print(f"qw_2      {qw2.fmt()}")
    print(f"qw_3      {qw3.fmt()}")
    print(f"SH1' direct {sh1p_direct.fmt()}")
    print(f"SH1'=T3anti {sh1p_t3.fmt()}")

    shape_ok = logn.lo > 8 * S and all(em4_shape_gate(p, logn) for p in range(4))
    prior_ok = (
        sigma1.subset_of(n1_sigma1)
        and sigma2.subset_of(n1_sigma2)
        and sigma3.subset_of(n1_sigma3)
    )
    gate("N2-S4 exact t^4 derivation of sigma_4; no gamma*zeta(3) term", sigma4_derivation_gate())
    gate("N2-J3 exact SH-1' identity with the antisymmetric T_3 block determinant", third_junction_gate())
    gate("N2-EM4 common B4 tail shape proved for gamma_0..gamma_3", shape_ok)
    gate("N2-G3 fresh gamma_3 width <= 1e-17", gamma3.width() <= GAMMA3_MAX_WIDTH)
    gate("N2-OLD refreshed sigma_1..sigma_3 intervals lie inside the frozen N1 intervals", prior_ok)
    gate("N2-Q3 fresh qw_3 interval is strictly positive", qw3.positive())
    gate("N2-DIR direct shifted Hankel determinant interval is strictly positive", sh1p_direct.positive())
    gate("N2-T3 antisymmetric T_3 block determinant interval is strictly positive", sh1p_t3.positive())
    gate("N2-OVL direct and T_3-block determinant enclosures overlap", sh1p_direct.overlaps(sh1p_t3))

    print("FAILED: " + (", ".join(FAILED) if FAILED else "none"))
    print("VERDICT: " + ("PASS C-LI-Q-MOMENT-1 N2" if not FAILED else "FAIL C-LI-Q-MOMENT-1 N2"))
    print("NONCLAIM: reference calibration only; not full T_3 positivity; no J-native A_J/B_J or moment functional; no public promotion; RH remains open")
    return 1 if FAILED else 0


if __name__ == "__main__":
    raise SystemExit(main())
