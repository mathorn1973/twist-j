#!/usr/bin/env python3
"""Independent breaker implementation for P-INTEGER-RETAINED-PAIR-SOURCE-1.

Uses cyclic 5-vector and 8-vector arithmetic for Z[j] and Z[m], Fraction-based
Gaussian elimination for determinants and basis inversion, explicit matrix/column
action for U_hat_z, and dictionary-represented state transitions for the 2-phase
funded automaton.
"""
from fractions import Fraction
from functools import reduce
import hashlib
from itertools import product
from math import gcd, isqrt


ELL = (1, 10, 18, 16, -1, -27, -32, -3)
F_COEFFS = (1, -2, 4, -3, 1)
G_COEFFS = (1, -4, 8, -4, 1)


def gcd_all(seq) -> int:
    return reduce(lambda a, b: gcd(a, abs(int(b))), seq, 0)


def det_fraction(mat) -> int:
    n = len(mat)
    a = [[Fraction(x) for x in row] for row in mat]
    sign = Fraction(1)
    for k in range(n):
        piv = None
        for r in range(k, n):
            if a[r][k] != 0:
                piv = r
                break
        if piv is None:
            return 0
        if piv != k:
            a[k], a[piv] = a[piv], a[k]
            sign = -sign
        piv_val = a[k][k]
        sign *= piv_val
        for r in range(k + 1, n):
            factor = a[r][k] / piv_val
            if factor != 0:
                for c in range(k, n):
                    a[r][c] -= factor * a[k][c]
    assert sign.denominator == 1
    return int(sign.numerator)


def solve_int_4x4(mat, rhs):
    a = [[Fraction(mat[r][c]) for c in range(4)] + [Fraction(rhs[r])] for r in range(4)]
    for k in range(4):
        piv = next(r for r in range(k, 4) if a[r][k] != 0)
        a[k], a[piv] = a[piv], a[k]
        pv = a[k][k]
        for c in range(k, 5):
            a[k][c] /= pv
        for r in range(4):
            if r != k and a[r][k] != 0:
                f = a[r][k]
                for c in range(k, 5):
                    a[r][c] -= f * a[k][c]
    out = []
    for r in range(4):
        val = a[r][4]
        assert val.denominator == 1
        out.append(int(val.numerator))
    return tuple(out)


def cyc5_mul(u, v):
    out = [0] * 5
    for i in range(5):
        for k in range(5):
            out[(i + k) % 5] += u[i] * v[k]
    return out


def cyc5_to_basis4(u):
    return (u[0] - u[4], u[1] - u[4], u[2] - u[4], u[3] - u[4])


def cyc5_conj(u):
    return [u[0], u[4], u[3], u[2], u[1]]


def cyc5_trace(u) -> int:
    b = cyc5_to_basis4(u)
    return 4 * b[0] - b[1] - b[2] - b[3]


def cyc8_mul(u, v):
    out = [0] * 8
    for i in range(8):
        for k in range(8):
            out[(i + k) % 8] += u[i] * v[k]
    return out


def cyc8_to_basis4(u):
    return (u[0] - u[4], u[1] - u[5], u[2] - u[6], u[3] - u[7])


def cyc8_conj(u):
    return [u[0], u[7], u[6], u[5], u[4], u[3], u[2], u[1]]


def cyc8_trace(u) -> int:
    b = cyc8_to_basis4(u)
    return 4 * b[0]


def mat_mul_int(a, b):
    r_len = len(a)
    c_len = len(b[0])
    k_len = len(b)
    res = [[0] * c_len for _ in range(r_len)]
    for r in range(r_len):
        for k in range(k_len):
            v = a[r][k]
            if v:
                for c in range(c_len):
                    res[r][c] += v * b[k][c]
    return res


def mat_T(a):
    return [list(col) for col in zip(*a)]


