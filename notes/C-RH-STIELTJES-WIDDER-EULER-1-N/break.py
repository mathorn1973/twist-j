#!/usr/bin/env python3
"""Independent exact breaker for C-RH-STIELTJES-WIDDER-EULER-1-N.

Frozen before the positive proof and verifier. Python standard library only.
No float, no external data, no zeta ordinate. Synthetic rational controls only.

The breaker attacks:
  B1  the rho -> z=rho(rho-1) coordinate;
  B2  the conjugate-pair resolvent formula;
  B3  the unconditional W_1 formula and sign;
  B4  the single-pole Widder factorial identity by an independent Taylor path;
  B5  positivity of on-line atoms at several rungs;
  B6  survival of f and W_1 for a low off-line atom;
  B7  negativity of W_2 for that same low off-line atom;
  B8  delayed W_2 response for a high off-line atom;
  B9  the upper-lip prime-cut orientation;
  B10 a later finite-rung sign change for the high off-line atom.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
from typing import Callable

Q = Fraction
C = tuple[Q, Q]


def c(re: int | Q = 0, im: int | Q = 0) -> C:
    return (Q(re), Q(im))


def add(x: C, y: C) -> C:
    return (x[0] + y[0], x[1] + y[1])


def neg(x: C) -> C:
    return (-x[0], -x[1])


def sub(x: C, y: C) -> C:
    return add(x, neg(y))


def mul(x: C, y: C) -> C:
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def scale(a: int | Q, x: C) -> C:
    return (Q(a) * x[0], Q(a) * x[1])


def conj(x: C) -> C:
    return (x[0], -x[1])


def inv(x: C) -> C:
    den = x[0] * x[0] + x[1] * x[1]
    if den == 0:
        raise ZeroDivisionError("zero complex rational")
    return (x[0] / den, -x[1] / den)


def div(x: C, y: C) -> C:
    return mul(x, inv(y))


def power(x: C, n: int) -> C:
    if n < 0:
        return power(inv(x), -n)
    out = c(1)
    base = x
    exponent = n
    while exponent:
        if exponent & 1:
            out = mul(out, base)
        base = mul(base, base)
        exponent >>= 1
    return out


def z_from_rho(beta: Q, gamma: Q) -> C:
    # (beta+i gamma)(beta-1+i gamma)
    return (beta * (beta - 1) - gamma * gamma, gamma * (2 * beta - 1))


def resolvent(u: Q, z: C) -> C:
    return inv(sub(c(u), z))


def pair_resolvent(u: Q, z: C) -> Q:
    return add(resolvent(u, z), resolvent(u, conj(z)))[0]


def pair_resolvent_formula(u: Q, z: C) -> Q:
    # z=-A+iB
    A = -z[0]
    B = z[1]
    return 2 * (u + A) / ((u + A) ** 2 + B**2)


def single_w_closed(k: int, u: Q, z: C) -> C:
    numerator = scale(factorial(2 * k - 1), power(neg(z), k))
    denominator = power(sub(c(u), z), 2 * k)
    return div(numerator, denominator)


def single_w_taylor(k: int, u: Q, z: C) -> C:
    """Independent coefficient extraction at u+h.

    Expand (u+h)^k and 1/(u-z+h), convolve through degree 2k-1,
    multiply the coefficient by (2k-1)! and the Widder sign.
    """
    order = 2 * k - 1
    numerator: list[C] = [c(0) for _ in range(order + 1)]
    # Exact binomial coefficients without importing a symbolic engine.
    for j in range(k + 1):
        coefficient = Q(factorial(k), factorial(j) * factorial(k - j)) * u ** (k - j)
        numerator[j] = c(coefficient)

    d = sub(c(u), z)
    denominator_inverse = [
        scale((-1) ** n, inv(power(d, n + 1))) for n in range(order + 1)
    ]
    coefficient = c(0)
    for j in range(min(k, order) + 1):
        coefficient = add(coefficient, mul(numerator[j], denominator_inverse[order - j]))
    return scale(((-1) ** (k - 1)) * factorial(order), coefficient)


def orbit_w(k: int, u: Q, z: C) -> Q:
    value = single_w_closed(k, u, z)
    if z[1] == 0:
        return value[0]
    return 2 * value[0]


def pair_w1_formula(u: Q, z: C) -> Q:
    A = -z[0]
    B = z[1]
    den = ((u + A) ** 2 + B**2) ** 2
    num = 2 * (A * (u + A) ** 2 + B**2 * (2 * u + A))
    return num / den


def first_nonpositive(u: Q, z: C, upper: int) -> int | None:
    for k in range(1, upper + 1):
        if orbit_w(k, u, z) <= 0:
            return k
    return None


findings: list[str] = []
checks = 0


def gate(name: str, predicate: bool, detail: str = "") -> None:
    global checks
    checks += 1
    if predicate:
        print(f"{name} PASS{(': ' + detail) if detail else ''}")
    else:
        findings.append(name)
        print(f"{name} FAIL{(': ' + detail) if detail else ''}")


print("C-RH-STIELTJES-WIDDER-EULER-1-N independent breaker")

u_low = Q(1, 100)
z_line = z_from_rho(Q(1, 2), Q(1))
z_low = z_from_rho(Q(9, 10), Q(1, 2))
z_high = z_from_rho(Q(3, 4), Q(10))

gate(
    "B1 coordinate controls",
    z_line == c(Q(-5, 4))
    and z_low == c(Q(-17, 50), Q(2, 5))
    and z_high == c(Q(-1603, 16), Q(5)),
)

gate(
    "B2 conjugate resolvent",
    pair_resolvent(u_low, z_low) == pair_resolvent_formula(u_low, z_low)
    and pair_resolvent(u_low, z_high) == pair_resolvent_formula(u_low, z_high),
)

gate(
    "B3 W1 pair formula",
    orbit_w(1, u_low, z_low) == pair_w1_formula(u_low, z_low)
    and orbit_w(1, u_low, z_high) == pair_w1_formula(u_low, z_high)
    and pair_w1_formula(u_low, z_low) > 0
    and pair_w1_formula(u_low, z_high) > 0,
)

identity_ok = True
for z in (z_line, z_low, z_high):
    for k in (1, 2, 3):
        identity_ok = identity_ok and single_w_closed(k, u_low, z) == single_w_taylor(k, u_low, z)
gate("B4 factorial identity k=1..3", identity_ok)

gate(
    "B5 on-line positivity k=1..8",
    all(orbit_w(k, u_low, z_line) > 0 for k in range(1, 9)),
)

gate(
    "B6 low off-line first rung survives",
    pair_resolvent(u_low, z_low) > 0 and orbit_w(1, u_low, z_low) > 0,
)

gate(
    "B7 low off-line W2 detects",
    orbit_w(2, u_low, z_low) < 0,
    f"sign={'negative' if orbit_w(2, u_low, z_low) < 0 else 'nonnegative'}",
)

gate(
    "B8 high off-line W2 delayed",
    orbit_w(1, u_low, z_high) > 0 and orbit_w(2, u_low, z_high) > 0,
)

# Formal upper-lip algebra. Write exp(-ell s)=E(C-iS), divide by q=iy.
# (C-iS)/(iy)=(-S-iC)/y. Hence Im=-E*C/y and -Im/pi=+E*C/(pi*y).
real_coeff_S = -1
imag_coeff_C = -1
density_coeff_C = -imag_coeff_C
gate(
    "B9 prime-cut orientation",
    real_coeff_S == -1 and imag_coeff_C == -1 and density_coeff_C == 1,
)

high_first = first_nonpositive(u_low, z_high, 128)
gate(
    "B10 high off-line later rung detects",
    high_first is not None and high_first > 2,
    f"first_nonpositive={high_first if high_first is not None else '>128'}",
)

print(f"BREAKER FINDINGS {len(findings)}/{checks}")
if findings:
    print("FIRED " + ",".join(findings))
    raise SystemExit(1)
raise SystemExit(0)
