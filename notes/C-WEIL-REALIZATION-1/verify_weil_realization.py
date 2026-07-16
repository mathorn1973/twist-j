#!/usr/bin/env python3
# verify_weil_realization.py
# Candidate C-WEIL-REALIZATION-1: exact anchors for the attack on
# J-WEIL-POSITIVE-REALIZATION [O].
#
# Three pillars:
#   A (dynamical layer, L5): the plenum step operator M_J has an Artin-Mazur
#     zeta that is rational with pure weights {phi^2, 1, phi^-2}; periodic
#     point counts are N_m = N(J^m - 1); the 2-form sector rotates by the
#     primitive 10th roots of unity.
#   B (arithmetic layer, target of the bridge): the plenum ideal zeta is
#     zeta_K of Q(zeta_5) = zeta * L(chi) * L(chi^2) * L(chi^3); the pentagon
#     root filter connects by Gauss sums; degree-1 primes are the step
#     operator's invariant hyperplanes; the full (a_K, Lambda_K) bookkeeping
#     is exact over log-prime symbols.
#   C (the wall's first vector): lambda_1 of xi_J = 1 + gamma/2 - log(4 pi)/2
#     is strictly positive by exact integer interval arithmetic, no zeros
#     imported.
#
# Discipline: Python 3 standard library only. Exact arithmetic (integers,
# Fractions, cyclotomic integer tuples, scaled-integer directed intervals) in
# every assertion. No floats anywhere in this file. Deterministic output.
# Frozen environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
# PYTHONHASHSEED=0 TZ=UTC.

from fractions import Fraction
from itertools import combinations

FAILED = []

def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILED.append(name)

# ===========================================================================
# Cyclotomic arithmetic: Z[zeta_5], basis (1, j, j^2, j^3), j^4 = -(1+j+j^2+j^3)
# ===========================================================================
def zmul(a, b):
    c = [0] * 7
    for i in range(4):
        for k in range(4):
            c[i + k] += a[i] * b[k]
    r = [c[0] + c[5], c[1] + c[6], c[2], c[3]]
    k4 = c[4]
    return (r[0] - k4, r[1] - k4, r[2] - k4, r[3] - k4)

def zpow(a, n):
    r = (1, 0, 0, 0)
    for _ in range(n):
        r = zmul(r, a)
    return r

def zadd(a, b): return tuple(x + y for x, y in zip(a, b))
def zsub(a, b): return tuple(x - y for x, y in zip(a, b))

J = (1, 0, 1, 0)      # J = 1 + zeta^2
Z5 = (0, 1, 0, 0)     # zeta_5
ONE4 = (1, 0, 0, 0)

def sigma(a, k):      # Galois: zeta -> zeta^k
    out = (a[0], 0, 0, 0)
    for i in (1, 2, 3):
        out = zadd(out, tuple(a[i] * x for x in zpow(Z5, (i * k) % 5)))
    return out

def znorm(a):         # product of the four conjugates; rational integer
    p = ONE4
    for k in (1, 2, 3, 4):
        p = zmul(p, sigma(a, k))
    return p

# Z[phi] arithmetic: pairs (a, b) meaning a + b*phi, phi^2 = phi + 1
def pmul(x, y):
    a, b = x; c, d = y
    return (a * c + b * d, a * d + b * c + b * d)

# ===========================================================================
# Integer matrix helpers
# ===========================================================================
def matmul(A, B):
    n, K, m = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(K)) for j in range(m)] for i in range(n)]

def matpow(A, m):
    n = len(A)
    R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for _ in range(m):
        R = matmul(R, A)
    return R

def idet(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    s = 0
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in A[1:]]
        s += (-1) ** j * A[0][j] * idet(minor)
    return s

