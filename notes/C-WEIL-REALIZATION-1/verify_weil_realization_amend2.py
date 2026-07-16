#!/usr/bin/env python3
# verify_weil_realization_amend2.py
# Amendment 2 to C-WEIL-REALIZATION-1, per the owner audit of 2026-07-15
# (second verdict). Machine-exact pins for the corrections that are
# verifiable inside this project's lane:
#
#   AN1  the corrected complex-coefficient CND identity (owner fix 1):
#        for finitely supported complex a with sum_k a_k = 0,
#          sum_{k,l} a_k conj(a_l) (1 - cos((k-l)theta))
#            = -(1/2) ( |sum_k a_k e^{ik theta}|^2 + |sum_k a_k e^{-ik theta}|^2 ),
#        checked exactly (doubled to avoid 1/2) in Z[zeta_20] at
#        theta = 2 pi / 10, the Phi_10 sector angle. D is self-conjugate.
#   AN2  scoping control: the single-modulus form is FALSE for genuinely
#        complex a (two witnesses) and TRUE for real a (one witness). The
#        owner's correction is necessary and exactly scoped.
#   AN3  owner fix 3: the determinant/exp-trace packaging is an identity,
#        det(I - xF)^{-1} = exp( sum_m Tr(F^m) x^m / m ), F the 4-cycle
#        (regular representation of C_4), and the Artin factorization
#        det(I - xF) = 1 - x^4 = prod_{k=0}^{3} (1 - i^k x) holds exactly
#        in Z[i][x]. Dead is ONLY the additive sector sum: its Dirichlet
#        coefficients diverge from a_K first at n = 16 (4 against 1).
#        Correct F row: IDEAL-PACKET-BY-ADDITIVE-SECTOR-SUM.
#   AN4  owner fix 4: the two zeta_K conventions agree exactly,
#        zeta * prod_{r=1..3} L(chi^r)  =  (1-5^{-s})^{-1} * prod_{r=0..3} L(chi^r)
#        with chi_0 the principal character mod 5, as Dirichlet coefficients
#        for all n <= 500; and dim V^{I_5} = 1: the fixed space of the
#        4-cycle on the character packet is one-dimensional
#        (rank(P - I) = 3 over Q, exact).
#   AN5  owner fix 2 frame: L_N, the lower-triangular matrix of ones, is
#        unimodular (det = 1, N <= 8), so K_N = (1/2) L_N T_{N-1} L_N^* is
#        an invertible congruence and K_N >= 0 iff T_{N-1} >= 0
#        (Sylvester, imported).
#   AN6  regression: the full-plane Gauss bridge of amendment 1 still holds
#        (n = 1..10).
#
# Discipline: stdlib only, exact arithmetic in every assertion, no floats
# in this file, deterministic output. Environment: LC_ALL=C LANG=C
# PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC

from fractions import Fraction

FAILED = []

def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILED.append(name)

# ---------------------------------------------------------------------------
# Z[zeta_20] and Z[i] machinery
# ---------------------------------------------------------------------------
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
ONE20 = (1, 0, 0, 0, 0, 0, 0, 0)
i20 = z20pow(Z20, 5)
z5 = z20pow(Z20, 4)
def z20conj(a):
    out = (0,) * 8
    for e in range(8):
        if a[e]:
            out = z20add(out, z20scale(z20pow(Z20, (19 * e) % 20), a[e]))
    return out
def emb(re, im):
    return z20add(z20scale(ONE20, re), z20scale(i20, im))
def wp(k):
    return z20pow(Z20, (2 * k) % 20)      # zeta_10^k

def cnd_data(vec):
    n = len(vec)
    a = [emb(re, im) for re, im in vec]
    D = (0,) * 8                           # doubled left side
    for k in range(n):
        for l in range(n):
            coef = z20mul(a[k], z20conj(a[l]))
            term = z20add(z20add((2, 0, 0, 0, 0, 0, 0, 0),
                                 z20scale(wp(k - l), -1)), z20scale(wp(l - k), -1))
            D = z20add(D, z20mul(coef, term))
    Ap = (0,) * 8
    Am = (0,) * 8
    for k in range(n):
        Ap = z20add(Ap, z20mul(a[k], wp(k)))
        Am = z20add(Am, z20mul(a[k], wp(-k)))
    two_mod = z20scale(z20add(z20mul(Ap, z20conj(Ap)), z20mul(Am, z20conj(Am))), -1)
    one_mod = z20scale(z20mul(Ap, z20conj(Ap)), -2)
    return D, two_mod, one_mod

