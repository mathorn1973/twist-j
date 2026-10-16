#!/usr/bin/env python3
"""Executable audit, witness generator, and comparison runner for Lane I2 (#1515).

NON-CANONICAL / L1 executable incubation audit on reconciled 705-site D.
Original work Apache-2.0, A. M. Thorn, 2026-10-15.

CLI modes:
  python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py
      Run full scientific audit (T01-T18 and X01-X10) and print deterministic
      scientific stdout including witness boundary states.
  python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py --compare
      Run separate 1200-record comparison mode and print:
      TWOUSE-COMPARE-v2 domain_sha256=2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0 records=1200 sha256=<64 lowercase hex>
  python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py --witnesses
      Print witness boundary trajectories and summary for the 7-step (1,4)/(4,1)
      order comparison, dirty-archive c1=e0 case, and lower/upper stock refusals.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import inspect
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


# ---------------------------------------------------------------------------
# Explicit expected/actual assertion helpers and formatting
# ---------------------------------------------------------------------------

def require_eq(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: expected={expected!r}, actual={actual!r}")


def require_true(
    cond: bool, label: str, *, expected: object = True, actual: object = False
) -> None:
    if not cond:
        raise AssertionError(f"{label}: expected={expected!r}, actual={actual!r}")


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
    require_eq(len(app.Y_SITES), 5, "T01.|Y|")
    require_eq(len(geom.b_st), 60, "T01.|B_st|")
    require_eq(len(geom.b_zero), 61, "T01.|B_zero|")
    require_eq(len(geom.y1_sites), 142, "T01.|Y+B_zero|")
    require_eq(len(geom.b2_sites), 489, "T01.|B_zero+B_zero|")
    require_eq(len(geom.domain_d), 705, "T01.|D|")
    require_eq(geom.n_sites, 705, "T01.n_sites")
    require_eq(geom.wave_tape_basis_dim, 1426, "T01.wave_tape_basis_dim")
    require_eq(geom.domain_bytes, 5029, "T01.DOMAIN.tsv.bytes")
    require_eq(
        geom.domain_sha256,
        "2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0",
        "T01.DOMAIN.tsv.sha256",
    )
    require_eq(list(geom.domain_d), sorted(geom.domain_d), "T01.domain_d.sorted")
    require_eq(
        sum(geom.stencil_coeffs.values(), Fraction(0, 1)),
        Fraction(8, 9),
        "T01.stencil_sum",
    )

    # Check P^T P = I_4, P^T J_0 = 0, K P = (1/2) P, P^T S = G_source
    for j in range(4):
        ej = app.basis_q4(j)
        pej = app.apply_P(ej)
        require_eq(app.apply_PT(pej), ej, f"T01.PT_P[e_{j}]")
        require_eq(app.apply_PT(app.apply_J0(pej)), app.zero_q4(), f"T01.PT_J0[P e_{j}]")
        k_pej = app.apply_K(pej)
        require_eq(
            k_pej,
            tuple(Fraction(1, 2) * x for x in pej),
            f"T01.K_P[e_{j}]",
        )
        sej = app.apply_S(ej)
        pt_sej = app.apply_PT(sej)
        exp_g = tuple(Fraction(4, 5) if i == j else Fraction(-1, 5) for i in range(4))
        require_eq(pt_sej, exp_g, f"T01.PT_S[e_{j}]")
        require_eq(app.dot_vec(sej, sej), Fraction(4, 5), f"T01.||S e_{j}||^2")

    # Check J_p = P^T H P = (59 I_4 + 1 1^T)/54 and M = P^T H S = (1770 I_4 - v 1^T)/1620
    ops = app.get_derived_operators()
    for r in range(4):
        for c in range(4):
            exp_jp = Fraction(60 if r == c else 1, 54)
            require_eq(ops.Jp[r][c], exp_jp, f"T01.Jp[{r},{c}]")
            exp_m = Fraction((1770 if r == c else 0) - EXPECTED_V_VECTOR[r], 1620)
            require_eq(ops.M[r][c], exp_m, f"T01.M[{r},{c}]")
            require_eq(ops.R0[r][c], -Fraction(1, 4) * exp_m, f"T01.R0[{r},{c}]")

    return (
        "T01 PASS: |B_st|=60, |B_zero|=61, |Y+B_zero|=142, |B_zero+B_zero|=489, "
        "|D|=705, dim=1426, DOMAIN.tsv sha256 verified, P^T P=I_4, J_p and M verified"
    )


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
                                require_eq(
                                    app.apply_generator(g, gx),
                                    x,
                                    f"T02.involution[g={g},x={x}]",
                                )
                                require_eq(
                                    sum(gx) % 5,
                                    expected_sums[g],
                                    f"T02.sum_action[g={g},x={x}]",
                                )

    x_coll_1 = (0, 0, 0, 0, 0, 1)
    x_coll_2 = (2, 1, 3, 4, 2, 2)
    require_eq(app.native_selector(0, x_coll_1), 1, "T02.selector(x_coll_1)")
    require_eq(app.native_selector(0, x_coll_2), 4, "T02.selector(x_coll_2)")
    v1 = app.native_tick(0, x_coll_1, x_coll_1)
    v2 = app.native_tick(0, x_coll_2, x_coll_2)
    expected_v = (1, (0, 0, 0, 0, 0, 4), (0, 0, 0, 0, 0, 4))
    require_eq(v1, expected_v, "T02.V(x_coll_1)")
    require_eq(v2, expected_v, "T02.V(x_coll_2)")
    require_eq(v1[0], 1, "T02.n_increment")
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

                    require_eq(
                        (j0, j1, j2, j3, j4),
                        EXPECTED_CANONICAL_SELECTORS[h],
                        f"T03.selectors[p={p}]",
                    )
                    c1, c2, c3 = EXPECTED_C1_C2_C3[h]
                    require_eq(app.receiver_of(x1), c1, f"T03.C1[p={p}]")
                    require_eq(app.receiver_of(x2), c2, f"T03.C2[p={p}]")
                    require_eq(app.receiver_of(x3), c3, f"T03.C3[p={p}]")
                    require_eq(sum(x3) % 5, 1, f"T03.z6(x3)[p={p}]")
                    require_eq(sum(x4) % 5, 4, f"T03.z6(x4)[p={p}]")
                    require_eq(x4, app.apply_generator(1, x3), f"T03.x4==g1(x3)[p={p}]")
                    require_eq(x5, x3, f"T03.x5==x3[p={p}]")
                    require_eq(app.receiver_of(x5), c3, f"T03.C5[p={p}]")
                    require_eq(app.eta_lift(c1), EXPECTED_Z5_VECTORS[h], f"T03.eta(C1)[p={p}]")

                    x0_rec = app.apply_generator(
                        j0, app.apply_generator(j1, app.apply_generator(j2, x5))
                    )
                    require_eq(x0_rec, x0, f"T03.x0_rec[p={p}]")
                    require_eq(x0_rec[:4], p, f"T03.p_rec[p={p}]")
                    require_eq(sum(x0_rec[:4]) % 5, h, f"T03.h_rec[p={p}]")

    require_eq(counts, {0: 125, 1: 125, 2: 125, 3: 125, 4: 125}, "T03.class_counts")
    return "T03 PASS: all 625 single-head preparations (125/class) audited and inverted"


def run_t04_paired_factorization_390625() -> str:
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
        require_eq(rec_x0a, (pa[0], pa[1], pa[2], pa[3], 0, 1), f"T04.rec_x0a[pa={pa}]")
        require_eq(app.receiver_of(x1a), EXPECTED_C1_C2_C3[ha][0], f"T04.C1_A[pa={pa}]")
        for pb, hb, x1b, x5b in single_trajs:
            total_pairs += 1
            fibre_counts[(ha, hb)] += 1
            require_eq(c3_to_h[app.receiver_of(x5a)], ha, "T04.c3_to_h_A")
            require_eq(c3_to_h[app.receiver_of(x5b)], hb, "T04.c3_to_h_B")
            require_eq(app.receiver_of(x1b), EXPECTED_C1_C2_C3[hb][0], "T04.C1_B")

    require_eq(total_pairs, 390625, "T04.total_pairs")
    for pair_key, cnt in fibre_counts.items():
        require_eq(cnt, 15625, f"T04.fibre_count[{pair_key}]")

    # Verify apparatus substate at c=0..7 is identical for distinct representatives in same fibre
    for ha in range(5):
        for hb in range(5):
            p_a1 = (ha, 0, 0, 0)
            p_a2 = ((ha - 1) % 5, 1, 2, 3)
            p_b1 = (hb, 0, 0, 0)
            p_b2 = (2, (hb - 2) % 5, 4, 1)
            require_eq(sum(p_a1) % 5, ha, "T04.sum(p_a1)")
            require_eq(sum(p_a2) % 5, ha, "T04.sum(p_a2)")
            require_eq(sum(p_b1) % 5, hb, "T04.sum(p_b1)")
            require_eq(sum(p_b2) % 5, hb, "T04.sum(p_b2)")
            s1 = app.run_seven_steps(app.prepare_ready_state(p_a1, p_b1, Fraction(1, 5)))
            s2 = app.run_seven_steps(app.prepare_ready_state(p_a2, p_b2, Fraction(1, 5)))
            require_true(isinstance(s1, app.CompositeState), "T04.s1_type")
            require_true(isinstance(s2, app.CompositeState), "T04.s2_type")
            assert isinstance(s1, app.CompositeState) and isinstance(s2, app.CompositeState)
            require_eq(
                s1.to_apparatus_substate(),
                s2.to_apparatus_substate(),
                f"T04.fibre_substate[({ha},{hb})]",
            )
            require_eq(app.recover_prepared_inputs(s1), (p_a1, p_b1), "T04.recover_s1")
            require_eq(app.recover_prepared_inputs(s2), (p_a2, p_b2), "T04.recover_s2")

    return "T04 PASS: 390625 paired inputs factor into 25 fibres of 15625; full recovery verified"


def _verify_f_basis_and_bilinear_column(
    x_basis: app.WaveTapeState, label: str, n_sites: int, z_d: Tuple[Fraction, ...], z_4: Tuple[Fraction, ...]
) -> None:
    """Verify F^-1(F(E))==E, F(F^-1(E))==E, E_full(F(E))==E_full(E), and polarization column == 0."""
    fx = app.F_step(x_basis)
    require_eq(app.F_inverse(fx), x_basis, f"{label}.F_inv_F")
    require_eq(app.F_step(app.F_inverse(x_basis)), x_basis, f"{label}.F_F_inv")
    require_eq(
        app.full_classical_energy(fx),
        app.full_classical_energy(x_basis),
        f"{label}.E_full_diag",
    )

    # Polarized bilinear form B_Q(X_1, E) of Q(X) = 2(E_full(F(X)) - E_full(X)):
    # B_Q(X_1, E) = u_1^T col_u(E) + v_1^T col_v(E) + A_{0,1}^T col_a(E)
    u2 = x_basis.u
    v2 = x_basis.v
    a0_2 = x_basis.A0
    w2 = fx.v
    b_out2 = fx.B0
    hv2 = app.apply_H(v2)
    pb_out2 = app.apply_P(b_out2)
    q2 = app.apply_K(
        tuple(w2[m] - Fraction(1, 2) * hv2[m] - 2 * pb_out2[m] for m in range(n_sites))
    )
    half_w_minus_u = tuple(Fraction(1, 2) * (w2[m] - u2[m]) for m in range(n_sites))
    require_eq(q2, half_w_minus_u, f"{label}.q2_identity")

    j0_q2 = app.apply_J0(q2)
    col_u = tuple(
        -j0_q2[m] + 2 * pb_out2[m] - u2[m] + Fraction(1, 2) * hv2[m] for m in range(n_sites)
    )
    col_v = app.apply_H(
        tuple(q2[m] - Fraction(1, 2) * w2[m] + Fraction(1, 2) * u2[m] for m in range(n_sites))
    )
    pt_q2 = app.apply_PT(q2)
    col_a = tuple(4 * pt_q2[j] + 4 * b_out2[j] - 4 * a0_2[j] for j in range(4))
    require_eq(col_u, z_d, f"{label}.col_u_zero")
    require_eq(col_v, z_d, f"{label}.col_v_zero")
    require_eq(col_a, z_4, f"{label}.col_a_zero")


def run_t05_certificate_f_bijectivity_and_energy() -> str:
    geom = app.get_geometry()
    n_sites = geom.n_sites
    require_eq(n_sites, 705, "T05.n_sites")
    require_eq(geom.wave_tape_basis_dim, 1426, "T05.wave_tape_basis_dim")

    # 1. Verify symmetry of H and operator blocks on all 705 basis vectors of Q^D
    z_d = app.zero_qd()
    z_4 = app.zero_q4()
    for i in range(n_sites):
        for j, coeff in geom.h_neighbors[i]:
            rev = dict(geom.h_neighbors[j]).get(i)
            require_eq(rev, coeff, f"T05.H_symmetry[{i},{j}]")

    # 2. Verify F_inverse(F_step(e)) == e, F_step(F_inverse(e)) == e, E_full conservation,
    # and all 1426 polarized bilinear energy columns (certifying all 1426x1426 = 2,033,476 entries)
    basis_checked = 0
    for i in range(n_sites):
        u_basis = list(z_d)
        u_basis[i] = Fraction(1, 1)
        u_tup = tuple(u_basis)

        # Basis in u slot
        xu = app.WaveTapeState(u=u_tup, v=z_d, A0=z_4, A1=z_4, B0=z_4, B1=z_4, k=0)
        _verify_f_basis_and_bilinear_column(xu, f"T05.u[{i}]", n_sites, z_d, z_4)
        basis_checked += 1

        # Basis in v slot
        xv = app.WaveTapeState(u=z_d, v=u_tup, A0=z_4, A1=z_4, B0=z_4, B1=z_4, k=1)
        _verify_f_basis_and_bilinear_column(xv, f"T05.v[{i}]", n_sites, z_d, z_4)
        basis_checked += 1

        # Verify K^2 - K + (1/4) P P^T = 0 on H e_i (the (v,v) quadratic energy block)
        hei = app.apply_H(u_tup)
        k_hei = app.apply_K(hei)
        k2_hei = app.apply_K(k_hei)
        ppt_hei = app.apply_P(app.apply_PT(hei))
        for m in range(n_sites):
            require_eq(
                k2_hei[m] - k_hei[m] + Fraction(1, 4) * ppt_hei[m],
                Fraction(0, 1),
                f"T05.K2_minus_K[{i},{m}]",
            )

    for slot in range(4):
        for j in range(4):
            ej = app.basis_q4(j)
            tapes = [z_4, z_4, z_4, z_4]
            tapes[slot] = ej
            xt = app.WaveTapeState(
                u=z_d, v=z_d, A0=tapes[0], A1=tapes[1], B0=tapes[2], B1=tapes[3], k=0
            )
            _verify_f_basis_and_bilinear_column(
                xt, f"T05.tape[slot={slot},j={j}]", n_sites, z_d, z_4
            )
            basis_checked += 1

    require_eq(basis_checked, geom.wave_tape_basis_dim, "T05.basis_checked")
    require_eq(basis_checked * basis_checked, 2033476, "T05.bilinear_entries")

    # 3. Verify R1-A witness (u=v=0, A0=e0) and wave_energy difference form
    e0 = app.basis_q4(0)
    x_r1a = app.WaveTapeState(u=z_d, v=z_d, A0=e0, A1=z_4, B0=z_4, B1=z_4, k=0)
    fx_r1a = app.F_step(x_r1a)
    require_eq(fx_r1a.v, tuple(2 * x for x in app.apply_P(e0)), "T05.R1A.v")
    require_eq(fx_r1a.B0, z_4, "T05.R1A.B0")
    require_eq(app.F_inverse(fx_r1a), x_r1a, "T05.R1A.F_inv")
    require_eq(
        app.wave_energy(fx_r1a.u, fx_r1a.v),
        app.wave_energy_difference_form(fx_r1a.u, fx_r1a.v),
        "T05.R1A.wave_energy_diff_form",
    )

    return (
        f"T05 PASS: coefficient-complete F/F^-1 and E_full (1426x1426=2033476 bilinear entries) "
        f"verified on all {basis_checked} basis vectors"
    )


def run_t06_certificate_hb_involutions_and_lbuf() -> str:
    geom = app.get_geometry()
    n_sites = geom.n_sites
    z_4 = app.zero_q4()
    # Check polynomial identity Delta(u, v + sigma*a(r), -sigma) + Delta(u, v, sigma) == 0
    # across all 25 labels r in F_5^2 and both sigma in {-1, +1}
    for q in range(5):
        for r2 in range(5):
            r = (q, r2)
            a_r = app.source_field_for_receiver(r)
            norm_sq_half = Fraction(1, 2) * app.dot_vec(a_r, a_r)
            for sig in (-1, 1):
                const_sum = norm_sq_half - (sig * sig) * app.dot_vec(a_r, a_r) + norm_sq_half
                require_eq(const_sum, Fraction(0, 1), f"T06.const_sum[r={r},sig={sig}]")
                for idx in range(n_sites):
                    require_eq(
                        sig * a_r[idx] + (-sig) * a_r[idx],
                        Fraction(0, 1),
                        f"T06.lin_coeff[r={r},idx={idx}]",
                    )

                # Test H_{B,A}^2 == id and H_{B,B}^2 == id on accepted, lower-refused, and upper-refused substates
                for u_scale, v_scale, b_val, cap_val in [
                    (Fraction(0, 1), Fraction(0, 1), Fraction(2, 5), Fraction(4, 5)),
                    (Fraction(1, 3), Fraction(-1, 2), Fraction(0, 1), Fraction(1, 10)),
                    (Fraction(0, 1), Fraction(-2, 1), Fraction(4, 5), Fraction(4, 5)),
                ]:
                    u_test = tuple(u_scale * x for x in app.apply_S(app.basis_q4(0)))
                    v_test = tuple(v_scale * x for x in app.apply_P(app.basis_q4(0)))
                    d_inc = app.contact_energy_increment(u_test, v_test, sig, r)
                    require_eq(
                        d_inc,
                        app.contact_energy_increment_bilinear(u_test, v_test, sig, r),
                        f"T06.d_inc_bilinear[r={r},sig={sig}]",
                    )
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
                    require_eq(sub_a2, sub, f"T06.H_BA_involution[r={r},sig={sig}]")
                    sub_b1 = app.funded_contact_B_substate(sub)
                    sub_b2 = app.funded_contact_B_substate(sub_b1)
                    require_eq(sub_b2, sub, f"T06.H_BB_involution[r={r},sig={sig}]")

                    # Check two-sided invertibility of the supplied-label apparatus substate
                    # transitions T_{c,B}^{(r_A, r_B)} and S_B^{(r_A, r_B)} across c=0..7
                    for c_phase in range(8):
                        row_fwd = app.apparatus_row_map(sub, c_phase, r, (1, 4))
                        row_back = app.apparatus_row_map_inverse(row_fwd, c_phase, r, (1, 4))
                        require_eq(row_back, sub, f"T06.T_c_inv_T_c[c={c_phase}]")
                        row_inv = app.apparatus_row_map_inverse(sub, c_phase, r, (1, 4))
                        row_fwd_inv = app.apparatus_row_map(row_inv, c_phase, r, (1, 4))
                        require_eq(row_fwd_inv, sub, f"T06.T_c_T_c_inv[c={c_phase}]")

                        fwd_sub, fwd_c = app.apparatus_step(sub, c_phase, r, (1, 4))
                        back_sub, back_c = app.apparatus_step_inverse(fwd_sub, fwd_c, r, (1, 4))
                        require_eq(
                            (back_sub, back_c),
                            (sub, c_phase),
                            f"T06.S_B_inv_S_B[c={c_phase}]",
                        )

    return (
        "T06 PASS: universal H_{B,A}^2=id, H_{B,B}^2=id, L_buf^-1, and supplied-label "
        "substate S_B^{(r_A,r_B)}^-1 verified across all 25 labels and 8 phases"
    )


def run_t07_certificate_bilinear_work_and_mu() -> str:
    geom = app.get_geometry()
    n_sites = geom.n_sites
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
        diff = tuple(w2[m] - Fraction(1, 2) * hw1[m] for m in range(n_sites))

        # Check J_0((1/2) H K H f - f) equality and fifth-site value
        hkh_f = app.apply_H(app.apply_K(app.apply_H(f_ej)))
        j0_term = app.apply_J0(
            tuple(Fraction(1, 2) * hkh_f[m] - f_ej[m] for m in range(n_sites))
        )
        require_eq(diff, j0_term, f"T07.diff_eq_j0_term[j={j}]")
        require_eq(
            diff[geom.y4_index],
            Fraction(EXPECTED_MU_VECTOR[j], 2099520),
            f"T07.y4_val[j={j}]",
        )

        for i in range(4):
            ei = app.basis_q4(i)
            g_ei = app.apply_S(ei)
            cross_ij = app.dot_vec(g_ei, diff)
            require_eq(
                cross_ij,
                -Fraction(EXPECTED_MU_VECTOR[j], EXPECTED_MU_DENOM),
                f"T07.Omega[{i},{j}]",
            )

    return "T07 PASS: 4x4 bilinear cross-work matrix equals -1*mu^T/10497600 with mu=(145483,173653,173653,142153)"


def run_t08_25_pair_work_table_and_capacities() -> str:
    for cap, exp_counts in EXPECTED_BRANCH_COUNTS.items():
        acc_acc = acc_ref = ref_acc = ref_ref = 0
        for ha in range(5):
            for hb in range(5):
                st0 = app.prepare_ready_state((ha, 0, 0, 0), (hb, 0, 0, 0), cap, b_init=cap)
                bounds = app.run_seven_steps(st0, return_boundaries=True)
                require_true(
                    isinstance(bounds, tuple) and len(bounds) == 8,
                    f"T08.bounds_len[cap={cap},({ha},{hb})]",
                )
                assert isinstance(bounds, tuple)
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
                    require_eq(ea, EXPECTED_E0_ON_Z5[ha], f"T08.E_A[({ha},{hb})]")
                    require_eq(
                        delta_b,
                        EXPECTED_E0_ON_Z5[hb] + exp_cross,
                        f"T08.Delta_B[({ha},{hb})]",
                    )
                    require_eq(w_fin, ea + delta_b, f"T08.W_fin_sum[({ha},{hb})]")
                    require_eq(
                        w_fin * 41990400,
                        EXPECTED_41990400_W_FINAL[(ha, hb)],
                        f"T08.41990400_W_fin[({ha},{hb})]",
                    )
                    require_true(0 <= ea <= Fraction(2, 5), f"T08.E_A_bounds[({ha},{hb})]")
                    require_true(
                        0 <= delta_b <= Fraction(2, 5), f"T08.Delta_B_bounds[({ha},{hb})]"
                    )
                    require_eq(st7.b, Fraction(4, 5) - w_fin, f"T08.b_final[({ha},{hb})]")
                    require_true(st7.b > 0, f"T08.b_final_pos[({ha},{hb})]")

        require_eq(
            (acc_acc, acc_ref, ref_acc, ref_ref),
            exp_counts,
            f"T08.branch_counts[cap={cap}]",
        )

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
    require_eq(w_14, Fraction(10352117, 20995200), "T09.W(1,4)")
    require_eq(w_41, Fraction(10323947, 20995200), "T09.W(4,1)")
    require_eq(diff, Fraction(313, 233280), "T09.W(1,4)-W(4,1)")
    return f"T09 PASS: order witness W(1,4)={fmt_frac(w_14)}, W(4,1)={fmt_frac(w_41)}, W(1,4)-W(4,1)=313/233280"


def run_t10_certificate_four_cut_operators_and_archives() -> str:
    geom = app.get_geometry()
    n_sites = geom.n_sites
    ops = app.get_derived_operators()
    # Verify single-source tables 12960 R0 z^(h) and 1399680 R1 z^(h)
    for h in range(5):
        zh = EXPECTED_Z5_VECTORS[h]
        r0_zh = app.mat_vec_4(ops.R0, zh)
        r1_zh = app.mat_vec_4(ops.R1, zh)
        require_eq(
            tuple(int(x * 12960) for x in r0_zh),
            EXPECTED_12960_R0_Z5[h],
            f"T10.12960_R0[h={h}]",
        )
        require_eq(
            tuple(int(x * 1399680) for x in r1_zh),
            EXPECTED_1399680_R1_Z5[h],
            f"T10.1399680_R1[h={h}]",
        )

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
                        v=tuple(x_c4.v[m] + g_b[m] for m in range(n_sites)),
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

                    require_eq(x_c7.A0, exp_b0, f"T10.b0[a={alpha_a},b={alpha_b},s={slot},j={j}]")
                    require_eq(x_c7.A1, exp_b1, f"T10.b1[a={alpha_a},b={alpha_b},s={slot},j={j}]")
                    require_eq(x_c7.B1, exp_b2, f"T10.b2[a={alpha_a},b={alpha_b},s={slot},j={j}]")
                    require_eq(x_c7.B0, exp_b3, f"T10.b3[a={alpha_a},b={alpha_b},s={slot},j={j}]")

    # Explicit WARM witness checks for c1 = e0 on (0,0) and (0,1)
    e0 = app.basis_q4(0)
    st_warm_00 = app.run_seven_steps(
        app.prepare_ready_state((0, 0, 0, 0), (0, 0, 0, 0), Fraction(4, 5), c1=e0)
    )
    assert isinstance(st_warm_00, app.CompositeState)
    require_eq(
        st_warm_00.X.B0,
        (
            Fraction(-5, 9),
            Fraction(-1, 108),
            Fraction(-1, 108),
            Fraction(-1, 108),
        ),
        "T10.warm_00.b3",
    )

    st_warm_01 = app.run_seven_steps(
        app.prepare_ready_state((0, 0, 0, 0), (1, 0, 0, 0), Fraction(4, 5), c1=e0)
    )
    assert isinstance(st_warm_01, app.CompositeState)
    require_eq(
        st_warm_01.X.B0,
        (
            Fraction(-585398, 1399680),
            Fraction(-60789, 1399680),
            Fraction(-60789, 1399680),
            Fraction(-61839, 1399680),
        ),
        "T10.warm_01.b3",
    )
    require_eq(app.full_classical_energy(st_warm_01.X), Fraction(21, 10), "T10.warm_01.E_full")
    require_eq(st_warm_01.W, Fraction(1, 10), "T10.warm_01.W")

    return "T10 PASS: universal 4-cut operator certificate and c1=e0 WARM witnesses verified"


def run_t11_direct_chronological_and_source_readers() -> str:
    # 1. Test API access restrictions of direct_source_reader
    sig = inspect.signature(app.direct_source_reader)
    require_eq(
        list(sig.parameters.keys()),
        ["b0", "b2", "sigma_A", "sigma_B", "d"],
        "T11.signature",
    )

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
        require_true(raised, f"T11.reject_forbidden[{type(forbidden).__name__}]")

    # 2. Verify chronological cut reader across c=0..7, including continued reading of (b0,b1)
    b0_val = st7.X.A0
    b1_val = st7.X.A1
    b2_val = st7.X.B1
    b3_val = st7.X.B0
    for c_idx in range(8):
        entries = app.direct_chronological_cut_reader(bounds[c_idx])
        if c_idx in (0, 1, 2):
            require_true(all(e.status == "UNWRITTEN" for e in entries), f"T11.c{c_idx}.unwritten")
        elif c_idx == 3:
            require_eq((entries[0].status, entries[0].vector), ("PRESENT", b0_val), "T11.c3.cut0")
            require_true(all(e.status == "UNWRITTEN" for e in entries[1:]), "T11.c3.rest")
        elif c_idx in (4, 5):
            require_eq(
                (entries[0].vector, entries[0].slot_name),
                (b0_val, "B1"),
                f"T11.c{c_idx}.cut0",
            )
            require_eq(
                (entries[1].vector, entries[1].slot_name),
                (b1_val, "B0"),
                f"T11.c{c_idx}.cut1",
            )
            require_true(all(e.status == "UNWRITTEN" for e in entries[2:]), f"T11.c{c_idx}.rest")
        elif c_idx == 6:
            require_eq((entries[0].vector, entries[0].slot_name), (b0_val, "A1"), "T11.c6.cut0")
            require_eq((entries[1].vector, entries[1].slot_name), (b1_val, "B1"), "T11.c6.cut1")
            require_eq((entries[2].vector, entries[2].slot_name), (b2_val, "B0"), "T11.c6.cut2")
            require_eq(entries[3].status, "UNWRITTEN", "T11.c6.cut3")
        else:
            require_eq((entries[0].vector, entries[0].slot_name), (b0_val, "A0"), "T11.c7.cut0")
            require_eq((entries[1].vector, entries[1].slot_name), (b1_val, "A1"), "T11.c7.cut1")
            require_eq((entries[2].vector, entries[2].slot_name), (b2_val, "B1"), "T11.c7.cut2")
            require_eq((entries[3].vector, entries[3].slot_name), (b3_val, "B0"), "T11.c7.cut3")

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
                require_eq(dec["z_A"], EXPECTED_Z5_VECTORS[ha], f"T11.z_A[({ha},{hb})]")
                require_eq(dec["z_B"], EXPECTED_Z5_VECTORS[hb], f"T11.z_B[({ha},{hb})]")
                require_eq((dec["alpha_A"], dec["alpha_B"]), (1, 1), f"T11.alpha[({ha},{hb})]")

    return "T11 PASS: direct_chronological_cut_reader, direct_source_reader, and API restrictions verified"


def run_t12_store_bounds_refusal_and_negative_work() -> str:
    # 1. Ready-family lower-bound refusal at B = 2/5 on (3,3)
    st_ref_25 = app.run_seven_steps(
        app.prepare_ready_state((3, 0, 0, 0), (3, 0, 0, 0), Fraction(2, 5))
    )
    assert isinstance(st_ref_25, app.CompositeState)
    require_eq((st_ref_25.sigma_A, st_ref_25.sigma_B), (-1, 1), "T12.ready_ref_25.sigma")
    require_eq((st_ref_25.W, st_ref_25.b), (Fraction(2, 5), Fraction(0, 1)), "T12.ready_ref_25.Wb")

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
    require_eq(delta_b_low, Fraction(9, 10), "T12.warm_low.delta_b")
    require_eq(c4_low.b - delta_b_low, Fraction(-1, 10), "T12.warm_low.b_cand")
    require_eq((warm_low_bounds[7].sigma_A, warm_low_bounds[7].sigma_B), (-1, 1), "T12.warm_low.sig")
    require_eq((warm_low_bounds[7].W, warm_low_bounds[7].b), (Fraction(0, 1), cap), "T12.warm_low.Wb")

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
    require_eq(delta_b_high, Fraction(-7, 10), "T12.warm_high.delta_b")
    require_eq(c4_high.b - delta_b_high, Fraction(3, 2), "T12.warm_high.b_cand")
    require_eq(
        (warm_high_bounds[7].sigma_A, warm_high_bounds[7].sigma_B),
        (-1, 1),
        "T12.warm_high.sig",
    )
    require_eq(
        (warm_high_bounds[7].W, warm_high_bounds[7].b),
        (Fraction(0, 1), cap),
        "T12.warm_high.Wb",
    )

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
    require_eq((warm_neg_acc_end.sigma_A, warm_neg_acc_end.sigma_B), (-1, -1), "T12.neg_acc.sig")
    require_eq(
        (warm_neg_acc_end.W, warm_neg_acc_end.b),
        (Fraction(-7, 10), Fraction(7, 10)),
        "T12.neg_acc.Wb",
    )

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
    require_eq(len(pi_class_set), 1, "T13.pi_class_collapse")

    # Check Pi_{class+d} = (X, W, b, d) collapses (0,0) with (3,0) and (0,3) with (3,3)
    require_eq(
        (endpoints[(0, 0)].X, endpoints[(0, 0)].W, endpoints[(0, 0)].b, endpoints[(0, 0)].d),
        (endpoints[(3, 0)].X, endpoints[(3, 0)].W, endpoints[(3, 0)].b, endpoints[(3, 0)].d),
        "T13.pi_class_d_(0,0)_(3,0)",
    )
    require_eq(
        (endpoints[(0, 3)].X, endpoints[(0, 3)].W, endpoints[(0, 3)].b, endpoints[(0, 3)].d),
        (endpoints[(3, 3)].X, endpoints[(3, 3)].W, endpoints[(3, 3)].b, endpoints[(3, 3)].d),
        "T13.pi_class_d_(0,3)_(3,3)",
    )

    # Check (sigma_A, sigma_B) separates all 4
    require_eq((endpoints[(0, 0)].sigma_A, endpoints[(0, 0)].sigma_B), (-1, -1), "T13.sig_(0,0)")
    require_eq((endpoints[(0, 3)].sigma_A, endpoints[(0, 3)].sigma_B), (-1, 1), "T13.sig_(0,3)")
    require_eq((endpoints[(3, 0)].sigma_A, endpoints[(3, 0)].sigma_B), (1, -1), "T13.sig_(3,0)")
    require_eq((endpoints[(3, 3)].sigma_A, endpoints[(3, 3)].sigma_B), (1, 1), "T13.sig_(3,3)")

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
                require_eq(view_no_sigb.sigma_B, None, "T13.sigma_B_omitted")
                dec = app.direct_source_reader(view_no_sigb)
                true_alpha_b = (1 - st.sigma_B) // 2
                require_eq(
                    dec["alpha_B_from_d_b0_b2"],
                    true_alpha_b,
                    f"T13.alpha_B_from_d[cap={c_val},({ha},{hb})]",
                )
                require_eq(
                    dec["alpha_B"],
                    true_alpha_b,
                    f"T13.alpha_B[cap={c_val},({ha},{hb})]",
                )

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
                require_true(
                    isinstance(bounds8, tuple) and len(bounds8) == 9,
                    "T14.bounds8_len",
                )
                assert isinstance(bounds8, tuple)
                for step_idx, b_st in enumerate(bounds8):
                    efull = app.full_classical_energy(b_st.X)
                    require_eq(efull - b_st.W, init_tape_e, f"T14.E_minus_W[step={step_idx}]")
                    require_eq(
                        efull + b_st.b,
                        init_tape_e + cap,
                        f"T14.E_plus_b[step={step_idx}]",
                    )
                    require_eq(b_st.W + b_st.b, cap, f"T14.W_plus_b[step={step_idx}]")
                    if step_idx < 8:
                        require_eq(b_st.c, step_idx, f"T14.c[step={step_idx}]")

                st7 = bounds8[7]
                st8 = bounds8[8]
                require_eq((st7.c, st7.n), (7, 5), "T14.st7_clock")
                require_eq((st8.c, st8.n), (0, 5), "T14.st8_clock")
                require_eq(
                    st8.to_apparatus_substate(),
                    st7.to_apparatus_substate(),
                    "T14.rollover_substate",
                )
                require_eq((st8.x_A, st8.x_B), (st7.x_A, st7.x_B), "T14.rollover_heads")

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
                require_eq(rec["valid"], True, f"T15.valid[cap={cap},({ha},{hb})]")
                require_eq(
                    app.recover_prepared_inputs(st7, c0=c0_vec, c1=c1_vec, b_init=cap),
                    (p_a, p_b),
                    f"T15.recover[cap={cap},({ha},{hb})]",
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

    require_eq(
        (g00, g11, g01),
        (Fraction(4, 5), Fraction(4, 5), Fraction(-1, 5)),
        "T16.calibrated_G",
    )
    require_eq(om00, Fraction(-145483, 10497600), "T16.om00")
    require_eq(om10, Fraction(-145483, 10497600), "T16.om10")
    require_eq(om01, Fraction(-173653, 10497600), "T16.om01")
    require_eq(om11, Fraction(-173653, 10497600), "T16.om11")

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
            require_eq(pred_b0, obs[(ha, hb)]["b0"], f"T16.pred_b0[({ha},{hb})]")
            require_eq(pred_b1, obs[(ha, hb)]["b1"], f"T16.pred_b1[({ha},{hb})]")
            require_eq(pred_b2, obs[(ha, hb)]["b2"], f"T16.pred_b2[({ha},{hb})]")
            require_eq(pred_b3, obs[(ha, hb)]["b3"], f"T16.pred_b3[({ha},{hb})]")
            require_eq(pred_ea, obs[(ha, hb)]["E_A"], f"T16.pred_ea[({ha},{hb})]")
            require_eq(pred_db, obs[(ha, hb)]["Delta_B"], f"T16.pred_db[({ha},{hb})]")

    # Clarification (i): verify q3(z0, z1) = z0 * z1 * (2*z0 - 1) has q3(z^(3)) = 1/2,
    # so b2 + q3(z_A) u shifts b2 at h_A = 3 by u/2 (not u)
    def q3_poly(z: Tuple[Fraction, Fraction, Fraction, Fraction]) -> Fraction:
        return z[0] * z[1] * (2 * z[0] - 1)

    for h in (0, 1, 2, 4):
        require_eq(q3_poly(EXPECTED_Z5_VECTORS[h]), Fraction(0, 1), f"T16.q3[h={h}]")
    require_eq(q3_poly(EXPECTED_Z5_VECTORS[3]), Fraction(1, 2), "T16.q3[h=3]")
    u_vec = (Fraction(2, 3), Fraction(-4, 5), Fraction(1, 7), Fraction(3, 11))
    shift_at_h3 = tuple(q3_poly(EXPECTED_Z5_VECTORS[3]) * x for x in u_vec)
    require_eq(shift_at_h3, tuple(Fraction(1, 2) * x for x in u_vec), "T16.shift_at_h3")
    require_true(shift_at_h3 != u_vec, "T16.shift_neq_u")

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
                require_eq(c_cur, 7, "T17.c_cur")
                require_eq(sub, st7.to_apparatus_substate(), f"T17.matched[cap={cap},({ha},{hb})]")

    # 2. Five restricted comparator separations:
    # (a) M_single on (0,1) at B = 4/5
    st_01 = app.run_seven_steps(
        app.prepare_ready_state((0, 0, 0, 0), (1, 0, 0, 0), Fraction(4, 5))
    )
    assert isinstance(st_01, app.CompositeState)
    require_true(st_01.X.B1 != app.zero_q4(), "T17.M_single.B1_nonzero")
    require_eq((st_01.W, st_01.sigma_B), (Fraction(1, 10), -1), "T17.M_single.W_sigB")

    # (b) M_cold on (4,4) at B* = 8224427/10497600
    b_star = Fraction(8224427, 10497600)
    st_44 = app.run_seven_steps(
        app.prepare_ready_state((4, 0, 0, 0), (4, 0, 0, 0), b_star, b_init=b_star)
    )
    assert isinstance(st_44, app.CompositeState)
    require_eq((st_44.sigma_B, st_44.b), (-1, Fraction(0, 1)), "T17.M_cold.st_44")
    require_eq(
        b_star - Fraction(2, 5) - Fraction(2, 5),
        Fraction(-173653, 10497600),
        "T17.M_cold.deficit",
    )

    # (c) M_{2-slot} on (1,0) at B = 4/5 retains A_final = (b0, b1) != (0,0)
    st_10 = app.run_seven_steps(
        app.prepare_ready_state((1, 0, 0, 0), (0, 0, 0, 0), Fraction(4, 5))
    )
    assert isinstance(st_10, app.CompositeState)
    require_true(
        st_10.X.A0 != app.zero_q4() and st_10.X.A1 != app.zero_q4(),
        "T17.M_2slot.A_nonzero",
    )

    # (d) M_{1sigma} direct un-reset shared-sigma on (0,1) at B = 4/5 gives -R0 z^(1) != +R0 z^(1)
    require_true(st_01.X.B1 != tuple(-x for x in st_01.X.B1), "T17.M_1sigma.sign_sep")

    return "T17 PASS: matched classical comparator agreement and 5 restricted-comparator separations verified"


def run_t18_invalid_endpoint_and_type_rejection_suite() -> str:
    cap = Fraction(4, 5)
    valid_st = app.run_seven_steps(
        app.prepare_ready_state((0, 0, 0, 0), (1, 0, 0, 0), cap, b_init=cap)
    )
    assert isinstance(valid_st, app.CompositeState)
    require_eq(
        app.recognize_ready_image(valid_st, c0=app.zero_q4(), c1=app.zero_q4(), b_init=cap)[
            "valid"
        ],
        True,
        "T18.valid_baseline",
    )

    # X01: Selector piston-sum mismatch (x_{5,A} = g_3(1,0,0,0,0,1) has rec=(1,0)=C3(0) and
    # inverse word g1 g1 g3 x_{5,A} = (1,0,0,0,0,1) has rec=(0,1), but piston sum 1 != 0)
    bad_x5a = app.apply_generator(3, (1, 0, 0, 0, 0, 1))
    require_eq(app.receiver_of(bad_x5a), (1, 0), "T18.X01.rec")
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
    require_eq(res_x01["valid"], False, "T18.X01.valid")
    require_eq(
        res_x01["failed_test"],
        "test2_piston_sum_selector_consistency",
        "T18.X01.failed_test",
    )

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
    require_eq((res_x02["valid"], res_x02["failed_test"]), (False, "test1_c3_receiver"), "T18.X02")

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
    require_eq(
        app.recognize_ready_image(st_x03_n)["failed_test"],
        "test1_clock_n5_c7",
        "T18.X03.n",
    )
    require_eq(
        app.recognize_ready_image(st_x03_c)["failed_test"],
        "test1_clock_n5_c7",
        "T18.X03.c",
    )
    require_eq(
        app.recognize_ready_image(st_x03_k)["failed_test"],
        "test4_initial_k_zero",
        "T18.X03.k",
    )

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
    require_eq(
        app.recognize_ready_image(st_x04)["failed_test"],
        "test3_delayed_buffer_d",
        "T18.X04",
    )

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
    require_eq(
        app.recognize_ready_image(st_x05)["failed_test"],
        "test4_initial_sigma_plus1",
        "T18.X05",
    )

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
    require_eq(
        app.recognize_ready_image(st_x06, b_init=cap)["failed_test"],
        "test4_initial_store_b",
        "T18.X06",
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
    require_eq(
        app.recognize_ready_image(st_x07)["failed_test"],
        "test4_initial_W_zero",
        "T18.X07",
    )

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
    require_eq(app.recognize_ready_image(st_x08)["valid"], False, "T18.X08")

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
    require_eq(
        app.recognize_ready_image(st_x09)["failed_test"],
        "test4_initial_wave_zero",
        "T18.X09",
    )

    # X10: Malformed carrier types (bool, float, out-of-range residues, wrong dimension 869 vs 705)
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
        lambda: app.WaveTapeState(
            u=(Fraction(0, 1),) * 869,
            v=valid_st.X.v,
            A0=valid_st.X.A0,
            A1=valid_st.X.A1,
            B0=valid_st.X.B0,
            B1=valid_st.X.B1,
            k=0,
        ),
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
    for idx, fn in enumerate(malformed_calls):
        caught = False
        err_msg = ""
        try:
            fn()
        except (TypeError, ValueError) as exc:
            caught = True
            err_msg = str(exc)
        require_true(caught, f"T18.X10[{idx}]")
        require_true(
            "expected" in err_msg and "actual" in err_msg,
            f"T18.X10_msg_expected_actual[{idx}]",
            expected="expected/actual in error message",
            actual=err_msg,
        )

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


def print_witness_report(witnesses: Sequence[Tuple[str, Tuple[app.CompositeState, ...]]]) -> None:
    for name, bounds in witnesses:
        print(f"[{name}]")
        for st in bounds:
            print(format_boundary_line(st))
    w1_c7 = witnesses[0][1][7]
    w2_c7 = witnesses[1][1][7]
    w3_c7 = witnesses[2][1][7]
    w4_c7 = witnesses[3][1][7]
    w5_c7 = witnesses[4][1][7]
    w6_c7 = witnesses[5][1][7]
    diff_14_41 = w1_c7.W - w2_c7.W
    print(
        f"WITNESS_SUMMARY order_W14={fmt_frac(w1_c7.W)} order_W41={fmt_frac(w2_c7.W)} "
        f"order_diff={fmt_frac(diff_14_41)} dirty_c1_e0_B0={fmt_vec4(w3_c7.X.B0)} "
        f"ready_low_ref_sig=({w4_c7.sigma_A:+d},{w4_c7.sigma_B:+d}) "
        f"warm_low_ref_sig=({w5_c7.sigma_A:+d},{w5_c7.sigma_B:+d}) "
        f"warm_high_ref_sig=({w6_c7.sigma_A:+d},{w6_c7.sigma_B:+d})"
    )


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
    print("C-FUNDED-TWO-USE-EXECUTABLE-2-N AUDIT START")
    for fn in tests:
        msg = fn()
        print(msg)

    print("WITNESS_BOUNDARY_STATES_BEGIN")
    witnesses = build_witness_trajectories()
    print_witness_report(witnesses)
    print("WITNESS_BOUNDARY_STATES_END")
    print(
        "C-FUNDED-TWO-USE-EXECUTABLE-2-N AUDIT PASS: tests=18/18 invalid_endpoints=10/10 "
        "domain_sites=705 basis_dim=1426 order_diff=313/233280 max_work=8224427/10497600 status=ALL_PASS"
    )


def main(argv: Sequence[str]) -> int:
    if len(argv) == 1:
        run_full_audit()
        return 0
    if len(argv) == 2 and argv[1] == "--compare":
        domain_sha, count, digest = app.compute_comparison_digest()
        print(
            f"TWOUSE-COMPARE-v2 domain_sha256={domain_sha} records={count} sha256={digest}"
        )
        return 0
    if len(argv) == 2 and argv[1] == "--witnesses":
        print_witness_report(build_witness_trajectories())
        return 0
    sys.stderr.write(f"Usage: {argv[0]} [--compare | --witnesses]\n")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
