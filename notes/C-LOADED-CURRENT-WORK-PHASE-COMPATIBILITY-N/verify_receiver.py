#!/usr/bin/env python3
"""Exact, bounded receiver and native clock audit; NON-CANONICAL / L1.

This independently written verifier uses only the Python standard library.
It does not import or rerun the earlier reduced or full-field verifiers.
Run only after this source and RECEIVER-PREREG.md have a public immutable pin.
"""
from itertools import product

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
JROOT = (0, 1, 0, 0)
ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return add(a, neg(b))


def times(n, a):
    return tuple(n * x for x in a)


def mul(a, b):
    coeff = [0] * 7
    for i in range(4):
        for k in range(4):
            coeff[i + k] += a[i] * b[k]
    for degree in range(6, 3, -1):
        value = coeff[degree]
        coeff[degree] = 0
        for shift in range(1, 5):
            coeff[degree - shift] -= value
    return tuple(coeff[:4])


ROOTS = [ONE]
for _ in range(4):
    ROOTS.append(mul(ROOTS[-1], JROOT))
ROOTS = tuple(ROOTS)
RHO = ROOTS[2]
J = add(ONE, RHO)
A = (1, 2, 1, 0)
STOCK = (3, 4, 2, 0)
PHI = (0, 0, -1, -1)
ALPHABET = (ZERO, ONE, JROOT, RHO, ROOTS[3], neg(ONE), J, A, STOCK)


def q(a):
    numerator = 5 * sum(x * x for x in a) - sum(a) ** 2
    if numerator % 2:
        raise ArithmeticError("nonintegral quadratic account")
    return numerator // 2


def total_q(state):
    return sum(q(a) for a in state)


def total_sum(state):
    result = ZERO
    for a in state:
        result = add(result, a)
    return result


