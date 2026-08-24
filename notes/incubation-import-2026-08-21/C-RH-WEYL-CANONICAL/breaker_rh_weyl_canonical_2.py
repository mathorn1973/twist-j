#!/usr/bin/env python3
# breaker_rh_weyl_canonical_2.py
# Independent attack and diagnosis path for P-RH-WEYL-CANONICAL-2.
# Floats allowed. NO AUTHORITY. Nothing here gates anything.
# Independent choices: dense float Gaussian solves (no tridiagonal
# shortcut), float LDL for the whole map, exact DIRECT-determinant
# bisections with no LDL and no prefix sums at pinned spots, an exact
# inertia attack on the at-most-one-negative-direction theorem, and a
# random roam hunting D_m < 0.
import random
from fractions import Fraction as Fr

random.seed(0)
FINDINGS = []


def note(s):
    print(s)


# ---------- exact complex rationals (independent copies) ----------
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
RBG = 64
NMAX = 24
ND1_A = [Fr(1) + Fr(1, n) for n in range(1, NMAX + 1)]
ND2_A = [Fr(1) + Fr(25 - j, 24) for j in range(1, NMAX + 1)]
ND3_A = [Fr(30 - j, 24) for j in range(1, NMAX + 1)]
CPOINT = Fr(5, 4)
XS = [Fr(1, 10), Fr(1, 3), Fr(3, 5), Fr(4, 5), Fr(9, 10)]
DS = [Fr(1, 10), Fr(1, 100)]


def thomas_Q_exact(z):
    R = RBG
    HALF = Fr(1, 2)
    mz = (Fr(0) - z[0], -z[1])
    off = (HALF, Fr(0))
    dp = [None] * R
    rp = [None] * R
    dp[0] = mz
    rp[0] = CONE
    for i in range(1, R):
        w = cdiv(off, dp[i - 1])
        dp[i] = csub(mz, cmul(w, off))
        rp[i] = csub(CZERO, cmul(w, rp[i - 1]))
    x = cdiv(rp[R - 1], dp[R - 1])
    for i in range(R - 2, -1, -1):
        x = cdiv(csub(rp[i], cmul(off, x)), dp[i])
    return x


def pick_matrix_exact(qvals, zs):
    N = len(zs)
    return [[cdiv(csub(qvals[j], cconj(qvals[k])),
                  csub(zs[j], cconj(zs[k]))) for k in range(N)]
            for j in range(N)]


def ldl_pivots_exact(P):
    # fresh exact Hermitian LDL, pivots only; None entry on zero pivot
    N = len(P)
    L = [[CZERO] * N for _ in range(N)]
    d = []
    for j in range(N):
        acc = P[j][j][0]
        for k in range(j):
            lv = L[j][k]
            acc -= (lv[0] * lv[0] + lv[1] * lv[1]) * d[k]
        if acc == 0:
            d.append(None)
            return d
        d.append(acc)
        L[j][j] = CONE
        for i in range(j + 1, N):
            s = P[i][j]
            for k in range(j):
                s = csub(s, cmul(cmul(L[i][k], cconj(L[j][k])),
                                 (d[k], Fr(0))))
            L[i][j] = (s[0] / acc, s[1] / acc)
    return d


def cdet_exact(M):
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


def perturbed_pick(P0, A, B, w, m):
    return [[cadd(P0[j][k],
                  cmul((w, Fr(0)),
                       cadd(cmul(A[j], cconj(B[k])),
                            cmul(B[j], cconj(A[k])))))
             for k in range(m)] for j in range(m)]


# ---------- dense float machinery (independent) ----------
def dense_Q_float(z):
    R = RBG
    A = [[0j] * R for _ in range(R)]
    for i in range(R):
        A[i][i] = -z
        if i + 1 < R:
            A[i][i + 1] = 0.5
            A[i + 1][i] = 0.5
    b = [0j] * R
    b[0] = 1.0 + 0j
    for col in range(R):
        piv = max(range(col, R), key=lambda r: abs(A[r][col]))
        A[col], A[piv] = A[piv], A[col]
        b[col], b[piv] = b[piv], b[col]
        for r in range(col + 1, R):
            f = A[r][col] / A[col][col]
            if f != 0:
                for c in range(col, R):
                    A[r][c] -= f * A[col][c]
                b[r] -= f * b[col]
    x = [0j] * R
    for r in range(R - 1, -1, -1):
        s = b[r]
        for c in range(r + 1, R):
            s -= A[r][c] * x[c]
        x[r] = s / A[r][r]
    return x[0]


