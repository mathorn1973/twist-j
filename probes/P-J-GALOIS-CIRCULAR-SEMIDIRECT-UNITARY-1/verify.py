#!/usr/bin/env python3
"""Exact audit for P-J-GALOIS-CIRCULAR-SEMIDIRECT-UNITARY-1.

Standard library only.  Exact integer, Fraction, and Q(zeta_5) arithmetic.
No file input, network, subprocess, randomness, clock, dynamic import, eval,
exec, float, or builtin complex arithmetic.

The theorem-grade implications are proved in PREREG.md.  This program
reconstructs and audits their finite exact premises from displayed inputs.
"""

from fractions import Fraction
from itertools import combinations


PROBE = "P-J-GALOIS-CIRCULAR-SEMIDIRECT-UNITARY-1"
CLAIM_A = "J-GALOIS-CIRCULAR-QUOTIENT-SEMIDIRECT-UNITARY"
CLAIM_B = "J-GALOIS-CIRCULAR-ODD-CHARACTER"

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
            for a, b in zip(row, column):
                total += Fraction(a) * Fraction(b)
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


def matsub(left, right):
    return matadd(left, matscale(right, -1))


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


def inverse(matrix):
    size = len(matrix)
    require(size > 0 and all(len(row) == size for row in matrix), "inverse shape")
    work = [
        [Fraction(value) for value in row] + identity(size)[index]
        for index, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        require(pivot is not None, "singular inverse")
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
    return [row[size:] for row in work]


def matrix_rank(matrix):
    require(matrix, "empty rank matrix")
    work = [[Fraction(value) for value in row] for row in matrix]
    rows = len(work)
    columns = len(work[0])
    require(all(len(row) == columns for row in work), "rank ragged matrix")
    pivot_row = 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, rows) if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def solve_square(matrix, vector):
    return matvec(inverse(matrix), vector)


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
        if matvec(basis_matrix, solution) == [Fraction(value) for value in vector]:
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
    """Evaluate low-to-high coefficients at a square matrix."""
    size = len(matrix)
    result = zero_matrix(size, size)
    power = identity(size)
    for coefficient in coefficients:
        result = matadd(result, matscale(power, coefficient))
        power = matmul(power, matrix)
    return result


def trace(matrix):
    require(matrix and all(len(row) == len(matrix) for row in matrix), "trace shape")
    return sum((matrix[index][index] for index in range(len(matrix))), Fraction(0))


def is_zero_matrix(matrix):
    return all(value == 0 for row in matrix for value in row)


def is_integral_matrix(matrix):
    return all(Fraction(value).denominator == 1 for row in matrix for value in row)


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


def matrix_key(matrix):
    return tuple(tuple(Fraction(value) for value in row) for row in matrix)


def projective_key(matrix):
    entries = [Fraction(value) for row in matrix for value in row]
    pivot = next((value for value in entries if value), None)
    if pivot is None:
        return None
    return tuple(value / pivot for value in entries)


def lattice_equal(left_basis, right_basis):
    if determinant(left_basis) == 0:
        return False
    transition = matmul(inverse(left_basis), right_basis)
    return is_integral_matrix(transition) and abs(determinant(transition)) == 1


def bounded_group_closure(generators, limit):
    size = len(generators[0])
    start = identity(size)
    seen = {matrix_key(start): start}
    frontier = [start]
    while frontier:
        next_frontier = []
        for item in frontier:
            for generator in generators:
                product = matmul(item, generator)
                key = matrix_key(product)
                if key in seen:
                    continue
                if len(seen) >= limit:
                    return None
                seen[key] = product
                next_frontier.append(product)
        frontier = next_frontier
    return list(seen.values())


# ---------------------------------------------------------------------------
# Q(zeta_5) in the basis 1,z,z^2,z^3 with Phi_5(z)=0


QZERO = (Fraction(0), Fraction(0), Fraction(0), Fraction(0))
QONE = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))


def q5(value):
    if isinstance(value, tuple) or isinstance(value, list):
        require(len(value) == 4, "Q5 coordinate length")
        return tuple(Fraction(entry) for entry in value)
    return (Fraction(value), Fraction(0), Fraction(0), Fraction(0))


def q5_add(left, right):
    return tuple(a + b for a, b in zip(q5(left), q5(right)))


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


def q5_galois_matrix(exponent):
    return columns_matrix([q5_galois(basis, exponent) for basis in QBASIS])


