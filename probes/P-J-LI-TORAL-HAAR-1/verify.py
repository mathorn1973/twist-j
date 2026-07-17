#!/usr/bin/env python3
# P-J-LI-TORAL-HAAR-1 exact verifier.
#
# Formal probe identity: probes/P-J-LI-TORAL-HAAR-1/PREREG.md, issue 50.
# This fresh copy is executed formally only after its immutable remote pin is
# read back. Earlier notes/C-LI-TORAL-HAAR-1 runs are non-formal preparation
# and are not evidence for this probe.
#
# Exact audit content:
#   - exact M_J characteristic data (the pinned Pillar A step matrix, as
#     in probes/P-ENTROPY-BRIDGE-1 and reproduce/dirac-ladder);
#   - algebraic modulus alternatives phi and phi^-1, exact in Z[zeta_5]
#     and Z[phi];
#   - the cyclotomic root-of-unity exclusion, proof-first with finite
#     exact case checks;
#   - the exterior-square non-escape pin: charpoly(Lambda^2 M_J) =
#     (y^2 - 3y + 1) Phi_10(y), while charpoly(M_J) has no cyclotomic
#     factor;
#   - NO libm anywhere: the former atan/log float witnesses are replaced
#     by deterministic directed Fraction intervals (alternating-series
#     brackets for arctan; atanh series with geometric tail bounds for
#     log; Machin bracket for pi); printed endpoints use directed
#     integer-scaled decimals, never float;
#   - the finite det(A^k - I) loops are labeled EXPLORATORY WITNESS; the
#     all-k, all-d statement follows directly from the carrier hypothesis
#     that A has no root-of-unity eigenvalue. TH5/TH6 place M_J in that class.
#
# Statements frozen before the single run:
#   TH1  Cayley dictionary, exact in Q(i) at rational gamma.
#   TH2  Half-angle law: theta_gamma = 2 arctan(1/(2 gamma)), exact.
#   TH3  Forced-measure dictionary on the synthetic rational multiset
#        {(1,1), (3/2,2), (7,1)}, exact via Chebyshev recurrence.
#   TH4  M_J characteristic data, exact in Z: for the pinned matrix,
#        charpoly(M_J) = Phi_5(x-1) = x^4 - 3x^3 + 4x^2 - 2x + 1,
#        det M_J = 1, tr M_J = 3, det(2I - M_J) = 5 (the Canon CODEC-TR4
#        cross-tie), p(1) = 1, p(-1) = 11.
#   TH5  Modulus alternatives, exact in Z[zeta_5]: alpha = z+z^4 and
#        beta = z^2+z^3 satisfy y^2+y-1 = 0, alpha+beta = -1,
#        alpha beta = -1; |1+z^a|^2 = 2+alpha for a in {1,4} and
#        2+beta for a in {2,3}; the two modulus-squares are the roots of
#        y^2 - 3y + 1 (sum 3, product 1), which under y = 1+u is exactly
#        u^2 - u - 1: the values are phi^2 = phi+1 and phi^-2 = 2-phi in
#        Z[phi]. y^2-3y+1 at y = 1 equals -1 != 0: NO eigenvalue of M_J
#        has modulus 1.
#   TH6  Cyclotomic exclusion, proof-first: p = charpoly(M_J) has no
#        rational root. By Gauss's lemma, a quadratic split would have
#        constants (b,d) = (1,1) or (-1,-1); a+c = -3 then forces the
#        linear coefficient to -3 or 3, never -2. Thus p is irreducible.
#        The imported elementary bound eulerphi(m) >= sqrt(m/2) confines
#        eulerphi(m) = 4 to m <= 32; exact enumeration gives
#        {5,8,10,12}. p differs from all four cyclotomic polynomials.
#   TH7  Exterior-square non-escape, exact in Z: Lambda^2 M_J is the
#        pinned 6x6 integer matrix of 2x2 minors and
#        charpoly(Lambda^2 M_J) = (y^2 - 3y + 1) Phi_10(y). The primitive
#        tenth roots live in Lambda^2 M_J only; the Koopman character
#        action is through M_J^T on Z^4, whose charpoly is p (TH4/TH6,
#        cyclotomic-free). The Phi_10 factor is therefore not an escape.
#   TH8  Directed bracket for theta at gamma = 1: 2 arctan(1/2) enclosed
#        by exact alternating-series partial sums; width < 10^-20;
#        endpoints printed as directed 24-digit decimals.
#   TH9  Directed bracket for the accumulation leading term at
#        eps = 1/1000: L = (eps/pi)(log(1/(2 pi eps)) + 1) with
#        pi by Machin (16 arctan(1/5) - 4 arctan(1/239), alternating
#        brackets), log 2 = 2 artanh(1/3), log 5 = 2 artanh(2/3),
#        log pi by artanh at the rational pi endpoints, geometric tail
#        bounds; directed interval arithmetic throughout; width < 10^-20;
#        endpoints printed as directed 24-digit decimals.
#   X1   EXPLORATORY WITNESS (finite, exact, not a theorem gate): det(A^k - I)
#        != 0 for the cat map [[2,1],[1,1]] with det(A^k - I) =
#        2 - tr(A^k), k = 1..300, and for M_J, k = 1..120. The all-k,
#        all-d statement follows from the carrier hypothesis, not these loops.
#
# Discipline: stdlib only; exact arithmetic in every assertion; no float
# operation occurs anywhere in this file. Environment: LC_ALL=C LANG=C
# PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.

