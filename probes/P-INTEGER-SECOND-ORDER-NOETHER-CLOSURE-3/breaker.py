#!/usr/bin/env python3
"""Independent dual-number and sparse-matrix audit of second-order Noether closure.

Written from PREREG.md using nested 7-sector time arrays, form (3.7b) of S_2,
first-order nilpotent Dual automatic differentiation, and 36x36 sparse temporal
generator matrices. No scientific execution or import before the public pin.
"""

from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import sys


PROBE = "P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-3"
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
    "AUXILIARY_GAUGE", "NOETHER", "SECOND_ORDER_NOETHER",
    "INTEGER_SECOND_ORDER_NOETHER", "DEFORMATION",
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


def state_tangent(dual_state):
    return tuple(tuple(tuple(entry.tangent if isinstance(entry, Dual) else F(0)
                             for entry in row)
                       for row in sector)
                 for sector in dual_state)


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


def energy_density_derivative(state, direction, bond, a):
    older, now = state[H][bond - 1], state[H][bond]
    d_old, d_now = direction[H][bond - 1], direction[H][bond]
    cp, c = state[CHI][bond - 1][0], state[CHI][bond][0]
    d_cp, d_c = direction[CHI][bond - 1][0], direction[CHI][bond][0]
    output = [(now[r] - older[r]) * (d_now[r] - d_old[r]) for r in range(5)]
    edge_old, edge_now = incidence(older), incidence(now)
    d_edge_old, d_edge_now = incidence(d_old), incidence(d_now)
    for k, (tail, head, weight) in enumerate(EDGES):
        share = F(weight, 4 * M) * (edge_old[k] * d_edge_now[k] + d_edge_old[k] * edge_now[k])
        output[tail] += share
        output[head] += share
    source = ((c - cp) * (d_c - d_cp) + (c * d_cp + d_c * cp) / F(2)
              - F(a, 8) * (d_c + d_cp))
    for r in range(5):
        output[r] += (SIGMA[r] * source
                      - F(DIPOLE[r], 2 * M) * (cp * d_now[r] + d_cp * now[r]
                                               + c * d_old[r] + d_c * older[r]))
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


def edge_current_derivative(state, direction, time, include_interaction=True):
    h, c = state[H], state[CHI]
    dh, dc = direction[H], direction[CHI]
    temporal = minus(h[time + 1], h[time - 1])
    d_temporal = minus(dh[time + 1], dh[time - 1])
    spatial = incidence(h[time])
    d_spatial = incidence(dh[time])
    result = [F(weight, 4 * M) * (spatial[k] * (d_temporal[tail] + d_temporal[head])
                                  + d_spatial[k] * (temporal[tail] + temporal[head]))
              for k, (tail, head, weight) in enumerate(EDGES)]
    if include_interaction:
        qc = c[time + 1][0] - c[time - 1][0]
        d_qc = dc[time + 1][0] - dc[time - 1][0]
        result[0] -= F(1, 4 * M) * (qc * (dh[time][0] + dh[time][1])
                                    + d_qc * (h[time][0] + h[time][1]))
    return tuple(result)


def residuals(state, time, a):
    h, c = state[H], state[CHI]
    lap = laplacian(h[time])
    rh = tuple(h[time + 1][r] - 2 * h[time][r] + h[time - 1][r]
               + lap[r] - G * c[time][0] * DIPOLE[r] for r in range(5))
    rc = (c[time + 1][0] - c[time][0] + c[time - 1][0]
          - F(a, 4) - G * dot(DIPOLE, h[time]))
    return rh, rc


def dressing_array(state):
    horizon = len(state[H]) - 1
    alpha, lam = state[ALPHA], state[LAMBDA]
    rows = [tuple(F(0) for _ in range(5)) for _ in range(horizon + 1)]
    running = tuple(F(0) for _ in range(5))
    for b in range(1, horizon):
        mu = tuple(alpha[b][0] + lam[b][r] for r in range(5))
        running = plus(running, mu)
        rows[b] = running
    return tuple(rows)


def field_direction(state, psi):
    horizon = len(psi) - 1
    result = editable(zeros(horizon))
    for n in range(1, horizon):
        qh = minus(state[H][n + 1], state[H][n - 1])
        qc = state[CHI][n + 1][0] - state[CHI][n - 1][0]
        result[H][n] = [psi[n][r] * qh[r] / F(2) for r in range(5)]
        result[CHI][n] = [dot(SIGMA, psi[n]) * qc / F(2)]
    return freeze(result)