# ---------------------------------------------------------------------------
# Alternating covariant pullbacks and the fixed quotient


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


def quotient_action(action, quotient_map, section):
    return matmul(quotient_map, matmul(action, section))


def seam_scalars(action, inclusion):
    if determinant(inclusion) == 0:
        return None
    inclusion_inverse = inverse(inclusion)
    unit = identity(len(action))
    return [
        scalar
        for scalar in range(5)
        if is_integral_matrix(
            matmul(inclusion_inverse, matsub(action, matscale(unit, scalar)))
        )
    ]


# ---------------------------------------------------------------------------
# Frozen construction and eighteen exact subgates


OUTPUT.extend(
    (
        "PROBE %s" % PROBE,
        "SPEC J_GALOIS_CIRCULAR_EXACT_V1",
        "MODE RESULT-EXPOSED PROOF-FIRST",
    )
)


J = q5_add(QONE, q5_pow(ZETA, 2))
DELTA_10 = q5_sub(QONE, J)
PHI5 = (1, 1, 1, 1, 1)
PHI10_LOW = (1, -1, 1, -1, 1)
delta_order = q5_pow(DELTA_10, 10) == QONE and all(
    q5_pow(DELTA_10, exponent) != QONE for exponent in range(1, 10)
)
g01 = (
    q5_poly_eval(PHI5, ZETA) == QZERO
    and q5_pow(ZETA, 5) == QONE
    and delta_order
    and DELTA_10 == q5_neg(q5_pow(ZETA, 2))
    and q5_galois(DELTA_10, 2) == q5_pow(DELTA_10, 7)
    and q5_galois(DELTA_10, 3) == q5_pow(DELTA_10, 3)
)
gate("G01", "FIELD", g01, "Phi5=0 delta10_order=10 gamma2=power7 gamma3=power3")


M_J = q5_regular_matrix(J)
U_2 = q5_galois_matrix(2)
EXPECTED_M_J = [
    [1, 0, -1, 1],
    [0, 1, -1, 0],
    [1, 0, 0, 0],
    [0, 1, -1, 1],
]
g02 = (
    M_J == EXPECTED_M_J
    and matvec(U_2, ZETA) == list(q5_pow(ZETA, 2))
    and all(
        q5(matvec(U_2, q5_mul(left, right)))
        == q5_mul(matvec(U_2, left), matvec(U_2, right))
        for left in QBASIS
        for right in QBASIS
    )
    and determinant(M_J) == 1
    and determinant(U_2) == -1
    and matpow(U_2, 4) == identity(4)
    and matpow(U_2, 2) != identity(4)
    and characteristic_polynomial(M_J) == [1, -3, 4, -2, 1]
)
gate("G02", "SOURCE", g02, "M_J=public U2=derived_gamma2Gal dets=(1,-1) U2_order=4")


P = construct_pullback(M_J)
S_E = construct_pullback(U_2)
EXPECTED_P = [
    [1, 0, 1, -1, 0, 1],
    [-1, 1, -1, 1, 0, -1],
    [0, -1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0],
    [-1, 0, -1, 0, 1, 0],
    [1, 0, 0, 0, -1, 0],
]
g03 = (
    P == EXPECTED_P
    and determinant(P) == 1
    and determinant(S_E) == -1
    and matpow(S_E, 4) == identity(6)
)
gate("G03", "PULLBACK", g03, "carrier=Alt2_dual convention=A^TWA orders_reconstructed")


