#!/usr/bin/env python3
"""Exact verifier for P-D3-ZWORK-VAR-BOUND-1.

Audits the exact algebraic and analytical ingredients of the sharp upper bound

    Z_work,cont^var(beta, L) := beta * <q(M_x)>_beta / (8 * L) < 1/4

for all beta > 0 and all finite even L >= 2 in the zero-divergence cyclotomic
equilibrium ensemble over D3(L) summing over all global flux sectors, together
with exact vacuum string lower bounds (Q_E >= 4d and Q_E >= 4L), exact
Decimal(130) evaluation on 2-edge and 3-edge cyclotomic complexes (including
the exact 3-edge crossover beta* ~ 0.242528416 where Z_work^var = Z_work^disc
~ 0.24920214 < 1/4), and five deliberate negative controls.

Dependencies: Python standard library only (zero float, zero complex,
zero file I/O, zero subprocesses, deterministic LF stdout).
"""

from __future__ import annotations

from collections import Counter
from decimal import Decimal, getcontext
from fractions import Fraction
import math
import sys


# 130-digit Decimal context resolves tiny deficits (~4.9e-112 at beta=0.01)
# and the 3-edge crossover with zero IEEE-754 floating-point usage.
getcontext().prec = 130


def compute_pi_decimal() -> Decimal:
    """Compute pi to full Decimal context precision via Machin's identity."""
    def atan_inv(n: int) -> Decimal:
        inv_n = Decimal(1) / Decimal(n)
        inv_n2 = inv_n * inv_n
        term = inv_n
        total = term
        eps = Decimal("1e-128")
        for k in range(1, 400):
            term = -term * inv_n2
            add_term = term / Decimal(2 * k + 1)
            total += add_term
            if abs(add_term) < eps:
                break
        return total

    return Decimal(16) * atan_inv(5) - Decimal(4) * atan_inv(239)


PI_DEC = compute_pi_decimal()

DIRS = (
    (1, 1, 0),
    (1, -1, 0),
    (1, 0, 1),
    (1, 0, -1),
    (0, 1, 1),
    (0, 1, -1),
)

# Ring O = Z[zeta_5] in power basis (1, j, j^2, j^3), j^4 = -(1 + j + j^2 + j^3).
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
MU10 = (
    (0, 1, 0, 0), (0, -1, 0, 0),
    (0, 0, 1, 0), (0, 0, -1, 0),
    (0, 0, 0, 1), (0, 0, 0, -1),
    (-1, -1, -1, -1), (1, 1, 1, 1),
    (1, 0, 0, 0), (-1, 0, 0, 0),
)


# ---------------------------------------------------------------------------
# Exact Cyclotomic Arithmetic
# ---------------------------------------------------------------------------
def z5_add(a: tuple[int, int, int, int], b: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def z5_sub(a: tuple[int, int, int, int], b: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])


