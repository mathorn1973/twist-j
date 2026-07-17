#!/usr/bin/env python3
# verify_weil_realization_amend1.py
# Amendment 1 to C-WEIL-REALIZATION-1, per the owner verdict of 2026-07-15.
#
#   AM1  full-plane Gauss bridge: 4 zeta_5^n = 4*[5|n] + sum_r chibar^r(n) g(chi^r)
#        for all n (the multiplicative DFT is blind to the ramified class 0 mod 5;
#        the correction term is mandatory).
#   AM2  negative control: at n = 5 the uncorrected right side is 0 while the
#        left side is 4. The old restricted identity (5 not dividing n) still
#        holds (regression).
#   AM3  Gauss sign identities for the odd quartic character:
#        g(chi) conj(g(chi)) = 5 but g(chi) g(chibar) = chi(-1) * 5 = -5;
#        conj(g(chi)) = chi(-1) g(chibar); the even character: g(chi^2)^2 = +5.
#   AM4  symbolic reduction of the frozen lambda_2 formula:
#        lambda_2 = 2 lambda_1 - sum_rho 1/rho^2
#                 = 1 + gamma - gamma^2 - 2 gamma_1 + pi^2/8 - log(4 pi),
#        exact vector algebra over the symbol basis (1, gamma, gamma^2,
#        gamma_1, pi^2, log 4pi). Convention frozen:
#        zeta(1+t) = 1/t + gamma - gamma_1 t + O(t^2).
#   AM5  gamma_1 is strictly negative, by an elementary two-sided bracket:
#        with f(x) = ln x / x (decreasing for x >= 3) and
#        A_N = sum_{k<=N} f(k) - ln^2(N)/2, one has
#        A_N - f(N) <= gamma_1 <= A_N for N >= 4
#        (t_k = f(k) - int_{k-1}^{k} f in (f(k)-f(k-1), 0), telescoping).
#        Computed in directed integer interval arithmetic, N = 10^5.
#   AM6  lambda_2 > 0 by exact interval assembly (calibration gate; G3/G4
#        bookkeeping, NOT a G5 result; no finite prefix of the Li ladder is
#        progress toward RH).
#
# Discipline: stdlib only, no floats anywhere in this file, directed integer
# intervals at scale S = 10^18, deterministic output. Imported classical
# facts: Machin bracketing; harmonic bracket for gamma; atanh geometric
# tails; sum_rho 1/rho^2 = 1 + gamma^2 + 2 gamma_1 - pi^2/8 (used only in
# AM4 as a labeled import); f = ln x / x decreasing for x > e.
# Environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC

from fractions import Fraction

FAILED = []

def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILED.append(name)

