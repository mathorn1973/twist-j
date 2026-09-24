#!/usr/bin/env python3
"""Job list and runner for C-PHOTON-PHASE-ORIENTATION-N v2 (NON-CANONICAL).

usage: jobs_v2.py list  MODELSET
       jobs_v2.py run   MODELSET OUTDIR WORKERS [--owner-authorized]
MODELSET: A2 (controls C1..C5) or B2 (TWIST point, needs --owner-authorized).
Standard library only. Deterministic job list; seeds are functions of
(model, L, start, replica).
"""
import math
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

PHI = (1 + 5 ** 0.5) / 2
MODELS = {
    "C1": dict(N=12, beta=1.5, label="Z12 Wilson beta 3/2, Coulomb control"),
    "C2": dict(N=12, beta=0.7, label="Z12 Wilson beta 7/10, confined control"),
    "C3": dict(N=5, beta=5.0, label="Z5 Wilson beta 5, Higgs/frozen control"),
    "C4": dict(N=12, beta=1.1, label="Z12 Wilson beta 11/10, near-edge Coulomb control"),
    "C5": dict(N=12, beta=0.9, label="Z12 Wilson beta 9/10, near-edge confined control"),
    "TW": dict(N=5, beta=None, label="TWIST weight W at t = 1"),
}
SETS = {"A2": ["C1", "C2", "C3", "C4", "C5"], "B2": ["TW"]}
LS = [8, 12, 16, 24]
NMEAS, EVERY = 4000, 2
CHAINS = [("cold", 1), ("cold", 2), ("hot", 1), ("hot", 2)]


def ntherm(L):
    return 2000 * L * L // 64


def tables(model):
    m = MODELS[model]
    N = m["N"]
    if model == "TW":
        W = [4.0, PHI ** 2, PHI ** -2, PHI ** -2, PHI ** 2]
        X = [0.0, math.tan(math.pi / 5), math.tan(2 * math.pi / 5), -math.tan(2 * math.pi / 5), -math.tan(math.pi / 5)]
    else:
        h = N // 2
        Wh = [math.exp(m["beta"] * math.cos(2 * math.pi * f / N)) for f in range(h + 1)]
        Xh = [math.sin(2 * math.pi * f / N) for f in range(h + 1)]
        Xh[0] = 0.0
        if N % 2 == 0:
            Xh[h] = 0.0
        W = [Wh[min(f, N - f)] for f in range(N)]
        X = [Xh[f] if f <= h else -Xh[N - f] for f in range(N)]
    return N, W, X


def seed(model, L, start, rep):
    mi = list(MODELS).index(model)
    return 0xC2000000 + mi * 0x100000 + L * 0x1000 + (0x10 if start == "hot" else 0) + rep


def jobs(modelset):
    out = []
    for model in SETS[modelset]:
        N, W, X = tables(model)
        for L in LS:
            for start, rep in CHAINS:
                name = f"{model}_L{L}_{start}{rep}"
                cmd = ["./zlgt2", str(N), str(L), hex(seed(model, L, start, rep)), start,
                       str(ntherm(L)), str(NMEAS), str(EVERY), str(40 if L == 16 else 0)]
                cmd += [repr(v) for v in W] + [repr(v) for v in X]
                cost = (ntherm(L) + NMEAS * EVERY) * 4 * L ** 4 * (N + 6)
                out.append((cost, name, cmd))
    out.sort(key=lambda t: -t[0])
    return out


def complete(fn):
    if not os.path.exists(fn):
        return False
    with open(fn) as fh:
        tail = fh.read()[-200:]
    return "END sweeps=" in tail


def main():
    mode, modelset = sys.argv[1], sys.argv[2]
    if modelset == "B2" and mode == "run" and "--owner-authorized" not in sys.argv:
        sys.exit("refused: B2 needs --owner-authorized")
    js = jobs(modelset)
    if mode == "list":
        for cost, name, cmd in js:
            print(name, " ".join(cmd[:9]))
        return
    outdir, workers = sys.argv[3], int(sys.argv[4])
    os.makedirs(outdir, exist_ok=True)

    def run(job):
        cost, name, cmd = job
        fn = os.path.join(outdir, name + ".log")
        if complete(fn):
            return name + " skip"
        with open(fn, "w") as fh:
            r = subprocess.run(cmd, stdout=fh, stderr=subprocess.PIPE, text=True)
        if r.returncode != 0 or r.stderr:
            return name + f" FAIL rc={r.returncode} stderr={r.stderr[:200]!r}"
        return name + " done"

    with ThreadPoolExecutor(max_workers=workers) as ex:
        for msg in ex.map(run, js):
            print(msg, flush=True)


if __name__ == "__main__":
    main()
