#!/usr/bin/env python3
"""Exact-interval incubation verifier for sigma_3, lambda_3, and T_2.

No zero list, prime table, floating-point arithmetic, network access, random
input, or external package is used.  Every numerical assertion is made with
outward-rounded fixed-point integer intervals.  The analytic formulas and
tail lemmas are documented in LAMBDA3_T2.md.

Incubation only.  This execution does not create a public Canon claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


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

    def fmt(self, digits: int = 24) -> str:
        def one(v: int) -> str:
            sign = "-" if v < 0 else ""
            v = abs(v)
            whole, frac = divmod(v, S)
            body = f"{whole}.{frac:024d}"
            return sign + body[: len(str(whole)) + 1 + digits]

        return f"[{one(self.lo)}, {one(self.hi)}]"


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
    # For f(x)=log(x)/x and n>=5:
    # A_n-f(n)/2 <= gamma_1
    # <= A_n-f(n)/2+(log(n)-1)/(8n^2).
    # The larger 1/(6n^2) correction preserves the established lambda_2 pin.
    a_n = sum_log_over_k - logn.square().div_int(2)
    f_n = logn.div_int(n)
    extra = (logn - I.exact_int(1)).div_int(6 * n * n)
    core = a_n - f_n.div_int(2)
    return I(core.lo, core.hi + extra.hi)


def gamma2_convex_tail_interval(n: int, logn: I, sum_log2_over_k: I) -> I:
    # For f(x)=log^2(x)/x, log(n)>3 makes f decreasing and convex.
    # If A_n=sum_{k<=n}f(k)-log^3(n)/3, the trapezoid Peano kernel gives
    #
    # A_n-f(n)/2 <= gamma_2
    # <= A_n-f(n)/2+(log^2(n)-2log(n))/(8n^2).
    assert n >= 32 and logn.lo > 3 * S
    logn2 = logn.square()
    a_n = sum_log2_over_k - logn2.mul(logn).div_int(3)
    f_n = logn2.div_int(n)
    slope = logn2 - logn.mul_int(2)
    assert slope.lo > 0
    extra = slope.div_int(8 * n * n)
    core = a_n - f_n.div_int(2)
    return I(core.lo, core.hi + extra.hi)


def zeta3_interval(n: int, partial_sum: I) -> I:
    # Integral comparison for the positive decreasing x^(-3) tail.
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


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + name + (("  " + detail) if detail else ""))
    if not ok:
        raise AssertionError(name)


def formula_vector_gate() -> bool:
    """Exact rational guard for lambda_3=3 sigma_1-3 sigma_2+sigma_3.

    Basis: 1, gamma, gamma^2, gamma^3, gamma_1, gamma*gamma_1,
    gamma_2, pi^2, zeta(3), log(4pi).
    """
    q = Fraction
    sigma1 = (q(1), q(1, 2), q(0), q(0), q(0), q(0), q(0), q(0), q(0), q(-1, 2))
    sigma2 = (q(1), q(0), q(1), q(0), q(2), q(0), q(0), q(-1, 8), q(0), q(0))
    sigma3 = (q(1), q(0), q(0), q(1), q(0), q(3), q(3, 2), q(0), q(-7, 8), q(0))
    derived = tuple(3 * a - 3 * b + c for a, b, c in zip(sigma1, sigma2, sigma3))
    expected = (q(1), q(3, 2), q(-3), q(1), q(-6), q(3), q(3, 2), q(3, 8), q(-7, 8), q(-3, 2))
    return derived == expected


def main() -> int:
    print("C-J-LI-LAMBDA3-T2 incubation verifier")
    print(f"scale=10^24  N={N}  log_terms={LOG_TERMS}")

    pi = pi_interval()
    logn = log_integer(N)
    harmonic, sum_log, sum_log2, zeta3_partial = finite_sum_intervals(N)
    gamma = gamma_interval(N, logn, harmonic)
    gamma1 = gamma1_convex_tail_interval(N, logn, sum_log)
    gamma2 = gamma2_convex_tail_interval(N, logn, sum_log2)
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
    lambda3 = sigma1.mul_int(3) - sigma2.mul_int(3) + sigma3

    c0 = sigma1.mul_int(2)
    c1 = -sigma2
    c2 = sigma3 - sigma2
    anti = c0 - c2
    q_invariant = (
        sigma1.mul(sigma1.mul_int(2) + sigma3 - sigma2)
        - sigma2.square()
    )
    minor01 = c0.square() - c1.square()
    minor02 = c0.square() - c2.square()
    det_t2 = anti.mul(q_invariant).mul_int(2)
    det_k3 = anti.mul(q_invariant).div_int(4)

    print(f"gamma_2  {gamma2.fmt()}")
    print(f"zeta(3)  {zeta3.fmt()}")
    print(f"sigma_3  {sigma3.fmt()}")
    print(f"lambda_3 {lambda3.fmt()}")
    print(f"c_0      {c0.fmt()}")
    print(f"c_1      {c1.fmt()}")
    print(f"c_2      {c2.fmt()}")
    print(f"c0-c2    {anti.fmt()}")
    print(f"Q        {q_invariant.fmt()}")
    print(f"M01      {minor01.fmt()}")
    print(f"M02      {minor02.fmt()}")
    print(f"det T_2  {det_t2.fmt()}")
    print(f"det K_3  {det_k3.fmt()}")

    gate("L1 exact lambda_3 coefficient vector", formula_vector_gate())
    gate("L2 gamma_2 interval is strictly negative", gamma2.negative())
    gate("L3 sigma_3 interval is strictly negative", sigma3.negative())
    gate("L4 lambda_3 interval is strictly positive", lambda3.positive())
    gate("L5 c_0 is strictly positive", c0.positive())
    gate("L6 antisymmetric eigenvalue c_0-c_2 is positive", anti.positive())
    gate("L7 symmetric-block invariant Q is positive", q_invariant.positive())
    gate("L8 adjacent principal 2x2 minor is positive", minor01.positive())
    gate("L9 nonadjacent principal 2x2 minor is positive", minor02.positive())
    gate("L10 det(T_2) is strictly positive", det_t2.positive())
    gate("L11 det(K_3) is strictly positive", det_k3.positive())

    print("VERDICT: PASS incubation Li positivity gate at T_2 / K_3")
    print("STATUS: CANDIDATE-C, single architecture; RH untouched")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
