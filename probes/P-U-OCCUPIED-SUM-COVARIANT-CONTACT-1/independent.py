#!/usr/bin/env python3
"""Exact audit by modular linear algebra and centered-coordinate dynamics.

Written independently of primary.py. No imports from another probe or audit.
The analytical target was disclosed before implementation; this is not blind.
"""

import hashlib
import itertools
import json


POINTS = tuple(itertools.product(range(5), repeat=2))
TIMES = (4, 5, 6, 9, 16, 31, 64)
HORIZON = 64


def require(condition, context):
    if not condition:
        raise AssertionError(context)


def parity(n):
    result = 0
    while n:
        result ^= n % 2
        n //= 2
    return result


def reduced_nullspace(rows, width):
    """RREF and a basis for the homogeneous solution space over F5."""
    a = [list(row) for row in rows]
    pivots = []
    for col in range(width):
        found = next((i for i in range(len(pivots), len(a)) if a[i][col]), None)
        if found is None:
            continue
        k = len(pivots)
        a[k], a[found] = a[found], a[k]
        inv = pow(a[k][col], -1, 5)
        a[k] = [(v * inv) % 5 for v in a[k]]
        for i in range(len(a)):
            if i != k and a[i][col]:
                factor = a[i][col]
                a[i] = [(v - factor * w) % 5 for v, w in zip(a[i], a[k])]
        pivots.append(col)
    free = [col for col in range(width) if col not in pivots]
    basis = []
    for col in free:
        vec = [0] * width
        vec[col] = 1
        for row, pivot in enumerate(pivots):
            vec[pivot] = -a[row][col] % 5
        basis.append(vec)
    return pivots, basis


def classification():
    rows = []
    index = {point: i for i, point in enumerate(POINTS)}
    for x, y in POINTS:
        for other in (((-x) % 5, (-y) % 5), (y, x)):
            row = [0] * 25
            row[index[x, y]] += 1
            row[index[other]] += 1
            rows.append([v % 5 for v in row])
    pivots, basis = reduced_nullspace(rows, 25)
    require(len(pivots) == 19 and len(basis) == 6, "covariance rank")
    all_maps = set()
    target_maps = set()
    checks = 0
    for coefficients in itertools.product(range(5), repeat=len(basis)):
        table = bytes(sum(c * vec[i] for c, vec in zip(coefficients, basis)) % 5
                      for i in range(25))
        all_maps.add(table)
        unit = True
        for i, (x, y) in enumerate(POINTS):
            value = table[i]
            require((value + table[index[-x % 5, -y % 5]]) % 5 == 0,
                    "odd inversion")
            require((value + table[index[y, x]]) % 5 == 0, "odd swap")
            require(table[index[-y % 5, -x % 5]] == value, "b covariance")
            c, h = (x + y) % 5, (y - x) % 5
            if c in (1, 4) and h in (2, 3):
                unit &= (2 * h * value) % 5 == 1
            checks += 1
        if unit:
            target_maps.add(table)
    require(len(all_maps) == 15625 and len(target_maps) == 3125,
            "class and target counts")
    linear = []
    for a, b in POINTS:
        table = bytes((a * x + b * y) % 5 for x, y in POINTS)
        if table in target_maps:
            linear.append([a, b])
    require(linear == [[3, 2]], "unique linear representative")
    for x, y in POINTS:
        if (x + y) % 5 in (1, 4) and (y - x) % 5 in (2, 3):
            require({table[index[x, y]] for table in target_maps}
                    == {2 * (y - x) % 5}, "complete output equivalence")
    return {
        "class_maps": len(all_maps),
        "class_point_checks": checks,
        "target_maps": len(target_maps),
        "class_sha256": hashlib.sha256(b"".join(sorted(all_maps))).hexdigest(),
        "target_sha256": hashlib.sha256(b"".join(sorted(target_maps))).hexdigest(),
        "linear_coefficients": linear[0],
    }


def generator(i, state):
    """The five native affine maps in (x,u,y,v,q,r) coordinates."""
    x, u, y, v, q, r = state
    if i == 0:
        output = (u + 2, x + 3, v + 3, y + 2, q, r)
    elif i == 1:
        output = (-y, -v, -x, -u, -q, -r)
    elif i == 2:
        output = (2 - y, 1 + r - v, 2 - x, 1 - u - r, 1 - q, -r)
    elif i == 3:
        output = (-x, -u, -y, -v, 1 - q, 1 - r)
    elif i == 4:
        output = (-x, -u, -y, -v, 2 - q, 1 - r)
    else:
        raise AssertionError("invalid generator")
    return tuple(value % 5 for value in output)


def contact(state, source):
    x, u, y, v, q, r = state
    shift = (2 * (y - x) * source) % 5
    return (x, (u - shift) % 5, y, (v + shift) % 5, q, r)


def trace(state):
    return sum(state) % 5


def selected(n, state):
    return (trace(state) + 2 * parity(n)) % 5


def quadratic(state):
    x, u, y, v, _, _ = state
    return 2 * (x * u + y * v) % 5


