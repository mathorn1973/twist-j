#!/usr/bin/env python3
"""
P-QDD-INSTRUMENT-NONSELECTION-1 exact audit.

Standard library only. All scientific assertions use Fraction or integers.
No float, Decimal, complex approximation, random input or external data.

The universal theorem statements are proved in PREREG.md. This verifier audits
frozen matrix identities, exact breakers, the rational R_t family identities,
and one constructive 16-dimensional orthogonal dilation.
"""

from fractions import Fraction as F
from itertools import combinations


def vec(*xs):
    return [F(x) for x in xs]


def zeros(n, m):
    return [[F(0) for _ in range(m)] for _ in range(n)]


def eye(n):
    A = zeros(n, n)
    for i in range(n):
        A[i][i] = F(1)
    return A


def transpose(A):
    return [list(row) for row in zip(*A)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def mscale(c, A):
    c = F(c)
    return [[c * x for x in row] for row in A]


def mm(A, B):
    n = len(A)
    k = len(B)
    m = len(B[0])
    assert len(A[0]) == k
    C = zeros(n, m)
    for i in range(n):
        for t in range(k):
            if A[i][t] == 0:
                continue
            for j in range(m):
                C[i][j] += A[i][t] * B[t][j]
    return C


def mv(A, x):
    return [sum((A[i][j] * x[j] for j in range(len(x))), F(0))
            for i in range(len(A))]


def vadd(x, y):
    return [a + b for a, b in zip(x, y)]


def vsub(x, y):
    return [a - b for a, b in zip(x, y)]


def vscale(c, x):
    c = F(c)
    return [c * a for a in x]


def outer(x, y):
    return [[a * b for b in y] for a in x]


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), F(0))


def inner(x, y, G):
    return dot(x, mv(G, y))


def rankop(x, y, G):
    # x y^T G
    return outer(x, mv(G, y))


def kron(A, B):
    na, ma = len(A), len(A[0])
    nb, mb = len(B), len(B[0])
    C = zeros(na * nb, ma * mb)
    for i in range(na):
        for j in range(ma):
            for k in range(nb):
                for l in range(mb):
                    C[i * nb + k][j * mb + l] = A[i][j] * B[k][l]
    return C


def tensor_vec(x, y):
    return [a * b for a in x for b in y]


def density(x, G):
    w = inner(x, x, G)
    assert w > 0
    return mscale(F(1, 1) / w, rankop(x, x, G))


def reflection(z, G):
    nz = inner(z, z, G)
    assert nz > 0
    return msub(eye(len(z)), mscale(F(2, 1) / nz, rankop(z, z, G)))


def gram_schmidt(vectors, G):
    out = []
    for v in vectors:
        w = list(v)
        for q in out:
            coeff = inner(w, q, G) / inner(q, q, G)
            w = vsub(w, vscale(coeff, q))
        assert any(x != 0 for x in w)
        out.append(w)
    return out


def extend_isometry(source, target, G):
    assert len(source) == len(target)
    A = gram_schmidt(source, G)
    B = gram_schmidt(target, G)
    for a, b in zip(A, B):
        assert inner(a, a, G) == inner(b, b, G)
    O = eye(len(G))
    fixed = []
    for a, b in zip(A, B):
        x = mv(O, a)
        y = b
        assert inner(x, x, G) == inner(y, y, G)
        if x != y:
            z = vsub(x, y)
            H = reflection(z, G)
            for q in fixed:
                assert mv(H, q) == q
            O = mm(H, O)
        assert mv(O, a) == b
        fixed.append(b)
    return O


def poly_trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def poly_add(a, b):
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    return poly_trim(out)


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return poly_trim(out)


def matrix_equal(A, B):
    return A == B


def mat_is_zero(A):
    return all(x == 0 for row in A for x in row)


def scalar_matrix(c, A):
    return mscale(F(c), A)


# Frozen QDD geometry.
I4 = eye(4)
one = vec(1, 1, 1, 1)
J4 = outer(one, one)
G = msub(I4, mscale(F(1, 5), J4))
Ginv = madd(I4, J4)
E_low = mscale(F(1, 4), J4)
E_high = msub(I4, E_low)


def sharp(A):
    return mm(mm(Ginv, transpose(A)), G)


def effect(K):
    return mm(sharp(K), K)


# Frozen pointer basis inside ker(sum).
r = [F(1, 2), F(1, 2), F(-1, 2), F(-1, 2)]
f = [F(1, 2), F(-1, 2), F(1, 2), F(-1, 2)]
g = [F(1, 2), F(-1, 2), F(-1, 2), F(1, 2)]


def R_t(t):
    t = F(t)
    den = F(1) + t * t
    c = (F(1) - t * t) / den
    s = (F(2) * t) / den
    rr = rankop(r, r, G)
    ff = rankop(f, f, G)
    fr = rankop(f, r, G)
    rf = rankop(r, f, G)
    return madd(I4, madd(mscale(c - 1, madd(rr, ff)), mscale(s, msub(fr, rf))))


