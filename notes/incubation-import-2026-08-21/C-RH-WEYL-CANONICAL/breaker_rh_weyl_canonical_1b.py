#!/usr/bin/env python3
# breaker_rh_weyl_canonical_1b.py
# Correction breaker for P-RH-WEYL-CANONICAL-1, prompted by the owner-side
# independent review of PR #6. NO AUTHORITY. Discharges the FW5 obligation
# that breaker 1 left unmet, and machine-verifies the rank-two threshold
# identity adopted for the lane. Independent paths: dense Fraction LU (no
# tridiagonal shortcut), dense float LU, direct exact determinants.
import math
from fractions import Fraction as Fr

FINDINGS = []


def note(s):
    print(s)


# ---------- exact complex rationals ----------
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


def dense_solve_exact(R, z, rhs):
    # dense Gaussian elimination over Q(i), no pivToting tricks, independent
    # of the verifier's tridiagonal Thomas path
    A = [[CZERO] * R for _ in range(R)]
    for i in range(R):
        A[i][i] = (Fr(0) - z[0], -z[1])
        if i + 1 < R:
            A[i][i + 1] = (Fr(1, 2), Fr(0))
            A[i + 1][i] = (Fr(1, 2), Fr(0))
    b = list(rhs)
    for col in range(R):
        piv = A[col][col]
        if piv == CZERO:
            raise RuntimeError("zero pivot")
        for r in range(col + 1, R):
            if A[r][col] == CZERO:
                continue
            f = cdiv(A[r][col], piv)
            for c in range(col, R):
                A[r][c] = csub(A[r][c], cmul(f, A[col][c]))
            b[r] = csub(b[r], cmul(f, b[col]))
    x = [CZERO] * R
    for r in range(R - 1, -1, -1):
        s = b[r]
        for c in range(r + 1, R):
            s = csub(s, cmul(A[r][c], x[c]))
        x[r] = cdiv(s, A[r][r])
    return x


def dense_solve_float(R, c, rhs):
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
                for cc in range(col, R):
                    A[r][cc] -= f * A[col][cc]
                b[r] -= f * b[col]
    x = [0.0] * R
    for r in range(R - 1, -1, -1):
        s = b[r]
        for cc in range(r + 1, R):
            s -= A[r][cc] * x[cc]
        x[r] = s / A[r][r]
    return x


note("P-RH-WEYL-CANONICAL-1 correction breaker 1b (no authority)")
note("purpose: discharge FW5 for real, and machine-verify the rank-two")
note("threshold identity; prompted by the owner-side review of PR #6")

# ---------- C1: the REAL FW5: finite moments at c = 2, two paths ----------
note("C1 FW5 discharge: finite Q_R Taylor coefficients at c = 2,")
note("   dense-exact vs dense-float, and distance to the Q(sqrt3) limit")
KMAX = 6
# exact limit coefficients, independently: m(2+t) = -4 - 2t + 2 g(t),
# g = sqrt(3+4t+t^2), computed here by DIRECT recursion from
# (3+4t+t^2) g'' relation avoided; use g_j from g^2 = F matching instead
ORD = KMAX + 1
F = [Fr(3), Fr(4), Fr(1)] + [Fr(0)] * (ORD - 3)
# g_j = p_j + q_j sqrt3 as pairs; solve g^2 = F coefficientwise
g = [(Fr(0), Fr(1))] + [(Fr(0), Fr(0))] * (ORD - 1)
for s in range(1, ORD):
    acc = (F[s], Fr(0))
    for j in range(1, s):
        pj, qj = g[j]
        pk, qk = g[s - j]
        acc = (acc[0] - (pj * pk + 3 * qj * qk), acc[1] - (pj * qk + qj * pk))
    # acc = 2 g0 g_s => g_s = acc / (2 sqrt3) ; with g0 = (0,1):
    # (p,q)/(2 sqrt3) = (q*3, p)/(6)  since dividing by sqrt3 maps
    # p + q sqrt3 -> q + (p/3) sqrt3
    p, q = acc
    g[s] = (q / 2, p / 6)  # division of p + q sqrt3 by 2 sqrt3
mlim = []
for j in range(ORD):
    p, q = g[j]
    p2, q2 = 2 * p, 2 * q
    if j == 0:
        p2 -= 4
    if j == 1:
        p2 -= 2
    mlim.append((p2, q2))
# certified sqrt3 bracket
from math import isqrt
n3 = isqrt(3 * 10 ** 80)
S3LO = Fr(n3, 10 ** 40)
S3HI = Fr(n3 + 1, 10 ** 40)
assert S3LO * S3LO <= 3 <= S3HI * S3HI
ok_all = True
for R in [4, 8, 16, 32, 64]:
    vec = [CONE if i == 0 else CZERO for i in range(R)]
    vecf = [1.0 if i == 0 else 0.0 for i in range(R)]
    for k in range(KMAX + 1):
        vec = dense_solve_exact(R, (Fr(2), Fr(0)), vec)
        vecf = dense_solve_float(R, 2.0, vecf)
        ce = vec[0][0]
        cf = vecf[0]
        rel = abs(float(ce) - cf) / max(1e-300, abs(cf))
        p, q = mlim[k]
        end1 = p + q * S3LO
        end2 = p + q * S3HI
        dist = max(abs(ce - end1), abs(ce - end2))
        line = ("  R=%d k=%d exact_vs_float_rel=%.1e dist_to_limit<%.3e"
                % (R, k, rel, float(dist)))
        note(line)
        if rel > 1e-11:
            ok_all = False
            FINDINGS.append("C1 float/exact mismatch R=%d k=%d" % (R, k))
        if R == 64 and not dist < Fr(1, 10 ** 30):
            ok_all = False
            FINDINGS.append("C1 R=64 distance not < 1e-30 at k=%d" % k)