def reader(state):
    x, u, y, v, _, _ = state
    s = (x + u + y + v) % 5
    return ((1 - s * s) * (x + v + 3) + s * s * quadratic(state)) % 5


def full_carrier():
    pairs = inverse = commute = changes = 0
    for state in itertools.product(range(5), repeat=6):
        for s in range(5):
            out = contact(state, s)
            pairs += 1
            require(contact(out, -s) == state, "global contact inverse")
            inverse += 1
            require(trace(out) == trace(state), "trace invariant")
            require(sum(out[:4]) % 5 == sum(state[:4]) % 5, "S invariant")
            require(out[0] == state[0] and out[2] == state[2]
                    and out[4:] == state[4:], "control coordinates retained")
            for i in (1, 3, 4):
                require(generator(i, out) == contact(generator(i, state), s),
                        "full generator commutation")
                commute += 1
            require((quadratic(out) - quadratic(state)) % 5
                    == 4 * (state[2] - state[0]) ** 2 * s % 5,
                    "global M response")
            changes += 1
    witness = (0, 2, 0, 3, 1, 0)
    require(trace(witness) == 1, "off-support witness is on stable H1")
    require(quadratic(contact(witness, 1)) != (quadratic(witness) + 1) % 5,
            "off-support unit gain must fail")
    # These are raw zero and raw (2,1,2,1,1,0), converted to centered coordinates.
    left = (4, 2, 1, 3, 0, 0)
    right = (1, 3, 3, 4, 1, 0)
    require(left != right and generator(selected(0, left), left)
            == generator(selected(0, right), right), "native collision")
    return {
        "full_carrier_source_pairs": pairs,
        "full_contact_inverse_checks": inverse,
        "full_generator_commutation_checks": commute,
        "full_m_change_checks": changes,
        "off_support_unit_counterexample": True,
        "global_injectivity_counterexample": True,
    }


def prepared():
    counts = {
        "prepared_trajectories": 0,
        "prepared_state_boundaries": 0,
        "prepared_step_inverse_checks": 0,
        "first_record_boundaries": 0,
        "second_record_boundaries": 0,
        "initial_record_boundaries": 0,
        "prepared_source_boundaries": 0,
    }
    # Trace dynamics derived directly from the affine generator formula, starting
    # on z=0. Inverse chooses its generator from clock and this trace sequence,
    # without looking at a saved predecessor or solving for an old state.
    trace_schedule = [0]
    for n in range(max(TIMES) + HORIZON):
        z = trace_schedule[-1]
        representative = (0, 0, 0, 0, 0, z)
        trace_schedule.append(trace(generator((z + 2 * parity(n)) % 5,
                                               representative)))
    for trigger in TIMES:
        for first, initial, second in itertools.product(range(5), repeat=3):
            free = ((initial - 1) % 5, 2, (1 - initial) % 5, 3,
                    -first % 5, first)
            actual = free
            counts["prepared_trajectories"] += 1
            for n in range(trigger + HORIZON + 1):
                require(actual == (free if n <= trigger else contact(free, second)),
                        ("full boundary formula", trigger, first, initial, second, n))
                require(trace(actual) == trace_schedule[n], "clock trace")
                counts["prepared_state_boundaries"] += 1
                require((*actual[4:], second) == (*free[4:], second), "source boundary")
                counts["prepared_source_boundaries"] += 1
                if n == 0:
                    require(reader(actual) == initial, "initial record")
                    counts["initial_record_boundaries"] += 1
                elif 3 <= n <= trigger:
                    require(reader(actual) == (initial + first) % 5, "first record")
                    counts["first_record_boundaries"] += 1
                elif n > trigger:
                    require(reader(actual) == (initial + first + second) % 5,
                            "second record")
                    counts["second_record_boundaries"] += 1
                if n >= 3:
                    require(sum(actual[:4]) % 5 in (1, 4), "occupied receiver")
                    require((actual[0] + actual[2]) % 5 in (1, 4)
                            and (actual[2] - actual[0]) % 5 in (2, 3), "target orbit")
                if n == trigger + HORIZON:
                    break
                i = selected(n, actual)
                if n >= 3:
                    require(i in (1, 3, 4), "tail generator")
                touched = contact(actual, second) if n == trigger else actual
                successor = generator(selected(n, touched), touched)
                inverse_i = (trace_schedule[n] + 2 * parity(n)) % 5
                predecessor = generator(inverse_i, successor)
                if n == trigger:
                    predecessor = contact(predecessor, -second)
                require(predecessor == actual, "inverse on attained layer")
                counts["prepared_step_inverse_checks"] += 1
                actual = successor
                free = generator(selected(n, free), free)
    require(counts == {
        "prepared_trajectories": 875,
        "prepared_state_boundaries": 73750,
        "prepared_step_inverse_checks": 72875,
        "first_record_boundaries": 15125,
        "second_record_boundaries": 56000,
        "initial_record_boundaries": 875,
        "prepared_source_boundaries": 73750,
    }, "boundary inventory")
    counts.update(trigger_times=list(TIMES), tail_horizon=HORIZON)
    return counts


def main():
    report = classification()
    report.update(full_carrier())
    report.update(prepared())
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