OMEGA_1 = [1, 0, 0, 1, 0, 1]
OMEGA_2 = [0, 1, -1, 0, 1, 0]
H_COLUMNS = (OMEGA_1, OMEGA_2)
C_1 = [-1, 0, 1, 0, 0, 0]
C_2 = [0, -1, 0, 1, 0, 0]
C_3 = [0, -1, 0, 0, 1, 0]
C_4 = [-1, 0, 0, 0, 0, 1]
C_COLUMNS = (C_1, C_2, C_3, C_4)
H_MATRIX = columns_matrix(H_COLUMNS)
C_MATRIX = columns_matrix(C_COLUMNS)
FULL_PRIMARY = columns_matrix(H_COLUMNS + C_COLUMNS)
P_H = restriction_matrix(P, H_COLUMNS)
S_H = restriction_matrix(S_E, H_COLUMNS)
P_C = restriction_matrix(P, C_COLUMNS)
S_C = restriction_matrix(S_E, C_COLUMNS)
Q_MAP = [
    [0, 1, 1, 0, 0, 0],
    [-1, 0, 0, 1, 0, 0],
    [0, -1, 0, 0, 1, 0],
    [-1, 0, 0, 0, 0, 1],
]
L_SECTION = columns_matrix(
    (
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1],
    )
)
g04 = (
    matrix_rank(H_MATRIX) == 2
    and matrix_rank(C_MATRIX) == 4
    and maximal_minor_gcd(H_MATRIX) == 1
    and maximal_minor_gcd(C_MATRIX) == 1
    and abs(determinant(FULL_PRIMARY)) == 5
    and P_H is not None
    and S_H is not None
    and P_C is not None
    and S_C is not None
    and matmul(Q_MAP, H_MATRIX) == zero_matrix(4, 2)
    and matrix_rank(Q_MAP) == 4
    and matmul(Q_MAP, L_SECTION) == identity(4)
)
gate("G04", "PRIMARY_QUOTIENT", g04, "H,C_saturated seam_index=5 L=free_rank4")


P_L = quotient_action(P, Q_MAP, L_SECTION)
S_L = quotient_action(S_E, Q_MAP, L_SECTION)
EXPECTED_P_L = [
    [0, 1, 0, 0],
    [0, 1, 0, -1],
    [0, -1, 1, 1],
    [-1, 1, -1, -1],
]
EXPECTED_S_L = [
    [-1, 0, 0, 0],
    [0, 1, 0, -1],
    [1, -1, 0, 0],
    [0, 1, 1, 0],
]
g05 = (
    matmul(Q_MAP, matmul(P, H_MATRIX)) == zero_matrix(4, 2)
    and matmul(Q_MAP, matmul(S_E, H_MATRIX)) == zero_matrix(4, 2)
    and P_L == EXPECTED_P_L
    and S_L == EXPECTED_S_L
    and determinant(P_L) == 1
    and determinant(S_L) == -1
)
gate("G05", "QUOTIENT_ACTION", g05, "Pbar,Sbar_derived in fixed quotient basis")


J_C = matmul(Q_MAP, C_MATRIX)
g06 = (
    abs(determinant(J_C)) == 5
    and P_C is not None
    and S_C is not None
    and matmul(P_L, J_C) == matmul(J_C, P_C)
    and matmul(S_L, J_C) == matmul(J_C, S_C)
    and seam_scalars(P_L, J_C) == [4]
    and seam_scalars(S_L, J_C) == [2]
)
gate("G06", "SEAM", g06, "0->C_Z->L->Z/5 P=-1 S=2")


ORBIT = [C_2]
for _ in range(3):
    ORBIT.append(matvec(P, ORBIT[-1]))
T_COORDINATES = [coordinates_in_basis(C_COLUMNS, vector) for vector in ORBIT]
T_COORDINATES_DEFINED = all(coordinates is not None for coordinates in T_COORDINATES)
T_PSI = (
    columns_matrix(T_COORDINATES) if T_COORDINATES_DEFINED else zero_matrix(4, 4)
)
EXPECTED_T_PSI = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, -1],
    [0, 0, -1, 0],
]
DELTA_BASIS = (QONE, DELTA_10, q5_pow(DELTA_10, 2), q5_pow(DELTA_10, 3))
B_DELTA = columns_matrix(DELTA_BASIS)
B_DELTA_INVERSE = inverse(B_DELTA) if determinant(B_DELTA) != 0 else None
K_DELTA = (
    matmul(B_DELTA_INVERSE, matmul(q5_regular_matrix(DELTA_10), B_DELTA))
    if B_DELTA_INVERSE is not None
    else zero_matrix(4, 4)
)
J_PSI = matmul(J_C, T_PSI)
J_PSI_INVERSE = inverse(J_PSI) if determinant(J_PSI) != 0 else None
F_L_TO_DELTA = J_PSI_INVERSE if J_PSI_INVERSE is not None else zero_matrix(4, 4)
B_IDEAL = columns_matrix(
    (
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [Fraction(2, 5), Fraction(1, 5), Fraction(1, 5), Fraction(2, 5)],
    )
)
B_IDEAL_INVERSE = inverse(B_IDEAL) if determinant(B_IDEAL) != 0 else None
ONE_PLUS_DELTA_ON_I = matmul(matadd(identity(4), K_DELTA), B_IDEAL)
g07 = (
    T_COORDINATES_DEFINED
    and B_DELTA_INVERSE is not None
    and J_PSI_INVERSE is not None
    and B_IDEAL_INVERSE is not None
    and T_PSI == EXPECTED_T_PSI
    and determinant(T_PSI) == 1
    and abs(determinant(B_DELTA)) == 1
    and abs(determinant(J_PSI)) == 5
    and lattice_equal(F_L_TO_DELTA, B_IDEAL)
    and is_integral_matrix(ONE_PLUS_DELTA_ON_I)
    and abs(determinant(ONE_PLUS_DELTA_ON_I)) == 1
    and matmul(F_L_TO_DELTA, matmul(P_L, J_PSI)) == K_DELTA
)
gate("G07", "FRACTIONAL_IDEAL", g07, "L=(1+delta10)^-1 O_K C_Z=O_K index=5")


