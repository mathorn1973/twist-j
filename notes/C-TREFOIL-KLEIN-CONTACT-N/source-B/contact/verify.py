#!/usr/bin/env python3
"""Exact certificates C0--C4 for the frozen contact-meridian note.

NON-CANONICAL, L1. Standard library only; no network, randomness, floats,
imports of another implementation, or output files. Operation products act
right to left; literal contact lists are chronological. This source must be
pinned with all other implementations before its first scientific execution.

Definitions: public Canon dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d;
CONTACT-RECORD as used at 03390dca1c0a69ab8989f0daada0810c9956791a.
"""

import hashlib
from itertools import permutations, product
import json
from pathlib import Path
import sys


F5 = range(5)
LETTERS = ("a", "b", "c", "d", "e", "U")
PREREG_SHA256 = "5061341dd53c3814ef87293b4a5d361600b123f53ac1892bd25005bb46b5640f"
FREEZE_SHA256 = "7b6475aba1f5a4a48de043c7b7b6f7f6d6cb1432fee5389dd9620f5e6e521861"
FROZEN_FILES = {
    "PREREG.md": PREREG_SHA256,
    "contact/CONTRACTS.md": "a59c01fae3fda515c430156b3c35700158dc01b72106bdb4fad5822e7939a7e7",
    "contact/PROOF.md": "fe33a9e87ed500feb7ece6d6ef6cb49ef950fb98d2633116e730b582059ab3cf",
    "geometry/PREREG_CONTRACT_DRAFT.md": "2677add0d957bddb190e73362afddbcab73aaf2d5f80a52b69d48d38a5d42dde",
    "geometry/PROOF.md": "a52eadca5c21565224b77493b496554ed7d79387daa02b76b952cc163f67e4de",
}

P = (
    (0, 2, 1, 3, 4),
    (0, 1, 2, 3, 4),
    (2, 1, 0, 3, 4),
    (1, 0, 2, 3, 4),
    (1, 0, 2, 3, 4),
)
N_EXPECTED = (
    (0, 4, 2, 3, 1),
    (0, 1, 2, 3, 4),
    (4, 1, 2, 3, 0),
    (1, 0, 2, 3, 4),
    (1, 0, 2, 3, 4),
)
CHECKS = 0
REPORTS = []


class CheckFailure(Exception):
    def __init__(self, label, detail=None):
        super().__init__(label)
        self.label = label
        self.detail = detail


def require(condition, label, detail=None):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise CheckFailure(label, detail)


def emit(value):
    print(json.dumps(value, sort_keys=True, separators=(",", ":")))


def report(section, start, **values):
    row = {"section": section, "status": "PASS", "checks": CHECKS - start}
    row.update(values)
    REPORTS.append(row)
    emit(row)


def basis(n):
    return ((0,) * n,) + tuple(
        tuple(int(i == j) for i in range(n)) for j in range(n)
    )


def native(letter, cell):
    """Literal original six-coordinate maps, before any endpoint reduction."""
    p1, p4, p1p, p4p, q, r = cell
    if letter == "a":
        out = (p4, p1, p4p, p1p, q, r)
    elif letter == "b":
        out = (-p1p, -p4p, -p1, -p4, -q, -r)
    elif letter == "c":
        out = (-p1p + 2, -p4p + 1 + r, -p1 + 2, -p4 + 1 - r, 1 - q, -r)
    elif letter == "d":
        out = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 1 - q, 1 - r)
    elif letter == "e":
        out = (2 - p1, 1 - p4, 3 - p1p, 4 - p4p, 2 - q, 1 - r)
    else:
        raise ValueError("unknown original native letter")
    return tuple(value % 5 for value in out)


def ucal(cell):
    """Literal conditional swap; the endpoint table P is not used here."""
    q, r = cell[4:]
    pair = ((1, 2), None, (0, 2), (0, 1), (0, 1))[q]
    if pair is None:
        changed = r
    elif r == pair[0]:
        changed = pair[1]
    elif r == pair[1]:
        changed = pair[0]
    else:
        changed = r
    return cell[:5] + (changed,)