def contact(a, b):
    difference = sub(a, b)
    if any(x % 2 for x in difference):
        return a, b, False
    center = tuple(x // 2 for x in add(a, b))
    relative = tuple(x // 2 for x in difference)
    rotated = mul(RHO, relative)
    return add(center, rotated), sub(center, rotated), True


def apply_word(state, word, audit=True):
    current = tuple(state)
    history = []
    for kind, left, right in word:
        before = current
        changed = list(current)
        if kind == "C":
            changed[left], changed[right], accepted = contact(
                current[left], current[right])
        elif kind == "S":
            changed[left], changed[right] = current[right], current[left]
            accepted = None
        else:
            raise ValueError(kind)
        current = tuple(changed)
        history.append((accepted, current))
        if audit:
            check(total_q(current) == total_q(before), "local account")
            check(total_sum(current) == total_sum(before), "local sum")
            if accepted is False:
                check(current == before, "literal refusal identity")
    return current, tuple(history)


def inverse_word(word):
    answer = []
    for kind, left, right in reversed(word):
        answer.extend([(kind, left, right)] * (4 if kind == "C" else 1))
    return tuple(answer)


RECEIVER_WORD = tuple(
    operation for _ in range(5) for operation in (("C", 0, 2), ("C", 0, 1)))
RECEIVER_INVERSE = inverse_word(RECEIVER_WORD)
FINAL_Q = (32, 17, 2, 7, 27)
STOCK_STATES = (
    (1, 1, 1, 1),
    (3, 2, 0, -1),
    (2, 3, 3, 1),
    (1, 0, -1, -1),
    STOCK,
)
STOCK_Q = (2, 27, 17, 7, 32)


def receiver(b, low=None, neutral_stock=False):
    state = (ROOTS[b], neg(ROOTS[b]), STOCK)
    if low is not None:
        state += (ROOTS[low], neg(ROOTS[low]))
    if neutral_stock:
        state += (neg(STOCK),)
    result, history = apply_word(state, RECEIVER_WORD)
    return state, result, history


def encoded(label):
    return (ROOTS[label // 5], neg(ROOTS[label // 5]), STOCK,
            ROOTS[label % 5], neg(ROOTS[label % 5]))


def neutral_clock(amplitudes):
    return tuple(slot for amplitude in amplitudes
                 for slot in (amplitude, neg(amplitude)))


def amplitudes(state):
    check(all(state[2 * k + 1] == neg(state[2 * k]) for k in range(5)),
          "neutral clock carrier")
    return tuple(state[2 * k] for k in range(5))


def clock_formula(values, m):
    return (mul(ROOTS[(m + 1) % 5], values[4]),) + tuple(
        mul(ROOTS[m], values[k]) for k in range(4))


def swaps_word():
    return tuple(operation for left, right in ((3, 4), (2, 3), (1, 2), (0, 1))
                 for operation in (("S", 2 * left, 2 * right),
                                   ("S", 2 * left + 1, 2 * right + 1)))


def clock_word(m, padded=False):
    word = list(swaps_word())
    if padded:
        word.extend([("C", 0, 1)] * 3)
        turns = (3 * m) % 5
        for k in range(5):
            word.extend([("C", 2 * k, 2 * k + 1)] * turns)
        word.extend([("C", 8, 9)] * (5 * (4 - turns)))
    else:
        for k in range(5):
            turns = (3 * (m + (k == 0))) % 5
            word.extend([("C", 2 * k, 2 * k + 1)] * turns)
    return tuple(word)


def repeat_word(state, word, count, audit=False):
    for _ in range(count):
        state, _ = apply_word(state, word, audit=audit)
    return state


def fifth_clock_target(state):
    word = tuple(("C", 2 * k, 2 * k + 1) for k in range(5) for _ in range(3))
    return apply_word(state, word, audit=False)[0]


def dense_clock_fixtures():
    return (
        (ZERO, ZERO, ZERO, ZERO, ZERO),
        (ONE, ZERO, ZERO, ZERO, ZERO),
        (ZERO, ZERO, ZERO, ZERO, J),
        (ONE, JROOT, RHO, ROOTS[3], J),
        (STOCK, A, neg(ONE), ZERO, PHI),
        tuple(times(2, a) for a in (ONE, JROOT, RHO, ROOTS[3], J)),
        (ONE, ZERO, J, ZERO, neg(JROOT)),
        (ONE, ONE, ONE, ONE, ONE),
    )


def run():
    check(mul(ROOTS[4], JROOT) == ONE, "root order five")
    check(q(A) == 7 and q(add(ONE, A)) == 10 and q(STOCK) == 32,
          "frozen stock accounts")
    check(len(RECEIVER_WORD) == 10 and len(RECEIVER_INVERSE) == 40,
          "literal receiver word lengths")
    check(len(set(FINAL_Q)) == 5, "injective terminal stock energy")
    for n in range(1, 6):
        expected = add(add(ONE, A), mul(ROOTS[(2 * n) % 5], A))
        check(expected == STOCK_STATES[n - 1], "closed stock state formula")
        check(q(expected) == STOCK_Q[n - 1], "closed stock account formula")

    # Complete ordered alphabet-pair controls: powers zero through five.
    for left, right in product(ALPHABET, repeat=2):
        current = (left, right)
        for count in range(6):
            check(total_q(current) == q(left) + q(right), "pair-power account")
            check(total_sum(current) == add(left, right), "pair-power sum")
            if count == 5:
                check(current == (left, right), "global C fifth power")
            else:
                current, _ = apply_word(current, (("C", 0, 1),))
        result, _ = apply_word((left, right), (("C", 0, 1),))
        restored, _ = apply_word(result, (("C", 0, 1),) * 4)
        check(restored == (left, right), "global C inverse")

    # Five prepared high digits, including every per-block admission.
    for b in range(5):
        initial, result, history = receiver(b)
        hit = (2 * b) % 5
        check(total_q(initial) == 36 and total_q(result) == 36,
              "unscaled high pointer plus fixed stock")
        check(q(result[2]) == FINAL_Q[b], "five digit calorimetric signature")
        check(q(result[0]) + q(result[1]) == 36 - FINAL_Q[b],
              "active stock release retained as pointer backreaction")
        for block in range(5):
            n = max(0, block - hit + 1)
            check(history[2 * block][0] == (block >= hit), "stock admission")
            check(history[2 * block + 1][0] == (block < hit or n == 5),
                  "high-pair admission")
            expected_stock = STOCK if n == 0 else STOCK_STATES[n - 1]
            check(history[2 * block][1][2] == expected_stock,
                  "stock state after its contact")
            check(history[2 * block + 1][1][2] == expected_stock,
                  "pointer contact leaves stock untouched")
        restored, _ = apply_word(result, RECEIVER_INVERSE)
        check(restored == initial, "prepared receiver inverse")
        neutral_initial, neutral_result, _ = receiver(b, neutral_stock=True)
        check(total_sum(neutral_initial) == ZERO and total_sum(neutral_result) == ZERO,
              "optional neutral stock companion")
        check(total_q(neutral_result) == 68, "optional neutral companion account")

    # All 25 physical pointer labels, with both low slots preserved.
    for label in range(25):
        initial = encoded(label)
        result, _ = apply_word(initial, RECEIVER_WORD)
        check(q(result[2]) == FINAL_Q[label // 5], "all label high-digit read")
        check(result[3:] == initial[3:], "low pair retained")
        check(total_q(result) == 40, "full encoded pointer and stock account")
        neutral = initial + (neg(STOCK),)
        neutral_result, _ = apply_word(neutral, RECEIVER_WORD)
        check(total_q(neutral_result) == 72 and total_sum(neutral_result) == ZERO,
              "full encoded pointer with neutral stock companion")
        restored, _ = apply_word(result, RECEIVER_INVERSE)
        check(restored == initial, "all label complete inverse")

    # Real reencodings versus merely changing the character name.
    for label in range(25):
        readings = []
        for t in range(5):
            relabelled = ((1 + 5 * t) * label) % 25
            state = encoded(relabelled)
            result, _ = apply_word(state, RECEIVER_WORD)
            readings.append(q(result[2]))
            check(relabelled % 5 == label % 5, "reencoding low digit fixed")
        check(len(set(readings)) == (1 if label % 5 == 0 else 5),
              "reencoding discrimination exactly for unit low digit")
    witness_labels = tuple(((1 + 5 * t) * 13) % 25 for t in range(5))
    check(witness_labels == (13, 3, 18, 8, 23), "frozen witness labels")
    witness_q = tuple(q(apply_word(encoded(label), RECEIVER_WORD)[0][2])
                      for label in witness_labels)
    check(witness_q == (2, 32, 7, 17, 27), "frozen reencoded witness outputs")
    check(tuple(value - 32 for value in witness_q) == (-30, 0, -25, -15, -5),
          "signed receiver stock work at reencoded witness")
    same_physical_result = apply_word(encoded(13), RECEIVER_WORD)[0]
    for _t in range(5):
        result, _ = apply_word(encoded(13), RECEIVER_WORD)
        check(result == same_physical_result and q(result[2]) == 2,
              "character name alone cannot alter physical receiver")

    # Exhaustive 9^3 occupied triples: no prepared-pair restriction.
    for state in product(ALPHABET, repeat=3):
        result, _ = apply_word(state, RECEIVER_WORD)
        restored, _ = apply_word(result, RECEIVER_INVERSE)
        check(restored == state, "raw occupied receiver inverse")
        check(total_q(result) == total_q(state), "raw receiver complete account")
        check(total_sum(result) == total_sum(state), "raw receiver complete sum")
    refusing = (ONE, JROOT, ZERO)
    for kind, left, right in RECEIVER_WORD:
        check(kind == "C" and any(x % 2 for x in sub(refusing[left], refusing[right])),
              "explicit all-refused input")
    refused_result, refused_history = apply_word(refusing, RECEIVER_WORD)
    check(refused_result == refusing and all(not accepted for accepted, _ in refused_history),
          "all-refused receiver word is identity")

    # Native clock words, prescribed neutral amplitude formula and fixed calendar.
    basis_fixtures = []
    for site in range(5):
        for value in ALPHABET:
            fixture = [ZERO] * 5
            fixture[site] = value
            basis_fixtures.append(tuple(fixture))
    clock_fixtures = tuple(basis_fixtures) + dense_clock_fixtures()
    raw_clock_fixtures = tuple(
        tuple(ALPHABET[(offset + 2 * k + k * k) % len(ALPHABET)] for k in range(10))
        for offset in range(9))
    for m in range(5):
        word = clock_word(m)
        padded_word = clock_word(m, padded=True)
        check(sum(op[0] == "C" for op in padded_word) == 23
              and sum(op[0] == "S" for op in padded_word) == 8,
              "common supplied attempt calendar")
        for values in clock_fixtures:
            initial = neutral_clock(values)
            result, _ = apply_word(initial, word)
            check(amplitudes(result) == clock_formula(values, m),
                  "native clock equals amplitude formula")
            padded_result, _ = apply_word(initial, padded_word)
            check(padded_result == result, "padded native word same final state")
            restored, _ = apply_word(result, inverse_word(word))
            check(restored == initial, "native clock neutral inverse")
            fifth = repeat_word(initial, word, 5)
            check(fifth == fifth_clock_target(initial), "native clock fifth power")
            check(amplitudes(fifth) == tuple(mul(JROOT, x) for x in values),
                  "clock fifth power j on neutral amplitudes")
        for values in dense_clock_fixtures():
            initial = neutral_clock(values)
            check(repeat_word(initial, word, 25) == initial,
                  "dense neutral clock twenty-fifth power")
        for initial in raw_clock_fixtures:
            result, _ = apply_word(initial, word)
            check(apply_word(initial, padded_word)[0] == result,
                  "padded equality on raw occupied clock")
            check(apply_word(result, inverse_word(word))[0] == initial,
                  "native clock raw occupied inverse")
            check(repeat_word(initial, word, 5) == fifth_clock_target(initial),
                  "raw occupied clock fifth power")
            check(repeat_word(initial, word, 25) == initial,
                  "raw occupied clock twenty-fifth power")

    # One common delta preparation; one fixed known receiver site, every m.
    actual_clock_readings = []
    delta = neutral_clock((ONE, ZERO, ZERO, ZERO, ZERO))
    for m in range(5):
        ticked, _ = apply_word(delta, clock_word(m, padded=True))
        check(ticked[2:4] == (ROOTS[m], neg(ROOTS[m])),
              "one actual native tick reaches known site one")
        check(total_q(ticked) == 4, "clock preparation account four")
        initial = ticked + (STOCK,)
        attached_word = tuple(
            operation for _ in range(5)
            for operation in (("C", 2, 10), ("C", 2, 3)))
        result, _ = apply_word(initial, attached_word)
        actual_clock_readings.append(q(result[10]))
        check(total_q(result) == 36, "clock plus fixed stock account thirty-six")
        check(q(result[10]) == FINAL_Q[m], "actual clock family separated")
        restored, _ = apply_word(result, inverse_word(attached_word))
        check(restored == initial, "attached receiver inverse")
        unticked, _ = apply_word(restored[:10], inverse_word(clock_word(m, padded=True)))
        check(unticked == delta, "complete receiver then clock inverse")
        check(repeat_word(delta, clock_word(m), 5) != delta,
              "nonzero neutral delta has least period twenty-five")
    check(tuple(actual_clock_readings) == FINAL_Q, "actual dynamics readout table")

    # Thirteen controlled native ticks, not a compilation of one field tick.
    thirteenth_readings = []
    for m in range(5):
        word = clock_word(m, padded=True)
        ticked = repeat_word(delta, word, 13)
        exponent = (13 * m + 2) % 5
        check(ticked[6:8] == (ROOTS[exponent], neg(ROOTS[exponent])),
              "thirteenth native tick reaches known site three")
        check(all(ticked[k] == ZERO for k in range(10) if k not in (6, 7)),
              "thirteenth tick remains a single occupied neutral pair")
        initial = ticked + (STOCK,)
        attached_word = tuple(
            operation for _ in range(5)
            for operation in (("C", 6, 10), ("C", 6, 7)))
        result, _ = apply_word(initial, attached_word)
        thirteenth_readings.append(q(result[10]))
        check(total_q(result) == 36, "thirteen-tick experiment complete account")
        check(q(result[10]) == FINAL_Q[exponent], "native thirteen-tick response")
        check(total_q(result[:10]) == 36 - q(result[10]),
              "active stock release remains in complete clock")
        neutral_initial = initial + (neg(STOCK),)
        neutral_result, _ = apply_word(neutral_initial, attached_word)
        check(total_q(neutral_result) == 68 and total_sum(neutral_result) == ZERO,
              "native clock experiment with neutral stock companion")
        check(neutral_result[11] == neg(STOCK), "neutral companion untouched")
        restored, _ = apply_word(result, inverse_word(attached_word))
        check(restored == initial, "thirteen-tick receiver inverse")
        unticked = repeat_word(restored[:10], inverse_word(word), 13)
        check(unticked == delta, "complete thirteen-tick experiment inverse")
    check(tuple(thirteenth_readings) == (2, 32, 7, 17, 27),
          "thirteen actual ticks reproduce witness response")

    print("NON-CANONICAL / L1; exact finite receiver and native-clock audit")
    print("stock_Q=32; receiver_contacts=10; literal_inverse_contacts=40")
    print("high_digit_stock_Q=32,17,2,7,27")
    print("physical_reencoding_labels=13,3,18,8,23")
    print("physical_reencoding_stock_Q=2,32,7,17,27")
    print("fixed_physical_state_stock_Q=2,2,2,2,2")
    print("native_clock_stock_Q=32,17,2,7,27")
    print("native_clock_thirteen_tick_stock_Q=2,32,7,17,27")
    print("witness_stock_work=-30,0,-25,-15,-5")
    print("clock_account=4; clock_plus_stock_account=36; encoded_plus_stock_account=40")
    print("padded_tick_contacts=23; padded_tick_slot_swaps=8")
    print("raw_receiver_triples=729; clock_neutral_fixtures_per_m=53; raw_clock_fixtures=9")
    print("assertions=" + str(ASSERTIONS))
    print("PASS")


if __name__ == "__main__":
    run()