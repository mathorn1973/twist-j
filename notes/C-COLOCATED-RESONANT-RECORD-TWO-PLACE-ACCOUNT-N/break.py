#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Independent cyclic-convolution and matrix-trace checker (break.py)
for C-COLOCATED-RESONANT-RECORD-TWO-PLACE-ACCOUNT-N.

Representation: 5-component cyclic group ring Z[C_5] = (c0, c1, c2, c3, c4)
modulo the diagonal ideal Z*(1, 1, 1, 1, 1), pure 5-cyclic convolution,
autocorrelation extraction A(v) = p0 - p1, B(v) = p1 - p2, 4x4 rational
multiplication matrix trace/determinant checks, and unreduced loaded contact
displacement d = (2v - x - e_v + F) / 4.
Standard library only; exact int and Fraction arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
import itertools
import math
import sys

Cyc5 = tuple[int, int, int, int, int]
Phi2 = tuple[int, int]  # A + B * phi

ZERO5: Cyc5 = (0, 0, 0, 0, 0)
ONE5: Cyc5 = (1, 0, 0, 0, 0)
J1_5: Cyc5 = (0, 1, 0, 0, 0)
RHO5: Cyc5 = (0, 0, 1, 0, 0)  # j^2
J4_5: Cyc5 = (0, 0, 0, 0, 1)  # j^4
PHI5: Cyc5 = (0, 0, -1, -1, 0)  # -j^2 - j^3
CAP_J5: Cyc5 = (1, 0, 1, 0, 0)  # 1 + j^2
CAP_J_INV5: Cyc5 = (0, -1, -1, 0, 0)  # -j - j^2
THREE_PLUS_RHO5: Cyc5 = (3, 0, 1, 0, 0)
ONE_MINUS_RHO5: Cyc5 = (1, 0, -1, 0, 0)
ONE_MINUS_J4_5: Cyc5 = (1, 0, 0, 0, -1)


def from_vec4(v: tuple[int, int, int, int]) -> Cyc5:
    return (v[0], v[1], v[2], v[3], 0)


def c_eq(a: Cyc5, b: Cyc5) -> bool:
    d0 = a[0] - b[0]
    return (
        (a[1] - b[1] == d0)
        and (a[2] - b[2] == d0)
        and (a[3] - b[3] == d0)
        and (a[4] - b[4] == d0)
    )


def c_list_eq(la: list[Cyc5], lb: list[Cyc5]) -> bool:
    return len(la) == len(lb) and all(c_eq(x, y) for x, y in zip(la, lb))


def c_add(a: Cyc5, b: Cyc5) -> Cyc5:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4])


def c_sub(a: Cyc5, b: Cyc5) -> Cyc5:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3], a[4] - b[4])


def c_neg(a: Cyc5) -> Cyc5:
    return (-a[0], -a[1], -a[2], -a[3], -a[4])


def c_scale(k: int, a: Cyc5) -> Cyc5:
    return (k * a[0], k * a[1], k * a[2], k * a[3], k * a[4])


def c_mul(a: Cyc5, b: Cyc5) -> Cyc5:
    out = [0, 0, 0, 0, 0]
    for r in range(5):
        ar = a[r]
        if ar:
            for s in range(5):
                bs = b[s]
                if bs:
                    out[(r + s) % 5] += ar * bs
    return (out[0], out[1], out[2], out[3], out[4])


def c_pow(a: Cyc5, exp: int) -> Cyc5:
    res = ONE5
    base = a
    e = exp
    while e > 0:
        if e & 1:
            res = c_mul(res, base)
        base = c_mul(base, base)
        e >>= 1
    return res


def c_conj(a: Cyc5) -> Cyc5:
    return (a[0], a[4], a[3], a[2], a[1])


def c_div_m_exact(a: Cyc5, m: int) -> Cyc5 | None:
    rem = a[0] % m
    if (
        (a[1] % m != rem)
        or (a[2] % m != rem)
        or (a[3] % m != rem)
        or (a[4] % m != rem)
    ):
        return None
    return (
        (a[0] - rem) // m,
        (a[1] - rem) // m,
        (a[2] - rem) // m,
        (a[3] - rem) // m,
        (a[4] - rem) // m,
    )


def c_in_2o(a: Cyc5) -> bool:
    r = a[0] & 1
    return (
        ((a[1] & 1) == r)
        and ((a[2] & 1) == r)
        and ((a[3] & 1) == r)
        and ((a[4] & 1) == r)
    )


def c_eps_mod5(a: Cyc5) -> int:
    # Augmentation j -> 1 on quotient by (1,1,1,1,1)
    return ((a[0] - a[4]) + (a[1] - a[4]) + (a[2] - a[4]) + (a[3] - a[4])) % 5


