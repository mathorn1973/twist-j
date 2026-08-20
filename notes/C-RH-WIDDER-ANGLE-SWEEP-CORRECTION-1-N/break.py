#!/usr/bin/env python3
"""Independent exact breaker for C-RH-WIDDER-ANGLE-SWEEP-CORRECTION-1-N.

Frozen before the positive proof and verifier. Python standard library only.
No float, no external data, no actual zeta zero. Rational synthetic controls.

Return codes:
  0  breaker clean
  1  integrity stop (not emitted by this mathematical script)
  2  mathematical disagreement
"""

from __future__ import annotations

from fractions import Fraction as Q
from math import factorial

C = tuple[Q, Q]


def c(re: int | Q = 0, im: int | Q = 0) -> C:
    return (Q(re), Q(im))


def c_add(x: C, y: C) -> C:
    return (x[0] + y[0], x[1] + y[1])


def c_mul(x: C, y: C) -> C:
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def c_conj(x: C) -> C:
    return (x[0], -x[1])


def c_abs2(x: C) -> Q:
    return x[0] * x[0] + x[1] * x[1]


def c_pow(x: C, n: int) -> C:
    result = c(1)
    base = x
    exponent = n
    while exponent:
        if exponent & 1:
            result = c_mul(result, base)
        base = c_mul(base, base)
        exponent >>= 1
    return result


def c_div(x: C, y: C) -> C:
    den = c_abs2(y)
    num = c_mul(x, c_conj(y))
    return (num[0] / den, num[1] / den)


def pair_term(k: int, A: Q, B: Q, u: Q) -> Q:
    """Conjugate-pair contribution to W_k."""
    ratio = c_div(c_pow(c(A, -B), k), c_pow(c(u + A, -B), 2 * k))
    return 2 * Q(factorial(2 * k - 1)) * ratio[0]


def first_negative_power(A: Q, B: Q, cap: int = 10000) -> int | None:
    if B == 0:
        return None
    acc = c(1)
    base = c(A, -B)
    for k in range(1, cap + 1):
        acc = c_mul(acc, base)
        if acc[0] < 0:
            return k
    return None


def z_from_rho(beta: Q, gamma: Q) -> tuple[Q, Q]:
    A = gamma * gamma + beta * (1 - beta)
    B = abs(gamma * (2 * beta - 1))
    return A, B


findings: list[str] = []
checks = 0


def gate(name: str, condition: bool, detail: str = "") -> None:
    global checks
    checks += 1
    if condition:
        print(f"{name} PASS{(': ' + detail) if detail else ''}")
    else:
        findings.append(name)
        print(f"{name} FAIL{(': ' + detail) if detail else ''}")


print("C-RH-WIDDER-ANGLE-SWEEP-CORRECTION-1-N independent breaker")

# B1. Frozen arbitrary-level endpoint counterexample.
A = Q(1)
B = Q(1)
u = Q(1, 2)
endpoint = c_pow(c(A, -B), 8)[0]
actual = pair_term(8, A, B, u)
expected_actual = Q(
    -172056926056081143103488000,
    51185893014090757,
)
gate(
    "B1 arbitrary-level endpoint criterion is false",
    endpoint == 16 and actual == expected_actual and actual < 0,
    f"endpoint={endpoint} pair_sign={'negative' if actual < 0 else 'nonnegative'}",
)

# B2. Resonance: A=B gives theta=pi/4. Level 2 stays positive on all
# sampled rational u; level 3 has an exact negative witness.
ugrid = (
    Q(1, 1000),
    Q(1, 100),
    Q(1, 10),
    Q(1, 2),
    Q(1),
    Q(2),
    Q(10),
    Q(100),
    Q(1000),
)
level2_positive = all(pair_term(2, A, B, x) > 0 for x in ugrid)
level3_negative = any(pair_term(3, A, B, x) < 0 for x in ugrid)
gate(
    "B2 resonance rejects ceil and gives first failure 3",
    first_negative_power(A, B) == 3 and level2_positive and level3_negative,
)

# B3. Owner depths survive the correction.
A_low, B_low = z_from_rho(Q(9, 10), Q(1, 2))
A_high, B_high = z_from_rho(Q(3, 4), Q(10))
gate(
    "B3 owner depths remain 2 and 32",
    first_negative_power(A_low, B_low) == 2
    and first_negative_power(A_high, B_high) == 32,
)

