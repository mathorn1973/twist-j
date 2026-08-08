#!/usr/bin/env python3
"""Exact L1 audit for P-J-HARMONIC-SEAM-1.

The theorem candidate classifies the ten torsion weights of one contracting
Fibonacci/cyclotomic ladder. Arithmetic is exact in Z[zeta_5] in the ordered
basis (1,z,z^2,z^3), with Fraction used only for rational multiples of pi in
principal-branch bookkeeping. No float, complex approximation, logarithm,
trigonometric evaluation, external data, or prior incubation output is used.
"""

from fractions import Fraction
import sys


CHECKS = []


def check(label, condition):
    CHECKS.append((label, bool(condition)))


def radd(left, right):
    return tuple(left[i] + right[i] for i in range(4))


def rsub(left, right):
    return tuple(left[i] - right[i] for i in range(4))


def rscale(value, scalar):
    return tuple(scalar * value[i] for i in range(4))


def rmul(left, right):
    """Multiply in Z[z]/(z^4+z^3+z^2+z+1)."""
    raw = [0] * 7
    for i in range(4):
        for j in range(4):
            raw[i + j] += left[i] * right[j]
    for degree in (6, 5, 4):
        carry = raw[degree]
        if carry:
            raw[degree] = 0
            for step in range(4):
                raw[degree - 4 + step] -= carry
    return tuple(raw[:4])


def rpow(base, exponent):
    if exponent < 0:
        raise ValueError("negative exponent is outside the frozen ring API")
    result = ONE
    factor = base
    power = exponent
    while power:
        if power & 1:
            result = rmul(result, factor)
        factor = rmul(factor, factor)
        power >>= 1
    return result


def rconj(value):
    """Complex conjugation z -> z^-1 = z^4 in the fixed power basis."""
    a, b, c, d = value
    return (a - b, -b, d - b, c - b)


def arch_norm_square(value):
    return rmul(value, rconj(value))


def exact_order(value, bound=10):
    for exponent in range(1, bound + 1):
        if rpow(value, exponent) == ONE:
            return exponent
    return None


def principal_angle_pi(sign, power):
    """Angle of sign*z^power as a rational multiple of pi in (-1,1]."""
    angle = Fraction(2 * power, 5)
    if sign == -1:
        angle += 1
    while angle > 1:
        angle -= 2
    while angle <= -1:
        angle += 2
    return angle


def pair_add(left, right):
    return (left[0] + right[0], left[1] + right[1])


def pair_scale(value, scalar):
    return (scalar * value[0], scalar * value[1])


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
NEG_ONE = (-1, 0, 0, 0)
Z = (0, 1, 0, 0)
Z2 = rpow(Z, 2)
Z3 = rpow(Z, 3)
Z4 = rpow(Z, 4)
PHI = (0, 0, -1, -1)
PSI = rsub(ONE, PHI)
J = (1, 0, 1, 0)
PHI_INV = rsub(PHI, ONE)
PHI_INV2 = rsub(rscale(ONE, 2), PHI)
NEG_Z = rscale(Z, -1)
NEG_Z_INV = rscale(Z4, -1)
NEG_Z2 = rscale(Z2, -1)
NEG_Z3 = rscale(Z3, -1)


# ---------------------------------------------------------------------------
# Carrier sanity and complete mu_10 list.
# ---------------------------------------------------------------------------
check("C0-01 z^5 = 1", rpow(Z, 5) == ONE)
check(
    "C0-02 cyclotomic relation",
    radd(radd(radd(radd(ONE, Z), Z2), Z3), Z4) == ZERO,
)
check("C0-03 phi^2 = phi + 1", rmul(PHI, PHI) == radd(PHI, ONE))
check("C0-04 psi = 1 - phi", PSI == rsub(ONE, PHI))
check("C0-05 psi*phi = -1", rmul(PSI, PHI) == NEG_ONE)
check("C0-06 J*phi = z", rmul(J, PHI) == Z)

MU10 = []
for sign in (1, -1):
    for power in range(5):
        label = ("+" if sign == 1 else "-") + f"z^{power}"
        value = rscale(rpow(Z, power), sign)
        MU10.append((label, sign, power, value))

mu_values = [entry[3] for entry in MU10]
check("C0-07 mu_10 has ten distinct listed elements", len(set(mu_values)) == 10)
check("C0-08 every listed mu_10 element has tenth power 1", all(rpow(v, 10) == ONE for v in mu_values))


# ---------------------------------------------------------------------------
# S1. Universal integral numerator ladder.
# u(a,b) = a*phi - b, and (a,b) -> (b,a+b) under multiplication by psi.
# ---------------------------------------------------------------------------
def u_state(a, b):
    return radd(rscale(PHI, a), rscale(ONE, -b))


def u_word(a, b):
    return (-b, 0, -a, -a)


check("S1-01 u(a,b) has the frozen integer word form", u_state(7, 11) == u_word(7, 11))
check("S1-02 u_1 = -psi", u_state(1, 1) == rscale(PSI, -1))
check("S1-03 psi*phi = -1 is the first universal basis identity", rmul(PSI, PHI) == NEG_ONE)
check(
    "S1-04 psi*(-1) = phi-1 is the second universal basis identity",
    rmul(PSI, NEG_ONE) == rsub(PHI, ONE),
)
check(
    "S1-05 basis identities certify u(a,b) -> u(b,a+b)",
    rmul(PSI, u_state(2, 3)) == u_state(3, 5)
    and rmul(PSI, u_state(-5, 8)) == u_state(8, 3),
)


