#!/usr/bin/env python3
"""Exact audit for P-J-PLENUM-POLAR-GAUSS-1.

Standard library only. Exact integer, Fraction, and Q(sqrt(5)) arithmetic.
No float, builtin complex arithmetic, file input, network, subprocess,
randomness, clock, dynamic import, eval, exec, or environment input.

The universal implications are proved in PREREG.md. This verifier rebuilds
and audits their finite exact premises from the displayed inputs.
"""

from fractions import Fraction


PROBE = "P-J-PLENUM-POLAR-GAUSS-1"
CLAIM_A = "J-PLENUM-POLAR-GAUSS"
CLAIM_B = "J-PLENUM-POLAR-ORBIT-SEPARATION"

FAILURES = []
OUTPUT = []


def require(condition, message):
    """Reserve exceptions and nonzero process status for integrity STOP."""
    if not condition:
        raise RuntimeError("STOP: " + message)


def gate(code, label, condition, detail):
    """Record one completed exact scientific gate."""
    status = "PASS" if condition else "FAIL"
    if not condition:
        FAILURES.append(code)
    shown = detail if condition else "falsifier=%s" % code
    OUTPUT.append("CHECK %s %s %s %s" % (code, label, status, shown))


# ---------------------------------------------------------------------------
# Exact rational vectors and matrices


def zero_matrix(rows, columns):
    return [[Fraction(0) for _ in range(columns)] for _ in range(rows)]


def identity(size):
    out = zero_matrix(size, size)
    for index in range(size):
        out[index][index] = Fraction(1)
    return out


def transpose(matrix):
    require(matrix, "empty transpose")
    require(all(len(row) == len(matrix[0]) for row in matrix), "ragged transpose")
    return [list(column) for column in zip(*matrix)]


def matmul(left, right):
    require(left and right, "empty matrix product")
    require(len(left[0]) == len(right), "matrix product shape")
    require(all(len(row) == len(left[0]) for row in left), "ragged left matrix")
    require(all(len(row) == len(right[0]) for row in right), "ragged right matrix")
    out = []
    for row in left:
        out_row = []
        for column in zip(*right):
            out_row.append(
                sum(
                    (Fraction(a) * Fraction(b) for a, b in zip(row, column)),
                    Fraction(0),
                )
            )
        out.append(out_row)
    return out


