#!/usr/bin/env python3
# verify_toral_haar_nogo.py
# C-LI-TORAL-HAAR-1: exact machine pins for the toral Haar-Koopman no-go.
#
# The analytic theorem (candidate document, section 2) is a proof, not a
# computation; this verifier pins its exact skeleton: the Cayley dictionary
# between critical-line zeros and unit-circle atoms, the forced-measure
# ladder dictionary on synthetic rational instances, the character-orbit
# obstruction for the hyperbolic toral Koopman operator, and the exact
# calculus behind the accumulation law. Imported classical inputs (Li's
# criterion; the countable-Lebesgue decomposition of hyperbolic toral
# Koopman operators; Fourier uniqueness of finite measures on T; the
# Riemann-von Mangoldt count) are named in the document and are NOT
# asserted here.
#
# Statements frozen before the single run:
#   TH1  Cayley dictionary, exact in Q(i) at rational gamma: for
#        rho = 1/2 + i gamma, z = (rho-1)/rho satisfies |z|^2 = 1,
#        1 - z = 1/rho, |1-z|^2 = 1/(gamma^2 + 1/4).
#   TH2  Half-angle law, exact: Re z = (gamma^2-1/4)/(gamma^2+1/4),
#        Im z = gamma/(gamma^2+1/4), and Im(z) * 2 gamma = 1 + Re(z),
#        i.e. tan(theta/2) = 1/(2 gamma), theta = 2 arctan(1/(2 gamma)).
#   TH3  Forced-measure dictionary on a synthetic rational zero multiset
#        Gamma = {(1,1), (3/2,2), (7,1)} (gamma, multiplicity), exact in Q
#        via Chebyshev recurrence on x = cos theta:
#        (i)   the atom weight w = m/(gamma^2+1/4) equals 2 m (1 - x);
#        (ii)  lambda_n := sum 2 m (1 - T_n(x)) equals
#              (1/2) int |D_n|^2 d sigma_xi for n = 0..10;
#        (iii) t_n := lambda_{n+1} + lambda_{n-1} - 2 lambda_n equals
#              sigma_xi_hat(n) = sum 2 w T_n(x) for n = 0..10;
#        (iv)  sigma_xi(T) = t_0 = 2 lambda_1.
#   TH4  Hyperbolic toral character-orbit obstruction, exact in Z: for
#        A = [[2,1],[1,1]] (det 1, trace 3 > 2), det(A^k - I) = 2 - tr(A^k)
#        and it is nonzero for k = 1..300; hence no nonconstant character
#        of T^2 is fixed by any power of the Koopman operator, the exact
#        skeleton of the empty-point-spectrum import.
#   TH5  Accumulation-law calculus, exact symbolic coefficients over the
#        basis (1, log gamma, log 2pi) and (1, log eps, log 2pi):
#        d/dgamma [ -(log(gamma/2pi) + 1)/gamma ] = log(gamma/2pi)/gamma^2,
#        and -F(1/eps) = eps (log(1/(2 pi eps)) + 1).
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
ONE = (F(1), F(0))

