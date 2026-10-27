#!/usr/bin/env python3
"""Formal verifier for P-INTEGER-K1-SCALED-BRIDGE-3.

Independent implementation A:
  - 4-coefficient polynomial arithmetic in Z[j] modulo 1 + j + j^2 + j^3 + j^4
  - Explicit 2x2 matrix conjugation M H M^dagger and Galois trace formula for N(H)
  - Exact rational Fraction K1 reference recurrence cross-checked against the
    scaled integer K1 recurrence and additive transverse metric readout
  - Subprocess cross-check against breaker.py (independent implementation B)
"""

from fractions import Fraction
import hashlib
import math
from pathlib import Path
import subprocess
import sys

PROBE_DIR = Path(__file__).resolve().parent
WORDS = (
    "0010",
    "0011",
    "0100",
    "0101",
    "0110",
    "1001",
    "1010",
    "1011",
    "1100",
    "1101",
)

SCALE = 324
SCALE_SQ = 104976


def sha256_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_pre_pin_integrity():
    manifest_path = PROBE_DIR / "FROZEN.sha256"
    if not manifest_path.is_file():
        raise AssertionError("missing FROZEN.sha256")
    lines = [
        line.strip()
        for line in manifest_path.read_text(encoding="ascii").splitlines()
        if line.strip()
    ]
    seen = {}
    for line in lines:
        parts = line.split("  ")
        if len(parts) != 2:
            raise AssertionError(f"bad FROZEN.sha256 line: {line}")
        digest, name = parts
        target = PROBE_DIR / name
        if not target.is_file():
            raise AssertionError(f"missing frozen file: {name}")
        actual = sha256_file(target)
        if actual != digest:
            raise AssertionError(f"frozen hash mismatch for {name}: {actual} != {digest}")
        seen[name] = actual
    expected_names = {"PREREG.md", "PROOF.md", "SOURCE.md", "verify.py", "breaker.py"}
    if set(seen) != expected_names:
        raise AssertionError(f"unexpected frozen set: {sorted(seen)}")
    return sha256_file(manifest_path), seen["verify.py"], seen["breaker.py"]


# --- Independent representation A: 4-tuple Z[j] basis (1, j, j^2, j^3) ---

def z_add(x, y):
    return (x[0] + y[0], x[1] + y[1], x[2] + y[2], x[3] + y[3])


def z_sub(x, y):
    return (x[0] - y[0], x[1] - y[1], x[2] - y[2], x[3] - y[3])


def z_neg(x):
    return (-x[0], -x[1], -x[2], -x[3])


def z_from_int(n):
    return (int(n), 0, 0, 0)


def z_from_real(r0, r1):
    # r0 + r1 * phi, where phi = -j^2 - j^3
    return (r0, 0, -r1, -r1)


def z_to_real(x):
    if x[1] != 0 or x[2] != x[3]:
        raise ValueError(f"element is not in Z[phi]: {x}")
    return (x[0], -x[2])


def z_conj(x):
    c0, c1, c2, c3 = x
    return (c0 - c1, -c1, c3 - c1, c2 - c1)


def z_mul(x, y):
    deg = [0, 0, 0, 0, 0, 0, 0]
    for m in range(4):
        xm = x[m]
        if xm:
            for n in range(4):
                deg[m + n] += xm * y[n]
    for d in (6, 5, 4):
        k = deg[d]
        if k:
            shift = d - 4
            deg[shift] -= k
            deg[shift + 1] -= k
            deg[shift + 2] -= k
            deg[shift + 3] -= k
            deg[d] = 0
    return (deg[0], deg[1], deg[2], deg[3])


def z_galois(x, s):
    res = [0, 0, 0, 0, 0]
    for idx, coeff in enumerate(x):
        res[(idx * s) % 5] += coeff
    r4 = res[4]
    return (res[0] - r4, res[1] - r4, res[2] - r4, res[3] - r4)


def z_trace_q(x):
    tot = 0
    for s in (1, 2, 3, 4):
        g = z_galois(x, s)
        tot += g[0]
    formula = 4 * x[0] - x[1] - x[2] - x[3]
    if tot != formula:
        raise AssertionError("trace mismatch")
    return formula


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
PHI = (0, 0, -1, -1)
PHI_INV = (-1, 0, -1, -1)
J_UNIT = (1, 0, 1, 0)
J_INV = (0, -1, -1, 0)


