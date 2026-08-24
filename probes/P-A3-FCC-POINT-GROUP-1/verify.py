#!/usr/bin/env python3
"""Exact verifier for P-A3-FCC-POINT-GROUP-1.

Prospective accepted verifier.  Do not execute before the public
preregistration pin required by PREREG.md.
"""

from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import gcd, isqrt
import sys


A = ((2, -1, 0), (-1, 2, -1), (0, -1, 2))
I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
F = ((1, 0, -1), (-1, 1, -1), (0, -1, 0))
P = 5

scientific_results = []
integrity_results = []
control_results = []


def fmt_bool(value):
    return "yes" if value else "no"


def fmt_hist(hist):
    return "{" + ",".join("%d:%d" % (k, hist[k]) for k in sorted(hist)) + "}"


def gate(name, ok, detail):
    scientific_results.append(bool(ok))
    print("%s %s %s" % ("PASS" if ok else "FAIL", name, detail))


def integrity(name, ok, detail):
    integrity_results.append(bool(ok))
    print("%s %s %s" % ("PASS" if ok else "FAIL", name, detail))


def control(name, fired, detail):
    control_results.append(bool(fired))
    print("%s %s %s" % ("FIRED" if fired else "NOT-FIRED", name, detail))


def transpose(matrix):
    return tuple(tuple(matrix[j][i] for j in range(len(matrix))) for i in range(len(matrix[0])))


def mat_mul(left, right, modulus=None):
    rows = len(left)
    inner = len(right)
    cols = len(right[0])
    out = tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(inner)) for j in range(cols))
        for i in range(rows)
    )
    if modulus is None:
        return out
    return tuple(tuple(value % modulus for value in row) for row in out)


def mat_vec(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix)))


def matrix_from_columns(columns):
    return tuple(tuple(columns[j][i] for j in range(len(columns))) for i in range(len(columns[0])))