def charpoly(A):
    # Faddeev-LeVerrier; exact integer divisions asserted
    n = len(A)
    c = [1]
    Mk = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for k in range(1, n + 1):
        Mk = matmul(A, Mk)
        t = sum(Mk[i][i] for i in range(n))
        assert t % k == 0
        ck = -t // k
        c.append(ck)
        for i in range(n):
            Mk[i][i] += ck
    return c  # det(zI - A) = z^n + c[1] z^(n-1) + ... + c[n]; also
              # det(I - zA) = 1 + c[1] z + ... + c[n] z^n (ascending)

def ext2(A):
    idx = list(combinations(range(4), 2))
    return [[A[i][k] * A[j][l] - A[i][l] * A[j][k]
             for (k, l) in idx] for (i, j) in idx]

def ext3(A):
    idx = list(combinations(range(4), 3))
    return [[idet([[A[i][j] for j in cs] for i in rs]) for cs in idx] for rs in idx]

def polymul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return r

# ===========================================================================
# PILLAR A: the plenum's own zeta (dynamical layer)
# ===========================================================================
# A1: the axiom step map equals multiplication by J.
cols = [zmul(J, zpow(Z5, i)) for i in range(4)]
M = [[cols[j][i] for j in range(4)] for i in range(4)]
def stepmap(v):
    a, b, c, d = v
    return (a - c + d, b - c, a, b - c + d)
ok = True
rng = range(-2, 3)
for a in rng:
    for b in rng:
        for c in rng:
            for d in rng:
                mv = tuple(sum(M[i][j] * (a, b, c, d)[j] for j in range(4)) for i in range(4))
                ok = ok and (stepmap((a, b, c, d)) == mv)
check("A1 axiom step (a,b,c,d)->(a-c+d, b-c, a, b-c+d) equals multiplication by J, exhaustive box +-2", ok)

# A2: characteristic polynomial, determinant, trace.
cpM = charpoly(M)
check("A2 charpoly(M_J) = z^4 - 3z^3 + 4z^2 - 2z + 1, det = 1, trace = 3",
      cpM == [1, -3, 4, -2, 1] and idet(M) == 1 and sum(M[i][i] for i in range(4)) == 3)

# A3: periodic point counts two-path: det(M^m - I) = N(J^m - 1), m = 1..30;
#     N_1 = 1 anchors aperiodicity (single fixed point).
ok = True
N_m = []
for m in range(1, 31):
    Mm = matpow(M, m)
    d = idet([[Mm[i][j] - (1 if i == j else 0) for j in range(4)] for i in range(4)])
    nj = znorm(zsub(zpow(J, m), ONE4))
    ok = ok and (nj == (d, 0, 0, 0)) and d > 0
    N_m.append(d)
check("A3 N_m = det(M^m - I) = N(J^m - 1) > 0, two independent code paths, m = 1..30; N_1 = 1",
      ok and N_m[0] == 1)

# A4: exterior powers. Lambda^2 charpoly = (z^2 - 3z + 1) * Phi_10(z);
#     Lambda^3 charpoly = reciprocal of charpoly(M).
L2, L3 = ext2(M), ext3(M)
cp2, cp3 = charpoly(L2), charpoly(L3)
check("A4 charpoly(Lambda^2 M) = z^6-4z^5+5z^4-5z^3+5z^2-4z+1 = (z^2-3z+1)*Phi_10(z), palindromic; charpoly(Lambda^3 M) = reciprocal of charpoly(M)",
      cp2 == [1, -4, 5, -5, 5, -4, 1]
      and cp2 == polymul([1, -3, 1], [1, -1, 1, -1, 1])
      and cp2 == cp2[::-1]
      and cp3 == cpM[::-1])