def matadd(left, right):
    require(len(left) == len(right), "matrix sum rows")
    require(all(len(a) == len(b) for a, b in zip(left, right)), "matrix sum columns")
    return [
        [Fraction(a) + Fraction(b) for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]


def matscale(matrix, scalar):
    scalar = Fraction(scalar)
    return [[scalar * Fraction(value) for value in row] for row in matrix]


def matsub(left, right):
    return matadd(left, matscale(right, -1))


def matpow(matrix, exponent):
    require(exponent >= 0, "negative matrix power")
    require(matrix and all(len(row) == len(matrix) for row in matrix), "matrix power shape")
    result = identity(len(matrix))
    factor = [[Fraction(value) for value in row] for row in matrix]
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = matmul(result, factor)
        factor = matmul(factor, factor)
        remaining >>= 1
    return result


def matvec(matrix, vector):
    require(all(len(row) == len(vector) for row in matrix), "matrix-vector shape")
    return [
        sum((Fraction(a) * Fraction(b) for a, b in zip(row, vector)), Fraction(0))
        for row in matrix
    ]


def determinant(matrix):
    size = len(matrix)
    require(size > 0 and all(len(row) == size for row in matrix), "determinant shape")
    work = [[Fraction(value) for value in row] for row in matrix]
    value = Fraction(1)
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            value = -value
        pivot_value = work[column][column]
        value *= pivot_value
        for row in range(column + 1, size):
            if work[row][column] == 0:
                continue
            factor = work[row][column] / pivot_value
            for entry in range(column, size):
                work[row][entry] -= factor * work[column][entry]
    return value


def vector_add(left, right):
    require(len(left) == len(right), "vector sum shape")
    return [Fraction(a) + Fraction(b) for a, b in zip(left, right)]


def vector_scale(vector, scalar):
    return [Fraction(scalar) * Fraction(value) for value in vector]


def quadratic_norm(vector):
    return sum((Fraction(value) * Fraction(value) for value in vector), Fraction(0))


def restriction_to_v(action):
    """Matrix on f_j=e_j-e_4; coordinates are the first four entries."""
    require(len(action) == 5 and all(len(row) == 5 for row in action), "V restriction shape")
    columns = []
    for index in range(4):
        basis = [Fraction(0) for _ in range(5)]
        basis[index] = Fraction(1)
        basis[4] = Fraction(-1)
        image = matvec(action, basis)
        if sum(image, Fraction(0)) != 0 or image[4] != -sum(image[:4], Fraction(0)):
            return None
        columns.append(image[:4])
    return [[columns[column][row] for column in range(4)] for row in range(4)]


def matrix_l1(matrix):
    return sum((abs(value) for row in matrix for value in row), Fraction(0))


# ---------------------------------------------------------------------------
# Q(sqrt(5)) as pairs a+b*s, s^2=5


QS_ZERO = (Fraction(0), Fraction(0))
QS_ONE = (Fraction(1), Fraction(0))
QS_S = (Fraction(0), Fraction(1))


def qs(value):
    if isinstance(value, tuple):
        require(len(value) == 2, "Qsqrt tuple length")
        return (Fraction(value[0]), Fraction(value[1]))
    if isinstance(value, list):
        require(len(value) == 2, "Qsqrt list length")
        return (Fraction(value[0]), Fraction(value[1]))
    return (Fraction(value), Fraction(0))


def qs_add(left, right):
    left = qs(left)
    right = qs(right)
    return (left[0] + right[0], left[1] + right[1])


def qs_neg(value):
    value = qs(value)
    return (-value[0], -value[1])


def qs_sub(left, right):
    return qs_add(left, qs_neg(right))


def qs_mul(left, right):
    left = qs(left)
    right = qs(right)
    return (
        left[0] * right[0] + Fraction(5) * left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def qs_pow(value, exponent):
    require(exponent >= 0, "negative Qsqrt power")
    result = QS_ONE
    factor = qs(value)
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = qs_mul(result, factor)
        factor = qs_mul(factor, factor)
        remaining >>= 1
    return result


def qs_sum(values):
    total = QS_ZERO
    for value in values:
        total = qs_add(total, value)
    return total


def qs_lift_matrix(matrix):
    return [[qs(value) for value in row] for row in matrix]


def qs_zero_matrix(rows, columns):
    return [[QS_ZERO for _ in range(columns)] for _ in range(rows)]


def qs_identity(size):
    return qs_lift_matrix(identity(size))


def qs_transpose(matrix):
    require(matrix, "empty Qsqrt transpose")
    require(all(len(row) == len(matrix[0]) for row in matrix), "ragged Qsqrt transpose")
    return [list(column) for column in zip(*matrix)]


def qs_matmul(left, right):
    require(left and right, "empty Qsqrt matrix product")
    require(len(left[0]) == len(right), "Qsqrt matrix product shape")
    require(all(len(row) == len(left[0]) for row in left), "ragged Qsqrt left")
    require(all(len(row) == len(right[0]) for row in right), "ragged Qsqrt right")
    out = []
    for row in left:
        out_row = []
        for column in zip(*right):
            out_row.append(qs_sum(qs_mul(a, b) for a, b in zip(row, column)))
        out.append(out_row)
    return out


def qs_matadd(left, right):
    require(len(left) == len(right), "Qsqrt matrix sum rows")
    require(all(len(a) == len(b) for a, b in zip(left, right)), "Qsqrt matrix sum columns")
    return [
        [qs_add(a, b) for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]


def qs_matscale(matrix, scalar):
    return [[qs_mul(value, scalar) for value in row] for row in matrix]


def qs_matsub(left, right):
    return qs_matadd(left, qs_matscale(right, -1))


def qs_matpow(matrix, exponent):
    require(exponent >= 0, "negative Qsqrt matrix power")
    require(matrix and all(len(row) == len(matrix) for row in matrix), "Qsqrt power shape")
    result = qs_identity(len(matrix))
    factor = [[qs(value) for value in row] for row in matrix]
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = qs_matmul(result, factor)
        factor = qs_matmul(factor, factor)
        remaining >>= 1
    return result


def qs_matvec(matrix, vector):
    require(all(len(row) == len(vector) for row in matrix), "Qsqrt matrix-vector shape")
    return [qs_sum(qs_mul(a, b) for a, b in zip(row, vector)) for row in matrix]


def qs_quadratic_norm(vector):
    return qs_sum(qs_mul(value, value) for value in vector)


def qs_restriction_to_v(action):
    require(len(action) == 5 and all(len(row) == 5 for row in action), "Qsqrt V restriction shape")
    columns = []
    for index in range(4):
        basis = [QS_ZERO for _ in range(5)]
        basis[index] = QS_ONE
        basis[4] = qs(-1)
        image = qs_matvec(action, basis)
        if qs_sum(image) != QS_ZERO or image[4] != qs_neg(qs_sum(image[:4])):
            return None
        columns.append(image[:4])
    return [[columns[column][row] for column in range(4)] for row in range(4)]


def qs_matrix_key(matrix):
    return tuple(value for row in matrix for value in row)


def qs_projective_sign_key(matrix):
    key = qs_matrix_key(matrix)
    negative_key = qs_matrix_key(qs_matscale(matrix, -1))
    return min(key, negative_key)


def qs_is_scalar_matrix(matrix):
    size = len(matrix)
    require(size > 0 and all(len(row) == size for row in matrix), "scalar test shape")
    diagonal = matrix[0][0]
    return all(
        matrix[row][column] == (diagonal if row == column else QS_ZERO)
        for row in range(size)
        for column in range(size)
    )


# ---------------------------------------------------------------------------
# Frozen construction


I5 = identity(5)
G = zero_matrix(5, 5)
for column in range(5):
    G[(column + 1) % 5][column] = Fraction(1)

G2 = matpow(G, 2)
G3 = matpow(G, 3)
G4 = matpow(G, 4)
N = zero_matrix(5, 5)
for power in range(5):
    N = matadd(N, matpow(G, power))

P0 = matscale(N, Fraction(1, 5))
PV = matsub(I5, P0)
J = matadd(I5, G2)
GAMMA = matsub(matadd(G, G4), matadd(G2, G3))
A = matmul(G, GAMMA)
D = matsub(matscale(I5, 5), N)

S = zero_matrix(5, 5)
for column in range(5):
    S[(3 * column) % 5][column] = Fraction(1)
S_INV = matpow(S, 3)

QI5 = qs_lift_matrix(I5)
QPV = qs_lift_matrix(PV)
QJ = qs_lift_matrix(J)
QG = qs_lift_matrix(G)
QG2 = qs_lift_matrix(G2)
QGAMMA = qs_lift_matrix(GAMMA)
QS_MATRIX = qs_lift_matrix(S)
QS_INV_MATRIX = qs_lift_matrix(S_INV)

# 1/s=s/5 and 1/(2s)=s/10 in Q(s), s^2=5.
H = qs_matscale(QGAMMA, (0, Fraction(1, 5)))
U = qs_matmul(QG, H)
B = qs_matscale(qs_matsub(qs_matscale(QI5, 5), QGAMMA), (0, Fraction(1, 10)))
B_PLUS = qs_matscale(qs_matadd(qs_matscale(QI5, 5), QGAMMA), (0, Fraction(1, 10)))
B_V = qs_matmul(B, QPV)
B_INV_V = qs_matmul(B_PLUS, QPV)

P_PLUS = qs_matscale(qs_matadd(QPV, H), Fraction(1, 2))
P_MINUS = qs_matscale(qs_matsub(QPV, H), Fraction(1, 2))
PHI = (Fraction(1, 2), Fraction(1, 2))
PHI_INV = (Fraction(-1, 2), Fraction(1, 2))


# ---------------------------------------------------------------------------
# Sixteen exact gates


OUTPUT.append("SPEC J_PLENUM_POLAR_GAUSS_EXACT_V1")
OUTPUT.append("MODE RESULT-EXPOSED PROOF-FIRST")

g01 = (
    matpow(G, 5) == I5
    and all(matpow(G, exponent) != I5 for exponent in range(1, 5))
    and matmul(G, N) == N
    and matmul(N, N) == matscale(N, 5)
    and matmul(PV, PV) == PV
    and transpose(PV) == PV
    and matmul(PV, N) == zero_matrix(5, 5)
    and restriction_to_v(G) is not None
)
gate("G01", "CARRIER", g01, "g_order=5 rank_V=4 projector=exact")

D_V = restriction_to_v(D)
g02 = (
    D_V is not None
    and determinant(D_V) == 125
    and matmul(D, N) == zero_matrix(5, 5)
    and matmul(D, D) == matscale(D, 5)
    and matmul(D, J) == matmul(J, D)
    and all(
        all((D[row][column] - D[0][column]).numerator % 5 == 0 for row in range(5))
        for column in range(5)
    )
)
gate("G02", "CENTERING", g02, "kernel=ZN image=equal_mod_5 index=125")

J_V = restriction_to_v(J)
g03 = (
    J_V is not None
    and matmul(J, N) == matscale(N, 2)
    and determinant(J) == 2
    and determinant(J_V) == 1
    and all(sum((J[row][column] for row in range(5)), Fraction(0)) == 2 for column in range(5))
)
gate("G03", "RAW_J", g03, "augmentation_multiplier=2 det_full=2 det_V=1")

g04 = (
    transpose(GAMMA) == GAMMA
    and matmul(GAMMA, N) == zero_matrix(5, 5)
    and matmul(GAMMA, GAMMA) == D
    and matsub(matscale(J, 2), matmul(G, matsub(GAMMA, I5))) == N
)
gate("G04", "INTEGRAL_GAUSS", g04, "GammaN=0 Gamma2=5I-N quotient_identity=safe")

QZERO5 = qs_zero_matrix(5, 5)
g05 = (
    qs_transpose(H) == H
    and qs_matmul(H, H) == QPV
    and qs_matmul(P_PLUS, P_PLUS) == P_PLUS
    and qs_matmul(P_MINUS, P_MINUS) == P_MINUS
    and qs_matmul(P_PLUS, P_MINUS) == QZERO5
    and qs_matadd(P_PLUS, P_MINUS) == QPV
    and qs_matadd(P_PLUS, qs_matscale(P_MINUS, -1)) == H
)
gate("G05", "GAUSS_SECTORS", g05, "H2=P_V projectors=orthogonal_complete")

U_V = qs_restriction_to_v(U)
QI4 = qs_identity(4)
g06 = (
    U_V is not None
    and qs_matmul(qs_transpose(U), U) == QPV
    and qs_matmul(U, qs_transpose(U)) == QPV
    and qs_matpow(U, 2) == qs_matmul(QG2, QPV)
    and qs_matpow(U, 5) == H
    and qs_matpow(U, 10) == QPV
    and qs_matpow(U_V, 10) == QI4
    and all(qs_matpow(U_V, exponent) != QI4 for exponent in range(1, 10))
)
gate("G06", "NORMALIZED_MIXER", g06, "U5=A/sqrt5 unitary_on_V order=10")

spectral_b = qs_matadd(qs_matscale(P_PLUS, PHI_INV), qs_matscale(P_MINUS, PHI))
spectral_b_inv = qs_matadd(qs_matscale(P_PLUS, PHI), qs_matscale(P_MINUS, PHI_INV))
g07 = (
    qs_mul(PHI, PHI_INV) == QS_ONE
    and 2 * 2 < 5 < 3 * 3
    and qs_transpose(B) == B
    and B_V == spectral_b
    and B_INV_V == spectral_b_inv
    and qs_matmul(B_V, B_INV_V) == QPV
    and qs_matmul(B_INV_V, B_V) == QPV
)
gate("G07", "POSITIVE_BOOST", g07, "eigenvalues=phi^-1,phi positive_on_V=yes")

QJTJ = qs_lift_matrix(matmul(transpose(J), J))
FULL_POLAR_TARGET = qs_matsub(QJ, qs_matscale(qs_lift_matrix(N), Fraction(2, 5)))
g08 = (
    qs_matmul(B_V, B_V) == qs_matmul(QJTJ, QPV)
    and qs_matmul(U, B) == FULL_POLAR_TARGET
    and qs_matmul(B, U) == FULL_POLAR_TARGET
    and qs_matmul(U, B_V) == qs_matmul(QJ, QPV)
)
gate("G08", "POLAR", g08, "B2=JstarJ_on_V J=U5B=BU5 full_correction=2N/5")

g09 = (
    matmul(S, matmul(G, S_INV)) == G3
    and qs_matmul(QS_MATRIX, qs_matmul(H, QS_INV_MATRIX)) == qs_matscale(H, -1)
    and qs_matmul(QS_MATRIX, qs_matmul(B_V, QS_INV_MATRIX)) == B_INV_V
    and qs_matmul(QS_MATRIX, qs_matmul(U, QS_INV_MATRIX)) == qs_matscale(qs_matpow(U, 3), -1)
)
gate("G09", "GALOIS", g09, "g_to_g3 H_to_minusH B_to_Binv U5_to_minusU5cubed")

S_V_RATIONAL = restriction_to_v(S)
require(S_V_RATIONAL is not None, "Galois restriction missing")
S_V = qs_lift_matrix(S_V_RATIONAL)

normal_forms = []
for epsilon in range(2):
    for exponent_u in range(10):
        for exponent_s in range(4):
            form = qs_matmul(qs_matpow(U_V, exponent_u), qs_matpow(S_V, exponent_s))
            normal_forms.append(qs_matscale(form, -1 if epsilon else 1))

seen = {qs_matrix_key(QI4): QI4}
frontier = [QI4]
overflow = False
while frontier and not overflow:
    current = frontier.pop(0)
    for generator in (U_V, S_V):
        image = qs_matmul(current, generator)
        key = qs_matrix_key(image)
        if key not in seen:
            seen[key] = image
            frontier.append(image)
            if len(seen) > 160:
                overflow = True
                break

scalar_values = {
    matrix[0][0]
    for matrix in seen.values()
    if qs_is_scalar_matrix(matrix)
}
projective_keys = {qs_projective_sign_key(matrix) for matrix in seen.values()}
minus_identity = qs_matscale(QI4, -1)
minus_word = qs_matmul(
    qs_matpow(U_V, 3),
    qs_matmul(qs_matpow(S_V, 3), qs_matmul(U_V, S_V)),
)
g10 = (
    not overflow
    and len(normal_forms) == 80
    and len({qs_matrix_key(matrix) for matrix in normal_forms}) == 80
    and len(seen) == 80
    and set(seen) == {qs_matrix_key(matrix) for matrix in normal_forms}
    and scalar_values == {qs(-1), QS_ONE}
    and len(projective_keys) == 40
    and minus_word == minus_identity
    and qs_matmul(S_V, qs_matmul(U_V, qs_matpow(S_V, 3)))
    == qs_matscale(qs_matpow(U_V, 3), -1)
    and qs_matpow(S_V, 4) == QI4
    and all(qs_matpow(S_V, exponent) not in (QI4, minus_identity) for exponent in range(1, 4))
    and all(qs_matpow(U_V, exponent) not in (QI4, minus_identity) for exponent in range(1, 10))
)
gate("G10", "MARKED_GROUP", g10, "linear=80 scalar_kernel=2 projective=40 type=C10_semidirect_3_C4")

g11 = (
    A == matsub(matadd(I5, G2), matadd(G3, G4))
    and matmul(A, A) == matsub(matscale(G2, 5), N)
    and matmul(transpose(A), A) == D
    and sum(1 for value in (1, 0, 1, -1, -1) if value != 0) == 4
    and matrix_l1(matmul(A, A)) == 40
)
gate("G11", "INTEGER_MIXER", g11, "A2=5g2-N norm_multiplier=5 signed_words=4^n")

D0 = [Fraction(4), Fraction(-1), Fraction(-1), Fraction(-1), Fraction(-1)]
HOLE = [Fraction(5), Fraction(0), Fraction(5), Fraction(-5), Fraction(-5)]
orbit_ok = True
for exponent in range(10):
    actual = matvec(matpow(A, exponent), D0)
    if exponent % 2 == 0:
        half = exponent // 2
        expected = vector_scale(matvec(matpow(G, 2 * half), D0), 5 ** half)
    else:
        half = (exponent - 1) // 2
        expected = vector_scale(matvec(matpow(G, 2 * half), HOLE), 5 ** half)
    orbit_ok = orbit_ok and actual == expected

g12 = (
    sum(D0, Fraction(0)) == 0
    and D0 == [D[row][0] for row in range(5)]
    and matvec(A, D0) == HOLE
    and orbit_ok
    and all(
        quadratic_norm(matvec(matpow(A, exponent), D0)) == (5 ** exponent) * 20
        for exponent in range(10)
    )
    and [value * value for value in D0] == [16, 1, 1, 1, 1]
    and [value * value for value in HOLE] == [25, 0, 25, 25, 25]
)
gate("G12", "SUPPORTED_ORBIT", g12, "vertex=16,1,1,1,1 hole=25,0,25,25,25 period=10")

raw_orbits = [matvec(matpow(J, exponent), D0) for exponent in range(9)]
raw_formula_ok = True
raw_residue_ok = True
for exponent, actual in enumerate(raw_orbits):
    source = [Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)]
    expanded = matvec(matpow(J, exponent), source)
    expected = vector_add(vector_scale(expanded, 5), vector_scale([1, 1, 1, 1, 1], -(2 ** exponent)))
    raw_formula_ok = raw_formula_ok and actual == expected
    residue = (-pow(2, exponent, 5)) % 5
    raw_residue_ok = raw_residue_ok and all(int(value) % 5 == residue for value in actual)

g13 = (
    raw_formula_ok
    and raw_residue_ok
    and all(all(value != 0 for value in orbit) for orbit in raw_orbits)
    and raw_orbits[8] == [29, 29, -76, 94, -76]
)
gate("G13", "RAW_ORBIT", g13, "formula=5(1+g2)^n_e0-2^nN zero_cells=none n8=29,29,-76,94,-76")

raw_norms = [quadratic_norm(vector) for vector in raw_orbits]
expected_raw_norms = [20, 30, 70, 180, 470, 1230, 3220, 8430, 22070]
phi_formula_ok = all(
    qs(raw_norms[exponent])
    == qs_mul(10, qs_add(qs_pow(PHI, 2 * exponent), qs_pow(PHI_INV, 2 * exponent)))
    for exponent in range(9)
)
g14 = (
    raw_norms == expected_raw_norms
    and all(raw_norms[index + 2] == 3 * raw_norms[index + 1] - raw_norms[index] for index in range(7))
    and phi_formula_ok
)
gate("G14", "RAW_NORMS", g14, "q=20,30,70,180,470,1230,3220,8430,22070 recurrence=3q1-q0")

QD0 = [qs(value) for value in D0]
plus_d0 = qs_matvec(P_PLUS, QD0)
minus_d0 = qs_matvec(P_MINUS, QD0)
g15 = (
    qs_matmul(B_V, P_PLUS) == qs_matscale(P_PLUS, PHI_INV)
    and qs_matmul(B_V, P_MINUS) == qs_matscale(P_MINUS, PHI)
    and qs_matmul(U, P_PLUS) == qs_matmul(P_PLUS, U)
    and qs_matmul(U, P_MINUS) == qs_matmul(P_MINUS, U)
    and qs_quadratic_norm(plus_d0) == qs(10)
    and qs_quadratic_norm(minus_d0) == qs(10)
)
gate("G15", "PLANE_SEPARATION", g15, "Pplus_scale=phi^-1 Pminus_scale=phi ratio_multiplier=phi^4")

boost_d0 = qs_matvec(B, QD0)
raw_d0 = matvec(J, D0)
D1 = [Fraction(1), Fraction(-1), Fraction(0), Fraction(0), Fraction(0)]
raw_d1 = matvec(J, D1)
A_V = restriction_to_v(A)
g16 = (
    boost_d0 == [(0, 2), (0, -1), (0, 0), (0, 0), (0, -1)]
    and [qs_mul(value, value) for value in boost_d0] == [qs(20), qs(5), QS_ZERO, QS_ZERO, qs(5)]
    and raw_d0 == [3, -2, 3, -2, -2]
    and [value * value for value in raw_d0] == [9, 4, 9, 4, 4]
    and quadratic_norm(raw_d0) * quadratic_norm(D1) == 3 * quadratic_norm(D0)
    and quadratic_norm(raw_d1) == 2 * quadratic_norm(D1)
    and A_V is not None
    and J_V != A_V
    and U_V != qs_lift_matrix(J_V)
    and U_V != qs_lift_matrix(A_V)
)
gate("G16", "ORBIT_SEPARATION", g16, "boost_profile=20,5,0,0,5 raw_profile=9,4,9,4,4 J_ratios=3/2,2")


# ---------------------------------------------------------------------------
# Frozen claim decision


CLAIM_A_GATES = {"G%02d" % index for index in range(1, 11)}
CLAIM_B_GATES = {"G01", "G03", "G04", "G05", "G06", "G07", "G08", "G09"} | {
    "G%02d" % index for index in range(11, 17)
}
failed = set(FAILURES)
claim_a_status = "CONFIRMED" if not (failed & CLAIM_A_GATES) else "FIRED"
claim_b_status = "CONFIRMED" if not (failed & CLAIM_B_GATES) else "FIRED"

for line in OUTPUT:
    print(line)
print("RESULT CLAIM_A %s %s" % (CLAIM_A, claim_a_status))
print("RESULT CLAIM_B %s %s" % (CLAIM_B, claim_b_status))
print("SCOPE born=NONE probability=NONE outcomes=NONE records=NONE action_layer=L1")
overall = "PASS" if claim_a_status == claim_b_status == "CONFIRMED" else "SCIENTIFIC-FIRED"
print("RESULT OVERALL %s gates=16 claims=2" % overall)
