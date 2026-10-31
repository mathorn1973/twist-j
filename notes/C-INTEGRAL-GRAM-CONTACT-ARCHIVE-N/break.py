#!/usr/bin/env python3
"""Independent finite breaker for C-INTEGRAL-GRAM-CONTACT-ARCHIVE-N.

Author: A. M. Thorn <thorn@twistj.com>
SPDX-License-Identifier: Apache-2.0

Scientific input: the frozen adjacent PREREG.md only.  This implementation
uses general polynomial convolution/reduction, not a fixed multiplication
table.  Record contacts use the integer sandwich B G B^dagger / 4, B=2A,
without a state representative or a call to the raw contact.

PREPARATION ONLY until both implementations have been publicly frozen and
read back.  Syntax compilation is not scientific execution or a PASS.
The finite audit cannot establish the universal claims or a public gate.

Conventions resolving otherwise unspecified details of the preregistration:
* Unqualified C and the pair certificate mean exponent +1.  F2 additionally
  checks exponent -1 independently and checks both inverse compositions.
* J=1+rho; derive its inverse by exact rational elimination, then verify that
  its coefficients are integral and that both products equal 1.
* Control 2 normalizes G by its Hermitian trace h.  For its stated fixtures h
  is a positive rational integer, so coefficientwise Fraction suffices.
* Count zero VALID boundary occurrences and distinct cases separately.
* Old memory is checked at ticks 4..8, covering both the first-output archive
  window and the reader window 6,7,8.
* F7 checks both inverse compositions at every transition.

No floating point, random inputs, third-party packages, or network calls.
Failures are accumulated; every group and every negative control is tried.
Exceptions and failed exact divisions are integrity failures.  Other failed
checks retain an exact first witness per assertion, plus occurrence counts;
they still require integrity review before scientific interpretation.
"""

from __future__ import annotations

from collections import Counter
from contextlib import contextmanager
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


PREREG_SHA256 = "067115f7b1df57cf8475eceb3bbca7d4eb2b97ec940b6a2fe4798c5b520074a2"
SOURCE_COMMIT = "c6e7eaef4741d7ec36bfb2e96d0e5831ea9295be"


@dataclass(frozen=True, slots=True)
class Poly:
    """An integer polynomial modulo Phi_5, stored with trailing zeros removed."""

    p: tuple[int, ...] = ()

    def __post_init__(self):
        work = list(self.p)
        if any(type(c) is not int for c in work):
            raise TypeError("Poly requires literal integer coefficients")
        # General monic polynomial division by 1+X+X^2+X^3+X^4.
        while len(work) > 4:
            leading = work[-1]
            shift = len(work) - 5
            for k in range(5):
                work[shift + k] -= leading
            work.pop()
        while work and work[-1] == 0:
            work.pop()
        object.__setattr__(self, "p", tuple(work))

    def coefficients(self):
        return self.p + (0,) * (4 - len(self.p))

    @staticmethod
    def coerce(value):
        if isinstance(value, Poly):
            return value
        if type(value) is int:
            return Poly((value,))
        raise TypeError("expected Poly or literal int")

    def __add__(self, other):
        other = self.coerce(other)
        size = max(len(self.p), len(other.p))
        result = [0] * size
        for k, value in enumerate(self.p):
            result[k] += value
        for k, value in enumerate(other.p):
            result[k] += value
        return Poly(tuple(result))

    __radd__ = __add__

    def __neg__(self):
        return Poly(tuple(-c for c in self.p))

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        if not self.p or not other.p:
            return Poly()
        result = [0] * (len(self.p) + len(other.p) - 1)
        for left_degree, left in enumerate(self.p):
            for right_degree, right in enumerate(other.p):
                result[left_degree + right_degree] += left * right
        return Poly(tuple(result))

    __rmul__ = __mul__

    def __pow__(self, exponent):
        if type(exponent) is not int or exponent < 0:
            raise ValueError("only nonnegative integer powers are supported")
        answer, base = Poly((1,)), self
        while exponent:
            if exponent & 1:
                answer = answer * base
            base = base * base
            exponent //= 2
        return answer

    def substitute_power(self, exponent):
        if type(exponent) is not int or exponent < 1:
            raise ValueError("substitution power must be a positive integer")
        if not self.p:
            return Poly()
        result = [0] * (exponent * (len(self.p) - 1) + 1)
        for degree, value in enumerate(self.p):
            result[degree * exponent] += value
        return Poly(tuple(result))

    def bar(self):
        return self.substitute_power(4)

    def mod(self, modulus):
        if type(modulus) is not int or modulus < 1:
            raise ValueError("modulus must be a positive integer")
        return Poly(tuple(c % modulus for c in self.p))

    def divisible(self, divisor):
        return all(c % divisor == 0 for c in self.p)

    def exact_div(self, divisor):
        if type(divisor) is not int or divisor == 0:
            raise ValueError("divisor must be a nonzero integer")
        quotients = []
        for degree, coefficient in enumerate(self.coefficients()):
            quotient, remainder = divmod(coefficient, divisor)
            if remainder != 0:
                raise ArithmeticError(
                    "nonintegral division: coefficients="
                    + repr(self.coefficients())
                    + ", divisor=" + str(divisor)
                    + ", degree=" + str(degree)
                    + ", remainder=" + str(remainder)
                )
            quotients.append(quotient)
        return Poly(tuple(quotients))