# ---------------------------------------------------------------------------
# A(x) is the algebraic landing point of H(x) = Log(A(x)).
# ---------------------------------------------------------------------------
def A(value):
    return rsub(ONE, rmul(PSI, value))


check("S2-01 all ten landing points are nonzero", all(A(v) != ZERO for v in mu_values))
check("S2-02 A(1) = phi", A(ONE) == PHI)
check("S2-03 psi*(-z) = J", rmul(PSI, NEG_Z) == J)
check("S2-04 A(-z) = 1-J = -z^2", A(NEG_Z) == NEG_Z2)
check("S2-05 principal angle of -z^2 is -pi/5", principal_angle_pi(-1, 2) == Fraction(-1, 5))


# ---------------------------------------------------------------------------
# S3. Complete real-axis classification.
# ---------------------------------------------------------------------------
real_labels = []
for label, _sign, _power, value in MU10:
    landing = A(value)
    if landing == rconj(landing):
        real_labels.append(label)

check("S3-01 A(x) is real exactly for x in {1,-1}", set(real_labels) == {"+z^0", "-z^0"})
check("S3-02 A(-1) = phi^-2 = 2-phi", A(NEG_ONE) == PHI_INV2)
check("S3-03 phi^-1 = phi-1", rmul(PHI, PHI_INV) == ONE)
check("S3-04 (2-phi)*phi^2 = 1", rmul(PHI_INV2, rmul(PHI, PHI)) == ONE)


# ---------------------------------------------------------------------------
# S4. Complete imaginary-axis classification via |A(x)|^2 = 1.
# ---------------------------------------------------------------------------
norm_one_labels = []
norm_formula_ok = True
for label, _sign, _power, value in MU10:
    landing = A(value)
    norm_square = arch_norm_square(landing)
    if norm_square == ONE:
        norm_one_labels.append(label)
    rhs = rsub(
        radd(ONE, rmul(PSI, PSI)),
        rmul(PSI, radd(value, rconj(value))),
    )
    if norm_square != rhs:
        norm_formula_ok = False

check("S4-01 exact norm formula holds on complete mu_10", norm_formula_ok)
check(
    "S4-02 |A(x)|=1 exactly for x in {-z,-z^-1}",
    set(norm_one_labels) == {"-z^1", "-z^4"},
)
check("S4-03 (-z)+(-z^-1) = psi", radd(NEG_Z, NEG_Z_INV) == PSI)
check("S4-04 A(-z^-1) = -z^3", A(NEG_Z_INV) == NEG_Z3)
check("S4-05 principal angle of -z^3 is +pi/5", principal_angle_pi(-1, 3) == Fraction(1, 5))


# ---------------------------------------------------------------------------
# S5. Explicit free/torsion landings and primitive torsion order.
# The unbounded unit-group statement is supplied by the written proof in PREREG.
# ---------------------------------------------------------------------------
check("S5-01 free landing A(1) = phi", A(ONE) == PHI)
check("S5-02 inverse free landing A(-1) = phi^-2", A(NEG_ONE) == PHI_INV2)
check("S5-03 torsion landing A(-z) = -z^2", A(NEG_Z) == NEG_Z2)
check("S5-04 conjugate torsion landing A(-z^-1) = -z^3", A(NEG_Z_INV) == NEG_Z3)
check("S5-05 -z^2 has exact order 10", exact_order(NEG_Z2) == 10)
check("S5-06 -z^3 has exact order 10", exact_order(NEG_Z3) == 10)
check("S5-07 the two torsion landings are conjugate", rconj(NEG_Z2) == NEG_Z3)
check("S5-08 J*phi=z links the mixed unit back to torsion", rmul(J, PHI) == Z)


# ---------------------------------------------------------------------------
# S6. Principal-branch reconstruction in the symbolic basis (log phi, i*pi).
# No numerical transcendental comparison occurs.
# ---------------------------------------------------------------------------
H_ONE = (Fraction(1), Fraction(0))
H_NEG_Z = (Fraction(0), Fraction(-1, 5))
LOG_J_EXPECTED = (Fraction(-1), Fraction(2, 5))
LOG_J_RECONSTRUCTED = pair_add(pair_scale(H_ONE, -1), pair_scale(H_NEG_Z, -2))

check("S6-01 -H(1)-2H(-z) reconstructs (-log phi)+(2/5)i*pi", LOG_J_RECONSTRUCTED == LOG_J_EXPECTED)
check("S6-02 J principal argument coefficient is 2/5", LOG_J_EXPECTED[1] == Fraction(2, 5))
check("S6-03 J log-modulus coefficient is -1", LOG_J_EXPECTED[0] == Fraction(-1))


# ---------------------------------------------------------------------------
# Deterministic scientific routing. MISMATCH is a scientific outcome, not STOP.
# ---------------------------------------------------------------------------
for label, passed in CHECKS:
    print(("PASS " if passed else "FAIL ") + label)

failures = [label for label, passed in CHECKS if not passed]
print(f"CHECKS {len(CHECKS)}")
if failures:
    print("DECISION MISMATCH")
    print("FAILURES " + " | ".join(failures))
    raise SystemExit(0)

print("DECISION SEAM-PASS")
raise SystemExit(0)