from fractions import Fraction
from math import gcd
import itertools

FAILED_GATES = []
FAILED_WITNESSES = []

def check(name, ok, *, theorem_gate=True):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        if theorem_gate:
            FAILED_GATES.append(name)
        else:
            FAILED_WITNESSES.append(name)

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
# TH1, TH2: Cayley dictionary and half-angle law (unchanged from v1)
# ===========================================================================
ok = True
for g in GAMMAS:
    rho = (F(1, 2), g)
    z = cdiv(csub(rho, ONE), rho)
    ok = ok and cabs2(z) == 1
    ok = ok and csub(ONE, z) == cdiv(ONE, rho)
    ok = ok and cabs2(csub(ONE, z)) == 1 / (g * g + F(1, 4))
check("TH1 Cayley dictionary exact at five rational gammas: |z|^2 = 1, 1 - z = 1/rho, |1-z|^2 = 1/(gamma^2+1/4) for z = (rho-1)/rho, rho = 1/2 + i gamma", ok)

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
    half_int = sum(
        F(m) / (g * g + F(1, 4)) * (2 - 2 * cheb(x, n)) / (2 - 2 * x)
        for x, m, g in xs)
    ok = ok and lam(n) == half_int
    t_n = lam(n + 1) + lam(n - 1) - 2 * lam(n)
    sigma_hat = sum(2 * (F(m) / (g * g + F(1, 4))) * cheb(x, n) for x, m, g in xs)
    ok = ok and t_n == sigma_hat
sigma_mass = sum(2 * (F(m) / (g * g + F(1, 4))) for x, m, g in xs)
ok = ok and sigma_mass == 2 * lam(1)
ok = ok and sigma_mass == lam(0 + 1) + lam(0 - 1) - 2 * lam(0)
check("TH3 forced-measure dictionary exact on the synthetic multiset {(1,1),(3/2,2),(7,1)}: w = m/(gamma^2+1/4) = 2m(1-cos theta); lambda_n = (1/2) int |D_n|^2 d sigma_xi and t_n = sigma_xi_hat(n) for n = 0..10; sigma_xi(T) = t_0 = 2 lambda_1", ok)

# ===========================================================================
# Exact linear algebra over Z / Q
# ===========================================================================
MJ = [[1, 0, -1, 1], [0, 1, -1, 0], [1, 0, 0, 0], [0, 1, -1, 1]]

def detZ(M):
    n = len(M)
    s = 0
    for p in itertools.permutations(range(n)):
        inv = sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])
        term = (-1) ** inv
        for i in range(n):
            term *= M[i][p[i]]
        s += term
    return s

def charpoly(M):
    # Faddeev-LeVerrier; returns monic coefficient list [1, c1, ..., cn]
    n = len(M)
    Mf = [[F(x) for x in row] for row in M]
    A = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    coeffs = [F(1)]
    for k in range(1, n + 1):
        A = [[sum(Mf[i][t] * A[t][j] for t in range(n)) for j in range(n)]
             for i in range(n)]
        ck = -sum(A[i][i] for i in range(n)) / k
        coeffs.append(ck)
        for i in range(n):
            A[i][i] += ck
    return coeffs

def polymul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r

def polyeval(p, x):
    v = 0
    for c in p:
        v = v * x + c
    return v

# ===========================================================================
# TH4: M_J characteristic data
# ===========================================================================
P_MJ = [1, -3, 4, -2, 1]                     # x^4 - 3x^3 + 4x^2 - 2x + 1
# Phi_5(x-1) by exact polynomial substitution: sum_{k=0..4} (x-1)^k
xm1 = [1, -1]
acc = [0, 0, 0, 0, 1]
powr = [1]
for k in range(1, 5):
    powr = polymul(powr, xm1)
    acc = [a + b for a, b in zip(acc, [0] * (4 - k) + powr)]
