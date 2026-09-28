#!/usr/bin/env python3
"""Frozen engineering analysis, NON-CANONICAL; no rigorous coverage claim.

Input: the untouched run_pilot.py output directory and its execution manifest.
Output: JSON retaining all chain estimates, including failed diagnostics.
No phase, scaling, thermodynamic, or P1 verdict is implemented here.
"""

import argparse
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import statistics
import sys


L_VALUES = (4, 6, 8)
MODES = (1, 2)
CHAINS = (0, 1, 2, 3)
INITIAL = {0: "cold0", 1: "hot0", 2: "cold1", 3: "hot1"}
BLOCKS = 32
BLOCK_LENGTH = 128
MULTIPLIER = 4.0
THRESHOLDS = {
    "empirical_se_multiplier": MULTIPLIER,
    "maximum_signed_interval_halfwidth": 0.05,
    "minimum_each_endpoint_sweeps_per_chain": 256,
    "minimum_endpoint_changes_per_chain": 16,
    "minimum_completed_roundtrips_per_chain": 8,
    "minimum_final_each_edge_swap_acceptance": 0.05,
    "maximum_se_coarsening_ratio": 2.0,
    "block_lengths": [128, 256, 512],
    "minimum_expected_p0": 0.5,
}
INTEGER_FIELDS = {
    "L", "k", "chain", "block", "n", "n0",
    "target_flip_attempts", "target_flip_accepts", "swap_attempts",
    "swap_accepts", "roundtrips", "target_endpoint_changes",
}
FLOAT_FIELDS = {
    "sumT", "sumT2", "sumY0", "sumY0sq", "sum_action", "sum_action2",
    "min_swap_accept",
}
FIELDS = INTEGER_FIELDS | FLOAT_FIELDS


class InvalidInput(Exception):
    pass


def require(condition, message):
    if not condition:
        raise InvalidInput(message)


def finite_number(text, where):
    try:
        number = float(text)
    except (TypeError, ValueError) as exc:
        raise InvalidInput(f"{where}: invalid number") from exc
    require(math.isfinite(number), f"{where}: nonfinite number")
    return number


def nonnegative_integer(text, where):
    try:
        number = int(text)
    except (TypeError, ValueError) as exc:
        raise InvalidInput(f"{where}: invalid integer") from exc
    require(number >= 0, f"{where}: negative integer")
    return number


