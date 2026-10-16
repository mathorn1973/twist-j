#!/usr/bin/env python3
"""Independent exact audit of two-contact wave-summary memory ranks and refresh laws.

Probe: P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1
Issue: #1528
Primary Subject: notes/C-HB-REFRESH-MEMORY-BOUNDARY-N (#1525)
Author: A. M. Thorn <thorn@twistj.com>
License: Apache-2.0
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, replace
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
from itertools import permutations, product
from math import lcm
from pathlib import Path
import sys
from typing import Iterable, Mapping


PROBE_ID = "P-HB-REFRESH-MEMORY-INDEPENDENT-AUDIT-1"
PROBE_DIR = Path(__file__).resolve().parent

Point = tuple[int, int, int]
Vec = dict[int, Q]
Port = tuple[Q, Q, Q, Q]
Vec2 = tuple[Q, Q]
Vec3 = tuple[Q, Q, Q]
Vec4 = tuple[Q, Q, Q, Q]

ZERO_PORT: Port = (Q(0), Q(0), Q(0), Q(0))
F5: tuple[int, ...] = (0, 1, 2, 3, 4)
BALANCED_LIFT: dict[int, int] = {0: 0, 1: 1, 2: 2, 3: -2, 4: -1}
ALL_LABELS: tuple[tuple[int, int], ...] = tuple(product(F5, repeat=2))

Y_SITES: tuple[Point, ...] = (
    (0, 0, 0),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
    (2, 0, 0),
)
Z_NEAR: Point = (6, 0, 0)
Z_FAR: Point = (10, 0, 0)

SHELL_WEIGHTS: dict[int, int] = {2: 6, 4: 1, 8: 15, 10: 1, 16: 1}
DOMAIN_SHA256 = "2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0"
DOMAIN_BYTES = 5029
EXPECTED_DOMAIN_SITES = 705
EXPECTED_AMPLITUDE_DIM = 1426

G_TARGET: tuple[Vec2, Vec2] = (
    (Q(4, 5), Q(-1, 5)),
    (Q(-1, 5), Q(4, 5)),
)
M_TARGET: tuple[Port, Port] = (
    (Q(4, 5), Q(-1, 5), Q(-1, 5), Q(-1, 5)),
    (Q(-1, 5), Q(4, 5), Q(-1, 5), Q(-1, 5)),
)
H_ROW_TARGET: Port = (Q(1, 324), Q(6, 324), Q(6, 324), Q(0))
KAPPA_TARGET: Vec2 = (Q(-145483, 10497600), Q(-173653, 10497600))
MINOR_3X3_TARGET: Q = Q(3, 5) * Q(-1, 10 * 324 * 324)
MINOR_4X4_TARGET: Q = Q(3, 5) * Q(-1, 10 * 324) * Q(-1, 10 * 324 * 324)

STAGE_ORDER: tuple[str, ...] = (
    "custody",
    "geometry_and_operators",
    "refresh_identities_target1",
    "rank_minors_and_criteria_target2",
    "far_counterexample_target3",
    "finite_contact_predictor_target4",
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


def check_eq(actual: object, expected: object, stage: str, label: str) -> None:
    if actual != expected:
        raise ExactAuditFailure(
            stage, f"{label}: actual={actual!r} expected={expected!r}"
        )


def _point_add(a: Point, b: Point) -> Point:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


STENCIL: tuple[tuple[Point, int], ...] = tuple(
    (d, SHELL_WEIGHTS[d[0] * d[0] + d[1] * d[1] + d[2] * d[2]])
    for d in product(range(-4, 5), repeat=3)
    if (d[0] + d[1] + d[2]) % 2 == 0
    and (d[0] * d[0] + d[1] * d[1] + d[2] * d[2]) in SHELL_WEIGHTS
)
B_ZERO: tuple[Point, ...] = ((0, 0, 0),) + tuple(d for d, _ in STENCIL)
D: tuple[Point, ...] = tuple(
    sorted(
        {
            _point_add(_point_add(y, d1), d2)
            for y in Y_SITES
            for d1 in B_ZERO
            for d2 in B_ZERO
        }
    )
)
INDEX: dict[Point, int] = {site: idx for idx, site in enumerate(D)}
PORT_IDS: tuple[int, ...] = tuple(INDEX[y] for y in Y_SITES[:4])
PORT_SET: frozenset[int] = frozenset(PORT_IDS)
Y_IDS: tuple[int, ...] = tuple(INDEX[y] for y in Y_SITES)
Y4_ID: int = INDEX[Y_SITES[4]]
Z_NEAR_ID: int = INDEX[Z_NEAR]
Z_FAR_ID: int = INDEX[Z_FAR]
AMPLITUDE_DIM: int = 2 * len(D) + 16

NEIGHBORS: tuple[tuple[tuple[int, int], ...], ...] = tuple(
    tuple(
        (INDEX[target], weight)
        for delta, weight in STENCIL
        if (target := _point_add(site, delta)) in INDEX
    )
    for site in D
)


def q_val(x: Q | int) -> Q:
    if not isinstance(x, (int, Q)):
        raise TypeError(f"only exact int or Fraction allowed, got {type(x)!r}")
    return Q(x)


def port_vec(values: Iterable[Q | int]) -> Port:
    tup = tuple(q_val(v) for v in values)
    if len(tup) != 4:
        raise ValueError(f"port vector must have length 4, got {len(tup)}")
    return tup  # type: ignore[return-value]


def sparse_vec(values: Mapping[int, Q | int]) -> Vec:
    out: Vec = {}
    for idx, val in values.items():
        if not isinstance(idx, int) or not (0 <= idx < len(D)):
            raise ValueError(f"invalid site index {idx!r}")
        qv = q_val(val)
        if qv:
            out[idx] = qv
    return out


def vec_add(*vectors: Mapping[int, Q]) -> Vec:
    out: Vec = {}
    for vec in vectors:
        for idx, val in vec.items():
            tot = out.get(idx, Q(0)) + val
            if tot:
                out[idx] = tot
            else:
                out.pop(idx, None)
    return out


def vec_scale(vec: Mapping[int, Q], scalar: Q | int) -> Vec:
    s = q_val(scalar)
    if not s:
        return {}
    return {idx: s * val for idx, val in vec.items() if val}


def vec_sub(left: Mapping[int, Q], right: Mapping[int, Q]) -> Vec:
    return vec_add(left, vec_scale(right, -1))


def vec_dot(left: Mapping[int, Q], right: Mapping[int, Q]) -> Q:
    if len(left) > len(right):
        left, right = right, left
    return sum((val * right[idx] for idx, val in left.items() if idx in right), Q(0))


def vec_norm2(vec: Mapping[int, Q]) -> Q:
    return sum((val * val for val in vec.values()), Q(0))


def port_add(left: Port, right: Port) -> Port:
    return port_vec(a + b for a, b in zip(left, right))


def port_scale(vec: Port, scalar: Q | int) -> Port:
    s = q_val(scalar)
    return port_vec(s * v for v in vec)


def port_dot(left: Port, right: Port) -> Q:
    return sum((a * b for a, b in zip(left, right)), Q(0))


def port_norm2(vec: Port) -> Q:
    return port_dot(vec, vec)


def P_op(p: Port) -> Vec:
    return {idx: val for idx, val in zip(PORT_IDS, port_vec(p)) if val}


def PT_op(vec: Mapping[int, Q]) -> Port:
    return port_vec(vec.get(idx, Q(0)) for idx in PORT_IDS)


def J0_op(vec: Mapping[int, Q]) -> Vec:
    return {idx: val for idx, val in vec.items() if idx not in PORT_SET and val}


def K_op(vec: Mapping[int, Q]) -> Vec:
    return {
        idx: (val / 2 if idx in PORT_SET else val)
        for idx, val in vec.items()
        if val
    }


def S_col(col_idx: int) -> Vec:
    if col_idx not in (0, 1, 2, 3):
        raise ValueError(f"invalid source column {col_idx!r}")
    out: Vec = {}
    for j, y_id in enumerate(Y_IDS):
        out[y_id] = (Q(4, 5) if j == col_idx else Q(-1, 5))
    return out


S0_VEC: Vec = S_col(0)
S1_VEC: Vec = S_col(1)
E4_VEC: Vec = {Y4_ID: Q(1)}


def A_op(eta2: Vec2) -> Vec:
    c0, c1 = q_val(eta2[0]), q_val(eta2[1])
    return vec_add(vec_scale(S0_VEC, c0), vec_scale(S1_VEC, c1))


def AT_op(vec: Mapping[int, Q]) -> Vec2:
    return (vec_dot(S0_VEC, vec), vec_dot(S1_VEC, vec))


def eta2_from_label(label: tuple[int, int]) -> Vec2:
    q, r = label
    if q not in BALANCED_LIFT or r not in BALANCED_LIFT:
        raise ValueError(f"invalid F5^2 label {label!r}")
    return (Q(BALANCED_LIFT[q], 2), Q(BALANCED_LIFT[r] + 1, 2))


def _canon_key(vec: Mapping[int, Q]) -> tuple[tuple[int, Q], ...]:
    return tuple(sorted((idx, q_val(val)) for idx, val in vec.items() if val))


def _int_scaled(key: tuple[tuple[int, Q], ...]) -> tuple[int, list[tuple[int, int]]]:
    if not key:
        return 1, []
    denom = lcm(*(val.denominator for _, val in key))
    return denom, [
        (idx, val.numerator * (denom // val.denominator)) for idx, val in key
    ]


@lru_cache(maxsize=None)
def _h_cached(key: tuple[tuple[int, Q], ...]) -> tuple[tuple[int, Q], ...]:
    if not key:
        return ()
    denom, entries = _int_scaled(key)
    totals: dict[int, int] = {}
    for idx, val in entries:
        totals[idx] = totals.get(idx, 0) + 360 * val
        for nbr, weight in NEIGHBORS[idx]:
            totals[nbr] = totals.get(nbr, 0) + weight * val
    scale_denom = 324 * denom
    return tuple((idx, Q(tot, scale_denom)) for idx, tot in totals.items() if tot)


@lru_cache(maxsize=None)
def _l_cached(key: tuple[tuple[int, Q], ...]) -> tuple[tuple[int, Q], ...]:
    if not key:
        return ()
    denom, entries = _int_scaled(key)
    totals: dict[int, int] = {}
    for idx, val in entries:
        totals[idx] = totals.get(idx, 0) + 288 * val
        for nbr, weight in NEIGHBORS[idx]:
            totals[nbr] = totals.get(nbr, 0) - weight * val
    scale_denom = 324 * denom
    return tuple((idx, Q(tot, scale_denom)) for idx, tot in totals.items() if tot)


def H_op(vec: Mapping[int, Q]) -> Vec:
    """Wave operator H = 2I - L_D evaluated from integer stencil sums."""
    return dict(_h_cached(_canon_key(vec)))


def LD_op(vec: Mapping[int, Q]) -> Vec:
    """Full-diagonal Dirichlet Laplacian L_D evaluated directly from stencil."""
    return dict(_l_cached(_canon_key(vec)))


@dataclass(frozen=True)
class WaveTapeState:
    u: Vec
    v: Vec
    a0: Port = ZERO_PORT
    a1: Port = ZERO_PORT
    b0: Port = ZERO_PORT
    b1: Port = ZERO_PORT

    def __post_init__(self) -> None:
        object.__setattr__(self, "u", sparse_vec(self.u))
        object.__setattr__(self, "v", sparse_vec(self.v))
        for slot in ("a0", "a1", "b0", "b1"):
            object.__setattr__(self, slot, port_vec(getattr(self, slot)))


def F_step(state: WaveTapeState) -> WaveTapeState:
    hv = H_op(state.v)
    j0u = J0_op(state.u)
    pa0 = P_op(state.a0)
    w = K_op(vec_add(hv, vec_scale(j0u, -1), vec_scale(pa0, 4)))
    b_out = port_add(state.a0, port_scale(PT_op(vec_sub(w, state.u)), Q(-1, 2)))
    return WaveTapeState(
        u=state.v,
        v=w,
        a0=state.a1,
        a1=state.b1,
        b0=b_out,
        b1=state.b0,
    )


def F_inv_step(state: WaveTapeState) -> WaveTapeState:
    hu = H_op(state.u)
    j0v = J0_op(state.v)
    pb0 = P_op(state.b0)
    old_u = K_op(vec_add(hu, vec_scale(j0v, -1), vec_scale(pb0, 4)))
    old_a0 = port_add(state.b0, port_scale(PT_op(vec_sub(state.v, old_u)), Q(1, 2)))
    return WaveTapeState(
        u=old_u,
        v=state.u,
        a0=old_a0,
        a1=state.a0,
        b0=state.b1,
        b1=state.a1,
    )


def wave_energy_direct(u: Mapping[int, Q], v: Mapping[int, Q]) -> Q:
    """Direct quadratic wave energy E_D(u, v) = (||v - u||^2 + u^T L_D v) / 2."""
    return (vec_norm2(vec_sub(v, u)) + vec_dot(u, LD_op(v))) / 2


def full_energy_direct(state: WaveTapeState) -> Q:
    tape_sum = (
        port_norm2(state.a0)
        + port_norm2(state.a1)
        + port_norm2(state.b0)
        + port_norm2(state.b1)
    )
    return wave_energy_direct(state.u, state.v) + 2 * tape_sum


def rho_func(u: Mapping[int, Q], v: Mapping[int, Q]) -> Vec2:
    """Wave functional rho(u, v) = A^T(v - H u / 2)."""
    diff = vec_sub(v, vec_scale(H_op(u), Q(1, 2)))
    return AT_op(diff)


def gamma_func(u: Mapping[int, Q], v: Mapping[int, Q]) -> Q:
    """Wave functional gamma(u, v) = (u_{y4} - (H v)_{y4} / 2) / 5."""
    hv = H_op(v)
    return (u.get(Y4_ID, Q(0)) - hv.get(Y4_ID, Q(0)) / 2) / 5


def delta_func(u: Mapping[int, Q], v: Mapping[int, Q]) -> Q:
    """Wave functional delta(u, v) = (v_{y4} - (H K H v)_{y4} / 2 + (H J0 u)_{y4} / 2) / 5."""
    hkh_v = H_op(K_op(H_op(v)))
    hj0_u = H_op(J0_op(u))
    return (
        v.get(Y4_ID, Q(0))
        - hkh_v.get(Y4_ID, Q(0)) / 2
        + hj0_u.get(Y4_ID, Q(0)) / 2
    ) / 5


def xi_func(u: Mapping[int, Q], v: Mapping[int, Q]) -> Vec3:
    r0, r1 = rho_func(u, v)
    return (r0, r1, delta_func(u, v))


def mat2_vec2(mat: tuple[Vec2, Vec2], vec: Vec2) -> Vec2:
    return (
        mat[0][0] * vec[0] + mat[0][1] * vec[1],
        mat[1][0] * vec[0] + mat[1][1] * vec[1],
    )


def mat2x4_port(mat: tuple[Port, Port], p: Port) -> Vec2:
    return (port_dot(mat[0], p), port_dot(mat[1], p))


def vec2_dot(a: Vec2, b: Vec2) -> Q:
    return a[0] * b[0] + a[1] * b[1]


def det_nxn(matrix: tuple[tuple[Q, ...], ...]) -> Q:
    """Exact Leibniz determinant for small rational matrices."""
    n = len(matrix)
    total = Q(0)
    for perm in permutations(range(n)):
        inversions = sum(
            1
            for i in range(n)
            for j in range(i + 1, n)
            if perm[i] > perm[j]
        )
        sign = -1 if (inversions % 2) else 1
        term = Q(sign)
        for row_idx, col_idx in enumerate(perm):
            term *= matrix[row_idx][col_idx]
        total += term
    return total


def reduced_contact_work(rho: Vec2, eta2: Vec2, sigma: int) -> Q:
    if sigma not in (-1, 1):
        raise ValueError(f"invalid contact sign {sigma!r}")
    g_eta = mat2_vec2(G_TARGET, eta2)
    return vec2_dot(eta2, g_eta) / 2 + sigma * vec2_dot(eta2, rho)


def full_contact_step(
    state: WaveTapeState,
    work: Q,
    battery: Q,
    capacity: Q,
    sigma: int,
    label: tuple[int, int],
) -> tuple[WaveTapeState, Q, Q, int, Q, str]:
    eta2 = eta2_from_label(label)
    a_vec = A_op(eta2)
    v_cand = vec_add(state.v, vec_scale(a_vec, sigma))
    delta_dir = wave_energy_direct(state.u, v_cand) - wave_energy_direct(
        state.u, state.v
    )
    proposed = battery - delta_dir
    if proposed < 0:
        return state, work, battery, sigma, delta_dir, "lower_refusal"
    if proposed > capacity:
        return state, work, battery, sigma, delta_dir, "upper_refusal"
    kind = (
        "zero_cost_accept"
        if delta_dir == 0
        else ("neg_work_accept" if delta_dir < 0 else "pos_work_accept")
    )
    next_state = replace(state, v=v_cand)
    return next_state, work + delta_dir, proposed, -sigma, delta_dir, kind


def reduced_single_contact_step(
    xi: Vec3,
    work: Q,
    battery: Q,
    capacity: Q,
    sigma: int,
    label: tuple[int, int],
) -> tuple[Vec3, Q, Q, int, Q, str]:
    rho = (xi[0], xi[1])
    delta_mem = xi[2]
    eta2 = eta2_from_label(label)
    delta_red = reduced_contact_work(rho, eta2, sigma)
    proposed = battery - delta_red
    if proposed < 0:
        return xi, work, battery, sigma, delta_red, "lower_refusal"
    if proposed > capacity:
        return xi, work, battery, sigma, delta_red, "upper_refusal"
    kind = (
        "zero_cost_accept"
        if delta_red == 0
        else ("neg_work_accept" if delta_red < 0 else "pos_work_accept")
    )
    g_eta = mat2_vec2(G_TARGET, eta2)
    k_eta = vec2_dot(KAPPA_TARGET, eta2)
    next_xi: Vec3 = (
        rho[0] + sigma * g_eta[0],
        rho[1] + sigma * g_eta[1],
        delta_mem + sigma * k_eta,
    )
    return next_xi, work + delta_red, proposed, -sigma, delta_red, kind


def reduced_two_contact_predict(
    xi0: Vec3,
    a0: Port,
    a1: Port,
    work0: Q,
    battery0: Q,
    capacity: Q,
    label1: tuple[int, int],
    sigma1: int,
    label2: tuple[int, int],
    sigma2: int,
) -> dict[str, object]:
    xi1, work1, battery1, sigma1_after, delta1, kind1 = reduced_single_contact_step(
        xi0, work0, battery0, capacity, sigma1, label1
    )
    delta_plus = xi1[2]
    h_dot_a0 = port_dot(H_ROW_TARGET, a0)
    m_a1 = mat2x4_port(M_TARGET, a1)
    base_shift = delta_plus - h_dot_a0 / 5
    rho2: Vec2 = (base_shift + 2 * m_a1[0], base_shift + 2 * m_a1[1])

    eta2_second = eta2_from_label(label2)
    delta2 = reduced_contact_work(rho2, eta2_second, sigma2)
    proposed2 = battery1 - delta2
    if proposed2 < 0:
        kind2 = "lower_refusal"
        work2 = work1
        battery2 = battery1
        sigma2_after = sigma2
        rho2_after = rho2
    elif proposed2 > capacity:
        kind2 = "upper_refusal"
        work2 = work1
        battery2 = battery1
        sigma2_after = sigma2
        rho2_after = rho2
    else:
        kind2 = (
            "zero_cost_accept"
            if delta2 == 0
            else ("neg_work_accept" if delta2 < 0 else "pos_work_accept")
        )
        work2 = work1 + delta2
        battery2 = proposed2
        sigma2_after = -sigma2
        g_eta2 = mat2_vec2(G_TARGET, eta2_second)
        rho2_after = (
            rho2[0] + sigma2 * g_eta2[0],
            rho2[1] + sigma2 * g_eta2[1],
        )

    return {
        "xi1": xi1,
        "delta1": delta1,
        "kind1": kind1,
        "rho2": rho2,
        "delta2": delta2,
        "kind2": kind2,
        "rho2_after": rho2_after,
        "work": work2,
        "battery": battery2,
        "signs": (sigma1_after, sigma2_after),
    }


def run_stage_custody() -> str:
    stage = "custody"
    manifest_path = PROBE_DIR / "INPUTS.sha256"
    sources_path = PROBE_DIR / "SOURCES.tsv"
    check(manifest_path.is_file(), stage, "missing INPUTS.sha256")
    check(sources_path.is_file(), stage, "missing SOURCES.tsv")

    expected_files = {
        "DOMAIN.tsv",
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
    check_eq(sorted(seen_files), sorted(expected_files), stage, "pinned-file-set")

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


def run_stage_geometry_and_operators() -> str:
    stage = "geometry_and_operators"
    raw_domain = (PROBE_DIR / "DOMAIN.tsv").read_bytes()
    check_eq(len(raw_domain), DOMAIN_BYTES, stage, "domain-bytes")
    check_eq(
        hashlib.sha256(raw_domain).hexdigest(),
        DOMAIN_SHA256,
        stage,
        "domain-sha256",
    )
    lines = raw_domain.decode("ascii").splitlines()
    check_eq(lines[0], "x\ty\tz", stage, "domain-header")
    file_sites = tuple(
        tuple(int(tok) for tok in line.split("\t")) for line in lines[1:]
    )
    check_eq(len(file_sites), EXPECTED_DOMAIN_SITES, stage, "file-site-count")
    check_eq(len(D), EXPECTED_DOMAIN_SITES, stage, "constructed-site-count")
    check_eq(D, file_sites, stage, "ordered-domain-equality")
    reconstructed = (
        "x\ty\tz\n" + "".join(f"{x}\t{y}\t{z}\n" for x, y, z in D)
    ).encode("ascii")
    check_eq(reconstructed, raw_domain, stage, "reconstructed-domain-bytes")

    check_eq(len(STENCIL), 60, stage, "stencil-size")
    check_eq(len(B_ZERO), 61, stage, "b0-size")
    check_eq(sum(w for _, w in STENCIL), 288, stage, "stencil-weight-sum")
    check_eq(AMPLITUDE_DIM, EXPECTED_AMPLITUDE_DIM, stage, "amplitude-dim")

    directed_edges = 0
    for i, site in enumerate(D):
        check_eq(sum(site) % 2, 0, stage, f"d3-parity-{i}")
        for j, weight in NEIGHBORS[i]:
            rev = next((w for nbr, w in NEIGHBORS[j] if nbr == i), None)
            check_eq(rev, weight, stage, f"stencil-symmetry-{i}-{j}")
            directed_edges += 1
        ei = {i: Q(1)}
        hi = H_op(ei)
        li = LD_op(ei)
        check_eq(vec_add(hi, li), {i: Q(2)}, stage, f"H-plus-LD-{i}")
        check_eq(hi.get(i, Q(0)), Q(10, 9), stage, f"H-diag-{i}")
        check_eq(li.get(i, Q(0)), Q(8, 9), stage, f"LD-diag-{i}")
        # Lemma 1 checks on each site basis vector
        check_eq(AT_op(J0_op(ei)), (
            Q(-1, 5) if i == Y4_ID else Q(0),
            Q(-1, 5) if i == Y4_ID else Q(0),
        ), stage, f"AT-J0-{i}")
        check_eq(
            vec_sub(K_op(ei), vec_scale(ei, Q(1, 2))),
            vec_scale(J0_op(ei), Q(1, 2)),
            stage,
            f"K-minus-half-I-{i}",
        )
        check_eq(K_op(J0_op(ei)), J0_op(ei), stage, f"K-J0-{i}")

    for j in range(4):
        p_unit = port_vec(int(k == j) for k in range(4))
        check_eq(
            K_op(P_op(p_unit)),
            vec_scale(P_op(p_unit), Q(1, 2)),
            stage,
            f"K-P-port-{j}",
        )

    # Check G = A^T A, M = A^T P, h^T = e4^T H P, kappa^T = e4^T(A - H K H A / 2) / 5
    g_computed = (AT_op(S0_VEC), AT_op(S1_VEC))
    check_eq(g_computed, G_TARGET, stage, "G-matrix")
    check_eq(det_nxn(G_TARGET), Q(3, 5), stage, "det-G")

    m_cols = [
        AT_op(P_op(port_vec(int(k == j) for k in range(4)))) for j in range(4)
    ]
    m_computed: tuple[Port, Port] = (
        port_vec(m_cols[j][0] for j in range(4)),
        port_vec(m_cols[j][1] for j in range(4)),
    )
    check_eq(m_computed, M_TARGET, stage, "M-matrix")

    h_row_computed = PT_op(H_op(E4_VEC))
    check_eq(h_row_computed, H_ROW_TARGET, stage, "h-row")

    kappa_computed = (delta_func({}, S0_VEC), delta_func({}, S1_VEC))
    check_eq(kappa_computed, KAPPA_TARGET, stage, "kappa-row")

    return (
        f"sites={len(D)} amp_dim={AMPLITUDE_DIM} stencil={len(STENCIL)} "
        f"directed_edges={directed_edges} h=1/324,1/54,1/54,0 "
        f"kappa={KAPPA_TARGET[0]},{KAPPA_TARGET[1]}"
    )


def _iter_full_basis() -> Iterable[tuple[str, WaveTapeState]]:
    for i in range(len(D)):
        yield f"u[{i}]", WaveTapeState(u={i: Q(1)}, v={})
    for i in range(len(D)):
        yield f"v[{i}]", WaveTapeState(u={}, v={i: Q(1)})
    for slot in ("a0", "a1", "b0", "b1"):
        for j in range(4):
            unit_p = port_vec(int(k == j) for k in range(4))
            yield f"{slot}[{j}]", WaveTapeState(u={}, v={}, **{slot: unit_p})


def run_stage_refresh_identities_target1() -> str:
    stage = "refresh_identities_target1"
    basis_count = 0
    coeff_checks = 0
    inv_checks = 0

    for label, state in _iter_full_basis():
        basis_count += 1
        f1 = F_step(state)
        f2 = F_step(f1)

        # Two-sided invertibility and linear energy-coupling identity on basis
        check_eq(F_inv_step(f1), state, stage, f"F_inv_after_F-{label}")
        check_eq(F_step(F_inv_step(state)), state, stage, f"F_after_F_inv-{label}")
        inv_checks += 2
        coupling_lhs = vec_sub(vec_add(f1.v, state.u), H_op(state.v))
        coupling_rhs = vec_scale(P_op(port_add(state.a0, f1.b0)), 2)
        check_eq(coupling_lhs, coupling_rhs, stage, f"coupling-identity-{label}")

        # Target 1 identity 1: rho(FX) = gamma(X)*1_2 + 2 M a0
        gam_x = gamma_func(state.u, state.v)
        m_a0 = mat2x4_port(M_TARGET, state.a0)
        rho_f1_expected: Vec2 = (gam_x + 2 * m_a0[0], gam_x + 2 * m_a0[1])
        rho_f1_actual = rho_func(f1.u, f1.v)
        check_eq(rho_f1_actual, rho_f1_expected, stage, f"rho(FX)-{label}")
        coeff_checks += 2

        # Target 1 identity 2: gamma(FX) = delta(X) - h^T a0 / 5
        del_x = delta_func(state.u, state.v)
        h_a0 = port_dot(H_ROW_TARGET, state.a0)
        gam_f1_expected: Q = del_x - h_a0 / 5
        gam_f1_actual = gamma_func(f1.u, f1.v)
        check_eq(gam_f1_actual, gam_f1_expected, stage, f"gamma(FX)-{label}")
        coeff_checks += 1

        # Target 1 identity 3: rho(F^2 X) = (delta(X) - h^T a0 / 5)*1_2 + 2 M a1
        m_a1 = mat2x4_port(M_TARGET, state.a1)
        rho_f2_expected: Vec2 = (
            gam_f1_expected + 2 * m_a1[0],
            gam_f1_expected + 2 * m_a1[1],
        )
        rho_f2_actual = rho_func(f2.u, f2.v)
        check_eq(rho_f2_actual, rho_f2_expected, stage, f"rho(F2X)-{label}")
        coeff_checks += 2

    check_eq(basis_count, EXPECTED_AMPLITUDE_DIM, stage, "basis-count")
    check_eq(coeff_checks, 5 * EXPECTED_AMPLITUDE_DIM, stage, "coeff-check-count")
    check_eq(coeff_checks, 7130, stage, "coeff-check-7130")

    return (
        f"basis_inputs={basis_count} refresh_coefficients={coeff_checks} "
        f"inverse_compositions={inv_checks}"
    )


def run_stage_rank_minors_and_criteria_target2() -> str:
    stage = "rank_minors_and_criteria_target2"
    check_eq(_point_add(Y_SITES[4], (4, 0, 0)), Z_NEAR, stage, "z-near-decomp")
    check_eq(
        _point_add(_point_add(Y_SITES[4], (4, 0, 0)), (4, 0, 0)),
        Z_FAR,
        stage,
        "z-far-decomp",
    )

    # 3x3 minor for (rho_0, rho_1, delta) on ((0, s0), (0, s1), (0, delta_(10,0,0)))
    v_cols_3: tuple[Vec, Vec, Vec] = (S0_VEC, S1_VEC, {Z_FAR_ID: Q(1)})
    mat3: tuple[tuple[Q, ...], ...] = (
        tuple(rho_func({}, v)[0] for v in v_cols_3),
        tuple(rho_func({}, v)[1] for v in v_cols_3),
        tuple(delta_func({}, v) for v in v_cols_3),
    )
    check_eq(mat3[0], (Q(4, 5), Q(-1, 5), Q(0)), stage, "mat3-row0")
    check_eq(mat3[1], (Q(-1, 5), Q(4, 5), Q(0)), stage, "mat3-row1")
    check_eq(
        mat3[2],
        (KAPPA_TARGET[0], KAPPA_TARGET[1], Q(-1, 10 * 324 * 324)),
        stage,
        "mat3-row2",
    )
    det3 = det_nxn(mat3)
    check_eq(det3, MINOR_3X3_TARGET, stage, "det3-target")
    check_eq(det3, Q(-3, 5248800), stage, "det3-value")
    check(det3 != 0, stage, "det3-nonzero")

    # 4x4 minor for (rho_0, rho_1, gamma, delta) inserting (0, delta_(6,0,0)) as 3rd column
    v_cols_4: tuple[Vec, Vec, Vec, Vec] = (
        S0_VEC,
        S1_VEC,
        {Z_NEAR_ID: Q(1)},
        {Z_FAR_ID: Q(1)},
    )
    mat4: tuple[tuple[Q, ...], ...] = (
        tuple(rho_func({}, v)[0] for v in v_cols_4),
        tuple(rho_func({}, v)[1] for v in v_cols_4),
        tuple(gamma_func({}, v) for v in v_cols_4),
        tuple(delta_func({}, v) for v in v_cols_4),
    )
    check_eq(mat4[0], (Q(4, 5), Q(-1, 5), Q(0), Q(0)), stage, "mat4-row0")
    check_eq(mat4[1], (Q(-1, 5), Q(4, 5), Q(0), Q(0)), stage, "mat4-row1")
    check_eq(mat4[2][2], Q(-1, 10 * 324), stage, "gamma-znear")
    check_eq(mat4[2][3], Q(0), stage, "gamma-zfar")
    check_eq(mat4[3][3], Q(-1, 10 * 324 * 324), stage, "delta-zfar")
    det4 = det_nxn(mat4)
    check_eq(det4, MINOR_4X4_TARGET, stage, "det4-target")
    check_eq(det4, Q(3, 1698693120000), stage, "det4-value")
    check(det4 != 0, stage, "det4-nonzero")

    # Verify native basis labels (2, 4) -> (1, 0) and (0, 1) -> (0, 1) recover rho_0, rho_1
    # from exact pre-guard work at n=0,1,2 and that Boolean guards separate distinct works.
    check_eq(eta2_from_label((2, 4)), (Q(1), Q(0)), stage, "eta2-basis-0")
    check_eq(eta2_from_label((0, 1)), (Q(0), Q(1)), stage, "eta2-basis-1")

    separation_witnesses = 0
    for col_idx, v_col in enumerate(v_cols_4):
        state = WaveTapeState(u={}, v=v_col)
        cur = state
        for n_step in (0, 1, 2):
            rho_cur = rho_func(cur.u, cur.v)
            for basis_bit, label in enumerate(((2, 4), (0, 1))):
                a_vec = A_op(eta2_from_label(label))
                w_plus = wave_energy_direct(
                    cur.u, vec_add(cur.v, a_vec)
                ) - wave_energy_direct(cur.u, cur.v)
                check_eq(
                    w_plus - Q(2, 5),
                    rho_cur[basis_bit],
                    stage,
                    f"pre-guard-work-recovery-col{col_idx}-n{n_step}-b{basis_bit}",
                )
                # Compare against zero wave when rho_cur[basis_bit] != 0
                if rho_cur[basis_bit] != 0:
                    w_zero = Q(2, 5)
                    b_thresh = min(w_plus, w_zero)
                    check(b_thresh > 0, stage, "positive-threshold")
                    acc_col = 0 <= b_thresh - w_plus <= b_thresh
                    acc_zero = 0 <= b_thresh - w_zero <= b_thresh
                    check(
                        acc_col != acc_zero,
                        stage,
                        f"boolean-guard-separation-col{col_idx}-n{n_step}-b{basis_bit}",
                    )
                    separation_witnesses += 1
            cur = F_step(cur)

    return (
        f"rank_02=3 det3={det3} rank_012=4 det4={det4} "
        f"guard_separations={separation_witnesses}"
    )


def run_stage_far_counterexample_target3() -> str:
    stage = "far_counterexample_target3"
    x_plus = WaveTapeState(u={}, v={Z_FAR_ID: Q(1)})
    x_minus = WaveTapeState(u={}, v={Z_FAR_ID: Q(-1)})

    # Initial equality on (rho, gamma, E_full, all tapes) and opposite delta
    check_eq(rho_func(x_plus.u, x_plus.v), (Q(0), Q(0)), stage, "rho0-plus")
    check_eq(rho_func(x_minus.u, x_minus.v), (Q(0), Q(0)), stage, "rho0-minus")
    check_eq(gamma_func(x_plus.u, x_plus.v), Q(0), stage, "gamma0-plus")
    check_eq(gamma_func(x_minus.u, x_minus.v), Q(0), stage, "gamma0-minus")
    check_eq(full_energy_direct(x_plus), Q(1, 2), stage, "energy0-plus")
    check_eq(full_energy_direct(x_minus), Q(1, 2), stage, "energy0-minus")
    check_eq(delta_func(x_plus.u, x_plus.v), Q(-1, 1049760), stage, "delta0-plus")
    check_eq(delta_func(x_minus.u, x_minus.v), Q(1, 1049760), stage, "delta0-minus")

    # Step 1
    f1_plus = F_step(x_plus)
    f1_minus = F_step(x_minus)
    for tag, st in (("plus", f1_plus), ("minus", f1_minus)):
        check_eq(
            (st.a0, st.a1, st.b0, st.b1),
            (ZERO_PORT,) * 4,
            stage,
            f"tapes1-{tag}",
        )
        check_eq(full_energy_direct(st), Q(1, 2), stage, f"energy1-{tag}")
        check_eq(rho_func(st.u, st.v), (Q(0), Q(0)), stage, f"rho1-{tag}")

    # Step 2
    f2_plus = F_step(f1_plus)
    f2_minus = F_step(f1_minus)
    for tag, st in (("plus", f2_plus), ("minus", f2_minus)):
        check_eq(
            (st.a0, st.a1, st.b0, st.b1),
            (ZERO_PORT,) * 4,
            stage,
            f"tapes2-{tag}",
        )
        check_eq(full_energy_direct(st), Q(1, 2), stage, f"energy2-{tag}")
    check_eq(
        rho_func(f2_plus.u, f2_plus.v),
        (Q(-1, 1049760), Q(-1, 1049760)),
        stage,
        "rho2-plus",
    )
    check_eq(
        rho_func(f2_minus.u, f2_minus.v),
        (Q(1, 1049760), Q(1, 1049760)),
        stage,
        "rho2-minus",
    )

    # Second contact with A(1, 0)^T (label (2, 4)), sigma=+1, B=1, b=1/2
    st_p, w_p, b_p, sig_p, del_p, kind_p = full_contact_step(
        f2_plus, Q(0), Q(1, 2), Q(1), 1, (2, 4)
    )
    st_m, w_m, b_m, sig_m, del_m, kind_m = full_contact_step(
        f2_minus, Q(0), Q(1, 2), Q(1), 1, (2, 4)
    )
    check_eq(kind_p, "pos_work_accept", stage, "far-plus-accepted")
    check_eq(kind_m, "pos_work_accept", stage, "far-minus-accepted")
    check_eq(sig_p, -1, stage, "far-plus-sign")
    check_eq(sig_m, -1, stage, "far-minus-sign")
    check_eq(del_p, Q(419903, 1049760), stage, "far-plus-work")
    check_eq(del_m, Q(419905, 1049760), stage, "far-minus-work")
    check(w_p != w_m, stage, "far-work-distinct")
    check_eq(b_p, Q(104977, 1049760), stage, "far-plus-store")
    check_eq(b_m, Q(104975, 1049760), stage, "far-minus-store")
    check_eq(full_energy_direct(st_p) - w_p, Q(1, 2), stage, "far-plus-conservation")
    check_eq(full_energy_direct(st_m) - w_m, Q(1, 2), stage, "far-minus-conservation")

    # Near witness audit at (6, 0, 0)
    near_plus = WaveTapeState(u={}, v={Z_NEAR_ID: Q(1)})
    near_minus = WaveTapeState(u={}, v={Z_NEAR_ID: Q(-1)})
    check_eq(rho_func(near_plus.u, near_plus.v), (Q(0), Q(0)), stage, "near-rho0-plus")
    check_eq(gamma_func(near_plus.u, near_plus.v), Q(-1, 3240), stage, "near-gamma0-plus")
    check_eq(gamma_func(near_minus.u, near_minus.v), Q(1, 3240), stage, "near-gamma0-minus")
    f1_near_plus = F_step(near_plus)
    f1_near_minus = F_step(near_minus)
    check_eq(
        rho_func(f1_near_plus.u, f1_near_plus.v),
        (Q(-1, 3240), Q(-1, 3240)),
        stage,
        "near-rho1-plus",
    )
    check_eq(
        rho_func(f1_near_minus.u, f1_near_minus.v),
        (Q(1, 3240), Q(1, 3240)),
        stage,
        "near-rho1-minus",
    )

    return (
        f"far_rho2_plus={rho_func(f2_plus.u, f2_plus.v)[0]} "
        f"far_work_plus={w_p} far_work_minus={w_m} "
        f"near_rho1_plus={rho_func(f1_near_plus.u, f1_near_plus.v)[0]}"
    )


def _build_audit_states() -> list[tuple[str, WaveTapeState]]:
    occ_u1 = vec_add(
        {PORT_IDS[0]: Q(1, 10)},
        {Y4_ID: Q(1, 5)},
        {Z_NEAR_ID: Q(1, 3)},
    )
    occ_v1 = vec_add(
        vec_scale(S0_VEC, Q(3, 4)),
        vec_scale(S1_VEC, Q(-1, 4)),
        {Z_FAR_ID: Q(1, 7)},
    )
    occ_u2 = vec_add(
        {PORT_IDS[1]: Q(-1, 10)},
        {PORT_IDS[3]: Q(1, 4)},
        {Z_NEAR_ID: Q(-1, 5)},
    )
    occ_v2 = vec_add(
        vec_scale(S0_VEC, Q(1, 4)),
        vec_scale(S1_VEC, Q(-3, 4)),
        {Z_FAR_ID: Q(-1, 9)},
    )
    waves: tuple[tuple[str, Vec, Vec], ...] = (
        ("far_plus", {}, {Z_FAR_ID: Q(1)}),
        ("far_minus", {}, {Z_FAR_ID: Q(-1)}),
        ("zero", {}, {}),
        ("occ_mix_1", occ_u1, occ_v1),
        ("occ_mix_2", occ_u2, occ_v2),
    )
    tape_options: tuple[tuple[str, tuple[Port, Port, Port, Port]], ...] = (
        ("tape_zero", (ZERO_PORT, ZERO_PORT, ZERO_PORT, ZERO_PORT)),
        (
            "tape_nonzero",
            (
                (Q(1, 3), Q(-1, 5), Q(1, 7), Q(0)),
                (Q(-1, 2), Q(1, 4), Q(0), Q(1, 3)),
                (Q(1, 5), Q(0), Q(-1, 3), Q(1, 2)),
                (Q(0), Q(1, 6), Q(-1, 4), Q(1, 5)),
            ),
        ),
    )
    states: list[tuple[str, WaveTapeState]] = []
    for w_name, u_vec, v_vec in waves:
        for t_name, (a0, a1, b0, b1) in tape_options:
            states.append(
                (
                    f"{w_name}:{t_name}",
                    WaveTapeState(u=u_vec, v=v_vec, a0=a0, a1=a1, b0=b0, b1=b1),
                )
            )
    return states


def run_stage_finite_contact_predictor_target4() -> str:
    stage = "finite_contact_predictor_target4"

    # 1. Complete 50 signed-source update rows and 70500 wave-work coefficients
    coeff_total = 0
    const_total = 0
    for label in ALL_LABELS:
        eta2 = eta2_from_label(label)
        a_vec = A_op(eta2)
        la_vec = LD_op(a_vec)
        ha_vec = H_op(a_vec)
        g_eta = mat2_vec2(G_TARGET, eta2)
        k_eta = vec2_dot(KAPPA_TARGET, eta2)
        for sigma in (-1, 1):
            cold = wave_energy_direct({}, vec_scale(a_vec, sigma))
            check_eq(
                cold,
                vec2_dot(eta2, g_eta) / 2,
                stage,
                f"cold-work-{label}-{sigma}",
            )
            const_total += 1
            check_eq(
                rho_func({}, vec_scale(a_vec, sigma)),
                (sigma * g_eta[0], sigma * g_eta[1]),
                stage,
                f"rho-shift-{label}-{sigma}",
            )
            check_eq(
                delta_func({}, vec_scale(a_vec, sigma)),
                sigma * k_eta,
                stage,
                f"delta-shift-{label}-{sigma}",
            )
            for i in range(len(D)):
                u_coeff_dir = sigma * (
                    la_vec.get(i, Q(0)) / 2 - a_vec.get(i, Q(0))
                )
                u_coeff_red = -sigma * ha_vec.get(i, Q(0)) / 2
                check_eq(
                    u_coeff_dir,
                    u_coeff_red,
                    stage,
                    f"u-coeff-{label}-{sigma}-{i}",
                )
                v_coeff_dir = sigma * a_vec.get(i, Q(0))
                v_coeff_red = sigma * (
                    eta2[0] * S0_VEC.get(i, Q(0))
                    + eta2[1] * S1_VEC.get(i, Q(0))
                )
                check_eq(
                    v_coeff_dir,
                    v_coeff_red,
                    stage,
                    f"v-coeff-{label}-{sigma}-{i}",
                )
                coeff_total += 2

    check_eq(const_total, 50, stage, "const-total-50")
    check_eq(coeff_total, 70500, stage, "coeff-total-70500")

    # 2. 2000 single-contact guarded cases:
    #    10 states (5 waves x 2 tapes) x 25 labels x 2 signs x 4 battery stocks = 2000
    states = _build_audit_states()
    check_eq(len(states), 10, stage, "ten-states")
    stocks: tuple[tuple[Q, Q], ...] = (
        (Q(0), Q(0)),
        (Q(1, 2), Q(1)),
        (Q(4, 5), Q(4, 5)),
        (Q(2), Q(4)),
    )
    single_count = 0
    single_kinds: Counter[str] = Counter()
    single_signs: Counter[int] = Counter()

    for state_name, st0 in states:
        e0 = full_energy_direct(st0)
        xi0 = xi_func(st0.u, st0.v)
        for label in ALL_LABELS:
            for sigma in (-1, 1):
                for b_init, cap in stocks:
                    single_count += 1
                    w_init = Q(3, 11)
                    st1, w1, b1, sig1, del_dir, kind_dir = full_contact_step(
                        st0, w_init, b_init, cap, sigma, label
                    )
                    xi1, w1_red, b1_red, sig1_red, del_red, kind_red = (
                        reduced_single_contact_step(
                            xi0, w_init, b_init, cap, sigma, label
                        )
                    )
                    ctx = f"single-{state_name}-{label}-{sigma}-{b_init}/{cap}"
                    check_eq(del_red, del_dir, stage, f"delta-{ctx}")
                    check_eq(kind_red, kind_dir, stage, f"kind-{ctx}")
                    check_eq((w1_red, b1_red, sig1_red), (w1, b1, sig1), stage, f"spectators-{ctx}")
                    check_eq(xi_func(st1.u, st1.v), xi1, stage, f"xi-after-{ctx}")

                    # Energy and store conservation + involution
                    e1 = full_energy_direct(st1)
                    check_eq(e1 - w1, e0 - w_init, stage, f"energy-minus-work-{ctx}")
                    check_eq(e1 + b1, e0 + b_init, stage, f"energy-plus-store-{ctx}")
                    check_eq(w1 + b1, w_init + b_init, stage, f"work-plus-store-{ctx}")
                    st_back, w_back, b_back, sig_back, _, _ = full_contact_step(
                        st1, w1, b1, cap, sig1, label
                    )
                    check_eq(
                        (st_back, w_back, b_back, sig_back),
                        (st0, w_init, b_init, sigma),
                        stage,
                        f"involution-{ctx}",
                    )
                    if kind_dir in ("lower_refusal", "upper_refusal"):
                        check_eq(st1, st0, stage, f"refusal-identity-{ctx}")
                    single_kinds[kind_dir] += 1
                    single_signs[sigma] += 1

    check_eq(single_count, 2000, stage, "single-contact-2000")
    for req_kind in (
        "zero_cost_accept",
        "pos_work_accept",
        "neg_work_accept",
        "lower_refusal",
        "upper_refusal",
    ):
        check(
            single_kinds[req_kind] > 0,
            stage,
            f"missing-single-kind-{req_kind}",
        )
    check_eq(single_signs[-1], 1000, stage, "single-sign-minus")
    check_eq(single_signs[1], 1000, stage, "single-sign-plus")

    # 3. 480 two-contact guarded cases:
    #    10 states x 4 source pairs x 4 sign pairs x 3 stocks = 480
    source_pairs: tuple[tuple[tuple[int, int], tuple[int, int]], ...] = (
        ((0, 3), (2, 4)),
        ((2, 4), (0, 1)),
        ((1, 4), (0, 0)),
        ((2, 1), (3, 2)),
    )
    sign_pairs: tuple[tuple[int, int], ...] = (
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    )
    two_stocks = stocks[:3]
    two_count = 0
    two_kinds: Counter[str] = Counter()
    two_branches: Counter[str] = Counter()

    for state_name, st0 in states:
        e0 = full_energy_direct(st0)
        xi0 = xi_func(st0.u, st0.v)
        for label1, label2 in source_pairs:
            for sigma1, sigma2 in sign_pairs:
                for b_init, cap in two_stocks:
                    two_count += 1
                    w_init = Q(0)
                    ctx = (
                        f"two-{state_name}-{label1}-{label2}-"
                        f"{sigma1},{sigma2}-{b_init}/{cap}"
                    )

                    # Full 1426-coordinate simulation: Contact 1 -> F -> F -> Contact 2
                    st1, w1, b1, sig1_after, del1_dir, kind1_dir = full_contact_step(
                        st0, w_init, b_init, cap, sigma1, label1
                    )
                    e1 = full_energy_direct(st1)
                    check_eq(e1 - w1, e0, stage, f"e1-conservation-{ctx}")
                    f1_st = F_step(st1)
                    f2_st = F_step(f1_st)
                    check_eq(full_energy_direct(f1_st), e1, stage, f"f1-energy-{ctx}")
                    check_eq(full_energy_direct(f2_st), e1, stage, f"f2-energy-{ctx}")
                    rho2_actual = rho_func(f2_st.u, f2_st.v)

                    st2, w2, b2, sig2_after, del2_dir, kind2_dir = full_contact_step(
                        f2_st, w1, b1, cap, sigma2, label2
                    )
                    e2 = full_energy_direct(st2)
                    check_eq(e2 - w2, e0, stage, f"e2-conservation-{ctx}")
                    check_eq(e2 + b2, e0 + b_init, stage, f"e2-joint-store-{ctx}")
                    check_eq(w2 + b2, b_init, stage, f"w2-plus-b2-{ctx}")
                    rho2_after_actual = rho_func(st2.u, st2.v)

                    # Reduced 3-coordinate predictor from (xi0, a0, a1) and spectators
                    pred = reduced_two_contact_predict(
                        xi0=xi0,
                        a0=st0.a0,
                        a1=st0.a1,
                        work0=w_init,
                        battery0=b_init,
                        capacity=cap,
                        label1=label1,
                        sigma1=sigma1,
                        label2=label2,
                        sigma2=sigma2,
                    )
                    check_eq(pred["delta1"], del1_dir, stage, f"pred-delta1-{ctx}")
                    check_eq(pred["kind1"], kind1_dir, stage, f"pred-kind1-{ctx}")
                    check_eq(pred["rho2"], rho2_actual, stage, f"pred-rho2-{ctx}")
                    check_eq(pred["delta2"], del2_dir, stage, f"pred-delta2-{ctx}")
                    check_eq(pred["kind2"], kind2_dir, stage, f"pred-kind2-{ctx}")
                    check_eq(
                        pred["rho2_after"],
                        rho2_after_actual,
                        stage,
                        f"pred-rho2-after-{ctx}",
                    )
                    check_eq(pred["work"], w2, stage, f"pred-work-{ctx}")
                    check_eq(pred["battery"], b2, stage, f"pred-battery-{ctx}")
                    check_eq(
                        pred["signs"],
                        (sig1_after, sig2_after),
                        stage,
                        f"pred-signs-{ctx}",
                    )

                    two_kinds[kind1_dir] += 1
                    two_kinds[kind2_dir] += 1
                    b_tag = (
                        ("A" if sig1_after == -sigma1 else "R")
                        + ("A" if sig2_after == -sigma2 else "R")
                    )
                    two_branches[b_tag] += 1

    check_eq(two_count, 480, stage, "two-contact-480")
    for req_kind in (
        "zero_cost_accept",
        "pos_work_accept",
        "neg_work_accept",
        "lower_refusal",
        "upper_refusal",
    ):
        check(
            two_kinds[req_kind] > 0,
            stage,
            f"missing-two-kind-{req_kind}",
        )
    for branch_code in ("AA", "AR", "RA", "RR"):
        check(
            two_branches[branch_code] > 0,
            stage,
            f"missing-two-branch-{branch_code}",
        )

    return (
        f"single_cases={single_count} two_cases={two_count} "
        f"single_ZeroPosNegLowUp={single_kinds['zero_cost_accept']},"
        f"{single_kinds['pos_work_accept']},{single_kinds['neg_work_accept']},"
        f"{single_kinds['lower_refusal']},{single_kinds['upper_refusal']} "
        f"two_AA_AR_RA_RR={two_branches['AA']},{two_branches['AR']},"
        f"{two_branches['RA']},{two_branches['RR']}"
    )


STAGE_RUNNERS = {
    "custody": run_stage_custody,
    "geometry_and_operators": run_stage_geometry_and_operators,
    "refresh_identities_target1": run_stage_refresh_identities_target1,
    "rank_minors_and_criteria_target2": run_stage_rank_minors_and_criteria_target2,
    "far_counterexample_target3": run_stage_far_counterexample_target3,
    "finite_contact_predictor_target4": run_stage_finite_contact_predictor_target4,
}


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(newline="\n")
    print(f"PROBE {PROBE_ID}")
    print("SCOPE PUBLIC NON-CANONICAL L1 independent-code-audit")
    for idx, stage in enumerate(STAGE_ORDER):
        try:
            summary = STAGE_RUNNERS[stage]()
        except ExactAuditFailure as exc:
            print(f"STAGE {stage} FAIL {exc.message}")
            for rem in STAGE_ORDER[idx + 1 :]:
                print(f"STAGE {rem} NOT_RUN")
            print("VERDICT SCIENTIFIC_FAIL")
            return 0
        print(f"STAGE {stage} PASS {summary}")
    print("VERDICT PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