cp = charpoly(MJ)
ok = (cp == [F(x) for x in P_MJ])
ok = ok and (acc == P_MJ)                    # Phi_5(x-1) expansion
ok = ok and detZ(MJ) == 1
ok = ok and sum(MJ[i][i] for i in range(4)) == 3
D2 = [[(2 if i == j else 0) - MJ[i][j] for j in range(4)] for i in range(4)]
ok = ok and detZ(D2) == 5 and polyeval(P_MJ, 2) == 5
ok = ok and polyeval(P_MJ, 1) == 1 and polyeval(P_MJ, -1) == 11
check("TH4 M_J characteristic data exact: charpoly(M_J) = Phi_5(x-1) = x^4-3x^3+4x^2-2x+1 for the pinned step matrix; det = 1, tr = 3, det(2I-M_J) = 5 (CODEC-TR4 cross-tie), p(1) = 1, p(-1) = 11", ok)

# ===========================================================================
# TH5: modulus alternatives phi and phi^-1, exact in Z[zeta_5] and Z[phi]
# ===========================================================================
# Z[zeta_5] as tuples over basis (1, z, z^2, z^3), z^4 = -1-z-z^2-z^3.
def z5mul(a, b):
    c = [0] * 7
    for i in range(4):
        for j in range(4):
            c[i + j] += a[i] * b[j]
    for d in range(6, 3, -1):
        k = c[d]
        if k:
            c[d] = 0
            for e in range(d - 4, d):
                c[e] -= k
    return tuple(c[:4])

def z5add(a, b): return tuple(x + y for x, y in zip(a, b))
def z5sc(a, s): return tuple(s * x for x in a)

Z5 = (0, 1, 0, 0)
def z5pow(a, n):
    r = (1, 0, 0, 0)
    for _ in range(n):
        r = z5mul(r, a)
    return r

alpha = z5add(z5pow(Z5, 1), z5pow(Z5, 4))
beta = z5add(z5pow(Z5, 2), z5pow(Z5, 3))
UNIT = (1, 0, 0, 0)
ok = z5add(z5add(z5mul(alpha, alpha), alpha), z5sc(UNIT, -1)) == (0, 0, 0, 0)
ok = ok and z5add(z5add(z5mul(beta, beta), beta), z5sc(UNIT, -1)) == (0, 0, 0, 0)
ok = ok and z5add(alpha, beta) == z5sc(UNIT, -1)
ok = ok and z5mul(alpha, beta) == z5sc(UNIT, -1)
# |1+z^a|^2 = (1+z^a)(1+z^(5-a)) = 2 + (z^a + z^(5-a))
for a, target in ((1, alpha), (4, alpha), (2, beta), (3, beta)):
    prod = z5mul(z5add(UNIT, z5pow(Z5, a)), z5add(UNIT, z5pow(Z5, 5 - a)))
    ok = ok and prod == z5add(z5sc(UNIT, 2), target)
# sum 3 and product 1 of the two modulus-squares; roots of y^2 - 3y + 1
ma, mb = z5add(z5sc(UNIT, 2), alpha), z5add(z5sc(UNIT, 2), beta)
ok = ok and z5add(ma, mb) == z5sc(UNIT, 3) and z5mul(ma, mb) == UNIT
ok = ok and polyeval([1, -3, 1], 1) == -1          # y = 1 is NOT a root
# (y^2-3y+1) under y = 1+u is u^2 - u - 1: the golden pair phi^2, phi^-2
yp1 = [1, 1]                                        # u + 1
comp = polymul(yp1, yp1)                            # (u+1)^2
comp = [comp[0], comp[1] - 3, comp[2] - 3 + 1]      # -3(u+1) + 1
ok = ok and comp == [1, -1, -1]
check("TH5 modulus alternatives exact in Z[zeta_5]: alpha, beta satisfy y^2+y-1 = 0 with alpha+beta = -1, alpha beta = -1; |1+z^a|^2 = 2+alpha (a in {1,4}) or 2+beta (a in {2,3}); the modulus-squares are the roots of y^2-3y+1 (sum 3, product 1) = phi^2 and phi^-2 under y = 1+u (u^2-u-1); y = 1 gives -1 != 0: no eigenvalue of M_J has modulus 1", ok)

