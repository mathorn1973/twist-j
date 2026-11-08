#!/usr/bin/env python3
"""Independent-method certificate for P-INTEGER-SOURCE-HOLONOMY-1.

NON-CANONICAL. Written from PREREG.md without access to the author code.
The implementer has seen the mathematical predictions. Independence is
implementation and method independence within the same assisted session;
it is neither external review nor result-blind experimentation.

Arithmetic uses five cyclic coefficients modulo the all-ones relation.
Hermitian transport uses coordinate formulas. K1 uses integer scaled
recurrences; rational pairs are reduced only when making the certificate.
"""

import hashlib
import itertools
import json
import math
import sys


class ScientificFailure(Exception):
    """A completed exact scientific check failed."""


def demand(condition, label):
    if not condition:
        raise ScientificFailure(label)


# Every ring element has five cyclic coefficients. The fifth coefficient
# is set to zero by subtracting its value times (1,1,1,1,1).
ZERO = (0, 0, 0, 0, 0)
ONE = (1, 0, 0, 0, 0)
JROOT = (0, 1, 0, 0, 0)
PHI = (0, 0, -1, -1, 0)
BIGJ = (1, 0, 1, 0, 0)
PHI_INVERSE = (-1, 0, -1, -1, 0)
BIGJ_INVERSE = (0, -1, -1, 0, 0)


def canonical(coefficients):
    last = coefficients[4]
    return tuple(value - last for value in coefficients)


def ring_integer(value):
    return (value, 0, 0, 0, 0)


def add(left, right):
    return canonical(tuple(left[k] + right[k] for k in range(5)))


def negate(value):
    return tuple(-entry for entry in value)


def subtract(left, right):
    return add(left, negate(right))


def scale(value, integer):
    return tuple(integer * entry for entry in value)


def multiply(left, right):
    cyclic = [0] * 5
    for i, left_coefficient in enumerate(left):
        if left_coefficient:
            for k, right_coefficient in enumerate(right):
                if right_coefficient:
                    cyclic[(i + k) % 5] += left_coefficient * right_coefficient
    return canonical(cyclic)


def conjugate(value):
    cyclic = [0] * 5
    for k, coefficient in enumerate(value):
        cyclic[(-k) % 5] += coefficient
    return canonical(cyclic)


def embedding(value, exponent):
    cyclic = [0] * 5
    for k, coefficient in enumerate(value):
        cyclic[(exponent * k) % 5] += coefficient
    return canonical(cyclic)


def field_trace(value):
    return 4 * value[0] - sum(value[1:])


def absolute_field_norm(value):
    result = ONE
    for exponent in (1, 2, 3, 4):
        result = multiply(result, embedding(value, exponent))
    demand(result[1:] == (0, 0, 0, 0), "ring/absolute_norm_not_integer")
    return result[0]


def four_coefficients(value):
    demand(value[4] == 0, "ring/noncanonical_fifth_coefficient")
    return list(value[:4])


def real_element(constant, phi_coefficient):
    return (constant, 0, -phi_coefficient, -phi_coefficient, 0)


def real_coefficients(value):
    demand(
        value[1] == 0 and value[2] == value[3] and value[4] == 0,
        "hermitian/diagonal_outside_Z_phi",
    )
    return (value[0], -value[2])


def hermitian_from_eight(values):
    demand(len(values) == 8, "hermitian/input_width")
    a = real_element(values[0], values[1])
    d = real_element(values[2], values[3])
    c = tuple(values[4:]) + (0,)
    return (a, d, c)


def eight_from_hermitian(register):
    a, d, c = register
    demand(c[4] == 0, "hermitian/off_diagonal_noncanonical")
    a_pair = real_coefficients(a)
    d_pair = real_coefficients(d)
    values = a_pair + d_pair + c[:4]
    demand(all(type(value) is int for value in values), "hermitian/noninteger")
    return values


def hermitian_add(left, right):
    return tuple(add(left[k], right[k]) for k in range(3))


def hermitian_subtract(left, right):
    return tuple(subtract(left[k], right[k]) for k in range(3))


def determinant(register):
    a, d, c = register
    return subtract(multiply(a, d), multiply(c, conjugate(c)))


def diagonal_transport(register, first, second):
    a, d, c = register
    return (
        multiply(multiply(first, conjugate(first)), a),
        multiply(multiply(second, conjugate(second)), d),
        multiply(multiply(first, conjugate(second)), c),
    )


def upper_transport(register, parameter):
    a, d, c = register
    parameter_bar = conjugate(parameter)
    cross = add(multiply(parameter, conjugate(c)), multiply(c, parameter_bar))
    square_term = multiply(multiply(parameter, parameter_bar), d)
    return (add(add(a, cross), square_term), d, add(c, multiply(parameter, d)))


