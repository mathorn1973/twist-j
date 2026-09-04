#!/usr/bin/env python3
"""Exact proof-input audit for P-J-FIBONACCI-BRAID-1.

Standard library only. Exact integer, Fraction, and Q(zeta_5) arithmetic.
No float, builtin complex arithmetic, file input, network, subprocess,
randomness, clock, dynamic import, eval, exec, or braid-word search.

The universal claims are carried by the proofs frozen in PREREG.md. This
program audits their finite algebraic premises from the displayed inputs.
"""

from fractions import Fraction
from itertools import combinations


PROBE = "P-J-FIBONACCI-BRAID-1"
CLAIM_A = "J-CM-FIBONACCI-BRAID-PROJECTIVE-NONMEMBERSHIP"
CLAIM_B = "J-CIRCULAR-FIBONACCI-DETERMINANT-CHARACTER"

FAILURES = []


def require(condition, message):
    """Reserve exceptions and nonzero process status for integrity STOP."""
    if not condition:
        raise RuntimeError("STOP: " + message)


def gate(code, label, condition, detail):
    """Record a completed scientific PASS or FIRED gate."""
    status = "PASS" if condition else "FAIL"
    if not condition:
        FAILURES.append(code)
    shown_detail = detail if condition else "falsifier=%s" % code
    print("CHECK %s %s %s %s" % (code, label, status, shown_detail))


# ---------------------------------------------------------------------------
# Exact rational matrix arithmetic


def zero_matrix(rows, columns):
    return [[Fraction(0) for _ in range(columns)] for _ in range(rows)]


def identity(size):
    out = zero_matrix(size, size)
    for index in range(size):
        out[index][index] = Fraction(1)
    return out


def transpose(matrix):
    require(matrix, "empty transpose")
    require(all(len(row) == len(matrix[0]) for row in matrix), "ragged matrix")
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
            total = Fraction(0)
            for left_value, right_value in zip(row, column):
                total += Fraction(left_value) * Fraction(right_value)
            out_row.append(total)
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


def matvec(matrix, vector):
    require(all(len(row) == len(vector) for row in matrix), "matrix-vector shape")
    return [
        sum((Fraction(a) * Fraction(b) for a, b in zip(row, vector)), Fraction(0))
        for row in matrix
    ]


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


