#!/usr/bin/env python3
"""Exact finite census of the conditional native-classical two-cut contact.

Accepted verifier for P-NATIVE-CLASSICAL-CONTACT-CENSUS-1.
The complete frozen contract is PREREG.md in this directory.
Original work: A. M. Thorn, Apache-2.0.

Standard library only. All arithmetic is exact: integers mod 5 on the
native side, fractions.Fraction on the classical side. No floats.
Comparison tables are embedded from the audited published proof; every
computed quantity is derived here from the frozen contract definitions.
"""

from fractions import Fraction
from itertools import product

F = Fraction


def require(cond, msg):
    if not cond:
        raise AssertionError(msg)


# ---------------------------------------------------------------- native side

def g0(x):
    a, b, c, d, q, r = x
    return (b, a, d, c, q, r)


def g1(x):
    a, b, c, d, q, r = x
    return ((-c) % 5, (-d) % 5, (-a) % 5, (-b) % 5, (-q) % 5, (-r) % 5)


def g2(x):
    a, b, c, d, q, r = x
    return ((2 - c) % 5, (1 + r - d) % 5, (2 - a) % 5,
            (1 - r - b) % 5, (1 - q) % 5, (-r) % 5)


def g3(x):
    a, b, c, d, q, r = x
    return ((2 - a) % 5, (1 - b) % 5, (3 - c) % 5,
            (4 - d) % 5, (1 - q) % 5, (1 - r) % 5)


def g4(x):
    a, b, c, d, q, r = x
    return ((2 - a) % 5, (1 - b) % 5, (3 - c) % 5,
            (4 - d) % 5, (2 - q) % 5, (1 - r) % 5)


GENS = (g0, g1, g2, g3, g4)
SUM_MAP = (
    lambda z: z % 5,
    lambda z: (-z) % 5,
    lambda z: (2 - z) % 5,
    lambda z: (2 - z) % 5,
    lambda z: (3 - z) % 5,
)


def theta(n):
    return bin(n).count("1") % 2


# Published tables (comparison targets only), PROOF sections 1, 2 and 4.
BRANCH = {  # h: (j0,j1,j2), C1, C2, C3
    0: ((1, 1, 3), (0, 4), (0, 1), (1, 0)),
    1: ((2, 2, 4), (1, 4), (0, 1), (2, 0)),
    2: ((3, 1, 3), (1, 0), (4, 0), (2, 1)),
    3: ((4, 1, 3), (2, 0), (3, 0), (3, 1)),
    4: ((0, 2, 4), (0, 1), (1, 4), (1, 2)),
}
ENC = {  # h: (encoding E, preparation work)
    0: ((F(0), F(0), F(0), F(0)), F(0)),
    1: ((F(1, 2), F(0), F(0), F(0)), F(1, 10)),
    2: ((F(1, 2), F(1, 2), F(0), F(0)), F(3, 20)),
    3: ((F(1), F(1, 2), F(0), F(0)), F(2, 5)),
    4: ((F(0), F(1), F(0), F(0)), F(2, 5)),
}
B0_NUM = {  # 12960 * b0 by h
    0: (0, 0, 0, 0),
    1: (-1421, 354, 354, 348),
    2: (-1072, -1062, 708, 696),
    3: (-2493, -708, 1062, 1044),
    4: (698, -2832, 708, 696),
}
B1_NUM = {  # 1399680 * b1 by h
    0: (0, 0, 0, 0),
    1: (192202, -47829, -47829, -48879),
    2: (143434, 145312, -95658, -97758),
    3: (335636, 97483, -143487, -146637),
    4: (-97536, 386282, -95658, -97758),
}
ELL = (0, 1, 2, -2, -1)


def eta(q, r):
    return (F(ELL[q], 2), F(ELL[r] + 1, 2), F(0), F(0))


def expected_x3_pistons(h, p):
    p0, p1, p2, p3 = p
    if h in (0, 1):
        v = (2 - p0, 1 - p1, 3 - p2, 4 - p3)
    elif h in (2, 3):
        v = (-p2, -p3, -p0, -p1)
    else:
        v = (p3, p2 - 1, p1 + 1, p0 - 1)
    return tuple(t % 5 for t in v)


