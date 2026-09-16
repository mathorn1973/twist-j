#!/usr/bin/env python3
"""Exact standalone audit of passive quadratic prediction and calibration."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations, product
import sys


PAIRS = tuple((i, j) for i in range(4) for j in range(i, 4))
GRID = tuple(product(range(-2, 3), repeat=4))
U = (1, 1, 1, 1)
CHI = (1, -1, -1, 1)
SOURCE_SITES = ((0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1), (2, 0, 0))
PORTS = SOURCE_SITES[1:] + ((-1, -1, 0), (-1, 0, -1), (-1, 0, 1))
ORIGIN = (0, 0, 0)
INTEGER_H = (
    (-354, 1416, -354, -354),
    (-354, -354, 1416, -354),
    (-348, -348, -348, 1422),
    (-368, -343, -343, -373),
    (8, 53, -22, -22),
    (8, -22, 53, -22),
    (16, -14, -9, 16),
)
INTEGER_H_ORIGIN = (1421, -349, -349, -349)
COEFFICIENTS = tuple(map(F, (
    "-6480865109/82312993800", "6549292699/49387796280",
    "6551015617/49387796280", "-111027113/111030330",
    "-111027113/111030330", "-9409883/9409350", "1556538/1568225",
    "-11092/313645", "-11092/313645", "0",
)))
EXPECTED_DETERMINANT = -176542678173169038600000000000000000
ATOM_ERROR_GAIN = F(84944136907, 246938981400)
DEPOSIT_ERROR_GAIN = F(751911453, 185050550)
COMMON_ERROR_GAIN = F(64211196595109, 14569399902600)


def dot(left, right):
    return sum((a * b for a, b in zip(left, right)), F(0))


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def scale(factor, vector):
    return tuple(factor * a for a in vector)


def monomials(z):
    return tuple(z[i] * z[j] for i, j in PAIRS)


def square_row(vector):
    return tuple(vector[i] * vector[j] * (1 if i == j else 2) for i, j in PAIRS)


ATOM_ROWS_20 = (
    square_row(U),
    scale(5, square_row(CHI)),
    scale(10, add(square_row((1, 0, 0, -1)), square_row((0, 1, -1, 0)))),
)
ATOM_ROWS = tuple(scale(F(1, 20), row) for row in ATOM_ROWS_20)


def atoms(z):
    return (F(sum(z) ** 2, 20), F(dot(CHI, z) ** 2, 4),
            F((z[0] - z[3]) ** 2 + (z[1] - z[2]) ** 2, 2))


def passive_record(z):
    weights = atoms(z)
    total = sum(weights)
    if total == 0:
        return ("PI-ATOMS", "ZERO_SUPPORT", F(0), weights, "ZERO_DENOMINATOR")
    return ("PI-ATOMS", "SUPPORTED", total, weights,
            ("NORMALIZED", tuple(w / total for w in weights)))


def rref(rows, columns=None):
    matrix = [list(map(F, row)) for row in rows]
    if not matrix:
        return matrix, ()
    width = len(matrix[0]) if columns is None else columns
    pivot_row = 0
    pivots = []
    for col in range(width):
        found = next((i for i in range(pivot_row, len(matrix)) if matrix[i][col]), None)
        if found is None:
            continue
        matrix[pivot_row], matrix[found] = matrix[found], matrix[pivot_row]
        divisor = matrix[pivot_row][col]
        matrix[pivot_row] = [x / divisor for x in matrix[pivot_row]]
        for i in range(len(matrix)):
            if i != pivot_row and matrix[i][col]:
                factor = matrix[i][col]
                matrix[i] = [x - factor * y for x, y in zip(matrix[i], matrix[pivot_row])]
        pivots.append(col)
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return matrix, tuple(pivots)


def rank(rows):
    return len(rref(rows)[1])


def bareiss_determinant(rows):
    """Integer fraction-free elimination, independent of rational RREF."""
    matrix = [list(row) for row in rows]
    previous = 1
    sign = 1
    for k in range(len(matrix) - 1):
        if matrix[k][k] == 0:
            found = next((i for i in range(k + 1, len(matrix)) if matrix[i][k]), None)
            if found is None:
                return 0
            matrix[k], matrix[found] = matrix[found], matrix[k]
            sign = -sign
        pivot = matrix[k][k]
        for i in range(k + 1, len(matrix)):
            for j in range(k + 1, len(matrix)):
                numerator = matrix[i][j] * pivot - matrix[i][k] * matrix[k][j]
                assert numerator % previous == 0
                matrix[i][j] = numerator // previous
            matrix[i][k] = 0
        previous = pivot
    return sign * matrix[-1][-1]


def solve_row_basis(rows, target):
    n = len(rows)
    augmented = [[rows[j][i] for j in range(n)] + [target[i]] for i in range(n)]
    reduced, pivots = rref(augmented, n)
    assert pivots == tuple(range(n))
    return tuple(row[-1] for row in reduced)


def stencil_by_norm():
    weights = {2: 6, 4: 1, 8: 15, 10: 1, 16: 1}
    return {d: F(weights[sum(x * x for x in d)], 324)
            for d in product(range(-4, 5), repeat=3)
            if sum(d) % 2 == 0 and sum(x * x for x in d) in weights}


def stencil_by_orbits():
    result = {}
    shells = (((1, 1, 0), 6), ((2, 0, 0), 1), ((2, 2, 0), 15),
              ((3, 1, 0), 1), ((4, 0, 0), 1))
    for shell, weight in shells:
        for ordering in permutations(shell):
            for signs in product((-1, 1), repeat=3):
                displacement = tuple(a * b for a, b in zip(ordering, signs))
                result[displacement] = F(weight, 324)
    return result


def spatial_response(site, stencil):
    response = [F(0)] * 4
    for j, source_site in enumerate(SOURCE_SITES):
        displacement = tuple(a - b for a, b in zip(source_site, site))
        kernel = F(10, 9) if site == source_site else stencil.get(displacement, F(0))
        for i in range(4):
            response[i] += kernel * (F(j == i) - F(1, 5))
    return tuple(response)


def direct_first_cold_step(z, ports, stencil):
    """Independent field-level preparation and full Laplacian step; gamma=1."""
    source = {site: F((z + (0,))[i]) - F(sum(z), 5)
              for i, site in enumerate(SOURCE_SITES)}
    support = set(source)
    for site in source:
        support.update(add(site, d) for d in stencil)
    free_next = {}
    for site in support:
        value = source.get(site, F(0))
        laplacian = sum((weight * (value - source.get(add(site, d), F(0)))
                         for d, weight in stencil.items()), F(0))
        free_next[site] = 2 * value - laplacian
    outgoing = {site: -(free_next.get(site, F(0)) / F(3, 2)) / 2 for site in ports}
    return outgoing, {site: value * value for site, value in outgoing.items()}


def calibration_rows():
    return ATOM_ROWS + tuple(scale(F(1, 23619600), square_row(row)) for row in INTEGER_H)


def gate_01_factorization():
    assert rank(ATOM_ROWS) == 3
    basis = tuple(tuple(int(i == j) for i in range(4)) for j in range(4))
    assert len({passive_record(e) for e in basis}) == 1
    assert passive_record(add(basis[0], basis[3])) == passive_record(add(basis[1], basis[2]))
    cross_pairs = ((0, 1), (0, 2), (1, 3), (2, 3))
    assert len({passive_record(add(basis[i], basis[j])) for i, j in cross_pairs}) == 1
    # Symbolic d,a,b basis checks certify the displayed coefficient formula.
    for d, a, b in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        alpha, beta, gamma = 5 * (d + a + 2 * b), d + a - 2 * b, d - a
        reconstructed = tuple(alpha * tr + beta * lr + gamma * rr
                              for tr, lr, rr in zip(*ATOM_ROWS))
        expected = tuple((d if i == j else a if (i, j) in ((0, 3), (1, 2)) else b)
                         * (1 if i == j else 2) for i, j in PAIRS)
        assert reconstructed == expected


def gate_02_ensemble_dimension():
    groups = defaultdict(list)
    for z in GRID:
        record = passive_record(z)
        assert atoms(z) == tuple(dot(row, monomials(z)) for row in ATOM_ROWS)
        assert record[2] == dot(z, z) - F(sum(z) ** 2, 5)
        assert (record[1] == "ZERO_SUPPORT") == (z == (0, 0, 0, 0))
        groups[record].append(z)
    constraints = []
    for members in groups.values():
        reference = monomials(members[0])
        constraints.extend(add(monomials(z), scale(-1, reference)) for z in members[1:])
    assert rank(constraints) == 7
    assert all(dot(c, row) == 0 for c in constraints for row in ATOM_ROWS)
    assert rank([monomials(z) for z in GRID]) == 10
    assert rank([(1,) + monomials(z) for z in GRID]) == 11


def gate_03_spatial_derivation():
    stencil = stencil_by_norm()
    assert stencil == stencil_by_orbits()
    assert len(stencil) == 60 and sum(stencil.values()) == F(8, 9)
    assert tuple(sum(sum(v * v for v in d) == n for d in stencil)
                 for n in (2, 4, 8, 10, 16)) == (12, 6, 12, 24, 6)
    sites = PORTS + (ORIGIN,)
    expected_rows = INTEGER_H + (INTEGER_H_ORIGIN,)
    for site, integer_row in zip(sites, expected_rows):
        assert spatial_response(site, stencil) == scale(F(1, 1620), integer_row)
    for j in range(4):
        z = tuple(int(i == j) for i in range(4))
        outgoing, deposits = direct_first_cold_step(z, sites, stencil_by_orbits())
        for site, integer_row in zip(sites, expected_rows):
            expected = F(-integer_row[j], 4860)
            assert outgoing[site] == expected and deposits[site] == expected * expected


def gate_04_calibration_basis():
    integer_rows = ATOM_ROWS_20 + tuple(square_row(row) for row in INTEGER_H)
    assert len(set(PORTS)) == 7 and ORIGIN not in PORTS
    assert bareiss_determinant(integer_rows) == EXPECTED_DETERMINANT
    assert rank(calibration_rows()) == 10


def gate_05_held_out_identity():
    rows = calibration_rows()
    target = scale(F(1, 23619600), square_row(INTEGER_H_ORIGIN))
    assert solve_row_basis(rows, target) == COEFFICIENTS
    for j in range(10):
        assert sum(c * row[j] for c, row in zip(COEFFICIENTS, rows)) == target[j]
    for z in GRID:
        inputs = atoms(z) + tuple(F(dot(row, z) ** 2, 23619600) for row in INTEGER_H)
        assert dot(COEFFICIENTS, inputs) == F(dot(INTEGER_H_ORIGIN, z) ** 2, 23619600)


def gate_06_error_certificate():
    assert sum(abs(c) for c in COEFFICIENTS[:3]) == ATOM_ERROR_GAIN
    assert sum(abs(c) for c in COEFFICIENTS[3:]) == DEPOSIT_ERROR_GAIN
    assert ATOM_ERROR_GAIN + DEPOSIT_ERROR_GAIN == COMMON_ERROR_GAIN
    signs = tuple(1 if c >= 0 else -1 for c in COEFFICIENTS)
    assert dot(COEFFICIENTS, signs) == COMMON_ERROR_GAIN
    for atom_radius, deposit_radius in ((F(0), F(1)), (F(1), F(0)), (F(2, 3), F(3, 7))):
        errors = tuple(sign * (atom_radius if i < 3 else deposit_radius)
                       for i, sign in enumerate(signs))
        assert dot(COEFFICIENTS, errors) == (ATOM_ERROR_GAIN * atom_radius
                                            + DEPOSIT_ERROR_GAIN * deposit_radius)


def gate_07_source_distinction():
    e0, e1 = (1, 0, 0, 0), (0, 1, 0, 0)
    record = passive_record(e0)
    assert record == passive_record(e1)
    assert record == ("PI-ATOMS", "SUPPORTED", F(4, 5),
                      (F(1, 20), F(1, 4), F(1, 2)),
                      ("NORMALIZED", (F(1, 16), F(5, 16), F(5, 8))))
    deposits = tuple(F(dot(INTEGER_H_ORIGIN, z) ** 2, 23619600) for z in (e0, e1))
    assert deposits == (F(2019241, 23619600), F(121801, 23619600))
    assert tuple(value // F(1, 16) for value in deposits) == (1, 0)


GATES = (
    ("G01_FACTORABLE_QUADRATICS", gate_01_factorization),
    ("G02_FULL_PASSIVE_LAW_DIMENSION", gate_02_ensemble_dimension),
    ("G03_INDEPENDENT_SPATIAL_RESPONSE", gate_03_spatial_derivation),
    ("G04_SEVEN_PORT_BASIS", gate_04_calibration_basis),
    ("G05_HELD_OUT_IDENTITY", gate_05_held_out_identity),
    ("G06_ADDITIVE_ERROR_CERTIFICATE", gate_06_error_certificate),
    ("G07_FINEST_RECORD_COLLISION", gate_07_source_distinction),
)


def main():
    if not __debug__:
        raise RuntimeError("STOP_INTEGRITY: non-optimized Python is required")
    sys.stdout.reconfigure(newline="\n")
    outcomes = []
    for name, check in GATES:
        try:
            check()
            outcomes.append((name, True))
        except AssertionError:
            outcomes.append((name, False))
    passed = all(value for _, value in outcomes)
    print("PROBE P-QDD-PASSIVE-QUADRATIC-CALIBRATION-1")
    print("MODE EXACT CONDITIONAL L1")
    for name, value in outcomes:
        print("CHECK", name, "PASS" if value else "FIRED")
    print("CLAIM QDD-PASSIVE-QUADRATIC-CALIBRATION", "CONFIRMED" if passed else "FIRED")
    print("PHYSICAL_PREPARATION_APPARATUS_OCCURRENCE UNRESOLVED")
    print("TERMINAL", "CONFIRMED" if passed else "SCIENTIFIC-FIRED")


if __name__ == "__main__":
    main()
