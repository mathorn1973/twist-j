#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify.py
candidate C-TT-VECTOR-MOMENT-UNDERDETERMINATION-2
authority: none. Incubation verifier. Audits written proofs at complete
finite scope; it is not itself the source of a computed status.

Exact arithmetic only. Coefficient field Q(zeta_5) on the basis
{1, z, z^2, z^3} with z^4 = -(1 + z + z^2 + z^3). Integer exponent arithmetic
in Z/5. No float literal and no float operation appears in this file.
Python standard library only. The engine design is shared with the -1
verifier by the same author; independence is supplied by the breaker.

Run:
  LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
      python3 verify.py
Exit 0 if every gate PASS, exit 1 otherwise.
"""

import sys
from fractions import Fraction
from itertools import product, combinations_with_replacement

N = 5
INV = {1: 1, 2: 3, 3: 2, 4: 4}
UNITS = (1, 2, 3, 4)

FAILS = []
GATES = 0


# ---------------------------------------------------------------- Q(zeta_5)

def red5(v):
    c = v[4]
    return (v[0] - c, v[1] - c, v[2] - c, v[3] - c)


ZERO = (Fraction(0),) * 4


def zpow(k):
    v = [Fraction(0)] * 5
    v[k % N] = Fraction(1)
    return red5(v)


ONE = zpow(0)


def qadd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def qsub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])


def qscale(s, a):
    return (s * a[0], s * a[1], s * a[2], s * a[3])


def qmul(a, b):
    A = [a[0], a[1], a[2], a[3], Fraction(0)]
    B = [b[0], b[1], b[2], b[3], Fraction(0)]
    out = [Fraction(0)] * 5
    for i in range(N):
        ai = A[i]
        if ai:
            for j in range(N):
                bj = B[j]
                if bj:
                    out[(i + j) % N] += ai * bj
    return red5(out)


def qfmt(a):
    return "[" + ",".join(str(x) for x in a) + "]"


def qint(n):
    return qscale(Fraction(n), ONE)


# ------------------------------------------------------------------- laws
# A configuration is a 5-tuple of (sign, exponent) with v_x = sign * z^exp.

def law_A():
    w = Fraction(1, N ** N)
    return [(w, tuple((1, t[x]) for x in range(N)))
            for t in product(range(N), repeat=N)]


def law_B(m):
    w = Fraction(1, N * 2 ** N)
    out = []
    for t0 in range(N):
        for eps in product((1, -1), repeat=N):
            out.append((w, tuple((eps[x], (t0 + m * x) % N) for x in range(N))))
    return out


def law_Bmix():
    out = []
    for m in (1, 2, 3, 4):
        for w, cfg in law_B(m):
            out.append((w / 4, cfg))
    return out


def law_dict(law):
    d = {}
    for w, cfg in law:
        d[cfg] = d.get(cfg, Fraction(0)) + w
    return {k: v for k, v in d.items() if v != 0}


# ------------------------------------------------------------ config maps

def act_tau(c, cfg):
    return tuple(cfg[(x - c) % N] for x in range(N))


def act_rho(u, cfg):
    ui = INV[u]
    return tuple(cfg[(ui * x) % N] for x in range(N))


def act_gamma(u, cfg):
    return tuple((s, (u * e) % N) for s, e in cfg)


def act_D(u, cfg):
    ui = INV[u]
    return tuple((cfg[(ui * x) % N][0], (u * cfg[(ui * x) % N][1]) % N)
                 for x in range(N))


def push(d, f):
    out = {}
    for cfg, w in d.items():
        c2 = f(cfg)
        out[c2] = out.get(c2, Fraction(0)) + w
    return {k: v for k, v in out.items() if v != 0}


# ------------------------------------------------------------- expectations

def expect(law, p, q):
    n = [p[x] - q[x] for x in range(N)]
    par = [(p[x] + q[x]) & 1 for x in range(N)]
    acc = [Fraction(0)] * N
    for w, cfg in law:
        sgn = 1
        e = 0
        for x in range(N):
            s, ex = cfg[x]
            if par[x] and s < 0:
                sgn = -sgn
            nx = n[x]
            if nx:
                e += nx * ex
        acc[e % N] += w if sgn > 0 else -w
    return red5(acc)


def unit(x, k=1):
    v = [0] * N
    v[x] = k
    return tuple(v)


ZV = (0,) * N


def spectrum_row(row):
    out = []
    for k in range(N):
        acc = ZERO
        for r in range(N):
            acc = qadd(acc, qmul(row[r], zpow((-k * r) % N)))
        out.append(acc)
    return out


# ------------------------------------------------------------------- gates

def gate(name, ok, detail=""):
    global GATES
    GATES += 1
    tag = "PASS" if ok else "FAIL"
    if not ok:
        FAILS.append(name)
    line = "CHECK %-52s %s" % (name, tag)
    if detail:
        line += "  " + detail
    print(line)


def monomials_of_degree(deg):
    for combo in combinations_with_replacement(range(2 * N), deg):
        p = [0] * N
        q = [0] * N
        for s in combo:
            if s < N:
                p[s] += 1
            else:
                q[s - N] += 1
        yield tuple(p), tuple(q)


# -------------------------------------------------------------------- main

def main():
    print("C-TT-VECTOR-MOMENT-UNDERDETERMINATION-2 verifier")
    print("family A, B_0..B_4, Bmix on Z/5 at a = 1, field Q(zeta_5)")
    print("elements printed as [c0,c1,c2,c3] meaning c0 + c1 z + c2 z^2 + c3 z^3")
    print("")

    laws = {"A": law_A()}
    for m in range(N):
        laws["B%d" % m] = law_B(m)
    laws["Bmix"] = law_Bmix()
    six = ["A", "B0", "B1", "B2", "B3", "B4"]
    dicts = {nm: law_dict(laws[nm]) for nm in laws}

    # -- supports
    gate("A.support.3125", len(dicts["A"]) == 3125, "n=%d" % len(dicts["A"]))
    okB = all(len(dicts["B%d" % m]) == 160 for m in range(N))
    gate("Bm.support.160.each", okB,
         "n=%s" % ",".join(str(len(dicts["B%d" % m])) for m in range(N)))
    gate("Bmix.support.640", len(dicts["Bmix"]) == 640,
         "n=%d" % len(dicts["Bmix"]))
    gate("weights.sum.1.all.seven",
         all(sum(dicts[nm].values()) == 1 for nm in dicts))

    # -- deterministic pointwise modulus
    okmod = all(s in (1, -1)
                for nm in six for cfg in dicts[nm] for s, e in cfg)
    gate("pointwise.modulus.one.all.six", okmod)

    # -- P5 composition claim on every configuration of every law
    okc = True
    for nm in dicts:
        for cfg in dicts[nm]:
            for u in UNITS:
                a = act_D(u, cfg)
                b = act_gamma(u, act_rho(u, cfg))
                c = act_rho(u, act_gamma(u, cfg))
                if a != b or a != c:
                    okc = False
    gate("P5.composition.D.eq.gamma.rho.eq.rho.gamma", okc)

    # -- P5 action table as measure equalities
    okt = all(push(dicts[nm], lambda cc, c=c: act_tau(c, cc)) == dicts[nm]
              for nm in dicts for c in range(N))
    gate("P5.tau.invariance.all.seven", okt)

    n_rho = 0
    for u in UNITS:
        for m in range(N):
            tgt = "B%d" % ((INV[u] * m) % N)
            if push(dicts["B%d" % m],
                    lambda cc, u=u: act_rho(u, cc)) == dicts[tgt]:
                n_rho += 1
    gate("P5.rho.orbit.Bm.to.B.uinv.m.20of20", n_rho == 20, "ok=%d" % n_rho)
    gate("P5.rho.fixes.A",
         all(push(dicts["A"], lambda cc, u=u: act_rho(u, cc)) == dicts["A"]
             for u in UNITS))
    gate("P5.rho.fixes.Bmix",
         all(push(dicts["Bmix"], lambda cc, u=u: act_rho(u, cc))
             == dicts["Bmix"] for u in UNITS))

    n_gam = 0
    for u in UNITS:
        for m in range(N):
            tgt = "B%d" % ((u * m) % N)
            if push(dicts["B%d" % m],
                    lambda cc, u=u: act_gamma(u, cc)) == dicts[tgt]:
                n_gam += 1
    gate("P5.gamma.orbit.Bm.to.B.um.20of20", n_gam == 20, "ok=%d" % n_gam)
    gate("P5.gamma.fixes.A",
         all(push(dicts["A"], lambda cc, u=u: act_gamma(u, cc)) == dicts["A"]
             for u in UNITS))
    gate("P5.gamma.fixes.Bmix",
         all(push(dicts["Bmix"], lambda cc, u=u: act_gamma(u, cc))
             == dicts["Bmix"] for u in UNITS))

    n_D = 0
    for u in UNITS:
        for nm in dicts:
            if push(dicts[nm], lambda cc, u=u: act_D(u, cc)) == dicts[nm]:
                n_D += 1
    gate("P5.diagonal.fixes.every.law.28of28", n_D == 28, "ok=%d" % n_D)

    # -- second-order data for all six
    ok2 = True
    for nm in six:
        L = laws[nm]
        if any(expect(L, unit(x), ZV) != ZERO for x in range(N)):
            ok2 = False
        for x in range(N):
            for y in range(N):
                want = ONE if x == y else ZERO
                if expect(L, unit(x), unit(y)) != want:
                    ok2 = False
                pxy = [0] * N
                pxy[x] += 1
                pxy[y] += 1
                if expect(L, tuple(pxy), ZV) != ZERO:
                    ok2 = False
    gate("P1.mean0.C.delta.P.zero.all.six", ok2)

    # -- P4 spectra of the squared readout
    peaks = []
    okA = None
    for nm in six + ["Bmix"]:
        L = laws[nm]
        row = [expect(L, unit(r, 2), unit(0, 2)) for r in range(N)]
        Sw = spectrum_row(row)
        prow = []
        for r in range(N):
            pp = [0] * N
            pp[r] += 2
            pp[0] += 2
            prow.append(expect(L, tuple(pp), ZV))
        Piw = spectrum_row(prow)
        gate("P4.Pi_w.zero.%s" % nm, all(s == ZERO for s in Piw))
        if nm == "A":
            okA = all(s == ONE for s in Sw)
            gate("P4.S_w.A.flat.one", okA)
        elif nm == "Bmix":
            five4 = qscale(Fraction(5, 4), ONE)
            okX = Sw[0] == ZERO and all(Sw[k] == five4 for k in UNITS)
            gate("P4.S_w.Bmix.5over4.off.zero", okX)
            print("  S_w Bmix = " + " ".join(qfmt(s) for s in Sw))
        else:
            m = int(nm[1])
            pk = (2 * m) % N
            okm = Sw[pk] == qint(5) and all(Sw[k] == ZERO
                                            for k in range(N) if k != pk)
            gate("P4.S_w.%s.5.delta.k.%d" % (nm, pk), okm)
            peaks.append(pk)
    gate("P5.peak.table.2m", peaks == [(2 * m) % N for m in range(N)],
         "peaks=%s" % ",".join(str(x) for x in peaks))
    gate("P5.inverse.map.m.equals.3k0",
         [(3 * k0) % N for k0 in range(N)] == [0, 3, 1, 4, 2])
    print("")

    # -- monomial sweeps, degrees <= 3, 4, 5, over the six laws
    vals = {}   # (deg, p, q) -> dict law -> value
    counts = {}
    for deg in range(6):
        cnt = 0
        for p, q in monomials_of_degree(deg):
            cnt += 1
            vals[(p, q)] = {nm: expect(laws[nm], p, q) for nm in six}
        counts[deg] = cnt
    gate("count.deg.le3.286", sum(counts[d] for d in range(4)) == 286,
         "n=%d" % sum(counts[d] for d in range(4)))
    gate("count.deg.4.715", counts[4] == 715, "n=%d" % counts[4])
    gate("count.deg.5.2002", counts[5] == 2002, "n=%d" % counts[5])

    # P1 across all six at degree <= 3
    bad = 0
    for deg in range(4):
        for p, q in monomials_of_degree(deg):
            V = vals[(p, q)]
            ref = V["A"]
            if any(V[nm] != ref for nm in six):
                bad += 1
    gate("P1.family.agreement.deg.le3", bad == 0, "separators=%d" % bad)

    # P2 and P3 at degree 4
    twenty = set()
    for x in range(N):
        for y in range(N):
            if x != y:
                twenty.add((unit(x, 2), unit(y, 2)))
    pairs = [(a, b) for i, a in enumerate(six) for b in six[i + 1:]]
    okP2 = True
    detail = []
    for a, b in pairs:
        seps = set()
        for p, q in monomials_of_degree(4):
            V = vals[(p, q)]
            if V[a] != V[b]:
                seps.add((p, q))
        detail.append(len(seps))
        if seps != twenty:
            okP2 = False
    gate("P2.universal.separator.set.15.pairs", okP2,
         "sizes=%s" % ",".join(str(x) for x in detail))

    okP3 = True
    for x in range(N):
        for y in range(N):
            if x == y:
                for nm in six:
                    if vals[(unit(x, 2), unit(x, 2))][nm] != ONE:
                        okP3 = False
                continue
            key = (unit(x, 2), unit(y, 2))
            if vals[key]["A"] != ZERO:
                okP3 = False
            for m in range(N):
                if vals[key]["B%d" % m] != zpow((2 * m * (x - y)) % N):
                    okP3 = False
    gate("P3.value.table.z.2m.xminusy", okP3)

    # P6 at degree 5
    tens = set()
    for x in range(N):
        tens.add((unit(x, 5), ZV))
        tens.add((ZV, unit(x, 5)))
    okP6a = True
    for m in range(N):
        seps = set()
        okvals = True
        for p, q in monomials_of_degree(5):
            V = vals[(p, q)]
            if V["A"] != V["B%d" % m]:
                seps.add((p, q))
                if V["A"] != ONE or V["B%d" % m] != ZERO:
                    okvals = False
        if seps != tens or not okvals:
            okP6a = False
    gate("P6.deg5.A.vs.Bm.exactly.ten.fifth.powers", okP6a)
    okP6b = True
    for i in range(N):
        for j in range(i + 1, N):
            for p, q in monomials_of_degree(5):
                V = vals[(p, q)]
                if V["B%d" % i] != V["B%d" % j]:
                    okP6b = False
    gate("P6.deg5.no.separator.between.B.laws", okP6b)

    # P7 fourth moment and cumulant, family wide
    okP7 = True
    for nm in six:
        L = laws[nm]
        m4 = expect(L, unit(0, 2), unit(0, 2))
        C00 = expect(L, unit(0), unit(0))
        P00_ = [0] * N
        P00_[0] = 2
        P00 = expect(L, tuple(P00_), ZV)
        K = qsub(qsub(m4, qmul(P00, P00)),
                 qscale(Fraction(2), qmul(C00, C00)))
        if m4 != ONE or K != qint(-1):
            okP7 = False
    gate("P7.abs.v4.one.and.K.minus.one.all.six", okP7)

    print("")
    print("SUMMARY gates=%d fails=%d" % (GATES, len(FAILS)))
    if FAILS:
        for f in FAILS:
            print("FAILED %s" % f)
        print("VERDICT FAIL")
        return 1
    print("VERDICT PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