def native_run(p):
    """Three unchanged ticks from (0;(p,0,1)). Returns (js, x1, x2, x3)."""
    x = (p[0], p[1], p[2], p[3], 0, 1)
    js, xs = [], []
    for n in range(3):
        j = (sum(x) + 2 * theta(n)) % 5
        js.append(j)
        x = GENS[j](x)
        xs.append(x)
    return tuple(js), xs[0], xs[1], xs[2]


# ------------------------------------------------------------ classical side
# Sparse exact-rational wave vectors: dict site -> Fraction, zero omitted.
# Sites are integer triples; fields are zero outside the finite set D.

SHELL_W = {2: 6, 4: 1, 8: 15, 10: 1, 16: 1}
Y = ((0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1), (2, 0, 0))
R_SITES = Y[:4]


def build_stencil():
    B = []
    for d in product(range(-4, 5), repeat=3):
        n2 = d[0] * d[0] + d[1] * d[1] + d[2] * d[2]
        if n2 in SHELL_W and sum(d) % 2 == 0:
            B.append((d, F(SHELL_W[n2], 324)))
    return B


B_STENCIL = build_stencil()
B_ZERO = [d for d, _ in B_STENCIL] + [(0, 0, 0)]
C_DIAG = sum(c for _, c in B_STENCIL)


def add3(x, y):
    return (x[0] + y[0], x[1] + y[1], x[2] + y[2])


def minkowski(A, Bs):
    return {add3(a, b) for a in A for b in Bs}


D_SET = minkowski(minkowski(set(Y), B_ZERO), B_ZERO)
Y1_SET = minkowski(set(Y), B_ZERO)


def w_clean(v):
    return {x: t for x, t in v.items() if t != 0}


def w_add(u, v, s=F(1)):
    out = dict(u)
    for x, t in v.items():
        out[x] = out.get(x, F(0)) + s * t
    return w_clean(out)


def w_scale(u, s):
    if s == 0:
        return {}
    return {x: s * t for x, t in u.items()}


def w_dot(u, v):
    if len(u) > len(v):
        u, v = v, u
    return sum((t * v.get(x, F(0)) for x, t in u.items()), F(0))


def apply_L(f):
    """Principal Dirichlet operator: diagonal C_DIAG everywhere on D,
    off-diagonal -c_d to neighbours inside D, zero extension outside."""
    out = {}
    for y, fy in f.items():
        out[y] = out.get(y, F(0)) + C_DIAG * fy
        for d, cd in B_STENCIL:
            x = (y[0] - d[0], y[1] - d[1], y[2] - d[2])
            if x in D_SET:
                out[x] = out.get(x, F(0)) - cd * fy
    return w_clean(out)


def apply_H(f):
    return w_add(w_scale(f, F(2)), apply_L(f), F(-1))


def apply_J(f):  # J = I - P P^T  (C/2 with G = 2I)
    out = dict(f)
    for y in R_SITES:
        out.pop(y, None)
    return w_clean(out)


def apply_K(f):  # K = (I + P P^T)^-1: 1/2 on R, 1 elsewhere
    out = {}
    for x, t in f.items():
        out[x] = t / 2 if x in R_SITES else t
    return w_clean(out)


def insert_P(a):
    return w_clean({R_SITES[j]: a[j] for j in range(4)})


def apply_PT(f):
    return tuple(f.get(y, F(0)) for y in R_SITES)


def energy_D(u, v):
    diff = w_add(v, u, F(-1))
    return (w_dot(diff, diff) + w_dot(u, apply_L(v))) / F(2)


def q_g(a):
    return 2 * sum(t * t for t in a)


def source_S(z):
    s = sum(z)
    out = {}
    for i in range(4):
        out[Y[i]] = z[i] - s / 5
    out[Y[4]] = -s / 5
    return w_clean(out)


ZERO4 = (F(0), F(0), F(0), F(0))


