#!/usr/bin/env python3
"""Exact verifier for W2I-B twisted perfect correction.

NON-CANONICAL. Standard library only. No floating point in the mathematical
checks. The corrected W2I quotient verifier is reused for B_mix, Lbar, and
Qbar; this script independently reconstructs the quotient Neron-Severi
certificate and the nine-term divisor decomposition.
"""

from fractions import Fraction
from itertools import combinations
from pathlib import Path
import runpy

HERE = Path(__file__).resolve().parent
W2I = HERE / "HODGE-TATE-CM5-W2I-MIXED-ORDER80-VERIFY.py"
qns = runpy.run_path(str(W2I))

Bmix = qns["Bmix"]
Lmix = qns["Lmix"]
Qbar = qns["EXPECTED_QBAR"]


def transpose(A):
    return [list(row) for row in zip(*A)]


def matmul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def matadd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matscale(c, A):
    return [[c * x for x in row] for row in A]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def blockdiag(A, B):
    m, n = len(A), len(B)
    out = [[0 for _ in range(m + n)] for _ in range(m + n)]
    for i in range(m):
        for j in range(m):
            out[i][j] = A[i][j]
    for i in range(n):
        for j in range(n):
            out[m + i][m + j] = B[i][j]
    return out


def matpow(A, n):
    out = eye(len(A))
    for _ in range(n):
        out = matmul(out, A)
    return out


def zero(n):
    return [[0] * n for _ in range(n)]


def form_from_matrix(M):
    return {
        (i, j): Fraction(M[i][j])
        for i in range(len(M))
        for j in range(i + 1, len(M))
        if M[i][j]
    }


def add_forms(*forms):
    out = {}
    for F in forms:
        for key, value in F.items():
            out[key] = out.get(key, Fraction(0)) + value
    return {k: v for k, v in out.items() if v}


def scale_form(c, F):
    c = Fraction(c)
    return {k: c * v for k, v in F.items() if c * v}


def wedge(A, B):
    out = {}
    for I, a in A.items():
        for J, b in B.items():
            if set(I) & set(J):
                continue
            inv = sum(1 for i in I for j in J if i > j)
            K = tuple(sorted(I + J))
            out[K] = out.get(K, Fraction(0)) + a * b * ((-1) ** inv)
    return {k: v for k, v in out.items() if v}


def top(F):
    return F.get(tuple(range(8)), Fraction(0))


# ---------------------------------------------------------------------------
# Integral CM5 NS basis upstairs
# ---------------------------------------------------------------------------

OMEGA = [
    [0, 1, 0, 0],
    [-1, 0, 1, 0],
    [0, -1, 0, 1],
    [0, 0, -1, 0],
]

R = [
    [-1, 2, 0, -2],
    [0, 1, 2, -2],
    [-2, 2, 1, 0],
    [-2, 0, 2, -1],
]

PHI = [[(eye(4)[i][j] + R[i][j]) // 2 for j in range(4)] for i in range(4)]

MJ = [
    [0, 0, 0, -1],
    [1, 0, 0, -1],
    [0, 1, 0, -1],
    [0, 0, 1, -1],
]

MJINV = [
    [-1, 1, 0, 0],
    [-1, 0, 1, 0],
    [-1, 0, 0, 1],
    [-1, 0, 0, 0],
]

Z4 = zero(4)

N = []
N.append(blockdiag(OMEGA, Z4))
N.append(blockdiag(matmul(OMEGA, PHI), Z4))
N.append(blockdiag(Z4, OMEGA))
N.append(blockdiag(Z4, matmul(OMEGA, PHI)))

for k in range(4):
    A = matpow(MJ, k)
    Abar = matpow(MJINV, k)
    top_right = matmul(OMEGA, A)
    bottom_left = matmul(OMEGA, Abar)
    E = [[0] * 8 for _ in range(8)]
    for i in range(4):
        for j in range(4):
            E[i][4 + j] = top_right[i][j]
            E[4 + i][j] = bottom_left[i][j]
    # Hermitian symmetry makes E alternating.
    assert all(E[i][j] == -E[j][i] for i in range(8) for j in range(8))
    N.append(E)

assert len(N) == 8

# Columns define pullbacks of quotient divisor classes D_0,...,D_7.
C = [
    [0, -12, 0, 0, -8, 2, 10, -2],
    [0, 0, 0, 0, 6, 0, -10, 2],
    [-10, 0, 0, -8, 0, -6, 0, -2],
    [10, -4, 10, 6, 0, 6, 0, 2],
    [0, -4, -20, 0, 0, -2, 0, 2],
    [0, -4, 0, 0, 0, 0, 0, 0],
    [0, -4, 0, 0, 0, 0, 0, 2],
    [0, -16, -20, 0, 0, 0, 0, 2],
]

Dmat = []
for col in range(8):
    pull = [[0] * 8 for _ in range(8)]
    for r in range(8):
        pull = matadd(pull, matscale(C[r][col], N[r]))
    descended = matmul(transpose(Bmix), matmul(pull, Bmix))
    assert all(Fraction(x).denominator == 1 for row in descended for x in row)
    Dmat.append(descended)

D = [form_from_matrix(M) for M in Dmat]

# ---------------------------------------------------------------------------
# Nine-term divisor identity
# ---------------------------------------------------------------------------

coeffs = {
    (0, 3, 6): 1,
    (0, 5, 7): 2,
    (0, 7, 7): 2,
    (2, 3, 7): 1,
    (2, 4, 7): -1,
    (2, 7, 7): -2,
    (3, 3, 4): 1,
    (3, 4, 7): 2,
    (5, 6, 7): -1,
}

cycle = {}
top_defect = Fraction(0)
individual_tops = {}

for (i, j, k), c in coeffs.items():
    triple = wedge(wedge(D[i], D[j]), D[k])
    cycle = add_forms(cycle, scale_form(c, triple))
    sum_div = add_forms(D[i], D[j], D[k])
    t = -Fraction(1, 2) * top(wedge(triple, sum_div))
    individual_tops[(i, j, k)] = t
    top_defect += c * t

assert cycle == Qbar
assert individual_tops == {
    (0, 3, 6): Fraction(-125),
    (0, 5, 7): Fraction(-15),
    (0, 7, 7): Fraction(-10),
    (2, 3, 7): Fraction(90),
    (2, 4, 7): Fraction(0),
    (2, 7, 7): Fraction(-50),
    (3, 3, 4): Fraction(-10),
    (3, 4, 7): Fraction(-12),
    (5, 6, 7): Fraction(-10),
}
assert top_defect == -9

Lform = form_from_matrix(Lmix)
LQ = top(wedge(Lform, Qbar))
assert LQ == 10

# K_Q has ch = Qbar - 9 pt. Add four points on the base:
# ch(K_Q') = Qbar - 5 pt. Tensoring by the weight-one root M multiplies
# by exp(L/2), adding +(L.Qbar)/2 = +5 pt, so the top term cancels.
base_top_after_four_points = top_defect + 4
weight_one_top = base_top_after_four_points + Fraction(1, 2) * LQ
assert base_top_after_four_points == -5
assert weight_one_top == 0

print("quotient divisor classes integral = 8/8")
print("bar Q triple-divisor identity     = PASS")
print("Koszul top defect                 =", top_defect)
print("Lbar.Qbar                         =", LQ)
print("base top after four points        =", base_top_after_four_points)
print("weight-one top after root twist   =", weight_one_top)
print("RESULT: W2I-B twisted perfect correction PASS")
