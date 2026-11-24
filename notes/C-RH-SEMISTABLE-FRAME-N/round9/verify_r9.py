"""Development implementation of the frozen Round 9 finite audit."""

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, permutations, product


class AuditFailure(Exception):
    """An exact check failed."""


def require(condition, message):
    if not condition:
        raise AuditFailure(message)


@dataclass(frozen=True)
class Frame:
    t: int
    m: int
    atom_count: int
    pair_count: int
    target_dim: int
    source_dims: tuple
    source_ranks: tuple
    span_rank: int
    occupancy_dims: dict
    witness_target: int
    witness_source: int
    defect: Fraction


def spectral_certificate(occupancy_dims, target_dim, source_dim,
                         witness_target, witness_source, label):
    """Compute the coordinate witness and the trace upper bound."""
    require(sum(occupancy_dims.values()) == target_dim,
            f"{label} occupancy dimensions")
    require(sum(k * dimension for k, dimension in occupancy_dims.items()) == source_dim,
            f"{label} occupancy trace")
    occupancy = {k: Fraction(k * target_dim, source_dim) for k in occupancy_dims}
    mean = sum(Fraction(occupancy_dims[k], target_dim) * q for k, q in occupancy.items())
    require(mean == 1, f"{label} occupancy mean {mean}")
    variance = sum(Fraction(occupancy_dims[k], target_dim) * (q - 1) ** 2
                   for k, q in occupancy.items())
    positive_mass = sum(Fraction(occupancy_dims[k], target_dim) * max(q - 1, 0)
                        for k, q in occupancy.items())
    require(witness_target == occupancy_dims[max(occupancy_dims)],
            f"{label} high-occupancy witness target dimension")
    require(witness_source == max(occupancy_dims) * witness_target,
            f"{label} high-occupancy witness preimage dimension")
    defect = Fraction(witness_source, source_dim) - Fraction(witness_target, target_dim)
    require(defect == positive_mass, f"{label} witness {defect} vs upper bound {positive_mass}")
    require(defect ** 2 <= variance / 4, f"{label} variance upper bound")
    return occupancy, variance, defect


def audit_incidence(t, m):
    label = f"A (t={t}, m={m})"
    s = t * t
    atom_weights = {}
    occupancy_dims = {}
    source_dims = [0] * m
    supports = [set() for _ in range(m)]
    pair_counts = {(u, v): 0 for u, v in combinations(range(m), 2)}

    for k in (s - t, s, s + t):
        weight = 2 * s if k == s else m - s
        require(k > 0 and weight > 0, f"{label} nonpositive size or weight for K={k}")
        occupancy_dims[k] = 0
        for a in range(1, m):
            for b in range(m):
                members = sorted({(a * j + b) % m for j in range(k)})
                require(len(members) == k, f"{label} cardinality at {(k, a, b)}")
                atom = (k, a, b)
                require(atom not in atom_weights, f"{label} repeated coordinate label {atom}")
                atom_weights[atom] = weight
                occupancy_dims[k] += weight
                for u in members:
                    source_dims[u] += weight
                    supports[u].add(atom)
                for pair in combinations(members, 2):
                    pair_counts[pair] += weight

    target_dim = sum(atom_weights.values())
    source_dim = sum(source_dims)
    expected_d = 2 * m * (m - 1) * s
    expected_pair_count = 2 * s * s * (m - 1)
    require(target_dim == 2 * m * m * (m - 1), f"{label} D={target_dim}")
    require(source_dim == s * target_dim, f"{label} R={source_dim}")
    for u, dimension in enumerate(source_dims):
        require(dimension == expected_d, f"{label} d[{u}]={dimension}")
    require(Fraction(expected_d ** 2, target_dim) == expected_pair_count,
            f"{label} Gram-energy bound")
    for (u, v), count in pair_counts.items():
        require(count == expected_pair_count, f"{label} lambda[{u},{v}]={count}")

    # A supported label contributes its distinct coordinate copies to the rank.
    source_ranks = tuple(sum(atom_weights[atom] for atom in support)
                         for support in supports)
    span_rank = sum(atom_weights[atom] for atom in set().union(*supports))
    require(source_ranks == tuple(source_dims), f"{label} noninjective coordinate map")
    require(span_rank == target_dim, f"{label} target span rank={span_rank}")
    witness_labels = {atom for atom in atom_weights if atom[0] == s + t}
    witness_target = sum(atom_weights[atom] for atom in witness_labels)
    witness_source = sum(sum(atom_weights[atom] for atom in support & witness_labels)
                         for support in supports)
    occupancy, variance, defect = spectral_certificate(
        occupancy_dims, target_dim, source_dim, witness_target, witness_source, label
    )
    require(all(q == Fraction(k, s) for k, q in occupancy.items()),
            f"{label} occupancy entries {occupancy}")
    rho = Fraction(expected_d, target_dim)
    sigma = Fraction(target_dim, source_dim)
    require(variance == (1 - Fraction(s, m)) / s, f"{label} variance={variance}")
    require(defect == Fraction(m - s, 2 * m * t), f"{label} defect={defect}")
    require(4 * defect ** 2 == (1 - rho) ** 2 * sigma,
            f"{label} squared defect formula")

    print(f"{label}: labels={len(atom_weights)}, word counts={len(source_dims)}, "
          f"pair counts={len(pair_counts)}, D={target_dim}, d={expected_d}, "
          f"R={source_dim}, lambda={expected_pair_count}, span={span_rank}, "
          f"witness=({witness_target},{witness_source}), variance={variance}, defect={defect}")
    return Frame(t, m, len(atom_weights), len(pair_counts), target_dim, tuple(source_dims),
                 source_ranks, span_rank, occupancy_dims, witness_target, witness_source, defect)


