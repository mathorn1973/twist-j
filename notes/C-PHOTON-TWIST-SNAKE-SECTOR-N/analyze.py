#!/usr/bin/env python3
"""Frozen engineering analysis, NON-CANONICAL; no rigorous coverage claim.

Input: the untouched run_snake.py output directory and its execution manifest.
Output: JSON retaining all estimates, including failed diagnostics.
No phase, scaling, thermodynamic, or P1 verdict is implemented here.

Job groups per (L,k): U (kind 0, five unconstrained round-trip chains),
P (kind 3, two chains: dwell at twist 0, one step, dwell at twist 1), C0
(kind 4, class 0: two restricted up-only chains and one chain dwelling at
L^2 from the cold class layout), CM (kind 5, class minus, likewise); exact
control groups (kind 2, four chains) for L in {4,6}.

Primary route (class sum):
  log R_k = log r_0 + log[ pi_1(0) e^{l_0} + pi_1(-) e^{l_-} ],
  r_0 from the P group (forward at its n=0 dwell, reverse at its n=1 dwell),
  pi_1(-) the class-minus fraction at the P n=1 dwell, l_c the restricted
  ladder sums of C0 and CM; E Y = sum_c P_c E^{(c)} Y with the class weights
  P_c = pi_1(c) e^{l_c} / sum. Errors by the delta method with the three
  groups independent (r_0 and pi_1 share the P group and are treated as
  independent estimates). The U route (unconstrained ladder, as in the
  consumed predecessor) is an exact cross-check (G11: log R, log r_0 and
  pi_1(-)) read only when it passes its own gates including the sector gate
  G9'.

Step estimator (every ladder): the equal-weight geometric mean of the two
exact pairings F/PB and PF/Bw of PREREG.md,
  log r_n = 1/2 [ (log F_n + rv/2) + (log PF_n + rv/2)
               - (log PB_{n+1} + rv/2) - (log Bw_{n+1} + rv/2) ],
with first-order bias corrections of the logs of pooled means; for
unconstrained ladders PF = PB = 1 exactly. Batch standard errors use the
per-batch influence at ensemble m,
  u_b = 1/2 (f_b/F_m + pf_b/PF_m) [step m exists]
      - 1/2 (pb_b/PB_m + bw_b/Bw_m) [step m-1 exists],
at block scales 512, 1024, 2048 (coarsening inside one segment only),
SE^2 = sum_m Var_b(u_b)/B_m, maximum over scales. Subset gates use the
pooled within-group batch variance so that the tested deviation never
enters its own tolerance.

Closed status set and strict precedence, fixed before execution:
  per (L,k):  FAIL_IMPLEMENTATION > INCOMPLETE > FAIL_CONSISTENCY
              > INCONCLUSIVE_EQUILIBRATION > UNRESOLVED
              > RESOLVED_SIGNED_CONTRAST
  per L:      the worst mode label; RESOLVED_SIGNED_CONTRAST only when both
              modes pass every gate, both class-sum log R_k report
              half-widths are at most 1.0, both class-sum mean-Y report
              half-widths are at most 0.05 and at least one mean-Y interval
              excludes zero; otherwise UNRESOLVED.
  overall:    the worst volume label.
The U route carries its own sub-label (GATES_PASSED, SECTOR_FROZEN,
INCONCLUSIVE_EQUILIBRATION or FAIL_CONSISTENCY); controls carry
CONTROL_PASS, CONTROL_SECTOR_FROZEN, FAIL_CONSISTENCY or INCOMPLETE.
A job that timed out (exit 124) or failed to launch (exit 127) makes its
(L,k) INCOMPLETE and nothing else. Any other nonzero exit, nonempty stderr,
byte or hash mismatch, malformed record, histogram, class or sector
inconsistency, audit or environment mismatch is a custody or implementation
failure: every group is labelled FAIL_IMPLEMENTATION and every estimate is
NONINFERENTIAL_ESTIMATE, although all estimates stay visible.
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


L_VALUES = (4, 6, 8, 10)
CONTROL_L_VALUES = (4, 6)
MODES = (1, 2)
KIND_MAIN, KIND_CONTROL, KIND_PI1, KIND_CLASS0, KIND_CLASSM = 0, 2, 3, 4, 5
KINDS = (KIND_MAIN, KIND_CONTROL, KIND_PI1, KIND_CLASS0, KIND_CLASSM)
KIND_NAMES = {KIND_MAIN: "main", KIND_CONTROL: "control", KIND_PI1: "pi1",
              KIND_CLASS0: "class0", KIND_CLASSM: "classMinus"}
KIND_CHAINS = {KIND_MAIN: (0, 1, 2, 3, 4), KIND_CONTROL: (0, 1, 2, 3), KIND_PI1: (0, 1, 2, 3),
               KIND_CLASS0: (0, 1, 2), KIND_CLASSM: (0, 1, 2)}
LADDER_CHAINS = (0, 1)  # restricted chains with visit rows; chain 2 dwells at L^2 only
CLASS_SUM_KINDS = (KIND_PI1, KIND_CLASS0, KIND_CLASSM)
RESTRICTED_KINDS = (KIND_CLASS0, KIND_CLASSM)
ROUND_TRIP_KINDS = (KIND_MAIN, KIND_CONTROL)
RESTRICTION = {KIND_MAIN: -1, KIND_CONTROL: -1, KIND_PI1: -1, KIND_CLASS0: 0, KIND_CLASSM: 1}
BASE = {KIND_MAIN: 0, KIND_CONTROL: 2, KIND_PI1: 0, KIND_CLASS0: 0, KIND_CLASSM: 0}
INITIAL_ROUND_TRIP = {0: "cold0", 1: "hot0", 2: "coldT", 3: "hotT", 4: "coldAltT"}
SEED_BASE = 202609300000
WARMUP_SWEEPS = 512
DWELL_SWEEPS = 16384
DWELL_LONG_SWEEPS = 32768  # step-zero dwells and restricted endpoint dwells
VISIT_SWEEPS = 2048
EQUILIBRATION_SWEEPS = 32
POST_FORCING_SWEEPS = 512
BLOCK_LENGTH = 512
DWELL_BLOCKS = DWELL_SWEEPS // BLOCK_LENGTH
DWELL_LONG_BLOCKS = DWELL_LONG_SWEEPS // BLOCK_LENGTH
VISIT_BLOCKS = VISIT_SWEEPS // BLOCK_LENGTH
COARSENING = (1, 2, 4)
SCALES = tuple(str(BLOCK_LENGTH * f) for f in COARSENING)
# A two-chain up-only ladder has one 2048-sweep batch per chain per visit, so
# the within-chain pooled variance has no degrees of freedom at that scale: the
# subset gates (G3) of restricted ladders use the first two scales. Aggregate
# statistics (partial sums, deficit, G6, G7) keep all three scales, with one
# degree of freedom per intermediate ensemble at the coarsest scale.
RESTRICTED_SUBSET_SCALES = SCALES[:2]
MULTIPLIER = 4.0
THRESHOLDS = {
    "empirical_se_multiplier": MULTIPLIER,
    "maximum_log_R_report_halfwidth": 1.0,
    "maximum_mean_Y_report_halfwidth": 0.05,
    "maximum_se_coarsening_ratio": 1.5,
    "block_lengths": [BLOCK_LENGTH * f for f in COARSENING],
    "exact_untwisted_mean_Y": 0.0,
    "maximum_untwisted_mean_Y_squared": 1.0,
    "negligible_contrast_R_upper": 1e-3,
}
PHI = (1.0 + math.sqrt(5.0)) / 2.0
WEIGHT = {0: 4.0, 1: PHI ** 2, 2: PHI ** -2, 3: PHI ** -2, 4: PHI ** 2}
RATIO = {k: [WEIGHT[(f + k) % 5] / WEIGHT[f] for f in range(5)] for k in MODES}
RATIO_BOUNDS = {k: (min(RATIO[k]), max(RATIO[k])) for k in MODES}
EXPECTED_AUDIT = (
    'NON-CANONICAL floating-point engineering audit\n'
    'geometries\t4\n'
    'fixture_states\t864\n'
    'estimator_identities\t384\n'
    'local_enumerations\t96\n'
    'restricted_enumerations\t1312\n'
    'mixed_enumerations\t10\n'
    'forcing_checks\t1440\n'
    'restricted_law_checks\t6976\n'
    'invariance_checks\t384\n'
    'inversion_checks\t42\n'
    'exercise_sweeps\t160\n'
    'restricted_sweeps\t160\n'
    'forbidden_candidates\t961\n'
    'schedule_rows\t464\n'
    'mutations_caught\t320\n'
    'result\tPASS\n'
)
EXPECTED_ENVIRONMENT = {"workers": 4, "audit_timeout_seconds": 600, "per_chain_timeout_seconds": 2400}
HIST_F = tuple(f"hF{f}" for f in range(5))
HIST_B = tuple(f"hB{f}" for f in range(5))
SECTOR_FIELDS = ("sec0", "secMinus", "secPlus", "secOther", "untMinus", "untPlus", "untOther",
                 "pure0", "pureMinus", "purePlus", "flips", "classMinus", "forced")
INTEGER_FIELDS = ({"L", "k", "chain", "kind", "segment", "n", "block", "count"}
                  | set(HIST_F) | set(HIST_B) | set(SECTOR_FIELDS))
SIGNED_INTEGER_FIELDS = {"sumW", "minW", "maxW"}
STRING_FIELDS = {"phase"}
FLOAT_FIELDS = {
    "sumFn", "sumFn2", "sumFi", "sumFi2", "sumBn", "sumBn2", "sumBi", "sumBi2",
    "sumPFi", "sumPFi2", "sumY", "sumY2", "sumS", "sumS2",
}
FIELDS = INTEGER_FIELDS | SIGNED_INTEGER_FIELDS | STRING_FIELDS | FLOAT_FIELDS
# Additive per-block quantities whose batch means are per-sweep means.
BATCH_FIELDS = tuple(sorted(FLOAT_FIELDS)) + ("PFn", "PB", "secMinus", "secPlus", "untMinus", "untPlus",
                                             "allMinus", "allPlus", "classMinus", "sumW", "pure0", "pureMinus")
PHASES = {"dwell", "up", "down"}
UNAVAILABLE_EXIT_CODES = {124, 127}
STATUS_ORDER = ["FAIL_IMPLEMENTATION", "INCOMPLETE", "FAIL_CONSISTENCY",
                "INCONCLUSIVE_EQUILIBRATION", "UNRESOLVED", "RESOLVED_SIGNED_CONTRAST"]
GATES_PASSED = "GATES_PASSED"  # per-mode gate outcome; volumes carry the closed labels
SECTOR_FROZEN = "SECTOR_FROZEN"  # U-route sub-label only


class InvalidInput(Exception):
    pass


def require(condition, message):
    if not condition:
        raise InvalidInput(message)


def worst(statuses):
    return min(statuses, key=STATUS_ORDER.index)


def stem_of(size, mode, kind, chain):
    return f"L{size}_k{mode}_{KIND_NAMES[kind]}_c{chain}"


def kind_sizes(kind):
    return CONTROL_L_VALUES if kind == KIND_CONTROL else L_VALUES


def declared_jobs():
    return [(size, mode, kind, chain) for kind in KINDS for size in kind_sizes(kind) for mode in MODES
            for chain in KIND_CHAINS[kind]]


def top_dwell(kind, chain):
    return kind in RESTRICTED_KINDS and chain == 2


def initial_name(kind, chain):
    if kind in ROUND_TRIP_KINDS:
        return INITIAL_ROUND_TRIP[chain]
    if kind == KIND_PI1:
        return "hot0" if chain % 2 else "cold0"
    suffix = "C0" if kind == KIND_CLASS0 else "CM"
    if top_dwell(kind, chain):
        return ("coldAltT" if kind == KIND_CLASSM else "coldT") + suffix
    return ("hot1" if chain % 2 else ("coldAlt1" if kind == KIND_CLASSM else "cold1")) + suffix


def schedule_name(kind, chain):
    if kind in ROUND_TRIP_KINDS:
        return "round_trip"
    if kind == KIND_PI1:
        return "step_zero"
    return "dwell_at_top" if top_dwell(kind, chain) else "up_only"


def finite_number(text, where):
    try:
        number = float(text)
    except (TypeError, ValueError) as exc:
        raise InvalidInput(f"{where}: invalid number") from exc
    require(math.isfinite(number), f"{where}: nonfinite number")
    return number


def integer(text, where, nonnegative=True):
    try:
        number = int(text)
    except (TypeError, ValueError) as exc:
        raise InvalidInput(f"{where}: invalid integer") from exc
    require(not nonnegative or number >= 0, f"{where}: negative integer")
    return number


def start_twist(size, kind, chain):
    if kind in ROUND_TRIP_KINDS:
        return 0 if chain < 2 else size * size
    if kind == KIND_PI1:
        return 0
    return size * size if top_dwell(kind, chain) else 1


def final_twist(size, kind, chain):
    if kind in ROUND_TRIP_KINDS:
        return 1 if chain < 2 else size * size - 1
    return 1 if kind == KIND_PI1 else size * size


def first_twist(kind):
    """The lowest ensemble of a ladder of this kind."""
    return 1 if kind in RESTRICTED_KINDS else 0


def expected_segments(size, kind, chain):
    """The frozen visiting order of each kind."""
    seam = size * size
    if kind in ROUND_TRIP_KINDS:
        n = start_twist(size, kind, chain)
        direction = 1 if n == 0 else -1
        sequence = [(n, "dwell", DWELL_BLOCKS)]
        for _ in range(1, seam):
            n += direction
            sequence.append((n, "up" if direction == 1 else "down", VISIT_BLOCKS))
        n += direction
        sequence.append((n, "dwell", DWELL_BLOCKS))
        direction = -direction
        for _ in range(1, seam):
            n += direction
            sequence.append((n, "up" if direction == 1 else "down", VISIT_BLOCKS))
        return sequence
    if kind == KIND_PI1:
        return [(0, "dwell", DWELL_LONG_BLOCKS), (1, "dwell", DWELL_LONG_BLOCKS)]
    if top_dwell(kind, chain):
        return [(seam, "dwell", DWELL_LONG_BLOCKS)]
    return [(n, "up", VISIT_BLOCKS) for n in range(1, seam)] + [(seam, "dwell", DWELL_LONG_BLOCKS)]


def close(left, right, tolerance):
    return abs(left - right) <= tolerance * (1.0 + abs(left) + abs(right))


def class_of(W, n):
    return 0 if 2 * W >= -n else 1


def read_run(path, expected_key):
    size, mode, kind, chain = expected_key
    restricted = kind in RESTRICTED_KINDS
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise InvalidInput(f"{path.name}: invalid UTF-8") from exc
    metadata = {}
    lines = []
    for line_number, line in enumerate(text.splitlines(), 1):
        if line.startswith("#"):
            parts = line[1:].lstrip().split("\t")
            require(len(parts) >= 2, f"{path.name}:{line_number}: malformed metadata")
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
    rows = []
    for source in reader:
        require(None not in source and None not in source.values(),
                f"{path.name}: malformed row")
        row = {}
        for field in INTEGER_FIELDS:
            row[field] = integer(source[field], f"{path.name}:{field}")
        for field in SIGNED_INTEGER_FIELDS:
            row[field] = integer(source[field], f"{path.name}:{field}", nonnegative=False)
        for field in FLOAT_FIELDS:
            row[field] = finite_number(source[field], f"{path.name}:{field}")
        row["phase"] = source["phase"]
        require(row["phase"] in PHASES, f"{path.name}: unexpected phase")
        require((row["L"], row["k"], row["chain"], row["kind"]) == (size, mode, chain, kind),
                f"{path.name}: unexpected run key")
        require(row["count"] == BLOCK_LENGTH, f"{path.name}: unexpected block length")
        for first, second in (("sumFn", "sumFn2"), ("sumFi", "sumFi2"), ("sumBn", "sumBn2"),
                              ("sumBi", "sumBi2"), ("sumPFi", "sumPFi2"), ("sumY", "sumY2"),
                              ("sumS", "sumS2")):
            require(row[second] >= 0, f"{path.name}: negative second moment")
            tolerance = 1e-8 * max(1.0, row[first] ** 2, row["count"] * row[second])
            require(row[first] ** 2 <= row["count"] * row[second] + tolerance,
                    f"{path.name}: inconsistent first and second moments")
        # Derived additive fields: naive PF and PB are the indicator-1 sweep counts.
        row["PFn"] = sum(row[h] for h in HIST_F)
        row["PB"] = sum(row[h] for h in HIST_B)
        row["allMinus"] = row["secMinus"] + row["untMinus"]
        row["allPlus"] = row["secPlus"] + row["untPlus"]
        rows.append(row)
    seam = size * size
    sequence = expected_segments(size, kind, chain)
    expected_rows = sum(blocks for _, _, blocks in sequence)
    require(len(rows) == expected_rows, f"{path.name}: expected {expected_rows} block rows")
    ratio = RATIO[mode]
    low, high = RATIO_BOUNDS[mode]
    lo = first_twist(kind)
    ladder_chain = restricted and not top_dwell(kind, chain)
    index = 0
    forced_segments = 0
    for segment, (n, phase, blocks) in enumerate(sequence):
        segment_forced = None
        for block in range(blocks):
            row = rows[index]
            index += 1
            require(row["segment"] == segment and row["n"] == n and row["phase"] == phase
                    and row["block"] == block, f"{path.name}: block sequence differs from frozen order")
            count = row["count"]
            hist_f = [row[h] for h in HIST_F]
            hist_b = [row[h] for h in HIST_B]
            floor_f = 0.0 if restricted else low
            if n < seam:
                require(sum(hist_f) == (count if not restricted else sum(hist_f)) and sum(hist_f) <= count,
                        f"{path.name}: forward histogram count")
                if not restricted:
                    require(sum(hist_f) == count, f"{path.name}: forward histogram count")
                naive = math.fsum(hist_f[f] * ratio[f] for f in range(5))
                naive2 = math.fsum(hist_f[f] * ratio[f] ** 2 for f in range(5))
                require(close(row["sumFn"], naive, 1e-9) and close(row["sumFn2"], naive2, 1e-9),
                        f"{path.name}: naive forward sums disagree with the flux histogram")
                require(floor_f * count * (1 - 1e-9) <= row["sumFi"] <= high * count * (1 + 1e-9),
                        f"{path.name}: conditional forward estimator outside its exact bounds")
                require(0 <= row["sumPFi"] <= count * (1 + 1e-9) and row["sumPFi2"] <= count * (1 + 1e-9),
                        f"{path.name}: conditional forward indicator outside [0, 1]")
                if not restricted:
                    require(close(row["sumPFi"], count, 1e-12) and close(row["sumPFi2"], count, 1e-12),
                            f"{path.name}: unconstrained forward indicator differs from one")
            else:
                require(sum(hist_f) == 0 and all(row[f] == 0 for f in ("sumFn", "sumFn2", "sumFi", "sumFi2",
                                                                        "sumPFi", "sumPFi2")),
                        f"{path.name}: forward estimator recorded at the twisted endpoint")
            if n > lo or top_dwell(kind, chain):
                require(sum(hist_b) <= count, f"{path.name}: reverse histogram count")
                if not restricted:
                    require(sum(hist_b) == count, f"{path.name}: reverse histogram count")
                naive = math.fsum(hist_b[f] / ratio[(f - mode) % 5] for f in range(5))
                naive2 = math.fsum(hist_b[f] / ratio[(f - mode) % 5] ** 2 for f in range(5))
                require(close(row["sumBn"], naive, 1e-9) and close(row["sumBn2"], naive2, 1e-9),
                        f"{path.name}: naive reverse sums disagree with the flux histogram")
                require(floor_f * count * (1 - 1e-9) <= row["sumBi"] <= high * count * (1 + 1e-9),
                        f"{path.name}: conditional reverse estimator outside its exact bounds")
            elif n == 0:
                require(sum(hist_b) == 0 and all(row[f] == 0 for f in ("sumBn", "sumBn2", "sumBi", "sumBi2")),
                        f"{path.name}: reverse estimator recorded at the untwisted endpoint")
            else:
                # At twist 1 a restricted ladder chain records the reverse estimator of step 0 with
                # its class indicator (one for class 0, zero for class minus); the analyzer ignores it.
                require(sum(hist_b) <= count, f"{path.name}: reverse histogram count at the first twist")
            twisted = row["sec0"] + row["secMinus"] + row["secPlus"] + row["secOther"]
            require(twisted == count * n, f"{path.name}: twisted slice sector counts")
            require(row["untMinus"] + row["untPlus"] + row["untOther"] <= count * (seam - n),
                    f"{path.name}: untwisted sector counts")
            pure = row["pure0"] + row["pureMinus"] + row["purePlus"]
            require(pure <= count and row["flips"] <= count, f"{path.name}: pure or flip counts")
            require(row["classMinus"] <= count, f"{path.name}: class count")
            if n == 0:
                require(pure == 0 and row["classMinus"] == 0 and row["sumW"] == 0,
                        f"{path.name}: sector or class recorded without twisted slices")
            if kind == KIND_CLASS0:
                require(row["classMinus"] == 0, f"{path.name}: class-0 chain recorded in class minus")
            if kind == KIND_CLASSM:
                require(row["classMinus"] == count, f"{path.name}: class-minus chain recorded outside its class")
            # W is bounded by the twisted slice count: |w_j| <= 2 L^2 / 5 + 1 per slice.
            bound = n * (2 * seam // 5 + 1)
            require(-bound <= row["minW"] <= row["maxW"] <= bound, f"{path.name}: twisted-slice sum extremes out of range")
            require(count * row["minW"] <= row["sumW"] <= count * row["maxW"], f"{path.name}: twisted-slice sum out of range")
            if kind == KIND_CLASS0:
                require(2 * row["minW"] >= -n, f"{path.name}: class-0 block reaches class minus")
            if kind == KIND_CLASSM:
                require(2 * row["maxW"] < -n, f"{path.name}: class-minus block reaches class 0")
            require(row["forced"] in (0, 1), f"{path.name}: forced flag")
            if not ladder_chain or segment == 0:
                require(row["forced"] == 0, f"{path.name}: forced flag on a segment without a restricted up step")
            if segment_forced is None:
                segment_forced = row["forced"]
            require(row["forced"] == segment_forced, f"{path.name}: forced flag differs inside a segment")
        forced_segments += segment_forced or 0
    steps = len(sequence) - 1
    production = sum(blocks for _, _, blocks in sequence) * BLOCK_LENGTH
    sweeps_total = (WARMUP_SWEEPS + production + (steps - forced_segments) * EQUILIBRATION_SWEEPS
                    + forced_segments * POST_FORCING_SWEEPS)
    required_metadata = {
        "format": "twist_snake_sector_blocks_v2", "L": str(size), "k": str(mode), "chain": str(chain),
        "kind": str(kind), "kind_name": KIND_NAMES[kind], "base": str(BASE[kind]),
        "restriction": str(RESTRICTION[kind]), "schedule": schedule_name(kind, chain),
        "seed": str(SEED_BASE + 1000 * size + 100 * mode + 10 * kind + chain),
        "seam_size": str(seam), "start_twist": str(start_twist(size, kind, chain)),
        "chain_initial": initial_name(kind, chain),
        "warmup_sweeps": str(WARMUP_SWEEPS), "dwell_sweeps": str(DWELL_SWEEPS),
        "dwell_long_sweeps": str(DWELL_LONG_SWEEPS),
        "visit_sweeps": str(VISIT_SWEEPS), "equilibration_sweeps": str(EQUILIBRATION_SWEEPS),
        "post_forcing_sweeps": str(POST_FORCING_SWEEPS),
        "block_length": str(BLOCK_LENGTH), "segments": str(len(sequence)),
        "seam_order": "x2_fastest_then_x3",
        "class_rule": "class0_if_2W_ge_minus_n_else_classMinus",
        "sampling": "every_production_sweep_after_full_heatbath_sweep",
        "final_twist": str(final_twist(size, kind, chain)),
        "forced_steps": str(forced_segments),
        "sweeps_total": str(sweeps_total),
        "completion": "PASS",
    }
    for field, value in required_metadata.items():
        require(metadata.get(field) == value, f"{path.name}: incorrect {field}")
    return {"key": expected_key, "rows": rows, "metadata": metadata, "file": path.name,
            "sha256": hashlib.sha256(raw).hexdigest()}


# ---------------------------------------------------------------------------
# Batches and ensembles


def batches(rows, factor):
    """Coarsen consecutive blocks inside one segment only; never across segments.

    Every returned batch has the same sweep count, so unweighted batch means
    average exactly to the pooled mean. Batch values are per-sweep means.
    """
    result = []
    by_segment = {}
    for row in rows:
        by_segment.setdefault((row["chain"], row["segment"]), []).append(row)
    for (chain, _), group in sorted(by_segment.items()):
        group = sorted(group, key=lambda item: item["block"])
        require(len(group) % factor == 0, "incomplete coarsening group")
        segment_blocks = group[-1]["block"] + 1
        for start in range(0, len(group), factor):
            chunk = group[start:start + factor]
            count = sum(r["count"] for r in chunk)
            batch = {"chain": chain, "phase": chunk[0]["phase"], "count": count, "n": chunk[0]["n"],
                     "half": 0 if chunk[0]["block"] < segment_blocks // 2 else 1}
            for field in BATCH_FIELDS:
                batch[field] = math.fsum(r[field] for r in chunk) / count
            result.append(batch)
    return result


def variance(values):
    require(len(values) >= 2, "not enough batches for a variance")
    return statistics.variance(values)


GROUP_KEYS = {"chain": lambda b: b["chain"], "phase": lambda b: b["phase"],
              "chain_half": lambda b: (b["chain"], b["half"])}


def within_variance(values_by_group):
    """Pooled variance of deviations from each group's own mean, dof = N - G."""
    total = 0.0
    n = 0
    for values in values_by_group.values():
        m = mean(values)
        total += math.fsum((v - m) ** 2 for v in values)
        n += len(values)
    dof = n - len(values_by_group)
    require(dof >= 1, "not enough batches for a within-group variance")
    return total / dof


