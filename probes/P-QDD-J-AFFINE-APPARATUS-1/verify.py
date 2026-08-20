#!/usr/bin/env python3
"""Exact audit for P-QDD-J-AFFINE-APPARATUS-1."""

from fractions import Fraction as Q
import inspect

from exact_matrix import (
    add, basis, cols, coord_proj, dot, eye, inv, kron, mat, mm, mpow, mv,
    neg, perm, pointer_block, rank, scale, sharp, sub, sum_mats, tr, zero,
)

BASE = "362e9c3a9afa9f63005eaf0a1c03baac66617012"
ISSUE = 456
A = (1, 2, 3, 4)
F5 = (0, 1, 2, 3, 4)


def image(c, b, x):
    return (b + c * x) % 5


def hoff(a, k):
    return k * (1 - a) % 5


def build_class():
    """Build from J, F5, affine symmetry, pointer and memory only."""
    i4 = eye(4)
    one4 = tuple(tuple(Q(1) for _ in F5[:4]) for _ in F5[:4])
    g = sub(i4, scale(Q(1, 5), one4))
    gi = inv(g)
    mj = mat(((1, 0, -1, 1), (0, 1, -1, 0), (1, 0, 0, 0), (0, 1, -1, 1)))
    d = sub(mj, i4)
    us = tuple(mv(mpow(d, k), basis(4, 0)) for k in F5)
    ub = cols(us[:4])
    ubi = inv(ub)

    def rho(c, b):
        return mm(cols(tuple(us[image(c, b, x)] for x in range(4))), ubi)

    aff = {(c, b): rho(c, b) for c in A for b in F5}
    h = {(a, k): aff[(a, hoff(a, k))] for a in A for k in F5}
    p = {k: scale(Q(1, 4), sum_mats((h[(a, k)] for a in A), 4, 4)) for k in F5}
    q = {k: sub(i4, p[k]) for k in F5}
    i2, x, i5 = eye(2), mat(((0, 1), (1, 0))), eye(5)
    b = {(a, k): add(kron(p[k], i2), kron(mm(h[(a, k)], q[k]), x)) for a in A for k in F5}
    u = {
        a: sum_mats((kron(b[(a, k)], coord_proj(5, k)) for k in F5), 40, 40)
        for a in A
    }
    lm = {(c, b0): perm(tuple(image(c, b0, x0) for x0 in F5)) for c in A for b0 in F5}
    ta = {key: kron(kron(aff[key], i2), lm[key]) for key in aff}
    gt, gti = kron(kron(g, i2), i5), kron(kron(gi, i2), i5)
    return dict(I4=i4, G=g, GI=gi, D=d, US=us, AFF=aff, H=h, P=p, Q=q,
                B=b, U=u, TA=ta, GT=gt, GTI=gti)


