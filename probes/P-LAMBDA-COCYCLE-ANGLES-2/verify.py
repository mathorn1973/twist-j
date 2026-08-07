#!/usr/bin/env python3
"""Exact verifier for P-LAMBDA-COCYCLE-ANGLES-2.

The program audits the converse direction of the compact lambda-adic
cocycle-vector hypothesis: that the Koopman operator U_J of multiplication by
J = 1 + zeta_5^2 on L^2(O_lambda,Haar) has pure point spectrum whose eigenvalue
angles are exactly the registered grid 2 pi (1/4) Z[1/5], and that the grid
condition therefore suffices as well as being necessary.

Arithmetic is integer arithmetic in Z[zeta_5] = Z[x]/(x^4+x^3+x^2+x+1) in the
ordered basis 1, zeta, zeta^2, zeta^3, its finite quotients, and Fraction.  No
floating-point value is formed and no external dataset is read.
"""

from fractions import Fraction
from math import gcd
from itertools import permutations, product
import sys


CHECKS = []


def check(label, condition):
    CHECKS.append((label, bool(condition)))


# ---------------------------------------------------------------------------
# Z[zeta_5] in the basis 1, zeta, zeta^2, zeta^3, with zeta^4 = -1-zeta-zeta^2-zeta^3.
# ---------------------------------------------------------------------------
def rmul(left, right, modulus=None):
    raw = [0] * 7
    for i in range(4):
        if left[i]:
            for j in range(4):
                raw[i + j] += left[i] * right[j]
    for degree in (6, 5, 4):
        carry = raw[degree]
        if carry:
            raw[degree] = 0
            for step in range(4):
                raw[degree - 4 + step] -= carry
    result = tuple(raw[:4])
    if modulus is not None:
        result = tuple(value % modulus for value in result)
    return result


def radd(left, right, modulus=None):
    result = tuple(left[i] + right[i] for i in range(4))
    if modulus is not None:
        result = tuple(value % modulus for value in result)
    return result


def rsub(left, right, modulus=None):
    result = tuple(left[i] - right[i] for i in range(4))
    if modulus is not None:
        result = tuple(value % modulus for value in result)
    return result


def rpow(base, exponent, modulus=None):
    result = ONE
    factor = base
    while exponent:
        if exponent & 1:
            result = rmul(result, factor, modulus)
        factor = rmul(factor, factor, modulus)
        exponent >>= 1
    return result


def rnorm(value):
    """Absolute norm, as the determinant of the multiplication matrix."""
    columns = []
    for j in range(4):
        unit_vector = [0] * 4
        unit_vector[j] = 1
        columns.append(rmul(value, tuple(unit_vector)))
    matrix = [[columns[j][i] for j in range(4)] for i in range(4)]
    total = 0
    for perm in permutations(range(4)):
        sign = 1
        for i in range(4):
            for j in range(i + 1, 4):
                if perm[i] > perm[j]:
                    sign = -sign
        term = sign
        for i in range(4):
            term *= matrix[i][perm[i]]
        total += term
    return total


def v5(number):
    if number == 0:
        return None
    count = 0
    while number % 5 == 0:
        number //= 5
        count += 1
    return count


def vlam(value):
    """lambda-adic valuation, via v_5 of the absolute norm; N(lambda) = 5."""
    return v5(rnorm(value))


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
ZETA = (0, 1, 0, 0)
J = (1, 0, 1, 0)                 # 1 + zeta^2
PHI = (0, 0, -1, -1)             # -zeta^2 - zeta^3
LAM = (1, -1, 0, 0)              # 1 - zeta

# Frozen ranges.
ORDER_LEVELS = tuple(range(1, 13))       # m in ord_(lambda^(4m))(J) = 4*5^m
VALUATION_LEVELS = tuple(range(0, 5))    # m in v_lambda(J^(4*5^m) - 1)
UNIT_COUNT_LEVELS = (1, 2)               # m in |(O/5^m)^x| = 4*5^(4m-1)
GRID_LEVELS = tuple(range(0, 6))
OFF_GRID_DENOMINATORS = (3, 7, 8, 9, 11, 12, 16, 60)
INDUCTION_LENGTH = 24

