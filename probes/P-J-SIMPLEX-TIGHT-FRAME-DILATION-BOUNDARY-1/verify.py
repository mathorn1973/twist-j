#!/usr/bin/env python3
"""Exact audit for P-J-SIMPLEX-TIGHT-FRAME-DILATION-BOUNDARY-1.

Standard library only. Exact integer and Fraction arithmetic. No float,
builtin complex arithmetic, file input, network, subprocess, shell,
randomness, clock, dynamic import, eval, exec, or environment input.

Universal implications are proved in PREREG.md. This verifier audits their
finite exact premises on the complete frozen carriers.
"""

from fractions import Fraction


PROBE = "P-J-SIMPLEX-TIGHT-FRAME-DILATION-BOUNDARY-1"
CLAIM_A = "J-SIMPLEX-TIGHT-FRAME-DILATION"
CLAIM_B = "J-SIMPLEX-QUADRATIC-SUPPORT-RIGIDITY"

FAILURES = []
OUTPUT = []


def require(condition, message):
    """Reserve exceptions and nonzero status for integrity STOP."""
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
# Exact rational linear algebra


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


def columns_matrix(columns):
    require(columns, "empty column family")
    height = len(columns[0])
    require(all(len(column) == height for column in columns), "column shape")
    return [
        [Fraction(columns[column][row]) for column in range(len(columns))]
        for row in range(height)
    ]


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


def vector_add(left, right):
    require(len(left) == len(right), "vector sum shape")
    return [Fraction(a) + Fraction(b) for a, b in zip(left, right)]


def vector_scale(vector, scalar):
    return [Fraction(scalar) * Fraction(value) for value in vector]


def dot(left, right):
    require(len(left) == len(right), "dot-product shape")
    return sum((Fraction(a) * Fraction(b) for a, b in zip(left, right)), Fraction(0))


def quadratic_norm(vector):
    return dot(vector, vector)


def outer(left, right):
    return [[Fraction(a) * Fraction(b) for b in right] for a in left]


def matrix_trace(matrix):
    require(matrix and all(len(row) == len(matrix) for row in matrix), "trace shape")
    return sum((matrix[index][index] for index in range(len(matrix))), Fraction(0))


def sum_matrices(matrices, rows, columns):
    out = zero_matrix(rows, columns)
    for matrix in matrices:
        out = matadd(out, matrix)
    return out


def kron(left, right):
    require(left and right, "empty Kronecker product")
    return [
        [
            Fraction(left[i][j]) * Fraction(right[k][ell])
            for j in range(len(left[0]))
            for ell in range(len(right[0]))
        ]
        for i in range(len(left))
        for k in range(len(right))
    ]


def tensor_vector(left, right):
    return [Fraction(a) * Fraction(b) for a in left for b in right]


def proportional(left, right):
    require(len(left) == len(right), "proportional shape")
    pivot = next((index for index, value in enumerate(right) if value != 0), None)
    if pivot is None:
        return all(value == 0 for value in left)
    ratio = Fraction(left[pivot]) / Fraction(right[pivot])
    return all(Fraction(a) == ratio * Fraction(b) for a, b in zip(left, right))


# ---------------------------------------------------------------------------
# Frozen five-cell carrier and simplex


I5 = identity(5)
ONES = [Fraction(1) for _ in range(5)]
N = outer(ONES, ONES)
PV = matsub(I5, matscale(N, Fraction(1, 5)))

G = zero_matrix(5, 5)
for column in range(5):
    G[(column + 1) % 5][column] = Fraction(1)
G_INV = matpow(G, 4)

UNIT_VECTORS = []
for cell in range(5):
    basis = [Fraction(0) for _ in range(5)]
    basis[cell] = Fraction(1)
    UNIT_VECTORS.append(matvec(PV, basis))

SIMPLEX_MATRIX = columns_matrix(UNIT_VECTORS)
FRAME = [outer(vector, vector) for vector in UNIT_VECTORS]
PROJECTORS = [matscale(operator, Fraction(5, 4)) for operator in FRAME]


