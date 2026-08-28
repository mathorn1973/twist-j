#!/usr/bin/env python3
"""Exact audit for P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1.

The universal proof is frozen in PREREG.md.  This verifier constructs the
covariant pullback from M_J and audits every finite identity with integers,
Fraction, and exact Q(phi) arithmetic.  Standard library only; no numerical
eigenvalues, tolerance, randomness, network, clock, subprocess, or search.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


PROBE = "P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1"
CONFIRMED = "CM-ALTERNATING-PRIMARY-LATTICE-SEAM-CONFIRMED"
PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))

M_J = (
    (1, 0, -1, 1),
    (0, 1, -1, 0),
    (1, 0, 0, 0),
    (0, 1, -1, 1),
)

OMEGA_1 = (1, 0, 0, 1, 0, 1)
OMEGA_2 = (0, 1, -1, 0, 1, 0)

C_BASIS = (
    (-1, 0, 1, 0, 0, 0),
    (0, -1, 0, 1, 0, 0),
    (0, -1, 0, 0, 1, 0),
    (-1, 0, 0, 0, 0, 1),
)

Q_POLY = (1, -3, 1)
R_POLY = (1, -1, 1, -1, 1)


def require(condition, message):
    if not condition:
        raise RuntimeError("STOP: " + message)


def gate(number, label, condition):
    require(condition, "G%02d %s" % (number, label))
    print("G%02d %s PASS" % (number, label))


def gcd_int(left, right):
    a = abs(int(left))
    b = abs(int(right))
    while b:
        a, b = b, a % b
    return a


def lcm_int(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_int(left, right)


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def zero_matrix(rows, columns):
    return [[Fraction(0) for _ in range(columns)] for _ in range(rows)]


def identity(size):
    out = zero_matrix(size, size)
    for index in range(size):
        out[index][index] = Fraction(1)
    return out


def matmul(left, right):
    require(left and right, "empty matrix product")
    require(len(left[0]) == len(right), "matrix product shape")
    require(all(len(row) == len(left[0]) for row in left), "ragged left matrix")
    require(all(len(row) == len(right[0]) for row in right), "ragged right matrix")
    out = []
    for row in left:
        out_row = []
        for column in zip(*right):
            total = 0
            for left_value, right_value in zip(row, column):
                total += left_value * right_value
            out_row.append(total)
        out.append(out_row)
    return out


def matadd(left, right):
    require(len(left) == len(right), "matrix sum rows")
    require(all(len(a) == len(b) for a, b in zip(left, right)), "matrix sum columns")
    return [
        [a + b for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]


def matscale(matrix, scalar):
    return [[scalar * value for value in row] for row in matrix]


def matpow(matrix, exponent):
    require(exponent >= 0, "negative matrix exponent")
    result = identity(len(matrix))
    factor = [list(row) for row in matrix]
    power = exponent
    while power:
        if power & 1:
            result = matmul(result, factor)
        factor = matmul(factor, factor)
        power >>= 1
    return result


def matvec(matrix, vector):
    require(all(len(row) == len(vector) for row in matrix), "matrix-vector shape")
    out = []
    for row in matrix:
        total = 0
        for coefficient, value in zip(row, vector):
            total += coefficient * value
        out.append(total)
    return out


def columns_matrix(columns):
    require(columns, "empty column family")
    width = len(columns[0])
    require(all(len(column) == width for column in columns), "column shape")
    return [[columns[column][row] for column in range(len(columns))] for row in range(width)]


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


def rref(matrix):
    if not matrix:
        return [], ()
    work = [[Fraction(value) for value in row] for row in matrix]
    columns = len(work[0])
    require(all(len(row) == columns for row in work), "rref shape")
    pivot_row = 0
    pivots = []
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(work[row], work[pivot_row])
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(work):
            break
    return work, tuple(pivots)


def matrix_rank(matrix):
    return len(rref(matrix)[1])


def canonical_rowspace(matrix):
    reduced, pivots = rref(matrix)
    return [row for row in reduced[: len(pivots)]]


def is_zero_matrix(matrix):
    return all(value == 0 for row in matrix for value in row)


def vector_add(left, right):
    return [a + b for a, b in zip(left, right)]


def vector_scale(vector, scalar):
    return [scalar * value for value in vector]


def poly_trim(poly):
    out = [Fraction(value) for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_add(left, right):
    out = [Fraction(0) for _ in range(max(len(left), len(right)))]
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return poly_trim(out)


def poly_scale(poly, scalar):
    return poly_trim([Fraction(scalar) * Fraction(value) for value in poly])


def poly_mul(left, right):
    out = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            out[left_index + right_index] += Fraction(left_value) * Fraction(right_value)
    return poly_trim(out)


def poly_pow(poly, exponent):
    require(exponent >= 0, "negative polynomial exponent")
    result = [Fraction(1)]
    factor = poly_trim(poly)
    power = exponent
    while power:
        if power & 1:
            result = poly_mul(result, factor)
        factor = poly_mul(factor, factor)
        power >>= 1
    return result


def poly_compose(poly, inner):
    result = [Fraction(0)]
    for exponent, coefficient in enumerate(poly):
        result = poly_add(result, poly_scale(poly_pow(inner, exponent), coefficient))
    return poly_trim(result)


def poly_matrix_eval(poly, matrix):
    size = len(matrix)
    result = zero_matrix(size, size)
    unit = identity(size)
    for coefficient in reversed(poly):
        result = matadd(matmul(result, matrix), matscale(unit, Fraction(coefficient)))
    return result


def characteristic_polynomial(matrix):
    size = len(matrix)
    require(all(len(row) == size for row in matrix), "characteristic shape")
    unit = identity(size)
    state = unit
    coefficients = [Fraction(1)]
    for step in range(1, size + 1):
        product = matmul(matrix, state)
        coefficient = -sum(product[index][index] for index in range(size)) / Fraction(step)
        coefficients.append(coefficient)
        state = matadd(product, matscale(unit, coefficient))
    return coefficients


def resultant(left, right):
    left = poly_trim(left)
    right = poly_trim(right)
    left_degree = len(left) - 1
    right_degree = len(right) - 1
    left_high = list(reversed(left))
    right_high = list(reversed(right))
    size = left_degree + right_degree
    sylvester = []
    for shift in range(right_degree):
        sylvester.append(
            [Fraction(0)] * shift
            + left_high
            + [Fraction(0)] * (size - shift - len(left_high))
        )
    for shift in range(left_degree):
        sylvester.append(
            [Fraction(0)] * shift
            + right_high
            + [Fraction(0)] * (size - shift - len(right_high))
        )
    return determinant(sylvester)


def alt_matrix(coordinates):
    require(len(coordinates) == 6, "alternating coordinate count")
    out = [[0 for _ in range(4)] for _ in range(4)]
    for value, (row, column) in zip(coordinates, PAIRS):
        out[row][column] = value
        out[column][row] = -value
    return out


def alt_coordinates(matrix):
    return [matrix[row][column] for row, column in PAIRS]


def pullback_coordinates(coordinates):
    form = alt_matrix(coordinates)
    return alt_coordinates(matmul(transpose(M_J), matmul(form, M_J)))


def construct_pullback_matrix():
    columns = []
    for index in range(6):
        basis = [0 for _ in range(6)]
        basis[index] = 1
        columns.append(pullback_coordinates(basis))
    return columns_matrix(columns)


def pfaffian(coordinates):
    w01, w02, w03, w12, w13, w23 = coordinates
    return w01 * w23 - w02 * w13 + w03 * w12


def pfaffian_quadratic_matrix():
    out = zero_matrix(6, 6)
    out[0][5] = out[5][0] = Fraction(1, 2)
    out[1][4] = out[4][1] = Fraction(-1, 2)
    out[2][3] = out[3][2] = Fraction(1, 2)
    return out


def form_value(coordinates, left, right):
    form = alt_matrix(coordinates)
    total = 0
    for row in range(4):
        for column in range(4):
            total += left[row] * form[row][column] * right[column]
    return total


def row_times_matrix(row, matrix):
    return [
        sum(row[index] * matrix[index][column] for index in range(len(row)))
        for column in range(len(matrix[0]))
    ]


def common_denominator(matrix):
    value = 1
    for row in matrix:
        for entry in row:
            value = lcm_int(value, Fraction(entry).denominator)
    return value


def integer_content(matrix):
    value = 0
    for row in matrix:
        for entry in row:
            fraction = Fraction(entry)
            require(fraction.denominator == 1, "content of nonintegral matrix")
            value = gcd_int(value, fraction.numerator)
    return value


@dataclass(frozen=True)
class QPhi:
    """a+b*phi with phi^2=phi+1 and a,b in Q."""

    a: Fraction
    b: Fraction = Fraction(0)

    @staticmethod
    def coerce(value):
        if isinstance(value, QPhi):
            return value
        return QPhi(Fraction(value), Fraction(0))

    def __add__(self, other):
        value = QPhi.coerce(other)
        return QPhi(self.a + value.a, self.b + value.b)

    __radd__ = __add__

    def __neg__(self):
        return QPhi(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-QPhi.coerce(other))

    def __rsub__(self, other):
        return QPhi.coerce(other) - self

    def __mul__(self, other):
        value = QPhi.coerce(other)
        return QPhi(
            self.a * value.a + self.b * value.b,
            self.a * value.b + self.b * value.a + self.b * value.b,
        )

    __rmul__ = __mul__


QPHI_ZERO = QPhi(Fraction(0), Fraction(0))
QPHI_ONE = QPhi(Fraction(1), Fraction(0))
PHI = QPhi(Fraction(0), Fraction(1))


def qphi_vector(vector):
    return [QPhi.coerce(value) for value in vector]


def source_firewall():
    path = Path(__file__)
    raw = path.read_bytes()
    require(raw.endswith(b"\n"), "source lacks final LF")
    require(b"\r" not in raw, "source is not LF-only")
    source = raw.decode("utf-8")
    tree = ast.parse(source)
    imports = set()
    calls = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            require(not isinstance(node.value, (float, complex)), "float or complex literal")
        elif isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split(".")[0])
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            calls.add(node.func.id)
    allowed = {"__future__", "ast", "dataclasses", "fractions", "pathlib"}
    forbidden_imports = {
        "cmath",
        "decimal",
        "math",
        "mpmath",
        "numpy",
        "os",
        "random",
        "requests",
        "secrets",
        "socket",
        "subprocess",
        "sympy",
        "time",
        "urllib",
    }
    forbidden_calls = {"compile", "complex", "eval", "exec", "float", "input", "open"}
    require(imports <= allowed, "unapproved import")
    require(not (imports & forbidden_imports), "forbidden import")
    require(not (calls & forbidden_calls), "forbidden dynamic or inexact call")
    return True


def main():
    print("PROBE " + PROBE)

    pullback = construct_pullback_matrix()
    expected_pullback = [
        [1, 0, 1, -1, 0, 1],
        [-1, 1, -1, 1, 0, -1],
        [0, -1, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0],
        [-1, 0, -1, 0, 1, 0],
        [1, 0, 0, 0, -1, 0],
    ]
    pf_matrix = pfaffian_quadratic_matrix()
    pf_covariance = matmul(
        transpose(pullback), matmul(pf_matrix, pullback)
    ) == pf_matrix
    gate(
        1,
        "pullback_and_pfaffian_covariance",
        determinant(M_J) == 1
        and pullback == expected_pullback
        and pf_covariance
        and pfaffian(OMEGA_1) == 1
        and pfaffian(matvec(pullback, OMEGA_1)) == 1,
    )

    characteristic = characteristic_polynomial(pullback)
    characteristic_expected = [1, -4, 5, -5, 5, -4, 1]
    product = poly_mul(Q_POLY, R_POLY)
    r_eisenstein = poly_compose(R_POLY, (-1, -1))
    gate(
        2,
        "characteristic_primary_factorization",
        characteristic == characteristic_expected
        and product == list(reversed(characteristic_expected))
        and 2 * 2 < 5 < 3 * 3
        and r_eisenstein == [5, 10, 10, 5, 1]
        and all(value % 5 == 0 for value in r_eisenstein[:-1])
        and r_eisenstein[0] % 25 != 0,
    )

    q_of_p = poly_matrix_eval(Q_POLY, pullback)
    r_of_p = poly_matrix_eval(R_POLY, pullback)
    full_basis = columns_matrix((OMEGA_1, OMEGA_2) + C_BASIS)
    order_ten = all(
        matvec(matpow(pullback, 10), vector) == list(vector)
        and matvec(matpow(pullback, 5), vector) == vector_scale(vector, -1)
        for vector in C_BASIS
    ) and all(
        any(matvec(matpow(pullback, exponent), vector) != list(vector) for vector in C_BASIS)
        for exponent in range(1, 10)
    )
    gate(
        3,
        "rational_primary_decomposition",
        is_zero_matrix(matmul(q_of_p, r_of_p))
        and matrix_rank(q_of_p) == 4
        and matrix_rank(r_of_p) == 2
        and determinant(full_basis) != 0
        and order_ten,
    )

    p_omega_1 = matvec(pullback, OMEGA_1)
    p_omega_2 = matvec(pullback, OMEGA_2)
    gate(
        4,
        "cm_pencil_identification",
        matvec(q_of_p, OMEGA_1) == [0] * 6
        and matvec(q_of_p, OMEGA_2) == [0] * 6
        and p_omega_1 == vector_add(OMEGA_1, vector_scale(OMEGA_2, -1))
        and p_omega_2 == vector_add(vector_scale(OMEGA_1, -1), vector_scale(OMEGA_2, 2))
        and matrix_rank(columns_matrix((OMEGA_1, OMEGA_2))) == 2,
    )

    h_constraints = [
        [0, 1, 1, 0, 0, 0],
        [-1, 0, 0, 1, 0, 0],
        [0, -1, 0, 0, 1, 0],
        [-1, 0, 0, 0, 0, 1],
    ]
    h_first_coordinates = [[OMEGA_1[0], OMEGA_2[0]], [OMEGA_1[1], OMEGA_2[1]]]
    gate(
        5,
        "hyperbolic_integral_saturation",
        canonical_rowspace(q_of_p) == canonical_rowspace(h_constraints)
        and determinant(h_first_coordinates) == 1,
    )

    c_constraints = [
        [1, 0, 1, 0, 0, 1],
        [0, 1, 0, 1, 1, 0],
    ]
    c_columns = columns_matrix(C_BASIS)
    c_parameter_block = [c_columns[row] for row in (2, 3, 4, 5)]
    gate(
        6,
        "circular_integral_saturation",
        canonical_rowspace(r_of_p) == canonical_rowspace(c_constraints)
        and matrix_rank(c_columns) == 4
        and determinant(c_parameter_block) == 1
        and all(matvec(c_constraints, vector) == [0, 0] for vector in C_BASIS)
        and determinant([[c_constraints[0][0], c_constraints[0][1]],
                         [c_constraints[1][0], c_constraints[1][1]]]) == 1,
    )

    ell = [2, 1, 2, 1, 1, 2]
    seam_annihilates = all(
        sum(ell[index] * vector[index] for index in range(6)) % 5 == 0
        for vector in (OMEGA_1, OMEGA_2) + C_BASIS
    )
    five_is_prime = all(5 % candidate != 0 for candidate in range(2, 5))
    gate(
        7,
        "index_five_cyclic_seam",
        determinant(full_basis) == 5
        and seam_annihilates
        and ell[1] == 1
        and five_is_prime,
    )

    ell_image = row_times_matrix(ell, pullback)
    gate(
        8,
        "seam_action_minus_one",
        all((image + source) % 5 == 0 for image, source in zip(ell_image, ell))
        and any((image - source) % 5 != 0 for image, source in zip(ell_image, ell)),
    )

    bezout = poly_add(
        poly_mul((8, -3), R_POLY),
        poly_mul((-3, 2, -2, 3), Q_POLY),
    )
    q_mod_five = [int(value) % 5 for value in Q_POLY]
    r_mod_five = [int(value) % 5 for value in R_POLY]
    gate(
        9,
        "resultant_and_ramification",
        bezout == [5]
        and resultant(Q_POLY, R_POLY) == 25
        and q_mod_five == [1, 2, 1]
        and r_mod_five == [1, 4, 1, 4, 1]
        and q_mod_five == [int(value) % 5 for value in poly_pow((1, 1), 2)]
        and r_mod_five == [int(value) % 5 for value in poly_pow((1, 1), 4)],
    )

    projector_numerator_poly = (8, -11, 11, -11, 11, -3)
    projector_numerator = poly_matrix_eval(projector_numerator_poly, pullback)
    projector = matscale(projector_numerator, Fraction(1, 5))
    expected_projector_numerator = [
        [2, 1, 2, 1, 1, 2],
        [-1, 2, -1, 2, 2, -1],
        [1, -2, 1, -2, -2, 1],
        [2, 1, 2, 1, 1, 2],
        [-1, 2, -1, 2, 2, -1],
        [2, 1, 2, 1, 1, 2],
    ]
    projector_from_bezout = matscale(
        matmul(matadd(matscale(identity(6), 8), matscale(pullback, -3)), r_of_p),
        Fraction(1, 5),
    )
    gate(
        10,
        "exact_primary_projector_denominator_five",
        projector_numerator == expected_projector_numerator
        and projector == projector_from_bezout
        and matmul(projector, projector) == projector
        and matmul(projector, pullback) == matmul(pullback, projector)
        and matvec(projector, OMEGA_1) == list(OMEGA_1)
        and matvec(projector, OMEGA_2) == list(OMEGA_2)
        and all(matvec(projector, vector) == [0] * 6 for vector in C_BASIS)
        and common_denominator(projector) == 5
        and integer_content(projector_numerator) == 1
        and matmul(projector_numerator, projector_numerator)
            == matscale(projector_numerator, 5)
        and matmul(projector_numerator, projector_numerator) != projector_numerator,
    )

    phi_inverse = PHI - QPHI_ONE
    phi_squared = PHI * PHI
    phi_inverse_squared = phi_inverse * phi_inverse
    omega_stable = vector_add(
        qphi_vector(OMEGA_1), vector_scale(qphi_vector(OMEGA_2), phi_inverse)
    )
    omega_unstable = vector_add(
        qphi_vector(OMEGA_1), vector_scale(qphi_vector(OMEGA_2), -PHI)
    )
    stable_image = matvec(pullback, omega_stable)
    unstable_image = matvec(pullback, omega_unstable)
    gate(
        11,
        "null_rank_two_real_eigenforms",
        phi_squared == QPhi(Fraction(1), Fraction(1))
        and phi_inverse_squared == QPhi(Fraction(2), Fraction(-1))
        and stable_image == vector_scale(omega_stable, phi_inverse_squared)
        and unstable_image == vector_scale(omega_unstable, phi_squared)
        and pfaffian(omega_stable) == QPHI_ZERO
        and pfaffian(omega_unstable) == QPHI_ZERO
        and omega_stable[0] == QPHI_ONE
        and omega_unstable[0] == QPHI_ONE
        and phi_squared.b != 0
        and phi_inverse_squared.b != 0
        and phi_squared * phi_squared != QPHI_ONE
        and phi_inverse_squared * phi_inverse_squared != QPHI_ONE,
    )

    left = (1, 0, 0, 0)
    right = (0, 1, 1, 0)
    period_before = form_value(OMEGA_1, left, right)
    period_after = form_value(p_omega_1, left, right)
    gate(
        12,
        "scope_and_exact_source_firewalls",
        period_before == 1
        and period_after == 0
        and p_omega_1 != list(OMEGA_1)
        and source_firewall(),
    )

    print("DECISION " + CONFIRMED)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
