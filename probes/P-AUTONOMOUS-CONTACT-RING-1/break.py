#!/usr/bin/env python3
"""NON-CANONICAL L1 independent audit of the frozen contact-ring contract.

This implementation uses five cyclic coefficients modulo j**5 = 1.
Subtracting the fifth coefficient from every coefficient chooses the unique
representative with fifth coefficient zero modulo 1+j+j**2+j**3+j**4.
No polynomial-reduction implementation or primary source is imported.
"""

from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from math import gcd


ZERO = (0, 0, 0, 0, 0)
ONE = (1, 0, 0, 0, 0)
TRANSITIONS = (
    (1, 2, 3, 4, 0, 5, 6, 7, 8),
    (5, 1, 2, 3, 4, 6, 7, 8, 0),
)


def normalize(coefficients):
    """Fix the additive constant-vector ambiguity of five coefficients."""
    coefficients = tuple(coefficients)
    assert len(coefficients) == 5
    assert all(type(coefficient) is int for coefficient in coefficients)
    last = coefficients[4]
    return tuple(coefficient - last for coefficient in coefficients)


def from_four(coefficients):
    coefficients = tuple(coefficients)
    assert len(coefficients) == 4
    return normalize(coefficients + (0,))


def to_four(cell):
    return normalize(cell)[:4]


def scalar(value):
    assert type(value) is int
    return (value, 0, 0, 0, 0)


def plus(left, right):
    return normalize(a + b for a, b in zip(left, right))


def minus(left, right):
    return normalize(a - b for a, b in zip(left, right))


def times_integer(multiplier, cell):
    assert type(multiplier) is int
    return normalize(multiplier * coefficient for coefficient in cell)


def shift(cell, exponent):
    """Multiplication by j**exponent in the five-term cyclic group ring."""
    result = [0] * 5
    for index, coefficient in enumerate(cell):
        result[(index + exponent) % 5] = coefficient
    return normalize(result)


def times(left, right):
    """Five-term cyclic convolution, followed only by gauge normalization."""
    result = [0] * 5
    for left_index, left_coefficient in enumerate(left):
        for right_index, right_coefficient in enumerate(right):
            result[(left_index + right_index) % 5] += (
                left_coefficient * right_coefficient
            )
    return normalize(result)


def conjugate(cell):
    result = [0] * 5
    for index, coefficient in enumerate(cell):
        result[(-index) % 5] = coefficient
    return normalize(result)


def trace(cell):
    return 5 * cell[0] - sum(cell)


