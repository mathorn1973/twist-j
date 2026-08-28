#!/usr/bin/env python3
"""Exact audit for P-J-QUADRATIC-CARRY-NORM-SEAM-2.

Standard library only. No floats, randomness, files, environment inputs, or
network. All arithmetic is exact in Q(zeta_5) using Fraction.
"""

from fractions import Fraction as F
from math import gcd
import sys

ZERO = (F(0), F(0), F(0), F(0))
ONE = (F(1), F(0), F(0), F(0))
JBAS = (F(0), F(1), F(0), F(0))
BASIS = [
    (F(1), F(0), F(0), F(0)),
    (F(0), F(1), F(0), F(0)),
    (F(0), F(0), F(1), F(0)),
    (F(0), F(0), F(0), F(1)),
]


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def neg(x):
    return tuple(-a for a in x)


def sub(x, y):
    return add(x, neg(y))


def scal(a, x):
    return tuple(a * b for b in x)


def mul(x, y):
    # Multiply in Q[j]/(1+j+j^2+j^3+j^4), basis 1,j,j^2,j^3.
    c = [F(0)] * 7
    for i in range(4):
        for k in range(4):
            c[i + k] += x[i] * y[k]
    # j^5=1, j^6=j.
    c[0] += c[5]
    c[1] += c[6]
    # j^4=-(1+j+j^2+j^3).
    t = c[4]
    for i in range(4):
        c[i] -= t
    return tuple(c[:4])


def jpow(n):
    n %= 5
    if n == 0:
        return ONE
    if n == 1:
        return JBAS
    if n == 2:
        return (F(0), F(0), F(1), F(0))
    if n == 3:
        return (F(0), F(0), F(0), F(1))
    return (F(-1), F(-1), F(-1), F(-1))


def sigma(x, k):
    out = ZERO
    for i, a in enumerate(x):
        out = add(out, scal(a, jpow(i * k)))
    return out


def conj(x):
    return sigma(x, 4)


def u(x):
    return sigma(x, 2)


def tr_k_q(x):
    t = ZERO
    for k in (1, 2, 3, 4):
        t = add(t, sigma(x, k))
    assert t[1:] == (F(0), F(0), F(0))
    return t[0]


def tr_kplus_q(x):
    return tr_k_q(x) / 2


SQRT5 = add(ONE, scal(F(2), add(JBAS, jpow(4))))
INV_SQRT5 = scal(F(1, 5), SQRT5)


def div_sqrt5(x):
    return mul(x, INV_SQRT5)


def H(x):
    return mul(x, conj(x))


def q0_field(x):
    return tr_kplus_q(H(x))


def q1_field(x):
    z = div_sqrt5(sub(H(x), u(H(x))))
    assert z[1:] == (F(0), F(0), F(0))
    return z[0]


def q0_poly(v):
    a, b, c, d = v
    return 2 * (a*a + b*b + c*c + d*d) - (
        a*b + a*c + a*d + b*c + b*d + c*d
    )


def q1_poly(v):
    a, b, c, d = v
    return a*b - a*c - a*d + b*c - b*d + c*d


def mat_mul(A, B):
    n = len(A)
    p = len(B)
    m = len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(p)) for j in range(m)]
            for i in range(n)]


def mat_T(A):
    return [list(row) for row in zip(*A)]


def mat_pow(A, n):
    I = [[F(int(i == j)) for j in range(len(A))] for i in range(len(A))]
    R = I
    for _ in range(n):
        R = mat_mul(R, A)
    return R


def mat_eq(A, B):
    return A == B


def qmat(Q, v):
    return sum(v[i] * Q[i][j] * v[j] for i in range(4) for j in range(4))


def matrix_from_columns(cols):
    return [[cols[j][i] for j in range(len(cols))] for i in range(len(cols[0]))]


def apply_mat(A, v):
    return tuple(sum(A[i][j] * v[j] for j in range(4)) for i in range(4))


def quadratic_coefficients_from_field(qfun):
    # Monomial order: a2,b2,c2,d2,ab,ac,ad,bc,bd,cd.
    diag = [qfun(e) for e in BASIS]
    cross = []
    for i in range(4):
        for j in range(i + 1, 4):
            cross.append(qfun(add(BASIS[i], BASIS[j])) - diag[i] - diag[j])
    return tuple(diag + cross)


def h_coefficients():
    # Same monomial order, coefficients in K.
    diag = [H(e) for e in BASIS]
    cross = []
    for i in range(4):
        for j in range(i + 1, 4):
            cross.append(sub(H(add(BASIS[i], BASIS[j])), add(diag[i], diag[j])))
    return tuple(diag + cross)


def kplus_pair(x):
    # Return A,B with x=A+B*sqrt5. Valid for x in K+.
    assert x[1] == 0 and x[2] == x[3]
    B = -x[2] / 2
    A = x[0] + B
    assert add((A, F(0), F(0), F(0)), scal(B, SQRT5)) == x
    return A, B


