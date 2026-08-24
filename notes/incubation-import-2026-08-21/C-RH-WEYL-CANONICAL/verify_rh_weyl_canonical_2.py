#!/usr/bin/env python3
# verify_rh_weyl_canonical_2.py
# P-RH-WEYL-CANONICAL-2: exact rank-two threshold map w*(x, delta;
# design, m) on the free Jacobi model, four frozen node designs, m to
# 24, R = 64 background. Exact arithmetic in every assertion (Fraction,
# Q(i) pairs). Detection = strictly negative block quadratic; zero is
# boundary. See PREREG-P-RH-WEYL-CANONICAL-2.md; frozen before first
# execution. Exit 0 iff all checks pass.
import sys
from fractions import Fraction as Fr

CHECKS = []


def report(name, ok):
    CHECKS.append((name, ok))
    print("%s %s" % (name, "PASS" if ok else "FAIL"))


def dec6(fr):
    n = fr.numerator
    d = fr.denominator
    if n == 0:
        return "0"
    sgn = "-" if n < 0 else "+"
    n = abs(n)
    shift = 7 - (len(str(n)) - len(str(d)))
    def mant(sh):
        if sh >= 0:
            return (n * 10 ** sh) // d
        return n // (d * 10 ** (-sh))
    m = mant(shift)
    while m < 10 ** 6:
        shift += 1
        m = mant(shift)
    while m >= 10 ** 7:
        shift -= 1
        m = mant(shift)
    s = str(m)
    return "%s%s.%se%+d" % (sgn, s[0], s[1:7], 6 - shift)


# ---------- complex rational arithmetic (re, im) ----------------------
def cadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def csub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def cmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def cdiv(x, y):
    d = y[0] * y[0] + y[1] * y[1]
    return ((x[0] * y[0] + x[1] * y[1]) / d, (x[1] * y[0] - x[0] * y[1]) / d)


def cconj(x):
    return (x[0], -x[1])


CZERO = (Fr(0), Fr(0))
CONE = (Fr(1), Fr(0))
HALF = Fr(1, 2)
RBG = 64


def thomas_Q(z):
    # e1 entry of (J_R - z)^-1, R = RBG, exact over Q(i)
    R = RBG
    dp = [None] * R
    rp = [None] * R
    mz = (Fr(0) - z[0], -z[1])
    dp[0] = mz
    rp[0] = CONE
    off = (HALF, Fr(0))
    for i in range(1, R):
        w = cdiv(off, dp[i - 1])
        dp[i] = csub(mz, cmul(w, off))
        rp[i] = csub(CZERO, cmul(w, rp[i - 1]))
    x = cdiv(rp[R - 1], dp[R - 1])
    for i in range(R - 2, -1, -1):
        x = cdiv(csub(rp[i], cmul(off, x)), dp[i])
    return x


def thomas_solve_real(c, rhs):
    # (J_R - c) x = rhs over Q, c rational, full vector
    R = RBG
    dp = [None] * R
    rp = [None] * R
    dp[0] = -c
    rp[0] = rhs[0]
    for i in range(1, R):
        w = HALF / dp[i - 1]
        dp[i] = -c - w * HALF
        rp[i] = rhs[i] - w * rp[i - 1]
    x = [None] * R
    x[R - 1] = rp[R - 1] / dp[R - 1]
    for i in range(R - 2, -1, -1):
        x[i] = (rp[i] - HALF * x[i + 1]) / dp[i]
    return x


def pick_matrix(qvals, zs):
    N = len(zs)
    return [[cdiv(csub(qvals[j], cconj(qvals[k])),
                  csub(zs[j], cconj(zs[k]))) for k in range(N)]
            for j in range(N)]


