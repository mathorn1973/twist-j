#!/usr/bin/env python3
"""Preregistration-only independent numerator/cascade breaker.

Do not execute before its public source pin.  Internal basis is
(1,rho,rho**2,rho**3).  The author verifier is neither read nor imported.
"""

import argparse
import hashlib
import json
import platform
import sys


ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
RHO = (0, 1, 0, 0)
J = (1, 1, 0, 0)
U = (1, -1, 0, 0)
J_INV = (0, -1, 0, -1)
D = 12
CORE = 16
EDGES = tuple((0, other) for other in range(1, CORE))
ARCHIVES = (ZERO, ONE, (0, 0, 0, 1), U, J)
OCCUPIED_N = (1, 3, 5, 7, 15, 27, 85, 1365, 4095)


def demand(condition, explanation):
    if not condition:
        raise AssertionError(explanation)


def add(a, b):
    return tuple(a[i] + b[i] for i in range(4))


def scale(k, a):
    return tuple(k * x for x in a)


def multiply(a, b):
    # Independent cyclic convolution in Z[rho]/(rho**5-1), then Phi_5.
    cyclic = [0] * 5
    for i in range(4):
        for k in range(4):
            cyclic[(i + k) % 5] += a[i] * b[k]
    return tuple(cyclic[i] - cyclic[4] for i in range(4))


def power(a, exponent):
    demand(exponent >= 0, "negative exponent in positive-power helper")
    result = ONE
    while exponent:
        if exponent & 1:
            result = multiply(result, a)
        a = multiply(a, a)
        exponent >>= 1
    return result


def rho_matrix(z):
    a, b, c, d = z
    return (-d, a - d, b - d, c - d)


def q(z):
    # Gram form in the rho basis, independent of the author's closed formula.
    return (2 * sum(a * a for a in z)
            - sum(z[i] * z[k] for i in range(4) for k in range(i + 1, 4)))


def j_coordinates(z):
    a, b, c, d = z
    return [a - c, d - c, b - c, -c]


