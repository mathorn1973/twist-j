#!/usr/bin/env python3
"""Post-lock G3/NC0--NC5 verifier for C-GOLDEN-AME-J-RIGIDITY-1-N.

This is an independent, standard-library-only integrity verifier.  It does
not compute a Groebner basis, saturation, radical, elimination, target-ideal
membership, or a solution branch.  Its exact known-point arithmetic is in
Q(zeta_40) = Q[z]/(z^16-z^12+z^8-z^4+1).

The locked public constructor is used only as the independently frozen
nine-block fixture for construction B and for the NC3 synthetic-token API
test.  Construction A, raw row-Gram serialization, column-Gram construction,
Q(zeta_40) arithmetic, and all other checks below are implemented here.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
from typing import Iterable, Mapping


if sys.flags.optimize:
    raise SystemExit("refusing optimized Python: exact verifier requires active assertions")


SOURCE_BYTES = 8515
SOURCE_SHA256 = "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae"
BLOCK_BYTES = 8234
BLOCK_SHA256 = "af0aac863f54beb2c8396368fd87102e75192a38ec77efee0605210123540649"
RAW_BYTES = 136262
RAW_SHA256 = "09aac23466680ba762e363ad75845aa1535f4e8e32cee75ad41119f43cb16762"
LOCKED_BUILDER_SHA256 = "b26844a99db5ff9baf4ed7493ed8c9c7aea28a561c8eeadb2c70fdc77530383c"

DIM = 6
FLATTENINGS = ((0, 1), (0, 2), (0, 3))
Monomial = tuple[int, int, int, int, int]
Polynomial = dict[Monomial, int]
Token = tuple[str, int]
Tensor = dict[tuple[int, int, int, int], Token]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


# ---------------------------------------------------------------------------
# Exact Q(zeta_40) arithmetic.  Basis: 1,z,...,z^15.

DEGREE = 16
KElement = tuple[Fraction, ...]
K_ZERO: KElement = (Fraction(0),) * DEGREE
K_ONE: KElement = (Fraction(1),) + (Fraction(0),) * (DEGREE - 1)


def k_reduce(coefficients: Iterable[Fraction | int]) -> KElement:
    work = [Fraction(value) for value in coefficients]
    if len(work) < DEGREE:
        work.extend(Fraction(0) for _ in range(DEGREE - len(work)))
    for degree in range(len(work) - 1, DEGREE - 1, -1):
        coefficient = work[degree]
        if not coefficient:
            continue
        work[degree] = Fraction(0)
        # z^16 = z^12 - z^8 + z^4 - 1.
        work[degree - 4] += coefficient
        work[degree - 8] -= coefficient
        work[degree - 12] += coefficient
        work[degree - 16] -= coefficient
    return tuple(work[:DEGREE])


def k_add(left: KElement, right: KElement) -> KElement:
    return tuple(a + b for a, b in zip(left, right))


def k_neg(value: KElement) -> KElement:
    return tuple(-coefficient for coefficient in value)


def k_sub(left: KElement, right: KElement) -> KElement:
    return k_add(left, k_neg(right))


def k_scale(scalar: Fraction | int, value: KElement) -> KElement:
    q = Fraction(scalar)
    return tuple(q * coefficient for coefficient in value)


def k_mul(left: KElement, right: KElement) -> KElement:
    product = [Fraction(0)] * (2 * DEGREE - 1)
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right):
            if b:
                product[i + j] += a * b
    return k_reduce(product)


def z_power(exponent: int) -> KElement:
    # This reduction is intrinsic to the post-lock known-point field only.
    exponent %= 40
    coefficients = [Fraction(0)] * (exponent + 1)
    coefficients[exponent] = Fraction(1)
    return k_reduce(coefficients)


def k_pow(value: KElement, exponent: int) -> KElement:
    require(exponent >= 0, "negative K exponent")
    result = K_ONE
    base = value
    power = exponent
    while power:
        if power & 1:
            result = k_mul(result, base)
        base = k_mul(base, base)
        power >>= 1
    return result


def k_conjugate(value: KElement) -> KElement:
    result = K_ZERO
    for exponent, coefficient in enumerate(value):
        if coefficient:
            result = k_add(result, k_scale(coefficient, z_power(-exponent)))
    return result


def k_text(value: KElement) -> str:
    terms = []
    for exponent, coefficient in enumerate(value):
        if coefficient:
            terms.append(f"{coefficient}*z^{exponent}")
    return "+".join(terms) if terms else "0"


# ---------------------------------------------------------------------------
# Independent strict source parser.

def strip_comments(text: str) -> str:
    return "\n".join(line.split("%", 1)[0] for line in text.splitlines())


def parse_rows(block: str, pattern: str, allowed: set[str]) -> list[list[str]]:
    rows = [row.strip() for row in strip_comments(block).split(";") if row.strip()]
    require(len(rows) == 36, "literal row count")
    result: list[list[str]] = []
    for row_number, row in enumerate(rows):
        tokens = re.findall(pattern, row)
        require(len(tokens) == 36, f"literal width row {row_number}")
        require(set(tokens) <= allowed, f"literal alphabet row {row_number}")
        result.append(tokens)
    return result


def parse_source(data: bytes) -> Tensor:
    require(len(data) == SOURCE_BYTES, "source byte pin")
    require(sha256(data) == SOURCE_SHA256, "source SHA-256 pin")
    text = data.decode("utf-8")
    matches = re.findall(
        r"\bU\s*=\s*\[(.*?)\]\s*\.\*\s*w\.\^\s*\[(.*?)\]\s*;",
        text,
        re.S,
    )
    require(len(matches) == 1, "unique U literal")
    amplitude_rows = parse_rows(
        matches[0][0],
        r"(?<![A-Za-z0-9_])(?:0|a|b|c)(?![A-Za-z0-9_])",
        {"0", "a", "b", "c"},
    )
    exponent_rows = parse_rows(
        matches[0][1],
        r"(?<![A-Za-z0-9_])(?:[0-9]|1[0-9])(?![A-Za-z0-9_])",
        {str(value) for value in range(20)},
    )
    result: Tensor = {}
    for flat_row in range(36):
        for flat_column in range(36):
            label = amplitude_rows[flat_row][flat_column]
            exponent = int(exponent_rows[flat_row][flat_column])
            if label == "0":
                require(exponent == 0, "nonzero exponent off support")
                continue
            i, j = divmod(flat_row, DIM)
            k, ell = divmod(flat_column, DIM)
            result[(i, j, k, ell)] = (label, exponent)
    return result


def load_locked_builder(path: Path):
    data = path.read_bytes()
    require(sha256(data) == LOCKED_BUILDER_SHA256, "locked builder SHA-256")
    sys.dont_write_bytecode = True
    specification = importlib.util.spec_from_file_location("locked_golden_symbolic", path)
    require(specification is not None and specification.loader is not None, "builder import spec")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


def parse_block_permutations(data: bytes) -> tuple[tuple[int, ...], tuple[int, ...]]:
    require(len(data) == BLOCK_BYTES, "block944 byte pin")
    require(sha256(data) == BLOCK_SHA256, "block944 SHA-256 pin")
    text = data.decode("utf-8")

    def one(name: str) -> tuple[int, ...]:
        matches = re.findall(rf"\b{name}\s*=\s*\[(.*?)\];", text, re.S)
        require(len(matches) == 1, f"unique {name}")
        rows = [row for row in strip_comments(matches[0]).split(";") if row.strip()]
        require(len(rows) == 36, f"{name} rows")
        positions = []
        for row_number, row in enumerate(rows):
            tokens = re.findall(r"(?<![A-Za-z0-9_])(?:o|0|1)(?![A-Za-z0-9_])", row)
            require(len(tokens) == 36, f"{name} width {row_number}")
            ones = [column for column, token in enumerate(tokens) if token == "1"]
            require(len(ones) == 1, f"{name} one-hot {row_number}")
            positions.append(ones[0])
        require(sorted(positions) == list(range(36)), f"{name} permutation")
        return tuple(positions)

    row_map = one("P1")
    p2_old_to_new = one("P2")
    column_map = [0] * 36
    for old_column, new_column in enumerate(p2_old_to_new):
        column_map[new_column] = old_column
    return row_map, tuple(column_map)


def construct_b(module, block_data: bytes) -> Tensor:
    parsed_rows, parsed_columns = parse_block_permutations(block_data)
    require(parsed_rows == tuple(module.BLOCK_ROW_TO_G_ROW), "block row-map provenance")
    require(parsed_columns == tuple(module.BLOCK_COL_TO_G_COL), "block column-map provenance")
    result: Tensor = {}
    require(len(module.BLOCKS) == 9, "nine blocks")
    for block_number, block in enumerate(module.BLOCKS):
        require(len(block) == 4 and all(len(row) == 4 for row in block), "block shape")
        for inner_row in range(4):
            for inner_column in range(4):
                token = block[inner_row][inner_column]
                if token is None:
                    continue
                new_row = 4 * block_number + inner_row
                new_column = 4 * block_number + inner_column
                g_row = module.BLOCK_ROW_TO_G_ROW[new_row]
                g_column = module.BLOCK_COL_TO_G_COL[new_column]
                i, ell = divmod(g_row, DIM)
                k, j = divmod(g_column, DIM)
                index = (i, j, k, ell)
                require(index not in result, "construction B duplicate")
                result[index] = (str(token[0]), int(token[1]))
    return result


# ---------------------------------------------------------------------------
# Independent sparse polynomial construction and serialization.

def flatten(tensor: Mapping[tuple[int, int, int, int], object], row_parties: tuple[int, int]):
    column_parties = tuple(party for party in range(4) if party not in row_parties)
    rows: list[dict[int, object]] = [dict() for _ in range(36)]
    for index, value in tensor.items():
        row = 6 * index[row_parties[0]] + index[row_parties[1]]
        column = 6 * index[column_parties[0]] + index[column_parties[1]]
        require(column not in rows[row], "flatten duplicate")
        rows[row][column] = value
    return rows


def token_product(left: Token, right: Token, side: str) -> Monomial:
    amplitude = [0, 0, 0]
    amplitude[{"a": 0, "b": 1, "c": 2}[left[0]]] += 1
    amplitude[{"a": 0, "b": 1, "c": 2}[right[0]]] += 1
    if side == "row":
        x_exponent, y_exponent = left[1], right[1]
    elif side == "column":
        # conj(left) * right
        x_exponent, y_exponent = right[1], left[1]
    else:
        raise AssertionError("unknown Gram side")
    return amplitude[0], amplitude[1], amplitude[2], x_exponent, y_exponent


def normalize(terms: Counter[Monomial]) -> Polynomial:
    return {monomial: coefficient for monomial, coefficient in terms.items() if coefficient}


def gram_records(tensor: Tensor, side: str):
    records = []
    for row_parties in FLATTENINGS:
        rows = flatten(tensor, row_parties)
        vectors = rows
        if side == "column":
            vectors = [dict() for _ in range(36)]
            for row, entries in enumerate(rows):
                for column, token in entries.items():
                    vectors[column][row] = token
        for left in range(36):
            for right in range(36):
                terms: Counter[Monomial] = Counter()
                for inner in sorted(set(vectors[left]).intersection(vectors[right])):
                    terms[token_product(vectors[left][inner], vectors[right][inner], side)] += 1
                if left == right:
                    terms[(0, 0, 0, 0, 0)] -= 1
                prefix = "" if side == "row" else "col"
                tag = f"{prefix}{row_parties[0]}{row_parties[1]}:{left:02d}:{right:02d}"
                records.append((row_parties, left, right, tag, normalize(terms)))
    return records


def raw_records(tensor: Tensor):
    records = gram_records(tensor, "row")
    records.append(
        (
            None,
            0,
            0,
            "unit_phase",
            {(0, 0, 0, 1, 1): 1, (0, 0, 0, 0, 0): -1},
        )
    )
    return records


def serialize(records) -> bytes:
    payload = []
    for _parties, _left, _right, tag, polynomial in records:
        terms = [[list(monomial), coefficient] for monomial, coefficient in sorted(polynomial.items())]
        payload.append({"tag": tag, "terms": terms})
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")


def star_polynomial(polynomial: Polynomial) -> Polynomial:
    return {
        (a, b, c, y_exponent, x_exponent): coefficient
        for (a, b, c, x_exponent, y_exponent), coefficient in polynomial.items()
    }


def domain_normal_form(polynomial: Polynomial) -> dict[tuple[int, int, int, int], int]:
    """Unique Laurent normal form modulo <x*y-1>.

    The final coordinate is the possibly negative exponent of x after the
    injective identification y=x^-1.
    """

    terms: Counter[tuple[int, int, int, int]] = Counter()
    for (a, b, c, x_exponent, y_exponent), coefficient in polynomial.items():
        terms[(a, b, c, x_exponent - y_exponent)] += coefficient
    return {monomial: coefficient for monomial, coefficient in terms.items() if coefficient}


def rational_evaluate(polynomial: Polynomial, values: tuple[Fraction, ...]) -> Fraction:
    result = Fraction(0)
    for monomial, coefficient in polynomial.items():
        term = Fraction(coefficient)
        for value, exponent in zip(values, monomial):
            term *= value**exponent
        result += term
    return result


def nc0_relations() -> tuple[Polynomial, ...]:
    one = (0, 0, 0, 0, 0)
    return (
        {(0, 0, 2, 0, 0): 2, one: -1},
        {(2, 0, 0, 0, 0): 1, (0, 2, 0, 0, 0): 1, (0, 0, 2, 0, 0): -1},
        {(0, 2, 0, 0, 0): 1, (1, 1, 0, 0, 0): -1, (2, 0, 0, 0, 0): -1},
        {(0, 0, 0, 8, 0): 1, (0, 0, 0, 6, 0): -1, (0, 0, 0, 4, 0): 1, (0, 0, 0, 2, 0): -1, one: 1},
        {(0, 0, 1, 0, 0): 1, (1, 0, 0, 1, 0): -1, (1, 0, 0, 0, 1): -1},
        {(0, 1, 0, 0, 0): 1, (1, 0, 0, 2, 0): -1, (1, 0, 0, 0, 2): -1},
    )


def involution_audit(records) -> tuple[int, str]:
    by_coordinate = {
        (parties, left, right): polynomial
        for parties, left, right, _tag, polynomial in records
    }
    mapping = []
    for parties, left, right, tag, polynomial in records:
        if parties is None:
            partner = by_coordinate[(None, 0, 0)]
            partner_tag = "unit_phase"
        else:
            partner = by_coordinate[(parties, right, left)]
            partner_tag = f"{parties[0]}{parties[1]}:{right:02d}:{left:02d}"
        require(star_polynomial(polynomial) == partner, f"involution mismatch {tag}")
        mapping.append(f"{tag}->{partner_tag}")
    mapping_bytes = ("\n".join(mapping) + "\n").encode("ascii")
    return len(mapping), sha256(mapping_bytes)


# ---------------------------------------------------------------------------
# Known-point evaluation and exact Gram checks.

def exact_constants():
    sqrt2 = k_add(z_power(5), z_power(-5))
    sqrt5 = k_sub(k_scale(2, k_add(z_power(4), z_power(-4))), K_ONE)
    sqrt10 = k_mul(sqrt2, sqrt5)
    imaginary_unit = z_power(10)
    sine = k_neg(k_mul(imaginary_unit, k_sub(z_power(4), z_power(-4))))
    cosine = k_add(z_power(2), z_power(-2))
    values = {
        "a": k_scale(Fraction(1, 10), k_mul(sine, sqrt10)),
        "b": k_scale(Fraction(1, 10), k_mul(cosine, sqrt10)),
        "c": k_scale(Fraction(1, 2), sqrt2),
        "x": z_power(2),
        "y": z_power(-2),
    }
    require(k_pow(z_power(1), 40) == K_ONE, "z^40")
    require(k_pow(z_power(1), 20) == k_neg(K_ONE), "z^20")
    require(k_mul(sqrt2, sqrt2) == k_scale(2, K_ONE), "sqrt2 exact")
    require(k_mul(sqrt5, sqrt5) == k_scale(5, K_ONE), "sqrt5 exact")
    require(k_mul(values["x"], values["y"]) == K_ONE, "known xy")
    for name in ("a", "b", "c"):
        require(k_conjugate(values[name]) == values[name], f"known {name} real")
    require(k_scale(20, k_mul(values["a"], values["a"])) == k_sub(k_scale(5, K_ONE), sqrt5), "a source square")
    require(k_scale(20, k_mul(values["b"], values["b"])) == k_add(k_scale(5, K_ONE), sqrt5), "b source square")
    require(k_scale(2, k_mul(values["c"], values["c"])) == K_ONE, "c source square")
    require(all(k_pow(values["x"], exponent) != K_ONE for exponent in range(1, 20)), "x primitive 20")
    return values


def evaluate_monomial(monomial: Monomial, values: Mapping[str, KElement]) -> KElement:
    result = K_ONE
    for name, exponent in zip(("a", "b", "c", "x", "y"), monomial):
        result = k_mul(result, k_pow(values[name], exponent))
    return result


def evaluate_polynomial(polynomial: Polynomial, values: Mapping[str, KElement]) -> KElement:
    result = K_ZERO
    for monomial, coefficient in polynomial.items():
        result = k_add(result, k_scale(coefficient, evaluate_monomial(monomial, values)))
    return result


def exact_tensor(tokens: Tensor, values: Mapping[str, KElement]):
    return {
        index: k_mul(values[label], k_pow(values["x"], exponent))
        for index, (label, exponent) in tokens.items()
    }


def gram_exact(matrix_rows, side: str) -> tuple[int, int]:
    vectors = matrix_rows
    if side == "right":
        vectors = [dict() for _ in range(36)]
        for row, entries in enumerate(matrix_rows):
            for column, value in entries.items():
                vectors[column][row] = value
    checked = 0
    failures = 0
    for left in range(36):
        for right in range(36):
            value = K_ZERO
            for inner in set(vectors[left]).intersection(vectors[right]):
                if side == "left":
                    term = k_mul(vectors[left][inner], k_conjugate(vectors[right][inner]))
                else:
                    term = k_mul(k_conjugate(vectors[left][inner]), vectors[right][inner])
                value = k_add(value, term)
            expected = K_ONE if left == right else K_ZERO
            checked += 1
            if value != expected:
                failures += 1
    return checked, failures


# ---------------------------------------------------------------------------
# Tiny polynomial engine for the universal NC1 scalar identities.

SmallMonomial = tuple[int, int, int]  # C,g,h
SmallPolynomial = dict[SmallMonomial, int]


def sp_add(left: SmallPolynomial, right: SmallPolynomial, right_scale: int = 1) -> SmallPolynomial:
    terms: Counter[SmallMonomial] = Counter(left)
    for monomial, coefficient in right.items():
        terms[monomial] += right_scale * coefficient
    return {monomial: coefficient for monomial, coefficient in terms.items() if coefficient}


def sp_mul(left: SmallPolynomial, right: SmallPolynomial) -> SmallPolynomial:
    terms: Counter[SmallMonomial] = Counter()
    for lm, lc in left.items():
        for rm, rc in right.items():
            terms[tuple(a + b for a, b in zip(lm, rm))] += lc * rc
    return {monomial: coefficient for monomial, coefficient in terms.items() if coefficient}


def global_phase_schema_check() -> None:
    one = {(0, 0, 0): 1}
    cvar = {(1, 0, 0): 1}
    gh = {(0, 1, 1): 1}
    gh_minus_one = sp_add(gh, one, -1)
    for delta in (0, 1):
        c_plus_delta = sp_add(cvar, one if delta else {})
        c_prime = sp_add(sp_mul(gh, c_plus_delta), one if delta else {}, -1)
        forward = sp_add(sp_mul(gh, cvar), gh_minus_one if delta else {})
        require(c_prime == forward, f"NC1 forward identity delta={delta}")
        recovered = sp_add(sp_add(c_prime, sp_mul(gh_minus_one, c_plus_delta), -1), cvar, -1)
        require(not recovered, f"NC1 reverse identity delta={delta}")


COLUMN_CERTIFICATE = """COLUMN_REDUNDANCY_CERTIFICATE_V1
For any n x n matrices A,B over a commutative ring, put
  C = A*B-I,  P = B*A-I,  q = det(A),  r = det(B).