def ldl_hermitian(P):
    N = len(P)
    L = [[CZERO] * N for _ in range(N)]
    d = [None] * N
    for j in range(N):
        acc = P[j][j][0]
        for k in range(j):
            lv = L[j][k]
            acc -= (lv[0] * lv[0] + lv[1] * lv[1]) * d[k]
        d[j] = acc
        L[j][j] = CONE
        if acc == 0:
            raise RuntimeError("zero pivot")
        for i in range(j + 1, N):
            s = P[i][j]
            for k in range(j):
                s = csub(s, cmul(cmul(L[i][k], cconj(L[j][k])),
                                 (d[k], Fr(0))))
            L[i][j] = (s[0] / d[j], s[1] / d[j])
    return L, d


def forward_sub(L, b):
    N = len(b)
    u = [None] * N
    for i in range(N):
        s = b[i]
        for k in range(i):
            s = csub(s, cmul(L[i][k], u[k]))
        u[i] = s
    return u


def cdet(M):
    N = len(M)
    A = [row[:] for row in M]
    det = CONE
    for col in range(N):
        piv = A[col][col]
        if piv == CZERO:
            found = False
            for r in range(col + 1, N):
                if A[r][col] != CZERO:
                    A[col], A[r] = A[r], A[col]
                    det = (Fr(0) - det[0], -det[1])
                    piv = A[col][col]
                    found = True
                    break
            if not found:
                return CZERO
        det = cmul(det, piv)
        for r in range(col + 1, N):
            if A[r][col] == CZERO:
                continue
            f = cdiv(A[r][col], piv)
            for c in range(col, N):
                A[r][c] = csub(A[r][c], cmul(f, A[col][c]))
    return det


def rdet(M):
    N = len(M)
    A = [row[:] for row in M]
    det = Fr(1)
    for col in range(N):
        piv = A[col][col]
        if piv == 0:
            found = False
            for r in range(col + 1, N):
                if A[r][col] != 0:
                    A[col], A[r] = A[r], A[col]
                    det = -det
                    piv = A[col][col]
                    found = True
                    break
            if not found:
                return Fr(0)
        det *= piv
        for r in range(col + 1, N):
            if A[r][col] == 0:
                continue
            f = A[r][col] / piv
            for c in range(col, N):
                A[r][c] -= f * A[col][c]
    return det


# ---------- block quantities and thresholds ---------------------------
def block_quantities_pick(L, d, A, B):
    u = forward_sub(L, A)
    v = forward_sub(L, B)
    regs = []
    Ds = []
    al = Fr(0)
    be = Fr(0)
    ga = CZERO
    for i in range(len(d)):
        ui, vi = u[i], v[i]
        al += (ui[0] * ui[0] + ui[1] * ui[1]) / d[i]
        be += (vi[0] * vi[0] + vi[1] * vi[1]) / d[i]
        ga = cadd(ga, cdiv(cmul(cconj(ui), vi), (d[i], Fr(0))))
        regs.append(ga[0])
        Ds.append(al * be - (ga[0] * ga[0] + ga[1] * ga[1]))
    return regs, Ds


def block_quantities_gram(Lc, dh, avec):
    uw = forward_sub(Lc, avec)
    regs = []
    Ds = []
    s_acc = CZERO
    h_acc = Fr(0)
    for i in range(len(dh)):
        wi = uw[i]
        s_acc = cadd(s_acc, cdiv(cmul(wi, wi), (dh[i], Fr(0))))
        h_acc += (wi[0] * wi[0] + wi[1] * wi[1]) / dh[i]
        regs.append(s_acc[0])
        Ds.append(h_acc * h_acc - (s_acc[0] * s_acc[0] + s_acc[1] * s_acc[1]))
    return regs, Ds


def quad(reg, D, w):
    return 1 + 2 * w * reg - w * w * D


def nstar_scan(regs, Ds, w):
    # returns (nstar or None, list of boundary m values)
    bmarks = []
    for m in range(len(Ds)):
        qv = quad(regs[m], Ds[m], w)
        if qv < 0:
            return m + 1, bmarks
        if qv == 0:
            bmarks.append(m + 1)
    return None, bmarks


