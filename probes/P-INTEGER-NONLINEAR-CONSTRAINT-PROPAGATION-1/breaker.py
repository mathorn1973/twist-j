#!/usr/bin/env python3
"""Independent rational/direct-coordinate audit of cubic constraint propagation.

Written from this probe's PREREG.md without reading its primary or PROOF.md.
Uses rational physical evolution, direct 8-coordinate Hermitian transforms, and
4x4 Gaussian elimination on the mean-zero subspace e^perp to solve the discrete
Hamiltonian constraint 2 L tau = Pi_0 e_tot before comparing with the integer
constraint lift.

Do not execute or import before the complete public prospective pin is read
back. The program uses only exact integers and Fraction arithmetic.
"""

from fractions import Fraction as F
from hashlib import sha256
from math import lcm
from pathlib import Path
import sys


PROBE = "P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1"
M = 324
G = F(1, 324)
ELL = (1, -1, 0, 0, 0)
SIGMA = (F(1, 2), F(1, 2), F(0), F(0), F(0))
TWO_SIGMA = (1, 1, 0, 0, 0)
H_ZERO = (0, 0, 0, 0, 0, 0, 0, 0)
H_REFERENCE = (0, 0, 1, 0, 0, 0, 0, 0)
DELTA = F(253, 8684010)
ORIENTED_EDGES = tuple(
    (site, (site + step) % 5, 29 if step == 1 else 65,
     F(29, 324) if step == 1 else F(65, 324))
    for step in (1, 2) for site in range(5)
)

INITIAL = (
    ("0010", (0, 1, 1, 0, 0), (1, 1, 0, 0, 0), F(713, 2592), F(-1, 2)),
    ("0011", (0, 1, 1, 0, 0), (0, 1, 1, 0, 0), F(53, 432), F(-1, 2)),
    ("0100", (1, 1, 0, 0, 0), (1, 0, 0, 0, 1), F(713, 2592), F(0)),
    ("0101", (1, 1, 0, 0, 0), (1, 1, 0, 0, 0), F(53, 432), F(0)),
    ("0110", (0, 1, 1, 0, 0), (1, 0, 0, 0, 1), F(67, 162), F(-1, 2)),
    ("1001", (1, 0, 0, 0, 1), (0, 1, 1, 0, 0), F(67, 162), F(1, 2)),
    ("1010", (1, 1, 0, 0, 0), (1, 1, 0, 0, 0), F(53, 432), F(0)),
    ("1011", (1, 1, 0, 0, 0), (0, 1, 1, 0, 0), F(713, 2592), F(0)),
    ("1100", (1, 0, 0, 0, 1), (1, 0, 0, 0, 1), F(53, 432), F(1, 2)),
    ("1101", (1, 0, 0, 0, 1), (1, 1, 0, 0, 0), F(713, 2592), F(1, 2)),
)

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
    "AUTHORITY", "RING", "TRANSPORT", "HOLONOMY", "COST", "INITIAL_DATA",
    "INTEGER", "BARE_INVERSE", "FUNDED_INVERSE", "CONSERVATION", "BRANCH",
    "IMAGE_GUARD", "RECURRENCE", "MEAN", "SOURCE_READER", "LORENTZ",
    "SOURCE_BOUND", "EQUILIBRIUM", "ENERGY", "PRECISION", "GRAM",
    "GREEN", "CONTINUITY", "HAMILTONIAN_CONSTRAINT", "MOMENTUM_CONSTRAINT",
    "BIANCHI", "INTEGER_CONSTRAINT", "ACTION", "OFFSHELL_ACTION",
    "CANONICAL", "SYMPLECTIC", "FIXED_COUNTER", "CONTROL",
    "SHARP_BUDGET", "PERIOD", "CERTIFICATE", "BREAKER_BYTES",
))


class ScientificFailure(Exception):
    def __init__(self, key):
        if key not in FALSIFIERS:
            raise ValueError("unregistered falsifier key")
        self.key = key
        super().__init__(key)


def require(condition, key):
    if not condition:
        raise ScientificFailure(key)


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def square_norm(vector):
    return sum(value * value for value in vector)


def subtract(left, right):
    return tuple(a - b for a, b in zip(left, right))


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def times(factor, vector):
    return tuple(factor * value for value in vector)


def unit(size, site):
    return tuple(F(int(index == site)) for index in range(size))


def integer_tuple(value, size):
    return (isinstance(value, tuple) and len(value) == size
            and all(type(entry) is int for entry in value))


def comma(values):
    return ",".join(str(value) for value in values)


def incidence_b5(vertex_field):
    return tuple(vertex_field[head] - vertex_field[tail]
                 for tail, head, _, _ in ORIENTED_EDGES)


def divergence_b5t(edge_field):
    accum = [0] * 5
    for (tail, head, _, _), value in zip(ORIENTED_EDGES, edge_field):
        accum[tail] -= value
        accum[head] += value
    return tuple(accum)


def weight_edges(edge_field):
    return tuple(w * value for (_, _, _, w), value in zip(ORIENTED_EDGES, edge_field))


def int_weight_edges(edge_field):
    return tuple(mw * value for (_, _, mw, _), value in zip(ORIENTED_EDGES, edge_field))


def laplacian_int(field):
    return tuple(188 * field[r]
                 - 29 * (field[(r - 1) % 5] + field[(r + 1) % 5])
                 - 65 * (field[(r - 2) % 5] + field[(r + 2) % 5])
                 for r in range(5))


def adjoint_green_int(field):
    return tuple(188 * field[r]
                 - 65 * (field[(r - 1) % 5] + field[(r + 1) % 5])
                 - 29 * (field[(r - 2) % 5] + field[(r + 2) % 5])
                 for r in range(5))


def laplacian(field):
    return tuple(F(value, M) for value in laplacian_int(field))


def project_mean_zero(vertex_field):
    average = F(sum(vertex_field), 5)
    return tuple(F(value) - average for value in vertex_field)


def edge_form(left, right):
    total = F(0)
    for tail, head, _, w in ORIENTED_EDGES:
        total += w * (left[head] - left[tail]) * (right[head] - right[tail])
    return total


def stiffness(vector):
    field, source = vector[:5], vector[5]
    return tuple(value - G * source * dipole
                 for value, dipole in zip(laplacian(field), ELL)) + (
                     source - G * dot(ELL, field),)


def stiffness_form(left, right):
    return (edge_form(left[:5], right[:5]) + left[5] * right[5]
            - G * (left[5] * dot(ELL, right[:5]) + right[5] * dot(ELL, left[:5])))


def equilibrium(a):
    force = F(a, 4)
    field = tuple(F(1, 5) + force * entry / 8683757
                  for entry in (40986, -40986, 5832, 0, -5832))
    source = force * F(8684010, 8683757)
    return field + (source,)


def equilibrium_offset(a):
    force = F(a, 4)
    return F(4342005, 8683757) * force * force


def centered(physical, a):
    return subtract(physical, equilibrium(a))


def total_bond(previous, current, a):
    older = centered(previous, a)
    now = centered(current, a)
    return (F(square_norm(subtract(now, older)), 2)
            + stiffness_form(older, now) / 2)


def component_bonds(previous, current):
    h_old, c_old = previous[:5], previous[5]
    h_now, c_now = current[:5], current[5]
    field = F(square_norm(subtract(h_now, h_old)), 2) + edge_form(h_old, h_now) / 2
    source = F((c_now - c_old) ** 2, 2) + c_old * c_now / 2
    interaction = -G * (c_old * dot(ELL, h_now) + c_now * dot(ELL, h_old)) / 2
    return field, source, interaction


def vertex_energy_densities(previous_h, previous_c, current_h, current_c, a):
    diff_h = subtract(current_h, previous_h)
    b_prev = incidence_b5(previous_h)
    b_curr = incidence_b5(current_h)
    spatial_share = [F(0)] * 5
    for idx, (tail, head, _, w) in enumerate(ORIENTED_EDGES):
        term = (w / 4) * b_curr[idx] * b_prev[idx]
        spatial_share[tail] += term
        spatial_share[head] += term
    e_h = tuple(F(diff_h[r] * diff_h[r], 2) + spatial_share[r] for r in range(5))
    force = F(a, 4)
    c_bond = (F((current_c - previous_c) ** 2, 2)
              + F(previous_c * current_c, 2)
              - force * F(previous_c + current_c, 2))
    e_chi = tuple(SIGMA[r] * c_bond for r in range(5))
    e_int = tuple(-G * F(ELL[r], 2) * (previous_c * current_h[r] + current_c * previous_h[r])
                  for r in range(5))
    e_loc = tuple(e_h[r] + e_chi[r] + e_int[r] for r in range(5))
    shift = equilibrium_offset(a) / 5
    e_tot = tuple(e_loc[r] + shift for r in range(5))
    return e_loc, e_tot


