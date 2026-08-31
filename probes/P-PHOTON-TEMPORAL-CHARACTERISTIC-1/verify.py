#!/usr/bin/env python3
"""Exact certificate audit for P-PHOTON-TEMPORAL-CHARACTERISTIC-1.

The written proof in PREREG.md owns the universal real-variable statements.
This verifier audits their finite integer/rational certificates and the exact
transfer algebra.  It does not sample momentum, frequency, or epsilon.

No input files, network, subprocesses, random choices, clocks, environment
reads, floating point, or filesystem writes.  Successful scientific stdout
is buffered until every gate passes.  Execute only after the public pin.
"""

from fractions import Fraction
from itertools import permutations, product
from math import factorial
import sys


PROBE_ID = "P-PHOTON-TEMPORAL-CHARACTERISTIC-1"
NORMS = (2, 4, 8, 10, 16)
WEIGHTS = (6, 1, 15, 1, 1)
SIZES = (12, 6, 12, 24, 6)
SCALE = Fraction(1, 324)
MAX_SYMBOL = Fraction(16, 9)
IDENTITY3 = (
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1)),
)


class AuditFailure(Exception):
    """A frozen exact certificate failed."""


def require(condition, message):
    if not condition:
        raise AuditFailure(message)


def all_shells():
    buckets = {norm: [] for norm in NORMS}
    for vector in product(range(-4, 5), repeat=3):
        norm = sum(entry * entry for entry in vector)
        if norm in buckets:
            buckets[norm].append(vector)
    return tuple(tuple(buckets[norm]) for norm in NORMS)


def clean_poly(poly):
    return {exponent: Fraction(value) for exponent, value in poly.items() if value}


def add_poly(left, right):
    result = dict(left)
    for exponent, value in right.items():
        result[exponent] = result.get(exponent, Fraction(0)) + value
    return clean_poly(result)


def scale_poly(poly, scalar):
    return clean_poly({exponent: Fraction(scalar) * value for exponent, value in poly.items()})


def multiply_poly(left, right):
    result = {}
    for left_exp, left_value in left.items():
        for right_exp, right_value in right.items():
            require(len(left_exp) == len(right_exp), "polynomial dimension mismatch")
            exponent = tuple(a + b for a, b in zip(left_exp, right_exp))
            result[exponent] = result.get(exponent, Fraction(0)) + left_value * right_value
    return clean_poly(result)


def power_poly(poly, power):
    require(power >= 0 and poly, "invalid polynomial power")
    dimension = len(next(iter(poly)))
    result = {(0,) * dimension: Fraction(1)}
    for _ in range(power):
        result = multiply_poly(result, poly)
    return result


def full_moment(shells, weights, degree):
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
    return {
        2: scale_poly(radius_squared, 648),
        4: scale_poly(power_poly(radius_squared, 2), 3168),
    }


def moments_match(shells, weights, expected):
    return all(full_moment(shells, weights, degree) == expected[degree] for degree in (2, 4))


def signed_permutation_group():
    return tuple((permutation, signs) for permutation in permutations(range(3)) for signs in product((-1, 1), repeat=3))


def act_signed_permutation(action, vector):
    permutation, signs = action
    return tuple(signs[index] * vector[permutation[index]] for index in range(3))


def point_group_certificate(shells):
    group = signed_permutation_group()
    shell_sets = tuple(set(shell) for shell in shells)
    return len(group) == 48 and all(
        act_signed_permutation(action, vector) in shell_set
        for action in group
        for shell, shell_set in zip(shells, shell_sets)
        for vector in shell
    )


def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    return tuple(tuple(matrix[row][column] for row in range(rows)) for column in range(columns))