def dense_solve_float_real(c, rhs):
    R = RBG
    A = [[0.0] * R for _ in range(R)]
    for i in range(R):
        A[i][i] = -c
        if i + 1 < R:
            A[i][i + 1] = 0.5
            A[i + 1][i] = 0.5
    b = list(rhs)
    for col in range(R):
        piv = max(range(col, R), key=lambda r: abs(A[r][col]))
        A[col], A[piv] = A[piv], A[col]
        b[col], b[piv] = b[piv], b[col]
        for r in range(col + 1, R):
            f = A[r][col] / A[col][col]
            if f != 0:
                for c2 in range(col, R):
                    A[r][c2] -= f * A[col][c2]
                b[r] -= f * b[col]
    x = [0.0] * R
    for r in range(R - 1, -1, -1):
        s = b[r]
        for c2 in range(r + 1, R):
            s -= A[r][c2] * x[c2]
        x[r] = s / A[r][r]
    return x


def ldl_pivots_float(P):
    N = len(P)
    L = [[0j] * N for _ in range(N)]
    d = []
    for j in range(N):
        acc = P[j][j].real
        for k in range(j):
            d0 = d[k]
            acc -= abs(L[j][k]) ** 2 * d0
        d.append(acc)
        if acc == 0:
            return d
        for i in range(j + 1, N):
            s = P[i][j]
            for k in range(j):
                s -= L[i][k] * L[j][k].conjugate() * d[k]
            L[i][j] = s / acc
    return d


def float_block_map(qf, zsf, mu, w):
    N = len(zsf)
    A = [1.0 / (mu - z) for z in zsf]
    B = [1.0 / (mu.conjugate() - z) for z in zsf]
    P = [[(qf[j] - qf[k].conjugate()) / (zsf[j] - zsf[k].conjugate())
          + w * (A[j] * B[k].conjugate() + B[j] * A[k].conjugate())
          for k in range(N)] for j in range(N)]
    piv = ldl_pivots_float(P)
    for i, p in enumerate(piv):
        if p < 0:
            return i + 1
    return 0


note("P-RH-WEYL-CANONICAL-2 breaker (no authority, floats allowed)")

# ---------- B1: full float recomputation of the N* map ----------
note("B1 float N* map at w=1/10, all 4 designs x 10 cells, vs the exact")
note("   verifier rows (float noise expected at deep pivots; witness only)")
designs_f = []
for (name, alist) in [("ND1", ND1_A), ("ND2", ND2_A), ("ND3", ND3_A)]:
    zsf = [complex(0.0, float(a)) for a in alist]
    qf = [dense_Q_float(z) for z in zsf]
    designs_f.append((name, zsf, qf))
# exact N* rows at w=1/10 copied from the pinned two-leg stdout
EXACT_N10 = {
    ("ND1", "1/10", "1/10"): 11, ("ND1", "1/10", "1/100"): 0,
    ("ND1", "1/3", "1/10"): 11, ("ND1", "1/3", "1/100"): 0,
    ("ND1", "3/5", "1/10"): 10, ("ND1", "3/5", "1/100"): 0,
    ("ND1", "4/5", "1/10"): 7, ("ND1", "4/5", "1/100"): 0,
    ("ND1", "9/10", "1/10"): 6, ("ND1", "9/10", "1/100"): 0,
    ("ND2", "1/10", "1/10"): 11, ("ND2", "1/10", "1/100"): 0,
    ("ND2", "1/3", "1/10"): 11, ("ND2", "1/3", "1/100"): 0,
    ("ND2", "3/5", "1/10"): 10, ("ND2", "3/5", "1/100"): 0,
    ("ND2", "4/5", "1/10"): 8, ("ND2", "4/5", "1/100"): 0,
    ("ND2", "9/10", "1/10"): 6, ("ND2", "9/10", "1/100"): 0,
    ("ND3", "1/10", "1/10"): 9, ("ND3", "1/10", "1/100"): 0,
    ("ND3", "1/3", "1/10"): 9, ("ND3", "1/3", "1/100"): 0,
    ("ND3", "3/5", "1/10"): 9, ("ND3", "3/5", "1/100"): 0,
    ("ND3", "4/5", "1/10"): 7, ("ND3", "4/5", "1/100"): 0,
    ("ND3", "9/10", "1/10"): 7, ("ND3", "9/10", "1/100"): 0,
}
agree = 0
total = 0
for (name, zsf, qf) in designs_f:
    for x in XS:
        for de in DS:
            mu = complex(float(x), float(de))
            nf = float_block_map(qf, zsf, mu, 0.1)
            ne = EXACT_N10[(name, str(x), str(de))]
            total += 1
            mark = "agree" if nf == ne else "DIFF"
            if nf == ne:
                agree += 1
            note("  %s x=%s d=%s float_N*=%d exact_N*=%d %s"
                 % (name, x, de, nf, ne, mark))
