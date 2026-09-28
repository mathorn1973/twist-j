#!/usr/bin/env python3
"""Synthetic fixture tests for analyze.py. NON-CANONICAL.

Every number below is fabricated by a pseudo-random generator with the
frozen file layout; nothing here is a sampler output or a scientific value.
Run: python3 test_analyze.py
"""
import hashlib
import json
import math
import random
import re
import sys
import tempfile
from collections import Counter
from pathlib import Path

import analyze

HEADER = ("L\tk\tchain\tkind\tsegment\tn\tphase\tblock\tcount"
          "\tsumFn\tsumFn2\tsumFi\tsumFi2\tsumBn\tsumBn2\tsumBi\tsumBi2\tsumPFi\tsumPFi2"
          "\tsumY\tsumY2\tsumS\tsumS2\thF0\thF1\thF2\thF3\thF4\thB0\thB1\thB2\thB3\thB4"
          "\tsec0\tsecMinus\tsecPlus\tsecOther\tuntMinus\tuntPlus\tuntOther"
          "\tpure0\tpureMinus\tpurePlus\tflips\tclassMinus\tsumW\tminW\tmaxW\tforced")
COLUMNS = HEADER.split("\t")
U, CONTROL, P, C0, CM = analyze.KIND_MAIN, analyze.KIND_CONTROL, analyze.KIND_PI1, analyze.KIND_CLASS0, analyze.KIND_CLASSM


def static_layout_check():
    """The sampler's header literal and metadata keys agree with the analyzer's layout."""
    source = Path(__file__).resolve().with_name("sample.cpp").read_text()
    start = source.index('"L\\tk\\tchain\\tkind')
    end = source.index('\\n";', start)
    pieces = re.findall(r'"((?:[^"\\]|\\.)*)"', source[start:end + 3])
    header = "".join(pieces).encode().decode("unicode_escape").rstrip("\n")
    assert header == HEADER, (header, HEADER)
    assert len(COLUMNS) == 49 and set(COLUMNS) == analyze.FIELDS
    keys = set(re.findall(r'# ([A-Za-z_]+)\\t', source))
    analyzer_keys = {"format", "L", "k", "chain", "kind", "kind_name", "base", "restriction", "schedule", "seed",
                     "seam_size", "start_twist", "chain_initial", "warmup_sweeps", "dwell_sweeps", "dwell_long_sweeps",
                     "visit_sweeps",
                     "equilibration_sweeps", "post_forcing_sweeps", "block_length", "segments", "seam_order",
                     "class_rule", "sampling", "final_twist", "forced_steps", "sweeps_total", "completion"}
    assert analyzer_keys <= keys, analyzer_keys - keys
    assert re.search(r"seed_base = UINT64_C\((\d+)\)", source).group(1) == str(analyze.SEED_BASE)
    assert re.search(r"constexpr int field_count = (\d+);", source).group(1) == str(len(COLUMNS))
    print("static layout check ok")


# ---------------------------------------------------------------------------
# Fabricated truths


def two_point(mode, target):
    """Flux law between the smallest ratio value and the value closest to one with mean `target`."""
    values = analyze.RATIO[mode]
    i_low = values.index(min(values))
    i_one = min(range(5), key=lambda f: abs(values[f] - 1.0))
    low, one = values[i_low], values[i_one]
    t = min(max((target - low) / (one - low), 0.0), 1.0)
    p = [0.0] * 5
    p[i_low] = 1.0 - t
    p[i_one] = t
    return p


def law_mean(mode, p):
    return math.fsum(pp * v for pp, v in zip(p, analyze.RATIO[mode]))


