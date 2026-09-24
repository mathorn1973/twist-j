#!/usr/bin/env python3
"""Analysis and frozen decision rule for C-PHOTON-CONTRAST-DRIFT-N.
NON-CANONICAL engineering orientation. Standard library only.
Parsing, blocks, standard errors and the fit are those of analyze_v3.py
(imported, unchanged).

usage: analyze_drift.py LOGDIR
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import analyze_v3 as A  # noqa: E402
from jobs_drift import PLAN  # noqa: E402

# Plateau of part B3 (analysis_B3.txt, sha256 5d870f10...): inverse-variance
# weighted mean of the six pooled contrasts with s >= 1/4, standard error taken
# as fully correlated (weighted mean of the six standard errors).
P_REF, SE_P = 0.602177, 0.002859
# Pooled B3 points (L, m, Delta, SE) from analysis_B3.txt, for the information refit.
B3 = [(8, 1, 0.599843, 0.0027), (8, 2, 0.602553, 0.0021), (12, 1, 0.602356, 0.0056),
      (12, 2, 0.604161, 0.0036), (16, 1, 0.589804, 0.0065), (16, 2, 0.60305, 0.0026),
      (24, 1, 0.580132, 0.011), (24, 2, 0.600327, 0.0059)]


def main():
    logdir = sys.argv[1]
    print(f"ANALYSIS C-PHOTON-CONTRAST-DRIFT-N P_ref={P_REF:.6f} SE_P={SE_P:.6f} block={A.BLOCK}")
    stop, res = [], {}
    for L in sorted(PLAN):
        chains, ftr = {}, []
        for rep in PLAN[L]:
            name = f"TW_L{L}_cold{rep}"
            M, C, run, end = A.parse(os.path.join(logdir, name + ".log"))
            if len(M) != 4000 or end is None or run is None:
                stop.append(f"INTEGRITY {name} meas={len(M)} end={end is not None}")
                continue
            T = [m for m in M if m["triv"]]
            ftriv = len(T) / len(M)
            ftr.append(f"cold{rep}={ftriv:.3f}")
            if ftriv < A.FTRIV:
                print(f"  TRAPPED {name} ftriv={ftriv:.3f}")
                continue
            chains[rep] = {q: A.blocks([m[q] for m in T]) for q in A.QTY}
            for q in ("D1", "mono"):
                vals = [m[q] for m in T]
                h, hb = len(vals) // 2, A.BLOCK // 2
                b1 = [sum(vals[i * hb:(i + 1) * hb]) / hb for i in range(h // hb)]
                b2 = [sum(vals[h + i * hb:h + (i + 1) * hb]) / hb for i in range((len(vals) - h) // hb)]
                z = A.zdiff(A.mean_se(b1), A.mean_se(b2))
                if z > 4:
                    stop.append(f"STATIONARITY {name} {q} z={z:.2f}")
        print(f"  FTRIV L={L} " + " ".join(ftr))
        if 2 * len(chains) < len(PLAN[L]):
            stop.append(f"TOO_FEW_QUALIFYING L={L} {len(chains)}/{len(PLAN[L])}")
            continue
        P = {q: A.mean_se([b for r in chains for b in chains[r][q]]) for q in A.QTY}
        d = ((1 + P["x2"][0]) / 2, P["x2"][1] / 2)
        chi25 = (d[0] - P["A1"][0], math.hypot(d[1], P["A1"][1]))
        bb = (d[0] - P["B1"][0], math.hypot(d[1], P["B1"][1]))
        dl = P_REF - P["D1"][0]
        sig = math.hypot(P["D1"][1], SE_P)
        res[L] = (dl, sig, P)
        line = " ".join(f"{q}={P[q][0]:.6g}+-{P[q][1]:.2g}" for q in ("D1", "D2", "mono", "polrad", "fnz", "cos"))
        print(f"  L={L} chains={len(chains)} {line}")
        print(f"    byproduct d={d[0]:.6f}+-{d[1]:.2g} b_L={bb[0]:.6f}+-{bb[1]:.2g} 25chi_L={chi25[0]:.6f}+-{chi25[1]:.2g}")
        print(f"    drift d_L=P_ref-Delta_L(1)={dl:.6f} sigma_L={sig:.6f} z={dl / sig:.3f}")
    for s in stop:
        print("  GATE " + s)
    if stop or any(L not in res for L in PLAN):
        term = "STOP_DRIFT"
    else:
        z = {L: res[L][0] / res[L][1] for L in res}
        if z[24] > 3 and z[32] > 3:
            term = "DRIFT_CONFIRMED"
        elif abs(z[24]) <= 3 and abs(z[32]) <= 3:
            term = "NO_DRIFT"
        else:
            term = "MIXED"
            for L in res:
                if z[L] < -3:
                    print(f"  ANOMALY_HIGH L={L} z={z[L]:.3f}")
        pts = [(4 * math.sin(math.pi * m / L) ** 2, y, se) for L, m, y, se in B3]
        for L in res:
            Pq = res[L][2]
            for m, key in ((1, "D1"), (2, "D2")):
                pts.append((4 * math.sin(math.pi * m / L) ** 2, Pq[key][0], Pq[key][1]))
        f = A.fit(pts)
        if f is not None:
            print(f"  INFO_REFIT_B3_PLUS_NEW Z={f['Z']:.6g}+-{f['seZ']:.2g} M={f['M']:.6g}+-{f['seM']:.2g} "
                  f"chi2={f['chi2']:.2f} dof={f['dof']} (no decision weight)")
    print("TERMINAL " + term)


if __name__ == "__main__":
    main()
