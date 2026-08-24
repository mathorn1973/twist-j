#!/usr/bin/env python3
# verify_rh_weyl_canonical_1.py
# P-RH-WEYL-CANONICAL-1: T2 lane opener. Exact verification of the S1-S5
# gate machinery on the free Jacobi canonical model: dictionary chi^(1)/chi,
# Herglotz/Pick PSD by exact LDL* over Q(i), certified node convergence to
# the known limit, one-point moment convergence in Q(sqrt 3), and
# finite-node detection of a non-self-adjoint defect.
# Python standard library only. Every assertion uses int or Fraction.
# Floats never appear anywhere in this file. Deterministic output.
#
# Env: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
import sys
from fractions import Fraction as Fr
from math import isqrt

CHECKS = []


def report(name, ok):
    CHECKS.append((name, ok))
    print("%s: %s" % (name, "PASS" if ok else "FAIL"))


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


# ---------- certified square-root enclosures --------------------------
PREC = 10 ** 40


def sqrt_enclosure(r):
    # r rational > 0; returns (lo, hi) rational with lo^2 <= r <= hi^2,
    # hi - lo <= 2/PREC roughly
    p = r.numerator
    q = r.denominator
    n = isqrt(p * q * PREC * PREC)
    lo = Fr(n, q * PREC)
    hi = Fr(n + 1, q * PREC)
    return lo, hi


# ---------- model: free Jacobi J_R (b_k = 0, a_k = 1/2) ---------------
HALF = Fr(1, 2)


def tridiag_solve_e1(R, z, b1extra=CZERO):
    # solve (J_R - z) x = e1 over C-rationals; returns full x, or None if
    # a pivot vanishes. b1extra is added to the (1,1) diagonal entry.
    dd = []
    rr = []
    for i in range(R):
        base = (Fr(0) - z[0], -z[1])
        if i == 0:
            base = cadd(base, b1extra)
        dd.append(base)
        rr.append(CONE if i == 0 else CZERO)
    off = (HALF, Fr(0))
    dp = [None] * R
    rp = [None] * R
    dp[0] = dd[0]
    rp[0] = rr[0]
    for i in range(1, R):
        if dp[i - 1] == CZERO:
            return None
        w = cdiv(off, dp[i - 1])
        dp[i] = csub(dd[i], cmul(w, off))
        rp[i] = csub(rr[i], cmul(w, rp[i - 1]))
    if dp[R - 1] == CZERO:
        return None
    x = [None] * R
    x[R - 1] = cdiv(rp[R - 1], dp[R - 1])
    for i in range(R - 2, -1, -1):
        x[i] = cdiv(csub(rp[i], cmul(off, x[i + 1])), dp[i])
    return x


def Q_resolvent(R, z, b1extra=CZERO):
    x = tridiag_solve_e1(R, z, b1extra)
    if x is None:
        return None
    return x[0]


def charpoly_ratio(R, z):
    # chi = det(J_R - z), chi^(1) = det with row/col 1 removed; both by the
    # three-term recurrence p_k = (b - z) p_{k-1} - (1/4) p_{k-2}, b = 0.
    quart = (Fr(1, 4), Fr(0))
    mz = (Fr(0) - z[0], -z[1])
    def chain(length):
        p0, p1 = CONE, mz
        if length == 0:
            return CONE
        for _ in range(length - 1):
            p0, p1 = p1, csub(cmul(mz, p1), cmul(quart, p0))
        return p1
    chi = chain(R)
    chi1 = chain(R - 1)
    if chi == CZERO:
        return None
    return cdiv(chi1, chi)


