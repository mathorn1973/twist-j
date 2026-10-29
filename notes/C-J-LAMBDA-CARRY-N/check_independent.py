#!/usr/bin/env python3
"""Independent all-depth carry compiler audit, frozen before scientific run.

NON-CANONICAL. No author code or earlier artifact is imported.
Arithmetic uses the lambda companion matrix and its integer adjugate.
Carry discovery is complete BFS from zero for BOTH prescribed units.
An unfinished guarded discovery is INCOMPLETE, not a mathematical negative.

The reversible arithmetic oracle explicitly stores base-five carry-id digits,
writes output and carry registers, and then erases the carry chain. Physical
primitives are checked by complete phase/kernel tables. The enormous compiled
row circuit is justified compositionally, not claimed to have been expanded
and physically simulated for every arithmetic input.
"""

from collections import deque
from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
import json
import sys
import time


DIGITS = (0, 1, 2, 3, 4)
EXHAUSTIVE_DEPTHS = tuple(range(1, 8))
LONG_DEPTHS = (8, 9, 12, 16, 32, 64, 128)
WORD_DEPTHS = tuple(range(1, 6))
MAX_CARRY_STATES = 1_000_000
RUN_BUDGET_SECONDS = 300
Q_BOUND = 3134
COEFFICIENT_BOUND = 35
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
LAMBDA = (
    (0, 0, 0, -5),
    (1, 0, 0, 10),
    (0, 1, 0, -10),
    (0, 0, 1, 5),
)
TO_ZETA = (
    (1, 1, 1, 1),
    (0, -1, -2, -3),
    (0, 0, 1, 3),
    (0, 0, 0, -1),
)
ROOTS_ZETA = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
    (-1, -1, -1, -1),
)
EQUALITY_PERMUTATION = (3, 2, 1, 0, 4)
NEGATIVE_INPUT = (0, 3, 0, 0, 0, 0)
NEGATIVE_CORRECT = (0, 1, 4, 3, 0, 4)
NEGATIVE_SHORTCUT = (0, 1, 4, 3, 0, 0)


class AuditFailure(Exception):
    pass


class Incomplete(Exception):
    pass


def require(condition, message):
    if not condition:
        raise AuditFailure(message)


class Budget:
    def __init__(self):
        self.started = time.monotonic()
        self.stage = "initialization"

    def check(self):
        if time.monotonic() - self.started > RUN_BUDGET_SECONDS:
            raise Incomplete("runtime guard reached during " + self.stage)


def eye():
    return tuple(tuple(int(i == j) for j in range(4)) for i in range(4))


def mm(left, right):
    return tuple(tuple(sum(left[i][k] * right[k][j] for k in range(4))
                       for j in range(4)) for i in range(4))


def mv(matrix, vector):
    return tuple(sum(matrix[i][k] * vector[k] for k in range(4)) for i in range(4))


def linear(*terms):
    return tuple(tuple(sum(coefficient * matrix[i][j] for coefficient, matrix in terms)
                       for j in range(4)) for i in range(4))


def determinant(matrix):
    size = len(matrix)
    value = 0
    for perm in permutations(range(size)):
        term = -1 if sum(perm[i] > perm[j] for i in range(size) for j in range(i + 1, size)) % 2 else 1
        for i in range(size):
            term *= matrix[i][perm[i]]
        value += term
    return value


def adjugate(matrix):
    return tuple(tuple((-1 if (i + j) % 2 else 1)
                       * determinant(tuple(tuple(matrix[r][c] for c in range(4) if c != i)
                                           for r in range(4) if r != j))
                       for j in range(4)) for i in range(4))


def vector_add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def vector_subtract(left, right):
    return tuple(a - b for a, b in zip(left, right))


def encode_id(number, q):
    result = []
    for _ in range(q):
        result.append(number % 5)
        number //= 5
    require(number == 0, "carry id does not fit its declared q digits")
    return tuple(result)


