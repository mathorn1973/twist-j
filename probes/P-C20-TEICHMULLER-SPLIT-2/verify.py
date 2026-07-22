#!/usr/bin/env python3
"""Exact audit for P-C20-TEICHMULLER-SPLIT-2.

The finite carrier is R = Z[zeta_5]/(5).  The all-depth statement is
proved in PREREG.md; this program audits its exact lattice determinant
and residue-group ingredients without replacing the cyclotomic quotients
by a different truncated-polynomial carrier.
"""

import sys


P = 5
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
J = (1, 0, 1, 0)
LAMBDA = (1, -1, 0, 0)
BASIS = tuple(tuple(1 if i == j else 0 for i in range(4)) for j in range(4))
ALL = tuple(
    (a, b, c, d)
    for a in range(P)
    for b in range(P)
    for c in range(P)
    for d in range(P)
)


def o_mul(left, right):
    """Multiply in Z[j]/(j^4+j^3+j^2+j+1), with integer coefficients."""
    product = [0] * 7
    for i, a in enumerate(left):
        for k, b in enumerate(right):
            product[i + k] += a * b
    for degree in range(6, 3, -1):
        top = product[degree]
        if top:
            for shift in range(4):
                product[degree - 4 + shift] -= top
            product[degree] = 0
    return tuple(product[i] for i in range(4))


def ring_mul(left, right):
    return tuple(value % P for value in o_mul(left, right))


def ring_sub(left, right):
    return tuple((a - b) % P for a, b in zip(left, right))


def ring_pow(value, exponent):
    result = ONE
    base = value
    power = exponent
    while power:
        if power & 1:
            result = ring_mul(result, base)
        base = ring_mul(base, base)
        power >>= 1
    return result


def ring_order(value, limit=100):
    current = ONE
    for exponent in range(1, limit + 1):
        current = ring_mul(current, value)
        if current == ONE:
            return exponent
    return 0


def scalar(value):
    return (value % P, 0, 0, 0)


def residue(value):
    return sum(value) % P


def matrix_from_columns(columns):
    return tuple(tuple(columns[j][i] for j in range(4)) for i in range(4))


def mat_vec(matrix, vector):
    return tuple(
        sum(matrix[i][j] * vector[j] for j in range(4)) % P
        for i in range(4)
    )


def mat_mul(left, right):
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(4)) % P
            for j in range(4)
        )
        for i in range(4)
    )


def mat_sub(left, right):
    return tuple(
        tuple((left[i][j] - right[i][j]) % P for j in range(4))
        for i in range(4)
    )


def mat_scalar(value):
    return tuple(
        tuple((value if i == j else 0) % P for j in range(4))
        for i in range(4)
    )


def mat_pow(matrix, exponent):
    result = mat_scalar(1)
    base = matrix
    power = exponent
    while power:
        if power & 1:
            result = mat_mul(result, base)
        base = mat_mul(base, base)
        power >>= 1
    return result


def mat_order(matrix, limit=100):
    current = mat_scalar(1)
    for exponent in range(1, limit + 1):
        current = mat_mul(current, matrix)
        if current == mat_scalar(1):
            return exponent
    return 0


def int_matrix_from_columns(columns):
    return tuple(tuple(columns[j][i] for j in range(4)) for i in range(4))


def int_mat_mul(left, right):
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(4))
            for j in range(4)
        )
        for i in range(4)
    )


def int_mat_pow(matrix, exponent):
    result = tuple(tuple(1 if i == j else 0 for j in range(4)) for i in range(4))
    base = matrix
    power = exponent
    while power:
        if power & 1:
            result = int_mat_mul(result, base)
        base = int_mat_mul(base, base)
        power >>= 1
    return result