def grouped(batch_list, values, group):
    key = GROUP_KEYS[group]
    result = {}
    for batch, value in zip(batch_list, values):
        result.setdefault(key(batch), []).append(value)
    return result


def mean(values):
    return math.fsum(values) / len(values)


def se_max(by_scale):
    return max(by_scale.values())


# The four step estimators: (field of the pooled mean, batch field, side).
FORWARD_FIELDS = (("F", "sumFi"), ("PF", "sumPFi"))
REVERSE_FIELDS = (("PB", "PB"), ("Bw", "sumBi"))


class Ensemble:
    """All batches at one twist count m, at every scale, with the pooled means of
    the four step estimators (conditional forms) and their relative batch
    variances at the finest scale. A pooled mean of zero makes the ensemble
    degenerate: no log exists and the ladder cannot be formed."""

    def __init__(self, rows, m, seam, lo):
        self.m = m
        self.rows = [r for r in rows if r["n"] == m]
        require(self.rows, f"ensemble {m}: absent samples")
        self.has_forward = m < seam
        self.has_reverse = m > lo
        self.batches = {scale: batches(self.rows, factor) for scale, factor in zip(SCALES, COARSENING)}
        count = sum(r["count"] for r in self.rows)
        self.samples = count
        self.mean = {}
        self.naive = {}
        self.rv = {}
        self.zero = []
        fine = self.batches[SCALES[0]]
        for name, field in (FORWARD_FIELDS if self.has_forward else ()) + (REVERSE_FIELDS if self.has_reverse else ()):
            value = math.fsum(r[field] for r in self.rows) / count
            self.mean[name] = value
            if value > 0:
                self.rv[name] = variance([b[field] for b in fine]) / (len(fine) * value ** 2)
            else:
                self.zero.append(name)
        if self.has_forward:
            self.naive["F"] = math.fsum(r["sumFn"] for r in self.rows) / count
            self.naive["PF"] = math.fsum(r["PFn"] for r in self.rows) / count
        if self.has_reverse:
            self.naive["Bw"] = math.fsum(r["sumBn"] for r in self.rows) / count
            self.naive["PB"] = self.mean["PB"]

    def log(self, name):
        """First-order bias-corrected log of a pooled mean."""
        return math.log(self.mean[name]) + 0.5 * self.rv[name]