ZERO = Poly()
ONE = Poly((1,))
JROOT = Poly((0, 1))
RHO = JROOT ** 2
RHO_INVERSE = RHO.bar()
WINDOW = frozenset((6, 7, 8))
ARCHIVE = (5, 6, 4)


def q(value):
    coeffs = value.coefficients()
    numerator = 5 * sum(c * c for c in coeffs) - sum(coeffs) ** 2
    quotient, remainder = divmod(numerator, 2)
    if remainder:
        raise ArithmeticError("q numerator is not even")
    return quotient


def norm(value):
    return value * value.bar()


def invariants(state):
    return (
        sum(state, ZERO),
        sum((norm(value) for value in state), ZERO),
        sum(q(value) for value in state),
    )


def gram(state):
    conjugates = tuple(value.bar() for value in state)
    return tuple(tuple(left * right for right in conjugates) for left in state)


def difference_norm(record, i, j):
    return record[i][i] + record[j][j] - record[i][j] - record[j][i]


def raw_contact(state, i, j, exponent=1):
    if exponent not in (1, -1) or i == j:
        raise ValueError("invalid contact")
    difference = state[i] - state[j]
    admitted = difference.divisible(2)
    if not admitted:
        return state, False
    mean = (state[i] + state[j]).exact_div(2)
    half_difference = difference.exact_div(2)
    rotated = (RHO if exponent == 1 else RHO_INVERSE) * half_difference
    result = list(state)
    result[i], result[j] = mean + rotated, mean - rotated
    return tuple(result), True


def record_contact(record, i, j, exponent, audit):
    """Apply the specified record operation using B G B^dagger / 4."""
    if exponent not in (1, -1) or i == j:
        raise ValueError("invalid record contact")
    admitted = difference_norm(record, i, j).divisible(2)
    if not admitted:
        return record, False
    size = len(record)
    rotation = RHO if exponent == 1 else RHO_INVERSE
    # Sparse integer rows of B=2I+(rotation-1)vv^T, v=e_i-e_j.
    rows = [((k, 2 * ONE),) for k in range(size)]
    rows[i] = ((i, ONE + rotation), (j, ONE - rotation))
    rows[j] = ((i, ONE - rotation), (j, ONE + rotation))
    conjugate_rows = [tuple((k, value.bar()) for k, value in row) for row in rows]
    result = []
    for left in range(size):
        output_row = []
        for right in range(size):
            numerator = ZERO
            for source_row, left_coefficient in rows[left]:
                for source_column, right_coefficient in conjugate_rows[right]:
                    numerator += (
                        left_coefficient * record[source_row][source_column]
                        * right_coefficient
                    )
            audit.stats["matrix_entry_divisions"] += 1
            audit.stats["matrix_coefficient_divisions"] += 4
            # Raises an integrity failure rather than rounding or truncating.
            output_row.append(numerator.exact_div(4))
        result.append(tuple(output_row))
    return tuple(result), True


# Every data gate follows the given fourteen-row table literally.
GATES = (
    ("swap", 4, 5, 0),
    ("swap", 4, 2, 0),
    ("contact", 0, 4, 1),
    ("swap", 4, 6, 0),
    ("swap", 4, 3, 0),
    ("contact", 1, 4, 1),
    ("hold", 0, 0, 0),
    ("hold", 0, 0, 0),
    ("contact", 1, 4, -1),
    ("swap", 4, 3, 0),
    ("swap", 4, 6, 0),
    ("contact", 0, 4, -1),
    ("swap", 4, 2, 0),
    ("swap", 4, 5, 0),
)


def raw_gate(state, gate_index, inverse=False):
    kind, i, j, exponent = GATES[gate_index]
    if kind == "hold":
        return state
    if kind == "swap":
        result = list(state)
        result[i], result[j] = result[j], result[i]
        return tuple(result)
    return raw_contact(state, i, j, -exponent if inverse else exponent)[0]


