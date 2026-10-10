#!/usr/bin/env python3
"""Exact, self-contained audit; analytical answers were exposed before pinning.

This file is a proposed audit, not an execution record or an admission of its
conditional interaction. Only Python's standard library and integer F5
arithmetic are used. It does not import any existing scientific program.
"""

from itertools import product
from hashlib import sha256
import json


FIELD = range(5)
TRIGGERS = (4, 5, 6, 9, 16, 31, 64)
TAIL_HORIZON = 64
TAIL_GENERATORS = (1, 3, 4)


def require(condition, description):
    if not condition:
        raise AssertionError(description)


def theta(n):
    return n.bit_count() & 1


def generator(index, v):
    a, b, c, d, q, r = v
    if index == 0:
        result = (b, a, d, c, q, r)
    elif index == 1:
        result = (-c, -d, -a, -b, -q, -r)
    elif index == 2:
        result = (2 - c, 1 - d + r, 2 - a, 1 - b - r, 1 - q, -r)
    elif index == 3:
        result = (2 - a, 1 - b, 3 - c, 4 - d, 1 - q, 1 - r)
    elif index == 4:
        result = (2 - a, 1 - b, 3 - c, 4 - d, 2 - q, 1 - r)
    else:
        raise ValueError("invalid native generator")
    return tuple(value % 5 for value in result)


def native(n, v):
    return generator((sum(v) + 2 * theta(n)) % 5, v)


def centered_pair(v):
    return (v[0] - 1) % 5, (v[2] - 4) % 5


def representative_f(x, y):
    return 2 * (y - x) % 5


def contact(v, source):
    """The representative contact on every complete checkpoint, not a chart."""
    x, y = centered_pair(v)
    shift = representative_f(x, y) * source % 5
    return (v[0], (v[1] - shift) % 5, v[2], (v[3] + shift) % 5, v[4], v[5])


def memory(v):
    return 2 * ((v[0] - 1) * (v[1] - 3) + (v[2] - 4) * (v[3] - 2)) % 5


def reader(v):
    piston_sum = sum(v[:4]) % 5
    local = (v[0] + v[3]) % 5
    return ((1 - piston_sum * piston_sum) * local
            + piston_sum * piston_sum * memory(v)) % 5


def prepare(old_value, first_source):
    return (old_value, 0, -old_value % 5, 0, -first_source % 5, first_source)


def augmented(state, trigger):
    n, v, source = state
    if n == trigger:
        v = contact(v, source)
    return n + 1, native(n, v), source


def reached_trace(n):
    """Trace on the actual time image of the whole initial H0."""
    if n < 2:
        return 0
    if n == 2:
        return 2
    return (4 + 2 * theta(n - 1)) % 5


def inverse_on_reached_time_slice(state, trigger):
    n, v, source = state
    require(n > 0, "partial inverse excludes the initial time boundary")
    require(sum(v) % 5 == reached_trace(n), "inverse requires the reached sheet")
    previous_n = n - 1
    index = (reached_trace(previous_n) + 2 * theta(previous_n)) % 5
    previous_v = generator(index, v)
    if previous_n == trigger:
        previous_v = contact(previous_v, -source)
    require(sum(previous_v) % 5 == reached_trace(previous_n), "inverse sheet")
    return previous_n, previous_v, source


def table_from_parameters(parameters):
    """Six free values F(c,h), c=0,1,2 and h=1,2, in that order."""
    values = []
    for x, y in product(FIELD, repeat=2):
        c = (x + y) % 5
        h = (y - x) % 5
        if h == 0:
            values.append(0)
            continue
        canonical_c = min(c, (-c) % 5)
        canonical_h = min(h, (-h) % 5)
        sign = 1 if h == canonical_h else -1
        values.append(sign * parameters[2 * canonical_c + canonical_h - 1] % 5)
    return tuple(values)


def at(table, x, y):
    return table[5 * (x % 5) + y % 5]


