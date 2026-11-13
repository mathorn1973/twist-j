"""Exact L1 audit. First execution requires the public preregistration pin."""
from fractions import Fraction
from itertools import product

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
ROOT = (0, 1, 0, 0)
P = (0, 0, 1, 0)
P_INVERSE = (0, 0, 0, 1)
A = (1, -1, 0, 0)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def scale(n, x):
    return tuple(n * a for a in x)


def sub(x, y):
    return add(x, scale(-1, y))


def mul(x, y):
    coefficients = [0] * 7
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            coefficients[i + j] += a * b
    for degree in range(6, 3, -1):
        leading = coefficients[degree]
        for offset in range(1, 5):
            coefficients[degree - offset] -= leading
        coefficients[degree] = 0
    return tuple(coefficients[:4])


def power(x, exponent):
    assert exponent >= 0
    result = ONE
    for _ in range(exponent):
        result = mul(result, x)
    return result


def conjugate(x):
    result = ZERO
    for i, coefficient in enumerate(x):
        result = add(result, scale(coefficient, power(ROOT, (-i) % 5)))
    return result


def hermitian(x):
    return mul(x, conjugate(x))


def q(x):
    numerator = 5 * sum(a * a for a in x) - sum(x) ** 2
    assert numerator % 2 == 0
    return numerator // 2


def admitted(x, y):
    return all(coefficient % 2 == 0 for coefficient in sub(x, y))


