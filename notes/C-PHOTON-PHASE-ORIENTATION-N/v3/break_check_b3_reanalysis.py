#!/usr/bin/env python3
"""Second reading of C-PHOTON-PHASE-ORIENTATION-N version 3, part B3.
NON-CANONICAL break attempt, no decision weight. Standard library only.

Written after the frozen terminal was known; it cannot change it. Every
variant listed here is run once and every output line is recorded.

Independent of analyze_v3.py: it does not import it or jobs_v3.py. It reuses
only the frozen definitions (Delta = A - B, TRIVIAL iff max |Fbar_a| < 3/4,
a chain qualifies iff at least 1/4 of its measurements are TRIVIAL, the rule
thresholds). Estimation and fit are done differently:

  errors  V1 to V3: batch means with batches of 400 measurements (twice the
          frozen block); V4: integrated autocorrelation time with the
          automatic window of Sokal (c = 6), per chain, combined over chains
  fit     profile chi2 over M on a grid, Z solved linearly for each M;
          interval for M from delta chi2 = 4 (two sigma), for Z from the
          curvature of the profile in Z at the best M
  rule    (a) |Delta_L(1)| <= 3 SE at L = 16 and 24 -> MASSIVE
          (b) Z - 3 SE(Z) > 0 and M_up(2 sigma) < thr -> COULOMB
          (c) M_lo(2 sigma) > thr -> MASSIVE
          (d) otherwise UNRESOLVED
Variants:
  V1  all qualifying chains, L = 8, 12, 16, 24
  V2  cold chains only
  V3  all qualifying chains, fit without L = 8
  V4  as V1 with autocorrelation-time errors
  V5  diagnostic: every measurement of every chain, trapped chains included
      and no sector conditioning (not a valid estimator in a frozen-sector
      phase; shows what the conditioning does)

usage: break_check_b3_reanalysis.py LOGDIR
"""
import math
import os
import sys

LS = (8, 12, 16, 24)
CHAINS = (("cold", 1), ("cold", 2), ("hot", 1), ("hot", 2))
FM = ("fm01", "fm02", "fm03", "fm12", "fm13", "fm23")
THR = math.sin(math.pi / 24) ** 2          # qhat_min^2 / 4


def read(fn):
    rows = []
    with open(fn) as fh:
        for ln in fh:
            if ln.startswith("M "):
                kv = {}
                for t in ln.split()[1:]:
                    k, v = t.split("=")
                    kv[k] = float(v)
                triv = max(abs(kv[k]) for k in FM) < 0.75
                rows.append((kv["A1"] - kv["B1"], kv["A2"] - kv["B2"], triv))
    return rows


def batches(v, size):
    nb = len(v) // size
    return [sum(v[i * size:(i + 1) * size]) / size for i in range(nb)]


def mse(b):
    n = len(b)
    m = math.fsum(b) / n
    return m, math.sqrt(math.fsum((x - m) ** 2 for x in b) / (n - 1) / n)


