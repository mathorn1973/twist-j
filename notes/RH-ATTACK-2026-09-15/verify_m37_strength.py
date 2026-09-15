#!/usr/bin/env python3
"""verify_m37_strength.py -- exact verifier for ATTACK-M37-STRENGTH.md (lane C, 2026-09-15).

Revision after review (same date): CHECK 02 inert-factor test made non-tautological,
CHECK 03 label restricted to what is tested, CHECK 12 unnormalized exponent computed
independently of the normalized one, CHECK 13 decimal computed by exact integer
division, CHECK 14 extended to the exact endpoints of the b-range, and two checks
added: CHECK 16 (residue k-factor ratio G_k/G_1 = prod_{p|k}(1-2p^{-s})^{-1}, which
refutes the k-factor displayed in the pre-review note) and CHECK 17 (zero-freeness
of the F^{(1)}/O_5 correction product on Re s >= 1/2).

NON-CANONICAL. Python 3 standard library only. All gated arithmetic is int or
fractions.Fraction. Floating point occurs only in the block labelled DIAGNOSTIC,
which asserts nothing. Deterministic; run from a clean shell with
    LC_ALL=C PYTHONHASHSEED=0 python3 verify_m37_strength.py
Exit status 0 iff every check passes.

Objects checked (see the note for the definitions):
  chi = chi_5, split prime = p with chi(p) = 1, R = squarefree split-supported
  integers, f(r) = (-2)^omega(r) on R and 0 off R,
  F^{(k)}(s) = prod_{p split, p not | k} (1 - 2 p^{-s}) = sum_{r in R, (r,k)=1} f(r) r^{-s},
  zeta(s) L(s,chi) = zeta_F(s), F^{(k)} zeta_F = G_k (Euler product),
  beta*(kappa) = (3 - 2 kappa)/(4 - 2 kappa), beta_pole(kappa, w) = 1 - w/(2 - kappa),
  nu_sigma = (2860 sigma - 169)/9578 + (1261 - 2860 sigma)/3528.
"""
from fractions import Fraction as Fr
from math import gcd, isqrt
import sys

RESULTS = []


def check(name, ok, detail=""):
    RESULTS.append(bool(ok))
    line = "CHECK %02d %s: %s" % (len(RESULTS), "PASS" if ok else "FAIL", name)
    if detail:
        line += " [" + detail + "]"
    print(line)


# ---------------------------------------------------------------------------
# formal power series over Q, truncated at x^ORD (inclusive)
# ---------------------------------------------------------------------------
ORD = 12


def ps(coeffs):
    a = [Fr(0)] * (ORD + 1)
    for i, c in enumerate(coeffs[: ORD + 1]):
        a[i] = Fr(c)
    return a


def ps_mul(a, b):
    c = [Fr(0)] * (ORD + 1)
    for i in range(ORD + 1):
        if a[i] == 0:
            continue
        for j in range(ORD + 1 - i):
            c[i + j] += a[i] * b[j]
    return c


def ps_inv(a):
    assert a[0] != 0
    b = [Fr(0)] * (ORD + 1)
    b[0] = 1 / a[0]
    for n in range(1, ORD + 1):
        s = Fr(0)
        for i in range(1, n + 1):
            s += a[i] * b[n - i]
        b[n] = -s / a[0]
    return b


def ps_sub(a, b):
    return [a[i] - b[i] for i in range(ORD + 1)]


def ps_add(a, b):
    return [a[i] + b[i] for i in range(ORD + 1)]


def ps_eq(a, b):
    return all(a[i] == b[i] for i in range(ORD + 1))


ONE = ps([1])
X = ps([0, 1])
X2 = ps([0, 0, 1])
X3 = ps([0, 0, 0, 1])
one_minus_x = ps([1, -1])
one_minus_2x = ps([1, -2])
one_plus_x = ps([1, 1])
one_minus_x2 = ps([1, 0, -1])
one_plus_x2 = ps([1, 0, 1])
inv_1mx = ps_inv(one_minus_x)
inv_1mx_sq = ps_mul(inv_1mx, inv_1mx)