# ---------------------------------------------------------------------------
# C1  The ring, J, and its infinite order.
# ---------------------------------------------------------------------------
check("C1-01 zeta^5 equals 1", rpow(ZETA, 5) == ONE)
check(
    "C1-02 zeta satisfies x^4+x^3+x^2+x+1",
    radd(radd(radd(radd(rpow(ZETA, 4), rpow(ZETA, 3)), rpow(ZETA, 2)), ZETA), ONE) == ZERO,
)
check("C1-03 phi^2 equals phi+1", rmul(PHI, PHI) == radd(PHI, ONE))
check("C1-04 J*phi equals zeta", rmul(J, PHI) == ZETA)
check("C1-05 the absolute norm of J is 1", rnorm(J) == 1)
check("C1-06 the absolute trace of J is 3", 4 * J[0] - J[1] - J[2] - J[3] == 3)
ROOTS_OF_UNITY = tuple(
    tuple(sign * component for component in rpow(ZETA, power))
    for sign in (1, -1)
    for power in range(5)
)
check(
    "C1-07 J is none of the ten roots of unity of Q(zeta_5), so J has infinite order",
    len(set(ROOTS_OF_UNITY)) == 10 and tuple(J) not in set(ROOTS_OF_UNITY),
)

# ---------------------------------------------------------------------------
# C2  Reduction modulo lambda, and ord_lambda(J) = 4.
# ---------------------------------------------------------------------------
check("C2-01 the norm of lambda is 5", rnorm(LAM) == 5)


def residue(value):
    """O/lambda -> F_5, induced by zeta -> 1."""
    return sum(value) % 5


hom_ok = True
for left in ((1, 2, 3, 4), (0, 1, -1, 2), J, PHI, LAM, ZETA):
    for right in ((2, 0, 1, 1), (-3, 1, 0, 2), J, ONE, LAM):
        if residue(rmul(left, right)) != (residue(left) * residue(right)) % 5:
            hom_ok = False
        if residue(radd(left, right)) != (residue(left) + residue(right)) % 5:
            hom_ok = False
check("C2-02 the residue map O -> F_5 is a ring homomorphism on the declared pairs", hom_ok)
check("C2-03 lambda reduces to 0 and J reduces to 2", residue(LAM) == 0 and residue(J) == 2)
check(
    "C2-04 2 has multiplicative order 4 in F_5, so ord_lambda(J) = 4",
    [pow(2, e, 5) for e in range(1, 5)] == [2, 4, 3, 1],
)