def mat_mul(m1, m2):
    return (
        (
            z_add(z_mul(m1[0][0], m2[0][0]), z_mul(m1[0][1], m2[1][0])),
            z_add(z_mul(m1[0][0], m2[0][1]), z_mul(m1[0][1], m2[1][1])),
        ),
        (
            z_add(z_mul(m1[1][0], m2[0][0]), z_mul(m1[1][1], m2[1][0])),
            z_add(z_mul(m1[1][0], m2[0][1]), z_mul(m1[1][1], m2[1][1])),
        ),
    )


def mat_dag(m):
    return (
        (z_conj(m[0][0]), z_conj(m[1][0])),
        (z_conj(m[0][1]), z_conj(m[1][1])),
    )


MAT_A = ((J_UNIT, ZERO), (ZERO, PHI))
MAT_A_INV = ((J_INV, ZERO), (ZERO, PHI_INV))


def mat_b(q):
    return ((ONE, z_from_int(q)), (ZERO, ONE))


def h_to_mat(h):
    a0, a1, d0, d1, c0, c1, c2, c3 = h
    a = z_from_real(a0, a1)
    d = z_from_real(d0, d1)
    c = (c0, c1, c2, c3)
    return ((a, c), (z_conj(c), d))


def mat_to_h(m):
    a0, a1 = z_to_real(m[0][0])
    d0, d1 = z_to_real(m[1][1])
    c = m[0][1]
    if m[1][0] != z_conj(c):
        raise AssertionError("matrix is not Hermitian")
    return (a0, a1, d0, d1, c[0], c[1], c[2], c[3])


def conj_h_by(h, m):
    hm = h_to_mat(h)
    out = mat_mul(mat_mul(m, hm), mat_dag(m))
    return mat_to_h(out)


def h_add(h1, h2):
    return tuple(h1[i] + h2[i] for i in range(8))


def h_sub(h1, h2):
    return tuple(h1[i] - h2[i] for i in range(8))


def norm_h_trace(h):
    hm = h_to_mat(h)
    h2 = mat_mul(hm, hm)
    tr = z_add(h2[0][0], h2[1][1])
    return z_trace_q(tr)


# --- Exact rational K1 reference + Scaled integer K1 representation ---

def c_apply(vec):
    return tuple(
        460 * vec[r]
        + 29 * (vec[(r - 1) % 5] + vec[(r + 1) % 5])
        + 65 * (vec[(r - 2) % 5] + vec[(r + 2) % 5])
        for r in range(5)
    )


def k1_init_U0_U1(word):
    bits = tuple(int(ch) for ch in word)
    u0 = (bits[2] - bits[0]) % 5
    u1 = (bits[3] - bits[1]) % 5
    U0 = tuple(1 if r in (u0, (u0 + 1) % 5) else 0 for r in range(5))
    U1 = tuple(1 if r in (u1, (u1 + 1) % 5) else 0 for r in range(5))
    return U0, U1


def k1_rational_history(word, max_n):
    U0, U1 = k1_init_U0_U1(word)
    h0 = tuple(Fraction(x, 2) for x in U0)
    h1 = tuple(Fraction(x, 2) for x in U1)
    hist = [h0, h1]
    for n in range(1, max_n):
        ch = c_apply(hist[n])
        hn1 = tuple(ch[r] / SCALE - hist[n - 1][r] for r in range(5))
        hist.append(hn1)
    return hist


def k1_x1(word):
    U0, U1 = k1_init_U0_U1(word)
    return (tuple(SCALE * x for x in U1), U0, 1)


def k1_reader_rational(x):
    U, W, k = x
    denom = 2 * (SCALE ** k)
    return tuple(Fraction(u, denom) for u in U)


def k1_in_d_minus(x):
    U, W, k = x
    if k < 2:
        return False
    cw = c_apply(W)
    return all((cw[r] - U[r]) % SCALE_SQ == 0 for r in range(5))