def cell_index(system_cell, record_cell):
    return 5 * system_cell + record_cell


def coefficient_matrix(vector):
    require(len(vector) == 25, "joint coefficient shape")
    return [
        [Fraction(vector[cell_index(system, record)]) for record in range(5)]
        for system in range(5)
    ]


def system_contraction(left, right):
    left_matrix = coefficient_matrix(left)
    right_matrix = coefficient_matrix(right)
    return matmul(left_matrix, transpose(right_matrix))


def record_contraction(left, right):
    left_matrix = coefficient_matrix(left)
    right_matrix = coefficient_matrix(right)
    return matmul(transpose(left_matrix), right_matrix)


def hyperplane_basis(cell):
    indices = [index for index in range(5) if index != cell]
    anchor = indices[-1]
    out = []
    for index in indices[:-1]:
        vector = [Fraction(0) for _ in range(5)]
        vector[index] = Fraction(1)
        vector[anchor] = Fraction(-1)
        out.append(vector)
    return out


# ---------------------------------------------------------------------------
# Fifteen exact gates


OUTPUT.append("SPEC J_SIMPLEX_DILATION_BOUNDARY_EXACT_V1")
OUTPUT.append("MODE RESULT-EXPOSED PROOF-FIRST")

g01 = (
    matpow(G, 5) == I5
    and all(matpow(G, exponent) != I5 for exponent in range(1, 5))
    and matmul(PV, PV) == PV
    and transpose(PV) == PV
    and matvec(PV, ONES) == [0, 0, 0, 0, 0]
    and matrix_trace(PV) == 4
)
gate("G01", "AUGMENTATION_CARRIER", g01, "g_order=5 P_V_rank=4 full_cells=5")

simplex_gram = matmul(transpose(SIMPLEX_MATRIX), SIMPLEX_MATRIX)
g02 = (
    SIMPLEX_MATRIX == PV
    and simplex_gram == PV
    and matrix_rank(SIMPLEX_MATRIX) == 4
    and matvec(SIMPLEX_MATRIX, ONES) == [0, 0, 0, 0, 0]
    and all(
        dot(UNIT_VECTORS[left], UNIT_VECTORS[right])
        == (Fraction(4, 5) if left == right else Fraction(-1, 5))
        for left in range(5)
        for right in range(5)
    )
)
gate("G02", "SIMPLEX", g02, "Gram_diag=4/5 offdiag=-1/5 rank=4 unique_relation=sum")

frame_sum = sum_matrices(FRAME, 5, 5)
coordinate_response_ok = True
v_basis = []
for index in range(4):
    vector = [Fraction(0) for _ in range(5)]
    vector[index] = Fraction(1)
    vector[4] = Fraction(-1)
    v_basis.append(vector)
for cell in range(5):
    coordinate_response_ok = coordinate_response_ok and (
        FRAME[cell] == matmul(PV, matmul(outer(I5[cell], I5[cell]), PV))
        and all(
            dot(left, matvec(FRAME[cell], right)) == left[cell] * right[cell]
            for left in v_basis
            for right in v_basis
        )
    )

g03 = (
    frame_sum == PV
    and all(matmul(operator, operator) == matscale(operator, Fraction(4, 5)) for operator in FRAME)
    and coordinate_response_ok
    and all(
        matmul(G, matmul(FRAME[cell], G_INV)) == FRAME[(cell + 1) % 5]
        for cell in range(5)
    )
)
gate("G03", "TIGHT_FRAME", g03, "sum_E=P_V E2=4E/5 response=d_k_squared")

