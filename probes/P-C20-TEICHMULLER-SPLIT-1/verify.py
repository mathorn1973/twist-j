#!/usr/bin/env python3
"""Exact audit for P-C20-TEICHMULLER-SPLIT-1.

Finite exact identities in the thick ramified fiber Z[zeta_5]/5, plus one
all-m valuation identity with a one-line proof (5^(m-1) is odd). The
independent matrix leg re-derives the cycle from the raw axiom step map with
no ring multiplication reused.
"""


P = 5
CONE = (1, 0, 0, 0)
CZERO = (0, 0, 0, 0)
J = (1, 0, 1, 0)

checks = []


def check(name, condition):
    checks.append((name, bool(condition)))


def ring_mul(left, right):
    """Multiply in Z[zeta_5]/5, basis (1, j, j^2, j^3), j^5 = 1."""
    prod = [0] * 5
    for i, a in enumerate(left):
        if a:
            for k, b in enumerate(right):
                prod[(i + k) % 5] = (prod[(i + k) % 5] + a * b) % P
    top = prod[4]
    return tuple((prod[t] - top) % P for t in range(4))


def ring_pow(value, exponent):
    out = CONE
    for _ in range(exponent):
        out = ring_mul(out, value)
    return out


def ring_order(value):
    current, exponent = value, 1
    while current != CONE:
        current = ring_mul(current, value)
        exponent += 1
        if exponent > 600:
            return 0
    return exponent


def ring_sub(left, right):
    return tuple((a - b) % P for a, b in zip(left, right))


def scalar(t):
    return (t % P, 0, 0, 0)


ALL = [(a, b, c, d) for a in range(P) for b in range(P)
       for c in range(P) for d in range(P)]

check(
    "01 RING         Z[zeta_5]/5 in the basis (1,j,j^2,j^3); J=1+j^2 has ord(J)=20 and J^10=-1",
    ring_order(J) == 20 and ring_pow(J, 10) == scalar(4),
)

check(
    "02 WHEEL        J^5=2 exactly, the scalar i_5 with i_5^4=1; the fifth powers walk 2,-1,3=phi",
    ring_pow(J, 5) == scalar(2) and pow(2, 4, P) == 1
    and [ring_pow(J, 5 * k) for k in range(1, 4)] == [scalar(2), scalar(4), scalar(3)],
)

UNIP = ring_pow(J, 16)
NILP = ring_sub(UNIP, CONE)
split_ok = UNIP == ring_mul(scalar(3), J) and ring_order(UNIP) == 5
split_ok &= ring_pow(NILP, 4) == CZERO and ring_pow(NILP, 3) != CZERO
split_ok &= ring_mul(ring_pow(J, 5), UNIP) == J
split_ok &= ({ring_pow(scalar(2), k) for k in range(4)}
             & {ring_pow(UNIP, k) for k in range(5)}) == {CONE}
check(
    "03 SPLIT        u=J^16=3J is unipotent of order 5 with nilpotency index exactly 4; J=J^5*J^16 and <2> intersect <u> = {1}: <J> = C_4 x C_5, Teichmueller times unipotent",
    split_ok,
)

constants = sorted(scalar(t) for t in range(1, P))
two_part_ok = sorted(
    x for x in (ring_pow(J, k) for k in range(20)) if ring_pow(x, 4) == CONE
) == constants
two_part_ok &= sorted(x for x in ALL if ring_pow(x, 8) == CONE) == constants
two_part_ok &= sorted(x for x in ALL if ring_pow(x, 4) == CONE) == constants
check(
    "04 TWO-PART     the 2-part of <J> is <J^5>=C_4; exhaustively over all 625 elements x^8=1 iff x^4=1 iff x is a nonzero constant: no order-8 element exists",
    two_part_ok,
)

depth_ok = sum(1 for x in ALL if sum(x) % P != 0) == 500
depth_ok &= all((4 * 5 ** (m - 1)) % 8 == 4 for m in range(1, 13))
check(
    "05 DEPTH        |units|=500=4*5^3, and v_2(4*5^(m-1))=2 at every depth m (witnessed m<=12, proven all m since 5^(m-1) is odd): eight is forbidden by Lagrange",
    depth_ok,
)


def mat_mul(left, right):
    return tuple(tuple(sum(left[i][k] * right[k][j] for k in range(4)) % P
                       for j in range(4)) for i in range(4))


def mat_sub(left, right):
    return tuple(tuple((left[i][j] - right[i][j]) % P for j in range(4))
                 for i in range(4))


def mat_scalar(t):
    return tuple(tuple((t if i == j else 0) % P for j in range(4)) for i in range(4))


def mat_pow(value, exponent):
    out = mat_scalar(1)
    for _ in range(exponent):
        out = mat_mul(out, value)
    return out


def mat_order(value):
    current, exponent = value, 1
    while current != mat_scalar(1):
        current = mat_mul(current, value)
        exponent += 1
        if exponent > 600:
            return 0
    return exponent


def step(vector):
    a, b, c, d = vector
    return ((a - c + d) % P, (b - c) % P, a % P, (b - c + d) % P)


STEP_MATRIX = tuple(tuple(v % P for v in row) for row in
                    ((1, 0, -1, 1),
                     (0, 1, -1, 0),
                     (1, 0, 0, 0),
                     (0, 1, -1, 1)))

matrix_ok = mat_order(STEP_MATRIX) == 20
matrix_ok &= mat_pow(STEP_MATRIX, 5) == mat_scalar(2)
matrix_ok &= mat_pow(STEP_MATRIX, 10) == mat_scalar(4)
matrix_ok &= mat_pow(STEP_MATRIX, 16) == mat_mul(mat_scalar(3), STEP_MATRIX)
jordan = mat_sub(STEP_MATRIX, mat_scalar(2))
matrix_ok &= mat_pow(jordan, 4) == mat_scalar(0) and mat_pow(jordan, 3) != mat_scalar(0)
vector = (1, 0, 0, 0)
for k in range(20):
    matrix_ok &= tuple(mat_pow(STEP_MATRIX, k)[i][0] for i in range(4)) == vector
    matrix_ok &= vector == ring_pow(J, k)
    vector = step(vector)
check(
    "06 MATRIX       the raw axiom step matrix independently gives M^5=2I, M^10=-I, M^16=3M, ord(M)=20, (M-2I)^4=0!=(M-2I)^3 (one Jordan block J_4(2)), in exact column agreement with the ring walk for k=0..19",
    matrix_ok,
)


passed = sum(result for _, result in checks)
for name, result in checks:
    print(("PASS " if result else "FAIL ") + name)
if passed == len(checks):
    print(f"RESULT {passed}/{len(checks)} ALL PASS")
else:
    print(f"RESULT {passed}/{len(checks)} FAILURES PRESENT")
raise SystemExit(0 if passed == len(checks) else 1)
