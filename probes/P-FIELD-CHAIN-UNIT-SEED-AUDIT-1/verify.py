#!/usr/bin/env python3
"""Independent exact verifier for P-FIELD-CHAIN-UNIT-SEED-AUDIT-1 (v103 lane RB)."""

from __future__ import annotations

import math
from typing import Dict, List, Tuple

Vec4 = Tuple[int, int, int, int]
Mat4 = Tuple[Vec4, Vec4, Vec4, Vec4]

A_F: Mat4 = (
    (1, 0, 1, 0),
    (0, 1, 0, 1),
    (-2, 1, -1, 1),
    (1, -3, 1, -2),
)

B_F: Mat4 = (
    (4, -2, 2, -1),
    (-2, 6, -1, 3),
    (2, -1, 2, 0),
    (-1, 3, 0, 2),
)

L_MAT: Mat4 = (
    (1, -3, -1, -2),
    (-3, 4, -2, 1),
    (0, 5, 1, 2),
    (5, -5, 2, -1),
)

V_INV: Mat4 = (
    (1, 2, 1, 2),
    (2, -1, 2, -1),
    (0, -5, 1, -3),
    (-5, 5, -3, 4),
)

ADJ_B_F: Mat4 = (
    (4, 2, -3, -1),
    (2, 6, 1, -8),
    (-3, 1, 10, -3),
    (-1, -8, -3, 20),
)

I4: Mat4 = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
)

Z4_MAT: Mat4 = (
    (0, 0, 0, 0),
    (0, 0, 0, 0),
    (0, 0, 0, 0),
    (0, 0, 0, 0),
)

YBAR3: Vec4 = (0, 0, 3, 1)
USTAR_TARGET: Vec4 = (0, -1, -1, 2)
L_USTAR_TARGET: Vec4 = (0, 0, -2, 1)


def mat_add(a: Mat4, b: Mat4, scale_b: int = 1) -> Mat4:
    return tuple(
        tuple(a[i][j] + scale_b * b[i][j] for j in range(4))
        for i in range(4)
    )  # type: ignore[return-value]


def mat_scale(c: int, a: Mat4) -> Mat4:
    return tuple(tuple(c * a[i][j] for j in range(4)) for i in range(4))  # type: ignore[return-value]


def mat_mul(a: Mat4, b: Mat4) -> Mat4:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4))
        for i in range(4)
    )  # type: ignore[return-value]


def mat_transpose(a: Mat4) -> Mat4:
    return tuple(tuple(a[j][i] for j in range(4)) for i in range(4))  # type: ignore[return-value]


def mat_pow(a: Mat4, n: int) -> Mat4:
    res = I4
    for _ in range(n):
        res = mat_mul(res, a)
    return res


def mat_vec(a: Mat4, v: Vec4) -> Vec4:
    return tuple(sum(a[i][j] * v[j] for j in range(4)) for i in range(4))  # type: ignore[return-value]


def vec_mod5(v: Vec4) -> Vec4:
    return (v[0] % 5, v[1] % 5, v[2] % 5, v[3] % 5)


def det4(m: Mat4) -> int:
    from itertools import permutations

    total = 0
    for p in permutations(range(4)):
        inv = sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j])
        sign = -1 if (inv % 2) else 1
        prod = 1
        for i in range(4):
            prod *= m[i][p[i]]
        total += sign * prod
    return total


def h_quad(y: Vec4) -> int:
    a, b, c, d = y
    num = sum(y[i] * B_F[i][j] * y[j] for i in range(4) for j in range(4))
    assert num % 2 == 0
    h1 = num // 2
    h2 = (
        2 * a * a
        - 2 * a * b
        + 3 * b * b
        + c * c
        + d * d
        + 2 * a * c
        - a * d
        - b * c
        + 3 * b * d
    )
    assert h1 == h2
    return h1


def h_schur_4x(y: Vec4) -> int:
    a, b, c, d = y
    q_ab = 3 * a * a + 2 * a * b + 2 * b * b
    s1 = 2 * c + 2 * a - b
    s2 = 2 * d - a + 3 * b
    return q_ab + s1 * s1 + s2 * s2


