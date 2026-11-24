"""Opposition implementation of the frozen round 8 finite audit."""

from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import gcd


MAP_DOMAINS = (
    (2, 2, (1, 1), 16),
    (3, 2, (1, 1), 81),
    (2, 2, (1, 2), 64),
    (3, 2, (1, 2), 729),
    (2, 3, (1, 1), 64),
    (3, 3, (1, 1), 729),
    (2, 3, (1, 2), 512),
    (2, 3, (2, 2), 4096),
)

BLOCK_DOMAINS = (
    (2, (1, 1), 16),
    (3, (1, 1), 81),
    (2, (1, 2), 64),
    (3, (1, 2), 729),
    (2, (2, 2), 256),
)

SUBSPACE_COUNTS = {
    (2, 1): 2,
    (2, 2): 5,
    (2, 3): 16,
    (2, 4): 67,
    (3, 1): 2,
    (3, 2): 6,
    (3, 3): 28,
}


def require(condition, statement, case=()):
    if not condition:
        raise AssertionError(f"{statement}; case={case!r}")


@lru_cache(maxsize=None)
def vectors(field, dimension):
    return tuple(product(range(field), repeat=dimension))


@lru_cache(maxsize=None)
def dimensions_by_size(field, dimension):
    return {field**power: power for power in range(dimension + 1)}


@lru_cache(maxsize=None)
def subspaces(field, dimension):
    # Grow spans by adjoining a point. Sets identify equal spans directly.
    zero_space = frozenset({(0,) * dimension})
    discovered = {zero_space}
    frontier = [zero_space]
    for space in frontier:
        for point in vectors(field, dimension):
            if point in space:
                continue
            extended = frozenset(
                tuple((x + scalar * y) % field for x, y in zip(member, point))
                for member in space
                for scalar in range(field)
            )
            if extended not in discovered:
                discovered.add(extended)
                frontier.append(extended)
    require(len(frontier) == SUBSPACE_COUNTS[field, dimension],
            "subspace count", (field, dimension))
    sizes = dimensions_by_size(field, dimension)
    return tuple((space, sizes[len(space)]) for space in frontier)


def reshape_maps(entries, target_dimension, source_dimensions):
    maps = []
    offset = 0
    for width in source_dimensions:
        maps.append(tuple(
            entries[start:start + width]
            for start in range(offset, offset + target_dimension * width, width)
        ))
        offset += target_dimension * width
    return tuple(maps)


def image_table(matrix, field):
    return {
        point: tuple(sum(a * x for a, x in zip(row, point)) % field for row in matrix)
        for point in vectors(field, len(matrix[0]))
    }


def maximum_defect(field, target_dimension, source_dimensions, image_lists):
    # Count the preimage points, retaining repeats when a map has a kernel.
    source_total = sum(source_dimensions)
    size_tables = tuple(dimensions_by_size(field, width) for width in source_dimensions)
    largest_numerator = max(
        target_dimension * sum(
            sizes[sum(image in space for image in images)]
            for sizes, images in zip(size_tables, image_lists)
        ) - source_total * space_dimension
        for space, space_dimension in subspaces(field, target_dimension)
    )
    return Fraction(largest_numerator, source_total * target_dimension)


def kernel_maximum(field, target_dimension, source_dimensions, image_tables):
    # Enumerate K once as points of the direct sum, then intersect explicitly.
    left_table, right_table = image_tables
    kernel = tuple(
        (left_point, right_point)
        for left_point, left_image in left_table.items()
        for right_point, right_image in right_table.items()
        if all((x + y) % field == 0 for x, y in zip(left_image, right_image))
    )
    source_total = sum(source_dimensions)
    kernel_sizes = dimensions_by_size(field, source_total)
    largest_numerator = max(
        source_total * kernel_sizes[sum(
            left in left_space and right in right_space for left, right in kernel
        )] - (source_total - target_dimension) * (left_dimension + right_dimension)
        for left_space, left_dimension in subspaces(field, source_dimensions[0])
        for right_space, right_dimension in subspaces(field, source_dimensions[1])
    )
    return Fraction(largest_numerator, source_total)


def kronecker_concat(maps, auxiliaries):
    return [
        [entry * factor
         for matrix, auxiliary in zip(maps, auxiliaries)
         for entry in matrix[target_row]
         for factor in auxiliary[auxiliary_row]]
        for target_row in range(len(maps[0]))
        for auxiliary_row in range(len(auxiliaries[0]))
    ]


