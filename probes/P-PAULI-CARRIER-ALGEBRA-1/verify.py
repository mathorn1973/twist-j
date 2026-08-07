#!/usr/bin/env python3
"""P-PAULI-CARRIER-ALGEBRA-1 exact verifier.

Exact arithmetic only. Standard library only. No floats, random choices,
external files, datasets, timestamps, or private infrastructure.

Scope: L4 support algebra only. No CAR, Fock space, energy, locality,
decoder, MatterData, Born measure, or physical Pauli-exclusion claim.
"""
from fractions import Fraction as F
import sys

RESULTS = []


def check(name, condition):
    ok = bool(condition)
    RESULTS.append(ok)
    print(("PASS " if ok else "FAIL ") + name)


# ------------------------------------------------------------------ integers
I2_Z = ((1, 0), (0, 1))
X_Z = ((0, 1), (1, 0))
Z_Z = ((1, 0), (0, -1))
B_Z = ((0, -1), (1, 0))


def imul(A, B):
    return tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(len(B)))
              for j in range(len(B[0])))
        for i in range(len(A))
    )


def itrans(A):
    return tuple(tuple(A[j][i] for j in range(len(A)))
                 for i in range(len(A[0])))


def ineg(A):
    return tuple(tuple(-x for x in row) for row in A)


# ------------------------------------------------------------------ F_5 quotient
F5X = {1, 2, 3, 4}
Q = frozenset({1, 4})
N = frozenset({2, 3})
classes = (Q, N)


def mul_class(k, C):
    return frozenset((k * x) % 5 for x in C)


def chi5(x):
    return 1 if (x % 5) in Q else -1


swap_ok = mul_class(2, Q) == N and mul_class(2, N) == Q
check("P1 quotient has two sign classes and multiplication by 2 swaps them",
      F5X == Q | N and Q.isdisjoint(N) and len(classes) == 2 and swap_ok)
check("P1 quadratic character gives chi_5(2) = -1", chi5(2) == -1)
check("P1 Pauli relations X^2=Z^2=I and ZX=-XZ",
      imul(X_Z, X_Z) == I2_Z
      and imul(Z_Z, Z_Z) == I2_Z
      and imul(Z_Z, X_Z) == ineg(imul(X_Z, Z_Z)))

B_from_quotient = imul(X_Z, Z_Z)
check("P2 B=XZ is the public integer skeleton [[0,-1],[1,0]]",
      B_from_quotient == B_Z)
check("P2 B is alternating and B^2=-I",
      itrans(B_Z) == ineg(B_Z) and imul(B_Z, B_Z) == ineg(I2_Z))


# -------------------------------- generic polynomial identity over Z[a,b,c,d]
# Polynomial representation: dict exponent-4-tuple -> integer coefficient.
def pclean(P):
    return {m: c for m, c in P.items() if c}


def padd(P, Qp):
    out = dict(P)
    for m, c in Qp.items():
        out[m] = out.get(m, 0) + c
    return pclean(out)


def pneg(P):
    return {m: -c for m, c in P.items()}


def psub(P, Qp):
    return padd(P, pneg(Qp))


def pmul(P, Qp):
    out = {}
    for m, c in P.items():
        for n, d in Qp.items():
            e = tuple(m[i] + n[i] for i in range(4))
            out[e] = out.get(e, 0) + c * d
    return pclean(out)


def pconst(n):
    return {} if n == 0 else {(0, 0, 0, 0): n}


def pvar(i):
    e = [0, 0, 0, 0]
    e[i] = 1
    return {tuple(e): 1}


def pmatmul(A, B):
    out = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            s = {}
            for k in range(len(B)):
                s = padd(s, pmul(A[i][k], B[k][j]))
            row.append(s)
        out.append(tuple(row))
    return tuple(out)


def ptrans(A):
    return tuple(tuple(A[j][i] for j in range(len(A)))
                 for i in range(len(A[0])))


a, b, c, d = (pvar(i) for i in range(4))
Apoly = ((a, b), (c, d))
Bpoly = ((pconst(0), pconst(-1)), (pconst(1), pconst(0)))
detA = psub(pmul(a, d), pmul(b, c))
lhs = pmatmul(pmatmul(ptrans(Apoly), Bpoly), Apoly)
rhs = tuple(tuple(pmul(detA, Bpoly[i][j]) for j in range(2))
            for i in range(2))
