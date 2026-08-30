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


def conj(a):
    """CM conjugation z -> z^4."""
    c = [Fr(0)] * 7
    power_map = {0: 0, 1: 4, 2: 3, 3: 2}
    for i in range(4):
        if a[i] == 0:
            continue
        c[power_map[i]] += a[i]
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


def is_int(a):
    """Test algebraic integrality through the exact characteristic polynomial."""
    matrix = multiplication_matrix(a)
    n = 4
    identity = [
        [Fr(1) if i == j else Fr(0) for j in range(n)]
        for i in range(n)
    ]
    power_matrix = [row[:] for row in identity]
    coefficients = [Fr(1)]
    for k in range(1, n + 1):
        power_matrix = [
            [
                sum(matrix[i][t] * power_matrix[t][j] for t in range(n))
                for j in range(n)
            ]
            for i in range(n)
        ]
        trace = sum(power_matrix[i][i] for i in range(n))
        coefficient = -trace / k
        coefficients.append(coefficient)
        for i in range(n):
            power_matrix[i][i] += coefficient
    return all(x.denominator == 1 for x in coefficients)


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
J = K(1, 0, 1)


# =============================================================================
# Exact local audit for notes/C-COAXIAL-STEP-READING-FAMILY-N/README.md.
#
# Status: NON-CANONICAL, candidate-T skeleton with a candidate-D reading.
# This is not a formal public probe, preregistration, two-architecture gate,
# Canon change, or Registry change. Exact arithmetic in Q(zeta_5) decides
# every check. Finite sweeps are exhaustive and deterministic; there is no
# randomness. Any failed check produces exit status 1.
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


def parity_sign(n):
    """Return (-1)^n as an integer, including for negative n."""
    return 1 if n % 2 == 0 else -1


# ---------- 0. Base identities and the frozen unit family -------------------
check(
    "phi satisfies phi^2 = phi + 1, phi(phi-1) = 1, and phi = -(z^2+z^3)",
    mul(PHI, PHI) == add(PHI, ONE)
    and mul(PHI, sub(PHI, ONE)) == ONE
    and PHI == K(0, 0, -1, -1)
    and mul(SQRT5, SQRT5) == K(5)
    and sub(add(PHI, PHI), ONE) == SQRT5,
)

zeta10_powers = [power(ZETA10, k) for k in range(11)]
check(
    "zeta_10 = -z^3 is primitive of order 10 with zeta_10^2 = z",
    len(set(zeta10_powers[:10])) == 10
    and zeta10_powers[10] == ONE
    and zeta10_powers[2] == Z
    and zeta10_powers[5] == neg(ONE),
)

check(
    "J = 1 + z^2 = z phi^-1 exactly",
    J == add(ONE, power(Z, 2))
    and J == mul(Z, inv(PHI)),
)


def unit(r, n):
    return mul(power(ZETA10, r % 10), power(PHI, n))


family = {(r, n): unit(r, n) for r in range(10) for n in range(-6, 7)}
check(
    "the family zeta_10^r phi^n is injective for r mod 10 and |n| <= 6",
    len(set(family.values())) == 130,
    "130 distinct elements",
)


# ---------- 1. The labeled icosian placement and its orbit lattice ----------
def quaternion_mul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (
        sub(sub(sub(mul(a0, b0), mul(a1, b1)), mul(a2, b2)), mul(a3, b3)),
        sub(add(add(mul(a0, b1), mul(a1, b0)), mul(a2, b3)), mul(a3, b2)),
        add(add(sub(mul(a0, b2), mul(a1, b3)), mul(a2, b0)), mul(a3, b1)),
        add(sub(add(mul(a0, b3), mul(a1, b2)), mul(a2, b1)), mul(a3, b0)),
    )


def quaternion_conj(a):
    return (a[0], neg(a[1]), neg(a[2]), neg(a[3]))


def reduced_norm(a):
    return quaternion_mul(a, quaternion_conj(a))[0]


