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
    power = [row[:] for row in identity]
    coefficients = [Fr(1)]
    for k in range(1, n + 1):
        power = [
            [
                sum(matrix[i][t] * power[t][j] for t in range(n))
                for j in range(n)
            ]
            for i in range(n)
        ]
        trace = sum(power[i][i] for i in range(n))
        coefficient = -trace / k
        coefficients.append(coefficient)
        for i in range(n):
            power[i][i] += coefficient
    return all(x.denominator == 1 for x in coefficients)


SQRT5 = K(-1, 0, -2, -2)
PHI = smul(Fr(1, 2), add(ONE, SQRT5))


# =============================================================================
# Exact local audit for notes/C-COAXIAL-INTEGRAL-2I-STEP-N/README.md.
#
# Status: NON-CANONICAL, candidate-T / L1. This is not a formal public probe,
# preregistration, two-architecture gate, Canon change, or Registry change.
# Exact arithmetic in Q(zeta_5) is used for every decision. Finite sample
# checks are explicitly labeled AUDIT. Any failed check produces exit status 1.
# =============================================================================
import itertools
import random
import sys
from math import gcd


ok = True


def check(name, condition, extra=""):
    global ok
    ok &= bool(condition)
    print(
        f"[{'PASS' if condition else 'FAIL'}] {name}"
        + (f"   {extra}" if extra else "")
    )


# ---------- 1. The icosian group and the splitting B = K + K e ------------
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


GROUP = {quaternion_key(Q1): Q1}
frontier = [Q1]
while frontier:
    new_frontier = []
    for x in frontier:
        for generator in (OMEGA, Qi, Qj):
            y = quaternion_mul(x, generator)
            if quaternion_key(y) not in GROUP:
                GROUP[quaternion_key(y)] = y
                new_frontier.append(y)
    frontier = new_frontier