def record_gate(record, gate_index, audit, inverse=False):
    kind, i, j, exponent = GATES[gate_index]
    if kind == "hold":
        return record
    if kind == "swap":
        permutation = list(range(len(record)))
        permutation[i], permutation[j] = permutation[j], permutation[i]
        return tuple(
            tuple(record[permutation[r]][permutation[c]] for c in range(len(record)))
            for r in range(len(record))
        )
    return record_contact(
        record, i, j, -exponent if inverse else exponent, audit
    )[0]


def raw_tick(complete_state, backward=False):
    clock, state = complete_state
    gate_index = (clock - 1) % 14 if backward else clock
    result = raw_gate(state, gate_index, inverse=backward)
    return ((clock - 1) % 14 if backward else (clock + 1) % 14), result


def record_tick(complete_record, audit, backward=False):
    clock, record = complete_record
    gate_index = (clock - 1) % 14 if backward else clock
    result = record_gate(record, gate_index, audit, inverse=backward)
    return ((clock - 1) % 14 if backward else (clock + 1) % 14), result


def reader(complete_record):
    clock, record = complete_record
    if clock not in WINDOW:
        return "NOT_IN_WINDOW", None
    return "VALID", tuple(tuple(record[i][j] for j in ARCHIVE) for i in ARCHIVE)


