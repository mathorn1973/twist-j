#!/usr/bin/env python3
"""P-FCC-WEIGHTED-SHELL-REMAINDER-1, pure L2 exact certificate audit.
The written proof, not numerical sampling, owns the universal real-variable
inequalities, cosine zero criterion, integration argument, and uniform limit.
This code audits their finite rational/integer certificates only. It selects
no physical carrier, flux, temporal rule, cone, phase, or photon.

No input files, network, random choices, environment reads, floating point,
or filesystem writes. Successful scientific stdout is buffered until every
gate has passed. Execute only after the public preregistration pin is sealed.
"""

from fractions import Fraction
from itertools import product
from math import factorial
import sys


PROBE_ID = "P-FCC-WEIGHTED-SHELL-REMAINDER-1"
NORMS = (2, 4, 8, 10, 16)
WEIGHTS = (6, 1, 15, 1, 1)
SIZES = (12, 6, 12, 24, 6)
IDENTITY3 = (
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1)),
)


class AuditFailure(Exception):
    """An exact certificate failed; no successful transcript is emitted."""


def require(condition, message):
    if not condition:
        raise AuditFailure(message)


def clean_poly(poly):
    return {exponent: Fraction(value) for exponent, value in poly.items() if value}


def add_poly(left, right):
    result = dict(left)
    for exponent, value in right.items():
        result[exponent] = result.get(exponent, Fraction(0)) + value
    return clean_poly(result)


def scale_poly(poly, scalar):
    return clean_poly({exponent: scalar * value for exponent, value in poly.items()})


def multiply_poly(left, right):
    result = {}
    for left_exp, left_value in left.items():
        for right_exp, right_value in right.items():
            require(len(left_exp) == len(right_exp), "polynomial dimension mismatch")
            exponent = tuple(a + b for a, b in zip(left_exp, right_exp))
            result[exponent] = result.get(exponent, Fraction(0)) + left_value * right_value
    return clean_poly(result)


def power_poly(poly, power):
    require(power >= 0 and bool(poly), "invalid polynomial power input")
    dimension = len(next(iter(poly)))
    result = {(0,) * dimension: Fraction(1)}
    for _ in range(power):
        result = multiply_poly(result, poly)
    return result


def all_shells():
    buckets = {norm: [] for norm in NORMS}
    for vector in product(range(-4, 5), repeat=3):
        norm = sum(entry * entry for entry in vector)
        if norm in buckets:
            buckets[norm].append(vector)
    return tuple(tuple(buckets[norm]) for norm in NORMS)


def full_moment(shells, weights, degree):
    """Expand all coefficients independently by the multinomial formula."""
    require(len(shells) == len(weights), "shell/weight count mismatch")
    result = {}
    for x_degree in range(degree + 1):
        for y_degree in range(degree - x_degree + 1):
            z_degree = degree - x_degree - y_degree
            exponent = (x_degree, y_degree, z_degree)
            multinomial = factorial(degree) // (
                factorial(x_degree) * factorial(y_degree) * factorial(z_degree)
            )
            total = 0
            for shell, weight in zip(shells, weights):
                for x, y, z in shell:
                    total += weight * (x ** x_degree) * (y ** y_degree) * (z ** z_degree)
            result[exponent] = Fraction(multinomial * total)
    return clean_poly(result)


def expected_moments():
    radius_squared = {
        (2, 0, 0): Fraction(1),
        (0, 2, 0): Fraction(1),
        (0, 0, 2): Fraction(1),
    }
    moment2 = scale_poly(radius_squared, 648)
    moment4 = scale_poly(power_poly(radius_squared, 2), 3168)
    moment6 = {}
    for axis in range(3):
        exponent = [0, 0, 0]
        exponent[axis] = 6
        moment6[tuple(exponent)] = Fraction(21888)
    for first in range(3):
        for second in range(3):
            if first != second:
                exponent = [0, 0, 0]
                exponent[first] = 4
                exponent[second] = 2
                moment6[tuple(exponent)] = Fraction(63360)
    return radius_squared, {2: moment2, 4: moment4, 6: moment6}


