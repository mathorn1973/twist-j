#!/usr/bin/env python3
"""Exact audit for P-C8-BILINEAR-SHADOW-1.

The all-n results are proof-first. This frozen verifier exhausts the F_25
field, the two axes of the order-eight group, the Galois action on both
digit branches, the branch-invariant base-valued record, and the strict
mod-8 refinement of the norm channel, on complete exponent classes and a
fixed finite trajectory prefix.
"""


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
field_ok &= order(TAU) == 8 and power(TAU, 2) == J and power(TAU, 4) == MINUS_ONE
field_ok &= ETA == (0, 2) and power(ETA, 2) == PHI and order(ETA) == 8
field_ok &= sorted(x for x in ALL if mul(x, x) == PHI) == sorted([ETA, neg(ETA)])
field_ok &= sorted(x for x in ALL if mul(x, x) == J) == sorted([TAU, neg(TAU)])
check(
    "01 FIELD        F_25 pair model exact; tau has order 8 with tau^2=J; eta=tau^3 has eta^2=phi; r^2=phi has exactly {eta,-eta} and r^2=J exactly {tau,-tau}",
    field_ok,
)

axes_ok = sorted(C8) == sorted(BASE_AXIS + TAU_AXIS)
axes_ok &= sorted(power(TAU, 2 * k) for k in range(4)) == sorted(BASE_AXIS)
axes_ok &= sorted(power(TAU, 2 * k + 1) for k in range(4)) == sorted(TAU_AXIS)
ord8 = [x for x in UNITS if order(x) == 8]
axes_ok &= sorted(ord8) == sorted([TAU, neg(TAU), ETA, neg(ETA)])
axes_ok &= {mul(x, x) for x in ord8} == {J, PHI}
axes_ok &= sum(1 for x in UNITS if power(x, 8) == ONE) == 8
check(
    "02 AXES         <tau> = F_5* union tau F_5*: even layer IS the base line, odd layer its tau-translate; order-8 elements are exactly {+-tau,+-eta}, all squaring into {J,phi}",
    axes_ok,
)

galois_ok = all(frobenius((a, b)) == (a, (-b) % P) for a, b in ALL)
galois_ok &= all(frobenius(x) == x for x in BASE_AXIS)
galois_ok &= all(frobenius(x) == neg(x) for x in TAU_AXIS)
galois_ok &= all(norm(x) == norm(neg(x)) for x in ALL)
check(
    "03 GALOIS       Frobenius x->x^5 is conjugation a+b tau -> a-b tau; it fixes the even layer pointwise, negates the odd layer, and N(x)=N(-x) on all of F_25",
    galois_ok,
)

swap_ok = True
plus_state, minus_state = ONE, ONE
for n in range(N_MAX):
    digit_sum = n.bit_count()
    swap_ok &= plus_state == power(ETA, digit_sum % 8)
    swap_ok &= minus_state == power(neg(ETA), digit_sum % 8)
    swap_ok &= frobenius(plus_state) == minus_state
    expected_minus = plus_state if digit_sum % 2 == 0 else neg(plus_state)
    swap_ok &= minus_state == expected_minus
    carry = ((n + 1) & -(n + 1)).bit_length() - 1
    step = power(ETA, (1 - carry) % 8)
    plus_state = mul(plus_state, step)
    minus_state = mul(minus_state, power(neg(ETA), (1 - carry) % 8))
check(
    "04 BRANCH-SWAP  both branch recursions equal r_epsilon^s2(n) for 0<=n<2^16 and Frob(Y+)=Y- everywhere: the registered branch involution IS the Galois action",
    swap_ok,
)

record_ok = all(norm(power(ETA, s)) == norm(power(neg(ETA), s)) for s in range(8))
record_ok &= all(
    power(ETA, s) == power(neg(ETA), s) == (pow(3, s // 2, P), 0)
    for s in range(0, 8, 2)
)
record_ok &= all(
    mul(power(ETA, s), power(ETA, t))
    == mul(power(neg(ETA), s), power(neg(ETA), t))
    == (pow(3, ((s + t) % 8) // 2, P), 0)
    for s in range(1, 8, 2) for t in range(1, 8, 2)
)
record_ok &= all((power(ETA, s) == power(neg(ETA), s)) == (s % 2 == 0) for s in range(8))
record_ok &= all(
    mul(power(ETA, s), power(ETA, t))[1] != 0
    and mul(power(ETA, s), power(ETA, t)) != mul(power(neg(ETA), s), power(neg(ETA), t))
    for s in range(0, 8, 2) for t in range(1, 8, 2)
)
check(
    "05 RECORD       the record (Theta always; Y at even s2; Y_n Y_m at odd pairs) is F_5-valued and branch-invariant; branches differ exactly at odd classes; mixed-parity products are off-base and branch-dependent",
    record_ok,
)

refine_ok = all(
    (pow(2, s, P) == pow(2, t, P)) == (s % 4 == t % 4)
    for s in range(8) for t in range(8)
)
refine_ok &= len({pow(3, s // 2, P) for s in range(0, 8, 2)}) == 4
refine_ok &= len({pow(3, u // 2, P) for u in range(0, 8, 2)}) == 4
s15, s255 = (15).bit_count(), (255).bit_count()
refine_ok &= pow(2, s15 % 4, P) == pow(2, s255 % 4, P) == 1
refine_ok &= power(ETA, s15 % 8) == MINUS_ONE and power(ETA, s255 % 8) == ONE
s1, s31 = (1).bit_count(), (31).bit_count()
refine_ok &= pow(2, s1 % 4, P) == pow(2, s31 % 4, P) == 2
refine_ok &= mul(power(ETA, s1 % 8), power(ETA, s1 % 8)) == PHI
refine_ok &= mul(power(ETA, s1 % 8), power(ETA, s31 % 8)) == (2, 0)
refine_ok &= all(
    mul(power(ETA, s), power(ETA, s)) == (pow(pow(2, s, P), 3, P), 0)
    for s in range(0, 8, 2)
)
check(
    "06 REFINEMENT   the norm channel reads exactly s2 mod 4; even-layer values read s2 mod 8 and odd-pair values read s2(n)+s2(m) mod 8; witnesses n=15 vs 255 and pairs (1,1) vs (1,31); even Y^2=Theta^-1",
    refine_ok,
)


passed = sum(result for _, result in checks)
for name, result in checks:
    print(("PASS " if result else "FAIL ") + name)
if passed == len(checks):
    print(f"RESULT {passed}/{len(checks)} ALL PASS")
else:
    print(f"RESULT {passed}/{len(checks)} FAILURES PRESENT")
raise SystemExit(0 if passed == len(checks) else 1)
