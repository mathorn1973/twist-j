#!/usr/bin/env python3
"""Independent exact recurrence/dual-number audit of the frozen contract.

This program reads only the five declared authority files.  It neither imports
nor reads any other scientific implementation, and makes no file writes.
"""

from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path
import sys


ORDER = 4
F = Fraction
ZERO = F(0)
ONE = F(1)
DIRECTIONS = ((1, -1, 0), (0, 1, -1), (1, -2, 1))
AUTHORITY = (
    ("CANON.md", 1052518, "d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b"),
    ("CORE.md", 30714, "9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728"),
    ("FRONTIER.md", 27382, "8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0"),
    ("REGISTRY.tsv", 532811, "5cd008147435bf1facfe93b2e05d9d7e41554d73f647ad09659aac002195890d"),
    ("CHANGELOG.md", 207770, "79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078"),
)


class ScientificFailure(Exception):
    pass


def need(condition, category):
    if not condition:
        raise ScientificFailure(category)


class Dual:
    """Exact first derivative, propagated through the whole scalar action."""

    __slots__ = ("value", "tangent")

    def __init__(self, value, tangent=ZERO):
        self.value = F(value)
        self.tangent = F(tangent)

    @staticmethod
    def lift(value):
        return value if isinstance(value, Dual) else Dual(value)

    def __add__(self, other):
        other = self.lift(other)
        return Dual(self.value + other.value, self.tangent + other.tangent)

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, -self.tangent)

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __rsub__(self, other):
        return self.lift(other) + (-self)

    def __mul__(self, other):
        other = self.lift(other)
        return Dual(self.value * other.value,
                    self.tangent * other.value + self.value * other.tangent)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.lift(other)
        return Dual(self.value / other.value,
                    (self.tangent * other.value - self.value * other.tangent)
                    / (other.value * other.value))

    def __rtruediv__(self, other):
        return self.lift(other) / self

    def __eq__(self, other):
        other = self.lift(other)
        return self.value == other.value and self.tangent == other.tangent


def primal(value):
    return value.value if isinstance(value, Dual) else value


