#!/usr/bin/env python3
"""Exact audit for C-RH-WIDDER-ANGLE-SWEEP-CORRECTION-1-N.

The universal statements are carried by PROOF.md. This program uses exact
integer and Fraction arithmetic only. It audits the polynomial coefficient
form, the two handoff corrections, the owner depths, the finite-prefix family,
and the conditional safe-depth algebra.

No float, no external data, no actual zeta zero.
"""

from __future__ import annotations

from fractions import Fraction as Q
from math import comb, factorial

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


def poly_eval(coefficients: list[Q], u: Q) -> Q:
    value = Q(0)
    for coefficient in reversed(coefficients):
        value = value * u + coefficient
    return value


def numerator_coefficients(k: int, A: Q, B: Q) -> list[Q]:
    """Coefficients of Re[(A-iB)^k (u+A+iB)^(2k)]."""
    left = c_pow(c(A, -B), k)
    powers = [c(1)]
    right_base = c(A, B)
    for _ in range(2 * k):
        powers.append(c_mul(powers[-1], right_base))
    return [
        Q(comb(2 * k, j)) * c_mul(left, powers[2 * k - j])[0]
        for j in range(2 * k + 1)
    ]


def pair_term_polynomial(k: int, A: Q, B: Q, u: Q) -> Q:
    numerator = poly_eval(numerator_coefficients(k, A, B), u)
    denominator = ((u + A) * (u + A) + B * B) ** (2 * k)
    return 2 * Q(factorial(2 * k - 1)) * numerator / denominator


def pair_term_direct(k: int, A: Q, B: Q, u: Q) -> Q:
    ratio = c_div(c_pow(c(A, -B), k), c_pow(c(u + A, -B), 2 * k))
    return 2 * Q(factorial(2 * k - 1)) * ratio[0]


def first_negative_power(A: Q, B: Q, cap: int = 10000) -> int | None:
    if B == 0:
        return None
    value = c(1)
    base = c(A, -B)
    for k in range(1, cap + 1):
        value = c_mul(value, base)
        if value[0] < 0:
            return k
    return None


def z_from_rho(beta: Q, gamma: Q) -> tuple[Q, Q]:
    return (
        gamma * gamma + beta * (1 - beta),
        abs(gamma * (2 * beta - 1)),
    )


checks = 0


def gate(name: str, condition: bool, detail: str = "") -> None:
    global checks
    if not condition:
        raise AssertionError(name + ((": " + detail) if detail else ""))
    checks += 1
    print(f"{name} PASS{(': ' + detail) if detail else ''}")


print("C-RH-WIDDER-ANGLE-SWEEP-CORRECTION-1-N verify")

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

# V1. Independent polynomial route agrees with direct complex division.
route_ok = True
for A, B in (
    (Q(1), Q(1)),
    (Q(17, 50), Q(2, 5)),
    (Q(1603, 16), Q(5)),
    (Q(5), Q(2)),
):
    for k in range(1, 13):
        for u in ugrid:
            route_ok = route_ok and (
                pair_term_polynomial(k, A, B, u)
                == pair_term_direct(k, A, B, u)
            )
gate("V1 polynomial numerator equals direct pair formula", route_ok)

# V2. Frozen arbitrary-level endpoint counterexample.
A = Q(1)
B = Q(1)
u = Q(1, 2)
endpoint = c_pow(c(1, -1), 8)[0]
counterexample = pair_term_polynomial(8, A, B, u)
expected = Q(
    -172056926056081143103488000,
    51185893014090757,
)
gate(
    "V2 arbitrary-level endpoint counterexample",
    endpoint == 16 and counterexample == expected and counterexample < 0,
)

# V3. Resonance coefficient geometry.
coeff2 = numerator_coefficients(2, A, B)
coeff3 = numerator_coefficients(3, A, B)
resonance_ok = (
    coeff2 == [Q(0), Q(16), Q(24), Q(8), Q(0)]
    and all(value >= 0 for value in coeff2)
    and poly_eval(coeff2, Q(1, 1000)) > 0
    and coeff3[0] < 0
    and first_negative_power(A, B) == 3
)
gate("V3 resonance first failure is 3, not ceil value 2", resonance_ok)

# V4. Owner depths survive.
A_low, B_low = z_from_rho(Q(9, 10), Q(1, 2))
A_high, B_high = z_from_rho(Q(3, 4), Q(10))
gate(
    "V4 owner first-failure depths",
    first_negative_power(A_low, B_low) == 2
    and first_negative_power(A_high, B_high) == 32,
    "low=2 high=32",
)

# V5. Before first failure every numerator coefficient is nonnegative.
coefficient_geometry_ok = True
controls = (
    (Q(17, 50), Q(2, 5)),
    (Q(1603, 16), Q(5)),
    (Q(1), Q(1)),
    (Q(5), Q(2)),
    (Q(13), Q(3)),
)
for a, b in controls:
    first = first_negative_power(a, b, 1024)
    if first is None:
        continue
    for k in range(1, first):
        coefficient_geometry_ok = coefficient_geometry_ok and all(
            coefficient >= 0
            for coefficient in numerator_coefficients(k, a, b)
        )
    coefficient_geometry_ok = (
        coefficient_geometry_ok
        and numerator_coefficients(first, a, b)[0] < 0
    )