def gate_A1_metric_effects():
    assert mm(G, Ginv) == I4
    assert mm(Ginv, G) == I4
    assert sharp(E_low) == E_low
    assert sharp(E_high) == E_high
    assert mm(E_low, E_low) == E_low
    assert mm(E_high, E_high) == E_high
    assert mat_is_zero(mm(E_low, E_high))
    assert madd(E_low, E_high) == I4
    assert mv(G, one) == vscale(F(1, 5), one)
    for q in (r, f, g):
        assert sum(q, F(0)) == 0
        assert mv(G, q) == q
        assert inner(q, q, G) == 1
    assert inner(r, f, G) == 0
    assert inner(r, g, G) == 0
    assert inner(f, g, G) == 0
    print("PASS A1: frozen G and ordered effect pair are exact")


def gate_A2_pointer_and_controlled_witness():
    Pi_low = rankop(r, r, G)
    Pi_high = msub(I4, Pi_low)
    X = madd(I4, madd(mscale(-1, madd(rankop(r, r, G), rankop(f, f, G))),
                       madd(rankop(r, f, G), rankop(f, r, G))))
    assert mv(X, r) == f
    assert mv(X, f) == r
    assert mm(X, X) == I4
    assert effect(X) == I4
    assert mm(Pi_low, Pi_low) == Pi_low
    assert mm(Pi_high, Pi_high) == Pi_high
    assert madd(Pi_low, Pi_high) == I4

    G16 = kron(G, G)
    U = madd(kron(E_low, I4), kron(E_high, X))
    assert mm(mm(transpose(U), G16), U) == G16
    assert mm(U, U) == eye(16)

    P_low = kron(I4, Pi_low)
    P_high = kron(I4, Pi_high)
    basis = [vec(1, 0, 0, 0), vec(0, 1, 0, 0),
             vec(0, 0, 1, 0), vec(0, 0, 0, 1)]
    for e in basis:
        inp = tensor_vec(e, r)
        out = mv(U, inp)
        assert mv(P_low, out) == tensor_vec(mv(E_low, e), r)
        assert mv(P_high, out) == tensor_vec(mv(E_high, e), f)
    print("PASS A2: four-dimensional pointer PVM and controlled witness are exact")


def gate_A3_occurrence_identity():
    # Audit several representatives. The universal identity is written in PREREG.
    H = [
        [F(-5, 7), F(8, 7), F(-2, 7), F(-2, 7)],
        [F(0), F(1), F(0), F(0)],
        [F(-6, 7), F(4, 7), F(6, 7), F(-1, 7)],
        [F(-6, 7), F(4, 7), F(-1, 7), F(6, 7)],
    ]
    P12 = [vec(0, 1, 0, 0), vec(1, 0, 0, 0),
           vec(0, 0, 1, 0), vec(0, 0, 0, 1)]
    representatives = [E_low, E_high, mm(H, E_high), mm(P12, E_high)]
    expected = [E_low, E_high, E_high, E_high]
    for K, E in zip(representatives, expected):
        assert effect(K) == E
        assert mm(mm(transpose(K), G), K) == mm(G, E)
    print("PASS A3: occurrence identity K^T G K = G E audited exactly")


def gate_A4_cross_gram_breaker():
    H = [
        [F(-5, 7), F(8, 7), F(-2, 7), F(-2, 7)],
        [F(0), F(1), F(0), F(0)],
        [F(-6, 7), F(4, 7), F(6, 7), F(-1, 7)],
        [F(-6, 7), F(4, 7), F(-1, 7), F(6, 7)],
    ]
    assert effect(H) == I4
    K_low = E_low
    K_high = mm(H, E_high)
    assert effect(K_low) == E_low
    assert effect(K_high) == E_high
    C = mm(sharp(K_low), K_high)
    expected = [[F(-5, 7), F(5, 7), F(0), F(0)] for _ in range(4)]
    assert C == expected
    assert not mat_is_zero(C)
    print("PASS A4: diagonal-orbit breaker has exact nonzero cross Gram C")


def gate_A5_diagonal_action_not_physical_gauge():
    P12 = [vec(0, 1, 0, 0), vec(1, 0, 0, 0),
           vec(0, 0, 1, 0), vec(0, 0, 0, 1)]
    assert effect(P12) == I4
    assert mm(P12, E_low) == E_low
    K0 = E_low
    K1 = mm(P12, E_high)
    assert effect(K1) == E_high
    assert mat_is_zero(mm(sharp(K0), K1))
    v = vec(1, 0, 0, 0)
    x = mv(E_high, v)
    y = mv(K1, v)
    assert density(x, G) != density(y, G)
    print("PASS A5: one diagonal O(G,Q) action changes the exact post-state")


