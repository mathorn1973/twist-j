#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify.py
candidate C-TT-VECTOR-MOMENT-UNDERDETERMINATION-1
target line on promotion: mathorn1973/twist-j main, child probe
authority: none. Incubation verifier. Audits a written proof at complete
finite scope; it is not itself the source of a computed status.

Exact arithmetic only. Coefficient field Q(zeta_5) on the basis
{1, z, z^2, z^3} with z^4 = -(1 + z + z^2 + z^3). Integer exponent arithmetic
in Z/5. No float literal and no float operation appears in this file.
Python standard library only.

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

FAILS = []
GATES = 0


# ---------------------------------------------------------------- Q(zeta_5)

def red5(v):
    """v: length-5 list of Fraction, coeffs of z^0..z^4. Canonical 4-tuple."""
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


def rho(u, cfg):
    ui = INV[u]
    return tuple(cfg[(ui * x) % N] for x in range(N))


def tau(c, cfg):
    return tuple(cfg[(x - c) % N] for x in range(N))


# ------------------------------------------------------------- expectations

def expect(law, p, q):
    """E[ prod_x v_x^{p_x} conj(v_x)^{q_x} ] exactly, as a Q(zeta_5) element."""
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


def addv(a, b):
    return tuple(a[i] + b[i] for i in range(N))


ZV = (0,) * N


def mat_C(law):
    return [[expect(law, unit(x), unit(y)) for y in range(N)] for x in range(N)]


def mat_P(law):
    return [[expect(law, addv(unit(x), unit(y)), ZV) for y in range(N)]
            for x in range(N)]


def mat_Cw(law):
    return [[expect(law, unit(x, 2), unit(y, 2)) for y in range(N)]
            for x in range(N)]


def mat_Pw(law):
    return [[expect(law, addv(unit(x, 2), unit(y, 2)), ZV) for y in range(N)]
            for x in range(N)]


def spectrum(mat):
    """S(k) = sum_r mat[r][0] z^{-k r}. Requires translation invariance."""
    out = []
    for k in range(N):
        acc = ZERO
        for r in range(N):
            acc = qadd(acc, qmul(mat[r][0], zpow((-k * r) % N)))
        out.append(acc)
    return out


# ------------------------------------------------------------------- gates

def gate(name, ok, detail=""):
    global GATES
    GATES += 1
    tag = "PASS" if ok else "FAIL"
    if not ok:
        FAILS.append(name)
    line = "CHECK %-46s %s" % (name, tag)
    if detail:
        line += "  " + detail
    print(line)


def is_delta(mat):
    for x in range(N):
        for y in range(N):
            want = ONE if x == y else ZERO
            if mat[x][y] != want:
                return False
    return True


def is_zero(mat):
    return all(mat[x][y] == ZERO for x in range(N) for y in range(N))


def is_allones(mat):
    return all(mat[x][y] == ONE for x in range(N) for y in range(N))


def transl_inv(mat):
    for x in range(N):
        for y in range(N):
            if mat[x][y] != mat[(x - y) % N][0]:
                return False
    return True


# -------------------------------------------------------------------- main