# A5: the weights, symbolically exact.
#     phi^2 = phi + 1 and phi^-2 = 2 - phi are the roots of z^2 - 3z + 1;
#     Phi_10(-zeta^k) = 0 for k = 1..4 (the 2-form rotation sector);
#     eigenvalue products in Z[zeta_5]:
#     mu_1 mu_4 = 1 + phi, mu_2 mu_3 = 2 - phi (as elements: phi = -z^2 - z^3),
#     mixed products are minus the primitive fifth roots, total product N(J) = 1.
phi2 = (1, 1)          # phi + 1 = phi^2 in Z[phi]
phim2 = (2, -1)        # 2 - phi = phi^-2
def q(x):              # z^2 - 3z + 1 at x in Z[phi]
    xx = pmul(x, x)
    return (xx[0] - 3 * x[0] + 1, xx[1] - 3 * x[1])
ok = (q(phi2) == (0, 0) and q(phim2) == (0, 0)
      and pmul(phi2, phim2) == (1, 0)
      and (phi2[0] + phim2[0], phi2[1] + phim2[1]) == (3, 0))
def phi10(t):          # t^4 - t^3 + t^2 - t + 1 in Z[zeta_5]
    return zadd(zsub(zadd(zsub(zpow(t, 4), zpow(t, 3)), zpow(t, 2)), t), ONE4)
for k in (1, 2, 3, 4):
    mz = tuple(-x for x in zpow(Z5, k))
    ok = ok and (phi10(mz) == (0, 0, 0, 0))
mu = [zadd(ONE4, zpow(Z5, k)) for k in (1, 2, 3, 4)]   # mu_k = 1 + zeta^k
phi_el = (0, 0, -1, -1)                                 # phi = -z^2 - z^3
ok = ok and zmul(mu[0], mu[3]) == zadd(ONE4, phi_el)          # phi^2
ok = ok and zmul(mu[1], mu[2]) == zsub((2, 0, 0, 0), phi_el)  # phi^-2
ok = ok and zmul(mu[0], mu[1]) == tuple(-x for x in zpow(Z5, 4))
ok = ok and zmul(mu[0], mu[2]) == tuple(-x for x in zpow(Z5, 2))
ok = ok and zmul(mu[3], mu[2]) == tuple(-x for x in zpow(Z5, 1))
ok = ok and zmul(mu[3], mu[1]) == tuple(-x for x in zpow(Z5, 3))
ok = ok and zmul(zmul(mu[0], mu[1]), zmul(mu[2], mu[3])) == ONE4
check("A5 weights exact: {phi^2, phi^-2} solve z^2-3z+1, product 1, sum 3; mixed 2-form eigenvalues are -zeta^k (primitive 10th roots); total product N(J) = 1", ok)

# A6: Artin-Mazur rationality, exact series identity to order 16:
#     exp(sum N_m z^m / m) =
#     det(I - z L1) det(I - z L3) / [ (1-z)^2 det(I - z L2) ].
ORDER = 16
lhs = [Fraction(0)] * (ORDER + 1)
lhs[0] = Fraction(1)
for n in range(1, ORDER + 1):
    s = Fraction(0)
    for k in range(1, n + 1):
        Nk = N_m[k - 1] if k <= 30 else None
        s += Fraction(Nk) * lhs[n - k]
    lhs[n] = s / n
num = polymul(cpM, cp3)                     # ascending coefficients
den = polymul(polymul([1, -1], [1, -1]), cp2)
rhs = [Fraction(0)] * (ORDER + 1)
for n in range(ORDER + 1):
    v = Fraction(num[n] if n < len(num) else 0)
    for k in range(1, n + 1):
        dk = den[k] if k < len(den) else 0
        v -= dk * rhs[n - k]
    rhs[n] = v                              # den[0] = 1
check("A6 Artin-Mazur zeta of the plenum step is the rational function (charM * charL3) / ((1-z)^2 * charL2), exact series match to order 16",
      lhs == rhs)

# ===========================================================================
# PILLAR B: the plenum's ideal zeta (arithmetic layer)
# ===========================================================================
# B1: disc(Phi_5) = prod_{i<j} (zeta^i - zeta^j)^2 = 125 = 5^3 = p^d.
p = ONE4
for i in range(1, 5):
    for j in range(i + 1, 5):
        d = zsub(zpow(Z5, i), zpow(Z5, j))
        p = zmul(p, zmul(d, d))