check(
    "omega is an icosian with Nrd = 1 and Trd = 1/phi = 2 cos(2 pi/5)",
    reduced_norm(OMEGA) == ONE and add(OMEGA[0], OMEGA[0]) == phi_inverse,
)
check(
    "<omega,i,j> has order 120 and every enumerated element has Nrd = 1",
    len(GROUP) == 120 and all(reduced_norm(v) == ONE for v in GROUP.values()),
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


def matrix_trace(a):
    return add(a[0][0], a[1][1])


def matrix_inv(a):
    determinant_inverse = inv(matrix_det(a))
    return (
        (mul(determinant_inverse, a[1][1]), neg(mul(determinant_inverse, a[0][1]))),
        (neg(mul(determinant_inverse, a[1][0])), mul(determinant_inverse, a[0][0])),
    )


MATRICES = [split_matrix(v) for v in GROUP.values()]
check(
    "M gives 120 distinct matrices of determinant 1 and "
    "M(omega) = diag(z,z^-1)",
    len(set(MATRICES)) == 120
    and all(matrix_det(matrix) == ONE for matrix in MATRICES)
    and split_matrix(OMEGA) == ((Z, ZERO), (ZERO, conj(Z))),
)

group_values = list(GROUP.values())
right_generators = (OMEGA, Qi, Qj)
check(
    "M(gs) = M(g)M(s) on every group element and right generator, "
    "hence M is a faithful representation",
    all(
        split_matrix(quaternion_mul(g, generator))
        == matrix_mul(split_matrix(g), split_matrix(generator))
        for g in group_values
        for generator in right_generators
    ),
)

ZETA10 = neg(mul(Z, mul(Z, Z)))


def power(a, n):
    if n < 0:
        return power(inv(a), -n)
    result = ONE
    for _ in range(n):
        result = mul(result, a)
    return result


def residue_mod_5(a):
    total = sum(a[i] for i in range(4))
    return (
        (total.numerator % 5)
        * pow(total.denominator % 5, -1, 5)
        % 5
    )


# ---------- 2. Direct triangular criterion ---------------------------------
a_F = neg(mul(power(Z, 3), inv(sub(ONE, Z))))
check(
    "a = -z^3/(1-z) is not integral, while (1-z)a is integral",
    (not is_int(a_F)) and is_int(mul(sub(ONE, Z), a_F)),
)

units = [
    mul(power(ZETA10, i), power(PHI, n))
    for i in range(10)
    for n in (-2, -1, 0, 1, 2)
]
criterion_mismatches = sum(
    1
    for q1 in units[:40]
    for q2 in units[:40]
    if is_int(mul(a_F, sub(q1, q2)))
    != (residue_mod_5(q1) == residue_mod_5(q2))
)
check(
    "AUDIT: integrality of a(q1-q2) agrees with q1 = q2 mod p_5",
    criterion_mismatches == 0,
    "1,600 unit pairs, 0 mismatches",
)


# ---------- 3. Trace audit; this is not the proof of the criterion ----------
def all_traces_integral(diagonal):
    return all(
        is_int(matrix_trace(matrix_mul(matrix, diagonal)))
        for matrix in MATRICES
    )


random.seed(0)
trace_mismatches = 0
for q1 in random.sample(units, 25):
    for q2 in random.sample(units, 25):
        diagonal = ((q1, ZERO), (ZERO, q2))
        if all_traces_integral(diagonal) != (
            residue_mod_5(q1) == residue_mod_5(q2)
        ):
            trace_mismatches += 1
check(
    "AUDIT: the trace test agrees with the ramified congruence",
    trace_mismatches == 0,
    "625 seeded unit pairs, 0 mismatches",
)

for exponent, expected in ((-1, False), (-2, True), (-3, False), (-4, True)):
    q = mul(ZETA10, power(PHI, exponent))
    rapidity = 2 * abs(exponent)
    check(
        f"zeta_10 phi^{exponent} at rapidity {rapidity} log phi has "
        f"{'integral' if expected else 'non-integral'} traces",
        all_traces_integral(((q, ZERO), (ZERO, inv(q)))) == expected,
    )

J_candidate = mul(mul(ZETA10, ZETA10), inv(PHI))
check(
    "in the frozen relative placement, diag(J,1) has a non-integral trace",
    not all_traces_integral(((J_candidate, ZERO), (ZERO, ONE))),
)

u = mul(ZETA10, inv(PHI))
u_diagonal = ((u, ZERO), (ZERO, inv(u)))
certificate_traces = [
    matrix_trace(matrix_mul(matrix, u_diagonal)) for matrix in MATRICES
]
exact_certificate = K(Fr(1, 5), Fr(-3, 5), Fr(3, 5), Fr(4, 5))
check(
    "exact D_u certificate (1 - 3z + 3z^2 + 4z^3)/5 occurs among tr(g D_u)",
    exact_certificate in certificate_traces,
)


# ---------- 4. Integral model and the local spanning premise ----------------
nonintegral_matrices = sum(
    1
    for matrix in MATRICES
    if not all(is_int(matrix[i][j]) for i in range(2) for j in range(2))
)
check(
    "the splitting basis has 100 of 120 matrices with a non-integral entry",
    nonintegral_matrices == 100,
)


def split_vector_coordinates(g):
    a0, a1, b0, b1 = solve_coordinates(g)
    return (add(a0, mul(a1, Z)), conj(add(b0, mul(b1, Z))))


all_coordinates = [split_vector_coordinates(v) for v in GROUP.values()]
lattice_basis = None
for i in range(len(all_coordinates)):
    for j in range(len(all_coordinates)):
        candidate = (
            (all_coordinates[i][0], all_coordinates[j][0]),
            (all_coordinates[i][1], all_coordinates[j][1]),
        )
        if matrix_det(candidate) == ZERO:
            continue
        candidate_inverse = matrix_inv(candidate)
        good = True
        for coordinates in all_coordinates:
            first = add(
                mul(candidate_inverse[0][0], coordinates[0]),
                mul(candidate_inverse[0][1], coordinates[1]),
            )
            second = add(
                mul(candidate_inverse[1][0], coordinates[0]),
                mul(candidate_inverse[1][1], coordinates[1]),
            )
            if not (is_int(first) and is_int(second)):
                good = False
                break
        if good:
            lattice_basis = candidate
            break
    if lattice_basis is not None:
        break

expected_b = K(Fr(2, 5), Fr(4, 5), Fr(1, 5), Fr(3, 5))
one_coordinates = split_vector_coordinates(Q1)
i_coordinates = split_vector_coordinates(Qi)
one_i_basis = (
    (one_coordinates[0], i_coordinates[0]),
    (one_coordinates[1], i_coordinates[1]),
)
expected_orbit_basis = ((ONE, a_F), (ZERO, expected_b))
triangular_lattice_basis = (
    lattice_basis is not None
    and lattice_basis == one_i_basis
    and lattice_basis == expected_orbit_basis
)
check(
    "the found orbit basis has the split images of 1 and i as columns and "
    "equals [[1,a],[0,b]] with the stated exact a and b",
    triangular_lattice_basis,
)
if lattice_basis is None:
    sys.exit(1)

lattice_basis_inverse = matrix_inv(lattice_basis)
integral_matrices = []
for matrix in MATRICES:
    left = tuple(
        tuple(
            add(
                mul(lattice_basis_inverse[i][0], matrix[0][j]),
                mul(lattice_basis_inverse[i][1], matrix[1][j]),
            )
            for j in range(2)
        )
        for i in range(2)
    )
    conjugated = tuple(
        tuple(
            add(
                mul(left[i][0], lattice_basis[0][j]),
                mul(left[i][1], lattice_basis[1][j]),
            )
            for j in range(2)
        )
        for i in range(2)
    )
    integral_matrices.append(conjugated)

check(
    "in the lattice basis rho'(2I) is contained in M_2(O_K)",
    sum(
        1
        for matrix in integral_matrices
        if not all(is_int(matrix[i][j]) for i in range(2) for j in range(2))
    )
    == 0,
)

residue_image = {
    tuple(residue_mod_5(matrix[i][j]) for i in range(2) for j in range(2))
    for matrix in integral_matrices
}
check(
    "reduction of rho'(2I) modulo p_5 is injective and has 120 elements",
    len(residue_image) == 120,
)


def rank_mod_5(rows):
    matrix = [list(row) for row in rows]
    rank = 0
    for column in range(4):
        pivot = next(
            (row for row in range(rank, len(matrix)) if matrix[row][column] % 5),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], -1, 5)
        matrix[rank] = [(x * inverse) % 5 for x in matrix[rank]]
        for row in range(len(matrix)):
            if row != rank and matrix[row][column] % 5:
                factor = matrix[row][column]
                matrix[row] = [
                    (x - factor * y) % 5
                    for x, y in zip(matrix[row], matrix[rank])
                ]
        rank += 1
    return rank


