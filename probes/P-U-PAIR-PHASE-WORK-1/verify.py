#!/usr/bin/env python3
"""Exact native paired phase audit. A. M. Thorn. NON-CANONICAL / L1."""
# SPDX-License-Identifier: Apache-2.0

from itertools import product


def theta(counter):
    return counter.bit_count() % 2


def trace(checkpoint):
    return sum(checkpoint) % 5


def native_tick(counter, checkpoint):
    p1, p2, p3, p4, q, r = checkpoint
    selector = (trace(checkpoint) + 2 * theta(counter)) % 5
    if selector == 1:
        image = (-p3, -p4, -p1, -p2, -q, -r)
    elif selector in (3, 4):
        image = (2 - p1, 1 - p2, 3 - p3, 4 - p4, selector - 2 - q, 1 - r)
    else:
        raise AssertionError((counter, checkpoint, selector))
    return tuple(value % 5 for value in image)


def chart(checkpoint):
    p1, p2, p3, p4, _, r = checkpoint
    z = trace(checkpoint)
    assert z in (1, 4)
    sheet = int(z == 4)
    sign = 1 - 2 * sheet
    pistons = (p1 + p3, p2 + p4, sign * (p1 - p3 - 2), sign * (p2 - p4 - 1))
    hand = r + 5 * ((sheet - r) % 2)
    return tuple(value % 5 for value in pistons), sheet, hand


def clock_read(counter):
    return counter % 5, theta(counter - 1), theta(counter)


def projected_read(counter, checkpoint):
    return checkpoint[:4], trace(checkpoint), clock_read(counter)


def native_history(initial):
    checkpoints = [initial]
    lifts = [initial[-1]]
    for counter in range(32):
        old = checkpoints[-1]
        old_chart, old_sheet, _ = chart(old)
        kick = old_sheet ^ theta(counter)
        new = native_tick(counter, old)
        new_chart, new_sheet, _ = chart(new)
        lifted_r = -lifts[-1] + kick
        assert new_sheet == 1 - theta(counter)
        assert new_chart == tuple(-value % 5 for value in old_chart)
        assert new[-1] == lifted_r % 5
        checkpoints.append(new)
        lifts.append(lifted_r)
    return checkpoints, lifts


def audit_native():
    preparations = 0
    pair_checks = 0
    for z in (1, 4):
        for *pistons, r in product(range(5), repeat=5):
            q = (z - sum(pistons) - r) % 5
            checkpoints, lifts = native_history((*pistons, q, r))
            for start in range(1, 31):
                end = start + 2
                k = (start + 1) // 2
                event = theta(k - 1) ^ theta(k)
                shift = event if start % 2 else -event
                old_v, old_h, old_hand = chart(checkpoints[start])
                new_v, new_h, new_hand = chart(checkpoints[end])
                assert new_v == old_v and new_h == old_h ^ event
                assert (new_hand - old_hand) % 10 == shift % 10
                assert lifts[end] - lifts[start] == shift
                pair_checks += 1
            assert projected_read(1, checkpoints[1]) == projected_read(11, checkpoints[11])
            assert projected_read(11, checkpoints[11]) == projected_read(21, checkpoints[21])
            assert (lifts[11] - lifts[1], lifts[21] - lifts[11]) == (4, 2)
            assert checkpoints[1] == checkpoints[31] and clock_read(1) == clock_read(31)
            assert checkpoints[2] == checkpoints[32] and clock_read(2) == clock_read(32)
            assert (lifts[31] - lifts[1], lifts[32] - lifts[2]) == (10, -10)
            preparations += 1
    assert preparations == 6250 and pair_checks == 187500
    print(f"PASS NATIVE preparations={preparations} ticks=32 paired_checks={pair_checks}")
    print("PASS MATCHED starts=1,11 ticks=10,10 lifted_shifts=4,2 marked_clock_equal=True")
    print("PASS RETURNS intervals=1:31,2:32 lifted_shifts=10,-10 full_checkpoint=True")
    stationary = (1, 3, 4, 2, 1, 0)
    checkpoints, _ = native_history(stationary)
    assert all(state[:4] == stationary[:4] for state in checkpoints)
    print("PASS PISTONS fixed=1,3,4,2 all_ticks=32")


def valuation_count(horizon):
    total = 0
    power = 1
    while power <= horizon:
        total += horizon // power - horizon // (2 * power)
        power *= 4
    return total


def digit_difference(value):
    difference = 0
    while value:
        value, digit = divmod(value, 4)
        difference += int(digit == 1) - int(digit == 2)
    return difference


def audit_discrepancy():
    prefix = 0
    discrepancies = [0]
    for horizon in range(1, 4097):
        valuation = (horizon & -horizon).bit_length() - 1
        event = theta(horizon - 1) ^ theta(horizon)
        assert event == int(valuation % 2 == 0)
        prefix += event
        assert prefix == valuation_count(horizon)
        difference = 3 * prefix - 2 * horizon
        assert difference == digit_difference(horizon)
        discrepancies.append(difference)
    assert discrepancies[0] == digit_difference(0) == 3 * valuation_count(0)
    for digits in range(1, 65):
        all_ones = (4**digits - 1) // 3
        all_twos = 2 * all_ones
        for horizon, expected in ((all_ones, digits), (all_twos, -digits)):
            assert 3 * valuation_count(horizon) - 2 * horizon == expected
            assert digit_difference(horizon) == expected
        if digits <= 6:
            covered = discrepancies[:4**digits]
            assert min(covered) == -digits and max(covered) == digits
            funded = [digits + difference for difference in covered]
            assert min(funded) == 0 and max(funded) == 2 * digits
    print("PASS DISCREPANCY M=0..4096 base=4 digit_weights=0,1,-1,0")
    print("PASS BALANCE full_ranges_s=1..6 extreme_witnesses_s=1..64 min_capacity=2s")


def main():
    if not __debug__:
        raise RuntimeError("Assertions must be enabled")
    print("P-U-PAIR-PHASE-WORK-1 NON-CANONICAL L1 EXACT")
    audit_native()
    audit_discrepancy()
    print("RESULT PASS; universal bounded-work statement in PROOF.md")


if __name__ == "__main__":
    main()