def det_int(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    total = 0
    for column, coefficient in enumerate(matrix[0]):
        minor = tuple(
            tuple(row[j] for j in range(len(matrix)) if j != column)
            for row in matrix[1:]
        )
        total += (-1 if column & 1 else 1) * coefficient * det_int(minor)
    return total


def v2(value):
    exponent = 0
    while value % 2 == 0:
        value //= 2
        exponent += 1
    return exponent


def step(vector):
    a, b, c, d = vector
    return (
        (a - c + d) % P,
        (b - c) % P,
        a % P,
        (b - c + d) % P,
    )


checks = []


def check(label, condition):
    checks.append((label, bool(condition)))


lambda_r = tuple(value % P for value in LAMBDA)
lambda_matrix = int_matrix_from_columns(tuple(o_mul(LAMBDA, e) for e in BASIS))
residue_is_multiplicative = all(
    residue(ring_mul(e_i, e_j)) == (residue(e_i) * residue(e_j)) % P
    for e_i in BASIS
    for e_j in BASIS
)
unit_flags = tuple(any(ring_mul(x, y) == ONE for y in ALL) for x in ALL)
model_ok = len(ALL) == 625 and len(set(ALL)) == 625
model_ok &= ring_pow(lambda_r, 4) == ZERO and ring_pow(lambda_r, 3) != ZERO
model_ok &= residue_is_multiplicative
model_ok &= all(unit == (residue(x) != 0) for x, unit in zip(ALL, unit_flags))
model_ok &= sum(unit_flags) == 500 and abs(det_int(lambda_matrix)) == 5
check(
    "01 MODEL        R=A_4 has 625 elements; lambda^4=0!=lambda^3; residue and the unit criterion are exact; |R*|=500",
    model_ok,
)


j_powers = tuple(ring_pow(J, exponent) for exponent in range(20))
cycle_ok = ring_pow(J, 5) == scalar(2)
cycle_ok &= ring_pow(J, 10) == scalar(4)
cycle_ok &= ring_pow(J, 15) == scalar(3)
cycle_ok &= ring_pow(J, 20) == ONE
cycle_ok &= ring_order(J) == 20 and len(set(j_powers)) == 20
check(
    "02 CYCLE        J^5=2, J^10=-1, J^15=3, and the exact order of J in R is 20",
    cycle_ok,
)


t_part = ring_pow(J, 5)
u_part = ring_pow(J, 16)
nilpotent = ring_sub(u_part, ONE)
t_group = {ring_pow(t_part, exponent) for exponent in range(4)}
u_group = {ring_pow(u_part, exponent) for exponent in range(5)}
products = {
    ring_mul(ring_pow(t_part, a), ring_pow(u_part, b))
    for a in range(4)
    for b in range(5)
}
split_ok = t_part == scalar(2) and u_part == ring_mul(scalar(3), J)
split_ok &= ring_order(t_part) == 4 and ring_order(u_part) == 5
split_ok &= ring_pow(nilpotent, 4) == ZERO and ring_pow(nilpotent, 3) != ZERO
split_ok &= ring_mul(t_part, u_part) == J
split_ok &= t_group & u_group == {ONE}
split_ok &= products == set(j_powers) and len(products) == 20
check(
    "03 SPLIT        t=J^5 and u=J^16=3J have orders 4 and 5; u-1 has index 4; J=tu and <J>=<t> x <u>",
    split_ok,
)


constants = {scalar(value) for value in range(1, P)}
roots4 = {x for x in ALL if ring_pow(x, 4) == ONE}
roots8 = {x for x in ALL if ring_pow(x, 8) == ONE}
exact8 = {x for x in ALL if ring_pow(x, 8) == ONE and ring_pow(x, 4) != ONE}
roots_ok = roots4 == constants and roots8 == constants and not exact8
check(
    "04 ROOTS-R      over all 625 elements, mu_8(R)=mu_4(R)=F_5* as the four nonzero constants; R has no order-8 element",
    roots_ok,
)


depth_ok = abs(det_int(lambda_matrix)) == 5
for m in range(1, 17):
    carrier_size = abs(det_int(int_mat_pow(lambda_matrix, m)))
    unit_count = 4 * 5 ** (m - 1)
    depth_ok &= carrier_size == 5 ** m
    depth_ok &= unit_count == 4 * (carrier_size // 5)
    depth_ok &= v2(unit_count) == 2 and unit_count % 8 == 4
depth_ok &= 4 * 5 ** 3 == sum(unit_flags)
check(
    "05 DEPTH        det(m_lambda)=5 audits |A_m|=5^m; the proved 5-group kernel leaves 2-primary C_4 and no order 8 at any m",
    depth_ok,
)


step_matrix = matrix_from_columns(tuple(step(e) for e in BASIS))
ring_matrix = matrix_from_columns(tuple(ring_mul(J, e) for e in BASIS))
matrix_ok = step_matrix == ring_matrix
matrix_ok &= all(
    mat_vec(step_matrix, vector) == step(vector) == ring_mul(J, vector)
    for vector in ALL
)
for exponent in range(20):
    matrix_power = mat_pow(step_matrix, exponent)
    ring_power = ring_pow(J, exponent)
    for e in BASIS:
        matrix_ok &= mat_vec(matrix_power, e) == ring_mul(ring_power, e)
matrix_u = mat_pow(step_matrix, 16)
matrix_nilpotent = mat_sub(matrix_u, mat_scalar(1))
matrix_jordan = mat_sub(step_matrix, mat_scalar(2))
matrix_ok &= mat_order(step_matrix) == 20
matrix_ok &= mat_pow(step_matrix, 5) == mat_scalar(2)
matrix_ok &= mat_pow(step_matrix, 10) == mat_scalar(4)
matrix_ok &= matrix_u == mat_mul(mat_scalar(3), step_matrix)
matrix_ok &= mat_order(matrix_u) == 5
matrix_ok &= mat_pow(matrix_nilpotent, 4) == mat_scalar(0)
matrix_ok &= mat_pow(matrix_nilpotent, 3) != mat_scalar(0)
matrix_ok &= mat_pow(matrix_jordan, 4) == mat_scalar(0)
matrix_ok &= mat_pow(matrix_jordan, 3) != mat_scalar(0)
check(
    "06 MATRIX       M_R is built from step(e_i); all 625 vectors and all four columns through k=19 agree with the independent ring action and matrix split",
    matrix_ok,
)


passed = sum(result for _, result in checks)
lines = [("PASS " if result else "FAIL ") + label for label, result in checks]
if passed == len(checks):
    lines.append(f"RESULT {passed}/{len(checks)} ALL PASS")
else:
    lines.append(f"RESULT {passed}/{len(checks)} FAILURES PRESENT")
sys.stdout.buffer.write(("\n".join(lines) + "\n").encode("ascii"))
raise SystemExit(0 if passed == len(checks) else 1)