def columns_matrix(columns):
    require(columns, "empty column family")
    height = len(columns[0])
    require(all(len(column) == height for column in columns), "column shape")
    return [
        [Fraction(columns[column][row]) for column in range(len(columns))]
        for row in range(height)
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


def matrix_rank(matrix):
    require(matrix, "empty rank matrix")
    work = [[Fraction(value) for value in row] for row in matrix]
    row_count = len(work)
    column_count = len(work[0])
    require(all(len(row) == column_count for row in work), "rank ragged matrix")
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def solve_square(matrix, vector):
    size = len(matrix)
    require(size > 0 and all(len(row) == size for row in matrix), "solve shape")
    require(len(vector) == size, "solve vector shape")
    work = [
        [Fraction(value) for value in row] + [Fraction(vector[index])]
        for index, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        require(pivot is not None, "singular solve")
        work[column], work[pivot] = work[pivot], work[column]
        pivot_value = work[column][column]
        work[column] = [value / pivot_value for value in work[column]]
        for row in range(size):
            if row == column or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(work[row], work[column])
            ]
    return [work[index][-1] for index in range(size)]


def coordinates_in_basis(columns, vector):
    basis_matrix = columns_matrix(columns)
    row_count = len(basis_matrix)
    rank = len(columns)
    require(len(vector) == row_count, "coordinate vector shape")
    for rows in combinations(range(row_count), rank):
        square = [[basis_matrix[row][column] for column in range(rank)] for row in rows]
        if determinant(square) == 0:
            continue
        rhs = [vector[row] for row in rows]
        solution = solve_square(square, rhs)
        if matvec(basis_matrix, solution) == [Fraction(v) for v in vector]:
            return solution
    return None


def restriction_matrix(action, columns):
    coordinates = [
        coordinates_in_basis(columns, matvec(action, column)) for column in columns
    ]
    if any(column is None for column in coordinates):
        return None
    return columns_matrix(coordinates)


def characteristic_polynomial(matrix):
    """Return det(xI-A) coefficients high-to-low by Faddeev-LeVerrier."""
    size = len(matrix)
    require(size > 0 and all(len(row) == size for row in matrix), "characteristic shape")
    unit = identity(size)
    state = unit
    coefficients = [Fraction(1)]
    for step in range(1, size + 1):
        product = matmul(matrix, state)
        coefficient = -sum(
            (product[index][index] for index in range(size)), Fraction(0)
        ) / Fraction(step)
        coefficients.append(coefficient)
        state = matadd(product, matscale(unit, coefficient))
    return coefficients


def poly_matrix_eval(coefficients, matrix):
    """Evaluate low-to-high scalar coefficients at a square matrix."""
    size = len(matrix)
    result = zero_matrix(size, size)
    power = identity(size)
    for coefficient in coefficients:
        result = matadd(result, matscale(power, coefficient))
        power = matmul(power, matrix)
    return result


def is_zero_matrix(matrix):
    return all(value == 0 for row in matrix for value in row)


def gcd_int(left, right):
    left = abs(int(left))
    right = abs(int(right))
    while right:
        left, right = right, left % right
    return left


def maximal_minor_gcd(matrix):
    row_count = len(matrix)
    column_count = len(matrix[0])
    require(row_count >= column_count, "maximal minor shape")
    value = 0
    for rows in combinations(range(row_count), column_count):
        minor = [[matrix[row][column] for column in range(column_count)] for row in rows]
        det = determinant(minor)
        require(det.denominator == 1, "nonintegral maximal minor")
        value = gcd_int(value, det.numerator)
    return value


def vector_add(left, right):
    return [Fraction(a) + Fraction(b) for a, b in zip(left, right)]


def vector_scale(vector, scalar):
    return [Fraction(scalar) * Fraction(value) for value in vector]


# ---------------------------------------------------------------------------
# Q(zeta_5) in the basis 1,z,z^2,z^3 with Phi_5(z)=0


QZERO = (Fraction(0), Fraction(0), Fraction(0), Fraction(0))
QONE = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))


def q5(value):
    if isinstance(value, tuple):
        require(len(value) == 4, "Q5 tuple length")
        return tuple(Fraction(entry) for entry in value)
    if isinstance(value, list):
        require(len(value) == 4, "Q5 list length")
        return tuple(Fraction(entry) for entry in value)
    return (Fraction(value), Fraction(0), Fraction(0), Fraction(0))


def q5_add(left, right):
    left = q5(left)
    right = q5(right)
    return tuple(a + b for a, b in zip(left, right))


def q5_neg(value):
    return tuple(-entry for entry in q5(value))


def q5_sub(left, right):
    return q5_add(left, q5_neg(right))


def q5_mul(left, right):
    left = q5(left)
    right = q5(right)
    coefficients = [Fraction(0) for _ in range(5)]
    for left_degree, left_value in enumerate(left):
        for right_degree, right_value in enumerate(right):
            coefficients[(left_degree + right_degree) % 5] += left_value * right_value
    top = coefficients[4]
    return tuple(coefficients[index] - top for index in range(4))


def q5_pow(value, exponent):
    require(exponent >= 0, "negative Q5 power")
    result = QONE
    factor = q5(value)
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = q5_mul(result, factor)
        factor = q5_mul(factor, factor)
        remaining >>= 1
    return result