def half(cell):
    cell = normalize(cell)
    assert all(coefficient % 2 == 0 for coefficient in cell)
    return normalize(coefficient // 2 for coefficient in cell)


def parity(cell):
    return tuple(coefficient % 2 for coefficient in to_four(cell))


@lru_cache(maxsize=None)
def cell_account(cell):
    """Validate every actual cell and return its full h, q and residue."""
    assert cell == normalize(cell)
    coefficients = to_four(cell)
    numerator = 5 * sum(coefficient * coefficient for coefficient in cell)
    numerator -= sum(cell) ** 2
    assert numerator % 2 == 0
    account = numerator // 2
    hermitian = times(cell, conjugate(cell))
    hermitian_trace = trace(hermitian)
    assert hermitian_trace % 2 == 0
    assert account == hermitian_trace // 2
    assert account >= 0
    assert 2 * account >= sum(coefficient * coefficient for coefficient in coefficients)
    residue = sum(coefficients) % 5
    return hermitian, account, residue


def signature(state):
    """Complete sum, Hermitian account, half trace and labelled residues."""
    total = ZERO
    hermitian = ZERO
    account = 0
    residues = []
    for cell in state:
        cell_h, cell_q, cell_r = cell_account(cell)
        total = plus(total, cell)
        hermitian = plus(hermitian, cell_h)
        account += cell_q
        residues.append(cell_r)
    assert trace(hermitian) % 2 == 0
    assert account == trace(hermitian) // 2
    return total, hermitian, account, tuple(residues)


def accepted(left, right):
    return parity(minus(left, right)) == (0, 0, 0, 0)


def contact(left, right, backward=False):
    before = (left, right)
    admitted = accepted(left, right)
    old_parity = parity(minus(left, right))
    if admitted:
        total = plus(left, right)
        difference = minus(left, right)
        # rho = j**2 and rho**4 = j**8 = j**3.
        turned = shift(difference, 3 if backward else 2)
        after = (half(plus(total, turned)), half(minus(total, turned)))
    else:
        after = before
    assert signature(after) == signature(before)
    assert parity(minus(*after)) == old_parity
    assert accepted(*after) == admitted
    return after


def matching(state, bit, backward=False):
    size = len(state)
    assert size >= 4 and size % 2 == 0
    assert bit in (0, 1)
    result = list(state)
    assigned = set()
    for left in range(bit, size, 2):
        right = (left + 1) % size
        assert left not in assigned and right not in assigned
        assigned.update((left, right))
        # Both arguments come from the immutable old state.
        result[left], result[right] = contact(
            state[left], state[right], backward=backward
        )
    assert assigned == set(range(size))
    result = tuple(result)
    assert signature(result) == signature(state)
    return result


def reader(cell):
    cell_account(cell)
    if normalize(cell) == ZERO:
        return ["BLANK"]
    numerator = trace(cell)
    common = gcd(abs(numerator), 5)
    return ["VALUE", numerator // common, 5 // common]


def serialized_state(state):
    return [list(to_four(cell)) for cell in state]


def json_line(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ) + "\n"


def hash_row(digest, value):
    digest.update(json_line(value).encode("utf-8"))


def formula_states(size, translation, amplitude):
    """Construct the nine frozen formulas without calling a contact map."""
    assert size >= 8 and size % 2 == 0
    assert 0 <= translation < size and translation % 2 == 0
    assert type(amplitude) is int and amplitude != 0

    def placed(entries):
        state = [ZERO] * size
        for address, value in entries:
            state[(address + translation) % size] = value
        return tuple(state)

    base = placed(((1, scalar(2 * amplitude)), (5, scalar(-2 * amplitude))))
    left_states = []
    right_states = []
    for exponent in range(1, 5):
        root_power = shift(ONE, 2 * exponent)
        a_cell = times_integer(amplitude, plus(ONE, root_power))
        d_cell = times_integer(amplitude, minus(ONE, root_power))
        left_states.append(placed((
            (0, d_cell), (1, a_cell),
            (4, times_integer(-1, d_cell)),
            (5, times_integer(-1, a_cell)),
        )))
        right_states.append(placed((
            (1, a_cell), (2, d_cell),
            (5, times_integer(-1, a_cell)),
            (6, times_integer(-1, d_cell)),
        )))
    return (base,) + tuple(left_states) + tuple(right_states)


def fixed_readers(state, translation):
    size = len(state)
    return [reader(state[(translation + offset) % size]) for offset in (0, 2, 4, 6)]


def check_formula_state(state, number, translation, amplitude, residues):
    total, hermitian, account, current_residues = signature(state)
    assert total == ZERO
    assert hermitian == scalar(8 * amplitude * amplitude)
    assert account == 16 * amplitude * amplitude
    assert current_residues == residues
    blank = ["BLANK"]
    positive = ["VALUE", amplitude, 1]
    negative = ["VALUE", -amplitude, 1]
    if number == 0:
        expected_readers = [blank, blank, blank, blank]
        expected_sum_reader = blank
    elif 1 <= number <= 4:
        expected_readers = [positive, blank, negative, blank]
        expected_sum_reader = positive
    else:
        assert 5 <= number <= 8
        expected_readers = [blank, positive, blank, negative]
        expected_sum_reader = positive
    assert fixed_readers(state, translation) == expected_readers
    size = len(state)
    first_two = plus(state[translation], state[(translation + 2) % size])
    assert reader(first_two) == expected_sum_reader


def clock_bit(counter):
    assert type(counter) is int and counter >= 1
    valuation = 0
    remaining = counter
    while remaining % 2 == 0:
        remaining //= 2
        valuation += 1
    return int(valuation % 2 == 0)


def audit_pairs():
    digest = sha256()
    cells = tuple(from_four(c) for c in product((-1, 0, 1), repeat=4))
    assert len(cells) == 81
    count = 0
    for left in cells:
        for right in cells:
            initial = (left, right)
            admitted = accepted(left, right)
            after = contact(left, right)
            assert contact(*after, backward=True) == initial
            power = initial
            for _ in range(5):
                power = contact(*power)
            assert power == initial
            fourth_after = after
            for _ in range(4):
                fourth_after = contact(*fourth_after)
            assert fourth_after == initial
            fourth_initial = initial
            for _ in range(4):
                fourth_initial = contact(*fourth_initial)
            assert fourth_initial == contact(*initial, backward=True)
            hash_row(digest, [
                list(to_four(left)), list(to_four(right)), int(admitted),
                list(to_four(after[0])), list(to_four(after[1])),
            ])
            count += 1
    assert count == 6561
    # Admission includes the unchanged equal-cell branch.
    assert accepted(ONE, ONE)
    assert contact(ONE, ONE) == (ONE, ONE)
    return count, digest.hexdigest()


def audit_matchings():
    digest = sha256()
    alphabet = (
        ZERO, ONE, scalar(-1), shift(ONE, 1), shift(scalar(-1), 1),
        shift(ONE, 2), shift(scalar(-1), 2),
        shift(ONE, 3), shift(scalar(-1), 3),
    )
    assert len(set(alphabet)) == 9
    count = 0
    for initial in product(alphabet, repeat=4):
        for bit in (0, 1):
            after = matching(initial, bit)
            assert matching(after, bit, backward=True) == initial
            hash_row(digest, [serialized_state(initial), bit, serialized_state(after)])
            count += 1
    assert count == 13122
    return count, digest.hexdigest()


def audit_nine_states():
    digest = sha256()
    count = 0
    for size in (8, 10, 12):
        for translation in range(0, size, 2):
            for amplitude in range(-15, 16, 2):
                assert amplitude != 0 and amplitude % 2 == 1
                states = formula_states(size, translation, amplitude)
                assert len(states) == 9 and len(set(states)) == 9
                initial = states[0]
                source_addresses = {(translation + 1) % size, (translation + 5) % size}
                assert all(
                    cell == ZERO for address, cell in enumerate(initial)
                    if address not in source_addresses
                )
                assert initial[(translation + 1) % size] == scalar(2 * amplitude)
                assert initial[(translation + 5) % size] == scalar(-2 * amplitude)
                residues = signature(initial)[3]
                for number in range(9):
                    before = states[number]
                    check_formula_state(before, number, translation, amplitude, residues)
                    for bit in (0, 1):
                        after = matching(before, bit)
                        target_number = TRANSITIONS[bit][number]
                        assert after == states[target_number]
                        check_formula_state(
                            after, target_number, translation, amplitude, residues
                        )
                        assert matching(after, bit, backward=True) == before
                        hash_row(digest, [
                            size, translation, amplitude, number, bit,
                            serialized_state(before), serialized_state(after),
                        ])
                        count += 1
    assert count == 4320
    return count, digest.hexdigest()


def audit_histories():
    digest = sha256()
    count = 0
    accounts = []
    windows = []
    for amplitude in (-1, 1):
        states = formula_states(8, 0, amplitude)
        initial = states[0]
        residues = signature(initial)[3]
        accounts.append(signature(initial)[2])
        state = initial
        number = 0
        history = []
        early_read_window = []
        for counter in range(3, 260):
            assert state == states[number]
            check_formula_state(state, number, 0, amplitude, residues)
            readings = fixed_readers(state, 0)
            if counter in (3, 10):
                assert state[2] == ZERO and state[6] == ZERO
            if 4 <= counter <= 9:
                assert reader(state[2]) == ["VALUE", amplitude, 1]
                assert reader(state[6]) == ["VALUE", -amplitude, 1]
            if 3 <= counter <= 10 and reader(state[2]) == ["VALUE", amplitude, 1]:
                early_read_window.append(counter)
            if counter == 10:
                assert state == initial
                assert counter != 3
            hash_row(digest, [amplitude, counter, number, serialized_state(state), readings])
            history.append((counter, state))
            count += 1
            if counter != 259:
                bit = clock_bit(counter)
                state = matching(state, bit)
                number = TRANSITIONS[bit][number]
        assert len(history) == 257
        assert early_read_window == [4, 5, 6, 7, 8, 9]
        windows.append(early_read_window)
        backward_counter = 259
        recovered_steps = 0
        for previous_counter, previous_state in reversed(history[:-1]):
            assert backward_counter == previous_counter + 1
            state = matching(state, clock_bit(previous_counter), backward=True)
            backward_counter -= 1
            assert backward_counter == previous_counter
            assert state == previous_state
            recovered_steps += 1
        assert recovered_steps == 256
        assert backward_counter == 3 and state == initial
    assert count == 514
    assert accounts == [16, 16]
    assert windows[0] == windows[1]
    return count, digest.hexdigest(), accounts[0], windows[0]


def audit_controls():
    digest = sha256()
    initial_zero = (ZERO,) * 8
    state = initial_zero
    for counter in range(3, 259):
        assert state == initial_zero
        state = matching(state, clock_bit(counter))
        assert state == initial_zero
    hash_row(digest, ["zero", serialized_state(initial_zero), serialized_state(state)])

    even_states = formula_states(8, 0, 2)
    initial_even = even_states[0]
    after_one = matching(initial_even, 1)
    after_zero = matching(after_one, 0)
    one_minus_rho = minus(ONE, shift(ONE, 2))
    expected_leak = times(one_minus_rho, one_minus_rho)
    assert expected_leak != ZERO
    assert after_zero[3] == expected_leak
    assert all(after_zero != candidate for candidate in even_states)
    assert matching(after_zero, 0, backward=True) == after_one
    assert matching(after_one, 1, backward=True) == initial_even
    hash_row(digest, [
        "even", serialized_state(initial_even),
        serialized_state(after_one), serialized_state(after_zero),
    ])
    return 2, digest.hexdigest(), list(to_four(after_zero[3]))


def audit_clock():
    bits = []
    native_matches = []
    for counter in range(1, 8193):
        bit = clock_bit(counter)
        native = ((counter - 1).bit_count() % 2) ^ (counter.bit_count() % 2)
        native_matches.append(bit == native)
        assert bit == native
        bits.append(str(bit))
    word = "".join(bits)
    assert len(word) == 8192
    digest = sha256((word + "\n").encode("ascii")).hexdigest()
    counts = []
    for length in range(1, 65):
        factors = {
            word[start:start + length]
            for start in range(len(word) - length + 1)
        }
        count = len(factors)
        assert count <= 4 * length
        counts.append(count)
    assert len(counts) == 64
    assert all(native_matches)
    return len(word), digest, counts, all(native_matches)


def audit():
    assert __debug__, "Assertions must remain enabled."
    assert reader(ZERO) == ["BLANK"]
    assert reader(from_four((1, 4, 0, 0))) == ["VALUE", 0, 1]
    assert reader(ONE) == ["VALUE", 4, 5]
    assert reader(scalar(-1)) == ["VALUE", -4, 5]
    pair_count, pair_digest = audit_pairs()
    ring_count, ring_digest = audit_matchings()
    orbit_count, orbit_digest = audit_nine_states()
    boundary_count, trajectory_digest, primary_account, read_window = audit_histories()
    control_count, control_digest, even_z3 = audit_controls()
    clock_length, clock_digest, factor_counts, native_match = audit_clock()
    return {
        "probe": "P-AUTONOMOUS-CONTACT-RING-1",
        "pair_cases": pair_count,
        "pair_sha256": pair_digest,
        "ring_cases": ring_count,
        "ring_sha256": ring_digest,
        "orbit_cases": orbit_count,
        "orbit_sha256": orbit_digest,
        "trajectory_boundaries": boundary_count,
        "trajectory_sha256": trajectory_digest,
        "control_cases": control_count,
        "control_sha256": control_digest,
        "even_control_z3": even_z3,
        "clock_length": clock_length,
        "clock_sha256": clock_digest,
        "factor_counts": factor_counts,
        "orbit_transition": [list(row) for row in TRANSITIONS],
        "primary_read_window": read_window,
        "erased_boundary": 10,
        "primary_account": primary_account,
        "native_bit_match": native_match,
    }


if __name__ == "__main__":
    print(json.dumps(audit(), sort_keys=True, separators=(",", ":"), ensure_ascii=True))
