#!/usr/bin/env python3
"""Exact finite audit for the CM5 Perry/theta-symmetry W2E-A note.

NON-CANONICAL. Standard-library only. No floating point.

Checks:
  * Smith invariants of the q and q' polarization blocks;
  * all 156 five-primary Lagrangian planes and Q-descent;
  * all 2295 two-primary Lagrangian 4-planes and Q-descent;
  * the exact count 85 * 156 = 13260 of order-80 candidates;
  * the invariant-Ext dimension threshold h >= 100.
"""

from fractions import Fraction
from itertools import combinations, product
from math import gcd


# ---------------------------------------------------------------------------
# Exact integer linear algebra
# ---------------------------------------------------------------------------

def det_int(M):
    """Bareiss exact determinant."""
    A = [list(map(int, row)) for row in M]
    n = len(A)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            pivot = next((r for r in range(k + 1, n) if A[r][k] != 0), None)
            if pivot is None:
                return 0
            A[k], A[pivot] = A[pivot], A[k]
            sign = -sign
        p = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * p - A[i][k] * A[k][j]) // prev
        prev = p
        for i in range(k + 1, n):
            A[i][k] = 0
    return sign * A[-1][-1]


def det_fraction(M):
    A = [[Fraction(x) for x in row] for row in M]
    n = len(A)
    if n == 0:
        return Fraction(1)
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