def unconstrained_truth(size, mode, rng, control=False):
    """Per-step flux laws (unconstrained ladder from n=0), as in the consumed generator."""
    values = analyze.RATIO[mode]
    seam = size * size
    probs = [two_point(mode, math.exp(rng.uniform(-0.35, -0.02))) for _ in range(seam)]
    if control:
        i_one = min(range(5), key=lambda f: abs(values[f] - 1.0))
        i_high = values.index(max(values))
        one, high = values[i_one], values[i_high]
        for n in range(seam // 2, seam):
            target = 1.0 / law_mean(mode, probs[seam - 1 - n])
            t = min(max((target - one) / (high - one), 0.0), 1.0)
            p = [0.0] * 5
            p[i_one] = 1.0 - t
            p[i_high] = t
            probs[n] = p
    return {"p": probs, "r": [law_mean(mode, pr) for pr in probs], "q": [1.0] * seam, "qp": [1.0] * seam}


def restricted_truth(size, mode, rng, r_scale=1.0):
    """Restricted ladder n = 1..L^2-1: step ratio r_n, forward indicator probability q_n (PF),
    reverse indicator probability qp_n (PB); F_n = r_n qp_n, Bw_n = q_n / r_n; the flux law
    over indicator-1 forward sweeps has mean r_n qp_n / q_n <= 1."""
    seam = size * size
    truth = {"p": [None], "r": [None], "q": [None], "qp": [None]}
    for _ in range(1, seam):
        r = min(1.0, math.exp(rng.uniform(-0.3, -0.02)) * r_scale)
        q = rng.uniform(0.6, 0.95)
        qp = q * rng.uniform(0.8, 1.0)
        p = two_point(mode, r * qp / q)
        r = law_mean(mode, p) * q / qp  # exact value of the fabricated law
        truth["p"].append(p)
        truth["r"].append(r)
        truth["q"].append(q)
        truth["qp"].append(qp)
    return truth


def make_truth(size, mode, rng):
    """All fabricated quantities of one (L,k): step 0, pi_1(-), two restricted ladders, the
    consistent unconstrained ladder, and the endpoint means of Y."""
    seam = size * size
    r0_law = two_point(mode, math.exp(rng.uniform(-0.3, -0.05)))
    r0 = law_mean(mode, r0_law)
    pi = rng.uniform(0.15, 0.4)
    c0 = restricted_truth(size, mode, rng)
    cm = restricted_truth(size, mode, rng, r_scale=0.9)
    l0 = math.fsum(math.log(r) for r in c0["r"][1:])
    lm = math.fsum(math.log(r) for r in cm["r"][1:])
    log_D = math.log((1 - pi) * math.exp(l0) + pi * math.exp(lm))
    u_step = math.exp(log_D / (seam - 1))
    u_probs = [r0_law] + [two_point(mode, u_step) for _ in range(1, seam)]
    u = {"p": u_probs, "r": [law_mean(mode, p) for p in u_probs], "q": [1.0] * seam, "qp": [1.0] * seam}
    Y0, Ym = rng.uniform(0.3, 0.6), rng.uniform(-0.6, -0.3)
    Pm = pi * math.exp(lm) / math.exp(log_D)
    Y = (1 - Pm) * Y0 + Pm * Ym
    return {"r0": r0, "pi": pi, "ladders": {U: u, C0: c0, CM: cm},
            "log_R": math.fsum(math.log(r) for r in u["r"]), "log_R_class_sum": math.log(r0) + log_D,
            "l0": l0, "lm": lm, "P_minus": Pm,
            "Y": {U: Y, C0: Y0, CM: Ym, P: rng.uniform(-0.5, 0.5)}}


# ---------------------------------------------------------------------------
# Fabricated records


def fabricate_run(directory, size, mode, kind, chain, rng, truth, corrupt=None, sector="agree", hook=None):
    seam = size * size
    values = analyze.RATIO[mode]
    low, high = analyze.RATIO_BOUNDS[mode]
    restricted = kind in analyze.RESTRICTED_KINDS
    ladder_chain = restricted and not analyze.top_dwell(kind, chain)
    sequence = analyze.expected_segments(size, kind, chain)
    lines = [
        "# format\ttwist_snake_sector_blocks_v2",
        "# status\tNON-CANONICAL floating-point engineering diagnostic",
        f"# L\t{size}", f"# k\t{mode}", f"# chain\t{chain}", f"# kind\t{kind}",
        f"# kind_name\t{analyze.KIND_NAMES[kind]}", f"# base\t{analyze.BASE[kind]}",
        f"# restriction\t{analyze.RESTRICTION[kind]}", f"# schedule\t{analyze.schedule_name(kind, chain)}",
        f"# seed\t{analyze.SEED_BASE + 1000 * size + 100 * mode + 10 * kind + chain}",
        f"# seam_size\t{seam}", f"# start_twist\t{analyze.start_twist(size, kind, chain)}",
        f"# chain_initial\t{analyze.initial_name(kind, chain)}",
        f"# warmup_sweeps\t{analyze.WARMUP_SWEEPS}", f"# dwell_sweeps\t{analyze.DWELL_SWEEPS}",
        f"# dwell_long_sweeps\t{analyze.DWELL_LONG_SWEEPS}",
        f"# visit_sweeps\t{analyze.VISIT_SWEEPS}",
        f"# equilibration_sweeps\t{analyze.EQUILIBRATION_SWEEPS}",
        f"# post_forcing_sweeps\t{analyze.POST_FORCING_SWEEPS}",
        f"# block_length\t{analyze.BLOCK_LENGTH}", f"# segments\t{len(sequence)}",
        "# seam_order\tx2_fastest_then_x3",
        "# class_rule\tclass0_if_2W_ge_minus_n_else_classMinus",
        "# action_density\tminus_sum_logW_divided_by_6L4",
        "# sampling\tevery_production_sweep_after_full_heatbath_sweep",
        HEADER,
    ]
    ladder = truth["ladders"].get(kind) if kind in (U, C0, CM) else truth.get("control")
    if kind == P:
        ladder = truth["ladders"][U]

    def binomial(count, q):
        if q >= 1.0:
            return count
        return sum(1 for _ in range(count) if rng.random() < q)

    def histogram(probs, total):
        counts = Counter(rng.choices(range(5), weights=probs, k=total)) if total else Counter()
        return [counts.get(f, 0) for f in range(5)]

    def conditional(mean_value, count, floor, ceiling, spread=0.05):
        value = min(ceiling, max(floor, mean_value + spread * rng.gauss(0, 1) / 4))
        total = value * count
        return total, total ** 2 / count + count * spread ** 2 * (1.0 + 0.1 * abs(rng.gauss(0, 1)))

    def forward(n, count):
        q = ladder["q"][n]
        n_ind = binomial(count, q)
        hist = histogram(ladder["p"][n], n_ind)
        naive = math.fsum(hist[f] * values[f] for f in range(5))
        naive2 = math.fsum(hist[f] * values[f] ** 2 for f in range(5))
        f_mean = ladder["r"][n] * ladder["qp"][n]
        fi = conditional(f_mean, count, 0.0 if restricted else low, high)
        pfi = (count, count) if not restricted else conditional(q, count, 0.0, 1.0)
        return (naive, naive2), fi, pfi, hist

    def reverse(n, count):
        # Reverse of step n at twist n + 1: indicator probability qp_n, pushforward flux law.
        qp = ladder["qp"][n]
        n_ind = binomial(count, qp)
        probs = [0.0] * 5
        vals = [0.0] * 5
        total = law_mean(mode, ladder["p"][n])
        for f in range(5):
            probs[(f + mode) % 5] = ladder["p"][n][f] * values[f] / total
            vals[(f + mode) % 5] = 1.0 / values[f]
        hist = histogram(probs, n_ind)
        naive = math.fsum(hist[f] * vals[f] for f in range(5))
        naive2 = math.fsum(hist[f] * vals[f] ** 2 for f in range(5))
        b_mean = ladder["q"][n] / ladder["r"][n]
        bi = conditional(b_mean, count, 0.0 if restricted else low, high)
        return (naive, naive2), bi, hist

    zero = ((0.0, 0.0), (0.0, 0.0), (0.0, 0.0), [0] * 5)
    forced_total = 0
    for segment, (n, phase, blocks) in enumerate(sequence):
        forced = 0
        if ladder_chain and segment > 0 and n % 2 == 0 and rng.random() < (0.75 if kind == CM else 0.1):
            forced = 1  # a fabricated forcing pattern; the analyzer only checks the flag's form
        forced_total += forced
        for block in range(blocks):
            count = analyze.BLOCK_LENGTH
            if n == seam:
                f, fi, pfi, hf = zero
            else:
                f, fi, pfi, hf = forward(n, count)
            if n == 0 or (kind == CM and n == 1):
                b, bi, hb = (0.0, 0.0), (0.0, 0.0), [0] * 5
            elif kind == C0 and n == 1:
                # The unconstrained reverse estimator of step 0 is recorded but unused.
                b, bi, hb = reverse_unconstrained(truth, mode, count, rng, values, low, high, histogram)
            else:
                b, bi, hb = reverse(n - 1, count)
            if kind == U:
                y_mean = truth["Y"][U] if n == seam else 0.0
            elif kind == P:
                y_mean = truth["Y"][P] if n == 1 else 0.0
            elif kind in (C0, CM):
                y_mean = truth["Y"][kind] if n == seam else 0.0
            else:
                y_mean = truth["Yc"] if n == 0 else (-truth["Yc"] if n == seam else 0.0)
            sum_y = count * y_mean + math.sqrt(count) * 0.5 * rng.gauss(0, 1)
            sum_y2 = sum_y ** 2 / count + count * 0.25 * (1.0 + 0.1 * abs(rng.gauss(0, 1)))
            sum_s = count * 1.16 + math.sqrt(count) * 0.01 * rng.gauss(0, 1)
            sum_s2 = sum_s ** 2 / count + count * 1e-4
            # Sector bookkeeping. Unconstrained kinds: all twisted slices w = 0 except that at
            # n = 1 the single slice is in class minus with probability pi (W = -1 there);
            # the frozen chain 4 has every twisted slice at w = -1. Class-minus kinds: every
            # twisted slice at w = -1 (W = -n).
            if (sector == "frozen" and kind == U and chain == 4) or kind == CM:
                class_minus = count if n > 0 else 0
                sec = [0, count * n, 0, 0]
                pure = [0, count if n > 0 else 0, 0]
                sum_w, min_w, max_w = -n * count, -n, -n
            elif n == 1 and kind in (U, P, CONTROL) and analyze.BASE[kind] == 0:
                class_minus = binomial(count, truth["pi"])
                sec = [count - class_minus, class_minus, 0, 0]
                pure = [count - class_minus, class_minus, 0]
                sum_w, min_w, max_w = -class_minus, -1 if class_minus else 0, 0 if class_minus < count else -1
            else:
                class_minus = 0
                sec = [count * n, 0, 0, 0]
                pure = [count if n > 0 else 0, 0, 0]
                sum_w, min_w, max_w = 0, 0, 0
            unt = [0, 0, 0]
            values_list = ([size, mode, chain, kind, segment, n, phase, block, count,
                            f[0], f[1], fi[0], fi[1], b[0], b[1], bi[0], bi[1], pfi[0], pfi[1],
                            sum_y, sum_y2, sum_s, sum_s2] + hf + hb + sec + unt + pure
                           + [0, class_minus, sum_w, min_w, max_w, forced])
            row = dict(zip(COLUMNS, values_list))
            if corrupt == "order" and segment == 3 and block == 0:
                row["n"] = n + 1
            if corrupt == "zero_visit" and segment == 3 and block == 1:
                for key in ("sumFn", "sumFn2", "sumFi", "sumFi2"):
                    row[key] = 0.0
                for key in ("hF0", "hF1", "hF2", "hF3", "hF4"):
                    row[key] = 0
            if hook is not None:
                hook(row)
            lines.append("\t".join(repr(row[c]) if isinstance(row[c], float) else str(row[c]) for c in COLUMNS))
    lines.append(f"# final_twist\t{analyze.final_twist(size, kind, chain)}")
    lines.append(f"# forced_steps\t{forced_total}")
    steps = len(sequence) - 1
    production = sum(blocks for _, _, blocks in sequence) * analyze.BLOCK_LENGTH
    lines.append(f"# sweeps_total\t{analyze.WARMUP_SWEEPS + production + (steps - forced_total) * analyze.EQUILIBRATION_SWEEPS + forced_total * analyze.POST_FORCING_SWEEPS}")
    lines.append("# completion\tPASS")
    stem = analyze.stem_of(size, mode, kind, chain)
    (directory / f"{stem}.tsv").write_text("\n".join(lines) + "\n")
    (directory / f"{stem}.stderr").write_bytes(b"")
    return stem


def reverse_unconstrained(truth, mode, count, rng, values, low, high, histogram):
    p0 = truth["ladders"][U]["p"][0]
    total = law_mean(mode, p0)
    probs = [0.0] * 5
    vals = [0.0] * 5
    for f in range(5):
        probs[(f + mode) % 5] = p0[f] * values[f] / total
        vals[(f + mode) % 5] = 1.0 / values[f]
    hist = histogram(probs, count)
    naive = math.fsum(hist[f] * vals[f] for f in range(5))
    naive2 = math.fsum(hist[f] * vals[f] ** 2 for f in range(5))
    b_mean = min(high, max(low, 1.0 / total + 0.0125 * rng.gauss(0, 1)))
    return (naive, naive2), (b_mean * count, (b_mean * count) ** 2 / count + count * 0.05 ** 2), hist


def record(directory, stem, code=0):
    out = (directory / f"{stem}.tsv").read_bytes()
    err = (directory / f"{stem}.stderr").read_bytes()
    return {"stem": stem, "exit_code": code, "seconds": 1.0,
            "stdout_bytes": len(out), "stderr_bytes": len(err),
            "stdout_sha256": hashlib.sha256(out).hexdigest(),
            "stderr_sha256": hashlib.sha256(err).hexdigest()}


def build(directory, sizes, rng, corrupt=None, drop=(), audit=True, sector="agree", control_bias=0.0,
          hooks=None, truth_for=None, control_hook=None, control_sector=None):
    """Fabricate every declared job of the listed sizes. `drop` lists (L,k,kind,chain) keys to omit;
    `hooks` maps stems to row hooks; `truth_for(L,k,kind,chain,truth)` may replace a chain's truth."""
    hooks = hooks or {}
    (directory / "audit.tsv").write_text(analyze.EXPECTED_AUDIT if audit else "broken\n")
    (directory / "audit.stderr").write_bytes(b"")
    (directory / "environment.json").write_text(json.dumps(
        {"architecture": "synthetic", "system": "synthetic", "python": "synthetic",
         "workers": 4, "audit_timeout_seconds": 600, "per_chain_timeout_seconds": 2400,
         "binary_sha256": "0" * 64}, indent=2) + "\n")
    records = [record(directory, "audit")]
    truths = {}
    for size in sizes:
        for mode in analyze.MODES:
            truth = make_truth(size, mode, rng)
            truths[(size, mode)] = truth
            for kind in (U, P, C0, CM):
                for chain in analyze.KIND_CHAINS[kind]:
                    if (size, mode, kind, chain) in drop:
                        continue
                    chain_truth = truth_for(size, mode, kind, chain, truth) if truth_for else truth
                    stem = analyze.stem_of(size, mode, kind, chain)
                    fabricate_run(directory, size, mode, kind, chain, rng, chain_truth,
                                  corrupt if (size, mode, kind, chain) == (4, 1, U, 0) else None, sector,
                                  hooks.get(stem))
                    records.append(record(directory, stem))
            if size in analyze.CONTROL_L_VALUES:
                control = dict(truth)
                control["control"] = unconstrained_truth(size, mode, rng, control=True)
                control["Yc"] = rng.uniform(-0.5, 0.5)
                if control_bias:
                    control["control"]["p"] = [[1.0 if f == 0 else 0.0 for f in range(5)]] * (size * size)
                    control["control"]["r"] = [analyze.RATIO[mode][0]] * (size * size)
                for chain in analyze.KIND_CHAINS[CONTROL]:
                    if (size, mode, CONTROL, chain) in drop:
                        continue
                    hook = control_hook
                    if control_sector and (size, chain) in control_sector:
                        hook = control_sector[(size, chain)]
                    stem = fabricate_run(directory, size, mode, CONTROL, chain, rng, control, hook=hook)
                    records.append(record(directory, stem))
    (directory / "execution.json").write_text(json.dumps(records, indent=2) + "\n")
    return truths


def modes_of(result, size=4):
    volume = next(v for v in result["volumes"] if v["L"] == size)
    return {m["k"]: m for m in volume["modes"]}


def main():
    static_layout_check()
    rng = random.Random(12345)
    with tempfile.TemporaryDirectory() as tmp:
        directory = Path(tmp) / "clean"
        directory.mkdir()
        truths = build(directory, analyze.L_VALUES, rng)
        result = analyze.read_execution(directory)
        json.dumps(result, sort_keys=True, allow_nan=False)
        assert result["execution_errors"] == [], result["execution_errors"]
        assert result["status"] not in ("FAIL_IMPLEMENTATION", "FAIL_CONSISTENCY", "INCOMPLETE"), result["status"]
        assert result["missing_runs"] == []
        assert all(c["status"] == "CONTROL_PASS" for c in result["controls"]), [
            (c["L"], c["k"], c["status"], c.get("control_failures"), c.get("sector_failures")) for c in result["controls"]]
        for volume in result["volumes"]:
            for mode in volume["modes"]:
                truth = truths[(volume["L"], mode["k"])]
                assert mode["status"] == analyze.GATES_PASSED, (volume["L"], mode["k"], mode["diagnostic_failures"],
                                                               mode["consistency_failures"])
                assert mode["U"]["status"] == analyze.GATES_PASSED, mode["U"]["diagnostic_failures"]
                assert mode["cross_check_G11"]["pass"] is True, mode["cross_check_G11"]
                assert abs(mode["log_R"] - truth["log_R_class_sum"]) <= 6 * mode["log_R_se_report"] + 0.05, (
                    volume["L"], mode["k"], mode["log_R"], truth["log_R_class_sum"], mode["log_R_se_report"])
                assert abs(mode["U"]["log_R"] - truth["log_R"]) <= 6 * mode["U"]["log_R_se_report"] + 0.05
                assert abs(mode["U"]["log_R_bar"] - truth["log_R"]) <= 6 * mode["U"]["log_R_se_report"] + 0.1
                assert abs(mode["mean_Y_twisted"] - truth["Y"][U]) <= 6 * mode["mean_Y_twisted_se_report"] + 0.03, (
                    mode["mean_Y_twisted"], truth["Y"][U], mode["mean_Y_twisted_se_report"])
                assert abs(mode["P_minus"] - truth["P_minus"]) <= 6 * mode["P_minus_se_report"] + 0.03
                assert abs(mode["P"]["pi1_minus"] - truth["pi"]) <= 6 * mode["P"]["pi1_minus_se_report"] + 0.01
                assert abs(mode["class0"]["log_l"] - truth["l0"]) <= 6 * mode["class0"]["log_l_se_report"] + 0.05
                assert abs(mode["classMinus"]["log_l"] - truth["lm"]) <= 6 * mode["classMinus"]["log_l_se_report"] + 0.05
                assert len(mode["class0"]["steps"]) == volume["L"] ** 2 - 1
                assert len(mode["U"]["steps"]) == volume["L"] ** 2 and len(mode["U"]["chains"]) == 5
                assert mode["U"]["sector_failures"] == [] and mode["U"]["calibration_failures"] == []
            assert volume["cross_mode_positivity"]["applicable"] is True
            assert volume["status"] in ("RESOLVED_SIGNED_CONTRAST", "UNRESOLVED")
            assert volume["D_empirical_engineering_interval"] is not None
        print("clean fixture:", result["status"], [(v["L"], v["status"]) for v in result["volumes"]])

        directory = Path(tmp) / "frozen"
        directory.mkdir()
        build(directory, (4,), random.Random(5), sector="frozen")
        result = analyze.read_execution(directory)
        assert result["execution_errors"] == [], result["execution_errors"]
        for m in modes_of(result).values():
            assert m["U"]["status"] == analyze.SECTOR_FROZEN, (m["U"]["status"], m["U"]["diagnostic_failures"])
            assert m["U"]["sector_failures"], m["U"]["sector_failures"]
            assert m["cross_check_G11"]["pass"] is None
            assert m["status"] == analyze.GATES_PASSED, (m["status"], m["diagnostic_failures"])
        assert result["volumes"][0]["status"] in ("RESOLVED_SIGNED_CONTRAST", "UNRESOLVED")
        print("frozen U chain 4: U route", modes_of(result)[1]["U"]["status"], "volume", result["volumes"][0]["status"])

        directory = Path(tmp) / "control_violation"
        directory.mkdir()
        build(directory, (4,), random.Random(6), control_bias=1.0)
        result = analyze.read_execution(directory)
        assert result["execution_errors"] == [], result["execution_errors"]
        assert all(c["status"] == "FAIL_CONSISTENCY" for c in result["controls"] if c["L"] == 4), [
            c["status"] for c in result["controls"]]
        assert result["volumes"][0]["status"] == "FAIL_CONSISTENCY", result["volumes"][0]["status"]
        assert all("control:qualified_control_group_failed" in m["consistency_failures"]
                   for m in result["volumes"][0]["modes"])
        print("control violation:", result["status"])

        # Control sector freeze: chain 3 sits in another sector at the 3k endpoint.
        def freeze_3k(row):
            seam = row["L"] ** 2
            if row["n"] == seam:
                row["untMinus"] = 0
                row["secMinus"], row["sec0"] = int(0.9 * row["count"] * seam), row["count"] * seam - int(0.9 * row["count"] * seam)
                row["sumY"] = -3.0 * row["count"]
                row["sumY2"] = row["sumY"] ** 2 / row["count"] + row["count"] * 0.25
        directory = Path(tmp) / "control_frozen"
        directory.mkdir()
        build(directory, (4, 6), random.Random(13), control_sector={(4, 3): freeze_3k})
        result = analyze.read_execution(directory)
        assert result["execution_errors"] == [], result["execution_errors"]
        four = [c for c in result["controls"] if c["L"] == 4]
        six = [c for c in result["controls"] if c["L"] == 6]
        assert all(c["status"] == "CONTROL_SECTOR_FROZEN" and c["qualified"] is False for c in four), [
            (c["status"], c["sector_failures"]) for c in four]
        assert all(any("chain_3" in f for f in c["sector_failures"]) for c in four)
        assert all(c["status"] == "CONTROL_PASS" for c in six)
        for volume in result["volumes"][:2]:
            for m in volume["modes"]:
                assert m["status"] == analyze.GATES_PASSED, (volume["L"], m["status"], m["diagnostic_failures"])
        print("control sector frozen at L=4, qualified at L=6:", [(c["L"], c["k"], c["status"]) for c in result["controls"]])

        directory = Path(tmp) / "no_qualified_control"
        directory.mkdir()
        build(directory, (4, 6), random.Random(14), control_sector={(4, 3): freeze_3k, (6, 3): freeze_3k})
        result = analyze.read_execution(directory)
        assert result["execution_errors"] == [], result["execution_errors"]
        assert all(c["status"] == "CONTROL_SECTOR_FROZEN" for c in result["controls"])
        for volume in result["volumes"][:2]:
            for m in volume["modes"]:
                assert m["status"] == "INCONCLUSIVE_EQUILIBRATION" and "control:no_qualified_control_group" in m["diagnostic_failures"]
            assert volume["status"] == "INCONCLUSIVE_EQUILIBRATION"
        print("no qualified control:", result["status"])

        directory = Path(tmp) / "corrupt_order"
        directory.mkdir()
        build(directory, (4,), random.Random(7), corrupt="order")
        result = analyze.read_execution(directory)
        assert result["status"] == "FAIL_IMPLEMENTATION", result["status"]
        assert any("block sequence" in e for e in result["execution_errors"]), result["execution_errors"]
        print("corrupt block order:", result["status"])

        directory = Path(tmp) / "zero_visit"
        directory.mkdir()
        build(directory, (4,), random.Random(7), corrupt="zero_visit")
        result = analyze.read_execution(directory)
        assert result["status"] == "FAIL_IMPLEMENTATION", result["status"]
        assert any("histogram" in e or "bounds" in e for e in result["execution_errors"]), result["execution_errors"]
        print("zero forward sums at a visit:", result["status"])

        directory = Path(tmp) / "missing_class_chain"
        directory.mkdir()
        build(directory, (4, 6), random.Random(8), drop=((6, 2, CM, 1),))
        result = analyze.read_execution(directory)
        assert result["status"] == "INCOMPLETE", result["status"]
        assert [6, 2, CM, 1] in result["missing_runs"]
        six = result["volumes"][1]
        assert six["status"] == "INCOMPLETE"
        assert six["modes"][0]["status"] == analyze.GATES_PASSED
        assert six["modes"][1]["status"] == "INCOMPLETE" and len(six["modes"][1]["available_chains"]) == 14
        assert result["volumes"][0]["status"] in ("RESOLVED_SIGNED_CONTRAST", "UNRESOLVED")
        print("missing class chain:", result["status"], [(v["L"], v["status"]) for v in result["volumes"]])

        directory = Path(tmp) / "missing_U_chain"
        directory.mkdir()
        build(directory, (4,), random.Random(8), drop=((4, 1, U, 3),))
        result = analyze.read_execution(directory)
        assert result["volumes"][0]["status"] != "INCOMPLETE", result["volumes"][0]["status"]
        one = modes_of(result)[1]
        assert one["U"]["status"] == "INCOMPLETE" and one["cross_check_G11"]["pass"] is None
        assert one["status"] == analyze.GATES_PASSED, (one["status"], one["diagnostic_failures"])
        assert [4, 1, U, 3] in result["missing_runs"]
        print("missing U chain: mode", one["status"], "U route", one["U"]["status"], "volume", result["volumes"][0]["status"])

        directory = Path(tmp) / "bad_audit"
        directory.mkdir()
        build(directory, (4,), random.Random(9), audit=False)
        result = analyze.read_execution(directory)
        assert result["status"] == "FAIL_IMPLEMENTATION"
        assert any("audit" in e for e in result["execution_errors"])
        print("bad audit:", result["status"])

        directory = Path(tmp) / "tampered_hash"
        directory.mkdir()
        build(directory, (4,), random.Random(10))
        path = directory / "L4_k2_classMinus_c1.tsv"
        path.write_bytes(path.read_bytes() + b"\n")
        result = analyze.read_execution(directory)
        assert result["status"] == "FAIL_IMPLEMENTATION"
        assert any("stdout_bytes mismatch" in e for e in result["execution_errors"])
        print("tampered bytes:", result["status"])

        directory = Path(tmp) / "timeout"
        directory.mkdir()
        build(directory, (4,), random.Random(11))
        records = json.loads((directory / "execution.json").read_text())
        for item in records:
            if item["stem"] == "L4_k1_pi1_c1":
                item["exit_code"] = 124
        (directory / "execution.json").write_text(json.dumps(records, indent=2) + "\n")
        result = analyze.read_execution(directory)
        assert result["status"] == "INCOMPLETE", result["status"]
        assert result["execution_errors"] == []
        assert result["unavailable_jobs"] == [{"stem": "L4_k1_pi1_c1", "exit_code": 124}]
        assert modes_of(result)[1]["status"] == "INCOMPLETE"
        print("timed-out job:", result["status"])

        directory = Path(tmp) / "crash"
        directory.mkdir()
        build(directory, (4,), random.Random(12))
        records = json.loads((directory / "execution.json").read_text())
        for item in records:
            if item["stem"] == "L4_k2_class0_c2":
                item["exit_code"] = 1
        (directory / "execution.json").write_text(json.dumps(records, indent=2) + "\n")
        result = analyze.read_execution(directory)
        assert result["status"] == "FAIL_IMPLEMENTATION", result["status"]
        assert all(v["status"] == "FAIL_IMPLEMENTATION" for v in result["volumes"])
        print("crashed job:", result["status"])
    gate_tests()
    print("ALL SYNTHETIC TESTS PASSED")
    return 0


# ---------------------------------------------------------------------------
# One fabricated deviation per gate; each must fire the intended gate.


def refab_forward(row, ladder, n, rng, mode, restricted):
    values = analyze.RATIO[mode]
    count = row["count"]
    low, high = analyze.RATIO_BOUNDS[mode]
    q = ladder["q"][n]
    n_ind = count if q >= 1 else sum(1 for _ in range(count) if rng.random() < q)
    counts = Counter(rng.choices(range(5), weights=ladder["p"][n], k=n_ind)) if n_ind else Counter()
    hist = [counts.get(f, 0) for f in range(5)]
    naive = math.fsum(hist[f] * values[f] for f in range(5))
    naive2 = math.fsum(hist[f] * values[f] ** 2 for f in range(5))
    cond = min(high, max(0.0 if restricted else low, ladder["r"][n] * ladder["qp"][n] + 0.0125 * rng.gauss(0, 1)))
    row.update(sumFn=naive, sumFn2=naive2, sumFi=cond * count, sumFi2=(cond * count) ** 2 / count + count * 0.05 ** 2)
    if restricted:
        pf = min(1.0, max(0.0, q + 0.0125 * rng.gauss(0, 1)))
        row.update(sumPFi=pf * count, sumPFi2=(pf * count) ** 2 / count + count * 0.05 ** 2)
    for f in range(5):
        row[f"hF{f}"] = hist[f]


def refab_reverse(row, ladder, n, rng, mode, restricted, qp_scale=1.0):
    values = analyze.RATIO[mode]
    count = row["count"]
    low, high = analyze.RATIO_BOUNDS[mode]
    qp = min(1.0, ladder["qp"][n] * qp_scale)
    n_ind = count if qp >= 1 else sum(1 for _ in range(count) if rng.random() < qp)
    total = law_mean(mode, ladder["p"][n])
    probs = [0.0] * 5
    vals = [0.0] * 5
    for f in range(5):
        probs[(f + mode) % 5] = ladder["p"][n][f] * values[f] / total
        vals[(f + mode) % 5] = 1.0 / values[f]
    counts = Counter(rng.choices(range(5), weights=probs, k=n_ind)) if n_ind else Counter()
    hist = [counts.get(f, 0) for f in range(5)]
    naive = math.fsum(hist[f] * vals[f] for f in range(5))
    naive2 = math.fsum(hist[f] * vals[f] ** 2 for f in range(5))
    cond = min(high, max(0.0 if restricted else low, ladder["q"][n] / ladder["r"][n] + 0.0125 * rng.gauss(0, 1)))
    row.update(sumBn=naive, sumBn2=naive2, sumBi=cond * count, sumBi2=(cond * count) ** 2 / count + count * 0.05 ** 2)
    for f in range(5):
        row[f"hB{f}"] = hist[f]


def set_y(row, mean, spread=0.5):
    count = row["count"]
    row["sumY"] = count * mean
    row["sumY2"] = row["sumY"] ** 2 / count + count * spread ** 2


def shifted_ladder(ladder, mode, factor, restricted):
    """The same ladder with every step ratio multiplied by `factor` (clipped below 1)."""
    out = {"p": [], "r": [], "q": list(ladder["q"]), "qp": list(ladder["qp"])}
    for n, r in enumerate(ladder["r"]):
        if r is None:
            out["p"].append(None)
            out["r"].append(None)
            continue
        target = min(0.97, r * factor)
        if restricted:
            p = two_point(mode, target * ladder["qp"][n] / ladder["q"][n])
            out["p"].append(p)
            out["r"].append(law_mean(mode, p) * ladder["q"][n] / ladder["qp"][n])
        else:
            p = two_point(mode, target)
            out["p"].append(p)
            out["r"].append(law_mean(mode, p))
    return out


def gate_tests():
    seam = 16
    base = {k: make_truth(4, k, random.Random(1)) for k in (1, 2)}
    rng = random.Random(99)

    def with_ladder(truth, kind, ladder, y=None):
        copy = dict(truth)
        copy["ladders"] = dict(truth["ladders"])
        copy["ladders"][kind] = ladder
        if y is not None:
            copy["Y"] = dict(truth["Y"])
            copy["Y"].update(y)
        return copy

    def run_case(name, expect, **kw):
        truth_for = kw.pop("truth_for", None)
        expect_errors = kw.pop("expect_errors", False)
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp) / "d"
            d.mkdir()
            build(d, (4,), random.Random(kw.pop("seed", 2)),
                  truth_for=lambda L, k, kind, c, t: (truth_for(L, k, kind, c, base[k]) if truth_for else base[k]), **kw)
            result = analyze.read_execution(d)
            json.dumps(result, sort_keys=True, allow_nan=False)
            if expect_errors:
                return result
            assert result["execution_errors"] == [], (name, result["execution_errors"])
            expect(result)
            print(f"gate case ok: {name}")
            return result

    def hooks_for(kind, chains, hook):
        return {analyze.stem_of(4, k, kind, c): hook for k in (1, 2) for c in chains}

    # U G3: chain 3 samples a different ladder.
    alt_u = {k: shifted_ladder(base[k]["ladders"][U], k, 1.1, False) for k in (1, 2)}

    def expect_u_g3(r):
        for m in modes_of(r).values():
            assert "chain_3:log_R_disagreement" in m["U"]["diagnostic_failures"], m["U"]["diagnostic_failures"]
            assert m["U"]["status"] == "INCONCLUSIVE_EQUILIBRATION"
            assert m["cross_check_G11"]["pass"] is None
            assert m["status"] == analyze.GATES_PASSED
    run_case("U G3 chain 3 different truth", expect_u_g3,
             truth_for=lambda L, k, kind, c, t: with_ladder(t, U, alt_u[k]) if (kind == U and c == 3) else t)

    # G11: the whole U ladder shifted -> exact cross-check fails -> FAIL_CONSISTENCY.
    def expect_g11(r):
        for m in modes_of(r).values():
            assert m["U"]["status"] == analyze.GATES_PASSED, m["U"]["diagnostic_failures"]
            assert "G11:U_route_disagrees_with_class_sum_log_R" in m["consistency_failures"], m["consistency_failures"]
            assert m["status"] == "FAIL_CONSISTENCY"
    run_case("G11 U ladder shifted", expect_g11,
             truth_for=lambda L, k, kind, c, t: with_ladder(t, U, alt_u[k]) if kind == U else t)

    # U G4: up rows from a different ladder.
    def hook_up(k):
        def h(row):
            if row["phase"] != "up":
                return
            n = row["n"]
            if n < seam:
                refab_forward(row, alt_u[k], n, rng, k, False)
            if n > 0:
                refab_reverse(row, alt_u[k], n - 1, rng, k, False)
        return h

    def expect_u_g4(r):
        for m in modes_of(r).values():
            assert "pooled:direction_disagreement" in m["U"]["diagnostic_failures"], m["U"]["diagnostic_failures"]
    run_case("U G4 up rows from a different truth", expect_u_g4,
             hooks={analyze.stem_of(4, k, U, c): hook_up(k) for k in (1, 2) for c in range(5)})

    # U G2: reverse rows from a different ladder -> pairing deficit.
    def hook_g2(k):
        def h(row):
            if row["n"] > 0:
                refab_reverse(row, alt_u[k], row["n"] - 1, rng, k, False)
        return h

    def expect_u_g2(r):
        for m in modes_of(r).values():
            assert "pooled:forward_reverse_deficit" in m["U"]["diagnostic_failures"], m["U"]["diagnostic_failures"]
    run_case("U G2 reverse from a different truth", expect_u_g2,
             hooks={analyze.stem_of(4, k, U, c): hook_g2(k) for k in (1, 2) for c in range(5)})

    # Restricted G2: reverse rows from a different restricted ladder -> F/PB and PF/Bw disagree
    # while naive and conditional forms stay mutually consistent.
    alt_cm = {k: shifted_ladder(base[k]["ladders"][CM], k, 1.1, True) for k in (1, 2)}

    def hook_rg2(k):
        def h(row):
            if row["n"] > 1:
                refab_reverse(row, alt_cm[k], row["n"] - 1, rng, k, True)
        return h

    def expect_rg2(r):
        for m in modes_of(r).values():
            assert "classMinus:pairing_deficit" in m["classMinus"]["diagnostic_failures"], m["classMinus"]["diagnostic_failures"]
            assert m["classMinus"]["consistency_failures"] == [], m["classMinus"]["consistency_failures"]
            # A wrong l_- moves the class sum away from the (correct) U ladder by P_- log 1.1 per
            # step; whether G11 also fires depends on the fabricated class weight.
            assert set(m["consistency_failures"]) <= {"G11:U_route_disagrees_with_class_sum_log_R"}, m["consistency_failures"]
            assert m["status"] in ("INCONCLUSIVE_EQUILIBRATION", "FAIL_CONSISTENCY"), m["status"]
    run_case("restricted G2 reverse rows from another ladder", expect_rg2, hooks=hooks_for(CM, (0, 1, 2), hook_rg2(1)) | {
        analyze.stem_of(4, 2, CM, c): hook_rg2(2) for c in range(3)})

    # G5: second half of U chain 2's twisted dwell shifted.
    def hook_g5(row):
        if row["n"] == seam and row["phase"] == "dwell" and row["block"] >= analyze.DWELL_BLOCKS // 2:
            set_y(row, 0.3)

    def expect_g5(r):
        for m in modes_of(r).values():
            assert "chain_2:twisted_dwell_half_disagreement" in m["U"]["diagnostic_failures"]
    run_case("U G5 chain 2 dwell halves differ", expect_g5, hooks=hooks_for(U, (2,), hook_g5))

    # Restricted G5 on the plateau chain.
    def expect_rg5(r):
        for m in modes_of(r).values():
            assert "class0_chain_2:twisted_dwell_half_disagreement" in m["class0"]["diagnostic_failures"], m["class0"]["diagnostic_failures"]
            assert m["status"] == "INCONCLUSIVE_EQUILIBRATION"
    run_case("restricted G5 chain 2 halves differ", expect_rg5, hooks=hooks_for(C0, (2,), hook_g5))

    # G6: conditional F biased by 3 percent (U) -> FAIL_CONSISTENCY.
    def hook_g6(row):
        if row["n"] < seam:
            row["sumFi"] *= 1.03
            row["sumFi2"] *= 1.03 ** 2

    def expect_g6(r):
        for m in modes_of(r).values():
            assert "pooled:naive_conditional_F_disagreement" in m["U"]["consistency_failures"]
            assert m["status"] == "FAIL_CONSISTENCY"
        assert r["volumes"][0]["status"] == "FAIL_CONSISTENCY"
    run_case("U G6 conditional F +3 percent", expect_g6, hooks=hooks_for(U, range(5), hook_g6))

    # Restricted G6 on PF and on Bw.
    def hook_g6_pf(row):
        if row["n"] < seam:
            row["sumPFi"] *= 0.97
            row["sumPFi2"] *= 0.97 ** 2

    def expect_g6_pf(r):
        for m in modes_of(r).values():
            assert "class0:naive_conditional_PF_disagreement" in m["class0"]["consistency_failures"], m["class0"]["consistency_failures"]
            assert m["status"] == "FAIL_CONSISTENCY"
    run_case("restricted G6 conditional PF -3 percent", expect_g6_pf, hooks=hooks_for(C0, (0, 1), hook_g6_pf))

    def hook_g6_bw(row):
        if row["n"] > 1:
            row["sumBi"] *= 1.03
            row["sumBi2"] *= 1.03 ** 2

    def expect_g6_bw(r):
        for m in modes_of(r).values():
            assert "classMinus:naive_conditional_Bw_disagreement" in m["classMinus"]["consistency_failures"]
    run_case("restricted G6 conditional Bw +3 percent", expect_g6_bw, hooks=hooks_for(CM, (0, 1, 2), hook_g6_bw))

    # G7: strongly autocorrelated Y blocks in the U twisted dwell.
    state = {}

    def hook_g7(row):
        if row["n"] != seam:
            return
        key = (row["kind"], row["chain"], row["segment"])
        previous = state.get(key, 0.0)
        value = 0.97 * previous + math.sqrt(1 - 0.97 ** 2) * 0.05 * rng.gauss(0, 1)
        state[key] = value
        set_y(row, 0.1 + value)

    def expect_g7(r):
        for m in modes_of(r).values():
            assert "pooled:mean_Y_twisted_coarsening_instability" in m["U"]["diagnostic_failures"], (
                m["U"]["diagnostic_failures"], m["U"]["coarsening_se_ratios"])
    run_case("U G7 autocorrelated Y blocks", expect_g7, hooks=hooks_for(U, range(5), hook_g7))

    def expect_rg7(r):
        for m in modes_of(r).values():
            assert "classMinus_pooled:mean_Y_twisted_coarsening_instability" in m["classMinus"]["diagnostic_failures"], (
                m["classMinus"]["diagnostic_failures"], m["classMinus"]["coarsening_se_ratios"])
    run_case("restricted G7 autocorrelated Y blocks", expect_rg7, hooks=hooks_for(CM, (0, 1, 2), hook_g7))

    # P calibration: both P chains biased at n=0 -> INCONCLUSIVE; U chains 0,1 biased -> U route only.
    def hook_y0(row):
        if row["n"] == 0:
            set_y(row, 0.3)

    def expect_p_cal(r):
        for m in modes_of(r).values():
            assert "P_pooled:untwisted_mean_Y_nonzero" in m["P"]["calibration_failures"]
            assert m["status"] == "INCONCLUSIVE_EQUILIBRATION"
    run_case("P calibration mean Y0 nonzero", expect_p_cal, hooks=hooks_for(P, range(4), hook_y0))

    def expect_u_cal(r):
        for m in modes_of(r).values():
            assert "chains_0_1:untwisted_mean_Y_nonzero" in m["U"]["calibration_failures"]
            assert m["U"]["status"] == "INCONCLUSIVE_EQUILIBRATION"
            assert m["status"] == analyze.GATES_PASSED, m["diagnostic_failures"]
    run_case("U calibration mean Y0 nonzero (U route only)", expect_u_cal, hooks=hooks_for(U, (0, 1), hook_y0))

    def hook_y2(row):
        if row["n"] == 0:
            row["sumY2"] = row["count"] * 1.5

    def expect_p_bound(r):
        for m in modes_of(r).values():
            assert "P_pooled:untwisted_mean_Y_squared_above_one" in m["P"]["calibration_failures"]
    run_case("P bound Y0 squared above one", expect_p_bound, hooks=hooks_for(P, range(4), hook_y2))

    # G9' partial: U chain 4 in class minus for 40 percent of its dwell -> SECTOR_FROZEN (U only).
    def hook_g9(row):
        if row["n"] == seam and row["phase"] == "dwell" and row["block"] < int(0.4 * analyze.DWELL_BLOCKS):
            row["sec0"], row["secMinus"] = 0, row["count"] * seam
            row["pure0"], row["pureMinus"] = 0, row["count"]
            row["classMinus"], row["sumW"], row["minW"], row["maxW"] = row["count"], -seam * row["count"], -seam, -seam

    def expect_g9(r):
        for m in modes_of(r).values():
            assert any(f.startswith("chain_4:") for f in m["U"]["sector_failures"]), m["U"]["sector_failures"]
            assert m["U"]["status"] == analyze.SECTOR_FROZEN, m["U"]["status"]
            assert m["status"] == analyze.GATES_PASSED
    run_case("G9' U chain 4 partially frozen", expect_g9, hooks=hooks_for(U, (4,), hook_g9))

    # G9' on the w=-1 slice fraction alone (class unchanged): chain 3 with a third of its slices at w=-1.
    def hook_g9_slices(row):
        if row["n"] == seam:
            per_sweep = seam // 3
            third = row["count"] * per_sweep
            row["sec0"], row["secMinus"] = row["count"] * seam - third, third
            row["pure0"] = 0
            row["sumW"], row["minW"], row["maxW"] = -third, -per_sweep, -per_sweep

    def expect_g9_slices(r):
        for m in modes_of(r).values():
            assert "chain_3:wMinus_slice_occupancy_disagreement" in m["U"]["sector_failures"], m["U"]["sector_failures"]
            assert "chain_3:class_minus_occupancy_disagreement" not in m["U"]["sector_failures"]
    run_case("G9' slice fraction alone", expect_g9_slices, hooks=hooks_for(U, (3,), hook_g9_slices))

    # Restricted G3: hot chain of C0 samples a different ladder.
    alt_c0 = {k: shifted_ladder(base[k]["ladders"][C0], k, 1.1, True) for k in (1, 2)}

    def expect_rg3(r):
        for m in modes_of(r).values():
            assert "class0_chain_1:log_l_disagreement" in m["class0"]["diagnostic_failures"], m["class0"]["diagnostic_failures"]
            assert set(m["consistency_failures"]) <= {"G11:U_route_disagrees_with_class_sum_log_R"}, m["consistency_failures"]
            assert m["status"] in ("INCONCLUSIVE_EQUILIBRATION", "FAIL_CONSISTENCY"), m["status"]
    run_case("restricted G3 hot chain different ladder", expect_rg3,
             truth_for=lambda L, k, kind, c, t: with_ladder(t, C0, alt_c0[k]) if (kind == C0 and c == 1) else t)

    # Plateau chain disagreement in mean Y (chain 2 of CM).
    def hook_plateau(row):
        if row["n"] == seam:
            set_y(row, 0.25)

    def expect_plateau(r):
        for m in modes_of(r).values():
            assert "classMinus_chain_2:mean_Y_disagreement" in m["classMinus"]["diagnostic_failures"], m["classMinus"]["diagnostic_failures"]
            assert m["status"] == "INCONCLUSIVE_EQUILIBRATION"
    run_case("plateau chain mean Y disagreement", expect_plateau, hooks=hooks_for(CM, (2,), hook_plateau))

    # Plateau chain disagreement in the all-slice w=-1 count (zero within-chain variance, nonzero difference).
    def hook_plateau_w(row):
        if row["n"] == seam:
            row["secMinus"], row["sec0"] = row["count"] * (seam - 2), row["count"] * 2
            row["sumW"], row["minW"], row["maxW"] = -(seam - 2) * row["count"], -(seam - 2), -(seam - 2)

    def expect_plateau_w(r):
        for m in modes_of(r).values():
            assert "classMinus_chain_2:all_slice_wMinus_disagreement" in m["classMinus"]["diagnostic_failures"], m["classMinus"]["diagnostic_failures"]
            assert "classMinus_chain_2:mean_W_disagreement" in m["classMinus"]["diagnostic_failures"]
    run_case("plateau chain W disagreement", expect_plateau_w, hooks=hooks_for(CM, (2,), hook_plateau_w))

    # P chain disagreement in pi_1(-).
    def hook_pi(row):
        if row["n"] == 1:
            c = int(0.8 * row["count"])
            row["classMinus"], row["sec0"], row["secMinus"] = c, row["count"] - c, c
            row["pure0"], row["pureMinus"] = row["count"] - c, c
            row["sumW"], row["minW"], row["maxW"] = -c, -1, 0

    def expect_pi(r):
        for m in modes_of(r).values():
            assert "P_chain_1:class_minus_disagreement" in m["P"]["diagnostic_failures"], m["P"]["diagnostic_failures"]
            assert m["status"] == "INCONCLUSIVE_EQUILIBRATION"
    run_case("P chains disagree in pi_1", expect_pi, hooks=hooks_for(P, (1,), hook_pi))

    # P halves: second half of chain 0's twist-1 dwell in another class fraction.
    def hook_pi_half(row):
        if row["n"] == 1 and row["block"] >= analyze.DWELL_LONG_BLOCKS // 2:
            hook_pi(row)

    def expect_pi_half(r):
        for m in modes_of(r).values():
            assert "P_chain_0:class_minus_half_disagreement" in m["P"]["diagnostic_failures"], m["P"]["diagnostic_failures"]
    run_case("P dwell halves differ in pi_1", expect_pi_half, hooks=hooks_for(P, (0,), hook_pi_half))

    # G11 sub-check on pi_1: U chains 0 and 1 at twist 1 in another class fraction, U otherwise fine.
    def hook_u_pi(row):
        if row["n"] == 1 and row["phase"] == "up":
            hook_pi(row)

    def expect_u_pi(r):
        for m in modes_of(r).values():
            assert "G11:U_route_disagrees_with_class_sum_pi1_minus" in m["consistency_failures"], m["consistency_failures"]
    run_case("G11 pi_1 U against P", expect_u_pi, hooks=hooks_for(U, (0, 1), hook_u_pi))

    # Zero-mean step: the class-minus forward indicator never fires at n = 3 -> INCONCLUSIVE, not FAIL_IMPLEMENTATION.
    def hook_zero(row):
        if row["n"] == 3:
            for key in ("sumFn", "sumFn2", "sumFi", "sumFi2", "sumPFi", "sumPFi2"):
                row[key] = 0.0
            for f in range(5):
                row[f"hF{f}"] = 0

    def expect_zero(r):
        assert r["execution_errors"] == []
        for m in modes_of(r).values():
            assert m["classMinus"]["log_l"] is None
            assert any(f.startswith("classMinus:zero_estimator_mean") for f in m["classMinus"]["diagnostic_failures"])
            assert m["status"] == "INCONCLUSIVE_EQUILIBRATION" and m["log_R"] is None
    run_case("zero indicator step routes to INCONCLUSIVE", expect_zero, hooks=hooks_for(CM, (0, 1), hook_zero))

    # One chain only with a zero indicator step: the pooled ladder exists, G3 cannot be read.
    def expect_one_zero(r):
        assert r["execution_errors"] == []
        for m in modes_of(r).values():
            assert m["classMinus"]["log_l"] is not None
            assert "classMinus_chain_0:zero_estimator_mean_in_subset" in m["classMinus"]["diagnostic_failures"], m["classMinus"]["diagnostic_failures"]
            assert m["classMinus"]["log_l_by_chain"]["0"] is None if "0" in m["classMinus"]["log_l_by_chain"] else m["classMinus"]["log_l_by_chain"][0] is None
            assert m["status"] in ("INCONCLUSIVE_EQUILIBRATION", "FAIL_CONSISTENCY")
    run_case("one chain zero indicator step is not a custody failure", expect_one_zero, hooks=hooks_for(CM, (0,), hook_zero))

    # Row checks that must be custody failures.
    def hook_bad_class(row):
        if row["n"] == 5 and row["block"] == 0:
            row["minW"] = -3
            row["sumW"] = row["count"] * -3 + 100

    def hook_bad_forced(row):
        if row["segment"] == 2:
            row["forced"] = 1

    for name, kind, chains, hook, needle in (
            ("class-0 block reaching class minus", C0, (0,), hook_bad_class, "class-0 block"),
            ("forced flag on an unconstrained chain", U, (0,), hook_bad_forced, "forced flag")):
        result = run_case(name, None, hooks=hooks_for(kind, chains, hook), expect_errors=True)
        assert result["status"] == "FAIL_IMPLEMENTATION" and any(needle in e for e in result["execution_errors"]), (
            name, result["execution_errors"])
        print(f"gate case ok: {name}")

    # G10: R1 = 1 exactly with R2 small violates positivity -> FAIL_CONSISTENCY.
    def truth_g10(L, k, kind, c, t):
        values = analyze.RATIO[k]
        i_one = min(range(5), key=lambda f: abs(values[f] - 1.0))
        i_low = values.index(min(values))
        copy = dict(t)
        copy["ladders"] = {}
        mixture = [0.0] * 5
        if k == 1:
            mixture[i_one] = 1.0
        else:
            mixture[i_low], mixture[i_one] = 0.7, 0.3
        target = law_mean(k, mixture)
        for kd in (U, C0, CM):
            lad = {"p": [], "r": [], "q": list(t["ladders"][kd]["q"]), "qp": list(t["ladders"][kd]["qp"])}
            for n in range(seam):
                if kd != U and n == 0:
                    lad["p"].append(None)
                    lad["r"].append(None)
                    continue
                if kd == U:
                    lad["p"].append(mixture)
                    lad["r"].append(target)
                else:
                    # The same step ratio inside both classes keeps the class sum equal to the U ladder.
                    p = two_point(k, target * lad["qp"][n] / lad["q"][n])
                    lad["p"].append(p)
                    lad["r"].append(law_mean(k, p) * lad["q"][n] / lad["qp"][n])
            copy["ladders"][kd] = lad
        return copy

    def expect_g10(r):
        assert r["volumes"][0]["cross_mode_positivity"]["R1_le_0.618_plus_0.382_R2"] is False
        for m in modes_of(r).values():
            assert "pooled:cross_mode_positivity_violated" in m["consistency_failures"]
    run_case("G10 positivity violated", expect_g10, truth_for=truth_g10)

    # C3: control mean Y not antisymmetric.
    def hook_c3(row):
        if row["n"] == seam:
            set_y(row, 0.4)

    def expect_c3(r):
        four = [c for c in r["controls"] if c["L"] == 4]
        assert all("control:mean_Y_reversal_antisymmetry" in c["control_failures"] for c in four), four
        assert r["volumes"][0]["status"] == "FAIL_CONSISTENCY"
    run_case("C3 control antisymmetry violated", expect_c3, control_hook=hook_c3)

    # Degenerate: identical Y blocks at the U twisted dwell.
    def hook_degenerate(row):
        if row["n"] == seam:
            row["sumY"] = row["count"] * 0.25
            row["sumY2"] = row["count"] * 0.0625

    def expect_degenerate(r):
        for m in modes_of(r).values():
            assert "pooled:mean_Y_twisted_degenerate_se" in m["U"]["diagnostic_failures"], m["U"]["diagnostic_failures"]
    run_case("degenerate Y variance", expect_degenerate, hooks=hooks_for(U, range(5), hook_degenerate))

    # Negligible contrast: every step ratio at the smallest value in every ladder.
    def truth_small(L, k, kind, c, t):
        values = analyze.RATIO[k]
        i_low = values.index(min(values))
        p = [0.0] * 5
        p[i_low] = 1.0
        copy = dict(t)
        copy["ladders"] = {}
        for kd in (U, C0, CM):
            q, qp = t["ladders"][kd]["q"], t["ladders"][kd]["qp"]
            lad = {"p": [], "r": [], "q": q, "qp": qp}
            for n in range(seam):
                if kd != U and n == 0:
                    lad["p"].append(None)
                    lad["r"].append(None)
                else:
                    lad["p"].append(p)
                    lad["r"].append(values[i_low] * (1.0 if kd == U else q[n] / qp[n]))
            copy["ladders"][kd] = lad
        return copy

    def expect_small(r):
        for m in modes_of(r).values():
            assert m["contrast_negligible"] is True, m["R_interval_noninferential"]
    run_case("negligible contrast flag", expect_small, truth_for=truth_small)

    # Timed-out control caps the volume and the overall label at INCOMPLETE.
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp) / "d"
        d.mkdir()
        build(d, (4,), random.Random(5))
        records = json.loads((d / "execution.json").read_text())
        for item in records:
            if item["stem"] == "L4_k1_control_c0":
                item["exit_code"] = 124
        (d / "execution.json").write_text(json.dumps(records, indent=2) + "\n")
        result = analyze.read_execution(d)
        assert result["volumes"][0]["status"] == "INCOMPLETE" and result["volumes"][0].get("control_incomplete")
        print("gate case ok: timed-out control caps the volume")


if __name__ == "__main__":
    sys.exit(main())
