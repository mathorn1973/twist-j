#!/usr/bin/env python3
"""Independent pure-integer and 5-cyclic implementation for P-INTEGER-K1-SCALED-BRIDGE-3."""

import hashlib
import math
import sys

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


# --- Independent representation B: 5-tuple cyclic Z[j] modulo (1,1,1,1,1) ---

def cyc_red(x):
    x4 = x[4]
    return (x[0] - x4, x[1] - x4, x[2] - x4, x[3] - x4, 0)


def cyc_add(x, y):
    return cyc_red(tuple(x[i] + y[i] for i in range(5)))


def cyc_sub(x, y):
    return cyc_red(tuple(x[i] - y[i] for i in range(5)))


def cyc_mul(x, y):
    out = [0, 0, 0, 0, 0]
    for i in range(5):
        xi = x[i]
        if xi:
            for k in range(5):
                out[(i + k) % 5] += xi * y[k]
    return cyc_red(out)


def cyc_conj(x):
    return cyc_red((x[0], x[4], x[3], x[2], x[1]))


def cyc_from_c(c0, c1, c2, c3):
    return (c0, c1, c2, c3, 0)


def cyc_from_real(r0, r1):
    # r0 + r1 * phi where phi = -j^2 - j^3
    return (r0, 0, -r1, -r1, 0)


def cyc_to_real(x):
    x = cyc_red(x)
    if x[1] != 0 or x[4] != 0 or x[2] != x[3]:
        raise ValueError(f"not in Z[phi]: {x}")
    return (x[0], -x[2])


PHI_CYC = (0, 0, -1, -1, 0)
PHI_INV_CYC = (-1, 0, -1, -1, 0)
J_UNIT_CYC = (1, 0, 1, 0, 0)
J_INV_CYC = (0, -1, -1, 0, 0)


# --- Direct coordinate formulas on 8-integer Hermitian state ---
# h = (a0, a1, d0, d1, c0, c1, c2, c3)

def diagonal_transport_direct(h, first, second):
    a0, a1, d0, d1, c0, c1, c2, c3 = h
    a_cyc = cyc_from_real(a0, a1)
    d_cyc = cyc_from_real(d0, d1)
    c_cyc = cyc_from_c(c0, c1, c2, c3)
    na_cyc = cyc_mul(cyc_mul(first, cyc_conj(first)), a_cyc)
    nd_cyc = cyc_mul(cyc_mul(second, cyc_conj(second)), d_cyc)
    nc_cyc = cyc_mul(cyc_mul(first, c_cyc), cyc_conj(second))
    na0, na1 = cyc_to_real(na_cyc)
    nd0, nd1 = cyc_to_real(nd_cyc)
    return (na0, na1, nd0, nd1, nc_cyc[0], nc_cyc[1], nc_cyc[2], nc_cyc[3])


def step_A_direct(h):
    return diagonal_transport_direct(h, J_UNIT_CYC, PHI_CYC)


def step_A_inv_direct(h):
    return diagonal_transport_direct(h, J_INV_CYC, PHI_INV_CYC)


def step_B_direct(h, q):
    if q == 0:
        return h
    a0, a1, d0, d1, c0, c1, c2, c3 = h
    a_cyc = cyc_from_real(a0, a1)
    d_cyc = cyc_from_real(d0, d1)
    c_cyc = cyc_from_c(c0, c1, c2, c3)
    cc_cyc = cyc_conj(c_cyc)
    q_cyc = (q, 0, 0, 0, 0)
    q2_cyc = (q * q, 0, 0, 0, 0)
    na_cyc = cyc_add(
        a_cyc,
        cyc_add(cyc_mul(q_cyc, cyc_add(c_cyc, cc_cyc)), cyc_mul(q2_cyc, d_cyc)),
    )
    nc_cyc = cyc_add(c_cyc, cyc_mul(q_cyc, d_cyc))
    na0, na1 = cyc_to_real(na_cyc)
    return (na0, na1, d0, d1, nc_cyc[0], nc_cyc[1], nc_cyc[2], nc_cyc[3])


def herm_add(h1, h2):
    return tuple(h1[i] + h2[i] for i in range(8))


def herm_sub(h1, h2):
    return tuple(h1[i] - h2[i] for i in range(8))


def norm_h_quadratic(h):
    a0, a1, d0, d1, c0, c1, c2, c3 = h
    real_part = 4 * a0 * a0 + 4 * a0 * a1 + 6 * a1 * a1
    real_part += 4 * d0 * d0 + 4 * d0 * d1 + 6 * d1 * d1
    off_sum = c0 + c1 + c2 + c3
    off_part = 10 * (c0 * c0 + c1 * c1 + c2 * c2 + c3 * c3) - 2 * off_sum * off_sum
    return real_part + off_part


# --- Pure integer scaled K1 representation ---

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


