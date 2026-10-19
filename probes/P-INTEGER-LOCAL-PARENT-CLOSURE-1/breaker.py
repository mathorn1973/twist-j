#!/usr/bin/env python3
"""Independent exact audit of the local parent and regular-chart completion.

Prospective code: no execution or import before the public pin.
Encoding: six-component physical rows, immutable native coordinate tuples,
dual differentiation, rational polynomial coefficients, and full temporal
matrices with pivoted Gaussian elimination. Standard library only.
"""

from fractions import Fraction as F
from hashlib import sha256
from math import gcd, lcm
from pathlib import Path
import sys


PROBE = "P-INTEGER-LOCAL-PARENT-CLOSURE-1"
M = 324
G = F(1, M)
ELL = (1, -1, 0, 0, 0)
SIGMA = (F(1, 2), F(1, 2), F(0), F(0), F(0))
EDGES = tuple((r, (r + length) % 5, 29 if length == 1 else 65)
              for length in (1, 2) for r in range(5))
VBASIS = tuple(tuple(int(r == i) - int(r == 4) for r in range(5))
               for i in range(4))
KBASIS = (
    (1, 1, 1, 1, 1, 0, 0, 0, 0, 0),
    (-1, -1, 0, 0, 0, 1, 0, 0, 0, 0),
    (0, -1, -1, 0, 0, 0, 1, 0, 0, 0),
    (0, 0, -1, -1, 0, 0, 0, 1, 0, 0),
    (0, 0, 0, -1, -1, 0, 0, 0, 1, 0),
    (-1, 0, 0, 0, -1, 0, 0, 0, 0, 1),
)
PHYSICAL, THETA, TERMINAL, SHIFT, TAU, CYCLE = range(6)
AUTHORITY = (
    ("CANON.md", 1052518, "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
    ("CORE.md", 30714, "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
    ("FRONTIER.md", 27382, "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
    ("REGISTRY.tsv", 532811, "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
    ("CHANGELOG.md", 207770, "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
)
FALSIFIERS = frozenset((
    "AUTHORITY", "DOMAIN", "PARENT_VARIATION", "CUBIC_COMPLETION",
    "LOCAL_RECONSTRUCTION", "CHART_INVERSE", "FINITE_GAUGE", "NOETHER",
    "COMMUTATOR", "INTEGER_GAUGE", "AUXILIARY_RANK", "STATIONARY_EQUATIONS",
    "WITNESSES", "NEGATIVE_CONTROLS", "CERTIFICATE", "BREAKER_BYTES",
))


class ScientificFailure(Exception):
    def __init__(self, key):
        if key not in FALSIFIERS:
            raise ValueError("unregistered falsifier")
        self.key = key
        super().__init__(key)


def require(condition, key):
    if not condition:
        raise ScientificFailure(key)


class SingularChart(Exception):
    """An exact mathematical obstruction, separate from scientific failure."""


class Dual:
    """Exact value and one nilpotent tangent coefficient."""

    __slots__ = ("value", "tangent")

    def __init__(self, value, tangent=0):
        self.value = F(value)
        self.tangent = F(tangent)

    @staticmethod
    def promote(other):
        return other if isinstance(other, Dual) else Dual(other)

    def __add__(self, other):
        other = self.promote(other)
        return Dual(self.value + other.value, self.tangent + other.tangent)

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, -self.tangent)

    def __sub__(self, other):
        return self + (-self.promote(other))

    def __rsub__(self, other):
        return self.promote(other) - self

    def __mul__(self, other):
        other = self.promote(other)
        return Dual(self.value * other.value,
                    self.tangent * other.value + self.value * other.tangent)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.promote(other)
        return Dual(self.value / other.value,
                    (self.tangent * other.value - self.value * other.tangent)
                    / other.value ** 2)

    def __rtruediv__(self, other):
        return self.promote(other) / self

    def __pow__(self, exponent):
        if type(exponent) is not int or exponent < 0:
            raise ValueError("nonnegative integer powers only")
        if exponent == 0:
            return Dual(1)
        return Dual(self.value ** exponent,
                    exponent * self.value ** (exponent - 1) * self.tangent)


class Polynomial:
    """A univariate polynomial over Q, independently retaining every degree."""

    __slots__ = ("coefficients",)

    def __init__(self, coefficients):
        values = [F(v) for v in coefficients]
        while len(values) > 1 and values[-1] == 0:
            values.pop()
        self.coefficients = tuple(values or [F(0)])

    @staticmethod
    def promote(value):
        return value if isinstance(value, Polynomial) else Polynomial((value,))

    def coefficient(self, degree):
        return self.coefficients[degree] if degree < len(self.coefficients) else F(0)

    def __add__(self, other):
        other = self.promote(other)
        size = max(len(self.coefficients), len(other.coefficients))
        return Polynomial(tuple(self.coefficient(i) + other.coefficient(i)
                                for i in range(size)))

    __radd__ = __add__

    def __neg__(self):
        return Polynomial(tuple(-v for v in self.coefficients))

    def __sub__(self, other):
        return self + (-self.promote(other))

    def __rsub__(self, other):
        return self.promote(other) - self

    def __mul__(self, other):
        other = self.promote(other)
        result = [F(0)] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i, left in enumerate(self.coefficients):
            for j, right in enumerate(other.coefficients):
                result[i + j] += left * right
        return Polynomial(result)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = F(other)
        return Polynomial(tuple(value / other for value in self.coefficients))

    def __pow__(self, exponent):
        if type(exponent) is not int or exponent < 0:
            raise ValueError("nonnegative integer powers only")
        answer = Polynomial((1,))
        for _ in range(exponent):
            answer = answer * self
        return answer


def dot(left, right):
    return sum(x * y for x, y in zip(left, right))


def plus(left, right):
    return tuple(x + y for x, y in zip(left, right))


def minus(left, right):
    return tuple(x - y for x, y in zip(left, right))


def scaled(factor, vector):
    return tuple(factor * x for x in vector)


def incidence(vertex):
    return tuple(vertex[head] - vertex[tail] for tail, head, _ in EDGES)


def divergence(edge):
    result = [0] * 5
    for value, (tail, head, _) in zip(edge, EDGES):
        result[tail] -= value
        result[head] += value
    return tuple(result)


def weighted(edge):
    return tuple(F(weight, M) * value for value, (_, _, weight) in zip(edge, EDGES))


def laplacian(vertex):
    return divergence(weighted(incidence(vertex)))


def zero_rows(horizon, width):
    return tuple((F(0),) * width for _ in range(horizon + 1))


def native_zero(horizon):
    return (zero_rows(horizon, 6), zero_rows(horizon, 5), (F(0),) * 5,
            zero_rows(horizon, 10), zero_rows(horizon, 5), zero_rows(horizon, 10))


def native_map(function, *states):
    result = []
    for sector in range(6):
        if sector == TERMINAL:
            result.append(tuple(function(*values) for values in zip(*(s[sector] for s in states))))
        else:
            result.append(tuple(tuple(function(*values) for values in zip(*rows))
                                for rows in zip(*(s[sector] for s in states))))
    return tuple(result)


def native_add(state, direction, factor=1):
    return native_map(lambda x, d: x + factor * d, state, direction)


def native_dual(state, direction):
    return native_map(Dual, state, direction)


def native_values(state):
    for sector in range(6):
        if sector == TERMINAL:
            yield from state[sector]
        else:
            for row in state[sector]:
                yield from row


def physical_action(trajectory, a):
    horizon = len(trajectory) - 1
    result = 0
    for b in range(1, horizon + 1):
        delta = minus(trajectory[b], trajectory[b - 1])
        result += dot(delta, delta) / F(2)
    for n in range(1, horizon):
        h, c = trajectory[n][:5], trajectory[n][5]
        result += (-dot(h, laplacian(h)) / F(2) - c * c / F(2)
                   + F(a, 4) * c + G * c * dot(ELL, h))
    return result


def bond_density(trajectory, bond, a):
    previous, current = trajectory[bond - 1], trajectory[bond]
    hc, hp = current[:5], previous[:5]
    cc, cp = current[5], previous[5]
    result = [(hc[r] - hp[r]) ** 2 / F(2) for r in range(5)]
    bc, bp = incidence(hc), incidence(hp)
    for k, (tail, head, weight) in enumerate(EDGES):
        contribution = F(weight, 4 * M) * bc[k] * bp[k]
        result[tail] += contribution
        result[head] += contribution
    source = (cc - cp) ** 2 / F(2) + cc * cp / F(2) - F(a, 8) * (cc + cp)
    for r in range(5):
        result[r] += SIGMA[r] * source - G * F(ELL[r], 2) * (cp * hc[r] + cc * hp[r])
    return tuple(result)


def edge_current(trajectory, time):
    h = trajectory[time][:5]
    q = minus(trajectory[time + 1], trajectory[time - 1])
    bh = incidence(h)
    result = [F(weight, 4 * M) * bh[k] * (q[tail] + q[head])
              for k, (tail, head, weight) in enumerate(EDGES)]
    result[0] -= G * q[5] * (h[0] + h[1]) / F(4)
    return tuple(result)


def energy_offset(a):
    return F(4342005, 8683757) * F(a, 4) ** 2


def residual_arrays(state):
    horizon = len(state[PHYSICAL]) - 1
    mu = list(zero_rows(horizon, 5))
    mu[horizon] = state[TERMINAL]
    return tuple(mu), state[SHIFT]


def reconstruct_multipliers(state):
    horizon = len(state[PHYSICAL]) - 1
    theta = state[THETA]
    mu = [(F(0),) * 5]
    mu += [minus(theta[b], theta[b - 1]) for b in range(1, horizon)]
    mu.append(minus(state[TERMINAL], theta[horizon - 1]))
    shift = list(zero_rows(horizon, 10))
    for n in range(1, horizon):
        shift[n] = plus(state[SHIFT][n], incidence(theta[n]))
    return tuple(mu), tuple(shift)


def auxiliary_action(mu, shift, tau, cycle):
    horizon = len(tau) - 1
    result = sum(2 * dot(mu[b], laplacian(tau[b])) for b in range(1, horizon + 1))
    for n in range(1, horizon):
        result += 2 * dot(shift[n], plus(weighted(incidence(minus(tau[n + 1], tau[n]))), cycle[n]))
    return result


def interaction_action(trajectory, mu, shift, a, e_hom):
    horizon = len(trajectory) - 1
    offset = (energy_offset(a) - e_hom) / F(5)
    result = 0
    for b in range(1, horizon + 1):
        density = tuple(value + offset for value in bond_density(trajectory, b, a))
        result -= dot(mu[b], density)
    for n in range(1, horizon):
        result += dot(shift[n], edge_current(trajectory, n))
    return result


def parent_action(state, a, e_hom, epsilon):
    mu, shift = residual_arrays(state)
    return (physical_action(state[PHYSICAL], a)
            + auxiliary_action(mu, shift, state[TAU], state[CYCLE])
            + epsilon * interaction_action(state[PHYSICAL], mu, shift, a, e_hom))


def field_generator(trajectory, theta):
    horizon = len(trajectory) - 1
    result = list(zero_rows(horizon, 6))
    for n in range(1, horizon):
        parameters = theta[n] + (dot(SIGMA, theta[n]),)
        delta = minus(trajectory[n + 1], trajectory[n - 1])
        result[n] = tuple(parameters[i] * delta[i] / F(2) for i in range(6))
    return tuple(result)


def physical_add(trajectory, direction, factor=1):
    return tuple(tuple(x + factor * v for x, v in zip(row, tangent))
                 for row, tangent in zip(trajectory, direction))


def dress_fields(trajectory, theta, epsilon):
    return physical_add(trajectory, field_generator(trajectory, theta), -epsilon)


def completed_action(old_state, a, e_hom, epsilon):
    dressed = list(old_state)
    dressed[PHYSICAL] = dress_fields(old_state[PHYSICAL], old_state[THETA], epsilon)
    return parent_action(tuple(dressed), a, e_hom, epsilon)


def full_generator_matrix(theta):
    horizon = len(theta) - 1
    size = 6 * (horizon + 1)
    matrix = [[F(0)] * size for _ in range(size)]
    for n in range(1, horizon):
        parameters = theta[n] + (dot(SIGMA, theta[n]),)
        for component in range(6):
            row = 6 * n + component
            matrix[row][6 * (n + 1) + component] = parameters[component] / F(2)
            matrix[row][6 * (n - 1) + component] = -parameters[component] / F(2)
    return tuple(tuple(row) for row in matrix)


def full_k_matrix(theta, epsilon):
    matrix = full_generator_matrix(theta)
    return tuple(tuple(F(int(i == j)) - epsilon * value for j, value in enumerate(row))
                 for i, row in enumerate(matrix))


def matrix_vector(matrix, vector):
    return tuple(dot(row, vector) for row in matrix)


def physical_flat(trajectory):
    return tuple(value for row in trajectory for value in row)


def physical_rows(vector):
    return tuple(tuple(vector[i:i + 6]) for i in range(0, len(vector), 6))


def row_reduction(matrix, right=None):
    """Full pivoted rational elimination, retaining rank, determinant, and RHS."""
    differentiating = any(isinstance(value, Dual) for row in matrix for value in row)
    differentiating = differentiating or (right is not None and any(isinstance(value, Dual) for value in right))
    promote = Dual.promote if differentiating else F
    rows = [list(map(promote, row)) for row in matrix]
    columns = len(rows[0]) if rows else 0
    nrows = len(rows)
    if right is not None:
        for row, value in zip(rows, right):
            row.append(promote(value))
    rank = 0
    determinant = F(1)
    pivots = []
    nonzero_entry = (lambda value: value.value != 0 or value.tangent != 0) if differentiating else (lambda value: value != 0)
    for column in range(columns):
        pivot = next((r for r in range(rank, nrows)
                      if (rows[r][column].value if differentiating else rows[r][column]) != 0), None)
        if pivot is None:
            continue
        if pivot != rank:
            rows[rank], rows[pivot] = rows[pivot], rows[rank]
            determinant = -determinant
        value = rows[rank][column]
        determinant *= value
        active = [j for j, entry in enumerate(rows[rank]) if nonzero_entry(entry)]
        for j in active:
            rows[rank][j] = rows[rank][j] / value
        for r in range(nrows):
            factor = rows[r][column]
            if r != rank and nonzero_entry(factor):
                for j in active:
                    rows[r][j] = rows[r][j] - factor * rows[rank][j]
        pivots.append(column)
        rank += 1
        if rank == nrows:
            break
    if nrows != columns or rank != columns:
        determinant = F(0)
    return tuple(tuple(row) for row in rows), tuple(pivots), determinant


def rational_solve(matrix, right):
    reduced, pivots, determinant = row_reduction(matrix, right)
    if len(pivots) != len(matrix):
        raise SingularChart("singular chart")
    return tuple(row[-1] for row in reduced), determinant


def chart_reconstruct(native, epsilon):
    vector, determinant = rational_solve(full_k_matrix(native[THETA], epsilon),
                                         physical_flat(native[PHYSICAL]))
    old = list(native)
    old[PHYSICAL] = physical_rows(vector)
    return tuple(old), determinant


def exact_chart_direction(old, psi, epsilon):
    rhs = scaled(epsilon, physical_flat(field_generator(old[PHYSICAL], psi)))
    vector, determinant = rational_solve(full_k_matrix(old[THETA], epsilon), rhs)
    direction = list(native_zero(len(psi) - 1))
    direction[PHYSICAL] = physical_rows(vector)
    direction[THETA] = psi
    return tuple(direction), determinant


def exact_chart_translate(old, psi, epsilon):
    native = list(old)
    native[PHYSICAL] = dress_fields(old[PHYSICAL], old[THETA], epsilon)
    native[THETA] = tuple(plus(row, shift) for row, shift in zip(old[THETA], psi))
    return chart_reconstruct(tuple(native), epsilon)


def chart_lie_bracket(old, psi, eta, epsilon):
    """Differentiate complete matrix solves using Dual elimination."""
    left, _ = exact_chart_direction(old, psi, epsilon)
    right, _ = exact_chart_direction(old, eta, epsilon)
    differentiated_right, _ = exact_chart_direction(native_dual(old, left), eta, epsilon)
    differentiated_left, _ = exact_chart_direction(native_dual(old, right), psi, epsilon)
    tangent = lambda value: value.tangent if isinstance(value, Dual) else F(0)
    return native_add(native_map(tangent, differentiated_right),
                      native_map(tangent, differentiated_left), -1)


def parent_derivative(state, direction, a, e_hom, epsilon):
    value = parent_action(native_dual(state, direction), a, e_hom, epsilon)
    return value.tangent if isinstance(value, Dual) else F(0)


def completed_derivative(old, direction, a, e_hom, epsilon):
    value = completed_action(native_dual(old, direction), a, e_hom, epsilon)
    return value.tangent if isinstance(value, Dual) else F(0)


def completed_coefficients(old, a, e_hom):
    value = completed_action(old, a, e_hom, Polynomial((0, 1)))
    return Polynomial.promote(value).coefficients


def normalized_encoding(numerators, denominator):
    if type(denominator) is not int or denominator < 1:
        raise ValueError("positive integer denominator required")
    divisor = denominator
    for value in independent_values(numerators, True):
        if F(value).denominator != 1:
            raise ValueError("integer numerator required")
        divisor = gcd(divisor, int(value))
    return native_map(lambda value: int(value) // divisor, numerators), denominator // divisor


def encode_native(state):
    denominator = 1
    for value in independent_values(state, True):
        denominator = lcm(denominator, F(value).denominator)
    def integer_numerator(value):
        scaled_value = F(value) * denominator
        require(scaled_value.denominator == 1, "INTEGER_GAUGE")
        return scaled_value.numerator
    numerators = native_map(integer_numerator, state)
    return normalized_encoding(numerators, denominator)


def decode_native(numerators, denominator):
    return native_map(lambda value: F(value, denominator), numerators)


def translate_integer(numerators, denominator, parameter_numerators, parameter_denominator):
    if type(parameter_denominator) is not int or parameter_denominator < 1:
        raise ValueError("positive integer parameter denominator required")
    result = list(native_map(lambda value: parameter_denominator * value, numerators))
    result[THETA] = tuple(tuple(value + denominator * omega for value, omega in zip(row, parameter))
                          for row, parameter in zip(result[THETA], parameter_numerators))
    return normalized_encoding(tuple(result), denominator * parameter_denominator)


def translate_native(state, parameter):
    result = list(state)
    result[THETA] = tuple(plus(row, change) for row, change in zip(state[THETA], parameter))
    return tuple(result)


def auxiliary_equations(r, nu, horizon):
    """Derivatives of the bilinear auxiliary action in admissible tau,p bases."""
    equations = []
    for n in range(1, horizon):
        equations.extend(2 * dot(nu[n], basis) for basis in KBASIS)
    for b in range(1, horizon + 1):
        previous = nu[b - 1] if b > 1 else (F(0),) * 10
        current = nu[b] if b < horizon else (F(0),) * 10
        covector = divergence(weighted(minus(previous, current)))
        if b == horizon:
            covector = plus(covector, laplacian(r))
        equations.extend(2 * dot(covector, basis) for basis in VBASIS)
    return tuple(equations)


def auxiliary_matrix(horizon):
    columns = []
    for r in range(5):
        unit = tuple(F(int(i == r)) for i in range(5))
        columns.append(auxiliary_equations(unit, zero_rows(horizon, 10), horizon))
    for n in range(1, horizon):
        for k in range(10):
            nu = list(zero_rows(horizon, 10))
            nu[n] = tuple(F(int(i == k)) for i in range(10))
            columns.append(auxiliary_equations((F(0),) * 5, tuple(nu), horizon))
    return tuple(tuple(column[r] for column in columns) for r in range(len(columns[0])))


def quartic_invariant(trajectory):
    return sum(value ** 4 for row in trajectory[1:-1] for value in row[:5])


def replace_row(state, sector, time, row):
    result = list(state)
    rows = list(state[sector])
    rows[time] = tuple(row)
    result[sector] = tuple(rows)
    return tuple(result)


def coordinate_directions(horizon):
    result = []
    for sector, width in ((PHYSICAL, 6), (THETA, 5)):
        for n in range(1, horizon):
            for j in range(width):
                result.append(replace_row(native_zero(horizon), sector, n,
                                          tuple(F(int(i == j)) for i in range(width))))
    for j in range(5):
        state = list(native_zero(horizon))
        state[TERMINAL] = tuple(F(int(i == j)) for i in range(5))
        result.append(tuple(state))
    for n in range(1, horizon):
        for k in range(10):
            result.append(replace_row(native_zero(horizon), SHIFT, n,
                                      tuple(F(int(i == k)) for i in range(10))))
    for sector, times, basis in ((TAU, range(1, horizon + 1), VBASIS),
                                  (CYCLE, range(1, horizon), KBASIS)):
        for n in times:
            for vector in basis:
                result.append(replace_row(native_zero(horizon), sector, n, vector))
    return tuple(result)


def independent_values(state, include_endpoints=False):
    horizon = len(state[PHYSICAL]) - 1
    physical_times = range(horizon + 1) if include_endpoints else range(1, horizon)
    for n in physical_times:
        yield from state[PHYSICAL][n]
    for n in range(1, horizon):
        yield from state[THETA][n]
    yield from state[TERMINAL]
    for n in range(1, horizon):
        yield from state[SHIFT][n]
    for b in range(1, horizon + 1):
        yield from state[TAU][b][:4]
    for n in range(1, horizon):
        row = state[CYCLE][n]
        yield row[0] + row[5] + row[9]
        yield from row[5:10]


def fixture_integer(n, j, channel, a, seed):
    return ((17 * n + 11 * j + 7 * seed + 5 * a + 3 * channel) % 19) - 9


def configuration(a, seed, horizon=5):
    state = list(native_zero(horizon))
    state[PHYSICAL] = tuple(tuple(F(fixture_integer(n, j, 0, a, seed), 60)
                                   for j in range(6)) for n in range(horizon + 1))
    for sector, width, channel in ((THETA, 5, 1), (SHIFT, 10, 3)):
        rows = list(state[sector])
        for n in range(1, horizon):
            rows[n] = tuple(F(fixture_integer(n, j, channel, a, seed), 60) for j in range(width))
        state[sector] = tuple(rows)
    state[TERMINAL] = tuple(F(fixture_integer(5, j, 2, a, seed), 60) for j in range(5))
    for sector, times, basis, channel in ((TAU, range(1, horizon + 1), VBASIS, 4),
                                          (CYCLE, range(1, horizon), KBASIS, 5)):
        rows = list(state[sector])
        for n in times:
            rows[n] = tuple(sum(F(fixture_integer(n, j, channel, a, seed), 60) * basis[j][k]
                                for j in range(len(basis))) for k in range(len(basis[0])))
        state[sector] = tuple(rows)
    return tuple(state), F(seed + 1, 7 + a * a)


def parameters(a, seed, horizon=5):
    result = []
    for n in range(1, horizon):
        for r in range(5):
            rows = list(zero_rows(horizon, 5))
            rows[n] = tuple(int(i == r) for i in range(5))
            result.append((tuple(rows), 16))
    rows = [(0,) * 5]
    rows += [tuple(fixture_integer(n, r, 6, a, seed) for r in range(5))
             for n in range(1, horizon)]
    rows.append((0,) * 5)
    result.append((tuple(rows), 112))
    return tuple(result)


def decode_parameter(numerators, denominator):
    return tuple(tuple(F(value, denominator) for value in row) for row in numerators)


def domain_check(state):
    horizon = len(state[PHYSICAL]) - 1
    require(state[THETA][0] == (0,) * 5 and state[THETA][horizon] == (0,) * 5, "DOMAIN")
    require(all(sum(row) == 0 for row in state[TAU]), "DOMAIN")
    require(all(divergence(row) == (0,) * 5 for row in state[CYCLE]), "DOMAIN")
    require(len(tuple(independent_values(state))) == 31 * horizon - 22, "DOMAIN")
    require(len(tuple(independent_values(state, True))) == 31 * horizon - 10, "DOMAIN")


def physical_directional(function, trajectory, direction):
    dual_trajectory = tuple(tuple(Dual(value, tangent) for value, tangent in zip(row, drow))
                            for row, drow in zip(trajectory, direction))
    value = function(dual_trajectory)
    return value.tangent if isinstance(value, Dual) else F(0)


def physical_polynomial(function, trajectory, direction):
    line = physical_add(trajectory, direction, Polynomial((0, 1)))
    return Polynomial.promote(function(line))


def inherited_coefficients(old, a, e_hom):
    """Independent #1658 form (3.7b), plus direct polynomial Hessian of I."""
    x, theta = old[PHYSICAL], old[THETA]
    mu, shift = reconstruct_multipliers(old)
    residual_mu, residual_shift = residual_arrays(old)
    first = field_generator(x, theta)
    second = field_generator(first, theta)
    a_function = lambda trajectory: physical_action(trajectory, a)
    i_function = lambda trajectory: interaction_action(trajectory, mu, shift, a, e_hom)
    residual_i = lambda trajectory: interaction_action(trajectory, residual_mu, residual_shift, a, e_hom)
    s0 = physical_action(x, a) + auxiliary_action(mu, shift, old[TAU], old[CYCLE])
    s1 = i_function(x)
    s2 = (-physical_directional(i_function, x, first)
          - physical_polynomial(a_function, x, first).coefficient(2)
          - physical_directional(a_function, x, second))
    s3 = physical_polynomial(residual_i, x, first).coefficient(2)
    return s0, s1, s2, s3


def s2_direct(old, a, e_hom):
    """Form (3.7b) evaluated also on Dual input, using physical quadratic parity."""
    x, theta = old[PHYSICAL], old[THETA]
    mu, shift = reconstruct_multipliers(old)
    u = field_generator(x, theta)
    z = field_generator(u, theta)
    di = (interaction_action(physical_add(x, u), mu, shift, a, e_hom)
          - interaction_action(physical_add(x, u, -1), mu, shift, a, e_hom)) / F(2)
    da = (physical_action(physical_add(x, z), a)
          - physical_action(physical_add(x, z, -1), a)) / F(2)
    return -di - physical_action(u, 0) - da


def state_directional(function, state, direction):
    result = function(native_dual(state, direction))
    return result.tangent if isinstance(result, Dual) else F(0)


def residuals(trajectory, time, a):
    row, previous, following = trajectory[time], trajectory[time - 1], trajectory[time + 1]
    l = laplacian(row[:5])
    h = tuple(following[r] - 2 * row[r] + previous[r] + l[r] - G * row[5] * ELL[r]
              for r in range(5))
    c = following[5] - row[5] + previous[5] - F(a, 4) - G * dot(ELL, row[:5])
    return h + (c,)


def terminal_energy_gradient(trajectory, a):
    previous, current = trajectory[-2], trajectory[-1]
    lh = laplacian(current[:5])
    h = tuple(previous[r] - current[r] + lh[r] / 2 - G * current[5] * F(ELL[r], 2)
              for r in range(5))
    c = previous[5] - current[5] / 2 - F(a, 8) - G * dot(ELL, current[:5]) / 2
    return h + (c,)


def fraction_text(value):
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def fraction_list(values):
    return ",".join(fraction_text(value) for value in values)


def local_reconstruction_check(state):
    horizon = len(state[PHYSICAL]) - 1
    mu, shift = reconstruct_multipliers(state)
    running = (F(0),) * 5
    for n in range(1, horizon):
        previous = running
        running = plus(running, mu[n])
        require(running == state[THETA][n], "LOCAL_RECONSTRUCTION")
        require(minus(running, mu[n]) == previous, "LOCAL_RECONSTRUCTION")
        require(minus(shift[n], incidence(running)) == state[SHIFT][n], "LOCAL_RECONSTRUCTION")
    require(plus(running, mu[horizon]) == state[TERMINAL], "LOCAL_RECONSTRUCTION")
    numerators, denominator = encode_native(state)
    im, ishift = reconstruct_multipliers(numerators)
    for b in range(1, horizon + 1):
        total = sum(im[b])
        alpha = F(total, 5 * denominator)
        lam = tuple(F(5 * value - total, 5 * denominator) for value in im[b])
        require(sum(lam) == 0 and tuple(alpha + value for value in lam) == mu[b], "LOCAL_RECONSTRUCTION")
    for n in range(1, horizon):
        require(tuple(F(value, denominator) for value in ishift[n]) == shift[n], "LOCAL_RECONSTRUCTION")


def integer_translation_check(state, p_num, p_den, q_num, q_den):
    encoded, denominator = encode_native(state)
    psi = decode_parameter(p_num, p_den)
    eta = decode_parameter(q_num, q_den)
    moved, moved_den = translate_integer(encoded, denominator, p_num, p_den)
    target = translate_native(state, psi)
    require(decode_native(moved, moved_den) == target, "INTEGER_GAUGE")
    minus_p = tuple(tuple(-value for value in row) for row in p_num)
    restored, restored_den = translate_integer(moved, moved_den, minus_p, p_den)
    require((restored, restored_den) == (encoded, denominator), "INTEGER_GAUGE")
    twice, twice_den = translate_integer(moved, moved_den, q_num, q_den)
    sum_num = tuple(tuple(q_den * left + p_den * right for left, right in zip(p_row, q_row))
                    for p_row, q_row in zip(p_num, q_num))
    once, once_den = translate_integer(encoded, denominator, sum_num, p_den * q_den)
    require((once, once_den) == (twice, twice_den), "INTEGER_GAUGE")
    require(decode_native(once, once_den) == translate_native(target, eta), "INTEGER_GAUGE")
    require(tuple(once[PHYSICAL][n] for n in (0, len(state[PHYSICAL]) - 1))
            == tuple(tuple(int(value * once_den) for value in state[PHYSICAL][n])
                     for n in (0, len(state[PHYSICAL]) - 1)), "INTEGER_GAUGE")
    divisor = once_den
    for value in independent_values(once, True):
        divisor = gcd(divisor, value)
    require(divisor == 1, "INTEGER_GAUGE")


def audit_configurations():
    horizon = 5
    directions = coordinate_directions(horizon)
    require(len(directions) == 133, "DOMAIN")
    action_digest, gradient_digest, gauge_digest = sha256(), sha256(), sha256()
    counts = dict(configurations=0, parent=0, completion=0, finite=0, noether=0,
                  commutator=0, integer=0, local=0, bulk=0, boundary=0)
    for a in (-1, 0, 1):
        for seed in (0, 1):
            index = counts["configurations"]
            old, e_hom = configuration(a, seed)
            domain_check(old)
            counts["configurations"] += 1
            for coordinate, direction in enumerate(directions):
                value = parent_derivative(old, direction, a, e_hom, F(1))
                coefficient = Polynomial.promote(parent_action(
                    native_add(old, direction, Polynomial((0, 1))), a, e_hom, F(1))).coefficient(1)
                require(value == coefficient, "PARENT_VARIATION")
                gradient_digest.update(f"D|{index}|{coordinate}|{fraction_text(value)}\n".encode("ascii"))
                counts["parent"] += 1
            coefficients = inherited_coefficients(old, a, e_hom)
            actual_coefficients = completed_coefficients(old, a, e_hom)
            actual_coefficients += (F(0),) * max(0, 4 - len(actual_coefficients))
            require(len(actual_coefficients) == 4 and coefficients == actual_coefficients, "CUBIC_COMPLETION")
            for epsilon in (-1, 0, 1, 2):
                value = completed_action(old, a, e_hom, epsilon)
                require(value == sum(coefficient * epsilon ** power
                                     for power, coefficient in enumerate(coefficients)), "CUBIC_COMPLETION")
                action_digest.update(f"A|{index}|{epsilon}|{fraction_list(coefficients + (value,))}\n".encode("ascii"))
                counts["completion"] += 1
            parameter_list = parameters(a, seed)
            require(len(parameter_list) == 21, "DOMAIN")
            for j, (p_num, p_den) in enumerate(parameter_list):
                q_num, q_den = parameter_list[(j + 1) % 21]
                psi, eta = decode_parameter(p_num, p_den), decode_parameter(q_num, q_den)
                total_parameter = tuple(plus(left, right) for left, right in zip(psi, eta))
                negative_parameter = tuple(scaled(-1, row) for row in psi)
                for epsilon in (-1, 0, 1, 2):
                    native = list(old)
                    native[PHYSICAL] = dress_fields(old[PHYSICAL], old[THETA], epsilon)
                    native = tuple(native)
                    recovered, determinant = chart_reconstruct(native, epsilon)
                    require(determinant != 0 and recovered == old, "CHART_INVERSE")
                    moved, moved_det = exact_chart_translate(old, psi, epsilon)
                    twice, twice_det = exact_chart_translate(moved, eta, epsilon)
                    once, once_det = exact_chart_translate(old, total_parameter, epsilon)
                    restored, _ = exact_chart_translate(moved, negative_parameter, epsilon)
                    require(moved_det != 0 and twice_det != 0 and once_det != 0, "FINITE_GAUGE")
                    require(twice == once and restored == old, "FINITE_GAUGE")
                    require(dress_fields(moved[PHYSICAL], moved[THETA], epsilon) == native[PHYSICAL], "FINITE_GAUGE")
                    require(completed_action(moved, a, e_hom, epsilon)
                            == completed_action(old, a, e_hom, epsilon), "FINITE_GAUGE")
                    native_moved = translate_native(native, psi)
                    require(parent_action(native_moved, a, e_hom, epsilon)
                            == parent_action(native, a, e_hom, epsilon), "FINITE_GAUGE")
                    counts["finite"] += 1
                    tangent, _ = exact_chart_direction(old, psi, epsilon)
                    require(completed_derivative(old, tangent, a, e_hom, epsilon) == 0, "NOETHER")
                    counts["noether"] += 1
                    bracket = chart_lie_bracket(old, psi, eta, epsilon)
                    require(all(value == 0 for value in native_values(bracket)), "COMMUTATOR")
                    counts["commutator"] += 1
                    integer_translation_check(native, p_num, p_den, q_num, q_den)
                    counts["integer"] += 1
                    local_reconstruction_check(native_moved)
                    counts["local"] += 1
                    payload_values = physical_flat(moved[PHYSICAL]) + physical_flat(tangent[PHYSICAL])
                    require(len(payload_values) == 72, "CERTIFICATE")
                    gauge_digest.update(f"G|{index}|{j}|{epsilon}|{fraction_list(payload_values)}\n".encode("ascii"))
            stationary = list(old)
            kappa = F(index + 1, 7)
            stationary[TERMINAL] = (kappa,) * 5
            stationary[SHIFT] = zero_rows(horizon, 10)
            stationary = tuple(stationary)
            boundary_gradient = terminal_energy_gradient(old[PHYSICAL], a)
            for coordinate, direction in enumerate(directions[:24]):
                n, component = 1 + coordinate // 6, coordinate % 6
                value = parent_derivative(stationary, direction, a, e_hom, F(1))
                expected = -residuals(old[PHYSICAL], n, a)[component]
                if n == horizon - 1:
                    expected -= kappa * boundary_gradient[component]
                    counts["boundary"] += 1
                else:
                    counts["bulk"] += 1
                require(value == expected, "STATIONARY_EQUATIONS")
    expected_counts = dict(configurations=6, parent=798, completion=24, finite=504, noether=504,
                           commutator=504, integer=504, local=504, bulk=108, boundary=36)
    require(counts == expected_counts, "CERTIFICATE")
    return action_digest.hexdigest(), gradient_digest.hexdigest(), gauge_digest.hexdigest()


def audit_auxiliary_rank():
    matrix = auxiliary_matrix(5)
    require(len(matrix) == 44 and all(len(row) == 45 for row in matrix), "AUXILIARY_RANK")
    _, pivots, _ = row_reduction(matrix)
    kernel = (F(1),) * 5 + (F(0),) * 40
    require(len(pivots) == 44 and matrix_vector(matrix, kernel) == (F(0),) * 44,
            "AUXILIARY_RANK")
    return len(pivots)


def parameter_with_entries(horizon, entries):
    rows = list(zero_rows(horizon, 5))
    for n, row in entries:
        rows[n] = tuple(F(value) for value in row)
    return tuple(rows)


def audit_witnesses():
    controls = set()
    unit = (F(1), F(0), F(0), F(0), F(0))
    physical_unit = unit + (F(0),)
    # Inherited witness: mu_3=e, N=0, hence theta_3=theta_4=e and r=e.
    old = replace_row(native_zero(5), PHYSICAL, 3, physical_unit)
    old = replace_row(old, THETA, 3, (F(1),) * 5)
    old = replace_row(old, THETA, 4, (F(1),) * 5)
    old = list(old)
    old[TERMINAL] = (F(1),) * 5
    old = tuple(old)
    psi = parameter_with_entries(5, ((2, unit), (3, unit)))
    coefficients = inherited_coefficients(old, 0, F(0))
    exact_value = completed_action(old, 0, F(0), F(1))
    require(coefficients[3] == F(-1, 8) and exact_value == F(85, 324), "WITNESSES")
    require(exact_value - sum(coefficients[:3]) == F(-1, 8), "NEGATIVE_CONTROLS")
    controls.add("OMIT_S3")
    tangent, _ = exact_chart_direction(old, psi, F(1))
    moved, _ = exact_chart_translate(old, psi, F(1))
    require(tuple(tangent[PHYSICAL][n][0] for n in (2, 3, 4)) == (F(1, 2), F(-1, 5), F(1, 10)), "WITNESSES")
    require(tuple(moved[PHYSICAL][n][0] for n in (2, 3, 4)) == (F(3, 8), F(3, 4), F(1, 8)), "WITNESSES")
    require(completed_derivative(old, tangent, 0, F(0), F(1)) == 0, "NOETHER")
    first = field_generator(old[PHYSICAL], psi)
    second = field_generator(first, old[THETA])
    truncated = list(native_zero(5))
    truncated[THETA] = psi
    truncated[PHYSICAL] = physical_add(first, second)
    truncated_defect = completed_derivative(old, tuple(truncated), 0, F(0), F(1))
    require(truncated_defect == F(8, 81), "NEGATIVE_CONTROLS")
    controls.add("TRUNCATED_GENERATOR")
    d1, d2 = list(native_zero(5)), list(native_zero(5))
    d1[PHYSICAL], d2[PHYSICAL] = first, second
    original_i = lambda state: interaction_action(state[PHYSICAL], *reconstruct_multipliers(state), 0, F(0))
    original_s2 = lambda state: s2_direct(state, 0, F(0))
    w3 = state_directional(original_s2, old, tuple(d1)) + state_directional(original_i, old, tuple(d2))
    w4 = state_directional(original_s2, old, tuple(d2))
    require((w3, w4, w3 + w4) == (F(1, 8), F(-115, 1296), F(47, 1296)), "WITNESSES")

    # Terminal lapse holonomy is an invariant retained by the local reconstruction.
    terminal = list(native_zero(5))
    terminal[TERMINAL] = (F(1),) * 5
    mu, _ = reconstruct_multipliers(tuple(terminal))
    total = tuple(sum(row[r] for row in mu) for r in range(5))
    dropped = tuple(sum(row[r] for row in mu[:-1]) for r in range(5))
    require(total == (F(1),) * 5 and dropped == (F(0),) * 5, "NEGATIVE_CONTROLS")
    controls.add("DROP_TERMINAL_RESIDUAL")

    # Full temporal matrix: one distant parameter changes an early old field.
    nonlocal_old = replace_row(native_zero(5), PHYSICAL, 5, physical_unit)
    for n in range(1, 5):
        nonlocal_old = replace_row(nonlocal_old, THETA, n, (F(2),) * 5)
    nonlocal_psi = parameter_with_entries(5, ((4, scaled(2, unit)),))
    nonlocal_direction, determinant = exact_chart_direction(nonlocal_old, nonlocal_psi, F(1))
    response = tuple(nonlocal_direction[PHYSICAL][n][0] for n in range(1, 5))
    require(response == (F(1, 5), F(1, 5), F(2, 5), F(3, 5)), "NEGATIVE_CONTROLS")
    matrix = full_k_matrix(nonlocal_old[THETA], F(1))
    scalar_indices = tuple(6 * n for n in range(1, 5))
    scalar_matrix = tuple(tuple(matrix[i][j] for j in scalar_indices) for i in scalar_indices)
    _, scalar_pivots, scalar_det = row_reduction(scalar_matrix)
    require(scalar_det == 5 and len(scalar_pivots) == 4 and determinant == 5 ** 6, "WITNESSES")
    controls.add("NONLOCAL_INVERSE")

    # Singular charts have an exact nonzero kernel; native parent translations remain defined.
    singular = replace_row(native_zero(5), THETA, 1, (F(2),) * 5)
    singular = replace_row(singular, THETA, 2, (F(-2),) * 5)
    matrix = full_k_matrix(singular[THETA], F(1))
    kernel = list(zero_rows(5, 6))
    kernel[1] = kernel[2] = physical_unit
    require(any(value != 0 for value in physical_flat(kernel))
            and matrix_vector(matrix, physical_flat(kernel)) == (F(0),) * 36, "NEGATIVE_CONTROLS")
    _, pivots, determinant = row_reduction(matrix)
    require(determinant == 0 and len(pivots) == 30, "WITNESSES")
    rejected = False
    try:
        chart_reconstruct(singular, F(1))
    except SingularChart:
        rejected = True
    require(rejected, "NEGATIVE_CONTROLS")
    require(parent_action(singular, 0, F(0), F(1)) == parent_action(native_zero(5), 0, F(0), F(1)), "WITNESSES")
    controls.add("SINGULAR_CHART")

    # A vanished leading minor is not the same as a singular complete chart.
    pivot_chart = replace_row(native_zero(5), PHYSICAL, 1, physical_unit)
    pivot_chart = replace_row(pivot_chart, THETA, 1, (F(2),) * 5)
    pivot_chart = replace_row(pivot_chart, THETA, 2, (F(-2),) * 5)
    pivot_chart = replace_row(pivot_chart, THETA, 3, (F(2),) * 5)
    matrix = full_k_matrix(pivot_chart[THETA], F(1))
    scalar_matrix = tuple(tuple(matrix[i][j] for j in scalar_indices) for i in scalar_indices)
    _, scalar_pivots, scalar_det = row_reduction(scalar_matrix)
    leading_two = tuple(tuple(row[j] for j in range(2)) for row in scalar_matrix[:2])
    _, leading_pivots, leading_det = row_reduction(leading_two)
    require(scalar_det == -1 and len(scalar_pivots) == 4
            and leading_det == 0 and len(leading_pivots) == 1, "WITNESSES")
    native_pivot = list(pivot_chart)
    native_pivot[PHYSICAL] = dress_fields(pivot_chart[PHYSICAL], pivot_chart[THETA], F(1))
    recovered, determinant = chart_reconstruct(tuple(native_pivot), F(1))
    require(recovered == pivot_chart and determinant == 1, "CHART_INVERSE")

    # The old TT metric is not an invariant reading of the exact theta symmetry.
    metric = replace_row(native_zero(5), PHYSICAL, 3, scaled(F(1, 4), physical_unit))
    metric_psi = parameter_with_entries(5, ((2, scaled(16, unit)),))
    changed, determinant = exact_chart_translate(metric, metric_psi, F(1))
    require(determinant != 0 and changed[PHYSICAL][2][0] == 2, "NEGATIVE_CONTROLS")
    invariant = dress_fields(changed[PHYSICAL], changed[THETA], F(1))
    require(invariant == metric[PHYSICAL] and invariant[2][0] == 0, "WITNESSES")
    raw_metric = (-1, 1 + changed[PHYSICAL][2][0], 1 - changed[PHYSICAL][2][0], 1)
    require(raw_metric == (-1, 3, -1, 1), "NEGATIVE_CONTROLS")
    controls.add("RAW_METRIC")

    # A local invariant quartic adds physical force without changing the gauge quotient.
    alternative = replace_row(native_zero(5), PHYSICAL, 2, physical_unit)
    alternative_direction = replace_row(native_zero(5), PHYSICAL, 2, physical_unit)
    j_function = lambda state: quartic_invariant(state[PHYSICAL])
    require(state_directional(j_function, alternative, alternative_direction) == 4, "NEGATIVE_CONTROLS")
    require(j_function(translate_native(alternative, metric_psi)) == j_function(alternative), "NEGATIVE_CONTROLS")
    eps_poly = Polynomial((0, 1))
    alternative_series = eps_poly ** 3 * quartic_invariant(dress_fields(old[PHYSICAL], old[THETA], eps_poly))
    require(all(alternative_series.coefficient(k) == 0 for k in (0, 1, 2)), "WITNESSES")
    controls.add("NONUNIQUE_COMPLETION")

    # Product denominators alone do not give a bijection of redundant encodings.
    zero, denominator = encode_native(native_zero(5))
    half_num = parameter_with_entries(5, ((2, unit),))
    first_raw = list(native_map(lambda value: 2 * value, zero))
    first_raw[THETA] = tuple(tuple(value + denominator * omega for value, omega in zip(row, param))
                             for row, param in zip(first_raw[THETA], half_num))
    second_raw = list(native_map(lambda value: 2 * value, tuple(first_raw)))
    second_raw[THETA] = tuple(tuple(value - 2 * denominator * omega for value, omega in zip(row, param))
                              for row, param in zip(second_raw[THETA], half_num))
    require(denominator == 1 and all(value == 0 for value in native_values(tuple(second_raw))), "NEGATIVE_CONTROLS")
    require(normalized_encoding(tuple(second_raw), 4) == (zero, 1), "NEGATIVE_CONTROLS")
    controls.add("UNNORMALIZED_ROUNDTRIP")
    require(controls == frozenset(("OMIT_S3", "TRUNCATED_GENERATOR", "DROP_TERMINAL_RESIDUAL",
                                   "NONLOCAL_INVERSE", "SINGULAR_CHART", "RAW_METRIC",
                                   "NONUNIQUE_COMPLETION", "UNNORMALIZED_ROUNDTRIP")), "CERTIFICATE")
    return len(controls)


def certificate():
    root = Path(__file__).resolve().parents[2]
    for name, size, digest in AUTHORITY:
        raw = (root / "canon" / name).read_bytes()
        require(len(raw) == size and sha256(raw).hexdigest() == digest, "AUTHORITY")
    for basis in VBASIS:
        require(sum(basis) == 0, "DOMAIN")
    for basis in KBASIS:
        require(divergence(basis) == (0,) * 5, "DOMAIN")
    _, cycle_pivots, _ = row_reduction(KBASIS)
    require(len(cycle_pivots) == 6, "DOMAIN")
    action_digest, gradient_digest, gauge_digest = audit_configurations()
    rank = audit_auxiliary_rank()
    controls = audit_witnesses()
    lines = [
        "CERTIFICATE=" + PROBE,
        "AUTHORITY_FILES=5",
        "CONFIGURATIONS=6",
        "PARENT_COORDINATES=133",
        "PARENT_VARIATIONS=798",
        "CUBIC_COMPLETION_CHECKS=24",
        "FINITE_GAUGE_CHECKS=504",
        "EXACT_NOETHER_CHECKS=504",
        "EXACT_COMMUTATOR_CHECKS=504",
        "INTEGER_GAUGE_CHECKS=504",
        "LOCAL_MULTIPLIER_CHECKS=504",
        f"AUXILIARY_CONSTRAINT_RANK={rank}",
        "BULK_EQUATION_CHECKS=108",
        "BOUNDARY_VARIATION_CHECKS=36",
        "ACTION_PAYLOAD_SHA256=" + action_digest,
        "PARENT_GRADIENT_SHA256=" + gradient_digest,
        "GAUGE_PAYLOAD_SHA256=" + gauge_digest,
        "OLD_TRUNCATION_REMAINDERS=1/8,-115/1296,47/1296",
        "CUBIC_COMPLETION_WITNESS=-1/8,85/324",
        "EXACT_TANGENT_WITNESS=1/2,-1/5,1/10",
        "FINITE_MAP_WITNESS=3/8,3/4,1/8",
        "NONLOCAL_INVERSE_WITNESS=1/5,1/5,2/5,3/5",
        "SINGULAR_CHART=0;KERNEL_NONZERO",
        "RAW_METRIC_COUNTEREXAMPLE=2;-1,3,-1,1",
        "ALTERNATIVE_BULK_GRADIENT=4",
        f"NEGATIVE_CONTROLS={controls}",
        "CERTIFICATE_RESULT=PASS",
    ]
    require(len(lines) == 27, "CERTIFICATE")
    return ("\n".join(lines) + "\n").encode("ascii")


def main():
    try:
        output = certificate()
    except ScientificFailure as failure:
        output = f"FALSIFIER={failure.key}\nRESULT=FAIL\n".encode("ascii")
    sys.stdout.buffer.write(output)


if __name__ == "__main__":
    main()
