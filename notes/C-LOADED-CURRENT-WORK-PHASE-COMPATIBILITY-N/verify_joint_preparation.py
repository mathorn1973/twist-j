#!/usr/bin/env python3
"""Exact prospective joint-preparation audit, NON-CANONICAL / L1.

Standalone standard-library source. Do not execute before its public pin.
No earlier verifier or field/clock trajectory is imported or replayed.
"""
from collections import Counter
from hashlib import sha256
from itertools import product
import json

CHECKS = 0
Z = (0, 0, 0, 0)
E = (1, 0, 0, 0)
JROOT = (0, 1, 0, 0)


def demand(condition, reason):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(reason)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def negative(x):
    return tuple(-a for a in x)


def subtract(x, y):
    return add(x, negative(y))


def multiply(x, y):
    coefficients = [0] * 7
    for a in range(4):
        for b in range(4):
            coefficients[a + b] += x[a] * y[b]
    for degree in range(6, 3, -1):
        top = coefficients[degree]
        coefficients[degree] = 0
        for lower in range(degree - 4, degree):
            coefficients[lower] -= top
    return tuple(coefficients[:4])


ROOTS = [E]
for _ in range(4):
    ROOTS.append(multiply(ROOTS[-1], JROOT))
ROOTS = tuple(ROOTS)
RHO = ROOTS[2]
LAMBDA = subtract(E, JROOT)
UNITS = ROOTS + tuple(negative(x) for x in ROOTS)


def norm(x):
    numerator = 5 * sum(a * a for a in x) - sum(x) ** 2
    if numerator % 2:
        raise ArithmeticError("nonintegral quadratic account")
    return numerator // 2


def residue(x):
    return sum(x) % 5


def total_norm(state):
    return sum(norm(x) for x in state)


def total_sum(state):
    value = Z
    for x in state:
        value = add(value, x)
    return value


def residue_histogram(state):
    counts = Counter(residue(x) for x in state)
    return tuple(counts[k] for k in range(5))


