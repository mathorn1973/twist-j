#!/usr/bin/env python3
"""Independent adversarial audit of the nonlinear two-message receiver on U.

Probe: P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-2
Issue: #1534
Author: A. M. Thorn <thorn@twistj.com>
License: Apache-2.0
"""

from __future__ import annotations

import hashlib
from itertools import product
from pathlib import Path
import sys


PROBE_ID = "P-U-NONLINEAR-RECEIVER-INDEPENDENT-AUDIT-2"
PROBE_DIR = Path(__file__).resolve().parent
F5 = (0, 1, 2, 3, 4)
ALL_STATES = tuple(product(F5, repeat=6))
ALL_PAIRS = tuple(product(F5, repeat=2))
INV5 = {1: 1, 2: 3, 3: 2, 4: 4}

STAGE_ORDER = (
    "custody",
    "generators_and_quotient",
    "nonlinear_chart_claim1",
    "prefix_claim2",
    "synchronized_invariants_claim3",
    "prepared_tail_and_regression_claim4",
    "access_boundary_and_quotient_claim5",
    "nonaffinity_and_minimality_claims6_7",
)

# Independently derived affine generator matrices g_k(x) = M_k x + t_k mod 5
GENERATOR_MATRICES = (
    (
        (0, 1, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0),
        (0, 0, 1, 0, 0, 0),
        (0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 1),
    ),
    (
        (0, 0, 4, 0, 0, 0),
        (0, 0, 0, 4, 0, 0),
        (4, 0, 0, 0, 0, 0),
        (0, 4, 0, 0, 0, 0),
        (0, 0, 0, 0, 4, 0),
        (0, 0, 0, 0, 0, 4),
    ),
    (
        (0, 0, 4, 0, 0, 0),
        (0, 0, 0, 4, 0, 1),
        (4, 0, 0, 0, 0, 0),
        (0, 4, 0, 0, 0, 4),
        (0, 0, 0, 0, 4, 0),
        (0, 0, 0, 0, 0, 4),
    ),
    (
        (4, 0, 0, 0, 0, 0),
        (0, 4, 0, 0, 0, 0),
        (0, 0, 4, 0, 0, 0),
        (0, 0, 0, 4, 0, 0),
        (0, 0, 0, 0, 4, 0),
        (0, 0, 0, 0, 0, 4),
    ),
    (
        (4, 0, 0, 0, 0, 0),
        (0, 4, 0, 0, 0, 0),
        (0, 0, 4, 0, 0, 0),
        (0, 0, 0, 4, 0, 0),
        (0, 0, 0, 0, 4, 0),
        (0, 0, 0, 0, 0, 4),
    ),
)

GENERATOR_SHIFTS = (
    (0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0),
    (2, 1, 2, 1, 1, 0),
    (2, 1, 3, 4, 1, 1),
    (2, 1, 3, 4, 2, 1),
)


class ExactAuditFailure(Exception):
    """Raised when a formal scientific audit assertion fails."""

    def __init__(self, stage: str, message: str) -> None:
        super().__init__(message)
        self.stage = stage
        self.message = message


def check(condition: bool, stage: str, message: str) -> None:
    if not condition:
        raise ExactAuditFailure(stage, message)


def validate_residue(value: object, label: str = "residue") -> int:
    if type(value) is not int or not (0 <= value < 5):
        raise ValueError(f"invalid {label}: {value!r}")
    return value


def validate_nonneg_int(value: object, label: str = "index") -> int:
    if type(value) is not int or value < 0:
        raise ValueError(f"invalid {label}: {value!r}")
    return value


def validate_tuple_len(
    vec: object, length: int, label: str = "vector"
) -> tuple[int, ...]:
    if not isinstance(vec, tuple) or len(vec) != length:
        raise ValueError(f"invalid {label} tuple length: {vec!r}")
    for idx, entry in enumerate(vec):
        validate_residue(entry, f"{label}[{idx}]")
    return vec


def validate_state(x: object, label: str = "state") -> tuple[int, ...]:
    return validate_tuple_len(x, 6, label)


def validate_receiver(r_pair: object, label: str = "receiver") -> tuple[int, ...]:
    return validate_tuple_len(r_pair, 2, label)


def z_trace(x: tuple[int, ...]) -> int:
    x = validate_state(x)
    return sum(x) % 5


def theta_bit(n: int) -> int:
    n = validate_nonneg_int(n, "n")
    return bin(n).count("1") & 1


def selector_index(z: int, theta: int) -> int:
    z = validate_residue(z, "z")
    if type(theta) is not int or theta not in (0, 1):
        raise ValueError(f"invalid theta: {theta!r}")
    return (z + 2 * theta) % 5


def g_tuple(k: int, x: tuple[int, ...]) -> tuple[int, ...]:
    k = validate_residue(k, "generator_index")
    a, b, c, d, q, r = validate_state(x)
    if k == 0:
        return (b, a, d, c, q, r)
    if k == 1:
        return ((-c) % 5, (-d) % 5, (-a) % 5, (-b) % 5, (-q) % 5, (-r) % 5)
    if k == 2:
        return (
            (2 - c) % 5,
            (1 - d + r) % 5,
            (2 - a) % 5,
            (1 - b - r) % 5,
            (1 - q) % 5,
            (-r) % 5,
        )
    if k == 3:
        return (
            (2 - a) % 5,
            (1 - b) % 5,
            (3 - c) % 5,
            (4 - d) % 5,
            (1 - q) % 5,
            (1 - r) % 5,
        )
    return (
        (2 - a) % 5,
        (1 - b) % 5,
        (3 - c) % 5,
        (4 - d) % 5,
        (2 - q) % 5,
        (1 - r) % 5,
    )


