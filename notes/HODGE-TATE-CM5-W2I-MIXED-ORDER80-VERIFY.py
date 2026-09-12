#!/usr/bin/env python3
"""Exact verifier for the corrected CM5 W2I mixed order-80 quotient note.

NON-CANONICAL. Standard library only. No floating point.

The key guard in this version is that bar Q is recomputed directly from the
original six-term W2E form and the quotient basis; its quotient coordinates are
not taken as input.
"""

from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt
from pathlib import Path
import runpy

HERE = Path(__file__).resolve().parent
W2E = HERE / "HODGE-TATE-CM5-PERRY-W2E-A-THETA-VERIFY.py"
ns = runpy.run_path(str(W2E))

pass2 = ns["pass2"]
A_MINUS = ns["A_MINUS"]
A_PLUS = ns["A_PLUS"]
eval_Q = ns["eval_Q"]


def det_fraction(M):
    A = [[Fraction(x) for x in row] for row in M]
    n = len(A)
    out = Fraction(1)
    for k in range(n):
        pivot = next((r for r in range(k, n) if A[r][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            A[k], A[pivot] = A[pivot], A[k]
            out = -out
        p = A[k][k]
        out *= p
        for j in range(k, n):
            A[k][j] /= p
        for i in range(k + 1, n):
            f = A[i][k]
            if f:
                for j in range(k, n):
                    A[i][j] -= f * A[k][j]
    return out


def transpose(A):
    return [list(row) for row in zip(*A)]


def matmul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def transform_form(B, L):
    return matmul(transpose(B), matmul(L, B))


def blockdiag(A, B):
    m, n = len(A), len(B)
    out = [[Fraction(0) for _ in range(m + n)] for _ in range(m + n)]
    for i in range(m):
        for j in range(m):
            out[i][j] = Fraction(A[i][j])
    for i in range(n):
        for j in range(n):
            out[m + i][m + j] = Fraction(B[i][j])
    return out


# Chosen W2E-passing two-primary plane.
H2 = (
    (1, 0, 1, 0, 0, 0, 0, 0),
    (0, 1, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 0, 1, 0),
    (0, 0, 0, 0, 0, 1, 0, 0),
)
assert H2 in pass2

L8 = blockdiag(
    [[2 * x for x in row] for row in A_MINUS],
    [[2 * x for x in row] for row in A_PLUS],
)

# Mixed quotient basis.
Bmix = [
    [1, 0, Fraction(1, 2), 0, 0, 0, Fraction(1, 10), 0],
    [0, Fraction(1, 2), 0, 0, 0, 0, Fraction(3, 10), 0],
    [0, 0, Fraction(1, 2), 0, 0, 0, Fraction(1, 10), 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, Fraction(1, 10), 0],
    [0, 0, 0, 0, 0, Fraction(1, 2), Fraction(3, 10), 0],
    [0, 0, 0, 0, 0, 0, Fraction(1, 10), 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
]
assert det_fraction(Bmix) == Fraction(1, 80)

Lmix = transform_form(Bmix, L8)
EXPECTED_MIX = [
    [0, 2, -1, 2, 0, 0, 1, 0],
    [-2, 0, 0, -1, 0, 0, 0, 0],
    [1, 0, 0, 3, 0, 0, 0, 0],
    [-2, 1, -3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 2, -2],
    [0, 0, 0, 0, -3, 0, 0, 1],
    [-1, 0, 0, 0, -2, 0, 0, 1],
    [0, 0, 0, 0, 2, -1, -1, 0],
]
assert Lmix == [[Fraction(x) for x in row] for row in EXPECTED_MIX]
assert det_fraction(Lmix) == 25

entry_gcd = 0
for row in EXPECTED_MIX:
    for x in row:
        entry_gcd = gcd(entry_gcd, abs(x))
assert entry_gcd == 1
assert isqrt(int(det_fraction(Lmix))) == 5
assert any(int(x) % 2 for row in EXPECTED_MIX for x in row)

# Recompute Qbar directly from W2E Q and Bmix.
cols = [tuple(Bmix[i][j] for i in range(8)) for j in range(8)]
Qbar = {}
for six in combinations(range(8), 6):
    value = eval_Q([cols[j] for j in six])
    if value:
        Qbar[six] = value

EXPECTED_QBAR = {
    (0, 1, 2, 3, 4, 5): Fraction(5),
    (0, 1, 2, 3, 4, 6): Fraction(3),
    (0, 1, 2, 3, 6, 7): Fraction(1),
    (0, 1, 3, 4, 5, 6): Fraction(-1),
    (0, 1, 4, 5, 6, 7): Fraction(1),
    (0, 2, 3, 4, 5, 6): Fraction(3),
    (2, 3, 4, 5, 6, 7): Fraction(1),
}
assert Qbar == EXPECTED_QBAR
assert all(v.denominator == 1 for v in Qbar.values())
qgcd = 0
for v in Qbar.values():
    qgcd = gcd(qgcd, abs(v.numerator))
assert qgcd == 1

print("chosen H2 passes W2E           = yes")
print("mixed quotient index           =", 1 // det_fraction(Bmix))
print("mixed polarization determinant =", det_fraction(Lmix))
print("mixed polarization type        = (1,1,1,5)")
print("corrected Qbar coefficients    =", Qbar)
print("Qbar primitive gcd             =", qgcd)
print("bar L divisible by 2           = no")
print("RESULT: corrected W2I mixed quotient verifier PASS")
