#!/usr/bin/env python3
"""Frozen zero-evidence mixing analysis for E-PHOTON-Z5-PHASE-MEASUREMENT-1."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import math
from pathlib import Path
import statistics
from typing import Iterable

REQUIRED_METRICS = (
    "logw",
    "polyakov_radius",
    "vortex_density",
    "monopole_density",
    "monopole_weighted_density",
    "score_mean",
)
MIXING_METRICS = (
    "logw",
    "polyakov_radius",
    "vortex_density",
    "monopole_density",
)


@dataclass(frozen=True)
class Chain:
    path: Path
    sha256: str
    meta: dict[str, str]
    samples: tuple[dict[str, str], ...]
    terminal: tuple[str, ...]


def parse_fields(line: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for token in line.split()[1:]:
        if "=" not in token:
            continue
        key, value = token.split("=", 1)
        fields[key] = value
    return fields


def read_chain(path: Path) -> Chain:
    data = path.read_bytes()
    text = data.decode("utf-8")
    meta: dict[str, str] | None = None
    samples: list[dict[str, str]] = []
    terminal: list[str] = []
    for raw in text.splitlines():
        if raw.startswith("RUN "):
            if meta is not None:
                raise ValueError(f"{path}: repeated RUN line")
            meta = parse_fields(raw)
        elif raw.startswith("SAMPLE "):
            samples.append(parse_fields(raw))
        elif raw.startswith((
            "SUMMARY ",
            "FLUX_FRACTIONS ",
            "CORRELATOR ",
            "DUAL_WARD_STATUS ",
            "CORRELATOR_UNCERTAINTY_STATUS ",
            "EVIDENTIAL_STATUS ",
        )):
            terminal.append(raw)
    if meta is None:
        raise ValueError(f"{path}: missing RUN line")
    expected = int(meta["measurements"])
    if len(samples) != expected:
        raise ValueError(f"{path}: expected {expected} samples, found {len(samples)}")
    for index, sample in enumerate(samples):
        if int(sample.get("index", "-1")) != index:
            raise ValueError(f"{path}: nonconsecutive sample index at {index}")
        missing = [name for name in REQUIRED_METRICS if name not in sample]
        if missing:
            raise ValueError(f"{path}: sample {index} lacks {missing}")
    required_terminal = {
        "DUAL_WARD_STATUS NOT_IMPLEMENTED_PILOT",
        "CORRELATOR_UNCERTAINTY_STATUS NOT_IMPLEMENTED_PILOT",
        "EVIDENTIAL_STATUS ZERO_PILOT_ONLY",
    }
    if not required_terminal.issubset(set(terminal)):
        raise ValueError(f"{path}: required zero-evidence terminal markers are missing")
    if meta.get("model") != "TWIST_Z5_FACE_WEIGHT_V1":
        raise ValueError(f"{path}: unexpected model")
    if meta.get("kernel") != "EXACT_PHI_HEATBATH" or meta.get("t") != "1":
        raise ValueError(f"{path}: physical t=1 exact kernel not declared")
    return Chain(
        path=path,
        sha256=hashlib.sha256(data).hexdigest(),
        meta=meta,
        samples=tuple(samples),
        terminal=tuple(terminal),
    )


def values(chain: Chain, metric: str) -> list[float]:
    return [float(sample[metric]) for sample in chain.samples]


def mean(data: Iterable[float]) -> float:
    sequence = list(data)
    return math.fsum(sequence) / len(sequence)


def autocorrelation_time(data: list[float]) -> float:
    n = len(data)
    centre = mean(data)
    variance = math.fsum((value - centre) ** 2 for value in data) / n
    if variance == 0:
        return 0.5
    correlations: list[float] = []
    max_lag = min(n // 2, 256)
    for lag in range(1, max_lag + 1):
        covariance = math.fsum(
            (data[index] - centre) * (data[index + lag] - centre)
            for index in range(n - lag)
        ) / (n - lag)
        correlations.append(covariance / variance)
    # Geyer's initial-positive-pair truncation.
    total = 0.0
    index = 0
    while index < len(correlations):
        pair = correlations[index]
        if index + 1 < len(correlations):
            pair += correlations[index + 1]
        if pair <= 0:
            break
        total += pair
        index += 2
    return max(0.5, 0.5 + total)


def blocking_errors(data: list[float]) -> list[tuple[int, int, float]]:
    result: list[tuple[int, int, float]] = []
    block = 1
    while True:
        nblocks = len(data) // block
        if nblocks < 8:
            break
        block_means = [
            mean(data[index * block : (index + 1) * block])
            for index in range(nblocks)
        ]
        if len(block_means) < 2:
            break
        standard_error = statistics.stdev(block_means) / math.sqrt(nblocks)
        result.append((block, nblocks, standard_error))
        block *= 2
    return result


def metric_stats(chain: Chain, metric: str) -> tuple[float, float, float, float]:
    data = values(chain, metric)
    tau = autocorrelation_time(data)
    ess = len(data) / (2.0 * tau)
    blocks = blocking_errors(data)
    conservative_error = max((entry[2] for entry in blocks), default=0.0)
    return mean(data), conservative_error, tau, ess


def fmt(value: float) -> str:
    if not math.isfinite(value):
        return str(value)
    return f"{value:.12g}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("logs", nargs="+", type=Path)
    args = parser.parse_args()

    chains = sorted((read_chain(path) for path in args.logs), key=lambda chain: (
        int(chain.meta["L"]), chain.meta["start"], int(chain.meta["seed"])
    ))
    groups: dict[int, dict[str, Chain]] = {}
    failures: list[str] = []

    print("PILOT_ANALYSIS E-PHOTON-Z5-PHASE-MEASUREMENT-1 V1")
    for chain in chains:
        linear_size = int(chain.meta["L"])
        start = chain.meta["start"]
        if start in groups.setdefault(linear_size, {}):
            failures.append(f"duplicate_{linear_size}_{start}")
        groups[linear_size][start] = chain
        unique_hashes = len({sample["state_hash"] for sample in chain.samples})
        unique_fraction = unique_hashes / len(chain.samples)
        if unique_fraction < 0.9:
            failures.append(f"state_hash_stuck_L{linear_size}_{start}")
        print(
            "CHAIN"
            f" file={chain.path.name}"
            f" sha256={chain.sha256}"
            f" L={linear_size}"
            f" start={start}"
            f" seed={chain.meta['seed']}"
            f" samples={len(chain.samples)}"
            f" unique_state_fraction={fmt(unique_fraction)}"
        )
        for metric in REQUIRED_METRICS:
            metric_mean, error, tau, ess = metric_stats(chain, metric)
            print(
                "METRIC"
                f" L={linear_size}"
                f" start={start}"
                f" name={metric}"
                f" mean={fmt(metric_mean)}"
                f" conservative_se={fmt(error)}"
                f" tau_int={fmt(tau)}"
                f" ess={fmt(ess)}"
            )
            if metric in MIXING_METRICS and ess < 16:
                failures.append(f"low_ess_L{linear_size}_{start}_{metric}")

    for required_size in (6, 8):
        starts = groups.get(required_size, {})
        if set(starts) != {"cold", "hot"}:
            failures.append(f"missing_hot_cold_L{required_size}")
            continue
        cold, hot = starts["cold"], starts["hot"]
        for metric in MIXING_METRICS:
            cold_mean, cold_error, _, _ = metric_stats(cold, metric)
            hot_mean, hot_error, _, _ = metric_stats(hot, metric)
            denominator = math.hypot(cold_error, hot_error)
            z_score = abs(cold_mean - hot_mean) / denominator if denominator else (
                0.0 if cold_mean == hot_mean else math.inf
            )
            print(
                "HOT_COLD"
                f" L={required_size}"
                f" name={metric}"
                f" cold={fmt(cold_mean)}"
                f" hot={fmt(hot_mean)}"
                f" z={fmt(z_score)}"
            )
            if z_score > 4:
                failures.append(f"hot_cold_L{required_size}_{metric}")

    blockers = (
        "DUAL_WARD_ENGINE",
        "CORRELATOR_RAW_JACKKNIFE",
        "PRODUCTION_THRESHOLDS",
        "CHECKPOINT_RESTART",
        "SECOND_FULL_IMPLEMENTATION_OR_FROZEN_SUBSET",
    )
    print("PRODUCTION_BLOCKERS " + ",".join(blockers))
    if failures:
        print("PILOT_FAILURES " + ",".join(sorted(set(failures))))
        print("RESULT STOP_MIXING_OR_INTEGRITY")
        raise SystemExit(1)
    print("PILOT_FAILURES NONE")
    print("RESULT PILOT_KERNEL_PASS_PRODUCTION_BLOCKED")


if __name__ == "__main__":
    main()
