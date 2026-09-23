#!/usr/bin/env python3
"""Break check for C-PHOTON-PHASE-ORIENTATION-N version 3, part B3, against the
owner's independent exact heat-bath engine (public probe
P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2). NON-CANONICAL engineering check.
Standard library only.

Frozen before any B3 L = 8 observable was read. Up to this freeze only the
sha256 of the B3 logs and their END state hashes were compared across the two
hosts.

Observables per plaquette at L = 8, TWIST weight t = 1:
  logw = mean log W(f),  x2 = mean X(f)^2,  cos = mean cos(2 pi f/5),
  W = (4, phi^2, phi^-2, phi^-2, phi^2), X = tan(pi f/5).

Pilot side: every SAMPLE line of L8_{cold,hot}_r{1,2}.log; the value is
  computed from the exact integer flux_count_0..4 (not from the printed
  floats); per chain 16 batches of 32 samples; chain mean and SE by batch
  means; pooled = mean of the 4 chain means, SE = sqrt(sum SE_c^2)/4.
B3 side: every M line of TW_L8_{cold,hot}{1,2}.log, all 4000 measurements,
  no sector conditioning (the pilot does not condition either); per chain 20
  batches of 200; pooled likewise.

Decision, fixed now: z = |pooled_B3 - pooled_pilot| / hypot(SE_B3, SE_pilot)
  for logw. CROSSCHECK_PASS iff z <= 4. Otherwise CROSSCHECK_FAIL: the B3
  terminal is then reported with that flag and no reading fixed in advance is
  taken from it.
Secondary, no decision weight: the same z for x2 and cos; cold-only pools;
  the B3 TRIVIAL-only pool; hot/cold z inside each engine.

usage:
  break_check_b3_pilot.py pilot PILOTDIR      > pilot_summary.txt
  break_check_b3_pilot.py b3 LOGDIR           > b3_summary.txt
  break_check_b3_pilot.py compare PILOT_SUMMARY B3_SUMMARY
"""
import math
import os
import sys

PHI = (1 + math.sqrt(5)) / 2
LOGW = [math.log(4.0), 2 * math.log(PHI), -2 * math.log(PHI), -2 * math.log(PHI), 2 * math.log(PHI)]
X2 = [0.0, 5 - 2 * math.sqrt(5), 5 + 2 * math.sqrt(5), 5 + 2 * math.sqrt(5), 5 - 2 * math.sqrt(5)]
COS = [math.cos(2 * math.pi * k / 5) for k in range(5)]
OBS = ("logw", "x2", "cos")
CHAINS = (("cold", 1), ("cold", 2), ("hot", 1), ("hot", 2))
TRIV = 0.75


def batch_mean_se(vals, nb):
    size = len(vals) // nb
    bl = [sum(vals[i * size:(i + 1) * size]) / size for i in range(nb)]
    m = sum(bl) / nb
    var = sum((b - m) ** 2 for b in bl) / (nb - 1)
    return m, math.sqrt(var / nb), size * nb


def pool(chain_stats):
    k = len(chain_stats)
    m = sum(c[0] for c in chain_stats) / k
    se = math.sqrt(sum(c[1] ** 2 for c in chain_stats)) / k
    return m, se


def emit(tag, per_chain):
    """per_chain: {(start, rep): {obs: [values]}}"""
    for obs in OBS:
        stats = {}
        for key in CHAINS:
            vals = per_chain[key][obs]
            nb = 16 if tag == "pilot" else 20
            stats[key] = batch_mean_se(vals, nb)
            print("CHAIN %s %s%d %s n=%d mean=%.12f se=%.12f" % (tag, key[0], key[1], obs, stats[key][2], stats[key][0], stats[key][1]))
        allp = pool([stats[k] for k in CHAINS])
        cold = pool([stats[k] for k in CHAINS if k[0] == "cold"])
        hot = pool([stats[k] for k in CHAINS if k[0] == "hot"])
        print("POOL %s all %s mean=%.12f se=%.12f" % (tag, obs, allp[0], allp[1]))
        print("POOL %s cold %s mean=%.12f se=%.12f" % (tag, obs, cold[0], cold[1]))
        print("POOL %s hot %s mean=%.12f se=%.12f" % (tag, obs, hot[0], hot[1]))
        print("HOTCOLD %s %s z=%.4f" % (tag, obs, abs(hot[0] - cold[0]) / math.hypot(hot[1], cold[1])))