U_3_ZETA = q5_galois_matrix(3)
GAMMA_3_DELTA = (
    matmul(B_DELTA_INVERSE, matmul(U_3_ZETA, B_DELTA))
    if B_DELTA_INVERSE is not None
    else zero_matrix(4, 4)
)
S_FIELD = matmul(F_L_TO_DELTA, matmul(S_L, J_PSI))
TARGET_S_FIELD = matmul(matpow(K_DELTA, 4), GAMMA_3_DELTA)
ideal_s_action = (
    matmul(B_IDEAL_INVERSE, matmul(TARGET_S_FIELD, B_IDEAL))
    if B_IDEAL_INVERSE is not None
    else zero_matrix(4, 4)
)
g08 = (
    T_COORDINATES_DEFINED
    and B_DELTA_INVERSE is not None
    and J_PSI_INVERSE is not None
    and B_IDEAL_INVERSE is not None
    and S_FIELD == TARGET_S_FIELD
    and is_integral_matrix(ideal_s_action)
    and abs(determinant(ideal_s_action)) == 1
    and matmul(S_L, matmul(P_L, matpow(S_L, 3))) == matpow(P_L, 3)
    and matmul(matpow(S_L, 3), matmul(P_L, S_L)) == matpow(P_L, 7)
)
gate("G08", "CONTRAVARIANCE", g08, "S=m_delta10^4 o gamma3 relation=SPS^-1=P^3")


g09 = (
    T_COORDINATES_DEFINED
    and B_DELTA_INVERSE is not None
    and J_PSI_INVERSE is not None
    and matmul(S_FIELD, K_DELTA) == matmul(matpow(K_DELTA, 3), S_FIELD)
    and matmul(S_FIELD, K_DELTA) != matmul(K_DELTA, S_FIELD)
    and matmul(S_L, P_L) != matmul(P_L, S_L)
)
gate("G09", "TYPE", g09, "gamma3_semilinear=yes O_K_linear=no noncommuting=yes")


NORMAL_FORMS = [
    matmul(matpow(P_L, a), matpow(S_L, b))
    for a in range(10)
    for b in range(4)
]
NORMAL_KEYS = {matrix_key(matrix) for matrix in NORMAL_FORMS}
GROUP = bounded_group_closure((P_L, S_L), 256)
g10 = (
    matpow(P_L, 10) == identity(4)
    and matpow(P_L, 5) == matscale(identity(4), -1)
    and matpow(S_L, 4) == identity(4)
    and matmul(S_L, matmul(P_L, matpow(S_L, 3))) == matpow(P_L, 3)
    and len(NORMAL_KEYS) == 40
    and GROUP is not None
    and len(GROUP) == 40
    and {matrix_key(matrix) for matrix in GROUP} == NORMAL_KEYS
)
gate("G10", "GROUP", g10, "C10_semidirect_3_C4 order=40 normal_forms=40")


