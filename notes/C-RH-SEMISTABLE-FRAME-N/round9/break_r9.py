#!/usr/bin/env python3
"""Blind opposition to the frozen round 9 preregistration.

Author: A. M. Thorn. The verifier and its output were not consulted.
Only the standard library is used. No scientific execution precedes the freeze.
"""

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, permutations, product


AFFINE_CASES = ((2, 11), (2, 17), (2, 29), (3, 19), (3, 37), (4, 37), (4, 67), (5, 53))
LATTICE_CASES = ((1, 2), (1, 3), (1, 5), (2, 2), (2, 3))


class AuditFailure(Exception):
    """A prospective identity failed."""


def require(condition, detail):
    if not condition:
        raise AuditFailure(detail)


@dataclass(frozen=True)
class Layer:
    size: int
    weight: int
    labels: int
    incidence: tuple[int, ...]


@dataclass(frozen=True)
class Certificate:
    target: int
    ranks: tuple[int, ...]
    span: int
    source: int
    occupancy: tuple[Fraction, ...]
    mean: Fraction
    variance: Fraction
    positive_mass: Fraction
    coordinate_defect: Fraction


@dataclass(frozen=True)
class Family:
    t: int
    m: int
    layers: tuple[Layer, ...]
    certificate: Certificate


def incidence_layer(m, size, weight):
    # Transpose the incidence table. Each source has one bit for each atom label.
    require(size > 0, f"A m={m}: nonpositive atom size {size}")
    require(weight > 0, f"A m={m}, K={size}: nonpositive multiplicity")
    sources = [0] * m
    labels = 0
    for a, b in product(range(1, m), range(m)):
        support = {(a * j + b) % m for j in range(size)}
        require(len(support) == size, f"A m={m}: wrong atom size at {(size, a, b)}")
        atom_bit = 1 << labels
        for u in support:
            sources[u] |= atom_bit
        labels += 1
    return Layer(size, weight, labels, tuple(sources))


def coordinate_certificate(layers, copies):
    # An inclusion has a distinct output basis vector for every set bit and
    # every copy of that bit. Unions and intersections therefore count ranks.
    weights = tuple(layer.weight * copies for layer in layers)
    target = sum(layer.labels * weight for layer, weight in zip(layers, weights))
    ranks = tuple(
        sum(mask.bit_count() * weight for mask, weight in zip(masks, weights))
        for masks in zip(*(layer.incidence for layer in layers))
    )
    span = 0
    for layer, weight in zip(layers, weights):
        covered = 0
        for mask in layer.incidence:
            covered |= mask
        span += weight * covered.bit_count()

    source = sum(ranks)
    occupancy = tuple(Fraction(target * layer.size, source) for layer in layers)
    masses = tuple(
        Fraction(layer.labels * weight, target) for layer, weight in zip(layers, weights)
    )
    mean = sum(mass * value for mass, value in zip(masses, occupancy))
    variance = sum(
        mass * (value - mean) ** 2 for mass, value in zip(masses, occupancy)
    )
    positive_mass = sum(
        mass * max(value - 1, 0) for mass, value in zip(masses, occupancy)
    )

    high = layers[-1]
    high_rank = weights[-1] * sum(mask.bit_count() for mask in high.incidence)
    high_target = weights[-1] * high.labels
    coordinate_defect = Fraction(high_rank, source) - Fraction(high_target, target)
    return Certificate(
        target, ranks, span, source, occupancy, mean, variance,
        positive_mass, coordinate_defect,
    )