check("B1 disc Q(zeta_5) = prod (zeta^i - zeta^j)^2 = 125 = 5^3 = p^d, exact in Z[zeta_5]", p == (125, 0, 0, 0))

# B2: quartic character mod 5 in Z[i], chi(2) = i. Multiplicativity and
#     orthogonality sum_j chi^j(a) = 4 [a = 1 mod 5].
chi_of = {1: (1, 0), 2: (0, 1), 4: (-1, 0), 3: (0, -1)}
def cxmul(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def chi_pow(n, j):
    if n % 5 == 0:
        return (0, 0)
    v = (1, 0)
    for _ in range(j):
        v = cxmul(v, chi_of[n % 5])
    return v
ok = all(chi_pow(a * b, 1) == cxmul(chi_pow(a, 1), chi_pow(b, 1))
         for a in range(1, 5) for b in range(1, 5))
for a in range(1, 5):
    s = (0, 0)
    for j in range(4):
        t = chi_pow(a, j)
        s = (s[0] + t[0], s[1] + t[1])
    ok = ok and (s == ((4, 0) if a % 5 == 1 else (0, 0)))
check("B2 quartic character mod 5: multiplicative, orthogonality sum_j chi^j(a) = 4[a=1], exact in Z[i]", ok)

# B3: Gauss sums in Z[zeta_20] (basis z^0..z^7, x^8 = x^6 - x^4 + x^2 - 1):
#     g(chi^j) * conj(g(chi^j)) = 5 for j = 1,2,3; g(chi^0) = -1;
#     Fourier bridge 4 zeta_5^n = sum_j chibar^j(n) g(chi^j): the additive
#     pentagon filter and the multiplicative character decomposition are the
#     same data.
def z20mul(a, b):
    c = [0] * 15
    for i in range(8):
        for j in range(8):
            c[i + j] += a[i] * b[j]
    for d in range(14, 7, -1):
        k = c[d]
        if k:
            c[d] = 0
            c[d - 2] += k
            c[d - 4] -= k
            c[d - 6] += k
            c[d - 8] -= k
    return tuple(c[:8])
def z20pow(a, n):
    r = (1, 0, 0, 0, 0, 0, 0, 0)
    for _ in range(n):
        r = z20mul(r, a)
    return r
def z20add(a, b): return tuple(x + y for x, y in zip(a, b))
def z20scale(a, s): return tuple(s * x for x in a)
Z20 = (0, 1, 0, 0, 0, 0, 0, 0)
z5_20 = z20pow(Z20, 4)
i_20 = z20pow(Z20, 5)
def z20conj(a):
    out = (0,) * 8
    for e in range(8):
        if a[e]:
            out = z20add(out, z20scale(z20pow(Z20, (19 * e) % 20), a[e]))
    return out
def gauss(j):
    g = (0,) * 8
    for a in range(1, 5):
        ch = chi_pow(a, j)
        term = z20add(z20scale(z20pow(z5_20, a), ch[0]),
                      z20scale(z20mul(i_20, z20pow(z5_20, a)), ch[1]))
        g = z20add(g, term)
    return g
FIVE20 = (5, 0, 0, 0, 0, 0, 0, 0)
ok = all(z20mul(gauss(j), z20conj(gauss(j))) == FIVE20 for j in (1, 2, 3))
g0 = (0,) * 8
for a in range(1, 5):
    g0 = z20add(g0, z20pow(z5_20, a))
ok = ok and g0 == (-1, 0, 0, 0, 0, 0, 0, 0)
for n in (1, 2, 3, 4):
    tot = (0,) * 8
    for j in range(4):
        g = g0 if j == 0 else gauss(j)
        ch = chi_pow(n, j)
        tot = z20add(tot, z20add(z20scale(g, ch[0]), z20scale(z20mul(i_20, g), -ch[1])))
    ok = ok and (tot == z20scale(z20pow(z5_20, n), 4))
check("B3 Gauss sums: |g(chi^j)|^2 = 5 exactly in Z[zeta_20]; g(chi^0) = -1; bridge 4 zeta_5^n = sum_j chibar^j(n) g(chi^j)", ok)

# B4: a_K = 1 * chi * chi^2 * chi^3 (Dirichlet convolution): real, integral,
#     nonnegative through n = 3000; spot values from the splitting law
#     (Dedekind + cyclotomic reciprocity, imported T; derivations in comments).
NMAX = 3000
b1 = [(0, 0)] * (NMAX + 1)
for d in range(1, NMAX + 1):
    for n in range(d, NMAX + 1, d):
        t = chi_pow(n // d, 1)
        b1[n] = (b1[n][0] + t[0], b1[n][1] + t[1])
b2 = [(0, 0)] * (NMAX + 1)
for d in range(1, NMAX + 1):
    if b1[d] != (0, 0):
        for n in range(d, NMAX + 1, d):
            t = cxmul(b1[d], chi_pow(n // d, 2))
            b2[n] = (b2[n][0] + t[0], b2[n][1] + t[1])
b3 = [(0, 0)] * (NMAX + 1)
for d in range(1, NMAX + 1):
    if b2[d] != (0, 0):
        for n in range(d, NMAX + 1, d):
            t = cxmul(b2[d], chi_pow(n // d, 3))
            b3[n] = (b3[n][0] + t[0], b3[n][1] + t[1])
aK = [0] * (NMAX + 1)
ok = True
for n in range(1, NMAX + 1):
    ok = ok and (b3[n][1] == 0) and (b3[n][0] >= 0)
    aK[n] = b3[n][0]
# spot table:
#   5 = lambda^4 ramified: one ideal of norm 5, 25, 125, ...
#   11, 31, 41, 61 = 1 mod 5: four degree-1 primes each
#   16 = 2^4, 81 = 3^4: 2, 3 inert-type f = 4: one prime ideal of norm p^4
#   121 = 11^2: multisets of size 2 from 4 primes: C(5,2) = 10
#   256 = 2^8: (P_2)^2 only: 1
#   361 = 19^2: 19 = 4 mod 5, f = 2: two primes of norm 361
#   55 = 5*11: lambda * (norm-11 primes): 4;   605 = 5*121: 10
SPOT = {1: 1, 2: 0, 3: 0, 4: 0, 5: 1, 11: 4, 16: 1, 25: 1, 31: 4, 41: 4,
        55: 4, 61: 4, 81: 1, 121: 10, 125: 1, 256: 1, 361: 2, 605: 10}
ok = ok and all(aK[n] == v for n, v in SPOT.items())
check("B4 a_K = 1*chi*chi^2*chi^3 is real, integral, nonnegative through 3000; 18 spot values match the splitting law exactly", ok)

# B5: von Mangoldt bookkeeping of the plenum zeta, exact over log-prime
#     symbols: sum_{d|n} Lambda_K(d) a_K(n/d) = a_K(n) log n for n <= 3000,
#     where log n = sum_p v_p(n) log p and Lambda_K comes from the splitting
#     law: Lambda_K(5^m) = log 5; p = 1 mod 5: Lambda_K(p^m) = 4 log p;
#     p = 4 mod 5: 4 log p for even m, else 0; p = 2,3 mod 5: 4 log p for
#     4 | m, else 0.
spf = list(range(NMAX + 1))
for i in range(2, int(NMAX ** 0.5) + 1):
    if spf[i] == i:
        for k in range(i * i, NMAX + 1, i):
            if spf[k] == k:
                spf[k] = i
def factor(n):
    f = {}
    while n > 1:
        p = spf[n]
        f[p] = f.get(p, 0) + 1
        n //= p
    return f
def lambdaK(n):
    f = factor(n)
    if len(f) != 1:
        return {}
    (p, m), = f.items()
    if p == 5:
        return {5: 1}
    r = p % 5
    if r == 1:
        return {p: 4}
    if r == 4:
        return {p: 4} if m % 2 == 0 else {}
    return {p: 4} if m % 4 == 0 else {}
ok = True
for n in range(1, NMAX + 1):
    lhsv = {}
    for d in range(1, n + 1):
        if n % d == 0:
            lk = lambdaK(d)
            if lk:
                a = aK[n // d]
                if a:
                    for pp, c in lk.items():
                        lhsv[pp] = lhsv.get(pp, 0) + c * a
    rhsv = {}
    if aK[n]:
        for pp, m in factor(n).items():
            rhsv[pp] = aK[n] * m
    lhsv = {k: v for k, v in lhsv.items() if v}
    rhsv = {k: v for k, v in rhsv.items() if v}
    ok = ok and (lhsv == rhsv)
check("B5 Lambda_K * a_K = a_K log identity exact over log-prime symbols for all n <= 3000 (splitting-law path vs character path)", ok)

# B6: degree-1 primes are the step operator's invariant hyperplanes:
#     number of roots of Phi_5 mod p equals a_K(p) for every prime p < 200.
ok = True
for pr in [x for x in range(2, 200) if all(x % q for q in range(2, x))]:
    roots = sum(1 for x in range(pr) if (1 + x + x * x + x ** 3 + x ** 4) % pr == 0)
    ok = ok and (roots == aK[pr])
check("B6 invariant hyperplanes of M_J mod p (roots of Phi_5) = a_K(p) = degree-1 primes, all p < 200 including p = 5", ok)

# B7 witness (printed, not asserted): the periodic points of the plenum meet
#     the split primes: factorizations of N_m with residues mod 5.
line = []
for m in range(1, 13):
    f = {}
    x = N_m[m - 1]
    d = 2
    while d * d <= x:
        while x % d == 0:
            f[d] = f.get(d, 0) + 1
            x //= d
        d += 1
    if x > 1:
        f[x] = f.get(x, 0) + 1
    line.append("N_%d=%d=%s" % (m, N_m[m - 1],
                "*".join("%d^%d(r%d)" % (pp, e, pp % 5) if e > 1 else "%d(r%d)" % (pp, pp % 5)
                         for pp, e in sorted(f.items()))))
print("B7 witness " + "; ".join(line[:6]))
print("B7 witness " + "; ".join(line[6:]))

# ===========================================================================
# PILLAR C: lambda_1 of xi_J is strictly positive, exact integer intervals
# ===========================================================================
# lambda_1 = 1 + gamma/2 - log(4 pi)/2. Scaled-integer directed interval
# arithmetic at scale S = 10^18. Imported classical facts: the Machin formula
# with alternating-tail bracketing; the harmonic bracket
# 1/(2(N+1)) < H_N - ln N - gamma < 1/(2N); atanh series with geometric tail.
S = 10 ** 18

def ivadd(x, y): return (x[0] + y[0], x[1] + y[1])
def ivsub(x, y): return (x[0] - y[1], x[1] - y[0])
def ivscale_div2(x): return (x[0] // 2, -((-x[1]) // 2))
def ivmul_pos(x, y):  # both intervals positive
    return ((x[0] * y[0]) // S, -((-(x[1] * y[1])) // S))

def atanh_iv(t):
    # t = (lo, hi) positive scaled interval, t_hi < S. Sum t^(2k+1)/(2k+1)
    # with directed rounding; geometric tail bound from t_hi.
    s_lo, s_hi = 0, 0
    acc = (t[0], t[1])
    k = 0
    t2 = ((t[0] * t[0]) // S, -((-(t[1] * t[1])) // S))
    while True:
        term_lo = acc[0] // (2 * k + 1)
        term_hi = -((-acc[1]) // (2 * k + 1))
        s_lo += term_lo
        s_hi += term_hi
        # next power
        acc = ((acc[0] * t2[0]) // S, -((-(acc[1] * t2[1])) // S))
        k += 1
        if acc[1] < (2 * k + 1):  # next terms below 1 scaled unit each
            # geometric tail bound using ratio t2_hi:
            # tail <= acc_hi/(2k+1) * 1/(1 - t2_hi/S)
            denom = S - t2[1]
            tail = -((-(acc[1] * S)) // (denom * (2 * k + 1))) + 1
            s_hi += tail
            break
    return (s_lo, s_hi)

def ln_of_iv(x):
    # x = (lo, hi) scaled, x > 1. ln x = 2 atanh((x-1)/(x+1)), monotone.
    t_lo = ((x[0] - S) * S) // (x[0] + S)
    t_hi = -((-((x[1] - S) * S)) // (x[1] + S))
    a = atanh_iv((t_lo, t_hi))
    return (2 * a[0], 2 * a[1])

def arctan_inv_int(q, terms):
    # arctan(1/q), alternating series, exact Fractions -> scaled interval
    fr = Fraction(0)
    sign = 1
    for k in range(terms):
        fr += Fraction(sign, (2 * k + 1) * q ** (2 * k + 1))
        sign = -sign
    nxt = Fraction(1, (2 * terms + 1) * q ** (2 * terms + 1))
    lo_f, hi_f = (fr - nxt, fr) if sign > 0 else (fr, fr + nxt)
    lo = (lo_f.numerator * S) // lo_f.denominator
    hi = -((-(hi_f.numerator * S)) // hi_f.denominator)
    return (lo, hi)

a5 = arctan_inv_int(5, 14)
a239 = arctan_inv_int(239, 6)
pi_iv = ivsub((16 * a5[0], 16 * a5[1]), (4 * a239[0], 4 * a239[1]))
four_pi = (4 * pi_iv[0], 4 * pi_iv[1])
ln4pi = ln_of_iv(four_pi)

# gamma via H_N - ln N with the harmonic bracket, N = 10^5 and 2*10^5
def gamma_iv(N):
    H_lo = 0
    H_hi = 0
    for k in range(1, N + 1):
        q = S // k
        H_lo += q
        H_hi += q if S % k == 0 else q + 1
    # ln N: N = 10^a * r handled generically via ln_of_iv on exact (N*S, N*S)
    lnN = ln_of_iv((N * S, N * S))
    g_lo = H_lo - lnN[1] - (-((-S) // (2 * N)))       # subtract ceil(S/(2N))
    g_hi = H_hi - lnN[0] - (S // (2 * (N + 1)))       # subtract floor(S/(2(N+1)))
    return (g_lo, g_hi)

g1 = gamma_iv(10 ** 5)
g2 = gamma_iv(2 * 10 ** 5)
check("C0 gamma intervals from N = 1e5 and N = 2e5 overlap (bracket consistency)",
      max(g1[0], g2[0]) <= min(g1[1], g2[1]))
gamma = (max(g1[0], g2[0]), min(g1[1], g2[1]))

lam1 = ivadd((S, S), ivsub(ivscale_div2(gamma), ivscale_div2(ln4pi)))
check("C1 lambda_1(xi_J) = 1 + gamma/2 - log(4 pi)/2 > 0, exact integer interval, width < 2e-9, no zeros imported",
      lam1[0] > 0 and (lam1[1] - lam1[0]) < 2 * 10 ** 9)
print("C1 witness lambda_1 in [%d, %d] * 10^-18 (approx 0.0230957089...)" % (lam1[0], lam1[1]))
print("C1 witness gamma    in [%d, %d] * 10^-18" % (gamma[0], gamma[1]))
print("C1 witness log(4pi) in [%d, %d] * 10^-18" % (ln4pi[0], ln4pi[1]))

print("FAILED: " + (", ".join(FAILED) if FAILED else "none"))
print("VERDICT: " + ("PASS all exact anchors of C-WEIL-REALIZATION-1" if not FAILED else "FAIL"))