# ===========================================================================
# TH6: cyclotomic exclusion, proof-first
# ===========================================================================
# No rational root: a rational root of the monic integer p divides p(0)=1,
# so it is +-1; p(1) = 1 != 0, p(-1) = 11 != 0 (TH4). By Gauss's lemma,
# a quadratic split over Q would be
# p = (x^2+ax+b)(x^2+cx+d) over Z with bd = 1. Hence (b,d) is (1,1) or
# (-1,-1). Since a+c = -3, the linear coefficient ad+bc would then be
# -3 or 3, never the required -2. No coefficient search is used.
ok = True
constant_cases = [(b, d) for b in (-1, 1) for d in (-1, 1) if b * d == 1]
ok = ok and constant_cases == [(-1, -1), (1, 1)]
ok = ok and all(b * (-3) != -2 for b, d in constant_cases)
# Euler phi enumeration: {m <= 32 : phi(m) = 4} = {5, 8, 10, 12}
def eulerphi(m):
    return sum(1 for k in range(1, m + 1) if gcd(k, m) == 1)
ok = ok and [m for m in range(1, 33) if eulerphi(m) == 4] == [5, 8, 10, 12]
# p differs coefficientwise from every degree-4 cyclotomic polynomial
PHI5 = [1, 1, 1, 1, 1]
PHI8 = [1, 0, 0, 0, 1]
PHI10 = [1, -1, 1, -1, 1]
PHI12 = [1, 0, -1, 0, 1]
ok = ok and all(P_MJ != q for q in (PHI5, PHI8, PHI10, PHI12))
check("TH6 cyclotomic exclusion proof-first: p has no rational root; Gauss's lemma leaves exactly the constant cases (b,d) = (1,1),(-1,-1), where a+c = -3 forces linear coefficient -3 or 3, not -2, so p is irreducible; {m : eulerphi(m) = 4} = {5,8,10,12} on m <= 32 (bound eulerphi(m) >= sqrt(m/2), imported); p differs from Phi_5, Phi_8, Phi_10, Phi_12: no eigenvalue of M_J is a root of unity", ok)

# ===========================================================================
# TH7: exterior-square non-escape
# ===========================================================================
pairs = list(itertools.combinations(range(4), 2))
L2 = [[MJ[i][k] * MJ[j][l] - MJ[i][l] * MJ[j][k] for (k, l) in pairs]
      for (i, j) in pairs]
cp6 = charpoly(L2)
target = polymul([1, -3, 1], PHI10)
ok = (cp6 == [F(x) for x in target])
ok = ok and target == [1, -4, 5, -5, 5, -4, 1]
# and the acting object is cyclotomic-free: charpoly(M_J^T) = charpoly(M_J)
MJT = [[MJ[j][i] for j in range(4)] for i in range(4)]
ok = ok and charpoly(MJT) == [F(x) for x in P_MJ]
check("TH7 exterior-square non-escape exact: charpoly(Lambda^2 M_J) = (y^2-3y+1) Phi_10(y) = y^6-4y^5+5y^4-5y^3+5y^2-4y+1, so the primitive tenth roots live in Lambda^2 M_J only; the Koopman character action runs through M_J^T on Z^4 with charpoly p, cyclotomic-free by TH6", ok)

# ===========================================================================
# Directed interval machinery (Fractions only; no float anywhere)
# ===========================================================================
def atan_bracket(x, terms):
    # 0 < x <= 1/2 rational; alternating series with strictly decreasing
    # terms; returns exact [lo, hi] containing arctan(x) plus the exact
    # monotonicity flag (bracket validity is a checked statement, not an
    # assumption).
    s = F(0)
    prev_t = None
    penult = None
    mono = True
    for k in range(terms):
        t = x ** (2 * k + 1) / (2 * k + 1)
        mono = mono and (prev_t is None or t < prev_t)
        prev_t = t
        penult = s
        s = s + t if k % 2 == 0 else s - t
    lo, hi = (s, penult) if s < penult else (penult, s)
    return lo, hi, mono

def ln_bracket(r, terms):
    # r rational > 1; artanh series, positive terms, geometric tail bound.
    x = (r - 1) / (r + 1)
    s = F(0)
    for k in range(terms):
        s += x ** (2 * k + 1) / (2 * k + 1)
    tail = x ** (2 * terms + 1) / ((2 * terms + 1) * (1 - x * x))
    return 2 * s, 2 * (s + tail)

def decstr(fr, digits, direction):
    # directed decimal string of a positive Fraction; floor for 'lo',
    # ceiling for 'hi'; deterministic, no float.
    scaled = fr * 10 ** digits
    n = scaled.numerator // scaled.denominator
    if direction == "hi" and scaled != n:
        n += 1
    s = str(n).rjust(digits + 1, "0")
    return s[:-digits] + "." + s[-digits:]

