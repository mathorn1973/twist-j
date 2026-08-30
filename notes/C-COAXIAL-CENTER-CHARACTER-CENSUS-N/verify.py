from fractions import Fraction as Fr


# K = Q(zeta_5) in the basis (1, z, z^2, z^3), with
# z^4 = -(1 + z + z^2 + z^3).
def K(*c):
    return tuple(Fr(x) for x in (list(c) + [0, 0, 0, 0])[:4])


ZERO = K(0)
ONE = K(1)
Z = K(0, 1)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def smul(s, a):
    return tuple(Fr(s) * x for x in a)


def _red(c):
    """Reduce a polynomial of degree at most six modulo Phi_5."""
    c = list(c) + [0] * (7 - len(c))
    for degree in (6, 5):
        # z^5 = 1 and z^6 = z.
        if c[degree]:
            c[degree - 5] += c[degree]
            c[degree] = 0
    if c[4]:
        coefficient = c[4]
        c[4] = 0
        for i in range(4):
            c[i] -= coefficient
    return tuple(c[:4])


def mul(a, b):
    c = [Fr(0)] * 7
    for i in range(4):
        if a[i] == 0:
            continue
        for j in range(4):
            c[i + j] += a[i] * b[j]
    return _red(c)


def multiplication_matrix(a):
    """Matrix of multiplication by a in the power basis."""
    columns = []
    for i in range(4):
        e = [Fr(0)] * 4
        e[i] = Fr(1)
        columns.append(mul(a, tuple(e)))
    return [[columns[j][i] for j in range(4)] for i in range(4)]


def inv(a):
    matrix = multiplication_matrix(a)
    n = 4
    augmented = [
        row[:] + [Fr(1) if i == j else Fr(0) for j in range(n)]
        for i, row in enumerate(matrix)
    ]
    for column in range(n):
        pivot = next(row for row in range(column, n) if augmented[row][column] != 0)
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        value = augmented[column][column]
        augmented[column] = [x / value for x in augmented[column]]
        for row in range(n):
            if row != column and augmented[row][column] != 0:
                factor = augmented[row][column]
                augmented[row] = [
                    x - factor * y
                    for x, y in zip(augmented[row], augmented[column])
                ]
    e0 = [Fr(1), Fr(0), Fr(0), Fr(0)]
    solution = [
        sum(augmented[i][n + j] * e0[j] for j in range(n))
        for i in range(n)
    ]
    return tuple(solution)


def power(a, n):
    if n < 0:
        return power(inv(a), -n)
    result = ONE
    for _ in range(n):
        result = mul(result, a)
    return result


SQRT5 = K(-1, 0, -2, -2)
PHI = smul(Fr(1, 2), add(ONE, SQRT5))
ZETA10 = neg(mul(Z, mul(Z, Z)))


# =============================================================================
# Exact local audit for notes/C-COAXIAL-CENTER-CHARACTER-CENSUS-N/README.md.
#
# Status: NON-CANONICAL, candidate-T census with frozen decision set
# UNIQUE / NONUNIQUE / EMPTY / STOP. This is not a formal public probe,
# preregistration, two-architecture gate, Canon change, or Registry change.
# Exact arithmetic in Q(zeta_5) decides every check. Finite sweeps are
# exhaustive and deterministic; there is no randomness. Any failed check
# produces exit status 1.
# =============================================================================
import sys


ok = True


def check(name, condition, extra=""):
    global ok
    ok &= bool(condition)
    print(
        f"[{'PASS' if condition else 'FAIL'}] {name}"
        + (f"   {extra}" if extra else "")
    )


# ---------- 0. Base identities and the frozen surviving group ---------------
check(
    "phi satisfies phi^2 = phi + 1, phi(phi-1) = 1, and phi = -(z^2+z^3)",
    mul(PHI, PHI) == add(PHI, ONE)
    and mul(PHI, sub(PHI, ONE)) == ONE
    and PHI == K(0, 0, -1, -1)
    and mul(SQRT5, SQRT5) == K(5),
)

