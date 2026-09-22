#!/usr/bin/env python3
"""Analysis and frozen decision rule for C-PHOTON-PHASE-ORIENTATION-N v3 (rule identical to v2).
NON-CANONICAL engineering orientation. Standard library only.

usage: analyze_v2.py MODELSET LOGDIR [BLOCKTABLE_OUT]
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jobs_v3 as J  # noqa: E402

BLOCK = 200
TRIV = 0.75      # trivial topological sector: every plane-averaged integer flux below 3/4
FTRIV = 0.25     # a chain qualifies if at least this fraction of its measurements is trivial
QTY = ["D1", "D2", "A1", "B1", "A2", "B2", "x2", "mono", "polrad", "fnz", "cos"]


def parse(fn):
    M, C, run, end = [], [], None, None
    with open(fn) as fh:
        for ln in fh:
            if ln.startswith("M "):
                d = {k: float(v) for k, v in (kv.split("=") for kv in ln.split()[1:])}
                d["D1"] = d["A1"] - d["B1"]
                d["D2"] = d["A2"] - d["B2"]
                d["triv"] = max(abs(d[k]) for k in ("fm01", "fm02", "fm03", "fm12", "fm13", "fm23")) < TRIV
                M.append(d)
            elif ln.startswith("C "):
                C.append({k: float(v) for k, v in (kv.split("=") for kv in ln.split()[1:])})
            elif ln.startswith("RUN "):
                run = ln.strip()
            elif ln.startswith("END "):
                end = ln.strip()
    return M, C, run, end


def blocks(vals):
    nb = len(vals) // BLOCK
    return [sum(vals[i * BLOCK:(i + 1) * BLOCK]) / BLOCK for i in range(nb)]


def mean_se(bl):
    n = len(bl)
    m = sum(bl) / n
    var = sum((b - m) ** 2 for b in bl) / (n - 1) if n > 1 else 0.0
    return m, math.sqrt(var / n)


def zdiff(a, b):
    d = abs(a[0] - b[0])
    s = math.hypot(a[1], b[1])
    if s == 0:
        return 0.0 if d == 0 else float("inf")
    return d / s


def fit(points):
    """Weighted Levenberg-Marquardt fit of y = Z s/(s+M); points (s, y, se)."""
    smin = min(s for s, _, _ in points)
    pts = [(s, y, se) for s, y, se in points if se > 0]
    if len(pts) < 3:
        return None

    def model(p, s):
        Z, M = p
        return Z * s / (s + M)

    def chi2(p):
        return sum(((y - model(p, s)) / se) ** 2 for s, y, se in pts)

    def jac(p, s, se):
        Z, M = p
        return (s / (s + M) / se, -Z * s / (s + M) ** 2 / se)

    best = None
    ymax = max(y for _, y, _ in pts)
    for M0 in (1e-3, 1e-2, 5e-2, 2e-1, 1.0):
        p = [ymax if ymax > 0 else 1e-3, M0]
        lam = 1e-3
        c = chi2(p)
        for _ in range(400):
            JTJ = [[0.0, 0.0], [0.0, 0.0]]
            JTr = [0.0, 0.0]
            for s, y, se in pts:
                j = jac(p, s, se)
                r = (y - model(p, s)) / se
                for a in range(2):
                    JTr[a] += j[a] * r
                    for b in range(2):
                        JTJ[a][b] += j[a] * j[b]
            A = [[JTJ[0][0] * (1 + lam), JTJ[0][1]], [JTJ[1][0], JTJ[1][1] * (1 + lam)]]
            det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
            if det == 0:
                break
            dz = (A[1][1] * JTr[0] - A[0][1] * JTr[1]) / det
            dm = (-A[1][0] * JTr[0] + A[0][0] * JTr[1]) / det
            q = [p[0] + dz, p[1] + dm]
            if q[1] <= -0.9 * smin:
                q[1] = -0.9 * smin + 1e-12
            cq = chi2(q)
            if cq < c:
                if abs(c - cq) < 1e-12 * (1 + c):
                    p, c = q, cq
                    break
                p, c, lam = q, cq, lam / 3
            else:
                lam *= 5
                if lam > 1e12:
                    break
        if best is None or c < best[1]:
            best = (p, c)
    p, c = best
    JTJ = [[0.0, 0.0], [0.0, 0.0]]
    for s, y, se in pts:
        j = jac(p, s, se)
        for a in range(2):
            for b in range(2):
                JTJ[a][b] += j[a] * j[b]
    det = JTJ[0][0] * JTJ[1][1] - JTJ[0][1] * JTJ[1][0]
    if det <= 0:
        return None
    cov = [[JTJ[1][1] / det, -JTJ[0][1] / det], [-JTJ[1][0] / det, JTJ[0][0] / det]]
    return dict(Z=p[0], M=p[1], seZ=math.sqrt(max(cov[0][0], 0)), seM=math.sqrt(max(cov[1][1], 0)),
                chi2=c, dof=len(pts) - 2)


def analyze_model(model, logdir, rows):
    res = {"model": model, "L": {}, "stop": [], "corr": None}
    corr_acc = []
    for L in J.LS:
        chains = {}
        for start, rep in J.CHAINS:
            name = f"{model}_L{L}_{start}{rep}"
            fn = os.path.join(logdir, name + ".log")
            M, C, run, end = parse(fn)
            if len(M) != J.NMEAS or end is None or run is None:
                res["stop"].append(f"INTEGRITY {name} meas={len(M)} end={end is not None}")
                continue
            T = [m for m in M if m["triv"]]
            ftriv = len(T) / len(M)
            res.setdefault("ftriv", {})[name] = ftriv
            if ftriv < FTRIV:
                res.setdefault("trapped", []).append(f"{name} ftriv={ftriv:.3f}")
                continue
            bq = {q: blocks([m[q] for m in T]) for q in QTY}
            for i in range(len(bq["D1"])):
                rows.append("\t".join([name, str(i), f"{ftriv:.4f}"] + [repr(bq[q][i]) for q in QTY]))
            chains[(start, rep)] = bq
            # stationarity: halves of the trivial-sector subsequence, blocks of BLOCK/2
            for q in ("D1", "mono"):
                vals = [m[q] for m in T]
                h = len(vals) // 2
                b1 = [sum(vals[i * (BLOCK // 2):(i + 1) * (BLOCK // 2)]) / (BLOCK // 2) for i in range(h // (BLOCK // 2))]
                b2 = [sum(vals[h + i * (BLOCK // 2):h + (i + 1) * (BLOCK // 2)]) / (BLOCK // 2) for i in range((len(vals) - h) // (BLOCK // 2))]
                z = zdiff(mean_se(b1), mean_se(b2))
                if z > 4:
                    res["stop"].append(f"STATIONARITY {name} {q} z={z:.2f}")
            if L == 16:
                corr_acc += [(c, sum(m["cos"] for m in M) / len(M)) for c in C]
        ncold = sum(1 for key in chains if key[0] == "cold")
        nhot = sum(1 for key in chains if key[0] == "hot")
        if ncold == 0:
            res["stop"].append(f"NO_COLD_CHAIN_IN_TRIVIAL_SECTOR L={L}")
            continue
        pooled = {}
        for q in QTY:
            allb = [b for key in chains for b in chains[key][q]]
            pooled[q] = mean_se(allb)
        cold = mean_se([b for key in chains if key[0] == "cold" for b in chains[key]["D1"]])
        if nhot > 0:
            hot = mean_se([b for key in chains if key[0] == "hot" for b in chains[key]["D1"]])
            zhc = zdiff(cold, hot)
            if zhc > 4:
                res["stop"].append(f"HOTCOLD L={L} D1 cold={cold[0]:.5f} hot={hot[0]:.5f} z={zhc:.2f}")
        else:
            hot, zhc = None, float("nan")
            res.setdefault("hot_trapped_L", []).append(L)
        res["L"][L] = dict(pooled=pooled, zhc=zhc, cold=cold, hot=hot, nchains=len(chains))
    if corr_acc:
        n = len(corr_acc)
        cbar = sum(cb for _, cb in corr_acc) / n
        out = []
        for k in range(2, 5):
            def Cn(t):
                lo = sum(c[f"L{t}"] for c, _ in corr_acc) / n
                tr = sum(c[f"T{t}"] for c, _ in corr_acc) / n
                return 12 * (lo - cbar ** 2) + 12 * (tr - cbar ** 2)
            q4 = (k ** -4 + (16 - k) ** -4) / ((k + 1) ** -4 + (15 - k) ** -4)
            q = Cn(k) / Cn(k + 1) if Cn(k + 1) != 0 else float("nan")
            out.append((k, Cn(k), q, q4))
        res["corr"] = (n, out)
    return res


def decide(res):
    if res["stop"] or any(L not in res["L"] for L in J.LS):
        return "STOP_MIXING_ORIENTATION", None
    Ls = res["L"]
    # rule (a): zero at L = 16 and 24
    a = all(abs(Ls[L]["pooled"]["D1"][0]) <= 3 * Ls[L]["pooled"]["D1"][1] for L in (16, 24))
    pts = []
    for L in J.LS:
        for mm, key in ((1, "D1"), (2, "D2")):
            s = 4 * math.sin(math.pi * mm / L) ** 2
            y, se = Ls[L]["pooled"][key]
            pts.append((s, y, se))
    f = fit(pts)
    if a:
        return "MASSIVE_ORIENTATION", f
    if f is None:
        return "UNRESOLVED_ORIENTATION", f
    thr = 4 * math.sin(math.pi / 24) ** 2 / 4
    if f["Z"] - 3 * f["seZ"] > 0 and f["M"] + 2 * f["seM"] < thr:
        return "COULOMB_ORIENTATION", f
    if f["M"] - 2 * f["seM"] > thr:
        return "MASSIVE_ORIENTATION", f
    return "UNRESOLVED_ORIENTATION", f


def main():
    modelset, logdir = sys.argv[1], sys.argv[2]
    rows = ["\t".join(["chain", "block", "ftriv"] + QTY)]
    labels = {}
    thr = 4 * math.sin(math.pi / 24) ** 2 / 4
    print(f"ANALYSIS C-PHOTON-PHASE-ORIENTATION-N v3 set={modelset} block={BLOCK} q2min/4={thr:.6f}")
    for model in J.SETS[modelset]:
        res = analyze_model(model, logdir, rows)
        lab, f = decide(res)
        labels[model] = lab
        print(f"MODEL {model} ({J.MODELS[model]['label']})")
        for L in sorted(res["L"]):
            P = res["L"][L]["pooled"]
            line = " ".join(f"{q}={P[q][0]:.6g}+-{P[q][1]:.2g}" for q in ("D1", "D2", "mono", "polrad", "fnz", "cos"))
            print(f"  L={L} chains={res['L'][L]['nchains']} {line} hotcold_z={res['L'][L]['zhc']:.2f}")
            if model == "TW":
                d = ((1 + P["x2"][0]) / 2, P["x2"][1] / 2)
                chi25 = (d[0] - P["A1"][0], math.hypot(d[1], P["A1"][1]))
                bb = (d[0] - P["B1"][0], math.hypot(d[1], P["B1"][1]))
                print(f"    byproduct d={d[0]:.6f}+-{d[1]:.2g} b_L={bb[0]:.6f}+-{bb[1]:.2g} 25chi_L={chi25[0]:.6f}+-{chi25[1]:.2g}")
        for s in res["stop"]:
            print("  GATE " + s)
        for s in res.get("trapped", []):
            print("  TRAPPED " + s)
        if res.get("hot_trapped_L"):
            print("  HOT_TRAPPED_AT_L " + ",".join(str(x) for x in res["hot_trapped_L"]) + " (hot/cold gate not evaluable there)")
        ft = res.get("ftriv", {})
        if ft:
            print("  FTRIV " + " ".join(f"{k.split('_',1)[1]}={v:.3f}" for k, v in sorted(ft.items())))
        if f is not None:
            print(f"  FIT Z={f['Z']:.6g}+-{f['seZ']:.2g} M={f['M']:.6g}+-{f['seM']:.2g} chi2={f['chi2']:.2f} dof={f['dof']}")
        if res["corr"]:
            n, out = res["corr"]
            for k, cn, q, q4 in out:
                print(f"  CORR16 n={k} C={cn:.5e} Q={q:.4f} Q4={q4:.4f} D={q / q4 - 1:+.4f} (samples {n}, diagnostic)")
        print(f"  LABEL {model} {lab}")
    if modelset == "A3":
        ok = (labels["C1"] == "COULOMB_ORIENTATION" and labels["C2"] == "MASSIVE_ORIENTATION"
              and labels["C3"] != "COULOMB_ORIENTATION" and labels["C4"] != "MASSIVE_ORIENTATION"
              and labels["C5"] != "COULOMB_ORIENTATION")
        print("ENGINE_CALIBRATION_V3 " + ("PASS" if ok else "FAIL"))
    else:
        print("TERMINAL " + labels["TW"])
    if len(sys.argv) > 3:
        with open(sys.argv[3], "w") as fh:
            fh.write("\n".join(rows) + "\n")


if __name__ == "__main__":
    main()
