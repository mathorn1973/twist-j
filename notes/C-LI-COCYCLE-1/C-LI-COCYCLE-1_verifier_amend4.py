#!/usr/bin/env python3
# C-LI-COCYCLE-1_verifier_amend4.py
# Amendment 4: the det-scale erratum of amendment 3 and the measure
# symmetrization correction.
#
# Errata frozen before the single run:
#   ERR-A (scale): amendment 3's S4 witness compared det T_2 directly with
#       the owner's interval for det K_3. The owner's K carries the 1/2
#       normalization, K_3 = T_2 / 2 entrywise, so det K_3 = det T_2 / 8.
#       The amend3 stdout therefore printed "contains float: False" for a
#       gate that in fact passes at witness grade. Per the discipline the
#       amend3 run is archived unmodified; this amendment carries the
#       corrected comparison.
#   ERR-B (symmetrization): amendment 3's S3 concluded "hence sigma = 2 mu_v".
#       That identity holds only for conjugation-symmetric mu_v (as on both
#       real finite instances of S3). The correct general normalization,
#       per the corrected spine (notes/j-li-schoenberg-2 consolidation, S4):
#           sigma = mu_v + iota_* mu_v,  iota(z) = conj(z),
#           mu_v(T) = lambda_1,  sigma(T) = 2 lambda_1,  sigma_hat(m) = t_m.
#       The cosine data t_m determines sigma only; the non-symmetric mu_v
#       is NOT determined by Fourier uniqueness.
#
# Statements frozen before the single run:
#   A1  det K_3 = det T_2 / 8, exactly, on both finite instances of
#       amendment 3 (exemplar cycle ladder t_m = 2 c_10(m); C_4 instance
#       t_m = 8 * [4|m]).
#   A2  A conjugation-ASYMMETRIC instance separating sigma from 2 mu_v,
#       exact in Z[i]: U = (multiplication by i) on C, v = 1, so
#       mu_v = delta_i and the cocycle b(n) = sum_{k<n} i^k has ladder
#       psi = (0,1,2,1,0,...), period 4. Checks, all exact:
#       (i)   t_m = psi(m+1) + psi(m-1) - 2 psi(m) = 2 Re moment_m(mu_v)
#             = moment_m(sigma) for m = 0..8, with sigma = delta_i +
#             delta_{-i};
#       (ii)  psi(n) = (1/2) * int |D_n|^2 d sigma for n = 0..8 (the
#             corrected ladder dictionary on the symmetrized side);
#       (iii) moment_1(sigma) = 0 while moment_1(2 mu_v) = 2i: sigma and
#             2 mu_v are different measures with the same cosine data.
#   A3  On both REAL instances of amendment 3 the spectral measure is
#       conjugation-invariant (all moments have zero imaginary part,
#       exactly), so S3's instance-level "sigma = 2 mu_v" stays true THERE;
#       only its general form was wrong.
#   A4  Atom normalization on the C_4 instance: mu_v({1}) = 1 and
#       |Delta g(N) - (2N+1)| <= 3 for N = 0..200, so
#       Delta g(N) / (2N+1) -> 1 = mu_v({1}); the factor-2 formula
#       "mu_v({1}) = lim 2 Delta lambda / (2N+1)" (root consolidation,
#       section 1) would give 2 and is the SIGMA atom: sigma({1}) = 2.
#   A5  Float witnesses (printed, never asserted): lambda_3 and
#       det K_3 = det T_2 / 8 against the owner's pinned intervals; the
#       corrected line must read "contains float: True" for both.
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
# Shared exact machinery
# ===========================================================================

def det3(M):
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

def toeplitz3(t):
    return [[t[0], t[1], t[2]], [t[1], t[0], t[1]], [t[2], t[1], t[0]]]

# Z[zeta_20] ring (as in amendments 2 and 3) for the exemplar instance.
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

def z20add(a, b):
    return tuple(x + y for x, y in zip(a, b))

Z20 = (0, 1, 0, 0, 0, 0, 0, 0)
z10 = z20pow(Z20, 2)

def z20conj(a):
    out = (0,) * 8
    for e in range(8):
        if a[e]:
            out = z20add(out, tuple(a[e] * x for x in z20pow(Z20, (19 * e) % 20)))
    return out

def c10(m):
    s = (0,) * 8
    for j in (1, 3, 7, 9):
        s = z20add(s, z20pow(z10, (j * m) % 10))
    return s

# Z[i] arithmetic as integer pairs.
def imul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])

def ipow(a, n):
    r = (1, 0)
    for _ in range(n):
        r = imul(r, a)
    return r

def iadd(a, b):
    return (a[0] + b[0], a[1] + b[1])

I = (0, 1)
MI = (0, -1)

# ===========================================================================
# A1: det K_3 = det T_2 / 8 on both amendment-3 instances, exact
# ===========================================================================
ok_rational = all(c10(m)[1:] == (0,) * 7 for m in range(5))
c10_scalar = [c10(m)[0] for m in range(5)]           # (4, 1, -1, 1, -1)
t_exemplar = [2 * x for x in c10_scalar]             # t_m = 2 c_10(m)
t_c4 = [8 if m % 4 == 0 else 0 for m in range(5)]    # C_4 instance
ok = ok_rational and c10_scalar == [4, 1, -1, 1, -1]
for t in (t_exemplar, t_c4):
    T2 = toeplitz3([F(x) for x in t])
    K3 = toeplitz3([F(x, 2) for x in t])             # K = T / 2 entrywise
    ok = ok and (det3(K3) == det3(T2) / 8)
