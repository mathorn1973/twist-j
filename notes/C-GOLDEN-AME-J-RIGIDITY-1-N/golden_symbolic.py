#!/usr/bin/env python3
"""Publicly locked construction freeze for preregistration issue #369.

The public issue lock fixes the golden AME(4,6) construction scope.  This
module deliberately does *construction only*:

* construction A parses the pinned 36-by-36 MATLAB literal directly;
* construction B reconstructs the same tensor from a frozen nine-block
  4-by-4 presentation of the partial-transpose flattening;
* the polynomial Gram equations can be serialized, counted and hashed;
* no Groebner basis, radical, elimination, saturation, factorization,
  ideal-membership test, or target-relation test is implemented here.

The formal coefficient ring used by the equation generator is

    Q[a,b,c,x,y] / (x*y - 1),

with involution a*=a, b*=b, c*=c, x*=y, y*=x.  Source exponents are literal
integers in 0..19.  In particular, this module never reduces exponents and
never imposes any finite order on x.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
import hashlib
import json
import re
from typing import Iterable, Iterator, Mapping, Sequence


DIMENSION = 6
FLATTENINGS = ((0, 1), (0, 2), (0, 3))

ORIGINAL_PIN = {
    "repository": "https://github.com/matrix-toolbox/AME_4_6.git",
    "commit": "1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8",
    "path": "AME46_ORIGINAL.m",
    "bytes": 8515,
    "sha256": "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae",
    "git_blob_sha1": "e0d0e171d58b3360c39595d677ffc401a466112d",
}

# Auxiliary provenance for the two permutations used by the 9 x (4 x 4)
# view.  It is from the same repository and the same immutable commit as the
# normative AME46_ORIGINAL.m source.  Construction B below is self-contained
# after this fixture is frozen; it does not parse construction A.
BLOCK944_PIN = {
    "repository": "https://github.com/matrix-toolbox/AME_4_6.git",
    "commit": "1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8",
    "path": "block944.m",
    "bytes": 8234,
    "sha256": "af0aac863f54beb2c8396368fd87102e75192a38ec77efee0605210123540649",
    "git_blob_sha1": "caab29cb76e60e3165abf70931cf35e387b6e3b1",
}


Index4 = tuple[int, int, int, int]
Token = tuple[str, int]
Tensor = dict[Index4, Token]
Monomial = tuple[int, int, int, int, int]  # a,b,c,x,y exponents
Polynomial = dict[Monomial, int]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def verify_pin(data: bytes, pin: Mapping[str, object]) -> None:
    if len(data) != pin["bytes"]:
        raise AssertionError(("byte count", len(data), pin["bytes"]))
    if sha256_bytes(data) != pin["sha256"]:
        raise AssertionError("SHA-256 source pin mismatch")
    if git_blob_sha1(data) != pin["git_blob_sha1"]:
        raise AssertionError("git blob source pin mismatch")


def _strip_matlab_comments(text: str) -> str:
    return "\n".join(line.split("%", 1)[0] for line in text.splitlines())


def _parse_literal_rows(block: str, token_pattern: str, allowed: set[str]) -> list[list[str]]:
    clean = _strip_matlab_comments(block)
    rows = [row.strip() for row in clean.split(";") if row.strip()]
    if len(rows) != 36:
        raise ValueError(f"expected 36 rows, found {len(rows)}")
    output: list[list[str]] = []
    for row_number, row in enumerate(rows):
        tokens = re.findall(token_pattern, row)
        if len(tokens) != 36:
            raise ValueError(
                f"row {row_number}: expected 36 tokens, found {len(tokens)}"
            )
        if not set(tokens) <= allowed:
            raise ValueError(("unexpected token", row_number, set(tokens) - allowed))
        output.append(tokens)
    return output


def construct_a_direct(data: bytes) -> Tensor:
    """Construction A: strict direct parser of the pinned MATLAB literal."""

    verify_pin(data, ORIGINAL_PIN)
    text = data.decode("utf-8")
    matches = re.findall(
        r"\bU\s*=\s*\[(.*?)\]\s*\.\*\s*w\.\^\s*\[(.*?)\]\s*;",
        text,
        re.S,
    )
    if len(matches) != 1:
        raise ValueError(f"expected one U amplitude/exponent literal, found {len(matches)}")
    amplitude_block, exponent_block = matches[0]
    amplitudes = _parse_literal_rows(
        amplitude_block,
        r"(?<![A-Za-z0-9_])(?:0|a|b|c)(?![A-Za-z0-9_])",
        {"0", "a", "b", "c"},
    )
    exponents = _parse_literal_rows(
        exponent_block,
        r"(?<![A-Za-z0-9_])(?:[0-9]|1[0-9])(?![A-Za-z0-9_])",
        {str(value) for value in range(20)},
    )

    tensor: Tensor = {}
    for flat_row in range(36):
        for flat_column in range(36):
            label = amplitudes[flat_row][flat_column]
            if label == "0":
                continue
            exponent = int(exponents[flat_row][flat_column])
            if not 0 <= exponent <= 19:
                raise AssertionError("source exponent outside literal range 0..19")
            i, j = divmod(flat_row, DIMENSION)
            k, ell = divmod(flat_column, DIMENSION)
            tensor[(i, j, k, ell)] = (label, exponent)
    return tensor


# For G = T^(partial transpose on the second matrix subsystem), use
#
#     G_(6*i+ell, 6*k+j) = T_(i,j,k,ell).
#
# In the nine-block coordinates, output row/column slot q maps back to the
# following old G row/column.  The row map is read from P1.  The column map is
# the inverse orientation induced by right multiplication with P2.
BLOCK_ROW_TO_G_ROW = (
    8, 9, 28, 29,
    2, 3, 18, 19,
    0, 1, 22, 23,
    26, 27, 6, 7,
    4, 5, 20, 21,
    34, 35, 12, 13,
    30, 31, 14, 15,
    10, 11, 24, 25,
    32, 33, 16, 17,
)

BLOCK_COL_TO_G_COL = (
    25, 31, 10, 4,
    1, 7, 16, 22,
    0, 6, 27, 33,
    15, 24, 30, 21,
    17, 23, 26, 32,
    19, 13, 28, 34,
    29, 35, 2, 8,
    14, 20, 5, 11,
    9, 3, 12, 18,
)

# Nine diagonal 4-by-4 blocks.  None means structural zero.  A nonzero cell
# (label,r) means label*x**r, with r a literal integer rather than a residue
# class assumed by the symbolic construction.
BLOCKS: tuple[tuple[tuple[Token | None, ...], ...], ...] = (
    (
        (("c", 7), None, ("b", 5), ("a", 2)),
        (None, ("c", 19), ("a", 14), ("b", 1)),
        (None, ("c", 10), ("a", 15), ("b", 2)),
        (("c", 0), None, ("b", 8), ("a", 5)),
    ),
    (
        (("c", 17), None, ("b", 0), ("a", 5)),
        (None, ("c", 19), ("a", 5), ("b", 0)),
        (("b", 10), ("a", 15), ("a", 4), ("b", 7)),
        (("a", 5), ("b", 0), ("b", 17), ("a", 10)),
    ),
    (
        (None, ("c", 0), ("a", 3), ("b", 0)),
        (("c", 0), None, ("b", 0), ("a", 7)),
        (("a", 1), ("b", 16), ("b", 10), ("a", 5)),
        (("b", 14), ("a", 19), ("a", 5), ("b", 10)),
    ),
    (
        (("c", 0), None, ("c", 10), None),
        (None, ("c", 14), None, ("c", 10)),
        (("c", 10), None, ("c", 10), None),
        (None, ("c", 0), None, ("c", 6)),
    ),
    (
        (("b", 14), ("a", 15), ("a", 18), ("b", 3)),
        (("a", 1), ("b", 12), ("b", 3), ("a", 18)),
        (("a", 0), ("b", 15), ("b", 14), ("a", 13)),
        (("b", 15), ("a", 0), ("a", 7), ("b", 16)),
    ),
    (
        (("c", 0), None, ("c", 1), None),
        (None, ("c", 16), None, ("c", 11)),
        (("c", 2), None, ("c", 13), None),
        (None, ("c", 2), None, ("c", 7)),
    ),
    (
        (("b", 9), ("a", 16), ("a", 10), ("b", 5)),
        (("a", 16), ("b", 13), ("b", 15), ("a", 0)),
        (("a", 12), ("b", 1), None, ("c", 19)),
        (("b", 15), ("a", 14), ("c", 5), None),
    ),
    (
        (("a", 2), ("b", 13), ("b", 4), ("a", 9)),
        (("b", 19), ("a", 0), ("a", 3), ("b", 18)),
        (("b", 7), ("a", 0), ("c", 0), None),
        (("a", 10), ("b", 13), None, ("c", 0)),
    ),
    (
        (("a", 7), ("b", 14), None, ("c", 10)),
        (("b", 6), ("a", 3), ("c", 0), None),
        (("b", 4), ("a", 1), ("c", 8), None),
        (("a", 3), ("b", 10), None, ("c", 16)),
    ),
)


def construct_b_blocks() -> Tensor:
    """Construction B: reconstruct T from the frozen 9 x (4 x 4) fixture."""

    if sorted(BLOCK_ROW_TO_G_ROW) != list(range(36)):
        raise AssertionError("row fixture is not a permutation")
    if sorted(BLOCK_COL_TO_G_COL) != list(range(36)):
        raise AssertionError("column fixture is not a permutation")
    if len(BLOCKS) != 9:
        raise AssertionError("expected nine blocks")

    tensor: Tensor = {}
    for block_number, block in enumerate(BLOCKS):
        if len(block) != 4 or any(len(row) != 4 for row in block):
            raise AssertionError(("bad 4-by-4 block", block_number))
        for inner_row in range(4):
            for inner_column in range(4):
                token = block[inner_row][inner_column]
                if token is None:
                    continue
                new_row = 4 * block_number + inner_row
                new_column = 4 * block_number + inner_column
                g_row = BLOCK_ROW_TO_G_ROW[new_row]
                g_column = BLOCK_COL_TO_G_COL[new_column]
                i, ell = divmod(g_row, DIMENSION)
                k, j = divmod(g_column, DIMENSION)
                indices = (i, j, k, ell)
                if indices in tensor:
                    raise AssertionError(("duplicate reconstructed entry", indices))
                tensor[indices] = token
    return tensor


def flatten_tensor(tensor: Mapping[Index4, object], row_parties: tuple[int, int]):
    column_parties = tuple(party for party in range(4) if party not in row_parties)
    rows: list[dict[int, object]] = [dict() for _ in range(36)]
    for indices, value in tensor.items():
        row = 6 * indices[row_parties[0]] + indices[row_parties[1]]
        column = 6 * indices[column_parties[0]] + indices[column_parties[1]]
        if column in rows[row]:
            raise AssertionError(("duplicate matrix cell", row_parties, row, column))
        rows[row][column] = value
    return rows


def token_monomial(token: Token, conjugated: bool = False) -> Monomial:
    label, exponent = token
    amplitude = {"a": [1, 0, 0], "b": [0, 1, 0], "c": [0, 0, 1]}[label]
    # No reduction modulo 20.  Involution sends x**r to y**r.
    return (
        amplitude[0],
        amplitude[1],
        amplitude[2],
        0 if conjugated else exponent,
        exponent if conjugated else 0,
    )


def multiply_monomials(left: Monomial, right: Monomial) -> Monomial:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def normalize_polynomial(terms: Mapping[Monomial, int]) -> Polynomial:
    return {monomial: coefficient for monomial, coefficient in terms.items() if coefficient}


@dataclass(frozen=True)
class GramEquation:
    row_parties: tuple[int, int] | None
    left_row: int
    right_row: int
    polynomial: Polynomial

    @property
    def tag(self) -> str:
        if self.row_parties is None:
            return "unit_phase"
        return f"{self.row_parties[0]}{self.row_parties[1]}:{self.left_row:02d}:{self.right_row:02d}"


def gram_equations(tensor: Mapping[Index4, Token]) -> tuple[GramEquation, ...]:
    """Build, but do not solve, the complete frozen polynomial system.

    There are 3*36*36 ordered row-Gram coordinates plus x*y-1.  Identically
    empty coordinates remain present in the serialization so that the target
    system cannot silently change after the public pin.
    """

    output: list[GramEquation] = []
    for row_parties in FLATTENINGS:
        rows = flatten_tensor(tensor, row_parties)
        for left_row in range(36):
            for right_row in range(36):
                terms: Counter[Monomial] = Counter()
                common_columns = sorted(set(rows[left_row]).intersection(rows[right_row]))
                for column in common_columns:
                    left = token_monomial(rows[left_row][column], conjugated=False)
                    right = token_monomial(rows[right_row][column], conjugated=True)
                    terms[multiply_monomials(left, right)] += 1
                if left_row == right_row:
                    terms[(0, 0, 0, 0, 0)] -= 1
                output.append(
                    GramEquation(
                        row_parties,
                        left_row,
                        right_row,
                        normalize_polynomial(terms),
                    )
                )

    output.append(
        GramEquation(
            None,
            0,
            0,
            {
                (0, 0, 0, 1, 1): 1,
                (0, 0, 0, 0, 0): -1,
            },
        )
    )
    return tuple(output)


def serialize_equations(equations: Iterable[GramEquation]) -> bytes:
    serial = []
    for equation in equations:
        terms = [
            [list(monomial), coefficient]
            for monomial, coefficient in sorted(equation.polynomial.items())
        ]
        serial.append({"tag": equation.tag, "terms": terms})
    return (json.dumps(serial, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")


def structural_report(tensor: Mapping[Index4, Token]) -> dict[str, object]:
    label_counts = Counter(label for label, _ in tensor.values())
    exponent_counts = Counter(exponent for _, exponent in tensor.values())
    flattenings = {}
    for row_parties in FLATTENINGS:
        rows = flatten_tensor(tensor, row_parties)
        row_support = Counter(len(row) for row in rows)
        overlaps = Counter()
        raw_gram_terms = 0
        for left in range(36):
            for right in range(36):
                overlap = len(set(rows[left]).intersection(rows[right]))
                overlaps[overlap] += 1
                raw_gram_terms += overlap
        flattenings["".join(map(str, row_parties))] = {
            "row_support_histogram": dict(sorted(row_support.items())),
            "ordered_overlap_histogram": dict(sorted(overlaps.items())),
            "raw_gram_terms": raw_gram_terms,
        }

    equations = gram_equations(tensor)
    equation_bytes = serialize_equations(equations)
    active = sum(bool(equation.polynomial) for equation in equations)
    return {
        "support": len(tensor),
        "label_counts": dict(sorted(label_counts.items())),
        "literal_exponent_histogram": dict(sorted(exponent_counts.items())),
        "block_nonzero_counts": [
            sum(cell is not None for row in block for cell in row) for block in BLOCKS
        ],
        "flattenings": flattenings,
        "equation_coordinates_including_xy": len(equations),
        "active_equations_including_xy": active,
        "equation_serialization_bytes": len(equation_bytes),
        "equation_serialization_sha256": sha256_bytes(equation_bytes),
    }


def parse_block944_permutations(data: bytes) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Independently parse P1/P2 only, for provenance of the block fixture."""

    verify_pin(data, BLOCK944_PIN)
    text = data.decode("utf-8")

    def one_permutation(name: str) -> tuple[int, ...]:
        matches = re.findall(rf"\b{name}\s*=\s*\[(.*?)\];", text, re.S)
        if len(matches) != 1:
            raise ValueError(("permutation literal count", name, len(matches)))
        clean = _strip_matlab_comments(matches[0])
        rows = [row for row in clean.split(";") if row.strip()]
        if len(rows) != 36:
            raise ValueError((name, "row count", len(rows)))
        positions = []
        for row_number, row in enumerate(rows):
            tokens = re.findall(
                r"(?<![A-Za-z0-9_])(?:o|0|1)(?![A-Za-z0-9_])", row
            )
            if len(tokens) != 36:
                raise ValueError((name, row_number, "token count", len(tokens)))
            ones = [index for index, token in enumerate(tokens) if token == "1"]
            if len(ones) != 1:
                raise ValueError((name, row_number, "ones", ones))
            positions.append(ones[0])
        if sorted(positions) != list(range(36)):
            raise ValueError((name, "not a permutation"))
        return tuple(positions)

    p1_row_to_old_row = one_permutation("P1")
    p2_old_row_to_new_column = one_permutation("P2")
    p2_new_column_to_old_column = [0] * 36
    for old_column, new_column in enumerate(p2_old_row_to_new_column):
        p2_new_column_to_old_column[new_column] = old_column
    return p1_row_to_old_row, tuple(p2_new_column_to_old_column)