phi_inverse = inv(PHI)
half = K(Fr(1, 2))
Q1 = (ONE, ZERO, ZERO, ZERO)
Qi = (ZERO, ONE, ZERO, ZERO)
Qj = (ZERO, ZERO, ONE, ZERO)
OMEGA = (smul(Fr(1, 2), phi_inverse), smul(Fr(1, 2), PHI), ZERO, half)


def quaternion_key(a):
    return tuple(x for coefficient in a for x in coefficient)


GROUP_TARGET = 120
GROUP = {quaternion_key(Q1): Q1}
frontier = [Q1]
group_generation_converged = False
for _generation in range(GROUP_TARGET + 1):
    if not frontier:
        group_generation_converged = True
        break
    new_frontier = []
    overflow = False
    for x in frontier:
        for generator in (OMEGA, Qi, Qj):
            y = quaternion_mul(x, generator)
            if quaternion_key(y) not in GROUP:
                GROUP[quaternion_key(y)] = y
                new_frontier.append(y)
                if len(GROUP) > GROUP_TARGET:
                    overflow = True
                    break
        if overflow:
            break
    frontier = new_frontier
    if overflow:
        break

check(
    "omega is an icosian with Nrd = 1 and Trd = 1/phi, and |<omega,i,j>| = 120",
    reduced_norm(OMEGA) == ONE
    and add(OMEGA[0], OMEGA[0]) == phi_inverse
    and group_generation_converged
    and len(GROUP) == 120
    and all(reduced_norm(v) == ONE for v in GROUP.values()),
)

OMEGA_J = quaternion_mul(OMEGA, Qj)
BASIS = [Q1, OMEGA, Qj, OMEGA_J]


def solve_coordinates(g):
    matrix = [[BASIS[column][row] for column in range(4)] for row in range(4)]
    right_side = [g[row] for row in range(4)]
    augmented = [matrix[i][:] + [right_side[i]] for i in range(4)]
    for column in range(4):
        pivot = next(
            row for row in range(column, 4) if augmented[row][column] != ZERO
        )
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_inverse = inv(augmented[column][column])
        augmented[column] = [
            mul(pivot_inverse, x) for x in augmented[column]
        ]
        for row in range(4):
            if row != column and augmented[row][column] != ZERO:
                factor = augmented[row][column]
                augmented[row] = [
                    sub(x, mul(factor, y))
                    for x, y in zip(augmented[row], augmented[column])
                ]
    return [augmented[i][4] for i in range(4)]


def split_matrix(g):
    a0, a1, b0, b1 = solve_coordinates(g)
    x = add(a0, mul(a1, Z))
    y = add(b0, mul(b1, Z))
    return ((x, neg(y)), (conj(y), conj(x)))


def split_vector(g):
    a0, a1, b0, b1 = solve_coordinates(g)
    return (add(a0, mul(a1, Z)), conj(add(b0, mul(b1, Z))))


def matrix_mul(a, b):
    return tuple(
        tuple(
            add(mul(a[i][0], b[0][j]), mul(a[i][1], b[1][j]))
            for j in range(2)
        )
        for i in range(2)
    )


def matrix_det(a):
    return sub(mul(a[0][0], a[1][1]), mul(a[0][1], a[1][0]))


def matrix_inv(a):
    determinant_inverse = inv(matrix_det(a))
    return (
        (mul(determinant_inverse, a[1][1]), neg(mul(determinant_inverse, a[0][1]))),
        (neg(mul(determinant_inverse, a[1][0])), mul(determinant_inverse, a[0][0])),
    )


def matrix_is_int(a):
    return all(is_int(a[i][j]) for i in range(2) for j in range(2))


MATRIX_BY_QUATERNION = {
    key: split_matrix(value) for key, value in GROUP.items()
}
MATRICES = list(MATRIX_BY_QUATERNION.values())
MATRIX_SET = set(MATRICES)
check(
    "M is faithful: 120 distinct determinant-one matrices with "
    "M(omega) = diag(z, z^-1)",
    len(MATRIX_SET) == 120
    and all(matrix_det(matrix) == ONE for matrix in MATRICES)
    and split_matrix(OMEGA) == ((Z, ZERO), (ZERO, conj(Z))),
)