def wstar_bracket(reg, D):
    # certified dyadic enclosure of the positive root; "inf" when none
    if D == 0:
        if reg < 0:
            v = Fr(-1) / (2 * reg)
            return (v, v)
        return "inf"
    if D < 0:
        raise RuntimeError("D < 0")
    lo, hi = Fr(0), Fr(1)
    while quad(reg, D, hi) > 0:
        hi *= 2
    for _ in range(40):
        mid = (lo + hi) / 2
        if quad(reg, D, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo, hi)


def bracket_min(brs):
    # elementwise-min enclosure over non-inf brackets
    lo = None
    hi = None
    for b in brs:
        if b == "inf":
            continue
        if lo is None or b[0] < lo:
            lo = b[0]
        if hi is None or b[1] < hi:
            hi = b[1]
    if lo is None:
        return "inf"
    return (lo, hi)


# ---------- frozen designs and grid -----------------------------------
NMAX = 24
ND1_A = [Fr(1) + Fr(1, n) for n in range(1, NMAX + 1)]
ND2_A = [Fr(1) + Fr(25 - j, 24) for j in range(1, NMAX + 1)]
ND3_A = [Fr(30 - j, 24) for j in range(1, NMAX + 1)]
CPOINT = Fr(5, 4)
SMAX = 47
XS = [Fr(1, 10), Fr(1, 3), Fr(3, 5), Fr(4, 5), Fr(9, 10)]
DS = [Fr(1, 10), Fr(1, 100)]
WS = [Fr(1, 10), Fr(1, 100)]
MREP = [8, 12, 16, 20, 24]
ANCHORS = {
    (Fr(1, 3), Fr(1, 10)): (Fr(1709750, 10 ** 7), Fr(1709754, 10 ** 7)),
    (Fr(9, 10), Fr(1, 10)): (Fr(1800329, 10 ** 8), Fr(1800333, 10 ** 8)),
    (Fr(1, 3), Fr(1, 100)): (Fr(2141725, 10 ** 5), Fr(2141729, 10 ** 5)),
}
IDCELLS = [(Fr(1, 3), Fr(1, 10)), (Fr(4, 5), Fr(1, 100))]
IDWS = [Fr(1, 10), Fr(1, 17)]
IDM = 12


