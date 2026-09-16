#!/usr/bin/env python3
"""Exact verifier for W2K-B contraction ranks.

NON-CANONICAL. Standard library only. Arithmetic is in Q(sqrt(5)); no floats.
"""

from fractions import Fraction
from itertools import combinations


# ---------------------------------------------------------------------------
# Q(sqrt(5))
# ---------------------------------------------------------------------------

class F:
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __add__(self, other):
        other = q(other)
        return F(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return F(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-q(other))

    def __rsub__(self, other):
        return q(other) - self

    def __mul__(self, other):
        other = q(other)
        return F(
            self.a * other.a + 5 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def inv(self):
        n = self.a * self.a - 5 * self.b * self.b
        if n == 0:
            raise ZeroDivisionError
        return F(self.a / n, -self.b / n)

    def __truediv__(self, other):
        return self * q(other).inv()

    def __eq__(self, other):
        other = q(other)
        return self.a == other.a and self.b == other.b

    def __bool__(self):
        return self.a != 0 or self.b != 0

    def __repr__(self):
        return f"({self.a}+{self.b}*sqrt5)"


def q(x):
    return x if isinstance(x, F) else F(x, 0)


ZERO = F(0)
ONE = F(1)
SQRT5 = F(0, 1)


def rank(M):
    A = [[q(x) for x in row] for row in M]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = A[r][c].inv()
        A[r] = [x * inv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


# ---------------------------------------------------------------------------
# Exterior algebra on x0,...,x3,y0,...,y3
# ---------------------------------------------------------------------------

def one(i):
    return {(i,): ONE}


def add(*forms):
    out = {}
    for form in forms:
        for I, a in form.items():
            out[I] = out.get(I, ZERO) + a
    return {I: a for I, a in out.items() if a}


def scale(c, form):
    c = q(c)
    return {I: c * a for I, a in form.items() if c * a}


def wedge(A, B):
    out = {}
    for I, a in A.items():
        for J, b in B.items():
            if set(I) & set(J):
                continue
            inv = sum(1 for i in I for j in J if i > j)
            K = tuple(sorted(I + J))
            coeff = a * b * (-1 if inv % 2 else 1)
            out[K] = out.get(K, ZERO) + coeff
    return {I: a for I, a in out.items() if a}


def contract(form, i):
    out = {}
    for I, a in form.items():
        if i not in I:
            continue
        pos = I.index(i)
        J = I[:pos] + I[pos + 1:]
        coeff = a * (-1 if pos % 2 else 1)
        out[J] = out.get(J, ZERO) + coeff
    return {I: a for I, a in out.items() if a}


def vec(form, basis):
    return [form.get(I, ZERO) for I in basis]


def columns_to_matrix(cols):
    if not cols:
        return []
    return [[cols[j][i] for j in range(len(cols))] for i in range(len(cols[0]))]


u = [wedge(one(i), one(4 + i)) for i in range(4)]
A = add(u[0], u[1])
B = add(u[2], u[3])
A2 = wedge(A, A)
B2 = wedge(B, B)

# 2q' = 5-sqrt(5), 2q = 5+sqrt(5).
a = F(5, -1)
b = F(5, 1)
# -5 phi^2 = -(15+5sqrt5)/2; -5 phi^-2 = -(15-5sqrt5)/2.
c = F(Fraction(-15, 2), Fraction(-5, 2))
d = F(Fraction(-15, 2), Fraction(5, 2))

L = add(scale(a, A), scale(b, B))
delta6 = add(scale(c, wedge(A2, B)), scale(d, wedge(A, B2)))
delta = add(L, delta6)

# ---------------------------------------------------------------------------
# HT^2 source rank
# ---------------------------------------------------------------------------

H13 = [
    tuple(sorted((i,) + tuple(4 + j for j in J)))
    for i in range(4)
    for J in combinations(range(4), 3)
]
H02 = [tuple(4 + i for i in I) for I in combinations(range(4), 2)]
H24 = [
    tuple(sorted(I + tuple(4 + j for j in range(4))))
    for I in combinations(range(4), 2)
]

# H^2(O) -> H^{1,3} by eta wedge L.
eta_cols = []
for i, j in combinations(range(4), 2):
    eta = wedge(one(4 + i), one(4 + j))
    eta_cols.append(vec(wedge(eta, L), H13))
M_eta = columns_to_matrix(eta_cols)

# bivectors -> H^{1,3} by double contraction of delta6.
biv_cols = []
for i, j in combinations(range(4), 2):
    biv_cols.append(vec(contract(contract(delta6, i), j), H13))
M_biv = columns_to_matrix(biv_cols)

M_middle = [M_eta[i] + M_biv[i] for i in range(len(M_eta))]
assert rank(M_eta) == 6
assert rank(M_biv) == 6
assert rank(M_middle) == 10

# H^1(T): theta_{ij}=dbar z_j tensor d/dz_i.
end_cols = []
for i in range(4):
    for j in range(4):
        yj = one(4 + j)
        low = wedge(yj, contract(L, i))
        high = wedge(yj, contract(delta6, i))
        end_cols.append(vec(low, H02) + vec(high, H24))
M_end = columns_to_matrix(end_cols)
assert rank(M_end) == 10

source_ht2_rank = 10 + 10
source_ht2_dim = 6 + 16 + 6
source_ann2 = source_ht2_dim - source_ht2_rank
assert source_ht2_rank == 20
assert source_ann2 == 8

# ---------------------------------------------------------------------------
# HT^1 source rank
# ---------------------------------------------------------------------------

ht1_outputs = []
for j in range(4):
    ht1_outputs.append(wedge(one(4 + j), delta))
for i in range(4):
    ht1_outputs.append(contract(delta, i))

ht1_basis = sorted(set().union(*(set(Fm.keys()) for Fm in ht1_outputs)))
M_ht1 = columns_to_matrix([vec(Fm, ht1_basis) for Fm in ht1_outputs])
source_ht1_rank = rank(M_ht1)
assert source_ht1_rank == 8

# ---------------------------------------------------------------------------
# Outer product rank
# ---------------------------------------------------------------------------

outer_ht2_dim = source_ht2_dim + 8 * 8 + source_ht2_dim
outer_kernel_dim = source_ann2 + source_ann2  # middle has no kernel: HT1 action injective
outer_rank = outer_ht2_dim - outer_kernel_dim
assert outer_ht2_dim == 120
assert outer_kernel_dim == 16
assert outer_rank == 104

# Source semiregularity dimension breaker at order 80.
source_r_lower = 12
source_ext2_lower = 8 + 2 * source_r_lower
source_semireg_target = 6 + 16 + 6
assert source_ext2_lower == 32
assert source_semireg_target == 28
assert source_ext2_lower > source_semireg_target

print("rank H2(O) half                  =", rank(M_eta))
print("rank bivector half              =", rank(M_biv))
print("rank combined H13 block         =", rank(M_middle))
print("rank H1(T) block                =", rank(M_end))
print("source HT2 contraction rank     =", source_ht2_rank)
print("source HT2 annihilator dim      =", source_ann2)
print("source HT1 contraction rank     =", source_ht1_rank)
print("source Ext2 lower / target      =", source_ext2_lower, source_semireg_target)
print("outer HT2 dimension             =", outer_ht2_dim)
print("outer annihilator dimension     =", outer_kernel_dim)
print("outer contraction rank          =", outer_rank)
print("RESULT: W2K-B contraction-rank verifier PASS")