group_items = tuple(GROUP.items())
homomorphism_pairs = 0
homomorphism_ok = len(group_items) == GROUP_TARGET
if homomorphism_ok:
    for left_key, left in group_items:
        left_matrix = MATRIX_BY_QUATERNION[left_key]
        for right_key, right in group_items:
            product_key = quaternion_key(quaternion_mul(left, right))
            product_matrix = MATRIX_BY_QUATERNION.get(product_key)
            if product_matrix is None or product_matrix != matrix_mul(
                left_matrix,
                MATRIX_BY_QUATERNION[right_key],
            ):
                homomorphism_ok = False
                break
            homomorphism_pairs += 1
        if not homomorphism_ok:
            break

check(
    "M is a homomorphism on all 120 x 120 products of the generated group",
    homomorphism_ok and homomorphism_pairs == GROUP_TARGET ** 2,
    f"{homomorphism_pairs} exact products checked",
)

a_F = neg(mul(power(Z, 3), inv(sub(ONE, Z))))
b_F = K(Fr(2, 5), Fr(4, 5), Fr(1, 5), Fr(3, 5))
F_LAM = ((ONE, a_F), (ZERO, b_F))
check(
    "the orbit basis [[1,a],[0,b]] has the split images of 1 and i as columns",
    split_vector(Q1) == (ONE, ZERO)
    and split_vector(Qi) == (a_F, b_F),
)

F_INV = matrix_inv(F_LAM)


def in_lattice_coordinates(vector):
    return (
        add(mul(F_INV[0][0], vector[0]), mul(F_INV[0][1], vector[1])),
        add(mul(F_INV[1][0], vector[0]), mul(F_INV[1][1], vector[1])),
    )


check(
    "all 120 orbit vectors are integral in the basis, so Lambda = F O_K^2 "
    "is the orbit lattice",
    all(
        all(is_int(x) for x in in_lattice_coordinates(split_vector(v)))
        for v in GROUP.values()
    ),
)

check(
    "conjugation by the basis makes all 120 matrices integral, so the "
    "labeled 2I preserves Lambda",
    all(
        matrix_is_int(matrix_mul(matrix_mul(F_INV, matrix), F_LAM))
        for matrix in MATRICES
    ),
)


# ---------- 2. The survival criterion, re-audited on this base --------------
check(
    "a = -z^3/(1-z) is not integral while (1-z)a is integral",
    (not is_int(a_F)) and is_int(mul(sub(ONE, Z), a_F)),
)

triangle_units = [unit(r, n) for r in (0, 3) for n in range(-2, 3)]
check(
    "triangular identity F^-1 diag(q1,q2) F = [[q1, a(q1-q2)],[0,q2]] "
    "on 100 unit pairs",
    all(
        matrix_mul(matrix_mul(F_INV, ((q1, ZERO), (ZERO, q2))), F_LAM)
        == ((q1, mul(a_F, sub(q1, q2))), (ZERO, q2))
        for q1 in triangle_units
        for q2 in triangle_units
    ),
)


def step(q):
    return ((q, ZERO), (ZERO, inv(q)))


def preserves_lattice(matrix):
    return matrix_is_int(
        matrix_mul(matrix_mul(F_INV, matrix), F_LAM)
    ) and matrix_is_int(
        matrix_mul(matrix_mul(F_INV, matrix_inv(matrix)), F_LAM)
    )


def residue_mod_5(a):
    total = sum(a[i] for i in range(4))
    return (
        (total.numerator % 5)
        * pow(total.denominator % 5, -1, 5)
        % 5
    )


survival = {}
for r in range(10):
    for n in range(-4, 5):
        survival[(r, n)] = preserves_lattice(step(unit(r, n)))
