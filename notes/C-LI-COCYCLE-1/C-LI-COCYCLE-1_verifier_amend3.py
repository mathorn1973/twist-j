#!/usr/bin/env python3
# C-LI-COCYCLE-1_verifier_amend3.py
# Amendment 3: independent derivation of sigma_3, the measure normalization
# fix (owner verdict 5), and witnesses for the lambda_3 / T_2 gate.
#
# Statements frozen before the single run:
#   S1  Independent derivation of sigma_3 by the xi(1+t) expansion.
#       With xi(s) = (s-1) pi^(-s/2) Gamma(s/2+1) zeta(s), s = 1+t:
#       log xi(1+t) = log(t zeta(1+t)) - ((1+t)/2) log pi
#                     + log Gamma(3/2 + t/2),
#       and log xi(1+t) = log xi(0) + sigma_1 t - (sigma_2/2) t^2
#                         + (sigma_3/3) t^3 - ...
#       Imported component series (classical):
#       t zeta(1+t) = 1 + gamma t - gamma_1 t^2 + (gamma_2/2) t^3 + O(t^4)
#       (Stieltjes convention zeta(1+t) = 1/t + gamma - gamma_1 t + ...);
#       log Gamma(3/2 + x) about x = 0 with psi(3/2) = 2 - gamma - 2 log 2,
#       psi'(3/2) = pi^2/2 - 4, psi''(3/2) = 16 - 14 zeta(3).
#       Exact vector algebra must reproduce:
#       t^1:  sigma_1 = 1 + gamma/2 - log 2 - (1/2) log pi
#       t^2:  sigma_2 = 1 + gamma^2 + 2 gamma_1 - pi^2/8
#       t^3:  sigma_3 = 1 + gamma^3 + 3 gamma gamma_1 + (3/2) gamma_2
#                       - (7/8) zeta(3)
#       The t^1 and t^2 rows reproduce the previously imported identities,
#       validating the route; the t^3 row derives the owner's frozen
#       formula rather than importing it.
#   S2  lambda_3 = 3 sigma_1 - 3 sigma_2 + sigma_3 (binomial), exact.
#   S3  Measure normalization fix on both finite instances: the cocycle
#       spectral measure obeys mu_v(T) = ladder(1), while the
#       second-difference sequence satisfies t_m = 2 * (cosine moments of
#       mu_v); hence sigma = 2 mu_v and sigma(T) = t_0 = 2 * ladder(1).
#       Exemplar: t_m(f) = 2 c_10(m) for m = 0..10, mu_v(T) = f(1) = 4,
#       t_0 = 8. C_4 instance: t_m(g) = 2 * (4 if 4|m else 0),
#       mu_v(T) = g(1) = 4, t_0 = 8.
#   S4  Witnesses (floats, printed, never asserted): sigma_3 = -1.112e-4;
#       lambda_3 against the owner's pinned interval
#       [0.207638918333718933341285, 0.207638922051014328719963];
#       t_2 = lambda_3 + lambda_1 - 2 lambda_2; det T_2 against the
#       owner's [6.9813247888e-14, 7.3758515923e-14]. Certification at
#       that scale requires gamma_2 brackets of width about 1e-12
#       (EM-4 remainder at N = 1e5, or EM-2 at N = 1e7); recorded as the
#       spec for the two-architecture re-run, not performed here.
#
# Discipline: stdlib only; exact arithmetic in every assertion; floats
# appear only in printed witnesses. Environment: LC_ALL=C LANG=C
# PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.

from fractions import Fraction
import math

FAILED = []

def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILED.append(name)

F = Fraction

# ===========================================================================
# S1: the xi(1+t) expansion, exact vector algebra.
# Symbol basis for t^1: (1, gamma, log2, logpi)
# ===========================================================================
# A(t) = log(1 + u), u = gamma t - gamma_1 t^2 + (gamma_2/2) t^3:
#   A1 = gamma
#   A2 = -gamma_1 - gamma^2/2
#   A3 = gamma_2/2 + gamma*gamma_1 + gamma^3/3
# B(t) = log Gamma(3/2 + t/2):
#   B1 = psi(3/2)/2          = 1 - gamma/2 - log2
#   B2 = psi'(3/2)/8         = pi^2/16 - 1/2
#   B3 = psi''(3/2)/48       = 1/3 - (7/24) zeta(3)
# C(t) = -((1+t)/2) log pi:  C1 = -(1/2) log pi
# t^1 over (1, gamma, log2, logpi):
A1 = (F(0), F(1), F(0), F(0))
B1 = (F(1), F(-1, 2), F(-1), F(0))
C1 = (F(0), F(0), F(0), F(-1, 2))
s1_derived = tuple(a + b + c for a, b, c in zip(A1, B1, C1))
s1_target = (F(1), F(1, 2), F(-1), F(-1, 2))     # 1 + gamma/2 - log2 - logpi/2
check("S1a t^1 row: sigma_1 = 1 + gamma/2 - log2 - (1/2) log pi (equals 1 + gamma/2 - (1/2) log 4pi), derived exactly from the expansion", s1_derived == s1_target)

# t^2 over (1, gamma_1, gamma^2, pi^2): coefficient of t^2 equals -sigma_2/2
A2 = (F(0), F(-1), F(-1, 2), F(0))
B2 = (F(-1, 2), F(0), F(0), F(1, 16))
sum2 = tuple(a + b for a, b in zip(A2, B2))
sigma2 = tuple(-2 * x for x in sum2)
check("S1b t^2 row: sigma_2 = 1 + 2 gamma_1 + gamma^2 - pi^2/8, derived exactly (reproduces the previously imported identity)",
      sigma2 == (F(1), F(2), F(1), F(-1, 8)))

