#!/usr/bin/env python3
"""Lazy, fail-closed analysis for P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2.

All 2048 dual checkpoints enter the registered mobility, mixing and Ward
statistics.  Numerical Ward centres and residuals are withheld until every
exact reader check, mobility gate, mixing gate and prospective precision gate
has passed.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext, ROUND_HALF_EVEN
import hashlib
import importlib.util
import math
from pathlib import Path
import re
import statistics
import sys
from types import ModuleType
from typing import Callable, Mapping, Sequence

import state_reader as reader


PROBE = "P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-2"
FAMILIES = reader.FAMILY_NAMES
PRIMAL_SAMPLES = 512
PRIMAL_BLOCK = 32
DUAL_SAMPLES = 2048
DUAL_BLOCK = 128
DECIMAL_PRECISION = 80
CONTACT_PRECISION_LIMIT = 0.03
OFFCONTACT_PRECISION_LIMIT = 0.02
STANDARD_ERROR_BUDGET = 4.0
DICTIONARY_SLACK = 5e-15
WARD_ESS_MIN = 64.0
WARD_PRIMAL_RHAT_MAX = 1.10
WARD_DUAL_RHAT_MAX = 1.05
WARD_BULK_ESS_MIN = 200.0
WARD_DRIFT_Z_MAX = 4.0
WARD_START_Z_MAX = 4.0
WARD_UNIQUE_MIN = 0.99
TERMINAL_VOCABULARY = frozenset(
    {
        "BREAK_DUAL_DICTIONARY",
        "STOP_DUAL_INTEGRITY",
        "STOP_DUAL_MIXING",
        "DUAL_CROSSCHECK_PASS",
    }
)

# These literals are inherited byte-for-byte from CROSSCHECK-1's binary64
# character dictionary.  The new exact-current conversion below does not use
# host trigonometric functions.
KAPPA2 = float.fromhex("0x1.0e44323405ac0p-1")
INV_KAPPA2 = float.fromhex("0x1.e4f92e2dff6f0p+0")
X2_LARGE = float.fromhex("0x1.2f1bbcdcbfa54p+3")

STATS_SHA256 = "d3d2ffba5ade37863f8e34a9b6c8198cf3e222aa8f12a6ba78b621d5c5bef4ce"
QUALIFICATION_SHA256 = "e19617765e0605be1b6ffdd22035ebb8a243ce9b51136978d44e0b0c2a999c93"

PILOT_HASHES = {
    "L6_cold_r1.log": "ce741456b8e5cc9e73c4ae2aeaf174a110f28e450285a79ce8b6e1c82c1d958f",
    "L6_cold_r2.log": "86a17a86a23b41a118bfa8418cacc8b7c0a23e7c95fda5a32fe547c4737d84fd",
    "L6_hot_r1.log": "225b09fb6906d7a314eb03f2d2d72220df795b8463add3375accf2b049b1d4e4",
    "L6_hot_r2.log": "2b28e29538187c3a5065447b805c1337c166ea24107d885f4666468fdb0ba88e",
    "L8_cold_r1.log": "f80740acaf14bdaabe0ae2af099b22a75bbe6e49423b78651d2800a9ad3682b2",
    "L8_cold_r2.log": "85c8a88f1b87149c5e1aa31994a5be4581b516059061425966481ece08eab853",
    "L8_hot_r1.log": "f0e865a029abbb618fecaaac4a9357cad56027fc261d434278e9fcc048fe1f32",
    "L8_hot_r2.log": "d7037f179e5e8b42c1e467c386a36fc9c41125d3cf0d62ce4db29d8e3dd644ed",
}

PRIMAL_SPECS = {
    "primal_L6_cold_r1.log": (6, "cold", 1, 0xE755060000000101, 512, 4),
    "primal_L6_hot_r1.log": (6, "hot", 1, 0xE755060000000201, 512, 4),
    "primal_L8_cold_r1.log": (8, "cold", 1, 0xE755080000000101, 1024, 8),
    "primal_L8_hot_r1.log": (8, "hot", 1, 0xE755080000000201, 1024, 8),
}


@dataclass(frozen=True)
class DualSpec:
    name: str
    L: int
    start: str
    replica: int
    seed: str
    warm_bottom: int
    thin: int
    validation_stride: int
    transition_cap: int


DUAL_SPECS = (
    DualSpec("dual_L6_cold_r1.jsonl", 6, "cold", 1, "0xbc2def7bcee975913c3b3b3999e83ad3", 98304, 1536, 1536, 1073741824),
    DualSpec("dual_L6_cold_r2.jsonl", 6, "cold", 2, "0x1a7ab1ad0011b62c04dcf48da9be3403", 98304, 1536, 1536, 1073741824),
    DualSpec("dual_L6_stratified_r1.jsonl", 6, "stratified", 1, "0x5f0f36673dd145755b9a49e703aef3d6", 98304, 1536, 1536, 1073741824),
    DualSpec("dual_L6_stratified_r2.jsonl", 6, "stratified", 2, "0x2b19daecb5c523f30bee3be7c047eb40", 98304, 1536, 1536, 1073741824),
    DualSpec("dual_L8_cold_r1.jsonl", 8, "cold", 1, "0x46ba01f80aec780ff9cc8b7e876c700c", 262144, 4096, 4096, 4294967296),
    DualSpec("dual_L8_cold_r2.jsonl", 8, "cold", 2, "0x2e0ccaa683e5f39f1237f05193b299c4", 262144, 4096, 4096, 4294967296),
    DualSpec("dual_L8_stratified_r1.jsonl", 8, "stratified", 1, "0xf8f631709b4b9ce34f8a658bef3e1d0a", 262144, 4096, 4096, 4294967296),
    DualSpec("dual_L8_stratified_r2.jsonl", 8, "stratified", 2, "0xfcd563ecc8bf8179b96c20db2c388307", 262144, 4096, 4096, 4294967296),
)

READER_STAT_FIELDS = frozenset(
    {
        "j_nonzero_by_direction",
        "j_sum",
        "j_sum_by_direction",
        "j2_sum_by_direction",
        "n_sum_by_orientation",
        "n2_sum",
        "n2_sum_by_orientation",
        "pair_sums",
        "sj2_longitudinal",
        "sj2_trace",
    }
)
READER_RUN_FIELDS = (reader.RUN_FIELDS | {"reader_schema", "state_audit_stride"})
READER_CHECKPOINT_FIELDS = (
    (reader.CHECKPOINT_FIELDS - {"state_2bit_base64"}) | READER_STAT_FIELDS
)
READER_SUMMARY_FIELDS = frozenset(
    {
        "packed_frame_bytes",
        "packed_frames",
        "packed_stream_sha256",
        "reader_schema",
        "state_audit_frames",
    }
)
SUMMARY_SHADOW_FIELDS = {
    "distinct_nonzero_current_hashes": "distinct_checkpoint_nonzero_current_hashes",
    "nonzero_current_hashes": "checkpoint_nonzero_current_hashes",
    "state_hashes": "checkpoint_state_hashes",
}
LOWER_SHA256 = re.compile(r"[0-9a-f]{64}\Z")


class IntegrityFailure(RuntimeError):
    pass


@dataclass(frozen=True)
class Chain:
    name: str
    L: int
    start: str
    replica: int
    samples: tuple[Mapping[str, object], ...]


@dataclass(frozen=True)
class DualParse:
    chain: Chain
    qualification_chain: object
    audit_frames: int


@dataclass(frozen=True)
class MarginalIdentity:
    L: int
    name: str
    left: tuple[float, float]
    right: tuple[float, float]
    precision_limit: float


def _fail(reason: str) -> None:
    raise IntegrityFailure(reason)


def _require(condition: bool, reason: str) -> None:
    if not condition:
        _fail(reason)


def _exact_fields(record: Mapping[str, object], expected: frozenset[str], where: str) -> None:
    actual = frozenset(record)
    _require(
        actual == expected,
        f"{where}:schema:missing={sorted(expected - actual)!r}:extra={sorted(actual - expected)!r}",
    )


def _int(value: object, where: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        _fail(f"{where}:not_integer")
    return value


def _uint(value: object, where: str) -> int:
    result = _int(value, where)
    _require(0 <= result <= (1 << 64) - 1, f"{where}:not_uint64")
    return result


def _signed(value: object, where: str) -> int:
    result = _int(value, where)
    _require(-(1 << 63) <= result < (1 << 63), f"{where}:not_int64")
    return result


def _integer_vector(value: object, length: int, where: str, *, signed: bool = False) -> tuple[int, ...]:
    _require(isinstance(value, list) and len(value) == length, f"{where}:shape")
    parser = _signed if signed else _uint
    return tuple(parser(entry, f"{where}[{index}]") for index, entry in enumerate(value))


def _exact_pairs(value: object, length: int, where: str) -> tuple[tuple[int, int], ...]:
    _require(isinstance(value, list) and len(value) == length, f"{where}:shape")
    result: list[tuple[int, int]] = []
    for index, pair in enumerate(value):
        _require(isinstance(pair, list) and len(pair) == 2, f"{where}[{index}]:pair_shape")
        result.append((_signed(pair[0], f"{where}[{index}][0]"), _signed(pair[1], f"{where}[{index}][1]")))
    return tuple(result)


def _lower_hash(value: object, where: str, *, allow_empty: bool = False) -> str:
    _require(isinstance(value, str), f"{where}:not_string")
    if allow_empty and value == "":
        return value
    _require(LOWER_SHA256.fullmatch(value) is not None, f"{where}:not_lower_sha256")
    return value


def finite(value: object, where: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        _fail(f"{where}:not_numeric")
    result = float(value)
    _require(math.isfinite(result), f"{where}:nonfinite")
    return result


def require_ascii_lf(path: Path, *, maximum: int | None = None) -> tuple[bytes, list[str]]:
    try:
        raw = path.read_bytes()
    except OSError as error:
        raise IntegrityFailure(f"missing_{path.name}") from error
    if maximum is not None:
        _require(len(raw) <= maximum, f"file_cap_{path.name}")
    _require(raw.endswith(b"\n") and b"\r" not in raw, f"newlines_{path.name}")
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError as error:
        raise IntegrityFailure(f"nonascii_{path.name}") from error
    return raw, text.splitlines()


def key_value_fields(line: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for token in line.split()[1:]:
        _require("=" in token, "malformed_key_value_record")
        key, value = token.split("=", 1)
        _require(bool(key) and key not in result, "duplicate_key_value_field")
        result[key] = value
    return result


def load_hashed_module(path: Path, expected_hash: str, module_name: str) -> ModuleType:
    try:
        raw = path.read_bytes()
    except OSError as error:
        raise IntegrityFailure(f"dependency_missing_{path.name}") from error
    actual = hashlib.sha256(raw).hexdigest()
    _require(actual == expected_hash, f"dependency_hash_{path.name}_{actual}")
    spec = importlib.util.spec_from_file_location(f"{module_name}_{actual}", path)
    _require(spec is not None and spec.loader is not None, f"dependency_spec_{path.name}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def parse_pilot_inputs(base: Path) -> dict[str, tuple[dict[str, str], ...]]:
    pilot_base = base.parent / "P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2"
    result: dict[str, tuple[dict[str, str], ...]] = {}
    for name, expected_hash in PILOT_HASHES.items():
        raw, lines = require_ascii_lf(pilot_base / name)
        _require(hashlib.sha256(raw).hexdigest() == expected_hash, f"pilot_hash_{name}")
        sample_lines = [line for line in lines if line.startswith("SAMPLE ")]
        _require(len(sample_lines) == PRIMAL_SAMPLES, f"pilot_samples_{name}")
        parsed = tuple(key_value_fields(line) for line in sample_lines)
        L = int(name[1])
        for index, item in enumerate(parsed):
            _require(item.get("index") == str(index), f"pilot_index_{name}_{index}")
            total = sum(int(item[f"flux_count_{value}"]) for value in range(5))
            _require(total == 6 * L**4, f"pilot_flux_census_{name}_{index}")
        result[name] = parsed
    return result


def pilot_x2_series(samples: Sequence[Mapping[str, str]], L: int) -> list[float]:
    total = 6 * L**4
    return [
        (
            (int(item["flux_count_1"]) + int(item["flux_count_4"])) * KAPPA2
            + (int(item["flux_count_2"]) + int(item["flux_count_3"])) * X2_LARGE
        )
        / total
        for item in samples
    ]


def parse_primal(base: Path, pilot: Mapping[str, tuple[dict[str, str], ...]]) -> list[Chain]:
    chains: list[Chain] = []
    for name, (L, start, replica, seed, thermal, between) in PRIMAL_SPECS.items():
        _, lines = require_ascii_lf(base / name)
        _require(len(lines) == PRIMAL_SAMPLES + 2 and lines[0].startswith("RUN "), f"primal_layout_{name}")
        header = key_value_fields(lines[0])
        expected_header = {
            "L": str(L),
            "seed": f"0x{seed:016x}",
            "start": start,
            "thermal_cycles": str(thermal),
            "measurements": str(PRIMAL_SAMPLES),
            "between_cycles": str(between),
        }
        for key, expected in expected_header.items():
            _require(header.get(key) == expected, f"primal_header_{name}_{key}")
        _require(lines[-1].startswith("SUMMARY ") and key_value_fields(lines[-1]).get("status") == "PASS", f"primal_summary_{name}")
        public = pilot[f"L{L}_{start}_r{replica}.log"]
        samples: list[Mapping[str, object]] = []
        for index, line in enumerate(lines[1:-1]):
            _require(line.startswith("SAMPLE "), f"primal_record_{name}_{index}")
            item = key_value_fields(line)
            _require(item.get("index") == str(index), f"primal_index_{name}_{index}")
            for key in ("state_hash", "cache_hash", *(f"flux_count_{value}" for value in range(5))):
                _require(item.get(key) == public[index].get(key), f"primal_public_replay_{name}_{index}_{key}")
            record: dict[str, object] = {"state_hash": item["state_hash"]}
            for key in (
                "g_mean",
                "g2_mean",
                "x2_mean",
                *(f"pair_{family}" for family in FAMILIES),
                *(f"rho_power_{axis}" for axis in range(4)),
            ):
                record[key] = finite(float(item[key]), f"primal_{name}_{index}_{key}")
            expected_x2 = pilot_x2_series((public[index],), L)[0]
            _require(abs(float(record["x2_mean"]) - expected_x2) <= 1e-14, f"primal_x2_{name}_{index}")
            record["rho_power_mean"] = math.fsum(float(record[f"rho_power_{axis}"]) for axis in range(4)) / 4.0
            samples.append(record)
        chains.append(Chain(name, L, start, replica, tuple(samples)))
    return chains


def _exact_power_float(pair: tuple[int, int], L: int) -> float:
    if L == 6:
        _require(pair[1] == 0, "L6_lowest_mode_sqrt2_component")
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        context.rounding = ROUND_HALF_EVEN
        value = Decimal(pair[0])
        if pair[1]:
            value += Decimal(pair[1]) * Decimal(2).sqrt(context=context)
        value /= Decimal(2 * L**4)
    result = float(value)
    _require(math.isfinite(result) and result >= -1e-15, "lowest_mode_nonfinite_or_negative")
    return max(0.0, result)


def _validate_sufficient_checkpoint(item: Mapping[str, object], L: int, index: int) -> dict[str, object]:
    where = f"L{L}:checkpoint[{index}]"
    audit = index % reader.STATE_AUDIT_STRIDE == 0
    expected_fields = READER_CHECKPOINT_FIELDS | ({"state_b64"} if audit else set())
    _exact_fields(item, frozenset(expected_fields), where)
    _require(_int(item.get("checkpoint"), f"{where}:index") == index, f"{where}:order")
    _lower_hash(item.get("state_sha256"), f"{where}:state_sha256")
    _lower_hash(item.get("packed_state_sha256"), f"{where}:packed_state_sha256")
    _lower_hash(item.get("current_hash"), f"{where}:current_hash", allow_empty=True)

    volume = L**4
    n_plaq = 6 * volume
    n_links = 4 * volume
    n_sum = _signed(item.get("n_sum"), f"{where}:n_sum")
    support = _uint(item.get("support"), f"{where}:support")
    n2_sum = _uint(item.get("n2_sum"), f"{where}:n2_sum")
    n_by = _integer_vector(item.get("n_sum_by_orientation"), 6, f"{where}:n_by", signed=True)
    n2_by = _integer_vector(item.get("n2_sum_by_orientation"), 6, f"{where}:n2_by")
    _require(sum(n_by) == n_sum, f"{where}:n_orientation_sum")
    _require(sum(n2_by) == n2_sum == support, f"{where}:hard_n2_support")
    _require(support <= n_plaq and abs(n_sum) <= support and (support - n_sum) % 2 == 0, f"{where}:hard_state_moments")
    _require(all(value <= volume for value in n2_by), f"{where}:n2_orientation_bound")
    _require(all(abs(value) <= n2 for value, n2 in zip(n_by, n2_by)), f"{where}:n_orientation_bound")
    pair_sums = _integer_vector(item.get("pair_sums"), 4, f"{where}:pair_sums", signed=True)
    _require(all(abs(value) <= n_plaq for value in pair_sums), f"{where}:pair_bound")

    j_sum = _signed(item.get("j_sum"), f"{where}:j_sum")
    j_by = _integer_vector(item.get("j_sum_by_direction"), 4, f"{where}:j_by", signed=True)
    j2_sum = _uint(item.get("j2_sum"), f"{where}:j2_sum")
    j2_by = _integer_vector(item.get("j2_sum_by_direction"), 4, f"{where}:j2_by")
    j_nnz = _uint(item.get("j_nnz"), f"{where}:j_nnz")
    j_nnz_by = _integer_vector(item.get("j_nonzero_by_direction"), 4, f"{where}:j_nnz_by")
    _require(sum(j_by) == j_sum, f"{where}:j_direction_sum")
    _require(sum(j2_by) == j2_sum, f"{where}:j2_direction_sum")
    _require(sum(j_nnz_by) == j_nnz, f"{where}:j_nnz_direction_sum")
    _require(j_nnz <= j2_sum <= n_links, f"{where}:hard_current_bound")
    _require(all(value <= volume for value in j2_by) and all(value <= volume for value in j_nnz_by), f"{where}:current_direction_bound")
    _require(_uint(item.get("current_nonzero"), f"{where}:current_nonzero") == int(j_nnz != 0), f"{where}:current_nonzero")
    _require((item["current_hash"] != "") == bool(j_nnz), f"{where}:current_hash_identity")

    traces = _exact_pairs(item.get("sj2_trace"), 4, f"{where}:sj2_trace")
    longitudinal = _exact_pairs(item.get("sj2_longitudinal"), 4, f"{where}:sj2_longitudinal")
    bound = 8 * volume * volume
    _require(all(abs(a) <= bound and abs(b) <= bound for a, b in traces + longitudinal), f"{where}:lowest_mode_bound")
    if L == 6:
        _require(all(b == 0 for _, b in traces + longitudinal), f"{where}:L6_sqrt2")

    if audit:
        raw = {
            key: item[key]
            for key in reader.CHECKPOINT_FIELDS
            if key != "state_2bit_base64"
        }
        raw["state_2bit_base64"] = item["state_b64"]
        try:
            derived = reader.verify_checkpoint(L, raw)
        except reader.StateIntegrityError as error:
            raise IntegrityFailure(f"{where}:audit:{error}") from error
        exact_claims = {
            "n_sum_by_orientation": list(derived.n_sum_by_orientation),
            "n2_sum": derived.n2_sum,
            "n2_sum_by_orientation": list(derived.n2_sum_by_orientation),
            "pair_sums": [entry.total for entry in derived.pair_sums],
            "j_sum": derived.j_sum,
            "j_sum_by_direction": list(derived.j_sum_by_direction),
            "j2_sum_by_direction": list(derived.j2_sum_by_direction),
            "j_nonzero_by_direction": list(derived.j_nonzero_by_direction),
            "sj2_trace": [list(entry.trace_twice_unnormalized) for entry in derived.lowest_momenta],
            "sj2_longitudinal": [list(entry.longitudinal_twice_unnormalized) for entry in derived.lowest_momenta],
        }
        for key, expected in exact_claims.items():
            _require(item[key] == expected, f"{where}:audit_{key}")

    record: dict[str, object] = {
        "state_hash": item["state_sha256"],
        "n_mean": n_sum / n_plaq,
        "n2_mean": n2_sum / n_plaq,
        "j_mean": j_sum / n_links,
        "j2_mean": j2_sum / n_links,
        "j_nonzero_density": j_nnz / n_links,
    }
    for family, value in zip(FAMILIES, pair_sums):
        record[f"pair_{family}"] = value / n_plaq
    powers = [_exact_power_float(pair, L) for pair in traces]
    for axis, value in enumerate(powers):
        record[f"sj_power_{axis}"] = value
    record["sj_power_mean"] = math.fsum(powers) / 4.0
    return record


def parse_dual(base: Path, qualification: ModuleType, spec: DualSpec) -> DualParse:
    path = base / spec.name
    raw, lines = require_ascii_lf(path, maximum=reader.MAX_COMMITTED_STREAM_BYTES)
    _require(len(lines) == DUAL_SAMPLES + 2, f"dual_line_count_{spec.name}")
    records = [qualification._json_record(line.encode("ascii"), spec.name, index + 1) for index, line in enumerate(lines)]
    run, checkpoints, summary = records[0], records[1:-1], records[-1]
    _exact_fields(run, frozenset(READER_RUN_FIELDS), f"{spec.name}:run")
    expected_run = {
        "type": "run",
        "L": spec.L,
        "S": max(15, spec.L * spec.L),
        "bitstream_domain": "photon-z5-dual-mobility-qualification-1",
        "checkpoints": DUAL_SAMPLES,
        "development_only": False,
        "legacy_selector_probability": "1/16",
        "seed": spec.seed,
        "start": spec.start,
        "state_encoding": reader.STATE_ENCODING,
        "state_packed_bytes": reader.packed_state_size(spec.L),
        "state_unpacked_bytes": reader.state_size(spec.L),
        "thin": spec.thin,
        "transition_cap": spec.transition_cap,
        "validation_stride": spec.validation_stride,
        "warm_bottom": spec.warm_bottom,
        "reader_schema": reader.READER_SCHEMA,
        "state_audit_stride": reader.STATE_AUDIT_STRIDE,
    }
    for key, expected in expected_run.items():
        _require(type(run.get(key)) is type(expected) and run.get(key) == expected, f"{spec.name}:run:{key}")

    expectation = qualification.RunExpectation(
        label=spec.name,
        L=spec.L,
        bitstream_domain="photon-z5-dual-mobility-qualification-1",
        development_only=False,
        seed=spec.seed,
        start=spec.start,
        warm_bottom=spec.warm_bottom,
        checkpoints=DUAL_SAMPLES,
        thin=spec.thin,
        validation_stride=spec.validation_stride,
        transition_cap=spec.transition_cap,
    )
    base_checkpoints: list[Mapping[str, object]] = []
    samples: list[Mapping[str, object]] = []
    previous_transition = -1
    for index, item in enumerate(checkpoints, 1):
        samples.append(_validate_sufficient_checkpoint(item, spec.L, index))
        base_item = {key: item[key] for key in qualification.CHECKPOINT_FIELDS}
        qualification._exact_fields(base_item, qualification.CHECKPOINT_FIELDS, f"{spec.name}:checkpoint[{index}]")
        qualification._literal(base_item["type"], "checkpoint", f"{spec.name}:checkpoint[{index}]:type")
        qualification._literal(base_item["L"], spec.L, f"{spec.name}:checkpoint[{index}]:L")
        qualification._literal(base_item["checkpoint"], index, f"{spec.name}:checkpoint[{index}]:index")
        qualification._literal(base_item["post_warm_bottom_attempt"], index * spec.thin, f"{spec.name}:checkpoint[{index}]:bottom")
        qualification._homology(base_item["homology"], f"{spec.name}:checkpoint[{index}]")
        current_nonzero = qualification._uint(base_item["current_nonzero"], f"{spec.name}:checkpoint[{index}]:current")
        swap_accepted = qualification._uint(base_item["swap_accepted"], f"{spec.name}:checkpoint[{index}]:swap")
        _require(current_nonzero <= 1 and swap_accepted <= 1, f"{spec.name}:checkpoint[{index}]:binary")
        transition = qualification._uint(base_item["transition"], f"{spec.name}:checkpoint[{index}]:transition")
        _require(transition > previous_transition, f"{spec.name}:checkpoint[{index}]:transition_order")
        previous_transition = transition
        walker = qualification._uint(base_item["walker_id"], f"{spec.name}:checkpoint[{index}]:walker")
        _require(walker <= max(15, spec.L * spec.L), f"{spec.name}:checkpoint[{index}]:walker_bound")
        base_checkpoints.append(base_item)

    summary_fields = (
        (qualification.SUMMARY_FIELDS - frozenset(SUMMARY_SHADOW_FIELDS))
        | frozenset(SUMMARY_SHADOW_FIELDS.values())
        | READER_SUMMARY_FIELDS
    )
    _exact_fields(summary, frozenset(summary_fields), f"{spec.name}:summary")
    _require(summary.get("reader_schema") == reader.READER_SCHEMA, f"{spec.name}:summary:reader_schema")
    _require(_uint(summary.get("packed_frame_bytes"), f"{spec.name}:summary:frame_bytes") == reader.packed_state_size(spec.L), f"{spec.name}:summary:frame_bytes")
    _require(_uint(summary.get("packed_frames"), f"{spec.name}:summary:frames") == DUAL_SAMPLES, f"{spec.name}:summary:frames")
    _require(_uint(summary.get("state_audit_frames"), f"{spec.name}:summary:audit") == DUAL_SAMPLES // reader.STATE_AUDIT_STRIDE, f"{spec.name}:summary:audit")
    _lower_hash(summary.get("packed_stream_sha256"), f"{spec.name}:summary:stream_hash")
    base_summary = {
        key: summary[SUMMARY_SHADOW_FIELDS.get(key, key)]
        for key in qualification.SUMMARY_FIELDS
    }
    qualification._validate_summary(base_summary, expectation, tuple(base_checkpoints))
    parsed = qualification.ParsedChain(expectation, {key: run[key] for key in qualification.RUN_FIELDS}, tuple(base_checkpoints), base_summary)
    chain = Chain(spec.name, spec.L, spec.start, spec.replica, tuple(samples))
    return DualParse(chain, parsed, DUAL_SAMPLES // reader.STATE_AUDIT_STRIDE)


def chain_values(chain: Chain, metric: str) -> list[float]:
    return [finite(item[metric], f"{chain.name}:{metric}") for item in chain.samples]


def _group_separation(stats: ModuleType, chains: Sequence[Chain], series: Sequence[Sequence[float]]) -> float:
    starts = sorted({chain.start for chain in chains})
    _require(len(starts) == 2, "mixing:start_groups")
    if len(chains) == 2:
        left = stats.series_stats(series[0])
        right = stats.series_stats(series[1])
        return float(stats.z_difference(left.mean, left.mcse, right.mean, right.mcse))
    groups: list[tuple[float, float]] = []
    for start in starts:
        entries = [stats.series_stats(values) for chain, values in zip(chains, series) if chain.start == start]
        _require(len(entries) == 2, f"mixing:start_group_{start}")
        groups.append(stats.conservative_group_mean_se(entries))
    return float(stats.z_difference(*groups[0], *groups[1]))


def ward_mixing_audit(
    stats: ModuleType,
    L: int,
    ensemble: str,
    chains: Sequence[Chain],
    metrics: Sequence[str],
) -> tuple[str, list[str]]:
    dual = ensemble == "dual"
    ess_min = WARD_ESS_MIN
    rhat_max = WARD_DUAL_RHAT_MAX if dual else WARD_PRIMAL_RHAT_MAX
    bulk_min = WARD_BULK_ESS_MIN
    tail_min = None
    failures: list[str] = []
    minima: list[float] = []
    rhats: list[float] = []
    folded: list[float] = []
    bulks: list[float] = []
    tails: list[float] = []
    drifts: list[float] = []
    starts: list[float] = []
    expected_samples = DUAL_SAMPLES if dual else PRIMAL_SAMPLES
    for chain in chains:
        unique = len({str(item["state_hash"]) for item in chain.samples}) / expected_samples
        if unique < WARD_UNIQUE_MIN:
            failures.append(f"L{L}:{ensemble}:{chain.name}:unique={unique:.12g}")
    for metric in metrics:
        series = [chain_values(chain, metric) for chain in chains]
        entries = [stats.series_stats(values) for values in series]
        minimum = min(float(entry.ess) for entry in entries)
        drift = max(float(stats.half_drift_z(values)) for values in series)
        rank, fold = (float(value) for value in stats.rank_folded_rhat(series))
        bulk, tail = (float(value) for value in stats.bulk_tail_ess(series))
        separation = _group_separation(stats, chains, series)
        minima.append(minimum)
        rhats.append(rank)
        folded.append(fold)
        bulks.append(bulk)
        tails.append(tail)
        drifts.append(drift)
        starts.append(separation)
        prefix = f"L{L}:{ensemble}:{metric}"
        if any(not math.isfinite(float(entry.variance)) or float(entry.variance) <= 0.0 for entry in entries):
            failures.append(f"{prefix}:variance")
        if not math.isfinite(minimum) or minimum < ess_min:
            failures.append(f"{prefix}:minESS={minimum:.12g}")
        if not math.isfinite(rank) or rank > rhat_max:
            failures.append(f"{prefix}:Rhat={rank:.12g}")
        if not math.isfinite(fold) or fold > rhat_max:
            failures.append(f"{prefix}:folded={fold:.12g}")
        if not math.isfinite(bulk) or bulk < bulk_min:
            failures.append(f"{prefix}:bulk={bulk:.12g}")
        if tail_min is not None and (not math.isfinite(tail) or tail < tail_min):
            failures.append(f"{prefix}:tail={tail:.12g}")
        if not math.isfinite(drift) or drift > WARD_DRIFT_Z_MAX:
            failures.append(f"{prefix}:drift={drift:.12g}")
        if not math.isfinite(separation) or separation > WARD_START_Z_MAX:
            failures.append(f"{prefix}:starts={separation:.12g}")
    line = (
        f"WARD_MIXING L={L} ensemble={ensemble} {'PASS' if not failures else 'FAIL'} "
        f"metrics={len(metrics)} minESS={min(minima):.6g} maxRhat={max(rhats):.6g} "
        f"maxFolded={max(folded):.6g} minBulk={min(bulks):.6g} "
        f"minTail={min(tails):.6g} maxDrift={max(drifts):.6g} maxStarts={max(starts):.6g}"
    )
    return line, failures


def blocks(chains: Sequence[Sequence[Sequence[float]]], samples: int, block: int) -> list[list[float]]:
    result: list[list[float]] = []
    _require(samples % block == 0, "block_divisibility")
    for chain in chains:
        _require(len(chain) == samples, "block_sample_count")
        for offset in range(0, samples, block):
            chunk = chain[offset : offset + block]
            width = len(chunk[0])
            result.append([math.fsum(row[column] for row in chunk) / block for column in range(width)])
    return result


def column_mean(rows: Sequence[Sequence[float]]) -> list[float]:
    return [math.fsum(row[column] for row in rows) / len(rows) for column in range(len(rows[0]))]


def jackknife(rows: Sequence[Sequence[float]], estimator: Callable[[Sequence[float]], float]) -> tuple[float, float]:
    _require(len(rows) >= 16, "too_few_blocks")
    estimate = estimator(column_mean(rows))
    leave_one = [estimator(column_mean(rows[:index] + rows[index + 1 :])) for index in range(len(rows))]
    centre = math.fsum(leave_one) / len(leave_one)
    variance = (len(rows) - 1.0) / len(rows) * math.fsum((value - centre) ** 2 for value in leave_one)
    _require(math.isfinite(estimate) and math.isfinite(variance), "jackknife_nonfinite")
    return estimate, math.sqrt(max(0.0, variance))


def _marginal_identities(
    pilot: Mapping[str, tuple[dict[str, str], ...]],
    primal: Sequence[Chain],
    dual: Sequence[Chain],
) -> list[MarginalIdentity]:
    result: list[MarginalIdentity] = []
    for L in (6, 8):
        pchains = [chain for chain in primal if chain.L == L]
        dchains = [chain for chain in dual if chain.L == L]
        pilot_rows = [
            [[value] for value in pilot_x2_series(samples, L)]
            for name, samples in pilot.items()
            if name.startswith(f"L{L}_")
        ]
        p_contact = jackknife(blocks(pilot_rows, PRIMAL_SAMPLES, PRIMAL_BLOCK), lambda mean: mean[0])
        d_contact_rows = [[[finite(item["n2_mean"], "n2_mean")] for item in chain.samples] for chain in dchains]
        d_contact = jackknife(blocks(d_contact_rows, DUAL_SAMPLES, DUAL_BLOCK), lambda mean: 2.0 * mean[0] - 1.0)
        result.append(
            MarginalIdentity(
                L,
                "contact",
                p_contact,
                d_contact,
                CONTACT_PRECISION_LIMIT,
            )
        )
        for family in FAMILIES:
            p_rows = [
                [[finite(item["g_mean"], "g_mean"), finite(item[f"pair_{family}"], family)] for item in chain.samples]
                for chain in pchains
            ]
            d_rows = [
                [[finite(item["n_mean"], "n_mean"), finite(item[f"pair_{family}"], family)] for item in chain.samples]
                for chain in dchains
            ]
            p_cov = jackknife(blocks(p_rows, PRIMAL_SAMPLES, PRIMAL_BLOCK), lambda mean: mean[1] - mean[0] ** 2)
            d_cov = jackknife(blocks(d_rows, DUAL_SAMPLES, DUAL_BLOCK), lambda mean: INV_KAPPA2 * (mean[1] - mean[0] ** 2))
            result.append(
                MarginalIdentity(
                    L,
                    family,
                    p_cov,
                    d_cov,
                    OFFCONTACT_PRECISION_LIMIT,
                )
            )
    return result


def _screening_lines(primal: Sequence[Chain], dual: Sequence[Chain]) -> list[str]:
    lines: list[str] = []
    for L in (6, 8):
        pchains = [chain for chain in primal if chain.L == L]
        dchains = [chain for chain in dual if chain.L == L]
        p_rows = [[[finite(item["rho_power_mean"], "rho_power_mean")] for item in chain.samples] for chain in pchains]
        d_rows = [
            [[finite(item["sj_power_mean"], "sj_power_mean"), finite(item["n2_mean"], "n2_mean")] for item in chain.samples]
            for chain in dchains
        ]
        p_rho = jackknife(blocks(p_rows, PRIMAL_SAMPLES, PRIMAL_BLOCK), lambda mean: mean[0])
        d_sj = jackknife(blocks(d_rows, DUAL_SAMPLES, DUAL_BLOCK), lambda mean: 25.0 * mean[0])
        baseline = jackknife(blocks(d_rows, DUAL_SAMPLES, DUAL_BLOCK), lambda mean: 3.0 * (1.0 - mean[1]))
        with localcontext() as context:
            context.prec = DECIMAL_PRECISION
            context.rounding = ROUND_HALF_EVEN
            lambda_decimal = Decimal(1) if L == 6 else Decimal(2) - Decimal(2).sqrt(context=context)
        lambda_l = float(lambda_decimal)
        screening = (p_rho[0] + d_sj[0]) / lambda_l
        screening_se = math.hypot(p_rho[1], d_sj[1]) / lambda_l
        lines.append(
            f"SCREENING L={L} R_lowest={screening:.12g} se={screening_se:.12g} "
            f"four_se={STANDARD_ERROR_BUDGET*screening_se:.12g} contact_baseline={baseline[0]:.12g} "
            f"baseline_se={baseline[1]:.12g} decision_authority=NONE"
        )
    return lines


def analyze(base: Path) -> tuple[list[str], str]:
    repository_root = base.parent.parent
    qualification_path = base.parent / "P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1" / "qualification_analysis.py"
    stats_path = base.parent / "P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2" / "analyze_pilot.py"
    qualification = load_hashed_module(qualification_path, QUALIFICATION_SHA256, "crosscheck2_qualification")
    stats = qualification.load_frozen_statistics(stats_path, STATS_SHA256)
    qualification._validate_statistical_gates(qualification.StatisticalGates())
    pilot = parse_pilot_inputs(base)
    primal = parse_primal(base, pilot)
    parsed_dual = [parse_dual(base, qualification, spec) for spec in DUAL_SPECS]
    dual = [entry.chain for entry in parsed_dual]
    qchains = [entry.qualification_chain for entry in parsed_dual]

    lines = [
        f"PROBE {PROBE}",
        "EVIDENTIAL_SCOPE ZERO_ENGINEERING_ONLY",
        "INPUT_CUSTODY public_pilot_logs=8 primal_replays=4 dual_chains=8 status=PASS",
        f"READER_INTEGRITY frames={len(dual)*DUAL_SAMPLES} audit_frames={sum(entry.audit_frames for entry in parsed_dual)} status=PASS",
    ]
    qualification_failures: list[str] = []
    primal_metrics = (
        "g_mean",
        "x2_mean",
        *(f"pair_{family}" for family in FAMILIES),
        *(f"rho_power_{axis}" for axis in range(4)),
    )
    dual_metrics = (
        "n_mean",
        "n2_mean",
        *(f"pair_{family}" for family in FAMILIES),
        "j2_mean",
        "j_nonzero_density",
        *(f"sj_power_{axis}" for axis in range(4)),
    )
    for L in (6, 8):
        qgroup = [chain for chain in qchains if chain.expectation.L == L]
        for chain in qgroup:
            line, found = qualification._mobility_audit(chain)
            lines.append(line)
            qualification_failures.extend(found)
            checkpoint_hashes = int(chain.summary["distinct_nonzero_current_hashes"])
            checkpoint_hash_pass = checkpoint_hashes >= 32
            lines.append(
                f"CHECKPOINT_MOBILITY L={L} chain={chain.expectation.label} "
                f"distinct_nonzero_current_hashes={checkpoint_hashes} threshold=32 "
                f"status={'PASS' if checkpoint_hash_pass else 'FAIL'}"
            )
            if not checkpoint_hash_pass:
                qualification_failures.append(
                    f"L{L}:{chain.expectation.label}:MOB:distinct_checkpoint_nonzero_current_hashes={checkpoint_hashes}"
                )
        line, found = qualification._mixing_audit(stats, L, qgroup, qualification.StatisticalGates())
        lines.append(line)
        qualification_failures.extend(found)

    if qualification_failures:
        for failure in qualification_failures:
            lines.append(f"MIXING_FAILURE {failure}")
        terminal = "STOP_DUAL_MIXING"
        lines.append(f"TERMINAL {terminal}")
        lines.append("EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY")
        return lines, terminal

    ward_failures: list[str] = []
    for L in (6, 8):
        pgroup = [chain for chain in primal if chain.L == L]
        dgroup = [chain for chain in dual if chain.L == L]
        line, found = ward_mixing_audit(stats, L, "primal", pgroup, primal_metrics)
        lines.append(line)
        ward_failures.extend(found)
        line, found = ward_mixing_audit(stats, L, "dual", dgroup, dual_metrics)
        lines.append(line)
        ward_failures.extend(found)

    if ward_failures:
        for failure in ward_failures:
            lines.append(f"MIXING_FAILURE {failure}")
        terminal = "STOP_DUAL_MIXING"
        lines.append(f"TERMINAL {terminal}")
        lines.append("EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY")
        return lines, terminal

    identities = _marginal_identities(pilot, primal, dual)
    precision_failures = False
    for identity in identities:
        four_se = STANDARD_ERROR_BUDGET * math.hypot(identity.left[1], identity.right[1])
        passed = math.isfinite(four_se) and four_se <= identity.precision_limit
        precision_failures |= not passed
        lines.append(
            f"PRECISION L={identity.L} name={identity.name} four_se={four_se:.12g} "
            f"precision_limit={identity.precision_limit:.12g} status={'PASS' if passed else 'FAIL'}"
        )
    if precision_failures:
        terminal = "STOP_DUAL_MIXING"
        lines.append(f"TERMINAL {terminal}")
        lines.append("EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY")
        return lines, terminal

    dictionary_failure = False
    for identity in identities:
        residual = identity.left[0] + identity.right[0]
        se = math.hypot(identity.left[1], identity.right[1])
        passed = abs(residual) <= STANDARD_ERROR_BUDGET * se + DICTIONARY_SLACK
        dictionary_failure |= not passed
        lines.append(
            f"IDENTITY L={identity.L} name={identity.name} residual={residual:.12g} "
            f"se={se:.12g} four_se={STANDARD_ERROR_BUDGET*se:.12g} precision_limit={identity.precision_limit:.12g} "
            f"status={'PASS' if passed else 'DICTIONARY_FAIL'}"
        )
    lines.extend(_screening_lines(primal, dual))
    if dictionary_failure:
        terminal = "STOP_DUAL_INTEGRITY"
        lines.append("INTEGRITY_REASON DICTIONARY_RESIDUAL_OUTSIDE_BUDGET")
    else:
        terminal = "DUAL_CROSSCHECK_PASS"
    lines.append(f"TERMINAL {terminal}")
    lines.append("EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY")
    return lines, terminal


def main() -> int:
    if len(sys.argv) != 1:
        print("usage: python3 analyze_crosscheck2.py", file=sys.stderr)
        return 64
    base = Path(__file__).resolve().parent
    try:
        lines, _ = analyze(base)
    except (IntegrityFailure, reader.StateIntegrityError, OSError, ImportError, RuntimeError, ValueError) as error:
        reason = str(error).replace(" ", "_")
        lines = [
            f"PROBE {PROBE}",
            "EVIDENTIAL_SCOPE ZERO_ENGINEERING_ONLY",
            f"INTEGRITY_FAILURE reason={reason}",
            "TERMINAL STOP_DUAL_INTEGRITY",
            "EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY",
        ]
    sys.stdout.buffer.write(("\n".join(lines) + "\n").encode("ascii"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
