#!/usr/bin/env python3
"""Exact audit for P-J-COINCIDENCE-RECORD-BOUNDARY-1.

Standard library only. Exact integer and Fraction arithmetic. No float,
builtin complex arithmetic, file input, network, subprocess, shell,
randomness, clock, dynamic import, eval, exec, or environment input.

Universal statements are proved in PREREG.md. This verifier audits their
finite exact premises and keeps the sole physical hypothesis visibly
UNTESTED and at STOP.
"""

from fractions import Fraction
from itertools import product


PROBE = "P-J-COINCIDENCE-RECORD-BOUNDARY-1"
CLAIM_A = "J-RESIDUAL-UNIT-NORMAL-FORM"
CLAIM_B = "J-COINCIDENCE-CARTESIAN-GRAM-SEAM"
HYPOTHESIS = "COINCIDENCE-RECORD-FREQUENCY"

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
# Exact finite linear algebra


def identity(size):
    require(size > 0, "identity size")
    return [
        [1 if row == column else 0 for column in range(size)]
        for row in range(size)
    ]


def transpose(matrix):
    require(matrix, "empty transpose")
    require(all(len(row) == len(matrix[0]) for row in matrix), "ragged transpose")
    return [list(column) for column in zip(*matrix)]


def matmul(left, right):
    require(left and right, "empty matrix product")
    require(len(left[0]) == len(right), "matrix product shape")
    require(all(len(row) == len(left[0]) for row in left), "ragged left matrix")
    require(all(len(row) == len(right[0]) for row in right), "ragged right matrix")
    return [
        [sum(a * b for a, b in zip(row, column)) for column in zip(*right)]
        for row in left
    ]


def matadd(left, right):
    require(len(left) == len(right), "matrix sum rows")
    require(all(len(a) == len(b) for a, b in zip(left, right)), "matrix sum columns")
    return [[a + b for a, b in zip(x, y)] for x, y in zip(left, right)]


def matscale(matrix, scalar):
    return [[scalar * value for value in row] for row in matrix]


def matpow(matrix, exponent):
    require(exponent >= 0, "negative matrix power")
    require(matrix and all(len(row) == len(matrix) for row in matrix), "matrix power shape")
    out = identity(len(matrix))
    factor = [list(row) for row in matrix]
    remaining = exponent
    while remaining:
        if remaining & 1:
            out = matmul(out, factor)
        factor = matmul(factor, factor)
        remaining >>= 1
    return out


def matvec(matrix, vector):
    require(all(len(row) == len(vector) for row in matrix), "matrix-vector shape")
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def quadratic_total(vector):
    return sum(value * value for value in vector)


def unit_total(vector):
    return sum(abs(value) for value in vector)


# ---------------------------------------------------------------------------
# Frozen residual-unit and coincidence constructors


def cell_units(vector, cell):
    require(len(vector) == 5, "unit vector size")
    require(0 <= cell < 5, "unit cell")
    require(all(isinstance(value, int) for value in vector), "nonintegral unit input")
    coefficient = vector[cell]
    if coefficient == 0:
        return []
    sign = 1 if coefficient > 0 else -1
    return [
        (cell, sign, ordinal)
        for ordinal in range(1, abs(coefficient) + 1)
    ]


def units(vector):
    return [unit for cell in range(5) for unit in cell_units(vector, cell)]


def tagged_fibre(vector, cell, tag):
    require(tag in {"S", "R"}, "unknown fibre tag")
    return [(tag, unit) for unit in cell_units(vector, cell)]


def complete_pairs(vector, cell):
    system = tagged_fibre(vector, cell, "S")
    record = tagged_fibre(vector, cell, "R")
    return [(left, right) for left in system for right in record]


def diagonal_pairs(vector, cell):
    system = tagged_fibre(vector, cell, "S")
    record = tagged_fibre(vector, cell, "R")
    return list(zip(system, record))