D_FIVE = matpow(P_L, 6)
AFFINE_FORMS = [
    matmul(matpow(D_FIVE, a), matpow(S_L, b))
    for a in range(5)
    for b in range(4)
]
AFFINE_KEYS = {matrix_key(matrix) for matrix in AFFINE_FORMS}
PROJECTIVE_KEYS = {projective_key(matrix) for matrix in NORMAL_FORMS}
LINEAR_KERNEL = [
    (a, b)
    for a in range(10)
    for b in range(4)
    if matmul(matpow(P_L, a), matpow(S_L, b)) == identity(4)
]
PROJECTIVE_KERNEL = [
    (a, b)
    for a in range(10)
    for b in range(4)
    if projective_key(matmul(matpow(P_L, a), matpow(S_L, b)))
    == projective_key(identity(4))
]
g11 = (
    matpow(D_FIVE, 5) == identity(4)
    and matpow(D_FIVE, 1) != identity(4)
    and matmul(S_L, matmul(D_FIVE, matpow(S_L, 3))) == matpow(D_FIVE, 3)
    and len(AFFINE_KEYS) == 20
    and matrix_key(matpow(P_L, 5)) not in AFFINE_KEYS
    and NORMAL_KEYS
    == AFFINE_KEYS | {matrix_key(matmul(matpow(P_L, 5), matrix)) for matrix in AFFINE_FORMS}
    and LINEAR_KERNEL == [(0, 0)]
    and PROJECTIVE_KERNEL == [(0, 0), (5, 0)]
    and len(PROJECTIVE_KEYS) == 20
)
gate("G11", "CENTRAL_PROJECTIVE", g11, "C2xAGL1F5 linear=40 projective=20")


G_L = [
    [2, 0, 1, 0],
    [0, 2, 0, -1],
    [1, 0, 2, 1],
    [0, -1, 1, 2],
]
LEADING_MINORS = [
    determinant([row[:size] for row in G_L[:size]]) for size in range(1, 5)
]
g12 = (
    G_L == transpose(G_L)
    and LEADING_MINORS == [2, 4, 6, 5]
    and all(value > 0 for value in LEADING_MINORS)
)
gate("G12", "POSITIVE_FORM", g12, "Gram=explicit Sylvester=(2,4,6,5)")


g13 = (
    matmul(transpose(P_L), matmul(G_L, P_L)) == G_L
    and matmul(transpose(S_L), matmul(G_L, S_L)) == G_L
)
gate("G13", "UNITARY", g13, "Pbar,Sbar preserve one explicit positive form")


ODD_INDICES = {1, 3, 7, 9}
EVEN_INDICES = {2, 4, 6, 8}
g14 = (
    characteristic_polynomial(P_L) == [1, -1, 1, -1, 1]
    and is_zero_matrix(poly_matrix_eval(PHI10_LOW, P_L))
    and delta_order
    and len({q5_pow(DELTA_10, exponent) for exponent in ODD_INDICES}) == 4
)
gate("G14", "SPECTRUM", g14, "charpoly=Phi10 eigenvalues=delta10^{1,3,7,9} simple=yes")


GROUP_CYCLE = []
value = 1
for _ in range(4):
    GROUP_CYCLE.append(value)
    value = (3 * value) % 10
DUAL_CYCLE = []
value = 1
for _ in range(4):
    DUAL_CYCLE.append(value)
    value = (7 * value) % 10
dual_permutations = [
    {index: (pow(7, b, 10) * index) % 10 for index in ODD_INDICES}
    for b in range(4)
]
g15 = (
    GROUP_CYCLE == [1, 3, 9, 7]
    and DUAL_CYCLE == [1, 7, 9, 3]
    and set(GROUP_CYCLE) == ODD_INDICES
    and set(DUAL_CYCLE) == ODD_INDICES
    and all(set(permutation.values()) == ODD_INDICES for permutation in dual_permutations)
    and all(
        all(permutation[index] != index for index in ODD_INDICES)
        for permutation in dual_permutations[1:]
    )
)
gate("G15", "EIGENLINE_SYSTEM", g15, "normalizer_action=3 dual_action=7 transitive_monomial=yes")


EXPECTED_P_TRACES = [4, 1, -1, 1, -1, -4, -1, 1, -1, 1]
CHARACTER = {}
character_ok = True
ramanujan_ok = True
for a in range(10):
    ramanujan = QZERO
    for exponent in ODD_INDICES:
        ramanujan = q5_add(ramanujan, q5_pow(DELTA_10, exponent * a))
    for b in range(4):
        matrix = matmul(matpow(P_L, a), matpow(S_L, b))
        value = trace(matrix)
        CHARACTER[(a, b)] = value
        target = Fraction(EXPECTED_P_TRACES[a]) if b == 0 else Fraction(0)
        character_ok = character_ok and value == target
        if b == 0:
            ramanujan_ok = ramanujan_ok and ramanujan == q5(target)