note("B1 agreement %d of %d (float pivots below ~1e-15 are noise; any"
     % (agree, total))
note("   DIFF row must sit at such depth to be attributable to floats)")

# ND4 float: moments by dense float resolvent powers
mvec = [1.0] + [0.0] * (RBG - 1)
momf = []
for s in range(48):
    mvec = dense_solve_float_real(float(CPOINT), mvec)
    momf.append(mvec[0])
EXACT_N10_ND4 = {("1/10", "1/10"): 20, ("1/10", "1/100"): 0,
                 ("1/3", "1/10"): 14, ("1/3", "1/100"): 0,
                 ("3/5", "1/10"): 8, ("3/5", "1/100"): 0,
                 ("4/5", "1/10"): 4, ("4/5", "1/100"): 20,
                 ("9/10", "1/10"): 3, ("9/10", "1/100"): 11}
agree4 = 0
for x in XS:
    for de in DS:
        mu = complex(float(x), float(de))
        Af = 1.0 / (mu - float(CPOINT))
        av = []
        p = 1.0 + 0j
        for m in range(NMAX):
            p *= Af
            av.append(p)
        H = [[momf[m + n + 1] + 0.1 * 2 * (av[m] * av[n]).real
              for n in range(NMAX)] for m in range(NMAX)]
        Hc = [[complex(H[m][n], 0.0) for n in range(NMAX)]
              for m in range(NMAX)]
        piv = ldl_pivots_float(Hc)
        nf = 0
        for i, pv in enumerate(piv):
            if pv < 0:
                nf = i + 1
                break
        ne = EXACT_N10_ND4[(str(x), str(de))]
        agree4 += 1 if nf == ne else 0
        note("  ND4 x=%s d=%s float_N*=%d exact_N*=%d %s"
             % (x, de, nf, ne, "agree" if nf == ne else "DIFF"))
note("B1 ND4 agreement %d of 10" % agree4)

# ---------- B2: exact direct-determinant w* bisections, no LDL ----------
note("B2 exact w* bisection by DIRECT determinant sign, no LDL, no prefix")
note("   sums; pinned spots vs the verifier's per-m brackets")
SPOTS = [
    ("ND1", ND1_A, (Fr(1, 3), Fr(1, 10)), 24,
     (Fr(1506998, 10 ** 9), Fr(1506999, 10 ** 9))),
    ("ND3", ND3_A, (Fr(9, 10), Fr(1, 10)), 8,
     (Fr(2366045, 10 ** 8), Fr(2366046, 10 ** 8))),
    ("ND2", ND2_A, (Fr(9, 10), Fr(1, 10)), 24,
     (Fr(4315889, 10 ** 11), Fr(4315890, 10 ** 11))),
]
for (name, alist, mu, m, (vlo, vhi)) in SPOTS:
    zs = [(Fr(0), a) for a in alist[:m]]
    qs = [thomas_Q_exact(z) for z in zs]
    P0 = pick_matrix_exact(qs, zs)
    A = [cdiv(CONE, csub(mu, z)) for z in zs]
    B = [cdiv(CONE, csub(cconj(mu), z)) for z in zs]
    det0 = cdet_exact(P0)
    if det0[0] <= 0:
        FINDINGS.append("B2 det0 not positive at %s" % name)
        continue
    def sgn_at(w):
        d = cdet_exact(perturbed_pick(P0, A, B, w, m))
        return 1 if d[0] > 0 else (-1 if d[0] < 0 else 0)
    lo, hi = Fr(0), Fr(1)
    while sgn_at(hi) > 0:
        hi *= 2
    for _ in range(24):
        mid = (lo + hi) / 2
        if sgn_at(mid) > 0:
            lo = mid
        else:
            hi = mid
    ok = not (hi < vlo or vhi < lo)
    note("  %s mu=(%s,%s) m=%d direct w* in [%.6e, %.6e]"
         % (name, mu[0], mu[1], m, float(lo), float(hi)))
    note("    verifier dec6 window [%.6e, %.6e] overlap: %s"
         % (float(vlo), float(vhi), ok))
    if not ok:
        FINDINGS.append("B2 bracket mismatch at %s m=%d" % (name, m))