# t^3 over (1, gamma^3, gamma*gamma_1, gamma_2, zeta3): coefficient equals sigma_3/3
A3 = (F(0), F(1, 3), F(1), F(1, 2), F(0))
B3 = (F(1, 3), F(0), F(0), F(0), F(-7, 24))
sigma3 = tuple(3 * (a + b) for a, b in zip(A3, B3))
check("S1c t^3 row: sigma_3 = 1 + gamma^3 + 3 gamma gamma_1 + (3/2) gamma_2 - (7/8) zeta(3), DERIVED (the owner's frozen formula confirmed independently)",
      sigma3 == (F(1), F(1), F(3), F(3, 2), F(-7, 8)))

# ===========================================================================
# S2: lambda_3 binomial identity over abstract sigma symbols
# ===========================================================================
# lambda_n = sum_{k=1..n} (-1)^(k+1) C(n,k) sigma_k; n = 3: 3, -3, 1
lam3 = (F(3), F(-3), F(1))
binom = tuple(F((-1) ** (k + 1)) * F(math.comb(3, k)) for k in range(1, 4))
check("S2 lambda_3 = 3 sigma_1 - 3 sigma_2 + sigma_3, exact binomial coefficients", lam3 == binom)

# ===========================================================================
# S3: measure normalization on the two finite instances
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
def z20conj(a):
    out = (0,) * 8
    for e in range(8):
        if a[e]:
            out = z20add(out, tuple(a[e] * x for x in z20pow(Z20, (19 * e) % 20)))
    return out
def f_of(n):
    tot = (0,) * 8
    for j in (1, 3, 7, 9):
        s = (0,) * 8
        for k in range(n):
            s = z20add(s, z20pow(z10, (j * k) % 10))
        tot = z20add(tot, z20mul(s, z20conj(s)))
    return tot[0]
fv = [f_of(n) for n in range(0, 13)]
def c10(m):
    s = (0,) * 8
    for j in (1, 3, 7, 9):
        s = z20add(s, z20pow(z10, (j * m) % 10))
    return s[0]
def p(v, m): return v[abs(m)]
ok = all(p(fv, m + 1) + p(fv, m - 1) - 2 * p(fv, m) == 2 * c10(m) for m in range(0, 11))
ok = ok and (fv[1] == 4) and (p(fv, 1) + p(fv, -1) - 2 * p(fv, 0) == 8)
I4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def g_of(n):
    tot = 0
    for j in range(4):
        s = (0, 0)
        for k in range(n):
            e = I4[(j * k) % 4]
            s = (s[0] + e[0], s[1] + e[1])
        tot += s[0] * s[0] + s[1] * s[1]
    return tot
gv = [g_of(n) for n in range(0, 13)]
ok = ok and all(p(gv, m + 1) + p(gv, m - 1) - 2 * p(gv, m) == (8 if m % 4 == 0 else 0) for m in range(0, 11))
ok = ok and (gv[1] == 4)
check("S3 normalization fix pinned on both instances: mu_v(T) = ladder(1) while t_m = 2 * cosine moments of mu_v (exemplar: t_m = 2 c_10(m); C_4: t_m = 2*4*[4|m]); hence sigma = 2 mu_v, sigma(T) = 2 lambda_1, mu_v(T) = lambda_1", ok)

# ===========================================================================
# S4: float witnesses (printed only)
# ===========================================================================
gamma = 0.5772156649015329
gamma1 = -0.07281584548367673
gamma2 = -0.009690363192872318
zeta3 = 1.2020569031595943
s1f = 1 + gamma / 2 - math.log(4 * math.pi) / 2
s2f = 1 + gamma * gamma + 2 * gamma1 - math.pi ** 2 / 8
s3f = 1 + gamma ** 3 + 3 * gamma * gamma1 + 1.5 * gamma2 - 0.875 * zeta3
l1f, l2f = s1f, 2 * s1f - s2f
l3f = 3 * s1f - 3 * s2f + s3f
print("S4 witness sigma_3 = %.12e ; lambda_3 = %.15f" % (s3f, l3f))
print("S4 witness owner lambda_3 interval [0.207638918333718933, 0.207638922051014329] contains float: %s"
      % (0.207638918333718933 < l3f < 0.207638922051014329))
t0, t1_, t2_ = 2 * l1f, l2f - 2 * l1f, l3f + l1f - 2 * l2f
detT2 = (t0 * (t0 * t0 - t1_ * t1_) - t1_ * (t1_ * t0 - t1_ * t2_)
         + t2_ * (t1_ * t1_ - t0 * t2_))
print("S4 witness t = (%.12f, %.12f, %.12f) ; det T_2 = %.10e" % (t0, t1_, t2_, detT2))
print("S4 witness owner det K_3 interval [6.9813247888e-14, 7.3758515923e-14] contains float: %s"
      % (6.9813247888e-14 < detT2 < 7.3758515923e-14))
print("S4 note: certifying det T_2 > 0 at the 7e-14 scale needs gamma_2 brackets of width about 1e-12: EM-4 remainder at N = 1e5 or EM-2 at N = 1e7; spec recorded for the two-architecture re-run")

print("FAILED: " + (", ".join(FAILED) if FAILED else "none"))
print("VERDICT: " + ("PASS amendment 3 of C-LI-COCYCLE-1" if not FAILED else "FAIL"))
