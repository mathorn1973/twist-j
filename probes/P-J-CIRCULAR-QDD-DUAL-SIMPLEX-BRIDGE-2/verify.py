#!/usr/bin/env python3
"""Exact audit for P-J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE-2.

Standard library only.  Every scientific comparison uses exact integer or
Fraction arithmetic.  There is no file input, network, subprocess, random
state, clock, dynamic import, eval, exec, float, or builtin complex arithmetic.

The universal lattice and representation implications are proved in the
frozen PREREG.md.  This program reconstructs and audits their finite premises.
"""

from fractions import Fraction
from itertools import combinations, product
from math import gcd, lcm


PROBE = "P-J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE-2"
CLAIM_A = "J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE"
CLAIM_B = "J-CIRCULAR-QDD-SIGNED-AFFINE-PROJECTOR-INTERTWINER"
BASE = "3b15217d28575726da1ff3af4de71cba4544637d"
CLAIM_LOCK = 801
CANON = "v75"
SCOPE_LINE = (
    "SCOPE L1_only Born=NONE probability=NONE measurement=NONE apparatus=NONE "
    "physical_qudit=NONE decoder_completion=NONE L2-L6=NONE"
)

FAILURES = []
OUTPUT = []


def require(condition, message):
    """Reserve exceptions and nonzero process status for integrity STOP."""
    if not condition:
        raise RuntimeError("STOP: " + message)


def gate(code, label, condition, detail):
    """Record one completed exact scientific gate without aborting on FIRED."""
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


def matvec(matrix, vector):
    require(all(len(row) == len(vector) for row in matrix), "matrix-vector shape")
    return [
        sum((Fraction(a) * Fraction(b) for a, b in zip(row, vector)), Fraction(0))
        for row in matrix
    ]


def matpow(matrix, exponent):
    require(exponent >= 0, "negative matrix power")
    require(matrix and all(len(row) == len(matrix) for row in matrix), "power shape")
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


def outer(left, right):
    return [[Fraction(a) * Fraction(b) for b in right] for a in left]


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