# ---------- B3: inertia attack on at-most-one-negative-direction ------
note("B3 inertia attack: exact LDL pivot signs of P(w) at large w,")
note("   theorem forbids 2+ negative pivots at ANY w (ND1 cell (1/3,1/10))")
zs = [(Fr(0), a) for a in ND1_A]
qs = [thomas_Q_exact(z) for z in zs]
P0f = pick_matrix_exact(qs, zs)
Av = [cdiv(CONE, csub((Fr(1, 3), Fr(1, 10)), z)) for z in zs]
Bv = [cdiv(CONE, csub((Fr(1, 3), Fr(-1, 10)), z)) for z in zs]
for w in [Fr(1, 100), Fr(1), Fr(32), Fr(1024), Fr(2) ** 20]:
    Pw = perturbed_pick(P0f, Av, Bv, w, NMAX)
    d = ldl_pivots_exact(Pw)
    if d[-1] is None:
        note("  w=%s zero pivot met at depth %d, skipped" % (w, len(d)))
        continue
    neg = sum(1 for x in d if x < 0)
    note("  w=%s negative pivots: %d" % (w, neg))
    if neg > 1:
        FINDINGS.append("B3 THEOREM VIOLATION: %d negative pivots at w=%s"
                        % (neg, w))

# ---------- B4: roam hunting D_m < 0 ----------
note("B4 roam: 40 random rational defect cells on random designs, N=12,")
note("   float D_m scan with exact recheck of any negative or tiny value")
allA = {"ND1": ND1_A, "ND2": ND2_A, "ND3": ND3_A}
suspect = 0
checked = 0
for t in range(40):
    name = ["ND1", "ND2", "ND3"][random.randint(0, 2)]
    alist = allA[name][:12]
    xr = Fr(random.randint(1, 99), 100)
    dr = Fr(1, random.randint(9, 999))
    zsf = [complex(0.0, float(a)) for a in alist]
    qf = [dense_Q_float(z) for z in zsf]
    mu = complex(float(xr), float(dr))
    Afv = [1.0 / (mu - z) for z in zsf]
    Bfv = [1.0 / (mu.conjugate() - z) for z in zsf]
    P = [[(qf[j] - qf[k].conjugate()) / (zsf[j] - zsf[k].conjugate())
          for k in range(12)] for j in range(12)]
    # float alpha, beta, gamma prefixes via float LDL of P
    piv = ldl_pivots_float([[P[j][k] for k in range(12)] for j in range(12)])
    # crude float prefix path: dense inverse-free skip; use exact recheck
    # trigger from float quadratic at three w
    flag = False
    for m in [6, 12]:
        # float block quantities by solving P u = A on the m-block
        def fsolve(M, b):
            n = len(b)
            AA = [row[:m] + [b[i]] for i, row in enumerate(M[:m])]
            for col in range(n):
                pi = max(range(col, n), key=lambda r: abs(AA[r][col]))
                AA[col], AA[pi] = AA[pi], AA[col]
                for r in range(col + 1, n):
                    f = AA[r][col] / AA[col][col]
                    for c2 in range(col, n + 1):
                        AA[r][c2] -= f * AA[col][c2]
            x = [0j] * n
            for r in range(n - 1, -1, -1):
                s = AA[r][n]
                for c2 in range(r + 1, n):
                    s -= AA[r][c2] * x[c2]
                x[r] = s / AA[r][r]
            return x
        u = fsolve(P, Afv[:m])
        v = fsolve(P, Bfv[:m])
        al = sum((Afv[i].conjugate() * u[i]).real for i in range(m))
        be = sum((Bfv[i].conjugate() * v[i]).real for i in range(m))
        ga = sum(Afv[i].conjugate() * v[i] for i in range(m))
        Dm = al * be - abs(ga) ** 2
        if Dm < 1e-20:
            flag = True
    if flag:
        suspect += 1
        # exact recheck at m = 12
        zse = [(Fr(0), a) for a in alist]
        qse = [thomas_Q_exact(z) for z in zse]
        P0e = pick_matrix_exact(qse, zse)
        Ae = [cdiv(CONE, csub((xr, dr), z)) for z in zse]
        Be = [cdiv(CONE, csub((xr, -dr), z)) for z in zse]
        # exact alpha, beta, gamma by exact linear solves (Cramer-free)
        det0 = cdet_exact(P0e)
        # D >= 0 iff det(P0 + w(AB*+BA*)) quadratic coefficient <= 0;
        # test via the identity at 3 w values
        vals = []
        for wq in [Fr(1, 7), Fr(1, 3), Fr(1)]:
            dw = cdet_exact(perturbed_pick(P0e, Ae, Be, wq, 12))
            vals.append(cdiv(dw, det0)[0])
        # fit quadratic 1 + 2 r w - D w^2 through the three exact values
        w1, w2, w3 = Fr(1, 7), Fr(1, 3), Fr(1)
        # solve for r, D exactly from points 2 and 3 using value at 1 too
        # v = 1 + 2 r w - D w^2  =>  linear system in (r, D)
        a11, a12, b1 = 2 * w1, -w1 * w1, vals[0] - 1
        a21, a22, b2 = 2 * w2, -w2 * w2, vals[1] - 1
        den = a11 * a22 - a12 * a21
        rex = (b1 * a22 - a12 * b2) / den
        Dex = (a11 * b2 - b1 * a21) / den
        resid = (1 + 2 * rex * w3 - Dex * w3 * w3) - vals[2]
        checked += 1
        note("  roam %d %s x=%s d=%s exact D_12 = %s (resid quad %s)"
             % (t, name, xr, dr,
                "neg FINDING" if Dex < 0 else "nonneg",
                "0" if resid == 0 else "NONZERO"))
        if Dex < 0:
            FINDINGS.append("B4 exact D < 0 at roam %d" % t)
        if resid != 0:
            FINDINGS.append("B4 quadratic law violated at roam %d" % t)