check("P3 polynomial identity A^T B A = det(A) B over every commutative ring",
      lhs == rhs)


# ---------------- K=Q(zeta_5), basis 1,zeta,zeta^2,zeta^3, Phi_5(zeta)=0
def red(v):
    top = v[4]
    return (v[0] - top, v[1] - top, v[2] - top, v[3] - top)


def zadd(x, y):
    return tuple(a0 + b0 for a0, b0 in zip(x, y))


def zsub(x, y):
    return tuple(a0 - b0 for a0, b0 in zip(x, y))


def zneg(x):
    return tuple(-a0 for a0 in x)


def zint(n):
    return (F(n), F(0), F(0), F(0))


def zmul(x, y):
    coeff = [F(0)] * 5
    for i in range(4):
        if x[i] == 0:
            continue
        for j in range(4):
            if y[j] != 0:
                coeff[(i + j) % 5] += x[i] * y[j]
    return red(tuple(coeff))


def zinv(x):
    columns = []
    for j in range(4):
        e = [F(0)] * 4
        e[j] = F(1)
        columns.append(zmul(x, tuple(e)))
    aug = [[columns[col][row] for col in range(4)] for row in range(4)]
    rhs0 = [F(1), F(0), F(0), F(0)]
    for col in range(4):
        pivot = next((r for r in range(col, 4) if aug[r][col] != 0), None)
        if pivot is None:
            return None
        aug[col], aug[pivot] = aug[pivot], aug[col]
        rhs0[col], rhs0[pivot] = rhs0[pivot], rhs0[col]
        scale = 1 / aug[col][col]
        aug[col] = [v * scale for v in aug[col]]
        rhs0[col] *= scale
        for r in range(4):
            if r == col or aug[r][col] == 0:
                continue
            factor = aug[r][col]
            aug[r] = [u - factor * v for u, v in zip(aug[r], aug[col])]
            rhs0[r] -= factor * rhs0[col]
    return tuple(rhs0)


def gal(x, exponent):
    coeff = [F(0)] * 5
    for i in range(4):
        coeff[(i * exponent) % 5] += x[i]
    return red(tuple(coeff))


Z0 = zint(0)
Z1 = zint(1)
ZETA = (F(0), F(1), F(0), F(0))


def matmul(A, B):
    out = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            s = Z0
            for k in range(len(B)):
                s = zadd(s, zmul(A[i][k], B[k][j]))
            row.append(s)
        out.append(tuple(row))
    return tuple(out)


def trans(A):
    return tuple(tuple(A[j][i] for j in range(len(A)))
                 for i in range(len(A[0])))


def det2(A):
    return zsub(zmul(A[0][0], A[1][1]), zmul(A[0][1], A[1][0]))


def matsub(A, B):
    return tuple(tuple(zsub(A[i][j], B[i][j]) for j in range(len(A[0])))
                 for i in range(len(A)))


def rref_K(matrix):
    data = [list(row) for row in matrix]
    if not data:
        return data, []
    pivots = []
    row = 0
    for col in range(len(data[0])):
        pivot = next((r for r in range(row, len(data))
                      if data[r][col] != Z0), None)
        if pivot is None:
            continue
        data[row], data[pivot] = data[pivot], data[row]
        inv = zinv(data[row][col])
        data[row] = [zmul(inv, v) for v in data[row]]
        for r in range(len(data)):
            if r == row or data[r][col] == Z0:
                continue
            factor = data[r][col]
            data[r] = [zsub(u, zmul(factor, v))
                       for u, v in zip(data[r], data[row])]
        pivots.append(col)
        row += 1
        if row == len(data):
            break
    return data, pivots


def rank_K(matrix):
    return len(rref_K(matrix)[1])


# Frozen public marked integral 2I representative.
S = ((Z0, zneg(Z1)), (Z1, Z0))
T = ((ZETA, Z1), (Z0, gal(ZETA, 4)))
B_K = S
I2_K = ((Z1, Z0), (Z0, Z1))