def h_pair_cyclic(v: Cyc5) -> Phi2:
    p = c_mul(v, c_conj(v))
    # By conjugate symmetry in Z[C_5], p[1] == p[4] and p[2] == p[3]
    if p[1] != p[4] or p[2] != p[3]:
        raise AssertionError(f"Non-Hermitian autocorrelation: {p}")
    return (p[0] - p[1], p[1] - p[2])


def mul_matrix_4x4(v: Cyc5) -> list[list[int]]:
    """Construct the 4x4 multiplication matrix of v on power basis (1, j, j^2, j^3)."""
    cols: list[tuple[int, int, int, int]] = []
    for k in range(4):
        basis_k = [0, 0, 0, 0, 0]
        basis_k[k] = 1
        prod = c_mul(v, (basis_k[0], basis_k[1], basis_k[2], basis_k[3], basis_k[4]))
        c4 = prod[4]
        cols.append((prod[0] - c4, prod[1] - c4, prod[2] - c4, prod[3] - c4))
    return [[cols[col][row] for col in range(4)] for row in range(4)]


def mat4_trace(m: list[list[int]]) -> int:
    return m[0][0] + m[1][1] + m[2][2] + m[3][3]


def mat4_det(m: list[list[int]]) -> int:
    a = [[Fraction(val, 1) for val in row] for row in m]
    sign = 1
    for i in range(4):
        pivot = i
        while pivot < 4 and a[pivot][i] == 0:
            pivot += 1
        if pivot == 4:
            return 0
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            sign = -sign
        piv_val = a[i][i]
        for r in range(i + 1, 4):
            factor = a[r][i] / piv_val
            for c in range(i, 4):
                a[r][c] -= factor * a[i][c]
    det_f = Fraction(sign, 1)
    for i in range(4):
        det_f *= a[i][i]
    if det_f.denominator != 1:
        raise AssertionError("Non-integral determinant")
    return det_f.numerator


def phi_add(p: Phi2, q: Phi2) -> Phi2:
    return (p[0] + q[0], p[1] + q[1])


def phi_scale(k: int, p: Phi2) -> Phi2:
    return (k * p[0], k * p[1])


def phi_mul(p: Phi2, q: Phi2) -> Phi2:
    a, b = p
    c, d = q
    return (a * c + b * d, a * d + b * c + b * d)


def phi_conj(p: Phi2) -> Phi2:
    return (p[0] + p[1], -p[1])


def phi_trace(p: Phi2) -> int:
    return 2 * p[0] + p[1]


def phi_norm(p: Phi2) -> int:
    a, b = p
    return a * a + a * b - b * b


def q_norm(v: Cyc5) -> int:
    p = c_mul(v, c_conj(v))
    # Full K/Q trace is 4*p0 - (p1+p2+p3+p4); Q(v) is half the full trace
    full_tr = 4 * p[0] - (p[1] + p[2] + p[3] + p[4])
    if full_tr & 1:
        raise AssertionError("Odd full K/Q trace")
    return full_tr // 2


def unreduced_loaded_step(
    x: Cyc5, b_slots: list[Cyc5], f_field: Cyc5, idx: int
) -> tuple[Cyc5, list[Cyc5], Cyc5, bool, Cyc5, Phi2]:
    """Apply the unreduced loaded contact law d = (2v - x - e_v + F) / 4 with e_v = 0."""
    v = b_slots[idx]
    num = c_add(c_sub(c_scale(2, v), x), f_field)
    d = c_div_m_exact(num, 4)
    new_b = list(b_slots)
    if d is None:
        return x, new_b, f_field, False, ZERO5, (0, 0)
    curr = c_mul(c_sub(RHO5, ONE5), d)
    x_next = c_sub(x, curr)
    v_next = c_add(v, curr)
    f_next = c_add(f_field, curr)
    new_b[idx] = v_next
    return x_next, new_b, f_next, True, curr, h_pair_cyclic(d)


def check_cut_invariants(
    x: Cyc5,
    b_slots: list[Cyc5],
    f_field: Cyc5,
    init_sum: Cyc5,
    init_eps: list[int],
    init_q_full: int,
    init_h_full: Phi2,
) -> int:
    checks = 0
    if not c_eq(c_add(f_field, x), ZERO5):
        raise AssertionError("Gauss A violation in break.py")
    checks += 1
    b_sum = ZERO5
    for s in b_slots:
        b_sum = c_add(b_sum, s)
    if not c_eq(c_sub(f_field, b_sum), ZERO5):
        raise AssertionError("Gauss B violation in break.py")
    checks += 1
    if not c_eq(c_add(x, b_sum), init_sum):
        raise AssertionError("Slot sum violation in break.py")
    checks += 1
    cur_eps = [c_eps_mod5(x)] + [c_eps_mod5(s) for s in b_slots]
    if cur_eps != init_eps:
        raise AssertionError("Residue mod 5 violation in break.py")
    checks += 1
    q_full = 2 * (q_norm(x) + sum(q_norm(s) for s in b_slots))
    if q_full != init_q_full:
        raise AssertionError("Scalar account violation in break.py")
    checks += 1
    h_sum = h_pair_cyclic(x)
    for s in b_slots:
        h_sum = phi_add(h_sum, h_pair_cyclic(s))
    h_full = phi_scale(2, h_sum)
    if h_full != init_h_full:
        raise AssertionError("Hermitian account violation in break.py")
    checks += 1
    return checks