# ---------------------------------------------------------------------------
# Z[i] character and Z[zeta_20] machinery (as in the pinned verifier)
# ---------------------------------------------------------------------------
chi_of = {1: (1, 0), 2: (0, 1), 4: (-1, 0), 3: (0, -1)}
def cxmul(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def chi_pow(n, j):
    if n % 5 == 0:
        return (0, 0)
    v = (1, 0)
    for _ in range(j):
        v = cxmul(v, chi_of[n % 5])
    return v

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
z5 = z20pow(Z20, 4)
i20 = z20pow(Z20, 5)
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
        g = z20add(g, z20add(z20scale(z20pow(z5, a), ch[0]),
                             z20scale(z20mul(i20, z20pow(z5, a)), ch[1])))
    return g
g0 = (0,) * 8
for a in range(1, 5):
    g0 = z20add(g0, z20pow(z5, a))
G = [g0, gauss(1), gauss(2), gauss(3)]
FIVE = (5, 0, 0, 0, 0, 0, 0, 0)
FOUR = (4, 0, 0, 0, 0, 0, 0, 0)

def bridge_rhs(n):
    tot = (0,) * 8
    for j in range(4):
        ch = chi_pow(n, j)                     # chibar^j(n) = conj of chi^j(n)
        tot = z20add(tot, z20add(z20scale(G[j], ch[0]),
                                 z20scale(z20mul(i20, G[j]), -ch[1])))
    return tot

# AM1: full-plane bridge with the ramified correction term.
ok = True
for n in range(1, 16):
    lhs = z20scale(z20pow(z5, n), 4)
    corr = FOUR if n % 5 == 0 else (0,) * 8
    ok = ok and (lhs == z20add(corr, bridge_rhs(n)))
check("AM1 full-plane bridge 4 zeta_5^n = 4*[5|n] + sum_r chibar^r(n) g(chi^r), n = 1..15, exact in Z[zeta_20]", ok)

# AM2: negative control at n = 5 and regression of the restricted identity.
ok = (bridge_rhs(5) == (0,) * 8) and (z20scale(z20pow(z5, 5), 4) == FOUR)
for n in (1, 2, 3, 4, 6, 7, 8, 9):
    ok = ok and (z20scale(z20pow(z5, n), 4) == bridge_rhs(n))
check("AM2 uncorrected right side is 0 at n = 5 (left side 4): the multiplicative DFT is blind to the ramified class; restricted identity regression for 5 not dividing n", ok)

# AM3: Gauss sign identities. chi odd: chi(-1) = chi(4) = -1.
ok = (chi_pow(4, 1) == (-1, 0)) and (chi_pow(4, 2) == (1, 0))
ok = ok and (z20mul(G[1], z20conj(G[1])) == FIVE)
ok = ok and (z20mul(G[3], z20conj(G[3])) == FIVE)
ok = ok and (z20mul(G[1], G[3]) == z20scale(FIVE, -1))          # g(chi) g(chibar) = -5
ok = ok and (z20conj(G[1]) == z20scale(G[3], -1))               # conj g(chi) = chi(-1) g(chibar)
ok = ok and (z20mul(G[2], G[2]) == FIVE)                        # even character: g(chi^2)^2 = +5
check("AM3 g(chi)conj(g(chi)) = 5 but g(chi)g(chibar) = chi(-1)*5 = -5 (odd quartic); conj g(chi) = chi(-1) g(chibar); g(chi^2)^2 = +5", ok)

# AM4: symbolic reduction over the basis (1, gamma, gamma^2, gamma_1, pi^2, log4pi).
lam1 = (Fraction(1), Fraction(1, 2), Fraction(0), Fraction(0), Fraction(0), Fraction(-1, 2))
S2   = (Fraction(1), Fraction(0), Fraction(1), Fraction(2), Fraction(-1, 8), Fraction(0))
boxed = (Fraction(1), Fraction(1), Fraction(-1), Fraction(-2), Fraction(1, 8), Fraction(-1))
red = tuple(2 * a - b for a, b in zip(lam1, S2))
check("AM4 lambda_2 = 2 lambda_1 - sum 1/rho^2 reduces exactly to 1 + gamma - gamma^2 - 2 gamma_1 + pi^2/8 - log(4 pi) (imported: sum 1/rho^2 = 1 + gamma^2 + 2 gamma_1 - pi^2/8; convention zeta(1+t) = 1/t + gamma - gamma_1 t + O(t^2))",
      red == boxed)

# ---------------------------------------------------------------------------
# Directed integer interval arithmetic at scale S = 10^18 (as in the pinned
# verifier, reproduced here so this file is self-contained).
# ---------------------------------------------------------------------------
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
            H_hi - lnN[0] - (S // (2 * (N + 1))))

gam = gamma_iv(10 ** 5)

# AM5: gamma_1 bracket. ln k built cumulatively:
# ln k = ln(k-1) + 2 atanh(1/(2k-1)), directed at every step.
def atanh_inv_odd(m):
    # atanh(1/m) for integer m >= 3, directed interval, geometric tail
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

NG = 10 ** 5
ln_lo, ln_hi = 0, 0
A_lo, A_hi = 0, 0
for k in range(2, NG + 1):
    inc = atanh_inv_odd(2 * k - 1)
    ln_lo += 2 * inc[0]
    ln_hi += 2 * inc[1]
    A_lo += ln_lo // k
    A_hi += -((-ln_hi) // k)
# subtract ln^2(N)/2, directed (ln N interval is positive)
A_lo -= -((-(ln_hi * ln_hi)) // (2 * S))
A_hi -= (ln_lo * ln_lo) // (2 * S)
fN_hi = -((-ln_hi) // NG)
g1_lo = A_lo - fN_hi
g1_hi = A_hi
check("AM5 gamma_1 strictly negative: elementary bracket A_N - f(N) <= gamma_1 <= A_N at N = 10^5, directed integer intervals; the sign that the lambda_2 falsifier watches",
      g1_hi < 0 and (g1_hi - g1_lo) < 2 * 10 ** 14)
print("AM5 witness gamma_1 in [%d, %d] * 10^-18 (reference -0.0728158454836767)" % (g1_lo, g1_hi))

# AM6: lambda_2 = 1 + gamma - gamma^2 - 2 gamma_1 + pi^2/8 - log(4 pi) > 0.
gam2 = ((gam[0] * gam[0]) // S, -((-(gam[1] * gam[1])) // S))   # gamma > 0
m2g1 = (-2 * g1_hi, -2 * g1_lo)                                 # gamma_1 < 0
lam2_lo = S + gam[0] - gam2[1] + m2g1[0] + pi2_8[0] - ln4pi[1]
lam2_hi = S + gam[1] - gam2[0] + m2g1[1] + pi2_8[1] - ln4pi[0]
check("AM6 lambda_2(xi_J) > 0 by exact interval assembly (calibration gate, G3/G4 bookkeeping; NOT a G5 result; no finite Li prefix is progress toward RH)",
      lam2_lo > 0 and lam2_hi < S // 5)
print("AM6 witness lambda_2 in [%d, %d] * 10^-18 (reference 0.09234573522804...)" % (lam2_lo, lam2_hi))

print("FAILED: " + (", ".join(FAILED) if FAILED else "none"))
print("VERDICT: " + ("PASS amendment 1 of C-WEIL-REALIZATION-1" if not FAILED else "FAIL"))