check(
    "AUDIT: D(q) Lambda = Lambda iff n is even, over 90 cases with "
    "r mod 10 and |n| <= 4",
    all(
        survival[(r, n)] == (n % 2 == 0)
        for r in range(10)
        for n in range(-4, 5)
    ),
    "90 cases, 0 mismatches",
)

check(
    "the ramified readout is (-1)^r 3^n mod 5 and survival is exactly "
    "readout in {1,-1} in the 90-case finite audit",
    all(
        residue_mod_5(unit(r, n)) == (parity_sign(r) * pow(3, n, 5)) % 5
        and survival[(r, n)]
        == (residue_mod_5(unit(r, n)) in (1, 4))
        for r in range(10)
        for n in range(-4, 5)
    ),
)


# ---------- 3. The two archimedean legs of the reading ----------------------
def tau(q):
    return mul(q, inv(conj(q)))


check(
    "q qbar = phi^2n and tau(q) = q/qbar = z^r on the 130-element "
    "finite family sweep",
    all(
        mul(q, conj(q)) == power(PHI, 2 * n)
        and tau(q) == power(Z, r % 5)
        for (r, n), q in family.items()
    ),
)

herm_basis = [
    ((ONE, ZERO), (ZERO, ZERO)),
    ((ZERO, ZERO), (ZERO, ONE)),
    ((ZERO, ONE), (ONE, ZERO)),
    ((ZERO, Z), (conj(Z), ZERO)),
]


def eigenvalue_reading_holds(r, m):
    q = unit(r, 2 * m)
    d = step(q)
    d_star = ((conj(q), ZERO), (ZERO, conj(inv(q))))
    scale_plus = power(PHI, 4 * m)
    scale_minus = power(PHI, -4 * m)
    phase = tau(q)
    for x in herm_basis:
        image = matrix_mul(matrix_mul(d, x), d_star)
        expected = (
            (
                mul(scale_plus, x[0][0]),
                mul(phase, x[0][1]),
            ),
            (
                mul(conj(phase), x[1][0]),
                mul(scale_minus, x[1][1]),
            ),
        )
        if image != expected:
            return False
    return True


check(
    "eigenvalue reading: D X D* scales the cone axes by phi^{+-4m} and the "
    "transverse entries by tau, tau-bar",
    all(
        eigenvalue_reading_holds(r, m)
        for r in range(10)
        for m in range(-3, 4)
    ),
    "70 surviving steps, 4 Hermitian basis matrices each",
)

check(
    "adjoint-to-step phase regression: D* D^-1 = diag(z^-r, z^r) = "
    "M(omega)^-r lies in 2I for 50 finite-sweep steps",
    all(
        matrix_mul(
            ((conj(q), ZERO), (ZERO, conj(inv(q)))),
            matrix_inv(step(q)),
        )
        == ((power(Z, -r), ZERO), (ZERO, power(Z, r)))
        and ((power(Z, -r), ZERO), (ZERO, power(Z, r))) in MATRIX_SET
        for r in range(10)
        for m in (-2, -1, 0, 1, 2)
        for q in (unit(r, 2 * m),)
    ),
)


# ---------- 4. The Lucas ladder of boost values -----------------------------
LUCAS = [2, 1]
FIBONACCI = [0, 1]
for _ in range(220):
    LUCAS.append(LUCAS[-1] + LUCAS[-2])
    FIBONACCI.append(FIBONACCI[-1] + FIBONACCI[-2])


def lucas(k):
    return LUCAS[abs(k)]


def fibonacci(k):
    if k < 0:
        # F_{-k} = -F_k for the even indices 4m used here.
        return -FIBONACCI[-k]
    return FIBONACCI[k]


def boost_point(m):
    """The literal declared point (L_4m/2, sqrt(5) F_4m/2) in H(F)."""
    return (
        K(Fr(lucas(4 * m), 2)),
        smul(Fr(fibonacci(4 * m), 2), SQRT5),
    )


