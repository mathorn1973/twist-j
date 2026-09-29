#!/usr/bin/env python3
"""Pinned descriptive CM localization. No sampling or inference is performed."""

import argparse
import csv
from fractions import Fraction
import hashlib
import io
import json
import math
from pathlib import Path
import re
import subprocess


SOURCE_COMMIT = "fc16df1b06d971ca7ef4e2f35eab92d8b9637bdb"
PREFIX = "notes/C-PHOTON-TWIST-SNAKE-SECTOR-N/ENGINEERING/"
SIZES = (4, 6, 8, 10)
MODES = (1, 2)
CHAINS = (0, 1)
BLOCK = 512
TOLERANCE = 1e-9
ESTIMATORS = {"F": "sumFi", "PF": "sumPFi", "PB": "PB", "Bw": "sumBi"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def close(left, right):
    return abs(left - right) <= TOLERANCE * (1 + abs(right))


def exact(value):
    return f"{value.numerator}/{value.denominator}"


def total(values):
    values = list(values)
    return None if any(v is None for v in values) else math.fsum(values)


def difference(left, right):
    return None if left is None or right is None else left - right


def blob(repo, path):
    return subprocess.check_output(["git", "-C", str(repo), "show", f"{SOURCE_COMMIT}:{path}"])


def input_paths():
    return [PREFIX + f"L{L}_k{k}_classMinus_c{c}.tsv"
            for L in SIZES for k in MODES for c in CHAINS] + [PREFIX + "analysis.json"]


def load_inputs(repo, manifest_path):
    manifest_bytes = manifest_path.read_bytes()
    manifest = json.loads(manifest_bytes)
    require(manifest["commit"] == SOURCE_COMMIT, "wrong immutable input commit")
    data = {}
    digests = {}
    for path in input_paths():
        claimed = manifest["sha256"].get(path)
        require(isinstance(claimed, str) and re.fullmatch(r"[0-9a-f]{64}", claimed),
                f"absent or malformed input hash: {path}")
        raw = blob(repo, path)
        actual = hashlib.sha256(raw).hexdigest()
        require(actual == claimed, f"input hash mismatch: {path}")
        data[path] = raw
        digests[path] = actual
    return data, digests, hashlib.sha256(manifest_bytes).hexdigest()


def read_chain(raw, L, k, chain):
    metadata = {}
    lines = []
    for line in raw.decode("utf-8").splitlines():
        if line.startswith("#"):
            key, value = line[1:].lstrip().split("\t", 1)
            require(key not in metadata, f"duplicate metadata: {key}")
            metadata[key] = value
        elif line.strip():
            lines.append(line)
    reader = csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t")
    require(reader.fieldnames is not None, "missing table header")
    require(len(reader.fieldnames) == len(set(reader.fieldnames)), "duplicate table fields")
    needed = {"L", "k", "chain", "kind", "segment", "n", "phase", "block", "count",
              "sumFi", "sumPFi", "sumBi", "forced", "classMinus", "sumW", "minW", "maxW"}
    needed |= {f"hB{i}" for i in range(5)}
    require(needed <= set(reader.fieldnames), "missing table fields")
    rows = []
    integer_fields = needed - {"phase", "sumFi", "sumPFi", "sumBi"}
    for source in reader:
        require(None not in source and None not in source.values(), "malformed table row")
        row = {f: int(source[f]) for f in integer_fields}
        row["phase"] = source["phase"]
        for field in ("sumFi", "sumPFi", "sumBi"):
            row[field] = Fraction(source[field])
            require(row[field] >= 0, f"negative estimator {field}")
        row["PB"] = sum(row[f"hB{i}"] for i in range(5))
        require(all(row[f"hB{i}"] >= 0 for i in range(5)), "negative histogram count")
        require(0 <= row["PB"] <= BLOCK, "reverse histogram count exceeds block")
        require(row["count"] == BLOCK, "wrong block length")
        require((row["L"], row["k"], row["chain"], row["kind"]) == (L, k, chain, 5),
                "wrong run identity")
        require(row["classMinus"] == BLOCK, "row outside class minus")
        require(row["minW"] <= row["maxW"] and 2 * row["maxW"] < -row["n"],
                "class-minus extrema violate restriction")
        require(BLOCK * row["minW"] <= row["sumW"] <= BLOCK * row["maxW"],
                "sumW inconsistent with extrema")
        rows.append(row)
    M = L * L
    expected = [(m - 1, m, "up" if m < M else "dwell", b)
                for m in range(1, M + 1) for b in range(4 if m < M else 64)]
    require(len(rows) == len(expected), "wrong number of rows")
    flags = {}
    by_n = {}
    for row, wanted in zip(rows, expected):
        require(tuple(row[f] for f in ("segment", "n", "phase", "block")) == wanted,
                "row sequence differs from frozen schedule")
        n, flag = row["n"], row["forced"]
        require(flag in (0, 1), "invalid forced flag")
        require(n != 1 or flag == 0, "reset on initial ensemble")
        require(flags.setdefault(n, flag) == flag, "forced flag varies inside ensemble")
        by_n.setdefault(n, []).append(row)
    resets = sum(flags.values())
    production = len(rows) * BLOCK
    required = {
        "format": "twist_snake_sector_blocks_v2", "L": str(L), "k": str(k), "chain": str(chain),
        "kind": "5", "kind_name": "classMinus", "base": "0", "restriction": "1",
        "schedule": "up_only", "seed": str(202609300000 + 1000 * L + 100 * k + 50 + chain),
        "seam_size": str(M), "start_twist": "1", "final_twist": str(M),
        "chain_initial": "coldAlt1CM" if chain == 0 else "hot1CM",
        "warmup_sweeps": "512", "dwell_sweeps": "16384", "dwell_long_sweeps": "32768",
        "visit_sweeps": "2048", "equilibration_sweeps": "32", "post_forcing_sweeps": "512",
        "block_length": "512", "segments": str(M), "seam_order": "x2_fastest_then_x3",
        "class_rule": "class0_if_2W_ge_minus_n_else_classMinus",
        "sampling": "every_production_sweep_after_full_heatbath_sweep",
        "forced_steps": str(resets),
        "sweeps_total": str(512 + production + (M - 1 - resets) * 32 + resets * 512),
        "completion": "PASS",
    }
    for field, value in required.items():
        require(metadata.get(field) == value, f"wrong metadata field {field}")
    return by_n, flags, metadata


def estimator(rows, field):
    values = [Fraction(r[field], BLOCK) for r in rows]
    B = len(values)
    require(B >= 2, "not enough finest-scale blocks")
    mean = sum(values, Fraction()) / B
    variance = sum(((x - mean) ** 2 for x in values), Fraction()) / (B - 1)
    rv = variance / (B * mean ** 2) if mean else None
    correction = rv / 2 if rv is not None else None
    raw_log = math.log(float(mean)) if mean else None
    value = raw_log + float(correction) if mean else None
    return {"blocks": B, "sweeps": B * BLOCK, "mean_exact": exact(mean),
            "variance_exact": exact(variance),
            "relative_variance_exact": exact(rv) if rv is not None else None,
            "bias_correction_exact": exact(correction) if correction is not None else None,
            "raw_log_engineering": raw_log, "corrected_log_engineering": value,
            "status": "AVAILABLE" if mean else "ZERO_ESTIMATOR_MEAN"}


def linear_combination(terms):
    if any(e["corrected_log_engineering"] is None for _, e in terms):
        return {"raw_log_engineering": None, "bias_correction_exact": None,
                "value_engineering": None, "status": "ZERO_ESTIMATOR_MEAN"}
    correction = sum((weight * Fraction(e["bias_correction_exact"]) for weight, e in terms), Fraction())
    raw = math.fsum(float(weight) * e["raw_log_engineering"] for weight, e in terms)
    return {"raw_log_engineering": raw, "bias_correction_exact": exact(correction),
            "value_engineering": raw + float(correction), "status": "AVAILABLE"}


def analyze_chain(raw, L, k, chain, reference):
    by_n, flags, metadata = read_chain(raw, L, k, chain)
    M, half = L * L, Fraction(1, 2)
    ensembles = []
    zeros = []
    last_reset = None
    for n in range(1, M + 1):
        names = (["F", "PF"] if n < M else []) + (["PB", "Bw"] if n > 1 else [])
        estimates = {name: estimator(by_n[n], ESTIMATORS[name]) for name in names}
        zeros.extend({"n": n, "estimator": name} for name, e in estimates.items()
                     if e["status"] == "ZERO_ESTIMATOR_MEAN")
        terms = [(half if name in ("F", "PF") else -half, e) for name, e in estimates.items()]
        if flags[n]:
            last_reset = n
        ensembles.append({"n": n, "forced": flags[n],
                          "steps_since_last_reset": n - last_reset if last_reset is not None else None,
                          "estimators": estimates, "contribution": linear_combination(terms)})
    steps = []
    cumulative = 0.0
    for n in range(1, M):
        left, right = ensembles[n - 1]["estimators"], ensembles[n]["estimators"]
        pairing_A = linear_combination([(Fraction(1), left["F"]), (Fraction(-1), right["PB"])])
        pairing_B = linear_combination([(Fraction(1), left["PF"]), (Fraction(-1), right["Bw"])])
        step = linear_combination([(half, left["F"]), (half, left["PF"]),
                                   (-half, right["PB"]), (-half, right["Bw"])])
        cumulative = total([cumulative, step["value_engineering"]])
        steps.append({"n": n, "destination_n": n + 1, "forced_source": flags[n],
                      "forced_destination": flags[n + 1],
                      "steps_since_last_reset_at_destination": ensembles[n]["steps_since_last_reset"],
                      "pairing_A_engineering": pairing_A["value_engineering"],
                      "pairing_B_engineering": pairing_B["value_engineering"], **step,
                      "cumulative_engineering": cumulative})
    values = [e["contribution"]["value_engineering"] for e in ensembles]
    step_sum = total(s["value_engineering"] for s in steps)
    ensemble_sum = total(values)
    initial, intermediate, endpoint = values[0], total(values[1:-1]), values[-1]
    if step_sum is not None:
        require(ensemble_sum is not None and close(step_sum, ensemble_sum), "step/ensemble sum mismatch")
        require(close(total([initial, intermediate, endpoint]), step_sum), "endpoint decomposition mismatch")
        require(reference is not None and close(step_sum, reference), "parent chain reconstruction mismatch")
    else:
        require(reference is None, "null chain sum does not match parent")
    return {"L": L, "k": k, "chain": chain, "status": "DESCRIPTIVE_ONLY",
            "metadata": metadata, "zero_means": zeros, "ensembles": ensembles, "steps": steps,
            "summary": {"log_l_engineering": step_sum, "parent_log_l_engineering": reference,
                        "reconstruction_difference": difference(step_sum, reference),
                        "reconstruction_check": "MATCH", "initial_ensemble_engineering": initial,
                        "intermediate_ensembles_engineering": intermediate,
                        "endpoint_ensemble_engineering": endpoint,
                        "forced_reached_n": [n for n, flag in flags.items() if flag]}}


def paired_chains(left, right):
    paired_steps, paired_ensembles = [], []
    for a, b in zip(left["steps"], right["steps"]):
        require(a["n"] == b["n"], "paired step mismatch")
        paired_steps.append({"n": a["n"], "destination_n": a["destination_n"],
                             "difference_engineering": difference(a["value_engineering"], b["value_engineering"]),
                             "cumulative_difference_engineering": difference(a["cumulative_engineering"], b["cumulative_engineering"]),
                             **{f"chain{c}_{name}": item[name]
                                for c, item in enumerate((a, b))
                                for name in ("forced_source", "forced_destination", "steps_since_last_reset_at_destination")}})
    for a, b in zip(left["ensembles"], right["ensembles"]):
        require(a["n"] == b["n"], "paired ensemble mismatch")
        paired_ensembles.append({"n": a["n"], "chain0_forced": a["forced"], "chain1_forced": b["forced"],
                                "difference_engineering": difference(a["contribution"]["value_engineering"],
                                                                     b["contribution"]["value_engineering"])})
    partitions = {}
    for label, records, fields in (("steps_by_destination_flags", paired_steps,
                                  ("chain0_forced_destination", "chain1_forced_destination")),
                                 ("ensembles_by_reached_flags", paired_ensembles,
                                  ("chain0_forced", "chain1_forced"))):
        groups = []
        for f0 in (0, 1):
            for f1 in (0, 1):
                chosen = [r for r in records if (r[fields[0]], r[fields[1]]) == (f0, f1)]
                groups.append({"chain0_flag": f0, "chain1_flag": f1, "count": len(chosen),
                               "n": [r["n"] for r in chosen],
                               "sum_difference_engineering": total(r["difference_engineering"] for r in chosen)})
        require(sum(g["count"] for g in groups) == len(records), "reset partition coverage mismatch")
        partitions[label] = groups
    fields = ("log_l_engineering", "initial_ensemble_engineering", "intermediate_ensembles_engineering",
              "endpoint_ensemble_engineering")
    summary = {"difference_" + f: difference(left["summary"][f], right["summary"][f]) for f in fields}
    complete = summary["difference_log_l_engineering"]
    if complete is not None:
        require(close(total(r["difference_engineering"] for r in paired_steps), complete),
                "paired step difference does not recompose")
        require(close(total(r["difference_engineering"] for r in paired_ensembles), complete),
                "paired ensemble difference does not recompose")
        for groups in partitions.values():
            require(close(total(g["sum_difference_engineering"] for g in groups), complete),
                    "reset partition does not recompose")
    return {"L": left["L"], "k": left["k"], "orientation": "chain0_minus_chain1",
            "status": "DESCRIPTIVE_ONLY", "summary": summary, "steps": paired_steps,
            "ensembles": paired_ensembles, "reset_partitions": partitions}


def write_tsv(path, rows):
    require(rows, "empty output table")
    fields = list(rows[0])
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: "null" if value is None else value for key, value in row.items()})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    require(not args.output.exists(), "output directory already exists; refusing overwrite")
    data, digests, manifest_digest = load_inputs(args.repo, args.inputs)
    parent = json.loads(data[PREFIX + "analysis.json"])
    require(parent["analysis"] == "C-PHOTON-TWIST-SNAKE-SECTOR-N", "wrong parent analysis")
    reference = {(v["L"], m["k"]): m["classMinus"] for v in parent["volumes"] for m in v["modes"]}
    chains, pairs = [], []
    for L in SIZES:
        for k in MODES:
            group = []
            for c in CHAINS:
                path = PREFIX + f"L{L}_k{k}_classMinus_c{c}.tsv"
                one = analyze_chain(data[path], L, k, c, reference[L, k]["log_l_by_chain"][str(c)])
                require(int(one["metadata"]["forced_steps"]) == reference[L, k]["forced_steps_by_chain"][str(c)],
                        "parent reset total mismatch")
                one["input_path"], one["input_sha256"] = path, digests[path]
                chains.append(one)
                group.append(one)
            pairs.append(paired_chains(*group))
    output = {"analysis": "C-PHOTON-RESTRICTED-REACHABILITY-N/localization", "status": "DESCRIPTIVE_ONLY",
              "source_commit": SOURCE_COMMIT, "input_manifest_sha256": manifest_digest, "input_sha256": digests,
              "arithmetic": "exact rational arithmetic on recorded decimals; logarithmic outputs are floating-point engineering values",
              "scope": "all sixteen CM up-only chains; all eight chain0-minus-chain1 pairs; no fresh samples or inference",
              "excluded_scope": "chain2 endpoint and full parent G3 own-versus-others comparison; no equilibration or connectivity verdict",
              "parent_status_unchanged": parent["status"], "reconstruction_tolerance": TOLERANCE,
              "chains": chains, "pairs": pairs}
    args.output.mkdir(parents=True)
    (args.output / "localization.json").write_text(json.dumps(output, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    write_tsv(args.output / "steps.tsv", [{"L": c["L"], "k": c["k"], "chain": c["chain"], **s}
                                          for c in chains for s in c["steps"]])
    write_tsv(args.output / "paired_steps.tsv", [{"L": p["L"], "k": p["k"], **s} for p in pairs for s in p["steps"]])
    write_tsv(args.output / "paired_ensembles.tsv", [{"L": p["L"], "k": p["k"], **e} for p in pairs for e in p["ensembles"]])
    output_names = ("localization.json", "steps.tsv", "paired_steps.tsv", "paired_ensembles.tsv")
    sums = [hashlib.sha256((args.output / name).read_bytes()).hexdigest() + "  " + name for name in output_names]
    (args.output / "SHA256SUMS").write_text("\n".join(sums) + "\n", encoding="ascii")
    print("DESCRIPTIVE_ONLY: 16 ladders, 8 pairs, all reconstruction checks MATCH")


if __name__ == "__main__":
    main()