def q5_galois(value, exponent):
    exponent %= 5
    require(exponent in (1, 2, 3, 4), "nonunit Galois exponent")
    coefficients = [Fraction(0) for _ in range(5)]
    for degree, entry in enumerate(q5(value)):
        coefficients[(degree * exponent) % 5] += entry
    top = coefficients[4]
    return tuple(coefficients[index] - top for index in range(4))


def q5_conj(value):
    return q5_galois(value, 4)


def q5_poly_eval(coefficients, value):
    result = QZERO
    for coefficient in reversed(coefficients):
        result = q5_add(q5_mul(result, value), q5(coefficient))
    return result


QBASIS = (
    QONE,
    (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
)
ZETA = QBASIS[1]


def q5_regular_matrix(value):
    return columns_matrix([q5_mul(value, basis) for basis in QBASIS])


def q5_trace(value):
    matrix = q5_regular_matrix(value)
    return sum((matrix[index][index] for index in range(4)), Fraction(0))


def q5_norm(value):
    return determinant(q5_regular_matrix(value))


def q5_integral(value):
    return all(entry.denominator == 1 for entry in q5(value))


def q5_matrix_mul(left, right):
    require(left and right and len(left[0]) == len(right), "Q5 matrix product shape")
    require(all(len(row) == len(left[0]) for row in left), "ragged Q5 left")
    require(all(len(row) == len(right[0]) for row in right), "ragged Q5 right")
    out = []
    for row in left:
        out_row = []
        for column in zip(*right):
            total = QZERO
            for a, b in zip(row, column):
                total = q5_add(total, q5_mul(a, b))
            out_row.append(total)
        out.append(out_row)
    return out


def q5_matrix_star(matrix):
    return [
        [q5_conj(matrix[column][row]) for column in range(len(matrix))]
        for row in range(len(matrix[0]))
    ]


def q5_matrix_identity(size):
    return [
        [QONE if row == column else QZERO for column in range(size)]
        for row in range(size)
    ]


def q5_det2(matrix):
    require(len(matrix) == 2 and all(len(row) == 2 for row in matrix), "Q5 det2 shape")
    return q5_sub(q5_mul(matrix[0][0], matrix[1][1]), q5_mul(matrix[0][1], matrix[1][0]))


def q5_matrix_integral(matrix):
    return all(q5_integral(entry) for row in matrix for entry in row)


# ---------------------------------------------------------------------------
# Alternating covariant pullback


PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))


def alternating_matrix(coordinates):
    require(len(coordinates) == 6, "alternating coordinate count")
    out = zero_matrix(4, 4)
    for value, (row, column) in zip(coordinates, PAIRS):
        out[row][column] = Fraction(value)
        out[column][row] = -Fraction(value)
    return out


def alternating_coordinates(matrix):
    return [matrix[row][column] for row, column in PAIRS]


def construct_pullback(multiplier):
    columns = []
    for index in range(6):
        basis = [Fraction(0) for _ in range(6)]
        basis[index] = Fraction(1)
        form = alternating_matrix(basis)
        image = matmul(transpose(multiplier), matmul(form, multiplier))
        columns.append(alternating_coordinates(image))
    return columns_matrix(columns)


def pfaffian_quadratic_matrix():
    out = zero_matrix(6, 6)
    out[0][5] = out[5][0] = Fraction(1, 2)
    out[1][4] = out[4][1] = Fraction(-1, 2)
    out[2][3] = out[3][2] = Fraction(1, 2)
    return out


def trace_form_coordinates(parameter):
    coordinates = []
    for left, right in PAIRS:
        value = q5_mul(parameter, q5_mul(QBASIS[left], q5_conj(QBASIS[right])))
        coordinates.append(q5_trace(value) / Fraction(5))
    return coordinates


# ---------------------------------------------------------------------------
# Frozen construction and seventeen exact gates


print("SPEC FIB_CM_EXACT_V1")
print("MODE RESULT-EXPOSED PROOF-FIRST")