def gate_A6_rational_injection_controls():
    # Universal rational-circle identities as polynomial identities in t.
    cnum = [1, 0, -1]
    snum = [0, 2]
    den = [1, 0, 1]
    assert poly_add(poly_mul(cnum, cnum), poly_mul(snum, snum)) == poly_mul(den, den)
    assert poly_add(den, cnum) == [2]
    assert snum == [0, 2]  # t * (den + cnum) = 2 t

    ts = [F(0), F(1), F(2), F(1, 2), F(3), F(1, 3), F(5)]
    Ks = []
    for t in ts:
        R = R_t(t)
        assert effect(R) == I4
        assert mv(R, g) == g
        assert mm(R, E_low) == E_low
        assert mm(R, E_high) == mm(E_high, R)
        K = mm(R, E_high)
        assert effect(K) == E_high
        assert mat_is_zero(mm(E_low, K))
        Ks.append(K)
    for i, j in combinations(range(len(ts)), 2):
        assert Ks[i] != Ks[j]
        assert Ks[i] != mscale(-1, Ks[j])
    print("PASS A6: rational R_t family identities and pairwise controls are exact")


def gate_A7_reflection_extension():
    H = reflection(vsub(r, f), G)
    assert effect(H) == I4
    assert mv(H, r) == f
    assert mv(H, g) == g
    assert mv(H, one) == one
    print("PASS A7: rational reflection extension step is exact")


def gate_A8_construct_nonlueder_dilation():
    P12 = [vec(0, 1, 0, 0), vec(1, 0, 0, 0),
           vec(0, 0, 1, 0), vec(0, 0, 0, 1)]
    K0 = E_low
    K1 = mm(P12, E_high)
    assert madd(effect(K0), effect(K1)) == I4

    basis = [vec(1, 0, 0, 0), vec(0, 1, 0, 0),
             vec(0, 0, 1, 0), vec(0, 0, 0, 1)]
    source = [tensor_vec(e, r) for e in basis]
    target = [vadd(tensor_vec(mv(K0, e), r), tensor_vec(mv(K1, e), f))
              for e in basis]
    G16 = kron(G, G)
    for i in range(4):
        for j in range(4):
            assert inner(source[i], source[j], G16) == inner(target[i], target[j], G16)
    U = extend_isometry(source, target, G16)
    assert mm(mm(transpose(U), G16), U) == G16
    for s, t in zip(source, target):
        assert mv(U, s) == t
    print("PASS A8: explicit non-Lueder complete family has a rational orthogonal dilation")


def gate_A9_positive_section_controls():
    neg = mscale(-1, E_low)
    assert sharp(neg) == neg
    assert effect(neg) == E_low
    # -E_low is not G-positive, witnessed on the all-ones direction.
    assert inner(one, mv(neg, one), G) < 0
    # Exact positive forms for the frozen projectors.
    assert mm(G, E_low) == mscale(F(1, 20), J4)
    assert mm(G, E_high) == E_high
    print("PASS A9: self-adjoint sign breaker and positive-root controls are exact")


def gate_A10_controlled_circularity():
    X0 = I4
    X1 = R_t(F(2, 3))
    assert effect(X0) == I4
    assert effect(X1) == I4
    U = madd(kron(E_low, X0), kron(E_high, X1))
    G16 = kron(G, G)
    assert mm(mm(transpose(U), G16), U) == G16
    e0 = mv(X0, r)
    e1 = mv(X1, r)
    # Adapted pointer slots may be chosen from the orthogonal images.
    assert inner(e0, e0, G) == 1
    assert inner(e1, e1, G) == 1
    # This concrete X1 does not guarantee e0 perp e1; circularity theorem itself
    # is the algebraic reduction formula in PREREG. Audit it branchwise directly.
    for e in [vec(1, 0, 0, 0), vec(0, 1, 0, 0),
              vec(0, 0, 1, 0), vec(0, 0, 0, 1)]:
        out = mv(U, tensor_vec(e, r))
        target = vadd(tensor_vec(mv(E_low, e), e0),
                      tensor_vec(mv(E_high, e), e1))
        assert out == target
    print("PASS A10: target-controlled coupling contains the target projectors explicitly")


def main():
    gate_A1_metric_effects()
    gate_A2_pointer_and_controlled_witness()
    gate_A3_occurrence_identity()
    gate_A4_cross_gram_breaker()
    gate_A5_diagonal_action_not_physical_gauge()
    gate_A6_rational_injection_controls()
    gate_A7_reflection_extension()
    gate_A8_construct_nonlueder_dilation()
    gate_A9_positive_section_controls()
    gate_A10_controlled_circularity()
    print("ALL PASS: QDD instrument nonselection exact audit complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
