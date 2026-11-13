#!/usr/bin/env python3
"""Independent exact audit of the frozen 64-G chronological construction.

Authored from PROGRAM.json, the analytical physical proofs, and the native
generator equations in canon/CANON.md, without reading another verifier.
The field implementation is rational polynomial arithmetic modulo X**8+1.
No floating point, symbolic package, tensor truncation, or pulse search is used.
The inverse audit is algebraic; it asserts no physical availability of G^-1.
"""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
import json
from pathlib import Path


class Cyclotomic:
    """An element of Q[X]/(X^8+1), with X = exp(i*pi/8)."""

    __slots__ = ("coefficients",)

    def __init__(self, coefficients):
        self.coefficients = tuple(Fraction(c) for c in coefficients)
        assert len(self.coefficients) == 8

    def __hash__(self):
        return hash(self.coefficients)

    def __eq__(self, other):
        return isinstance(other, Cyclotomic) and self.coefficients == other.coefficients

    def __bool__(self):
        return any(self.coefficients)

    def __add__(self, other):
        return add(self, scalar(other) if isinstance(other, (int, Fraction)) else other)

    __radd__ = __add__

    def __neg__(self):
        return Cyclotomic(tuple(-c for c in self.coefficients))

    def __sub__(self, other):
        return self + -(scalar(other) if isinstance(other, (int, Fraction)) else other)

    def __mul__(self, other):
        return multiply(self, scalar(other) if isinstance(other, (int, Fraction)) else other)

    __rmul__ = __mul__

    def conjugate(self):
        # X^-r = -X^(8-r), 1 <= r <= 7.
        return Cyclotomic((self.coefficients[0],) + tuple(-self.coefficients[8-r] for r in range(1, 8)))


@lru_cache(maxsize=None)
def scalar(value):
    return Cyclotomic((value, 0, 0, 0, 0, 0, 0, 0))


@lru_cache(maxsize=32768)
def add(left, right):
    if not left:
        return right
    if not right:
        return left
    return Cyclotomic(tuple(a+b for a, b in zip(left.coefficients, right.coefficients)))


@lru_cache(maxsize=32768)
def multiply(left, right):
    if not left or not right:
        return scalar(0)
    if left == scalar(1):
        return right
    if right == scalar(1):
        return left
    result = [Fraction(0)] * 8
    for a, ca in enumerate(left.coefficients):
        if ca:
            for b, cb in enumerate(right.coefficients):
                if cb:
                    degree = a+b
                    result[degree % 8] += ca*cb * (1 if degree < 8 else -1)
    return Cyclotomic(result)


@lru_cache(maxsize=None)
def root_power(exponent):
    exponent %= 16
    result = [0] * 8
    result[exponent % 8] = 1 if exponent < 8 else -1
    return Cyclotomic(result)


ZERO, ONE = scalar(0), scalar(1)
IMAGINARY = root_power(4)


def clean(vector):
    return {index: amplitude for index, amplitude in vector.items() if amplitude}


def accumulate(vector, index, amplitude):
    vector[index] = vector.get(index, ZERO) + amplitude


def adjoint(matrix):
    """Conjugate transpose of a column-indexed sparse matrix."""
    result = [{} for _ in matrix]
    for column, entries in enumerate(matrix):
        for row, value in entries.items():
            result[row][column] = value.conjugate()
    return tuple(result)


def apply_matrix(matrix, vector):
    result = {}
    for column, amplitude in vector.items():
        for row, entry in matrix[column].items():
            accumulate(result, row, entry*amplitude)
    return clean(result)


def matrix_product(left, right):
    return tuple(apply_matrix(left, column) for column in right)


def identity(dimension):
    return tuple({j: ONE} for j in range(dimension))


@lru_cache(maxsize=None)
def carrier_matrix(level, angle, phase):
    """Full five-level physical primitive; angle in pi/4, phase in pi/2."""
    assert 1 <= level <= 4 and angle > 0 and phase in range(4)
    cosine = (root_power(angle)+root_power(-angle))*Fraction(1, 2)
    sine = (root_power(angle)-root_power(-angle))*(-IMAGINARY)*Fraction(1, 2)
    upper = -IMAGINARY*sine*root_power(-4*phase)
    lower = -IMAGINARY*sine*root_power(4*phase)
    columns = [dict(column) for column in identity(5)]
    columns[0] = clean({0: cosine, level: lower})
    columns[level] = clean({0: upper, level: cosine})
    return tuple(columns)