character_norm = sum((value * value for value in CHARACTER.values()), Fraction(0)) / 40
g16 = (
    character_ok
    and ramanujan_ok
    and character_norm == 1
    and CHARACTER[(5, 0)] == -4
)
gate("G16", "ODD_CHARACTER", g16, "all40_values=yes norm=1 chi(P^5)=-4")


unseen = set(range(10))
CHARACTER_ORBITS = []
while unseen:
    start = min(unseen)
    orbit = set()
    value = start
    for _ in range(4):
        orbit.add(value)
        value = (3 * value) % 10
    CHARACTER_ORBITS.append(tuple(sorted(orbit)))
    unseen -= orbit
CHARACTER_ORBITS.sort(key=lambda orbit: (len(orbit), orbit))
IRREP_DIMENSIONS = []
for orbit in CHARACTER_ORBITS:
    stabilizer_size = 4 // len(orbit)
    IRREP_DIMENSIONS.extend([len(orbit)] * stabilizer_size)
IRREP_DIMENSIONS.sort()
EXPECTED_EVEN_TRACES = [4, -1, -1, -1, -1, 4, -1, -1, -1, -1]
even_trace_ok = True
for a in range(10):
    even_sum = QZERO
    for exponent in EVEN_INDICES:
        even_sum = q5_add(even_sum, q5_pow(DELTA_10, exponent * a))
    even_trace_ok = even_trace_ok and even_sum == q5(EXPECTED_EVEN_TRACES[a])
even_kernel = [a for a, value in enumerate(EXPECTED_EVEN_TRACES) if value == 4]
g17 = (
    CHARACTER_ORBITS == [(0,), (5,), (1, 3, 7, 9), (2, 4, 6, 8)]
    and IRREP_DIMENSIONS == [1] * 8 + [4, 4]
    and sum(dimension * dimension for dimension in IRREP_DIMENSIONS) == 40
    and even_trace_ok
    and even_kernel == [0, 5]
    and LINEAR_KERNEL == [(0, 0)]
)
gate("G17", "IRREP_CENSUS", g17, "irreps=8x1D+2x4D odd=faithful even_kernel=<P^5>")


normalizer_ok = True
for a in range(10):
    for b in range(4):
        item = matmul(matpow(P_L, a), matpow(S_L, b))
        item_inverse = matmul(matpow(S_L, (-b) % 4), matpow(P_L, (-a) % 10))
        target_power = pow(3, b, 10)
        normalizer_ok = normalizer_ok and (
            matmul(item, item_inverse) == identity(4)
            and matmul(item_inverse, item) == identity(4)
            and matmul(item, matmul(P_L, item_inverse)) == matpow(P_L, target_power)
        )
g18 = (
    GROUP is not None
    and len(GROUP) == 40
    and normalizer_ok
    and all(set(permutation.values()) == ODD_INDICES for permutation in dual_permutations)
)
gate("G18", "FINITE_MONOMIAL_BOUNDARY", g18, "finite=40 every_element_normalizes_eigenline_system")


CLAIM_A_GATES = tuple("G%02d" % index for index in range(1, 14))
CLAIM_B_GATES = tuple("G%02d" % index for index in range(1, 12)) + tuple(
    "G%02d" % index for index in range(14, 19)
)
claim_a_ok = all(code not in FAILURES for code in CLAIM_A_GATES)
claim_b_ok = all(code not in FAILURES for code in CLAIM_B_GATES)

OUTPUT.append(
    "RESULT CLAIM_A %s %s" % (CLAIM_A, "CONFIRMED" if claim_a_ok else "FIRED")
)
OUTPUT.append(
    "RESULT CLAIM_B %s %s" % (CLAIM_B, "CONFIRMED" if claim_b_ok else "FIRED")
)
OUTPUT.append(
    "BOUNDARY linear_group_order=40 projective_group_order=20 "
    "spectral_action=monomial superposition_mixer=NOT_CLAIMED"
)
OUTPUT.append(
    "SCOPE L1_only Born=NONE probability=NONE physical_qudit=NONE "
    "Clifford=NONE universality=NONE space=NONE L2-L6=NONE"
)

if claim_a_ok and claim_b_ok and not FAILURES:
    OUTPUT.append("RESULT OVERALL PASS gates=18 claims=2")
else:
    confirmed = int(claim_a_ok) + int(claim_b_ok)
    OUTPUT.append(
        "RESULT OVERALL FIRED gates_pass=%d/18 claims_confirmed=%d/2"
        % (18 - len(FAILURES), confirmed)
    )

print("\n".join(OUTPUT))
