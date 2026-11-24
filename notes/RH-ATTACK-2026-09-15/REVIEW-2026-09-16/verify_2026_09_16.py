#!/usr/bin/env python3
"""Exact checks for the 2026-09-16 RH attack addendum.

Standard library only. This proves a finite-support obstruction for target (29)
and exact polynomial identities for the shadow-cancellation model. It proves
neither RH nor its negation.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import lcm
import sys

K = 72
N = 144
TARGET = F(9, 2**23)
LOWER_LO = F(7601923, 10**9)
LOWER_HI = F(7601924, 10**9)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def solve_bareiss(a: list[list[int]], b: list[int]) -> list[F]:
    """Solve A x = b by fraction-free Bareiss elimination."""
    n = len(a)
    require(n > 0 and all(len(row) == n for row in a), "bad matrix shape")
    require(len(b) == n, "bad rhs shape")
    m = [row[:] + [rhs] for row, rhs in zip(a, b)]
    previous = 1
    for k in range(n - 1):
        if m[k][k] == 0:
            pivot_row = next((i for i in range(k + 1, n) if m[i][k] != 0), None)
            require(pivot_row is not None, "singular Gram matrix")
            m[k], m[pivot_row] = m[pivot_row], m[k]
        pivot = m[k][k]
        for i in range(k + 1, n):
            aik = m[i][k]
            for j in range(k + 1, n + 1):
                numerator = m[i][j] * pivot - aik * m[k][j]
                q, r = divmod(numerator, previous)
                require(r == 0, f"Bareiss non-exact division at ({i},{j})")
                m[i][j] = q
            m[i][k] = 0
        previous = pivot
    require(m[-1][-2] != 0, "singular Gram matrix")
    x = [F(0) for _ in range(n)]
    for i in range(n - 1, -1, -1):
        rhs = F(m[i][n]) - sum((F(m[i][j]) * x[j] for j in range(i + 1, n)), F(0))
        require(m[i][i] != 0, "zero diagonal in back substitution")
        x[i] = rhs / m[i][i]
    return x


def verify_finite_support_obstruction() -> None:
    # Replace w_n=1/(n(n+1)) by integer weights W_n=D*w_n.
    # The common positive factor D cancels from the least-squares minimizer.
    d = lcm(*range(1, N + 2))
    weights = [d // (n * (n + 1)) for n in range(1, N + 1)]
    rows = [[n % k for k in range(2, K + 1)] for n in range(1, N + 1)]
    dim = K - 1
    gram = [
        [sum(w * row[i] * row[j] for w, row in zip(weights, rows)) for j in range(dim)]
        for i in range(dim)
    ]
    rhs = [sum(w * row[i] for w, row in zip(weights, rows)) for i in range(dim)]
    coeff = solve_bareiss(gram, rhs)

    # Exact minimum over real coefficients for the first N terms:
    # min ||1-Rc||_W^2 = <1,1>_W - b^T G^{-1} b.
    one_norm = F(sum(weights))
    projection = sum((F(v) * c for v, c in zip(rhs, coeff)), F(0))
    minimum = (one_norm - projection) / d
    require(minimum > 0, "non-positive finite minimum")
    require(LOWER_LO < minimum < LOWER_HI, "unexpected exact lower enclosure")
    require(minimum > 7000 * TARGET, "finite obstruction does not clear target")

    print("PASS: exact 71x71 weighted Gram system solved by stdlib Bareiss elimination.")
    print("PASS: 7601923/10^9 < min_{span_R{r_2,...,r_72}} E_144 < 7601924/10^9.")
    print("PASS: finite minimum > 7000 * (9/2^23).")
    print("CONCLUSION: no real, rational, or complex q in span{r_2,...,r_72} can satisfy target (29).")


def trim(p: list[F]) -> list[F]:
    q = p[:]
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return q


def add(p: list[F], q: list[F]) -> list[F]:
    out = [F(0)] * max(len(p), len(q))
    for i, value in enumerate(p):
        out[i] += value
    for i, value in enumerate(q):
        out[i] += value
    return trim(out)


def scale(p: list[F], a: F) -> list[F]:
    return trim([a * value for value in p])


def mul(p: list[F], q: list[F]) -> list[F]:
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def compose_linear(p: list[F], a: F, b: F) -> list[F]:
    out = [F(0)]
    for c in reversed(p):
        out = add(mul(out, [b, a]), [c])
    return trim(out)


def evaluate(p: list[F], s: F) -> F:
    out = F(0)
    for c in reversed(p):
        out = out * s + c
    return out


def verify_shadow_model() -> None:
    eps = F(1, 4)
    s = [F(0), F(1)]
    p = [F(1)]
    for beta in (F(1, 4), F(1, 2), F(3, 4)):
        p = mul(p, [beta * beta + 1, -2 * beta, F(1)])
    require(compose_linear(p, F(-1), F(1)) == p, "reflection symmetry failed")
    base = [F(1), F(0), F(1)]
    top = [F(25, 16), F(-3, 2), F(1)]
    require(mul(p, base) == mul(compose_linear(p, F(1), eps), top), "shift cancellation failed")
    c = eps * evaluate(p, F(1)) / evaluate(p, F(1) + eps)
    require(c == F(17, 128), "wrong normalized residue")
    left = add(scale(mul(s, base), c), scale(mul([F(-3, 4), F(1)], top), F(-1)))
    right = mul([F(-1), F(1)], [F(-150, 128), F(177, 128), F(-111, 128)])
    require(left == right, "regularized quotient identity failed")
    print("PASS: shadow model reflection, shift cancellation, residue and regularization identities.")
    print("MODEL ONLY: Z(s)=P(s)/(P(1)*(s-1)) is not the Riemann zeta function.")


def main() -> int:
    try:
        verify_finite_support_obstruction()
        verify_shadow_model()
    except (ArithmeticError, AssertionError, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("ALL CHECKS PASS. NON-CANONICAL; no RH status change; one local architecture.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
