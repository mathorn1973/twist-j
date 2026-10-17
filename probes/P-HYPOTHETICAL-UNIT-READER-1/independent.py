#!/usr/bin/env python3
"""Exact independent audit for P-HYPOTHETICAL-UNIT-READER-1.

The complete update is implemented using a cyclic coordinate, not a
case-by-case stock-transfer implementation. This file has no dependency on
the primary program, model module, external files, or external inputs.
Execution is reserved for the publicly pinned audit.
"""

from hashlib import sha256
from itertools import product
import json


PROBE = "P-HYPOTHETICAL-UNIT-READER-1"
CUTOFF = 8


def zero_errors(state):
    """The three stored zero flags may initially be wrong."""
    return (
        state[5] ^ int(state[0] == 0),
        state[6] ^ int(state[1] == 0),
        state[7] ^ int(state[2] == 0),
    )


def cyclic_move(stock, receiver, direction, increment):
    """A fixed-total pair is one cycle of length 2(total+1)."""
    total = stock + receiver
    circumference = 2 * (total + 1)
    coordinate = receiver if direction == 1 else 2 * total + 1 - receiver
    coordinate = (coordinate + increment) % circumference
    if coordinate <= total:
        new_receiver = coordinate
        new_direction = 1
    else:
        new_receiver = 2 * total + 1 - coordinate
        new_direction = -1
    return total - new_receiver, new_receiver, new_direction


def evolve(state, reverse=False):
    """The inverse recovers the contact from the stored output phase."""
    active = 1 - state[9] if reverse else state[9]
    result = list(state)
    if state[10 + active]:
        old_stock, old_receiver = state[active], state[2]
        new_stock, new_receiver, new_direction = cyclic_move(
            old_stock,
            old_receiver,
            state[3 + active],
            -1 if reverse else 1,
        )
        result[active] = new_stock
        result[2] = new_receiver
        result[3 + active] = new_direction
        result[5 + active] = (
            state[5 + active]
            ^ int(old_stock == 0)
            ^ int(new_stock == 0)
        )
        result[7] = (
            state[7]
            ^ int(old_receiver == 0)
            ^ int(new_receiver == 0)
        )
        result[8] = (state[8] + new_receiver - old_receiver) % 5
    result[9] = 1 - state[9]
    return tuple(result)


def current(post_state):
    """Read the previous receiver increment from the local stored flags."""
    active = 1 - post_state[9]
    if post_state[10 + active] == 0:
        return 0
    if post_state[3 + active] == 1 and post_state[7] == 0:
        return 1
    if post_state[3 + active] == -1 and post_state[5 + active] == 0:
        return -1
    return 0


def prepare(a, b, receiver, contacts=(1, 1)):
    return (
        a, b, receiver, 1, 1,
        int(a == 0), int(b == 0), int(receiver == 0),
        receiver % 5, 0, contacts[0], contacts[1],
    )


def enumerate_states():
    for total in range(CUTOFF + 1):
        for first in range(total + 1):
            for second in range(total - first + 1):
                receiver = total - first - second
                for directions in product((-1, 1), repeat=2):
                    for flags in product((0, 1), repeat=3):
                        for pointer in range(5):
                            for phase in range(2):
                                for contacts in product((0, 1), repeat=2):
                                    yield (
                                        (first, second, receiver)
                                        + directions + flags
                                        + (pointer, phase) + contacts
                                    )


def audit_complete_domain():
    digest = sha256()
    count = 0
    calibrated = 0
    for state in enumerate_states():
        after = evolve(state)
        digest.update(
            (" ".join(map(str, state + after)) + "\n").encode("ascii")
        )
        assert evolve(after, reverse=True) == state
        assert evolve(evolve(state, reverse=True)) == state
        assert min(after[:3]) >= 0
        assert sum(after[:3]) == sum(state[:3])
        assert (after[8] - after[2]) % 5 == (state[8] - state[2]) % 5
        assert zero_errors(after) == zero_errors(state)
        active = state[9]
        inactive = 1 - active
        assert after[3 + inactive] == state[3 + inactive]
        assert after[5 + inactive] == state[5 + inactive]
        assert after[inactive] == state[inactive]
        assert after[10:] == state[10:]
        assert after[9] == 1 - state[9]
        increment = after[2] - state[2]
        assert increment in (-1, 0, 1)
        if state[10 + active] == 0:
            assert after[:9] == state[:9]
            assert current(after) == 0
        if zero_errors(state) == (0, 0, 0):
            assert current(after) == increment
            calibrated += 1
        count += 1
    assert count == 211200
    assert calibrated == 26400
    return count, calibrated, digest.hexdigest()


