#!/usr/bin/env python3
"""P-DIGON-TRIANGLE-J-MODE-1 exact verifier.

Public probe under POLICY.md, preregistered in PREREG.md of this directory.
Python standard library only. Exact arithmetic: Fractions in
Q(zeta_5) = Q[x]/(x^4 + x^3 + x^2 + x + 1). No float anywhere. Deterministic,
sorted output, one RESULT line, exit 0 iff every check passes. Launches no
subprocess, reads and writes no file.

Run from the repository root:
  LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-DIGON-TRIANGLE-J-MODE-1/verify.py

The same checks were run in the author's incubation lane before this public
pin (verifier SHA-256 ebfa5326...1518 there); this file is the public pin and
its first execution in this repository follows the pin, as POLICY.md requires.
"""
from fractions import Fraction as F
import sys

# ----------------------------------------------------------------- Q(zeta_5)
# element = tuple of four Fractions (a0, a1, a2, a3) = a0 + a1 z + a2 z^2 + a3 z^3


def red(c):
    m = [F(0)] * 5
    for i, v in enumerate(c):
        m[i % 5] += F(v)                       # z^5 = 1
    t = m[4]                                   # z^4 = -(1 + z + z^2 + z^3)
    return tuple(m[i] - t for i in range(4))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def mul(a, b):
    r = [F(0)] * 7
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            r[i + j] += x * y
    return red(r)


def gal(a, k):
    """Galois map z -> z^k."""
    o = [F(0)] * 5
    for i, x in enumerate(a):
        o[(k * i) % 5] += x
    return red(o)


def const(q):
    return red([F(q)])


def zpow(k):
    return red([0] * (k % 5) + [1])


def is_rational(a):
    return a[1] == 0 and a[2] == 0 and a[3] == 0


def inv(a):
    n = mul(mul(a, gal(a, 2)), mul(gal(a, 3), gal(a, 4)))   # the norm, rational
    if not is_rational(n) or n[0] == 0:
        raise ZeroDivisionError("not invertible")
    q = mul(gal(a, 2), mul(gal(a, 3), gal(a, 4)))
    return tuple(x / n[0] for x in q)


ZERO = const(0)
ONE = const(1)
Z = zpow(1)
PHI = neg(add(zpow(2), zpow(3)))               # phi = -z^2 - z^3
INV_PHI = sub(PHI, ONE)                        # 1/phi = phi - 1
J = add(ONE, zpow(2))                          # J = 1 + z^2


def sigma(k):
    return gal(J, k)                           # sigma_k(J) = 1 + z^(2k)


# ----------------------------------------------------------------- linear algebra over Q(zeta_5)

def matvec(A, v):
    out = []
    for row in A:
        s = ZERO
        for a, x in zip(row, v):
            s = add(s, mul(a, x))
        out.append(s)
    return out


def imat(A):
    """integer matrix -> Q(zeta_5) matrix"""
    return [[const(a) for a in row] for row in A]


def charpoly_int(A):
    """Faddeev-LeVerrier over Fractions for an integer square matrix.
    Returns [1, c1, ..., cn] for x^n + c1 x^(n-1) + ... + cn."""
    n = len(A)
    A = [[F(a) for a in row] for row in A]
    I = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    M = [[F(0)] * n for _ in range(n)]
    coeffs = [F(1)]
    for k in range(1, n + 1):
        AM = [[sum(A[i][l] * M[l][j] for l in range(n)) for j in range(n)] for i in range(n)]
        M = [[AM[i][j] + coeffs[-1] * I[i][j] for j in range(n)] for i in range(n)]
        AM = [[sum(A[i][l] * M[l][j] for l in range(n)) for j in range(n)] for i in range(n)]
        coeffs.append(-sum(AM[i][i] for i in range(n)) / k)
    return coeffs


def matmul_int(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][l] * B[l][j] for l in range(m)) for j in range(p)] for i in range(n)]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


# ----------------------------------------------------------------- the cell