def edge_currents(previous_h, previous_c, current_h, current_c, next_h, next_c,
                  with_interaction=True):
    q_h = subtract(next_h, previous_h)
    q_c = next_c - previous_c
    b_curr = incidence_b5(current_h)
    j_h = tuple((w / 4) * b_curr[idx] * (q_h[tail] + q_h[head])
                for idx, (tail, head, _, w) in enumerate(ORIENTED_EDGES))
    j_int_0 = -G * q_c * F(current_h[0] + current_h[1], 4) if with_interaction else F(0)
    j_int = (j_int_0,) + (F(0),) * 9
    return add(j_h, j_int), j_h, j_int


def transpose(matrix):
    return tuple(tuple(row[column] for row in matrix) for column in range(len(matrix[0])))


def multiply(left, right):
    columns = transpose(right)
    return tuple(tuple(dot(row, column) for column in columns) for row in left)


def matrix_vector(matrix, vector):
    return tuple(dot(row, vector) for row in matrix)


def identity(size):
    return tuple(unit(size, index) for index in range(size))


def determinant(matrix):
    rows = [list(map(F, row)) for row in matrix]
    answer = F(1)
    for column in range(len(rows)):
        pivot = next((r for r in range(column, len(rows)) if rows[r][column]), None)
        if pivot is None:
            return F(0)
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            answer = -answer
        value = rows[column][column]
        answer *= value
        for r in range(column + 1, len(rows)):
            factor = rows[r][column] / value
            for c in range(column, len(rows)):
                rows[r][c] -= factor * rows[column][c]
    return answer


def solve(matrix, rhs, key="EQUILIBRIUM"):
    rows = [list(map(F, row)) + [F(value)] for row, value in zip(matrix, rhs)]
    size = len(rows)
    for column in range(size):
        pivot = next((r for r in range(column, size) if rows[r][column]), None)
        require(pivot is not None, key)
        rows[column], rows[pivot] = rows[pivot], rows[column]
        value = rows[column][column]
        rows[column] = [entry / value for entry in rows[column]]
        for r in range(size):
            if r == column:
                continue
            factor = rows[r][column]
            rows[r] = [entry - factor * basis for entry, basis in zip(rows[r], rows[column])]
    return tuple(row[-1] for row in rows)


BASIS_EPERP = tuple(subtract(unit(5, site), unit(5, 4)) for site in range(4))
UMAT_EPERP = transpose(BASIS_EPERP)
L_MAT = transpose(tuple(laplacian(unit(5, site)) for site in range(5)))
GRAM_2L_EPERP = multiply(multiply(transpose(UMAT_EPERP),
                                  tuple(times(2, row) for row in L_MAT)),
                         UMAT_EPERP)


def solve_hamiltonian_constraint(e_density):
    """Solve 2 L tau = Pi_0 e_density on e^perp by 4x4 Gaussian elimination."""
    rhs_5 = project_mean_zero(e_density)
    rhs_4 = matrix_vector(transpose(UMAT_EPERP), rhs_5)
    coords = solve(GRAM_2L_EPERP, rhs_4, key="HAMILTONIAN_CONSTRAINT")
    tau = matrix_vector(UMAT_EPERP, coords)
    require(sum(tau) == 0 and times(2, laplacian(tau)) == rhs_5, "HAMILTONIAN_CONSTRAINT")
    require(tau == tuple(F(162, 53605) * val for val in adjoint_green_int(e_density)),
            "HAMILTONIAN_CONSTRAINT")
    return tau


def solve_momentum_constraint(tau_now, tau_next, j_total):
    return subtract(times(F(-1, 2), j_total),
                    weight_edges(incidence_b5(subtract(tau_next, tau_now))))


def three_slice_residuals(hp, cp, h, c, hn, cn, a):
    r_h = tuple(hn[r] - 2 * h[r] + hp[r] + lap - G * c * dip
                for r, (lap, dip) in enumerate(zip(laplacian(h), ELL)))
    r_c = cn - c + cp - F(a, 4) - G * dot(ELL, h)
    return r_h, r_c


def continuity_source_term(hp, cp, h, c, hn, cn, a):
    q_h = subtract(hn, hp)
    q_c = cn - cp
    r_h, r_c = three_slice_residuals(hp, cp, h, c, hn, cn, a)
    return tuple(F(1, 2) * q_h[r] * r_h[r] + F(1, 2) * SIGMA[r] * q_c * r_c
                 for r in range(5))


def bianchi_source_term(hp, cp, h, c, hn, cn, a):
    return times(F(-1, 2), project_mean_zero(continuity_source_term(hp, cp, h, c, hn, cn, a)))


def real_product(left, right):
    a, b = left
    c, d = right
    return a * c + b * d, a * d + b * c + b * d


def off_diagonal_norm(c):
    c0, c1, c2, c3 = c
    adjacent = c0 * c1 + c1 * c2 + c2 * c3
    other = c0 * c2 + c0 * c3 + c1 * c3
    return square_norm(c) - adjacent, adjacent - other


def times_j(c):
    c0, c1, c2, c3 = c
    return -c3, c0 - c3, c1 - c3, c2 - c3


def times_j_inverse(c):
    c0, c1, c2, c3 = c
    return c1 - c0, c2 - c0, c3 - c0, -c0


def hermitian_a(h):
    a0, a1, d0, d1 = h[:4]
    return (2 * a0 - a1, -a0 + a1, d0 + d1, d0 + 2 * d1,
            *times_j(h[4:]))


def hermitian_a_inverse(h):
    a0, a1, d0, d1 = h[:4]
    return (a0 + a1, a0 + 2 * a1, 2 * d0 - d1, -d0 + d1,
            *times_j_inverse(h[4:]))


def hermitian_b(h, t):
    a0, a1, d0, d1, c0, c1, c2, c3 = h
    return (a0 + t * (2 * c0 - c1) + t * t * d0,
            a1 + t * (c1 - c2 - c3) + t * t * d1,
            d0, d1, c0 + t * d0, c1, c2 - t * d1, c3 - t * d1)


def hermitian_loop(h, t):
    a0, a1, d0, d1, c0, c1, c2, c3 = h
    cross0 = -5 * c0 + 5 * c1 - 3 * c2 + c3
    cross1 = 2 * c0 - 3 * c1 + 3 * c2
    return (a0 + t * cross0 + t * t * (9 * d0 - 5 * d1),
            a1 + t * cross1 + t * t * (-5 * d0 + 4 * d1),
            d0, d1,
            c0 + t * (-2 * d0 + d1), c1 + t * d0,
            c2 + t * (-d0 + 2 * d1), c3 + t * d1)


def monitor(y):
    return 9 * y * y, -5 * y * y, 1, 0, -2 * y, y, -y, 0


def hermitian_cost(h):
    a0, a1, d0, d1 = h[:4]
    return (4 * a0 * a0 + 4 * a0 * a1 + 6 * a1 * a1
            + 4 * d0 * d0 + 4 * d0 * d1 + 6 * d1 * d1
            + 10 * square_norm(h[4:]) - 2 * sum(h[4:]) ** 2)


def trace_cost(h):
    aa = real_product(h[:2], h[:2])
    dd = real_product(h[2:4], h[2:4])
    cc = off_diagonal_norm(h[4:])
    return 4 * (aa[0] + dd[0] + 2 * cc[0]) + 2 * (aa[1] + dd[1] + 2 * cc[1])


def hermitian_determinant(h):
    ad = real_product(h[:2], h[2:4])
    cc = off_diagonal_norm(h[4:])
    return ad[0] - cc[0], ad[1] - cc[1]


def core_member(core):
    if not isinstance(core, tuple) or len(core) != 4:
        return False
    z, r, d, h = core
    return (integer_tuple(z, 6) and integer_tuple(r, 6)
            and type(d) is int and d >= 1 and integer_tuple(h, 8))


def state_member(state):
    return (isinstance(state, tuple) and len(state) == 3 and core_member(state[0])
            and type(state[1]) is int and state[1] >= 0
            and type(state[2]) is int and state[2] in (-1, 1))


def decode(core):
    z, r, d, _ = core
    return (tuple(F(value, d) for value in z),
            tuple(F(value, d) for value in r))


def encode(values, denominator):
    scaled = tuple(value * denominator for value in values)
    require(all(isinstance(value, F) and value.denominator == 1 for value in scaled), "INTEGER")
    return tuple(value.numerator for value in scaled)


def integer_bond_constraints(core, a):
    z, r, d, _ = core
    p, y = z[:5], z[5]
    q, v = r[:5], r[5]
    bp = incidence_b5(p)
    bq = incidence_b5(q)
    edge_share = [0] * 5
    for idx, (tail, head, mw, _) in enumerate(ORIENTED_EDGES):
        prod = mw * bp[idx] * bq[idx]
        edge_share[tail] += prod
        edge_share[head] += prod
    src_part = M * (y - v) ** 2 + M * y * v - 81 * a * d * (y + v)
    e_int = tuple(2 * M * (p[site] - q[site]) ** 2
                  + edge_share[site]
                  + TWO_SIGMA[site] * src_part
                  - 2 * ELL[site] * (v * p[site] + y * q[site])
                  for site in range(5))
    theta = adjoint_green_int(e_int)
    return e_int, theta