def moments_match(shells, weights, expected):
    return all(full_moment(shells, weights, degree) == expected[degree] for degree in (2, 4, 6))


def trig_expr(poly, cosine=0, sine=0):
    """Exact p(x)+cosine*cos(x)+sine*sin(x); p uses integer powers."""
    return (
        {power: Fraction(value) for power, value in poly.items() if value},
        Fraction(cosine),
        Fraction(sine),
    )


def add_trig(left, right):
    polynomial = dict(left[0])
    for power, value in right[0].items():
        polynomial[power] = polynomial.get(power, Fraction(0)) + value
    return trig_expr(polynomial, left[1] + right[1], left[2] + right[2])


def derivative_trig(expression):
    polynomial, cosine, sine = expression
    return trig_expr(
        {power - 1: power * value for power, value in polynomial.items() if power},
        sine,
        -cosine,
    )


def second_derivative_trig(expression):
    return derivative_trig(derivative_trig(expression))


def at_zero_trig(expression):
    polynomial, cosine, _ = expression
    return polynomial.get(0, Fraction(0)) + cosine


def is_even_trig(expression):
    polynomial, _, sine = expression
    return sine == 0 and all(power % 2 == 0 for power in polynomial)


def scalar_functions():
    # The three literal coefficient lists are independent inputs to the audit.
    p2 = trig_expr({0: -1, 2: Fraction(1, 2)}, cosine=1)
    p4 = trig_expr({0: 1, 2: Fraction(-1, 2), 4: Fraction(1, 24)}, cosine=-1)
    p6 = trig_expr(
        {0: -1, 2: Fraction(1, 2), 4: Fraction(-1, 24), 6: Fraction(1, 720)},
        cosine=1,
    )
    return p2, p4, p6


def scalar_derivative_certificate(p2, p4, p6):
    return (
        second_derivative_trig(p2) == trig_expr({0: 1}, cosine=-1)
        and second_derivative_trig(p4) == p2
        and second_derivative_trig(p6) == p4
    )


def scalar_initial_and_sum_certificate(p2, p4, p6):
    return (
        all(is_even_trig(item) for item in (p2, p4, p6))
        and all(at_zero_trig(item) == 0 for item in (p2, p4, p6))
        and all(at_zero_trig(derivative_trig(item)) == 0 for item in (p2, p4, p6))
        and add_trig(p2, p4) == trig_expr({4: Fraction(1, 24)})
        and add_trig(p4, p6) == trig_expr({6: Fraction(1, 720)})
    )


def scalar_certificate(p2, p4, p6):
    return scalar_derivative_certificate(p2, p4, p6) and scalar_initial_and_sum_certificate(p2, p4, p6)


def positive_gap_certificate(radius_squared, moment6):
    gap = add_poly(scale_poly(power_poly(radius_squared, 3), 21888), scale_poly(moment6, -1))
    required_gap = {(2, 2, 2): Fraction(131328)}
    for first in range(3):
        for second in range(3):
            if first != second:
                exponent = [0, 0, 0]
                exponent[first] = 4
                exponent[second] = 2
                required_gap[tuple(exponent)] = Fraction(2304)
    return (
        gap == required_gap
        and all(value >= 0 for value in gap.values())
        and all(all(power % 2 == 0 for power in exponent) for exponent in gap)
    )


def normalization_certificate(quartic_constant, sextic_constant, bound_constant, weighted_count):
    # No claim that the global bound is sharp is tested or emitted.
    return (
        Fraction(648, 2) == 324
        and Fraction(3168, 24) == 132
        and quartic_constant == Fraction(132, 324)
        and sextic_constant == Fraction(21888, 720 * 324)
        and bound_constant == Fraction(2 * weighted_count, 324)
        and weighted_count == 288
    )


def transpose(matrix):
    return tuple(tuple(matrix[row][column] for row in range(3)) for column in range(3))