def uses_forward(m, lo, hi):
    return lo <= m < hi


def uses_reverse(m, lo, hi):
    return lo < m <= hi


def influence(ensemble, batch, lo, hi):
    """Per-batch linearised contribution u_b to the log ratio over steps [lo, hi)."""
    m = ensemble.m
    value = 0.0
    if uses_forward(m, lo, hi):
        value += 0.5 * (batch["sumFi"] / ensemble.mean["F"] + batch["sumPFi"] / ensemble.mean["PF"])
    if uses_reverse(m, lo, hi):
        value -= 0.5 * (batch["PB"] / ensemble.mean["PB"] + batch["sumBi"] / ensemble.mean["Bw"])
    return value


def deficit_influence(ensemble, batch, lo, hi):
    """Per-batch contribution v_b to the pairing deficit (F/PB against PF/Bw)."""
    m = ensemble.m
    value = 0.0
    if uses_forward(m, lo, hi):
        value += batch["sumFi"] / ensemble.mean["F"] - batch["sumPFi"] / ensemble.mean["PF"]
    if uses_reverse(m, lo, hi):
        value += batch["sumBi"] / ensemble.mean["Bw"] - batch["PB"] / ensemble.mean["PB"]
    return value


def contribution(ensemble, lo, hi, logs=None):
    """c_m for the pooled ensemble, or for supplied subset logs, over steps [lo, hi)."""
    m = ensemble.m
    logs = logs or {}

    def log_of(name):
        return logs[name] if name in logs else ensemble.log(name)

    value = 0.0
    if uses_forward(m, lo, hi):
        value += 0.5 * (log_of("F") + log_of("PF"))
    if uses_reverse(m, lo, hi):
        value -= 0.5 * (log_of("PB") + log_of("Bw"))
    return value


def subset_logs(ensemble, predicate):
    """Bias-corrected logs of the four means over a subset of rows (finest scale)."""
    rows = [r for r in ensemble.rows if predicate(r)]
    if not rows:
        return None, 0
    count = sum(r["count"] for r in rows)
    fine = batches(rows, 1)
    logs = {}
    for name, field in (FORWARD_FIELDS if ensemble.has_forward else ()) + (REVERSE_FIELDS if ensemble.has_reverse else ()):
        value = math.fsum(r[field] for r in rows) / count
        if value <= 0:
            return None, count  # a zero subset mean: no log exists (a sampling outcome, not a custody defect)
        rv = variance([b[field] for b in fine]) / (len(fine) * value ** 2) if len(fine) >= 2 else 0.0
        logs[name] = math.log(value) + 0.5 * rv
    return logs, count


def bar_log_ratio(forward_hist, reverse_hist, mode):
    """Bennett acceptance ratio from exact integer flux histograms (secondary value,
    unconstrained ladders only).

    With l_f = log W(f+k) - log W(f) the log weight ratio h_{n+1}/h_n of a
    forward sample with flux f, and l_{f-k} that of a reverse sample whose
    effective flux is f, the exact identity E_n sigma(l - C) = E_{n+1} sigma(C - l)
    at C = log r_n gives the estimating equation solved here by bisection.
    """
    logs = [math.log(RATIO[mode][f]) for f in range(5)]
    n_f = sum(forward_hist)
    n_b = sum(reverse_hist)
    require(n_f > 0 and n_b > 0, "BAR requires samples on both sides")

    def sigma(t):
        if t >= 0:
            return 1.0 / (1.0 + math.exp(-t))
        e = math.exp(t)
        return e / (1.0 + e)

    def residual(c):
        left = math.fsum(forward_hist[f] * sigma(logs[f] - c) for f in range(5)) / n_f
        right = math.fsum(reverse_hist[f] * sigma(c - logs[(f - mode) % 5]) for f in range(5)) / n_b
        return left - right  # decreasing in c

    low, high = min(logs) - 5.0, max(logs) + 5.0
    require(residual(low) > 0 > residual(high), "BAR equation has no bracketed root")
    for _ in range(200):
        mid = 0.5 * (low + high)
        if residual(mid) > 0:
            low = mid
        else:
            high = mid
    return 0.5 * (low + high)


# ---------------------------------------------------------------------------
# Ladder analysis


