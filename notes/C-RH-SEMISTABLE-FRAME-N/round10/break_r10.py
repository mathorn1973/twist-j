#!/usr/bin/env python3
"""Exact opponent audit from the frozen round 10 preregistration."""

from fractions import Fraction
from itertools import product


MODELS = (
    (2, 2, 3), (2, 2, 5), (3, 2, 3), (3, 2, 5),
    (2, 3, 4), (2, 3, 6), (3, 3, 4),
)


def identity(size, scale=1):
    return tuple(
        tuple(scale if i == j else 0 for j in range(size))
        for i in range(size)
    )


def multiply(left, right):
    columns = tuple(zip(*right))
    return tuple(
        tuple(sum(x * y for x, y in zip(row, col)) for col in columns)
        for row in left
    )


def rational_pivots(matrix):
    """Return the signed product of the pivots and their number."""
    rows = [list(map(Fraction, row)) for row in matrix]
    pivot_count = 0
    pivot_product = Fraction(1)
    for col in range(len(rows[0])):
        source = next(
            (i for i in range(pivot_count, len(rows)) if rows[i][col]),
            None,
        )
        if source is None:
            continue
        if source != pivot_count:
            rows[source], rows[pivot_count] = rows[pivot_count], rows[source]
            pivot_product = -pivot_product
        pivot_row = rows[pivot_count]
        pivot = pivot_row[col]
        pivot_product *= pivot
        for row in rows[pivot_count + 1:]:
            if row[col]:
                ratio = row[col] / pivot
                for j in range(col, len(row)):
                    row[j] -= ratio * pivot_row[j]
        pivot_count += 1
    return pivot_product, pivot_count


def determinant(matrix):
    pivot_product, count = rational_pivots(matrix)
    return pivot_product if count == len(matrix) else Fraction(0)


def is_unit(value, prime):
    value = Fraction(value)
    return value.numerator % prime != 0 and value.denominator % prime != 0


def scale_and_reduce(matrix, prime):
    residues = []
    for row in matrix:
        residue_row = []
        for value in row:
            scaled = prime * Fraction(value)
            assert scaled.denominator % prime != 0, (prime, value)
            residue_row.append(
                scaled.numerator * pow(scaled.denominator, -1, prime) % prime
            )
        residues.append(tuple(residue_row))
    return tuple(residues)


def has_rank_one(matrix, prime):
    # A nonzero pivot and all minors anchored at it certify rank one.
    pivot = next(
        ((i, j) for i, row in enumerate(matrix)
         for j, value in enumerate(row) if value % prime),
        None,
    )
    if pivot is None:
        return False
    i, j = pivot
    pivot_row = matrix[i]
    return all(
        (pivot_row[j] * row[col] - row[j] * pivot_row[col]) % prime == 0
        for row in matrix for col in range(len(row))
    )


def nonzero_vectors(prime, size):
    return tuple(vector for vector in product(range(prime), repeat=size) if any(vector))


def orbit_matrices(vector, prime, ambient_size):
    size = len(vector)
    pivot = next(i for i, value in enumerate(vector) if value)
    other_indices = tuple(i for i in range(size) if i != pivot)
    core_identity = identity(size)
    core = tuple(zip(vector, *(core_identity[i] for i in other_indices)))

    # Solve C_x t = v in the pivot coordinate and then in the remaining coordinates.
    first_row = tuple(
        Fraction(1, vector[pivot]) if coordinate == pivot else 0
        for coordinate in range(size)
    )
    core_inverse = (first_row,) + tuple(
        tuple(a - vector[i] * b for a, b in zip(core_identity[i], first_row))
        for i in other_indices
    )
    offset = tuple(Fraction(core_identity[0][i] - vector[i], prime) for i in range(size))
    inverse_offset = tuple(
        -sum(a * b for a, b in zip(row, offset)) for row in core_inverse
    )
    ambient_identity = identity(ambient_size)
    padding = (0,) * (ambient_size - size - 1)
    matrix = tuple(
        row + (value,) + padding for row, value in zip(core, offset)
    ) + ambient_identity[size:]
    inverse = tuple(
        row + (value,) + padding for row, value in zip(core_inverse, inverse_offset)
    ) + ambient_identity[size:]
    return matrix, inverse


