#!/usr/bin/env python3
"""Exact prepared snapshots of one overlapping-contact work/clock completion.

Universal continuous assertions belong to PROOF.md. No floating-point
trigonometry, predecessor executable, search or external data is consumed.
"""

from fractions import Fraction as F
from hashlib import sha256
import importlib.util
from itertools import product
import json
from pathlib import Path


CHECKER_SHA256 = "3db7f8389fef4189631cbca38d8fa99c81ba64acb26c1a11f6ab3cc30173fe78"
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
TWO = (2, 0, 0, 0)
U = (1, -1, 0, 0)
B0 = (1, 0, -1, 0)
LAMBDAS = (0, 1, 2, 7)
EDGES = ((0, 1), (1, 2))
PULSES = tuple((edge, kind) for edge in EDGES
               for kind in ("compute", "contact", "uncompute"))
OMEGA0 = ((0, 1, 0, 0), (-1, 0, 1, 0), (0, -1, 0, 1), (0, 0, -1, 0))
GRAM = tuple(tuple(5 * int(i == k) - 1 for k in range(4)) for i in range(4))


def json_default(value):
    if isinstance(value, F):
        return value.numerator if value.denominator == 1 else [value.numerator, value.denominator]
    raise TypeError("noncanonical JSON value")


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      default=json_default).encode("ascii")


def emit(kind, **fields):
    print(encoded(dict(kind=kind, **fields)).decode("ascii"))


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def scale(n, x):
    return tuple(n * a for a in x)


def q(x):
    return F(5 * sum(a * a for a in x) - sum(x) ** 2, 2)


def account(data):
    return sum(q(x) for x in data)


def interaction(data):
    return q(sub(data[0], data[1])) + q(sub(data[1], data[2]))


def parity(data, edge):
    i, k = edge
    return all(a % 2 == 0 for a in sub(data[i], data[k]))


def rotate(x, multiplier):
    a, b, c, d = x
    if multiplier == "full":
        return d - c, -c, a - c, b - c
    if multiplier == "half":
        return d, d - a, d - b, d - c
    if multiplier == "inverse":
        return c - b, d - b, -b, a - b
    if multiplier == "inverse_half":
        return a - b, a - c, a - d, a
    raise ValueError("unknown multiplier")