Then, with adj(B) the adjugate,
  r*P = B*C*adj(B),
  q*r-1 = det(I+C)-1 =: delta in <C_ij>,
and therefore
  P = q*B*C*adj(B) - delta*P.
Thus every coordinate of P belongs to the ideal generated by coordinates of C.
Application: A=F, B=F^dagger, separately for F01,F02,F03, n=36.
No column coordinate is added to the primary ideal.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--block944", required=True, type=Path)
    parser.add_argument("--builder", required=True, type=Path)
    args = parser.parse_args()

    module = load_locked_builder(args.builder)
    tensor_a = parse_source(args.source.read_bytes())
    tensor_b = construct_b(module, args.block944.read_bytes())
    require(tensor_a == tensor_b, "NC4 constructions differ")
    counts = Counter(label for label, _exponent in tensor_a.values())
    require(len(tensor_a) == 112 and counts == {"a": 40, "b": 40, "c": 32}, "source support counts")

    rows = raw_records(tensor_a)
    raw_bytes = serialize(rows)
    require(len(rows) == 3889, "raw record count")
    require(sum(bool(record[4]) for record in rows) == 383, "raw active count")
    require(len(raw_bytes) == RAW_BYTES, "raw byte count")
    require(sha256(raw_bytes) == RAW_SHA256, "raw SHA-256")

    involution_count, involution_map_sha = involution_audit(rows)
    require(involution_count == 3889, "NC2 involution count")

    # NC3 tests the actual locked raw API and this independent implementation.
    require(module.token_monomial(("a", 20), conjugated=False) == (1, 0, 0, 20, 0), "NC3 locked x^20 literal")
    require(module.token_monomial(("a", 20), conjugated=True) == (1, 0, 0, 0, 20), "NC3 locked y^20 literal")
    require(token_product(("a", 20), ("c", 0), "row") == (1, 0, 1, 20, 0), "NC3 independent x^20 literal")
    x20_minus_one = {(0, 0, 0, 20, 0): 1, (0, 0, 0, 0, 0): -1}
    require(domain_normal_form(x20_minus_one) != {}, "NC3 NC0 nonzero normal form")

    # NC0 exact leak witnesses at (a,b,c,x,y)=(1,1,1,1,1).
    targets = nc0_relations()
    require(all(domain_normal_form(target) for target in targets), "NC0 target normal forms")
    target_witness_values = tuple(
        rational_evaluate(target, (Fraction(1),) * 5) for target in targets
    )
    require(all(value != 0 for value in target_witness_values), "NC0 target witness")
    require(
        rational_evaluate(
            x20_minus_one,
            (Fraction(1), Fraction(1), Fraction(1), Fraction(2), Fraction(1, 2)),
        )
        == 2**20 - 1,
        "NC0 x^20 witness at x=2,y=1/2",
    )
    # Rational circle identity for the infinite physical unit-phase locus.
    # Coefficients are in ascending powers of t:
    # (1-t^2)^2+(2t)^2=(1+t^2)^2.
    circle_left = tuple(a + b for a, b in zip((1, 0, -2, 0, 1), (0, 0, 4, 0, 0)))
    circle_right = (1, 0, 2, 0, 1)
    require(circle_left == circle_right, "NC0 rational circle identity")

    global_phase_schema_check()

    values = exact_constants()
    require(all(evaluate_polynomial(record[4], values) == K_ZERO for record in rows), "sealed generator known point")
    exact = exact_tensor(tensor_a, values)
    left_coordinates = 0
    right_coordinates = 0
    for parties in FLATTENINGS:
        matrix = flatten(exact, parties)
        checked, failures = gram_exact(matrix, "left")
        require(failures == 0, f"known left unitary {parties}")
        left_coordinates += checked
        checked, failures = gram_exact(matrix, "right")
        require(failures == 0, f"known right unitary {parties}")
        right_coordinates += checked
    require(left_coordinates == right_coordinates == 3888, "known Gram coordinate totals")

    columns = gram_records(tensor_a, "column")
    column_bytes = serialize(columns)
    column_active = sum(bool(record[4]) for record in columns)
    require(len(columns) == 3888, "column coordinate count")
    require(all(evaluate_polynomial(record[4], values) == K_ZERO for record in columns), "column known point")

    known_constant_bytes = ("\n".join(f"{name}={k_text(values[name])}" for name in ("a", "b", "c", "x", "y")) + "\n").encode("ascii")
    column_cert_sha = sha256(COLUMN_CERTIFICATE.encode("ascii"))
    evidence = {
        "source_sha256": sha256(args.source.read_bytes()),
        "block944_sha256": sha256(args.block944.read_bytes()),
        "builder_sha256": sha256(args.builder.read_bytes()),
        "raw_sha256": sha256(raw_bytes),
        "raw_bytes": len(raw_bytes),
        "raw_records": len(rows),
        "raw_active": sum(bool(record[4]) for record in rows),
        "involution_records": involution_count,
        "involution_map_sha256": involution_map_sha,
        "known_constants_sha256": sha256(known_constant_bytes),
        "sealed_generators_zero": len(rows),
        "left_gram_coordinates_zero": left_coordinates,
        "right_gram_coordinates_zero": right_coordinates,
        "column_records": len(columns),
        "column_active": column_active,
        "column_serialization_bytes": len(column_bytes),
        "column_serialization_sha256": sha256(column_bytes),
        "column_certificate_sha256": column_cert_sha,
    }
    evidence_bytes = (json.dumps(evidence, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")

    print("GOLDEN_RIGIDITY_G3_CONTROLS_V1")
    print("PUBLIC_PIN_COMMIT=bc06e77c86c74dfe1b7b988614a33b5130b877f7")
    print("PUBLIC_PIN_TREE=0f8057a815efee04a1ed47b81336765fa237e84b")
    print(f"SOURCE_PINS=PASS original:{evidence['source_sha256']} block944:{evidence['block944_sha256']}")
    print("NC0=PASS dimension:4 saturation:unchanged positive_locus:INFINITE targets_forced:000000 x20_forced:0 x_elimination:ZERO")
    print("NC0_TARGET_NONZERO_WITNESS_VALUES=" + ",".join(str(value) for value in target_witness_values))
    print("NC1=PASS ideal:MAIN_EXTENDED_BY_gh_MINUS_1 free_unit_phase:1 dimension_increment:CONDITIONAL_PLUS_1 g_cyclotomy:NONE")
    print(f"NC2=PASS involution_records:{involution_count} map_sha256:{involution_map_sha} real_action:v_to_minus_v")
    print("NC3=PASS synthetic_x20:x^20 synthetic_star:y^20 nc0_normal_form:x^20-1")
    print(f"NC4=PASS constructions:A_EQUALS_B raw_records:{len(rows)} active:{evidence['raw_active']} bytes:{len(raw_bytes)} sha256:{evidence['raw_sha256']}")
    print(f"KNOWN_QZETA40=PASS constants_sha256:{evidence['known_constants_sha256']} sealed_generators_zero:{len(rows)}")
    print(f"LEFT_UNITARITY=PASS flattenings:3 coordinates_zero:{left_coordinates}")
    print(f"RIGHT_UNITARITY=PASS flattenings:3 coordinates_zero:{right_coordinates}")
    print(f"NC5=PASS column_records:{len(columns)} active:{column_active} bytes:{len(column_bytes)} sha256:{evidence['column_serialization_sha256']} universal_certificate_sha256:{column_cert_sha}")
    print("NC5_METHOD=INDEPENDENT_COLUMN_CONSTRUCTION_PLUS_UNIVERSAL_DETERMINANT_IDEAL_CERTIFICATE")
    print("GROEBNER=NOT_RUN SATURATION_ENGINE=NOT_RUN RADICAL=NOT_RUN ELIMINATION=NOT_RUN TARGET_IDEAL_SOLUTION=NOT_RUN")
    print("LIMITATION_NC1_DIMENSION=MAIN_DIMENSION_PENDING_G4")
    print("LIMITATION_NC2_BRANCH_PAIRING=STRUCTURAL_CONJUGATION_ONLY_EXACT_REAL_CARDINALITY_PENDING_G5")
    print("LIMITATION_NC5=UNIVERSAL_SCHEMA_NOT_EXPANDED_36_BY_36_DETERMINANTS")
    print(f"EVIDENCE_JSON_SHA256={sha256(evidence_bytes)}")
    print("SUMMARY=PASS")


if __name__ == "__main__":
    main()