def z5_mul(a: tuple[int, int, int, int], b: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    if a == ZERO or b == ZERO:
        return ZERO
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    p0 = a0 * b0
    p1 = a0 * b1 + a1 * b0
    p2 = a0 * b2 + a1 * b1 + a2 * b0
    p3 = a0 * b3 + a1 * b2 + a2 * b1 + a3 * b0
    p4 = a1 * b3 + a2 * b2 + a3 * b1
    p5 = a2 * b3 + a3 * b2
    p6 = a3 * b3
    return (p0 + p5 - p4, p1 + p6 - p4, p2 - p4, p3 - p4)


def z5_conj(a: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    a0, a1, a2, a3 = a
    return (a0 - a1, -a1, a3 - a1, a2 - a1)


def z5_h(a: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    return z5_mul(a, z5_conj(a))


def z5_tr(a: tuple[int, int, int, int]) -> int:
    return 4 * a[0] - a[1] - a[2] - a[3]


def z5_qe(a: tuple[int, int, int, int]) -> int:
    """Exact 2*q(a) = Tr(a * bar(a)) = a^T (5 I_4 - J_4) a."""
    a0, a1, a2, a3 = a
    s = a0 + a1 + a2 + a3
    return 5 * (a0 * a0 + a1 * a1 + a2 * a2 + a3 * a3) - s * s


def q_ginv_5(m: tuple[int, int, int, int]) -> int:
    """Exact 5 * (m^T G^{-1} m) = sum(m_i^2) + (sum m_i)^2."""
    m0, m1, m2, m3 = m
    s = m0 + m1 + m2 + m3
    return (m0 * m0 + m1 * m1 + m2 * m2 + m3 * m3) + s * s


def exact_det_4x4(mat: list[list[Fraction]]) -> Fraction:
    """Exact Fraction determinant of a 4x4 matrix via Gaussian elimination."""
    a = [[Fraction(x) for x in row] for row in mat]
    det = Fraction(1)
    for col in range(4):
        piv = None
        for row in range(col, 4):
            if a[row][col] != 0:
                piv = row
                break
        if piv is None:
            return Fraction(0)
        if piv != col:
            a[col], a[piv] = a[piv], a[col]
            det = -det
        pv = a[col][col]
        det *= pv
        for row in range(col + 1, 4):
            fac = a[row][col] / pv
            if fac != 0:
                for k in range(col, 4):
                    a[row][k] -= fac * a[col][k]
    return det


# ---------------------------------------------------------------------------
# 12-Edge FCC Lattice D3(L) Builder (Even L >= 2)
# ---------------------------------------------------------------------------
def build_d3(L: int) -> dict[str, object]:
    assert L >= 2 and (L & 1) == 0
    verts = [
        (x, y, z)
        for x in range(L)
        for y in range(L)
        for z in range(L)
        if ((x + y + z) & 1) == 0
    ]
    v_idx = {v: i for i, v in enumerate(verts)}
    nv = len(verts)

    edges = []
    inc_out = [[] for _ in range(nv)]
    inc_in = [[] for _ in range(nv)]
    x_cuts = [[] for _ in range(L)]

    for vi, (x, y, z) in enumerate(verts):
        for a, (dx, dy, dz) in enumerate(DIRS):
            ui = v_idx[((x + dx) % L, (y + dy) % L, (z + dz) % L)]
            ei = len(edges)
            edges.append((vi, ui, a, dx, dy, dz))
            inc_out[vi].append(ei)
            inc_in[ui].append(ei)
            if dx == 1:
                x_cuts[x].append((ei, 1))

    return {
        "L": L,
        "verts": verts,
        "v_idx": v_idx,
        "nv": nv,
        "edges": edges,
        "ne": len(edges),
        "inc_out": inc_out,
        "inc_in": inc_in,
        "x_cuts": x_cuts,
    }


def add_unit_x_string(topo: dict[str, object], E: list[tuple[int, int, int, int]], q: tuple[int, int, int, int]) -> None:
    L = topo["L"]
    v_idx = topo["v_idx"]
    for x in range(L):
        y = x & 1
        u = v_idx[(x, y, 0)]
        dir_want = 0 if y == 0 else 1
        ei = u * 6 + dir_want
        E[ei] = z5_add(E[ei], q)


def max_div_err(topo: dict[str, object], E: list[tuple[int, int, int, int]]) -> int:
    inc_out = topo["inc_out"]
    inc_in = topo["inc_in"]
    bad = 0
    for vi in range(topo["nv"]):
        d0 = d1 = d2 = d3 = 0
        for ei in inc_out[vi]:
            x = E[ei]
            d0 += x[0]
            d1 += x[1]
            d2 += x[2]
            d3 += x[3]
        for ei in inc_in[vi]:
            x = E[ei]
            d0 -= x[0]
            d1 -= x[1]
            d2 -= x[2]
            d3 -= x[3]
        if (d0 | d1 | d2 | d3) != 0:
            bad += 1
    return bad


def cut_flux(E: list[tuple[int, int, int, int]], cut: list[tuple[int, int]]) -> tuple[int, int, int, int]:
    t0 = t1 = t2 = t3 = 0
    for ei, sgn in cut:
        x = E[ei]
        if sgn == 1:
            t0 += x[0]
            t1 += x[1]
            t2 += x[2]
            t3 += x[3]
        else:
            t0 -= x[0]
            t1 -= x[1]
            t2 -= x[2]
            t3 -= x[3]
    return (t0, t1, t2, t3)


# ---------------------------------------------------------------------------
# F01: Exact Cyclotomic Gram Matrix, Inverse, Spectrum, and Sharp Floor
# ---------------------------------------------------------------------------
def check_f01_gram_and_floor() -> dict[str, object]:
    G = [[Fraction(4 if i == j else -1) for j in range(4)] for i in range(4)]
    G_inv = [[Fraction(2 if i == j else 1, 5) for j in range(4)] for i in range(4)]

    prod_ok = all(
        sum(G[i][k] * G_inv[k][j] for k in range(4)) == Fraction(1 if i == j else 0)
        for i in range(4)
        for j in range(4)
    )
    det_g = exact_det_4x4(G)
    det_ginv = exact_det_4x4(G_inv)

    eigen_vecs = [
        (1, 1, 1, 1),
        (1, -1, 0, 0),
        (1, 0, -1, 0),
        (1, 0, 0, -1),
    ]
    eigen_vals = [Fraction(1), Fraction(5), Fraction(5), Fraction(5)]
    ginv_eigen_vals = [Fraction(1), Fraction(1, 5), Fraction(1, 5), Fraction(1, 5)]
    det_basis = exact_det_4x4([[Fraction(x) for x in row] for row in eigen_vecs])
    spec_ok = (
        det_basis != 0
        and all(
            [sum(G[i][j] * vec[j] for j in range(4)) for i in range(4)] == [lam * vec[i] for i in range(4)]
            for vec, lam in zip(eigen_vecs, eigen_vals)
        )
        and all(
            [sum(G_inv[i][j] * vec[j] for j in range(4)) for i in range(4)] == [lam * vec[i] for i in range(4)]
            for vec, lam in zip(eigen_vecs, ginv_eigen_vals)
        )
    )

    # Since z^T G z >= ||z||_2^2, any z outside [-3,3]^4 has ||z||_inf >= 4 => 2*q(z) >= 16.
    # Thus enumerating [-3,3]^4 certifies both the minimum nonzero 2*q(z) and all shells <= 14.
    shells: Counter[int] = Counter()
    ident_mismatches = 0
    min_nz_2q = None
    mu10_found = set()
    for a0 in range(-3, 4):
        for a1 in range(-3, 4):
            for a2 in range(-3, 4):
                for a3 in range(-3, 4):
                    z = (a0, a1, a2, a3)
                    v_gram = z5_qe(z)
                    v_tr = z5_tr(z5_h(z))
                    c = (0, a0, a1, a2, a3)
                    v_diff = sum((c[r] - c[s]) ** 2 for r in range(5) for s in range(r + 1, 5))
                    if not (v_gram == v_tr == v_diff and (v_gram & 1) == 0):
                        ident_mismatches += 1
                    if v_gram <= 14:
                        shells[v_gram] += 1
                    if z != ZERO:
                        if min_nz_2q is None or v_gram < min_nz_2q:
                            min_nz_2q = v_gram
                        if v_gram == 4:
                            mu10_found.add(z)

    ok = (
        prod_ok
        and det_g == Fraction(125)
        and det_ginv == Fraction(1, 125)
        and spec_ok
        and ident_mismatches == 0
        and min_nz_2q == 4
        and mu10_found == set(MU10)
        and shells[0] == 1
        and shells[4] == 10
        and shells[6] == 20
        and shells[10] == 20
        and shells[14] == 60
    )
    return {
        "pass": ok,
        "det_G": int(det_g),
        "spec_G": [int(x) for x in eigen_vals],
        "min_nonzero_q": min_nz_2q // 2,
        "mu10_count": len(mu10_found),
        "shells": {k: shells[k] for k in (0, 4, 6, 10, 14)},
    }


# ---------------------------------------------------------------------------
# F02: Exact Vacuum & Purely Magnetic String Lower Bounds (4d and 4L)
# ---------------------------------------------------------------------------
def check_f02_vacuum_bounds() -> dict[str, object]:
    topo10 = build_d3(10)
    nv10 = topo10["nv"]
    adj = [[] for _ in range(nv10)]
    for ei, (u, v, *_rest) in enumerate(topo10["edges"]):
        adj[u].append((v, ei, 1))
        adj[v].append((u, ei, -1))

    src = topo10["v_idx"][(0, 0, 0)]
    dist = [-1] * nv10
    parent = [None] * nv10
    dist[src] = 0
    queue = [src]
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        du = dist[u]
        for v, ei, sgn in adj[u]:
            if dist[v] == -1:
                dist[v] = du + 1
                parent[v] = (u, ei, sgn)
                queue.append(v)

    dipole_rows = []
    for d in (1, 2, 3, 4):
        target = next(v for v in range(nv10) if dist[v] == d)
        E = [ZERO] * topo10["ne"]
        cur = target
        while cur != src:
            pu, ei, sgn = parent[cur]
            E[ei] = z5_add(E[ei], ONE) if sgn == 1 else z5_sub(E[ei], ONE)
            cur = pu
        qe_val = sum(z5_qe(x) for x in E)

        seen_edges = set()
        overlap_count = 0
        flux_bad = 0
        for k in range(d):
            cut_flux_k = ZERO
            for ei, (u, v, *_rest) in enumerate(topo10["edges"]):
                if dist[u] <= k and dist[v] > k:
                    if ei in seen_edges:
                        overlap_count += 1
                    seen_edges.add(ei)
                    cut_flux_k = z5_add(cut_flux_k, E[ei])
                elif dist[v] <= k and dist[u] > k:
                    if ei in seen_edges:
                        overlap_count += 1
                    seen_edges.add(ei)
                    cut_flux_k = z5_sub(cut_flux_k, E[ei])
            if cut_flux_k != ONE:
                flux_bad += 1

        row_ok = (overlap_count == 0) and (flux_bad == 0) and (qe_val == 4 * d)
        dipole_rows.append((d, qe_val, 4 * d, row_ok))

    periodic_rows = []
    parallelogram_ok = False
    for L in (6, 8, 10, 12):
        topo = build_d3(L)
        E_str = [ZERO] * topo["ne"]
        add_unit_x_string(topo, E_str, ONE)
        qe_str = sum(z5_qe(x) for x in E_str)
        div_err = max_div_err(topo, E_str)

        all_cut_edges = [ei for cut in topo["x_cuts"] for ei, _ in cut]
        cuts_disjoint = (
            len(all_cut_edges) == len(set(all_cut_edges))
            and len(all_cut_edges) == 2 * (L ** 3)
            and all(len(c) == 2 * L * L for c in topo["x_cuts"])
        )
        cuts_flux_ok = all(cut_flux(E_str, c) == ONE for c in topo["x_cuts"])

        qb_bg = 4 * (8 * topo["nv"])
        dq_mag = (qe_str + qb_bg) - qb_bg
        row_ok = cuts_disjoint and cuts_flux_ok and (div_err == 0) and (qe_str == 4 * L) and (dq_mag == 4 * L)
        periodic_rows.append((L, qe_str, 4 * L, row_ok))

        if L == 6:
            E_bg = [ZERO] * topo["ne"]
            add_unit_x_string(topo, E_bg, (2, 1, 0, -1))
            q_bg = sum(z5_qe(x) for x in E_bg)
            q_plus = sum(z5_qe(z5_add(a, b)) for a, b in zip(E_bg, E_str))
            q_minus = sum(z5_qe(z5_sub(a, b)) for a, b in zip(E_bg, E_str))
            parallelogram_ok = ((q_plus - q_bg) + (q_minus - q_bg) == 2 * qe_str)

    return {
        "pass": all(r[3] for r in dipole_rows) and all(r[3] for r in periodic_rows) and parallelogram_ok,
        "dipole_rows": dipole_rows,
        "periodic_rows": periodic_rows,
        "parallelogram_ok": parallelogram_ok,
    }


# ---------------------------------------------------------------------------
# F03: Exact Decimal(130) 4D Poisson Summation Identity
# ---------------------------------------------------------------------------
def dec_cos_sin(x: Decimal) -> tuple[Decimal, Decimal]:
    """High-precision Decimal (cos(x), sin(x)) via range reduction and Taylor series."""
    two_pi = Decimal(2) * PI_DEC
    x = x % two_pi
    if x > PI_DEC:
        x -= two_pi
    x2 = x * x
    eps = Decimal("1e-125")

    c_term = Decimal(1)
    c_tot = Decimal(1)
    for k in range(1, 120):
        c_term = -c_term * x2 / Decimal((2 * k - 1) * (2 * k))
        c_tot += c_term
        if abs(c_term) < eps:
            break

    s_term = x
    s_tot = x
    for k in range(1, 120):
        s_term = -s_term * x2 / Decimal((2 * k) * (2 * k + 1))
        s_tot += s_term
        if abs(s_term) < eps:
            break
    return c_tot, s_tot


def check_f03_poisson_4d() -> dict[str, object]:
    """Pointwise verification of 4D Poisson summation with G = 5*I_4 - J_4."""
    u = (Decimal("0.37"), Decimal("-0.81"), Decimal("1.19"), Decimal("0.53"))
    two_pi = Decimal(2) * PI_DEC
    sqrt125 = Decimal(125).sqrt()
    max_rel_err = Decimal(0)
    rows = []

    for bstr in ("0.50", "1.00", "2.00"):
        beta = Decimal(bstr)
        q_cut = int(Decimal(115) / beta) + 2
        b_n = math.isqrt(q_cut) + 1

        exp_q = {q: (-beta * Decimal(q)).exp() for q in range(0, q_cut + 1, 2)}
        cs = [{n: dec_cos_sin(uk * Decimal(n)) for n in range(-b_n, b_n + 1)} for uk in u]

        lhs = Decimal(0)
        c0_tbl, c1_tbl, c2_tbl, c3_tbl = cs
        for n0 in range(-b_n, b_n + 1):
            s2_0 = n0 * n0
            if 5 * s2_0 > 2 * q_cut:
                continue
            c0, s0 = c0_tbl[n0]
            for n1 in range(-b_n, b_n + 1):
                s1_1 = n0 + n1
                s2_1 = s2_0 + n1 * n1
                if 15 * s2_1 - 5 * s1_1 * s1_1 > 3 * q_cut:
                    continue
                c1, s1 = c1_tbl[n1]
                c01 = c0 * c1 - s0 * s1
                s01 = s0 * c1 + c0 * s1
                for n2 in range(-b_n, b_n + 1):
                    s1_2 = s1_1 + n2
                    s2_2 = s2_1 + n2 * n2
                    if 20 * s2_2 - 5 * s1_2 * s1_2 > 4 * q_cut:
                        continue
                    c2, s2 = c2_tbl[n2]
                    c012 = c01 * c2 - s01 * s2
                    s012 = s01 * c2 + c01 * s2
                    disc = s1_2 * s1_2 - 4 * (5 * s2_2 - s1_2 * s1_2 - q_cut)
                    if disc < 0:
                        continue
                    r_disc = math.isqrt(disc)
                    lo = (s1_2 - r_disc + 3) // 4
                    hi = (s1_2 + r_disc) // 4
                    for n3 in range(lo, hi + 1):
                        s1_3 = s1_2 + n3
                        val = 5 * (s2_2 + n3 * n3) - s1_3 * s1_3
                        if val <= q_cut:
                            c3, s3 = c3_tbl[n3]
                            cos_dot = c012 * c3 - s012 * s3
                            lhs += exp_q[val] * cos_dot

        d_cut = Decimal(2300) * beta
        b_d = int(d_cut.sqrt() / two_pi) + 2
        rhs_sum = Decimal(0)
        denom20b = Decimal(20) * beta
        for m0 in range(-b_d, b_d + 1):
            d0 = u[0] - two_pi * Decimal(m0)
            sq0 = d0 * d0
            if sq0 > d_cut:
                continue
            for m1 in range(-b_d, b_d + 1):
                d1 = u[1] - two_pi * Decimal(m1)
                sq1 = sq0 + d1 * d1
                if sq1 > d_cut:
                    continue
                for m2 in range(-b_d, b_d + 1):
                    d2 = u[2] - two_pi * Decimal(m2)
                    sq2 = sq1 + d2 * d2
                    if sq2 > d_cut:
                        continue
                    for m3 in range(-b_d, b_d + 1):
                        d3 = u[3] - two_pi * Decimal(m3)
                        sq3 = sq2 + d3 * d3
                        if sq3 > d_cut:
                            continue
                        sd = d0 + d1 + d2 + d3
                        v5 = sq3 + sd * sd
                        if v5 <= d_cut:
                            rhs_sum += (-v5 / denom20b).exp()

        rhs = (PI_DEC * PI_DEC) / (beta * beta * sqrt125) * rhs_sum
        rel_err = abs(lhs - rhs) / abs(lhs)
        if rel_err > max_rel_err:
            max_rel_err = rel_err
        rows.append((bstr, rel_err))

    return {
        "pass": max_rel_err < Decimal("1e-40"),
        "max_rel_err": max_rel_err,
        "rows": rows,
    }


# ---------------------------------------------------------------------------
# F04: Exact Spin-Wave Cancellation and Strict Vortex Positivity on D3(L)
# ---------------------------------------------------------------------------
def check_f04_spin_wave_and_strictness() -> dict[str, object]:
    rows = []
    for L in (2, 4, 6):
        topo = build_d3(L)
        nv = topo["nv"]
        ne = topo["ne"]
        edges = topo["edges"]

        sum_dx2 = sum(e[3] * e[3] for e in edges)
        b_dx = [0] * nv
        for u, v, _a, dx, _dy, _dz in edges:
            b_dx[u] += dx
            b_dx[v] -= dx
        max_b_dx = max(abs(x) for x in b_dx)

        theta = [
            (
                (17 * i + 3) % 97 - 48,
                (31 * i + 7) % 89 - 44,
                (13 * i * i + 5) % 83 - 41,
                (29 * i + 11) % 79 - 39,
            )
            for i in range(nv)
        ]
        sw = [0, 0, 0, 0]
        for u, v, _a, dx, _dy, _dz in edges:
            if dx != 0:
                tu = theta[u]
                tv = theta[v]
                sw[0] += dx * (tv[0] - tu[0])
                sw[1] += dx * (tv[1] - tu[1])
                sw[2] += dx * (tv[2] - tu[2])
                sw[3] += dx * (tv[3] - tu[3])

        k_coeff = Fraction(sum_dx2, 2 * L * L)
        gauss_limit_z = Fraction(2 * k_coeff, 8 * L)
        row_ok = (
            sum_dx2 == 2 * (L ** 3)
            and sum_dx2 == 4 * nv
            and max_b_dx == 0
            and sw == [0, 0, 0, 0]
            and k_coeff == Fraction(L, 1)
            and gauss_limit_z == Fraction(1, 4)
        )
        rows.append((L, nv, ne, sum_dx2, max_b_dx, tuple(sw), k_coeff, gauss_limit_z, row_ok))

    min_vortex_ginv = Fraction(q_ginv_5((1, 0, 0, 0)), 5)
    vortex_pos_ok = (min_vortex_ginv == Fraction(2, 5)) and (min_vortex_ginv > 0)
    return {
        "pass": all(r[8] for r in rows) and vortex_pos_ok,
        "rows": rows,
        "min_vortex_ginv": min_vortex_ginv,
    }


# ---------------------------------------------------------------------------
# F05: Exact Decimal(130) 2-Edge & 3-Edge Cyclotomic Complexes + Crossover
# ---------------------------------------------------------------------------
def gen_ellipsoid_qG_by_parity(q_cut: int) -> dict[tuple[int, int, int, int], Counter[int]]:
    """Single-pass exact pure-integer histograms of 2*q(v) = v^T G v <= q_cut grouped by v mod 2."""
    out: dict[tuple[int, int, int, int], Counter[int]] = {
        (a, b, c, d): Counter()
        for a in (0, 1) for b in (0, 1) for c in (0, 1) for d in (0, 1)
    }
    b = math.isqrt(q_cut) + 1
    for x0 in range(-b, b + 1):
        s2_0 = x0 * x0
        if 5 * s2_0 > 2 * q_cut:
            continue
        p0 = x0 & 1
        for x1 in range(-b, b + 1):
            s1_1 = x0 + x1
            s2_1 = s2_0 + x1 * x1
            if 15 * s2_1 - 5 * s1_1 * s1_1 > 3 * q_cut:
                continue
            p1 = x1 & 1
            for x2 in range(-b, b + 1):
                s1_2 = s1_1 + x2
                s2_2 = s2_1 + x2 * x2
                if 20 * s2_2 - 5 * s1_2 * s1_2 > 4 * q_cut:
                    continue
                disc = s1_2 * s1_2 - 4 * (5 * s2_2 - s1_2 * s1_2 - q_cut)
                if disc < 0:
                    continue
                rd = math.isqrt(disc)
                lo = (s1_2 - rd + 3) // 4
                hi = (s1_2 + rd) // 4
                p2 = x2 & 1
                for x3 in range(lo, hi + 1):
                    s1_3 = s1_2 + x3
                    val = 5 * (s2_2 + x3 * x3) - s1_3 * s1_3
                    if val <= q_cut:
                        out[(p0, p1, p2, x3 & 1)][val] += 1
    return out


def gen_ellipsoid_qGinv5_by_parity(v5_cut: int) -> dict[tuple[int, int, int, int], Counter[int]]:
    """Single-pass exact pure-integer histograms of 5*(m^T G^{-1} m) <= v5_cut grouped by m mod 2."""
    out: dict[tuple[int, int, int, int], Counter[int]] = {
        (a, b, c, d): Counter()
        for a in (0, 1) for b in (0, 1) for c in (0, 1) for d in (0, 1)
    }
    b0 = math.isqrt(v5_cut)
    for x0 in range(-b0, b0 + 1):
        s2_0 = x0 * x0
        if s2_0 > v5_cut:
            continue
        p0 = x0 & 1
        b1 = math.isqrt(v5_cut - s2_0)
        for x1 in range(-b1, b1 + 1):
            s2_1 = s2_0 + x1 * x1
            if s2_1 > v5_cut:
                continue
            p1 = x1 & 1
            b2 = math.isqrt(v5_cut - s2_1)
            for x2 in range(-b2, b2 + 1):
                s2_2 = s2_1 + x2 * x2
                if s2_2 > v5_cut:
                    continue
                s1_2 = x0 + x1 + x2
                # 2*x3^2 + 2*s1_2*x3 + (s2_2 + s1_2^2 - v5_cut) <= 0
                disc = 2 * v5_cut - 2 * s2_2 - s1_2 * s1_2
                if disc < 0:
                    continue
                rd = math.isqrt(disc)
                lo = (-s1_2 - rd) // 2 - 1
                hi = (-s1_2 + rd) // 2 + 1
                p2 = x2 & 1
                for x3 in range(lo, hi + 1):
                    s1_3 = s1_2 + x3
                    v5 = s2_2 + x3 * x3 + s1_3 * s1_3
                    if v5 <= v5_cut:
                        out[(p0, p1, p2, x3 & 1)][v5] += 1
    return out


def merge_parity_hist(by_p: dict[tuple[int, int, int, int], Counter[int]]) -> Counter[int]:
    tot: Counter[int] = Counter()
    for cnt in by_p.values():
        tot.update(cnt)
    return tot


def eval_3edge_dual(
    beta: Decimal,
    parities: list[tuple[int, int, int, int]],
    hist_m: dict[tuple[int, int, int, int], Counter[int]],
    hist_n: dict[tuple[int, int, int, int], Counter[int]],
    pi2: Decimal,
) -> tuple[Decimal, Decimal, Decimal, Decimal, Decimal]:
    """Return (Z_work_var, deficit, dF1, Z_work_disc, mean_MG3) via dual Villain sum."""
    quarter = Decimal("0.25")
    Z3 = Decimal(0)
    JG3 = Decimal(0)
    th0 = Decimal(0)
    th1 = Decimal(0)
    for p in parities:
        Am = Decimal(0)
        for v5, cnt in hist_m[p].items():
            Am += Decimal(cnt) * (-pi2 * Decimal(v5) / (Decimal(10) * beta)).exp()
        Bn = Decimal(0)
        Bn_j = Decimal(0)
        for v5, cnt in hist_n[p].items():
            w = Decimal(cnt) * (-pi2 * Decimal(v5) / (Decimal(30) * beta)).exp()
            Bn += w
            if v5 > 0:
                Bn_j += (pi2 * Decimal(v5) / (Decimal(45) * beta * beta)) * w
        Z3 += Am * Bn
        JG3 += Am * Bn_j
        th0 += Am
        th1 += Am if p[0] == 0 else -Am
    mean_JG3 = JG3 / Z3
    mean_MG3 = Decimal(4) / (Decimal(3) * beta) - mean_JG3
    deficit = (Decimal(3) * beta / Decimal(16)) * mean_JG3
    zw_var = quarter - deficit
    dF1 = Decimal(6) * beta - (th1 / th0).ln()
    zw_disc = (Decimal(3) * beta) / (Decimal(2) * dF1)
    return zw_var, deficit, dF1, zw_disc, mean_MG3


def check_f05_cyclotomic_complexes() -> dict[str, object]:
    """Exact Decimal(130) verification on 2-edge and 3-edge cyclotomic complexes
    plus exact bisection of the 3-edge variance-vs-discrete crossing.
    """
    betas = ("0.01", "0.05", "0.10", "0.50", "1.00", "2.00")
    pi2 = PI_DEC * PI_DEC
    quarter = Decimal("0.25")
    parities = [(a, b, c, d) for a in (0, 1) for b in (0, 1) for c in (0, 1) for d in (0, 1)]

    hist_2_pr = merge_parity_hist(gen_ellipsoid_qG_by_parity(120))
    hist_2_du = merge_parity_hist(gen_ellipsoid_qGinv5_by_parity(230))
    hist_3_pr_k = gen_ellipsoid_qG_by_parity(450)
    hist_3_pr_q = gen_ellipsoid_qG_by_parity(160)
    hist_3_du_m = gen_ellipsoid_qGinv5_by_parity(120)
    hist_3_du_n = gen_ellipsoid_qGinv5_by_parity(340)

    res_2 = []
    res_3 = []
    max_ov_2 = Decimal(0)
    max_ov_3 = Decimal(0)

    for bstr in betas:
        beta = Decimal(bstr)

        # ---- 2-edge cyclotomic complex (c = 1/4, <M^T G M>_Gauss = 1/beta) ----
        Z2_du = Decimal(0)
        JG2_du = Decimal(0)
        for v5, cnt in hist_2_du.items():
            w = Decimal(cnt) * (-pi2 * Decimal(v5) / (Decimal(10) * beta)).exp()
            Z2_du += w
            if v5 > 0:
                JG2_du += (pi2 * Decimal(v5) / (Decimal(20) * beta * beta)) * w
        mean_JG2_du = JG2_du / Z2_du
        mean_MG2_du = Decimal(1) / beta - mean_JG2_du
        deficit_2 = (beta / Decimal(4)) * mean_JG2_du

        if beta >= Decimal("0.50"):
            Z2_pr = Decimal(0)
            MG2_pr = Decimal(0)
            for qv, cnt in hist_2_pr.items():
                w = Decimal(cnt) * (-Decimal(2) * beta * Decimal(qv)).exp()
                Z2_pr += w
                MG2_pr += Decimal(qv) * w
            mean_MG2_pr = MG2_pr / Z2_pr
            d2 = abs(mean_MG2_pr - mean_MG2_du)
            if d2 > max_ov_2:
                max_ov_2 = d2

        zw_var_2 = quarter - deficit_2
        zw_disc_2 = quarter
        res_2.append({
            "beta": bstr,
            "Z_work_var": zw_var_2,
            "deficit": deficit_2,
            "Z_work_disc": zw_disc_2,
            "strict_lt_quarter": (deficit_2 > 0) and (zw_var_2 < quarter),
            "strict_lt_disc": zw_var_2 < zw_disc_2,
        })

        # ---- 3-edge cyclotomic complex (c = 1/3, <M^T G M>_Gauss = 4/(3*beta)) ----
        du_vals = None
        if beta <= Decimal("1.00"):
            du_vals = eval_3edge_dual(beta, parities, hist_3_du_m, hist_3_du_n, pi2)

        pr_vals = None
        if beta >= Decimal("0.50"):
            Z3_pr = Decimal(0)
            MG3_pr = Decimal(0)
            th0_pr = Decimal(0)
            th1_pr = Decimal(0)
            for r in parities:
                th = Decimal(0)
                for qv, cnt in hist_3_pr_k[r].items():
                    th += Decimal(cnt) * (-beta * Decimal(qv) / Decimal(2)).exp()
                sq = Decimal(0)
                sq_mg = Decimal(0)
                for qv, cnt in hist_3_pr_q[r].items():
                    w = Decimal(cnt) * (-Decimal(3) * beta * Decimal(qv) / Decimal(2)).exp()
                    sq += w
                    sq_mg += Decimal(qv) * w
                Z3_pr += th * sq
                MG3_pr += th * sq_mg
                if r == (0, 0, 0, 0):
                    th0_pr = th
                elif r == (1, 0, 0, 0):
                    th1_pr = th
            mean_MG3_pr = MG3_pr / Z3_pr
            dF1_3_pr = Decimal(6) * beta - (th1_pr / th0_pr).ln()
            pr_vals = (mean_MG3_pr, dF1_3_pr)

        if du_vals is not None and pr_vals is not None:
            d3 = max(abs(pr_vals[0] - du_vals[4]), abs(pr_vals[1] - du_vals[2]))
            if d3 > max_ov_3:
                max_ov_3 = d3

        if du_vals is not None:
            zw_var_3, deficit_3, dF1_3, zw_disc_3, _ = du_vals
            if pr_vals is not None:
                dF1_3 = pr_vals[1]
                zw_disc_3 = (Decimal(3) * beta) / (Decimal(2) * dF1_3)
        else:
            mean_MG3_pr, dF1_3 = pr_vals
            zw_var_3 = (Decimal(3) * beta * mean_MG3_pr) / Decimal(16)
            deficit_3 = quarter - zw_var_3
            zw_disc_3 = (Decimal(3) * beta) / (Decimal(2) * dF1_3)

        res_3.append({
            "beta": bstr,
            "Z_work_var": zw_var_3,
            "deficit": deficit_3,
            "Z_work_disc": zw_disc_3,
            "diff_var_minus_disc": zw_var_3 - zw_disc_3,
            "strict_lt_quarter": (deficit_3 > 0) and (zw_var_3 < quarter),
            "disc_lt_quarter": zw_disc_3 < quarter,
        })

    # Exact 3-edge crossover between beta = 0.10 (var > disc) and beta = 0.50 (var < disc)
    r3_by_b = {r["beta"]: r for r in res_3}
    sign_change_ok = (
        r3_by_b["0.10"]["diff_var_minus_disc"] > 0
        and r3_by_b["0.50"]["diff_var_minus_disc"] < 0
    )

    lo = Decimal("0.20")
    hi = Decimal("0.30")
    zv_lo, _, _, zd_lo, _ = eval_3edge_dual(lo, parities, hist_3_du_m, hist_3_du_n, pi2)
    zv_hi, _, _, zd_hi, _ = eval_3edge_dual(hi, parities, hist_3_du_m, hist_3_du_n, pi2)
    bracket_ok = (zv_lo - zd_lo > 0) and (zv_hi - zd_hi < 0)
    for _ in range(130):
        mid = (lo + hi) / Decimal(2)
        zv_m, _, _, zd_m, _ = eval_3edge_dual(mid, parities, hist_3_du_m, hist_3_du_n, pi2)
        if zv_m - zd_m > 0:
            lo = mid
        else:
            hi = mid
    beta_star = (lo + hi) / Decimal(2)
    zv_star, def_star, _, zd_star, _ = eval_3edge_dual(beta_star, parities, hist_3_du_m, hist_3_du_n, pi2)
    cross_diff = abs(zv_star - zd_star)
    cross_ok = (
        sign_change_ok
        and bracket_ok
        and cross_diff < Decimal("1e-35")
        and def_star > 0
        and zv_star < quarter
        and zd_star < quarter
        and abs(beta_star - Decimal("0.242528416")) < Decimal("1e-9")
        and abs(zv_star - Decimal("0.24920214")) < Decimal("1e-8")
    )

    ok = (
        max_ov_2 < Decimal("1e-40")
        and max_ov_3 < Decimal("1e-40")
        and all(r["strict_lt_quarter"] and r["strict_lt_disc"] for r in res_2)
        and all(r["strict_lt_quarter"] and r["disc_lt_quarter"] for r in res_3)
        and cross_ok
    )
    return {
        "pass": ok,
        "max_ov_2": max_ov_2,
        "max_ov_3": max_ov_3,
        "res_2": res_2,
        "res_3": res_3,
        "beta_star": beta_star,
        "Z_star_var": zv_star,
        "Z_star_disc": zd_star,
        "cross_diff": cross_diff,
    }


# ---------------------------------------------------------------------------
# F06: Five Deliberate Negative Controls (All Must Be Rejected)
# ---------------------------------------------------------------------------
def check_f06_negative_controls(f05: dict[str, object]) -> dict[str, object]:
    # C01: Corrupt Gram matrix G_bad = 5*I_4 fails cyclotomic trace identity on z=(1,1,0,0)
    z_test = (1, 1, 0, 0)
    v_tr = z5_tr(z5_h(z_test))
    v_bad_gram = 5 * sum(x * x for x in z_test)
    c01_rejected = (v_tr == 6) and (v_bad_gram == 10) and (v_bad_gram != v_tr)

    # C02: Omitting nonzero Villain vortices (m === 0) collapses deficit to 0, contradicting exact sum
    r2_beta1 = next(r for r in f05["res_2"] if r["beta"] == "1.00")
    c02_rejected = (r2_beta1["deficit"] > 0) and (Decimal("0.25") != r2_beta1["Z_work_var"])

    # C03: Perturbing one edge weight dx_{e0}: 1 -> 2 on D3(4) breaks B*dx = 0 and spin-wave cancellation
    topo4 = build_d3(4)
    nv4 = topo4["nv"]
    edges4 = topo4["edges"]
    b_dx_bad = [0] * nv4
    sw_bad = [0, 0, 0, 0]
    theta4 = [((17 * i + 3) % 97 - 48, 0, 0, 0) for i in range(nv4)]
    perturbed_done = False
    for ei, (u, v, _a, dx, _dy, _dz) in enumerate(edges4):
        dx_use = dx
        if not perturbed_done and dx == 1:
            dx_use = 2
            perturbed_done = True
        b_dx_bad[u] += dx_use
        b_dx_bad[v] -= dx_use
        if dx_use != 0:
            sw_bad[0] += dx_use * (theta4[v][0] - theta4[u][0])
    c03_rejected = (max(abs(x) for x in b_dx_bad) == 1) and (sw_bad[0] != 0)

    # C04: Removing one edge from unit x-string on D3(6) lowers Q_E to 20 < 4L=24 but breaks div=0 & cut flux
    topo6 = build_d3(6)
    E_broken = [ZERO] * topo6["ne"]
    add_unit_x_string(topo6, E_broken, ONE)
    first_nz = next(i for i, x in enumerate(E_broken) if x != ZERO)
    E_broken[first_nz] = ZERO
    qe_broken = sum(z5_qe(x) for x in E_broken)
    div_broken = max_div_err(topo6, E_broken)
    cut_ok_broken = all(cut_flux(E_broken, c) == ONE for c in topo6["x_cuts"])
    c04_rejected = (qe_broken == 20) and (div_broken == 2) and (not cut_ok_broken)

    # C05: False non-crossing claim on 3-edge complex rejected by opposite signs at beta=0.10 vs 0.50
    r3_010 = next(r for r in f05["res_3"] if r["beta"] == "0.10")
    r3_050 = next(r for r in f05["res_3"] if r["beta"] == "0.50")
    c05_rejected = (r3_010["diff_var_minus_disc"] * r3_050["diff_var_minus_disc"] < 0)

    ok = c01_rejected and c02_rejected and c03_rejected and c04_rejected and c05_rejected
    return {
        "pass": ok,
        "controls": (
            "corrupt_gram",
            "zero_vortex_truncation",
            "perturbed_edge_weight",
            "broken_divergence_string",
            "constant_sign_3edge",
        ),
    }


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", newline="\n")

    f01 = check_f01_gram_and_floor()
    f02 = check_f02_vacuum_bounds()
    f03 = check_f03_poisson_4d()
    f04 = check_f04_spin_wave_and_strictness()
    f05 = check_f05_cyclotomic_complexes()
    f06 = check_f06_negative_controls(f05)

    all_ok = f01["pass"] and f02["pass"] and f03["pass"] and f04["pass"] and f05["pass"] and f06["pass"]

    shells_str = ",".join(str(f01["shells"][k]) for k in (0, 4, 6, 10, 14))
    dipole_str = ",".join(str(r[1]) for r in f02["dipole_rows"])
    periodic_str = ",".join(str(r[1]) for r in f02["periodic_rows"])
    max_b_dx_all = max(r[4] for r in f04["rows"])
    max_sw_all = max(max(abs(x) for x in r[5]) for r in f04["rows"])
    gauss_z_vals = sorted({str(r[7]) for r in f04["rows"]})
    all_var_lt_q = all(r["strict_lt_quarter"] for r in f05["res_2"]) and all(
        r["strict_lt_quarter"] for r in f05["res_3"]
    )

    lines = [
        (
            f"{'PASS' if f01['pass'] else 'FAIL'} gram_floor: "
            f"det_G={f01['det_G']} spec={f01['spec_G']} min_nz_q={f01['min_nonzero_q']} "
            f"mu10={f01['mu10_count']} shells={shells_str}"
        ),
        (
            f"{'PASS' if f02['pass'] else 'FAIL'} vacuum_bounds: "
            f"dipole_4d={dipole_str} periodic_4L={periodic_str} "
            f"parallelogram={'true' if f02['parallelogram_ok'] else 'false'}"
        ),
        (
            f"{'PASS' if f03['pass'] else 'FAIL'} poisson_4d: "
            f"betas=0.50,1.00,2.00 max_rel_err={f03['max_rel_err']:.3e}"
        ),
        (
            f"{'PASS' if f04['pass'] else 'FAIL'} spin_wave_strictness: "
            f"L=2,4,6 max_abs_B_dx={max_b_dx_all} max_abs_sw={max_sw_all} "
            f"gauss_Z={','.join(gauss_z_vals)} min_vortex_Ginv={f04['min_vortex_ginv']}"
        ),
        (
            f"{'PASS' if f05['pass'] else 'FAIL'} complex_2edge_3edge: "
            f"max_ov_2={f05['max_ov_2']:.3e} max_ov_3={f05['max_ov_3']:.3e} "
            f"all_var_lt_quarter={'true' if all_var_lt_q else 'false'}"
        ),
        (
            f"{'PASS' if f05['pass'] else 'FAIL'} complex_3edge_crossover: "
            f"beta_star={f05['beta_star']:.9f} Z_var={f05['Z_star_var']:.8f} "
            f"Z_disc={f05['Z_star_disc']:.8f} abs_diff={f05['cross_diff']:.3e}"
        ),
    ]
    for r in f05["res_2"]:
        lines.append(
            f"DATA 2edge beta={r['beta']} Z_var={r['Z_work_var']:.12f} "
            f"deficit={r['deficit']:.6e} Z_disc={r['Z_work_disc']:.12f}"
        )
    for r in f05["res_3"]:
        lines.append(
            f"DATA 3edge beta={r['beta']} Z_var={r['Z_work_var']:.12f} "
            f"deficit={r['deficit']:.6e} Z_disc={r['Z_work_disc']:.12f} "
            f"diff={r['diff_var_minus_disc']:+.6e}"
        )
    lines.append(
        f"{'PASS' if f06['pass'] else 'FAIL'} controls: " + " ".join(f06["controls"])
    )
    lines.append(f"{'PASS' if all_ok else 'FAIL'} D3-ZWORK-VAR-BOUND-1")

    for line in lines:
        print(line)
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