def audit_two_writes():
    count = 0
    for first in (0, 1):
        for second in (0, 1):
            for initial_receiver in (0, 1, 2):
                initial = prepare(first, second, initial_receiver)
                one = evolve(initial)
                two = evolve(one)
                assert one[2] == initial_receiver + first
                assert two[2] == initial_receiver + first + second
                assert current(one) == first
                assert current(two) == second
                assert two[:2] == (0, 0)
                assert two[8] == two[2]
                assert two[3:5] == (
                    1 if first == 1 else -1,
                    1 if second == 1 else -1,
                )
                assert zero_errors(two) == (0, 0, 0)
                count += 1
    assert count == 12
    return count


def audit_context():
    initials = (prepare(1, 0, 1), prepare(0, 1, 1))
    middles = tuple(evolve(state) for state in initials)
    finals = tuple(evolve(state) for state in middles)
    same_indices = (0, 1, 2, 5, 6, 7, 8, 9, 10, 11)
    assert tuple(finals[0][i] for i in same_indices) == tuple(
        finals[1][i] for i in same_indices
    )
    last = [end[2] - middle[2] for middle, end in zip(middles, finals)]
    assert last == [0, 1]
    assert [current(state) for state in finals] == last
    directions = [list(state[3:5]) for state in finals]
    assert directions == [[1, -1], [-1, 1]]
    assert finals[0][:3] == (0, 0, 2)
    assert finals[0][8] == 2
    return {
        "stocks": list(finals[0][:3]),
        "pointer": finals[0][8],
        "last": last,
        "directions": directions,
    }


def audit_fault():
    initial = (0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1)
    after = evolve(initial)
    actual = after[2] - initial[2]
    reading = current(after)
    errors = list(zero_errors(after))
    assert actual == 0
    assert reading == -1
    assert errors == [1, 0, 0]
    assert zero_errors(initial) == zero_errors(after)
    return {"actual": actual, "read": reading, "errors": errors}


def profile_coefficients(state):
    """Return (constant, coefficient of c) in the stock-only energy."""
    return (
        sum(value - value % 2 for value in state[:3]),
        sum(value % 2 for value in state[:3]),
    )


def audit_energy():
    initials = (
        (3, 2, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1),
        (2, 3, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1),
    )
    finals = tuple(evolve(state) for state in initials)
    assert sum(initials[0][:3]) == sum(initials[1][:3]) == 6
    assert initials[0][3:] == initials[1][3:]
    assert finals[0][3:] == finals[1][3:]
    assert profile_coefficients(initials[0]) == (4, 2)
    assert profile_coefficients(initials[1]) == (4, 2)
    assert finals[0][:3] == (2, 2, 2)
    assert finals[1][:3] == (1, 3, 2)
    defects = []
    for before, after in zip(initials, finals):
        old = profile_coefficients(before)
        new = profile_coefficients(after)
        defects.append([new[0] - old[0], new[1] - old[1]])
    assert defects == [[2, -2], [0, 0]]
    return defects


def audit_cycle():
    initial = (2, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1)
    states = [initial]
    increments = []
    for _ in range(12):
        after = evolve(states[-1])
        increments.append(after[2] - states[-1][2])
        assert current(after) == increments[-1]
        states.append(after)
    assert states[-1] == initial
    assert len(set(states[:-1])) == 12
    assert increments == [1, 1, 1, 0, 0, -1, -1, -1, -1, 0, 0, 1]
    return {
        "states": [list(state) for state in states],
        "currents": increments,
        "period": len(states) - 1,
    }


def disconnected_projection(state):
    return (
        state[2], state[4], state[6], state[7],
        state[8], state[9], state[10], state[11],
    )


def audit_disconnected():
    pairs = 0
    observations = 0
    for second in (0, 1):
        for initial_receiver in (0, 1, 2):
            left = prepare(0, second, initial_receiver, contacts=(0, 1))
            right = prepare(3, second, initial_receiver, contacts=(0, 1))
            for observation in range(13):
                assert disconnected_projection(left) == disconnected_projection(right)
                observations += 1
                if observation < 12:
                    old_left, old_right = left, right
                    left, right = evolve(left), evolve(right)
                    if old_left[9] == 0:
                        assert left[2] == old_left[2]
                        assert right[2] == old_right[2]
                        assert current(left) == current(right) == 0
            pairs += 1
    assert pairs == 6
    assert observations == 78
    return pairs, observations


def main():
    states, calibrated, transition_hash = audit_complete_domain()
    two_write_preparations = audit_two_writes()
    context = audit_context()
    fault = audit_fault()
    energy_defects = audit_energy()
    cycle = audit_cycle()
    disconnected_pairs, disconnected_observations = audit_disconnected()
    report = {
        "probe": PROBE,
        "cutoff": CUTOFF,
        "states": states,
        "calibrated_states": calibrated,
        "transition_sha256": transition_hash,
        "two_write_preparations": two_write_preparations,
        "context": context,
        "fault": fault,
        "energy_defects": energy_defects,
        "cycle": cycle,
        "disconnected_pairs": disconnected_pairs,
        "disconnected_observations": disconnected_observations,
    }
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
