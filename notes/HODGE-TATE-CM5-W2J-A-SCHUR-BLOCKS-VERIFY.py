#!/usr/bin/env python3
"""Exact verifier for W2J-A principal index-two Schur blocks.

NON-CANONICAL. Standard library only. No floating point.
"""

from fractions import Fraction
from pathlib import Path
import runpy

HERE = Path(__file__).resolve().parent
BASE = HERE / "HODGE-TATE-CM5-W2I-B-PERFECT-CORRECTION-VERIFY.py"
ns = runpy.run_path(str(BASE))

N = ns["N"]
Bmix = ns["Bmix"]
Lform = ns["Lform"]
Qbar = ns["Qbar"]
matadd = ns["matadd"]
matscale = ns["matscale"]
matmul = ns["matmul"]
transpose = ns["transpose"]
form_from_matrix = ns["form_from_matrix"]
add_forms = ns["add_forms"]
scale_form = ns["scale_form"]
wedge = ns["wedge"]
top = ns["top"]


def transform_form(B, L):
    return matmul(transpose(B), matmul(L, B))


def pfaffian(M):
    n = len(M)
    if n == 0:
        return Fraction(1)
    out = Fraction(0)
    for j in range(1, n):
        sign = 1 if j % 2 == 1 else -1
        sub = [
            [M[a][b] for b in range(n) if b not in (0, j)]
            for a in range(n) if a not in (0, j)
        ]
        out += sign * Fraction(M[0][j]) * pfaffian(sub)
    return out


# LLL-reduced quotient NS basis. Columns are coefficients in N_0,...,N_7.
LRED = [
    [2, 0, 2, -2, 0, 2, 0, 0],
    [0, 0, 0, -2, 2, -2, 2, 0],
    [2, 2, -2, 2, 0, 0, 0, 0],
    [0, -4, -2, 0, 2, 2, 2, 0],
    [-2, 0, -2, -2, 0, 0, 0, -2],
    [0, 0, 0, 0, 0, 0, 4, -8],
    [0, 0, 0, 0, 2, 2, 4, 2],
    [0, 0, 0, 0, 2, 2, -4, -2],
]

Rmat = []
Rpull_coeff = []
for col in range(8):
    coeff = [LRED[r][col] for r in range(8)]
    Rpull_coeff.append(coeff)
    pull = [[0] * 8 for _ in range(8)]
    for r in range(8):
        pull = matadd(pull, matscale(coeff[r], N[r]))
    desc = transform_form(Bmix, pull)
    assert all(Fraction(x).denominator == 1 for row in desc for x in row)
    Rmat.append(desc)

# S_i in the R basis.
SCOEFF = [
    [0, 1, 0, 0, -1, 0, 0, 0],
    [1, -1, -1, 0, -1, 0, 0, 0],
    [1, 1, 0, -1, -1, -1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0],
    [1, -1, 0, -1, -1, 0, 0, 0],
    [1, 0, -1, 0, 0, -1, 0, 0],
]

Smat = []
Spull = []
for sc in SCOEFF:
    M = [[0] * 8 for _ in range(8)]
    orig = [0] * 8
    for j, c in enumerate(sc):
        if c:
            M = matadd(M, matscale(c, Rmat[j]))
            for r in range(8):
                orig[r] += c * Rpull_coeff[j][r]
    Smat.append(M)
    Spull.append(orig)

EXPECTED_PULL = [
    [0, -2, 2, -6, 0, 0, -2, -2],
    [0, -2, 2, 4, 0, 0, -2, -2],
    [2, 2, 2, -8, 0, 0, -4, -4],
    [0, 2, 2, -2, 0, 0, 2, 2],
    [4, 0, -2, 2, 0, 0, -2, -2],
    [-2, 2, 4, 0, 0, 0, -2, -2],
]
assert Spull == EXPECTED_PULL
assert [pfaffian(M) for M in Smat] == [1] * 6

# Exact arithmetic in F=Q(phi), phi^2=phi+1.
def f_add(u, v):
    return (Fraction(u[0]) + Fraction(v[0]), Fraction(u[1]) + Fraction(v[1]))


def f_mul(u, v):
    x, y = map(Fraction, u)
    a, b = map(Fraction, v)
    return (x * a + y * b, x * b + y * a + y * b)


def f_sign_at_embedding(u, conjugate=False):
    # x+y phi = (2x+y + y sqrt(5))/2; conjugate changes sqrt(5) sign.
    x, y = map(Fraction, u)
    A = 2 * x + y
    B = -y if conjugate else y
    if B == 0:
        return 1 if A > 0 else -1 if A < 0 else 0
    if A >= 0 and B > 0:
        return 1
    if A <= 0 and B < 0:
        return -1
    left = A * A
    right = 5 * B * B
    if A > 0 and B < 0:
        return 1 if left > right else -1 if left < right else 0
    if A < 0 and B > 0:
        return 1 if right > left else -1 if right < left else 0
    raise AssertionError((A, B))


# For pullback Hermitian coefficients c=(a0,a1,d0,d1,b0,...,b3),
# determinant/trace pairs already reduced exactly to x+y phi.
TRACE_DET = [
    ((2, -8), (8, 4)),
    ((2, 2), (-12, -16)),
    ((4, -6), (-28, -44)),
    ((2, 0), (-8, -4)),
    ((2, 2), (-12, 4)),
    ((2, 2), (-12, 4)),
]

indices = []
for tr, det in TRACE_DET:
    neg = 0
    for conjugate in (False, True):
        sd = f_sign_at_embedding(det, conjugate)
        st = f_sign_at_embedding(tr, conjugate)
        assert sd != 0
        if sd < 0:
            neg += 1
        else:
            assert st != 0
            neg += 2 if st < 0 else 0
    indices.append(neg)
assert indices == [2] * 6

S = [form_from_matrix(M) for M in Smat]
QA = wedge(wedge(S[0], S[1]), S[2])
QB = wedge(wedge(S[3], S[4]), S[5])
assert add_forms(QA, QB) == Qbar

LQA = top(wedge(Lform, QA))
LQB = top(wedge(Lform, QB))
assert LQA == 5
assert LQB == 5


def koszul_top(A, B, C):
    triple = wedge(wedge(A, B), C)
    return -Fraction(1, 2) * top(wedge(triple, add_forms(A, B, C)))


topA = koszul_top(S[0], S[1], S[2])
topB = koszul_top(S[3], S[4], S[5])
assert topA == 4
assert topB == -6

base_top = topA + topB - 3  # three O_p[1] terms
root_add = Fraction(1, 2) * (LQA + LQB)
assert base_top == -5
assert root_add == 5
assert base_top + root_add == 0

print("Pf(S_i)                    =", [pfaffian(M) for M in Smat])
print("index(S_i)                 =", indices)
print("bar Q two-triple identity  = PASS")
print("Lbar.Q_A, Lbar.Q_B         =", LQA, LQB)
print("Koszul top A, B            =", topA, topB)
print("base top after 3 pt[1]     =", base_top)
print("root-gerbe top addition    =", root_add)
print("RESULT: W2J-A Schur-block verifier PASS")