def main():
    src = inspect.getsource(build_class)
    assert all(x not in src for x in ("E_low", "E_high", "TARGET_LOW", "TARGET_HIGH"))
    c = build_class()
    i4, g, gi, d = c["I4"], c["G"], c["GI"], c["D"]
    us, aff, h, p, q = c["US"], c["AFF"], c["H"], c["P"], c["Q"]
    blocks, couplings, ta, gt, gti = c["B"], c["U"], c["TA"], c["GT"], c["GTI"]
    gates = 1

    assert mpow(d, 5) == i4 and mm(mm(tr(d), g), d) == g
    gates += 1
    assert tuple(sum((us[k][i] for k in F5), Q(0)) for i in range(4)) == (Q(0),) * 4
    for x in F5:
        for y in F5:
            assert dot(us[x], g, us[y]) == (Q(4, 5) if x == y else Q(-1, 5))
    assert us[2] == (Q(-1),) * 4
    gates += 1

    assert len(set(aff.values())) == 20
    for (a, b0), r in aff.items():
        assert mm(mm(tr(r), g), r) == g
        assert all(mv(r, us[x]) == us[image(a, b0, x)] for x in F5)
        for aa in A:
            for bb in F5:
                assert mm(r, aff[(aa, bb)]) == aff[(a * aa % 5, (b0 + a * bb) % 5)]
    gates += 1

    assert sum_mats((p[k] for k in F5), 4, 4) == scale(Q(5, 4), i4)
    for k in F5:
        assert mm(p[k], p[k]) == p[k] and sharp(p[k], g, gi) == p[k] and rank(p[k]) == 1
        assert mv(p[k], us[k]) == us[k]
        assert mm(q[k], q[k]) == q[k] and sharp(q[k], g, gi) == q[k] and rank(q[k]) == 3
        for (a, b0), r in aff.items():
            assert mm(mm(r, p[k]), inv(r)) == p[image(a, b0, k)]
    gates += 1

    assert len(set(couplings.values())) == 4
    invol, selfadj = [], []
    i40 = eye(40)
    for a in A:
        u = couplings[a]
        assert mm(mm(tr(u), gt), u) == gt
        assert all(mm(t, u) == mm(u, t) for t in ta.values())
        for k in F5:
            e = kron(eye(8), coord_proj(5, k))
            assert mm(e, u) == mm(u, e)
        if mm(u, u) == i40:
            invol.append(a)
        if sharp(u, gt, gti) == u:
            selfadj.append(a)
    assert invol == [1, 4] and selfadj == [1, 4]
    gates += 1

    for a in A:
        for k in F5:
            k0, k1 = pointer_block(blocks[(a, k)], 0), pointer_block(blocks[(a, k)], 1)
            assert k0 == p[k] and k1 == mm(h[(a, k)], q[k])
            assert mm(sharp(k0, g, gi), k0) == p[k]
            assert mm(sharp(k1, g, gi), k1) == q[k]
            assert mm(sharp(k0, g, gi), k1) == zero(4, 4)
    gates += 1

    # Target comparison is deliberately after the complete class construction.
    elow = scale(Q(1, 4), tuple(tuple(Q(1) for _ in range(4)) for _ in range(4)))
    ehigh, token = sub(i4, elow), 2
    assert p[token] == elow and q[token] == ehigh
    pairs = {}
    for a in A:
        k0, k1 = pointer_block(blocks[(a, token)], 0), pointer_block(blocks[(a, token)], 1)
        assert mm(sharp(k0, g, gi), k0) == elow
        assert mm(sharp(k1, g, gi), k1) == ehigh
        pairs[a] = (k0, k1)
    assert pairs[1] == (elow, ehigh)
    gates += 1

    for i, a in enumerate(A):
        for b0 in A[i + 1:]:
            assert pairs[a][1] != pairs[b0][1] and pairs[a][1] != neg(pairs[b0][1])
    gates += 1
    assert pairs[1][1] != pairs[4][1] and pairs[1][1] != neg(pairs[4][1])
    gates += 1
    dr = tuple(rank(sub(pairs[a][1], ehigh)) for a in A)
    assert dr == (0, 3, 3, 2) and [a for a, r in zip(A, dr) if r == 0] == [1]
    gates += 1
    assert gates == 11

    print("P-QDD-J-AFFINE-APPARATUS-1")
    print(f"BASE_COMMIT {BASE}")
    print(f"ISSUE {ISSUE}")
    print("CLASS_INPUTS M_J,D_J,G,F5,AGL1,pointer-C2,memory-F5")
    print("CLASS_TARGET_INDEPENDENCE PASS")
    print("PHASE_MOTOR order=5 G_orthogonal=YES")
    print("SIMPLEX vertices=5 gram_diag=4/5 gram_off=-1/5")
    print("AFFINE_GROUP order=20 faithful=YES")
    print("STABILIZER_PROJECTORS count=5 ranks=1 complements=3")
    print("COUPLING_CLASS multipliers=1,2,3,4 size=4 reversible=4 covariant=4")
    print("TARGET_TOKEN 2")
    print("TARGET_EFFECTS realized=4")
    print("POSTSTATE_CLASSES 4")
    print("LUEDER_MULTIPLIER 1")
    print("INVOLUTIVE_SELFADJOINT multipliers=1,4 classes=2")
    print("MOVING_DISPLACEMENT_RANKS a1=0 a2=3 a3=3 a4=2")
    print("ADDED_IDENTITY_MINIMAL_DISTURBANCE selects=1 status=EXTRA_PREMISE")
    print("DECISION NONUNIQUE")
    print("O2_GLOBAL_STATUS UNCHANGED")
    print("SAMPLING NOT PROVIDED")
    print("CANDIDATE_CEILING T restricted-class theorem")
    print("ALL PASS 11/11")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