def fmt_pair(pair):
    a, b = pair
    if b == 0:
        return str(a)
    return f"({a},{b})"


CHECKS = []


def check(name, condition, detail):
    ok = bool(condition)
    CHECKS.append((name, ok, detail))
    if not ok:
        raise AssertionError(name + ": " + detail)


def main():
    # Static carrier integrity.
    check("K1 sqrt5^2=5", mul(SQRT5, SQRT5) == scal(F(5), ONE),
          "sqrt5 exact in Q(zeta5)")

    MJ = [
        [F(1), F(0), F(-1), F(1)],
        [F(0), F(1), F(-1), F(0)],
        [F(1), F(0), F(0), F(0)],
        [F(0), F(1), F(-1), F(1)],
    ]
    I4 = [[F(int(i == j)) for j in range(4)] for i in range(4)]
    D = [[MJ[i][j] - I4[i][j] for j in range(4)] for i in range(4)]
    check("K2 D^5=I", mat_eq(mat_pow(D, 5), I4),
          "D=M_J-I is multiplication by j^2")

    U = matrix_from_columns([u(e) for e in BASIS])

    # G1: coefficient formulas from field definitions.
    q0c = quadratic_coefficients_from_field(q0_field)
    q1c = quadratic_coefficients_from_field(q1_field)
    q0_target = (F(2), F(2), F(2), F(2), F(-1), F(-1), F(-1), F(-1), F(-1), F(-1))
    q1_target = (F(0), F(0), F(0), F(0), F(1), F(-1), F(-1), F(1), F(-1), F(1))
    check("G1 q0 field=polynomial", q0c == q0_target,
          "q0 coefficients exact")
    check("G1 q1 field=polynomial", q1c == q1_target,
          "q1 coefficients exact")

    # Matrices of q0 and public q_- = 2 q1.
    Q0 = [[F(2) if i == j else F(-1, 2) for j in range(4)] for i in range(4)]
    Qminus = [
        [F(0), F(1), F(-1), F(-1)],
        [F(1), F(0), F(1), F(-1)],
        [F(-1), F(1), F(0), F(1)],
        [F(-1), F(-1), F(1), F(0)],
    ]
    # Recover polynomial coefficient lists from symmetric matrices.
    q0_from_matrix = tuple([Q0[i][i] for i in range(4)] +
                           [2*Q0[i][j] for i in range(4) for j in range(i+1,4)])
    q1_from_qminus = tuple([Qminus[i][i]/2 for i in range(4)] +
                           [Qminus[i][j] for i in range(4) for j in range(i+1,4)])
    check("G1 q0=q_plus", q0_from_matrix == q0_target,
          "q_plus=(5/2)(I-(1/5)11^T)")
    check("G1 2q1=q_minus", q1_from_qminus == q1_target,
          "public epsilon-line matrix")

    # Generator covariance by matrix congruence.
    DtQ0D = mat_mul(mat_T(D), mat_mul(Q0, D))
    UtQ0U = mat_mul(mat_T(U), mat_mul(Q0, U))
    DtQmD = mat_mul(mat_T(D), mat_mul(Qminus, D))
    UtQmU = mat_mul(mat_T(U), mat_mul(Qminus, U))
    check("G1 affine character law", DtQ0D == Q0 and UtQ0U == Q0 and
          DtQmD == Qminus and UtQmU == [[-x for x in row] for row in Qminus],
          "q0 invariant; q1 epsilon under U")

    # G2: unique rational prime coalescence.
    diffs = [int(a-b) for a, b in zip(q0_target, q1_target)]
    g = 0
    for d in diffs:
        if d:
            g = gcd(g, abs(d))
    check("G2 coefficient gcd=2", g == 2,
          "q0 mod ell=q1 mod ell iff ell divides 2")
    q0m2 = tuple(int(x) % 2 for x in q0_target)
    q1m2 = tuple(int(x) % 2 for x in q1_target)
    e2 = (0,0,0,0,1,1,1,1,1,1)
    check("G2 common mod2=e2", q0m2 == q1m2 == e2,
          "binary carry polynomial shape")

    # G3: coefficientwise relative-norm reconstruction.
    hc = h_coefficients()
    recon = []
    recon_u = []
    for a, b in zip(q0_target, q1_target):
        recon.append(add(scal(a/2, ONE), scal(b/2, SQRT5)))
        recon_u.append(sub(scal(a/2, ONE), scal(b/2, SQRT5)))
    check("G3 H reconstruction", tuple(recon) == hc,
          "H=(q0+sqrt5*q1)/2 coefficientwise")
    check("G3 uH reconstruction", tuple(recon_u) == tuple(u(z) for z in hc),
          "uH=(q0-sqrt5*q1)/2 coefficientwise")

    # G4: independence, normalization and multiplicativity witness.
    check("G4 two character lines independent", q0_target != q1_target and
          any(q0_target[i] != 0 and q1_target[i] == 0 for i in range(10)),
          "affine covariance leaves two coefficients")
    check("G4 normalization A=1/2", q0_field(ONE) == 2 and q1_field(ONE) == 0,
          "F(1)=2A")
    x = add(ONE, JBAS)
    x2 = mul(x, x)
    vals = (q0_field(x), q1_field(x), q0_field(x2), q1_field(x2))
    check("G4 witness values", vals == (F(3), F(1), F(7), F(3)),
          "x=1+j gives (3,1); x^2 gives (7,3)")
    # Derive the multiplicativity defect as a polynomial in formal B over Q(sqrt5).
    # Kplus coefficients are pairs (r,s) representing r+s*sqrt5.
    def kp_add(z, w):
        return (z[0] + w[0], z[1] + w[1])
    def kp_neg(z):
        return (-z[0], -z[1])
    def kp_mul(z, w):
        return (z[0]*w[0] + 5*z[1]*w[1], z[0]*w[1] + z[1]*w[0])
    def poly_sub(P, Q):
        n = max(len(P), len(Q))
        z = (F(0), F(0))
        return tuple(kp_add(P[i] if i < len(P) else z,
                            kp_neg(Q[i] if i < len(Q) else z)) for i in range(n))
    def poly_mul(P, Q):
        out = [(F(0), F(0)) for _ in range(len(P)+len(Q)-1)]
        for i, a0 in enumerate(P):
            for j, b0 in enumerate(Q):
                out[i+j] = kp_add(out[i+j], kp_mul(a0, b0))
        return tuple(out)

    q0x, q1x, q0x2, q1x2 = vals
    Fx = ((q0x/2, F(0)), (F(0), q1x))
    Fx2 = ((q0x2/2, F(0)), (F(0), q1x2))
    defect = poly_sub(Fx2, poly_mul(Fx, Fx))
    target_defect = ((F(5,4),F(0)), (F(0),F(0)), (F(-5),F(0)))
    check("G4 multiplicativity factor", defect == target_defect,
          "derived polynomial is (5/4)(1-4B^2)")
    # B=+/-1/2 equals H/uH coefficientwise by G3.
    plus = tuple(add(scal(a/2, ONE), scal(b/2, SQRT5)) for a,b in zip(q0_target,q1_target))
    minus = tuple(sub(scal(a/2, ONE), scal(b/2, SQRT5)) for a,b in zip(q0_target,q1_target))
    check("G4 multiplicative pair=H,uH", plus == hc and minus == tuple(u(z) for z in hc),
          "B=+/-1/2 are the two norm embeddings")

    # G5: face weights.
    q0_face = []
    q1_face = []
    h_face = []
    for k in range(5):
        xk = add(ONE, jpow(k))
        q0_face.append(q0_field(xk))
        q1_face.append(q1_field(xk))
        h_face.append(kplus_pair(H(xk)))
    check("G5 q0 face vector", tuple(q0_face) == (F(8),F(3),F(3),F(3),F(3)),
          "(8,3,3,3,3)")
    check("G5 q1 face vector", tuple(q1_face) == (F(0),F(1),F(-1),F(-1),F(1)),
          "(0,1,-1,-1,1)")
    target_faces = (
        (F(4),F(0)),
        (F(3,2),F(1,2)),
        (F(3,2),F(-1,2)),
        (F(3,2),F(-1,2)),
        (F(3,2),F(1,2)),
    )
    check("G5 exact face weights", tuple(h_face) == target_faces,
          "4,(3+s)/2,(3-s)/2,(3-s)/2,(3+s)/2")

    # G6: q0 alone loses the Galois sign channel.
    x1 = add(ONE, jpow(1))
    x2b = add(ONE, jpow(2))
    check("G6 invariant-only no-go", q0_field(x1) == q0_field(x2b) == 3 and H(x1) != H(x2b),
          "q0=3 on both, relative norms are conjugate and unequal")

    print("TWIST-J P-J-QUADRATIC-CARRY-NORM-SEAM-2")
    print("exact arithmetic in Q(zeta_5); no floats")
    print("q0 coefficients:", ",".join(str(x) for x in q0_target))
    print("q1 coefficients:", ",".join(str(x) for x in q1_target))
    print("difference gcd:", g)
    print("common mod2:", "e2")
    print("face q0:", ",".join(str(x) for x in q0_face))
    print("face q1:", ",".join(str(x) for x in q1_face))
    print("face H (A+B*sqrt5):", ";".join(fmt_pair(x) for x in h_face))
    print()
    for i, (name, ok, detail) in enumerate(CHECKS, 1):
        print("PASS %02d %s :: %s" % (i, name, detail) if ok else
              "FAIL %02d %s :: %s" % (i, name, detail))
    print()
    print("RESULT %d/%d SEAM-CERTIFIED" % (len(CHECKS), len(CHECKS)))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print("ROUTE-FALSIFIED", str(exc))
        raise SystemExit(1)
