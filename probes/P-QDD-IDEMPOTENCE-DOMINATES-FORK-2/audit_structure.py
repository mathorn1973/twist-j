"""Exact structural gates C2-C9 for the pinned QDD probe."""

from fractions import Fraction as F

from exact_matrix import add, det, dot, mm, mpow, mv, rank, sharp, tr, zero
from qdd_class import F5, affine_perm, compose, inverse_perm


def run_structure(check, data):
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
    return {
        "i4": i4, "one4": one4, "gram": gram, "gram_inv": gram_inv,
        "vertices": vertices, "all_perms": all_perms, "simplex": simplex,
        "affine": affine, "full_stabilizer": full_stabilizer,
        "affine_stabilizer": affine_stabilizer, "p": p, "q": q,
        "r_sign": r_sign, "c_plane": c_plane, "j_plane": j_plane,
        "affine_set": affine_set,
    }
