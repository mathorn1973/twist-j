#!/usr/bin/env python3
# P-ENTROPY-BRIDGE-1 exact verifier. TWIST-J public kernel, Thue-Morse
# drive, frozen joint Cesaro law, lift defect, and cut depth necessity.
# Exact integer and Fraction arithmetic, standard library only, no float
# in any assertion. See PREREG.md in this directory for the frozen
# decision surface; gates G01 to G16.

import sys
from fractions import Fraction

S_VEC = (2, 1, 2, 1)
U_VEC = (0, 1, 0, -1)
C_D = (2, 1, 3, 4, 1, 1)
V_E = (0, 0, 0, 0, 1, 0)


def gen_a(x):
    p1, p4, p1p, p4p, q, r = x
    return (p4, p1, p4p, p1p, q, r)


def gen_b(x):
    p1, p4, p1p, p4p, q, r = x
    return ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5,
            (-q) % 5, (-r) % 5)


def gen_c(x):
    p1, p4, p1p, p4p, q, r = x
    b4 = ((-p1p) % 5, (-p4p) % 5, (-p1) % 5, (-p4) % 5)
    return ((b4[0] + S_VEC[0] + r * U_VEC[0]) % 5,
            (b4[1] + S_VEC[1] + r * U_VEC[1]) % 5,
            (b4[2] + S_VEC[2] + r * U_VEC[2]) % 5,
            (b4[3] + S_VEC[3] + r * U_VEC[3]) % 5,
            (1 - q) % 5, (-r) % 5)


def gen_d(x):
    return tuple((C_D[i] - x[i]) % 5 for i in range(6))


def gen_e(x):
    return tuple(((C_D[i] + V_E[i]) - x[i]) % 5 for i in range(6))


GENS = (gen_a, gen_b, gen_c, gen_d, gen_e)


def dec(i):
    out = []
    for _ in range(6):
        out.append(i % 5)
        i //= 5
    return tuple(out)


def enc(x):
    i = 0
    for k in range(5, -1, -1):
        i = i * 5 + x[k]
    return i


N = 15625
STATES = [dec(i) for i in range(N)]
ZTAB = [sum(s) % 5 for s in STATES]

CHECKS = []


def check(name, ok):
    CHECKS.append((name, bool(ok)))


def table(f):
    return tuple(enc(f(s)) for s in STATES)


def compose_tab(f, g):
    # (f o g)[i] = f[g[i]]
    return tuple(f[g[i]] for i in range(N))


def aff_compose(f, g):
    # integer affine maps x -> A x + t on Z^6; returns f o g
    A, t = f
    B, u = g
    C = [[sum(A[i][k] * B[k][j] for k in range(6)) for j in range(6)]
         for i in range(6)]
    v = [sum(A[i][k] * u[k] for k in range(6)) + t[i] for i in range(6)]
    return (C, v)


def det_bareiss(M):
    M = [row[:] for row in M]
    n = len(M)
    sign = 1
    prev = 1
    for i in range(n - 1):
        if M[i][i] == 0:
            sw = None
            for rr in range(i + 1, n):
                if M[rr][i] != 0:
                    sw = rr
                    break
            if sw is None:
                return 0
            M[i], M[sw] = M[sw], M[i]
            sign = -sign
        for rr in range(i + 1, n):
            for cc in range(i + 1, n):
                M[rr][cc] = (M[rr][cc] * M[i][i]
                             - M[rr][i] * M[i][cc]) // prev
        prev = M[i][i]
    return sign * M[n - 1][n - 1]