check(
    "the F_5-span of reduced rho'(2I) has rank 4, hence equals M_2(F_5)",
    rank_mod_5([list(v) for v in residue_image]) == 4,
)


# ---------- 5. Lattice preservation and the Hermitian identities ------------
q = mul(ZETA10, power(PHI, -2))
q_bar = conj(q)
D = ((q, ZERO), (ZERO, inv(q)))
D_star = ((q_bar, ZERO), (ZERO, inv(q_bar)))


def in_lattice_basis(matrix):
    return matrix_mul(matrix_mul(lattice_basis_inverse, matrix), lattice_basis)


check(
    "D_q, D_q^-1, D_q*, and (D_q*)^-1 all preserve Lambda",
    all(
        all(is_int(x) for row in in_lattice_basis(matrix) for x in row)
        for matrix in (D, matrix_inv(D), D_star, matrix_inv(D_star))
    ),
)

check(
    "D_q* D_q^-1 = diag(z^-1,z) = rho(omega^-1) belongs to 2I",
    matrix_mul(D_star, matrix_inv(D)) == ((conj(Z), ZERO), (ZERO, Z))
    and matrix_mul(D_star, matrix_inv(D)) in set(MATRICES),
)

delta = sub(Z, conj(Z))
check(
    "delta = z - z^-1 satisfies conjugate(delta) = -delta and -delta^2 = 2+phi",
    conj(delta) == neg(delta) and neg(mul(delta, delta)) == add(K(2), PHI),
)

trace_zero_icosians = [v for v in GROUP.values() if v[0] == ZERO]
check(
    "the determinant identity holds on all 30 trace-zero icosians",
    len(trace_zero_icosians) == 30
    and all(
        neg(
            matrix_det(
                tuple(
                    tuple(mul(delta, x) for x in row)
                    for row in split_matrix(v)
                )
            )
        )
        == mul(add(K(2), PHI), reduced_norm(v))
        for v in trace_zero_icosians
    ),
)

vertex_norm = add(mul(ONE, ONE), mul(PHI, PHI))
check(
    "the quadratic norm of the vertex (0,1,phi) is 2+phi",
    vertex_norm == add(K(2), PHI),
)