def decode_id(digits):
    number = 0
    for digit in reversed(digits):
        number = 5 * number + digit
    return number


def q_for_count(count):
    q, capacity = 0, 1
    while capacity < count:
        q += 1
        capacity *= 5
    return q


def canonical_table_hash(table):
    encoded = json.dumps(table, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")
    return sha256(encoded).hexdigest()


def map_row(source, forward, inverse):
    return ("".join(map(str, source)) + ">" + "".join(map(str, forward))
            + ">" + "".join(map(str, inverse)) + "\n").encode("ascii")


def word_row(source, output):
    return ("".join(map(str, source)) + ">" + "".join(map(str, output)) + "\n").encode("ascii")


def norm_data(lambda_coefficients):
    zeta = mv(TO_ZETA, lambda_coefficients)
    q_value = 5 * sum(c * c for c in zeta) - sum(zeta) ** 2
    require(q_value >= 0, "trace quadratic form became negative")
    require(q_value <= Q_BOUND, "analytic reachable-carry Q bound failed")
    require(max(abs(c) for c in zeta) <= COEFFICIENT_BOUND,
            "analytic reachable-carry coefficient bound failed")
    return zeta, q_value, max(abs(c) for c in zeta)


def build_engine():
    ident = eye()
    adj = adjugate(LAMBDA)
    require(determinant(LAMBDA) == 5, "lambda determinant")
    require(mm(adj, LAMBDA) == linear((5, ident))
            and mm(LAMBDA, adj) == linear((5, ident)), "integer adjugate division identity")
    require(mm(TO_ZETA, TO_ZETA) == ident, "basis substitution identity")
    l2 = mm(LAMBDA, LAMBDA)
    j = linear((2, ident), (-2, LAMBDA), (1, l2))
    j_inverse = linear((-2, ident), (3, LAMBDA), (-1, l2))
    require(mm(j, j_inverse) == ident and mm(j_inverse, j) == ident, "exact J inverse")
    require(determinant(j) == determinant(j_inverse) == 1, "unit norms")
    zeta = linear((1, ident), (-1, LAMBDA))
    zeta_power = ident
    zeta_sum = linear((0, ident))
    for _ in range(5):
        zeta_sum = linear((1, zeta_sum), (1, zeta_power))
        zeta_power = mm(zeta_power, zeta)
    require(zeta_power == ident and zeta_sum == linear((0, ident)), "cyclotomic identities")
    require(1791 * 1791 > 5 * 800 * 800, "rational minimum-modulus bound")
    for a, b in product(DIGITS, repeat=2):
        require(6 * b * b - 6 * a * b + 4 * a * a <= 96, "J forcing norm bound")
        require(6 * b * b - 4 * a * b + 4 * a * a <= 96, "inverse forcing norm bound")
    return {"adj_lambda": adj, "J": j, "J_inverse": j_inverse}


def carry_edge(carry, digit, unit_vector, adj_lambda):
    total = tuple(carry[i] + digit * unit_vector[i] for i in range(4))
    output = total[0] % 5
    residual = (total[0] - output,) + total[1:]
    numerator = mv(adj_lambda, residual)
    require(all(v % 5 == 0 for v in numerator), "carry division not integral")
    successor = tuple(v // 5 for v in numerator)
    require(mv(LAMBDA, successor) == residual, "exact local carry identity")
    return output, successor


def discover_automaton(name, engine, budget):
    budget.stage = "complete carry BFS for " + name
    unit_vector = mv(engine[name], ONE)
    distances = {ZERO: 0}
    queue = deque((ZERO,))
    edges = {}
    norm_data(ZERO)
    while queue:
        budget.check()
        state = queue.popleft()
        row = []
        for digit in DIGITS:
            output, successor = carry_edge(state, digit, unit_vector, engine["adj_lambda"])
            row.append((output, successor))
            if successor not in distances:
                if len(distances) >= MAX_CARRY_STATES:
                    raise Incomplete("state guard reached before complete carry closure for " + name)
                norm_data(successor)
                distances[successor] = distances[state] + 1
                queue.append(successor)
        require({output for output, _ in row} == set(DIGITS),
                "one carry state does not permute the five input/output letters")
        edges[state] = tuple(row)
    require(len(edges) == len(distances), "carry BFS ended with incomplete transition rows")

    zeta_states = [ZERO] + sorted(mv(TO_ZETA, c) for c in distances if c != ZERO)
    lambda_states = [mv(TO_ZETA, c) for c in zeta_states]
    index = {c: i for i, c in enumerate(lambda_states)}
    require(index[ZERO] == 0, "semantic zero does not have reserved id zero")
    transitions = [[[output, index[successor]] for output, successor in edges[state]]
                   for state in lambda_states]
    table = {"states": zeta_states, "transitions": transitions}
    q = q_for_count(len(lambda_states))
    codes = tuple(encode_id(i, q) for i in range(len(lambda_states)))
    require(all(decode_id(code) == i for i, code in enumerate(codes)), "carry code roundtrip")
    max_q = max(norm_data(c)[1] for c in lambda_states)
    max_abs = max(norm_data(c)[2] for c in lambda_states)
    facts = {
        "unit": name, "states": len(lambda_states), "edges": 5 * len(lambda_states),
        "max_depth": max(distances.values()), "max_Q": max_q, "max_abs": max_abs,
        "q": q, "table_sha256": canonical_table_hash(table),
    }
    return {"name": name, "matrix": engine[name], "states": tuple(lambda_states),
            "index": index, "transitions": transitions, "q": q, "codes": codes,
            "facts": facts}


def audit_duality(forward, inverse, inverse_matrix):
    require(len(forward["states"]) == len(inverse["states"]), "unit carry closures have unequal sizes")
    dual = {}
    for i, state in enumerate(forward["states"]):
        target = tuple(-v for v in mv(inverse_matrix, state))
        require(target in inverse["index"], "forward carry dual absent from inverse closure")
        dual[i] = inverse["index"][target]
    require(set(dual.values()) == set(range(len(inverse["states"]))), "carry duality not bijective")
    checked = 0
    for state_id, row in enumerate(forward["transitions"]):
        for digit, (output, successor) in enumerate(row):
            back_output, back_successor = inverse["transitions"][dual[state_id]][output]
            require(back_output == digit and back_successor == dual[successor],
                    "dual edge does not swap input and output exactly")
            checked += 1
    return checked


def stream(automaton, word):
    state = 0
    output = []
    for digit in word:
        emitted, state = automaton["transitions"][state][digit]
        output.append(emitted)
    return tuple(output), state


def word_value(word):
    value = ZERO
    for digit in reversed(word):
        value = mv(LAMBDA, value)
        value = (value[0] + digit,) + value[1:]
    return value


def shift_value(value, count):
    for _ in range(count):
        value = mv(LAMBDA, value)
    return value


def check_ring_identity(automaton, source, output, final_state):
    product_value = mv(automaton["matrix"], word_value(source))
    residual = vector_subtract(product_value, word_value(output))
    require(residual == shift_value(automaton["states"][final_state], len(source)),
            "complete O telescoping identity failed")


def out_of_place(automaton, source, target, sign):
    require(sign in (-1, 1), "invalid output-addition sign")
    length, q = len(source), automaton["q"]
    require(len(target) == length, "out-of-place target length")
    carry_registers = [[0] * q for _ in range(length + 1)]
    result = list(target)
    for i, digit in enumerate(source):
        state_id = decode_id(carry_registers[i])
        require(state_id < len(automaton["states"]), "initialized carry computation reached an unused code")
        output, successor = automaton["transitions"][state_id][digit]
        result[i] = (result[i] + sign * output) % 5
        code = automaton["codes"][successor]
        for k in range(q):
            carry_registers[i + 1][k] = (carry_registers[i + 1][k] + code[k]) % 5
    for i in range(length - 1, -1, -1):
        state_id = decode_id(carry_registers[i])
        require(state_id < len(automaton["states"]), "carry uncomputation reached an unused code")
        _, successor = automaton["transitions"][state_id][source[i]]
        code = automaton["codes"][successor]
        for k in range(q):
            carry_registers[i + 1][k] = (carry_registers[i + 1][k] - code[k]) % 5
    require(all(v == 0 for register in carry_registers for v in register),
            "carry workspace did not return to all-zero digits")
    return tuple(result)


def clean_multiply(source, forward, inverse):
    # E_forward, swap data/buffer, E_inverse with output subtraction.
    buffer = out_of_place(forward, source, (0,) * len(source), 1)
    data, buffer = buffer, source
    buffer = out_of_place(inverse, data, buffer, -1)
    require(buffer == (0,) * len(source), "in-place multiplication did not clean its data buffer")
    return data


def audit_one_word(source, forward, inverse, dirty=False):
    output, final_carry = stream(forward, source)
    back_output, final_inverse_carry = stream(inverse, source)
    check_ring_identity(forward, source, output, final_carry)
    check_ring_identity(inverse, source, back_output, final_inverse_carry)
    require(stream(inverse, output)[0] == source and stream(forward, back_output)[0] == source,
            "unit stream compositions are not inverse")
    require(clean_multiply(source, forward, inverse) == output, "clean in-place J differs from stream")
    require(clean_multiply(source, inverse, forward) == back_output, "clean in-place inverse differs from stream")
    if dirty:
        occupied = tuple((i + 2) % 5 for i in range(len(source)))
        for automaton, expected in ((forward, output), (inverse, back_output)):
            result = out_of_place(automaton, source, occupied, 1)
            require(result == tuple((a + b) % 5 for a, b in zip(occupied, expected)),
                    "out-of-place operation overwrote occupied target digits")
            require(out_of_place(automaton, source, result, -1) == occupied,
                    "occupied-target addition did not invert")
    return output, back_output


def long_words(length):
    words = {tuple(d for _ in range(length)) for d in DIGITS}
    words.add(tuple(i % 5 for i in range(length)))
    words.add(tuple((4 - i) % 5 for i in range(length)))
    words.add(tuple(i.bit_count() % 2 for i in range(length)))
    for offset in DIGITS:
        words.add(tuple((i * i + 3 * i + offset) % 5 for i in range(length)))
    for position in (0, length // 2, length - 1):
        for amplitude in (1, 2, 3, 4):
            word = [0] * length
            word[position] = amplitude
            words.add(tuple(word))
    return tuple(sorted(words))


def audit_words(forward, inverse, budget):
    exhaustive, long = [], []
    dirty_cases = 0
    for length in EXHAUSTIVE_DEPTHS:
        budget.stage = "exhaustive arithmetic and clean circuits at N=" + str(length)
        digest = sha256()
        outputs, inverse_outputs = set(), set()
        count = 0
        for source in product(DIGITS, repeat=length):
            if count % 256 == 0:
                budget.check()
            output, back_output = audit_one_word(source, forward, inverse, dirty=length <= 4)
            digest.update(map_row(source, output, back_output))
            outputs.add(output)
            inverse_outputs.add(back_output)
            count += 1
            if length <= 4:
                dirty_cases += 2
        require(count == 5 ** length and len(outputs) == len(inverse_outputs) == count,
                "exhaustive finite-level unit maps are not complete permutations")
        exhaustive.append({"N": length, "words": count, "map_sha256": digest.hexdigest()})
    require(sum(row["words"] for row in exhaustive) == 97655, "exhaustive inventory size")
    for length in LONG_DEPTHS:
        budget.stage = "deterministic long arithmetic and clean circuits at N=" + str(length)
        digest = sha256()
        words = long_words(length)
        for source in words:
            budget.check()
            output, back_output = audit_one_word(source, forward, inverse)
            digest.update(map_row(source, output, back_output))
        long.append({"N": length, "words": len(words), "map_sha256": digest.hexdigest()})
    return exhaustive, long, dirty_cases


def root_sum(exponents):
    exponents = tuple(exponents)
    return tuple(sum(ROOTS_ZETA[exponent % 5][i] for exponent in exponents) for i in range(4))


def audit_diagonal_words(forward, inverse, budget):
    facts = []
    for length in WORD_DEPTHS:
        budget.stage = "diagonal readout by repeated clean J at N=" + str(length)
        digest = sha256()
        outputs = set()
        zero_count, count = 0, 0
        for source in product(DIGITS, repeat=length):
            if count % 256 == 0:
                budget.check()
            current = source
            output = []
            for clock in range(length):
                output.append(current[clock])
                current = clean_multiply(current, forward, inverse)
            output = tuple(output)
            outputs.add(output)
            digest.update(word_row(source, output))
            exact_zero = root_sum(output) == ZERO
            balanced = length % 5 == 0 and all(output.count(d) == length // 5 for d in DIGITS)
            require(exact_zero == balanced, "exact O return criterion")
            zero_count += int(exact_zero)
            count += 1
        require(count == len(outputs) == 5 ** length, "diagonal output not a complete permutation")
        require(zero_count == (120 if length == 5 else 0), "small complete-word return count")
        facts.append({"N": length, "words": count, "map_sha256": digest.hexdigest(),
                      "zero_count": zero_count})
    return facts


def permutation_sign(perm):
    return -1 if sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm))) % 2 else 1


def equality_phase(a, k, x, phase_target):
    shifted = (x + 4 - a) % 5
    control = shifted
    phase = Fraction(k * control * phase_target, 25)
    control = EQUALITY_PERMUTATION[control]
    phase += Fraction(k * control * phase_target, 25)
    control = EQUALITY_PERMUTATION[control]
    require(control == shifted, "equality permutation did not restore its control")
    beta = Fraction(25 - 3 * k, 250)
    require(Fraction(k, 25) > 0 and beta > 0, "equality construction used a nonpositive pair pulse")
    echo_sum = 0
    for _ in range(5):
        echo_sum += control
        phase += beta * control * phase_target
        control = (control + 1) % 5
    require(control == shifted and echo_sum == 10, "five-shift equality echo failed")
    restored = (control - (4 - a)) % 5
    require(restored == x, "equality pretranslation did not uncompute")
    target = Fraction(k * int(x == a) * phase_target, 5)
    require(phase - target == phase_target, "complete positive-pulse equality phase differs nonintegrally")
    return phase


def multiplication_phase(sign, x, y, z):
    original = (x, y, z)
    registers = list(original)
    phase = sum(value ** 3 for value in original)
    pair_pulses, cubic_phases = 0, 3
    for source, target in ((0, 1), (0, 2), (1, 2)):
        registers[target] = (registers[target] + registers[source]) % 5
        pair_pulses += 1
        phase -= registers[target] ** 3
        cubic_phases += 1
        registers[target] = (registers[target] - registers[source]) % 5
        pair_pulses += 1
        require(tuple(registers) == original, "pair linear form did not uncompute")
    registers[2] = (registers[2] + registers[0]) % 5
    registers[2] = (registers[2] + registers[1]) % 5
    pair_pulses += 2
    phase += registers[2] ** 3
    cubic_phases += 1
    registers[2] = (registers[2] - registers[1]) % 5
    registers[2] = (registers[2] - registers[0]) % 5
    pair_pulses += 2
    require(tuple(registers) == original and pair_pulses == 10 and cubic_phases == 7,
            "cubic polarization resource/restoration identity")
    require(phase % 5 == x * y * z % 5, "cubic polarization identity")
    return sign * phase % 5


def audit_physical_primitives(budget):
    budget.stage = "complete physical primitive truth tables"
    require(permutation_sign(EQUALITY_PERMUTATION) == 1, "equality local permutation determinant")
    for shift in DIGITS:
        require(permutation_sign(tuple((x + shift) % 5 for x in DIGITS)) == 1,
                "cyclic local translation determinant")
    equality_phases = {}
    for a, k, x, t in product(DIGITS, (1, 2, 3, 4), DIGITS, DIGITS):
        equality_phases[(a, k, x, t)] = equality_phase(a, k, x, t)
    equality_matrix_cases = 0
    for a, k, x, old, new in product(DIGITS, (1, 2, 3, 4), DIGITS, DIGITS, DIGITS):
        exponents = []
        for t in DIGITS:
            exponent = 5 * equality_phases[(a, k, x, t)]
            require(exponent.denominator == 1, "equality phase not a fifth-root phase after echo")
            exponents.append(exponent.numerator + (old - new) * t)
        numerator = root_sum(exponents)
        expected = (5, 0, 0, 0) if new == (old + k * int(x == a)) % 5 else ZERO
        require(numerator == expected, "equality Fourier kernel or relative phase failed")
        equality_matrix_cases += 1
    multiplication_phases = {}
    for sign, x, y, z in product((-1, 1), DIGITS, DIGITS, DIGITS):
        multiplication_phases[(sign, x, y, z)] = multiplication_phase(sign, x, y, z)
    multiply_matrix_cases = 0
    for sign, x, y, old, new in product((-1, 1), DIGITS, DIGITS, DIGITS, DIGITS):
        numerator = root_sum(multiplication_phases[(sign, x, y, t)] + (old - new) * t for t in DIGITS)
        expected = (5, 0, 0, 0) if new == (old + sign * x * y) % 5 else ZERO
        require(numerator == expected, "multiply-add Fourier kernel or relative phase failed")
        multiply_matrix_cases += 1
    facts = {"equality_phase_cases": len(equality_phases),
             "equality_matrix_cases": equality_matrix_cases,
             "multiply_phase_cases": len(multiplication_phases),
             "multiply_matrix_cases": multiply_matrix_cases}
    require(facts == {"equality_phase_cases": 500, "equality_matrix_cases": 2500,
                      "multiply_phase_cases": 250, "multiply_matrix_cases": 1250},
            "physical primitive inventory")
    budget.check()
    return facts


def apply_row(controls, target, expected_controls, values):
    r = len(controls)
    flags = [0] * r
    products = [0] * max(0, r - 1)
    for i in range(r):
        flags[i] = (flags[i] + int(controls[i] == expected_controls[i])) % 5
    for i in range(r - 1):
        left = flags[0] if i == 0 else products[i - 1]
        products[i] = (products[i] + left * flags[i + 1]) % 5
    active = flags[0] if r == 1 else products[-1]
    output = tuple((old + active * value) % 5 for old, value in zip(target, values))
    for i in range(r - 2, -1, -1):
        left = flags[0] if i == 0 else products[i - 1]
        products[i] = (products[i] - left * flags[i + 1]) % 5
    for i in range(r - 1, -1, -1):
        flags[i] = (flags[i] - int(controls[i] == expected_controls[i])) % 5
    require(flags == [0] * r and products == [0] * max(0, r - 1), "lookup row flags not clean")
    return output


def audit_rows_and_resources(forward, inverse):
    require(forward["q"] == inverse["q"], "dual automata require unequal code widths")
    q = forward["q"]
    toy_cases = 0
    for wanted, values in (((3,), (4,)), ((2, 0, 4), (2, 3))):
        for controls in product(DIGITS, repeat=len(wanted)):
            for target in product(DIGITS, repeat=len(values)):
                output = apply_row(controls, target, wanted, values)
                expected = tuple((old + (value if controls == wanted else 0)) % 5
                                 for old, value in zip(target, values))
                require(output == expected, "lookup row changed a nonmatching control or wrong target")
                toy_cases += 1
    r = q + 1
    forward_row_bound = 34 * r - 20 + q + 1
    erase_row_bound = 34 * r - 20 + q
    require(forward_row_bound + erase_row_bound == 70 * q + 29, "compiled E row count")
    rows_j = 5 * len(forward["states"])
    rows_inverse = 5 * len(inverse["states"])
    facts = {"q": q, "rows_J": rows_j, "rows_inverse": rows_inverse,
             "pair_upper_per_digit": (70 * q + 29) * (rows_j + rows_inverse) + 3,
             "memory_linear": q + 2, "memory_constant": 3 * q + 1}
    for length in EXHAUSTIVE_DEPTHS + LONG_DEPTHS:
        allocated = 2 * length + q * (length + 1) + (q + 1) + q
        require(allocated == facts["memory_linear"] * length + facts["memory_constant"],
                "full data/buffer/carry/flag workspace count")
    return facts, toy_cases


def audit_negative_a6(forward):
    correct, _ = stream(forward, NEGATIVE_INPUT)
    raw = tuple((2 * NEGATIVE_INPUT[k]
                 - (2 * NEGATIVE_INPUT[k - 1] if k >= 1 else 0)
                 + (NEGATIVE_INPUT[k - 2] if k >= 2 else 0)) % 5 for k in range(6))
    old = list(raw)
    old[4] = (old[4] - (2 * NEGATIVE_INPUT[0]) // 5) % 5
    old = tuple(old)
    require(correct == NEGATIVE_CORRECT and old == NEGATIVE_SHORTCUT and correct != old,
            "the prescribed A6 failure of the A5-only shortcut was absent")
    return {"input": NEGATIVE_INPUT, "correct": correct, "old_shortcut": old}


def main():
    budget = Budget()
    engine = build_engine()
    forward = discover_automaton("J", engine, budget)
    inverse = discover_automaton("J_inverse", engine, budget)
    budget.stage = "complete inverse-automaton edge duality"
    dual_edges = audit_duality(forward, inverse, engine["J_inverse"])
    budget.check()
    gates = audit_physical_primitives(budget)
    resources, toy_cases = audit_rows_and_resources(forward, inverse)
    exhaustive, long, dirty_cases = audit_words(forward, inverse, budget)
    word_readout = audit_diagonal_words(forward, inverse, budget)
    negative = audit_negative_a6(forward)
    budget.check()
    report = {
        "facts": {
            "carry": [forward["facts"], inverse["facts"]],
            "dual_edges": dual_edges,
            "exhaustive": exhaustive,
            "long": long,
            "word_readout": word_readout,
            "resources": resources,
            "negative_A6": negative,
            "gates": gates,
        },
        "checks": {
            "engine": "lambda basis; integer adjugate division; independent exact O telescoping",
            "complete_BFS_both_units": True,
            "carry_zero_id": 0,
            "carry_id_digits_least_significant_first": True,
            "guard_states_per_unit": MAX_CARRY_STATES,
            "guard_seconds": RUN_BUDGET_SECONDS,
            "guard_failure_is_incomplete_not_negative": True,
            "dirty_target_E_cases": dirty_cases,
            "toy_lookup_row_cases": toy_cases,
            "full_arithmetic_oracle_enumeration": True,
            "all_physical_pulses_expanded_for_all_arithmetic_words": False,
            "physical_claim": "complete primitive matrices plus clean reversible row decomposition and symbolic resource bound",
            "native_U_transfer": False,
        },
        "scope": "NON-CANONICAL; local independent reconstruction in one session and one architecture",
        "result": "PASS",
    }
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    try:
        main()
    except Incomplete as exc:
        print(json.dumps({"result": "INCOMPLETE", "reason": str(exc),
                          "mathematical_negative": False}, sort_keys=True, indent=2))
        sys.exit(2)
    except Exception as exc:
        print(json.dumps({"result": "FAIL", "exception": type(exc).__name__,
                          "message": str(exc)}, sort_keys=True, indent=2))
        raise