def apply_letter(letter, cell):
    return ucal(cell) if letter == "U" else native(letter, cell)


def word_cell(cell, word):
    for letter in word:
        cell = apply_letter(letter, cell)
    return cell


def iterate(function, state, count):
    for _ in range(count):
        state = function(state)
    return state


def check_custody():
    start = CHECKS
    root = Path(__file__).resolve().parents[1]
    freeze_bytes = (root / "FREEZE.json").read_bytes()
    require(hashlib.sha256(freeze_bytes).hexdigest() == FREEZE_SHA256,
            "C0_frozen_manifest_bytes")
    manifest = json.loads(freeze_bytes)
    require(manifest["files"] == FROZEN_FILES, "C0_manifest_exact_file_set")
    for relative, expected in sorted(FROZEN_FILES.items()):
        actual = hashlib.sha256((root / relative).read_bytes()).hexdigest()
        require(actual == expected, "C0_accepted_file_bytes", relative)
    report("C0", start, prereg_sha256=PREREG_SHA256,
           freeze_sha256=FREEZE_SHA256, accepted_files=len(FROZEN_FILES))


def reduced_c(qr):
    qx, qy, rx, ry = qr
    return qx, qy, P[qx][rx], P[qy][ry]


def reduced_k(side, delta, qr):
    out = list(qr)
    out[side] = (out[side] + 3 * delta) % 5
    return tuple(out)


def reduced_a(side, delta, qr):
    out = list(qr)
    old_q = out[side]
    new_q = (old_q + 3 * delta) % 5
    out[side] = new_q
    out[side + 2] = P[new_q][P[old_q][out[side + 2]]]
    return tuple(out)


def pair_cell(state, side):
    return state[4 * side:4 * side + 4] + (state[8 + side], state[10 + side])


def replace_pair_cell(state, side, cell):
    out = list(state)
    out[4 * side:4 * side + 4] = cell[:4]
    out[8 + side], out[10 + side] = cell[4:]
    return tuple(out)


def mixed_h(state):
    a, b, c, d = state[:4]
    e, f, g, k = state[4:8]
    return (3 * (a * k + d * e) + 2 * (b * g + c * f)) % 5


def pair_leaf(state, leaf):
    """Literal complete W_b and native leaves; all 13 coordinates retained."""
    if leaf == "W":
        value = mixed_h(state)
        if value == 0:
            return state
        sigma = int(value in (3, 4))
        out = state
        if sigma != state[12]:
            out = replace_pair_cell(out, 0, native("b", pair_cell(out, 0)))
            out = replace_pair_cell(out, 1, native("b", pair_cell(out, 1)))
        return out[:12] + (sigma,)
    letter, side_name = leaf
    side = 0 if side_name == "x" else 1
    return replace_pair_cell(state, side, apply_letter(letter, pair_cell(state, side)))


def reader_word(side):
    return ("U" + side, "e" + side, "d" + side, "W", "bx", "by", "W",
            "d" + side, "e" + side, "W", "by", "bx", "W", "U" + side)


def literal_reader(state, side):
    for leaf in reader_word(side):
        state = pair_leaf(state, leaf)
    return state