def second_order_field_direction(state, psi):
    return field_direction(field_direction(state, psi), dressing_array(state))


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


def s2_form_b(state, a, include_interaction=True, current_sites=None):
    """Form (3.7b) of S_2[x, M], valid on both Fraction and Dual entries."""
    horizon = len(state[H]) - 1
    psi_m = dressing_array(state)
    y = field_direction(state, psi_m)
    z = field_direction(y, psi_m)
    alpha, lam, shift = state[ALPHA], state[LAMBDA], state[SHIFT]
    dx_sint = F(0)
    for b in range(1, horizon + 1):
        de = energy_density_derivative(state, y, b, a)
        dx_sint -= alpha[b][0] * sum(de)
        dx_sint -= dot(lam[b], de)
    for n in range(1, horizon):
        if current_sites is None or n in current_sites:
            dj = edge_current_derivative(state, y, n, include_interaction)
            dx_sint += dot(shift[n], dj)
    dx_aauto_z = F(0)
    for n in range(1, horizon):
        rh, rc = residuals(state, n, a)
        dx_aauto_z -= dot(rh, z[H][n]) + rc * z[CHI][n][0]
    return -dx_sint - physical_hessian(y) / F(2) - dx_aauto_z


def action_parts(state, a, e_hom, include_interaction=True, current_sites=None):
    """Complete global (S_0, S_int, S_2), valid on Fraction and Dual entries."""
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
    second_order = s2_form_b(state, a, include_interaction, current_sites)
    return free, interaction, second_order


def action_value(state, a, e_hom, epsilon=1, **options):
    free, interaction, second_order = action_parts(state, a, e_hom, **options)
    return free + epsilon * interaction + (epsilon ** 2) * second_order


def physical_action(state, a):
    physical = list(zeros(len(state[H]) - 1))
    physical[H], physical[CHI] = state[H], state[CHI]
    return action_parts(tuple(physical), a, F(0))[0]


def dual_derivatives(state, direction, a, e_hom, **options):
    parts = action_parts(state_dual(state, direction), a, e_hom, **options)
    return tuple(value.tangent if isinstance(value, Dual) else F(0) for value in parts)


def directional(state, direction, a, e_hom, epsilon=1, **options):
    free, interaction, second_order = dual_derivatives(state, direction, a, e_hom, **options)
    return free + epsilon * interaction + (epsilon ** 2) * second_order


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


def hat_direction(state, psi, epsilon=1):
    d0 = auxiliary_direction(psi)
    d1 = field_direction(state, psi)
    d2 = second_order_field_direction(state, psi)
    return state_add(state_add(d0, d1, epsilon), d2, epsilon ** 2)


def pure_multipliers(state, d0):
    result = list(state)
    for sector in (ALPHA, LAMBDA, SHIFT):
        result[sector] = d0[sector]
    return tuple(result)


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


def integer_second_order_noether(numerators, denominator, parameter, parameter_denominator,
                                 a, d0s2, d1si, d2s0):
    horizon = len(numerators[H]) - 1
    scale_int = 16 * M * (denominator ** 3) * parameter_denominator
    psi_hat = [(0,) * 5 for _ in range(horizon + 1)]
    running = (0,) * 5
    for b in range(1, horizon):
        ab = int(F(numerators[ALPHA][b][0]))
        lb = tuple(int(F(v)) for v in numerators[LAMBDA][b])
        running = tuple(r + ab + z for r, z in zip(running, lb))
        psi_hat[b] = running
    ytilde_h = [(0,) * 5 for _ in range(horizon + 1)]
    ytilde_c = [0] * (horizon + 1)
    for n in range(1, horizon):
        qh = minus(numerators[H][n + 1], numerators[H][n - 1])
        qc = numerators[CHI][n + 1][0] - numerators[CHI][n - 1][0]
        ytilde_h[n] = tuple(parameter[n][r] * int(F(qh[r])) for r in range(5))
        ytilde_c[n] = (parameter[n][0] + parameter[n][1]) * int(F(qc))
    delta_hat_2 = 0
    for n in range(1, horizon):
        z2_h = tuple(psi_hat[n][r] * (ytilde_h[n + 1][r] - ytilde_h[n - 1][r]) for r in range(5))
        z2_c = (psi_hat[n][0] + psi_hat[n][1]) * (ytilde_c[n + 1] - ytilde_c[n - 1])
        _, _, _, ah, ac = integer_continuity_pair(numerators, n, a, denominator)
        delta_hat_2 -= 4 * sum(int(F(ah[r])) * z2_h[r] for r in range(5)) + int(F(ac)) * z2_c
    for val in (scale_int * d0s2, scale_int * d1si, scale_int * d2s0):
        require(F(val).denominator == 1, "INTEGER_SECOND_ORDER_NOETHER")
    delta_hat_0 = int(F(scale_int * d0s2))
    delta_hat_1 = int(F(scale_int * d1si))
    require(delta_hat_2 == int(F(scale_int * d2s0)), "INTEGER_SECOND_ORDER_NOETHER")
    require(delta_hat_0 + delta_hat_1 + delta_hat_2 == 0, "INTEGER_SECOND_ORDER_NOETHER")