def audit_affine_families():
    cases = ((2, 11), (2, 17), (2, 29), (3, 19), (3, 37), (4, 37), (4, 67), (5, 53))
    frames = tuple(audit_incidence(t, m) for t, m in cases)
    totals = (sum(frame.atom_count for frame in frames),
              sum(len(frame.source_dims) for frame in frames),
              sum(frame.pair_count for frame in frames))
    require(totals == (34134, 270, 5689), f"A totals {totals}")
    print(f"A totals: labels={totals[0]}, word counts={totals[1]}, pair counts={totals[2]}")
    return frames


def audit_averaging(frame):
    m = 11
    size = 1 << m
    mask = size - 1
    basis = tuple(1 << index for index in range(m))
    chars = tuple(tuple(1 if (n & bit) == 0 else -1 for bit in basis) for n in range(size))
    b_numerators = tuple(sum(row) for row in chars)
    inverse_rotations = tuple(tuple((u - h) % m for u in range(m)) for h in range(m))
    require(all(sorted(order) == list(range(m)) for order in inverse_rotations),
            "B cyclic action does not permute the characters")
    rotations = tuple(tuple(((n << h) | (n >> (m - h))) & mask for n in range(size))
                      for h in range(m))
    require({order[0] for order in inverse_rotations} == set(range(m)),
            "B characters do not form one orbit")

    rotation_count = 0
    translation_count = 0
    for n, row in enumerate(chars):
        gamma_sum = [0] * m
        for h, order in enumerate(inverse_rotations):
            rotated = rotations[h][n]
            rotated_row = chars[rotated]
            for u, source_u in enumerate(order):
                if rotated_row[u] != row[source_u]:
                    raise AuditFailure(f"B rotation at {(n, h, u)}")
                gamma_sum[u] += rotated_row[u]
                rotation_count += 1

            for v, bit in enumerate(basis):
                # Left action of (e_v,h) and right action of (e_v,0).
                left_row = chars[bit ^ rotated]
                rotated_v = (v + h) % m
                right_row = chars[n ^ rotations[h][bit]]
                for u in range(m):
                    expected_left = -row[order[u]] if u == v else row[order[u]]
                    expected_right = -row[u] if u == rotated_v else row[u]
                    if left_row[u] != expected_left or right_row[u] != expected_right:
                        raise AuditFailure(f"B standard translation at {(n, h, u, v)}")
                    translation_count += 2
        require(gamma_sum == [b_numerators[n]] * m, f"B Gamma average at n={n}")

    require(rotation_count == size * m ** 2, f"B rotation count {rotation_count}")
    require(translation_count == 2 * size * m ** 3, f"B translation count {translation_count}")
    char_columns = tuple(zip(*chars))
    # Each function is constant in the Gamma coordinate. Its multiplicity cancels.
    for u, column in enumerate(char_columns):
        for v, other in enumerate(char_columns):
            inner = Fraction(sum(x * y for x, y in zip(column, other)), size)
            require(inner == int(u == v), f"B Gram[{u},{v}]={inner}")

    norm_squared = Fraction(sum(value ** 2 for value in b_numerators), size * m ** 2)
    require(norm_squared == Fraction(1, m), f"B average norm squared={norm_squared}")
    projection_count = 0
    for u, column in enumerate(char_columns):
        inner = Fraction(sum(x * value for x, value in zip(column, b_numerators)), size * m)
        require(inner == Fraction(1, m), f"B inner product for word {u}: {inner}")
        for n in range(size):
            # The numerator of P_u b(n), before division by |N| m.
            numerator = sum(sign * b_numerators[n ^ translation]
                            for translation, sign in enumerate(column))
            if numerator != size * column[n]:
                raise AuditFailure(f"B full N-character projection at {(u, n)}: {numerator}")
            projection_count += 1

    require(projection_count == size * m, f"B projection count {projection_count}")
    require(m * norm_squared == 1, "B squared normalization of the averaged maps")
    require(frame.m == m and all(dimension == rank for dimension, rank
                                in zip(frame.source_dims, frame.source_ranks)),
            "B seed coordinate inclusions")
    require(frame.span_rank == frame.target_dim, "B averaged target span")
    print(f"B: |N|={size}, |N semidirect Gamma|={size * m}, "
          f"rotations={rotation_count}, translations={translation_count}, "
          f"Gram entries={m ** 2}, average evaluations={size * m}, "
          f"full projection evaluations={projection_count}, orbit size={m}, "
          f"average squared norm={norm_squared}, squared normalization={m}")


