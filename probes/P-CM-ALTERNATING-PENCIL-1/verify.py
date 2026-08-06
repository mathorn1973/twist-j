#!/usr/bin/env python3
"""Exact verifier for P-CM-ALTERNATING-PENCIL-1.

The program uses the power basis 1, j, j^2, j^3 for the fifth cyclotomic
integer ring.  It audits the alternating trace-form pencil and the declared
unit actions with integer and Fraction arithmetic only.
"""

from fractions import Fraction
from itertools import permutations, product
import sys


CHECKS = []


def check(label, condition):
    CHECKS.append((label, bool(condition)))


# Ring arithmetic in the power basis 1, j, j^2, j^3.
def ring_add(left, right):
    return tuple(
        left[index] + right[index]
        for index in range(4)
    )


def ring_neg(value):
    return tuple(-coefficient for coefficient in value)


def ring_sub(left, right):
    return ring_add(left, ring_neg(right))


def ring_scale(scalar, value):
    return tuple(scalar * coefficient for coefficient in value)


def ring_mul(left, right):
    coefficients = [Fraction(0) for _ in range(5)]
    for left_degree in range(4):
        for right_degree in range(4):
            degree = (left_degree + right_degree) % 5
            coefficients[degree] += (
                left[left_degree] * right[right_degree]
            )
    top = coefficients[4]
    return tuple(
        coefficients[index] - top
        for index in range(4)
    )


def ring_pow(value, exponent):
    result = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
    factor = value
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = ring_mul(result, factor)
        factor = ring_mul(factor, factor)
        remaining >>= 1
    return result


def ring_sum(values):
    total = (Fraction(0), Fraction(0), Fraction(0), Fraction(0))
    for value in values:
        total = ring_add(total, value)
    return total


def conjugate(value):
    constant, first, second, third = value
    return (
        constant - first,
        -first,
        third - first,
        second - first,
    )


def galois(value, exponent):
    coefficients = [Fraction(0) for _ in range(5)]
    for degree in range(4):
        coefficients[(degree * exponent) % 5] += value[degree]
    top = coefficients[4]
    return tuple(
        coefficients[index] - top
        for index in range(4)
    )


def ring_trace(value):
    return 4 * value[0] - value[1] - value[2] - value[3]


def integral_element(value):
    return all(
        Fraction(coefficient).denominator == 1
        for coefficient in value
    )


