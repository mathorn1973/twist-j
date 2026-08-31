#!/usr/bin/env python3
"""Exact audit for P-QDD-REPEATABLE-POINTER-DEPHASING-1."""

from fractions import Fraction as F
import sys


def zero(r, c):
    return [[F(0) for _ in range(c)] for _ in range(r)]


def eye(n):
    out = zero(n, n)
    for i in range(n):
        out[i][i] = F(1)
    return out


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def scale(c, A):
    return [[c * x for x in row] for row in A]


def trans(A):
    return [list(row) for row in zip(*A)]


def mul(A, B):
    rows = len(A)
    mid = len(B)
    cols = len(B[0])
    assert len(A[0]) == mid
    return [[sum((A[i][k] * B[k][j] for k in range(mid)), F(0))
             for j in range(cols)] for i in range(rows)]


def tr(A):
    return sum((A[i][i] for i in range(len(A))), F(0))


def eq(A, B):
    return A == B


def is_zero(A):
    return all(x == 0 for row in A for x in row)


def col(xs):
    return [[F(x)] for x in xs]


def outer_metric(u, v, metric):
    return mul(mul(u, trans(v)), metric)


def bilinear(u, v, metric):
    return mul(mul(trans(u), metric), v)[0][0]


def block_diag(A, B):
    n = len(A)
    m = len(B)
    out = zero(n + m, n + m)
    for i in range(n):
        for j in range(n):
            out[i][j] = A[i][j]
    for i in range(m):
        for j in range(m):
            out[n + i][n + j] = B[i][j]
    return out


def vstack(A, B):
    return [row[:] for row in A] + [row[:] for row in B]


def top_left(A, n):
    return [row[:n] for row in A[:n]]


def bottom_right(A, n):
    return [row[n:] for row in A[n:]]


I = eye(4)
ONE = col([1, 1, 1, 1])
J4 = mul(ONE, trans(ONE))
G = sub(I, scale(F(1, 5), J4))
GINV = add(I, J4)
P = scale(F(1, 4), J4)
Q = sub(I, P)
HJOINT = block_diag(G, G)


def sharp(A):
    return mul(mul(GINV, trans(A)), G)


def joint_sharp(J):
    return mul(mul(GINV, trans(J)), HJOINT)


def phi(KL, KH, R):
    return add(mul(mul(KL, R), sharp(KL)),
               mul(mul(KH, R), sharp(KH)))


def pointer_reduce(Y):
    return add(top_left(Y, 4), bottom_right(Y, 4))


def matrix_basis():
    out = []
    for i in range(4):
        for j in range(4):
            E = zero(4, 4)
            E[i][j] = F(1)
            out.append(E)
    return out


r = scale(F(1, 2), col([1, 1, -1, -1]))
f = scale(F(1, 2), col([1, -1, 1, -1]))
g = scale(F(1, 2), col([1, -1, -1, 1]))


def op(u, v):
    return outer_metric(u, v, G)


def rotation_high(t):
    t = F(t)
    den = 1 + t * t
    c = (1 - t * t) / den
    s = 2 * t / den
    return add(
        P,
        add(
            add(scale(c, op(r, r)), scale(s, op(f, r))),
            add(
                add(scale(-s, op(r, f)), scale(c, op(f, f))),
                op(g, g),
            ),
        ),
    )


CHECKS = []


def check(name, ok):
    CHECKS.append((name, bool(ok)))


def first_nonzero(A):
    for i, row in enumerate(A):
        for j, x in enumerate(row):
            if x != 0:
                return i, j, x
    return None