def det3(matrix):
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def inverse3_fraction(matrix):
    augmented = [
        [Fraction(value) for value in matrix[i]] + [Fraction(i == j) for j in range(3)]
        for i in range(3)
    ]
    for column in range(3):
        pivot = next(row for row in range(column, 3) if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(3):
            if row == column:
                continue
            scale = augmented[row][column]
            augmented[row] = [
                augmented[row][j] - scale * augmented[column][j] for j in range(6)
            ]
    return tuple(tuple(augmented[i][j] for j in range(3, 6)) for i in range(3))


def matrix_order(matrix, bound, modulus=None):
    power = I3
    for order in range(1, bound + 1):
        power = mat_mul(power, matrix, modulus)
        if power == I3:
            return order
    return 0


def order_histogram(group, bound, modulus=None):
    return dict(Counter(matrix_order(matrix, bound, modulus) for matrix in group))


def dot_a(left, right, modulus=None):
    value = sum(left[i] * A[i][j] * right[j] for i in range(3) for j in range(3))
    return value if modulus is None else value % modulus


def basis_to_z4(coefficients):
    c1, c2, c3 = coefficients
    return (c1, -c1 + c2, -c2 + c3, -c3)


def z4_to_basis(vector):
    assert sum(vector) == 0
    return (vector[0], vector[0] + vector[1], vector[0] + vector[1] + vector[2])


def restriction_matrix(permutation, sign):
    columns = []
    for basis_vector in I3:
        source = basis_to_z4(basis_vector)
        image = [0, 0, 0, 0]
        for index in range(4):
            image[permutation[index]] = sign * source[index]
        columns.append(z4_to_basis(tuple(image)))
    return matrix_from_columns(tuple(columns))


def signed_permutation_matrices():
    matrices = set()
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = [[0, 0, 0] for _ in range(3)]
            for index in range(3):
                matrix[permutation[index]][index] = signs[index]
            matrices.add(tuple(tuple(row) for row in matrix))
    return matrices


def shell(norm):
    bound = isqrt(norm)
    return tuple(
        vector
        for vector in product(range(-bound, bound + 1), repeat=3)
        if sum(vector) % 2 == 0 and sum(value * value for value in vector) == norm
    )


def generated_group(generators, modulus=None):
    seen = {I3}
    queue = [I3]
    while queue:
        current = queue.pop(0)
        for generator in generators:
            candidate = mat_mul(current, generator, modulus)
            if candidate not in seen:
                seen.add(candidate)
                queue.append(candidate)
    return seen


def rational_rank(rows):
    work = [[Fraction(value) for value in row] for row in rows if any(row)]
    if not work:
        return 0
    row = 0
    columns = len(work[0])
    for column in range(columns):
        pivot = next((index for index in range(row, len(work)) if work[index][column]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        scale = work[row][column]
        work[row] = [value / scale for value in work[row]]
        for index in range(len(work)):
            if index == row or not work[index][column]:
                continue
            scale = work[index][column]
            work[index] = [work[index][j] - scale * work[row][j] for j in range(columns)]
        row += 1
        if row == len(work):
            break
    return row


MONOMIALS = tuple(sorted((a, b, 4 - a - b) for a in range(5) for b in range(5 - a)))
MONOMIAL_INDEX = {monomial: index for index, monomial in enumerate(MONOMIALS)}


def polynomial_action_matrix(matrix):
    inverse = transpose(matrix)
    action = [[0 for _ in MONOMIALS] for _ in MONOMIALS]
    for source_index, exponents in enumerate(MONOMIALS):
        target = [0, 0, 0]
        sign = 1
        for source_variable, exponent in enumerate(exponents):
            target_variable = next(
                index for index in range(3) if inverse[source_variable][index]
            )
            coefficient = inverse[source_variable][target_variable]
            target[target_variable] += exponent
            sign *= coefficient ** exponent
        target_index = MONOMIAL_INDEX[tuple(target)]
        action[target_index][source_index] = sign
    return tuple(tuple(row) for row in action)


def fixed_space_dimension(group):
    rows = []
    for matrix in group:
        action = polynomial_action_matrix(matrix)
        for i in range(len(MONOMIALS)):
            rows.append(tuple(action[i][j] - (i == j) for j in range(len(MONOMIALS))))
    return len(MONOMIALS) - rational_rank(rows)


def polynomial_vector(terms):
    return tuple(Fraction(terms.get(monomial, 0)) for monomial in MONOMIALS)


def apply_polynomial_action(matrix, vector):
    action = polynomial_action_matrix(matrix)
    return tuple(sum(action[i][j] * vector[j] for j in range(len(vector))) for i in range(len(vector)))


def shell_moments(points):
    m20 = tuple(sum(vector[i] ** 2 for vector in points) for i in range(3))
    m40 = tuple(sum(vector[i] ** 4 for vector in points) for i in range(3))
    m22 = tuple(
        sum(vector[i] ** 2 * vector[j] ** 2 for vector in points)
        for i in range(3)
        for j in range(i + 1, 3)
    )
    anisotropy = tuple(
        sum(vector[i] ** 4 - 3 * vector[i] ** 2 * vector[j] ** 2 for vector in points)
        for i in range(3)
        for j in range(3)
        if i != j
    )
    mixed_second = tuple(
        sum(vector[i] * vector[j] for vector in points)
        for i in range(3)
        for j in range(i + 1, 3)
    )
    odd_fourth = tuple(
        sum(vector[0] ** a * vector[1] ** b * vector[2] ** c for vector in points)
        for a, b, c in MONOMIALS
        if a % 2 or b % 2 or c % 2
    )
    return m20, m40, m22, anisotropy, mixed_second, odd_fourth


TENSOR_INDICES = tuple(product(range(3), repeat=4))


def fourth_moment_tensor(points):
    return tuple(
        sum(vector[i] * vector[j] * vector[k] * vector[l] for vector in points)
        for i, j, k, l in TENSOR_INDICES
    )


def tensor_entry(tensor, indices):
    return tensor[TENSOR_INDICES.index(indices)]


def isotropic_basis_entry(indices):
    i, j, k, l = indices
    delta = lambda left, right: int(left == right)
    return (
        delta(i, j) * delta(k, l)
        + delta(i, k) * delta(j, l)
        + delta(i, l) * delta(j, k)
    )


def b3_reduced_tensor(tensor):
    diagonal = tensor_entry(tensor, (0, 0, 0, 0))
    paired = tensor_entry(tensor, (0, 0, 1, 1))
    for position, indices in enumerate(TENSOR_INDICES):
        multiplicities = tuple(indices.count(axis) for axis in range(3))
        if 4 in multiplicities:
            expected = diagonal
        elif sorted(multiplicities) == [0, 2, 2]:
            expected = paired
        else:
            expected = 0
        if tensor[position] != expected:
            return False
    return True


def weighted_tensor(weights, tensors):
    return tuple(
        sum(Fraction(weights[shell_index]) * tensors[shell_index][position] for shell_index in range(len(weights)))
        for position in range(len(TENSOR_INDICES))
    )


def isotropic_tensor(tensor):
    scale = tensor_entry(tensor, (0, 0, 1, 1))
    return all(
        tensor[position] == scale * isotropic_basis_entry(indices)
        for position, indices in enumerate(TENSOR_INDICES)
    )


# A01: roots are constructed in the defining Z^4 carrier.
roots_z4 = tuple(
    sorted(
        vector
        for vector in product((-1, 0, 1), repeat=4)
        if sum(vector) == 0 and sum(value * value for value in vector) == 2
    )
)
expected_roots_z4 = {
    tuple((1 if coordinate == i else -1 if coordinate == j else 0) for coordinate in range(4))
    for i in range(4)
    for j in range(4)
    if i != j
}
roots = tuple(sorted(z4_to_basis(vector) for vector in roots_z4))
gram_from_basis = tuple(
    tuple(sum(basis_to_z4(I3[i])[k] * basis_to_z4(I3[j])[k] for k in range(4)) for j in range(3))
    for i in range(3)
)
leading_minors = (A[0][0], A[0][0] * A[1][1] - A[0][1] * A[1][0], det3(A))
gate("A01a BASIS-GRAM", gram_from_basis == A, "Gram=A:%s" % fmt_bool(gram_from_basis == A))
gate("A01b POSITIVE-DEFINITE", leading_minors == (2, 3, 4), "leading_minors=%s" % (leading_minors,))
gate("A01c ROOT-COUNT", len(roots) == 12, "roots=%d" % len(roots))
gate(
    "A01d ROOT-CLASSIFICATION",
    set(roots_z4) == expected_roots_z4,
    "coordinate_differences=%s" % fmt_bool(set(roots_z4) == expected_roots_z4),
)


# A02: every possible ordered image triple of the basis is filtered.
aut = set()
unimodular = True
for columns in product(roots, repeat=3):
    if all(dot_a(columns[i], columns[j]) == A[i][j] for i in range(3) for j in range(3)):
        matrix = matrix_from_columns(columns)
        unimodular = unimodular and abs(det3(matrix)) == 1
        aut.add(matrix)
aut_preserves_gram = all(mat_mul(mat_mul(transpose(matrix), A), matrix) == A for matrix in aut)
gate("A02a GRAM-TRIPLE-COUNT", len(aut) == 48, "triples=1728 accepted=%d" % len(aut))
gate("A02b UNIMODULAR", unimodular, "all_determinants_unit=%s" % fmt_bool(unimodular))
gate("A02c AUT-PREDICATE", aut_preserves_gram, "all_preserve_A=%s" % fmt_bool(aut_preserves_gram))


# A03: a separately generated marked S4 x C2 model is compared as a set.
s4_factor = {
    restriction_matrix(permutation, 1) for permutation in permutations(range(4))
}
w_model = {
    restriction_matrix(permutation, sign)
    for permutation in permutations(range(4))
    for sign in (-1, 1)
}
minus_identity = tuple(tuple(-I3[i][j] for j in range(3)) for i in range(3))
central_minus = all(mat_mul(minus_identity, matrix) == mat_mul(matrix, minus_identity) for matrix in aut)
gate("A03a S4-FAITHFUL", len(s4_factor) == 24, "S4_restrictions=%d" % len(s4_factor))
gate("A03b SIGNED-S4-SIZE", len(w_model) == 48, "signed_model=%d" % len(w_model))
gate("A03c AUT-EQUALS-SIGNED-S4", aut == w_model, "set_equal=%s" % fmt_bool(aut == w_model))
gate("A03d MINUS-I-OUTSIDE-S4", minus_identity not in s4_factor, "outside=%s" % fmt_bool(minus_identity not in s4_factor))
gate("A03e MINUS-I-CENTRAL", central_minus, "central=%s" % fmt_bool(central_minus))
direct_product_identification = aut == w_model and minus_identity not in s4_factor and central_minus
gate("A03f AUT-DIRECT-PRODUCT", direct_product_identification, "S4xC2=%s" % fmt_bool(direct_product_identification))


# A04: exact order census.
expected_aut_hist = {1: 1, 2: 19, 3: 8, 4: 12, 6: 8}
aut_hist = order_histogram(aut, 48)
gate("A04a AUT-ORDER-HISTOGRAM", aut_hist == expected_aut_hist, "hist=%s" % fmt_hist(aut_hist))
gate("A04b AUT-NO-ORDER-FIVE", 5 not in aut_hist, "order5=%d" % aut_hist.get(5, 0))
integrity("I01 AUT-ORDERS-RESOLVED", 0 not in aut_hist, "unresolved=%d" % aut_hist.get(0, 0))


# D01-D04: exact A3-to-D3 transport and the axes-forced ceiling.
f_inverse = inverse3_fraction(F)
expected_f_inverse = (
    (Fraction(1, 2), Fraction(-1, 2), Fraction(-1, 2)),
    (Fraction(0), Fraction(0), Fraction(-1)),
    (Fraction(-1, 2), Fraction(-1, 2), Fraction(-1, 2)),
)
columns_f = transpose(F)
f_isometry = mat_mul(transpose(F), F) == A
f_index_two = det3(F) == -2
f_image_in_d3 = all(sum(column) % 2 == 0 for column in columns_f)
d3_generators = ((1, 1, 0), (1, 0, 1), (0, 1, 1))
d3_generator_preimages = tuple(mat_vec(f_inverse, generator) for generator in d3_generators)
d3_in_image = all(
    all(value.denominator == 1 for value in preimage)
    and mat_vec(F, preimage) == generator
    for generator, preimage in zip(d3_generators, d3_generator_preimages)
)
gate("D01a TRANSPORT-ISOMETRY", f_isometry, "FtF=A:%s" % fmt_bool(f_isometry))
gate("D01b TRANSPORT-INDEX", f_index_two, "detF=%d" % det3(F))
gate("D01c IMAGE-IN-D3", f_image_in_d3, "basis_parity=%s" % fmt_bool(f_image_in_d3))
gate("D01d INVERSE-FORMULA", f_inverse == expected_f_inverse, "exact=%s" % fmt_bool(f_inverse == expected_f_inverse))
gate("D01e D3-IN-IMAGE", d3_in_image, "generator_preimages_integral=%s" % fmt_bool(d3_in_image))

shell2 = shell(2)
transported_roots = {mat_vec(F, root) for root in roots}
gate("D02a MINIMAL-SHELL-SIZE", len(shell2) == 12, "shell2=%d" % len(shell2))
gate("D02b ROOT-TRANSPORT", transported_roots == set(shell2), "equal=%s" % fmt_bool(transported_roots == set(shell2)))

transported_group = set()
transport_integral = True
for matrix in aut:
    conjugate = mat_mul(mat_mul(F, matrix), f_inverse)
    transport_integral = transport_integral and all(value.denominator == 1 for row in conjugate for value in row)
    transported_group.add(tuple(tuple(int(value) for value in row) for row in conjugate))
signed_group = signed_permutation_matrices()
gate("D03a CONJUGATES-INTEGRAL", transport_integral, "integral=%s" % fmt_bool(transport_integral))
gate("D03b SIGNED-GROUP-SIZE", len(signed_group) == 48, "signed=%d" % len(signed_group))
gate("D03c TRANSPORTED-GROUP", transported_group == signed_group, "equal=%s" % fmt_bool(transported_group == signed_group))

shell4 = shell(4)
axes = {
    tuple(2 * sign if coordinate == axis else 0 for coordinate in range(3))
    for axis in range(3)
    for sign in (-1, 1)
}
signed_preserve_d3 = all(
    all(sum(mat_vec(matrix, vector)) % 2 == 0 for vector in d3_generators)
    for matrix in signed_group
)
axes_rank = rational_rank(axes)
gate("D04a SHELL4-AXES", set(shell4) == axes, "shell4=%d equal_axes=%s" % (len(shell4), fmt_bool(set(shell4) == axes)))
gate("D04b AXES-SPAN", axes_rank == 3, "rank=%d" % axes_rank)
gate("D04c SIGNED-PRESERVE-D3", signed_preserve_d3, "preserve=%s" % fmt_bool(signed_preserve_d3))
full_point_group_ceiling = set(shell4) == axes and axes_rank == 3 and signed_preserve_d3
gate("D04d FULL-POINT-GROUP", full_point_group_ceiling, "axes_ceiling_and_converse=%s" % fmt_bool(full_point_group_ceiling))


# F01: exhaustive finite orthogonal group, pruned only by its Gram equations.
vectors5 = tuple(tuple(vector) for vector in product(range(P), repeat=3))
first_columns = tuple(vector for vector in vectors5 if dot_a(vector, vector, P) == A[0][0] % P)
o5 = set()
for first in first_columns:
    second_columns = tuple(
        vector
        for vector in vectors5
        if dot_a(vector, vector, P) == A[1][1] % P
        and dot_a(first, vector, P) == A[0][1] % P
    )
    for second in second_columns:
        for third in vectors5:
            if (
                dot_a(third, third, P) == A[2][2] % P
                and dot_a(first, third, P) == A[0][2] % P
                and dot_a(second, third, P) == A[1][2] % P
            ):
                o5.add(
                    tuple(
                        tuple(value % P for value in row)
                        for row in matrix_from_columns((first, second, third))
                    )
                )
expected_o5_hist = {1: 1, 2: 51, 3: 20, 4: 60, 5: 24, 6: 60, 10: 24}
o5_hist = order_histogram(o5, 240, P)
gate("F01a FINITE-FORM-NONDEGENERATE", det3(A) % P != 0, "detAmod5=%d" % (det3(A) % P))
gate("F01b FINITE-ORTHOGONAL-SIZE", len(o5) == 240, "size=%d" % len(o5))
gate("F01c FINITE-ORDER-HISTOGRAM", o5_hist == expected_o5_hist, "hist=%s" % fmt_hist(o5_hist))
integrity("I02 FINITE-ORDERS-RESOLVED", 0 not in o5_hist, "unresolved=%d" % o5_hist.get(0, 0))


# F02: reduction image and homomorphism.
def reduce5(matrix):
    return tuple(tuple(value % P for value in row) for row in matrix)


red_image = {reduce5(matrix) for matrix in aut}
red_homomorphism = all(
    reduce5(mat_mul(left, right)) == mat_mul(reduce5(left), reduce5(right), P)
    for left in aut
    for right in aut
)
red_kernel = {matrix for matrix in aut if reduce5(matrix) == I3}
red_hist = order_histogram(red_image, 240, P)
gate("F02a REDUCTION-HOMOMORPHISM", red_homomorphism, "hom=%s" % fmt_bool(red_homomorphism))
gate("F02b REDUCTION-ORTHOGONAL", red_image <= o5, "contained=%s" % fmt_bool(red_image <= o5))
gate("F02c REDUCTION-INJECTIVE", red_kernel == {I3}, "kernel=%d" % len(red_kernel))
gate("F02d REDUCTION-IMAGE-SIZE", len(red_image) == 48, "image=%d" % len(red_image))
exact_index_five = len(red_image) > 0 and len(o5) == 5 * len(red_image)
gate("F02e REDUCTION-INDEX-FIVE", exact_index_five, "O5=%d five_times_image=%d" % (len(o5), 5 * len(red_image)))
gate("F02f REDUCTION-HISTOGRAM", red_hist == expected_aut_hist, "hist=%s" % fmt_hist(red_hist))
gate("F02g REDUCTION-NO-ORDER-FIVE", 5 not in red_hist, "order5=%d" % red_hist.get(5, 0))


# F03: typed no-section proof, without adding an unfrozen subgroup-existence claim.
order_a5 = 60
order_a5c2 = 120
a5_cauchy_order_five = order_a5 % P == 0
a5c2_cauchy_order_five = order_a5c2 % P == 0
typed_obstruction = 5 not in aut_hist and 5 not in red_hist
gate("F03a A5-ORDER-DIVISIBLE-BY-FIVE", a5_cauchy_order_five, "order=%d" % order_a5)
gate("F03b A5XC2-ORDER-DIVISIBLE-BY-FIVE", a5c2_cauchy_order_five, "order=%d" % order_a5c2)
gate("F03c A5-NO-LIFT", typed_obstruction, "Aut_order5=%d image_order5=%d" % (aut_hist.get(5, 0), red_hist.get(5, 0)))
gate("F03d A5XC2-NO-LIFT", typed_obstruction, "Aut_order5=%d image_order5=%d" % (aut_hist.get(5, 0), red_hist.get(5, 0)))


# Q01-Q02: exact homogeneous degree-four representation.
quartic_dimension = len(MONOMIALS)
fixed_dimension = fixed_space_dimension(signed_group)
r4 = polynomial_vector(
    {
        (4, 0, 0): 1,
        (0, 4, 0): 1,
        (0, 0, 4): 1,
        (2, 2, 0): 2,
        (2, 0, 2): 2,
        (0, 2, 2): 2,
    }
)
m4 = polynomial_vector({(4, 0, 0): 1, (0, 4, 0): 1, (0, 0, 4): 1})
r4_invariant = all(apply_polynomial_action(matrix, r4) == r4 for matrix in signed_group)
m4_invariant = all(apply_polynomial_action(matrix, m4) == m4 for matrix in signed_group)
basis_rank = rational_rank((r4, m4))
gate("Q01a EXACT-DEGREE-FOUR-DIMENSION", quartic_dimension == 15, "V4=%d" % quartic_dimension)
gate("Q01b FIXED-SPACE-DIMENSION", fixed_dimension == 2, "fixed=%d" % fixed_dimension)
gate("Q01c RADIAL-QUARTIC-INVARIANT", r4_invariant, "R4=%s" % fmt_bool(r4_invariant))
gate("Q01d CUBIC-QUARTIC-INVARIANT", m4_invariant, "M4=%s" % fmt_bool(m4_invariant))
gate("Q01e INVARIANT-BASIS-RANK", basis_rank == 2, "basis_rank=%d" % basis_rank)
invariant_basis_spans = fixed_dimension == basis_rank == 2 and r4_invariant and m4_invariant
gate("Q01f INVARIANT-BASIS-SPANS", invariant_basis_spans, "spans=%s" % fmt_bool(invariant_basis_spans))

quarter_turn = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
quarter_group = generated_group((quarter_turn,))
quarter_fixed_dimension = fixed_space_dimension(quarter_group)
m4_not_radial = rational_rank((r4, m4)) == 2
gate("Q02a QUOTIENT-DIMENSION", fixed_dimension - 1 == 1, "quotient_dim=%d" % (fixed_dimension - 1))
gate("Q02b M4-CLASS-NONZERO", m4_not_radial, "M4_nonradial=%s" % fmt_bool(m4_not_radial))
gate("Q02c QUARTER-TURN-GROUP-SIZE", len(quarter_group) == 4, "C4=%d" % len(quarter_group))
gate("Q02d QUARTER-TURN-FIXED-DIMENSION", quarter_fixed_dimension == 5, "C4_fixed=%d" % quarter_fixed_dimension)


# S01: complete low-shell moment table.
norms = (2, 4, 6, 8)
shells = {norm: shell(norm) for norm in norms}
expected_sizes = (12, 6, 24, 12)
expected_anisotropies = (-4, 32, -72, -64)
observed_sizes = tuple(len(shells[norm]) for norm in norms)
observed_anisotropies = []
second_diagonal_symmetry = True
fourth_diagonal_symmetry = True
paired_fourth_symmetry = True
ordered_anisotropy_symmetry = True
mixed_second_zero = True
odd_fourth_zero = True
moment_identities = True
for norm in norms:
    points = shells[norm]
    m20, m40, m22, anisotropy, mixed_second, odd_fourth = shell_moments(points)
    second_diagonal_symmetry = second_diagonal_symmetry and len(set(m20)) == 1
    fourth_diagonal_symmetry = fourth_diagonal_symmetry and len(set(m40)) == 1
    paired_fourth_symmetry = paired_fourth_symmetry and len(set(m22)) == 1
    ordered_anisotropy_symmetry = ordered_anisotropy_symmetry and len(set(anisotropy)) == 1
    mixed_second_zero = mixed_second_zero and all(value == 0 for value in mixed_second)
    odd_fourth_zero = odd_fourth_zero and all(value == 0 for value in odd_fourth)
    moment_identities = moment_identities and 3 * m40[0] + 6 * m22[0] == len(points) * norm * norm
    observed_anisotropies.append(anisotropy[0])
gate("S01a SHELL-SIZES", observed_sizes == expected_sizes, "sizes=%s" % (observed_sizes,))
gate("S01b SHELL-ANISOTROPIES", tuple(observed_anisotropies) == expected_anisotropies, "anis=%s" % (tuple(observed_anisotropies),))
gate("S01c SECOND-DIAGONAL-SYMMETRY", second_diagonal_symmetry, "equal=%s" % fmt_bool(second_diagonal_symmetry))
gate("S01d FOURTH-DIAGONAL-SYMMETRY", fourth_diagonal_symmetry, "equal=%s" % fmt_bool(fourth_diagonal_symmetry))
gate("S01e PAIRED-FOURTH-SYMMETRY", paired_fourth_symmetry, "equal=%s" % fmt_bool(paired_fourth_symmetry))
gate("S01f ORDERED-ANISOTROPY-SYMMETRY", ordered_anisotropy_symmetry, "equal=%s" % fmt_bool(ordered_anisotropy_symmetry))
gate("S01g MIXED-SECOND-ZERO", mixed_second_zero, "zero=%s" % fmt_bool(mixed_second_zero))
gate("S01h ODD-FOURTH-ZERO", odd_fourth_zero, "zero=%s" % fmt_bool(odd_fourth_zero))
gate("S01i RADIAL-MOMENT-IDENTITY", moment_identities, "holds=%s" % fmt_bool(moment_identities))
shell_nonisotropy = all(value != 0 for value in observed_anisotropies)
gate("S01j SHELL-NONISOTROPY", shell_nonisotropy, "all_nonzero=%s" % fmt_bool(shell_nonisotropy))


# C01-C04: symbolic cone and weight-type firewall.
shell_tensors = tuple(fourth_moment_tensor(shells[norm]) for norm in norms)
tensor_b3_reduction = all(b3_reduced_tensor(tensor) for tensor in shell_tensors)
per_vector_coefficients = tuple(observed_anisotropies[:3])
reduced_scaled = tuple(Fraction(value, 4) for value in per_vector_coefficients)
reduced_coefficients_integral = all(value.denominator == 1 for value in reduced_scaled)
reduced_coefficients = tuple(value.numerator for value in reduced_scaled)
ray_one = (8, 1, 0)
ray_two = (0, 9, 4)
interior = (6, 3, 1)

tensor_residual_rows = tuple(
    tuple(
        shell_tensors[shell_index][position]
        - isotropic_basis_entry(indices)
        * tensor_entry(shell_tensors[shell_index], (0, 0, 1, 1))
        for shell_index in range(3)
    )
    for position, indices in enumerate(TENSOR_INDICES)
)
zero_coefficient_row = (0, 0, 0)
tensor_anchor_coefficients = tuple(
    tensor_entry(shell_tensors[shell_index], (0, 0, 1, 1)) for shell_index in range(3)
)
tensor_residual_census = Counter(tensor_residual_rows)
expected_tensor_residual_census = Counter(
    {zero_coefficient_row: 78, per_vector_coefficients: 3}
)
tensor_isotropy_reduction = (
    set(tensor_residual_rows) - {zero_coefficient_row} == {per_vector_coefficients}
)


def cone_residual(vector, coefficients=per_vector_coefficients):
    return sum(coefficients[i] * vector[i] for i in range(3))


gate("T01 FOURTH-TENSOR-INDEX-CARDINALITY", len(TENSOR_INDICES) == len(set(TENSOR_INDICES)) == 81, "indices=%d" % len(TENSOR_INDICES))
gate("T02 B3-TENSOR-REDUCTION", tensor_b3_reduction, "all_four_shells=%s" % fmt_bool(tensor_b3_reduction))
gate("T03 ISOTROPY-ANCHOR-COEFFICIENTS", tensor_anchor_coefficients == (4, 0, 72), "anchors=%s" % (tensor_anchor_coefficients,))
gate("T04 TENSOR-RESIDUAL-CENSUS", tensor_residual_census == expected_tensor_residual_census, "zero_rows=%d anisotropy_rows=%d" % (tensor_residual_census[zero_coefficient_row], tensor_residual_census[per_vector_coefficients]))
gate("T05 FULL-TENSOR-ISOTROPY-IFF", tensor_isotropy_reduction, "nonzero_row_types=%d" % len(set(tensor_residual_rows) - {zero_coefficient_row}))
gate("C01a PER-VECTOR-COEFFICIENTS", per_vector_coefficients == (-4, 32, -72), "coeff=%s" % (per_vector_coefficients,))
gate("C01b COEFFICIENTS-DIVISIBLE-BY-FOUR", reduced_coefficients_integral, "integral=%s" % fmt_bool(reduced_coefficients_integral))
gate("C01c REDUCED-CONE-EQUATION", reduced_coefficients == (-1, 8, -18), "reduced=%s equation=w1=8w2-18w3" % (reduced_coefficients,))

ray_one_primitive = gcd(gcd(*ray_one[:2]), ray_one[2]) == 1
ray_two_primitive = gcd(gcd(*ray_two[:2]), ray_two[2]) == 1
symbolic_left = (
    (Fraction(1), Fraction(0)),
    (Fraction(1, 8), Fraction(18, 8)),
    (Fraction(0), Fraction(1)),
)
symbolic_right = (
    (Fraction(ray_one[0], 8), Fraction(ray_two[0], 4)),
    (Fraction(ray_one[1], 8), Fraction(ray_two[1], 4)),
    (Fraction(ray_one[2], 8), Fraction(ray_two[2], 4)),
)
decomposition_coefficient_map = (
    (Fraction(1, 8), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1, 4)),
)
gate("C02a FIRST-RAY-ON-CONE", cone_residual(ray_one) == 0, "ray=%s residual=%d" % (ray_one, cone_residual(ray_one)))
gate("C02b SECOND-RAY-ON-CONE", cone_residual(ray_two) == 0, "ray=%s residual=%d" % (ray_two, cone_residual(ray_two)))
rays_nonnegative = all(value >= 0 for value in ray_one + ray_two)
gate("C02c RAYS-NONNEGATIVE", rays_nonnegative, "nonnegative=%s" % fmt_bool(rays_nonnegative))
gate("C02d FIRST-RAY-PRIMITIVE", ray_one_primitive, "primitive=%s" % fmt_bool(ray_one_primitive))
gate("C02e SECOND-RAY-PRIMITIVE", ray_two_primitive, "primitive=%s" % fmt_bool(ray_two_primitive))
gate("C02f SYMBOLIC-DECOMPOSITION", symbolic_left == symbolic_right, "identity=%s" % fmt_bool(symbolic_left == symbolic_right))
ray_rank = rational_rank((ray_one, ray_two))
gate("C02g DECOMPOSITION-UNIQUE", ray_rank == 2, "ray_rank=%d" % ray_rank)
decomposition_coefficients_nonnegative = all(
    value >= 0 for row in decomposition_coefficient_map for value in row
)
gate("C02h DECOMPOSITION-COEFFICIENT-SIGNS", decomposition_coefficients_nonnegative, "nonnegative=%s" % fmt_bool(decomposition_coefficients_nonnegative))
cone_complete = (
    cone_residual(ray_one) == 0
    and cone_residual(ray_two) == 0
    and rays_nonnegative
    and symbolic_left == symbolic_right
    and ray_rank == 2
    and decomposition_coefficients_nonnegative
)
gate("C02i CONE-COMPLETE", cone_complete, "symbolic_bidirectional=%s" % fmt_bool(cone_complete))
isotropic_witnesses = all(
    isotropic_tensor(weighted_tensor(weights, shell_tensors[:3]))
    for weights in (ray_one, ray_two, interior)
)
gate("C02j TENSOR-WITNESSES", isotropic_witnesses, "three_isotropic=%s" % fmt_bool(isotropic_witnesses))

ray_one_boundary_typing = sum(value > 0 for value in ray_one) == 2
ray_two_boundary_typing = sum(value > 0 for value in ray_two) == 2
strict_interior = all(value > 0 for value in interior)
interior_on_cone = cone_residual(interior) == 0
face_w2_zero_only_origin = reduced_coefficients[0] < 0 and reduced_coefficients[2] < 0
gate("C03a FIRST-RAY-BOUNDARY", ray_one_boundary_typing, "positive_coordinates=%d" % sum(value > 0 for value in ray_one))
gate("C03b SECOND-RAY-BOUNDARY", ray_two_boundary_typing, "positive_coordinates=%d" % sum(value > 0 for value in ray_two))
gate("C03c INTERIOR-POSITIVE", strict_interior, "interior=%s" % (interior,))
gate("C03d INTERIOR-ON-CONE", interior_on_cone, "residual=%d" % cone_residual(interior))
gate("C03e FACE-W2-ZERO", face_w2_zero_only_origin, "only_origin=%s" % fmt_bool(face_w2_zero_only_origin))

total_mass_scaled = tuple(
    3 * Fraction(per_vector_coefficients[i], observed_sizes[i]) for i in range(3)
)
total_mass_integral = all(value.denominator == 1 for value in total_mass_scaled)
total_mass_coefficients = tuple(value.numerator for value in total_mass_scaled)
gate("C04a TOTAL-MASS-INTEGRAL-SCALING", total_mass_integral, "integral=%s" % fmt_bool(total_mass_integral))
gate("C04b TOTAL-MASS-EQUATION", total_mass_coefficients == (-1, 16, -9), "coeff=%s" % (total_mass_coefficients,))
gate("C04c WEIGHT-TYPES-DISTINCT", total_mass_coefficients != per_vector_coefficients, "distinct=%s" % fmt_bool(total_mass_coefficients != per_vector_coefficients))


print("-- type-correct mutation controls --")

# K01-K03: genuine root inputs and a genuine integral subgroup.
b1 = (1, 0, 0)
b2 = (0, 1, 0)
b1_plus_b2 = (1, 1, 0)
bad_root_triple = (b1, b2, b1_plus_b2)
bad_root_triple_rejected = all(root in roots for root in bad_root_triple) and not all(
    dot_a(bad_root_triple[i], bad_root_triple[j]) == A[i][j]
    for i in range(3)
    for j in range(3)
)
control("K01 WRONG-GRAM-ROOT-TRIPLE", bad_root_triple_rejected, "typed_roots=yes Cartan_Gram=no")

aut_plus = {matrix for matrix in aut if det3(matrix) == 1}
control("K02 PROPER-INTEGRAL-SUBGROUP", len(aut_plus) == 24 and aut_plus != aut, "det_plus_size=%d full_size=%d" % (len(aut_plus), len(aut)))

aut_plus_hist = order_histogram(aut_plus, 48)
control(
    "K03 SUBGROUP-HISTOGRAM",
    aut_plus_hist == {1: 1, 2: 9, 3: 8, 4: 6} and aut_plus_hist != expected_aut_hist,
    "subgroup_hist=%s differs_full=%s" % (fmt_hist(aut_plus_hist), fmt_bool(aut_plus_hist != expected_aut_hist)),
)

# K04-K06: same transport and lattice types.
f_bad = matrix_from_columns((tuple(-value for value in columns_f[0]), columns_f[1], columns_f[2]))
control("K04 BAD-ISOMETRY-TRANSPORT", mat_mul(transpose(f_bad), f_bad) != A, "Fbad_t_Fbad_not_A=yes")

control("K05 WRONG-SHELL-AXES", set(shell2) != axes, "shell2=%d axes=%d" % (len(shell2), len(axes)))

signed_plus = {matrix for matrix in signed_group if det3(matrix) == 1}
control("K06 PROPER-POINT-SUBGROUP", len(signed_plus) == 24 and signed_plus != signed_group, "signed_det_plus=%d full=%d" % (len(signed_plus), len(signed_group)))

# K07-K09: genuine finite and reduction subgroups, including a positive lift control.
so5 = {matrix for matrix in o5 if det3(matrix) % P == 1}
so5_hist = order_histogram(so5, 240, P)
control("K07 SPECIAL-ORTHOGONAL-SUBGROUP", len(so5) == 120 and so5 != o5, "SO5=%d O5=%d hist=%s" % (len(so5), len(o5), fmt_hist(so5_hist)))

red_plus = {reduce5(matrix) for matrix in aut_plus}
control("K08 PROPER-REDUCTION-IMAGE", len(red_plus) == 24 and red_plus != red_image, "red_det_plus=%d full_image=%d" % (len(red_plus), len(red_image)))

red_plus_lift = {reduce5(matrix): matrix for matrix in aut_plus}
section_table_bijective = len(red_plus_lift) == len(red_plus) == len(aut_plus) and set(red_plus_lift) == red_plus
section_right_inverse = section_table_bijective and all(
    reduce5(red_plus_lift[matrix]) == matrix for matrix in red_plus
)
section_homomorphic = section_table_bijective and all(
        mat_mul(red_plus_lift[left], red_plus_lift[right])
        == red_plus_lift[mat_mul(left, right, P)]
        for left in red_plus
        for right in red_plus
)
control("K09a SECTION-RIGHT-INVERSE", section_right_inverse, "right_inverse=%s" % fmt_bool(section_right_inverse))
control("K09b SECTION-HOMOMORPHISM", section_homomorphic, "homomorphism=%s" % fmt_bool(section_homomorphic))

# K10-K12: homogeneous subgroup and in-type moment mutations.
control("K10 QUARTER-TURN-INVARIANTS", quarter_fixed_dimension == 5 and quarter_fixed_dimension != fixed_dimension, "C4_fixed=%d full_fixed=%d" % (quarter_fixed_dimension, fixed_dimension))

wrong_size_table = (12, 8, 24, 12)
control("K11a WRONG-SHELL-SIZE-TABLE", wrong_size_table != observed_sizes, "wrong=%s observed=%s" % (wrong_size_table, observed_sizes))

wrong_anisotropy_table = (0, 32, -72, -64)
control("K11b WRONG-SHELL-ANISOTROPY-TABLE", wrong_anisotropy_table != tuple(observed_anisotropies), "wrong=%s observed=%s" % (wrong_anisotropy_table, tuple(observed_anisotropies)))

asymmetric_subset = ((1, 1, 0), (-1, -1, 0))
subset_anisotropy = shell_moments(asymmetric_subset)[3]
subset_tensor = fourth_moment_tensor(asymmetric_subset)
control(
    "K12 ASYMMETRIC-D3-SUBSET",
    len(set(subset_anisotropy)) > 1 and not b3_reduced_tensor(subset_tensor),
    "ordered_pair_values=%s B3_reduced=%s" % (subset_anisotropy, fmt_bool(b3_reduced_tensor(subset_tensor))),
)

# K13-K16: same-domain weights and explicit normalization alias detection.
off_cone_weight = (1, 1, 1)
off_cone_tensor = weighted_tensor(off_cone_weight, shell_tensors[:3])
control(
    "K13 OFF-CONE-WEIGHT",
    cone_residual(off_cone_weight) == -44 and not isotropic_tensor(off_cone_tensor),
    "weight=%s residual=%d tensor_isotropic=%s"
    % (off_cone_weight, cone_residual(off_cone_weight), fmt_bool(isotropic_tensor(off_cone_tensor))),
)

control("K14a FIRST-BOUNDARY-NOT-STRICT", not all(value > 0 for value in ray_one), "first_ray_has_zero=yes")
control("K14b SECOND-BOUNDARY-NOT-STRICT", not all(value > 0 for value in ray_two), "second_ray_has_zero=yes")

control("K15 NONZERO-OTHER-FACE", ray_one[2] == 0 and any(ray_one) and cone_residual(ray_one) == 0, "w3_zero_ray=%s" % (ray_one,))

total_residual_ray_one = sum(total_mass_coefficients[i] * ray_one[i] for i in range(3))
control(
    "K16a PER-VECTOR-RAY-ACCEPTED",
    cone_residual(ray_one) == 0,
    "per_vector_residual=%d" % cone_residual(ray_one),
)
control(
    "K16b TOTAL-MASS-ALIAS-REJECTED",
    total_residual_ray_one != 0,
    "total_mass_residual=%d" % total_residual_ray_one,
)

# K17-K22: explicit guards requested by the atomic contract.
monomials_degree_at_most_four = tuple(
    (a, b, c)
    for a in range(5)
    for b in range(5)
    for c in range(5)
    if a + b + c <= 4
)
control(
    "K17 DEGREE-AT-MOST-FOUR-ALIAS",
    len(monomials_degree_at_most_four) == 35 and len(monomials_degree_at_most_four) != quartic_dimension,
    "degree_leq4=%d exact_degree4=%d" % (len(monomials_degree_at_most_four), quartic_dimension),
)

def collapsed_reduction(_matrix):
    return I3


collapsed_kernel = {matrix for matrix in aut if collapsed_reduction(matrix) == I3}
control(
    "K18 NONINJECTIVE-REDUCTION-MUTATION",
    len(collapsed_kernel) == len(aut) and collapsed_kernel != {I3},
    "constant_identity_kernel=%d" % len(collapsed_kernel),
)

control(
    "K19 ORDER-FIVE-FINITE-SUPERGROUP",
    o5_hist.get(5, 0) == 24 and 5 not in red_hist,
    "O5_order5=%d image_order5=%d" % (o5_hist.get(5, 0), red_hist.get(5, 0)),
)

radial_class_rank = rational_rank((r4, r4))
control(
    "K20 RADIAL-QUOTIENT-ZERO",
    radial_class_rank == 1 and m4_not_radial,
    "radial_pair_rank=%d M4_nonradial=%s" % (radial_class_rank, fmt_bool(m4_not_radial)),
)

first_shell_moments = shell_moments(shells[2])
wrong_radial_rhs = len(shells[2]) * 2 * 2 + 1
control(
    "K21 WRONG-RADIAL-MOMENT-RHS",
    3 * first_shell_moments[1][0] + 6 * first_shell_moments[2][0] != wrong_radial_rhs,
    "wrong_rhs=%d" % wrong_radial_rhs,
)

negative_cone_line = tuple(-value for value in ray_one)
control(
    "K22 EQUATION-WITHOUT-NONNEGATIVITY",
    cone_residual(negative_cone_line) == 0 and not all(value >= 0 for value in negative_cone_line),
    "signed_ray=%s residual=%d" % (negative_cone_line, cone_residual(negative_cone_line)),
)


passed = sum(scientific_results)
integrity_passed = sum(integrity_results)
controls_fired = sum(control_results)
if integrity_passed != len(integrity_results) or controls_fired != len(control_results):
    print(
        "RESULT STOP gates=%d/%d integrity=%d/%d controls=%d/%d"
        % (
            passed,
            len(scientific_results),
            integrity_passed,
            len(integrity_results),
            controls_fired,
            len(control_results),
        )
    )
    sys.exit(1)
if passed == len(scientific_results):
    print(
        "RESULT PROBE-PASS gates=%d/%d integrity=%d/%d controls=%d/%d"
        % (passed, len(scientific_results), integrity_passed, len(integrity_results), controls_fired, len(control_results))
    )
    sys.exit(0)
else:
    print(
        "RESULT NEGATIVE gates=%d/%d integrity=%d/%d controls=%d/%d"
        % (passed, len(scientific_results), integrity_passed, len(integrity_results), controls_fired, len(control_results))
    )
    sys.exit(0)
