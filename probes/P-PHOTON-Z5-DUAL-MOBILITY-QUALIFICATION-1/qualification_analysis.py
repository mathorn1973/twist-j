#!/usr/bin/env python3
"""Strict, side-effect-free analysis of mobility-qualification JSONL logs.

The engine is intentionally not invoked here.  A caller supplies every run
expectation (including seed and schedule), the already-produced JSONL bytes or
paths, and an explicit path plus SHA-256 custody value for the frozen pilot-2
statistics implementation.  No run seed or formal schedule is embedded in
this module.

The public API is :func:`analyze_logs`.  It returns deterministic concise
``lines`` and ordered ``failures``; malformed or incomplete inputs become an
``INTEGRITY`` failure rather than a partial mobility verdict.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import re
import statistics
import sys
from types import ModuleType
from typing import Callable, Mapping, Sequence


UINT64_MAX = (1 << 64) - 1
FROZEN_STATS_PROBE = "P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2"
FROZEN_STATS_FILE = "analyze_pilot.py"
FAMILY_NAMES = (
    "hold",
    "legacy",
    "conjugation",
    "cube",
    "tristar",
    "homology",
    "swap",
)
H2_NAMES = ("01", "02", "03", "12", "13", "23")

# These binary64 literals, rather than a host libm call, define the Z5
# character contrasts used by this qualification.
Z5_COS = (
    1.0,
    0.30901699437494745,
    -0.8090169943749475,
    -0.8090169943749475,
    0.30901699437494745,
)
Z5_SIN = (
    0.0,
    0.9510565162951535,
    0.5877852522924731,
    -0.5877852522924731,
    -0.9510565162951535,
)

MIXING_METRICS = (
    "support_fraction",
    "n_mean",
    "h_norm",
    *(f"H2_{name}_{part}" for name in H2_NAMES for part in ("cos", "sin")),
)

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
        "post_warm_bottom_attempt",
        "state_sha256",
        "support",
        "swap_accepted",
        "transition",
        "type",
        "walker_id",
    }
)

SUMMARY_FIELDS = frozenset(
    {
        "L",
        "S",
        "bottom_attempts",
        "bottom_census_current_entries",
        "bottom_census_current_exits",
        "bottom_target_validations",
        "checkpoint_current_entries",
        "checkpoint_current_exits",
        "checkpoint_target_validations",
        "checkpoints",
        "distinct_H2_vectors",
        "distinct_nonzero_current_hashes",
        "distinct_nonzero_current_walkers",
        "final_homology",
        "final_state_sha256",
        "final_support",
        "homology_component_changes",
        "homology_visited_values",
        "max_current_excursion_bottom_attempts",
        "max_zero_wait_bottom_attempts",
        "measured_current_swap_down",
        "measured_current_swap_up",
        "measured_family_attempts",
        "measured_homology_swap_down",
        "measured_homology_swap_up",
        "measured_legacy_accepts",
        "measured_legacy_firewall_rejects",
        "measured_legacy_max_word",
        "measured_legacy_metropolis_rejects",
        "measured_local_current_births",
        "measured_local_current_deaths",
        "measured_local_current_vector_moves",
        "measured_local_homology_births",
        "measured_local_homology_deaths",
        "measured_local_homology_moves",
        "measured_roundtrips",
        "measured_swap_accepts",
        "measured_swap_attempts",
        "measured_target_current_entries",
        "measured_target_current_exits",
        "measured_target_current_exports",
        "measured_target_current_imports",
        "measured_target_local_current_births",
        "measured_transitions",
        "measured_walker_roundtrips",
        "measurement_start_transition",
        "nonzero_current_bottom_censuses",
        "nonzero_current_checkpoints",
        "nonzero_current_hashes",
        "nonzero_current_walker_ids",
        "post_warm_bottom_attempts",
        "product_validations",
        "quartile_current_entries",
        "quartile_current_exits",
        "quartile_H2_component_changes",
        "quartile_H2_vector_counts",
        "quartile_H2_visited_values",
        "quartile_nonzero_current_censuses",
        "state_hashes",
        "thin",
        "total_family_attempts",
        "total_legacy_accepts",
        "total_legacy_firewall_rejects",
        "total_legacy_max_word",
        "total_legacy_metropolis_rejects",
        "total_local_current_births",
        "total_local_current_deaths",
        "total_local_current_vector_moves",
        "total_local_homology_births",
        "total_local_homology_deaths",
        "total_local_homology_moves",
        "total_roundtrips",
        "total_swap_accepts",
        "total_swap_attempts",
        "total_target_current_entries",
        "total_target_current_exits",
        "total_transitions",
        "total_walker_roundtrips",
        "type",
        "validation_stride",
    }
)

LEVEL_VECTOR_FIELDS = (
    "measured_local_current_births",
    "measured_local_current_deaths",
    "measured_local_current_vector_moves",
    "measured_local_homology_births",
    "measured_local_homology_deaths",
    "measured_local_homology_moves",
    "measured_walker_roundtrips",
    "total_local_current_births",
    "total_local_current_deaths",
    "total_local_current_vector_moves",
    "total_local_homology_births",
    "total_local_homology_deaths",
    "total_local_homology_moves",
    "total_walker_roundtrips",
)

EDGE_VECTOR_FIELDS = (
    "measured_current_swap_down",
    "measured_current_swap_up",
    "measured_homology_swap_down",
    "measured_homology_swap_up",
    "measured_swap_accepts",
    "measured_swap_attempts",
    "total_swap_accepts",
    "total_swap_attempts",
)

MEASURED_TOTAL_PAIRS = (
    ("measured_legacy_accepts", "total_legacy_accepts"),
    ("measured_legacy_firewall_rejects", "total_legacy_firewall_rejects"),
    ("measured_legacy_max_word", "total_legacy_max_word"),
    ("measured_legacy_metropolis_rejects", "total_legacy_metropolis_rejects"),
    ("measured_local_current_births", "total_local_current_births"),
    ("measured_local_current_deaths", "total_local_current_deaths"),
    ("measured_local_current_vector_moves", "total_local_current_vector_moves"),
    ("measured_local_homology_births", "total_local_homology_births"),
    ("measured_local_homology_deaths", "total_local_homology_deaths"),
    ("measured_local_homology_moves", "total_local_homology_moves"),
    ("measured_roundtrips", "total_roundtrips"),
    ("measured_swap_accepts", "total_swap_accepts"),
    ("measured_swap_attempts", "total_swap_attempts"),
    ("measured_walker_roundtrips", "total_walker_roundtrips"),
)

LOWER_HEX_32 = re.compile(r"0x[0-9a-f]{32}\Z")
LOWER_HEX_64 = re.compile(r"[0-9a-f]{64}\Z")
CANONICAL_INTEGER = re.compile(r"(?:0|-?[1-9][0-9]*)\Z")


class IntegrityError(ValueError):
    """A JSONL input, run contract, or frozen dependency is not exact."""


@dataclass(frozen=True)
class RunExpectation:
    """Externally pinned identity and schedule for one engine invocation."""

    label: str
    L: int
    bitstream_domain: str
    development_only: bool
    seed: str
    start: str
    warm_bottom: int
    checkpoints: int
    thin: int
    validation_stride: int
    transition_cap: int
    legacy_selector_probability: str = "1/16"


@dataclass(frozen=True)
class ParsedChain:
    expectation: RunExpectation
    run: Mapping[str, object]
    checkpoints: tuple[Mapping[str, object], ...]
    summary: Mapping[str, object]


@dataclass(frozen=True)
class AnalysisResult:
    lines: tuple[str, ...]
    failures: tuple[str, ...]


@dataclass(frozen=True)
class StatisticalGates:
    per_chain_ess_min: float = 128.0
    rhat_max: float = 1.03
    bulk_ess_min: float = 400.0
    tail_ess_min: float = 200.0
    drift_z_max: float = 4.0
    start_z_max: float = 4.0


CustodyHook = Callable[[Path, str], None]
LogSource = bytes | bytearray | memoryview | Path


def _fail(message: str) -> None:
    raise IntegrityError(message)


def _require(condition: bool, message: str) -> None:
    if not condition:
        _fail(message)


def _validate_statistical_gates(gates: StatisticalGates) -> None:
    """Allow development overrides only when they cannot loosen the pin."""

    values = (
        gates.per_chain_ess_min,
        gates.rhat_max,
        gates.bulk_ess_min,
        gates.tail_ess_min,
        gates.drift_z_max,
        gates.start_z_max,
    )
    _require(all(math.isfinite(value) and value > 0.0 for value in values), "statistics:gates_not_finite_positive")
    _require(gates.per_chain_ess_min >= 128.0, "statistics:per_chain_ess_gate_loosened")
    _require(gates.rhat_max <= 1.03, "statistics:rhat_gate_loosened")
    _require(gates.bulk_ess_min >= 400.0, "statistics:bulk_ess_gate_loosened")
    _require(gates.tail_ess_min >= 200.0, "statistics:tail_ess_gate_loosened")
    _require(gates.drift_z_max <= 4.0, "statistics:drift_gate_loosened")
    _require(gates.start_z_max <= 4.0, "statistics:start_gate_loosened")


def _canonical_json_int(token: str) -> int:
    if CANONICAL_INTEGER.fullmatch(token) is None:
        _fail(f"noncanonical JSON integer {token!r}")
    value = int(token)
    if not -(1 << 63) <= value <= UINT64_MAX:
        _fail("JSON integer outside supported engine range")
    return value


def _reject_float(token: str) -> float:
    _fail(f"floating JSON number is forbidden: {token!r}")
    raise AssertionError("unreachable")


def _reject_constant(token: str) -> float:
    _fail(f"non-finite JSON token is forbidden: {token!r}")
    raise AssertionError("unreachable")


def _unique_object(pairs: Sequence[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            _fail(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def _json_record(raw: bytes, label: str, line_number: int) -> dict[str, object]:
    _require(raw.startswith(b"{") and raw.endswith(b"}"), f"{label}:{line_number}:not_object")
    _require(not any(byte in b" \t\r\v\f" for byte in raw), f"{label}:{line_number}:noncanonical_whitespace")
    _require(b"\\" not in raw, f"{label}:{line_number}:unexpected_JSON_escape")
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError as error:
        raise IntegrityError(f"{label}:{line_number}:non_ASCII") from error
    try:
        value = json.loads(
            text,
            object_pairs_hook=_unique_object,
            parse_int=_canonical_json_int,
            parse_float=_reject_float,
            parse_constant=_reject_constant,
        )
    except IntegrityError:
        raise
    except (TypeError, ValueError, json.JSONDecodeError) as error:
        raise IntegrityError(f"{label}:{line_number}:invalid_JSON") from error
    _require(isinstance(value, dict), f"{label}:{line_number}:not_object")
    return value


def _exact_fields(record: Mapping[str, object], fields: frozenset[str], where: str) -> None:
    actual = frozenset(record)
    if actual != fields:
        missing = sorted(fields - actual)
        extra = sorted(actual - fields)
        _fail(f"{where}:schema missing={missing!r} extra={extra!r}")


def _uint(value: object, where: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= UINT64_MAX:
        _fail(f"{where}:not_uint64")
    return value


def _signed(value: object, where: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or not -(1 << 63) <= value < (1 << 63):
        _fail(f"{where}:not_int64")
    return value


def _literal(value: object, expected: object, where: str) -> None:
    if type(value) is not type(expected) or value != expected:
        _fail(f"{where}:expected_{expected!r}_got_{value!r}")


def _uint_vector(record: Mapping[str, object], key: str, length: int, where: str) -> list[int]:
    value = record[key]
    if not isinstance(value, list) or len(value) != length:
        _fail(f"{where}:{key}:expected_vector_length_{length}")
    return [_uint(entry, f"{where}:{key}[{index}]") for index, entry in enumerate(value)]


def _homology(value: object, where: str) -> tuple[int, ...]:
    if not isinstance(value, list) or len(value) != 6:
        _fail(f"{where}:homology_shape")
    result = tuple(_uint(entry, f"{where}:homology[{index}]") for index, entry in enumerate(value))
    if any(entry > 4 for entry in result):
        _fail(f"{where}:homology_residue")
    return result


def _hash64(value: object, where: str, allow_empty: bool = False) -> str:
    if not isinstance(value, str):
        _fail(f"{where}:not_string")
    if allow_empty and value == "":
        return value
    if LOWER_HEX_64.fullmatch(value) is None:
        _fail(f"{where}:not_lower_sha256")
    return value


def _sorted_hashes(value: object, where: str) -> list[str]:
    if not isinstance(value, list):
        _fail(f"{where}:not_list")
    result = [_hash64(entry, f"{where}[{index}]") for index, entry in enumerate(value)]
    if result != sorted(set(result)):
        _fail(f"{where}:not_strictly_sorted_unique")
    return result


def _sorted_walkers(value: object, S: int, where: str) -> list[int]:
    if not isinstance(value, list):
        _fail(f"{where}:not_list")
    result = [_uint(entry, f"{where}[{index}]") for index, entry in enumerate(value)]
    if any(entry > S for entry in result) or result != sorted(set(result)):
        _fail(f"{where}:not_sorted_unique_walker_ids")
    return result


def _family_counts(value: object, where: str) -> dict[str, int]:
    if not isinstance(value, dict) or tuple(value) != FAMILY_NAMES:
        _fail(f"{where}:family_schema_or_engine_order")
    return {name: _uint(value[name], f"{where}:{name}") for name in FAMILY_NAMES}


def _visited_values(value: object, where: str) -> list[list[int]]:
    if not isinstance(value, list) or len(value) != 6:
        _fail(f"{where}:shape")
    result: list[list[int]] = []
    for component, entries in enumerate(value):
        if not isinstance(entries, list):
            _fail(f"{where}[{component}]:not_list")
        parsed = [_uint(entry, f"{where}[{component}][]") for entry in entries]
        if any(entry > 4 for entry in parsed) or parsed != sorted(set(parsed)):
            _fail(f"{where}[{component}]:not_sorted_unique_Z5")
        result.append(parsed)
    return result


def _quartile_visited_values(value: object, where: str) -> list[list[list[int]]]:
    if not isinstance(value, list) or len(value) != 4:
        _fail(f"{where}:quartile_shape")
    return [_visited_values(entry, f"{where}[{index}]") for index, entry in enumerate(value)]


def _quartile_changes(value: object, where: str) -> list[list[int]]:
    if not isinstance(value, list) or len(value) != 4:
        _fail(f"{where}:quartile_shape")
    result: list[list[int]] = []
    for quartile, entries in enumerate(value):
        if not isinstance(entries, list) or len(entries) != 6:
            _fail(f"{where}[{quartile}]:component_shape")
        result.append([_uint(entry, f"{where}[{quartile}][{component}]") for component, entry in enumerate(entries)])
    return result


def _quartile_sizes(count: int) -> tuple[int, int, int, int]:
    quotient, remainder = divmod(count, 4)
    boundaries = [k * quotient + (k * remainder) // 4 for k in range(5)]
    return tuple(boundaries[index + 1] - boundaries[index] for index in range(4))  # type: ignore[return-value]


def _expected_validation_count(count: int, thin: int, stride: int) -> int:
    common = math.lcm(thin, stride)
    union = count // thin + count // stride - count // common
    if thin != 1 and stride != 1:
        union += 1
    return union


def _read_log_source(source: LogSource, label: str) -> bytes:
    if isinstance(source, Path):
        try:
            return source.read_bytes()
        except OSError as error:
            raise IntegrityError(f"{label}:cannot_read_log") from error
    if isinstance(source, (bytes, bytearray, memoryview)):
        return bytes(source)
    _fail(f"{label}:unsupported_log_source")
    raise AssertionError("unreachable")


def _validate_expectation(expected: RunExpectation) -> None:
    _require(bool(expected.label) and expected.label.isascii(), "expectation:bad_label")
    _require(expected.L in (3, 4), f"{expected.label}:L_must_be_3_or_4")
    _require(isinstance(expected.bitstream_domain, str) and bool(expected.bitstream_domain), f"{expected.label}:bad_domain")
    _require(type(expected.development_only) is bool, f"{expected.label}:bad_development_flag")
    _require(LOWER_HEX_32.fullmatch(expected.seed) is not None, f"{expected.label}:bad_seed")
    _require(expected.start in ("cold", "stratified"), f"{expected.label}:bad_start")
    _require(expected.legacy_selector_probability == "1/16", f"{expected.label}:bad_legacy_probability")
    for name in ("warm_bottom", "checkpoints", "thin", "validation_stride", "transition_cap"):
        value = getattr(expected, name)
        _uint(value, f"{expected.label}:{name}")
        _require(value > 0, f"{expected.label}:{name}_must_be_positive")
    _require(expected.checkpoints >= 128 and expected.checkpoints % 2 == 0, f"{expected.label}:checkpoints_must_be_even_and_at_least_128")
    post = expected.checkpoints * expected.thin
    _require(post <= UINT64_MAX - expected.warm_bottom, f"{expected.label}:bottom_budget_overflow")


def parse_chain(source: LogSource, expected: RunExpectation) -> ParsedChain:
    """Parse one exact run/checkpoint/summary JSONL stream."""

    _validate_expectation(expected)
    data = _read_log_source(source, expected.label)
    _require(data.endswith(b"\n"), f"{expected.label}:missing_final_LF")
    _require(b"\r" not in data, f"{expected.label}:CR_forbidden")
    lines = data[:-1].split(b"\n")
    _require(all(lines), f"{expected.label}:blank_line")
    required_lines = expected.checkpoints + 2
    _require(len(lines) == required_lines, f"{expected.label}:line_count_{len(lines)}_expected_{required_lines}")
    records = [_json_record(line, expected.label, index + 1) for index, line in enumerate(lines)]
    run = records[0]
    checkpoints = records[1:-1]
    summary = records[-1]

    _exact_fields(run, RUN_FIELDS, f"{expected.label}:run")
    _literal(run["type"], "run", f"{expected.label}:run:type")
    _literal(run["L"], expected.L, f"{expected.label}:run:L")
    _literal(run["S"], max(15, expected.L * expected.L), f"{expected.label}:run:S")
    _literal(run["bitstream_domain"], expected.bitstream_domain, f"{expected.label}:run:domain")
    _literal(run["development_only"], expected.development_only, f"{expected.label}:run:development_only")
    _literal(run["legacy_selector_probability"], expected.legacy_selector_probability, f"{expected.label}:run:legacy_probability")
    _literal(run["seed"], expected.seed, f"{expected.label}:run:seed")
    _literal(run["start"], expected.start, f"{expected.label}:run:start")
    for name in ("warm_bottom", "checkpoints", "thin", "validation_stride", "transition_cap"):
        _literal(run[name], getattr(expected, name), f"{expected.label}:run:{name}")

    n_plaq = 6 * expected.L**4
    S = max(15, expected.L * expected.L)
    previous_transition = -1
    parsed_checkpoints: list[Mapping[str, object]] = []
    for index, checkpoint in enumerate(checkpoints, 1):
        where = f"{expected.label}:checkpoint[{index}]"
        _exact_fields(checkpoint, CHECKPOINT_FIELDS, where)
        _literal(checkpoint["type"], "checkpoint", f"{where}:type")
        _literal(checkpoint["L"], expected.L, f"{where}:L")
        _literal(checkpoint["checkpoint"], index, f"{where}:index")
        _literal(checkpoint["post_warm_bottom_attempt"], index * expected.thin, f"{where}:bottom_attempt")
        homology = _homology(checkpoint["homology"], where)
        current_nonzero = _uint(checkpoint["current_nonzero"], f"{where}:current_nonzero")
        swap_accepted = _uint(checkpoint["swap_accepted"], f"{where}:swap_accepted")
        _require(current_nonzero <= 1 and swap_accepted <= 1, f"{where}:binary_field")
        j_nnz = _uint(checkpoint["j_nnz"], f"{where}:j_nnz")
        j2_sum = _uint(checkpoint["j2_sum"], f"{where}:j2_sum")
        _require(j_nnz <= 4 * expected.L**4, f"{where}:j_nnz_bound")
        _require(current_nonzero == int(j_nnz != 0) == int(j2_sum != 0), f"{where}:current_census_identity")
        current_hash = _hash64(checkpoint["current_hash"], f"{where}:current_hash", allow_empty=True)
        _require((current_hash != "") == bool(current_nonzero), f"{where}:current_hash_identity")
        _hash64(checkpoint["state_sha256"], f"{where}:state_sha256")
        support = _uint(checkpoint["support"], f"{where}:support")
        n_sum = _signed(checkpoint["n_sum"], f"{where}:n_sum")
        _require(support <= n_plaq and abs(n_sum) <= support and (support - n_sum) % 2 == 0, f"{where}:hard_state_moments")
        transition = _uint(checkpoint["transition"], f"{where}:transition")
        _require(transition > previous_transition, f"{where}:transition_not_increasing")
        previous_transition = transition
        walker = _uint(checkpoint["walker_id"], f"{where}:walker_id")
        _require(walker <= S, f"{where}:walker_out_of_range")
        _require(all(0 <= value <= 4 for value in homology), f"{where}:homology")
        parsed_checkpoints.append(checkpoint)

    _validate_summary(summary, expected, tuple(parsed_checkpoints))
    return ParsedChain(expected, run, tuple(parsed_checkpoints), summary)


def _validate_summary(
    summary: Mapping[str, object],
    expected: RunExpectation,
    checkpoints: tuple[Mapping[str, object], ...],
) -> None:
    label = expected.label
    where = f"{label}:summary"
    _exact_fields(summary, SUMMARY_FIELDS, where)
    _literal(summary["type"], "summary", f"{where}:type")
    S = max(15, expected.L * expected.L)
    post = expected.checkpoints * expected.thin
    _literal(summary["L"], expected.L, f"{where}:L")
    _literal(summary["S"], S, f"{where}:S")
    _literal(summary["checkpoints"], expected.checkpoints, f"{where}:checkpoints")
    _literal(summary["thin"], expected.thin, f"{where}:thin")
    _literal(summary["validation_stride"], expected.validation_stride, f"{where}:validation_stride")
    _literal(summary["post_warm_bottom_attempts"], post, f"{where}:post_warm_bottom_attempts")
    _literal(summary["bottom_attempts"], expected.warm_bottom + post, f"{where}:bottom_attempts")
    _literal(summary["checkpoint_target_validations"], expected.checkpoints, f"{where}:checkpoint_validations")
    _literal(summary["bottom_target_validations"], _expected_validation_count(post, expected.thin, expected.validation_stride), f"{where}:bottom_validations")
    _literal(summary["product_validations"], 2, f"{where}:product_validations")

    for key in LEVEL_VECTOR_FIELDS:
        _uint_vector(summary, key, S + 1, where)
    for key in EDGE_VECTOR_FIELDS:
        _uint_vector(summary, key, S, where)
    for key in (
        "bottom_census_current_entries",
        "bottom_census_current_exits",
        "checkpoint_current_entries",
        "checkpoint_current_exits",
        "distinct_H2_vectors",
        "distinct_nonzero_current_hashes",
        "distinct_nonzero_current_walkers",
        "final_support",
        "max_current_excursion_bottom_attempts",
        "max_zero_wait_bottom_attempts",
        "measured_legacy_accepts",
        "measured_legacy_firewall_rejects",
        "measured_legacy_max_word",
        "measured_legacy_metropolis_rejects",
        "measured_roundtrips",
        "measured_target_current_entries",
        "measured_target_current_exits",
        "measured_target_current_exports",
        "measured_target_current_imports",
        "measured_target_local_current_births",
        "measured_transitions",
        "measurement_start_transition",
        "nonzero_current_bottom_censuses",
        "nonzero_current_checkpoints",
        "state_hashes",
        "total_legacy_accepts",
        "total_legacy_firewall_rejects",
        "total_legacy_max_word",
        "total_legacy_metropolis_rejects",
        "total_roundtrips",
        "total_target_current_entries",
        "total_target_current_exits",
        "total_transitions",
    ):
        _uint(summary[key], f"{where}:{key}")

    final_homology = _homology(summary["final_homology"], f"{where}:final_homology")
    _hash64(summary["final_state_sha256"], f"{where}:final_state_sha256")
    hashes = _sorted_hashes(summary["nonzero_current_hashes"], f"{where}:nonzero_current_hashes")
    walkers = _sorted_walkers(summary["nonzero_current_walker_ids"], S, f"{where}:nonzero_current_walker_ids")
    _literal(summary["distinct_nonzero_current_hashes"], len(hashes), f"{where}:hash_count")
    _literal(summary["distinct_nonzero_current_walkers"], len(walkers), f"{where}:walker_count")

    homology_values = _visited_values(summary["homology_visited_values"], f"{where}:homology_visited_values")
    homology_changes = _uint_vector(summary, "homology_component_changes", 6, where)
    quartile_values = _quartile_visited_values(summary["quartile_H2_visited_values"], f"{where}:quartile_H2_visited_values")
    quartile_changes = _quartile_changes(summary["quartile_H2_component_changes"], f"{where}:quartile_H2_component_changes")
    quartile_vectors = _uint_vector(summary, "quartile_H2_vector_counts", 4, where)
    quartile_entries = _uint_vector(summary, "quartile_current_entries", 4, where)
    quartile_exits = _uint_vector(summary, "quartile_current_exits", 4, where)
    quartile_nonzero = _uint_vector(summary, "quartile_nonzero_current_censuses", 4, where)
    quartile_sizes = _quartile_sizes(post)
    for quartile, size in enumerate(quartile_sizes):
        _require(quartile_nonzero[quartile] <= size, f"{where}:quartile_{quartile}:current_census_bound")
        _require(quartile_vectors[quartile] <= size, f"{where}:quartile_{quartile}:H2_vector_bound")
        _require(quartile_vectors[quartile] > 0, f"{where}:quartile_{quartile}:empty_H2_vectors")
        _require(quartile_entries[quartile] <= size and quartile_exits[quartile] <= size, f"{where}:quartile_{quartile}:current_transition_bound")
        _require(all(value <= size for value in quartile_changes[quartile]), f"{where}:quartile_{quartile}:H2_change_bound")
        _require(all(quartile_values[quartile][component] for component in range(6)), f"{where}:quartile_{quartile}:empty_H2_values")
    _literal(summary["bottom_census_current_entries"], sum(quartile_entries), f"{where}:quartile_entry_sum")
    _literal(summary["bottom_census_current_exits"], sum(quartile_exits), f"{where}:quartile_exit_sum")
    _literal(summary["nonzero_current_bottom_censuses"], sum(quartile_nonzero), f"{where}:quartile_nonzero_sum")
    for component in range(6):
        _literal(homology_changes[component], sum(row[component] for row in quartile_changes), f"{where}:H2_change_sum[{component}]")
        union = sorted({entry for row in quartile_values for entry in row[component]})
        _literal(homology_values[component], union, f"{where}:H2_value_union[{component}]")

    checkpoint_nonzero = sum(_uint(item["current_nonzero"], f"{where}:checkpoint_current") for item in checkpoints)
    _literal(summary["nonzero_current_checkpoints"], checkpoint_nonzero, f"{where}:nonzero_checkpoint_count")
    checkpoint_hashes = {str(item["current_hash"]) for item in checkpoints if item["current_hash"]}
    checkpoint_walkers = {_uint(item["walker_id"], f"{where}:checkpoint_walker") for item in checkpoints if item["current_nonzero"]}
    _require(checkpoint_hashes.issubset(set(hashes)), f"{where}:checkpoint_hash_not_in_census")
    _require(checkpoint_walkers.issubset(set(walkers)), f"{where}:checkpoint_walker_not_in_census")
    _require(len(hashes) <= _uint(summary["nonzero_current_bottom_censuses"], f"{where}:nonzero_censuses"), f"{where}:current_hash_count_bound")
    _require(len(walkers) <= S + 1, f"{where}:current_walker_count_bound")
    _require(checkpoint_nonzero <= _uint(summary["nonzero_current_bottom_censuses"], f"{where}:nonzero_censuses"), f"{where}:checkpoint_current_not_subset")
    checkpoint_H2 = {tuple(item["homology"]) for item in checkpoints}
    _require(_uint(summary["distinct_H2_vectors"], f"{where}:distinct_H2_vectors") >= len(checkpoint_H2), f"{where}:H2_vector_count_below_checkpoints")
    _require(_uint(summary["distinct_H2_vectors"], f"{where}:distinct_H2_vectors") <= post, f"{where}:H2_vector_count_bound")
    for component in range(6):
        observed = {int(item["homology"][component]) for item in checkpoints}  # type: ignore[index]
        _require(observed.issubset(set(homology_values[component])), f"{where}:H2_checkpoint_value_missing[{component}]")

    last = checkpoints[-1]
    _literal(summary["final_state_sha256"], last["state_sha256"], f"{where}:final_state")
    _literal(summary["final_support"], last["support"], f"{where}:final_support")
    _literal(final_homology, tuple(last["homology"]), f"{where}:final_H2")
    _require(_uint(summary["state_hashes"], f"{where}:state_hashes") >= len({item["state_sha256"] for item in checkpoints}), f"{where}:state_hash_count_below_checkpoints")
    _require(_uint(summary["state_hashes"], f"{where}:state_hashes") <= post, f"{where}:state_hash_count_bound")

    checkpoint_entries = sum(not checkpoints[index - 1]["current_nonzero"] and checkpoints[index]["current_nonzero"] for index in range(1, len(checkpoints)))
    checkpoint_exits = sum(checkpoints[index - 1]["current_nonzero"] and not checkpoints[index]["current_nonzero"] for index in range(1, len(checkpoints)))
    emitted_entries = _uint(summary["checkpoint_current_entries"], f"{where}:checkpoint_entries")
    emitted_exits = _uint(summary["checkpoint_current_exits"], f"{where}:checkpoint_exits")
    _require(emitted_entries in (checkpoint_entries, checkpoint_entries + 1), f"{where}:checkpoint_entry_reconciliation")
    _require(emitted_exits in (checkpoint_exits, checkpoint_exits + 1), f"{where}:checkpoint_exit_reconciliation")
    _require((emitted_entries - checkpoint_entries) + (emitted_exits - checkpoint_exits) <= 1, f"{where}:checkpoint_baseline_reconciliation")

    final_current = int(bool(last["current_nonzero"]))
    census_difference = _uint(summary["bottom_census_current_entries"], f"{where}:bottom_entries") - _uint(summary["bottom_census_current_exits"], f"{where}:bottom_exits")
    _require(census_difference in (final_current, final_current - 1), f"{where}:bottom_current_path_identity")
    _require(_uint(summary["bottom_census_current_entries"], f"{where}:bottom_entries") <= _uint(summary["measured_target_current_entries"], f"{where}:target_entries"), f"{where}:bottom_entries_exceed_target_entries")
    _require(_uint(summary["bottom_census_current_exits"], f"{where}:bottom_exits") <= _uint(summary["measured_target_current_exits"], f"{where}:target_exits"), f"{where}:bottom_exits_exceed_target_exits")
    _require(_uint(summary["nonzero_current_bottom_censuses"], f"{where}:nonzero_censuses") <= post, f"{where}:current_census_bound")
    _require(_uint(summary["max_current_excursion_bottom_attempts"], f"{where}:max_excursion") <= post, f"{where}:excursion_bound")
    _require(_uint(summary["max_zero_wait_bottom_attempts"], f"{where}:max_zero_wait") <= post, f"{where}:zero_wait_bound")

    measured_family = _family_counts(summary["measured_family_attempts"], f"{where}:measured_family_attempts")
    total_family = _family_counts(summary["total_family_attempts"], f"{where}:total_family_attempts")
    measured_transitions = _uint(summary["measured_transitions"], f"{where}:measured_transitions")
    total_transitions = _uint(summary["total_transitions"], f"{where}:total_transitions")
    measurement_start = _uint(summary["measurement_start_transition"], f"{where}:measurement_start_transition")
    _literal(measured_transitions, sum(measured_family.values()), f"{where}:measured_family_sum")
    _literal(total_transitions, sum(total_family.values()), f"{where}:total_family_sum")
    _literal(total_transitions, measurement_start + measured_transitions, f"{where}:transition_partition")
    _require(total_transitions <= expected.transition_cap and int(last["transition"]) <= total_transitions, f"{where}:transition_cap_or_checkpoint")
    for family in FAMILY_NAMES:
        _require(measured_family[family] <= total_family[family], f"{where}:family_partition:{family}")

    measured_attempts = _uint_vector(summary, "measured_swap_attempts", S, where)
    total_attempts = _uint_vector(summary, "total_swap_attempts", S, where)
    measured_accepts = _uint_vector(summary, "measured_swap_accepts", S, where)
    total_accepts = _uint_vector(summary, "total_swap_accepts", S, where)
    _literal(measured_attempts[0], post, f"{where}:measured_bottom_attempts")
    _literal(total_attempts[0], expected.warm_bottom + post, f"{where}:total_bottom_attempts")
    _literal(sum(measured_attempts), measured_family["swap"], f"{where}:measured_swap_sum")
    _literal(sum(total_attempts), total_family["swap"], f"{where}:total_swap_sum")
    for edge in range(S):
        _require(measured_accepts[edge] <= measured_attempts[edge], f"{where}:measured_swap_accept[{edge}]")
        _require(total_accepts[edge] <= total_attempts[edge], f"{where}:total_swap_accept[{edge}]")
    for key in ("measured_current_swap_down", "measured_current_swap_up", "measured_homology_swap_down", "measured_homology_swap_up"):
        flux = _uint_vector(summary, key, S, where)
        _require(all(value <= measured_accepts[edge] for edge, value in enumerate(flux)), f"{where}:{key}_exceeds_accepts")

    measured_legacy = sum(_uint(summary[key], f"{where}:{key}") for key in (
        "measured_legacy_accepts",
        "measured_legacy_firewall_rejects",
        "measured_legacy_metropolis_rejects",
    ))
    total_legacy = sum(_uint(summary[key], f"{where}:{key}") for key in (
        "total_legacy_accepts",
        "total_legacy_firewall_rejects",
        "total_legacy_metropolis_rejects",
    ))
    _literal(measured_legacy, measured_family["legacy"], f"{where}:measured_legacy_partition")
    _literal(total_legacy, total_family["legacy"], f"{where}:total_legacy_partition")

    measured_births = _uint_vector(summary, "measured_local_current_births", S + 1, where)
    measured_deaths = _uint_vector(summary, "measured_local_current_deaths", S + 1, where)
    measured_current_moves = _uint_vector(summary, "measured_local_current_vector_moves", S + 1, where)
    measured_H2_births = _uint_vector(summary, "measured_local_homology_births", S + 1, where)
    measured_H2_deaths = _uint_vector(summary, "measured_local_homology_deaths", S + 1, where)
    measured_H2_moves = _uint_vector(summary, "measured_local_homology_moves", S + 1, where)
    total_births = _uint_vector(summary, "total_local_current_births", S + 1, where)
    total_deaths = _uint_vector(summary, "total_local_current_deaths", S + 1, where)
    total_current_moves = _uint_vector(summary, "total_local_current_vector_moves", S + 1, where)
    total_H2_births = _uint_vector(summary, "total_local_homology_births", S + 1, where)
    total_H2_deaths = _uint_vector(summary, "total_local_homology_deaths", S + 1, where)
    total_H2_moves = _uint_vector(summary, "total_local_homology_moves", S + 1, where)
    for level in range(S + 1):
        _require(measured_births[level] + measured_deaths[level] <= measured_current_moves[level], f"{where}:measured_current_local_partition[{level}]")
        _require(measured_H2_births[level] + measured_H2_deaths[level] <= measured_H2_moves[level], f"{where}:measured_H2_local_partition[{level}]")
        _require(total_births[level] + total_deaths[level] <= total_current_moves[level], f"{where}:total_current_local_partition[{level}]")
        _require(total_H2_births[level] + total_H2_deaths[level] <= total_H2_moves[level], f"{where}:total_H2_local_partition[{level}]")
    _literal(summary["measured_target_local_current_births"], measured_births[0], f"{where}:target_local_birth")
    _literal(summary["measured_target_current_entries"], measured_births[0] + _uint(summary["measured_target_current_imports"], f"{where}:imports"), f"{where}:target_entry_decomposition")
    _literal(summary["measured_target_current_exits"], measured_deaths[0] + _uint(summary["measured_target_current_exports"], f"{where}:exports"), f"{where}:target_exit_decomposition")
    current_down = _uint_vector(summary, "measured_current_swap_down", S, where)
    current_up = _uint_vector(summary, "measured_current_swap_up", S, where)
    _require(_uint(summary["measured_target_current_imports"], f"{where}:imports") <= current_down[0], f"{where}:imports_exceed_down_flux")
    _require(_uint(summary["measured_target_current_exports"], f"{where}:exports") <= current_up[0], f"{where}:exports_exceed_up_flux")
    _require(_uint(summary["measured_target_current_entries"], f"{where}:target_entries") <= _uint(summary["total_target_current_entries"], f"{where}:total_target_entries"), f"{where}:measured_entries_not_subset")
    _require(_uint(summary["measured_target_current_exits"], f"{where}:target_exits") <= _uint(summary["total_target_current_exits"], f"{where}:total_target_exits"), f"{where}:measured_exits_not_subset")
    _literal(summary["measured_roundtrips"], sum(_uint_vector(summary, "measured_walker_roundtrips", S + 1, where)), f"{where}:measured_roundtrip_sum")
    _literal(summary["total_roundtrips"], sum(_uint_vector(summary, "total_walker_roundtrips", S + 1, where)), f"{where}:total_roundtrip_sum")

    for measured_key, total_key in MEASURED_TOTAL_PAIRS:
        measured_value = summary[measured_key]
        total_value = summary[total_key]
        if isinstance(measured_value, list) and isinstance(total_value, list):
            _require(all(int(left) <= int(right) for left, right in zip(measured_value, total_value)), f"{where}:{measured_key}_not_subset")
        else:
            _require(int(measured_value) <= int(total_value), f"{where}:{measured_key}_not_subset")


def load_frozen_statistics(
    statistics_path: Path,
    expected_sha256: str,
    custody_hook: CustodyHook | None = None,
) -> ModuleType:
    """SHA-custody and then load the explicitly named frozen statistics file."""

    path = Path(statistics_path).resolve()
    _require(path.name == FROZEN_STATS_FILE and path.parent.name == FROZEN_STATS_PROBE, "statistics:path_not_frozen_pilot_2")
    _require(LOWER_HEX_64.fullmatch(expected_sha256) is not None, "statistics:bad_expected_sha256")
    try:
        data = path.read_bytes()
    except OSError as error:
        raise IntegrityError("statistics:cannot_read") from error
    actual = hashlib.sha256(data).hexdigest()
    _require(actual == expected_sha256, f"statistics:sha256_mismatch:{actual}")
    if custody_hook is not None:
        try:
            custody_hook(path, actual)
        except Exception as error:
            raise IntegrityError("statistics:custody_hook_failed") from error

    module_name = f"_photon_frozen_mixing_{actual}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    _require(spec is not None and spec.loader is not None, "statistics:cannot_make_import_spec")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except Exception:
        sys.modules.pop(module_name, None)
        raise
    for name in (
        "series_stats",
        "half_drift_z",
        "rank_folded_rhat",
        "bulk_tail_ess",
        "conservative_group_mean_se",
        "z_difference",
    ):
        _require(callable(getattr(module, name, None)), f"statistics:missing_{name}")
    return module


def _metric_series(chain: ParsedChain, metric: str) -> list[float]:
    L = chain.expectation.L
    n_plaq = 6 * L**4
    if metric == "support_fraction":
        return [int(item["support"]) / n_plaq for item in chain.checkpoints]
    if metric == "n_mean":
        return [int(item["n_sum"]) / n_plaq for item in chain.checkpoints]
    if metric == "h_norm":
        return [float(sum(min(int(value), 5 - int(value)) for value in item["homology"])) for item in chain.checkpoints]  # type: ignore[union-attr]
    match = re.fullmatch(r"H2_(01|02|03|12|13|23)_(cos|sin)", metric)
    if match is None:
        raise KeyError(metric)
    component = H2_NAMES.index(match.group(1))
    table = Z5_COS if match.group(2) == "cos" else Z5_SIN
    return [table[int(item["homology"][component])] for item in chain.checkpoints]  # type: ignore[index]


def _start_separation(stats: ModuleType, chains: Sequence[ParsedChain], series: Sequence[Sequence[float]]) -> float:
    groups: list[tuple[float, float]] = []
    for start in ("cold", "stratified"):
        entries = [stats.series_stats(values) for chain, values in zip(chains, series) if chain.expectation.start == start]
        if len(entries) != 2:
            _fail(f"mixing:start_group_{start}_not_two")
        groups.append(stats.conservative_group_mean_se(entries))
    return float(stats.z_difference(*groups[0], *groups[1]))


def _mixing_audit(
    stats: ModuleType,
    L: int,
    chains: Sequence[ParsedChain],
    gates: StatisticalGates,
) -> tuple[str, list[str]]:
    failures: list[str] = []
    minima_ess: list[float] = []
    rank_values: list[float] = []
    folded_values: list[float] = []
    bulk_values: list[float] = []
    tail_values: list[float] = []
    drift_values: list[float] = []
    start_values: list[float] = []
    for metric in MIXING_METRICS:
        series = [_metric_series(chain, metric) for chain in chains]
        chain_stats = [stats.series_stats(values) for values in series]
        min_ess = min(float(entry.ess) for entry in chain_stats)
        max_drift = max(float(stats.half_drift_z(values)) for values in series)
        rank_rhat, folded_rhat = (float(value) for value in stats.rank_folded_rhat(series))
        bulk_ess, tail_ess = (float(value) for value in stats.bulk_tail_ess(series))
        start_z = _start_separation(stats, chains, series)
        minima_ess.append(min_ess)
        rank_values.append(rank_rhat)
        folded_values.append(folded_rhat)
        bulk_values.append(bulk_ess)
        tail_values.append(tail_ess)
        drift_values.append(max_drift)
        start_values.append(start_z)
        if any(not math.isfinite(float(entry.variance)) or float(entry.variance) <= 0.0 for entry in chain_stats):
            failures.append(f"L{L}:MIX:{metric}:variance")
        if not math.isfinite(min_ess) or min_ess < gates.per_chain_ess_min:
            failures.append(f"L{L}:MIX:{metric}:minESS={min_ess:.12g}")
        if not math.isfinite(rank_rhat) or rank_rhat > gates.rhat_max:
            failures.append(f"L{L}:MIX:{metric}:Rhat={rank_rhat:.12g}")
        if not math.isfinite(folded_rhat) or folded_rhat > gates.rhat_max:
            failures.append(f"L{L}:MIX:{metric}:folded={folded_rhat:.12g}")
        if not math.isfinite(bulk_ess) or bulk_ess < gates.bulk_ess_min:
            failures.append(f"L{L}:MIX:{metric}:bulk={bulk_ess:.12g}")
        if not math.isfinite(tail_ess) or tail_ess < gates.tail_ess_min:
            failures.append(f"L{L}:MIX:{metric}:tail={tail_ess:.12g}")
        if not math.isfinite(max_drift) or max_drift > gates.drift_z_max:
            failures.append(f"L{L}:MIX:{metric}:drift={max_drift:.12g}")
        if not math.isfinite(start_z) or start_z > gates.start_z_max:
            failures.append(f"L{L}:MIX:{metric}:starts={start_z:.12g}")
    line = (
        f"L{L} MIX {'PASS' if not failures else 'FAIL'} metrics={len(MIXING_METRICS)} "
        f"minESS={min(minima_ess):.6g} maxRhat={max(rank_values):.6g} "
        f"maxFolded={max(folded_values):.6g} minBulk={min(bulk_values):.6g} "
        f"minTail={min(tail_values):.6g} maxDrift={max(drift_values):.6g} "
        f"maxStarts={max(start_values):.6g}"
    )
    return line, failures


def _band_sums(values: Sequence[int], S: int) -> tuple[int, int, int, int]:
    result = [0, 0, 0, 0]
    for level, value in enumerate(values):
        result[min(3, 4 * level // (S + 1))] += int(value)
    return tuple(result)  # type: ignore[return-value]


def _checkpoint_uniqueness(checkpoints: Sequence[Mapping[str, object]]) -> tuple[float, tuple[float, ...]]:
    all_fraction = len({item["state_sha256"] for item in checkpoints}) / len(checkpoints)
    sizes = _quartile_sizes(len(checkpoints))
    fractions: list[float] = []
    cursor = 0
    for size in sizes:
        group = checkpoints[cursor : cursor + size]
        fractions.append(len({item["state_sha256"] for item in group}) / size)
        cursor += size
    return all_fraction, tuple(fractions)


def _mobility_audit(chain: ParsedChain) -> tuple[str, list[str]]:
    expected = chain.expectation
    summary = chain.summary
    L = expected.L
    S = max(15, L * L)
    prefix = f"L{L}:{expected.label}:MOB"
    failures: list[str] = []

    def gate(condition: bool, name: str, value: object) -> None:
        if not condition:
            failures.append(f"{prefix}:{name}={value}")

    bottom_entries = int(summary["bottom_census_current_entries"])
    bottom_exits = int(summary["bottom_census_current_exits"])
    target_entries = int(summary["measured_target_current_entries"])
    target_exits = int(summary["measured_target_current_exits"])
    current_censuses = int(summary["nonzero_current_bottom_censuses"])
    current_hashes = int(summary["distinct_nonzero_current_hashes"])
    current_walkers = int(summary["distinct_nonzero_current_walkers"])
    imports = int(summary["measured_target_current_imports"])
    exports = int(summary["measured_target_current_exports"])
    gate(bottom_entries >= 8, "bottom_entries", bottom_entries)
    gate(bottom_exits >= 8, "bottom_exits", bottom_exits)
    gate(target_entries >= 8, "target_entries", target_entries)
    gate(target_exits >= 8, "target_exits", target_exits)
    gate(current_censuses >= 16, "current_censuses", current_censuses)
    gate(current_hashes >= 8, "current_hashes", current_hashes)
    gate(current_walkers >= 4, "current_walkers", current_walkers)
    gate(imports >= 4, "imports", imports)
    gate(exports >= 4, "exports", exports)
    for key in ("quartile_current_entries", "quartile_current_exits", "quartile_nonzero_current_censuses"):
        values = [int(value) for value in summary[key]]  # type: ignore[union-attr]
        gate(all(value >= 1 for value in values), key, values)
    zero_wait = int(summary["max_zero_wait_bottom_attempts"])
    excursion = int(summary["max_current_excursion_bottom_attempts"])
    gate(zero_wait <= 65536, "max_zero_wait", zero_wait)
    gate(excursion <= 65536, "max_excursion", excursion)

    current_up = [int(value) for value in summary["measured_current_swap_up"]]  # type: ignore[union-attr]
    current_down = [int(value) for value in summary["measured_current_swap_down"]]  # type: ignore[union-attr]
    gate(min(current_up) >= 4, "min_edge_current_up", min(current_up))
    gate(min(current_down) >= 4, "min_edge_current_down", min(current_down))

    current_births = [int(value) for value in summary["measured_local_current_births"]]  # type: ignore[union-attr]
    current_deaths = [int(value) for value in summary["measured_local_current_deaths"]]  # type: ignore[union-attr]
    current_moves = [int(value) for value in summary["measured_local_current_vector_moves"]]  # type: ignore[union-attr]
    birth_bands = _band_sums(current_births, S)
    death_bands = _band_sums(current_deaths, S)
    current_move_bands = _band_sums(current_moves, S)
    gate(min(birth_bands) >= 2, "min_band_current_births", min(birth_bands))
    gate(min(death_bands) >= 2, "min_band_current_deaths", min(death_bands))
    gate(min(current_move_bands) >= 8, "min_band_current_moves", min(current_move_bands))
    gate(current_births[S] >= 2, "top_current_births", current_births[S])
    gate(current_deaths[S] >= 2, "top_current_deaths", current_deaths[S])

    homology_values = summary["homology_visited_values"]
    quartile_homology_values = summary["quartile_H2_visited_values"]
    homology_changes = [int(value) for value in summary["homology_component_changes"]]  # type: ignore[union-attr]
    quartile_changes = [[int(value) for value in row] for row in summary["quartile_H2_component_changes"]]  # type: ignore[union-attr]
    gate(all(list(values) == [0, 1, 2, 3, 4] for values in homology_values), "H2_all_values", homology_values)
    gate(all(list(values) == [0, 1, 2, 3, 4] for quartile in quartile_homology_values for values in quartile), "H2_quartile_all_values", "incomplete")
    gate(min(homology_changes) >= 512, "min_H2_changes", min(homology_changes))
    gate(min(value for row in quartile_changes for value in row) >= 64, "min_quartile_H2_changes", min(value for row in quartile_changes for value in row))
    H2_vectors = int(summary["distinct_H2_vectors"])
    quartile_H2_vectors = [int(value) for value in summary["quartile_H2_vector_counts"]]  # type: ignore[union-attr]
    gate(H2_vectors >= 512, "H2_vectors", H2_vectors)
    gate(min(quartile_H2_vectors) >= 128, "min_quartile_H2_vectors", min(quartile_H2_vectors))

    H2_up = [int(value) for value in summary["measured_homology_swap_up"]]  # type: ignore[union-attr]
    H2_down = [int(value) for value in summary["measured_homology_swap_down"]]  # type: ignore[union-attr]
    gate(min(H2_up) >= 64, "min_edge_H2_up", min(H2_up))
    gate(min(H2_down) >= 64, "min_edge_H2_down", min(H2_down))
    H2_moves = [int(value) for value in summary["measured_local_homology_moves"]]  # type: ignore[union-attr]
    H2_move_bands = _band_sums(H2_moves, S)
    gate(min(H2_move_bands) >= 32, "min_band_H2_moves", min(H2_move_bands))
    gate(H2_moves[S] >= 32, "top_H2_moves", H2_moves[S])

    swap_attempts = [int(value) for value in summary["measured_swap_attempts"]]  # type: ignore[union-attr]
    swap_accepts = [int(value) for value in summary["measured_swap_accepts"]]  # type: ignore[union-attr]
    swap_rates = [accepted / attempted if attempted else 0.0 for accepted, attempted in zip(swap_accepts, swap_attempts)]
    gate(min(swap_rates) >= 0.70, "min_swap_rate", f"{min(swap_rates):.12g}")
    bottom_attempts = swap_attempts[0]
    attempt_ratios = [attempted / bottom_attempts for attempted in swap_attempts]
    gate(min(attempt_ratios) >= 0.95 and max(attempt_ratios) <= 1.05, "edge_attempt_ratio", f"{min(attempt_ratios):.6g}/{max(attempt_ratios):.6g}")
    roundtrips = int(summary["measured_roundtrips"])
    walker_roundtrips = [int(value) for value in summary["measured_walker_roundtrips"]]  # type: ignore[union-attr]
    walkers_with_trip = sum(value > 0 for value in walker_roundtrips)
    required_walkers = math.ceil(0.75 * (S + 1))
    gate(roundtrips >= 64, "roundtrips", roundtrips)
    gate(walkers_with_trip >= required_walkers, "walkers_with_trip", f"{walkers_with_trip}/{required_walkers}")

    unique_all, unique_quarters = _checkpoint_uniqueness(chain.checkpoints)
    gate(unique_all >= 0.75, "checkpoint_unique", f"{unique_all:.12g}")
    gate(min(unique_quarters) >= 0.50, "min_quarter_unique", f"{min(unique_quarters):.12g}")

    local_H2_births = sum(int(value) for value in summary["measured_local_homology_births"])  # type: ignore[union-attr]
    local_H2_deaths = sum(int(value) for value in summary["measured_local_homology_deaths"])  # type: ignore[union-attr]
    target_local_births = current_births[0]
    target_local_deaths = current_deaths[0]
    line = (
        f"L{L} MOB {expected.label} {'PASS' if not failures else 'FAIL'} "
        f"current={bottom_entries}/{bottom_exits} target={target_entries}/{target_exits} "
        f"census={current_censuses} hashes={current_hashes} walkers={current_walkers} "
        f"io={imports}/{exports} localJ0={target_local_births}/{target_local_deaths} "
        f"edgeJ={min(current_up)}/{min(current_down)} "
        f"H2={H2_vectors}/{min(homology_changes)} edgeH2={min(H2_up)}/{min(H2_down)} "
        f"localH2bd={local_H2_births}/{local_H2_deaths} swap={min(swap_rates):.6g} "
        f"trips={roundtrips}/{walkers_with_trip} unique={unique_all:.6g}/{min(unique_quarters):.6g}"
    )
    return line, failures


def _validate_surface(expectations: Sequence[RunExpectation], logs: Mapping[str, LogSource]) -> tuple[RunExpectation, ...]:
    _require(len(expectations) > 0, "surface:no_expectations")
    labels = [entry.label for entry in expectations]
    _require(len(labels) == len(set(labels)), "surface:duplicate_labels")
    _require(set(logs) == set(labels), f"surface:log_labels expected={sorted(labels)!r} actual={sorted(logs)!r}")
    ordered = tuple(sorted(expectations, key=lambda entry: (entry.L, entry.start, entry.label)))
    _require(len({entry.seed for entry in ordered}) == len(ordered), "surface:duplicate_seeds")
    L_values = sorted({entry.L for entry in ordered})
    _require(L_values == [3, 4], "surface:requires_exactly_L3_and_L4")
    for L in L_values:
        group = [entry for entry in ordered if entry.L == L]
        _require(len(group) == 4, f"surface:L{L}:requires_four_chains")
        _require(sum(entry.start == "cold" for entry in group) == 2, f"surface:L{L}:requires_two_cold")
        _require(sum(entry.start == "stratified" for entry in group) == 2, f"surface:L{L}:requires_two_stratified")
        schedule = {
            (entry.bitstream_domain, entry.development_only, entry.warm_bottom, entry.checkpoints, entry.thin, entry.validation_stride, entry.transition_cap)
            for entry in group
        }
        _require(len(schedule) == 1, f"surface:L{L}:schedule_not_common")
    complete_schedule = {
        (
            entry.bitstream_domain,
            entry.development_only,
            entry.warm_bottom,
            entry.checkpoints,
            entry.thin,
            entry.validation_stride,
            entry.transition_cap,
        )
        for entry in ordered
    }
    _require(len(complete_schedule) == 1, "surface:L3_L4_schedule_not_common")
    return ordered


def _scale_audit(chains: Sequence[ParsedChain]) -> tuple[str, list[str]]:
    """Conservative L3-to-L4 anti-collapse gate on equal census budgets.

    The integer comparisons avoid a platform-dependent statistical decision.
    L4 must retain at least one quarter of the worst L3 current-event and
    round-trip counts and at least one half of the worst L3 per-component H2
    change count.  These are feasibility bounds, not extrapolations to L>4.
    """

    groups = {
        L: [chain for chain in chains if chain.expectation.L == L]
        for L in (3, 4)
    }

    def current_events(chain: ParsedChain) -> int:
        return int(chain.summary["bottom_census_current_entries"]) + int(
            chain.summary["bottom_census_current_exits"]
        )

    def h2_changes(chain: ParsedChain) -> int:
        return min(int(value) for value in chain.summary["homology_component_changes"])  # type: ignore[union-attr]

    def roundtrips(chain: ParsedChain) -> int:
        return int(chain.summary["measured_roundtrips"])

    current_L3 = max(current_events(chain) for chain in groups[3])
    current_L4 = min(current_events(chain) for chain in groups[4])
    h2_L3 = max(h2_changes(chain) for chain in groups[3])
    h2_L4 = min(h2_changes(chain) for chain in groups[4])
    trips_L3 = max(roundtrips(chain) for chain in groups[3])
    trips_L4 = min(roundtrips(chain) for chain in groups[4])

    failures: list[str] = []
    if 4 * current_L4 < current_L3:
        failures.append(f"SCALE:current={current_L4}/{current_L3}")
    if 2 * h2_L4 < h2_L3:
        failures.append(f"SCALE:H2={h2_L4}/{h2_L3}")
    if 4 * trips_L4 < trips_L3:
        failures.append(f"SCALE:roundtrips={trips_L4}/{trips_L3}")
    line = (
        f"SCALE {'PASS' if not failures else 'FAIL'} "
        f"current={current_L4}/{current_L3} H2={h2_L4}/{h2_L3} "
        f"roundtrips={trips_L4}/{trips_L3}"
    )
    return line, failures


def analyze_logs(
    logs: Mapping[str, LogSource],
    expectations: Sequence[RunExpectation],
    *,
    statistics_path: Path,
    statistics_sha256: str,
    custody_hook: CustodyHook | None = None,
    statistical_gates: StatisticalGates = StatisticalGates(),
) -> AnalysisResult:
    """Parse and analyze exactly four chains for every supplied L.

    The function performs no subprocess, engine, network, or output-file
    action.  All qualification data and schedule identity are caller-owned.
    """

    try:
        _validate_statistical_gates(statistical_gates)
        ordered = _validate_surface(expectations, logs)
        chains = [parse_chain(logs[entry.label], entry) for entry in ordered]
        stats = load_frozen_statistics(Path(statistics_path), statistics_sha256, custody_hook)
    except (IntegrityError, OSError, ImportError) as error:
        failure = f"INTEGRITY:{error}"
        return AnalysisResult(("INTEGRITY FAIL",), (failure,))

    lines: list[str] = []
    failures: list[str] = []
    for L in sorted({chain.expectation.L for chain in chains}):
        group = [chain for chain in chains if chain.expectation.L == L]
        for chain in group:
            line, chain_failures = _mobility_audit(chain)
            lines.append(line)
            failures.extend(chain_failures)
        line, mixing_failures = _mixing_audit(stats, L, group, statistical_gates)
        lines.append(line)
        failures.extend(mixing_failures)
    scale_line, scale_failures = _scale_audit(chains)
    lines.append(scale_line)
    failures.extend(scale_failures)
    lines.append(f"ANALYSIS {'PASS' if not failures else 'FAIL'} failures={len(failures)}")
    return AnalysisResult(tuple(lines), tuple(failures))