def identity(size):
    return tuple(tuple(int(i == j) for j in range(size)) for i in range(size))


def transpose(matrix):
    return tuple(zip(*matrix))


def multiply(left, right):
    columns = transpose(right)
    return tuple(tuple(sum(x * y for x, y in zip(row, col)) for col in columns)
                 for row in left)


def add(left, right):
    return tuple(tuple(x + y for x, y in zip(left_row, right_row))
                 for left_row, right_row in zip(left, right))


def scale(matrix, factor):
    return tuple(tuple(factor * entry for entry in row) for row in matrix)


def eliminate(matrix, width):
    """Reduce the first width columns and track pivot count and determinant factor."""
    rows = [[Fraction(entry) for entry in row] for row in matrix]
    pivot_count = 0
    determinant_factor = Fraction(1)
    for j in range(width):
        pivot = next((i for i in range(pivot_count, len(rows)) if rows[i][j]), None)
        if pivot is None:
            continue
        if pivot != pivot_count:
            rows[pivot_count], rows[pivot] = rows[pivot], rows[pivot_count]
            determinant_factor = -determinant_factor
        value = rows[pivot_count][j]
        determinant_factor *= value
        pivot_row = [entry / value for entry in rows[pivot_count]]
        rows[pivot_count] = pivot_row
        for i, row in enumerate(rows):
            if i != pivot_count and row[j]:
                multiplier = row[j]
                rows[i] = [entry - multiplier * other for entry, other in zip(row, pivot_row)]
        pivot_count += 1
    return rows, pivot_count, determinant_factor


def rank(matrix):
    return eliminate(matrix, len(matrix[0]))[1]


