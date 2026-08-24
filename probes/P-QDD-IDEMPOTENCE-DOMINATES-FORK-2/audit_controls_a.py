"""Exact finite and sampled gates C10-C14 for the pinned QDD probe."""

from fractions import Fraction as F

from exact_matrix import add, independent, inv, mm, neg, scale, sharp, sub, zero
from qdd_class import F5, SIGNS, circle_point, moving


def run_control_families(check, data, ctx):
    i4 = ctx["i4"]
    gram, gram_inv = ctx["gram"], ctx["gram_inv"]
    simplex = ctx["simplex"]
    full_stabilizer = ctx["full_stabilizer"]
    q = ctx["q"]
    j_plane = ctx["j_plane"]

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

    return {
        "normalizer": normalizer,
        "circle_family": circle_family,
        "enlarged": enlarged,
        "cayley": cayley,
        "circle_points": len(circle_points),
    }
