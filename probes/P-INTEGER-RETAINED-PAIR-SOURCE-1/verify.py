#!/usr/bin/env python3
"""Formal verifier for P-INTEGER-RETAINED-PAIR-SOURCE-1.

NON-CANONICAL L1 probe. Uses only the Python standard library.
Implements:
1. Cyclotomic trace-form and index-3/41 seam coordinate bridge from (J, M)
   via 4-coordinate modular polynomial arithmetic in Z[j]/(Phi_5) and Z[m]/(m^4+1).
2. Universal division-free integer pair involution U_hat_z on C = Z^81 x Z_{>0}
   via rank-one dual inner products and integer certificate matrices N_z.
3. 2-phase funded reversible integer pair-source automaton with positive-definite
   energy E, conserved budget E + b, and port-independent sharp bank threshold.
4. Subprocess execution and byte-for-byte comparison against independent breaker.py.
"""
from fractions import Fraction
from functools import reduce
import hashlib
from itertools import product
from math import gcd, isqrt
from pathlib import Path
import subprocess
import sys


PROBE_DIR = Path(__file__).resolve().parent
ELL = (1, 10, 18, 16, -1, -27, -32, -3)
F_COEFFS = (1, -2, 4, -3, 1)   # 1 - 2x + 4x^2 - 3x^3 + x^4
G_COEFFS = (1, -4, 8, -4, 1)   # 1 - 4x + 8x^2 - 4x^3 + x^4


def gcd_list(vals) -> int:
    g = 0
    for v in vals:
        g = gcd(g, abs(int(v)))
    return g


