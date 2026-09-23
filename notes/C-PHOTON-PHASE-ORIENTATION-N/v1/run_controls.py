#!/usr/bin/env python3
"""Driver and analysis for C-PHOTON-PHASE-ORIENTATION-N part A (controls only).
usage: run_controls.py run | analyze
"""
import math
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

N = 30
CONTROLS = {1: ("C1_coulomb", 1.5), 2: ("C2_confined", 0.7)}
LS = [8, 12, 16]
NTHERM, NMEAS, EVERY = 1000, 1500, 2
OUT = "runs"


def wilson(beta):
    W = [math.exp(beta * math.cos(2 * math.pi * f / N)) for f in range(N)]
    X = [math.sin(2 * math.pi * f / N) for f in range(N)]
    return W, X


def job(c, L, chain):
    name, beta = CONTROLS[c]
    W, X = wilson(beta)
    seed = 0xA0000000 + 1000 * L + 10 * c + chain
    start = "cold" if chain == 0 else "hot"
    cevery = 25 if L == 16 else 0
    fn = f"{OUT}/{name}_L{L}_{start}.log"
    if os.path.exists(fn) and os.path.getsize(fn) > 0:
        with open(fn) as fh:
            if sum(1 for ln in fh if ln.startswith("M ")) == NMEAS:
                return fn
    with open(fn, "w") as fh:
        subprocess.run(["./zlgt", str(N), str(L), hex(seed), start, str(NTHERM), str(NMEAS), str(EVERY), str(cevery)]
                       + [repr(v) for v in W] + [repr(v) for v in X], stdout=fh, check=True)
    return fn


def run():
    os.makedirs(OUT, exist_ok=True)
    jobs = [(c, L, ch) for L in LS for c in CONTROLS for ch in (0, 1)]
    jobs.sort(key=lambda t: -t[1])
    with ThreadPoolExecutor(max_workers=2) as ex:
        for fn in ex.map(lambda t: job(*t), jobs):
            print("done", fn, flush=True)


def parse(fn):
    M, C = [], []
    for ln in open(fn):
        if ln.startswith("M "):
            d = dict(kv.split("=") for kv in ln.split()[1:])
            M.append({k: float(v) for k, v in d.items()})
        elif ln.startswith("C "):
            d = dict(kv.split("=") for kv in ln.split()[1:])
            C.append({k: float(v) for k, v in d.items()})
    return M, C


def jack(vals, block=50):
    nb = len(vals) // block
    blocks = [sum(vals[i * block:(i + 1) * block]) / block for i in range(nb)]
    mean = sum(blocks) / nb
    var = sum((b - mean) ** 2 for b in blocks) / (nb * (nb - 1))
    return mean, math.sqrt(var)


def analyze():
    res = {}
    for c, (name, beta) in CONTROLS.items():
        for L in LS:
            per = {}
            for start in ("cold", "hot"):
                M, C = parse(f"{OUT}/{name}_L{L}_{start}.log")
                d1 = [m["A1"] - m["B1"] for m in M]
                d2 = [m["A2"] - m["B2"] for m in M]
                per[start] = dict(d1=jack(d1), d2=jack(d2), mono=jack([m["mono"] for m in M]),
                                  pol=jack([m["polrad"] for m in M]), cos=jack([m["cos"] for m in M]), M=M, C=C)
            a, b = per["cold"]["d1"], per["hot"]["d1"]
            z = abs(a[0] - b[0]) / math.hypot(a[1], b[1])
            pooled = {k: ((per["cold"][k][0] + per["hot"][k][0]) / 2, math.hypot(per["cold"][k][1], per["hot"][k][1]) / 2)
                      for k in ("d1", "d2", "mono", "pol", "cos")}
            res[(c, L)] = (pooled, z, per)
            print(f"{name} beta={beta} L={L} Delta1={pooled['d1'][0]:.5f}+-{pooled['d1'][1]:.5f} Delta2={pooled['d2'][0]:.5f}+-{pooled['d2'][1]:.5f} "
                  f"mono={pooled['mono'][0]:.5f} polrad={pooled['pol'][0]:.5f}+-{pooled['pol'][1]:.5f} cos={pooled['cos'][0]:.5f} hotcold_z={z:.2f}")
    ok = True
    for c, (name, beta) in CONTROLS.items():
        rho = res[(c, 16)][0]["d1"][0] / res[(c, 8)][0]["d1"][0]
        monos = [res[(c, L)][0]["mono"][0] for L in LS]
        zs = [res[(c, L)][1] for L in LS]
        if c == 1:
            good = rho >= 0.75 and all(mn < 0.01 for mn in monos)
        else:
            good = rho <= 0.5 and all(mn > 0.05 for mn in monos)
        good = good and all(zz <= 4 for zz in zs)
        ok = ok and good
        print(f"{name} rho=Delta16/Delta8={rho:.4f} monos={[round(m,5) for m in monos]} hotcold_z={[round(z,2) for z in zs]} -> {'PASS' if good else 'FAIL'}")
    # correlator ratio diagnostics at L=16 for the Coulomb control
    for c in CONTROLS:
        name = CONTROLS[c][0]
        Cs = []
        cosm = []
        for start in ("cold", "hot"):
            M, C = parse(f"{OUT}/{name}_L16_{start}.log")
            Cs += C
            cosm += [m["cos"] for m in M]
        cbar = sum(cosm) / len(cosm)
        def Cn(n):
            lo = sum(x[f"L{n}"] for x in Cs) / len(Cs)
            tr = sum(x[f"T{n}"] for x in Cs) / len(Cs)
            return 12 * (lo - cbar ** 2) + 12 * (tr - cbar ** 2)
        for n in range(2, 5):
            q = Cn(n) / Cn(n + 1)
            q4 = (n ** -4 + (16 - n) ** -4) / ((n + 1) ** -4 + (15 - n) ** -4)
            print(f"CORR {name} L=16 n={n} C={Cn(n):.5e} Q={q:.4f} Q4={q4:.4f} D={q/q4-1:+.4f} (samples {len(Cs)}, no error bars: diagnostic)")
    print("ENGINE_CALIBRATION " + ("PASS" if ok else "FAIL"))


if __name__ == "__main__":
    run() if sys.argv[1] == "run" else analyze()