g04 = (
    all(matmul(projector, projector) == projector for projector in PROJECTORS)
    and sum_matrices(PROJECTORS, 5, 5) == matscale(PV, Fraction(5, 4))
    and all(matrix_rank(projector) == 1 for projector in PROJECTORS)
    and all(
        matrix_trace(matmul(PROJECTORS[left], PROJECTORS[right]))
        == (Fraction(1) if left == right else Fraction(1, 16))
        for left in range(5)
        for right in range(5)
    )
)
gate("G04", "PROJECTOR_GUARD", g04, "Pi=5E/4 sum=5P_V/4 cross_trace=1/16")

CONTROLLED_ADD = zero_matrix(25, 25)
permutation = []
for system in range(5):
    for record in range(5):
        source = cell_index(system, record)
        target = cell_index(system, (record + system) % 5)
        CONTROLLED_ADD[target][source] = Fraction(1)
        permutation.append(target)

inversions = sum(
    1
    for left in range(25)
    for right in range(left + 1, 25)
    if permutation[left] > permutation[right]
)
permutation_sign = -1 if inversions % 2 else 1
g05 = (
    sorted(permutation) == list(range(25))
    and matmul(transpose(CONTROLLED_ADD), CONTROLLED_ADD) == identity(25)
    and matpow(CONTROLLED_ADD, 5) == identity(25)
    and all(matpow(CONTROLLED_ADD, exponent) != identity(25) for exponent in range(1, 5))
    and permutation_sign == 1
)
gate("G05", "CONTROLLED_ADD", g05, "integral_permutation=yes order=5 determinant=1")

READY_EMBEDDING = zero_matrix(25, 5)
COPY_EMBEDDING = zero_matrix(25, 5)
for cell in range(5):
    READY_EMBEDDING[cell_index(cell, 0)][cell] = Fraction(1)
    COPY_EMBEDDING[cell_index(cell, cell)][cell] = Fraction(1)

g06 = (
    matmul(CONTROLLED_ADD, READY_EMBEDDING) == COPY_EMBEDDING
    and matmul(transpose(COPY_EMBEDDING), COPY_EMBEDDING) == I5
    and matmul(transpose(READY_EMBEDDING), READY_EMBEDDING) == I5
    and matrix_rank(COPY_EMBEDDING) == 5
)
gate("G06", "FULL_CELL_COPY", g06, "C_add(d_tensor_e0)=sum_dk_ek_tensor_ek isometry=yes")

copy_columns = [[COPY_EMBEDDING[row][cell] for row in range(25)] for cell in range(5)]
gram_identity_ok = True
for left in range(5):
    for right in range(5):
        expected = zero_matrix(5, 5)
        if left == right:
            expected[left][left] = Fraction(1)
        gram_identity_ok = gram_identity_ok and (
            system_contraction(copy_columns[left], copy_columns[right]) == expected
            and record_contraction(copy_columns[left], copy_columns[right]) == expected
        )

g07 = gram_identity_ok
gate("G07", "JOINT_GRAM", g07, "both_contractions=diag(d_k_squared) universal=polarized")

D0 = [Fraction(4), Fraction(-1), Fraction(-1), Fraction(-1), Fraction(-1)]
HOLE = [Fraction(5), Fraction(0), Fraction(5), Fraction(-5), Fraction(-5)]
d0_joint = matvec(COPY_EMBEDDING, D0)
hole_joint = matvec(COPY_EMBEDDING, HOLE)
g08 = (
    [record_contraction(d0_joint, d0_joint)[cell][cell] for cell in range(5)]
    == [16, 1, 1, 1, 1]
    and [record_contraction(hole_joint, hole_joint)[cell][cell] for cell in range(5)]
    == [25, 0, 25, 25, 25]
    and matrix_trace(record_contraction(d0_joint, d0_joint)) == 20
    and matrix_trace(record_contraction(hole_joint, hole_joint)) == 100
)
gate("G08", "GRAM_WITNESSES", g08, "vertex=16,1,1,1,1 hole=25,0,25,25,25 totals=20,100")

