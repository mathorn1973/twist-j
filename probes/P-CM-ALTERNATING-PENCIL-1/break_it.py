#!/usr/bin/env python3
"""Independent adversarial checks for P-CM-ALTERNATING-PENCIL-1.

Ring elements use five cyclic coefficients modulo the relation
1 + j + j^2 + j^3 + j^4 = 0.  The unique representative whose five
coefficients sum to zero keeps this route distinct from the verifier's
four-coordinate power-basis implementation.
"""

from fractions import Fraction
from itertools import product
import sys


ATTACKS = []


def record(label, condition):
    ATTACKS.append((label, bool(condition)))


def cyclic_reduce(coefficients):
    values = tuple(Fraction(coefficient) for coefficient in coefficients)
    average = sum(values, Fraction(0)) / 5
    return tuple(coefficient - average for coefficient in values)


def cyclic_add(left, right):
    return cyclic_reduce(
        tuple(left[index] + right[index] for index in range(5))
    )


def cyclic_neg(value):
    return cyclic_reduce(tuple(-coefficient for coefficient in value))


def cyclic_sub(left, right):
    return cyclic_add(left, cyclic_neg(right))


def cyclic_scale(scalar, value):
    return cyclic_reduce(
        tuple(Fraction(scalar) * coefficient for coefficient in value)
    )


def cyclic_mul(left, right):
    coefficients = [Fraction(0) for _ in range(5)]
    for left_degree in range(5):
        for right_degree in range(5):
            degree = (left_degree + right_degree) % 5
            coefficients[degree] += (
                left[left_degree] * right[right_degree]
            )
    return cyclic_reduce(tuple(coefficients))


def cyclic_pow(value, exponent):
    result = CYCLIC_ONE
    factor = value
    remaining = exponent
    while remaining > 0:
        if remaining % 2 == 1:
            result = cyclic_mul(result, factor)
        factor = cyclic_mul(factor, factor)
        remaining //= 2
    return result


def cyclic_conjugate(value):
    return cyclic_reduce(
        tuple(value[(-degree) % 5] for degree in range(5))
    )


def cyclic_trace(value):
    return 4 * value[0] - sum(value[1:], Fraction(0))


CYCLIC_ONE = cyclic_reduce((1, 0, 0, 0, 0))
CYCLIC_ROOT = cyclic_reduce((0, 1, 0, 0, 0))
CYCLIC_MINUS_ONE = cyclic_neg(CYCLIC_ONE)
CYCLIC_ROOT_INVERSE = cyclic_pow(CYCLIC_ROOT, 4)
REAL_UNIT = cyclic_neg(
    cyclic_add(cyclic_pow(CYCLIC_ROOT, 2), cyclic_pow(CYCLIC_ROOT, 3))
)
REAL_UNIT_INVERSE = cyclic_sub(REAL_UNIT, CYCLIC_ONE)
SPECIAL_UNIT = cyclic_add(CYCLIC_ONE, cyclic_pow(CYCLIC_ROOT, 2))
SPECIAL_UNIT_INVERSE = cyclic_mul(REAL_UNIT, CYCLIC_ROOT_INVERSE)
LAMBDA_ONE = cyclic_sub(CYCLIC_ROOT, CYCLIC_ROOT_INVERSE)
LAMBDA_TWO = cyclic_sub(
    cyclic_pow(CYCLIC_ROOT, 2),
    cyclic_pow(CYCLIC_ROOT, 3),
)


BASIS = (
    CYCLIC_ONE,
    CYCLIC_ROOT,
    cyclic_pow(CYCLIC_ROOT, 2),
    cyclic_pow(CYCLIC_ROOT, 3),
)


def power_basis_coordinates(value):
    shifted = tuple(value[index] - value[4] for index in range(4))
    if any(coefficient.denominator != 1 for coefficient in shifted):
        raise ValueError("nonintegral power-basis coordinate")
    return tuple(coefficient.numerator for coefficient in shifted)


def multiplication_matrix(value):
    columns = tuple(
        power_basis_coordinates(cyclic_mul(value, basis_value))
        for basis_value in BASIS
    )
    return tuple(
        tuple(columns[column][row] for column in range(4))
        for row in range(4)
    )


def matrix_transpose(matrix):
    return tuple(
        tuple(matrix[row][column] for row in range(4))
        for column in range(4)
    )


def matrix_mul(left, right):
    return tuple(
        tuple(
            sum(
                left[row][inner] * right[inner][column]
                for inner in range(4)
            )
            for column in range(4)
        )
        for row in range(4)
    )


def matrix_add(left, right):
    return tuple(
        tuple(
            left[row][column] + right[row][column]
            for column in range(4)
        )
        for row in range(4)
    )


def matrix_scale(scalar, matrix):
    return tuple(
        tuple(scalar * entry for entry in row)
        for row in matrix
    )


