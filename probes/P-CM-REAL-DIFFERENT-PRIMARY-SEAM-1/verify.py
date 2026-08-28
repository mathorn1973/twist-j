#!/usr/bin/env python3
"""Exact audit for P-CM-REAL-DIFFERENT-PRIMARY-SEAM-1.

The written proof in PREREG.md carries the universal theorem. This verifier
uses exact integer, Fraction, matrix, polynomial, and Z[beta] arithmetic only,
with beta^2=1-beta. Standard library only; no numerical approximation, search,
network, subprocess, clock, or external probe import.
"""

from __future__ import annotations

import ast
from fractions import Fraction
from pathlib import Path


PROBE = "P-CM-REAL-DIFFERENT-PRIMARY-SEAM-1"
DECISION = "CM-REAL-DIFFERENT-PRIMARY-SEAM-CONFIRMED"
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


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def zero_matrix(rows, columns):
    return [
        [Fraction(0) for _ in range(columns)]
        for _ in range(rows)
    ]


def identity(size):
    out = zero_matrix(size, size)
    for index in range(size):
        out[index][index] = Fraction(1)
    return out


def matmul(left, right):
    require(left and right, "empty matrix product")
    require(len(left[0]) == len(right), "matrix product shape")
    require(
        all(len(row) == len(left[0]) for row in left),
        "ragged left matrix",
    )
    require(
        all(len(row) == len(right[0]) for row in right),
        "ragged right matrix",
    )
    out = []
    for row in left:
        out_row = []
        for column in zip(*right):
            total = Fraction(0)
            for left_value, right_value in zip(row, column):
                total += left_value * right_value
            out_row.append(total)
        out.append(out_row)
    return out