def inverse_and_determinant(matrix):
    size = len(matrix)
    augmented = tuple(row + unit_row for row, unit_row in zip(matrix, identity(size)))
    rows, pivots, determinant = eliminate(augmented, size)
    require(pivots == size, "Singular matrix where an inverse is required")
    return tuple(tuple(row[size:]) for row in rows), determinant


def compose(g, h):
    return tuple(g[x] for x in h)


def audit_hecke(frames):
    group = tuple(permutations(range(3)))
    unit = identity(len(group))
    zero = scale(unit, 0)
    tau = (1, 0, 2)
    regular = {g: tuple(tuple(int(x == compose(g, h)) for h in group) for x in group)
               for g in group}
    require(len(regular) == 6, "C regular group cardinality")
    for g, h in product(group, repeat=2):
        require(multiply(regular[g], regular[h]) == regular[compose(g, h)],
                f"C left regular multiplication for {(g, h)}")

    signs = {g: (-1) ** sum(g[i] > g[j] for i, j in combinations(range(3), 2))
             for g in group}
    trivial = zero
    sign = zero
    for g in group:
        trivial = add(trivial, scale(regular[g], Fraction(1, 6)))
        sign = add(sign, scale(regular[g], Fraction(signs[g], 6)))
    standard = add(add(unit, scale(trivial, -1)), scale(sign, -1))
    corner = scale(add(unit, scale(regular[tau], -1)), Fraction(1, 2))
    corner_rank = rank(corner)
    require(transpose(corner) == corner and multiply(corner, corner) == corner,
            "C corner self-adjoint idempotence")
    require(corner_rank == 3, f"C corner rank={corner_rank}")
    require(multiply(corner, trivial) == zero, "C trivial block survives the corner")
    blocks = (multiply(corner, sign), multiply(corner, standard))
    block_ranks = tuple(rank(block) for block in blocks)
    require(block_ranks == (1, 2), f"C block ranks={block_ranks}")
    for block in blocks:
        require(transpose(block) == block and multiply(block, block) == block,
                "C block self-adjoint idempotence")
    require(multiply(*blocks) == zero and multiply(*reversed(blocks)) == zero,
            "C block orthogonality")
    require(add(*blocks) == corner, "C sum of blocks")

    compressed = tuple(multiply(multiply(corner, regular[g]), corner) for g in group)
    commutator_count = 0
    for left, right in combinations(compressed, 2):
        require(multiply(left, right) == multiply(right, left), "C noncommuting generators")
        commutator_count += 1
    span_dimension = rank(tuple(tuple(entry for row in matrix for entry in row)
                                for matrix in compressed))
    require(span_dimension == 2, f"C Hecke span dimension={span_dimension}")
    print(f"C corner: rank={corner_rank}, block ranks={block_ranks}, "
          f"commutators={commutator_count}, Hecke span dimension={span_dimension}")

    for frame in frames:
        label = f"C (t={frame.t}, m={frame.m})"
        corner_target = corner_rank * frame.target_dim
        corner_source = tuple(corner_rank * dimension for dimension in frame.source_dims)
        source_weights = []
        target_weights = []
        defects = []
        kernel_counts = []
        span_budgets = []
        for block_rank in block_ranks:
            target_dim = block_rank * frame.target_dim
            source_dims = tuple(block_rank * dimension for dimension in frame.source_dims)
            source_dim = sum(source_dims)
            source_ranks = tuple(block_rank * dimension for dimension in frame.source_ranks)
            span_rank = block_rank * frame.span_rank
            source_weight = Fraction(source_dim, sum(corner_source))
            target_weight = Fraction(target_dim, corner_target)
            expected_weight = Fraction(block_rank, corner_rank)
            require(source_weight == target_weight == expected_weight, f"{label} block weights")
            require(all(Fraction(d, whole) == expected_weight
                        for d, whole in zip(source_dims, corner_source)),
                    f"{label} individual source weights")
            kernel_count = sum(d - r for d, r in zip(source_dims, source_ranks))
            span_budget = target_dim - span_rank
            require(source_dims == source_ranks and span_budget == 0,
                    f"{label} kernel={kernel_count}, span budget={span_budget}")
            occupancy_dims = {k: block_rank * dim for k, dim in frame.occupancy_dims.items()}
            _, _, defect = spectral_certificate(
                occupancy_dims, target_dim, source_dim, block_rank * frame.witness_target,
                block_rank * frame.witness_source, f"{label} rank-{block_rank} block"
            )
            require(defect == frame.defect, f"{label} block defect={defect}")
            source_weights.append(source_weight)
            target_weights.append(target_weight)
            defects.append(defect)
            kernel_counts.append(kernel_count)
            span_budgets.append(span_budget)
        require(source_weights == target_weights == [Fraction(1, 3), Fraction(2, 3)],
                f"{label} block balance")
        weighted = sum(weight * defect for weight, defect in zip(source_weights, defects))
        require(weighted == frame.defect, f"{label} weighted defect={weighted}")
        print(f"{label}: source weights={','.join(map(str, source_weights))}, "
              f"target weights={','.join(map(str, target_weights))}, "
              f"kernels={kernel_counts}, span budgets={span_budgets}, "
              f"block defects={','.join(map(str, defects))}, weighted defect={weighted}")