def integer_second_order_tangent(numerators, denominator, parameter, parameter_denominator, epsilon):
    horizon = len(numerators[H]) - 1
    result = editable(state_scale(80 * denominator * parameter_denominator, numerators))
    psi_hat = [(0,) * 5 for _ in range(horizon + 1)]
    running = (0,) * 5
    for b in range(1, horizon):
        ab = int(F(numerators[ALPHA][b][0]))
        lb = tuple(int(F(v)) for v in numerators[LAMBDA][b])
        running = tuple(r + ab + z for r, z in zip(running, lb))
        psi_hat[b] = running
    ytilde_h = [(0,) * 5 for _ in range(horizon + 1)]
    ytilde_c = [0] * (horizon + 1)
    for n in range(1, horizon):
        qh = minus(numerators[H][n + 1], numerators[H][n - 1])
        qc = numerators[CHI][n + 1][0] - numerators[CHI][n - 1][0]
        ytilde_h[n] = tuple(parameter[n][r] * qh[r] for r in range(5))
        ytilde_c[n] = (parameter[n][0] + parameter[n][1]) * qc
    for n in range(1, horizon):
        for r in range(5):
            result[H][n][r] += (
                40 * denominator * epsilon * ytilde_h[n][r]
                + 20 * (epsilon ** 2) * psi_hat[n][r] * (ytilde_h[n + 1][r] - ytilde_h[n - 1][r])
            )
        result[CHI][n][0] += (
            20 * denominator * epsilon * ytilde_c[n]
            + 5 * (epsilon ** 2) * (psi_hat[n][0] + psi_hat[n][1]) * (ytilde_c[n + 1] - ytilde_c[n - 1])
        )
        for k, value in enumerate(incidence(parameter[n])):
            result[SHIFT][n][k] += 80 * (denominator ** 2) * value
    for b in range(1, horizon + 1):
        difference = minus(parameter[b], parameter[b - 1])
        total = sum(difference)
        result[ALPHA][b][0] += 16 * (denominator ** 2) * total
        for r in range(5):
            result[LAMBDA][b][r] += 16 * (denominator ** 2) * (5 * difference[r] - total)
    output = freeze(result)
    require(all(F(value).denominator == 1 for value in state_values(output)), "INTEGER_TANGENT")
    new_denominator = 80 * (denominator ** 2) * parameter_denominator
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
    return minus(sparse_apply(eta_matrix, sparse_apply(psi_matrix, vector)),
                 sparse_apply(psi_matrix, sparse_apply(eta_matrix, vector)))


def sparse_residuals(state, psi, eta):
    vec = physical_flat(state)
    g_psi = sparse_generator(psi)
    g_eta = sparse_generator(eta)
    g_m = sparse_generator(dressing_array(state))
    bare = sparse_commutator(g_psi, g_eta, vec)
    cross = sparse_commutator(g_eta, g_psi, vec)
    m_psi = sparse_apply(g_m, sparse_apply(g_psi, vec))
    m_eta = sparse_apply(g_m, sparse_apply(g_eta, vec))
    cross_3 = minus(sparse_apply(g_eta, m_psi), sparse_apply(g_psi, m_eta))
    c3 = plus(cross_3, sparse_apply(g_m, bare))
    c4 = sparse_apply(g_m, cross_3)
    return bare, cross, c3, c4