def integer_slice_constraints(core, next_core, a):
    z, r, _, _ = core
    z_next, _, _, _ = next_core
    p = z[:5]
    q_delta = tuple(z_next[i] - M * r[i] for i in range(6))
    q_dh, q_dc = q_delta[:5], q_delta[5]
    bp = incidence_b5(p)
    j_int = tuple(mw * bp[idx] * (q_dh[tail] + q_dh[head])
                  - (q_dc * (p[0] + p[1]) if idx == 0 else 0)
                  for idx, (tail, head, mw, _) in enumerate(ORIENTED_EDGES))
    e_now, th_now = integer_bond_constraints(core, a)
    e_nxt, th_nxt = integer_bond_constraints(next_core, a)
    diff_th = subtract(th_nxt, times(M * M, th_now))
    pi_int = subtract(times(-53605 * M, j_int), int_weight_edges(incidence_b5(diff_th)))
    require(integer_tuple(e_now, 5) and integer_tuple(th_now, 5)
            and integer_tuple(e_nxt, 5) and integer_tuple(th_nxt, 5)
            and integer_tuple(j_int, 10) and integer_tuple(pi_int, 10), "INTEGER_CONSTRAINT")
    require(sum(th_now) == 0 and sum(th_nxt) == 0, "HAMILTONIAN_CONSTRAINT")
    require(laplacian_int(th_now) == tuple(10721 * (5 * v - sum(e_now)) for v in e_now),
            "HAMILTONIAN_CONSTRAINT")
    require(laplacian_int(th_nxt) == tuple(10721 * (5 * v - sum(e_nxt)) for v in e_nxt),
            "HAMILTONIAN_CONSTRAINT")
    require(add(subtract(e_nxt, times(M * M, e_now)),
                times(M, divergence_b5t(j_int))) == (0,) * 5, "CONTINUITY")
    require(divergence_b5t(pi_int) == (0,) * 5, "BIANCHI")
    return e_now, th_now, j_int, pi_int


def forward(core, a, field_coupling=1, feedback=1, move_monitor=True):
    old_z, _, d, h = core
    current, previous = decode(core)
    spatial = laplacian(current[:5])
    field = tuple(2 * current[r] - previous[r] - spatial[r]
                  + field_coupling * G * current[5] * ELL[r] for r in range(5))
    source = current[5] - previous[5] + F(a, 4) + feedback * G * dot(ELL, current[:5])
    next_d = M * d
    next_z = encode(field + (source,), next_d)
    next_r = encode(current, next_d)
    next_h = hermitian_loop(h, next_z[5] - old_z[5]) if move_monitor else h
    return next_z, next_r, next_d, next_h