def check_word_prime_orbit():
    elements = diagonal = off_diagonal = 0
    for prime, size, ambient_size in MODELS:
        vectors = nonzero_vectors(prime, size)
        assert len(vectors) == len(set(vectors)) == prime ** size - 1
        matrices = []
        ambient_identity = identity(ambient_size)
        for vector in vectors:
            matrix, inverse = orbit_matrices(vector, prime, ambient_size)
            scale_and_reduce(matrix, prime)
            scale_and_reduce(inverse, prime)
            assert multiply(matrix, inverse) == ambient_identity, vector
            assert multiply(inverse, matrix) == ambient_identity, vector
            value = determinant(matrix)
            assert is_unit(value, prime), vector
            matrices.append((matrix, inverse, value))
        elements += len(matrices)
        for i, (left, left_inverse, left_det) in enumerate(matrices):
            for j in range(i, len(matrices)):
                right, right_inverse, right_det = matrices[j]
                context = (prime, size, ambient_size, vectors[i], vectors[j])
                relative = multiply(left_inverse, right)
                # The determinants of both relative matrices are ratios of the basis determinants.
                assert is_unit(right_det / left_det, prime), context
                if i == j:
                    assert relative == ambient_identity, context
                    diagonal += 1
                    continue
                reverse = multiply(right_inverse, left)
                assert is_unit(left_det / right_det, prime), context
                assert multiply(relative, reverse) == ambient_identity, context
                assert multiply(reverse, relative) == ambient_identity, context
                assert has_rank_one(scale_and_reduce(relative, prime), prime), context
                assert has_rank_one(scale_and_reduce(reverse, prime), prime), context
                off_diagonal += 2
    assert (elements, diagonal + off_diagonal, diagonal, off_diagonal) == (62, 920, 62, 858)
    print(f"A orbit: elements={elements} ordered={diagonal + off_diagonal} "
          f"diagonal={diagonal} off_diagonal={off_diagonal}")


def neighbor_basis(covector, prime, pivot):
    size = len(covector)
    unit = identity(size)
    scaled_unit = identity(size, prime)
    matrix = tuple(
        tuple(prime if i == pivot else -covector[i] for i in range(size))
        if index == pivot else row
        for index, row in enumerate(unit)
    )
    scaled_inverse = tuple(
        covector if index == pivot else row
        for index, row in enumerate(scaled_unit)
    )
    return matrix, scaled_inverse


def scaled_neighbor_relative(scaled_inverse, covector, pivot, prime):
    # The products of integer entries give the required p-integral matrix at scale p.
    # Use the sparse columns of the right-hand lattice basis.
    return tuple(
        tuple(prime * row[pivot] if col == pivot else row[col] - a * row[pivot]
              for col, a in enumerate(covector))
        for row in scaled_inverse
    )


def check_neighbors():
    neighbors = diagonal = off_diagonal = 0
    for prime, orbit_size, size in MODELS:
        normalized = tuple(
            ((0,) * pivot + (1,) + tail, pivot)
            for pivot in range(size)
            for tail in product(range(prime), repeat=size - pivot - 1)
        )
        expected = (prime ** size - 1) // (prime - 1)
        assert len(normalized) == len({a for a, _ in normalized}) == expected
        scaled_identity = identity(size, prime)
        squared_scale_identity = identity(size, prime * prime)
        bases = []
        for covector, pivot in normalized:
            assert next(value for value in covector if value) == 1
            matrix, scaled_inverse = neighbor_basis(covector, prime, pivot)
            value = determinant(matrix)
            assert value == prime, covector
            assert multiply(matrix, scaled_inverse) == scaled_identity, covector
            assert multiply(scaled_inverse, matrix) == scaled_identity, covector
            assert all(sum(a * v for a, v in zip(covector, col)) % prime == 0
                       for col in zip(*matrix)), covector
            bases.append((covector, pivot, scaled_inverse, value))
        neighbors += len(bases)
        for i, (a, a_pivot, a_inverse, a_det) in enumerate(bases):
            for j in range(i, len(bases)):
                b, b_pivot, b_inverse, b_det = bases[j]
                context = (prime, orbit_size, size, a, b)
                relative = scaled_neighbor_relative(a_inverse, b, b_pivot, prime)
                assert is_unit(b_det / a_det, prime), context
                if i == j:
                    assert relative == scaled_identity, context
                    diagonal += 1
                    continue
                reverse = scaled_neighbor_relative(b_inverse, a, a_pivot, prime)
                assert is_unit(a_det / b_det, prime), context
                # These products test the two inverse identities at scale p^2.
                assert multiply(relative, reverse) == squared_scale_identity, context
                assert multiply(reverse, relative) == squared_scale_identity, context
                assert has_rank_one(relative, prime), context
                assert has_rank_one(reverse, prime), context
                off_diagonal += 2
    assert (neighbors, diagonal + off_diagonal, diagonal, off_diagonal) == (290, 21614, 290, 21324)
    print(f"B neighbors: neighbors={neighbors} ordered={diagonal + off_diagonal} "
          f"diagonal={diagonal} off_diagonal={off_diagonal}")