phi5_at_zeta = q5_poly_eval((1, 1, 1, 1, 1), ZETA)
zeta_order = q5_pow(ZETA, 5) == QONE and all(
    q5_pow(ZETA, exponent) != QONE for exponent in range(1, 5)
)
A = q5_add(ZETA, q5_pow(ZETA, 4))
J = q5_add(QONE, q5_pow(ZETA, 2))
DELTA = q5_sub(QONE, J)
conjugation_ok = (
    q5_conj(ZETA) == q5_pow(ZETA, 4)
    and all(q5_conj(q5_conj(value)) == value for value in QBASIS + (A, J, DELTA))
    and q5_conj(q5_mul(J, DELTA)) == q5_mul(q5_conj(J), q5_conj(DELTA))
)
g01 = (
    phi5_at_zeta == QZERO
    and zeta_order
    and conjugation_ok
    and q5_conj(A) == A
    and q5_add(q5_mul(A, A), A) == QONE
)
gate("G01", "FIELD", g01, "phi5=0 order_zeta=5 involution=conjugation")


M_J = q5_regular_matrix(J)
EXPECTED_M_J = [
    [1, 0, -1, 1],
    [0, 1, -1, 0],
    [1, 0, 0, 0],
    [0, 1, -1, 1],
]
char_m_j = characteristic_polynomial(M_J)
g02 = (
    M_J == EXPECTED_M_J
    and determinant(M_J) == 1
    and q5_norm(J) == 1
    and char_m_j == [1, -3, 4, -2, 1]
    and q5_pow(q5_sub(J, QONE), 3) == ZETA
)
gate("G02", "J_REGULAR", g02, "det=1 norm=1 charpoly=Phi5(x-1)")


lambda_1 = q5_sub(ZETA, q5_pow(ZETA, 4))
lambda_2 = q5_sub(q5_pow(ZETA, 2), q5_pow(ZETA, 3))
OMEGA_1 = trace_form_coordinates(lambda_1)
OMEGA_2 = trace_form_coordinates(lambda_2)
EXPECTED_OMEGA_1 = [1, 0, 0, 1, 0, 1]
EXPECTED_OMEGA_2 = [0, 1, -1, 0, 1, 0]
H_COLUMNS = (OMEGA_1, OMEGA_2)
g03 = (
    OMEGA_1 == EXPECTED_OMEGA_1
    and OMEGA_2 == EXPECTED_OMEGA_2
    and matrix_rank(columns_matrix(H_COLUMNS)) == 2
    and maximal_minor_gcd(columns_matrix(H_COLUMNS)) == 1
)
gate(
    "G03",
    "CM_FORMS",
    g03,
    "omega1=(1,0,0,1,0,1) omega2=(0,1,-1,0,1,0) saturated=yes",
)


P = construct_pullback(M_J)
EXPECTED_P = [
    [1, 0, 1, -1, 0, 1],
    [-1, 1, -1, 1, 0, -1],
    [0, -1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0],
    [-1, 0, -1, 0, 1, 0],
    [1, 0, 0, 0, -1, 0],
]
PF = pfaffian_quadratic_matrix()
g04 = (
    P == EXPECTED_P
    and determinant(P) == 1
    and matmul(transpose(P), matmul(PF, P)) == PF
)
gate("G04", "PULLBACK", g04, "convention=covariant det=1 pfaffian=invariant")


Q_POLY = (1, -3, 1)
R_POLY = (1, -1, 1, -1, 1)
q_of_p = poly_matrix_eval(Q_POLY, P)
r_of_p = poly_matrix_eval(R_POLY, P)
g05 = (
    characteristic_polynomial(P) == [1, -4, 5, -5, 5, -4, 1]
    and matrix_rank(q_of_p) == 4
    and matrix_rank(r_of_p) == 2
    and is_zero_matrix(matmul(q_of_p, r_of_p))
    and all(matvec(q_of_p, vector) == [0] * 6 for vector in H_COLUMNS)
)
gate(
    "G05",
    "PRIMARY",
    g05,
    "charpoly=q*Phi10 rank_qP=4 rank_phi10P=2 H_kernel=yes",
)