# CHECK 01: local factor identity at a split prime not dividing k
lhs = ps_mul(one_minus_2x, inv_1mx_sq)               # (1-2x)/(1-x)^2
rhs = ps_sub(ONE, ps_mul(X2, inv_1mx_sq))            # 1 - x^2/(1-x)^2
explicit = ps([1, 0] + [-(j - 1) for j in range(2, ORD + 1)])  # 1 - sum_{j>=2}(j-1)x^j
check("split local factor (1-2x)/(1-x)^2 = 1 - x^2/(1-x)^2 = 1 - sum_{j>=2}(j-1)x^j to order x^%d" % ORD,
      ps_eq(lhs, rhs) and ps_eq(lhs, explicit),
      "coefficients " + ",".join(str(c) for c in lhs[:6]) + ",...")

# CHECK 02: zeta(s)L(s,chi) local factors and the G_k local table
zeta_loc = inv_1mx
L_split = inv_1mx                        # chi(p) = 1
L_inert = ps_inv(one_plus_x)             # chi(p) = -1
L_ram = ONE                              # chi(5) = 0
zF_split = ps_mul(zeta_loc, L_split)
zF_inert = ps_mul(zeta_loc, L_inert)
zF_ram = ps_mul(zeta_loc, L_ram)
ok02 = (ps_eq(zF_split, inv_1mx_sq) and ps_eq(zF_inert, ps_inv(one_minus_x2)) and ps_eq(zF_ram, inv_1mx))
# G_k factors: split p not | k : (1-2x) * zF_split ; split p | k : zF_split ; inert : zF_inert ; 5 : zF_ram
G_split_free = ps_mul(one_minus_2x, zF_split)
G_split_k = zF_split
G_inert = zF_inert
G_ram = zF_ram
# the infinitely many factors (split p not | k, inert p) are 1 + O(x^2): coefficient of x^1 vanishes
ok02b = (G_split_free[1] == 0 and G_inert[1] == 0 and ps_eq(G_split_free, explicit)
         and ps_eq(G_inert, ps_inv(one_minus_x2))
         and ps_eq(G_inert, ps_add(ONE, ps_mul(X2, ps_inv(one_minus_x2))))   # 1 + x^2/(1-x^2)
         and G_split_k[1] == 2 and G_ram[1] == 1)
check("zeta L local factors (split 1/(1-x)^2, inert 1/(1-x^2), p=5 1/(1-x)) and G_k local table: infinite factors are 1+O(x^2)",
      ok02 and ok02b)

# CHECK 03: relation to the Canon orientation channel O_5: (1-2x)(1+x^2) = (1-x)^2 - 2x^3
poly_l = ps_mul(one_minus_2x, one_plus_x2)
poly_r = ps_sub(ps_mul(one_minus_x, one_minus_x), ps_mul(ps([2]), X3))
ratio = ps_mul(poly_l, inv_1mx_sq)     # F^{(1)}-factor / O_5-factor = (1-2x)(1+x^2)/(1-x)^2
ratio_claim = ps_sub(ONE, ps_mul(ps([0, 0, 0, 2]), inv_1mx_sq))
check("F^{(1)} local / O_5 local = (1-2x)(1+x^2)/(1-x)^2 = 1 - 2x^3/(1-x)^2 as formal series to x^%d (convergence: text; zero-freeness: CHECK 17)" % ORD,
      ps_eq(poly_l, poly_r) and ps_eq(ratio, ratio_claim))

# ---------------------------------------------------------------------------
# arithmetic: chi_5, split primes, f(r), Euler-product coefficients to N = 2000
# ---------------------------------------------------------------------------
N = 2000
CHI = (0, 1, -1, -1, 1)


def chi(n):
    return CHI[n % 5]


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i * i:: i] = bytearray(len(s[i * i:: i]))
    return [i for i in range(n + 1) if s[i]]


PR = primes_upto(N)
SPLIT = [p for p in PR if chi(p) == 1]
INERT = [p for p in PR if chi(p) == -1]
check("chi_5 table (0,1,-1,-1,1); split primes <= %d counted; smallest split prime is 11; 2^2 < 11 so |p^{-s}| < 1/2 on Re s >= 1/2"
      % N, SPLIT[0] == 11 and 2 * 2 < 11 and len(SPLIT) + len(INERT) + 1 == len(PR) and 5 in PR,
      "%d split, %d inert" % (len(SPLIT), len(INERT)))


def factor(n):
    out = []
    m = n
    for p in PR:
        if p * p > m:
            break
        if m % p == 0:
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            out.append((p, e))
    if m > 1:
        out.append((m, 1))
    return out