def contact(x, y):
    delta = subtract(x, y)
    if any(a % 2 for a in delta):
        return x, y, False
    center = tuple(a // 2 for a in add(x, y))
    relative = tuple(a // 2 for a in delta)
    rotated = multiply(RHO, relative)
    return add(center, rotated), subtract(center, rotated), True


def perform(state, word, audit=True):
    current = tuple(state)
    admitted = []
    for kind, left, right in word:
        previous = current
        output = list(current)
        if kind == "C":
            output[left], output[right], accepted = contact(current[left], current[right])
        elif kind == "S":
            output[left], output[right] = current[right], current[left]
            accepted = None
        else:
            raise ValueError(kind)
        current = tuple(output)
        admitted.append(accepted)
        if audit:
            demand(norm(current[left]) + norm(current[right]) ==
                   norm(previous[left]) + norm(previous[right]), "affected-pair account")
            demand(add(current[left], current[right]) ==
                   add(previous[left], previous[right]), "affected-pair ring sum")
            if kind == "C":
                demand(residue(current[left]) == residue(previous[left])
                       and residue(current[right]) == residue(previous[right]),
                       "individual ordinary-contact residues")
                if accepted is False:
                    demand(current == previous, "literal refusal identity")
            else:
                demand(residue_histogram(current) == residue_histogram(previous),
                       "swap only permutes residues")
    return current, tuple(admitted)


def apply(state, word, audit=True):
    return perform(state, word, audit)[0]


def literal_inverse(word):
    return tuple(op for op in reversed(word) for _ in range(4 if op[0] == "C" else 1))


def repeat(state, word, count):
    for _ in range(count):
        state = apply(state, word)
    return state


def scale_state(unit, state):
    return tuple(multiply(unit, x) for x in state)


def phase(x):
    return ROOTS.index(x)


def pair(r, opposite=False):
    value = ROOTS[r % 5]
    return (negative(value), value) if opposite else (value, negative(value))


def bank(s):
    references = tuple(negative(ROOTS[(s + k) % 5]) for k in range(5))
    return references + references


def receiver(start):
    return tuple(("C", 0, start + k) for k in range(5))


def bank_reading(state, start):
    changed = tuple(k for k in range(5) if state[start + k] != state[start + 5 + k])
    return changed[0] if changed else None


A = (("C", 0, 1),)
B = (("C", 2, 3),)
K = (("C", 0, 2), ("C", 1, 3))
MAIN_WORD = tuple(op for k in range(1, 5) for op in A + K * k) + A
MAIN_INVERSE = literal_inverse(MAIN_WORD)
MAIN_COMPRESSED_INVERSE = A * 4
for _k in range(4, 0, -1):
    MAIN_COMPRESSED_INVERSE += K * (5 - _k) + A * 4
SECONDARY_PHASES = (2, 4, 1, 3)
SECONDARY_WORD = tuple(op for helper in range(4)
                       for op in (("C", 0, 2 + 2 * helper),
                                  ("C", 1, 3 + 2 * helper)))
SECONDARY_INVERSE = literal_inverse(SECONDARY_WORD)
HIT_COUNTS = (0, 2, 4, 1, 3)
SWAP_WORD = (("S", 0, 3), ("S", 1, 2))


def main_input(r, s):
    return pair(r) + pair(s, opposite=True)


def secondary_input(r, s):
    return pair(r) + tuple(slot for k in SECONDARY_PHASES
                           for slot in pair(s + k, opposite=True))


def family_word(t):
    turns = 3 * t % 5
    return B * turns + MAIN_WORD + B * (5 - turns)


def hash_records(records):
    payload = json.dumps(records, separators=(",", ":"), sort_keys=True) + "\n"
    return sha256(payload.encode("ascii")).hexdigest()


def independent_state(phases):
    return pair(phases[0]) + tuple(slot for value in phases[1:]
                                  for slot in pair(value, opposite=True))


def independent_phases(state):
    demand(state[1] == negative(state[0]), "balanced independent source")
    result = [phase(state[0])]
    for i in range(4):
        demand(state[2 + 2 * i] == negative(state[3 + 2 * i]),
               "balanced independent helper")
        result.append(phase(state[3 + 2 * i]))
    return tuple(result)


def main():
    demand(multiply(ROOTS[4], JROOT) == E, "root order five")
    demand(norm(E) == 2 and norm(LAMBDA) == 5, "base accounts")
    demand(len(MAIN_WORD) == 25 and len(MAIN_INVERSE) == 100
           and len(MAIN_COMPRESSED_INVERSE) == 40, "main contact lengths")
    demand(len(SECONDARY_WORD) == 8 and len(SECONDARY_INVERSE) == 32,
           "secondary contact lengths")
    demand(all(len(family_word(t)) == 30 for t in range(5)), "common family attempt count")

    main_records = []
    for r, s in product(range(5), repeat=2):
        initial = main_input(r, s)
        result = apply(initial, MAIN_WORD)
        expected = pair(s) + pair(2 * s - r, opposite=True)
        demand(result == expected, "main exact phase map")
        demand(total_norm(result) == 8 and total_sum(result) == Z,
               "main four-slot neutral account")
        demand(all(norm(x) == 2 for x in result), "main unit outputs")
        demand((phase(result[0]) - phase(result[3])) % 5 == (r - s) % 5,
               "old relative phase is retained, not erased")
        demand(apply(result, MAIN_INVERSE) == initial, "main literal inverse")
        demand(apply(result, MAIN_COMPRESSED_INVERSE) == initial, "main compressed inverse")
        demand(repeat(initial, MAIN_WORD, 5) == initial, "prepared main fifth iterate")
        main_records.append([r, s, phase(result[0]), phase(result[3])])

        prepared = initial + bank(s)
        reset = apply(prepared, MAIN_WORD)
        demand(reset[4:] == prepared[4:] and total_norm(reset) == 28,
               "main bank untouched and completely funded")
        read = apply(reset, receiver(4))
        demand(bank_reading(read, 4) == 0, "main reset source reads bank phase zero")
        matching = [k for k in range(5) if read[2] == read[9 + k]]
        demand(matching == [(s - r) % 5], "used helper records old source relative phase")
        demand(read[9:] == prepared[9:], "main reader twins untouched")
        demand(apply(apply(read, literal_inverse(receiver(4))), MAIN_INVERSE) == prepared,
               "complete main reader and reset inverse")

    first_main = apply(main_input(2, 0), MAIN_WORD)
    second_main = apply(first_main, MAIN_WORD)
    demand(first_main[0] == E and second_main[0] == ROOTS[3],
           "main reset is not a permanent lock to the initial frame")

    independent_bank_records = []
    for r, s, v in product(range(5), repeat=3):
        initial = main_input(r, s) + bank(v)
        reset = apply(initial, MAIN_WORD)
        demand(reset[:2] == pair(s) and reset[4:] == initial[4:],
               "main reset uses donor phase, not an unrelated bank")
        demand(total_norm(reset) == 28 and total_sum(reset) == Z,
               "independent donor and bank complete account")
        read = apply(reset, receiver(4))
        reading = bank_reading(read, 4)
        demand(reading == (s - v) % 5, "independent donor-bank phase is observable")
        demand(read[9:] == initial[9:], "independent bank twins preserved")
        demand(apply(apply(read, literal_inverse(receiver(4))), MAIN_INVERSE) == initial,
               "independent donor-bank complete inverse")
        independent_bank_records.append([r, s, v, reading])

    family_records = []
    for r, s in product(range(5), repeat=2):
        initial = main_input(r, s)
        prepared = initial + bank(s)
        for t in range(5):
            word = family_word(t)
            inverse = literal_inverse(word)
            demand(len(inverse) == 120, "family literal inverse length")
            result = apply(initial, word)
            demand(result == pair(s + t) + pair(2 * s + t - r, opposite=True),
                   "same-preparation family exact phase map")
            demand(total_norm(result) == 8 and total_sum(result) == Z,
                   "same-preparation family account")
            demand((phase(result[0]) - phase(result[3])) % 5 == (r - s) % 5,
                   "family keeps old relative phase")
            demand(apply(result, inverse) == initial, "family complete inverse")
            reset = apply(prepared, word)
            demand(reset[4:] == prepared[4:] and total_norm(reset) == 28,
                   "family leaves shared bank untouched")
            read = apply(reset, receiver(4))
            demand(bank_reading(read, 4) == t, "unchanged reader distinguishes family offset")
            matching = [k for k in range(5) if read[2] == read[9 + k]]
            demand(matching == [(s + t - r) % 5], "family helper memory against bank")
            demand(read[9:] == prepared[9:], "family reader twins untouched")
            demand(apply(apply(read, literal_inverse(receiver(4))), inverse) == prepared,
                   "complete family reader and reset inverse")
            family_records.append([r, s, t, phase(result[0]), phase(result[3]),
                                   bank_reading(read, 4), matching[0]])

    secondary_records = []
    for s in range(5):
        helper_records = set()
        for r in range(5):
            delta = (r - s) % 5
            initial = secondary_input(r, s)
            result, accepted = perform(initial, SECONDARY_WORD)
            demand(result[:2] == pair(s), "secondary source aligns to prepared bank frame")
            demand(total_norm(result) == 20 and total_sum(result) == Z,
                   "secondary neutral account")
            demand(all(norm(x) == 2 for x in result), "secondary individual unit accounts")
            demand(sum(accepted) == 2 * HIT_COUNTS[delta], "secondary accepted helper gates")
            changed = tuple(i for i in range(4)
                            if result[2 + 2 * i] != initial[2 + 2 * i])
            demand(len(changed) == HIT_COUNTS[delta], "secondary helper record length")
            helper_records.add(result[2:])
            demand(apply(result, SECONDARY_INVERSE) == initial, "secondary complete inverse")
            prepared = initial + bank(s)
            reset = apply(prepared, SECONDARY_WORD)
            demand(reset[10:] == prepared[10:] and total_norm(reset) == 40,
                   "secondary shared bank unchanged and funded")
            read = apply(reset, receiver(10))
            demand(bank_reading(read, 10) == 0, "secondary reset source reads zero")
            recorded = tuple(i for i, k in enumerate(SECONDARY_PHASES)
                             if read[2 + 2 * i] != read[15 + k])
            demand(recorded == changed, "secondary helper record against untouched twins")
            demand(read[15:] == prepared[15:], "secondary reader twins untouched")
            demand(apply(apply(read, literal_inverse(receiver(10))), SECONDARY_INVERSE) == prepared,
                   "complete secondary reader and reset inverse")
            secondary_records.append([r, s, len(changed), list(changed)])
        demand(len(helper_records) == 5, "secondary records distinguish old relative phases")

    once = apply(secondary_input(2, 0), SECONDARY_WORD)
    twice = apply(once, SECONDARY_WORD)
    demand(once[0] == E and twice[0] == ROOTS[2],
           "secondary reset is not a permanent phase lock")

    # All independent unit phases: a permutation, not unconditional alignment.
    outputs = set()
    mapping = []
    output_counts = Counter()
    input_aligned = 0
    intersection = 0
    for phases in product(range(5), repeat=5):
        initial = independent_state(phases)
        result = apply(initial, SECONDARY_WORD)
        output = independent_phases(result)
        outputs.add(output)
        output_counts[output[0]] += 1
        input_aligned += phases[0] == 0
        intersection += phases[0] == 0 and output[0] == 0
        demand(apply(result, SECONDARY_INVERSE) == initial,
               "independent helper configuration inverse")
        mapping.append([list(phases), list(output)])
    demand(len(outputs) == 3125, "complete independent carrier permutation")
    demand(input_aligned == 625 and output_counts[0] == 625,
           "alignment measure unchanged on independent carrier")
    demand(tuple(output_counts[k] for k in range(5)) == (625,) * 5,
           "uniform output source marginal")

    # Per-slot lambda residues: exact contact controls only on O, not a field carrier.
    elements = tuple(product(range(-1, 2), repeat=4))
    for x, y in product(elements, repeat=2):
        original = (x, y)
        current = original
        for _ in range(5):
            current = apply(current, (("C", 0, 1),))
        demand(current == original, "ordinary contact fifth power on coefficient box")

    obstruction_seed = (E, negative(E), LAMBDA, negative(LAMBDA),
                        LAMBDA, negative(LAMBDA)) + (Z,) * 6
    seed_histogram = residue_histogram(obstruction_seed)
    demand(total_norm(obstruction_seed) == 24 and total_sum(obstruction_seed) == Z,
           "equal-account obstruction seed")
    demand(seed_histogram == (10, 1, 0, 0, 1), "seed residue histogram")
    for r, s in product(range(5), repeat=2):
        target = pair(r) + bank(s)
        demand(total_norm(target) == 24 and total_sum(target) == Z,
               "equal-account twelve-slot bank target")
        demand(residue_histogram(target) == (0, 1, 0, 0, 11),
               "bank target residue histogram")
        demand(residue_histogram(target) != seed_histogram,
               "histogram obstruction survives arbitrary slot permutations")

    # Simultaneous unit covariance of both prepared protocols and composed readers.
    for r, s in product(range(5), repeat=2):
        for prepared, word, start in (
                (main_input(r, s) + bank(s), MAIN_WORD, 4),
                (secondary_input(r, s) + bank(s), SECONDARY_WORD, 10)):
            reset = apply(prepared, word)
            complete_word = word + receiver(start)
            result = apply(prepared, complete_word)
            for unit in UNITS:
                rotated = scale_state(unit, prepared)
                demand(apply(rotated, word) == scale_state(unit, reset),
                       "reset whole-frame covariance")
                final = apply(rotated, complete_word)
                demand(final == scale_state(unit, result),
                       "composed reset and reader whole-frame covariance")
                demand(bank_reading(final, start) == 0, "whole-frame readout covariance")
                demand(apply(final, literal_inverse(complete_word)) == rotated,
                       "rotated composed complete inverse")

    # Fixed raw occupied controls, retaining all unused slots.
    raw_words = (MAIN_WORD, SECONDARY_WORD) + tuple(family_word(t) for t in range(5))
    for number in range(32):
        initial = tuple(elements[(11 * number + 7 * k + k * k) % 81] for k in range(10))
        for word in raw_words:
            result = apply(initial, word)
            demand(apply(result, literal_inverse(word)) == initial,
                   "raw ten-slot complete literal inverse")
        result = apply(initial, MAIN_WORD)
        demand(apply(result, MAIN_COMPRESSED_INVERSE) == initial,
               "raw main compressed inverse")

    # A distinct protocol class: two whole-slot swaps with a prepared donor pair.
    for r, s in product(range(5), repeat=2):
        initial = main_input(r, s)
        result = apply(initial, SWAP_WORD)
        demand(result == pair(s) + pair(r, opposite=True), "two-swap donor phase exchange")
        demand(total_norm(result) == 8 and total_sum(result) == Z, "two-swap complete account")
        demand(apply(result, literal_inverse(SWAP_WORD)) == initial, "two-swap inverse")

    print("NON-CANONICAL / L1; exact joint-preparation author audit")
    print("main_map=(r,s)->(s,2s-r); relative_phase_retained=r-s")
    print("main_contacts=25; literal_inverse=100; compressed_inverse=40")
    print("main_account=8; with_untouched_bank=28; prepared_period_divides=5")
    print("main_phase_cases=25; records_sha256=" + hash_records(main_records))
    print("independent_donor_bank_cases=125; reading=s-v; records_sha256=" +
          hash_records(independent_bank_records))
    print("equal_length_family_cases=125; contacts=30; inverse=120; account=8; with_bank=28")
    print("family_records_sha256=" + hash_records(family_records))
    print("secondary_contacts=8; inverse=32; account=20; with_bank=40")
    print("secondary_hit_counts=0,2,4,1,3; cases=25; records_sha256=" +
          hash_records(secondary_records))
    print("independent_configurations=3125; distinct_outputs=" + str(len(outputs)))
    print("independent_output_source_counts=" +
          ",".join(str(output_counts[k]) for k in range(5)))
    print("independent_input_and_output_aligned=" + str(intersection))
    print("independent_mapping_sha256=" + hash_records(mapping))
    print("residue_pair_controls=6561; equal_Q24_histograms=10,1,0,0,1|0,1,0,0,11")
    print("whole_frame_units=10; raw_ten_slot_controls=32; donor_swap_cases=25")
    print("no_native_clock_or_field_replay; no_attractor_or_erasure_claim")
    print("assertions=" + str(CHECKS))
    print("PASS")


if __name__ == "__main__":
    main()