def lower_transport(register, parameter):
    a, d, c = register
    parameter_bar = conjugate(parameter)
    cross = add(multiply(parameter, c), multiply(parameter_bar, conjugate(c)))
    square_term = multiply(multiply(parameter, parameter_bar), a)
    return (a, add(add(d, cross), square_term), add(c, multiply(a, parameter_bar)))


def transport_a(register):
    return diagonal_transport(register, BIGJ, PHI)


def transport_a_inverse(register):
    return diagonal_transport(register, BIGJ_INVERSE, PHI_INVERSE)


def norm_from_trace(register):
    a, d, c = register
    return field_trace(
        add(add(multiply(a, a), multiply(d, d)), scale(multiply(c, conjugate(c)), 2))
    )


def arithmetic_norm(register):
    a0, a1, d0, d1, c0, c1, c2, c3 = eight_from_hermitian(register)
    c_entries = (c0, c1, c2, c3)
    return (
        4 * a0 * a0 + 4 * a0 * a1 + 6 * a1 * a1
        + 4 * d0 * d0 + 4 * d0 * d1 + 6 * d1 * d1
        + 10 * sum(value * value for value in c_entries)
        - 2 * sum(c_entries) ** 2
    )


def energy(core):
    s, q, h, reference, detector, phase = core
    return (
        1 + s * s - s * q + q * q
        + arithmetic_norm(h) + arithmetic_norm(reference) + arithmetic_norm(detector)
    )


# Core state order: (s,q,H,R,Z,p). Full state appends (bank,direction).
def bare_step(core, direction):
    s, q, h, reference, detector, phase = core
    demand(direction in (-1, 1), "state/invalid_direction")
    demand(0 <= phase < 6, "state/invalid_phase")
    if direction == 1:
        operation = phase
        if operation == 0:
            s, q = s - q, s
        elif operation == 1:
            h = upper_transport(h, ring_integer(-q))
        elif operation == 2:
            h = transport_a_inverse(h)
        elif operation == 3:
            h = upper_transport(h, ring_integer(q))
        elif operation == 4:
            h = transport_a(h)
        else:
            detector = hermitian_add(detector, hermitian_subtract(h, reference))
        phase = (phase + 1) % 6
    else:
        operation = (phase - 1) % 6
        if operation == 0:
            s, q = q, q - s
        elif operation == 1:
            h = upper_transport(h, ring_integer(q))
        elif operation == 2:
            h = transport_a(h)
        elif operation == 3:
            h = upper_transport(h, ring_integer(-q))
        elif operation == 4:
            h = transport_a_inverse(h)
        else:
            detector = hermitian_subtract(detector, hermitian_subtract(h, reference))
        phase = operation
    return (s, q, h, reference, detector, phase)


def funded_step(state, inverse=False):
    core = state[:6]
    bank, direction = state[6:]
    demand(type(bank) is int and bank >= 0, "state/invalid_bank")
    candidate = bare_step(core, -direction if inverse else direction)
    balance = bank + energy(core) - energy(candidate)
    if balance >= 0:
        return candidate + (balance, direction)
    return core + (bank, -direction)


def pack(state):
    s, q, h, reference, detector, phase, bank, direction = state
    values = [s, q, phase, bank, direction]
    values.extend(eight_from_hermitian(h))
    values.extend(eight_from_hermitian(reference))
    values.extend(eight_from_hermitian(detector))
    demand(len(values) == 29, "state/packed_width")
    demand(all(type(value) is int for value in values), "state/packed_noninteger")
    return values


def hash_row(digest, row):
    encoded = json.dumps(row, separators=(",", ":")) + "\n"
    digest.update(encoded.encode("utf-8"))


# Matrix arithmetic is used only for the independent algebraic controls;
# all transported Hermitian data above use direct coordinate formulas.
def matrix_multiply(left, right):
    return (
        add(multiply(left[0], right[0]), multiply(left[1], right[2])),
        add(multiply(left[0], right[1]), multiply(left[1], right[3])),
        add(multiply(left[2], right[0]), multiply(left[3], right[2])),
        add(multiply(left[2], right[1]), multiply(left[3], right[3])),
    )


def matrix_trace(matrix):
    return add(matrix[0], matrix[3])