def main() -> int:
    total_assertions = 0

    # =========================================================================
    # A1: Two-place Galois/Hermitian account and conjugate trace decomposition
    # =========================================================================
    a1_assertions = 0
    if not c_eq(c_mul(CAP_J5, CAP_J_INV5), ONE5):
        raise AssertionError("J * J^-1 != 1 in Z[C_5]")
    a1_assertions += 1

    h_1mr = h_pair_cyclic(ONE_MINUS_RHO5)
    h_1mj4 = h_pair_cyclic(ONE_MINUS_J4_5)
    h_j = h_pair_cyclic(CAP_J5)
    h_3pr = h_pair_cyclic(THREE_PLUS_RHO5)

    if h_1mr != (2, 1) or phi_trace(h_1mr) != 5 or phi_norm(h_1mr) != 5:
        raise AssertionError("Bad h(1-j^2)")
    if h_1mj4 != (3, -1) or phi_trace(h_1mj4) != 5 or phi_norm(h_1mj4) != 5:
        raise AssertionError("Bad h(1-j^4)")
    if phi_conj(h_1mr) != h_1mj4 or phi_mul(h_1mr, h_1mj4) != (5, 0):
        raise AssertionError("Galois conjugate / norm failure")
    if h_j != (2, -1) or phi_trace(h_j) != 3 or phi_norm(h_j) != 1:
        raise AssertionError("Bad h(J)")
    if h_3pr != (10, -3) or phi_trace(h_3pr) != 17 or phi_norm(h_3pr) != 61:
        raise AssertionError("Bad h(3+rho)")
    if phi_add(phi_scale(4, h_j), h_1mr) != h_3pr:
        raise AssertionError("4 h(J) + h(1-rho) != h(3+rho)")
    a1_assertions += 6

    grid_2: list[Cyc5] = [
        from_vec4((c0, c1, c2, c3))
        for c0, c1, c2, c3 in itertools.product((-2, -1, 0, 1, 2), repeat=4)
    ]
    b0_count = 0
    for c in grid_2:
        vv_bar = c_mul(c, c_conj(c))
        ac, bc = h_pair_cyclic(c)
        if not c_eq(vv_bar, c_add(c_scale(ac, ONE5), c_scale(bc, PHI5))):
            raise AssertionError("v*vbar != A + B*phi")
        qc = q_norm(c)
        nc = phi_norm((ac, bc))
        # Independent 4x4 matrix trace and determinant checks
        mat_vv = mul_matrix_4x4(vv_bar)
        mat_c = mul_matrix_4x4(c)
        if mat4_trace(mat_vv) != 2 * qc or qc != 2 * ac + bc:
            raise AssertionError("4x4 matrix trace != 2 Q(c)")
        if mat4_det(mat_c) != nc:
            raise AssertionError("4x4 matrix det != N(h(c))")
        if (c_eq(c, ZERO5) and (qc != 0 or nc != 0)) or (
            (not c_eq(c, ZERO5)) and (qc <= 0 or nc <= 0)
        ):
            raise AssertionError("Positivity failure")

        c_1mr = c_mul(ONE_MINUS_RHO5, c)
        c_1mj4 = c_mul(ONE_MINUS_J4_5, c)
        h_c_1mr = h_pair_cyclic(c_1mr)
        h_c_1mj4 = h_pair_cyclic(c_1mj4)
        if h_c_1mr != (2 * ac + bc, ac + 3 * bc):
            raise AssertionError("h((1-j^2)c) mismatch")
        if h_c_1mj4 != (3 * ac - bc, 2 * bc - ac):
            raise AssertionError("h((1-j^4)c) mismatch")

        q_1mr = q_norm(c_1mr)
        q_1mj4 = q_norm(c_1mj4)
        if q_1mr != 5 * (ac + bc) or q_1mj4 != 5 * ac:
            raise AssertionError("Trace formula mismatch")
        if q_1mr + q_1mj4 != 5 * qc:
            raise AssertionError("Conjugate trace sum != 5 Q(c)")
        if (q_1mr == q_1mj4) != (bc == 0):
            raise AssertionError("Equality condition B_c == 0 failed")
        if bc == 0:
            b0_count += 1
            if 2 * q_1mr != 5 * qc:
                raise AssertionError("B_c == 0 ratio failure")
        if phi_scale(5, (ac, bc)) != phi_mul(h_1mj4, h_c_1mr):
            raise AssertionError("Current-to-displacement conversion failed")
        a1_assertions += 10

    if (
        q_norm(ONE_MINUS_RHO5) != 5
        or q_norm(ONE_MINUS_J4_5) != 5
        or q_norm(c_mul(ONE_MINUS_RHO5, ONE_MINUS_RHO5)) != 15
        or q_norm(c_mul(ONE_MINUS_RHO5, ONE_MINUS_J4_5)) != 10
    ):
        raise AssertionError("Counterexample pair (c1, c2) failed")
    a1_assertions += 1
    total_assertions += a1_assertions

    # =========================================================================
    # A2: Iff resonance theorem for the 2-contact returning selector
    # =========================================================================
    a2_assertions = 0
    grid_1: list[Cyc5] = [
        from_vec4((c0, c1, c2, c3))
        for c0, c1, c2, c3 in itertools.product((-1, 0, 1), repeat=4)
    ]
    nonzero_1 = [c for c in grid_1 if not c_eq(c, ZERO5)]

    if c_eq(
        c_add(ONE5, c_add(ONE5, c_scale(2, ONE5))),
        c_add(c_scale(3, ONE5), ONE_MINUS_RHO5),
    ):
        raise AssertionError("Slot-sum counterexample (1,1) failed")
    a2_assertions += 1

    resonant_in_grid1 = 0
    a2_cuts_checked = 0
    for a in grid_1:
        for c in nonzero_1:
            is_res = c_eq(a, c_mul(CAP_J5, c))
            lhs_sum = c_add(c_scale(2, a), c_scale(2, c))
            rhs_sum = c_add(c_scale(3, a), c_mul(ONE_MINUS_RHO5, c))
            if c_eq(lhs_sum, rhs_sum) != is_res:
                raise AssertionError("3-slot sum iff failed")
            a2_assertions += 1

            h0 = c_add(a, c_scale(2, c))
            z0 = ZERO5
            u_comp = c_neg(c_add(a, h0))
            x0 = a
            f0 = c_neg(a)
            b0 = [h0, z0, u_comp]
            init_sum = c_add(x0, c_add(h0, c_add(z0, u_comp)))
            init_eps = [c_eps_mod5(x0)] + [c_eps_mod5(s) for s in b0]
            init_q = 2 * (q_norm(x0) + sum(q_norm(s) for s in b0))
            init_h = phi_scale(
                2,
                phi_add(
                    h_pair_cyclic(x0),
                    phi_add(
                        h_pair_cyclic(h0),
                        phi_add(h_pair_cyclic(z0), h_pair_cyclic(u_comp)),
                    ),
                ),
            )

            x1, b1, f1, adm1, _, area1 = unreduced_loaded_step(x0, b0, f0, 0)
            a2_assertions += check_cut_invariants(
                x1, b1, f1, init_sum, init_eps, init_q, init_h
            )
            a2_cuts_checked += 1
            if not adm1 or not c_eq(x1, c_add(a, c_mul(ONE_MINUS_RHO5, c))):
                raise AssertionError("Step 1 admission/state mismatch")
            a2_assertions += 1

            x2, b2, f2, adm2, _, area2 = unreduced_loaded_step(x1, b1, f1, 1)
            a2_assertions += check_cut_invariants(
                x2, b2, f2, init_sum, init_eps, init_q, init_h
            )
            a2_cuts_checked += 1

            returned_and_admitted = adm2 and c_eq(x2, a) and c_eq(f2, f0)
            if returned_and_admitted != is_res:
                raise AssertionError("Resonance iff failed")
            a2_assertions += 1

            if is_res:
                resonant_in_grid1 += 1
                if (
                    not c_eq(x1, c_scale(2, c))
                    or not c_eq(b2[0], c_scale(2, a))
                    or not c_eq(b2[1], c_mul(ONE_MINUS_RHO5, c))
                    or phi_add(area1, area2) != phi_scale(2, h_pair_cyclic(c))
                ):
                    raise AssertionError("Resonant state/area mismatch")
                a2_assertions += 1

            xi, bi, fi = x2, b2, f2
            for idx in (1, 1, 1, 1, 0, 0, 0, 0):
                xi, bi, fi, _, _, _ = unreduced_loaded_step(xi, bi, fi, idx)
                a2_assertions += check_cut_invariants(
                    xi, bi, fi, init_sum, init_eps, init_q, init_h
                )
                a2_cuts_checked += 1
            if not (c_eq(xi, x0) and c_list_eq(bi, b0) and c_eq(fi, f0)):
                raise AssertionError("8-contact inverse failed")
            a2_assertions += 1

    for c in grid_2:
        if c_eq(c, ZERO5):
            continue
        a = c_mul(CAP_J5, c)
        h0 = c_mul(THREE_PLUS_RHO5, c)
        if not c_eq(h0, c_add(a, c_scale(2, c))):
            raise AssertionError("h0 != (3+rho)c")
        x1, b1, f1, adm1, _, area1 = unreduced_loaded_step(
            a, [h0, ZERO5, c_neg(c_add(a, h0))], c_neg(a), 0
        )
        x2, b2, f2, adm2, _, area2 = unreduced_loaded_step(x1, b1, f1, 1)
        if not (adm1 and adm2):
            raise AssertionError("Resonant pair refused in grid_2")
        if not (c_eq(x1, c_scale(2, c)) and c_eq(x2, a) and c_eq(f2, c_neg(a))):
            raise AssertionError("Resonant trajectory failure in grid_2")
        if not (
            c_eq(b2[0], c_scale(2, a)) and c_eq(b2[1], c_mul(ONE_MINUS_RHO5, c))
        ):
            raise AssertionError("Resonant output slots failure in grid_2")
        ac, bc = h_pair_cyclic(c)
        if phi_add(h_pair_cyclic(b2[0]), h_pair_cyclic(b2[1])) != h_pair_cyclic(h0):
            raise AssertionError("Pointwise Hermitian partition failed")
        if (
            q_norm(h0) != 17 * ac + bc
            or q_norm(b2[0]) != 12 * ac - 4 * bc
            or q_norm(b2[1]) != 5 * (ac + bc)
            or phi_add(area1, area2) != (2 * ac, 2 * bc)
        ):
            raise AssertionError("Trace/area formula mismatch in grid_2")
        a2_assertions += 6

    total_assertions += a2_assertions

    # =========================================================================
    # A3: F_16 inertness and 5-phase one-hot selectivity iff c notin 2O
    # =========================================================================
    a3_assertions = 0
    cosets_mod2 = [
        from_vec4((b0, b1, b2, b3))
        for b0, b1, b2, b3 in itertools.product((0, 1), repeat=4)
    ]
    nonzero_cosets = [u for u in cosets_mod2 if not c_eq(u, ZERO5)]
    for u in nonzero_cosets:
        for v in nonzero_cosets:
            if c_in_2o(c_mul(u, v)):
                raise AssertionError("Zero divisor in O/2O")
            a3_assertions += 1

    rho_pows = [c_pow(RHO5, k) for k in range(5)]
    c_1957: Cyc5 = from_vec4((-1, -2, -2, 0))
    odd_seeds: list[Cyc5] = nonzero_1 + [c_1957]
    even_seeds: list[Cyc5] = [c_scale(2, c) for c in odd_seeds]
    all_bank_seeds = odd_seeds + even_seeds

    odd_onehot_pass = 0
    even_onehot_fail = 0
    a3_cuts_checked = 0

    for c in all_bank_seeds:
        c_is_odd = not c_in_2o(c)
        ac, bc = h_pair_cyclic(c)
        seed_all_m_onehot = True

        for m in range(5):
            a_m = c_mul(c_mul(CAP_J5, c), rho_pows[m])
            b_slots: list[Cyc5] = []
            for k in range(5):
                hk = c_mul(c_mul(THREE_PLUS_RHO5, c), rho_pows[k])
                zk = ZERO5
                uk = c_neg(hk)
                b_slots.extend([hk, zk, uk])
            b_slots.append(c_neg(a_m))

            x_cur = a_m
            f_cur = c_neg(a_m)
            init_b = list(b_slots)
            b_sum0 = ZERO5
            for s in b_slots:
                b_sum0 = c_add(b_sum0, s)
            init_sum = c_add(x_cur, b_sum0)
            init_eps = [c_eps_mod5(x_cur)] + [c_eps_mod5(s) for s in b_slots]
            init_q = 2 * (q_norm(x_cur) + sum(q_norm(s) for s in b_slots))
            h_acc = h_pair_cyclic(x_cur)
            for s in b_slots:
                h_acc = phi_add(h_acc, h_pair_cyclic(s))
            init_h = phi_scale(2, h_acc)

            adm_flags: list[bool] = []
            path_area: Phi2 = (0, 0)
            for k in range(5):
                x_cur, b_slots, f_cur, adm_h, _, ar_h = unreduced_loaded_step(
                    x_cur, b_slots, f_cur, 3 * k
                )
                a3_assertions += check_cut_invariants(
                    x_cur, b_slots, f_cur, init_sum, init_eps, init_q, init_h
                )
                a3_cuts_checked += 1
                adm_flags.append(adm_h)
                path_area = phi_add(path_area, ar_h)

                x_cur, b_slots, f_cur, adm_z, _, ar_z = unreduced_loaded_step(
                    x_cur, b_slots, f_cur, 3 * k + 1
                )
                a3_assertions += check_cut_invariants(
                    x_cur, b_slots, f_cur, init_sum, init_eps, init_q, init_h
                )
                a3_cuts_checked += 1
                adm_flags.append(adm_z)
                path_area = phi_add(path_area, ar_z)

            m_onehot = c_eq(x_cur, a_m) and c_eq(f_cur, c_neg(a_m))
            for k in range(5):
                hk_out = b_slots[3 * k]
                zk_out = b_slots[3 * k + 1]
                if k == m:
                    exp_h = c_scale(2, a_m)
                    exp_z = c_mul(c_mul(ONE_MINUS_RHO5, c), rho_pows[m])
                    if (
                        not c_eq(hk_out, exp_h)
                        or not c_eq(zk_out, exp_z)
                        or not (adm_flags[2 * k] and adm_flags[2 * k + 1])
                    ):
                        m_onehot = False
                else:
                    if (
                        not c_eq(hk_out, init_b[3 * k])
                        or not c_eq(zk_out, ZERO5)
                        or adm_flags[2 * k]
                        or adm_flags[2 * k + 1]
                    ):
                        m_onehot = False

            if c_is_odd:
                if not m_onehot:
                    raise AssertionError("Odd seed failed one-hot")
                if (
                    h_pair_cyclic(b_slots[3 * m + 1]) != phi_mul((2, 1), (ac, bc))
                    or q_norm(b_slots[3 * m + 1]) != 5 * (ac + bc)
                    or path_area != (2 * ac, 2 * bc)
                ):
                    raise AssertionError("Odd seed quantum/area mismatch")
                a3_assertions += 2
            else:
                if m == 1:
                    if not adm_flags[0] or c_eq(b_slots[0], init_b[0]):
                        raise AssertionError("Even seed failed Theorem 3 converse")
                    a3_assertions += 1
                if not m_onehot:
                    seed_all_m_onehot = False

            for k in range(4, -1, -1):
                for idx in (
                    3 * k + 1,
                    3 * k + 1,
                    3 * k + 1,
                    3 * k + 1,
                    3 * k,
                    3 * k,
                    3 * k,
                    3 * k,
                ):
                    x_cur, b_slots, f_cur, _, _, _ = unreduced_loaded_step(
                        x_cur, b_slots, f_cur, idx
                    )
                    a3_assertions += check_cut_invariants(
                        x_cur, b_slots, f_cur, init_sum, init_eps, init_q, init_h
                    )
                    a3_cuts_checked += 1
            if not (
                c_eq(x_cur, a_m)
                and c_list_eq(b_slots, init_b)
                and c_eq(f_cur, c_neg(a_m))
            ):
                raise AssertionError("40-contact bank inverse failed")
            a3_assertions += 1

        if c_is_odd and seed_all_m_onehot:
            odd_onehot_pass += 1
        elif (not c_is_odd) and (not seed_all_m_onehot):
            even_onehot_fail += 1
        else:
            raise AssertionError("Iff selectivity violation")
        a3_assertions += 1

    total_assertions += a3_assertions

    # =========================================================================
    # A4: Exact instantiation of PR #1957 35-quantum
    # =========================================================================
    a4_assertions = 0
    if not c_eq(c_mul(ONE_MINUS_RHO5, CAP_J_INV5), c_1957) or c_in_2o(c_1957):
        raise AssertionError("c_1957 derivation failed")
    if h_pair_cyclic(c_1957) != (3, 4) or q_norm(c_1957) != 10:
        raise AssertionError("h(c_1957) != 3 + 4*phi or Q != 10")
    a4_assertions += 2

    for k in range(5):
        ck = c_mul(c_1957, rho_pows[k])
        ak = c_mul(CAP_J5, ck)
        h0k = c_mul(THREE_PLUS_RHO5, ck)
        h1k = c_scale(2, ak)
        z2k = c_mul(ONE_MINUS_RHO5, ck)
        if (
            h_pair_cyclic(ak) != (2, 1)
            or q_norm(ak) != 5
            or h_pair_cyclic(h0k) != (18, 19)
            or q_norm(h0k) != 55
            or h_pair_cyclic(h1k) != (8, 4)
            or q_norm(h1k) != 20
            or h_pair_cyclic(z2k) != (10, 15)
            or q_norm(z2k) != 35
            or phi_scale(2, h_pair_cyclic(ck)) != (6, 8)
        ):
            raise AssertionError("PR #1957 values mismatch")
        a4_assertions += 1

    a0_p35 = ONE_MINUS_RHO5
    a1_p27 = c_mul(ONE_MINUS_RHO5, rho_pows[4])
    c0_port = c_1957
    c1_port = c_mul(c_1957, rho_pows[4])
    h0_port = c_mul(THREE_PLUS_RHO5, c0_port)
    h1_port = c_mul(THREE_PLUS_RHO5, c1_port)

    for label, sig, expected_q_pair in (
        ("P27", a1_p27, (0, 35)),
        ("P35", a0_p35, (35, 0)),
    ):
        b_port = [
            h0_port,
            ZERO5,
            c_neg(h0_port),
            h1_port,
            ZERO5,
            c_neg(h1_port),
            c_neg(sig),
        ]
        xp = sig
        fp = c_neg(sig)
        port_area: Phi2 = (0, 0)
        for idx in (0, 1, 3, 4):
            xp, b_port, fp, _, _, ar = unreduced_loaded_step(xp, b_port, fp, idx)
            port_area = phi_add(port_area, ar)
        got_q_pair = (q_norm(b_port[1]), q_norm(b_port[4]))
        if (
            not c_eq(xp, sig)
            or not c_eq(fp, c_neg(sig))
            or got_q_pair != expected_q_pair
            or port_area != (6, 8)
            or phi_trace(port_area) != 20
        ):
            raise AssertionError(f"PR #1957 port check failed for {label}")
        a4_assertions += 1

    total_assertions += a4_assertions

    # =========================================================================
    # A5: Conditional closure of the work-to-count identity (9a)
    # =========================================================================
    a5_assertions = 0
    profiles: list[tuple[int, int, int, int, int]] = [
        (1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0),
        (0, 0, 0, 0, 1),
        (1, 1, 0, 0, 0),
        (2, 0, 3, 0, 1),
        (4, 4, 4, 4, 4),
        (7, 3, 0, 2, 1),
        (11, 5, 2, 0, 7),
        (3, 1, 4, 1, 5),
        (9, 2, 6, 5, 3),
    ]
    a5_channel_checks = 0
    for c in odd_seeds:
        ac, bc = h_pair_cyclic(c)
        w0 = 5 * (ac + bc)
        h_rec_unit = phi_mul((2, 1), (ac, bc))
        channel_quanta: list[int] = []
        channel_h: list[Phi2] = []
        for m in range(5):
            a_m = c_mul(c_mul(CAP_J5, c), rho_pows[m])
            h_m = c_mul(c_mul(THREE_PLUS_RHO5, c), rho_pows[m])
            x1, b1, f1, adm1, _, _ = unreduced_loaded_step(
                a_m, [h_m, ZERO5, c_neg(h_m), c_neg(a_m)], c_neg(a_m), 0
            )
            x2, b2, f2, adm2, _, _ = unreduced_loaded_step(x1, b1, f1, 1)
            if not (adm1 and adm2 and c_eq(x2, a_m) and c_eq(f2, c_neg(a_m))):
                raise AssertionError("Single-channel arrival failed in A5")
            channel_quanta.append(q_norm(b2[1]))
            channel_h.append(h_pair_cyclic(b2[1]))
            a5_assertions += 1

        if any(q != w0 for q in channel_quanta) or any(
            hp != h_rec_unit for hp in channel_h
        ):
            raise AssertionError("Channel quantum not constant across phases")
        a5_assertions += 1

        for prof in profiles:
            tot_n = sum(prof)
            w_rec = [prof[k] * channel_quanta[k] for k in range(5)]
            tot_w = sum(w_rec)
            h_rec = [phi_scale(prof[k], channel_h[k]) for k in range(5)]
            tot_h_a = sum(hp[0] for hp in h_rec)
            tot_h_b = sum(hp[1] for hp in h_rec)
            for k in range(5):
                if prof[k] > 0:
                    w_bar_k = Fraction(w_rec[k], prof[k])
                    if w_bar_k != Fraction(w0, 1):
                        raise AssertionError("Conditional mean work != w0")
                if Fraction(w_rec[k], tot_w) != Fraction(prof[k], tot_n):
                    raise AssertionError("Identity (9a) rational share mismatch")
                if (
                    Fraction(h_rec[k][0], tot_h_a) != Fraction(prof[k], tot_n)
                    or (
                        tot_h_b != 0
                        and Fraction(h_rec[k][1], tot_h_b) != Fraction(prof[k], tot_n)
                    )
                ):
                    raise AssertionError("Identity (9a) Hermitian share mismatch")
                a5_assertions += 1
                a5_channel_checks += 1

    total_assertions += a5_assertions

    # =========================================================================
    # A6: Operational boundaries (dead-time lock, backreaction, 2*b^n growth)
    # =========================================================================
    a6_assertions = 0
    dead_time_cases = 0
    backreaction_cases = 0
    for c in odd_seeds:
        for m in range(5):
            ck = c_mul(c, rho_pows[m])
            a_m = c_mul(CAP_J5, ck)
            h_dis = c_scale(2, a_m)
            z_occ = c_mul(ONE_MINUS_RHO5, ck)

            b_fresh = [h_dis, ZERO5, c_neg(h_dis), c_neg(a_m)]
            x1, b1, f1, adm1, _, _ = unreduced_loaded_step(a_m, b_fresh, c_neg(a_m), 0)
            x2, b2, f2, adm2, _, _ = unreduced_loaded_step(x1, b1, f1, 1)
            if (
                adm1
                or adm2
                or not c_eq(x2, a_m)
                or not c_eq(b2[0], h_dis)
                or not c_eq(b2[1], ZERO5)
            ):
                raise AssertionError("Dead-time lock failed")
            dead_time_cases += 1
            a6_assertions += 1

            b_unarch = [h_dis, z_occ, c_neg(c_add(h_dis, z_occ)), c_neg(a_m)]
            u1, ub1, uf1, uadm1, _, _ = unreduced_loaded_step(
                a_m, b_unarch, c_neg(a_m), 0
            )
            u2, ub2, uf2, uadm2, _, _ = unreduced_loaded_step(u1, ub1, uf1, 1)
            exp_x_dist = c_mul(c_add(ONE5, c_pow(RHO5, 2)), ck)
            exp_z_dist = c_mul(c_sub(ONE5, c_pow(RHO5, 2)), ck)
            if (
                uadm1
                or (not uadm2)
                or not c_eq(u2, exp_x_dist)
                or not c_eq(ub2[1], exp_z_dist)
                or c_eq(u2, a_m)
                or c_eq(ub2[1], z_occ)
            ):
                raise AssertionError("Unarchived backreaction failed")
            backreaction_cases += 1
            a6_assertions += 1

    primitive_seeds_4 = [(1, 0, 0, 0), (0, 1, 0, 0), (1, 0, -1, 0), (-1, -2, -2, 0)]
    for a0_mode, b_mode in ((5, 4), (7, 6)):
        p_prev = 2
        p_cur = a0_mode
        for n in range(1, 26):
            if n > 1:
                p_prev, p_cur = p_cur, a0_mode * p_cur - (b_mode * b_mode) * p_prev
            denom = 2 * (b_mode**n)
            cos_n = Fraction(p_cur, denom)
            if (
                (p_cur & 1) != 1
                or math.gcd(p_cur, denom) != 1
                or cos_n.numerator != p_cur
                or cos_n.denominator != denom
            ):
                raise AssertionError("Denominator reduction failure")
            for e0 in primitive_seeds_4:
                scaled_num = [coord * cos_n.numerator for coord in e0]
                if all(val % cos_n.denominator == 0 for val in scaled_num):
                    raise AssertionError("Unscaled free-mode pulse unexpectedly in O")
                m_horiz = 2 * (b_mode**25)
                if any(
                    (coord * m_horiz * cos_n.numerator) % cos_n.denominator != 0
                    for coord in e0
                ):
                    raise AssertionError("Horizon-scaled free-mode pulse not in O")
                a6_assertions += 2
            a6_assertions += 1

    total_assertions += a6_assertions

    print("C-COLOCATED-RESONANT-RECORD-TWO-PLACE-ACCOUNT-N VERIFY")
    print(f"A1_HERMITIAN_GALOIS_GRID=625 B0_COUNT={b0_count} ASSERTIONS={a1_assertions}")
    print(
        f"A2_RESONANCE_IFF_PAIRS=6480 RESONANT_GRID1={resonant_in_grid1} RESONANT_GRID2=624 CUTS={a2_cuts_checked} ASSERTIONS={a2_assertions}"
    )
    print(
        f"A3_F16_INERTNESS_COSETS=16 ODD_ONEHOT_PASS={odd_onehot_pass} EVEN_ONEHOT_FAIL={even_onehot_fail} CUTS={a3_cuts_checked} ASSERTIONS={a3_assertions}"
    )
    print(
        f"A4_PR1957_QUANTUM=35 HELPER_DROP=55->20 AREA=6+8phi PORT_P27=(0,35) PORT_P35=(35,0) ASSERTIONS={a4_assertions}"
    )
    print(
        f"A5_IDENTITY_9A_SEEDS=81 PROFILES=12 CHANNEL_CHECKS={a5_channel_checks} ASSERTIONS={a5_assertions}"
    )
    print(
        f"A6_DEAD_TIME_LOCK={dead_time_cases} BACKREACTION={backreaction_cases} MODES_N_MAX=25 ASSERTIONS={a6_assertions}"
    )
    print(f"TOTAL_ASSERTIONS={total_assertions}")
    print("VERIFY PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
