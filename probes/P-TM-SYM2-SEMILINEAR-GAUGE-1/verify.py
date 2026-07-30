#!/usr/bin/env python3
"""Exact verifier for P-TM-SYM2-SEMILINEAR-GAUGE-1.

The program is deliberately self-contained and result-neutral.  It scans the
entire frozen 2 x 48 carrier, decides each homogeneous incidence system in
two independent ways, and derives the scientific route only after checking
all structural certificates.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Sequence


PROBE_ID = "P-TM-SYM2-SEMILINEAR-GAUGE-1"
SOURCE_PREDEFINITION_FILENAME = "SOURCE-PREDEFINITION.md"
SOURCE_MEASURE1_EXPECTED_FILENAME = "SOURCE-MEASURE1-EXPECTED.txt"
SOURCE_PREDEFINITION_SHA256 = (
    "9f5dfe902bb0ff9fc19c4bdc4fb1095301a55bd00201f770ab81a36899c2273f"
)
SOURCE_MEASURE1_EXPECTED_SHA256 = (
    "395209f15d0943f38b1d8af4f6d20769c5e113c65bac9455944613ab3b40726f"
)
SCAN_EXPONENTS = (0, 1)
W_ORDER_THEOREM = 48
SELECTOR_COUNT_THEOREM = 48
SCAN_CASE_COUNT_THEOREM = 96
LINEAR_GAUGE_ORDER_THEOREM = 12
POSSIBLE_GAMMA_ORDERS = (12, 24)
DETERMINANT_GRID = (0, 1, 2, 3)
COSET_CHARACTER_CASES = ((1, 0), (0, 1), (1, 1))
RESIDUAL_INVARIANT_BY_CHARACTER = {
    (1, 0): "chi_F",
    (0, 1): "chi_Q",
    (1, 1): "chi_Q chi_F",
}
SCIENTIFIC_ROUTES = ("LINEAR-ONLY", "SEMILINEAR-DOUBLE")
STOP_ROUTE = "STOP"

SOURCE_SPECS = {
    SOURCE_PREDEFINITION_FILENAME: {
        "sha256": SOURCE_PREDEFINITION_SHA256,
        "bytes": 25896,
        "lf": 776,
        "cr": 0,
        "markers": (
            b"## 7. Semilinear realization group and effective gauge",
            b"## 8. Analytic ceiling, dichotomy, and scientific routes",
            b"## 9. Contract for the future exact scan",
            b"These are all 96",
            b"LINEAR-ONLY",
            b"SEMILINEAR-DOUBLE",
        ),
    },
    SOURCE_MEASURE1_EXPECTED_FILENAME: {
        "sha256": SOURCE_MEASURE1_EXPECTED_SHA256,
        "bytes": 9879,
        "lf": 79,
        "cr": 0,
        "markers": (
            b"AUDIT: line-set projective stabilizer order 60; "
            b"Aut(Lines, sigma_line) order 12",
            b"AUDIT: gauge action free: yes",
            b"B5 ORBIT 4: size 12",
            b"ROUTE: NEGATIVE (N2: the canonicality test returns NONCANONICAL)",
            b"RESULT: PASS (all certificates green in mode --evaluate)",
        ),
    },
}


class StopVerification(Exception):
    """A structural failure; never a scientific route."""


def require(condition: bool, code: str) -> None:
    if not condition:
        raise StopVerification(code)


@dataclass(frozen=True)
class K:
    """An exact element a + b*sqrt(5), with rational a and b."""

    a: Fraction
    b: Fraction

    def __init__(self, a: Any = 0, b: Any = 0) -> None:
        object.__setattr__(self, "a", Fraction(a))
        object.__setattr__(self, "b", Fraction(b))

    @staticmethod
    def coerce(value: Any) -> K:
        if isinstance(value, K):
            return value
        return K(value)

    def __add__(self, other: Any) -> K:
        rhs = K.coerce(other)
        return K(self.a + rhs.a, self.b + rhs.b)

    def __radd__(self, other: Any) -> K:
        return self + other

    def __sub__(self, other: Any) -> K:
        rhs = K.coerce(other)
        return K(self.a - rhs.a, self.b - rhs.b)

    def __rsub__(self, other: Any) -> K:
        return K.coerce(other) - self

    def __neg__(self) -> K:
        return K(-self.a, -self.b)

    def __mul__(self, other: Any) -> K:
        rhs = K.coerce(other)
        return K(
            self.a * rhs.a + 5 * self.b * rhs.b,
            self.a * rhs.b + self.b * rhs.a,
        )

    def __rmul__(self, other: Any) -> K:
        return self * other

    def __truediv__(self, other: Any) -> K:
        rhs = K.coerce(other)
        norm = rhs.a * rhs.a - 5 * rhs.b * rhs.b
        if norm == 0:
            raise ZeroDivisionError("division by zero in Q(sqrt(5))")
        return K(
            (self.a * rhs.a - 5 * self.b * rhs.b) / norm,
            (self.b * rhs.a - self.a * rhs.b) / norm,
        )

    def __rtruediv__(self, other: Any) -> K:
        return K.coerce(other) / self

    def __bool__(self) -> bool:
        return self.a != 0 or self.b != 0

    def tau(self) -> K:
        return K(self.a, -self.b)


ZERO = K(0)
ONE = K(1)
NEG_ONE = K(-1)
SQRT5 = K(0, 1)
PHI = (ONE + SQRT5) / 2

Vector = tuple[K, K, K]
Matrix = tuple[Vector, Vector, Vector]
Permutation = tuple[int, int, int, int, int, int]
WElement = tuple[tuple[int, int, int], tuple[int, int, int]]
Solution = tuple[K, ...]


def qdata(value: K) -> list[int]:
    return [
        value.a.numerator,
        value.a.denominator,
        value.b.numerator,
        value.b.denominator,
    ]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_hash(value: Any) -> str:
    data = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return sha256_bytes(data)


def add_vectors(left: Vector, right: Vector) -> Vector:
    return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value]


def scale_vector(scale: K, vector: Vector) -> Vector:
    return tuple(scale * vector[i] for i in range(3))  # type: ignore[return-value]


def tau_vector(vector: Vector) -> Vector:
    return tuple(value.tau() for value in vector)  # type: ignore[return-value]


def dot(row: Sequence[K], column: Sequence[K]) -> K:
    require(len(row) == len(column), "dot-dimension")
    total = ZERO
    for left, right in zip(row, column):
        total += left * right
    return total


def mat_vec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(dot(row, vector) for row in matrix)  # type: ignore[return-value]


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(3)), ZERO)
            for j in range(3)
        )
        for i in range(3)
    )  # type: ignore[return-value]


def tau_matrix(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(value.tau() for value in row) for row in matrix
    )  # type: ignore[return-value]


def determinant(matrix: Matrix) -> K:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (
        d * h - e * g
    )


def matrix_inverse(matrix: Matrix) -> Matrix:
    det = determinant(matrix)
    require(bool(det), "matrix-inverse-singular")
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return (
        ((e * i - f * h) / det, (c * h - b * i) / det, (b * f - c * e) / det),
        ((f * g - d * i) / det, (a * i - c * g) / det, (c * d - a * f) / det),
        ((d * h - e * g) / det, (b * g - a * h) / det, (a * e - b * d) / det),
    )


def matrix_from_columns(columns: Sequence[Vector]) -> Matrix:
    require(len(columns) == 3, "matrix-column-count")
    return tuple(
        tuple(columns[j][i] for j in range(3)) for i in range(3)
    )  # type: ignore[return-value]


def diagonal(values: Sequence[K]) -> Matrix:
    require(len(values) == 3, "diagonal-size")
    return tuple(
        tuple(values[i] if i == j else ZERO for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def flatten_matrix(matrix: Matrix) -> tuple[K, ...]:
    return tuple(matrix[i][j] for i in range(3) for j in range(3))


def unflatten_matrix(values: Sequence[K]) -> Matrix:
    require(len(values) >= 9, "unflatten-size")
    return tuple(
        tuple(values[3 * i + j] for j in range(3)) for i in range(3)
    )  # type: ignore[return-value]


def normalize_solution(solution: Sequence[K]) -> Solution:
    require(len(solution) == 15, "solution-size")
    pivot = next((solution[i] for i in range(9) if solution[i]), None)
    require(pivot is not None, "solution-zero-matrix")
    return tuple(value / pivot for value in solution)


def normalize_matrix(matrix: Matrix) -> Matrix:
    flat = flatten_matrix(matrix)
    pivot = next((value for value in flat if value), None)
    require(pivot is not None, "normalize-zero-matrix")
    return unflatten_matrix(tuple(value / pivot for value in flat))


def proportional_scalar(left: Vector, right: Vector) -> K | None:
    position = next((i for i, value in enumerate(right) if value), None)
    if position is None:
        return None
    scalar = left[position] / right[position]
    if not scalar:
        return None
    if all(left[i] == scalar * right[i] for i in range(3)):
        return scalar
    return None


def projectively_equal(left: Vector, right: Vector) -> bool:
    return proportional_scalar(left, right) is not None


VECTORS: tuple[Vector, ...] = (
    (ZERO, ONE, PHI),
    (ZERO, ONE, -PHI),
    (ONE, PHI, ZERO),
    (ONE, -PHI, ZERO),
    (PHI, ZERO, ONE),
    (PHI, ZERO, NEG_ONE),
)
SIGMA_LINE: Permutation = (1, 0, 3, 2, 5, 4)


def permutation_parity(permutation: Sequence[int]) -> int:
    inversions = sum(
        1
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
        if permutation[i] > permutation[j]
    )
    return inversions % 2


def compose_permutations(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[i]] for i in range(6))  # type: ignore[return-value]


def inverse_permutation(permutation: Permutation) -> Permutation:
    result = [0] * 6
    for i, image in enumerate(permutation):
        result[image] = i
    return tuple(result)  # type: ignore[return-value]


def w_permutation(element: WElement) -> Permutation:
    pi, delta = element
    return tuple(
        2 * pi[j] + (b ^ delta[j]) for j in range(3) for b in range(2)
    )  # type: ignore[return-value]


def w_compose(left: WElement, right: WElement) -> WElement:
    pi_left, delta_left = left
    pi_right, delta_right = right
    return (
        tuple(pi_left[pi_right[j]] for j in range(3)),
        tuple(
            delta_right[j] ^ delta_left[pi_right[j]] for j in range(3)
        ),
    )  # type: ignore[return-value]


def w_inverse(element: WElement) -> WElement:
    pi, delta = element
    pi_inverse = [0] * 3
    for j, image in enumerate(pi):
        pi_inverse[image] = j
    return (
        tuple(pi_inverse),
        tuple(delta[pi_inverse[k]] for k in range(3)),
    )  # type: ignore[return-value]


def enumerate_w() -> list[WElement]:
    return [
        (tuple(pi), tuple(delta))
        for pi in itertools.permutations(range(3))
        for delta in itertools.product((0, 1), repeat=3)
    ]


def enumerate_selectors() -> list[WElement]:
    return [
        (tuple(pi), tuple(epsilon))
        for pi in itertools.permutations(range(3))
        for epsilon in itertools.product((0, 1), repeat=3)
    ]


def character_pair(element: WElement) -> tuple[int, int]:
    pi, delta = element
    return (permutation_parity(pi), sum(delta) % 2)


def verify_sources(probe_dir: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for filename in (
        SOURCE_PREDEFINITION_FILENAME,
        SOURCE_MEASURE1_EXPECTED_FILENAME,
    ):
        spec = SOURCE_SPECS[filename]
        path = probe_dir / filename
        require(path.is_file() and not path.is_symlink(), f"source-file:{filename}")
        data = path.read_bytes()
        record = {
            "filename": filename,
            "bytes": len(data),
            "lf": data.count(b"\n"),
            "cr": data.count(b"\r"),
            "sha256": sha256_bytes(data),
            "final_lf": data.endswith(b"\n"),
        }
        require(record["bytes"] == spec["bytes"], f"source-bytes:{filename}")
        require(record["lf"] == spec["lf"], f"source-lf:{filename}")
        require(record["cr"] == spec["cr"], f"source-cr:{filename}")
        require(record["sha256"] == spec["sha256"], f"source-sha:{filename}")
        require(record["final_lf"], f"source-final-lf:{filename}")
        for marker in spec["markers"]:
            require(marker in data, f"source-marker:{filename}")
        records.append(record)
    return records


def build_incidence_system(exponent: int, permutation: Permutation) -> list[list[K]]:
    require(exponent in SCAN_EXPONENTS, "incidence-exponent")
    require(sorted(permutation) == list(range(6)), "incidence-permutation")
    rows: list[list[K]] = []
    for line_index, source in enumerate(VECTORS):
        transformed_source = tau_vector(source) if exponent else source
        target = VECTORS[permutation[line_index]]
        for coordinate in range(3):
            row = [ZERO for _ in range(15)]
            for column in range(3):
                row[3 * coordinate + column] = transformed_source[column]
            row[9 + line_index] = -target[coordinate]
            rows.append(row)
    require(len(rows) == 18 and all(len(row) == 15 for row in rows), "incidence-shape")
    return rows


def rref(
    rows: Sequence[Sequence[K]],
) -> tuple[list[list[K]], tuple[int, ...], list[list[K]]]:
    matrix = [list(row) for row in rows]
    if not matrix:
        return matrix, (), []
    width = len(matrix[0])
    require(all(len(row) == width for row in matrix), "rref-ragged")
    transform = [
        [ONE if row == column else ZERO for column in range(len(matrix))]
        for row in range(len(matrix))
    ]
    pivot_row = 0
    pivots: list[int] = []
    for column in range(width):
        candidate = next(
            (row for row in range(pivot_row, len(matrix)) if matrix[row][column]),
            None,
        )
        if candidate is None:
            continue
        matrix[pivot_row], matrix[candidate] = matrix[candidate], matrix[pivot_row]
        transform[pivot_row], transform[candidate] = (
            transform[candidate],
            transform[pivot_row],
        )
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [value / scale for value in matrix[pivot_row]]
        transform[pivot_row] = [
            value / scale for value in transform[pivot_row]
        ]
        for row in range(len(matrix)):
            if row == pivot_row or not matrix[row][column]:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                matrix[row][j] - factor * matrix[pivot_row][j]
                for j in range(width)
            ]
            transform[row] = [
                transform[row][j] - factor * transform[pivot_row][j]
                for j in range(len(matrix))
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    for i, column in enumerate(pivots):
        require(matrix[i][column] == ONE, "rref-pivot-one")
        require(
            all(matrix[row][column] == ZERO for row in range(len(matrix)) if row != i),
            "rref-pivot-column",
        )
        require(
            all(matrix[i][prior] == ZERO for prior in range(column)),
            "rref-leading-pivot",
        )
    return matrix, tuple(pivots), transform


def nullspace_basis(
    reduced: Sequence[Sequence[K]], pivots: Sequence[int], width: int
) -> list[Solution]:
    free_columns = [column for column in range(width) if column not in pivots]
    basis: list[Solution] = []
    for free in free_columns:
        vector = [ZERO for _ in range(width)]
        vector[free] = ONE
        for pivot_row, pivot_column in enumerate(pivots):
            vector[pivot_column] = -reduced[pivot_row][free]
        basis.append(tuple(vector))
    for vector in basis:
        require(
            all(dot(row, vector) == ZERO for row in reduced),
            "nullspace-basis-vector",
        )
    require(len(basis) == width - len(pivots), "nullspace-dimension")
    return basis


def verify_rref_certificate(
    original: Sequence[Sequence[K]],
    reduced: Sequence[Sequence[K]],
    pivots: Sequence[int],
    basis: Sequence[Solution],
    transform: Sequence[Sequence[K]],
) -> bool:
    row_count = len(original)
    require(row_count == 18, "rref-certificate-row-count")
    require(len(reduced) == row_count, "rref-certificate-reduced-rows")
    require(len(transform) == row_count, "rref-certificate-transform-rows")
    require(
        all(len(row) == 15 for row in original)
        and all(len(row) == 15 for row in reduced),
        "rref-certificate-width",
    )
    require(
        all(len(row) == row_count for row in transform),
        "rref-certificate-transform-width",
    )
    for row in range(row_count):
        for column in range(15):
            require(
                sum(
                    (
                        transform[row][middle] * original[middle][column]
                        for middle in range(row_count)
                    ),
                    ZERO,
                )
                == reduced[row][column],
                "rref-row-equivalence",
            )
    require(tuple(pivots) == tuple(sorted(pivots)), "rref-pivot-order")
    require(len(set(pivots)) == len(pivots), "rref-pivot-uniqueness")
    require(len(pivots) + len(basis) == 15, "rref-rank-nullity")
    for row, pivot in enumerate(pivots):
        require(reduced[row][pivot] == ONE, "rref-certificate-pivot-one")
        require(
            all(
                reduced[other][pivot] == ZERO
                for other in range(row_count)
                if other != row
            ),
            "rref-certificate-pivot-column",
        )
        require(
            all(reduced[row][column] == ZERO for column in range(pivot)),
            "rref-certificate-leading-entry",
        )
    for row in range(len(pivots), row_count):
        require(
            all(value == ZERO for value in reduced[row]),
            "rref-certificate-zero-row-order",
        )
    free_columns = [
        column for column in range(15) if column not in set(pivots)
    ]
    require(len(free_columns) == len(basis), "rref-free-column-count")
    for basis_index, vector in enumerate(basis):
        require(len(vector) == 15, "rref-basis-width")
        require(
            all(dot(row, vector) == ZERO for row in original),
            "rref-original-nullspace",
        )
        require(
            all(
                vector[column] == (ONE if index == basis_index else ZERO)
                for index, column in enumerate(free_columns)
            ),
            "rref-canonical-free-coordinates",
        )
    return True


def polynomial_add(
    left: dict[tuple[int, ...], K], right: dict[tuple[int, ...], K]
) -> dict[tuple[int, ...], K]:
    result = dict(left)
    for exponent, coefficient in right.items():
        result[exponent] = result.get(exponent, ZERO) + coefficient
        if not result[exponent]:
            del result[exponent]
    return result


def polynomial_scale(
    polynomial: dict[tuple[int, ...], K], scale: K
) -> dict[tuple[int, ...], K]:
    if not scale:
        return {}
    return {
        exponent: coefficient * scale
        for exponent, coefficient in polynomial.items()
        if coefficient * scale
    }


def polynomial_multiply(
    left: dict[tuple[int, ...], K], right: dict[tuple[int, ...], K]
) -> dict[tuple[int, ...], K]:
    result: dict[tuple[int, ...], K] = {}
    for left_exp, left_coefficient in left.items():
        for right_exp, right_coefficient in right.items():
            exponent = tuple(
                left_exp[i] + right_exp[i] for i in range(len(left_exp))
            )
            result[exponent] = (
                result.get(exponent, ZERO)
                + left_coefficient * right_coefficient
            )
            if not result[exponent]:
                del result[exponent]
    return result


def determinant_polynomial_coefficients(
    basis: Sequence[Solution],
) -> dict[tuple[int, ...], K]:
    dimension = len(basis)
    entry_polynomials: list[dict[tuple[int, ...], K]] = []
    for matrix_entry in range(9):
        polynomial: dict[tuple[int, ...], K] = {}
        for parameter, vector in enumerate(basis):
            coefficient = vector[matrix_entry]
            if coefficient:
                exponent = tuple(
                    1 if i == parameter else 0 for i in range(dimension)
                )
                polynomial[exponent] = coefficient
        entry_polynomials.append(polynomial)

    result: dict[tuple[int, ...], K] = {}
    for permutation in itertools.permutations(range(3)):
        term = {tuple(0 for _ in range(dimension)): ONE}
        for row in range(3):
            term = polynomial_multiply(
                term, entry_polynomials[3 * row + permutation[row]]
            )
        sign = NEG_ONE if permutation_parity(permutation) else ONE
        result = polynomial_add(result, polynomial_scale(term, sign))
    for exponent in result:
        require(sum(exponent) == 3, "determinant-polynomial-degree")
        require(all(power <= 3 for power in exponent), "determinant-partial-degree")
    return result


def evaluate_polynomial(
    coefficients: dict[tuple[int, ...], K], parameters: Sequence[int]
) -> K:
    total = ZERO
    for exponent, coefficient in coefficients.items():
        term = coefficient
        for parameter, power in zip(parameters, exponent):
            for _ in range(power):
                term *= parameter
        total += term
    return total


def linear_combination(
    basis: Sequence[Solution], parameters: Sequence[int]
) -> Solution:
    require(len(basis) == len(parameters), "linear-combination-size")
    if not basis:
        return tuple(ZERO for _ in range(15))
    return tuple(
        sum(
            (basis[j][coordinate] * parameters[j] for j in range(len(basis))),
            ZERO,
        )
        for coordinate in range(15)
    )


def choose_invertible_witness(
    basis: Sequence[Solution],
    coefficients: dict[tuple[int, ...], K],
) -> Solution | None:
    dimension = len(basis)
    first: Solution | None = None
    saw_nonzero = False
    for parameters in itertools.product(DETERMINANT_GRID, repeat=dimension):
        polynomial_value = evaluate_polynomial(coefficients, parameters)
        solution = linear_combination(basis, parameters)
        direct_value = determinant(unflatten_matrix(solution))
        require(polynomial_value == direct_value, "determinant-polynomial-evaluation")
        if polynomial_value and first is None:
            first = normalize_solution(solution)
        saw_nonzero = saw_nonzero or bool(polynomial_value)
    require(saw_nonzero == bool(coefficients), "determinant-grid-completeness")
    return first


def verify_incidence_witness(
    exponent: int, permutation: Permutation, solution: Solution
) -> bool:
    if len(solution) != 15:
        return False
    matrix = unflatten_matrix(solution)
    lambdas = solution[9:]
    if not determinant(matrix) or any(not value for value in lambdas):
        return False
    rows = build_incidence_system(exponent, permutation)
    if any(dot(row, solution) != ZERO for row in rows):
        return False
    induced: list[int] = []
    for source in VECTORS:
        twisted = tau_vector(source) if exponent else source
        image = mat_vec(matrix, twisted)
        matches = [
            index
            for index, target in enumerate(VECTORS)
            if projectively_equal(image, target)
        ]
        if len(matches) != 1:
            return False
        induced.append(matches[0])
    induced_permutation = tuple(induced)
    if induced_permutation != permutation:
        return False
    if compose_permutations(permutation, SIGMA_LINE) != compose_permutations(
        SIGMA_LINE, permutation
    ):
        return False
    return True


def projective_frame_data(
    exponent: int, permutation: Permutation
) -> tuple[Matrix, Matrix, Vector, Vector] | None:
    sources = tuple(
        tau_vector(vector) if exponent else vector for vector in VECTORS
    )
    source_basis = matrix_from_columns(sources[:3])
    target_basis = matrix_from_columns(
        tuple(VECTORS[permutation[i]] for i in range(3))
    )
    if not determinant(source_basis) or not determinant(target_basis):
        return None
    source_coordinates = mat_vec(matrix_inverse(source_basis), sources[3])
    target_coordinates = mat_vec(
        matrix_inverse(target_basis), VECTORS[permutation[3]]
    )
    if any(not value for value in source_coordinates + target_coordinates):
        return None
    return (
        source_basis,
        target_basis,
        source_coordinates,
        target_coordinates,
    )


def projective_frame_candidate(
    exponent: int, permutation: Permutation
) -> Solution | None:
    data = projective_frame_data(exponent, permutation)
    if data is None:
        return None
    source_basis, target_basis, source_coordinates, target_coordinates = data
    scales = tuple(
        target_coordinates[i] / source_coordinates[i] for i in range(3)
    )
    matrix = mat_mul(
        mat_mul(target_basis, diagonal(scales)), matrix_inverse(source_basis)
    )
    if not determinant(matrix):
        return None
    sources = tuple(
        tau_vector(vector) if exponent else vector for vector in VECTORS
    )
    lambdas: list[K] = []
    for index, source in enumerate(sources):
        scalar = proportional_scalar(
            mat_vec(matrix, source), VECTORS[permutation[index]]
        )
        if scalar is None:
            return None
        lambdas.append(scalar)
    solution = normalize_solution(flatten_matrix(matrix) + tuple(lambdas))
    return solution


def frame_completeness_certificate(
    exponent: int, permutation: Permutation
) -> bool:
    sources = tuple(
        tau_vector(vector) if exponent else vector for vector in VECTORS
    )
    source_basis = matrix_from_columns(sources[:3])
    require(bool(determinant(source_basis)), "frame-source-basis")
    source_coordinates = mat_vec(matrix_inverse(source_basis), sources[3])
    require(
        all(source_coordinates),
        "frame-source-coordinate-nonzero",
    )
    target_basis = matrix_from_columns(
        tuple(VECTORS[permutation[i]] for i in range(3))
    )
    if not determinant(target_basis):
        # An invertible map cannot send a basis to three dependent lines.
        return True
    target_coordinates = mat_vec(
        matrix_inverse(target_basis), VECTORS[permutation[3]]
    )
    if any(not value for value in target_coordinates):
        # All source fourth-frame coordinates are nonzero.  A zero target
        # coordinate is therefore an exact frame-path rejection, not STOP.
        return True
    scales = tuple(
        target_coordinates[i] / source_coordinates[i] for i in range(3)
    )
    require(all(scales), "frame-scale-nonzero")
    candidate_matrix = mat_mul(
        mat_mul(target_basis, diagonal(scales)), matrix_inverse(source_basis)
    )
    require(bool(determinant(candidate_matrix)), "frame-candidate-invertible")
    return True


def induce_line_permutation(matrix: Matrix, exponent: int) -> Permutation | None:
    images: list[int] = []
    for vector in VECTORS:
        source = tau_vector(vector) if exponent else vector
        image = mat_vec(matrix, source)
        matches = [
            index
            for index, target in enumerate(VECTORS)
            if projectively_equal(image, target)
        ]
        if len(matches) != 1:
            return None
        images.append(matches[0])
    if sorted(images) != list(range(6)):
        return None
    return tuple(images)  # type: ignore[return-value]


def w_from_permutation(permutation: Permutation) -> WElement | None:
    values: list[int] = []
    pi: list[int] = []
    delta: list[int] = []
    for j in range(3):
        first = permutation[2 * j]
        second = permutation[2 * j + 1]
        if first // 2 != second // 2 or (first ^ second) != 1:
            return None
        pi.append(first // 2)
        delta.append(first % 2)
        values.append(first // 2)
    if sorted(values) != list(range(3)):
        return None
    return (tuple(pi), tuple(delta))  # type: ignore[return-value]


def reconstruct_linear_gauge(w_elements: Sequence[WElement]) -> set[WElement]:
    generators: tuple[Matrix, ...] = (
        ((ZERO, ZERO, ONE), (ONE, ZERO, ZERO), (ZERO, ONE, ZERO)),
        ((NEG_ONE, ZERO, ZERO), (ZERO, ONE, ZERO), (ZERO, ZERO, ONE)),
        ((ONE, ZERO, ZERO), (ZERO, NEG_ONE, ZERO), (ZERO, ZERO, ONE)),
        ((ONE, ZERO, ZERO), (ZERO, ONE, ZERO), (ZERO, ZERO, NEG_ONE)),
    )
    generator_elements: list[WElement] = []
    for matrix in generators:
        permutation = induce_line_permutation(matrix, 0)
        require(permutation is not None, "linear-generator-action")
        element = w_from_permutation(permutation)
        require(element is not None, "linear-generator-centralizer")
        require(character_pair(element) == (0, 0), "linear-generator-character")
        generator_elements.append(element)
    identity: WElement = ((0, 1, 2), (0, 0, 0))
    closure = {identity}
    frontier = [identity]
    while frontier:
        current = frontier.pop()
        for generator in generator_elements:
            for product in (
                w_compose(current, generator),
                w_compose(generator, current),
            ):
                if product not in closure:
                    closure.add(product)
                    frontier.append(product)
    kernel = {element for element in w_elements if character_pair(element) == (0, 0)}
    require(len(closure) == LINEAR_GAUGE_ORDER_THEOREM, "linear-gauge-order")
    require(closure == kernel, "linear-gauge-kernel-equality")
    return closure


def faithfulness_certificate() -> bool:
    b1 = scale_vector(-PHI, VECTORS[0])
    b2 = scale_vector(-PHI, VECTORS[1])
    b3 = VECTORS[2]
    frame = matrix_from_columns((b1, b2, b3))
    require(bool(determinant(frame)), "faithfulness-frame-basis")
    require(
        VECTORS[3] == add_vectors(add_vectors(b1, b2), b3),
        "faithfulness-v4-coordinates",
    )
    v5_coordinates = (PHI - ONE, ONE, PHI)
    reconstructed_v5 = add_vectors(
        add_vectors(
            scale_vector(v5_coordinates[0], b1),
            scale_vector(v5_coordinates[1], b2),
        ),
        scale_vector(v5_coordinates[2], b3),
    )
    require(reconstructed_v5 == VECTORS[4], "faithfulness-v5-coordinates")
    conjugate_coordinates = tuple(
        value.tau() for value in v5_coordinates
    )  # type: ignore[assignment]
    require(
        conjugate_coordinates == (-PHI, ONE, ONE - PHI),
        "faithfulness-conjugate-coordinates",
    )
    require(
        not projectively_equal(
            conjugate_coordinates, v5_coordinates  # type: ignore[arg-type]
        ),
        "faithfulness-exponent-one-pointwise",
    )
    return True


def semilinear_compose(
    left: tuple[Matrix, int], right: tuple[Matrix, int]
) -> tuple[Matrix, int]:
    left_matrix, left_exponent = left
    right_matrix, right_exponent = right
    twisted_right = tau_matrix(right_matrix) if left_exponent else right_matrix
    return (
        normalize_matrix(mat_mul(left_matrix, twisted_right)),
        left_exponent ^ right_exponent,
    )


def semilinear_inverse(realization: tuple[Matrix, int]) -> tuple[Matrix, int]:
    matrix, exponent = realization
    inverse = matrix_inverse(matrix)
    if exponent:
        inverse = tau_matrix(inverse)
    return (normalize_matrix(inverse), exponent)


def selector_orbits(
    group: set[WElement], selectors: Sequence[WElement]
) -> tuple[list[tuple[WElement, ...]], bool]:
    selector_set = set(selectors)
    require(len(selector_set) == SELECTOR_COUNT_THEOREM, "selector-set-size")
    free = True
    for selector in selectors:
        images = {w_compose(group_element, selector) for group_element in group}
        if len(images) != len(group):
            free = False
        require(images <= selector_set, "selector-action-closure")
    unseen = set(selector_set)
    orbits: list[tuple[WElement, ...]] = []
    while unseen:
        representative = min(unseen)
        orbit = tuple(
            sorted(w_compose(group_element, representative) for group_element in group)
        )
        require(len(set(orbit)) == len(orbit), "selector-orbit-duplicate")
        orbits.append(orbit)
        unseen -= set(orbit)
    orbits.sort(key=lambda orbit: orbit[0])
    require(
        set().union(*(set(orbit) for orbit in orbits)) == selector_set,
        "selector-orbit-cover",
    )
    return orbits, free


def completeness_certificate(
    case_records: Sequence[dict[str, Any]],
    accepted: dict[tuple[int, WElement], Solution],
    w_elements: Sequence[WElement],
) -> bool:
    expected_keys = {
        (exponent, element)
        for exponent in SCAN_EXPONENTS
        for element in w_elements
    }
    actual_keys = {
        (record["exponent"], record["element"]) for record in case_records
    }
    require(len(case_records) == SCAN_CASE_COUNT_THEOREM, "scan-case-count")
    require(actual_keys == expected_keys, "scan-key-completeness")
    require(
        all(
            record["frame_accept"] == record["rref_accept"]
            for record in case_records
        ),
        "dual-path-decision-agreement",
    )
    for key, solution in accepted.items():
        exponent, element = key
        require(
            verify_incidence_witness(exponent, w_permutation(element), solution),
            "accepted-realization-incidence",
        )
    # Converse certificate: W was independently proved to be the complete
    # commuting permutation centralizer.  Every realization induces one of
    # those keys, its homogeneous coordinates lie in the computed complete
    # nullspace, and its nonzero determinant makes the determinant polynomial
    # nonzero, so the exhaustive grid decision accepts that key.
    require(len(actual_keys) == 2 * len(w_elements), "converse-key-carrier")
    return True


def element_data(element: WElement) -> dict[str, Any]:
    return {"pi": list(element[0]), "delta": list(element[1])}


def solution_data(solution: Solution) -> dict[str, Any]:
    return {
        "B": [qdata(value) for value in solution[:9]],
        "lambda": [qdata(value) for value in solution[9:]],
    }


def emit_transcript(state: dict[str, Any]) -> None:
    print(f"PROBE: {PROBE_ID}")
    print("MODE: exact complete semilinear incidence scan")
    for source in state["sources"]:
        print(
            "SOURCE:"
            f" {source['filename']}"
            f" bytes={source['bytes']}"
            f" lf={source['lf']}"
            f" cr={source['cr']}"
            f" sha256={source['sha256']}"
        )
    print("STRUCTURE: exact field/vector/projective reconstruction PASS")
    print("STRUCTURE: W complete centralizer order 48 PASS")
    print("STRUCTURE: selector torsor and character covariance PASS")
    print("STRUCTURE: inherited exponent-zero gauge equals common kernel order 12 PASS")
    print("STRUCTURE: independent projective-frame uniqueness for 96 cases PASS")
    print("STRUCTURE: full 18x15 RREF/nullspace/determinant scan for 96 cases PASS")
    print("STRUCTURE: dual-path decision and normalized-witness agreement PASS")
    print("STRUCTURE: faithfulness and two-direction completeness PASS")
    print("STRUCTURE: semilinear composition/inverse/exact-sequence checks PASS")
    print("STRUCTURE: free selector action and complete orbit partition PASS")
    print(f"CASE_TABLE_SHA256: {state['case_table_sha256']}")
    print(f"ACCEPTED_REALIZATIONS: {len(state['accepted_rows'])}")
    for row in state["case_rows"]:
        print("CASE: " + json.dumps(row, sort_keys=True, separators=(",", ":")))
    for row in state["accepted_rows"]:
        print(
            "WITNESS: "
            + json.dumps(row, sort_keys=True, separators=(",", ":"))
        )
    print("SCIENTIFIC_RESULT_BEGIN")
    print("ROUTE:", state["route"])
    print("GAMMA_SL_ORDER:", state["gamma_order"])
    print("EXPONENT_ONE_COUNT:", state["exponent_one_count"])
    print("COSET_CHARACTER:", state["coset_character"])
    print("RESIDUAL_INVARIANT:", state["residual_invariant"])
    print("SELECTOR_ORBIT_COUNT:", len(state["orbits"]))
    print(
        "SELECTOR_ORBIT_SIZES:",
        ",".join(str(len(orbit)) for orbit in state["orbits"]),
    )
    print("RESULT:", "PASS")
    print("SCIENTIFIC_RESULT_END")


def main() -> int:
    """Run the one complete deterministic evaluation."""

    try:
        probe_dir = Path(__file__).resolve().parent
        sources = verify_sources(probe_dir)

        require(PHI * PHI == PHI + ONE, "field-phi-polynomial")
        require(PHI.tau() == ONE - PHI, "field-tau-phi")
        require(all(value.tau().tau() == value for vector in VECTORS for value in vector), "field-tau-involution")
        require(all(any(vector) for vector in VECTORS), "line-nonzero")
        require(
            all(
                not projectively_equal(VECTORS[i], VECTORS[j])
                for i in range(6)
                for j in range(i + 1, 6)
            ),
            "line-distinctness",
        )

        w_elements = enumerate_w()
        require(len(w_elements) == W_ORDER_THEOREM, "w-order")
        require(len(set(w_elements)) == W_ORDER_THEOREM, "w-uniqueness")
        w_permutations = {w_permutation(element) for element in w_elements}
        require(len(w_permutations) == W_ORDER_THEOREM, "w-permutation-faithful")
        full_centralizer = {
            tuple(permutation)
            for permutation in itertools.permutations(range(6))
            if compose_permutations(tuple(permutation), SIGMA_LINE)
            == compose_permutations(SIGMA_LINE, tuple(permutation))
        }
        require(w_permutations == full_centralizer, "w-centralizer-completeness")
        require(
            all(
                w_compose(element, w_inverse(element))
                == ((0, 1, 2), (0, 0, 0))
                for element in w_elements
            ),
            "w-inverses",
        )

        selectors = enumerate_selectors()
        require(len(selectors) == SELECTOR_COUNT_THEOREM, "selector-count")
        require(len(set(selectors)) == SELECTOR_COUNT_THEOREM, "selector-unique")
        kernel = {
            element for element in w_elements if character_pair(element) == (0, 0)
        }
        require(len(kernel) == LINEAR_GAUGE_ORDER_THEOREM, "character-kernel-order")
        require(
            {character_pair(element) for element in w_elements}
            == {(0, 0), (0, 1), (1, 0), (1, 1)},
            "character-surjectivity",
        )
        for left in w_elements:
            for right in w_elements:
                product_character = character_pair(w_compose(left, right))
                expected_character = tuple(
                    character_pair(left)[i] ^ character_pair(right)[i]
                    for i in range(2)
                )
                require(product_character == expected_character, "character-homomorphism")
        for action in w_elements:
            for selector in selectors:
                image = w_compose(action, selector)
                expected = tuple(
                    character_pair(action)[i] ^ character_pair(selector)[i]
                    for i in range(2)
                )
                require(character_pair(image) == expected, "character-covariance")

        linear_gauge = reconstruct_linear_gauge(w_elements)
        require(linear_gauge == kernel, "linear-gauge-integrity")
        require(faithfulness_certificate(), "faithfulness-certificate")

        case_records: list[dict[str, Any]] = []
        accepted: dict[tuple[int, WElement], Solution] = {}
        case_rows: list[dict[str, Any]] = []
        accepted_rows: list[dict[str, Any]] = []
        case_index = 0
        for exponent in SCAN_EXPONENTS:
            for element in w_elements:
                permutation = w_permutation(element)
                require(
                    frame_completeness_certificate(exponent, permutation),
                    "frame-completeness",
                )
                frame_solution = projective_frame_candidate(exponent, permutation)

                system = build_incidence_system(exponent, permutation)
                reduced, pivots, row_transform = rref(system)
                basis = nullspace_basis(reduced, pivots, 15)
                require(
                    verify_rref_certificate(
                        system, reduced, pivots, basis, row_transform
                    ),
                    "rref-certificate",
                )
                coefficients = determinant_polynomial_coefficients(basis)
                rref_solution = choose_invertible_witness(basis, coefficients)

                frame_accept = frame_solution is not None
                rref_accept = rref_solution is not None
                require(frame_accept == rref_accept, "dual-path-decision")
                if frame_accept:
                    require(len(basis) == 1, "accepted-nullity-one")
                    require(
                        set(coefficients) == {(3,)},
                        "accepted-determinant-polynomial-shape",
                    )
                    require(frame_solution == rref_solution, "dual-path-witness")
                    require(frame_solution is not None, "accepted-frame-solution")
                    require(
                        verify_incidence_witness(exponent, permutation, frame_solution),
                        "accepted-direct-check",
                    )
                    accepted[(exponent, element)] = frame_solution

                coefficient_data = [
                    {
                        "exponent": list(monomial),
                        "coefficient": qdata(coefficients[monomial]),
                    }
                    for monomial in sorted(coefficients)
                ]
                witness_sha = (
                    canonical_hash(solution_data(frame_solution))
                    if frame_solution is not None
                    else "NONE"
                )
                case_row = {
                    "index": case_index,
                    "e": exponent,
                    "pi": list(element[0]),
                    "delta": list(element[1]),
                    "rank": len(pivots),
                    "nullity": len(basis),
                    "determinant_polynomial_sha256": canonical_hash(coefficient_data),
                    "accepted": int(frame_accept),
                    "witness_sha256": witness_sha,
                }
                case_rows.append(case_row)
                case_records.append(
                    {
                        "exponent": exponent,
                        "element": element,
                        "frame_accept": frame_accept,
                        "rref_accept": rref_accept,
                        "rank": len(pivots),
                        "nullity": len(basis),
                    }
                )
                if frame_solution is not None:
                    accepted_rows.append(
                        {
                            "index": case_index,
                            "e": exponent,
                            "element": element_data(element),
                            "solution": solution_data(frame_solution),
                        }
                    )
                case_index += 1

        require(case_index == SCAN_CASE_COUNT_THEOREM, "scan-final-count")
        require(
            completeness_certificate(case_records, accepted, w_elements),
            "completeness-certificate",
        )
        exponent_zero = {
            element for (exponent, element) in accepted if exponent == 0
        }
        exponent_one = {
            element for (exponent, element) in accepted if exponent == 1
        }
        require(exponent_zero == linear_gauge == kernel, "exponent-zero-equality")
        require(not (exponent_zero & exponent_one), "cross-exponent-faithfulness")
        require(
            len(exponent_one) in (0, LINEAR_GAUGE_ORDER_THEOREM),
            "exponent-one-dichotomy",
        )

        identity_element: WElement = ((0, 1, 2), (0, 0, 0))
        identity_matrix: Matrix = (
            (ONE, ZERO, ZERO),
            (ZERO, ONE, ZERO),
            (ZERO, ZERO, ONE),
        )
        require(
            accepted[(0, identity_element)][:9] == flatten_matrix(identity_matrix),
            "identity-witness",
        )
        for left_key, left_solution in accepted.items():
            for right_key, right_solution in accepted.items():
                left_exponent, left_element = left_key
                right_exponent, right_element = right_key
                composed_matrix, composed_exponent = semilinear_compose(
                    (unflatten_matrix(left_solution), left_exponent),
                    (unflatten_matrix(right_solution), right_exponent),
                )
                composed_element = w_compose(left_element, right_element)
                composed_key = (composed_exponent, composed_element)
                require(composed_key in accepted, "semilinear-composition-closure")
                require(
                    composed_matrix
                    == unflatten_matrix(accepted[composed_key]),
                    "semilinear-composition-formula",
                )
            inverse_matrix, inverse_exponent = semilinear_inverse(
                (unflatten_matrix(left_solution), left_key[0])
            )
            inverse_key = (inverse_exponent, w_inverse(left_key[1]))
            require(inverse_key in accepted, "semilinear-inverse-closure")
            require(
                inverse_matrix == unflatten_matrix(accepted[inverse_key]),
                "semilinear-inverse-formula",
            )

        if exponent_one:
            representative = min(exponent_one)
            left_coset = {w_compose(representative, element) for element in kernel}
            right_coset = {w_compose(element, representative) for element in kernel}
            require(exponent_one == left_coset == right_coset, "exponent-one-coset")
            characters = {character_pair(element) for element in exponent_one}
            require(len(characters) == 1, "coset-character-common")
            coset_character = next(iter(characters))
            require(coset_character in COSET_CHARACTER_CASES, "coset-character-nonzero")
            residual_invariant = RESIDUAL_INVARIANT_BY_CHARACTER[coset_character]
            route = SCIENTIFIC_ROUTES[1]
            gamma = kernel | exponent_one
        else:
            coset_character = None
            residual_invariant = "(chi_Q,chi_F)"
            route = SCIENTIFIC_ROUTES[0]
            gamma = set(kernel)

        require(len(gamma) in POSSIBLE_GAMMA_ORDERS, "gamma-order-dichotomy")
        require(len(gamma) == len(accepted), "faithful-image-cardinality")
        orbits, free_action = selector_orbits(gamma, selectors)
        require(free_action, "selector-action-free")
        expected_orbit_count = 4 if len(gamma) == 12 else 2
        require(len(orbits) == expected_orbit_count, "selector-orbit-count")
        require(
            all(len(orbit) == len(gamma) for orbit in orbits),
            "selector-orbit-size",
        )
        if exponent_one:
            for orbit in orbits:
                invariant_values: set[int] = set()
                for selector in orbit:
                    q_value, f_value = character_pair(selector)
                    if coset_character == (1, 0):
                        invariant_values.add(f_value)
                    elif coset_character == (0, 1):
                        invariant_values.add(q_value)
                    else:
                        invariant_values.add(q_value ^ f_value)
                require(len(invariant_values) == 1, "residual-invariant-orbit")
            require(
                len(
                    {
                        (
                            character_pair(orbit[0])[1]
                            if coset_character == (1, 0)
                            else character_pair(orbit[0])[0]
                            if coset_character == (0, 1)
                            else character_pair(orbit[0])[0]
                            ^ character_pair(orbit[0])[1]
                        )
                        for orbit in orbits
                    }
                )
                == 2,
                "residual-invariant-separates",
            )

        case_table_sha256 = canonical_hash(case_rows)
        state = {
            "sources": sources,
            "case_rows": case_rows,
            "case_table_sha256": case_table_sha256,
            "accepted_rows": accepted_rows,
            "route": route,
            "gamma_order": len(gamma),
            "exponent_one_count": len(exponent_one),
            "coset_character": (
                "NONE"
                if coset_character is None
                else f"({coset_character[0]},{coset_character[1]})"
            ),
            "residual_invariant": residual_invariant,
            "orbits": orbits,
        }
        emit_transcript(state)
        return 0
    except StopVerification as exc:
        print(f"ROUTE: {STOP_ROUTE}")
        print(f"STOP_CODE: {exc}")
        print("RESULT: FAIL")
        return 1
    except Exception as exc:
        print(f"ROUTE: {STOP_ROUTE}")
        print(f"STOP_CODE: INTERNAL-{type(exc).__name__}")
        print("RESULT: FAIL")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