def audit_affine():
    families = []
    labels_checked = words_checked = pairs_checked = 0
    for t, m in AFFINE_CASES:
        key = f"A t={t}, m={m}"
        s = t * t
        layers = tuple(
            incidence_layer(m, size, weight)
            for size, weight in ((s - t, m - s), (s, 2 * s), (s + t, m - s))
        )
        certificate = coordinate_certificate(layers, 1)
        expected_target = 2 * m * m * (m - 1)
        expected_domain = 2 * m * (m - 1) * s
        require(certificate.target == expected_target, f"{key}: target dimension")
        require(certificate.source == s * expected_target, f"{key}: source dimension")
        require(certificate.span == expected_target, f"{key}: image span")

        for u, rank in enumerate(certificate.ranks):
            require(rank == expected_domain, f"{key}: source {u} has rank {rank}")
            for layer in layers:
                observed = layer.incidence[u].bit_count()
                expected = layer.size * (m - 1)
                require(
                    observed == expected,
                    f"{key}: source {u}, K={layer.size}: {observed} != {expected}",
                )
            words_checked += 1

        # Each ordered pair of distinct positions has a unique nonzero affine
        # multiplier and shift for fixed u != v. Check each layer independently
        # so discrepancies cannot cancel between layers in the weighted sum.
        expected_pair = 2 * s * s * (m - 1)
        gram_bound = Fraction(expected_domain ** 2, certificate.target)
        for u, v in combinations(range(m), 2):
            weighted_pair = 0
            for layer in layers:
                observed = (layer.incidence[u] & layer.incidence[v]).bit_count()
                expected = layer.size * (layer.size - 1)
                require(
                    observed == expected,
                    f"{key}: pair {(u, v)}, K={layer.size}: {observed} != {expected}",
                )
                weighted_pair += layer.weight * observed
            require(weighted_pair == expected_pair == gram_bound, f"{key}: Gram energy at {(u, v)}")
            pairs_checked += 1

        occupancies = tuple(Fraction(layer.size, s) for layer in layers)
        expected_variance = (1 - Fraction(s, m)) / s
        expected_defect = Fraction(m - s, 2 * m * t)
        require(certificate.occupancy == occupancies, f"{key}: occupancies")
        require(certificate.mean == 1, f"{key}: occupancy mean")
        require(certificate.variance == expected_variance, f"{key}: occupancy variance")
        require(certificate.positive_mass == expected_defect, f"{key}: positive spectral mass")
        require(certificate.coordinate_defect == expected_defect, f"{key}: coordinate defect")
        require(expected_defect ** 2 <= certificate.variance / 4, f"{key}: variance bound")

        labels_checked += sum(layer.labels for layer in layers)
        families.append(Family(t, m, layers, certificate))
        print(
            f"{key}: D={certificate.target}, d={expected_domain}, R={certificate.source}, "
            f"pair={expected_pair}, variance={certificate.variance}, defect={expected_defect}"
        )

    counts = (labels_checked, words_checked, pairs_checked)
    require(counts == (34134, 270, 5689), f"A: aggregate counts {counts}")
    print(f"A PASS: {counts[0]} atom labels, {counts[1]} sources, {counts[2]} pairs")
    return tuple(families)


def rotate(n, step, width):
    step %= width
    return ((n << step) | (n >> (width - step))) & ((1 << width) - 1)


def walsh_coefficients(values):
    # Unnormalized Walsh transform, using only the butterfly integer sums.
    coefficients = list(values)
    step = 1
    while step < len(coefficients):
        for start in range(0, len(coefficients), 2 * step):
            for offset in range(step):
                i = start + offset
                j = i + step
                a, b = coefficients[i], coefficients[j]
                coefficients[i], coefficients[j] = a + b, a - b
        step *= 2
    return coefficients