check(
    "AUDIT: the literal boost point (L_4m/2, sqrt5 F_4m/2) reconstructs "
    "phi^{+-4m} and lies on c^2-s^2=1 for |m| <= 8",
    all(
        add(*boost_point(m)) == power(PHI, 4 * m)
        and sub(*boost_point(m)) == power(PHI, -4 * m)
        and sub(
            mul(boost_point(m)[0], boost_point(m)[0]),
            mul(boost_point(m)[1], boost_point(m)[1]),
        )
        == ONE
        for m in range(-8, 9)
    ),
    "17 exact finite-regression cases",
)

check(
    "Pell gap L_4m^2 - 5 F_4m^2 = 4 and gamma_m = L_4m/2 strictly increases "
    "in the finite range 0 <= m <= 50",
    all(
        lucas(4 * m) ** 2 - 5 * fibonacci(4 * m) ** 2 == 4
        for m in range(0, 51)
    )
    and all(lucas(4 * (m + 1)) > lucas(4 * m) for m in range(0, 50)),
)

check(
    "first noncompact reading: gamma = L_4/2 = 7/2, gamma beta = 3 sqrt5/2, "
    "beta^2 = 45/49 < 1",
    lucas(4) == 7
    and fibonacci(4) == 3
    and Fr(5 * 3 * 3, 7 * 7) == Fr(45, 49)
    and Fr(45, 49) < 1,
)


def beta(m):
    return smul(Fr(fibonacci(4 * m), lucas(4 * m)), SQRT5)


check(
    "Einstein composition is count addition: exact beta-addition law for "
    "all |a|, |b| <= 4",
    all(
        mul(
            add(beta(a), beta(b)),
            inv(add(ONE, mul(beta(a), beta(b)))),
        )
        == beta(a + b)
        for a in range(-4, 5)
        for b in range(-4, 5)
    ),
    "81 exact identities in Q(sqrt5)",
)

check(
    "one-step recurrence gamma_{m+1} = 7 gamma_m - gamma_{m-1} and the "
    "half-integer step matrix [[7,15],[3,7]]/2 has determinant 1 and "
    "advances (L_4m/2, F_4m/2) in the stated finite regressions",
    all(
        lucas(4 * (m + 1)) == 7 * lucas(4 * m) - lucas(4 * (m - 1))
        for m in range(1, 40)
    )
    and Fr(7 * 7 - 15 * 3, 4) == 1
    and all(
        (
            Fr(7 * lucas(4 * m) + 15 * fibonacci(4 * m), 4),
            Fr(3 * lucas(4 * m) + 7 * fibonacci(4 * m), 4),
        )
        == (Fr(lucas(4 * (m + 1)), 2), Fr(fibonacci(4 * (m + 1)), 2))
        for m in range(0, 20)
    ),
)

check(
    "Pell points: (7/2,3/2) at m=1 and (161,72) at m=3 lie on t^2-5x^2=1, "
    "the classical (9,4) sits at the excluded index 6, and D(phi^3) breaks "
    "the lattice",
    Fr(49, 4) - 5 * Fr(9, 4) == 1
    and (lucas(12), fibonacci(12)) == (322, 144)
    and 161 ** 2 - 5 * 72 ** 2 == 1
    and (lucas(6), fibonacci(6)) == (18, 8)
    and 9 ** 2 - 5 * 4 ** 2 == 1
    and lucas(4) % 2 == 1
    and lucas(8) % 2 == 1
    and not preserves_lattice(step(power(PHI, 3))),
)


def reduce_mod_2(a):
    if not all(coefficient.denominator % 2 == 1 for coefficient in a):
        raise ArithmeticError("a denominator is not invertible modulo 2")
    return tuple(
        coefficient.numerator
        * pow(coefficient.denominator, -1, 2)
        % 2
        for coefficient in a
    )