def gram_diagonal(vector):
    require(len(vector) == 5, "Gram vector size")
    coefficient_matrix = [
        [vector[row] if row == column else 0 for column in range(5)]
        for row in range(5)
    ]
    gram = matmul(transpose(coefficient_matrix), coefficient_matrix)
    return [gram[index][index] for index in range(5)], gram


def supported_centered(vector):
    require(len(vector) == 5, "supported vector size")
    return sum(vector) == 0 and all(
        (value - vector[0]) % 5 == 0 for value in vector
    )


# ---------------------------------------------------------------------------
# Frozen five-cell maps and complete audit carrier


I5 = identity(5)
N = [[1 for _ in range(5)] for _ in range(5)]
G = [[0 for _ in range(5)] for _ in range(5)]
for column in range(5):
    G[(column + 1) % 5][column] = 1

A = matadd(
    matadd(I5, matpow(G, 2)),
    matscale(matadd(matpow(G, 3), matpow(G, 4)), -1),
)
J = matadd(I5, matpow(G, 2))

D0 = [4, -1, -1, -1, -1]
H = [-1, 1, 0, 0, 0]
FIVE_H = [5 * value for value in H]

SAMPLE_STATES = [
    list(values)
    for values in product(range(-2, 3), repeat=5)
    if sum(values) == 0
]


# ---------------------------------------------------------------------------
# Sixteen exact gates


OUTPUT.append("SPEC J_COINCIDENCE_RECORD_BOUNDARY_EXACT_V1")
OUTPUT.append("MODE RESULT-EXPOSED PROOF-FIRST")

g01 = all(
    len(cell_units(vector, cell)) == abs(vector[cell])
    and all(unit[0] == cell for unit in cell_units(vector, cell))
    and all(
        unit[1] == (1 if vector[cell] > 0 else -1)
        for unit in cell_units(vector, cell)
    )
    for vector in SAMPLE_STATES
    for cell in range(5)
)
gate(
    "G01",
    "RESIDUAL_FIBRES",
    g01,
    "states=381 signed_ordinal=yes cardinality=absolute_value",
)

normal_form_unique = True
for coefficient in range(-6, 7):
    solutions = [
        (positive, negative)
        for positive in range(7)
        for negative in range(7)
        if positive * negative == 0 and positive - negative == coefficient
    ]
    normal_form_unique = normal_form_unique and solutions == [
        (max(coefficient, 0), max(-coefficient, 0))
    ]

reconstruction = all(
    sum(unit[1] for unit in cell_units(vector, cell)) == vector[cell]
    for vector in SAMPLE_STATES
    for cell in range(5)
)
g02 = normal_form_unique and reconstruction
gate("G02", "NORMAL_FORM", g02, "reduced_pair_unique=yes reconstruction=exact")

covariance = True
for vector in SAMPLE_STATES:
    rotated = matvec(G, vector)
    transported = {
        ((unit[0] + 1) % 5, unit[1], unit[2])
        for unit in units(vector)
    }
    covariance = covariance and transported == set(units(rotated))
g03 = covariance
gate(
    "G03",
    "CELL_COVARIANCE",
    g03,
    "five_cycle_transports_fibres=yes token_persistence=NONE",
)

positive_words = {"a", "b"}
negative_words = {"c"}
survivors = set()
for matched_positive in positive_words:
    survivors.add(tuple(sorted(positive_words - {matched_positive})))
g04 = (
    len(positive_words) - len(negative_words) == 1
    and survivors == {("a",), ("b",)}
)
gate(
    "G04",
    "CANCELLATION_AMBIGUITY",
    g04,
    "net=1 historical_survivor_choices=2 invariant=cardinality",
)