def pulse(ion, level, axis, signed_angle):
    assert axis in ("x", "y") and signed_angle
    phase = (int(axis == "y") + (2 if signed_angle < 0 else 0)) % 4
    return ("R", ion, level, abs(signed_angle), phase)


def pulse_adjoint(operation):
    kind, ion, level, angle, phase = operation
    assert kind == "R"
    return kind, ion, level, angle, (phase+2) % 4


def cycle_star_word(permutation):
    """The declared canonical cycle compiler, not a greedy sorting circuit."""
    assert sorted(permutation) == list(range(5))
    visited = set()
    word = []
    for smallest in range(5):
        if smallest in visited:
            continue
        cycle = []
        current = smallest
        while current not in visited:
            visited.add(current)
            cycle.append(current)
            current = permutation[current]
        assert current == smallest and min(cycle) == smallest
        if len(cycle) == 1:
            continue
        if smallest == 0:
            word.extend(cycle[1:])
        else:
            word.extend(cycle + [smallest])
    assert len(word) <= 6
    return tuple(word)


def permutation_pulses(ion, permutation):
    return [pulse(ion, j, "x", 4) for j in cycle_star_word(permutation)]


def inverse_pulses(word):
    return [pulse_adjoint(operation) for operation in reversed(word)]


def monomial_matrix(word):
    result = identity(5)
    for operation in word:
        _, _, level, angle, phase = operation
        result = matrix_product(carrier_matrix(level, angle, phase), result)
    return result


def affine_audit():
    lengths = {}
    for a, b in product(range(1, 5), range(5)):
        permutation = tuple((a*x+b) % 5 for x in range(5))
        word = permutation_pulses(0, permutation)
        matrix = monomial_matrix(word)
        physical_inverse = monomial_matrix(inverse_pulses(word))
        assert physical_inverse == adjoint(matrix)
        assert matrix_product(physical_inverse, matrix) == identity(5)
        for x, column in enumerate(matrix):
            assert set(column) == {permutation[x]}
            phase = column[permutation[x]]
            assert phase.conjugate()*phase == ONE
        # Diagonal conjugation coefficients are audited separately for all d_j.
        for diagonal_label in range(5):
            diagonal = tuple({x: ONE} if x == diagonal_label else {} for x in range(5))
            conjugated = matrix_product(physical_inverse, matrix_product(diagonal, matrix))
            expected = tuple({x: ONE} if permutation[x] == diagonal_label else {} for x in range(5))
            assert conjugated == expected
        lengths[a, b] = len(word)
    assert sum(lengths.values()) == 72
    return lengths


def echo_audit(lengths):
    """Integer coefficient identities for all 500 rows and all six edges."""
    directions = [v for v in product(range(5), repeat=3)
                  if any(v) and next(c for c in v if c) == 1]
    assert len(directions) == 31 and directions == sorted(directions)
    active = (1, 0, 0)
    spectator_directions = [v for v in directions if v != active][:15]
    parameters = list(product(range(1, 5), product(range(5), repeat=3)))
    assert len(parameters) == 500
    for endpoint in range(2, 8):
        vectors = {}
        remaining = iter(spectator_directions)
        for ion in range(17):
            vectors[ion] = active if ion in (14, endpoint) else next(remaining)
        images = {}
        per_g_carriers = 0
        for ion in range(17):
            maps = []
            v = vectors[ion]
            for a, u in parameters:
                offset = sum(c*d for c, d in zip(v, u)) % 5
                maps.append((a, offset))
                per_g_carriers += 2*lengths[a, offset]
            assert Counter(maps) == Counter({pair: 25 for pair in lengths})
            for x in range(5):
                image = tuple((a*x+b) % 5 for a, b in maps)
                assert Counter(image) == Counter({label: 100 for label in range(5)})
                images[ion, x] = image
        assert per_g_carriers == 61200
        for first, second in combinations(range(17), 2):
            selected = {first, second} == {14, endpoint}
            for x, y in product(range(5), repeat=2):
                counts = Counter(zip(images[first, x], images[second, y]))
                if not selected:
                    expected = {(r, s): 20 for r, s in product(range(5), repeat=2)}
                elif x == y:
                    expected = {(r, r): 100 for r in range(5)}
                else:
                    expected = {(r, s): 25 for r, s in product(range(5), repeat=2) if r != s}
                assert counts == Counter(expected)
                # Symmetrize the d_r*d_s coefficients and include 2*g_ij.
                if selected:
                    for r in range(5):
                        assert 2*counts[r, r] == (200 if x == y else 0)
                    for r, s in combinations(range(5), 2):
                        assert 2*(counts[r, s]+counts[s, r]) == (0 if x == y else 100)
        # These coefficients are 40*S^2-10*B+50*B*[x=y].
        # B=5*Q-S^2 has coefficients 4 on d_r^2 and -2 on d_r*d_s.
        assert 40-10*4 == 0 and 80-10*(-2) == 100
        assert 40-10*4+50*4 == 200 and 80-10*(-2)+50*(-2) == 0
    return 500


