#!/usr/bin/env python3
"""Independent method-blind adversarial breaker for R2 (#1588 / PR #1585).

Candidate: C-FUNDED-AREA-INDEPENDENT-REVIEW-N
Target: probes/P-FUNDED-AREA-PHASE-RECORD-1 (PR #1585, pin a4ec92176c9f8ace9f884254e05d57a5466b84e0)
Author: A. M. Thorn <thorn@twistj.com>
SPDX-License-Identifier: Apache-2.0
"""

from __future__ import annotations

import hashlib
import math
import sys

State = tuple[int, int, int, int, int, int, int, int]
WeylOp = tuple[tuple[int, int], ...]

IDENTITY_WEYL: WeylOp = tuple((k, 0) for k in range(5))
GATES: tuple[tuple[str, int], ...] = (("Q", 1), ("P", 1), ("Q", -1), ("P", -1))


def cost_h(q: int, p: int, u: int, v: int) -> int:
    return q * q + p * p + u * u + v * v


def total_e(s: State) -> int:
    q, p, u, v, b, _, _, _ = s
    return cost_h(q, p, u, v) + b


def unfunded_step(q: int, p: int, u: int, v: int, axis: str, h: int) -> tuple[int, int, int, int]:
    if axis == "Q":
        return (q + h, p, u, v)
    if axis == "P":
        return (q, p + h, u + h * q, v + h * q)
    raise ValueError(f"unknown axis: {axis}")


def delta_algebraic(q: int, p: int, u: int, v: int, axis: str, h: int) -> int:
    if axis == "Q":
        return 2 * h * q + 1
    if axis == "P":
        return 2 * h * p + 1 + 2 * h * q * (u + v) + 2 * q * q
    raise ValueError(f"unknown axis: {axis}")


def gate_direct(s: State, axis: str, eps: int) -> tuple[State, bool, int]:
    q, p, u, v, b, sigma, eta, c = s
    h = eps * sigma
    nq, np_, nu, nv = unfunded_step(q, p, u, v, axis, h)
    delta = cost_h(nq, np_, nu, nv) - cost_h(q, p, u, v)
    if b >= delta:
        return (nq, np_, nu, nv, b - delta, sigma, eta, c), True, delta
    return (q, p, u, v, b, -sigma, eta, c), False, delta


def gate_expanded(s: State, axis: str, eps: int) -> tuple[State, bool, int]:
    q, p, u, v, b, sigma, eta, c = s
    h = eps * sigma
    delta = delta_algebraic(q, p, u, v, axis, h)
    if b >= delta:
        nq, np_, nu, nv = unfunded_step(q, p, u, v, axis, h)
        return (nq, np_, nu, nv, b - delta, sigma, eta, c), True, delta
    return (q, p, u, v, b, -sigma, eta, c), False, delta


def controller_letter(c: int, eta: int) -> tuple[str, int]:
    if c == 0:
        return ("Q", 1)
    if c == 1:
        return ("P", eta)
    if c == 2:
        return ("Q", -1)
    if c == 3:
        return ("P", -eta)
    raise ValueError(f"invalid controller phase: {c}")


def step_u_star(s: State) -> tuple[State, bool]:
    _, _, _, _, _, _, eta, c = s
    axis, eps = controller_letter(c, eta)
    ns, accepted, _ = gate_direct(s, axis, eps)
    q, p, u, v, b, sigma, eta_out, _ = ns
    return (q, p, u, v, b, sigma, eta_out, (c + 1) % 4), accepted


def inv_u_star(s: State) -> State:
    q, p, u, v, b, sigma, eta, c = s
    c_prev = (c - 1) % 4
    axis, eps = controller_letter(c_prev, eta)
    prev_s, _, _ = gate_direct((q, p, u, v, b, sigma, eta, c_prev), axis, -eps)
    return prev_s


def apply_step_weyl(w: WeylOp, dq: int, dp: int) -> WeylOp:
    if dq == 0 and dp == 0:
        return w
    if dq != 0 and dp == 0:
        return tuple(((img + dq) % 5, exp) for img, exp in w)
    if dp != 0 and dq == 0:
        return tuple((img, (exp + dp * img) % 5) for img, exp in w)
    raise ValueError(f"non-elementary step displacement: dq={dq}, dp={dp}")