# B4. Below the first negative power, no sampled u may be negative.
below_ok = True
controls = (
    (Q(17, 50), Q(2, 5)),
    (Q(1603, 16), Q(5)),
    (Q(1), Q(1)),
    (Q(5), Q(2)),
    (Q(13), Q(3)),
)
for a, b in controls:
    first = first_negative_power(a, b, 512)
    if first is None:
        continue
    for k in range(1, first):
        below_ok = below_ok and all(pair_term(k, a, b, x) > 0 for x in ugrid)
gate("B4 no sampled negativity below first negative power", below_ok)

# B5. Corrected arbitrary-level integer criterion. A sampled negative at
# level k requires that some power j<=k already has negative real part.
criterion_ok = True
extra_counterexamples = 0
for a in (Q(1), Q(2), Q(3), Q(5)):
    for b in (Q(1), Q(2), Q(3), Q(5)):
        first = first_negative_power(a, b, 512)
        for k in range(1, 33):
            sampled_negative = any(pair_term(k, a, b, x) < 0 for x in ugrid)
            prior_negative = first is not None and first <= k
            if sampled_negative and not prior_negative:
                criterion_ok = False
            endpoint_nonnegative = c_pow(c(a, -b), k)[0] >= 0
            if sampled_negative and endpoint_nonnegative:
                extra_counterexamples += 1
gate(
    "B5 corrected integer criterion survives sampled attack",
    criterion_ok and extra_counterexamples > 0,
    f"later-level endpoint counterexamples={extra_counterexamples}",
)

# B6. Finite-prefix family. Exact bound B/A < 1/(2N), plus sampled
# positivity for every k<=N on N=1..64.
prefix_ok = True
prefix_checks = 0
for N in range(1, 65):
    a = Q(N * N) + Q(3, 16)
    b = Q(N, 2)
    prefix_ok = prefix_ok and b / a < Q(1, 2 * N)
    for k in range(1, N + 1):
        prefix_checks += 1
        prefix_ok = prefix_ok and all(pair_term(k, a, b, x) > 0 for x in ugrid)
gate(
    "B6 finite-prefix family N=1..64",
    prefix_ok,
    f"exact sampled levels={prefix_checks}",
)

# B7. The low off-line control refutes a termwise W1 -> W2 implication.
transition_ok = (
    all(pair_term(1, A_low, B_low, x) > 0 for x in ugrid)
    and any(pair_term(2, A_low, B_low, x) < 0 for x in ugrid)
)
gate("B7 termwise adjacent-level implication is false", transition_ok)

# B8. W2 safe geometry for strip controls with |gamma|>=1.
w2_ok = True
for beta in (Q(1, 100), Q(1, 3), Q(1, 2), Q(3, 4), Q(99, 100)):
    for gamma in (Q(1), Q(2), Q(5), Q(14), Q(1000)):
        a, b = z_from_rho(beta, gamma)
        w2_ok = w2_ok and b < a
        w2_ok = w2_ok and all(pair_term(2, a, b, x) > 0 for x in ugrid)
gate("B8 W2 strip controls are strictly positive", w2_ok)

# B9. Safe-depth algebraic ratio bound B/A < 1/H at gamma>=H.
safe_ok = True
for H in (Q(1), Q(2), Q(10), Q(100), Q(10**6)):
    for beta in (Q(1, 100), Q(1, 3), Q(3, 4), Q(99, 100)):
        for gamma in (H, H + 1, 2 * H):
            a, b = z_from_rho(beta, gamma)
            safe_ok = safe_ok and b / a < 1 / H
gate("B9 safe-depth ratio B/A<1/H", safe_ok)

# B10. The fixed endpoint counterexample is not a failure of the pole
# calculus: direct conjugate summation equals twice the real part.
direct = c_add(
    c_div(c_pow(c(1, -1), 8), c_pow(c(Q(3, 2), -1), 16)),
    c_div(c_pow(c(1, 1), 8), c_pow(c(Q(3, 2), 1), 16)),
)
gate(
    "B10 conjugate-pair bookkeeping",
    direct[1] == 0
    and Q(factorial(15)) * direct[0] == expected_actual,
)

print(f"BREAKER FINDINGS {len(findings)}/{checks}")
if findings:
    print("FIRED " + ",".join(findings))
    raise SystemExit(2)
raise SystemExit(0)