check(
    "gamma_m is an integer iff 3 | m, equivalently phi^2m = 1 in F_16, "
    "for |m| <= 8",
    all(
        (lucas(4 * m) % 2 == 0)
        == (m % 3 == 0)
        == (reduce_mod_2(power(PHI, 2 * m)) == (1, 0, 0, 0))
        for m in range(-8, 9)
    ),
)


# ---------- 5. Exactness of the reading and the decode map ------------------
def epsilon(q):
    residue = residue_mod_5(q)
    if residue == 1:
        return 1
    if residue == 4:
        return -1
    raise ArithmeticError("the step does not survive")


surviving = {(r, m): unit(r, 2 * m) for r in range(10) for m in range(-6, 7)}


def reading(r, m):
    q = unit(r, 2 * m)
    return (
        tau(q),
        boost_point(m),
        epsilon(q),
    )


BOOST_IDENTITY = (ONE, ZERO)
check(
    "the archimedean pair (tau, boost) has kernel exactly {1,-1} on the "
    "130-element surviving finite sweep",
    sorted(
        (r, m)
        for (r, m) in surviving
        if tau(surviving[(r, m)]) == ONE
        and boost_point(m) == BOOST_IDENTITY
    )
    == [(0, 0), (5, 0)]
    and surviving[(0, 0)] == ONE
    and surviving[(5, 0)] == neg(ONE),
)

check(
    "the ramified sign is (-1)^{r+m} and flips under q -> -q on the "
    "130-element surviving finite sweep",
    all(
        epsilon(surviving[(r, m)]) == parity_sign(r + m)
        and epsilon(neg(surviving[(r, m)]))
        == -epsilon(surviving[(r, m)])
        for (r, m) in surviving
    ),
)

readings = {key: reading(*key) for key in surviving}
check(
    "the triple (tau, boost, sign) is faithful: 130 distinct readings on "
    "the finite sweep",
    len(set(readings.values())) == 130,
)


def _integer_from_rational_k(a):
    if a[1:] != (Fr(0), Fr(0), Fr(0)) or a[0].denominator != 1:
        raise ValueError("the boost coordinate is not a rational integer")
    return int(a[0])


def decode_boost_point(value):
    """Invert a literal half-Lucas boost point without a fixed m window."""
    c, s = value
    lucas_value = _integer_from_rational_k(smul(2, c))
    fibonacci_value = _integer_from_rational_k(
        smul(2, mul(s, inv(SQRT5)))
    )
    if lucas_value < 2:
        raise ValueError("the boost point is not on the half-Lucas ladder")

    sign = -1 if fibonacci_value < 0 else 1
    target = (lucas_value, abs(fibonacci_value))
    current = (2, 0)
    # For a valid point L_4m grows faster than 2^|m|. This input-size bound
    # therefore exceeds every valid |m| and terminates on malformed input.
    max_steps = 2 * lucas_value.bit_length() + 2
    for m_abs in range(max_steps + 1):
        if current == target:
            return sign * m_abs
        if current[0] > lucas_value:
            break
        next_lucas_numerator = 7 * current[0] + 15 * current[1]
        next_fibonacci_numerator = 3 * current[0] + 7 * current[1]
        if next_lucas_numerator % 2 or next_fibonacci_numerator % 2:
            raise ArithmeticError("the exact boost recurrence lost integrality")
        current = (
            next_lucas_numerator // 2,
            next_fibonacci_numerator // 2,
        )
    raise ValueError("the boost point is not on the half-Lucas ladder")


def decode(value):
    phase, boost, sign = value
    if sign not in (-1, 1):
        raise ValueError("the ramified sign is not +1 or -1")
    m = decode_boost_point(boost)
    phase_exponents = [k for k in range(5) if power(Z, k) == phase]
    if len(phase_exponents) != 1:
        raise ValueError("the phase is not in the declared mu_5")
    a = phase_exponents[0]
    parity = (m + (0 if sign == 1 else 1)) % 2
    residues = [x for x in range(10) if x % 5 == a and x % 2 == parity]
    if len(residues) != 1:
        raise ArithmeticError("CRT reconstruction modulo 10 is not unique")
    r = residues[0]
    return (r, m)


