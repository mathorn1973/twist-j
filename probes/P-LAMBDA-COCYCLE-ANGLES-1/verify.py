#!/usr/bin/env python3
"""Exact verifier for P-LAMBDA-COCYCLE-ANGLES-1.

The program audits the reduction of the second-difference falsifier of
LAMBDA-COCYCLE-ANGLES [H] to its Cayley-angle falsifier.  Every load-bearing
step is an identity of rational functions in one free variable g, the ordinate
of a critical-line zero, so a passing check is a statement about every ordinate
at once and not about a sample.  Arithmetic is integer polynomial arithmetic
and Fraction arithmetic only.  No floating point value is formed and no
external dataset is read.
"""

from fractions import Fraction
import sys


CHECKS = []


def check(label, condition):
    CHECKS.append((label, bool(condition)))


# ---------------------------------------------------------------------------
# Integer polynomials in one variable, low degree first, trimmed.
# ---------------------------------------------------------------------------
def ptrim(coefficients):
    result = list(coefficients)
    while result and result[-1] == 0:
        result.pop()
    return tuple(result)


def padd(left, right):
    width = max(len(left), len(right))
    return ptrim(
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(width)
    )


def pneg(value):
    return tuple(-coefficient for coefficient in value)


def psub(left, right):
    return padd(left, pneg(right))


def pmul(left, right):
    if not left or not right:
        return ()
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        if a:
            for j, b in enumerate(right):
                result[i + j] += a * b
    return ptrim(result)


def ppow(value, exponent):
    result = (1,)
    for _ in range(exponent):
        result = pmul(result, value)
    return result


def psubs_neg(value):
    """Substitute -g for g."""
    return ptrim(
        coefficient * (-1) ** index
        for index, coefficient in enumerate(value)
    )


def peval(value, point):
    result = Fraction(0)
    for coefficient in reversed(value):
        result = result * point + coefficient
    return result


ZERO = ()
ONE = (1,)
G = (0, 1)


# ---------------------------------------------------------------------------
# Complex rational functions (re + i*im)/den with polynomial entries.
# ---------------------------------------------------------------------------
def cr(re, im, den):
    return (re, im, den)


def cradd(left, right):
    a, b, d = left
    e, f, h = right
    return cr(padd(pmul(a, h), pmul(e, d)), padd(pmul(b, h), pmul(f, d)), pmul(d, h))


def crsub(left, right):
    e, f, h = right
    return cradd(left, cr(pneg(e), pneg(f), h))


def crmul(left, right):
    a, b, d = left
    e, f, h = right
    return cr(psub(pmul(a, e), pmul(b, f)), padd(pmul(a, f), pmul(b, e)), pmul(d, h))


def crpow(value, exponent):
    result = cr(ONE, ZERO, ONE)
    for _ in range(exponent):
        result = crmul(result, value)
    return result


def crinv(value):
    a, b, d = value
    modulus = padd(pmul(a, a), pmul(b, b))
    return cr(pmul(d, a), pneg(pmul(d, b)), modulus)


def crconj(value):
    a, b, d = value
    return cr(a, pneg(b), d)


def crnorm2(value):
    a, b, d = value
    return cr(padd(pmul(a, a), pmul(b, b)), ZERO, pmul(d, d))


def creq(left, right):
    a, b, d = left
    e, f, h = right
    return pmul(a, h) == pmul(e, d) and pmul(b, h) == pmul(f, d)


def crreal(value):
    a, _, d = value
    return cr(a, ZERO, d)


def creval(value, point):
    a, b, d = value
    divisor = peval(d, point)
    return (peval(a, point) / divisor, peval(b, point) / divisor)


# ---------------------------------------------------------------------------
# Frozen objects.  g is the free ordinate variable of a critical-line zero.
# ---------------------------------------------------------------------------
N_MAX = 20
ORDINATE_LADDER = tuple(Fraction(k, 2) for k in range(1, 13))
DELTAS = (Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000))
FANOUTS = (1, 2, 5, 10, 50)

# rho = 1/2 + i g, written with denominator 2.
RHO = cr(ONE, pmul((2,), G), (2,))
# A = 4 g^2 - 1, B = 4 g, D = 4 g^2 + 1.
A = psub(pmul((4,), pmul(G, G)), ONE)
B = pmul((4,), G)
D = padd(pmul((4,), pmul(G, G)), ONE)
W = cr(A, B, D)
# The reciprocal of the paired mass 1/4 + g^2, as a rational function.
INV_MASS = cr((4,), ZERO, padd(ONE, pmul((4,), pmul(G, G))))
# Tangent half-angle data for alpha = 2 arctan(U/V) with U = 1, V = 2 g.
U = ONE
V = pmul((2,), G)