def read_run(path):
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise InvalidInput(f"{path.name}: invalid UTF-8") from exc
    metadata = {}
    edges = {}
    replica_roundtrips = {}
    lines = []
    for line_number, line in enumerate(text.splitlines(), 1):
        if line.startswith("#"):
            parts = line[1:].lstrip().split("\t")
            require(len(parts) >= 2, f"{path.name}:{line_number}: malformed metadata")
            if parts[0] == "swap_edge":
                require(len(parts) == 4, f"{path.name}: malformed swap_edge")
                index, attempts, accepts = [
                    nonnegative_integer(v, f"{path.name}:swap_edge")
                    for v in parts[1:]
                ]
                require(index not in edges, f"{path.name}: duplicate swap edge")
                require(0 <= accepts <= attempts, f"{path.name}: invalid swap counts")
                edges[index] = (attempts, accepts)
            elif parts[0] == "replica_roundtrips":
                require(len(parts) == 3, f"{path.name}: malformed replica_roundtrips")
                replica, count = [nonnegative_integer(v, f"{path.name}:replica_roundtrips")
                                  for v in parts[1:]]
                require(replica not in replica_roundtrips,
                        f"{path.name}: duplicate replica roundtrip record")
                replica_roundtrips[replica] = count
            else:
                require(parts[0] not in metadata, f"{path.name}: duplicate metadata key")
                metadata[parts[0]] = "\t".join(parts[1:])
        elif line.strip():
            lines.append(line)
    require(lines, f"{path.name}: absent table")
    reader = csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t")
    require(reader.fieldnames is not None, f"{path.name}: absent header")
    require(len(reader.fieldnames) == len(set(reader.fieldnames)),
            f"{path.name}: duplicate header field")
    require(set(reader.fieldnames) == FIELDS, f"{path.name}: unexpected TSV schema")
    blocks = []
    key = None
    for index, source in enumerate(reader):
        require(None not in source and None not in source.values(),
                f"{path.name}: malformed row")
        row = {}
        for field in INTEGER_FIELDS:
            row[field] = nonnegative_integer(source[field], f"{path.name}:{field}")
        for field in FLOAT_FIELDS:
            row[field] = finite_number(source[field], f"{path.name}:{field}")
        current = (row["L"], row["k"], row["chain"])
        require(current[0] in L_VALUES and current[1] in MODES and current[2] in CHAINS,
                f"{path.name}: unexpected run key")
        if key is None:
            key = current
        require(current == key, f"{path.name}: multiple run keys")
        require(row["block"] == index, f"{path.name}: blocks missing or unordered")
        require(row["n"] == BLOCK_LENGTH, f"{path.name}: unexpected block length")
        require(row["n0"] <= row["n"], f"{path.name}: n0 > n")
        require(row["target_endpoint_changes"] <= row["n"],
                f"{path.name}: too many observed endpoint changes")
        for stem in ("target_flip", "swap"):
            require(row[f"{stem}_accepts"] <= row[f"{stem}_attempts"],
                    f"{path.name}: accepted count exceeds attempts")
        require(0 <= row["min_swap_accept"] <= 1,
                f"{path.name}: invalid min_swap_accept")
        for first, second, count in (
            ("sumT", "sumT2", row["n"] - row["n0"]),
            ("sumY0", "sumY0sq", row["n0"]),
            ("sum_action", "sum_action2", row["n"]),
        ):
            require(row[second] >= 0, f"{path.name}: negative second moment")
            tolerance = 1e-8 * max(1.0, row[first] ** 2, count * row[second])
            require(row[first] ** 2 <= count * row[second] + tolerance,
                    f"{path.name}: inconsistent first and second moments")
            if count == 0:
                require(abs(row[first]) <= 1e-12 and abs(row[second]) <= 1e-12,
                        f"{path.name}: nonzero moment on empty endpoint")
        blocks.append(row)
    require(len(blocks) == BLOCKS, f"{path.name}: expected exactly {BLOCKS} blocks")
    require(metadata.get("chain_initial") == INITIAL[key[2]],
            f"{path.name}: missing or incorrect chain_initial")
    required_metadata = {
        "format": "twist_endpoint_blocks_v1", "L": str(key[0]),
        "k": str(key[1]), "chain": str(key[2]),
        "seed": str(202609270000 + 1000 * key[0] + 100 * key[1] + key[2]),
        "replicas": str(2 * key[0] + 1), "warmup_sweeps": "512",
        "production_sweeps": "4096", "block_length": "128",
        "endpoint_proposal_probability": "0.5",
        "sampling": "every_production_sweep_after_local_endpoint_and_exchange_updates",
        "completion": "PASS",
    }
    for field, value in required_metadata.items():
        require(metadata.get(field) == value, f"{path.name}: incorrect {field}")
    require("beta_ladder" in metadata, f"{path.name}: missing beta_ladder")
    ladder = [finite_number(v, f"{path.name}:beta_ladder")
              for v in metadata["beta_ladder"].split(",")]
    expected_ladder = [j / (2 * key[0]) for j in range(2 * key[0] + 1)]
    require(ladder == expected_ladder, f"{path.name}: beta ladder differs from frozen ladder")
    require(set(edges) == set(range(len(ladder) - 1)),
            f"{path.name}: missing or extra swap edges")
    require(set(replica_roundtrips) == set(range(len(ladder))),
            f"{path.name}: missing or extra replica roundtrip records")
    require(sum(replica_roundtrips.values()) == sum(b["roundtrips"] for b in blocks),
            f"{path.name}: replica roundtrip totals disagree")
    require(sum(a for a, _ in edges.values()) == sum(b["swap_attempts"] for b in blocks),
            f"{path.name}: swap attempt totals disagree")
    require(sum(a for _, a in edges.values()) == sum(b["swap_accepts"] for b in blocks),
            f"{path.name}: swap acceptance totals disagree")
    return {
        "key": key, "blocks": blocks, "edges": edges, "metadata": metadata,
        "replica_roundtrips": replica_roundtrips,
        "file": path.name, "sha256": hashlib.sha256(raw).hexdigest(),
    }


def se_of_mean(values):
    if len(values) < 2:
        raise InvalidInput("not enough batch means")
    return statistics.stdev(values) / math.sqrt(len(values))


def coarsen(blocks, factor):
    require(len(blocks) % factor == 0, "incomplete coarsening group")
    result = []
    for start in range(0, len(blocks), factor):
        group = blocks[start:start + factor]
        result.append({
            "n": sum(b["n"] for b in group),
            "n0": sum(b["n0"] for b in group),
            "sumT": math.fsum(b["sumT"] for b in group),
        })
    return result