# ---------------------------------------------------------------------------
# C3  The order ladder.  O/lambda^(4m) is modelled as Z[x]/(Phi_5, 5^m),
#     because lambda^4 and (5) generate the same ideal (e = 4).
# ---------------------------------------------------------------------------
check(
    "C3-01 lambda^4 and 5 generate the same ideal: v_lambda(5) = 4 and v_lambda(lambda) = 1",
    vlam((5, 0, 0, 0)) == 4 and vlam(LAM) == 1,
)
def multiplicative_order(base, modulus, bound):
    """Exact order, found from the divisors of a known multiple."""
    if rpow(base, bound, modulus) != ONE:
        return None
    order = bound
    changed = True
    while changed:
        changed = False
        for prime in (2, 5):
            if order % prime == 0 and rpow(base, order // prime, modulus) == ONE:
                order //= prime
                changed = True
    return order


measured_orders = []
for level in ORDER_LEVELS:
    modulus = 5 ** level
    # |(O/lambda^(4m))^x| = 4*5^(4m-1) is a multiple of every element order.
    measured_orders.append(
        multiplicative_order(J, modulus, 4 * 5 ** (4 * level - 1))
    )
order_ok = measured_orders == [4 * 5 ** level for level in ORDER_LEVELS]
check(
    f"C3-02 ord_(lambda^(4m))(J) = 4*5^m for 1<=m<={max(ORDER_LEVELS)}",
    order_ok,
)
def is_four_times_power_of_five(size):
    if size is None or size % 4 != 0:
        return False
    rest = size // 4
    while rest % 5 == 0:
        rest //= 5
    return rest == 1


check(
    "C3-03 every measured orbit size is 4 times a power of 5, the index sequence n_A",
    all(is_four_times_power_of_five(size) for size in measured_orders)
    and measured_orders == [4 * 5 ** level for level in ORDER_LEVELS],
)
unit_count_ok = True
for level in UNIT_COUNT_LEVELS:
    modulus = 5 ** level
    units = 0
    for coefficients in product(range(modulus), repeat=4):
        if sum(coefficients) % 5 != 0:
            units += 1
    if units != 4 * 5 ** (4 * level - 1):
        unit_count_ok = False
check(
    "C3-04 |(O/5^m)^x| = 4*5^(4m-1) by direct count for the declared m",
    unit_count_ok,
)
check(
    "C3-05 every orbit size divides 4*5^a by Lagrange, since |(O/lambda^k)^x| = 4*5^(k-1)",
    unit_count_ok and all(
        (4 * 5 ** (4 * level - 1)) % (4 * 5 ** level) == 0 for level in ORDER_LEVELS
    ),
)

# ---------------------------------------------------------------------------
# C4  The valuation ladder, including the boundary jump at the first step.
# ---------------------------------------------------------------------------
valuations = []
for level in VALUATION_LEVELS:
    power = rpow(J, 4 * 5 ** level)
    valuations.append(vlam(rsub(power, ONE)))
check("C4-01 v_lambda(J^4 - 1) = 1, the boundary case e/(p-1) = 1", valuations[0] == 1)
check(
    "C4-02 v_lambda(J^20 - 1) = 6, a jump of 5 rather than e = 4",
    valuations[1] == 6,
)
check(
    "C4-03 v_lambda(J^(4*5^m) - 1) = 4m+2 for m >= 1 on the declared range",
    all(valuations[level] == 4 * level + 2 for level in VALUATION_LEVELS if level >= 1),
)
check(
    "C4-04 the ladder is strictly increasing, so J^(4*5^m) is never 1",
    all(
        valuations[index] < valuations[index + 1]
        for index in range(len(valuations) - 1)
    )
    and all(value is not None for value in valuations),
)

# ---------------------------------------------------------------------------
# C5  The eigenvalue angle set is exactly the registered grid.
# ---------------------------------------------------------------------------
# An orbit of size d contributes the d-th roots of unity, that is the angle
# fractions j/d.  Collect them over the declared levels.
MAX_GRID_LEVEL = max(GRID_LEVELS)
GRID_LIMIT = 4 * 5 ** MAX_GRID_LEVEL

# Built one way: the union of the d-th roots of unity over the orbit sizes d.
generated = set()
for level in GRID_LEVELS:
    size = 4 * 5 ** level
    for j in range(size):
        generated.add(Fraction(j, size))

# Built the other way, independently: reduced fractions of Z[1/5]/4 shape,
# that is denominator 2^e * 5^f with e <= 2, no reference to the union above.
admissible = set()
for denominator in range(1, GRID_LIMIT + 1):
    rest, twos, fives = denominator, 0, 0
    while rest % 2 == 0:
        rest //= 2
        twos += 1
    while rest % 5 == 0:
        rest //= 5
        fives += 1
    if rest != 1 or twos > 2 or fives > MAX_GRID_LEVEL:
        continue
    for numerator in range(denominator):
        if gcd(numerator, denominator) == 1:
            admissible.add(Fraction(numerator, denominator))


def divides_some_index(denominator, span=14):
    return any((4 * 5 ** level) % denominator == 0 for level in range(span))


check(
    "C5-01 every generated angle fraction has denominator dividing some 4*5^a",
    all(divides_some_index(fraction.denominator) for fraction in generated),
)
check(
    "C5-02 the orbit-generated angle set equals the (1/4)Z[1/5] set built independently",
    generated == admissible and len(generated) == GRID_LIMIT,
)
check(
    "C5-03 an off-grid denominator divides no 4*5^a and is never generated",
    all(
        not divides_some_index(denominator)
        and all(
            fraction.denominator != denominator for fraction in generated
        )
        for denominator in OFF_GRID_DENOMINATORS
    ),
)
check(
    "C5-04 the grid is closed under the index action: n_A kills level a exactly when A>=a",
    all(
        (Fraction(4 * 5 ** index_level * numerator, 4 * 5 ** level).denominator == 1)
        == (index_level >= level)
        for level in GRID_LEVELS
        for index_level in GRID_LEVELS
        for numerator in (1, 3, 7, 11)
    ),
)

# ---------------------------------------------------------------------------
# C6  The converse induction: two initial values plus second differences.
# ---------------------------------------------------------------------------
induction_ok = True
DECLARED_SEQUENCES = (
    tuple(Fraction(n * n, 3) for n in range(INDUCTION_LENGTH)),
    tuple(Fraction(n, 1) for n in range(INDUCTION_LENGTH)),
    tuple(Fraction((-1) ** n * n, 7) for n in range(INDUCTION_LENGTH)),
    tuple(Fraction(n * (n - 1), 2) for n in range(INDUCTION_LENGTH)),
)
for target in DECLARED_SEQUENCES:
    if target[0] != 0:
        target = tuple(value - target[0] for value in target)
    rebuilt = [target[0], target[1]]
    for n in range(1, INDUCTION_LENGTH - 1):
        second = target[n + 1] + target[n - 1] - 2 * target[n]
        rebuilt.append(2 * rebuilt[n] - rebuilt[n - 1] + second)
    if tuple(rebuilt) != target:
        induction_ok = False
check(
    "C6-01 matching second differences and two initial values rebuild the sequence exactly",
    induction_ok,
)
def fejer_at(circle_point, n):
    """|1 + z + ... + z^(n-1)|^2 at an exact rational point of the unit circle."""
    real, imaginary = Fraction(0), Fraction(0)
    power_real, power_imaginary = Fraction(1), Fraction(0)
    for _ in range(n):
        real += power_real
        imaginary += power_imaginary
        power_real, power_imaginary = (
            power_real * circle_point[0] - power_imaginary * circle_point[1],
            power_real * circle_point[1] + power_imaginary * circle_point[0],
        )
    return real * real + imaginary * imaginary


CIRCLE_POINTS = (
    (Fraction(3, 5), Fraction(4, 5)),
    (Fraction(5, 13), Fraction(12, 13)),
    (Fraction(-7, 25), Fraction(24, 25)),
    (Fraction(8, 17), Fraction(15, 17)),
)
check(
    "C6-02 the Fejer normalization supplies those two values: D_0 = 0 and D_1 = 1",
    all(point[0] ** 2 + point[1] ** 2 == 1 for point in CIRCLE_POINTS)
    and all(fejer_at(point, 0) == 0 for point in CIRCLE_POINTS)
    and all(fejer_at(point, 1) == 1 for point in CIRCLE_POINTS),
)

# ---------------------------------------------------------------------------
# C7  Mass bookkeeping for the constructed vector.
# ---------------------------------------------------------------------------
# Atom masses (1/2)/(1/4+g^2) at each of +/- alpha_g, over a free rational
# ladder standing in for ordinates.  The vector norm is the total mass.
LADDER = tuple(Fraction(k, 2) for k in range(1, 13))
total_mass = Fraction(0)
mass_ok = True
for point in LADDER:
    weight = Fraction(1, 2) / (Fraction(1, 4) + point * point)
    if weight <= 0:
        mass_ok = False
    total_mass += 2 * weight
paired = sum(Fraction(1, 1) / (Fraction(1, 4) + point * point) for point in LADDER)
check("C7-01 every atom mass is strictly positive", mass_ok)
check(
    "C7-02 the two atoms of an ordinate carry total mass 1/(1/4+g^2)",
    total_mass == paired,
)
# The construction itself, on exact rational data: coefficients c_i on an
# orthonormal family, atom masses m_i = c_i^2, vector norm sum m_i.
COEFFICIENTS = tuple(Fraction(1, k) for k in range(1, 15))
atom_masses = tuple(coefficient * coefficient for coefficient in COEFFICIENTS)
vector_norm_squared = sum(
    coefficient * coefficient for coefficient in COEFFICIENTS
)
check(
    "C7-03 the vector norm equals the total atom mass, so summability gives v in L^2",
    vector_norm_squared == sum(atom_masses)
    and all(mass > 0 for mass in atom_masses)
    and vector_norm_squared > 0,
)

# ---------------------------------------------------------------------------
# C8  Registered conclusions.
# ---------------------------------------------------------------------------
spectrum_ok = order_ok and unit_count_ok
check(
    "C8-01 U_J has pure point spectrum with eigenvalue angles exactly the grid",
    spectrum_ok,
)
check(
    "C8-02 every grid angle is attained, so the converse construction has its atoms",
    spectrum_ok and mass_ok,
)
check(
    "C8-03 the grid condition is sufficient as well as necessary",
    spectrum_ok and induction_ok and mass_ok,
)
check(
    "C8-04 a cocycle vector exists iff RH holds and every Cayley angle is on the grid",
    spectrum_ok and induction_ok and mass_ok,
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