g05 = all(
    len(tagged_fibre(vector, cell, "S")) == abs(vector[cell])
    and len(tagged_fibre(vector, cell, "R")) == abs(vector[cell])
    and set(tagged_fibre(vector, cell, "S")).isdisjoint(
        tagged_fibre(vector, cell, "R")
    )
    for vector in SAMPLE_STATES
    for cell in range(5)
)
gate(
    "G05",
    "TAGGED_COPIES",
    g05,
    "system_record_disjoint=yes equal_marginal_size=absolute_value",
)

g06 = all(
    len(complete_pairs(vector, cell)) == vector[cell] * vector[cell]
    for vector in SAMPLE_STATES
    for cell in range(5)
)
gate(
    "G06",
    "CARTESIAN_CARDINALITY",
    g06,
    "complete_within_cell_pairs=d_k_squared",
)

g07 = all(
    all(
        pair[0][1][1] * pair[1][1][1] == 1
        for pair in complete_pairs(vector, cell)
    )
    for vector in SAMPLE_STATES
    for cell in range(5)
)
gate(
    "G07",
    "SIGN_SQUARE",
    g07,
    "nonzero_pair_sign=positive zero_fibre=empty",
)

gram_ok = True
for vector in SAMPLE_STATES:
    diagonal, gram = gram_diagonal(vector)
    counts = [len(complete_pairs(vector, cell)) for cell in range(5)]
    gram_ok = gram_ok and diagonal == counts
    gram_ok = gram_ok and all(
        gram[row][column] == 0
        for row in range(5)
        for column in range(5)
        if row != column
    )
g08 = gram_ok
gate(
    "G08",
    "GRAM_SEAM",
    g08,
    "cartesian_counts=diag_Kd_Gram cross_cells=zero",
)

AD0 = matvec(A, D0)
d0_counts = [len(complete_pairs(D0, cell)) for cell in range(5)]
ad0_counts = [len(complete_pairs(AD0, cell)) for cell in range(5)]
g09 = (
    AD0 == [5, 0, 5, -5, -5]
    and d0_counts == [16, 1, 1, 1, 1]
    and ad0_counts == [25, 0, 25, 25, 25]
    and sum(d0_counts) == 20
    and sum(ad0_counts) == 100
)
gate(
    "G09",
    "EXPOSED_WITNESSES",
    g09,
    "vertex=16,1,1,1,1 hole=25,0,25,25,25 totals=20,100",
)

g10 = all(
    (len(complete_pairs(vector, cell)) == 0) == (vector[cell] == 0)
    for vector in SAMPLE_STATES
    for cell in range(5)
)
gate(
    "G10",
    "COMBINATORIAL_DARKNESS",
    g10,
    "complete_pair_cell_empty_iff_d_k_zero",
)

finite_ratio_ok = True
for vector in SAMPLE_STATES:
    total = quadratic_total(vector)
    if total == 0:
        continue
    ratios = [
        Fraction(len(complete_pairs(vector, cell)), total)
        for cell in range(5)
    ]
    finite_ratio_ok = finite_ratio_ok and sum(ratios, Fraction(0)) == 1
    finite_ratio_ok = finite_ratio_ok and all(
        ratios[cell] == Fraction(vector[cell] * vector[cell], total)
        for cell in range(5)
    )
g11 = finite_ratio_ok
gate(
    "G11",
    "FINITE_RATIO",
    g11,
    "nonzero_complete_relation_normalizes_to_square_profile",
)

relation_nonselection = True
for size in range(1, 6):
    vector = [size, -size, 0, 0, 0]
    product_pairs = complete_pairs(vector, 0)
    diagonal = diagonal_pairs(vector, 0)
    attainable = {
        len(product_pairs[:count])
        for count in range(len(product_pairs) + 1)
    }
    relation_nonselection = (
        relation_nonselection
        and len(product_pairs) == size * size
        and len(diagonal) == size
        and attainable == set(range(size * size + 1))
    )

size_two = [2, -2, 0, 0, 0]
g12 = relation_nonselection and len(complete_pairs(size_two, 0)) != len(
    diagonal_pairs(size_two, 0)
)
gate(
    "G12",
    "RELATION_NONSELECTION",
    g12,
    "same_marginals_allow_counts_0_through_n_squared diagonal=n",
)

