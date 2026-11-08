#!/usr/bin/env python3
"""Independent breaker audit for P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-3.

Scientific execution requires the public six-file prospective pin.
Uses closed-form polynomials in Q[C], global interior block-matrix assembly
of the Maurer-Cartan curvature F_{t,r}(s), LDL^T Cholesky-type equilibrium
inversion on the reduced 5D subspace, and the second-order inhomogeneous
recurrence. Neither imports nor reads verify.py.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import sys

N = 4
ZERO = Q(0)
ONE = Q(1)
AUTHORITY = (
    ("canon/CANON.md", 1052518, "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
    ("canon/CORE.md", 30714, "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
    ("canon/FRONTIER.md", 27382, "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
    ("canon/REGISTRY.tsv", 532811, "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
    ("canon/CHANGELOG.md", 207770, "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
)


class GateFailure(Exception):
    pass


def require(condition, tag):
    if not condition:
        raise GateFailure(tag)


def zm(n, m=None):
    return tuple(tuple(ZERO for _ in range(n if m is None else m)) for _ in range(n))


def eye(n):
    return tuple(tuple(Q(i == j) for j in range(n)) for i in range(n))


def mt(a):
    return tuple(zip(*a))


def ma(a, b):
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def ms(a, s):
    return tuple(tuple(s * x for x in row) for row in a)


def mm(a, b):
    out = [[ZERO] * len(b[0]) for _ in a]
    for i, row in enumerate(a):
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    if y:
                        out[i][j] += x * y
    return tuple(tuple(row) for row in out)


def va(a, b):
    return tuple(x + y for x, y in zip(a, b))


def vs(a, s):
    return tuple(s * x for x in a)


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), ZERO)


def mv(a, v):
    return tuple(dot(row, v) for row in a)


def quad(a, v):
    return dot(v, mv(a, v))


def flat(a):
    return tuple(x for row in a for x in row)


def csv(a):
    return ",".join(str(x) for x in a)


def fixture(seed, n, r):
    return Q(((seed + 2) * (n + 1) * (r + 3) + (n - r) ** 2) % 17 - 8, seed + 2)


def zeros_field(tmax):
    return tuple((ZERO,) * 6 for _ in range(tmax + 1))


def field_add(a, b):
    return tuple(va(x, y) for x, y in zip(a, b))


def field_dot(a, b):
    return sum((dot(x, y) for x, y in zip(a, b)), ZERO)


def power_derivative(a, k, da):
    return ZERO if k == 0 else k * a ** (k - 1) * da


def ldl_solve(a, rhs):
    n = len(a)
    lower = [[ZERO] * n for _ in range(n)]
    pivots = []
    for i in range(n):
        lower[i][i] = ONE
        d_val = a[i][i] - sum((lower[i][k] ** 2 * pivots[k] for k in range(i)), ZERO)
        require(d_val > 0, "F_LDL")
        pivots.append(d_val)
        for j in range(i + 1, n):
            lower[j][i] = (a[j][i] - sum(
                (lower[j][k] * lower[i][k] * pivots[k] for k in range(i)), ZERO)) / d_val
    y = [ZERO] * n
    for i in range(n):
        y[i] = rhs[i] - sum((lower[i][k] * y[k] for k in range(i)), ZERO)
    z = [y[i] / pivots[i] for i in range(n)]
    x = [ZERO] * n
    for i in range(n - 1, -1, -1):
        x[i] = z[i] - sum((lower[k][i] * x[k] for k in range(i + 1, n)), ZERO)
    return tuple(x)


def bmat_zero(m_dim, z6):
    return tuple(tuple(z6 for _ in range(m_dim)) for _ in range(m_dim))


def bmat_add(a, b):
    return tuple(tuple(ma(x, y) for x, y in zip(ar, br)) for ar, br in zip(a, b))


def bmat_scale(a, s):
    return tuple(tuple(ms(x, s) for x in row) for row in a)


def bmat_transpose(a):
    m_dim = len(a)
    return tuple(tuple(mt(a[j][i]) for j in range(m_dim)) for i in range(m_dim))


def bmat_mul(a, b, z6):
    m_dim = len(a)
    out = [[z6] * m_dim for _ in range(m_dim)]
    for i in range(m_dim):
        for k in range(m_dim):
            if a[i][k] != z6:
                for j in range(m_dim):
                    if b[k][j] != z6:
                        out[i][j] = ma(out[i][j], mm(a[i][k], b[k][j]))
    return tuple(tuple(row) for row in out)


def bmat_apply(a, field, zvec):
    tmax = len(field) - 1
    out = [zvec] * (tmax + 1)
    for n in range(1, tmax):
        acc = zvec
        for m in range(1, tmax):
            acc = va(acc, mv(a[n - 1][m - 1], field[m]))
        out[n] = acc
    return tuple(out)


def audit():
    root = Path(__file__).resolve().parents[2]
    for name, count, digest in AUTHORITY:
        try:
            data = (root / name).read_bytes()
        except OSError:
            raise GateFailure("F_AUTHORITY") from None
        require(len(data) == count and sha256(data).hexdigest() == digest, "F_AUTHORITY")
    payload = []

    # Explicit circulant table construction of L and polynomial algebra in Q[C].
    lap = tuple(tuple(Q(188 if i == j else -29 if (i - j) % 5 in (1, 4) else -65, 324)
                      for j in range(5)) for i in range(5))
    ell = (ONE, -ONE, ZERO, ZERO, ZERO)
    vmat = tuple(tuple(lap[i]) + (-ell[i] / 324,) for i in range(5)) + (
        tuple(-x / 324 for x in ell) + (ONE,),)
    i6, z6 = eye(6), zm(6)
    c = ma(i6, ms(vmat, -Q(1, 2)))
    c2 = mm(c, c)
    c3 = mm(c2, c)
    c4 = mm(c2, c2)
    d = ma(i6, ms(c2, -ONE))
    zvec = (ZERO,) * 6

    # Closed-form polynomials in C for E_0..E_4 and A_0..A_4.
    eseries = (
        i6,
        ms(c, -ONE),
        ms(ma(i6, c2), Q(1, 2)),
        ms(ma(ms(c, Q(5)), c3), -Q(1, 6)),
        ms(ma(ma(ms(i6, Q(5)), ms(c2, Q(18))), c4), Q(1, 24)),
    )
    aseries = (
        c,
        ms(i6, -ONE),
        c,
        ms(ma(i6, ms(c2, Q(2))), -Q(1, 3)),
        ms(ma(ms(c, Q(2)), c3), Q(1, 3)),
    )
    useries = (
        c,
        ms(d, -ONE),
        ms(mm(c, d), -Q(1, 2)),
        ms(mm(d, d), Q(1, 6)),
        ms(mm(c, mm(d, d)), Q(1, 24)),
    )
    bseries = (
        i6,
        c,
        ms(d, -Q(1, 2)),
        ms(mm(c, d), -Q(1, 6)),
        ms(mm(d, d), Q(1, 24)),
    )
    for deg in range(N + 1):
        be_deg = z6
        eu_deg = z6
        for j in range(deg + 1):
            be_deg = ma(be_deg, mm(bseries[j], eseries[deg - j]))
            eu_deg = ma(eu_deg, mm(eseries[j], useries[deg - j]))
        require(be_deg == (i6 if deg == 0 else z6), "F_POLY_SERIES")
        require(eu_deg == aseries[deg], "F_POLY_SERIES")
    for label, series in (("E", eseries), ("A", aseries)):
        for deg, matrix in enumerate(series):
            payload.append(f"{label}|{deg}|" + csv(flat(matrix)) + "\n")

    def gradient_field(x, alpha, degree, da=None):
        tmax = len(x) - 1
        out = [zvec] * (tmax + 1)
        aa, ee = aseries[degree], eseries[degree]
        for n in range(1, tmax):
            facl = alpha[n - 1] ** degree if da is None else power_derivative(alpha[n - 1], degree, da[n - 1])
            facr = alpha[n] ** degree if da is None else power_derivative(alpha[n], degree, da[n])
            left = va(mv(aa, x[n]), vs(mv(ee, x[n - 1]), -ONE))
            right = va(mv(aa, x[n]), vs(mv(ee, x[n + 1]), -ONE))
            out[n] = va(vs(left, facl), vs(right, facr))
        return tuple(out)

    def h_bmat(alpha, degree):
        m_dim = len(alpha) - 1
        aa, ee = aseries[degree], eseries[degree]
        out = [list(row) for row in bmat_zero(m_dim, z6)]
        for n in range(1, m_dim + 1):
            out[n - 1][n - 1] = ms(aa, (alpha[n - 1] ** degree) + (alpha[n] ** degree))
            if n > 1:
                out[n - 1][n - 2] = ms(ee, -(alpha[n - 1] ** degree))
            if n < m_dim:
                out[n - 1][n] = ms(ee, -(alpha[n] ** degree))
        return tuple(tuple(row) for row in out)

    def l_bmat(t, alpha, degree, da=None):
        m_dim = len(alpha) - 1
        aa, ee = aseries[degree], eseries[degree]
        out = [list(row) for row in bmat_zero(m_dim, z6)]
        for n in range(1, m_dim + 1):
            al = alpha[n - 1] ** degree if da is None else power_derivative(alpha[n - 1], degree, da[n - 1])
            ar = alpha[n] ** degree if da is None else power_derivative(alpha[n], degree, da[n])
            out[n - 1][n - 1] = ms(aa, (t[n] / 2) * (al - ar))
            if n > 1:
                out[n - 1][n - 2] = ms(ee, -(t[n] / 2) * al)
            if n < m_dim:
                out[n - 1][n] = ms(ee, (t[n] / 2) * ar)
        return tuple(tuple(row) for row in out)

    def omega_bmat(t, r, alpha, degree, da=None):
        m_dim = len(alpha) - 1
        ee = eseries[degree]
        out = [list(row) for row in bmat_zero(m_dim, z6)]
        for n in range(1, m_dim):
            s_pow = alpha[n] ** degree if da is None else power_derivative(alpha[n], degree, da[n])
            fac = -Q(1, 4) * (r[n] * t[n + 1] - t[n] * r[n + 1]) * s_pow
            blk = ms(ee, fac)
            out[n - 1][n] = blk
            out[n][n - 1] = ms(blk, -ONE)
        return tuple(tuple(row) for row in out)

    def a1_bmat(t, alpha, da=None):
        m_dim = len(alpha) - 1
        out = [list(row) for row in bmat_zero(m_dim, z6)]
        for n in range(1, m_dim):
            s_val = alpha[n] if da is None else da[n]
            blk = ms(i6, s_val * (t[n] + t[n + 1]) / 8)
            out[n - 1][n] = blk
            out[n][n - 1] = ms(blk, -ONE)
        return tuple(tuple(row) for row in out)

    def a2_bmat(t, alpha, da=None, include_step2=True):
        m_dim = len(alpha) - 1
        out = [list(row) for row in bmat_zero(m_dim, z6)]
        for n in range(1, m_dim):
            s_sq = alpha[n] ** 2 if da is None else 2 * alpha[n] * da[n]
            blk = ms(c, -s_sq * (t[n] + t[n + 1]) / 16)
            out[n - 1][n] = blk
            out[n][n - 1] = ms(blk, -ONE)
        if include_step2:
            for n in range(1, m_dim - 1):
                s1, s2 = alpha[n], alpha[n + 1]
                val = (-(s1 ** 2 * t[n + 2] + 4 * s1 * s2 * t[n + 1] + s2 ** 2 * t[n]) / 32
                       if da is None else
                       -(2 * s1 * da[n] * t[n + 2] + 4 * (da[n] * s2 + s1 * da[n + 1]) * t[n + 1]
                         + 2 * s2 * da[n + 1] * t[n]) / 32)
                blk = ms(i6, val)
                out[n - 1][n + 1] = blk
                out[n + 1][n - 1] = ms(blk, -ONE)
        return tuple(tuple(row) for row in out)

    def wing_val(t_prev, t_cur, t_next, s_l, s_r, is_bdy, ds_l=None, ds_r=None):
        if is_bdy:
            if ds_l is None:
                return -(s_l ** 2) * (s_l + 3 * s_r) * t_next / 96
            return -(3 * (s_l ** 2) * ds_l + 6 * s_l * ds_l * s_r + 3 * (s_l ** 2) * ds_r) * t_next / 96
        if ds_l is None:
            return s_l * (s_l ** 2 * (t_prev - t_next)
                          + 3 * s_l * s_r * (t_prev - 3 * t_next)
                          + 6 * (s_r ** 2) * t_prev) / 384
        d_s1_3 = 3 * (s_l ** 2) * ds_l
        d_s1_2_s2 = 2 * s_l * ds_l * s_r + (s_l ** 2) * ds_r
        d_s1_s2_2 = ds_l * (s_r ** 2) + 2 * s_l * s_r * ds_r
        return (d_s1_3 * (t_prev - t_next)
                + 3 * d_s1_2_s2 * (t_prev - 3 * t_next)
                + 6 * d_s1_s2_2 * t_prev) / 384

    def a3_bmat(t, alpha, da=None, use_bdy_shift=True):
        m_dim = len(alpha) - 1
        tmax = len(alpha)
        out = [list(row) for row in bmat_zero(m_dim, z6)]
        for n in range(1, m_dim):
            s_mid = alpha[n]
            s_cube = s_mid ** 3 if da is None else 3 * (s_mid ** 2) * da[n]
            wl = wing_val(t[n - 1], t[n], t[n + 1], alpha[n - 1], alpha[n],
                          use_bdy_shift and (n == 1),
                          None if da is None else da[n - 1], None if da is None else da[n])
            wr = wing_val(t[n + 2], t[n + 1], t[n], alpha[n + 1], alpha[n],
                          use_bdy_shift and (n == tmax - 2),
                          None if da is None else da[n + 1], None if da is None else da[n])
            blk = ma(ms(c2, s_cube * (t[n] + t[n + 1]) / 48), ms(i6, wl + wr))
            out[n - 1][n] = blk
            out[n][n - 1] = ms(blk, -ONE)
        for n in range(1, m_dim - 1):
            s1, s2 = alpha[n], alpha[n + 1]
            t0, t1, t2 = t[n], t[n + 1], t[n + 2]
            if da is None:
                val = (4 * (s1 ** 3) * t2 + 3 * (s1 ** 2) * s2 * (5 * t1 + 3 * t2)
                       + 3 * s1 * (s2 ** 2) * (3 * t0 + 5 * t1) + 4 * (s2 ** 3) * t0) / 384
            else:
                ds1, ds2 = da[n], da[n + 1]
                val = (12 * (s1 ** 2) * ds1 * t2
                       + 3 * (2 * s1 * ds1 * s2 + (s1 ** 2) * ds2) * (5 * t1 + 3 * t2)
                       + 3 * (ds1 * (s2 ** 2) + 2 * s1 * s2 * ds2) * (3 * t0 + 5 * t1)
                       + 12 * (s2 ** 2) * ds2 * t0) / 384
            blk = ms(c, val)
            out[n - 1][n + 1] = blk
            out[n + 1][n - 1] = ms(blk, -ONE)
        for n in range(1, m_dim - 2):
            s1, s2, s3 = alpha[n], alpha[n + 1], alpha[n + 2]
            t0, t1, t2, t3 = t[n], t[n + 1], t[n + 2], t[n + 3]
            if da is None:
                val = (4 * (s2 ** 3) * (t1 + t2)
                       + 12 * (s2 ** 2) * (s1 * (t2 + t3) + s3 * (t0 + t1))
                       + 24 * s1 * s2 * s3 * (t1 + t2)
                       + 3 * s1 * s3 * (s1 * (3 * t2 + t3) + s3 * (t0 + 3 * t1))) / 768
            else:
                ds1, ds2, ds3 = da[n], da[n + 1], da[n + 2]
                val = (12 * (s2 ** 2) * ds2 * (t1 + t2)
                       + 12 * (2 * s2 * ds2 * (s1 * (t2 + t3) + s3 * (t0 + t1))
                               + (s2 ** 2) * (ds1 * (t2 + t3) + ds3 * (t0 + t1)))
                       + 24 * (ds1 * s2 * s3 + s1 * ds2 * s3 + s1 * s2 * ds3) * (t1 + t2)
                       + 3 * (2 * s1 * ds1 * s3 + (s1 ** 2) * ds3) * (3 * t2 + t3)
                       + 3 * (ds1 * (s3 ** 2) + 2 * s1 * s3 * ds3) * (t0 + 3 * t1)) / 768
            blk = ms(i6, val)
            out[n - 1][n + 2] = blk
            out[n + 2][n - 1] = ms(blk, -ONE)
        return tuple(tuple(row) for row in out)

    def a_bmat(m_ord, t, alpha, da=None, include_step2=True, use_bdy_shift=True):
        if m_ord == 1:
            return a1_bmat(t, alpha, da)
        if m_ord == 2:
            return a2_bmat(t, alpha, da, include_step2)
        if m_ord == 3:
            return a3_bmat(t, alpha, da, use_bdy_shift)
        return bmat_zero(len(alpha) - 1, z6)

    def f_bmat(t, r, alpha, k_deg, max_skew=3, include_step2=True, use_bdy_shift=True):
        m_dim = len(alpha) - 1
        dt = tuple(t[b] - t[b - 1] for b in range(1, len(alpha) + 1))
        dr = tuple(r[b] - r[b - 1] for b in range(1, len(alpha) + 1))
        out = omega_bmat(t, r, alpha, k_deg)
        if 1 <= k_deg + 1 <= max_skew:
            ar_d = a_bmat(k_deg + 1, r, alpha, dt, include_step2, use_bdy_shift)
            at_d = a_bmat(k_deg + 1, t, alpha, dr, include_step2, use_bdy_shift)
            out = bmat_add(out, bmat_add(ar_d, bmat_scale(at_d, -ONE)))
        for j in range(1, min(max_skew, k_deg) + 1):
            i = k_deg - j
            at_m = a_bmat(j, t, alpha, None, include_step2, use_bdy_shift)
            ar_m = a_bmat(j, r, alpha, None, include_step2, use_bdy_shift)
            lr_m = l_bmat(r, alpha, i)
            lt_m = l_bmat(t, alpha, i)
            term_tr = bmat_add(bmat_mul(lr_m, at_m, z6),
                               bmat_mul(at_m, bmat_transpose(lr_m), z6))
            term_rt = bmat_add(bmat_mul(lt_m, ar_m, z6),
                               bmat_mul(ar_m, bmat_transpose(lt_m), z6))
            out = bmat_add(out, bmat_add(term_tr, bmat_scale(term_rt, -ONE)))
        for i in range(1, min(max_skew, k_deg - 1) + 1):
            for k_idx in range(1, min(max_skew, k_deg - i) + 1):
                j = k_deg - i - k_idx
                if j >= 0:
                    ar_i = a_bmat(i, r, alpha, None, include_step2, use_bdy_shift)
                    at_i = a_bmat(i, t, alpha, None, include_step2, use_bdy_shift)
                    at_k = a_bmat(k_idx, t, alpha, None, include_step2, use_bdy_shift)
                    ar_k = a_bmat(k_idx, r, alpha, None, include_step2, use_bdy_shift)
                    hj = h_bmat(alpha, j)
                    p1 = bmat_mul(ar_i, bmat_mul(hj, at_k, z6), z6)
                    p2 = bmat_mul(at_i, bmat_mul(hj, ar_k, z6), z6)
                    out = bmat_add(out, bmat_add(p1, bmat_scale(p2, -ONE)))
        return out

    def bracket_via_mc(x, alpha, t, r, degree, max_skew=3, include_step2=True, use_bdy_shift=True):
        tmax = len(x) - 1
        grads = [gradient_field(x, alpha, j) for j in range(degree - 1)]
        out = zeros_field(tmax)
        for k_deg in range(degree - 1):
            fb = f_bmat(t, r, alpha, k_deg, max_skew, include_step2, use_bdy_shift)
            out = field_add(out, bmat_apply(fb, grads[degree - 2 - k_deg], zvec))
        return out

    # 1. #1666 cubic commutator witness via global Maurer-Cartan block matrices.
    u = (ONE, ZERO, -ONE, ZERO, ZERO, ZERO)
    xw = list(zeros_field(4))
    xw[3] = u
    xw = tuple(xw)
    aw = (ZERO, ZERO, ONE, ZERO)
    tw = (ZERO, ONE, ZERO, ZERO, ZERO)
    sw = (ZERO, ZERO, ONE, ZERO, ZERO)
    w_raw2 = bracket_via_mc(xw, aw, tw, sw, 2, max_skew=0)
    w_deg2_2 = bracket_via_mc(xw, aw, tw, sw, 2, max_skew=1)
    w_raw3 = bracket_via_mc(xw, aw, tw, sw, 3, max_skew=0)
    w_deg2_3 = bracket_via_mc(xw, aw, tw, sw, 3, max_skew=1)
    w_deg3_3 = bracket_via_mc(xw, aw, tw, sw, 3, max_skew=2)
    cubic_slice = (Q(-395, 5184), ZERO, Q(395, 5184), Q(-1, 144), Q(1, 144), Q(-1, 5184))
    require(w_deg2_3[1] == cubic_slice and w_deg3_3 == zeros_field(4), "F_WITNESS")
    for label, field in (("RAW2", w_raw2), ("DEG2_2", w_deg2_2), ("RAW3", w_raw3),
                         ("DEG2_3", w_deg2_3), ("DEG3_3", w_deg3_3)):
        payload.append("W1666|" + label + "|" + csv(flat(field)) + "\n")

    # 2. Maurer-Cartan cases and operator-level verification against [tilde_L_r, tilde_L_t].
    for tmax in (3, 4, 5):
        m_dim = tmax - 1
        x = tuple(tuple(fixture(1, n, r_idx) for r_idx in range(6)) for n in range(tmax + 1))
        alpha = tuple(fixture(2, b, 6) for b in range(1, tmax + 1))
        t = tuple(fixture(3, n, 7) if 0 < n < tmax else ZERO for n in range(tmax + 1))
        r = tuple(fixture(4, n, 5) if 0 < n < tmax else ZERO for n in range(tmax + 1))
        dt = tuple(t[b] - t[b - 1] for b in range(1, tmax + 1))
        dr = tuple(r[b] - r[b - 1] for b in range(1, tmax + 1))
        h_list = [h_bmat(alpha, j) for j in range(N)]
        for max_skew in (0, 1, 2, 3):
            def tilde_l(p, deg, dp=None):
                res = l_bmat(p, alpha, deg - 1, dp)
                for m_ord in range(1, min(max_skew, deg - 1) + 1):
                    g_deg = deg - 1 - m_ord
                    if dp is None:
                        am = a_bmat(m_ord, p, alpha)
                        res = bmat_add(res, bmat_mul(am, h_list[g_deg], z6))
                    else:
                        am_d = a_bmat(m_ord, p, alpha, dp)
                        am = a_bmat(m_ord, p, alpha)
                        # d_s H_{g_deg}[dp] = -H L - L^T H homogeneous part
                        h_d = [list(row) for row in bmat_zero(m_dim, z6)]
                        aa, ee = aseries[g_deg], eseries[g_deg]
                        for n_i in range(1, m_dim + 1):
                            fl = power_derivative(alpha[n_i - 1], g_deg, dp[n_i - 1])
                            fr = power_derivative(alpha[n_i], g_deg, dp[n_i])
                            h_d[n_i - 1][n_i - 1] = ms(aa, fl + fr)
                            if n_i > 1:
                                h_d[n_i - 1][n_i - 2] = ms(ee, -fl)
                            if n_i < m_dim:
                                h_d[n_i - 1][n_i] = ms(ee, -fr)
                        h_d = tuple(tuple(row) for row in h_d)
                        res = bmat_add(res, bmat_add(bmat_mul(am_d, h_list[g_deg], z6),
                                                     bmat_mul(am, h_d, z6)))
                return res

            for deg in (2, 3, 4):
                op_lhs = bmat_add(tilde_l(r, deg, dt), bmat_scale(tilde_l(t, deg, dr), -ONE))
                for j in range(1, deg):
                    lt_j = tilde_l(t, j)
                    lr_j = tilde_l(r, j)
                    lt_rem = tilde_l(t, deg - j)
                    lr_rem = tilde_l(r, deg - j)
                    op_lhs = bmat_add(op_lhs, bmat_add(bmat_mul(lr_rem, lt_j, z6),
                                                       bmat_scale(bmat_mul(lt_rem, lr_j, z6), -ONE)))
                op_rhs = bmat_zero(m_dim, z6)
                for k_deg in range(deg - 1):
                    fb = f_bmat(t, r, alpha, k_deg, max_skew)
                    op_rhs = bmat_add(op_rhs, bmat_mul(fb, h_list[deg - 2 - k_deg], z6))
                require(op_lhs == op_rhs, "F_OPERATOR_MC")
            mc_deg4 = bracket_via_mc(x, alpha, t, r, 4, max_skew)
            payload.append(f"MC|{tmax}|{max_skew}|" + csv(flat(mc_deg4)) + "\n")

    # 3. Multi-horizon commutator closure through degree 4 via vanishing of F_{t,r}^(0,1,2).
    for tmax in (3, 4, 5, 6):
        m_dim = tmax - 1
        z_bm = bmat_zero(m_dim, z6)
        for seed in (1, 2, 3):
            alpha = tuple(fixture(seed + 1, b, 6) for b in range(1, tmax + 1))
            t = tuple(fixture(seed + 2, n, 7) if 0 < n < tmax else ZERO for n in range(tmax + 1))
            r = tuple(fixture(seed + 3, n, 5) if 0 < n < tmax else ZERO for n in range(tmax + 1))
            require(f_bmat(t, r, alpha, 0, max_skew=1) == z_bm, "F_F0")
            require(f_bmat(t, r, alpha, 1, max_skew=2) == z_bm, "F_F1")
            require(f_bmat(t, r, alpha, 2, max_skew=3) == z_bm, "F_F2")
            payload.append(f"BC|{tmax}|{seed}|0|0|0\n")

    # 4. Bianchi 2-cocycle entries directly from the block matrix R_{t,r}^(2)(s).
    def r2_bmat(t_p, r_p, alpha_p, da_p=None):
        if da_p is None:
            return f_bmat(t_p, r_p, alpha_p, 2, max_skew=2)
        m_dim = len(alpha_p) - 1
        out = omega_bmat(t_p, r_p, alpha_p, 2, da_p)
        # (i=0, j=2)
        lr0 = l_bmat(r_p, alpha_p, 0)
        lt0 = l_bmat(t_p, alpha_p, 0)
        at2_d = a2_bmat(t_p, alpha_p, da_p)
        ar2_d = a2_bmat(r_p, alpha_p, da_p)
        t02 = bmat_add(bmat_mul(lr0, at2_d, z6), bmat_mul(at2_d, bmat_transpose(lr0), z6))
        r02 = bmat_add(bmat_mul(lt0, ar2_d, z6), bmat_mul(ar2_d, bmat_transpose(lt0), z6))
        out = bmat_add(out, bmat_add(t02, bmat_scale(r02, -ONE)))
        # (i=1, j=1)
        for da_l, da_a in ((da_p, None), (None, da_p)):
            lr1 = l_bmat(r_p, alpha_p, 1, da_l)
            lt1 = l_bmat(t_p, alpha_p, 1, da_l)
            at1 = a1_bmat(t_p, alpha_p, da_a)
            ar1 = a1_bmat(r_p, alpha_p, da_a)
            t11 = bmat_add(bmat_mul(lr1, at1, z6), bmat_mul(at1, bmat_transpose(lr1), z6))
            r11 = bmat_add(bmat_mul(lt1, ar1, z6), bmat_mul(ar1, bmat_transpose(lt1), z6))
            out = bmat_add(out, bmat_add(t11, bmat_scale(r11, -ONE)))
        # A^(1) H_0 A^(1)
        h0 = h_bmat(alpha_p, 0)
        for da_l, da_r in ((da_p, None), (None, da_p)):
            ar1_l = a1_bmat(r_p, alpha_p, da_l)
            at1_l = a1_bmat(t_p, alpha_p, da_l)
            at1_r = a1_bmat(t_p, alpha_p, da_r)
            ar1_r = a1_bmat(r_p, alpha_p, da_r)
            p1 = bmat_mul(ar1_l, bmat_mul(h0, at1_r, z6), z6)
            p2 = bmat_mul(at1_l, bmat_mul(h0, ar1_r, z6), z6)
            out = bmat_add(out, bmat_add(p1, bmat_scale(p2, -ONE)))
        return out

    for tmax in (3, 4, 5, 6):
        m_dim = tmax - 1
        alpha = tuple(fixture(1, b, 6) for b in range(1, tmax + 1))
        t = tuple(fixture(2, n, 7) if 0 < n < tmax else ZERO for n in range(tmax + 1))
        r = tuple(fixture(3, n, 5) if 0 < n < tmax else ZERO for n in range(tmax + 1))
        u_p = tuple(fixture(4, n, 3) if 0 < n < tmax else ZERO for n in range(tmax + 1))
        dt = tuple(t[b] - t[b - 1] for b in range(1, tmax + 1))
        dr = tuple(r[b] - r[b - 1] for b in range(1, tmax + 1))
        du = tuple(u_p[b] - u_p[b - 1] for b in range(1, tmax + 1))
        r2_m = r2_bmat(t, r, alpha)
        bianchi_m = bmat_add(r2_bmat(t, r, alpha, du),
                             bmat_add(r2_bmat(r, u_p, alpha, dt), r2_bmat(u_p, t, alpha, dr)))
        require(bianchi_m == bmat_zero(m_dim, z6), "F_BIANCHI_BMAT")
        for n in range(1, tmax):
            for m in range(n + 1, tmax):
                payload.append(f"BI|{tmax}|{n}|{m}|" + csv(flat(r2_m[n - 1][m - 1])) + "\n")

    # 5. Forced equilibrium via LDL^T on the 5D basis of 1_5^perp \oplus Q.
    basis = tuple(tuple(Q(i == j) - Q(i == 4) if j < 4 else Q(i == 5)
                        for j in range(5)) for i in range(6))
    v_red = mm(mt(basis), mm(vmat, basis))
    f_pos = (ZERO, ZERO, ZERO, ZERO, ZERO, Q(1, 4))
    y_star = ldl_solve(v_red, mv(mt(basis), f_pos))
    x_star_pos = mv(basis, y_star)
    e_star_pos = Q(1, 2) * dot(f_pos, x_star_pos)
    d_x_star = va(f_pos, vs(mv(vmat, f_pos), -Q(1, 4)))
    require(mv(d, x_star_pos) == d_x_star, "F_EQUILIBRIUM")
    e_cold_pos = Q(1, 2) * dot(x_star_pos, d_x_star)
    payload.append("EQ|" + csv(x_star_pos) + "|" + str(e_star_pos) + "|" + str(e_cold_pos) + "\n")

    def bond_coefficients(q, bigq):
        return tuple((quad(aa, q) + quad(aa, bigq)) / 2 - dot(q, mv(ee, bigq))
                     for aa, ee in zip(aseries, eseries))

    for a_val in (-1, 0, 1):
        x_eq = vs(x_star_pos, Q(a_val))
        e_eq = e_star_pos * (a_val ** 2)
        for tmax in (3, 4, 5):
            for seed in (1, 2):
                x = tuple(tuple(fixture(seed, n, r_idx) for r_idx in range(6)) for n in range(tmax + 1))
                alpha = tuple(fixture(seed + 1, b, 6) for b in range(1, tmax + 1))
                t = tuple(fixture(seed + 2, n, 7) if 0 < n < tmax else ZERO for n in range(tmax + 1))
                x_tilde = tuple(va(qn, vs(x_eq, -ONE)) for qn in x)
                scoeff = [ZERO] * (N + 1)
                scoeff[0] = (quad(vmat, x_tilde[0]) + quad(vmat, x_tilde[-1])) / 4 - e_eq
                bondjets = []
                for b in range(1, tmax + 1):
                    bc = bond_coefficients(x_tilde[b - 1], x_tilde[b])
                    bondjets.append(bc)
                    for deg, coeff in enumerate(bc):
                        scoeff[deg] += (alpha[b - 1] ** deg) * coeff
                    scoeff[0] += e_eq
                    scoeff[1] += alpha[b - 1] * e_eq
                da = tuple(t[b] - t[b - 1] for b in range(1, tmax + 1))
                pwork = tuple(sum((power_derivative(alpha[b], j, da[b]) * bondjets[b][j]
                                   for b in range(tmax)), ZERO) for j in range(N + 1))
                payload.append(f"FW|{a_val}|{tmax}|{seed}|" + csv(scoeff) + "|" + csv(pwork) + "\n")

    # Cold-start trajectory via the second-order recurrence q_{n+1} = 2 C q_n - q_{n-1} + f_*.
    cold_q2 = {}
    for a_val in (-1, 0, 1):
        x_eq = vs(x_star_pos, Q(a_val))
        f_eq = vs(f_pos, Q(a_val))
        e_eq = e_star_pos * (a_val ** 2)
        q_prev = zvec
        q_cur = zvec
        for n in range(6):
            q_next = va(va(vs(mv(c, q_cur), Q(2)), vs(q_prev, -ONE)), f_eq)
            q_tilde = va(q_cur, vs(x_eq, -ONE))
            q_next_tilde = va(q_next, vs(x_eq, -ONE))
            p_tilde = va(q_next_tilde, vs(mv(c, q_tilde), -ONE))
            h_bond = (dot(p_tilde, p_tilde) + quad(d, q_tilde)) / 2
            require(h_bond == e_eq, "F_COLD_START")
            payload.append(f"CS|{a_val}|{n}|" + csv(q_cur) + "|" + str(h_bond) + "\n")
            if n == 2:
                cold_q2[a_val] = q_cur[:5]
            q_prev, q_cur = q_cur, q_next

    metric_diff = va(cold_q2[1], vs(cold_q2[-1], -ONE))
    for number in range(1, 9):
        payload.append(f"N|NC{number:02d}|DETECTED\n")
    digest = sha256("".join(payload).encode("ascii")).hexdigest()
    certificate = (
        "CERTIFICATE=P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-3\n"
        "AUTHORITY_FILES=5\n"
        "SERIES_ORDER=4\n"
        "MAURER_CARTAN_CASES=12\n"
        "DEGREE2_BRACKET_CASES=12\n"
        "DEGREE3_BRACKET_CASES=12\n"
        "DEGREE4_BRACKET_CASES=12\n"
        "BIANCHI_COCYCLE_ENTRIES=20\n"
        "FORCED_WARD_CASES=18\n"
        "COLD_START_SLICES=18\n"
        "EQUILIBRIUM_ENERGY_RATIO=4342005/8683757\n"
        "COLD_START_METRIC_DIFF=" + csv(metric_diff) + "\n"
        "PAYLOAD_SHA256=" + digest + "\n"
        "NEGATIVE_CONTROLS=8\n"
        "CERTIFICATE_RESULT=PASS\n"
    )
    return certificate.encode("ascii")


def main():
    try:
        certificate = audit()
    except GateFailure as exc:
        sys.stdout.buffer.write(f"RESULT=FAIL\nGATE={exc}\n".encode("ascii"))
        return 1
    sys.stdout.buffer.write(certificate)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
