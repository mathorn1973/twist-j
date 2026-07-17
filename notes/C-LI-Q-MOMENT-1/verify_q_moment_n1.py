#!/usr/bin/env python3
"""Pinned exact-interval N1 verifier for C-LI-Q-MOMENT-1.

This verifier refines the gamma_2 enclosure to the frozen width 1e-9 and
checks the exact determinant junction SH-1 = Q.  It uses outward-rounded
fixed-point integer intervals only.  No zero list, prime table, float,
Decimal, random input, network access, subprocess, or external package is
used.

The pin and action rules are in N1_SH1_PIN.md.  Passing this finite audit
creates no J-native realization and does not prove RH.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import sys


# Force byte-stable LF output on both Windows and POSIX Python.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", newline="\n", write_through=True)


S = 10**24
N = 200_000
LOG_TERMS = 32
GAMMA2_MAX_WIDTH = 10**15  # 1e-9 at scale 1e24.

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

    # Positive remainder bounded by
    # 2*y^(2K+1)/((2K+1)*(1-y^2)).
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
    # Machin: pi = 16 atan(1/5) - 4 atan(1/239).
    return (
        arctan_inv_bounds(5, 22).mul_int(16)
        - arctan_inv_bounds(239, 7).mul_int(4)
    )


def finite_sum_intervals(n: int) -> tuple[I, I, I, I]:
    """Return H_n, sum(log k/k), sum(log^2 k/k), sum(1/k^3)."""
    h_lo = h_hi = 0
    s1_lo = s1_hi = 0
    s2_lo = s2_hi = 0
    z3_lo = z3_hi = 0

    for k in range(1, n + 1):
        h_lo += S // k
        h_hi += ceil_div(S, k)

        logk = log_integer(k)
        s1_lo += logk.lo // k
        s1_hi += ceil_div(logk.hi, k)

        logk2 = logk.square()
        s2_lo += logk2.lo // k
        s2_hi += ceil_div(logk2.hi, k)

        cube = k**3
        z3_lo += S // cube
        z3_hi += ceil_div(S, cube)

    return (
        I(h_lo, h_hi),
        I(s1_lo, s1_hi),
        I(s2_lo, s2_hi),
        I(z3_lo, z3_hi),
    )


def gamma_interval(n: int, logn: I, harmonic: I) -> I:
    # 1/(2(n+1)) < H_n - log(n) - gamma < 1/(2n).
    upper_residual = I.from_fraction(Fraction(1, 2 * n))
    lower_residual = I.from_fraction(Fraction(1, 2 * (n + 1)))
    return I(
        harmonic.lo - logn.hi - upper_residual.hi,
        harmonic.hi - logn.lo - lower_residual.lo,
    )


def gamma1_convex_tail_interval(n: int, logn: I, sum_log_over_k: I) -> I:
    # Safe established enclosure for the first Stieltjes constant.
    a_n = sum_log_over_k - logn.square().div_int(2)
    f_n = logn.div_int(n)
    extra = (logn - I.exact_int(1)).div_int(6 * n * n)
    core = a_n - f_n.div_int(2)
    return I(core.lo, core.hi + extra.hi)


def gamma2_em2_interval(n: int, logn: I, sum_log2_over_k: I) -> tuple[I, I, I]:
    """B2 Euler--Maclaurin enclosure for the second Stieltjes constant.

    If core=A_n-f(n)/2 and B=-f'(n)/12>0, then
    gamma_2=core+B+R with |R|<=B, hence gamma_2 in [core,core+2B].
    Return gamma_2, B, and the f'' numerator used by the shape gate.
    """
    assert n >= 32 and logn.lo > 3 * S
    logn2 = logn.square()
    slope = logn2 - logn.mul_int(2)  # -n^2 f'(n), strictly positive.
    curvature = logn2 - logn.mul_int(3) + I.exact_int(1)
    assert slope.lo > 0 and curvature.lo > 0

    a_n = sum_log2_over_k - logn2.mul(logn).div_int(3)
    f_n = logn2.div_int(n)
    core = a_n - f_n.div_int(2)
    b2_term = slope.div_int(12 * n * n)
    gamma2 = I(core.lo, core.hi + 2 * b2_term.hi)
    return gamma2, b2_term, curvature


def zeta3_interval(n: int, partial_sum: I) -> I:
    lower_tail = I.from_fraction(Fraction(1, 2 * (n + 1) ** 2))
    upper_tail = I.from_fraction(Fraction(1, 2 * n**2))
    return I(
        partial_sum.lo + lower_tail.lo,
        partial_sum.hi + upper_tail.hi,
    )


def log_4pi_interval(pi: I) -> I:
    # pi/2 is in [1,2], and log(4pi)=3log(2)+log(pi/2).
    lo = log_unit_rational(pi.lo, 2 * S)
    hi = log_unit_rational(pi.hi, 2 * S)
    return LOG2.mul_int(3) + I(lo.lo, hi.hi)


Poly = dict[tuple[int, int, int], Fraction]


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
            m = tuple(x + y for x, y in zip(ma, mb))
            out[m] = out.get(m, Fraction(0)) + ca * cb
            if out[m] == 0:
                del out[m]
    return out


def bridge_identity_gate() -> bool:
    s1: Poly = {(1, 0, 0): Fraction(1)}
    s2: Poly = {(0, 1, 0): Fraction(1)}
    s3: Poly = {(0, 0, 1): Fraction(1)}

    qw1 = poly_add(poly_scale(s1, Fraction(2)), s2)
    qw2 = poly_add(
        poly_add(poly_scale(s1, Fraction(6)), poly_scale(s2, Fraction(3))),
        s3,
    )
    direct = poly_add(poly_mul(s1, qw2), poly_scale(poly_mul(qw1, qw1), Fraction(-1)))
    reduced = poly_add(
        poly_mul(s1, poly_add(poly_add(poly_scale(s1, Fraction(2)), s3), poly_scale(s2, Fraction(-1)))),
        poly_scale(poly_mul(s2, s2), Fraction(-1)),
    )
    expected: Poly = {
        (2, 0, 0): Fraction(2),
        (1, 1, 0): Fraction(-1),
        (1, 0, 1): Fraction(1),
        (0, 2, 0): Fraction(-1),
    }
    return direct == reduced == expected


def gate(name: str, condition: bool) -> None:
    print(("PASS " if condition else "FAIL ") + name)
    if not condition:
        FAILED.append(name)


def main() -> int:
    # Frozen comparator intervals, all represented exactly at scale 1e24.
    lambda1_pin = I(
        23095708964233559 * 10**6,
        23095708972138893 * 10**6,
    )
    m1_pin = I(
        37100438723459 * 10**6,
        37100843555683 * 10**6,
    )
    historical_gamma2 = I(
        -9690364105552333923998,
        -9690362736532310677668,
    )
    historical_q = I(
        1883563636456191,
        1989968490233267,
    )

    pi = pi_interval()
    logn = log_integer(N)
    harmonic, sum_log, sum_log2, zeta3_partial = finite_sum_intervals(N)
    gamma = gamma_interval(N, logn, harmonic)
    gamma1 = gamma1_convex_tail_interval(N, logn, sum_log)
    gamma2, b2_term, curvature = gamma2_em2_interval(N, logn, sum_log2)
    zeta3 = zeta3_interval(N, zeta3_partial)
    log4pi = log_4pi_interval(pi)

    one = I.exact_int(1)
    sigma1 = one + gamma.div_int(2) - log4pi.div_int(2)
    sigma2 = one + gamma.square() + gamma1.mul_int(2) - pi.square().div_int(8)
    sigma3 = (
        one
        + gamma.square().mul(gamma)
        + gamma.mul(gamma1).mul_int(3)
        + gamma2.mul_int(3).div_int(2)
        - zeta3.mul_int(7).div_int(8)
    )

    qw0 = sigma1
    qw1 = sigma1.mul_int(2) + sigma2
    qw2 = sigma1.mul_int(6) + sigma2.mul_int(3) + sigma3
    sh1_direct = qw0.mul(qw2) - qw1.square()
    sh1_reduced = (
        sigma1.mul(sigma1.mul_int(2) + sigma3 - sigma2)
        - sigma2.square()
    )

    print("C-LI-Q-MOMENT-1 N1 exact-interval verifier")
    print(f"scale=10^24  N={N}  log_terms={LOG_TERMS}")
    print(f"EM2 B2    {b2_term.fmt()}")
    print(f"gamma_2   {gamma2.fmt()}")
    print(f"g2 width  {fmt_scaled(gamma2.width())}")
    print(f"sigma_1   {sigma1.fmt()}")
    print(f"sigma_2   {sigma2.fmt()}")
    print(f"sigma_3   {sigma3.fmt()}")
    print(f"qw_0      {qw0.fmt()}")
    print(f"qw_1      {qw1.fmt()}")
    print(f"qw_2      {qw2.fmt()}")
    print(f"SH1 direct {sh1_direct.fmt()}")
    print(f"SH1=Q norm {sh1_reduced.fmt()}")

    shape_ok = (
        logn.lo > 3 * S
        and (logn.square() - logn.mul_int(2)).lo > 0
        and curvature.lo > 0
    )
    gate("N1-ALG exact SH-1 coefficient vector equals Q: (2,-1,1,-1)", bridge_identity_gate())
    gate("N1-EM2 B2 shape checks and gamma_2 width <= 1e-9", shape_ok and gamma2.width() <= GAMMA2_MAX_WIDTH)
    gate("N1-G2 fresh gamma_2 interval is contained in the historical pin", gamma2.subset_of(historical_gamma2))
    gate("N1-J0 fresh qw_0 interval is contained in the lambda_1 pin", qw0.subset_of(lambda1_pin))
    gate("N1-J1 fresh qw_1 interval is contained in the M_1 pin", qw1.subset_of(m1_pin))
    gate("N1-Q2 fresh qw_2 interval is strictly positive", qw2.positive())
    gate("N1-DIR direct SH-1 interval is strictly positive", sh1_direct.positive())
    gate("N1-RED reduced SH-1=Q interval is strictly positive", sh1_reduced.positive())
    gate("N1-OVL direct and reduced SH-1 enclosures overlap", sh1_direct.overlaps(sh1_reduced))
    gate("N1-XPIN fresh reduced SH-1=Q interval is contained in the historical Q pin", sh1_reduced.subset_of(historical_q))

    print("FAILED: " + (", ".join(FAILED) if FAILED else "none"))
    print("VERDICT: " + ("PASS C-LI-Q-MOMENT-1 N1" if not FAILED else "FAIL C-LI-Q-MOMENT-1 N1"))
    print("NONCLAIM: no J-native A_J/B_J or moment functional; no public promotion; RH remains open")
    return 1 if FAILED else 0


if __name__ == "__main__":
    raise SystemExit(main())