def check_gram():
    count = 0
    for prime, size, ambient_size in MODELS:
        orbit_count = prime ** size - 1
        neighbor_count = (prime ** ambient_size - 1) // (prime - 1)
        for quarter in range(5):
            z = Fraction(quarter, 4)
            context = (prime, size, ambient_size, z)
            a = (neighbor_count * z - 1) / (neighbor_count - 1)
            constant_eigenvalue = 1 + (orbit_count - 1) * a
            difference_eigenvalue = 1 - a
            gram = tuple(
                tuple((1 - a) * entry + a for entry in row)
                for row in identity(orbit_count)
            )
            for i, row in enumerate(gram):
                assert all(entry == (1 if i == j else a)
                           for j, entry in enumerate(row)), context
                assert sum(row) == constant_eigenvalue, context
                # The vectors e_j - e_last form a basis for the sum-zero space.
                assert all(
                    row[j] - row[-1]
                    == difference_eigenvalue * (int(i == j) - int(i == orbit_count - 1))
                    for j in range(orbit_count - 1)
                ), context
            assert constant_eigenvalue >= Fraction(neighbor_count - orbit_count, neighbor_count - 1) > 0, context
            _, rank = rational_pivots(gram)
            assert rank == (orbit_count if z < 1 else 1), context
            count += 1
    assert count == 35
    print(f"C Gram: cases={count}")


def check_compact_types():
    total_considered = total_retained = 0
    for prime, size, expected_order, expected_dims in (
        (2, 2, 6, (1, 2)), (2, 3, 168, (1, 6)),
        (3, 2, 48, (1, 3, 4)), (3, 3, 11232, (1, 12, 13)),
    ):
        zero = (0,) * size
        vectors = nonzero_vectors(prime, size)
        negative_vectors = tuple(tuple(-value % prime for value in v) for v in vectors)
        rows = (zero,) + vectors
        row_actions = {
            row: tuple(sum(a * b for a, b in zip(row, v)) % prime for v in vectors)
            for row in rows
        }
        group_identity = identity(size)
        rank_by_image_size = {prime ** rank: rank for rank in range(size + 1)}
        considered = retained = 0
        aug_sum = minus_sum = aug_square = minus_square = cross_sum = 0
        identity_dimensions = None
        for matrix in product(rows, repeat=size):
            considered += 1
            images = tuple(zip(*(row_actions[row] for row in matrix)))
            # Over F_p a rank r map has exactly p^r distinct images, including 0.
            image_size = len(set(images) | {zero})
            assert image_size in rank_by_image_size, matrix
            if rank_by_image_size[image_size] != size:
                continue
            retained += 1
            assert zero not in images, matrix
            fixed = sum(image == origin for image, origin in zip(images, vectors))
            if prime == 2:
                augmentation = fixed - 1
                dims = (1, augmentation)
            else:
                negative_fixed = sum(
                    image == negative_origin
                    for image, negative_origin in zip(images, negative_vectors)
                )
                assert (fixed + negative_fixed) % 2 == (fixed - negative_fixed) % 2 == 0, matrix
                augmentation = (fixed + negative_fixed) // 2 - 1
                minus = (fixed - negative_fixed) // 2
                dims = (1, augmentation, minus)
                minus_sum += minus
                minus_square += minus * minus
                cross_sum += augmentation * minus
            aug_sum += augmentation
            aug_square += augmentation * augmentation
            if matrix == group_identity:
                identity_dimensions = dims
        assert considered == prime ** (size * size), (prime, size)
        assert retained == expected_order, (prime, size)
        assert identity_dimensions == expected_dims, (prime, size, identity_dimensions)
        assert aug_sum == 0 and aug_square == retained, (prime, size, aug_sum, aug_square)
        if prime == 3:
            assert minus_sum == cross_sum == 0 and minus_square == retained, (
                prime, size, minus_sum, cross_sum, minus_square,
            )
        total_considered += considered
        total_retained += retained
        print(f"D GL_{size}(F_{prime}): considered={considered} retained={retained} "
              f"dimensions={identity_dimensions}")
    assert (total_considered, total_retained) == (20292, 11454)
    print(f"D totals: considered={total_considered} retained={total_retained}")