def verify_algebraic_identities() -> None:
    # 1. Cyclotomic and invariance identities for A_f and B_f
    assert mat_pow(A_F, 5) == I4
    cyc_sum = Z4_MAT
    for k in range(5):
        cyc_sum = mat_add(cyc_sum, mat_pow(A_F, k))
    assert cyc_sum == Z4_MAT
    assert mat_mul(mat_transpose(A_F), mat_mul(B_F, A_F)) == B_F

    # 2. Determinant and adjugate of B_f (5 * B_f^-1)
    assert det4(B_F) == 5
    assert mat_mul(B_F, ADJ_B_F) == mat_scale(5, I4)
    assert mat_mul(ADJ_B_F, B_F) == mat_scale(5, I4)
    diag_adj = tuple(ADJ_B_F[i][i] for i in range(4))
    assert diag_adj == (4, 6, 10, 20)

    # 3. Chain operator L and V_inv = 5 * L^-1 identities
    i_minus_af = mat_add(I4, A_F, -1)
    i_minus_af2 = mat_add(I4, mat_pow(A_F, 2), -1)
    assert mat_mul(i_minus_af, i_minus_af2) == L_MAT
    assert mat_mul(A_F, L_MAT) == mat_mul(L_MAT, A_F)
    assert mat_mul(L_MAT, L_MAT) == mat_scale(5, mat_pow(A_F, 3))
    assert V_INV == mat_mul(mat_pow(A_F, 2), L_MAT)
    assert mat_mul(V_INV, L_MAT) == mat_scale(5, I4)
    assert mat_mul(L_MAT, V_INV) == mat_scale(5, I4)
    assert det4(L_MAT) == 25
    assert mat_mul(mat_transpose(L_MAT), mat_mul(B_F, L_MAT)) == mat_scale(5, B_F)

    # 4. Exact polynomial identity check via evaluation on complete degree-2 grid [-1,1]^4
    for a in (-1, 0, 1):
        for b in (-1, 0, 1):
            q_ab = 3 * a * a + 2 * a * b + 2 * b * b
            assert 2 * q_ab == 5 * a * a + (a + 2 * b) ** 2
            assert 3 * q_ab == 5 * b * b + (3 * a + b) ** 2
            for c in (-1, 0, 1):
                for d in (-1, 0, 1):
                    y = (a, b, c, d)
                    assert 4 * h_quad(y) == h_schur_4x(y)
                    assert h_quad(mat_vec(L_MAT, y)) == 5 * h_quad(y)


