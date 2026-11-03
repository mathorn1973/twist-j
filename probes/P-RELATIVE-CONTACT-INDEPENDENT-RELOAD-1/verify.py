#!/usr/bin/env python3
"""Exact two-input reload contract on one complete 56-slot carrier.

Arithmetic and the 535-contact builder are adapted from the publicly pinned
P-RELATIVE-CONTACT-VARIABLE-ARRIVAL-1, head 377a99ae11b885e27e863e2323c9a2f6e7d68510.
The four/five-coefficient comparison is a representation crosscheck within
one executable, not an independently authored breaker. New reload outputs
are not assumed: endpoint and checkpoint digests are reported after replay.
No packages, randomness, network access or file writes. Input values never
select operations; only the fixed PROGRAM below evolves the complete state.
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



CONTACT_APPLICATIONS = 0
SWAP_APPLICATIONS = 0


def apply_contact(state4, state5, edge):
    global CONTACT_APPLICATIONS
    i, j = edge
    # Cached exact pair checks establish conservation on every use of a pair.
    state4[i], state4[j] = contact4(state4[i], state4[j])
    state5[i], state5[j] = contact5(state5[i], state5[j])
    assert state5[i] == lift5(state4[i])
    assert state5[j] == lift5(state4[j])
    CONTACT_APPLICATIONS += 1


def apply_swap(state4, state5, edge):
    global SWAP_APPLICATIONS
    i, j = edge
    a, b = state4[i], state4[j]
    c, d = state5[i], state5[j]
    state4[i], state4[j] = b, a
    state5[i], state5[j] = d, c
    assert add(state4[i], state4[j]) == add(a, b)
    assert account(state4[i]) + account(state4[j]) == account(a) + account(b)
    assert add5(state5[i], state5[j]) == add5(c, d)
    assert account5(state5[i]) + account5(state5[j]) == account5(c) + account5(d)
    # Generic swaps transport labelled residues; they do not preserve them
    # at fixed labels unless the exchanged residues happen to agree.
    assert (residue(state4[i]), residue(state4[j])) == (residue(b), residue(a))
    assert state5[i] == lift5(state4[i])
    assert state5[j] == lift5(state4[j])
    SWAP_APPLICATIONS += 1


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


SA = S


def second_memory_address(address):
    return address + 20 if 11 <= address <= 30 else address


SB = tuple(tuple(second_memory_address(i) for i in edge) for edge in SA)
RELOAD = tuple(("SWAP", i, 51 + i) for i in range(5))
CONTACTS_A = tuple(("C", i, j) for i, j in SA)
CONTACTS_B = tuple(("C", i, j) for i, j in SB)
PROGRAM = CONTACTS_A * 10 + RELOAD + CONTACTS_B * 10


def inverse_program(program):
    result = []
    for kind, i, j in reversed(program):
        assert kind in ("C", "SWAP")
        result.extend([(kind, i, j)] * (4 if kind == "C" else 1))
    return tuple(result)


INVERSE_PROGRAM = inverse_program(PROGRAM)


def source_phase(index):
    """Closed nine-state formula, not a simulated expected trajectory."""
    index %= 9
    if index == 0:
        return ZERO, (2, 0, 0, 0), ZERO
    power = index if index <= 4 else index - 4
    r = rotate(ONE, power)
    u, w = sub(ONE, r), add(ONE, r)
    return (u, w, ZERO) if index <= 4 else (ZERO, w, u)


def input_state(source, clock):
    q = rotate(W, clock)
    return source_phase(source) + (q, neg(q))


def bank_state(label):
    """None is absence; an integer label, including zero, is a present record."""
    assert label is None or 0 <= label < 5
    bank = ()
    for p in range(5):
        value = rotate(B, int(p == label))
        bank += (neg(value), value)
    return bank


def state_formula(source, clock, selector, labels, queued):
    assert 0 <= selector < 3 and len(labels) == 4 and len(queued) == 5
    token = tuple(U if i == selector else ZERO for i in range(3))
    state = input_state(source, clock) + (ZERO,) + token + (W, ZERO)
    for label in labels:
        state += bank_state(label)
    return state + tuple(queued)


def initial_state(parameters):
    n, k, m, ell = parameters
    return state_formula(n, k, 0, (None,) * 4, input_state(m, ell))


def final_labels(n, k):
    delta = (1, 8)[n]
    return (-k) % 5, (-(k + delta)) % 5


def event_schedule(n):
    assert n in (0, 1)
    return ((0, 0), (1, 1), (9, 0)) if n == 0 else ((0, 1), (8, 0), (9, 1))


def stage_formula(parameters, stage, tick, read=None):
    """Independent boundary formula from phase orbits and the frozen schedule.

    read=0/1 means the corresponding completed read; read=None means the
    completed macrostep. In particular read 1 has source phase n+tick-1.
    No observed state or previously predicted state enters this formula.
    """
    n, k, m, ell = parameters
    a, b = (n, k) if stage == 0 else (m, ell)
    cutoff = (tick, 1 if read is None else read)
    marks = sum(event <= cutoff for event in event_schedule(a))
    pair = final_labels(a, b)
    current = tuple(pair[i] if marks > i else None for i in range(2))
    labels = current + (None, None) if stage == 0 else final_labels(n, k) + current
    queued = input_state(m, ell) if stage == 0 else input_state(n + 10, k + 10)
    source = a + tick + (1 if read is None else -read)
    clock = b + tick + int(read is None)
    return state_formula(source, clock, marks % 3, labels, queued)


def reload_formula(parameters):
    n, k, m, ell = parameters
    return state_formula(m, ell, 0, final_labels(n, k) + (None, None),
                         input_state(n + 10, k + 10))


def invariants(state):
    total = ZERO
    for value in state:
        total = add(total, value)
    return sum(map(account, state)), total, tuple(map(residue, state))


def compact(value):
    return json.dumps(value, separators=(",", ":")).encode("utf-8")


def read_bank(state, base):
    """Decode actual coordinates, with no input label or event information."""
    absent = (neg(B), B)
    turned = rotate(B)
    present = (neg(turned), turned)
    marks = []
    for p in range(5):
        pair = tuple(state[base + 2 * p:base + 2 * p + 2])
        assert pair in (absent, present), (base, p, "invalid pair")
        if pair == present:
            marks.append(p)
    assert len(marks) <= 1, (base, "multiple present pairs")
    return marks[0] if marks else None


def decode_pair(pa, pb):
    assert pa is not None and pb is not None
    difference = (pa - pb) % 5
    assert difference in (1, 3)
    return (0 if difference == 1 else 1), (-pa) % 5


def verify_complete(state4, state5, expected, expected_invariants, context):
    assert len(state4) == len(state5) == len(expected) == 56
    assert tuple(state4) == expected, context
    assert tuple(state5) == tuple(map(lift5, expected)), context
    assert invariants(state4) == expected_invariants, context
    assert sum(map(account5, state5)) == expected_invariants[0], context


def check_retention(state4, retained):
    for bank, previous in enumerate(retained):
        base = 11 + 10 * bank
        current = tuple(state4[base:base + 10])
        if previous is not None:
            assert current == previous, (bank, "retained archive changed")
        elif read_bank(state4, base) is not None:
            retained[bank] = current


def check_stage_events(events, stage, source):
    schedule = event_schedule(source)
    assert len(events) == 3
    assert [(e["tick"], e["read"]) for e in events] == list(schedule)
    assert [e["selector_before"] for e in events] == [0, 1, 2]
    contact_base, operation_base = 5350 * stage, 5355 * stage
    for event, (tick, read) in zip(events, schedule):
        onset = 535 * tick + (1 if read == 0 else 270)
        completion = 535 * tick + (261 if read == 0 else 530)
        assert event["onset_contact"] == contact_base + onset
        assert event["completion_contact"] == contact_base + completion
        assert event["onset_operation"] == operation_base + onset
        assert event["completion_operation"] == operation_base + completion
    expected_onsets = (1, 805) if source == 0 else (270, 4281)
    expected_completions = (261, 1065) if source == 0 else (530, 4541)
    assert tuple(e["onset_contact"] - contact_base for e in events[:2]) == expected_onsets
    assert tuple(e["completion_contact"] - contact_base for e in events[:2]) == expected_completions
    gap = (804, 4011)[source]
    for field in ("onset_contact", "completion_contact", "onset_operation", "completion_operation"):
        assert events[1][field] - events[0][field] == gap


def main():
    if sys.flags.optimize or not __debug__:
        raise SystemExit("Integrity failure: assertions must remain enabled")
    assert len(READ) == 261 and len(SA) == len(SB) == 535 and len(F_INVERSE) == 8
    word_bytes = Path(__file__).with_name("WORD535.txt").read_bytes()
    assert sha256(word_bytes).hexdigest() == WORD_SHA256
    literal = tuple((int(i) - 1, int(j) - 1)
                    for i, j in re.findall(r"C\((\d+),(\d+)\)", word_bytes.decode("ascii")))
    assert literal == SA
    assert SB == tuple(tuple(i + 20 if 11 <= i <= 30 else i for i in edge) for edge in literal)
    assert len(PROGRAM) == 10705 and len(INVERSE_PROGRAM) == 42805
    assert sum(kind == "C" for kind, _, _ in PROGRAM) == 10700
    assert sum(kind == "SWAP" for kind, _, _ in PROGRAM) == 5
    assert INVERSE_PROGRAM == (inverse_program(CONTACTS_B) * 10
                               + tuple(reversed(RELOAD))
                               + inverse_program(CONTACTS_A) * 10)
    assert all(kind in ("C", "SWAP") and 0 <= i < 56 and 0 <= j < 56 and i != j
               for kind, i, j in PROGRAM)
    assert all(i < 31 and j < 31 for i, j in SA)
    assert all(i < 51 and j < 51 and i not in range(11, 31) and j not in range(11, 31)
               for i, j in SB)
    assert all(i not in range(11, 51) and j not in range(11, 51) for _, i, j in RELOAD)

    # Check the analytic source orbit independently of all expected run states.
    source4 = list(source_phase(0))
    source5 = list(map(lift5, source4))
    assert len({source_phase(i) for i in range(9)}) == 9
    for phase in range(9):
        assert tuple(source4) == source_phase(phase)
        for edge in F:
            apply_contact(source4, source5, edge)
        assert tuple(source4) == source_phase(phase + 1)
        assert tuple(source5) == tuple(map(lift5, source_phase(phase + 1)))
    assert CONTACT_APPLICATIONS == 18 and SWAP_APPLICATIONS == 0

    inputs = tuple(product(range(2), range(5), range(2), range(5)))
    preparations = tuple(initial_state(p) for p in inputs)
    assert len(inputs) == len(set(preparations)) == 100
    common = {state[5:51] for state in preparations}
    assert len(common) == 1 and len(next(iter(common))) == 46
    assert sum(map(account, next(iter(common)))) == 128
    expected_invariants = invariants(preparations[0])
    assert expected_invariants[:2] == (156, (6, 0, 0, 0))
    assert all(invariants(state) == expected_invariants for state in preparations)

    start_contacts, start_swaps = CONTACT_APPLICATIONS, SWAP_APPLICATIONS
    read_hash, step_hash, reload_hash = sha256(), sha256(), sha256()
    endpoint_hash, event_hash, decoded_hash = sha256(), sha256(), sha256()
    read_count = step_count = reload_count = event_count = inverse_count = 0
    record_quadruples, decoded_inputs = set(), set()
    for parameters, initial in zip(inputs, preparations):
        state4, state5 = list(initial), list(map(lift5, initial))
        case_contacts, case_swaps = CONTACT_APPLICATIONS, SWAP_APPLICATIONS
        cursor = 0
        retained = [None] * 4
        first_archive = first_archive5 = spent_input = spent_input5 = None
        case_events = []
        for stage, word in enumerate((SA, SB)):
            if stage == 1:
                first_archive = tuple(state4[11:31])
                first_archive5 = tuple(state5[11:31])
                spent_input = tuple(state4[:5])
                spent_input5 = tuple(state5[:5])
                all_banks = tuple(state4[11:51])
                for operation in RELOAD:
                    assert PROGRAM[cursor] == operation
                    _, i, j = operation
                    # The admitted pairs have equal residues. The swap primitive
                    # remains the generic transport operation defined above.
                    assert residue(state4[i]) == residue(state4[j])
                    apply_swap(state4, state5, (i, j))
                    cursor += 1
                    assert tuple(state4[11:51]) == all_banks
                    assert tuple(state4[11:31]) == first_archive
                    assert tuple(state5[11:31]) == first_archive5
                    assert invariants(state4) == expected_invariants
                verify_complete(state4, state5, reload_formula(parameters),
                                expected_invariants, (parameters, "reload"))
                assert tuple(state4[51:56]) == spent_input
                assert tuple(state5[51:56]) == spent_input5
                check_retention(state4, retained)
                reload_hash.update(compact([parameters, state4]))
                reload_count += 1
            a, b = parameters[:2] if stage == 0 else parameters[2:]
            schedule = event_schedule(a)
            events = []
            for tick in range(10):
                for index, edge in enumerate(word):
                    assert PROGRAM[cursor] == ("C", *edge)
                    prior_g = state4[G]
                    apply_contact(state4, state5, edge)
                    cursor += 1
                    # Literal, every-contact retention for the disjoint resources.
                    if stage == 0:
                        assert tuple(state4[31:56]) == initial[31:56]
                        assert tuple(state5[31:56]) == tuple(map(lift5, initial[31:56]))
                    else:
                        assert tuple(state4[11:31]) == first_archive
                        assert tuple(state5[11:31]) == first_archive5
                        assert tuple(state4[51:56]) == spent_input
                        assert tuple(state5[51:56]) == spent_input5
                    if index in (0, 269):
                        read = int(index == 269)
                        active = (tick, read) in schedule
                        assert prior_g == ZERO
                        assert state4[G] == (U if active else ZERO)
                        if state4[G] == U:
                            selector_state = tuple(state4[6:9])
                            assert selector_state in ((U, ZERO, ZERO), (ZERO, U, ZERO), (ZERO, ZERO, U))
                            events.append({"tick": tick, "read": read,
                                           "selector_before": selector_state.index(U),
                                           "onset_contact": CONTACT_APPLICATIONS - case_contacts,
                                           "onset_operation": cursor})
                            event_count += 1
                    if index in (260, 529):
                        read = int(index == 529)
                        if (tick, read) in schedule:
                            assert (events[-1]["tick"], events[-1]["read"]) == (tick, read)
                            events[-1]["completion_contact"] = CONTACT_APPLICATIONS - case_contacts
                            events[-1]["completion_operation"] = cursor
                        verify_complete(state4, state5, stage_formula(parameters, stage, tick, read),
                                        expected_invariants, (parameters, stage, tick, read, "read"))
                        check_retention(state4, retained)
                        read_hash.update(compact([parameters, stage, tick, read, state4]))
                        read_count += 1
                verify_complete(state4, state5, stage_formula(parameters, stage, tick),
                                expected_invariants, (parameters, stage, tick, "step"))
                check_retention(state4, retained)
                step_hash.update(compact([parameters, stage, tick + 1, state4]))
                step_count += 1
            check_stage_events(events, stage, a)
            actual_pair = tuple(read_bank(state4, 11 + 20 * stage + 10 * bank) for bank in range(2))
            assert decode_pair(*actual_pair) == (a, b)
            case_events.append(events)
        assert cursor == len(PROGRAM)
        assert CONTACT_APPLICATIONS - case_contacts == 10700
        assert SWAP_APPLICATIONS - case_swaps == 5
        codes = tuple(read_bank(state4, 11 + 10 * bank) for bank in range(4))
        assert all(code is not None for code in codes)
        decoded = decode_pair(*codes[:2]) + decode_pair(*codes[2:])
        assert decoded == parameters
        assert all(value is not None for value in retained)
        record_quadruples.add(codes)
        decoded_inputs.add(decoded)
        endpoint_hash.update(compact([parameters, state4]))
        event_hash.update(compact([parameters, case_events]))
        decoded_hash.update(compact([parameters, codes, decoded]))
        for kind, i, j in INVERSE_PROGRAM:
            if kind == "C":
                apply_contact(state4, state5, (i, j))
            else:
                assert residue(state4[i]) == residue(state4[j])
                apply_swap(state4, state5, (i, j))
        verify_complete(state4, state5, initial, expected_invariants, (parameters, "complete inverse"))
        assert CONTACT_APPLICATIONS - case_contacts == 53500
        assert SWAP_APPLICATIONS - case_swaps == 10
        inverse_count += 1
    assert (read_count, step_count, reload_count, event_count, inverse_count) == (4000, 2000, 100, 600, 100)
    assert CONTACT_APPLICATIONS - start_contacts == 5350000
    assert SWAP_APPLICATIONS - start_swaps == 1000
    assert len(record_quadruples) == len(decoded_inputs) == 100
    assert decoded_inputs == set(inputs)
    result = {
        "status": "PASS", "scope": "NON-CANONICAL / L1 / candidate-C",
        "study": "two independently prepared inputs; fixed finite reload program",
        "slots": 56, "common_auxiliary_slots": 46, "common_auxiliary_account": 128,
        "complete_account": 156, "complete_sum": [6, 0, 0, 0], "input_states": 100,
        "contacts_per_step": 535, "steps_per_stage": 10, "stages": 2,
        "forward_contacts_each": 10700, "forward_swaps_each": 5,
        "inverse_contacts_each": 42800, "inverse_swaps_each": 5,
        "full_read_checkpoints": read_count, "full_step_checkpoints": step_count,
        "full_reload_checkpoints": reload_count, "events": event_count,
        "complete_inverses": inverse_count,
        "paired_arithmetic_contact_applications": CONTACT_APPLICATIONS - start_contacts,
        "paired_arithmetic_swap_applications": SWAP_APPLICATIONS - start_swaps,
        "source_orbit_setup_contacts_excluded": start_contacts,
        "distinct_four_coefficient_pair_checks": contact4.cache_info().currsize,
        "distinct_five_coefficient_pair_checks": contact5.cache_info().currsize,
        "record_quadruples": sorted(record_quadruples), "decoded_inputs": len(decoded_inputs),
        "macro_intervals": [1, 8], "within_stage_contact_intervals": [804, 4011],
        "second_stage_contact_offset": 5350, "second_stage_operation_offset": 5355,
        "labelled_residue_vector": list(expected_invariants[2]),
        "word535_sha256": WORD_SHA256,
        "complete_program_sha256": sha256(compact(PROGRAM)).hexdigest(),
        "endpoint_sha256": endpoint_hash.hexdigest(),
        "read_checkpoint_sha256": read_hash.hexdigest(),
        "step_checkpoint_sha256": step_hash.hexdigest(),
        "reload_checkpoint_sha256": reload_hash.hexdigest(),
        "event_sha256": event_hash.hexdigest(), "decoded_sha256": decoded_hash.hexdigest(),
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
