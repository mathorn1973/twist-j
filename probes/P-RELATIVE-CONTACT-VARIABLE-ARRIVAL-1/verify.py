#!/usr/bin/env python3
"""Exact, result-exposed confirmation of the declared ten-input apparatus.

No external packages, randomness, environment-dependent output or file writes.
Four-coefficient and independent cyclic five-coefficient contacts are compared
after every applied edge. The operation word never depends on an observation.
"""

from functools import lru_cache
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import re
import sys


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
WORD_SHA256 = "ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b"
EXPOSED_ENDPOINT_SHA256 = "a10212635f9c3a5079952aa7a46a24352f62c6506fcb43cc4c10295ea4d347e4"


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return add(a, neg(b))


def mul_j(a):
    x, y, z, t = a
    return (-t, x - t, y - t, z - t)


def rotate(a, k=1):
    for _ in range(2 * (k % 5)):
        a = mul_j(a)
    return a


def account(a):
    numerator = 5 * sum(x * x for x in a) - sum(a) ** 2
    assert numerator % 2 == 0
    return numerator // 2


def residue(a):
    return sum(a) % 5


@lru_cache(None)
def contact4(a, b):
    if any((x - y) % 2 for x, y in zip(a, b)):
        c, d = a, b
    else:
        center = tuple((x + y) // 2 for x, y in zip(a, b))
        half = tuple((x - y) // 2 for x, y in zip(a, b))
        turned = rotate(half)
        c, d = add(center, turned), sub(center, turned)
    assert add(c, d) == add(a, b)
    assert account(c) + account(d) == account(a) + account(b)
    assert (residue(c), residue(d)) == (residue(a), residue(b))
    return c, d


# Independent arithmetic: five cyclic coefficients, modulo a constant vector.
# This implementation has no four-coefficient contact or rotation calls.
def normalize5(a):
    minimum = min(a)
    return tuple(x - minimum for x in a)


def add5(a, b):
    return normalize5(tuple(x + y for x, y in zip(a, b)))


def sub5(a, b):
    return normalize5(tuple(x - y for x, y in zip(a, b)))


def account5(a):
    numerator = 5 * sum(x * x for x in a) - sum(a) ** 2
    assert numerator % 2 == 0
    return numerator // 2


@lru_cache(None)
def contact5(a, b):
    difference = sub5(a, b)
    if any(x % 2 for x in difference):
        c, d = a, b
    else:
        half = tuple(x // 2 for x in difference)
        turned = tuple(half[(i - 2) % 5] for i in range(5))
        delta = sub5(turned, half)
        c, d = add5(a, delta), sub5(b, delta)
    assert add5(c, d) == add5(a, b)
    assert account5(c) + account5(d) == account5(a) + account5(b)
    assert (sum(c) % 5, sum(d) % 5) == (sum(a) % 5, sum(b) % 5)
    return c, d


@lru_cache(None)
def lift5(a):
    return normalize5(a + (0,))


APPLICATIONS = 0


def apply_pair(state4, state5, edge):
    global APPLICATIONS
    i, j = edge
    state4[i], state4[j] = contact4(state4[i], state4[j])
    state5[i], state5[j] = contact5(state5[i], state5[j])
    assert state5[i] == lift5(state4[i])
    assert state5[j] == lift5(state4[j])
    APPLICATIONS += 1


def inverse(word):
    return tuple(edge for edge in reversed(word) for _ in range(4))


U = sub(ONE, rotate(ONE))  # Lower-case u in the mathematical specification.
W = add(ONE, rotate(ONE))
B = add(ONE, rotate(ONE, 2))
F = ((0, 1), (1, 2))
F_INVERSE = inverse(F)
T = ((3, 4),)
G, H, GATE, CLOCK = 5, 9, 10, 3
OPEN = ((1, G),)
A0 = ((G, H),)
OPEN2 = ((H, GATE),)


def enable(selector):
    contact = ((selector, H),)
    return A0 + contact + A0 * 4 + contact * 4


def disable(selector):
    contact = ((selector, H),)
    return contact + A0 + contact * 4 + A0 * 4


def scan(base):
    word = ()
    for p in range(5):
        a, b = base + 2 * p, base + 2 * p + 1
        opening = ((CLOCK, GATE),)
        writer = ((CLOCK, a),) * 4 + ((a, b),) * 4
        writer += ((CLOCK, a), (a, b))
        word += opening + writer + opening * 4 + T
    return word


def wrapper(selector, base):
    return enable(selector) + OPEN2 + scan(base) + OPEN2 * 4 + disable(selector)


def d_word(c, d):
    a, b = ((H, c),), ((H, d),)
    return a * 3 + b * 3 + a + b + a


def selector_word(c, d):
    d = d_word(c, d)
    return A0 + d + A0 * 4 + d


READ = OPEN + wrapper(6, 11) + wrapper(7, 21)
READ += selector_word(7, 8) + selector_word(6, 7) + OPEN * 4
S = READ + F_INVERSE + READ + F + F + T


def source_orbit():
    start = (ZERO, (2, 0, 0, 0), ZERO)
    state4 = list(start)
    state5 = list(map(lift5, start))
    orbit = []
    for _ in range(9):
        orbit.append(tuple(state4))
        for edge in F:
            apply_pair(state4, state5, edge)
    assert tuple(state4) == start and len(set(orbit)) == 9
    return tuple(orbit)


def state_for(orbit, source, clock, selector, codes):
    q = rotate(W, clock)
    token = tuple(U if i == selector else ZERO for i in range(3))
    state = orbit[source % 9] + (q, neg(q), ZERO) + token + (W, ZERO)
    for phase in codes:
        value = rotate(B, phase)
        state += (neg(value), value)
    return state


def invariants(state):
    total = ZERO
    for value in state:
        total = add(total, value)
    return sum(map(account, state)), total, tuple(map(residue, state))


def compact(value):
    return json.dumps(value, separators=(",", ":")).encode("utf-8")


def main():
    assert not sys.flags.optimize, "Assertions must remain enabled"
    assert len(READ) == 261 and len(S) == 535
    assert len(F_INVERSE) == 8
    word_bytes = Path(__file__).with_name("WORD535.txt").read_bytes()
    assert sha256(word_bytes).hexdigest() == WORD_SHA256
    literal = tuple((int(i) - 1, int(j) - 1)
                    for i, j in re.findall(r"C\((\d+),(\d+)\)", word_bytes.decode("ascii")))
    assert literal == S  # Includes chronological orientation, not only an edge set.
    orbit = source_orbit()
    preparations = tuple(state_for(orbit, n, k, 0, (0,) * 10)
                         for n, k in product(range(2), range(5)))
    assert len(set(preparations)) == 10
    assert len({state[5:] for state in preparations}) == 1
    assert len(preparations[0][5:]) == 26
    initial_residues = {invariants(state)[2] for state in preparations}
    assert len(initial_residues) == 1
    endpoints, records = [], []
    boundary_hash, read_hash = sha256(), sha256()
    boundary_count = read_count = event_count = inverse_count = 0
    start_applications = APPLICATIONS
    for n, k in product(range(2), range(5)):
        initial = state_for(orbit, n, k, 0, (0,) * 10)
        expected_invariants = invariants(initial)
        assert len(initial) == 31 and expected_invariants[:2] == (82, (4, 0, 0, 0))
        state4, state5 = list(initial), list(map(lift5, initial))
        codes, marks, events = [0] * 10, 0, []
        retained = [None, None]
        delta = 1 if n == 0 else 8
        for tick in range(10):
            phase, clock = (n + tick) % 9, (k + tick) % 5
            for index, edge in enumerate(S):
                prior_g = state4[G]
                apply_pair(state4, state5, edge)
                if index in (0, 269):
                    active = phase == (0 if index == 0 else 1)
                    assert prior_g == ZERO
                    assert state4[G] == (U if active else ZERO)
                    if active:
                        events.append({"tick": tick, "read": 1 if index == 0 else 2,
                                       "onset_contact": 535 * tick + index + 1,
                                       "completion_contact": 535 * tick + index + 261,
                                       "selector_before": marks % 3})
                        event_count += 1
                if index in (260, 529):
                    first = index == 260
                    active = phase == (0 if first else 1)
                    if active:
                        if marks < 2:
                            codes[5 * marks + (-clock) % 5] = 1
                        marks += 1
                    source = phase if first else (phase - 1) % 9
                    expected = state_for(orbit, source, clock, marks % 3, codes)
                    assert tuple(state4) == expected, (n, k, tick, index, "read state")
                    assert tuple(state5) == tuple(map(lift5, expected))
                    assert invariants(state4) == expected_invariants
                    read_hash.update(compact([n, k, tick, 1 if first else 2, state4]))
                    read_count += 1
            expected = state_for(orbit, phase + 1, clock + 1, marks % 3, codes)
            assert tuple(state4) == expected, (n, k, tick, "boundary state")
            assert invariants(state4) == expected_invariants
            for bank in range(2):
                archive = tuple(state4[11 + 10 * bank:21 + 10 * bank])
                if retained[bank] is not None:
                    assert archive == retained[bank]
                if marks > bank and retained[bank] is None:
                    retained[bank] = archive
            boundary_hash.update(compact([n, k, tick + 1, state4]))
            boundary_count += 1
        assert marks == 3 and len(events) == 3
        assert [event["tick"] for event in events] == [0, delta, 9]
        assert [event["selector_before"] for event in events] == [0, 1, 2]
        onset_pair = [event["onset_contact"] for event in events[:2]]
        completion_pair = [event["completion_contact"] for event in events[:2]]
        assert onset_pair == ([1, 805] if n == 0 else [270, 4281])
        assert completion_pair == ([261, 1065] if n == 0 else [530, 4541])
        primitive_gap = 804 if n == 0 else 4011
        assert onset_pair[1] - onset_pair[0] == primitive_gap
        assert completion_pair[1] - completion_pair[0] == primitive_gap
        pa, pb = (-k) % 5, (-(k + delta)) % 5
        assert codes[:5] == [int(p == pa) for p in range(5)]
        assert codes[5:] == [int(p == pb) for p in range(5)]
        assert {1: 1, 3: 8}[(pa - pb) % 5] == delta
        assert (-pa) % 5 == k
        endpoints.append({"source_phase": n, "clock_phase": k, "state": tuple(state4)})
        records.append({"input": [n, k], "codes": [pa, pb], "events": events})
        for _ in range(10):
            for edge in inverse(S):
                apply_pair(state4, state5, edge)
        assert tuple(state4) == initial
        assert tuple(state5) == tuple(map(lift5, initial))
        inverse_count += 1
    pairs = {tuple(record["codes"]) for record in records}
    assert len(pairs) == 10
    assert len({pa for pa, _ in pairs}) == len({pb for _, pb in pairs}) == 5
    assert all(sum(pa == p for pa, _ in pairs) == 2 for p in range(5))
    assert {invariants(endpoint["state"])[2] for endpoint in endpoints} == initial_residues
    endpoint_hash = sha256(compact(endpoints)).hexdigest()
    assert endpoint_hash == EXPOSED_ENDPOINT_SHA256
    assert (boundary_count, read_count, event_count, inverse_count) == (100, 200, 30, 10)
    assert APPLICATIONS - start_applications == 267500
    result = {
        "status": "PASS", "scope": "NON-CANONICAL / L1 / candidate-C",
        "study": "result-exposed confirmation; ten-input finite contract",
        "slots": 31, "common_auxiliary_slots": 26, "account": 82,
        "contacts_per_step": 535, "input_states": 10, "steps_each": 10,
        "full_boundaries": boundary_count, "full_read_checkpoints": read_count,
        "events": event_count, "complete_inverses": inverse_count,
        "paired_arithmetic_contact_applications": APPLICATIONS - start_applications,
        "distinct_four_coefficient_pair_checks": contact4.cache_info().currsize,
        "distinct_five_coefficient_pair_checks": contact5.cache_info().currsize,
        "record_pairs": sorted(pairs), "first_record_count": 5,
        "second_record_count": 5, "second_alternatives_per_first": 2,
        "macro_intervals": [1, 8], "primitive_intervals": [804, 4011],
        "labelled_residue_vector": list(next(iter(initial_residues))),
        "initial_and_final_residue_vector_count": 1,
        "word_sha256": WORD_SHA256, "endpoint_sha256": endpoint_hash,
        "boundary_sha256": boundary_hash.hexdigest(),
        "read_checkpoint_sha256": read_hash.hexdigest(), "records": records,
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