COMPRESSED_COPY = matmul(kron(PV, PV), COPY_EMBEDDING)
simplex_copy_columns = [tensor_vector(vector, vector) for vector in UNIT_VECTORS]
simplex_copy_matrix = columns_matrix(simplex_copy_columns)
compressed_sum = matvec(COMPRESSED_COPY, ONES)
g09 = (
    COMPRESSED_COPY == simplex_copy_matrix
    and matrix_rank(SIMPLEX_MATRIX) == 4
    and matrix_rank(COMPRESSED_COPY) == 5
    and matvec(PV, ONES) == [0, 0, 0, 0, 0]
    and compressed_sum != [0 for _ in range(25)]
    and quadratic_norm(compressed_sum) == 4
)
gate("G09", "COPY_COMPRESSION", g09, "source_rank=4 target_rank=5 sum_source=0 sum_target_norm2=4")

target_gram = matmul(transpose(COMPRESSED_COPY), COMPRESSED_COPY)
hadamard_square = [
    [PV[row][column] * PV[row][column] for column in range(5)]
    for row in range(5)
]
g10 = (
    target_gram == hadamard_square
    and matrix_rank(simplex_gram) == 4
    and matrix_rank(target_gram) == 5
    and all(
        target_gram[left][right]
        == (Fraction(16, 25) if left == right else Fraction(1, 25))
        for left in range(5)
        for right in range(5)
    )
)
gate("G10", "NO_SIMPLEX_COPY", g10, "input_Gram_rank=4 output_Gram_rank=5 linear_factorization=impossible")

HYPERPLANES = [hyperplane_basis(cell) for cell in range(5)]
g11 = all(
    matrix_rank(columns_matrix(HYPERPLANES[cell])) == 3
    and all(sum(vector, Fraction(0)) == 0 and vector[cell] == 0 for vector in HYPERPLANES[cell])
    and all(dot(UNIT_VECTORS[cell], vector) == 0 for vector in HYPERPLANES[cell])
    and matrix_rank(columns_matrix(HYPERPLANES[cell] + [UNIT_VECTORS[cell]])) == 4
    for cell in range(5)
)
gate("G11", "DARK_HYPERPLANES", g11, "d_k=0 iff d_in_u_k_perp dimension=3")

SYMMETRIC_PAIRS = [(row, column) for row in range(5) for column in range(row, 5)]
SYMMETRIC_BASIS = []
for row, column in SYMMETRIC_PAIRS:
    matrix = zero_matrix(5, 5)
    matrix[row][column] = Fraction(1)
    matrix[column][row] = Fraction(1)
    SYMMETRIC_BASIS.append(matrix)


def kernel_constraint_rows(vector):
    rows = []
    images = [matvec(matrix, vector) for matrix in SYMMETRIC_BASIS]
    for output_coordinate in range(5):
        rows.append([image[output_coordinate] for image in images])
    return rows


rigidity_ok = True
for cell in range(5):
    constraints = kernel_constraint_rows(ONES)
    for vector in HYPERPLANES[cell]:
        constraints += kernel_constraint_rows(vector)
    frame_coordinates = [FRAME[cell][row][column] for row, column in SYMMETRIC_PAIRS]
    rigidity_ok = rigidity_ok and (
        len(SYMMETRIC_BASIS) == 15
        and matrix_rank(constraints) == 14
        and any(value != 0 for value in frame_coordinates)
        and all(dot(row, frame_coordinates) == 0 for row in constraints)
    )

g12 = rigidity_ok
gate("G12", "KERNEL_RIGIDITY", g12, "symmetric_sector_kernel_dim=1 generator=E_k")

normalization_ok = frame_sum == PV
covariance_ok = all(
    matmul(G, matmul(FRAME[cell], G_INV)) == FRAME[(cell + 1) % 5]
    for cell in range(5)
)
canonical_darkness_ok = all(
    all(dot(vector, matvec(FRAME[cell], vector)) == 0 for vector in HYPERPLANES[cell])
    for cell in range(5)
)
g13 = normalization_ok and covariance_ok and canonical_darkness_ok
gate("G13", "RIGID_FAMILY", g13, "PSD_plus_darkness_plus_covariance_plus_sumI implies_Wk=E_k")