def dual_lie_commutator(state, psi, eta, epsilon=1):
    v_psi = hat_direction(state, psi, epsilon)
    v_eta = hat_direction(state, eta, epsilon)
    d_psi_eta = state_tangent(hat_direction(state_dual(state, v_psi), eta, epsilon))
    d_eta_psi = state_tangent(hat_direction(state_dual(state, v_eta), psi, epsilon))
    return state_add(d_psi_eta, d_eta_psi, -1)


def authority_and_incidence():
    root = Path(__file__).resolve().parents[2]
    count = 0
    for name, expected_size, expected_hash in AUTHORITY:
        raw = (root / "canon" / name).read_bytes()
        require(len(raw) == expected_size and sha256(raw).hexdigest() == expected_hash, "AUTHORITY")
        count += 1
    for basis in VERTEX_BASIS:
        require(sum(basis) == 0, "INCIDENCE")
        require(laplacian(basis) == scaled(G, laplacian_integer(basis)), "INCIDENCE")
        require(laplacian_integer(green_adjoint_integer(basis)) == scaled(53605, basis), "INCIDENCE")
    for idx, cycle in enumerate(CYCLE_BASIS):
        require(divergence(cycle) == (0,) * 5 and cycle[4 + idx] == 1, "INCIDENCE")
    return count


