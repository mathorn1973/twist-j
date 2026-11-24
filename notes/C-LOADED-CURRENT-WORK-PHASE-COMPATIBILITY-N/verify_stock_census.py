#!/usr/bin/env python3
"""Prospective exact stock census, NON-CANONICAL / L1.

Standard library only. No earlier verifier is imported or executed.
The exposed external counts are hypotheses checked only after public pin.
"""
from collections import Counter
from hashlib import sha256
from itertools import product
import json

ASSERTIONS = 0
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
ROOT = (0, 1, 0, 0)


def require(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def plus(x, y):
    return tuple(x[k] + y[k] for k in range(4))


def minus(x, y):
    return tuple(x[k] - y[k] for k in range(4))


def scaled(n, x):
    return tuple(n * value for value in x)


def multiply(x, y):
    coefficients = [0] * 7
    for left, cx in enumerate(x):
        for right, cy in enumerate(y):
            coefficients[left + right] += cx * cy
    for degree in (6, 5, 4):
        leading = coefficients[degree]
        for destination in range(degree - 4, degree):
            coefficients[destination] -= leading
    return tuple(coefficients[:4])


POWERS = [ONE]
for _ in range(4):
    POWERS.append(multiply(POWERS[-1], ROOT))
POWERS = tuple(POWERS)
RHO = POWERS[2]
J = plus(ONE, RHO)
OLD_STOCK = (3, 4, 2, 0)
SMALL_STOCK = (2, -2, 1, 0)
NORMALIZED_STOCK = (1, 2, 0, -2)
OLD_READINGS = (32, 17, 2, 7, 27)
SMALL_READINGS = (12, 7, 22, 2, 17)
NORMALIZED_READINGS = (22, 12, 2, 7, 17)
WITNESSES = ((OLD_STOCK, OLD_READINGS, "Q32"),
             (SMALL_STOCK, SMALL_READINGS, "Q22_S"),
             (NORMALIZED_STOCK, NORMALIZED_READINGS, "Q22_T"))
UNITS = tuple(scaled(sign, POWERS[k]) for sign in (1, -1) for k in range(5))
RAW_ALPHABET = (ZERO, ONE, ROOT, J, OLD_STOCK)
WORD = tuple(op for _ in range(5) for op in (("C", 0, 2), ("C", 0, 1)))


def account(x):
    twice = 5 * sum(value * value for value in x) - sum(x) ** 2
    if twice % 2:
        raise ArithmeticError("quadratic account is not integral")
    return twice // 2


def account_sum(state):
    return sum(account(x) for x in state)


def ring_sum(state):
    result = ZERO
    for value in state:
        result = plus(result, value)
    return result


def ordinary_contact(left, right):
    delta = minus(left, right)
    if any(value % 2 for value in delta):
        return left, right, False
    midpoint = tuple(value // 2 for value in plus(left, right))
    relative = tuple(value // 2 for value in delta)
    rotated = multiply(RHO, relative)
    return plus(midpoint, rotated), minus(midpoint, rotated), True


def execute(state, word, audit=True):
    current = tuple(state)
    for kind, left, right in word:
        before = current
        updated = list(current)
        if kind == "C":
            updated[left], updated[right], accepted = ordinary_contact(
                current[left], current[right])
        else:
            if kind != "S":
                raise ValueError("unknown operation")
            updated[left], updated[right] = current[right], current[left]
            accepted = None
        current = tuple(updated)
        if audit:
            require(account_sum(current) == account_sum(before), "local account")
            require(ring_sum(current) == ring_sum(before), "local ring sum")
            if accepted is False:
                require(current == before, "refusal is literal identity")
    return current


def inverse(word):
    return tuple(op for op in reversed(word)
                 for _ in range(4 if op[0] == "C" else 1))


INVERSE = inverse(WORD)


def input_state(stock, b):
    return (POWERS[b], scaled(-1, POWERS[b]), stock)


def response(stock, audit=True):
    return tuple(account(execute(input_state(stock, b), WORD, audit)[2])
                 for b in range(5))


def is_success(readings):
    return len(set(readings)) == 5


def record(stock, readings):
    return {"Q": account(stock), "stock": list(stock), "readings": list(readings)}


def canonical_digest(records):
    payload = json.dumps(records, sort_keys=True, separators=(",", ":")) + "\n"
    return sha256(payload.encode("ascii")).hexdigest()


def rotate_state(unit, state):
    return tuple(multiply(unit, value) for value in state)


def clock_word(m):
    word = []
    for left, right in ((3, 4), (2, 3), (1, 2), (0, 1)):
        word.extend((("S", 2 * left, 2 * right),
                     ("S", 2 * left + 1, 2 * right + 1)))
    for pair in range(5):
        exponent = 3 * (m + (pair == 0)) % 5
        word.extend([("C", 2 * pair, 2 * pair + 1)] * exponent)
    return tuple(word)


def repeat(state, word, count):
    for _ in range(count):
        state = execute(state, word)
    return state


def reader_word_at(site, stock_index=10):
    return tuple(op for _ in range(5)
                 for op in (("C", 2 * site, stock_index),
                            ("C", 2 * site, 2 * site + 1)))


def run():
    require(multiply(POWERS[4], ROOT) == ONE, "fifth root relation")
    require(len(WORD) == 10 and len(INVERSE) == 40, "fixed receiver calendar")
    require(account(OLD_STOCK) == 32 and account(SMALL_STOCK) == 22,
            "frozen stock preparation accounts")
    require(response(OLD_STOCK) == OLD_READINGS, "old stock response")
    require(response(SMALL_STOCK) == SMALL_READINGS, "exposed hand-derived Q22 witness S")
    require(account(NORMALIZED_STOCK) == 22
            and response(NORMALIZED_STOCK) == NORMALIZED_READINGS,
            "exposed hand-derived normalized Q22 witness T")
    for small_stock, small_readings in ((SMALL_STOCK, SMALL_READINGS),
                                        (NORMALIZED_STOCK, NORMALIZED_READINGS)):
        for b in range(5):
            initial = input_state(small_stock, b)
            final = execute(initial, WORD)
            require(account_sum(final) == 26, "small high-pair complete account")
            require(account_sum(final[:2]) == 26 - small_readings[b],
                    "small stock work remains as pointer backreaction")
            require(account(final[2]) <= 22, "small stock is active")
            require(execute(final, INVERSE) == initial, "small stock complete inverse")
            neutral = initial + (scaled(-1, small_stock),)
            neutral_final = execute(neutral, WORD)
            require(account_sum(neutral_final) == 48 and ring_sum(neutral_final) == ZERO,
                    "small neutral high-pair preparation account")
            require(neutral_final[3] == neutral[3], "small neutral companion preserved")
            require(execute(neutral_final, INVERSE) == neutral, "small neutral inverse")
        for label in range(25):
            initial = input_state(small_stock, label // 5) + (
                POWERS[label % 5], scaled(-1, POWERS[label % 5]))
            final = execute(initial, WORD)
            require(account_sum(final) == 30 and final[3:] == initial[3:],
                    "small stock and old two-pair pointer account")
            require(execute(final, INVERSE) == initial, "small two-pair inverse")
            neutral = initial + (scaled(-1, small_stock),)
            neutral_final = execute(neutral, WORD)
            require(account_sum(neutral_final) == 52 and ring_sum(neutral_final) == ZERO,
                    "small stock and neutral old two-pair pointer account")
            require(execute(neutral_final, INVERSE) == neutral, "small full neutral inverse")

    # Complete search for Q <= 32; analytic coordinate bound is in STOCK-PREREG.md.
    successful = []
    bounded_candidates = 0
    for stock in product(range(-5, 6), repeat=4):
        energy = account(stock)
        require(energy >= 0, "nonnegative enumerated stock account")
        if energy > 32:
            continue
        bounded_candidates += 1
        readings = response(stock)
        if is_success(readings):
            successful.append(record(stock, readings))
            for b in range(5):
                initial = input_state(stock, b)
                require(execute(execute(initial, WORD), INVERSE) == initial,
                        "every successful bounded stock has literal inverse")
    successful.sort(key=lambda row: (row["Q"], row["stock"]))
    counts = dict(sorted(Counter(row["Q"] for row in successful).items()))
    require(counts == {22: 40, 28: 40, 32: 40},
            "exposed norm census mismatch: " + repr(counts))
    require(len(successful) == 120, "exposed bounded success total")
    minimum = successful[0]
    require(minimum["Q"] == 22, "minimum within fixed word and readout stock family")
    require(all(any(tuple(row["stock"]) == stock for row in successful)
                for stock in (SMALL_STOCK, NORMALIZED_STOCK)),
            "both explicit Q22 witnesses belong to complete census")

    # Separate full coefficient box. No quadratic-account cutoff is applied here.
    box_successful = []
    for stock in product(range(-2, 3), repeat=4):
        readings = response(stock)
        if is_success(readings):
            box_successful.append(record(stock, readings))
    box_successful.sort(key=lambda row: (row["Q"], row["stock"]))
    box_counts = dict(sorted(Counter(row["Q"] for row in box_successful).items()))
    require(len(box_successful) == 32,
            "exposed unrestricted 625-stock box count mismatch: " + str(len(box_successful)))

    # Simultaneous covariance under all ten Q-preserving root units.
    for stock, base, _name in WITNESSES:
        for b in range(5):
            initial = input_state(stock, b)
            final = execute(initial, WORD)
            for unit in UNITS:
                rotated_initial = rotate_state(unit, initial)
                rotated_final = execute(rotated_initial, WORD)
                require(rotated_final == rotate_state(unit, final),
                        "prepared simultaneous unit covariance")
                require(account(rotated_final[2]) == account(final[2]),
                        "simultaneous frame rotation leaves readout unchanged")
                require(execute(rotated_final, INVERSE) == rotated_initial,
                        "rotated prepared inverse")
        for s in range(5):
            rotated_stock = multiply(POWERS[s], stock)
            require(response(rotated_stock) == tuple(base[(b - s) % 5] for b in range(5)),
                    "stock-only phase rotation reads relative phase b-s")

    for initial in product(RAW_ALPHABET, repeat=3):
        final = execute(initial, WORD)
        require(execute(final, INVERSE) == initial, "raw occupied complete inverse")
        for unit in UNITS:
            rotated_initial = rotate_state(unit, initial)
            rotated_final = execute(rotated_initial, WORD)
            require(rotated_final == rotate_state(unit, final),
                    "raw occupied simultaneous unit covariance")
            require(execute(rotated_final, INVERSE) == rotated_initial,
                    "raw rotated complete inverse")
    refusal = (ONE, ROOT, ZERO)
    require(execute(refusal, WORD) == refusal, "explicit completely refused raw input")

    # Actual native clock ticks and fixed marked receivers in both stock frames.
    delta = (ONE, scaled(-1, ONE)) + (ZERO,) * 8
    frame_tables = {}
    for stock, base, name in WITNESSES:
        for ticks in (1, 13):
            table = [[None] * 5 for _ in range(5)]
            site = ticks % 5
            reader = reader_word_at(site)
            for m in range(5):
                native_word = clock_word(m)
                ticked = repeat(delta, native_word, ticks)
                exponent = (m * ticks + ticks // 5) % 5
                require(ticked[2 * site:2 * site + 2] ==
                        (POWERS[exponent], scaled(-1, POWERS[exponent])),
                        "literal clock reaches declared port and amplitude")
                require(account_sum(ticked) == 4, "native clock preparation account")
                unrotated_initial = ticked + (stock,)
                unrotated_final = execute(unrotated_initial, reader)
                for s in range(5):
                    reference = multiply(POWERS[s], stock)
                    initial = ticked + (reference,)
                    final = execute(initial, reader)
                    reading = account(final[10])
                    table[s][m] = reading
                    require(reading == base[(exponent - s) % 5],
                            "actual clock reads only relative phase")
                    require(account_sum(final) == 4 + account(stock),
                            "actual clock and stock complete account")
                    restored = execute(final, inverse(reader))
                    require(restored == initial, "actual relative-frame receiver inverse")
                    require(repeat(restored, inverse(native_word), ticks) == delta + (reference,),
                            "entire clock and receiver inverse preserves stock")
                for unit in UNITS:
                    rotated_start = rotate_state(unit, delta + (stock,))
                    rotated_ticked = repeat(rotated_start, native_word, ticks)
                    rotated_final = execute(rotated_ticked, reader)
                    require(rotated_final == rotate_state(unit, unrotated_final),
                            "complete actual clock and stock simultaneous covariance")
                    require(account(rotated_final[10]) == account(unrotated_final[10]),
                            "complete frame rotation leaves clock readout unchanged")
            frame_tables[name + "_ticks_" + str(ticks)] = table
    require(frame_tables["Q22_S_ticks_1"][0] == list(SMALL_READINGS),
            "small stock one-tick response")
    require(frame_tables["Q22_S_ticks_13"][0] == [22, 12, 2, 7, 17],
            "small stock thirteen-tick response")

    require(frame_tables["Q22_T_ticks_1"][0] == list(NORMALIZED_READINGS),
            "normalized small stock one-tick response")
    require(frame_tables["Q22_T_ticks_13"][0] == [2, 22, 7, 12, 17],
            "normalized small stock thirteen-tick response")

    print("NON-CANONICAL / L1; exact author-side fixed-word stock census")
    print("external_informal_assertion_count=not_reproduced")
    print("complete_coefficient_box=11^4=14641; Q_cutoff=32")
    print("norm_bounded_candidates=" + str(bounded_candidates))
    print("successful_by_Q=" + json.dumps(counts, separators=(",", ":")))
    print("successful_total=" + str(len(successful)))
    print("successful_records_sha256=" + canonical_digest(successful))
    print("minimum_record=" + json.dumps(minimum, sort_keys=True, separators=(",", ":")))
    print("normalized_small_stock=1,2,0,-2; Q=22; readings=22,12,2,7,17")
    print("alternative_small_stock=2,-2,1,0; Q=22; readings=12,7,22,2,17")
    print("small_high_pair_accounts=26,48; small_two_pair_accounts=30,52")
    print("unrestricted_small_box=5^4=625; successful=" + str(len(box_successful)))
    print("small_box_successful_by_Q=" + json.dumps(box_counts, separators=(",", ":")))
    print("small_box_records_sha256=" + canonical_digest(box_successful))
    print("relative_frame_tables=" + json.dumps(frame_tables, sort_keys=True, separators=(",", ":")))
    print("simultaneous_units=10; raw_occupied_triples=125")
    print("assertions=" + str(ASSERTIONS))
    print("PASS")


if __name__ == "__main__":
    run()