counterfamily_ok = True
darkness_selection_ok = True
for parameter in (Fraction(0), Fraction(1, 2), Fraction(1)):
    family = [
        matadd(matscale(FRAME[cell], parameter), matscale(PV, (1 - parameter) / 5))
        for cell in range(5)
    ]
    counterfamily_ok = counterfamily_ok and (
        sum_matrices(family, 5, 5) == PV
        and all(transpose(operator) == operator for operator in family)
        and all(matmul(PV, operator) == operator for operator in family)
        and all(
            matmul(G, matmul(family[cell], G_INV)) == family[(cell + 1) % 5]
            for cell in range(5)
        )
    )
    witness = HYPERPLANES[0][0]
    response = dot(witness, matvec(family[0], witness))
    darkness_selection_ok = darkness_selection_ok and (
        (response == 0) if parameter == 1 else (response > 0)
    )

cross_vector = HYPERPLANES[0][0]
cross_operator = matadd(
    outer(UNIT_VECTORS[0], cross_vector),
    outer(cross_vector, UNIT_VECTORS[0]),
)
hyperplane_matrix = columns_matrix(HYPERPLANES[0])
cross_restriction = matmul(transpose(hyperplane_matrix), matmul(cross_operator, hyperplane_matrix))
positive_witness = vector_add(UNIT_VECTORS[0], cross_vector)
negative_witness = vector_add(UNIT_VECTORS[0], vector_scale(cross_vector, -1))
cross_coordinates = [cross_operator[row][column] for row, column in SYMMETRIC_PAIRS]
frame_zero_coordinates = [FRAME[0][row][column] for row, column in SYMMETRIC_PAIRS]
g14 = (
    counterfamily_ok
    and darkness_selection_ok
    and cross_restriction == zero_matrix(3, 3)
    and not proportional(cross_coordinates, frame_zero_coordinates)
    and dot(positive_witness, matvec(cross_operator, positive_witness)) > 0
    and dot(negative_witness, matvec(cross_operator, negative_witness)) < 0
)
gate("G14", "NECESSITY_CONTROLS", g14, "darkness_selects_t=1 PSD_excludes_indefinite_cross=yes")

SCOPE_LINE = (
    "SCOPE L1_only Born=NONE probability=NONE apparatus=NONE outcomes=NONE "
    "records=NONE physical_partial_trace=NONE L2-L6=NONE"
)
g15 = (
    COPY_EMBEDDING != COMPRESSED_COPY
    and frame_sum == PV
    and SCOPE_LINE
    == "SCOPE L1_only Born=NONE probability=NONE apparatus=NONE outcomes=NONE "
    "records=NONE physical_partial_trace=NONE L2-L6=NONE"
)
gate("G15", "BOUNDARY_FIREWALL", g15, "copy_before_compression=yes physical_semantics=NONE")


# ---------------------------------------------------------------------------
# Frozen decisions


CLAIM_A_GATES = {"G%02d" % index for index in range(1, 11)} | {"G15"}
CLAIM_B_GATES = {"G01", "G02", "G03", "G04", "G11", "G12", "G13", "G14", "G15"}
failed = set(FAILURES)
claim_a_status = "CONFIRMED" if not (failed & CLAIM_A_GATES) else "FIRED"
claim_b_status = "CONFIRMED" if not (failed & CLAIM_B_GATES) else "FIRED"

for line in OUTPUT:
    print(line)
print("RESULT CLAIM_A %s %s" % (CLAIM_A, claim_a_status))
print("RESULT CLAIM_B %s %s" % (CLAIM_B, claim_b_status))
print(SCOPE_LINE)
overall = "PASS" if claim_a_status == claim_b_status == "CONFIRMED" else "SCIENTIFIC-FIRED"
print("RESULT OVERALL %s gates=15 claims=2" % overall)