def pullback(form, linear_map):
    return matrix_mul(
        matrix_mul(matrix_transpose(linear_map), form),
        linear_map,
    )


def trace_gram(parameter):
    return tuple(
        tuple(
            cyclic_trace(
                cyclic_mul(
                    parameter,
                    cyclic_mul(left, cyclic_conjugate(right)),
                )
            )
            / 5
            for right in BASIS
        )
        for left in BASIS
    )


OMEGA_ONE = trace_gram(LAMBDA_ONE)
OMEGA_TWO = trace_gram(LAMBDA_TWO)


def pencil_form(first_coefficient, second_coefficient):
    return matrix_add(
        matrix_scale(first_coefficient, OMEGA_ONE),
        matrix_scale(second_coefficient, OMEGA_TWO),
    )


UPPER_POSITIONS = (
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 2),
    (1, 3),
    (2, 3),
)


def upper_entries(matrix):
    return tuple(matrix[row][column] for row, column in UPPER_POSITIONS)


def alternating_matrix(entries):
    matrix = [[0 for _ in range(4)] for _ in range(4)]
    for entry, position in zip(entries, UPPER_POSITIONS):
        row, column = position
        matrix[row][column] = entry
        matrix[column][row] = -entry
    return tuple(tuple(row) for row in matrix)


def pfaffian(matrix):
    return (
        matrix[0][1] * matrix[2][3]
        - matrix[0][2] * matrix[1][3]
        + matrix[0][3] * matrix[1][2]
    )


PENCIL_VECTOR_ONE = upper_entries(OMEGA_ONE)
PENCIL_VECTOR_TWO = upper_entries(OMEGA_TWO)


def pencil_coordinates(matrix):
    vector = upper_entries(matrix)
    for first in range(6):
        for second in range(first + 1, 6):
            minor = (
                PENCIL_VECTOR_ONE[first] * PENCIL_VECTOR_TWO[second]
                - PENCIL_VECTOR_ONE[second] * PENCIL_VECTOR_TWO[first]
            )
            if minor == 0:
                continue
            first_coefficient = Fraction(
                vector[first] * PENCIL_VECTOR_TWO[second]
                - vector[second] * PENCIL_VECTOR_TWO[first],
                minor,
            )
            second_coefficient = Fraction(
                PENCIL_VECTOR_ONE[first] * vector[second]
                - PENCIL_VECTOR_ONE[second] * vector[first],
                minor,
            )
            if (
                first_coefficient.denominator != 1
                or second_coefficient.denominator != 1
            ):
                return None
            coordinates = (
                first_coefficient.numerator,
                second_coefficient.numerator,
            )
            if pencil_form(*coordinates) == matrix:
                return coordinates
            return None
    raise ValueError("pencil generators are dependent")


def scalar_multiplier(image, source):
    candidate = None
    for row in range(4):
        for column in range(4):
            if source[row][column] != 0:
                candidate = Fraction(
                    image[row][column], source[row][column]
                )
                break
        if candidate is not None:
            break
    if candidate is None:
        return None
    if matrix_scale(candidate, source) != image:
        return None
    return candidate


def unit_with_real_exponent(sign, root_exponent, real_exponent):
    if real_exponent >= 0:
        real_factor = cyclic_pow(REAL_UNIT, real_exponent)
    else:
        real_factor = cyclic_pow(REAL_UNIT_INVERSE, -real_exponent)
    return cyclic_scale(
        sign,
        cyclic_mul(cyclic_pow(CYCLIC_ROOT, root_exponent), real_factor),
    )


# Attack one: widen the unit search around the fixed form.
UNIT_CANDIDATES = tuple(
    unit_with_real_exponent(sign, root_exponent, real_exponent)
    for real_exponent in range(-6, 7)
    for root_exponent in range(5)
    for sign in (1, -1)
)
TEN_ROOTS = tuple(
    cyclic_scale(sign, cyclic_pow(CYCLIC_ROOT, root_exponent))
    for root_exponent in range(5)
    for sign in (1, -1)
)
FIXING_UNITS = tuple(
    unit
    for unit in UNIT_CANDIDATES
    if pullback(OMEGA_ONE, multiplication_matrix(unit)) == OMEGA_ONE
)
unit_candidates_distinct = all(
    UNIT_CANDIDATES[first] != UNIT_CANDIDATES[second]
    for first in range(len(UNIT_CANDIDATES))
    for second in range(first + 1, len(UNIT_CANDIDATES))
)
ten_roots_distinct = all(
    TEN_ROOTS[first] != TEN_ROOTS[second]
    for first in range(len(TEN_ROOTS))
    for second in range(first + 1, len(TEN_ROOTS))
)
record(
    "A1 unit search fixes Omega_1 only at the ten roots of unity",
    unit_candidates_distinct
    and ten_roots_distinct
    and len(FIXING_UNITS) == 10
    and all(unit in TEN_ROOTS for unit in FIXING_UNITS)
    and all(unit in FIXING_UNITS for unit in TEN_ROOTS),
)