ata = matmul(transpose(A), A)
five_i_minus_n = matadd(matscale(I5, 5), matscale(N, -1))
g13 = ata == five_i_minus_n and all(
    quadratic_total(matvec(A, vector)) == 5 * quadratic_total(vector)
    for vector in SAMPLE_STATES
)
gate(
    "G13",
    "A_PAIR_EXTENSIVITY",
    g13,
    "A_star_A=5I-N pair_total_multiplier=5_on_V",
)

AH = matvec(A, H)
g14 = (
    AH == [-2, 1, -1, 2, 0]
    and supported_centered(D0)
    and supported_centered(FIVE_H)
    and (unit_total(D0), unit_total(AD0)) == (8, 20)
    and (unit_total(FIVE_H), unit_total(matvec(A, FIVE_H))) == (10, 30)
    and Fraction(unit_total(AD0), unit_total(D0)) == Fraction(5, 2)
    and Fraction(
        unit_total(matvec(A, FIVE_H)), unit_total(FIVE_H)
    ) == 3
)
gate(
    "G14",
    "SINGLE_UNIT_NONSELECTION",
    g14,
    "A_l1_ratios=5/2,3 no_state_independent_unit_yield",
)

raw = list(D0)
raw_totals = []
for _ in range(4):
    raw_totals.append(quadratic_total(raw))
    raw = matvec(J, raw)

five_is_not_square = all(candidate * candidate != 5 for candidate in range(-5, 6))
u5_integer_boundary = AD0 != [0, 0, 0, 0, 0] and five_is_not_square
g15 = raw_totals == [20, 30, 70, 180] and u5_integer_boundary
gate(
    "G15",
    "SCALE_FORK",
    g15,
    "raw_J_totals=20,30,70,180 U5_normalization_not_integer_count_map",
)

HYPOTHESIS_STATUS = "UNTESTED STOP"
SCOPE_LINE = (
    "SCOPE L1_only physical_records=NONE frequency_law=NONE probability=NONE "
    "self_location_fact=NONE single_run_randomness=NONE L2-L6=NONE"
)
g16 = (
    HYPOTHESIS == "COINCIDENCE-RECORD-FREQUENCY"
    and HYPOTHESIS_STATUS == "UNTESTED STOP"
    and "physical_records=NONE" in SCOPE_LINE
    and "frequency_law=NONE" in SCOPE_LINE
)
gate(
    "G16",
    "HYPOTHESIS_FIREWALL",
    g16,
    "physical_row=UNTESTED_STOP computation_cannot_confirm_H",
)


# ---------------------------------------------------------------------------
# Frozen decisions


CLAIM_A_GATES = {"G01", "G02", "G03", "G04", "G16"}
CLAIM_B_GATES = {
    "G05",
    "G06",
    "G07",
    "G08",
    "G09",
    "G10",
    "G11",
    "G12",
    "G13",
    "G14",
    "G15",
    "G16",
}
failed = set(FAILURES)
claim_a_status = "CONFIRMED" if not (failed & CLAIM_A_GATES) else "FIRED"
claim_b_status = "CONFIRMED" if not (failed & CLAIM_B_GATES) else "FIRED"

for line in OUTPUT:
    print(line)
print("RESULT CLAIM_A %s %s" % (CLAIM_A, claim_a_status))
print("RESULT CLAIM_B %s %s" % (CLAIM_B, claim_b_status))
print("HYPOTHESIS %s %s" % (HYPOTHESIS, HYPOTHESIS_STATUS))
print(SCOPE_LINE)
overall = (
    "PASS"
    if claim_a_status == claim_b_status == "CONFIRMED"
    else "SCIENTIFIC-FIRED"
)
print("RESULT OVERALL %s gates=16 claims=2 hypothesis=1" % overall)