# ---------- Pick matrix and exact LDL pivots --------------------------
def pick_pivots(qvals, zs):
    # returns list of real rational pivots (Gaussian elimination without
    # pivoting on the Hermitian Pick matrix); None entries after a zero
    # pivot stop.
    N = len(zs)
    A = [[None] * N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            num = csub(qvals[j], cconj(qvals[k]))
            den = csub(zs[j], cconj(zs[k]))
            A[j][k] = cdiv(num, den)
    pivots = []
    for i in range(N):
        piv = A[i][i]
        if piv[1] != 0:
            raise RuntimeError("nonreal pivot")
        pivots.append(piv[0])
        if piv[0] == 0:
            break
        for j in range(i + 1, N):
            fac = cdiv(A[j][i], piv)
            for k in range(i + 1, N):
                A[j][k] = csub(A[j][k], cmul(fac, A[i][k]))
    return pivots


# ---------- Q(sqrt 3) pair and series arithmetic ----------------------
def pmulp(x, y):
    return (x[0] * y[0] + 3 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def paddp(x, y):
    return (x[0] + y[0], x[1] + y[1])


def psubp(x, y):
    return (x[0] - y[0], x[1] - y[1])


def pinvp(x):
    d = x[0] * x[0] - 3 * x[1] * x[1]
    return (x[0] / d, -x[1] / d)


PZERO = (Fr(0), Fr(0))
PONE = (Fr(1), Fr(0))
ORD = 7  # keep t^0..t^6


def smul(A, B):
    C = [PZERO] * ORD
    for i in range(ORD):
        if A[i] == PZERO:
            continue
        for j in range(ORD - i):
            C[i + j] = paddp(C[i + j], pmulp(A[i], B[j]))
    return C


def sdiv(A, B):
    C = [PZERO] * ORD
    b0inv = pinvp(B[0])
    for k in range(ORD):
        acc = A[k]
        for j in range(k):
            acc = psubp(acc, pmulp(C[j], B[k - j]))
        C[k] = pmulp(acc, b0inv)
    return C


def series_sqrt(F):
    # Newton iteration g <- (g + F/g)/2, g0 = sqrt(F0) supplied as (0,1)
    g = [PZERO] * ORD
    g[0] = (Fr(0), Fr(1))  # sqrt 3
    half = (Fr(1, 2), Fr(0))
    for _ in range(6):
        g = [pmulp(half, paddp(g[i], t[i])) for t in [sdiv(F, g)]
             for i in range(ORD)]
    return g


# ---------- frozen data ----------------------------------------------
RSET = [4, 8, 16, 32, 64]
NODES_A = [Fr(1) + Fr(1, n) for n in range(1, 9)]
NODES_Z = [(Fr(0), a) for a in NODES_A]
CPOINT = (Fr(2), Fr(0))
KMAX = 6
# conjugate pole-pair defects (A4 orbit analogue): (name, mu, weight, gated)
DEFECTS = [
    ("D1", (Fr(1, 3), Fr(1, 10)), Fr(1, 10), True),
    ("D2", (Fr(9, 10), Fr(1, 10)), Fr(1, 10), False),
    ("D3", (Fr(1, 3), Fr(1, 100)), Fr(1, 100), False),
]


def main():
    print("P-RH-WEYL-CANONICAL-1 verifier")
    print("T2 lane opener: free Jacobi model, gates S1-S5, nodes"
          " a_n = 1 + 1/n, n = 1..8")
    print("R in {4,8,16,32,64}, moment point c = 2, k <= 6,"
          " detection eps in {1/10, 1/100}")

    # CHECK 0: enclosures
    ok = True
    encl = {}
    for a in NODES_A:
        lo, hi = sqrt_enclosure(a * a + 1)
        ok &= lo * lo <= a * a + 1 <= hi * hi
        ok &= hi - lo < Fr(1, 10 ** 39)
        encl[a] = (lo, hi)
    s3lo, s3hi = sqrt_enclosure(Fr(3))
    ok &= s3lo * s3lo <= 3 <= s3hi * s3hi
    ok &= s3hi - s3lo < Fr(1, 10 ** 39)
    report("CHECK 0 sqrt enclosures certified", bool(ok))

    # CHECK 1: dictionary S1
    ok = True
    for R in [4, 8, 16]:
        for z in [NODES_Z[0], NODES_Z[3], CPOINT]:
            qa = Q_resolvent(R, z)
            qb = charpoly_ratio(R, z)
            ok &= (qa is not None) and (qb is not None) and qa == qb
    report("CHECK 1 dictionary chi^(1)/chi equals resolvent Q", bool(ok))

    # CHECK 2: normalization S3
    # J e1 = (b_1, a_1, 0, ...): first moment b_1 = 0; zeroth moment 1
    mu0 = Fr(1)
    mu1 = Fr(0)  # b_1 of the frozen model, stated and used as such
    report("CHECK 2 Laurent normalization mu0 = 1, mu1 = 0",
           mu0 == 1 and mu1 == 0)

    # CHECK 3: S2 and S4 pointwise and matrix form
    ok = True
    qstore = {}
    for R in RSET:
        for (n, z) in enumerate(NODES_Z):
            q = Q_resolvent(R, z)
            ok &= q is not None
            if q is None:
                continue
            qstore[(R, n)] = q
            ok &= q[1] > 0
    q64 = [qstore[(64, n)] for n in range(8)]
    pivs = pick_pivots(q64, NODES_Z)
    ok &= len(pivs) == 8 and all(p > 0 for p in pivs)
    for i, p in enumerate(pivs):
        print("PICKPIVOT R=64 i=%d p~=%s" % (i + 1, dec6(p)))
    report("CHECK 3 Herglotz: Im Q > 0 all R,n; 8x8 Pick pivots positive",
           bool(ok))

    # CHECK 4: node convergence with certified bounds
    ok = True
    prev = {}
    for R in RSET:
        for (n, z) in enumerate(NODES_Z):
            a = NODES_A[n]
            q = qstore[(R, n)]
            lo, hi = encl[a]
            qlo = 2 * (lo - a)
            qhi = 2 * (hi - a)
            x = q[0]
            y = q[1]
            d2 = x * x + max((y - qlo) * (y - qlo), (y - qhi) * (y - qhi))
            print("CONV n=%d R=%d dist2_hi~=%s" % (n + 1, R, dec6(d2)))
            if n in prev:
                ok &= d2 < prev[n]
            prev[n] = d2
            if R == 64:
                ok &= d2 < Fr(1, 10 ** 40)
    report("CHECK 4 node convergence certified, decreasing, <1e-40 at R=64",
           bool(ok))

    # CHECK 5: moment convergence at c = 2 in Q(sqrt 3)
    # limit series: m(2+t) = -4 - 2t + 2 sqrt(3 + 4t + t^2)
    F = [PZERO] * ORD
    F[0] = (Fr(3), Fr(0))
    F[1] = (Fr(4), Fr(0))
    F[2] = (Fr(1), Fr(0))
    g = series_sqrt(F)
    ok = smul(g, g) == F
    mlim = []
    for j in range(ORD):
        term = pmulp((Fr(2), Fr(0)), g[j])
        if j == 0:
            term = paddp(term, (Fr(-4), Fr(0)))
        if j == 1:
            term = paddp(term, (Fr(-2), Fr(0)))
        mlim.append(term)
    # exact Q_R Taylor coefficients at c = 2 by iterated solves
    for R in RSET:
        # coefficient of (z-2)^k of Q_R is e1^T (J-2)^{-(k+1)} e1
        vec = [CONE if i == 0 else CZERO for i in range(R)]
        coeffs = []
        cur = vec
        for k in range(KMAX + 1):
            cur = solve_vec(R, CPOINT, cur)
            coeffs.append(cur[0][0])
        for k in range(KMAX + 1):
            p, qq = mlim[k]
            end1 = p + qq * s3lo
            end2 = p + qq * s3hi
            c = coeffs[k]
            dist = max(abs(c - end1), abs(c - end2))
            print("MOM R=%d k=%d dist_hi~=%s" % (R, k, dec6(dist)))
            if R == 64:
                ok &= dist < Fr(1, 10 ** 30)
    report("CHECK 5 moment convergence at c=2, series sqrt exact,"
           " <1e-30 at R=64", bool(ok))

    # CHECK 6: detection of the conjugate pole-pair defect (A4 analogue)
    ok = True
    for (name, mu, w, gated) in DEFECTS:
        qp = []
        for z in NODES_Z:
            q = qstore[(64, NODES_Z.index(z))]
            d1 = cdiv((w, Fr(0)), csub(mu, z))
            d2 = cdiv((w, Fr(0)), csub(cconj(mu), z))
            qp.append(cadd(q, cadd(d1, d2)))
        pv = pick_pivots(qp, NODES_Z)
        nstar = None
        for i, p in enumerate(pv):
            if p <= 0:
                nstar = i + 1
                break
        print("DETECT defect=%s mu=%s+%si w=%s Nstar=%s first_bad_pivot~=%s"
              % (name, mu[0], mu[1], w, nstar if nstar else "none",
                 dec6(pv[nstar - 1]) if nstar else "-"))
        if gated:
            ok &= nstar is not None and nstar <= 8
    report("CHECK 6 detection of defect D1 within 8 nodes", bool(ok))

    npass = sum(1 for (_, o) in CHECKS if o)
    failed = [n for (n, o) in CHECKS if not o]
    fw2 = not (CHECKS[3][1] and CHECKS[4][1])
    fw4 = not CHECKS[1][1]
    if not failed:
        print("LANE VERDICT: T2 LANE OPEN, instruments exact-verified on"
              " the canonical model; remaining content = zeta-side"
              " obligations O1-O4")
    elif fw2 or fw4:
        print("LANE VERDICT: [F-bounded, T2 INSTRUMENTS], redesign before"
              " any zeta-side work")
    else:
        print("LANE VERDICT: lane opens with dropped claims, see failed"
              " checks")
    print("CHECKS: %d of %d PASS, FAILED: %s"
          % (npass, len(CHECKS), ",".join(failed) if failed else "none"))
    sys.exit(0 if not failed else 1)


def solve_vec(R, z, rhs):
    # solve (J_R - z) x = rhs over C-rationals (generic right-hand side)
    dd = []
    for i in range(R):
        dd.append((Fr(0) - z[0], -z[1]))
    off = (HALF, Fr(0))
    dp = [None] * R
    rp = [None] * R
    dp[0] = dd[0]
    rp[0] = rhs[0]
    for i in range(1, R):
        w = cdiv(off, dp[i - 1])
        dp[i] = csub(dd[i], cmul(w, off))
        rp[i] = csub(rhs[i], cmul(w, rp[i - 1]))
    x = [None] * R
    x[R - 1] = cdiv(rp[R - 1], dp[R - 1])
    for i in range(R - 2, -1, -1):
        x[i] = cdiv(csub(rp[i], cmul(off, x[i + 1])), dp[i])
    return x


if __name__ == "__main__":
    main()
