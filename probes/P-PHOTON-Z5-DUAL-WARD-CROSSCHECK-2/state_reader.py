#!/usr/bin/env python3
"""Independent fail-closed reader for CROSSCHECK-2 target states.

The engine is not imported.  A checkpoint carries the complete target state
in a canonical two-bit encoding; this module reconstructs every exact state,
boundary, current and homology quantity used by the Ward analysis directly
from those bytes.

Lowest-momentum powers are also engine-independent.  For L=2,3,6 they are
exact :class:`fractions.Fraction` values.  For L=8 they are represented as
``rational + sqrt2 * coefficient`` without evaluating the square root.
"""

from __future__ import annotations

import base64
import binascii
import argparse
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
import re
import sys
from typing import Mapping, Sequence, TypeAlias


DIM = 4
PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
PAIR_LABELS = ("01", "02", "03", "12", "13", "23")
FAMILY_NAMES = ("inline1", "transverse1", "inline2", "transverse2")
STATE_ENCODING = "2bit-site-major-pairs-v1"
READER_SCHEMA = "crosscheck2-sufficient-statistics-v1"
SUPPORTED_EXTENTS = (2, 3, 6, 8)
LOWER_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
FORMAL_CHECKPOINTS = 2048
STATE_AUDIT_STRIDE = 16
MAX_ENGINE_STREAM_BYTES = 100_000_000
MAX_ENGINE_LINE_BYTES = 262_144
MAX_COMMITTED_STREAM_BYTES = 5_000_000
MAX_COMMITTED_RUN_BYTES = 4_096
MAX_COMMITTED_SUMMARY_BYTES = 263_000
PACKED_STREAM_DOMAIN = b"P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2\0packed-state-stream-v1\0"

RUN_FIELDS = frozenset(
    {
        "L",
        "S",
        "bitstream_domain",
        "checkpoints",
        "development_only",
        "legacy_selector_probability",
        "seed",
        "start",
        "state_encoding",
        "state_packed_bytes",
        "state_unpacked_bytes",
        "thin",
        "transition_cap",
        "type",
        "validation_stride",
        "warm_bottom",
    }
)

CHECKPOINT_FIELDS = frozenset(
    {
        "L",
        "checkpoint",
        "current_hash",
        "current_nonzero",
        "homology",
        "j_nnz",
        "j2_sum",
        "n_sum",
        "packed_state_sha256",
        "post_warm_bottom_attempt",
        "state_2bit_base64",
        "state_sha256",
        "support",
        "swap_accepted",
        "transition",
        "type",
        "walker_id",
    }
)


class StateIntegrityError(ValueError):
    """The packed state or an engine claim is not exactly self-consistent."""


@dataclass(frozen=True)
class Qsqrt2:
    """An exact element ``rational + coefficient*sqrt(2)``."""

    rational: Fraction = Fraction(0)
    coefficient: Fraction = Fraction(0)

    def __add__(self, other: object) -> "Qsqrt2":
        if isinstance(other, Qsqrt2):
            return Qsqrt2(
                self.rational + other.rational,
                self.coefficient + other.coefficient,
            )
        if isinstance(other, (int, Fraction)):
            return Qsqrt2(self.rational + other, self.coefficient)
        return NotImplemented

    def __radd__(self, other: object) -> "Qsqrt2":
        return self.__add__(other)

    def __neg__(self) -> "Qsqrt2":
        return Qsqrt2(-self.rational, -self.coefficient)

    def __sub__(self, other: object) -> "Qsqrt2":
        if isinstance(other, (Qsqrt2, int, Fraction)):
            return self + (-other if isinstance(other, Qsqrt2) else -Fraction(other))
        return NotImplemented

    def scale(self, value: int | Fraction) -> "Qsqrt2":
        factor = Fraction(value)
        return Qsqrt2(self.rational * factor, self.coefficient * factor)

    def divide(self, value: int) -> "Qsqrt2":
        if value == 0:
            raise ZeroDivisionError
        return self.scale(Fraction(1, value))


ExactPower: TypeAlias = Fraction | Qsqrt2


@dataclass(frozen=True)
class PairSums:
    family: str
    total: int
    by_orientation: tuple[int, ...]


@dataclass(frozen=True)
class MomentumPower:
    momentum_axis: int
    component_twice_unnormalized: tuple[tuple[int, int], ...]
    longitudinal_twice_unnormalized: tuple[int, int]
    trace_twice_unnormalized: tuple[int, int]
    component_power: tuple[ExactPower, ...]
    longitudinal_power: ExactPower
    trace: ExactPower