def main():
    # 01. Carrier and projectors.
    carrier_ok = eq(mul(G, GINV), I) and eq(mul(GINV, G), I)
    carrier_ok = carrier_ok and eq(mul(P, P), P) and eq(mul(Q, Q), Q)
    carrier_ok = carrier_ok and is_zero(mul(P, Q)) and is_zero(mul(Q, P))
    carrier_ok = carrier_ok and eq(add(P, Q), I)
    carrier_ok = carrier_ok and eq(sharp(P), P) and eq(sharp(Q), Q)
    check("CARRIER        exact G inverse and complementary self-adjoint projectors",
          carrier_ok)

    # 02. The frozen sum-zero basis is G-orthonormal and spans Q.
    basis = (r, f, g)
    basis_ok = True
    for i, u in enumerate(basis):
        for j, v in enumerate(basis):
            basis_ok = basis_ok and bilinear(u, v, G) == F(int(i == j))
    basis_ok = basis_ok and all(is_zero(mul(P, u)) for u in basis)
    basis_ok = basis_ok and all(eq(mul(Q, u), u) for u in basis)
    check("HIGH-BASIS     r,f,g are an exact G-orthonormal basis of im(Q)",
          basis_ok)

    # 03. Representative finite-memory phases stay in the registered fibre.
    phase_ts = [F(0), F(1, 2), F(1), F(2), F(3, 2)]
    phases = []
    phase_ok = True
    for t in phase_ts:
        Rhi = rotation_high(t)
        KL = P
        KH = mul(Rhi, Q)
        phase_ok = phase_ok and eq(mul(sharp(KL), KL), P)
        phase_ok = phase_ok and eq(mul(sharp(KH), KH), Q)
        phase_ok = phase_ok and eq(mul(P, KL), KL) and eq(mul(KL, P), KL)
        phase_ok = phase_ok and eq(mul(Q, KH), KH) and eq(mul(KH, Q), KH)
        phases.append((KL, KH))
    check("PHASE-FIBRE    five rational phase representatives satisfy effects and repeatability",
          phase_ok)

    # 04-06. Exact pointer reduction, block dephasing and trace preservation.
    reduction_ok = True
    dephase_ok = True
    trace_ok = True
    basis16 = matrix_basis()
    for KL, KH in phases:
        J = vstack(KL, KH)
        reduction_ok = reduction_ok and eq(mul(joint_sharp(J), J), I)
        for R in basis16:
            Y = mul(mul(J, R), joint_sharp(J))
            direct = phi(KL, KH, R)
            reduction_ok = reduction_ok and eq(pointer_reduce(Y), direct)
            dephase_ok = dephase_ok and is_zero(mul(mul(P, direct), Q))
            dephase_ok = dephase_ok and is_zero(mul(mul(Q, direct), P))
            trace_ok = trace_ok and tr(direct) == tr(R)
    check("POINTER-REDUCE orthogonal pointer contraction equals the two-branch channel on 5x16 audit basis",
          reduction_ok)
    check("DEPHASING      LOW/HIGH cross blocks vanish on the complete 5x16 audit basis",
          dephase_ok)
    check("TRACE          the reduced channel preserves matrix trace on the complete 5x16 audit basis",
          trace_ok)

    # 07. N1: nonorthogonal records retain exact 3/5 coherence.
    v = col([4, 3, 2, 1])
    m = bilinear(v, v, G)
    rho = scale(F(1, 1) / m, outer_metric(v, v, G))
    cross = mul(mul(P, rho), Q)
    gamma = F(3, 5)
    phi_gamma = add(
        add(mul(mul(P, rho), P), mul(mul(Q, rho), Q)),
        scale(gamma, add(mul(mul(P, rho), Q), mul(mul(Q, rho), P))),
    )
    out_cross = mul(mul(P, phi_gamma), Q)
    n1_ok = not is_zero(cross)
    n1_ok = n1_ok and eq(out_cross, scale(gamma, cross))
    n1_ok = n1_ok and not is_zero(out_cross)
    check("CONTROL-N1     pointer overlap gamma=3/5 retains exactly 3/5 of the frozen cross block",
          n1_ok)

    # 08. N2: exact effects without output repeatability need not dephase.
    z = col([1, 0, 0, 0])
    zz = bilinear(z, z, G)
    W = sub(I, scale(F(2, 1) / zz, op(z, z)))
    KL = P
    KH = mul(W, Q)
    effects_ok = eq(mul(sharp(W), W), I)
    effects_ok = effects_ok and eq(mul(sharp(KL), KL), P)
    effects_ok = effects_ok and eq(mul(sharp(KH), KH), Q)
    repeatability_fails = not eq(mul(Q, KH), KH)
    out = phi(KL, KH, I)
    bad_cross = mul(mul(P, out), Q)
    n2_ok = effects_ok and repeatability_fails and not is_zero(bad_cross)
    check("CONTROL-N2     effect-preserving nonrepeatable HIGH branch produces a nonzero cross block",
          n2_ok)

    # 09. Exact witness data are stable and nontrivial.
    n1w = first_nonzero(out_cross)
    n2w = first_nonzero(bad_cross)
    witness_ok = m == F(10) and n1w is not None and n2w is not None
    check("WITNESSES      source norm is 10 and both negative controls have explicit nonzero entries",
          witness_ok)

    print("TWIST-J QDD repeatable pointer dephasing audit")
    print("exact Fraction arithmetic; L4 only; no physical decoherence claim")
    print()
    passed = 0
    for idx, (name, ok) in enumerate(CHECKS, 1):
        tag = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"{tag} {idx:02d} {name}")
    print()
    print(f"DATA phase_representatives={len(phases)} matrix_basis={len(basis16)}")
    print(f"DATA control_n1_gamma={gamma.numerator}/{gamma.denominator} source_norm={m.numerator}/{m.denominator}")
    if n1w is not None:
        print(f"DATA control_n1_first_nonzero=({n1w[0]},{n1w[1]})={n1w[2].numerator}/{n1w[2].denominator}")
    if n2w is not None:
        print(f"DATA control_n2_first_nonzero=({n2w[0]},{n2w[1]})={n2w[2].numerator}/{n2w[2].denominator}")
    print()
    verdict = "ALL PASS" if passed == len(CHECKS) else "FAILURES PRESENT"
    print(f"RESULT {passed}/{len(CHECKS)} {verdict}")
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