def matadd(left, right):
    require(len(left) == len(right), "matrix sum rows")
    require(
        all(len(a) == len(b) for a, b in zip(left, right)),
        "matrix sum columns",
    )
    return [
        [a + b for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]


def matscale(matrix, scalar):
    return [
        [Fraction(scalar) * value for value in row]
        for row in matrix
    ]


def matvec(matrix, vector):
    require(
        all(len(row) == len(vector) for row in matrix),
        "matrix-vector shape",
    )
    return [
        sum(
            (coefficient * value
             for coefficient, value in zip(row, vector)),
            Fraction(0),
        )
        for row in matrix
    ]


def columns_matrix(columns):
    require(columns, "empty column family")
    height = len(columns[0])
    require(
        all(len(column) == height for column in columns),
        "column shape",
    )
    return [
        [columns[column][row] for column in range(len(columns))]
        for row in range(height)
    ]


def determinant(matrix):
    size = len(matrix)
    require(
        size > 0 and all(len(row) == size for row in matrix),
        "determinant shape",
    )
    work = [
        [Fraction(value) for value in row]
        for row in matrix
    ]
    value = Fraction(1)
    for column in range(size):
        pivot = next(
            (
                row
                for row in range(column, size)
                if work[row][column] != 0
            ),
            None,
        )
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


def common_denominator(matrix):
    value = 1
    for row in matrix:
        for entry in row:
            denominator = Fraction(entry).denominator
            left = value
            right = denominator
            while right:
                left, right = right, left % right
            value = value * denominator // left
    return value


def poly_matrix_eval(poly, matrix):
    size = len(matrix)
    result = zero_matrix(size, size)
    unit = identity(size)
    for coefficient in reversed(poly):
        result = matadd(
            matmul(result, matrix),
            matscale(unit, coefficient),
        )
    return result


def poly_add(left, right):
    out = [Fraction(0) for _ in range(max(len(left), len(right)))]
    for index, value in enumerate(left):
        out[index] += Fraction(value)
    for index, value in enumerate(right):
        out[index] += Fraction(value)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_mul(left, right):
    out = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            out[left_index + right_index] += (
                Fraction(left_value) * Fraction(right_value)
            )
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def resultant(left, right):
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
    out = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    for value, (row, column) in zip(coordinates, PAIRS):
        out[row][column] = value
        out[column][row] = -value
    return out


def alt_coordinates(matrix):
    return [
        matrix[row][column]
        for row, column in PAIRS
    ]


def pullback_coordinates(coordinates):
    form = alt_matrix(coordinates)
    return alt_coordinates(
        matmul(transpose(M_J), matmul(form, M_J))
    )


def construct_pullback_matrix():
    columns = []
    for index in range(6):
        basis = [Fraction(0) for _ in range(6)]
        basis[index] = Fraction(1)
        columns.append(pullback_coordinates(basis))
    return columns_matrix(columns)


def vector_add(left, right):
    require(len(left) == len(right), "vector sum shape")
    return [a + b for a, b in zip(left, right)]


def vector_scale(vector, scalar):
    return [Fraction(scalar) * value for value in vector]


def linear_combination(coefficients, vectors):
    require(len(coefficients) == len(vectors), "linear combination shape")
    result = [Fraction(0) for _ in vectors[0]]
    for coefficient, vector in zip(coefficients, vectors):
        result = vector_add(result, vector_scale(vector, coefficient))
    return result


def row_times_matrix(row, matrix):
    require(len(row) == len(matrix), "row-matrix shape")
    return [
        sum(
            (row[index] * matrix[index][column]
             for index in range(len(row))),
            Fraction(0),
        )
        for column in range(len(matrix[0]))
    ]


def h_coordinates(vector):
    require(len(vector) == 6, "H-coordinate shape")
    a = vector[0]
    b = vector[1]
    require(
        list(vector) == [a, b, -b, a, b, a],
        "vector is not in displayed H",
    )
    return (Fraction(a), Fraction(b))


def ab_sums(vector):
    require(len(vector) == 6, "A/B sum shape")
    return (
        vector[0] + vector[2] + vector[5],
        vector[1] + vector[3] + vector[4],
    )


def o_pair(a, b=0):
    return (Fraction(a), Fraction(b))


def o_add(left, right):
    return (left[0] + right[0], left[1] + right[1])


def o_neg(value):
    return (-value[0], -value[1])


def o_sub(left, right):
    return o_add(left, o_neg(right))


def o_scale(value, scalar):
    return (
        Fraction(scalar) * value[0],
        Fraction(scalar) * value[1],
    )


def o_mul(left, right):
    # beta^2 = 1-beta
    a, b = left
    c, d = right
    return (
        a * c + b * d,
        a * d + b * c - b * d,
    )


def o_trace(value):
    # conjugate beta has trace -1
    return 2 * value[0] - value[1]


def o_trace_pair(left, right):
    return o_trace(o_mul(left, right))


def o_mult_matrix(value):
    a, b = value
    return [
        [a, b],
        [b, a - b],
    ]


def o_residue(value):
    a, b = value
    require(
        a.denominator == 1 and b.denominator == 1,
        "residue of nonintegral O element",
    )
    return (a.numerator + 2 * b.numerator) % 5


def mod_pair(value):
    a, b = value
    require(
        Fraction(a).denominator == 1
        and Fraction(b).denominator == 1,
        "mod pair of nonintegral element",
    )
    return (
        Fraction(a).numerator % 5,
        Fraction(b).numerator % 5,
    )


def source_scope_firewall():
    path = Path(__file__)
    raw = path.read_bytes()
    require(raw.endswith(b"\n"), "source lacks final LF")
    require(b"\r" not in raw, "source is not LF-only")

    tree = ast.parse(raw.decode("utf-8"))
    imports = set()
    calls = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            require(
                not isinstance(node.value, (float, complex)),
                "float or complex literal",
            )
        elif isinstance(node, ast.Import):
            imports.update(
                alias.name.split(".")[0]
                for alias in node.names
            )
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split(".")[0])
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            calls.add(node.func.id)

    allowed = {"__future__", "ast", "fractions", "pathlib"}
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
    forbidden_calls = {
        "compile",
        "complex",
        "eval",
        "exec",
        "float",
        "input",
        "open",
    }
    require(imports <= allowed, "unapproved import")
    require(not (imports & forbidden_imports), "forbidden import")
    require(not (calls & forbidden_calls), "forbidden call")

    prereg = (path.parent / "PREREG.md").read_text(encoding="utf-8")
    required = (
        "Status: preregistered protocol only. Formal execution count: zero.",
        "RESULT-EXPOSED, proof-first",
        "ACTION_LAYER:   L1",
        "P-CM-REAL-DIFFERENT-PRIMARY-SEAM-1",
        "CM-REAL-DIFFERENT-PRIMARY-SEAM",
        "e_H(E_Z)=d_F^-1 H_Z",
        "d_F=(q'(u))=(delta)=(s_J^2)",
        "O/(s_J^2)",
        "not a discriminant-form isometry claim",
        "Neither `d_F^-1/O` nor `Q_seam` is asserted to be a ring.",
        "No Canon fold",
    )
    return all(item in prereg for item in required)