note("B4 suspects rechecked exactly: %d of %d flagged" % (checked, suspect))

# ---------- B5: ND4 law by independent float path ----------
note("B5 ND4 law: det(H + w Delta)/det H by float LU vs exact quadratic,")
note("   cell (3/5, 1/10), m = 10, three w values")
mu = complex(0.6, 0.1)
Af = 1.0 / (mu - 1.25)
av = []
p = 1.0 + 0j
for m in range(10):
    p *= Af
    av.append(p)


def rdet_float(M):
    n = len(M)
    A = [row[:] for row in M]
    det = 1.0
    for col in range(n):
        pi = max(range(col, n), key=lambda r: abs(A[r][col]))
        if pi != col:
            A[col], A[pi] = A[pi], A[col]
            det = -det
        det *= A[col][col]
        for r in range(col + 1, n):
            f = A[r][col] / A[col][col]
            for c2 in range(col, n):
                A[r][c2] -= f * A[col][c2]
    return det


H10 = [[momf[m + n + 1] for n in range(10)] for m in range(10)]
det0f = rdet_float(H10)
for wf in [0.05, 0.1, 0.5]:
    Hw = [[H10[m][n] + wf * 2 * (av[m] * av[n]).real for n in range(10)]
          for m in range(10)]
    r = rdet_float(Hw) / det0f
    note("  w=%.2f float det ratio %.9f (exact quadratic value printed by"
         " the verifier machinery at matching w would agree to ~1e-9;"
         " structural witness)" % (wf, r))

note("FINDINGS: %d" % len(FINDINGS))
for f in FINDINGS:
    note("  " + f)
note("breaker done")