def contact(pair, inverse=False):
    x, y = pair
    if not admitted(x, y):
        return pair
    center = tuple(a // 2 for a in add(x, y))
    difference = tuple(a // 2 for a in sub(x, y))
    rotated = mul(P_INVERSE if inverse else P, difference)
    return add(center, rotated), sub(center, rotated)


def iterate_contact(pair, steps):
    for _ in range(steps):
        pair = contact(pair)
    return pair


def modal_accounts(pair):
    x, y = pair
    return Fraction(q(add(x, y)), 2), Fraction(q(sub(x, y)), 2)


def conserved_pair(before, after):
    assert add(*before) == add(*after)
    assert add(hermitian(before[0]), hermitian(before[1])) == add(
        hermitian(after[0]), hermitian(after[1])
    )
    assert sum(map(q, before)) == sum(map(q, after))
    assert modal_accounts(before) == modal_accounts(after)
    assert sum(modal_accounts(before)) == sum(map(q, before))
    assert contact(after, inverse=True) == before
    assert contact(contact(before, inverse=True)) == before
    assert iterate_contact(before, 5) == before


def contact_audit():
    assert power(ROOT, 5) == ONE
    assert mul(P, P_INVERSE) == ONE
    assert q(A) == 5
    assert hermitian(A) == sub(scale(2, ONE), add(ROOT, power(ROOT, 4)))
    assert mul(hermitian(A), hermitian(sub(ONE, P))) == scale(5, ONE)
    phases = tuple(mul(A, power(P, k)) for k in range(5))
    assert len(set(phases)) == 5
    cases = matched = refused = 0
    controls = {3: 0, -3: 0, -1: 0}
    for sign, c, k, r in product((-1, 1), (-3, -1, 1, 3), range(5), range(5)):
        before = (scale(sign, phases[k]), scale(c, phases[r]))
        after = contact(before)
        conserved_pair(before, after)
        assert admitted(*before) == (k == r)
        assert all(abs(coefficient) <= 12 for value in after for coefficient in value)
        if k == r:
            matched += 1
            u = phases[r]
            expected_plus = Fraction(5 * (sign + c) ** 2, 2)
            expected_minus = Fraction(5 * (sign - c) ** 2, 2)
            assert modal_accounts(before) == (expected_plus, expected_minus)
            center = scale((sign + c) // 2, u)
            difference = mul(P, scale((sign - c) // 2, u))
            assert after == (add(center, difference), sub(center, difference))
            gain = Fraction(5 * (c * c - 1), 2)
            assert q(after[0]) - q(before[0]) == gain
            assert q(before[1]) - q(after[1]) == gain
            assert tuple(map(q, after)) == (5 * (1 + c * c) // 2,) * 2
            # Equality in the number field certifies equal real gains in both embeddings.
            embedding_gain = 5 * (c * c - 1) // 4
            assert sub(hermitian(after[0]), hermitian(before[0])) == scale(
                embedding_gain, ONE
            )
            if sign == 1 and c in controls:
                expected_modes = {3: (40, 10), -3: (10, 40), -1: (0, 10)}
                assert modal_accounts(before) == expected_modes[c]
                assert gain == (0 if c == -1 else 20)
                controls[c] += 1
        else:
            refused += 1
            assert after == before
        cases += 1
    assert (cases, matched, refused) == (200, 40, 160)
    assert controls == {3: 5, -3: 5, -1: 5}

    pure_states = 0
    for u in phases:
        symmetric = (u, u)
        antisymmetric = (u, scale(-1, u))
        assert modal_accounts(symmetric) == (10, 0)
        assert modal_accounts(antisymmetric) == (0, 10)
        assert sum(map(q, symmetric)) == sum(map(q, antisymmetric)) == 10
        assert contact(symmetric) == symmetric
        assert contact(antisymmetric) == (mul(P, u), scale(-1, mul(P, u)))
        conserved_pair(symmetric, contact(symmetric))
        conserved_pair(antisymmetric, contact(antisymmetric))
        pure_states += 2
    assert pure_states == 10
    return cases, matched, refused, pure_states


def identity(size):
    return [[int(i == j) for j in range(size)] for i in range(size)]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matmul(left, right):
    assert len(left[0]) == len(right)
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right)))
         for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def matvec(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


def matrix_sub(left, right):
    return [[a - b for a, b in zip(lrow, rrow)] for lrow, rrow in zip(left, right)]


def matrix_power(matrix, exponent):
    result = identity(len(matrix))
    for _ in range(exponent):
        result = matmul(result, matrix)
    return result


def rref(matrix):
    rows = [[Fraction(value) for value in row] for row in matrix]
    width = len(rows[0])
    assert all(len(row) == width for row in rows)
    pivots = []
    pivot_row = 0
    for column in range(width):
        selected = next(
            (i for i in range(pivot_row, len(rows)) if rows[i][column]), None
        )
        if selected is None:
            continue
        rows[pivot_row], rows[selected] = rows[selected], rows[pivot_row]
        divisor = rows[pivot_row][column]
        rows[pivot_row] = [value / divisor for value in rows[pivot_row]]
        for i in range(len(rows)):
            if i == pivot_row or not rows[i][column]:
                continue
            multiplier = rows[i][column]
            rows[i] = [
                a - multiplier * b for a, b in zip(rows[i], rows[pivot_row])
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return rows, pivots


def nullspace(matrix):
    reduced, pivots = rref(matrix)
    width = len(matrix[0])
    basis = []
    for free in range(width):
        if free in pivots:
            continue
        vector = [Fraction(0)] * width
        vector[free] = Fraction(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free]
        assert matvec(matrix, vector) == (0,) * len(matrix)
        basis.append(vector)
    return basis, len(pivots)


def inverse(matrix):
    size = len(matrix)
    unit = identity(size)
    reduced, pivots = rref([row + unit[i] for i, row in enumerate(matrix)])
    assert pivots == list(range(size))
    result = [row[size:] for row in reduced]
    assert matmul(matrix, result) == unit
    assert matmul(result, matrix) == unit
    return result


def determinant(matrix):
    rows = [[Fraction(value) for value in row] for row in matrix]
    result = Fraction(1)
    for column in range(len(rows)):
        selected = next(
            (i for i in range(column, len(rows)) if rows[i][column]), None
        )
        if selected is None:
            return Fraction(0)
        if selected != column:
            rows[column], rows[selected] = rows[selected], rows[column]
            result = -result
        pivot = rows[column][column]
        result *= pivot
        for i in range(column + 1, len(rows)):
            multiplier = rows[i][column] / pivot
            for j in range(column, len(rows)):
                rows[i][j] -= multiplier * rows[column][j]
    return result


def commutator(left, right):
    return matrix_sub(matmul(left, right), matmul(right, left))


def zero_matrix(matrix):
    return all(value == 0 for row in matrix for value in row)


def symmetric_basis(size, skew=False):
    result = []
    for i in range(size):
        for j in range(i + int(skew), size):
            matrix = [[0] * size for _ in range(size)]
            matrix[i][j] = 1
            if i != j:
                matrix[j][i] = -1 if skew else 1
            result.append(matrix)
    return result


def constraints(basis, projectors):
    size = len(projectors[0])
    rows = []
    for projector in projectors:
        brackets = [commutator(matrix, projector) for matrix in basis]
        for i in range(size):
            for j in range(size):
                rows.append([bracket[i][j] for bracket in brackets])
    return rows


def linear_combination(coefficients, basis):
    size = len(basis[0])
    return [
        [sum(c * matrix[i][j] for c, matrix in zip(coefficients, basis))
         for j in range(size)]
        for i in range(size)
    ]


def commutant_audit():
    dimensions = []
    for size in range(2, 6):
        projectors = []
        for edge in range(size - 1):
            vector = [int(i == edge) - int(i == edge + 1) for i in range(size)]
            projector = [
                [Fraction(a * b, 2) for b in vector] for a in vector
            ]
            assert matmul(projector, projector) == projector
            projectors.append(projector)
        real_basis = symmetric_basis(size)
        imaginary_basis = symmetric_basis(size, skew=True)
        assert len(real_basis) == size * (size + 1) // 2
        assert len(imaginary_basis) == size * (size - 1) // 2
        real_kernel, real_rank = nullspace(constraints(real_basis, projectors))
        imaginary_kernel, imaginary_rank = nullspace(
            constraints(imaginary_basis, projectors)
        )
        assert real_rank == len(real_basis) - 2
        assert imaginary_rank == len(imaginary_basis)
        assert len(real_kernel) == 2 and imaginary_kernel == []
        unit = identity(size)
        ones = [[1] * size for _ in range(size)]
        for projector in projectors:
            assert zero_matrix(commutator(unit, projector))
            assert zero_matrix(commutator(ones, projector))
        for coefficients in real_kernel:
            matrix = linear_combination(coefficients, real_basis)
            b = matrix[0][1]
            a = matrix[0][0] - b
            assert matrix == [
                [a * int(i == j) + b for j in range(size)] for i in range(size)
            ]
        dimensions.append((size, len(real_kernel), len(imaginary_kernel)))
    assert dimensions == [(2, 2, 0), (3, 2, 0), (4, 2, 0), (5, 2, 0)]
    return dimensions


def twice_generating(arguments):
    p1, p2, new_q1, new_q2 = arguments
    total = new_q1 + new_q2
    return -2 * p1 * new_q2 + 2 * p2 * total - p2 * p2 - total * total


def generating_derivative(arguments, coordinate):
    plus = list(arguments)
    minus = list(arguments)
    plus[coordinate] += 1
    minus[coordinate] -= 1
    # Central difference is exact for this degree-two polynomial.
    return Fraction(twice_generating(plus) - twice_generating(minus), 4)


def quadratic(matrix, vector):
    return sum(a * b for a, b in zip(vector, matvec(matrix, vector)))


def symplectic_audit():
    omega = [[0, 1, 0, 0], [-1, 0, 1, 0], [0, -1, 0, 1], [0, 0, -1, 0]]
    multiplication = [[0, 0, -1, 1], [0, 0, -1, 0],
                      [1, 0, -1, 0], [0, 1, -1, 0]]
    darboux = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
    canonical = [[0, 0, 1, 0], [0, 0, 0, 1],
                 [-1, 0, 0, 0], [0, -1, 0, 0]]
    step = [[-1, -1, 0, 1], [1, 0, 0, 0],
            [0, -1, 0, 0], [0, -1, 1, 0]]
    gram = [[Fraction(5 * int(i == j) - 1, 2) for j in range(4)]
            for i in range(4)]
    pfaffian = omega[0][1] * omega[2][3] - omega[0][2] * omega[1][3]
    pfaffian += omega[0][3] * omega[1][2]
    assert pfaffian == 1 and determinant(omega) == 1
    assert determinant(darboux) == -1
    assert all(value.denominator == 1 for row in inverse(darboux) for value in row)
    assert matmul(matmul(transpose(darboux), omega), darboux) == canonical
    assert matmul(matmul(inverse(darboux), multiplication), darboux) == step
    assert matmul(matmul(transpose(multiplication), omega), multiplication) == omega
    assert matmul(matmul(transpose(step), canonical), step) == canonical
    assert matrix_power(multiplication, 5) == identity(4)
    assert matrix_power(step, 5) == identity(4)
    assert matmul(matmul(transpose(multiplication), gram), multiplication) == gram
    for column in range(4):
        vector = tuple(int(i == column) for i in range(4))
        assert matvec(multiplication, vector) == mul(P, vector)
    darboux_gram = matmul(matmul(transpose(darboux), gram), darboux)
    assert matmul(matmul(transpose(step), darboux_gram), step) == darboux_gram
    cases = half_integral = 0
    for vector in product(range(-2, 3), repeat=4):
        q1, q2, p1, p2 = vector
        new_q1, new_q2, new_p1, new_p2 = matvec(step, vector)
        arguments = (p1, p2, new_q1, new_q2)
        assert tuple(-generating_derivative(arguments, i) for i in range(2)) == (q1, q2)
        assert tuple(-generating_derivative(arguments, i) for i in range(2, 4)) == (
            new_p1, new_p2
        )
        twice_action = twice_generating(arguments)
        action = Fraction(twice_action, 2)
        assert action.denominator in (1, 2)
        assert twice_action % 2 == q2 % 2
        assert abs(twice_action) <= 44
        assert max(map(abs, matvec(step, vector))) <= 6
        polynomial = matvec(darboux, vector)
        assert q(polynomial) == quadratic(darboux_gram, vector)
        assert (q(polynomial) == 0) == (vector == (0, 0, 0, 0))
        half_integral += action.denominator == 2
        cases += 1
    assert (cases, half_integral) == (625, 250)
    return cases, half_integral


def native_step(triple, inverse=False):
    x, y = contact(triple[:2], inverse=inverse)
    return x, y, triple[2]


def interaction_energy(triple, stiffness):
    return sum(map(q, triple)) + stiffness * q(sub(triple[1], triple[2]))


def funded_step(state, stiffness, inverse=False):
    triple, bank, direction = state
    assert bank >= 0 and direction in (-1, 1)
    travel = -direction if inverse else direction
    candidate = native_step(triple, inverse=(travel == -1))
    next_bank = bank + interaction_energy(triple, stiffness)
    next_bank -= interaction_energy(candidate, stiffness)
    if next_bank < 0:
        return triple, bank, -direction
    return candidate, next_bank, direction


def reverse_direction(state):
    triple, bank, direction = state
    return triple, bank, -direction


def bounded_bank_state(state, stiffness, total):
    triple, bank, direction = state
    assert direction in (-1, 1)
    assert isinstance(bank, int) and 0 <= bank <= 70
    assert all(q(value) == 5 for value in triple)
    assert all(abs(coefficient) <= 2 for value in triple for coefficient in value)
    assert interaction_energy(triple, stiffness) + bank == total
    assert 0 <= total <= 95


def bank_audit():
    phases = tuple(mul(A, power(P, k)) for k in range(5))
    cases = forward_steps = inverse_steps = reflections = 0
    for stiffness, stage, k, r, bank, direction in product(
        (1, 2), (0, 1), range(5), range(5), (0, 5, 10, 20, 40), (-1, 1)
    ):
        triple = (phases[k], scale(-1, phases[r]), phases[r])
        if stage == 1:
            triple = native_step(triple)
        initial = (triple, bank, direction)
        initial_interaction = 10 if stage == 1 and k == r else 20
        assert q(sub(triple[1], triple[2])) == initial_interaction
        total = interaction_energy(triple, stiffness) + bank
        assert total == 15 + initial_interaction * stiffness + bank
        if stage == 1 and k == r and bank == 0 and direction == -1:
            assert funded_step(initial, stiffness) == (triple, 0, 1)
        state = initial
        history = []
        for _ in range(20):
            bounded_bank_state(state, stiffness, total)
            history.append(state)
            successor = funded_step(state, stiffness)
            assert funded_step(successor, stiffness, inverse=True) == state
            predecessor = funded_step(state, stiffness, inverse=True)
            assert funded_step(predecessor, stiffness) == state
            assert predecessor == reverse_direction(
                funded_step(reverse_direction(state), stiffness)
            )
            reflections += successor[2] != state[2]
            state = successor
            forward_steps += 1
        bounded_bank_state(state, stiffness, total)
        for expected in reversed(history):
            state = funded_step(state, stiffness, inverse=True)
            assert state == expected
            bounded_bank_state(state, stiffness, total)
            inverse_steps += 1
        assert state == initial
        cases += 1
    assert (cases, forward_steps, inverse_steps) == (1000, 20000, 20000)
    assert reflections > 0
    controls = 0
    for stiffness in (1, 2):
        triple = (A, scale(-1, A), A)
        rotated = (mul(P, A), scale(-1, mul(P, A)), A)
        assert q(sub(triple[1], triple[2])) == 20
        assert q(sub(rotated[1], rotated[2])) == 10
        assert interaction_energy(triple, stiffness) == 15 + 20 * stiffness
        assert interaction_energy(rotated, stiffness) == 15 + 10 * stiffness
        before = (triple, 0, 1)
        after = funded_step(before, stiffness)
        assert after == (rotated, 10 * stiffness, 1)
        assert funded_step(after, stiffness, inverse=True) == before
        exhausted = (rotated, 0, -1)
        reflected = funded_step(exhausted, stiffness)
        assert reflected == (rotated, 0, 1)
        assert funded_step(reflected, stiffness, inverse=True) == exhausted
        controls += 2
    assert controls == 4
    return cases, forward_steps, inverse_steps, controls


def main():
    contact_counts = contact_audit()
    dimensions = commutant_audit()
    symplectic_counts = symplectic_audit()
    bank_counts = bank_audit()
    print("P-NEUTRAL-RING-MODAL-ACTION-1")
    print("contact cases=%d matched=%d refused=%d pure_mode_states=%d" % contact_counts)
    print("receiver_controls c=3:40,10,20 c=-3:10,40,20 c=-1:0,10,0 phases=5")
    print("commutant " + " ".join("%d:%d,%d" % row for row in dimensions))
    print("darboux cases=%d half_integral_actions=%d" % symplectic_counts)
    print("bank cases=%d forward=%d inverse=%d explicit_controls=%d" % bank_counts)
    print("RESULT PASS")


if __name__ == "__main__":
    main()