def audit_averaging(family):
    m = 11
    order_n = 1 << m
    order_g = m * order_n
    words = range(m)
    rotations = range(m)
    values = tuple(
        tuple(1 - 2 * ((n >> u) & 1) for u in words)
        for n in range(order_n)
    )
    permutation_rows = tuple(tuple((u + h) % m for u in words) for h in rotations)
    for u in words:
        require({row[u] for row in permutation_rows} == set(words), f"B: orbit of {u}")

    numerators = []
    for n, row in enumerate(values):
        sums = [0] * m
        for h, permutation in enumerate(permutation_rows):
            rotated = values[rotate(n, -h, m)]
            for u, v in enumerate(permutation):
                if rotated[u] != row[v]:
                    raise AuditFailure(f"B: rotation at {(n, h, u)}")
                sums[u] += rotated[u]

            # Left translation by (e_j, h) acts on functions via its inverse.
            # Its N component sends n to rotate(n XOR e_j, -h).
            for j in words:
                translated = values[rotate(n ^ (1 << j), -h, m)]
                for u, v in enumerate(permutation):
                    expected = -row[v] if j == v else row[v]
                    if translated[u] != expected:
                        raise AuditFailure(f"B: translated rotation at {(n, h, j, u)}")

        numerator = sum(row)
        require(all(value == numerator for value in sums), f"B: Gamma average at n={n}")
        numerators.append(numerator)

    for u, v in product(words, repeat=2):
        inner = Fraction(m * sum(row[u] * row[v] for row in values), order_g)
        require(inner == int(u == v), f"B: seed Gram entry {(u, v)} equals {inner}")

    norm_squared = Fraction(m * sum(n * n for n in numerators), order_g * m * m)
    require(norm_squared == Fraction(1, m), f"B: averaged norm squared {norm_squared}")
    require(m * norm_squared == 1, "B: squared isometric normalization")
    coefficients = walsh_coefficients(numerators)
    active = {1 << u for u in words}
    for frequency, coefficient in enumerate(coefficients):
        expected = order_n if frequency in active else 0
        require(coefficient == expected, f"B: Fourier numerator at {frequency} is {coefficient}")
    projection_ranks = []
    for u in words:
        inner_numerator = sum(row[u] * n for row, n in zip(values, numerators))
        inner = Fraction(m * inner_numerator, order_g * m)
        projected = Fraction(coefficients[1 << u], order_n * m)
        require(inner == projected == Fraction(1, m), f"B: seed coefficient {u}")
        # Each target coordinate projects along the same one-dimensional line.
        projection_ranks.append(family.certificate.target * int(projected != 0))

    require(family.m == m and len(family.certificate.ranks) == m, "B: affine seed count")
    require(all(rank == family.certificate.target for rank in projection_ranks), "B: Fourier kernels")
    direct_rank = 0
    for layer in family.layers:
        character_coordinates = 0
        for u, mask in enumerate(layer.incidence):
            character_coordinates |= mask << (u * layer.labels)
        direct_rank += layer.weight * character_coordinates.bit_count()
    require(direct_rank == family.certificate.source, "B: direct seed dimension")
    require(family.certificate.span == family.certificate.target, "B: averaged image cover")
    # The seed Gram matrix is diagonal by character across words. In each
    # coordinate of the target, P_u sends b to a nonzero multiple of f_u.
    print(
        f"B PASS: |G|={order_g}, orbit={m}, all {order_n * m ** 3} translated-character values, "
        f"norm squared={norm_squared}, projection coefficient={Fraction(1, m)}"
    )


def identity(size):
    return tuple(tuple(int(i == j) for j in range(size)) for i in range(size))


def transpose(matrix):
    return tuple(zip(*matrix))


def matrix_product(left, right):
    columns = transpose(right)
    return tuple(
        tuple(sum(a * b for a, b in zip(row, column)) for column in columns)
        for row in left
    )


def matrix_sum(*matrices):
    return tuple(
        tuple(sum(entries) for entries in zip(*rows))
        for rows in zip(*matrices)
    )


def scale(matrix, scalar):
    return tuple(tuple(scalar * entry for entry in row) for row in matrix)