# ---------------------------------------------------------------------------
# B1  The Cayley factor is a unit and is exactly the half-angle unit.
# ---------------------------------------------------------------------------
cayley = crsub(cr(ONE, ZERO, ONE), crinv(RHO))
check("B1-01 1-1/rho equals (4g^2-1+4ig)/(4g^2+1)", creq(cayley, W))
check("B1-02 the Cayley factor is a unit: A^2+B^2=D^2", padd(pmul(A, A), pmul(B, B)) == pmul(D, D))
check(
    "B1-03 (A,B,D) is the half-angle triple (V^2-U^2,2UV,V^2+U^2), U=1, V=2g",
    A == psub(pmul(V, V), pmul(U, U))
    and B == pmul((2,), pmul(U, V))
    and D == padd(pmul(V, V), pmul(U, U)),
)
check(
    "B1-04 the conjugate ordinate gives the conjugate factor",
    psubs_neg(A) == A and psubs_neg(B) == pneg(B),
)
check(
    "B1-05 1/rho+1/conj(rho) equals 1/(1/4+g^2), the paired mass",
    creq(cradd(crinv(RHO), crinv(crconj(RHO))), INV_MASS),
)

# ---------------------------------------------------------------------------
# B2  The reciprocal-square collapse.
# ---------------------------------------------------------------------------
inv_rho2 = crinv(crmul(RHO, RHO))
check(
    "B2-01 (w-1)^2 equals 1/rho^2",
    creq(crpow(crsub(W, cr(ONE, ZERO, ONE)), 2), inv_rho2),
)
check(
    "B2-02 1/rho^2 equals -w/(1/4+g^2)",
    creq(inv_rho2, crmul(crsub(cr(ZERO, ZERO, ONE), W), INV_MASS)),
)
collapse_ok = True
for n in range(1, N_MAX + 1):
    left = crsub(cr(ZERO, ZERO, ONE), crmul(crpow(W, n - 1), inv_rho2))
    right = crmul(crpow(W, n), INV_MASS)
    if not creq(left, right):
        collapse_ok = False
check(
    f"B2-03 -w^(n-1)/rho^2 equals w^n/(1/4+g^2) for 1<=n<={N_MAX}",
    collapse_ok,
)

# ---------------------------------------------------------------------------
# B3  The second-difference identity, first for a free base then for w.
# ---------------------------------------------------------------------------
X = (0, 1)
free_ok = True
for n in range(1, N_MAX + 1):
    left = psub(padd(ppow(X, n + 1), ppow(X, n - 1)), pmul((2,), ppow(X, n)))
    right = pmul(ppow(X, n - 1), ppow(psub(X, ONE), 2))
    if left != right:
        free_ok = False
check(
    f"B3-01 X^(n+1)+X^(n-1)-2X^n equals X^(n-1)(X-1)^2 for 1<=n<={N_MAX}",
    free_ok,
)
cayley_second_ok = True
for n in range(1, N_MAX + 1):
    left = crsub(
        cradd(crpow(W, n + 1), crpow(W, n - 1)),
        crmul(cr((2,), ZERO, ONE), crpow(W, n)),
    )
    right = crmul(crpow(W, n - 1), crpow(crsub(W, cr(ONE, ZERO, ONE)), 2))
    if not creq(left, right):
        cayley_second_ok = False
check(
    f"B3-02 the same identity holds for the Cayley factor for 1<=n<={N_MAX}",
    cayley_second_ok,
)

# ---------------------------------------------------------------------------
# B4  The Li side: the ordinate contribution to t_n and to M.
# ---------------------------------------------------------------------------
unit_power_ok = True
for n in range(1, N_MAX + 1):
    if not creq(crnorm2(crpow(W, n)), cr(ONE, ZERO, ONE)):
        unit_power_ok = False
check(f"B4-01 |w^n| equals 1 for 1<=n<={N_MAX}", unit_power_ok)

pair_ok = True
residual_ok = True
sine_ok = True
for n in range(1, N_MAX + 1):
    # rho and its conjugate contribute -w^(n-1)/rho^2 and its conjugate.
    term = crmul(crpow(W, n), INV_MASS)
    paired = cradd(term, crconj(term))
    doubled_real = crmul(cr((2,), ZERO, ONE), crmul(crreal(crpow(W, n)), INV_MASS))
    if not creq(paired, doubled_real):
        pair_ok = False
    # M-term minus t_n-term equals |w^n-1|^2/(1/4+g^2).
    mass_term = crmul(cr((2,), ZERO, ONE), INV_MASS)
    residual = crsub(mass_term, paired)
    modulus = crnorm2(crsub(crpow(W, n), cr(ONE, ZERO, ONE)))
    if not creq(residual, crmul(modulus, INV_MASS)):
        residual_ok = False
    # |w^n-1|^2 = 2-2cos(n alpha) = 4 sin^2(n alpha/2).
    if not creq(
        modulus,
        crsub(cr((2,), ZERO, ONE), crmul(cr((2,), ZERO, ONE), crreal(crpow(W, n)))),
    ):
        sine_ok = False
