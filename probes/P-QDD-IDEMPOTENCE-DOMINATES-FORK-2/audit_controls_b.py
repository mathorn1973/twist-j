"""Exact selection and target gates C15-C17 for the pinned QDD probe."""

from exact_matrix import mm, neg, sharp, sub
from qdd_class import F5, class_idempotent


def run_control_selection(check, ctx, families):
    i4, one4 = ctx["i4"], ctx["one4"]
    gram, gram_inv = ctx["gram"], ctx["gram_inv"]
    simplex = ctx["simplex"]
    q, p = ctx["q"], ctx["p"]
    r_sign, c_plane = ctx["r_sign"], ctx["c_plane"]
    affine_set = ctx["affine_set"]
    normalizer = families["normalizer"]
    controls = {
        k: normalizer[k] | families["circle_family"][k] | families["enlarged"][k] | families["cayley"][k]
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
            and mm(t_star, q[k]) == t_star
            and mm(t_star, t_star) == q[k]
            and not class_idempotent(t_star)
        )
    check("C16 naturality-fork and affine-circle breakers are killed only by class idempotence", breakers_ok)

    # Target comparison is deliberately last.
    from fractions import Fraction as F
    from exact_matrix import scale

    target_low = scale(F(1, 4), one4)
    target_high = sub(i4, target_low)
    token = 2
    check(
        "C17 target comparison last gives the Lueder ordered projector pair",
        p[token] == target_low and q[token] == target_high,
    )
    return {
        "circle_points": families["circle_points"],
        "cayley_minimum": min(len(families["cayley"][k]) for k in F5),
    }