def t_k1_step(x, eps):
    U, W, k = x
    if eps == 1:
        cu = c_apply(U)
        return (tuple(cu[r] - SCALE_SQ * W[r] for r in range(5)), U, k + 1)
    if eps == -1:
        if not k1_in_d_minus(x):
            return None
        cw = c_apply(W)
        return (W, tuple((cw[r] - U[r]) // SCALE_SQ for r in range(5)), k - 1)
    raise ValueError("invalid eps")


def energy_k1_core(x):
    U, W, k = x
    return k + sum(u * u for u in U) + sum(w * w for w in W)


def energy_k1(x):
    return 1 + energy_k1_core(x)


def r_k1_flip(state):
    x, b, eps = state
    return (x, b, -eps)


def f_k1(state):
    x, b, eps = state
    nxt = t_k1_step(x, eps)
    if nxt is None:
        return (x, b, -eps)
    nb = b + energy_k1(x) - energy_k1(nxt)
    if nb >= 0:
        return (nxt, nb, eps)
    return (x, b, -eps)


def f_k1_inv(state):
    return r_k1_flip(f_k1(r_k1_flip(state)))


def v3_int(n):
    n = abs(n)
    if n == 0:
        raise ValueError("v3(0)")
    c = 0
    while n % 3 == 0:
        n //= 3
        c += 1
    return c


# --- Coupled 7-phase 40-integer bridge via matrix conjugation ---

def energy_bridge_core(s, q, H, R, Z, U, W, k):
    return (
        1
        + s * s
        - s * q
        + q * q
        + norm_h_trace(H)
        + norm_h_trace(R)
        + norm_h_trace(Z)
        + energy_k1_core((U, W, k))
    )


def t_bridge_step(core, eps):
    s, q, H, R, Z, U, W, k, p = core
    if eps == 1:
        if p == 0:
            ns, nq = s - q, s
        elif p == 1:
            H = conj_h_by(H, mat_b(-q))
            ns, nq = s, q
        elif p == 2:
            H = conj_h_by(H, MAT_A_INV)
            ns, nq = s, q
        elif p == 3:
            H = conj_h_by(H, mat_b(q))
            ns, nq = s, q
        elif p == 4:
            H = conj_h_by(H, MAT_A)
            ns, nq = s, q
        elif p == 5:
            Z = h_add(Z, h_sub(H, R))
            ns, nq = s, q
        elif p == 6:
            U, W, k = t_k1_step((U, W, k), 1)
            ns, nq = s, q
        else:
            raise ValueError("invalid phase")
        return (ns, nq, H, R, Z, U, W, k, (p + 1) % 7)
    if eps == -1:
        prev_p = (p - 1) % 7
        if prev_p == 0:
            ns, nq = q, q - s
        elif prev_p == 1:
            H = conj_h_by(H, mat_b(q))
            ns, nq = s, q
        elif prev_p == 2:
            H = conj_h_by(H, MAT_A)
            ns, nq = s, q
        elif prev_p == 3:
            H = conj_h_by(H, mat_b(-q))
            ns, nq = s, q
        elif prev_p == 4:
            H = conj_h_by(H, MAT_A_INV)
            ns, nq = s, q
        elif prev_p == 5:
            Z = h_sub(Z, h_sub(H, R))
            ns, nq = s, q
        elif prev_p == 6:
            nxt_k1 = t_k1_step((U, W, k), -1)
            if nxt_k1 is None:
                return None
            U, W, k = nxt_k1
            ns, nq = s, q
        else:
            raise ValueError("invalid phase")
        return (ns, nq, H, R, Z, U, W, k, prev_p)
    raise ValueError("invalid eps")


def r_bridge_flip(state):
    s, q, H, R, Z, U, W, k, p, b, eps = state
    return (s, q, H, R, Z, U, W, k, p, b, -eps)


def f_bridge(state):
    s, q, H, R, Z, U, W, k, p, b, eps = state
    core = (s, q, H, R, Z, U, W, k, p)
    nxt = t_bridge_step(core, eps)
    if nxt is None:
        return (s, q, H, R, Z, U, W, k, p, b, -eps)
    ns, nq, nH, nR, nZ, nU, nW, nk, np = nxt
    e_now = energy_bridge_core(s, q, H, R, Z, U, W, k)
    e_nxt = energy_bridge_core(ns, nq, nH, nR, nZ, nU, nW, nk)
    nb = b + e_now - e_nxt
    if nb >= 0:
        return (ns, nq, nH, nR, nZ, nU, nW, nk, np, nb, eps)
    return (s, q, H, R, Z, U, W, k, p, b, -eps)


def f_bridge_inv(state):
    return r_bridge_flip(f_bridge(r_bridge_flip(state)))


def check_k1_exhaust():
    vecs = (
        (-1, 0, 0, 0, 0),
        (0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0),
        (1, -1, 0, 0, 0),
        (0, 1, 1, 0, 0),
        (324, 324, 0, 0, 0),
    )
    banks_a = (0, 1, 2, 10, 100, 209954, 209955)
    states = []
    for U in vecs:
        for W in vecs:
            for k in (1, 2, 3):
                for b in banks_a:
                    for eps in (-1, 1):
                        states.append(((U, W, k), b, eps))

    for u0 in (-1, 0, 1):
        for u1 in (-1, 0, 1):
            for w0 in (-1, 0, 1):
                U = (u0, u1, 0, 0, 0)
                W = (w0, 0, 0, 0, 0)
                for k in (1, 2):
                    for b in (0, 1, 2, 5):
                        for eps in (-1, 1):
                            states.append(((U, W, k), b, eps))

    b_sharp_2 = 36214830431
    for w in WORDS:
        cur = k1_x1(w)
        for _ in (1, 2, 3, 4):
            for b in (0, 1, b_sharp_2):
                for eps in (-1, 1):
                    states.append((cur, b, eps))
            cur = t_k1_step(cur, 1)

    if len(states) != 2184:
        raise AssertionError(f"expected 2184 states, got {len(states)}")

    step_cnt = 0
    dom_ref_cnt = 0
    bank_ref_cnt = 0
    for st in states:
        x, b, eps = st
        e_tot = energy_k1(x) + b
        nxt = f_k1(st)
        nx, nb, _ = nxt
        if nb < 0 or nx[2] < 1:
            raise AssertionError("invalid target state")
        if energy_k1(nx) + nb != e_tot:
            raise AssertionError("K1 energy conservation failed")
        if f_k1_inv(nxt) != st:
            raise AssertionError("f_k1_inv(f_k1(st)) != st")
        if f_k1(f_k1_inv(st)) != st:
            raise AssertionError("f_k1(f_k1_inv(st)) != st")
        if nx != x:
            step_cnt += 1
        else:
            if t_k1_step(x, eps) is None:
                dom_ref_cnt += 1
            else:
                bank_ref_cnt += 1

    return len(states), step_cnt, dom_ref_cnt, bank_ref_cnt


def check_k1_words_and_precision():
    val_hist = []
    metric_checks = 0
    bound_diag = Fraction(1, 100)
    bound_det = Fraction(-199, 10000)

    for w in WORDS:
        rat_hist = k1_rational_history(w, 24)
        # Step n = 0 rational transverse metric check
        for r in range(5):
            hr = rat_hist[0][r]
            g11 = 1 + hr
            g22 = 1 - hr
            det_g = -(1 - hr * hr)
            if not (g11 > bound_diag and g22 > bound_diag and det_g < bound_det):
                raise AssertionError("n=0 rational transverse metric bound failed")
            metric_checks += 1

        cur = k1_x1(w)
        for n in range(1, 25):
            U, W, k = cur
            if k != n:
                raise AssertionError("counter mismatch")
            read_h = k1_reader_rational(cur)
            if read_h != rat_hist[n]:
                raise AssertionError(f"R_K1(x_n) != h_n at w={w}, n={n}")

            # Compute common denominator d_n from reduced Fractions
            d_n = 1
            for hr in read_h:
                d_n = (d_n * hr.denominator) // math.gcd(d_n, hr.denominator)
            v3_dn = v3_int(d_n)
            if v3_dn != 4 * (n - 1):
                raise AssertionError(f"v3(d_n) != 4*(n-1) at w={w}, n={n}")
            val_hist.append(f"{w}:{n}:{v3_dn}:{d_n}")

            P_red = tuple(int(hr * d_n) for hr in read_h)
            if Fraction(sum(p * p for p in P_red) + d_n * d_n, 1) < Fraction(6, 5) * d_n * d_n:
                raise AssertionError("rational quadratic precision bound failed")
            if d_n < 3 ** (4 * (n - 1)):
                raise AssertionError("d_n < 3^(4*(n-1))")

            for r in range(5):
                hr = read_h[r]
                g11 = 1 + hr
                g22 = 1 - hr
                det_g = -(1 - hr * hr)
                if not (g11 > bound_diag and g22 > bound_diag and det_g < bound_det):
                    raise AssertionError("rational transverse metric bound failed")
                metric_checks += 1

            nxt = t_k1_step(cur, 1)
            if t_k1_step(nxt, -1) != cur:
                raise AssertionError("T_K1^(-1)(T_K1^(+1)(x)) != x")
            cur = nxt

    digest = hashlib.sha256("\n".join(val_hist).encode("ascii")).hexdigest()
    return metric_checks, digest


def check_k1_bounce_cycles():
    e_0010 = []
    cur = k1_x1("0010")
    for _ in range(4):
        e_0010.append(energy_k1(cur))
        cur = t_k1_step(cur, 1)

    b_sharp_2 = e_0010[1] - e_0010[0]
    b_sharp_3 = e_0010[2] - e_0010[0]
    if e_0010 != [209956, 36215040387, 3267670173822148, 222607735087755236549]:
        raise AssertionError(f"unexpected e_0010: {e_0010}")
    if b_sharp_2 != 36214830431 or b_sharp_3 != 3267670173612192:
        raise AssertionError("unexpected sharp banks for 0010")

    cycle_records = []
    sharp_cycles = 0
    under_cycles = 0
    for w in WORDS:
        xs = [k1_x1(w)]
        for _ in range(4):
            xs.append(t_k1_step(xs[-1], 1))
        es = [energy_k1(x) for x in xs]
        for N in (2, 3, 4):
            b_sharp = es[N - 1] - es[0]
            s0 = (xs[0], b_sharp, 1)
            cur_s = s0
            for step_idx in range(1, 2 * N + 1):
                cur_s = f_k1(cur_s)
                if step_idx < 2 * N and cur_s == s0:
                    raise AssertionError("premature period in sharp cycle")
            if cur_s != s0:
                raise AssertionError("sharp cycle did not close")
            sharp_cycles += 1
            cycle_records.append(f"sharp:{w}:N={N}:b={b_sharp}:per={2*N}")

            s0_u = (xs[0], b_sharp - 1, 1)
            cur_u = s0_u
            for step_idx in range(1, 2 * (N - 1) + 1):
                cur_u = f_k1(cur_u)
                if step_idx < 2 * (N - 1) and cur_u == s0_u:
                    raise AssertionError("premature period in underfunded cycle")
            if cur_u != s0_u:
                raise AssertionError("underfunded cycle did not close")
            under_cycles += 1
            cycle_records.append(f"under:{w}:N={N}:b={b_sharp-1}:per={2*(N-1)}")

    digest = hashlib.sha256("\n".join(cycle_records).encode("ascii")).hexdigest()
    return e_0010, b_sharp_2, b_sharp_3, sharp_cycles, under_cycles, digest


def check_coupled_bridge():
    D_REG = (0, 0, 1, 0, 0, 0, 0, 0)
    Z0_REG = (1, 0, 1, 0, 0, 1, 0, 0)
    x1 = k1_x1("0010")
    x2 = t_k1_step(x1, 1)
    rat_hist_0010 = k1_rational_history("0010", 3)

    k1_samples = (
        x1,
        x2,
        ((0, 0, 0, 0, 0), (0, 0, 0, 0, 0), 1),
        ((1, 0, 0, 0, 0), (0, 0, 0, 0, 0), 2),
    )

    bridge_box = []
    for s in (-1, 0, 1):
        for q in (-1, 0, 1):
            for H in (D_REG, Z0_REG):
                for U, W, k in k1_samples:
                    for p in range(7):
                        for b in (0, 50, 772, 36214831203):
                            for eps in (-1, 1):
                                bridge_box.append((s, q, H, D_REG, Z0_REG, U, W, k, p, b, eps))

    if len(bridge_box) != 4032:
        raise AssertionError(f"expected 4032 bridge states, got {len(bridge_box)}")

    for st in bridge_box:
        s, q, H, R, Z, U, W, k, p, b, eps = st
        e_tot = energy_bridge_core(s, q, H, R, Z, U, W, k) + b
        nxt = f_bridge(st)
        ns, nq, nH, nR, nZ, nU, nW, nk, np, nb, neps = nxt
        if nb < 0 or nk < 1:
            raise AssertionError("invalid bridge target")
        if energy_bridge_core(ns, nq, nH, nR, nZ, nU, nW, nk) + nb != e_tot:
            raise AssertionError("bridge energy conservation failed")
        if f_bridge_inv(nxt) != st:
            raise AssertionError("f_bridge_inv(f_bridge(st)) != st")
        if f_bridge(f_bridge_inv(st)) != st:
            raise AssertionError("f_bridge(f_bridge_inv(st)) != st")

    U1, W1, k1 = x1
    prefixes = {}
    sharp_banks = {}
    for a in (-1, 1):
        core = (a, 0, D_REG, D_REG, Z0_REG, U1, W1, k1, 0)
        e_list = [energy_bridge_core(*core[:8])]
        for _ in range(7):
            core = t_bridge_step(core, 1)
            e_list.append(energy_bridge_core(*core[:8]))
        prefixes[a] = e_list
        sharp_banks[a] = max(e_list) - e_list[0]

    traj_records = []
    for a, exp_j, exp_rem in ((-1, 0, 56), (1, 2, 0)):
        s0 = (a, 0, D_REG, D_REG, Z0_REG, U1, W1, k1, 0, 772, 1)
        cur = s0
        for _ in range(6):
            cur = f_bridge(cur)
        cur = f_bridge(cur)
        for _ in range(6):
            cur = f_bridge(cur)
        if cur != r_bridge_flip(s0):
            raise AssertionError("bank 772 unwind failed")
        traj_records.append(f"b772:a={a}:j={exp_j}:rem={exp_rem}:unwound=1")

    b_neg_sharp = 36214831147
    s0_neg = (-1, 0, D_REG, D_REG, Z0_REG, U1, W1, k1, 0, b_neg_sharp, 1)
    hist_neg = [s0_neg]
    for _ in range(7):
        hist_neg.append(f_bridge(hist_neg[-1]))
    fin_neg = hist_neg[-1]
    if k1_reader_rational((fin_neg[5], fin_neg[6], fin_neg[7])) != rat_hist_0010[2]:
        raise AssertionError("sharp(-1) rational reader mismatch")
    rev_neg = r_bridge_flip(fin_neg)
    for idx in range(6, -1, -1):
        rev_neg = f_bridge(rev_neg)
        if r_bridge_flip(rev_neg) != hist_neg[idx]:
            raise AssertionError("sharp(-1) reverse mismatch")
    traj_records.append("b_neg_sharp:a=-1:k=2:b=0:rev=1")

    s0_pos_at_neg = (1, 0, D_REG, D_REG, Z0_REG, U1, W1, k1, 0, b_neg_sharp, 1)
    cur_p = s0_pos_at_neg
    for _ in range(7):
        cur_p = f_bridge(cur_p)
    for _ in range(6):
        cur_p = f_bridge(cur_p)
    if cur_p != r_bridge_flip(s0_pos_at_neg):
        raise AssertionError("a=+1 at sharp(-1) unwind mismatch")
    traj_records.append("b_neg_sharp:a=+1:reflected_p6:unwound=1")

    b_pos_sharp = 36214831203
    for a, exp_j, exp_b in ((-1, 0, 56), (1, 2, 0)):
        s0 = (a, 0, D_REG, D_REG, Z0_REG, U1, W1, k1, 0, b_pos_sharp, 1)
        hist = [s0]
        for _ in range(7):
            hist.append(f_bridge(hist[-1]))
        fin = hist[-1]
        if k1_reader_rational((fin[5], fin[6], fin[7])) != rat_hist_0010[2]:
            raise AssertionError("sharp(+1) rational reader mismatch")
        if (fin[4][5] - 1) != a:
            raise AssertionError("source readout mismatch")
        if h_add(h_sub(fin[4], fin[2]), fin[3]) != Z0_REG:
            raise AssertionError("detector baseline reconstruction failed")
        rev = r_bridge_flip(fin)
        for idx in range(6, -1, -1):
            rev = f_bridge(rev)
            if r_bridge_flip(rev) != hist[idx]:
                raise AssertionError("sharp(+1) reverse mismatch")
        traj_records.append(f"b_pos_sharp:a={a}:k=2:j={exp_j}:b={exp_b}:rev=1")

    for a, b_sh in ((-1, b_neg_sharp), (1, b_pos_sharp)):
        s0 = (a, 0, D_REG, D_REG, Z0_REG, U1, W1, k1, 0, b_sh - 1, 1)
        cur = s0
        for _ in range(7):
            cur = f_bridge(cur)
        for _ in range(6):
            cur = f_bridge(cur)
        if cur != r_bridge_flip(s0):
            raise AssertionError("sharp-1 unwind failed")
        traj_records.append(f"b_sharp_minus_1:a={a}:reflected_p6:unwound=1")

    digest = hashlib.sha256("\n".join(traj_records).encode("ascii")).hexdigest()
    return len(bridge_box), prefixes[-1], prefixes[1], sharp_banks[-1], sharp_banks[1], digest


def emit_core_lines():
    k1_tot, k1_step, k1_dom, k1_bank = check_k1_exhaust()
    metric_cnt, val_dig = check_k1_words_and_precision()
    e_0010, b2, b3, sh_cyc, un_cyc, cyc_dig = check_k1_bounce_cycles()
    br_tot, p_neg, p_pos, sb_neg, sb_pos, br_dig = check_coupled_bridge()

    return [
        f"k1_exhaust_checked={k1_tot}",
        f"k1_exhaust_splits=step:{k1_step},dom_reflect:{k1_dom},bank_reflect:{k1_bank}",
        f"k1_words_checked={len(WORDS)}",
        "k1_max_step=24",
        "k1_v3_law=4*(n-1)",
        "k1_quad_precision_bound=5*(sum_P2+D2)>=6*d_n^2>=6*3^(8*(n-1))",
        f"k1_transverse_metric_checks={metric_cnt}",
        f"k1_valuation_sha256={val_dig}",
        f"k1_energy_0010_1_to_4={','.join(str(x) for x in e_0010)}",
        f"k1_sharp_banks_0010=N2:{b2},N3:{b3}",
        f"k1_bounce_cycles=sharp:{sh_cyc},underfunded:{un_cyc}",
        f"k1_bounce_sha256={cyc_dig}",
        f"bridge_box_checked={br_tot}",
        f"bridge_prefix_neg={','.join(str(x) for x in p_neg)}",
        f"bridge_prefix_pos={','.join(str(x) for x in p_pos)}",
        f"bridge_sharp_banks={sb_neg},{sb_pos}",
        "bridge_b772_outcomes=neg:(p6_reflect,j0,rem56,unwound),pos:(p6_reflect,j2,rem0,unwound)",
        "bridge_sharp_outcomes=neg:(k2,j0,b56,rev_ok),pos:(k2,j2,b0,rev_ok)",
        f"bridge_trajectories_sha256={br_dig}",
    ]


def run_breaker_and_compare(core_lines):
    breaker_path = PROBE_DIR / "breaker.py"
    proc = subprocess.run(
        [sys.executable, "-I", str(breaker_path)],
        cwd=str(PROBE_DIR.parent.parent),
        capture_output=True,
        text=True,
        check=True,
    )
    if proc.stderr:
        raise AssertionError(f"breaker stderr not empty: {proc.stderr}")
    b_lines = [line.strip() for line in proc.stdout.splitlines() if line.strip()]
    if b_lines != core_lines + ["BREAKER_RESULT=PASS"]:
        raise AssertionError(f"breaker mismatch:\n{b_lines}\n!=\n{core_lines}")


def main():
    frozen_sha, verify_sha, breaker_sha = check_pre_pin_integrity()
    core_lines = emit_core_lines()
    run_breaker_and_compare(core_lines)
    print("PROBE=P-INTEGER-K1-SCALED-BRIDGE-3")
    print("STATUS=NON-CANONICAL")
    print("CLAIM_LEVEL=L1")
    print(f"frozen_manifest_sha256={frozen_sha}")
    print(f"verify_sha256={verify_sha}")
    print(f"breaker_sha256={breaker_sha}")
    for line in core_lines:
        print(line)
    print("independent_breaker_match=PASS")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