def ratio_summary(chains):
    """Coarsen inside each independent chain, never across its boundary."""
    all_blocks = [b for chain in chains for b in chain]
    count = sum(b["n"] for b in all_blocks)
    n0 = sum(b["n0"] for b in all_blocks)
    p0 = n0 / count
    tmean = math.fsum(b["sumT"] for b in all_blocks) / count
    if p0 == 0:
        return {"mean": None, "p0": p0, "mean_T": tmean, "se": None,
                "se_by_block_length": {}, "chain_residual_se": None,
                "p0_se": None, "halfwidth": None, "interval": None}
    estimate = tmean / p0
    errors = {}
    denominator_errors = []
    for factor in (1, 2, 4):
        batches = [b for chain in chains for b in coarsen(chain, factor)]
        residual = [(b["sumT"] - estimate * b["n0"]) / b["n"] for b in batches]
        errors[str(BLOCK_LENGTH * factor)] = se_of_mean(residual) / p0
        denominator_errors.append(se_of_mean([b["n0"] / b["n"] for b in batches]))
    chain_error = None
    if len(chains) > 1:
        residual = []
        fractions = []
        for blocks in chains:
            n = sum(b["n"] for b in blocks)
            nz = sum(b["n0"] for b in blocks)
            ts = math.fsum(b["sumT"] for b in blocks)
            residual.append((ts - estimate * nz) / n)
            fractions.append(nz / n)
        chain_error = se_of_mean(residual) / p0
        denominator_errors.append(se_of_mean(fractions))
    error = max(list(errors.values()) + ([chain_error] if chain_error is not None else []))
    halfwidth = MULTIPLIER * error
    return {
        "mean": estimate, "p0": p0, "mean_T": tmean, "se": error,
        "se_by_block_length": errors, "chain_residual_se": chain_error,
        "p0_se": max(denominator_errors), "halfwidth": halfwidth,
        "interval": [estimate - halfwidth, estimate + halfwidth],
    }


def four_se_agreement(first, second):
    """Do not let observed between-chain spread inflate its own gate."""
    if first["mean"] is None or second["mean"] is None:
        return False
    first_error = max(first["se_by_block_length"].values())
    second_error = max(second["se_by_block_length"].values())
    tolerance = MULTIPLIER * math.hypot(first_error, second_error)
    return abs(first["mean"] - second["mean"]) <= tolerance