def main():
    print("C-TT-VECTOR-MOMENT-UNDERDETERMINATION-1 verifier")
    print("carrier X = Z/5, scale a = 1, field Q(zeta_5) basis {1,z,z^2,z^3}")
    print("elements printed as [c0,c1,c2,c3] meaning c0 + c1 z + c2 z^2 + c3 z^3")
    print("")

    A = law_A()
    B0 = law_B(0)
    Bm = {m: law_B(m) for m in (1, 2, 3, 4)}
    BX = law_Bmix()

    dA, dB0, dBX = law_dict(A), law_dict(B0), law_dict(BX)
    dBm = {m: law_dict(Bm[m]) for m in (1, 2, 3, 4)}

    # -- support and normalization
    gate("A.support.3125", len(dA) == 3125, "n=%d" % len(dA))
    gate("B0.support.160", len(dB0) == 160, "n=%d" % len(dB0))
    gate("Bmix.support.640", len(dBX) == 640, "n=%d" % len(dBX))
    gate("A.weights.sum.1", sum(dA.values()) == 1)
    gate("B0.weights.sum.1", sum(dB0.values()) == 1)
    gate("Bmix.weights.sum.1", sum(dBX.values()) == 1)

    # -- deterministic pointwise modulus, |v_x| = 1 by construction
    modA = all(s in (1, -1) for cfg in dA for s, e in cfg)
    modB = all(s in (1, -1) for cfg in dB0 for s, e in cfg)
    gate("A.pointwise.modulus.one", modA)
    gate("B0.pointwise.modulus.one", modB)

    # -- F3, invariance as measures
    for nm, d in (("A", dA), ("B0", dB0), ("Bmix", dBX)):
        ok = all({tau(c, k): v for k, v in d.items()} == d for c in range(N))
        gate("%s.translation.invariant" % nm, ok)
        ok = all({rho(u, k): v for k, v in d.items()} == d for u in (1, 2, 3, 4))
        gate("%s.rho.invariant" % nm, ok)

    # -- F6, individual B_m for m != 0 must NOT be rho invariant
    for m in (1, 2, 3, 4):
        d = dBm[m]
        broken = any({rho(u, k): v for k, v in d.items()} != d
                     for u in (2, 3, 4))
        gate("B%d.rho.NOT.invariant" % m, broken)
        okt = all({tau(c, k): v for k, v in d.items()} == d for c in range(N))
        gate("B%d.translation.invariant" % m, okt)

    # -- F2, second order data
    CA, CB = mat_C(A), mat_C(B0)
    PA, PB = mat_P(A), mat_P(B0)
    meanA = [expect(A, unit(x), ZV) for x in range(N)]
    meanB = [expect(B0, unit(x), ZV) for x in range(N)]
    gate("A.mean.zero", all(m == ZERO for m in meanA))
    gate("B0.mean.zero", all(m == ZERO for m in meanB))
    gate("A.C.equals.delta", is_delta(CA))
    gate("B0.C.equals.delta", is_delta(CB))
    gate("A.P.equals.zero", is_zero(PA))
    gate("B0.P.equals.zero", is_zero(PB))
    gate("A.C.translation.invariant", transl_inv(CA))
    gate("B0.C.translation.invariant", transl_inv(CB))

    SA, SB = spectrum(CA), spectrum(CB)
    PiA, PiB = spectrum(PA), spectrum(PB)
    gate("A.S_v.equals.one", all(s == ONE for s in SA))
    gate("B0.S_v.equals.one", all(s == ONE for s in SB))
    gate("A.Pi_v.equals.zero", all(s == ZERO for s in PiA))
    gate("B0.Pi_v.equals.zero", all(s == ZERO for s in PiB))
    print("  S_v(k) A  = " + " ".join(qfmt(s) for s in SA))
    print("  S_v(k) B0 = " + " ".join(qfmt(s) for s in SB))
    print("")

    # -- F2, squared image w = v^2
    CwA, CwB = mat_Cw(A), mat_Cw(B0)
    PwA, PwB = mat_Pw(A), mat_Pw(B0)
    gate("A.Cw.equals.delta", is_delta(CwA))
    gate("B0.Cw.equals.allones", is_allones(CwB))
    gate("A.Cw.translation.invariant", transl_inv(CwA))
    gate("B0.Cw.translation.invariant", transl_inv(CwB))
    SwA, SwB = spectrum(CwA), spectrum(CwB)
    PiwA, PiwB = spectrum(PwA), spectrum(PwB)
    gate("A.S_w.equals.one.all.k", all(s == ONE for s in SwA))
    gate("B0.S_w.equals.5.delta.k0",
         SwB[0] == qint(5) and all(SwB[k] == ZERO for k in (1, 2, 3, 4)))
    gate("A.Pi_w.equals.zero", all(s == ZERO for s in PiwA))
    gate("B0.Pi_w.equals.zero", all(s == ZERO for s in PiwB))
    print("  S_w(k) A  = " + " ".join(qfmt(s) for s in SwA))
    print("  S_w(k) B0 = " + " ".join(qfmt(s) for s in SwB))
    print("")

    # -- F6, control family spectra
    for m in (1, 2, 3, 4):
        Sm = spectrum(mat_Cw(Bm[m]))
        peak = (2 * m) % N
        ok = Sm[peak] == qint(5) and all(Sm[k] == ZERO
                                         for k in range(N) if k != peak)
        gate("B%d.S_w.equals.5.delta.k.%d" % (m, peak), ok)
    SwX = spectrum(mat_Cw(BX))
    five4 = qscale(Fraction(5, 4), ONE)
    ok = SwX[0] == ZERO and all(SwX[k] == five4 for k in (1, 2, 3, 4))
    gate("Bmix.S_w.equals.5over4.off.zero", ok)
    print("  S_w(k) Bmix = " + " ".join(qfmt(s) for s in SwX))
    print("")

    # -- F4, fixed modulus versus Wick closure
    for nm, law, C, P in (("A", A, CA, PA), ("B0", B0, CB, PB)):
        m4 = expect(law, unit(0, 2), unit(0, 2))
        wick = qadd(qmul(P[0][0], P[0][0]), qscale(Fraction(2),
                                                   qmul(C[0][0], C[0][0])))
        gate("%s.E.abs.v4.equals.one" % nm, m4 == ONE, qfmt(m4))
        gate("%s.wick.value.equals.two" % nm, wick == qint(2), qfmt(wick))
        gate("%s.wick.NOGO.gap.minus.one" % nm, qsub(m4, wick) == qint(-1))

    # -- fourth cumulant K
    def cum(law, C, P):
        K = []
        for x in range(N):
            row = []
            for y in range(N):
                m = expect(law, unit(x, 2), unit(y, 2))
                t = qsub(m, qmul(P[x][x], P[y][y]))
                row.append(qsub(t, qscale(Fraction(2), qmul(C[x][y], C[x][y]))))
            K.append(row)
        return K

    KA, KB = cum(A, CA, PA), cum(B0, CB, PB)
    okA = all(KA[x][y] == (qint(-1) if x == y else ZERO)
              for x in range(N) for y in range(N))
    okB = all(KB[x][y] == (qint(-1) if x == y else ONE)
              for x in range(N) for y in range(N))
    gate("A.K.equals.minus.delta", okA)
    gate("B0.K.equals.one.minus.2delta", okB)
    diff = all(qsub(KB[x][y], KA[x][y]) == (ZERO if x == y else ONE)
               for x in range(N) for y in range(N))
    gate("K.difference.is.offdiagonal.one", diff)
    print("")

    # -- F1, exhaustive sweep of every monomial of total degree <= 3
    seps_le3 = []
    count_le3 = 0
    for deg in range(4):
        for combo in combinations_with_replacement(range(2 * N), deg):
            p = [0] * N
            q = [0] * N
            for s in combo:
                if s < N:
                    p[s] += 1
                else:
                    q[s - N] += 1
            count_le3 += 1
            ea = expect(A, tuple(p), tuple(q))
            eb = expect(B0, tuple(p), tuple(q))
            if ea != eb:
                seps_le3.append((tuple(p), tuple(q), ea, eb))
    gate("monomials.degree.le3.count.286", count_le3 == 286,
         "n=%d" % count_le3)
    gate("F1.no.separator.at.degree.le3", len(seps_le3) == 0,
         "separators=%d" % len(seps_le3))

    # -- F5, exhaustive sweep at total degree exactly 4
    seps4 = []
    count4 = 0
    for combo in combinations_with_replacement(range(2 * N), 4):
        p = [0] * N
        q = [0] * N
        for s in combo:
            if s < N:
                p[s] += 1
            else:
                q[s - N] += 1
        count4 += 1
        ea = expect(A, tuple(p), tuple(q))
        eb = expect(B0, tuple(p), tuple(q))
        if ea != eb:
            seps4.append((tuple(p), tuple(q), ea, eb))
    gate("monomials.degree.4.count.715", count4 == 715, "n=%d" % count4)

    predicted = set()
    for x in range(N):
        for y in range(N):
            if x != y:
                predicted.add((unit(x, 2), unit(y, 2)))
    found = set((p, q) for p, q, ea, eb in seps4)
    gate("F5.degree4.separator.count.20", len(seps4) == 20,
         "n=%d" % len(seps4))
    gate("F5.degree4.separator.set.is.v2conjv2", found == predicted)
    okval = all(ea == ZERO and eb == ONE for p, q, ea, eb in seps4)
    gate("F5.degree4.separator.values.0.and.1", okval)

    # -- minimal separating degree is exactly 4
    gate("S1.iv.minimal.separating.degree.is.4",
         len(seps_le3) == 0 and len(seps4) == 20)

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