def tau_int(v, c=6.0):
    n = len(v)
    m = math.fsum(v) / n
    d = [x - m for x in v]
    c0 = math.fsum(x * x for x in d) / n
    tau = 0.5
    for t in range(1, n // 2):
        ct = math.fsum(d[i] * d[i + t] for i in range(n - t)) / (n - t)
        tau += ct / c0
        if t >= c * tau:
            break
    return m, c0, max(tau, 0.5)


def fit_profile(pts):
    """pts: list of (s, y, se). Returns dict or None."""
    smin = min(p[0] for p in pts)

    def prof(M):
        g = [s / (s + M) for s, _, _ in pts]
        w = [1 / se ** 2 for _, _, se in pts]
        num = math.fsum(wi * gi * y for wi, gi, (_, y, _) in zip(w, g, pts))
        den = math.fsum(wi * gi * gi for wi, gi in zip(w, g))
        Z = num / den
        chi2 = math.fsum(wi * (y - Z * gi) ** 2 for wi, gi, (_, y, _) in zip(w, g, pts))
        return chi2, Z, math.sqrt(1 / den)

    lo = -0.9 * smin
    grid = [lo + (0.05 - lo) * i / 20000 for i in range(20001)]
    grid += [0.05 * (1.0005 ** i) for i in range(1, 12000)]
    vals = [(prof(M), M) for M in grid]
    (c0, Z0, seZ0), M0 = min(vals, key=lambda t: t[0][0])
    inside = [M for (c, _, _), M in vals if c - c0 <= 4.0]
    inside1 = [M for (c, _, _), M in vals if c - c0 <= 1.0]
    return dict(Z=Z0, seZ=seZ0, M=M0, Mlo2=min(inside), Mup2=max(inside),
                Mlo1=min(inside1), Mup1=max(inside1), chi2=c0, dof=len(pts) - 2,
                edge=(max(inside) >= grid[-1]))


def label(D1, fit):
    a = all(abs(D1[L][0]) <= 3 * D1[L][1] for L in (16, 24) if L in D1)
    if a and 16 in D1 and 24 in D1:
        return "MASSIVE_ORIENTATION(a)"
    if fit is None:
        return "UNRESOLVED_ORIENTATION"
    if fit["Z"] - 3 * fit["seZ"] > 0 and fit["Mup2"] < THR:
        return "COULOMB_ORIENTATION"
    if fit["Mlo2"] > THR:
        return "MASSIVE_ORIENTATION(c)"
    return "UNRESOLVED_ORIENTATION"


def main(d):
    data = {}
    for L in LS:
        for st, rp in CHAINS:
            rows = read(os.path.join(d, "TW_L%d_%s%d.log" % (L, st, rp)))
            assert len(rows) == 4000
            data[(L, st, rp)] = rows
    print("SECOND READING C-PHOTON-PHASE-ORIENTATION-N v3 B3 thr=%.6f" % THR)
    variants = {
        "V1": dict(chains=CHAINS, fitLs=LS, err="batch400", cond=True),
        "V2": dict(chains=CHAINS[:2], fitLs=LS, err="batch400", cond=True),
        "V3": dict(chains=CHAINS, fitLs=(12, 16, 24), err="batch400", cond=True),
        "V4": dict(chains=CHAINS, fitLs=LS, err="tau", cond=True),
        "V5": dict(chains=CHAINS, fitLs=LS, err="batch400", cond=False),
    }
    for name, v in variants.items():
        est = {1: {}, 2: {}}
        for L in LS:
            per = {1: [], 2: []}
            used = []
            for key in v["chains"]:
                rows = data[(L,) + key]
                if v["cond"]:
                    T = [r for r in rows if r[2]]
                    if len(T) < len(rows) / 4:
                        continue
                else:
                    T = rows
                used.append("%s%d:%d" % (key[0], key[1], len(T)))
                for m in (1, 2):
                    per[m].append([r[m - 1] for r in T])
            if not per[1]:
                continue
            for m in (1, 2):
                if v["err"] == "batch400":
                    allb = [b for series in per[m] for b in batches(series, 400)]
                    est[m][L] = mse(allb)
                else:
                    n_tot = sum(len(s) for s in per[m])
                    mean = math.fsum(math.fsum(s) for s in per[m]) / n_tot
                    var_mean = 0.0
                    for s in per[m]:
                        mm, c0, tau = tau_int(s)
                        w = len(s) / n_tot
                        var_mean += w * w * 2 * tau * c0 / len(s)
                        if m == 1:
                            print("  %s TAU L=%d n=%d tau_int=%.3f" % (name, L, len(s), tau))
                    est[m][L] = (mean, math.sqrt(var_mean))
            print("  %s L=%d chains=%s D1=%.6f+-%.6f D2=%.6f+-%.6f" % (
                name, L, ",".join(used), est[1][L][0], est[1][L][1], est[2][L][0], est[2][L][1]))
        pts = []
        for L in v["fitLs"]:
            for m in (1, 2):
                if L in est[m]:
                    pts.append((4 * math.sin(math.pi * m / L) ** 2, est[m][L][0], est[m][L][1]))
        fit = fit_profile(pts) if len(pts) >= 3 else None
        if fit:
            print("  %s FIT Z=%.6f+-%.6f M=%.6f [1sig %.6f, %.6f] [2sig %.6f, %.6f] chi2=%.2f dof=%d edge=%s" % (
                name, fit["Z"], fit["seZ"], fit["M"], fit["Mlo1"], fit["Mup1"], fit["Mlo2"], fit["Mup2"],
                fit["chi2"], fit["dof"], fit["edge"]))
        print("  %s LABEL %s%s" % (name, label(est[1], fit), "  (diagnostic only)" if name == "V5" else ""))


if __name__ == "__main__":
    main(sys.argv[1])