def f_val(n, k=1):
    """f(n) 1_{(n,k)=1}: (-2)^omega(n) if n squarefree and all prime factors split, else 0."""
    if gcd(n, k) != 1:
        return 0
    v = 1
    for p, e in factor(n):
        if e != 1 or chi(p) != 1:
            return 0
        v *= -2
    return v


def euler_coeffs(k):
    """coefficients c(n), n <= N, of prod_{p split, p not | k} (1 - 2 p^{-s}) (exact sieve)."""
    c = [0] * (N + 1)
    c[1] = 1
    for p in SPLIT:
        if k % p == 0:
            continue
        for n in range(N, p - 1, -1):
            if n % p == 0:
                c[n] -= 2 * c[n // p]
    return c


# CHECK 05: k = 1 coefficient identity
c1 = euler_coeffs(1)
ok05 = all(c1[n] == f_val(n) for n in range(1, N + 1))
n_supp = sum(1 for n in range(1, N + 1) if c1[n] != 0)
check("coefficients of prod_{p split}(1-2p^{-s}) agree with f(r)=(-2)^omega(r) on R and vanish off R, all r <= %d" % N,
      ok05, "%d nonzero coefficients; f(11)=%d, f(209)=%d, f(121)=%d, f(7)=%d" % (n_supp, c1[11], c1[209], c1[121], c1[7]))

# CHECK 06: coprime-to-k versions
ok06 = True
for k in (11, 209, 6061):
    ck = euler_coeffs(k)
    ok06 = ok06 and all(ck[n] == f_val(n, k) for n in range(1, N + 1))
check("coefficients of prod_{p split, p not | k}(1-2p^{-s}) equal f(r) 1_{(r,k)=1}, r <= %d, for k in {11, 209, 6061}" % N, ok06)


# CHECK 07: Dirichlet convolution f^{(k)} * a_F = g_k  (a_F = 1 * chi = ideal count of Q(sqrt5))
def dirichlet_conv(a, b):
    c = [0] * (N + 1)
    for d in range(1, N + 1):
        if a[d] == 0:
            continue
        for m in range(1, N // d + 1):
            c[d * m] += a[d] * b[m]
    return c


one_seq = [0] + [1] * N
chi_seq = [0] + [chi(n) for n in range(1, N + 1)]
aF = dirichlet_conv(one_seq, chi_seq)


def g_local(p, j, k):
    if p == 5:
        return 1
    if chi(p) == -1:
        return 1 if j % 2 == 0 else 0
    # split
    if k % p == 0:
        return j + 1                 # 1/(1-x)^2
    return -(j - 1)                  # 1 - sum_{j>=2}(j-1) x^j  (j = 1 gives 0)


def g_val(n, k):
    v = 1
    for p, e in factor(n):
        v *= g_local(p, e, k)
    return v


ok07 = True
for k in (1, 11, 209):
    fk = [0] + [f_val(n, k) for n in range(1, N + 1)]
    conv = dirichlet_conv(fk, aF)
    ok07 = ok07 and all(conv[n] == g_val(n, k) for n in range(1, N + 1))
    if k == 1:
        g1 = conv
check("Euler-product identity F^{(k)} zeta L = G_k at coefficient level: (f^{(k)} * (1*chi))(n) = g_k(n), n <= %d, k in {1, 11, 209}" % N,
      ok07, "g_1(11)=%d, g_1(121)=%d, g_1(1331)=%d, g_1(4)=%d, g_1(2)=%d, g_1(5)=%d" % (g1[11], g1[121], g1[1331], g1[4], g1[2], g1[5]))

# CHECK 08: G_k has zero coefficient at every squarefree n coprime to 5k (n > 1) -- the x^1 vanishing globally
ok08 = all(g1[n] == 0 for n in range(2, N + 1) if all(e == 1 for _, e in factor(n)) and n % 5 != 0)
check("g_1(n) = 0 for every squarefree n > 1 with 5 not | n, n <= %d (Euler factors are 1+O(p^{-2s}))" % N, ok08)

# ---------------------------------------------------------------------------
# threshold algebra
# ---------------------------------------------------------------------------


def poly_mul(a, b):
    c = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def poly_sub(a, b):
    n = max(len(a), len(b))
    a = a + [Fr(0)] * (n - len(a))
    b = b + [Fr(0)] * (n - len(b))
    return [a[i] - b[i] for i in range(n)]


# polynomials in kappa, coefficient lists [c0, c1, ...]
P_2mk = [Fr(2), Fr(-1)]          # 2 - kappa
P_3m2k = [Fr(3), Fr(-2)]         # 3 - 2 kappa
P_4m2k = [Fr(4), Fr(-2)]         # 4 - 2 kappa
lhs_poly = poly_mul(P_2mk, P_3m2k)
rhs_poly = poly_sub(poly_mul(P_2mk, P_4m2k), [c / 2 for c in P_4m2k])
ok09 = all(c == 0 for c in poly_sub(lhs_poly, rhs_poly))
# i.e. (2-kappa) beta* = (2-kappa) - 1/2 with beta* = (3-2kappa)/(4-2kappa): the sigma-terms cancel identically
check("threshold identity (2-k)(3-2k) = (2-k)(4-2k) - (4-2k)/2 as polynomials in kappa, i.e. U^{beta-sigma} = U^{1-sigma}T^{-1/2} at U=T^{2-kappa} iff beta = (3-2kappa)/(4-2kappa)",
      ok09, "both sides = 6 - 7k + 2k^2")


def beta_star(kap):
    return (3 - 2 * kap) / (4 - 2 * kap)


def beta_pole(kap, w):
    return 1 - w / (2 - kap)


kappas = [Fr(0), Fr(1, 2), Fr(49, 50), Fr(99, 100), Fr(999, 1000), Fr(1)]
ok10 = all(beta_pole(k, Fr(1, 2)) == beta_star(k) for k in kappas)
table = {Fr(0): Fr(3, 4), Fr(49, 50): Fr(26, 51), Fr(99, 100): Fr(51, 101), Fr(999, 1000): Fr(501, 1001), Fr(1): Fr(1, 2)}
ok10 = ok10 and all(beta_star(k) == v for k, v in table.items())
# sigma-independence: the exponent equation with sigma present
for sig in (Fr(51, 200), Fr(1, 4), Fr(13, 50)):
    for k in kappas:
        b = beta_star(k)
        ok10 = ok10 and ((2 - k) * (b - sig) == (2 - k) * (1 - sig) - Fr(1, 2))
check("beta*(kappa) = beta_pole(kappa, 1/2); table beta*(0)=3/4, beta*(0.98)=26/51, beta*(0.99)=51/101, beta*(0.999)=501/1001, beta*(1)=1/2; sigma cancels",
      ok10)

# ---------------------------------------------------------------------------
# nu_sigma and exponent bookkeeping
# ---------------------------------------------------------------------------


def nu(sig):
    return (2860 * sig - 169) / Fr(9578) + (1261 - 2860 * sig) / Fr(3528)


SIG = Fr(51, 200)
NU = nu(SIG)
ok11 = (NU == Fr(7069361, 33791184)) and (2 * NU < 1)
for sig in (Fr(1, 4), Fr(13, 50)):        # nu is affine in sigma: endpoint checks cover the strip
    ok11 = ok11 and (0 < nu(sig) < sig) and (2 * nu(sig) < 1)
tail_proved = 1 - 3 * SIG / 2 + NU / 2
tail_target = 1 - 3 * SIG / 2
ok11 = ok11 and tail_target == Fr(247, 400)
check("nu(51/200) = 7069361/33791184; 0 < nu < sigma and 2 nu < 1 at sigma in {1/4, 13/50}; tail target exponent 1 - 3 sigma/2 = 247/400",
      ok11, "proved tail exponent = %s, excess nu/2 = %s" % (tail_proved, NU / 2))

# CHECK 12: mean-value versus target exponents (powers of T, squared norms), U = T^{2-kappa}
ok12 = True
rows = []
for k in (Fr(0), Fr(1, 2), Fr(49, 50), Fr(1)):
    eU = 2 - k                                     # U = T^{eU}
    e_mv_first = eU * (1 - 2 * SIG)                # (U^{1/2-sigma})^2
    e_mv_second = eU * (1 - 2 * SIG) + (eU - 1)    # U^{1-2sigma} * U/T
    e_mv_norm = max(e_mv_first, e_mv_second)
    # unnormalized exponent read directly from Proposition 6: int_T^{2T}|F_U|^2 << (T + U) U^{1-2 sigma}
    e_mv_unnorm = max(Fr(1), eU) + eU * (1 - 2 * SIG)
    e_target = 2 * eU * (1 - SIG) - 1              # (U^{1-sigma} T^{-1/2})^2
    rows.append((k, e_mv_first, e_mv_second, e_target, e_mv_unnorm))
    ok12 = (ok12 and (e_mv_second == e_target) and (e_mv_first <= e_mv_second)
            and (e_mv_unnorm - e_target == 1) and (e_mv_unnorm - 1 == e_mv_norm))
# the (M32) gap is a different quantity: 2 nu, strictly between 0 and 1
gap_m32 = 2 * NU
ok12 = ok12 and (0 < gap_m32 < 1)
check("normalized mean value U^{1-2s}(1+U/T) sits exactly at the (M37) target exponent for all kappa in [0,1]; the unnormalized exponent (T+U)U^{1-2s} of Proposition 6, formed independently, exceeds the target by exactly 1; (M32) gap 2nu is neither 0 nor 1",
      ok12, "at kappa=0 (U=Y=T^2): MV %s = target %s, unnormalized %s; 2nu = %s" % (rows[0][2], rows[0][3], rows[0][4], gap_m32))

# CHECK 13: single-pole budget: ratio exponent (weighted pole term)^2 / target^2 = 2 w - 2 (2-kappa)(1-beta)
ok13 = True
for k in kappas:
    for b in (Fr(1, 2) + Fr(1, 100), Fr(3, 5), Fr(3, 4), Fr(9, 10), Fr(99, 100)):
        r_W = 0 - 2 * (2 - k) * (1 - b)            # (W): w = 0
        r_max = 2 * NU - 2 * (2 - k) * (1 - b)     # unconditional pointwise ceiling w = nu
        r_task = 2 * Fr(1, 2) - 2 * (2 - k) * (1 - b)   # task threshold reading w = 1/2
        ok13 = ok13 and (r_W < 0)
        ok13 = ok13 and ((r_max <= 0) == (b <= beta_pole(k, NU)))
        ok13 = ok13 and ((r_task <= 0) == (b <= beta_star(k)))
    ok13 = ok13 and beta_pole(k, Fr(0)) == 1 and beta_pole(k, NU) > beta_star(k)
bp99 = beta_pole(Fr(99, 100), NU)
bp99_dec = bp99.numerator * 10 ** 5 // bp99.denominator        # exact integer division, truncated
# the sign statement as an identity: 2w - 2(2-kappa)(1-beta) is affine in beta with slope 2(2-kappa) > 0,
# so its sign on beta < 1 is settled by the value at beta = 1 (= 2w) and at beta = 1 - w/(2-kappa) (= 0)
ok13b = all((0 - 2 * (2 - k) * (1 - Fr(1)) == 0) and (2 * NU - 2 * (2 - k) * (1 - beta_pole(k, NU)) == 0)
            and (2 - k > 0) for k in kappas)
check("single-pole ratio exponent 2w - 2(2-kappa)(1-beta) (affine in beta, slope 2(2-kappa) > 0, zero at beta_pole): negative for all beta<1 under (W) (w=0); nonpositive iff beta <= 1 - w/(2-kappa) (sampled 5 betas x 6 kappas plus the affine identity); beta_pole(kappa,nu) > beta*(kappa) since 2nu < 1",
      ok13 and ok13b, "beta_pole(0.99, nu) = %s ~ 0.%05d (truncated, exact integer division)" % (bp99, bp99_dec))

# CHECK 14: Lorentzian shape and window bounds (exact rational sample points)
ok14 = True
for (b, s, g, t) in ((Fr(3, 4), Fr(51, 200), Fr(1000), Fr(1000)), (Fr(3, 5), Fr(51, 200), Fr(1000), Fr(2001, 2)),
                     (Fr(51, 100), Fr(13, 50), Fr(1500), Fr(1499))):
    d2 = (b - s) ** 2 + (g - t) ** 2
    ok14 = ok14 and d2 == (b - s) * (b - s) + (g - t) * (g - t) and d2 > 0
    bb = b - s
    ok14 = ok14 and (Fr(6, 25) <= bb <= Fr(3, 4))          # beta - sigma in [1/2-13/50, 1-1/4]
    if abs(g - t) <= 1:
        ok14 = ok14 and (1 / (bb * bb + 1) <= 1 / d2 <= 1 / (bb * bb))
# exact endpoints of the half-width range: beta in (1/2, 1), sigma in (1/4, 13/50)
ok14 = ok14 and (Fr(1, 2) - Fr(13, 50) == Fr(6, 25)) and (Fr(1) - Fr(1, 4) == Fr(3, 4))
# two-sided window inequality b^2 <= b^2 + d^2 <= b^2 + 1 for 0 <= d <= 1, at the endpoints of both ranges
for bb in (Fr(6, 25), Fr(3, 4)):
    for d in (Fr(0), Fr(1, 2), Fr(1)):
        ok14 = ok14 and (bb * bb <= bb * bb + d * d <= bb * bb + 1)
    ok14 = ok14 and (2 / (1 + bb * bb) <= 2 / (bb * bb))       # window length 2 times the two-sided bound
check("|rho - s|^2 = (beta-sigma)^2 + (gamma-t)^2 (three exact sample points); b-range endpoints 1/2 - 13/50 = 6/25 and 1 - 1/4 = 3/4 exact; window inequality b^2 <= b^2 + d^2 <= b^2 + 1 at d in {0, 1/2, 1} and b at both endpoints",
      ok14)

# CHECK 15: F_U^{(k)} coefficient energy at the sieve scale: sum_{r<=N} f(r)^2 r^{-2 sigma} rational bookkeeping is not needed;
# instead verify |f(r)|^2 = (a_chi * a_chi)(r) on R (used by (A11)/(A60)) for r <= N
achi = aF                                    # a_chi = 1 * chi
achi2 = dirichlet_conv(achi, achi)
ok15 = all((c1[n] * c1[n] == achi2[n]) for n in range(1, N + 1) if c1[n] != 0)
ok15 = ok15 and all(abs(c1[n]) == achi[n] for n in range(1, N + 1) if c1[n] != 0)
check("|f(r)| = a_chi(r) and f(r)^2 = (a_chi*a_chi)(r) on R, r <= %d (input of the mean-value bound (A60))" % N, ok15)

# CHECK 16 (added after review): residue k-factor.  G_{k,p}/G_{1,p} at split p | k is
# (1-x)^{-2} / [(1-2x)(1-x)^{-2}] = 1/(1-2x), so G_k = G_1 prod_{p|k} (1 - 2 p^{-s})^{-1}.
# (The pre-review note displayed prod_{p|k} (1-p^{-s})^2/(1-2p^{-s}); that is refuted here.)
ratio_local = ps_mul(G_split_k, ps_inv(G_split_free))          # (1-x)^{-2} / [(1-2x)(1-x)^{-2}]
ratio_true = ps_inv(one_minus_2x)                              # 1/(1-2x) = sum 2^j x^j
ratio_old = ps_mul(ps_mul(one_minus_x, one_minus_x), ps_inv(one_minus_2x))   # (1-x)^2/(1-2x)
ok16 = ps_eq(ratio_local, ratio_true) and not ps_eq(ratio_local, ratio_old)
ok16 = ok16 and all(ratio_true[j] == 2 ** j for j in range(ORD + 1))
# numerical instance at p = 11, s = 2 (x = 1/121), exact rationals
Xv = Fr(1, 121)
ok16 = ok16 and ((1 / (1 - Xv) ** 2) / ((1 - 2 * Xv) / (1 - Xv) ** 2) == Fr(121, 119) == 1 / (1 - 2 * Xv))
ok16 = ok16 and ((1 - Xv) ** 2 / (1 - 2 * Xv) == Fr(14400, 14399))


def dirichlet_inv(a):
    """Dirichlet inverse of an integer sequence with a[1] = 1, indices 1..N."""
    b = [0] * (N + 1)
    b[1] = 1
    for n in range(2, N + 1):
        acc = 0
        for d in range(2, n + 1):
            if n % d == 0 and a[d] != 0:
                acc += a[d] * b[n // d]
        b[n] = -acc
    return b


g1_inv = dirichlet_inv(g1)
ok16c = True
detail16 = []
for k in (11, 209):
    gk = [0] + [g_val(n, k) for n in range(1, N + 1)]
    quot = dirichlet_conv(g1_inv, gk)                            # coefficients of G_k / G_1
    # expected: prod_{p | k} (1 - 2 p^{-s})^{-1} = sum over n supported on primes dividing k of 2^{Omega(n)} n^{-s}
    for n in range(1, N + 1):
        fac = factor(n)
        if all(k % p == 0 for p, _ in fac):
            exp_val = 2 ** sum(e for _, e in fac)
        else:
            exp_val = 0
        ok16c = ok16c and quot[n] == exp_val
    detail16.append("k=%d: (G_k/G_1)(11)=%d, (121)=%d, (1331)=%d, (209)=%d, (19)=%d" % (k, quot[11], quot[121], quot[1331], quot[209], quot[19]))
check("residue k-factor: G_{k,p}/G_{1,p} = 1/(1-2x) (formal series to x^%d, coefficients 2^j), not (1-x)^2/(1-2x); at p=11, s=2 the ratio is 121/119 (old display 14400/14399); coefficient level (G_k/G_1)(n) = 2^Omega(n) on n supported on p|k, 0 otherwise, n <= %d, k in {11, 209}" % (ORD, N),
      ok16 and ok16c, "; ".join(detail16))

# CHECK 17 (added after review): the correction product prod_{split}(1 - 2x^3/(1-x)^2) is zero-free on
# Re s >= 1/2: with y = |x| <= 11^{-1/2}, 2y^3/(1-y)^2 < 1/8 iff 16 y^3 < (1-y)^2; using y^2 = 1/11 at the
# extreme point this is 16y/11 < 12/11 - 2y iff 38 y < 12 iff y < 6/19 iff 1/11 < 36/361 iff 361 < 396.
# The function 2y^3/(1-y)^2 is increasing on (0,1), so the bound at y = 11^{-1/2} covers all split p >= 11.
y2 = Fr(1, 11)
ok17 = (y2 < Fr(6, 19) ** 2) and (361 < 396)
# second, self-contained route: the rational witness y_w = 302/1000 exceeds 11^{-1/2} exactly (y_w^2 * 11 > 1),
# and 2 y_w^3/(1-y_w)^2 < 1/8; since 2y^3/(1-y)^2 is increasing on (0,1) (numerator increasing, denominator
# decreasing), every y <= 11^{-1/2} < y_w satisfies the bound.  Monotonicity sampled on a rational grid.
yw = Fr(302, 1000)
ok17 = ok17 and (yw * yw * 11 > 1) and (2 * yw ** 3 / (1 - yw) ** 2 < Fr(1, 8))
grid = [Fr(j, 1000) for j in range(1, 400)]
vals = [2 * y ** 3 / (1 - y) ** 2 for y in grid]
ok17 = ok17 and all(vals[i] < vals[i + 1] for i in range(len(vals) - 1))
check("F^{(1)}/O_5 correction factor 1 - 2x^3/(1-x)^2 is zero-free at every split prime on Re s >= 1/2: |2x^3/(1-x)^2| < 1/8 at y = 11^{-1/2}, reduced exactly to 1/11 < (6/19)^2 (361 < 396); rational witness y_w = 0.302 > 11^{-1/2} (0.302^2 * 11 > 1) with 2y_w^3/(1-y_w)^2 < 1/8; monotonicity of 2y^3/(1-y)^2 sampled on y = 0.001..0.399",
      ok17, "2 y_w^3/(1-y_w)^2 = %s" % (2 * yw ** 3 / (1 - yw) ** 2))

# ---------------------------------------------------------------------------
# DIAGNOSTIC (floating point, asserts nothing)
# ---------------------------------------------------------------------------
print("DIAGNOSTIC (floats, no assertions):")
from math import atan, pi
print("  nu(51/200) = %.9f, 2nu = %.9f, proved tail exponent = %.9f, target = %.4f" % (float(NU), float(2 * NU), float(tail_proved), float(tail_target)))
for k in (Fr(0), Fr(49, 50), Fr(99, 100), Fr(999, 1000), Fr(1)):
    print("  kappa=%-6s beta*=%-8.5f beta_pole(kappa,nu)=%-8.5f beta_pole(kappa,0)=1" % (k, float(beta_star(k)), float(beta_pole(k, NU))))
for bb in (0.24, 0.5, 0.75):
    print("  beta-sigma=%.2f: Lorentzian mass fraction inside |t-gamma|<=1 = %.4f" % (bb, (2 / pi) * atan(1 / bb)))

npass = sum(RESULTS)
print("CHECKS: %d of %d PASS" % (npass, len(RESULTS)))
sys.exit(0 if npass == len(RESULTS) else 1)