def main():
    # ---- G01 relations on the shadow ----
    A, B, C, D, E = (table(g) for g in GENS)
    IDT = tuple(range(N))
    ok = all(compose_tab(T, T) == IDT for T in (A, B, C, D, E))
    BC = compose_tab(C, B)  # bc(s) = gen_c(gen_b(s))
    BC5 = compose_tab(BC, compose_tab(BC, compose_tab(
        BC, compose_tab(BC, BC))))
    ok = ok and BC5 == IDT
    check("G01 RELATIONS      involutions and (bc)^5 = id on F_5^6", ok)

    # ---- G02 the lift defect over Z ----
    Bm = [[0, 0, -1, 0, 0, 0], [0, 0, 0, -1, 0, 0], [-1, 0, 0, 0, 0, 0],
          [0, -1, 0, 0, 0, 0], [0, 0, 0, 0, -1, 0], [0, 0, 0, 0, 0, -1]]
    bZ = (Bm, [0] * 6)
    Cm = [[0, 0, -1, 0, 0, U_VEC[0]], [0, 0, 0, -1, 0, U_VEC[1]],
          [-1, 0, 0, 0, 0, U_VEC[2]], [0, -1, 0, 0, 0, U_VEC[3]],
          [0, 0, 0, 0, -1, 0], [0, 0, 0, 0, 0, -1]]
    cZ = (Cm, [S_VEC[0], S_VEC[1], S_VEC[2], S_VEC[3], 1, 0])
    bcZ = aff_compose(cZ, bZ)
    p = bcZ
    for _ in range(4):
        p = aff_compose(p, bcZ)
    A5, t5 = p
    dm = [[A5[i][j] - (1 if i == j else 0) for j in range(6)]
          for i in range(6)]
    defect_ok = (t5 == [10, 5, 10, 5, 5, 0]
                 and dm[1][5] == -5 and dm[3][5] == 5
                 and all(dm[i][j] == 0 for i in range(6) for j in range(6)
                         if not (j == 5 and i in (1, 3))))
    nonzero = any(v != 0 for v in t5) or any(
        dm[i][j] != 0 for i in range(6) for j in range(6))
    mod5zero = (all(v % 5 == 0 for v in t5)
                and all(dm[i][j] % 5 == 0 for i in range(6)
                        for j in range(6)))
    check("G02 LIFT-DEFECT    (bc)^5 = x + (10, 5-5r, 10, 5+5r, 5, 0)"
          " over Z; nonzero; zero mod 5", defect_ok and nonzero and mod5zero)

    # ---- G03 unit facts ----
    MJ = [[1, 0, -1, 1], [0, 1, -1, 0], [1, 0, 0, 0], [0, 1, -1, 1]]
    check("G03 UNIT           det(M_J) = 1; J == 2 (unit) at the ramified"
          " place", det_bareiss(MJ) == 1 and (1 + 1 * 1) % 5 == 2)

    # ---- census: warmup 400, window 300, closure ----
    F = [[0] * N, [0] * N]
    for t in (0, 1):
        gt = [GENS[(z + 2 * t) % 5] for z in range(5)]
        Ft = F[t]
        for i in range(N):
            Ft[i] = enc(gt[ZTAB[i]](STATES[i]))
    NT = 2049
    tm = [bin(n).count("1") & 1 for n in range(NT)]
    warm = [F[tm[n]] for n in range(400)]
    wind = [F[tm[n]] for n in range(400, 700)]
    sigs = {}
    basins = {}
    for seed in range(N):
        s = seed
        for T in warm:
            s = T[s]
        w1 = set()
        for T in wind:
            w1.add(s)
            s = T[s]
        sig = frozenset(w1)
        if sig not in sigs:
            sigs[sig] = len(sigs)
        basins[sig] = basins.get(sig, 0) + 1
    atts = list(sigs)

    check("G04 COUNT-313      313 attractors", len(atts) == 313)

    sizes = {}
    support = set()
    total = 0
    for sig in atts:
        sizes[len(sig)] = sizes.get(len(sig), 0) + 1
        support |= sig
        total += len(sig)
    check("G05 SIZES          312 of size 20, 1 of size 10; support 6250"
          " disjoint", sizes == {20: 312, 10: 1} and total == 6250
          and len(support) == 6250)

    bh = {}
    for sig in atts:
        bh[basins[sig]] = bh.get(basins[sig], 0) + 1
    check("G06 BASINS         312 basins of 50, 1 basin of 25;"
          " coverage 15625",
          bh == {50: 312, 25: 1} and sum(basins.values()) == N)

    fired = set()
    for i in support:
        for t in (0, 1):
            fired.add((ZTAB[i] + 2 * t) % 5)
    check("G07 SHEET          z in {1, 4} on the support; only b, d, e"
          " fire", all(ZTAB[i] in (1, 4) for i in support)
          and fired <= {1, 3, 4})

    closed = all(all(F[0][i] in sig and F[1][i] in sig for i in sig)
                 for sig in atts)
    check("G08 CLOSED-BOTH    every signature closed under both branches",
          closed)

    check("G09 ANCHOR-312     (5^4 - 1)/2 = 312; 312*(2/625) + 1/625 = 1",
          (5 ** 4 - 1) // 2 == 312
          and 312 * Fraction(2, 625) + Fraction(1, 625) == 1)

    # ---- G10 branch indegree on the recurrent support ----
    R = sorted(support)
    Rset = support
    ok = True
    tot = {}
    for t in (0, 1):
        indeg = {}
        for i in R:
            j = F[t][i]
            indeg[j] = indeg.get(j, 0) + 1
            tot[j] = tot.get(j, 0) + 1
        hist = {}
        for i in R:
            v = indeg.get(i, 0)
            hist[v] = hist.get(v, 0) + 1
        ok = ok and hist == {0: 3125, 2: 3125}
    ok = ok and all(tot.get(i, 0) == 2 for i in R)
    check("G10 INDEGREE       each branch {0: 3125, 2: 3125} on the"
          " support; total exactly 2 per state", ok)

    # ---- joint Cesaro transport, frozen window W = [512, 2048) ----
    comp_of = {}
    for k, sig in enumerate(atts):
        for s in sig:
            comp_of[s] = k
    w = [1] * N
    occ = [0] * N
    occ_mid = None
    letters = {}
    pair00 = 0
    cm512 = None
    mass_on_R = False
    W0, W1, MID = 512, 2048, 1024
    # phase 1: n in [0, W0), full range with a mass guard
    for n in range(W0):
        nw = [0] * N
        Ft = F[tm[n]]
        for i in range(N):
            wi = w[i]
            if wi:
                nw[Ft[i]] += wi
        w = nw
    # boundary n = W0: component masses and support location
    cm = {}
    total_on_R = 0
    off_R = 0
    for i in range(N):
        wi = w[i]
        if wi:
            k = comp_of.get(i)
            if k is None:
                off_R += wi
            else:
                cm[k] = cm.get(k, 0) + wi
                total_on_R += wi
    mass_on_R = (off_R == 0 and total_on_R == N)
    if mass_on_R:
        cm512 = {}
        for v in cm.values():
            cm512[v] = cm512.get(v, 0) + 1
    # phase 2: n in [W0, W1), iterate the recurrent support only (valid
    # because mass_on_R is checked; if it failed, the gates below fail)
    ITER = R if mass_on_R else list(range(N))
    for n in range(W0, W1):
        th = tm[n]
        for i in ITER:
            wi = w[i]
            if wi:
                occ[i] += wi
                sel = (ZTAB[i] + 2 * th) % 5
                letters[sel] = letters.get(sel, 0) + wi
        if th == 0 and tm[n + 1] == 0:
            pair00 += 1
        nw = [0] * N
        Ft = F[th]
        for i in ITER:
            wi = w[i]
            if wi:
                nw[Ft[i]] += wi
        w = nw
        if n + 1 == MID:
            occ_mid = occ[:]

    check("G11 COMPONENT-MASS at n = 512 mass per component = basin size:"
          " {50: 312, 25: 1}", cm512 == {50: 312, 25: 1})

    unit = (1536 * N) // 6250  # 3840
    ok = all(occ[i] == unit for i in R) and all(
        occ[i] == 0 for i in range(N) if i not in Rset)
    check("G12 OCCUPATION     occupation over [512, 2048) is exactly"
          " 3840 per recurrent state and 0 elsewhere", ok)

    def maxdist(vec, T):
        worst = Fraction(0)
        for sig in atts:
            m = sum(vec[s] for s in sig)
            if m == 0:
                return None
            L = len(sig)
            d = Fraction(0)
            for s in sig:
                d += abs(Fraction(vec[s], m) - Fraction(1, L))
            if d > worst:
                worst = d
        return worst

    d_mid = maxdist(occ_mid, MID - W0)
    d_end = maxdist(occ, W1 - W0)
    check("G13 LADDER-1024    max within-component L1 distance: exactly"
          " 1/256 at N = 1024 and exactly 0 at N = 2048",
          d_mid == Fraction(1, 256) and d_end == 0)

    check("G14 LETTERS        letter masses on W exactly b = 16000000,"
          " d = 4000000, e = 4000000; ratios (2/3, 1/6, 1/6)",
          letters == {1: 16000000, 3: 4000000, 4: 4000000}
          and Fraction(letters.get(1, 0), 24000000) == Fraction(2, 3)
          and Fraction(letters.get(3, 0), 24000000) == Fraction(1, 6)
          and Fraction(letters.get(4, 0), 24000000) == Fraction(1, 6))

    check("G15 PAIR00         theta pair (0,0) count on W exactly"
          " 256 = 1536/6", pair00 == 256)

    # ---- G16 cut depth necessity ----
    tmL = [bin(n).count("1") & 1 for n in range(1 << 15)]

    def ptm(L):
        seen = set()
        for i in range(len(tmL) - L):
            seen.add(tuple(tmL[i:i + L]))
        return len(seen)

    p3, p4 = ptm(3), ptm(4)
    need = -(-6250 // 625)  # ceil = 10
    check("G16 DEPTH          p_TM(3) = 6 < 10 <= p_TM(4) = 10: TM-depth"
          " K >= 4 necessary at lambda-depth 4",
          p3 == 6 and p4 == 10 and need == 10 and p3 < need <= p4)

    print("P-ENTROPY-BRIDGE-1 exact verifier")
    print("public kernel F_5^6; five involutions; Thue-Morse drive;")
    print("selector i = (z + 2 theta) mod 5; census warmup 400 window 300;")
    print("joint Cesaro transport, frozen window [512, 2048); integer")
    print("occupation, exact equalities only; lift defect over Z; cut")
    print("depth necessity")
    print()
    passed = 0
    for i, (name, ok) in enumerate(CHECKS, 1):
        tag = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print("%s %02d %s" % (tag, i, name))
    print()
    print("RESULT %d/%d %s" % (passed, len(CHECKS),
                               "ALL PASS" if passed == len(CHECKS)
                               else "FAILURES PRESENT"))
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
