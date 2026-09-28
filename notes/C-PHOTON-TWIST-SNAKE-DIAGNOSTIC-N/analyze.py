#!/usr/bin/env python3
"""Frozen engineering analysis, NON-CANONICAL; no rigorous coverage claim.

Input: the untouched run_snake.py output directory and its execution manifest.
Output: JSON retaining all estimates, including failed diagnostics.
No phase, scaling, thermodynamic, or P1 verdict is implemented here.

Closed status set and strict precedence, fixed before execution:
  per (L,k):  FAIL_IMPLEMENTATION > INCOMPLETE > FAIL_CONSISTENCY
              > INCONCLUSIVE_EQUILIBRATION > SECTOR_FROZEN > UNRESOLVED
              > RESOLVED_SIGNED_CONTRAST
  per L:      the worst mode label; RESOLVED_SIGNED_CONTRAST only when both modes
              pass every gate, both log R_k report half-widths are at most 1.0,
              both mean-Y report half-widths are at most 0.05 and at least one
              mean-Y interval excludes zero; otherwise UNRESOLVED.
  overall:    the worst volume label.
A job that timed out (exit 124) or failed to launch (exit 127) makes its group
INCOMPLETE and nothing else. Any other nonzero exit, nonempty stderr, byte or
hash mismatch, malformed record, histogram or sector inconsistency, audit or
environment mismatch is a custody or implementation failure: every group is
labelled FAIL_IMPLEMENTATION and every estimate is NONINFERENTIAL_ESTIMATE,
although all estimates stay visible. A failed exact control group (base 2)
labels every main group FAIL_CONSISTENCY.

Error model (engineering, no coverage claim). Estimates are regrouped by
ensemble m: log R = sum_m c_m with
  c_m = w_m log F_m [m<S] - (1 - w_{m-1}) log B_m [m>0],
F_m the pooled mean of the conditional forward estimator at m, B_m the pooled
mean of the conditional reverse estimator at m (for step m-1), and the
inverse-variance weight w_n = rv_B(n+1) / (rv_F(n) + rv_B(n+1)) from relative
batch variances at the finest scale. Logs of pooled means are bias-corrected to
first order, log F + rv_F / 2. Batch standard errors use the per-batch influence
  u_b = w_m f_b / F_m [m<S] - (1 - w_{m-1}) g_b / B_m [m>0],
computed at block scales 512, 1024, 2048 (coarsening inside one segment only),
SE^2 = sum_m Var_b(u_b) / B_m, and the maximum over scales of the aggregate.
Subset gates use the pooled within-group batch variance at each m, the groups
being the chains (G3, G9), the pass directions (G4) or the dwell halves (G5),
so that the deviation a gate tests never enters its own tolerance.
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
MAIN_BASE = 0
CONTROL_BASE = 2
MAIN_CHAINS = (0, 1, 2, 3, 4)
CONTROL_CHAINS = (0, 1, 2, 3)
INITIAL = {0: "cold0", 1: "hot0", 2: "coldT", 3: "hotT", 4: "coldAltT"}
WARMUP_SWEEPS = 512
DWELL_SWEEPS = 16384
VISIT_SWEEPS = 2048
EQUILIBRATION_SWEEPS = 32
BLOCK_LENGTH = 512
DWELL_BLOCKS = DWELL_SWEEPS // BLOCK_LENGTH
VISIT_BLOCKS = VISIT_SWEEPS // BLOCK_LENGTH
COARSENING = (1, 2, 4)
SCALES = tuple(str(BLOCK_LENGTH * f) for f in COARSENING)
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
    "pure_pass_minimum_fraction": 0.95,
}
PHI = (1.0 + math.sqrt(5.0)) / 2.0
WEIGHT = {0: 4.0, 1: PHI ** 2, 2: PHI ** -2, 3: PHI ** -2, 4: PHI ** 2}
RATIO = {k: [WEIGHT[(f + k) % 5] / WEIGHT[f] for f in range(5)] for k in MODES}
RATIO_BOUNDS = {k: (min(RATIO[k]), max(RATIO[k])) for k in MODES}
EXPECTED_AUDIT = (
    "NON-CANONICAL floating-point engineering audit\n"
    "geometries\t4\nfixture_states\t64\nestimator_identities\t384\n"
    "local_enumerations\t96\ninvariance_checks\t384\ninversion_checks\t42\n"
    "exercise_sweeps\t160\nschedule_rows\t320\nmutations_caught\t192\nresult\tPASS\n"
)
EXPECTED_ENVIRONMENT = {"workers": 4, "audit_timeout_seconds": 600, "per_chain_timeout_seconds": 2400}
HIST_F = tuple(f"hF{f}" for f in range(5))
HIST_B = tuple(f"hB{f}" for f in range(5))
SECTOR_FIELDS = ("sec0", "secMinus", "secPlus", "secOther", "secUntwisted",
                 "pure0", "pureMinus", "purePlus", "flips")
INTEGER_FIELDS = ({"L", "k", "chain", "segment", "n", "block", "count"}
                  | set(HIST_F) | set(HIST_B) | set(SECTOR_FIELDS))
STRING_FIELDS = {"phase"}
FLOAT_FIELDS = {
    "sumFn", "sumFn2", "sumFi", "sumFi2", "sumBn", "sumBn2", "sumBi", "sumBi2",
    "sumY", "sumY2", "sumS", "sumS2",
}
FIELDS = INTEGER_FIELDS | STRING_FIELDS | FLOAT_FIELDS
PHASES = {"dwell", "up", "down"}
UNAVAILABLE_EXIT_CODES = {124, 127}
STATUS_ORDER = ["FAIL_IMPLEMENTATION", "INCOMPLETE", "FAIL_CONSISTENCY",
                "INCONCLUSIVE_EQUILIBRATION", "SECTOR_FROZEN", "UNRESOLVED",
                "RESOLVED_SIGNED_CONTRAST"]
GATES_PASSED = "GATES_PASSED"  # per-mode gate outcome; volumes carry the closed labels


class InvalidInput(Exception):
    pass


def require(condition, message):
    if not condition:
        raise InvalidInput(message)


def worst(statuses):
    return min(statuses, key=STATUS_ORDER.index)


def stem_of(size, mode, base, chain):
    return f"L{size}_k{mode}_c{chain}" if base == MAIN_BASE else f"L{size}_k{mode}_b{base}_c{chain}"


def declared_jobs():
    jobs = [(size, mode, MAIN_BASE, chain) for size in L_VALUES for mode in MODES for chain in MAIN_CHAINS]
    jobs += [(size, mode, CONTROL_BASE, chain) for size in CONTROL_L_VALUES for mode in MODES
             for chain in CONTROL_CHAINS]
    return jobs


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


def start_twist(size, chain):
    return 0 if chain < 2 else size * size


def expected_segments(size, chain):
    """The frozen visiting order: dwell, pass, dwell, pass back."""
    seam = size * size
    n = start_twist(size, chain)
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


def close(left, right, tolerance):
    return abs(left - right) <= tolerance * (1.0 + abs(left) + abs(right))


def read_run(path, expected_key):
    size, mode, base, chain = expected_key
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
            row[field] = nonnegative_integer(source[field], f"{path.name}:{field}")
        for field in FLOAT_FIELDS:
            row[field] = finite_number(source[field], f"{path.name}:{field}")
        row["phase"] = source["phase"]
        require(row["phase"] in PHASES, f"{path.name}: unexpected phase")
        require((row["L"], row["k"], row["chain"]) == (size, mode, chain), f"{path.name}: unexpected run key")
        require(row["count"] == BLOCK_LENGTH, f"{path.name}: unexpected block length")
        for first, second in (("sumFn", "sumFn2"), ("sumFi", "sumFi2"), ("sumBn", "sumBn2"),
                              ("sumBi", "sumBi2"), ("sumY", "sumY2"), ("sumS", "sumS2")):
            require(row[second] >= 0, f"{path.name}: negative second moment")
            tolerance = 1e-8 * max(1.0, row[first] ** 2, row["count"] * row[second])
            require(row[first] ** 2 <= row["count"] * row[second] + tolerance,
                    f"{path.name}: inconsistent first and second moments")
        rows.append(row)
    seam = size * size
    sequence = expected_segments(size, chain)
    expected_rows = sum(blocks for _, _, blocks in sequence)
    require(len(rows) == expected_rows, f"{path.name}: expected {expected_rows} block rows")
    ratio = RATIO[mode]
    low, high = RATIO_BOUNDS[mode]
    index = 0
    for segment, (n, phase, blocks) in enumerate(sequence):
        for block in range(blocks):
            row = rows[index]
            index += 1
            require(row["segment"] == segment and row["n"] == n and row["phase"] == phase
                    and row["block"] == block, f"{path.name}: block sequence differs from frozen order")
            count = row["count"]
            hist_f = [row[h] for h in HIST_F]
            hist_b = [row[h] for h in HIST_B]
            if n < seam:
                require(sum(hist_f) == count, f"{path.name}: forward histogram count")
                naive = math.fsum(hist_f[f] * ratio[f] for f in range(5))
                naive2 = math.fsum(hist_f[f] * ratio[f] ** 2 for f in range(5))
                require(close(row["sumFn"], naive, 1e-9) and close(row["sumFn2"], naive2, 1e-9),
                        f"{path.name}: naive forward sums disagree with the flux histogram")
                require(low * count * (1 - 1e-9) <= row["sumFi"] <= high * count * (1 + 1e-9),
                        f"{path.name}: conditional forward estimator outside its exact bounds")
            else:
                require(sum(hist_f) == 0 and all(row[f] == 0 for f in ("sumFn", "sumFn2", "sumFi", "sumFi2")),
                        f"{path.name}: forward estimator recorded at the twisted endpoint")
            if n > 0:
                require(sum(hist_b) == count, f"{path.name}: reverse histogram count")
                naive = math.fsum(hist_b[f] / ratio[(f - mode) % 5] for f in range(5))
                naive2 = math.fsum(hist_b[f] / ratio[(f - mode) % 5] ** 2 for f in range(5))
                require(close(row["sumBn"], naive, 1e-9) and close(row["sumBn2"], naive2, 1e-9),
                        f"{path.name}: naive reverse sums disagree with the flux histogram")
                require(low * count * (1 - 1e-9) <= row["sumBi"] <= high * count * (1 + 1e-9),
                        f"{path.name}: conditional reverse estimator outside its exact bounds")
            else:
                require(sum(hist_b) == 0 and all(row[f] == 0 for f in ("sumBn", "sumBn2", "sumBi", "sumBi2")),
                        f"{path.name}: reverse estimator recorded at the untwisted endpoint")
            twisted = row["sec0"] + row["secMinus"] + row["secPlus"] + row["secOther"]
            require(twisted == count * n, f"{path.name}: twisted slice sector counts")
            require(row["secUntwisted"] <= count * (seam - n), f"{path.name}: untwisted sector counts")
            pure = row["pure0"] + row["pureMinus"] + row["purePlus"]
            require(pure <= count and row["flips"] <= count, f"{path.name}: pure or flip counts")
            if n == 0:
                require(pure == 0, f"{path.name}: pure layout recorded without twisted slices")
    required_metadata = {
        "format": "twist_snake_blocks_v1", "L": str(size), "k": str(mode), "chain": str(chain),
        "base": str(base),
        "seed": str(202609280000 + 1000 * size + 100 * mode + 10 * base + chain),
        "seam_size": str(seam), "start_twist": str(start_twist(size, chain)),
        "chain_initial": INITIAL[chain],
        "warmup_sweeps": str(WARMUP_SWEEPS), "dwell_sweeps": str(DWELL_SWEEPS),
        "visit_sweeps": str(VISIT_SWEEPS), "equilibration_sweeps": str(EQUILIBRATION_SWEEPS),
        "block_length": str(BLOCK_LENGTH), "segments": str(2 * seam),
        "seam_order": "x2_fastest_then_x3",
        "sampling": "every_production_sweep_after_full_heatbath_sweep",
        "final_twist": str(1 if start_twist(size, chain) == 0 else seam - 1),
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
    average exactly to the pooled mean.
    """
    result = []
    by_segment = {}
    for row in rows:
        by_segment.setdefault((row["chain"], row["segment"]), []).append(row)
    for (chain, _), group in sorted(by_segment.items()):
        group = sorted(group, key=lambda item: item["block"])
        require(len(group) % factor == 0, "incomplete coarsening group")
        for start in range(0, len(group), factor):
            chunk = group[start:start + factor]
            count = sum(r["count"] for r in chunk)
            batch = {"chain": chain, "phase": chunk[0]["phase"], "count": count,
                     "half": 0 if chunk[0]["block"] < DWELL_BLOCKS // 2 else 1}
            for field in FLOAT_FIELDS:
                batch[field] = math.fsum(r[field] for r in chunk) / count
            for field in ("pure0", "pureMinus", "purePlus"):
                batch[field] = sum(r[field] for r in chunk) / count
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


class Ensemble:
    """All batches at one twist count m, at every scale."""

    def __init__(self, rows, m, seam):
        self.m = m
        self.rows = [r for r in rows if r["n"] == m]
        require(self.rows, f"ensemble {m}: absent samples")
        self.has_forward = m < seam
        self.has_reverse = m > 0
        self.batches = {scale: batches(self.rows, factor) for scale, factor in zip(SCALES, COARSENING)}
        count = sum(r["count"] for r in self.rows)
        self.samples = count
        self.F = math.fsum(r["sumFi"] for r in self.rows) / count if self.has_forward else None
        self.B = math.fsum(r["sumBi"] for r in self.rows) / count if self.has_reverse else None
        self.Fn = math.fsum(r["sumFn"] for r in self.rows) / count if self.has_forward else None
        self.Bn = math.fsum(r["sumBn"] for r in self.rows) / count if self.has_reverse else None
        require(self.F is None or self.F > 0, f"ensemble {m}: nonpositive forward mean")
        require(self.B is None or self.B > 0, f"ensemble {m}: nonpositive reverse mean")
        fine = self.batches[SCALES[0]]
        self.rvF = variance([b["sumFi"] for b in fine]) / (len(fine) * self.F ** 2) if self.has_forward else None
        self.rvB = variance([b["sumBi"] for b in fine]) / (len(fine) * self.B ** 2) if self.has_reverse else None

    def log_forward(self):
        """First-order bias-corrected log of the pooled forward mean."""
        return math.log(self.F) + 0.5 * self.rvF

    def log_reverse(self):
        return math.log(self.B) + 0.5 * self.rvB


def weights(ensembles, seam):
    """Inverse-variance weight of the forward estimator for every step n."""
    w = {}
    for n in range(seam):
        rvF = ensembles[n].rvF
        rvB = ensembles[n + 1].rvB
        w[n] = rvB / (rvF + rvB) if rvF + rvB > 0 else 0.5
    return w


def uses_forward(m, lo, hi):
    return lo <= m < hi


def uses_reverse(m, lo, hi):
    return lo < m <= hi


def influence(ensemble, batch, w, lo, hi):
    """Per-batch linearised contribution u_b to the log ratio over steps [lo, hi)."""
    m = ensemble.m
    value = 0.0
    if uses_forward(m, lo, hi):
        value += w[m] * batch["sumFi"] / ensemble.F
    if uses_reverse(m, lo, hi):
        value -= (1.0 - w[m - 1]) * batch["sumBi"] / ensemble.B
    return value


def deficit_influence(ensemble, batch, lo, hi):
    """Per-batch contribution v_b to the unit-weight forward-reverse deficit."""
    m = ensemble.m
    value = 0.0
    if uses_forward(m, lo, hi):
        value += batch["sumFi"] / ensemble.F
    if uses_reverse(m, lo, hi):
        value += batch["sumBi"] / ensemble.B
    return value


def contribution(ensemble, w, lo, hi, log_forward=None, log_reverse=None):
    """c_m for the pooled ensemble, or for supplied subset logs, over steps [lo, hi)."""
    m = ensemble.m
    value = 0.0
    if uses_forward(m, lo, hi):
        value += w[m] * (ensemble.log_forward() if log_forward is None else log_forward)
    if uses_reverse(m, lo, hi):
        value -= (1.0 - w[m - 1]) * (ensemble.log_reverse() if log_reverse is None else log_reverse)
    return value


def subset_logs(ensemble, predicate):
    """Bias-corrected logs of the means over a subset of rows (finest scale for the correction)."""
    rows = [r for r in ensemble.rows if predicate(r)]
    if not rows:
        return None, None, 0
    count = sum(r["count"] for r in rows)
    fine = batches(rows, 1)
    log_f = log_b = None
    if ensemble.has_forward:
        F = math.fsum(r["sumFi"] for r in rows) / count
        require(F > 0, "nonpositive subset forward mean")
        rv = variance([b["sumFi"] for b in fine]) / (len(fine) * F ** 2) if len(fine) >= 2 else 0.0
        log_f = math.log(F) + 0.5 * rv
    if ensemble.has_reverse:
        B = math.fsum(r["sumBi"] for r in rows) / count
        require(B > 0, "nonpositive subset reverse mean")
        rv = variance([b["sumBi"] for b in fine]) / (len(fine) * B ** 2) if len(fine) >= 2 else 0.0
        log_b = math.log(B) + 0.5 * rv
    return log_f, log_b, count


def bar_log_ratio(forward_hist, reverse_hist, mode):
    """Bennett acceptance ratio from exact integer flux histograms (secondary value).

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
    def __init__(self, rows, seam, mode):
        self.seam = seam
        self.mode = mode
        self.ensembles = [Ensemble(rows, m, seam) for m in range(seam + 1)]
        self.w = weights(self.ensembles, seam)
        self._pooled = {}

    def pooled_variance(self, group):
        """Within-group pooled variance of the full-range influence at every m and scale."""
        if group not in self._pooled:
            table = {}
            for scale in SCALES:
                table[scale] = {}
                for e in self.ensembles:
                    u = [influence(e, b, self.w, 0, self.seam) for b in e.batches[scale]]
                    table[scale][e.m] = within_variance(grouped(e.batches[scale], u, group))
            self._pooled[group] = table
        return self._pooled[group]

    def partial(self, lo, hi):
        """Pooled log ratio over steps [lo, hi) with aggregate batch SE by scale."""
        total = math.fsum(contribution(e, self.w, lo, hi) for e in self.ensembles)
        se_by_scale = {}
        for scale in SCALES:
            var_total = 0.0
            for e in self.ensembles:
                if not (uses_forward(e.m, lo, hi) or uses_reverse(e.m, lo, hi)):
                    continue
                u = [influence(e, b, self.w, lo, hi) for b in e.batches[scale]]
                var_total += variance(u) / len(u)
            se_by_scale[scale] = math.sqrt(var_total)
        return total, se_by_scale

    def deficit(self):
        total = 0.0
        for e in self.ensembles:
            if e.has_forward:
                total += e.log_forward()
            if e.has_reverse:
                total += e.log_reverse()
        se_by_scale = {}
        for scale in SCALES:
            var_total = 0.0
            for e in self.ensembles:
                v = [deficit_influence(e, b, 0, self.seam) for b in e.batches[scale]]
                var_total += variance(v) / len(v)
            se_by_scale[scale] = math.sqrt(var_total)
        return total, se_by_scale

    def subset(self, predicate, group, ensembles=None):
        """log ratio over the full step range from a subset of rows, restricted to the
        listed ensembles (all by default); SE from the within-`group` pooled variance."""
        pooled = self.pooled_variance(group)
        chosen = set(range(self.seam + 1)) if ensembles is None else set(ensembles)
        total = 0.0
        se_by_scale = {scale: 0.0 for scale in SCALES}
        for e in self.ensembles:
            if e.m not in chosen:
                continue
            log_f, log_b, count = subset_logs(e, predicate)
            require(count > 0, f"ensemble {e.m}: subset has no samples")
            total += contribution(e, self.w, 0, self.seam, log_f, log_b)
            for scale, factor in zip(SCALES, COARSENING):
                n_batches = count // (BLOCK_LENGTH * factor)
                require(n_batches >= 1, "subset too small for this scale")
                se_by_scale[scale] += pooled[scale][e.m] / n_batches
        return total, {scale: math.sqrt(v) for scale, v in se_by_scale.items()}

    def consistency(self):
        """Naive versus conditional estimators, paired by block (linear form, exactly zero-mean)."""
        result = {}
        for side, field_naive, field_imp, attribute in (
            ("forward", "sumFn", "sumFi", "has_forward"), ("reverse", "sumBn", "sumBi", "has_reverse")):
            statistic = 0.0
            se_scale = {}
            for scale in SCALES:
                total = 0.0
                for e in self.ensembles:
                    if not getattr(e, attribute):
                        continue
                    improved = e.F if side == "forward" else e.B
                    diffs = [b[field_naive] - b[field_imp] for b in e.batches[scale]]
                    total += variance(diffs) / (len(diffs) * improved ** 2)
                    if scale == SCALES[0]:
                        statistic += mean(diffs) / improved
                se_scale[scale] = math.sqrt(total)
            result[side] = {"statistic": statistic, "se": se_max(se_scale), "se_by_block_length": se_scale}
        return result

    def steps(self):
        table = []
        bar_total = 0.0
        equal_total = 0.0
        for n in range(self.seam):
            e, f = self.ensembles[n], self.ensembles[n + 1]
            hist_f = [sum(r[h] for r in e.rows) for h in HIST_F]
            hist_b = [sum(r[h] for r in f.rows) for h in HIST_B]
            bar = bar_log_ratio(hist_f, hist_b, self.mode)
            bar_total += bar
            equal = 0.5 * (e.log_forward() - f.log_reverse())
            equal_total += equal
            table.append({
                "n": n, "weight_forward": self.w[n],
                "log_r": self.w[n] * e.log_forward() - (1.0 - self.w[n]) * f.log_reverse(),
                "log_r_equal_weight": equal, "log_r_bar": bar,
                "forward_conditional": e.F, "forward_naive": e.Fn,
                "reverse_conditional": f.B, "reverse_naive": f.Bn,
                "forward_samples": e.samples, "reverse_samples": f.samples,
                "forward_flux_histogram": hist_f, "reverse_flux_histogram": hist_b,
            })
        return table, bar_total, equal_total


def mean_summary(rows, field, group=None):
    """Pooled mean of a block field with batch SE at every scale; optionally the
    within-`group` pooled variance for subset comparisons."""
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
    return abs(first - second) <= MULTIPLIER * math.hypot(first_se, second_se)


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
    twisted_slices = sum(r["count"] * r["n"] for r in rows)
    result = {"pure0_fraction": fraction(rows, "pure0"), "pureMinus_fraction": fraction(rows, "pureMinus"),
              "purePlus_fraction": fraction(rows, "purePlus"), "flips": sum(r["flips"] for r in rows),
              "untwisted_nonzero_slice_fraction": None, "twisted_slice_fractions": None}
    untwisted_slices = sum(r["count"] * (seam - r["n"]) for r in rows)
    if untwisted_slices:
        result["untwisted_nonzero_slice_fraction"] = sum(r["secUntwisted"] for r in rows) / untwisted_slices
    if twisted_slices:
        result["twisted_slice_fractions"] = {
            "w0": sum(r["sec0"] for r in rows) / twisted_slices,
            "wMinus": sum(r["secMinus"] for r in rows) / twisted_slices,
            "wPlus": sum(r["secPlus"] for r in rows) / twisted_slices,
            "other": sum(r["secOther"] for r in rows) / twisted_slices,
        }
    return result


def pure_down_pass(run, field, seam):
    """True when every down-pass and dwell segment of the chain is at least 95% pure in `field`
    (untwisted dwell: at least 95% of sweeps have no untwisted slice with w != 0)."""
    by_segment = {}
    for r in run["rows"]:
        if r["phase"] in ("down", "dwell"):
            by_segment.setdefault(r["segment"], []).append(r)
    minimum = THRESHOLDS["pure_pass_minimum_fraction"]
    for segment_rows in by_segment.values():
        if segment_rows[0]["n"] == 0:
            sweeps = sum(r["count"] for r in segment_rows)
            if sum(r["secUntwisted"] for r in segment_rows) > (1 - minimum) * sweeps:
                return False
            continue
        if fraction(segment_rows, field) < minimum:
            return False
    return True


def analyze_mode(runs, size, mode):
    seam = size * size
    rows = [r for run in runs for r in run["rows"]]
    chains = sorted(run["key"][3] for run in runs)
    failures = []
    consistency_failures = []
    sector_failures = []
    ladder = Ladder(rows, seam, mode)
    log_R, log_R_se_by_scale = ladder.partial(0, seam)
    deficit, deficit_se_by_scale = ladder.deficit()
    consistency = ladder.consistency()
    steps, log_R_bar, log_R_equal = ladder.steps()
    twisted_rows = [r for r in rows if r["n"] == seam]
    untwisted_rows = [r for r in rows if r["n"] == 0]
    # G8a uses only chains 0 and 1, whose initial laws are reversal symmetric.
    symmetric_untwisted_rows = [r for r in untwisted_rows if r["chain"] in (0, 1)]
    y_twisted = mean_summary(twisted_rows, "sumY", "chain")
    y_twisted_halves = mean_summary(twisted_rows, "sumY", "chain_half")
    y_untwisted = mean_summary(symmetric_untwisted_rows, "sumY")
    y_untwisted_all = mean_summary(untwisted_rows, "sumY")
    y2_untwisted = mean_summary(untwisted_rows, "sumY2")
    pure_minus = mean_summary(twisted_rows, "pureMinus", "chain")
    pure_zero = mean_summary(twisted_rows, "pure0", "chain")
    # G2 forward-reverse consistency of the whole ladder.
    if abs(deficit) > MULTIPLIER * se_max(deficit_se_by_scale):
        failures.append("pooled:forward_reverse_deficit")
    # G6 naive versus conditional estimators.
    for side in ("forward", "reverse"):
        if abs(consistency[side]["statistic"]) > MULTIPLIER * consistency[side]["se"]:
            consistency_failures.append(f"pooled:naive_conditional_{side}_disagreement")
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
        # G9 sector occupancy at the twisted dwell against the other chains.
        for field, summary in (("pureMinus", pure_minus), ("pure0", pure_zero)):
            own_p, own_p_se = subset_mean(dwell, field, summary["within_variance_by_block_length"])
            others_p, others_p_se = subset_mean([r for r in twisted_rows if r["chain"] != chain], field,
                                                summary["within_variance_by_block_length"])
            if not agree(own_p, se_max(own_p_se), others_p, se_max(others_p_se)):
                sector_failures.append(prefix + f"{field}_occupancy_disagreement")
        directions = {}
        for phase in ("up", "down"):
            value, _ = ladder.subset(lambda r, c=chain, p=phase: r["chain"] == c and r["phase"] == p,
                                     "phase", range(1, seam))
            directions[phase] = value
        down_or_dwell, down_se = ladder.subset(lambda r, c=chain: r["chain"] == c and r["phase"] in ("down", "dwell"),
                                               "chain")
        chain_rows = run["rows"]
        chain_results.append({
            "chain": chain, "initial": INITIAL[chain], "label": "NONINFERENTIAL_ESTIMATE",
            "log_R": own, "log_R_se_pooled_variance": se_max(own_se),
            "log_R_intermediate_by_direction": directions,
            "log_R_down_and_dwell": down_or_dwell, "log_R_down_and_dwell_se": se_max(down_se),
            "mean_Y_twisted": own_y, "mean_Y_twisted_se_pooled_variance": se_max(own_y_se),
            "twisted_dwell_halves": [halves[0][0], halves[1][0]],
            "sector_twisted_dwell": sector_summary(dwell, seam),
            "sector_down_rows": sector_summary([r for r in chain_rows if r["phase"] == "down"], seam),
            "sector_up_rows": sector_summary([r for r in chain_rows if r["phase"] == "up"], seam),
            "sector_untwisted_dwell": sector_summary([r for r in chain_rows if r["n"] == 0], seam),
            "descriptive_moments_only": {
                "mean_Y_twisted_squared": math.fsum(r["sumY2"] for r in dwell) / sum(r["count"] for r in dwell),
                "mean_action_twisted": math.fsum(r["sumS"] for r in dwell) / sum(r["count"] for r in dwell),
            },
            "input_file": run["file"], "input_sha256": run["sha256"],
        })
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
    # G8a: batch-SE calibration against the exactly known mean of chains 0 and 1 (not an equilibration test).
    if abs(y_untwisted["mean"]) > MULTIPLIER * y_untwisted["se"]:
        failures.append("chains_0_1:untwisted_mean_Y_nonzero")
    # G8b: exact bound of the stationary law; classed with the equilibration gates.
    if y2_untwisted["mean"] - MULTIPLIER * y2_untwisted["se"] > THRESHOLDS["maximum_untwisted_mean_Y_squared"]:
        failures.append("pooled:untwisted_mean_Y_squared_above_one")
    # Sector-conditional descriptive from pure down passes of chains 2 (w=0) and 4 (w=-1).
    sector_ratio = None
    if 2 in chain_log_R and 4 in chain_log_R:
        run_two = next(run for run in runs if run["key"][3] == 2)
        run_four = next(run for run in runs if run["key"][3] == 4)
        pure_two = pure_down_pass(run_two, "pure0", seam)
        pure_four = pure_down_pass(run_four, "pureMinus", seam)
        two = next(c for c in chain_results if c["chain"] == 2)
        four = next(c for c in chain_results if c["chain"] == 4)
        sector_ratio = {
            "chain_2_down_pass_pure_w0": pure_two, "chain_4_down_pass_pure_wMinus": pure_four,
            "log_ratio_wMinus_over_w0": (four["log_R_down_and_dwell"] - two["log_R_down_and_dwell"]
                                         if pure_two and pure_four else None),
            "log_ratio_se": (math.hypot(four["log_R_down_and_dwell_se"], two["log_R_down_and_dwell_se"])
                             if pure_two and pure_four else None),
            "label": "NONINFERENTIAL_SECTOR_CONDITIONAL",
        }
    chain_values = [chain_log_R[c][0] for c in chains]
    se_chain_log_R = statistics.stdev(chain_values) / math.sqrt(len(chain_values))
    se_report_log_R = max(se_max(log_R_se_by_scale), se_chain_log_R)
    y_values = [chain_Y[c][0] for c in chains]
    se_chain_Y = statistics.stdev(y_values) / math.sqrt(len(y_values))
    se_report_Y = max(y_twisted["se"], se_chain_Y)
    log_R_halfwidth = MULTIPLIER * se_report_log_R
    Y_halfwidth = MULTIPLIER * se_report_Y
    log_R_interval = [log_R - log_R_halfwidth, log_R + log_R_halfwidth]
    R_interval = [math.exp(v) for v in log_R_interval]
    batch_halfwidth = MULTIPLIER * se_max(log_R_se_by_scale)
    R_interval_batch = [math.exp(log_R - batch_halfwidth), math.exp(log_R + batch_halfwidth)]
    Y_interval = [y_twisted["mean"] - Y_halfwidth, y_twisted["mean"] + Y_halfwidth]
    corners = [a * b for a in R_interval for b in Y_interval]
    contrast_box = [min(corners), max(corners)]
    passes = not failures and not consistency_failures and not sector_failures and not degenerate
    if consistency_failures:
        status = "FAIL_CONSISTENCY"
    elif failures or degenerate:
        status = "INCONCLUSIVE_EQUILIBRATION"
    elif sector_failures:
        status = "SECTOR_FROZEN"
    else:
        status = GATES_PASSED
    return {
        "k": mode, "status": status,
        "estimate_label": "EMPIRICAL_ENGINEERING_ONLY" if passes else "NONINFERENTIAL_ESTIMATE",
        "log_R": log_R, "log_R_se_batch": se_max(log_R_se_by_scale),
        "log_R_se_between_chains": se_chain_log_R, "log_R_se_report": se_report_log_R,
        "log_R_se_by_block_length": log_R_se_by_scale,
        "log_R_interval": log_R_interval if passes else None,
        "log_R_interval_noninferential": log_R_interval,
        "log10_R_interval_noninferential": [v / math.log(10.0) for v in log_R_interval],
        "R_interval_noninferential": R_interval,
        "R_interval_batch_se": R_interval_batch,
        "log_R_resolved": passes and log_R_halfwidth <= THRESHOLDS["maximum_log_R_report_halfwidth"],
        "contrast_negligible": R_interval[1] < THRESHOLDS["negligible_contrast_R_upper"],
        "minus_log_R_per_seam_plaquette": -log_R / seam,
        "log_R_equal_weight": log_R_equal, "log_R_bar": log_R_bar,
        "forward_reverse_deficit": deficit, "forward_reverse_deficit_se": se_max(deficit_se_by_scale),
        "naive_conditional_consistency": consistency,
        "direction_split": {"up_minus_down_log_R": delta, "se": se_max(delta_se), "up": up, "down": down},
        "mean_Y_twisted": y_twisted["mean"], "mean_Y_twisted_se_batch": y_twisted["se"],
        "mean_Y_twisted_se_between_chains": se_chain_Y, "mean_Y_twisted_se_report": se_report_Y,
        "mean_Y_twisted_se_by_block_length": y_twisted["se_by_block_length"],
        "mean_Y_twisted_interval": Y_interval if passes else None,
        "mean_Y_twisted_interval_noninferential": Y_interval,
        "mean_Y_width_pass": passes and Y_halfwidth <= THRESHOLDS["maximum_mean_Y_report_halfwidth"],
        "mean_Y_interval_excludes_zero": Y_interval[0] > 0 or Y_interval[1] < 0,
        "mean_Y_twisted_squared": mean_summary(twisted_rows, "sumY2")["mean"],
        "mean_Y_untwisted_chains_0_1": y_untwisted["mean"], "mean_Y_untwisted_chains_0_1_se": y_untwisted["se"],
        "mean_Y_untwisted_all_chains": y_untwisted_all["mean"], "mean_Y_untwisted_all_chains_se": y_untwisted_all["se"],
        "mean_Y_untwisted_squared": y2_untwisted["mean"],
        "mean_Y_untwisted_squared_se": y2_untwisted["se"],
        "mean_action_untwisted": mean_summary(untwisted_rows, "sumS")["mean"],
        "mean_action_twisted": mean_summary(twisted_rows, "sumS")["mean"],
        "signed_contrast_box_noninferential": contrast_box,
        "sector_twisted_dwell_pooled": sector_summary(twisted_rows, seam),
        "sector_conditional": sector_ratio,
        "coarsening_se_ratios": ratios,
        "diagnostic_failures": failures, "consistency_failures": consistency_failures,
        "sector_failures": sector_failures,
        "chains": chain_results, "steps": steps,
    }


def analyze_control(runs, size, mode):
    """Exact control group: whole-seam source 2k, pass to 3k = -2k. Exact identities."""
    seam = size * size
    rows = [r for run in runs for r in run["rows"]]
    ladder = Ladder(rows, seam, mode)
    log_R, log_R_se = ladder.partial(0, seam)
    failures = []
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
    y_start = mean_summary([r for r in rows if r["n"] == 0], "sumY")
    y_end = mean_summary([r for r in rows if r["n"] == seam], "sumY")
    if abs(y_start["mean"] + y_end["mean"]) > MULTIPLIER * math.hypot(y_start["se"], y_end["se"]):
        failures.append("control:mean_Y_reversal_antisymmetry")
    deficit, deficit_se = ladder.deficit()
    steps, log_R_bar, log_R_equal = ladder.steps()
    return {
        "k": mode, "status": "FAIL_CONSISTENCY" if failures else "CONTROL_PASS",
        "log_R": log_R, "log_R_se_batch": se_max(log_R_se), "log_R_bar": log_R_bar,
        "log_R_equal_weight": log_R_equal,
        "row_symmetry": symmetry,
        "mean_Y_source_2k": y_start["mean"], "mean_Y_source_2k_se": y_start["se"],
        "mean_Y_source_3k": y_end["mean"], "mean_Y_source_3k_se": y_end["se"],
        "forward_reverse_deficit": deficit, "forward_reverse_deficit_se": se_max(deficit_se),
        "control_failures": failures,
        "sector_source_2k": sector_summary([r for r in rows if r["n"] == 0], seam),
        "sector_source_3k": sector_summary([r for r in rows if r["n"] == seam], seam),
        "chains": [{"chain": run["key"][3], "initial": INITIAL[run["key"][3]],
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
    """Exact positivity of the seam-residue law from the two ratios, at interval corners."""
    by_k = {item["k"]: item for item in modes}
    R1 = by_k[1]["R_interval_batch_se"]
    R2 = by_k[2]["R_interval_batch_se"]
    corners = [residue_law(a, b) for a in R1 for b in R2]
    law_interval = {name: [min(c[name] for c in corners), max(c[name] for c in corners)] for name in ("p0", "p1", "p2")}
    # Most favourable corner: R1 low against R2 high, and vice versa.
    inequality_1 = R1[0] <= 1 / PHI + R2[1] / PHI ** 2
    inequality_2 = R2[0] <= 1 / PHI + R1[1] / PHI ** 2
    return {"residue_law_interval_noninferential": law_interval,
            "R1_le_0.618_plus_0.382_R2": inequality_1, "R2_le_0.618_plus_0.382_R1": inequality_2,
            "applicable": all(not item["sector_failures"] for item in modes)}


def report(runs):
    result = {
        "analysis": "C-PHOTON-TWIST-SNAKE-DIAGNOSTIC-N",
        "status": "INCOMPLETE", "status_precedence": STATUS_ORDER, "thresholds": THRESHOLDS,
        "scope": "NON-CANONICAL engineering diagnostics of finite-volume twisted ratios and signed contrasts",
        "coverage": "4SE intervals are empirical; no rigorous or simultaneous coverage is claimed",
        "limitations": [
            "Passing the gates does not prove equilibration, stationarity or decorrelation.",
            "No thermodynamic, phase, scaling, or P1 verdict is produced.",
            "Squared ranges are formed from signed boxes, not squared noisy point estimates.",
            "All estimates remain visible even when inference is withheld.",
            "Values at different L are reported separately; no comparison across L is made.",
            "Sector-conditional values are descriptive and carry no inferential label.",
        ],
        "missing_runs": [], "volumes": [], "controls": [],
    }
    indexed = {}
    for run in runs:
        require(run["key"] not in indexed, f"duplicate run {run['key']}")
        indexed[run["key"]] = run
    result["missing_runs"] = [list(key) for key in declared_jobs() if key not in indexed]
    result["available_run_count"] = len(runs)
    # Exact control groups first: a failure taints every main group.
    control_failed = False
    for size in CONTROL_L_VALUES:
        for mode in MODES:
            keys = [(size, mode, CONTROL_BASE, chain) for chain in CONTROL_CHAINS]
            if all(key in indexed for key in keys):
                control = analyze_control([indexed[key] for key in keys], size, mode)
                control_failed = control_failed or control["status"] == "FAIL_CONSISTENCY"
            else:
                control = {"k": mode, "status": "INCOMPLETE",
                           "available_chains": [indexed[key]["file"] for key in keys if key in indexed]}
            control["L"] = size
            result["controls"].append(control)
    for size in L_VALUES:
        modes = []
        for mode in MODES:
            keys = [(size, mode, MAIN_BASE, chain) for chain in MAIN_CHAINS]
            if all(key in indexed for key in keys):
                item = analyze_mode([indexed[key] for key in keys], size, mode)
                if control_failed:
                    item["consistency_failures"].append("control:exact_control_group_failed")
                    item["status"] = "FAIL_CONSISTENCY"
                    item["estimate_label"] = "NONINFERENTIAL_ESTIMATE"
                    item["log_R_interval"] = None
                    item["mean_Y_twisted_interval"] = None
                modes.append(item)
            else:
                partial = [indexed[key] for key in keys if key in indexed]
                modes.append({
                    "k": mode, "status": "INCOMPLETE", "estimate_label": "NONINFERENTIAL_ESTIMATE",
                    "sector_failures": [],
                    "available_chains": [
                        {"chain": run["key"][3], "initial": INITIAL[run["key"][3]],
                         "input_file": run["file"], "input_sha256": run["sha256"]}
                        for run in partial
                    ],
                })
        volume = {"L": size, "modes": modes}
        positivity = cross_mode(modes) if all(item["status"] != "INCOMPLETE" for item in modes) else None
        volume["cross_mode_positivity"] = positivity
        if positivity and positivity["applicable"] and not (
                positivity["R1_le_0.618_plus_0.382_R2"] and positivity["R2_le_0.618_plus_0.382_R1"]):
            for item in modes:
                item["consistency_failures"].append("pooled:cross_mode_positivity_violated")
                if item["status"] in (GATES_PASSED, "INCONCLUSIVE_EQUILIBRATION", "SECTOR_FROZEN"):
                    item["status"] = "FAIL_CONSISTENCY"
                    item["estimate_label"] = "NONINFERENTIAL_ESTIMATE"
                    item["log_R_interval"] = None
                    item["mean_Y_twisted_interval"] = None
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
        if any(c["status"] == "INCOMPLETE" and c["L"] == size for c in result["controls"]):
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
