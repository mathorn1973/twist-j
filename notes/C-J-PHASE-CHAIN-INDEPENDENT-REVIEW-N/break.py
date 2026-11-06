#!/usr/bin/env python3
"""Independent standalone breaker and verifier for #1598 (C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N).

PUBLIC / NON-CANONICAL / L1.
Reviewer session: Antigravity-phase-chain-review-20261018 (A. M. Thorn, Apache-2.0).

Method-blind phase-1 implementation written from the frozen specifications and
public Canon equations before opening target PROOF.md, verify.py, RESULT.md,
EXPECTED.txt, or RUN.md on PRs #1577, #1579, and #1581.
Uses Python 3 standard library only; no target or canonical probe module is imported.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
REVIEW_DIR = Path(__file__).resolve().parent
SOURCES_TSV = REVIEW_DIR / "SOURCES.tsv"
DOMAIN_TSV = REPO_ROOT / "probes" / "P-TWO-USE-TYPED-READOUT-CLOSURE-1" / "DOMAIN.tsv"

F5 = (0, 1, 2, 3, 4)
BITS = (0, 1)
ELL = (0, 1, 2, -2, -1)

# Five fifth-root pistons in marked order (1, j, j^2, j^3, j^4)
ROOT_PISTONS: Tuple[Tuple[int, int, int, int], ...] = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
    (4, 4, 4, 4),
)

# Three determinant-one reference pistons of #1581 and single receiver I2 of #1579
REF_YA = (0, 2, 2, 0)
REF_YB = (4, 2, 2, 0)
REF_YC = (1, 1, 0, 1)
REFS_3 = (REF_YA, REF_YB, REF_YC)
REF_WEIGHTS = (1, 2, 4)
I2_PISTON = (1, 0, 0, 1)
COLLECTOR_Z0 = (4, 0, 4, 2, 0, 0)

# Reading involution table P_q(r) from DEF-RESIDUAL-CONTACT-ARCHITECTURE
P_TABLE: Tuple[Tuple[int, int, int, int, int], ...] = (
    (0, 2, 1, 3, 4),
    (0, 1, 2, 3, 4),
    (2, 1, 0, 3, 4),
    (1, 0, 2, 3, 4),
    (1, 0, 2, 3, 4),
)

# Lattice geometry constants from primary specification
Y_SITES: Tuple[Tuple[int, int, int], ...] = (
    (0, 0, 0),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
    (2, 0, 0),
)
SHELL_WEIGHTS: Dict[int, int] = {2: 6, 4: 1, 8: 15, 10: 1, 16: 1}
STENCIL_DENOM = 324
DIAG_H = Fraction(10, 9)


def require(cond: bool, label: str, detail: object = None) -> None:
    if not cond:
        raise AssertionError(f"FALSIFIER [{label}]: {detail!r}")


# ---------------------------------------------------------------------------
# 0. Custody check of SOURCES.tsv on main worktree files and DOMAIN.tsv
# ---------------------------------------------------------------------------

def check_sources_custody() -> Dict[str, int]:
    require(SOURCES_TSV.is_file(), "sources_tsv_exists")
    lines = SOURCES_TSV.read_text(encoding="utf-8").splitlines()
    require(len(lines) == 18, "sources_tsv_row_count", len(lines))
    header = lines[0].split("\t")
    require(
        header == ["path", "commit", "git_blob", "bytes", "sha256", "role", "license"],
        "sources_tsv_header",
        header,
    )
    checked_main_files = 0
    for row in lines[1:]:
        path_str, commit_sha, _blob, exp_bytes_s, exp_sha, role, _lic = row.split("\t")
        exp_bytes = int(exp_bytes_s)
        if commit_sha == "dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d":
            fpath = REPO_ROOT / path_str
            require(fpath.is_file(), "main_source_exists", path_str)
            raw = fpath.read_bytes()
            act_sha = hashlib.sha256(raw).hexdigest()
            require(len(raw) == exp_bytes, "main_source_bytes", (path_str, len(raw), exp_bytes))
            require(act_sha == exp_sha, "main_source_sha256", (path_str, act_sha, exp_sha))
            checked_main_files += 1
        else:
            require(role.startswith("target_pr"), "pinned_target_role", (path_str, role))
    require(checked_main_files == 14, "checked_main_files_count", checked_main_files)
    return {"sources_rows": len(lines) - 1, "checked_main_files": checked_main_files}


# ---------------------------------------------------------------------------
# 1. Cyclotomic algebra, native generators, and quotient envelope E_Q
# ---------------------------------------------------------------------------

def cyc_to_power_5(coeffs_b0: Sequence[int]) -> Tuple[int, int, int, int, int]:
    """Embed B0 = (1, zeta, zeta^2, zeta^3) into Z^5 mod (1+zeta+zeta^2+zeta^3+zeta^4)."""
    return (coeffs_b0[0], coeffs_b0[1], coeffs_b0[2], coeffs_b0[3], 0)


def cyc_reduce_b0(v5: Sequence[int]) -> Tuple[int, int, int, int]:
    """Reduce a 5-tuple in Z[zeta_5] to basis B0 by subtracting v5[4]*(1+zeta+zeta^2+zeta^3+zeta^4)."""
    c4 = v5[4]
    return (v5[0] - c4, v5[1] - c4, v5[2] - c4, v5[3] - c4)


def cyc_mul_b0(a: Sequence[int], b: Sequence[int]) -> Tuple[int, int, int, int]:
    res = [0, 0, 0, 0, 0]
    for i in range(4):
        for k in range(4):
            res[(i + k) % 5] += a[i] * b[k]
    return cyc_reduce_b0(res)


def cyc_galois_b0(a: Sequence[int], m: int) -> Tuple[int, int, int, int]:
    res = [0, 0, 0, 0, 0]
    for i in range(4):
        res[(i * m) % 5] += a[i]
    return cyc_reduce_b0(res)


def native_gen(g: int, cell: Tuple[int, int, int, int, int, int]) -> Tuple[int, int, int, int, int, int]:
    a, b, c, d, q, r = cell
    if g == 0:
        return (b, a, d, c, q, r)
    if g == 1:
        return ((-c) % 5, (-d) % 5, (-a) % 5, (-b) % 5, (-q) % 5, (-r) % 5)
    if g == 2:
        return ((2 - c) % 5, (1 + r - d) % 5, (2 - a) % 5, (1 - r - b) % 5, (1 - q) % 5, (-r) % 5)
    if g == 3:
        return ((2 - a) % 5, (1 - b) % 5, (3 - c) % 5, (4 - d) % 5, (1 - q) % 5, (1 - r) % 5)
    if g == 4:
        return ((2 - a) % 5, (1 - b) % 5, (3 - c) % 5, (4 - d) % 5, (2 - q) % 5, (1 - r) % 5)
    raise ValueError(f"Invalid generator {g}")


def quotient_q(cell: Tuple[int, int, int, int, int, int]) -> Tuple[int, int, int]:
    return (sum(cell) % 5, cell[4], cell[5])


def quotient_gen(g: int, q_triple: Tuple[int, int, int]) -> Tuple[int, int, int]:
    z, q, r = q_triple
    if g == 0:
        return (z, q, r)
    if g == 1:
        return ((-z) % 5, (-q) % 5, (-r) % 5)
    if g == 2:
        return ((2 - z) % 5, (1 - q) % 5, (-r) % 5)
    if g == 3:
        return ((2 - z) % 5, (1 - q) % 5, (1 - r) % 5)
    if g == 4:
        return ((3 - z) % 5, (2 - q) % 5, (1 - r) % 5)
    raise ValueError(f"Invalid generator {g}")


def native_u_step(n: int, cell: Tuple[int, int, int, int, int, int]) -> Tuple[int, Tuple[int, int, int, int, int, int]]:
    theta = n.bit_count() % 2
    sel = (sum(cell) + 2 * theta) % 5
    return n + 1, native_gen(sel, cell)


def check_cyclotomic_and_quotient_envelope() -> Dict[str, object]:
    # 1. Five roots in Z[zeta_5]
    mixed_terms = []
    for k, p in enumerate(ROOT_PISTONS):
        beta = tuple(ELL[x] for x in p)
        # Check that beta equals zeta_5^k in B0
        expected_unit = [0, 0, 0, 0, 0]
        expected_unit[k] = 1
        require(beta == cyc_reduce_b0(expected_unit), "root_balanced_lift", (k, p, beta))
        # Augmentation: sum_{i=0}^3 beta_i * 1^i
        # Since zeta=1 maps B0=(1,1,1,1), WAIT: in Z[zeta_5], aug(zeta^k) = 1.
        # In terms of representative sum in Z[zeta_5]/(zeta_5-1), beta_0+beta_1+beta_2+beta_3 mod 5 == 1!
        require(sum(beta) % 5 == 1, "root_augmentation_mod5", (k, beta))
        require(sum(p) % 5 == 1, "root_piston_sum_mod5", (k, p))
        a_norm = cyc_mul_b0(beta, cyc_galois_b0(beta, 4))
        b_norm = cyc_mul_b0(cyc_galois_b0(beta, 2), cyc_galois_b0(beta, 3))
        require(a_norm == (1, 0, 0, 0) and b_norm == (1, 0, 0, 0), "root_archimedean_norms", k)
        c_mixed = cyc_mul_b0(beta, cyc_galois_b0(beta, 3))
        exp_c = [0, 0, 0, 0, 0]
        exp_c[(-k) % 5] = 1
        require(c_mixed == cyc_reduce_b0(exp_c), "root_mixed_term", (k, c_mixed))
        mixed_terms.append(c_mixed)
        cell = p + (0, 1)
        require(quotient_q(cell) == (2, 0, 1), "root_common_initial_quotient", (k, cell))
    require(len(set(mixed_terms)) == 5, "distinct_mixed_terms", mixed_terms)

    # Four basis checks for augmentation mod 5 under multiplication by j
    for i in range(4):
        e_i = tuple(int(m == i) for m in range(4))
        j_ei = cyc_mul_b0((0, 1, 0, 0), e_i)
        require(sum(j_ei) % 5 == sum(e_i) % 5, "basis_augmentation_mul_j", i)

    # 2. Exhaustive 15625 native checkpoints x 2 driver values = 31250 steps
    selected_steps = 0
    for cell in product(F5, repeat=6):
        q_in = quotient_q(cell)
        for g in F5:
            img = native_gen(g, cell)
            require(native_gen(g, img) == cell, "native_gen_involution", (g, cell))
            require(quotient_q(img) == quotient_gen(g, q_in), "native_gen_quotient", (g, cell))
        for theta in BITS:
            sel = (sum(cell) + 2 * theta) % 5
            img_u = native_gen(sel, cell)
            sel_q = (q_in[0] + 2 * theta) % 5
            require(sel == sel_q, "selector_factors_through_q", (cell, theta))
            require(quotient_q(img_u) == quotient_gen(sel_q, q_in), "u_step_quotient_law", (cell, theta))
            selected_steps += 1
    require(selected_steps == 31250, "selected_steps_count", selected_steps)

    # 3. 35 affine basis rows (zero + 6 basis vectors of F5^6 x 5 generators)
    basis_6 = [(0, 0, 0, 0, 0, 0)] + [tuple(int(j == i) for j in range(6)) for i in range(6)]
    affine_basis_rows = 0
    for b_cell in basis_6:
        for g in F5:
            require(
                quotient_q(native_gen(g, b_cell)) == quotient_gen(g, quotient_q(b_cell)),
                "affine_basis_quotient_row",
                (b_cell, g),
            )
            affine_basis_rows += 1
    require(affine_basis_rows == 35, "affine_basis_rows_count", affine_basis_rows)

    # 4. 125 Ucal quotient triples
    ucal_triples = 0
    for z, q, r in product(F5, repeat=3):
        p0 = (z - q - r) % 5
        rep_cell = (p0, 0, 0, 0, q, r)
        u_cell = (p0, 0, 0, 0, q, P_TABLE[q][r])
        require(
            quotient_q(u_cell) == ((z - r + P_TABLE[q][r]) % 5, q, P_TABLE[q][r]),
            "ucal_quotient_triple",
            (z, q, r),
        )
        ucal_triples += 1
    require(ucal_triples == 125, "ucal_triples_count", ucal_triples)

    # 5. Whole-cell CSUM on zero + 12 basis vectors of F5^12 (13 rows, 26 signed checks)
    basis_12 = [(0,) * 12] + [tuple(int(j == i) for j in range(12)) for i in range(12)]
    csum_rows = 0
    for vec12 in basis_12:
        x_cell = vec12[:6]
        y_cell = vec12[6:]
        qx = quotient_q(x_cell)
        qy = quotient_q(y_cell)
        y_plus = tuple((y_cell[i] + x_cell[i]) % 5 for i in range(6))
        y_minus = tuple((y_cell[i] - x_cell[i]) % 5 for i in range(6))
        y_back = tuple((y_plus[i] - x_cell[i]) % 5 for i in range(6))
        require(y_back == y_cell, "csum_basis_inverse", vec12)
        require(
            quotient_q(y_plus) == tuple((qy[i] + qx[i]) % 5 for i in range(3)),
            "csum_plus_quotient",
            vec12,
        )
        require(
            quotient_q(y_minus) == tuple((qy[i] - qx[i]) % 5 for i in range(3)),
            "csum_minus_quotient",
            vec12,
        )
        csum_rows += 1
    require(csum_rows == 13, "csum_rows_count", csum_rows)

    return {
        "selected_steps": selected_steps,
        "affine_basis_rows": affine_basis_rows,
        "ucal_triples": ucal_triples,
        "csum_basis_rows": csum_rows,
    }


# ---------------------------------------------------------------------------
# 2. Determinant polarization, 625-reference census, and 3-reference code
# ---------------------------------------------------------------------------

def h_polar(px: Tuple[int, int, int, int], py: Tuple[int, int, int, int]) -> int:
    a, b, c, d = px
    u, v, w, z = py
    return (3 * (a * z + d * u) + 2 * (b * w + c * v)) % 5


def det_2x2(p: Tuple[int, int, int, int]) -> int:
    return (p[0] * p[3] - p[1] * p[2]) % 5


def delta_polar(px: Tuple[int, int, int, int], py: Tuple[int, int, int, int]) -> int:
    val = h_polar(px, py)
    return 1 if val == 0 else 0


def check_reference_census_and_code() -> Dict[str, object]:
    eval_count = 0
    hyperplane_images = set()
    mask_counts: Dict[Tuple[int, int, int, int, int], int] = {
        m: 0 for m in product(BITS, repeat=5)
    }
    sep_j_j4 = 0
    sep_both_conj = 0
    conj_patterns: Dict[Tuple[int, int, int, int], int] = {}

    for y in product(F5, repeat=4):
        u, v, w, z = y
        h_tuple = tuple(h_polar(p, y) for p in ROOT_PISTONS)
        eval_count += 5
        # Verify polarization equals (det(P+Y)-det(P)-det(Y))/2 mod 5
        for k, p in enumerate(ROOT_PISTONS):
            py_sum = tuple((p[i] + y[i]) % 5 for i in range(4))
            polar_det = (3 * (det_2x2(py_sum) - det_2x2(p) - det_2x2(y))) % 5
            require(h_tuple[k] == polar_det, "det_polarization_identity", (p, y))
        expected_phi = tuple(
            (3 * val) % 5 for val in (z, -w, -v, u, v + w - u - z)
        )
        require(h_tuple == expected_phi, "hyperplane_formula_match", (y, h_tuple, expected_phi))
        require(sum(h_tuple) % 5 == 0, "hyperplane_sum_zero", h_tuple)
        hyperplane_images.add(h_tuple)

        mask = tuple(1 if x == 0 else 0 for x in h_tuple)
        mask_counts[mask] += 1
        neg_y = tuple((-c) % 5 for c in y)
        neg_mask = tuple(delta_polar(p, neg_y) for p in ROOT_PISTONS)
        require(mask == neg_mask, "mask_sign_invariance", y)

        if mask[1] != mask[4]:
            sep_j_j4 += 1
            if mask[2] != mask[3]:
                sep_both_conj += 1
                pat = mask[1:5]
                conj_patterns[pat] = conj_patterns.get(pat, 0) + 1

    require(eval_count == 3125, "polar_evaluations_count", eval_count)
    require(len(hyperplane_images) == 625, "hyperplane_bijection_size", len(hyperplane_images))

    expected_per_weight = {0: 204, 1: 52, 2: 12, 3: 4, 4: 0, 5: 1}
    nonempty_classes = 0
    for mask, cnt in mask_counts.items():
        wt = sum(mask)
        require(cnt == expected_per_weight[wt], "mask_count_by_weight", (mask, cnt, expected_per_weight[wt]))
        if cnt > 0:
            nonempty_classes += 1
    require(nonempty_classes == 27, "nonempty_mask_classes", nonempty_classes)
    require(sep_j_j4 == 200, "sep_j_j4_count", sep_j_j4)
    require(sep_both_conj == 64, "sep_both_conj_count", sep_both_conj)
    require(
        conj_patterns == {
            (1, 1, 0, 0): 16,
            (1, 0, 1, 0): 16,
            (0, 1, 0, 1): 16,
            (0, 0, 1, 1): 16,
        },
        "conj_patterns_four_embeddings",
        conj_patterns,
    )
    const_masks = mask_counts[(0, 0, 0, 0, 0)] + mask_counts[(1, 1, 1, 1, 1)]
    require(const_masks == 205, "constant_masks_count", const_masks)

    # Check single receiver I2=(1,0,0,1) mask in #1579
    i2_mask = tuple(delta_polar(p, I2_PISTON) for p in ROOT_PISTONS)
    require(i2_mask == (0, 1, 1, 0, 0), "i2_five_root_mask", i2_mask)

    # Check three references YA, YB, YC in #1581
    for ref in REFS_3:
        require(det_2x2(ref) == 1, "ref_det_one", ref)
    mask_a = tuple(delta_polar(p, REF_YA) for p in ROOT_PISTONS)
    mask_b = tuple(delta_polar(p, REF_YB) for p in ROOT_PISTONS)
    mask_c = tuple(delta_polar(p, REF_YC) for p in ROOT_PISTONS)
    require(mask_a == (1, 0, 0, 1, 0), "mask_ya", mask_a)
    require(mask_b == (1, 0, 0, 0, 1), "mask_yb", mask_b)
    require(mask_c == (0, 1, 0, 0, 0), "mask_yc", mask_c)

    codes_m = tuple((mask_a[k] + 2 * mask_b[k] + 4 * mask_c[k]) % 5 for k in range(5))
    require(codes_m == (3, 4, 0, 1, 2), "five_phase_codes_m", codes_m)
    for k in range(5):
        require((codes_m[k] + 2) % 5 == k, "five_phase_decoder_inverse", k)

    # Binary-output lower bound in frozen class
    require((1 << 2) < 5 <= (1 << 3), "binary_output_lower_bound_three")

    # Zero-piston alias vs present identity phase k=0
    zero_p = (0, 0, 0, 0)
    zero_deltas = tuple(delta_polar(zero_p, r) for r in REFS_3)
    zero_m = (zero_deltas[0] + 2 * zero_deltas[1] + 4 * zero_deltas[2]) % 5
    require(zero_deltas == (1, 1, 1) and zero_m == 2, "zero_piston_alias_m2", (zero_deltas, zero_m))
    require(zero_m == codes_m[4] and zero_m != codes_m[0], "zero_aliases_j4_not_identity")

    return {
        "polar_evaluations": eval_count,
        "nonempty_mask_classes": nonempty_classes,
        "sep_j_j4": sep_j_j4,
        "sep_both_conj": sep_both_conj,
        "const_masks": const_masks,
        "i2_mask": list(i2_mask),
        "codes_m": list(codes_m),
    }


# ---------------------------------------------------------------------------
# 3. Literal contact leaves, #1579 2500/75000 audit, and #1581 18750 + 50x182 audit
# ---------------------------------------------------------------------------

AY_WORD: Tuple[str, ...] = (
    "Uy", "ey", "dy", "W", "bx", "by", "W", "dy", "ey", "W", "by", "bx", "W", "Uy"
)
AX_WORD: Tuple[str, ...] = (
    "Ux", "ex", "dx", "W", "bx", "by", "W", "dx", "ex", "W", "by", "bx", "W", "Ux"
)


def contact_leaf_pair(
    cell_x: Tuple[int, int, int, int, int, int],
    cell_y: Tuple[int, int, int, int, int, int],
    eta: int,
    op: str,
) -> Tuple[Tuple[int, int, int, int, int, int], Tuple[int, int, int, int, int, int], int]:
    """Execute one literal leaf on (cell_x, cell_y, eta) where each cell is (a,b,c,d,q,r)."""
    if op == "W":
        val = h_polar(cell_x[:4], cell_y[:4])
        if val == 0:
            return cell_x, cell_y, eta
        sig = 1 if val in (3, 4) else 0
        if sig != eta:
            return native_gen(1, cell_x), native_gen(1, cell_y), sig
        return cell_x, cell_y, sig
    letter, side = op[0], op[1]
    target = cell_x if side == "x" else cell_y
    if letter == "U":
        q, r = target[4], target[5]
        updated = target[:4] + (q, P_TABLE[q][r])
    elif letter == "b":
        updated = native_gen(1, target)
    elif letter == "d":
        updated = native_gen(3, target)
    elif letter == "e":
        updated = native_gen(4, target)
    else:
        raise ValueError(f"Unknown leaf {op}")
    if side == "x":
        return updated, cell_y, eta
    return cell_x, updated, eta


def run_contact_word(
    cell_x: Tuple[int, int, int, int, int, int],
    cell_y: Tuple[int, int, int, int, int, int],
    eta: int,
    word: Sequence[str],
) -> Tuple[Tuple[int, int, int, int, int, int], Tuple[int, int, int, int, int, int], int]:
    for op in word:
        cell_x, cell_y, eta = contact_leaf_pair(cell_x, cell_y, eta, op)
    return cell_x, cell_y, eta


def check_contact_inventories() -> Dict[str, object]:
    # 1. Verify first unequal (Q(x), Q(y), eta) leaf in A_y for #1579 controls (j vs j^-1 on I2)
    x_plus = ROOT_PISTONS[1] + (0, 1)
    x_minus = ROOT_PISTONS[4] + (0, 1)
    y_i2 = I2_PISTON + (0, 0)
    cx_p, cy_p, eta_p = x_plus, y_i2, 0
    cx_m, cy_m, eta_m = x_minus, y_i2, 0
    first_diff_leaf: Optional[Tuple[int, str]] = None
    for idx, op in enumerate(AY_WORD, start=1):
        cx_p, cy_p, eta_p = contact_leaf_pair(cx_p, cy_p, eta_p, op)
        cx_m, cy_m, eta_m = contact_leaf_pair(cx_m, cy_m, eta_m, op)
        q_state_p = (quotient_q(cx_p), quotient_q(cy_p), eta_p)
        q_state_m = (quotient_q(cx_m), quotient_q(cy_m), eta_m)
        if q_state_p != q_state_m and first_diff_leaf is None:
            first_diff_leaf = (idx, op)
    require(first_diff_leaf == (4, "W"), "first_unequal_q_bit_leaf", first_diff_leaf)
    require(cy_p == (1, 0, 0, 1, 3, 1) and cy_m == (1, 0, 0, 1, 0, 0), "i2_endpoints_j_jinv", (cy_p, cy_m))

    # 2. #1579 inventory: 2500 complete cases + 500 ry=0 ready cases + 75000 continuation boundaries
    cases_1579 = 0
    ready_1579 = 0
    cont_boundaries_1579 = 0
    ay_rev = tuple(reversed(AY_WORD))
    ax_rev = tuple(reversed(AX_WORD))

    for px in (ROOT_PISTONS[1], ROOT_PISTONS[4]):
        delt = delta_polar(px, I2_PISTON)
        for qx, qy, rx, ry in product(F5, repeat=4):
            for eta in BITS:
                cx0 = px + (qx, rx)
                cy0 = I2_PISTON + (qy, ry)
                cx1, cy1, eta1 = run_contact_word(cx0, cy0, eta, AY_WORD)
                exp_qy = (qy + 3 * delt) % 5
                exp_ry = P_TABLE[exp_qy][P_TABLE[qy][ry]]
                require(
                    cx1 == cx0 and cy1 == I2_PISTON + (exp_qy, exp_ry) and eta1 == eta,
                    "contact_1579_endpoint",
                    (cx0, cy0, eta),
                )
                if ry == 0:
                    require(cy1[5] == delt, "contact_1579_ready_write", (px, qx, qy, rx, eta))
                    ready_1579 += 1
                bx0, by0, beta0 = run_contact_word(cx1, cy1, eta1, ay_rev)
                require((bx0, by0, beta0) == (cx0, cy0, eta), "contact_1579_inverse")

                # Continuation through A_x and A_x^-1 (15 boundaries each, including initial)
                ry_sq = (cy1[5] * cy1[5]) % 5
                for cont_word in (AX_WORD, ax_rev):
                    tx, ty, teta = cx1, cy1, eta1
                    require((ty[5] * ty[5]) % 5 == ry_sq, "cont_boundary_0_ry_sq")
                    cont_boundaries_1579 += 1
                    for op in cont_word:
                        tx, ty, teta = contact_leaf_pair(tx, ty, teta, op)
                        require((ty[5] * ty[5]) % 5 == ry_sq, "cont_boundary_ry_sq", op)
                        cont_boundaries_1579 += 1
                    require(ty == cy1 and teta == eta1, "cont_full_y_restored")
                cases_1579 += 1

    require(cases_1579 == 2500, "cases_1579_count", cases_1579)
    require(ready_1579 == 500, "ready_1579_count", ready_1579)
    require(cont_boundaries_1579 == 75000, "cont_boundaries_1579_count", cont_boundaries_1579)

    # 3. #1581 inventory: 18750 occupied contact cases + 3750 ry=0 ready cases
    cases_1581 = 0
    ready_1581 = 0
    sample_collector = (3, 1, 4, 2, 1, 3)
    for px in ROOT_PISTONS:
        for ref_idx, py in enumerate(REFS_3):
            wt = REF_WEIGHTS[ref_idx]
            delt = delta_polar(px, py)
            for qx, rx, qy, ry in product(F5, repeat=4):
                for eta in BITS:
                    cx0 = px + (qx, rx)
                    cy0 = py + (qy, ry)
                    cx1, cy1, eta1 = run_contact_word(cx0, cy0, eta, AY_WORD)
                    exp_qy = (qy + 3 * delt) % 5
                    exp_ry = P_TABLE[exp_qy][P_TABLE[qy][ry]]
                    require(
                        cx1 == cx0 and cy1 == py + (exp_qy, exp_ry) and eta1 == eta,
                        "contact_1581_endpoint",
                    )
                    if ry == 0:
                        require(cy1[5] == delt, "contact_1581_ready_write")
                        ready_1581 += 1
                    # Weighted CSUM addition to collector and inverse
                    z_coll = sample_collector
                    for _ in range(wt):
                        z_coll = tuple((z_coll[i] + cy1[i]) % 5 for i in range(6))
                    exp_z = tuple((sample_collector[i] + wt * cy1[i]) % 5 for i in range(6))
                    require(z_coll == exp_z, "weighted_csum_collector")
                    for _ in range(wt):
                        z_coll = tuple((z_coll[i] - cy1[i]) % 5 for i in range(6))
                    require(z_coll == sample_collector, "weighted_csum_inverse")
                    bx0, by0, beta0 = run_contact_word(cx1, cy1, eta1, ay_rev)
                    require((bx0, by0, beta0) == (cx0, cy0, eta), "contact_1581_inverse")
                    cases_1581 += 1

    require(cases_1581 == 18750, "cases_1581_count", cases_1581)
    require(ready_1581 == 3750, "ready_1581_count", ready_1581)

    return {
        "first_unequal_leaf": f"{first_diff_leaf[0]}:{first_diff_leaf[1]}",
        "cases_1579": cases_1579,
        "ready_1579": ready_1579,
        "cont_boundaries_1579": cont_boundaries_1579,
        "cases_1581": cases_1581,
        "ready_1581": ready_1581,
    }


def run_three_ref_prefix_on_joined(
    p_a: Tuple[int, int, int, int],
    p_b: Tuple[int, int, int, int],
    eta0: int,
    *,
    omit_w: bool = False,
) -> Dict[str, object]:
    """Execute the 182-operation prefix (or 102-operation W-deleted control) on the joined carrier."""
    s_a = p_a + (0, 1)
    s_b = p_b + (0, 1)
    refs = [REF_YA + (0, 0), REF_YB + (0, 0), REF_YC + (0, 0)]
    heads = [COLLECTOR_Z0, COLLECTOR_Z0]
    eta = eta0
    classical_marker = ("COLD_CLASSICAL_STATE", 0, 0, 0, 5, 1, 1, (0, 0))

    word_fwd = tuple(op for op in AY_WORD if not (omit_w and op == "W"))
    word_inv = tuple(reversed(word_fwd))

    forward_trace_ops: List[Tuple[str, int, int, str]] = []
    leaf_count = 0
    contact_leaves = 0
    csum_leaves = 0
    block_checks = 0
    second_source_head0_checks = 0

    for lane_idx in (0, 1):
        head0_snapshot = heads[0]
        for ref_idx in (0, 1, 2):
            wt = REF_WEIGHTS[ref_idx]
            # Forward A_y on (source[lane_idx], refs[ref_idx], eta)
            for op in word_fwd:
                src = s_a if lane_idx == 0 else s_b
                src_new, ref_new, eta = contact_leaf_pair(src, refs[ref_idx], eta, op)
                if lane_idx == 0:
                    s_a = src_new
                else:
                    s_b = src_new
                refs[ref_idx] = ref_new
                forward_trace_ops.append(("contact", lane_idx, ref_idx, op))
                leaf_count += 1
                contact_leaves += 1
                require(
                    classical_marker == ("COLD_CLASSICAL_STATE", 0, 0, 0, 5, 1, 1, (0, 0)),
                    "classical_unchanged_at_leaf",
                )
                if lane_idx == 1:
                    require(heads[0] == head0_snapshot, "head0_preserved_during_lane1")
                    second_source_head0_checks += 1
            # Weighted CSUM from refs[ref_idx] into heads[lane_idx]
            for _ in range(wt):
                heads[lane_idx] = tuple((heads[lane_idx][i] + refs[ref_idx][i]) % 5 for i in range(6))
                forward_trace_ops.append(("csum_add", lane_idx, ref_idx, "CSUM"))
                leaf_count += 1
                csum_leaves += 1
                if lane_idx == 1:
                    require(heads[0] == head0_snapshot, "head0_preserved_during_lane1_csum")
                    second_source_head0_checks += 1
            # Inverse A_y^-1 on (source[lane_idx], refs[ref_idx], eta)
            for op in word_inv:
                src = s_a if lane_idx == 0 else s_b
                src_new, ref_new, eta = contact_leaf_pair(src, refs[ref_idx], eta, op)
                if lane_idx == 0:
                    s_a = src_new
                else:
                    s_b = src_new
                refs[ref_idx] = ref_new
                forward_trace_ops.append(("contact", lane_idx, ref_idx, op))
                leaf_count += 1
                contact_leaves += 1
                if lane_idx == 1:
                    require(heads[0] == head0_snapshot, "head0_preserved_during_lane1_inv")
                    second_source_head0_checks += 1
            # Block boundary check: sources, all 3 references, and eta restored
            require(s_a == p_a + (0, 1) and s_b == p_b + (0, 1), "block_sources_restored")
            require(
                refs == [REF_YA + (0, 0), REF_YB + (0, 0), REF_YC + (0, 0)],
                "block_refs_restored",
            )
            require(eta == eta0, "block_eta_restored")
            block_checks += 1

    final_heads = (heads[0], heads[1])

    # Run full reverse word and verify complete joined state restoration
    for kind, lane_idx, ref_idx, op in reversed(forward_trace_ops):
        if kind == "csum_add":
            heads[lane_idx] = tuple((heads[lane_idx][i] - refs[ref_idx][i]) % 5 for i in range(6))
        else:
            src = s_a if lane_idx == 0 else s_b
            src_new, ref_new, eta = contact_leaf_pair(src, refs[ref_idx], eta, op)
            if lane_idx == 0:
                s_a = src_new
            else:
                s_b = src_new
            refs[ref_idx] = ref_new

    require(
        s_a == p_a + (0, 1)
        and s_b == p_b + (0, 1)
        and refs == [REF_YA + (0, 0), REF_YB + (0, 0), REF_YC + (0, 0)]
        and heads == [COLLECTOR_Z0, COLLECTOR_Z0]
        and eta == eta0,
        "prefix_full_reverse_restores_initial_state",
    )

    return {
        "final_heads": final_heads,
        "leaf_count": leaf_count,
        "contact_leaves": contact_leaves,
        "csum_leaves": csum_leaves,
        "block_checks": block_checks,
        "second_source_head0_checks": second_source_head0_checks,
    }


def check_all_50_prefixes() -> Dict[str, object]:
    codes_m = (3, 4, 0, 1, 2)
    total_prefixes = 0
    total_block_checks = 0
    for k_a, k_b in product(range(5), repeat=2):
        p_a, p_b = ROOT_PISTONS[k_a], ROOT_PISTONS[k_b]
        m_a, m_b = codes_m[k_a], codes_m[k_b]
        exp_ha = (1, 0, 0, 1, (3 * m_a) % 5, m_a)
        exp_hb = (1, 0, 0, 1, (3 * m_b) % 5, m_b)
        for eta0 in BITS:
            res = run_three_ref_prefix_on_joined(p_a, p_b, eta0, omit_w=False)
            require(res["leaf_count"] == 182, "prefix_182_leaves", res["leaf_count"])
            require(res["contact_leaves"] == 168 and res["csum_leaves"] == 14, "prefix_leaf_split")
            require(res["final_heads"] == (exp_ha, exp_hb), "prefix_collector_endpoints", (k_a, k_b, eta0))
            total_prefixes += 1
            total_block_checks += int(res["block_checks"])

    require(total_prefixes == 50 and total_block_checks == 300, "prefix_50_and_300_counts")

    # W-deleted controls for all 25 pairs + outside-family zero-piston pair
    exp_m2_head = (1, 0, 0, 1, 1, 2)
    for k_a, k_b in product(range(5), repeat=2):
        ctrl = run_three_ref_prefix_on_joined(ROOT_PISTONS[k_a], ROOT_PISTONS[k_b], 0, omit_w=True)
        require(
            ctrl["final_heads"] == (exp_m2_head, exp_m2_head),
            "w_deleted_prefix_collapses_to_m2",
            (k_a, k_b, ctrl["final_heads"]),
        )
    zero_res = run_three_ref_prefix_on_joined((0, 0, 0, 0), (0, 0, 0, 0), 0, omit_w=False)
    require(
        zero_res["final_heads"] == (exp_m2_head, exp_m2_head),
        "zero_piston_pair_collapses_to_m2",
        zero_res["final_heads"],
    )

    return {
        "prefixes_audited": total_prefixes,
        "block_boundaries_audited": total_block_checks,
        "w_deleted_controls": 25,
    }


# ---------------------------------------------------------------------------
# 4. Independent 705-site lattice wave/tape engine and response matrices
# ---------------------------------------------------------------------------

class IndependentWaveApparatus:
    def __init__(self) -> None:
        b_st: List[Tuple[int, int, int]] = []
        stencil: Dict[Tuple[int, int, int], Fraction] = {}
        for x1 in range(-4, 5):
            for x2 in range(-4, 5):
                for x3 in range(-4, 5):
                    if (x1 + x2 + x3) % 2 != 0:
                        continue
                    nsq = x1 * x1 + x2 * x2 + x3 * x3
                    if nsq in SHELL_WEIGHTS:
                        d = (x1, x2, x3)
                        b_st.append(d)
                        stencil[d] = Fraction(SHELL_WEIGHTS[nsq], STENCIL_DENOM)
        require(len(b_st) == 60, "b_st_len_60", len(b_st))
        b_zero = tuple(sorted(b_st + [(0, 0, 0)]))
        y1 = {(y[0] + b[0], y[1] + b[1], y[2] + b[2]) for y in Y_SITES for b in b_zero}
        b2 = {(a[0] + b[0], a[1] + b[1], a[2] + b[2]) for a in b_zero for b in b_zero}
        dom = tuple(sorted({(u[0] + b[0], u[1] + b[1], u[2] + b[2]) for u in y1 for b in b_zero}))
        require(len(y1) == 142 and len(b2) == 489 and len(dom) == 705, "lattice_shell_sizes")

        # Verify against DOMAIN.tsv
        raw = DOMAIN_TSV.read_bytes()
        require(
            len(raw) == 5029
            and hashlib.sha256(raw).hexdigest()
            == "2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0",
            "domain_tsv_custody",
        )
        tsv_pts = tuple(
            tuple(int(x) for x in line.split("\t"))
            for line in raw.decode("ascii").splitlines()[1:]
        )
        require(dom == tsv_pts, "constructed_domain_matches_tsv")

        self.dom = dom
        self.n_sites = 705
        self.site_idx = {pt: i for i, pt in enumerate(dom)}
        self.port_idx = tuple(self.site_idx[pt] for pt in Y_SITES[:4])
        self.y4_idx = self.site_idx[Y_SITES[4]]

        nbrs_all: List[Tuple[Tuple[int, Fraction], ...]] = []
        for pt in dom:
            row: List[Tuple[int, Fraction]] = []
            for d, coeff in stencil.items():
                nb = (pt[0] - d[0], pt[1] - d[1], pt[2] - d[2])
                j = self.site_idx.get(nb)
                if j is not None:
                    row.append((j, coeff))
            nbrs_all.append(tuple(row))
        self.h_nbrs = tuple(nbrs_all)

        # Derive response matrices R0, R0_inv, R1, D2, D3 and check closed form
        self.R0, self.R0_inv, self.R1, self.D2, self.D3, self.PHS = self._derive_matrices()

    def apply_H(self, u: Sequence[Fraction]) -> Tuple[Fraction, ...]:
        out = [Fraction(0, 1)] * self.n_sites
        for i, ui in enumerate(u):
            if ui != 0:
                out[i] += DIAG_H * ui
                for j, coeff in self.h_nbrs[i]:
                    out[j] += coeff * ui
        return tuple(out)

    def apply_P(self, z: Sequence[Fraction]) -> Tuple[Fraction, ...]:
        out = [Fraction(0, 1)] * self.n_sites
        for j, idx in enumerate(self.port_idx):
            out[idx] = z[j]
        return tuple(out)

    def apply_PT(self, u: Sequence[Fraction]) -> Tuple[Fraction, ...]:
        return tuple(u[idx] for idx in self.port_idx)

    def apply_J0(self, u: Sequence[Fraction]) -> Tuple[Fraction, ...]:
        out = list(u)
        for idx in self.port_idx:
            out[idx] = Fraction(0, 1)
        return tuple(out)

    def apply_K(self, u: Sequence[Fraction]) -> Tuple[Fraction, ...]:
        out = list(u)
        half = Fraction(1, 2)
        for idx in self.port_idx:
            out[idx] = out[idx] * half
        return tuple(out)

    def apply_S(self, z: Sequence[Fraction]) -> Tuple[Fraction, ...]:
        s5 = (z[0] + z[1] + z[2] + z[3]) * Fraction(1, 5)
        out = [Fraction(0, 1)] * self.n_sites
        for j, idx in enumerate(self.port_idx):
            out[idx] = z[j] - s5
        out[self.y4_idx] = -s5
        return tuple(out)

    @staticmethod
    def eta_lift(rec: Tuple[int, int]) -> Tuple[Fraction, Fraction, Fraction, Fraction]:
        q, r = rec
        return (
            Fraction(ELL[q], 2),
            Fraction(ELL[r] + 1, 2),
            Fraction(0, 1),
            Fraction(0, 1),
        )

    @staticmethod
    def dot(a: Sequence[Fraction], b: Sequence[Fraction]) -> Fraction:
        total = Fraction(0, 1)
        for x, y in zip(a, b):
            if x != 0 and y != 0:
                total += x * y
        return total

    def wave_energy(self, u: Sequence[Fraction], v: Sequence[Fraction]) -> Fraction:
        hv = self.apply_H(v)
        return Fraction(1, 2) * (self.dot(u, u) + self.dot(v, v) - self.dot(u, hv))

    def full_energy(self, X: Dict[str, object]) -> Fraction:
        u: Tuple[Fraction, ...] = X["u"]  # type: ignore[assignment]
        v: Tuple[Fraction, ...] = X["v"]  # type: ignore[assignment]
        a0: Tuple[Fraction, ...] = X["A0"]  # type: ignore[assignment]
        a1: Tuple[Fraction, ...] = X["A1"]  # type: ignore[assignment]
        b0: Tuple[Fraction, ...] = X["B0"]  # type: ignore[assignment]
        b1: Tuple[Fraction, ...] = X["B1"]  # type: ignore[assignment]
        tape_sq = self.dot(a0, a0) + self.dot(a1, a1) + self.dot(b0, b0) + self.dot(b1, b1)
        return self.wave_energy(u, v) + 2 * tape_sq

    def cold_X(self) -> Dict[str, object]:
        z_w = (Fraction(0, 1),) * self.n_sites
        z_t = (Fraction(0, 1),) * 4
        return {"u": z_w, "v": z_w, "A0": z_t, "A1": z_t, "B0": z_t, "B1": z_t, "k": 0}

    def F_step(self, X: Dict[str, object]) -> Dict[str, object]:
        u: Tuple[Fraction, ...] = X["u"]  # type: ignore[assignment]
        v: Tuple[Fraction, ...] = X["v"]  # type: ignore[assignment]
        a0: Tuple[Fraction, ...] = X["A0"]  # type: ignore[assignment]
        a1: Tuple[Fraction, ...] = X["A1"]  # type: ignore[assignment]
        b0: Tuple[Fraction, ...] = X["B0"]  # type: ignore[assignment]
        b1: Tuple[Fraction, ...] = X["B1"]  # type: ignore[assignment]
        k: int = X["k"]  # type: ignore[assignment]

        hv = self.apply_H(v)
        j0u = self.apply_J0(u)
        pa0 = self.apply_P(a0)
        rhs = tuple(hv[i] - j0u[i] + 4 * pa0[i] for i in range(self.n_sites))
        w_next = self.apply_K(rhs)
        pt_diff = self.apply_PT(tuple(w_next[i] - u[i] for i in range(self.n_sites)))
        b_out = tuple(a0[j] - Fraction(1, 2) * pt_diff[j] for j in range(4))
        return {
            "u": v,
            "v": w_next,
            "A0": a1,
            "A1": b1,
            "B0": b_out,
            "B1": b0,
            "k": (k + 1) % 2,
        }

    @staticmethod
    def _invert_4x4(mat: Tuple[Tuple[Fraction, ...], ...]) -> Tuple[Tuple[Fraction, ...], ...]:
        aug = [
            [mat[r][c] for c in range(4)] + [Fraction(1 if r == c else 0, 1) for c in range(4)]
            for r in range(4)
        ]
        for col in range(4):
            piv = next((r for r in range(col, 4) if aug[r][col] != 0), None)
            require(piv is not None, "matrix_4x4_nonsingular")
            assert piv is not None
            aug[col], aug[piv] = aug[piv], aug[col]
            pv = aug[col][col]
            for j in range(8):
                aug[col][j] /= pv
            for r in range(4):
                if r != col and aug[r][col] != 0:
                    fac = aug[r][col]
                    for j in range(8):
                        aug[r][j] -= fac * aug[col][j]
        return tuple(tuple(aug[r][4 + c] for c in range(4)) for r in range(4))

    @staticmethod
    def mat_vec_4(
        mat: Tuple[Tuple[Fraction, ...], ...], vec: Sequence[Fraction]
    ) -> Tuple[Fraction, Fraction, Fraction, Fraction]:
        return tuple(  # type: ignore[return-value]
            sum((mat[r][c] * vec[c] for c in range(4)), Fraction(0, 1)) for r in range(4)
        )

    def _derive_matrices(
        self,
    ) -> Tuple[
        Tuple[Tuple[Fraction, ...], ...],
        Tuple[Tuple[Fraction, ...], ...],
        Tuple[Tuple[Fraction, ...], ...],
        Tuple[Tuple[Fraction, ...], ...],
        Tuple[Tuple[Fraction, ...], ...],
        Tuple[Tuple[Fraction, ...], ...],
    ]:
        r0_cols, r1_cols, d2_cols, d3_cols, phs_cols = [], [], [], [], []
        z_w = (Fraction(0, 1),) * self.n_sites
        z_t = (Fraction(0, 1),) * 4
        for j in range(4):
            ej = tuple(Fraction(1 if i == j else 0, 1) for i in range(4))
            s_ej = self.apply_S(ej)
            phs_cols.append(self.apply_PT(self.apply_H(s_ej)))
            x0: Dict[str, object] = {
                "u": z_w, "v": s_ej, "A0": z_t, "A1": z_t, "B0": z_t, "B1": z_t, "k": 0
            }
            x1 = self.F_step(x0)
            x2 = self.F_step(x1)
            x3 = self.F_step(x2)
            x4 = self.F_step(x3)
            r0_cols.append(x4["A0"])
            r1_cols.append(x4["A1"])
            d2_cols.append(x4["B1"])
            d3_cols.append(x4["B0"])

        def tr(cols: List[ object]) -> Tuple[Tuple[Fraction, ...], ...]:
            return tuple(tuple(cols[c][r] for c in range(4)) for r in range(4))  # type: ignore[index]

        r0 = tr(r0_cols)
        phs = tr(phs_cols)
        # Closed-form check: R0 == -(1/4) P^T H S
        for r in range(4):
            for c in range(4):
                require(r0[r][c] == -Fraction(1, 4) * phs[r][c], "r0_closed_form_phs", (r, c))
        return r0, self._invert_4x4(r0), tr(r1_cols), tr(d2_cols), tr(d3_cols), phs

    def run_coupled_steps(
        self,
        x_a0: Tuple[int, int, int, int, int, int],
        x_b0: Tuple[int, int, int, int, int, int],
        cap_b: Fraction,
        *,
        steps: int = 7,
    ) -> List[Dict[str, object]]:
        state: Dict[str, object] = {
            "n": 0,
            "c": 0,
            "x_A": x_a0,
            "x_B": x_b0,
            "X": self.cold_X(),
            "W": Fraction(0, 1),
            "b": cap_b,
            "B": cap_b,
            "sigma_A": 1,
            "sigma_B": 1,
            "d": (0, 0),
        }
        boundaries = [state]
        cur = state
        for _ in range(steps):
            c: int = cur["c"]  # type: ignore[assignment]
            n: int = cur["n"]  # type: ignore[assignment]
            xa: Tuple[int, int, int, int, int, int] = cur["x_A"]  # type: ignore[assignment]
            xb: Tuple[int, int, int, int, int, int] = cur["x_B"]  # type: ignore[assignment]
            X: Dict[str, object] = cur["X"]  # type: ignore[assignment]
            W: Fraction = cur["W"]  # type: ignore[assignment]
            b: Fraction = cur["b"]  # type: ignore[assignment]
            B_cap: Fraction = cur["B"]  # type: ignore[assignment]
            sig_a: int = cur["sigma_A"]  # type: ignore[assignment]
            sig_b: int = cur["sigma_B"]  # type: ignore[assignment]
            d_rec: Tuple[int, int] = cur["d"]  # type: ignore[assignment]

            if c == 0:
                _, xa1 = native_u_step(n, xa)
                _, xb1 = native_u_step(n, xb)
                nxt = {
                    "n": n + 1, "c": 1, "x_A": xa1, "x_B": xb1,
                    "X": X, "W": W, "b": b, "B": B_cap,
                    "sigma_A": sig_a, "sigma_B": sig_b, "d": d_rec,
                }
            elif c == 1:
                new_d = ((d_rec[0] + xb[4]) % 5, (d_rec[1] + xb[5]) % 5)
                a_vec = self.apply_S(self.eta_lift((xa[4], xa[5])))
                u_cur: Tuple[Fraction, ...] = X["u"]  # type: ignore[assignment]
                v_cur: Tuple[Fraction, ...] = X["v"]  # type: ignore[assignment]
                v_cand = tuple(v_cur[i] + sig_a * a_vec[i] for i in range(self.n_sites))
                delta_e = self.wave_energy(u_cur, v_cand) - self.wave_energy(u_cur, v_cur)
                b_cand = b - delta_e
                if 0 <= b_cand <= B_cap:
                    new_X = dict(X)
                    new_X["v"] = v_cand
                    nxt = {
                        "n": n, "c": 2, "x_A": xa, "x_B": xb,
                        "X": new_X, "W": W + delta_e, "b": b_cand, "B": B_cap,
                        "sigma_A": -sig_a, "sigma_B": sig_b, "d": new_d,
                    }
                else:
                    nxt = {
                        "n": n, "c": 2, "x_A": xa, "x_B": xb,
                        "X": X, "W": W, "b": b, "B": B_cap,
                        "sigma_A": sig_a, "sigma_B": sig_b, "d": new_d,
                    }
            elif c in (2, 3, 5, 6):
                _, xa1 = native_u_step(n, xa)
                _, xb1 = native_u_step(n, xb)
                nxt = {
                    "n": n + 1, "c": (c + 1) % 8, "x_A": xa1, "x_B": xb1,
                    "X": self.F_step(X), "W": W, "b": b, "B": B_cap,
                    "sigma_A": sig_a, "sigma_B": sig_b, "d": d_rec,
                }
            elif c == 4:
                a_vec = self.apply_S(self.eta_lift(d_rec))
                u_cur = X["u"]  # type: ignore[assignment]
                v_cur = X["v"]  # type: ignore[assignment]
                v_cand = tuple(v_cur[i] + sig_b * a_vec[i] for i in range(self.n_sites))
                delta_e = self.wave_energy(u_cur, v_cand) - self.wave_energy(u_cur, v_cur)
                b_cand = b - delta_e
                if 0 <= b_cand <= B_cap:
                    new_X = dict(X)
                    new_X["v"] = v_cand
                    nxt = {
                        "n": n, "c": 5, "x_A": xa, "x_B": xb,
                        "X": new_X, "W": W + delta_e, "b": b_cand, "B": B_cap,
                        "sigma_A": sig_a, "sigma_B": -sig_b, "d": d_rec,
                    }
                else:
                    nxt = {
                        "n": n, "c": 5, "x_A": xa, "x_B": xb,
                        "X": X, "W": W, "b": b, "B": B_cap,
                        "sigma_A": sig_a, "sigma_B": sig_b, "d": d_rec,
                    }
            else:
                nxt = {
                    "n": n, "c": 0, "x_A": xa, "x_B": xb,
                    "X": X, "W": W, "b": b, "B": B_cap,
                    "sigma_A": sig_a, "sigma_B": sig_b, "d": d_rec,
                }
            cur = nxt
            boundaries.append(cur)
        return boundaries

    @staticmethod
    def receiver_projection_Y(state: Dict[str, object]) -> Tuple[object, ...]:
        X: Dict[str, object] = state["X"]  # type: ignore[assignment]
        return (
            state["n"],
            state["c"],
            X["u"],
            X["v"],
            X["A0"],
            X["A1"],
            X["B0"],
            X["B1"],
            X["k"],
            state["W"],
            state["b"],
            state["B"],
            state["sigma_A"],
            state["sigma_B"],
            state["d"],
        )

    def decode_port_no_d(
        self,
        b0: Sequence[Fraction],
        b2: Sequence[Fraction],
        sigma_A: int,
        sigma_B: int,
    ) -> Tuple[Tuple[Fraction, Fraction, Fraction, Fraction], Tuple[Fraction, Fraction, Fraction, Fraction]]:
        """Restricted port decoder using ONLY (b0, b2, sigma_A, sigma_B) with d omitted (d=None)."""
        require(sigma_A == -1 and sigma_B == -1, "both_contacts_accepted_sigma_minus1")
        z_a = self.mat_vec_4(self.R0_inv, b0)
        d2_za = self.mat_vec_4(self.D2, z_a)
        res_b2 = tuple(b2[j] - d2_za[j] for j in range(4))
        z_b = self.mat_vec_4(self.R0_inv, res_b2)
        return z_a, z_b


def check_all_relays(app: IndependentWaveApparatus) -> Dict[str, object]:
    expected_clocks = ((0, 0), (1, 1), (1, 2), (2, 3), (3, 4), (3, 5), (4, 6), (5, 7))

    # 1. Cold kick energies for M=0..4
    exp_rec_m = ((1, 0), (2, 4), (1, 2), (3, 3), (4, 2))
    exp_vec_m = (
        (Fraction(1, 2), Fraction(1, 2), Fraction(0, 1), Fraction(0, 1)),
        (Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1)),
        (Fraction(1, 2), Fraction(3, 2), Fraction(0, 1), Fraction(0, 1)),
        (Fraction(-1, 1), Fraction(-1, 2), Fraction(0, 1), Fraction(0, 1)),
        (Fraction(-1, 2), Fraction(3, 2), Fraction(0, 1), Fraction(0, 1)),
    )
    exp_cold_e = (
        Fraction(3, 20),
        Fraction(2, 5),
        Fraction(17, 20),
        Fraction(2, 5),
        Fraction(23, 20),
    )
    vec_to_m: Dict[Tuple[Fraction, Fraction, Fraction, Fraction], int] = {}
    for m in range(5):
        head_m = (1, 0, 0, 1, (3 * m) % 5, m)
        _, head_m1 = native_u_step(0, head_m)
        rec_1 = (head_m1[4], head_m1[5])
        require(rec_1 == exp_rec_m[m], "collector_step1_receiver", (m, rec_1))
        z_m = app.eta_lift(rec_1)
        require(z_m == exp_vec_m[m], "collector_step1_vector", (m, z_m))
        s_zm = app.apply_S(z_m)
        e_m = Fraction(1, 2) * app.dot(s_zm, s_zm)
        require(e_m == exp_cold_e[m], "collector_cold_kick_energy", (m, e_m))
        vec_to_m[z_m] = m

    # 2. #1577 unchanged-port blindness audit (4 pairs in {P1, P4}^2 + 1 control + rollover)
    cap_1577 = Fraction(4, 5)
    trajs_1577 = []
    for p_a, p_b in product((ROOT_PISTONS[1], ROOT_PISTONS[4]), repeat=2):
        bnds = app.run_coupled_steps(p_a + (0, 1), p_b + (0, 1), cap_1577, steps=8)
        require(len(bnds) == 9, "len_bnds_1577_with_rollover")
        for idx in range(8):
            require(
                (bnds[idx]["n"], bnds[idx]["c"]) == expected_clocks[idx],
                "clock_schedule_1577",
            )
            require(
                app.full_energy(bnds[idx]["X"]) == bnds[idx]["W"]  # type: ignore[arg-type]
                and bnds[idx]["b"] + bnds[idx]["W"] == cap_1577,
                "energy_account_1577",
            )
        # Check rollover step 8 (c: 7 -> 0, n stays 5, no renewal)
        require((bnds[8]["n"], bnds[8]["c"]) == (5, 0), "rollover_clock_5_0")
        require(
            bnds[8]["W"] == bnds[7]["W"]
            and bnds[8]["b"] == bnds[7]["b"]
            and bnds[8]["X"] == bnds[7]["X"]
            and bnds[8]["sigma_A"] == -1
            and bnds[8]["sigma_B"] == -1,
            "rollover_no_renewal_1577",
        )
        trajs_1577.append(bnds)

    # All 4 trajectories have identical receiver projection Y at all 9 boundaries, but distinct native heads
    ref_y_hist = [app.receiver_projection_Y(b) for b in trajs_1577[0]]
    for t_idx in range(1, 4):
        require(
            [app.receiver_projection_Y(b) for b in trajs_1577[t_idx]] == ref_y_hist,
            "unchanged_port_identical_receiver_Y",
            t_idx,
        )
        for b_idx in range(9):
            require(
                (trajs_1577[t_idx][b_idx]["x_A"], trajs_1577[t_idx][b_idx]["x_B"])
                != (trajs_1577[0][b_idx]["x_A"], trajs_1577[0][b_idx]["x_B"]),
                "unchanged_port_distinct_native_heads",
            )

    # Control trajectory for #1577: p_A = P1, p_B = (2,0,0,0)
    ctrl_1577 = app.run_coupled_steps(ROOT_PISTONS[1] + (0, 1), (2, 0, 0, 0, 0, 1), cap_1577, steps=7)
    ref_1577 = trajs_1577[0][:8]
    require(
        app.receiver_projection_Y(ctrl_1577[0]) == app.receiver_projection_Y(ref_1577[0])
        and app.receiver_projection_Y(ctrl_1577[1]) == app.receiver_projection_Y(ref_1577[1]),
        "ctrl_1577_agrees_through_b1",
    )
    require(ctrl_1577[2]["d"] != ref_1577[2]["d"], "ctrl_1577_d_differs_at_b2")
    for b_idx in range(5):
        require(ctrl_1577[b_idx]["X"] == ref_1577[b_idx]["X"], "ctrl_1577_wave_agrees_through_b4")
    require(ctrl_1577[5]["X"] != ref_1577[5]["X"], "ctrl_1577_wave_differs_at_b5")
    require(
        ctrl_1577[7]["X"]["A0"] == ref_1577[7]["X"]["A0"]  # type: ignore[index]
        and ctrl_1577[7]["X"]["A1"] == ref_1577[7]["X"]["A1"],  # type: ignore[index]
        "ctrl_1577_first_cuts_preserved",
    )
    dec_1577_ref = app.decode_port_no_d(
        ref_1577[7]["X"]["A0"], ref_1577[7]["X"]["B1"], -1, -1  # type: ignore[index]
    )
    dec_1577_ctrl = app.decode_port_no_d(
        ctrl_1577[7]["X"]["A0"], ctrl_1577[7]["X"]["B1"], -1, -1  # type: ignore[index]
    )
    require(
        dec_1577_ref[0] == dec_1577_ctrl[0] and dec_1577_ref[1] != dec_1577_ctrl[1],
        "ctrl_1577_decodes_distinct_second_source",
    )

    # 3. #1579 single-reference declared contact audit (4 pairs in {P1, P4}^2 at B=2 + W-deleted control)
    cap_1579 = Fraction(2, 1)
    records_1579 = set()
    bnds_by_pair_1579: Dict[Tuple[int, int], List[Dict[str, object]]] = {}
    max_w_1579 = Fraction(0, 1)
    for k_a in (1, 4):
        for k_b in (1, 4):
            cx_a, cy_a, eta_a = run_contact_word(ROOT_PISTONS[k_a] + (0, 1), I2_PISTON + (0, 0), 0, AY_WORD)
            cx_b, cy_b, eta_b = run_contact_word(ROOT_PISTONS[k_b] + (0, 1), I2_PISTON + (0, 0), 0, AY_WORD)
            require(
                cx_a == ROOT_PISTONS[k_a] + (0, 1)
                and cx_b == ROOT_PISTONS[k_b] + (0, 1)
                and eta_a == 0
                and eta_b == 0,
                "prefix_1579_restores_sources_and_bits",
            )
            bnds = app.run_coupled_steps(cy_a, cy_b, cap_1579, steps=7)
            for idx in range(8):
                require(
                    (bnds[idx]["n"], bnds[idx]["c"]) == expected_clocks[idx],
                    "clock_schedule_1579",
                )
                w_cur: Fraction = bnds[idx]["W"]  # type: ignore[assignment]
                require(
                    app.full_energy(bnds[idx]["X"]) == w_cur  # type: ignore[arg-type]
                    and bnds[idx]["b"] + w_cur == cap_1579
                    and w_cur <= Fraction(8, 5),
                    "energy_account_1579",
                )
                if w_cur > max_w_1579:
                    max_w_1579 = w_cur
            fin_x: Dict[str, object] = bnds[7]["X"]  # type: ignore[assignment]
            b0_vec: Tuple[Fraction, ...] = fin_x["A0"]  # type: ignore[assignment]
            b2_vec: Tuple[Fraction, ...] = fin_x["B1"]  # type: ignore[assignment]
            records_1579.add((b0_vec, b2_vec))
            za_dec, zb_dec = app.decode_port_no_d(b0_vec, b2_vec, -1, -1)
            exp_za = exp_vec_m[1 if k_a == 1 else 0]
            exp_zb = exp_vec_m[1 if k_b == 1 else 0]
            require((za_dec, zb_dec) == (exp_za, exp_zb), "decode_1579_exact", (k_a, k_b))
            bnds_by_pair_1579[(k_a, k_b)] = bnds

    require(len(records_1579) == 4, "four_distinct_records_1579")
    for k_a in (1, 4):
        b_p = bnds_by_pair_1579[(k_a, 1)]
        b_m = bnds_by_pair_1579[(k_a, 4)]
        for idx in range(5):
            require(b_p[idx]["X"] == b_m[idx]["X"], "wave_agrees_through_b4_1579", (k_a, idx))
        require(b_p[5]["X"] != b_m[5]["X"], "wave_differs_at_b5_1579", k_a)
        require(
            b_p[7]["X"]["A0"] == b_m[7]["X"]["A0"]  # type: ignore[index]
            and b_p[7]["X"]["A1"] == b_m[7]["X"]["A1"],  # type: ignore[index]
            "first_cuts_equal_1579",
            k_a,
        )

    # W-deleted control in #1579
    ay_no_w = tuple(op for op in AY_WORD if op != "W")
    for k_a, k_b in product((1, 4), repeat=2):
        _, cy_a_nw, _ = run_contact_word(ROOT_PISTONS[k_a] + (0, 1), I2_PISTON + (0, 0), 0, ay_no_w)
        _, cy_b_nw, _ = run_contact_word(ROOT_PISTONS[k_b] + (0, 1), I2_PISTON + (0, 0), 0, ay_no_w)
        require(
            cy_a_nw == (1, 0, 0, 1, 3, 1) and cy_b_nw == (1, 0, 0, 1, 3, 1),
            "w_deleted_1579_collapses_to_pp",
        )

    # 4. #1581 three-reference 25-pair relay audit at B=5 (200 boundaries)
    cap_1581 = Fraction(5, 1)
    codes_m = (3, 4, 0, 1, 2)
    records_25 = set()
    first_records_5 = set()
    bnds_by_pair_1581: Dict[Tuple[int, int], List[Dict[str, object]]] = {}
    max_w_1581 = Fraction(0, 1)
    relay_boundaries_count = 0

    for k_a, k_b in product(range(5), repeat=2):
        pref = run_three_ref_prefix_on_joined(ROOT_PISTONS[k_a], ROOT_PISTONS[k_b], 0, omit_w=False)
        ha, hb = pref["final_heads"]  # type: ignore[misc]
        bnds = app.run_coupled_steps(ha, hb, cap_1581, steps=7)
        require(len(bnds) == 8, "eight_boundaries_1581")
        for idx in range(8):
            relay_boundaries_count += 1
            require(
                (bnds[idx]["n"], bnds[idx]["c"]) == expected_clocks[idx],
                "clock_schedule_1581",
            )
            w_cur = bnds[idx]["W"]  # type: ignore[assignment]
            require(
                app.full_energy(bnds[idx]["X"]) == w_cur  # type: ignore[arg-type]
                and bnds[idx]["b"] + w_cur == cap_1581
                and w_cur <= Fraction(23, 5),
                "energy_account_1581",
            )
            if w_cur > max_w_1581:
                max_w_1581 = w_cur

        # Check cut persistence across boundaries 3 -> 4 -> 5 -> 6 -> 7
        cut0_b3 = bnds[3]["X"]["B0"]  # type: ignore[index]
        cut1_b4 = bnds[4]["X"]["B0"]  # type: ignore[index]
        require(
            bnds[4]["X"]["B1"] == cut0_b3  # type: ignore[index]
            and bnds[5]["X"]["B1"] == cut0_b3  # type: ignore[index]
            and bnds[6]["X"]["A1"] == cut0_b3  # type: ignore[index]
            and bnds[7]["X"]["A0"] == cut0_b3,  # type: ignore[index]
            "cut0_persists_through_second_contact",
        )
        require(
            bnds[5]["X"]["B0"] == cut1_b4  # type: ignore[index]
            and bnds[6]["X"]["B1"] == cut1_b4  # type: ignore[index]
            and bnds[7]["X"]["A1"] == cut1_b4,  # type: ignore[index]
            "cut1_persists_through_second_contact",
        )

        fin_x = bnds[7]["X"]  # type: ignore[assignment]
        b0_vec = fin_x["A0"]  # type: ignore[assignment]
        b1_vec = fin_x["A1"]  # type: ignore[assignment]
        b2_vec = fin_x["B1"]  # type: ignore[assignment]
        b3_vec = fin_x["B0"]  # type: ignore[assignment]
        records_25.add((b0_vec, b1_vec, b2_vec, b3_vec))
        first_records_5.add((b0_vec, b1_vec))

        za_dec, zb_dec = app.decode_port_no_d(b0_vec, b2_vec, -1, -1)
        m_a_dec = vec_to_m[za_dec]
        m_b_dec = vec_to_m[zb_dec]
        ka_dec = (m_a_dec + 2) % 5
        kb_dec = (m_b_dec + 2) % 5
        require(
            (m_a_dec, m_b_dec) == (codes_m[k_a], codes_m[k_b])
            and (ka_dec, kb_dec) == (k_a, k_b),
            "decode_25_pairs_exact_no_d",
            (k_a, k_b),
        )
        bnds_by_pair_1581[(k_a, k_b)] = bnds

    require(relay_boundaries_count == 200, "relay_boundaries_200", relay_boundaries_count)
    require(len(records_25) == 25 and len(first_records_5) == 5, "distinct_record_sets_25_and_5")

    # Check independence of first wave/tape history through boundary 4 and first cuts from second source
    for k_a in range(5):
        ref_bnds = bnds_by_pair_1581[(k_a, 0)]
        for k_b in range(1, 5):
            cmp_bnds = bnds_by_pair_1581[(k_a, k_b)]
            for idx in range(5):
                require(
                    cmp_bnds[idx]["X"] == ref_bnds[idx]["X"],
                    "first_wave_tape_independent_of_second_source_through_b4",
                    (k_a, k_b, idx),
                )
            require(
                cmp_bnds[5]["X"] != ref_bnds[5]["X"],
                "second_contact_changes_wave_at_b5",
                (k_a, k_b),
            )
            require(
                cmp_bnds[7]["X"]["A0"] == ref_bnds[7]["X"]["A0"]  # type: ignore[index]
                and cmp_bnds[7]["X"]["A1"] == ref_bnds[7]["X"]["A1"],  # type: ignore[index]
                "first_retained_cuts_independent_of_second_source",
                (k_a, k_b),
            )

    # Check downstream replay of W-deleted control matches (j^4, j^4) = (4, 4)
    ctrl_pref = run_three_ref_prefix_on_joined(ROOT_PISTONS[0], ROOT_PISTONS[1], 0, omit_w=True)
    ctrl_ha, ctrl_hb = ctrl_pref["final_heads"]  # type: ignore[misc]
    ctrl_bnds = app.run_coupled_steps(ctrl_ha, ctrl_hb, cap_1581, steps=7)
    require(
        ctrl_bnds[7] == bnds_by_pair_1581[(4, 4)][7],
        "w_deleted_downstream_matches_j4_j4",
    )

    return {
        "relay_boundaries_1581": relay_boundaries_count,
        "distinct_record_sets_1581": len(records_25),
        "distinct_first_records_1581": len(first_records_5),
        "max_work_1579": f"{max_w_1579.numerator}/{max_w_1579.denominator}",
        "max_work_1581": f"{max_w_1581.numerator}/{max_w_1581.denominator}",
    }


def main() -> None:
    custody = check_sources_custody()
    env_res = check_cyclotomic_and_quotient_envelope()
    census_res = check_reference_census_and_code()
    contact_res = check_contact_inventories()
    prefix_res = check_all_50_prefixes()
    app = IndependentWaveApparatus()
    relay_res = check_all_relays(app)

    summary = {
        "status": "PASS",
        "candidate": "C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N",
        "custody": custody,
        "quotient_envelope": env_res,
        "reference_census": census_res,
        "contact_inventories": contact_res,
        "prefixes": prefix_res,
        "relays": relay_res,
    }
    print("PASS C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N: independent phase-chain and resource-boundary audit")
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