def analyze_mode(runs):
    pooled = ratio_summary([run["blocks"] for run in runs])
    failures = []
    chain_results = []
    for run in runs:
        blocks = run["blocks"]
        chain = run["key"][2]
        prefix = f"chain_{chain}:"
        estimate = ratio_summary([blocks])
        halves = [ratio_summary([blocks[:BLOCKS // 2]]),
                  ratio_summary([blocks[BLOCKS // 2:]])]
        n0 = sum(b["n0"] for b in blocks)
        n = sum(b["n"] for b in blocks)
        changes = sum(b["target_endpoint_changes"] for b in blocks)
        roundtrips = sum(b["roundtrips"] for b in blocks)
        edge_acceptance = [accepted / attempted if attempted else 0.0
                           for _, (attempted, accepted) in sorted(run["edges"].items())]
        if min(n0, n - n0) < THRESHOLDS["minimum_each_endpoint_sweeps_per_chain"]:
            failures.append(prefix + "endpoint_occupancy")
        if changes < THRESHOLDS["minimum_endpoint_changes_per_chain"]:
            failures.append(prefix + "endpoint_changes")
        if roundtrips < THRESHOLDS["minimum_completed_roundtrips_per_chain"]:
            failures.append(prefix + "roundtrips")
        if min(edge_acceptance) < THRESHOLDS["minimum_final_each_edge_swap_acceptance"]:
            failures.append(prefix + "adjacent_swap_acceptance")
        if not four_se_agreement(estimate, pooled):
            failures.append(prefix + "between_chain_disagreement")
        if not four_se_agreement(*halves):
            failures.append(prefix + "time_half_disagreement")
        if estimate["p0_se"] is None or estimate["p0"] + MULTIPLIER * estimate["p0_se"] < 0.5:
            failures.append(prefix + "denominator_below_equilibrium_bound")
        chain_results.append({
            "chain": chain, "initial": INITIAL[chain],
            "label": "NONINFERENTIAL_ESTIMATE", "estimate": estimate,
            "time_halves": halves, "endpoint_occupancy": [n0, n - n0],
            "endpoint_changes": changes, "roundtrips": roundtrips,
            "roundtrips_by_replica": run["replica_roundtrips"],
            "edge_acceptance": edge_acceptance,
            "descriptive_moments_only": {
                "mean_T_squared": math.fsum(b["sumT2"] for b in blocks) / n,
                "mean_Y0": math.fsum(b["sumY0"] for b in blocks) / n,
                "mean_Y0_squared": math.fsum(b["sumY0sq"] for b in blocks) / n,
                "mean_action": math.fsum(b["sum_action"] for b in blocks) / n,
            },
            "input_file": run["file"], "input_sha256": run["sha256"],
        })
    errors = list(pooled["se_by_block_length"].values())
    degenerate_variance = bool(errors) and max(errors) == 0
    if not errors:
        failures.append("pooled:missing_batch_variance")
        stability_ratio = None
    elif degenerate_variance:
        stability_ratio = None
    elif min(errors) <= 0:
        failures.append("pooled:batch_coarsening_instability")
        stability_ratio = None
    else:
        stability_ratio = max(errors) / min(errors)
        if stability_ratio > THRESHOLDS["maximum_se_coarsening_ratio"]:
            failures.append("pooled:batch_coarsening_instability")
    width_pass = (not degenerate_variance and pooled["halfwidth"] is not None and
                  pooled["halfwidth"] <= THRESHOLDS["maximum_signed_interval_halfwidth"])
    excludes_zero = (pooled["interval"] is not None and
                     (pooled["interval"][0] > 0 or pooled["interval"][1] < 0))
    return {
        "k": runs[0]["key"][1], "pooled": pooled, "chains": chain_results,
        "diagnostic_failures": failures, "mobility_and_stability_pass": not failures,
        "coarsening_se_ratio": stability_ratio, "width_pass": width_pass,
        "degenerate_batch_variance": degenerate_variance,
        "signed_interval_excludes_zero": excludes_zero,
        "estimate_label": "EMPIRICAL_ENGINEERING_ONLY" if not failures else "NONINFERENTIAL_ESTIMATE",
    }


def square_interval(interval):
    low, high = interval
    nearest = 0.0 if low <= 0 <= high else min(low * low, high * high)
    return nearest, max(low * low, high * high)


def report(runs):
    result = {
        "analysis": "C-PHOTON-TWIST-ENDPOINT-DIAGNOSTIC-N",
        "status": "INCOMPLETE", "thresholds": THRESHOLDS,
        "scope": "NON-CANONICAL engineering diagnostics of finite-volume signed ratios",
        "coverage": "4SE intervals are empirical; no rigorous or simultaneous coverage is claimed",
        "limitations": [
            "Passing mobility gates does not prove equilibration or decorrelation.",
            "No thermodynamic, phase, scaling, or P1 verdict is produced.",
            "Squared ranges are formed from signed intervals, not squared noisy point estimates.",
            "All chain estimates remain visible even when inference is withheld.",
        ],
        "missing_runs": [], "volumes": [],
    }
    indexed = {}
    for run in runs:
        require(run["key"] not in indexed, f"duplicate run {run['key']}")
        indexed[run["key"]] = run
    expected = [(size, mode, chain) for size in L_VALUES for mode in MODES for chain in CHAINS]
    result["missing_runs"] = [list(key) for key in expected if key not in indexed]
    result["available_run_count"] = len(runs)
    for size in L_VALUES:
        if not all((size, mode, chain) in indexed for mode in MODES for chain in CHAINS):
            partial = [run for run in runs if run["key"][0] == size]
            result["volumes"].append({
                "L": size, "status": "INCOMPLETE", "available_chains": [
                    {"k": run["key"][1], "chain": run["key"][2],
                     "label": "NONINFERENTIAL_ESTIMATE",
                     "estimate": ratio_summary([run["blocks"]]),
                     "input_file": run["file"], "input_sha256": run["sha256"]}
                    for run in sorted(partial, key=lambda item: item["key"])
                ],
            })
            continue
        modes = [analyze_mode([indexed[(size, mode, chain)] for chain in CHAINS])
                 for mode in MODES]
        volume = {"L": size, "modes": modes}
        mobility_pass = all(item["mobility_and_stability_pass"] for item in modes)
        if not mobility_pass:
            volume["status"] = "INCONCLUSIVE_MOBILITY"
            volume["D_empirical_engineering_interval"] = None
        elif any(item["degenerate_batch_variance"] for item in modes):
            volume["status"] = "UNRESOLVED"
            volume["D_empirical_engineering_interval"] = None
        else:
            squared = [square_interval(item["pooled"]["interval"]) for item in modes]
            volume["D_empirical_engineering_interval"] = [
                math.fsum(pair[0] for pair in squared), math.fsum(pair[1] for pair in squared),
            ]
            if all(item["width_pass"] for item in modes) and any(
                    item["signed_interval_excludes_zero"] for item in modes):
                volume["status"] = "RESOLVED_SIGNED_CONTRAST"
            else:
                volume["status"] = "UNRESOLVED"
        result["volumes"].append(volume)
    statuses = [item["status"] for item in result["volumes"]]
    if result["missing_runs"]:
        result["status"] = "INCOMPLETE"
    elif "INCONCLUSIVE_MOBILITY" in statuses:
        result["status"] = "INCONCLUSIVE_MOBILITY"
    elif all(status == "RESOLVED_SIGNED_CONTRAST" for status in statuses):
        result["status"] = "RESOLVED_SIGNED_CONTRAST"
    else:
        result["status"] = "UNRESOLVED"
    return result


def read_execution(directory):
    """Validate process outcomes and custody before admitting scientific output."""
    manifest_path = directory / "execution.json"
    try:
        records = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeError) as exc:
        raise InvalidInput("malformed execution.json") from exc
    require(isinstance(records, list), "execution.json must contain a list")
    expected_stems = {
        f"L{size}_k{mode}_c{chain}": (size, mode, chain)
        for size in L_VALUES for mode in MODES for chain in CHAINS
    }
    seen = set()
    runs = []
    errors = []
    for record in records:
        if not isinstance(record, dict):
            errors.append("malformed execution record")
            continue
        stem = record.get("stem")
        if not isinstance(stem, str) or stem not in set(expected_stems) | {"audit"} or stem in seen:
            errors.append("unexpected or duplicate execution stem")
            continue
        seen.add(stem)
        try:
            code = record["exit_code"]
            require(type(code) is int, f"{stem}: invalid exit code")
            for suffix, size_key, hash_key in (
                ("tsv", "stdout_bytes", "stdout_sha256"),
                ("stderr", "stderr_bytes", "stderr_sha256"),
            ):
                raw = (directory / f"{stem}.{suffix}").read_bytes()
                require(type(record.get(size_key)) is int and record[size_key] == len(raw),
                        f"{stem}: {size_key} mismatch")
                require(record.get(hash_key) == hashlib.sha256(raw).hexdigest(),
                        f"{stem}: {hash_key} mismatch")
            require(code == 0 and record["stderr_bytes"] == 0,
                    f"{stem}: nonzero exit or nonempty stderr")
            if stem == "audit":
                audit = (directory / "audit.tsv").read_text(encoding="utf-8")
                expected_audit = (
                    "NON-CANONICAL floating-point engineering audit\n"
                    "geometries\t3\nfixture_states\t12\nmutations_caught\t24\nresult\tPASS\n"
                )
                require(audit == expected_audit, "audit: unexpected output")
        except (InvalidInput, OSError, UnicodeError, KeyError) as exc:
            errors.append(str(exc))
        if stem != "audit":
            try:
                run = read_run(directory / f"{stem}.tsv")
                require(run["key"] == expected_stems[stem], f"{stem}: run key mismatch")
                runs.append(run)
            except (InvalidInput, OSError, UnicodeError) as exc:
                errors.append(str(exc))
    if "audit" not in seen:
        errors.append("missing audit execution record")
    result = report(runs)
    result["execution_manifest_sha256"] = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
    result["execution_errors"] = errors
    if errors:
        result["status"] = "FAIL_IMPLEMENTATION"
        for volume in result["volumes"]:
            volume["status"] = "FAIL_IMPLEMENTATION"
            volume["D_empirical_engineering_interval"] = None
            for mode in volume.get("modes", []):
                mode["estimate_label"] = "NONINFERENTIAL_ESTIMATE"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_directory", type=Path, help="untouched run_pilot.py output directory")
    args = parser.parse_args()
    try:
        result = read_execution(args.output_directory)
    except (InvalidInput, OSError, ArithmeticError, ValueError) as exc:
        result = {"status": "FAIL_IMPLEMENTATION", "reason": str(exc),
                  "scope": "malformed or inaccessible diagnostic input; no scientific inference"}
    print(json.dumps(result, indent=2, sort_keys=True, allow_nan=False))
    if result["status"] == "FAIL_IMPLEMENTATION":
        return 2
    if result["status"] == "INCOMPLETE":
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
