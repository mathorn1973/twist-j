# SPDX-License-Identifier: Apache-2.0
"""Bounded H3 distance and stock sweep under the native matching."""

HORIZON = 85
ORIENTATIONS = ("low", "high")


def power(h3, word, exponent):
    result = h3.ONE
    for _ in range(exponent):
        result = h3.mul(result, word)
    return result


def launch(native, p, distance, orientation, u, u_inverse, target_word):
    h3 = native.h3
    field = native.empty()
    amplitude = 2**p
    radiation = h3.scale(amplitude, h3.ONE)
    forward, compensator = (u, u_inverse) if orientation == "low" else (u_inverse, u)
    for y in range(4):
        material = h3.scale(amplitude, forward if y < 2 else compensator)
        words = (material, h3.scale(-1, material), radiation, h3.scale(-1, radiation))
        for x in (0, 1):
            native.put(field, x, y, words)
    native.put(field, 1 + distance, 1,
               (target_word, h3.scale(-1, target_word), h3.ZERO, h3.ZERO))
    return tuple(field)


def compare(low, high, key):
    return next((tick for tick, (left, right) in enumerate(zip(low[key], high[key]), 1)
                 if left != right), None)


def audit(native, p, distance, orientation, u, u_inverse, target_word):
    h3 = native.h3
    target = (1 + distance, 1)
    arrival = distance + 1
    amplitude = 2**p
    emitted_unit = h3.J if orientation == "low" else h3.J_INV
    initial = launch(native, p, distance, orientation, u, u_inverse, target_word)
    target_initial = native.cell(initial, *target)
    stock_h = h3.add(h3.scale(40 * amplitude**2, h3.ONE), h3.scale(2, h3.h(target_word)))
    stock = (h3.ZERO, h3.ZERO, stock_h, 80 * amplitude**2 + 10)
    h3.require(native.ledger(initial) == stock, "complete initial sweep stock")

    expected_earliest_corr = h3.ZERO
    if distance <= p:
        expected_earliest_corr = h3.scale(
            -(2 ** (p - distance)), h3.mul(power(h3, target_word, distance), emitted_unit)
        )
    field = initial
    records = {"corr_C": [], "corr_B": [], "tag": []}
    exponent = 0
    first_write = None
    first_corr = None
    counts = [0, 0]
    for tick in range(1, HORIZON + 1):
        bit = (tick - 1) % 2
        post_c, post_b, events = native.step(field, bit)
        h3.require(native.ledger(post_c) == native.ledger(post_b) == stock, "substep stock conservation")
        h3.require(tuple(native.reverse(post_b, bit)) == field, "native tick inverse")
        before, at_c, at_b = (native.cell(cut, *target) for cut in (field, post_c, post_b))
        local_tags = tuple(tag for x, y, tag in events if (x, y) == target)
        h3.require(len(local_tags) <= 1, "target has at most one branch per tick")
        tag = local_tags[0] if local_tags else 0
        if tick < arrival:
            h3.require(before == at_c == at_b == target_initial and tag == 0, "strict causal absence")
        if tick == arrival:
            h3.require(at_c[:3] == target_initial[:3], "earliest causal contact is horizontal CORR")
            h3.require(at_c[3] == expected_earliest_corr, "earliest CORR parity and amplitude")
            if p == 2:
                expected_tag = (1 if orientation == "low" else 2) if distance == 1 else 0
                h3.require(tag == expected_tag, "p=2 earliest-window receiver controls")
                if distance == 2:
                    h3.require(not h3.even(at_c[3]), "p=2 distance-two field is odd")
        h3.require(not h3.even(before[0]) and at_c[:2] == before[:2], "odd target refuses vertical C")
        h3.require(
            all(native.cell(cut, target[0], y)[:2] == (h3.ZERO, h3.ZERO)
                for cut in (post_c, post_b) for y in (0, 2, 3)),
            "no other material in the target column",
        )
        h3.require(at_b[1] == h3.scale(-1, at_b[0]), "target material remains antipodal")
        h3.require((at_b[:2] != at_c[:2]) == bool(tag), "target write agrees with native branch")
        if tag:
            counts[tag - 1] += 1
            if first_write is None:
                first_write = tick
            exponent += 1 if tag == 1 else -1
            unit = h3.J if tag == 1 else h3.J_INV
            h3.require(at_b[0] == h3.mul(at_c[0], unit), "native target gap multiplier")
        if first_corr is None and at_c[3] != h3.ZERO:
            first_corr = tick
        records["corr_C"].append(at_c[3])
        records["corr_B"].append(at_b[3])
        records["tag"].append(tag)
        field = tuple(post_b)

    unit = h3.J if exponent >= 0 else h3.J_INV
    final_power = h3.mul(target_word, power(h3, unit, abs(exponent)))
    h3.require(native.cell(field, *target)[0] == final_power, "terminal target exponent")
    restored = field
    for tick in range(HORIZON, 0, -1):
        restored = tuple(native.reverse(restored, (tick - 1) % 2))
    h3.require(restored == initial, "whole-terminal inverse")

    summary = {
        "first_nonzero_CORR": first_corr,
        "first_material_B_write": first_write,
        "B1_B2_counts": counts,
        "terminal_J_exponent": exponent,
        "earliest_CORR_j_coordinates": list(records["corr_C"][arrival - 1]),
        "earliest_target_B": records["tag"][arrival - 1],
    }
    return records, summary


def run(native):
    h3 = native.h3
    target_word = h3.sub(h3.ONE, h3.RHO)
    u = h3.add(h3.J_POWERS[1], h3.J_POWERS[4])
    inverse_coordinates = h3.inverse(u)
    h3.require(all(value.denominator == 1 for value in inverse_coordinates), "integral source unit inverse")
    u_inverse = tuple(map(int, inverse_coordinates))
    h3.require(h3.mul(u, u_inverse) == h3.ONE, "source unit inverse")
    h3.require(not h3.even(target_word), "target is in the nonzero parity class")
    h3.require(h3.scalar_account(h3.scale(2, h3.h(target_word))) == 10, "target scalar stock")
    matrix = []
    for p in (1, 2, 3, 4):
        for distance in (1, 2, 3):
            low, high = (
                audit(native, p, distance, sign, u, u_inverse, target_word)
                for sign in ORIENTATIONS
            )
            matrix.append({
                "p": p,
                "distance": distance,
                "low": low[1],
                "high": high[1],
                "first_different_CORR": compare(low[0], high[0], "corr_C"),
                "first_different_post_B_CORR": compare(low[0], high[0], "corr_B"),
                "first_different_target_B": compare(low[0], high[0], "tag"),
            })
    return {"launches": 24, "ticks_per_launch": HORIZON, "matrix": matrix}