def raw_contact(a, b):
    delta = tuple(a[i] - b[i] for i in range(4))
    if any(x % 2 for x in delta):
        return (a, b)
    twist = rho_matrix(delta)
    return (tuple((a[i] + b[i] + twist[i]) // 2 for i in range(4)),
            tuple((a[i] + b[i] - twist[i]) // 2 for i in range(4)))


def admitted(a, b):
    return all((a[i] - b[i]) % 2 == 0 for i in range(4))


def integer_pair(n, gain):
    numerator = gain * n + 1
    odd = numerator
    depth = 0
    while odd % 2 == 0:
        odd //= 2
        depth += 1
    return numerator, odd, depth


def load(n, gain, archives=()):
    first = scale(2 * (gain - 1) * n, U)
    second = scale(2 * n, add(scale(gain - 1, U), scale(2, ONE)))
    return [first, second, scale(2, J)] + [ZERO] * (CORE - 3) + list(archives)


def expected_after_two(n, gain):
    numerator = gain * n + 1
    return [scale(numerator, multiply(U, J)),
            scale(2 * n, (gain, -(gain - 2), 0, 0)),
            add(scale(gain * n, multiply(U, U)), multiply(J, J))]


def expected_current(n, gain):
    numerator, _, depth = integer_pair(n, gain)
    count = min(depth, D + 1)
    state = expected_after_two(n, gain) + [ZERO] * (CORE - 3)
    state[0] = scale(numerator // (1 << count),
                     multiply(U, power(J, count + 1)))
    for s in range(1, count + 1):
        state[2 + s] = scale(numerator // (1 << s),
                             multiply(multiply(U, U), power(J, s)))
        demand(state[2 + s] != ZERO, "formula produced a zero successful record")
    return state


def read_current(active, cascade):
    # This signature makes source/reference leftovers inaccessible to the reader.
    demand(len(cascade) == D + 1, "wrong cascade width")
    depth = 0
    for value in cascade:
        if value == ZERO:
            break
        depth += 1
    if depth == D + 1:
        return "DEPTH_LIMIT"
    demand(all(z == ZERO for z in cascade[depth:]), "nonzero record after first zero")
    normalized = multiply(power(J_INV, depth + 1), active)
    m = normalized[0]
    demand(normalized == scale(m, U), "normalized active outside the u-integer chart")
    demand(m > 0 and m % 2 == 1, "reader did not return a positive odd")
    return (m, depth)


class Lane:
    def __init__(self):
        self.cache = {}
        self.calls = 0

    def contact(self, state, left, right):
        key = (state[left], state[right])
        result = self.cache.get(key)
        if result is None:
            result = raw_contact(*key)
            demand(add(*key) == add(*result), "pair sum changed")
            demand(q(key[0]) + q(key[1]) == q(result[0]) + q(result[1]), "pair Q changed")
            demand(sum(key[0]) % 5 == sum(result[0]) % 5, "first labelled residue changed")
            demand(sum(key[1]) % 5 == sum(result[1]) % 5, "second labelled residue changed")
            delta = tuple(key[0][i] - key[1][i] for i in range(4))
            demand(rho_matrix(delta) == multiply(RHO, delta), "independent rho maps disagree")
            cycle = key
            for _ in range(5):
                cycle = raw_contact(*cycle)
            demand(cycle == key, "fifth-power contact identity failed")
            inverse = result
            for _ in range(4):
                inverse = raw_contact(*inverse)
            demand(inverse == key, "primitive inverse failed")
            self.cache[key] = result
        state[left], state[right] = result
        self.calls += 1

    def apply_word(self, state, n, gain):
        flags = []
        for position, (left, right) in enumerate(EDGES):
            flags.append(admitted(state[left], state[right]))
            self.contact(state, left, right)
            if position == 0:
                demand(state[0] == scale(2 * gain * n, U), "first synthesis active formula")
                demand(state[1] == expected_after_two(n, gain)[1], "first synthesis leftover formula")
            if position == 1:
                demand(state[:3] == expected_after_two(n, gain), "second synthesis formula")
        return flags

    def inverse_word(self, state):
        for left, right in reversed(EDGES):
            for _ in range(4):
                self.contact(state, left, right)


def audit_total(state, n, gain, archives):
    demand(len(state) == CORE + len(archives), "state width changed")
    expected_q = (40 * gain * (gain - 1) + 32) * n * n + 12 + sum(q(z) for z in archives)
    demand(sum(q(z) for z in state) == expected_q, "complete account changed")
    expected_sum = add(scale(4 * n, (gain, -(gain - 1), 0, 0)), scale(2, J))
    for archive in archives:
        expected_sum = add(expected_sum, archive)
    actual_sum = tuple(sum(z[i] for z in state) for i in range(4))
    demand(actual_sum == expected_sum, "complete sum changed")
    demand(state[CORE:] == list(archives), "occupied archive changed")


def one_case(lane, n, gain, archives=(), positive=True):
    initial = load(n, gain, archives)
    state = initial.copy()
    audit_total(state, n, gain, archives)
    flags = lane.apply_word(state, n, gain)
    expected = expected_current(n, gain) + list(archives)
    demand(state == expected, "complete current-state formula mismatch")
    audit_total(state, n, gain, archives)
    numerator, m, depth = integer_pair(n, gain)
    demand(flags[:2] == [True, True], "a synthesis contact was refused")
    taken = min(depth, D + 1)
    demand(flags[2:] == [True] * taken + [False] * (D + 1 - taken),
           "cascade admission/refusal prefix mismatch")
    result = read_current(state[0], state[3:CORE])
    if positive:
        demand(depth <= D, "positive corpus exceeded the frozen depth limit")
        demand(result == (m, depth), "reader arithmetic mismatch")
        inverse_numerator = (1 << depth) * m - 1
        demand(inverse_numerator % gain == 0, "arithmetic inverse not exactly divisible")
        demand(inverse_numerator // gain == n, "arithmetic inverse did not recover input")
    else:
        demand(gain == 3 and n == 5461 and numerator == 1 << 14,
               "outside-depth witness changed")
        demand(result == "DEPTH_LIMIT", "outside-depth witness was not flagged")
        demand(all(z != ZERO for z in state[3:CORE]), "saturation record unexpectedly blank")
        demand(all(x % 2 == 0 for x in state[0]), "saturated active was not even")
    current = state.copy()
    lane.inverse_word(state)
    demand(state == initial, "full native inverse failed")
    return current, result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--boundaries-out", help="optional complete q=3 fingerprint payload")
    args = parser.parse_args()
    demand(multiply(J, J_INV) == ONE, "declared J inverse failed")
    demand(len(EDGES) == D + 3 == 15, "fixed word length changed")
    edge_bytes = "".join(f"{i},{k}\n" for i, k in EDGES).encode("ascii")
    lane = Lane()
    boundaries = []
    histogram = {}
    for n in range(1, 4096, 2):
        current, (_, depth) = one_case(lane, n, 3)
        boundaries.append([n, [j_coordinates(z) for z in current]])
        histogram[depth] = histogram.get(depth, 0) + 1
    demand(len(boundaries) == 2048 and set(histogram) == set(range(1, D + 1)),
           "q=3 count or depth coverage mismatch")

    general = 0
    general_depth_zero = 0
    for gain in range(1, 10):
        for n in range(1, 128, 2):
            _, (_, depth) = one_case(lane, n, gain)
            general += 1
            general_depth_zero += int(depth == 0)
    demand(general == 576 and general_depth_zero == 256,
           "general supplied-gain coverage mismatch")

    occupied = 0
    for n in OCCUPIED_N:
        for left_archive in ARCHIVES:
            for right_archive in ARCHIVES:
                one_case(lane, n, 3, (left_archive, right_archive))
                occupied += 1
    demand(occupied == 225, "occupied archive count mismatch")
    _, saturation = one_case(lane, 5461, 3, positive=False)

    boundary_bytes = json.dumps(boundaries, separators=(",", ":")).encode("ascii")
    if args.boundaries_out:
        with open(args.boundaries_out, "wb") as handle:
            handle.write(boundary_bytes)
    result = {
        "status": "PASS",
        "scope": "NON-CANONICAL / L1 / candidate-C; independent single-architecture audit",
        "internal_basis": "1,rho,rho^2,rho^3",
        "boundary_basis": "1,j,j^2,j^3",
        "edge_count": len(EDGES),
        "edge_sha256": hashlib.sha256(edge_bytes).hexdigest(),
        "boundary_sha256": hashlib.sha256(boundary_bytes).hexdigest(),
        "boundary_bytes": len(boundary_bytes),
        "q3_cases": len(boundaries),
        "q3_depth_histogram": histogram,
        "general_gain_cases": general,
        "general_depth_zero_cases": general_depth_zero,
        "occupied_cases": occupied,
        "outside_depth_cases": 1,
        "outside_depth_reader": saturation,
        "native_inverse_cases": len(boundaries) + general + occupied + 1,
        "primitive_applications": lane.calls,
        "distinct_ordered_primitive_pairs": len(lane.cache),
        "core_slots": CORE,
        "occupied_test_slots": CORE + 2,
        "q3_account": "272*n^2+12",
        "reader_inputs": "active plus thirteen current cascade slots only",
        "normalization_scope": "reader computation, not a primitive contact operation",
        "python": sys.version.split()[0],
        "architecture": platform.machine(),
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
