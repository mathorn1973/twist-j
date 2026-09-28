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
import sys
import tempfile
from collections import Counter
from pathlib import Path

import analyze

HEADER = ("L\tk\tchain\tsegment\tn\tphase\tblock\tcount\tsumFn\tsumFn2\tsumFi\tsumFi2"
          "\tsumBn\tsumBn2\tsumBi\tsumBi2\tsumY\tsumY2\tsumS\tsumS2"
          "\thF0\thF1\thF2\thF3\thF4\thB0\thB1\thB2\thB3\thB4"
          "\tsec0\tsecMinus\tsecPlus\tsecOther\tsecUntwisted\tpure0\tpureMinus\tpurePlus\tflips")


def make_truth(size, mode, rng, control=False):
    """Fabricated per-step flux mixtures with their exact naive means.

    Two-point mixtures between the smallest ratio value and the value 1 keep
    every fabricated step ratio inside (0, 1], as the exact ratios are bounded
    by one only in the aggregate; this is a fixture convenience, not physics.
    """
    values = analyze.RATIO[mode]
    seam = size * size
    i_low = values.index(min(values))
    i_one = min(range(5), key=lambda f: abs(values[f] - 1.0))
    low, one = values[i_low], values[i_one]

    def two_point(target):
        t = min(max((target - low) / (one - low), 0.0), 1.0)
        p = [0.0] * 5
        p[i_low] = 1.0 - t
        p[i_one] = t
        return p

    probs = [two_point(math.exp(rng.uniform(-0.35, -0.02))) for _ in range(seam)]
    if control:
        # Exact antisymmetry log r_n = -log r_{S-1-n} needs partners above one;
        # mix between the value 1 and the largest value for the second half.
        i_high = values.index(max(values))
        high = values[i_high]
        for n in range(seam // 2, seam):
            partner = seam - 1 - n
            target = 1.0 / math.fsum(p * v for p, v in zip(probs[partner], values))
            t = min(max((target - one) / (high - one), 0.0), 1.0)
            p = [0.0] * 5
            p[i_one] = 1.0 - t
            p[i_high] = t
            probs[n] = p
    r = [math.fsum(p * v for p, v in zip(pr, values)) for pr in probs]
    return {"p": probs, "r": r, "Y": rng.uniform(-0.5, 0.5)}


COLUMNS = HEADER.split("\t")


def fabricate_run(directory, size, mode, base, chain, rng, truth, corrupt=None, sector="agree", hook=None):
    seam = size * size
    values = analyze.RATIO[mode]
    low, high = analyze.RATIO_BOUNDS[mode]
    lines = [
        "# format\ttwist_snake_blocks_v1",
        "# status\tNON-CANONICAL floating-point engineering diagnostic",
        f"# L\t{size}", f"# k\t{mode}", f"# chain\t{chain}", f"# base\t{base}",
        f"# seed\t{202609280000 + 1000 * size + 100 * mode + 10 * base + chain}",
        f"# seam_size\t{seam}", f"# start_twist\t{analyze.start_twist(size, chain)}",
        f"# chain_initial\t{analyze.INITIAL[chain]}",
        f"# warmup_sweeps\t{analyze.WARMUP_SWEEPS}", f"# dwell_sweeps\t{analyze.DWELL_SWEEPS}",
        f"# visit_sweeps\t{analyze.VISIT_SWEEPS}",
        f"# equilibration_sweeps\t{analyze.EQUILIBRATION_SWEEPS}",
        f"# block_length\t{analyze.BLOCK_LENGTH}", f"# segments\t{2 * seam}",
        "# seam_order\tx2_fastest_then_x3",
        "# action_density\tminus_sum_logW_divided_by_6L4",
        "# sampling\tevery_production_sweep_after_full_heatbath_sweep",
        HEADER,
    ]

    def histogram(probs, count):
        counts = Counter(rng.choices(range(5), weights=probs, k=count))
        return [counts.get(f, 0) for f in range(5)]

    def fabricate(hist, vals, count):
        naive = math.fsum(hist[f] * vals[f] for f in range(5))
        naive2 = math.fsum(hist[f] * vals[f] ** 2 for f in range(5))
        per = naive / count
        # Conditional values: the naive mean plus small zero-mean noise, within bounds.
        noise = 0.05 * rng.gauss(0, 1) / math.sqrt(count) * math.sqrt(count)
        cond_mean = min(high, max(low, per + 0.05 * rng.gauss(0, 1) / 4))
        cond_sum = cond_mean * count
        cond_sum2 = cond_sum ** 2 / count + count * 0.05 ** 2 * (1.0 + abs(noise))
        return (naive, naive2), (cond_sum, cond_sum2)

    def forward(n, count):
        hist = histogram(truth["p"][n], count)
        return fabricate(hist, values, count) + (hist,)

    def reverse(n, count):
        probs = [0.0] * 5
        vals = [0.0] * 5
        for f in range(5):
            probs[(f + mode) % 5] = truth["p"][n][f] * values[f] / truth["r"][n]
            vals[(f + mode) % 5] = 1.0 / values[f]
        hist = histogram(probs, count)
        return fabricate(hist, vals, count) + (hist,)

    y_end = truth["Y"] if base == 0 else -truth["Y"]
    for segment, (n, phase, blocks) in enumerate(analyze.expected_segments(size, chain)):
        for block in range(blocks):
            count = analyze.BLOCK_LENGTH
            f, fi, hf = (((0.0, 0.0), (0.0, 0.0), [0] * 5) if n == seam else forward(n, count))
            b, bi, hb = (((0.0, 0.0), (0.0, 0.0), [0] * 5) if n == 0 else reverse(n - 1, count))
            if base == 0:
                y_mean = truth["Y"] if n == seam else 0.0
            else:
                y_mean = truth["Y"] if n == 0 else (y_end if n == seam else 0.0)
            sum_y = count * y_mean + math.sqrt(count) * 0.5 * rng.gauss(0, 1)
            sum_y2 = sum_y ** 2 / count + count * 0.25 * (1.0 + 0.1 * abs(rng.gauss(0, 1)))
            sum_s = count * 1.16 + math.sqrt(count) * 0.01 * rng.gauss(0, 1)
            sum_s2 = sum_s ** 2 / count + count * 1e-4
            # Sector bookkeeping: agree -> every twisted slice w=0; frozen chain 4 -> w=-1.
            if sector == "frozen" and chain == 4:
                sec = [0, count * n, 0, 0, 0]
                pure = [0, count if n > 0 else 0, 0]
            else:
                sec = [count * n, 0, 0, 0, 0]
                pure = [count if n > 0 else 0, 0, 0]
            flips = 0
            values_list = [size, mode, chain, segment, n, phase, block, count,
                           f[0], f[1], fi[0], fi[1], b[0], b[1], bi[0], bi[1],
                           sum_y, sum_y2, sum_s, sum_s2] + hf + hb + sec + pure + [flips]
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
    lines.append(f"# final_twist\t{1 if chain < 2 else seam - 1}")
    lines.append("# completion\tPASS")
    stem = analyze.stem_of(size, mode, base, chain)
    (directory / f"{stem}.tsv").write_text("\n".join(lines) + "\n")
    (directory / f"{stem}.stderr").write_bytes(b"")
    return stem


def record(directory, stem, code=0):
    out = (directory / f"{stem}.tsv").read_bytes()
    err = (directory / f"{stem}.stderr").read_bytes()
    return {"stem": stem, "exit_code": code, "seconds": 1.0,
            "stdout_bytes": len(out), "stderr_bytes": len(err),
            "stdout_sha256": hashlib.sha256(out).hexdigest(),
            "stderr_sha256": hashlib.sha256(err).hexdigest()}


def build(directory, sizes, rng, corrupt=None, drop=None, audit=True, sector="agree", control_bias=0.0,
          hooks=None, truth_for=None, control_hook=None):
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
            for chain in analyze.MAIN_CHAINS:
                if drop == (size, mode, 0, chain):
                    continue
                chain_truth = truth_for(size, mode, chain, truth) if truth_for else truth
                stem = analyze.stem_of(size, mode, 0, chain)
                fabricate_run(directory, size, mode, 0, chain, rng, chain_truth,
                              corrupt if (size, mode, chain) == (4, 1, 0) else None, sector,
                              hooks.get(stem))
                records.append(record(directory, stem))
            if size in analyze.CONTROL_L_VALUES:
                control_truth = make_truth(size, mode, rng, control=True)
                if control_bias:
                    control_truth["p"] = [[1.0 if f == 0 else 0.0 for f in range(5)]] * (size * size)
                    control_truth["r"] = [analyze.RATIO[mode][0]] * (size * size)
                for chain in analyze.CONTROL_CHAINS:
                    stem = fabricate_run(directory, size, mode, 2, chain, rng, control_truth,
                                         hook=control_hook)
                    records.append(record(directory, stem))
    (directory / "execution.json").write_text(json.dumps(records, indent=2) + "\n")
    return truths


def main():
    rng = random.Random(12345)
    with tempfile.TemporaryDirectory() as tmp:
        directory = Path(tmp) / "clean"
        directory.mkdir()
        truths = build(directory, analyze.L_VALUES, rng)
        result = analyze.read_execution(directory)
        assert result["execution_errors"] == [], result["execution_errors"]
        assert result["status"] not in ("FAIL_IMPLEMENTATION", "FAIL_CONSISTENCY"), result["status"]
        assert result["missing_runs"] == []
        assert all(c["status"] == "CONTROL_PASS" for c in result["controls"]), [
            (c["L"], c["k"], c["status"], c.get("control_failures")) for c in result["controls"]]
        for volume in result["volumes"]:
            for mode in volume["modes"]:
                truth = truths[(volume["L"], mode["k"])]
                expected = math.fsum(math.log(r) for r in truth["r"])
                assert abs(mode["log_R"] - expected) <= 6 * mode["log_R_se_report"] + 0.05, (
                    volume["L"], mode["k"], mode["log_R"], expected, mode["log_R_se_report"])
                assert abs(mode["log_R_bar"] - expected) <= 6 * mode["log_R_se_report"] + 0.1
                assert abs(mode["mean_Y_twisted"] - truth["Y"]) <= 6 * mode["mean_Y_twisted_se_report"] + 0.02
                assert len(mode["steps"]) == volume["L"] ** 2
                assert len(mode["chains"]) == 5
                assert mode["sector_failures"] == [], mode["sector_failures"]
                assert mode["status"] == analyze.GATES_PASSED, (mode["diagnostic_failures"], mode["consistency_failures"])
                assert mode["sector_conditional"]["chain_2_down_pass_pure_w0"] is True
            assert volume["cross_mode_positivity"] is not None
            assert volume["status"] in ("RESOLVED_SIGNED_CONTRAST", "UNRESOLVED")
            assert volume["D_empirical_engineering_interval"] is not None
        print("clean fixture:", result["status"], [(v["L"], v["status"]) for v in result["volumes"]])

        directory = Path(tmp) / "frozen"
        directory.mkdir()
        build(directory, (4,), random.Random(5), sector="frozen")
        result = analyze.read_execution(directory)
        assert result["execution_errors"] == [], result["execution_errors"]
        statuses = [m["status"] for m in result["volumes"][0]["modes"]]
        assert all(s in ("SECTOR_FROZEN", "INCONCLUSIVE_EQUILIBRATION") for s in statuses), statuses
        assert all(m["sector_failures"] for m in result["volumes"][0]["modes"])
        assert result["volumes"][0]["modes"][0]["sector_conditional"]["chain_4_down_pass_pure_wMinus"] is True
        print("frozen alternative sector:", result["status"], statuses)

        directory = Path(tmp) / "control_violation"
        directory.mkdir()
        build(directory, (4,), random.Random(6), control_bias=1.0)
        result = analyze.read_execution(directory)
        assert result["execution_errors"] == [], result["execution_errors"]
        assert all(c["status"] == "FAIL_CONSISTENCY" for c in result["controls"] if c["L"] == 4), [
            c["status"] for c in result["controls"]]
        assert result["volumes"][0]["status"] == "FAIL_CONSISTENCY", result["volumes"][0]["status"]
        assert all("control:exact_control_group_failed" in m["consistency_failures"]
                   for m in result["volumes"][0]["modes"])
        print("control violation:", result["status"])

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

        directory = Path(tmp) / "missing"
        directory.mkdir()
        build(directory, (4, 6), random.Random(8), drop=(6, 2, 0, 3))
        result = analyze.read_execution(directory)
        assert result["status"] == "INCOMPLETE", result["status"]
        assert [6, 2, 0, 3] in result["missing_runs"]
        six = result["volumes"][1]
        assert six["status"] == "INCOMPLETE"
        assert six["modes"][0]["status"] in (analyze.GATES_PASSED, "INCONCLUSIVE_EQUILIBRATION", "SECTOR_FROZEN")
        assert six["modes"][1]["status"] == "INCOMPLETE" and len(six["modes"][1]["available_chains"]) == 4
        assert all(c["status"] == "CONTROL_PASS" for c in result["controls"])
        print("missing run:", result["status"], [(v["L"], v["status"]) for v in result["volumes"]])

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
        path = directory / "L4_k2_c1.tsv"
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
            if item["stem"] == "L4_k1_c2":
                item["exit_code"] = 124
        (directory / "execution.json").write_text(json.dumps(records, indent=2) + "\n")
        result = analyze.read_execution(directory)
        assert result["status"] == "INCOMPLETE", result["status"]
        assert result["execution_errors"] == []
        assert result["unavailable_jobs"] == [{"stem": "L4_k1_c2", "exit_code": 124}]
        assert result["volumes"][0]["modes"][0]["status"] == "INCOMPLETE"
        print("timed-out job:", result["status"])

        directory = Path(tmp) / "crash"
        directory.mkdir()
        build(directory, (4,), random.Random(12))
        records = json.loads((directory / "execution.json").read_text())
        for item in records:
            if item["stem"] == "L4_k2_c0":
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
# One fabricated deviation per gate; each must fire exactly the intended gate.


def refab_forward(row, probs, rng, mode):
    values = analyze.RATIO[mode]
    count = row["count"]
    low, high = analyze.RATIO_BOUNDS[mode]
    counts = Counter(rng.choices(range(5), weights=probs, k=count))
    hist = [counts.get(f, 0) for f in range(5)]
    naive = math.fsum(hist[f] * values[f] for f in range(5))
    naive2 = math.fsum(hist[f] * values[f] ** 2 for f in range(5))
    cond = min(high, max(low, naive / count + 0.0125 * rng.gauss(0, 1)))
    row.update(sumFn=naive, sumFn2=naive2, sumFi=cond * count, sumFi2=(cond * count) ** 2 / count + count * 0.05 ** 2)
    for f in range(5):
        row[f"hF{f}"] = hist[f]


def refab_reverse(row, probs_fwd, r, rng, mode):
    values = analyze.RATIO[mode]
    count = row["count"]
    low, high = analyze.RATIO_BOUNDS[mode]
    probs = [0.0] * 5
    vals = [0.0] * 5
    for f in range(5):
        probs[(f + mode) % 5] = probs_fwd[f] * values[f] / r
        vals[(f + mode) % 5] = 1.0 / values[f]
    counts = Counter(rng.choices(range(5), weights=probs, k=count))
    hist = [counts.get(f, 0) for f in range(5)]
    naive = math.fsum(hist[f] * vals[f] for f in range(5))
    naive2 = math.fsum(hist[f] * vals[f] ** 2 for f in range(5))
    cond = min(high, max(low, naive / count + 0.0125 * rng.gauss(0, 1)))
    row.update(sumBn=naive, sumBn2=naive2, sumBi=cond * count, sumBi2=(cond * count) ** 2 / count + count * 0.05 ** 2)
    for f in range(5):
        row[f"hB{f}"] = hist[f]


def set_y(row, mean, spread=0.5):
    count = row["count"]
    row["sumY"] = count * mean
    row["sumY2"] = row["sumY"] ** 2 / count + count * spread ** 2


def modes_of(result):
    return {m["k"]: m for m in result["volumes"][0]["modes"]}


def shifted_truth(truth, mode, factor):
    """The same ladder with every step ratio multiplied by `factor` (clipped below 1)."""
    values = analyze.RATIO[mode]
    i_low = values.index(min(values))
    i_one = min(range(5), key=lambda f: abs(values[f] - 1.0))
    low, one = values[i_low], values[i_one]
    probs = []
    for r in truth["r"]:
        target = min(0.97, r * factor)
        s = min(max((target - low) / (one - low), 0.0), 1.0)
        p = [0.0] * 5
        p[i_low], p[i_one] = 1.0 - s, s
        probs.append(p)
    return {"p": probs, "r": [math.fsum(pp * v for pp, v in zip(pr, values)) for pr in probs],
            "Y": truth["Y"]}


def gate_tests():
    seam = 16
    base = {k: make_truth(4, k, random.Random(1)) for k in (1, 2)}
    alt = {k: shifted_truth(base[k], k, 1.1) for k in (1, 2)}
    rng = random.Random(99)
    all_stems = [analyze.stem_of(4, k, 0, c) for k in (1, 2) for c in range(5)]

    def run_case(name, expect, **kw):
        truth_for = kw.pop("truth_for", None)
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp) / "d"
            d.mkdir()
            build(d, (4,), random.Random(kw.pop("seed", 1)),
                  truth_for=lambda L, k, c, t: (truth_for(L, k, c, base[k]) if truth_for else base[k]), **kw)
            result = analyze.read_execution(d)
            assert result["execution_errors"] == [], (name, result["execution_errors"])
            expect(result)
            print(f"gate case ok: {name}")
            return result

    def hooks_for(chains, hook):
        return {analyze.stem_of(4, k, 0, c): hook for k in (1, 2) for c in chains}

    # G3: chain 3 samples a different ladder.
    def expect_g3(r):
        for m in modes_of(r).values():
            assert "chain_3:log_R_disagreement" in m["diagnostic_failures"], m["diagnostic_failures"]
            assert m["status"] == "INCONCLUSIVE_EQUILIBRATION"
    run_case("G3 chain 3 different truth", expect_g3,
             truth_for=lambda L, k, c, t: alt[k] if c == 3 else t)

    # G4: up rows from a different ladder, refabricated consistently.
    def hook_up(k):
        def h(row):
            if row["phase"] != "up":
                return
            n = row["n"]
            if n < seam:
                refab_forward(row, alt[k]["p"][n], rng, k)
            if n > 0:
                refab_reverse(row, alt[k]["p"][n - 1], alt[k]["r"][n - 1], rng, k)
        return h
    def expect_g4(r):
        for m in modes_of(r).values():
            assert "pooled:direction_disagreement" in m["diagnostic_failures"], m["diagnostic_failures"]
    run_case("G4 up rows from a different truth", expect_g4,
             hooks={analyze.stem_of(4, k, 0, c): hook_up(k) for k in (1, 2) for c in range(5)})

    # G2: reverse rows from a different ladder -> forward/reverse deficit.
    def hook_g2(k):
        def h(row):
            n = row["n"]
            if n > 0:
                refab_reverse(row, alt[k]["p"][n - 1], alt[k]["r"][n - 1], rng, k)
        return h
    def expect_g2(r):
        for m in modes_of(r).values():
            assert "pooled:forward_reverse_deficit" in m["diagnostic_failures"], m["diagnostic_failures"]
    run_case("G2 reverse from a different truth", expect_g2,
             hooks={analyze.stem_of(4, k, 0, c): hook_g2(k) for k in (1, 2) for c in range(5)})

    # G5: second half of chain 2's twisted dwell shifted.
    def hook_g5(row):
        if row["n"] == seam and row["phase"] == "dwell" and row["block"] >= analyze.DWELL_BLOCKS // 2:
            set_y(row, 0.3)
    def expect_g5(r):
        for m in modes_of(r).values():
            assert "chain_2:twisted_dwell_half_disagreement" in m["diagnostic_failures"], m["diagnostic_failures"]
    run_case("G5 chain 2 dwell halves differ", expect_g5, hooks=hooks_for((2,), hook_g5))

    # G6: conditional forward biased by 3 percent -> FAIL_CONSISTENCY.
    def hook_g6(row):
        if row["n"] < seam:
            row["sumFi"] *= 1.03
            row["sumFi2"] *= 1.03 ** 2
    def expect_g6(r):
        for m in modes_of(r).values():
            assert "pooled:naive_conditional_forward_disagreement" in m["consistency_failures"]
            assert m["status"] == "FAIL_CONSISTENCY"
        assert r["volumes"][0]["status"] == "FAIL_CONSISTENCY"
    run_case("G6 conditional +3 percent", expect_g6, hooks=hooks_for(range(5), hook_g6))

    # G7: strongly autocorrelated Y blocks in the twisted dwell.
    state = {}
    def hook_g7(row):
        if row["n"] != seam:
            return
        key = (row["chain"], row["segment"])
        previous = state.get(key, 0.0)
        value = 0.97 * previous + math.sqrt(1 - 0.97 ** 2) * 0.05 * rng.gauss(0, 1)
        state[key] = value
        set_y(row, 0.1 + value)
    def expect_g7(r):
        for m in modes_of(r).values():
            assert "pooled:mean_Y_twisted_coarsening_instability" in m["diagnostic_failures"], (
                m["diagnostic_failures"], m["coarsening_se_ratios"])
    run_case("G7 autocorrelated Y blocks", expect_g7, hooks=hooks_for(range(5), hook_g7))

    # G8a: chains 0 and 1 biased at n=0 fire; chain 2 alone must not.
    def hook_y0(row):
        if row["n"] == 0:
            set_y(row, 0.3)
    def expect_g8a(r):
        for m in modes_of(r).values():
            assert "chains_0_1:untwisted_mean_Y_nonzero" in m["diagnostic_failures"], m["diagnostic_failures"]
    run_case("G8a chains 0 and 1 biased", expect_g8a, hooks=hooks_for((0, 1), hook_y0))
    def expect_not_g8a(r):
        for m in modes_of(r).values():
            assert "chains_0_1:untwisted_mean_Y_nonzero" not in m["diagnostic_failures"]
    run_case("G8a chain 2 alone must not fire", expect_not_g8a, hooks=hooks_for((2,), hook_y0))

    # G8b: mean Y0^2 above one.
    def hook_y2(row):
        if row["n"] == 0:
            row["sumY2"] = row["count"] * 1.5
    def expect_g8b(r):
        for m in modes_of(r).values():
            assert "pooled:untwisted_mean_Y_squared_above_one" in m["diagnostic_failures"]
            assert m["status"] == "INCONCLUSIVE_EQUILIBRATION"
    run_case("G8b untwisted Y squared above one", expect_g8b, hooks=hooks_for(range(5), hook_y2))

    # G9 partial: chain 4 in the alternative sector for 40 percent of its dwell.
    def hook_g9(row):
        if row["n"] == seam and row["phase"] == "dwell" and row["block"] < int(0.4 * analyze.DWELL_BLOCKS):
            row["sec0"], row["secMinus"] = 0, row["count"] * seam
            row["pure0"], row["pureMinus"] = 0, row["count"]
    def expect_g9(r):
        for m in modes_of(r).values():
            assert any(f.startswith("chain_4:") for f in m["sector_failures"]), m["sector_failures"]
            assert m["status"] == "SECTOR_FROZEN", m["status"]
    run_case("G9 chain 4 partially frozen", expect_g9, hooks=hooks_for((4,), hook_g9))

    # G10: R1 = 1 exactly with R2 small violates positivity -> FAIL_CONSISTENCY.
    def truth_g10(L, k, c, t):
        values = analyze.RATIO[k]
        i_one = min(range(5), key=lambda f: abs(values[f] - 1.0))
        i_low = values.index(min(values))
        probs = []
        for _ in range(seam):
            p = [0.0] * 5
            if k == 1:
                p[i_one] = 1.0
            else:
                p[i_low], p[i_one] = 0.7, 0.3
            probs.append(p)
        r = [math.fsum(pp * v for pp, v in zip(pr, values)) for pr in probs]
        return {"p": probs, "r": r, "Y": t["Y"]}
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

    # Degenerate: identical Y blocks at the twisted dwell.
    def hook_degenerate(row):
        if row["n"] == seam:
            row["sumY"] = row["count"] * 0.25
            row["sumY2"] = row["count"] * 0.0625
    def expect_degenerate(r):
        for m in modes_of(r).values():
            assert "pooled:mean_Y_twisted_degenerate_se" in m["diagnostic_failures"], m["diagnostic_failures"]
    run_case("degenerate Y variance", expect_degenerate, hooks=hooks_for(range(5), hook_degenerate))

    # Negligible contrast: every step ratio at the smallest value.
    def truth_small(L, k, c, t):
        values = analyze.RATIO[k]
        i_low = values.index(min(values))
        p = [0.0] * 5
        p[i_low] = 1.0
        return {"p": [p] * seam, "r": [values[i_low]] * seam, "Y": t["Y"]}
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
            if item["stem"] == "L4_k1_b2_c0":
                item["exit_code"] = 124
        (d / "execution.json").write_text(json.dumps(records, indent=2) + "\n")
        result = analyze.read_execution(d)
        assert result["volumes"][0]["status"] == "INCOMPLETE" and result["volumes"][0].get("control_incomplete")
        print("gate case ok: timed-out control caps the volume")


if __name__ == "__main__":
    sys.exit(main())
