#!/usr/bin/env python3
"""Exact audit for P-C8-BILINEAR-SHADOW-2.

The all-n statements are proof-first.  This verifier exhausts F_25, both
axes of the C8 subgroup, the Galois action, all exponent classes of the
branch-invariant record, and a fixed trajectory prefix.  It writes an exact
LF transcript on every host through the binary stdout interface.
"""

import sys


P = 5
ZERO = (0, 0)
ONE = (1, 0)
MINUS_ONE = (4, 0)
J = (2, 0)
PHI = (3, 0)
TAU = (0, 1)
N_MAX = 1 << 16

checks = []


def check(name, condition):
    checks.append((name, bool(condition)))


def neg(value):
    return ((-value[0]) % P, (-value[1]) % P)


def mul(left, right):
    """Multiply pairs in F_5[tau]/(tau^2 - 2)."""
    a, b = left
    c, d = right
    return ((a * c + 2 * b * d) % P, (a * d + b * c) % P)


def power(value, exponent):
    out = ONE
    base = value
    while exponent:
        if exponent & 1:
            out = mul(out, base)
        base = mul(base, base)
        exponent >>= 1
    return out


def frobenius(value):
    return power(value, 5)


def norm(value):
    product = mul(value, frobenius(value))
    return product[0] if product[1] == 0 else None


def order(value):
    for exponent in range(1, 25):
        if power(value, exponent) == ONE:
            return exponent
    return 0


ETA = power(TAU, 3)
ALL = [(a, b) for a in range(P) for b in range(P)]
UNITS = [x for x in ALL if x != ZERO]
BASE_AXIS = [(a, 0) for a in range(1, P)]
TAU_AXIS = [(0, b) for b in range(1, P)]
C8 = [power(TAU, k) for k in range(8)]

field_ok = all(a * a % P != 2 for a in range(P))
field_ok &= order(TAU) == 8 and power(TAU, 2) == J
field_ok &= power(TAU, 4) == MINUS_ONE
field_ok &= ETA == (0, 2) and power(ETA, 2) == PHI and order(ETA) == 8
field_ok &= sorted(x for x in ALL if mul(x, x) == PHI) == sorted(
    [ETA, neg(ETA)]
)
field_ok &= sorted(x for x in ALL if mul(x, x) == J) == sorted(
    [TAU, neg(TAU)]
)
check(
    "01 FIELD        F_25 pair model exact; tau has order 8 with tau^2=J; eta=tau^3 has eta^2=phi; the two square-root pairs are exact",
    field_ok,
)

roots4 = [x for x in UNITS if power(x, 4) == ONE]
roots8 = [x for x in UNITS if power(x, 8) == ONE]
ord8 = [x for x in UNITS if order(x) == 8]
axes_ok = sorted(C8) == sorted(BASE_AXIS + TAU_AXIS)
axes_ok &= sorted(power(TAU, 2 * k) for k in range(4)) == sorted(BASE_AXIS)
axes_ok &= sorted(power(TAU, 2 * k + 1) for k in range(4)) == sorted(TAU_AXIS)
axes_ok &= sorted(roots4) == sorted(BASE_AXIS)
axes_ok &= sorted(roots8) == sorted(C8)
axes_ok &= sorted(ord8) == sorted([TAU, neg(TAU), ETA, neg(ETA)])
axes_ok &= {mul(x, x) for x in ord8} == {J, PHI}
check(
    "02 AXES         <tau>=F_5* union tau F_5*: even powers are exactly the nonzero base-field axis; all fourth and eighth roots and all order-8 elements are exhausted",
    axes_ok,
)

galois_ok = all(frobenius((a, b)) == (a, (-b) % P) for a, b in ALL)
galois_ok &= all(frobenius(x) == x for x in BASE_AXIS)
galois_ok &= all(frobenius(x) == neg(x) for x in TAU_AXIS)
galois_ok &= all(norm(x) == norm(neg(x)) for x in ALL)
check(
    "03 GALOIS       Frobenius is a+b*tau -> a-b*tau; it fixes F_5 pointwise, negates tau F_5, and N(x)=N(-x) on all of F_25",
    galois_ok,
)

