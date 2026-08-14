#!/usr/bin/env python3
"""Target-free exact self-tests for the proposed rigidity CAS workflow.

Only artificial toy ideals are used.  The program deliberately depends only
on Python's standard library.  It checks the algebraic identities behind the
Rabinowitsch saturation/radical tests, the unit-circle trace reduction, exact
Sturm isolation, and a small modular good-prime screen.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple


NAMES = ("a", "b", "s", "x", "y", "z", "t", "r")
N = len(NAMES)
Monomial = Tuple[int, ...]


@dataclass(frozen=True)
class Poly:
    terms: Mapping[Monomial, Fraction]

    def __post_init__(self) -> None:
        clean = {m: Fraction(c) for m, c in self.terms.items() if c}
        object.__setattr__(self, "terms", clean)

    @staticmethod
    def constant(c: int | Fraction) -> "Poly":
        c = Fraction(c)
        return Poly({(0,) * N: c}) if c else Poly({})

    @staticmethod
    def variable(index: int) -> "Poly":
        m = [0] * N
        m[index] = 1
        return Poly({tuple(m): Fraction(1)})

    def __add__(self, other: "Poly" | int) -> "Poly":
        other = as_poly(other)
        out: Dict[Monomial, Fraction] = dict(self.terms)
        for m, c in other.terms.items():
            out[m] = out.get(m, Fraction(0)) + c
        return Poly(out)

    def __radd__(self, other: "Poly" | int) -> "Poly":
        return self + other

    def __neg__(self) -> "Poly":
        return Poly({m: -c for m, c in self.terms.items()})

    def __sub__(self, other: "Poly" | int) -> "Poly":
        return self + (-as_poly(other))

    def __rsub__(self, other: "Poly" | int) -> "Poly":
        return as_poly(other) - self

    def __mul__(self, other: "Poly" | int) -> "Poly":
        other = as_poly(other)
        out: Dict[Monomial, Fraction] = {}
        for m1, c1 in self.terms.items():
            for m2, c2 in other.terms.items():
                m = tuple(i + j for i, j in zip(m1, m2))
                out[m] = out.get(m, Fraction(0)) + c1 * c2
        return Poly(out)

    def __rmul__(self, other: "Poly" | int) -> "Poly":
        return self * other

    def __pow__(self, exponent: int) -> "Poly":
        if exponent < 0:
            raise ValueError("ordinary polynomial exponent must be nonnegative")
        result = Poly.constant(1)
        base = self
        n = exponent
        while n:
            if n & 1:
                result = result * base
            base = base * base
            n >>= 1
        return result


def as_poly(value: Poly | int | Fraction) -> Poly:
    return value if isinstance(value, Poly) else Poly.constant(value)


a, b, sat, x, y, z, rab, r = (Poly.variable(i) for i in range(N))


def quotient_xy_normal_form(poly: Poly) -> Poly:
    """Normal form modulo xy-1, sufficient for a toy identity check."""
    out: Dict[Monomial, Fraction] = {}
    ix, iy = NAMES.index("x"), NAMES.index("y")
    for m0, coeff in poly.terms.items():
        m = list(m0)
        cancel = min(m[ix], m[iy])
        m[ix] -= cancel
        m[iy] -= cancel
        mt = tuple(m)
        out[mt] = out.get(mt, Fraction(0)) + coeff
    return Poly(out)


def trim(p: Sequence[Fraction]) -> List[Fraction]:
    q = list(p)
    while q and q[-1] == 0:
        q.pop()
    return q


def derivative(p: Sequence[Fraction]) -> List[Fraction]:
    return trim([Fraction(i) * p[i] for i in range(1, len(p))])


def divrem(p: Sequence[Fraction], q: Sequence[Fraction]) -> Tuple[List[Fraction], List[Fraction]]:
    p = trim(p)
    q = trim(q)
    if not q:
        raise ZeroDivisionError
    quotient = [Fraction(0)] * max(1, len(p) - len(q) + 1)
    remainder = p[:]
    while remainder and len(remainder) >= len(q):
        shift = len(remainder) - len(q)
        coeff = remainder[-1] / q[-1]
        quotient[shift] += coeff
        for i, qi in enumerate(q):
            remainder[i + shift] -= coeff * qi
        remainder = trim(remainder)
    return trim(quotient), remainder


def sturm_sequence(p: Sequence[Fraction]) -> List[List[Fraction]]:
    seq = [trim(p), derivative(p)]
    while seq[-1]:
        _, rem = divrem(seq[-2], seq[-1])
        if not rem:
            break
        seq.append([-c for c in rem])
    return seq


def eval_univariate(p: Sequence[Fraction], q: Fraction) -> Fraction:
    value = Fraction(0)
    for coeff in reversed(p):
        value = value * q + coeff
    return value


def sign(value: Fraction) -> int:
    return (value > 0) - (value < 0)


def variations_at(seq: Sequence[Sequence[Fraction]], q: Fraction) -> int:
    signs = [sign(eval_univariate(p, q)) for p in seq]
    signs = [s for s in signs if s]
    return sum(s1 != s2 for s1, s2 in zip(signs, signs[1:]))


def roots_in(seq: Sequence[Sequence[Fraction]], left: Fraction, right: Fraction) -> int:
    return variations_at(seq, left) - variations_at(seq, right)


def mod_trim(p: Sequence[int], prime: int) -> List[int]:
    q = [v % prime for v in p]
    while q and q[-1] == 0:
        q.pop()
    return q


def mod_divrem(p: Sequence[int], q: Sequence[int], prime: int) -> Tuple[List[int], List[int]]:
    p = mod_trim(p, prime)
    q = mod_trim(q, prime)
    if not q:
        raise ZeroDivisionError
    quotient = [0] * max(1, len(p) - len(q) + 1)
    remainder = p[:]
    qlead_inv = pow(q[-1], -1, prime)
    while remainder and len(remainder) >= len(q):
        shift = len(remainder) - len(q)
        coeff = remainder[-1] * qlead_inv % prime
        quotient[shift] = (quotient[shift] + coeff) % prime
        for i, qi in enumerate(q):
            remainder[i + shift] = (remainder[i + shift] - coeff * qi) % prime
        remainder = mod_trim(remainder, prime)
    return mod_trim(quotient, prime), remainder


def mod_gcd(p: Sequence[int], q: Sequence[int], prime: int) -> List[int]:
    p, q = mod_trim(p, prime), mod_trim(q, prime)
    while q:
        _, rem = mod_divrem(p, q, prime)
        p, q = q, rem
    if not p:
        return []
    inv = pow(p[-1], -1, prime)
    return [(v * inv) % prime for v in p]


def run() -> None:
    checks: List[Tuple[str, bool, str]] = []

    # Toy ideal <xy-1, x+y>: x^2+1 has an explicit membership certificate.
    q_xy = x * y - 1
    q_sum = x + y
    phase_target = x**2 + 1
    identity = x * q_sum - q_xy
    checks.append(("ordinary ideal membership identity", identity == phase_target,
                   "x(x+y)-(xy-1)=x^2+1"))

    # Toy saturation <ab> : a^infinity.  Rabinowitsch adds 1-sa.
    sat_identity = sat * (a * b) + b * (1 - sat * a)
    checks.append(("Rabinowitsch saturation identity", sat_identity == b,
                   "s(ab)+b(1-sa)=b"))

    # Toy radical: z belongs to sqrt(<z^2>) because the augmented ideal is 1.
    radical_identity = (1 - rab * z) * (1 + rab * z) + rab**2 * z**2
    checks.append(("Rabinowitsch radical identity", radical_identity == Poly.constant(1),
                   "(1-tz)(1+tz)+t^2 z^2=1"))

    # On xy=1, Phi_20(x)/x^4 equals T^4-5T^2+5 for T=x+y.
    phi20 = x**8 - x**6 + x**4 - x**2 + 1
    trace_poly_lift = x**4 * ((x + y) ** 4 - 5 * (x + y) ** 2 + 5)
    trace_diff_nf = quotient_xy_normal_form(trace_poly_lift - phi20)
    checks.append(("unit-circle trace reduction", not trace_diff_nf.terms,
                   "Phi20=x^4((x+y)^4-5(x+y)^2+5) modulo xy-1"))

    # Exact Sturm isolation for the golden-ratio toy polynomial.
    golden = [Fraction(-1), Fraction(-1), Fraction(1)]
    golden_sturm = sturm_sequence(golden)
    golden_counts = (roots_in(golden_sturm, Fraction(-1), Fraction(0)),
                     roots_in(golden_sturm, Fraction(1), Fraction(2)))
    checks.append(("Sturm isolation r^2-r-1", golden_counts == (1, 1),
                   f"root counts (-1,0),(1,2)={golden_counts}"))

    # Exact Sturm isolation for the phase trace polynomial.
    phase_trace = [Fraction(5), Fraction(0), Fraction(-5), Fraction(0), Fraction(1)]
    phase_sturm = sturm_sequence(phase_trace)
    intervals = [(-2, Fraction(-3, 2)), (Fraction(-3, 2), -1),
                 (1, Fraction(3, 2)), (Fraction(3, 2), 2)]
    phase_counts = tuple(roots_in(phase_sturm, Fraction(lo), Fraction(hi))
                         for lo, hi in intervals)
    checks.append(("Sturm isolation T^4-5T^2+5", phase_counts == (1, 1, 1, 1),
                   f"four rational interval counts={phase_counts}"))

    # Toy good-prime screen: discriminant 5 is the only squarefreeness obstruction.
    modular = []
    deriv = [-1, 2]
    for prime in (7, 11, 13):
        gcd = mod_gcd([-1, -1, 1], deriv, prime)
        modular.append((prime, gcd))
    modular_ok = all(gcd == [1] for _, gcd in modular)
    checks.append(("modular squarefree good-prime screen", modular_ok,
                   f"gcd(f,f') over F_p={modular}"))

    for name, ok, detail in checks:
        print(f"{'PASS' if ok else 'FAIL'}  {name}: {detail}")
    print(f"SUMMARY {sum(ok for _, ok, _ in checks)}/{len(checks)} PASS")
    if not all(ok for _, ok, _ in checks):
        raise SystemExit(1)


if __name__ == "__main__":
    run()