# ---------- 6. The place above two ------------------------------------------
def reduce_mod_2(a):
    if not all(coefficient.denominator % 2 == 1 for coefficient in a):
        raise ArithmeticError("a denominator is not invertible modulo 2")
    return tuple(
        coefficient.numerator
        * pow(coefficient.denominator, -1, 2)
        % 2
        for coefficient in a
    )


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


q_mod_2 = reduce_mod_2(q)
power_mod_2 = q_mod_2
order_mod_2 = 1
while power_mod_2 != (1, 0, 0, 0):
    power_mod_2 = multiply_f16(power_mod_2, q_mod_2)
    order_mod_2 += 1

check(
    "q mod 2 = 1+z has order 15 in F_16^x, so a two-adic selector remains open",
    q_mod_2 == (1, 1, 0, 0) and order_mod_2 == 15,
)


# ---------- 7. The lattices O^0 and L ---------------------------------------
def to_real_quadratic(a):
    if not (a[1] == 0 and a[2] == a[3]):
        raise ArithmeticError("element is not in F")
    return (a[0], -a[2])


pure_quaternions = [
    (g[1], g[2], g[3]) for g in GROUP.values() if g[0] == ZERO
]
vertices = []
for coordinate in range(3):
    for sign_1 in (1, -1):
        for sign_2 in (1, -1):
            vertex = [ZERO, ZERO, ZERO]
            vertex[(coordinate + 1) % 3] = smul(sign_1, ONE)
            vertex[(coordinate + 2) % 3] = smul(sign_2, PHI)
            vertices.append(tuple(vertex))


def integer_rows(generators):
    rows = []
    for vector in generators:
        for scaled in (vector, tuple(mul(PHI, coefficient) for coefficient in vector)):
            row = []
            for coefficient in scaled:
                row.extend(to_real_quadratic(coefficient))
            rows.append(row)
    return rows


def clear_denominators(rows):
    denominator = 1
    for row in rows:
        for coefficient in row:
            denominator = (
                denominator
                * coefficient.denominator
                // gcd(denominator, coefficient.denominator)
            )
    scaled_rows = [
        [coefficient * denominator for coefficient in row] for row in rows
    ]
    if not all(
        coefficient.denominator == 1
        for row in scaled_rows
        for coefficient in row
    ):
        raise ArithmeticError("the common denominator did not clear all rows")
    return [[int(coefficient) for coefficient in row] for row in scaled_rows], denominator