check("P2 frozen integral 2I generator S is the same integer matrix B",
      S == ((Z0, zneg(Z1)), (Z1, Z0)))
check("P4 frozen generators have determinant one",
      det2(S) == Z1 and det2(T) == Z1)
check("P4 B is invariant under both frozen integral 2I generators",
      matmul(matmul(trans(S), B_K), S) == B_K
      and matmul(matmul(trans(T), B_K), T) == B_K)


# Linear system for M=(m00,m01,m10,m11): A^T M A=M for A=S,T.
def bilinear_constraints(A):
    positions = ((0, 0), (0, 1), (1, 0), (1, 1))
    columns = []
    for ri, ci in positions:
        M = [[Z0, Z0], [Z0, Z0]]
        M[ri][ci] = Z1
        M = tuple(tuple(row) for row in M)
        defect = matsub(matmul(matmul(trans(A), M), A), M)
        columns.append([defect[i][j] for i in range(2) for j in range(2)])
    return [[columns[col][row] for col in range(4)] for row in range(4)]


bilinear_system = bilinear_constraints(S) + bilinear_constraints(T)
_, piv = rref_K(bilinear_system)
B_flat = (Z0, zneg(Z1), Z1, Z0)


def kernel_contains(system, vector):
    for row in system:
        total = Z0
        for coeff, value in zip(row, vector):
            total = zadd(total, zmul(coeff, value))
        if total != Z0:
            return False
    return True


check("P4 invariant bilinear-form space has K-dimension one and contains B",
      4 - len(piv) == 1 and kernel_contains(bilinear_system, B_flat))

# Add symmetry constraint m01-m10=0; nullity must become zero.
symmetry_row = [Z0, Z1, zneg(Z1), Z0]
check("P4 invariant symmetric bilinear-form subspace is zero",
      rank_K(bilinear_system + [symmetry_row]) == 4)


# Tensor action g tensor g on row-major basis e11,e12,e21,e22.
def kron2(A, B):
    out = []
    for i in range(2):
        for k in range(2):
            row = []
            for j in range(2):
                for l in range(2):
                    row.append(zmul(A[i][j], B[k][l]))
            out.append(tuple(row))
    return tuple(out)


def vector_constraints(A):
    KAA = kron2(A, A)
    rows = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(zsub(KAA[i][j], Z1 if i == j else Z0))
        rows.append(row)
    return rows


tensor_system = vector_constraints(S) + vector_constraints(T)
Omega = (Z0, Z1, zneg(Z1), Z0)
check("P5 invariant tensor subspace has K-dimension one and contains Omega",
      4 - rank_K(tensor_system) == 1 and kernel_contains(tensor_system, Omega))

# Swap e_ij -> e_ji.
SWAP = (
    (Z1, Z0, Z0, Z0),
    (Z0, Z0, Z1, Z0),
    (Z0, Z1, Z0, Z0),
    (Z0, Z0, Z0, Z1),
)

def matvec(A, v):
    out = []
    for i in range(len(A)):
        s = Z0
        for j in range(len(v)):
            s = zadd(s, zmul(A[i][j], v[j]))
        out.append(s)
    return tuple(out)

check("P5 tensor swap sends Omega to -Omega",
      matvec(SWAP, Omega) == tuple(zneg(x) for x in Omega))

# Direct alternating-pairing checks on a symbolic integer test basis are
# consequences of B^T=-B; audit on arbitrary rational samples too.
def eps(v, w):
    return v[0] * (-w[1]) + v[1] * w[0]

samples = [
    (F(1), F(0)), (F(0), F(1)), (F(2), F(3)), (F(-5), F(7)),
]
alt_ok = all(eps(v, v) == 0 for v in samples)
alt_ok = alt_ok and all(eps(w, v) == -eps(v, w)
                        for v in samples for w in samples)
check("P5 alternating pairing is swap-odd and self-pairing vanishes", alt_ok)


print()
print("P-PAULI-CARRIER-ALGEBRA-1 exact verifier")
print(f"RESULT {sum(RESULTS)}/{len(RESULTS)} PASS")
print("SCOPE L4 support only; no CAR, energy, locality, decoder, or physics lift")

sys.exit(0 if all(RESULTS) else 1)
