#!/usr/bin/env python3
"""Independent dual-number audit of the global cubic Noether extension.

Written from PREREG.md without reading this probe's primary or PROOF.md.
The action is evaluated directly on nested time arrays. Derivatives use
first-order dual numbers, and commutators use sparse temporal matrices.
No scientific execution or import is permitted before the public pin.
"""

from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import sys


PROBE = "P-INTEGER-CUBIC-NOETHER-CLOSURE-1"
M = 324
G = F(1, M)
DIPOLE = (1, -1, 0, 0, 0)
SIGMA = (F(1, 2), F(1, 2), F(0), F(0), F(0))
EDGES = tuple((r, (r + length) % 5, 29 if length == 1 else 65)
              for length in (1, 2) for r in range(5))
VERTEX_BASIS = tuple(tuple(int(r == i) - int(r == 4) for r in range(5))
                     for i in range(4))
CYCLE_BASIS = (
    (1, 1, 1, 1, 1, 0, 0, 0, 0, 0),
    (-1, -1, 0, 0, 0, 1, 0, 0, 0, 0),
    (0, -1, -1, 0, 0, 0, 1, 0, 0, 0),
    (0, 0, -1, -1, 0, 0, 0, 1, 0, 0),
    (1, 1, 1, 0, 0, 0, 0, 0, 1, 0),
    (0, 1, 1, 1, 0, 0, 0, 0, 0, 1),
)

