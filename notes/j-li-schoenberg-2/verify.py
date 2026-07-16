#!/usr/bin/env python3
"""
C-J-LI-SCHOENBERG-2 candidate verifier.

Purpose
-------
Test the first nontrivial joint positivity condition forced by any
Schoenberg/Herglotz realization of the Riemann Li coefficients:

    K_2 = [[lambda_1, lambda_2/2],
           [lambda_2/2, lambda_2]] >= 0.

Equivalently, with lambda_1, lambda_2 > 0,

    4 lambda_1 - lambda_2 > 0.

No zero list and no prime table are used.  The constants are enclosed by
fixed-point integer interval arithmetic.  gamma_1 is bounded by a convex-trapezoid tail estimate for the
elementary A_N limit.

Candidate grade only.  One architecture in this workspace.  No Canon status.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
from pathlib import Path

S = 10**24
N = 100_000
LOG_TERMS = 32


def floor_frac(q: Fraction) -> int:
    return q.numerator * S // q.denominator


def ceil_frac(q: Fraction) -> int:
    return -((-q.numerator * S) // q.denominator)


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


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
            return I((self.lo * self.lo) // S,
                     ceil_div(self.hi * self.hi, S))
        if self.hi <= 0:
            return I((self.hi * self.hi) // S,
                     ceil_div(self.lo * self.lo, S))
        return I(0, ceil_div(max(self.lo * self.lo, self.hi * self.hi), S))

    def positive(self) -> bool:
        return self.lo > 0

    def negative(self) -> bool:
        return self.hi < 0

    def fmt(self, digits: int = 24) -> str:
        def one(v: int) -> str:
            sign = "-" if v < 0 else ""
            v = abs(v)
            whole, frac = divmod(v, S)
            return f"{sign}{whole}.{frac:024d}"[:len(sign) + len(str(whole)) + 1 + digits]
        return f"[{one(self.lo)}, {one(self.hi)}]"


def log_unit_rational(num: int, den: int, terms: int = LOG_TERMS) -> I:
    """Rigorous log(num/den) for 1 <= num/den <= 2 by atanh series."""
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
        d = bp * odd
        lo_sum += (S * ap) // d
        hi_sum += ceil_div(S * ap, d)
        ap *= a2
        bp *= b2

    # Remaining positive tail:
    # 2 * y^(2K+1) / ((2K+1) * (1-y^2)).
    p = 2 * terms + 1
    tail_num = 2 * pow(a, p) * b2
    tail_den = p * pow(b, p) * (b2 - a2)
    tail_hi = ceil_div(S * tail_num, tail_den)

    return I(2 * lo_sum, 2 * hi_sum + tail_hi)


LOG2 = log_unit_rational(2, 1)


def log_integer(k: int) -> I:
    assert k >= 1
    m = k.bit_length() - 1
    base = 1 << m
    return LOG2.mul_int(m) + log_unit_rational(k, base)


def arctan_inv_bounds(q: int, terms: int) -> I:
    """Alternating-series enclosure of arctan(1/q)."""
    partials: list[Fraction] = [Fraction(0)]
    s = Fraction(0)
    for k in range(terms + 1):
        t = Fraction(1, (2 * k + 1) * pow(q, 2 * k + 1))
        s = s + t if k % 2 == 0 else s - t
        partials.append(s)
    a = partials[terms]
    b = partials[terms + 1]
    lo, hi = (a, b) if a <= b else (b, a)
    return I(floor_frac(lo), ceil_frac(hi))


def pi_interval() -> I:
    # Machin: pi = 16 atan(1/5) - 4 atan(1/239).
    a = arctan_inv_bounds(5, 22)
    b = arctan_inv_bounds(239, 7)
    return a.mul_int(16) - b.mul_int(4)


def harmonic_interval(n: int) -> I:
    lo = 0
    hi = 0
    for k in range(1, n + 1):
        lo += S // k
        hi += ceil_div(S, k)
    return I(lo, hi)


def sum_log_over_k_interval(n: int) -> I:
    lo = 0
    hi = 0
    for k in range(1, n + 1):
        lk = log_integer(k)
        lo += lk.lo // k
        hi += ceil_div(lk.hi, k)
    return I(lo, hi)


def gamma_interval(n: int, logn: I, hn: I) -> I:
    # 1/(2(n+1)) < H_n - log n - gamma < 1/(2n).
    lower_correction = I.from_fraction(Fraction(1, 2 * n))
    upper_correction = I.from_fraction(Fraction(1, 2 * (n + 1)))
    return I(hn.lo - logn.hi - lower_correction.hi,
             hn.hi - logn.lo - upper_correction.lo)


def gamma1_convex_tail_interval(n: int, logn: I, slog: I) -> I:
    # A_n = sum_{k<=n} log(k)/k - log(n)^2/2.
    # Let f(x)=log(x)/x.  For n>=5, f is decreasing and convex on
    # [n,infinity).  Writing T_n=A_n-gamma_1 as the sum over unit
    # intervals of integral(f)-right_endpoint(f), one has
    #
    #   T_n = f(n)/2 - sum E_k,
    #
    # where E_k is the trapezoid error.  Convexity gives E_k>=0.
    # The Peano-kernel identity and max ((x-a)(b-x)/2)=1/8 give
    #
    #   sum E_k <= (f'(infinity)-f'(n))/8
    #             = (log n - 1)/(8 n^2).
    #
    # Therefore
    #   A_n-f(n)/2 <= gamma_1
    #     <= A_n-f(n)/2 + (log n-1)/(8n^2).
    # We deliberately use the looser denominator 6, so all endpoint
    # rounding remains outward and the interval is still rigorous.
    a_n = slog - logn.square().div_int(2)
    f_n = logn.div_int(n)
    h = logn - I.exact_int(1)
    extra = h.div_int(6 * n * n)
    core = a_n - f_n.div_int(2)
    return I(core.lo, core.hi + extra.hi)


def log_4pi_interval(pi: I) -> I:
    # pi/2 lies in [1,2].  Monotonicity plus rational endpoint bounds.
    lo_r = log_unit_rational(pi.lo, 2 * S)
    hi_r = log_unit_rational(pi.hi, 2 * S)
    log_pi_over_2 = I(lo_r.lo, hi_r.hi)
    return LOG2.mul_int(3) + log_pi_over_2


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + name + (("  " + detail) if detail else ""))
    if not ok:
        raise AssertionError(name)


def main() -> int:
    print("C-J-LI-SCHOENBERG-2 candidate verifier")
    print(f"scale=10^24  N={N}  log_terms={LOG_TERMS}")

    pi = pi_interval()
    logn = log_integer(N)
    hn = harmonic_interval(N)
    slog = sum_log_over_k_interval(N)
    gamma = gamma_interval(N, logn, hn)
    gamma1 = gamma1_convex_tail_interval(N, logn, slog)
    log4pi = log_4pi_interval(pi)

    one = I.exact_int(1)
    eight = 8

    lambda1 = one + gamma.div_int(2) - log4pi.div_int(2)
    lambda2 = (one + gamma - gamma.square()
               - gamma1.mul_int(2)
               + pi.square().div_int(eight)
               - log4pi)
    delta = lambda1.mul_int(4) - lambda2
    det_k2 = lambda2.mul(delta).div_int(4)

    print(f"pi       {pi.fmt()}")
    print(f"gamma    {gamma.fmt()}")
    print(f"gamma_1  {gamma1.fmt()}")
    print(f"log(4pi) {log4pi.fmt()}")
    print(f"lambda_1 {lambda1.fmt()}")
    print(f"lambda_2 {lambda2.fmt()}")
    print(f"4l1-l2   {delta.fmt()}")
    print(f"det K_2  {det_k2.fmt()}")

    gate("S1 gamma_1 interval is strictly negative", gamma1.negative())
    gate("S2 lambda_1 is strictly positive", lambda1.positive())
    gate("S3 lambda_2 is strictly positive", lambda2.positive())
    gate("S4 4 lambda_1 - lambda_2 is strictly positive", delta.positive())
    gate("S5 Schoenberg K_2 determinant is strictly positive", det_k2.positive())

    # Negative control: the old AM6 interval alone cannot prove S4.
    old_l1 = I(23095708964233559 * 10**6, 23095708972138893 * 10**6)
    old_l2 = I(92230606084387762 * 10**6, 92460864725386214 * 10**6)
    old_delta = old_l1.mul_int(4) - old_l2
    gate("NC old lambda intervals are inconclusive for S4",
         old_delta.lo < 0 < old_delta.hi,
         old_delta.fmt())

    print("VERDICT: PASS candidate joint Li positivity gate at N=2")
    print("STATUS: CANDIDATE-C, single architecture; RH untouched")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