def row_lattice_basis(matrix, columns=6):
    """Unimodular Euclidean row reduction for this full-rank integer input."""
    matrix = [row[:] for row in matrix if any(row)]
    rank = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(rank, len(matrix)) if matrix[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        changed = True
        while changed:
            changed = False
            for row in range(rank + 1, len(matrix)):
                if matrix[row][column] != 0:
                    quotient = matrix[row][column] // matrix[rank][column]
                    matrix[row] = [
                        x - quotient * y
                        for x, y in zip(matrix[row], matrix[rank])
                    ]
                    if matrix[row][column] != 0:
                        matrix[rank], matrix[row] = matrix[row], matrix[rank]
                        changed = True
        rank += 1
    return matrix[:rank]


O0_rows, O0_denominator = clear_denominators(integer_rows(pure_quaternions))
L_rows, L_denominator = clear_denominators(integer_rows(vertices))
order_rows, order_denominator = clear_denominators(integer_rows(GROUP.values()))
common_denominator = 1
for denominator in (O0_denominator, L_denominator, order_denominator):
    common_denominator = (
        common_denominator
        * denominator
        // gcd(common_denominator, denominator)
    )
O0_rows = [
    [coefficient * (common_denominator // O0_denominator) for coefficient in row]
    for row in O0_rows
]
L_rows = [
    [coefficient * (common_denominator // L_denominator) for coefficient in row]
    for row in L_rows
]
order_rows = [
    [
        coefficient * (common_denominator // order_denominator)
        for coefficient in row
    ]
    for row in order_rows
]
O0_basis = row_lattice_basis(O0_rows)
L_basis = row_lattice_basis(L_rows)
order_basis = row_lattice_basis(order_rows, columns=8)


def exact_determinant(matrix):
    matrix = [[Fr(x) for x in row] for row in matrix]
    n = len(matrix)
    determinant = Fr(1)
    for column in range(n):
        pivot = next(
            (row for row in range(column, n) if matrix[row][column] != 0),
            None,
        )
        if pivot is None:
            return Fr(0)
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            determinant = -determinant
        determinant *= matrix[column][column]
        pivot_value = matrix[column][column]
        matrix[column] = [x / pivot_value for x in matrix[column]]
        for row in range(column + 1, n):
            if matrix[row][column] != 0:
                factor = matrix[row][column]
                matrix[row] = [
                    x - factor * y
                    for x, y in zip(matrix[row], matrix[column])
                ]
    return determinant


def row_coordinates(basis, vector):
    vector = [Fr(x) for x in vector]
    coordinates = [Fr(0)] * len(basis)
    for index, row in enumerate(basis):
        leading = next(
            (position for position in range(len(vector)) if row[position] != 0),
            None,
        )
        if leading is None:
            continue
        if vector[leading] != 0:
            quotient = vector[leading] / row[leading]
            coordinates[index] = quotient
            vector = [a - quotient * b for a, b in zip(vector, row)]
    return coordinates, vector


def is_integrally_contained(source_basis, target_basis):
    for row in source_basis:
        coordinates, remainder = row_coordinates(target_basis, row)
        if any(remainder) or any(
            coordinate.denominator != 1 for coordinate in coordinates
        ):
            return False
    return True


order_leading_positions = [
    next((index for index, value in enumerate(row) if value != 0), None)
    for row in order_basis
]
order_has_full_echelon_basis = (
    len(order_basis) == 8 and order_leading_positions == list(range(8))
)
order_trace_kernel_basis = (
    [row[2:] for row in order_basis[2:]]
    if order_has_full_echelon_basis
    else []
)
pure_span_is_full_trace_kernel = (
    order_has_full_echelon_basis
    and len(order_trace_kernel_basis) == 6
    and is_integrally_contained(O0_basis, order_trace_kernel_basis)
    and is_integrally_contained(order_trace_kernel_basis, O0_basis)
)
check(
    "the R-span of the 30 trace-zero icosians equals the trace-zero kernel "
    "O^0 of the full icosian order",
    pure_span_is_full_trace_kernel,
)

L_is_contained_in_O0 = (
    len(O0_basis) == 6
    and len(L_basis) == 6
    and is_integrally_contained(L_basis, O0_basis)
)
check(
    "L is contained in O^0 and both have Z-rank 6, hence R-rank 3",
    L_is_contained_in_O0,
)
if not (pure_span_is_full_trace_kernel and L_is_contained_in_O0):
    sys.exit(1)

check(
    "the integer index [O^0:L] is 16",
    abs(exact_determinant(L_basis) / exact_determinant(O0_basis)) == 16,
)


inclusion_coordinates = [row_coordinates(O0_basis, row)[0] for row in L_basis]
inclusion_matrix = [
    [int(coordinate) for coordinate in row]
    for row in inclusion_coordinates
]


def determinantal_divisor(matrix, size):
    divisor = 0
    for row_indices in itertools.combinations(range(len(matrix)), size):
        for column_indices in itertools.combinations(range(len(matrix[0])), size):
            minor = [
                [matrix[row][column] for column in column_indices]
                for row in row_indices
            ]
            determinant = exact_determinant(minor)
            if determinant.denominator != 1:
                raise ArithmeticError("an inclusion minor is not integral")
            divisor = gcd(divisor, abs(determinant.numerator))
    return divisor


determinantal_divisors = [
    determinantal_divisor(inclusion_matrix, size) for size in range(1, 7)
]
invariant_factors = [determinantal_divisors[0]] + [
    determinantal_divisors[index] // determinantal_divisors[index - 1]
    for index in range(1, 6)
]
check(
    "integer determinantal divisors are (1,1,2,4,8,16), hence the Smith "
    "factors are (1,1,2,2,2,2) and O^0/L = (Z/2)^4",
    determinantal_divisors == [1, 1, 2, 4, 8, 16]
    and invariant_factors == [1, 1, 2, 2, 2, 2],
    f"divisors = {determinantal_divisors}; factors = {invariant_factors}",
)


print("\n" + ("ALL CHECKS PASS" if ok else "ONE OR MORE CHECKS FAILED"))
sys.exit(0 if ok else 1)