def json_value(value):
    if isinstance(value, Poly):
        return list(value.coefficients())
    if isinstance(value, Fraction):
        return {"numerator": value.numerator, "denominator": value.denominator}
    if isinstance(value, dict):
        return {str(k): json_value(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [json_value(v) for v in value]
    return value


class Audit:
    def __init__(self, name):
        self.name = name
        self.stats = Counter()
        self.failures = {}
        self.context = {}

    def fail(self, label, actual, expected, integrity=False):
        self.stats["failed_checks"] += 1
        if integrity:
            self.stats["integrity_failures"] += 1
        key = (label, integrity)
        if key in self.failures:
            self.failures[key]["occurrences"] += 1
        else:
            self.failures[key] = {
                "assertion": label,
                "kind": "INTEGRITY" if integrity else "CHECK",
                "occurrences": 1,
                "first_context": json_value(self.context),
                "actual": json_value(actual),
                "expected": json_value(expected),
            }

    def eq(self, label, actual, expected):
        self.stats["checks"] += 1
        if actual != expected:
            self.fail(label, actual, expected)

    def check(self, label, condition, witness=None):
        self.stats["checks"] += 1
        if not condition:
            self.fail(label, witness if witness is not None else condition, True)

    @contextmanager
    def case(self, **context):
        previous = self.context
        self.context = dict(previous, **context)
        try:
            yield
        except Exception as error:
            self.fail(
                "exception", {"type": type(error).__name__, "message": str(error)},
                "no exception", integrity=True,
            )
        finally:
            self.context = previous

    def report(self):
        status = "FAILED" if self.failures else "OK"
        print(self.name + " " + json.dumps(
            {"status": status, **dict(sorted(self.stats.items()))}, sort_keys=True
        ))
        for failure in self.failures.values():
            print(self.name + ".FAIL " + json.dumps(failure, sort_keys=True))


class Certificate:
    def __init__(self):
        self.digest = sha256()
        self.lines = 0
        self.prefix_counts = Counter()

    def append(self, prefix, integers, required_fields):
        values = tuple(integers)
        if len(values) != required_fields or any(type(v) is not int for v in values):
            raise ArithmeticError("certificate field count or integer type mismatch")
        line = prefix + ",".join(str(value) for value in values) + "\n"
        self.digest.update(line.encode("utf-8"))
        self.lines += 1
        self.prefix_counts[prefix] += 1

    def pair(self, state, output, admitted, energy):
        self.append("", (
            *state[0].coefficients(), *state[1].coefficients(),
            *output[0].coefficients(), *output[1].coefficients(),
            int(admitted), energy,
        ), 18)

    def program(self, prefix, case_index, boundary, clock, state, energy):
        flat = tuple(c for value in state for c in value.coefficients())
        self.append(prefix, (case_index, boundary, clock, *flat, energy), 32)


def residue_power(value, exponent):
    result = ONE
    for _ in range(exponent):
        result = (result * value).mod(2)
    return result


def rational_inverse_coefficients(value):
    """Solve the general four-dimensional multiplication system over Q."""
    columns = [(value * (JROOT ** k)).coefficients() for k in range(4)]
    rows = [
        [Fraction(columns[column][row]) for column in range(4)]
        + [Fraction(int(row == 0))]
        for row in range(4)
    ]
    for column in range(4):
        pivot = next((r for r in range(column, 4) if rows[r][column] != 0), None)
        if pivot is None:
            raise ArithmeticError("singular multiplication system")
        rows[column], rows[pivot] = rows[pivot], rows[column]
        divisor = rows[column][column]
        rows[column] = [entry / divisor for entry in rows[column]]
        for row in range(4):
            if row != column:
                multiplier = rows[row][column]
                rows[row] = [
                    rows[row][k] - multiplier * rows[column][k] for k in range(5)
                ]
    return tuple(rows[row][4] for row in range(4))


def audit_f1(audit):
    nonzero_trace_zeros = 0
    for coefficients in product((0, 1), repeat=4):
        audit.stats["residues"] += 1
        with audit.case(coefficients=coefficients):
            value = Poly(coefficients)
            conjugate = value.bar().mod(2)
            residue_norm = (value * conjugate).mod(2)
            audit.eq("A.conjugation_frobenius4", conjugate, residue_power(value, 4))
            audit.eq("A.norm_fifth_power", residue_norm, residue_power(value, 5))
            audit.eq("A.norm_zero_iff_zero", residue_norm == ZERO, value == ZERO)
            audit.eq("A.norm_fixed", residue_norm.bar().mod(2), residue_norm)
            finite_trace = (residue_norm + residue_norm * residue_norm).mod(2)
            audit.check("A.trace_in_F2", finite_trace in (ZERO, ONE), finite_trace)
            audit.eq("A.q_trace_parity", Poly((q(value) % 2,)), finite_trace)
            integer_norm = norm(value)
            raw_trace = sum((integer_norm.substitute_power(k) for k in range(1, 5)), ZERO)
            audit.eq("A.integer_trace_is_twice_q", raw_trace, 2 * q(value) * ONE)
            if value != ZERO and q(value) % 2 == 0:
                nonzero_trace_zeros += 1
    audit.eq("F1.residue_count", audit.stats["residues"], 16)
    audit.eq("A.five_nonzero_trace_zeros", nonzero_trace_zeros, 5)
    audit.stats["nonzero_trace_zeros"] = nonzero_trace_zeros
    with audit.case(component="J inverse and rho order"):
        J = ONE + RHO
        inverse_coefficients = rational_inverse_coefficients(J)
        integral = all(value.denominator == 1 for value in inverse_coefficients)
        audit.check("F1.J_inverse_integral", integral, inverse_coefficients)
        if integral:
            inverse = Poly(tuple(value.numerator for value in inverse_coefficients))
            audit.eq("F1.J_left_inverse", inverse * J, ONE)
            audit.eq("F1.J_right_inverse", J * inverse, ONE)
        audit.eq("F1.rho_relation", J - ONE, RHO)
        audit.eq("F1.rho_fifth_power", RHO ** 5, ONE)
        for exponent in range(1, 5):
            audit.check("F1.rho_exact_order", RHO ** exponent != ONE, exponent)
        audit.eq("F1.rho_inverse", RHO * RHO_INVERSE, ONE)


def audit_f2(audit, certificate):
    box = tuple(Poly(coefficients) for coefficients in product((-1, 0, 1), repeat=4))
    for case_index, (x, y) in enumerate(product(box, repeat=2)):
        audit.stats["pairs"] += 1
        with audit.case(case_index=case_index, x=x, y=y):
            state = (x, y)
            before = invariants(state)
            record = gram(state)
            admitted = (x - y).divisible(2)
            audit.stats["admitted_pairs" if admitted else "refused_pairs"] += 1
            delta = difference_norm(record, 0, 1)
            audit.eq("A.Gram_difference_norm", delta, norm(x - y))
            audit.eq("A.admission_mod2", admitted, delta.divisible(2))
            audit.eq("A.admission_mod4", admitted, delta.divisible(4))
            positive, positive_admission = raw_contact(state, 0, 1, 1)
            certificate.pair(state, positive, positive_admission, before[2])
            for exponent in (1, -1):
                with audit.case(exponent=exponent):
                    output, raw_admission = (
                        (positive, positive_admission) if exponent == 1
                        else raw_contact(state, 0, 1, exponent)
                    )
                    continued, record_admission = record_contact(record, 0, 1, exponent, audit)
                    audit.eq("B.raw_admission", raw_admission, admitted)
                    audit.eq("B.record_admission", record_admission, admitted)
                    audit.eq("B.sum_h_E", invariants(output), before)
                    audit.eq("B.Gram_continuation", continued, gram(output))
                    restored, inverse_admission = raw_contact(output, 0, 1, -exponent)
                    restored_record, inverse_record_admission = record_contact(
                        continued, 0, 1, -exponent, audit
                    )
                    audit.eq("B.raw_inverse", restored, state)
                    audit.eq("B.record_inverse", restored_record, record)
                    audit.eq("B.inverse_raw_admission", inverse_admission, admitted)
                    audit.eq("B.inverse_record_admission", inverse_record_admission, admitted)
                    if not admitted:
                        audit.eq("B.refused_raw_identity", output, state)
                        audit.eq("B.refused_record_identity", continued, record)
                    fifth, fifth_record = output, continued
                    for _ in range(4):
                        fifth = raw_contact(fifth, 0, 1, exponent)[0]
                        fifth_record = record_contact(fifth_record, 0, 1, exponent, audit)[0]
                    audit.eq("B.raw_fifth_power", fifth, state)
                    audit.eq("B.record_fifth_power", fifth_record, record)
    audit.eq("F2.pair_count", audit.stats["pairs"], 6561)
    audit.eq("F2.certificate_lines", certificate.lines, 6561)


def normalized_gram_with_integer_trace(state):
    record = gram(state)
    h = sum((record[k][k] for k in range(len(state))), ZERO)
    coefficients = h.coefficients()
    if coefficients[1:] != (0, 0, 0) or coefficients[0] <= 0:
        raise ArithmeticError("normalization control needs positive integer h")
    return tuple(
        tuple(tuple(Fraction(c, coefficients[0]) for c in entry.coefficients()) for entry in row)
        for row in record
    )


def control_binary_trace(audit):
    state = (ONE, ZERO)
    audit.eq("control1.q", q(ONE), 2)
    audit.eq("control1.trace_even", q(ONE) % 2, 0)
    audit.eq("control1.raw_admission", ONE.divisible(2), False)
    audit.eq("control1.full_norm_admission", norm(ONE).divisible(2), False)
    output, admitted = raw_contact(state, 0, 1)
    audit.eq("control1.refused", admitted, False)
    audit.eq("control1.identity", output, state)
    continued, record_admission = record_contact(gram(state), 0, 1, 1, audit)
    audit.eq("control1.record_refused", record_admission, False)
    audit.eq("control1.record_identity", continued, gram(state))


def control_normalization(audit):
    first, second = (ONE, ZERO), (2 * ONE, ZERO)
    audit.eq("control2.normalized_Grams", normalized_gram_with_integer_trace(first),
             normalized_gram_with_integer_trace(second))
    audit.eq("control2.receiver_accounts", tuple(q(raw_contact(s, 0, 1)[0][1])
             for s in (first, second)), (0, 5))


def control_phase(audit):
    states = ((2 * ONE, 2 * RHO), (2 * ONE, 2 * RHO_INVERSE))
    outputs = []
    for index, state in enumerate(states):
        record = gram(state)
        audit.eq("control3.input_diagonal", (record[0][0], record[1][1]),
                 (4 * ONE, 4 * ONE))
        output, admitted = raw_contact(state, 0, 1)
        outputs.append(output)
        audit.eq("control3.admitted", admitted, True)
        audit.eq("control3.input_E", invariants(state)[2], 16)
        audit.eq("control3.output_E", invariants(output)[2], 16)
        audit.eq("control3.full_invariants", invariants(output), invariants(state))
    audit.eq("control3.receiver_accounts", tuple(q(s[1]) for s in outputs), (3, 13))
    audit.eq("control3.source_accounts", tuple(q(s[0]) for s in outputs), (13, 3))


def control_outside_map(audit):
    first, second = (ONE, ONE), (JROOT, JROOT)
    audit.eq("control4.input_Grams", gram(first), gram(second))
    transformed = tuple((s[1], s[0].bar()) for s in (first, second))
    records = tuple(gram(s) for s in transformed)
    audit.eq("control4.off_diagonal", (records[0][0][1], records[1][0][1]), (ONE, RHO))
    audit.check("control4.non_descent", records[0] != records[1], records)


def control_reference_extension(audit):
    states = ((2 * ONE,), (2 * RHO,))
    audit.eq("control5.single_slot_first", gram(states[0]), ((4 * ONE,),))
    audit.eq("control5.single_slot_second", gram(states[1]), ((4 * ONE,),))
    outputs = tuple(raw_contact(s + (2 * ONE,), 0, 1)[0] for s in states)
    audit.eq("control5.receiver_accounts", tuple(q(s[1]) for s in outputs), (8, 13))


def audit_f3(audit):
    controls = (
        control_binary_trace, control_normalization, control_phase,
        control_outside_map, control_reference_extension,
    )
    for control_index, control in enumerate(controls, 1):
        audit.stats["controls_attempted"] += 1
        with audit.case(control=control_index):
            control(audit)
            audit.stats["controls_completed"] += 1
    audit.eq("F3.control_count", audit.stats["controls_attempted"], 5)
    audit.eq("F3.completed_control_count", audit.stats["controls_completed"], 5)


def polynomial_evaluation_mod(value, point, modulus):
    answer = 0
    for coefficient in reversed(value.p):
        answer = (answer * point + coefficient) % modulus
    return answer


def audit_f4(audit):
    a = 2 * ONE + JROOT
    abar = 2 * ONE + JROOT.bar()
    with audit.case(component="nonintegral fibre ratio witness"):
        audit.eq("F4.conjugate", abar, a.bar())
        audit.eq("F4.Phi5_at_minus2_mod11", sum((-2) ** k for k in range(5)) % 11, 0)
        audit.eq("F4.a_maps_to_zero", polynomial_evaluation_mod(a, -2, 11), 0)
        audit.check("F4.abar_maps_to_nonzero", polynomial_evaluation_mod(abar, -2, 11) != 0,
                    polynomial_evaluation_mod(abar, -2, 11))
    words = (
        (ONE, 2 * ONE, 3 * ONE, JROOT, ONE + JROOT, ZERO, RHO),
        (ZERO, ONE, 2 * ONE, ZERO, JROOT, ONE - JROOT, RHO_INVERSE),
        (ONE, ONE, ONE, ONE, ONE, ONE, ONE),
    )
    for word_index, word in enumerate(words):
        for initial_clock in range(14):
            audit.stats["paired_cycles"] += 1
            with audit.case(word_index=word_index, initial_clock=initial_clock):
                first = (initial_clock, tuple(a * value for value in word))
                second = (initial_clock, tuple(abar * value for value in word))
                for boundary in range(15):
                    audit.context["boundary"] = boundary
                    audit.stats["paired_boundaries"] += 1
                    audit.eq("C.fibre_clocks", first[0], second[0])
                    audit.eq("C.fibre_Gram_records", gram(first[1]), gram(second[1]))
                    if boundary < 14:
                        first, second = raw_tick(first), raw_tick(second)
    audit.eq("F4.paired_cycle_count", audit.stats["paired_cycles"], 42)
    audit.eq("F4.paired_boundary_count", audit.stats["paired_boundaries"], 630)


def check_boundary(audit, complete_state, complete_record, initial_invariants):
    clock, state = complete_state
    record_clock, record = complete_record
    actual_record = gram(state)
    audit.eq("C.record_clock", record_clock, clock)
    audit.eq("C.all_step_Gram", record, actual_record)
    current_invariants = invariants(state)
    audit.eq("B.full_S_h_E", current_invariants, initial_invariants)
    audit.eq("B.Gram_trace_h", sum((record[k][k] for k in range(len(state))), ZERO),
             current_invariants[1])
    reading = reader(complete_record)
    expected_reading = (
        ("VALID", tuple(tuple(actual_record[i][j] for j in ARCHIVE) for i in ARCHIVE))
        if clock in WINDOW else ("NOT_IN_WINDOW", None)
    )
    audit.eq("D.record_only_reader", reading, expected_reading)
    is_zero_valid = (
        reading[0] == "VALID" and reading[1] is not None
        and all(entry == ZERO for row in reading[1] for entry in row)
    )
    if clock in WINDOW:
        audit.stats["valid_boundaries"] += 1
    if is_zero_valid:
        audit.stats["zero_valid_boundaries"] += 1
        audit.eq("D.zero_is_still_VALID", reading[0], "VALID")
    return current_invariants[2], reading, is_zero_valid


def audit_f5(audit, certificate):
    U = (ZERO, ONE, -ONE, JROOT)
    V = (ZERO, ONE, RHO, RHO_INVERSE)
    M = (ZERO, ONE, JROOT, ONE + JROOT, 2 * ONE - JROOT)
    cases_with_zero_valid = set()
    audit.stats["zero_valid_boundaries"] = 0
    # product makes m vary fastest, with the exact outer-to-inner order below.
    for case_index, (u1, u2, v1, v2, memory) in enumerate(product(U, U, V, V, M)):
        audit.stats["prepared_cases"] += 1
        with audit.case(case_index=case_index, inputs=(u1, u2, v1, v2, memory)):
            initial = (0, (2 * u1, 2 * u2, 2 * v1, 2 * v2, memory, ZERO, ZERO))
            complete = initial
            recorded = (0, gram(initial[1]))
            initial_invariants = invariants(initial[1])
            expected_energy = 4 * sum(q(value) for value in (u1, u2, v1, v2)) + q(memory)
            audit.eq("D.prepared_energy", initial_invariants[2], expected_energy)
            a1 = (ONE + RHO) * u1 + (ONE - RHO) * v1
            b1 = (ONE - RHO) * u1 + (ONE + RHO) * v1
            a2 = (ONE + RHO) * u2 + (ONE - RHO) * v2
            b2 = (ONE - RHO) * u2 + (ONE + RHO) * v2
            endpoint = (a1, a2, ZERO, ZERO, b2, memory, b1)
            archive_record = gram((memory, b1, b2))
            if all(value == ZERO for value in initial[1]):
                audit.stats["all_zero_inputs"] += 1
            for boundary in range(15):
                audit.context["boundary"] = boundary
                audit.stats["boundaries"] += 1
                energy, reading, zero_valid = check_boundary(
                    audit, complete, recorded, initial_invariants
                )
                clock, state = complete
                certificate.program("P|", case_index, boundary, clock, state, energy)
                audit.eq("D.prepared_clock", clock, boundary % 14)
                if boundary in WINDOW:
                    audit.eq("D.complete_endpoint", state, endpoint)
                    audit.eq("D.archive_reader_order", reading, ("VALID", archive_record))
                if boundary == 3:
                    audit.eq("D.first_output_receiver", state[4], b1)
                if 4 <= boundary <= 8:
                    audit.eq("D.first_output_archive", state[6], b1)
                    audit.eq("D.old_memory", state[5], memory)
                if zero_valid:
                    cases_with_zero_valid.add(case_index)
                if boundary < 14:
                    complete = raw_tick(complete)
                    recorded = record_tick(recorded, audit)
            audit.eq("D.prepared_full_return", complete, initial)
            audit.eq("D.prepared_record_return", recorded, (0, gram(initial[1])))
    audit.stats["zero_valid_cases"] = len(cases_with_zero_valid)
    audit.eq("F5.case_count", audit.stats["prepared_cases"], 1280)
    audit.eq("F5.boundary_count", audit.stats["boundaries"], 1280 * 15)
    audit.eq("F5.all_zero_input_included", audit.stats["all_zero_inputs"], 1)
    audit.eq("F5.valid_boundary_count", audit.stats["valid_boundaries"], 1280 * 3)
    audit.eq("F5.certificate_lines", certificate.prefix_counts["P|"], 1280 * 15)


def audit_f6(audit, certificate):
    alphabets = ((ONE, ONE + 2 * JROOT), (ONE, 2 * RHO))
    cases_with_zero_valid = set()
    audit.stats["zero_valid_boundaries"] = 0
    case_index = 0
    for alphabet_index, alphabet in enumerate(alphabets):
        for bits in product((0, 1), repeat=7):
            audit.stats["occupied_cases"] += 1
            with audit.case(case_index=case_index, alphabet=alphabet_index, bits=bits):
                state = tuple(alphabet[bit] for bit in bits)
                audit.check("F6.every_initial_slot_occupied", all(value != ZERO for value in state), state)
                initial = (0, state)
                complete, recorded = initial, (0, gram(state))
                initial_invariants = invariants(state)
                for boundary in range(15):
                    audit.context["boundary"] = boundary
                    audit.stats["boundaries"] += 1
                    energy, _, zero_valid = check_boundary(
                        audit, complete, recorded, initial_invariants
                    )
                    certificate.program("O|", case_index, boundary, complete[0], complete[1], energy)
                    audit.eq("D.occupied_clock", complete[0], boundary % 14)
                    if zero_valid:
                        cases_with_zero_valid.add(case_index)
                    if boundary < 14:
                        complete = raw_tick(complete)
                        recorded = record_tick(recorded, audit)
                audit.eq("D.occupied_full_return", complete, initial)
                audit.eq("D.occupied_record_return", recorded, (0, gram(state)))
            case_index += 1
    audit.stats["zero_valid_cases"] = len(cases_with_zero_valid)
    audit.eq("F6.case_count", audit.stats["occupied_cases"], 256)
    audit.eq("F6.boundary_count", audit.stats["boundaries"], 256 * 15)
    audit.eq("F6.valid_boundary_count", audit.stats["valid_boundaries"], 256 * 3)
    audit.eq("F6.certificate_lines", certificate.prefix_counts["O|"], 256 * 15)


def audit_f7(audit):
    state = tuple(ONE + 2 * (JROOT ** k) for k in range(7))
    for initial_clock in range(14):
        audit.stats["complete_cycles"] += 1
        with audit.case(initial_clock=initial_clock):
            initial = (initial_clock, state)
            initial_record = (initial_clock, gram(state))
            complete, recorded = initial, initial_record
            initial_invariants = invariants(state)
            for boundary in range(15):
                audit.context["boundary"] = boundary
                audit.stats["boundaries"] += 1
                check_boundary(audit, complete, recorded, initial_invariants)
                audit.eq("F7.clock", complete[0], (initial_clock + boundary) % 14)
                if boundary == 14:
                    break
                following = raw_tick(complete)
                following_record = record_tick(recorded, audit)
                audit.eq("C.raw_backward_after_forward", raw_tick(following, backward=True), complete)
                audit.eq("C.record_backward_after_forward",
                         record_tick(following_record, audit, backward=True), recorded)
                preceding = raw_tick(complete, backward=True)
                preceding_record = record_tick(recorded, audit, backward=True)
                audit.eq("C.raw_forward_after_backward", raw_tick(preceding), complete)
                audit.eq("C.record_forward_after_backward", record_tick(preceding_record, audit), recorded)
                audit.eq("C.backward_Gram_continuation", preceding_record,
                         (preceding[0], gram(preceding[1])))
                audit.stats["inverse_transition_pairs"] += 1
                complete, recorded = following, following_record
            audit.eq("D.all_clock_full_return", complete, initial)
            audit.eq("D.all_clock_record_return", recorded, initial_record)
    audit.eq("F7.cycle_count", audit.stats["complete_cycles"], 14)
    audit.eq("F7.boundary_count", audit.stats["boundaries"], 14 * 15)
    audit.eq("F7.inverse_transition_count", audit.stats["inverse_transition_pairs"], 14 * 14)


def main():
    # Read local provenance before starting any finite scientific audit.  The
    # independent public source freeze/readback remains an external prerequisite.
    try:
        source_path = Path(__file__).resolve()
        source_hash = sha256(source_path.read_bytes()).hexdigest()
        prereg_hash = sha256(source_path.with_name("PREREG.md").read_bytes()).hexdigest()
    except Exception as error:
        print("INTEGRITY_FAILURE " + json.dumps({
            "stage": "provenance", "type": type(error).__name__, "message": str(error)
        }, sort_keys=True))
        return 2
    print("PROVENANCE " + json.dumps({
        "source_sha256": source_hash,
        "prereg_sha256": prereg_hash,
        "prereg_source_commit": SOURCE_COMMIT,
    }, sort_keys=True))
    if prereg_hash != PREREG_SHA256:
        print("INTEGRITY_FAILURE changed pinned preregistration; audit not started")
        return 2

    pair_certificate, program_certificate = Certificate(), Certificate()
    groups = (
        ("F1", lambda audit: audit_f1(audit)),
        ("F2", lambda audit: audit_f2(audit, pair_certificate)),
        ("F3", lambda audit: audit_f3(audit)),
        ("F4", lambda audit: audit_f4(audit)),
        ("F5", lambda audit: audit_f5(audit, program_certificate)),
        ("F6", lambda audit: audit_f6(audit, program_certificate)),
        ("F7", lambda audit: audit_f7(audit)),
    )
    failed = False
    for name, routine in groups:
        audit = Audit(name)
        with audit.case(group=name):
            routine(audit)
        audit.report()
        failed = failed or bool(audit.failures)

    certificate_audit = Audit("CERTIFICATES")
    certificate_audit.eq("pair_line_count", pair_certificate.lines, 6561)
    certificate_audit.eq("program_line_count", program_certificate.lines, (1280 + 256) * 15)
    certificate_audit.eq("prepared_line_count", program_certificate.prefix_counts["P|"], 1280 * 15)
    certificate_audit.eq("occupied_line_count", program_certificate.prefix_counts["O|"], 256 * 15)
    certificate_audit.report()
    failed = failed or bool(certificate_audit.failures)
    print("PAIR_SHA256 " + pair_certificate.digest.hexdigest())
    print("PROGRAM_SHA256 " + program_certificate.digest.hexdigest())
    print("CERTIFICATE_STATUS " + ("FAILED_AUDIT" if failed else "COMPLETE_FINITE_AUDIT"))
    print("RESULT " + ("FAILED_REQUIRES_INTEGRITY_REVIEW" if failed else "FINITE_AUDIT_OK_ONLY"))
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        exit_code = main()
    except Exception as error:
        # Do not silently drop later diagnostics into stderr or imply PASS.
        print("INTEGRITY_FAILURE " + json.dumps({
            "stage": "uncaught", "type": type(error).__name__, "message": str(error)
        }, sort_keys=True))
        exit_code = 2
    raise SystemExit(exit_code)