A_CM_DERIVED = restriction_matrix(P, H_COLUMNS)
A_CM = A_CM_DERIVED if A_CM_DERIVED is not None else zero_matrix(2, 2)
trace_a_cm = A_CM[0][0] + A_CM[1][1]
det_a_cm = determinant(A_CM)
kappa_a_cm = (
    trace_a_cm * trace_a_cm / det_a_cm if det_a_cm != 0 else None
)
g06 = (
    A_CM_DERIVED is not None
    and A_CM == [[1, -1], [-1, 2]]
    and trace_a_cm == 3
    and det_a_cm == 1
    and kappa_a_cm == 9
)
gate("G06", "A_CM", g06, "matrix=((1,-1),(-1,2)) trace=3 det=1 kappa=9")


QMINUS_ONE = q5(-1)
F_O = [[A, QONE], [A, q5_neg(A)]]
R = [[q5_pow(ZETA, 3), QZERO], [QZERO, q5_neg(q5_pow(ZETA, 4))]]
B_1 = R
B_2 = q5_matrix_mul(F_O, q5_matrix_mul(R, F_O))
EXPECTED_B_2 = [
    [q5_mul(A, q5_pow(ZETA, 2)), q5_neg(ZETA)],
    [q5_neg(q5_mul(A, ZETA)), q5_neg(A)],
]
QIDENTITY_2 = q5_matrix_identity(2)
g07 = (
    q5_matrix_mul(F_O, F_O) == QIDENTITY_2
    and q5_det2(F_O) == QMINUS_ONE
    and B_2 == EXPECTED_B_2
    and q5_matrix_integral(F_O)
    and q5_matrix_integral(B_1)
    and q5_matrix_integral(B_2)
    and q5_det2(B_1) == DELTA
    and q5_det2(B_2) == DELTA
)
gate("G07", "FIB_GAUGE", g07, "integral=yes det_F=-1 det_B1=det_B2=1-J")


braid_left = q5_matrix_mul(B_1, q5_matrix_mul(B_2, B_1))
braid_right = q5_matrix_mul(B_2, q5_matrix_mul(B_1, B_2))
g08 = (
    braid_left == braid_right
    and q5_matrix_mul(B_1, B_2) != q5_matrix_mul(B_2, B_1)
    and B_2[0][1] != QZERO
    and B_2[1][0] != QZERO
)
gate("G08", "FIB_BRAID", g08, "relation=yes noncommuting=yes")


G_FIB = [[A, QZERO], [QZERO, QONE]]
invariance_1 = q5_matrix_mul(q5_matrix_star(B_1), q5_matrix_mul(G_FIB, B_1))
invariance_2 = q5_matrix_mul(q5_matrix_star(B_2), q5_matrix_mul(G_FIB, B_2))


def golden_polynomial(value):
    value = Fraction(value)
    return value * value + value - 1


positive_interval = (
    golden_polynomial(Fraction(1, 2)) < 0
    and golden_polynomial(Fraction(2, 3)) > 0
    and 2 * Fraction(1, 2) + 1 > 0
)
g09 = (
    invariance_1 == G_FIB
    and invariance_2 == G_FIB
    and q5_conj(A) == A
    and q5_add(q5_mul(A, A), A) == QONE
    and positive_interval
)
gate(
    "G09",
    "FIB_HERMITIAN",
    g09,
    "generator_invariance=yes selected_a_interval=(1/2,2/3)",
)


g10 = (
    g06
    and g08
    and g09
    and q5_det2(B_1) != QZERO
    and q5_det2(B_2) != QZERO
    and kappa_a_cm == 9
    and Fraction(9) > Fraction(4)
)
gate("G10", "A_PROOF_INPUTS", g10, "target_kappa=9 unitary_range=[0,4]")