class Ladder:
    def __init__(self, rows, seam, mode, lo):
        self.seam = seam
        self.mode = mode
        self.lo = lo
        self.subset_scales = RESTRICTED_SUBSET_SCALES if lo == 1 else SCALES
        self.ensembles = [Ensemble(rows, m, seam, lo) for m in range(lo, seam + 1)]
        self.zero_means = [(e.m, name) for e in self.ensembles for name in e.zero]
        self._pooled = {}

    @property
    def degenerate(self):
        return bool(self.zero_means)

    def pooled_variance(self, group):
        """Within-group pooled variance of the full-range influence at every m and scale."""
        if group not in self._pooled:
            table = {}
            for scale in self.subset_scales:
                table[scale] = {}
                for e in self.ensembles:
                    u = [influence(e, b, self.lo, self.seam) for b in e.batches[scale]]
                    table[scale][e.m] = within_variance(grouped(e.batches[scale], u, group))
            self._pooled[group] = table
        return self._pooled[group]

    def partial(self, lo, hi):
        """Pooled log ratio over steps [lo, hi) with aggregate batch SE by scale."""
        total = math.fsum(contribution(e, lo, hi) for e in self.ensembles)
        se_by_scale = {}
        for scale in SCALES:
            var_total = 0.0
            for e in self.ensembles:
                if not (uses_forward(e.m, lo, hi) or uses_reverse(e.m, lo, hi)):
                    continue
                u = [influence(e, b, lo, hi) for b in e.batches[scale]]
                var_total += variance(u) / len(u)
            se_by_scale[scale] = math.sqrt(var_total)
        return total, se_by_scale

    def deficit(self):
        """Pairing deficit sum_n [(log F - log PB) - (log PF - log Bw)], zero in expectation."""
        total = 0.0
        for e in self.ensembles:
            if e.has_forward:
                total += e.log("F") - e.log("PF")
            if e.has_reverse:
                total += e.log("Bw") - e.log("PB")
        se_by_scale = {}
        for scale in SCALES:
            var_total = 0.0
            for e in self.ensembles:
                v = [deficit_influence(e, b, self.lo, self.seam) for b in e.batches[scale]]
                var_total += variance(v) / len(v)
            se_by_scale[scale] = math.sqrt(var_total)
        return total, se_by_scale

    def subset(self, predicate, group, ensembles=None):
        """log ratio over the full step range from a subset of rows, restricted to the
        listed ensembles (all by default); SE from the within-`group` pooled variance.
        Returns (None, None) when the subset has a zero estimator mean at some twist."""
        pooled = self.pooled_variance(group)
        chosen = set(range(self.lo, self.seam + 1)) if ensembles is None else set(ensembles)
        total = 0.0
        se_by_scale = {scale: 0.0 for scale in self.subset_scales}
        for e in self.ensembles:
            if e.m not in chosen:
                continue
            logs, count = subset_logs(e, predicate)
            require(count > 0, f"ensemble {e.m}: subset has no samples")
            if logs is None:
                return None, None
            total += contribution(e, self.lo, self.seam, logs)
            for scale, factor in zip(SCALES, COARSENING):
                if scale not in self.subset_scales:
                    continue
                n_batches = count // (BLOCK_LENGTH * factor)
                require(n_batches >= 1, "subset too small for this scale")
                se_by_scale[scale] += pooled[scale][e.m] / n_batches
        return total, {scale: math.sqrt(v) for scale, v in se_by_scale.items()}

    def consistency(self, restricted):
        """Naive versus conditional estimators, paired by block (linear form, exactly
        zero-mean): F, Bw and, for restricted ladders, PF. PB has no conditional form."""
        result = {}
        sides = [("F", "sumFn", "sumFi", "has_forward"), ("Bw", "sumBn", "sumBi", "has_reverse")]
        if restricted:
            sides.append(("PF", "PFn", "sumPFi", "has_forward"))
        for name, field_naive, field_imp, attribute in sides:
            statistic = 0.0
            se_scale = {}
            for scale in SCALES:
                total = 0.0
                for e in self.ensembles:
                    if not getattr(e, attribute) or name in e.zero:
                        continue
                    improved = e.mean[name]
                    diffs = [b[field_naive] - b[field_imp] for b in e.batches[scale]]
                    total += variance(diffs) / (len(diffs) * improved ** 2)
                    if scale == SCALES[0]:
                        statistic += mean(diffs) / improved
                se_scale[scale] = math.sqrt(total)
            result[name] = {"statistic": statistic, "se": se_max(se_scale), "se_by_block_length": se_scale}
        return result

    def steps(self, bar):
        table = []
        bar_total = 0.0 if bar else None
        for n in range(self.lo, self.seam):
            e, f = self.ensembles[n - self.lo], self.ensembles[n + 1 - self.lo]
            hist_f = [sum(r[h] for r in e.rows) for h in HIST_F]
            hist_b = [sum(r[h] for r in f.rows) for h in HIST_B]
            entry = {
                "n": n,
                "log_r": 0.5 * (e.log("F") + e.log("PF") - f.log("PB") - f.log("Bw")),
                "log_r_pairing_A": e.log("F") - f.log("PB"),
                "log_r_pairing_B": e.log("PF") - f.log("Bw"),
                "F_conditional": e.mean["F"], "F_naive": e.naive["F"],
                "PF_conditional": e.mean["PF"], "PF_naive": e.naive["PF"],
                "PB": f.mean["PB"],
                "Bw_conditional": f.mean["Bw"], "Bw_naive": f.naive["Bw"],
                "forward_samples": e.samples, "reverse_samples": f.samples,
                "forward_flux_histogram": hist_f, "reverse_flux_histogram": hist_b,
            }
            if bar:
                entry["log_r_bar"] = bar_log_ratio(hist_f, hist_b, self.mode)
                bar_total += entry["log_r_bar"]
            table.append(entry)
        return table, bar_total


def mean_summary(rows, field, group=None):
    """Pooled per-sweep mean of an additive block field with batch SE at every scale;
    optionally the within-`group` pooled variance for subset comparisons."""
    count = sum(r["count"] for r in rows)
    value = math.fsum(r[field] for r in rows) / count
    se_by_scale = {}
    var_by_scale = {}
    within_by_scale = {}
    for scale, factor in zip(SCALES, COARSENING):
        batch_list = batches(rows, factor)
        values = [b[field] for b in batch_list]
        var_by_scale[scale] = variance(values)
        se_by_scale[scale] = math.sqrt(var_by_scale[scale] / len(values))
        if group is not None:
            within_by_scale[scale] = within_variance(grouped(batch_list, values, group))
    return {"mean": value, "count": count, "se_by_block_length": se_by_scale,
            "se": se_max(se_by_scale), "variance_by_block_length": var_by_scale,
            "within_variance_by_block_length": within_by_scale}


