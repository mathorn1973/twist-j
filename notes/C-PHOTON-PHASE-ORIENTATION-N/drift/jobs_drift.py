#!/usr/bin/env python3
"""Job list and runner for C-PHOTON-CONTRAST-DRIFT-N (NON-CANONICAL).
Engine zlgt2.c and the TWIST tables, seeds and thermalization of
C-PHOTON-PHASE-ORIENTATION-N v3 (imported from jobs_v3.py, unchanged).
New chains only: TW cold replicas 3..14 at L = 24 and 1..8 at L = 32.

usage: jobs_drift.py list
       jobs_drift.py run OUTDIR WORKERS --owner-authorized
Standard library only.
"""
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jobs_v3 as J  # noqa: E402

PLAN = {24: list(range(3, 15)), 32: list(range(1, 9))}


def jobs():
    N, W, X = J.tables("TW")
    out = []
    for L, reps in PLAN.items():
        for rep in reps:
            name = f"TW_L{L}_cold{rep}"
            cmd = ["./zlgt2", str(N), str(L), hex(J.seed("TW", L, "cold", rep)), "cold",
                   str(J.ntherm(L)), str(J.NMEAS), str(J.EVERY), "0"]
            cmd += [repr(v) for v in W] + [repr(v) for v in X]
            cost = (J.ntherm(L) + J.NMEAS * J.EVERY) * L ** 4
            out.append((cost, name, cmd))
    out.sort(key=lambda t: -t[0])
    return out


def main():
    mode = sys.argv[1]
    js = jobs()
    if mode == "list":
        for cost, name, cmd in js:
            print(name, " ".join(cmd[:9]))
        return
    if "--owner-authorized" not in sys.argv:
        sys.exit("refused: TWIST-weight runs need --owner-authorized")
    outdir, workers = sys.argv[2], int(sys.argv[3])
    os.makedirs(outdir, exist_ok=True)

    def run(job):
        cost, name, cmd = job
        fn = os.path.join(outdir, name + ".log")
        if J.complete(fn):
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