def cell(k1, k2, shared_sign=-1):
    """Two faces, one shared edge. Face 1 has k1 edges (indices 0..k1-1, all +1).
    Face 2 has k2 edges: the shared edge (index k1-1) with sign shared_sign and
    k2-1 fresh edges (+1). Returns incidence C (ne x 2), Gram G = C^T C, step T."""
    ne = k1 + k2 - 1
    C = [[0, 0] for _ in range(ne)]
    for i in range(k1):
        C[i][0] = 1
    C[k1 - 1][1] = shared_sign
    for i in range(k1, ne):
        C[i][1] = 1
    G = [[sum(C[i][a] * C[i][b] for i in range(ne)) for b in range(2)] for a in range(2)]
    n = ne + 2
    T = [[0] * n for _ in range(n)]
    for i in range(ne):                          # E' = E + C M
        T[i][i] = 1
        for a in range(2):
            T[i][ne + a] = C[i][a]
    for a in range(2):                           # M' = M - C^T E' = M - C^T E - G M
        for i in range(ne):
            T[ne + a][i] = -C[i][a]
        for b in range(2):
            T[ne + a][ne + b] = int(a == b) - G[a][b]
    return C, G, T


# ----------------------------------------------------------------- checks
RESULTS = []


def check(name, cond, note):
    RESULTS.append((name, bool(cond), note))


def modes_of(C, G, T, k1, mus, want_form_1_plus_mu2):
    """For each mode mu: lambda = 2 - mu - mu^-1, r = k1 - lambda (reference face 1),
    verify G-eigenvector, T-eigenvector, and return list of (mu, lambda, r)."""
    ne = len(C)
    out = []
    CC = imat(C)
    GG = imat(G)
    TT = imat(T)
    for mu in mus:
        mu_inv = inv(mu)
        lam = sub(const(2), add(mu, mu_inv))
        assert lam == mul(sub(ONE, mu), sub(ONE, mu_inv))
        r = sub(const(k1), lam)
        M = [ONE, r]
        GM = matvec(GG, M)
        ok_G = GM == [mul(lam, ONE), mul(lam, r)]
        E = [mul(x, inv(sub(mu, ONE))) for x in matvec(CC, M)]
        v = E + M
        Tv = matvec(TT, v)
        ok_T = Tv == [mul(mu, x) for x in v]
        form = mul(r, mu) == add(ONE, mul(mu, mu))
        out.append((mu, lam, r, ok_G, ok_T, form))
    return out


# ---- T1: the digon + triangle cell, order 5
C23, G23, T23 = cell(2, 3)
check("T1a", G23 == [[2, -1], [-1, 3]], "G = C^T C = [[2,-1],[-1,3]] for digon + triangle, shared edge -1")
cp = charpoly_int(T23)
check("T1b", cp == [F(1), F(-1), F(0), F(0), F(0), F(-1), F(1)],
      "charpoly(T) = (x-1)^2 Phi_5(x) = x^6 - x^5 - x + 1")
P = eye(6)
for _ in range(5):
    P = matmul_int(P, T23)
check("T1c", P == eye(6) and T23 != eye(6), "T^5 = I and T != I")

# ---- T2, T3, T4 on the four modes mu = zeta^k
MU = [zpow(k) for k in (1, 2, 3, 4)]
modes = modes_of(C23, G23, T23, 2, MU, True)
check("T2a", all(m[3] for m in modes), "G (1, r_k) = lambda_k (1, r_k) with r_k = 2 - lambda_k = mu + 1/mu, all k")
check("T2b", all(m[4] for m in modes), "T v = mu v for v = (C M/(mu - 1), M), M = (1, r_k), all k")
check("T3a", all(m[5] for m in modes), "r_k mu = 1 + mu^2 for all k")
check("T3b", all(mul(m[2], m[0]) == sigma(k) for m, k in zip(modes, (1, 2, 3, 4))),
      "r_k mu = sigma_k(J) = 1 + zeta^(2k) for all k")
mu1, lam1, r1 = modes[0][0], modes[0][1], modes[0][2]
mu2, lam2, r2 = modes[1][0], modes[1][1], modes[1][2]
check("T3c", r1 == INV_PHI and mul(r1, mu1) == J, "k = 1: r = 1/phi = |J| and r mu = J (polar form of J)")
check("T3d", r2 == neg(PHI) and mul(r2, mu2) == sigma(2), "k = 2: r = -phi and r mu = sigma_2(J)")
check("T3e", mul(J, PHI) == Z, "J phi = zeta (the axiom block): the argument of J is the mode frequency 2 pi/5")
check("T4a", all(add(m[1], mul(inv(m[2]), inv(m[2]))) == const(4) for m in modes),
      "lambda_k + 1/r_k^2 = 4 for all k (hypotenuse 2)")