def audit_constants_and_controls():
    demand(multiply(BIGJ, BIGJ_INVERSE) == ONE, "constants/J_inverse")
    demand(multiply(PHI, PHI_INVERSE) == ONE, "constants/phi_inverse")
    demand(multiply(BIGJ, PHI) == JROOT, "constants/J_phi")
    v = subtract(multiply(BIGJ, PHI_INVERSE), ONE)
    w = multiply(v, conjugate(v))
    constants = {
        "phi": four_coefficients(PHI),
        "J": four_coefficients(BIGJ),
        "v": four_coefficients(v),
        "w": four_coefficients(w),
        "trace_w": field_trace(w),
        "trace_w2": field_trace(multiply(w, w)),
    }
    expected = {
        "phi": [0, 0, -1, -1],
        "J": [1, 0, 1, 0],
        "v": [-2, 1, -1, 0],
        "w": [9, 0, 5, 5],
        "trace_w": 26,
        "trace_w2": 294,
    }
    demand(constants == expected, "constants/predictions")
    identity_h = hermitian_from_eight((1, 0, 1, 0, 0, 0, 0, 0))
    changed_h = diagonal_transport(identity_h, BIGJ, ONE)
    control_one = (
        absolute_field_norm(BIGJ) == 1
        and determinant(changed_h) != determinant(identity_h)
    )
    demand(control_one, "negative_control/absolute_not_relative_norm")

    control_two = JROOT != ONE
    for index in range(8):
        basis = tuple(1 if position == index else 0 for position in range(8))
        basis_h = hermitian_from_eight(basis)
        control_two = control_two and diagonal_transport(basis_h, JROOT, JROOT) == basis_h
    demand(control_two, "negative_control/central_phase")

    identity_m = (ONE, ZERO, ZERO, ONE)
    a_matrix = (BIGJ, ZERO, ZERO, PHI)
    a_inverse = (BIGJ_INVERSE, ZERO, ZERO, PHI_INVERSE)
    b_matrix = (ONE, ONE, ZERO, ONE)
    b_inverse = (ONE, negate(ONE), ZERO, ONE)
    commutator = matrix_multiply(
        matrix_multiply(matrix_multiply(a_matrix, b_matrix), a_inverse), b_inverse
    )
    demand(commutator == (ONE, v, ZERO, ONE), "loop/commutator_formula")
    detector_h = hermitian_from_eight((0, 0, 1, 0, 0, 0, 0, 0))
    control_three = (
        matrix_trace(commutator) == matrix_trace(identity_m) == ring_integer(2)
        and upper_transport(detector_h, v) != detector_h
    )
    demand(control_three, "negative_control/trace_two_nontrivial_action")

    edge_10 = a_matrix
    edge_21 = matrix_multiply(b_matrix, a_inverse)
    edge_02 = b_inverse
    control_four = (
        matrix_multiply(matrix_multiply(edge_02, edge_21), edge_10) == identity_m
    )
    demand(control_four, "negative_control/pure_frames_telescope")
    return constants, [control_one, control_two, control_three, control_four], v, w


def audit_transport():
    digest = hashlib.sha256()
    rows = 0
    for coordinates in itertools.product((-1, 0, 1), repeat=8):
        h = hermitian_from_eight(coordinates)
        label = "transport/row=" + str(rows)
        calculated_norm = norm_from_trace(h)
        demand(calculated_norm == arithmetic_norm(h), label + "/norm_formula")
        demand(
            calculated_norm >= 2 * sum(value * value for value in coordinates),
            label + "/norm_lower_bound",
        )
        before = determinant(h)
        real_coefficients(before)
        outputs = (
            transport_a(h),
            transport_a_inverse(h),
            upper_transport(h, ONE),
            upper_transport(h, negate(ONE)),
            lower_transport(h, ONE),
            lower_transport(h, negate(ONE)),
        )
        output_coordinates = []
        for gate_index, output in enumerate(outputs):
            demand(determinant(output) == before, label + "/gate=" + str(gate_index))
            output_coordinates.append(list(eight_from_hermitian(output)))
        hash_row(digest, [list(coordinates), output_coordinates])
        rows += 1
    demand(rows == 6561, "transport/row_count")
    return rows, digest.hexdigest()


def fixtures():
    zero8 = (0, 0, 0, 0, 0, 0, 0, 0)
    d8 = (0, 0, 1, 0, 0, 0, 0, 0)
    i8 = (1, 0, 1, 0, 0, 0, 0, 0)
    j8 = (1, 0, 1, 0, 0, 1, 0, 0)
    raw = (
        (d8, d8, j8),
        (i8, d8, (0, 1, 1, -1, 1, 1, -1, 0)),
        ((1, -1, -1, 1, 1, 0, -1, 1), i8, (-1, 0, -1, 0, 0, -1, 0, 0)),
        (zero8, zero8, zero8),
    )
    return tuple(tuple(hermitian_from_eight(register) for register in fixture) for fixture in raw)