def det_bareiss(mat) -> int:
    n = len(mat)
    a = [[int(x) for x in row] for row in mat]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap_row = None
            for r in range(k + 1, n):
                if a[r][k] != 0:
                    swap_row = r
                    break
            if swap_row is None:
                return 0
            a[k], a[swap_row] = a[swap_row], a[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[k][k] * a[i][j] - a[i][k] * a[k][j]
                if num % prev != 0:
                    raise AssertionError("Bareiss division not exact")
                a[i][j] = num // prev
            a[i][k] = 0
        prev = a[k][k]
    return sign * a[n - 1][n - 1]


def mat_mul(a, b):
    rows = len(a)
    cols = len(b[0])
    inner = len(b)
    out = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for k in range(inner):
            aik = a[i][k]
            if aik:
                for j in range(cols):
                    out[i][j] += aik * b[k][j]
    return out


def mat_transpose(a):
    return [list(col) for col in zip(*a)]


def o5_mul(a, b):
    """Multiply in Z[j]/(1 + j + j^2 + j^3 + j^4) in basis (1, j, j^2, j^3)."""
    c = [0] * 7
    for i in range(4):
        for k in range(4):
            c[i + k] += a[i] * b[k]
    # Reduce j^6 = j, j^5 = 1, j^4 = -1 - j - j^2 - j^3
    c[1] += c[6]
    c[0] += c[5]
    c4 = c[4]
    return (c[0] - c4, c[1] - c4, c[2] - c4, c[3] - c4)


def o5_conj(a):
    """Complex conjugate in Z[j]: j -> j^4 = -1 - j - j^2 - j^3, j^2 -> j^3, j^3 -> j^2."""
    a0, a1, a2, a3 = a
    return (a0 - a1, -a1, a3 - a1, a2 - a1)


def o5_trace(a) -> int:
    """Field trace Tr_{Q(j)/Q}(a) via multiplication matrix trace."""
    total = 0
    for r in range(4):
        basis = [0, 0, 0, 0]
        basis[r] = 1
        prod = o5_mul(a, tuple(basis))
        total += prod[r]
    return total


def o8_mul(a, b):
    """Multiply in Z[m]/(m^4 + 1) in basis (1, m, m^2, m^3)."""
    res = [0, 0, 0, 0]
    for i in range(4):
        for k in range(4):
            s = i + k
            if s < 4:
                res[s] += a[i] * b[k]
            else:
                res[s - 4] -= a[i] * b[k]
    return tuple(res)


def o8_conj(a):
    """Complex conjugate in Z[m]: m -> -m^3, m^2 -> -m^2, m^3 -> -m."""
    a0, a1, a2, a3 = a
    return (a0, -a3, -a2, -a1)


def o8_trace(a) -> int:
    """Field trace Tr_{Q(m)/Q}(a) via multiplication matrix trace."""
    total = 0
    for r in range(4):
        basis = [0, 0, 0, 0]
        basis[r] = 1
        prod = o8_mul(a, tuple(basis))
        total += prod[r]
    return total


def poly_mod_monic4(deg_k: int, coeffs4):
    """Return x^deg_k mod (c0 + c1 x + c2 x^2 + c3 x^3 + x^4) as 4-tuple."""
    c0, c1, c2, c3, _ = coeffs4
    v = [1, 0, 0, 0]
    for _ in range(deg_k):
        top = v[3]
        v = [-c0 * top, v[0] - c1 * top, v[1] - c2 * top, v[2] - c3 * top]
    return tuple(v)


def inv_TJ(a):
    a0, a1, a2, a3 = a
    c3 = a1 - a3
    c2 = -3 * a1 + 2 * a3
    c1 = 3 * a1 + a2 - 2 * a3
    c0 = a0 - a1 - a2
    return (c0, c1, c2, c3)


def inv_TM(b):
    b0, b1, b2, b3 = b
    num = -b1 + b2 + b3
    if num % 3 != 0:
        raise ValueError("b not in Lambda_3")
    s = num // 3
    c3 = 2 * s - b3
    c2 = 4 * b3 - 7 * s
    c1 = b1 - 2 * c2
    c0 = b0 - c1 + 5 * c3
    return (c0, c1, c2, c3)


def q_form(z) -> int:
    a = z[:4]
    b = z[4:]
    return 5 * sum(x * x for x in a) - sum(a) ** 2 + 4 * sum(x * x for x in b)


def is_in_S(z) -> bool:
    return (z[5] - z[6] - z[7]) % 3 == 0


def is_admitted(z, bound: int) -> bool:
    return is_in_S(z) and 0 < q_form(z) <= bound


def g0_apply(x):
    s = sum(x[1:5])
    return (x[0],) + tuple(5 * x[i] - s for i in range(1, 5)) + tuple(4 * x[i] for i in range(5, 9))


def pair_metric_apply(x):
    rows = [g0_apply(x[9 * i:9 * i + 9]) for i in range(9)]
    cols = [g0_apply([rows[i][j] for i in range(9)]) for j in range(9)]
    return tuple(cols[j][i] for i in range(9) for j in range(9))


def basis_81(idx: int):
    return tuple(1 if i == idx else 0 for i in range(81))


E_READY = basis_81(0)


def kron_9(u, v):
    return tuple(x * y for x in u for y in v)


def dot_vec(u, v) -> int:
    return sum(x * y for x, y in zip(u, v))


def m_content(X, D: int) -> int:
    return gcd(gcd_list(X), abs(int(D)))


def cell_energy(X, D: int) -> int:
    return dot_vec(X, pair_metric_apply(X)) + D * D


def compile_program(z, bound: int):
    active = is_admitted(z, bound)
    qz = q_form(z)
    Az = 1 + qz
    if not active:
        return {
            "z": tuple(z),
            "bound": bound,
            "active": False,
            "q": qz,
            "A": Az,
            "d": 1,
            "w": E_READY,
            "v": (0,) * 81,
            "r": (0,) * 81,
        }
    yz = (1,) + tuple(z)
    wz = kron_9(yz, yz)
    gyz = g0_apply(yz)
    dual_w = kron_9(gyz, gyz)
    vz = tuple(Az * e_i - w_i for e_i, w_i in zip(E_READY, wz))
    rz = tuple(Az * e_i - dw_i for e_i, dw_i in zip(E_READY, dual_w))
    return {
        "z": tuple(z),
        "bound": bound,
        "active": True,
        "q": qz,
        "A": Az,
        "d": Az * (Az - 1),
        "w": wz,
        "v": vz,
        "r": rz,
    }


def u_hat(z, bound: int, X, D: int):
    if D <= 0:
        raise ValueError("D must be positive")
    gate = compile_program(z, bound)
    if not gate["active"]:
        return (tuple(X), int(D))
    m = m_content(X, D)
    dz = gate["d"]
    vz = gate["v"]
    rz = gate["r"]
    rx = dot_vec(rz, X)
    Y = tuple(dz * x_i - rx * v_i for x_i, v_i in zip(X, vz))
    M = dz * D
    g = gcd(gcd_list(Y), M)
    return (tuple(m * (y_i // g) for y_i in Y), m * (M // g))


def n_matrix(gate):
    dz = gate["d"]
    vz = gate["v"]
    rz = gate["r"]
    return [[dz * (1 if i == j else 0) - vz[i] * rz[j] for j in range(81)] for i in range(81)]


def state_energy(u) -> int:
    z, z_arch, P, B, n, p = u
    return (
        1
        + q_form(z)
        + q_form(z_arch)
        + cell_energy(P[0], P[1])
        + sum(cell_energy(cell[0], cell[1]) for cell in B)
        + n * n
        + p * p
    )


def core_step(u, bound: int, eps: int):
    z, z_arch, P, B, n, p = u
    K = len(B)
    B_list = list(B)
    active = is_admitted(z, bound)
    if eps == 1:
        if p == 0:
            if active and 0 <= n < K:
                B_list[n] = u_hat(z, bound, B_list[n][0], B_list[n][1])
            return (z, z_arch, P, tuple(B_list), n, 1)
        if p == 1:
            P_new = P
            if active and 0 <= n < K:
                P_new, B_list[n] = B_list[n], P
            return (z, z_arch, P_new, tuple(B_list), n + 1, 0)
        raise ValueError("bad phase")
    if eps == -1:
        if p == 1:
            if active and 0 <= n < K:
                B_list[n] = u_hat(z, bound, B_list[n][0], B_list[n][1])
            return (z, z_arch, P, tuple(B_list), n, 0)
        if p == 0:
            n_prev = n - 1
            P_new = P
            if active and 0 <= n_prev < K:
                P_new, B_list[n_prev] = B_list[n_prev], P
            return (z, z_arch, P_new, tuple(B_list), n_prev, 1)
        raise ValueError("bad phase")
    raise ValueError("bad direction")


def funded_step(state, bound: int):
    u, b, eps = state
    u_next = core_step(u, bound, eps)
    b_next = b + state_energy(u) - state_energy(u_next)
    if b_next >= 0:
        return (u_next, b_next, eps)
    return (u, b, -eps)


def j_dir(state):
    u, b, eps = state
    return (u, b, -eps)


def funded_inv(state, bound: int):
    return j_dir(funded_step(j_dir(state), bound))


def bal_mod(val: int, mod: int) -> int:
    half = mod // 2
    r = (val + half) % mod - half
    return r


def capture_step(x_in, z_prog, z_arch, mod: int, inverse: bool = False):
    if not inverse:
        z_new = tuple(bal_mod(a + x, mod) for a, x in zip(z_arch, x_in))
        return (tuple(x_in), z_new, tuple(z_prog))
    z_arch_old = tuple(bal_mod(p - x, mod) for p, x in zip(z_prog, x_in))
    return (tuple(x_in), tuple(z_arch), z_arch_old)


def check_pre_pin_integrity():
    frozen = PROBE_DIR / "FROZEN.sha256"
    if not frozen.exists():
        raise AssertionError("Missing FROZEN.sha256")
    lines = [line.strip() for line in frozen.read_text(encoding="utf-8").splitlines() if line.strip()]
    seen = set()
    for line in lines:
        parts = line.split()
        if len(parts) != 2:
            raise AssertionError(f"Malformed FROZEN.sha256 line: {line}")
        expected_hex, rel_name = parts
        target = PROBE_DIR / rel_name
        actual_hex = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual_hex != expected_hex:
            raise AssertionError(f"Hash mismatch for {rel_name}: {actual_hex} != {expected_hex}")
        seen.add(rel_name)
    required = {"PREREG.md", "PROOF.md", "SOURCE.md", "verify.py", "breaker.py"}
    if seen != required:
        raise AssertionError(f"Unexpected FROZEN.sha256 file set: {seen}")


def run_all_checks():
    # 1. Cyclotomic trace-form and index-3/41 seam coordinate bridge
    J_powers = [(1, 0, 0, 0)]
    J_elem = (1, 0, 1, 0)
    for _ in range(4):
        J_powers.append(o5_mul(J_powers[-1], J_elem))
    # f(J) = J^4 - 3 J^3 + 4 J^2 - 2 J + 1 == 0
    f_J = tuple(
        J_powers[4][i] - 3 * J_powers[3][i] + 4 * J_powers[2][i] - 2 * J_powers[1][i] + J_powers[0][i]
        for i in range(4)
    )
    assert f_J == (0, 0, 0, 0), f"f(J) != 0: {f_J}"

    M_powers = [(1, 0, 0, 0)]
    M_elem = (1, 1, 1, 0)
    for _ in range(4):
        M_powers.append(o8_mul(M_powers[-1], M_elem))
    # g(M) = M^4 - 4 M^3 + 8 M^2 - 4 M + 1 == 0
    g_M = tuple(
        M_powers[4][i] - 4 * M_powers[3][i] + 8 * M_powers[2][i] - 4 * M_powers[1][i] + M_powers[0][i]
        for i in range(4)
    )
    assert g_M == (0, 0, 0, 0), f"g(M) != 0: {g_M}"

    T_J = [[J_powers[col][row] for col in range(4)] for row in range(4)]
    T_M = [[M_powers[col][row] for col in range(4)] for row in range(4)]
    det_TJ = det_bareiss(T_J)
    det_TM = det_bareiss(T_M)
    assert det_TJ == -1 and det_TM == -3

    G5 = [[o5_trace(o5_mul(tuple(1 if k == r else 0 for k in range(4)),
                           o5_conj(tuple(1 if k == s else 0 for k in range(4)))))
           for s in range(4)] for r in range(4)]
    G8 = [[o8_trace(o8_mul(tuple(1 if k == r else 0 for k in range(4)),
                           o8_conj(tuple(1 if k == s else 0 for k in range(4)))))
           for s in range(4)] for r in range(4)]
    assert G5 == [[4 if r == s else -1 for s in range(4)] for r in range(4)]
    assert G8 == [[4 if r == s else 0 for s in range(4)] for r in range(4)]
    det_G5 = det_bareiss(G5)
    det_G8 = det_bareiss(G8)
    assert det_G5 == 125 and det_G8 == 256

    G = [[G5[r][s] if r < 4 and s < 4 else (G8[r - 4][s - 4] if r >= 4 and s >= 4 else 0)
          for s in range(8)] for r in range(8)]
    det_G = det_bareiss(G)
    assert det_G == 32000

    T_JM = [[T_J[r][s] if r < 4 and s < 4 else (T_M[r - 4][s - 4] if r >= 4 and s >= 4 else 0)
             for s in range(8)] for r in range(8)]
    G_S = mat_mul(mat_transpose(T_JM), mat_mul(G, T_JM))
    det_GS = det_bareiss(G_S)
    assert det_GS == 288000

    # Reduction matrix C: R -> S in power bases (1..x^7) -> (1..J^3, 1..M^3)
    C_cols = []
    for k in range(8):
        col_f = poly_mod_monic4(k, F_COEFFS)
        col_g = poly_mod_monic4(k, G_COEFFS)
        C_cols.append(col_f + col_g)
    C_mat = mat_transpose(C_cols)
    det_C = abs(det_bareiss(C_mat))
    assert det_C == 41
    G_R = mat_mul(mat_transpose(C_mat), mat_mul(G_S, C_mat))
    det_GR = det_bareiss(G_R)
    assert det_GR == 484128000

    # Mod-41 unique root lifting
    common_roots = [
        x for x in range(41)
        if sum(F_COEFFS[k] * pow(x, k, 41) for k in range(5)) % 41 == 0
        and sum(G_COEFFS[k] * pow(x, k, 41) for k in range(5)) % 41 == 0
    ]
    assert common_roots == [19]
    j_roots = [
        x for x in range(41)
        if sum(pow(x, k, 41) for k in range(5)) % 41 == 0 and (1 + x * x) % 41 == 19
    ]
    m_roots = [
        x for x in range(41)
        if (pow(x, 4, 41) + 1) % 41 == 0 and (1 + x + x * x) % 41 == 19
    ]
    assert j_roots == [10] and m_roots == [27]
    ell_from_roots = tuple([pow(10, k, 41) for k in range(4)] + [-pow(27, k, 41) for k in range(4)])
    assert ell_from_roots == ELL

    # Verify all 6561 ternary vectors
    total_ternary = 0
    in_S_count = 0
    admitted_32_count = 0
    bridge_hasher = hashlib.sha256()
    for z in product((-1, 0, 1), repeat=8):
        total_ternary += 1
        if not is_in_S(z):
            continue
        in_S_count += 1
        cA = inv_TJ(z[:4])
        cB = inv_TM(z[4:])
        # Reconstruct via T_J and T_M
        rec_a = tuple(sum(T_J[r][k] * cA[k] for k in range(4)) for r in range(4))
        rec_b = tuple(sum(T_M[r][k] * cB[k] for k in range(4)) for r in range(4))
        assert rec_a == z[:4] and rec_b == z[4:]
        c_full = cA + cB
        q_pullback = sum(c_full[i] * G_S[i][j] * c_full[j] for i in range(8) for j in range(8))
        qz = q_form(z)
        assert q_pullback == qz
        u_eval = sum(cA[k] * pow(19, k, 41) for k in range(4)) % 41
        v_eval = sum(cB[k] * pow(19, k, 41) for k in range(4)) % 41
        seam_eval = (u_eval - v_eval) % 41
        ell_eval = sum(l_i * z_i for l_i, z_i in zip(ELL, z)) % 41
        assert seam_eval == ell_eval
        if 0 < qz <= 32:
            admitted_32_count += 1
        bridge_hasher.update(f"{z}:{cA}:{cB}:{qz}:{seam_eval}\n".encode("utf-8"))
    assert total_ternary == 6561 and in_S_count == 2187 and admitted_32_count == 2162
    bridge_sha256 = bridge_hasher.hexdigest()

    # 2. Universal integer pair involution U_hat_z and full integer certificates
    inv_checked = 0
    for z in product((-1, 0, 1), repeat=8):
        if not is_admitted(z, 32):
            continue
        gate = compile_program(z, 32)
        Az = gate["A"]
        wz = gate["w"]
        X1, D1 = u_hat(z, 32, E_READY, 1)
        assert (X1, D1) == (wz, Az)
        X2, D2 = u_hat(z, 32, X1, D1)
        assert (X2, D2) == (E_READY, 1)
        assert cell_energy(E_READY, 1) == 2
        assert cell_energy(X1, D1) == 2 * Az * Az
        assert cell_energy(X1, D1) - cell_energy(E_READY, 1) == 2 * gate["q"] * (gate["q"] + 2)
        inv_checked += 1
    assert inv_checked == 2162

    L_gram = mat_transpose([pair_metric_apply(basis_81(i)) for i in range(81)])
    e1_prog = (1, 0, 0, 0, 0, 0, 0, 0)
    v_prog = (1, 0, 0, 0, -1, 0, 0, 0)
    neg_v_prog = (-1, 0, 0, 0, 1, 0, 0, 0)
    dense_prog = (1, -1, 1, -1, 1, 1, 1, 0)
    bench_programs = [e1_prog, v_prog, neg_v_prog, dense_prog] + [
        tuple(t * x for x in v_prog) for t in (40, 41, 42)
    ]
    cert_labels = []
    for z in bench_programs:
        gate = compile_program(z, 14112)
        assert gate["active"]
        dz = gate["d"]
        N = n_matrix(gate)
        NN = mat_mul(N, N)
        assert NN == [[dz * dz * (1 if i == j else 0) for j in range(81)] for i in range(81)]
        NTLN = mat_mul(mat_transpose(N), mat_mul(L_gram, N))
        assert NTLN == [[dz * dz * L_gram[i][j] for j in range(81)] for i in range(81)]
        # Verify product density factorization (w w^T L) == (y y^T G_0) tensor (y y^T G_0)
        yz = (1,) + z
        gyz = g0_apply(yz)
        one_num = [[yz[i] * gyz[j] for j in range(9)] for i in range(9)]
        wz = gate["w"]
        lwz = pair_metric_apply(wz)
        for i, j, k, l in product(range(9), repeat=4):
            assert wz[9 * i + k] * lwz[9 * j + l] == one_num[i][j] * one_num[k][l]
        cert_labels.append(f"{gate['q']}:{gate['A']}:{dz}")

    # 600-element cell-program box
    w_e1 = compile_program(e1_prog, 32)["w"]
    w_v = compile_program(v_prog, 32)["w"]
    test_cells = [(basis_81(i), 1) for i in range(81)]
    test_cells += [(tuple(3 * x for x in basis_81(9 * r)), 3) for r in range(9)]
    for k_idx in (1, 9, 10, 40, 72, 80):
        b0 = basis_81(0)
        bk = basis_81(k_idx)
        test_cells.append((tuple(b0[i] + 2 * bk[i] for i in range(81)), 5))
    test_cells += [
        (w_e1, 5),
        (tuple(2 * x for x in w_e1), 10),
        (w_v, 9),
        (tuple(4 * x for x in w_v), 36),
    ]
    assert len(test_cells) == 100
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
            X1, D1 = u_hat(z, 32, X, D)
            X2, D2 = u_hat(z, 32, X1, D1)
            assert (X2, D2) == (X, D)
            assert m_content(X1, D1) == m_content(X, D)
            assert Fraction(dot_vec(X1, pair_metric_apply(X1)), D1 * D1) == Fraction(
                dot_vec(X, pair_metric_apply(X)), D * D
            )
            inv_box_count += 1
            inv_box_hasher.update(
                f"{z}:{D}:{D1}:{m_content(X, D)}:{cell_energy(X1, D1)}:{X1[0]}:{X1[1]}:{X1[9]}:{X1[80]}\n".encode(
                    "utf-8"
                )
            )
    assert inv_box_count == 600
    inv_box_sha256 = inv_box_hasher.hexdigest()

    # 3. Funded 2-phase integer automaton
    p_comb = (tuple(2 * basis_81(1)[i] + basis_81(80)[i] for i in range(81)), 3)
    ports = [(basis_81(0), 1), (basis_81(9), 1), p_comb]
    stocks = [
        ((basis_81(0), 1), (basis_81(0), 1)),
        ((basis_81(9), 1), (basis_81(0), 1)),
        ((w_v, 9), (basis_81(0), 1)),
    ]
    z_zero = (0,) * 8
    accepted_count = 0
    reflected_count = 0
    for z in (e1_prog, v_prog, z_zero):
        for P in ports:
            for B in stocks:
                for n in (-1, 0, 1, 2, 3, 4):
                    for p in (0, 1):
                        u = (z, z_zero, P, B, n, p)
                        for b in (0, 1, 49, 500):
                            for eps in (1, -1):
                                st = (u, b, eps)
                                st_next = funded_step(st, 32)
                                st_back = funded_inv(st_next, 32)
                                assert st_back == st
                                assert funded_step(funded_inv(st, 32), 32) == st
                                assert state_energy(st_next[0]) + st_next[1] == state_energy(u) + b
                                if st_next[2] == eps:
                                    accepted_count += 1
                                else:
                                    reflected_count += 1
    assert accepted_count + reflected_count == 2592

    # Port-independence across 81 basis ports + 9 scaled ports
    port_test_list = [(basis_81(i), 1) for i in range(81)]
    for r in range(9):
        b_a = basis_81(9 * r)
        b_b = basis_81((9 * r + 1) % 81)
        port_test_list.append((tuple(2 * b_a[i] + b_b[i] for i in range(81)), 3))
    for P0 in port_test_list:
        u0 = (v_prog, z_zero, P0, ((E_READY, 1),), 0, 0)
        # Sharp bank b_sharp(v, 1) = 161
        st = (u0, 161, 1)
        st1 = funded_step(st, 32)
        st2 = funded_step(st1, 32)
        assert st2[1] == 0 and st2[2] == 1
        assert st2[0][2] == (w_v, 9) and st2[0][3] == (P0,) and st2[0][4] == 1 and st2[0][5] == 0
        # Full reversal
        assert funded_inv(funded_inv(st2, 32), 32) == st
        # Underfunded bank 160 reflects on step 1
        st_under = funded_step((u0, 160, 1), 32)
        assert st_under == (u0, 160, -1)

    # K = 3 sharp and underfunded bounce trajectories
    traj_hasher = hashlib.sha256()
    k3_prefixes = []
    k3_bounces = []
    P0_ref = (basis_81(9), 1)
    B_ready_3 = ((E_READY, 1), (E_READY, 1), (E_READY, 1))
    for label, z in (("e1", e1_prog), ("v", v_prog), ("dense", dense_prog)):
        gate = compile_program(z, 32)
        Az = gate["A"]
        wz = gate["w"]
        b_sharp = 6 * (Az * Az - 1) + 9
        u0 = (z, z_zero, P0_ref, B_ready_3, 0, 0)
        E0 = state_energy(u0)
        st = (u0, b_sharp, 1)
        diffs = [0]
        for _ in range(6):
            st = funded_step(st, 32)
            assert st[2] == 1
            diffs.append(state_energy(st[0]) - E0)
        assert st[1] == 0
        assert st[0][2] == (wz, Az)
        assert st[0][3] == (P0_ref, (wz, Az), (wz, Az))
        assert st[0][4] == 3 and st[0][5] == 0
        # Reverse 6 steps
        st_rev = j_dir(st)
        for _ in range(6):
            st_rev = funded_step(st_rev, 32)
        assert j_dir(st_rev) == (u0, b_sharp, 1)
        k3_prefixes.append(f"{label}:" + ",".join(str(d) for d in diffs))

        # Underfunded by 1 unit: b0 = b_sharp - 1
        b_under = b_sharp - 1
        st_u = (u0, b_under, 1)
        forward_states = [st_u]
        for _ in range(5):
            st_u = funded_step(st_u, 32)
            assert st_u[2] == 1
            forward_states.append(st_u)
        assert st_u[1] == 3 and st_u[0][4] == 2 and st_u[0][5] == 1
        # 6th step reflects
        st_bounce = funded_step(st_u, 32)
        assert st_bounce == (st_u[0], 3, -1)
        # Next 5 steps unwind back to u0 with bank b_under and dir -1
        st_unwind = st_bounce
        for idx in range(4, -1, -1):
            st_unwind = funded_step(st_unwind, 32)
            assert st_unwind[0] == forward_states[idx][0]
            assert st_unwind[1] == forward_states[idx][1]
            assert st_unwind[2] == -1
        assert st_unwind == (u0, b_under, -1)
        k3_bounces.append(f"{label}:(b0:{b_under},step5_b:3,reflected,unwound)")
        traj_hasher.update(f"{label}:{diffs}:{b_sharp}:{b_under}\n".encode("utf-8"))

    # Dirty-stock energy release control
    u_dirty0 = (v_prog, z_zero, (basis_81(9), 1), ((w_v, 9),), 0, 0)
    E_dirty0 = state_energy(u_dirty0)
    st_dirty1 = funded_step((u_dirty0, 0, 1), 32)
    delta_E_dirty = state_energy(st_dirty1[0]) - E_dirty0
    assert delta_E_dirty == -159 and st_dirty1[1] == 159
    st_dirty2 = funded_step(st_dirty1, 32)
    assert st_dirty2[0][2] == (E_READY, 1) and st_dirty2[0][3] == ((basis_81(9), 1),)
    traj_hasher.update(f"dirty:{delta_E_dirty}:{st_dirty1[1]}:{st_dirty2[1]}\n".encode("utf-8"))

    # Funded program capture
    scalar_count = 0
    for mod in (3, 5, 7):
        for x_val, p_val, a_val in product(range(mod), repeat=3):
            xb = (bal_mod(x_val, mod),)
            pb = (bal_mod(p_val, mod),)
            ab = (bal_mod(a_val, mod),)
            out = capture_step(xb, pb, ab, mod, inverse=False)
            assert capture_step(*out, mod, inverse=True) == (xb, pb, ab)
            if ab == (0,):
                assert out == (xb, xb, pb)
            scalar_count += 1
    assert scalar_count == 495

    mod_14112 = 2 * isqrt(14112) + 1
    assert mod_14112 == 237
    vec_capture_progs = [e1_prog, v_prog, dense_prog] + [tuple(t * x for x in v_prog) for t in (40, 41, 42)]
    prior_z = (1, 1, 0, -1, 1, 1, 1, 0)
    for x_prog in vec_capture_progs:
        out = capture_step(x_prog, prior_z, z_zero, mod_14112, inverse=False)
        assert out == (x_prog, x_prog, prior_z)
        assert capture_step(*out, mod_14112, inverse=True) == (x_prog, prior_z, z_zero)
        delta_cap = (q_form(out[1]) + q_form(out[2])) - (q_form(prior_z) + q_form(z_zero))
        assert delta_cap == q_form(x_prog)

    # Opposite-seam collision and Q=14112, K=91 sharp banks
    lam = Fraction(354161, 735212)
    k1_banks = []
    k91_banks = []
    ref_probs = {}
    for t in (40, 41, 42):
        zt = tuple(t * x for x in v_prog)
        Xt, Dt = u_hat(zt, 14112, E_READY, 1)
        ref_probs[t] = Fraction(Xt[0], Dt) ** 2
        b1 = 2 * (Dt * Dt - 1) + 1
        b91 = 182 * (Dt * Dt - 1) + 91 * 91
        k1_banks.append(b1)
        k91_banks.append(b91)
    gap = lam * ref_probs[40] + (1 - lam) * ref_probs[42] - ref_probs[41]
    assert gap == Fraction(15936, 1210262180216419)
    assert k1_banks == [327731201, 361751201, 398353537]
    assert k91_banks == [29823547481, 32919367481, 36250180057]
    traj_hasher.update(f"seam:{gap}:{k1_banks}:{k91_banks}\n".encode("utf-8"))
    traj_sha256 = traj_hasher.hexdigest()

    return [
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


def main():
    check_pre_pin_integrity()
    lines = run_all_checks()
    proc = subprocess.run(
        [sys.executable, "-I", str(PROBE_DIR / "breaker.py")],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise AssertionError(f"breaker.py failed (rc={proc.returncode}): {proc.stderr}")
    if proc.stderr:
        raise AssertionError(f"breaker.py emitted stderr: {proc.stderr}")
    breaker_lines = proc.stdout.splitlines()
    if breaker_lines != lines:
        raise AssertionError(f"breaker.py mismatch:\n{breaker_lines}\n!=\n{lines}")
    for line in lines:
        print(line)
    print("independent_breaker_match=PASS")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
