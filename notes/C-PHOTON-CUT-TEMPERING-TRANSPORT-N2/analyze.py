#!/usr/bin/env python3
"""Frozen transport-only engineering analysis; NON-CANONICAL, no inference.

Read the untouched controller output and retain every available chain.
No signed confidence interval, squared contrast, phase or P1 verdict is made.
The 4-SE comparisons below are empirical diagnostics without coverage claims.
Adapted from the publicly consumed C-PHOTON-TWIST-ENDPOINT-DIAGNOSTIC-N.
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


ITEM = "C-PHOTON-CUT-TEMPERING-TRANSPORT-N2"
L_VALUES = (4,)
MODES = (1, 2)
BASES = (0, 2)
CHAINS = (0, 1, 2, 3, 4)
INITIAL = {0: "cold0", 1: "hot0", 2: "cold1", 3: "hot1", 4: "alt1"}
BLOCK_LENGTH = 128
BLOCKS = 128
REPLICAS = 65
MULTIPLIER = 4.0
SCALES = (1, 2, 4, 8)
AUDIT_TEXT = "NON-CANONICAL floating-point engineering audit\nresult\tPASS\n"
TEST_TEXT = "NON-CANONICAL analyzer fixture audit\nresult\tPASS\n"
THRESHOLDS = {
    "empirical_se_multiplier": MULTIPLIER,
    "minimum_each_endpoint_sweeps_per_chain": 1024,
    "minimum_endpoint_changes_per_chain": 64,
    "minimum_completed_roundtrips_per_chain": 8,
    "minimum_final_each_edge_swap_acceptance": 0.10,
    "maximum_pooled_se_coarsening_ratio": 2.0,
    "block_lengths": [BLOCK_LENGTH * factor for factor in SCALES],
    "zero_error_rule": "p0,Y0,Y1 unresolved; winding metrics allowed if agreement passes",
}
INTEGER_FIELDS = {
    "L", "k", "base", "chain", "block", "n", "n0", "nTpos", "nTneg",
    "target_T_sign_changes", "target_flip_attempts", "target_flip_accepts",
    "target_endpoint_changes", "swap_attempts", "swap_accepts", "roundtrips",
}
FLOAT_FIELDS = {
    "sumT", "sumT2", "sumY0", "sumY0sq", "sumPosT", "sumNegT",
    "sumW1", "sumW0", "sumM1", "sumM0", "sumP1", "sumP0",
    "sum_action", "sum_action2", "min_swap_accept",
}
FIELDS = INTEGER_FIELDS | FLOAT_FIELDS
# Numerators and denominators are block sufficient sums. A tuple is a sum.
METRICS = {
    "p0": ("n0", "n"),
    "Y0": ("sumY0", "n0"),
    "Y1": ("sumT", "n1"),
    "W0": ("sumW0", "n0"),
    "W1": ("sumW1", "n1"),
    "M0": ("sumM0", "n0"),
    "M1": ("sumM1", "n1"),
    "P0": ("sumP0", "n0"),
    "P1": ("sumP1", "n1"),
    "Y_unconditional": (("sumY0", "sumT"), "n"),
    "signed_ratio": ("sumT", "n0"),
    "positive_ratio_part": ("sumPosT", "n0"),
    "negative_ratio_part": ("sumNegT", "n0"),
}
GATE_METRICS = ("p0", "Y0", "Y1", "W0", "W1", "M0", "M1", "P0", "P1")
CORE_METRICS = ("p0", "Y0", "Y1")


class InvalidInput(Exception):
    pass


def require(condition, message):
    if not condition:
        raise InvalidInput(message)


def finite_number(value, where):
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise InvalidInput(f"{where}: invalid number") from exc
    require(math.isfinite(number), f"{where}: nonfinite number")
    return number


def nonnegative_integer(value, where):
    try:
        number = int(value)
    except (TypeError, ValueError) as exc:
        raise InvalidInput(f"{where}: invalid integer") from exc
    require(number >= 0, f"{where}: negative integer")
    return number


def expected_keys():
    return [(size, mode, base, chain) for size in L_VALUES for mode in MODES
            for base in BASES for chain in CHAINS]


def stem_for(key):
    size, mode, base, chain = key
    return f"L{size}_k{mode}_b{base}_c{chain}"


def read_run(path):
    raw = path.read_bytes()
    try:
        source_text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise InvalidInput(f"{path.name}: invalid UTF-8") from exc
    metadata, edges, replica_roundtrips, lines = {}, {}, {}, []
    for line_number, line in enumerate(source_text.splitlines(), 1):
        if line.startswith("#"):
            parts = line[1:].lstrip().split("\t")
            require(len(parts) >= 2, f"{path.name}:{line_number}: malformed metadata")
            if parts[0] == "swap_edge":
                require(len(parts) == 4, f"{path.name}: malformed swap_edge")
                index, attempts, accepts = [nonnegative_integer(v, path.name)
                                             for v in parts[1:]]
                require(index not in edges, f"{path.name}: duplicate swap edge")
                require(accepts <= attempts, f"{path.name}: invalid swap counts")
                edges[index] = (attempts, accepts)
            elif parts[0] == "replica_roundtrips":
                require(len(parts) == 3, f"{path.name}: malformed replica_roundtrips")
                replica, count = [nonnegative_integer(v, path.name) for v in parts[1:]]
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
    blocks, key = [], None
    for index, source in enumerate(reader):
        require(None not in source and None not in source.values(),
                f"{path.name}: malformed row")
        row = {field: nonnegative_integer(source[field], f"{path.name}:{field}")
               for field in INTEGER_FIELDS}
        row.update({field: finite_number(source[field], f"{path.name}:{field}")
                    for field in FLOAT_FIELDS})
        current = (row["L"], row["k"], row["base"], row["chain"])
        require(current in expected_keys(), f"{path.name}: unexpected run key")
        if key is None:
            key = current
        require(current == key, f"{path.name}: multiple run keys")
        require(row["block"] == index, f"{path.name}: blocks missing or unordered")
        require(row["n"] == BLOCK_LENGTH, f"{path.name}: unexpected block length")
        require(row["n0"] <= row["n"], f"{path.name}: n0 > n")
        n1 = row["n"] - row["n0"]
        require(row["nTpos"] + row["nTneg"] <= n1,
                f"{path.name}: sign counts exceed endpoint-one observations")
        require(row["target_T_sign_changes"] <= row["nTpos"] + row["nTneg"],
                f"{path.name}: too many sign changes")
        require(row["target_endpoint_changes"] <= row["n"],
                f"{path.name}: too many endpoint changes")
        require(row["target_flip_attempts"] <= row["n"],
                f"{path.name}: too many target endpoint proposals")
        for name in ("target_flip", "swap"):
            require(row[f"{name}_accepts"] <= row[f"{name}_attempts"],
                    f"{path.name}: accepted count exceeds attempts")
        require(row["swap_attempts"] == BLOCK_LENGTH * (REPLICAS - 1) // 2,
                f"{path.name}: wrong block swap-attempt count")
        require(0 <= row["min_swap_accept"] <= 1,
                f"{path.name}: invalid min_swap_accept")
        for first, second, count in (("sumT", "sumT2", n1),
                                    ("sumY0", "sumY0sq", row["n0"]),
                                    ("sum_action", "sum_action2", row["n"])):
            require(row[second] >= 0, f"{path.name}: negative second moment")
            tolerance = 1e-8 * max(1.0, row[first] ** 2, count * row[second])
            require(row[first] ** 2 <= count * row[second] + tolerance,
                    f"{path.name}: inconsistent first and second moments")
            if count == 0:
                require(abs(row[first]) <= 1e-12 and abs(row[second]) <= 1e-12,
                        f"{path.name}: nonzero moment on empty endpoint")
        require(row["sumPosT"] >= 0 and row["sumNegT"] >= 0,
                f"{path.name}: negative sign-part magnitude")
        tolerance = 1e-8 * max(1.0, row["sumPosT"] + row["sumNegT"])
        require(abs(row["sumT"] - row["sumPosT"] + row["sumNegT"]) <= tolerance,
                f"{path.name}: sign-split mismatch")
        for part, count_name in (("sumPosT", "nTpos"), ("sumNegT", "nTneg")):
            if row[count_name] == 0:
                require(row[part] <= 1e-12, f"{path.name}: sign sum with zero sign count")
        max_w = math.ceil((2 * row["L"] ** 2 + 2) / 5)
        for endpoint, count in ((0, row["n0"]), (1, n1)):
            winding = row[f"sumW{endpoint}"]
            minus, plus = row[f"sumM{endpoint}"], row[f"sumP{endpoint}"]
            tolerance = 1e-8 * max(1, count)
            require(min(minus, plus) >= 0 and minus + plus <= count + tolerance,
                    f"{path.name}: invalid slice sign fractions")
            require(plus - max_w * minus - tolerance <= winding
                    <= max_w * plus - minus + tolerance,
                    f"{path.name}: winding and sign fractions disagree")
            if count == 0:
                require(abs(winding) <= 1e-12 and minus <= 1e-12 and plus <= 1e-12,
                        f"{path.name}: winding record on empty endpoint")
        blocks.append(row)
    require(len(blocks) == BLOCKS, f"{path.name}: expected exactly {BLOCKS} blocks")
    required_metadata = {
        "format": "twist_cut_transport_blocks_v1", "L": str(key[0]),
        "k": str(key[1]), "base": str(key[2]), "chain": str(key[3]),
        "seed": str(202609280000 + 10000 * key[2] + 1000 * key[0]
                    + 100 * key[1] + key[3]),
        "replicas": str(REPLICAS), "warmup_sweeps": "2048",
        "production_sweeps": "16384", "block_length": str(BLOCK_LENGTH),
        "chain_initial": INITIAL[key[3]], "endpoint_proposal_probability": "0.5",
        "sampling": "every_production_sweep_after_local_sheet_endpoint_and_exchange_updates",
        "cut": "all_01_plaquettes_x0_equals_0",
        "sheet_orbits": "all_x1_slices_every_replica_every_sweep",
        "completion": "PASS",
    }
    for field, value in required_metadata.items():
        require(metadata.get(field) == value, f"{path.name}: incorrect {field}")
    require("lambda_ladder" in metadata, f"{path.name}: missing lambda_ladder")
    ladder = [finite_number(value, f"{path.name}:lambda_ladder")
              for value in metadata["lambda_ladder"].split(",")]
    require(ladder == [j / 64 for j in range(REPLICAS)],
            f"{path.name}: lambda ladder differs from frozen ladder")
    require(set(edges) == set(range(REPLICAS - 1)),
            f"{path.name}: missing or extra swap edges")
    require(set(replica_roundtrips) == set(range(REPLICAS)),
            f"{path.name}: missing or extra replica roundtrip records")
    require(all(attempts == BLOCK_LENGTH * BLOCKS // 2 for attempts, _ in edges.values()),
            f"{path.name}: wrong per-edge swap-attempt count")
    require(sum(replica_roundtrips.values()) == sum(b["roundtrips"] for b in blocks),
            f"{path.name}: replica roundtrip totals disagree")
    require(sum(a for a, _ in edges.values()) == sum(b["swap_attempts"] for b in blocks),
            f"{path.name}: swap attempt totals disagree")
    require(sum(a for _, a in edges.values()) == sum(b["swap_accepts"] for b in blocks),
            f"{path.name}: swap acceptance totals disagree")
    return {"key": key, "blocks": blocks, "edges": edges, "metadata": metadata,
            "replica_roundtrips": replica_roundtrips, "file": path.name,
            "sha256": hashlib.sha256(raw).hexdigest()}


def se_of_mean(values):
    require(len(values) >= 2, "not enough batch means")
    return statistics.stdev(values) / math.sqrt(len(values))


def value_of(block, spec):
    if spec == "n1":
        return block["n"] - block["n0"]
    if isinstance(spec, tuple):
        return math.fsum(block[field] for field in spec)
    return block[spec]


def sums_for(blocks, metric):
    numerator, denominator = METRICS[metric]
    return (math.fsum(value_of(block, numerator) for block in blocks),
            math.fsum(value_of(block, denominator) for block in blocks),
            sum(block["n"] for block in blocks))


def ratio_summary(chains, metric):
    """Delta-method batch residuals; coarsening never crosses a chain boundary."""
    totals = [sums_for(blocks, metric) for blocks in chains]
    numerator = math.fsum(row[0] for row in totals)
    denominator = math.fsum(row[1] for row in totals)
    count = sum(row[2] for row in totals)
    result = {"mean": None, "numerator": numerator, "denominator": denominator,
              "observations": count, "se_by_block_length": {}, "batch_se": None,
              "chain_residual_se": None, "descriptive_se": None,
              "four_batch_se": None, "label": "NONINFERENTIAL_ESTIMATE"}
    if denominator <= 0:
        return result
    estimate = numerator / denominator
    denominator_mean = denominator / count
    errors = {}
    for factor in SCALES:
        variance_terms, batch_count = [], 0
        for blocks in chains:
            require(len(blocks) % factor == 0, "incomplete coarsening group")
            residuals = []
            for start in range(0, len(blocks), factor):
                num, den, n = sums_for(blocks[start:start + factor], metric)
                residuals.append((num - estimate * den) / n)
            require(len(residuals) >= 2, "not enough within-chain batch means")
            # Center each chain separately: variation among chain means must
            # not inflate the batch error used for leave-one-out agreement.
            variance_terms.append(len(residuals) * statistics.variance(residuals))
            batch_count += len(residuals)
        errors[str(BLOCK_LENGTH * factor)] = (math.sqrt(math.fsum(variance_terms))
                                              / batch_count / denominator_mean)
    chain_error = None
    if len(chains) > 1:
        chain_error = se_of_mean([(num - estimate * den) / n for num, den, n in totals])
        chain_error /= denominator_mean
    batch_error = max(errors.values())
    result.update(mean=estimate, se_by_block_length=errors, batch_se=batch_error,
                  chain_residual_se=chain_error,
                  descriptive_se=max(batch_error, chain_error or 0.0),
                  four_batch_se=MULTIPLIER * batch_error)
    return result


def four_se_agreement(first, second):
    if first["mean"] is None or second["mean"] is None:
        return False
    # Neither between-chain spread nor a paired correlated pool is used here.
    tolerance = MULTIPLIER * math.hypot(first["batch_se"], second["batch_se"])
    return abs(first["mean"] - second["mean"]) <= tolerance


def coarsening(summary, metric):
    errors = list(summary["se_by_block_length"].values())
    if not errors:
        return {"pass": False, "ratio": None, "reason": "missing_batch_variance"}
    if max(errors) == 0:
        allowed = metric not in CORE_METRICS
        return {"pass": allowed, "ratio": None,
                "reason": "zero_winding_error_allowed" if allowed else "zero_core_error_unresolved"}
    if min(errors) <= 0:
        return {"pass": False, "ratio": None, "reason": "mixed_zero_and_positive_errors"}
    ratio = max(errors) / min(errors)
    return {"pass": ratio <= THRESHOLDS["maximum_pooled_se_coarsening_ratio"],
            "ratio": ratio, "reason": "pooled_scale_comparison"}


def identity_residual(summary, target, one_sided=False):
    mean, error = summary["mean"], summary["batch_se"]
    residual = None if mean is None else mean - target
    would_pass = (mean is not None and error is not None and
                  (residual >= -MULTIPLIER * error if one_sided
                   else abs(residual) <= MULTIPLIER * error))
    return {"mean": mean, "target": target, "residual": residual,
            "batch_se": error, "four_batch_se": None if error is None else MULTIPLIER * error,
            "comparison": "lower_bound" if one_sided else "equality",
            "would_pass": would_pass, "evaluated_after_mobility": False}


def analyze_group(runs):
    key = runs[0]["key"][:3]
    pooled = {metric: ratio_summary([run["blocks"] for run in runs], metric)
              for metric in METRICS}
    failures, chain_results = [], []
    for run in runs:
        blocks, chain = run["blocks"], run["key"][3]
        prefix = f"chain_{chain}:"
        others = [other["blocks"] for other in runs if other["key"][3] != chain]
        estimates = {metric: ratio_summary([blocks], metric) for metric in METRICS}
        half_estimates = [{metric: ratio_summary([half], metric) for metric in GATE_METRICS}
                          for half in (blocks[:BLOCKS // 2], blocks[BLOCKS // 2:])]
        leave_one_out = {metric: ratio_summary(others, metric) for metric in GATE_METRICS}
        agreements = {}
        for metric in GATE_METRICS:
            between = four_se_agreement(estimates[metric], leave_one_out[metric])
            halves = four_se_agreement(half_estimates[0][metric], half_estimates[1][metric])
            agreements[metric] = {"leave_one_out_pass": between, "halves_pass": halves}
            if not between:
                failures.append(prefix + metric + ":leave_one_out_disagreement")
            if not halves:
                failures.append(prefix + metric + ":time_half_disagreement")
        n0, n = sum(b["n0"] for b in blocks), sum(b["n"] for b in blocks)
        changes = sum(b["target_endpoint_changes"] for b in blocks)
        roundtrips = sum(b["roundtrips"] for b in blocks)
        acceptance = [accepted / attempted if attempted else 0.0
                      for _, (attempted, accepted) in sorted(run["edges"].items())]
        if min(n0, n - n0) < THRESHOLDS["minimum_each_endpoint_sweeps_per_chain"]:
            failures.append(prefix + "endpoint_occupancy")
        if changes < THRESHOLDS["minimum_endpoint_changes_per_chain"]:
            failures.append(prefix + "endpoint_changes")
        if roundtrips < THRESHOLDS["minimum_completed_roundtrips_per_chain"]:
            failures.append(prefix + "roundtrips")
        if min(acceptance) < THRESHOLDS["minimum_final_each_edge_swap_acceptance"]:
            failures.append(prefix + "adjacent_swap_acceptance")
        chain_results.append({
            "chain": chain, "initial": INITIAL[chain], "estimates": estimates,
            "time_halves": half_estimates, "leave_one_out": leave_one_out,
            "agreement_gates": agreements, "endpoint_occupancy": [n0, n - n0],
            "endpoint_changes": changes, "roundtrips": roundtrips,
            "roundtrips_by_replica": run["replica_roundtrips"], "edge_acceptance": acceptance,
            "signed_descriptives_only": {
                "positive_endpoint_one_observations": sum(b["nTpos"] for b in blocks),
                "negative_endpoint_one_observations": sum(b["nTneg"] for b in blocks),
                "successive_nonzero_endpoint_one_sign_changes": sum(b["target_T_sign_changes"] for b in blocks),
                "mean_T_squared": math.fsum(b["sumT2"] for b in blocks) / n,
                "mean_Y0_squared_times_I0": math.fsum(b["sumY0sq"] for b in blocks) / n,
            },
            "input_file": run["file"], "input_sha256": run["sha256"],
        })
    stability = {metric: coarsening(pooled[metric], metric) for metric in GATE_METRICS}
    for metric, gate in stability.items():
        if not gate["pass"]:
            failures.append("pooled:" + metric + ":" + gate["reason"])
    if key[2] == 2:
        identities = {"equal_endpoint_mass": identity_residual(pooled["p0"], 0.5),
                      "reversal_mean_Y": identity_residual(pooled["Y_unconditional"], 0.0)}
    else:
        identities = {"untwisted_mean_Y": identity_residual(pooled["Y0"], 0.0),
                      "endpoint_zero_mass_bound": identity_residual(pooled["p0"], 0.5, True)}
    return {"L": key[0], "k": key[1], "base": key[2],
            "role": "main" if key[2] == 0 else "reversal_control",
            "pooled": pooled, "chains": chain_results,
            "mobility_failures": failures, "mobility_pass": not failures,
            "pooled_coarsening": stability, "identity_residuals": identities,
            "signed_ratio_meaning": "c_k" if key[2] == 0 else "endpoint_mean_not_c_k",
            "status": "PENDING_GLOBAL_GATES"}


def report(runs):
    indexed = {}
    for run in runs:
        require(run["key"] not in indexed, f"duplicate run {run['key']}")
        indexed[run["key"]] = run
    missing = [key for key in expected_keys() if key not in indexed]
    result = {
        "analysis": ITEM, "status": "FAIL_IMPLEMENTATION" if missing else "PENDING",
        "thresholds": THRESHOLDS, "missing_runs": [list(key) for key in missing],
        "available_run_count": len(runs), "groups": [], "incomplete_groups": [],
        "scope": "NON-CANONICAL finite-L engineering transport qualification only",
        "coverage": "4SE comparisons have no rigorous or simultaneous coverage claim",
        "estimate_label": "NONINFERENTIAL_ESTIMATE",
        "limitations": [
            "Qualification does not prove equilibrium, decorrelation or a mixing time.",
            "Every signed mean and positive/negative part remains descriptive.",
            "No signed interval, D interval, thermodynamic lower bound, phase or P1 verdict is formed.",
            "No prescribed winding branch occupancy or sign occupancy is required.",
            "Identity comparisons are read only after all main and control groups pass mobility.",
        ],
    }
    for size in L_VALUES:
        for mode in MODES:
            for base in BASES:
                keys = [(size, mode, base, chain) for chain in CHAINS]
                if all(key in indexed for key in keys):
                    result["groups"].append(analyze_group([indexed[key] for key in keys]))
                else:
                    available = [indexed[key] for key in keys if key in indexed]
                    result["incomplete_groups"].append({
                        "L": size, "k": mode, "base": base,
                        "available_chains": [{"chain": run["key"][3], "estimates": {
                            metric: ratio_summary([run["blocks"]], metric) for metric in METRICS},
                            "input_file": run["file"], "input_sha256": run["sha256"]}
                            for run in available],
                    })
    groups = result["groups"]
    all_mobility = not missing and all(group["mobility_pass"] for group in groups)
    if missing:
        status = "FAIL_IMPLEMENTATION"
    elif not all_mobility:
        status = "INCONCLUSIVE_MOBILITY"
    else:
        identities_pass = True
        for group in groups:
            for residual in group["identity_residuals"].values():
                residual["evaluated_after_mobility"] = True
                identities_pass = identities_pass and residual["would_pass"]
        status = "TRANSPORT_QUALIFIED" if identities_pass else "FAIL_CONSISTENCY"
    result["status"] = status
    for group in groups:
        group["status"] = status
    return result


def read_execution(directory):
    """Check byte custody and every declared process before interpreting gates."""
    manifest_path = directory / "execution.json"
    raw_manifest = manifest_path.read_bytes()
    try:
        records = json.loads(raw_manifest.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeError) as exc:
        raise InvalidInput("malformed execution.json") from exc
    require(isinstance(records, list), "execution.json must contain a list")
    expected = {stem_for(key): key for key in expected_keys()}
    expected_text = {"audit": AUDIT_TEXT, "analyzer_tests": TEST_TEXT}
    allowed = set(expected) | set(expected_text)
    seen, runs, errors = set(), [], []
    extra_tables = sorted(path.name for path in directory.glob("*.tsv")
                          if path.name not in {stem + ".tsv" for stem in allowed})
    if extra_tables:
        errors.append("unexpected stdout tables: " + ",".join(extra_tables))
    for record in records:
        if not isinstance(record, dict):
            errors.append("malformed execution record")
            continue
        stem = record.get("stem")
        if not isinstance(stem, str) or stem not in allowed or stem in seen:
            errors.append("unexpected or duplicate execution stem")
            continue
        seen.add(stem)
        try:
            code = record["exit_code"]
            require(type(code) is int, f"{stem}: invalid exit code")
            seconds = record.get("seconds")
            require(type(seconds) in (int, float) and math.isfinite(seconds) and seconds >= 0,
                    f"{stem}: invalid elapsed seconds")
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
            if stem in expected_text:
                require((directory / f"{stem}.tsv").read_text(encoding="utf-8") == expected_text[stem],
                        f"{stem}: unexpected audit output")
        except (InvalidInput, OSError, UnicodeError, KeyError) as exc:
            errors.append(str(exc))
        if stem in expected:
            try:
                run = read_run(directory / f"{stem}.tsv")
                require(run["key"] == expected[stem], f"{stem}: run key mismatch")
                runs.append(run)
            except (InvalidInput, OSError, UnicodeError) as exc:
                errors.append(str(exc))
    for stem in sorted(allowed - seen):
        errors.append(f"missing execution record: {stem}")
    result = report(runs)
    result["execution_manifest_sha256"] = hashlib.sha256(raw_manifest).hexdigest()
    result["execution_errors"] = errors
    if errors:
        result["status"] = "FAIL_IMPLEMENTATION"
        for group in result["groups"]:
            group["status"] = "FAIL_IMPLEMENTATION"
            for residual in group["identity_residuals"].values():
                residual["evaluated_after_mobility"] = False
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_directory", type=Path)
    args = parser.parse_args()
    try:
        result = read_execution(args.output_directory)
    except (InvalidInput, OSError, ArithmeticError, ValueError, TypeError) as exc:
        result = {"analysis": ITEM, "status": "FAIL_IMPLEMENTATION", "reason": str(exc),
                  "scope": "inaccessible or malformed engineering input; no inference"}
    print(json.dumps(result, indent=2, sort_keys=True, allow_nan=False))
    return 2 if result["status"] == "FAIL_IMPLEMENTATION" else 0


if __name__ == "__main__":
    sys.exit(main())