@dataclass(frozen=True)
class DerivedState:
    L: int
    state_sha256: str
    packed_state_sha256: str
    packed: bytes
    residues: bytes
    current: tuple[int, ...]
    current_hash: str
    support: int
    n_sum: int
    n_sum_by_orientation: tuple[int, ...]
    n2_sum: int
    n2_sum_by_orientation: tuple[int, ...]
    pair_sums: tuple[PairSums, ...]
    j_sum: int
    j_sum_by_direction: tuple[int, ...]
    j2_sum: int
    j2_sum_by_direction: tuple[int, ...]
    j_nonzero: int
    j_nonzero_by_direction: tuple[int, ...]
    homology: tuple[int, ...]
    lowest_momenta: tuple[MomentumPower, ...]
    axis_average_current_power: ExactPower


def _fail(reason: str) -> None:
    raise StateIntegrityError(reason)


def _require(condition: bool, reason: str) -> None:
    if not condition:
        _fail(reason)


def _exact_int(value: object, where: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        _fail(f"{where}:not_integer")
    return value


def _uint64(value: object, where: str) -> int:
    result = _exact_int(value, where)
    _require(0 <= result <= (1 << 64) - 1, f"{where}:not_uint64")
    return result


def _int64(value: object, where: str) -> int:
    result = _exact_int(value, where)
    _require(-(1 << 63) <= result < (1 << 63), f"{where}:not_int64")
    return result


def _exact_string(value: object, where: str) -> str:
    if not isinstance(value, str):
        _fail(f"{where}:not_string")
    return value


def state_size(L: int) -> int:
    if isinstance(L, bool) or not isinstance(L, int) or L not in SUPPORTED_EXTENTS:
        _fail(f"unsupported_extent_{L!r}")
    return len(PAIRS) * L**DIM


def packed_state_size(L: int) -> int:
    return (state_size(L) + 3) // 4


def verify_encoding_header(L: int, run: Mapping[str, object]) -> None:
    """Verify the three run-level canonical state-encoding declarations."""

    expected_unpacked = state_size(L)
    expected_packed = packed_state_size(L)
    _require(run.get("state_encoding") == STATE_ENCODING, "run:state_encoding")
    _require(
        _exact_int(run.get("state_unpacked_bytes"), "run:state_unpacked_bytes")
        == expected_unpacked,
        "run:state_unpacked_length",
    )
    _require(
        _exact_int(run.get("state_packed_bytes"), "run:state_packed_bytes")
        == expected_packed,
        "run:state_packed_length",
    )


def pack_residues(residues: Sequence[int]) -> str:
    """Fixture helper implementing the canonical MSB-first two-bit packing."""

    packed = bytearray((len(residues) + 3) // 4)
    codes = {0: 0, 1: 1, 4: 2}
    for index, residue in enumerate(residues):
        if residue not in codes:
            _fail(f"pack:forbidden_residue[{index}]")
        packed[index // 4] |= codes[residue] << (6 - 2 * (index % 4))
    return base64.b64encode(bytes(packed)).decode("ascii")


def unpack_residues(L: int, encoded: object) -> bytes:
    """Decode canonical standard base64 and reject all unused/invalid codes."""

    text = _exact_string(encoded, "state_2bit_base64")
    try:
        ascii_bytes = text.encode("ascii")
    except UnicodeEncodeError as error:
        raise StateIntegrityError("state_2bit_base64:non_ASCII") from error
    try:
        packed = base64.b64decode(ascii_bytes, validate=True)
    except (binascii.Error, ValueError) as error:
        raise StateIntegrityError("state_2bit_base64:invalid_standard_base64") from error
    _require(
        base64.b64encode(packed) == ascii_bytes,
        "state_2bit_base64:noncanonical_padding_or_alphabet",
    )
    expected_count = state_size(L)
    _require(len(packed) == packed_state_size(L), "state_2bit_base64:packed_length")
    decoded = bytearray(expected_count)
    code_to_residue = (0, 1, 4)
    for index in range(len(packed) * 4):
        code = (packed[index // 4] >> (6 - 2 * (index % 4))) & 3
        if index >= expected_count:
            _require(code == 0, "state_2bit_base64:nonzero_tail_bits")
            continue
        _require(code != 3, f"state_2bit_base64:invalid_code[{index}]")
        decoded[index] = code_to_residue[code]
    return bytes(decoded)


def packed_bytes(L: int, encoded: object) -> bytes:
    """Return canonical packed bytes after exercising the complete decoder."""

    text = _exact_string(encoded, "state_2bit_base64")
    unpack_residues(L, text)
    return base64.b64decode(text.encode("ascii"), validate=True)


@lru_cache(maxsize=None)
def _forward_table(L: int) -> tuple[tuple[int, ...], ...]:
    volume = L**DIM
    axes: list[tuple[int, ...]] = []
    for axis in range(DIM):
        stride = L ** (DIM - axis - 1)
        row: list[int] = []
        for site in range(volume):
            coordinate = (site // stride) % L
            row.append(site + stride if coordinate + 1 < L else site - (L - 1) * stride)
        axes.append(tuple(row))
    return tuple(axes)


def _shift_site(L: int, site: int, axis: int, distance: int) -> int:
    stride = L ** (DIM - axis - 1)
    coordinate = (site // stride) % L
    return site + (((coordinate + distance) % L) - coordinate) * stride


@lru_cache(maxsize=None)
def _shift_table(L: int, axis: int, distance: int) -> tuple[int, ...]:
    return tuple(_shift_site(L, site, axis, distance) for site in range(L**DIM))


@lru_cache(maxsize=None)
def _coordinate_table(L: int, axis: int) -> tuple[int, ...]:
    stride = L ** (DIM - axis - 1)
    return tuple((site // stride) % L for site in range(L**DIM))


def _principal(residue: int) -> int:
    if residue == 4:
        return -1
    if residue in (0, 1):
        return residue
    _fail(f"hard_state:forbidden_residue_{residue}")
    raise AssertionError("unreachable")


def _boundaries(
    L: int,
    residues: bytes,
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[tuple[int, ...], ...]]:
    volume = L**DIM
    forward = _forward_table(L)
    modular = [0] * (volume * DIM)
    integer = [0] * (volume * DIM)
    for site in range(volume):
        base = site * len(PAIRS)
        for pair_index, (a, b) in enumerate(PAIRS):
            residue = residues[base + pair_index]
            lifted = _principal(residue)
            if residue == 0:
                continue
            terms = (
                (site * DIM + a, 1),
                (forward[a][site] * DIM + b, 1),
                (forward[b][site] * DIM + a, -1),
                (site * DIM + b, -1),
            )
            for link, sign in terms:
                modular[link] += sign * residue
                integer[link] += sign * lifted
    return tuple(modular), tuple(integer), forward


def _exact_add(left: ExactPower, right: ExactPower) -> ExactPower:
    if isinstance(left, Qsqrt2) or isinstance(right, Qsqrt2):
        lhs = left if isinstance(left, Qsqrt2) else Qsqrt2(left)
        rhs = right if isinstance(right, Qsqrt2) else Qsqrt2(right)
        return lhs + rhs
    return left + right


def _exact_scale(value: ExactPower, factor: int | Fraction) -> ExactPower:
    if isinstance(value, Qsqrt2):
        return value.scale(factor)
    return value * Fraction(factor)


def _exact_sum(values: Sequence[ExactPower]) -> ExactPower:
    if any(isinstance(value, Qsqrt2) for value in values):
        result: ExactPower = Qsqrt2()
    else:
        result = Fraction(0)
    for value in values:
        result = _exact_add(result, value)
    return result


def _cosine_coefficient(L: int, difference: int) -> ExactPower:
    index = difference % L
    if L == 2:
        return (Fraction(1), Fraction(-1))[index]
    if L == 3:
        return (Fraction(1), Fraction(-1, 2), Fraction(-1, 2))[index]
    if L == 6:
        return (
            Fraction(1),
            Fraction(1, 2),
            Fraction(-1, 2),
            Fraction(-1),
            Fraction(-1, 2),
            Fraction(1, 2),
        )[index]
    if L == 8:
        return (
            Qsqrt2(Fraction(1), Fraction(0)),
            Qsqrt2(Fraction(0), Fraction(1, 2)),
            Qsqrt2(),
            Qsqrt2(Fraction(0), Fraction(-1, 2)),
            Qsqrt2(Fraction(-1), Fraction(0)),
            Qsqrt2(Fraction(0), Fraction(-1, 2)),
            Qsqrt2(),
            Qsqrt2(Fraction(0), Fraction(1, 2)),
        )[index]
    _fail(f"lowest_mode:unsupported_extent_{L}")
    raise AssertionError("unreachable")


def _pair_from_exact(value: ExactPower, where: str) -> tuple[int, int]:
    if isinstance(value, Qsqrt2):
        _require(value.rational.denominator == 1, f"{where}:noninteger_rational")
        _require(value.coefficient.denominator == 1, f"{where}:noninteger_sqrt2")
        return value.rational.numerator, value.coefficient.numerator
    _require(value.denominator == 1, f"{where}:noninteger_fraction")
    return value.numerator, 0


def _power_from_twice_pair(L: int, value: tuple[int, int]) -> ExactPower:
    denominator = 2 * L**DIM
    if L == 8:
        return Qsqrt2(Fraction(value[0], denominator), Fraction(value[1], denominator))
    _require(value[1] == 0, "lowest_mode:unexpected_sqrt2_component")
    return Fraction(value[0], denominator)


def _mode_power_twice(L: int, coordinate_sums: Sequence[int]) -> tuple[int, int]:
    _require(len(coordinate_sums) == L, "lowest_mode:coordinate_shape")
    terms: list[ExactPower] = []
    for left in range(L):
        for right in range(L):
            coefficient = _cosine_coefficient(L, left - right)
            terms.append(_exact_scale(coefficient, coordinate_sums[left] * coordinate_sums[right]))
    return _pair_from_exact(_exact_scale(_exact_sum(terms), 2), "lowest_mode:twice_power")


def _lowest_momenta(L: int, current: Sequence[int]) -> tuple[MomentumPower, ...]:
    volume = L**DIM
    result: list[MomentumPower] = []
    for momentum_axis in range(DIM):
        coordinates = _coordinate_table(L, momentum_axis)
        coordinate_sums_by_component = [[0] * L for _ in range(DIM)]
        for site, coordinate in enumerate(coordinates):
            base = site * DIM
            for component in range(DIM):
                coordinate_sums_by_component[component][coordinate] += current[base + component]
        components: list[ExactPower] = []
        component_pairs: list[tuple[int, int]] = []
        for component in range(DIM):
            pair = _mode_power_twice(L, coordinate_sums_by_component[component])
            component_pairs.append(pair)
            components.append(_power_from_twice_pair(L, pair))
        trace = _exact_sum(components)
        trace_pair = (
            sum(value[0] for value in component_pairs),
            sum(value[1] for value in component_pairs),
        )
        result.append(
            MomentumPower(
                momentum_axis,
                tuple(component_pairs),
                component_pairs[momentum_axis],
                trace_pair,
                tuple(components),
                components[momentum_axis],
                trace,
            )
        )
    return tuple(result)


def derive_state(L: int, encoded: object, expected_sha256: object) -> DerivedState:
    """Decode one state and independently derive all Ward sufficient statistics."""

    residues = unpack_residues(L, encoded)
    packed = packed_bytes(L, encoded)
    claimed_hash = _exact_string(expected_sha256, "state_sha256")
    _require(LOWER_SHA256.fullmatch(claimed_hash) is not None, "state_sha256:shape")
    actual_hash = hashlib.sha256(residues).hexdigest()
    _require(actual_hash == claimed_hash, "state_sha256:mismatch")

    modular_boundary, integer_boundary, forward = _boundaries(L, residues)
    _require(not any(value % 5 for value in modular_boundary), "state:not_closed_mod5")
    _require(not any(value % 5 for value in integer_boundary), "state:integer_boundary_not_divisible_by_5")
    current = tuple(value // 5 for value in integer_boundary)

    divergence = [0] * (L**DIM)
    for site in range(L**DIM):
        for axis in range(DIM):
            value = current[site * DIM + axis]
            divergence[site] -= value
            divergence[forward[axis][site]] += value
    _require(not any(divergence), "state:current_divergence")

    n_by_orientation = [0] * len(PAIRS)
    n2_by_orientation = [0] * len(PAIRS)
    support = 0
    for index, residue in enumerate(residues):
        lifted = _principal(residue)
        orientation = index % len(PAIRS)
        n_by_orientation[orientation] += lifted
        n2_by_orientation[orientation] += lifted * lifted
        support += int(lifted != 0)

    pair_families: list[PairSums] = []
    for family in FAMILY_NAMES:
        orientation_sums: list[int] = []
        for pair_index, (a, b) in enumerate(PAIRS):
            shift_axis = a if family.startswith("inline") else min(
                axis for axis in range(DIM) if axis not in (a, b)
            )
            distance = 1 if family.endswith("1") else 2
            shifted_sites = _shift_table(L, shift_axis, distance)
            product = 0
            for site, shifted in enumerate(shifted_sites):
                left = _principal(residues[site * len(PAIRS) + pair_index])
                right = _principal(residues[shifted * len(PAIRS) + pair_index])
                product += left * right
            orientation_sums.append(product)
        pair_families.append(PairSums(family, sum(orientation_sums), tuple(orientation_sums)))

    j_by_direction = [0] * DIM
    j2_by_direction = [0] * DIM
    j_nonzero_by_direction = [0] * DIM
    for site in range(L**DIM):
        for direction in range(DIM):
            value = current[site * DIM + direction]
            j_by_direction[direction] += value
            j2_by_direction[direction] += value * value
            j_nonzero_by_direction[direction] += int(value != 0)

    residue_orientation_totals = [0] * len(PAIRS)
    for index, residue in enumerate(residues):
        residue_orientation_totals[index % len(PAIRS)] += residue
    scale = (L * L) % 5
    _require(scale != 0, "state:H2_noninvertible_extent")
    inverse = pow(scale, -1, 5)
    homology = tuple((inverse * total) % 5 for total in residue_orientation_totals)

    momenta = _lowest_momenta(L, current)
    axis_average = _exact_scale(
        _exact_sum([entry.trace for entry in momenta]), Fraction(1, DIM)
    )
    current_hash = (
        hashlib.sha256(",".join(str(value) for value in current).encode("ascii")).hexdigest()
        if any(current)
        else ""
    )
    return DerivedState(
        L=L,
        state_sha256=actual_hash,
        packed_state_sha256=hashlib.sha256(packed).hexdigest(),
        packed=packed,
        residues=residues,
        current=current,
        current_hash=current_hash,
        support=support,
        n_sum=sum(n_by_orientation),
        n_sum_by_orientation=tuple(n_by_orientation),
        n2_sum=sum(n2_by_orientation),
        n2_sum_by_orientation=tuple(n2_by_orientation),
        pair_sums=tuple(pair_families),
        j_sum=sum(j_by_direction),
        j_sum_by_direction=tuple(j_by_direction),
        j2_sum=sum(j2_by_direction),
        j2_sum_by_direction=tuple(j2_by_direction),
        j_nonzero=sum(j_nonzero_by_direction),
        j_nonzero_by_direction=tuple(j_nonzero_by_direction),
        homology=homology,
        lowest_momenta=momenta,
        axis_average_current_power=axis_average,
    )


def verify_checkpoint(L: int, record: Mapping[str, object]) -> DerivedState:
    """Verify exact checkpoint schema and every state-derived engine claim."""

    actual_fields = frozenset(record)
    _require(
        actual_fields == CHECKPOINT_FIELDS,
        f"checkpoint:schema:missing={sorted(CHECKPOINT_FIELDS - actual_fields)!r}:extra={sorted(actual_fields - CHECKPOINT_FIELDS)!r}",
    )
    _require(record.get("type") == "checkpoint", "checkpoint:type")
    _require(_exact_int(record.get("L"), "checkpoint:L") == L, "checkpoint:L_mismatch")
    _uint64(record.get("checkpoint"), "checkpoint:index")
    _uint64(record.get("post_warm_bottom_attempt"), "checkpoint:post_warm_bottom_attempt")
    _uint64(record.get("swap_accepted"), "checkpoint:swap_accepted")
    _uint64(record.get("transition"), "checkpoint:transition")
    _uint64(record.get("walker_id"), "checkpoint:walker_id")
    derived = derive_state(L, record.get("state_2bit_base64"), record.get("state_sha256"))

    _require(_uint64(record.get("support"), "checkpoint:support") == derived.support, "checkpoint:support_mismatch")
    _require(_int64(record.get("n_sum"), "checkpoint:n_sum") == derived.n_sum, "checkpoint:n_sum_mismatch")
    _require(_uint64(record.get("j_nnz"), "checkpoint:j_nnz") == derived.j_nonzero, "checkpoint:j_nnz_mismatch")
    _require(_uint64(record.get("j2_sum"), "checkpoint:j2_sum") == derived.j2_sum, "checkpoint:j2_sum_mismatch")
    _require(
        _uint64(record.get("current_nonzero"), "checkpoint:current_nonzero")
        == int(derived.j_nonzero != 0),
        "checkpoint:current_nonzero_mismatch",
    )
    _require(_exact_string(record.get("current_hash"), "checkpoint:current_hash") == derived.current_hash, "checkpoint:current_hash_mismatch")
    _require(
        _exact_string(record.get("packed_state_sha256"), "checkpoint:packed_state_sha256")
        == derived.packed_state_sha256,
        "checkpoint:packed_state_sha256_mismatch",
    )
    claimed_homology = record.get("homology")
    _require(
        isinstance(claimed_homology, list)
        and len(claimed_homology) == len(PAIRS)
        and all(type(value) is int and 0 <= value <= 4 for value in claimed_homology),
        "checkpoint:homology_schema",
    )
    _require(tuple(claimed_homology) == derived.homology, "checkpoint:H2_mismatch")
    return derived


def sufficient_record(record: Mapping[str, object], derived: DerivedState) -> dict[str, object]:
    """Replace a full engine frame with compact reader-authoritative statistics."""

    result = {key: value for key, value in record.items() if key != "state_2bit_base64"}
    result.update(
        {
            "j_nonzero_by_direction": list(derived.j_nonzero_by_direction),
            "j_sum": derived.j_sum,
            "j_sum_by_direction": list(derived.j_sum_by_direction),
            "j2_sum_by_direction": list(derived.j2_sum_by_direction),
            "n_sum_by_orientation": list(derived.n_sum_by_orientation),
            "n2_sum": derived.n2_sum,
            "n2_sum_by_orientation": list(derived.n2_sum_by_orientation),
            "pair_sums": [entry.total for entry in derived.pair_sums],
            "sj2_longitudinal": [
                list(entry.longitudinal_twice_unnormalized)
                for entry in derived.lowest_momenta
            ],
            "sj2_trace": [
                list(entry.trace_twice_unnormalized)
                for entry in derived.lowest_momenta
            ],
        }
    )
    checkpoint = _exact_int(record.get("checkpoint"), "checkpoint:index")
    if should_audit(checkpoint):
        result["state_b64"] = record["state_2bit_base64"]
    return result


def should_audit(checkpoint: int) -> bool:
    return 1 <= checkpoint <= FORMAL_CHECKPOINTS and checkpoint % STATE_AUDIT_STRIDE == 0


def committed_size_upper_bound() -> int:
    """Conservative schema-width proof for the formal L8 committed stream.

    The checkpoint template uses signed/unsigned 64-bit extrema, so it is
    wider than any value admitted by the reader or the L8 engine contract.
    The run and summary allowances are separately capped canonical lines.
    No L8 physical state is constructed by this proof.
    """

    signed_wide = -(1 << 63)
    unsigned_wide = (1 << 64) - 1
    hash_wide = "f" * 64
    pair_wide = [signed_wide, signed_wide]
    checkpoint: dict[str, object] = {
        "L": 8,
        "checkpoint": FORMAL_CHECKPOINTS,
        "current_hash": hash_wide,
        "current_nonzero": 1,
        "homology": [4] * 6,
        "j_nnz": unsigned_wide,
        "j2_sum": unsigned_wide,
        "n_sum": signed_wide,
        "packed_state_sha256": hash_wide,
        "post_warm_bottom_attempt": unsigned_wide,
        "state_sha256": hash_wide,
        "support": unsigned_wide,
        "swap_accepted": 1,
        "transition": unsigned_wide,
        "type": "checkpoint",
        "walker_id": unsigned_wide,
        "j_nonzero_by_direction": [unsigned_wide] * 4,
        "j_sum": signed_wide,
        "j_sum_by_direction": [signed_wide] * 4,
        "j2_sum_by_direction": [unsigned_wide] * 4,
        "n_sum_by_orientation": [signed_wide] * 6,
        "n2_sum": unsigned_wide,
        "n2_sum_by_orientation": [unsigned_wide] * 6,
        "pair_sums": [signed_wide] * 4,
        "sj2_longitudinal": [pair_wide] * 4,
        "sj2_trace": [pair_wide] * 4,
    }
    ordinary = len(_canonical_json_line(checkpoint))
    checkpoint["state_b64"] = "A" * (4 * ((packed_state_size(8) + 2) // 3))
    audited = len(_canonical_json_line(checkpoint))
    audit_count = FORMAL_CHECKPOINTS // STATE_AUDIT_STRIDE
    return (
        MAX_COMMITTED_RUN_BYTES
        + MAX_COMMITTED_SUMMARY_BYTES
        + (FORMAL_CHECKPOINTS - audit_count) * ordinary
        + audit_count * audited
    )


def _canonical_json_line(record: Mapping[str, object]) -> bytes:
    try:
        encoded = json.dumps(
            record,
            allow_nan=False,
            ensure_ascii=True,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("ascii") + b"\n"
    except (TypeError, ValueError, UnicodeError) as error:
        raise StateIntegrityError("reader:cannot_encode_canonical_JSON") from error
    return encoded


def _canonical_json_int(token: str) -> int:
    if re.fullmatch(r"(?:0|-?[1-9][0-9]*)", token) is None:
        _fail(f"reader:noncanonical_JSON_integer_{token!r}")
    return int(token)


def _reject_json_number(token: str) -> float:
    _fail(f"reader:floating_or_nonfinite_JSON_number_{token!r}")
    raise AssertionError("unreachable")


def _unique_object(pairs: Sequence[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        _require(key not in result, f"reader:duplicate_JSON_key_{key!r}")
        result[key] = value
    return result


def _parse_engine_line(raw: bytes, line_number: int) -> dict[str, object]:
    _require(raw.endswith(b"\n"), f"reader:line_{line_number}:missing_LF")
    body = raw[:-1]
    _require(body.startswith(b"{") and body.endswith(b"}"), f"reader:line_{line_number}:not_object")
    _require(not any(byte in b" \t\r\v\f" for byte in body), f"reader:line_{line_number}:whitespace")
    _require(b"\\" not in body, f"reader:line_{line_number}:JSON_escape")
    try:
        text = body.decode("ascii")
        value = json.loads(
            text,
            object_pairs_hook=_unique_object,
            parse_int=_canonical_json_int,
            parse_float=_reject_json_number,
            parse_constant=_reject_json_number,
        )
    except StateIntegrityError:
        raise
    except (UnicodeError, TypeError, ValueError, json.JSONDecodeError) as error:
        raise StateIntegrityError(f"reader:line_{line_number}:invalid_JSON") from error
    _require(isinstance(value, dict), f"reader:line_{line_number}:not_object")
    return value


def _read_limited_line(stream, line_number: int, total: int) -> tuple[bytes, int]:
    raw = stream.readline(MAX_ENGINE_LINE_BYTES + 1)
    _require(len(raw) <= MAX_ENGINE_LINE_BYTES, f"reader:line_{line_number}:line_cap")
    total += len(raw)
    _require(total <= MAX_ENGINE_STREAM_BYTES, "reader:engine_stream_cap")
    return raw, total


def transform_stream(input_stream, output_stream, expected_L: int) -> tuple[int, str]:
    """Online full-state firewall and compact sufficient-statistics transform."""

    _require(expected_L in (6, 8), "reader:formal_extent_must_be_6_or_8")
    input_total = 0
    output_total = 0

    def emit(record: Mapping[str, object], line_cap: int | None = None) -> None:
        nonlocal output_total
        line = _canonical_json_line(record)
        if line_cap is not None:
            _require(len(line) <= line_cap, "reader:canonical_record_line_cap")
        output_total += len(line)
        _require(output_total <= MAX_COMMITTED_STREAM_BYTES, "reader:committed_stream_cap")
        output_stream.write(line)

    raw, input_total = _read_limited_line(input_stream, 1, input_total)
    _require(bool(raw), "reader:missing_run")
    run = _parse_engine_line(raw, 1)
    actual_fields = frozenset(run)
    _require(
        actual_fields == RUN_FIELDS,
        f"reader:run_schema:missing={sorted(RUN_FIELDS - actual_fields)!r}:extra={sorted(actual_fields - RUN_FIELDS)!r}",
    )
    _require(run.get("type") == "run", "reader:run_type")
    _require(_exact_int(run.get("L"), "reader:run:L") == expected_L, "reader:run_L")
    _require(
        _exact_int(run.get("checkpoints"), "reader:run:checkpoints") == FORMAL_CHECKPOINTS,
        "reader:run_checkpoint_count",
    )
    verify_encoding_header(expected_L, run)
    emitted_run = dict(run)
    emitted_run["reader_schema"] = READER_SCHEMA
    emitted_run["state_audit_stride"] = STATE_AUDIT_STRIDE
    emit(emitted_run, MAX_COMMITTED_RUN_BYTES)

    rolling = hashlib.sha256()
    rolling.update(PACKED_STREAM_DOMAIN)
    rolling.update(f"L={expected_L}\0".encode("ascii"))
    last_derived: DerivedState | None = None
    audit_frames = 0
    for checkpoint in range(1, FORMAL_CHECKPOINTS + 1):
        line_number = checkpoint + 1
        raw, input_total = _read_limited_line(input_stream, line_number, input_total)
        _require(bool(raw), f"reader:missing_checkpoint_{checkpoint}")
        record = _parse_engine_line(raw, line_number)
        _require(
            _exact_int(record.get("checkpoint"), f"reader:checkpoint[{checkpoint}]:index")
            == checkpoint,
            f"reader:checkpoint[{checkpoint}]:order",
        )
        derived = verify_checkpoint(expected_L, record)
        rolling.update(derived.packed)
        compact = sufficient_record(record, derived)
        if should_audit(checkpoint):
            audit_frames += 1
        emit(compact)
        last_derived = derived

    raw, input_total = _read_limited_line(input_stream, FORMAL_CHECKPOINTS + 2, input_total)
    _require(bool(raw), "reader:missing_summary")
    summary = _parse_engine_line(raw, FORMAL_CHECKPOINTS + 2)
    _require(summary.get("type") == "summary", "reader:summary_type")
    _require(_exact_int(summary.get("L"), "reader:summary:L") == expected_L, "reader:summary_L")
    _require(
        _exact_int(summary.get("checkpoints"), "reader:summary:checkpoints")
        == FORMAL_CHECKPOINTS,
        "reader:summary_checkpoint_count",
    )
    _require(last_derived is not None, "reader:no_checkpoints")
    _require(summary.get("final_state_sha256") == last_derived.state_sha256, "reader:summary_final_state")
    emitted_summary = dict(summary)
    emitted_summary.update(
        {
            "packed_frame_bytes": packed_state_size(expected_L),
            "packed_frames": FORMAL_CHECKPOINTS,
            "packed_stream_sha256": rolling.hexdigest(),
            "reader_schema": READER_SCHEMA,
            "state_audit_frames": audit_frames,
        }
    )
    emit(emitted_summary, MAX_COMMITTED_SUMMARY_BYTES)

    extra, input_total = _read_limited_line(input_stream, FORMAL_CHECKPOINTS + 3, input_total)
    _require(extra == b"", "reader:trailing_record")
    if hasattr(output_stream, "flush"):
        output_stream.flush()
    return output_total, rolling.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="CROSSCHECK-2 independent state reader")
    parser.add_argument("--expect-L", dest="expected_L", type=int, required=True, choices=(6, 8))
    args = parser.parse_args()
    try:
        transform_stream(sys.stdin.buffer, sys.stdout.buffer, args.expected_L)
    except (StateIntegrityError, BrokenPipeError, OSError, ValueError) as error:
        print(f"STATE_READER_FAILURE {str(error).replace(' ', '_')}", file=sys.stderr)
        return 1
    return 0


__all__ = [
    "CHECKPOINT_FIELDS",
    "DIM",
    "DerivedState",
    "ExactPower",
    "FAMILY_NAMES",
    "FORMAL_CHECKPOINTS",
    "MAX_COMMITTED_STREAM_BYTES",
    "MAX_COMMITTED_RUN_BYTES",
    "MAX_COMMITTED_SUMMARY_BYTES",
    "MAX_ENGINE_LINE_BYTES",
    "MAX_ENGINE_STREAM_BYTES",
    "MomentumPower",
    "PAIRS",
    "PAIR_LABELS",
    "PairSums",
    "Qsqrt2",
    "READER_SCHEMA",
    "RUN_FIELDS",
    "STATE_ENCODING",
    "STATE_AUDIT_STRIDE",
    "StateIntegrityError",
    "derive_state",
    "pack_residues",
    "packed_bytes",
    "packed_state_size",
    "state_size",
    "committed_size_upper_bound",
    "should_audit",
    "unpack_residues",
    "verify_checkpoint",
    "verify_encoding_header",
]


if __name__ == "__main__":
    raise SystemExit(main())