def backward(core, a):
    z, r, d, h = core
    if d % M or any(value % M for value in r):
        return None
    previous_d = d // M
    current, previous = decode(core)
    spatial = laplacian(previous[:5])
    older_field = tuple(2 * previous[site] - current[site] - spatial[site]
                        + G * previous[5] * ELL[site] for site in range(5))
    older_source = previous[5] - current[5] + F(a, 4) + G * dot(ELL, previous[:5])
    older_scaled = tuple(value * previous_d for value in older_field + (older_source,))
    if any(value.denominator != 1 for value in older_scaled):
        return None
    previous_z = tuple(value // M for value in r)
    previous_r = tuple(value.numerator for value in older_scaled)
    previous_h = hermitian_loop(h, previous_z[5] - z[5])
    return previous_z, previous_r, previous_d, previous_h


def account(core):
    z, r, d, h = core
    return 1 + d + square_norm(z) + square_norm(r) + hermitian_cost(h)


def core_bond(core, a):
    current, previous = decode(core)
    return total_bond(previous, current, a)


def reverse(state):
    return state[0], state[1], -state[2]


def funded(state, a):
    core, bank, direction = state
    if direction == 1:
        destination = forward(core, a)
    elif direction == -1:
        destination = backward(core, a)
    else:
        raise ValueError("direction outside carrier")
    ceiling = account(core) + bank
    if destination is None or account(destination) > ceiling:
        return reverse(state)
    return destination, ceiling - account(destination), direction


def inverse_funded(state, a):
    return reverse(funded(reverse(state), a))


def initial_row(word):
    for row in INITIAL:
        if row[0] == word:
            return row
    raise ValueError("word outside declared prepared family")


def prepared_core(word, a):
    _, first, second, _, _ = initial_row(word)
    z = tuple(6 + 5 * entry for entry in second) + (10 * a,)
    r = tuple(6 + 5 * entry for entry in first) + (0,)
    return z, r, 40, monitor(10 * a)


def check_authority():
    repository = Path(__file__).resolve().parents[2]
    for name, size, digest in AUTHORITY:
        data = (repository / "canon" / name).read_bytes()
        require(len(data) == size and sha256(data).hexdigest() == digest, "AUTHORITY")
    require(len(AUTHORITY) == 5, "CERTIFICATE")
    return len(AUTHORITY)


def check_initial_and_ring():
    labels = ("0010", "0011", "0100", "0101", "0110",
              "1001", "1010", "1011", "1100", "1101")
    require(tuple(row[0] for row in INITIAL) == labels, "INITIAL_DATA")
    for word, first, second, expected_energy, expected_dipole in INITIAL:
        bits = tuple(int(bit) for bit in word)
        for n, literal in enumerate((first, second)):
            site = bits[n + 2] - bits[n]
            expected = tuple(int((r - site) % 5 in (0, 1)) for r in range(5))
            require(literal == expected, "INITIAL_DATA")
        h0 = tuple(F(value, 2) for value in first)
        h1 = tuple(F(value, 2) for value in second)
        energy = F(square_norm(subtract(h1, h0)), 2) + edge_form(h0, h1) / 2
        require(energy == expected_energy and dot(ELL, h0) == expected_dipole, "INITIAL_DATA")
        for a in (-1, 0, 1):
            core = prepared_core(word, a)
            current, previous = decode(core)
            require(core_member(core) and sum(current[:5]) == sum(previous[:5]) == 1,
                    "INITIAL_DATA")
            require(current[:5] == tuple(F(1, 5) + (value - F(1, 5)) / 4 for value in h1)
                    and previous[:5] == tuple(F(1, 5) + (value - F(1, 5)) / 4 for value in h0)
                    and current[5] == F(a, 4) and previous[5] == 0, "INITIAL_DATA")
    require(real_product((0, 1), (0, 1)) == (1, 1), "RING")
    require(real_product((0, 1), (-1, 1)) == (1, 0), "RING")
    for index in range(4):
        basis = tuple(int(site == index) for site in range(4))
        image = basis
        orbit = []
        for _ in range(5):
            orbit.append(image)
            require(times_j_inverse(times_j(image)) == image, "RING")
            image = times_j(image)
        require(image == basis and tuple(sum(row[r] for row in orbit) for r in range(4))
                == (0, 0, 0, 0), "RING")


def hermitian_fixtures():
    fixtures = [H_ZERO]
    for index in range(8):
        basis = tuple(int(site == index) for site in range(8))
        fixtures.extend((basis, tuple(-value for value in basis)))
    fixtures.extend(((1, -1, 2, 0, -2, 1, 0, 1),
                     (0, 1, -1, 2, 1, 0, -1, 2)))
    require(len(fixtures) == 19, "CERTIFICATE")
    return tuple(fixtures)


def check_h_cost(h):
    require(integer_tuple(h, 8), "TRANSPORT")
    value = hermitian_cost(h)
    require(value == trace_cost(h) and value >= 2 * square_norm(h)
            and (value == 0) == (h == H_ZERO), "COST")


def check_transports(fixtures):
    transports = holonomies = 0
    for h in fixtures:
        check_h_cost(h)
        for image, inverse in ((hermitian_a(h), hermitian_a_inverse),
                               (hermitian_a_inverse(h), hermitian_a)):
            check_h_cost(image)
            require(inverse(image) == h and hermitian_determinant(image) == hermitian_determinant(h),
                    "TRANSPORT")
            transports += 1
        for t in (-2, -1, 0, 1, 2):
            image = hermitian_b(h, t)
            check_h_cost(image)
            require(hermitian_b(image, -t) == h
                    and hermitian_determinant(image) == hermitian_determinant(h), "TRANSPORT")
            transports += 1
            direct = hermitian_loop(h, t)
            factored = hermitian_a(hermitian_b(hermitian_a_inverse(hermitian_b(h, -t)), t))
            require(direct == factored and hermitian_loop(direct, -t) == h
                    and hermitian_determinant(direct) == hermitian_determinant(h), "HOLONOMY")
            check_h_cost(direct)
            holonomies += 1
    require((transports, holonomies) == (133, 95), "CERTIFICATE")
    return transports, holonomies


def check_funded_case(state, a, branches):
    require(state_member(state), "INTEGER")
    core, bank, direction = state
    out = funded(state, a)
    require(state_member(out), "INTEGER")
    require(inverse_funded(out, a) == state and funded(inverse_funded(state, a), a) == state,
            "FUNDED_INVERSE")
    require(account(out[0]) + out[1] == account(core) + bank, "CONSERVATION")
    require(core_bond(out[0], a) == core_bond(core, a), "ENERGY")
    if out[0] == core:
        require(integer_bond_constraints(out[0], a) == integer_bond_constraints(core, a),
                "HAMILTONIAN_CONSTRAINT")
    target = forward(core, a) if direction == 1 else backward(core, a)
    label = "forward" if direction == 1 else "backward"
    if target is None:
        branches.add(label + "_domain")
        expected = reverse(state)
    elif account(target) > account(core) + bank:
        branches.add(label + "_bank")
        expected = reverse(state)
    else:
        branches.add(label + "_move")
        expected = target, account(core) + bank - account(target), direction
    require(out == expected, "BRANCH")


def check_core_and_funding(fixtures):
    base = []
    for a in (-1, 0, 1):
        for i in range(19):
            for d in (1, 2, 40):
                z = (i - 9, 1, -2, 0, 3, i % 5 - 2)
                r = (2, -1, 0, 1, 9 - i, (i // 5) % 5 - 2)
                base.append((a, (z, r, d, fixtures[i])))
    require(len(base) == 171, "CERTIFICATE")
    decrease = ((0, 0, 0, 0, 0, 100), (0, 0, 0, 0, 0, 100), 1, monitor(100))
    require(account(forward(decrease, 0)) < account(decrease), "BRANCH")
    entries = base + [(0, decrease)]
    core_count = funded_count = 0
    branches = set()
    for a, core in entries:
        image = forward(core, a)
        require(core_member(core) and core_member(image), "INTEGER")
        require(image[2] == M * core[2] and backward(image, a) == core, "BARE_INVERSE")
        predecessor = backward(core, a)
        if predecessor is not None:
            require(forward(predecessor, a) == core, "BARE_INVERSE")
        require(core_bond(image, a) == core_bond(core, a), "ENERGY")
        integer_slice_constraints(core, image, a)
        core_count += 1
        for candidate in (core, image):
            increase = account(forward(candidate, a)) - account(candidate)
            banks = (0, 1, 772, max(0, increase - 1), max(0, increase), max(0, increase + 1))
            for bank in banks:
                for direction in (-1, 1):
                    check_funded_case((candidate, bank, direction), a, branches)
                    funded_count += 1
    require((core_count, funded_count) == (172, 4128), "CERTIFICATE")
    require(branches == {"forward_move", "backward_move", "forward_bank", "backward_bank",
                         "backward_domain"}, "BRANCH")
    image_defects = 0
    for a, core in base:
        require(backward(core, a) is None, "IMAGE_GUARD")
        require(funded((core, 1000000000, -1), a) == (core, 1000000000, 1), "IMAGE_GUARD")
        z, r, d, h = forward(core, a)
        for entry in range(13):
            corrupt_d = d + int(entry == 0)
            corrupt_r = tuple(value + int(entry == site + 1) for site, value in enumerate(r))
            corrupt_z = tuple(value + int(entry == site + 7) for site, value in enumerate(z))
            corrupt = corrupt_z, corrupt_r, corrupt_d, h
            require(core_member(corrupt) and backward(corrupt, a) is None, "IMAGE_GUARD")
            require(funded((corrupt, 1000000000, -1), a) == (corrupt, 1000000000, 1), "IMAGE_GUARD")
            image_defects += 1
    require(image_defects == 2223, "CERTIFICATE")
    return core_count, funded_count, image_defects


def matrices_green_and_equilibrium():
    for site in range(5):
        e_site = unit(5, site)
        require(divergence_b5t(weight_edges(incidence_b5(e_site))) == laplacian(e_site), "GREEN")
        expected_pi0 = tuple(10721 * (5 * int(r == site) - 1) for r in range(5))
        require(laplacian_int(adjoint_green_int(tuple(int(r == site) for r in range(5)))) == expected_pi0,
                "GREEN")
        require(adjoint_green_int(laplacian_int(tuple(int(r == site) for r in range(5)))) == expected_pi0,
                "GREEN")
    require(laplacian_int((1,) * 5) == (0,) * 5 and adjoint_green_int((1,) * 5) == (0,) * 5, "GREEN")
    require(adjoint_green_int(ELL) == (253, -253, 36, 0, -36), "GREEN")
    gram_l4 = multiply(multiply(transpose(UMAT_EPERP), L_MAT), UMAT_EPERP)
    require(gram_l4 == transpose(gram_l4), "GREEN")
    count = 0
    for size in range(1, 5):
        leading = tuple(row[:size] for row in gram_l4[:size])
        require(determinant(leading) > 0, "GREEN")
        count += 1
    b5_columns = tuple(incidence_b5(col) for col in BASIS_EPERP)
    gram_b5 = tuple(tuple(dot(u, v) for v in b5_columns) for u in b5_columns)
    require(determinant(gram_b5) > 0 and incidence_b5((1,) * 5) == (0,) * 10, "GREEN")
    kmat = transpose(tuple(stiffness(unit(6, site)) for site in range(6)))
    eye = identity(6)
    require(kmat == transpose(kmat), "GRAM")
    columns = tuple(subtract(unit(6, site), unit(6, 4)) for site in range(4)) + (unit(6, 5),)
    umat = transpose(columns)
    gram_k = multiply(multiply(transpose(umat), kmat), umat)
    inverse_dipole = times(F(324, 53605), (253, -253, 36, 0, -36))
    require(sum(inverse_dipole) == 0 and laplacian(inverse_dipole) == ELL, "EQUILIBRIUM")
    require(dot(ELL, inverse_dipole) == F(163944, 53605)
            and G * G * dot(ELL, inverse_dipole) == DELTA, "EQUILIBRIUM")
    for a in (-1, 0, 1):
        force = (F(0),) * 5 + (F(a, 4),)
        coordinates = solve(gram_k, matrix_vector(transpose(umat), force))
        derived = matrix_vector(umat, coordinates)
        expected = subtract(equilibrium(a), (F(1, 5),) * 5 + (F(0),))
        require(derived == expected and matrix_vector(kmat, derived) == force,
                "EQUILIBRIUM")
        eq = equilibrium(a)
        require(sum(eq[:5]) == 1 and laplacian(eq[:5]) == times(G * eq[5], ELL)
                and eq[5] == F(a, 4) + G * dot(ELL, eq[:5]), "EQUILIBRIUM")
    ksquare = multiply(kmat, kmat)
    forms = (
        tuple(tuple(kmat[i][j] - F(59, 100) * eye[i][j] for j in range(6)) for i in range(6)),
        tuple(tuple(F(201, 200) * eye[i][j] - kmat[i][j] for j in range(6)) for i in range(6)),
        tuple(tuple(kmat[i][j] - ksquare[i][j] / 4 - eye[i][j] / 2
                    for j in range(6)) for i in range(6)),
    )
    for form in forms:
        gram = multiply(multiply(transpose(umat), form), umat)
        require(gram == transpose(gram), "GRAM")
        for size in range(1, 6):
            leading = tuple(row[:size] for row in gram[:size])
            require(determinant(leading) > 0, "GRAM")
            count += 1
    require(count == 19, "CERTIFICATE")
    return kmat, count


def history(word, a, stop=12, field_coupling=1, feedback_mode="all"):
    core = prepared_core(word, a)
    current, previous = decode(core)
    cores = {1: core}
    values = [previous, current]
    rows = [(core[1][:5], 0, 40, H_REFERENCE),
            (core[0][:5], core[0][5], 40, core[3])]
    for n in range(1, stop):
        if feedback_mode == "all":
            feedback = 1
        elif feedback_mode == "none":
            feedback = 0
        elif feedback_mode == "first":
            feedback = int(n == 1)
        elif feedback_mode == "reversed":
            feedback = -1
        else:
            raise ValueError("unknown feedback comparison")
        core = forward(core, a, field_coupling=field_coupling, feedback=feedback)
        require(core_member(core), "INTEGER")
        cores[n + 1] = core
        current, _ = decode(core)
        values.append(current)
        rows.append((core[0][:5], core[0][5], core[2], core[3]))
    return rows, values, cores


def free_history(word, a, stop=12):
    current, previous = decode(prepared_core(word, a))
    values = [previous, current]
    for _ in range(1, stop):
        old, now = values[-2], values[-1]
        spatial = laplacian(now[:5])
        field = tuple(2 * now[site] - old[site] - spatial[site] for site in range(5))
        source = now[5] - old[5] + F(a, 4)
        values.append(field + (source,))
    return values


def local_action(v, xi, hp, hn, cp, cn, a):
    kinetic_h = F(square_norm(subtract(v, hp)) + square_norm(subtract(hn, v)), 2)
    kinetic_c = F((xi - cp) ** 2 + (cn - xi) ** 2, 2)
    return (kinetic_h - edge_form(v, v) / 2 + kinetic_c - xi * xi / 2
            + F(a, 4) * xi + G * xi * dot(ELL, v))


def exact_gradients(v, xi, hp, hn, cp, cn, a):
    spatial = laplacian(v)
    grad_h = tuple(2 * v[r] - hp[r] - hn[r] - spatial[r] + G * xi * ELL[r]
                   for r in range(5))
    grad_c = xi - cp - cn + F(a, 4) + G * dot(ELL, v)
    return grad_h + (grad_c,)


def cubic_action_48(point, hp, cp, hn, cn, a, e_hom):
    v = point[0:5]
    xi = point[5]
    tau_n = point[6:11]
    tau_n1 = point[11:16]
    p_n = point[16:26]
    lhom_n = point[26]
    lhom_n1 = point[27]
    llapse_n = point[28:33]
    llapse_n1 = point[33:38]
    nshift_n = point[38:48]
    eloc_n, etot_n = vertex_energy_densities(hp, cp, v, xi, a)
    eloc_n1, etot_n1 = vertex_energy_densities(v, xi, hn, cn, a)
    htot_n, htot_n1 = sum(etot_n), sum(etot_n1)
    jtot_n, _, _ = edge_currents(hp, cp, v, xi, hn, cn)
    pmom_n = add(weight_edges(incidence_b5(subtract(tau_n1, tau_n))), p_n)
    base = local_action(v, xi, hp, hn, cp, cn, a)
    hom = -lhom_n * (htot_n - e_hom) - lhom_n1 * (htot_n1 - e_hom)
    lapse_n = 2 * dot(llapse_n, laplacian(tau_n)) - dot(llapse_n, project_mean_zero(eloc_n))
    lapse_n1 = 2 * dot(llapse_n1, laplacian(tau_n1)) - dot(llapse_n1, project_mean_zero(eloc_n1))
    shift = 2 * dot(nshift_n, pmom_n) + dot(nshift_n, jtot_n)
    return base + hom + lapse_n + lapse_n1 + shift


def central_cubic_48(point, hp, cp, hn, cn, a, e_hom):
    coords = list(point)
    derivatives = []
    for i in range(48):
        saved = coords[i]
        coords[i] = saved + 1
        high = cubic_action_48(tuple(coords), hp, cp, hn, cn, a, e_hom)
        coords[i] = saved - 1
        low = cubic_action_48(tuple(coords), hp, cp, hn, cn, a, e_hom)
        coords[i] = saved
        derivatives.append((high - low) / 2)
    return tuple(derivatives)


def analytical_cubic_48(point, hp, cp, hn, cn, a, e_hom):
    v = point[0:5]
    xi = point[5]
    tau_n = point[6:11]
    tau_n1 = point[11:16]
    p_n = point[16:26]
    lhom_n = point[26]
    lhom_n1 = point[27]
    llapse_n = point[28:33]
    llapse_n1 = point[33:38]
    nshift_n = point[38:48]
    eloc_n, etot_n = vertex_energy_densities(hp, cp, v, xi, a)
    eloc_n1, etot_n1 = vertex_energy_densities(v, xi, hn, cn, a)
    htot_n, htot_n1 = sum(etot_n), sum(etot_n1)
    jtot_n, _, _ = edge_currents(hp, cp, v, xi, hn, cn)
    pmom_n = add(weight_edges(incidence_b5(subtract(tau_n1, tau_n))), p_n)
    base = exact_gradients(v, xi, hp, hn, cp, cn, a)
    grad_v = list(base[:5])
    grad_xi = base[5]
    mu_n = tuple(lhom_n + entry for entry in project_mean_zero(llapse_n))
    mu_n1 = tuple(lhom_n1 + entry for entry in project_mean_zero(llapse_n1))
    for mu_b, h_nb, c_nb in ((mu_n, hp, cp), (mu_n1, hn, cn)):
        b_nb = incidence_b5(h_nb)
        edge_vec = tuple((w / 4) * (mu_b[tail] + mu_b[head]) * b_nb[idx]
                         for idx, (tail, head, _, w) in enumerate(ORIENTED_EDGES))
        div_edge = divergence_b5t(edge_vec)
        for r in range(5):
            grad_v[r] -= (mu_b[r] * (v[r] - h_nb[r])
                          + div_edge[r]
                          - (G / 2) * mu_b[r] * ELL[r] * c_nb)
        mu_sigma = (mu_b[0] + mu_b[1]) / 2
        grad_xi -= (mu_sigma * (xi - F(c_nb, 2) - F(a, 8))
                    - (G / 2) * sum(mu_b[s] * ELL[s] * h_nb[s] for s in range(5)))
    q_h = subtract(hn, hp)
    q_c = cn - cp
    shift_edge = tuple((w / 4) * nshift_n[idx] * (q_h[tail] + q_h[head])
                       for idx, (tail, head, _, w) in enumerate(ORIENTED_EDGES))
    div_shift = divergence_b5t(shift_edge)
    for r in range(5):
        grad_v[r] += div_shift[r] - (G / 2) * q_c * nshift_n[0] * SIGMA[r]
    div_we_n = divergence_b5t(weight_edges(nshift_n))
    grad_tau_n = subtract(times(2, laplacian(llapse_n)), times(2, div_we_n))
    grad_tau_n1 = add(times(2, laplacian(llapse_n1)), times(2, div_we_n))
    grad_p_n = times(2, nshift_n)
    grad_lhom_n = -(htot_n - e_hom)
    grad_lhom_n1 = -(htot_n1 - e_hom)
    grad_llapse_n = subtract(times(2, laplacian(tau_n)), project_mean_zero(eloc_n))
    grad_llapse_n1 = subtract(times(2, laplacian(tau_n1)), project_mean_zero(eloc_n1))
    grad_nshift = add(times(2, pmom_n), jtot_n)
    return (tuple(grad_v) + (grad_xi,) + grad_tau_n + grad_tau_n1 + grad_p_n
            + (grad_lhom_n, grad_lhom_n1) + grad_llapse_n + grad_llapse_n1 + grad_nshift)


def three_adic_valuation(number):
    require(type(number) is int and number >= 1, "PRECISION")
    power = 0
    while number % 3 == 0:
        number //= 3
        power += 1
    return power


def check_histories():
    digest = sha256()
    cdigest = sha256()
    record_count = variation_count = bond_count = bianchi_count = precision_count = 0
    histories = {}
    constraint_data = {}
    for word, _, _, canonical_energy, dipole0 in INITIAL:
        for a in (-1, 0, 1):
            rows, values, cores = history(word, a)
            histories[word, a] = rows, values, cores
            force = F(a, 4)
            expected_energy = (canonical_energy / 16 - G * F(a, 32) * dipole0
                               + F(a * a, 32) / (1 - DELTA))
            require(F(0) < expected_energy < F(3, 50), "ENERGY")
            eloc_bonds = {0: None}
            etot_bonds = {0: None}
            tau_bonds = {0: None}
            eint_bonds = {0: None}
            theta_bonds = {0: None}
            for n in range(13):
                p, y, d, h = rows[n]
                current = values[n]
                require(integer_tuple(p, 5) and type(y) is int and type(d) is int
                        and integer_tuple(h, 8), "INTEGER")
                require(d == (40 if n == 0 else 40 * M ** (n - 1)), "INTEGER")
                require(current == tuple(F(value, d) for value in p + (y,)), "INTEGER")
                require(sum(p) == d and sum(current[:5]) == 1, "MEAN")
                require(h == monitor(y) and hermitian_determinant(h) == (0, 0)
                        and F(h[5], d) == current[5], "SOURCE_READER")
                require(hermitian_cost(h) == 294 * y ** 4 + 52 * y * y + 4, "COST")
                require(abs(current[5]) < F(3, 4), "SOURCE_BOUND")
                for value in current[:5]:
                    require(abs(value - F(1, 5)) < F(9, 20)
                            and F(-1, 4) < value < F(13, 20), "LORENTZ")
                    metric = (-1, 1 + value, 1 - value, 1)
                    det_g = metric[0] * metric[1] * metric[2] * metric[3]
                    require(metric[1] > 0 and metric[2] > 0 and det_g < F(-231, 400), "LORENTZ")
                if n >= 1:
                    core = cores[n]
                    older_from_core = decode(core)[1]
                    require(older_from_core == values[n - 1], "RECURRENCE")
                    require(5 * account(core) >= d * d, "COST")
                    bond = total_bond(values[n - 1], current, a)
                    require(bond == core_bond(core, a) == expected_energy, "ENERGY")
                    e_int, theta_int = integer_bond_constraints(core, a)
                    eloc, etot = vertex_energy_densities(values[n - 1][:5], values[n - 1][5],
                                                         current[:5], current[5], a)
                    tau = solve_hamiltonian_constraint(etot)
                    require(sum(etot) == expected_energy, "ENERGY")
                    require(tuple(F(v, 4 * M * d * d) for v in e_int) == eloc,
                            "INTEGER_CONSTRAINT")
                    require(tuple(F(v, 8 * 53605 * d * d) for v in theta_int) == tau,
                            "INTEGER_CONSTRAINT")
                    eloc_bonds[n] = eloc
                    etot_bonds[n] = etot
                    tau_bonds[n] = tau
                    eint_bonds[n] = e_int
                    theta_bonds[n] = theta_int
                    bond_count += 1
                    lcd = lcm(*(entry.denominator for entry in current))
                    require(three_adic_valuation(lcd) == 4 * (n - 1), "PRECISION")
                    numerators = tuple((entry * lcd).numerator for entry in current)
                    require(sum(numerators[:5]) == lcd
                            and 5 * (square_norm(numerators) + lcd * lcd) >= 6 * 3 ** (8 * (n - 1)),
                            "PRECISION")
                    precision_count += 1
                line = (f"{word}|{a}|{n}|{comma(p)}|{y}|{d}|{comma(h)}\n").encode("ascii")
                digest.update(line)
                record_count += 1
            p_slices = {}
            j_slices = {}
            for n in range(1, 12):
                old, now, nxt = values[n - 1], values[n], values[n + 1]
                r_h, r_c = three_slice_residuals(old[:5], old[5], now[:5], now[5],
                                                 nxt[:5], nxt[5], a)
                require(r_h == (0,) * 5 and r_c == 0, "RECURRENCE")
                e_now, th_now, j_int, pi_int = integer_slice_constraints(
                    cores[n], cores[n + 1], a)
                require(e_now == eint_bonds[n] and th_now == theta_bonds[n],
                        "INTEGER_CONSTRAINT")
                d = cores[n][2]
                j_tot, _, _ = edge_currents(old[:5], old[5], now[:5], now[5],
                                            nxt[:5], nxt[5])
                p_n = solve_momentum_constraint(tau_bonds[n], tau_bonds[n + 1], j_tot)
                require(tuple(F(v, 4 * M * M * d * d) for v in j_int) == j_tot,
                        "INTEGER_CONSTRAINT")
                require(tuple(F(v, 8 * 53605 * M * M * M * d * d) for v in pi_int) == p_n,
                        "INTEGER_CONSTRAINT")
                require(add(subtract(etot_bonds[n + 1], etot_bonds[n]),
                            divergence_b5t(j_tot)) == (0,) * 5, "CONTINUITY")
                pmom = add(weight_edges(incidence_b5(subtract(tau_bonds[n + 1], tau_bonds[n]))), p_n)
                require(add(times(2, pmom), j_tot) == (0,) * 10, "MOMENTUM_CONSTRAINT")
                require(divergence_b5t(p_n) == (0,) * 5, "BIANCHI")
                p_slices[n] = p_n
                j_slices[n] = j_tot
                cline = (f"{word}|{a}|{n}|{comma(e_now)}|{comma(th_now)}"
                         f"|{comma(j_int)}|{comma(pi_int)}\n").encode("ascii")
                cdigest.update(cline)
                bianchi_count += 1
            constraint_data[word, a] = (eloc_bonds, etot_bonds, tau_bonds,
                                        p_slices, j_slices, eint_bonds, theta_bonds)
            for n in (1, 2, 5, 11):
                old, now, nxt = values[n - 1], values[n], values[n + 1]
                pt = (now[:5] + (now[5],) + tau_bonds[n] + tau_bonds[n + 1] + p_slices[n]
                      + (F(0), F(0)) + (F(0),) * 5 + (F(0),) * 5 + (F(0),) * 10)
                num_g = central_cubic_48(pt, old[:5], old[5], nxt[:5], nxt[5], a, expected_energy)
                ana_g = analytical_cubic_48(pt, old[:5], old[5], nxt[:5], nxt[5], a, expected_energy)
                require(num_g == (0,) * 48 and ana_g == (0,) * 48, "ACTION")
                variation_count += 48
    require((record_count, bond_count, bianchi_count, variation_count, precision_count)
            == (390, 360, 330, 5760, 360), "CERTIFICATE")
    return (record_count, digest.hexdigest(), bond_count, bianchi_count,
            cdigest.hexdigest(), variation_count, precision_count,
            histories, constraint_data)


def check_offshell(histories, constraint_data):
    _, values, cores = histories["0011", 0]
    _, _, tau_bonds, p_slices, _, _, _ = constraint_data["0011", 0]
    e_hom0 = core_bond(cores[1], 0)
    h1, c1 = values[1][:5], values[1][5]
    h2, c2 = values[2][:5], values[2][5]
    h3, c3 = values[3][:5], values[3][5]
    base_pt = (h2 + (c2,) + tau_bonds[2] + tau_bonds[3] + p_slices[2]
               + (F(0), F(0)) + (F(0),) * 5 + (F(0),) * 5 + (F(0),) * 10)
    cases = []
    # Case 1
    p1 = list(base_pt)
    p1[0:5] = add(h2, (1, 0, 0, 0, 0))
    p1[28:33] = (F(1), F(-1), F(0), F(0), F(0))
    cases.append((tuple(p1), h1, c1, h3, c3, 0, e_hom0))
    # Case 2
    p2 = list(base_pt)
    p2[5] = c2 + 1
    p2[26] = F(1)
    cases.append((tuple(p2), h1, c1, h3, c3, 0, e_hom0))
    # Case 3
    p3 = list(base_pt)
    p3[38] = F(1)
    cases.append((tuple(p3), h1, c1, h3, c3 + 1, 0, e_hom0))
    # Case 4
    p4 = list(base_pt)
    p4[6:11] = add(tau_bonds[2], (1, -1, 0, 0, 0))
    p4[33:38] = (F(0), F(1), F(-1), F(0), F(0))
    cases.append((tuple(p4), h1, c1, add(h3, (0, 0, 1, 0, 0)), c3, 0, e_hom0))
    # Case 5
    p5 = list(base_pt)
    p5[16:26] = add(p_slices[2], (1, 1, 1, 1, 1, 0, 0, 0, 0, 0))
    p5[39] = F(1)
    cases.append((tuple(p5), h1, c1 - 1, h3, c3, 0, e_hom0))
    # Case 6
    p6 = (
        (F(1, 3), F(-2, 5), F(0), F(3, 7), F(-1))
        + (F(-2, 3),)
        + (F(1, 2), F(-1, 2), F(1, 3), F(-1, 3), F(0))
        + (F(0), F(1, 5), F(-1, 5), F(1, 4), F(-1, 4))
        + (F(1, 2), F(-1, 3), F(0), F(1, 5), F(-1, 2), F(1, 4), F(0), F(-1, 4), F(1, 6), F(-1, 6))
        + (F(1, 3), F(-1, 2))
        + (F(1), F(-1, 2), F(0), F(-1, 2), F(0))
        + (F(0), F(1), F(-1), F(1, 3), F(-1, 3))
        + (F(1), F(0), F(-1, 2), F(0), F(1, 3), F(-1, 4), F(1, 2), F(0), F(0), F(-1))
    )
    cases.append((p6, (F(0),) * 5, F(1, 2), (F(1),) * 5, F(-3, 4), 1, F(1, 7)))
    checked = 0
    for pt, hp, cp, hn, cn, a, e_hom in cases:
        ana = analytical_cubic_48(pt, hp, cp, hn, cn, a, e_hom)
        num = central_cubic_48(pt, hp, cp, hn, cn, a, e_hom)
        require(num == ana, "OFFSHELL_ACTION")
        require(any(x != 0 for x in ana[:6]) and any(x != 0 for x in ana[6:]), "OFFSHELL_ACTION")
        v, xi = pt[0:5], pt[5]
        eloc_n, etot_n = vertex_energy_densities(hp, cp, v, xi, a)
        eloc_n1, etot_n1 = vertex_energy_densities(v, xi, hn, cn, a)
        j_tot, _, _ = edge_currents(hp, cp, v, xi, hn, cn)
        require(add(subtract(etot_n1, etot_n), divergence_b5t(j_tot))
                == continuity_source_term(hp, cp, v, xi, hn, cn, a), "CONTINUITY")
        tau_ham_n = solve_hamiltonian_constraint(eloc_n)
        tau_ham_n1 = solve_hamiltonian_constraint(eloc_n1)
        p_mom = solve_momentum_constraint(tau_ham_n, tau_ham_n1, j_tot)
        require(divergence_b5t(p_mom)
                == bianchi_source_term(hp, cp, v, xi, hn, cn, a), "BIANCHI")
        checked += 48
    require(checked == 288, "CERTIFICATE")
    return checked


def wronskian(previous1, current1, previous2, current2):
    return dot(previous1, current2) - dot(current1, previous2)


def check_canonical_and_symplectic(histories, kmat):
    step_count = 0
    for (_, a), (_, values, _) in histories.items():
        for n in range(1, 12):
            z_old = centered(values[n - 1], a)
            z_now = centered(values[n], a)
            z_next = centered(values[n + 1], a)
            p_now = subtract(z_now, z_old)
            p_next = subtract(z_next, z_now)
            kz = matrix_vector(kmat, z_now)
            require(p_next == subtract(p_now, kz) and z_next == add(z_now, p_next), "CANONICAL")
            require(add(p_next, kz) == p_now and add(z_now, p_next) == z_next, "CANONICAL")
            step_count += 1
    require(step_count == 330, "CERTIFICATE")
    eye = identity(6)
    zero = tuple((F(0),) * 6 for _ in range(6))
    b_over_m = tuple(tuple(2 * eye[i][j] - kmat[i][j] for j in range(6)) for i in range(6))
    tmat = (tuple(b_over_m[i] + times(-1, eye[i]) for i in range(6))
            + tuple(eye[i] + zero[i] for i in range(6)))
    j12 = (tuple(zero[i] + times(-1, eye[i]) for i in range(6))
           + tuple(eye[i] + zero[i] for i in range(6)))
    require(multiply(multiply(transpose(tmat), j12), tmat) == j12, "SYMPLECTIC")
    symplectic_count = 0
    words = tuple(row[0] for row in INITIAL)
    for a in (-1, 0, 1):
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                first = histories[words[i], a][1]
                second = histories[words[j], a][1]
                omega1 = wronskian(centered(first[0], a), centered(first[1], a),
                                   centered(second[0], a), centered(second[1], a))
                for n in range(1, 13):
                    omega_n = wronskian(centered(first[n - 1], a), centered(first[n], a),
                                        centered(second[n - 1], a), centered(second[n], a))
                    require(omega_n == omega1, "SYMPLECTIC")
                    symplectic_count += 1
    require(symplectic_count == 1620, "CERTIFICATE")
    first = histories["0010", 1][1]
    second = histories["0011", 1][1]
    raw2 = wronskian(first[1], first[2], second[1], second[2])
    raw3 = wronskian(first[2], first[3], second[2], second[3])
    drift = raw3 - raw2
    require(drift == F(1, 4) * (first[2][5] - second[2][5]) == F(1, 10368), "CONTROL")
    return step_count, symplectic_count, drift


def check_witnesses_and_controls(histories, constraint_data):
    negative = histories["0010", -1]
    positive = histories["0010", 1]
    require(negative[0][2][:3] == ((4379, 2779, 794, 2594, 2414), -6480, 12960)
            and positive[0][2][:3] == ((4399, 2759, 794, 2594, 2414), 6480, 12960), "FIXED_COUNTER")
    direct = subtract(positive[1][2][:5], negative[1][2][:5])
    require(direct == times(F(1, 648), ELL), "FIXED_COUNTER")
    rows, values, cores = histories["0011", 0]
    eloc_bonds, etot_bonds, tau_bonds, p_slices, j_slices, eint_bonds, theta_bonds = constraint_data["0011", 0]
    require(rows[1][:3] == ((6, 11, 11, 6, 6), 0, 40), "FIXED_COUNTER")
    require(rows[2][:3] == ((2414, 2769, 2769, 2414, 2594), -5, 12960), "FIXED_COUNTER")
    require(rows[3][:3] == ((973001, 594836, 594831, 973006, 1063366), -1975, 4199040), "FIXED_COUNTER")
    expected_eint1 = (2350, 3975, 3975, 2350, 3250)
    expected_etot1 = (F(47, 41472), F(53, 27648), F(53, 27648), F(47, 41472), F(65, 41472))
    expected_theta1 = (-211250, 173775, 173775, -211250, 74950)
    expected_tau1 = (F(-845, 2744576), F(6951, 27445760), F(6951, 27445760),
                     F(-845, 2744576), F(1499, 13722880))
    require(eint_bonds[1] == expected_eint1 and etot_bonds[1] == expected_etot1
            and sum(etot_bonds[1]) == F(53, 6912), "FIXED_COUNTER")
    require(theta_bonds[1] == expected_theta1 and tau_bonds[1] == expected_tau1, "FIXED_COUNTER")
    j_tot1, j_h1, j_int1 = edge_currents(values[0][:5], values[0][5],
                                         values[1][:5], values[1][5],
                                         values[2][:5], values[2][5], with_interaction=True)
    require(j_tot1 == j_slices[1] and j_int1[0] == F(17, 134369280)
            and j_int1[1:] == (F(0),) * 9, "FIXED_COUNTER")
    _, _, j_int_vec1, _ = integer_slice_constraints(cores[1], cores[2], 0)
    require(j_int_vec1 == (-47040, 0, 47125, 0, 0, -105625, 105625, 47125, 0, -47125),
            "FIXED_COUNTER")
    controls = set()
    # Control 5: omit dipole interaction current from j_tot,1
    p1_no_int = solve_momentum_constraint(tau_bonds[1], tau_bonds[2], j_h1)
    defect_no_int = divergence_b5t(p1_no_int)
    expected_defect_no_int = (F(-17, 268738560), F(17, 268738560), F(0), F(0), F(0))
    require(defect_no_int == expected_defect_no_int, "CONTROL")
    controls.add("omitted_interaction_current")
    # Control 6: omit source and interaction energy densities from tau
    eloc2_free, _ = vertex_energy_densities(values[1][:5], F(0), values[2][:5], F(0), 0)
    tau2_free = solve_hamiltonian_constraint(eloc2_free)
    p1_no_src_tau = solve_momentum_constraint(tau_bonds[1], tau2_free, j_tot1)
    require(divergence_b5t(p1_no_src_tau) == times(-1, expected_defect_no_int), "CONTROL")
    controls.add("omitted_source_tau")
    # Control 7: off-gauge cubic shift-to-field backreaction at n=1
    pt_shift = (values[1][:5] + (values[1][5],) + tau_bonds[1] + tau_bonds[2] + p_slices[1]
                + (F(0), F(0)) + (F(0),) * 5 + (F(0),) * 5
                + (F(1),) + (F(0),) * 9)
    shift_grad = central_cubic_48(pt_shift, values[0][:5], values[0][5],
                                  values[2][:5], values[2][5], 0, F(53, 6912))[:5]
    expected_shift_grad = (F(943, 1679616), F(-157, 279936), F(0), F(0), F(0))
    require(shift_grad == expected_shift_grad
            and analytical_cubic_48(pt_shift, values[0][:5], values[0][5],
                                    values[2][:5], values[2][5], 0, F(53, 6912))[:5]
            == expected_shift_grad, "CONTROL")
    controls.add("offgauge_shift_backreaction")
    free = free_history("0011", 0)
    reciprocal = subtract(values[3][:5], free[3][:5])
    require(values[2][5] == F(-1, 2592) and values[2][:5] == free[2][:5]
            and reciprocal == times(F(-1, 839808), ELL), "FIXED_COUNTER")
    first_components = component_bonds(values[0], values[1])
    second_components = component_bonds(values[1], values[2])
    third_components = component_bonds(values[2], values[3])
    total = total_bond(values[0], values[1], 0)
    exchange = subtract(second_components, first_components)
    require(total == F(53, 6912) and sum(first_components) == sum(second_components)
            == sum(third_components) == total, "ENERGY")
    require(exchange == (0, F(1, 13436928), F(-1, 13436928)), "ENERGY")
    second_exchange = subtract(third_components, second_components)
    b0 = 839808
    require(second_exchange == (F(-180609, 2 * b0 * b0), F(28045, 2 * b0 * b0),
                                F(152564, 2 * b0 * b0)), "ENERGY")
    require(account(cores[1]) == 745 and account(cores[2]) == 70657990
            and hermitian_cost(cores[2][3]) == 185054
            and square_norm(cores[2][0][:5]) == 33718350
            and square_norm(cores[2][1]) == 36741600, "SHARP_BUDGET")
    bank = account(cores[2]) - account(cores[1])
    require(bank == 70657245 and funded((cores[1], bank, 1), 0) == (cores[2], 0, 1)
            and funded((cores[1], bank - 1, 1), 0) == (cores[1], bank - 1, -1), "SHARP_BUDGET")
    # Control 1: no feedback
    no_feedback = history("0011", 0, stop=3, feedback_mode="none")
    require(no_feedback[1] == free[:4] and all(value[5] == 0 for value in no_feedback[1]), "CONTROL")
    require(exact_gradients(no_feedback[1][1][:5], no_feedback[1][1][5],
                            no_feedback[1][0][:5], no_feedback[1][2][:5],
                            no_feedback[1][0][5], no_feedback[1][2][5], 0)[5]
            == F(-1, 2592), "CONTROL")
    controls.add("no_feedback")
    # Control 2: first feedback only
    first_only = history("0011", 0, stop=3, feedback_mode="first")
    continued = values[3][5] - first_only[1][3][5]
    require(first_only[1][3][5] == values[2][5] and continued == F(-71, 839808), "CONTROL")
    require(any(bianchi_source_term(first_only[1][1][:5], first_only[1][1][5],
                                    first_only[1][2][:5], first_only[1][2][5],
                                    first_only[1][3][:5], first_only[1][3][5], 0)), "CONTROL")
    controls.add("first_feedback_only")
    # Control 3: no field coupling
    no_field = history("0011", 0, stop=3, field_coupling=0)
    require([value[:5] for value in no_field[1]] == [value[:5] for value in free[:4]], "CONTROL")
    require(exact_gradients(no_field[1][2][:5], no_field[1][2][5],
                            no_field[1][1][:5], no_field[1][3][:5],
                            no_field[1][1][5], no_field[1][3][5], 0)[:5]
            == times(F(-1, 839808), ELL), "CONTROL")
    require(any(bianchi_source_term(no_field[1][1][:5], no_field[1][1][5],
                                    no_field[1][2][:5], no_field[1][2][5],
                                    no_field[1][3][:5], no_field[1][3][5], 0)), "CONTROL")
    controls.add("no_field_coupling")
    # Control 4: reversed feedback sign
    wrong_sign = history("0011", 0, stop=2, feedback_mode="reversed")
    require(exact_gradients(wrong_sign[1][1][:5], wrong_sign[1][1][5],
                            wrong_sign[1][0][:5], wrong_sign[1][2][:5],
                            wrong_sign[1][0][5], wrong_sign[1][2][5], 0)[5]
            == F(-1, 1296), "CONTROL")
    eloc_rev1, _ = vertex_energy_densities(wrong_sign[1][0][:5], wrong_sign[1][0][5],
                                           wrong_sign[1][1][:5], wrong_sign[1][1][5], 0)
    eloc_rev2, _ = vertex_energy_densities(wrong_sign[1][1][:5], wrong_sign[1][1][5],
                                           wrong_sign[1][2][:5], wrong_sign[1][2][5], 0)
    jtot_rev1, _, _ = edge_currents(wrong_sign[1][0][:5], wrong_sign[1][0][5],
                                    wrong_sign[1][1][:5], wrong_sign[1][1][5],
                                    wrong_sign[1][2][:5], wrong_sign[1][2][5])
    p_rev1 = solve_momentum_constraint(solve_hamiltonian_constraint(eloc_rev1),
                                       solve_hamiltonian_constraint(eloc_rev2),
                                       jtot_rev1)
    defect_rev = divergence_b5t(p_rev1)
    expected_defect_rev = (F(-1, 44789760), F(-1, 44789760), F(1, 67184640),
                           F(1, 67184640), F(1, 67184640))
    require(defect_rev == expected_defect_rev
            and defect_rev == bianchi_source_term(
                wrong_sign[1][0][:5], wrong_sign[1][0][5],
                wrong_sign[1][1][:5], wrong_sign[1][1][5],
                wrong_sign[1][2][:5], wrong_sign[1][2][5], 0), "CONTROL")
    controls.add("wrong_feedback_sign")
    # Control 8: no monitor transport
    no_monitor = forward(cores[1], 0, move_monitor=False)
    require(no_monitor[3][5] == 0 and no_monitor[0][5] == -5, "CONTROL")
    controls.add("no_monitor_transport")
    # Control 9: omitted interaction energy
    uncoupled_account_increase = sum(second_components[:2]) - sum(first_components[:2])
    require(uncoupled_account_increase == F(1, 13436928) != 0
            and uncoupled_account_increase + exchange[2] == 0, "CONTROL")
    controls.add("omitted_interaction_energy")
    # Control 10: unrestricted metric degeneracy
    degenerate = ((1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0), 1, H_REFERENCE)
    require(core_member(degenerate), "CONTROL")
    bad = decode(degenerate)[0][0]
    require((-1, 1 + bad, 1 - bad, 1) == (-1, 2, 0, 1) and bad * bad - 1 == 0, "CONTROL")
    controls.add("unrestricted_metric_degeneracy")
    require(len(controls) == 10, "CERTIFICATE")
    return (direct, expected_etot1, expected_tau1, j_int1[0],
            expected_defect_no_int, expected_defect_rev, expected_shift_grad, bank)


def check_cycles(histories):
    periods = []
    for a in (-1, 0, 1):
        cores = histories["0011", a][2]
        require(account(cores[1]) < account(cores[2]) < account(cores[3]), "SHARP_BUDGET")
        for target in (1, 2):
            ceiling = max(account(cores[n]) for n in range(1, target + 1))
            start = cores[1], ceiling - account(cores[1]), 1
            state = start
            seen = {state}
            first_return = None
            reached = 1
            for tick in range(1, 2 * target + 1):
                state = funded(state, a)
                require(state_member(state), "PERIOD")
                require(account(state[0]) + state[1] == ceiling
                        and core_bond(state[0], a) == core_bond(start[0], a), "CONSERVATION")
                if state[0] == cores[target]:
                    reached = target
                if state == start:
                    first_return = tick
                    break
                require(state not in seen, "PERIOD")
                seen.add(state)
            require(first_return == 2 * target and len(seen) == first_return and reached == target, "PERIOD")
            periods.append(first_return)
    require(tuple(periods) == (2, 4, 2, 4, 2, 4), "CERTIFICATE")
    return tuple(periods)


def certificate():
    authority = check_authority()
    check_initial_and_ring()
    fixtures = hermitian_fixtures()
    transports, holonomies = check_transports(fixtures)
    cores, funded_cases, defects = check_core_and_funding(fixtures)
    kmat, minors = matrices_green_and_equilibrium()
    (records, digest, cbonds, bslices, cdigest,
     variations, precision, histories, constraint_data) = check_histories()
    offshell = check_offshell(histories, constraint_data)
    canonical, symplectic, drift = check_canonical_and_symplectic(histories, kmat)
    (direct, etot1, tau1, jint1_0, defect_no_int,
     defect_rev, shift_grad, bank) = check_witnesses_and_controls(histories, constraint_data)
    periods = check_cycles(histories)
    lines = (
        "CERTIFICATE=" + PROBE,
        "AUTHORITY_FILES=" + str(authority),
        "TRANSPORT_CHECKS=" + str(transports),
        "HOLONOMY_CHECKS=" + str(holonomies),
        "CORE_FIXTURES=" + str(cores),
        "FUNDED_CASES=" + str(funded_cases),
        "IMAGE_DEFECTS=" + str(defects),
        "HISTORY_RECORDS=" + str(records),
        "HISTORY_SHA256=" + digest,
        "CONSTRAINT_BONDS=" + str(cbonds),
        "BIANCHI_SLICES=" + str(bslices),
        "CONSTRAINT_SHA256=" + cdigest,
        "CUBIC_VARIATIONS=" + str(variations),
        "OFFSHELL_CUBIC_VARIATIONS=" + str(offshell),
        "GREEN_MINOR_CHECKS=" + str(minors),
        "PRECISION_CHECKS=" + str(precision),
        "CANONICAL_STEPS=" + str(canonical),
        "SYMPLECTIC_CHECKS=" + str(symplectic),
        "DIRECT_CONTRAST=" + comma(direct),
        "ZERO_SOURCE_ENERGY_DENSITY=" + comma(etot1),
        "ZERO_SOURCE_TAU1=" + comma(tau1),
        "ZERO_SOURCE_INTERACTION_CURRENT=" + str(jint1_0),
        "NO_INTERACTION_CURRENT_BIANCHI_DEFECT=" + comma(defect_no_int),
        "REVERSED_FEEDBACK_BIANCHI_DEFECT=" + comma(defect_rev),
        "SHIFT_CUBIC_BACKREACTION=" + comma(shift_grad),
        "AFFINE_WRONSKIAN_DRIFT=" + str(drift),
        "ZERO_SOURCE_FIRST_BANK=" + str(bank),
        "CYCLE_PERIODS=" + comma(periods),
        "NEGATIVE_CONTROLS=PASS",
        "CERTIFICATE_RESULT=PASS",
    )
    require(len(lines) == 30, "CERTIFICATE")
    return ("\n".join(lines) + "\n").encode("ascii")


def main():
    try:
        output = certificate()
    except ScientificFailure as failure:
        output = ("FALSIFIER=" + failure.key + "\nRESULT=FAIL\n").encode("ascii")
    sys.stdout.buffer.write(output)


if __name__ == "__main__":
    main()
