#!/usr/bin/env python3
"""Exact primary verifier for P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-1.

Scientific execution requires the public six-file prospective pin.
Uses Fraction matrix series, field-space directional derivatives, and
Gauss-Jordan equilibrium elimination. Neither imports nor reads breaker.py.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
from pathlib import Path
import subprocess
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


def inv(a):
    n = len(a)
    rows = [list(a[i]) + list(eye(n)[i]) for i in range(n)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if rows[i][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        scale = rows[col][col]
        rows[col] = [x / scale for x in rows[col]]
        for i in range(n):
            if i != col and rows[i][col]:
                scale = rows[i][col]
                rows[i] = [x - scale * y for x, y in zip(rows[i], rows[col])]
    return tuple(tuple(row[n:]) for row in rows)


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


def block(a, b, c, d):
    return tuple(tuple(ar) + tuple(br) for ar, br in zip(a, b)) + tuple(
        tuple(cr) + tuple(dr) for cr, dr in zip(c, d))


def upper_blocks(m):
    return tuple(row[:6] for row in m[:6]), tuple(row[6:] for row in m[:6])


def flat(a):
    return tuple(x for row in a for x in row)


def csv(a):
    return ",".join(str(x) for x in a)


def series_mul(a, b, order=N):
    out = []
    for k in range(order + 1):
        acc = zm(len(a[0]), len(b[0][0]))
        for j in range(k + 1):
            acc = ma(acc, mm(a[j], b[k - j]))
        out.append(acc)
    return out


def series_inverse(a, order=N):
    out = [inv(a[0])]
    for k in range(1, order + 1):
        acc = zm(len(a[0]))
        for j in range(1, k + 1):
            acc = ma(acc, mm(a[j], out[k - j]))
        out.append(ms(mm(out[0], acc), -ONE))
    return out


def generating_series(mseries):
    ub = [upper_blocks(m) for m in mseries]
    u = [pair[0] for pair in ub]
    b = [pair[1] for pair in ub]
    e = series_inverse(b)
    a = series_mul(e, u)
    return u, b, e, a


def fixture(seed, n, r):
    return Q(((seed + 2) * (n + 1) * (r + 3) + (n - r) ** 2) % 17 - 8, seed + 2)


def zeros_field(tmax):
    return tuple((ZERO,) * 6 for _ in range(tmax + 1))


def field_add(a, b):
    return tuple(va(x, y) for x, y in zip(a, b))


def field_scale(a, s):
    return tuple(vs(x, s) for x in a)


def field_dot(a, b):
    return sum((dot(x, y) for x, y in zip(a, b)), ZERO)


def power_derivative(a, k, da):
    return ZERO if k == 0 else k * a ** (k - 1) * da


def d_monom(a, p, b, q, c_val, r_pow, da, db, dc):
    term1 = (p * a ** (p - 1) * da if p > 0 else ZERO) * (b ** q) * (c_val ** r_pow)
    term2 = (a ** p) * (q * b ** (q - 1) * db if q > 0 else ZERO) * (c_val ** r_pow)
    term3 = (a ** p) * (b ** q) * (r_pow * c_val ** (r_pow - 1) * dc if r_pow > 0 else ZERO)
    return term1 + term2 + term3


def eval_poly3(terms, s_vals, t_vals, ds_vals=None):
    acc = ZERO
    for coeff, p0, p1, p2, ti in terms:
        if ds_vals is None:
            m = (s_vals[0] ** p0) * (s_vals[1] ** p1) * (s_vals[2] ** p2)
        else:
            m = d_monom(s_vals[0], p0, s_vals[1], p1, s_vals[2], p2,
                        ds_vals[0], ds_vals[1], ds_vals[2])
        acc += coeff * m * t_vals[ti]
    return acc


def wing_L(t_prev, t_cur, t_next, s_l, s_r, is_bdy, ds_l=None, ds_r=None):
    if is_bdy:
        terms = ((Q(-4, 384), 3, 0, 0, 2), (Q(-12, 384), 2, 1, 0, 2))
    else:
        terms = (
            (Q(1, 384), 3, 0, 0, 0), (Q(-1, 384), 3, 0, 0, 2),
            (Q(3, 384), 2, 1, 0, 0), (Q(-9, 384), 2, 1, 0, 2),
            (Q(6, 384), 1, 2, 0, 0),
        )
    return eval_poly3(terms, (s_l, s_r, ZERO), (t_prev, t_cur, t_next),
                      None if ds_l is None else (ds_l, ds_r, ZERO))


def coeff_step2_C(t0, t1, t2, s1, s2, ds1=None, ds2=None):
    terms = (
        (Q(4, 384), 3, 0, 0, 2),
        (Q(15, 384), 2, 1, 0, 1), (Q(9, 384), 2, 1, 0, 2),
        (Q(9, 384), 1, 2, 0, 0), (Q(15, 384), 1, 2, 0, 1),
        (Q(4, 384), 0, 3, 0, 0),
    )
    return eval_poly3(terms, (s1, s2, ZERO), (t0, t1, t2),
                      None if ds1 is None else (ds1, ds2, ZERO))


def coeff_step3_I(t0, t1, t2, t3, s1, s2, s3, ds1=None, ds2=None, ds3=None):
    terms = (
        (Q(9, 768), 2, 0, 1, 2), (Q(3, 768), 2, 0, 1, 3),
        (Q(12, 768), 1, 2, 0, 2), (Q(12, 768), 1, 2, 0, 3),
        (Q(24, 768), 1, 1, 1, 1), (Q(24, 768), 1, 1, 1, 2),
        (Q(3, 768), 1, 0, 2, 0), (Q(9, 768), 1, 0, 2, 1),
        (Q(4, 768), 0, 3, 0, 1), (Q(4, 768), 0, 3, 0, 2),
        (Q(12, 768), 0, 2, 1, 0), (Q(12, 768), 0, 2, 1, 1),
    )
    return eval_poly3(terms, (s1, s2, s3), (t0, t1, t2, t3),
                      None if ds1 is None else (ds1, ds2, ds3))


def audit():
    root = Path(__file__).resolve().parents[2]
    for name, count, digest in AUTHORITY:
        try:
            data = (root / name).read_bytes()
        except OSError:
            raise GateFailure("F_AUTHORITY") from None
        require(len(data) == count and sha256(data).hexdigest() == digest, "F_AUTHORITY")
    payload = []
    controls = [False] * 8
    counts = dict(mc=0, b2=0, b3=0, b4=0, bianchi=0, fw=0, cs=0)

    # Directed edge incidence construction of the K1 five-site Laplacian.
    lap = [[ZERO] * 5 for _ in range(5)]
    for jump, numerator in ((1, 29), (2, 65)):
        for tail in range(5):
            head = (tail + jump) % 5
            inc = [ZERO] * 5
            inc[tail], inc[head] = -ONE, ONE
            for i in range(5):
                for j in range(5):
                    lap[i][j] += Q(numerator, 324) * inc[i] * inc[j]
    lap = tuple(tuple(row) for row in lap)
    ell = (ONE, -ONE, ZERO, ZERO, ZERO)
    vmat = tuple(tuple(lap[i]) + (-ell[i] / 324,) for i in range(5)) + (
        tuple(-x / 324 for x in ell) + (ONE,),)
    i6, z6, i12 = eye(6), zm(6), eye(12)
    c = ma(i6, ms(vmat, -Q(1, 2)))
    c2 = mm(c, c)
    d = ma(i6, ms(c2, -ONE))
    k = block(z6, i6, ms(d, -ONE), z6)
    m0 = block(c, i6, ms(d, -ONE), c)
    zvec = (ZERO,) * 6

    powers = [i12]
    for deg in range(1, N + 1):
        powers.append(mm(powers[-1], k))
    rseries = [ms(powers[deg], Q(1, factorial(deg))) for deg in range(N + 1)]
    mseries = [mm(m0, r) for r in rseries]
    _, _, eseries, aseries = generating_series(mseries)
    for label, series in (("E", eseries), ("A", aseries)):
        for deg, matrix in enumerate(series):
            payload.append(f"{label}|{deg}|" + csv(flat(matrix)) + "\n")

    def gradient(x, alpha, degree, da=None):
        out = list(zeros_field(len(x) - 1))
        aa, ee = aseries[degree], eseries[degree]
        for n in range(1, len(x) - 1):
            left = va(mv(aa, x[n]), vs(mv(ee, x[n - 1]), -ONE))
            right = va(mv(aa, x[n]), vs(mv(ee, x[n + 1]), -ONE))
            if da is None:
                facl, facr = alpha[n - 1] ** degree, alpha[n] ** degree
            else:
                facl = power_derivative(alpha[n - 1], degree, da[n - 1])
                facr = power_derivative(alpha[n], degree, da[n])
            out[n] = va(vs(left, facl), vs(right, facr))
        return tuple(out)

    def raw_op(t, alpha, field, degree, da=None):
        tmax = len(field) - 1
        out = list(zeros_field(tmax))
        aa, ee = aseries[degree], eseries[degree]
        for n in range(1, tmax):
            pl = va(mv(aa, field[n]), vs(mv(ee, field[n - 1]), -ONE))
            pr = va(mv(ee, field[n + 1]), vs(mv(aa, field[n]), -ONE))
            al = alpha[n - 1] ** degree if da is None else power_derivative(alpha[n - 1], degree, da[n - 1])
            ar = alpha[n] ** degree if da is None else power_derivative(alpha[n], degree, da[n])
            out[n] = vs(va(vs(pl, al), vs(pr, ar)), t[n] / 2)
        return tuple(out)

    def raw_op_transpose(t, alpha, field, degree):
        tmax = len(field) - 1
        out = list(zeros_field(tmax))
        aa, ee = aseries[degree], eseries[degree]
        for n in range(1, tmax):
            al, ar = alpha[n - 1] ** degree, alpha[n] ** degree
            diag_term = vs(mv(aa, field[n]), (t[n] / 2) * (al - ar))
            from_left = vs(mv(ee, field[n - 1]), (t[n - 1] / 2) * al) if n > 1 else zvec
            from_right = vs(mv(ee, field[n + 1]), -(t[n + 1] / 2) * ar) if n < tmax - 1 else zvec
            out[n] = va(diag_term, va(from_left, from_right))
        return tuple(out)

    def skew1(t, alpha, field, da=None):
        tmax = len(field) - 1
        out = list(zeros_field(tmax))
        for n in range(1, tmax):
            ar = alpha[n] if da is None else da[n]
            al = alpha[n - 1] if da is None else da[n - 1]
            right = vs(field[n + 1], ar * (t[n] + t[n + 1]) / 8) if n + 1 <= tmax - 1 else zvec
            left = vs(field[n - 1], -al * (t[n - 1] + t[n]) / 8) if n - 1 >= 1 else zvec
            out[n] = va(left, right)
        return tuple(out)

    def skew2(t, alpha, field, da=None, include_step2=True):
        tmax = len(field) - 1
        out = list(zeros_field(tmax))
        for n in range(1, tmax):
            acc = zvec
            if n + 1 <= tmax - 1:
                s_sq = alpha[n] ** 2 if da is None else 2 * alpha[n] * da[n]
                acc = va(acc, vs(mv(c, field[n + 1]), -s_sq * (t[n] + t[n + 1]) / 16))
            if n - 1 >= 1:
                s_sq = alpha[n - 1] ** 2 if da is None else 2 * alpha[n - 1] * da[n - 1]
                acc = va(acc, vs(mv(c, field[n - 1]), s_sq * (t[n - 1] + t[n]) / 16))
            if include_step2 and n + 2 <= tmax - 1:
                s1, s2 = alpha[n], alpha[n + 1]
                c2_val = (-(s1 ** 2 * t[n + 2] + 4 * s1 * s2 * t[n + 1] + s2 ** 2 * t[n]) / 32
                          if da is None else
                          -(2 * s1 * da[n] * t[n + 2] + 4 * (da[n] * s2 + s1 * da[n + 1]) * t[n + 1]
                            + 2 * s2 * da[n + 1] * t[n]) / 32)
                acc = va(acc, vs(field[n + 2], c2_val))
            if include_step2 and n - 2 >= 1:
                s1, s2 = alpha[n - 2], alpha[n - 1]
                c2_val = ((s1 ** 2 * t[n] + 4 * s1 * s2 * t[n - 1] + s2 ** 2 * t[n - 2]) / 32
                          if da is None else
                          (2 * s1 * da[n - 2] * t[n] + 4 * (da[n - 2] * s2 + s1 * da[n - 1]) * t[n - 1]
                           + 2 * s2 * da[n - 1] * t[n - 2]) / 32)
                acc = va(acc, vs(field[n - 2], c2_val))
            out[n] = acc
        return tuple(out)

    def skew3_block(t, alpha, n, m, v, tmax, da=None, use_bdy_shift=True):
        step = m - n
        if step == 1:
            s_mid = alpha[n]
            s_cube = s_mid ** 3 if da is None else 3 * (s_mid ** 2) * da[n]
            part_c2 = vs(mv(c2, v), s_cube * (t[n] + t[n + 1]) / 48)
            wl = wing_L(t[n - 1], t[n], t[n + 1], alpha[n - 1], alpha[n],
                        use_bdy_shift and (n == 1),
                        None if da is None else da[n - 1], None if da is None else da[n])
            wr = wing_L(t[n + 2], t[n + 1], t[n], alpha[n + 1], alpha[n],
                        use_bdy_shift and (n == tmax - 2),
                        None if da is None else da[n + 1], None if da is None else da[n])
            return va(part_c2, vs(v, wl + wr))
        if step == 2:
            val = coeff_step2_C(t[n], t[n + 1], t[n + 2], alpha[n], alpha[n + 1],
                                None if da is None else da[n], None if da is None else da[n + 1])
            return vs(mv(c, v), val)
        if step == 3:
            val = coeff_step3_I(t[n], t[n + 1], t[n + 2], t[n + 3],
                                alpha[n], alpha[n + 1], alpha[n + 2],
                                None if da is None else da[n],
                                None if da is None else da[n + 1],
                                None if da is None else da[n + 2])
            return vs(v, val)
        return zvec

    def skew3(t, alpha, field, da=None, use_bdy_shift=True):
        tmax = len(field) - 1
        out = list(zeros_field(tmax))
        for n in range(1, tmax):
            acc = zvec
            for m in range(1, tmax):
                if abs(m - n) in (1, 2, 3):
                    if n < m:
                        acc = va(acc, skew3_block(t, alpha, n, m, field[m], tmax, da, use_bdy_shift))
                    else:
                        acc = va(acc, vs(skew3_block(t, alpha, m, n, field[m], tmax, da, use_bdy_shift), -ONE))
            out[n] = acc
        return tuple(out)

    def skew_m(m_ord, t, alpha, field, da=None, include_step2=True, use_bdy_shift=True):
        if m_ord == 1:
            return skew1(t, alpha, field, da)
        if m_ord == 2:
            return skew2(t, alpha, field, da, include_step2)
        if m_ord == 3:
            return skew3(t, alpha, field, da, use_bdy_shift)
        return zeros_field(len(field) - 1)

    def generator(x, alpha, t, degree, max_skew=3, da=None, include_step2=True, use_bdy_shift=True):
        tmax = len(x) - 1
        if degree == 0:
            return zeros_field(tmax)
        out = raw_op(t, alpha, x, degree - 1, da)
        for m_ord in range(1, min(max_skew, degree - 1) + 1):
            g_deg = degree - 1 - m_ord
            if da is None:
                corr = skew_m(m_ord, t, alpha, gradient(x, alpha, g_deg),
                              None, include_step2, use_bdy_shift)
            else:
                corr = field_add(
                    skew_m(m_ord, t, alpha, gradient(x, alpha, g_deg), da, include_step2, use_bdy_shift),
                    skew_m(m_ord, t, alpha, gradient(x, alpha, g_deg, da), None, include_step2, use_bdy_shift),
                )
            out = field_add(out, corr)
        return out

    def bracket(x, alpha, t, r, degree, max_skew=3, include_step2=True, use_bdy_shift=True):
        dt = tuple(t[b] - t[b - 1] for b in range(1, len(x)))
        dr = tuple(r[b] - r[b - 1] for b in range(1, len(x)))
        val = field_add(
            generator(x, alpha, r, degree, max_skew, dt, include_step2, use_bdy_shift),
            field_scale(generator(x, alpha, t, degree, max_skew, dr, include_step2, use_bdy_shift), -ONE),
        )
        for j in range(1, degree):
            xt = generator(x, alpha, t, j, max_skew, None, include_step2, use_bdy_shift)
            xr = generator(x, alpha, r, j, max_skew, None, include_step2, use_bdy_shift)
            val = field_add(val, generator(xt, alpha, r, degree - j, max_skew, None, include_step2, use_bdy_shift))
            val = field_add(val, field_scale(
                generator(xr, alpha, t, degree - j, max_skew, None, include_step2, use_bdy_shift), -ONE))
        return val

    def omega_op(t, r, alpha, field, degree):
        tmax = len(field) - 1
        out = list(zeros_field(tmax))
        ee = eseries[degree]
        for n in range(1, tmax):
            acc = zvec
            if n + 1 <= tmax - 1:
                fac = -Q(1, 4) * (r[n] * t[n + 1] - t[n] * r[n + 1]) * (alpha[n] ** degree)
                acc = va(acc, vs(mv(ee, field[n + 1]), fac))
            if n - 1 >= 1:
                fac = Q(1, 4) * (r[n - 1] * t[n] - t[n - 1] * r[n]) * (alpha[n - 1] ** degree)
                acc = va(acc, vs(mv(ee, field[n - 1]), fac))
            out[n] = acc
        return tuple(out)

    def curvature_op(t, r, alpha, field, k_deg, max_skew=3):
        tmax = len(field) - 1
        dt = tuple(t[b] - t[b - 1] for b in range(1, tmax + 1))
        dr = tuple(r[b] - r[b - 1] for b in range(1, tmax + 1))
        out = omega_op(t, r, alpha, field, k_deg)
        if 1 <= k_deg + 1 <= max_skew:
            out = field_add(out, skew_m(k_deg + 1, r, alpha, field, dt))
            out = field_add(out, field_scale(skew_m(k_deg + 1, t, alpha, field, dr), -ONE))
        for j in range(1, min(max_skew, k_deg) + 1):
            i = k_deg - j
            # L_r^(i) A_t^(j) + A_t^(j) (L_r^(i))^T - (t <-> r)
            at_f = skew_m(j, t, alpha, field)
            ar_f = skew_m(j, r, alpha, field)
            lrt_f = raw_op_transpose(r, alpha, field, i)
            ltt_f = raw_op_transpose(t, alpha, field, i)
            term_tr = field_add(raw_op(r, alpha, at_f, i), skew_m(j, t, alpha, lrt_f))
            term_rt = field_add(raw_op(t, alpha, ar_f, i), skew_m(j, r, alpha, ltt_f))
            out = field_add(out, field_add(term_tr, field_scale(term_rt, -ONE)))
        for i in range(1, min(max_skew, k_deg - 1) + 1):
            for k_idx in range(1, min(max_skew, k_deg - i) + 1):
                j = k_deg - i - k_idx
                if j >= 0:
                    at_f = skew_m(k_idx, t, alpha, field)
                    ar_f = skew_m(k_idx, r, alpha, field)
                    h_at = gradient(at_f, alpha, j)
                    h_ar = gradient(ar_f, alpha, j)
                    aha = field_add(skew_m(i, r, alpha, h_at),
                                    field_scale(skew_m(i, t, alpha, h_ar), -ONE))
                    out = field_add(out, aha)
        return out

    # 1. Exact resolution of the #1666 cubic commutator witness.
    u = (ONE, ZERO, -ONE, ZERO, ZERO, ZERO)
    xw = list(zeros_field(4))
    xw[3] = u
    xw = tuple(xw)
    aw = (ZERO, ZERO, ONE, ZERO)
    tw = (ZERO, ONE, ZERO, ZERO, ZERO)
    sw = (ZERO, ZERO, ONE, ZERO, ZERO)
    w_raw2 = bracket(xw, aw, tw, sw, 2, max_skew=0)
    w_deg2_2 = bracket(xw, aw, tw, sw, 2, max_skew=1)
    w_raw3 = bracket(xw, aw, tw, sw, 3, max_skew=0)
    w_deg2_3 = bracket(xw, aw, tw, sw, 3, max_skew=1)
    w_deg3_3 = bracket(xw, aw, tw, sw, 3, max_skew=2)
    w_step1_only = bracket(xw, aw, tw, sw, 3, max_skew=2, include_step2=False)
    cubic_slice = (Q(-395, 5184), ZERO, Q(395, 5184), Q(-1, 144), Q(1, 144), Q(-1, 5184))
    require(w_raw2[1] == vs(u, -Q(1, 4)) and w_deg2_2 == zeros_field(4), "F_WITNESS")
    require(w_raw3[1] == vs(mv(c, u), Q(1, 4)), "F_WITNESS")
    require(w_deg2_3[1] == vs(mv(c, u), -Q(1, 8)) == cubic_slice, "F_WITNESS")
    require(w_deg3_3 == zeros_field(4), "F_WITNESS")
    require(w_step1_only[1] == cubic_slice, "F_WITNESS")
    controls[0] = w_raw2 != zeros_field(4)
    controls[1] = w_deg2_3[1] == cubic_slice and w_deg2_3 != zeros_field(4)
    controls[2] = w_step1_only[1] == cubic_slice and w_step1_only != zeros_field(4)
    for label, field in (("RAW2", w_raw2), ("DEG2_2", w_deg2_2), ("RAW3", w_raw3),
                         ("DEG2_3", w_deg2_3), ("DEG3_3", w_deg3_3)):
        payload.append("W1666|" + label + "|" + csv(flat(field)) + "\n")

    # 2. Maurer-Cartan factorization [delta_t, delta_r] x = F_{t,r}(s) grad_q S(x, s).
    for tmax in (3, 4, 5):
        x = tuple(tuple(fixture(1, n, r_idx) for r_idx in range(6)) for n in range(tmax + 1))
        alpha = tuple(fixture(2, b, 6) for b in range(1, tmax + 1))
        t = tuple(fixture(3, n, 7) if 0 < n < tmax else ZERO for n in range(tmax + 1))
        r = tuple(fixture(4, n, 5) if 0 < n < tmax else ZERO for n in range(tmax + 1))
        grads = [gradient(x, alpha, j) for j in range(N)]
        for max_skew in (0, 1, 2, 3):
            for deg in (2, 3, 4):
                lhs = bracket(x, alpha, t, r, deg, max_skew)
                rhs = zeros_field(tmax)
                for k_deg in range(deg - 1):
                    rhs = field_add(rhs, curvature_op(t, r, alpha, grads[deg - 2 - k_deg], k_deg, max_skew))
                require(lhs == rhs, "F_MAURER_CARTAN")
            mc_deg4 = bracket(x, alpha, t, r, 4, max_skew)
            if tmax == 4 and max_skew == 2:
                controls[3] = mc_deg4 != zeros_field(tmax)
            if tmax == 4 and max_skew == 3:
                no_bdy = bracket(x, alpha, t, r, 4, max_skew=3, use_bdy_shift=False)
                controls[5] = no_bdy != zeros_field(tmax)
            payload.append(f"MC|{tmax}|{max_skew}|" + csv(flat(mc_deg4)) + "\n")
            counts["mc"] += 1

    # 3. Multi-horizon off-shell commutator closure through degree 4.
    for tmax in (3, 4, 5, 6):
        for seed in (1, 2, 3):
            x = tuple(tuple(fixture(seed, n, r_idx) for r_idx in range(6)) for n in range(tmax + 1))
            alpha = tuple(fixture(seed + 1, b, 6) for b in range(1, tmax + 1))
            t = tuple(fixture(seed + 2, n, 7) if 0 < n < tmax else ZERO for n in range(tmax + 1))
            r = tuple(fixture(seed + 3, n, 5) if 0 < n < tmax else ZERO for n in range(tmax + 1))
            b2 = bracket(x, alpha, t, r, 2, max_skew=1)
            b3 = bracket(x, alpha, t, r, 3, max_skew=2)
            b4 = bracket(x, alpha, t, r, 4, max_skew=3)
            require(b2 == zeros_field(tmax), "F_BRACKET_DEG2")
            require(b3 == zeros_field(tmax), "F_BRACKET_DEG3")
            require(b4 == zeros_field(tmax), "F_BRACKET_DEG4")
            counts["b2"] += 1
            counts["b3"] += 1
            counts["b4"] += 1
            payload.append(f"BC|{tmax}|{seed}|0|0|0\n")

    # 4. Parameter-space Bianchi 2-cocycle and nonlinear A H A self-interaction check.
    def r2_eval(t_p, r_p, alpha_p, field, da_p=None, include_aha=True):
        tmax = len(field) - 1
        # Evaluate R_{t,r}^(2)(s) or its directional derivative da_p on field.
        if da_p is None:
            out = omega_op(t_p, r_p, alpha_p, field, 2)
            for i, j in ((0, 2), (1, 1)):
                at_f = skew_m(j, t_p, alpha_p, field)
                ar_f = skew_m(j, r_p, alpha_p, field)
                lrt_f = raw_op_transpose(r_p, alpha_p, field, i)
                ltt_f = raw_op_transpose(t_p, alpha_p, field, i)
                term_tr = field_add(raw_op(r_p, alpha_p, at_f, i), skew_m(j, t_p, alpha_p, lrt_f))
                term_rt = field_add(raw_op(t_p, alpha_p, ar_f, i), skew_m(j, r_p, alpha_p, ltt_f))
                out = field_add(out, field_add(term_tr, field_scale(term_rt, -ONE)))
            if include_aha:
                at_f = skew1(t_p, alpha_p, field)
                ar_f = skew1(r_p, alpha_p, field)
                aha = field_add(skew1(r_p, alpha_p, gradient(at_f, alpha_p, 0)),
                                field_scale(skew1(t_p, alpha_p, gradient(ar_f, alpha_p, 0)), -ONE))
                out = field_add(out, aha)
            return out
        # Directional derivative along da_p (since R^(2) is quadratic in alpha_p):
        out = list(zeros_field(tmax))
        ee2 = eseries[2]
        for n in range(1, tmax):
            acc = zvec
            if n + 1 <= tmax - 1:
                fac = -Q(1, 4) * (r_p[n] * t_p[n + 1] - t_p[n] * r_p[n + 1]) * (2 * alpha_p[n] * da_p[n])
                acc = va(acc, vs(mv(ee2, field[n + 1]), fac))
            if n - 1 >= 1:
                fac = Q(1, 4) * (r_p[n - 1] * t_p[n] - t_p[n - 1] * r_p[n]) * (2 * alpha_p[n - 1] * da_p[n - 1])
                acc = va(acc, vs(mv(ee2, field[n - 1]), fac))
            out[n] = acc
        out = tuple(out)
        # (i=0, j=2): L^(0) is alpha-independent, A^(2) is differentiated along da_p
        at2_d = skew2(t_p, alpha_p, field, da_p)
        ar2_d = skew2(r_p, alpha_p, field, da_p)
        lrt0 = raw_op_transpose(r_p, alpha_p, field, 0)
        ltt0 = raw_op_transpose(t_p, alpha_p, field, 0)
        t02 = field_add(raw_op(r_p, alpha_p, at2_d, 0), skew2(t_p, alpha_p, lrt0, da_p))
        r02 = field_add(raw_op(t_p, alpha_p, ar2_d, 0), skew2(r_p, alpha_p, ltt0, da_p))
        out = field_add(out, field_add(t02, field_scale(r02, -ONE)))
        # (i=1, j=1): product rule over L^(1) and A^(1)
        for da_L, da_A in ((da_p, None), (None, da_p)):
            at1 = skew1(t_p, alpha_p, field, da_A)
            ar1 = skew1(r_p, alpha_p, field, da_A)
            alpha_L = alpha_p if da_L is None else da_L
            lrt1 = raw_op_transpose(r_p, alpha_L, field, 1)
            ltt1 = raw_op_transpose(t_p, alpha_L, field, 1)
            t11 = field_add(raw_op(r_p, alpha_p, at1, 1, da_L), skew1(t_p, alpha_p, lrt1, da_A))
            r11 = field_add(raw_op(t_p, alpha_p, ar1, 1, da_L), skew1(r_p, alpha_p, ltt1, da_A))
            out = field_add(out, field_add(t11, field_scale(r11, -ONE)))
        if include_aha:
            for da_l, da_r in ((da_p, None), (None, da_p)):
                at1 = skew1(t_p, alpha_p, field, da_r)
                ar1 = skew1(r_p, alpha_p, field, da_r)
                aha = field_add(skew1(r_p, alpha_p, gradient(at1, alpha_p, 0), da_l),
                                field_scale(skew1(t_p, alpha_p, gradient(ar1, alpha_p, 0), da_l), -ONE))
                out = field_add(out, aha)
        return out

    for tmax in (3, 4, 5, 6):
        alpha = tuple(fixture(1, b, 6) for b in range(1, tmax + 1))
        t = tuple(fixture(2, n, 7) if 0 < n < tmax else ZERO for n in range(tmax + 1))
        r = tuple(fixture(3, n, 5) if 0 < n < tmax else ZERO for n in range(tmax + 1))
        u_p = tuple(fixture(4, n, 3) if 0 < n < tmax else ZERO for n in range(tmax + 1))
        dt = tuple(t[b] - t[b - 1] for b in range(1, tmax + 1))
        dr = tuple(r[b] - r[b - 1] for b in range(1, tmax + 1))
        du = tuple(u_p[b] - u_p[b - 1] for b in range(1, tmax + 1))
        for n in range(1, tmax):
            for m in range(n + 1, tmax):
                cols_r2 = []
                for col in range(6):
                    probe = list(zeros_field(tmax))
                    probe[m] = i6[col]
                    probe = tuple(probe)
                    r2_vec = r2_eval(t, r, alpha, probe)
                    curl_a3 = va(skew3(r, alpha, probe, dt)[n],
                                 vs(skew3(t, alpha, probe, dr)[n], -ONE))
                    require(va(r2_vec[n], curl_a3) == zvec, "F_BIANCHI")
                    b_sum = va(r2_eval(t, r, alpha, probe, du)[n],
                               va(r2_eval(r, u_p, alpha, probe, dt)[n],
                                  r2_eval(u_p, t, alpha, probe, dr)[n]))
                    require(b_sum == zvec, "F_BIANCHI")
                    cols_r2.append(r2_vec[n])
                r2_block = mt(tuple(cols_r2))
                payload.append(f"BI|{tmax}|{n}|{m}|" + csv(flat(r2_block)) + "\n")
                counts["bianchi"] += 1

    # Negative control NC05: omitting A H A breaks Bianchi cocycle at (1, 4) on T = 5.
    alpha5 = (ONE, ONE, ONE, ONE, ONE)
    t5 = (ZERO, ONE, ZERO, ZERO, ZERO, ZERO)
    r5 = (ZERO, ZERO, ONE, ZERO, ZERO, ZERO)
    u5 = (ZERO, ZERO, ZERO, ONE, ZERO, ZERO)
    dt5 = tuple(t5[b] - t5[b - 1] for b in range(1, 6))
    dr5 = tuple(r5[b] - r5[b - 1] for b in range(1, 6))
    du5 = tuple(u5[b] - u5[b - 1] for b in range(1, 6))
    probe5 = list(zeros_field(5))
    probe5[4] = i6[0]
    probe5 = tuple(probe5)
    no_aha_bianchi = va(
        r2_eval(t5, r5, alpha5, probe5, du5, include_aha=False)[1],
        va(r2_eval(r5, u5, alpha5, probe5, dt5, include_aha=False)[1],
           r2_eval(u5, t5, alpha5, probe5, dr5, include_aha=False)[1]),
    )
    require(no_aha_bianchi == vs(i6[0], Q(1, 32)), "F_CONTROL")
    controls[4] = no_aha_bianchi == vs(i6[0], Q(1, 32))

    # 5. Forced affine scalar-lapse completion and vacuum cold-start trajectory.
    m_eq = [list(row) for row in vmat]
    m_eq[0] = [ONE, ONE, ONE, ONE, ONE, ZERO]
    f_pos = (ZERO, ZERO, ZERO, ZERO, ZERO, Q(1, 4))
    x_star_pos = mv(inv(m_eq), f_pos)
    expected_x_star = (
        Q(20493, 17367514), Q(-20493, 17367514), Q(1458, 8683757),
        ZERO, Q(-1458, 8683757), Q(4342005, 17367514),
    )
    require(x_star_pos == expected_x_star and mv(vmat, x_star_pos) == f_pos, "F_EQUILIBRIUM")
    e_star_pos = Q(1, 2) * dot(f_pos, x_star_pos)
    e_cold_pos = Q(1, 2) * quad(d, x_star_pos)
    require(e_star_pos == Q(4342005, 8683757) * Q(1, 16), "F_EQUILIBRIUM")
    require(e_cold_pos == e_star_pos - Q(1, 128) == Q(26052283, 69470056) * Q(1, 16), "F_EQUILIBRIUM")
    payload.append("EQ|" + csv(x_star_pos) + "|" + str(e_star_pos) + "|" + str(e_cold_pos) + "\n")

    def bond_coefficients(q, bigq):
        return tuple((quad(aa, q) + quad(aa, bigq)) / 2 - dot(q, mv(ee, bigq))
                     for aa, ee in zip(aseries, eseries))

    def forced_action(x, alpha, a_val):
        x_eq = vs(x_star_pos, Q(a_val))
        e_eq = e_star_pos * (a_val ** 2)
        x_tilde = tuple(va(qn, vs(x_eq, -ONE)) for qn in x)
        res = [ZERO] * (N + 1)
        res[0] = (quad(vmat, x_tilde[0]) + quad(vmat, x_tilde[-1])) / 4
        res[0] += -Q(a_val, 8) * (x[0][5] + x[-1][5]) + e_eq / 2
        for b in range(1, len(x)):
            coeffs = bond_coefficients(x_tilde[b - 1], x_tilde[b])
            for deg, coeff in enumerate(coeffs):
                res[deg] += (alpha[b - 1] ** deg) * coeff
            res[0] += e_eq
            res[1] += alpha[b - 1] * e_eq
        return tuple(res)

    for a_val in (-1, 0, 1):
        x_eq = vs(x_star_pos, Q(a_val))
        f_eq = vs(f_pos, Q(a_val))
        for tmax in (3, 4, 5):
            for seed in (1, 2):
                x = tuple(tuple(fixture(seed, n, r_idx) for r_idx in range(6)) for n in range(tmax + 1))
                alpha = tuple(fixture(seed + 1, b, 6) for b in range(1, tmax + 1))
                t = tuple(fixture(seed + 2, n, 7) if 0 < n < tmax else ZERO for n in range(tmax + 1))
                r = tuple(fixture(seed + 3, n, 5) if 0 < n < tmax else ZERO for n in range(tmax + 1))
                scoeff = forced_action(x, alpha, a_val)
                aut0 = sum((dot(va(x[b], vs(x[b - 1], -ONE)), va(x[b], vs(x[b - 1], -ONE))) / 2
                            for b in range(1, tmax + 1)), ZERO)
                aut0 -= sum((quad(vmat, x[n]) / 2 - dot(f_eq, x[n]) for n in range(1, tmax)), ZERO)
                require(scoeff[0] == aut0, "F_FORCED_ACTION")
                x_tilde = tuple(va(qn, vs(x_eq, -ONE)) for qn in x)
                da = tuple(t[b] - t[b - 1] for b in range(1, tmax + 1))
                bondjets = [bond_coefficients(x_tilde[b - 1], x_tilde[b]) for b in range(1, tmax + 1)]
                pwork = tuple(sum((power_derivative(alpha[b], j, da[b]) * bondjets[b][j]
                                   for b in range(tmax)), ZERO) for j in range(N + 1))
                grads = [gradient(x_tilde, alpha, j) for j in range(N + 1)]
                adj = [generator(x_tilde, alpha, t, j, max_skew=3) for j in range(N + 1)]
                adjwork = tuple(sum((field_dot(grads[j], adj[k_idx - j]) for j in range(k_idx + 1)), ZERO)
                                for k_idx in range(N + 1))
                require(all(pwork[j] + adjwork[j] == 0 for j in range(N + 1)), "F_FORCED_WARD")
                for deg in (2, 3, 4):
                    require(bracket(x_tilde, alpha, t, r, deg, max_skew=3) == zeros_field(tmax), "F_FORCED_BRACKET")
                counts["fw"] += 1
                payload.append(f"FW|{a_val}|{tmax}|{seed}|" + csv(scoeff) + "|" + csv(pwork) + "\n")

    cold_q2 = {}
    for a_val in (-1, 0, 1):
        x_eq = vs(x_star_pos, Q(a_val))
        f_eq = vs(f_pos, Q(a_val))
        e_eq = e_star_pos * (a_val ** 2)
        z_tilde = vs(x_eq, -ONE) + vs(f_eq, Q(1, 2))
        q_hist = []
        for n in range(6):
            qn = va(z_tilde[:6], x_eq)
            pn = z_tilde[6:]
            q_hist.append(qn)
            h_bond = (dot(pn, pn) + quad(d, z_tilde[:6])) / 2
            require(h_bond == e_eq, "F_COLD_START")
            z_next = mv(m0, z_tilde)
            bond_c = bond_coefficients(z_tilde[:6], z_next[:6])
            require(bond_c[1] + e_eq == 0, "F_COLD_START")
            if a_val == 1 and n == 0:
                controls[6] = bond_c[1] == -e_star_pos and bond_c[1] != 0
                wrong_znext = mv(m0, vs(x_eq, -ONE) + zvec)
                wrong_c1 = bond_coefficients(vs(x_eq, -ONE), wrong_znext[:6])[1] + e_eq
                require(wrong_c1 == Q(1, 128), "F_CONTROL")
                controls[7] = wrong_c1 == Q(1, 128)
            counts["cs"] += 1
            payload.append(f"CS|{a_val}|{n}|" + csv(qn) + "|" + str(h_bond) + "\n")
            z_tilde = z_next
        require(q_hist[0] == zvec and q_hist[1] == f_eq, "F_COLD_START")
        for n in range(1, 5):
            lhs = va(va(q_hist[n + 1], vs(mv(c, q_hist[n]), -Q(2))), q_hist[n - 1])
            require(lhs == f_eq, "F_COLD_START")
        cold_q2[a_val] = q_hist[2][:5]

    metric_diff = va(cold_q2[1], vs(cold_q2[-1], -ONE))
    expected_diff = (Q(1, 648), Q(-1, 648), ZERO, ZERO, ZERO)
    require(metric_diff == expected_diff, "F_COLD_START")
    require(all(controls), "F_CONTROL")
    for number in range(1, 9):
        payload.append(f"N|NC{number:02d}|DETECTED\n")
    require(counts == dict(mc=12, b2=12, b3=12, b4=12, bianchi=20, fw=18, cs=18), "F_COUNTS")
    digest = sha256("".join(payload).encode("ascii")).hexdigest()
    certificate = (
        "CERTIFICATE=P-INTEGER-MAURER-CARTAN-LAPSE-CLOSURE-1\n"
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
        proc = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("breaker.py"))],
            capture_output=True,
            check=False,
        )
        require(proc.returncode == 0 and proc.stdout == certificate, "F_BREAKER")
    except GateFailure as exc:
        sys.stdout.buffer.write(f"RESULT=FAIL\nGATE={exc}\n".encode("ascii"))
        return 1
    sys.stdout.buffer.write(certificate + b"BREAKER_RAW_BYTES=IDENTICAL\nRESULT=PASS\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