def is_p_integral(matrix, p):
    return all(entry.denominator % p != 0 for row in matrix for entry in row)


def audit_mirabolic():
    cases = ((1, 2), (1, 3), (1, 5), (2, 2), (2, 3))
    total_before = 0
    total_after = 0
    total_integral = 0
    for k, p in cases:
        basis_rows = [list(row) for row in identity(k + 1)]
        basis_rows[0][1] = 1
        basis_rows[1][1] = -p
        basis = tuple(tuple(row) for row in basis_rows)
        basis_inv, _ = inverse_and_determinant(basis)
        z = tuple((int(i == 0),) for i in range(k + 1))
        ell = ((p, 1) + (0,) * (k - 1),)
        before = 0
        after = 0
        integral = 0

        for entries in product(range(p ** 2), repeat=k ** 2):
            before += 1
            determinant = entries[0] if k == 1 else entries[0] * entries[3] - entries[1] * entries[2]
            if determinant % p == 0:
                continue
            after += 1
            local = tuple(entries[start:start + k] for start in range(0, k ** 2, k))
            diagonal = ((1,) + (0,) * k,) + tuple((0,) + row for row in local)
            ambient = multiply(multiply(basis, diagonal), basis_inv)
            ambient_inv, ambient_det = inverse_and_determinant(ambient)
            label = f"D (k={k}, p={p}, C={local})"
            require(multiply(ambient, z) == z, f"{label} does not fix z")
            require(multiply(ell, ambient) == ell, f"{label} does not fix ell")
            require(ambient_det == determinant, f"{label} det G={ambient_det}")
            column_condition = all((row[0] - int(i == 0)) % p == 0
                                   for i, row in enumerate(local))
            ambient_integral = is_p_integral(ambient, p)
            inverse_integral = is_p_integral(ambient_inv, p)
            require(ambient_integral == inverse_integral == column_condition,
                    f"{label} integral={ambient_integral}, inverse integral={inverse_integral}, "
                    f"column test={column_condition}")
            integral += ambient_integral and inverse_integral

        total_before += before
        total_after += after
        total_integral += integral
        print(f"D (k={k}, p={p}): before={before}, retained={after}, integral={integral}")

    totals = (total_before, total_after, total_integral)
    require(totals == (6855, 4012, 528), f"D totals {totals}")
    print(f"D totals: before={total_before}, retained={total_after}, integral={total_integral}")


def main():
    print("NON-CANONICAL Round 9 finite audit (status ceiling candidate-C)")
    try:
        frames = audit_affine_families()
        audit_averaging(frames[0])
        audit_hecke(frames)
        audit_mirabolic()
    except AuditFailure as error:
        print(f"FAIL A-D: {error}", flush=True)
        return 1
    except Exception:
        print("FAIL A-D: unexpected implementation error", flush=True)
        raise
    print("PASS A-D: all preregistered finite checks passed", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
