# Copyright 2026 A. M. Thorn
# SPDX-License-Identifier: Apache-2.0

"""Independent exact matrix check of the affine semantic construction.

No previous probe implementation is imported. Native generators, preparation,
and readout are represented by literal affine matrices over F5. Tail closure
under both possible control bits proves the continuation for every later time.
"""

from collections import Counter
from itertools import product
import json


BLANK = -1

# Each last column is the affine constant; native coordinate order is a,b,c,d,q,r.
GENERATORS = (
    (
        (0, 1, 0, 0, 0, 0, 0),
        (1, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0, 1, 0),
    ),
    (
        (0, 0, 4, 0, 0, 0, 0),
        (0, 0, 0, 4, 0, 0, 0),
        (4, 0, 0, 0, 0, 0, 0),
        (0, 4, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 4, 0, 0),
        (0, 0, 0, 0, 0, 4, 0),
    ),
    (
        (0, 0, 4, 0, 0, 0, 2),
        (0, 0, 0, 4, 0, 1, 1),
        (4, 0, 0, 0, 0, 0, 2),
        (0, 4, 0, 0, 0, 4, 1),
        (0, 0, 0, 0, 4, 0, 1),
        (0, 0, 0, 0, 0, 4, 0),
    ),
    (
        (4, 0, 0, 0, 0, 0, 2),
        (0, 4, 0, 0, 0, 0, 1),
        (0, 0, 4, 0, 0, 0, 3),
        (0, 0, 0, 4, 0, 0, 4),
        (0, 0, 0, 0, 4, 0, 1),
        (0, 0, 0, 0, 0, 4, 1),
    ),
    (
        (4, 0, 0, 0, 0, 0, 2),
        (0, 4, 0, 0, 0, 0, 1),
        (0, 0, 4, 0, 0, 0, 3),
        (0, 0, 0, 4, 0, 0, 4),
        (0, 0, 0, 0, 4, 0, 2),
        (0, 0, 0, 0, 0, 4, 1),
    ),
)

# Columns lambda, mu, constant. This expands r=3(1+mu-lambda).
PREPARATION = (
    (0, 3, 0),
    (0, 0, 3),
    (0, 3, 0),
    (0, 0, 2),
    (3, 1, 4),
    (2, 3, 3),
)

# X=a+b+c-d-1 and H=2a+b+d+q+r-2.
READOUT = (
    (1, 1, 1, 4, 0, 0, 4),
    (2, 1, 0, 1, 1, 1, 3),
)


def affine(matrix, coordinates):
    augmented = tuple(coordinates) + (1,)
    assert all(len(row) == len(augmented) for row in matrix)
    return tuple(sum(coefficient * value for coefficient, value in zip(row, augmented)) % 5
                 for row in matrix)


def theta(time):
    """Canon control bit: finite binary digit sum modulo two."""
    assert time >= 0
    parity = 0
    while time:
        parity ^= time % 2
        time //= 2
    return parity


def advance(state, control):
    assert control in (0, 1)
    selector = (sum(state) + 2 * control) % 5
    return affine(GENERATORS[selector], state), selector


def decode(pair):
    position, height = pair
    return BLANK if height == 0 else height * height * position % 5


def tail_label(state):
    """Select the tail by native equations, returning its label or None."""
    a, b, c, d, q, r = state
    sum_ac = (a + c) % 5
    sum_bd = (b + d) % 5
    difference_ac = (a - c - 2) % 5
    difference_bd = (b - d - 1) % 5
    total = (a + b + c + d + q + r) % 5
    if (sum_bd == 0 and difference_bd == 0
            and difference_ac in (2, 3) and total in (1, 4)):
        return 2 * sum_ac * difference_ac * total % 5
    return None


def run():
    """Return (sorted flat state+label+X+H rows, stable count dictionary)."""
    blank_states = {}
    first_states = {}
    observed_tail = set()
    all_observed = set()
    actual_edges = 0
    actual_outputs = 0
    resets = 0
    preparation_count = 0
    for lam, mu in product(range(5), repeat=2):
        preparation_count += 1
        initial = affine(PREPARATION, (lam, mu))
        state = initial
        trajectory = [state]
        selectors = []
        for time in range(8):
            state, selector = advance(state, theta(time))
            actual_edges += 1
            selectors.append(selector)
            trajectory.append(state)
        assert tuple(selectors[:3]) == (2, 2, 4)
        assert trajectory[2] == initial
        resets += 1
        assert initial not in blank_states
        assert trajectory[1] not in first_states
        blank_states[initial] = BLANK
        first_states[trajectory[1]] = lam
        for time, state in enumerate(trajectory):
            wanted = BLANK if time in (0, 2) else lam if time == 1 else mu
            assert decode(affine(READOUT, state)) == wanted, ("prefix output", lam, mu, time)
            actual_outputs += 1
            all_observed.add(state)
            if time >= 3:
                assert tail_label(state) == mu, ("prefix tail label", lam, mu, time)
            if time in (3, 4, 7, 8):
                observed_tail.add(state)

    scanned_states = 0
    tail_states = {}
    for state in product(range(5), repeat=6):
        scanned_states += 1
        label = tail_label(state)
        if label is not None:
            tail_states[state] = label
    assert scanned_states == 15625
    assert len(tail_states) == 100
    assert Counter(tail_states.values()) == Counter({mu: 20 for mu in range(5)})
    assert observed_tail == set(tail_states)

    tail_edges = 0
    for state, label in tail_states.items():
        assert decode(affine(READOUT, state)) == label
        for control in (0, 1):
            successor, _selector = advance(state, control)
            assert successor in tail_states, ("tail closure", state, control)
            assert tail_states[successor] == label, ("tail label change", state, control)
            assert decode(affine(READOUT, successor)) == label
            tail_edges += 1
    assert tail_edges == 200

    blank_set = set(blank_states)
    first_set = set(first_states)
    tail_set = set(tail_states)
    assert len(blank_set) == len(first_set) == 25
    assert not blank_set.intersection(first_set)
    assert not blank_set.intersection(tail_set)
    assert not first_set.intersection(tail_set)
    domain = {**blank_states, **first_states, **tail_states}
    assert len(domain) == 150
    assert all_observed == set(domain)
    assert Counter(domain.values()) == Counter({label: 25 for label in range(-1, 5)})

    rows = []
    output_labels = {}
    for state, label in sorted(domain.items()):
        pair = affine(READOUT, state)
        assert decode(pair) == label
        if pair in output_labels:
            assert output_labels[pair] == label, ("cross-label collision", state)
        output_labels[pair] = label
        rows.append(state + (label,) + pair)
    assert set(output_labels) == set(product(range(5), repeat=2))
    unequal_label_pairs = 0
    for index, left in enumerate(rows):
        for right in rows[index + 1:]:
            if left[6] != right[6]:
                unequal_label_pairs += 1
                assert left[7:] != right[7:]
    assert unequal_label_pairs == 9375

    counts = {
        "native_states_scanned": scanned_states,
        "preparations": preparation_count,
        "actual_prefix_edges": actual_edges,
        "actual_prefix_output_checks": actual_outputs,
        "prefix_resets": resets,
        "blank_states": len(blank_states),
        "first_states": len(first_states),
        "tail_states": len(tail_states),
        "actual_tail_coverage_states": len(observed_tail),
        "tail_edges": tail_edges,
        "domain_states": len(domain),
        "readout_pairs": len(output_labels),
        "unequal_label_state_pairs": unequal_label_pairs,
        "cross_label_collisions": 0,
        "decoder_mismatches": 0,
    }
    return rows, counts


if __name__ == "__main__":
    _rows, result = run()
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
