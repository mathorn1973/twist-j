"""Descriptive correlations and covariance at a single fixed registered volume."""
import argparse
from decimal import Decimal
import json
from pathlib import Path

import numpy as np

from analyze_ordered import ENDPOINTS, ROUNDING, SAMPLES, VOLUMES, json_record


def load_values(path, L, thermal):
    values = None
    keys = None
    seen = set()
    with path.open(encoding="utf-8") as source:
        for line in source:
            record = json_record(line)
            names = tuple(sorted(record["observables"]))
            if values is None:
                keys = names
                values = np.empty((4, SAMPLES, len(keys)), dtype=np.float64)
            if names != keys:
                raise ValueError("Observable inventory changes within a volume")
            chain_names = [f"L{L}-c{i}" for i in (1, 2, 3, 4)]
            chain = chain_names.index(record["chain"])
            sample = record["sample"]
            identity = (chain, sample)
            if (record["L"] != L or type(sample) is not int or not 0 <= sample < SAMPLES
                    or record["macrocycle"] != thermal + sample + 1 or identity in seen):
                raise ValueError("Bad or duplicate state identity")
            seen.add(identity)
            centres = []
            for key in keys:
                lo, hi = map(Decimal, record["observables"][key])
                if not lo.is_finite() or not hi.is_finite() or not 0 <= (hi-lo)/2 <= ROUNDING:
                    raise ValueError(f"Invalid measured interval for {key}")
                centres.append(float((lo+hi)/2))
            values[chain, sample] = centres
    return (keys, values) if len(seen) == 4 * SAMPLES else (None, None)


def summaries(values):
    chain_means = np.mean(values, axis=1)
    means = np.mean(chain_means, axis=0)
    candidates = [np.std(chain_means, axis=0, ddof=1) / 2]
    for length in (64, 128, 256, 512):
        groups = SAMPLES // length
        batch_means = values.reshape(4, groups, length, values.shape[-1]).mean(axis=2)
        variance = np.sum(np.var(batch_means, axis=1, ddof=1), axis=0) / (16 * groups)
        candidates.append(np.sqrt(variance))
    return means, np.max(candidates, axis=0)


def report(keys, values):
    means, errors = summaries(values)
    frame = {key: {"mean": float(means[i]), "diagnostic_se": float(errors[i]),
                   "arithmetic_radius": str(ROUNDING)} for i, key in enumerate(keys)}
    primary = [i for i, key in enumerate(keys) if key.startswith(("A:", "D:"))]
    measured = values[:, :, primary].reshape(4*SAMPLES, len(primary))
    covariance = np.atleast_2d(np.cov(measured, rowvar=False))
    amplitude_checks = {}
    for key, item in frame.items():
        if key.startswith("A:"):
            _, label, scale = key.split(":")
            amplitude_checks[f"{label}:{scale}"] = {scale: item["mean"]/int(scale)}
    for key in keys:
        if not key.startswith("Acheck:"):
            continue
        _, label, scale, lag = key.split(":")
        scale, lag = int(scale), int(lag)
        if lag != 0:
            group = amplitude_checks.setdefault(f"{label}:{scale}", {})
            group[str(lag)] = frame[key]["mean"]
    for group in amplitude_checks.values():
        series = [group[lag] for lag in sorted(group, key=int)]
        group["negative_point_estimate"] = any(x < 0 for x in series)
        group["monotonicity_point_estimate_flag"] = any(y > x for x, y in zip(series, series[1:]))
    return {
        "status": "descriptive-complete", "values": frame, "amplitude_checks": amplitude_checks,
        "paired_raw_state_covariance": {"keys": [keys[i] for i in primary],
                                        "matrix": covariance.tolist()},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--volume", required=True, choices=VOLUMES, type=int)
    parser.add_argument("--receipts", required=True, type=Path)
    parser.add_argument("measurement_jsonl", type=Path)
    args = parser.parse_args()
    thermal = json.loads(args.receipts.read_text(encoding="utf-8")).get(str(args.volume), {})
    endpoint = thermal.get("endpoint")
    if endpoint not in ENDPOINTS:
        result = {"status": "no-accepted-thermal-endpoint"}
    else:
        keys, values = load_values(args.measurement_jsonl, args.volume, endpoint)
        result = report(keys, values) if values is not None else {"status": "incomplete"}
    print(json.dumps({"L": args.volume, **result}, allow_nan=False, indent=2))


if __name__ == "__main__":
    main()