def audit_complete_steps():
    digest = hashlib.sha256()
    rows = 0
    bank_values = (0, 1, 12, 32, 116, 346, 715, 716, 771, 772)
    fixture_values = fixtures()
    enumeration = itertools.product(
        (-1, 0, 1), (-1, 0, 1), range(6), (-1, 1), bank_values, fixture_values
    )
    for s, q, phase, direction, bank, fixture in enumeration:
        h, reference, detector = fixture
        core = (s, q, h, reference, detector, phase)
        state = core + (bank, direction)
        label = "full_step/row=" + str(rows)
        demand(bare_step(bare_step(core, 1), -1) == core, label + "/T_inverse_after_T")
        demand(bare_step(bare_step(core, -1), 1) == core, label + "/T_after_T_inverse")
        forward = funded_step(state)
        backward = funded_step(state, inverse=True)
        demand(funded_step(forward, inverse=True) == state, label + "/F_inverse_after_F")
        demand(funded_step(backward) == state, label + "/F_after_F_inverse")
        total = energy(core) + bank
        for name, output in (("forward", forward), ("inverse", backward)):
            demand(energy(output[:6]) + output[6] == total, label + "/" + name + "/energy")
            demand(output[6] >= 0, label + "/" + name + "/bank")
            demand(output[3] == reference, label + "/" + name + "/reference")
        hash_row(digest, [pack(state), pack(forward), pack(backward)])
        rows += 1
    demand(rows == 4320, "full_step/row_count")
    return rows, digest.hexdigest()


def ready_core(sign):
    d = hermitian_from_eight((0, 0, 1, 0, 0, 0, 0, 0))
    occupied = hermitian_from_eight((1, 0, 1, 0, 0, 1, 0, 0))
    return (sign, 0, d, d, occupied, 0)


def audit_experiments(v, w):
    digest = hashlib.sha256()
    rows = 0
    prefix_costs = []
    increments = []
    predicted_prefixes = {
        -1: [26, 26, 38, 58, 142, 372, 742],
        1: [26, 26, 38, 58, 142, 372, 798],
    }
    predicted_budgets = {-1: 716, 1: 772}
    for sign in (-1, 1):
        initial_core = ready_core(sign)
        label = "experiment/sign=" + str(sign)
        demand(eight_from_hermitian(initial_core[4])[5] == 1, label + "/occupied_input")
        bare_history = [initial_core]
        for unused in range(6):
            bare_history.append(bare_step(bare_history[-1], 1))
        costs = [energy(core) for core in bare_history]
        demand(costs == predicted_prefixes[sign], label + "/prefix_costs")
        prefix_costs.append([sign, costs])
        sharp_budget = max(costs) - costs[0]
        demand(sharp_budget == predicted_budgets[sign], label + "/sharp_budget")
        h_out = (w, ONE, scale(v, sign))
        z_out = (add(ONE, w), ONE, add(JROOT, scale(v, sign)))
        demand(bare_history[6][2] == h_out, label + "/loop_H_out")
        demand(bare_history[6][4] == z_out, label + "/detector_Z_out")
        demand(bare_history[6][0:2] == (sign, sign), label + "/source_link_out")
        demand(bare_history[6][5] == 0, label + "/six_phase_return")

        for initial_bank in (715, 716, 771, 772):
            history = [initial_core + (initial_bank, 1)]
            row_label = label + "/bank=" + str(initial_bank)
            for step_index in range(1, 7):
                history.append(funded_step(history[-1]))
                if step_index < 6 or initial_bank >= sharp_budget:
                    expected = bare_history[step_index] + (
                        initial_bank + costs[0] - costs[step_index], 1
                    )
                else:
                    expected = bare_history[5] + (initial_bank + costs[0] - costs[5], -1)
                demand(history[-1] == expected, row_label + "/step=" + str(step_index))
            restored = history[-1]
            for index in range(5, -1, -1):
                restored = funded_step(restored, inverse=True)
                demand(restored == history[index], row_label + "/reverse=" + str(index))
            if initial_bank == 772:
                demand(history[-1][6] == (56 if sign == -1 else 0), row_label + "/final_bank")
                read_coordinate = eight_from_hermitian(history[-1][4])[5]
                demand(read_coordinate == 1 + sign, row_label + "/occupied_read_coordinate")
                demand(read_coordinate - 1 == sign, row_label + "/fixed_reader")
            hash_row(digest, [sign, initial_bank, [pack(state) for state in history]])
            rows += 1

        long_core = initial_core
        for unused in range(36):
            long_core = bare_step(long_core, 1)
        for index, name in ((0, "source"), (1, "link"), (2, "H"), (3, "reference"), (5, "phase")):
            demand(long_core[index] == initial_core[index], label + "/36_restore_" + name)
        increment = hermitian_subtract(long_core[4], initial_core[4])
        predicted_increment = (scale(w, 10), ZERO, scale(v, 6 * sign))
        demand(increment == predicted_increment, label + "/36_detector_increment")
        increments.append([sign, list(eight_from_hermitian(increment))])
    demand(rows == 8, "experiment/row_count")
    return rows, digest.hexdigest(), prefix_costs, increments