S2 = sub(const(3), PHI)
check("T4b", lam1 == S2 and S2 == mul(sub(ONE, Z), sub(ONE, zpow(4))) and add(S2, mul(PHI, PHI)) == const(4),
      "k = 1: lambda = 3 - phi = |1 - zeta|^2 = s^2 and s^2 + phi^2 = 4: legs s, phi, hypotenuse 2")
check("T4c", lam2 == add(const(2), PHI) and add(lam2, mul(INV_PHI, INV_PHI)) == const(4),
      "k = 2: lambda = 2 + phi and (2 + phi) + phi^-2 = 4: legs sqrt(2+phi), 1/phi, hypotenuse 2")
check("T4d", mul(lam1, lam2) == const(5), "lambda_1 lambda_2 = 5 = N(1 - zeta_5) = det G")

# ---- T5: the digon is the reason for 1 + mu^2
t5 = []
for k1 in (1, 2, 3):
    k2 = 3 if k1 != 3 else 2
    Ck, Gk, Tk = cell(k1, k2)
    for mu in MU:
        lam = sub(const(2), add(mu, inv(mu)))
        r = sub(const(k1), lam)
        lhs = mul(r, mu)
        rhs = add(mul(const(k1 - 2), mu), add(ONE, mul(mu, mu)))
        t5.append((k1, lhs == rhs, lhs == add(ONE, mul(mu, mu))))
check("T5a", all(t[1] for t in t5), "r mu = (k1 - 2) mu + 1 + mu^2 for reference face of k1 edges, k1 = 1, 2, 3")
check("T5b", all(t[2] == (t[0] == 2) for t in t5), "the form 1 + mu^2 holds iff the reference face is a digon (k1 = 2)")
Ct, Gt, Tt = cell(3, 2)
tri = []
for mu in MU:
    lam = sub(const(2), add(mu, inv(mu)))
    r = sub(const(3), lam)
    tri.append(mul(r, mu) == add(ONE, add(mu, mul(mu, mu))))
check("T5c", all(tri), "triangle as reference face: r mu = 1 + mu + mu^2 (Phi_3 form), never 1 + mu^2")

# ---- T6: complete census of two-face cells inside the window
# minimal polynomials of 2cos(2 pi / N), integer coefficients high -> low
MINPOLY = {1: [1, -2], 2: [1, 2], 3: [1, 1], 4: [1, 0], 5: [1, 1, -1], 6: [1, -1],
           8: [1, 0, -2], 10: [1, -1, -1], 12: [1, 0, -3]}


def polyrem(a, b):
    a = [F(v) for v in a]
    b = [F(v) for v in b]
    while a and a[0] == 0:
        a.pop(0)
    while len(a) >= len(b):
        c = a[0] / b[0]
        for i in range(len(b)):
            a[i] -= c * b[i]
        a.pop(0)
        while a and a[0] == 0:
            a.pop(0)
    return a


census = {}
for k1 in range(1, 5):
    for k2 in range(1, 5):
        lam_poly = [1, -(k1 + k2), k1 * k2 - 1]            # roots lambda
        f = lambda v: lam_poly[0] * v * v + lam_poly[1] * v + lam_poly[2]
        disc = lam_poly[1] ** 2 - 4 * lam_poly[2]
        inside = disc > 0 and f(0) >= 0 and f(4) > 0 and 0 < k1 + k2 < 8
        degenerate = f(0) == 0
        wall = f(4) == 0
        t_poly = [1, -(4 - k1 - k2), 4 - 2 * (k1 + k2) + k1 * k2 - 1]   # roots t = 2 - lambda = 2 cos omega
        orders = sorted(N for N, m in MINPOLY.items() if not polyrem(t_poly, m))
        census[(k1, k2)] = (inside, degenerate, wall, orders)