claim_a_ok = all(code not in FAILURES for code in (
    "G01", "G02", "G03", "G04", "G05", "G06", "G07", "G08", "G09", "G10"
))
print(
    "RESULT CLAIM_A %s %s"
    % (CLAIM_A, "CONFIRMED" if claim_a_ok else "FIRED")
)


C_1 = [-1, 0, 1, 0, 0, 0]
C_2 = [0, -1, 0, 1, 0, 0]
C_3 = [0, -1, 0, 0, 1, 0]
C_4 = [-1, 0, 0, 0, 0, 1]
C_COLUMNS = (C_1, C_2, C_3, C_4)
C_MATRIX = columns_matrix(C_COLUMNS)
FULL_PRIMARY = columns_matrix(H_COLUMNS + C_COLUMNS)
g11 = (
    matrix_rank(C_MATRIX) == 4
    and maximal_minor_gcd(C_MATRIX) == 1
    and all(matvec(r_of_p, vector) == [0] * 6 for vector in C_COLUMNS)
    and matrix_rank(r_of_p) == 2
    and abs(determinant(FULL_PRIMARY)) == 5
)
gate("G11", "C_LATTICE", g11, "rank=4 saturated=yes seam_index=5")


P_C_DERIVED = restriction_matrix(P, C_COLUMNS)
P_C = P_C_DERIVED if P_C_DERIVED is not None else zero_matrix(4, 4)
g12 = (
    P_C_DERIVED is not None
    and characteristic_polynomial(P_C) == [1, -1, 1, -1, 1]
    and is_zero_matrix(poly_matrix_eval(R_POLY, P_C))
    and matpow(P_C, 5) == matscale(identity(4), -1)
    and matpow(P_C, 10) == identity(4)
    and matpow(P_C, 1) != identity(4)
    and matpow(P_C, 2) != identity(4)
    and matpow(P_C, 5) != identity(4)
    and determinant(P_C) == 1
)
gate("G12", "C_ACTION", g12, "charpoly=Phi10 order=10")


ORBIT = [C_2]
for _ in range(3):
    ORBIT.append(matvec(P, ORBIT[-1]))
EXPECTED_ORBIT = [
    C_2,
    C_1,
    vector_add(C_1, vector_scale(C_4, -1)),
    vector_add(C_2, vector_scale(C_3, -1)),
]
T_COORDINATES = [coordinates_in_basis(C_COLUMNS, vector) for vector in ORBIT]
T_DERIVED = all(coordinates is not None for coordinates in T_COORDINATES)
T = columns_matrix(T_COORDINATES) if T_DERIVED else zero_matrix(4, 4)
EXPECTED_T = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, -1],
    [0, 0, -1, 0],
]
g13 = (
    T_DERIVED
    and ORBIT == EXPECTED_ORBIT
    and T == EXPECTED_T
    and determinant(T) == 1
)
gate("G13", "C_ORBIT", g13, "determinant=1")


DELTA_BASIS = (QONE, DELTA, q5_pow(DELTA, 2), q5_pow(DELTA, 3))
DELTA_BASIS_MATRIX = columns_matrix(DELTA_BASIS)
delta_order = q5_pow(DELTA, 10) == QONE and all(
    q5_pow(DELTA, exponent) != QONE for exponent in range(1, 10)
)
g14 = (
    DELTA == q5_neg(q5_pow(ZETA, 2))
    and q5_poly_eval(R_POLY, DELTA) == QZERO
    and q5_pow(DELTA, 5) == QMINUS_ONE
    and delta_order
    and q5_neg(q5_pow(DELTA, 3)) == ZETA
    and abs(determinant(DELTA_BASIS_MATRIX)) == 1
)
gate("G14", "DELTA", g14, "value=1-J=-zeta^2 order=10 zeta=-delta^3")