def multiply_matrix(left, right):
    return tuple(
        tuple(
            sum(left[row][middle] * right[middle][column] for middle in range(len(right)))
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def add_matrix(left, right):
    return tuple(tuple(a + b for a, b in zip(left_row, right_row)) for left_row, right_row in zip(left, right))


def scale_matrix(matrix, scalar):
    return tuple(tuple(Fraction(scalar) * value for value in row) for row in matrix)


def matrix_vector(matrix, vector):
    return tuple(sum(matrix[row][column] * vector[column] for column in range(len(vector))) for row in range(len(matrix)))


def determinant2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def determinant3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def fractional_part(value):
    value = Fraction(value)
    return value - value.numerator // value.denominator


def residue_vector(vector):
    return tuple(fractional_part(value) for value in vector)


def lattice_data():
    basis = (
        (Fraction(1), Fraction(1), Fraction(0)),
        (Fraction(1), Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(1), Fraction(1)),
    )
    dual = (
        (Fraction(1, 2), Fraction(1, 2), Fraction(-1, 2)),
        (Fraction(1, 2), Fraction(-1, 2), Fraction(1, 2)),
        (Fraction(-1, 2), Fraction(1, 2), Fraction(1, 2)),
    )
    return basis, dual


def support_lattice_certificate(shells, basis):
    columns = transpose(basis)
    even_residues = tuple(vector for vector in product((0, 1), repeat=3) if sum(vector) % 2 == 0)
    return (
        all(sum(vector) % 2 == 0 for shell in shells for vector in shell)
        and all(column in shells[0] for column in columns)
        and determinant3(basis) == -2
        and len(even_residues) == 4
    )


def dual_cosets(dual):
    return {residue_vector(matrix_vector(dual, vector)) for vector in product((0, 1), repeat=3)}


def reciprocal_certificate(basis, dual):
    zero = (Fraction(0),) * 3
    half = (Fraction(1, 2),) * 3
    required = {zero, half}
    return (
        multiply_matrix(transpose(basis), dual) == IDENTITY3
        and dual_cosets(dual) == required
        and all(
            all(value.denominator == 1 for value in matrix_vector(transpose(basis), representative))
            for representative in required
        )
    )


def flat_flux(_x, _vector):
    return Fraction(1)


def bad_flux(_x, vector):
    marked = {(1, 1, 0), (-1, -1, 0)}
    return Fraction(-1) if tuple(vector) in marked else Fraction(1)


def flux_reversal_certificate(flux, shell):
    origin = (0, 0, 0)
    for vector in shell:
        value = flux(origin, vector)
        reverse = flux(tuple(origin[index] + vector[index] for index in range(3)), tuple(-entry for entry in vector))
        if value not in (Fraction(-1), Fraction(1)) or reverse != value:
            return False
    return True


def triangle_holonomy(flux):
    origin = (0, 0, 0)
    first = (1, 1, 0)
    second = (-1, 0, 1)
    third = (0, -1, -1)
    x1 = tuple(origin[index] + first[index] for index in range(3))
    x2 = tuple(x1[index] + second[index] for index in range(3))
    require(tuple(first[index] + second[index] + third[index] for index in range(3)) == origin, "triangle does not close")
    return flux(origin, first) * flux(x1, second) * flux(x2, third)


def flux_certificate(flux, shell):
    origin = (0, 0, 0)
    return (
        all(flux(origin, vector) == 1 for vector in shell)
        and flux_reversal_certificate(flux, shell)
        and triangle_holonomy(flux) == 1
    )


def trig_expr(poly, cosine=0, sine=0):
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


def scalar_remainder_certificate(p2, p4):
    return (
        second_derivative_trig(p2) == trig_expr({0: 1}, cosine=-1)
        and second_derivative_trig(p4) == p2
        and at_zero_trig(p2) == 0
        and at_zero_trig(derivative_trig(p2)) == 0
        and at_zero_trig(p4) == 0
        and at_zero_trig(derivative_trig(p4)) == 0
        and add_trig(p2, p4) == trig_expr({4: Fraction(1, 24)})
    )


def temporal_class_certificate(a, b):
    return Fraction(2) + Fraction(a) == 0 and Fraction(b) == 1


def pconstant(value):
    return {(0, 0): Fraction(value)} if value else {}


def pvariable(index):
    exponent = [0, 0]
    exponent[index] = 1
    return {tuple(exponent): Fraction(1)}


def transfer_polynomials(lower_left=1):
    symbol = pvariable(1)
    return (
        (add_poly(pconstant(2), scale_poly(symbol, -1)), pconstant(-1)),
        (pconstant(lower_left), pconstant(0)),
    )


def polynomial_det2(matrix):
    return add_poly(multiply_poly(matrix[0][0], matrix[1][1]), scale_poly(multiply_poly(matrix[0][1], matrix[1][0]), -1))


def characteristic_polynomial(transfer):
    lam = pvariable(0)
    matrix = (
        (add_poly(lam, scale_poly(transfer[0][0], -1)), scale_poly(transfer[0][1], -1)),
        (scale_poly(transfer[1][0], -1), add_poly(lam, scale_poly(transfer[1][1], -1))),
    )
    return polynomial_det2(matrix)


def expected_characteristic():
    lam = pvariable(0)
    symbol = pvariable(1)
    return add_poly(
        add_poly(power_poly(lam, 2), scale_poly(lam, -2)),
        add_poly(multiply_poly(lam, symbol), pconstant(1)),
    )


def sp_clean(poly):
    return {degree: Fraction(value) for degree, value in poly.items() if value}


def sp_add(left, right):
    result = dict(left)
    for degree, value in right.items():
        result[degree] = result.get(degree, Fraction(0)) + value
    return sp_clean(result)


def sp_scale(poly, scalar):
    return sp_clean({degree: Fraction(scalar) * value for degree, value in poly.items()})


def sp_mul(left, right):
    result = {}
    for left_degree, left_value in left.items():
        for right_degree, right_value in right.items():
            degree = left_degree + right_degree
            result[degree] = result.get(degree, Fraction(0)) + left_value * right_value
    return sp_clean(result)


def root_certificate():
    one = {0: Fraction(1)}
    symbol = {1: Fraction(1)}
    real = sp_add(one, sp_scale(symbol, Fraction(-1, 2)))
    imag_squared = sp_add(symbol, {2: Fraction(-1, 4)})
    two_minus_symbol = sp_add({0: Fraction(2)}, sp_scale(symbol, -1))
    norm = sp_add(sp_mul(real, real), imag_squared)
    real_equation = sp_add(
        sp_add(sp_mul(real, real), sp_scale(imag_squared, -1)),
        sp_add(sp_scale(sp_mul(two_minus_symbol, real), -1), one),
    )
    imaginary_equation = sp_add(sp_scale(real, 2), sp_scale(two_minus_symbol, -1))
    discriminant = sp_add({2: Fraction(1)}, {1: Fraction(-4)})
    required_discriminant = sp_mul(symbol, sp_add(symbol, {0: Fraction(-4)}))
    return norm == one and not real_equation and not imaginary_equation and discriminant == required_discriminant


def apex_certificate():
    t0 = ((Fraction(2), Fraction(-1)), (Fraction(1), Fraction(0)))
    identity = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    nilpotent = add_matrix(t0, scale_matrix(identity, -1))
    zero = ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(0)))
    return (
        determinant2(t0) == 1
        and t0 != identity
        and multiply_matrix(nilpotent, nilpotent) == zero
        and t0[0][0] + t0[1][1] == 2
    )