def zero(rows, cols):
    return [[ZERO for _ in range(cols)] for _ in range(rows)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def add(left, right):
    return [[x + y for x, y in zip(a, b)] for a, b in zip(left, right)]


def scale(scalar, matrix):
    return [[scalar * entry for entry in row] for row in matrix]


def subtract(left, right):
    return add(left, scale(-1, right))


def multiply(left, right):
    out = zero(len(left), len(right[0]))
    for i, row in enumerate(left):
        for k, coefficient in enumerate(row):
            if coefficient != 0:
                for j, entry in enumerate(right[k]):
                    if entry != 0:
                        out[i][j] += coefficient * entry
    return out


def matvec(matrix, vector):
    return [sum((a * b for a, b in zip(row, vector)), ZERO) for row in matrix]


def dot(left, right):
    return sum((a * b for a, b in zip(left, right)), ZERO)


def vadd(left, right):
    return [a + b for a, b in zip(left, right)]


def vsub(left, right):
    return [a - b for a, b in zip(left, right)]


def vscale(scalar, vector):
    return [scalar * entry for entry in vector]


def block(a, b, c, d):
    return [x + y for x, y in zip(a, b)] + [x + y for x, y in zip(c, d)]


def window(matrix, row, col, size=6):
    return [line[col:col + size] for line in matrix[row:row + size]]


def inverse(matrix, category):
    """Gauss-Jordan works over both Q and the exact dual-number extension."""
    n = len(matrix)
    augmented = [list(row) + unit for row, unit in zip(matrix, eye(n))]
    for column in range(n):
        candidates = [r for r in range(column, n)
                      if primal(augmented[r][column]) != 0]
        need(bool(candidates), category)
        pivot_row = candidates[0]
        augmented[column], augmented[pivot_row] = augmented[pivot_row], augmented[column]
        divisor = augmented[column][column]
        augmented[column] = [entry / divisor for entry in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor != 0:
                augmented[row] = [a - factor * b
                                  for a, b in zip(augmented[row], augmented[column])]
    need([row[:n] for row in augmented] == eye(n), category)
    return [row[n:] for row in augmented]


def ldl_pivots(matrix):
    n = len(matrix)
    lower = eye(n)
    diagonal = []
    for j in range(n):
        pivot = matrix[j][j] - sum(
            (lower[j][k] * lower[j][k] * diagonal[k] for k in range(j)), ZERO)
        need(pivot > 0, "F_GEOMETRY")
        diagonal.append(pivot)
        for i in range(j + 1, n):
            numerator = matrix[i][j] - sum(
                (lower[i][k] * lower[j][k] * diagonal[k] for k in range(j)), ZERO)
            lower[i][j] = numerator / pivot
    diagonal_matrix = [[diagonal[i] if i == j else ZERO for j in range(n)]
                       for i in range(n)]
    need(multiply(multiply(lower, diagonal_matrix), transpose(lower)) == matrix,
         "F_GEOMETRY")
    return diagonal


def paired(matrix, tangent):
    return [[Dual(a, b) for a, b in zip(row, drow)]
            for row, drow in zip(matrix, tangent)]


def tangents(matrix):
    return [[entry.tangent if isinstance(entry, Dual) else ZERO for entry in row]
            for row in matrix]


def energy(phase, dmatrix):
    q, p = phase[:6], phase[6:]
    return (dot(p, p) + dot(q, matvec(dmatrix, q))) / 2


def action(q, endq, amatrix, ematrix):
    # Evaluate the quadratic itself; derivatives follow through scalar arithmetic.
    return (dot(q, matvec(amatrix, q)) + dot(endq, matvec(amatrix, endq))) / 2 \
        - dot(q, matvec(ematrix, endq))


def incoming(q, endq, amatrix, ematrix):
    return vsub(matvec(ematrix, endq), matvec(amatrix, q))


def outgoing(q, endq, amatrix, ematrix):
    return vsub(matvec(amatrix, endq), matvec(ematrix, q))


def matrix_convolution(left, right):
    out = []
    for degree in range(ORDER + 1):
        coefficient = zero(len(left[0]), len(right[0][0]))
        for i in range(degree + 1):
            coefficient = add(coefficient, multiply(left[i], right[degree - i]))
        out.append(coefficient)
    return out


def matrix_vector_convolution(matrices, vectors):
    out = []
    for degree in range(ORDER + 1):
        coefficient = [ZERO] * len(matrices[0])
        for i in range(degree + 1):
            coefficient = vadd(coefficient, matvec(matrices[i], vectors[degree - i]))
        out.append(coefficient)
    return out


def vector_dot_convolution(left, right):
    return [sum((dot(left[i], right[degree - i]) for i in range(degree + 1)), ZERO)
            for degree in range(ORDER + 1)]


def scaled_argument(series, scalar):
    return [scale(scalar ** degree, coefficient)
            for degree, coefficient in enumerate(series)]


def constant_vector_series(vector):
    return [list(vector)] + [[ZERO] * len(vector) for _ in range(ORDER)]


def vector_series_add(left, right):
    return [vadd(a, b) for a, b in zip(left, right)]


def vector_series_subtract(left, right):
    return [vsub(a, b) for a, b in zip(left, right)]


def polynomial_action(q, endq, amatrices, ematrices):
    aq = matrix_vector_convolution(amatrices, q)
    aqend = matrix_vector_convolution(amatrices, endq)
    eqend = matrix_vector_convolution(ematrices, endq)
    first = vector_dot_convolution(q, aq)
    second = vector_dot_convolution(endq, aqend)
    mixed = vector_dot_convolution(q, eqend)
    return [(a + b) / 2 - c for a, b, c in zip(first, second, mixed)]


def csv(values):
    return ",".join(str(value) for value in values)


def flat(matrix):
    return [entry for row in matrix for entry in row]


def audit():
    repo = Path(__file__).resolve().parents[2]
    counts = {
        "AUTHORITY_FILES": 0, "COMPOSITION_PAIRS": 0,
        "REGULAR_BOUNDARY_CASES": 0, "CONSTRAINED_VARIATIONS": 0,
        "FREE_LAPSE_WITNESSES": 0, "GAUGE_PHASE_SERIES": 0,
        "GAUGE_BOND_SERIES": 0, "GAUGE_ACTION_SERIES": 0,
        "CAUSTIC_HISTORIES": 0,
    }
    for name, size, digest in AUTHORITY:
        try:
            data = (repo / "canon" / name).read_bytes()
        except OSError as error:
            raise ScientificFailure("F_AUTHORITY") from error
        need(len(data) == size and sha256(data).hexdigest() == digest, "F_AUTHORITY")
        counts["AUTHORITY_FILES"] += 1

    records = []
    identity = eye(6)
    spatial = zero(5, 5)
    for tail in range(5):
        for step, weight in ((1, F(29, 324)), (2, F(65, 324))):
            incidence = [ZERO] * 5
            incidence[tail] = -ONE
            incidence[(tail + step) % 5] = ONE
            for i in range(5):
                for j in range(5):
                    spatial[i][j] += weight * incidence[i] * incidence[j]
    expected_spatial = [[F(188 if i == j else (-29 if (i - j) % 5 in (1, 4)
                                              else -65), 324)
                         for j in range(5)] for i in range(5)]
    need(spatial == expected_spatial, "F_GEOMETRY")
    ell = [ONE, -ONE, ZERO, ZERO, ZERO]
    coupling = F(1, 324)
    potential = zero(6, 6)
    for i in range(5):
        for j in range(5):
            potential[i][j] = spatial[i][j]
        potential[i][5] = potential[5][i] = -coupling * ell[i]
    potential[5][5] = ONE
    cmat = subtract(identity, scale(F(1, 2), potential))
    csquared = multiply(cmat, cmat)
    dmat = subtract(identity, csquared)
    uniform = [ONE] * 5 + [ZERO]
    need(matvec(dmat, uniform) == [ZERO] * 6, "F_GEOMETRY")
    need(add(csquared, dmat) == identity, "F_GEOMETRY")
    need(all(matrix == transpose(matrix) for matrix in (spatial, potential, cmat, dmat)),
         "F_GEOMETRY")
    need(multiply(cmat, dmat) == multiply(dmat, cmat), "F_GEOMETRY")
    nil = zero(6, 6)
    generator = block(nil, identity, scale(-1, dmat), nil)
    transfer = block(cmat, identity, scale(-1, dmat), cmat)
    metric = block(dmat, nil, nil, identity)
    need(multiply(multiply(transpose(transfer), metric), transfer) == metric,
         "F_GEOMETRY")
    need(multiply(transfer, generator) == multiply(generator, transfer), "F_GEOMETRY")

    positive_spatial = subtract(eye(5), spatial)
    positive_full = subtract(scale(3, identity), potential)
    pivots_spatial = ldl_pivots(positive_spatial)
    pivots_full = ldl_pivots(positive_full)
    schur = -coupling * coupling * dot(
        ell, matvec(inverse(positive_spatial, "F_GEOMETRY"), ell))
    need(schur < 0, "F_GEOMETRY")
    records.append("P|" + csv(pivots_spatial) + "|" + csv(pivots_full) + "|" + str(schur))

    transfer3 = multiply(multiply(transfer, transfer), transfer)
    u3 = window(transfer3, 0, 0)
    b3 = window(transfer3, 0, 6)
    need(u3 == subtract(multiply(csquared, cmat), scale(3, multiply(cmat, dmat))),
         "F_GEOMETRY")
    need(b3 == subtract(scale(4, csquared), identity), "F_GEOMETRY")
    need(b3 == multiply(subtract(identity, potential), positive_full), "F_GEOMETRY")
    need(window(transfer3, 6, 0) == scale(-1, multiply(dmat, b3))
         and window(transfer3, 6, 6) == u3, "F_GEOMETRY")
    e3 = inverse(b3, "F_GEOMETRY")
    need(multiply(b3, e3) == identity and multiply(e3, b3) == identity, "F_GEOMETRY")
    a3 = multiply(e3, u3)
    records.append("B|" + csv(flat(u3)) + "|" + csv(flat(b3)) + "|" + csv(flat(e3)))

    # Solve R' = K R coefficient by coefficient, without matrix powers.
    exponential = [eye(12)]
    for degree in range(1, ORDER + 1):
        exponential.append(scale(F(1, degree), multiply(generator, exponential[-1])))
    for degree in range(ORDER):
        need(scale(degree + 1, exponential[degree + 1])
             == multiply(generator, exponential[degree]), "F_SERIES")
    for left_degree in range(ORDER + 1):
        for right_degree in range(ORDER + 1 - left_degree):
            total_degree = left_degree + right_degree
            need(multiply(exponential[left_degree], exponential[right_degree])
                 == scale(comb(total_degree, left_degree), exponential[total_degree]),
                 "F_SERIES")
            counts["COMPOSITION_PAIRS"] += 1
    for degree, coefficient in enumerate(exponential):
        records.append("R|" + str(degree) + "|" + csv(flat(coefficient)))

    transfers = [multiply(transfer, coefficient) for coefficient in exponential]
    useries = [window(coefficient, 0, 0) for coefficient in transfers]
    bseries = [window(coefficient, 0, 6) for coefficient in transfers]
    eseries = [inverse(bseries[0], "F_SERIES")]
    for degree in range(1, ORDER + 1):
        convolution = zero(6, 6)
        for i in range(1, degree + 1):
            convolution = add(convolution, multiply(bseries[i], eseries[degree - i]))
        eseries.append(scale(-1, multiply(eseries[0], convolution)))
    aseries = matrix_convolution(eseries, useries)
    constant_identity = [identity] + [zero(6, 6) for _ in range(ORDER)]
    need(matrix_convolution(bseries, eseries) == constant_identity
         and matrix_convolution(eseries, bseries) == constant_identity, "F_SERIES")
    need(eseries[0] == identity and aseries[0] == cmat, "F_SERIES")
    need(eseries[1] == scale(-1, cmat) and aseries[1] == scale(-1, identity), "F_SERIES")
    need(all(a == transpose(a) for a in eseries + aseries), "F_SERIES")

    # Differentiate B(L)^{-1} and the quadratic expression by exact dual arithmetic.
    dual_b3 = paired(b3, u3)
    dual_u3 = paired(u3, scale(-1, multiply(dmat, b3)))
    dual_e3 = inverse(dual_b3, "F_BOUNDARY")
    dual_a3 = multiply(dual_e3, dual_u3)
    expected_e3_prime = scale(-1, multiply(multiply(e3, u3), e3))
    expected_a3_prime = add(multiply(expected_e3_prime, u3),
                            multiply(e3, scale(-1, multiply(dmat, b3))))
    need(tangents(dual_e3) == expected_e3_prime
         and tangents(dual_a3) == expected_a3_prime, "F_BOUNDARY")
    dual_a0 = paired(aseries[0], aseries[1])
    dual_e0 = paired(eseries[0], eseries[1])

    control_evidence = {name: [] for name in ("NC01", "NC02", "NC06", "NC08")}
    bad_unchanged_phase = False
    bad_positive_dressing = False

    for seed in range(1, 7):
        initial = [F(((seed + 1) * (j + 2) + j * j) % 19 - 9, seed + 2)
                   for j in range(12)]
        phases = [initial]
        for _ in range(3):
            phases.append(matvec(transfer, phases[-1]))
        for n, phase in enumerate(phases):
            records.append("Z|" + str(seed) + "|" + str(n) + "|" + csv(phase))
        hamiltonian = energy(initial, dmat)
        need(hamiltonian > 0, "F_VARIATION")
        need(all(energy(phase, dmat) == hamiltonian for phase in phases), "F_VARIATION")
        records.append("H|" + str(seed) + "|" + str(hamiltonian))

        bond_actions = []
        parameter_derivatives = []
        left_momenta = []
        right_momenta = []
        for bond in range(3):
            q, endq = phases[bond][:6], phases[bond + 1][:6]
            bond_actions.append(action(q, endq, aseries[0], eseries[0]))
            differentiated = action(q, endq, dual_a0, dual_e0)
            need(differentiated.value == bond_actions[-1], "F_VARIATION")
            parameter_derivatives.append(differentiated.tangent)
            right_momenta.append(incoming(q, endq, aseries[0], eseries[0]))
            left_momenta.append(outgoing(q, endq, aseries[0], eseries[0]))
            need(right_momenta[-1] == phases[bond][6:]
                 and left_momenta[-1] == phases[bond + 1][6:], "F_VARIATION")
        need(all(left_momenta[n - 1] == right_momenta[n] for n in (1, 2)),
             "F_VARIATION")
        need(parameter_derivatives == [-hamiltonian] * 3, "F_VARIATION")
        constrained = [dot(direction, parameter_derivatives) for direction in DIRECTIONS]
        for value in constrained:
            need(value == 0, "F_VARIATION")
            counts["CONSTRAINED_VARIATIONS"] += 1
        free_work = dot((1, 0, 0), parameter_derivatives)
        need(free_work == -hamiltonian and free_work != 0, "F_VARIATION")
        counts["FREE_LAPSE_WITNESSES"] += 1
        fixed_energy = hamiltonian + 1
        shifted_derivatives = [value + fixed_energy for value in parameter_derivatives]
        added_works = [dot(direction, shifted_derivatives) for direction in DIRECTIONS]
        need(added_works == [ZERO] * 3 and hamiltonian - fixed_energy == -1, "F_VARIATION")
        records.append("W|" + str(seed) + "|" + csv(constrained) + "|" + str(free_work)
                       + "|" + csv(added_works))
        control_evidence["NC01"].append(hamiltonian > 0 and constrained == [ZERO] * 3)
        control_evidence["NC02"].append(added_works == [ZERO] * 3
                                        and hamiltonian - fixed_energy == -1)

        q, endq = phases[0][:6], phases[3][:6]
        recovered = matvec(e3, vsub(endq, matvec(u3, q)))
        need(recovered == initial[6:], "F_BOUNDARY")
        actual_sum = sum(bond_actions, ZERO)
        reduced_action = action(q, endq, a3, e3)
        reduced_dual = action(q, endq, dual_a3, dual_e3)
        boundary_derivative = reduced_dual.tangent
        need(actual_sum == reduced_action == reduced_dual.value, "F_BOUNDARY")
        need(boundary_derivative == -hamiltonian, "F_BOUNDARY")
        need(incoming(q, endq, a3, e3) == phases[0][6:]
             and outgoing(q, endq, a3, e3) == phases[3][6:], "F_BOUNDARY")
        recovered_energy = energy(q + recovered, dmat)
        need(recovered_energy - fixed_energy == -1, "F_BOUNDARY")
        counts["REGULAR_BOUNDARY_CASES"] += 1
        control_evidence["NC06"].append(recovered_energy - fixed_energy == -1)
        control_evidence["NC08"].append(boundary_derivative != hamiltonian)
        records.append("A|" + str(seed) + "|" + str(actual_sum) + "|" + str(reduced_action)
                       + "|" + str(boundary_derivative))

        theta = [ZERO, F(seed - 3, seed + 1), F(2 * seed - 5, seed + 2), ZERO]
        eta = [ZERO, F(seed + 2, seed + 3), -F(seed + 1, seed + 4), ZERO]
        alpha = [theta[n + 1] - theta[n] for n in range(3)]
        need(sum(alpha, ZERO) == 0, "F_GAUGE")
        transformed = []
        for n in range(4):
            constant_phase = constant_vector_series(phases[n])
            phase_series = matrix_vector_convolution(
                scaled_argument(exponential, theta[n]), constant_phase)
            transformed.append(phase_series)
            if n in (0, 3):
                need(phase_series == constant_phase, "F_GAUGE")
            dressed = matrix_vector_convolution(
                scaled_argument(exponential, -theta[n]), phase_series)
            need(dressed == constant_phase, "F_GAUGE")
            phase_q = [coefficient[:6] for coefficient in phase_series]
            phase_p = [coefficient[6:] for coefficient in phase_series]
            d_phase_q = [matvec(dmat, coefficient) for coefficient in phase_q]
            kinetic = vector_dot_convolution(phase_p, phase_p)
            potential_energy = vector_dot_convolution(phase_q, d_phase_q)
            energy_series = [(a + b) / 2 for a, b in zip(kinetic, potential_energy)]
            need(energy_series == [hamiltonian] + [ZERO] * ORDER, "F_GAUGE")
            composed = matrix_vector_convolution(
                scaled_argument(exponential, eta[n]), phase_series)
            combined = matrix_vector_convolution(
                scaled_argument(exponential, theta[n] + eta[n]), constant_phase)
            need(composed == combined, "F_GAUGE")
            if seed == 1:
                wrong_dressed = matrix_vector_convolution(
                    scaled_argument(exponential, theta[n]), phase_series)
                bad_positive_dressing = bad_positive_dressing or any(wrong_dressed[1])
            counts["GAUGE_PHASE_SERIES"] += 1
            for degree, coefficient in enumerate(phase_series):
                records.append("G|" + str(seed) + "|" + str(n) + "|" + str(degree)
                               + "|" + csv(coefficient))

        action_series = [ZERO] * (ORDER + 1)
        for bond in range(3):
            transformed_transfer = scaled_argument(transfers, alpha[bond])
            actual_transfer = matrix_vector_convolution(transformed_transfer, transformed[bond])
            need(actual_transfer == transformed[bond + 1], "F_GAUGE")
            qseries = [coefficient[:6] for coefficient in transformed[bond]]
            endqseries = [coefficient[:6] for coefficient in transformed[bond + 1]]
            at = scaled_argument(aseries, alpha[bond])
            et = scaled_argument(eseries, alpha[bond])
            actual_incoming = vector_series_subtract(
                matrix_vector_convolution(et, endqseries),
                matrix_vector_convolution(at, qseries))
            actual_outgoing = vector_series_subtract(
                matrix_vector_convolution(at, endqseries),
                matrix_vector_convolution(et, qseries))
            need(actual_incoming == [coefficient[6:] for coefficient in transformed[bond]]
                 and actual_outgoing == [coefficient[6:] for coefficient in transformed[bond + 1]],
                 "F_GAUGE")
            actual_bond_series = polynomial_action(qseries, endqseries, at, et)
            action_series = vadd(action_series, actual_bond_series)
            if seed == 1:
                omitted_phase_transfer = matrix_vector_convolution(
                    transformed_transfer, constant_vector_series(phases[bond]))
                residual = vector_series_subtract(
                    omitted_phase_transfer, constant_vector_series(phases[bond + 1]))
                bad_unchanged_phase = bad_unchanged_phase or any(residual[1])
            counts["GAUGE_BOND_SERIES"] += 1
        need(action_series == [actual_sum] + [ZERO] * ORDER, "F_GAUGE")
        counts["GAUGE_ACTION_SERIES"] += 1
        records.append("S|" + str(seed) + "|" + csv(action_series))

    initial_caustic_phases = []
    forbidden_endpoint_changes = []
    caustic_energy = None
    for sign in (-1, 1):
        signed_uniform = vscale(sign, uniform)
        reference_lapses = None
        reference_cumulative = None
        reference_phases = None
        for distinguished in range(3):
            lapses = [F(-3 if bond == distinguished else 0) for bond in range(3)]
            cumulative = [ZERO]
            for lapse in lapses:
                cumulative.append(cumulative[-1] + lapse)
            phases = [vscale(F(n) + cumulative[n], signed_uniform) + signed_uniform
                      for n in range(4)]
            need(phases[0][:6] == phases[3][:6] == [ZERO] * 6, "F_CAUSTIC")
            need(sum(lapses, ZERO) == -3, "F_CAUSTIC")
            energies = [energy(phase, dmat) for phase in phases]
            need(energies == [F(5, 2)] * 4, "F_CAUSTIC")
            caustic_energy = energies[0]
            bond_actions = []
            parameter_derivatives = []
            caustic_incoming = []
            caustic_outgoing = []
            for bond, lapse in enumerate(lapses):
                displacement = vsub(phases[bond + 1][:6], phases[bond][:6])
                denominator = 1 + lapse
                need(denominator != 0, "F_CAUSTIC")
                squared_displacement = dot(displacement, displacement)
                bond_actions.append(squared_displacement / (2 * denominator))
                caustic_incoming.append(vscale(1 / denominator, displacement))
                caustic_outgoing.append(vscale(1 / denominator, displacement))
                parameter_derivatives.append(-squared_displacement / (2 * denominator ** 2))
                need(caustic_incoming[-1] == phases[bond][6:]
                     and caustic_outgoing[-1] == phases[bond + 1][6:], "F_CAUSTIC")
            need(all(caustic_outgoing[n - 1] == caustic_incoming[n] for n in (1, 2)),
                 "F_CAUSTIC")
            need(parameter_derivatives == [-caustic_energy] * 3, "F_CAUSTIC")
            total_action = sum(bond_actions, ZERO)
            works = [dot(direction, parameter_derivatives) for direction in DIRECTIONS]
            need(total_action == 0 and works == [ZERO] * 3, "F_CAUSTIC")
            if distinguished == 0:
                reference_lapses = lapses
                reference_cumulative = cumulative
                reference_phases = phases
                initial_caustic_phases.append(tuple(phases[0]))
            else:
                theta = vsub(cumulative, reference_cumulative)
                equivalent_lapses = [reference_lapses[n] + theta[n + 1] - theta[n]
                                     for n in range(3)]
                equivalent_phases = [vadd(reference_phases[n][:6],
                                         vscale(theta[n], reference_phases[n][6:]))
                                     + reference_phases[n][6:] for n in range(4)]
                need(theta[0] == theta[3] == 0 and equivalent_lapses == lapses
                     and equivalent_phases == phases, "F_CAUSTIC")

            forbidden_theta = [ZERO, ZERO, ZERO, ONE]
            changed_lapses = [lapses[n] + forbidden_theta[n + 1] - forbidden_theta[n]
                              for n in range(3)]
            changed_phases = [vadd(phases[n][:6], vscale(forbidden_theta[n], phases[n][6:]))
                              + phases[n][6:] for n in range(4)]
            lapse_change = sum(changed_lapses, ZERO) - sum(lapses, ZERO)
            final_q_change = vsub(changed_phases[3][:6], phases[3][:6])
            need(lapse_change == 1 and final_q_change == signed_uniform, "F_CAUSTIC")
            forbidden_endpoint_changes.append(lapse_change != 0 and any(final_q_change))
            counts["CAUSTIC_HISTORIES"] += 1
            records.append("C|" + str(sign) + "|" + str(distinguished) + "|" + csv(flat(phases))
                           + "|" + str(caustic_energy) + "|" + str(total_action)
                           + "|" + csv(works))

    caustic_orbits = len(set(initial_caustic_phases))
    need(caustic_orbits == 2, "F_CAUSTIC")
    controls = {
        "NC01": len(control_evidence["NC01"]) == 6 and all(control_evidence["NC01"]),
        "NC02": len(control_evidence["NC02"]) == 6 and all(control_evidence["NC02"]),
        "NC03": bad_unchanged_phase,
        "NC04": bad_positive_dressing,
        "NC05": initial_caustic_phases[0][6:] != initial_caustic_phases[1][6:],
        "NC06": len(control_evidence["NC06"]) == 6 and all(control_evidence["NC06"]),
        "NC07": len(forbidden_endpoint_changes) == 6 and all(forbidden_endpoint_changes),
        "NC08": len(control_evidence["NC08"]) == 6 and all(control_evidence["NC08"]),
    }
    for number in range(1, 9):
        name = "NC" + str(number).zfill(2)
        need(controls[name], "F_CONTROL")
        records.append("N|" + name + "|DETECTED")
    expected_counts = {
        "AUTHORITY_FILES": 5, "COMPOSITION_PAIRS": 15,
        "REGULAR_BOUNDARY_CASES": 6, "CONSTRAINED_VARIATIONS": 18,
        "FREE_LAPSE_WITNESSES": 6, "GAUGE_PHASE_SERIES": 24,
        "GAUGE_BOND_SERIES": 18, "GAUGE_ACTION_SERIES": 6,
        "CAUSTIC_HISTORIES": 6,
    }
    need(counts == expected_counts and len(controls) == 8, "F_COUNTS")
    need(len(records) == 189, "F_COUNTS")
    payload = ("\n".join(records) + "\n").encode("ascii")
    payload_digest = sha256(payload).hexdigest()
    certificate = [
        "CERTIFICATE=P-INTEGER-FIXED-DURATION-BOUNDARY-1",
        "AUTHORITY_FILES=" + str(counts["AUTHORITY_FILES"]),
        "SERIES_ORDER=" + str(ORDER),
        "COMPOSITION_PAIRS=" + str(counts["COMPOSITION_PAIRS"]),
        "REGULAR_BOUNDARY_CASES=" + str(counts["REGULAR_BOUNDARY_CASES"]),
        "CONSTRAINED_VARIATIONS=" + str(counts["CONSTRAINED_VARIATIONS"]),
        "FREE_LAPSE_WITNESSES=" + str(counts["FREE_LAPSE_WITNESSES"]),
        "GAUGE_PHASE_SERIES=" + str(counts["GAUGE_PHASE_SERIES"]),
        "GAUGE_BOND_SERIES=" + str(counts["GAUGE_BOND_SERIES"]),
        "GAUGE_ACTION_SERIES=" + str(counts["GAUGE_ACTION_SERIES"]),
        "CAUSTIC_HISTORIES=" + str(counts["CAUSTIC_HISTORIES"]),
        "CAUSTIC_ORBITS=" + str(caustic_orbits),
        "CAUSTIC_ENERGY=" + str(caustic_energy),
        "PAYLOAD_SHA256=" + payload_digest,
        "NEGATIVE_CONTROLS=" + str(len(controls)),
        "CERTIFICATE_RESULT=PASS",
    ]
    return "\n".join(certificate) + "\n"


def main():
    try:
        certificate = audit()
    except ScientificFailure as failure:
        sys.stdout.write(str(failure) + "\nRESULT=FAIL\n")
        return 0
    sys.stdout.write(certificate)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
