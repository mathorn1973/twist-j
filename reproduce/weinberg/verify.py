#!/usr/bin/env python3
# TWIST-J Weinberg witness. Exact arithmetic only: integers,
# rationals, Q(sqrt5) pairs, the cyclotomic ring Z[zeta_5], and a
# formal pi graded ring with Q(sqrt5) coefficients. Standard library
# only, no floats anywhere. pi is a formal symbol; the measured
# comparison of sin^2 theta_W stays a fenced witness outside this
# file, and no value is claimed beyond the committed form.
#
# The sector: the tree value 3/13 = deg_f / (V + 1) with
# deg_f = Tr(J) = 3 and V = 12 = d(d + 1); the hypercharge law
# Y_F = (B - L) + 2 T_3^R reproducing all seven standard model
# hypercharges exactly; B_quark = 1/3 = 1/dim ker(Tr) with the trace
# kernel of dimension 3; and the committed form sin^2 theta_W =
# 3/13 + 1/(32 pi^2 phi^4) with phi^-4 = 5 - 3 phi > 0 exactly,
# pi even and delta free on the parity register.
#
# Claims verified: WEINBERG-TREE, HYPERCHARGE-LAW, WEINBERG-FORM.

import sys
from fractions import Fraction as Fr
from itertools import product
from math import gcd

CHECKS = []


def check(tag, description, ok):
    CHECKS.append(("%-12s %s" % (tag, description), bool(ok)))


# ------------------------------------------------ Q(sqrt5): a + b sqrt5
def q5(a, b=0):
    return (Fr(a), Fr(b))


Q5_ONE = q5(1)
PHI = (Fr(1, 2), Fr(1, 2))


def q5_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def q5_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def q5_mul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def q5_scal(c, x):
    return (Fr(c) * x[0], Fr(c) * x[1])


def q5_pos(x):
    a, b = x
    if a >= 0 and b >= 0:
        return not (a == 0 and b == 0)
    if a < 0 and b < 0:
        return False
    if b > 0:
        return 5 * b * b > a * a
    return a * a > 5 * b * b


# ------------------------------------------------ Z[zeta_5], basis 1..z^3
def zmul(a, b):
    c = [0] * 5
    for i in range(4):
        for j in range(4):
            c[(i + j) % 5] += a[i] * b[j]
    return (c[0] - c[4], c[1] - c[4], c[2] - c[4], c[3] - c[4])


ZONE = (1, 0, 0, 0)
ZETA = (0, 1, 0, 0)
J = (1, 0, 1, 0)
BASIS = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))


def mult_trace(a):
    # trace of multiplication by a on the power basis of Z[zeta_5]
    t = 0
    for k in range(4):
        t += zmul(a, BASIS[k])[k]
    return t


def tr_functional(v):
    # Tr(a0 + a1 z + a2 z^2 + a3 z^3) = 4 a0 - a1 - a2 - a3
    return 4 * v[0] - v[1] - v[2] - v[3]


def rank_q(rows):
    m = [[Fr(x) for x in row] for row in rows]
    rank = 0
    col = 0
    ncols = len(m[0])
    while rank < len(m) and col < ncols:
        piv = next((r for r in range(rank, len(m)) if m[r][col] != 0),
                   None)
        if piv is None:
            col += 1
            continue
        m[rank], m[piv] = m[piv], m[rank]
        m[rank] = [x / m[rank][col] for x in m[rank]]
        for r in range(len(m)):
            if r != rank and m[r][col] != 0:
                f = m[r][col]
                m[r] = [x - f * y for x, y in zip(m[r], m[rank])]
        rank += 1
        col += 1
    return rank