def main():
    print("P-RH-WEYL-CANONICAL-2 verifier")
    print("exact rank-two threshold map, free Jacobi background R = 64,"
          " four designs, m to 24")
    print("designs: ND1 chain 1+1/n; ND2 spread 1+(25-j)/24; ND3 shifted"
          " (30-j)/24; ND4 one-point Gram at c = 5/4")
    print("grid: x in {1/10,1/3,3/5,4/5,9/10}, delta in {1/10,1/100};"
          " weights {1/10,1/100}; detection = strictly negative quadratic")

    # ---------- backgrounds ----------
    designs = []
    ok0 = True
    for (name, alist) in [("ND1", ND1_A), ("ND2", ND2_A), ("ND3", ND3_A)]:
        ok0 &= len(set(alist)) == NMAX
        ok0 &= all(a > 0 for a in alist)
        zs = [(Fr(0), a) for a in alist]
        qs = [thomas_Q(z) for z in zs]
        P0 = pick_matrix(qs, zs)
        L, d = ldl_hermitian(P0)
        ok0 &= all(x > 0 for x in d)
        print("BG %s min pivot %s" % (name, dec6(d[NMAX - 1])))
        designs.append((name, "pick", zs, P0, L, d))
    vec = [Fr(1)] + [Fr(0)] * (RBG - 1)
    mom = []
    for s in range(SMAX + 1):
        vec = thomas_solve_real(CPOINT, vec)
        mom.append(vec[0])
    H = [[mom[m + n + 1] for n in range(NMAX)] for m in range(NMAX)]
    Hc = [[(H[i][k], Fr(0)) for k in range(NMAX)] for i in range(NMAX)]
    Lc, dh = ldl_hermitian(Hc)
    ok0 &= all(x > 0 for x in dh)
    print("BG ND4 min pivot %s" % dec6(dh[NMAX - 1]))
    designs.append(("ND4", "gram", None, Hc, Lc, dh))
    report("CHECK 0 foundations: distinct upper half-plane nodes,"
           " positive background pivots, all designs", bool(ok0))

    # ---------- the map ----------
    ok2 = True
    store = {}
    for (name, kind, zs, P0, L, d) in designs:
        for x in XS:
            for de in DS:
                mu = (x, de)
                if kind == "pick":
                    A = [cdiv(CONE, csub(mu, z)) for z in zs]
                    B = [cdiv(CONE, csub(cconj(mu), z)) for z in zs]
                    regs, Dl = block_quantities_pick(L, d, A, B)
                else:
                    Ac = cdiv(CONE, csub(mu, (CPOINT, Fr(0))))
                    avec = []
                    p = CONE
                    for m in range(NMAX):
                        p = cmul(p, Ac)
                        avec.append(p)
                    regs, Dl = block_quantities_gram(L, d, avec)
                ok2 &= all(v >= 0 for v in Dl)
                store[(name, x, de)] = (regs, Dl)
                ns = []
                for w in WS:
                    n, bm = nstar_scan(regs, Dl, w)
                    ns.append((n, bm))
                brs = [wstar_bracket(regs[m - 1], Dl[m - 1]) for m in MREP]
                allb = [wstar_bracket(regs[m], Dl[m]) for m in range(NMAX)]
                mn = bracket_min(allb)
                def fmt_b(b):
                    return "inf" if b == "inf" else dec6(b[0])
                def fmt_n(t):
                    n, bm = t
                    s = "none" if n is None else str(n)
                    if bm:
                        s += "b" + ",".join(str(v) for v in bm)
                    return s
                print("MAP %s x=%s d=%s N*(1/10)=%s N*(1/100)=%s %s min24=[%s,%s]"
                      % (name, x, de, fmt_n(ns[0]), fmt_n(ns[1]),
                         " ".join("m%d=%s" % (m, fmt_b(b))
                                  for (m, b) in zip(MREP, brs)),
                         "inf" if mn == "inf" else dec6(mn[0]),
                         "inf" if mn == "inf" else dec6(mn[1])))

    # ---------- CHECK 1: identity against direct determinants ----------
    ok1 = True
    for (name, kind, zs, P0, L, d) in designs:
        for (x, de) in IDCELLS:
            regs, Dl = store[(name, x, de)]
            reg12, D12 = regs[IDM - 1], Dl[IDM - 1]
            mu = (x, de)
            if kind == "pick":
                A = [cdiv(CONE, csub(mu, z)) for z in zs]
                B = [cdiv(CONE, csub(cconj(mu), z)) for z in zs]
                P0m = [row[:IDM] for row in P0[:IDM]]
                det0 = cdet(P0m)
                for w in IDWS:
                    Pw = [[cadd(P0[j][k],
                                cmul((w, Fr(0)),
                                     cadd(cmul(A[j], cconj(B[k])),
                                          cmul(B[j], cconj(A[k])))))
                           for k in range(IDM)] for j in range(IDM)]
                    detw = cdet(Pw)
                    pred = cmul(det0, (quad(reg12, D12, w), Fr(0)))
                    if detw != pred:
                        ok1 = False
            else:
                Ac = cdiv(CONE, csub(mu, (CPOINT, Fr(0))))
                avec = []
                p = CONE
                for m in range(NMAX):
                    p = cmul(p, Ac)
                    avec.append(p)
                H0m = [[P0[j][k][0] for k in range(IDM)] for j in range(IDM)]
                det0 = rdet(H0m)
                for w in IDWS:
                    Hw = [[P0[j][k][0]
                           + w * 2 * cmul(avec[j], avec[k])[0]
                           for k in range(IDM)] for j in range(IDM)]
                    detw = rdet(Hw)
                    pred = det0 * quad(reg12, D12, w)
                    if detw != pred:
                        ok1 = False
    report("CHECK 1 rank-two determinant identity exact at m = 12,"
           " 2 cells x 2 weights x 4 designs", bool(ok1))
    report("CHECK 2 Cauchy-Schwarz D_m >= 0, all blocks, cells, designs",
           bool(ok2))

    # ---------- CHECK 3: WEYL-1/1b consistency on ND1, m <= 8 ----------
    ok3 = True
    for (x, de), (alo, ahi) in ANCHORS.items():
        regs, Dl = store[("ND1", x, de)]
        w = Fr(1, 10) if de == Fr(1, 10) else Fr(1, 100)
        n8 = None
        for m in range(8):
            if quad(regs[m], Dl[m], w) < 0:
                n8 = m + 1
                break
        if (x, de) == (Fr(9, 10), Fr(1, 10)):
            ok3 &= n8 == 6
        else:
            ok3 &= n8 is None
        br = wstar_bracket(regs[7], Dl[7])
        ok3 &= br != "inf" and alo < br[0] and br[1] < ahi
        print("CONS ND1 x=%s d=%s N*8=%s w*8=[%s,%s] anchor=(%s,%s)"
              % (x, de, "none" if n8 is None else n8,
                 dec6(br[0]), dec6(br[1]), dec6(alo), dec6(ahi)))
    report("CHECK 3 consistency with pinned WEYL-1/1b at m <= 8 on ND1",
           bool(ok3))

    # ---------- CHECK 4: prediction window ----------
    regs, Dl = store[("ND1", Fr(1, 3), Fr(1, 10))]
    nd1_star, _ = nstar_scan(regs, Dl, Fr(1, 10))
    ok4 = nd1_star is not None and 9 <= nd1_star <= 13
    print("PRED N*(D1, ND1, w=1/10) = %s window [9,13]"
          % ("none" if nd1_star is None else nd1_star))
    report("CHECK 4 owner window N*(D1, ND1, 1/10) in [9, 13]", bool(ok4))

    # ---------- CHECK 5: depth stop-gate ----------
    det_any = False
    for name in ["ND1", "ND2", "ND3", "ND4"]:
        regs, Dl = store[(name, Fr(1, 3), Fr(1, 10))]
        n, _ = nstar_scan(regs, Dl, Fr(1, 10))
        if n is not None:
            det_any = True
    report("CHECK 5 depth: D1 detected by m <= 24 at w = 1/10 on at"
           " least one design", bool(det_any))

    # ---------- frozen decision tree ----------
    npass = sum(1 for (_, o) in CHECKS if o)
    failed = [n for (n, o) in CHECKS if not o]
    fwa = not (CHECKS[0][1] and CHECKS[1][1] and CHECKS[2][1])
    fwb = not CHECKS[3][1]
    fwc = not CHECKS[4][1]
    fwd = not CHECKS[5][1]
    if fwa or fwb:
        print("LANE VERDICT: [F-bounded, T2 INSTRUMENTS], instrument or"
              " consistency gate failed, redesign before any zeta-side"
              " work")
    elif fwd:
        print("LANE VERDICT: [F-bounded, DEPTH READING], D1 undetected at"
              " depth 24 on all four designs; the E4 narrowed reading"
              " fails at these depths")
        if fwc:
            print("LANE VERDICT ADDENDUM: PREDICTION F (owner window"
                  " missed)")
    elif fwc:
        print("LANE VERDICT: PREDICTION F, MAP STANDS (owner window"
              " missed; the map rows remain the record)")
    else:
        print("LANE VERDICT: MAP RECORDED, all gates pass; the w* map"
              " rows are the record [candidate-C at the frozen grid]")
    print("CHECKS: %d of %d PASS, FAILED: %s"
          % (npass, len(CHECKS), ",".join(failed) if failed else "none"))
    sys.exit(0 if not failed else 1)


if __name__ == "__main__":
    main()