def adjugate_box_bounds(k: int) -> Tuple[int, int, int, int]:
    # From 5*a^2 <= 8k, 5*b^2 <= 12k, c^2 <= 4k, d^2 <= 8k
    return (
        math.isqrt((8 * k) // 5),
        math.isqrt((12 * k) // 5),
        math.isqrt(4 * k),
        math.isqrt(8 * k),
    )


def solve_units_via_schur_fibers() -> List[Vec4]:
    units: List[Vec4] = []
    # 5a^2 <= 8 => |a| <= 1; 5b^2 <= 12 => |b| <= 1
    for a in range(-1, 2):
        for b in range(-1, 2):
            q_ab = 3 * a * a + 2 * a * b + 2 * b * b
            rem = 4 - q_ab
            if rem < 0:
                continue
            lim = math.isqrt(rem)
            for s1 in range(-lim, lim + 1):
                for s2 in range(-lim, lim + 1):
                    if s1 * s1 + s2 * s2 != rem:
                        continue
                    num_c = s1 - 2 * a + b
                    num_d = s2 + a - 3 * b
                    if num_c % 2 == 0 and num_d % 2 == 0:
                        u = (a, b, num_c // 2, num_d // 2)
                        assert h_quad(u) == 1
                        units.append(u)
    units.sort()
    return units


def enumerate_shell_adjugate_box(k: int) -> Tuple[Dict[int, List[Vec4]], int]:
    ba, bb, bc, bd = adjugate_box_bounds(k)
    shells: Dict[int, List[Vec4]] = {j: [] for j in range(k + 1)}
    scanned = 0
    for a in range(-ba, ba + 1):
        for b in range(-bb, bb + 1):
            for c in range(-bc, bc + 1):
                for d in range(-bd, bd + 1):
                    scanned += 1
                    y = (a, b, c, d)
                    h = h_quad(y)
                    if h == 0:
                        assert y == (0, 0, 0, 0)
                    assert h >= 0
                    if h <= k:
                        shells[h].append(y)
    for j in shells:
        shells[j].sort()
    return shells, scanned


def main() -> None:
    verify_algebraic_identities()

    # R1: Unit classification by Schur fiber solver and adjugate box scan
    units_fiber = solve_units_via_schur_fibers()
    shells_k1, scanned_k1 = enumerate_shell_adjugate_box(1)
    assert scanned_k1 == 3 * 3 * 5 * 5 == 225
    assert shells_k1[0] == [(0, 0, 0, 0)]
    assert shells_k1[1] == units_fiber

    # Cross-check against the k <= 5 adjugate box [-2,2]x[-3,3]x[-4,4]x[-6,6]
    shells_k5, scanned_k5 = enumerate_shell_adjugate_box(5)
    assert adjugate_box_bounds(5) == (2, 3, 4, 6)
    assert scanned_k5 == 5 * 7 * 9 * 13 == 4095
    assert shells_k5[1] == units_fiber
    shell_counts_0_to_5 = tuple(len(shells_k5[j]) for j in range(6))

    # R2: Gate residue group G_25, unipotent A_f action, and unit residue mapping
    f5_all = [
        (r0, r1, r2, r3)
        for r0 in range(5)
        for r1 in range(5)
        for r2 in range(5)
        for r3 in range(5)
    ]
    g25_criterion = sorted(
        r for r in f5_all if (r[0] + 2 * r[1]) % 5 == 0 and (r[2] + 2 * r[3]) % 5 == 0
    )
    g25_image = sorted({vec_mod5(mat_vec(L_MAT, x)) for x in f5_all})
    g25_param = sorted(
        ((3 * r1) % 5, r1, (3 * r3) % 5, r3) for r1 in range(5) for r3 in range(5)
    )
    assert len(g25_criterion) == 25
    assert g25_criterion == g25_image == g25_param

    # Verify kernel of x -> Lx mod 5 on F_5^4 has size 25 and equals image of L mod 5
    ker_l_mod5 = sorted(x for x in f5_all if vec_mod5(mat_vec(L_MAT, x)) == (0, 0, 0, 0))
    assert len(ker_l_mod5) == 25
    assert ker_l_mod5 == g25_criterion

    # Verify unipotent shear action of A_f mod 5 on G_25 and fixed subgroup G_25^{A_f}
    af_fixed_g25: List[Vec4] = []
    for r in g25_criterion:
        r1, r3 = r[1], r[3]
        af_r = vec_mod5(mat_vec(A_F, r))
        expected_af_r = ((3 * (r1 + r3)) % 5, (r1 + r3) % 5, (3 * r3) % 5, r3)
        assert af_r == expected_af_r
        if af_r == r:
            af_fixed_g25.append(r)
    af_fixed_g25.sort()
    assert len(af_fixed_g25) == 5
    assert af_fixed_g25 == sorted(((3 * r1) % 5, r1, 0, 0) for r1 in range(5))

    # Map all 20 unit seeds into G_25
    residue_to_units: Dict[Vec4, List[Vec4]] = {r: [] for r in g25_criterion}
    for u in units_fiber:
        lu_mod5 = vec_mod5(mat_vec(L_MAT, u))
        assert lu_mod5 in residue_to_units
        residue_to_units[lu_mod5].append(u)

    covered_residues = sorted(r for r, us in residue_to_units.items() if len(us) > 0)
    missing_residues = sorted(r for r, us in residue_to_units.items() if len(us) == 0)
    max_unit_mult = max(len(us) for us in residue_to_units.values())
    assert missing_residues == af_fixed_g25

    # Check shell k=2 attainment of the 4 nonzero missing gate residues
    k2_missing_hits: Dict[Vec4, List[Vec4]] = {r: [] for r in missing_residues if r != (0, 0, 0, 0)}
    for x in shells_k5[2]:
        rx = vec_mod5(mat_vec(L_MAT, x))
        if rx in k2_missing_hits:
            k2_missing_hits[rx].append(x)

    # R3: Coset minimum and preimages for ybar3 = (0, 0, 3, 1) across shells k=1..5
    ybar3_by_shell: Dict[int, List[Tuple[Vec4, Vec4, int]]] = {}
    for k in range(1, 6):
        hits: List[Tuple[Vec4, Vec4, int]] = []
        for x in shells_k5[k]:
            lx = mat_vec(L_MAT, x)
            if vec_mod5(lx) == YBAR3:
                hy = h_quad(lx)
                assert hy == 5 * k
                hits.append((x, lx, hy))
        ybar3_by_shell[k] = hits

    least_k = next((k for k in range(1, 6) if ybar3_by_shell[k]), None)
    assert least_k is not None
    min_hits = ybar3_by_shell[least_k]

    print("PROBE=P-FIELD-CHAIN-UNIT-SEED-AUDIT-1")
    print("PREMISE_IDENTITIES=PASS")
    print(f"DET_BF={det4(B_F)} ADJ_BF_DIAG={ tuple(ADJ_B_F[i][i] for i in range(4)) }")
    print(f"K1_ADJUGATE_BOX={adjugate_box_bounds(1)} K1_SCANNED={scanned_k1}")
    print(f"K5_ADJUGATE_BOX={adjugate_box_bounds(5)} K5_SCANNED={scanned_k5}")
    print(f"SHELL_COUNTS_0_TO_5={shell_counts_0_to_5} TOTAL_LE_5={sum(shell_counts_0_to_5)}")
    print(f"UNIT_COUNT={len(units_fiber)} DISTINCT_UNIT_RESIDUES={len(covered_residues)} MAX_UNIT_MULT={max_unit_mult}")
    print(f"MISSING_GATE_RESIDUE_COUNT={len(missing_residues)} EQUALS_AF_FIXED_SUBGROUP={missing_residues == af_fixed_g25}")
    print("MISSING_GATE_RESIDUES=" + ",".join(str(r).replace(" ", "") for r in missing_residues))
    print(
        "NONZERO_MISSING_K2_MULTS="
        + ",".join(f"{str(r).replace(' ', '')}:{len(k2_missing_hits[r])}" for r in sorted(k2_missing_hits))
    )
    print("UNITS_AND_LU_MOD5_BEGIN")
    for idx, u in enumerate(units_fiber, 1):
        lu = mat_vec(L_MAT, u)
        lu_m5 = vec_mod5(lu)
        print(
            f"  U{idx:02d} u={str(u).replace(' ', '')} "
            f"Lu={str(lu).replace(' ', '')} "
            f"Lu_mod5={str(lu_m5).replace(' ', '')} "
            f"H(u)={h_quad(u)} H(Lu)={h_quad(lu)}"
        )
    print("UNITS_AND_LU_MOD5_END")
    print(
        f"YBAR3={str(YBAR3).replace(' ', '')} "
        f"LEAST_SHELL_K={least_k} "
        f"COSET_MIN_H={5 * least_k} "
        f"MINIMIZER_COUNT={len(min_hits)}"
    )
    for x, lx, hy in min_hits:
        print(
            f"  MINIMIZER x={str(x).replace(' ', '')} "
            f"y=Lx={str(lx).replace(' ', '')} "
            f"H(x)={h_quad(x)} H(y)={hy} "
            f"MATCHES_USTAR={x == USTAR_TARGET and lx == L_USTAR_TARGET}"
        )
    print(
        "YBAR3_SHELL_COUNTS_K1_TO_K5="
        + ",".join(f"k{k}:{len(ybar3_by_shell[k])}" for k in range(1, 6))
    )
    print("AUDIT_VERIFIER_STATUS=PASS")


if __name__ == "__main__":
    main()