# ===========================================================================
# TH8: directed bracket for theta at gamma = 1
# ===========================================================================
a_lo, a_hi, a_mono = atan_bracket(F(1, 2), 40)
th_lo, th_hi = 2 * a_lo, 2 * a_hi
ok = a_mono and (0 < th_lo < th_hi) and (th_hi - th_lo < F(1, 10 ** 20))
check("TH8 directed bracket for theta at synthetic gamma = 1: exact alternating-series enclosure of 2 arctan(1/2), width < 10^-20", ok)
print("TH8 enclosure theta in [%s, %s]" %
      (decstr(th_lo, 24, "lo"), decstr(th_hi, 24, "hi")))

# ===========================================================================
# TH9: directed bracket for the accumulation leading term at eps = 1/1000
# ===========================================================================
a5_lo, a5_hi, a5_mono = atan_bracket(F(1, 5), 16)
a239_lo, a239_hi, a239_mono = atan_bracket(F(1, 239), 6)
pi_lo = 16 * a5_lo - 4 * a239_hi
pi_hi = 16 * a5_hi - 4 * a239_lo
ok = a5_mono and a239_mono
ok = ok and (F(3) < pi_lo < pi_hi < F(4)) and (pi_hi - pi_lo < F(1, 10 ** 20))
ln2_lo, ln2_hi = ln_bracket(F(2), 40)
ln5_lo, ln5_hi = ln_bracket(F(5), 80)
ln10_lo, ln10_hi = ln2_lo + ln5_lo, ln2_hi + ln5_hi
lnpi_lo = ln_bracket(pi_lo, 80)[0]
lnpi_hi = ln_bracket(pi_hi, 80)[1]
eps = F(1, 1000)
inner_lo = 3 * ln10_lo - ln2_hi - lnpi_hi + 1
inner_hi = 3 * ln10_hi - ln2_lo - lnpi_lo + 1
ok = ok and 0 < inner_lo < inner_hi
L_lo = eps * inner_lo / pi_hi
L_hi = eps * inner_hi / pi_lo
ok = ok and (0 < L_lo < L_hi) and (L_hi - L_lo < F(1, 10 ** 20))
check("TH9 directed bracket for the accumulation leading term at eps = 1/1000: L = (eps/pi)(log(1/(2 pi eps)) + 1) enclosed by Machin pi and artanh log brackets with geometric tails, width < 10^-20", ok)
print("TH9 enclosure pi in [%s, %s]" %
      (decstr(pi_lo, 24, "lo"), decstr(pi_hi, 24, "hi")))
print("TH9 enclosure L(1/1000) in [%s, %s]" %
      (decstr(L_lo, 24, "lo"), decstr(L_hi, 24, "hi")))

# ===========================================================================
# X1: exploratory finite witnesses (exact, labeled, NOT a gate)
# ===========================================================================
def mmul(P, Q):
    n = len(P)
    return [[sum(P[i][t] * Q[t][j] for t in range(n)) for j in range(n)]
            for i in range(n)]

A2 = [[2, 1], [1, 1]]
P = [[1, 0], [0, 1]]
ok = True
prev_tr = 2
for k in range(1, 301):
    P = mmul(P, A2)
    tr = P[0][0] + P[1][1]
    ok = ok and (P[0][0] - 1) * (P[1][1] - 1) - P[0][1] * P[1][0] == 2 - tr != 0
    ok = ok and tr > prev_tr
    prev_tr = tr
Q = [[int(i == j) for j in range(4)] for i in range(4)]
for k in range(1, 121):
    Q = mmul(Q, MJ)
    QI = [[Q[i][j] - int(i == j) for j in range(4)] for i in range(4)]
    ok = ok and detZ(QI) != 0
check("X1 EXPLORATORY WITNESS (finite, exact, not a theorem gate): det(A^k - I) = 2 - tr(A^k) != 0 for the cat map, k = 1..300, and det(M_J^k - I) != 0 for k = 1..120; the all-k, all-d theorem follows from the no-root-of-unity carrier hypothesis, while TH5/TH6 place M_J in that class", ok, theorem_gate=False)

print("FAILED GATES: " + (", ".join(FAILED_GATES) if FAILED_GATES else "none"))
print("FAILED WITNESSES: " + (", ".join(FAILED_WITNESSES) if FAILED_WITNESSES else "none"))
if not FAILED_GATES and not FAILED_WITNESSES:
    print("VERDICT: PASS P-J-LI-TORAL-HAAR-1 (9/9 theorem gates; X1 witness pass)")
    raise SystemExit(0)
print("VERDICT: FAIL P-J-LI-TORAL-HAAR-1")
raise SystemExit(1)