def audit_class():
    # Independently construct the signed chart orbits and their partition.
    occupied = set()
    sizes = []
    for c, h in product(range(3), (1, 2)):
        orbit = {((sign_c * c) % 5, (sign_h * h) % 5)
                 for sign_c, sign_h in product((1, -1), repeat=2)}
        require(not occupied.intersection(orbit), "six orbits must be disjoint")
        occupied.update(orbit)
        sizes.append(len(orbit))
    forced_zero = {(c, 0) for c in FIELD}
    require(sizes == [2, 2, 4, 4, 4, 4], "signed orbit sizes")
    require(occupied | forced_zero == set(product(FIELD, repeat=2)), "whole chart")
    require(not occupied.intersection(forced_zero), "zero and free orbits")

    distinct = set()
    point_checks = 0
    survivors = set()
    tail_orbit = ((4, 2), (3, 1), (1, 3), (2, 4))
    for parameters in product(FIELD, repeat=6):
        table = table_from_parameters(parameters)
        require(table not in distinct, "different parameters must give distinct laws")
        distinct.add(table)
        for x, y in product(FIELD, repeat=2):
            value = at(table, x, y)
            require(at(table, -x, -y) == -value % 5, "joint odd symmetry")
            require(at(table, y, x) == -value % 5, "exchange odd symmetry")
            require(at(table, -y, -x) == value, "literal b covariance")
            if x == y:
                require(value == 0, "diagonal is forced zero")
            point_checks += 1

        # Compare the target on the whole orbit, not just the chosen coefficient.
        survivor = all(2 * (y - x) * at(table, x, y) % 5 == 1
                       for x, y in tail_orbit)
        require(survivor == (parameters[3] == 4), "one and only one target constraint")
        if survivor:
            survivors.add(table)
            for x, y in tail_orbit:
                require(at(table, x, y) == representative_f(x, y),
                        "all survivors agree as complete maps on the tail orbit")

    require(len(distinct) == 15625, "complete declared class count")
    require(point_checks == 390625, "all class points audited")
    require(len(survivors) == 3125, "target survivor count")
    linear_members = []
    for alpha, beta in product(FIELD, repeat=2):
        table = tuple((alpha * x + beta * y) % 5 for x, y in product(FIELD, repeat=2))
        if table in survivors:
            linear_members.append((alpha, beta))
    require(linear_members == [(3, 2)], "unique normalized linear member")
    # Sort complete point-value tables, not their six-parameter encodings.
    class_bytes = b"".join(sorted(bytes(table) for table in distinct))
    target_bytes = b"".join(sorted(bytes(table) for table in survivors))
    return {
        "class_maps": len(distinct),
        "class_point_checks": point_checks,
        "target_maps": len(survivors),
        "class_sha256": sha256(class_bytes).hexdigest(),
        "target_sha256": sha256(target_bytes).hexdigest(),
        "linear_coefficients": list(linear_members[0]),
    }


def audit_full_contact():
    pairs = inverse_checks = commutation_checks = change_checks = 0
    for v in product(FIELD, repeat=6):
        before = memory(v)
        x, y = centered_pair(v)
        for source in FIELD:
            pairs += 1
            changed = contact(v, source)
            require(contact(changed, -source) == v, "full contact left inverse")
            require(contact(contact(v, -source), source) == v, "full contact right inverse")
            inverse_checks += 1
            require((changed[0], changed[2], changed[4], changed[5])
                    == (v[0], v[2], v[4], v[5]), "dirty fixed coordinates")
            require(sum(changed[:4]) % 5 == sum(v[:4]) % 5, "complete piston sum")
            require(sum(changed) % 5 == sum(v) % 5, "complete trace")
            expected = (before + 2 * (y - x) * representative_f(x, y) * source) % 5
            require(memory(changed) == expected, "full carrier M change")
            change_checks += 1
            for index in TAIL_GENERATORS:
                require(generator(index, changed) == contact(generator(index, v), source),
                        "literal whole-state tail generator commutation")
                commutation_checks += 1
    require(pairs == 78125, "all full checkpoint/source pairs")
    return {
        "full_carrier_source_pairs": pairs,
        "full_contact_inverse_checks": inverse_checks,
        "full_generator_commutation_checks": commutation_checks,
        "full_m_change_checks": change_checks,
    }


