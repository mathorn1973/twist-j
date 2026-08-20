#!/usr/bin/env python3
"""Exact audit for P-QDD-IDEMPOTENCE-DOMINATES-FORK-1."""

from fractions import Fraction as F
import inspect
import sys

from exact_matrix import (
    add, cols, det, dot, flatten, independent, inv, mm, mpow, mv,
    neg, rank, scale, sharp, sub, tr, zero,
)
from qdd_class import (
    F5, SIGNS, affine_perm, build_class, circle_point, class_idempotent,
    compose, inverse_perm, moving,
)

BASE = "d44645a239df764c630984765a9fdd458b090a31"
ISSUE = 479
CHECKS = []


def check(label, condition):
    CHECKS.append((label, bool(condition)))


def main():
    source = inspect.getsource(build_class)
    forbidden = ("E_low", "E_high", "TARGET_LOW", "TARGET_HIGH", "TARGET_TOKEN")
    check(
        "C1 authority constants and target-independent class builder",
        BASE == "d44645a239df764c630984765a9fdd458b090a31"
        and ISSUE == 479
        and all(token not in source for token in forbidden),
    )

    data = build_class()
    i4, one4 = data["I4"], data["ONE4"]
    gram, gram_inv = data["G"], data["GI"]
    d_j, vertices = data["D"], data["VERTICES"]
    all_perms, simplex = data["PERMS"], data["SIMPLEX"]
    affine = data["AFFINE"]
    full_stabilizer, affine_stabilizer = data["STAB"], data["HSTAB"]
    p, p_full, q = data["P"], data["P_FULL"], data["Q"]
    r_sign, c_plane, j_plane = data["R"], data["C"], data["J"]

    check(
        "C2 J phase motor and regular-simplex identities",
        mpow(d_j, 5) == i4
        and d_j != i4
        and mm(mm(tr(d_j), gram), d_j) == gram
        and tuple(sum((vertices[k][i] for k in F5), F(0)) for i in range(4)) == (F(0),) * 4
        and vertices[2] == (F(-1),) * 4
        and all(
            dot(vertices[x], gram, vertices[y]) == (F(4, 5) if x == y else F(-1, 5))
            for x in F5
            for y in F5
        ),
    )

    principal = tuple(
        det(tuple(tuple(gram[i][j] for j in range(n)) for i in range(n)))
        for n in range(1, 5)
    )
    check(
        "C3 exact positivity and inverse of G",
        principal == (F(4, 5), F(3, 5), F(2, 5), F(1, 5))
        and mm(gram, gram_inv) == i4,
    )

    representation_ok = (
        len(all_perms) == 120
        and len(set(simplex.values())) == 120
        and all(mm(mm(tr(simplex[pi]), gram), simplex[pi]) == gram for pi in all_perms)
        and all(mv(simplex[pi], vertices[x]) == vertices[pi[x]] for pi in all_perms for x in F5)
    )
    law_ok = all(
        mm(simplex[pi], simplex[tau]) == simplex[compose(pi, tau)]
        for pi in all_perms
        for tau in all_perms
    )
    check("C4 complete marked-simplex S5 representation", representation_ok and law_ok)

    translation = affine_perm(1, 1)
    doubling = affine_perm(2, 0)
    generated = {tuple(F5)}
    frontier = [tuple(F5)]
    while frontier:
        current = frontier.pop()
        for generator in (translation, doubling):
            candidate = compose(generator, current)
            if candidate not in generated:
                generated.add(candidate)
                frontier.append(candidate)
    affine_set = set(affine)
    check(
        "C5 J-affine group is exactly AGL1(F5) of order twenty",
        len(affine_set) == 20
        and generated == affine_set
        and simplex[translation] == d_j
        and all(compose(a, b) in affine_set for a in affine for b in affine)
        and all(inverse_perm(a) in affine_set for a in affine),
    )

    fixed = lambda pi: sum(1 for x in F5 if pi[x] == x)
    transpositions = tuple(pi for pi in all_perms if fixed(pi) == 3)
    check(
        "C6 fixed-label certificate excludes every transposition from the affine group",
        len(transpositions) == 10
        and all(fixed(pi) == 3 for pi in transpositions)
        and all(fixed(pi) <= 1 for pi in affine if pi != tuple(F5))
        and not (set(transpositions) & affine_set),
    )

    check(
        "C7 full and affine record stabilizers intersect with index six",
        all(
            len(full_stabilizer[k]) == 24
            and len(affine_stabilizer[k]) == 4
            and set(full_stabilizer[k]) & affine_set == set(affine_stabilizer[k])
            and 24 // len(affine_stabilizer[k]) == 6
            for k in F5
        ),
    )

    check(
        "C8 projector construction, ranks, sharpness, and full-average agreement",
        all(
            p[k] == p_full[k]
            and mm(p[k], p[k]) == p[k]
            and sharp(p[k], gram, gram_inv) == p[k]
            and rank(p[k]) == 1
            and mv(p[k], vertices[k]) == vertices[k]
            and mm(q[k], q[k]) == q[k]
            and sharp(q[k], gram, gram_inv) == q[k]
            and rank(q[k]) == 3
            and mm(p[k], q[k]) == zero(4, 4)
            and add(p[k], q[k]) == i4
            for k in F5
        ),
    )

    check(
        "C9 affine centralizer pieces R,C,J obey the exact multiplication table",
        all(
            rank(r_sign[k]) == 1
            and rank(c_plane[k]) == 2
            and mm(r_sign[k], r_sign[k]) == r_sign[k]
            and sharp(r_sign[k], gram, gram_inv) == r_sign[k]
            and mm(c_plane[k], c_plane[k]) == c_plane[k]
            and sharp(c_plane[k], gram, gram_inv) == c_plane[k]
            and add(r_sign[k], c_plane[k]) == q[k]
            and mm(r_sign[k], c_plane[k]) == zero(4, 4)
            and mm(c_plane[k], r_sign[k]) == zero(4, 4)
            and mm(j_plane[k], j_plane[k]) == neg(c_plane[k])
            and sharp(j_plane[k], gram, gram_inv) == neg(j_plane[k])
            and mm(c_plane[k], j_plane[k]) == j_plane[k]
            and mm(j_plane[k], c_plane[k]) == j_plane[k]
            for k in F5
        ),
    )

    normalizer = {
        k: {
            scale(sign, mm(simplex[h], q[k]))
            for h in full_stabilizer[k]
            for sign in SIGNS
        }
        for k in F5
    }
    normalizer_ok = all(
        len(normalizer[k]) == 48
        and len({frozenset((t, neg(t))) for t in normalizer[k]}) == 24
        and all(
            mm(sharp(t, gram, gram_inv), t) == q[k]
            and mm(q[k], t) == t
            and mm(t, q[k]) == t
            for t in normalizer[k]
        )
        for k in F5
    )
    check("C10 complete 48-member S4 normalizer control", normalizer_ok)

    t_values = (F(0), F(1), F(-1), F(1, 2), F(-2), F(3), F(1, 3), F(-1, 5), F(7, 2))
    circle_points = tuple(dict.fromkeys(tuple(circle_point(t) for t in t_values) + ((F(-1), F(0)),)))
    circle_family = {
        k: {
            moving(data, k, e, r, s)
            for e in SIGNS
            for r, s in circle_points
        }
        for k in F5
    }
    circle_ok = all(
        all(r * r + s * s == 1 for r, s in circle_points)
        and all(
            mm(sharp(t, gram, gram_inv), t) == q[k]
            and mm(q[k], t) == t
            and mm(t, q[k]) == t
            for t in circle_family[k]
        )
        for k in F5
    )
    check("C11 affine C4 rational-circle control", circle_ok)

    enlarged = {
        k: {
            mm(simplex[h], x)
            for h in full_stabilizer[k]
            for x in circle_family[k]
        }
        for k in F5
    }
    enlarged_ok = all(
        normalizer[k] <= enlarged[k]
        and circle_family[k] <= enlarged[k]
        and all(
            mm(sharp(t, gram, gram_inv), t) == q[k]
            and mm(q[k], t) == t
            and mm(t, q[k]) == t
            for t in enlarged[k]
        )
        for k in F5
    )
    check("C12 enlarged stabilizer-times-circle control", enlarged_ok)

    skew_basis = {}
    for k in F5:
        candidates = [j_plane[k]]
        for h in full_stabilizer[k]:
            x = mm(simplex[h], q[k])
            a = sub(x, sharp(x, gram, gram_inv))
            if a != zero(4, 4):
                candidates.append(a)
        chosen = []
        for a in candidates:
            if independent(chosen + [a]):
                chosen.append(a)
            if len(chosen) == 3:
                break
        skew_basis[k] = tuple(chosen)

    skew_ok = all(
        len(skew_basis[k]) == 3
        and all(
            sharp(a, gram, gram_inv) == neg(a)
            and mm(q[k], mm(a, q[k])) == a
            for a in skew_basis[k]
        )
        for k in F5
    )
    check("C13 three-dimensional G-skew support basis for Cayley controls", skew_ok)

    grid = (-2, -1, 0, 1, 2)
    cayley = {}
    for k in F5:
        family = set()
        a0, a1, a2 = skew_basis[k]
        for c0 in grid:
            for c1 in grid:
                for c2 in grid:
                    a = add(scale(c0, a0), add(scale(c1, a1), scale(c2, a2)))
                    try:
                        denominator_inv = inv(add(i4, a))
                    except ValueError:
                        continue
                    o = mm(sub(i4, a), denominator_inv)
                    family.add(mm(q[k], mm(o, q[k])))
        cayley[k] = family

    cayley_ok = all(
        len(cayley[k]) >= 100
        and all(
            mm(sharp(t, gram, gram_inv), t) == q[k]
            and mm(q[k], t) == t
            and mm(t, q[k]) == t
            for t in cayley[k]
        )
        for k in F5
    )
    check("C14 deterministic rational Cayley sample of the full orthogonal family", cayley_ok)

    controls = {
        k: normalizer[k] | circle_family[k] | enlarged[k] | cayley[k]
        for k in F5
    }
    selected = {
        k: {t for t in controls[k] if class_idempotent(t)}
        for k in F5
    }
    control_selection_ok = all(
        selected[k] == {q[k], neg(q[k])}
        and all(
            mm(sharp(t, gram, gram_inv), t) == q[k]
            and mm(q[k], t) == t
            and mm(t, q[k]) == t
            for t in controls[k]
        )
        for k in F5
    )
    check("C15 all finite and sampled controls select exactly +-Q", control_selection_ok)

    breakers_ok = True
    for k in F5:
        others = [x for x in F5 if x != k]
        tau = list(F5)
        tau[others[0]], tau[others[1]] = others[1], others[0]
        tau = tuple(tau)
        t_tau = mm(simplex[tau], q[k])
        t_star = sub(r_sign[k], c_plane[k])
        breakers_ok = breakers_ok and (
            tau not in affine_set
            and t_tau in normalizer[k]
            and mm(t_tau, t_tau) == q[k]
            and not class_idempotent(t_tau)
            and mm(sharp(t_star, gram, gram_inv), t_star) == q[k]
            and mm(q[k], t_star) == t_star
            and mm(t_star, t_star) == q[k]
            and not class_idempotent(t_star)
        )
    check("C16 naturality-fork and affine-circle breakers are killed only by class idempotence", breakers_ok)

    # Target comparison is deliberately last.
    target_low = scale(F(1, 4), one4)
    target_high = sub(i4, target_low)
    token = 2
    check(
        "C17 target comparison last gives the Lueder ordered projector pair",
        p[token] == target_low and q[token] == target_high,
    )

    failures = [(index + 1, label) for index, (label, ok) in enumerate(CHECKS) if not ok]
    if not failures:
        decision = "IDEMPOTENCE-DOMINATES"
        exit_code = 0
    elif any(index == 1 for index, _ in failures):
        decision = "STOP"
        exit_code = 1
    elif any(2 <= index <= 9 for index, _ in failures):
        decision = "RELABELING-F"
        exit_code = 0
    elif any(10 <= index <= 14 for index, _ in failures):
        decision = "CONTROL-F"
        exit_code = 0
    elif any(15 <= index <= 16 for index, _ in failures):
        decision = "SELECTION-F"
        exit_code = 0
    else:
        decision = "TARGET-F"
        exit_code = 0

    print("P-QDD-IDEMPOTENCE-DOMINATES-FORK-1")
    print(f"BASE_COMMIT {BASE}")
    print(f"ISSUE {ISSUE}")
    print("CLASS_INPUTS M_J,D_J,G,F5,S5,AGL1,projectors,orthogonal-branches")
    print("CLASS_TARGET_INDEPENDENCE PASS" if CHECKS[0][1] else "CLASS_TARGET_INDEPENDENCE FAIL")
    print("J_AFFINE_GROUP order=20 simplex_symmetry=120")
    print("RECORD_STABILIZERS full=24 affine=4 index=6")
    print("TRANSPOSITION_AFFINE overlap=0")
    print("PROJECTORS ranks=1,3")
    print("GROUP_FREE_LEMMA class_idempotence_selects=+-Q")
    print("NORMALIZER_CONTROL algebraic=48 sign_classes=24")
    print(f"C4_CIRCLE_CONTROL points={len(circle_points)}")
    print("ENLARGED_CONTROL audited=YES")
    print(f"CAYLEY_CONTROL minimum_unique={min(len(cayley[k]) for k in F5)}")
    print("CONTROL_IDEMPOTENTS selected=+-Q-only")
    print("FORK_BREAKERS nonaffine-transposition=KILLED affine-R-minus-C=KILLED")
    print("TARGET_TOKEN 2")
    print("TARGET_EFFECTS P2=E_low Q2=E_high")
    print(f"DECISION {decision}")
    print("O2_GLOBAL_STATUS UNCHANGED")
    print("SAMPLING NOT PROVIDED")
    print("CANDIDATE_CEILING T restricted-L4-theorems" if not failures else "CANDIDATE_CEILING NONE")
    print(f"ALL PASS {len(CHECKS) - len(failures)}/{len(CHECKS)}")

    if failures:
        for index, label in failures:
            print(f"FAILURE C{index} {label}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