gate(
    "V5 first-failure coefficient geometry",
    coefficient_geometry_ok,
)

# V6. Corrected arbitrary-level integer criterion on a finite exact grid.
criterion_ok = True
later_endpoint_returns = 0
for a in (Q(1), Q(2), Q(3), Q(5)):
    for b in (Q(1), Q(2), Q(3), Q(5)):
        first = first_negative_power(a, b, 2048)
        for k in range(1, 49):
            sampled_negative = any(
                pair_term_polynomial(k, a, b, u0) < 0
                for u0 in ugrid
            )
            if sampled_negative:
                criterion_ok = criterion_ok and first is not None and first <= k
                if c_pow(c(a, -b), k)[0] >= 0:
                    later_endpoint_returns += 1
gate(
    "V6 corrected integer criterion finite audit",
    criterion_ok and later_endpoint_returns > 0,
    f"endpoint_returns={later_endpoint_returns}",
)

# V7. Intrinsic finite-prefix family, all coefficients, N=1..128.
prefix_ok = True
prefix_levels = 0
for N in range(1, 129):
    a = Q(N * N) + Q(3, 16)
    b = Q(N, 2)
    prefix_ok = prefix_ok and b / a < Q(1, 2 * N)
    base = c(a, -b)
    power = c(1)
    real_powers = [Q(1)]
    for _ in range(N):
        power = c_mul(power, base)
        real_powers.append(power[0])
    prefix_ok = prefix_ok and all(value > 0 for value in real_powers)
    for k in range(1, N + 1):
        prefix_levels += 1
        coefficients = numerator_coefficients(k, a, b)
        prefix_ok = prefix_ok and all(value > 0 for value in coefficients)
gate(
    "V7 finite-prefix horizon N=1..128",
    prefix_ok,
    f"levels={prefix_levels}",
)

# V8. Positive critical-line backgrounds preserve the prefix.
background_ok = True
N = 12
a = Q(N * N) + Q(3, 16)
b = Q(N, 2)
for k in range(1, N + 1):
    for u0 in ugrid:
        total = pair_term_polynomial(k, a, b, u0)
        for gamma in (Q(14), Q(21), Q(25), Q(30)):
            t = gamma * gamma + Q(1, 4)
            total += Q(factorial(2 * k - 1)) * t**k / (u0 + t) ** (2 * k)
        background_ok = background_ok and total > 0
gate("V8 positive on-line background preserves finite prefix", background_ok)

# V9. W2 strip geometry and termwise adjacent-level failure.
w2_ok = True
for beta in (Q(1, 100), Q(1, 3), Q(1, 2), Q(3, 4), Q(99, 100)):
    for gamma in (Q(1), Q(2), Q(5), Q(14), Q(1000)):
        a, b = z_from_rho(beta, gamma)
        w2_ok = w2_ok and b < a
        w2_ok = w2_ok and all(
            pair_term_polynomial(2, a, b, u0) > 0 for u0 in ugrid
        )
transition_fails = (
    all(pair_term_polynomial(1, A_low, B_low, u0) > 0 for u0 in ugrid)
    and any(pair_term_polynomial(2, A_low, B_low, u0) < 0 for u0 in ugrid)
)
gate("V9 W2 safe geometry and adjacent-level no-go", w2_ok and transition_fails)

# V10. Conditional safe-depth ratio algebra.
safe_ratio_ok = True
for H in (Q(1), Q(2), Q(10), Q(100), Q(10**6)):
    for beta in (Q(1, 100), Q(1, 3), Q(3, 4), Q(99, 100)):
        for gamma in (H, H + 1, 2 * H):
            a, b = z_from_rho(beta, gamma)
            safe_ratio_ok = safe_ratio_ok and b / a < 1 / H
gate("V10 actual-zeta safe-depth ratio B/A<1/H", safe_ratio_ok)

# V11. Exact later-level return is not isolated to one witness.
return_count = 0
for a, b in ((Q(1), Q(1)), (Q(2), Q(1)), (Q(3), Q(2)), (Q(5), Q(3))):
    first = first_negative_power(a, b, 2048)
    for k in range(1, 65):
        endpoint_nonnegative = c_pow(c(a, -b), k)[0] >= 0
        sampled_negative = any(
            pair_term_polynomial(k, a, b, u0) < 0 for u0 in ugrid
        )
        if first is not None and first <= k and endpoint_nonnegative and sampled_negative:
            return_count += 1
gate("V11 later-level endpoint return family", return_count > 0, f"witnesses={return_count}")

# V12. Pair convention, direct conjugate sum.
direct_pair = c_add(
    c_div(c_pow(c(1, -1), 8), c_pow(c(Q(3, 2), -1), 16)),
    c_div(c_pow(c(1, 1), 8), c_pow(c(Q(3, 2), 1), 16)),
)
pair_ok = (
    direct_pair[1] == 0
    and Q(factorial(15)) * direct_pair[0] == expected
)
gate("V12 conjugate-pair multiplicity convention", pair_ok)

print(f"RESULT {checks}/{checks} ALL PASS")