note("C1 verdict: %s (this independently reproduces the verifier CHECK 5"
     % ("OK" if ok_all else "DISCREPANCY"))
note("   verdict; breaker 1 never computed these finite moments)")

# ---------- C2: rank-two threshold identity, exact -------------------
note("C2 rank-two threshold identity, exact machine check at N = 8")
NODES_A = [Fr(1) + Fr(1, n) for n in range(1, 9)]
NODES_Z = [(Fr(0), a) for a in NODES_A]
q64 = []
for z in NODES_Z:
    vec = [CONE if i == 0 else CZERO for i in range(64)]
    x = dense_solve_exact(64, z, vec)
    q64.append(x[0])


def pick_matrix(qvals, zs):
    N = len(zs)
    return [[cdiv(csub(qvals[j], cconj(qvals[k])),
                  csub(zs[j], cconj(zs[k]))) for k in range(N)]
            for j in range(N)]


def cdet(M):
    # exact determinant over Q(i), Gaussian elimination (fraction-free not
    # needed at N = 8)
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


def solve_lin(M, rhs):
    N = len(M)
    A = [row[:] + [rhs[i]] for i, row in enumerate(M)]
    for col in range(N):
        piv = A[col][col]
        for r in range(col + 1, N):
            if A[r][col] == CZERO:
                continue
            f = cdiv(A[r][col], piv)
            for c in range(col, N + 1):
                A[r][c] = csub(A[r][c], cmul(f, A[col][c]))
    x = [CZERO] * N
    for r in range(N - 1, -1, -1):
        s = A[r][N]
        for c in range(r + 1, N):
            s = csub(s, cmul(A[r][c], x[c]))
        x[r] = cdiv(s, A[r][r])
    return x


P0 = pick_matrix(q64, NODES_Z)
DEFECTS = [
    ("D1", (Fr(1, 3), Fr(1, 10)), Fr(1, 10)),
    ("D2", (Fr(9, 10), Fr(1, 10)), Fr(1, 10)),
    ("D3", (Fr(1, 3), Fr(1, 100)), Fr(1, 100)),
]
for (name, mu, w) in DEFECTS:
    A = [cdiv(CONE, csub(mu, z)) for z in NODES_Z]
    B = [cdiv(CONE, csub(cconj(mu), z)) for z in NODES_Z]
    # alpha = A* P0^-1 A etc.
    x = solve_lin(P0, A)
    y = solve_lin(P0, B)
    alpha = CZERO
    beta = CZERO
    gamma = CZERO
    for i in range(8):
        alpha = cadd(alpha, cmul(cconj(A[i]), x[i]))
        beta = cadd(beta, cmul(cconj(B[i]), y[i]))
        gamma = cadd(gamma, cmul(cconj(A[i]), y[i]))
    assert alpha[1] == 0 and beta[1] == 0, "alpha, beta must be real"
    D = alpha[0] * beta[0] - (gamma[0] * gamma[0] + gamma[1] * gamma[1])
    reg = gamma[0]
    note("  %s: alpha>0:%s beta>0:%s Re(gamma)~%.6e D~%.6e (D>=0:%s)"
         % (name, alpha[0] > 0, beta[0] > 0, float(reg), float(D), D >= 0))
    det0 = cdet(P0)
    identity_ok = True
    for wtest in [w, Fr(1, 100), Fr(1)]:
        Pw = [[cadd(P0[j][k],
                    cmul((wtest, Fr(0)),
                         cadd(cmul(A[j], cconj(B[k])),
                              cmul(B[j], cconj(A[k])))))
               for k in range(8)] for j in range(8)]
        detw = cdet(Pw)
        ratio = cdiv(detw, det0)
        pred = (Fr(1) + 2 * wtest * reg - wtest * wtest * D, Fr(0))
        if ratio != pred:
            identity_ok = False
            FINDINGS.append("C2 identity FAILS %s w=%s" % (name, wtest))
    note("  %s: det P(w)/det P0 == 1 + 2w Re(gamma) - w^2 D exact at 3 w"
         " values: %s" % (name, "OK" if identity_ok else "FAIL"))
    # threshold verdict at the frozen weight, full 8x8 block only
    quad = Fr(1) + 2 * w * reg - w * w * D
    note("  %s: full-block quadratic at frozen w: sign=%+d (negative means"
         " a negative direction inside N=8)" % (name, (quad > 0) - (quad < 0)))
    # certified bracket of w* when D > 0
    if D > 0:
        lo, hi = Fr(0), Fr(1)
        while Fr(1) + 2 * hi * reg - hi * hi * D > 0:
            hi *= 2
        for _ in range(60):
            mid = (lo + hi) / 2
            if Fr(1) + 2 * mid * reg - mid * mid * D > 0:
                lo = mid
            else:
                hi = mid
        note("  %s: w*(N=8, full block) in [%.6e, %.6e]"
             % (name, float(lo), float(hi)))

note("C2 note: the identity is the 2x2 reduction of the rank-two update")
note("   P(w) = P0 + w(AB* + BA*); D >= 0 is Cauchy-Schwarz in the P0^-1")
note("   inner product with equality iff A parallel B; above w* there is")
note("   at most one negative direction by the rank-one comparison")
note("   P(w) >= P0 - w lambda_- v v*.")

note("FINDINGS: %d" % len(FINDINGS))
for f in FINDINGS:
    note("  " + f)
note("breaker 1b done")