def check_completed_contacts():
    start = CHECKS
    rows = 0
    for delta in (0, 1):
        for qr in product(F5, repeat=4):
            ax = lambda state: reduced_a(0, delta, state)
            ay = lambda state: reduced_a(1, delta, state)
            require(reduced_c(reduced_c(qr)) == qr, "C1_common_conjugator_involution", (delta, qr))
            require(iterate(ax, qr, 5) == qr, "C1_Ax_fifth_power", (delta, qr))
            require(iterate(ay, qr, 5) == qr, "C1_Ay_fifth_power", (delta, qr))
            require(ax(ay(qr)) == ay(ax(qr)), "C1_completed_contacts_commute", (delta, qr))
            require(ax(qr) == reduced_c(reduced_k(0, delta, reduced_c(qr))),
                    "C1_Ax_common_conjugation", (delta, qr))
            require(ay(qr) == reduced_c(reduced_k(1, delta, reduced_c(qr))),
                    "C1_Ay_common_conjugation", (delta, qr))
            rows += 1
    initial = (0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0)
    require(mixed_h(initial) == 0, "C1_witness_active_delta")
    left = initial
    right = initial
    for side in ("x", "y", "x"):
        left = literal_reader(left, side)
    for side in ("y", "x", "y"):
        right = literal_reader(right, side)
    expected_left = initial[:8] + (1, 3, 0, 1, 0)
    expected_right = initial[:8] + (3, 1, 1, 0, 0)
    require(left == expected_left, "C1_literal_full_AxAyAx_witness", left)
    require(right == expected_right, "C1_literal_full_AyAxAy_witness", right)
    require(left != right, "C1_expected_braid_failure")
    # The shift coefficient is a unit; at delta=1 a nonzero pair of powers
    # cannot fix both q coordinates. This is the injectivity certificate
    # for the analytically proved C5 x C5 presentation, not a word search.
    require(tuple((3 * value) % 5 for value in F5) == (0, 3, 1, 4, 2),
            "C1_unit_shift_coefficient")
    report("C1", start, complete_qr_rows=rows, active_shift_coefficient=3,
           exact_group="C5 x C5", literal_leaf_evaluations=84,
           witness_initial=initial, witness_AxAyAx=left, witness_AyAxAy=right,
           braid_for_this_pair="FAIL_AS_PRESCRIBED")


def perm_comp(left, right):
    return tuple(left[right[i]] for i in range(len(left)))


def perm_power(permutation, exponent):
    result = tuple(range(len(permutation)))
    for _ in range(exponent):
        result = perm_comp(permutation, result)
    return result


def check_s3():
    start = CHECKS
    p_basis = basis(4)
    rows = 0
    m_images = []
    n_images = []
    for q, r in product(F5, repeat=2):
        for p in p_basis:
            cell = p + (q, r)
            m_out = word_cell(cell, ("U",))
            n_out = word_cell(cell, ("e", "U", "e"))
            require(m_out == p + (q, P[q][r]), "C2_literal_M_complete_map", (p, q, r))
            require(n_out == p + (q, N_EXPECTED[q][r]), "C2_literal_N_complete_map", (p, q, r))
            rows += 1
        zero_cell = (0, 0, 0, 0, q, r)
        m_out = word_cell(zero_cell, ("U",))
        n_out = word_cell(zero_cell, ("e", "U", "e"))
        m_images.append(5 * m_out[4] + m_out[5])
        n_images.append(5 * n_out[4] + n_out[5])
    m, n = tuple(m_images), tuple(n_images)
    identity = tuple(range(25))
    require(tuple(sorted(m)) == identity and tuple(sorted(n)) == identity,
            "C2_complete_tables_are_permutations")
    require(perm_power(m, 2) == identity, "C2_M_involution")
    require(perm_power(n, 2) == identity, "C2_N_involution")
    mn = perm_comp(m, n)
    nm = perm_comp(n, m)
    mnm = perm_comp(mn, m)
    nmn = perm_comp(nm, n)
    require(mnm == nmn, "C2_global_braid")
    require(perm_power(mn, 3) == identity, "C2_product_cube")
    require(mn[1] == 4, "C2_fixed_order_three_witness")
    require(m[2] == 1 and n[2] == 2, "C2_fixed_distinct_meridians_witness")
    six = (identity, m, n, mn, nm, mnm)
    require(len(set(six)) == 6, "C2_six_distinct_normal_forms")
    for i, left in enumerate(six):
        for j, right in enumerate(six):
            require(perm_comp(left, right) in six, "C2_six_form_closure", (i, j))
    report("C2", start, piston_basis_qr_rows=rows, complete_maps_per_row=2,
           M_table=P, N_table=N_EXPECTED, exact_group="S3",
           meridian_order=2, product_order=3, group_order=6,
           normal_form_order=("I", "M", "N", "MN", "NM", "MNM"),
           scope="all occupied r; complete p and q restored; Ucal supplied")