zeta10_powers = [power(ZETA10, k) for k in range(11)]
check(
    "zeta_10 = -z^3 is primitive of order 10 with zeta_10^2 = z and "
    "zeta_10^5 = -1",
    len(set(zeta10_powers[:10])) == 10
    and zeta10_powers[10] == ONE
    and zeta10_powers[2] == Z
    and zeta10_powers[5] == neg(ONE),
)


def element(r, m):
    return mul(power(ZETA10, r % 10), power(PHI, 2 * m))


R_RANGE = range(10)
M_RANGE = range(-6, 7)
S_SWEEP = {(r, m): element(r, m) for r in R_RANGE for m in M_RANGE}
check(
    "the parametrization (r mod 10, m) of S is injective on the sweep",
    len(set(S_SWEEP.values())) == 130,
    "130 distinct elements",
)

PRODUCT_M = range(-2, 3)
check(
    "the group law is componentwise: q(r1,m1) q(r2,m2) = "
    "q(r1+r2 mod 10, m1+m2)",
    all(
        mul(element(r1, m1), element(r2, m2))
        == element((r1 + r2) % 10, m1 + m2)
        for r1 in R_RANGE
        for r2 in R_RANGE
        for m1 in PRODUCT_M
        for m2 in PRODUCT_M
    ),
    "2,500 exact products",
)