def mask_permutation(level, labels):
    assert 1 <= level <= 4 and len(labels) == 2 and list(labels) == sorted(set(labels))
    source = list(labels) + [j for j in range(5) if j not in labels]
    destination = [0, level] + [j for j in range(5) if j not in (0, level)]
    permutation = [None]*5
    for old, new in zip(source, destination):
        permutation[old] = new
    return tuple(permutation)


def mask_word(control, target, level, labels, beta):
    frame = permutation_pulses(control, mask_permutation(level, labels))
    g = ("G", control, target)
    return frame + [g, g, pulse(target, level, "y", -beta),
                    g, g, pulse(target, level, "y", beta)] + inverse_pulses(frame)


def singleton_masks(control, target, level, label):
    b, c = [j for j in range(5) if j != label][:2]
    return (("mask", control, target, level, tuple(sorted((label, b))), 1),
            ("mask", control, target, level, tuple(sorted((label, c))), 1),
            ("mask", control, target, level, (b, c), -1))


def exchange_word(first, second, level):
    g = ("G", first, second)
    word = [g]
    for axis in ("y", "x"):
        word.extend(pulse(ion, level, axis, -2) for ion in (first, second))
        word.append(g)
        word.extend(pulse(ion, level, axis, 2) for ion in (first, second))
    return word


def compile_operation(operation):
    kind = operation[0]
    if kind == "carrier":
        _, ion, level, axis, angle = operation
        return [pulse(ion, level, axis, angle)]
    if kind == "exchange":
        return exchange_word(*operation[1:])
    if kind == "mask":
        return mask_word(*operation[1:])
    assert kind == "single"
    return [step for mask in singleton_masks(*operation[1:]) for step in mask_word(*mask[1:])]


def tensor_apply(vector, ions, matrix):
    """Apply a complete small operator to a sparse 17-register state."""
    result = {}
    for labels, amplitude in vector.items():
        column = 0
        for ion in ions:
            column = 5*column+labels[ion]
        for row, entry in matrix[column].items():
            output = list(labels)
            for ion in reversed(ions):
                output[ion] = row % 5
                row //= 5
            accumulate(result, tuple(output), entry*amplitude)
    return clean(result)


def elementary_apply(vector, operation, sigma, omit_ls):
    if operation[0] == "R":
        _, ion, level, angle, phase = operation
        return tensor_apply(vector, (ion,), carrier_matrix(level, angle, phase))
    _, first, second = operation
    if omit_ls:
        # All 500 loop slots remain, as do the monomial carrier frames.
        # Their identity is independently certified by affine_audit().
        return vector
    phase = root_power(-4*sigma)
    return {labels: amplitude*(phase if labels[first] == labels[second] else ONE)
            for labels, amplitude in vector.items()}


@lru_cache(maxsize=None)
def local_matrix(operation, sigma, omit_ls=False):
    """Compile the actual primitive word on all 25 columns, retaining phases."""
    assert sigma in (-1, 1)
    if operation[0] == "carrier":
        _, _, level, axis, angle = operation
        _, _, _, area, phase = pulse(0, level, axis, angle)
        return carrier_matrix(level, area, phase)
    local_operation = (operation[0], 0, 1) + operation[3:]
    word = compile_operation(local_operation)
    result = []
    for first, second in product(range(5), repeat=2):
        vector = {(first, second): ONE}
        for primitive in word:
            vector = elementary_apply(vector, primitive, sigma, omit_ls)
        result.append({5*labels[0]+labels[1]: value for labels, value in vector.items()})
    return tuple(result)