def mat_identity(size):
    return tuple(tuple(int(i == j) for j in range(size)) for i in range(size))


def mat_mul(left, right):
    return tuple(tuple(sum(left[i][k] * right[k][j] for k in range(len(right))) % 5
                       for j in range(len(right[0]))) for i in range(len(left)))


def mat_vec(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) % 5 for row in matrix)


I4 = mat_identity(4)
A4 = ((0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0))
B4 = ((0, 0, 4, 0), (0, 0, 0, 4), (4, 0, 0, 0), (0, 4, 0, 0))
NEG4 = tuple(tuple(4 * int(i == j) for j in range(4)) for i in range(4))
LINEAR = {"a": A4, "b": B4, "c": B4, "d": NEG4, "e": NEG4, "U": I4}


def structural_expected(letter, cell):
    p, q, r = cell[:4], cell[4], cell[5]
    addition = ((2, 1 + r, 2, 1 - r) if letter == "c" else
                (2, 1, 3, 4) if letter in ("d", "e") else (0, 0, 0, 0))
    lp = mat_vec(LINEAR[letter], p)
    pp = tuple((a + b) % 5 for a, b in zip(lp, addition))
    if letter == "a":
        qp, rp = q, r
    elif letter == "b":
        qp, rp = -q, -r
    elif letter == "c":
        qp, rp = 1 - q, -r
    elif letter == "d":
        qp, rp = 1 - q, 1 - r
    elif letter == "e":
        qp, rp = 2 - q, 1 - r
    else:
        qp, rp = q, P[q][r]
    return pp + (qp % 5, rp % 5)


def inverse_sl2(matrix):
    a, b = matrix[0]
    c, d = matrix[1]
    require((a * d - b * c) % 5 == 1, "C3_support_matrix_determinant")
    return ((d % 5, -b % 5), (-c % 5, a % 5))


def commutator_sl2(left, right):
    return mat_mul(mat_mul(mat_mul(left, right), inverse_sl2(left)), inverse_sl2(right))


def parity(permutation):
    return sum(permutation[i] > permutation[j]
               for i in range(len(permutation)) for j in range(i + 1, len(permutation))) % 2


def check_tower():
    start = CHECKS
    rows = 0
    for letter in LETTERS:
        for q, r in product(F5, repeat=2):
            for p in basis(4):
                cell = p + (q, r)
                require(apply_letter(letter, cell) == structural_expected(letter, cell),
                        "C3_literal_generator_tower_form", (letter, p, q, r))
                rows += 1
    matrices = []
    for i, j, k in product(range(2), repeat=3):
        current = I4
        for flag, generator in ((i, A4), (j, B4), (k, NEG4)):
            if flag:
                current = mat_mul(current, generator)
        matrices.append(current)
    require(len(set(matrices)) == 8, "C3_eight_distinct_linear_matrices")
    for i, left in enumerate(matrices):
        require(mat_mul(left, left) == I4, "C3_linear_exponent_two", i)
        for j, right in enumerate(matrices):
            require(mat_mul(left, right) == mat_mul(right, left),
                    "C3_linear_commutativity", (i, j))

    h = ((2, 0), (0, 3))
    for t in F5:
        upper = ((1, t), (0, 1))
        lower = ((1, 0), (t, 1))
        require(commutator_sl2(h, upper) == ((1, 3 * t % 5), (0, 1)),
                "C3_perfectness_upper_certificate", t)
        require(commutator_sl2(h, lower) == ((1, 0), (3 * t % 5, 1)),
                "C3_perfectness_lower_certificate", t)

    identity5 = tuple(range(5))
    double = (1, 0, 3, 2, 4)
    expected_centralizer = {
        identity5, double, (2, 3, 0, 1, 4), (3, 2, 1, 0, 4)
    }
    even = tuple(p for p in permutations(range(5)) if parity(p) == 0)
    centralizer = {p for p in even if perm_comp(p, double) == perm_comp(double, p)}
    require(len(even) == 60, "C3_fixed_A5_carrier")
    require(centralizer == expected_centralizer, "C3_double_transposition_centralizer_V4")
    for left in sorted(centralizer):
        require(perm_power(left, 2) == identity5, "C3_centralizer_involutions", left)
        for right in sorted(centralizer):
            require(perm_comp(left, right) == perm_comp(right, left),
                    "C3_centralizer_abelian", (left, right))
    report("C3", start, generator_p_basis_qr_rows=rows, linear_group_order=8,
           linear_group="C2^3", q_group="D10 of order 10",
           piston_kernel_exponent=5, piston_kernel_order_bound="5^100",
           perfectness_commutator_rows=10,
           fixed_double_transposition=double,
           A5_centralizer=tuple(sorted(centralizer)),
           universal_conclusion="analytic proof: every SL2(F5)->Gamma_plus kills -I",
           Gamma_plus_order="not enumerated")