def audit_configurations():
    horizon = 5
    directions = coordinate_directions(horizon)
    gradient_digest = sha256()
    second_order_digest = sha256()
    counts = dict(configurations=0, gradients=0, continuity=0, propagation=0,
                  integer_continuity=0, first_noether=0, second_noether=0,
                  integer_second_noether=0, deformation=0, redefinition=0,
                  tangent=0, commutator=0)
    for a in (-1, 0, 1):
        for seed in (0, 1):
            state, numerators, e_hom = configuration(a, seed, horizon)
            domain_check(state, horizon)
            counts["configurations"] += 1
            for index, direction in enumerate(directions):
                d_one = directional(state, direction, a, e_hom, epsilon=1)
                d_zero = directional(state, direction, a, e_hom, epsilon=0)
                c_one = (action_value(state_add(state, direction, 1), a, e_hom, 1)
                         - action_value(state_add(state, direction, -1), a, e_hom, 1)) / F(2)
                c_zero = (action_value(state_add(state, direction, 1), a, e_hom, 0)
                          - action_value(state_add(state, direction, -1), a, e_hom, 0)) / F(2)
                require(d_one == c_one and d_zero == c_zero, "GLOBAL_GRADIENT")
                gradient_digest.update(f"{a}|{seed}|{index}|{d_one}\n".encode("ascii"))
                counts["gradients"] += 1
            for n in range(1, horizon):
                c_left, c_right = continuity_pair(state, n, a)
                p_left, p_right = constraint_pair(state, n, a)
                i_left, i_right, _, _, _ = integer_continuity_pair(numerators, n, a, 60)
                for r in range(5):
                    require(c_left[r] == c_right[r], "CONTINUITY")
                    require(p_left[r] == p_right[r], "CONSTRAINT_PROPAGATION")
                    require(i_left[r] == i_right[r], "INTEGER_CONTINUITY")
                    counts["continuity"] += 1
                    counts["propagation"] += 1
                    counts["integer_continuity"] += 1
            parameters = parameter_arrays(a, seed, horizon)
            for p_index, (p_num, p_den) in enumerate(parameters):
                psi = decode_parameter(p_num, p_den)
                d0 = auxiliary_direction(psi)
                d1 = field_direction(state, psi)
                d2 = second_order_field_direction(state, psi)
                d0_free, d0_int, d0_s2 = dual_derivatives(state, d0, a, e_hom)
                d1_free, d1_int, d1_s2 = dual_derivatives(state, d1, a, e_hom)
                d2_free, d2_int, d2_s2 = dual_derivatives(state, d2, a, e_hom)
                require(d0_free == 0, "AUXILIARY_GAUGE")
                require(d0_int + d1_free == 0, "NOETHER")
                counts["first_noether"] += 1
                require(d0_s2 + d1_int + d2_free == 0, "SECOND_ORDER_NOETHER")
                counts["second_noether"] += 1
                integer_second_order_noether(numerators, 60, p_num, p_den, a, d0_s2, d1_int, d2_free)
                counts["integer_second_noether"] += 1
                w3 = d1_s2 + d2_int
                w4 = d2_s2
                second_order_digest.update(
                    f"{a}|{seed}|{p_index}|{d0_s2}|{d1_int}|{d2_free}|{w3}|{w4}\n".encode("ascii")
                )
                pure = pure_multipliers(state, d0)
                for epsilon in (-1, 0, 1, 2):
                    direction = hat_direction(state, psi, epsilon)
                    d_exact = directional(state, direction, a, e_hom, epsilon)
                    p_vals = [action_value(state_add(state, direction, step), a, e_hom, epsilon)
                              for step in (2, 1, -1, -2)]
                    four_point = (-p_vals[0] + 8 * p_vals[1] - 8 * p_vals[2] + p_vals[3]) / F(12)
                    require(d_exact == four_point == (epsilon ** 3) * w3 + (epsilon ** 4) * w4,
                            "DEFORMATION")
                    counts["deformation"] += 1
                    shifted = physical_action(state_add(state, d1, -epsilon), a)
                    require(action_value(pure, a, e_hom, epsilon) == shifted, "FIELD_REDEFINITION")
                    counts["redefinition"] += 1
                    lifted, new_den = integer_second_order_tangent(numerators, 60, p_num, p_den, epsilon)
                    require(lifted == state_add(state, direction) and new_den == 80 * 3600 * p_den,
                            "INTEGER_TANGENT")
                    domain_check(lifted, horizon)
                    counts["tangent"] += 1
            for (i, _), (j, _) in combinations(parameters[:20], 2):
                psi = decode_parameter(i, 1)
                eta = decode_parameter(j, 1)
                bare, cross, c3, c4 = sparse_residuals(state, psi, eta)
                require(plus(bare, cross) == (F(0),) * 36, "COMMUTATOR")
                comm_state = dual_lie_commutator(state, psi, eta, epsilon=1)
                require(physical_flat(comm_state) == plus(c3, c4), "COMMUTATOR")
                for sector in (TAU, MOM, ALPHA, LAMBDA, SHIFT):
                    require(comm_state[sector] == zeros(horizon)[sector], "COMMUTATOR")
                counts["commutator"] += 1
    expected_counts = dict(configurations=6, gradients=798, continuity=120, propagation=120,
                           integer_continuity=120, first_noether=126, second_noether=126,
                           integer_second_noether=126, deformation=504, redefinition=504,
                           tangent=504, commutator=1140)
    require(counts == expected_counts, "CERTIFICATE")
    return gradient_digest.hexdigest(), second_order_digest.hexdigest()


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
    # 1. GLOBAL_NEIGHBOR_GRADIENT
    state = editable(zeros(horizon))
    state[H][1] = [F(v, 40) for v in (6, 11, 11, 6, 6)]
    state[SHIFT][1][0] = F(1)
    neighbor = freeze(state)
    baseline = list(neighbor)
    baseline[SHIFT] = zeros(horizon)[SHIFT]
    baseline = tuple(baseline)
    increments, limited = [], []
    for sector, site in tuple((H, r) for r in range(5)) + ((CHI, 0),):
        unit = physical_unit(horizon, sector, 2, site)
        base_derivative = directional(baseline, unit, a, e_hom)
        increments.append(directional(neighbor, unit, a, e_hom) - base_derivative)
        limited.append(directional(neighbor, unit, a, e_hom, current_sites={2}) - base_derivative)
    require(tuple(increments) == (F(29, 10368), F(29, 10368), F(0), F(0), F(0), F(-17, 51840))
            and tuple(limited) == (0,) * 6, "NEIGHBOR_WITNESS")
    controls.add("global_neighbor_currents")

    # 2, 3, 4, 5, 6. SECOND_ORDER_SPLIT, OMIT_S2_DEFECT, OMIT_DELTA2_DEFECT,
    # THIRD_FOURTH_REMAINDERS, QUARTIC_CENTRAL_DEFECT, PURE_GAUGE_S2_COMPLETION,
    # OMIT_HOMOGENEOUS_LAPSE.
    state = editable(zeros(horizon))
    state[H][3][0] = F(1)
    state[ALPHA][3][0] = F(1)
    rem_state = freeze(state)
    psi = parameter_units(horizon, ((2, (1, 0, 0, 0, 0)), (3, (1, 0, 0, 0, 0))))
    d0 = auxiliary_direction(psi)
    d1 = field_direction(rem_state, psi)
    d2 = second_order_field_direction(rem_state, psi)
    d0_free, d0_int, d0_s2 = dual_derivatives(rem_state, d0, a, e_hom)
    d1_free, d1_int, d1_s2 = dual_derivatives(rem_state, d1, a, e_hom)
    d2_free, d2_int, d2_s2 = dual_derivatives(rem_state, d2, a, e_hom)
    require((d0_s2, d1_int, d2_free) == (F(0), F(115, 324), F(-115, 324)), "REMAINDER_WITNESS")
    require(d0_s2 + d1_int == F(115, 324), "CONTROL")
    controls.add("omit_delta2_defect")
    w3 = d1_s2 + d2_int
    w4 = d2_s2
    require((d1_s2, d2_int, w3, w4, w3 + w4)
            == (F(-1, 8), F(1, 4), F(1, 8), F(-115, 1296), F(47, 1296)), "REMAINDER_WITNESS")
    direction = hat_direction(rem_state, psi, 1)
    exact = directional(rem_state, direction, a, e_hom, 1)
    naive = (action_value(state_add(rem_state, direction, 1), a, e_hom, 1)
             - action_value(state_add(rem_state, direction, -1), a, e_hom, 1)) / F(2)
    central_defect = naive - exact
    require(exact == F(47, 1296) and central_defect == F(1, 32), "CENTRAL_WITNESS")
    controls.add("quartic_central_defect")
    pure = pure_multipliers(rem_state, d0)
    s2_pure = action_parts(pure, a, e_hom)[2]
    redef_defect = action_value(pure, a, e_hom, 1) - physical_action(state_add(rem_state, d1, -1), a)
    require(s2_pure == F(115, 648) and redef_defect == F(0), "FIELD_REDEFINITION")
    no_alpha = list(d0)
    no_alpha[ALPHA] = zeros(horizon)[ALPHA]
    require(dual_derivatives(rem_state, tuple(no_alpha), a, e_hom)[1] + d1_free == F(-1, 10),
            "CONTROL")
    controls.add("omit_homogeneous_lapse")

    # Case B: alpha_2 = alpha_3 = 1
    state_b = editable(rem_state)
    state_b[ALPHA][2][0] = F(1)
    rem_state_b = freeze(state_b)
    d2_b = second_order_field_direction(rem_state_b, psi)
    split = (dual_derivatives(rem_state_b, d0, a, e_hom)[2],
             dual_derivatives(rem_state_b, d1, a, e_hom)[1],
             dual_derivatives(rem_state_b, d2_b, a, e_hom)[0])
    require(split == (F(115, 324), F(115, 324), F(-115, 162)) and sum(split) == 0,
            "REMAINDER_WITNESS")
    require(split[1] + split[2] == F(-115, 324), "CONTROL")
    controls.add("omit_s2_defect")

    # 7. OMIT_INTERACTION_CURRENT
    state = editable(zeros(horizon))
    state[H][2][0] = F(1)
    state[CHI][3][0] = F(1)
    cur_state = freeze(state)
    cur_psi = parameter_units(horizon, ((2, (1, 0, 0, 0, 0)),))
    cur_d0, cur_d1 = auxiliary_direction(cur_psi), field_direction(cur_state, cur_psi)
    require(dual_derivatives(cur_state, cur_d0, a, e_hom, include_interaction=False)[1]
            + dual_derivatives(cur_state, cur_d1, a, e_hom)[0] == F(-1, 1296), "CONTROL")
    controls.add("omit_interaction_current")

    # 8. DROP_COCLOSURE
    state = editable(zeros(horizon))
    state[MOM][2][0] = F(1)
    ambient_state = freeze(state)
    domain_check(ambient_state, horizon, admit_ambient_p=True)
    require(divergence(ambient_state[MOM][2]) != (0,) * 5
            and dual_derivatives(ambient_state, cur_d0, a, e_hom)[0] == -2, "CONTROL")
    controls.add("drop_coclosure")

    # 9, 10. EXTENDED_COMMUTATOR_CANCELLATION, WRONG_DELTA2_ORDER,
    # THIRD_ORDER_COMMUTATOR_RESIDUAL, FIXED_MEAN_ESCAPE
    state = editable(zeros(horizon))
    for n in range(horizon + 1):
        state[H][n] = [F(1, 5)] * 5
    state[H][4] = [F(1, 5) + value for value in DIPOLE]
    state[ALPHA][1][0] = F(1)
    state[ALPHA][2][0] = F(-1)
    nc_state = freeze(state)
    psi_nc = parameter_units(horizon, ((2, DIPOLE),))
    eta_nc = parameter_units(horizon, ((3, DIPOLE),))
    bare, cross, c3, c4 = sparse_residuals(nc_state, psi_nc, eta_nc)
    bare_h2 = bare[12:17]
    cross_h2 = cross[12:17]
    sum_h2 = plus(bare_h2, cross_h2)
    require(bare_h2 == (F(-1, 4), F(1, 4), F(0), F(0), F(0))
            and cross_h2 == (F(1, 4), F(-1, 4), F(0), F(0), F(0))
            and sum_h2 == (F(0),) * 5, "COMMUTATOR")
    require(minus(bare_h2, cross_h2) == (F(-1, 2), F(1, 2), F(0), F(0), F(0)), "CONTROL")
    controls.add("wrong_delta2_order")
    c3_h1 = c3[6:11]
    require(c3_h1 == (F(-1, 8), F(1, 8), F(0), F(0), F(0)) and c4[6:11] == (F(0),) * 5,
            "NONCLOSURE")
    require(dual_lie_commutator(nc_state, psi_nc, eta_nc, 1)[H][1] == c3_h1, "NONCLOSURE")
    controls.add("third_order_commutator_residual")
    escape = field_direction(nc_state, eta_nc)
    require(all(sum(row) == 1 for row in nc_state[H])
            and all(sum(row) == 0 for row in eta_nc)
            and sum(escape[H][3]) == 1, "CONTROL")
    controls.add("fixed_mean_escape")
    require(len(controls) == 10, "CERTIFICATE")
    return (
        tuple(increments), split, (w3, w4, w3 + w4), central_defect,
        (s2_pure, redef_defect), (bare_h2, cross_h2, sum_h2), c3_h1,
    )


