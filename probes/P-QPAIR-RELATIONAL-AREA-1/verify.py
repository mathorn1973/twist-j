#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exact audit for P-QPAIR-RELATIONAL-AREA-1 (DRAFT, not pinned).

Authority: none.  Zero-run preregistration verifier.  The written proofs in
PREREG.md carry the universal claims; this standard-library verifier audits
exact generic polynomial identities in eight or twelve variables, exact
Q(zeta_5) witnesses on the integral QPAIR carrier, and the finite pentit
audit family.  It touches no rational piston carrier.  It must not be
imported as a module.

Formal run (only after the immutable pin):
  LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
    python3 probes/P-QPAIR-RELATIONAL-AREA-1/verify.py

Exit code map: 0 pass, 1 STOP (integrity), 2 FALSIFIED (a gate failed).
"""

import sys
from fractions import Fraction
from itertools import product


F = Fraction
ZERO = F(0)
ONE = F(1)
QUARTER = F(1, 4)

FAILURES = []
GATE_COUNT = 0


# ------------------------------------------------------------------- gates

def gate(name, condition, detail=""):
    global GATE_COUNT
    GATE_COUNT += 1
    ok = bool(condition)
    if not ok:
        FAILURES.append(name)
    line = "CHECK %-52s %s" % (name, "PASS" if ok else "FAIL")
    if detail:
        line += "  " + detail
    print(line)


def report(name, value):
    print("REPORT %-51s %s" % (name, value))


# --------------------------------------------------------- Q(zeta_5) exact
# An element is a 4-tuple (c0, c1, c2, c3) meaning c0 + c1 z + c2 z^2 + c3 z^3
# with z^5 = 1 and z^4 = -(1 + z + z^2 + z^3).  Coordinates are Fractions.

def qred(values5):
    c4 = values5[4]
    return (values5[0] - c4, values5[1] - c4, values5[2] - c4,
            values5[3] - c4)


def qint(k):
    return (F(k), ZERO, ZERO, ZERO)


def zpow(exponent):
    values = [ZERO] * 5
    values[exponent % 5] = ONE
    return qred(values)


Q_ZERO = qint(0)
Q_ONE = qint(1)


def qadd(a, b):
    return tuple(a[i] + b[i] for i in range(4))


def qsub(a, b):
    return tuple(a[i] - b[i] for i in range(4))


def qneg(a):
    return tuple(-a[i] for i in range(4))


def qscale(s, a):
    return tuple(F(s) * a[i] for i in range(4))


def qmul(a, b):
    out = [ZERO] * 5
    for i in range(4):
        if a[i] == 0:
            continue
        for j in range(4):
            out[(i + j) % 5] += a[i] * b[j]
    return qred(out)


def qsigma(a, k):
    """Galois automorphism zeta -> zeta^k, k in {1,2,3,4}."""
    out = Q_ZERO
    for i in range(4):
        if a[i] != 0:
            out = qadd(out, qscale(a[i], zpow(i * k)))
    return out


def qconj(a):
    return qsigma(a, 4)


def qnorm_rel(a):
    """N_{K/K+}(a) = a c(a)."""
    return qmul(a, qconj(a))


PHI = qneg(qadd(zpow(2), zpow(3)))          # phi = -z^2 - z^3


def kplus(a):
    """Decompose a c-fixed element as (alpha, beta) with a = alpha + beta phi.
    Returns None when a is not c-fixed."""
    if qconj(a) != a:
        return None
    c0, c1, c2, c3 = a
    if c1 != 0 or c2 != c3:
        return None
    return (c0, -c2)


def kp_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def kp_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def kp_mul(x, y):
    a, b = x
    c, d = y
    return (a * c + b * d, a * d + b * c + b * d)


def kp_conj(x):
    """The other real embedding: phi -> psi = 1 - phi."""
    a, b = x
    return (a + b, -b)


def kp_norm(x):
    return kp_mul(x, kp_conj(x))[0]


def kp_inv(x):
    a, b = x
    nrm = a * a + a * b - b * b
    return ((a + b) / nrm, -b / nrm)


def kp_div(x, y):
    return kp_mul(x, kp_inv(y))


def sign_at(x, place):
    """Exact sign of alpha + beta phi at the real place '+' or '-'."""
    a, b = x
    p = a + b / 2
    q = b / 2 if place == "+" else -b / 2
    if q == 0:
        return (p > 0) - (p < 0)
    if p == 0:
        return (q > 0) - (q < 0)
    if p > 0 and q > 0:
        return 1
    if p < 0 and q < 0:
        return -1
    if p > 0 and q < 0:
        return 1 if p * p > 5 * q * q else -1
    return 1 if 5 * q * q > p * p else -1


def in_unit_quarter(x):
    """0 <= x <= 1/4 at both real places, exactly."""
    upper = kp_sub((QUARTER, ZERO), x)
    return all(sign_at(x, pl) >= 0 and sign_at(upper, pl) >= 0
               for pl in ("+", "-"))


def is_rational_square(r):
    """Exact test whether a nonnegative Fraction is a rational square."""
    if r < 0:
        return False
    num, den = r.numerator, r.denominator

    def isqrt_exact(n):
        if n < 2:
            return n if n * n == n else None
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) // 2
            sq = mid * mid
            if sq == n:
                return mid
            if sq < n:
                lo = mid + 1
            else:
                hi = mid - 1
        return None

    return isqrt_exact(num) is not None and isqrt_exact(den) is not None


# ------------------------------------------------ joint states over Q(zeta)

def joint_data(x):
    """x = (a, b, c, d) in K^4.  Returns D, n, N(D) as Q(zeta) elements."""
    a, b, c, d = x
    D = qsub(qmul(a, d), qmul(b, c))
    n = Q_ZERO
    for t in x:
        n = qadd(n, qnorm_rel(t))
    return D, n, qnorm_rel(D)


def area_kplus(x):
    """A(x) = N(D)/n^2 as (alpha, beta), or None if undefined."""
    D, n, ND = joint_data(x)
    nk = kplus(n)
    ndk = kplus(ND)
    if nk is None or ndk is None or nk == (ZERO, ZERO):
        return None
    return kp_div(ndk, kp_mul(nk, nk))


def disc_kplus(x):
    D, n, ND = joint_data(x)
    nk = kplus(n)
    ndk = kplus(ND)
    return kp_sub(kp_mul(nk, nk), kp_mul((F(4), ZERO), ndk))


def rho_V(x):
    """X c(X)^T as a 2x2 matrix of Q(zeta) elements."""
    a, b, c, d = x
    X = ((a, b), (c, d))
    out = []
    for i in range(2):
        row = []
        for k in range(2):
            s = Q_ZERO
            for j in range(2):
                s = qadd(s, qmul(X[i][j], qconj(X[k][j])))
            row.append(s)
        out.append(tuple(row))
    return tuple(out)


def qdet2(M):
    return qsub(qmul(M[0][0], M[1][1]), qmul(M[0][1], M[1][0]))


def qmat_mul(A, B):
    n = len(A)
    m = len(B[0])
    k = len(B)
    out = []
    for i in range(n):
        row = []
        for j in range(m):
            s = Q_ZERO
            for t in range(k):
                s = qadd(s, qmul(A[i][t], B[t][j]))
            row.append(s)
        out.append(tuple(row))
    return tuple(out)


def qmat_T(A):
    return tuple(tuple(A[i][j] for i in range(len(A)))
                 for j in range(len(A[0])))


def qmat_conj(A):
    return tuple(tuple(qconj(A[i][j]) for j in range(len(A[0])))
                 for i in range(len(A)))


def x_from_matrix(X):
    return (X[0][0], X[0][1], X[1][0], X[1][1])


# ----------------------------------------------------- generic polynomials
# A polynomial is a dict mapping exponent tuples (length NV) to Fractions.

def pclean(p):
    return {m: c for m, c in p.items() if c != 0}


def pconst(nv, value):
    return pclean({(0,) * nv: F(value)})


def pvar(nv, index):
    e = [0] * nv
    e[index] = 1
    return {tuple(e): ONE}


def padd(p, q):
    out = dict(p)
    for m, c in q.items():
        out[m] = out.get(m, ZERO) + c
    return pclean(out)


def pneg(p):
    return {m: -c for m, c in p.items()}


def psub(p, q):
    return padd(p, pneg(q))


def pscale(s, p):
    return pclean({m: F(s) * c for m, c in p.items()})


def pmul(p, q):
    out = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            m = tuple(a + b for a, b in zip(m1, m2))
            out[m] = out.get(m, ZERO) + c1 * c2
    return pclean(out)


def pmap_vars(p, perm):
    """Rename variables: new exponent[perm[i]] = old exponent[i]."""
    out = {}
    for m, c in p.items():
        e = [0] * len(m)
        for i, k in enumerate(m):
            e[perm[i]] += k
        out[tuple(e)] = out.get(tuple(e), ZERO) + c
    return pclean(out)


def pmat_mul(A, B, nv):
    n = len(A)
    m = len(B[0])
    k = len(B)
    out = []
    for i in range(n):
        row = []
        for j in range(m):
            s = pconst(nv, 0)
            for t in range(k):
                s = padd(s, pmul(A[i][t], B[t][j]))
            row.append(s)
        out.append(tuple(row))
    return tuple(out)


def pmat_T(A):
    return tuple(tuple(A[i][j] for i in range(len(A)))
                 for j in range(len(A[0])))


def pdet2(M):
    return psub(pmul(M[0][0], M[1][1]), pmul(M[0][1], M[1][0]))


# ---------------------------------------------- reordered 16-dim kappa audit
# Basis of (V tensor W)^{tensor 2} reordered by R to V_1 V_2 W_1 W_2:
# index (i, k, j, l) for e_i e_k f_j f_l.  alpha swaps i<->k, beta j<->l.

def kappa_coefficient_poly(nv, X):
    """P_-- R(x tensor x) as a dict basis->poly and the kappa coefficient.

    X is a 2x2 matrix of polynomials.  Returns (vector, coefficient) where
    vector is the full 16-component polynomial vector and coefficient is the
    polynomial c with vector == c * kappa, or None if not on the kappa line.
    """
    vec = {}
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    # x tensor x has coefficient X_ij X_kl on (e_i f_j)(e_k f_l),
                    # reordered to (i, k, j, l).
                    vec[(i, k, j, l)] = pmul(X[i][j], X[k][l])

    def apply_swap(v, which):
        out = {}
        for (i, k, j, l), p in v.items():
            if which == "alpha":
                key = (k, i, j, l)
            else:
                key = (i, k, l, j)
            out[key] = padd(out.get(key, pconst(nv, 0)), p)
        return out

    def vsub(u, v):
        keys = set(u) | set(v)
        return {key: psub(u.get(key, pconst(nv, 0)),
                          v.get(key, pconst(nv, 0))) for key in keys}

    def vscale(s, u):
        return {key: pscale(s, p) for key, p in u.items()}

    minus_alpha = vsub(vec, apply_swap(vec, "alpha"))
    minus_both = vsub(minus_alpha, apply_swap(minus_alpha, "beta"))
    proj = vscale(F(1, 4), minus_both)
    # kappa = (e0 wedge e1) tensor (f0 wedge f1)
    kappa = {(0, 1, 0, 1): ONE, (1, 0, 0, 1): -ONE,
             (0, 1, 1, 0): -ONE, (1, 0, 1, 0): ONE}
    coeff = proj.get((0, 1, 0, 1), pconst(nv, 0))
    on_line = True
    for key in product(range(2), repeat=4):
        expected = pscale(kappa.get(key, ZERO), coeff)
        actual = proj.get(key, pconst(nv, 0))
        if pclean(expected) != pclean(actual):
            on_line = False
    return proj, (coeff if on_line else None)


def kappa_coefficient_q(x):
    """Same computation for a concrete Q(zeta) joint state x = (a,b,c,d)."""
    X = ((x[0], x[1]), (x[2], x[3]))
    vec = {}
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    vec[(i, k, j, l)] = qmul(X[i][j], X[k][l])

    def swap(v, which):
        out = {}
        for (i, k, j, l), p in v.items():
            key = (k, i, j, l) if which == "alpha" else (i, k, l, j)
            out[key] = qadd(out.get(key, Q_ZERO), p)
        return out

    def vsub(u, v):
        return {key: qsub(u.get(key, Q_ZERO), v.get(key, Q_ZERO))
                for key in set(u) | set(v)}

    ma = vsub(vec, swap(vec, "alpha"))
    mb = vsub(ma, swap(ma, "beta"))
    proj = {key: qscale(F(1, 4), p) for key, p in mb.items()}
    kappa = {(0, 1, 0, 1): 1, (1, 0, 0, 1): -1,
             (0, 1, 1, 0): -1, (1, 0, 1, 0): 1}
    coeff = proj.get((0, 1, 0, 1), Q_ZERO)
    for key in product(range(2), repeat=4):
        if proj.get(key, Q_ZERO) != qscale(kappa.get(key, 0), coeff):
            return None
    return coeff


# --------------------------------------------------------- rational matrices

def frac_rank(rows):
    M = [list(r) for r in rows]
    nrows = len(M)
    ncols = len(M[0]) if M else 0
    rank = 0
    col = 0
    while rank < nrows and col < ncols:
        pivot = None
        for r in range(rank, nrows):
            if M[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            col += 1
            continue
        M[rank], M[pivot] = M[pivot], M[rank]
        pv = M[rank][col]
        M[rank] = [v / pv for v in M[rank]]
        for r in range(nrows):
            if r != rank and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[rank])]
        rank += 1
        col += 1
    return rank


# ------------------------------------------------------------------- main

def main():
    print("P-QPAIR-RELATIONAL-AREA-1 verifier (DRAFT)")
    print("two typed slots, two determinant forms: det(X c(X)^T) = N(D) and "
          "P_-- R(x tensor x) = (D/2) kappa; the area N(D)/n^2 in K+ and "
          "its two real embeddings")
    print("")

    if len(sys.argv) != 1:
        raise RuntimeError("no arguments accepted")
    gate("I01.environment", sys.version_info >= (3, 8))

    # ============================================================== R1
    # Eight variables: a b c d ab bb cb db ; the involution swaps i <-> i+4.
    NV = 8
    a, b, c, d = (pvar(NV, i) for i in range(4))
    ab, bb, cb, db = (pvar(NV, i) for i in range(4, 8))
    X = ((a, b), (c, d))
    Xbar = ((ab, bb), (cb, db))
    rhoV = pmat_mul(X, pmat_T(Xbar), NV)
    rhoW = pmat_mul(pmat_T(X), Xbar, NV)
    D = pdet2(X)
    Dbar = pdet2(Xbar)
    ND = pmul(D, Dbar)
    n = pconst(NV, 0)
    for i in range(2):
        for j in range(2):
            n = padd(n, pmul(X[i][j], Xbar[i][j]))
    trV = padd(rhoV[0][0], rhoV[1][1])
    trW = padd(rhoW[0][0], rhoW[1][1])
    gate("R1a.partial-trace.rhoV.explicit",
         rhoV[0][0] == padd(pmul(a, ab), pmul(b, bb))
         and rhoV[0][1] == padd(pmul(a, cb), pmul(b, db))
         and rhoV[1][0] == padd(pmul(c, ab), pmul(d, bb))
         and rhoV[1][1] == padd(pmul(c, cb), pmul(d, db)))
    gate("R1a.traces.equal.n", trV == n and trW == n)
    gate("R1a.det.rhoV.equals.N(D)", pdet2(rhoV) == ND)
    gate("R1a.det.rhoW.equals.N(D)", pdet2(rhoW) == ND)
    swap_bar = [4, 5, 6, 7, 0, 1, 2, 3]
    gate("R1a.N(D).c-fixed", pmap_vars(ND, swap_bar) == ND)
    gate("R1a.n.c-fixed", pmap_vars(n, swap_bar) == n)

    p_ = rhoV[0][0]
    q_ = rhoV[1][1]
    z_ = rhoV[0][1]
    zc_ = rhoV[1][0]
    disc = psub(pmul(n, n), pscale(4, ND))
    pyth = padd(pmul(psub(p_, q_), psub(p_, q_)), pscale(4, pmul(z_, zc_)))
    gate("R1b.discriminant.identity", disc == pyth)
    gate("R1b.pythagorean.beta+4A=1.numerators",
         padd(pyth, pscale(4, ND)) == pmul(n, n))
    gate("R1b.rhoV.offdiagonal.c-conjugate", pmap_vars(z_, swap_bar) == zc_)

    proj, coeff = kappa_coefficient_poly(NV, X)
    gate("R1c.kappa.coefficient.(ad-bc)/2",
         coeff is not None and coeff == pscale(F(1, 2), D))
    gate("R1c.projection.rank-one.line",
         coeff is not None
         and sum(1 for key, p in proj.items() if pclean(p)) == 4)
    if coeff is not None:
        coeff_bar = pmap_vars(coeff, swap_bar)
        gate("R1c.slot-comparison.4N(kappa)=det.rhoV",
             pscale(4, pmul(coeff, coeff_bar)) == pdet2(rhoV))
    else:
        gate("R1c.slot-comparison.4N(kappa)=det.rhoV", False)

    x0 = (Q_ONE, Q_ZERO, Q_ZERO, Q_ONE)
    u = zpow(1)
    xu = tuple(qmul(u, t) for t in x0)
    gate("R1d.phase.u.c(u)=1", qnorm_rel(u) == Q_ONE)
    gate("R1d.phase.H-slots.equal", rho_V(x0) == rho_V(xu)
         and all(qmul(s, qconj(t)) == qmul(su, qconj(tu))
                 for s, t, su, tu in
                 [(x0[i], x0[j], xu[i], xu[j])
                  for i in range(4) for j in range(4)]))
    D0 = joint_data(x0)[0]
    Du = joint_data(xu)[0]
    gate("R1d.phase.D.changes.by.u^2", D0 == Q_ONE and Du == zpow(2)
         and Du != D0)
    gate("R1d.phase.S-slots.differ",
         any(qmul(x0[i], x0[j]) != qmul(xu[i], xu[j])
             for i in range(4) for j in range(4)))
    gate("R1d.phase.trivial-involution.u^2=1",
         all(F(s) * F(s) == ONE for s in (1, -1)))

    # R1e: generic characters with 12 variables a b c d g11 g12 g21 g22
    # h11 h12 h21 h22 (no bars needed for D).
    NV2 = 12
    va = [pvar(NV2, i) for i in range(12)]
    Xg = ((va[0], va[1]), (va[2], va[3]))
    g = ((va[4], va[5]), (va[6], va[7]))
    h = ((va[8], va[9]), (va[10], va[11]))
    Xt = pmat_mul(pmat_mul(g, Xg, NV2), pmat_T(h), NV2)
    gate("R1e.character.D->det(g)det(h)D",
         pdet2(Xt) == pmul(pmul(pdet2(g), pdet2(h)), pdet2(Xg)))
    # exact Q(zeta) audit of the N(D) character and unitary invariance;
    # g = ((1+zeta, 1), (0, zeta)) with det (1+zeta) zeta, h = ((2,0),(1,1))
    # with det 2, neither unimodular
    G1 = ((qadd(Q_ONE, zpow(1)), Q_ONE), (Q_ZERO, zpow(1)))
    H1 = ((qint(2), Q_ZERO), (Q_ONE, Q_ONE))
    S0 = ((Q_ZERO, qneg(Q_ONE)), (Q_ONE, Q_ZERO))
    Xw = ((Q_ONE, Q_ONE), (Q_ZERO, PHI))
    Xw_t = qmat_mul(qmat_mul(G1, Xw), qmat_T(H1))
    Dw = qdet2(Xw)
    Dw_t = qdet2(Xw_t)
    detgh = qmul(qdet2(G1), qdet2(H1))
    gate("R1e.witness.det(g)det(h).nonunit",
         qnorm_rel(detgh) != Q_ONE and detgh != Q_ZERO)
    gate("R1e.witness.D.character", Dw_t == qmul(detgh, Dw))
    gate("R1e.witness.N(D).character",
         qnorm_rel(Dw_t) == qmul(qnorm_rel(detgh), qnorm_rel(Dw)))
    # unitary locals: S0 (real orthogonal) and diag(zeta, zeta^4)
    U2 = ((zpow(1), Q_ZERO), (Q_ZERO, zpow(4)))
    unitary_ok = (qmat_mul(S0, qmat_conj(qmat_T(S0))) == ((Q_ONE, Q_ZERO), (Q_ZERO, Q_ONE))
                  and qmat_mul(qmat_T(U2), qmat_conj(U2)) == ((Q_ONE, Q_ZERO), (Q_ZERO, Q_ONE)))
    Xw_u = qmat_mul(qmat_mul(S0, Xw), qmat_T(U2))
    lam = qadd(Q_ONE, zpow(1))
    Xw_s = tuple(tuple(qmul(lam, Xw[i][j]) for j in range(2)) for i in range(2))
    gate("R1e.witness.A.local-unitary.and.scalar.invariant",
         unitary_ok
         and area_kplus(x_from_matrix(Xw_u)) == area_kplus(x_from_matrix(Xw))
         and area_kplus(x_from_matrix(Xw_s)) == area_kplus(x_from_matrix(Xw)))

    # ============================================================== R2
    zeta = zpow(1)
    witnesses = [
        ("(1,0,0,1)", (Q_ONE, Q_ZERO, Q_ZERO, Q_ONE), (QUARTER, ZERO), "blind"),
        ("(1,0,0,phi)", (Q_ONE, Q_ZERO, Q_ZERO, PHI), (F(1, 5), ZERO), "blind"),
        ("(1,zeta,0,1)", (Q_ONE, zeta, Q_ZERO, Q_ONE), (F(1, 9), ZERO), "blind"),
        ("(1,1,0,phi)", (Q_ONE, Q_ONE, Q_ZERO, PHI),
         (F(10, 121), F(3, 121)), "split+"),
        ("(1,1,1,1+zeta)", (Q_ONE, Q_ONE, Q_ONE, qadd(Q_ONE, zeta)),
         (F(26, 361), F(-9, 361)), "split-"),
    ]
    for name, x, expected, kind in witnesses:
        A = area_kplus(x)
        gate("R2a.witness.%s.area.exact" % name, A == expected)
        if A is None:
            gate("R2a.witness.%s.place-order" % name, False)
            gate("R2b.witness.%s.bounds" % name, False)
            gate("R2d.witness.%s.Gal(K+/Q).indexing" % name, False)
            continue
        diff = kp_sub(A, kp_conj(A))   # iota_+(A) - iota_-(A) has sign of diff at +
        s_plus = sign_at(diff, "+")
        if kind == "blind":
            gate("R2a.witness.%s.place-order" % name, A[1] == 0 and s_plus == 0)
        elif kind == "split+":
            gate("R2a.witness.%s.place-order" % name, A[1] != 0 and s_plus > 0)
        else:
            gate("R2a.witness.%s.place-order" % name, A[1] != 0 and s_plus < 0)
        gate("R2b.witness.%s.bounds" % name, in_unit_quarter(A))
        D_, n_, ND_ = joint_data(x)
        gate("R2d.witness.%s.Gal(K+/Q).indexing" % name,
             qsigma(ND_, 2) == qsigma(ND_, 3) and qsigma(ND_, 1) == qsigma(ND_, 4)
             and qsigma(n_, 2) == qsigma(n_, 3) and qsigma(n_, 1) == qsigma(n_, 4)
             and kplus(qsigma(ND_, 2)) == kp_conj(kplus(ND_))
             and kplus(qsigma(n_, 2)) == kp_conj(kplus(n_)))
    # exact real embeddings of the split witnesses, as reports (R2 algebra)
    for name, x, expected, kind in witnesses:
        A = area_kplus(x)
        if A is not None and A[1] != 0:
            # alpha + beta phi = (2 alpha + beta)/2 + (beta/2) sqrt5
            report("R2r.embedding.{1,4}.%s" % name,
                   "(%s) + (%s)*sqrt5" % (A[0] + A[1] / 2, A[1] / 2))
            report("R2r.embedding.{2,3}.%s" % name,
                   "(%s) - (%s)*sqrt5" % (A[0] + A[1] / 2, A[1] / 2))

    # R2c discriminant witnesses
    xw = (Q_ONE, Q_ONE, Q_ZERO, PHI)
    dw = disc_kplus(xw)
    gate("R2c.disc.(1,1,0,phi).equals.6+3phi", dw == (F(6), F(3)))
    gate("R2c.disc.norm.45.not.square",
         kp_norm(dw) == F(45) and not is_rational_square(kp_norm(dw)))
    x2 = (qint(2), Q_ZERO, Q_ZERO, Q_ONE)
    d2 = disc_kplus(x2)
    n2k = kplus(joint_data(x2)[1])
    gate("R2c.disc.(2,0,0,1).equals.9.weights.4.1",
         d2 == (F(9), ZERO) and n2k == (F(5), ZERO)
         and (F(5) + F(3)) / 2 == F(4) and (F(5) - F(3)) / 2 == F(1))
    gate("R2c.(1,1,0,phi).N(D).integral.1+phi",
         kplus(joint_data(xw)[2]) == (F(1), F(1)))

    # R2b / R2v pentit family census with integer arithmetic
    # pentits: 0 and +-zeta^k as integer 4-tuples in the power basis
    def ired(v5):
        c4 = v5[4]
        return (v5[0] - c4, v5[1] - c4, v5[2] - c4, v5[3] - c4)

    def imul(x, y):
        out = [0] * 5
        for i in range(4):
            if x[i]:
                for j in range(4):
                    out[(i + j) % 5] += x[i] * y[j]
        return ired(out)

    def iadd(x, y):
        return (x[0] + y[0], x[1] + y[1], x[2] + y[2], x[3] + y[3])

    def isub(x, y):
        return (x[0] - y[0], x[1] - y[1], x[2] - y[2], x[3] - y[3])

    def iconj(x):
        # zeta -> zeta^4 : coefficient of zeta^i goes to zeta^(4i mod 5)
        out = [0] * 5
        for i in range(4):
            out[(4 * i) % 5] += x[i]
        return ired(out)

    def izpow(k):
        v = [0] * 5
        v[k % 5] = 1
        return ired(v)

    izero = (0, 0, 0, 0)
    pentits = [izero] + [izpow(k) for k in range(5)] + \
        [tuple(-t for t in izpow(k)) for k in range(5)]
    counts = {"states": 0, "blind": 0, "split": 0, "max": 0, "zero": 0,
              "violations": 0}
    area_values = {}
    for x in product(pentits, repeat=4):
        if all(t == izero for t in x):
            continue
        counts["states"] += 1
        Dp = isub(imul(x[0], x[3]), imul(x[1], x[2]))
        NDp = imul(Dp, iconj(Dp))
        nn = sum(1 for t in x if t != izero)   # n = number of nonzero pentits
        # N(D) as alpha + beta phi
        assert NDp[1] == 0 and NDp[2] == NDp[3]
        A = (F(NDp[0], nn * nn), F(-NDp[2], nn * nn))
        if not in_unit_quarter(A):
            counts["violations"] += 1
        if A[1] == 0:
            counts["blind"] += 1
        else:
            counts["split"] += 1
        if A == (QUARTER, ZERO):
            counts["max"] += 1
        if NDp == izero:
            counts["zero"] += 1
        area_values[A] = area_values.get(A, 0) + 1
    gate("R2b.pentit.family.size.14640", counts["states"] == 14640)
    gate("R2b.pentit.family.bounds.no.violation", counts["violations"] == 0)
    report("R2v.pentit.place-blind", counts["blind"])
    report("R2v.pentit.place-split", counts["split"])
    report("R2v.pentit.area.1/4", counts["max"])
    report("R2v.pentit.area.0", counts["zero"])
    report("R2v.pentit.distinct.areas", len(area_values))
    for A in sorted(area_values, key=lambda t: (t[0] + t[1] / 2, t[1])):
        report("R2v.pentit.area.(%s)+(%s)phi" % (A[0], A[1]), area_values[A])

    print("")
    print("gates: %d  failures: %d" % (GATE_COUNT, len(FAILURES)))
    if FAILURES:
        for name in FAILURES:
            print("FALSIFIED %s" % name)
        print("RESULT FALSIFIED")
        return 2
    print("RESULT PASS")
    return 0


if __name__ == "__main__":
    try:
        code = main()
    except Exception as exc:  # integrity, not science
        print("STOP %s: %s" % (type(exc).__name__, exc))
        code = 1
    sys.stdout.flush()
    sys.exit(code)