def cadd(a, b): return (a[0] + b[0], a[1] + b[1])
def csub(a, b): return (a[0] - b[0], a[1] - b[1])
def cmul(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def cdiv(a, b):
    d = b[0] * b[0] + b[1] * b[1]
    return ((a[0] * b[0] + a[1] * b[1]) / d, (a[1] * b[0] - a[0] * b[1]) / d)
def cabs2(a): return a[0] * a[0] + a[1] * a[1]

GAMMAS = [F(1), F(3, 2), F(7, 3), F(14), F(101, 7)]

# ===========================================================================
# TH1: Cayley dictionary
# ===========================================================================
ok = True
for g in GAMMAS:
    rho = (F(1, 2), g)
    z = cdiv(csub(rho, ONE), rho)
    ok = ok and cabs2(z) == 1
    ok = ok and csub(ONE, z) == cdiv(ONE, rho)
    ok = ok and cabs2(csub(ONE, z)) == 1 / (g * g + F(1, 4))
check("TH1 Cayley dictionary exact at five rational gammas: |z|^2 = 1, 1 - z = 1/rho, |1-z|^2 = 1/(gamma^2+1/4) for z = (rho-1)/rho, rho = 1/2 + i gamma", ok)

# ===========================================================================
# TH2: half-angle law
# ===========================================================================
ok = True
for g in GAMMAS:
    rho = (F(1, 2), g)
    z = cdiv(csub(rho, ONE), rho)
    d = g * g + F(1, 4)
    ok = ok and z[0] == (g * g - F(1, 4)) / d and z[1] == g / d
    ok = ok and z[1] * 2 * g == 1 + z[0]
check("TH2 half-angle law exact: Re z = (gamma^2-1/4)/(gamma^2+1/4), Im z = gamma/(gamma^2+1/4), Im(z) * 2 gamma = 1 + Re(z), so theta_gamma = 2 arctan(1/(2 gamma))", ok)

# ===========================================================================
# TH3: forced-measure dictionary on the synthetic zero multiset
# ===========================================================================
SYNTH = [(F(1), 1), (F(3, 2), 2), (F(7), 1)]

def cheb(x, n):
    a, b = F(1), x
    if n == 0:
        return a
    for _ in range(n - 1):
        a, b = b, 2 * x * b - a
    return b

xs = [((g * g - F(1, 4)) / (g * g + F(1, 4)), m, g) for g, m in SYNTH]
ok = all(F(m) / (g * g + F(1, 4)) == 2 * m * (1 - x) for x, m, g in xs)

def lam(n):
    n = abs(n)
    return sum(2 * m * (1 - cheb(x, n)) for x, m, g in xs)

for n in range(0, 11):
    # (ii) ladder dictionary: (1/2) int |D_n|^2 d sigma_xi, atoms at +-theta
    # with weight w each; |D_n(theta)|^2 = (2 - 2 cos n theta)/(2 - 2 cos theta)
    half_int = sum(
        F(m) / (g * g + F(1, 4)) * (2 - 2 * cheb(x, n)) / (2 - 2 * x)
        for x, m, g in xs)          # (1/2) * 2 atoms = 1 * per-pair value
    ok = ok and lam(n) == half_int
    # (iii) second differences equal the Fourier coefficients of sigma_xi
    t_n = lam(n + 1) + lam(n - 1) - 2 * lam(n)
    sigma_hat = sum(2 * (F(m) / (g * g + F(1, 4))) * cheb(x, n) for x, m, g in xs)
    ok = ok and t_n == sigma_hat
# (iv) total mass: sigma_xi(T) = 2 lambda_1 = t_0 (= lam(1) + lam(-1) - 2 lam(0))
sigma_mass = sum(2 * (F(m) / (g * g + F(1, 4))) for x, m, g in xs)
ok = ok and sigma_mass == 2 * lam(1)
ok = ok and sigma_mass == lam(0 + 1) + lam(0 - 1) - 2 * lam(0)
check("TH3 forced-measure dictionary exact on the synthetic multiset {(1,1),(3/2,2),(7,1)}: w = m/(gamma^2+1/4) = 2m(1-cos theta); lambda_n = (1/2) int |D_n|^2 d sigma_xi and t_n = sigma_xi_hat(n) for n = 0..10; sigma_xi(T) = t_0 = 2 lambda_1", ok)

# ===========================================================================
# TH4: hyperbolic toral character-orbit obstruction
# ===========================================================================
def mmul(P, Q):
    return ((P[0][0] * Q[0][0] + P[0][1] * Q[1][0], P[0][0] * Q[0][1] + P[0][1] * Q[1][1]),
            (P[1][0] * Q[0][0] + P[1][1] * Q[1][0], P[1][0] * Q[0][1] + P[1][1] * Q[1][1]))

A = ((2, 1), (1, 1))
ok = (A[0][0] * A[1][1] - A[0][1] * A[1][0] == 1) and (A[0][0] + A[1][1] == 3)
P = ((1, 0), (0, 1))
prev_tr = 2
for k in range(1, 301):
    P = mmul(P, A)
    tr = P[0][0] + P[1][1]
    detAkI = (P[0][0] - 1) * (P[1][1] - 1) - P[0][1] * P[1][0]
    ok = ok and detAkI == 2 - tr and detAkI != 0 and tr > prev_tr
    prev_tr = tr
check("TH4 character-orbit obstruction exact for A = [[2,1],[1,1]]: det A = 1, tr A = 3 > 2, and det(A^k - I) = 2 - tr(A^k) < 0 for k = 1..300 (trace strictly increasing): no nonzero lattice character is fixed by any Koopman power", ok)

# ===========================================================================
# TH5: accumulation-law calculus, exact symbolic coefficients
# ===========================================================================
# F(gamma) = (a + b log gamma + c log 2pi)/gamma with (a,b,c) = (-1,-1,1)
# equals -(log(gamma/2pi) + 1)/gamma.
a, b, c = F(-1), F(-1), F(1)
# F'(gamma) = ((b - a) - b log gamma - c log 2pi)/gamma^2; target
# log(gamma/2pi)/gamma^2 has coefficients (0, 1, -1).
ok = (b - a, -b, -c) == (F(0), F(1), F(-1))
# -F(1/eps) = (-a + b log eps ... ) with log(1/eps) = -log eps:
# -F(1/eps) = (-a, b, -c) . (1, log eps, log 2pi) * eps; target
# eps (log(1/(2 pi eps)) + 1) = eps (1 - log eps - log 2pi).
ok = ok and (-a, b, -c) == (F(1), F(-1), F(-1))
check("TH5 accumulation-law calculus exact: d/dgamma[-(log(gamma/2pi)+1)/gamma] = log(gamma/2pi)/gamma^2 and -F(1/eps) = eps (log(1/(2 pi eps)) + 1), coefficientwise over (1, log, log 2pi)", ok)

# ===========================================================================
# Float witnesses (printed only, never asserted)
# ===========================================================================
th1 = 2 * math.atan(0.5)
print("W1 witness theta_gamma at synthetic gamma = 1: theta = %.12f rad (atom pair at exp(+-i theta), weight 1/(1+1/4) = 0.8)" % th1)
eps = 1e-3
lead = (eps / math.pi) * (math.log(1.0 / (2 * math.pi * eps)) + 1)
print("W2 witness accumulation leading term at eps = 1e-3: M_xi(eps) ~ %.12e (remainder O(eps^2 log(1/eps)) analytic)" % lead)
print("W3 no-go summary: exact Haar cocycle => lambda_n >= 0 => RH => symmetrized spectral measure = sigma_xi, purely atomic with atoms off 1; hyperbolic toral Koopman off constants is countable Lebesgue, atomless: contradiction; the standard toral Haar-Koopman realization is excluded unconditionally")

print("FAILED: " + (", ".join(FAILED) if FAILED else "none"))
print("VERDICT: " + ("PASS C-LI-TORAL-HAAR-1" if not FAILED else "FAIL"))
