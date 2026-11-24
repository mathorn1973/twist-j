#!/usr/bin/env python3
"""Exact developer verification of the frozen non-canonical round 10 audit."""

from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product


TRIPLES = (
    (2, 2, 3),
    (2, 2, 5),
    (3, 2, 3),
    (3, 2, 5),
    (2, 3, 4),
    (2, 3, 6),
    (3, 3, 4),
)


def identity(size):
    return tuple(tuple(int(row == col) for col in range(size)) for row in range(size))


def multiply(left, right):
    columns = tuple(zip(*right))
    return tuple(
        tuple(sum(a * b for a, b in zip(row, col)) for col in columns)
        for row in left
    )


def scale(matrix, scalar):
    return tuple(tuple(scalar * entry for entry in row) for row in matrix)


def inverse_and_determinant(matrix):
    size = len(matrix)
    rows = [
        [Fraction(entry) for entry in row + unit_row]
        for row, unit_row in zip(matrix, identity(size))
    ]
    determinant = Fraction(1)
    for col in range(size):
        pivot_row = next((row for row in range(col, size) if rows[row][col]), None)
        assert pivot_row is not None, ("singular rational matrix", matrix)
        if pivot_row != col:
            rows[col], rows[pivot_row] = rows[pivot_row], rows[col]
            determinant = -determinant
        pivot = rows[col][col]
        determinant *= pivot
        rows[col] = [entry / pivot for entry in rows[col]]
        for row in range(size):
            if row != col and rows[row][col]:
                factor = rows[row][col]
                rows[row] = [a - factor * b for a, b in zip(rows[row], rows[col])]
    inverse = tuple(tuple(row[size:]) for row in rows)
    return inverse, determinant


def valuation(value, prime):
    if not value:
        return None  # Infinity.
    numerator, denominator = value.numerator, value.denominator
    exponent = 0
    while numerator % prime == 0:
        numerator //= prime
        exponent += 1
    while denominator % prime == 0:
        denominator //= prime
        exponent -= 1
    return exponent


def p_integral_reduction(matrix, prime):
    reduced = []
    for row in matrix:
        reduced_row = []
        for entry in row:
            denominator = entry.denominator % prime
            assert denominator, ("nonintegral reduction", entry, prime)
            reduced_row.append(entry.numerator * pow(denominator, -1, prime) % prime)
        reduced.append(reduced_row)
    return reduced