def k1_x1(word):
    U0, U1 = k1_init_U0_U1(word)
    return (tuple(SCALE * x for x in U1), U0, 1)


def k1_in_d_minus(x):
    U, W, k = x
    if k < 2:
        return False
    cw = c_apply(W)
    for r in range(5):
        if (cw[r] - U[r]) % SCALE_SQ != 0:
            return False
    return True


def t_k1_step(x, eps):
    U, W, k = x
    if eps == 1:
        cu = c_apply(U)
        U_next = tuple(cu[r] - SCALE_SQ * W[r] for r in range(5))
        return (U_next, U, k + 1)
    if eps == -1:
        if not k1_in_d_minus(x):
            return None
        cw = c_apply(W)
        W_prev = tuple((cw[r] - U[r]) // SCALE_SQ for r in range(5))
        return (W, W_prev, k - 1)
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
        raise ValueError("v3(0) is infinite")
    cnt = 0
    while n % 3 == 0:
        n //= 3
        cnt += 1
    return cnt


# --- Coupled 7-phase 40-integer bridge ---
# State: (s, q, H, R, Z, U, W, k, p, b, eps)

def energy_bridge_core(s, q, H, R, Z, U, W, k):
    return (
        1
        + s * s
        - s * q
        + q * q
        + norm_h_quadratic(H)
        + norm_h_quadratic(R)
        + norm_h_quadratic(Z)
        + energy_k1_core((U, W, k))
    )


def t_bridge_step(core, eps):
    s, q, H, R, Z, U, W, k, p = core
    if eps == 1:
        if p == 0:
            ns, nq = s - q, s
        elif p == 1:
            H = step_B_direct(H, -q)
            ns, nq = s, q
        elif p == 2:
            H = step_A_inv_direct(H)
            ns, nq = s, q
        elif p == 3:
            H = step_B_direct(H, q)
            ns, nq = s, q
        elif p == 4:
            H = step_A_direct(H)
            ns, nq = s, q
        elif p == 5:
            Z = herm_add(Z, herm_sub(H, R))
            ns, nq = s, q
        elif p == 6:
            nxt_k1 = t_k1_step((U, W, k), 1)
            U, W, k = nxt_k1
            ns, nq = s, q
        else:
            raise ValueError("invalid phase")
        return (ns, nq, H, R, Z, U, W, k, (p + 1) % 7)
    if eps == -1:
        prev_p = (p - 1) % 7
        if prev_p == 0:
            ns, nq = q, q - s
        elif prev_p == 1:
            H = step_B_direct(H, q)
            ns, nq = s, q
        elif prev_p == 2:
            H = step_A_direct(H)
            ns, nq = s, q
        elif prev_p == 3:
            H = step_B_direct(H, -q)
            ns, nq = s, q
        elif prev_p == 4:
            H = step_A_inv_direct(H)
            ns, nq = s, q
        elif prev_p == 5:
            Z = herm_sub(Z, herm_sub(H, R))
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
    for w in WORDS:
        U0, _ = k1_init_U0_U1(w)
        # Step n = 0 metric check: h_0 = U0 / 2
        denom0 = 2
        for r in range(5):
            num = U0[r]
            if not (100 * (denom0 + num) > denom0 and 100 * (denom0 - num) > denom0):
                raise AssertionError("n=0 metric diagonal bound failed")
            if not (10000 * (denom0 * denom0 - num * num) > 199 * denom0 * denom0):
                raise AssertionError("n=0 metric det bound failed")
            metric_checks += 1

        cur = k1_x1(w)
        for n in range(1, 25):
            U, W, k = cur
            if k != n:
                raise AssertionError("counter mismatch")
            denom = 2 * (SCALE ** n)
            if sum(U) != denom:
                raise AssertionError("sum(U_n) != 2 * 324^n")

            # Compute common gcd of (U_0, ..., U_4, denom)
            g = denom
            for u in U:
                g = math.gcd(g, abs(u))
            if g % 3 == 0:
                raise AssertionError(f"3 divides gcd at w={w}, n={n}")

            d_n = denom // g
            P_red = tuple(u // g for u in U)
            v3_dn = v3_int(d_n)
            if v3_dn != 4 * (n - 1):
                raise AssertionError(f"v3(d_n) mismatch at w={w}, n={n}")
            val_hist.append(f"{w}:{n}:{v3_dn}:{d_n}")

            # Check quadratic precision bound on reduced and canonical representations
            lhs_red = 5 * (sum(p * p for p in P_red) + d_n * d_n)
            rhs_dn = 6 * d_n * d_n
            rhs_pow = 6 * (3 ** (8 * (n - 1)))
            if not (lhs_red >= rhs_dn >= rhs_pow):
                raise AssertionError("quadratic precision bound failed on reduced")
            lhs_can = 5 * (sum(u * u for u in U) + denom * denom)
            if not (lhs_can >= 6 * denom * denom >= rhs_dn >= rhs_pow):
                raise AssertionError("quadratic precision bound failed on canonical")

            # Check transverse metric bounds at all 5 sites
            for r in range(5):
                ur = U[r]
                if not (100 * (denom + ur) > denom and 100 * (denom - ur) > denom):
                    raise AssertionError("metric diagonal bound failed")
                if not (10000 * (denom * denom - ur * ur) > 199 * denom * denom):
                    raise AssertionError("metric determinant bound failed")
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
        if not (es[0] < es[1] < es[2] < es[3] < es[4]):
            raise AssertionError("energy not strictly increasing")

        for N in (2, 3, 4):
            b_sharp = es[N - 1] - es[0]
            # 1. Sharp bank cycle of exact period 2N
            s0 = (xs[0], b_sharp, 1)
            cur_s = s0
            for step_idx in range(1, 2 * N + 1):
                cur_s = f_k1(cur_s)
                if step_idx == N - 1 and cur_s != (xs[N - 1], 0, 1):
                    raise AssertionError("failed to reach apex at N-1")
                if step_idx == N and cur_s != (xs[N - 1], 0, -1):
                    raise AssertionError("failed to reflect at apex N")
                if step_idx == 2 * N - 1 and cur_s != (xs[0], b_sharp, -1):
                    raise AssertionError("failed to return to x_1 at 2N-1")
                if step_idx < 2 * N and cur_s == s0:
                    raise AssertionError("premature period in sharp cycle")
            if cur_s != s0:
                raise AssertionError("sharp cycle did not close at 2N")
            sharp_cycles += 1
            cycle_records.append(f"sharp:{w}:N={N}:b={b_sharp}:per={2*N}")

            # 2. Underfunded bank B_sharp - 1 cycle of exact period 2(N-1)
            s0_u = (xs[0], b_sharp - 1, 1)
            cur_u = s0_u
            rem_at_nm1 = es[N - 1] - es[N - 2] - 1
            for step_idx in range(1, 2 * (N - 1) + 1):
                cur_u = f_k1(cur_u)
                if step_idx == N - 2 and cur_u != (xs[N - 2], rem_at_nm1, 1):
                    raise AssertionError("failed to reach N-1 in underfunded cycle")
                if step_idx == N - 1 and cur_u != (xs[N - 2], rem_at_nm1, -1):
                    raise AssertionError("failed to reflect at N-1 in underfunded cycle")
                if step_idx < 2 * (N - 1) and cur_u == s0_u:
                    raise AssertionError("premature period in underfunded cycle")
            if cur_u != s0_u:
                raise AssertionError("underfunded cycle did not close at 2(N-1)")
            under_cycles += 1
            cycle_records.append(f"under:{w}:N={N}:b={b_sharp-1}:per={2*(N-1)}")

    digest = hashlib.sha256("\n".join(cycle_records).encode("ascii")).hexdigest()
    return e_0010, b_sharp_2, b_sharp_3, sharp_cycles, under_cycles, digest


def check_coupled_bridge():
    D_REG = (0, 0, 1, 0, 0, 0, 0, 0)
    Z0_REG = (1, 0, 1, 0, 0, 1, 0, 0)
    x1 = k1_x1("0010")
    x2 = t_k1_step(x1, 1)
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

    # Prefix energies and trajectories for s = -1 and s = +1
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

    if prefixes[-1] != [209981, 209981, 209993, 210013, 210097, 210327, 210697, 36215041128]:
        raise AssertionError(f"unexpected prefix(-1): {prefixes[-1]}")
    if prefixes[1] != [209981, 209981, 209993, 210013, 210097, 210327, 210753, 36215041184]:
        raise AssertionError(f"unexpected prefix(+1): {prefixes[1]}")
    if sharp_banks[-1] != 36214831147 or sharp_banks[1] != 36214831203:
        raise AssertionError(f"unexpected sharp bridge banks: {sharp_banks}")

    traj_records = []

    # 1. Bank 772: phases 0..5 succeed, phase 6 reflects, 6 steps unwind to initial with eps=-1
    for a, exp_j, exp_rem in ((-1, 0, 56), (1, 2, 0)):
        s0 = (a, 0, D_REG, D_REG, Z0_REG, U1, W1, k1, 0, 772, 1)
        cur = s0
        for _ in range(6):
            cur = f_bridge(cur)
        if cur[8] != 6 or cur[9] != exp_rem or cur[10] != 1:
            raise AssertionError("bank 772 after 6 steps mismatch")
        if cur[4][5] != exp_j or (cur[5], cur[6], cur[7]) != x1:
            raise AssertionError("bank 772 detector or K1 state mismatch at p=6")
        cur = f_bridge(cur)
        if cur[8] != 6 or cur[9] != exp_rem or cur[10] != -1 or (cur[5], cur[6], cur[7]) != x1:
            raise AssertionError("bank 772 reflection at p=6 mismatch")
        for _ in range(6):
            cur = f_bridge(cur)
        if cur != r_bridge_flip(s0):
            raise AssertionError("bank 772 unwind failed")
        traj_records.append(f"b772:a={a}:j={exp_j}:rem={exp_rem}:unwound=1")

    # 2. Bank 36214831147 (sharp for a=-1): a=-1 completes all 7 phases; a=+1 reflects at phase 6
    b_neg_sharp = 36214831147
    s0_neg = (-1, 0, D_REG, D_REG, Z0_REG, U1, W1, k1, 0, b_neg_sharp, 1)
    hist_neg = [s0_neg]
    for _ in range(7):
        hist_neg.append(f_bridge(hist_neg[-1]))
    fin_neg = hist_neg[-1]
    if (fin_neg[5], fin_neg[6], fin_neg[7]) != x2 or fin_neg[8] != 0 or fin_neg[9] != 0 or fin_neg[4][5] != 0:
        raise AssertionError("sharp(-1) completion failed")
    rev_neg = r_bridge_flip(fin_neg)
    for idx in range(6, -1, -1):
        rev_neg = f_bridge(rev_neg)
        if r_bridge_flip(rev_neg) != hist_neg[idx]:
            raise AssertionError("sharp(-1) reverse trajectory mismatch")
    traj_records.append("b_neg_sharp:a=-1:k=2:b=0:rev=1")

    s0_pos_at_neg = (1, 0, D_REG, D_REG, Z0_REG, U1, W1, k1, 0, b_neg_sharp, 1)
    cur_p = s0_pos_at_neg
    for _ in range(6):
        cur_p = f_bridge(cur_p)
    if cur_p[8] != 6 or cur_p[9] != 36214830375 or cur_p[4][5] != 2:
        raise AssertionError("a=+1 at sharp(-1) phase 6 pre-state mismatch")
    cur_p = f_bridge(cur_p)
    if cur_p[8] != 6 or cur_p[10] != -1 or (cur_p[5], cur_p[6], cur_p[7]) != x1:
        raise AssertionError("a=+1 at sharp(-1) phase 6 reflection mismatch")
    for _ in range(6):
        cur_p = f_bridge(cur_p)
    if cur_p != r_bridge_flip(s0_pos_at_neg):
        raise AssertionError("a=+1 at sharp(-1) unwind mismatch")
    traj_records.append("b_neg_sharp:a=+1:reflected_p6:unwound=1")

    # 3. Bank 36214831203 (sharp for a=+1): both a=-1 and a=+1 complete all 7 phases
    b_pos_sharp = 36214831203
    for a, exp_j, exp_b in ((-1, 0, 56), (1, 2, 0)):
        s0 = (a, 0, D_REG, D_REG, Z0_REG, U1, W1, k1, 0, b_pos_sharp, 1)
        hist = [s0]
        for _ in range(7):
            hist.append(f_bridge(hist[-1]))
        fin = hist[-1]
        if (fin[5], fin[6], fin[7]) != x2 or fin[8] != 0 or fin[9] != exp_b or fin[4][5] != exp_j:
            raise AssertionError("sharp(+1) completion mismatch")
        if herm_add(herm_sub(fin[4], fin[2]), fin[3]) != Z0_REG:
            raise AssertionError("detector baseline reconstruction failed")
        rev = r_bridge_flip(fin)
        for idx in range(6, -1, -1):
            rev = f_bridge(rev)
            if r_bridge_flip(rev) != hist[idx]:
                raise AssertionError("sharp(+1) reverse trajectory mismatch")
        traj_records.append(f"b_pos_sharp:a={a}:k=2:j={exp_j}:b={exp_b}:rev=1")

    # 4. Sharp - 1 for each sign: reflects at phase 6 and unwinds in 6 steps
    for a, b_sh in ((-1, b_neg_sharp), (1, b_pos_sharp)):
        s0 = (a, 0, D_REG, D_REG, Z0_REG, U1, W1, k1, 0, b_sh - 1, 1)
        cur = s0
        for _ in range(6):
            cur = f_bridge(cur)
        if cur[8] != 6 or cur[9] != 36214830430:
            raise AssertionError("sharp-1 pre-phase-6 bank mismatch")
        cur = f_bridge(cur)
        if cur[8] != 6 or cur[10] != -1 or (cur[5], cur[6], cur[7]) != x1:
            raise AssertionError("sharp-1 reflection at phase 6 failed")
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


def main():
    for line in emit_core_lines():
        print(line)
    print("BREAKER_RESULT=PASS")


if __name__ == "__main__":
    main()