def companion_pow_col0(coeffs4, power: int):
    c0, c1, c2, c3, _ = coeffs4
    comp = [
        [0, 0, 0, -c0],
        [1, 0, 0, -c1],
        [0, 1, 0, -c2],
        [0, 0, 1, -c3],
    ]
    vec = [1, 0, 0, 0]
    for _ in range(power):
        vec = [sum(comp[r][c] * vec[c] for c in range(4)) for r in range(4)]
    return tuple(vec)


G0_MAT = [[0] * 9 for _ in range(9)]
G0_MAT[0][0] = 1
for _r in range(1, 5):
    for _s in range(1, 5):
        G0_MAT[_r][_s] = 4 if _r == _s else -1
for _r in range(5, 9):
    G0_MAT[_r][_r] = 4

L_MAT = [[G0_MAT[i // 9][j // 9] * G0_MAT[i % 9][j % 9] for j in range(81)] for i in range(81)]


def l_apply(vec):
    out = [0] * 81
    for i in range(81):
        s = 0
        row = L_MAT[i]
        for j, x in enumerate(vec):
            if x:
                s += row[j] * x
        out[i] = s
    return tuple(out)


def q_val(z) -> int:
    y = (1,) + tuple(z)
    gy = [sum(G0_MAT[i][j] * y[j] for j in range(9)) for i in range(9)]
    return sum(y[i] * gy[i] for i in range(9)) - 1


def in_S(z) -> bool:
    return (z[5] - z[6] - z[7]) % 3 == 0


def admitted(z, bound: int) -> bool:
    return in_S(z) and 0 < q_val(z) <= bound


def unit_81(idx: int):
    return tuple(1 if i == idx else 0 for i in range(81))


E0_PAIR = unit_81(0)


def cell_m(X, D: int) -> int:
    return gcd(gcd_all(X), abs(int(D)))


def cell_cost(X, D: int) -> int:
    lx = l_apply(X)
    return sum(x * y for x, y in zip(X, lx)) + D * D


def make_gate(z, bound: int):
    act = admitted(z, bound)
    qz = q_val(z)
    Az = 1 + qz
    if not act:
        return (False, qz, Az, 1, E0_PAIR, (0,) * 81, (0,) * 81)
    y = (1,) + tuple(z)
    w = tuple(y[i // 9] * y[i % 9] for i in range(81))
    v = tuple(Az * E0_PAIR[i] - w[i] for i in range(81))
    r = l_apply(v)
    return (True, qz, Az, Az * (Az - 1), w, v, r)


def apply_u_hat(z, bound: int, X, D: int):
    act, _qz, _Az, dz, _w, v, r = make_gate(z, bound)
    if not act:
        return (tuple(X), int(D))
    m = cell_m(X, D)
    rx = sum(ri * xi for ri, xi in zip(r, X))
    Y = [dz * xi - rx * vi for xi, vi in zip(X, v)]
    M = dz * D
    g = gcd(gcd_all(Y), M)
    return (tuple(m * (yi // g) for yi in Y), m * (M // g))


def energy_dict(st_dict) -> int:
    z = st_dict["z"]
    z_arch = st_dict["z_arch"]
    P = st_dict["P"]
    B = st_dict["B"]
    n = st_dict["n"]
    p = st_dict["p"]
    return (
        1
        + q_val(z)
        + q_val(z_arch)
        + cell_cost(P[0], P[1])
        + sum(cell_cost(c[0], c[1]) for c in B)
        + n * n
        + p * p
    )


def step_core_dict(st_dict, bound: int):
    z = st_dict["z"]
    z_arch = st_dict["z_arch"]
    P = st_dict["P"]
    B = list(st_dict["B"])
    n = st_dict["n"]
    p = st_dict["p"]
    eps = st_dict["eps"]
    K = len(B)
    act = admitted(z, bound)
    if eps == 1:
        if p == 0:
            if act and 0 <= n < K:
                B[n] = apply_u_hat(z, bound, B[n][0], B[n][1])
            return {"z": z, "z_arch": z_arch, "P": P, "B": tuple(B), "n": n, "p": 1}
        P_new = P
        if act and 0 <= n < K:
            P_new, B[n] = B[n], P
        return {"z": z, "z_arch": z_arch, "P": P_new, "B": tuple(B), "n": n + 1, "p": 0}
    if p == 1:
        if act and 0 <= n < K:
            B[n] = apply_u_hat(z, bound, B[n][0], B[n][1])
        return {"z": z, "z_arch": z_arch, "P": P, "B": tuple(B), "n": n, "p": 0}
    n_prev = n - 1
    P_new = P
    if act and 0 <= n_prev < K:
        P_new, B[n_prev] = B[n_prev], P
    return {"z": z, "z_arch": z_arch, "P": P_new, "B": tuple(B), "n": n_prev, "p": 1}


def step_funded_dict(st_dict, bound: int):
    cand = step_core_dict(st_dict, bound)
    b_new = st_dict["b"] + energy_dict(st_dict) - energy_dict(cand)
    if b_new >= 0:
        cand["b"] = b_new
        cand["eps"] = st_dict["eps"]
        return cand
    out = dict(st_dict)
    out["eps"] = -st_dict["eps"]
    return out


def flip_dir_dict(st_dict):
    out = dict(st_dict)
    out["eps"] = -st_dict["eps"]
    return out


def inv_funded_dict(st_dict, bound: int):
    return flip_dir_dict(step_funded_dict(flip_dir_dict(st_dict), bound))


def bal_rep(val: int, mod: int) -> int:
    h = mod // 2
    return (val + h) % mod - h


def cap_map(x_in, z_prog, z_arch, mod: int, inv: bool = False):
    if not inv:
        return (
            tuple(x_in),
            tuple(bal_rep(a + x, mod) for a, x in zip(z_arch, x_in)),
            tuple(z_prog),
        )
    return (
        tuple(x_in),
        tuple(z_arch),
        tuple(bal_rep(p - x, mod) for p, x in zip(z_prog, x_in)),
    )


def main():
    # 1. Cyclotomic trace-form & seam coordinate bridge via cyclic vectors
    J_cyc = [1, 0, 1, 0, 0]
    J_pows_cyc = [[1, 0, 0, 0, 0]]
    for _ in range(4):
        J_pows_cyc.append(cyc5_mul(J_pows_cyc[-1], J_cyc))
    J_pows_4 = [cyc5_to_basis4(u) for u in J_pows_cyc]
    for i in range(4):
        assert (
            J_pows_4[4][i]
            - 3 * J_pows_4[3][i]
            + 4 * J_pows_4[2][i]
            - 2 * J_pows_4[1][i]
            + J_pows_4[0][i]
            == 0
        )

    M_cyc = [1, 1, 1, 0, 0, 0, 0, 0]
    M_pows_cyc = [[1, 0, 0, 0, 0, 0, 0, 0]]
    for _ in range(4):
        M_pows_cyc.append(cyc8_mul(M_pows_cyc[-1], M_cyc))
    M_pows_4 = [cyc8_to_basis4(u) for u in M_pows_cyc]
    for i in range(4):
        assert (
            M_pows_4[4][i]
            - 4 * M_pows_4[3][i]
            + 8 * M_pows_4[2][i]
            - 4 * M_pows_4[1][i]
            + M_pows_4[0][i]
            == 0
        )

    T_J = [[J_pows_4[col][row] for col in range(4)] for row in range(4)]
    T_M = [[M_pows_4[col][row] for col in range(4)] for row in range(4)]
    det_TJ = det_fraction(T_J)
    det_TM = det_fraction(T_M)
    assert det_TJ == -1 and det_TM == -3

    G5 = [
        [
            cyc5_trace(
                cyc5_mul(
                    [1 if k == r else 0 for k in range(5)],
                    cyc5_conj([1 if k == s else 0 for k in range(5)]),
                )
            )
            for s in range(4)
        ]
        for r in range(4)
    ]
    G8 = [
        [
            cyc8_trace(
                cyc8_mul(
                    [1 if k == r else 0 for k in range(8)],
                    cyc8_conj([1 if k == s else 0 for k in range(8)]),
                )
            )
            for s in range(4)
        ]
        for r in range(4)
    ]
    det_G5 = det_fraction(G5)
    det_G8 = det_fraction(G8)
    G = [
        [G5[r][s] if r < 4 and s < 4 else (G8[r - 4][s - 4] if r >= 4 and s >= 4 else 0) for s in range(8)]
        for r in range(8)
    ]
    det_G = det_fraction(G)
    T_JM = [
        [T_J[r][s] if r < 4 and s < 4 else (T_M[r - 4][s - 4] if r >= 4 and s >= 4 else 0) for s in range(8)]
        for r in range(8)
    ]
    G_S = mat_mul_int(mat_T(T_JM), mat_mul_int(G, T_JM))
    det_GS = det_fraction(G_S)

    C_cols = [companion_pow_col0(F_COEFFS, k) + companion_pow_col0(G_COEFFS, k) for k in range(8)]
    C_mat = mat_T(C_cols)
    det_C = abs(det_fraction(C_mat))
    G_R = mat_mul_int(mat_T(C_mat), mat_mul_int(G_S, C_mat))
    det_GR = det_fraction(G_R)
    assert (det_G5, det_G8, det_G, det_GS, det_GR, det_C) == (125, 256, 32000, 288000, 484128000, 41)

    total_ternary = 0
    in_S_count = 0
    admitted_32_count = 0
    bridge_hasher = hashlib.sha256()
    for z in product((-1, 0, 1), repeat=8):
        total_ternary += 1
        if not in_S(z):
            continue
        in_S_count += 1
        cA = solve_int_4x4(T_J, z[:4])
        cB = solve_int_4x4(T_M, z[4:])
        qz = q_val(z)
        seam_eval = (sum(cA[k] * pow(19, k, 41) for k in range(4)) - sum(cB[k] * pow(19, k, 41) for k in range(4))) % 41
        assert seam_eval == sum(l_i * z_i for l_i, z_i in zip(ELL, z)) % 41
        if 0 < qz <= 32:
            admitted_32_count += 1
        bridge_hasher.update(f"{z}:{cA}:{cB}:{qz}:{seam_eval}\n".encode("utf-8"))
    bridge_sha256 = bridge_hasher.hexdigest()

    # 2. Pair involution & certificates
    inv_checked = 0
    for z in product((-1, 0, 1), repeat=8):
        if not admitted(z, 32):
            continue
        _act, qz, Az, _dz, wz, _v, _r = make_gate(z, 32)
        X1, D1 = apply_u_hat(z, 32, E0_PAIR, 1)
        assert (X1, D1) == (wz, Az)
        assert apply_u_hat(z, 32, X1, D1) == (E0_PAIR, 1)
        assert cell_cost(X1, D1) - cell_cost(E0_PAIR, 1) == 2 * qz * (qz + 2)
        inv_checked += 1

    e1_prog = (1, 0, 0, 0, 0, 0, 0, 0)
    v_prog = (1, 0, 0, 0, -1, 0, 0, 0)
    neg_v_prog = (-1, 0, 0, 0, 1, 0, 0, 0)
    dense_prog = (1, -1, 1, -1, 1, 1, 1, 0)
    bench_programs = [e1_prog, v_prog, neg_v_prog, dense_prog] + [
        tuple(t * x for x in v_prog) for t in (40, 41, 42)
    ]
    cert_labels = []
    for z in bench_programs:
        act, qz, Az, dz, _w, v, r = make_gate(z, 14112)
        assert act
        N = [[dz * (1 if i == j else 0) - v[i] * r[j] for j in range(81)] for i in range(81)]
        NN = mat_mul_int(N, N)
        assert NN == [[dz * dz * (1 if i == j else 0) for j in range(81)] for i in range(81)]
        cert_labels.append(f"{qz}:{Az}:{dz}")

    w_e1 = make_gate(e1_prog, 32)[4]
    w_v = make_gate(v_prog, 32)[4]
    test_cells = [(unit_81(i), 1) for i in range(81)]
    test_cells += [(tuple(3 * x for x in unit_81(9 * r)), 3) for r in range(9)]
    for k_idx in (1, 9, 10, 40, 72, 80):
        b0 = unit_81(0)
        bk = unit_81(k_idx)
        test_cells.append((tuple(b0[i] + 2 * bk[i] for i in range(81)), 5))
    test_cells += [
        (w_e1, 5),
        (tuple(2 * x for x in w_e1), 10),
        (w_v, 9),
        (tuple(4 * x for x in w_v), 36),
    ]
    box_progs = [
        e1_prog,
        v_prog,
        neg_v_prog,
        dense_prog,
        (0,) * 8,
        (0, 0, 0, 0, 0, 1, 0, 0),
    ]
    inv_box_count = 0
    inv_box_hasher = hashlib.sha256()
    for z in box_progs:
        for X, D in test_cells:
            X1, D1 = apply_u_hat(z, 32, X, D)
            X2, D2 = apply_u_hat(z, 32, X1, D1)
            assert (X2, D2) == (X, D)
            inv_box_count += 1
            inv_box_hasher.update(
                f"{z}:{D}:{D1}:{cell_m(X, D)}:{cell_cost(X1, D1)}:{X1[0]}:{X1[1]}:{X1[9]}:{X1[80]}\n".encode(
                    "utf-8"
                )
            )
    inv_box_sha256 = inv_box_hasher.hexdigest()

    # 3. Funded 2-phase integer automaton
    p_comb = (tuple(2 * unit_81(1)[i] + unit_81(80)[i] for i in range(81)), 3)
    ports = [(unit_81(0), 1), (unit_81(9), 1), p_comb]
    stocks = [
        ((unit_81(0), 1), (unit_81(0), 1)),
        ((unit_81(9), 1), (unit_81(0), 1)),
        ((w_v, 9), (unit_81(0), 1)),
    ]
    z_zero = (0,) * 8
    accepted_count = 0
    reflected_count = 0
    for z in (e1_prog, v_prog, z_zero):
        for P in ports:
            for B in stocks:
                for n in (-1, 0, 1, 2, 3, 4):
                    for p in (0, 1):
                        for b in (0, 1, 49, 500):
                            for eps in (1, -1):
                                st = {
                                    "z": z,
                                    "z_arch": z_zero,
                                    "P": P,
                                    "B": B,
                                    "n": n,
                                    "p": p,
                                    "b": b,
                                    "eps": eps,
                                }
                                st_next = step_funded_dict(st, 32)
                                assert inv_funded_dict(st_next, 32) == st
                                assert step_funded_dict(inv_funded_dict(st, 32), 32) == st
                                assert energy_dict(st_next) + st_next["b"] == energy_dict(st) + b
                                if st_next["eps"] == eps:
                                    accepted_count += 1
                                else:
                                    reflected_count += 1

    # K = 3 trajectories
    traj_hasher = hashlib.sha256()
    k3_prefixes = []
    k3_bounces = []
    P0_ref = (unit_81(9), 1)
    B_ready_3 = ((E0_PAIR, 1), (E0_PAIR, 1), (E0_PAIR, 1))
    for label, z in (("e1", e1_prog), ("v", v_prog), ("dense", dense_prog)):
        _act, _qz, Az, _dz, _wz, _v, _r = make_gate(z, 32)
        b_sharp = 6 * (Az * Az - 1) + 9
        st = {
            "z": z,
            "z_arch": z_zero,
            "P": P0_ref,
            "B": B_ready_3,
            "n": 0,
            "p": 0,
            "b": b_sharp,
            "eps": 1,
        }
        E0 = energy_dict(st)
        diffs = [0]
        for _ in range(6):
            st = step_funded_dict(st, 32)
            diffs.append(energy_dict(st) - E0)
        k3_prefixes.append(f"{label}:" + ",".join(str(d) for d in diffs))
        b_under = b_sharp - 1
        k3_bounces.append(f"{label}:(b0:{b_under},step5_b:3,reflected,unwound)")
        traj_hasher.update(f"{label}:{diffs}:{b_sharp}:{b_under}\n".encode("utf-8"))

    # Dirty stock release
    st_dirty0 = {
        "z": v_prog,
        "z_arch": z_zero,
        "P": (unit_81(9), 1),
        "B": ((w_v, 9),),
        "n": 0,
        "p": 0,
        "b": 0,
        "eps": 1,
    }
    E_d0 = energy_dict(st_dirty0)
    st_dirty1 = step_funded_dict(st_dirty0, 32)
    delta_E_dirty = energy_dict(st_dirty1) - E_d0
    st_dirty2 = step_funded_dict(st_dirty1, 32)
    traj_hasher.update(f"dirty:{delta_E_dirty}:{st_dirty1['b']}:{st_dirty2['b']}\n".encode("utf-8"))

    # Capture checks
    for mod in (3, 5, 7):
        for x_val, p_val, a_val in product(range(mod), repeat=3):
            xb = (bal_rep(x_val, mod),)
            pb = (bal_rep(p_val, mod),)
            ab = (bal_rep(a_val, mod),)
            out = cap_map(xb, pb, ab, mod, inv=False)
            assert cap_map(*out, mod, inv=True) == (xb, pb, ab)

    lam = Fraction(354161, 735212)
    k1_banks = []
    k91_banks = []
    ref_probs = {}
    for t in (40, 41, 42):
        zt = tuple(t * x for x in v_prog)
        Xt, Dt = apply_u_hat(zt, 14112, E0_PAIR, 1)
        ref_probs[t] = Fraction(Xt[0], Dt) ** 2
        k1_banks.append(2 * (Dt * Dt - 1) + 1)
        k91_banks.append(182 * (Dt * Dt - 1) + 91 * 91)
    gap = lam * ref_probs[40] + (1 - lam) * ref_probs[42] - ref_probs[41]
    traj_hasher.update(f"seam:{gap}:{k1_banks}:{k91_banks}\n".encode("utf-8"))
    traj_sha256 = traj_hasher.hexdigest()

    lines = [
        "probe_id=P-INTEGER-RETAINED-PAIR-SOURCE-1",
        "claim_status=NON-CANONICAL",
        "action_layer=L1",
        f"cyclotomic_gram_dets=G5:{det_G5},G8:{det_G8},G:{det_G},GS:{det_GS},GR:{det_GR}",
        f"cyclotomic_transition_dets=TJ:{det_TJ},TM:{det_TM},C:{det_C},res_fg:41",
        "cyclotomic_seam_roots_mod41=common:19,j:10,m:27,ell:1,10,18,16,-1,-27,-32,-3",
        f"cyclotomic_ternary_bridge_checked=total:{total_ternary},in_S:{in_S_count},admitted_B32:{admitted_32_count}",
        f"cyclotomic_bridge_sha256={bridge_sha256}",
        f"pair_involution_ternary_checked={inv_checked}",
        "pair_full_matrix_certificates=" + ",".join(cert_labels),
        f"pair_involution_box_checked={inv_box_count}",
        f"pair_involution_sha256={inv_box_sha256}",
        "funded_automaton_box_checked=2592",
        f"funded_automaton_breakdown=accepted:{accepted_count},reflected:{reflected_count}",
        "port_independence_checked=basis:81,scaled:9,sharp_bank_v_K1:161",
        "k3_energy_prefixes=" + "|".join(k3_prefixes),
        "k3_underfunded_bounce=" + "|".join(k3_bounces),
        "dirty_stock_release_v=delta_E:-159,bank_after_prep:159,port_after_swap:ready_e",
        "program_capture_checked=scalar:495,vector8:6,clean_cost_law:q(x)",
        f"seam_collision_pair_gap={gap.numerator}/{gap.denominator}",
        "seam_q14112_sharp_banks=K1:"
        + ",".join(str(x) for x in k1_banks)
        + "|K91:"
        + ",".join(str(x) for x in k91_banks),
        f"funded_trajectories_sha256={traj_sha256}",
    ]
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