check(
    "squares have both parameters even: q(r,m)^2 = q(2r mod 10, 2m), and "
    "every sweep element with r and m even is a square from the sweep",
    all(
        mul(S_SWEEP[(r, m)], S_SWEEP[(r, m)])
        == element((2 * r) % 10, 2 * m)
        for r in R_RANGE
        for m in M_RANGE
    )
    and all(
        S_SWEEP[(r, m)]
        == mul(element(r // 2, m // 2), element(r // 2, m // 2))
        or S_SWEEP[(r, m)]
        == mul(element(r // 2 + 5, m // 2), element(r // 2 + 5, m // 2))
        for r in (0, 2, 4, 6, 8)
        for m in (-6, -4, -2, 0, 2, 4, 6)
    ),
)


# ---------- 1. The four sign characters -------------------------------------
def chi(a, b, r, m):
    return -1 if (a * r + b * m) % 2 else 1


CHARACTERS = [(0, 0), (0, 1), (1, 0), (1, 1)]

check(
    "each chi_{a,b}(r,m) = (-1)^(ar+bm) is multiplicative on the product "
    "sweep",
    all(
        chi(a, b, (r1 + r2) % 10, m1 + m2)
        == chi(a, b, r1, m1) * chi(a, b, r2, m2)
        for (a, b) in CHARACTERS
        for r1 in R_RANGE
        for r2 in R_RANGE
        for m1 in PRODUCT_M
        for m2 in PRODUCT_M
    ),
    "4 characters, 2,500 products each",
)

check(
    "chi_{a,b} depends only on the residues (r mod 2, m mod 2), so it is "
    "well defined on S",
    all(
        chi(a, b, r, m) == chi(a, b, r % 2, m % 2)
        for (a, b) in CHARACTERS
        for r in R_RANGE
        for m in M_RANGE
    ),
)

generator_signs = {}
for s1 in (1, -1):
    for s2 in (1, -1):
        # s2^m for negative m equals s2^|m| because s2 is its own inverse.
        table = {
            (r, m): (s1 ** r) * (s2 ** abs(m))
            for r in R_RANGE
            for m in M_RANGE
        }
        matches = [
            (a, b)
            for (a, b) in CHARACTERS
            if all(
                table[(r, m)] == chi(a, b, r, m)
                for r in R_RANGE
                for m in M_RANGE
            )
        ]
        generator_signs[(s1, s2)] = matches

check(
    "exhaustiveness audit: every sign assignment to the generators "
    "(zeta_10, phi^2) extends to exactly one chi_{a,b}, and the relation "
    "zeta_10^10 = 1 is respected",
    all(len(matches) == 1 for matches in generator_signs.values())
    and sorted(
        matches[0] for matches in generator_signs.values()
    )
    == sorted(CHARACTERS)
    and all(s1 ** 10 == 1 for (s1, _) in generator_signs),
)


# ---------- 2. The center condition -----------------------------------------
check(
    "the center: -1 = zeta_10^5 = q(5,0) exactly",
    S_SWEEP[(5, 0)] == neg(ONE),
)

center_values = {(a, b): chi(a, b, 5, 0) for (a, b) in CHARACTERS}
ADMISSIBLE = sorted(
    (a, b) for (a, b) in CHARACTERS if center_values[(a, b)] == -1
)
check(
    "chi_{a,b}(-1) = (-1)^a, so central compatibility chi(-1) = -1 holds "
    "exactly for a = 1",
    all(
        center_values[(a, b)] == (-1 if a == 1 else 1)
        for (a, b) in CHARACTERS
    )
    and ADMISSIBLE == [(1, 0), (1, 1)],
)

check(
    "negative controls: chi_{0,0} and chi_{0,1} send -1 to +1 and are "
    "excluded",
    center_values[(0, 0)] == 1 and center_values[(0, 1)] == 1,
)

check(
    "the two admissible characters are distinct: they disagree exactly on "
    "the elements with odd boost count, witnessed by phi^2 = q(0,1)",
    chi(1, 0, 0, 1) == 1
    and chi(1, 1, 0, 1) == -1
    and all(
        (chi(1, 0, r, m) != chi(1, 1, r, m)) == (m % 2 == 1)
        for r in R_RANGE
        for m in M_RANGE
    ),
)

check(
    "the twist identity: chi_{1,1} = chi_{1,0} . chi_{0,1} pointwise, with "
    "chi_{0,1}(r,m) = (-1)^m the center-trivial boost parity",
    all(
        chi(1, 1, r, m) == chi(1, 0, r, m) * chi(0, 1, r, m)
        for r in R_RANGE
        for m in M_RANGE
    ),
)


# ---------- 3. The ramified readout realizes chi_{1,1} ----------------------
def residue_mod_5(a):
    total = sum(a[i] for i in range(4))
    return (
        (total.numerator % 5)
        * pow(total.denominator % 5, -1, 5)
        % 5
    )


def epsilon(q):
    residue = residue_mod_5(q)
    if residue == 1:
        return 1
    if residue == 4:
        return -1
    raise ArithmeticError("the element is outside the surviving group")


check(
    "the p_5 readout of every sweep element is a sign and equals "
    "chi_{1,1}(r,m) = (-1)^(r+m) exactly",
    all(
        epsilon(S_SWEEP[(r, m)]) == chi(1, 1, r, m)
        for r in R_RANGE
        for m in M_RANGE
    ),
    "130 elements",
)

check(
    "chi_{1,0} is the mu_5-membership parity: chi_{1,0}(r,m) = +1 exactly "
    "when zeta_10^r lies in mu_5",
    all(
        (chi(1, 0, r, m) == 1)
        == (power(ZETA10, r) in {power(Z, k) for k in range(5)})
        for r in R_RANGE
        for m in (-1, 0, 1)
    ),
)


# ---------- 4. The frozen census decision -----------------------------------
census_cardinality = len(ADMISSIBLE)
decision = {0: "EMPTY", 1: "UNIQUE"}.get(census_cardinality, "NONUNIQUE")
check(
    "the census decision on the frozen class is NONUNIQUE with cardinality "
    "exactly two",
    census_cardinality == 2 and decision == "NONUNIQUE",
    f"decision = {decision}, admissible = chi_(1,0) and chi_(1,1)",
)


print("\n" + ("ALL CHECKS PASS" if ok else "ONE OR MORE CHECKS FAILED"))
sys.exit(0 if ok else 1)