def g_matrix(k: int, x: tuple[int, ...]) -> tuple[int, ...]:
    k = validate_residue(k, "generator_index")
    x = validate_state(x)
    mat = GENERATOR_MATRICES[k]
    shift = GENERATOR_SHIFTS[k]
    return tuple(
        (sum(mat[row][col] * x[col] for col in range(6)) + shift[row]) % 5
        for row in range(6)
    )


def step_T(theta: int, x: tuple[int, ...]) -> tuple[int, ...]:
    x = validate_state(x)
    j = selector_index(z_trace(x), theta)
    return g_tuple(j, x)


def step_U(n: int, x: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    n = validate_nonneg_int(n, "n")
    x = validate_state(x)
    return (n + 1, step_T(theta_bit(n), x))


def psi_aff(x: tuple[int, ...]) -> tuple[int, ...]:
    a, b, c, d, q, r = validate_state(x)
    z = (a + b + c + d + q + r) % 5
    A = (a + c) % 5
    B = (b + d) % 5
    C = (a - c - 2) % 5
    D = (b - d - 1) % 5
    return (z, A, B, C, D, q)


def psi_aff_inv(w: tuple[int, ...]) -> tuple[int, ...]:
    z, A, B, C, D, q = validate_state(w, "affine_coords")
    a = (3 * (A + C + 2)) % 5
    c = (3 * (A - C - 2)) % 5
    b = (3 * (B + D + 1)) % 5
    d = (3 * (B - D - 1)) % 5
    r = (z - A - B - q) % 5
    return (a, b, c, d, q, r)


def g_affine_coords(k: int, w: tuple[int, ...]) -> tuple[int, ...]:
    k = validate_residue(k, "generator_index")
    z, A, B, C, D, q = validate_state(w, "affine_coords")
    r = (z - A - B - q) % 5
    if k == 0:
        return (z, B, A, (D - 1) % 5, (C + 1) % 5, q)
    if k == 1:
        return ((-z) % 5, (-A) % 5, (-B) % 5, C, D, (-q) % 5)
    if k == 2:
        return (
            (2 - z) % 5,
            (4 - A) % 5,
            (2 - B) % 5,
            C,
            (D + 2 * r) % 5,
            (1 - q) % 5,
        )
    if k == 3:
        return (
            (2 - z) % 5,
            (-A) % 5,
            (-B) % 5,
            (-C) % 5,
            (-D) % 5,
            (1 - q) % 5,
        )
    return (
        (3 - z) % 5,
        (-A) % 5,
        (-B) % 5,
        (-C) % 5,
        (-D) % 5,
        (2 - q) % 5,
    )


def pi_zqr(x: tuple[int, ...]) -> tuple[int, int, int]:
    x = validate_state(x)
    return (z_trace(x), x[4], x[5])


def g_zqr(k: int, zqr: tuple[int, int, int]) -> tuple[int, int, int]:
    k = validate_residue(k, "generator_index")
    z, q, r = validate_tuple_len(zqr, 3, "zqr")
    if k == 0:
        return (z, q, r)
    if k == 1:
        return ((-z) % 5, (-q) % 5, (-r) % 5)
    if k == 2:
        return ((2 - z) % 5, (1 - q) % 5, (-r) % 5)
    if k == 3:
        return ((2 - z) % 5, (1 - q) % 5, (1 - r) % 5)
    return ((3 - z) % 5, (2 - q) % 5, (1 - r) % 5)


def step_T_zqr(theta: int, zqr: tuple[int, int, int]) -> tuple[int, int, int]:
    z, q, r = validate_tuple_len(zqr, 3, "zqr")
    j = selector_index(z, theta)
    return g_zqr(j, (z, q, r))


def tau_val(z: int, A: int) -> int:
    z = validate_residue(z, "z")
    A = validate_residue(A, "A")
    return (z * pow(A, 3, 5) + 1 - pow(A, 4, 5)) % 5


def sigma_val(z: int, A: int) -> int:
    z = validate_residue(z, "z")
    A = validate_residue(A, "A")
    return (z * A + 1 - pow(A, 4, 5)) % 5


def lagrange_e(z: int, j: int) -> int:
    z = validate_residue(z, "z")
    j = validate_residue(j, "j")
    return (1 - pow((z - j) % 5, 4, 5)) % 5


def poly_T(x: tuple[int, ...]) -> int:
    z, A, B, C, D, q = psi_aff(x)
    e0, e1, e2, e3, e4 = (lagrange_e(z, j) for j in F5)
    tau = tau_val(z, A)
    return (e0 * C + e2 * q + (e1 + e4) * tau * D + e3 * D) % 5


def phi_sheet(x: tuple[int, ...]) -> tuple[int, ...]:
    z, A, B, C, D, q = psi_aff(x)
    if z == 0:
        return (z, C, A, B, D, q)
    if z == 2:
        return (z, q, A, B, C, D)
    if z in (1, 4):
        return (z, (tau_val(z, A) * D) % 5, A, B, C, q)
    return (z, D, A, B, C, q)


def phi_poly(x: tuple[int, ...]) -> tuple[int, ...]:
    z, A, B, C, D, q = psi_aff(x)
    e0 = lagrange_e(z, 0)
    e2 = lagrange_e(z, 2)
    y1 = poly_T(x)
    y4 = (e0 * D + (1 - e0) * C) % 5
    y5 = (e2 * D + (1 - e2) * q) % 5
    return (z, y1, A, B, y4, y5)


def phi_inv_sheet(y: tuple[int, ...]) -> tuple[int, ...]:
    y0, y1, y2, y3, y4, y5 = validate_state(y, "phi_coords")
    z, A, B = y0, y2, y3
    if z == 0:
        C, D, q = y1, y4, y5
    elif z == 2:
        q, C, D = y1, y4, y5
    elif z in (1, 4):
        C = y4
        D = (sigma_val(z, A) * y1) % 5
        q = y5
    else:
        D, C, q = y1, y4, y5
    return psi_aff_inv((z, A, B, C, D, q))


def phi_inv_poly(y: tuple[int, ...]) -> tuple[int, ...]:
    y0, y1, y2, y3, y4, y5 = validate_state(y, "phi_coords")
    z, A, B = y0, y2, y3
    e0, e1, e2, e3, e4 = (lagrange_e(z, j) for j in F5)
    C = (e0 * y1 + (1 - e0) * y4) % 5
    D = (
        e0 * y4
        + e2 * y5
        + (e1 + e4) * sigma_val(z, A) * y1
        + e3 * y1
    ) % 5
    q = (e2 * y1 + (1 - e2) * y5) % 5
    return psi_aff_inv((z, A, B, C, D, q))


def R_map(x: tuple[int, ...]) -> tuple[int, int]:
    y = phi_sheet(x)
    return (y[0], y[1])


def S_map(x: tuple[int, ...]) -> tuple[int, int, int, int]:
    y = phi_sheet(x)
    return (y[2], y[3], y[4], y[5])


def G_reader(r_pair: tuple[int, int]) -> str:
    z, t = validate_receiver(r_pair, "receiver")
    if z in (2, 3):
        return "BLANK"
    return f"PRESENT({t})"


def prep_E(lam: int, mu: int) -> tuple[int, ...]:
    lam = validate_residue(lam, "lambda")
    mu = validate_residue(mu, "mu")
    return (
        (3 * (lam + 3)) % 5,
        (3 * (mu + 1)) % 5,
        (3 * (-lam - 1)) % 5,
        (3 * (-mu - 1)) % 5,
        0,
        1,
    )


def x14_sign_rep(x: tuple[int, ...]) -> tuple[int, ...]:
    """Canonical sign-fibre representative {V(x), -V(x)} on X_14 (z in {1, 4})."""
    z, A, B, C, D, _ = psi_aff(x)
    check(z in (1, 4), "nonaffinity_and_minimality_claims6_7", f"not on X_14: {x}")
    v_pos = (A, B, (z * C) % 5, (z * D) % 5)
    v_neg = tuple((-coord) % 5 for coord in v_pos)
    return min(v_pos, v_neg)


def run_stage_custody() -> str:
    stage = "custody"
    manifest_path = PROBE_DIR / "INPUTS.sha256"
    sources_path = PROBE_DIR / "SOURCES.tsv"
    check(manifest_path.is_file(), stage, "missing INPUTS.sha256")
    check(sources_path.is_file(), stage, "missing SOURCES.tsv")

    expected_files = {
        "PREREG.md",
        "PROOF.md",
        "README.md",
        "SOURCES.tsv",
        "break.py",
        "verify.py",
    }
    seen_files: set[str] = set()
    lines = [
        line.strip()
        for line in manifest_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    for line in lines:
        parts = line.split()
        check(len(parts) == 2, stage, f"malformed INPUTS.sha256 line: {line!r}")
        digest, rel_name = parts
        check(rel_name not in seen_files, stage, f"duplicate entry {rel_name}")
        seen_files.add(rel_name)
        target = PROBE_DIR / rel_name
        check(target.is_file(), stage, f"missing pinned file {rel_name}")
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        check(
            actual == digest,
            stage,
            f"SHA-256 mismatch for {rel_name}: expected {digest}, got {actual}",
        )
    check(
        seen_files == expected_files,
        stage,
        f"INPUTS.sha256 file set {sorted(seen_files)} != {sorted(expected_files)}",
    )

    source_lines = sources_path.read_text(encoding="utf-8").splitlines()
    check(
        len(source_lines) >= 2 and source_lines[0] == "commit\tpath\tsha256\tbytes",
        stage,
        "invalid SOURCES.tsv header",
    )
    for row in source_lines[1:]:
        cols = row.split("\t")
        check(len(cols) == 4, stage, f"malformed SOURCES.tsv row: {row!r}")
        commit_sha, _, file_sha, byte_str = cols
        check(len(commit_sha) == 40, stage, f"bad commit SHA in SOURCES.tsv: {row!r}")
        check(len(file_sha) == 64, stage, f"bad file SHA in SOURCES.tsv: {row!r}")
        check(byte_str.isdigit() and int(byte_str) > 0, stage, f"bad bytes: {row!r}")

    return f"files={len(seen_files)} sources={len(source_lines) - 1}"


def run_stage_generators_and_quotient() -> str:
    stage = "generators_and_quotient"
    check(len(ALL_STATES) == 15625, stage, f"state count {len(ALL_STATES)} != 15625")

    gen_checks = 0
    inv_checks = 0
    aff_checks = 0
    trace_checks = 0
    quot_checks = 0
    for x in ALL_STATES:
        w = psi_aff(x)
        zqr = pi_zqr(x)
        for k in F5:
            gx_t = g_tuple(k, x)
            gx_m = g_matrix(k, x)
            check(
                gx_t == gx_m,
                stage,
                f"g_{k} tuple != matrix at x={x}: {gx_t} vs {gx_m}",
            )
            gen_checks += 1

            check(
                g_tuple(k, gx_t) == x,
                stage,
                f"g_{k} not involution at x={x}: got {g_tuple(k, gx_t)}",
            )
            inv_checks += 1

            gw = g_affine_coords(k, w)
            check(
                psi_aff(gx_t) == gw,
                stage,
                f"g_{k} affine coords mismatch at x={x}: {psi_aff(gx_t)} vs {gw}",
            )
            aff_checks += 1

            gzqr = g_zqr(k, zqr)
            check(
                z_trace(gx_t) == gzqr[0],
                stage,
                f"g_{k} trace mismatch at x={x}",
            )
            trace_checks += 1

            check(
                pi_zqr(gx_t) == gzqr,
                stage,
                f"g_{k} (z,q,r) quotient mismatch at x={x}: {pi_zqr(gx_t)} vs {gzqr}",
            )
            quot_checks += 1

    sel_checks = 0
    im_t0: set[int] = set()
    im_t1: set[int] = set()
    count_t0 = 0
    count_t1 = 0
    for x in ALL_STATES:
        zqr = pi_zqr(x)
        for theta in (0, 1):
            tx = step_T(theta, x)
            tzqr = step_T_zqr(theta, zqr)
            check(
                pi_zqr(tx) == tzqr,
                stage,
                f"T_{theta} quotient mismatch at x={x}",
            )
            if theta == 0:
                im_t0.add(z_trace(tx))
                if z_trace(x) in (0, 4):
                    count_t0 += 1
            else:
                im_t1.add(z_trace(tx))
                if z_trace(x) in (1, 2, 3):
                    count_t1 += 1
            sel_checks += 1

    check(im_t0 == {0, 4}, stage, f"im(tau_0) = {sorted(im_t0)} != [0, 4]")
    check(im_t1 == {1, 2, 3}, stage, f"im(tau_1) = {sorted(im_t1)} != [1, 2, 3]")
    check(
        (count_t0, count_t1) == (6250, 9375),
        stage,
        f"sheet image counts {(count_t0, count_t1)} != (6250, 9375)",
    )
    check(
        gen_checks == 78125
        and inv_checks == 78125
        and aff_checks == 78125
        and trace_checks == 78125
        and quot_checks == 78125
        and sel_checks == 31250,
        stage,
        "unexpected generator/selector check totals",
    )
    return (
        f"gen={gen_checks} inv={inv_checks} aff={aff_checks} "
        f"quot={quot_checks} sel={sel_checks}"
    )


def run_stage_nonlinear_chart_claim1() -> str:
    stage = "nonlinear_chart_claim1"
    aff_roundtrip = 0
    phi_roundtrip = 0
    poly_agree = 0
    sheet_counts = {z: 0 for z in F5}
    a0_total = 0
    a0_z14 = 0
    tau_inv_checks = 0
    fibre_counts = {r_val: 0 for r_val in ALL_PAIRS}

    seen_phi: set[tuple[int, ...]] = set()
    for x in ALL_STATES:
        w = psi_aff(x)
        check(psi_aff_inv(w) == x, stage, f"psi_aff_inv(psi_aff(x)) != x at {x}")
        check(psi_aff(psi_aff_inv(x)) == x, stage, f"psi_aff(psi_aff_inv(w)) != w at {x}")
        aff_roundtrip += 2

        ys = phi_sheet(x)
        yp = phi_poly(x)
        check(ys == yp, stage, f"phi_sheet != phi_poly at {x}: {ys} vs {yp}")
        check(ys[1] == poly_T(x), stage, f"Phi_1 != poly_T at {x}")
        poly_agree += 1

        x_back_s = phi_inv_sheet(ys)
        x_back_p = phi_inv_poly(ys)
        check(x_back_s == x, stage, f"phi_inv_sheet(phi(x)) != x at {x}")
        check(x_back_p == x, stage, f"phi_inv_poly(phi(x)) != x at {x}")

        y_back_s = phi_sheet(phi_inv_sheet(x))
        y_back_p = phi_poly(phi_inv_poly(x))
        check(y_back_s == x, stage, f"phi(phi_inv_sheet(y)) != y at {x}")
        check(y_back_p == x, stage, f"phi(phi_inv_poly(y)) != y at {x}")
        phi_roundtrip += 2

        seen_phi.add(ys)
        z, A = w[0], w[1]
        sheet_counts[z] += 1
        if A == 0:
            a0_total += 1
            check(tau_val(z, 0) == 1, stage, f"tau({z}, 0) != 1")
            if z in (1, 4):
                a0_z14 += 1
                check(
                    ys == (z, w[4], 0, w[2], w[3], w[5]),
                    stage,
                    f"unexpected Phi on z={z}, A=0 at {x}",
                )
        if z in (1, 4):
            t_val = tau_val(z, A)
            s_val = sigma_val(z, A)
            check(
                t_val != 0 and (t_val * s_val) % 5 == 1 and pow(t_val, 3, 5) == s_val,
                stage,
                f"tau/sigma inverse failure at z={z}, A={A}",
            )
            tau_inv_checks += 1

        r_val = R_map(x)
        s_val_tuple = S_map(x)
        check(
            (r_val[0], r_val[1], *s_val_tuple) == ys,
            stage,
            f"(R, S) != Phi at {x}",
        )
        fibre_counts[r_val] += 1

    check(len(seen_phi) == 15625, stage, f"|im(Phi)| = {len(seen_phi)} != 15625")
    check(
        all(cnt == 3125 for cnt in sheet_counts.values()),
        stage,
        f"sheet counts {sheet_counts} != 3125 each",
    )
    check(a0_total == 3125, stage, f"A=0 locus count {a0_total} != 3125")
    check(a0_z14 == 1250, stage, f"z in {{1,4}}, A=0 count {a0_z14} != 1250")
    check(tau_inv_checks == 6250, stage, f"tau_inv_checks {tau_inv_checks} != 6250")
    check(
        len(fibre_counts) == 25 and all(cnt == 625 for cnt in fibre_counts.values()),
        stage,
        f"receiver fibre counts not all 625: {fibre_counts}",
    )
    check(
        aff_roundtrip == 31250 and phi_roundtrip == 31250 and poly_agree == 15625,
        stage,
        "unexpected chart roundtrip counts",
    )
    return (
        f"aff_rt={aff_roundtrip} phi_rt={phi_roundtrip} poly={poly_agree} "
        f"fibres=25x625 a0_z14={a0_z14}"
    )


def run_stage_prefix_claim2() -> str:
    stage = "prefix_claim2"
    seen_initial_states: set[tuple[int, ...]] = set()
    seen_complements: set[tuple[int, int, int, int]] = set()

    for lam, mu in ALL_PAIRS:
        x0 = prep_E(lam, mu)
        seen_initial_states.add(x0)
        phi0 = phi_sheet(x0)
        check(
            phi0 == (2, 0, 1, 0, lam, mu),
            stage,
            f"Phi(E({lam},{mu})) = {phi0} != (2,0,1,0,{lam},{mu})",
        )
        check(R_map(x0) == (2, 0), stage, f"R(x0) != (2,0) for ({lam},{mu})")
        seen_complements.add(S_map(x0))

        j0 = selector_index(z_trace(x0), theta_bit(0))
        _, x1 = step_U(0, x0)
        j1 = selector_index(z_trace(x1), theta_bit(1))
        _, x2 = step_U(1, x1)
        j2 = selector_index(z_trace(x2), theta_bit(2))
        _, x3 = step_U(2, x2)

        selectors = (j0, j1, j2)
        traces = (z_trace(x0), z_trace(x1), z_trace(x2), z_trace(x3))
        r_trace = (R_map(x0), R_map(x1), R_map(x2), R_map(x3))
        g_trace = tuple(G_reader(r_item) for r_item in r_trace)

        check(
            selectors == (2, 2, 4),
            stage,
            f"selectors {selectors} != (2,2,4) for ({lam},{mu})",
        )
        check(
            traces == (2, 0, 2, 1),
            stage,
            f"traces {traces} != (2,0,2,1) for ({lam},{mu})",
        )
        check(x2 == x0, stage, f"x2 != x0 for ({lam},{mu}): {x2} vs {x0}")
        check((2, x2) != (0, x0), stage, "Omega state falsely reset")
        check(
            r_trace == ((2, 0), (0, lam), (2, 0), (1, mu)),
            stage,
            f"R trace {r_trace} mismatch for ({lam},{mu})",
        )
        check(
            g_trace == ("BLANK", f"PRESENT({lam})", "BLANK", f"PRESENT({mu})"),
            stage,
            f"G trace {g_trace} mismatch for ({lam},{mu})",
        )
        if lam == 0:
            check(
                g_trace[1] == "PRESENT(0)" and g_trace[1] != "BLANK",
                stage,
                "PRESENT(0) confused with BLANK at n=1",
            )
        if mu == 0:
            check(
                g_trace[3] == "PRESENT(0)" and g_trace[3] != "BLANK",
                stage,
                "PRESENT(0) confused with BLANK at n=3",
            )
        check(
            phi_sheet(x3) == (1, mu, 4, 0, (-lam) % 5, 2),
            stage,
            f"Phi(x3) = {phi_sheet(x3)} mismatch for ({lam},{mu})",
        )

    check(len(seen_initial_states) == 25, stage, "preparations not 25 distinct states")
    check(len(seen_complements) == 25, stage, "complements not 25 distinct tuples")
    return "pairs=25 selectors=(2,2,4) traces=(2,0,2,1) x2_eq_x0=25"


def run_stage_synchronized_invariants_claim3() -> str:
    stage = "synchronized_invariants_claim3"
    s5000 = [
        x
        for x in ALL_STATES
        if z_trace(x) in (1, 4) and psi_aff(x)[1] != 0
    ]
    check(len(s5000) == 5000, stage, f"|S_5000| = {len(s5000)} != 5000")
    s5000_set = set(s5000)

    edge_checks = 0
    fibre_counts = {pair: 0 for pair in ALL_PAIRS}
    for x in s5000:
        z, A, B, C, D, _ = psi_aff(x)
        inv_A = INV5[A]
        ic = (z * C * inv_A) % 5
        id_val = (z * D * inv_A) % 5
        fibre_counts[(ic, id_val)] += 1

        check(
            R_map(x) == (z, id_val),
            stage,
            f"R(x) != (z, z*D/A) on S_5000 at {x}: {R_map(x)} vs {(z, id_val)}",
        )
        check(
            G_reader(R_map(x)) == f"PRESENT({id_val})",
            stage,
            f"G(R(x)) != PRESENT({id_val}) on S_5000 at {x}",
        )

        for theta in (0, 1):
            j = selector_index(z, theta)
            check(j in (1, 3, 4), stage, f"unexpected generator g_{j} on S_5000")
            x_next = step_T(theta, x)
            check(x_next in s5000_set, stage, f"S_5000 not closed at {x}, theta={theta}")
            z_n, A_n, B_n, C_n, D_n, _ = psi_aff(x_next)
            check(
                A_n == (-A) % 5 and B_n == (-B) % 5,
                stage,
                f"(A', B') != (-A, -B) on S_5000 at {x}, theta={theta}",
            )
            inv_An = INV5[A_n]
            ic_n = (z_n * C_n * inv_An) % 5
            id_n = (z_n * D_n * inv_An) % 5
            check(
                (ic_n, id_n) == (ic, id_val),
                stage,
                f"invariant (zC/A, zD/A) changed from {(ic, id_val)} to {(ic_n, id_n)}",
            )
            check(
                G_reader(R_map(x_next)) == f"PRESENT({id_val})",
                stage,
                f"G(R(x_next)) != PRESENT({id_val})",
            )
            edge_checks += 1

    check(edge_checks == 10000, stage, f"edge_checks {edge_checks} != 10000")
    check(
        all(cnt == 200 for cnt in fibre_counts.values()),
        stage,
        f"S_5000 invariant fibres not all 200: {fibre_counts}",
    )

    for lam, mu in ALL_PAIRS:
        x = prep_E(lam, mu)
        for n in range(3):
            _, x = step_U(n, x)
        check(x in s5000_set, stage, f"x3({lam},{mu}) not in S_5000")
        z3, A3, _, C3, D3, _ = psi_aff(x)
        ic3 = (z3 * C3 * INV5[A3]) % 5
        id3 = (z3 * D3 * INV5[A3]) % 5
        check(
            (ic3, id3) == (lam, mu),
            stage,
            f"x3({lam},{mu}) invariants {(ic3, id3)} != ({lam},{mu})",
        )

    return f"states={len(s5000)} edges={edge_checks} fibres=25x200"


def run_stage_prepared_tail_and_regression_claim4() -> str:
    stage = "prepared_tail_and_regression_claim4"
    pair_sets: dict[tuple[int, int], set[tuple[int, ...]]] = {}
    union_set: set[tuple[int, ...]] = set()

    for lam, mu in ALL_PAIRS:
        states_lm: set[tuple[int, ...]] = set()
        for A in (1, 4):
            for z in (1, 4):
                inv_z = INV5[z]
                C = (lam * A * inv_z) % 5
                D = (mu * A * inv_z) % 5
                for q in F5:
                    states_lm.add(psi_aff_inv((z, A, 0, C, D, q)))
        check(
            len(states_lm) == 20,
            stage,
            f"|T_({lam},{mu})| = {len(states_lm)} != 20",
        )
        check(
            union_set.isdisjoint(states_lm),
            stage,
            f"T_({lam},{mu}) overlaps previous tail sets",
        )
        pair_sets[(lam, mu)] = states_lm
        union_set.update(states_lm)

    check(len(union_set) == 500, stage, f"|T_500| = {len(union_set)} != 500")
    characterized = {
        x
        for x in ALL_STATES
        if z_trace(x) in (1, 4) and psi_aff(x)[1] in (1, 4) and psi_aff(x)[2] == 0
    }
    check(union_set == characterized, stage, "T_500 != {z in {1,4}, A in {1,4}, B=0}")

    tail_edges = 0
    for (lam, mu), states_lm in pair_sets.items():
        for x in states_lm:
            check(
                G_reader(R_map(x)) == f"PRESENT({mu})",
                stage,
                f"tail state {x} in T_({lam},{mu}) does not read PRESENT({mu})",
            )
            for theta in (0, 1):
                x_next = step_T(theta, x)
                check(
                    x_next in states_lm,
                    stage,
                    f"T_({lam},{mu}) not closed under theta={theta} at {x}",
                )
                tail_edges += 1

    check(tail_edges == 1000, stage, f"tail_edges {tail_edges} != 1000")

    horizon = 1024
    observed_checkpoints = 0
    observed_updates = 0
    for lam, mu in ALL_PAIRS:
        x = prep_E(lam, mu)
        observed_checkpoints += 1
        for n in range(horizon):
            _, x = step_U(n, x)
            observed_checkpoints += 1
            observed_updates += 1
            if n + 1 == 3:
                check(
                    x in pair_sets[(lam, mu)],
                    stage,
                    f"x3({lam},{mu}) not in T_({lam},{mu})",
                )
            if n + 1 >= 3:
                check(
                    x in pair_sets[(lam, mu)],
                    stage,
                    f"x_{n+1}({lam},{mu}) left T_({lam},{mu})",
                )
                z_n, A_n, B_n, C_n, D_n, _ = psi_aff(x)
                check(
                    A_n in (1, 4) and B_n == 0,
                    stage,
                    f"unexpected (A_n, B_n) = {(A_n, B_n)} at n={n+1}",
                )
                ic_n = (z_n * C_n * INV5[A_n]) % 5
                id_n = (z_n * D_n * INV5[A_n]) % 5
                check(
                    (ic_n, id_n) == (lam, mu),
                    stage,
                    f"trajectory invariant drift at n={n+1} for ({lam},{mu})",
                )
                check(
                    R_map(x) == (z_n, mu) and G_reader(R_map(x)) == f"PRESENT({mu})",
                    stage,
                    f"readout drift at n={n+1} for ({lam},{mu})",
                )

    check(
        observed_checkpoints == 25625 and observed_updates == 25600,
        stage,
        f"unexpected trajectory counts: {observed_checkpoints}, {observed_updates}",
    )
    return (
        f"tail_sets=25x20 union=500 edges={tail_edges} "
        f"checkpoints={observed_checkpoints} updates={observed_updates}"
    )


def run_stage_access_boundary_and_quotient_claim5() -> str:
    stage = "access_boundary_and_quotient_claim5"
    init_zqr = {pi_zqr(prep_E(lam, mu)) for lam, mu in ALL_PAIRS}
    check(init_zqr == {(2, 0, 1)}, stage, f"initial (z,q,r) set {init_zqr} != {{(2,0,1)}}")

    # Compute full reachable (z, q, r) set from (2, 0, 1) under arbitrary control words
    reachable_zqr: set[tuple[int, int, int]] = {(2, 0, 1)}
    frontier = [(2, 0, 1)]
    while frontier:
        curr = frontier.pop()
        for theta in (0, 1):
            nxt = step_T_zqr(theta, curr)
            if nxt not in reachable_zqr:
                reachable_zqr.add(nxt)
                frontier.append(nxt)

    expected_tail_zqr = {
        (z, q, (z - A - q) % 5)
        for z in (1, 4)
        for A in (1, 4)
        for q in F5
    }
    check(
        len(expected_tail_zqr) == 20,
        stage,
        f"expected_tail_zqr size {len(expected_tail_zqr)} != 20",
    )
    check(
        reachable_zqr == {(2, 0, 1), (0, 1, 4)} | expected_tail_zqr,
        stage,
        f"unexpected reachable (z,q,r) set of size {len(reachable_zqr)}",
    )

    # Verify across 0 <= n <= 1024 that (z_n, q_n, r_n) is message-independent
    # while the raw source block (a_n, b_n, c_n, d_n) retains all 25 messages.
    horizon = 1024
    trajectories = {pair: [prep_E(*pair)] for pair in ALL_PAIRS}
    for pair, states_list in trajectories.items():
        x = states_list[0]
        for n in range(horizon):
            _, x = step_U(n, x)
            states_list.append(x)

    visited_actual_zqr: set[tuple[int, int, int]] = set()
    for n in range(horizon + 1):
        zqr_set = {pi_zqr(trajectories[pair][n]) for pair in ALL_PAIRS}
        check(
            len(zqr_set) == 1,
            stage,
            f"(z,q,r) depends on message at n={n}: {zqr_set}",
        )
        visited_actual_zqr.update(zqr_set)
        source_blocks = {trajectories[pair][n][:4] for pair in ALL_PAIRS}
        check(
            len(source_blocks) == 25,
            stage,
            f"source block depleted at n={n}: only {len(source_blocks)} distinct",
        )

    check(
        visited_actual_zqr == reachable_zqr,
        stage,
        f"actual trajectory visited {len(visited_actual_zqr)} != 22 reachable zqr states",
    )

    # Confirm R is a mixed coordinate: depends on both (a,b,c,d) and (q,r).
    base_x = prep_E(0, 0)
    alt_source_x = prep_E(0, 1)
    check(
        step_T(1, base_x)[4:] == step_T(1, alt_source_x)[4:]
        and R_map(step_T(1, base_x)) != R_map(step_T(1, alt_source_x)),
        stage,
        "R failed to depend on source coordinates (a,b,c,d)",
    )
    port_x1 = (0, 0, 0, 0, 0, 2)
    port_x2 = (0, 0, 0, 0, 1, 1)
    check(
        port_x1[:4] == port_x2[:4] and R_map(port_x1) != R_map(port_x2),
        stage,
        "R failed to depend on port coordinates (q,r)",
    )

    return (
        f"init_zqr=(2,0,1) reachable_zqr={len(reachable_zqr)} "
        f"msg_indep_steps={horizon + 1} source_blocks=25"
    )


def run_stage_nonaffinity_and_minimality_claims6_7() -> str:
    stage = "nonaffinity_and_minimality_claims6_7"

    # Claim 6: Nonaffinity witness E(0,0), E(0,1) before and after g_4
    e00 = prep_E(0, 0)
    e01 = prep_E(0, 1)
    check(
        e00 == (4, 3, 2, 2, 0, 1) and e01 == (4, 1, 2, 4, 0, 1),
        stage,
        f"unexpected E(0,0)={e00} or E(0,1)={e01}",
    )
    r_before_00 = R_map(e00)
    r_before_01 = R_map(e01)
    check(
        r_before_00 == (2, 0) and r_before_01 == (2, 0),
        stage,
        f"R before g4 not common (2,0): {r_before_00}, {r_before_01}",
    )
    after_00 = g_tuple(4, e00)
    after_01 = g_tuple(4, e01)
    check(
        after_00 == (3, 3, 1, 2, 2, 0) and after_01 == (3, 0, 1, 0, 2, 0),
        stage,
        f"unexpected g4(E(0,0))={after_00} or g4(E(0,1))={after_01}",
    )
    r_after_00 = R_map(after_00)
    r_after_01 = R_map(after_01)
    check(
        r_after_00 == (1, 0) and r_after_01 == (1, 1) and r_after_00 != r_after_01,
        stage,
        f"nonaffinity witness failed after g4: {r_after_00} vs {r_after_01}",
    )

    # Reconcile with origin-zero arbitrary-rank affine common-reset obstruction
    t3 = GENERATOR_SHIFTS[3]
    t4 = GENERATOR_SHIFTS[4]
    z2_eq_1_count = 0
    z2_eq_2_count = 0
    for x0 in ALL_STATES:
        _, x1 = step_U(0, x0)
        _, x2 = step_U(1, x1)
        _, x3 = step_U(2, x2)
        z2 = z_trace(x2)
        check(z2 in (1, 2), stage, f"z(x2) = {z2} not in {{1, 2}} at x0={x0}")
        x_sum = tuple((x2[i] + x3[i]) % 5 for i in range(6))
        if z2 == 1:
            z2_eq_1_count += 1
            check(x_sum == t3, stage, f"x2 + x3 != t3 on z(x2)=1 at x0={x0}")
            check(
                x14_sign_rep(x2) == x14_sign_rep(x3),
                stage,
                f"x2 and x3 not in same X_14 sign fibre at x0={x0}",
            )
        else:
            z2_eq_2_count += 1
            check(x_sum == t4, stage, f"x2 + x3 != t4 on z(x2)=2 at x0={x0}")

    check(
        (z2_eq_1_count, z2_eq_2_count) == (9375, 6250),
        stage,
        f"unexpected z(x2) split {(z2_eq_1_count, z2_eq_2_count)}",
    )

    # Claim 7: Two F5 coordinates minimal for 6 distinct semantic outputs,
    # and same-R initial witness E(0,0), E(1,0) with different next-R.
    realized_semantics: set[str] = set()
    for lam, mu in ALL_PAIRS:
        x0 = prep_E(lam, mu)
        _, x1 = step_U(0, x0)
        _, x2 = step_U(1, x1)
        _, x3 = step_U(2, x2)
        for st in (x0, x1, x2, x3):
            realized_semantics.add(G_reader(R_map(st)))

    expected_semantics = {"BLANK"} | {f"PRESENT({m})" for m in F5}
    check(
        realized_semantics == expected_semantics and len(realized_semantics) == 6,
        stage,
        f"semantic output set {realized_semantics} != 6 expected values",
    )
    min_k = next(k for k in range(5) if 5**k >= len(realized_semantics))
    check(
        5**0 < 6 and 5**1 < 6 <= 5**2 and min_k == 2,
        stage,
        f"minimal F5 coordinate count {min_k} != 2",
    )

    e10 = prep_E(1, 0)
    check(e10 == (2, 3, 4, 2, 0, 1), stage, f"unexpected E(1,0)={e10}")
    check(
        R_map(e00) == (2, 0) and R_map(e10) == (2, 0),
        stage,
        "E(0,0) and E(1,0) do not share initial R=(2,0)",
    )
    _, x1_00 = step_U(0, e00)
    _, x1_10 = step_U(0, e10)
    check(
        x1_00 == (0, 0, 3, 2, 1, 4) and x1_10 == (3, 0, 0, 2, 1, 4),
        stage,
        f"unexpected x1(0,0)={x1_00} or x1(1,0)={x1_10}",
    )
    check(
        R_map(x1_00) == (0, 0) and R_map(x1_10) == (0, 1) and R_map(x1_00) != R_map(x1_10),
        stage,
        f"non-autonomy witness failed at n=1: {R_map(x1_00)} vs {R_map(x1_10)}",
    )

    # Six explicit malformed-input rejections
    malformed_cases = (
        lambda: validate_state([0, 0, 0, 0, 0, 0]),
        lambda: validate_state((0, 0, 0, 0, 0)),
        lambda: validate_state((True, 0, 0, 0, 0, 0)),
        lambda: validate_state((5, 0, 0, 0, 0, 0)),
        lambda: step_U(-1, (0, 0, 0, 0, 0, 0)),
        lambda: G_reader((2, 0, 0)),  # type: ignore[arg-type]
    )
    rejected = 0
    for fn in malformed_cases:
        try:
            fn()
        except ValueError:
            rejected += 1
    check(rejected == 6, stage, f"malformed rejections {rejected} != 6")

    return (
        f"nonaff=((2,0)->(1,0)/(1,1)) z2_split=9375+6250 "
        f"sem_vals={len(realized_semantics)} min_k={min_k} "
        f"nonaut=((2,0)->(0,0)/(0,1)) malformed={rejected}"
    )


STAGE_RUNNERS = {
    "custody": run_stage_custody,
    "generators_and_quotient": run_stage_generators_and_quotient,
    "nonlinear_chart_claim1": run_stage_nonlinear_chart_claim1,
    "prefix_claim2": run_stage_prefix_claim2,
    "synchronized_invariants_claim3": run_stage_synchronized_invariants_claim3,
    "prepared_tail_and_regression_claim4": run_stage_prepared_tail_and_regression_claim4,
    "access_boundary_and_quotient_claim5": run_stage_access_boundary_and_quotient_claim5,
    "nonaffinity_and_minimality_claims6_7": run_stage_nonaffinity_and_minimality_claims6_7,
}


def main() -> int:
    print(f"PROBE {PROBE_ID}")
    failed_at: int | None = None
    failure_exc: ExactAuditFailure | None = None

    for idx, stage in enumerate(STAGE_ORDER):
        try:
            summary = STAGE_RUNNERS[stage]()
            print(f"STAGE {stage} PASS {summary}")
        except ExactAuditFailure as exc:
            print(f"STAGE {stage} FAIL {exc.message}")
            failed_at = idx
            failure_exc = exc
            break

    if failed_at is not None:
        for skipped in STAGE_ORDER[failed_at + 1 :]:
            print(f"STAGE {skipped} NOT_RUN")
        print(
            f"VERDICT SCIENTIFIC_FAIL stage={failure_exc.stage} "
            f"reason={failure_exc.message}"
        )
        return 0

    print(
        "SUMMARY states=15625 pairs=25 s5000=5000 tail=500 "
        "traj_checkpoints=25625 traj_updates=25600 zqr_reachable=22 min_f5_coords=2"
    )
    print(f"VERDICT PASS {PROBE_ID}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