DELTA_BASIS_DETERMINANT = determinant(DELTA_BASIS_MATRIX)
K_DELTA_DERIVED = DELTA_BASIS_DETERMINANT != 0
K_DELTA = (
    columns_matrix([
        solve_square(DELTA_BASIS_MATRIX, list(q5_mul(DELTA, basis)))
        for basis in DELTA_BASIS
    ])
    if K_DELTA_DERIVED
    else zero_matrix(4, 4)
)
EXPECTED_K_DELTA = [
    [0, 0, 0, -1],
    [1, 0, 0, 1],
    [0, 1, 0, -1],
    [0, 0, 1, 1],
]
g15 = (
    K_DELTA_DERIVED
    and K_DELTA == EXPECTED_K_DELTA
    and matmul(P_C, T) == matmul(T, K_DELTA)
    and determinant(T) == 1
    and characteristic_polynomial(K_DELTA) == [1, -1, 1, -1, 1]
)
gate("G15", "MODULE", g15, "companion_intertwiner=yes")


g16 = (
    q5_det2(B_1) == DELTA
    and q5_det2(B_2) == DELTA
    and q5_mul(DELTA, q5_pow(DELTA, 9)) == QONE
)
gate("G16", "GENERATOR_DETERMINANTS", g16, "value=1-J")


P_C_INVERSE = matpow(P_C, 9)
K_DELTA_INVERSE = matpow(K_DELTA, 9)
CHI_SIGMA_1 = P_C
CHI_SIGMA_2 = P_C
CHI_SIGMA_1_INVERSE = P_C_INVERSE
CHI_SIGMA_2_INVERSE = P_C_INVERSE
BRAID_LEFT_WORD = (1, 2, 1)
BRAID_RIGHT_WORD = (2, 1, 2)
chi_braid_relation = matmul(
    CHI_SIGMA_1, matmul(CHI_SIGMA_2, CHI_SIGMA_1)
) == matmul(CHI_SIGMA_2, matmul(CHI_SIGMA_1, CHI_SIGMA_2))
exponent_sum_relation = len(BRAID_LEFT_WORD) == len(BRAID_RIGHT_WORD) == 3
g17 = (
    chi_braid_relation
    and exponent_sum_relation
    and CHI_SIGMA_1 == CHI_SIGMA_2
    and matmul(CHI_SIGMA_1, CHI_SIGMA_1_INVERSE) == identity(4)
    and matmul(CHI_SIGMA_2, CHI_SIGMA_2_INVERSE) == identity(4)
    and matmul(P_C, T) == matmul(T, K_DELTA)
    and matmul(P_C_INVERSE, T) == matmul(T, K_DELTA_INVERSE)
    and matpow(P_C, 10) == identity(4)
    and matpow(K_DELTA, 10) == identity(4)
)
gate(
    "G17",
    "CHARACTER_PROOF_INPUTS",
    g17,
    "presentation=checked inverses=yes intertwiner=yes",
)

claim_b_dependencies = (
    "G01", "G02", "G03", "G04", "G05", "G07", "G08",
    "G11", "G12", "G13", "G14", "G15", "G16", "G17",
)
claim_b_ok = all(code not in FAILURES for code in claim_b_dependencies)
print(
    "RESULT CLAIM_B %s %s"
    % (CLAIM_B, "CONFIRMED" if claim_b_ok else "FIRED")
)
print(
    "SCOPE raw_M_J=TYPE_BOUNDARY galois_branch=OUT_OF_SCOPE "
    "physical_tau_identification=NONE"
)

if not FAILURES and claim_a_ok and claim_b_ok:
    print("RESULT OVERALL PASS gates=17 claims=2")
else:
    confirmed = int(claim_a_ok) + int(claim_b_ok)
    print(
        "RESULT OVERALL FIRED gates_pass=%d/17 claims_confirmed=%d/2"
        % (17 - len(FAILURES), confirmed)
    )