def pilot(d):
    per = {}
    for start, rep in CHAINS:
        fn = os.path.join(d, "L8_%s_r%d.log" % (start, rep))
        vals = {o: [] for o in OBS}
        with open(fn) as fh:
            for ln in fh:
                if not ln.startswith("SAMPLE "):
                    continue
                kv = dict(t.split("=", 1) for t in ln.split()[1:])
                cnt = [int(kv["flux_count_%d" % k]) for k in range(5)]
                tot = sum(cnt)
                assert tot == 6 * 8 ** 4, (fn, tot)
                vals["logw"].append(sum(c * w for c, w in zip(cnt, LOGW)) / tot)
                vals["x2"].append(sum(c * w for c, w in zip(cnt, X2)) / tot)
                vals["cos"].append(sum(c * w for c, w in zip(cnt, COS)) / tot)
        assert len(vals["logw"]) == 512, (fn, len(vals["logw"]))
        per[(start, rep)] = vals
    emit("pilot", per)


def b3(d):
    per, ptriv = {}, {}
    ntriv_total = 0
    for start, rep in CHAINS:
        fn = os.path.join(d, "TW_L8_%s%d.log" % (start, rep))
        vals = {o: [] for o in OBS}
        tv = {o: [] for o in OBS}
        with open(fn) as fh:
            for ln in fh:
                if not ln.startswith("M "):
                    continue
                kv = {k: float(v) for k, v in (t.split("=") for t in ln.split()[1:])}
                triv = max(abs(kv[k]) for k in ("fm01", "fm02", "fm03", "fm12", "fm13", "fm23")) < TRIV
                for o in OBS:
                    vals[o].append(kv[o])
                    if triv:
                        tv[o].append(kv[o])
        assert len(vals["logw"]) == 4000, (fn, len(vals["logw"]))
        per[(start, rep)] = vals
        ptriv[(start, rep)] = tv
        ntriv_total += len(tv["logw"])
        print("TRIVFRAC b3 %s%d %d/4000" % (start, rep, len(tv["logw"])))
    emit("b3", per)
    for o in OBS:
        allv = [v for k in CHAINS for v in ptriv[k][o]]
        nb = len(allv) // 200
        if nb >= 2:
            m, se, n = batch_mean_se(allv[: nb * 200], nb)
            print("POOL b3 trivial %s mean=%.12f se=%.12f n=%d" % (o, m, se, n))


def load(fn):
    out = {}
    with open(fn) as fh:
        for ln in fh:
            p = ln.split()
            if p and p[0] == "POOL":
                kv = dict(t.split("=") for t in p[4:])
                out[(p[2], p[3])] = (float(kv["mean"]), float(kv["se"]))
    return out


def compare(fp, fb):
    P, B = load(fp), load(fb)
    verdict = None
    for o in OBS:
        for grp in ("all", "cold"):
            a, b = P[(grp, o)], B[(grp, o)]
            z = abs(a[0] - b[0]) / math.hypot(a[1], b[1])
            role = "DECISION" if (o == "logw" and grp == "all") else "secondary"
            print("COMPARE %s %s pilot=%.8f+-%.8f b3=%.8f+-%.8f diff=%.8f z=%.4f %s"
                  % (o, grp, a[0], a[1], b[0], b[1], b[0] - a[0], z, role))
            if role == "DECISION":
                verdict = "CROSSCHECK_PASS" if z <= 4 else "CROSSCHECK_FAIL"
        if ("trivial", o) in B:
            a, b = P[("all", o)], B[("trivial", o)]
            z = abs(a[0] - b[0]) / math.hypot(a[1], b[1])
            print("COMPARE %s b3trivial_vs_pilotall pilot=%.8f b3=%.8f z=%.4f secondary" % (o, a[0], b[0], z))
    print("VERDICT %s" % verdict)


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "pilot":
        pilot(sys.argv[2])
    elif mode == "b3":
        b3(sys.argv[2])
    elif mode == "compare":
        compare(sys.argv[2], sys.argv[3])
    else:
        sys.exit("unknown mode")