def couple(wave, a):
    """Couple((u,v),a) = ((v,w),b), contract section 3 / lane R eq. (4)."""
    u, v = wave
    rhs = apply_H(v)
    rhs = w_add(rhs, apply_J(u), F(-1))
    rhs = w_add(rhs, insert_P(tuple(4 * t for t in a)))  # 2 P G a, G = 2I
    w = apply_K(rhs)
    p = tuple(t / 2 for t in apply_PT(w_add(w, u, F(-1))))
    b = tuple(a[j] - p[j] for j in range(4))
    return (v, w), b


def couple_inv(wave, b):
    """Inverse (5): from ((v,w),b) recover ((u,v),a) as (u, a); caller
    keeps v. Returns (u, a)."""
    v, w = wave
    rhs = apply_H(v)
    rhs = w_add(rhs, apply_J(w), F(-1))
    rhs = w_add(rhs, insert_P(tuple(4 * t for t in b)))  # 2 P G b
    u = apply_K(rhs)
    p = tuple(t / 2 for t in apply_PT(w_add(w, u, F(-1))))
    a = tuple(b[j] + p[j] for j in range(4))
    return u, a


def F_step(X):
    (wave, A, Bt, k) = X
    wave2, b = couple(wave, A[0])
    return (wave2, (A[1], Bt[1]), (b, Bt[0]), 1 - k)


def F_inv(X):
    (wave, A, Bt, k) = X
    v = wave[0]
    u, a = couple_inv(wave, Bt[0])
    return (((u, v)), (a, A[0]), (Bt[1], A[1]), 1 - k)


def energy_full(X):
    (u, v), A, Bt, _k = X
    return energy_D(u, v) + sum(q_g(t) for t in (A[0], A[1], Bt[0], Bt[1]))


X_BLANK = ((dict(), dict()), (ZERO4, ZERO4), (ZERO4, ZERO4), 0)


# ------------------------------------------------------------------- contact

def contact(wave, led, z):
    """C: (u,v,w) -> (u, v+Sz, w + E_D(u,v+Sz) - E_D(u,v)). Tapes/pointer
    and the native state are unchanged by C and are handled by callers."""
    u, v = wave
    v2 = w_add(v, source_S(z))
    return (u, v2), led + energy_D(u, v2) - energy_D(u, v)


def contact_inv(wave, led, z):
    u, v2 = wave
    v = w_add(v2, source_S(z), F(-1))
    return (u, v), led - energy_D(u, v2) + energy_D(u, v)


def cold_run(z, c0=ZERO4, c1=ZERO4):
    """Two F steps from X0(z;c0,c1). Returns (X0, X1, X2, b0, b1)."""
    X0 = (((dict(), source_S(z))), (ZERO4, ZERO4), (c0, c1), 0)
    X1 = F_step(X0)
    X2 = F_step(X1)
    return X0, X1, X2, X1[2][0], X2[2][0]


# ------------------------------------------------------- exact linear algebra