def expected_mask(level, labels, beta):
    _, _, _, area, phase = pulse(1, level, "y", 2*beta)
    rotation = carrier_matrix(level, area, phase)
    return tuple({5*c+r: value for r, value in rotation[t].items()}
                 if c in labels else {5*c+t: ONE}
                 for c, t in product(range(5), repeat=2))


def expected_exchange(level, sigma):
    columns = []
    for first, second in product(range(5), repeat=2):
        if first in (0, level) and second in (0, level):
            columns.append({5*second+first: -ONE})
        elif first == second:
            columns.append({5*first+second: sigma*IMAGINARY})
        else:
            columns.append({5*first+second: ONE})
    return tuple(columns)


def freeze_lists(value):
    return tuple(freeze_lists(item) for item in value) if isinstance(value, list) else value


def helper_audit(operations):
    exchange_ops = {operation for operation in operations if operation[0] == "exchange"}
    mask_ops = {operation for operation in operations if operation[0] == "mask"}
    single_ops = {operation for operation in operations if operation[0] == "single"}
    for operation in single_ops:
        mask_ops.update(singleton_masks(*operation[1:]))
    # The shared audit count identifies abstract (k,A,beta) helpers.
    # Every actual control/target placement is retained in register_audit.
    mask_ops = {(operation[0], 0, 1) + operation[3:] for operation in mask_ops}
    assert len(exchange_ops) == 4 and len(single_ops) == 2
    assert len(mask_ops) == 12
    for sigma in (-1, 1):
        for operation in sorted(exchange_ops):
            matrix = local_matrix(operation, sigma)
            assert matrix == expected_exchange(operation[3], sigma)
            assert matrix_product(adjoint(matrix), matrix) == identity(25)
            assert local_matrix(operation, sigma, True) == identity(25)
        for operation in sorted(mask_ops):
            _, _, _, level, labels, beta = operation
            matrix = local_matrix(operation, sigma)
            assert matrix == expected_mask(level, labels, beta)
            assert matrix_product(adjoint(matrix), matrix) == identity(25)
            assert local_matrix(operation, sigma, True) == identity(25)
        for operation in sorted(single_ops):
            _, _, _, level, label = operation
            matrix = local_matrix(operation, sigma)
            assert matrix == expected_mask(level, (label,), 2)
            assert matrix_product(adjoint(matrix), matrix) == identity(25)
            assert local_matrix(operation, sigma, True) == identity(25)
    return len(exchange_ops)*25*2, len(mask_ops)*25*2, len(single_ops)*25*2


def original_generator(index, checkpoint):
    """Canon section 2 selector and section 3 original generator equations."""
    p1, p4, p1p, p4p, q, r = checkpoint
    images = ((p4, p1, p4p, p1p, q, r),
              (-p1p, -p4p, -p1, -p4, -q, -r),
              (2-p1p, 1-p4p+r, 2-p1, 1-p4-r, 1-q, -r),
              (2-p1, 1-p4, 3-p1p, 4-p4p, 1-q, 1-r),
              (2-p1, 1-p4, 3-p1p, 4-p4p, 2-q, 1-r))
    return tuple(value % 5 for value in images[index])


def native_step(checkpoint):
    # theta_0 = binary_digit_sum(0) mod 2 = 0.
    selector = sum(checkpoint) % 5
    return original_generator(selector, checkpoint), selector


def endpoints(s, t):
    input_labels = [0]*17
    input_labels[0], input_labels[1], input_labels[6] = 1, t, s
    r1, selected_r1 = native_step(tuple(input_labels[2:8]))
    r2_native = list(input_labels[8:14])
    r2_native[4] = (r2_native[4]+1) % 5
    r2, selected_r2 = native_step(tuple(r2_native))
    r2_physical = list(r2)
    r2_physical[4] = (r2_physical[4]-1) % 5
    output_labels = input_labels[:]
    output_labels[2:8] = r1
    output_labels[8:14] = r2_physical
    output_labels[14:17] = (selected_r1, selected_r2, 1)
    return tuple(input_labels), tuple(output_labels)


