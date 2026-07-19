#!/usr/bin/env python3
"""Exact audit for P-CARRY-PENTAD-1.

The theorem candidate is proof-first. This verifier exhausts the finite
carriers and checks the declared integral matrices. It uses only exact
integers and the Python standard library.
"""

from itertools import permutations, product
from math import prod


GATES = []


def gate(name, condition):
    GATES.append((name, bool(condition)))


def parity(value):
    return value.bit_count() & 1


def raw_carry(left, right):
    return parity(left & right)


def carry_q(value):
    weight = value.bit_count()
    return (weight * (weight - 1) // 2) & 1


def carry_b(left, right):
    return carry_q(left ^ right) ^ carry_q(left) ^ carry_q(right)


def invertible(columns):
    rows = list(columns)
    rank = 0
    for bit in range(4):
        pivot = next(
            (index for index in range(rank, 4) if (rows[index] >> bit) & 1),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for index in range(4):
            if index != rank and ((rows[index] >> bit) & 1):
                rows[index] ^= rows[rank]
        rank += 1
    return rank == 4


def act(columns, value):
    image = 0
    for bit, column in enumerate(columns):
        if (value >> bit) & 1:
            image ^= column
    return image


def compose(left, right):
    """Column matrix for left after right over F_2."""
    return tuple(act(left, column) for column in right)


def column_power(matrix, exponent):
    result = (1, 2, 4, 8)
    for _ in range(exponent):
        result = compose(result, matrix)
    return result


GL4 = [matrix for matrix in product(range(16), repeat=4) if invertible(matrix)]
F2_IDENTITY = (1, 2, 4, 8)
PENTAD = (1, 2, 4, 8, 15)


def matrix_mul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(4)) for j in range(4)]
        for i in range(4)
    ]


def matrix_add(left, right):
    return [
        [left[i][j] + right[i][j] for j in range(4)] for i in range(4)
    ]


def matrix_sub(left, right):
    return [
        [left[i][j] - right[i][j] for j in range(4)] for i in range(4)
    ]


def matrix_scale(scalar, matrix):
    return [[scalar * entry for entry in row] for row in matrix]


def matrix_transpose(matrix):
    return [[matrix[j][i] for j in range(4)] for i in range(4)]


def matrix_power(matrix, exponent):
    result = [row[:] for row in I4]
    for _ in range(exponent):
        result = matrix_mul(result, matrix)
    return result


def determinant(matrix):
    total = 0
    for permutation in permutations(range(4)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(4)
            for j in range(i + 1, 4)
        )
        term = -1 if inversions & 1 else 1
        for row in range(4):
            term *= matrix[row][permutation[row]]
        total += term
    return total


def polynomial_multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def characteristic_polynomial(matrix):
    """Return coefficients [c_0,...,c_4] of det(XI-matrix)."""
    coefficients = [0] * 5
    for permutation in permutations(range(4)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(4)
            for j in range(i + 1, 4)
        )
        term = [-1 if inversions & 1 else 1]
        for row in range(4):
            factor = (
                [-matrix[row][permutation[row]], 1]
                if row == permutation[row]
                else [-matrix[row][permutation[row]]]
            )
            term = polynomial_multiply(term, factor)
        for degree, coefficient in enumerate(term):
            coefficients[degree] += coefficient
    return coefficients


def coordinate_permutation_matrix(permutation):
    """Action of a permutation of e_0,...,e_4 on a_i=e_i-e_0."""
    matrix = [[0] * 4 for _ in range(4)]
    for column in range(1, 5):
        if permutation[column] != 0:
            matrix[permutation[column] - 1][column - 1] += 1
        if permutation[0] != 0:
            matrix[permutation[0] - 1][column - 1] -= 1
    return matrix


def multiplier_permutation_matrix(multiplier):
    return coordinate_permutation_matrix(
        tuple((multiplier * residue) % 5 for residue in range(5))
    )


def reduce_mod_two(matrix):
    return tuple(
        sum((matrix[row][column] & 1) << row for row in range(4))
        for column in range(4)
    )