def mat_det_inv(M):
    """Exact determinant and inverse of a 4x4 Fraction matrix (rows)."""
    n = 4
    A = [list(M[i]) + [F(1) if i == j else F(0) for j in range(n)]
         for i in range(n)]
    det, sign = F(1), 1
    for col in range(n):
        piv = next((r for r in range(col, n) if A[r][col] != 0), None)
        require(piv is not None, "response matrix M is singular")
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            sign = -sign
        pv = A[col][col]
        det *= pv
        A[col] = [t / pv for t in A[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [t - f * s for t, s in zip(A[r], A[col])]
    return sign * det, tuple(tuple(A[i][n:]) for i in range(n))


def mat_vec(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(4)) for i in range(4))


# ------------------------------------------------------------- whole schedule

PROGRAM = ("U", "C", "UxF", "UxF", "STOP")
_traj = {}


def trajectory(z):
    """Classical post-contact trajectory for one encoding (cached per z;
    the frozen schedule factors through z and the blank state)."""
    if z not in _traj:
        wave, led = contact((dict(), dict()), F(0), z)
        X0 = ((wave), (ZERO4, ZERO4), (ZERO4, ZERO4), 0)
        X1 = F_step(X0)
        X2 = F_step(X1)
        _traj[z] = (X0, X1, X2, led)
    return _traj[z]


class Reject(Exception):
    pass


def recognize_and_invert(n, x3, X2, led, stage, program, Minv):
    """Published prepared-image recognition and inverse (PROOF section 6).
    Returns the recovered initial native state x0 or raises Reject."""
    if n != 3 or stage != 4 or program != PROGRAM:
        raise Reject("endpoint counter/stage/program")
    b0 = X2[2][1]
    z = mat_vec(Minv, tuple(-4 * t for t in b0))
    h = next((hh for hh, (e, _w) in ENC.items() if e == z), None)
    if h is None:
        raise Reject("decoded source outside the five encodings")
    j0, j1, j2 = BRANCH[h][0]
    x0 = GENS[j0](GENS[j1](GENS[j2](x3)))
    if (x0[4], x0[5]) != (0, 1):
        raise Reject("recovered receiver is not (0,1)")
    if sum(x0[:4]) % 5 != h:
        raise Reject("recovered piston sum does not match decoded h")
    x1 = GENS[j0](x0)
    z_back = eta(x1[4], x1[5])
    Xc = F_inv(F_inv(X2))
    wave0, led0 = contact_inv(Xc[0], led, z_back)
    X_init = ((wave0), Xc[1], Xc[2], Xc[3])
    if X_init != X_BLANK or led0 != 0:
        raise Reject("inverted classical origin is not blank with w=0")
    return x0


# ---------------------------------------------------------------------- main

E_BASIS = tuple(tuple(F(1) if i == j else F(0) for i in range(4))
                for j in range(4))
SRC9 = (ZERO4,) + E_BASIS + tuple(tuple(-t for t in e) for e in E_BASIS)
TAPES4 = (
    (ZERO4, ZERO4),
    (E_BASIS[0], ZERO4),
    (ZERO4, tuple(-t for t in E_BASIS[3])),
    (tuple(E_BASIS[1][i] + E_BASIS[2][i] for i in range(4)),
     tuple(E_BASIS[0][i] - E_BASIS[3][i] for i in range(4))),
)


def check_couple(wave, a):
    (v, w), b = couple(wave, a)
    require(energy_D(v, w) + q_g(b) == energy_D(*wave) + q_g(a),
            "per-cut energy identity (8)")
    u2, a2 = couple_inv((v, w), b)
    require((u2, a2) == (wave[0], a), "couple inverse roundtrip (4)/(5)")
    return (v, w), b


def main():
    # W1: stencil and carrier basics
    mult = {}
    for d, _c in B_STENCIL:
        mult[sum(t * t for t in d)] = mult.get(sum(t * t for t in d), 0) + 1
    require(mult == {2: 12, 4: 6, 8: 12, 10: 24, 16: 6},
            "stencil shell multiplicities")
    require(C_DIAG == F(8, 9), "stencil diagonal 8/9")
    require(len(set(Y)) == 5 and set(Y) <= D_SET, "marked sites in D")
    for e in E_BASIS:
        require(apply_PT(insert_P(e)) == e, "P^T P = I")

    # N1, N2: generator identities on every checkpoint
    n_ckpt = 0
    for x in product(range(5), repeat=6):
        n_ckpt += 1
        z = sum(x) % 5
        for gi, g in enumerate(GENS):
            y = g(x)
            require(g(y) == x, "generator involution")
            require(sum(y) % 5 == SUM_MAP[gi](z), "generator sum map")
    require(n_ckpt == 15625, "checkpoint count")
    require([theta(n) for n in range(3)] == [0, 1, 1], "driver bits")

    # Derived response maps from basis runs (no inherited matrices).
    b0_cols, b1_cols = [], []
    for e in E_BASIS:
        _X0, _X1, _X2, b0, b1 = cold_run(e)
        b0_cols.append(b0)
        b1_cols.append(b1)
    M_MAT = tuple(tuple(-4 * b0_cols[j][i] for j in range(4)) for i in range(4))
    R1_MAT = tuple(tuple(b1_cols[j][i] for j in range(4)) for i in range(4))
    det_M, M_INV = mat_det_inv(M_MAT)
    require(det_M != 0, "det(M) nonzero")

    # Linearity of the cold response on sources and encodings (W4 part).
    test_sources = list(SRC9) + [ENC[h][0] for h in range(5)]
    for z in test_sources:
        _X0, _X1, _X2, b0, b1 = cold_run(z)
        require(b0 == tuple(t * F(-1, 4) for t in mat_vec(M_MAT, z)),
                "b0 = -M z/4")
        require(b1 == mat_vec(R1_MAT, z), "b1 = R1 z")
        require(mat_vec(M_INV, tuple(-4 * t for t in b0)) == z,
                "decoder z = -4 M^-1 b0")

    # Occupied family: couple identities, F roundtrips, formulas (W2, W3).
    occupied = 0
    for z in SRC9:
        Sz = source_S(z)
        wave1, b0 = check_couple((dict(), Sz), ZERO4)
        wave2, b1 = check_couple(wave1, ZERO4)
        for c0, c1 in TAPES4:
            X0, X1, X2, bb0, bb1 = cold_run(z, c0, c1)
            require((bb0, bb1) == (b0, b1), "occupied B does not alter cuts")
            require(X1[0] == wave1 and X2[0] == wave2, "occupied wave steps")
            require(X1[1:] == ((ZERO4, c1), (b0, c0), 1), "state X1 (16)")
            require(X2[1:] == ((c1, c0), (b1, b0), 0), "state X2 (13)/(16)")
            require(F_inv(X1) == X0 and F_inv(X2) == X1, "F inverse (10)")
            require(F_step(F_inv(X2)) == X2, "F roundtrip other direction")
            e0 = energy_full(X0)
            require(energy_full(X1) == e0 == energy_full(X2),
                    "E_full invariance (12)")
            occupied += 1

    # Encodings: supports, work, per-cut and tape checks on each prepared
    # trajectory, tables, balance, contact roundtrips (E1, C1, W1-W4).
    b0_seen = set()
    for h in range(5):
        z, work = ENC[h]
        require(max(abs(t) for t in z) <= 1, "encoding in Z_op")
        Sz = source_S(z)
        require(set(Sz) <= set(Y), "source support in Y")
        e_formula = (sum(t * t for t in z) - sum(z) ** 2 / 5) / 2
        require(e_formula == work, "work formula vs published value")
        require(energy_D(dict(), Sz) == work, "E_D(0,Sz) from definition")
        X0, X1, X2, led = trajectory(z)
        require(led == work, "contact ledger equals preparation work")
        require(X0[0] == (dict(), Sz), "post-contact wave (0,Sz)")
        v1, v2 = X1[0][1], X2[0][1]
        b0, b1 = X1[2][0], X2[2][0]
        require(set(v1) <= Y1_SET and set(v2) <= D_SET, "causal supports")
        # W2/W3 on this prepared encoding trajectory itself: each cut with
        # its per-cut identity, complete tape/pointer states, both F
        # inverse compositions, and every intermediate full energy.
        wave1_e, b0_e = check_couple(X0[0], ZERO4)
        wave2_e, b1_e = check_couple(wave1_e, ZERO4)
        require(wave1_e == X1[0] and wave2_e == X2[0], "encoding wave steps")
        require((b0_e, b1_e) == (b0, b1), "encoding cut outputs")
        require(X1[1:] == ((ZERO4, ZERO4), (b0, ZERO4), 1), "encoding X1 state")
        require(X2[1:] == ((ZERO4, ZERO4), (b1, b0), 0), "encoding X2 state")
        require(F_inv(X1) == X0 and F_inv(X2) == X1, "encoding F inverse (10)")
        require(F_step(F_inv(X2)) == X2, "encoding F roundtrip")
        require(energy_full(X0) == energy_full(X1) == energy_full(X2) == work,
                "encoding E_full invariance")
        require(tuple(12960 * t for t in b0) == tuple(F(t) for t in B0_NUM[h]),
                "published 12960*b0 table")
        require(tuple(1399680 * t for t in b1)
                == tuple(F(t) for t in B1_NUM[h]), "published b1 table")
        require(all((12960 * t).denominator == 1 for t in b0)
                and all((1399680 * t).denominator == 1 for t in b1),
                "table integrality")
        require(energy_D(v1, v2) + q_g(b0) + q_g(b1) == work,
                "two-cut balance (18)")
        b0_seen.add(b0)
        for wave in (X0[0], X1[0], X2[0]):
            led_t = F(3, 7)
            wv, lv = contact(wave, led_t, z)
            require(contact_inv(wv, lv, z) == (wave, led_t),
                    "contact inverse after contact")
            wv2, lv2 = contact_inv(wave, led_t, z)
            require(contact(wv2, lv2, z) == (wave, led_t),
                    "contact after contact inverse")
            occupied += 1
    require(len(b0_seen) == 5, "five distinct first outputs")
    require(occupied == 51, "frozen occupied case count")

    # All 625 preparations: native tables and whole-run inverse (N3, R1).
    fibres = {h: 0 for h in range(5)}
    endpoints = {}
    for p in product(range(5), repeat=4):
        h = sum(p) % 5
        fibres[h] += 1
        js, x1, _x2, x3 = native_run(p)
        word, C1, C2, C3 = BRANCH[h]
        require(js == word, "branch selector word")
        require((x1[4], x1[5]) == C1 and (_x2[4], _x2[5]) == C2
                and (x3[4], x3[5]) == C3, "receiver table")
        require(x3[:4] == expected_x3_pistons(h, p), "final piston formula")
        require(sum(x3) % 5 == 1, "final total sum one")
        z = eta(x1[4], x1[5])
        require(z == ENC[h][0], "induced encoding from actual receiver")
        _X0, _X1, X2, led = trajectory(z)
        x0 = (p[0], p[1], p[2], p[3], 0, 1)
        got = recognize_and_invert(3, x3, X2, led, 4, PROGRAM, M_INV)
        require(got == x0, "whole-run inverse recovers preparation")
        endpoints[p] = (x3, X2, led)
    require(all(v == 125 for v in fibres.values()), "h-fibre sizes")

    # Negative controls (R2): every one must be rejected.
    controls = []
    # X1 isolates the piston-sum guard corrected in the source review:
    # x0=(0,0,0,1,0,1) has sum 1 but is driven by the fixed h=2 word
    # (g3,g1,g3), not its selector word, then paired with the true h=2
    # classical endpoint. Readiness passes; only the sum guard rejects.
    # This fabricated endpoint is deliberately not a native trajectory.
    x_fab = GENS[3](GENS[1](GENS[3]((0, 0, 0, 1, 0, 1))))
    require(x_fab == (0, 4, 0, 0, 2, 1), "fabricated X1 endpoint value")
    _x3b, X_b, l_b = endpoints[(0, 0, 0, 2)]
    controls.append((3, x_fab, X_b, l_b, 4))                      # X1 sum guard
    x3_c, X_c, l_c = endpoints[(0, 0, 0, 3)]
    X_c2 = (X_c[0], X_c[1], (X_c[2][1], X_c[2][0]), X_c[3])
    controls.append((3, x3_c, X_c2, l_c, 4))                      # X2 tape swap
    x3_d, X_d, l_d = endpoints[(0, 0, 0, 4)]
    b0_bad = (X_d[2][1][0] + F(1, 12960),) + X_d[2][1][1:]
    X_d2 = (X_d[0], X_d[1], (X_d[2][0], b0_bad), X_d[3])
    controls.append((3, x3_d, X_d2, l_d, 4))                      # X3 b0 shifted
    controls.append((2,) + endpoints[(0, 0, 0, 2)][0:1]
                    + endpoints[(0, 0, 0, 2)][1:] + (4,))         # X4 counter
    x3_e, X_e, _l_e = endpoints[(0, 0, 0, 1)]
    controls.append((3, x3_e, X_e, F(0), 4))                      # X5 ledger
    rejected = 0
    for n_c, x3_c, X_c, l_c, st_c in controls:
        try:
            recognize_and_invert(n_c, x3_c, X_c, l_c, st_c, PROGRAM, M_INV)
        except Reject:
            rejected += 1
    require(rejected == 5, "all negative controls rejected")

    print("NATIVE_CLASSICAL_CONTACT_CENSUS_PASS preparations=625 "
          "checkpoints=15625 encodings=5 occupied=51 rejected=5")


if __name__ == "__main__":
    main()