def audit_prepared_histories():
    trajectories = state_boundaries = source_boundaries = step_inverse_checks = 0
    first_records = second_records = initial_records = 0
    for trigger in TRIGGERS:
        horizon = trigger + TAIL_HORIZON
        for old_value, first_source, second_source in product(FIELD, repeat=3):
            trajectories += 1
            initial_v = prepare(old_value, first_source)
            state = (0, initial_v, second_source)
            native_v = initial_v
            for n in range(horizon + 1):
                actual_n, actual_v, actual_source = state
                require(actual_n == n, "one native counter without reset")
                require((actual_v[4], actual_v[5], actual_source)
                        == (native_v[4], native_v[5], second_source),
                        "actual native q,r and added source retained at every boundary")
                source_boundaries += 1
                expected_v = native_v if n <= trigger else contact(native_v, second_source)
                require(actual_v == expected_v, "complete state continuation formula")
                require(sum(actual_v) % 5 == reached_trace(n), "actual chronology sheet")
                state_boundaries += 1

                if n == 0:
                    require(reader(actual_v) == old_value, "same reader on initial occupied state")
                    initial_records += 1
                elif 3 <= n <= trigger:
                    require(reader(actual_v) == (old_value + first_source) % 5,
                            "first record at every declared boundary")
                    first_records += 1
                elif n > trigger:
                    require(reader(actual_v) == (old_value + first_source + second_source) % 5,
                            "second record at every declared boundary")
                    second_records += 1

                if n == 3:
                    target = (0, -(old_value + first_source) % 5, 1,
                              (old_value + first_source + 3) % 5,
                              (1 - first_source) % 5, (1 + first_source) % 5)
                    require(actual_v == target, "literal complete first output")
                if n == horizon:
                    break
                following = augmented(state, trigger)
                require(inverse_on_reached_time_slice(following, trigger) == state,
                        "complete restricted step inverse")
                step_inverse_checks += 1
                state = following
                native_v = native(n, native_v)

    require(trajectories == 875, "all prepared trajectories")
    require(state_boundaries == 73750, "all prepared time boundaries")
    require(step_inverse_checks == 72875, "all prepared inverse steps")
    require(first_records == 15125 and second_records == 56000 and initial_records == 875,
            "all meaningful record intervals")
    return {
        "prepared_trajectories": trajectories,
        "prepared_state_boundaries": state_boundaries,
        "prepared_source_boundaries": source_boundaries,
        "prepared_step_inverse_checks": step_inverse_checks,
        "first_record_boundaries": first_records,
        "second_record_boundaries": second_records,
        "initial_record_boundaries": initial_records,
    }


def audit_off_support_boundary():
    witness = (1, 0, 4, 0, 1, 0)
    source = 1
    require(sum(witness) % 5 == 1, "counterexample is in the stable union")
    require(centered_pair(witness) == (0, 0), "counterexample has h zero")
    changed = contact(witness, source)
    require(changed == witness and memory(changed) == memory(witness), "no change at h zero")
    require(memory(changed) != (memory(witness) + source) % 5,
            "global unit-gain extension must fail")
    return {"off_support_unit_counterexample": True}


def audit_global_injectivity_boundary():
    zero = (0, 0, 0, 0, 0, 0)
    other = (2, 1, 2, 1, 1, 0)
    require(zero != other, "distinct initial checkpoints")
    for trigger in TRIGGERS:
        for source in FIELD:
            expected = (1, zero, source)
            require(augmented((0, zero, source), trigger) == expected,
                    "first global-collision branch")
            require(augmented((0, other, source), trigger) == expected,
                    "second global-collision branch")
    return {"global_injectivity_counterexample": True}


def main():
    summary = {}
    summary.update(audit_class())
    summary.update(audit_full_contact())
    summary.update(audit_prepared_histories())
    summary.update(audit_off_support_boundary())
    summary.update(audit_global_injectivity_boundary())
    summary["trigger_times"] = list(TRIGGERS)
    summary["tail_horizon"] = TAIL_HORIZON
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