def rank_mod(matrix, width, prime):
    rows = [[entry % prime for entry in row] for row in matrix]
    rank = 0
    for col in range(width):
        pivot = next((row for row in range(rank, len(rows)) if rows[row][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_row = rows[rank]
        reciprocal = pow(pivot_row[col], -1, prime)
        for row in rows[rank + 1 :]:
            if row[col]:
                factor = row[col] * reciprocal
                for index in range(col, width):
                    row[index] = (row[index] - factor * pivot_row[index]) % prime
        rank += 1
        if rank == len(rows):
            break
    return rank


def compact_embedding(vector, prime, size):
    dimension = len(vector)
    pivot = next(index for index, entry in enumerate(vector) if entry)
    unit_columns = tuple(index for index in range(dimension) if index != pivot)
    matrix = [list(row) for row in identity(size)]
    for row, entry in enumerate(vector):
        matrix[row][0] = entry
        for col, coordinate in enumerate(unit_columns, start=1):
            matrix[row][col] = int(row == coordinate)
        matrix[row][dimension] = Fraction(int(row == 0) - entry, prime)
    return tuple(tuple(row) for row in matrix)


def check_a():
    elements = diagonal = off_diagonal = 0
    for prime, dimension, size in TRIPLES:
        unit = identity(size)
        records = []
        for vector in product(range(prime), repeat=dimension):
            if not any(vector):
                continue
            matrix = compact_embedding(vector, prime, size)
            inverse, determinant = inverse_and_determinant(matrix)
            assert multiply(matrix, inverse) == multiply(inverse, matrix) == unit, vector
            assert valuation(determinant, prime) == 0, (prime, vector, determinant)
            for constituent in (matrix, inverse):
                for row in constituent:
                    for entry in row:
                        exponent = valuation(entry, prime)
                        assert exponent is None or exponent >= -1, (prime, vector, entry)
            records.append((vector, matrix, inverse, determinant))
        assert len(records) == prime**dimension - 1, (prime, dimension, size)
        elements += len(records)

        # Check both orientations before counting two off-diagonal ordered pairs.
        for left, right in combinations_with_replacement(records, 2):
            x, matrix_x, inverse_x, det_x = left
            y, matrix_y, inverse_y, det_y = right
            context = (prime, dimension, size, x, y)
            assert valuation(det_y / det_x, prime) == 0, context
            relative = multiply(inverse_x, matrix_y)
            if x == y:
                assert relative == unit, context
                diagonal += 1
            else:
                assert valuation(det_x / det_y, prime) == 0, context
                reciprocal = multiply(inverse_y, matrix_x)
                for oriented in (relative, reciprocal):
                    reduced = p_integral_reduction(scale(oriented, prime), prime)
                    assert rank_mod(reduced, size, prime) == 1, context
                off_diagonal += 2
    counts = (elements, diagonal + off_diagonal, diagonal, off_diagonal)
    assert counts == (62, 920, 62, 858), counts
    return counts


def projective_covectors(prime, size):
    for pivot in range(size):
        for tail in product(range(prime), repeat=size - pivot - 1):
            yield (0,) * pivot + (1,) + tail, pivot


def neighbor_basis(covector, pivot, prime):
    matrix = [list(row) for row in identity(len(covector))]
    matrix[pivot] = [prime if col == pivot else -entry for col, entry in enumerate(covector)]
    return tuple(tuple(row) for row in matrix)


def check_b():
    neighbors = diagonal = off_diagonal = 0
    for prime, dimension, size in TRIPLES:
        unit = identity(size)
        scaled_unit = scale(unit, prime)
        records = []
        for covector, pivot in projective_covectors(prime, size):
            assert next(entry for entry in covector if entry) == 1, covector
            basis = neighbor_basis(covector, pivot, prime)
            inverse, determinant = inverse_and_determinant(basis)
            assert determinant == prime, (prime, covector, determinant)
            assert rank_mod(basis, size, prime) == size - 1, (prime, covector)
            for column in zip(*basis):
                assert sum(a * b for a, b in zip(covector, column)) % prime == 0, covector

            scaled_inverse = scale(inverse, prime)
            assert all(entry.denominator == 1 for row in scaled_inverse for entry in row), covector
            integer_inverse = tuple(tuple(entry.numerator for entry in row) for row in scaled_inverse)
            assert multiply(integer_inverse, basis) == scaled_unit, (prime, covector)
            assert multiply(basis, integer_inverse) == scaled_unit, (prime, covector)
            records.append((covector, basis, integer_inverse, determinant))
        expected = (prime**size - 1) // (prime - 1)
        assert len(records) == len({record[0] for record in records}) == expected, (prime, size)
        neighbors += len(records)

        # These products are p times the relatives, with integrality certified by
        # the integer factors above. Determinants of the relatives are quotients.
        for left, right in combinations_with_replacement(records, 2):
            a, basis_a, scaled_inverse_a, det_a = left
            b, basis_b, scaled_inverse_b, det_b = right
            context = (prime, dimension, size, a, b)
            assert valuation(det_b / det_a, prime) == 0, context
            scaled_relative = multiply(scaled_inverse_a, basis_b)
            if a == b:
                assert scaled_relative == scaled_unit, context
                diagonal += 1
            else:
                assert valuation(det_a / det_b, prime) == 0, context
                scaled_reciprocal = multiply(scaled_inverse_b, basis_a)
                assert rank_mod(scaled_relative, size, prime) == 1, context
                assert rank_mod(scaled_reciprocal, size, prime) == 1, context
                off_diagonal += 2
    counts = (neighbors, diagonal + off_diagonal, diagonal, off_diagonal)
    assert counts == (290, 21614, 290, 21324), counts
    return counts


def check_c():
    cases = 0
    for prime, dimension, size in TRIPLES:
        orbit_size = prime**dimension - 1
        neighbor_count = (prime**size - 1) // (prime - 1)
        for z in (Fraction(numerator, 4) for numerator in range(5)):
            context = (prime, dimension, size, z)
            a = (neighbor_count * z - 1) / (neighbor_count - 1)
            gram = tuple(
                tuple((1 - a) * int(row == col) + a for col in range(orbit_size))
                for row in range(orbit_size)
            )
            for row, entries in enumerate(gram):
                for col, value in enumerate(entries):
                    assert value == (1 if row == col else a), (context, row, col)
            lambda_constants = 1 + (orbit_size - 1) * a
            lambda_sum_zero = 1 - a
            lower_bound = Fraction(neighbor_count - orbit_size, neighbor_count - 1)
            assert lambda_constants >= lower_bound > 0, context

            # The constant vector has nonzero sum. The differences e_j - e_0
            # form a basis of the sum-zero space by their coordinates j > 0.
            for row, entries in enumerate(gram):
                assert sum(entries) == lambda_constants, (context, row)
                for col in range(1, orbit_size):
                    difference = entries[col] - entries[0]
                    coordinate = int(row == col) - int(row == 0)
                    assert difference == lambda_sum_zero * coordinate, (context, row, col)
            rank = int(lambda_constants != 0) + (orbit_size - 1) * int(lambda_sum_zero != 0)
            assert rank == (orbit_size if z < 1 else 1), (context, rank)
            cases += 1
    assert cases == 35, cases
    return cases


def check_d():
    cases = (
        (2, 2, 6, (1, 2)),
        (2, 3, 168, (1, 6)),
        (3, 2, 48, (1, 3, 4)),
        (3, 3, 11232, (1, 12, 13)),
    )
    considered = retained = 0
    for prime, size, expected_order, expected_dimensions in cases:
        unit = identity(size)
        sums = [0] * (len(expected_dimensions) - 1)
        squares = [0] * len(sums)
        mixed = 0
        case_considered = order = 0
        dimensions = None
        for entries in product(range(prime), repeat=size * size):
            case_considered += 1
            matrix = tuple(entries[start : start + size] for start in range(0, len(entries), size))
            if rank_mod(matrix, size, prime) != size:
                continue
            order += 1
            minus_identity = tuple(tuple(a - b for a, b in zip(row, one)) for row, one in zip(matrix, unit))
            chi_x = prime ** (size - rank_mod(minus_identity, size, prime)) - 1
            if prime == 2:
                characters = (chi_x - 1,)
            else:
                plus_identity = tuple(tuple(a + b for a, b in zip(row, one)) for row, one in zip(matrix, unit))
                chi_neg_x = prime ** (size - rank_mod(plus_identity, size, prime)) - 1
                chi_plus, plus_remainder = divmod(chi_x + chi_neg_x, 2)
                chi_minus, minus_remainder = divmod(chi_x - chi_neg_x, 2)
                assert plus_remainder == minus_remainder == 0, (prime, size, matrix)
                characters = (chi_plus - 1, chi_minus)
                mixed += characters[0] * characters[1]
            for index, value in enumerate(characters):
                sums[index] += value
                squares[index] += value**2
            if matrix == unit:
                dimensions = (1,) + characters

        context = (prime, size)
        assert case_considered == prime ** (size * size), context
        assert order == expected_order, (context, order)
        assert dimensions == expected_dimensions, (context, dimensions)
        assert sums == [0] * len(sums), (context, sums)
        assert squares == [order] * len(squares), (context, squares)
        if prime == 3:
            assert mixed == 0, (context, mixed)
        considered += case_considered
        retained += order
    counts = (considered, retained)
    assert counts == (20292, 11454), counts
    return counts


def rref_subspaces(prime, size):
    for dimension in range(1, size):
        for pivots in combinations(range(size), dimension):
            free = tuple(col for col in range(size) if col not in pivots)
            slots = tuple(
                (row, col)
                for row, pivot in enumerate(pivots)
                for col in free
                if col > pivot
            )
            matrix = [[0] * size for _ in pivots]
            for row, pivot in enumerate(pivots):
                matrix[row][pivot] = 1
            for entries in product(range(prime), repeat=len(slots)):
                for (row, col), entry in zip(slots, entries):
                    matrix[row][col] = entry
                yield tuple(tuple(row) for row in matrix), pivots, free


def check_e():
    counts = []
    for prime, size, expected_count in ((2, 4, 65), (3, 4, 210), (2, 5, 372)):
        positions = tuple((0, col) for col in range(1, size)) + tuple(
            (row, size - 1) for row in range(1, size - 1)
        )
        chi = [int(position in ((0, 1), (1, size - 1))) for position in positions]
        seen = set()
        for basis, pivots, free in rref_subspaces(prime, size):
            context = (prime, size, basis)
            assert basis not in seen, context
            seen.add(basis)

            # The pivot coordinates of v fix the coefficients for membership
            # in W. The free coordinates then give these annihilating forms.
            annihilator = []
            for col in free:
                covector = [0] * size
                covector[col] = 1
                for row, pivot in enumerate(pivots):
                    covector[pivot] = -basis[row][col]
                annihilator.append(covector)
            equations = [
                [covector[row] * vector[col] for row, col in positions]
                for vector in basis
                for covector in annihilator
            ]
            rank = rank_mod(equations, len(positions), prime)
            augmented_rank = rank_mod(equations + [chi], len(positions), prime)
            assert augmented_rank == rank + 1, (context, rank, augmented_rank)
        assert len(seen) == expected_count, (prime, size, len(seen))
        counts.append(len(seen))
    assert sum(counts) == 647, counts
    return counts


def main():
    a = check_a()
    print(f"A orbit_elements={a[0]} ordered_pairs={a[1]} diagonal={a[2]} off_diagonal={a[3]}")
    b = check_b()
    print(f"B neighbors={b[0]} ordered_pairs={b[1]} diagonal={b[2]} off_diagonal={b[3]}")
    print(f"C gram_cases={check_c()}")
    considered, retained = check_d()
    print(f"D considered={considered} invertible={retained}")
    counts = check_e()
    print(f"E subspaces={sum(counts)} case_counts={','.join(map(str, counts))}")


if __name__ == "__main__":
    main()
