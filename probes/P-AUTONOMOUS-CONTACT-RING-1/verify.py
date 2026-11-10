#!/usr/bin/env python3
"""Exact primary audit of the frozen autonomous contact-ring contract.

Four-coefficient polynomial arithmetic. The independently authored breaker
is loaded only after this audit, and its complete report must agree.
"""

from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import sys
from fractions import Fraction
from functools import lru_cache
from pathlib import Path


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
RHO = (0, 0, 1, 0)
RHO_INVERSE = (0, 0, 0, 1)
TRANSITION = ((1, 2, 3, 4, 0, 5, 6, 7, 8), (5, 1, 2, 3, 4, 6, 7, 8, 0))


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def scale(k, x):
    return tuple(k * a for a in x)


def multiply(x, y):
    polynomial = [0] * 7
    for i, a in enumerate(x):
        for k, b in enumerate(y):
            polynomial[i + k] += a * b
    for degree in range(6, 3, -1):
        coefficient = polynomial[degree]
        for offset in range(1, 5):
            polynomial[degree - offset] -= coefficient
        polynomial[degree] = 0
    return tuple(polynomial[:4])


def conjugate(x):
    a, b, c, d = x
    return (a - b, -b, d - b, c - b)


def trace(x):
    return 4 * x[0] - x[1] - x[2] - x[3]


def residue(x):
    return sum(x) % 5


@lru_cache(maxsize=None)
def cell_account(x):
    h = multiply(x, conjugate(x))
    numerator = 5 * sum(a * a for a in x) - sum(x) ** 2
    assert numerator % 2 == 0
    q = numerator // 2
    assert trace(h) == numerator
    assert q >= 0 and 2 * q >= sum(a * a for a in x)
    assert (q == 0) == (x == ZERO)
    return h, q


def invariants(state):
    total = ZERO
    hermitian = ZERO
    account = 0
    for cell in state:
        total = add(total, cell)
        h, q = cell_account(cell)
        hermitian = add(hermitian, h)
        account += q
    assert trace(hermitian) == 2 * account
    return total, hermitian, account, tuple(residue(cell) for cell in state)


def admitted(x, y):
    return all((a - b) % 2 == 0 for a, b in zip(x, y))