def safe_inverse(matrix):
    size = len(matrix)
    require(size > 0 and all(len(row) == size for row in matrix), "inverse shape")
    work = [
        [Fraction(value) for value in row] + identity(size)[index]
        for index, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            return None
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
    row_count = len(work)
    column_count = len(work[0])
    require(all(len(row) == column_count for row in work), "rank ragged matrix")
    pivot_row = 0
    for column in range(column_count):
        pivot = next((row for row in range(pivot_row, row_count) if work[row][column]), None)
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


def nullspace(matrix):
    require(matrix, "empty nullspace matrix")
    work = [[Fraction(value) for value in row] for row in matrix]
    row_count = len(work)
    column_count = len(work[0])
    require(all(len(row) == column_count for row in work), "nullspace ragged matrix")
    pivot_columns = []
    pivot_row = 0
    for column in range(column_count):
        pivot = next((row for row in range(pivot_row, row_count) if work[row][column]), None)
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
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    free_columns = [column for column in range(column_count) if column not in pivot_columns]
    basis = []
    for free in free_columns:
        vector = [Fraction(0) for _ in range(column_count)]
        vector[free] = Fraction(1)
        for row, pivot in reversed(list(enumerate(pivot_columns))):
            vector[pivot] = -sum(
                (work[row][column] * vector[column] for column in free_columns),
                Fraction(0),
            )
        basis.append(vector)
    return basis


def primitive_integer_vector(vector):
    if not vector or all(Fraction(value) == 0 for value in vector):
        return None
    denominator = 1
    for value in vector:
        denominator = lcm(denominator, Fraction(value).denominator)
    integers = [int(Fraction(value) * denominator) for value in vector]
    content = 0
    for value in integers:
        content = gcd(content, abs(value))
    require(content > 0, "zero primitive content")
    integers = [value // content for value in integers]
    first = next(value for value in integers if value)
    if first < 0:
        integers = [-value for value in integers]
    return integers


def reshape(vector, rows, columns):
    require(len(vector) == rows * columns, "reshape length")
    return [list(map(Fraction, vector[row * columns : (row + 1) * columns])) for row in range(rows)]


def trace(matrix):
    require(matrix and all(len(row) == len(matrix) for row in matrix), "trace shape")
    return sum((matrix[index][index] for index in range(len(matrix))), Fraction(0))


def is_integral_matrix(matrix):
    return all(Fraction(value).denominator == 1 for row in matrix for value in row)


def matrix_key(matrix):
    return tuple(tuple(Fraction(value) for value in row) for row in matrix)


def projective_key(matrix):
    entries = [Fraction(value) for row in matrix for value in row]
    pivot = next((value for value in entries if value), None)
    if pivot is None:
        return None
    return tuple(value / pivot for value in entries)


def sum_matrices(matrices, rows, columns):
    result = zero_matrix(rows, columns)
    for matrix in matrices:
        result = matadd(result, matrix)
    return result


def bounded_group_closure(generators, limit):
    size = len(generators[0])
    start = identity(size)
    seen = {matrix_key(start): start}
    frontier = [start]
    while frontier:
        next_frontier = []
        for item in frontier:
            for generator in generators:
                candidate = matmul(item, generator)
                key = matrix_key(candidate)
                if key in seen:
                    continue
                if len(seen) >= limit:
                    return None
                seen[key] = candidate
                next_frontier.append(candidate)
        frontier = next_frontier
    return list(seen.values())


def determinantal_divisor(matrix, size):
    rows = len(matrix)
    columns = len(matrix[0])
    require(size >= 1 and size <= min(rows, columns), "minor size")
    value = 0
    for selected_rows in combinations(range(rows), size):
        for selected_columns in combinations(range(columns), size):
            minor = [
                [matrix[row][column] for column in selected_columns]
                for row in selected_rows
            ]
            minor_det = determinant(minor)
            if minor_det.denominator != 1:
                return None
            value = gcd(value, abs(minor_det.numerator))
    return value


def smith_invariants(matrix):
    if not is_integral_matrix(matrix):
        return None
    rank = min(len(matrix), len(matrix[0]))
    divisors = [1]
    for size in range(1, rank + 1):
        divisor = determinantal_divisor(matrix, size)
        if divisor in (None, 0):
            return None
        divisors.append(divisor)
    return [divisors[index] // divisors[index - 1] for index in range(1, len(divisors))]


def lattice_equal(left_basis, right_basis):
    """Compare two full-rank rational lattices by both transition maps."""
    left_inverse = safe_inverse(left_basis)
    right_inverse = safe_inverse(right_basis)
    if left_inverse is None or right_inverse is None:
        return False
    left_to_right = matmul(right_inverse, left_basis)
    right_to_left = matmul(left_inverse, right_basis)
    return (
        is_integral_matrix(left_to_right)
        and is_integral_matrix(right_to_left)
        and abs(determinant(left_to_right)) == 1
        and abs(determinant(right_to_left)) == 1
    )


def seam_scalars(action, inclusion, modulus):
    inclusion_inverse = safe_inverse(inclusion)
    if inclusion_inverse is None:
        return None
    unit = identity(len(action))
    return [
        scalar
        for scalar in range(modulus)
        if is_integral_matrix(
            matmul(inclusion_inverse, matsub(action, matscale(unit, scalar)))
        )
    ]


def invariant_symmetric_constraints(action):
    size = len(action)
    pairs = [(row, column) for row in range(size) for column in range(row, size)]
    columns = []
    for basis_index in range(len(pairs)):
        form = zero_matrix(size, size)
        row, column = pairs[basis_index]
        form[row][column] = Fraction(1)
        form[column][row] = Fraction(1)
        if row == column:
            form[row][column] = Fraction(1)
        image = matsub(matmul(transpose(action), matmul(form, action)), form)
        columns.append([image[row][column] for row, column in pairs])
    return columns_matrix(columns), pairs


def intertwiner_constraints(source, target):
    """Rows for X source = target X with row-major X coordinates."""
    size = len(source)
    rows = []
    for row in range(size):
        for column in range(size):
            equation = [Fraction(0) for _ in range(size * size)]
            for index in range(size):
                equation[size * row + index] += Fraction(source[index][column])
                equation[size * index + column] -= Fraction(target[row][index])
            rows.append(equation)
    return rows


def bilinear(vector_left, gram, vector_right):
    return sum(
        (
            Fraction(left) * Fraction(right)
            for left, right in zip(vector_left, matvec(gram, vector_right))
        ),
        Fraction(0),
    )


def orthogonal_projector(vector, gram):
    norm = bilinear(vector, gram, vector)
    if norm == 0:
        return None
    row = matmul([list(map(Fraction, vector))], gram)[0]
    return matscale(outer(vector, row), Fraction(1, 1) / norm)


def sharp(action, gram, gram_inverse):
    return matmul(gram_inverse, matmul(transpose(action), gram))


# ---------------------------------------------------------------------------
# Q(zeta_5) in the basis 1,zeta,zeta^2,zeta^3


QZERO = (Fraction(0), Fraction(0), Fraction(0), Fraction(0))
QONE = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
ZETA = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
QBASIS = (
    QONE,
    ZETA,
    (Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
)


def q5(value):
    if isinstance(value, (tuple, list)):
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
    coefficients = [Fraction(0) for _ in range(7)]
    for left_degree, left_value in enumerate(left):
        for right_degree, right_value in enumerate(right):
            coefficients[left_degree + right_degree] += left_value * right_value
    for degree in range(6, 3, -1):
        top = coefficients[degree]
        coefficients[degree] = Fraction(0)
        for target in range(degree - 4, degree):
            coefficients[target] -= top
    return tuple(coefficients[:4])


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
    result = QZERO
    for degree, coefficient in enumerate(q5(value)):
        result = q5_add(
            result,
            tuple(coefficient * entry for entry in q5_pow(ZETA, (degree * exponent) % 5)),
        )
    return result


def q5_regular_matrix(value):
    return columns_matrix([q5_mul(value, basis) for basis in QBASIS])


def q5_galois_matrix(exponent):
    return columns_matrix([q5_galois(basis, exponent) for basis in QBASIS])


# ---------------------------------------------------------------------------
# Alternating-form pullback and quotient reconstruction


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
        coordinates = [Fraction(0) for _ in range(6)]
        coordinates[index] = Fraction(1)
        form = alternating_matrix(coordinates)
        image = matmul(transpose(multiplier), matmul(form, multiplier))
        columns.append(alternating_coordinates(image))
    return columns_matrix(columns)


# ---------------------------------------------------------------------------
# Frozen reconstruction and exact gates


def main():
    OUTPUT.extend(
        (
            "PROBE %s" % PROBE,
            "BASE %s" % BASE,
            "CLAIM_LOCK %d" % CLAIM_LOCK,
            "CANON %s" % CANON,
            "SPEC J_CIRCULAR_QDD_DUAL_SIMPLEX_EXACT_V1",
            "MODE RESULT-EXPOSED PROOF-FIRST",
        )
    )

    phi5_low = (1, 1, 1, 1, 1)
    phi5_at_zeta = QZERO
    for coefficient in reversed(phi5_low):
        phi5_at_zeta = q5_add(q5_mul(phi5_at_zeta, ZETA), coefficient)
    j_value = q5_add(QONE, q5_pow(ZETA, 2))
    delta_10 = q5_sub(QONE, j_value)
    m_j = q5_regular_matrix(j_value)
    d_j = matsub(m_j, identity(4))
    u_2 = q5_galois_matrix(2)
    expected_m_j = [
        [1, 0, -1, 1],
        [0, 1, -1, 0],
        [1, 0, 0, 0],
        [0, 1, -1, 1],
    ]
    g01 = (
        PROBE == "P-J-CIRCULAR-QDD-DUAL-SIMPLEX-BRIDGE-2"
        and BASE == "3b15217d28575726da1ff3af4de71cba4544637d"
        and CLAIM_LOCK == 801
        and CANON == "v75"
        and phi5_at_zeta == QZERO
        and q5_pow(ZETA, 5) == QONE
        and delta_10 == q5_neg(q5_pow(ZETA, 2))
        and m_j == expected_m_j
        and determinant(m_j) == 1
        and determinant(d_j) == 1
        and matpow(d_j, 5) == identity(4)
        and matpow(u_2, 4) == identity(4)
        and determinant(u_2) == -1
    )
    gate("G01", "FIELD_SOURCE", g01, "identity_guards=exact Phi5=0 M_J,D_J,U2=reconstructed")

    pullback_p = construct_pullback(m_j)
    pullback_s = construct_pullback(u_2)
    omega_1 = [1, 0, 0, 1, 0, 1]
    omega_2 = [0, 1, -1, 0, 1, 0]
    h_matrix = columns_matrix((omega_1, omega_2))
    c_columns = (
        [-1, 0, 1, 0, 0, 0],
        [0, -1, 0, 1, 0, 0],
        [0, -1, 0, 0, 1, 0],
        [-1, 0, 0, 0, 0, 1],
    )
    c_matrix = columns_matrix(c_columns)
    quotient_map = [
        [0, 1, 1, 0, 0, 0],
        [-1, 0, 0, 1, 0, 0],
        [0, -1, 0, 0, 1, 0],
        [-1, 0, 0, 0, 0, 1],
    ]
    quotient_section = columns_matrix(
        (
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
        )
    )
    p_l = matmul(quotient_map, matmul(pullback_p, quotient_section))
    s_l = matmul(quotient_map, matmul(pullback_s, quotient_section))
    expected_p_l = [
        [0, 1, 0, 0],
        [0, 1, 0, -1],
        [0, -1, 1, 1],
        [-1, 1, -1, -1],
    ]
    expected_s_l = [
        [-1, 0, 0, 0],
        [0, 1, 0, -1],
        [1, -1, 0, 0],
        [0, 1, 1, 0],
    ]
    c_in_l = matmul(quotient_map, c_matrix)
    image_one_plus_p = matadd(identity(4), p_l)
    old_seam_p = seam_scalars(p_l, c_in_l, 5)
    old_seam_s = seam_scalars(s_l, c_in_l, 5)
    g02 = (
        matrix_rank(h_matrix) == 2
        and smith_invariants(h_matrix) == [1, 1]
        and matrix_rank(quotient_map) == 4
        and matmul(quotient_map, h_matrix) == zero_matrix(4, 2)
        and matmul(quotient_map, quotient_section) == identity(4)
        and matmul(quotient_map, matmul(pullback_p, h_matrix)) == zero_matrix(4, 2)
        and matmul(quotient_map, matmul(pullback_s, h_matrix)) == zero_matrix(4, 2)
        and p_l == expected_p_l
        and s_l == expected_s_l
        and determinant(p_l) == 1
        and determinant(s_l) == -1
        and abs(determinant(c_in_l)) == 5
        and lattice_equal(c_in_l, image_one_plus_p)
        and old_seam_p == [4]
        and old_seam_s == [2]
    )
    gate("G02", "ALT2_QUOTIENT", g02, "P_L,S_L derived C=(I+P)L primary_seam=(-1,2)")

    p_constraints, symmetric_pairs = invariant_symmetric_constraints(p_l)
    s_constraints, _ = invariant_symmetric_constraints(s_l)
    p_invariant_basis = nullspace(p_constraints)
    joint_invariant_basis = nullspace(p_constraints + s_constraints)
    primitive_form_vector = (
        primitive_integer_vector(joint_invariant_basis[0])
        if len(joint_invariant_basis) == 1
        else None
    )
    g_l = zero_matrix(4, 4)
    if primitive_form_vector is not None:
        for value, (row, column) in zip(primitive_form_vector, symmetric_pairs):
            g_l[row][column] = Fraction(value)
            g_l[column][row] = Fraction(value)
    expected_g_l = [
        [2, 0, 1, 0],
        [0, 2, 0, -1],
        [1, 0, 2, 1],
        [0, -1, 1, 2],
    ]
    leading_minors = [
        determinant([row[:size] for row in g_l[:size]]) for size in range(1, 5)
    ]

    g03 = (
        len(p_invariant_basis) == 2
        and len(joint_invariant_basis) == 1
        and primitive_form_vector is not None
        and g_l == expected_g_l
        and leading_minors == [2, 4, 6, 5]
        and matmul(transpose(p_l), matmul(g_l, p_l)) == g_l
        and matmul(transpose(s_l), matmul(g_l, s_l)) == g_l
    )
    gate("G03", "COMMON_FORM_GUARD", g03, "dim_P=2 dim_PS=1 primitive_Gram positive")

    root_change = [
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, -1, 0, 0],
        [0, 0, 1, 0],
    ]
    cartan_a4 = [
        [2, -1, 0, 0],
        [-1, 2, -1, 0],
        [0, -1, 2, -1],
        [0, 0, -1, 2],
    ]
    g04 = (
        abs(determinant(root_change)) == 1
        and matmul(transpose(root_change), matmul(g_l, root_change)) == cartan_a4
        and determinant(g_l) == 5
        and smith_invariants(g_l) == [1, 1, 1, 5]
        and g_l == transpose(g_l)
        and is_integral_matrix(g_l)
        and all(g_l[index][index].numerator % 2 == 0 for index in range(4))
    )
    gate("G04", "A4_ROOT_AND_NONORTHOGONALITY", g04, "L=A4 even det=5 discriminant=Z/5")

    all_ones = [[Fraction(1) for _ in range(4)] for _ in range(4)]
    g_qdd = matsub(identity(4), matscale(all_ones, Fraction(1, 5)))
    e_zero = [1, 0, 0, 0]
    u_vectors = [matvec(matpow(d_j, exponent), e_zero) for exponent in range(5)]
    u_basis = columns_matrix(u_vectors[:4])
    u_basis_inverse = safe_inverse(u_basis)
    simplex_gram = [
        [bilinear(left, g_qdd, right) for right in u_vectors] for left in u_vectors
    ]
    expected_simplex_gram = [
        [Fraction(4, 5) if row == column else Fraction(-1, 5) for column in range(5)]
        for row in range(5)
    ]
    simplex_ok = (
        [sum((vector[index] for vector in u_vectors), Fraction(0)) for index in range(4)]
        == [0, 0, 0, 0]
        and u_basis_inverse is not None
        and abs(determinant(u_basis)) == 1
        and simplex_gram == expected_simplex_gram
        and matmul(transpose(d_j), matmul(g_qdd, d_j)) == g_qdd
    )

    rho = {}
    rho_defined = u_basis_inverse is not None
    if rho_defined:
        for multiplier in (1, 2, 3, 4):
            for translation in range(5):
                target_columns = [
                    u_vectors[(translation + multiplier * index) % 5]
                    for index in range(4)
                ]
                rho[(multiplier, translation)] = matmul(
                    columns_matrix(target_columns), u_basis_inverse
                )
    rho_30 = rho.get((3, 0), zero_matrix(4, 4))
    expected_rho_30 = [
        [1, 0, 0, -1],
        [0, 0, 1, -1],
        [0, 0, 0, -1],
        [0, 1, 0, -1],
    ]
    rho_law = rho_defined and len({matrix_key(value) for value in rho.values()}) == 20
    if rho_law:
        for (left_c, left_b), left in rho.items():
            for (right_c, right_b), right in rho.items():
                target = rho[
                    (
                        (left_c * right_c) % 5,
                        (left_b + left_c * right_b) % 5,
                    )
                ]
                rho_law = rho_law and matmul(left, right) == target
        for (multiplier, translation), action in rho.items():
            rho_law = rho_law and (
                matmul(transpose(action), matmul(g_qdd, action)) == g_qdd
                and all(
                    matvec(action, u_vectors[index])
                    == u_vectors[(translation + multiplier * index) % 5]
                    for index in range(5)
                )
            )
    g05 = (
        simplex_ok
        and rho_law
        and rho_30 == expected_rho_30
        and rho.get((1, 1)) == d_j
        and rho.get((2, 0)) == u_2
        and all(is_integral_matrix(action) for action in rho.values())
    )
    gate("G05", "QDD_SIMPLEX", g05, "simplex_Gram=(4,-1)/5 rho_family=20 faithful_orthogonal")

    bridge_constraints = intertwiner_constraints(d_j, matscale(p_l, -1))
    bridge_constraints += intertwiner_constraints(rho_30, matscale(s_l, -1))
    bridge_nullspace = nullspace(bridge_constraints)
    primitive_bridge_vector = (
        primitive_integer_vector(bridge_nullspace[0]) if len(bridge_nullspace) == 1 else None
    )
    bridge_a = (
        reshape(primitive_bridge_vector, 4, 4)
        if primitive_bridge_vector is not None
        else zero_matrix(4, 4)
    )
    expected_bridge_a = [
        [4, -1, -1, -1],
        [1, 1, 1, -4],
        [-3, 2, 2, 2],
        [2, -3, 2, -3],
    ]
    bridge_t = matscale(bridge_a, Fraction(1, 5))
    g06 = (
        len(bridge_nullspace) == 1
        and primitive_bridge_vector is not None
        and bridge_a == expected_bridge_a
        and determinant(bridge_a) == -125
        and determinant(bridge_t) == Fraction(-1, 5)
    )
    gate("G06", "BRIDGE_RECONSTRUCTION", g06, "Hom_dim=1 primitive_A=5T detT=-1/5")

    g_l_inverse = safe_inverse(g_l)
    bridge_t_inverse = safe_inverse(bridge_t)
    dual_certificate = matmul(g_l, bridge_t)
    expected_dual_certificate = [
        [1, 0, 0, 0],
        [0, 1, 0, -1],
        [0, 0, 1, 0],
        [0, -1, 1, 0],
    ]
    lambda_value = q5_sub(ZETA, QONE)
    lambda_matrix = q5_regular_matrix(lambda_value)
    lambda_square_matrix = matmul(lambda_matrix, lambda_matrix)
    image_lambda = matmul(bridge_t, lambda_matrix)
    image_lambda_square = matmul(bridge_t, lambda_square_matrix)
    total_inclusion = (
        matmul(bridge_t_inverse, c_in_l)
        if bridge_t_inverse is not None
        else zero_matrix(4, 4)
    )
    g07 = (
        g_l_inverse is not None
        and bridge_t_inverse is not None
        and dual_certificate == expected_dual_certificate
        and is_integral_matrix(dual_certificate)
        and abs(determinant(dual_certificate)) == 1
        and is_integral_matrix(bridge_t_inverse)
        and abs(determinant(bridge_t_inverse)) == 5
        and abs(determinant(lambda_matrix)) == 5
        and abs(determinant(lambda_square_matrix)) == 25
        and lattice_equal(image_lambda, identity(4))
        and lattice_equal(image_lambda_square, c_in_l)
        and abs(determinant(image_lambda)) == 1
        and abs(determinant(image_lambda_square)) == 5
        and smith_invariants(total_inclusion) == [1, 1, 5, 5]
        and lattice_equal(c_in_l, image_one_plus_p)
    )
    gate("G07", "DUAL_LATTICE", g07, "T(lambda2O,lambdaO,O)=(C,L,Ldual) indices=(5,5)")

    g08 = matmul(transpose(bridge_t), matmul(g_l, bridge_t)) == g_qdd
    gate("G08", "METRIC_ISOMETRY", g08, "T^T_G_L_T=G_QDD exact")

    w_vectors = [matvec(bridge_t, vector) for vector in u_vectors]
    oriented_p = all(
        matvec(matscale(p_l, -1), w_vectors[index]) == w_vectors[(index + 1) % 5]
        for index in range(5)
    )
    oriented_s = all(
        matvec(matscale(s_l, -1), w_vectors[index]) == w_vectors[(3 * index) % 5]
        for index in range(5)
    )
    g09 = (
        matmul(bridge_t, d_j) == matmul(matscale(p_l, -1), bridge_t)
        and matmul(bridge_t, rho_30) == matmul(matscale(s_l, -1), bridge_t)
        and oriented_p
        and oriented_s
        and matmul(bridge_t, d_j) != matmul(p_l, bridge_t)
        and matmul(bridge_t, rho_30) != matmul(s_l, bridge_t)
    )
    gate("G09", "SIGNED_INTERTWINING", g09, "D->-P rho30->-S oriented_simplex_preserved")

    dual_action_p = (
        matmul(bridge_t_inverse, matmul(p_l, bridge_t))
        if bridge_t_inverse is not None
        else zero_matrix(4, 4)
    )
    dual_action_s = (
        matmul(bridge_t_inverse, matmul(s_l, bridge_t))
        if bridge_t_inverse is not None
        else zero_matrix(4, 4)
    )
    dual_inclusion = bridge_t_inverse if bridge_t_inverse is not None else zero_matrix(4, 4)
    dual_seam_p = seam_scalars(dual_action_p, dual_inclusion, 5)
    dual_seam_s = seam_scalars(dual_action_s, dual_inclusion, 5)
    dual_seam_minus_p = seam_scalars(matscale(dual_action_p, -1), dual_inclusion, 5)
    dual_seam_minus_s = seam_scalars(matscale(dual_action_s, -1), dual_inclusion, 5)
    same_oriented_class = all(
        all(Fraction(value).denominator == 1 for value in matsub([w_vectors[index]], [w_vectors[0]])[0])
        for index in range(5)
    )
    congruence_kernel_basis = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [-1, -1, -1, 5],
    ]
    coordinate_sum = [[1, 1, 1, 1]]
    kernel_sums = matmul(coordinate_sum, congruence_kernel_basis)[0]
    d_quotient_rows = matmul(coordinate_sum, matsub(d_j, identity(4)))[0]
    r_quotient_rows = matmul(coordinate_sum, matsub(rho_30, identity(4)))[0]
    g10 = (
        smith_invariants(dual_inclusion) == [1, 1, 1, 5]
        and abs(determinant(congruence_kernel_basis)) == 5
        and all(value.numerator % 5 == 0 for value in kernel_sums)
        and lattice_equal(dual_inclusion, congruence_kernel_basis)
        and all(value.numerator % 5 == 0 for value in d_quotient_rows)
        and all(value.numerator % 5 == 0 for value in r_quotient_rows)
        and dual_seam_p == [4]
        and dual_seam_s == [4]
        and dual_seam_minus_p == [1]
        and dual_seam_minus_s == [1]
        and old_seam_p == [4]
        and old_seam_s == [2]
        and (dual_seam_p, dual_seam_s) != (old_seam_p, old_seam_s)
        and same_oriented_class
    )
    gate("G10", "DISCRIMINANT_SEAMS", g10, "Ldual/L=(-1,-1) L/C=(-1,2) kept_distinct")

    cauchy_matrix = matsub(matscale(identity(4), 4), all_ones)
    cauchy_sum = sum_matrices(
        [
            outer(
                [int(index == left) - int(index == right) for index in range(4)],
                [int(index == left) - int(index == right) for index in range(4)],
            )
            for left, right in combinations(range(4), 2)
        ],
        4,
        4,
    )
    bounded_vectors = list(product(range(-2, 3), repeat=4))
    low_shell = {
        tuple(vector)
        for vector in bounded_vectors
        if vector != (0, 0, 0, 0)
        and bilinear(vector, g_qdd, vector) <= Fraction(4, 5)
    }
    expected_low_shell = {tuple(map(int, vector)) for vector in u_vectors}
    expected_low_shell |= {tuple(-int(value) for value in vector) for vector in u_vectors}
    mapped_shell = {tuple(vector) for vector in w_vectors}
    mapped_shell |= {tuple(-value for value in vector) for vector in w_vectors}
    difference_basis = columns_matrix(
        [
            [w_vectors[index][coordinate] - w_vectors[0][coordinate] for coordinate in range(4)]
            for index in range(1, 5)
        ]
    )
    g11 = (
        cauchy_matrix == cauchy_sum
        and matscale(g_qdd, 5) == matadd(identity(4), cauchy_sum)
        and len(bounded_vectors) == 625
        and low_shell == expected_low_shell
        and len(low_shell) == 10
        and len(mapped_shell) == 10
        and all(
            is_integral_matrix(columns_matrix((vector,)))
            for vector in [matvec(g_l, shell_vector) for shell_vector in w_vectors]
        )
        and all(bilinear(vector, g_l, vector) == Fraction(4, 5) for vector in w_vectors)
        and is_integral_matrix(difference_basis)
        and abs(determinant(difference_basis)) == 1
    )
    gate("G11", "MINIMUM_SHELL", g11, "min=4/5 vectors=10 antipodal_classes=5 bound=625")

    qdd_projectors = [orthogonal_projector(vector, g_qdd) for vector in u_vectors]
    l_projectors = [orthogonal_projector(vector, g_l) for vector in w_vectors]
    projectors_defined = all(projector is not None for projector in qdd_projectors + l_projectors)
    stabilizer_projectors = []
    if rho_defined:
        for token in range(5):
            stabilizer_projectors.append(
                matscale(
                    sum_matrices(
                        [rho[(multiplier, token * (1 - multiplier) % 5)] for multiplier in (1, 2, 3, 4)],
                        4,
                        4,
                    ),
                    Fraction(1, 4),
                )
            )
    projectors_match = projectors_defined and bridge_t_inverse is not None and rho_defined
    if projectors_match:
        for token in range(5):
            projectors_match = projectors_match and (
                stabilizer_projectors[token] == qdd_projectors[token]
                and matmul(bridge_t, matmul(qdd_projectors[token], bridge_t_inverse))
                == l_projectors[token]
            )
    projector_sum = (
        sum_matrices(l_projectors, 4, 4) if projectors_defined else zero_matrix(4, 4)
    )
    projector_formula_ok = projectors_defined
    projector_overlap_ok = projectors_defined
    if projectors_defined:
        for token in range(5):
            qdd_formula = matscale(
                outer(u_vectors[token], matmul([u_vectors[token]], g_qdd)[0]),
                Fraction(5, 4),
            )
            l_formula = matscale(
                outer(w_vectors[token], matmul([w_vectors[token]], g_l)[0]),
                Fraction(5, 4),
            )
            projector_formula_ok = projector_formula_ok and (
                qdd_projectors[token] == qdd_formula
                and l_projectors[token] == l_formula
                and matvec(l_projectors[token], w_vectors[token]) == w_vectors[token]
            )
        for left in range(5):
            for right in range(5):
                expected_overlap = Fraction(1) if left == right else Fraction(1, 16)
                projector_overlap_ok = projector_overlap_ok and (
                    trace(matmul(l_projectors[left], l_projectors[right]))
                    == expected_overlap
                )
    nonorthogonal_pairs = projectors_defined and all(
        matmul(l_projectors[left], l_projectors[right]) != zero_matrix(4, 4)
        for left, right in combinations(range(5), 2)
    )
    g12 = (
        projectors_match
        and projector_formula_ok
        and projector_overlap_ok
        and g_l_inverse is not None
        and all(
            matmul(projector, projector) == projector
            and matrix_rank(projector) == 1
            and trace(projector) == 1
            and sharp(projector, g_l, g_l_inverse) == projector
            for projector in l_projectors
        )
        and projector_sum == matscale(identity(4), Fraction(5, 4))
        and projector_sum != identity(4)
        and nonorthogonal_pairs
        and all(not is_integral_matrix(projector) for projector in l_projectors)
    )
    gate("G12", "PROJECTOR_FORMULAS", g12, "averages_transported sum=5/4I cross_trace=1/16 fractional=yes")

    transformed_rho = []
    affine_transport = rho_defined and bridge_t_inverse is not None and projectors_defined
    if affine_transport:
        for (multiplier, translation), action in rho.items():
            transformed = matmul(bridge_t, matmul(action, bridge_t_inverse))
            transformed_rho.append(transformed)
            transformed_inverse = safe_inverse(transformed)
            action_inverse = safe_inverse(action)
            if transformed_inverse is None or action_inverse is None:
                affine_transport = False
                continue
            exponent = {1: 0, 3: 1, 4: 2, 2: 3}[multiplier]
            signed_word = matmul(
                matpow(matscale(p_l, -1), translation),
                matpow(matscale(s_l, -1), exponent),
            )
            affine_transport = affine_transport and transformed == signed_word
            for token in range(5):
                target = (translation + multiplier * token) % 5
                affine_transport = affine_transport and (
                    matmul(action, matmul(qdd_projectors[token], action_inverse))
                    == qdd_projectors[target]
                    and matmul(transformed, matmul(l_projectors[token], transformed_inverse))
                    == l_projectors[target]
                )
    h_group = bounded_group_closure((matscale(p_l, -1), matscale(s_l, -1)), 64)
    transformed_keys = {matrix_key(matrix) for matrix in transformed_rho}
    h_keys = {matrix_key(matrix) for matrix in h_group} if h_group is not None else set()
    g13 = (
        affine_transport
        and h_group is not None
        and len(h_group) == 20
        and len(transformed_keys) == 20
        and h_keys == transformed_keys
    )
    gate("G13", "AFFINE_TRANSPORT", g13, "signed_formula family=20 projector_transport=exact")

    full_group = bounded_group_closure((p_l, s_l), 96)
    full_keys = {matrix_key(matrix) for matrix in full_group} if full_group is not None else set()
    minus_h_keys = {matrix_key(matscale(matrix, -1)) for matrix in h_group} if h_group else set()
    projective_keys = {projective_key(matrix) for matrix in full_group} if full_group else set()
    old_complement = bounded_group_closure((matscale(p_l, -1), s_l), 64)
    old_complement_keys = (
        {matrix_key(matrix) for matrix in old_complement}
        if old_complement is not None
        else set()
    )
    projector_kernel = []
    if full_group is not None and projectors_defined:
        for matrix in full_group:
            matrix_inverse = safe_inverse(matrix)
            if matrix_inverse is None:
                projector_kernel = []
                break
            if all(
                matmul(matrix, matmul(projector, matrix_inverse)) == projector
                for projector in l_projectors
            ):
                projector_kernel.append(matrix)
    g14 = (
        full_group is not None
        and h_group is not None
        and old_complement is not None
        and len(full_group) == 40
        and len(h_group) == 20
        and len(old_complement) == 20
        and matrix_key(matscale(identity(4), -1)) not in h_keys
        and h_keys.isdisjoint(minus_h_keys)
        and full_keys == h_keys | minus_h_keys
        and len(projective_keys) == 20
        and h_keys != old_complement_keys
        and len(h_keys & old_complement_keys) == 10
        and {matrix_key(matrix) for matrix in projector_kernel}
        == {matrix_key(identity(4)), matrix_key(matscale(identity(4), -1))}
        and matpow(p_l, 5) == matscale(identity(4), -1)
        and len(h_group) not in (120, 240)
        and len(full_group) not in (120, 240)
    )
    gate("G14", "SPLIT_SIGN_GROUP", g14, "affine_subgroup=20 full=40 split=yes projective_kernel=2 old_intersection=10")

    g15 = (
        not is_integral_matrix(bridge_t)
        and not lattice_equal(bridge_t, identity(4))
        and len(low_shell) == 10
        and len({frozenset((vector, tuple(-value for value in vector))) for vector in mapped_shell}) == 5
        and all(
            matvec(p_l, w_vectors[index]) == [-value for value in w_vectors[(index + 1) % 5]]
            for index in range(5)
        )
        and all(
            matvec(s_l, w_vectors[index]) == [-value for value in w_vectors[(3 * index) % 5]]
            for index in range(5)
        )
        and matmul(bridge_t, d_j) != matmul(p_l, bridge_t)
        and matmul(bridge_t, rho_30) != matmul(s_l, bridge_t)
        and old_seam_s != dual_seam_s
        and SCOPE_LINE
        == "SCOPE L1_only Born=NONE probability=NONE measurement=NONE apparatus=NONE "
        "physical_qudit=NONE decoder_completion=NONE L2-L6=NONE"
    )
    gate(
        "G15",
        "NEGATIVE_CONTROLS_AND_FIREWALL",
        g15,
        "typed_carriers_distinct signs_fixed shell=10 seams_distinct physical_scope=NONE",
    )

    claim_a_gates = tuple("G%02d" % index for index in range(1, 12)) + ("G15",)
    claim_b_gates = (
        "G01",
        "G02",
        "G05",
        "G06",
        "G07",
        "G08",
        "G09",
        "G10",
        "G12",
        "G13",
        "G14",
        "G15",
    )
    claim_a_ok = all(code not in FAILURES for code in claim_a_gates)
    claim_b_ok = all(code not in FAILURES for code in claim_b_gates)

    OUTPUT.append(
        "RESULT CLAIM_A %s %s" % (CLAIM_A, "CONFIRMED" if claim_a_ok else "FIRED")
    )
    OUTPUT.append(
        "RESULT CLAIM_B %s %s" % (CLAIM_B, "CONFIRMED" if claim_b_ok else "FIRED")
    )
    OUTPUT.append(
        "BOUNDARY root_lattice=A4 dual_lattice=A4star minimal_vectors=10 "
        "antipodal_classes=5 linear_group=40 projective_projector_group=20"
    )
    OUTPUT.append(SCOPE_LINE)
    if claim_a_ok and claim_b_ok and not FAILURES:
        OUTPUT.append("RESULT OVERALL PASS gates=15 claims=2")
    else:
        confirmed = int(claim_a_ok) + int(claim_b_ok)
        OUTPUT.append(
            "RESULT OVERALL FIRED gates_pass=%d/15 claims_confirmed=%d/2"
            % (15 - len(FAILURES), confirmed)
        )

    print("\n".join(OUTPUT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
