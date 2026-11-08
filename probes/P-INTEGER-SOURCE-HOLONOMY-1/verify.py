#!/usr/bin/env python3
"""Exact author audit for P-INTEGER-SOURCE-HOLONOMY-1.

This entry point implements O using four polynomial coefficients.  Its only
independent-program interaction is a subprocess certificate from breaker.py.
Scientific failures complete with deterministic FAIL stdout and exit zero.
Operational errors are deliberately not caught as scientific failures.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import subprocess
import sys
from dataclasses import dataclass, replace
from fractions import Fraction
from functools import lru_cache
from pathlib import Path


PROBE = "P-INTEGER-SOURCE-HOLONOMY-1"
SCHEMA = PROBE + "/v1"

O = tuple[int, int, int, int]
H8 = tuple[int, int, int, int, int, int, int, int]
Matrix = tuple[tuple[O, O], tuple[O, O]]

ZERO: O = (0, 0, 0, 0)
ONE: O = (1, 0, 0, 0)
ROOT: O = (0, 1, 0, 0)
ZERO8: H8 = (0, 0, 0, 0, 0, 0, 0, 0)
D8: H8 = (0, 0, 1, 0, 0, 0, 0, 0)
I8: H8 = (1, 0, 1, 0, 0, 0, 0, 0)
J8: H8 = (1, 0, 1, 0, 0, 1, 0, 0)
IDENTITY: Matrix = ((ONE, ZERO), (ZERO, ONE))


class ScientificFailure(Exception):
    """A completed, labeled falsifier rather than an operational exception."""


def require(condition: bool, label: str) -> None:
    if not condition:
        raise ScientificFailure(label)


def integer(value: int) -> O:
    return (value, 0, 0, 0)


def add(left: O, right: O) -> O:
    return tuple(left[k] + right[k] for k in range(4))


def neg(value: O) -> O:
    return tuple(-entry for entry in value)


def sub(left: O, right: O) -> O:
    return add(left, neg(right))


def scale(value: O, factor: int) -> O:
    return tuple(factor * entry for entry in value)


def mul(left: O, right: O) -> O:
    coefficients = [0] * 7
    for i in range(4):
        for j in range(4):
            coefficients[i + j] += left[i] * right[j]
    # X^4 = -(1 + X + X^2 + X^3); reduce the highest power first.
    for power in range(6, 3, -1):
        coefficient = coefficients[power]
        coefficients[power] = 0
        for lower in range(power - 4, power):
            coefficients[lower] -= coefficient
    return tuple(coefficients[:4])


def power(value: O, exponent: int) -> O:
    if exponent < 0:
        raise ValueError("negative exponent outside polynomial power carrier")
    result = ONE
    for _ in range(exponent):
        result = mul(result, value)
    return result


def conjugate(value: O) -> O:
    a, b, c, d = value
    # bar(j) = j^4, bar(j^2) = j^3, bar(j^3) = j^2.
    return (a - b, -b, d - b, c - b)


def field_trace(value: O) -> int:
    return 4 * value[0] - value[1] - value[2] - value[3]


def galois(value: O, exponent: int) -> O:
    result = ZERO
    for degree, coefficient in enumerate(value):
        result = add(result, scale(power(ROOT, exponent * degree), coefficient))
    return result


def field_norm(value: O) -> O:
    result = ONE
    for exponent in (1, 2, 3, 4):
        result = mul(result, galois(value, exponent))
    return result


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            add(mul(left[i][0], right[0][j]), mul(left[i][1], right[1][j]))
            for j in range(2)
        )
        for i in range(2)
    )


def matproduct(*matrices: Matrix) -> Matrix:
    result = IDENTITY
    for matrix in matrices:
        result = matmul(result, matrix)
    return result


def adjoint(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(conjugate(matrix[j][i]) for j in range(2)) for i in range(2)
    )


def determinant(matrix: Matrix) -> O:
    return sub(mul(matrix[0][0], matrix[1][1]), mul(matrix[0][1], matrix[1][0]))


def matrix_trace(matrix: Matrix) -> O:
    return add(matrix[0][0], matrix[1][1])


def upper(value: O) -> Matrix:
    return ((ONE, value), (ZERO, ONE))


def lower(value: O) -> Matrix:
    return ((ONE, ZERO), (value, ONE))


def plus_element(a0: int, a1: int) -> O:
    return (a0, 0, -a1, -a1)


def plus_coordinates(value: O) -> tuple[int, int]:
    require(value[1] == 0 and value[2] == value[3], "O_PLUS_CLOSURE")
    return value[0], -value[2]


def hermitian_matrix(value: H8) -> Matrix:
    a = plus_element(value[0], value[1])
    d = plus_element(value[2], value[3])
    c = tuple(value[4:8])
    return ((a, c), (conjugate(c), d))


def hermitian_coordinates(matrix: Matrix) -> H8:
    require(matrix == adjoint(matrix), "HERMITIAN_CLOSURE")
    a0, a1 = plus_coordinates(matrix[0][0])
    d0, d1 = plus_coordinates(matrix[1][1])
    return (a0, a1, d0, d1, *matrix[0][1])


def h_add(left: H8, right: H8) -> H8:
    return tuple(left[k] + right[k] for k in range(8))


def h_sub(left: H8, right: H8) -> H8:
    return tuple(left[k] - right[k] for k in range(8))


def explicit_n(value: H8) -> int:
    a0, a1, d0, d1, *c = value
    return (
        4 * a0 * a0 + 4 * a0 * a1 + 6 * a1 * a1
        + 4 * d0 * d0 + 4 * d0 * d1 + 6 * d1 * d1
        + 10 * sum(entry * entry for entry in c) - 2 * sum(c) ** 2
    )


@dataclass(frozen=True)
class State:
    s: int
    q: int
    h: H8
    r: H8
    z: H8
    p: int
    bank: int
    epsilon: int


def pack(state: State) -> list[int]:
    return [
        state.s, state.q, state.p, state.bank, state.epsilon,
        *state.h, *state.r, *state.z,
    ]


def core(state: State) -> tuple:
    return state.s, state.q, state.h, state.r, state.z, state.p


def validate_state(state: State, label: str) -> None:
    require(all(type(entry) is int for entry in pack(state)), label + "_INTEGER")
    require(0 <= state.p < 6, label + "_PHASE")
    require(state.epsilon in (-1, 1), label + "_DIRECTION")
    require(state.bank >= 0, label + "_BANK")
    for name, value in (("H", state.h), ("R", state.r), ("Z", state.z)):
        require(len(value) == 8, label + "_" + name + "_ARITY")
        require(
            hermitian_coordinates(hermitian_matrix(value)) == value,
            label + "_" + name + "_INTEGRAL_HERMITIAN",
        )


class RowDigest:
    def __init__(self) -> None:
        self.count = 0
        self.digest = hashlib.sha256()

    def append(self, row: list) -> None:
        encoded = json.dumps(row, separators=(",", ":")) + "\n"
        self.digest.update(encoded.encode("utf-8"))
        self.count += 1

    def hexdigest(self) -> str:
        return self.digest.hexdigest()


class Engine:
    def __init__(self) -> None:
        j2 = mul(ROOT, ROOT)
        j3 = mul(j2, ROOT)
        self.phi = neg(add(j2, j3))
        self.j_value = add(ONE, j2)
        self.phi_inverse = sub(self.phi, ONE)
        self.j_inverse = neg(add(ROOT, j2))
        self.a = ((self.j_value, ZERO), (ZERO, self.phi))
        self.a_inverse = ((self.j_inverse, ZERO), (ZERO, self.phi_inverse))
        self.v = sub(mul(self.j_value, self.phi_inverse), ONE)
        self.w = mul(self.v, conjugate(self.v))

    def constants(self) -> dict:
        require(power(ROOT, 5) == ONE, "ROOT_ORDER_FIVE")
        require(mul(self.phi, self.phi_inverse) == ONE, "PHI_UNIT")
        require(mul(self.j_value, self.j_inverse) == ONE, "J_UNIT")
        require(matmul(self.a, self.a_inverse) == IDENTITY, "A_RIGHT_INVERSE")
        require(matmul(self.a_inverse, self.a) == IDENTITY, "A_LEFT_INVERSE")
        require(mul(self.phi, self.phi) == add(self.phi, ONE), "PHI_EQUATION")
        actual = {
            "phi": list(self.phi),
            "J": list(self.j_value),
            "v": list(self.v),
            "w": list(self.w),
            "trace_w": field_trace(self.w),
            "trace_w2": field_trace(mul(self.w, self.w)),
        }
        expected = {
            "phi": [0, 0, -1, -1],
            "J": [1, 0, 1, 0],
            "v": [-2, 1, -1, 0],
            "w": [9, 0, 5, 5],
            "trace_w": 26,
            "trace_w2": 294,
        }
        require(actual == expected, "CONSTANTS")
        return actual

    @lru_cache(maxsize=None)
    def n(self, value: H8) -> int:
        matrix = hermitian_matrix(value)
        return field_trace(matrix_trace(matmul(matrix, matrix)))

    def energy(self, state: State) -> int:
        source = state.s * state.s - state.s * state.q + state.q * state.q
        return 1 + source + self.n(state.h) + self.n(state.r) + self.n(state.z)

    def transport(self, matrix: Matrix, value: H8) -> H8:
        result = matproduct(matrix, hermitian_matrix(value), adjoint(matrix))
        return hermitian_coordinates(result)

    def bare(self, state: State, direction: int) -> State:
        if direction not in (-1, 1):
            raise ValueError("bare direction outside declared carrier")
        phase = state.p if direction == 1 else (state.p - 1) % 6
        output = state
        if phase == 0:
            if direction == 1:
                output = replace(state, s=state.s - state.q, q=state.s)
            else:
                output = replace(state, s=state.q, q=state.q - state.s)
        elif phase == 1:
            output = replace(
                state, h=self.transport(upper(integer(-direction * state.q)), state.h)
            )
        elif phase == 2:
            matrix = self.a_inverse if direction == 1 else self.a
            output = replace(state, h=self.transport(matrix, state.h))
        elif phase == 3:
            output = replace(
                state, h=self.transport(upper(integer(direction * state.q)), state.h)
            )
        elif phase == 4:
            matrix = self.a if direction == 1 else self.a_inverse
            output = replace(state, h=self.transport(matrix, state.h))
        elif phase == 5:
            difference = h_sub(state.h, state.r)
            detector = h_add(state.z, difference) if direction == 1 else h_sub(state.z, difference)
            output = replace(state, z=detector)
        else:
            raise ValueError("bare phase outside declared carrier")
        return replace(output, p=(state.p + direction) % 6)

    def funded(self, state: State, inverse: bool = False) -> State:
        direction = -state.epsilon if inverse else state.epsilon
        candidate = self.bare(state, direction)
        bank = state.bank + self.energy(state) - self.energy(candidate)
        if bank >= 0:
            return replace(candidate, bank=bank)
        return replace(state, epsilon=-state.epsilon)


def algebra_audit(engine: Engine) -> tuple[RowDigest, list[bool]]:
    gates = (
        engine.a, engine.a_inverse,
        upper(ONE), upper(neg(ONE)), lower(ONE), lower(neg(ONE)),
    )
    digest = RowDigest()
    for row_number, entries in enumerate(itertools.product((-1, 0, 1), repeat=8)):
        value = tuple(entries)
        label = f"TRANSPORT_ROW_{row_number}"
        actual_n = engine.n(value)
        require(actual_n == explicit_n(value), label + "_N_FORMULA")
        require(actual_n >= 2 * sum(entry * entry for entry in value), label + "_N_BOUND")
        source_det = determinant(hermitian_matrix(value))
        outputs = []
        for gate_number, gate in enumerate(gates):
            output = engine.transport(gate, value)
            require(
                determinant(hermitian_matrix(output)) == source_det,
                label + f"_DETERMINANT_{gate_number}",
            )
            outputs.append(list(output))
        digest.append([list(value), outputs])
    require(digest.count == 6561, "TRANSPORT_ROW_COUNT")

    bad = ((engine.j_value, ZERO), (ZERO, ONE))
    bad_action = engine.transport(bad, I8)
    control_1 = (
        field_norm(determinant(bad)) == ONE
        and determinant(hermitian_matrix(bad_action)) != determinant(hermitian_matrix(I8))
    )

    central = ((ROOT, ZERO), (ZERO, ROOT))
    basis = tuple(tuple(int(k == coordinate) for k in range(8)) for coordinate in range(8))
    control_2 = central != IDENTITY and all(
        engine.transport(central, value) == value for value in basis
    )

    commutator = matproduct(engine.a, upper(ONE), engine.a_inverse, upper(neg(ONE)))
    require(commutator == upper(engine.v), "COMMUTATOR_C1_FORMULA")
    control_3 = (
        matrix_trace(commutator) == matrix_trace(IDENTITY) == integer(2)
        and engine.transport(commutator, I8) != I8
    )

    m10 = engine.a
    m21 = matmul(upper(ONE), engine.a_inverse)
    m02 = upper(neg(ONE))
    control_4 = matproduct(m02, m21, m10) == IDENTITY
    controls = [control_1, control_2, control_3, control_4]
    for index, result in enumerate(controls, start=1):
        require(result, f"NEGATIVE_CONTROL_{index}")
    return digest, controls


def step_audit(engine: Engine) -> RowDigest:
    fixtures = (
        (D8, D8, J8),
        (I8, D8, (0, 1, 1, -1, 1, 1, -1, 0)),
        ((1, -1, -1, 1, 1, 0, -1, 1), I8, (-1, 0, -1, 0, 0, -1, 0, 0)),
        (ZERO8, ZERO8, ZERO8),
    )
    digest = RowDigest()
    inputs = itertools.product(
        (-1, 0, 1), (-1, 0, 1), range(6), (-1, 1),
        (0, 1, 12, 32, 116, 346, 715, 716, 771, 772), fixtures,
    )
    for row_number, (s, q, phase, epsilon, bank, fixture) in enumerate(inputs):
        h, r, z = fixture
        state = State(s, q, h, r, z, phase, bank, epsilon)
        forward = engine.funded(state)
        backward = engine.funded(state, inverse=True)
        label = f"STEP_ROW_{row_number}"
        require(engine.funded(forward, inverse=True) == state, label + "_INVERSE_FORWARD")
        require(engine.funded(backward) == state, label + "_FORWARD_INVERSE")
        total = engine.energy(state) + state.bank
        for suffix, output in (("INPUT", state), ("FORWARD", forward), ("BACKWARD", backward)):
            validate_state(output, label + "_" + suffix)
            require(engine.energy(output) + output.bank == total, label + "_" + suffix + "_ENERGY")
            require(output.r == state.r, label + "_" + suffix + "_REFERENCE")
        digest.append([pack(state), pack(forward), pack(backward)])
    require(digest.count == 4320, "STEP_ROW_COUNT")
    return digest


def experiment_audit(engine: Engine) -> tuple[RowDigest, list, list, list]:
    digest = RowDigest()
    prefix_costs = []
    increments = []
    budgets = []
    for a in (-1, 1):
        initial = State(a, 0, D8, D8, J8, 0, 0, 1)
        bare_history = [initial]
        for _ in range(6):
            bare_history.append(engine.bare(bare_history[-1], 1))
        costs = [engine.energy(state) for state in bare_history]
        predicted_costs = [26, 26, 38, 58, 142, 372, 742 if a == -1 else 798]
        require(costs == predicted_costs, f"EXPERIMENT_{a}_PREFIX_COSTS")
        prefix_costs.append([a, costs])
        budget = max(costs) - costs[0]
        require(budget == (716 if a == -1 else 772), f"EXPERIMENT_{a}_SHARP_BUDGET")
        budgets.append([a, budget])

        av = scale(engine.v, a)
        expected_h = hermitian_coordinates(((engine.w, av), (conjugate(av), ONE)))
        expected_z = hermitian_coordinates(
            ((add(ONE, engine.w), add(ROOT, av)), (add(conjugate(ROOT), conjugate(av)), ONE))
        )
        require(bare_history[-1].h == expected_h, f"EXPERIMENT_{a}_H_OUT")
        require(bare_history[-1].z == expected_z, f"EXPERIMENT_{a}_Z_OUT")
        require(initial.z[5] == 1, f"EXPERIMENT_{a}_OCCUPIED_INITIAL")
        require(expected_z[5] - 1 == a, f"EXPERIMENT_{a}_FIXED_READER")

        for bank in (715, 716, 771, 772):
            history = [replace(initial, bank=bank)]
            for step in range(6):
                previous = history[-1]
                output = engine.funded(previous)
                history.append(output)
                label = f"EXPERIMENT_{a}_BANK_{bank}_STEP_{step + 1}"
                validate_state(output, label)
                require(
                    engine.energy(output) + output.bank == costs[0] + bank,
                    label + "_ENERGY",
                )
                accepted = step < 5 or bank >= budget
                if accepted:
                    require(core(output) == core(bare_history[step + 1]), label + "_ACCEPTED_CORE")
                    require(output.epsilon == 1, label + "_ACCEPTED_DIRECTION")
                    require(output.bank == bank + costs[0] - costs[step + 1], label + "_ACCEPTED_BANK")
                else:
                    require(output == replace(previous, epsilon=-1), label + "_REFLECTION")
                    require(output.p == 5 and output.h == expected_h and output.z == J8, label + "_REJECTED_CORE")
            restored = history[-1]
            for reverse_index in range(5, -1, -1):
                restored = engine.funded(restored, inverse=True)
                require(
                    restored == history[reverse_index],
                    f"EXPERIMENT_{a}_BANK_{bank}_REVERSE_{reverse_index}",
                )
            require(restored == history[0], f"EXPERIMENT_{a}_BANK_{bank}_RESTORED")
            if bank == 772:
                require(history[-1].bank == (56 if a == -1 else 0), f"EXPERIMENT_{a}_COMMON_BANK")
                require(history[-1].z[5] == (0 if a == -1 else 2), f"EXPERIMENT_{a}_OCCUPIED_FINAL")
            digest.append([a, bank, [pack(state) for state in history]])

        repeated = initial
        for _ in range(36):
            repeated = engine.bare(repeated, 1)
        require(
            (repeated.s, repeated.q, repeated.h, repeated.r, repeated.p)
            == (initial.s, initial.q, initial.h, initial.r, initial.p),
            f"CYCLE_36_{a}_RESTORATION",
        )
        delta = h_sub(repeated.z, initial.z)
        off_diagonal = scale(engine.v, 6 * a)
        predicted_delta = hermitian_coordinates(
            ((scale(engine.w, 10), off_diagonal), (conjugate(off_diagonal), ZERO))
        )
        require(delta == predicted_delta, f"CYCLE_36_{a}_DETECTOR_INCREMENT")
        increments.append([a, list(delta)])
    require(digest.count == 8, "EXPERIMENT_ROW_COUNT")
    return digest, prefix_costs, increments, budgets


def valuation_three(value: int) -> int:
    if value <= 0:
        raise ValueError("valuation requires positive integer")
    valuation = 0
    while value % 3 == 0:
        valuation += 1
        value //= 3
    return valuation


def k1_audit() -> RowDigest:
    words = (
        "0010", "0011", "0100", "0101", "0110",
        "1001", "1010", "1011", "1100", "1101",
    )
    digest = RowDigest()
    for word in words:
        bits = tuple(int(bit) for bit in word)
        slices = []
        for t in (0, 1):
            position = (bits[t + 2] - bits[t]) % 5
            slices.append(tuple(
                Fraction(int(r == position) + int(r == (position + 1) % 5), 2)
                for r in range(5)
            ))
        for n in range(2, 25):
            current, previous = slices[-1], slices[-2]
            slices.append(tuple(
                (
                    460 * current[r]
                    + 29 * (current[(r + 1) % 5] + current[(r - 1) % 5])
                    + 65 * (current[(r + 2) % 5] + current[(r - 2) % 5])
                ) / 324 - previous[r]
                for r in range(5)
            ))
        for n, current in enumerate(slices):
            label = f"K1_{word}_COUNTER_{n}"
            require(sum(current) == 1, label + "_SUM")
            if n >= 2:
                previous, earlier = slices[n - 1], slices[n - 2]
                for r in range(5):
                    residual = (
                        324 * (current[r] + earlier[r]) - 460 * previous[r]
                        - 29 * (previous[(r - 1) % 5] + previous[(r + 1) % 5])
                        - 65 * (previous[(r - 2) % 5] + previous[(r + 2) % 5])
                    )
                    require(residual == 0, label + f"_RECURRENCE_{r}")
            denominator = math.lcm(*(entry.denominator for entry in current))
            predicted_valuation = 0 if n == 0 else 4 * (n - 1)
            require(valuation_three(denominator) == predicted_valuation, label + "_DENOMINATOR")
            digest.append([word, n, [[entry.numerator, entry.denominator] for entry in current]])
    require(digest.count == 250, "K1_ROW_COUNT")
    return digest


def author_certificate() -> tuple[dict, list]:
    engine = Engine()
    constants = engine.constants()
    transport, controls = algebra_audit(engine)
    steps = step_audit(engine)
    experiments, prefixes, increments, budgets = experiment_audit(engine)
    k1 = k1_audit()
    certificate = {
        "schema": SCHEMA,
        "constants": constants,
        "transport_rows": transport.count,
        "transport_sha256": transport.hexdigest(),
        "step_rows": steps.count,
        "step_sha256": steps.hexdigest(),
        "experiment_rows": experiments.count,
        "experiment_sha256": experiments.hexdigest(),
        "prefix_costs": prefixes,
        "detector_increments_36": increments,
        "k1_rows": k1.count,
        "k1_sha256": k1.hexdigest(),
        "negative_controls": controls,
    }
    return certificate, budgets


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate certificate JSON key")
        result[key] = value
    return result


def independent_certificate() -> dict:
    script = Path(__file__).resolve().with_name("breaker.py")
    completed = subprocess.run(
        [sys.executable, "-I", str(script)],
        cwd=str(script.parent),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError("breaker operational failure: nonzero exit")
    if completed.stderr:
        raise RuntimeError("breaker operational failure: nonempty stderr")
    output = completed.stdout.decode("utf-8")
    if not output.endswith("\n") or output.count("\n") != 1:
        raise RuntimeError("breaker operational failure: expected one JSON line")
    certificate = json.loads(output, object_pairs_hook=unique_object)
    if not isinstance(certificate, dict):
        raise RuntimeError("breaker operational failure: certificate is not an object")
    if set(certificate) == {"failure"}:
        label = certificate["failure"]
        if not isinstance(label, str) or not label or "\n" in label or "\r" in label:
            raise RuntimeError("breaker operational failure: invalid failure label")
        raise ScientificFailure("BREAKER_" + label)
    return certificate


def compare_certificates(author: dict, breaker: dict) -> None:
    require(set(author) == set(breaker), "CERTIFICATE_KEYS")
    for key in sorted(author):
        # Canonical JSON comparison also distinguishes integers from booleans
        # and floating point values which Python equality would conflate.
        left = json.dumps(author[key], sort_keys=True, separators=(",", ":"))
        right = json.dumps(breaker[key], sort_keys=True, separators=(",", ":"))
        require(left == right, "CERTIFICATE_" + key.upper())


def print_success(certificate: dict, budgets: list) -> None:
    print("PROBE " + PROBE)
    print("STATUS NON-CANONICAL L1 selected-apparatus")
    print("CONSTANTS " + json.dumps(certificate["constants"], sort_keys=True, separators=(",", ":")))
    print(
        "TRANSPORT rows=" + str(certificate["transport_rows"])
        + " evaluations=39366 sha256=" + certificate["transport_sha256"]
    )
    print("STEP rows=" + str(certificate["step_rows"]) + " sha256=" + certificate["step_sha256"])
    print("NEGATIVE_CONTROLS " + json.dumps(certificate["negative_controls"], separators=(",", ":")))
    print(
        "EXPERIMENT rows=" + str(certificate["experiment_rows"])
        + " sha256=" + certificate["experiment_sha256"]
    )
    for a, costs in certificate["prefix_costs"]:
        print("PREFIX_COSTS a=" + str(a) + " E=" + json.dumps(costs, separators=(",", ":")))
    for a, budget in budgets:
        print("SHARP_BUDGET a=" + str(a) + " bank=" + str(budget) + " common_772_final=" + str(772 - budget))
    for a, increment in certificate["detector_increments_36"]:
        print("BARE_CYCLE_36 a=" + str(a) + " delta_Z=" + json.dumps(increment, separators=(",", ":")))
    print("K1 rows=" + str(certificate["k1_rows"]) + " counters=0..24 sha256=" + certificate["k1_sha256"])
    print("INDEPENDENT_CERTIFICATE MATCH")
    print("RESULT PASS")


def main() -> int:
    try:
        certificate, budgets = author_certificate()
        breaker = independent_certificate()
        compare_certificates(certificate, breaker)
    except ScientificFailure as failure:
        print("PROBE " + PROBE)
        print("SCIENTIFIC_FAIL " + str(failure))
        print("RESULT FAIL")
        return 0
    print_success(certificate, budgets)
    return 0


if __name__ == "__main__":
    sys.exit(main())