expected = {
    (1, 1): (True, True, False, [1, 4]),
    (1, 2): (True, False, False, [10]),
    (1, 3): (True, False, False, [8]),
    (2, 2): (True, False, False, [3, 6]),
    (2, 3): (True, False, False, [5]),
    (3, 3): (False, False, True, [2, 4]),
}
ok6 = True
for key, val in census.items():
    k1, k2 = key
    sym = census[(k2, k1)]
    if val != sym:
        ok6 = False
    if key in expected or (k2, k1) in expected:
        exp = expected.get(key, expected.get((k2, k1)))
        if val != exp:
            ok6 = False
    else:
        if val[0]:
            ok6 = False
check("T6a", ok6, "census k1, k2 <= 4: (1,1) degenerate, (1,2) order 10, (1,3) order 8, (2,2) orders 3 and 6, "
                  "(2,3) order 5, (3,3) wall, all others outside")
# the bound: lambda_max >= max(k1, k2) because e_i^T G e_i = k_i (Rayleigh); so k >= 5 is outside.
check("T6b", all(not census[(k1, k2)][0] for k1 in range(1, 5) for k2 in range(1, 5) if max(k1, k2) >= 4 and (k1, k2) != (1, 4) and (k1, k2) != (4, 1)) and not census[(1, 4)][0],
      "every cell with a face of 4 or more edges is outside the window (lambda_max >= max(k1, k2))")
check("T6c", [key for key, val in census.items() if 5 in val[3]] == [(2, 3), (3, 2)],
      "(2,3) is the unique two-face cell with modes of order 5")
# the (2,1) cell with the digon as reference face: modes of order 10 read as the conjugates of J
C21, G21, T21 = cell(2, 1)
check("T6d", G21 == [[2, -1], [-1, 1]], "G of digon + monogon = [[2,-1],[-1,1]]")
MU10 = [neg(zpow(j)) for j in (1, 2, 3, 4)]             # primitive tenth roots: -zeta^j
cp21 = charpoly_int(T21)
# the cell has 2 edges and 2 faces, so T is 4 x 4; G is nonsingular (det 1), there is no static
# mode, and the whole characteristic polynomial is Phi_10(x) = x^4 - x^3 + x^2 - x + 1.
# (The incubation first run expected (x-1)^2 Phi_10(x) by mistake, copied from the 6 x 6 cell; archived there.)
check("T6e", cp21 == [F(1), F(-1), F(1), F(-1), F(1)], "charpoly(T) of digon + monogon = Phi_10(x), 4 x 4, no static mode")
m21 = modes_of(C21, G21, T21, 2, MU10, True)
check("T6f", all(m[3] and m[4] and m[5] for m in m21) and
      sorted(mul(m[2], m[0]) for m in m21) == sorted(sigma(k) for k in (1, 2, 3, 4)),
      "digon + monogon: T v = mu v for mu primitive tenth roots and {r mu} = {sigma_k(J)}, angles 36 and 108 degrees")

# ---- T7: orientation of the shared edge
C23p, G23p, T23p = cell(2, 3, shared_sign=+1)
check("T7a", G23p == [[2, 1], [1, 3]], "shared edge with the same sign in both faces: G = [[2,1],[1,3]]")
m7 = []
for mu in MU:
    lam = sub(const(2), add(mu, inv(mu)))
    r = sub(lam, const(2))                                   # from the first row: (2 - lam) + r = 0
    M = [ONE, r]
    ok_G = matvec(imat(G23p), M) == [mul(lam, ONE), mul(lam, r)]
    E = [mul(x, inv(sub(mu, ONE))) for x in matvec(imat(C23p), M)]
    v = E + M
    ok_T = matvec(imat(T23p), v) == [mul(mu, x) for x in v]
    m7.append((ok_G, ok_T, mul(r, mu)))
check("T7b", all(m[0] and m[1] for m in m7), "flipped orientation: modes mu = zeta^k with M = (1, -r_k)")
check("T7c", [m[2] for m in m7] == [neg(sigma(k)) for k in (1, 2, 3, 4)], "flipped orientation: r mu = -sigma_k(J)")

# ----------------------------------------------------------------- report
fails = 0
for name, ok, note in sorted(RESULTS):
    print(("PASS " if ok else "FAIL ") + name.ljust(4) + " " + note)
    if not ok:
        fails += 1
print("RESULT " + ("PASS" if fails == 0 else "FAIL") + " checks=%d fails=%d" % (len(RESULTS), fails))
sys.exit(0 if fails == 0 else 1)
