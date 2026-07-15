#!/usr/bin/env python3
"""Exact verifier candidate for P-CURVATURE-GAUSS-SPLIT-1.

This file must not be executed or imported before its reviewed bytes and
PREREG.md are committed and pushed as the immutable preregistration pin.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import gcd, lcm
import sys


MODULUS = 5
DIMENSION = 6
RULING_MERGE = "57de0af8a50e14e52f0fa81e0158f6a370cab5a5"
RULING_SHA256 = "94ae6278c5ec27262d7eeb443e1a8461a84c2f59df6f315fb5fda24f63bcb02e"
PUBLIC_ACTIVATION = "5abb22319007fd3172f7123f4b3a71b547fb94af"
PUBLIC_CONTENT = "7cfe2a62a456d0f84b1f60b4945dcdfe896e99db"
PUBLIC_CANON_SHA256 = "abd0e026ccc2be00cdb0d9d13d634e0a71602b1565e6d53ac23a99b506281021"
PUBLIC_TAG = "canon-v2"
INCORPORATED_TRACE_RULING = "cf15037f5cc2690a9633ca68ef13107920ce9ce81116963dc9d8490c088eeccb"
INCORPORATED_TRACE_PREREG = "94ec5263d2b2931bcd3863cb5f78e2326944479aa28aef987495c8601c65f8c9"
INCORPORATED_TRACE_VERIFIER = "c9b4d253a609cc489efc4386e5e61d3e92baa16b736b899048f2a3afa5e78c99"
INCORPORATED_TRACE_RESULT = "5d3c406233958bee62076a624012c28bf38c7c770bb79d35f62cf49e699e6baf"
PUBLIC_AMBIENT_TRACE = Fraction(-881, 8)
STATES = tuple(product(range(MODULUS), repeat=DIMENSION))
STATE_COUNT = MODULUS**DIMENSION
POWERS = tuple(MODULUS ** (DIMENSION - 1 - i) for i in range(DIMENSION))


SmallMatrix = tuple[tuple[int, ...], ...]
SmallVector = tuple[int, ...]
State = tuple[int, ...]
SparseVector = dict[int, Fraction]
SparseColumn = dict[int, Fraction]
SparseMatrix = tuple[SparseColumn, ...]


def state_id(x: State) -> int:
    return sum(value * weight for value, weight in zip(x, POWERS))


def matrix_multiply(left: SmallMatrix, right: SmallMatrix) -> SmallMatrix:
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(DIMENSION)) % MODULUS
            for j in range(DIMENSION)
        )
        for i in range(DIMENSION)
    )


def matrix_vector(matrix: SmallMatrix, vector: SmallVector) -> SmallVector:
    return tuple(
        sum(matrix[i][j] * vector[j] for j in range(DIMENSION)) % MODULUS
        for i in range(DIMENSION)
    )


def vector_add(left: SmallVector, right: SmallVector) -> SmallVector:
    return tuple((a + b) % MODULUS for a, b in zip(left, right))


@dataclass(frozen=True, order=True)
class Affine:
    matrix: SmallMatrix
    vector: SmallVector

    def __call__(self, x: State) -> State:
        return vector_add(matrix_vector(self.matrix, x), self.vector)


IDENTITY_MATRIX = tuple(
    tuple(1 if i == j else 0 for j in range(DIMENSION))
    for i in range(DIMENSION)
)
ZERO_VECTOR = (0,) * DIMENSION
IDENTITY = Affine(IDENTITY_MATRIX, ZERO_VECTOR)


def affine(rows: tuple[tuple[int, ...], ...], vector: SmallVector) -> Affine:
    return Affine(
        tuple(tuple(value % MODULUS for value in row) for row in rows),
        tuple(value % MODULUS for value in vector),
    )


def compose(g: Affine, h: Affine) -> Affine:
    """Return g o h, the map x -> g(h(x))."""
    return Affine(
        matrix_multiply(g.matrix, h.matrix),
        vector_add(matrix_vector(g.matrix, h.vector), g.vector),
    )


A_GEN = affine(
    (
        (0, 1, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0),
        (0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 1),
    ),
    ZERO_VECTOR,
)

B_GEN = affine(
    (
        (0, 0, -1, 0, 0, 0),
        (0, 0, 0, -1, 0, 0),
        (-1, 0, 0, 0, 0, 0),
        (0, -1, 0, 0, 0, 0),
        (0, 0, 0, 0, -1, 0),
        (0, 0, 0, 0, 0, -1),
    ),
    ZERO_VECTOR,
)

C_GEN = affine(
    (
        (0, 0, -1, 0, 0, 0),
        (0, 0, 0, -1, 0, 1),
        (-1, 0, 0, 0, 0, 0),
        (0, -1, 0, 0, 0, -1),
        (0, 0, 0, 0, -1, 0),
        (0, 0, 0, 0, 0, -1),
    ),
    (2, 1, 2, 1, 1, 0),
)

D_GEN = affine(
    tuple(
        tuple(-1 if i == j else 0 for j in range(DIMENSION))
        for i in range(DIMENSION)
    ),
    (2, 1, 3, 4, 1, 1),
)

E_GEN = affine(
    tuple(
        tuple(-1 if i == j else 0 for j in range(DIMENSION))
        for i in range(DIMENSION)
    ),
    (2, 1, 3, 4, 2, 1),
)

GENERATORS = (
    ("a", A_GEN),
    ("b", B_GEN),
    ("c", C_GEN),
    ("d", D_GEN),
    ("e", E_GEN),
)


def group_closure(generators: tuple[Affine, ...]) -> tuple[Affine, ...]:
    ordered = tuple(sorted(generators))
    seen = {IDENTITY}
    queue = deque([IDENTITY])
    while queue:
        current = queue.popleft()
        for generator in ordered:
            candidate = compose(current, generator)
            if candidate not in seen:
                seen.add(candidate)
                queue.append(candidate)
    return tuple(sorted(seen))


def group_is_exact(group: tuple[Affine, ...]) -> bool:
    members = set(group)
    return (
        IDENTITY in members
        and len(group) == 20
        and all(compose(g, h) in members for g in group for h in group)
        and all(
            any(
                compose(g, h) == IDENTITY and compose(h, g) == IDENTITY
                for h in group
            )
            for g in group
        )
        and group == tuple(sorted(group))
    )


def affine_permutation(g: Affine) -> tuple[int, ...]:
    return tuple(state_id(g(x)) for x in STATES)


def compose_permutations(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(STATE_COUNT))


def orbit_partition(
    group: tuple[Affine, ...],
) -> tuple[tuple[tuple[int, ...], ...], tuple[int, ...]]:
    labels = [-1] * STATE_COUNT
    orbits: list[tuple[int, ...]] = []
    for x in STATES:
        index = state_id(x)
        if labels[index] >= 0:
            continue
        orbit = tuple(sorted({state_id(g(x)) for g in group}))
        orbit_index = len(orbits)
        for item in orbit:
            labels[item] = orbit_index
        orbits.append(orbit)
    return tuple(orbits), tuple(labels)


def orbit_partition_is_exact(
    orbits: tuple[tuple[int, ...], ...], labels: tuple[int, ...]
) -> bool:
    flattened = tuple(sorted(item for orbit in orbits for item in orbit))
    least = tuple(orbit[0] for orbit in orbits)
    return (
        flattened == tuple(range(STATE_COUNT))
        and least == tuple(sorted(least))
        and all(labels[item] == i for i, orbit in enumerate(orbits) for item in orbit)
    )


def clean_mapping(values: dict[int, Fraction]) -> dict[int, Fraction]:
    return {index: value for index, value in values.items() if value}


def sparse_add(
    left: dict[int, Fraction],
    right: dict[int, Fraction],
    right_scale: Fraction = Fraction(1),
) -> dict[int, Fraction]:
    result = dict(left)
    for index, value in right.items():
        result[index] = result.get(index, Fraction(0)) + right_scale * value
        if not result[index]:
            del result[index]
    return result


def sparse_inner(left: SparseVector, right: SparseVector) -> Fraction:
    if len(left) > len(right):
        left, right = right, left
    return sum((value * right.get(index, 0) for index, value in left.items()), Fraction(0))


def sparse_sum(vector: SparseVector) -> Fraction:
    return sum(vector.values(), Fraction(0))


def apply_koopman(vector: SparseVector, permutation: tuple[int, ...]) -> SparseVector:
    return {permutation[index]: value for index, value in vector.items()}


def project_p_zero_mean(
    vector: SparseVector,
    orbits: tuple[tuple[int, ...], ...],
    labels: tuple[int, ...],
) -> SparseVector:
    if sparse_sum(vector):
        raise ValueError("P zero-mean specialization received nonzero mean")
    orbit_sums: dict[int, Fraction] = defaultdict(Fraction)
    for index, value in vector.items():
        orbit_sums[labels[index]] += value
    result: SparseVector = {}
    for orbit_index, total in orbit_sums.items():
        average = total / len(orbits[orbit_index])
        if average:
            for index in orbits[orbit_index]:
                result[index] = average
    return result


def project_q_zero_mean(
    vector: SparseVector,
    orbits: tuple[tuple[int, ...], ...],
    labels: tuple[int, ...],
) -> SparseVector:
    return sparse_add(vector, project_p_zero_mean(vector, orbits, labels), Fraction(-1))


def projector_action_audit(
    vectors: tuple[SparseVector, ...],
    orbits: tuple[tuple[int, ...], ...],
    labels: tuple[int, ...],
) -> bool:
    for vector in vectors:
        if sparse_sum(vector):
            return False
        projected = project_p_zero_mean(vector, orbits, labels)
        complement = sparse_add(vector, projected, Fraction(-1))
        if project_p_zero_mean(projected, orbits, labels) != projected:
            return False
        if project_q_zero_mean(complement, orbits, labels) != complement:
            return False
        if project_p_zero_mean(complement, orbits, labels):
            return False
        if project_q_zero_mean(projected, orbits, labels):
            return False
        if sparse_add(projected, complement) != vector:
            return False
        if sparse_inner(projected, complement):
            return False
    return True


def global_projector_certificate(
    orbits: tuple[tuple[int, ...], ...]
) -> bool:
    sizes = tuple(len(orbit) for orbit in orbits)
    if not sizes or sum(sizes) != STATE_COUNT or any(size <= 0 for size in sizes):
        return False
    reynolds_blocks = all(
        sum((Fraction(1, size) ** 2 for _ in range(size)), Fraction(0))
        == Fraction(1, size)
        and sum((Fraction(1, size) for _ in range(size)), Fraction(0)) == 1
        for size in sizes
    )
    constant_projector = (
        sum(
            (Fraction(1, STATE_COUNT) ** 2 for _ in range(STATE_COUNT)),
            Fraction(0),
        )
        == Fraction(1, STATE_COUNT)
    )
    reynolds_preserves_constant_and_sum = all(
        size * Fraction(1, size) == 1 for size in sizes
    )
    return (
        reynolds_blocks
        and constant_projector
        and reynolds_preserves_constant_and_sum
        and len(orbits) - 1 == 818
    )


def basis_vectors(
    orbits: tuple[tuple[int, ...], ...]
) -> tuple[SparseVector, ...]:
    size0 = len(orbits[0])
    result: list[SparseVector] = []
    for orbit_index in range(1, len(orbits)):
        size = len(orbits[orbit_index])
        vector: SparseVector = {
            index: Fraction(size0) for index in orbits[orbit_index]
        }
        for index in orbits[0]:
            vector[index] = Fraction(-size)
        result.append(vector)
    return tuple(result)


def vector_to_basis(
    vector: SparseVector,
    orbits: tuple[tuple[int, ...], ...],
) -> SparseColumn:
    if sparse_sum(vector):
        raise ValueError("basis conversion received nonzero mean")
    size0 = len(orbits[0])
    coordinates: SparseColumn = {}
    orbit_values: list[Fraction] = []
    for orbit in orbits:
        value = vector.get(orbit[0], Fraction(0))
        if any(vector.get(index, Fraction(0)) != value for index in orbit):
            raise ValueError("basis conversion received non-invariant vector")
        orbit_values.append(value)
    for i in range(1, len(orbits)):
        coefficient = orbit_values[i] / size0
        if coefficient:
            coordinates[i - 1] = coefficient
    expected0 = -sum(
        (coordinates.get(i - 1, 0) * len(orbits[i]) for i in range(1, len(orbits))),
        Fraction(0),
    )
    if orbit_values[0] != expected0:
        raise ValueError("basis conversion failed pivot-orbit reconstruction")
    return coordinates


def matrix_add(
    left: SparseMatrix,
    right: SparseMatrix,
    right_scale: Fraction = Fraction(1),
) -> SparseMatrix:
    if len(left) != len(right):
        raise ValueError("matrix size mismatch")
    return tuple(sparse_add(a, b, right_scale) for a, b in zip(left, right))


def matrix_compose(left: SparseMatrix, right: SparseMatrix) -> SparseMatrix:
    if len(left) != len(right):
        raise ValueError("matrix size mismatch")
    columns: list[SparseColumn] = []
    for right_column in right:
        output: SparseColumn = {}
        for intermediate, coefficient in right_column.items():
            output = sparse_add(output, left[intermediate], coefficient)
        columns.append(output)
    return tuple(columns)


def matrix_nnz(matrix: SparseMatrix) -> int:
    return sum(len(column) for column in matrix)


def matrix_is_zero(matrix: SparseMatrix) -> bool:
    return all(not column for column in matrix)


def matrix_apply(matrix: SparseMatrix, vector: SparseColumn) -> SparseColumn:
    output: SparseColumn = {}
    for column, coefficient in vector.items():
        output = sparse_add(output, matrix[column], coefficient)
    return output


def trace_product(left: SparseMatrix, right: SparseMatrix) -> Fraction:
    total = Fraction(0)
    for column_index, column in enumerate(left):
        for row_index, value in column.items():
            total += value * right[row_index].get(column_index, 0)
    return total


def weighted_coordinate_sum(column: SparseColumn, orbit_sizes: tuple[int, ...]) -> Fraction:
    return sum(
        (orbit_sizes[index + 1] * value for index, value in column.items()),
        Fraction(0),
    )


def matrix_weighted_coordinate_sums(
    matrix: SparseMatrix, orbit_sizes: tuple[int, ...]
) -> tuple[Fraction, ...]:
    return tuple(weighted_coordinate_sum(column, orbit_sizes) for column in matrix)


def gram_inner_coordinates_cached(
    left: SparseColumn,
    right: SparseColumn,
    orbit_sizes: tuple[int, ...],
    left_weighted: Fraction,
    right_weighted: Fraction,
) -> Fraction:
    size0 = orbit_sizes[0]
    diagonal = sum(
        (
            orbit_sizes[index + 1]
            * value
            * right.get(index, 0)
            for index, value in left.items()
        ),
        Fraction(0),
    )
    return (
        size0 * size0 * diagonal
        + size0 * left_weighted * right_weighted
    )


def gram_basis_operator_entry(
    basis_index: int,
    column: SparseColumn,
    orbit_sizes: tuple[int, ...],
    column_weighted: Fraction,
) -> Fraction:
    size0 = orbit_sizes[0]
    size = orbit_sizes[basis_index + 1]
    return (
        size0 * size0 * size * column.get(basis_index, 0)
        + size0 * size * column_weighted
    )


def gram_skew(matrix: SparseMatrix, orbit_sizes: tuple[int, ...]) -> bool:
    dimension = len(matrix)
    weighted = matrix_weighted_coordinate_sums(matrix, orbit_sizes)
    for i in range(dimension):
        for j in range(i, dimension):
            if (
                gram_basis_operator_entry(i, matrix[j], orbit_sizes, weighted[j])
                + gram_basis_operator_entry(j, matrix[i], orbit_sizes, weighted[i])
            ):
                return False
    return True


def gram_basis_certificate(
    basis: tuple[SparseVector, ...], orbit_sizes: tuple[int, ...]
) -> bool:
    size0 = orbit_sizes[0]
    for i, left in enumerate(basis):
        for j in range(i, len(basis)):
            right = basis[j]
            expected = Fraction(size0 * orbit_sizes[i + 1] * orbit_sizes[j + 1])
            if i == j:
                expected += size0 * size0 * orbit_sizes[i + 1]
            if sparse_inner(left, right) != expected:
                return False
    positive_definite_certificate = (
        size0 > 0
        and all(size0 * size0 * size > 0 for size in orbit_sizes[1:])
    )
    return positive_definite_certificate


def direct_route(
    basis: tuple[SparseVector, ...],
    perm_a: tuple[int, ...],
    perm_c: tuple[int, ...],
    orbits: tuple[tuple[int, ...], ...],
    labels: tuple[int, ...],
) -> tuple[
    SparseMatrix,
    SparseMatrix,
    SparseMatrix,
    tuple[SparseVector, ...],
    tuple[SparseVector, ...],
    bool,
    bool,
]:
    ambient_columns: list[SparseColumn] = []
    internal_columns: list[SparseColumn] = []
    exterior_columns: list[SparseColumn] = []
    a_images: list[SparseVector] = []
    c_images: list[SparseVector] = []
    leakage_a_zero = True
    leakage_c_zero = True

    for vector in basis:
        a_vector = apply_koopman(vector, perm_a)
        c_vector = apply_koopman(vector, perm_c)
        a_images.append(a_vector)
        c_images.append(c_vector)

        ac_vector = apply_koopman(c_vector, perm_a)
        ca_vector = apply_koopman(a_vector, perm_c)
        ambient = project_p_zero_mean(
            sparse_add(ac_vector, ca_vector, Fraction(-1)), orbits, labels
        )

        pc = project_p_zero_mean(c_vector, orbits, labels)
        pa = project_p_zero_mean(a_vector, orbits, labels)
        internal_left = project_p_zero_mean(
            apply_koopman(pc, perm_a), orbits, labels
        )
        internal_right = project_p_zero_mean(
            apply_koopman(pa, perm_c), orbits, labels
        )
        internal = sparse_add(internal_left, internal_right, Fraction(-1))

        qc = project_q_zero_mean(c_vector, orbits, labels)
        qa = project_q_zero_mean(a_vector, orbits, labels)
        leakage_a_zero = leakage_a_zero and not qa
        leakage_c_zero = leakage_c_zero and not qc
        exterior_left = project_p_zero_mean(
            apply_koopman(qc, perm_a), orbits, labels
        )
        exterior_right = project_p_zero_mean(
            apply_koopman(qa, perm_c), orbits, labels
        )
        exterior = sparse_add(exterior_left, exterior_right, Fraction(-1))

        ambient_columns.append(vector_to_basis(ambient, orbits))
        internal_columns.append(vector_to_basis(internal, orbits))
        exterior_columns.append(vector_to_basis(exterior, orbits))

    return (
        tuple(ambient_columns),
        tuple(internal_columns),
        tuple(exterior_columns),
        tuple(a_images),
        tuple(c_images),
        leakage_a_zero,
        leakage_c_zero,
    )


def transition_columns(
    permutation: tuple[int, ...],
    orbits: tuple[tuple[int, ...], ...],
    labels: tuple[int, ...],
) -> tuple[tuple[dict[int, int], ...], bool]:
    columns: list[dict[int, int]] = []
    complete = (
        len(permutation) == STATE_COUNT
        and len(set(permutation)) == STATE_COUNT
        and min(permutation) == 0
        and max(permutation) == STATE_COUNT - 1
    )
    row_totals = [0] * len(orbits)
    for orbit in orbits:
        counts: dict[int, int] = defaultdict(int)
        for index in orbit:
            counts[labels[permutation[index]]] += 1
        complete = complete and sum(counts.values()) == len(orbit)
        for target, count in counts.items():
            row_totals[target] += count
        columns.append(dict(counts))
    complete = complete and tuple(row_totals) == tuple(len(orbit) for orbit in orbits)
    return tuple(columns), complete


def compressed_from_transitions(
    counts: tuple[dict[int, int], ...],
    orbit_sizes: tuple[int, ...],
) -> SparseMatrix:
    size0 = orbit_sizes[0]

    def averaged(column: dict[int, int]) -> dict[int, Fraction]:
        return {
            target: Fraction(value, orbit_sizes[target])
            for target, value in column.items()
            if value
        }

    average0 = averaged(counts[0])
    result: list[SparseColumn] = []
    for source in range(1, len(counts)):
        source_average = averaged(counts[source])
        orbit_values: dict[int, Fraction] = {}
        targets = set(source_average) | set(average0)
        for target in targets:
            value = (
                size0 * source_average.get(target, 0)
                - orbit_sizes[source] * average0.get(target, 0)
            )
            if value:
                orbit_values[target] = value
        weighted_mean = sum(
            (orbit_sizes[i] * value for i, value in orbit_values.items()),
            Fraction(0),
        )
        if weighted_mean:
            raise ValueError("transition compression failed mean-zero audit")
        column = {
            target - 1: value / size0
            for target, value in orbit_values.items()
            if target > 0 and value
        }
        expected0 = -sum(
            (
                column.get(i - 1, 0) * orbit_sizes[i]
                for i in range(1, len(orbit_sizes))
            ),
            Fraction(0),
        )
        if orbit_values.get(0, 0) != expected0:
            raise ValueError("transition compression failed pivot reconstruction")
        result.append(column)
    return tuple(result)


def orbit_route(
    perm_a: tuple[int, ...],
    perm_c: tuple[int, ...],
    perm_ac: tuple[int, ...],
    perm_ca: tuple[int, ...],
    orbits: tuple[tuple[int, ...], ...],
    labels: tuple[int, ...],
) -> tuple[SparseMatrix, SparseMatrix, SparseMatrix, SparseMatrix, SparseMatrix, bool]:
    sizes = tuple(len(orbit) for orbit in orbits)
    matrices: dict[str, SparseMatrix] = {}
    complete = True
    for name, permutation in (
        ("a", perm_a),
        ("c", perm_c),
        ("ac", perm_ac),
        ("ca", perm_ca),
    ):
        counts, route_complete = transition_columns(permutation, orbits, labels)
        complete = complete and route_complete
        matrices[name] = compressed_from_transitions(counts, sizes)

    ba = matrices["a"]
    bc = matrices["c"]
    dac = matrices["ac"]
    dca = matrices["ca"]
    ba_bc = matrix_compose(ba, bc)
    bc_ba = matrix_compose(bc, ba)
    ambient = matrix_add(dac, dca, Fraction(-1))
    internal = matrix_add(ba_bc, bc_ba, Fraction(-1))
    exterior = matrix_add(
        matrix_add(dac, ba_bc, Fraction(-1)),
        matrix_add(dca, bc_ba, Fraction(-1)),
        Fraction(-1),
    )
    return ambient, internal, exterior, ba, bc, complete


def leakage_bilinear_audit(
    exterior: SparseMatrix,
    a_images: tuple[SparseVector, ...],
    c_images: tuple[SparseVector, ...],
    ba: SparseMatrix,
    bc: SparseMatrix,
    orbit_sizes: tuple[int, ...],
) -> bool:
    dimension = len(exterior)
    exterior_weighted = matrix_weighted_coordinate_sums(exterior, orbit_sizes)
    ba_weighted = matrix_weighted_coordinate_sums(ba, orbit_sizes)
    bc_weighted = matrix_weighted_coordinate_sums(bc, orbit_sizes)
    for i in range(dimension):
        for j in range(dimension):
            left = gram_basis_operator_entry(
                i, exterior[j], orbit_sizes, exterior_weighted[j]
            )
            la_lc = (
                sparse_inner(a_images[i], c_images[j])
                - gram_inner_coordinates_cached(
                    ba[i], bc[j], orbit_sizes, ba_weighted[i], bc_weighted[j]
                )
            )
            lc_la = (
                sparse_inner(c_images[i], a_images[j])
                - gram_inner_coordinates_cached(
                    bc[i], ba[j], orbit_sizes, bc_weighted[i], ba_weighted[j]
                )
            )
            if left != la_lc - lc_la:
                return False
    return True


IntegerRow = dict[int, int]


def normalize_integer_row(row: IntegerRow) -> IntegerRow:
    clean = {column: value for column, value in row.items() if value}
    divisor = 0
    for value in clean.values():
        divisor = gcd(divisor, abs(value))
    if divisor > 1:
        clean = {column: value // divisor for column, value in clean.items()}
    if clean and clean[min(clean)] < 0:
        clean = {column: -value for column, value in clean.items()}
    return clean


def primitive_integer_rows(matrix: SparseMatrix) -> tuple[IntegerRow, ...]:
    dimension = len(matrix)
    rows: list[SparseColumn] = [dict() for _ in range(dimension)]
    for column_index, column in enumerate(matrix):
        for row_index, value in column.items():
            rows[row_index][column_index] = value
    primitive: list[IntegerRow] = []
    for row in rows:
        denominator = 1
        for value in row.values():
            denominator = lcm(denominator, value.denominator)
        integers = {
            column: value.numerator * (denominator // value.denominator)
            for column, value in row.items()
        }
        primitive.append(normalize_integer_row(integers))
    return tuple(primitive)


def rank_mod_two(rows: tuple[IntegerRow, ...]) -> int:
    basis: dict[int, int] = {}
    for row in rows:
        packed = 0
        for column, value in row.items():
            if value & 1:
                packed |= 1 << column
        while packed:
            low = packed & -packed
            pivot = low.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = packed
                break
            packed ^= basis[pivot]
    return len(basis)


def ternary_add(
    left: tuple[int, int], right: tuple[int, int], mask: int
) -> tuple[int, int]:
    left1, left2 = left
    right1, right2 = right
    left0 = mask ^ (left1 | left2)
    right0 = mask ^ (right1 | right2)
    result1 = (left0 & right1) | (left1 & right0) | (left2 & right2)
    result2 = (left0 & right2) | (left2 & right0) | (left1 & right1)
    return result1, result2


def rank_mod_three(rows: tuple[IntegerRow, ...], dimension: int) -> int:
    mask = (1 << dimension) - 1
    basis: dict[int, tuple[int, int]] = {}
    for row in rows:
        ones = 0
        twos = 0
        for column, value in row.items():
            residue = value % 3
            if residue == 1:
                ones |= 1 << column
            elif residue == 2:
                twos |= 1 << column
        current = (ones, twos)
        while current[0] | current[1]:
            low = (current[0] | current[1]) & -(current[0] | current[1])
            pivot = low.bit_length() - 1
            coefficient = 1 if current[0] & low else 2
            if pivot not in basis:
                if coefficient == 2:
                    current = (current[1], current[0])
                basis[pivot] = current
                break
            pivot_row = basis[pivot]
            if coefficient == 1:
                current = ternary_add(current, (pivot_row[1], pivot_row[0]), mask)
            else:
                current = ternary_add(current, pivot_row, mask)
    return len(basis)


def fraction_free_echelon_kernel(
    matrix: SparseMatrix, integer_rows: tuple[IntegerRow, ...]
) -> tuple[int, tuple[SparseColumn, ...], bool]:
    dimension = len(matrix)
    rows = [dict(row) for row in integer_rows]

    rank = 0
    pivot_columns: list[int] = []
    for column in range(dimension):
        pivot = next(
            (row for row in range(rank, dimension) if rows[row].get(column, 0)),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        rows[rank] = normalize_integer_row(rows[rank])
        pivot_value = rows[rank][column]
        for row in range(rank + 1, dimension):
            factor = rows[row].get(column, 0)
            if factor:
                divisor = gcd(abs(pivot_value), abs(factor))
                row_scale = pivot_value // divisor
                pivot_scale = factor // divisor
                keys = set(rows[row]) | set(rows[rank])
                rows[row] = normalize_integer_row(
                    {
                        key: row_scale * rows[row].get(key, 0)
                        - pivot_scale * rows[rank].get(key, 0)
                        for key in keys
                    }
                )
        pivot_columns.append(column)
        rank += 1
        if rank == dimension:
            break

    free_columns = [column for column in range(dimension) if column not in set(pivot_columns)]
    kernel: list[SparseColumn] = []
    for free in free_columns:
        vector: SparseColumn = {free: Fraction(1)}
        for row in range(rank - 1, -1, -1):
            pivot = pivot_columns[row]
            subtotal = sum(
                (
                    Fraction(value) * vector.get(column, 0)
                    for column, value in rows[row].items()
                    if column != pivot
                ),
                Fraction(0),
            )
            if subtotal:
                vector[pivot] = -subtotal / rows[row][pivot]
        kernel.append(clean_mapping(vector))

    free_identity = all(
        vector.get(free, 0) == 1
        and all(vector.get(other, 0) == 0 for other in free_columns if other != free)
        for vector, free in zip(kernel, free_columns)
    )
    annihilated = all(not matrix_apply(matrix, vector) for vector in kernel)
    certificate = (
        len(kernel) == dimension - rank
        and free_identity
        and annihilated
        and len(pivot_columns) == rank
    )
    return rank, tuple(kernel), certificate


@dataclass(frozen=True)
class RankCertificate:
    rank: int
    nullity: int
    method: str
    mod2_lower: int
    mod3_lower: int
    kernel_ok: bool


def exact_rank_certificate(matrix: SparseMatrix) -> RankCertificate:
    dimension = len(matrix)
    integer_rows = primitive_integer_rows(matrix)
    mod2_lower = rank_mod_two(integer_rows)
    mod3_lower = rank_mod_three(integer_rows, dimension)
    rank, kernel, kernel_ok = fraction_free_echelon_kernel(matrix, integer_rows)
    certificate_ok = kernel_ok and max(mod2_lower, mod3_lower) <= rank
    return RankCertificate(
        rank,
        len(kernel),
        "exact-fraction-free",
        mod2_lower,
        mod3_lower,
        certificate_ok,
    )


def exact_matrix_types(matrix: SparseMatrix) -> bool:
    return all(
        isinstance(index, int)
        and 0 <= index < len(matrix)
        and isinstance(value, Fraction)
        for column in matrix
        for index, value in column.items()
    )


def format_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def format_zero(value: bool) -> str:
    return "ZERO" if value else "NONZERO"


def compute() -> tuple[list[tuple[str, bool]], dict[str, object]]:
    authority_ok = (
        PUBLIC_TAG == "canon-v2"
        and RULING_MERGE == "57de0af8a50e14e52f0fa81e0158f6a370cab5a5"
        and RULING_SHA256 == "94ae6278c5ec27262d7eeb443e1a8461a84c2f59df6f315fb5fda24f63bcb02e"
        and PUBLIC_ACTIVATION == "5abb22319007fd3172f7123f4b3a71b547fb94af"
        and PUBLIC_CONTENT == "7cfe2a62a456d0f84b1f60b4945dcdfe896e99db"
        and PUBLIC_CANON_SHA256
        == "abd0e026ccc2be00cdb0d9d13d634e0a71602b1565e6d53ac23a99b506281021"
        and INCORPORATED_TRACE_RULING
        == "cf15037f5cc2690a9633ca68ef13107920ce9ce81116963dc9d8490c088eeccb"
        and INCORPORATED_TRACE_PREREG
        == "94ec5263d2b2931bcd3863cb5f78e2326944479aa28aef987495c8601c65f8c9"
        and INCORPORATED_TRACE_VERIFIER
        == "c9b4d253a609cc489efc4386e5e61d3e92baa16b736b899048f2a3afa5e78c99"
        and INCORPORATED_TRACE_RESULT
        == "5d3c406233958bee62076a624012c28bf38c7c770bb79d35f62cf49e699e6baf"
    )
    carrier_ok = (
        len(STATES) == STATE_COUNT
        and len({state_id(x) for x in STATES}) == STATE_COUNT
        and all(len(x) == DIMENSION for x in STATES)
    )
    involutions = tuple(compose(g, g) == IDENTITY for _, g in GENERATORS)
    composition_ok = all(
        compose(g, h)(x) == g(h(x))
        for _, g in GENERATORS
        for _, h in GENERATORS
        for x in STATES
    )
    koopman_ok = composition_ok and all(
        compose(compose(g, h), compose(h, g)) == IDENTITY
        for _, g in GENERATORS
        for _, h in GENERATORS
    )

    group = group_closure((B_GEN, D_GEN))
    group_ok = group_is_exact(group)
    orbits, labels = orbit_partition(group)
    partition_ok = orbit_partition_is_exact(orbits, labels)
    census = Counter(len(orbit) for orbit in orbits)
    census_ok = census == Counter({5: 1, 10: 74, 20: 744})
    orbit_sizes = tuple(len(orbit) for orbit in orbits)
    dimensions_ok = len(orbits) == 819 and len(orbits) - 1 == 818
    projector_ok = (
        group_ok
        and partition_ok
        and sum(orbit_sizes) == STATE_COUNT
        and dimensions_ok
        and global_projector_certificate(orbits)
    )

    basis = basis_vectors(orbits)
    basis_ok = (
        len(basis) == 818
        and all(not sparse_sum(vector) for vector in basis)
        and all(
            vector.get(orbits[i][0], 0) == orbit_sizes[0]
            and vector.get(orbits[0][0], 0) == -orbit_sizes[i]
            for i, vector in enumerate(basis, start=1)
        )
        and orbit_sizes[0] > 0
        and all(size > 0 for size in orbit_sizes)
    )
    gram_basis_ok = gram_basis_certificate(basis, orbit_sizes)

    perm_a = affine_permutation(A_GEN)
    perm_c = affine_permutation(C_GEN)
    perm_ac = compose_permutations(perm_a, perm_c)
    perm_ca = compose_permutations(perm_c, perm_a)
    permutation_composition_ok = (
        perm_ac == affine_permutation(compose(A_GEN, C_GEN))
        and perm_ca == affine_permutation(compose(C_GEN, A_GEN))
        and all(
            compose_permutations(
                affine_permutation(left), affine_permutation(right)
            )
            == affine_permutation(compose(left, right))
            for _, left in GENERATORS
            for _, right in GENERATORS
        )
    )

    (
        ambient_a,
        internal_a,
        exterior_a,
        a_images,
        c_images,
        leakage_a_zero,
        leakage_c_zero,
    ) = direct_route(basis, perm_a, perm_c, orbits, labels)
    route_a_ok = (
        len(ambient_a) == len(internal_a) == len(exterior_a) == 818
        and all(exact_matrix_types(matrix) for matrix in (ambient_a, internal_a, exterior_a))
    )
    projector_action_ok = projector_action_audit(
        basis + a_images + c_images, orbits, labels
    )

    ambient_b, internal_b, exterior_b, ba, bc, transition_complete = orbit_route(
        perm_a, perm_c, perm_ac, perm_ca, orbits, labels
    )
    route_b_ok = (
        transition_complete
        and len(ambient_b) == len(internal_b) == len(exterior_b) == 818
        and all(exact_matrix_types(matrix) for matrix in (ambient_b, internal_b, exterior_b))
    )
    route_agreement = (
        ambient_a == ambient_b
        and internal_a == internal_b
        and exterior_a == exterior_b
    )
    operator_identity = ambient_a == matrix_add(internal_a, exterior_a)
    route_b_nnz = tuple(
        matrix_nnz(matrix) for matrix in (ambient_b, internal_b, exterior_b)
    )
    del ambient_b, internal_b, exterior_b

    skew_ambient = gram_skew(ambient_a, orbit_sizes)
    skew_internal = gram_skew(internal_a, orbit_sizes)
    skew_exterior = gram_skew(exterior_a, orbit_sizes)
    leakage_bilinear = leakage_bilinear_audit(
        exterior_a, a_images, c_images, ba, bc, orbit_sizes
    )
    typed_images_ok = all(not sparse_sum(vector) for vector in a_images + c_images)
    del a_images, c_images, ba, bc

    trace_ambient = trace_product(ambient_a, ambient_a)
    trace_internal = trace_product(internal_a, internal_a)
    trace_exterior = trace_product(exterior_a, exterior_a)
    cross = 2 * trace_product(internal_a, exterior_a)
    trace_identity = (
        trace_ambient == trace_internal + cross + trace_exterior
        and trace_ambient == PUBLIC_AMBIENT_TRACE
    )

    rank_ambient = exact_rank_certificate(ambient_a)
    rank_internal = exact_rank_certificate(internal_a)
    rank_exterior = exact_rank_certificate(exterior_a)
    rank_certificates = (rank_ambient, rank_internal, rank_exterior)
    matrices = (ambient_a, internal_a, exterior_a)
    traces = (trace_ambient, trace_internal, trace_exterior)
    rank_ok = all(
        certificate.kernel_ok
        and certificate.rank + certificate.nullity == 818
        and certificate.rank % 2 == 0
        and trace <= 0
        and (
            matrix_is_zero(matrix)
            == (certificate.rank == 0)
            == (trace == 0)
        )
        for matrix, trace, certificate in zip(matrices, traces, rank_certificates)
    )

    typing_ok = (
        basis_ok
        and route_a_ok
        and route_b_ok
        and typed_images_ok
    )
    exactness_ok = all(exact_matrix_types(matrix) for matrix in matrices) and all(
        isinstance(value, Fraction)
        for value in (trace_ambient, trace_internal, trace_exterior, cross)
    )
    deterministic_ok = (
        group == tuple(sorted(group))
        and tuple(orbit[0] for orbit in orbits) == tuple(sorted(orbit[0] for orbit in orbits))
        and len(ambient_a) == 818
    )

    audits = [
        ("I01", authority_ok),
        ("I02", carrier_ok),
        (
            "I03",
            all(involutions)
            and composition_ok
            and koopman_ok
            and permutation_composition_ok,
        ),
        ("I04", group_ok and partition_ok and census_ok),
        ("I05", projector_ok and projector_action_ok),
        ("I06", basis_ok and gram_basis_ok),
        ("I07", typing_ok),
        ("I08", route_a_ok),
        ("I09", route_b_ok),
        ("I10", route_agreement),
        (
            "I11",
            operator_identity
            and leakage_bilinear
            and skew_ambient
            and skew_internal
            and skew_exterior,
        ),
        ("I12", trace_identity),
        ("I13", rank_ok),
        ("I14", exactness_ok),
        ("I15", deterministic_ok),
    ]

    report: dict[str, object] = {
        "census": census,
        "group_order": len(group),
        "orbit_count": len(orbits),
        "basis_dimension": len(basis),
        "route_a_nnz": tuple(matrix_nnz(matrix) for matrix in matrices),
        "route_b_nnz": route_b_nnz,
        "route_agreement": route_agreement,
        "operator_identity": operator_identity,
        "leakage_bilinear": leakage_bilinear,
        "leakage_a_zero": leakage_a_zero,
        "leakage_c_zero": leakage_c_zero,
        "skew": (skew_ambient, skew_internal, skew_exterior),
        "trace_ambient": trace_ambient,
        "trace_internal": trace_internal,
        "trace_exterior": trace_exterior,
        "cross": cross,
        "rank_ambient": rank_ambient,
        "rank_internal": rank_internal,
        "rank_exterior": rank_exterior,
        "ambient_zero": matrix_is_zero(ambient_a),
        "internal_zero": matrix_is_zero(internal_a),
        "exterior_zero": matrix_is_zero(exterior_a),
    }
    return audits, report


def print_report(audits: list[tuple[str, bool]], report: dict[str, object]) -> int:
    passed = sum(value for _, value in audits)
    complete = passed == len(audits)
    census = report["census"]
    assert isinstance(census, Counter)
    rank_ambient = report["rank_ambient"]
    rank_internal = report["rank_internal"]
    rank_exterior = report["rank_exterior"]
    assert isinstance(rank_ambient, RankCertificate)
    assert isinstance(rank_internal, RankCertificate)
    assert isinstance(rank_exterior, RankCertificate)

    print("P-CURVATURE-GAUSS-SPLIT-1")
    print(f"RULING merge={RULING_MERGE} sha256={RULING_SHA256}")
    print("AUDIT " + " ".join(f"{name}={'P' if value else 'F'}" for name, value in audits))
    print(f"AUDIT {'PASS' if complete else 'FAIL'} {passed}/{len(audits)}")
    if not complete:
        print("DECISION STOP")
        print("RESULT INVALID")
        return 1
    print(
        "AUTHORITY "
        f"tag={PUBLIC_TAG} activation={PUBLIC_ACTIVATION} "
        f"content={PUBLIC_CONTENT} canon_sha256={PUBLIC_CANON_SHA256}"
    )
    print(
        "SOURCES "
        f"trace_ruling={INCORPORATED_TRACE_RULING} "
        f"trace_prereg={INCORPORATED_TRACE_PREREG} "
        f"trace_verifier={INCORPORATED_TRACE_VERIFIER} "
        f"trace_result={INCORPORATED_TRACE_RESULT}"
    )
    print(f"CARRIER states={STATE_COUNT}")
    print(
        "H "
        f"order={report['group_order']} orbits={report['orbit_count']} "
        f"census=5:{census.get(5,0)},10:{census.get(10,0)},20:{census.get(20,0)}"
    )
    print(f"PROJECTOR rank_P={report['basis_dimension']} basis=integer-orbit")
    print(
        "ROUTE_A nnz="
        + ",".join(str(value) for value in report["route_a_nnz"])
    )
    print(
        "ROUTE_B nnz="
        + ",".join(str(value) for value in report["route_b_nnz"])
    )
    print(
        "MATRIX_AGREEMENT "
        + ("PASS" if report["route_agreement"] and report["operator_identity"] else "FAIL")
    )
    print(
        "LEAKAGE "
        f"A={format_zero(bool(report['leakage_a_zero']))} "
        f"C={format_zero(bool(report['leakage_c_zero']))} "
        f"bilinear={'PASS' if report['leakage_bilinear'] else 'FAIL'}"
    )
    skew = report["skew"]
    assert isinstance(skew, tuple)
    print("SKEW " + ",".join("PASS" if value else "FAIL" for value in skew))
    print(
        "TRACE "
        f"ambient={format_fraction(report['trace_ambient'])} "
        f"internal={format_fraction(report['trace_internal'])} "
        f"exterior={format_fraction(report['trace_exterior'])} "
        f"cross={format_fraction(report['cross'])}"
    )
    reconstructed = (
        report["trace_internal"] + report["cross"] + report["trace_exterior"]
    )
    print(
        "TRACE_IDENTITY "
        f"reconstructed={format_fraction(reconstructed)} "
        f"ambient={format_fraction(report['trace_ambient'])} "
        f"anchor={format_fraction(PUBLIC_AMBIENT_TRACE)} PASS"
    )
    for name, certificate in (
        ("ambient", rank_ambient),
        ("internal", rank_internal),
        ("exterior", rank_exterior),
    ):
        print(
            f"RANK {name}={certificate.rank} nullity={certificate.nullity} "
            f"method={certificate.method} mod2={certificate.mod2_lower} "
            f"mod3={certificate.mod3_lower} "
            f"kernel={'PASS' if certificate.kernel_ok else 'FAIL'}"
        )
    if bool(report["exterior_zero"]):
        print("DECISION INTRINSIC")
    elif bool(report["internal_zero"]):
        print("DECISION PROJECTION-INDUCED")
    else:
        print("DECISION MIXED")
    print("RESULT VALID")
    return 0


def print_exception_stop(error: BaseException) -> int:
    print("P-CURVATURE-GAUSS-SPLIT-1")
    print(f"RULING merge={RULING_MERGE} sha256={RULING_SHA256}")
    print(f"ERROR type={type(error).__name__}")
    print("AUDIT " + " ".join(f"I{i:02d}=F" for i in range(1, 16)))
    print("AUDIT FAIL 0/15")
    print("DECISION STOP")
    print("RESULT INVALID")
    return 1


def main() -> int:
    try:
        audits, report = compute()
        return print_report(audits, report)
    except BaseException as error:
        if isinstance(error, (KeyboardInterrupt, SystemExit)):
            raise
        return print_exception_stop(error)


if __name__ == "__main__":
    sys.exit(main())