def sample_auxiliaries(field, family_index, seed, row_count, column_count):
    state = 1 + seed + 17 * family_index
    matrices = []
    for _ in range(2):
        matrix = []
        for _ in range(row_count):
            row = []
            for _ in range(column_count):
                state = (1103515245 * state + 12345) % (1 << 31)
                row.append((state >> 16) % field)
            matrix.append(row)
        matrices.append(matrix)
    return matrices


def prime_field_rank(matrix, field):
    rows = [[value % field for value in row] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((index for index in range(rank, len(rows)) if rows[index][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        leading_row = rows[rank]
        inverse = pow(leading_row[column], -1, field)
        for index in range(rank + 1, len(rows)):
            row = rows[index]
            factor = row[column] * inverse % field
            if factor:
                row[column:] = [(x - factor * y) % field
                                for x, y in zip(row[column:], leading_row[column:])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def rational_rank(matrix):
    rows = [[Fraction(value) for value in row] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((index for index in range(rank, len(rows)) if rows[index][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        leading_row = rows[rank]
        for index in range(rank + 1, len(rows)):
            row = rows[index]
            factor = row[column] / leading_row[column]
            if factor:
                rows[index] = [x - factor * y for x, y in zip(row, leading_row)]
        rank += 1
        if rank == len(rows):
            break
    return rank


def audit_maps_and_certificates():
    total_families = total_l1 = total_l2 = 0
    total_target_visits = total_source_pair_visits = 0
    for field, target_dimension, source_dimensions, expected_count in MAP_DOMAINS:
        source_total = sum(source_dimensions)
        divisor = gcd(target_dimension, source_total)
        a, b = source_total // divisor, target_dimension // divisor
        size = target_dimension * a
        families = l1_checks = l2_checks = 0
        target_count = len(subspaces(field, target_dimension))
        source_pair_count = (len(subspaces(field, source_dimensions[0]))
                             * len(subspaces(field, source_dimensions[1])))
        for family_index, entries in enumerate(product(range(field), repeat=target_dimension * source_total)):
            case = (field, target_dimension, source_dimensions, family_index)
            maps = reshape_maps(entries, target_dimension, source_dimensions)
            image_tables = tuple(image_table(matrix, field) for matrix in maps)
            eps = maximum_defect(field, target_dimension, source_dimensions,
                                 tuple(tuple(table.values()) for table in image_tables))
            kernel_defect = kernel_maximum(field, target_dimension, source_dimensions, image_tables)
            require(target_dimension * eps == kernel_defect,
                    "A kernel formula", (case, eps, kernel_defect))
            families += 1
            levels = (1, 2) if family_index < 32 else (1,)
            for level in levels:
                for seed in range(4):
                    auxiliaries = sample_auxiliaries(field, family_index, seed, a * level, b * level)
                    matrix = kronecker_concat(maps, auxiliaries)
                    order = size * level
                    require(len(matrix) == order and all(len(row) == order for row in matrix),
                            "B matrix shape", (case, level, seed))
                    rank = prime_field_rank(matrix, field)
                    require(eps <= Fraction(order - rank, order),
                            "B rank bound", (case, level, seed, eps, rank, order))
                    if level == 1:
                        l1_checks += 1
                    else:
                        l2_checks += 1
        require(families == expected_count, "A family count", (field, target_dimension, source_dimensions))
        require((l1_checks, l2_checks) == (4 * families, 4 * min(32, families)),
                "B certificate count", (field, target_dimension, source_dimensions))
        total_families += families
        total_l1 += l1_checks
        total_l2 += l2_checks
        total_target_visits += families * target_count
        total_source_pair_visits += families * source_pair_count
        print(f"A/B field={field} target={target_dimension} sources={source_dimensions} "
              f"families={families} target_spaces_per_family={target_count} "
              f"source_pairs_per_family={source_pair_count} l1={l1_checks} l2={l2_checks}", flush=True)

    require((total_families, total_l1, total_l2) == (6291, 25164, 960),
            "A/B total counts", (total_families, total_l1, total_l2))
    print(f"A pass families={total_families} target_subspace_visits={total_target_visits} "
          f"source_pair_visits={total_source_pair_visits}")
    print(f"B pass certificates={total_l1 + total_l2} l1={total_l1} l2={total_l2}")


def dot(left, right):
    return sum(x * y for x, y in zip(left, right))


def audit_averaging():
    points = tuple(product(range(2), repeat=2))
    characters = tuple(
        tuple((-1) ** dot(exponent, point) for point in points)
        for exponent in ((1, 0), (0, 1), (1, 1))
    )
    gram = tuple(tuple(dot(left, right) for right in characters) for left in characters)
    require(gram == ((4, 0, 0), (0, 4, 0), (0, 0, 4)), "C character Gram matrix", gram)
    character_rank = rational_rank(characters)
    require(character_rank == 3, "C character rank", (character_rank,))
    swap = tuple(points.index((y, x)) for x, y in points)
    projection = tuple(
        tuple(Fraction((column == row) + (column == swap[row]), 2) for column in range(4))
        for row in range(4)
    )
    projected = tuple(tuple(dot(row, character) for row in projection) for character in characters)
    b_vector, second_vector, c_vector = projected
    require(second_vector == b_vector, "C first two projected characters coincide", projected)
    require(rational_rank((b_vector, c_vector)) == 2, "C projected basis is independent", projected)
    require(all(rational_rank((column,)) == 1 for column in projected),
            "C projected line maps inject", projected)

    synthesis = tuple(zip(*projected))
    synthesis_rank = rational_rank(synthesis)
    kernel_witness = (1, -1, 0)
    require(synthesis_rank == 2, "C projected target span and synthesis rank", (synthesis_rank,))
    require(len(projected) - synthesis_rank == 1 and any(kernel_witness)
            and all(dot(row, kernel_witness) == 0 for row in synthesis),
            "C synthesis kernel", (synthesis, kernel_witness))

    coordinates = ((1, 0), (1, 0), (0, 1))
    reconstructed = tuple(tuple(x * b + y * c for b, c in zip(b_vector, c_vector))
                          for x, y in coordinates)
    require(reconstructed == projected, "C target coordinates", (reconstructed, projected))
    lower = Fraction(sum(y == 0 for _, y in coordinates), len(coordinates)) - Fraction(1, 2)
    require(lower == Fraction(1, 6), "C subspace lower witness", (lower,))

    maps = tuple(((x,), (y,)) for x, y in coordinates)
    x1 = ((1, 0), (0, 1), (0, 0))
    x2 = ((0, 0), (1, 0), (0, 1))
    x3 = ((1, 0), (0, 1), (0, 0))
    matrix = kronecker_concat(maps, (x1, x2, x3))
    require(len(matrix) == 6 and all(len(row) == 6 for row in matrix), "C certificate shape")
    certificate_rank = rational_rank(matrix)
    require(certificate_rank == 5, "C certificate rank", (certificate_rank,))
    upper = 1 - Fraction(certificate_rank, 6)
    require(lower == upper, "C witnesses certify exact defect", (lower, upper))
    print(f"C pass characters=3 character_rank={character_rank} synthesis_rank={synthesis_rank} "
          f"kernel_dimension=1 certificate_rank={certificate_rank} defect={lower}")


def block_columns(entries, block_dimensions):
    first, second = block_dimensions
    target_dimension = first + second
    return tuple((entries[start:start + first], entries[start + first:start + target_dimension])
                 for start in (0, target_dimension))


def diagonal_map(columns):
    first, second = columns
    return tuple((entry, 0) for entry in first) + tuple((0, entry) for entry in second)


def audit_blocks():
    total_families = total_semistable = total_balanced = 0
    total_full_visits = total_block_visits = 0
    for field, block_dimensions, expected_count in BLOCK_DOMAINS:
        target_dimension = sum(block_dimensions)
        source_total = 4
        p = (Fraction(1, 2), Fraction(1, 2))
        q = tuple(Fraction(dimension, target_dimension) for dimension in block_dimensions)
        beta = sum(abs(left - right) for left, right in zip(p, q)) / 2
        families = semistable = balanced = block_visits = 0
        target_count = len(subspaces(field, target_dimension))
        for family_index, entries in enumerate(product(range(field), repeat=2 * target_dimension)):
            case = (field, block_dimensions, family_index)
            columns = block_columns(entries, block_dimensions)
            maps = tuple(diagonal_map(pair) for pair in columns)
            image_lists = tuple(tuple(image_table(matrix, field).values()) for matrix in maps)
            eps = maximum_defect(field, target_dimension, (2, 2), image_lists)

            block_ranks = []
            internal_defects = []
            for block_index, block_dimension in enumerate(block_dimensions):
                active = tuple(pair[block_index] for pair in columns if any(pair[block_index]))
                block_rank = len(active)
                block_ranks.append(block_rank)
                internal = Fraction(0)
                if block_rank:
                    block_image_lists = tuple(
                        tuple(tuple(scalar * entry % field for entry in column)
                              for scalar in range(field))
                        for column in active
                    )
                    internal = maximum_defect(field, block_dimension, (1,) * block_rank,
                                              block_image_lists)
                    block_visits += len(subspaces(field, block_dimension))
                internal_defects.append(internal)

            b = tuple(Fraction(rank, source_total) for rank in block_ranks)
            kappa = Fraction(sum(2 - rank for rank in block_ranks), source_total)
            budget = sum(max(left - right, 0) for left, right in zip(q, b))
            weighted_internal = sum(min(left, right) * internal
                                    for left, right, internal in zip(q, b, internal_defects))
            require(max(kappa, beta) <= budget <= kappa + beta,
                    "D block budget limits", (case, kappa, beta, budget))
            require(budget <= eps <= budget + weighted_internal,
                    "D defect limits", (case, budget, eps, weighted_internal))
            if all(internal == 0 for internal in internal_defects):
                require(eps == budget, "D semistable equality", (case, eps, budget))
                semistable += 1
                if p == q:
                    require(eps == kappa, "D balanced semistable equality", (case, eps, kappa))
                    balanced += 1
            families += 1

        require(families == expected_count, "D family count", (field, block_dimensions, families))
        total_families += families
        total_semistable += semistable
        total_balanced += balanced
        total_full_visits += families * target_count
        total_block_visits += block_visits
        print(f"D field={field} blocks={block_dimensions} families={families} "
              f"target_spaces_per_family={target_count} block_subspace_visits={block_visits} "
              f"semistable={semistable} balanced_semistable={balanced}", flush=True)

    require(total_families == 1146, "D total families", (total_families,))
    print(f"D pass families={total_families} target_subspace_visits={total_full_visits} "
          f"block_subspace_visits={total_block_visits} semistable={total_semistable} "
          f"balanced_semistable={total_balanced}")


def total_variation(left, right):
    return sum(abs(x - y) for x, y in zip(left, right)) / 2


def normalize_trace(p, multipliers):
    weights = tuple(x * scale for x, scale in zip(p, multipliers))
    mean = sum(weights)
    return tuple(weight / mean for weight in weights)


def audit_normalization():
    grid_cases = 0
    equality_cases = 0
    for s, t, n in product(range(1, 9), range(1, 9), range(2, 9)):
        p = (Fraction(s, s + t), Fraction(t, s + t))
        for m in range(1, n):
            eta = Fraction(m, n)
            for delta1, delta2 in product((-1, 1), repeat=2):
                multipliers = (1 + delta1 * eta, 1 + delta2 * eta)
                q = normalize_trace(p, multipliers)
                deviation = total_variation(p, q)
                left, right = 2 * deviation, eta * (1 + deviation**2)
                require(left <= right, "E trace normalization bound",
                        (s, t, n, m, delta1, delta2, deviation))
                grid_cases += 1
                equality_cases += left == right
    require(grid_cases == 7168, "E grid count", (grid_cases,))

    eta = Fraction(3, 5)
    p = (Fraction(2, 3), Fraction(1, 3))
    multipliers = (1 - eta, 1 + eta)
    require(multipliers == (Fraction(2, 5), Fraction(8, 5)), "E equality multipliers", multipliers)
    q = normalize_trace(p, multipliers)
    deviation = total_variation(p, q)
    require(q == (Fraction(1, 3), Fraction(2, 3)) and deviation == Fraction(1, 3)
            and 2 * deviation == eta * (1 + deviation**2), "E trace equality case", (q, deviation))

    diagonal = ((Fraction(1, 2), Fraction(0)), (Fraction(0), Fraction(1, 2)))
    uniform = ((Fraction(1, 4),) * 2,) * 2
    require(tuple(map(sum, diagonal)) == tuple(map(sum, uniform))
            == (Fraction(1, 2), Fraction(1, 2)), "E matching row marginals")
    require(tuple(map(sum, zip(*diagonal))) == tuple(map(sum, zip(*uniform)))
            == (Fraction(1, 2), Fraction(1, 2)), "E matching column marginals")
    joint_deviation = total_variation(diagonal[0] + diagonal[1], uniform[0] + uniform[1])
    require(joint_deviation == Fraction(1, 2), "E joint total variation", (joint_deviation,))
    print(f"E pass grid_cases={grid_cases} grid_equalities={equality_cases} "
          f"additional_equality_cases=1 equality_variation={deviation} "
          f"marginal_table_pairs=1 joint_variation={joint_deviation}")


def main():
    audit_maps_and_certificates()
    audit_averaging()
    audit_blocks()
    audit_normalization()
    print("PASS C-RH-SEMISTABLE-FRAME-N round 8 finite opposition audit")


if __name__ == "__main__":
    main()