# Every sector has T+1 time rows. Unused endpoint/bond-zero rows are zero.
H, CHI, TAU, MOM, ALPHA, LAMBDA, SHIFT = range(7)
WIDTHS = (5, 1, 5, 10, 1, 5, 10)
AUTHORITY = (
    ("CANON.md", 1052518,
     "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
    ("CORE.md", 30714,
     "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
    ("FRONTIER.md", 27382,
     "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
    ("REGISTRY.tsv", 532811,
     "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
    ("CHANGELOG.md", 207770,
     "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
)
FALSIFIERS = frozenset((
    "AUTHORITY", "DOMAIN", "INCIDENCE", "GLOBAL_GRADIENT",
    "CONTINUITY", "CONSTRAINT_PROPAGATION", "INTEGER_CONTINUITY",
    "AUXILIARY_GAUGE", "NOETHER", "INTEGER_NOETHER", "DEFORMATION",
    "FIELD_REDEFINITION", "INTEGER_TANGENT", "COMMUTATOR",
    "NEIGHBOR_WITNESS", "REMAINDER_WITNESS", "CENTRAL_WITNESS",
    "CONTROL", "NONCLOSURE", "CERTIFICATE", "BREAKER_BYTES",
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


class Dual:
    """An exact value and the coefficient of one nilpotent direction."""

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
                    / (other.value * other.value))

    def __rtruediv__(self, other):
        return self.promote(other) / self

    def __pow__(self, exponent):
        if type(exponent) is not int or exponent < 0:
            raise ValueError("only nonnegative integer powers are used")
        if exponent == 0:
            return Dual(1)
        return Dual(self.value ** exponent,
                    exponent * self.value ** (exponent - 1) * self.tangent)


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


def laplacian_integer(vertex):
    return tuple(188 * vertex[r]
                 - 29 * (vertex[(r - 1) % 5] + vertex[(r + 1) % 5])
                 - 65 * (vertex[(r - 2) % 5] + vertex[(r + 2) % 5])
                 for r in range(5))


def green_adjoint_integer(vertex):
    return tuple(188 * vertex[r]
                 - 65 * (vertex[(r - 1) % 5] + vertex[(r + 1) % 5])
                 - 29 * (vertex[(r - 2) % 5] + vertex[(r + 2) % 5])
                 for r in range(5))


def project_zero_mean(vertex):
    average = sum(vertex) / F(5)
    return tuple(value - average for value in vertex)


def zeros(horizon):
    return tuple(tuple(tuple(F(0) for _ in range(width))
                       for _ in range(horizon + 1)) for width in WIDTHS)


def editable(state):
    return [[list(row) for row in sector] for sector in state]


def freeze(state):
    return tuple(tuple(tuple(row) for row in sector) for sector in state)


def state_add(state, direction, factor=1):
    return tuple(tuple(tuple(value + factor * change for value, change in zip(row, drow))
                       for row, drow in zip(sector, dsector))
                 for sector, dsector in zip(state, direction))


def state_scale(factor, state):
    return tuple(tuple(tuple(factor * value for value in row) for row in sector)
                 for sector in state)


def state_dual(state, direction):
    return tuple(tuple(tuple(Dual(value, change) for value, change in zip(row, drow))
                       for row, drow in zip(sector, dsector))
                 for sector, dsector in zip(state, direction))


def state_values(state):
    return tuple(value for sector in state for row in sector for value in row)


def domain_check(state, horizon, admit_ambient_p=False):
    require(len(state) == 7, "DOMAIN")
    for sector, width in zip(state, WIDTHS):
        require(len(sector) == horizon + 1 and all(len(row) == width for row in sector), "DOMAIN")
        require(all(isinstance(value, (int, F)) for row in sector for value in row), "DOMAIN")
    for b in range(1, horizon + 1):
        require(sum(state[TAU][b]) == sum(state[LAMBDA][b]) == 0, "DOMAIN")
    if not admit_ambient_p:
        for n in range(1, horizon):
            require(divergence(state[MOM][n]) == (0,) * 5, "DOMAIN")


def energy_density(state, bond, a):
    older, now = state[H][bond - 1], state[H][bond]
    cp, c = state[CHI][bond - 1][0], state[CHI][bond][0]
    output = [(now[r] - older[r]) ** 2 / F(2) for r in range(5)]
    edge_old, edge_now = incidence(older), incidence(now)
    for k, (tail, head, weight) in enumerate(EDGES):
        share = F(weight, 4 * M) * edge_old[k] * edge_now[k]
        output[tail] += share
        output[head] += share
    source = ((c - cp) ** 2 / F(2) + c * cp / F(2)
              - F(a, 8) * (c + cp))
    for r in range(5):
        output[r] += SIGMA[r] * source - F(DIPOLE[r], 2 * M) * (cp * now[r] + c * older[r])
    return tuple(output)


def edge_current(state, time, include_interaction=True):
    h, c = state[H], state[CHI]
    temporal = minus(h[time + 1], h[time - 1])
    spatial = incidence(h[time])
    result = [F(weight, 4 * M) * spatial[k] * (temporal[tail] + temporal[head])
              for k, (tail, head, weight) in enumerate(EDGES)]
    if include_interaction:
        result[0] -= F(1, 4 * M) * (c[time + 1][0] - c[time - 1][0]) * (h[time][0] + h[time][1])
    return tuple(result)


def action_parts(state, a, e_hom, include_interaction=True, current_sites=None):
    """The complete global S_0 and S_int, also valid on Dual entries."""
    horizon = len(state[H]) - 1
    h, c, tau, p, alpha, lam, shift = state
    free = F(0)
    interaction = F(0)
    offset = F(4342005, 8683757) * F(a, 4) ** 2
    for b in range(1, horizon + 1):
        change = minus(h[b], h[b - 1])
        free += dot(change, change) / F(2) + (c[b][0] - c[b - 1][0]) ** 2 / F(2)
        free += 2 * dot(lam[b], laplacian(tau[b]))
        density = energy_density(state, b, a)
        interaction -= alpha[b][0] * (sum(density) + offset - e_hom)
        interaction -= dot(lam[b], density)
    for n in range(1, horizon):
        free += (-dot(h[n], laplacian(h[n])) / F(2) - c[n][0] ** 2 / F(2)
                 + F(a, 4) * c[n][0] + G * c[n][0] * dot(DIPOLE, h[n]))
        momentum = plus(weighted(incidence(minus(tau[n + 1], tau[n]))), p[n])
        free += 2 * dot(shift[n], momentum)
        if current_sites is None or n in current_sites:
            interaction += dot(shift[n], edge_current(state, n, include_interaction))
    return free, interaction


def action_value(state, a, e_hom, epsilon=1, **options):
    free, interaction = action_parts(state, a, e_hom, **options)
    return free + epsilon * interaction


def physical_action(state, a):
    physical = list(zeros(len(state[H]) - 1))
    physical[H], physical[CHI] = state[H], state[CHI]
    return action_parts(tuple(physical), a, F(0))[0]


def dual_derivatives(state, direction, a, e_hom, **options):
    parts = action_parts(state_dual(state, direction), a, e_hom, **options)
    return tuple(value.tangent if isinstance(value, Dual) else F(0) for value in parts)


def directional(state, direction, a, e_hom, epsilon=1, **options):
    free, interaction = dual_derivatives(state, direction, a, e_hom, **options)
    return free + epsilon * interaction


def coordinate_directions(horizon):
    specs = []
    for n in range(1, horizon):
        for r in range(5):
            specs.append((H, n, tuple(int(i == r) for i in range(5))))
    specs.extend((CHI, n, (1,)) for n in range(1, horizon))
    for b in range(1, horizon + 1):
        specs.extend((TAU, b, vector) for vector in VERTEX_BASIS)
    for n in range(1, horizon):
        specs.extend((MOM, n, vector) for vector in CYCLE_BASIS)
    specs.extend((ALPHA, b, (1,)) for b in range(1, horizon + 1))
    for b in range(1, horizon + 1):
        specs.extend((LAMBDA, b, vector) for vector in VERTEX_BASIS)
    for n in range(1, horizon):
        for k in range(10):
            specs.append((SHIFT, n, tuple(int(j == k) for j in range(10))))
    result = []
    for sector, time, vector in specs:
        direction = editable(zeros(horizon))
        direction[sector][time] = list(map(F, vector))
        result.append(freeze(direction))
    require(len(result) == 31 * horizon - 22, "DOMAIN")
    return tuple(result)


def residuals(state, time, a):
    h, c = state[H], state[CHI]
    lap = laplacian(h[time])
    rh = tuple(h[time + 1][r] - 2 * h[time][r] + h[time - 1][r]
               + lap[r] - G * c[time][0] * DIPOLE[r] for r in range(5))
    rc = (c[time + 1][0] - c[time][0] + c[time - 1][0]
          - F(a, 4) - G * dot(DIPOLE, h[time]))
    return rh, rc


def continuity_pair(state, time, a):
    left = plus(minus(energy_density(state, time + 1, a), energy_density(state, time, a)),
                divergence(edge_current(state, time)))
    rh, rc = residuals(state, time, a)
    qh = minus(state[H][time + 1], state[H][time - 1])
    qc = state[CHI][time + 1][0] - state[CHI][time - 1][0]
    right = tuple((qh[r] * rh[r] + SIGMA[r] * qc * rc) / F(2) for r in range(5))
    return left, right


def constraint_pair(state, time, a):
    def ham(bond):
        return minus(scaled(2, laplacian(state[TAU][bond])),
                     project_zero_mean(energy_density(state, bond, a)))
    momentum = plus(scaled(2, plus(weighted(incidence(minus(state[TAU][time + 1], state[TAU][time]))),
                                    state[MOM][time])), edge_current(state, time))
    left = minus(ham(time + 1), ham(time))
    current_continuity = continuity_pair(state, time, a)[0]
    right = minus(minus(divergence(momentum), scaled(2, divergence(state[MOM][time]))),
                  project_zero_mean(current_continuity))
    return left, right


def parameter_arrays(a, seed, horizon):
    result = []
    for n in range(1, horizon):
        for r in range(5):
            numerator = [[0] * 5 for _ in range(horizon + 1)]
            numerator[n][r] = 1
            result.append((tuple(tuple(row) for row in numerator), 1))
    numerator = tuple(tuple(fixture_integer(n, r, 7, a, seed) if 0 < n < horizon else 0
                            for r in range(5)) for n in range(horizon + 1))
    result.append((numerator, 7))
    return tuple(result)


def decode_parameter(numerator, denominator):
    return tuple(tuple(F(value, denominator) for value in row) for row in numerator)


def auxiliary_direction(psi):
    horizon = len(psi) - 1
    result = editable(zeros(horizon))
    for b in range(1, horizon + 1):
        difference = minus(psi[b], psi[b - 1])
        result[ALPHA][b] = [sum(difference) / F(5)]
        result[LAMBDA][b] = list(project_zero_mean(difference))
    for n in range(1, horizon):
        result[SHIFT][n] = list(incidence(psi[n]))
    return freeze(result)


def field_direction(state, psi):
    horizon = len(psi) - 1
    result = editable(zeros(horizon))
    for n in range(1, horizon):
        qh = minus(state[H][n + 1], state[H][n - 1])
        qc = state[CHI][n + 1][0] - state[CHI][n - 1][0]
        result[H][n] = [psi[n][r] * qh[r] / F(2) for r in range(5)]
        result[CHI][n] = [dot(SIGMA, psi[n]) * qc / F(2)]
    return freeze(result)


def pure_multipliers(state, d0):
    result = list(state)
    for sector in (ALPHA, LAMBDA, SHIFT):
        result[sector] = d0[sector]
    return tuple(result)


def physical_hessian(direction):
    horizon = len(direction[H]) - 1
    h, c = direction[H], direction[CHI]
    result = F(0)
    for b in range(1, horizon + 1):
        dh = minus(h[b], h[b - 1])
        result += dot(dh, dh) + (c[b][0] - c[b - 1][0]) ** 2
    for n in range(1, horizon):
        result += -dot(h[n], laplacian(h[n])) - c[n][0] ** 2 + 2 * G * c[n][0] * dot(DIPOLE, h[n])
    return result


def fixture_integer(time, index, channel, a, seed):
    return (17 * time + 11 * index + 7 * seed + 5 * a + 3 * channel) % 19 - 9


def configuration(a, seed, horizon=5, denominator=60):
    rows = editable(zeros(horizon))
    for t in range(horizon + 1):
        rows[H][t] = [fixture_integer(t, r, 0, a, seed) for r in range(5)]
        rows[CHI][t] = [fixture_integer(t, 0, 1, a, seed)]
    for b in range(1, horizon + 1):
        rows[TAU][b] = [sum(fixture_integer(b, i, 2, a, seed) * VERTEX_BASIS[i][r]
                            for i in range(4)) for r in range(5)]
        rows[ALPHA][b] = [fixture_integer(b, 0, 4, a, seed)]
        rows[LAMBDA][b] = [sum(fixture_integer(b, i, 5, a, seed) * VERTEX_BASIS[i][r]
                               for i in range(4)) for r in range(5)]
    for n in range(1, horizon):
        rows[MOM][n] = [sum(fixture_integer(n, i, 3, a, seed) * CYCLE_BASIS[i][k]
                            for i in range(6)) for k in range(10)]
        rows[SHIFT][n] = [fixture_integer(n, k, 6, a, seed) for k in range(10)]
    integer_state = freeze(rows)
    rational_state = state_scale(F(1, denominator), integer_state)
    return rational_state, integer_state, F(seed + 1, 7 + a * a)


def integer_density(numerators, bond, a, denominator):
    previous, current = numerators[H][bond - 1], numerators[H][bond]
    cp, c = numerators[CHI][bond - 1][0], numerators[CHI][bond][0]
    old_edges, new_edges = incidence(previous), incidence(current)
    shares = [0] * 5
    for k, (tail, head, weight) in enumerate(EDGES):
        value = weight * old_edges[k] * new_edges[k]
        shares[tail] += value
        shares[head] += value
    source = M * (c - cp) ** 2 + M * c * cp - 81 * a * denominator * (c + cp)
    return tuple(2 * M * (current[r] - previous[r]) ** 2 + shares[r]
                 + int(r in (0, 1)) * source
                 - 2 * DIPOLE[r] * (cp * current[r] + c * previous[r]) for r in range(5))


def integer_continuity_pair(numerators, time, a, denominator):
    p, y = numerators[H], numerators[CHI]
    qh = minus(p[time + 1], p[time - 1])
    qc = y[time + 1][0] - y[time - 1][0]
    bp = incidence(p[time])
    currents = tuple(weight * bp[k] * (qh[tail] + qh[head])
                     - (qc * (p[time][0] + p[time][1]) if k == 0 else 0)
                     for k, (tail, head, weight) in enumerate(EDGES))
    ah = tuple(M * (p[time + 1][r] - 2 * p[time][r] + p[time - 1][r])
               + lap - y[time][0] * DIPOLE[r]
               for r, lap in enumerate(laplacian_integer(p[time])))
    ac = (M * (y[time + 1][0] - y[time][0] + y[time - 1][0])
          - 81 * a * denominator - dot(DIPOLE, p[time]))
    left = plus(minus(integer_density(numerators, time + 1, a, denominator),
                      integer_density(numerators, time, a, denominator)), divergence(currents))
    right = tuple(2 * qh[r] * ah[r] + int(r in (0, 1)) * qc * ac for r in range(5))
    require(all(isinstance(value, (int, F)) and F(value).denominator == 1
                for value in left + right + currents + ah + (ac,)), "INTEGER_CONTINUITY")
    return left, right, currents, ah, ac


def integer_tangent(numerators, denominator, parameter, parameter_denominator, epsilon):
    horizon = len(numerators[H]) - 1
    result = editable(state_scale(20 * parameter_denominator, numerators))
    for n in range(1, horizon):
        qh = minus(numerators[H][n + 1], numerators[H][n - 1])
        qc = numerators[CHI][n + 1][0] - numerators[CHI][n - 1][0]
        for r in range(5):
            result[H][n][r] += 10 * epsilon * parameter[n][r] * qh[r]
        result[CHI][n][0] += 5 * epsilon * (parameter[n][0] + parameter[n][1]) * qc
        for k, value in enumerate(incidence(parameter[n])):
            result[SHIFT][n][k] += 20 * denominator * value
    for b in range(1, horizon + 1):
        difference = minus(parameter[b], parameter[b - 1])
        total = sum(difference)
        result[ALPHA][b][0] += 4 * denominator * total
        for r in range(5):
            result[LAMBDA][b][r] += 4 * denominator * (5 * difference[r] - total)
    output = freeze(result)
    require(all(F(value).denominator == 1 for value in state_values(output)), "INTEGER_TANGENT")
    new_denominator = 20 * denominator * parameter_denominator
    return state_scale(F(1, new_denominator), output), new_denominator


def physical_flat(state):
    return tuple(value for n in range(len(state[H])) for value in state[H][n] + state[CHI][n])


def sparse_generator(psi):
    horizon = len(psi) - 1
    rows = []
    for n in range(horizon + 1):
        values = psi[n] + (dot(SIGMA, psi[n]),)
        for component in range(6):
            row = {}
            if 0 < n < horizon and values[component]:
                row[6 * (n + 1) + component] = values[component] / F(2)
                row[6 * (n - 1) + component] = -values[component] / F(2)
            rows.append(row)
    return tuple(rows)


def sparse_apply(matrix, vector):
    return tuple(sum(value * vector[column] for column, value in row.items()) for row in matrix)


def sparse_commutator(psi_matrix, eta_matrix, vector):
    # The declared Lie convention is eta*psi - psi*eta.
    return minus(sparse_apply(eta_matrix, sparse_apply(psi_matrix, vector)),
                 sparse_apply(psi_matrix, sparse_apply(eta_matrix, vector)))


def closed_commutator(state, psi, eta):
    horizon = len(psi) - 1
    output = []
    psi6 = tuple(row + (dot(SIGMA, row),) for row in psi)
    eta6 = tuple(row + (dot(SIGMA, row),) for row in eta)
    x = tuple(state[H][n] + state[CHI][n] for n in range(horizon + 1))
    for n in range(horizon + 1):
        for r in range(6):
            value = F(0)
            if 0 < n < horizon:
                forward = (eta6[n][r] * psi6[n + 1][r] - psi6[n][r] * eta6[n + 1][r]) / F(4)
                backward = (eta6[n][r] * psi6[n - 1][r] - psi6[n][r] * eta6[n - 1][r]) / F(4)
                value = -(forward + backward) * x[n][r]
                if n + 2 <= horizon:
                    value += forward * x[n + 2][r]
                else:
                    require(forward == 0, "COMMUTATOR")
                if n - 2 >= 0:
                    value += backward * x[n - 2][r]
                else:
                    require(backward == 0, "COMMUTATOR")
            output.append(value)
    return tuple(output)


def rank(matrix):
    rows = [list(map(F, row)) for row in matrix]
    if not rows:
        return 0
    pivot_row = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(pivot_row, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        divisor = rows[pivot_row][column]
        rows[pivot_row] = [value / divisor for value in rows[pivot_row]]
        for i in range(len(rows)):
            if i != pivot_row:
                multiple = rows[i][column]
                rows[i] = [value - multiple * pivot_value
                           for value, pivot_value in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def authority_and_incidence():
    root = Path(__file__).resolve().parents[2]
    for name, size, digest in AUTHORITY:
        data = (root / "canon" / name).read_bytes()
        require(len(data) == size and sha256(data).hexdigest() == digest, "AUTHORITY")
    columns = []
    for r in range(5):
        vector = tuple(int(i == r) for i in range(5))
        columns.append(incidence(vector))
        require(scaled(M, laplacian(vector)) == laplacian_integer(vector), "INCIDENCE")
        expected = tuple(10721 * (5 * int(i == r) - 1) for i in range(5))
        require(laplacian_integer(green_adjoint_integer(vector)) == expected
                and green_adjoint_integer(laplacian_integer(vector)) == expected, "INCIDENCE")
    require(rank(columns) == 4 and rank(VERTEX_BASIS) == 4 and rank(CYCLE_BASIS) == 6,
            "INCIDENCE")
    require(all(sum(vector) == 0 for vector in VERTEX_BASIS)
            and all(divergence(vector) == (0,) * 5 for vector in CYCLE_BASIS), "INCIDENCE")
    require(incidence((1,) * 5) == (0,) * 10, "INCIDENCE")
    return len(AUTHORITY)


def audit_configurations():
    horizon, denominator = 5, 60
    directions = coordinate_directions(horizon)
    gradient_digest, noether_digest = sha256(), sha256()
    counts = dict(configurations=0, gradients=0, continuity=0, propagation=0,
                  integer_continuity=0, noether=0, integer_noether=0,
                  deformation=0, redefinition=0, tangent=0, commutator=0)
    for a in (-1, 0, 1):
        for seed in (0, 1):
            state, numerators, e_hom = configuration(a, seed, horizon, denominator)
            domain_check(state, horizon)
            require(state_scale(denominator, state) == numerators, "DOMAIN")
            counts["configurations"] += 1
            for index, direction in enumerate(directions):
                derivative = directional(state, direction, a, e_hom)
                plus_value = action_value(state_add(state, direction), a, e_hom)
                minus_value = action_value(state_add(state, direction, -1), a, e_hom)
                require(derivative == (plus_value - minus_value) / F(2), "GLOBAL_GRADIENT")
                gradient_digest.update(f"{a}|{seed}|{index}|{derivative}\n".encode("ascii"))
                counts["gradients"] += 1
            integer_pairs = {}
            continuity_values = {}
            for n in range(1, horizon):
                lhs, rhs = continuity_pair(state, n, a)
                require(lhs == rhs, "CONTINUITY")
                continuity_values[n] = lhs
                counts["continuity"] += 5
                ham_left, ham_right = constraint_pair(state, n, a)
                require(ham_left == ham_right, "CONSTRAINT_PROPAGATION")
                counts["propagation"] += 5
                ileft, iright, currents, ah, ac = integer_continuity_pair(numerators, n, a, denominator)
                require(ileft == iright
                        and scaled(F(1, 4 * M * denominator * denominator), ileft) == lhs,
                        "INTEGER_CONTINUITY")
                require(scaled(F(1, 4 * M * denominator * denominator), currents)
                        == edge_current(state, n), "INTEGER_CONTINUITY")
                rh, rc = residuals(state, n, a)
                require(scaled(F(1, M * denominator), ah) == rh
                        and F(ac, M * denominator) == rc, "INTEGER_CONTINUITY")
                integer_pairs[n] = ileft, iright
                counts["integer_continuity"] += 5
            parameters = parameter_arrays(a, seed, horizon)
            require(len(parameters) == 21, "CERTIFICATE")
            decoded = tuple(decode_parameter(v, q) for v, q in parameters)
            for parameter_index, ((v, qp), psi) in enumerate(zip(parameters, decoded)):
                d0, d1 = auxiliary_direction(psi), field_direction(state, psi)
                domain_check(d0, horizon)
                for n in range(1, horizon):
                    require(divergence(weighted(d0[SHIFT][n])) == laplacian(psi[n]),
                            "AUXILIARY_GAUGE")
                d0free, d0int = dual_derivatives(state, d0, a, e_hom)
                d1free, remainder = dual_derivatives(state, d1, a, e_hom)
                pairing = sum(dot(psi[n], continuity_values[n]) for n in range(1, horizon))
                require(d0free == 0 and d0int == pairing and d1free == -pairing
                        and d0int + d1free == 0, "NOETHER")
                counts["noether"] += 1
                integer_lhs = sum(dot(v[n], integer_pairs[n][0]) for n in range(1, horizon))
                integer_rhs = sum(dot(v[n], integer_pairs[n][1]) for n in range(1, horizon))
                scale = 4 * M * denominator * denominator * qp
                require(F(integer_lhs).denominator == F(integer_rhs).denominator == 1
                        and integer_lhs - integer_rhs == 0
                        and d0int * scale == integer_lhs
                        and d1free * scale == -integer_rhs, "INTEGER_NOETHER")
                counts["integer_noether"] += 1
                noether_digest.update(f"{a}|{seed}|{parameter_index}|{d0int}|{d1free}|{remainder}\n".encode("ascii"))
                pure = pure_multipliers(state, d0)
                hessian = physical_hessian(d1)
                for epsilon in (-1, 0, 1, 2):
                    total_direction = state_add(d0, d1, epsilon)
                    full_derivative = directional(state, total_direction, a, e_hom, epsilon)
                    require(full_derivative == epsilon * epsilon * remainder, "DEFORMATION")
                    counts["deformation"] += 1
                    displaced_back = state_add(state, d1, -epsilon)
                    redefined = physical_action(displaced_back, a) - F(epsilon * epsilon, 2) * hessian
                    require(action_value(pure, a, e_hom, epsilon) == redefined, "FIELD_REDEFINITION")
                    counts["redefinition"] += 1
                    lifted, new_d = integer_tangent(numerators, denominator, v, qp, epsilon)
                    require(new_d == 20 * denominator * qp
                            and lifted == state_add(state, total_direction), "INTEGER_TANGENT")
                    domain_check(lifted, horizon)
                    counts["tangent"] += 1
            generators = tuple(sparse_generator(psi) for psi in decoded[:20])
            physical = physical_flat(state)
            for i, j in combinations(range(20), 2):
                actual = sparse_commutator(generators[i], generators[j], physical)
                expected = closed_commutator(state, decoded[i], decoded[j])
                require(actual == expected, "COMMUTATOR")
                counts["commutator"] += 1
    expected_counts = dict(configurations=6, gradients=798, continuity=120, propagation=120,
                           integer_continuity=120, noether=126, integer_noether=126,
                           deformation=504, redefinition=504, tangent=504, commutator=1140)
    require(counts == expected_counts, "CERTIFICATE")
    return gradient_digest.hexdigest(), noether_digest.hexdigest()


def physical_unit(horizon, sector, time, site=0):
    state = editable(zeros(horizon))
    state[sector][time][site] = F(1)
    return freeze(state)


def parameter_units(horizon, entries):
    result = [[F(0)] * 5 for _ in range(horizon + 1)]
    for time, vector in entries:
        result[time] = list(map(F, vector))
    return tuple(tuple(row) for row in result)


def audit_witnesses():
    horizon, a, e_hom = 5, 0, F(0)
    controls = set()
    # 1. The full horizon includes the n=1 current in the n=2 derivative.
    state = editable(zeros(horizon))
    state[H][1] = [F(v, 40) for v in (6, 11, 11, 6, 6)]
    state[SHIFT][1][0] = F(1)
    neighbor = freeze(state)
    baseline = list(neighbor)
    baseline[SHIFT] = zeros(horizon)[SHIFT]
    baseline = tuple(baseline)
    increments = []
    limited = []
    for sector, site in tuple((H, r) for r in range(5)) + ((CHI, 0),):
        unit = physical_unit(horizon, sector, 2, site)
        base_derivative = directional(baseline, unit, a, e_hom)
        increments.append(directional(neighbor, unit, a, e_hom) - base_derivative)
        limited.append(directional(neighbor, unit, a, e_hom, current_sites={2}) - base_derivative)
    require(tuple(increments) == (F(29, 10368), F(29, 10368), F(0), F(0), F(0), F(-17, 51840))
            and tuple(limited) == (0,) * 6, "NEIGHBOR_WITNESS")
    controls.add("global_neighbor_currents")
    # 2. The first-order cancellation has a nonzero second-order remainder.
    state = editable(zeros(horizon))
    state[H][3][0] = F(1)
    state[ALPHA][3][0] = F(1)
    remainder_state = freeze(state)
    psi = parameter_units(horizon, ((2, (1, 0, 0, 0, 0)), (3, (1, 0, 0, 0, 0))))
    d0, d1 = auxiliary_direction(psi), field_direction(remainder_state, psi)
    d0free, d0int = dual_derivatives(remainder_state, d0, a, e_hom)
    d1free, remainder = dual_derivatives(remainder_state, d1, a, e_hom)
    direction = state_add(d0, d1)
    exact = directional(remainder_state, direction, a, e_hom)
    require(d0free == 0 and d0int == F(1, 2) and d1free == F(-1, 2)
            and remainder == exact == F(115, 324), "REMAINDER_WITNESS")
    controls.add("second_order_remainder")
    # 3. A joint cubic displacement needs a true derivative.
    naive = (action_value(state_add(remainder_state, direction), a, e_hom)
             - action_value(state_add(remainder_state, direction, -1), a, e_hom)) / F(2)
    central_defect = naive - exact
    require(central_defect == F(-1, 8), "CENTRAL_WITNESS")
    controls.add("naive_centered_difference")
    # 4. The first-order field redefinition leaves the quadratic remainder.
    pure = pure_multipliers(remainder_state, d0)
    shifted_action = physical_action(state_add(remainder_state, d1, -1), a)
    redefinition_defect = action_value(pure, a, e_hom) - shifted_action
    require(redefinition_defect == F(-115, 648)
            and redefinition_defect == -physical_hessian(d1) / F(2), "FIELD_REDEFINITION")
    controls.add("field_redefinition_remainder")
    # 5. Wrong sign for the physical completion.
    require(d0int - d1free == 1 and d0int + d1free == 0, "CONTROL")
    controls.add("wrong_completion_sign")
    # 6. Removing the homogeneous part loses the mean contribution.
    no_alpha = list(d0)
    no_alpha[ALPHA] = zeros(horizon)[ALPHA]
    defect = dual_derivatives(remainder_state, tuple(no_alpha), a, e_hom)[1] + d1free
    require(defect == F(-1, 10), "CONTROL")
    controls.add("omitted_homogeneous_lapse")
    # 7. The dipole interaction current is required for the same physical law.
    state = editable(zeros(horizon))
    state[H][2][0] = F(1)
    state[CHI][3][0] = F(1)
    current_state = freeze(state)
    current_psi = parameter_units(horizon, ((2, (1, 0, 0, 0, 0)),))
    current_d0, current_d1 = auxiliary_direction(current_psi), field_direction(current_state, current_psi)
    truncated_int = dual_derivatives(current_state, current_d0, a, e_hom, include_interaction=False)[1]
    full_free = dual_derivatives(current_state, current_d1, a, e_hom)[0]
    require(truncated_int + full_free == F(-1, 1296), "CONTROL")
    controls.add("omitted_interaction_current")
    # 8. Co-closure is an actual domain condition in the auxiliary symmetry.
    state = editable(zeros(horizon))
    state[MOM][2][0] = F(1)
    ambient_state = freeze(state)
    domain_check(ambient_state, horizon, admit_ambient_p=True)
    require(divergence(ambient_state[MOM][2]) != (0,) * 5
            and dual_derivatives(ambient_state, current_d0, a, e_hom)[0] == -2, "CONTROL")
    controls.add("dropped_coclosure")
    # 9. A two-step commutator cannot be a nearest-time generator here.
    state = editable(zeros(horizon))
    for n in range(horizon + 1):
        state[H][n] = [F(1, 5)] * 5
    state[H][4] = [F(1, 5) + value for value in DIPOLE]
    nonclosure_state = freeze(state)
    psi = parameter_units(horizon, ((2, DIPOLE),))
    eta = parameter_units(horizon, ((3, DIPOLE),))
    bracket = sparse_commutator(sparse_generator(psi), sparse_generator(eta), physical_flat(nonclosure_state))
    require(bracket == closed_commutator(nonclosure_state, psi, eta), "COMMUTATOR")
    nonclosure = bracket[12:17]
    require(nonclosure == (F(-1, 4), F(1, 4), F(0), F(0), F(0))
            and minus(nonclosure_state[H][3], nonclosure_state[H][1]) == (0,) * 5, "NONCLOSURE")
    for r in range(5):
        zeta = parameter_units(horizon, ((2, tuple(int(i == r) for i in range(5))),))
        require(field_direction(nonclosure_state, zeta)[H][2] == (0,) * 5, "NONCLOSURE")
    controls.add("nearest_time_nonclosure")
    # 10. Mean-zero parameters need not preserve the fixed-mean field family.
    escape = field_direction(nonclosure_state, eta)
    require(all(sum(row) == 1 for row in nonclosure_state[H])
            and all(sum(row) == 0 for row in eta)
            and sum(escape[H][3]) == 1, "CONTROL")
    controls.add("fixed_mean_escape")
    require(len(controls) == 10, "CERTIFICATE")
    return tuple(increments), remainder, central_defect, redefinition_defect, nonclosure


def certificate():
    authority = authority_and_incidence()
    gradient_digest, noether_digest = audit_configurations()
    neighbor, remainder, central_defect, redefinition_defect, nonclosure = audit_witnesses()
    lines = (
        "CERTIFICATE=" + PROBE,
        "AUTHORITY_FILES=" + str(authority),
        "GLOBAL_CONFIGURATIONS=6",
        "GLOBAL_VARIATIONS=798",
        "CONTINUITY_VERTICES=120",
        "CONSTRAINT_PROPAGATION_VERTICES=120",
        "INTEGER_CONTINUITY_VERTICES=120",
        "NOETHER_IDENTITIES=126",
        "INTEGER_NOETHER_IDENTITIES=126",
        "DEFORMATION_CHECKS=504",
        "FIELD_REDEFINITION_CHECKS=504",
        "INTEGER_TANGENT_CHECKS=504",
        "COMMUTATOR_CHECKS=1140",
        "GLOBAL_GRADIENT_SHA256=" + gradient_digest,
        "NOETHER_PAYLOAD_SHA256=" + noether_digest,
        "GLOBAL_NEIGHBOR_GRADIENT=" + ",".join(map(str, neighbor[:5])) + ";" + str(neighbor[5]),
        "SECOND_ORDER_REMAINDER=" + str(remainder),
        "NAIVE_CENTRAL_DEFECT=" + str(central_defect),
        "FIELD_REDEFINITION_DEFECT=" + str(redefinition_defect),
        "GENERATOR_NONCLOSURE=" + ",".join(map(str, nonclosure)),
        "NEGATIVE_CONTROLS=10",
        "CERTIFICATE_RESULT=PASS",
    )
    require(len(lines) == 22, "CERTIFICATE")
    return ("\n".join(lines) + "\n").encode("ascii")


def main():
    try:
        output = certificate()
    except ScientificFailure as failure:
        output = ("FALSIFIER=" + failure.key + "\nRESULT=FAIL\n").encode("ascii")
    sys.stdout.buffer.write(output)


if __name__ == "__main__":
    main()
