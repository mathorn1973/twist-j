#!/usr/bin/env python3
"""Frozen statistical analysis for P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import statistics
import sys
from typing import Callable, Iterable, Sequence


FAMILIES = ("inline1", "transverse1", "inline2", "transverse2")
BLOCK = 32
SAMPLES = 512
SQRT5 = math.sqrt(5.0)
KAPPA2 = 5.0 - 2.0 * SQRT5
INV_KAPPA2 = 1.0 / KAPPA2

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

DUAL_SPECS = {
    f"dual_L{L}_{start}_r{replica}.jsonl": (
        L,
        start,
        replica,
        (0xE756060000000000 if L == 6 else 0xE756080000000000)
        + (0x100 if start == "cold" else 0x200)
        + replica,
        663552 if L == 6 else 2097152,
        2592 if L == 6 else 8192,
    )
    for L in (6, 8)
    for start in ("cold", "surface")
    for replica in (1, 2)
}


class IntegrityFailure(RuntimeError):
    pass


@dataclass(frozen=True)
class Chain:
    name: str
    L: int
    start: str
    replica: int
    samples: tuple[dict[str, object], ...]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def require_ascii_lf(path: Path) -> tuple[bytes, list[str]]:
    try:
        raw = path.read_bytes()
    except OSError as error:
        raise IntegrityFailure(f"missing_{path.name}") from error
    if b"\r" in raw or not raw.endswith(b"\n"):
        raise IntegrityFailure(f"noncanonical_newlines_{path.name}")
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError as error:
        raise IntegrityFailure(f"nonascii_{path.name}") from error
    return raw, text.splitlines()


def fields(line: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for token in line.split()[1:]:
        if "=" not in token:
            raise IntegrityFailure("malformed_key_value_record")
        key, value = token.split("=", 1)
        if not key or key in result:
            raise IntegrityFailure("duplicate_key_value_field")
        result[key] = value
    return result


def finite(value: object, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise IntegrityFailure(f"nonnumeric_{label}")
    answer = float(value)
    if not math.isfinite(answer):
        raise IntegrityFailure(f"nonfinite_{label}")
    return answer


def diagnostic_number(value: float) -> str:
    """Format a derived diagnostic without emitting a numeric inf/nan token."""

    return f"{value:.6f}" if math.isfinite(value) else "NONFINITE"


def load_pilot_stats(repository_root: Path):
    path = (
        repository_root
        / "probes"
        / "P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2"
        / "analyze_pilot.py"
    )
    spec = importlib.util.spec_from_file_location("frozen_pilot_stats", path)
    if spec is None or spec.loader is None:
        raise IntegrityFailure("cannot_load_frozen_pilot_stats")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def parse_pilot_inputs(base: Path) -> dict[str, tuple[dict[str, str], ...]]:
    pilot = base.parent / "P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2"
    result: dict[str, tuple[dict[str, str], ...]] = {}
    for name, expected_hash in PILOT_HASHES.items():
        raw, lines = require_ascii_lf(pilot / name)
        if digest(raw) != expected_hash:
            raise IntegrityFailure(f"pilot_hash_mismatch_{name}")
        sample_lines = [line for line in lines if line.startswith("SAMPLE ")]
        if len(sample_lines) != SAMPLES:
            raise IntegrityFailure(f"pilot_sample_count_{name}")
        parsed = tuple(fields(line) for line in sample_lines)
        for index, sample in enumerate(parsed):
            if sample.get("index") != str(index):
                raise IntegrityFailure(f"pilot_index_{name}")
            total = sum(int(sample[f"flux_count_{value}"]) for value in range(5))
            L = int(name[1])
            if total != 6 * L**4:
                raise IntegrityFailure(f"pilot_flux_census_{name}")
        result[name] = parsed
    return result


def parse_primal(base: Path, pilot: dict[str, tuple[dict[str, str], ...]]) -> list[Chain]:
    result: list[Chain] = []
    for name, (L, start, replica, seed, thermal, between) in PRIMAL_SPECS.items():
        _, lines = require_ascii_lf(base / name)
        if len(lines) != SAMPLES + 2 or not lines[0].startswith("RUN "):
            raise IntegrityFailure(f"primal_layout_{name}")
        header = fields(lines[0])
        expected_header = {
            "L": str(L),
            "seed": f"0x{seed:016x}",
            "start": start,
            "thermal_cycles": str(thermal),
            "measurements": str(SAMPLES),
            "between_cycles": str(between),
        }
        for key, expected in expected_header.items():
            if header.get(key) != expected:
                raise IntegrityFailure(f"primal_header_{name}_{key}")
        if not lines[-1].startswith("SUMMARY ") or fields(lines[-1]).get("status") != "PASS":
            raise IntegrityFailure(f"primal_summary_{name}")
        parsed: list[dict[str, object]] = []
        pilot_name = f"L{L}_{start}_r{replica}.log"
        public = pilot[pilot_name]
        for index, line in enumerate(lines[1:-1]):
            if not line.startswith("SAMPLE "):
                raise IntegrityFailure(f"primal_sample_record_{name}")
            item = fields(line)
            if item.get("index") != str(index):
                raise IntegrityFailure(f"primal_index_{name}")
            for key in (
                "state_hash",
                "cache_hash",
                "flux_count_0",
                "flux_count_1",
                "flux_count_2",
                "flux_count_3",
                "flux_count_4",
            ):
                if item.get(key) != public[index].get(key):
                    raise IntegrityFailure(f"primal_public_replay_{name}_{index}_{key}")
            record: dict[str, object] = {"state_hash": item["state_hash"]}
            for key in (
                "g_mean",
                "g2_mean",
                "x2_mean",
                "pair_inline1",
                "pair_transverse1",
                "pair_inline2",
                "pair_transverse2",
                "rho_power_0",
                "rho_power_1",
                "rho_power_2",
                "rho_power_3",
            ):
                value = float(item[key])
                if not math.isfinite(value):
                    raise IntegrityFailure(f"primal_nonfinite_{name}_{key}")
                record[key] = value
            public_x2 = pilot_x2_series((public[index],), L)[0]
            if abs(float(record["x2_mean"]) - public_x2) > 1e-14:
                raise IntegrityFailure(f"primal_x2_reconstruction_{name}_{index}")
            record["rho_power_mean"] = math.fsum(
                float(record[f"rho_power_{axis}"]) for axis in range(4)
            ) / 4.0
            parsed.append(record)
        result.append(Chain(name, L, start, replica, tuple(parsed)))
    return result


def parse_dual(base: Path) -> list[Chain]:
    result: list[Chain] = []
    for name, (L, start, replica, seed, thermal, between) in DUAL_SPECS.items():
        _, lines = require_ascii_lf(base / name)
        if len(lines) != SAMPLES + 2:
            raise IntegrityFailure(f"dual_layout_{name}")
        try:
            records = [json.loads(line) for line in lines]
        except (json.JSONDecodeError, UnicodeError) as error:
            raise IntegrityFailure(f"dual_json_{name}") from error
        header = records[0]
        expected = {
            "type": "run",
            "mode": "decision",
            "L": L,
            "seed": f"0x{seed:032x}",
            "start": start,
            "thermal_steps": thermal,
            "samples": SAMPLES,
            "between_steps": between,
            "domain": "dual756",
        }
        for key, value in expected.items():
            if header.get(key) != value:
                raise IntegrityFailure(f"dual_header_{name}_{key}")
        parsed: list[dict[str, object]] = []
        for index, item in enumerate(records[1:-1]):
            if item.get("type") != "sample" or item.get("index") != index:
                raise IntegrityFailure(f"dual_index_{name}")
            pairs = item.get("pair_products")
            momenta = item.get("lowest_momenta")
            if not isinstance(pairs, list) or [entry.get("family") for entry in pairs] != list(FAMILIES):
                raise IntegrityFailure(f"dual_pair_schema_{name}")
            if not isinstance(momenta, list) or [entry.get("momentum_axis") for entry in momenta] != list(range(4)):
                raise IntegrityFailure(f"dual_momentum_schema_{name}")
            record: dict[str, object] = {
                "state_hash": item.get("state_sha256"),
                "n_mean": finite(item.get("n_mean"), "n_mean"),
                "n2_mean": finite(item.get("n2_mean"), "n2_mean"),
                "j2_mean": finite(item.get("j2_mean"), "j2_mean"),
                "j_nonzero_density": finite(
                    item.get("j_nonzero_density"), "j_nonzero_density"
                ),
            }
            if item.get("partial_j_zero") is not True:
                raise IntegrityFailure(f"dual_current_closure_{name}_{index}")
            state_hash = record["state_hash"]
            if not isinstance(state_hash, str) or len(state_hash) != 64:
                raise IntegrityFailure(f"dual_state_hash_{name}")
            for family, entry in zip(FAMILIES, pairs):
                record[f"pair_{family}"] = finite(entry.get("mean"), family)
            for axis, entry in enumerate(momenta):
                record[f"sj_power_{axis}"] = finite(entry.get("sj_trace"), "sj_trace")
                finite(entry.get("longitudinal_power"), "longitudinal")
            record["sj_power_mean"] = finite(
                item.get("axis_average_sj_trace"), "axis_average_sj_trace"
            )
            parsed.append(record)
        summary = records[-1]
        if summary.get("type") != "summary" or summary.get("samples_emitted") != SAMPLES:
            raise IntegrityFailure(f"dual_summary_{name}")
        result.append(Chain(name, L, start, replica, tuple(parsed)))
    return result


def pilot_x2_series(samples: Sequence[dict[str, str]], L: int) -> list[float]:
    total = 6 * L**4
    x2_large = 5.0 + 2.0 * SQRT5
    return [
        (
            (int(item["flux_count_1"]) + int(item["flux_count_4"])) * KAPPA2
            + (int(item["flux_count_2"]) + int(item["flux_count_3"])) * x2_large
        )
        / total
        for item in samples
    ]


def chain_values(chain: Chain, metric: str) -> list[float]:
    return [finite(item[metric], metric) for item in chain.samples]


def group_separation(stats_module, chains: Sequence[Sequence[float]]) -> float:
    if len(chains) == 2:
        left = stats_module.series_stats(chains[0])
        right = stats_module.series_stats(chains[1])
        return stats_module.z_difference(left.mean, left.mcse, right.mean, right.mcse)
    if len(chains) != 4:
        raise IntegrityFailure("bad_group_chain_count")
    entries = [stats_module.series_stats(chain) for chain in chains]
    group: list[tuple[float, float]] = []
    for offset in (0, 2):
        pair = entries[offset : offset + 2]
        means = [item.mean for item in pair]
        centre = math.fsum(means) / 2.0
        se = max(
            math.hypot(pair[0].mcse, pair[1].mcse) / 2.0,
            statistics.stdev(means) / math.sqrt(2.0),
        )
        group.append((centre, se))
    return stats_module.z_difference(*group[0], *group[1])


def mixing_audit(
    stats_module,
    chains: Sequence[Chain],
    metrics: Sequence[str],
    rhat_limit: float,
) -> tuple[list[str], list[str]]:
    failures: list[str] = []
    detail: list[str] = []
    for chain in chains:
        unique = len({str(item["state_hash"]) for item in chain.samples}) / SAMPLES
        if unique < 0.99:
            failures.append(f"{chain.name}:unique={unique:.6g}")
    for metric in metrics:
        series = [chain_values(chain, metric) for chain in chains]
        ess_values: list[float] = []
        drift_values: list[float] = []
        for chain, values in zip(chains, series):
            item = stats_module.series_stats(values)
            ess_values.append(item.ess)
            drift = stats_module.half_drift_z(values)
            drift_values.append(drift)
            if not math.isfinite(item.variance) or item.variance <= 0.0:
                failures.append(f"{chain.name}:{metric}:variance")
            if not math.isfinite(item.ess):
                failures.append(f"{chain.name}:{metric}:ess=NONFINITE")
            elif item.ess < 64.0:
                failures.append(f"{chain.name}:{metric}:ess={item.ess:.6g}")
            if not math.isfinite(drift):
                failures.append(f"{chain.name}:{metric}:drift=NONFINITE")
        minimum_ess = min(ess_values) if all(map(math.isfinite, ess_values)) else math.nan
        maximum_drift = (
            max(drift_values) if all(map(math.isfinite, drift_values)) else math.nan
        )
        rank_rhat, folded_rhat = stats_module.rank_folded_rhat(series)
        pooled_ess = stats_module.bulk_tail_ess(series)[0]
        separation = group_separation(stats_module, series)
        if not math.isfinite(rank_rhat):
            failures.append(f"{metric}:rhat=NONFINITE")
        elif rank_rhat > rhat_limit:
            failures.append(f"{metric}:rhat={rank_rhat:.6g}")
        if not math.isfinite(folded_rhat):
            failures.append(f"{metric}:folded=NONFINITE")
        elif folded_rhat > rhat_limit:
            failures.append(f"{metric}:folded={folded_rhat:.6g}")
        if not math.isfinite(pooled_ess):
            failures.append(f"{metric}:bulk_ess=NONFINITE")
        elif pooled_ess < 200.0:
            failures.append(f"{metric}:bulk_ess={pooled_ess:.6g}")
        if math.isfinite(maximum_drift) and maximum_drift > 4.0:
            failures.append(f"{metric}:drift={maximum_drift:.6g}")
        if not math.isfinite(separation):
            failures.append(f"{metric}:starts=NONFINITE")
        elif separation > 4.0:
            failures.append(f"{metric}:starts={separation:.6g}")
        detail.append(
            f"{metric}:min_ess={diagnostic_number(minimum_ess)},"
            f"rhat={diagnostic_number(rank_rhat)},"
            f"folded={diagnostic_number(folded_rhat)},"
            f"bulk_ess={diagnostic_number(pooled_ess)},"
            f"drift={diagnostic_number(maximum_drift)},"
            f"starts={diagnostic_number(separation)}"
        )
    return failures, detail


def blocks(chains: Sequence[Sequence[Sequence[float]]]) -> list[list[float]]:
    result: list[list[float]] = []
    for chain in chains:
        if len(chain) != SAMPLES:
            raise IntegrityFailure("block_sample_count")
        for start in range(0, SAMPLES, BLOCK):
            chunk = chain[start : start + BLOCK]
            width = len(chunk[0])
            result.append(
                [math.fsum(row[column] for row in chunk) / BLOCK for column in range(width)]
            )
    return result


def column_mean(rows: Sequence[Sequence[float]]) -> list[float]:
    return [
        math.fsum(row[column] for row in rows) / len(rows)
        for column in range(len(rows[0]))
    ]


def jackknife(
    rows: Sequence[Sequence[float]], estimator: Callable[[Sequence[float]], float]
) -> tuple[float, float]:
    if len(rows) < 16:
        raise IntegrityFailure("too_few_blocks")
    estimate = estimator(column_mean(rows))
    leave_one: list[float] = []
    for omitted in range(len(rows)):
        kept = rows[:omitted] + rows[omitted + 1 :]
        leave_one.append(estimator(column_mean(kept)))
    centre = math.fsum(leave_one) / len(leave_one)
    variance = (len(rows) - 1.0) / len(rows) * math.fsum(
        (value - centre) ** 2 for value in leave_one
    )
    return estimate, math.sqrt(max(0.0, variance))


def joint_residual(
    left: tuple[float, float], right: tuple[float, float]
) -> tuple[float, float]:
    return left[0] + right[0], math.hypot(left[1], right[1])


def format_identity(
    L: int,
    name: str,
    residual: float,
    se: float,
    precision_limit: float,
) -> tuple[str, bool, bool]:
    halfwidth = 4.0 * se
    precision = halfwidth <= precision_limit
    dictionary = abs(residual) <= halfwidth + 5e-15
    status = (
        "PASS"
        if precision and dictionary
        else ("PRECISION_FAIL" if not precision else "DICTIONARY_FAIL")
    )
    return (
        f"IDENTITY L={L} name={name} residual={residual:.12g} se={se:.12g} "
        f"four_se={halfwidth:.12g} precision_limit={precision_limit:.12g} status={status}",
        precision,
        dictionary,
    )


def analyze(base: Path) -> tuple[list[str], str]:
    repository_root = base.parent.parent
    stats_module = load_pilot_stats(repository_root)
    pilot = parse_pilot_inputs(base)
    primal = parse_primal(base, pilot)
    dual = parse_dual(base)
    lines = [
        "PROBE P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1",
        "EVIDENTIAL_SCOPE ZERO_ENGINEERING_ONLY",
        "INPUT_CUSTODY public_pilot_logs=8 primal_replays=4 dual_chains=8 status=PASS",
    ]
    any_mixing = False
    any_precision = False
    any_dictionary = False

    primal_metrics = (
        "g_mean",
        "x2_mean",
        *(f"pair_{name}" for name in FAMILIES),
        *(f"rho_power_{axis}" for axis in range(4)),
    )
    dual_metrics = (
        "n_mean",
        "n2_mean",
        *(f"pair_{name}" for name in FAMILIES),
        "j2_mean",
        "j_nonzero_density",
        *(f"sj_power_{axis}" for axis in range(4)),
    )

    for L in (6, 8):
        pchains = [chain for chain in primal if chain.L == L]
        dchains = [chain for chain in dual if chain.L == L]
        p_fail, p_detail = mixing_audit(stats_module, pchains, primal_metrics, 1.10)
        d_fail, d_detail = mixing_audit(stats_module, dchains, dual_metrics, 1.05)
        any_mixing |= bool(p_fail or d_fail)
        lines.append(
            f"MIXING L={L} primal={'FAIL' if p_fail else 'PASS'} "
            f"dual={'FAIL' if d_fail else 'PASS'} primal_failures={len(p_fail)} "
            f"dual_failures={len(d_fail)}"
        )
        for entry in p_fail + d_fail:
            lines.append(f"MIXING_FAILURE L={L} {entry}")
        for entry in p_detail:
            lines.append(f"MIXING_DETAIL L={L} ensemble=primal {entry}")
        for entry in d_detail:
            lines.append(f"MIXING_DETAIL L={L} ensemble=dual {entry}")

        pilot_chains = [
            [[value] for value in pilot_x2_series(samples, L)]
            for name, samples in pilot.items()
            if name.startswith(f"L{L}_")
        ]
        p_contact = jackknife(blocks(pilot_chains), lambda mean: mean[0])
        d_contact_rows = [
            [[finite(item["n2_mean"], "n2_mean")] for item in chain.samples]
            for chain in dchains
        ]
        d_contact_raw = jackknife(blocks(d_contact_rows), lambda mean: 2.0 * mean[0] - 1.0)
        contact = joint_residual(p_contact, d_contact_raw)
        line, precision, dictionary = format_identity(L, "contact", *contact, 0.03)
        lines.append(line)
        any_precision |= not precision
        any_dictionary |= not dictionary

        for family in FAMILIES:
            p_rows = [
                [
                    [
                        finite(item["g_mean"], "g_mean"),
                        finite(item[f"pair_{family}"], family),
                    ]
                    for item in chain.samples
                ]
                for chain in pchains
            ]
            d_rows = [
                [
                    [
                        finite(item["n_mean"], "n_mean"),
                        finite(item[f"pair_{family}"], family),
                    ]
                    for item in chain.samples
                ]
                for chain in dchains
            ]
            p_cov = jackknife(blocks(p_rows), lambda mean: mean[1] - mean[0] ** 2)
            d_cov_raw = jackknife(
                blocks(d_rows),
                lambda mean: INV_KAPPA2 * (mean[1] - mean[0] ** 2),
            )
            residual = joint_residual(p_cov, d_cov_raw)
            line, precision, dictionary = format_identity(L, family, *residual, 0.02)
            lines.append(line)
            any_precision |= not precision
            any_dictionary |= not dictionary

        p_current_rows = [
            [[finite(item["rho_power_mean"], "rho_power_mean")] for item in chain.samples]
            for chain in pchains
        ]
        d_current_rows = [
            [
                [
                    finite(item["sj_power_mean"], "sj_power_mean"),
                    finite(item["n2_mean"], "n2_mean"),
                ]
                for item in chain.samples
            ]
            for chain in dchains
        ]
        lambda_l = 4.0 * math.sin(math.pi / L) ** 2
        p_rho = jackknife(blocks(p_current_rows), lambda mean: mean[0])
        d_sj = jackknife(blocks(d_current_rows), lambda mean: 25.0 * mean[0])
        baseline = jackknife(
            blocks(d_current_rows), lambda mean: 3.0 * (1.0 - mean[1])
        )
        screening = (p_rho[0] + d_sj[0]) / lambda_l
        screening_se = math.hypot(p_rho[1], d_sj[1]) / lambda_l
        lines.append(
            f"SCREENING L={L} R_lowest={screening:.12g} se={screening_se:.12g} "
            f"four_se={4.0*screening_se:.12g} contact_baseline={baseline[0]:.12g} "
            f"baseline_se={baseline[1]:.12g} decision_authority=NONE"
        )

    if any_mixing or any_precision:
        terminal = "STOP_DUAL_MIXING"
    elif any_dictionary:
        terminal = "STOP_DUAL_INTEGRITY"
        lines.append("INTEGRITY_REASON DICTIONARY_RESIDUAL_OUTSIDE_BUDGET")
    else:
        terminal = "DUAL_CROSSCHECK_PASS"
    lines.append(f"TERMINAL {terminal}")
    lines.append("EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY")
    return lines, terminal


def main() -> int:
    if len(sys.argv) != 1:
        print("usage: python3 analyze_crosscheck.py", file=sys.stderr)
        return 64
    base = Path(__file__).resolve().parent
    try:
        lines, _ = analyze(base)
    except (IntegrityFailure, OSError, RuntimeError, ValueError) as error:
        reason = str(error).replace(" ", "_")
        lines = [
            "PROBE P-PHOTON-Z5-DUAL-WARD-CROSSCHECK-1",
            "EVIDENTIAL_SCOPE ZERO_ENGINEERING_ONLY",
            f"INTEGRITY_FAILURE reason={reason}",
            "TERMINAL STOP_DUAL_INTEGRITY",
            "EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY",
        ]
    sys.stdout.write("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
