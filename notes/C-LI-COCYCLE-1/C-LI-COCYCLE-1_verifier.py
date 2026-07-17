#!/usr/bin/env python3
# C-LI-COCYCLE-1_verifier.py
# Candidate C-LI-COCYCLE-1: continuation on the J-native uniform cocycle
# (target row J-LI-COCYCLE-REALIZATION [O]). Frozen by
# PREREG_C-LI-COCYCLE-1.md; single execution after the pin.
#
# Discipline: Python 3 stdlib only, no floats anywhere in this file, exact
# arithmetic and directed integer intervals at scale S = 10^18 in every
# assertion. Environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
# PYTHONHASHSEED=0 TZ=UTC.

from fractions import Fraction

FAILED = []

def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILED.append(name)

# ===========================================================================
# CO1: symbol algebra over (1, gamma, gamma^2, gamma_1, pi^2, log4pi)
# ===========================================================================
s1 = (Fraction(1), Fraction(1, 2), Fraction(0), Fraction(0), Fraction(0), Fraction(-1, 2))
s2 = (Fraction(1), Fraction(0), Fraction(1), Fraction(2), Fraction(-1, 8), Fraction(0))
lam1 = s1
lam2 = tuple(2 * a - b for a, b in zip(s1, s2))
t0 = tuple(2 * a for a in lam1)
t1 = tuple(a - b for a, b in zip(lam2, t0))
M1 = tuple(a - b for a, b in zip(t0, t1))
ok = (t1 == tuple(-x for x in s2))
ok = ok and (tuple(a + b for a, b in zip(t0, t1)) == lam2)
ok = ok and (M1 == tuple(2 * a + b for a, b in zip(s1, s2)))
ok = ok and (M1 == (Fraction(3), Fraction(1), Fraction(1), Fraction(2), Fraction(-1, 8), Fraction(-1)))
check("CO1 dictionary algebra: t0 = 2 lambda_1, t1 = -sigma_2, t0+t1 = lambda_2, M1 = t0-t1 = 2 sigma_1 + sigma_2 = 3 + gamma + gamma^2 + 2 gamma_1 - pi^2/8 - log(4pi), exact", ok)

# ===========================================================================
# Directed integer interval machinery, S = 10^18
# ===========================================================================
S = 10 ** 18

