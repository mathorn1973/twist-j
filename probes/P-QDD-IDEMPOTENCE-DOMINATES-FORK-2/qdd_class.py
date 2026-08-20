"""Target-independent J-simplex and branch-class construction."""

from fractions import Fraction as F
from itertools import permutations

from exact_matrix import (
    add, basis, cols, eye, independent, inv, mat, mm, mpow, mv,
    neg, scale, sub, sum_mats, zero,
)

F5 = tuple(range(5))
UNITS = (1, 2, 3, 4)
SIGNS = (-1, 1)

def compose(p, q):
    """Permutation p after q."""
    return tuple(p[q[x]] for x in range(len(p)))


def inverse_perm(p):
    out = [0] * len(p)
    for i, image in enumerate(p):
        out[image] = i
    return tuple(out)


def affine_perm(c, b):
    return tuple((b + c * x) % 5 for x in F5)



def build_class():
    """Build only from the J step, the rational simplex, and frozen label actions."""
    i4 = eye(4)
    one4 = tuple(tuple(F(1) for _ in range(4)) for _ in range(4))
    gram = sub(i4, scale(F(1, 5), one4))
    gram_inv = add(i4, one4)
    m_j = mat(((1, 0, -1, 1), (0, 1, -1, 0), (1, 0, 0, 0), (0, 1, -1, 1)))
    d_j = sub(m_j, i4)
    vertices = tuple(mv(mpow(d_j, k), basis(4, 0)) for k in F5)
    vertex_basis = cols(vertices[:4])
    vertex_basis_inv = inv(vertex_basis)
    all_perms = tuple(permutations(F5))

    def rho(pi):
        moved = tuple(vertices[pi[x]] for x in range(4))
        return mm(cols(moved), vertex_basis_inv)

    simplex = {pi: rho(pi) for pi in all_perms}
    affine = tuple(affine_perm(c, b) for c in UNITS for b in F5)
    full_stabilizer = {k: tuple(pi for pi in all_perms if pi[k] == k) for k in F5}
    affine_stabilizer = {k: tuple(pi for pi in affine if pi[k] == k) for k in F5}

    p = {
        k: scale(F(1, 4), sum_mats((simplex[pi] for pi in affine_stabilizer[k]), 4, 4))
        for k in F5
    }
    p_full = {
        k: scale(F(1, 24), sum_mats((simplex[pi] for pi in full_stabilizer[k]), 4, 4))
        for k in F5
    }
    q = {k: sub(i4, p[k]) for k in F5}
    generator = {k: simplex[affine_perm(2, k * (1 - 2) % 5)] for k in F5}
    r_sign = {}
    c_plane = {}
    j_plane = {}
    for k in F5:
        gk = generator[k]
        r_sign[k] = scale(F(1, 4), add(sub(i4, gk), sub(mpow(gk, 2), mpow(gk, 3))))
        c_plane[k] = sub(q[k], r_sign[k])
        j_plane[k] = mm(gk, c_plane[k])

    return {
        "I4": i4,
        "ONE4": one4,
        "G": gram,
        "GI": gram_inv,
        "MJ": m_j,
        "D": d_j,
        "VERTICES": vertices,
        "PERMS": all_perms,
        "SIMPLEX": simplex,
        "AFFINE": affine,
        "STAB": full_stabilizer,
        "HSTAB": affine_stabilizer,
        "P": p,
        "P_FULL": p_full,
        "Q": q,
        "GEN": generator,
        "R": r_sign,
        "C": c_plane,
        "J": j_plane,
    }


def circle_point(t):
    t = t if isinstance(t, F) else F(t)
    den = 1 + t * t
    return (1 - t * t) / den, 2 * t / den


def moving(data, k, e, r, s):
    return add(
        scale(e, data["R"][k]),
        add(scale(r, data["C"][k]), scale(s, data["J"][k])),
    )


def class_idempotent(t):
    square = mm(t, t)
    return square == t or square == neg(t)