def certificate():
    authority = authority_and_incidence()
    gradient_digest, second_order_digest = audit_configurations()
    (neighbor, split, remainders, central_defect,
     pure_completion, comm_cancel, comm_res) = audit_witnesses()
    lines = (
        "CERTIFICATE=" + PROBE,
        "AUTHORITY_FILES=" + str(authority),
        "GLOBAL_CONFIGURATIONS=6",
        "GLOBAL_VARIATIONS=798",
        "CONTINUITY_VERTICES=120",
        "CONSTRAINT_PROPAGATION_VERTICES=120",
        "INTEGER_CONTINUITY_VERTICES=120",
        "FIRST_ORDER_NOETHER=126",
        "SECOND_ORDER_NOETHER=126",
        "INTEGER_SECOND_ORDER_NOETHER=126",
        "DEFORMATION_CHECKS=504",
        "PURE_GAUGE_REDEFINITION_CHECKS=504",
        "INTEGER_SECOND_ORDER_TANGENT_CHECKS=504",
        "EXTENDED_COMMUTATOR_CHECKS=1140",
        "GLOBAL_S2_GRADIENT_SHA256=" + gradient_digest,
        "SECOND_ORDER_PAYLOAD_SHA256=" + second_order_digest,
        "GLOBAL_NEIGHBOR_GRADIENT=" + ",".join(map(str, neighbor[:5])) + ";" + str(neighbor[5]),
        "SECOND_ORDER_SPLIT=" + ",".join(map(str, split)),
        "THIRD_FOURTH_REMAINDERS=" + ",".join(map(str, remainders)),
        "QUARTIC_CENTRAL_DEFECT=" + str(central_defect),
        "PURE_GAUGE_S2_COMPLETION=" + str(pure_completion[0]) + ";" + str(pure_completion[1]),
        "EXTENDED_COMMUTATOR_CANCELLATION=" + ";".join(",".join(map(str, part)) for part in comm_cancel),
        "THIRD_ORDER_COMMUTATOR_RESIDUAL=" + ",".join(map(str, comm_res)),
        "NEGATIVE_CONTROLS=10",
        "CERTIFICATE_RESULT=PASS",
    )
    require(len(lines) == 25, "CERTIFICATE")
    return ("\n".join(lines) + "\n").encode("ascii")


def main():
    try:
        output = certificate()
    except ScientificFailure as failure:
        output = ("FALSIFIER=" + failure.key + "\nRESULT=FAIL\n").encode("ascii")
    sys.stdout.buffer.write(output)


if __name__ == "__main__":
    main()
