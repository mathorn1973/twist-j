#!/usr/bin/env python3
"""Exact and finite-field primitives for the frozen artisan F8 experiment.

Standard-library only.  All conventions are copied from the publicly pinned
C-GOLDEN-AME-vs-GG-ARTISANAL-F8-1-N preregistration.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
import hashlib
import itertools
from pathlib import Path
import re
from typing import Callable, Iterable, Iterator, Sequence


P = 241
XI_MOD = 3
DEG = 32
DIM = 6
ID4 = (0, 1, 2, 3)
DESCRIPTORS = (
    ((1, 0, 3, 2), (2, 3, 0, 1), (3, 2, 1, 0)),
    ((1, 0, 3, 2), (2, 3, 1, 0), (3, 2, 0, 1)),
    ((1, 2, 3, 0), (2, 3, 0, 1), (3, 0, 1, 2)),
    ((1, 2, 3, 0), (3, 0, 1, 2), (2, 3, 0, 1)),
)

PRIMARY_PLAN = (
    ("A0", "B3"),
    ("A3", "B2"),
    ("$0", "$1"),
    ("A2", "B1"),
    ("$2", "$3"),
    ("$4", "B0"),
    ("$5", "A1"),
)

ALTERNATE_PLAN = (
    ("A1", "B0"),
    ("A2", "B1"),
    ("$0", "$1"),
    ("A3", "B2"),
    ("$2", "$3"),
    ("$4", "B3"),
    ("$5", "A0"),
)

GOLDEN_PIN = {
    "bytes": 8515,
    "sha256": "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae",
    "git_blob_sha1": "e0d0e171d58b3360c39595d677ffc401a466112d",
}
PAPER_PDF_PIN = {
    "bytes": 643554,
    "sha256": "3c423439d89a969235612bc4149069e8bfca349cf1532413ae90f19fdbf0e2be",
}
PAPER_SOURCE_PIN = {
    "bytes": 49234,
    "sha256": "c67eab02dc7960e171eea723aada3554fb2869c8e07ece7ae209132cc33c86d2",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def verify_pinned_bytes(path: Path, pin: dict, git_blob: bool = False) -> bytes:
    data = path.read_bytes()
    if len(data) != pin["bytes"] or sha256_bytes(data) != pin["sha256"]:
        raise AssertionError(f"source pin mismatch: {path.name}")
    if git_blob and git_blob_sha1(data) != pin["git_blob_sha1"]:
        raise AssertionError(f"git blob mismatch: {path.name}")
    return data


def parse_matrix_rows(block: str, token_pattern: str) -> list[list[str]]:
    rows = [row.strip() for row in block.split(";") if row.strip()]
    output = []
    for row_index, row in enumerate(rows):
        tokens = re.findall(token_pattern, row)
        if len(tokens) != 36:
            raise ValueError(f"row {row_index}: expected 36 tokens, found {len(tokens)}")
        output.append(tokens)
    if len(output) != 36:
        raise ValueError(f"expected 36 rows, found {len(output)}")
    return output


def parse_golden_source(data: bytes) -> dict[tuple[int, int, int, int], tuple[str, int]]:
    text = data.decode("utf-8")
    match = re.search(r"U\s*=\s*\[(.*?)\]\s*\.\*\s*w\.\^\s*\[(.*?)\]\s*;", text, re.S)
    if not match:
        raise ValueError("golden U matrix blocks not found")
    amplitudes = parse_matrix_rows(
        match.group(1), r"(?<![A-Za-z0-9_])(?:0|a|b|c)(?![A-Za-z0-9_])"
    )
    exponents = parse_matrix_rows(
        match.group(2), r"(?<![A-Za-z0-9_])(?:[0-9]|1[0-9])(?![A-Za-z0-9_])"
    )
    tensor = {}
    for row in range(36):
        for column in range(36):
            label = amplitudes[row][column]
            if label == "0":
                continue
            i, j = divmod(row, 6)
            k, ell = divmod(column, 6)
            tensor[(i, j, k, ell)] = (label, int(exponents[row][column]) % 20)
    if len(tensor) != 112:
        raise AssertionError(f"golden support mismatch: {len(tensor)}")
    return tensor


# Phi_120(X)=X^32+X^28-X^20-X^16-X^12+X^4+1.
def reduce120(coefficients: Iterable[Fraction | int]) -> tuple[Fraction, ...]:
    values = [Fraction(value) for value in coefficients]
    if len(values) < DEG:
        values.extend([Fraction(0)] * (DEG - len(values)))
    for degree in range(len(values) - 1, DEG - 1, -1):
        lead = values[degree]
        if not lead:
            continue
        values[degree] = 0
        values[degree - 4] -= lead
        values[degree - 12] += lead
        values[degree - 16] += lead
        values[degree - 20] += lead
        values[degree - 28] -= lead
        values[degree - 32] -= lead
    return tuple(values[:DEG])


@dataclass(frozen=True)
class K120:
    coefficients: tuple[Fraction, ...]

    def __init__(self, coefficients: Iterable[Fraction | int] = (0,)):
        object.__setattr__(self, "coefficients", reduce120(coefficients))

    def __add__(self, other: object) -> "K120":
        right = as_k120(other)
        return K120(a + b for a, b in zip(self.coefficients, right.coefficients))

    __radd__ = __add__

    def __neg__(self) -> "K120":
        return K120(-value for value in self.coefficients)

    def __sub__(self, other: object) -> "K120":
        return self + (-as_k120(other))

    def __rsub__(self, other: object) -> "K120":
        return as_k120(other) - self

    def __mul__(self, other: object) -> "K120":
        right = as_k120(other)
        product = [Fraction(0)] * (2 * DEG - 1)
        for i, a in enumerate(self.coefficients):
            if not a:
                continue
            for j, b in enumerate(right.coefficients):
                if b:
                    product[i + j] += a * b
        return K120(product)

    __rmul__ = __mul__

    def __pow__(self, exponent: int) -> "K120":
        if exponent < 0:
            return inverse_k120(self) ** (-exponent)
        result = K120((1,))
        base = self
        while exponent:
            if exponent & 1:
                result = result * base
            base = base * base
            exponent >>= 1
        return result

    def conjugate(self) -> "K120":
        result = K120()
        for power, coefficient in enumerate(self.coefficients):
            if coefficient:
                result += coefficient * XI_POWERS[(-power) % 120]
        return result

    def mod241(self) -> int:
        total = 0
        power = 1
        for coefficient in self.coefficients:
            denominator = coefficient.denominator % P
            if denominator == 0:
                raise AssertionError("non-241-integral exact coefficient")
            residue = coefficient.numerator % P * pow(denominator, -1, P) % P
            total = (total + residue * power) % P
            power = power * XI_MOD % P
        return total

    def serial(self) -> list[str]:
        return [f"{value.numerator}/{value.denominator}" for value in self.coefficients]


def as_k120(value: object) -> K120:
    return value if isinstance(value, K120) else K120((value,))


XI = K120((0, 1))
XI_POWERS = tuple(XI**power for power in range(120))


def inverse_k120(value: K120) -> K120:
    matrix = []
    for row in range(DEG):
        matrix.append(
            [(value * XI_POWERS[column]).coefficients[row] for column in range(DEG)]
            + [Fraction(row == 0)]
        )
    for column in range(DEG):
        pivot = next((row for row in range(column, DEG) if matrix[row][column]), None)
        if pivot is None:
            raise ZeroDivisionError("zero/nonunit in K120")
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        scale = matrix[column][column]
        matrix[column] = [entry / scale for entry in matrix[column]]
        for row in range(DEG):
            if row == column or not matrix[row][column]:
                continue
            scale = matrix[row][column]
            matrix[row] = [a - scale * b for a, b in zip(matrix[row], matrix[column])]
    return K120(row[-1] for row in matrix)


@lru_cache(maxsize=1)
def golden_amplitudes_exact() -> dict[str, K120]:
    c = (XI_POWERS[15] + XI_POWERS[-15]) * Fraction(1, 2)
    denominator = XI_POWERS[6] + XI_POWERS[-6]
    a = c * inverse_k120(denominator)
    b = (XI_POWERS[12] + XI_POWERS[-12]) * a
    amplitudes = {"a": a, "b": b, "c": c}
    expected_mod = golden_amplitudes_mod()
    if {key: value.mod241() for key, value in amplitudes.items()} != expected_mod:
        raise AssertionError("golden exact/mod amplitude disagreement")
    return amplitudes


def golden_amplitudes_mod() -> dict[str, int]:
    inverse2 = pow(2, -1, P)
    c = (pow(XI_MOD, 15, P) + pow(XI_MOD, -15, P)) * inverse2 % P
    a = c * pow((pow(XI_MOD, 6, P) + pow(XI_MOD, -6, P)) % P, -1, P) % P
    b = (pow(XI_MOD, 12, P) + pow(XI_MOD, -12, P)) * a % P
    return {"a": a, "b": b, "c": c}


@dataclass(frozen=True)
class Q6:
    """Integer a+b*w in Z[w], w=zeta_6 and w^2=w-1."""

    a: int = 0
    b: int = 0

    def __add__(self, other: "Q6") -> "Q6":
        return Q6(self.a + other.a, self.b + other.b)

    def __sub__(self, other: "Q6") -> "Q6":
        return Q6(self.a - other.a, self.b - other.b)

    def __neg__(self) -> "Q6":
        return Q6(-self.a, -self.b)

    def __mul__(self, other: "Q6") -> "Q6":
        return Q6(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a + self.b * other.b,
        )

    def conjugate(self) -> "Q6":
        return Q6(self.a + self.b, -self.b)

    def mod241(self) -> int:
        return (self.a + self.b * pow(XI_MOD, 20, P)) % P

    def to_k120(self, denominator: int = 1) -> K120:
        return (K120((self.a,)) + self.b * XI_POWERS[20]) * Fraction(1, denominator)

    def serial(self) -> dict[str, int]:
        return {"a": self.a, "b": self.b}


Q6_POWERS = (
    Q6(1, 0),
    Q6(0, 1),
    Q6(-1, 1),
    Q6(-1, 0),
    Q6(0, -1),
    Q6(1, -1),
)


def crt_coordinates(value: int) -> tuple[int, int]:
    value %= 6
    return value % 3, value % 2


def artisanal_phi(kind: str, p: int, q: int) -> int:
    if kind not in {"sym", "sparse"}:
        raise ValueError(kind)
    k, x = crt_coordinates(p)
    ell, y = crt_coordinates(q)
    value = k * k + ell * ell
    if (x, y) == (1, 1):
        return value % 3
    m = (x - y) % 3
    if kind == "sym":
        value -= (k + ell + m) ** 2
    else:
        value += (ell + m) ** 2
    return value % 3


def lambda_table(kind: str) -> tuple[int, ...]:
    return tuple(artisanal_phi(kind, p, q) for p in range(6) for q in range(6))


def gl2_f3() -> tuple[tuple[tuple[int, int], tuple[int, int]], ...]:
    output = []
    for a, b, c, d in itertools.product(range(3), repeat=4):
        if (a * d - b * c) % 3:
            output.append(((a, b), (c, d)))
    if len(output) != 48:
        raise AssertionError("GL(2,F3) order mismatch")
    return tuple(output)


def gl_lift_transpose_action(matrix, p: int, q: int) -> tuple[int, int]:
    lifted = tuple(
        tuple((4 * matrix[row][column] + 3 * (row == column)) % 6 for column in range(2))
        for row in range(2)
    )
    return (
        (lifted[0][0] * p + lifted[1][0] * q) % 6,
        (lifted[0][1] * p + lifted[1][1] * q) % 6,
    )


def transformed_lambda_table(kind: str, matrix) -> tuple[int, ...]:
    table = lambda_table(kind)
    output = []
    for p in range(6):
        for q in range(6):
            p2, q2 = gl_lift_transpose_action(matrix, p, q)
            output.append(table[6 * p2 + q2])
    return tuple(output)


def verify_lambda_table_autocorrelations(table: Sequence[int]) -> dict:
    if len(table) != 36 or any(value not in (0, 1, 2) for value in table):
        raise AssertionError("invalid omega3-exponent lambda table")
    ordinary = []
    twisted = []
    for ap in range(6):
        for aq in range(6):
            sum_ordinary = Q6()
            sum_twisted = Q6()
            for bp in range(6):
                for bq in range(6):
                    phi_b = table[6 * bp + bq]
                    phi_ab = table[6 * ((ap + bp) % 6) + ((aq + bq) % 6)]
                    delta = 2 * (phi_ab - phi_b)
                    sum_ordinary += Q6_POWERS[delta % 6]
                    symplectic = ap * bq - aq * bp
                    sum_twisted += Q6_POWERS[(delta + symplectic) % 6]
            expected = Q6(36, 0) if (ap, aq) == (0, 0) else Q6()
            if sum_ordinary != expected or sum_twisted != expected:
                raise AssertionError((ap, aq, sum_ordinary, sum_twisted))
            ordinary.append(sum_ordinary.serial())
            twisted.append(sum_twisted.serial())
    return {
        "ordinary_sha256": sha256_bytes(repr(ordinary).encode("ascii")),
        "twisted_sha256": sha256_bytes(repr(twisted).encode("ascii")),
    }


def verify_autocorrelations(kind: str) -> dict:
    return verify_lambda_table_autocorrelations(lambda_table(kind))


def artisanal_entry(kind: str, i: int, j: int, k: int, ell: int) -> Q6 | None:
    q = (i - j) % 6
    if q != (k - ell) % 6:
        return None
    value = Q6()
    for p in range(6):
        exponent = (2 * artisanal_phi(kind, p, q) + p * (i - k)) % 6
        value += Q6_POWERS[exponent]
    return value if value != Q6() else None


@lru_cache(maxsize=2)
def artisanal_tensor(kind: str) -> dict[tuple[int, int, int, int], Q6]:
    tensor = {}
    for indices in itertools.product(range(6), repeat=4):
        value = artisanal_entry(kind, *indices)
        if value is not None:
            tensor[indices] = value
    return tensor


def golden_tensor_exact(tokens: dict) -> dict[tuple[int, ...], K120]:
    amplitudes = golden_amplitudes_exact()
    return {
        indices: amplitudes[label] * XI_POWERS[(6 * exponent) % 120]
        for indices, (label, exponent) in tokens.items()
    }


def golden_tensor_mod(tokens: dict) -> tuple[dict, dict]:
    amplitudes = golden_amplitudes_mod()
    w = pow(XI_MOD, 6, P)
    direct = {
        indices: amplitudes[label] * pow(w, exponent, P) % P
        for indices, (label, exponent) in tokens.items()
    }
    conjugate = {
        indices: amplitudes[label] * pow(w, -exponent, P) % P
        for indices, (label, exponent) in tokens.items()
    }
    return direct, conjugate


def artisanal_tensor_mod(kind: str) -> tuple[dict, dict]:
    inverse6 = pow(6, -1, P)
    direct = {
        indices: value.mod241() * inverse6 % P
        for indices, value in artisanal_tensor(kind).items()
    }
    conjugate = {
        indices: value.conjugate().mod241() * inverse6 % P
        for indices, value in artisanal_tensor(kind).items()
    }
    return direct, conjugate


def inverse_permutation(permutation: Sequence[int]) -> tuple[int, ...]:
    output = [0] * len(permutation)
    for i, value in enumerate(permutation):
        output[value] = i
    return tuple(output)


def factor_labels(descriptor: Sequence[Sequence[int]]) -> dict[str, tuple[tuple[int, int], ...]]:
    matchings = (ID4,) + tuple(tuple(p) for p in descriptor)
    inverses = tuple(inverse_permutation(p) for p in matchings)
    output = {}
    for r in range(4):
        output[f"A{r}"] = tuple((colour, r) for colour in range(4))
    for s in range(4):
        output[f"B{s}"] = tuple(
            (colour, inverses[colour][s]) for colour in range(4)
        )
    return output


def flatten_tensor(tensor: dict, row_parties: tuple[int, int]) -> dict[int, dict[int, object]]:
    column_parties = tuple(party for party in range(4) if party not in row_parties)
    rows: dict[int, dict[int, object]] = defaultdict(dict)
    for indices, value in tensor.items():
        row = 6 * indices[row_parties[0]] + indices[row_parties[1]]
        column = 6 * indices[column_parties[0]] + indices[column_parties[1]]
        rows[row][column] = value
    return rows


def verify_golden_three_unitarity(tokens: dict) -> dict:
    tensor = golden_tensor_exact(tokens)
    results = {}
    for row_parties in ((0, 1), (0, 2), (0, 3)):
        rows = flatten_tensor(tensor, row_parties)
        for left in range(36):
            for right in range(36):
                total = K120()
                common = set(rows.get(left, {})).intersection(rows.get(right, {}))
                for column in common:
                    total += rows[left][column] * rows[right][column].conjugate()
                expected = K120((int(left == right),))
                if total != expected:
                    raise AssertionError(("golden unitarity", row_parties, left, right))
        results["".join(map(str, row_parties))] = "PASS"
    return results


def verify_artisanal_three_unitarity(kind: str) -> dict:
    tensor = artisanal_tensor(kind)
    results = {}
    # Every entry is numerator/6, so Gram numerators must equal 36*I.
    for row_parties in ((0, 1), (0, 2), (0, 3)):
        rows = flatten_tensor(tensor, row_parties)
        for left in range(36):
            for right in range(36):
                total = Q6()
                common = set(rows.get(left, {})).intersection(rows.get(right, {}))
                for column in common:
                    total += rows[left][column] * rows[right][column].conjugate()
                expected = Q6(36, 0) if left == right else Q6()
                if total != expected:
                    raise AssertionError((kind, row_parties, left, right, total))
        results["".join(map(str, row_parties))] = "PASS"
    return results


def bell_sector_projector9() -> dict[tuple[int, int], Q6]:
    """Return numerator entries of Pi_9; the common denominator is six."""

    matrix = {}
    for i, j, k, ell in itertools.product(range(6), repeat=4):
        q = (i - j) % 6
        if q != (k - ell) % 6 or q % 2 != 1:
            continue
        value = Q6()
        for p in (1, 3, 5):
            value += Q6_POWERS[(p * (i - k)) % 6]
        if value != Q6():
            matrix[(6 * i + j, 6 * k + ell)] = value
    return matrix


def q6_matrix_product(left: dict, right: dict) -> dict:
    right_by_row: dict[int, list[tuple[int, Q6]]] = defaultdict(list)
    for (row, column), value in right.items():
        right_by_row[row].append((column, value))
    output: dict[tuple[int, int], Q6] = {}
    for (row, middle), value_left in left.items():
        for column, value_right in right_by_row.get(middle, ()):
            key = (row, column)
            output[key] = output.get(key, Q6()) + value_left * value_right
    return {key: value for key, value in output.items() if value != Q6()}


def q6_scaled_matrix_equal(left: dict, left_scale: int, right: dict, right_scale: int) -> bool:
    keys = set(left) | set(right)
    for key in keys:
        if Q6(left_scale, 0) * left.get(key, Q6()) != Q6(right_scale, 0) * right.get(key, Q6()):
            return False
    return True


def verify_9plus27(kind: str) -> dict:
    # U and Pi9 are both represented by numerator matrices with denominator 6.
    u = {(6 * i + j, 6 * k + ell): value for (i, j, k, ell), value in artisanal_tensor(kind).items()}
    p9 = bell_sector_projector9()
    p9_squared = q6_matrix_product(p9, p9)
    if not q6_scaled_matrix_equal(p9_squared, 1, p9, 6):
        raise AssertionError("Pi9 is not exactly idempotent")
    trace_numerator = Q6()
    for index in range(36):
        trace_numerator += p9.get((index, index), Q6())
    if trace_numerator != Q6(54, 0):
        raise AssertionError(("Pi9 trace", trace_numerator))
    up = q6_matrix_product(u, p9)
    pu = q6_matrix_product(p9, u)
    if up != pu:
        raise AssertionError((kind, "U/Pi9 commutator"))
    # Pi27=I-Pi9 has numerator 6I-P9 and denominator 6.
    p27 = dict(p9)
    p27 = {key: -value for key, value in p27.items()}
    for index in range(36):
        key = (index, index)
        p27[key] = p27.get(key, Q6()) + Q6(6, 0)
        if p27[key] == Q6():
            del p27[key]
    p27_squared = q6_matrix_product(p27, p27)
    if not q6_scaled_matrix_equal(p27_squared, 1, p27, 6):
        raise AssertionError("Pi27 is not exactly idempotent")
    trace27 = Q6()
    for index in range(36):
        trace27 += p27.get((index, index), Q6())
    if trace27 != Q6(162, 0):
        raise AssertionError(("Pi27 trace", trace27))
    return {
        "rank_pi9_from_exact_idempotent_trace": 9,
        "rank_pi27_from_exact_idempotent_trace": 27,
        "commutator": "ZERO",
    }


@dataclass
class Relation:
    labels: tuple[tuple[int, int], ...]
    rows: dict[tuple[int, ...], object]
    factors: int
    name: str


def make_factor_relation(
    name: str,
    labels: tuple[tuple[int, int], ...],
    tensor: dict[tuple[int, ...], object],
) -> Relation:
    return Relation(labels, dict(tensor), 1, name)


def merge_relation(
    left: Relation,
    right: Relation,
    add: Callable,
    multiply: Callable,
    zero: object,
) -> Relation:
    shared = tuple(sorted(set(left.labels).intersection(right.labels)))
    if not shared:
        raise AssertionError(f"outer product forbidden: {left.name}, {right.name}")
    left_shared_positions = tuple(left.labels.index(label) for label in shared)
    right_shared_positions = tuple(right.labels.index(label) for label in shared)
    left_keep_positions = tuple(i for i, label in enumerate(left.labels) if label not in shared)
    right_keep_positions = tuple(i for i, label in enumerate(right.labels) if label not in shared)
    output_labels = tuple(left.labels[i] for i in left_keep_positions) + tuple(
        right.labels[i] for i in right_keep_positions
    )
    right_index: dict[tuple[int, ...], list[tuple[tuple[int, ...], object]]] = defaultdict(list)
    for assignment, value in right.rows.items():
        shared_key = tuple(assignment[i] for i in right_shared_positions)
        keep_key = tuple(assignment[i] for i in right_keep_positions)
        right_index[shared_key].append((keep_key, value))
    output: dict[tuple[int, ...], object] = {}
    for left_assignment, left_value in left.rows.items():
        shared_key = tuple(left_assignment[i] for i in left_shared_positions)
        left_keep = tuple(left_assignment[i] for i in left_keep_positions)
        for right_keep, right_value in right_index.get(shared_key, ()):
            key = left_keep + right_keep
            value = multiply(left_value, right_value)
            output[key] = add(output.get(key, zero), value)
    output = {key: value for key, value in output.items() if value != zero}
    return Relation(output_labels, output, left.factors + right.factors, f"({left.name}*{right.name})")


def relation_factors(
    descriptor: Sequence[Sequence[int]], direct: dict, conjugate: dict
) -> dict[str, Relation]:
    labels = factor_labels(descriptor)
    return {
        **{
            f"A{r}": make_factor_relation(f"A{r}", labels[f"A{r}"], direct)
            for r in range(4)
        },
        **{
            f"B{s}": make_factor_relation(f"B{s}", labels[f"B{s}"], conjugate)
            for s in range(4)
        },
    }


def contract_relation(
    descriptor: Sequence[Sequence[int]],
    direct: dict,
    conjugate: dict,
    plan,
    add: Callable,
    multiply: Callable,
    zero: object,
) -> tuple[object, list[dict]]:
    factors = relation_factors(descriptor, direct, conjugate)
    results: list[Relation] = []
    trace = []

    def resolve(name: str) -> Relation:
        return results[int(name[1:])] if name.startswith("$") else factors[name]

    for left_name, right_name in plan:
        left = resolve(left_name)
        right = resolve(right_name)
        merged = merge_relation(left, right, add, multiply, zero)
        results.append(merged)
        trace.append(
            {
                "left": left_name,
                "right": right_name,
                "left_rows": len(left.rows),
                "right_rows": len(right.rows),
                "output_rows": len(merged.rows),
                "output_rank": len(merged.labels),
            }
        )
    final = results[-1]
    if final.labels or set(final.rows) != {()}:
        raise AssertionError(("contraction did not close", final.labels, final.rows.keys()))
    return final.rows[()], trace


def contract_mod(descriptor, direct: dict, conjugate: dict, plan) -> tuple[int, list[dict]]:
    return contract_relation(
        descriptor,
        direct,
        conjugate,
        plan,
        lambda a, b: (a + b) % P,
        lambda a, b: (a * b) % P,
        0,
    )


def contract_q6_numerators(descriptor, direct: dict, conjugate: dict, plan) -> tuple[Q6, list[dict]]:
    return contract_relation(
        descriptor,
        direct,
        conjugate,
        plan,
        lambda a, b: a + b,
        lambda a, b: a * b,
        Q6(),
    )


@dataclass
class ExactFactor:
    name: str
    labels: tuple[tuple[int, int], ...]
    rows: tuple[tuple[tuple[int, ...], object], ...]
    indexes: dict[int, dict[tuple[int, ...], tuple[tuple[tuple[int, ...], object], ...]]]

    def candidates(self, assignments: dict[tuple[int, int], int]):
        mask = sum(1 << i for i, label in enumerate(self.labels) if label in assignments)
        if mask not in self.indexes:
            positions = tuple(i for i in range(4) if mask >> i & 1)
            index: dict[tuple[int, ...], list] = defaultdict(list)
            for values, token in self.rows:
                key = tuple(values[i] for i in positions)
                index[key].append((values, token))
            self.indexes[mask] = {key: tuple(value) for key, value in index.items()}
        positions = tuple(i for i in range(4) if mask >> i & 1)
        key = tuple(assignments[self.labels[i]] for i in positions)
        return self.indexes[mask].get(key, ())


def exact_factor_set(descriptor, direct_tokens: dict, conjugate_tokens: dict) -> dict[str, ExactFactor]:
    labels = factor_labels(descriptor)
    output = {}
    for prefix, tokens in (("A", direct_tokens), ("B", conjugate_tokens)):
        for copy in range(4):
            name = f"{prefix}{copy}"
            output[name] = ExactFactor(name, labels[name], tuple(tokens.items()), {})
    return output


GOLDEN_DFS_PRIMARY = ("A0", "B3", "A3", "B2", "A2", "B1", "B0", "A1")
GOLDEN_DFS_ALTERNATE = ("A1", "B0", "A2", "B1", "A3", "B2", "B3", "A0")


def golden_signature_contraction(tokens: dict, descriptor, factor_order) -> tuple[Counter, dict]:
    direct = tokens
    conjugate = {
        indices: (label, (-exponent) % 20)
        for indices, (label, exponent) in tokens.items()
    }
    factors = exact_factor_set(descriptor, direct, conjugate)
    assignments: dict[tuple[int, int], int] = {}
    signature: Counter = Counter()
    nodes = [0] * 9

    def visit(depth: int, na: int, nb: int, nc: int, exponent: int) -> None:
        nodes[depth] += 1
        if depth == 8:
            signature[(na, nb, nc, exponent % 20)] += 1
            return
        factor = factors[factor_order[depth]]
        for values, token in factor.candidates(assignments):
            added = []
            consistent = True
            for label, value in zip(factor.labels, values):
                if label in assignments:
                    if assignments[label] != value:
                        consistent = False
                        break
                else:
                    assignments[label] = value
                    added.append(label)
            if consistent:
                amplitude, phase = token
                visit(
                    depth + 1,
                    na + (amplitude == "a"),
                    nb + (amplitude == "b"),
                    nc + (amplitude == "c"),
                    (exponent + phase) % 20,
                )
            for label in added:
                del assignments[label]

    visit(0, 0, 0, 0, 0)
    return signature, {"factor_order": factor_order, "nodes_by_depth": nodes, "leaves": sum(signature.values())}


def evaluate_golden_signature(signature: Counter) -> K120:
    amplitudes = golden_amplitudes_exact()
    powers = {
        label: tuple(amplitudes[label] ** exponent for exponent in range(9))
        for label in ("a", "b", "c")
    }
    result = K120()
    for (na, nb, nc, exponent), count in sorted(signature.items()):
        result += (
            count
            * powers["a"][na]
            * powers["b"][nb]
            * powers["c"][nc]
            * XI_POWERS[(6 * exponent) % 120]
        )
    return result


def fingerprint(values: Sequence):
    if len(values) != 4:
        raise ValueError("four descriptor values required")
    v0, v1, v2, v3 = values
    return (
        v0,
        v1 + v2 + v3,
        v1 * v2 + v1 * v3 + v2 * v3,
        v1 * v2 * v3,
    )


def fingerprint_mod(values: Sequence[int]) -> tuple[int, int, int, int]:
    v0, e1, e2, e3 = fingerprint(values)
    return v0 % P, e1 % P, e2 % P, e3 % P


def serialize_signature(signature: Counter) -> list[dict]:
    return [
        {
            "n_a": key[0],
            "n_b": key[1],
            "n_c": key[2],
            "exponent_mod20": key[3],
            "multiplicity": value,
        }
        for key, value in sorted(signature.items())
    ]