ZERO = (Fraction(0), Fraction(0), Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
MINUS_ONE = ring_neg(ONE)
ROOT = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
ROOT_INVERSE = ring_pow(ROOT, 4)
PHI = (Fraction(0), Fraction(0), Fraction(-1), Fraction(-1))
PHI_INVERSE = ring_sub(PHI, ONE)
AXIOM = ring_add(ONE, ring_pow(ROOT, 2))
AXIOM_INVERSE = ring_mul(PHI, ROOT_INVERSE)
LAMBDA_ONE = (Fraction(1), Fraction(2), Fraction(1), Fraction(1))
LAMBDA_TWO = (Fraction(0), Fraction(0), Fraction(1), Fraction(-1))

BASIS = tuple(
    tuple(Fraction(int(row == column)) for row in range(4))
    for column in range(4)
)


def absolute_norm_element(value):
    return ring_mul(
        ring_mul(galois(value, 1), galois(value, 2)),
        ring_mul(galois(value, 3), galois(value, 4)),
    )


# Rational matrix arithmetic.
def matrix_transpose(matrix):
    return tuple(
        tuple(matrix[row][column] for row in range(len(matrix)))
        for column in range(len(matrix[0]))
    )


def matrix_mul(left, right):
    return tuple(
        tuple(
            sum(
                left[row][inner] * right[inner][column]
                for inner in range(len(right))
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def matrix_add(left, right):
    return tuple(
        tuple(
            left[row][column] + right[row][column]
            for column in range(len(left[0]))
        )
        for row in range(len(left))
    )


def matrix_scale(scalar, matrix):
    return tuple(
        tuple(scalar * entry for entry in row)
        for row in matrix
    )


def identity_matrix(size):
    return tuple(
        tuple(Fraction(int(row == column)) for column in range(size))
        for row in range(size)
    )


def permutation_sign(permutation):
    inversions = sum(
        int(permutation[left] > permutation[right])
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return -1 if inversions & 1 else 1


def determinant(matrix):
    size = len(matrix)
    total = Fraction(0)
    for permutation in permutations(range(size)):
        term = Fraction(permutation_sign(permutation))
        for row in range(size):
            term *= matrix[row][permutation[row]]
        total += term
    return total


def multiplication_matrix(value):
    columns = tuple(ring_mul(value, basis_value) for basis_value in BASIS)
    return tuple(
        tuple(columns[column][row] for column in range(4))
        for row in range(4)
    )


def conjugation_matrix():
    columns = tuple(conjugate(basis_value) for basis_value in BASIS)
    return tuple(
        tuple(columns[column][row] for column in range(4))
        for row in range(4)
    )


def integral_matrix(matrix):
    return all(
        Fraction(entry).denominator == 1
        for row in matrix
        for entry in row
    )


def pullback(form, linear_map):
    return matrix_mul(
        matrix_mul(matrix_transpose(linear_map), form),
        linear_map,
    )


def pfaffian(form):
    return (
        form[0][1] * form[2][3]
        - form[0][2] * form[1][3]
        + form[0][3] * form[1][2]
    )


def scalar_multiplier(image, form):
    candidate = None
    for row in range(4):
        for column in range(4):
            source_entry = form[row][column]
            image_entry = image[row][column]
            if source_entry == 0:
                if image_entry != 0:
                    return None
            else:
                ratio = image_entry / source_entry
                if candidate is None:
                    candidate = ratio
                elif ratio != candidate:
                    return None
    return candidate


# Alternating trace forms.
def omega_entry(parameter, left, right):
    traced = ring_mul(ring_mul(parameter, left), conjugate(right))
    return ring_trace(traced) / 5


def form_matrix(parameter):
    return tuple(
        tuple(
            omega_entry(parameter, BASIS[row], BASIS[column])
            for column in range(4)
        )
        for row in range(4)
    )


OMEGA_ONE = form_matrix(LAMBDA_ONE)
OMEGA_TWO = form_matrix(LAMBDA_TWO)


def pencil_form(first_coefficient, second_coefficient):
    return matrix_add(
        matrix_scale(first_coefficient, OMEGA_ONE),
        matrix_scale(second_coefficient, OMEGA_TWO),
    )


def pell_polynomial(first_coefficient, second_coefficient):
    return (
        first_coefficient * first_coefficient
        - first_coefficient * second_coefficient
        - second_coefficient * second_coefficient
    )


def real_mul(left, right):
    first_constant, first_phi = left
    second_constant, second_phi = right
    return (
        first_constant * second_constant + first_phi * second_phi,
        first_constant * second_phi
        + first_phi * second_constant
        + first_phi * second_phi,
    )


def real_pow(value, exponent):
    result = (1, 0)
    factor = value
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = real_mul(result, factor)
        factor = real_mul(factor, factor)
        remaining >>= 1
    return result


def real_norm(value):
    constant, phi_coefficient = value
    return (
        constant * constant
        + constant * phi_coefficient
        - phi_coefficient * phi_coefficient
    )


def imaginary_coordinates(value):
    return (value[0], value[2] - value[0])


def rebuild_imaginary(coordinates):
    return ring_add(
        ring_scale(coordinates[0], LAMBDA_ONE),
        ring_scale(coordinates[1], LAMBDA_TWO),
    )


def in_imaginary_lattice(value):
    coordinates = imaginary_coordinates(value)
    return (
        all(
            Fraction(coordinate).denominator == 1
            for coordinate in coordinates
        )
        and rebuild_imaginary(coordinates) == value
    )


def parameter_action_matrix(factor):
    first_column = imaginary_coordinates(ring_mul(LAMBDA_ONE, factor))
    second_column = imaginary_coordinates(ring_mul(LAMBDA_TWO, factor))
    return (
        (first_column[0], second_column[0]),
        (first_column[1], second_column[1]),
    )


def characteristic_polynomial_two(matrix):
    trace = matrix[0][0] + matrix[1][1]
    return (Fraction(1), -trace, determinant(matrix))


def evaluate_real_polynomial(polynomial, value):
    result = (0, 0)
    for coefficient in polynomial:
        result = real_mul(result, value)
        result = (result[0] + coefficient, result[1])
    return result


M_MINUS_ONE = multiplication_matrix(MINUS_ONE)
M_ROOT = multiplication_matrix(ROOT)
M_ROOT_INVERSE = multiplication_matrix(ROOT_INVERSE)
M_PHI = multiplication_matrix(PHI)
M_PHI_INVERSE = multiplication_matrix(PHI_INVERSE)
M_AXIOM = multiplication_matrix(AXIOM)
M_AXIOM_INVERSE = multiplication_matrix(AXIOM_INVERSE)
C_MATRIX = conjugation_matrix()
I4 = identity_matrix(4)
SHEAR_ONE = (
    (Fraction(1), Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
)
SHEAR_TWO = (
    (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1), Fraction(1)),
    (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
)
DIAGONAL_ONE = (
    (Fraction(-1), Fraction(0), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
)
TWICE_I4 = matrix_scale(2, I4)

COORDINATE_VALUES = tuple(range(-4, 5))
COEFFICIENT_VALUES = tuple(range(-20, 21))
COEFFICIENT_PAIRS = tuple(
    product(COEFFICIENT_VALUES, COEFFICIENT_VALUES)
)
NONBASIS_VECTORS = (
    (Fraction(1), Fraction(-1), Fraction(2), Fraction(0)),
    (Fraction(2), Fraction(3), Fraction(-1), Fraction(4)),
    (Fraction(-3), Fraction(0), Fraction(1), Fraction(2)),
    (Fraction(1), Fraction(1), Fraction(1), Fraction(1)),
)


# B1: ring arithmetic self-test.
minimal_polynomial_value = ring_sum(
    tuple(ring_pow(ROOT, exponent) for exponent in range(5))
)
check("B1-01 j^5 equals 1", ring_pow(ROOT, 5) == ONE)
check(
    "B1-02 j satisfies t^4+t^3+t^2+t+1",
    minimal_polynomial_value == ZERO,
)
check(
    "B1-03 phi^2 equals phi+1",
    ring_pow(PHI, 2) == ring_add(PHI, ONE),
)
check("B1-04 J*phi equals j", ring_mul(AXIOM, PHI) == ROOT)
check("B1-05 absolute norm of J equals 1", absolute_norm_element(AXIOM) == ONE)
check("B1-06 absolute trace of J equals 3", ring_trace(AXIOM) == 3)
check("B1-07 determinant of M_J equals 1", determinant(M_AXIOM) == 1)


# B2: the purely imaginary lattice in the declared coordinate box.
coordinate_solution_ok = True
for coordinates in product(
    COORDINATE_VALUES,
    COORDINATE_VALUES,
    COORDINATE_VALUES,
    COORDINATE_VALUES,
):
    value = tuple(Fraction(coordinate) for coordinate in coordinates)
    actual = conjugate(value) == ring_neg(value)
    predicted = (
        coordinates[1] == 2 * coordinates[0]
        and coordinates[2] + coordinates[3] == 2 * coordinates[0]
    )
    lattice_coordinates = (
        Fraction(coordinates[0]),
        Fraction(coordinates[2] - coordinates[0]),
    )
    rebuilt = rebuild_imaginary(lattice_coordinates)
    coordinate_solution_ok &= actual == predicted
    coordinate_solution_ok &= predicted == (rebuilt == value)
check(
    "B2-01 conjugation equation and lambda span agree on [-4,4]^4",
    coordinate_solution_ok,
)
check(
    "B2-02 lambda_1 and lambda_2 are purely imaginary",
    conjugate(LAMBDA_ONE) == ring_neg(LAMBDA_ONE)
    and conjugate(LAMBDA_TWO) == ring_neg(LAMBDA_TWO),
)
check(
    "B2-03 lambda_2 equals lambda_1*phi^-1",
    ring_mul(LAMBDA_ONE, PHI_INVERSE) == LAMBDA_TWO,
)
check(
    "B2-04 lambda_1*phi equals lambda_1+lambda_2",
    ring_mul(LAMBDA_ONE, PHI) == ring_add(LAMBDA_ONE, LAMBDA_TWO),
)


# B3: antisymmetry and alternation on the declared ordered vector square.
DECLARED_VECTORS = BASIS + NONBASIS_VECTORS
antisymmetry_ok = all(
    omega_entry(parameter, left, right)
    == -omega_entry(parameter, right, left)
    for parameter in (LAMBDA_ONE, LAMBDA_TWO)
    for left in DECLARED_VECTORS
    for right in DECLARED_VECTORS
)
alternation_ok = all(
    omega_entry(parameter, value, value) == 0
    for parameter in (LAMBDA_ONE, LAMBDA_TWO)
    for value in DECLARED_VECTORS
)
check(
    "B3-01 antisymmetry holds on the declared 8-vector ordered square",
    antisymmetry_ok,
)
check(
    "B3-02 alternation holds on the declared 8-vector list",
    alternation_ok,
)


# B4: integrality, one unimodular generator, and one nongenerator.
integrality_ok = all(
    integral_matrix(pencil_form(first_coefficient, second_coefficient))
    for first_coefficient, second_coefficient in COEFFICIENT_PAIRS
)
nongenerator_form = form_matrix(ring_scale(2, LAMBDA_ONE))
check(
    "B4-01 all pencil matrices are integral for -20<=a,b<=20",
    integrality_ok,
)
check("B4-02 determinant of Omega_1 equals 1", determinant(OMEGA_ONE) == 1)
check(
    "B4-03 the nongenerator 2*lambda_1 has determinant greater than 1",
    integral_matrix(nongenerator_form)
    and determinant(nongenerator_form) > 1,
)


# B5: the Pfaffian polynomial and its norm interpretation.
pfaffian_range_ok = all(
    pfaffian(pencil_form(first_coefficient, second_coefficient))
    == pell_polynomial(first_coefficient, second_coefficient)
    for first_coefficient, second_coefficient in COEFFICIENT_PAIRS
)
norm_range_ok = all(
    real_norm(
        (
            first_coefficient - second_coefficient,
            second_coefficient,
        )
    )
    == pell_polynomial(first_coefficient, second_coefficient)
    for first_coefficient, second_coefficient in COEFFICIENT_PAIRS
)
three_points = (
    pfaffian(pencil_form(1, 0)),
    pfaffian(pencil_form(0, 1)),
    pfaffian(pencil_form(1, 1)),
)
quadratic_coefficients = (
    three_points[0],
    three_points[2] - three_points[0] - three_points[1],
    three_points[1],
)
check(
    "B5-01 Pf(Omega_{a,b}) equals a^2-a*b-b^2 on [-20,20]^2",
    pfaffian_range_ok,
)
check(
    "B5-02 the Pfaffian equals the real quadratic norm on the range",
    norm_range_ok,
)
check(
    "B5-03 values at (1,0),(0,1),(1,1) determine coefficients 1,-1,-1",
    three_points == (1, -1, -1)
    and quadratic_coefficients == (1, -1, -1),
)


# B6: Pell members and the Fibonacci staircase.
unimodular_pell_ok = all(
    (
        determinant(pencil_form(first_coefficient, second_coefficient))
        == 1
    )
    == (abs(pell_polynomial(first_coefficient, second_coefficient)) == 1)
    for first_coefficient, second_coefficient in COEFFICIENT_PAIRS
)
fibonacci_values = [0, 1]
for _ in range(20):
    fibonacci_values.append(fibonacci_values[-1] + fibonacci_values[-2])
fibonacci_ok = all(
    pell_polynomial(fibonacci_values[index + 1], fibonacci_values[index])
    == (-1) ** index
    and real_pow((0, 1), index)
    == (fibonacci_values[index - 1], fibonacci_values[index])
    for index in range(1, 21)
)
check(
    "B6-01 unimodular matrices are exactly the Pell solutions on the range",
    unimodular_pell_ok,
)
check(
    "B6-02 Fibonacci pairs have Pfaffian (-1)^n for 1<=n<=20",
    fibonacci_ok,
)


# B7: the declared units and their pullback action.
DECLARED_UNIT_ACTIONS = (
    MINUS_ONE,
    ROOT,
    ROOT_INVERSE,
    PHI,
    PHI_INVERSE,
    AXIOM,
    AXIOM_INVERSE,
)
ROOTS_OF_UNITY = tuple(
    signed_root
    for exponent in range(5)
    for signed_root in (
        ring_pow(ROOT, exponent),
        ring_neg(ring_pow(ROOT, exponent)),
    )
)
DECLARED_FIXED_FORM_LIST = ROOTS_OF_UNITY + (
    PHI,
    PHI_INVERSE,
    AXIOM,
    AXIOM_INVERSE,
)
UNIT_INVERSE_PAIRS = (
    (MINUS_ONE, MINUS_ONE),
    (ROOT, ROOT_INVERSE),
    (PHI, PHI_INVERSE),
    (AXIOM, AXIOM_INVERSE),
)
unit_data_ok = all(
    ring_mul(unit, inverse) == ONE
    and determinant(multiplication_matrix(unit)) == 1
    and integral_element(unit)
    and integral_element(inverse)
    for unit, inverse in UNIT_INVERSE_PAIRS
)
pullback_action_ok = all(
    pullback(form_matrix(parameter), multiplication_matrix(unit))
    == form_matrix(
        ring_mul(parameter, ring_mul(unit, conjugate(unit)))
    )
    for unit in DECLARED_UNIT_ACTIONS
    for parameter in (LAMBDA_ONE, LAMBDA_TWO)
)
pencil_stability_ok = all(
    in_imaginary_lattice(
        ring_mul(parameter, ring_mul(unit, conjugate(unit)))
    )
    for unit in DECLARED_UNIT_ACTIONS
    for parameter in (LAMBDA_ONE, LAMBDA_TWO)
)
roots_distinct = all(
    ROOTS_OF_UNITY[first] != ROOTS_OF_UNITY[second]
    for first in range(10)
    for second in range(first + 1, 10)
)
fixed_form_ok = (
    roots_distinct
    and all(
        pullback(OMEGA_ONE, multiplication_matrix(unit)) == OMEGA_ONE
        for unit in DECLARED_FIXED_FORM_LIST[:10]
    )
    and all(
        pullback(OMEGA_ONE, multiplication_matrix(unit)) != OMEGA_ONE
        for unit in DECLARED_FIXED_FORM_LIST[10:]
    )
)
check("B7-01 declared generators and inverses are integral units", unit_data_ok)
check(
    "B7-02 unit pullback equals the relative-norm parameter action",
    pullback_action_ok,
)
check("B7-03 every declared unit action stays in the pencil", pencil_stability_ok)
check(
    "B7-04 exactly the ten roots in the fixed-form list preserve Omega_1",
    fixed_form_ok,
)


# B8: exact hyperbolic action matrices.
RELATIVE_NORM_AXIOM = ring_mul(AXIOM, conjugate(AXIOM))
ACTION_AXIOM = parameter_action_matrix(RELATIVE_NORM_AXIOM)
ACTION_PHI = parameter_action_matrix(PHI)
EXPECTED_ACTION_AXIOM = (
    (Fraction(1), Fraction(-1)),
    (Fraction(-1), Fraction(2)),
)
EXPECTED_ACTION_PHI = (
    (Fraction(1), Fraction(1)),
    (Fraction(1), Fraction(0)),
)
I2 = identity_matrix(2)
PHI_SQUARED_REAL = (1, 1)
PHI_INVERSE_SQUARED_REAL = (2, -1)
check(
    "B8-01 J*conj(J) equals phi^-2 and has the registered action matrix",
    RELATIVE_NORM_AXIOM == ring_pow(PHI_INVERSE, 2)
    and ACTION_AXIOM == EXPECTED_ACTION_AXIOM,
)
check(
    "B8-02 the phi action matrix has determinant -1",
    ACTION_PHI == EXPECTED_ACTION_PHI and determinant(ACTION_PHI) == -1,
)
check(
    "B8-03 A_J has determinant 1, trace 3, and polynomial t^2-3*t+1",
    determinant(ACTION_AXIOM) == 1
    and ACTION_AXIOM[0][0] + ACTION_AXIOM[1][1] == 3
    and characteristic_polynomial_two(ACTION_AXIOM) == (1, -3, 1),
)
check(
    "B8-04 the two eigenvalues are phi^2 and phi^-2",
    evaluate_real_polynomial((1, -3, 1), PHI_SQUARED_REAL) == (0, 0)
    and evaluate_real_polynomial(
        (1, -3, 1), PHI_INVERSE_SQUARED_REAL
    )
    == (0, 0)
    and PHI_SQUARED_REAL != PHI_INVERSE_SQUARED_REAL,
)
check(
    "B8-05 A_J is the inverse of the square of the phi action",
    matrix_mul(ACTION_AXIOM, matrix_mul(ACTION_PHI, ACTION_PHI)) == I2
    and matrix_mul(matrix_mul(ACTION_PHI, ACTION_PHI), ACTION_AXIOM) == I2,
)


# B9: Pfaffian covariance, the J entry obstruction, and conjugation.
DECLARED_INTEGRAL_MATRICES = (
    I4,
    M_MINUS_ONE,
    M_ROOT,
    M_ROOT_INVERSE,
    M_PHI,
    M_PHI_INVERSE,
    M_AXIOM,
    M_AXIOM_INVERSE,
    C_MATRIX,
    SHEAR_ONE,
    SHEAR_TWO,
    DIAGONAL_ONE,
    TWICE_I4,
)
DECLARED_PFAFFIAN_FORMS = (
    OMEGA_ONE,
    OMEGA_TWO,
    pencil_form(1, 1),
    pencil_form(2, -3),
)
pfaffian_law_ok = all(
    pfaffian(pullback(form, linear_map))
    == determinant(linear_map) * pfaffian(form)
    for linear_map in DECLARED_INTEGRAL_MATRICES
    for form in DECLARED_PFAFFIAN_FORMS
)
axiom_image = pullback(OMEGA_ONE, M_AXIOM)
entry_obstruction_ok = (
    determinant(M_AXIOM) == 1
    and axiom_image == pencil_form(1, -1)
    and scalar_multiplier(axiom_image, OMEGA_ONE) is None
)
conjugation_ok = (
    pullback(OMEGA_ONE, C_MATRIX) == matrix_scale(-1, OMEGA_ONE)
    and pullback(OMEGA_TWO, C_MATRIX) == matrix_scale(-1, OMEGA_TWO)
)
check(
    "B9-01 all declared matrices are integral",
    all(integral_matrix(matrix) for matrix in DECLARED_INTEGRAL_MATRICES),
)
check(
    "B9-02 Pf(M^T*W*M)=det(M)*Pf(W) on the declared matrices and forms",
    pfaffian_law_ok,
)
check(
    "B9-03 direct entries reject a scalar multiplier for the J pullback",
    entry_obstruction_ok,
)
check(
    "B9-04 conjugation pulls both pencil generators back to their negatives",
    conjugation_ok,
)


passed = sum(int(condition) for _, condition in CHECKS)
lines = [
    ("PASS " if condition else "FAIL ") + label
    for label, condition in CHECKS
]
if passed == len(CHECKS):
    lines.append(f"RESULT {passed}/{len(CHECKS)} ALL PASS")
else:
    lines.append(f"RESULT {passed}/{len(CHECKS)} FAILURES PRESENT")
sys.stdout.buffer.write(("\n".join(lines) + "\n").encode("ascii"))
raise SystemExit(0 if passed == len(CHECKS) else 1)