def smith_invariants_by_minors(A):
    """Smith invariant factors from determinantal divisors."""
    m, n = len(A), len(A[0])
    r = min(m, n)
    delta = [1]
    for k in range(1, r + 1):
        g = 0
        for rows in combinations(range(m), k):
            for cols in combinations(range(n), k):
                d = abs(det_int([[A[i][j] for j in cols] for i in rows]))
                g = gcd(g, d)
        delta.append(g)
    return tuple(delta[k] // delta[k - 1] for k in range(1, r + 1))


def rref_mod(rows, p):
    A = [[int(x) % p for x in row] for row in rows if any(int(x) % p for x in row)]
    if not A:
        return tuple()
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = pow(A[r][c], -1, p)
        A[r] = [(x * inv) % p for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [(A[i][j] - f * A[r][j]) % p for j in range(n)]
        r += 1
        if r == m:
            break
    return tuple(tuple(row) for row in A[:r])


def rank_mod(A, p):
    return len(rref_mod(A, p))


def pair_mod(v, w, J, p):
    return sum(v[i] * J[i][j] * w[j] for i in range(len(v)) for j in range(len(w))) % p


# ---------------------------------------------------------------------------
# CM5 integral matrices
# ---------------------------------------------------------------------------

# Canonical principal alternating form Omega_1 on one B factor.
OMEGA = [
    [0, 1, 0, 0],
    [-1, 0, 1, 0],
    [0, -1, 0, 1],
    [0, 0, -1, 0],
]

# Multiplication by sqrt(5) in the integral basis (1,j,j^2,j^3).
R = [
    [-1, 2, 0, -2],
    [0, 1, 2, -2],
    [-2, 2, 1, 0],
    [-2, 0, 2, -1],
]

I4 = [[int(i == j) for j in range(4)] for i in range(4)]


def mat_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mat_scale(c, A):
    return [[c * x for x in row] for row in A]


def mat_mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


QPLUS = [[x // 2 for x in row] for row in mat_add(mat_scale(5, I4), R)]
QMINUS = [[x // 2 for x in row] for row in mat_sub(mat_scale(5, I4), R)]

assert smith_invariants_by_minors(QPLUS) == (1, 1, 5, 5)
assert smith_invariants_by_minors(QMINUS) == (1, 1, 5, 5)
assert smith_invariants_by_minors(mat_scale(2, QPLUS)) == (2, 2, 10, 10)
assert smith_invariants_by_minors(mat_scale(2, QMINUS)) == (2, 2, 10, 10)


# ---------------------------------------------------------------------------
# The exact codimension-three correction form Q
# ---------------------------------------------------------------------------

# Integral dual H^1 basis x_0,...,x_7. The value is
#   Q = 40 * sum_I x_I
# over these six ordered 6-tuples I.
Q_SUPPORT = {
    (0, 1, 2, 3, 4, 5): 40,
    (0, 1, 2, 3, 5, 6): 40,
    (0, 1, 2, 3, 6, 7): 40,
    (0, 1, 4, 5, 6, 7): 40,
    (1, 2, 4, 5, 6, 7): 40,
    (2, 3, 4, 5, 6, 7): 40,
}


def eval_Q(vectors):
    assert len(vectors) == 6
    total = Fraction(0)
    for cols, coeff in Q_SUPPORT.items():
        M = [[v[c] for c in cols] for v in vectors]
        total += coeff * det_fraction(M)
    return total


STD = [tuple(Fraction(int(i == j)) for j in range(8)) for i in range(8)]


# ---------------------------------------------------------------------------
# Five-primary audit
# ---------------------------------------------------------------------------

# Kernel basis on one B factor, modulo 5.
u1 = (1, 3, 1, 0)
u2 = (2, 2, 0, 1)
BASIS5 = [
    u1 + (0, 0, 0, 0),
    u2 + (0, 0, 0, 0),
    (0, 0, 0, 0) + u1,
    (0, 0, 0, 0) + u2,
]

# Weil pairing in this basis. First block is q', second is q.
J5 = [
    [0, 3, 0, 0],
    [2, 0, 0, 0],
    [0, 0, 0, 2],
    [0, 0, 3, 0],
]


def all_2planes_F5():
    vectors = [v for v in product(range(5), repeat=4) if any(v)]
    out = set()
    for i, v in enumerate(vectors):
        for w in vectors[i + 1:]:
            rr = rref_mod([v, w], 5)
            if len(rr) == 2:
                out.add(rr)
    return out


def coord_to_std(c, p, basis):
    return tuple(sum(c[k] * basis[k][i] for k in range(len(c))) % p for i in range(8))


def five_descent_ok(rr):
    hs = [coord_to_std(row, 5, BASIS5) for row in rr]
    frac = [tuple(Fraction(x, 5) for x in h) for h in hs]
    gens = STD + frac
    for six in combinations(range(len(gens)), 6):
        if eval_Q([gens[i] for i in six]).denominator != 1:
            return False
    return True


planes5 = all_2planes_F5()
lag5 = [rr for rr in planes5 if pair_mod(rr[0], rr[1], J5, 5) == 0]
pass5 = [rr for rr in lag5 if five_descent_ok(rr)]

assert len(planes5) == 806
assert len(lag5) == 156
assert len(pass5) == 0

# A compact exact witness for one Lagrangian plane.
WITNESS_PLANE = ((0, 1, 0, 0), (0, 0, 0, 1))
h1 = coord_to_std(WITNESS_PLANE[0], 5, BASIS5)
h2 = coord_to_std(WITNESS_PLANE[1], 5, BASIS5)
witness_value = eval_Q([
    STD[0], STD[1], STD[2], STD[4],
    tuple(Fraction(x, 5) for x in h1),
    tuple(Fraction(x, 5) for x in h2),
])
assert witness_value == Fraction(-16, 5)


# ---------------------------------------------------------------------------
# Two-primary audit
# ---------------------------------------------------------------------------

# The polarization L is 2M. K(L)[2] is all F_2^8, and its pairing is M mod 2.
A_MINUS = mat_mul(OMEGA, QMINUS)
A_PLUS = mat_mul(OMEGA, QPLUS)
J2 = [[0] * 8 for _ in range(8)]
for i in range(4):
    for j in range(4):
        J2[i][j] = A_MINUS[i][j] % 2
        J2[i + 4][j + 4] = A_PLUS[i][j] % 2
assert rank_mod(J2, 2) == 8


def rref_subspaces_F2(n, k):
    """Generate every k-plane of F_2^n exactly once in RREF."""
    for pivots in combinations(range(n), k):
        pivset = set(pivots)
        base = [[0] * n for _ in range(k)]
        free = []
        for r, pcol in enumerate(pivots):
            base[r][pcol] = 1
            for c in range(pcol + 1, n):
                if c not in pivset:
                    free.append((r, c))
        for bits in range(1 << len(free)):
            rows = [row[:] for row in base]
            for bit, (r, c) in enumerate(free):
                if (bits >> bit) & 1:
                    rows[r][c] = 1
            yield tuple(tuple(row) for row in rows)


def det_mod2(M):
    return int(rank_mod(M, 2) == len(M))


def eval_Q_reduced_mod2(vectors):
    # Only Q/40 matters modulo 2 for the four half-lattice generators.
    out = 0
    for cols in Q_SUPPORT:
        M = [[v[c] % 2 for c in cols] for v in vectors]
        out ^= det_mod2(M)
    return out


def two_descent_ok(rr):
    # With four half-lattice generators, denominators < 2^4 are absorbed by 40.
    # Only evaluations containing all four half-generators can have a remaining 2.
    for i, j in combinations(range(8), 2):
        ei = tuple(int(k == i) for k in range(8))
        ej = tuple(int(k == j) for k in range(8))
        if eval_Q_reduced_mod2(list(rr) + [ei, ej]):
            return False
    return True


all4 = 0
lag2 = []
for rr in rref_subspaces_F2(8, 4):
    all4 += 1
    isotropic = True
    for i in range(4):
        for j in range(i + 1, 4):
            if pair_mod(rr[i], rr[j], J2, 2):
                isotropic = False
                break
        if not isotropic:
            break
    if isotropic:
        lag2.append(rr)

pass2 = [rr for rr in lag2 if two_descent_ok(rr)]

assert all4 == 200787
assert len(lag2) == 2295
assert len(pass2) == 85

# Every 1-dimensional subspace of F_5^4 is isotropic: 156 such lines.
lines5 = (5**4 - 1) // (5 - 1)
assert lines5 == 156
assert len(pass2) * lines5 == 13260


# ---------------------------------------------------------------------------
# Perry invariant-dimension threshold
# ---------------------------------------------------------------------------

def lower_e1(h):
    return Fraction(7) + Fraction(400, h)


def lower_e2(h):
    return Fraction(12) + Fraction(1600, h)

assert lower_e2(80) == 32
assert lower_e2(100) == 28


print("q-SNF              =", smith_invariants_by_minors(QPLUS))
print("qprime-SNF         =", smith_invariants_by_minors(QMINUS))
print("2q-SNF             =", smith_invariants_by_minors(mat_scale(2, QPLUS)))
print("2qprime-SNF        =", smith_invariants_by_minors(mat_scale(2, QMINUS)))
print("five Lagrangians   =", len(lag5))
print("five Q-descent     =", len(pass5))
print("witness Q value    =", witness_value)
print("two Lagrangians    =", len(lag2))
print("two Q-descent      =", len(pass2))
print("order-80 candidates=", len(pass2) * lines5)
print("e2^H lower h=80    =", lower_e2(80))
print("e2^H lower h=100   =", lower_e2(100))
print("RESULT: exact theta-symmetry audit PASS")