def subset_mean(rows, field, pooled_variance_by_scale):
    count = sum(r["count"] for r in rows)
    value = math.fsum(r[field] for r in rows) / count
    se_by_scale = {scale: math.sqrt(pooled_variance_by_scale[scale] / (count // (BLOCK_LENGTH * factor)))
                   for scale, factor in zip(SCALES, COARSENING)}
    return value, se_by_scale


def agree(first, first_se, second, second_se):
    """Within 4 sqrt(SE^2 + SE^2); the relative term 1e-12 absorbs summation roundoff when
    both standard errors vanish (identical constant blocks) and is negligible otherwise."""
    return abs(first - second) <= MULTIPLIER * math.hypot(first_se, second_se) + 1e-12 * (abs(first) + abs(second))


def coarsening_ratio(errors):
    """None when any scale has zero standard error (degenerate)."""
    values = list(errors.values())
    if min(values) <= 0:
        return None
    return max(values) / min(values)


def fraction(rows, field):
    return sum(r[field] for r in rows) / sum(r["count"] for r in rows)


def sector_summary(rows, seam):
    """Descriptive sector occupancy of a set of rows."""
    sweeps = sum(r["count"] for r in rows)
    twisted_slices = sum(r["count"] * r["n"] for r in rows)
    untwisted_slices = sum(r["count"] * (seam - r["n"]) for r in rows)
    result = {"class_minus_fraction": fraction(rows, "classMinus"),
              "mean_W": sum(r["sumW"] for r in rows) / sweeps,
              "pure0_fraction": fraction(rows, "pure0"), "pureMinus_fraction": fraction(rows, "pureMinus"),
              "purePlus_fraction": fraction(rows, "purePlus"), "flips": sum(r["flips"] for r in rows),
              "all_slice_fractions": {"wMinus": sum(r["allMinus"] for r in rows) / (sweeps * seam),
                                      "wPlus": sum(r["allPlus"] for r in rows) / (sweeps * seam)},
              "untwisted_slice_fractions": None, "twisted_slice_fractions": None}
    if untwisted_slices:
        result["untwisted_slice_fractions"] = {
            "wMinus": sum(r["untMinus"] for r in rows) / untwisted_slices,
            "wPlus": sum(r["untPlus"] for r in rows) / untwisted_slices,
            "other": sum(r["untOther"] for r in rows) / untwisted_slices,
        }
    if twisted_slices:
        result["twisted_slice_fractions"] = {
            "w0": sum(r["sec0"] for r in rows) / twisted_slices,
            "wMinus": sum(r["secMinus"] for r in rows) / twisted_slices,
            "wPlus": sum(r["secPlus"] for r in rows) / twisted_slices,
            "other": sum(r["secOther"] for r in rows) / twisted_slices,
        }
    return result


def leave_one_out(rows, field, chains, summary, prefix, failures, tag):
    """Each chain's per-sweep mean of `field` against the other chains, within-chain pooled variance."""
    for chain in chains:
        own, own_se = subset_mean([r for r in rows if r["chain"] == chain], field,
                                  summary["within_variance_by_block_length"])
        others, others_se = subset_mean([r for r in rows if r["chain"] != chain], field,
                                        summary["within_variance_by_block_length"])
        if not agree(own, se_max(own_se), others, se_max(others_se)):
            failures.append(f"{prefix}{chain}:{tag}")


def chain_values(rows, field, chains):
    return {chain: fraction([r for r in rows if r["chain"] == chain], field) for chain in chains}


def between_chain_se(values):
    values = list(values)
    return statistics.stdev(values) / math.sqrt(len(values)) if len(values) >= 2 else 0.0


# ---------------------------------------------------------------------------
# U route: unconstrained round-trip ladder, as in the consumed predecessor,
# with the sector gate G9' on class-minus and w=-1 slice fractions.


def analyze_unconstrained(runs, size, mode):
    seam = size * size
    rows = [r for run in runs for r in run["rows"]]
    chains = sorted(run["key"][3] for run in runs)
    failures = []
    consistency_failures = []
    sector_failures = []
    calibration_failures = []
    ladder = Ladder(rows, seam, mode, 0)
    require(not ladder.degenerate, "unconstrained ladder has a zero estimator mean")
    log_R, log_R_se_by_scale = ladder.partial(0, seam)
    deficit, deficit_se_by_scale = ladder.deficit()
    consistency = ladder.consistency(False)
    steps, log_R_bar = ladder.steps(True)
    twisted_rows = [r for r in rows if r["n"] == seam]
    untwisted_rows = [r for r in rows if r["n"] == 0]
    # G8a uses only chains 0 and 1, whose initial laws are reversal symmetric.
    symmetric_untwisted_rows = [r for r in untwisted_rows if r["chain"] in (0, 1)]
    y_twisted = mean_summary(twisted_rows, "sumY", "chain")
    y_twisted_halves = mean_summary(twisted_rows, "sumY", "chain_half")
    y_untwisted = mean_summary(symmetric_untwisted_rows, "sumY")
    y_untwisted_all = mean_summary(untwisted_rows, "sumY")
    y2_untwisted = mean_summary(untwisted_rows, "sumY2")
    class_minus = mean_summary(twisted_rows, "classMinus", "chain")
    slice_minus = mean_summary(twisted_rows, "secMinus", "chain")
    # G2 pairing (forward-reverse) consistency of the whole ladder.
    if abs(deficit) > MULTIPLIER * se_max(deficit_se_by_scale):
        failures.append("pooled:forward_reverse_deficit")
    # G6 naive versus conditional estimators.
    for name in ("F", "Bw"):
        if abs(consistency[name]["statistic"]) > MULTIPLIER * consistency[name]["se"]:
            consistency_failures.append(f"pooled:naive_conditional_{name}_disagreement")
    chain_results = []
    chain_log_R = {}
    chain_Y = {}
    for run in runs:
        chain = run["key"][3]
        chain_log_R[chain] = ladder.subset(lambda r, c=chain: r["chain"] == c, "chain")
        chain_Y[chain] = subset_mean([r for r in twisted_rows if r["chain"] == chain], "sumY",
                                     y_twisted["within_variance_by_block_length"])
    for run in runs:
        chain = run["key"][3]
        prefix = f"chain_{chain}:"
        # G3 start independence against the other chains (pooled batch variance).
        own, own_se = chain_log_R[chain]
        others, others_se = ladder.subset(lambda r, c=chain: r["chain"] != c, "chain")
        require(own is not None and others is not None, "unconstrained subset has a zero estimator mean")
        if not agree(own, se_max(own_se), others, se_max(others_se)):
            failures.append(prefix + "log_R_disagreement")
        own_y, own_y_se = chain_Y[chain]
        others_y, others_y_se = subset_mean([r for r in twisted_rows if r["chain"] != chain], "sumY",
                                            y_twisted["within_variance_by_block_length"])
        if not agree(own_y, se_max(own_y_se), others_y, se_max(others_y_se)):
            failures.append(prefix + "mean_Y_disagreement")
        # G5 time halves of the twisted dwell (within chain-half pooled variance).
        dwell = sorted([r for r in twisted_rows if r["chain"] == chain], key=lambda r: r["block"])
        halves = [subset_mean(dwell[:len(dwell) // 2], "sumY", y_twisted_halves["within_variance_by_block_length"]),
                  subset_mean(dwell[len(dwell) // 2:], "sumY", y_twisted_halves["within_variance_by_block_length"])]
        if not agree(halves[0][0], se_max(halves[0][1]), halves[1][0], se_max(halves[1][1])):
            failures.append(prefix + "twisted_dwell_half_disagreement")
        directions = {}
        for phase in ("up", "down"):
            value, _ = ladder.subset(lambda r, c=chain, p=phase: r["chain"] == c and r["phase"] == p,
                                     "phase", range(1, seam))
            directions[phase] = value
        chain_rows = run["rows"]
        chain_results.append({
            "chain": chain, "initial": initial_name(KIND_MAIN, chain), "label": "NONINFERENTIAL_ESTIMATE",
            "log_R": own, "log_R_se_pooled_variance": se_max(own_se),
            "log_R_intermediate_by_direction": directions,
            "mean_Y_twisted": own_y, "mean_Y_twisted_se_pooled_variance": se_max(own_y_se),
            "twisted_dwell_halves": [halves[0][0], halves[1][0]],
            "sector_twisted_dwell": sector_summary(dwell, seam),
            "sector_down_rows": sector_summary([r for r in chain_rows if r["phase"] == "down"], seam),
            "sector_up_rows": sector_summary([r for r in chain_rows if r["phase"] == "up"], seam),
            "sector_untwisted_dwell": sector_summary([r for r in chain_rows if r["n"] == 0], seam),
            "sector_twist_one_rows": sector_summary([r for r in chain_rows if r["n"] == 1], seam),
            "descriptive_moments_only": {
                "mean_Y_twisted_squared": math.fsum(r["sumY2"] for r in dwell) / sum(r["count"] for r in dwell),
                "mean_action_twisted": math.fsum(r["sumS"] for r in dwell) / sum(r["count"] for r in dwell),
            },
            "input_file": run["file"], "input_sha256": run["sha256"],
        })
    # G9' sector occupancy at the twisted dwell: class-minus fraction and w=-1 twisted-slice
    # count per sweep, each chain against the others (within-chain pooled variance).
    leave_one_out(twisted_rows, "classMinus", chains, class_minus, "chain_", sector_failures,
                  "class_minus_occupancy_disagreement")
    leave_one_out(twisted_rows, "secMinus", chains, slice_minus, "chain_", sector_failures,
                  "wMinus_slice_occupancy_disagreement")
    # G4 direction independence over the intermediate ensembles (dwell rows cancel exactly).
    up, up_se = ladder.subset(lambda r: r["phase"] == "up", "phase", range(1, seam))
    down, down_se = ladder.subset(lambda r: r["phase"] == "down", "phase", range(1, seam))
    delta = up - down
    delta_se = {scale: math.hypot(up_se[scale], down_se[scale]) for scale in SCALES}
    if abs(delta) > MULTIPLIER * se_max(delta_se):
        failures.append("pooled:direction_disagreement")
    # G7 coarsening stability of the aggregate standard errors.
    ratios = {"log_R": coarsening_ratio(log_R_se_by_scale),
              "mean_Y_twisted": coarsening_ratio(y_twisted["se_by_block_length"])}
    degenerate = any(value is None for value in ratios.values())
    for name, value in ratios.items():
        if value is None:
            failures.append(f"pooled:{name}_degenerate_se")
        elif value > THRESHOLDS["maximum_se_coarsening_ratio"]:
            failures.append(f"pooled:{name}_coarsening_instability")
    # G8a: batch-SE calibration against the exactly known mean of chains 0 and 1 (not an
    # equilibration test); G8b: exact bound of the stationary law. Both also cap the
    # class-sum route because r_0 uses the same n=0 rows of chains 0 and 1.
    if abs(y_untwisted["mean"]) > MULTIPLIER * y_untwisted["se"]:
        calibration_failures.append("chains_0_1:untwisted_mean_Y_nonzero")
    if y2_untwisted["mean"] - MULTIPLIER * y2_untwisted["se"] > THRESHOLDS["maximum_untwisted_mean_Y_squared"]:
        calibration_failures.append("pooled:untwisted_mean_Y_squared_above_one")
    values = [chain_log_R[c][0] for c in chains]
    se_report_log_R = max(se_max(log_R_se_by_scale), between_chain_se(values))
    y_values = [chain_Y[c][0] for c in chains]
    se_report_Y = max(y_twisted["se"], between_chain_se(y_values))
    passes = not (failures or consistency_failures or sector_failures or calibration_failures or degenerate)
    if consistency_failures:
        status = "FAIL_CONSISTENCY"
    elif failures or calibration_failures or degenerate:
        status = "INCONCLUSIVE_EQUILIBRATION"
    elif sector_failures:
        status = SECTOR_FROZEN
    else:
        status = GATES_PASSED
    twist_one_rows = [r for r in rows if r["n"] == 1]
    up_one_rows = [r for r in twist_one_rows if r["chain"] in (0, 1) and r["phase"] == "up"]
    pi1_up = mean_summary(up_one_rows, "classMinus")
    log_r0, log_r0_se = ladder.partial(0, 1)
    return {
        "route": "U", "k": mode, "status": status,
        "log_r0": log_r0, "log_r0_se_batch": se_max(log_r0_se),
        "pi1_minus_chains_0_1_up": pi1_up["mean"], "pi1_minus_chains_0_1_up_se": pi1_up["se"],
        "estimate_label": "EMPIRICAL_ENGINEERING_ONLY" if passes else "NONINFERENTIAL_ESTIMATE",
        "log_R": log_R, "log_R_se_batch": se_max(log_R_se_by_scale),
        "log_R_se_between_chains": between_chain_se(values), "log_R_se_report": se_report_log_R,
        "log_R_se_by_block_length": log_R_se_by_scale,
        "log_R_bar": log_R_bar,
        "forward_reverse_deficit": deficit, "forward_reverse_deficit_se": se_max(deficit_se_by_scale),
        "naive_conditional_consistency": consistency,
        "direction_split": {"up_minus_down_log_R": delta, "se": se_max(delta_se), "up": up, "down": down},
        "mean_Y_twisted": y_twisted["mean"], "mean_Y_twisted_se_batch": y_twisted["se"],
        "mean_Y_twisted_se_between_chains": between_chain_se(y_values), "mean_Y_twisted_se_report": se_report_Y,
        "mean_Y_twisted_se_by_block_length": y_twisted["se_by_block_length"],
        "mean_Y_twisted_squared": mean_summary(twisted_rows, "sumY2")["mean"],
        "mean_Y_untwisted_chains_0_1": y_untwisted["mean"], "mean_Y_untwisted_chains_0_1_se": y_untwisted["se"],
        "mean_Y_untwisted_all_chains": y_untwisted_all["mean"], "mean_Y_untwisted_all_chains_se": y_untwisted_all["se"],
        "mean_Y_untwisted_squared": y2_untwisted["mean"], "mean_Y_untwisted_squared_se": y2_untwisted["se"],
        "mean_action_untwisted": mean_summary(untwisted_rows, "sumS")["mean"],
        "mean_action_twisted": mean_summary(twisted_rows, "sumS")["mean"],
        "sector_twisted_dwell_pooled": sector_summary(twisted_rows, seam),
        "class_minus_fraction_twisted_by_chain": chain_values(twisted_rows, "classMinus", chains),
        "wMinus_twisted_slice_fraction_by_chain": {c: v / seam for c, v in chain_values(twisted_rows, "secMinus", chains).items()},
        "twist_one_class_minus_fraction_all_rows": fraction(twist_one_rows, "classMinus"),
        "twist_one_class_minus_fraction_chains_0_1_up": fraction(up_one_rows, "classMinus"),
        "coarsening_se_ratios": ratios,
        "diagnostic_failures": failures, "consistency_failures": consistency_failures,
        "sector_failures": sector_failures, "calibration_failures": calibration_failures,
        "chains": chain_results, "steps": steps,
    }


# ---------------------------------------------------------------------------
# P route: the step-zero group (dwell at twist 0, one step, dwell at twist 1).


def analyze_pi1(runs, size, mode):
    seam = size * size
    rows = [r for run in runs for r in run["rows"]]
    chains = sorted(run["key"][3] for run in runs)
    failures = []
    calibration_failures = []
    zero_rows = [r for r in rows if r["n"] == 0]
    one_rows = [r for r in rows if r["n"] == 1]
    require(zero_rows and one_rows and len(zero_rows) + len(one_rows) == len(rows), "step-zero rows away from twists 0 and 1")
    pi_minus = mean_summary(one_rows, "classMinus", "chain")
    y1 = mean_summary(one_rows, "sumY", "chain")
    bw = mean_summary(one_rows, "sumBi", "chain")
    f0 = mean_summary(zero_rows, "sumFi", "chain")
    y0 = mean_summary(zero_rows, "sumY", "chain")
    y0_squared = mean_summary(zero_rows, "sumY2")
    pi_halves = mean_summary(one_rows, "classMinus", "chain_half")
    y1_halves = mean_summary(one_rows, "sumY", "chain_half")
    y0_halves = mean_summary(zero_rows, "sumY", "chain_half")
    # Chain agreement (cold against hot) at both dwells.
    for rows_, field, summary, tag in ((one_rows, "classMinus", pi_minus, "class_minus_disagreement"),
                                      (one_rows, "sumY", y1, "mean_Y_twist_one_disagreement"),
                                      (one_rows, "sumBi", bw, "Bw0_disagreement"),
                                      (zero_rows, "sumFi", f0, "F0_disagreement"),
                                      (zero_rows, "sumY", y0, "mean_Y_twist_zero_disagreement")):
        leave_one_out(rows_, field, chains, summary, "P_chain_", failures, tag)
    # Time halves of each chain's dwells.
    for chain in chains:
        for rows_, field, summary, tag in ((one_rows, "classMinus", pi_halves, "class_minus_half_disagreement"),
                                          (one_rows, "sumY", y1_halves, "mean_Y_twist_one_half_disagreement"),
                                          (zero_rows, "sumY", y0_halves, "mean_Y_twist_zero_half_disagreement")):
            dwell = sorted([r for r in rows_ if r["chain"] == chain], key=lambda r: r["block"])
            halves = [subset_mean(dwell[:len(dwell) // 2], field, summary["within_variance_by_block_length"]),
                      subset_mean(dwell[len(dwell) // 2:], field, summary["within_variance_by_block_length"])]
            if not agree(halves[0][0], se_max(halves[0][1]), halves[1][0], se_max(halves[1][1])):
                failures.append(f"P_chain_{chain}:{tag}")
    # Coarsening stability of pi_1(-), mean Y at twist 1 and log r_0.
    r0 = log_step_zero(zero_rows, one_rows)
    ratios = {"pi1_minus": coarsening_ratio(pi_minus["se_by_block_length"]),
              "mean_Y_twist_one": coarsening_ratio(y1["se_by_block_length"]),
              "log_r0": coarsening_ratio(r0["log_r0_se_by_block_length"])}
    for name, value in ratios.items():
        if value is None:
            failures.append(f"P_pooled:{name}_degenerate_se")
        elif value > THRESHOLDS["maximum_se_coarsening_ratio"]:
            failures.append(f"P_pooled:{name}_coarsening_instability")
    # Calibration against the exactly known mean of Y at twist 0 (both initial laws are
    # reversal symmetric) and the exact bound on its square.
    if abs(y0["mean"]) > MULTIPLIER * y0["se"]:
        calibration_failures.append("P_pooled:untwisted_mean_Y_nonzero")
    if y0_squared["mean"] - MULTIPLIER * y0_squared["se"] > THRESHOLDS["maximum_untwisted_mean_Y_squared"]:
        calibration_failures.append("P_pooled:untwisted_mean_Y_squared_above_one")
    by_chain = chain_values(one_rows, "classMinus", chains)
    r0_by_chain = {}
    for chain in chains:
        try:
            r0_by_chain[chain] = log_step_zero([r for r in zero_rows if r["chain"] == chain],
                                               [r for r in one_rows if r["chain"] == chain])["log_r0"]
        except InvalidInput:
            r0_by_chain[chain] = None
    r0_values = [v for v in r0_by_chain.values() if v is not None]
    status = "INCONCLUSIVE_EQUILIBRATION" if failures or calibration_failures else GATES_PASSED
    return {
        "route": "P", "k": mode, "status": status,
        "pi1_minus": pi_minus["mean"], "pi1_minus_se_batch": pi_minus["se"],
        "pi1_minus_se_between_chains": between_chain_se(by_chain.values()),
        "pi1_minus_se_report": max(pi_minus["se"], between_chain_se(by_chain.values())),
        "pi1_minus_by_chain": by_chain,
        "log_r0": r0["log_r0"], "log_r0_se_batch": r0["log_r0_se_batch"],
        "log_r0_se_between_chains": between_chain_se(r0_values) if len(r0_values) >= 2 else 0.0,
        "log_r0_se_report": max(r0["log_r0_se_batch"], between_chain_se(r0_values) if len(r0_values) >= 2 else 0.0),
        "log_r0_by_chain": r0_by_chain, "step_zero": r0,
        "mean_Y_twist_one": y1["mean"], "mean_Y_twist_one_se": y1["se"],
        "mean_Y_twist_zero": y0["mean"], "mean_Y_twist_zero_se": y0["se"],
        "mean_Y_twist_zero_squared": y0_squared["mean"], "mean_Y_twist_zero_squared_se": y0_squared["se"],
        "mean_action_twist_zero": mean_summary(zero_rows, "sumS")["mean"],
        "sector_twist_one": sector_summary(one_rows, seam),
        "sector_twist_zero": sector_summary(zero_rows, seam),
        "coarsening_se_ratios": ratios, "diagnostic_failures": failures,
        "calibration_failures": calibration_failures,
        "chains": [{"chain": run["key"][3], "initial": initial_name(KIND_PI1, run["key"][3]),
                    "input_file": run["file"], "input_sha256": run["sha256"]} for run in runs],
    }


def log_step_zero(zero_rows, one_rows):
    """log r_0 = 1/2 [(log F_0 + rv/2) - (log Bw_0 + rv/2)] from the forward estimator at twist 0
    and the reverse estimator at twist 1 (PF = PB = 1 exactly for an unconstrained step);
    the two dwells are treated as independent samples."""
    f = mean_summary(zero_rows, "sumFi")
    b = mean_summary(one_rows, "sumBi")
    require(f["mean"] > 0 and b["mean"] > 0, "step 0 estimator mean is not positive")
    rv_f = f["se_by_block_length"][SCALES[0]] ** 2 / f["mean"] ** 2
    rv_b = b["se_by_block_length"][SCALES[0]] ** 2 / b["mean"] ** 2
    value = 0.5 * ((math.log(f["mean"]) + 0.5 * rv_f) - (math.log(b["mean"]) + 0.5 * rv_b))
    se_by_scale = {scale: 0.5 * math.hypot(f["se_by_block_length"][scale] / f["mean"],
                                           b["se_by_block_length"][scale] / b["mean"]) for scale in SCALES}
    return {"log_r0": value, "log_r0_se_batch": se_max(se_by_scale), "log_r0_se_by_block_length": se_by_scale,
            "F0": f["mean"], "F0_se": f["se"], "Bw0": b["mean"], "Bw0_se": b["se"]}


# ---------------------------------------------------------------------------
# C0 and CM routes: restricted up-only ladders from twist 1 to L^2 (chains 0, 1)
# and a chain dwelling at L^2 from the cold class layout (chain 2).


def analyze_restricted(runs, size, mode, kind):
    seam = size * size
    rows = [r for run in runs for r in run["rows"]]
    chains = sorted(run["key"][3] for run in runs)
    ladder_chains = [c for c in chains if c in LADDER_CHAINS]
    name = KIND_NAMES[kind]
    failures = []
    consistency_failures = []
    ladder = Ladder(rows, seam, mode, 1)
    twisted_rows = [r for r in rows if r["n"] == seam]
    y = mean_summary(twisted_rows, "sumY", "chain")
    w = mean_summary(twisted_rows, "sumW", "chain")
    all_minus = mean_summary(twisted_rows, "allMinus", "chain")
    y_halves = mean_summary(twisted_rows, "sumY", "chain_half")
    forced = {run["key"][3]: int(run["metadata"]["forced_steps"]) for run in runs}
    forced_by_parity = {"twist_odd": 0, "twist_even": 0}  # parity of the twist count reached by the reset step
    for run in runs:
        seen = set()
        for r in run["rows"]:
            key = (r["segment"], r["n"])
            if r["forced"] and key not in seen:
                seen.add(key)
                forced_by_parity["twist_odd" if r["n"] % 2 else "twist_even"] += 1
    chain_Y = {c: subset_mean([r for r in twisted_rows if r["chain"] == c], "sumY", y["within_variance_by_block_length"])
               for c in chains}
    result = {
        "route": name, "k": mode, "class": RESTRICTION[kind], "forced_steps_by_chain": forced,
        "forced_steps_by_parity_of_twist": forced_by_parity,
        "mean_Y_twisted": y["mean"], "mean_Y_twisted_se_batch": y["se"],
        "mean_Y_twisted_se_between_chains": between_chain_se([chain_Y[c][0] for c in chains]),
        "mean_Y_twisted_se_report": max(y["se"], between_chain_se([chain_Y[c][0] for c in chains])),
        "mean_Y_twisted_se_by_block_length": y["se_by_block_length"],
        "mean_Y_twisted_by_chain": {c: chain_Y[c][0] for c in chains},
        "mean_W_twisted_by_chain": chain_values(twisted_rows, "sumW", chains),
        "all_slice_wMinus_fraction_twisted_by_chain": {c: v / seam for c, v in chain_values(twisted_rows, "allMinus", chains).items()},
        "sector_twisted_dwell_pooled": sector_summary(twisted_rows, seam),
        "chains": [{"chain": run["key"][3], "initial": initial_name(kind, run["key"][3]),
                    "schedule": schedule_name(kind, run["key"][3]),
                    "input_file": run["file"], "input_sha256": run["sha256"]} for run in runs],
    }
    # G3 at the twisted dwell over all three chains: mean Y, mean W and all-slice w=-1 count.
    for field, summary, tag in (("sumY", y, "mean_Y_disagreement"), ("sumW", w, "mean_W_disagreement"),
                                ("allMinus", all_minus, "all_slice_wMinus_disagreement")):
        leave_one_out(twisted_rows, field, chains, summary, f"{name}_chain_", failures, tag)
    # G5 halves of every chain's twisted dwell.
    for chain in chains:
        dwell = sorted([r for r in twisted_rows if r["chain"] == chain], key=lambda r: r["block"])
        halves = [subset_mean(dwell[:len(dwell) // 2], "sumY", y_halves["within_variance_by_block_length"]),
                  subset_mean(dwell[len(dwell) // 2:], "sumY", y_halves["within_variance_by_block_length"])]
        if not agree(halves[0][0], se_max(halves[0][1]), halves[1][0], se_max(halves[1][1])):
            failures.append(f"{name}_chain_{chain}:twisted_dwell_half_disagreement")
    ratios = {"mean_Y_twisted": coarsening_ratio(y["se_by_block_length"])}
    # G6 naive against conditional for F, PF and Bw (ensembles with a zero mean skipped).
    consistency = ladder.consistency(True)
    for estimator in ("F", "PF", "Bw"):
        if abs(consistency[estimator]["statistic"]) > MULTIPLIER * consistency[estimator]["se"]:
            consistency_failures.append(f"{name}:naive_conditional_{estimator}_disagreement")
    result["naive_conditional_consistency"] = consistency
    if ladder.degenerate:
        failures.append(f"{name}:zero_estimator_mean:" + ",".join(f"m{m}:{e}" for m, e in ladder.zero_means))
        result.update({"status": "FAIL_CONSISTENCY" if consistency_failures else "INCONCLUSIVE_EQUILIBRATION",
                       "log_l": None, "log_l_se_batch": None, "log_l_se_report": None,
                       "diagnostic_failures": failures, "consistency_failures": consistency_failures,
                       "zero_means": ladder.zero_means, "coarsening_se_ratios": ratios})
        return result
    log_l, log_l_se_by_scale = ladder.partial(1, seam)
    deficit, deficit_se_by_scale = ladder.deficit()
    steps, _ = ladder.steps(False)
    # G2 pairing deficit.
    if abs(deficit) > MULTIPLIER * se_max(deficit_se_by_scale):
        failures.append(f"{name}:pairing_deficit")
    # G3 for the ladder sum: the two up-only chains against each other. A chain whose own
    # mean of some estimator vanishes at some twist has no ladder value (sampling outcome).
    chain_l = {c: ladder.subset(lambda r, c=c: r["chain"] == c, "chain") for c in ladder_chains}
    for chain in ladder_chains:
        own, own_se = chain_l[chain]
        others, others_se = ladder.subset(lambda r, c=chain: r["chain"] != c, "chain")
        if own is None or others is None:
            failures.append(f"{name}_chain_{chain}:zero_estimator_mean_in_subset")
        elif not agree(own, se_max(own_se), others, se_max(others_se)):
            failures.append(f"{name}_chain_{chain}:log_l_disagreement")
    ratios["log_l"] = coarsening_ratio(log_l_se_by_scale)
    for field, value in ratios.items():
        if value is None:
            failures.append(f"{name}_pooled:{field}_degenerate_se")
        elif value > THRESHOLDS["maximum_se_coarsening_ratio"]:
            failures.append(f"{name}_pooled:{field}_coarsening_instability")
    l_values = [chain_l[c][0] for c in ladder_chains if chain_l[c][0] is not None]
    between = between_chain_se(l_values) if len(l_values) == len(ladder_chains) else None
    status = ("FAIL_CONSISTENCY" if consistency_failures
              else "INCONCLUSIVE_EQUILIBRATION" if failures else GATES_PASSED)
    result.update({
        "status": status,
        "log_l": log_l, "log_l_se_batch": se_max(log_l_se_by_scale),
        "log_l_se_between_chains": between,
        "log_l_se_report": max(se_max(log_l_se_by_scale), between or 0.0),
        "log_l_se_by_block_length": log_l_se_by_scale, "log_l_by_chain": {c: chain_l[c][0] for c in ladder_chains},
        "pairing_deficit": deficit, "pairing_deficit_se": se_max(deficit_se_by_scale),
        "coarsening_se_ratios": ratios,
        "diagnostic_failures": failures, "consistency_failures": consistency_failures,
        "steps": steps,
    })
    return result


# ---------------------------------------------------------------------------
# Class sum


def class_sum(p_result, c0, cm):
    """The sum rule with delta-method errors; the inputs are treated as independent."""
    pi_m = p_result["pi1_minus"]
    pi_0 = 1.0 - pi_m
    l0, lm = c0["log_l"], cm["log_l"]
    a = (math.log(pi_0) if pi_0 > 0 else -math.inf) + l0
    b = (math.log(pi_m) if pi_m > 0 else -math.inf) + lm
    top = max(a, b)
    require(math.isfinite(top), "both class weights vanish")
    ea, eb = math.exp(a - top), math.exp(b - top)
    log_D = top + math.log(ea + eb)
    P0, Pm = ea / (ea + eb), eb / (ea + eb)
    log_R = p_result["log_r0"] + log_D
    # d log R / d pi_- = (e^{l_-} - e^{l_0}) / D ; d P_- / d pi_- = e^{l_0 + l_-} / D^2.
    d_pi = (math.exp(lm - top) - math.exp(l0 - top)) / (ea + eb)
    dP_dpi = math.exp(l0 + lm - 2 * log_D)
    Y0, Ym = c0["mean_Y_twisted"], cm["mean_Y_twisted"]
    Y = P0 * Y0 + Pm * Ym
    out = {"log_R": log_R, "P_minus": Pm, "P_zero": P0, "mean_Y": Y, "log_class_sum": log_D,
           "inputs": {"log_r0": p_result["log_r0"], "pi1_minus": pi_m, "l_0": l0, "l_minus": lm,
                      "Y_0": Y0, "Y_minus": Ym}}
    for label in ("batch", "report"):
        se_r0 = p_result["log_r0_se_" + label]
        se_pi = p_result["pi1_minus_se_" + label]
        se_l0 = c0["log_l_se_" + label]
        se_lm = cm["log_l_se_" + label]
        se_y0 = c0["mean_Y_twisted_se_" + label]
        se_ym = cm["mean_Y_twisted_se_" + label]
        var_log_R = se_r0 ** 2 + (P0 * se_l0) ** 2 + (Pm * se_lm) ** 2 + (d_pi * se_pi) ** 2
        var_P = (P0 * Pm) ** 2 * (se_l0 ** 2 + se_lm ** 2) + (dP_dpi * se_pi) ** 2
        var_Y = (P0 * se_y0) ** 2 + (Pm * se_ym) ** 2 + (Ym - Y0) ** 2 * var_P
        out[f"log_R_se_{label}"] = math.sqrt(var_log_R)
        out[f"P_minus_se_{label}"] = math.sqrt(var_P)
        out[f"mean_Y_se_{label}"] = math.sqrt(var_Y)
    return out


def analyze_mode(groups, size, mode):
    """groups: {kind: [runs]}; the class-sum kinds are complete, the U group may be absent."""
    seam = size * size
    u = analyze_unconstrained(groups[KIND_MAIN], size, mode) if groups.get(KIND_MAIN) else None
    p = analyze_pi1(groups[KIND_PI1], size, mode)
    c0 = analyze_restricted(groups[KIND_CLASS0], size, mode, KIND_CLASS0)
    cm = analyze_restricted(groups[KIND_CLASSM], size, mode, KIND_CLASSM)
    consistency_failures = []
    failures = []
    for route in (u, c0, cm):
        if route is not None:
            consistency_failures += route.get("consistency_failures", [])
    failures += p["calibration_failures"]
    for route in (p, c0, cm):
        failures += route["diagnostic_failures"]
    combined = None
    cross_check = {"pass": None, "reason": "U group absent"} if u is None else None
    if c0["log_l"] is not None and cm["log_l"] is not None:
        combined = class_sum(p, c0, cm)
        own_status = "FAIL_CONSISTENCY" if consistency_failures else "INCONCLUSIVE_EQUILIBRATION" if failures else GATES_PASSED
        if u is not None and u["status"] == GATES_PASSED and own_status != GATES_PASSED:
            cross_check = {"pass": None, "reason": f"class-sum route {own_status} before G11"}
        elif u is not None and u["status"] == GATES_PASSED:
            checks = {}
            for label, own, own_se, other, other_se in (
                    ("log_R", u["log_R"], u["log_R_se_batch"], combined["log_R"], combined["log_R_se_batch"]),
                    ("log_r0", u["log_r0"], u["log_r0_se_batch"], p["log_r0"], p["log_r0_se_batch"]),
                    ("pi1_minus", u["pi1_minus_chains_0_1_up"], u["pi1_minus_chains_0_1_up_se"],
                     p["pi1_minus"], p["pi1_minus_se_batch"])):
                tolerance = MULTIPLIER * math.hypot(own_se, other_se)
                checks[label] = {"U": own, "class_sum_route": other, "difference": own - other,
                                 "tolerance": tolerance, "pass": abs(own - other) <= tolerance}
            cross_check = {"pass": all(c["pass"] for c in checks.values()), "checks": checks}
            for label, check in checks.items():
                if not check["pass"]:
                    consistency_failures.append(f"G11:U_route_disagrees_with_class_sum_{label}")
        elif u is not None:
            cross_check = {"pass": None, "reason": f"U route {u['status']}"}
    if consistency_failures:
        status = "FAIL_CONSISTENCY"
    elif failures or combined is None:
        status = "INCONCLUSIVE_EQUILIBRATION"
    else:
        status = GATES_PASSED
    passes = status == GATES_PASSED
    result = {
        "k": mode, "status": status,
        "estimate_label": "EMPIRICAL_ENGINEERING_ONLY" if passes else "NONINFERENTIAL_ESTIMATE",
        "class_sum": combined, "cross_check_G11": cross_check,
        "diagnostic_failures": failures, "consistency_failures": consistency_failures,
        "U": u if u is not None else {"route": "U", "status": "INCOMPLETE"},
        "P": p, "class0": c0, "classMinus": cm,
    }
    if combined is not None:
        log_R_halfwidth = MULTIPLIER * combined["log_R_se_report"]
        Y_halfwidth = MULTIPLIER * combined["mean_Y_se_report"]
        log_R_interval = [combined["log_R"] - log_R_halfwidth, combined["log_R"] + log_R_halfwidth]
        R_interval = [math.exp(v) for v in log_R_interval]
        batch_halfwidth = MULTIPLIER * combined["log_R_se_batch"]
        Y_interval = [combined["mean_Y"] - Y_halfwidth, combined["mean_Y"] + Y_halfwidth]
        corners = [a * b for a in R_interval for b in Y_interval]
        result.update({
            "log_R": combined["log_R"], "log_R_se_batch": combined["log_R_se_batch"],
            "log_R_se_report": combined["log_R_se_report"],
            "log_R_interval": log_R_interval if passes else None,
            "log_R_interval_noninferential": log_R_interval,
            "log10_R_interval_noninferential": [v / math.log(10.0) for v in log_R_interval],
            "R_interval_noninferential": R_interval,
            "R_interval_batch_se": [math.exp(combined["log_R"] - batch_halfwidth),
                                    math.exp(combined["log_R"] + batch_halfwidth)],
            "log_R_resolved": passes and log_R_halfwidth <= THRESHOLDS["maximum_log_R_report_halfwidth"],
            "contrast_negligible": R_interval[1] < THRESHOLDS["negligible_contrast_R_upper"],
            "minus_log_R_per_seam_plaquette": -combined["log_R"] / seam,
            "P_minus": combined["P_minus"], "P_minus_se_report": combined["P_minus_se_report"],
            "mean_Y_twisted": combined["mean_Y"], "mean_Y_twisted_se_batch": combined["mean_Y_se_batch"],
            "mean_Y_twisted_se_report": combined["mean_Y_se_report"],
            "mean_Y_twisted_interval": Y_interval if passes else None,
            "mean_Y_twisted_interval_noninferential": Y_interval,
            "mean_Y_width_pass": passes and Y_halfwidth <= THRESHOLDS["maximum_mean_Y_report_halfwidth"],
            "mean_Y_interval_excludes_zero": Y_interval[0] > 0 or Y_interval[1] < 0,
            "signed_contrast_box_noninferential": [min(corners), max(corners)],
        })
    else:
        result.update({"log_R": None, "log_R_interval": None, "mean_Y_twisted": None,
                       "mean_Y_twisted_interval": None, "R_interval_batch_se": None,
                       "log_R_resolved": False, "mean_Y_width_pass": False,
                       "mean_Y_interval_excludes_zero": False, "contrast_negligible": False})
    return result


# ---------------------------------------------------------------------------
# Exact control groups with sector qualification


def analyze_control(runs, size, mode):
    """Exact control group: whole-seam source 2k, pass to 3k = -2k. Sector qualification
    of both endpoint dwells precedes the identity gates."""
    seam = size * size
    rows = [r for run in runs for r in run["rows"]]
    chains = sorted(run["key"][3] for run in runs)
    sector_failures = []
    endpoints = {}
    for label, n in (("source_2k", 0), ("source_3k", seam)):
        endpoint_rows = [r for r in rows if r["n"] == n]
        summaries = {field: mean_summary(endpoint_rows, field, "chain") for field in ("allMinus", "allPlus", "sumY")}
        for field, tag in (("allMinus", "all_slice_wMinus_disagreement"), ("allPlus", "all_slice_wPlus_disagreement"),
                           ("sumY", "mean_Y_disagreement")):
            leave_one_out(endpoint_rows, field, chains, summaries[field], f"control_{label}_chain_", sector_failures, tag)
        endpoints[label] = {
            "mean_Y": summaries["sumY"]["mean"], "mean_Y_se": summaries["sumY"]["se"],
            "mean_Y_by_chain": chain_values(endpoint_rows, "sumY", chains),
            "all_slice_wMinus_fraction_by_chain": {c: v / seam for c, v in chain_values(endpoint_rows, "allMinus", chains).items()},
            "all_slice_wPlus_fraction_by_chain": {c: v / seam for c, v in chain_values(endpoint_rows, "allPlus", chains).items()},
            "sector": sector_summary(endpoint_rows, seam),
        }
    ladder = Ladder(rows, seam, mode, 0)
    require(not ladder.degenerate, "control ladder has a zero estimator mean")
    log_R, log_R_se = ladder.partial(0, seam)
    log_R_by_chain = {c: ladder.subset(lambda r, c=c: r["chain"] == c, "chain")[0] for c in chains}
    failures = []
    consistency = ladder.consistency(False)
    consistency_failures = [f"control:naive_conditional_{name}_disagreement" for name in ("F", "Bw")
                            if abs(consistency[name]["statistic"]) > MULTIPLIER * consistency[name]["se"]]
    if abs(log_R) > MULTIPLIER * se_max(log_R_se):
        failures.append("control:total_log_ratio_nonzero")
    # Row-boundary symmetry C_m = C_{L-m}: the middle block of steps sums to zero.
    symmetry = []
    for m in range(1, size // 2):
        middle, middle_se = ladder.partial(m * size, (size - m) * size)
        ok = abs(middle) <= MULTIPLIER * se_max(middle_se)
        symmetry.append({"m": m, "middle_sum_log_r": middle, "se": se_max(middle_se), "pass": ok})
        if not ok:
            failures.append(f"control:row_symmetry_m{m}")
    y_start, y_end = endpoints["source_2k"], endpoints["source_3k"]
    if abs(y_start["mean_Y"] + y_end["mean_Y"]) > MULTIPLIER * math.hypot(y_start["mean_Y_se"], y_end["mean_Y_se"]):
        failures.append("control:mean_Y_reversal_antisymmetry")
    deficit, deficit_se = ladder.deficit()
    steps, log_R_bar = ladder.steps(True)
    if consistency_failures:
        status = "FAIL_CONSISTENCY"
    elif sector_failures:
        status = "CONTROL_SECTOR_FROZEN"
    elif failures:
        status = "FAIL_CONSISTENCY"
    else:
        status = "CONTROL_PASS"
    return {
        "k": mode, "status": status, "qualified": not sector_failures and not consistency_failures,
        "log_R": log_R, "log_R_se_batch": se_max(log_R_se), "log_R_bar": log_R_bar,
        "log_R_by_chain": log_R_by_chain,
        "row_symmetry": symmetry,
        "endpoints": endpoints,
        "mean_Y_source_2k": y_start["mean_Y"], "mean_Y_source_2k_se": y_start["mean_Y_se"],
        "mean_Y_source_3k": y_end["mean_Y"], "mean_Y_source_3k_se": y_end["mean_Y_se"],
        "forward_reverse_deficit": deficit, "forward_reverse_deficit_se": se_max(deficit_se),
        "naive_conditional_consistency": consistency,
        "control_failures": failures, "sector_failures": sector_failures,
        "consistency_failures": consistency_failures,
        "chains": [{"chain": run["key"][3], "initial": initial_name(KIND_CONTROL, run["key"][3]),
                    "input_file": run["file"], "input_sha256": run["sha256"]} for run in runs],
        "steps": steps,
    }


def square_interval(interval):
    low, high = interval
    nearest = 0.0 if low <= 0 <= high else min(low * low, high * high)
    return nearest, max(low * low, high * high)


def residue_law(R1, R2):
    return {"p0": (1 + 2 * R1 + 2 * R2) / 5, "p1": (1 + R1 / PHI - PHI * R2) / 5, "p2": (1 - PHI * R1 + R2 / PHI) / 5}


def cross_mode(modes):
    """Exact positivity of the seam-residue law from the two class-sum ratios, at interval corners."""
    by_k = {item["k"]: item for item in modes}
    if any(by_k[k].get("R_interval_batch_se") is None for k in MODES):
        return {"applicable": False, "reason": "a class-sum ratio is absent"}
    R1 = by_k[1]["R_interval_batch_se"]
    R2 = by_k[2]["R_interval_batch_se"]
    corners = [residue_law(a, b) for a in R1 for b in R2]
    law_interval = {name: [min(c[name] for c in corners), max(c[name] for c in corners)] for name in ("p0", "p1", "p2")}
    # Most favourable corner: R1 low against R2 high, and vice versa.
    inequality_1 = R1[0] <= 1 / PHI + R2[1] / PHI ** 2
    inequality_2 = R2[0] <= 1 / PHI + R1[1] / PHI ** 2
    return {"residue_law_interval_noninferential": law_interval,
            "R1_le_0.618_plus_0.382_R2": inequality_1, "R2_le_0.618_plus_0.382_R1": inequality_2,
            "applicable": all(item["status"] == GATES_PASSED for item in modes)}


def taint(item, tag):
    item["consistency_failures"].append(tag)
    item["status"] = "FAIL_CONSISTENCY"
    item["estimate_label"] = "NONINFERENTIAL_ESTIMATE"
    item["log_R_interval"] = None
    item["mean_Y_twisted_interval"] = None


def report(runs):
    result = {
        "analysis": "C-PHOTON-TWIST-SNAKE-SECTOR-N",
        "status": "INCOMPLETE", "status_precedence": STATUS_ORDER, "thresholds": THRESHOLDS,
        "scope": "NON-CANONICAL engineering diagnostics of finite-volume twisted ratios and signed contrasts",
        "coverage": "4SE intervals are empirical; no rigorous or simultaneous coverage is claimed",
        "limitations": [
            "Passing the gates does not prove equilibration, stationarity or decorrelation.",
            "No thermodynamic, phase, scaling, or P1 verdict is produced.",
            "Squared ranges are formed from signed boxes, not squared noisy point estimates.",
            "All estimates remain visible even when inference is withheld.",
            "Values at different L are reported separately; no comparison across L is made.",
            "Class-conditional values are descriptive; the class weights are finite-volume quantities.",
        ],
        "missing_runs": [], "volumes": [], "controls": [],
    }
    indexed = {}
    for run in runs:
        require(run["key"] not in indexed, f"duplicate run {run['key']}")
        indexed[run["key"]] = run
    result["missing_runs"] = [list(key) for key in declared_jobs() if key not in indexed]
    result["available_run_count"] = len(runs)
    # Exact control groups first, with sector qualification.
    # A control group carries the sources 2k and 3k, which are unrelated to the sector
    # structure of mode k itself; the groups test the implementation. Any qualified group
    # that fails taints every main group; if no group is qualified every main group is capped.
    control_failed = False
    control_qualified = False
    control_incomplete = set()
    for size in CONTROL_L_VALUES:
        for mode in MODES:
            keys = [(size, mode, KIND_CONTROL, chain) for chain in KIND_CHAINS[KIND_CONTROL]]
            if all(key in indexed for key in keys):
                control = analyze_control([indexed[key] for key in keys], size, mode)
                control_failed = control_failed or control["status"] == "FAIL_CONSISTENCY"
                control_qualified = control_qualified or control["qualified"]
            else:
                control = {"k": mode, "status": "INCOMPLETE", "qualified": False,
                           "available_chains": [indexed[key]["file"] for key in keys if key in indexed]}
                control_incomplete.add(size)
            control["L"] = size
            result["controls"].append(control)
    for size in L_VALUES:
        modes = []
        for mode in MODES:
            groups = {kind: [indexed[(size, mode, kind, chain)] for chain in KIND_CHAINS[kind]
                             if (size, mode, kind, chain) in indexed]
                      for kind in (KIND_MAIN, KIND_PI1, KIND_CLASS0, KIND_CLASSM)}
            complete = all(len(groups[kind]) == len(KIND_CHAINS[kind]) for kind in CLASS_SUM_KINDS)
            if len(groups[KIND_MAIN]) != len(KIND_CHAINS[KIND_MAIN]):
                groups[KIND_MAIN] = []  # the U route is read only when all five chains are present
            if complete:
                item = analyze_mode(groups, size, mode)
                if control_failed:
                    taint(item, "control:qualified_control_group_failed")
                elif not control_qualified:
                    item["diagnostic_failures"].append("control:no_qualified_control_group")
                    if item["status"] == GATES_PASSED:
                        item["status"] = "INCONCLUSIVE_EQUILIBRATION"
                        item["estimate_label"] = "NONINFERENTIAL_ESTIMATE"
                        item["log_R_interval"] = None
                        item["mean_Y_twisted_interval"] = None
                modes.append(item)
            else:
                modes.append({
                    "k": mode, "status": "INCOMPLETE", "estimate_label": "NONINFERENTIAL_ESTIMATE",
                    "consistency_failures": [], "diagnostic_failures": [],
                    "available_chains": [
                        {"kind": KIND_NAMES[run["key"][2]], "chain": run["key"][3],
                         "input_file": run["file"], "input_sha256": run["sha256"]}
                        for kind in groups for run in groups[kind]
                    ],
                })
        volume = {"L": size, "modes": modes}
        positivity = cross_mode(modes) if all(item["status"] != "INCOMPLETE" for item in modes) else None
        volume["cross_mode_positivity"] = positivity
        if positivity and positivity["applicable"] and not (
                positivity["R1_le_0.618_plus_0.382_R2"] and positivity["R2_le_0.618_plus_0.382_R1"]):
            for item in modes:
                taint(item, "pooled:cross_mode_positivity_violated")
        mode_statuses = ["UNRESOLVED" if item["status"] == GATES_PASSED else item["status"] for item in modes]
        volume["D_empirical_engineering_interval"] = None
        volume["log10_D_empirical_engineering_interval"] = None
        if all(item["status"] == GATES_PASSED for item in modes):
            if all(item["log_R_resolved"] for item in modes):
                squared = [square_interval(item["signed_contrast_box_noninferential"]) for item in modes]
                low = math.fsum(pair[0] for pair in squared)
                high = math.fsum(pair[1] for pair in squared)
                volume["D_empirical_engineering_interval"] = [low, high]
                volume["log10_D_empirical_engineering_interval"] = [
                    math.log10(low) if low > 0 else None, math.log10(high) if high > 0 else None]
            if (all(item["log_R_resolved"] and item["mean_Y_width_pass"] for item in modes)
                    and any(item["mean_Y_interval_excludes_zero"] for item in modes)):
                volume["status"] = "RESOLVED_SIGNED_CONTRAST"
            else:
                volume["status"] = "UNRESOLVED"
        else:
            volume["status"] = worst(mode_statuses)
        # An exact control group that is INCOMPLETE leaves the same L without its guard.
        if size in control_incomplete:
            volume["status"] = worst([volume["status"], "INCOMPLETE"])
            volume["control_incomplete"] = True
        result["volumes"].append(volume)
    result["status"] = worst([item["status"] for item in result["volumes"]]
                             + ["INCOMPLETE" for c in result["controls"] if c["status"] == "INCOMPLETE"])
    return result


def read_execution(directory):
    """Validate process outcomes and custody before admitting scientific output."""
    manifest_path = directory / "execution.json"
    try:
        records = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeError) as exc:
        raise InvalidInput("malformed execution.json") from exc
    require(isinstance(records, list), "execution.json must contain a list")
    expected_stems = {stem_of(*key): key for key in declared_jobs()}
    seen = set()
    runs = []
    errors = []
    unavailable = []
    for record in records:
        if not isinstance(record, dict):
            errors.append("malformed execution record")
            continue
        stem = record.get("stem")
        if not isinstance(stem, str) or stem not in set(expected_stems) | {"audit"} or stem in seen:
            errors.append("unexpected or duplicate execution stem")
            continue
        seen.add(stem)
        usable = True
        try:
            code = record["exit_code"]
            require(type(code) is int, f"{stem}: invalid exit code")
            if stem != "audit" and code in UNAVAILABLE_EXIT_CODES:
                unavailable.append({"stem": stem, "exit_code": code})
                continue
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
                require(audit == EXPECTED_AUDIT, "audit: unexpected output")
        except (InvalidInput, OSError, UnicodeError, KeyError) as exc:
            usable = False
            errors.append(str(exc))
        if stem != "audit":
            try:
                run = read_run(directory / f"{stem}.tsv", expected_stems[stem])
                if usable:
                    runs.append(run)
            except (InvalidInput, OSError, UnicodeError) as exc:
                errors.append(str(exc))
    if "audit" not in seen:
        errors.append("missing audit execution record")
    try:
        environment = json.loads((directory / "environment.json").read_text(encoding="utf-8"))
        require(isinstance(environment, dict), "environment.json must contain an object")
        for field, value in EXPECTED_ENVIRONMENT.items():
            require(environment.get(field) == value, f"environment.json: incorrect {field}")
        digest = environment.get("binary_sha256")
        require(isinstance(digest, str) and len(digest) == 64 and all(c in "0123456789abcdef" for c in digest),
                "environment.json: missing binary_sha256")
    except (OSError, UnicodeError, json.JSONDecodeError, InvalidInput) as exc:
        errors.append(f"environment.json: {exc}")
    result = report(runs)
    result["execution_manifest_sha256"] = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
    result["execution_errors"] = errors
    result["unavailable_jobs"] = unavailable
    if errors:
        result["status"] = "FAIL_IMPLEMENTATION"
        for volume in result["volumes"]:
            volume["status"] = "FAIL_IMPLEMENTATION"
            volume["D_empirical_engineering_interval"] = None
            volume["log10_D_empirical_engineering_interval"] = None
            for mode in volume.get("modes", []):
                mode["status"] = "FAIL_IMPLEMENTATION"
                mode["estimate_label"] = "NONINFERENTIAL_ESTIMATE"
                for field in ("log_R_interval", "mean_Y_twisted_interval"):
                    if field in mode:
                        mode[field] = None
        for control in result["controls"]:
            control["status"] = "FAIL_IMPLEMENTATION"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_directory", type=Path, help="untouched run_snake.py output directory")
    args = parser.parse_args()
    try:
        result = read_execution(args.output_directory)
        text = json.dumps(result, indent=2, sort_keys=True, allow_nan=False)
    except (InvalidInput, OSError, ArithmeticError, ValueError, TypeError) as exc:
        result = {"status": "FAIL_IMPLEMENTATION", "reason": str(exc),
                  "scope": "malformed or inaccessible diagnostic input; no scientific inference"}
        text = json.dumps(result, indent=2, sort_keys=True, allow_nan=False)
    print(text)
    if result["status"] == "FAIL_IMPLEMENTATION":
        return 2
    if result["status"] == "INCOMPLETE":
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