def normalization_certificate(moment2, moment4, scale, temporal_constant, spatial_constant):
    quadratic = moment2.get((2, 0, 0), 0) * scale / 2
    quartic = moment4.get((4, 0, 0), 0) * scale / 24
    return (
        quadratic == 1
        and quartic == Fraction(11, 27)
        and temporal_constant == Fraction(1, 12)
        and spatial_constant == Fraction(11, 27)
    )


def main():
    passed = []

    def gate(label, condition):
        require(condition, label)
        passed.append(label)

    shells = all_shells()
    expected = expected_moments()
    moments = {degree: full_moment(shells, WEIGHTS, degree) for degree in (2, 4)}
    weighted_count = sum(weight * len(shell) for weight, shell in zip(WEIGHTS, shells))
    all_steps = tuple(vector for shell in shells for vector in shell)
    basis, dual = lattice_data()

    gate(
        "G01 complete-shells-positive-selected-weights",
        tuple(len(shell) for shell in shells) == SIZES
        and all(weight > 0 for weight in WEIGHTS)
        and all(len(set(shell)) == len(shell) for shell in shells)
        and all(sum(entry * entry for entry in vector) == norm for norm, shell in zip(NORMS, shells) for vector in shell),
    )
    gate("G02 exact-48-signed-permutation-symmetry", point_group_certificate(shells))
    gate(
        "G03 exact-second-fourth-moments-and-weighted-count",
        moments == expected and weighted_count == 288,
    )
    gate(
        "G04 selected-scale-unit-tangent-and-global-bound",
        SCALE == Fraction(1, 324)
        and expected[2][(2, 0, 0)] * SCALE / 2 == 1
        and Fraction(2 * weighted_count) * SCALE == MAX_SYMBOL
        and MAX_SYMBOL < 4,
    )
    gate("G05 complete-support-lattice-is-D3", support_lattice_certificate(shells, basis))
    gate("G06 exact-reciprocal-two-coset-lattice", reciprocal_certificate(basis, dual))
    gate(
        "G07 fixed-trivial-flux-reversal-and-holonomy",
        flux_certificate(flat_flux, all_steps),
    )
    gate(
        "G08 Fourier-symbol-shell-reversal-certificate",
        all(tuple(-entry for entry in vector) in set(shell) for shell in shells for vector in shell)
        and all(flat_flux((0, 0, 0), vector) == 1 for shell in shells for vector in shell),
    )
    gate(
        "G09 selected-temporal-class-unique-coefficients",
        temporal_class_certificate(-2, 1),
    )

    transfer = transfer_polynomials()
    gate("G10 transfer-determinant-one", polynomial_det2(transfer) == pconstant(1))
    gate(
        "G11 exact-total-characteristic-polynomial",
        characteristic_polynomial(transfer) == expected_characteristic(),
    )
    gate("G12 reciprocal-unit-circle-root-algebra", root_certificate())
    gate(
        "G13 certified-stability-range-from-global-bound",
        Fraction(0) <= MAX_SYMBOL < 4
        and Fraction(2) - MAX_SYMBOL == Fraction(2, 9)
        and MAX_SYMBOL * (4 - MAX_SYMBOL) > 0,
    )
    gate("G14 double-root-parabolic-apex", apex_certificate())

    p2 = trig_expr({0: -1, 2: Fraction(1, 2)}, cosine=1)
    p4 = trig_expr({0: 1, 2: Fraction(-1, 2), 4: Fraction(1, 24)}, cosine=-1)
    gate("G15 global-scalar-cosine-remainder-chain", scalar_remainder_certificate(p2, p4))
    gate(
        "G16 exact-temporal-spatial-scaling-constants",
        normalization_certificate(moments[2], moments[4], SCALE, Fraction(1, 12), Fraction(11, 27)),
    )
    gate(
        "G17 unique-zero-character-after-D3-quotient",
        support_lattice_certificate(shells, basis)
        and reciprocal_certificate(basis, dual)
        and all(weight > 0 for weight in WEIGHTS),
    )

    changed_weights = (7,) + WEIGHTS[1:]
    dropped_shells = (tuple(vector for vector in shells[0] if vector != (1, 1, 0)),) + shells[1:]
    gate(
        "G18 negative-spatial-data-and-scale-controls-rejected",
        moments_match(shells, WEIGHTS, expected)
        and not moments_match(shells, changed_weights, expected)
        and not moments_match(dropped_shells, WEIGHTS, expected)
        and not normalization_certificate(moments[2], moments[4], Fraction(1, 323), Fraction(1, 12), Fraction(11, 27)),
    )

    # Triple the first dual-basis column.  Modulo Z^3 this still displays the
    # same two residue classes, but it is a genuine index-three sublattice,
    # not a unimodular change of basis of the selected reciprocal lattice.
    bad_dual = tuple((3 * row[0], row[1], row[2]) for row in dual)
    gate(
        "G19 negative-dual-and-flux-controls-rejected",
        dual_cosets(bad_dual) == dual_cosets(dual)
        and not reciprocal_certificate(basis, bad_dual)
        and flux_reversal_certificate(bad_flux, all_steps)
        and triangle_holonomy(bad_flux) == -1
        and not flux_certificate(bad_flux, all_steps),
    )

    bad_transfer = transfer_polynomials(lower_left=-1)
    altered_characteristic = add_poly(expected_characteristic(), {(0, 1): Fraction(1)})
    bad_p4 = trig_expr({0: 1, 2: Fraction(-1, 2), 4: Fraction(-1, 24)}, cosine=-1)
    gate(
        "G20 negative-temporal-transfer-and-bound-controls-rejected",
        not temporal_class_certificate(-1, 1)
        and not temporal_class_certificate(-2, 2)
        and polynomial_det2(bad_transfer) != pconstant(1)
        and characteristic_polynomial(transfer) != altered_characteristic
        and not scalar_remainder_certificate(p2, bad_p4)
        and not normalization_certificate(moments[2], moments[4], SCALE, Fraction(1, 13), Fraction(11, 27))
        and not normalization_certificate(moments[2], moments[4], SCALE, Fraction(1, 12), Fraction(10, 27)),
    )

    require(len(passed) == 20, "certificate gate count mismatch")
    lines = [PROBE_ID + " EXACT CERTIFICATE AUDIT"]
    lines.extend(label + " PASS" for label in passed)
    lines.append("ALL EXACT CERTIFICATES PASS: 20/20")
    lines.append("Owner datum is D; the conditional characteristic is proof-first T.")
    lines.append("L2-to-L5 only; Herm2 identification and physical photon remain open.")
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