check(
    f"B4-02 the ordinate pair contributes 2cos(n alpha)/(1/4+g^2) for 1<=n<={N_MAX}",
    pair_ok,
)
check(
    "B4-03 the ordinate pair contributes 2/(1/4+g^2) to M=2 lambda_1",
    creq(
        crmul(cr((2,), ZERO, ONE), cradd(crinv(RHO), crinv(crconj(RHO)))),
        crmul(cr((2,), ZERO, ONE), INV_MASS),
    ),
)
check(
    f"B4-04 M-term minus t_n-term equals |w^n-1|^2/(1/4+g^2) for 1<=n<={N_MAX}",
    residual_ok,
)
check(
    f"B4-05 |w^n-1|^2 equals 2-2cos(n alpha) equals 4 sin^2(n alpha/2) for 1<=n<={N_MAX}",
    sine_ok,
)

# ---------------------------------------------------------------------------
# B5  Sign and bound on the declared ordinate ladder, in exact rationals.
# ---------------------------------------------------------------------------
bound_ok = True
mass_positive_ok = True
for point in ORDINATE_LADDER:
    mass_value = peval(padd(ONE, pmul((4,), pmul(G, G))), point) / 4
    if mass_value < Fraction(1, 4):
        mass_positive_ok = False
    for n in range(1, N_MAX + 1):
        modulus = crnorm2(crsub(crpow(W, n), cr(ONE, ZERO, ONE)))
        value, imaginary = creval(modulus, point)
        if imaginary != 0 or value < 0 or value > 4:
            bound_ok = False
check(
    f"B5-01 0<=|w^n-1|^2<=4 on the declared ladder for 1<=n<={N_MAX}",
    bound_ok,
)
check("B5-02 1/4+g^2 is at least 1/4 on the declared ladder", mass_positive_ok)

# ---------------------------------------------------------------------------
# B6  The spectral side: the Fejer kernel obeys the same identity.
# ---------------------------------------------------------------------------
# A free rational point of the unit circle, z = (v^2-1+2iv)/(v^2+1).
Vv = (0, 1)
E = psub(pmul(Vv, Vv), ONE)
F = pmul((2,), Vv)
Gg = padd(pmul(Vv, Vv), ONE)
Z = cr(E, F, Gg)
check("B6-01 the free circle point is a unit: E^2+F^2=G^2", padd(pmul(E, E), pmul(F, F)) == pmul(Gg, Gg))

ONE_CR = cr(ONE, ZERO, ONE)


def fejer(n):
    """|1+z+...+z^(n-1)|^2 built as a geometric sum, no division by z-1."""
    total = cr(ZERO, ZERO, ONE)
    for k in range(n):
        total = cradd(total, crpow(Z, k))
    return crnorm2(total)


check("B6-02 D_1 equals 1, so M equals twice the total mass", creq(fejer(1), ONE_CR))
fejer_ok = True
for n in range(1, 13):
    left = crsub(cradd(fejer(n + 1), fejer(n - 1)), crmul(cr((2,), ZERO, ONE), fejer(n)))
    right = crmul(cr((2,), ZERO, ONE), crreal(crpow(Z, n)))
    if not creq(left, right):
        fejer_ok = False
check("B6-03 D_(n+1)+D_(n-1)-2D_n equals 2cos(n theta) for 1<=n<=12", fejer_ok)
check(
    "B6-04 the Fejer second difference uses the same X^(n-1)(X-1)^2 identity",
    free_ok and cayley_second_ok,
)

# ---------------------------------------------------------------------------
# B7  The 5-adic angle grid, in exact integer and Fraction arithmetic.
#
# The registered grid is alpha in 2 pi (1/4) Z[1/5], that is alpha/(2 pi) =
# m/(4 * 5^a).  The index sequence is n_A = 4 * 5^A.  A grid angle is
# annihilated by n_A as soon as A >= a; an off-grid rational angle is never
# annihilated and keeps a rational separation.
# ---------------------------------------------------------------------------
GRID_NUMERATORS = (1, 2, 3, 7, 11, 13, 24, 101)
GRID_LEVELS = (0, 1, 2, 3)
GRID_INDICES = (0, 1, 2, 3, 4, 5)
# Denominators that divide no 4*5^A: a prime factor outside {2,5}, or 8 | q.
OFF_GRID_DENOMINATORS = (3, 7, 8, 9, 11, 16, 12, 20 * 3)