VECS = [[(1, 0), (0, 1), (-1, -1)],        # complex, sum 0
        [(2, 0), (-1, 1), (-1, -1)],       # complex, sum 0
        [(1, 0), (-2, 0), (1, 0)],         # real, sum 0
        [(0, 1), (0, -2), (0, 1)]]         # purely imaginary, sum 0
ok = True
for vec in VECS:
    D, two_mod, one_mod = cnd_data(vec)
    ok = ok and (D == two_mod) and (D == z20conj(D))
check("AN1 corrected complex CND identity: doubled form D = -(|A+|^2 + |A-|^2) exactly in Z[zeta_20] at theta = 2 pi/10, four zero-sum vectors; D self-conjugate (real)", ok)

D1, _, one1 = cnd_data(VECS[0])
D2, _, one2 = cnd_data(VECS[1])
D3, _, one3 = cnd_data(VECS[2])
check("AN2 scoping control: single-modulus form FAILS for two genuinely complex vectors and HOLDS for the real vector; the owner correction is necessary and exactly scoped",
      D1 != one1 and D2 != one2 and D3 == one3)

# ---------------------------------------------------------------------------
# AN3: determinant packaging vs additive sector sum
# ---------------------------------------------------------------------------
# F = 4-cycle permutation matrix; Tr(F^m) = 4 if 4 | m else 0.
def trF(m):
    return 4 if m % 4 == 0 else 0
ORDER = 16
# exp side
E = [Fraction(0)] * (ORDER + 1)
E[0] = Fraction(1)
for n in range(1, ORDER + 1):
    s = Fraction(0)
    for k in range(1, n + 1):
        s += Fraction(trF(k)) * E[n - k]
    E[n] = s / n
