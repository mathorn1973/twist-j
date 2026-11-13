#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Primary exact verifier for C-COLOCATED-RESONANT-RECORD-TWO-PLACE-ACCOUNT-N.

Representation: 4-component power basis (1, j, j^2, j^3) over Z with
1 + j + j^2 + j^3 + j^4 = 0, explicit quadratic forms A(v), B(v) in Z[phi],
and reduced co-located contact displacement d = (v - x) / 2 on F = -x.
Standard library only; exact int and Fraction arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
import itertools
import math
import sys

Vec4 = tuple[int, int, int, int]
Phi2 = tuple[int, int]  # A + B * phi with phi^2 = phi + 1

ZERO: Vec4 = (0, 0, 0, 0)
ONE: Vec4 = (1, 0, 0, 0)
J_ROOT: Vec4 = (0, 1, 0, 0)
RHO: Vec4 = (0, 0, 1, 0)  # j^2
J_4: Vec4 = (-1, -1, -1, -1)  # j^4 = -1 - j - j^2 - j^3
PHI_EL: Vec4 = (0, 0, -1, -1)  # phi = -j^2 - j^3
CAP_J: Vec4 = (1, 0, 1, 0)  # J = 1 + rho = 1 + j^2
CAP_J_INV: Vec4 = (0, -1, -1, 0)  # J^-1 = -j - j^2
THREE_PLUS_RHO: Vec4 = (3, 0, 1, 0)  # 3 + rho
ONE_MINUS_RHO: Vec4 = (1, 0, -1, 0)  # 1 - j^2
ONE_MINUS_J4: Vec4 = (2, 1, 1, 1)  # 1 - j^4


def v_add(a: Vec4, b: Vec4) -> Vec4:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def v_sub(a: Vec4, b: Vec4) -> Vec4:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])


def v_neg(a: Vec4) -> Vec4:
    return (-a[0], -a[1], -a[2], -a[3])


def v_scale(k: int, a: Vec4) -> Vec4:
    return (k * a[0], k * a[1], k * a[2], k * a[3])


def v_mul(a: Vec4, b: Vec4) -> Vec4:
    deg = [0, 0, 0, 0, 0]
    for ia, va in enumerate(a):
        if va:
            for ib, vb in enumerate(b):
                if vb:
                    deg[(ia + ib) % 5] += va * vb
    c4 = deg[4]
    return (deg[0] - c4, deg[1] - c4, deg[2] - c4, deg[3] - c4)


def v_pow(a: Vec4, exp: int) -> Vec4:
    res = ONE
    base = a
    e = exp
    while e > 0:
        if e & 1:
            res = v_mul(res, base)
        base = v_mul(base, base)
        e >>= 1
    return res


def v_conj(a: Vec4) -> Vec4:
    # a0 + a1 j^4 + a2 j^3 + a3 j^2 with j^4 = -1 - j - j^2 - j^3
    a0, a1, a2, a3 = a
    return (a0 - a1, -a1, a3 - a1, a2 - a1)