check(
    "the explicit decode map inverts the reading on all 130 surviving "
    "finite-sweep elements",
    all(
        decode(readings[(r, m)]) == (r, m)
        and unit(*(lambda p: (p[0], 2 * p[1]))(decode(readings[(r, m)])))
        == surviving[(r, m)]
        for (r, m) in surviving
    ),
)

check(
    "the window-free decoder also inverts literal readings at m = +-50",
    all(
        decode(reading(r, m)) == (r, m)
        for r in range(10)
        for m in (-50, 50)
    ),
    "20 exact boundary witnesses; decode has no fixed |m| audit window",
)


# ---------- 6. The two finite places as decoder keys ------------------------
q_star = unit(1, -2)

check(
    "q* = zeta_10 phi^-2 = -z J^2 exactly",
    q_star == mul(ZETA10, power(PHI, -2))
    and q_star == neg(mul(Z, power(J, 2))),
)


def order_mod_2(residue):
    identity = (1, 0, 0, 0)

    def multiply_f16(x, y):
        c = [0] * 7
        for i in range(4):
            if x[i]:
                for j in range(4):
                    c[i + j] ^= y[j]
        for degree in (6, 5):
            if c[degree]:
                c[degree - 5] ^= 1
                c[degree] = 0
        if c[4]:
            c[4] = 0
            for i in range(4):
                c[i] ^= 1
        return tuple(c[:4])

    current = identity
    for order in range(1, 16):
        current = multiply_f16(current, residue)
        if current == identity:
            return order
    return None


check(
    "units reduce mod 2 with integer coordinates and q* = zeta_10 phi^-2 "
    "reduces to 1+z of multiplicative order 15 in F_16",
    all(
        all(x.denominator == 1 for x in q)
        for q in family.values()
    )
    and reduce_mod_2(q_star) == (1, 1, 0, 0)
    and order_mod_2(reduce_mod_2(q_star)) == 15,
)

two_adic_table = {
    (r5, m3): reduce_mod_2(unit(r5, 2 * m3))
    for r5 in range(5)
    for m3 in range(3)
}
check(
    "the two-adic key on survivors is exactly the pair (r mod 5, m mod 3): "
    "15 distinct table values matched on the 130-element finite sweep",
    len(set(two_adic_table.values())) == 15
    and all(
        reduce_mod_2(surviving[(r, m)])
        == two_adic_table[(r % 5, m % 3)]
        for (r, m) in surviving
    ),
)

joint_trivial = sorted(
    (r, m)
    for (r, m) in surviving
    if epsilon(surviving[(r, m)]) == 1
    and reduce_mod_2(surviving[(r, m)]) == (1, 0, 0, 0)
)
check(
    "the joint finite kernel on the 130-element sweep matches the powers "
    "of -phi^6 in that window",
    joint_trivial == [(0, -6), (0, 0), (0, 6), (5, -3), (5, 3)]
    and all(
        power(neg(power(PHI, 6)), k) == surviving[key]
        for k, key in (
            (-2, (0, -6)),
            (0, (0, 0)),
            (2, (0, 6)),
            (-1, (5, -3)),
            (1, (5, 3)),
        )
    ),
)


def joint_key(q):
    return (residue_mod_5(q), reduce_mod_2(q))


generator = unit(1, 4)
cycle = []
current = ONE
for _ in range(30):
    cycle.append(joint_key(current))
    current = mul(current, generator)
check(
    "the joint finite readout of g = zeta_10 phi^4 cycles with exact "
    "order 30",
    len(set(cycle)) == 30 and joint_key(current) == cycle[0],
    "the two finite places read exactly the Z/30 quotient",
)


print("\n" + ("ALL CHECKS PASS" if ok else "ONE OR MORE CHECKS FAILED"))
sys.exit(0 if ok else 1)