def atanh_iv(t):
    s_lo, s_hi = 0, 0
    acc = (t[0], t[1])
    k = 0
    t2 = ((t[0] * t[0]) // S, -((-(t[1] * t[1])) // S))
    while True:
        s_lo += acc[0] // (2 * k + 1)
        s_hi += -((-acc[1]) // (2 * k + 1))
        acc = ((acc[0] * t2[0]) // S, -((-(acc[1] * t2[1])) // S))
        k += 1
        if acc[1] < (2 * k + 1):
            denom = S - t2[1]
            s_hi += -((-(acc[1] * S)) // (denom * (2 * k + 1))) + 1
            break
    return (s_lo, s_hi)

def ln_of_iv(x):
    t_lo = ((x[0] - S) * S) // (x[0] + S)
    t_hi = -((-((x[1] - S) * S)) // (x[1] + S))
    a = atanh_iv((t_lo, t_hi))
    return (2 * a[0], 2 * a[1])

def arctan_inv_int(q, terms):
    fr = Fraction(0)
    sign = 1
    for k in range(terms):
        fr += Fraction(sign, (2 * k + 1) * q ** (2 * k + 1))
        sign = -sign
    nxt = Fraction(1, (2 * terms + 1) * q ** (2 * terms + 1))
    lo_f, hi_f = (fr - nxt, fr) if sign > 0 else (fr, fr + nxt)
    return ((lo_f.numerator * S) // lo_f.denominator,
            -((-(hi_f.numerator * S)) // hi_f.denominator))

def atanh_inv_odd(m):
    x_lo = S // m
    x_hi = -((-S) // m)
    s_lo, s_hi = 0, 0
    acc_lo, acc_hi = x_lo, x_hi
    k = 0
    m2 = m * m
    while True:
        s_lo += acc_lo // (2 * k + 1)
        s_hi += -((-acc_hi) // (2 * k + 1))
        acc_lo = acc_lo // m2
        acc_hi = -((-acc_hi) // m2)
        k += 1
        if acc_hi < (2 * k + 1):
            s_hi += -((-(acc_hi * m2)) // ((m2 - 1) * (2 * k + 1))) + 1
            break
    return (s_lo, s_hi)

a5 = arctan_inv_int(5, 14)
a239 = arctan_inv_int(239, 6)
pi_iv = (16 * a5[0] - 4 * a239[1], 16 * a5[1] - 4 * a239[0])
ln4pi = ln_of_iv((4 * pi_iv[0], 4 * pi_iv[1]))
pi2_8 = ((pi_iv[0] * pi_iv[0]) // (8 * S), -((-(pi_iv[1] * pi_iv[1])) // (8 * S)))

def gamma_iv(N):
    H_lo = 0
    H_hi = 0
    for k in range(1, N + 1):
        q = S // k
        H_lo += q
        H_hi += q if S % k == 0 else q + 1
    lnN = ln_of_iv((N * S, N * S))
    return (H_lo - lnN[1] - (-((-S) // (2 * N))),
            H_hi - lnN[0] - (S // (2 * (N + 1)))), lnN

gam, _ = gamma_iv(10 ** 5)

# ===========================================================================
# CO2: gamma_1 by second-order Euler-Maclaurin at N = 10^5
#   gamma_1 in [A_N - f(N)/2, A_N - f(N)/2 + 2B],  B = (ln N - 1)/(12 N^2)
# ===========================================================================
NG = 10 ** 5
ln_lo, ln_hi = 0, 0
A_lo, A_hi = 0, 0
for k in range(2, NG + 1):
    inc = atanh_inv_odd(2 * k - 1)
    ln_lo += 2 * inc[0]
    ln_hi += 2 * inc[1]
    A_lo += ln_lo // k
    A_hi += -((-ln_hi) // k)
A_lo -= -((-(ln_hi * ln_hi)) // (2 * S))
A_hi -= (ln_lo * ln_lo) // (2 * S)
fN_lo = ln_lo // NG
fN_hi = -((-ln_hi) // NG)
B_hi = -((-(ln_hi - S)) // (12 * NG * NG)) + 1
g1_lo = A_lo - (-((-fN_hi) // 2))
g1_hi = A_hi - (fN_lo // 2) + 2 * B_hi
check("CO2 gamma_1 by EM-2 bracket at N = 10^5: strictly negative, width < 1e-9, inside the amendment-1 elementary bracket (two independent bracket methods agree)",
      g1_hi < 0 and (g1_hi - g1_lo) < 10 ** 9
      and g1_lo > -72873410205792217 and g1_hi < -72758280940973182)
print("CO2 witness gamma_1 in [%d, %d] * 10^-18 (reference -0.0728158454836767)" % (g1_lo, g1_hi))

# ===========================================================================
# CO3: the T_1 gate. M1 = 3 + gamma + gamma^2 + 2 gamma_1 - pi^2/8 - log4pi
# ===========================================================================
gam2 = ((gam[0] * gam[0]) // S, -((-(gam[1] * gam[1])) // S))
m1_lo = 3 * S + gam[0] + gam2[0] + 2 * g1_lo - pi2_8[1] - ln4pi[1]
m1_hi = 3 * S + gam[1] + gam2[1] + 2 * g1_hi - pi2_8[0] - ln4pi[0]
lam2_lo = S + gam[0] - gam2[1] - 2 * g1_hi + pi2_8[0] - ln4pi[1]
lam2_hi = S + gam[1] - gam2[0] - 2 * g1_lo + pi2_8[1] - ln4pi[0]
det_lo = (m1_lo * lam2_lo) // S
det_hi = -((-(m1_hi * lam2_hi)) // S)
check("CO3 T_1 gate: M1 > 0 (and < 1e-4), lambda_2 > 0 (width < 1e-8), det T_1 = M1 * lambda_2 > 0, all exact intervals",
      m1_lo > 0 and m1_hi < S // 10 ** 4
      and lam2_lo > 0 and (lam2_hi - lam2_lo) < 10 ** 10
      and det_lo > 0)
print("CO3 witness M1       in [%d, %d] * 10^-18 (about 3.7e-5)" % (m1_lo, m1_hi))
print("CO3 witness lambda_2 in [%d, %d] * 10^-18 (reference 0.09234573522804...)" % (lam2_lo, lam2_hi))
print("CO3 witness det T_1  in [%d, %d] * 10^-18" % (det_lo, det_hi))

# ===========================================================================
# CO4: the J-native finite exemplar on the Lambda^2 torsion sector
# ===========================================================================
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
Z20 = (0, 1, 0, 0, 0, 0, 0, 0)
z10 = z20pow(Z20, 2)
z5c = z20pow(Z20, 4)

# tie to the plenum: -zeta_5^k = zeta_10^{(2k+5) mod 10}, exponents {1,3,7,9}
ok = True
expo = []
for k in (1, 2, 3, 4):
    e = (2 * k + 5) % 10
    expo.append(e)
    ok = ok and (tuple(-x for x in z20pow(z5c, k)) == z20pow(z10, e))
ok = ok and sorted(expo) == [1, 3, 7, 9]

# psi(n) = ||(U^n - I)(1,1,1,1)||^2 = sum_k (2 - zeta_10^{kn} - zeta_10^{-kn})
def psi_of(n):
    tot = (0,) * 8
    for e in (1, 3, 7, 9):
        term = z20add(z20add((2, 0, 0, 0, 0, 0, 0, 0),
                             tuple(-x for x in z20pow(z10, (e * n) % 10))),
                      tuple(-x for x in z20pow(z10, (-e * n) % 10)))
        tot = z20add(tot, term)
    return tot
PSI_EXPECT = [0, 6, 10, 6, 10, 16, 10, 6, 10, 6, 0]
psi = []
for n in range(0, 21):
    v = psi_of(n)
    ok = ok and (v[1:] == (0,) * 7)      # rational integer
    psi.append(v[0])
ok = ok and (psi[0:11] == PSI_EXPECT) and all(psi[n] == psi[n + 10] for n in range(11))

# second differences and the normal form K = L T L^T (psi even)
def psiv(n):
    return psi[abs(n)]
t = [psiv(m + 1) + psiv(m - 1) - 2 * psiv(m) for m in range(5)]
ok = ok and (t == [12, -2, -8, 8, 2])
N5 = 5
K = [[psiv(j) + psiv(k) - psiv(j - k) for k in range(1, N5 + 1)] for j in range(1, N5 + 1)]
T = [[t[abs(a - b)] for b in range(N5)] for a in range(N5)]
L = [[1 if b <= a else 0 for b in range(N5)] for a in range(N5)]
def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
LT = matmul(matmul(L, T), [[L[j][i] for j in range(N5)] for i in range(N5)])
ok = ok and (K == LT)

def idet(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    s = 0
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in A[1:]]
        s += (-1) ** j * A[0][j] * idet(minor)
    return s
minorsK = [idet([row[:m] for row in K[:m]]) for m in range(1, 6)]
minorsT = [idet([row[:m] for row in T[:m]]) for m in range(1, 6)]
ok = ok and all(x >= 0 for x in minorsK) and all(x >= 0 for x in minorsT)
ok = ok and minorsK[3] > 0 and minorsT[3] > 0 and minorsK[4] == 0 and minorsT[4] == 0
check("CO4 J-native exemplar: -zeta_5^k are exactly the primitive 10th roots (exponents 1,3,7,9); cocycle ladder psi(n) = 8 - 2 c_10(n) = (0,6,10,6,10,16,...), period 10; t = (12,-2,-8,8,2); K = L T L^T exactly; K and T PSD with rank exactly 4 (dets 5x5 = 0)", ok)
print("CO4 witness minors K: %s ; minors T: %s" % (minorsK, minorsT))

# ===========================================================================
# CO5: erratum pins for the additive branch (owner audit 3)
# ===========================================================================
def bcoef(n):
    return 4 if n % 5 == 1 else 0
def cxmul(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
chi_of = {1: (1, 0), 2: (0, 1), 4: (-1, 0), 3: (0, -1)}
def chi_pow(n, j):
    if n % 5 == 0:
        return (0, 0)
    v = (1, 0)
    for _ in range(j):
        v = cxmul(v, chi_of[n % 5])
    return v
NM = 20
b1 = [(0, 0)] * (NM + 1)
for d in range(1, NM + 1):
    for n in range(d, NM + 1, d):
        s_ = chi_pow(n // d, 1)
        b1[n] = (b1[n][0] + s_[0], b1[n][1] + s_[1])
c2 = [(0, 0)] * (NM + 1)
for d in range(1, NM + 1):
    for n in range(d, NM + 1, d):
        s_ = cxmul(b1[d], chi_pow(n // d, 2))
        c2[n] = (c2[n][0] + s_[0], c2[n][1] + s_[1])
aK = [(0, 0)] * (NM + 1)
for d in range(1, NM + 1):
    for n in range(d, NM + 1, d):
        s_ = cxmul(c2[d], chi_pow(n // d, 3))
        aK[n] = (aK[n][0] + s_[0], aK[n][1] + s_[1])
# also verify bcoef against the character table itself
ok = all(bcoef(n) == sum(chi_pow(n, j)[0] for j in range(4))
         and sum(chi_pow(n, j)[1] for j in range(4)) == 0 for n in range(1, 21))
ok = ok and (bcoef(1), aK[1][0]) == (4, 1)
ok = ok and (bcoef(5), aK[5][0]) == (0, 1)
ok = ok and (bcoef(6), aK[6][0]) == (4, 0)
scan = [q for q in (2, 3, 4, 7, 8, 9, 11, 13, 16) if bcoef(q) != aK[q][0]]
ok = ok and (scan == [16]) and (bcoef(11), aK[11][0]) == (4, 4)
check("CO5 erratum pinned: additive branch b(n) = 4*[n=1 mod 5] diverges from a_K already at n = 1 (4 vs 1), at n = 5 (0 vs 1), at n = 6 (4 vs 0); within the ordered unramified prime-power list the first distinguishing witness is exactly 16, with agreement at 11", ok)

# ===========================================================================
# CO6: chain regression, lambda_1 inside the rev1 pinned interval
# ===========================================================================
lam1_lo = S + gam[0] // 2 - (-((-ln4pi[1]) // 2))
lam1_hi = S + (-((-gam[1]) // 2)) - (ln4pi[0] // 2)
check("CO6 chain regression: lambda_1 recomputed lies inside the rev1 pinned interval [23095708964233559, 23095708972138893] * 10^-18",
      lam1_lo >= 23095708964233559 and lam1_hi <= 23095708972138893)
print("CO6 witness lambda_1 in [%d, %d] * 10^-18" % (lam1_lo, lam1_hi))

print("FAILED: " + (", ".join(FAILED) if FAILED else "none"))
print("VERDICT: " + ("PASS C-LI-COCYCLE-1 frozen gates" if not FAILED else "FAIL"))