def multiply_matrix(left, right):
    return tuple(
        tuple(sum(left[row][middle] * right[middle][column] for middle in range(3)) for column in range(3))
        for row in range(3)
    )


def matrix_vector(matrix, vector):
    return tuple(sum(matrix[row][column] * vector[column] for column in range(3)) for row in range(3))


def determinant3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def fractional_part(value):
    value = Fraction(value)
    return value - (value.numerator // value.denominator)


def residue_vector(vector):
    return tuple(fractional_part(value) for value in vector)


def lattice_matrices():
    basis = (
        (Fraction(1), Fraction(1), Fraction(1)),
        (Fraction(1), Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
    )
    reconstruction = (
        (Fraction(1, 2), Fraction(1, 2), Fraction(-1, 2)),
        (Fraction(1, 2), Fraction(-1, 2), Fraction(-1, 2)),
        (Fraction(0), Fraction(0), Fraction(1)),
    )
    dual = (
        (Fraction(1, 2), Fraction(1, 2), Fraction(0)),
        (Fraction(1, 2), Fraction(-1, 2), Fraction(0)),
        (Fraction(-1, 2), Fraction(-1, 2), Fraction(1)),
    )
    return basis, reconstruction, dual


def lattice_span_certificate(shells, basis, reconstruction):
    basis_columns = transpose(basis)
    even_residues = tuple(vector for vector in product((0, 1), repeat=3) if sum(vector) % 2 == 0)
    return (
        all(sum(vector) % 2 == 0 for shell in shells for vector in shell)
        and all(column in shells[0] for column in basis_columns)
        and determinant3(basis) == -2
        and multiply_matrix(basis, reconstruction) == IDENTITY3
        and all((2 * entry).denominator == 1 for row in reconstruction for entry in row)
        and len(even_residues) == 4
        and all(
            all(value.denominator == 1 for value in matrix_vector(reconstruction, vector))
            for vector in even_residues
        )
    )


def dual_cosets(dual):
    return {residue_vector(matrix_vector(dual, vector)) for vector in product((0, 1), repeat=3)}


def dual_certificate(basis, dual):
    zero = (Fraction(0),) * 3
    half = (Fraction(1, 2),) * 3
    required_cosets = {zero, half}
    return (
        determinant3(basis) == -2
        and multiply_matrix(transpose(basis), dual) == IDENTITY3
        and all((2 * entry).denominator == 1 for row in dual for entry in row)
        and dual_cosets(dual) == required_cosets
        and all(
            all(value.denominator == 1 for value in matrix_vector(transpose(basis), representative))
            for representative in required_cosets
        )
    )


def scaling_certificate(moments, exponent_table):
    # In M_d(epsilon*k)/epsilon^2 every coefficient gains epsilon^(d-2).
    # Positive epsilon, the inequalities, and taking suprema are proved in text.
    if exponent_table != ((2, 0), (4, 2), (6, 4)):
        return False
    for degree, epsilon_degree in exponent_table:
        moment = moments[degree]
        if not all(sum(exponent) == degree for exponent in moment):
            return False
        transformed = {
            (sum(exponent) - 2,) + exponent: value
            for exponent, value in moment.items()
        }
        independently_expected = {
            (epsilon_degree,) + exponent: value
            for exponent, value in moment.items()
        }
        if transformed != independently_expected:
            return False
    return True


def main():
    passed = []

    def gate(label, condition):
        require(condition, label)
        passed.append(label)

    shells = all_shells()
    radius_squared, expected = expected_moments()
    moments = {degree: full_moment(shells, WEIGHTS, degree) for degree in (2, 4, 6)}
    weighted_count = sum(weight * len(shell) for weight, shell in zip(WEIGHTS, shells))

    gate(
        "G01 complete-shell-census-and-positive-weights",
        tuple(len(shell) for shell in shells) == SIZES
        and all(weight > 0 for weight in WEIGHTS)
        and all(len(set(shell)) == len(shell) for shell in shells)
        and all(sum(entry * entry for entry in vector) == norm for norm, shell in zip(NORMS, shells) for vector in shell),
    )
    gate("G02 weighted-cardinality-288", weighted_count == 288)
    gate("G03 complete-quadratic-moment", moments[2] == expected[2])
    gate("G04 complete-quartic-moment", moments[4] == expected[4])
    gate("G05 complete-sextic-moment-including-mixed-zero", moments[6] == expected[6] and moments[6].get((2, 2, 2), 0) == 0)

    p2, p4, p6 = scalar_functions()
    gate("G06 scalar-second-derivative-chain", scalar_derivative_certificate(p2, p4, p6))
    gate("G07 scalar-evenness-initial-values-additive-identities", scalar_initial_and_sum_certificate(p2, p4, p6))
    gate("G08 nonnegative-even-monomial-M6-gap", positive_gap_certificate(radius_squared, moments[6]))
    gate(
        "G09 exact-normalization-and-global-bound-constants",
        normalization_certificate(Fraction(11, 27), Fraction(38, 405), Fraction(16, 9), weighted_count),
    )

    basis, reconstruction, dual = lattice_matrices()
    gate("G10 complete-support-lattice-D3-certificate", lattice_span_certificate(shells, basis, reconstruction))
    gate("G11 exact-dual-basis-and-two-cosets", dual_certificate(basis, dual))
    gate("G12 scaling-degrees-two-four-six", scaling_certificate(moments, ((2, 0), (4, 2), (6, 4))))

    # Independent negative controls reuse the same certificate predicates.
    # They do not change the frozen datum used by any positive gate.
    changed_weights = (7,) + WEIGHTS[1:]
    dropped_shells = (tuple(vector for vector in shells[0] if vector != (1, 1, 0)),) + shells[1:]
    gate(
        "G13 negative-weight-and-missing-vector-controls-rejected",
        moments_match(shells, WEIGHTS, expected)
        and not moments_match(shells, changed_weights, expected)
        and len(dropped_shells[0]) == len(shells[0]) - 1
        and not moments_match(dropped_shells, WEIGHTS, expected),
    )

    bad_p4 = trig_expr({0: 1, 2: Fraction(-1, 2), 4: Fraction(-1, 24)}, cosine=-1)
    gate(
        "G14 negative-scalar-sign-and-bound-constant-controls-rejected",
        scalar_certificate(p2, p4, p6)
        and not scalar_certificate(p2, bad_p4, p6)
        and not normalization_certificate(Fraction(11, 27), Fraction(37, 405), Fraction(16, 9), weighted_count)
        and not normalization_certificate(Fraction(-11, 27), Fraction(38, 405), Fraction(16, 9), weighted_count),
    )

    bad_dual = (dual[0], dual[1], (Fraction(1, 2), dual[2][1], dual[2][2]))
    gate(
        "G15 negative-dual-control-rejected-despite-same-residues",
        dual_cosets(bad_dual) == dual_cosets(dual)
        and not dual_certificate(basis, bad_dual),
    )
    gate(
        "G16 negative-scaling-exponent-control-rejected",
        not scaling_certificate(moments, ((2, 0), (4, 3), (6, 4))),
    )

    require(len(passed) == 16, "certificate gate count mismatch")
    lines = [PROBE_ID + " EXACT CERTIFICATE AUDIT"]
    lines.extend(label + " PASS" for label in passed)
    lines.append("ALL EXACT CERTIFICATES PASS: " + str(len(passed)) + "/16")
    lines.append("Universal real-variable conclusions rest on the written proof.")
    lines.append("L2 ONLY; no carrier selection, temporal rule, phase, or physical photon.")
    transcript = "\n".join(lines) + "\n"
    require(transcript.isascii(), "scientific transcript must be ASCII")
    sys.stdout.write(transcript)


if __name__ == "__main__":
    if len(sys.argv) != 1:
        sys.stderr.write("STOP: this verifier accepts no arguments.\n")
        sys.exit(2)
    try:
        main()
    except Exception:
        sys.stderr.write("STOP: exact certificate audit failed.\n")
        sys.exit(1)