# Attack two: exhaust the small alternating-matrix box.
ORBIT_UNITS = (
    CYCLIC_ROOT,
    CYCLIC_ROOT_INVERSE,
    REAL_UNIT,
    REAL_UNIT_INVERSE,
    SPECIAL_UNIT,
    SPECIAL_UNIT_INVERSE,
)
ORBIT_MAPS = tuple(multiplication_matrix(unit) for unit in ORBIT_UNITS)
unimodular_count = 0
pencil_count = 0
outside_count = 0
orbit_equivalence = True
for upper in product(range(-2, 3), repeat=6):
    form = alternating_matrix(upper)
    if abs(pfaffian(form)) != 1:
        continue
    unimodular_count += 1
    is_pencil_member = pencil_coordinates(form) is not None
    orbit_is_in_pencil = all(
        pencil_coordinates(pullback(form, linear_map)) is not None
        for linear_map in ORBIT_MAPS
    )
    if is_pencil_member:
        pencil_count += 1
    else:
        outside_count += 1
    if is_pencil_member != orbit_is_in_pencil:
        orbit_equivalence = False
record(
    "A2 small unimodular forms have a pencil orbit exactly in the pencil",
    unimodular_count > 0
    and pencil_count > 0
    and outside_count > 0
    and orbit_equivalence,
)


# Attack three: widen the coefficient box for the Pfaffian identity.
wide_pfaffian_match = all(
    pfaffian(pencil_form(first_coefficient, second_coefficient))
    == (
        first_coefficient * first_coefficient
        - first_coefficient * second_coefficient
        - second_coefficient * second_coefficient
    )
    for first_coefficient in range(-50, 51)
    for second_coefficient in range(-50, 51)
)
record(
    "A3 wider coefficient box has no Pfaffian mismatch",
    wide_pfaffian_match,
)


# Attack four: solve every declared unit pullback for a scalar.
DECLARED_UNITS = (
    CYCLIC_MINUS_ONE,
    CYCLIC_ROOT,
    CYCLIC_ROOT_INVERSE,
    REAL_UNIT,
    REAL_UNIT_INVERSE,
    SPECIAL_UNIT,
    SPECIAL_UNIT_INVERSE,
)
DECLARED_MULTIPLIERS = tuple(
    scalar_multiplier(
        pullback(OMEGA_ONE, multiplication_matrix(unit)),
        OMEGA_ONE,
    )
    for unit in DECLARED_UNITS
)
record(
    "A4 declared unit scalar pullbacks yield only multiplier +1",
    sum(multiplier is not None for multiplier in DECLARED_MULTIPLIERS) == 3
    and all(
        multiplier is None or multiplier == 1
        for multiplier in DECLARED_MULTIPLIERS
    ),
)


# Attack five: reconstruct the form from an inverse-different generator.
INVERSE_DIFFERENT_GENERATOR = cyclic_scale(
    Fraction(1, 5),
    cyclic_sub(CYCLIC_ONE, CYCLIC_ROOT),
)
GENERATOR_UNIT_FACTOR = cyclic_mul(
    CYCLIC_ROOT,
    cyclic_add(
        cyclic_add(CYCLIC_ONE, CYCLIC_ROOT),
        cyclic_pow(CYCLIC_ROOT, 2),
    ),
)
FACTORED_TRACE_COEFFICIENT = cyclic_mul(
    GENERATOR_UNIT_FACTOR,
    INVERSE_DIFFERENT_GENERATOR,
)


def coefficient_gram(trace_coefficient):
    return tuple(
        tuple(
            cyclic_trace(
                cyclic_mul(
                    trace_coefficient,
                    cyclic_mul(left, cyclic_conjugate(right)),
                )
            )
            for right in BASIS
        )
        for left in BASIS
    )


FACTORED_OMEGA_ONE = coefficient_gram(FACTORED_TRACE_COEFFICIENT)
record(
    "A5 inverse-different reconstruction agrees with Omega_1",
    FACTORED_TRACE_COEFFICIENT
    == cyclic_scale(Fraction(1, 5), LAMBDA_ONE)
    and FACTORED_OMEGA_ONE == OMEGA_ONE,
)


passed = sum(int(condition) for _, condition in ATTACKS)
output_lines = [
    ("PASS " if condition else "FAIL ") + label
    for label, condition in ATTACKS
]
if passed == len(ATTACKS):
    output_lines.append(f"RESULT {passed}/{len(ATTACKS)} ALL PASS")
else:
    output_lines.append(f"RESULT {passed}/{len(ATTACKS)} FAILURES PRESENT")
sys.stdout.buffer.write(("\n".join(output_lines) + "\n").encode("ascii"))
raise SystemExit(0 if passed == len(ATTACKS) else 1)