def expected_weyl(q0: int, p0: int, q: int, p: int, a_path: int) -> WeylOp:
    dq_tot = q - q0
    dp_tot = p - p0
    return tuple(
        ((k + dq_tot) % 5, (k * dp_tot + a_path - q0 * dp_tot) % 5)
        for k in range(5)
    )


def poly_mul_trunc(a: list[int], b: list[int], max_deg: int) -> list[int]:
    out = [0] * (max_deg + 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            if i + j <= max_deg:
                out[i + j] += ai * bj
    return out


def audit_attack_1_and_2() -> list[str]:
    lines: list[str] = []
    max_e = 12
    f1 = [0] * (max_e + 1)
    for x in range(-4, 5):
        if x * x <= max_e:
            f1[x * x] += 1
    f2 = poly_mul_trunc(f1, f1, max_e)
    r4 = poly_mul_trunc(f2, f2, max_e)
    expected_r4 = [1, 8, 24, 32, 24, 48, 96, 64, 24, 104, 144, 96, 96]
    if r4 != expected_r4:
        raise AssertionError(f"r4 mismatch: {r4} != {expected_r4}")
    tuple_xb_count = sum(r4[h] * (max_e + 1 - h) for h in range(max_e + 1))
    analytic_state_count = tuple_xb_count * 16
    if tuple_xb_count != 3605 or analytic_state_count != 57680:
        raise AssertionError(f"analytic count mismatch: {tuple_xb_count}, {analytic_state_count}")

    outside_box = 0
    for q in range(-4, 5):
        for p in range(-4, 5):
            for u in range(-4, 5):
                for v in range(-4, 5):
                    if max(abs(q), abs(p), abs(u), abs(v)) == 4 and cost_h(q, p, u, v) <= max_e:
                        outside_box += 1
    if outside_box != 0:
        raise AssertionError(f"found {outside_box} states with H<=12 outside [-3,3]^4")

    raw_states: list[State] = []
    for q in range(-3, 4):
        for p in range(-3, 4):
            for u in range(-3, 4):
                for v in range(-3, 4):
                    h_val = cost_h(q, p, u, v)
                    if h_val > max_e:
                        continue
                    for b in range(max_e - h_val + 1):
                        for sigma in (1, -1):
                            for eta in (1, -1):
                                for c in range(4):
                                    raw_states.append((q, p, u, v, b, sigma, eta, c))

    if len(raw_states) != 57680:
        raise AssertionError(f"enumerated state count {len(raw_states)} != 57680")

    gate_evals = 0
    rejected_evals = 0
    accepted_evals = 0
    gate_image_sets: dict[tuple[str, int], set[State]] = {g: set() for g in GATES}
    u_star_images: set[State] = set()

    for s in raw_states:
        e0 = total_e(s)
        diff0 = s[2] - s[3]
        for axis, eps in GATES:
            gate_evals += 1
            s1_dir, acc_dir, d_dir = gate_direct(s, axis, eps)
            s1_exp, acc_exp, d_exp = gate_expanded(s, axis, eps)
            if s1_dir != s1_exp or acc_dir != acc_exp or d_dir != d_exp:
                raise AssertionError(f"direct/expanded mismatch at {s} {axis}{eps}")
            if acc_dir:
                accepted_evals += 1
            else:
                rejected_evals += 1
            if s1_dir[4] < 0 or total_e(s1_dir) != e0 or (s1_dir[2] - s1_dir[3]) != diff0:
                raise AssertionError(f"invariant violation at {s} -> {s1_dir}")
            if s1_dir[6] != s[6] or s1_dir[7] != s[7]:
                raise AssertionError(f"control leak in elementary gate at {s}")
            back_s, _, _ = gate_direct(s1_dir, axis, -eps)
            if back_s != s:
                raise AssertionError(f"left inverse failed at {s} for {axis}{eps}")
            s_minus, _, _ = gate_direct(s, axis, -eps)
            fwd_s, _, _ = gate_direct(s_minus, axis, eps)
            if fwd_s != s:
                raise AssertionError(f"right inverse failed at {s} for {axis}{eps}")
            gate_image_sets[(axis, eps)].add(s1_dir)

        u1, _ = step_u_star(s)
        u_back = inv_u_star(u1)
        u_pre = inv_u_star(s)
        u_fwd, _ = step_u_star(u_pre)
        if u_back != s or u_fwd != s:
            raise AssertionError(f"U_* two-sided inverse failed at {s}")
        if total_e(u1) != e0 or (u1[2] - u1[3]) != diff0 or u1[6] != s[6]:
            raise AssertionError(f"U_* invariant failed at {s}")
        u_star_images.add(u1)

    if gate_evals != 230720 or rejected_evals != 89152 or accepted_evals != 141568:
        raise AssertionError(
            f"unexpected gate counts: total={gate_evals}, acc={accepted_evals}, rej={rejected_evals}"
        )
    for g, img_set in gate_image_sets.items():
        if len(img_set) != 57680:
            raise AssertionError(f"gate {g} merged states: image size {len(img_set)}")
    if len(u_star_images) != 57680:
        raise AssertionError(f"U_* merged states: image size {len(u_star_images)}")

    # Adversarial check on shells E in {13, 14, 15} inside [-3, 3]^4
    extra_states = 0
    extra_Rejects = 0
    for q in range(-3, 4):
        for p in range(-3, 4):
            for u in range(-3, 4):
                for v in range(-3, 4):
                    h_val = cost_h(q, p, u, v)
                    for e_val in (13, 14, 15):
                        if h_val > e_val:
                            continue
                        b = e_val - h_val
                        for sigma in (1, -1):
                            for eta in (1, -1):
                                for c in range(4):
                                    s = (q, p, u, v, b, sigma, eta, c)
                                    extra_states += 1
                                    for axis, eps in GATES:
                                        s1, acc, d1 = gate_direct(s, axis, eps)
                                        s2, acc2, d2 = gate_expanded(s, axis, eps)
                                        if s1 != s2 or acc != acc2 or d1 != d2:
                                            raise AssertionError("extra shell formula mismatch")
                                        if not acc:
                                            extra_Rejects += 1
                                        if gate_direct(s1, axis, -eps)[0] != s:
                                            raise AssertionError("extra shell inverse failure")
                                    if inv_u_star(step_u_star(s)[0]) != s:
                                        raise AssertionError("extra shell U_* inverse failure")

    lines.append(
        f"ATTACK_1_2 E<=12: r4_sum={sum(r4)} xb_tuples={tuple_xb_count} "
        f"raw_states={len(raw_states)} gate_evals={gate_evals} "
        f"accepted={accepted_evals} rejected={rejected_evals} "
        f"bijection_images=57680 extra_E13_15_states={extra_states} "
        f"extra_E13_15_rejects={extra_Rejects} STATUS=PASS"
    )
    return lines


def audit_attack_3_and_4() -> list[str]:
    lines: list[str] = []
    s0: State = (0, 0, 1, -1, 8320, 1, 1, 0)
    prefix_count = 0
    closed_count = 0
    min_bank = 8320
    max_abs_a = 0
    digest = hashlib.sha256()

    def dfs(depth: int, s: State, a_path: int, a2: int, w: WeylOp) -> None:
        nonlocal prefix_count, closed_count, min_bank, max_abs_a
        prefix_count += 1
        q, p, u, v, b, sigma, eta, c = s
        if b < min_bank:
            min_bank = b
        if abs(a_path) > max_abs_a:
            max_abs_a = abs(a_path)
        if b < 0 or sigma != 1:
            raise AssertionError(f"unexpected rejection in B=8320 tree at state {s}")
        if u != 1 + a_path or v != -1 + a_path:
            raise AssertionError(f"reference shift mismatch: u={u}, v={v}, A={a_path}")
        if (u * u - v * v) != 4 * a_path:
            raise AssertionError("quadratic reader mismatch")
        a_read = (u * u - v * v) // 4
        if a_read != a_path:
            raise AssertionError("A_read != A_path")
        if (u * u + v * v) != 2 + 2 * a_path * a_path:
            raise AssertionError("reference energy sum mismatch")
        if 2 * a_path != a2 + q * p:
            raise AssertionError(f"shoelace identity failed: 2*{a_path} != {a2} + {q}*{p}")
        if w != expected_weyl(0, 0, q, p, a_path):
            raise AssertionError(f"open-path Weyl law failed at q={q}, p={p}, A={a_path}")
        if q == 0 and p == 0:
            closed_count += 1
            if 2 * a_path != a2:
                raise AssertionError("closed-path shoelace mismatch")
            target_closed = tuple((k, a_read % 5) for k in range(5))
            if w != target_closed:
                raise AssertionError("closed-path Weyl scalar law failed")
        rec = f"{depth}:{q},{p},{u},{v},{b}:{a_path},{a2}:{w}\n".encode("ascii")
        digest.update(rec)
        if depth == 8:
            return
        for axis, eps in GATES:
            ns, acc, _ = gate_direct(s, axis, eps)
            if not acc:
                raise AssertionError("unexpected rejection in depth<=8 word tree")
            nq, np_, _, _, _, _, _, _ = ns
            dq = nq - q
            dp = np_ - p
            na_path = a_path + q * dp
            na2 = a2 + (q * np_ - p * nq)
            nw = apply_step_weyl(w, dq, dp)
            dfs(depth + 1, ns, na_path, na2, nw)

    dfs(0, s0, 0, 0, IDENTITY_WEYL)
    expected_prefixes = sum(4**n for n in range(9))
    expected_closed = sum(math.comb(2 * m, m) ** 2 for m in range(5))
    if prefix_count != 87381 or prefix_count != expected_prefixes:
        raise AssertionError(f"prefix_count={prefix_count} != 87381")
    if closed_count != 5341 or closed_count != expected_closed:
        raise AssertionError(f"closed_count={closed_count} != 5341")

    # Adversarial rejected-word and unprepared-reference suite (length 6 words = 4096)
    init_configs = [
        (0, 0, 1, -1, 2),   # prepared references, tight budget B=2 (rejections occur)
        (0, 0, 0, 0, 4),    # equal zero references u0=v0=0
        (0, 0, 2, 2, 10),   # equal nonzero references u0=v0=2
        (0, 0, 2, 0, 10),   # non-antipodal unequal references u0=2, v0=0
        (0, 0, 2, -2, 12),  # antipodal scaled gap u0=2, v0=-2 (d=2)
        (0, 0, -1, 1, 8),   # swapped antipodal references u0=-1, v0=1 (d=-1)
        (1, -1, 3, 0, 9),   # non-origin basepoint and occupied asymmetric references
    ]
    adv_paths = 0
    adv_rejected_steps = 0
    unprepared_reader_mismatch = 0

    def run_adv_tree(
        depth: int,
        s_init: State,
        s_cur: State,
        a_path: int,
        a2: int,
        w: WeylOp,
        word: list[tuple[str, int]],
    ) -> None:
        nonlocal adv_paths, adv_rejected_steps, unprepared_reader_mismatch
        q0, p0, u0, v0, _, _, _, _ = s_init
        q, p, u, v, _, _, _, _ = s_cur
        if u != u0 + a_path or v != v0 + a_path:
            raise AssertionError("general reference increment failed")
        if 2 * a_path != a2 + (q * p - q0 * p0):
            raise AssertionError("general shoelace endpoint identity failed")
        if (u * u - v * v) != (u0 * u0 - v0 * v0) + 2 * (u0 - v0) * a_path:
            raise AssertionError("general squared-cost difference identity failed")
        if w != expected_weyl(q0, p0, q, p, a_path):
            raise AssertionError("general chronological Weyl formula failed")
        if (u0, v0) != (1, -1) and a_path != 0 and (u * u - v * v) != 4 * a_path:
            unprepared_reader_mismatch += 1
        if depth == 6:
            adv_paths += 1
            cur = s_cur
            for axis, eps in reversed(word):
                cur, _, _ = gate_direct(cur, axis, -eps)
            if cur != s_init:
                raise AssertionError("multi-step word inverse failed across rejections")
            return
        for axis, eps in GATES:
            ns, acc, _ = gate_direct(s_cur, axis, eps)
            if not acc:
                adv_rejected_steps += 1
            nq, np_, _, _, _, _, _, _ = ns
            dq = nq - q
            dp = np_ - p
            word.append((axis, eps))
            run_adv_tree(
                depth + 1,
                s_init,
                ns,
                a_path + q * dp,
                a2 + (q * np_ - p * nq),
                apply_step_weyl(w, dq, dp),
                word,
            )
            word.pop()

    for q0, p0, u0, v0, b0 in init_configs:
        s_init: State = (q0, p0, u0, v0, b0, 1, 1, 0)
        run_adv_tree(0, s_init, s_init, 0, 0, IDENTITY_WEYL, [])

    lines.append(
        f"ATTACK_3_4 WORD_TREE: prefixes={prefix_count} closed={closed_count} "
        f"min_bank={min_bank} max_abs_A={max_abs_a} "
        f"tree_sha256={digest.hexdigest()} "
        f"adv_paths={adv_paths} adv_rejected_steps={adv_rejected_steps} "
        f"unprepared_reader_failures_verified={unprepared_reader_mismatch} STATUS=PASS"
    )
    return lines


def run_autonomous_steps(s0: State, steps: int) -> tuple[list[State], list[bool], int, int, WeylOp]:
    states = [s0]
    accepted_flags: list[bool] = []
    a_path = 0
    a2 = 0
    w = IDENTITY_WEYL
    cur = s0
    for _ in range(steps):
        q, p, _, _, _, _, _, _ = cur
        nxt, acc = step_u_star(cur)
        nq, np_, _, _, _, _, _, _ = nxt
        dq = nq - q
        dp = np_ - p
        a_path += q * dp
        a2 += q * np_ - p * nq
        w = apply_step_weyl(w, dq, dp)
        states.append(nxt)
        accepted_flags.append(acc)
        cur = nxt
    return states, accepted_flags, a_path, a2, w


def audit_attack_5() -> list[str]:
    lines: list[str] = []
    s_pos: State = (0, 0, 1, -1, 4, 1, 1, 0)
    s_neg: State = (0, 0, 1, -1, 4, 1, -1, 0)
    st_pos, acc_pos, a_pos, _, w_pos = run_autonomous_steps(s_pos, 4)
    st_neg, acc_neg, a_neg, _, w_neg = run_autonomous_steps(s_neg, 4)

    if not all(acc_pos) or not all(acc_neg):
        raise AssertionError("B=4 four-step history had unexpected rejection")
    h_pos = tuple(cost_h(s[0], s[1], s[2], s[3]) for s in st_pos)
    h_neg = tuple(cost_h(s[0], s[1], s[2], s[3]) for s in st_neg)
    b_pos = tuple(s[4] for s in st_pos)
    b_neg = tuple(s[4] for s in st_neg)
    if h_pos != (2, 3, 6, 5, 4) or h_neg != (2, 3, 6, 5, 4):
        raise AssertionError(f"unexpected H history: {h_pos}, {h_neg}")
    if b_pos != (4, 3, 0, 1, 2) or b_neg != (4, 3, 0, 1, 2):
        raise AssertionError(f"unexpected bank history: {b_pos}, {b_neg}")

    for sp, sn in zip(st_pos, st_neg):
        coarse_p = (sp[0] ** 2 + sp[1] ** 2, sp[2] ** 2 + sp[3] ** 2, sp[4], sp[5], sp[7])
        coarse_n = (sn[0] ** 2 + sn[1] ** 2, sn[2] ** 2 + sn[3] ** 2, sn[4], sn[5], sn[7])
        if coarse_p != coarse_n:
            raise AssertionError(f"coarse history mismatch: {coarse_p} != {coarse_n}")

    end_p = st_pos[-1]
    end_n = st_neg[-1]
    ord_p = (end_p[2] ** 2, end_p[3] ** 2)
    ord_n = (end_n[2] ** 2, end_n[3] ** 2)
    if ord_p != (4, 0) or ord_n != (0, 4) or a_pos != 1 or a_neg != -1:
        raise AssertionError("endpoint ordered reference cost mismatch")
    if w_pos != tuple((k, 1) for k in range(5)) or w_neg != tuple((k, 4) for k in range(5)):
        raise AssertionError("endpoint Weyl phase mismatch")
    # Scope guard: verify that exposing eta, p at t=2, or ordered (u^2,v^2) distinguishes them
    if st_pos[2][1] == st_neg[2][1] or st_pos[0][6] == st_neg[0][6] or ord_p == ord_n:
        raise AssertionError("exposed coordinates failed to separate opposite eta")

    lines.append(
        f"ATTACK_5 B4_OBSTRUCTION: H_hist={h_pos} b_hist={b_pos} "
        f"ord_pos={ord_p} ord_neg={ord_n} A_pos={a_pos} A_neg={a_neg} "
        f"W_exp_pos=1 W_exp_neg=4 coarse_match=True exposed_separates=True STATUS=PASS"
    )
    return lines


def audit_attack_6() -> list[str]:
    lines: list[str] = []
    budget_cases = 0
    accepted_runs = 0
    rejected_runs = 0
    for eta in (1, -1):
        for b_init in range(81):
            for k_laps in range(1, 7):
                budget_cases += 1
                s0: State = (0, 0, 1, -1, b_init, 1, eta, 0)
                states, acc_flags, a_path, a2, w = run_autonomous_steps(s0, 4 * k_laps)
                all_acc = all(acc_flags)
                threshold = 2 * k_laps * k_laps + 2
                if all_acc != (b_init >= threshold):
                    raise AssertionError(
                        f"threshold failure at eta={eta}, B={b_init}, K={k_laps}"
                    )
                end_s = states[-1]
                q, p, u, v, b_end, sigma_end, _, c_end = end_s
                if u != 1 + a_path or v != -1 + a_path or (u * u - v * v) != 4 * a_path:
                    raise AssertionError("actual-path reference law failed in budget grid")
                if 2 * a_path != a2 + q * p or w != expected_weyl(0, 0, q, p, a_path):
                    raise AssertionError("actual-path Weyl/shoelace law failed in budget grid")
                if all_acc:
                    accepted_runs += 1
                    if (q, p, u, v, b_end, sigma_end, c_end) != (
                        0,
                        0,
                        1 + eta * k_laps,
                        -1 + eta * k_laps,
                        b_init - 2 * k_laps * k_laps,
                        1,
                        0,
                    ):
                        raise AssertionError("accepted K-lap endpoint formula mismatch")
                    if w != tuple((idx, (eta * k_laps) % 5) for idx in range(5)):
                        raise AssertionError("accepted K-lap Weyl phase mismatch")
                else:
                    rejected_runs += 1

    if budget_cases != 972:
        raise AssertionError(f"budget_cases={budget_cases} != 972")

    # Extended threshold check K=7..10 at boundary B in {2K^2+1, 2K^2+2}
    for eta in (1, -1):
        for k_laps in range(7, 11):
            thr = 2 * k_laps * k_laps + 2
            _, acc_below, _, _, _ = run_autonomous_steps((0, 0, 1, -1, thr - 1, 1, eta, 0), 4 * k_laps)
            _, acc_at, _, _, _ = run_autonomous_steps((0, 0, 1, -1, thr, 1, eta, 0), 4 * k_laps)
            if all(acc_below) or not all(acc_at):
                raise AssertionError(f"extended threshold failure at K={k_laps}")

    # K=5, B=52, eta=+1 witness
    st_52, acc_52, a_52, _, w_52 = run_autonomous_steps((0, 0, 1, -1, 52, 1, 1, 0), 20)
    end_52 = st_52[-1]
    if not all(acc_52) or end_52 != (0, 0, 6, 4, 2, 1, 1, 0) or a_52 != 5 or w_52 != IDENTITY_WEYL:
        raise AssertionError(f"K=5, B=52 witness failed: end={end_52}, A={a_52}, W={w_52}")
    paid_work_52 = (end_52[2] ** 2 + end_52[3] ** 2) - 2
    if (end_52[2] ** 2, end_52[3] ** 2) != (36, 16) or paid_work_52 != 50:
        raise AssertionError("K=5, B=52 cost/work mismatch")

    # Nominal B=3 rejection control
    for eta in (1, -1):
        st_3, acc_3, a_3, _, w_3 = run_autonomous_steps((0, 0, 1, -1, 3, 1, eta, 0), 4)
        if acc_3 != [True, False, False, False]:
            raise AssertionError(f"B=3 acceptance pattern mismatch: {acc_3}")
        if st_3[-1] != (1, 0, 1, -1, 2, -1, eta, 0) or a_3 != 0:
            raise AssertionError(f"B=3 endpoint mismatch: {st_3[-1]}")
        if w_3 != tuple(((k + 1) % 5, 0) for k in range(5)):
            raise AssertionError("B=3 Weyl operator should be X^1")

    # Zero-reference controls (0,0,0,0,4,1,eta,0)
    for eta in (1, -1):
        st_z, acc_z, a_z, _, _ = run_autonomous_steps((0, 0, 0, 0, 4, 1, eta, 0), 4)
        if not all(acc_z) or st_z[-1] != (0, 0, eta, eta, 2, 1, eta, 0) or a_z != eta:
            raise AssertionError("zero-reference trajectory mismatch")
        if (st_z[-1][2] ** 2, st_z[-1][3] ** 2) != (1, 1):
            raise AssertionError("zero-reference squared cost should be (1,1)")

    # Autonomous periods of s_{4,+1} and s_{4,-1} and full cycle decomposition of E=6 shell
    shell_e6: list[State] = []
    for q in range(-2, 3):
        for p in range(-2, 3):
            for u in range(-2, 3):
                for v in range(-2, 3):
                    h_val = cost_h(q, p, u, v)
                    if h_val <= 6:
                        b = 6 - h_val
                        for sigma in (1, -1):
                            for eta in (1, -1):
                                for c in range(4):
                                    shell_e6.append((q, p, u, v, b, sigma, eta, c))
    if len(shell_e6) != 3728:
        raise AssertionError(f"E=6 shell size {len(shell_e6)} != 3728")

    visited: set[State] = set()
    cycle_hist: dict[int, int] = {}
    period_pos = 0
    period_neg = 0
    s4_pos: State = (0, 0, 1, -1, 4, 1, 1, 0)
    s4_neg: State = (0, 0, 1, -1, 4, 1, -1, 0)

    for s in shell_e6:
        if s in visited:
            continue
        cur = s
        orbit: list[State] = []
        seen_in_orbit: set[State] = set()
        while cur not in seen_in_orbit:
            seen_in_orbit.add(cur)
            orbit.append(cur)
            cur, _ = step_u_star(cur)
        if cur != s:
            raise AssertionError("first repeated state on E=6 was not initial state")
        plen = len(orbit)
        cycle_hist[plen] = cycle_hist.get(plen, 0) + 1
        visited.update(orbit)
        if s4_pos in seen_in_orbit:
            period_pos = plen
        if s4_neg in seen_in_orbit:
            period_neg = plen

    if period_pos != 124 or period_neg != 124:
        raise AssertionError(f"unexpected s4 periods: {period_pos}, {period_neg}")
    if len(cycle_hist) <= 1:
        raise AssertionError("expected multiple distinct cycle lengths on E=6 shell")

    # Verify record-capacity bound |A_read| <= floor(sqrt(B/2)) on all u-v=2 states with E<=15
    cap_checked = 0
    for e_val in range(2, 16):
        b_equiv = e_val - 2
        bound = math.isqrt(b_equiv // 2)
        for q in range(-3, 4):
            for p in range(-3, 4):
                for u in range(-3, 4):
                    v = u - 2
                    if abs(v) > 3:
                        continue
                    if cost_h(q, p, u, v) <= e_val:
                        cap_checked += 1
                        a_read = (u * u - v * v) // 4
                        if abs(a_read) > bound:
                            raise AssertionError(f"capacity bound violated: |{a_read}| > {bound}")

    sorted_cycles = ",".join(f"{k}:{cycle_hist[k]}" for k in sorted(cycle_hist))
    lines.append(
        f"ATTACK_6 RESOURCES_AND_ORBITS: budget_cases={budget_cases} "
        f"accepted_runs={accepted_runs} rejected_runs={rejected_runs} "
        f"K5_B52_refs=(6,4) K5_B52_work=50 B3_end=(1,0,1,-1,2,-1) "
        f"zero_ref_costs=(1,1) period_s4_pos={period_pos} period_s4_neg={period_neg} "
        f"E6_states={len(shell_e6)} E6_cycle_spectrum=[{sorted_cycles}] "
        f"capacity_states_checked={cap_checked} control_bits_cardinality=16 STATUS=PASS"
    )
    return lines


def main() -> int:
    out: list[str] = []
    out.append("R2_INDEPENDENT_BREAKER C-FUNDED-AREA-INDEPENDENT-REVIEW-N")
    out.extend(audit_attack_1_and_2())
    out.extend(audit_attack_3_and_4())
    out.extend(audit_attack_5())
    out.extend(audit_attack_6())
    out.append("OVERALL_VERDICT: CONFIRMED_IN_SCOPE (0 COUNTEREXAMPLES, ALL MANDATORY ATTACKS PASSED)")
    sys.stdout.write("\n".join(out) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