I4 = [[1 if row == column else 0 for column in range(4)] for row in range(4)]
C = [
    [-1, -1, -1, -1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
]
C_POWERS = {exponent: matrix_power(C, exponent) for exponent in range(6)}
GRAM = [[2 if row == column else 1 for column in range(4)] for row in range(4)]


# G01-G03: carry strata, polarization, and the minus-type pentad.
e2 = lambda value: sum(
    ((value >> i) & 1) * ((value >> j) & 1)
    for i in range(4)
    for j in range(i + 1, 4)
) & 1
e4 = lambda value: prod((value >> i) & 1 for i in range(4))
gate(
    "G01 carry bits: bit0=t=e1, bit1=q=e2, bit2=e4 on the full four-bit carrier",
    all(
        parity(value) == (value.bit_count() & 1)
        and carry_q(value) == e2(value)
        and ((value.bit_count() >> 2) & 1) == e4(value)
        for value in range(16)
    ),
)
gate(
    "G02 polarization: B(x,y)=t(x)t(y)+d(x,y), alternating with trivial radical",
    all(
        carry_b(left, right)
        == ((parity(left) & parity(right)) ^ raw_carry(left, right))
        for left in range(16)
        for right in range(16)
    )
    and all(carry_b(value, value) == 0 for value in range(16))
    and all(
        any(carry_b(value, witness) for witness in range(16))
        for value in range(1, 16)
    ),
)
q_zeros = tuple(value for value in range(16) if carry_q(value) == 0)
gate(
    "G03 q has Arf 1: six zeros and singular pentad 1,2,4,8,15 with pair value one and XOR zero",
    q_zeros == (0, 1, 2, 4, 8, 15)
    and all(
        carry_b(left, right) == 1
        for left in PENTAD
        for right in PENTAD
        if left != right
    )
    and (1 ^ 2 ^ 4 ^ 8 ^ 15) == 0,
)


# G04: the raw dot/carry form has only the two orthonormal-basis families.
unit_vectors = {1, 2, 4, 8}
complement_vectors = {15 ^ value for value in unit_vectors}
raw_stabilizer = [
    matrix
    for matrix in GL4
    if all(
        raw_carry(matrix[i], matrix[j]) == (1 if i == j else 0)
        for i in range(4)
        for j in range(i, 4)
    )
]
gate(
    "G04 raw d stabilizer: 48=S4xC2, only permutation/complement bases, hence no order five",
    len(raw_stabilizer) == 48
    and all(
        set(matrix) == unit_vectors or set(matrix) == complement_vectors
        for matrix in raw_stabilizer
    )
    and 48 % 5 != 0,
)


# G05-G06: O^-(4,2)=S5 and Sp(4,2)=S6 through faithful finite actions.
symplectic_group = [
    matrix
    for matrix in GL4
    if all(
        carry_b(matrix[i], matrix[j])
        == carry_b(1 << i, 1 << j)
        for i in range(4)
        for j in range(i + 1, 4)
    )
]
orthogonal_group = [
    matrix
    for matrix in GL4
    if all(carry_q(act(matrix, value)) == carry_q(value) for value in range(16))
]
pentad_actions = {
    tuple(PENTAD.index(act(matrix, value)) for value in PENTAD)
    for matrix in orthogonal_group
}
gate(
    "G05 orthogonal action: |O(q)|=120, faithful on the pentad, so O^-(4,2)=S5 inside Sp",
    len(orthogonal_group) == 120
    and len(pentad_actions) == 120
    and all(matrix in symplectic_group for matrix in orthogonal_group),
)
refinement_signatures = {
    vector: tuple(
        carry_q(value) ^ carry_b(vector, value) for value in range(16)
    )
    for vector in range(16)
}
signature_to_vector = {
    signature: vector for vector, signature in refinement_signatures.items()
}
minus_vectors = tuple(
    vector
    for vector, signature in refinement_signatures.items()
    if signature.count(0) == 6
)
sp_actions = set()
for matrix in symplectic_group:
    action = []
    for vector in minus_vectors:
        pulled_back = tuple(
            refinement_signatures[vector][act(matrix, value)]
            for value in range(16)
        )
        action.append(minus_vectors.index(signature_to_vector[pulled_back]))
    sp_actions.add(tuple(action))
gate(
    "G06 refinement action: six minus refinements and 720 faithful Sp actions, so Sp(4,2)=S6 with S5 stabilizer",
    len(symplectic_group) == 720
    and minus_vectors == (0, 1, 2, 4, 8, 15)
    and len(sp_actions) == 720,
)


# G07: width four is minimal once order five is fixed.
gl_order = lambda dimension: prod(
    (1 << dimension) - (1 << index) for index in range(dimension)
)
c_mod_two = reduce_mod_two(C)
gate(
    "G07 fixed-p width gate: ord_5(2)=4 and dimension four is the first GL(n,2) with order-five elements",
    all(
        ((((1 << exponent) - 1) % 5 == 0) == (exponent % 4 == 0))
        for exponent in range(1, 21)
    )
    and all((gl_order(dimension) % 5 == 0) == (dimension >= 4) for dimension in range(1, 13))
    and gl_order(2) == 6
    and gl_order(3) == 168
    and column_power(c_mod_two, 5) == F2_IDENTITY
    and all(column_power(c_mod_two, exponent) != F2_IDENTITY for exponent in range(1, 5)),
)


# G08-G12: cyclotomic lattice, J, integral conjugacy, and ramified quotient.
cyclotomic = [1, 1, 1, 1, 1]
j_characteristic = [1, -2, 4, -3, 1]
operators = {
    exponent: matrix_add(I4, C_POWERS[exponent]) for exponent in range(1, 5)
}
gate(
    "G08 augmentation cycle: C^5=I and char(C)=Phi5",
    C_POWERS[5] == I4
    and C_POWERS[4] != I4
    and characteristic_polynomial(C) == cyclotomic,
)
operator_characteristics = {
    exponent: characteristic_polynomial(operator)
    for exponent, operator in operators.items()
}
gate(
    "G09 shifted cycle: every I+C^a has char Phi5(X-1)=X^4-3X^3+4X^2-2X+1",
    all(
        operator_characteristics[exponent] == j_characteristic
        for exponent in range(1, 5)
    ),
)
conjugacy_ok = True
for exponent in range(1, 5):
    inverse = pow(exponent, -1, 5)
    conjugator = multiplier_permutation_matrix(exponent)
    conjugator_inverse = multiplier_permutation_matrix(inverse)
    conjugacy_ok &= matrix_mul(conjugator, conjugator_inverse) == I4
    conjugacy_ok &= (
        matrix_mul(matrix_mul(conjugator, C), conjugator_inverse)
        == C_POWERS[exponent]
    )
    conjugacy_ok &= (
        matrix_mul(matrix_mul(conjugator, operators[1]), conjugator_inverse)
        == operators[exponent]
    )
    conjugacy_ok &= (
        matrix_mul(matrix_mul(matrix_transpose(conjugator), GRAM), conjugator)
        == GRAM
    )
gate(
    "G10 exponent conjugacy: every r->a*r is an integral A4 isometry sending I+C to I+C^a",
    conjugacy_ok,
)
public_m_j = [
    [1, 0, -1, 1],
    [0, 1, -1, 0],
    [1, 0, 0, 0],
    [0, 1, -1, 1],
]
ideal_basis_change = [
    [1, -1, 0, 0],
    [0, 1, -1, 0],
    [0, 0, 1, -1],
    [0, 0, 0, 1],
]
gate(
    "G11 J bridge: I+C^2 on (zeta-1) is integrally conjugate to the public power-basis M_J",
    determinant(ideal_basis_change) == 1
    and matrix_mul(operators[2], ideal_basis_change)
    == matrix_mul(ideal_basis_change, public_m_j)
    and characteristic_polynomial(public_m_j) == j_characteristic,
)
quotient_ok = determinant(matrix_sub(I4, C)) == 5
for exponent in range(1, 5):
    geometric_sum = [[0] * 4 for _ in range(4)]
    for power in range(exponent):
        geometric_sum = matrix_add(geometric_sum, C_POWERS[power])
    quotient_ok &= (
        matrix_sub(C_POWERS[exponent], I4)
        == matrix_mul(matrix_sub(C, I4), geometric_sum)
    )
    quotient_ok &= (
        matrix_sub(operators[exponent], matrix_scale(2, I4))
        == matrix_sub(C_POWERS[exponent], I4)
    )
    quotient_ok &= [coefficient % 5 for coefficient in operator_characteristics[exponent]] == [1, 3, 4, 2, 1]
gate(
    "G12 ramified quotient: A4/(C-I)A4 has order 5, C=1, every I+C^a=2, and char=(X-2)^4 mod 5",
    quotient_ok,
)


# G13-G17: the correctly typed A4/2A4 bridge.
def q_a(value):
    coordinates = [(value >> index) & 1 for index in range(4)]
    norm = sum(
        coordinates[i] * GRAM[i][j] * coordinates[j]
        for i in range(4)
        for j in range(4)
    )
    return (norm // 2) & 1


q_a_zeros = tuple(value for value in range(16) if q_a(value) == 0)
gate(
    "G13 lattice form: q_A=q+B(15,.) is minus type with six zeros and the same polarization B",
    q_a_zeros == (0, 7, 11, 13, 14, 15)
    and all(q_a(value) == (carry_q(value) ^ carry_b(15, value)) for value in range(16))
    and all(
        (q_a(left ^ right) ^ q_a(left) ^ q_a(right)) == carry_b(left, right)
        for left in range(16)
        for right in range(16)
    ),
)


def tau_15(value):
    return value ^ (15 if carry_b(value, 15) else 0)


tau_columns = tuple(tau_15(1 << index) for index in range(4))
q_a_pentad = q_a_zeros[1:]
gate(
    "G14 explicit bridge: tau_15 is an involutive linear isometry q_A->q and maps the two pentads",
    invertible(tau_columns)
    and compose(tau_columns, tau_columns) == F2_IDENTITY
    and all(carry_q(act(tau_columns, value)) == q_a(value) for value in range(16))
    and {act(tau_columns, value) for value in q_a_pentad} == set(PENTAD),
)
weyl_matrices = [coordinate_permutation_matrix(permutation) for permutation in permutations(range(5))]
weyl_reductions = {reduce_mod_two(matrix) for matrix in weyl_matrices}
orthogonal_a = {
    matrix
    for matrix in GL4
    if all(q_a(act(matrix, value)) == q_a(value) for value in range(16))
}
conjugated_weyl = {
    compose(tau_columns, compose(matrix, tau_columns))
    for matrix in weyl_reductions
}
gate(
    "G15 Weyl bridge: W(A4)=S5 reduces isomorphically onto O(q_A), then tau_15 conjugates it onto O(q)",
    len(weyl_matrices) == 120
    and len(weyl_reductions) == 120
    and weyl_reductions == orthogonal_a
    and conjugated_weyl == set(orthogonal_group),
)
signed_weyl = [
    matrix_scale(sign, matrix) for sign in (-1, 1) for matrix in weyl_matrices
]
signed_identity_preimages = [
    matrix for matrix in signed_weyl if reduce_mod_two(matrix) == F2_IDENTITY
]
negative_identity = matrix_scale(-1, I4)
gate(
    "G16 sign kernel: {+-1}W(A4) has 240 integral maps, 120 reductions, and kernel exactly {+-I}",
    len({tuple(tuple(row) for row in matrix) for matrix in signed_weyl}) == 240
    and len({reduce_mod_two(matrix) for matrix in signed_weyl}) == 120
    and {tuple(tuple(row) for row in matrix) for matrix in signed_identity_preimages}
    == {
        tuple(tuple(row) for row in I4),
        tuple(tuple(row) for row in negative_identity),
    },
)
ideal_generators_mod_two = (3, 5, 9, 14)
cyclotomic_powers_mod_two = {1, 2, 4, 8, 15}
pentad_images = {
    act(ideal_generators_mod_two, value) for value in q_a_pentad
}
gate(
    "G17 cyclotomic pentad: the q_A singular five map to 1,zeta,...,zeta^4 mod 2 and sum to zero",
    pentad_images == cyclotomic_powers_mod_two
    and (1 ^ 2 ^ 4 ^ 8 ^ 15) == 0,
)


# G18: the two exact ramification pins.
two_i_minus_j = matrix_sub(matrix_scale(2, I4), operators[2])
gate(
    "G18 pins: Phi5(1)=5 and det(2I-(I+C^2))=N(2-J)=5",
    sum(cyclotomic) == 5
    and determinant(matrix_sub(I4, C)) == 5
    and determinant(two_i_minus_j) == 5,
)


passed = sum(result for _, result in GATES)
for name, result in GATES:
    print(("PASS " if result else "FAIL ") + name)
if passed == len(GATES):
    print(f"RESULT {passed}/{len(GATES)} ALL PASS")
else:
    print(f"RESULT {passed}/{len(GATES)}")
raise SystemExit(0 if passed == len(GATES) else 1)
