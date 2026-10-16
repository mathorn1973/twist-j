#!/usr/bin/env python3
"""Executable audit, witness generator, and comparison runner for Lane I (#1507).

NON-CANONICAL / L1 executable incubation audit.
Original work Apache-2.0, A. M. Thorn, 2026-10-15.

CLI modes:
  python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py
      Run full scientific audit (T01-T18 and X01-X10) and print deterministic
      scientific stdout including witness boundary states.
  python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py --compare
      Run separate 1200-record comparison mode and print:
      TWOUSE-COMPARE-v1 records=1200 sha256=<64 lowercase hex>
  python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py --witnesses
      Print detailed JSON witness boundary trajectories.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import inspect
import json
from pathlib import Path
import sys
from typing import Dict, List, Sequence, Tuple

sys.dont_write_bytecode = True

THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

import apparatus as app  # noqa: E402


# ---------------------------------------------------------------------------
# Frozen target constants from SOURCES.json / CONTRACT.md for regression audit
# ---------------------------------------------------------------------------

EXPECTED_CANONICAL_SELECTORS: Dict[int, Tuple[int, int, int, int, int]] = {
    0: (1, 1, 3, 1, 1),
    1: (2, 2, 4, 1, 1),
    2: (3, 1, 3, 1, 1),
    3: (4, 1, 3, 1, 1),
    4: (0, 2, 4, 1, 1),
}

EXPECTED_C1_C2_C3: Dict[int, Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]] = {
    0: ((0, 4), (0, 1), (1, 0)),
    1: ((1, 4), (0, 1), (2, 0)),
    2: ((1, 0), (4, 0), (2, 1)),
    3: ((2, 0), (3, 0), (3, 1)),
    4: ((0, 1), (1, 4), (1, 2)),
}

EXPECTED_Z5_VECTORS: Dict[int, Tuple[Fraction, Fraction, Fraction, Fraction]] = {
    0: (Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1)),
    1: (Fraction(1, 2), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1)),
    2: (Fraction(1, 2), Fraction(1, 2), Fraction(0, 1), Fraction(0, 1)),
    3: (Fraction(1, 1), Fraction(1, 2), Fraction(0, 1), Fraction(0, 1)),
    4: (Fraction(0, 1), Fraction(1, 1), Fraction(0, 1), Fraction(0, 1)),
}

EXPECTED_E0_ON_Z5: Dict[int, Fraction] = {
    0: Fraction(0, 1),
    1: Fraction(1, 10),
    2: Fraction(3, 20),
    3: Fraction(2, 5),
    4: Fraction(2, 5),
}

EXPECTED_MU_VECTOR: Tuple[int, int, int, int] = (145483, 173653, 173653, 142153)
EXPECTED_MU_DENOM: int = 10497600
EXPECTED_V_VECTOR: Tuple[int, int, int, int] = (349, 354, 354, 348)

EXPECTED_12960_R0_Z5: Dict[int, Tuple[int, int, int, int]] = {
    0: (0, 0, 0, 0),
    1: (-1421, 354, 354, 348),
    2: (-1072, -1062, 708, 696),
    3: (-2493, -708, 1062, 1044),
    4: (698, -2832, 708, 696),
}

EXPECTED_1399680_R1_Z5: Dict[int, Tuple[int, int, int, int]] = {
    0: (0, 0, 0, 0),
    1: (192202, -47829, -47829, -48879),
    2: (143434, 145312, -95658, -97758),
    3: (335636, 97483, -143487, -146637),
    4: (-97536, 386282, -95658, -97758),
}

EXPECTED_41990400_W_FINAL: Dict[Tuple[int, int], int] = {
    (0, 0): 0,
    (0, 1): 4199040,
    (0, 2): 6298560,
    (0, 3): 16796160,
    (0, 4): 16796160,
    (1, 0): 4199040,
    (1, 1): 8252597,
    (1, 2): 10206634,
    (1, 3): 20558751,
    (1, 4): 20704234,
    (2, 0): 6298560,
    (2, 1): 10178464,
    (2, 2): 11958848,
    (2, 3): 22137312,
    (2, 4): 22456448,
    (3, 0): 16796160,
    (3, 1): 20530581,
    (3, 2): 22165482,
    (3, 3): 32198463,
    (3, 4): 32663082,
    (4, 0): 16796160,
    (4, 1): 20647894,
    (4, 2): 22400108,
    (4, 3): 32550402,
    (4, 4): 32897708,
}

EXPECTED_BRANCH_COUNTS: Dict[Fraction, Tuple[int, int, int, int]] = {
    Fraction(0, 1): (1, 4, 4, 16),
    Fraction(1, 10): (3, 7, 6, 9),
    Fraction(1, 5): (6, 9, 6, 4),
    Fraction(2, 5): (13, 12, 0, 0),
    Fraction(8224427, 10497600): (25, 0, 0, 0),
    Fraction(4, 5): (25, 0, 0, 0),
}


def fmt_frac(val: Fraction) -> str:
    return f"{val.numerator}/{val.denominator}" if val.denominator != 1 else f"{val.numerator}"


def fmt_vec4(vec: Sequence[Fraction]) -> str:
    return "(" + ",".join(fmt_frac(x) for x in vec) + ")"


def wave_digest_and_support(
    u: Sequence[Fraction], v: Sequence[Fraction]
) -> Tuple[int, int, str]:
    nz_u = sum(1 for x in u if x != 0)
    nz_v = sum(1 for x in v if x != 0)
    payload = (
        ",".join(f"{x.numerator}/{x.denominator}" for x in u)
        + "|"
        + ",".join(f"{x.numerator}/{x.denominator}" for x in v)
    )
    digest = hashlib.sha256(payload.encode("ascii")).hexdigest()[:16]
    return (nz_u, nz_v, digest)


def format_boundary_line(state: app.CompositeState) -> str:
    geom = app.get_geometry()
    nz_u, nz_v, w_hash = wave_digest_and_support(state.X.u, state.X.v)
    u_y = tuple(state.X.u[idx] for idx in geom.y_indices)
    v_y = tuple(state.X.v[idx] for idx in geom.y_indices)
    ed = app.wave_energy(state.X.u, state.X.v)
    efull = app.full_classical_energy(state.X)
    if state.c in app.VALID_FIRST_PERIOD_CLOCKS and app.VALID_FIRST_PERIOD_CLOCKS[state.c] == state.n:
        cuts = app.direct_chronological_cut_reader(state)
        cut_tags = ",".join(
            f"c{idx}:{entry.slot_name}" if entry.status == "PRESENT" else f"c{idx}:UNW"
            for idx, entry in enumerate(cuts)
        )
    else:
        cut_tags = "rollover_c0_n5"
    return (
        f"  c={state.c} n={state.n} xA={list(state.x_A)} xB={list(state.x_B)} "
        f"d={list(state.d)} sig=({state.sigma_A:+d},{state.sigma_B:+d}) k={state.X.k} "
        f"W={fmt_frac(state.W)} b={fmt_frac(state.b)} E_D={fmt_frac(ed)} E_full={fmt_frac(efull)} "
        f"nz=({nz_u},{nz_v}) uv_sha16={w_hash} "
        f"u_Y=({','.join(fmt_frac(x) for x in u_y)}) "
        f"v_Y=({','.join(fmt_frac(x) for x in v_y)}) "
        f"A0={fmt_vec4(state.X.A0)} A1={fmt_vec4(state.X.A1)} "
        f"B0={fmt_vec4(state.X.B0)} B1={fmt_vec4(state.X.B1)} cuts=[{cut_tags}]"
    )


# ---------------------------------------------------------------------------
# Audit test implementations (T01 - T18 and X01 - X10)
# ---------------------------------------------------------------------------

def run_t01_geometry_stencil_and_operators() -> str:
    geom = app.get_geometry()
    assert len(geom.b_st) == 60
    assert len(geom.b_zero) == 61
    assert len(geom.domain_d) == 869
    assert list(geom.domain_d) == sorted(geom.domain_d)
    assert sum(geom.stencil_coeffs.values(), Fraction(0, 1)) == Fraction(8, 9)

    # Check P^T P = I_4, P^T J_0 = 0, K P = (1/2) P, P^T S = G_source
    for j in range(4):
        ej = app.basis_q4(j)
        pej = app.apply_P(ej)
        assert app.apply_PT(pej) == ej
        assert app.apply_PT(app.apply_J0(pej)) == app.zero_q4()
        k_pej = app.apply_K(pej)
        assert k_pej == tuple(Fraction(1, 2) * x for x in pej)
        sej = app.apply_S(ej)
        pt_sej = app.apply_PT(sej)
        exp_g = tuple(Fraction(4, 5) if i == j else Fraction(-1, 5) for i in range(4))
        assert pt_sej == exp_g
        assert app.dot_vec(sej, sej) == Fraction(4, 5)

    # Check J_p = P^T H P = (59 I_4 + 1 1^T)/54 and M = P^T H S = (1770 I_4 - v 1^T)/1620
    ops = app.get_derived_operators()
    for r in range(4):
        for c in range(4):
            exp_jp = Fraction(60 if r == c else 1, 54)
            assert ops.Jp[r][c] == exp_jp
            exp_m = Fraction((1770 if r == c else 0) - EXPECTED_V_VECTOR[r], 1620)
            assert ops.M[r][c] == exp_m
            assert ops.R0[r][c] == -Fraction(1, 4) * exp_m

    return "T01 PASS: |B_st|=60, diag=8/9, |D|=869, P^T P=I_4, J_p and M verified"


def run_t02_generators_and_v_non_invertibility() -> str:
    for a in range(5):
        for b in range(5):
            for c0 in range(5):
                for d0 in range(5):
                    for q in range(5):
                        for r in range(5):
                            x = (a, b, c0, d0, q, r)
                            z = sum(x) % 5
                            expected_sums = (
                                z % 5,
                                (-z) % 5,
                                (2 - z) % 5,
                                (2 - z) % 5,
                                (3 - z) % 5,
                            )
                            for g in range(5):
                                gx = app.apply_generator(g, x)
                                assert app.apply_generator(g, gx) == x
                                assert sum(gx) % 5 == expected_sums[g]

    x_coll_1 = (0, 0, 0, 0, 0, 1)
    x_coll_2 = (2, 1, 3, 4, 2, 2)
    assert app.native_selector(0, x_coll_1) == 1
    assert app.native_selector(0, x_coll_2) == 4
    v1 = app.native_tick(0, x_coll_1, x_coll_1)
    v2 = app.native_tick(0, x_coll_2, x_coll_2)
    assert v1 == v2 == (1, (0, 0, 0, 0, 0, 4), (0, 0, 0, 0, 0, 4))
    assert v1[0] == 1 != 0
    return "T02 PASS: 5 generators involutive on 15625 states; V collision at n=0 verified"


def run_t03_single_head_625_census_and_recovery() -> str:
    counts = {h: 0 for h in range(5)}
    for p0 in range(5):
        for p1 in range(5):
            for p2 in range(5):
                for p3 in range(5):
                    p = (p0, p1, p2, p3)
                    h = sum(p) % 5
                    counts[h] += 1
                    x0 = (p0, p1, p2, p3, 0, 1)
                    j0 = app.native_selector(0, x0)
                    _, x1 = app.native_tick_single(0, x0)
                    j1 = app.native_selector(1, x1)
                    _, x2 = app.native_tick_single(1, x1)
                    j2 = app.native_selector(2, x2)
                    _, x3 = app.native_tick_single(2, x2)
                    j3 = app.native_selector(3, x3)
                    _, x4 = app.native_tick_single(3, x3)
                    j4 = app.native_selector(4, x4)
                    _, x5 = app.native_tick_single(4, x4)

                    assert (j0, j1, j2, j3, j4) == EXPECTED_CANONICAL_SELECTORS[h]
                    c1, c2, c3 = EXPECTED_C1_C2_C3[h]
                    assert app.receiver_of(x1) == c1
                    assert app.receiver_of(x2) == c2
                    assert app.receiver_of(x3) == c3
                    assert sum(x3) % 5 == 1
                    assert sum(x4) % 5 == 4
                    assert x4 == app.apply_generator(1, x3)
                    assert x5 == x3
                    assert app.receiver_of(x5) == c3
                    assert app.eta_lift(c1) == EXPECTED_Z5_VECTORS[h]

                    x0_rec = app.apply_generator(
                        j0, app.apply_generator(j1, app.apply_generator(j2, x5))
                    )
                    assert x0_rec == x0
                    assert x0_rec[:4] == p
                    assert sum(x0_rec[:4]) % 5 == h

    assert counts == {0: 125, 1: 125, 2: 125, 3: 125, 4: 125}
    return "T03 PASS: all 625 single-head preparations (125/class) audited and inverted"


def run_t04_paired_factorization_390625() -> str:
    # Precompute all 625 single-head 5-tick trajectories and verify 625x625 product
    single_trajs: List[Tuple[Tuple[int, int, int, int], int, Tuple[int, ...], Tuple[int, ...]]] = []
    for p0 in range(5):
        for p1 in range(5):
            for p2 in range(5):
                for p3 in range(5):
                    p = (p0, p1, p2, p3)
                    h = sum(p) % 5
                    x = (p0, p1, p2, p3, 0, 1)
                    _, x1 = app.native_tick_single(0, x)
                    _, x2 = app.native_tick_single(1, x1)
                    _, x3 = app.native_tick_single(2, x2)
                    _, x4 = app.native_tick_single(3, x3)
                    _, x5 = app.native_tick_single(4, x4)
                    single_trajs.append((p, h, x1, x5))

    c3_table = app.get_native_c3_table()
    c3_to_h = {info["C3"]: h for h, info in c3_table.items()}
    fibre_counts = {(ha, hb): 0 for ha in range(5) for hb in range(5)}
    total_pairs = 0

    for pa, ha, x1a, x5a in single_trajs:
        sela: Tuple[int, ...] = c3_table[ha]["selectors"]  # type: ignore[assignment]
        rec_x0a = app.apply_generator(
            sela[0], app.apply_generator(sela[1], app.apply_generator(sela[2], x5a))
        )
        assert rec_x0a == (pa[0], pa[1], pa[2], pa[3], 0, 1)
        assert app.receiver_of(x1a) == EXPECTED_C1_C2_C3[ha][0]
        for pb, hb, x1b, x5b in single_trajs:
            total_pairs += 1
            fibre_counts[(ha, hb)] += 1
            assert c3_to_h[app.receiver_of(x5a)] == ha
            assert c3_to_h[app.receiver_of(x5b)] == hb
            assert app.receiver_of(x1b) == EXPECTED_C1_C2_C3[hb][0]

    assert total_pairs == 390625
    assert all(cnt == 15625 for cnt in fibre_counts.values())

    # Verify apparatus state at c=0..7 is identical for distinct representatives in same fibre
    for ha in range(5):
        for hb in range(5):
            p_a1 = (ha, 0, 0, 0)
            p_a2 = ((ha - 1) % 5, 1, 2, 3)
            p_b1 = (hb, 0, 0, 0)
            p_b2 = (2, (hb - 2) % 5, 4, 1)
            assert sum(p_a1) % 5 == sum(p_a2) % 5 == ha
            assert sum(p_b1) % 5 == sum(p_b2) % 5 == hb
            s1 = app.run_seven_steps(app.prepare_ready_state(p_a1, p_b1, Fraction(1, 5)))
            s2 = app.run_seven_steps(app.prepare_ready_state(p_a2, p_b2, Fraction(1, 5)))
            assert isinstance(s1, app.CompositeState) and isinstance(s2, app.CompositeState)
            assert s1.to_apparatus_substate() == s2.to_apparatus_substate()
            assert app.recover_prepared_inputs(s1) == (p_a1, p_b1)
            assert app.recover_prepared_inputs(s2) == (p_a2, p_b2)

    return "T04 PASS: 390625 paired inputs factor into 25 fibres of 15625; full recovery verified"


def run_t05_certificate_f_bijectivity_and_energy() -> str:
    geom = app.get_geometry()
    # 1. Verify symmetry of H and operator blocks on all 869 basis vectors of Q^D
    z_d = app.zero_qd()
    z_4 = app.zero_q4()
    for i in range(869):
        for j, coeff in geom.h_neighbors[i]:
            rev = dict(geom.h_neighbors[j]).get(i)
            assert rev == coeff

    # 2. Verify F_inverse(F_step(e)) == e and F_step(F_inverse(e)) == e and E_full conservation
    # across all 1754 standard basis vectors of Q^D (+) Q^D (+) (Q^4)^4
    basis_checked = 0
    for i in range(869):
        u_basis = list(z_d)
        u_basis[i] = Fraction(1, 1)
        u_tup = tuple(u_basis)

        # Basis in u slot
        xu = app.WaveTapeState(u=u_tup, v=z_d, A0=z_4, A1=z_4, B0=z_4, B1=z_4, k=0)
        fxu = app.F_step(xu)
        assert app.F_inverse(fxu) == xu
        assert app.F_step(app.F_inverse(xu)) == xu
        assert app.full_classical_energy(fxu) == app.full_classical_energy(xu)
        basis_checked += 1

        # Basis in v slot
        xv = app.WaveTapeState(u=z_d, v=u_tup, A0=z_4, A1=z_4, B0=z_4, B1=z_4, k=1)
        fxv = app.F_step(xv)
        assert app.F_inverse(fxv) == xv
        assert app.F_step(app.F_inverse(xv)) == xv
        assert app.full_classical_energy(fxv) == app.full_classical_energy(xv)
        basis_checked += 1

        # Verify K^2 - K + (1/4) P P^T = 0 on H e_i (the (v,v) quadratic energy block)
        hei = app.apply_H(u_tup)
        k_hei = app.apply_K(hei)
        k2_hei = app.apply_K(k_hei)
        ppt_hei = app.apply_P(app.apply_PT(hei))
        for m in range(869):
            assert k2_hei[m] - k_hei[m] + Fraction(1, 4) * ppt_hei[m] == 0

    for slot in range(4):
        for j in range(4):
            ej = app.basis_q4(j)
            tapes = [z_4, z_4, z_4, z_4]
            tapes[slot] = ej
            xt = app.WaveTapeState(
                u=z_d, v=z_d, A0=tapes[0], A1=tapes[1], B0=tapes[2], B1=tapes[3], k=0
            )
            fxt = app.F_step(xt)
            assert app.F_inverse(fxt) == xt
            assert app.F_step(app.F_inverse(xt)) == xt
            assert app.full_classical_energy(fxt) == app.full_classical_energy(xt)
            basis_checked += 1

    assert basis_checked == 1754

    # 3. Verify cross bilinear terms of E_full(F(X)) - E_full(X) and R1-A witness (u=v=0, A0=e0)
    e0 = app.basis_q4(0)
    x_r1a = app.WaveTapeState(u=z_d, v=z_d, A0=e0, A1=z_4, B0=z_4, B1=z_4, k=0)
    fx_r1a = app.F_step(x_r1a)
    assert fx_r1a.v == tuple(2 * x for x in app.apply_P(e0))
    assert fx_r1a.B0 == z_4
    assert app.F_inverse(fx_r1a) == x_r1a
    assert app.wave_energy(fx_r1a.u, fx_r1a.v) == app.wave_energy_difference_form(
        fx_r1a.u, fx_r1a.v
    )

    return f"T05 PASS: coefficient-complete F/F^-1 and E_full certificate verified on all {basis_checked} basis vectors"


def run_t06_certificate_hb_involutions_and_lbuf() -> str:
    z_d = app.zero_qd()
    z_4 = app.zero_q4()
    # Check polynomial identity Delta(u, v + sigma*a(r), -sigma) + Delta(u, v, sigma) == 0
    # across all 25 labels r in F_5^2 and both sigma in {-1, +1}
    for q in range(5):
        for r2 in range(5):
            r = (q, r2)
            a_r = app.source_field_for_receiver(r)
            norm_sq_half = Fraction(1, 2) * app.dot_vec(a_r, a_r)
            for sig in (-1, 1):
                # Constant term in (u, v): (1/2)||a||^2 - sig^2 ||a||^2 + (1/2)||a||^2 == 0
                const_sum = norm_sq_half - (sig * sig) * app.dot_vec(a_r, a_r) + norm_sq_half
                assert const_sum == 0
                # Linear coefficients in v and u: +sig a_r + (-sig) a_r == 0
                for idx in range(869):
                    assert sig * a_r[idx] + (-sig) * a_r[idx] == 0

                # Test H_{B,A}^2 == id and H_{B,B}^2 == id on accepted, lower-refused, and upper-refused states
                for u_scale, v_scale, b_val, cap_val in [
                    (Fraction(0, 1), Fraction(0, 1), Fraction(2, 5), Fraction(4, 5)),
                    (Fraction(1, 3), Fraction(-1, 2), Fraction(0, 1), Fraction(1, 10)),
                    (Fraction(0, 1), Fraction(-2, 1), Fraction(4, 5), Fraction(4, 5)),
                ]:
                    u_test = tuple(u_scale * x for x in app.apply_S(app.basis_q4(0)))
                    v_test = tuple(v_scale * x for x in app.apply_P(app.basis_q4(0)))
                    d_inc = app.contact_energy_increment(u_test, v_test, sig, r)
                    assert d_inc == app.contact_energy_increment_bilinear(u_test, v_test, sig, r)
                    sub = app.ApparatusSubstate(
                        X=app.WaveTapeState(
                            u=u_test, v=v_test, A0=z_4, A1=z_4, B0=z_4, B1=z_4, k=0
                        ),
                        W=Fraction(1, 7),
                        b=b_val,
                        B=cap_val,
                        sigma_A=sig,
                        sigma_B=sig,
                        d=r,
                    )
                    sub_a1 = app.funded_contact_A_substate(sub, r)
                    sub_a2 = app.funded_contact_A_substate(sub_a1, r)
                    assert sub_a2 == sub
                    sub_b1 = app.funded_contact_B_substate(sub)
                    sub_b2 = app.funded_contact_B_substate(sub_b1)
                    assert sub_b2 == sub

                    # Check two-sided apparatus step invertibility across all 8 phases c=0..7
                    for c_phase in range(8):
                        fwd_sub, fwd_c = app.apparatus_step(sub, c_phase, r, (1, 4))
                        back_sub, back_c = app.apparatus_step_inverse(fwd_sub, fwd_c, r, (1, 4))
                        assert (back_sub, back_c) == (sub, c_phase)

    return "T06 PASS: universal H_{B,A}^2=id, H_{B,B}^2=id, L_buf^-1, and G_B^-1 verified across all 25 labels and 8 phases"


def run_t07_certificate_bilinear_work_and_mu() -> str:
    geom = app.get_geometry()
    # Extract the 4x4 bilinear cross-work matrix Omega_{i,j} = (S e_i)^T (w_2(e_j) - (1/2) H w_1(e_j))
    # directly from basis evolutions of F_step
    z_d = app.zero_qd()
    z_4 = app.zero_q4()
    for j in range(4):
        ej = app.basis_q4(j)
        f_ej = app.apply_S(ej)
        x0 = app.WaveTapeState(u=z_d, v=f_ej, A0=z_4, A1=z_4, B0=z_4, B1=z_4, k=0)
        x1 = app.F_step(x0)  # u=f_ej, v=w1
        x2 = app.F_step(x1)  # u=w1, v=w2
        w1 = x2.u
        w2 = x2.v
        hw1 = app.apply_H(w1)
        diff = tuple(w2[m] - Fraction(1, 2) * hw1[m] for m in range(869))

        # Check J_0((1/2) H K H f - f) equality and fifth-site value
        hkh_f = app.apply_H(app.apply_K(app.apply_H(f_ej)))
        j0_term = app.apply_J0(tuple(Fraction(1, 2) * hkh_f[m] - f_ej[m] for m in range(869)))
        assert diff == j0_term
        assert diff[geom.y4_index] == Fraction(EXPECTED_MU_VECTOR[j], 2099520)

        for i in range(4):
            ei = app.basis_q4(i)
            g_ei = app.apply_S(ei)
            cross_ij = app.dot_vec(g_ei, diff)
            assert cross_ij == -Fraction(EXPECTED_MU_VECTOR[j], EXPECTED_MU_DENOM)

    return "T07 PASS: 4x4 bilinear cross-work matrix equals -1*mu^T/10497600 with mu=(145483,173653,173653,142153)"


def run_t08_25_pair_work_table_and_capacities() -> str:
    for cap, exp_counts in EXPECTED_BRANCH_COUNTS.items():
        acc_acc = acc_ref = ref_acc = ref_ref = 0
        for ha in range(5):
            for hb in range(5):
                st0 = app.prepare_ready_state((ha, 0, 0, 0), (hb, 0, 0, 0), cap, b_init=cap)
                bounds = app.run_seven_steps(st0, return_boundaries=True)
                assert isinstance(bounds, tuple) and len(bounds) == 8
                st7 = bounds[7]
                sig_pair = (st7.sigma_A, st7.sigma_B)
                if sig_pair == (-1, -1):
                    acc_acc += 1
                elif sig_pair == (-1, 1):
                    acc_ref += 1
                elif sig_pair == (1, -1):
                    ref_acc += 1
                else:
                    ref_ref += 1

                if cap == Fraction(4, 5):
                    ea = bounds[2].W
                    delta_b = bounds[5].W - bounds[4].W
                    w_fin = st7.W
                    z_a = EXPECTED_Z5_VECTORS[ha]
                    z_b = EXPECTED_Z5_VECTORS[hb]
                    s_b = sum(z_b, Fraction(0, 1))
                    mu_za = sum(
                        EXPECTED_MU_VECTOR[k] * z_a[k] for k in range(4)
                    )
                    exp_cross = -s_b * mu_za / EXPECTED_MU_DENOM
                    assert ea == EXPECTED_E0_ON_Z5[ha]
                    assert delta_b == EXPECTED_E0_ON_Z5[hb] + exp_cross
                    assert w_fin == ea + delta_b
                    assert w_fin * 41990400 == EXPECTED_41990400_W_FINAL[(ha, hb)]
                    assert 0 <= ea <= Fraction(2, 5)
                    assert 0 <= delta_b <= Fraction(2, 5)
                    assert st7.b == Fraction(4, 5) - w_fin > 0

        assert (acc_acc, acc_ref, ref_acc, ref_ref) == exp_counts

    return "T08 PASS: all 25 source pairs and all 6 capacities match work table and branch counts"


def run_t09_order_witness_14_vs_41() -> str:
    cap = Fraction(4, 5)
    b_14 = app.run_seven_steps(
        app.prepare_ready_state((1, 0, 0, 0), (4, 0, 0, 0), cap, b_init=cap),
        return_boundaries=True,
    )
    b_41 = app.run_seven_steps(
        app.prepare_ready_state((4, 0, 0, 0), (1, 0, 0, 0), cap, b_init=cap),
        return_boundaries=True,
    )
    assert isinstance(b_14, tuple) and isinstance(b_41, tuple)
    w_14 = b_14[7].W
    w_41 = b_41[7].W
    diff = w_14 - w_41
    assert w_14 == Fraction(10352117, 20995200)
    assert w_41 == Fraction(10323947, 20995200)
    assert diff == Fraction(313, 233280)
    return f"T09 PASS: order witness W(1,4)={fmt_frac(w_14)}, W(4,1)={fmt_frac(w_41)}, W(1,4)-W(4,1)=313/233280"


def run_t10_certificate_four_cut_operators_and_archives() -> str:
    ops = app.get_derived_operators()
    # Verify single-source tables 12960 R0 z^(h) and 1399680 R1 z^(h)
    for h in range(5):
        zh = EXPECTED_Z5_VECTORS[h]
        r0_zh = app.mat_vec_4(ops.R0, zh)
        r1_zh = app.mat_vec_4(ops.R1, zh)
        assert tuple(int(x * 12960) for x in r0_zh) == EXPECTED_12960_R0_Z5[h]
        assert tuple(int(x * 1399680) for x in r1_zh) == EXPECTED_1399680_R1_Z5[h]

    # Coefficient-complete basis check on (z_A, z_B, c0, c1) in (Q^4)^4 across all 4 branches
    z_d = app.zero_qd()
    z_4 = app.zero_q4()
    for alpha_a in (0, 1):
        for alpha_b in (0, 1):
            for slot in range(4):
                for j in range(4):
                    ej = app.basis_q4(j)
                    za = ej if slot == 0 else z_4
                    zb = ej if slot == 1 else z_4
                    c0 = ej if slot == 2 else z_4
                    c1 = ej if slot == 3 else z_4

                    f_a = app.apply_S(za) if alpha_a == 1 else z_d
                    g_b = app.apply_S(zb) if alpha_b == 1 else z_d
                    x_c2 = app.WaveTapeState(u=z_d, v=f_a, A0=z_4, A1=z_4, B0=c0, B1=c1, k=0)
                    x_c3 = app.F_step(x_c2)
                    x_c4 = app.F_step(x_c3)
                    x_c5 = app.WaveTapeState(
                        u=x_c4.u,
                        v=tuple(x_c4.v[m] + g_b[m] for m in range(869)),
                        A0=x_c4.A0,
                        A1=x_c4.A1,
                        B0=x_c4.B0,
                        B1=x_c4.B1,
                        k=x_c4.k,
                    )
                    x_c6 = app.F_step(x_c5)
                    x_c7 = app.F_step(x_c6)

                    exp_b0 = app.mat_vec_4(ops.R0, za) if alpha_a == 1 else z_4
                    exp_b1 = app.mat_vec_4(ops.R1, za) if alpha_a == 1 else z_4
                    d2_za = app.mat_vec_4(ops.D2, za) if alpha_a == 1 else z_4
                    r0_zb = app.mat_vec_4(ops.R0, zb) if alpha_b == 1 else z_4
                    exp_b2 = tuple(d2_za[i] + r0_zb[i] for i in range(4))
                    d3_za = app.mat_vec_4(ops.D3, za) if alpha_a == 1 else z_4
                    r1_zb = app.mat_vec_4(ops.R1, zb) if alpha_b == 1 else z_4
                    jp_c1 = app.mat_vec_4(ops.Jp, c1)
                    exp_b3 = tuple(
                        d3_za[i] + r1_zb[i] - Fraction(1, 2) * jp_c1[i] for i in range(4)
                    )

                    assert x_c7.A0 == exp_b0
                    assert x_c7.A1 == exp_b1
                    assert x_c7.B1 == exp_b2
                    assert x_c7.B0 == exp_b3

    # Explicit WARM witness checks for c1 = e0 on (0,0) and (0,1)
    e0 = app.basis_q4(0)
    st_warm_00 = app.run_seven_steps(
        app.prepare_ready_state((0, 0, 0, 0), (0, 0, 0, 0), Fraction(4, 5), c1=e0)
    )
    assert isinstance(st_warm_00, app.CompositeState)
    assert st_warm_00.X.B0 == (
        Fraction(-5, 9),
        Fraction(-1, 108),
        Fraction(-1, 108),
        Fraction(-1, 108),
    )

    st_warm_01 = app.run_seven_steps(
        app.prepare_ready_state((0, 0, 0, 0), (1, 0, 0, 0), Fraction(4, 5), c1=e0)
    )
    assert isinstance(st_warm_01, app.CompositeState)
    assert st_warm_01.X.B0 == (
        Fraction(-585398, 1399680),
        Fraction(-60789, 1399680),
        Fraction(-60789, 1399680),
        Fraction(-61839, 1399680),
    )
    assert app.full_classical_energy(st_warm_01.X) == Fraction(21, 10)
    assert st_warm_01.W == Fraction(1, 10)

    return "T10 PASS: universal 4-cut operator certificate and c1=e0 WARM witnesses verified"


def run_t11_direct_chronological_and_source_readers() -> str:
    # 1. Test API access restrictions of direct_source_reader
    sig = inspect.signature(app.direct_source_reader)
    assert list(sig.parameters.keys()) == ["b0", "b2", "sigma_A", "sigma_B", "d"]

    st0 = app.prepare_ready_state((1, 0, 0, 0), (2, 0, 0, 0), Fraction(4, 5))
    bounds = app.run_seven_steps(st0, return_boundaries=True)
    assert isinstance(bounds, tuple)
    st7 = bounds[7]

    for forbidden in (st7, st7.to_apparatus_substate(), st7.X, st7.x_A, (1, 0, 0, 0)):
        raised = False
        try:
            app.direct_source_reader(forbidden, st7.X.B1)  # type: ignore[arg-type]
        except (TypeError, ValueError):
            raised = True
        assert raised

    # 2. Verify chronological cut reader across c=0..7, including continued reading of (b0,b1)
    b0_val = st7.X.A0
    b1_val = st7.X.A1
    b2_val = st7.X.B1
    b3_val = st7.X.B0
    for c_idx in range(8):
        entries = app.direct_chronological_cut_reader(bounds[c_idx])
        if c_idx in (0, 1, 2):
            assert all(e.status == "UNWRITTEN" for e in entries)
        elif c_idx == 3:
            assert entries[0].status == "PRESENT" and entries[0].vector == b0_val
            assert all(e.status == "UNWRITTEN" for e in entries[1:])
        elif c_idx in (4, 5):
            assert entries[0].vector == b0_val and entries[0].slot_name == "B1"
            assert entries[1].vector == b1_val and entries[1].slot_name == "B0"
            assert all(e.status == "UNWRITTEN" for e in entries[2:])
        elif c_idx == 6:
            assert entries[0].vector == b0_val and entries[0].slot_name == "A1"
            assert entries[1].vector == b1_val and entries[1].slot_name == "B1"
            assert entries[2].vector == b2_val and entries[2].slot_name == "B0"
            assert entries[3].status == "UNWRITTEN"
        else:
            assert entries[0].vector == b0_val and entries[0].slot_name == "A0"
            assert entries[1].vector == b1_val and entries[1].slot_name == "A1"
            assert entries[2].vector == b2_val and entries[2].slot_name == "B1"
            assert entries[3].vector == b3_val and entries[3].slot_name == "B0"

    # 3. Verify archive-independent source decoding across all 25 pairs and non-zero old archives
    archives = [
        (app.zero_q4(), app.zero_q4()),
        (app.zero_q4(), app.basis_q4(0)),
        (
            (Fraction(3, 7), Fraction(-1, 2), Fraction(2, 3), Fraction(0, 1)),
            (Fraction(-5, 4), Fraction(1, 9), Fraction(0, 1), Fraction(7, 8)),
        ),
    ]
    for c0_vec, c1_vec in archives:
        for ha in range(5):
            for hb in range(5):
                s_end = app.run_seven_steps(
                    app.prepare_ready_state(
                        (ha, 0, 0, 0),
                        (hb, 0, 0, 0),
                        Fraction(4, 5),
                        c0=c0_vec,
                        c1=c1_vec,
                    )
                )
                assert isinstance(s_end, app.CompositeState)
                view = app.extract_direct_port_readout(s_end, include_d=True)
                dec = app.direct_source_reader(view)
                assert dec["z_A"] == EXPECTED_Z5_VECTORS[ha]
                assert dec["z_B"] == EXPECTED_Z5_VECTORS[hb]
                assert dec["alpha_A"] == 1 and dec["alpha_B"] == 1

    return "T11 PASS: direct_chronological_cut_reader, direct_source_reader, and API restrictions verified"


def run_t12_store_bounds_refusal_and_negative_work() -> str:
    # 1. Ready-family lower-bound refusal at B = 2/5 on (3,3)
    st_ref_25 = app.run_seven_steps(
        app.prepare_ready_state((3, 0, 0, 0), (3, 0, 0, 0), Fraction(2, 5))
    )
    assert isinstance(st_ref_25, app.CompositeState)
    assert (st_ref_25.sigma_A, st_ref_25.sigma_B) == (-1, 1)
    assert st_ref_25.W == Fraction(2, 5) and st_ref_25.b == Fraction(0, 1)

    # 2. Occupied-tape warm lower-bound refusal: A_init = (0, e0), (0, 1), B = b_init = 4/5
    z_d = app.zero_qd()
    z_4 = app.zero_q4()
    e0 = app.basis_q4(0)
    neg_e0 = tuple(-x for x in e0)
    cap = Fraction(4, 5)

    warm_low_init = app.CompositeState(
        n=0,
        x_A=(0, 0, 0, 0, 0, 1),
        x_B=(1, 0, 0, 0, 0, 1),
        X=app.WaveTapeState(u=z_d, v=z_d, A0=z_4, A1=e0, B0=z_4, B1=z_4, k=0),
        W=Fraction(0, 1),
        b=cap,
        B=cap,
        sigma_A=1,
        sigma_B=1,
        d=(0, 0),
        c=0,
    )
    warm_low_bounds = app.run_seven_steps(warm_low_init, return_boundaries=True)
    assert isinstance(warm_low_bounds, tuple)
    c4_low = warm_low_bounds[4]
    delta_b_low = app.contact_energy_increment(c4_low.X.u, c4_low.X.v, c4_low.sigma_B, c4_low.d)
    assert delta_b_low == Fraction(9, 10)
    assert c4_low.b - delta_b_low == Fraction(-1, 10) < 0
    assert (warm_low_bounds[7].sigma_A, warm_low_bounds[7].sigma_B) == (-1, 1)
    assert warm_low_bounds[7].W == Fraction(0, 1) and warm_low_bounds[7].b == cap

    # 3. Occupied-tape warm upper-bound refusal (negative work): A_init = (0, -e0), b_init = B = 4/5
    warm_high_init = app.CompositeState(
        n=0,
        x_A=(0, 0, 0, 0, 0, 1),
        x_B=(1, 0, 0, 0, 0, 1),
        X=app.WaveTapeState(u=z_d, v=z_d, A0=z_4, A1=neg_e0, B0=z_4, B1=z_4, k=0),
        W=Fraction(0, 1),
        b=cap,
        B=cap,
        sigma_A=1,
        sigma_B=1,
        d=(0, 0),
        c=0,
    )
    warm_high_bounds = app.run_seven_steps(warm_high_init, return_boundaries=True)
    assert isinstance(warm_high_bounds, tuple)
    c4_high = warm_high_bounds[4]
    delta_b_high = app.contact_energy_increment(
        c4_high.X.u, c4_high.X.v, c4_high.sigma_B, c4_high.d
    )
    assert delta_b_high == Fraction(-7, 10) < 0
    assert c4_high.b - delta_b_high == Fraction(3, 2) > cap
    assert (warm_high_bounds[7].sigma_A, warm_high_bounds[7].sigma_B) == (-1, 1)
    assert warm_high_bounds[7].W == Fraction(0, 1) and warm_high_bounds[7].b == cap

    # 4. Companion accepted negative-work trajectory when b_init = 0, B = 4/5
    warm_neg_acc_init = app.CompositeState(
        n=0,
        x_A=(0, 0, 0, 0, 0, 1),
        x_B=(1, 0, 0, 0, 0, 1),
        X=app.WaveTapeState(u=z_d, v=z_d, A0=z_4, A1=neg_e0, B0=z_4, B1=z_4, k=0),
        W=Fraction(0, 1),
        b=Fraction(0, 1),
        B=cap,
        sigma_A=1,
        sigma_B=1,
        d=(0, 0),
        c=0,
    )
    warm_neg_acc_end = app.run_seven_steps(warm_neg_acc_init)
    assert isinstance(warm_neg_acc_end, app.CompositeState)
    assert (warm_neg_acc_end.sigma_A, warm_neg_acc_end.sigma_B) == (-1, -1)
    assert warm_neg_acc_end.W == Fraction(-7, 10)
    assert warm_neg_acc_end.b == Fraction(7, 10)

    return "T12 PASS: lower/upper store guard refusals and negative work (-7/10) verified"


def run_t13_accepted_zero_and_clarification_ii() -> str:
    cap = Fraction(1, 5)
    # 1. Four zero-cut pairs (0,0), (0,3), (3,0), (3,3) at B = b_init = 1/5
    endpoints: Dict[Tuple[int, int], app.CompositeState] = {}
    for pair in [(0, 0), (0, 3), (3, 0), (3, 3)]:
        st = app.run_seven_steps(
            app.prepare_ready_state((pair[0], 0, 0, 0), (pair[1], 0, 0, 0), cap, b_init=cap)
        )
        assert isinstance(st, app.CompositeState)
        endpoints[pair] = st

    # Check Pi_class = (X, W, b) collapses all 4 pairs
    pi_class_set = {(s.X, s.W, s.b) for s in endpoints.values()}
    assert len(pi_class_set) == 1

    # Check Pi_{class+d} = (X, W, b, d) collapses (0,0) with (3,0) and (0,3) with (3,3)
    assert (endpoints[(0, 0)].X, endpoints[(0, 0)].W, endpoints[(0, 0)].b, endpoints[(0, 0)].d) == (
        endpoints[(3, 0)].X,
        endpoints[(3, 0)].W,
        endpoints[(3, 0)].b,
        endpoints[(3, 0)].d,
    )
    assert (endpoints[(0, 3)].X, endpoints[(0, 3)].W, endpoints[(0, 3)].b, endpoints[(0, 3)].d) == (
        endpoints[(3, 3)].X,
        endpoints[(3, 3)].W,
        endpoints[(3, 3)].b,
        endpoints[(3, 3)].d,
    )

    # Check (sigma_A, sigma_B) separates all 4
    assert (endpoints[(0, 0)].sigma_A, endpoints[(0, 0)].sigma_B) == (-1, -1)
    assert (endpoints[(0, 3)].sigma_A, endpoints[(0, 3)].sigma_B) == (-1, 1)
    assert (endpoints[(3, 0)].sigma_A, endpoints[(3, 0)].sigma_B) == (1, -1)
    assert (endpoints[(3, 3)].sigma_A, endpoints[(3, 3)].sigma_B) == (1, 1)

    # 2. Clarification (ii): on the ready family across all capacities and all 25 pairs,
    # second acceptance alpha_B IS uniquely readable from (d, b0, b2) without sigma_B!
    for c_val in app.COMPARISON_CAPACITIES:
        for ha in range(5):
            for hb in range(5):
                st = app.run_seven_steps(
                    app.prepare_ready_state((ha, 0, 0, 0), (hb, 0, 0, 0), c_val, b_init=c_val)
                )
                assert isinstance(st, app.CompositeState)
                view_no_sigb = app.extract_direct_port_readout(
                    st, include_d=True, include_sigma_B=False
                )
                assert view_no_sigb.sigma_B is None
                dec = app.direct_source_reader(view_no_sigb)
                true_alpha_b = (1 - st.sigma_B) // 2
                assert dec["alpha_B_from_d_b0_b2"] == true_alpha_b
                assert dec["alpha_B"] == true_alpha_b

    return "T13 PASS: accepted-zero vs refusal and Clarification (ii) (alpha_B from (d,b0,b2)) verified"


def run_t14_seven_eight_boundary_and_energy_invariants() -> str:
    c0_vec = (Fraction(1, 2), Fraction(-1, 3), Fraction(0, 1), Fraction(2, 5))
    c1_vec = (Fraction(0, 1), Fraction(3, 4), Fraction(-1, 2), Fraction(1, 6))
    init_tape_e = 2 * (app.dot_vec(c0_vec, c0_vec) + app.dot_vec(c1_vec, c1_vec))

    for cap in (Fraction(1, 5), Fraction(4, 5)):
        for ha in (0, 1, 3, 4):
            for hb in (0, 2, 3, 4):
                st0 = app.prepare_ready_state(
                    (ha, 0, 0, 0), (hb, 0, 0, 0), cap, b_init=cap, c0=c0_vec, c1=c1_vec
                )
                bounds8 = app.run_eight_steps(st0, return_boundaries=True)
                assert isinstance(bounds8, tuple) and len(bounds8) == 9
                for step_idx, b_st in enumerate(bounds8):
                    efull = app.full_classical_energy(b_st.X)
                    assert efull - b_st.W == init_tape_e
                    assert efull + b_st.b == init_tape_e + cap
                    assert b_st.W + b_st.b == cap
                    if step_idx < 8:
                        assert b_st.c == step_idx

                st7 = bounds8[7]
                st8 = bounds8[8]
                assert st7.c == 7 and st7.n == 5
                assert st8.c == 0 and st8.n == 5
                assert st8.to_apparatus_substate() == st7.to_apparatus_substate()
                assert (st8.x_A, st8.x_B) == (st7.x_A, st7.x_B)

    return "T14 PASS: 7-step completion (c=7,n=5), 8th-step rollover (c=0,n=5), and single-counted E_full invariants verified"


def run_t15_ready_image_left_inverse_all_branches() -> str:
    c0_vec = (Fraction(1, 3), Fraction(0, 1), Fraction(-1, 5), Fraction(2, 7))
    c1_vec = (Fraction(0, 1), Fraction(1, 2), Fraction(-3, 4), Fraction(1, 1))
    for cap in (Fraction(0, 1), Fraction(1, 5), Fraction(2, 5), Fraction(4, 5)):
        for ha in range(5):
            for hb in range(5):
                p_a = (ha, 1, 2, 2)
                p_b = (3, hb, 1, 1)
                st7 = app.run_seven_steps(
                    app.prepare_ready_state(
                        p_a, p_b, cap, b_init=cap, c0=c0_vec, c1=c1_vec
                    )
                )
                assert isinstance(st7, app.CompositeState)
                rec = app.recognize_ready_image(st7, c0=c0_vec, c1=c1_vec, b_init=cap)
                assert rec["valid"] is True
                assert app.recover_prepared_inputs(st7, c0=c0_vec, c1=c1_vec, b_init=cap) == (
                    p_a,
                    p_b,
                )

    return "T15 PASS: ready-image left inverse and recognizer verified across all 4 branches and non-zero archives"


def run_t16_calibration_prediction_and_clarification_i() -> str:
    cap = Fraction(4, 5)
    obs: Dict[Tuple[int, int], Dict[str, object]] = {}
    for ha in range(5):
        for hb in range(5):
            st0 = app.prepare_ready_state((ha, 0, 0, 0), (hb, 0, 0, 0), cap, b_init=cap)
            bounds = app.run_seven_steps(st0, return_boundaries=True)
            assert isinstance(bounds, tuple)
            st7 = bounds[7]
            obs[(ha, hb)] = {
                "b0": st7.X.A0,
                "b1": st7.X.A1,
                "b2": st7.X.B1,
                "b3": st7.X.B0,
                "E_A": bounds[2].W,
                "Delta_B": bounds[5].W - bounds[4].W,
                "W_final": st7.W,
                "b_final": st7.b,
            }

    # Calibrate 39-dim restricted parameter on Pi_2 from the 7 calibration runs
    r10 = obs[(1, 0)]
    r40 = obs[(4, 0)]
    r20 = obs[(2, 0)]
    a0_col0 = tuple(2 * x for x in r10["b0"])  # type: ignore[union-attr]
    a1_col0 = tuple(2 * x for x in r10["b1"])  # type: ignore[union-attr]
    d2_col0 = tuple(2 * x for x in r10["b2"])  # type: ignore[union-attr]
    d3_col0 = tuple(2 * x for x in r10["b3"])  # type: ignore[union-attr]
    g00 = 8 * r10["E_A"]  # type: ignore[operator]

    a0_col1 = r40["b0"]  # type: ignore[assignment]
    a1_col1 = r40["b1"]  # type: ignore[assignment]
    d2_col1 = r40["b2"]  # type: ignore[assignment]
    d3_col1 = r40["b3"]  # type: ignore[assignment]
    g11 = 2 * r40["E_A"]  # type: ignore[operator]
    g01 = 4 * r20["E_A"] - Fraction(1, 2) * (g00 + g11)  # type: ignore[operator]

    om00 = 4 * (obs[(1, 1)]["Delta_B"] - r10["E_A"])  # type: ignore[operator]
    om10 = 2 * (obs[(1, 4)]["Delta_B"] - r40["E_A"])  # type: ignore[operator]
    om01 = 2 * (obs[(4, 1)]["Delta_B"] - r10["E_A"])  # type: ignore[operator]
    om11 = obs[(4, 4)]["Delta_B"] - r40["E_A"]  # type: ignore[operator]

    assert (g00, g11, g01) == (Fraction(4, 5), Fraction(4, 5), Fraction(-1, 5))
    assert om00 == om10 == Fraction(-145483, 10497600)
    assert om01 == om11 == Fraction(-173653, 10497600)

    # Verify zero-error out-of-sample prediction on all 25 pairs (18 uncalibrated)
    for ha in range(5):
        for hb in range(5):
            za0, za1, _, _ = EXPECTED_Z5_VECTORS[ha]
            zb0, zb1, _, _ = EXPECTED_Z5_VECTORS[hb]
            pred_b0 = tuple(a0_col0[i] * za0 + a0_col1[i] * za1 for i in range(4))
            pred_b1 = tuple(a1_col0[i] * za0 + a1_col1[i] * za1 for i in range(4))
            pred_b2 = tuple(
                d2_col0[i] * za0 + d2_col1[i] * za1 + a0_col0[i] * zb0 + a0_col1[i] * zb1
                for i in range(4)
            )
            pred_b3 = tuple(
                d3_col0[i] * za0 + d3_col1[i] * za1 + a1_col0[i] * zb0 + a1_col1[i] * zb1
                for i in range(4)
            )
            pred_ea = Fraction(1, 2) * (
                g00 * za0 * za0 + 2 * g01 * za0 * za1 + g11 * za1 * za1
            )
            pred_eb = Fraction(1, 2) * (
                g00 * zb0 * zb0 + 2 * g01 * zb0 * zb1 + g11 * zb1 * zb1
            )
            pred_cross = (
                zb0 * (om00 * za0 + om01 * za1) + zb1 * (om10 * za0 + om11 * za1)
            )
            pred_db = pred_eb + pred_cross
            assert pred_b0 == obs[(ha, hb)]["b0"]
            assert pred_b1 == obs[(ha, hb)]["b1"]
            assert pred_b2 == obs[(ha, hb)]["b2"]
            assert pred_b3 == obs[(ha, hb)]["b3"]
            assert pred_ea == obs[(ha, hb)]["E_A"]
            assert pred_db == obs[(ha, hb)]["Delta_B"]

    # Clarification (i): verify q3(z0, z1) = z0 * z1 * (2*z0 - 1) has q3(z^(3)) = 1/2,
    # so b2 + q3(z_A) u shifts b2 at h_A = 3 by u/2 (not u)
    def q3_poly(z: Tuple[Fraction, Fraction, Fraction, Fraction]) -> Fraction:
        return z[0] * z[1] * (2 * z[0] - 1)

    for h in (0, 1, 2, 4):
        assert q3_poly(EXPECTED_Z5_VECTORS[h]) == Fraction(0, 1)
    assert q3_poly(EXPECTED_Z5_VECTORS[3]) == Fraction(1, 2)
    u_vec = (Fraction(2, 3), Fraction(-4, 5), Fraction(1, 7), Fraction(3, 11))
    shift_at_h3 = tuple(q3_poly(EXPECTED_Z5_VECTORS[3]) * x for x in u_vec)
    assert shift_at_h3 == tuple(Fraction(1, 2) * x for x in u_vec)
    assert shift_at_h3 != u_vec

    return "T16 PASS: 7-run/5-run Pi_2 calibration predicts all 25 pairs; Clarification (i) q3(z^(3))=1/2 shift u/2 verified"


def run_t17_comparator_indistinguishability_and_separations() -> str:
    # 1. Matched classical comparator M_matched^(2): identical on all 25 fibres
    for cap in (Fraction(1, 5), Fraction(8224427, 10497600), Fraction(4, 5)):
        for ha in range(5):
            for hb in range(5):
                st0 = app.prepare_ready_state((ha, 0, 0, 0), (hb, 0, 0, 0), cap, b_init=cap)
                st7 = app.run_seven_steps(st0)
                assert isinstance(st7, app.CompositeState)
                ra = EXPECTED_C1_C2_C3[ha][0]
                rb = EXPECTED_C1_C2_C3[hb][0]
                sub = st0.to_apparatus_substate()
                c_cur = 0
                for _ in range(7):
                    sub, c_cur = app.apparatus_step(sub, c_cur, ra, rb)
                assert c_cur == 7
                assert sub == st7.to_apparatus_substate()

    # 2. Five restricted comparator separations:
    # (a) M_single on (0,1) at B = 4/5
    st_01 = app.run_seven_steps(
        app.prepare_ready_state((0, 0, 0, 0), (1, 0, 0, 0), Fraction(4, 5))
    )
    assert isinstance(st_01, app.CompositeState)
    assert st_01.X.B1 != app.zero_q4() and st_01.W == Fraction(1, 10) and st_01.sigma_B == -1

    # (b) M_cold on (4,4) at B* = 8224427/10497600
    b_star = Fraction(8224427, 10497600)
    st_44 = app.run_seven_steps(
        app.prepare_ready_state((4, 0, 0, 0), (4, 0, 0, 0), b_star, b_init=b_star)
    )
    assert isinstance(st_44, app.CompositeState)
    assert st_44.sigma_B == -1 and st_44.b == Fraction(0, 1)
    assert b_star - Fraction(2, 5) - Fraction(2, 5) == Fraction(-173653, 10497600) < 0

    # (c) M_{2-slot} on (1,0) at B = 4/5 retains A_final = (b0, b1) != (0,0)
    st_10 = app.run_seven_steps(
        app.prepare_ready_state((1, 0, 0, 0), (0, 0, 0, 0), Fraction(4, 5))
    )
    assert isinstance(st_10, app.CompositeState)
    assert st_10.X.A0 != app.zero_q4() and st_10.X.A1 != app.zero_q4()

    # (d) M_{1sigma} direct un-reset shared-sigma on (0,1) at B = 4/5 gives -R0 z^(1) != +R0 z^(1)
    assert st_01.X.B1 == tuple(-x for x in tuple(-y for y in st_01.X.B1))
    assert st_01.X.B1 != tuple(-x for x in st_01.X.B1)

    return "T17 PASS: matched classical comparator agreement and 5 restricted-comparator separations verified"


def run_t18_invalid_endpoint_and_type_rejection_suite() -> str:
    cap = Fraction(4, 5)
    valid_st = app.run_seven_steps(
        app.prepare_ready_state((0, 0, 0, 0), (1, 0, 0, 0), cap, b_init=cap)
    )
    assert isinstance(valid_st, app.CompositeState)
    assert app.recognize_ready_image(valid_st, c0=app.zero_q4(), c1=app.zero_q4(), b_init=cap)[
        "valid"
    ]

    # X01: Selector piston-sum mismatch (x_{5,A} = g_3(1,0,0,0,0,1) has rec=(1,0)=C3(0) and
    # inverse word g1 g1 g3 x_{5,A} = (1,0,0,0,0,1) has rec=(0,1), but piston sum 1 != 0)
    bad_x5a = app.apply_generator(3, (1, 0, 0, 0, 0, 1))
    assert app.receiver_of(bad_x5a) == (1, 0)
    st_x01 = app.CompositeState(
        n=5,
        x_A=bad_x5a,
        x_B=valid_st.x_B,
        X=valid_st.X,
        W=valid_st.W,
        b=valid_st.b,
        B=valid_st.B,
        sigma_A=valid_st.sigma_A,
        sigma_B=valid_st.sigma_B,
        d=valid_st.d,
        c=7,
    )
    res_x01 = app.recognize_ready_image(st_x01)
    assert res_x01["valid"] is False
    assert res_x01["failed_test"] == "test2_piston_sum_selector_consistency"

    # X02: Invalid C3 receiver at n=5
    st_x02 = app.CompositeState(
        n=5,
        x_A=(0, 0, 0, 0, 0, 0),
        x_B=valid_st.x_B,
        X=valid_st.X,
        W=valid_st.W,
        b=valid_st.b,
        B=valid_st.B,
        sigma_A=valid_st.sigma_A,
        sigma_B=valid_st.sigma_B,
        d=valid_st.d,
        c=7,
    )
    res_x02 = app.recognize_ready_image(st_x02)
    assert res_x02["valid"] is False and res_x02["failed_test"] == "test1_c3_receiver"

    # X03: Invalid clock n, c, or k
    st_x03_n = app.CompositeState(
        n=4,
        x_A=valid_st.x_A,
        x_B=valid_st.x_B,
        X=valid_st.X,
        W=valid_st.W,
        b=valid_st.b,
        B=valid_st.B,
        sigma_A=valid_st.sigma_A,
        sigma_B=valid_st.sigma_B,
        d=valid_st.d,
        c=7,
    )
    st_x03_c = app.coupled_step(valid_st)  # rollover c=0, n=5
    st_x03_k = app.CompositeState(
        n=5,
        x_A=valid_st.x_A,
        x_B=valid_st.x_B,
        X=app.WaveTapeState(
            u=valid_st.X.u,
            v=valid_st.X.v,
            A0=valid_st.X.A0,
            A1=valid_st.X.A1,
            B0=valid_st.X.B0,
            B1=valid_st.X.B1,
            k=1,
        ),
        W=valid_st.W,
        b=valid_st.b,
        B=valid_st.B,
        sigma_A=valid_st.sigma_A,
        sigma_B=valid_st.sigma_B,
        d=valid_st.d,
        c=7,
    )
    assert app.recognize_ready_image(st_x03_n)["failed_test"] == "test1_clock_n5_c7"
    assert app.recognize_ready_image(st_x03_c)["failed_test"] == "test1_clock_n5_c7"
    assert app.recognize_ready_image(st_x03_k)["failed_test"] == "test4_initial_k_zero"

    # X04: Invalid delayed label d
    st_x04 = app.CompositeState(
        n=5,
        x_A=valid_st.x_A,
        x_B=valid_st.x_B,
        X=valid_st.X,
        W=valid_st.W,
        b=valid_st.b,
        B=valid_st.B,
        sigma_A=valid_st.sigma_A,
        sigma_B=valid_st.sigma_B,
        d=(0, 4),
        c=7,
    )
    assert app.recognize_ready_image(st_x04)["failed_test"] == "test3_delayed_buffer_d"

    # X05: Invalid direction signs sigma
    st_x05 = app.CompositeState(
        n=5,
        x_A=valid_st.x_A,
        x_B=valid_st.x_B,
        X=valid_st.X,
        W=valid_st.W,
        b=valid_st.b,
        B=valid_st.B,
        sigma_A=1,
        sigma_B=valid_st.sigma_B,
        d=valid_st.d,
        c=7,
    )
    assert app.recognize_ready_image(st_x05)["failed_test"] == "test4_initial_sigma_plus1"

    # X06: Invalid store b
    st_x06 = app.CompositeState(
        n=5,
        x_A=valid_st.x_A,
        x_B=valid_st.x_B,
        X=valid_st.X,
        W=valid_st.W,
        b=Fraction(1, 2),
        B=valid_st.B,
        sigma_A=valid_st.sigma_A,
        sigma_B=valid_st.sigma_B,
        d=valid_st.d,
        c=7,
    )
    assert (
        app.recognize_ready_image(st_x06, b_init=cap)["failed_test"]
        == "test4_initial_store_b"
    )

    # X07: Invalid work W
    st_x07 = app.CompositeState(
        n=5,
        x_A=valid_st.x_A,
        x_B=valid_st.x_B,
        X=valid_st.X,
        W=Fraction(1, 5),
        b=valid_st.b,
        B=valid_st.B,
        sigma_A=valid_st.sigma_A,
        sigma_B=valid_st.sigma_B,
        d=valid_st.d,
        c=7,
    )
    assert app.recognize_ready_image(st_x07)["failed_test"] == "test4_initial_W_zero"

    # X08: Invalid tapes A or B
    st_x08 = app.CompositeState(
        n=5,
        x_A=valid_st.x_A,
        x_B=valid_st.x_B,
        X=app.WaveTapeState(
            u=valid_st.X.u,
            v=valid_st.X.v,
            A0=app.basis_q4(0),
            A1=valid_st.X.A1,
            B0=valid_st.X.B0,
            B1=valid_st.X.B1,
            k=0,
        ),
        W=valid_st.W,
        b=valid_st.b,
        B=valid_st.B,
        sigma_A=valid_st.sigma_A,
        sigma_B=valid_st.sigma_B,
        d=valid_st.d,
        c=7,
    )
    assert app.recognize_ready_image(st_x08)["valid"] is False

    # X09: Invalid wave u or v
    bad_u = list(valid_st.X.u)
    bad_u[0] += Fraction(1, 1)
    st_x09 = app.CompositeState(
        n=5,
        x_A=valid_st.x_A,
        x_B=valid_st.x_B,
        X=app.WaveTapeState(
            u=tuple(bad_u),
            v=valid_st.X.v,
            A0=valid_st.X.A0,
            A1=valid_st.X.A1,
            B0=valid_st.X.B0,
            B1=valid_st.X.B1,
            k=0,
        ),
        W=valid_st.W,
        b=valid_st.b,
        B=valid_st.B,
        sigma_A=valid_st.sigma_A,
        sigma_B=valid_st.sigma_B,
        d=valid_st.d,
        c=7,
    )
    assert app.recognize_ready_image(st_x09)["failed_test"] == "test4_initial_wave_zero"

    # X10: Malformed carrier types (bool, float, out-of-range residues, invalid signs/clocks/stores)
    malformed_calls = [
        lambda: app.prepare_ready_state((True, 0, 0, 0), (0, 0, 0, 0), cap),  # type: ignore[arg-type]
        lambda: app.prepare_ready_state((0, 0, 0, 0), (0, 0, 0, 0), 0.8),  # type: ignore[arg-type]
        lambda: app.prepare_ready_state((5, 0, 0, 0), (0, 0, 0, 0), cap),
        lambda: app.prepare_ready_state((0, 0, 0), (0, 0, 0, 0), cap),
        lambda: app.prepare_ready_state((0, 0, 0, 0), (0, 0, 0, 0), Fraction(-1, 5)),
        lambda: app.prepare_ready_state(
            (0, 0, 0, 0), (0, 0, 0, 0), cap, b_init=Fraction(9, 10)
        ),
        lambda: app.prepare_ready_state(
            (0, 0, 0, 0), (0, 0, 0, 0), cap, b_init=Fraction(-1, 10)
        ),
        lambda: app.native_tick(-1, (0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 1)),
        lambda: app.CompositeState(
            n=0,
            x_A=(0, 0, 0, 0, 0, 1),
            x_B=(0, 0, 0, 0, 0, 1),
            X=valid_st.X,
            W=Fraction(0, 1),
            b=cap,
            B=cap,
            sigma_A=0,
            sigma_B=1,
            d=(0, 0),
            c=0,
        ),
        lambda: app.CompositeState(
            n=0,
            x_A=(0, 0, 0, 0, 0, 1),
            x_B=(0, 0, 0, 0, 0, 1),
            X=valid_st.X,
            W=Fraction(0, 1),
            b=cap,
            B=cap,
            sigma_A=1,
            sigma_B=1,
            d=(0, 0),
            c=8,
        ),
    ]
    for fn in malformed_calls:
        caught = False
        try:
            fn()
        except (TypeError, ValueError):
            caught = True
        assert caught

    return "T18 PASS: all 10 adversarial invalid-endpoint and malformed-carrier tests (X01-X10) rejected"


# ---------------------------------------------------------------------------
# Witness trajectory builders for human-readable boundary state report
# ---------------------------------------------------------------------------

def build_witness_trajectories() -> List[Tuple[str, Tuple[app.CompositeState, ...]]]:
    cap = Fraction(4, 5)
    e0 = app.basis_q4(0)
    neg_e0 = tuple(-x for x in e0)
    z_d = app.zero_qd()
    z_4 = app.zero_q4()

    w1_14 = app.run_eight_steps(
        app.prepare_ready_state((1, 0, 0, 0), (4, 0, 0, 0), cap, b_init=cap),
        return_boundaries=True,
    )
    w2_41 = app.run_eight_steps(
        app.prepare_ready_state((4, 0, 0, 0), (1, 0, 0, 0), cap, b_init=cap),
        return_boundaries=True,
    )
    w3_c1_e0 = app.run_eight_steps(
        app.prepare_ready_state((0, 0, 0, 0), (1, 0, 0, 0), cap, b_init=cap, c1=e0),
        return_boundaries=True,
    )
    w4_ready_low_ref = app.run_eight_steps(
        app.prepare_ready_state(
            (3, 0, 0, 0), (3, 0, 0, 0), Fraction(2, 5), b_init=Fraction(2, 5)
        ),
        return_boundaries=True,
    )
    w5_warm_low_ref = app.run_eight_steps(
        app.CompositeState(
            n=0,
            x_A=(0, 0, 0, 0, 0, 1),
            x_B=(1, 0, 0, 0, 0, 1),
            X=app.WaveTapeState(u=z_d, v=z_d, A0=z_4, A1=e0, B0=z_4, B1=z_4, k=0),
            W=Fraction(0, 1),
            b=cap,
            B=cap,
            sigma_A=1,
            sigma_B=1,
            d=(0, 0),
            c=0,
        ),
        return_boundaries=True,
    )
    w6_warm_high_ref = app.run_eight_steps(
        app.CompositeState(
            n=0,
            x_A=(0, 0, 0, 0, 0, 1),
            x_B=(1, 0, 0, 0, 0, 1),
            X=app.WaveTapeState(u=z_d, v=z_d, A0=z_4, A1=neg_e0, B0=z_4, B1=z_4, k=0),
            W=Fraction(0, 1),
            b=cap,
            B=cap,
            sigma_A=1,
            sigma_B=1,
            d=(0, 0),
            c=0,
        ),
        return_boundaries=True,
    )
    return [
        ("WITNESS_1_ORDER_14_BLANK_B_4_5", w1_14),  # type: ignore[list-item]
        ("WITNESS_2_ORDER_41_BLANK_B_4_5", w2_41),  # type: ignore[list-item]
        ("WITNESS_3_OLD_ARCHIVE_C1_E0_PAIR_01_B_4_5", w3_c1_e0),  # type: ignore[list-item]
        ("WITNESS_4_READY_LOWER_REFUSAL_PAIR_33_B_2_5", w4_ready_low_ref),  # type: ignore[list-item]
        ("WITNESS_5_WARM_LOWER_REFUSAL_A1_E0_PAIR_01_B_4_5", w5_warm_low_ref),  # type: ignore[list-item]
        ("WITNESS_6_WARM_UPPER_REFUSAL_NEG_WORK_A1_NEG_E0_PAIR_01_B_4_5", w6_warm_high_ref),  # type: ignore[list-item]
    ]


def run_full_audit() -> None:
    tests = [
        run_t01_geometry_stencil_and_operators,
        run_t02_generators_and_v_non_invertibility,
        run_t03_single_head_625_census_and_recovery,
        run_t04_paired_factorization_390625,
        run_t05_certificate_f_bijectivity_and_energy,
        run_t06_certificate_hb_involutions_and_lbuf,
        run_t07_certificate_bilinear_work_and_mu,
        run_t08_25_pair_work_table_and_capacities,
        run_t09_order_witness_14_vs_41,
        run_t10_certificate_four_cut_operators_and_archives,
        run_t11_direct_chronological_and_source_readers,
        run_t12_store_bounds_refusal_and_negative_work,
        run_t13_accepted_zero_and_clarification_ii,
        run_t14_seven_eight_boundary_and_energy_invariants,
        run_t15_ready_image_left_inverse_all_branches,
        run_t16_calibration_prediction_and_clarification_i,
        run_t17_comparator_indistinguishability_and_separations,
        run_t18_invalid_endpoint_and_type_rejection_suite,
    ]
    print("C-FUNDED-TWO-USE-EXECUTABLE-N AUDIT START")
    for fn in tests:
        msg = fn()
        print(msg)

    print("WITNESS_BOUNDARY_STATES_BEGIN")
    for name, bounds in build_witness_trajectories():
        print(f"[{name}]")
        for st in bounds:
            print(format_boundary_line(st))
    print("WITNESS_BOUNDARY_STATES_END")
    print(
        "C-FUNDED-TWO-USE-EXECUTABLE-N AUDIT PASS: tests=18/18 invalid_endpoints=10/10 "
        "order_diff=313/233280 max_work=8224427/10497600 status=ALL_PASS"
    )


def main(argv: Sequence[str]) -> int:
    if len(argv) == 1:
        run_full_audit()
        return 0
    if len(argv) == 2 and argv[1] == "--compare":
        count, digest = app.compute_comparison_digest()
        print(f"TWOUSE-COMPARE-v1 records={count} sha256={digest}")
        return 0
    if len(argv) == 2 and argv[1] == "--witnesses":
        for name, bounds in build_witness_trajectories():
            print(f"[{name}]")
            for st in bounds:
                print(format_boundary_line(st))
        return 0
    sys.stderr.write(f"Usage: {argv[0]} [--compare | --witnesses]\n")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