def row_reduce(matrix, pivot_columns):
    rows = [list(map(Fraction, row)) for row in matrix]
    rank = 0
    pivot_product = Fraction(1)
    for column in range(pivot_columns):
        selected = next((i for i in range(rank, len(rows)) if rows[i][column]), None)
        if selected is None:
            continue
        if selected != rank:
            rows[rank], rows[selected] = rows[selected], rows[rank]
            pivot_product = -pivot_product
        pivot = rows[rank][column]
        pivot_product *= pivot
        rows[rank] = [entry / pivot for entry in rows[rank]]
        for i, row in enumerate(rows):
            if i != rank and row[column]:
                multiple = row[column]
                rows[i] = [entry - multiple * a for entry, a in zip(row, rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rows, rank, pivot_product


def matrix_rank(matrix):
    return row_reduce(matrix, len(matrix[0]))[1]


def inverse_and_determinant(matrix):
    size = len(matrix)
    augmented = tuple(row + unit for row, unit in zip(matrix, identity(size)))
    rows, rank, determinant = row_reduce(augmented, size)
    require(rank == size, "Encountered a singular matrix in inversion")
    return tuple(tuple(row[size:]) for row in rows), determinant


def compose(g, h):
    return tuple(g[i] for i in h)


def parity(g):
    return (-1) ** sum(g[i] > g[j] for i, j in combinations(range(len(g)), 2))


def audit_hecke(families):
    group = tuple(permutations(range(3)))
    size = len(group)
    units = identity(size)
    zero = scale(units, 0)
    regular = {
        g: tuple(tuple(int(h == compose(g, x)) for x in group) for h in group)
        for g in group
    }
    require(len(set(regular.values())) == 6, "C: faithful left regular matrices")
    for g, h in product(group, repeat=2):
        require(
            matrix_product(regular[g], regular[h]) == regular[compose(g, h)],
            f"C: regular multiplication at {(g, h)}",
        )

    e = scale(matrix_sum(units, scale(regular[(1, 0, 2)], -1)), Fraction(1, 2))
    z_triv = scale(matrix_sum(*regular.values()), Fraction(1, 6))
    z_sign = scale(
        matrix_sum(*(scale(regular[g], parity(g)) for g in group)), Fraction(1, 6)
    )
    z_std = matrix_sum(units, scale(z_triv, -1), scale(z_sign, -1))
    require(transpose(e) == e == matrix_product(e, e), "C: E self-adjoint idempotent")
    require(matrix_rank(e) == 3, "C: rank of E")
    require(matrix_product(e, z_triv) == zero, "C: trivial block")

    blocks = tuple(matrix_product(e, central) for central in (z_sign, z_std))
    block_ranks = tuple(matrix_rank(block) for block in blocks)
    require(block_ranks == (1, 2), f"C: block ranks {block_ranks}")
    for block in blocks:
        require(transpose(block) == block == matrix_product(block, block), "C: block projection")
    require(matrix_sum(*blocks) == e, "C: block sum")
    require(matrix_product(*blocks) == matrix_product(*reversed(blocks)) == zero, "C: orthogonal blocks")

    corners = tuple(matrix_product(matrix_product(e, regular[g]), e) for g in group)
    for i, j in combinations(range(size), 2):
        require(
            matrix_product(corners[i], corners[j]) == matrix_product(corners[j], corners[i]),
            f"C: corner commutator {(i, j)}",
        )
    flattened = tuple(tuple(entry for row in corner for entry in row) for corner in corners)
    corner_rank = matrix_rank(flattened)
    require(corner_rank == 2, f"C: dimension of corner span is {corner_rank}")

    for family in families:
        key = f"C t={family.t}, m={family.m}"
        original = family.certificate
        whole = coordinate_certificate(family.layers, sum(block_ranks))
        pieces = tuple(coordinate_certificate(family.layers, rank) for rank in block_ranks)
        require(whole.span == whole.target, f"{key}: corner span")
        require(whole.ranks == tuple(3 * rank for rank in original.ranks), f"{key}: corner kernels")
        require(sum(piece.target for piece in pieces) == whole.target, f"{key}: target block sum")
        require(sum(piece.source for piece in pieces) == whole.source, f"{key}: source block sum")

        weighted_defect = Fraction(0)
        for rank, piece, expected_weight in zip(block_ranks, pieces, (Fraction(1, 3), Fraction(2, 3))):
            target_weight = Fraction(piece.target, whole.target)
            source_weight = Fraction(piece.source, whole.source)
            require(target_weight == source_weight == expected_weight, f"{key}: rank {rank} balance")
            require(piece.ranks == tuple(rank * r for r in original.ranks), f"{key}: rank {rank} kernels")
            require(piece.span == piece.target, f"{key}: rank {rank} span")
            require(
                piece.coordinate_defect == piece.positive_mass == original.coordinate_defect,
                f"{key}: rank {rank} intrinsic defect",
            )
            weighted_defect += source_weight * piece.coordinate_defect
        require(
            weighted_defect == whole.coordinate_defect == whole.positive_mass == original.coordinate_defect,
            f"{key}: weighted intrinsic defect",
        )
        print(f"{key}: source and target weights 1/3, 2/3, weighted defect={weighted_defect}")
    print(f"C PASS: E rank 3, block ranks {block_ranks}, commuting corner span={corner_rank}")


def p_integral(matrix, p):
    return all(entry.denominator % p != 0 for row in matrix for entry in row)


def audit_mirabolic():
    totals = [0, 0, 0]
    for k, p in LATTICE_CASES:
        key = f"D k={k}, p={p}"
        units = identity(k + 1)
        z = units[0]
        ell = (p, 1) + (0,) * (k - 1)
        w1 = (1, -p) + (0,) * (k - 1)
        basis = transpose((z, w1) + units[2:])
        basis_inverse, _ = inverse_and_determinant(basis)

        tested = invertible = integral = 0
        for entries in product(range(p * p), repeat=k * k):
            tested += 1
            c = tuple(entries[i:i + k] for i in range(0, k * k, k))
            det_c = entries[0] if k == 1 else entries[0] * entries[3] - entries[1] * entries[2]
            if det_c % p == 0:
                continue
            invertible += 1

            middle = (z,) + tuple((0,) + row for row in c)
            ambient = matrix_product(matrix_product(basis, middle), basis_inverse)
            ambient_inverse, det_ambient = inverse_and_determinant(ambient)
            require(det_ambient == det_c, f"{key}: determinant at {c}")
            require(tuple(row[0] for row in ambient) == z, f"{key}: z at {c}")
            require(matrix_product((ell,), ambient) == (ell,), f"{key}: ell at {c}")
            require(matrix_product(ambient, ambient_inverse) == units, f"{key}: inverse at {c}")

            mirabolic = all(row[0] % p == int(i == 0) for i, row in enumerate(c))
            forward_integral = p_integral(ambient, p)
            inverse_integral = p_integral(ambient_inverse, p)
            require(
                forward_integral == inverse_integral == mirabolic,
                f"{key}: biconditional at {c}, G={forward_integral}, "
                f"G inverse={inverse_integral}, first column={mirabolic}",
            )
            integral += forward_integral

        counts = (tested, invertible, integral)
        totals = [a + b for a, b in zip(totals, counts)]
        print(f"{key}: candidates={tested}, invertible={invertible}, ambient integral={integral}")
    require(tuple(totals) == (6855, 4012, 528), f"D: aggregate counts {totals}")
    print(f"D PASS: {totals[0]} candidates, {totals[1]} invertible, {totals[2]} ambient integral")


def main():
    print("Round 9 blind opposition. NON-CANONICAL finite audit, status ceiling candidate-C.")
    try:
        families = audit_affine()
        audit_averaging(families[0])
        audit_hecke(families)
        audit_mirabolic()
    except AuditFailure as error:
        print(f"Round 9 blind opposition FAIL: {error}", flush=True)
        return 1
    except Exception:
        print("Round 9 blind opposition FAIL: unexpected execution error", flush=True)
        raise
    print("Round 9 blind opposition PASS: A, B, C and D")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