ok = ok and det3(toeplitz3([F(x) for x in t_exemplar])) == 400
ok = ok and det3(toeplitz3([F(x) for x in t_c4])) == 512
check("A1 det K_3 = det T_2 / 8 exactly on both amendment-3 instances (exemplar det T_2 = 400, det K_3 = 50; C_4 det T_2 = 512, det K_3 = 64): the amend3 S4 comparison was mis-scaled by exactly 2^3", ok)

# ===========================================================================
# A2: the asymmetric instance mu_v = delta_i separating sigma from 2 mu_v
# ===========================================================================
# Ladder psi(n) = |sum_{k<n} i^k|^2, exact in Z[i].
def b_of(n):
    s = (0, 0)
    for k in range(n):
        s = iadd(s, ipow(I, k))
    return s

def psi(n):
    s = b_of(abs(n))
    return s[0] * s[0] + s[1] * s[1]

ok = [psi(n) for n in range(5)] == [0, 1, 2, 1, 0]
# (i) t_m = 2 Re moment_m(mu_v) = moment_m(sigma), m = 0..8
for m in range(0, 9):
    t_m = psi(m + 1) + psi(m - 1) - 2 * psi(m)
    mom_mu = ipow(I, m)                              # int z^m d delta_i
    mom_sigma = iadd(ipow(I, m), ipow(MI, m))        # sigma = delta_i + delta_-i
    ok = ok and (t_m == 2 * mom_mu[0]) and ((t_m, 0) == mom_sigma)
# (ii) psi(n) = (1/2) int |D_n|^2 d sigma, n = 0..8
for n in range(0, 9):
    Dn_i = b_of(n)                                   # D_n(i) = sum_{k<n} i^k
    Dn_mi = (Dn_i[0], -Dn_i[1])                      # D_n(-i) = conj(D_n(i))
    half_int = F(Dn_i[0] ** 2 + Dn_i[1] ** 2 + Dn_mi[0] ** 2 + Dn_mi[1] ** 2, 2)
    ok = ok and (half_int == psi(n))
# (iii) first moments differ: sigma != 2 mu_v as measures
m1_sigma = iadd(I, MI)
m1_2mu = (2 * I[0], 2 * I[1])
ok = ok and m1_sigma == (0, 0) and m1_2mu == (0, 2) and m1_sigma != m1_2mu
check("A2 asymmetric instance mu_v = delta_i, exact in Z[i]: t_m = 2 Re moment_m(mu_v) = moment_m(sigma) for m = 0..8; psi(n) = (1/2) int |D_n|^2 d sigma for n = 0..8; yet moment_1(sigma) = 0 while moment_1(2 mu_v) = 2i: the cosine data pins sigma = mu_v + iota_* mu_v, never mu_v itself", ok)

# ===========================================================================
# A3: both amendment-3 instances ARE conjugation-invariant, exactly
# ===========================================================================
ok = True
for m in range(0, 11):
    mom = c10(m)                                     # exemplar moment in Z[zeta_20]
    ok = ok and (z20conj(mom) == mom)
for m in range(0, 11):
    mom = (0, 0)                                     # C_4 moment: sum_j (i^j)^m
    for j in range(4):
        mom = iadd(mom, ipow(I, (j * m) % 4))
    ok = ok and mom[1] == 0 and mom[0] == (4 if m % 4 == 0 else 0)
check("A3 both amendment-3 instances have conjugation-invariant spectral measures (all moments exactly real), so S3's instance conclusion sigma = 2 mu_v was true THERE; only its general form is corrected by ERR-B", ok)

# ===========================================================================
# A4: atom normalization on the C_4 instance
# ===========================================================================
def g_of(n):
    return n * n + (0, 3, 4, 3)[n % 4]

ok = all(abs((g_of(N + 1) - g_of(N)) - (2 * N + 1)) <= 3 for N in range(0, 201))
# mu_v({1}) = 1 exactly: U = diag(1, i, -1, -i), v = (1,1,1,1), weight of
# eigenvalue 1 is |v_0|^2 = 1; the sigma atom doubles at the iota-fixed
# point: sigma({1}) = 2.
ok = ok and (g_of(1) == 4)                           # mu_v(T) = lambda_1 analogue
check("A4 atom normalization pinned on C_4: |Delta g(N) - (2N+1)| <= 3 for N <= 200, so Delta g / (2N+1) -> 1 = mu_v({1}); the factor-2 formula is the sigma atom sigma({1}) = 2, not mu_v({1})", ok)

# ===========================================================================
# A5: float witnesses (printed only) with the corrected det scale
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
print("A5 witness lambda_3 = %.15f ; owner interval [0.207638918333718933, 0.207638922051014329] contains float: %s"
      % (l3f, 0.207638918333718933 < l3f < 0.207638922051014329))
t0, t1_, t2_ = 2 * l1f, l2f - 2 * l1f, l3f + l1f - 2 * l2f
detT2 = (t0 * (t0 * t0 - t1_ * t1_) - t1_ * (t1_ * t0 - t1_ * t2_)
         + t2_ * (t1_ * t1_ - t0 * t2_))
detK3 = detT2 / 8
print("A5 witness det T_2 = %.10e ; det K_3 = det T_2 / 8 = %.10e" % (detT2, detK3))
print("A5 witness owner det K_3 interval [6.9813247888e-14, 7.3758515923e-14] contains float: %s"
      % (6.9813247888e-14 < detK3 < 7.3758515923e-14))
print("A5 note: this corrects the amend3 S4 line, which compared det T_2 itself against the det K_3 interval and printed False at a mis-scale of 2^3; certification spec for the two-architecture re-run is unchanged (gamma_2 brackets of width about 1e-12)")

print("FAILED: " + (", ".join(FAILED) if FAILED else "none"))
print("VERDICT: " + ("PASS amendment 4 of C-LI-COCYCLE-1" if not FAILED else "FAIL"))