def pair_map(data, edge, multiplier="full", force_rational=False):
    i, k = edge
    if not force_rational and not parity(data, edge):
        raise ArithmeticError("active primary pair lacks integral admission")
    total = add(data[i], data[k])
    delta = rotate(sub(data[i], data[k]), multiplier)
    numerators = (add(total, delta), sub(total, delta))
    if force_rational:
        pair = tuple(tuple(F(a, 2) for a in v) for v in numerators)
    else:
        if any(a % 2 for v in numerators for a in v):
            raise ArithmeticError("nonintegral primary snapshot")
        pair = tuple(tuple(a // 2 for a in v) for v in numerators)
    result = list(data)
    result[i], result[k] = pair
    return tuple(result)


def total_contact(data, edge):
    return pair_map(data, edge) if parity(data, edge) else data


def controller_energy(ctrl_q, ctrl_p):
    return 4 * ((ctrl_q - F(1, 2)) ** 2 + ctrl_p ** 2)


def base_energy(state, lam):
    data, _bank, _hand, ctrl_q, ctrl_p = state
    return account(data) + lam * interaction(data) + controller_energy(ctrl_q, ctrl_p)


def half_pulse(state, edge, kind, lam, direction):
    data, bank, hand, ctrl_q, ctrl_p = state
    before = base_energy(state, lam)
    admitted = parity(data, edge)
    if kind in ("compute", "uncompute"):
        if admitted:
            if direction == 1:
                ctrl_q, ctrl_p = F(1, 2) + ctrl_p, F(1, 2) - ctrl_q
            else:
                ctrl_q, ctrl_p = F(1, 2) - ctrl_p, ctrl_q - F(1, 2)
    elif kind == "contact":
        if ctrl_q != int(admitted) or ctrl_p != 0:
            raise ArithmeticError("primary contact has a stale or nonlogical controller")
        if admitted:
            data = pair_map(data, edge, "half" if direction == 1 else "inverse_half")
    else:
        raise ValueError("unknown pulse kind")
    unbalanced = data, bank, (hand + direction) % 12, ctrl_q, ctrl_p
    return data, bank + before - base_energy(unbalanced, lam), unbalanced[2], ctrl_q, ctrl_p


class ScientificFailure(Exception):
    pass


class Audit:
    def __init__(self, checker):
        self.checker = checker
        self.checks = 0

    def require(self, condition, name, context=None):
        self.checks += 1
        if not condition:
            raise ScientificFailure(encoded(dict(check=name, context=context)).decode("ascii"))

    def compare(self, state, other, context):
        transformed = (self.checker.to_power(other[0]), other[1], 2 * other[2], other[3], other[4])
        self.require(transformed == state, "independent_complete_snapshot", context)

    def snapshot(self, state, other, lam, initial_r, initial_h, initial_sum, context):
        self.compare(state, other, context)
        data, bank, hand, ctrl_q, ctrl_p = state
        r, interaction_value = account(data), interaction(data)
        self.require(r == initial_r, "data_account", context)
        self.require(controller_energy(ctrl_q, ctrl_p) == 1, "controller_account", context)
        self.require(base_energy(state, lam) + bank == initial_h, "complete_energy", context)
        self.require(self.checker.energy(other, lam) == initial_h, "independent_energy", context)
        self.require(bank >= 0, "nonnegative_bank", context)
        self.require(bank >= lam * (3 * r - interaction_value), "preserved_safe_margin", context)
        self.require(3 * r - interaction_value ==
                     q(add(add(data[0], data[1]), data[2])) + q(sub(data[0], data[2])),
                     "whole_path_bound_identity", context)
        self.require(tuple(sum(v[i] for v in data) for i in range(4)) == initial_sum,
                     "data_sum", context)
        self.require(all(type(a) is int for v in data for a in v), "integral_data_snapshot", context)
        self.require(F(bank).denominator == 1 and 0 <= hand < 12, "bank_clock_snapshot", context)


def initial_pair(checker, data, bank):
    return ((data, F(bank), 0, F(0), F(0)),
            (checker.from_power(data), F(bank), F(0), F(0), F(0)))


def audit_program(audit, data, bank, lam, blocks, digest=None, case=None):
    state, other = initial_pair(audit.checker, data, bank)
    initial_state = state
    r, h = account(data), base_energy(state, lam) + state[1]
    initial_sum = tuple(sum(v[i] for v in data) for i in range(4))
    audit.require(bank >= lam * (3 * r - interaction(data)), "funded_preparation", case)
    history = [state]
    operations = []
    counts = dict(forward_halfsteps=0, inverse_halfsteps=0, active_contact_halfsteps=0,
                  held_contact_halfsteps=0, active_controller_halfsteps=0)
    audit.snapshot(state, other, lam, r, h, initial_sum, (case, "initial"))
    if digest is not None:
        digest.update(encoded((case, "initial", state)) + b"\n")
    boundaries = []
    for block in range(blocks):
        for pulse, (edge, kind) in enumerate(PULSES):
            computed_bit = int(parity(state[0], edge))
            for half in range(2):
                if kind == "contact":
                    counts["active_contact_halfsteps" if computed_bit else "held_contact_halfsteps"] += 1
                elif computed_bit:
                    counts["active_controller_halfsteps"] += 1
                state = half_pulse(state, edge, kind, lam, 1)
                other = audit.checker.pulse(other, edge, kind, lam, F(1, 2))
                context = (case, "forward", block, pulse, half)
                audit.snapshot(state, other, lam, r, h, initial_sum, context)
                if digest is not None:
                    digest.update(encoded((context, state)) + b"\n")
                history.append(state)
                operations.append((edge, kind))
                counts["forward_halfsteps"] += 1
            expected_q = 0 if kind == "uncompute" else computed_bit
            audit.require(state[3:] == (F(expected_q), F(0)), "pulse_endpoint_controller", context)
            if kind == "contact":
                boundaries.append(state)
        audit.require(state[2:] == (0, F(0), F(0)), "block_ready_and_clock_return", (case, block))
    final = state
    for reverse_index, (edge, kind) in enumerate(reversed(operations), 1):
        state = half_pulse(state, edge, kind, lam, -1)
        other = audit.checker.pulse(other, edge, kind, lam, F(-1, 2))
        context = (case, "inverse", reverse_index)
        audit.snapshot(state, other, lam, r, h, initial_sum, context)
        audit.require(state == history[-1 - reverse_index], "literal_snapshot_inverse", context)
        if digest is not None:
            digest.update(encoded((context, state)) + b"\n")
        counts["inverse_halfsteps"] += 1
    audit.require(state == initial_state, "complete_inverse", case)
    return final, boundaries, counts


def transpose(matrix):
    return tuple(zip(*matrix))


def identity(n):
    return tuple(tuple(F(i == k) for k in range(n)) for i in range(n))


def mm(a, b):
    return tuple(tuple(sum(x * y for x, y in zip(row, col)) for col in zip(*b)) for row in a)


def block_diagonal(blocks):
    size = sum(len(block) for block in blocks)
    out = [[F(0)] * size for _ in range(size)]
    offset = 0
    for block in blocks:
        for i, row in enumerate(block):
            for k, value in enumerate(row):
                out[offset + i][offset + k] = F(value)
        offset += len(block)
    return tuple(map(tuple, out))


def matrix_inverse(matrix):
    n = len(matrix)
    rows = [list(map(F, row)) + list(identity(n)[i]) for i, row in enumerate(matrix)]
    for k in range(n):
        pivot = next((i for i in range(k, n) if rows[i][k]), None)
        if pivot is None:
            raise ArithmeticError("singular exact form")
        rows[k], rows[pivot] = rows[pivot], rows[k]
        divisor = rows[k][k]
        rows[k] = [v / divisor for v in rows[k]]
        for i in range(n):
            if i != k:
                factor = rows[i][k]
                rows[i] = [x - factor * y for x, y in zip(rows[i], rows[k])]
    return tuple(tuple(row[n:]) for row in rows)


def matrix_power(matrix, exponent):
    value = identity(len(matrix))
    for _ in range(exponent):
        value = mm(value, matrix)
    return value


def multiplier_matrix(name):
    columns = [rotate(tuple(int(i == k) for i in range(4)), name) for k in range(4)]
    return transpose(columns)


def contact_matrix(edge, name):
    multiplier = multiplier_matrix(name)
    out = [list(row) for row in identity(12)]
    left, right = edge
    for i in range(4):
        for k in range(4):
            plus = F(int(i == k) + multiplier[i][k], 2)
            minus = F(int(i == k) - multiplier[i][k], 2)
            out[4 * left + i][4 * left + k] = plus
            out[4 * right + i][4 * right + k] = plus
            out[4 * left + i][4 * right + k] = minus
            out[4 * right + i][4 * left + k] = minus
    return tuple(map(tuple, out))


def matrix_audit(audit):
    omega = block_diagonal((OMEGA0,) * 3)
    gram = block_diagonal((GRAM,) * 3)
    for edge in EDGES:
        full, half, inverse, inverse_half = [contact_matrix(edge, name)
                                            for name in ("full", "half", "inverse", "inverse_half")]
        for name, matrix in (("full", full), ("half", half), ("inverse", inverse),
                             ("inverse_half", inverse_half)):
            audit.require(mm(mm(transpose(matrix), omega), matrix) == omega, "matrix_symplectic", (edge, name))
            audit.require(mm(mm(transpose(matrix), gram), matrix) == gram, "matrix_account", (edge, name))
        audit.require(mm(half, half) == full, "half_square", edge)
        audit.require(matrix_power(full, 5) == identity(12), "contact_fifth_power", edge)
        audit.require(matrix_power(half, 10) == identity(12), "half_tenth_power", edge)
        audit.require(mm(full, inverse) == identity(12), "contact_inverse", edge)
        audit.require(mm(half, inverse_half) == identity(12), "half_inverse", edge)
    emit("MATRICES", status="PASS", base_data_dimension=12, pair_edges=EDGES,
         exact_forms="primitive symplectic and half-trace", contact_order=5, half_order=10)


# Sparse exact polynomials in independent formal gradient symbols.
def pc(value):
    return {(): F(value)} if value else {}


def pv(index):
    return {(index,): F(1)}


def pa(a, b):
    result = dict(a)
    for term, coefficient in b.items():
        result[term] = result.get(term, F(0)) + coefficient
        if not result[term]:
            del result[term]
    return result


def pn(a):
    return {term: -coefficient for term, coefficient in a.items()}


def pm(a, b):
    result = {}
    for term_a, coefficient_a in a.items():
        for term_b, coefficient_b in b.items():
            term = tuple(sorted(term_a + term_b))
            result[term] = result.get(term, F(0)) + coefficient_a * coefficient_b
            if not result[term]:
                del result[term]
    return result


def ps(values):
    result = {}
    for value in values:
        result = pa(result, value)
    return result


def pmm(a, b):
    return tuple(tuple(ps(pm(x, y) for x, y in zip(row, col)) for col in zip(*b)) for row in a)


def formal_suspension(audit):
    base = block_diagonal((OMEGA0,) * 3 + (((0, 1), (-1, 0)),))
    inv = matrix_inverse(base)
    product_form = block_diagonal((base, ((0, 1), (-1, 0))))
    energy_gradient = [pv(i) for i in range(14)]
    phase_gradient = [pv(14 + i) for i in range(14)]
    time_gradient = pv(28)
    mixed_gradient = [pa(e, pn(h)) for e, h in zip(energy_gradient, phase_gradient)]
    jacobian = [[pc(value) for value in row] for row in identity(16)]
    inverse_jacobian = [[pc(value) for value in row] for row in identity(16)]
    for i in range(14):
        jacobian[15][i] = mixed_gradient[i]
        inverse_jacobian[15][i] = pn(mixed_gradient[i])
    jacobian[15][14] = pn(time_gradient)
    inverse_jacobian[15][14] = time_gradient
    product_polynomial = tuple(tuple(pc(value) for value in row) for row in product_form)
    pulled = pmm(transpose(jacobian), pmm(product_polynomial, jacobian))
    expected = [[pc(value) for value in row] for row in product_form]
    for i in range(14):
        expected[14][i] = mixed_gradient[i]
        expected[i][14] = pn(mixed_gradient[i])
    audit.require(pulled == tuple(map(tuple, expected)), "formal_fixed_form_pullback")
    audit.require(pmm(jacobian, inverse_jacobian) ==
                  tuple(tuple(pc(value) for value in row) for row in identity(16)), "formal_coordinate_inverse")
    base_field = [pn(ps(pm(pc(inv[i][k]), phase_gradient[k]) for k in range(14))) for i in range(14)]
    bank_field = pn(ps(pm(e, x) for e, x in zip(energy_gradient, base_field)))
    velocity = base_field + [pc(1), bank_field]
    contraction_negative = pmm(pulled, tuple((value,) for value in velocity))
    target_negative = [pn(value) for value in energy_gradient] + [{}, pc(-1)]
    audit.require([row[0] for row in contraction_negative] == target_negative, "formal_hamilton_equation")
    b_capital_dot = ps([bank_field, pn(time_gradient)] +
                       [pm(value, x) for value, x in zip(mixed_gradient, base_field)])
    audit.require(b_capital_dot == pn(time_gradient), "capital_bank_time_derivative")
    audit.require(not ps(pm(h, x) for h, x in zip(phase_gradient, base_field)), "phase_self_bracket")
    emit("FORMAL_SUSPENSION", status="PASS", base_dimension=14, full_dimension=16,
         formal_variables=29, all_coefficients=True, clock_velocity=1,
         capital_bank_velocity="-partial_t h", literal_bank_velocity="-dE/ds")


def selector_audit(audit):
    for residues in product((0, 1), repeat=4):
        cosines = tuple(1 - 2 * value for value in residues)
        factors = tuple(F(1 + value, 2) for value in cosines)
        value = F(1)
        for factor in factors:
            value *= factor
        audit.require(value == int(not any(residues)), "exact_parity_selector", residues)
        # Each derivative has one factor -sin(pi*n)/2 times pi, hence zero.
        sine_coefficients = (0,) * 4
        gradient_pi_coefficients = []
        for coordinate in range(4):
            derivative = F(-sine_coefficients[coordinate], 2)
            for other in range(4):
                if coordinate != other:
                    derivative *= factors[other]
            gradient_pi_coefficients.append(derivative)
        audit.require(gradient_pi_coefficients == [0] * 4, "selector_critical_point", residues)
        transformed = audit.checker.from_power((residues, ZERO, ZERO))[0]
        audit.require(all(a % 2 == 0 for a in transformed) == (value == 1), "basis_independent_admission", residues)
    for bit in (0, 1):
        cosine, sine = 1 - 2 * bit, 0
        audit.require(F(1 - cosine, 2) == bit and sine == 0, "controller_selector_critical_point", bit)
    emit("SELECTORS", status="PASS", coefficient_parity_patterns=16,
         parity_gradient="zero by sin(pi*n)=0", controller_bits=2, floating_point=False)


def finite_audit(audit):
    values = tuple(sorted({ZERO, ONE, TWO, U, scale(-1, U), B0, scale(-1, B0)}))
    audit.require(len(values) == 7 and max(q(v) for v in values) == 8, "frozen_value_family")
    digest = sha256()
    totals = dict(cases=0, forward_halfsteps=0, inverse_halfsteps=0,
                  active_contact_halfsteps=0, held_contact_halfsteps=0, active_controller_halfsteps=0)
    for data in product(values, repeat=3):
        r, i = account(data), interaction(data)
        audit.require(r <= 24 and 0 <= i <= 3 * r, "finite_family_bound", data)
        for lam in LAMBDAS:
            beta = lam * (3 * r - i)
            banks = sorted({beta, beta + 1, 72 * lam})
            for bank in banks:
                case = (data, lam, bank)
                _final, _boundaries, counts = audit_program(audit, data, bank, lam, 2, digest, case)
                totals["cases"] += 1
                for key, value in counts.items():
                    totals[key] += value
    emit("FINITE", status="PASS", values=7, triples=343, lambdas=LAMBDAS,
         blocks_per_case=2, half_window_hand_modulus=12, snapshot_sha256=digest.hexdigest(), **totals)


def witness_audit(audit):
    for data, expected in (((TWO, ZERO, ZERO), (True, False)),
                           ((TWO, ZERO, B0), (False, True))):
        after = total_contact(data, EDGES[0])
        observed = parity(data, EDGES[1]), parity(after, EDGES[1])
        audit.require(observed == expected, "stale_parity_witness", data)
        independent = audit.checker.contact(audit.checker.from_power(data), EDGES[0], "full", True)
        audit.require(audit.checker.to_power(independent) == after, "stale_witness_second_arithmetic", data)
        emit("STALE_PARITY", initial=data, after_first_contact=after,
             initial_second_admission=observed[0], fresh_second_admission=observed[1])
    after = total_contact((TWO, ZERO, ZERO), EDGES[0])
    invalid = pair_map(after, EDGES[1], "full", True)
    expected_invalid = (after[0], (F(1), F(1, 2), F(1, 2), F(1, 2)),
                        (F(0), F(-1, 2), F(-3, 2), F(-1, 2)))
    audit.require(invalid == expected_invalid and any(F(a).denominator != 1 for v in invalid for a in v),
                  "stale_forced_nonintegral_output")
    emit("STALE_FORCED_OUTPUT", data=invalid, integral=False)
    glue = (TWO, TWO, ZERO)
    glue_after = total_contact(glue, EDGES[1])
    d_before = scale(F(1, 2), sub(glue[0], glue[1]))
    d_after = scale(F(1, 2), sub(glue_after[0], glue_after[1]))
    audit.require(q(d_before) == 0 and q(d_after) == F(5, 4), "naive_first_generator_changes")
    audit.require(glue_after != glue and parity(glue, EDGES[1]), "naive_glue_actual_second_motion")
    emit("NAIVE_FIXED_FORM", initial=glue, after_second_contact=glue_after,
         first_relative_Q_before=0, first_relative_Q_after=F(5, 4),
         defect="-dt wedge d(h12 after C23-h12)", nonzero_by_positive_phase_weights=True)
    minus_ju = rotate(U, "half")
    reserve = (U, scale(-1, U), minus_ju)
    midpoint = pair_map(reserve, EDGES[0], "half")
    end = pair_map(reserve, EDGES[0], "full")
    audit.require([account(z) for z in (reserve, midpoint, end)] == [15, 15, 15], "reserve_R")
    audit.require([interaction(z) for z in (reserve, midpoint, end)] == [35, 40, 35], "reserve_interactions")
    for lam in LAMBDAS:
        rows = []
        for bank in sorted({0, 5 * lam, 10 * lam}):
            states = [(z, F(bank + lam * (35 - interaction(z))), 0, F(1), F(0))
                      for z in (reserve, midpoint, end)]
            audit.require([s[1] for s in states] == [bank, bank - 5 * lam, bank], "reserve_bank", (lam, bank))
            for s in states:
                other = (audit.checker.from_power(s[0]), s[1], F(0), s[3], s[4])
                audit.require(audit.checker.energy(other, lam) == 16 + 35 * lam + bank, "reserve_independent_energy")
            rows.append(dict(initial_bank=bank, bank_snapshots=[s[1] for s in states],
                             uniform_funded=bank >= 10 * lam))
        emit("RESERVE", lam=lam, R=15, I=[35, 40, 35], safe_guard=10 * lam,
             first_contact_sharp_reserve=5 * lam, rows=rows)
    work = (scale(2, U), scale(-2, U), scale(2, U))
    outputs = []
    for lam in (1, 2):
        final, boundaries, _ = audit_program(audit, work, 60, lam, 1, case=("work", lam))
        audit.require(account(work) == 60 and
                      [interaction(work)] + [interaction(s[0]) for s in boundaries] == [160, 120, 135],
                      "both_active_interaction_sequence", lam)
        audit.require(all(s[3] == 1 for s in boundaries), "both_contact_controls_active", lam)
        audit.require(final[1] == 60 + 25 * lam, "both_active_bank_gain", lam)
        outputs.append(final)
    audit.require((outputs[0][0], outputs[0][2:]) == (outputs[1][0], outputs[1][2:]), "same_projected_work_motion")
    emit("FREE_WORK_COEFFICIENT", initial_bank=60, lambdas=[1, 2], bank_final=[s[1] for s in outputs],
         R=60, I=[160, 120, 135], same_data_controller_clock=True)


def load_checker():
    path = Path(__file__).with_name("checker.py")
    if sha256(path.read_bytes()).hexdigest() != CHECKER_SHA256:
        raise ValueError("checker.py custody mismatch")
    spec = importlib.util.spec_from_file_location("overlap_checker", path)
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    return checker


def main():
    checker = load_checker()
    audit = Audit(checker)
    emit("SOURCE", probe="P-OVERLAPPING-CONTACT-WORK-CLOCK-1", status="NON-CANONICAL L1",
         checker_sha256=CHECKER_SHA256, continuous_evidence="PROOF.md")
    try:
        matrix_audit(audit)
        formal_suspension(audit)
        selector_audit(audit)
        finite_audit(audit)
        witness_audit(audit)
        emit("RESULT", status="PASS", checks=audit.checks, falsifiers=0,
             scope="exact finite snapshots and polynomial identities; universal flow requires proof")
    except (ScientificFailure, ArithmeticError) as error:
        emit("RESULT", status="F", checks=audit.checks, falsifiers=1,
             error_type=type(error).__name__, detail=str(error))


if __name__ == "__main__":
    main()