def contact(x, y, inverse=False):
    if not admitted(x, y):
        return x, y
    total = add(x, y)
    rotated = multiply(RHO_INVERSE if inverse else RHO, sub(x, y))
    left = add(total, rotated)
    right = sub(total, rotated)
    assert all(a % 2 == 0 for a in left + right)
    return tuple(a // 2 for a in left), tuple(a // 2 for a in right)


def matching(state, bit, inverse=False):
    size = len(state)
    assert size >= 4 and size % 2 == 0 and bit in (0, 1)
    result = list(state)
    touched = set()
    for left in range(bit, size, 2):
        right = (left + 1) % size
        assert left not in touched and right not in touched
        touched.update((left, right))
        result[left], result[right] = contact(state[left], state[right], inverse)
    assert len(touched) == size
    return tuple(result)


def clock_bit(n):
    assert n >= 1
    valuation = 0
    while n % 2 == 0:
        valuation += 1
        n //= 2
    return int(valuation % 2 == 0)


def formula_state(size, shift, a, number):
    assert size >= 8 and size % 2 == 0 and shift % 2 == 0
    assert 0 <= number < 9
    state = [ZERO] * size
    if number == 0:
        entries = ((1, scale(2 * a, ONE)), (5, scale(-2 * a, ONE)))
    else:
        k = number if number <= 4 else number - 4
        rotation = ONE
        for _ in range(k):
            rotation = multiply(rotation, RHO)
        source = scale(a, add(ONE, rotation))
        receiver = scale(a, sub(ONE, rotation))
        if number <= 4:
            entries = ((0, receiver), (1, source),
                       (4, scale(-1, receiver)), (5, scale(-1, source)))
        else:
            entries = ((1, source), (2, receiver),
                       (5, scale(-1, source)), (6, scale(-1, receiver)))
    for index, cell in entries:
        state[(index + shift) % size] = cell
    return tuple(state)


def reader(cell):
    if cell == ZERO:
        return ["BLANK"]
    value = Fraction(trace(cell), 5)
    return ["VALUE", value.numerator, value.denominator]


def receivers(state, shift=0):
    return [reader(state[(shift + i) % len(state)]) for i in (0, 2, 4, 6)]


def check_formula_state(state, a, number, shift=0):
    total, hermitian, account, residues = invariants(state)
    assert total == ZERO
    assert hermitian == scale(8 * a * a, ONE)
    assert account == 16 * a * a
    assert residues == invariants(formula_state(len(state), shift, a, 0))[3]
    blank = ["BLANK"]
    positive = ["VALUE", a, 1]
    negative = ["VALUE", -a, 1]
    if number == 0:
        expected = [blank, blank, blank, blank]
    elif number <= 4:
        expected = [positive, blank, negative, blank]
    else:
        expected = [blank, positive, blank, negative]
    assert receivers(state, shift) == expected
    both = add(state[shift % len(state)], state[(shift + 2) % len(state)])
    assert reader(both) == (blank if number == 0 else positive)


def hash_row(digest, row):
    text = json.dumps(row, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    digest.update((text + "\n").encode("utf-8"))


def audit_pairs():
    cells = tuple(itertools.product((-1, 0, 1), repeat=4))
    digest = hashlib.sha256()
    cases = 0
    for x in cells:
        for y in cells:
            original = (x, y)
            output = contact(x, y)
            assert invariants(original) == invariants(output)
            assert admitted(*output) == admitted(x, y)
            assert contact(*output, inverse=True) == original
            four_from_output = output
            for _ in range(4):
                four_from_output = contact(*four_from_output)
                assert admitted(*four_from_output) == admitted(x, y)
                assert invariants(four_from_output) == invariants(original)
            # Four steps from C(x,y) are simultaneously C^4(C(x,y)) and C^5(x,y).
            assert four_from_output == original
            assert four_from_output == contact(*output, inverse=True)
            hash_row(digest, [x, y, int(admitted(x, y)), output[0], output[1]])
            cases += 1
    assert cases == 6561
    return cases, digest.hexdigest()


def audit_four_cells():
    alphabet = [ZERO]
    for index in range(4):
        unit = tuple(int(k == index) for k in range(4))
        alphabet.extend((unit, scale(-1, unit)))
    digest = hashlib.sha256()
    cases = 0
    for state in itertools.product(alphabet, repeat=4):
        before = invariants(state)
        for bit in (0, 1):
            after = matching(state, bit)
            assert invariants(after) == before
            assert matching(after, bit, inverse=True) == state
            hash_row(digest, [state, bit, after])
            cases += 1
    assert cases == 13122
    return cases, digest.hexdigest()


def audit_orbits():
    digest = hashlib.sha256()
    cases = 0
    for size in (8, 10, 12):
        for shift in range(0, size, 2):
            for a in range(-15, 16, 2):
                states = tuple(formula_state(size, shift, a, number) for number in range(9))
                assert len(set(states)) == 9
                for number, state in enumerate(states):
                    check_formula_state(state, a, number, shift)
                    before = invariants(state)
                    for bit in (0, 1):
                        after = matching(state, bit)
                        assert after == states[TRANSITION[bit][number]]
                        assert invariants(after) == before
                        assert matching(after, bit, inverse=True) == state
                        hash_row(digest, [size, shift, a, number, bit, state, after])
                        cases += 1
    assert cases == 4320
    return cases, digest.hexdigest()


def audit_histories():
    digest = hashlib.sha256()
    boundaries = 0
    for a in (-1, 1):
        state = formula_state(8, 0, a, 0)
        initial = state
        number = 0
        history = []
        for n in range(3, 260):
            assert state == formula_state(8, 0, a, number)
            check_formula_state(state, a, number)
            if n in (3, 10):
                assert state[2] == state[6] == ZERO
            if 4 <= n <= 9:
                assert reader(state[2]) == ["VALUE", a, 1]
                assert reader(state[6]) == ["VALUE", -a, 1]
            if n == 10:
                assert state == initial
            history.append(state)
            hash_row(digest, [a, n, number, state, receivers(state)])
            boundaries += 1
            if n < 259:
                bit = clock_bit(n)
                state = matching(state, bit)
                number = TRANSITION[bit][number]
        assert len(history) == 257
        for previous_n in range(258, 2, -1):
            state = matching(state, clock_bit(previous_n), inverse=True)
            assert state == history[previous_n - 3]
        assert state == initial
    assert boundaries == 514
    return boundaries, digest.hexdigest()


def audit_controls():
    digest = hashlib.sha256()
    initial = (ZERO,) * 8
    state = initial
    for n in range(3, 259):
        state = matching(state, clock_bit(n))
        assert state == initial
    hash_row(digest, ["zero", initial, state])
    initial = formula_state(8, 0, 2, 0)
    after_one = matching(initial, 1)
    after_zero = matching(after_one, 0)
    assert invariants(initial) == invariants(after_one) == invariants(after_zero)
    assert matching(after_zero, 0, inverse=True) == after_one
    assert matching(after_one, 1, inverse=True) == initial
    difference = sub(ONE, RHO)
    assert after_zero[3] == multiply(difference, difference) != ZERO
    assert all(after_zero != formula_state(8, 0, 2, k) for k in range(9))
    hash_row(digest, ["even", initial, after_one, after_zero])
    return 2, digest.hexdigest(), list(after_zero[3])


def audit_clock():
    bits = []
    for n in range(1, 8193):
        bit = clock_bit(n)
        assert bit == ((n - 1).bit_count() % 2) ^ (n.bit_count() % 2)
        bits.append(str(bit))
    word = "".join(bits)
    assert len(word) == 8192
    digest = hashlib.sha256((word + "\n").encode("ascii")).hexdigest()
    counts = []
    for length in range(1, 65):
        factors = {word[i:i + length] for i in range(len(word) - length + 1)}
        counts.append(len(factors))
        assert len(factors) <= 4 * length
    return len(word), digest, counts


def audit():
    assert __debug__, "Assertions must remain enabled"
    pair_cases, pair_digest = audit_pairs()
    ring_cases, ring_digest = audit_four_cells()
    orbit_cases, orbit_digest = audit_orbits()
    boundaries, trajectory_digest = audit_histories()
    control_cases, control_digest, even_z3 = audit_controls()
    clock_length, clock_digest, factor_counts = audit_clock()
    return {
        "probe": "P-AUTONOMOUS-CONTACT-RING-1",
        "pair_cases": pair_cases,
        "pair_sha256": pair_digest,
        "ring_cases": ring_cases,
        "ring_sha256": ring_digest,
        "orbit_cases": orbit_cases,
        "orbit_sha256": orbit_digest,
        "trajectory_boundaries": boundaries,
        "trajectory_sha256": trajectory_digest,
        "control_cases": control_cases,
        "control_sha256": control_digest,
        "even_control_z3": even_z3,
        "clock_length": clock_length,
        "clock_sha256": clock_digest,
        "factor_counts": factor_counts,
        "orbit_transition": [list(row) for row in TRANSITION],
        "primary_read_window": list(range(4, 10)),
        "erased_boundary": 10,
        "primary_account": 16,
        "native_bit_match": True,
    }


def main():
    primary = audit()
    path = Path(__file__).with_name("break.py")
    spec = importlib.util.spec_from_file_location("independent_contact_breaker", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    independent = module.audit()
    assert primary == independent, "Independent frozen audit reports disagree"
    output = {"independent_match": True, "report": primary, "status": "PASS"}
    print(json.dumps(output, sort_keys=True, separators=(",", ":"), ensure_ascii=True))


if __name__ == "__main__":
    main()