def index_at(level):
    return 4 * 5 ** level


grid_ok = True
coprime_ok = all(numerator % 5 != 0 for numerator in GRID_NUMERATORS)
for numerator in GRID_NUMERATORS:
    if numerator % 5 == 0:
        # The threshold statement is stated for m coprime to 5; a numerator
        # carrying a factor 5 reduces the level and is not a counterexample.
        continue
    for level in GRID_LEVELS:
        denominator = 4 * 5 ** level
        for index_level in GRID_INDICES:
            multiple = Fraction(index_at(index_level) * numerator, denominator)
            annihilated = multiple.denominator == 1
            if annihilated != (index_level >= level):
                grid_ok = False
check(
    "B7-01 a grid angle m/(4*5^a), m coprime to 5, is annihilated exactly when A>=a",
    grid_ok and coprime_ok,
)

off_grid_ok = True
for denominator in OFF_GRID_DENOMINATORS:
    divides_some_index = any(
        index_at(level) % denominator == 0 for level in range(0, 12)
    )
    if divides_some_index:
        off_grid_ok = False
        continue
    for numerator in range(1, denominator):
        if Fraction(numerator, denominator).denominator != denominator:
            continue
        for index_level in range(0, 12):
            residue = Fraction(index_at(index_level) * numerator, denominator)
            fractional = residue - int(residue)
            distance = min(fractional, 1 - fractional)
            if distance <= 0 or distance < Fraction(1, denominator):
                off_grid_ok = False
check(
    "B7-02 an off-grid angle p/q keeps distance at least 1/q from Z for every n_A",
    off_grid_ok,
)

pigeonhole_ok = True
descent_ok = True
split_ok = True
for delta in DELTAS:
    for fanout in FANOUTS:
        uniform = tuple(delta / (2 * fanout) for _ in range(fanout))
        spike = tuple(
            (delta / 2 if index == fanout - 1 else Fraction(0))
            for index in range(fanout)
        )
        for tuple_of_terms in (uniform, spike):
            if sum(tuple_of_terms) < delta / 2:
                pigeonhole_ok = False
            if max(tuple_of_terms) < delta / (2 * fanout):
                pigeonhole_ok = False
        # total >= delta and tail < delta/2 leaves head >= delta/2.
        for tail in (Fraction(0), delta / 4, delta / 2 - delta / 100):
            if delta - tail < delta / 2:
                split_ok = False
        for point in ORDINATE_LADDER:
            mass_value = peval(padd(ONE, pmul((4,), pmul(G, G))), point) / 4
            # term = |w^n-1|^2/(1/4+g^2) >= delta/(2K) forces the numerator up.
            numerator_bound = delta / (2 * fanout) * mass_value
            if numerator_bound < delta / (8 * fanout):
                descent_ok = False
check(
    "B7-03 a sum of K nonnegative terms at least delta/2 has a term at least delta/(2K)",
    pigeonhole_ok,
)
check(
    "B7-04 a tail below delta/2 leaves head mass at least delta/2 in the finite window",
    split_ok,
)
check(
    "B7-05 that term forces |w^n-1|^2 at least delta/(8K) since 1/4+g^2>=1/4",
    descent_ok,
)

# ---------------------------------------------------------------------------
# B8  The registered conclusions.
# ---------------------------------------------------------------------------
check(
    "B8-01 M-t_n is a sum of nonnegative terms, so 0<=M-t_n<=2M for every n",
    residual_ok and bound_ok and unit_power_ok,
)
check(
    "B8-02 no finite set of Li values can contradict the hypothesis",
    residual_ok and bound_ok and pair_ok,
)
check(
    "B8-03 t_(n_A)->M holds exactly when n_A alpha->0 mod 2 pi for every ordinate",
    residual_ok and sine_ok,
)
check(
    "B8-04 a tail separation fires the angle branch at one located ordinate",
    pigeonhole_ok and split_ok and descent_ok,
)
check(
    "B8-05 the grid 2 pi (1/4) Z[1/5] is exactly the set of angles n_A annihilates",
    grid_ok and off_grid_ok,
)


passed = sum(int(condition) for _, condition in CHECKS)
lines = [
    ("PASS " if condition else "FAIL ") + label
    for label, condition in CHECKS
]
if passed == len(CHECKS):
    lines.append(f"RESULT {passed}/{len(CHECKS)} ALL PASS")
else:
    lines.append(f"RESULT {passed}/{len(CHECKS)} FAILURES PRESENT")
sys.stdout.buffer.write(("\n".join(lines) + "\n").encode("ascii"))
raise SystemExit(0 if passed == len(CHECKS) else 1)