def main():
    print("PROBE " + PROBE)

    gate(1, "source_scope_firewall", source_scope_firewall())

    pullback = construct_pullback_matrix()
    expected_pullback = [
        [1, 0, 1, -1, 0, 1],
        [-1, 1, -1, 1, 0, -1],
        [0, -1, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0],
        [-1, 0, -1, 0, 1, 0],
        [1, 0, 0, 0, -1, 0],
    ]

    r_of_p = poly_matrix_eval(R_POLY, pullback)
    q_of_p = poly_matrix_eval(Q_POLY, pullback)
    projector_numerator = matmul(
        matadd(
            matscale(identity(6), 8),
            matscale(pullback, -3),
        ),
        r_of_p,
    )
    projector = matscale(projector_numerator, Fraction(1, 5))
    expected_projector_numerator = [
        [2, 1, 2, 1, 1, 2],
        [-1, 2, -1, 2, 2, -1],
        [1, -2, 1, -2, -2, 1],
        [2, 1, 2, 1, 1, 2],
        [-1, 2, -1, 2, 2, -1],
        [2, 1, 2, 1, 1, 2],
    ]

    h_action = columns_matrix(
        (
            h_coordinates(matvec(pullback, OMEGA_1)),
            h_coordinates(matvec(pullback, OMEGA_2)),
        )
    )
    gate(
        2,
        "public_pullback_and_primary_projector",
        determinant(M_J) == 1
        and pullback == expected_pullback
        and projector_numerator == expected_projector_numerator
        and matmul(projector, projector) == projector
        and matmul(projector, pullback) == matmul(pullback, projector)
        and matvec(projector, OMEGA_1) == list(OMEGA_1)
        and matvec(projector, OMEGA_2) == list(OMEGA_2)
        and all(
            matvec(projector, vector) == [0] * 6
            for vector in C_BASIS
        )
        and common_denominator(projector) == 5
        and h_action == [[1, -1], [-1, 2]],
    )

    one = o_pair(1)
    beta = o_pair(0, 1)
    phi = o_pair(1, 1)
    u = o_mul(beta, beta)
    q_at_u = o_add(
        o_sub(o_mul(u, u), o_scale(u, 3)),
        one,
    )
    gate(
        3,
        "real_quadratic_order_and_unit_action",
        o_add(o_mul(beta, beta), o_sub(beta, one)) == o_pair(0)
        and u == o_pair(1, -1)
        and o_sub(one, u) == beta
        and q_at_u == o_pair(0)
        and o_mul(beta, phi) == one
        and o_mult_matrix(u) == [[1, -1], [-1, 2]]
        and h_action == o_mult_matrix(u),
    )

    delta = o_pair(1, 2)
    q_prime_at_u = o_sub(o_scale(u, 2), o_pair(3))
    trace_gram = [
        [o_trace_pair(one, one), o_trace_pair(one, beta)],
        [o_trace_pair(beta, one), o_trace_pair(beta, beta)],
    ]

    codiff_1 = o_scale(delta, Fraction(1, 5))
    codiff_2 = o_scale(o_mul(delta, beta), Fraction(1, 5))
    dual_1 = o_add(codiff_1, codiff_2)
    dual_2 = codiff_1

    trace_dual = (
        o_trace_pair(dual_1, one) == 1
        and o_trace_pair(dual_1, beta) == 0
        and o_trace_pair(dual_2, one) == 0
        and o_trace_pair(dual_2, beta) == 1
    )
    gate(
        4,
        "different_and_codifferent",
        q_prime_at_u == o_neg(delta)
        and trace_gram == [[2, -1], [-1, 3]]
        and determinant(trace_gram) == 5
        and determinant(o_mult_matrix(delta)) == -5
        and o_mul(delta, delta) == o_pair(5)
        and dual_1 == o_pair(Fraction(3, 5), Fraction(1, 5))
        and dual_2 == o_pair(Fraction(1, 5), Fraction(2, 5))
        and trace_dual,
    )

    s_j_squared = o_sub(o_pair(3), phi)
    gate(
        5,
        "ramified_chord_generates_different",
        s_j_squared == o_pair(2, -1)
        and s_j_squared == o_mul(delta, beta)
        and s_j_squared == o_add(u, one)
        and o_mul(beta, phi) == one
        and abs(determinant(o_mult_matrix(s_j_squared))) == 5
        and abs(determinant(o_mult_matrix(delta))) == 5,
    )

    projected_coordinates = []
    delta_projected = []
    formula_ok = True
    for index in range(6):
        basis = [Fraction(0) for _ in range(6)]
        basis[index] = Fraction(1)
        projection = matvec(projector, basis)
        coordinates = h_coordinates(projection)
        projected_coordinates.append(coordinates)

        a_sum, b_sum = ab_sums(basis)
        expected_coordinates = (
            Fraction(2 * a_sum + b_sum, 5),
            Fraction(-a_sum + 2 * b_sum, 5),
        )
        formula_ok = formula_ok and coordinates == expected_coordinates

        delta_image = o_mul(delta, coordinates)
        delta_projected.append(delta_image)
        formula_ok = formula_ok and delta_image == o_pair(b_sum, a_sum)

    expected_delta_projected = [
        beta,
        one,
        beta,
        one,
        one,
        beta,
    ]
    gate(
        6,
        "projector_image_equals_codifferent_lattice",
        formula_ok
        and delta_projected == expected_delta_projected
        and set(delta_projected) == {one, beta}
        and projected_coordinates[0]
            == o_pair(Fraction(2, 5), Fraction(-1, 5))
        and projected_coordinates[1]
            == o_pair(Fraction(1, 5), Fraction(2, 5)),
    )

    full_basis = columns_matrix(
        (OMEGA_1, OMEGA_2) + C_BASIS
    )
    h_0 = linear_combination((1, 2), (OMEGA_1, OMEGA_2))
    c_0 = linear_combination((3, 1, 2, 1), C_BASIS)
    glue = [
        Fraction(h_value - c_value, 5)
        for h_value, c_value in zip(h_0, c_0)
    ]
    complement_projector = matadd(
        identity(6),
        matscale(projector, -1),
    )
    ell = [2, 1, 2, 1, 1, 2]
    q_seam_image = row_times_matrix(ell, q_of_p)
    gate(
        7,
        "canonical_seam_exact_sequence",
        abs(determinant(full_basis)) == 5
        and h_0 == [1, 2, -2, 1, 2, 1]
        and c_0 == [-4, -3, 3, 1, 2, 1]
        and glue == [1, 1, -1, 0, 0, 0]
        and matvec(projector, glue)
            == vector_scale(h_0, Fraction(1, 5))
        and matvec(complement_projector, glue)
            == vector_scale(c_0, Fraction(-1, 5))
        and all(value % 5 == 0 for value in q_seam_image)
        and matvec(q_of_p, C_BASIS[0]) != [0] * 6,
    )

    residue_coefficients = [
        o_residue(value)
        for value in delta_projected
    ]
    seam_basis = (OMEGA_1, OMEGA_2) + C_BASIS
    ell_annihilates_source_sum = all(
        sum(
            (ell[index] * vector[index] for index in range(6)),
            0,
        ) % 5 == 0
        for vector in seam_basis
    )
    ell_on_glue = sum(
        (ell[index] * glue[index] for index in range(6)),
        Fraction(0),
    )
    gate(
        8,
        "seam_residue_functional",
        residue_coefficients == ell
        and ell_annihilates_source_sum
        and ell_on_glue == 1
        and ell[1] == 1,
    )

    ell_image = row_times_matrix(ell, pullback)
    classes_mod_five = {
        (a, b)
        for a in range(5)
        for b in range(5)
    }
    delta_image_mod_five = {
        mod_pair(o_mul(delta, o_pair(a, b)))
        for a, b in classes_mod_five
    }
    residue_kernel_mod_five = {
        (a, b)
        for a, b in classes_mod_five
        if o_residue(o_pair(a, b)) == 0
    }
    gate(
        9,
        "annihilator_and_minus_one_action",
        all(
            (image + source) % 5 == 0
            for image, source in zip(ell_image, ell)
        )
        and any(
            (image - source) % 5 != 0
            for image, source in zip(ell_image, ell)
        )
        and o_residue(u) == 4
        and o_residue(s_j_squared) == 0
        and delta_image_mod_five == residue_kernel_mod_five
        and len(residue_kernel_mod_five) == 5,
    )

    delta_mod_five = mod_pair(delta)
    delta_square_mod_five = mod_pair(o_mul(delta, delta))
    residue_values = {
        o_residue(o_pair(a, b))
        for a, b in classes_mod_five
    }
    gate(
        10,
        "resultant_nilpotent_layer_guard",
        resultant(Q_POLY, R_POLY) == 25
        and poly_add(
            poly_mul((1, 2, 1), Q_POLY),
            (0, 0, 5),
        ) == list(R_POLY)
        and o_mul(delta, delta) == o_pair(5)
        and len(classes_mod_five) == 25
        and delta_mod_five != (0, 0)
        and delta_square_mod_five == (0, 0)
        and len(delta_image_mod_five) == 5
        and residue_values == {0, 1, 2, 3, 4}
        and all((value * value) % 5 != 0 for value in range(1, 5)),
    )

    alternate_coordinate = [
        (2 * value) % 5
        for value in ell
    ]
    chord_coordinate = [
        o_residue(o_mul(beta, value))
        for value in delta_projected
    ]
    gate(
        11,
        "scope_and_trivialization_guard",
        alternate_coordinate != ell
        and chord_coordinate == alternate_coordinate
        and all(
            alternate_coordinate[index] == (2 * ell[index]) % 5
            for index in range(6)
        )
        and matvec(pullback, OMEGA_1) != list(OMEGA_1)
        and common_denominator(projector) == 5
        and source_scope_firewall(),
    )

    print("DECISION " + DECISION)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