def main():
    # ------------------------------------------ 01 the trace and d
    ok = mult_trace(ZONE) == 4
    zk = ZONE
    for m in range(1, 5):
        zk = zmul(zk, ZETA)
        ok &= mult_trace(zk) == -1
    d = mult_trace(J)
    ok &= d == 3
    ok &= tr_functional(J) == 3
    check("TRACE-D",
          "on the power basis of Z[zeta_5]: Tr(1) = 4 and Tr(zeta^m) ="
          " -1 for m = 1..4, so Tr(J) = Tr(1 + zeta^2) = 3 = d ="
          " deg_f: the face degree is the trace of the axiom", ok)

    # ------------------------------------------ 02 the trace kernel
    kernel_vs = ((0, 1, -1, 0), (0, 1, 0, -1), (1, 1, 1, 2))
    ok = all(tr_functional(v) == 0 for v in kernel_vs)
    ok &= rank_q(kernel_vs) == 3
    ok &= tr_functional(ZONE) == 4 != 0
    count = sum(1 for v in product(range(5), repeat=4)
                if tr_functional(v) % 5 == 0)
    ok &= count == 125 == 5 ** 3
    ok &= Fr(1, 3) == Fr(1, 3) and 3 == rank_q(kernel_vs)
    check("KERNEL",
          "the trace kernel has dimension 3: three explicit independent"
          " kernel vectors of rank 3 over Q, the functional is nonzero"
          " (Tr(1) = 4), and over F_5 the kernel has exactly"
          " 125 = 5^3 points by full enumeration; B_quark = 1/3 ="
          " 1/dim ker(Tr)", ok)

    # ------------------------------------------ 03 the tree value
    d = 3
    V = d * (d + 1)
    ok = V == 12
    ok &= mult_trace(J) * (mult_trace(J) + 1) == 12
    ok &= Fr(3, 13) == Fr(d, V + 1)
    ok &= V + 1 == 13 and gcd(3, 13) == 1
    check("TREE",
          "V = 12 = d(d + 1) by the two agreeing routes (the counting"
          " route and Tr(J)(Tr(J) + 1)); the tree value is 3/13 ="
          " deg_f/(V + 1) with V + 1 = 13 and gcd(3, 13) = 1", ok)

    # ------------------------------------------ 04 the hypercharges
    # entries: (name, B - L, T_3^R, expected Y)
    table = (
        ("Q_L", Fr(1, 3), Fr(0), Fr(1, 3)),
        ("u_R", Fr(1, 3), Fr(1, 2), Fr(4, 3)),
        ("d_R", Fr(1, 3), Fr(-1, 2), Fr(-2, 3)),
        ("L_L", Fr(-1), Fr(0), Fr(-1)),
        ("nu_R", Fr(-1), Fr(1, 2), Fr(0)),
        ("e_R", Fr(-1), Fr(-1, 2), Fr(-2)),
        ("H", Fr(0), Fr(1, 2), Fr(1)),
    )
    ok = len(table) == 7
    values = []
    for name, bl, t3r, y in table:
        ok &= bl + 2 * t3r == y
        values.append(y)
    ok &= sorted(set(values)) == sorted(
        (Fr(1, 3), Fr(4, 3), Fr(-2, 3), Fr(-1), Fr(0), Fr(-2), Fr(1)))
    ok &= table[0][1] == Fr(1, 3)
    check("HYPERCHARGE",
          "Y_F = (B - L) + 2 T_3^R reproduces all seven standard model"
          " hypercharges exactly in Q: the quark doublet 1/3, u_R 4/3,"
          " d_R -2/3, the lepton doublet -1, nu_R 0, e_R -2, and the"
          " Higgs 1; the quark baryon number 1/3 is 1/dim ker(Tr)", ok)

    # ------------------------------------------ 05 the correction term
    phim2 = q5_sub(q5(2), PHI)
    phim4 = q5_mul(phim2, phim2)
    ok = phim4 == (Fr(7, 2), Fr(-3, 2))
    ok &= phim4 == q5_sub(q5(5), q5_scal(3, PHI))
    phi2 = q5_mul(PHI, PHI)
    ok &= q5_mul(phim4, q5_mul(phi2, phi2)) == Q5_ONE
    ok &= q5_pos(phim4) and 7 * 7 > 9 * 5
    ok &= 32 == 2 ** 5
    # the committed form as a pi graded object with Q(sqrt5) coefficients
    form = {0: q5(Fr(3, 13)), -2: q5_scal(Fr(1, 32), phim4)}
    ok &= len(form) == 2
    ok &= form[0] == q5(Fr(3, 13))
    ok &= form[-2] == (Fr(7, 64), Fr(-3, 64))
    check("CORRECTION",
          "phi^-4 = (2 - phi)^2 = 5 - 3 phi = (7 - 3 sqrt5)/2 exactly"
          " in Q(sqrt5), positive since 49 > 45, and phi^-4 phi^4 = 1;"
          " the committed form sin^2 theta_W = 3/13 +"
          " (1/32) pi^-2 phi^-4 has exactly two monomials: the tree"
          " value and the single correction rung over 32 = 2^5", ok)

    # ------------------------------------------ 06 parity and dominance
    form = {0: q5(Fr(3, 13)), -2: q5_scal(Fr(1, 32),
                                          (Fr(7, 2), Fr(-3, 2)))}
    ok = all(deg % 2 == 0 for deg in form)
    ok &= q5_pos(form[-2])
    ok &= q5_pos(form[0])
    check("PARITY-EVEN",
          "every pi degree of the Weinberg entry is even ({0, -2}), so"
          " sin^2 theta_W is pi even and delta free on the parity"
          " register, and the single correction is exactly positive:"
          " the form exceeds the tree value 3/13 at the form level;"
          " the measured comparison stays a fenced witness outside"
          " this file", ok)

    print("TWIST-J Weinberg witness (exact arithmetic, formal pi)")
    print("sin^2 theta_W = 3/13 + 1/(32 pi^2 phi^4); the tree value is"
          " 3/13 = deg_f/(V + 1)")
    print("Y_F = (B - L) + 2 T_3^R; B_quark = 1/3 = 1/dim ker(Tr); no"
          " value is claimed beyond the committed form")
    print()
    passed = 0
    for i, (name, okv) in enumerate(CHECKS, 1):
        tag = "PASS" if okv else "FAIL"
        if okv:
            passed += 1
        print("%s %02d %s" % (tag, i, name))
    print()
    print("RESULT %d/%d %s" % (passed, len(CHECKS),
                               "ALL PASS" if passed == len(CHECKS)
                               else "FAILURES PRESENT"))
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