def subspace_extensions(subspaces, additions, multiples, prime, size):
    """Adjoin each outside vector and deduplicate by the whole span."""
    extended = {}
    for span, basis in subspaces.items():
        for vector, scalar_multiples in enumerate(multiples):
            if vector in span:
                continue
            new_span = span.union(
                additions[shift][element]
                for shift in scalar_multiples[1:]
                for element in span
            )
            assert len(new_span) == prime ** size
            extended.setdefault(new_span, basis + (vector,))
    return extended


def witness_actions(prime, size, vectors, encoding):
    positions = tuple((0, col) for col in range(1, size)) + tuple(
        (row, size - 1) for row in range(1, size - 1)
    )
    a = positions.index((0, 1))
    b = positions.index((1, size - 1))
    for coefficients in product(range(prime), repeat=len(positions)):
        if (coefficients[a] + coefficients[b]) % prime != 1:
            continue
        rows = [[0] * size for _ in range(size)]
        for (row, col), value in zip(positions, coefficients):
            rows[row][col] = value
        action = tuple(
            encoding[tuple(sum(x * y for x, y in zip(row, vector)) % prime for row in rows)]
            for vector in vectors
        )
        yield (rows, action)


def check_stabilizer():
    total = 0
    for prime, size, expected in ((2, 4, 65), (3, 4, 210), (2, 5, 372)):
        vectors = tuple(product(range(prime), repeat=size))
        encoding = {vector: i for i, vector in enumerate(vectors)}
        additions = tuple(
            tuple(encoding[tuple((a + b) % prime for a, b in zip(vector, other))]
                  for other in vectors)
            for vector in vectors
        )
        multiples = tuple(
            tuple(encoding[tuple(scalar * value % prime for value in vector)]
                  for scalar in range(prime))
            for vector in vectors
        )
        witnesses = tuple(witness_actions(prime, size, vectors, encoding))
        assert len(witnesses) == prime ** (2 * size - 4)
        subspaces = {frozenset((encoding[(0,) * size],)): ()}
        count = 0
        for dimension in range(1, size):
            subspaces = subspace_extensions(subspaces, additions, multiples, prime, dimension)
            for span, basis in subspaces.items():
                context = (prime, size, dimension, tuple(sorted(span)))
                witness = next(
                    ((rows, action) for rows, action in witnesses
                     if all(action[vector] in span for vector in basis)),
                    None,
                )
                assert witness is not None, context
                rows, action = witness
                assert (rows[0][1] + rows[1][-1]) % prime == 1, context
                assert all(action[vector] in span for vector in span), context
                count += 1
        assert count == expected, (prime, size, count)
        total += count
        print(f"E F_{prime}^{size}: subspaces={count}")
    assert total == 647
    print(f"E total: subspaces={total}")


def main():
    if not __debug__:
        raise RuntimeError("The audit requires enabled assertions.")
    check_word_prime_orbit()
    check_neighbors()
    check_gram()
    check_compact_types()
    check_stabilizer()
    print("Round 10 exact audit passed (candidate-C).")


if __name__ == "__main__":
    main()
