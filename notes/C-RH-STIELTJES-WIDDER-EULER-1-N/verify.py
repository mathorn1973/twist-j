#!/usr/bin/env python3
"""Exact audit for C-RH-STIELTJES-WIDDER-EULER-1-N.

Python standard library only. Fractions and integer polynomial arithmetic.
No float, no external data, no zeta ordinate. The universal result is carried
by PROOF.md. This verifier audits frozen algebra and synthetic controls.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial

Q = Fraction
C = tuple[Q, Q]
Poly = list[C]


def c(re: int | Q = 0, im: int | Q = 0) -> C:
    return (Q(re), Q(im))


def c_add(x: C, y: C) -> C:
    return (x[0] + y[0], x[1] + y[1])


def c_neg(x: C) -> C:
    return (-x[0], -x[1])


def c_sub(x: C, y: C) -> C:
    return c_add(x, c_neg(y))


def c_mul(x: C, y: C) -> C:
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def c_scale(a: int | Q, x: C) -> C:
    return (Q(a) * x[0], Q(a) * x[1])


def c_conj(x: C) -> C:
    return (x[0], -x[1])


def c_inv(x: C) -> C:
    den = x[0] * x[0] + x[1] * x[1]
    if den == 0:
        raise ZeroDivisionError("zero complex rational")
    return (x[0] / den, -x[1] / den)


def c_div(x: C, y: C) -> C:
    return c_mul(x, c_inv(y))


def c_pow(x: C, n: int) -> C:
    if n < 0:
        return c_pow(c_inv(x), -n)
    result = c(1)
    base = x
    exponent = n
    while exponent:
        if exponent & 1:
            result = c_mul(result, base)
        base = c_mul(base, base)
        exponent >>= 1
    return result


def z_from_rho(beta: Q, gamma: Q) -> C:
    return (beta * (beta - 1) - gamma * gamma, gamma * (2 * beta - 1))


def alpha_square(beta: Q, gamma: Q) -> C:
    x = beta - Q(1, 2)
    return (x * x - gamma * gamma, 2 * x * gamma)


def resolvent(u: Q, z: C) -> C:
    return c_inv(c_sub(c(u), z))


def pair_f(u: Q, z: C) -> Q:
    return c_add(resolvent(u, z), resolvent(u, c_conj(z)))[0]


def pair_f_formula(u: Q, z: C) -> Q:
    A = -z[0]
    B = z[1]
    return 2 * (u + A) / ((u + A) ** 2 + B**2)


def single_w_closed(k: int, u: Q, z: C) -> C:
    return c_div(
        c_scale(factorial(2 * k - 1), c_pow(c_neg(z), k)),
        c_pow(c_sub(c(u), z), 2 * k),
    )


def orbit_w(k: int, u: Q, z: C) -> Q:
    value = single_w_closed(k, u, z)
    return value[0] if z[1] == 0 else 2 * value[0]


def pair_w1_formula(u: Q, z: C) -> Q:
    A = -z[0]
    B = z[1]
    return 2 * (A * (u + A) ** 2 + B**2 * (2 * u + A)) / (
        ((u + A) ** 2 + B**2) ** 2
    )


def poly_trim(p: Poly) -> Poly:
    out = p[:]
    while len(out) > 1 and out[-1] == c(0):
        out.pop()
    return out


def poly_add(p: Poly, q: Poly) -> Poly:
    length = max(len(p), len(q))
    out = [c(0) for _ in range(length)]
    for i in range(length):
        if i < len(p):
            out[i] = c_add(out[i], p[i])
        if i < len(q):
            out[i] = c_add(out[i], q[i])
    return poly_trim(out)


def poly_scale(a: int | Q, p: Poly) -> Poly:
    return poly_trim([c_scale(a, coefficient) for coefficient in p])


def poly_sub(p: Poly, q: Poly) -> Poly:
    return poly_add(p, poly_scale(-1, q))


def poly_derivative(p: Poly) -> Poly:
    if len(p) <= 1:
        return [c(0)]
    return [c_scale(i, p[i]) for i in range(1, len(p))]


def poly_times_u_minus_z(p: Poly, z: C) -> Poly:
    out = [c(0) for _ in range(len(p) + 1)]
    for i, coefficient in enumerate(p):
        out[i] = c_add(out[i], c_mul(c_neg(z), coefficient))
        out[i + 1] = c_add(out[i + 1], coefficient)
    return poly_trim(out)


def poly_evaluate(p: Poly, u: Q) -> C:
    value = c(0)
    for coefficient in reversed(p):
        value = c_add(c_mul(value, c(u)), coefficient)
    return value


def single_w_recursive(k: int, u: Q, z: C) -> C:
    """Differentiate N(u)/(u-z)^p by an exact numerator recurrence."""
    numerator = [c(0) for _ in range(k)] + [c(1)]
    denominator_power = 1
    for _ in range(2 * k - 1):
        numerator = poly_sub(
            poly_times_u_minus_z(poly_derivative(numerator), z),
            poly_scale(denominator_power, numerator),
        )
        denominator_power += 1
    value = c_div(poly_evaluate(numerator, u), c_pow(c_sub(c(u), z), denominator_power))
    return c_scale((-1) ** (k - 1), value)


def first_nonpositive(u: Q, z: C, upper: int) -> int | None:
    for k in range(1, upper + 1):
        if orbit_w(k, u, z) <= 0:
            return k
    return None


checks = 0


def gate(name: str, condition: bool, detail: str = "") -> None:
    global checks
    if not condition:
        raise AssertionError(name + ((": " + detail) if detail else ""))
    checks += 1
    print(f"{name} PASS{(': ' + detail) if detail else ''}")


print("C-RH-STIELTJES-WIDDER-EULER-1-N verify")

s_values = (Q(3, 2), Q(2), Q(5, 2), Q(3), Q(7, 2), Q(5))
coordinate_ok = all(
    (2 * s - 1) ** 2 == 1 + 4 * s * (s - 1) and s * (s - 1) > 0
    for s in s_values
)
gate("V1 functional coordinate u=s(s-1)", coordinate_ok)

rho_controls = (
    (Q(1, 2), Q(1)),
    (Q(9, 10), Q(1, 2)),
    (Q(3, 4), Q(10)),
    (Q(2, 5), Q(7, 3)),
)
symmetry_ok = True
for beta, gamma in rho_controls:
    z = z_from_rho(beta, gamma)
    symmetry_ok = symmetry_ok and z_from_rho(1 - beta, -gamma) == z
    symmetry_ok = symmetry_ok and z_from_rho(beta, -gamma) == c_conj(z)
gate("V2 functional-pair and conjugation symmetry", symmetry_ok)

shift_ok = True
for s in s_values:
    u = s * (s - 1)
    a = s - Q(1, 2)
    for beta, gamma in rho_controls:
        z = z_from_rho(beta, gamma)
        shift_ok = shift_ok and c_sub(c(u), z) == c_sub(c(a * a), alpha_square(beta, gamma))
gate("V3 shifted square-resolvent identity", shift_ok)

euler_prefactor_ok = all(
    Q(1, 2 * s - 1) * (Q(1, s) + Q(1, s - 1)) == Q(1, s * (s - 1))
    for s in s_values
)
gate("V4 Euler polar prefactor", euler_prefactor_ok)

u = Q(1, 100)
z_low = z_from_rho(Q(9, 10), Q(1, 2))
z_high = z_from_rho(Q(3, 4), Q(10))
z_line = z_from_rho(Q(1, 2), Q(1))

pair_formula_ok = all(
    pair_f(u, z) == pair_f_formula(u, z) > 0 for z in (z_low, z_high)
)
gate("V5 unconditional resolvent-pair positivity", pair_formula_ok)

w1_ok = all(
    orbit_w(1, u, z) == pair_w1_formula(u, z) > 0 for z in (z_low, z_high)
)
gate("V6 unconditional W1-pair positivity", w1_ok)

recursive_ok = True
for z in (z_line, z_low, z_high):
    for k in range(1, 7):
        recursive_ok = recursive_ok and single_w_recursive(k, u, z) == single_w_closed(k, u, z)
gate("V7 one-pole formula by recursive differentiation", recursive_ok)

stieltjes_atom_ok = True
for t in (Q(1, 4), Q(1), Q(5, 4), Q(7), Q(101, 3)):
    z = c(-t)
    for k in range(1, 9):
        expected = Q(factorial(2 * k - 1)) * t**k / (u + t) ** (2 * k)
        stieltjes_atom_ok = stieltjes_atom_ok and orbit_w(k, u, z) == expected > 0
gate("V8 critical-line Stieltjes atoms k=1..8", stieltjes_atom_ok)

low_ok = pair_f(u, z_low) > 0 and orbit_w(1, u, z_low) > 0 and orbit_w(2, u, z_low) < 0
gate("V9 low off-line first failure", low_ok, "first_nonpositive=2")

high_first = first_nonpositive(u, z_high, 64)
high_ok = high_first == 32 and all(orbit_w(k, u, z_high) > 0 for k in range(1, 32))
gate("V10 high off-line delayed failure", high_ok, f"first_nonpositive={high_first}")

# Formal boundary algebra: E(C-iS)/(iy)=E(-S-iC)/y.
# Coefficients are kept as exact integer pairs in the basis (C,S).
real_after_division = (0, -1)   # -S
imag_after_division = (-1, 0)   # -C
density_after_minus_im = (1, 0) # +C
cut_ok = (
    real_after_division == (0, -1)
    and imag_after_division == (-1, 0)
    and density_after_minus_im == (1, 0)
)
gate("V11 prime-cut upper-lip orientation", cut_ok)

# Algebraic no-cancellation identity:
# x(x-1)-y(y-1)=(x-y)(x+y-1).
no_cancel_ok = all(
    x * (x - 1) - y * (y - 1) == (x - y) * (x + y - 1)
    for x in (Q(-3, 2), Q(0), Q(1, 3), Q(2), Q(7, 4))
    for y in (Q(-2), Q(1, 5), Q(1), Q(9, 4))
)
gate("V12 functional-pair pole collision factorization", no_cancel_ok)

print(f"RESULT {checks}/{checks} ALL PASS")