def v_div2_exact(a: Vec4) -> Vec4 | None:
    if (a[0] & 1) or (a[1] & 1) or (a[2] & 1) or (a[3] & 1):
        return None
    return (a[0] // 2, a[1] // 2, a[2] // 2, a[3] // 2)


def v_in_2o(a: Vec4) -> bool:
    return ((a[0] & 1) == 0) and ((a[1] & 1) == 0) and ((a[2] & 1) == 0) and ((a[3] & 1) == 0)


def v_mod2(a: Vec4) -> Vec4:
    return (a[0] & 1, a[1] & 1, a[2] & 1, a[3] & 1)


def v_eps_mod5(a: Vec4) -> int:
    return (a[0] + a[1] + a[2] + a[3]) % 5


def h_pair(v: Vec4) -> Phi2:
    v0, v1, v2, v3 = v
    s0 = v0 * v0 + v1 * v1 + v2 * v2 + v3 * v3
    s1 = v0 * v1 + v1 * v2 + v2 * v3
    s2 = v0 * v2 + v1 * v3 + v0 * v3
    return (s0 - s1, s1 - s2)


def phi_add(p: Phi2, q: Phi2) -> Phi2:
    return (p[0] + q[0], p[1] + q[1])


def phi_sub(p: Phi2, q: Phi2) -> Phi2:
    return (p[0] - q[0], p[1] - q[1])


def phi_scale(k: int, p: Phi2) -> Phi2:
    return (k * p[0], k * p[1])


def phi_mul(p: Phi2, q: Phi2) -> Phi2:
    # (a + b phi)(c + d phi) = (ac + bd) + (ad + bc + bd) phi
    a, b = p
    c, d = q
    return (a * c + b * d, a * d + b * c + b * d)


def phi_conj(p: Phi2) -> Phi2:
    # sigma_2(A + B phi) = A + B(1 - phi) = (A + B) - B phi
    return (p[0] + p[1], -p[1])


def phi_trace(p: Phi2) -> int:
    # Tr_{Q(phi)/Q}(A + B phi) = 2A + B
    return 2 * p[0] + p[1]


def phi_norm(p: Phi2) -> int:
    # N_{Q(phi)/Q}(A + B phi) = A^2 + A B - B^2
    a, b = p
    return a * a + a * b - b * b


def q_norm(v: Vec4) -> int:
    return phi_trace(h_pair(v))


def colocated_step(
    x: Vec4, b_slots: list[Vec4], f_field: Vec4, idx: int
) -> tuple[Vec4, list[Vec4], Vec4, bool, Vec4, Phi2]:
    """Apply one co-located loaded contact C(x, b_slots[idx]) on F = -x."""
    v = b_slots[idx]
    d = v_div2_exact(v_sub(v, x))
    new_b = list(b_slots)
    if d is None:
        return x, new_b, f_field, False, ZERO, (0, 0)
    curr = v_mul(v_sub(RHO, ONE), d)  # i = (rho - 1) d
    x_next = v_sub(x, curr)
    v_next = v_add(v, curr)
    f_next = v_add(f_field, curr)
    new_b[idx] = v_next
    return x_next, new_b, f_next, True, curr, h_pair(d)


def check_cut_invariants(
    x: Vec4,
    b_slots: list[Vec4],
    f_field: Vec4,
    init_sum: Vec4,
    init_eps: list[int],
    init_q_full: int,
    init_h_full: Phi2,
) -> int:
    checks = 0
    # Gauss law at A: F + x = 0
    if v_add(f_field, x) != ZERO:
        raise AssertionError(f"Gauss A violation: x={x}, F={f_field}")
    checks += 1
    # Gauss law at B: F - sum_B v = 0
    b_sum = ZERO
    for s in b_slots:
        b_sum = v_add(b_sum, s)
    if v_sub(f_field, b_sum) != ZERO:
        raise AssertionError(f"Gauss B violation: F={f_field}, sum_B={b_sum}")
    checks += 1
    # Total slot sum conservation
    if v_add(x, b_sum) != init_sum:
        raise AssertionError("Total slot sum violation")
    checks += 1
    # Individual mod-5 residue conservation
    cur_eps = [v_eps_mod5(x)] + [v_eps_mod5(s) for s in b_slots]
    if cur_eps != init_eps:
        raise AssertionError(f"Residue mod 5 violation: {cur_eps} != {init_eps}")
    checks += 1
    # Complete scalar account 2 * (Q(x) + sum_B Q(v))
    q_full = 2 * (q_norm(x) + sum(q_norm(s) for s in b_slots))
    if q_full != init_q_full:
        raise AssertionError(f"Scalar account violation: {q_full} != {init_q_full}")
    checks += 1
    # Complete Hermitian account 2 * (h(x) + sum_B h(v))
    h_sum = h_pair(x)
    for s in b_slots:
        h_sum = phi_add(h_sum, h_pair(s))
    h_full = phi_scale(2, h_sum)
    if h_full != init_h_full:
        raise AssertionError(f"Hermitian account violation: {h_full} != {init_h_full}")
    checks += 1
    return checks


def main() -> int:
    total_assertions = 0

    # =========================================================================
    # A1: Two-place Galois/Hermitian account and conjugate trace decomposition
    # =========================================================================
    a1_assertions = 0
    if v_mul(CAP_J, CAP_J_INV) != ONE:
        raise AssertionError("J * J^-1 != 1")
    a1_assertions += 1

    h_1mr = h_pair(ONE_MINUS_RHO)
    h_1mj4 = h_pair(ONE_MINUS_J4)
    h_j = h_pair(CAP_J)
    h_3pr = h_pair(THREE_PLUS_RHO)

    if h_1mr != (2, 1) or phi_trace(h_1mr) != 5 or phi_norm(h_1mr) != 5:
        raise AssertionError(f"Bad h(1-j^2): {h_1mr}")
    if h_1mj4 != (3, -1) or phi_trace(h_1mj4) != 5 or phi_norm(h_1mj4) != 5:
        raise AssertionError(f"Bad h(1-j^4): {h_1mj4}")
    if phi_conj(h_1mr) != h_1mj4 or phi_mul(h_1mr, h_1mj4) != (5, 0):
        raise AssertionError("Galois conjugate / norm failure on 1-j^2 vs 1-j^4")
    if h_j != (2, -1) or phi_trace(h_j) != 3 or phi_norm(h_j) != 1:
        raise AssertionError(f"Bad h(J): {h_j}")
    if h_3pr != (10, -3) or phi_trace(h_3pr) != 17 or phi_norm(h_3pr) != 61:
        raise AssertionError(f"Bad h(3+rho): {h_3pr}")
    if phi_add(phi_scale(4, h_j), h_1mr) != h_3pr:
        raise AssertionError("4 h(J) + h(1-rho) != h(3+rho)")
    a1_assertions += 6

    grid_2: list[Vec4] = [
        (c0, c1, c2, c3)
        for c0, c1, c2, c3 in itertools.product((-2, -1, 0, 1, 2), repeat=4)
    ]
    b0_count = 0
    for c in grid_2:
        vv_bar = v_mul(c, v_conj(c))
        ac, bc = h_pair(c)
        # Check v * v_bar == A_c * 1 + B_c * phi
        if vv_bar != v_add(v_scale(ac, ONE), v_scale(bc, PHI_EL)):
            raise AssertionError(f"v*vbar != A+B*phi at {c}")
        qc = q_norm(c)
        nc = phi_norm((ac, bc))
        if qc != 2 * ac + bc:
            raise AssertionError("Q(c) != 2A + B")
        if (c == ZERO and (qc != 0 or nc != 0)) or (c != ZERO and (qc <= 0 or nc <= 0)):
            raise AssertionError(f"Positivity failure at {c}: Q={qc}, N={nc}")

        c_1mr = v_mul(ONE_MINUS_RHO, c)
        c_1mj4 = v_mul(ONE_MINUS_J4, c)
        h_c_1mr = h_pair(c_1mr)
        h_c_1mj4 = h_pair(c_1mj4)
        if h_c_1mr != (2 * ac + bc, ac + 3 * bc):
            raise AssertionError(f"h((1-j^2)c) mismatch at {c}")
        if h_c_1mj4 != (3 * ac - bc, 2 * bc - ac):
            raise AssertionError(f"h((1-j^4)c) mismatch at {c}")

        q_1mr = q_norm(c_1mr)
        q_1mj4 = q_norm(c_1mj4)
        if q_1mr != 5 * (ac + bc) or q_1mj4 != 5 * ac:
            raise AssertionError(f"Trace formula mismatch at {c}")
        if q_1mr + q_1mj4 != 5 * qc:
            raise AssertionError(f"Conjugate trace sum != 5 Q(c) at {c}")
        if (q_1mr == q_1mj4) != (bc == 0):
            raise AssertionError(f"Equality condition B_c == 0 failed at {c}")
        if bc == 0:
            b0_count += 1
            if 2 * q_1mr != 5 * qc:
                raise AssertionError(f"B_c == 0 ratio failure at {c}")
        # Current-to-displacement conversion: 5 h(c) == (3 - phi) h((rho - 1)c)
        if phi_scale(5, (ac, bc)) != phi_mul(h_1mj4, h_c_1mr):
            raise AssertionError(f"Current-to-displacement conversion failed at {c}")
        a1_assertions += 10

    # Explicit counterexamples c1 = 1 - j^2, c2 = 1 - j^4 with equal Q(c) = 5
    if (
        q_norm(ONE_MINUS_RHO) != 5
        or q_norm(ONE_MINUS_J4) != 5
        or q_norm(v_mul(ONE_MINUS_RHO, ONE_MINUS_RHO)) != 15
        or q_norm(v_mul(ONE_MINUS_RHO, ONE_MINUS_J4)) != 10
    ):
        raise AssertionError("Counterexample pair (c1, c2) failed")
    a1_assertions += 1
    total_assertions += a1_assertions

    # =========================================================================
    # A2: Iff resonance theorem for the 2-contact returning selector
    # =========================================================================
    a2_assertions = 0
    grid_1: list[Vec4] = [
        (c0, c1, c2, c3)
        for c0, c1, c2, c3 in itertools.product((-1, 0, 1), repeat=4)
    ]
    nonzero_1 = [c for c in grid_1 if c != ZERO]

    # Counterexample (a, c) = (1, 1) slot-sum check
    if v_add(ONE, v_add(ONE, v_scale(2, ONE))) == v_add(
        v_scale(3, ONE), ONE_MINUS_RHO
    ):
        raise AssertionError("Slot-sum counterexample (1,1) failed")
    a2_assertions += 1

    resonant_in_grid1 = 0
    a2_cuts_checked = 0
    for a in grid_1:
        for c in nonzero_1:
            is_res = a == v_mul(CAP_J, c)
            # 3-slot sum condition: 2a + 2c == 3a + (1-rho)c iff a == Jc
            lhs_sum = v_add(v_scale(2, a), v_scale(2, c))
            rhs_sum = v_add(v_scale(3, a), v_mul(ONE_MINUS_RHO, c))
            if (lhs_sum == rhs_sum) != is_res:
                raise AssertionError(f"3-slot sum iff failed for a={a}, c={c}")
            a2_assertions += 1

            h0 = v_add(a, v_scale(2, c))
            z0 = ZERO
            u_comp = v_neg(v_add(a, h0))
            x0 = a
            f0 = v_neg(a)
            b0 = [h0, z0, u_comp]
            init_sum = v_add(x0, v_add(h0, v_add(z0, u_comp)))
            init_eps = [v_eps_mod5(x0)] + [v_eps_mod5(s) for s in b0]
            init_q = 2 * (q_norm(x0) + sum(q_norm(s) for s in b0))
            init_h = phi_scale(
                2,
                phi_add(
                    h_pair(x0),
                    phi_add(h_pair(h0), phi_add(h_pair(z0), h_pair(u_comp))),
                ),
            )

            # Forward 2 contacts: C(x, h), C(x, z)
            x1, b1, f1, adm1, _, area1 = colocated_step(x0, b0, f0, 0)
            a2_assertions += check_cut_invariants(
                x1, b1, f1, init_sum, init_eps, init_q, init_h
            )
            a2_cuts_checked += 1
            if not adm1 or x1 != v_add(a, v_mul(ONE_MINUS_RHO, c)):
                raise AssertionError("Step 1 admission/state mismatch")
            a2_assertions += 1

            x2, b2, f2, adm2, _, area2 = colocated_step(x1, b1, f1, 1)
            a2_assertions += check_cut_invariants(
                x2, b2, f2, init_sum, init_eps, init_q, init_h
            )
            a2_cuts_checked += 1

            returned_and_admitted = adm2 and (x2 == a) and (f2 == f0)
            if returned_and_admitted != is_res:
                raise AssertionError(
                    f"Resonance iff failed for a={a}, c={c}: got {returned_and_admitted}, expected {is_res}"
                )
            a2_assertions += 1

            if is_res:
                resonant_in_grid1 += 1
                if (
                    x1 != v_scale(2, c)
                    or b2[0] != v_scale(2, a)
                    or b2[1] != v_mul(ONE_MINUS_RHO, c)
                    or phi_add(area1, area2) != phi_scale(2, h_pair(c))
                ):
                    raise AssertionError("Resonant state/area mismatch")
                a2_assertions += 1

            # Literal 8-contact inverse: C(x, z)^4 followed by C(x, h)^4
            xi, bi, fi = x2, b2, f2
            for idx in (1, 1, 1, 1, 0, 0, 0, 0):
                xi, bi, fi, _, _, _ = colocated_step(xi, bi, fi, idx)
                a2_assertions += check_cut_invariants(
                    xi, bi, fi, init_sum, init_eps, init_q, init_h
                )
                a2_cuts_checked += 1
            if xi != x0 or bi != b0 or fi != f0:
                raise AssertionError("8-contact inverse failed to restore state")
            a2_assertions += 1

    # Full resonant verification across all 624 non-zero seeds in {-2..2}^4
    for c in grid_2:
        if c == ZERO:
            continue
        a = v_mul(CAP_J, c)
        h0 = v_mul(THREE_PLUS_RHO, c)
        if h0 != v_add(a, v_scale(2, c)):
            raise AssertionError("h0 != (3+rho)c")
        x1, b1, f1, adm1, _, area1 = colocated_step(
            a, [h0, ZERO, v_neg(v_add(a, h0))], v_neg(a), 0
        )
        x2, b2, f2, adm2, _, area2 = colocated_step(x1, b1, f1, 1)
        if not (adm1 and adm2):
            raise AssertionError("Resonant pair refused in grid_2")
        if x1 != v_scale(2, c) or x2 != a or f2 != v_neg(a):
            raise AssertionError("Resonant trajectory failure in grid_2")
        if b2[0] != v_scale(2, a) or b2[1] != v_mul(ONE_MINUS_RHO, c):
            raise AssertionError("Resonant output slots failure in grid_2")
        ac, bc = h_pair(c)
        if phi_add(h_pair(b2[0]), h_pair(b2[1])) != h_pair(h0):
            raise AssertionError("Pointwise Hermitian partition h(h0)=h(h1)+h(z2) failed")
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
    # Verify O / 2O has 16 cosets and no zero divisors
    cosets_mod2 = [
        (b0, b1, b2, b3) for b0, b1, b2, b3 in itertools.product((0, 1), repeat=4)
    ]
    nonzero_cosets = [u for u in cosets_mod2 if u != ZERO]
    for u in nonzero_cosets:
        for v in nonzero_cosets:
            if v_in_2o(v_mul(u, v)):
                raise AssertionError(f"Zero divisor in O/2O: {u} * {v}")
            a3_assertions += 1

    rho_pows = [v_pow(RHO, k) for k in range(5)]
    c_1957: Vec4 = (-1, -2, -2, 0)
    odd_seeds: list[Vec4] = nonzero_1 + [c_1957]  # 81 odd seeds
    even_seeds: list[Vec4] = [v_scale(2, c) for c in odd_seeds]  # 81 even seeds
    all_bank_seeds = odd_seeds + even_seeds  # 162 seeds

    odd_onehot_pass = 0
    even_onehot_fail = 0
    a3_cuts_checked = 0

    for c in all_bank_seeds:
        c_is_odd = not v_in_2o(c)
        ac, bc = h_pair(c)
        seed_all_m_onehot = True

        for m in range(5):
            a_m = v_mul(v_mul(CAP_J, c), rho_pows[m])
            b_slots: list[Vec4] = []
            for k in range(5):
                hk = v_mul(v_mul(THREE_PLUS_RHO, c), rho_pows[k])
                zk = ZERO
                uk = v_neg(hk)
                b_slots.extend([hk, zk, uk])
            b_slots.append(v_neg(a_m))  # signal companion at B

            x_cur = a_m
            f_cur = v_neg(a_m)
            init_b = list(b_slots)
            b_sum0 = ZERO
            for s in b_slots:
                b_sum0 = v_add(b_sum0, s)
            init_sum = v_add(x_cur, b_sum0)
            init_eps = [v_eps_mod5(x_cur)] + [v_eps_mod5(s) for s in b_slots]
            init_q = 2 * (q_norm(x_cur) + sum(q_norm(s) for s in b_slots))
            h_acc = h_pair(x_cur)
            for s in b_slots:
                h_acc = phi_add(h_acc, h_pair(s))
            init_h = phi_scale(2, h_acc)

            adm_flags: list[bool] = []
            path_area: Phi2 = (0, 0)
            # 10-contact bank pass: k = 0..4, [C(x, h_k), C(x, z_k)]
            for k in range(5):
                x_cur, b_slots, f_cur, adm_h, _, ar_h = colocated_step(
                    x_cur, b_slots, f_cur, 3 * k
                )
                a3_assertions += check_cut_invariants(
                    x_cur, b_slots, f_cur, init_sum, init_eps, init_q, init_h
                )
                a3_cuts_checked += 1
                adm_flags.append(adm_h)
                path_area = phi_add(path_area, ar_h)

                x_cur, b_slots, f_cur, adm_z, _, ar_z = colocated_step(
                    x_cur, b_slots, f_cur, 3 * k + 1
                )
                a3_assertions += check_cut_invariants(
                    x_cur, b_slots, f_cur, init_sum, init_eps, init_q, init_h
                )
                a3_cuts_checked += 1
                adm_flags.append(adm_z)
                path_area = phi_add(path_area, ar_z)

            # Check whether this phase m achieved exact one-hot selectivity
            m_onehot = (x_cur == a_m) and (f_cur == v_neg(a_m))
            for k in range(5):
                hk_out = b_slots[3 * k]
                zk_out = b_slots[3 * k + 1]
                if k == m:
                    exp_h = v_scale(2, a_m)
                    exp_z = v_mul(v_mul(ONE_MINUS_RHO, c), rho_pows[m])
                    if (
                        hk_out != exp_h
                        or zk_out != exp_z
                        or not (adm_flags[2 * k] and adm_flags[2 * k + 1])
                    ):
                        m_onehot = False
                else:
                    if (
                        hk_out != init_b[3 * k]
                        or zk_out != ZERO
                        or adm_flags[2 * k]
                        or adm_flags[2 * k + 1]
                    ):
                        m_onehot = False

            if c_is_odd:
                if not m_onehot:
                    raise AssertionError(f"Odd seed {c} failed one-hot at m={m}")
                if (
                    h_pair(b_slots[3 * m + 1]) != phi_mul((2, 1), (ac, bc))
                    or q_norm(b_slots[3 * m + 1]) != 5 * (ac + bc)
                    or path_area != (2 * ac, 2 * bc)
                ):
                    raise AssertionError(f"Odd seed {c} quantum/area mismatch at m={m}")
                a3_assertions += 2
            else:
                if m == 1:
                    # Theorem 3(=>): at m=1, channel k=0 Contact 1 is admitted and disturbs h_0
                    if not adm_flags[0] or b_slots[0] == init_b[0]:
                        raise AssertionError(
                            f"Even seed {c} failed Theorem 3 converse at m=1, k=0"
                        )
                    a3_assertions += 1
                if not m_onehot:
                    seed_all_m_onehot = False

            # Literal 40-contact inverse of the 10-contact bank
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
                    x_cur, b_slots, f_cur, _, _, _ = colocated_step(
                        x_cur, b_slots, f_cur, idx
                    )
                    a3_assertions += check_cut_invariants(
                        x_cur, b_slots, f_cur, init_sum, init_eps, init_q, init_h
                    )
                    a3_cuts_checked += 1
            if x_cur != a_m or b_slots != init_b or f_cur != v_neg(a_m):
                raise AssertionError(f"40-contact bank inverse failed for seed {c}, m={m}")
            a3_assertions += 1

        if c_is_odd and seed_all_m_onehot:
            odd_onehot_pass += 1
        elif (not c_is_odd) and (not seed_all_m_onehot):
            even_onehot_fail += 1
        else:
            raise AssertionError(f"Iff selectivity violation for seed {c}")
        a3_assertions += 1

    total_assertions += a3_assertions

    # =========================================================================
    # A4: Exact instantiation of PR #1957 35-quantum
    # =========================================================================
    a4_assertions = 0
    if v_mul(ONE_MINUS_RHO, CAP_J_INV) != c_1957 or v_in_2o(c_1957):
        raise AssertionError("c_1957 derivation failed")
    if h_pair(c_1957) != (3, 4) or q_norm(c_1957) != 10:
        raise AssertionError("h(c_1957) != 3 + 4*phi or Q != 10")
    a4_assertions += 2

    for k in range(5):
        ck = v_mul(c_1957, rho_pows[k])
        ak = v_mul(CAP_J, ck)
        h0k = v_mul(THREE_PLUS_RHO, ck)
        h1k = v_scale(2, ak)
        z2k = v_mul(ONE_MINUS_RHO, ck)
        if (
            h_pair(ak) != (2, 1)
            or q_norm(ak) != 5
            or h_pair(h0k) != (18, 19)
            or q_norm(h0k) != 55
            or h_pair(h1k) != (8, 4)
            or q_norm(h1k) != 20
            or h_pair(z2k) != (10, 15)
            or q_norm(z2k) != 35
            or phi_scale(2, h_pair(ck)) != (6, 8)
        ):
            raise AssertionError(f"PR #1957 values mismatch at phase k={k}")
        a4_assertions += 1

    # Reproduce the two-selector port of PR #1957 on a0 = 1-rho (P35) and a1 = (1-rho)rho^4 (P27)
    a0_p35 = ONE_MINUS_RHO
    a1_p27 = v_mul(ONE_MINUS_RHO, rho_pows[4])
    c0_port = c_1957
    c1_port = v_mul(c_1957, rho_pows[4])
    h0_port = v_mul(THREE_PLUS_RHO, c0_port)
    h1_port = v_mul(THREE_PLUS_RHO, c1_port)

    for label, sig, expected_q_pair in (
        ("P27", a1_p27, (0, 35)),
        ("P35", a0_p35, (35, 0)),
    ):
        b_port = [
            h0_port,
            ZERO,
            v_neg(h0_port),
            h1_port,
            ZERO,
            v_neg(h1_port),
            v_neg(sig),
        ]
        xp = sig
        fp = v_neg(sig)
        port_area: Phi2 = (0, 0)
        for idx in (0, 1, 3, 4):
            xp, b_port, fp, _, _, ar = colocated_step(xp, b_port, fp, idx)
            port_area = phi_add(port_area, ar)
        got_q_pair = (q_norm(b_port[1]), q_norm(b_port[4]))
        if (
            xp != sig
            or fp != v_neg(sig)
            or got_q_pair != expected_q_pair
            or port_area != (6, 8)
            or phi_trace(port_area) != 20
        ):
            raise AssertionError(f"PR #1957 port check failed for {label}: {got_q_pair}")
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
        ac, bc = h_pair(c)
        w0 = 5 * (ac + bc)
        h_rec_unit = phi_mul((2, 1), (ac, bc))
        # Verify single-arrival recorded work across all 5 channels is w0
        channel_quanta: list[int] = []
        channel_h: list[Phi2] = []
        for m in range(5):
            a_m = v_mul(v_mul(CAP_J, c), rho_pows[m])
            h_m = v_mul(v_mul(THREE_PLUS_RHO, c), rho_pows[m])
            x1, b1, f1, adm1, _, _ = colocated_step(
                a_m, [h_m, ZERO, v_neg(h_m), v_neg(a_m)], v_neg(a_m), 0
            )
            x2, b2, f2, adm2, _, _ = colocated_step(x1, b1, f1, 1)
            if not (adm1 and adm2 and x2 == a_m and f2 == v_neg(a_m)):
                raise AssertionError("Single-channel arrival failed in A5")
            channel_quanta.append(q_norm(b2[1]))
            channel_h.append(h_pair(b2[1]))
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
            ck = v_mul(c, rho_pows[m])
            a_m = v_mul(CAP_J, ck)
            h_dis = v_scale(2, a_m)  # discharged helper 2 J c rho^m
            z_occ = v_mul(ONE_MINUS_RHO, ck)  # occupied record (1 - rho) c rho^m

            # (a) Dead-time lock when z is advanced to a fresh blank 0
            b_fresh = [h_dis, ZERO, v_neg(h_dis), v_neg(a_m)]
            x1, b1, f1, adm1, _, _ = colocated_step(a_m, b_fresh, v_neg(a_m), 0)
            x2, b2, f2, adm2, _, _ = colocated_step(x1, b1, f1, 1)
            if adm1 or adm2 or x2 != a_m or b2[0] != h_dis or b2[1] != ZERO:
                raise AssertionError(f"Dead-time lock failed for c={c}, m={m}")
            dead_time_cases += 1
            a6_assertions += 1

            # (b) Unarchived record backreaction when z_occ is left in the port
            b_unarch = [h_dis, z_occ, v_neg(v_add(h_dis, z_occ)), v_neg(a_m)]
            u1, ub1, uf1, uadm1, _, _ = colocated_step(a_m, b_unarch, v_neg(a_m), 0)
            u2, ub2, uf2, uadm2, _, _ = colocated_step(u1, ub1, uf1, 1)
            exp_x_dist = v_mul(v_add(ONE, v_pow(RHO, 2)), ck)  # (1 + rho^2) c rho^m
            exp_z_dist = v_mul(v_sub(ONE, v_pow(RHO, 2)), ck)  # (1 - rho^2) c rho^m
            if (
                uadm1
                or (not uadm2)
                or u2 != exp_x_dist
                or ub2[1] != exp_z_dist
                or u2 == a_m
                or ub2[1] == z_occ
            ):
                raise AssertionError(f"Unarchived backreaction failed for c={c}, m={m}")
            backreaction_cases += 1
            a6_assertions += 1

    # (c) Free-mode Chebyshev denominator growth for (a0, b) in {(5, 4), (7, 6)}
    primitive_seeds = [ONE, J_ROOT, ONE_MINUS_RHO, c_1957]
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
                raise AssertionError(
                    f"Denominator reduction failure at mode ({a0_mode},{b_mode}), n={n}"
                )
            # For every primitive e0, unscaled e0 * cos(n omega) is not in O
            for e0 in primitive_seeds:
                scaled_num = [coord * cos_n.numerator for coord in e0]
                if all(val % cos_n.denominator == 0 for val in scaled_num):
                    raise AssertionError("Unscaled free-mode pulse unexpectedly in O")
                # With horizon multiplier M = 2 * b^25, M * e0 * cos(n omega) is in O
                m_horiz = 2 * (b_mode**25)
                if any((coord * m_horiz * cos_n.numerator) % cos_n.denominator != 0 for coord in e0):
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