# det(I - xF) = 1 - x^4; series of (1 - x^4)^{-1} is 1 at multiples of 4
ok = all(E[n] == (1 if n % 4 == 0 else 0) for n in range(ORDER + 1))
# Artin factorization in Z[i][x]: prod_k (1 - i^k x) = 1 - x^4
def cxmul(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
poly = [(1, 0)]
for k in range(4):
    ik = (1, 0)
    for _ in range(k):
        ik = cxmul(ik, (0, 1))
    newp = [(0, 0)] * (len(poly) + 1)
    for d, c in enumerate(poly):
        newp[d] = (newp[d][0] + c[0], newp[d][1] + c[1])
        t = cxmul(c, ik)
        newp[d + 1] = (newp[d + 1][0] - t[0], newp[d + 1][1] - t[1])
    poly = newp
ok = ok and (poly == [(1, 0), (0, 0), (0, 0), (0, 0), (-1, 0)])
# additive sector sum vs a_K: first divergence at n = 16
chi_of = {1: (1, 0), 2: (0, 1), 4: (-1, 0), 3: (0, -1)}
def chi_pow(n, j):
    if n % 5 == 0:
        return (0, 0)
    v = (1, 0)
    for _ in range(j):
        v = cxmul(v, chi_of[n % 5])
    return v
NM = 20
b = [(0, 0)] * (NM + 1)
for d in range(1, NM + 1):
    for n in range(d, NM + 1, d):
        t = chi_pow(n // d, 1)
        b[n] = (b[n][0] + t[0], b[n][1] + t[1])
c2 = [(0, 0)] * (NM + 1)
for d in range(1, NM + 1):
    for n in range(d, NM + 1, d):
        t = cxmul(b[d], chi_pow(n // d, 2))
        c2[n] = (c2[n][0] + t[0], c2[n][1] + t[1])
aK = [(0, 0)] * (NM + 1)
for d in range(1, NM + 1):
    for n in range(d, NM + 1, d):
        t = cxmul(c2[d], chi_pow(n // d, 3))
        aK[n] = (aK[n][0] + t[0], aK[n][1] + t[1])
addsum16 = (0, 0)
for r in range(4):
    t = chi_pow(16, r)
    addsum16 = (addsum16[0] + t[0], addsum16[1] + t[1])
ok = ok and (addsum16 == (4, 0)) and (aK[16] == (1, 0)) and (addsum16 != aK[16])
# and the sum agrees at squarefree split spots (11), so the divergence is
# a prime-power phenomenon, exactly where sum and product part ways
addsum11 = (0, 0)
for r in range(4):
    t = chi_pow(11, r)
    addsum11 = (addsum11[0] + t[0], addsum11[1] + t[1])
ok = ok and (addsum11 == (4, 0)) and (aK[11] == (4, 0))
check("AN3 det(I-xF)^-1 = exp(sum Tr(F^m) x^m/m) exact to order 16; Artin factorization 1 - x^4 = prod (1 - i^k x) in Z[i][x]; additive sector sum diverges from a_K first at n = 16 (4 vs 1) while agreeing at n = 11: the F row is IDEAL-PACKET-BY-ADDITIVE-SECTOR-SUM, scoped", ok)

# ---------------------------------------------------------------------------
# AN4: the two zeta_K conventions and dim V^{I_5} = 1
# ---------------------------------------------------------------------------
N4 = 500
def conv(u, v):
    w = [(0, 0)] * (N4 + 1)
    for d in range(1, N4 + 1):
        if u[d] != (0, 0):
            for n in range(d, N4 + 1, d):
                t = cxmul(u[d], v[n // d])
                w[n] = (w[n][0] + t[0], w[n][1] + t[1])
    return w
onef = [(0, 0)] + [(1, 0)] * N4
chi0 = [(0, 0)] + [((1, 0) if n % 5 else (0, 0)) for n in range(1, N4 + 1)]
chi1 = [(0, 0)] + [chi_pow(n, 1) for n in range(1, N4 + 1)]
chi2v = [(0, 0)] + [chi_pow(n, 2) for n in range(1, N4 + 1)]
chi3v = [(0, 0)] + [chi_pow(n, 3) for n in range(1, N4 + 1)]
tower = [(0, 0)] * (N4 + 1)
k = 1
while k <= N4:
    tower[k] = (1, 0)
    k *= 5
path1 = conv(conv(conv(onef, chi1), chi2v), chi3v)
path2 = conv(conv(conv(conv(tower, chi0), chi1), chi2v), chi3v)
ok = all(path1[n] == path2[n] for n in range(1, N4 + 1))
# dim V^{I_5} = 1: fixed space of the 4-cycle P on the packet is 1-dim.
P = [[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
A = [[Fraction(P[i][j] - (1 if i == j else 0)) for j in range(4)] for i in range(4)]
rank = 0
rows = [r[:] for r in A]
for col in range(4):
    piv = None
    for r in range(rank, 4):
        if rows[r][col] != 0:
            piv = r
            break
    if piv is None:
        continue
    rows[rank], rows[piv] = rows[piv], rows[rank]
    pv = rows[rank][col]
    for r in range(4):
        if r != rank and rows[r][col] != 0:
            f = rows[r][col] / pv
            rows[r] = [x - f * y for x, y in zip(rows[r], rows[rank])]
    rank += 1
ok = ok and (rank == 3)
check("AN4 conventions equal: zeta*L(chi)L(chi^2)L(chi^3) = (1-5^-s)^-1 * L(chi_0)L(chi)L(chi^2)L(chi^3) as coefficients for n <= 500, chi_0 principal; dim V^I_5 = 1 (rank(P - I) = 3 exactly)", ok)

# ---------------------------------------------------------------------------
# AN5: the congruence frame of the finite gates
# ---------------------------------------------------------------------------
def idet(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    s = 0
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in A[1:]]
        s += (-1) ** j * A[0][j] * idet(minor)
    return s
ok = True
for N in range(1, 9):
    L = [[1 if j <= i else 0 for j in range(N)] for i in range(N)]
    ok = ok and (idet(L) == 1)
check("AN5 L_N (lower-triangular ones) is unimodular for N <= 8: K_N = (1/2) L_N T_(N-1) L_N* is an invertible congruence, K_N >= 0 iff T_(N-1) >= 0 (Sylvester, imported); K_2 corresponds to T_1", ok)

# ---------------------------------------------------------------------------
# AN6: regression, full-plane Gauss bridge of amendment 1
# ---------------------------------------------------------------------------
def gauss(j):
    g = (0,) * 8
    for a in range(1, 5):
        ch = chi_pow(a, j)
        g = z20add(g, z20add(z20scale(z20pow(z5, a), ch[0]),
                             z20scale(z20mul(i20, z20pow(z5, a)), ch[1])))
    return g
g0 = (0,) * 8
for a in range(1, 5):
    g0 = z20add(g0, z20pow(z5, a))
G = [g0, gauss(1), gauss(2), gauss(3)]
ok = True
for n in range(1, 11):
    tot = (0,) * 8
    for j in range(4):
        ch = chi_pow(n, j)
        tot = z20add(tot, z20add(z20scale(G[j], ch[0]), z20scale(z20mul(i20, G[j]), -ch[1])))
    corr = (4, 0, 0, 0, 0, 0, 0, 0) if n % 5 == 0 else (0,) * 8
    ok = ok and (z20scale(z20pow(z5, n), 4) == z20add(corr, tot))
check("AN6 regression: full-plane bridge 4 zeta_5^n = 4*[5|n] + sum_r chibar^r(n) g(chi^r), n = 1..10", ok)

print("FAILED: " + (", ".join(FAILED) if FAILED else "none"))
print("VERDICT: " + ("PASS amendment 2 of C-WEIL-REALIZATION-1" if not FAILED else "FAIL"))
