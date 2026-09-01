#!/usr/bin/env python3
"""Frozen engineering analysis for the second exact Z5 mixing pilot.

The program consumes exactly eight ASCII/LF logs, in this canonical order:

    L6_cold_r1.log, L6_cold_r2.log, L6_hot_r1.log, L6_hot_r2.log
    L8_cold_r1.log, L8_cold_r2.log, L8_hot_r1.log, L8_hot_r2.log

They are one for each member of

    L in {6, 8} x start in {cold, hot} x replica in {1, 2}.

Every log has final LF and exactly this positional layout: one ``RUN`` record,
512 consecutive ``SAMPLE`` records, one ``UPDATE_DIAGNOSTICS`` record,
``KERNEL_STATUS PASS``, and ``EVIDENTIAL_STATUS ZERO_PILOT_ONLY``.  Unknown,
extra, missing, or reordered lines are integrity failures.  ``RUN`` has
exactly the following keys:
``model``, ``L``, ``t``, ``seed``, ``start``, ``replica``,
``thermal_cycles``, ``measurements``, ``between_cycles``, and ``bit_cap``.

The mixing surface is deliberately the following *sixteen* metrics (the
expanded list is sixteen, not fourteen):

    logw
    polyakov_radius_mean
    polyakov_radius_0, polyakov_radius_1,
    polyakov_radius_2, polyakov_radius_3
    vortex_density
    monopole_density
    score_mean
    flux_asym_14, flux_asym_23
    flux_fraction_0, flux_fraction_1, flux_fraction_2,
    flux_fraction_3, flux_fraction_4

Every sample additionally carries the five integer diagnostics
``flux_count_0`` through ``flux_count_4``.  They are not mixing metrics.  The
counts must be canonical nonnegative decimals, sum exactly to ``6*L**4``, and
each printed flux fraction must agree with its count divided by that total to
within ``1e-15``.  The exact SAMPLE inventory is the index, the sixteen
metrics, the five counts, and the state/cache hashes.

The single ``UPDATE_DIAGNOSTICS`` footer has exactly eleven fields: four
canonical nonzero-line counts, the flat-cache identity, bit-cap exhaustion
and maximum-prefix fields, and the local, line, flat-sheet, and charge
decision totals.  Its totals are recomputed from the frozen schedule.

For each metric the frozen gates are:

    nonzero within-chain sample variance
    per-chain Geyer initial-monotone-sequence ESS >= 64
    rank-normalized split R-hat and folded split R-hat <= 1.05
    pooled bulk ESS >= 400 and pooled tail ESS >= 200
    hot/cold z <= 4 using autocorrelation-aware Monte Carlo standard errors
    per-chain first/second-half drift z <= 4

State-hash uniqueness must be at least 0.99.  Every chain must report a
nonzero noncontractible-line move in every direction, the flat-sheet cache
identity must pass, and the exact-prefix bit cap must never be exhausted.

This analyzer assigns engineering states only.  Its terminal precedence is

    BREAK_KERNEL
    STOP_INTEGRITY
    STOP_MIXING
    PILOT_READY_FOR_PRODUCTION_PREREG

and it never emits a phase label or phase evidence.  ``BREAK_KERNEL`` is
owned by the wrapper's independent exact contract audit: an untrusted raw-log
marker cannot select it here and is instead an integrity failure.  Every
complete modeled terminal exits zero; only a missing invocation or an
uncaught program failure exits nonzero.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import math
from pathlib import Path
import statistics
import sys
from typing import Iterable, Sequence


PILOT_ID = "P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2"
EXPECTED_MODEL = "TWIST_Z5_FACE_WEIGHT_V1"
EXPECTED_SAMPLES = 512
EXPECTED_BIT_CAP = 256
FRACTION_COUNT_TOLERANCE = 1.0e-15

LOG_NAMES = (
    "L6_cold_r1.log",
    "L6_cold_r2.log",
    "L6_hot_r1.log",
    "L6_hot_r2.log",
    "L8_cold_r1.log",
    "L8_cold_r2.log",
    "L8_hot_r1.log",
    "L8_hot_r2.log",
)

RUN_FIELDS = {
    "model",
    "L",
    "t",
    "seed",
    "start",
    "replica",
    "thermal_cycles",
    "measurements",
    "between_cycles",
    "bit_cap",
}

MIXING_METRICS = (
    "logw",
    "polyakov_radius_mean",
    "polyakov_radius_0",
    "polyakov_radius_1",
    "polyakov_radius_2",
    "polyakov_radius_3",
    "vortex_density",
    "monopole_density",
    "score_mean",
    "flux_asym_14",
    "flux_asym_23",
    "flux_fraction_0",
    "flux_fraction_1",
    "flux_fraction_2",
    "flux_fraction_3",
    "flux_fraction_4",
)

FLUX_COUNT_FIELDS = tuple(f"flux_count_{value}" for value in range(5))
SAMPLE_FIELDS = {
    "index",
    *MIXING_METRICS,
    *FLUX_COUNT_FIELDS,
    "state_hash",
    "cache_hash",
}

DIAGNOSTIC_FIELDS = {
    *(f"line_nonzero_{direction}" for direction in range(4)),
    "flat_cache_identity",
    "bit_cap_exhaustions",
    "max_prefix_bits",
    "local_decisions",
    "line_decisions",
    "flat_sheets",
    "charge_trials",
}

EXPECTED_SCHEDULE = {
    6: {"thermal_cycles": 512, "between_cycles": 4},
    8: {"thermal_cycles": 1024, "between_cycles": 8},
}

EXPECTED_SEEDS = {
    (6, "cold", 1): 0xE755060000000101,
    (6, "cold", 2): 0xE755060000000102,
    (6, "hot", 1): 0xE755060000000201,
    (6, "hot", 2): 0xE755060000000202,
    (8, "cold", 1): 0xE755080000000101,
    (8, "cold", 2): 0xE755080000000102,
    (8, "hot", 1): 0xE755080000000201,
    (8, "hot", 2): 0xE755080000000202,
}

UNIQUE_STATE_MIN = 0.99
PER_CHAIN_ESS_MIN = 64.0
RHAT_MAX = 1.05
BULK_ESS_MIN = 400.0
TAIL_ESS_MIN = 200.0
Z_MAX = 4.0


class IntegrityError(ValueError):
    """A malformed, incomplete, or non-frozen input surface."""


@dataclass(frozen=True)
class Chain:
    path: Path
    sha256: str
    meta: dict[str, str]
    samples: tuple[dict[str, str], ...]
    line_nonzero: tuple[int, int, int, int]

    @property
    def linear_size(self) -> int:
        return parse_decimal_int(self.meta["L"], "L")

    @property
    def start(self) -> str:
        return self.meta["start"]

    @property
    def replica(self) -> int:
        return parse_decimal_int(self.meta["replica"], "replica")

    @property
    def seed(self) -> int:
        return parse_seed(self.meta["seed"])


@dataclass(frozen=True)
class SeriesStats:
    mean: float
    mcse: float
    tau_int: float
    ess: float
    variance: float


def parse_fields(line: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for token in line.split()[1:]:
        if "=" not in token:
            raise IntegrityError(f"malformed field in {line.split()[0]}")
        key, value = token.split("=", 1)
        if not key or key in fields:
            raise IntegrityError(f"duplicate or empty field in {line.split()[0]}")
        fields[key] = value
    return fields


def parse_decimal_int(value: str, name: str) -> int:
    try:
        result = int(value, 10)
    except ValueError as error:
        raise IntegrityError(f"invalid integer {name}={value}") from error
    return result


def parse_canonical_uint(value: str, name: str) -> int:
    if (
        not value
        or any(character not in "0123456789" for character in value)
        or (value != "0" and value.startswith("0"))
    ):
        raise IntegrityError(f"invalid canonical unsigned integer {name}={value}")
    return int(value, 10)


def is_lower_hex(value: str, width: int) -> bool:
    return len(value) == width and all(character in "0123456789abcdef" for character in value)


def parse_seed(value: str) -> int:
    try:
        return int(value, 0)
    except ValueError as error:
        # Decimal output without a prefix is already handled by base zero.
        raise IntegrityError(f"invalid seed={value}") from error


def parse_finite(value: str, name: str) -> float:
    try:
        result = float(value)
    except ValueError as error:
        raise IntegrityError(f"invalid float {name}={value}") from error
    if not math.isfinite(result):
        raise IntegrityError(f"non-finite float {name}={value}")
    return result


def raw_kernel_break_marker(data: bytes) -> bool:
    try:
        lines = data.decode("utf-8").splitlines()
    except UnicodeDecodeError:
        return False
    markers = {
        "BREAK_KERNEL",
        "KERNEL_STATUS BREAK",
        "KERNEL_STATUS BREAK_KERNEL",
    }
    return any(line.strip() in markers for line in lines)


def validate_log_argument_names(arguments: Sequence[str]) -> None:
    actual = tuple(Path(argument).name for argument in arguments)
    if actual != LOG_NAMES:
        raise IntegrityError(
            "raw log names/order mismatch: " + ",".join(actual)
        )


def read_chain(path: Path, data: bytes) -> Chain:
    if not data or not data.endswith(b"\n") or b"\r" in data:
        raise IntegrityError(f"{path.name}: raw log is not LF with final LF")
    try:
        text = data.decode("ascii")
    except UnicodeDecodeError as error:
        raise IntegrityError(f"{path.name}: log is not ASCII") from error
    if any(byte != 10 and not 32 <= byte <= 126 for byte in data):
        raise IntegrityError(f"{path.name}: log contains nonprinting ASCII")

    lines = text.splitlines()
    expected_line_count = EXPECTED_SAMPLES + 4
    if len(lines) != expected_line_count:
        raise IntegrityError(
            f"{path.name}: expected {expected_line_count} lines, found {len(lines)}"
        )
    if any(line != line.strip() for line in lines):
        raise IntegrityError(f"{path.name}: line has leading or trailing whitespace")
    if not lines[0].startswith("RUN "):
        raise IntegrityError(f"{path.name}: line 1 is not RUN")
    meta = parse_fields(lines[0])
    if set(meta) != RUN_FIELDS:
        raise IntegrityError(f"{path.name}: RUN field inventory mismatch")

    samples: list[dict[str, str]] = []
    for index in range(EXPECTED_SAMPLES):
        line = lines[index + 1]
        if not line.startswith("SAMPLE "):
            raise IntegrityError(f"{path.name}: line {index + 2} is not SAMPLE")
        samples.append(parse_fields(line))

    diagnostics_line = lines[EXPECTED_SAMPLES + 1]
    if not diagnostics_line.startswith("UPDATE_DIAGNOSTICS "):
        raise IntegrityError(f"{path.name}: misplaced UPDATE_DIAGNOSTICS")
    diagnostics = parse_fields(diagnostics_line)
    if lines[EXPECTED_SAMPLES + 2] != "KERNEL_STATUS PASS":
        raise IntegrityError(f"{path.name}: invalid KERNEL_STATUS footer")
    if lines[EXPECTED_SAMPLES + 3] != "EVIDENTIAL_STATUS ZERO_PILOT_ONLY":
        raise IntegrityError(f"{path.name}: invalid EVIDENTIAL_STATUS footer")

    linear_size = parse_canonical_uint(meta.get("L", ""), "L")
    expected_flux_total = 6 * linear_size**4
    for index, sample in enumerate(samples):
        if set(sample) != SAMPLE_FIELDS:
            raise IntegrityError(f"{path.name}: SAMPLE {index} field inventory mismatch")
        if sample["index"] != str(index):
            raise IntegrityError(f"{path.name}: nonconsecutive SAMPLE index {index}")
        for metric in MIXING_METRICS:
            parse_finite(sample[metric], metric)
        if not is_lower_hex(sample["state_hash"], 16):
            raise IntegrityError(f"{path.name}: SAMPLE {index} has invalid state_hash")
        if not is_lower_hex(sample["cache_hash"], 16):
            raise IntegrityError(f"{path.name}: SAMPLE {index} has invalid cache_hash")
        flux_counts = [
            parse_canonical_uint(sample[field], field) for field in FLUX_COUNT_FIELDS
        ]
        if sum(flux_counts) != expected_flux_total:
            raise IntegrityError(
                f"{path.name}: SAMPLE {index} flux counts sum to {sum(flux_counts)}"
            )
        flux_fractions = [
            parse_finite(sample[f"flux_fraction_{value}"], f"flux_fraction_{value}")
            for value in range(5)
        ]
        for value, (count, fraction) in enumerate(zip(flux_counts, flux_fractions)):
            expected_fraction = count / expected_flux_total
            if abs(fraction - expected_fraction) > FRACTION_COUNT_TOLERANCE:
                raise IntegrityError(
                    f"{path.name}: SAMPLE {index} flux_fraction_{value} disagrees with count"
                )
        flux_sum = math.fsum(
            flux_fractions
        )
        if abs(flux_sum - 1.0) > 5.0 * FRACTION_COUNT_TOLERANCE:
            raise IntegrityError(
                f"{path.name}: SAMPLE {index} flux fractions sum to {flux_sum:.12g}"
            )

    if set(diagnostics) != DIAGNOSTIC_FIELDS:
        raise IntegrityError(f"{path.name}: UPDATE_DIAGNOSTICS field inventory mismatch")
    if diagnostics["flat_cache_identity"] != "PASS":
        raise IntegrityError(f"{path.name}: flat cache identity failed")
    if parse_canonical_uint(
        diagnostics["bit_cap_exhaustions"], "bit_cap_exhaustions"
    ) != 0:
        raise IntegrityError(f"{path.name}: exact-prefix bit cap was exhausted")
    max_prefix_bits = parse_canonical_uint(
        diagnostics["max_prefix_bits"], "max_prefix_bits"
    )
    if max_prefix_bits > EXPECTED_BIT_CAP:
        raise IntegrityError(f"{path.name}: maximum prefix exceeds bit cap")
    line_nonzero = tuple(
        parse_canonical_uint(
            diagnostics[f"line_nonzero_{direction}"],
            f"line_nonzero_{direction}",
        )
        for direction in range(4)
    )

    thermal_cycles = parse_canonical_uint(
        meta.get("thermal_cycles", ""), "thermal_cycles"
    )
    between_cycles = parse_canonical_uint(
        meta.get("between_cycles", ""), "between_cycles"
    )
    total_cycles = thermal_cycles + EXPECTED_SAMPLES * between_cycles
    expected_decisions = {
        "local_decisions": total_cycles * 4 * linear_size**4,
        "line_decisions": total_cycles * 4 * linear_size**3,
        "flat_sheets": total_cycles * 4,
        "charge_trials": total_cycles,
    }
    for field, expected in expected_decisions.items():
        actual = parse_canonical_uint(diagnostics[field], field)
        if actual != expected:
            raise IntegrityError(
                f"{path.name}: {field}={actual}, expected {expected}"
            )

    return Chain(
        path=path,
        sha256=hashlib.sha256(data).hexdigest(),
        meta=meta,
        samples=tuple(samples),
        line_nonzero=line_nonzero,  # type: ignore[arg-type]
    )


def validate_chain_surface(chains: Sequence[Chain]) -> None:
    if len(chains) != 8:
        raise IntegrityError(f"expected exactly 8 logs, received {len(chains)}")
    seen: set[tuple[int, str, int]] = set()
    for chain in chains:
        if set(chain.meta) != RUN_FIELDS:
            raise IntegrityError(f"{chain.path.name}: RUN field inventory mismatch")
        if chain.meta["model"] != EXPECTED_MODEL:
            raise IntegrityError(f"{chain.path.name}: unexpected model")
        if chain.meta["t"] != "1":
            raise IntegrityError(f"{chain.path.name}: t must be exactly 1")
        if chain.start not in {"cold", "hot"}:
            raise IntegrityError(f"{chain.path.name}: invalid start={chain.start}")
        key = (chain.linear_size, chain.start, chain.replica)
        if key not in EXPECTED_SEEDS:
            raise IntegrityError(f"{chain.path.name}: unexpected chain key {key!r}")
        if key in seen:
            raise IntegrityError(f"{chain.path.name}: duplicate chain key {key!r}")
        seen.add(key)
        if chain.seed != EXPECTED_SEEDS[key]:
            raise IntegrityError(f"{chain.path.name}: frozen seed mismatch")
        schedule = EXPECTED_SCHEDULE[chain.linear_size]
        if parse_decimal_int(chain.meta["thermal_cycles"], "thermal_cycles") != schedule[
            "thermal_cycles"
        ]:
            raise IntegrityError(f"{chain.path.name}: thermal cycle mismatch")
        if parse_decimal_int(chain.meta["between_cycles"], "between_cycles") != schedule[
            "between_cycles"
        ]:
            raise IntegrityError(f"{chain.path.name}: between-cycle mismatch")
        if parse_decimal_int(chain.meta["measurements"], "measurements") != EXPECTED_SAMPLES:
            raise IntegrityError(f"{chain.path.name}: measurement-count mismatch")
        if parse_decimal_int(chain.meta["bit_cap"], "bit_cap") != EXPECTED_BIT_CAP:
            raise IntegrityError(f"{chain.path.name}: bit-cap mismatch")
    if seen != set(EXPECTED_SEEDS):
        missing_keys = sorted(set(EXPECTED_SEEDS) - seen)
        raise IntegrityError(f"missing chain keys {missing_keys!r}")


def values(chain: Chain, metric: str) -> list[float]:
    return [parse_finite(sample[metric], metric) for sample in chain.samples]


def arithmetic_mean(data: Iterable[float]) -> float:
    sequence = list(data)
    if not sequence:
        raise IntegrityError("mean of empty sequence")
    return math.fsum(sequence) / len(sequence)


def autocovariance(data: Sequence[float], lag: int, centre: float) -> float:
    count = len(data) - lag
    if count <= 0:
        return 0.0
    # A fixed-n denominator gives the positive-semidefinite sequence used by
    # the Geyer truncation and keeps this implementation architecture-stable.
    return math.fsum(
        (data[index] - centre) * (data[index + lag] - centre)
        for index in range(count)
    ) / len(data)


def geyer_tau_int(data: Sequence[float]) -> float:
    if len(data) < 4:
        raise IntegrityError("Geyer IMS requires at least four values")
    centre = arithmetic_mean(data)
    gamma0 = autocovariance(data, 0, centre)
    if gamma0 <= 0.0:
        return 0.5
    rho = [1.0]
    rho.extend(
        autocovariance(data, lag, centre) / gamma0 for lag in range(1, len(data))
    )
    pairs: list[float] = []
    for lag in range(0, len(rho) - 1, 2):
        pair = rho[lag] + rho[lag + 1]
        if pair <= 0.0:
            break
        if pairs and pair > pairs[-1]:
            pair = pairs[-1]
        pairs.append(pair)
    tau = -0.5 + math.fsum(pairs)
    return max(0.5, tau)


def series_stats(data: Sequence[float]) -> SeriesStats:
    if len(data) < 4:
        raise IntegrityError("series has fewer than four values")
    centre = arithmetic_mean(data)
    variance = statistics.variance(data)
    tau = geyer_tau_int(data)
    ess = min(float(len(data)), len(data) / (2.0 * tau))
    mcse = math.sqrt(max(0.0, variance) * 2.0 * tau / len(data))
    return SeriesStats(centre, mcse, tau, ess, variance)


def z_difference(mean_a: float, se_a: float, mean_b: float, se_b: float) -> float:
    denominator = math.hypot(se_a, se_b)
    if denominator == 0.0:
        return 0.0 if mean_a == mean_b else math.inf
    return abs(mean_a - mean_b) / denominator


def half_drift_z(data: Sequence[float]) -> float:
    if len(data) % 2:
        raise IntegrityError("half drift requires an even sample count")
    midpoint = len(data) // 2
    left = series_stats(data[:midpoint])
    right = series_stats(data[midpoint:])
    return z_difference(left.mean, left.mcse, right.mean, right.mcse)


def split_chains(series: Sequence[Sequence[float]]) -> list[list[float]]:
    result: list[list[float]] = []
    for chain in series:
        if len(chain) % 2:
            raise IntegrityError("split chains require even lengths")
        midpoint = len(chain) // 2
        result.append(list(chain[:midpoint]))
        result.append(list(chain[midpoint:]))
    return result


def average_ranks(data: Sequence[float]) -> list[float]:
    order = sorted(range(len(data)), key=lambda index: (data[index], index))
    ranks = [0.0] * len(data)
    cursor = 0
    while cursor < len(order):
        end = cursor + 1
        while end < len(order) and data[order[end]] == data[order[cursor]]:
            end += 1
        rank = ((cursor + 1) + end) / 2.0
        for position in range(cursor, end):
            ranks[order[position]] = rank
        cursor = end
    return ranks


def rank_normalize(chains: Sequence[Sequence[float]]) -> list[list[float]]:
    lengths = [len(chain) for chain in chains]
    flat = [value for chain in chains for value in chain]
    ranks = average_ranks(flat)
    normal = statistics.NormalDist()
    count = len(flat)
    transformed = [
        normal.inv_cdf((rank - 0.375) / (count + 0.25)) for rank in ranks
    ]
    result: list[list[float]] = []
    cursor = 0
    for length in lengths:
        result.append(transformed[cursor : cursor + length])
        cursor += length
    return result


def basic_rhat(chains: Sequence[Sequence[float]]) -> float:
    if len(chains) < 2:
        raise IntegrityError("R-hat requires at least two chains")
    length = len(chains[0])
    if length < 2 or any(len(chain) != length for chain in chains):
        raise IntegrityError("R-hat chains must have equal length >= 2")
    means = [arithmetic_mean(chain) for chain in chains]
    within = arithmetic_mean(statistics.variance(chain) for chain in chains)
    between = length * statistics.variance(means)
    if within == 0.0:
        return 1.0 if between == 0.0 else math.inf
    var_plus = ((length - 1.0) / length) * within + between / length
    return math.sqrt(max(0.0, var_plus / within))


def rank_folded_rhat(chains: Sequence[Sequence[float]]) -> tuple[float, float]:
    split = split_chains(chains)
    ranked = rank_normalize(split)
    rank_rhat = basic_rhat(ranked)
    flat = [value for chain in split for value in chain]
    median = statistics.median(flat)
    folded = [[abs(value - median) for value in chain] for chain in split]
    folded_rhat = basic_rhat(rank_normalize(folded))
    return rank_rhat, folded_rhat


def multi_chain_ess(chains: Sequence[Sequence[float]]) -> float:
    if len(chains) < 2:
        raise IntegrityError("pooled ESS requires at least two chains")
    length = len(chains[0])
    if length < 4 or any(len(chain) != length for chain in chains):
        raise IntegrityError("pooled ESS chains must have equal length >= 4")
    chain_means = [arithmetic_mean(chain) for chain in chains]
    within = arithmetic_mean(statistics.variance(chain) for chain in chains)
    between = length * statistics.variance(chain_means)
    var_plus = ((length - 1.0) / length) * within + between / length
    total_count = len(chains) * length
    if var_plus <= 0.0:
        return float(total_count) if between == 0.0 else 0.0

    autocovariances: list[list[float]] = []
    for chain, centre in zip(chains, chain_means):
        autocovariances.append(
            [autocovariance(chain, lag, centre) for lag in range(length)]
        )
    rho = [1.0]
    for lag in range(1, length):
        mean_gamma = arithmetic_mean(row[lag] for row in autocovariances)
        estimate = 1.0 - (within - mean_gamma) / var_plus
        rho.append(min(1.0, estimate))

    pairs: list[float] = []
    for lag in range(0, len(rho) - 1, 2):
        pair = rho[lag] + rho[lag + 1]
        if pair <= 0.0:
            break
        if pairs and pair > pairs[-1]:
            pair = pairs[-1]
        pairs.append(pair)
    tau = max(1.0, -1.0 + 2.0 * math.fsum(pairs))
    return min(float(total_count), total_count / tau)


def empirical_quantile(data: Sequence[float], probability: float) -> float:
    if not 0.0 <= probability <= 1.0 or not data:
        raise IntegrityError("invalid empirical quantile request")
    ordered = sorted(data)
    position = probability * (len(ordered) - 1)
    lower = int(math.floor(position))
    upper = int(math.ceil(position))
    if lower == upper:
        return ordered[lower]
    fraction = position - lower
    return ordered[lower] * (1.0 - fraction) + ordered[upper] * fraction


def bulk_tail_ess(chains: Sequence[Sequence[float]]) -> tuple[float, float]:
    split = split_chains(chains)
    bulk = multi_chain_ess(rank_normalize(split))
    flat = [value for chain in split for value in chain]
    low = empirical_quantile(flat, 0.05)
    high = empirical_quantile(flat, 0.95)
    low_indicator = [[1.0 if value <= low else 0.0 for value in chain] for chain in split]
    high_indicator = [[1.0 if value >= high else 0.0 for value in chain] for chain in split]
    tail = min(multi_chain_ess(low_indicator), multi_chain_ess(high_indicator))
    return bulk, tail


def conservative_group_mean_se(stats: Sequence[SeriesStats]) -> tuple[float, float]:
    if len(stats) != 2:
        raise IntegrityError("hot/cold groups require exactly two replicas")
    means = [entry.mean for entry in stats]
    group_mean = arithmetic_mean(means)
    within_se = math.hypot(stats[0].mcse, stats[1].mcse) / 2.0
    between_se = statistics.stdev(means) / math.sqrt(2.0)
    return group_mean, max(within_se, between_se)


def fmt(value: float) -> str:
    if not math.isfinite(value):
        return "inf" if value > 0 else "-inf"
    return f"{value:.12g}"


def print_terminal(result: str, failures: Sequence[str]) -> None:
    unique = sorted(set(failures))
    print("PILOT_FAILURES " + (",".join(unique) if unique else "NONE"))
    print(f"RESULT {result}")


def main(argv: Sequence[str] | None = None) -> int:
    arguments = list(sys.argv[1:] if argv is None else argv)
    if len(arguments) != 8:
        print("USAGE_ERROR expected_exactly_8_log_paths", file=sys.stderr)
        return 64

    print(f"PILOT_ANALYSIS {PILOT_ID} V1")

    try:
        validate_log_argument_names(arguments)
    except IntegrityError as error:
        print(f"INTEGRITY_DETAIL {str(error).replace(chr(10), ' ')}")
        print_terminal("STOP_INTEGRITY", ["raw_log_inventory"])
        return 0

    loaded: list[tuple[Path, bytes]] = []
    read_errors: list[str] = []
    for argument in arguments:
        path = Path(argument)
        try:
            loaded.append((path, path.read_bytes()))
        except OSError:
            read_errors.append(f"unreadable_{path.name}")

    raw_breaks = sorted(
        path.name for path, data in loaded if raw_kernel_break_marker(data)
    )
    if raw_breaks:
        for name in raw_breaks:
            read_errors.append(f"untrusted_raw_kernel_break_{name}")
    if read_errors:
        print_terminal("STOP_INTEGRITY", read_errors)
        return 0

    try:
        chains = [read_chain(path, data) for path, data in loaded]
        validate_chain_surface(chains)
    except IntegrityError as error:
        print(f"INTEGRITY_DETAIL {str(error).replace(chr(10), ' ')}")
        print_terminal("STOP_INTEGRITY", ["input_surface"])
        return 0

    chains.sort(key=lambda chain: (chain.linear_size, chain.start, chain.replica))
    mixing_failures: list[str] = []
    cache: dict[tuple[tuple[int, str, int], str], SeriesStats] = {}
    series_cache: dict[tuple[tuple[int, str, int], str], list[float]] = {}

    try:
        for chain in chains:
            key = (chain.linear_size, chain.start, chain.replica)
            hashes = {sample["state_hash"].lower() for sample in chain.samples}
            unique_fraction = len(hashes) / len(chain.samples)
            print(
                "CHAIN"
                f" file={chain.path.name}"
                f" sha256={chain.sha256}"
                f" L={chain.linear_size}"
                f" start={chain.start}"
                f" replica={chain.replica}"
                f" seed={chain.seed}"
                f" samples={len(chain.samples)}"
                f" unique_state_fraction={fmt(unique_fraction)}"
                f" line_nonzero_0={chain.line_nonzero[0]}"
                f" line_nonzero_1={chain.line_nonzero[1]}"
                f" line_nonzero_2={chain.line_nonzero[2]}"
                f" line_nonzero_3={chain.line_nonzero[3]}"
            )
            if unique_fraction < UNIQUE_STATE_MIN:
                mixing_failures.append(
                    f"low_unique_state_L{chain.linear_size}_{chain.start}_r{chain.replica}"
                )
            for direction, count in enumerate(chain.line_nonzero):
                if count == 0:
                    mixing_failures.append(
                        f"no_line_move_L{chain.linear_size}_{chain.start}_r{chain.replica}_mu{direction}"
                    )
            for metric in MIXING_METRICS:
                data = values(chain, metric)
                stats = series_stats(data)
                drift = half_drift_z(data)
                cache[(key, metric)] = stats
                series_cache[(key, metric)] = data
                print(
                    "METRIC"
                    f" L={chain.linear_size}"
                    f" start={chain.start}"
                    f" replica={chain.replica}"
                    f" name={metric}"
                    f" mean={fmt(stats.mean)}"
                    f" mcse={fmt(stats.mcse)}"
                    f" tau_int={fmt(stats.tau_int)}"
                    f" ess={fmt(stats.ess)}"
                    f" half_drift_z={fmt(drift)}"
                )
                if stats.variance == 0.0:
                    mixing_failures.append(
                        f"zero_variance_L{chain.linear_size}_{chain.start}_r{chain.replica}_{metric}"
                    )
                if stats.ess < PER_CHAIN_ESS_MIN:
                    mixing_failures.append(
                        f"low_ess_L{chain.linear_size}_{chain.start}_r{chain.replica}_{metric}"
                    )
                if drift > Z_MAX:
                    mixing_failures.append(
                        f"half_drift_L{chain.linear_size}_{chain.start}_r{chain.replica}_{metric}"
                    )

        for linear_size in (6, 8):
            for metric in MIXING_METRICS:
                metric_series = [
                    series_cache[((linear_size, start, replica), metric)]
                    for start in ("cold", "hot")
                    for replica in (1, 2)
                ]
                rank_rhat, folded_rhat = rank_folded_rhat(metric_series)
                bulk_ess, tail_ess = bulk_tail_ess(metric_series)
                cold_stats = [
                    cache[((linear_size, "cold", replica), metric)] for replica in (1, 2)
                ]
                hot_stats = [
                    cache[((linear_size, "hot", replica), metric)] for replica in (1, 2)
                ]
                cold_mean, cold_se = conservative_group_mean_se(cold_stats)
                hot_mean, hot_se = conservative_group_mean_se(hot_stats)
                hot_cold_z = z_difference(cold_mean, cold_se, hot_mean, hot_se)
                print(
                    "POOLED"
                    f" L={linear_size}"
                    f" name={metric}"
                    f" rank_rhat={fmt(rank_rhat)}"
                    f" folded_rhat={fmt(folded_rhat)}"
                    f" bulk_ess={fmt(bulk_ess)}"
                    f" tail_ess={fmt(tail_ess)}"
                    f" cold_mean={fmt(cold_mean)}"
                    f" hot_mean={fmt(hot_mean)}"
                    f" hot_cold_z={fmt(hot_cold_z)}"
                )
                if rank_rhat > RHAT_MAX:
                    mixing_failures.append(f"rank_rhat_L{linear_size}_{metric}")
                if folded_rhat > RHAT_MAX:
                    mixing_failures.append(f"folded_rhat_L{linear_size}_{metric}")
                if bulk_ess < BULK_ESS_MIN:
                    mixing_failures.append(f"low_bulk_ess_L{linear_size}_{metric}")
                if tail_ess < TAIL_ESS_MIN:
                    mixing_failures.append(f"low_tail_ess_L{linear_size}_{metric}")
                if hot_cold_z > Z_MAX:
                    mixing_failures.append(f"hot_cold_L{linear_size}_{metric}")
    except (IntegrityError, OverflowError, statistics.StatisticsError) as error:
        print(f"INTEGRITY_DETAIL statistics_{str(error).replace(chr(10), ' ')}")
        print_terminal("STOP_INTEGRITY", ["statistics_surface"])
        return 0

    if mixing_failures:
        print_terminal("STOP_MIXING", mixing_failures)
        return 0
    print_terminal("PILOT_READY_FOR_PRODUCTION_PREREG", [])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
