"""Development verifier for the frozen round 8 finite audit."""

from fractions import Fraction
from itertools import combinations, product
from math import gcd


FAMILIES = (
    (2, 2, (1, 1)),
    (3, 2, (1, 1)),
    (2, 2, (1, 2)),
    (3, 2, (1, 2)),
    (2, 3, (1, 1)),
    (3, 3, (1, 1)),
    (2, 3, (1, 2)),
    (2, 3, (2, 2)),
)


def reduced_rows(rows, field):
    if field is None:
        matrix = [list(map(Fraction, row)) for row in rows]
    else:
        matrix = [[entry % field for entry in row] for row in rows]
    if not matrix:
        return matrix, []

    pivots = []
    for column in range(len(matrix[0])):
        position = len(pivots)
        pivot = next((i for i in range(position, len(matrix)) if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[position], matrix[pivot] = matrix[pivot], matrix[position]
        row = matrix[position]
        if field is None:
            normalizer = 1 / row[column]
            row = [normalizer * entry for entry in row]
        else:
            normalizer = pow(row[column], -1, field)
            row = [normalizer * entry % field for entry in row]
        matrix[position] = row

        for i, other in enumerate(matrix):
            if i == position or not other[column]:
                continue
            factor = other[column]
            if field is None:
                matrix[i] = [x - factor * y for x, y in zip(other, row)]
            else:
                matrix[i] = [(x - factor * y) % field for x, y in zip(other, row)]
        pivots.append(column)
        if len(pivots) == len(matrix):
            break
    return matrix[:len(pivots)], pivots


def rank(rows, field):
    return len(reduced_rows(rows, field)[1])


def kernel_basis(rows, width, field):
    matrix, pivots = reduced_rows(rows, field)
    basis = []
    for free in range(width):
        if free in pivots:
            continue
        vector = [0] * width
        vector[free] = 1
        for row, pivot in zip(matrix, pivots):
            coefficient = -row[free]
            vector[pivot] = coefficient if field is None else coefficient % field
        basis.append(tuple(vector))
    return tuple(basis)


def subspace_bases(dimension, field):
    """Enumerate the unique reduced row echelon bases of all subspaces."""
    for subspace_dim in range(dimension + 1):
        for pivots in combinations(range(dimension), subspace_dim):
            free = [
                (row, column)
                for row, pivot in enumerate(pivots)
                for column in range(pivot + 1, dimension)
                if column not in pivots
            ]
            for entries in product(range(field), repeat=len(free)):
                basis = [[0] * dimension for _ in pivots]
                for row, pivot in enumerate(pivots):
                    basis[row][pivot] = 1
                for (row, column), entry in zip(free, entries):
                    basis[row][column] = entry
                yield tuple(tuple(row) for row in basis)


def matrix_families(field, target_dim, source_dims):
    """Maps are tuples of columns. The entry counter runs by source, row, column."""
    for entries in product(range(field), repeat=target_dim * sum(source_dims)):
        maps = []
        offset = 0
        for dim in source_dims:
            maps.append(tuple(
                tuple(entries[offset + row * dim + column] for row in range(target_dim))
                for column in range(dim)
            ))
            offset += target_dim * dim
        yield tuple(maps)


def defect(maps, target_dim, target_bases, field):
    source_dim = sum(map(len, maps))
    best_numerator = 0
    for basis in target_bases:
        basis_dim = len(basis)
        codimension_sum = sum(rank(columns + basis, field) - basis_dim for columns in maps)
        inverse_dim_sum = source_dim - codimension_sum
        numerator = target_dim * inverse_dim_sum - source_dim * basis_dim
        best_numerator = max(best_numerator, numerator)
    return Fraction(best_numerator, source_dim * target_dim)


def direct_sum_bases(source_dims, field):
    block_bases = []
    offset = 0
    width = sum(source_dims)
    for dim in source_dims:
        before = (0,) * offset
        after = (0,) * (width - offset - dim)
        block_bases.append(tuple(
            tuple(before + row + after for row in basis)
            for basis in subspace_bases(dim, field)
        ))
        offset += dim
    return tuple(sum(bases, ()) for bases in product(*block_bases))


def kernel_expression(maps, target_dim, source_bases, field):
    columns = sum(maps, ())
    source_dim = len(columns)
    kernel = kernel_basis(zip(*columns), source_dim, field)
    best_numerator = 0
    for basis in source_bases:
        basis_dim = len(basis)
        intersection_dim = len(kernel) + basis_dim - rank(kernel + basis, field)
        numerator = source_dim * intersection_dim - (source_dim - target_dim) * basis_dim
        best_numerator = max(best_numerator, numerator)
    return Fraction(best_numerator, source_dim)


def auxiliary_matrices(field, source_count, a, b, ell, family_index, seed):
    state = 1 + seed + 17 * family_index
    matrices = []
    for _ in range(source_count):
        matrix = []
        for _ in range(a * ell):
            row = []
            for _ in range(b * ell):
                state = (1103515245 * state + 12345) % (1 << 31)
                row.append((state >> 16) % field)
            matrix.append(tuple(row))
        matrices.append(tuple(matrix))
    return tuple(matrices)


def kronecker_matrix(maps, auxiliaries, target_dim):
    return tuple(
        tuple(
            column[target_row] * entry
            for columns, aux in zip(maps, auxiliaries)
            for column in columns
            for entry in aux[aux_row]
        )
        for target_row in range(target_dim)
        for aux_row in range(len(auxiliaries[0]))
    )


def audit_finite_families():
    families = 0
    certificates = {1: 0, 2: 0}
    for field, target_dim, source_dims in FAMILIES:
        source_dim = sum(source_dims)
        divisor = gcd(target_dim, source_dim)
        a, b = source_dim // divisor, target_dim // divisor
        square_dim = target_dim * a
        target_bases = tuple(subspace_bases(target_dim, field))
        source_bases = direct_sum_bases(source_dims, field)
        for family_index, maps in enumerate(matrix_families(field, target_dim, source_dims)):
            label = (field, target_dim, source_dims, family_index)
            eps = defect(maps, target_dim, target_bases, field)
            assert target_dim * eps == kernel_expression(maps, target_dim, source_bases, field), label
            for ell in ((1, 2) if family_index < 32 else (1,)):
                for seed in range(4):
                    aux = auxiliary_matrices(field, len(maps), a, b, ell, family_index, seed)
                    matrix = kronecker_matrix(maps, aux, target_dim)
                    matrix_rank = rank(matrix, field)
                    assert eps <= 1 - Fraction(matrix_rank, square_dim * ell), (label, ell, seed)
                    certificates[ell] += 1
            families += 1
    assert families == 6291
    assert certificates == {1: 25164, 2: 960}
    print(f"A: {families} exhaustive map families satisfy the kernel formula")
    print(f"B: {certificates[1]} level-1 and {certificates[2]} level-2 rank bounds hold")


def audit_group_averaging():
    points = tuple(product(range(2), repeat=2))
    weights = ((1, 0), (0, 1), (1, 1))
    characters = tuple(
        tuple((-1) ** (a * x + b * y) for x, y in points)
        for a, b in weights
    )
    gram = tuple(tuple(sum(x * y for x, y in zip(u, v)) for v in characters) for u in characters)
    assert gram == ((4, 0, 0), (0, 4, 0), (0, 0, 4))
    assert rank(characters, None) == 3
    point_index = {point: i for i, point in enumerate(points)}
    averaged = tuple(
        tuple(Fraction(vector[i] + vector[point_index[(y, x)]], 2) for i, (x, y) in enumerate(points))
        for vector in characters
    )
    first, second, third = averaged
    assert first == second
    assert all(rank((column,), None) == 1 for column in averaged)
    assert rank((first, third), None) == rank(averaged, None) == 2
    relation = (1, -1, 0)
    assert kernel_basis(zip(*averaged), 3, None) == (tuple(-entry for entry in relation),)

    maps = (((1, 0),), ((1, 0),), ((0, 1),))
    witness = (((1, 0),),)
    lower = defect(maps, 2, witness, None)
    assert lower == Fraction(1, 6)
    aux = (
        ((1, 0), (0, 1), (0, 0)),
        ((0, 0), (1, 0), (0, 1)),
        ((1, 0), (0, 1), (0, 0)),
    )
    matrix_rank = rank(kronecker_matrix(maps, aux, 2), None)
    assert matrix_rank == 5
    assert lower == 1 - Fraction(matrix_rank, 6)
    print(f"C: rational character Gram 4I, synthesis rank 2, certificate rank {matrix_rank}/6, epsilon {lower}")


def block_defect(columns, target_dim, bases, field):
    image_ranks = tuple(rank((column,), field) for column in columns)
    image_dim_sum = sum(image_ranks)
    if not image_dim_sum:
        return Fraction(0), 0
    best_numerator = 0
    for basis in bases:
        basis_dim = len(basis)
        intersection_dim_sum = sum(
            image_rank + basis_dim - rank((column,) + basis, field)
            for column, image_rank in zip(columns, image_ranks)
        )
        numerator = target_dim * intersection_dim_sum - image_dim_sum * basis_dim
        best_numerator = max(best_numerator, numerator)
    return Fraction(best_numerator, image_dim_sum * target_dim), image_dim_sum


def audit_block_families():
    families = 0
    zero_defect_cases = 0
    balanced_zero_defect_cases = 0
    for field, block_dims in ((2, (1, 1)), (3, (1, 1)), (2, (1, 2)), (3, (1, 2)), (2, (2, 2))):
        left, right = block_dims
        target_dim = left + right
        target_bases = tuple(subspace_bases(target_dim, field))
        left_bases = tuple(subspace_bases(left, field))
        right_bases = tuple(subspace_bases(right, field))
        q = (Fraction(left, target_dim), Fraction(right, target_dim))
        p = (Fraction(1, 2), Fraction(1, 2))
        beta = sum(abs(pi - qi) for pi, qi in zip(p, q)) / 2
        left_columns = tuple(product(range(field), repeat=left))
        right_columns = tuple(product(range(field), repeat=right))
        for first_left, first_right, second_left, second_right in product(
            left_columns, right_columns, left_columns, right_columns
        ):
            maps = (
                (first_left + (0,) * right, (0,) * left + first_right),
                (second_left + (0,) * right, (0,) * left + second_right),
            )
            eps = defect(maps, target_dim, target_bases, field)
            e_left, r_left = block_defect((first_left, second_left), left, left_bases, field)
            e_right, r_right = block_defect((first_right, second_right), right, right_bases, field)
            kappa = Fraction(4 - r_left - r_right, 4)
            b = (Fraction(r_left, 4), Fraction(r_right, 4))
            budget = sum(max(qi - bi, 0) for qi, bi in zip(q, b))
            remainder = sum(min(qi, bi) * ei for qi, bi, ei in zip(q, b, (e_left, e_right)))
            label = (field, block_dims, maps)
            assert max(kappa, beta) <= budget <= kappa + beta, label
            assert budget <= eps <= budget + remainder, label
            if e_left == e_right == 0:
                assert eps == budget, label
                zero_defect_cases += 1
                if p == q:
                    assert eps == kappa, label
                    balanced_zero_defect_cases += 1
            families += 1
    assert families == 1146
    print(
        f"D: {families} exhaustive block budgets hold, including {zero_defect_cases} zero-defect "
        f"and {balanced_zero_defect_cases} balanced zero-defect cases"
    )


def variation(p, q):
    return sum(abs(pi - qi) for pi, qi in zip(p, q)) / 2


def normalization(p, factors):
    weighted = tuple(pi * ai for pi, ai in zip(p, factors))
    total = sum(weighted)
    return tuple(value / total for value in weighted)


def marginals(table):
    return tuple(map(sum, table)), tuple(map(sum, zip(*table)))


def audit_normalization():
    cases = 0
    for s, t, n in product(range(1, 9), range(1, 9), range(2, 9)):
        p = (Fraction(s, s + t), Fraction(t, s + t))
        for m, sign1, sign2 in product(range(1, n), (-1, 1), (-1, 1)):
            eta = Fraction(m, n)
            q = normalization(p, (1 + sign1 * eta, 1 + sign2 * eta))
            v = variation(p, q)
            assert 2 * v <= eta * (1 + v * v), (s, t, n, m, sign1, sign2)
            cases += 1
    assert cases == 7168

    eta = Fraction(3, 5)
    p = (Fraction(2, 3), Fraction(1, 3))
    factors = (1 - eta, 1 + eta)
    assert factors == (Fraction(2, 5), Fraction(8, 5))
    q = normalization(p, factors)
    assert q == (Fraction(1, 3), Fraction(2, 3))
    v = variation(p, q)
    assert v == Fraction(1, 3)
    assert 2 * v == eta * (1 + v * v)

    half, quarter = Fraction(1, 2), Fraction(1, 4)
    table1 = ((half, Fraction(0)), (Fraction(0), half))
    table2 = ((quarter, quarter), (quarter, quarter))
    assert marginals(table1) == marginals(table2) == ((half, half), (half, half))
    joint_variation = variation(sum(table1, ()), sum(table2, ()))
    assert joint_variation == half
    print(f"E: {cases} normalization bounds hold, sharp variation {v}, joint variation {joint_variation}")


def main():
    audit_finite_families()
    audit_group_averaging()
    audit_block_families()
    audit_normalization()
    print("PASS: round 8 finite audit, NON-CANONICAL candidate-C")


if __name__ == "__main__":
    main()