def chi(cell):
    return sum(cell) % 5, cell[5]


def chi_expected(letter, pair):
    z, r = pair
    if letter == "a":
        result = z, r
    elif letter == "b":
        result = -z, -r
    elif letter == "c":
        result = 2 - z, -r
    elif letter == "d":
        result = 2 - z, 1 - r
    elif letter == "e":
        result = 3 - z, 1 - r
    else:
        raise ValueError("chi certificate only for original generators")
    return tuple(value % 5 for value in result)


def check_chi():
    start = CHECKS
    rows = 0
    for letter in LETTERS[:5]:
        for cell in basis(6):
            require(chi(native(letter, cell)) == chi_expected(letter, chi(cell)),
                    "C4_native_chi_affine_identity", (letter, cell))
            rows += 1
    x0 = (0, 0, 0, 0, 0, 0)
    x2 = (3, 0, 0, 0, 2, 0)
    require(chi(x0) == chi(x2) == (0, 0), "C4_fixed_equal_chi_inputs")
    y0, y2 = ucal(x0), ucal(x2)
    require(y0[5] == 0 and y2[5] == 2, "C4_fixed_Ucal_chi_failure")
    require(chi(y0) != chi(y2), "C4_unequal_chi_outputs")
    report("C4", start, affine_generator_rows=rows,
           inputs=(x0, x2), outputs=(y0, y2),
           input_chi=(chi(x0), chi(x2)), output_chi=(chi(y0), chi(y2)),
           all_time_conclusion="analytic induction with actual sigma=z+2theta_n",
           time_search="none", controller_scope="chi history only")


def main():
    emit({"implementation": "contact-author", "status": "START",
          "scientific_status": "NON-CANONICAL L1", "targets": ("C0", "C1", "C2", "C3", "C4")})
    try:
        check_custody()
        check_completed_contacts()
        check_s3()
        check_tower()
        check_chi()
    except CheckFailure as exc:
        emit({"status": "FAIL", "check": exc.label, "detail": exc.detail,
              "checks_completed": CHECKS, "sections_completed": [r["section"] for r in REPORTS]})
        return 1
    except Exception as exc:
        emit({"status": "ERROR", "exception": type(exc).__name__, "message": str(exc),
              "checks_completed": CHECKS, "sections_completed": [r["section"] for r in REPORTS]})
        return 2
    emit({"status": "PASS", "implementation": "contact-author", "total_checks": CHECKS,
          "sections": [r["section"] for r in REPORTS],
          "boundary": "finite certificates support the frozen proofs; no native admission or physical knot claim"})
    return 0


if __name__ == "__main__":
    sys.exit(main())