swap_ok = True
plus_state, minus_state = ONE, ONE
for n in range(N_MAX):
    digit_sum = n.bit_count()
    swap_ok &= plus_state == power(ETA, digit_sum % 8)
    swap_ok &= minus_state == power(neg(ETA), digit_sum % 8)
    swap_ok &= frobenius(plus_state) == minus_state
    swap_ok &= minus_state == (
        plus_state if digit_sum % 2 == 0 else neg(plus_state)
    )
    carry = ((n + 1) & -(n + 1)).bit_length() - 1
    step = (1 - carry) % 8
    plus_state = mul(plus_state, power(ETA, step))
    minus_state = mul(minus_state, power(neg(ETA), step))
check(
    "04 BRANCH-SWAP  both recursions equal r_epsilon^s2(n) for 0<=n<2^16 and Frob(Y+)=Y- throughout: the registered branches are Galois-conjugate",
    swap_ok,
)

even_classes = (0, 2, 4, 6)
odd_classes = (1, 3, 5, 7)
record_ok = all(
    norm(power(ETA, s)) == norm(power(neg(ETA), s)) == pow(2, s, P)
    for s in range(8)
)
record_ok &= all(
    power(ETA, s) == power(neg(ETA), s) == (pow(3, s // 2, P), 0)
    for s in even_classes
)
record_ok &= all(
    mul(power(ETA, s), power(ETA, t))
    == mul(power(neg(ETA), s), power(neg(ETA), t))
    == (pow(3, ((s + t) % 8) // 2, P), 0)
    for s in odd_classes
    for t in odd_classes
)
record_ok &= all(
    (power(ETA, s) == power(neg(ETA), s)) == (s % 2 == 0)
    for s in range(8)
)
record_ok &= all(
    mul(power(ETA, s), power(ETA, t))[1] != 0
    and mul(power(ETA, s), power(ETA, t))
    != mul(power(neg(ETA), s), power(neg(ETA), t))
    for s in even_classes
    for t in odd_classes
)
check(
    "05 RECORD       Theta always, Y on even digit-sum classes, and Y_n*Y_m on odd pairs form an F_5-valued branch-invariant record; mixed parity is off-axis and branch-dependent",
    record_ok,
)

refine_ok = all(
    (pow(2, s, P) == pow(2, t, P)) == (s % 4 == t % 4)
    for s in range(8)
    for t in range(8)
)
refine_ok &= all(
    (power(ETA, s) == power(ETA, t)) == (s % 8 == t % 8)
    for s in even_classes
    for t in even_classes
)
odd_pairs = [(s, t) for s in odd_classes for t in odd_classes]
refine_ok &= all(
    (
        mul(power(ETA, s), power(ETA, t))
        == mul(power(ETA, u), power(ETA, v))
    )
    == ((s + t) % 8 == (u + v) % 8)
    for s, t in odd_pairs
    for u, v in odd_pairs
)
s15, s255 = (15).bit_count(), (255).bit_count()
refine_ok &= pow(2, s15, P) == pow(2, s255, P) == 1
refine_ok &= power(ETA, s15) == MINUS_ONE and power(ETA, s255) == ONE
s1, s31 = (1).bit_count(), (31).bit_count()
refine_ok &= pow(2, s1, P) == pow(2, s31, P) == 2
refine_ok &= mul(power(ETA, s1), power(ETA, s1)) == PHI
refine_ok &= mul(power(ETA, s1), power(ETA, s31)) == J
refine_ok &= all(
    mul(power(ETA, s), power(ETA, s)) == (pow(pow(2, s, P), 3, P), 0)
    for s in even_classes
)
check(
    "06 REFINEMENT   the norm reads exactly s2 mod 4; even values and odd-pair products read the declared classes mod 8; witnesses 15/255 and (1,1)/(1,31) separate them",
    refine_ok,
)


passed = sum(result for _, result in checks)
lines = [("PASS " if result else "FAIL ") + name for name, result in checks]
if passed == len(checks):
    lines.append(f"RESULT {passed}/{len(checks)} ALL PASS")
else:
    lines.append(f"RESULT {passed}/{len(checks)} FAILURES PRESENT")
sys.stdout.buffer.write(("\n".join(lines) + "\n").encode("ascii"))
raise SystemExit(0 if passed == len(checks) else 1)