def reduce_pairs(numerators, denominator):
    pairs = []
    for numerator in numerators:
        divisor = math.gcd(numerator, denominator)
        pairs.append([numerator // divisor, denominator // divisor])
    return pairs


def three_valuation(positive_integer):
    demand(positive_integer > 0, "K1/nonpositive_denominator")
    value = 0
    while positive_integer % 3 == 0:
        positive_integer //= 3
        value += 1
    return value


def k1_stencil(numerators, position):
    return (
        460 * numerators[position]
        + 29 * (numerators[(position + 1) % 5] + numerators[(position - 1) % 5])
        + 65 * (numerators[(position + 2) % 5] + numerators[(position - 2) % 5])
    )


def audit_k1():
    words = ("0010", "0011", "0100", "0101", "0110", "1001", "1010", "1011", "1100", "1101")
    digest = hashlib.sha256()
    rows = 0
    for word in words:
        digits = tuple(int(digit) for digit in word)
        scaled_history = []
        for time in (0, 1):
            offset = digits[time + 2] - digits[time]
            numerators = tuple(
                int(position == offset % 5) + int(position == (offset + 1) % 5)
                for position in range(5)
            )
            scaled_history.append((numerators, 2))
        for time in range(2, 25):
            previous, previous_denominator = scaled_history[-1]
            earlier, earlier_denominator = scaled_history[-2]
            denominator = 324 * previous_denominator
            demand(denominator % earlier_denominator == 0, "K1/scaled_denominator_divisibility")
            multiplier = denominator // earlier_denominator
            numerators = tuple(
                k1_stencil(previous, position) - multiplier * earlier[position]
                for position in range(5)
            )
            scaled_history.append((numerators, denominator))

        for time, (numerators, denominator) in enumerate(scaled_history):
            label = "K1/word=" + word + "/n=" + str(time)
            demand(sum(numerators) == denominator, label + "/mass")
            pairs = reduce_pairs(numerators, denominator)
            common_denominator = 1
            for numerator, entry_denominator in pairs:
                demand(math.gcd(numerator, entry_denominator) == 1, label + "/fraction_reduction")
                common_denominator = (
                    common_denominator // math.gcd(common_denominator, entry_denominator)
                ) * entry_denominator
            expected_valuation = 0 if time == 0 else 4 * (time - 1)
            demand(three_valuation(common_denominator) == expected_valuation, label + "/valuation")
            if time >= 2:
                previous, previous_denominator = scaled_history[time - 1]
                earlier, earlier_denominator = scaled_history[time - 2]
                for position in range(5):
                    left = 324 * previous_denominator * earlier_denominator * numerators[position]
                    right = denominator * (
                        earlier_denominator * k1_stencil(previous, position)
                        - 324 * previous_denominator * earlier[position]
                    )
                    demand(left == right, label + "/recurrence/r=" + str(position))
            hash_row(digest, [word, time, pairs])
            rows += 1
    demand(rows == 250, "K1/row_count")
    return rows, digest.hexdigest()


def certificate():
    constants, controls, v, w = audit_constants_and_controls()
    transport_rows, transport_digest = audit_transport()
    step_rows, step_digest = audit_complete_steps()
    experiment_rows, experiment_digest, prefix_costs, increments = audit_experiments(v, w)
    k1_rows, k1_digest = audit_k1()
    return {
        "schema": "P-INTEGER-SOURCE-HOLONOMY-1/v1",
        "constants": constants,
        "transport_rows": transport_rows,
        "transport_sha256": transport_digest,
        "step_rows": step_rows,
        "step_sha256": step_digest,
        "experiment_rows": experiment_rows,
        "experiment_sha256": experiment_digest,
        "prefix_costs": prefix_costs,
        "detector_increments_36": increments,
        "k1_rows": k1_rows,
        "k1_sha256": k1_digest,
        "negative_controls": controls,
    }


if __name__ == "__main__":
    try:
        result = certificate()
    except ScientificFailure as failure:
        result = {"failure": str(failure)}
    sys.stdout.write(json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n")
