#!/usr/bin/env python3
"""Independent F8 audit for the public artisan-F8 preregistration.

The modular evaluator is a frontier dynamic program over compatible tensor
support tuples.  It does not use the preregistered binary join tree.  Exact
replay is a second implementation: depth-first compatible-tuple enumeration
in a different factor order, followed by reconstruction in Q(zeta_120).

Python standard library only.  No repository imports and no implicit paths.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
import sys
from typing import Iterable, Sequence


P = 241
XI_IMAGE = 3
EXPECTED_SOURCE_BYTES = 8515
EXPECTED_SOURCE_SHA256 = "55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae"
EXPECTED_SOURCE_BLOB = "e0d0e171d58b3360c39595d677ffc401a466112d"

ID4 = (0, 1, 2, 3)
DESCRIPTORS = (
    ((1, 0, 3, 2), (2, 3, 0, 1), (3, 2, 1, 0)),
    ((1, 0, 3, 2), (2, 3, 1, 0), (3, 2, 0, 1)),
    ((1, 2, 3, 0), (2, 3, 0, 1), (3, 0, 1, 2)),
    ((1, 2, 3, 0), (3, 0, 1, 2), (2, 3, 0, 1)),
)
DESCRIPTOR_NAMES = ("D0", "D1", "D2", "D3")

# Deliberately different from the preregistered binary tree.
FRONTIER_ORDER = ("A0", "B0", "A1", "B1", "A2", "B2", "A3", "B3")
# Deliberately different again: this is used only by the direct exact replay.
REPLAY_ORDER = ("A3", "B1", "A0", "B3", "A2", "B0", "A1", "B2")


def invperm(p: Sequence[int]) -> tuple[int, ...]:
    q = [0] * len(p)
    for i, x in enumerate(p):
        q[x] = i
    return tuple(q)


def factor_labels(descriptor: Sequence[Sequence[int]]) -> dict[str, tuple[int, ...]]:
    sigmas = (ID4,) + tuple(tuple(x) for x in descriptor)
    inverses = tuple(invperm(x) for x in sigmas)
    out: dict[str, tuple[int, ...]] = {}
    for r in range(4):
        out[f"A{r}"] = tuple(4 * q + r for q in range(4))
    for s in range(4):
        out[f"B{s}"] = tuple(4 * q + inverses[q][s] for q in range(4))
    counts = Counter(w for labels in out.values() for w in labels)
    if sorted(counts.values()) != [2] * 16:
        raise AssertionError("factor graph is not a pairing")
    return out


@dataclass(frozen=True, slots=True)
class Pair:
    """a+b*zeta_6 with zeta_6^2=zeta_6-1."""

    a: int
    b: int

    def __add__(self, other: "Pair") -> "Pair":
        return Pair(self.a + other.a, self.b + other.b)

    def __mul__(self, other: "Pair") -> "Pair":
        return Pair(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a + self.b * other.b,
        )

    def conjugate(self) -> "Pair":
        return Pair(self.a + self.b, -self.b)


PAIR_ZERO = Pair(0, 0)
PAIR_ONE = Pair(1, 0)
ZETA6_POWERS = (
    Pair(1, 0), Pair(0, 1), Pair(-1, 1),
    Pair(-1, 0), Pair(0, -1), Pair(1, -1),
)


@dataclass(frozen=True, slots=True)
class Entry:
    coords: tuple[int, int, int, int]
    mod: int
    # golden: (label index 0/1/2, signed exponent mod 20)
    # artisanal: Pair numerator, already conjugated for B entries
    meta: object


def file_pins(path: Path) -> tuple[bytes, dict[str, object]]:
    data = path.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    blob = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
    if len(data) != EXPECTED_SOURCE_BYTES:
        raise ValueError(f"source byte count {len(data)} != {EXPECTED_SOURCE_BYTES}")
    if sha != EXPECTED_SOURCE_SHA256:
        raise ValueError(f"source SHA256 {sha} != frozen pin")
    if blob != EXPECTED_SOURCE_BLOB:
        raise ValueError(f"source git blob {blob} != frozen pin")
    return data, {"bytes": len(data), "sha256": sha, "git_blob_sha1": blob}


def parse_literal(block: str, token_pattern: str) -> list[list[str]]:
    token_re = re.compile(token_pattern)
    rows = [x.strip() for x in block.split(";") if x.strip()]
    if len(rows) != 36:
        raise ValueError(f"matrix literal has {len(rows)} rows")
    answer: list[list[str]] = []
    for row_number, row in enumerate(rows):
        tokens = token_re.findall(row)
        residue = token_re.sub("", row).replace(",", "")
        if residue.strip() or len(tokens) != 36:
            raise ValueError(
                f"bad literal row {row_number}: tokens={len(tokens)}, residue={residue!r}"
            )
        answer.append(tokens)
    return answer


def golden_support(data: bytes) -> tuple[list[Entry], list[Entry], dict[str, int]]:
    text = data.decode("utf-8")
    match = re.search(
        r"U\s*=\s*\[(.*?)\]\s*\.\*\s*w\.\^\s*\[(.*?)\]\s*;",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise ValueError("could not locate frozen MATLAB literals")
    labels = parse_literal(match.group(1), r"(?<![A-Za-z0-9_])(0|a|b|c)(?![A-Za-z0-9_])")
    exponent_text = parse_literal(match.group(2), r"(?<![A-Za-z0-9_])(\d+)(?![A-Za-z0-9_])")
    exponents = [[int(x) for x in row] for row in exponent_text]
    if any(not 0 <= x < 20 for row in exponents for x in row):
        raise ValueError("phase outside Z/20")

    xi = XI_IMAGE
    c = (pow(xi, 15, P) + pow(xi, -15, P)) * pow(2, -1, P) % P
    den = (pow(xi, 6, P) + pow(xi, -6, P)) % P
    if den != 207:
        raise AssertionError("frozen golden denominator did not map to 207")
    a = c * pow(den, -1, P) % P
    b = (pow(xi, 12, P) + pow(xi, -12, P)) * a % P
    amplitudes = {"a": a, "b": b, "c": c}
    label_index = {"a": 0, "b": 1, "c": 2}
    direct: list[Entry] = []
    conjugate: list[Entry] = []
    for row in range(36):
        for col in range(36):
            label = labels[row][col]
            if label == "0":
                continue
            e = exponents[row][col]
            coords = (row // 6, row % 6, col // 6, col % 6)
            direct.append(Entry(coords, amplitudes[label] * pow(xi, 6 * e, P) % P,
                                (label_index[label], e % 20)))
            conjugate.append(Entry(coords, amplitudes[label] * pow(xi, -6 * e, P) % P,
                                   (label_index[label], (-e) % 20)))
    direct.sort(key=lambda x: x.coords)
    conjugate.sort(key=lambda x: x.coords)
    if len(direct) != 112:
        raise AssertionError(f"golden support {len(direct)} != 112")
    return direct, conjugate, amplitudes


def phase_exponent(kind: str, p: int, q: int) -> int:
    k, x = p % 3, p % 2
    ell, y = q % 3, q % 2
    base = k * k + ell * ell
    if (x, y) == (1, 1):
        return base % 3
    m = (x - y) % 3
    correction = -(k + ell + m) ** 2 if kind == "sym" else (ell + m) ** 2
    return (base + correction) % 3


def artisanal_numerator(kind: str, i: int, j: int, k: int, ell: int) -> Pair | None:
    q = (i - j) % 6
    if q != (k - ell) % 6:
        return None
    total = PAIR_ZERO
    for p in range(6):
        total = total + ZETA6_POWERS[(2 * phase_exponent(kind, p, q) + p * (i - k)) % 6]
    return total


def artisanal_support(kind: str) -> tuple[list[Entry], list[Entry]]:
    omega = pow(XI_IMAGE, 20, P)
    inv6 = pow(6, -1, P)
    direct: list[Entry] = []
    conjugate: list[Entry] = []
    for i in range(6):
        for j in range(6):
            for k in range(6):
                for ell in range(6):
                    pair = artisanal_numerator(kind, i, j, k, ell)
                    if pair is None or pair == PAIR_ZERO:
                        continue
                    coords = (i, j, k, ell)
                    cp = pair.conjugate()
                    direct.append(Entry(coords, (pair.a + pair.b * omega) * inv6 % P, pair))
                    conjugate.append(Entry(coords, (cp.a + cp.b * omega) * inv6 % P, cp))
    direct.sort(key=lambda x: x.coords)
    conjugate.sort(key=lambda x: x.coords)
    return direct, conjugate


def support_indices(entries: Sequence[Entry]) -> tuple[dict[tuple[int, ...], tuple[Entry, ...]], ...]:
    tables: list[dict[tuple[int, ...], list[Entry]]] = [defaultdict(list) for _ in range(16)]
    for entry in entries:
        for mask in range(16):
            key = tuple(entry.coords[q] for q in range(4) if mask >> q & 1)
            tables[mask][key].append(entry)
    return tuple({key: tuple(value) for key, value in table.items()} for table in tables)


def make_factor_sequence(
    descriptor: Sequence[Sequence[int]], order: Sequence[str]
) -> tuple[tuple[str, tuple[int, ...], bool], ...]:
    labels = factor_labels(descriptor)
    return tuple((name, labels[name], name.startswith("B")) for name in order)


def frontier_contract(
    descriptor: Sequence[Sequence[int]],
    direct_index: tuple[dict[tuple[int, ...], tuple[Entry, ...]], ...],
    conjugate_index: tuple[dict[tuple[int, ...], tuple[Entry, ...]], ...],
) -> tuple[int, dict[str, object]]:
    """Contract modulo 241 by boundary-state dynamic programming."""

    states: dict[tuple[int, ...], int] = {(): 1}
    boundary: tuple[int, ...] = ()
    stages: list[dict[str, int | str]] = []
    for name, wires, is_conjugate in make_factor_sequence(descriptor, FRONTIER_ORDER):
        before_pos = {wire: i for i, wire in enumerate(boundary)}
        mask = sum(1 << q for q, wire in enumerate(wires) if wire in before_pos)
        after = tuple(sorted(set(boundary).symmetric_difference(wires)))
        wire_to_q = {wire: q for q, wire in enumerate(wires)}
        sources = tuple(
            (0, before_pos[wire]) if wire in before_pos and wire not in wire_to_q
            else (1, wire_to_q[wire])
            for wire in after
        )
        index = conjugate_index if is_conjugate else direct_index
        new: dict[tuple[int, ...], int] = {}
        transitions = 0
        for state, coefficient in states.items():
            partial = tuple(state[before_pos[wires[q]]] for q in range(4) if mask >> q & 1)
            for entry in index[mask].get(partial, ()):
                key = tuple(state[pos] if source == 0 else entry.coords[pos]
                            for source, pos in sources)
                product = coefficient * entry.mod % P
                new[key] = (new.get(key, 0) + product) % P
                transitions += 1
        states = {key: value for key, value in new.items() if value}
        boundary = after
        stages.append({
            "factor": name,
            "matched_wires": mask.bit_count(),
            "boundary_rank": len(boundary),
            "nonzero_states": len(states),
            "transitions": transitions,
        })
    if boundary or set(states) - {()}:
        raise AssertionError("frontier contraction did not close")
    return states.get((), 0), {
        "order": list(FRONTIER_ORDER),
        "max_boundary_rank": max(stage["boundary_rank"] for stage in stages),
        "total_transitions": sum(stage["transitions"] for stage in stages),
        "stages": stages,
    }


def fingerprint_mod(values: Sequence[int]) -> tuple[int, int, int, int]:
    v0, v1, v2, v3 = values
    return (
        v0 % P,
        (v1 + v2 + v3) % P,
        (v1 * v2 + v1 * v3 + v2 * v3) % P,
        (v1 * v2 * v3) % P,
    )


def two_unitary_mod(direct: Sequence[Entry], conjugate: Sequence[Entry]) -> bool:
    cvalue = {entry.coords: entry.mod for entry in conjugate}
    for left in ((0, 1), (0, 2), (0, 3)):
        right = tuple(q for q in range(4) if q not in left)
        rows: list[dict[int, int]] = [dict() for _ in range(36)]
        for entry in direct:
            r = 6 * entry.coords[left[0]] + entry.coords[left[1]]
            c = 6 * entry.coords[right[0]] + entry.coords[right[1]]
            rows[r][c] = entry.mod
        for r in range(36):
            for s in range(36):
                total = 0
                for col, value in rows[r].items():
                    if col not in rows[s]:
                        continue
                    coords = [0] * 4
                    coords[left[0]], coords[left[1]] = divmod(s, 6)
                    coords[right[0]], coords[right[1]] = divmod(col, 6)
                    total = (total + value * cvalue.get(tuple(coords), 0)) % P
                if total != (1 if r == s else 0):
                    return False
    return True


def gl_orbit_count(kind: str) -> int:
    tables = set()
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    if (a * d - b * c) % 3 == 0:
                        continue
                    # hat(G)^T action; calculate it directly modulo six.
                    h00, h01 = (4 * a + 3) % 6, (4 * b) % 6
                    h10, h11 = (4 * c) % 6, (4 * d + 3) % 6
                    table = []
                    for p in range(6):
                        for q in range(6):
                            pp = (h00 * p + h10 * q) % 6
                            qq = (h01 * p + h11 * q) % 6
                            table.append(phase_exponent(kind, pp, qq))
                    tables.add(tuple(table))
    return len(tables)


# ---- Exact Q(zeta_120) arithmetic -----------------------------------------


DEGREE = 32


def reduce_poly(values: Iterable[int | Fraction]) -> tuple[Fraction, ...]:
    out = [Fraction(x) for x in values]
    if len(out) < DEGREE:
        out += [Fraction(0)] * (DEGREE - len(out))
    for d in range(len(out) - 1, DEGREE - 1, -1):
        lead = out[d]
        if not lead:
            continue
        out[d] = 0
        out[d - 4] -= lead
        out[d - 12] += lead
        out[d - 16] += lead
        out[d - 20] += lead
        out[d - 28] -= lead
        out[d - 32] -= lead
    return tuple(out[:DEGREE])


def trim(p: list[Fraction]) -> list[Fraction]:
    while p and p[-1] == 0:
        p.pop()
    return p


def poly_sub(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
                 for i in range(n)])


def poly_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    if not a or not b:
        return []
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] += x * y
    return trim(out)


def poly_divmod(a: list[Fraction], b: list[Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    a, b = trim(a[:]), trim(b[:])
    if not b:
        raise ZeroDivisionError
    quotient = [Fraction(0)] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b):
        shift = len(a) - len(b)
        lead = a[-1] / b[-1]
        quotient[shift] += lead
        for j, value in enumerate(b):
            a[shift + j] -= lead * value
        trim(a)
    return trim(quotient), a


@dataclass(frozen=True, slots=True)
class K120:
    c: tuple[Fraction, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "c", reduce_poly(self.c))

    @staticmethod
    def scalar(value: int | Fraction) -> "K120":
        return K120((Fraction(value),))

    def __bool__(self) -> bool:
        return any(self.c)

    def __add__(self, other: "K120 | int | Fraction") -> "K120":
        other = kcoerce(other)
        return K120(tuple(a + b for a, b in zip(self.c, other.c)))

    __radd__ = __add__

    def __neg__(self) -> "K120":
        return K120(tuple(-x for x in self.c))

    def __sub__(self, other: "K120 | int | Fraction") -> "K120":
        return self + (-kcoerce(other))

    def __rsub__(self, other: "K120 | int | Fraction") -> "K120":
        return kcoerce(other) - self

    def __mul__(self, other: "K120 | int | Fraction") -> "K120":
        other = kcoerce(other)
        raw = [Fraction(0)] * (2 * DEGREE - 1)
        for i, a in enumerate(self.c):
            if a:
                for j, b in enumerate(other.c):
                    if b:
                        raw[i + j] += a * b
        return K120(tuple(raw))

    __rmul__ = __mul__

    def inverse(self) -> "K120":
        if not self:
            raise ZeroDivisionError
        # Phi_120 low-to-high.
        modulus = [Fraction(0)] * 33
        for degree, value in ((0, 1), (4, 1), (12, -1), (16, -1),
                              (20, -1), (28, 1), (32, 1)):
            modulus[degree] = Fraction(value)
        r0, r1 = modulus, trim(list(self.c))
        t0, t1 = [], [Fraction(1)]
        while r1:
            quotient, remainder = poly_divmod(r0, r1)
            r0, r1 = r1, remainder
            t0, t1 = t1, poly_sub(t0, poly_mul(quotient, t1))
        if len(r0) != 1:
            raise ZeroDivisionError("non-unit")
        return K120(tuple(x / r0[0] for x in t0))

    def __truediv__(self, other: "K120 | int | Fraction") -> "K120":
        return self * kcoerce(other).inverse()

    def __pow__(self, power: int) -> "K120":
        if power < 0:
            return self.inverse() ** (-power)
        result = K_ONE
        base = self
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power //= 2
        return result


def kcoerce(value: K120 | int | Fraction) -> K120:
    return value if isinstance(value, K120) else K120.scalar(value)


K_ZERO = K120.scalar(0)
K_ONE = K120.scalar(1)
XI = K120((Fraction(0), Fraction(1)))
XI_POWERS = tuple(XI ** e for e in range(120))


def exact_constants() -> tuple[K120, K120, K120]:
    c = (XI_POWERS[15] + XI_POWERS[-15]) / 2
    a = c / (XI_POWERS[6] + XI_POWERS[-6])
    b = (XI_POWERS[12] + XI_POWERS[-12]) * a
    return a, b, c


def direct_replay(
    descriptor: Sequence[Sequence[int]],
    direct: Sequence[Entry],
    conjugate: Sequence[Entry],
    target_kind: str,
) -> dict[str, object]:
    """Enumerate full compatible tuples in REPLAY_ORDER.

    This is intentionally not dynamic programming: it retains an auditable
    leaf count and accumulates the exact signature prescribed in G4.
    """

    dindex, cindex = support_indices(direct), support_indices(conjugate)
    factors = make_factor_sequence(descriptor, REPLAY_ORDER)
    assignment = [-1] * 16
    leaves = 0
    modular = 0

    if target_kind == "golden":
        signatures: Counter[tuple[int, int, int, int]] = Counter()

        def visit(depth: int, product: int, na: int, nb: int, nc: int, exponent: int) -> None:
            nonlocal leaves, modular
            if depth == 8:
                leaves += 1
                modular = (modular + product) % P
                signatures[(na, nb, nc, exponent % 20)] += 1
                return
            _name, wires, is_conjugate = factors[depth]
            mask = sum(1 << q for q, wire in enumerate(wires) if assignment[wire] >= 0)
            key = tuple(assignment[wires[q]] for q in range(4) if mask >> q & 1)
            index = cindex if is_conjugate else dindex
            for entry in index[mask].get(key, ()):
                changed = []
                for q, wire in enumerate(wires):
                    if assignment[wire] < 0:
                        assignment[wire] = entry.coords[q]
                        changed.append(wire)
                label, phase = entry.meta
                visit(depth + 1, product * entry.mod % P,
                      na + (label == 0), nb + (label == 1), nc + (label == 2),
                      exponent + phase)
                for wire in changed:
                    assignment[wire] = -1

        visit(0, 1, 0, 0, 0, 0)
        return {
            "mod241": modular,
            "compatible_tuples": leaves,
            "order": list(REPLAY_ORDER),
            "signature_counts": signatures,
        }

    pair_total = PAIR_ZERO

    def visit_pair(depth: int, product_mod: int, product_pair: Pair) -> None:
        nonlocal leaves, modular, pair_total
        if depth == 8:
            leaves += 1
            modular = (modular + product_mod) % P
            pair_total = pair_total + product_pair
            return
        _name, wires, is_conjugate = factors[depth]
        mask = sum(1 << q for q, wire in enumerate(wires) if assignment[wire] >= 0)
        key = tuple(assignment[wires[q]] for q in range(4) if mask >> q & 1)
        index = cindex if is_conjugate else dindex
        for entry in index[mask].get(key, ()):
            changed = []
            for q, wire in enumerate(wires):
                if assignment[wire] < 0:
                    assignment[wire] = entry.coords[q]
                    changed.append(wire)
            visit_pair(depth + 1, product_mod * entry.mod % P, product_pair * entry.meta)
            for wire in changed:
                assignment[wire] = -1

    visit_pair(0, 1, PAIR_ONE)
    return {
        "mod241": modular,
        "compatible_tuples": leaves,
        "order": list(REPLAY_ORDER),
        "pair_numerator": pair_total,
    }


def exact_value(replay: dict[str, object], target_kind: str) -> K120:
    if target_kind == "golden":
        a, b, c = exact_constants()
        powers = tuple(tuple(x ** e for e in range(9)) for x in (a, b, c))
        phases = tuple(XI_POWERS[(6 * e) % 120] for e in range(20))
        total = K_ZERO
        signatures: Counter = replay["signature_counts"]  # type: ignore[assignment]
        for (na, nb, nc, exponent), count in signatures.items():
            total += count * powers[0][na] * powers[1][nb] * powers[2][nc] * phases[exponent]
        return total
    pair: Pair = replay["pair_numerator"]  # type: ignore[assignment]
    return (K120.scalar(pair.a) + pair.b * XI_POWERS[20]) / (6 ** 8)


def k_residue(value: K120) -> int:
    total = 0
    power = 1
    for coefficient in value.c:
        denominator = coefficient.denominator % P
        if denominator == 0:
            raise ValueError("non-241-integral coefficient")
        total = (total + coefficient.numerator * pow(denominator, -1, P) * power) % P
        power = power * XI_IMAGE % P
    return total


def exact_fp(values: Sequence[K120]) -> tuple[K120, K120, K120, K120]:
    v0, v1, v2, v3 = values
    return (v0, v1 + v2 + v3, v1 * v2 + v1 * v3 + v2 * v3, v1 * v2 * v3)


def serialize_coefficients(value: K120) -> list[str]:
    return [str(x) for x in value.c]


def first_difference(left: Sequence[int], right: Sequence[int]) -> int | None:
    return next((i for i, (a, b) in enumerate(zip(left, right)) if a != b), None)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True,
                        help="path to the pinned AME46_ORIGINAL.m")
    parser.add_argument("--output", type=Path, required=True,
                        help="canonical JSON certificate path")
    parser.add_argument("--skip-exact", action="store_true")
    parser.add_argument("--progress", action="store_true")
    args = parser.parse_args()

    data, source_pin = file_pins(args.source)
    supports: dict[str, tuple[list[Entry], list[Entry]]] = {}
    golden_direct, golden_conjugate, amplitudes = golden_support(data)
    supports["golden"] = (golden_direct, golden_conjugate)
    supports["sym"] = artisanal_support("sym")
    supports["sparse"] = artisanal_support("sparse")

    integrity = {
        "source": source_pin,
        "support_sizes": {name: len(value[0]) for name, value in supports.items()},
        "golden_amplitudes_mod241": amplitudes,
        "two_unitary_mod241": {
            name: two_unitary_mod(*value) for name, value in supports.items()
        },
        "gl2_f3_distinct_tables": {kind: gl_orbit_count(kind) for kind in ("sym", "sparse")},
    }
    if not all(integrity["two_unitary_mod241"].values()):
        raise AssertionError("modular two-unitarity gate failed")
    if integrity["gl2_f3_distinct_tables"] != {"sym": 24, "sparse": 24}:
        raise AssertionError("GL(2,F3) deduplication gate failed")

    modular: dict[str, object] = {}
    for target_name in ("golden", "sym", "sparse"):
        direct, conjugate = supports[target_name]
        dindex, cindex = support_indices(direct), support_indices(conjugate)
        values: list[int] = []
        stats: dict[str, object] = {}
        for descriptor_name, descriptor in zip(DESCRIPTOR_NAMES, DESCRIPTORS):
            if args.progress:
                print(f"frontier {target_name}/{descriptor_name}", file=sys.stderr, flush=True)
            value, stat = frontier_contract(descriptor, dindex, cindex)
            values.append(value)
            stats[descriptor_name] = stat
        modular[target_name] = {
            "v_mod241": values,
            "F8_mod241": list(fingerprint_mod(values)),
            "frontier_stats": stats,
        }

    exact_certificates: dict[str, object] = {}
    coordinate_names = ("v0", "e1", "e2", "e3")
    verdicts: dict[str, str] = {}
    replay_cache: dict[tuple[str, int], tuple[dict[str, object], K120]] = {}

    def get_exact(target: str, descriptor_index: int) -> tuple[dict[str, object], K120]:
        key = (target, descriptor_index)
        if key not in replay_cache:
            if args.progress:
                print(f"exact replay {target}/D{descriptor_index}", file=sys.stderr, flush=True)
            direct, conjugate = supports[target]
            replay = direct_replay(DESCRIPTORS[descriptor_index], direct, conjugate, target)
            expected = modular[target]["v_mod241"][descriptor_index]  # type: ignore[index]
            if replay["mod241"] != expected:
                raise AssertionError(
                    f"direct replay {target}/D{descriptor_index}={replay['mod241']} != frontier {expected}"
                )
            value = exact_value(replay, target)
            if k_residue(value) != expected:
                raise AssertionError("exact reconstruction does not reduce to locator value")
            replay_cache[key] = replay, value
        return replay_cache[key]

    for target in ("sym", "sparse"):
        golden_fp_mod = modular["golden"]["F8_mod241"]  # type: ignore[index]
        target_fp_mod = modular[target]["F8_mod241"]  # type: ignore[index]
        coordinate = first_difference(golden_fp_mod, target_fp_mod)
        if args.skip_exact:
            verdicts[target] = "LOCATOR_MISMATCH" if coordinate is not None else "LOCATOR_MATCH_INCONCLUSIVE"
            continue
        needed = [0] if coordinate == 0 else ([1, 2, 3] if coordinate in (1, 2, 3) else [0, 1, 2, 3])
        golden_values = [K_ZERO] * 4
        target_values = [K_ZERO] * 4
        replays: dict[str, object] = {"golden": {}, target: {}}
        for descriptor_index in needed:
            golden_replay, golden_value = get_exact("golden", descriptor_index)
            target_replay, target_value = get_exact(target, descriptor_index)
            golden_values[descriptor_index] = golden_value
            target_values[descriptor_index] = target_value
            for name, replay in (("golden", golden_replay), (target, target_replay)):
                audit = {
                    "mod241": replay["mod241"],
                    "compatible_tuples": replay["compatible_tuples"],
                    "order": replay["order"],
                }
                if name == "golden":
                    audit["nonzero_signature_bins"] = len(replay["signature_counts"])
                    audit["signature_total"] = sum(replay["signature_counts"].values())
                else:
                    pair = replay["pair_numerator"]
                    audit["pair_numerator_over_6^8"] = [pair.a, pair.b]
                replays[name][f"D{descriptor_index}"] = audit

        if coordinate is None:
            golden_coordinate = exact_fp(golden_values)
            target_coordinate = exact_fp(target_values)
            exact_index = first_difference([k_residue(x) for x in golden_coordinate],
                                           [k_residue(x) for x in target_coordinate])
            # All residues matched by construction.  Test exact coefficients directly.
            exact_index = next((i for i, (x, y) in enumerate(zip(golden_coordinate, target_coordinate))
                                if x != y), None)
            if exact_index is None:
                verdicts[target] = f"F8_MATCH_INCONCLUSIVE_{target.upper()}"
                exact_certificates[target] = {
                    "locator_first_difference": None,
                    "exact_first_difference": None,
                    "replay": replays,
                }
                continue
            coordinate = exact_index
        golden_coordinate = exact_fp(golden_values)[coordinate]
        target_coordinate = exact_fp(target_values)[coordinate]
        difference = golden_coordinate - target_coordinate
        residue = k_residue(difference)
        locator_difference = (golden_fp_mod[coordinate] - target_fp_mod[coordinate]) % P
        if residue != locator_difference or not difference:
            raise AssertionError("exact mismatch certificate failed")
        verdicts[target] = f"EXACT_NO_{target.upper()}"
        exact_certificates[target] = {
            "coordinate_index": coordinate,
            "coordinate_name": coordinate_names[coordinate],
            "difference_convention": "golden_minus_target",
            "difference_coefficients_Q_zeta120_power_basis": serialize_coefficients(difference),
            "difference_mod241_xi_to_3": residue,
            "locator_difference_mod241": locator_difference,
            "replay": replays,
        }

    union = (
        "EXACT_NO_GG_ARTISANAL_9PLUS27"
        if verdicts.get("sym") == "EXACT_NO_SYM" and verdicts.get("sparse") == "EXACT_NO_SPARSE"
        else "F8_MATCH_INCONCLUSIVE_GG_ARTISANAL_9PLUS27"
    )

    result = {
        "schema": "artisan-f8-independent-compatible-tuples-v1",
        "public_pin": {
            "commit": "62c1e877c3817923dca6b922ebd4562f83d2bbea",
            "prereg_sha256": "0ffaca441435003aeb0779160e9fcdbca6c40a25c4ea2acce836ff3eca6e0137",
        },
        "field": {"prime": P, "xi_image": XI_IMAGE, "xi_order": 120},
        "integrity": integrity,
        "descriptors": {name: [list(x) for x in value]
                        for name, value in zip(DESCRIPTOR_NAMES, DESCRIPTORS)},
        "modular": modular,
        "exact_certificates": exact_certificates,
        "orbit_verdicts": verdicts,
        "union_verdict": union,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    encoded = (json.dumps(result, sort_keys=True, indent=2) + "\n").encode()
    args.output.write_bytes(encoded)

    print("ARTISAN_F8_INDEPENDENT_COMPATIBLE_TUPLES_V1")
    for target in ("golden", "sym", "sparse"):
        print(f"{target.upper()}_V=" + ",".join(map(str, modular[target]["v_mod241"])))  # type: ignore[index]
        print(f"{target.upper()}_F8=" + ",".join(map(str, modular[target]["F8_mod241"])))  # type: ignore[index]
    for target in ("sym", "sparse"):
        cert = exact_certificates.get(target)
        if cert and "coordinate_name" in cert:
            print(f"{target.upper()}_FIRST={cert['coordinate_name']};DIFF_MOD241={cert['difference_mod241_xi_to_3']}")
        print(f"{target.upper()}_VERDICT={verdicts[target]}")
    print(f"UNION_VERDICT={union}")
    print(f"CERTIFICATE_SHA256={hashlib.sha256(encoded).hexdigest()}")


if __name__ == "__main__":
    main()