def register_audit(operations):
    output_states = {}
    omitted_success = 0
    for sigma in (-1, 1):
        compiled = []
        omitted = []
        for operation in operations:
            ions = (operation[1],) if operation[0] == "carrier" else operation[1:3]
            compiled.append((ions, local_matrix(operation, sigma)))
            omitted.append((ions, local_matrix(operation, sigma, True)))
        # Explicit transpose-conjugation of the compiled matrices, followed
        # by reversed operator order; never invert a desired target table.
        inverse = [(ions, adjoint(matrix)) for ions, matrix in reversed(compiled)]
        for s, t in product(range(5), repeat=2):
            input_labels, output_labels = endpoints(s, t)
            state = {input_labels: ONE}
            for ions, matrix in compiled:
                state = tensor_apply(state, ions, matrix)
            assert state == {output_labels: ONE}
            output_states[s, t] = output_labels
            for ions, matrix in inverse:
                state = tensor_apply(state, ions, matrix)
            assert state == {input_labels: ONE}
            state = {input_labels: ONE}
            for ions, matrix in omitted:
                state = tensor_apply(state, ions, matrix)
            success = state == {output_labels: ONE}
            assert not success
            if sigma == 1:
                omitted_success += success
    assert len(set(output_states.values())) == 25
    for t in range(5):
        third, fourth = output_states[3, t], output_states[4, t]
        assert third[:14] == fourth[:14]
        assert third[14] == 3 and fourth[14] == 4
        assert third[15:] == fourth[15:]
    return omitted_success


def resource_audit(program, operations):
    word = [primitive for operation in operations for primitive in compile_operation(operation)]
    exponents = Counter()
    direct_carriers = 0
    direct_angle = 0
    for operation in word:
        if operation[0] == "G":
            _, first, second = operation
            assert 14 in (first, second)
            endpoint = second if first == 14 else first
            assert endpoint in range(2, 8)
            exponents[endpoint] += 1
        else:
            direct_carriers += 1
            direct_angle += operation[3]
    g_blocks = sum(exponents.values())
    assert g_blocks == 64
    assert [exponents[k] for k in range(2, 8)] == [4, 4, 16, 16, 20, 4]
    assert program["gamma_edges"] == [[14, k, exponents[k]] for k in range(2, 8)]
    carrier_pulses = 61200*g_blocks+direct_carriers
    carrier_angle_pi = Fraction(61200*g_blocks) + Fraction(direct_angle, 4)
    ls_loops = 500*g_blocks
    switching_boundaries = carrier_pulses+ls_loops+1
    bounds = program["bounds"]
    assert g_blocks == bounds["g_blocks"] == 64
    assert ls_loops == bounds["ls_loops"] == 32000
    assert carrier_pulses <= bounds["carrier_pulses"] == 3917023
    assert carrier_angle_pi <= bounds["carrier_angle_pi"] == 3916995
    assert switching_boundaries <= bounds["switching_boundaries"] == 3949024
    assert bounds["omitted_ls_success"] == 0
    return {"g_blocks": g_blocks, "ls_loops": ls_loops,
            "carrier_pulses": carrier_pulses,
            "carrier_angle_pi": str(carrier_angle_pi),
            "switching_boundaries": switching_boundaries,
            "gamma_exponents": [exponents[k] for k in range(2, 8)]}


def main():
    program = json.loads(Path(__file__).with_name("PROGRAM.json").read_text(encoding="utf-8"))
    assert program["schema"] == "ion-native-compression-v1"
    assert program["ions"] == 17 and program["angle_unit"] == "pi/4"
    assert program["chronological"] is True
    operations = tuple(freeze_lists(operation) for operation in program["operations"])
    assert operations[:4] == tuple(("exchange", 6, 14, k) for k in range(1, 5))
    assert len(operations) == 22
    # Elementary adjoints are audited before their use in every frame.
    primitives = {(step[2], step[3], step[4]) for op in operations
                  for step in compile_operation(op) if step[0] == "R"}
    for level, angle, phase in primitives:
        matrix = carrier_matrix(level, angle, phase)
        assert carrier_matrix(level, angle, (phase+2) % 4) == adjoint(matrix)
        assert matrix_product(adjoint(matrix), matrix) == identity(5)
    lengths = affine_audit()
    echo_rows = echo_audit(lengths)
    exchange_columns, mask_columns, single_columns = helper_audit(operations)
    omitted_success = register_audit(operations)
    summary = resource_audit(program, operations)
    summary.update(status="PASS", actual_inputs=25, exchange_columns=exchange_columns,
                   mask_columns=mask_columns, single_columns=single_columns,
                   echo_rows=echo_rows, omitted_ls_success=omitted_success)
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
