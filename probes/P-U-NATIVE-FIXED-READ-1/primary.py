#!/usr/bin/env python3
"""Exact direct-coordinate audit. No predecessor verifier is imported."""
from itertools import combinations, product
import json
import sys

F5 = range(5)


def norm(values):
    return tuple(value % 5 for value in values)


def generator(index, state):
    p1, p4, p1p, p4p, q, r = state
    if index == 0:
        out = p4, p1, p4p, p1p, q, r
    elif index == 1:
        out = -p1p, -p4p, -p1, -p4, -q, -r
    elif index == 2:
        out = 2-p1p, 1-p4p+r, 2-p1, 1-p4-r, 1-q, -r
    elif index == 3:
        out = 2-p1, 1-p4, 3-p1p, 4-p4p, 1-q, 1-r
    elif index == 4:
        out = 2-p1, 1-p4, 3-p1p, 4-p4p, 2-q, 1-r
    else:
        raise ValueError(index)
    return norm(out)


def native(n, state):
    theta = n.bit_count() % 2
    index = (sum(state) + 2*theta) % 5
    return generator(index, state), index


def first_three(state):
    word = []
    for n in range(3):
        state, index = native(n, state)
        word.append(index)
    return state, tuple(word)


def endpoint(state):
    a, b, c, d, q, r = state
    return norm((d, c-r, b+1, a+r+3, q+1, r+1))


def read_m(p):
    a, b, c, d = p[:4]
    return 2*((a-1)*(b-3)+(c-4)*(d-2)) % 5


def read_k(state):
    return ((state[0]-1)**2+(state[2]-4)**2) % 5


def read_context(state):
    s = sum(state[:4]) % 5
    return ((1-s*s)*2*state[3]+s*s*2*(read_k(state)-1)) % 5


def read_x(state):
    return (2*(state[5]-state[4])+1) % 5


def read_sum_source(state):
    return 3*(state[5]-state[4]) % 5


def read_sum_receiver(state):
    s = sum(state[:4]) % 5
    local = (state[0]+state[3]) % 5
    return ((1-s*s)*local+s*s*read_m(state)) % 5


def affine_point(p0, direction, y):
    return norm(a+y*b for a, b in zip(p0, direction))


def source_fibre(u):
    return norm((u+4, 4*u+1))


def line_record(p0, direction, a, b, c):
    return [list(p0), list(direction), a, b, c]


def audit_native():
    words = ((0, 2, 4), (1, 1, 3), (2, 2, 4),
             (3, 1, 3), (4, 1, 3))
    total = h0 = 0
    for state in product(F5, repeat=6):
        out, word = first_three(state)
        z = sum(state) % 5
        assert word == words[z], (state, word, words[z])
        assert sum(out) % 5 == 1, (state, out)
        total += 1
        if z == 0:
            assert out == endpoint(state), (state, out, endpoint(state))
            h0 += 1
    stable_checks = 0
    for p in product(F5, repeat=4):
        for index in (1, 3, 4):
            out = generator(index, p+(0, 0))
            assert read_m(out) == read_m(p), (p, index, out)
            assert read_k(out) == read_k(p), (p, index, out)
            stable_checks += 1
    # Selector closure is separate from the invariant's generator check.
    for z in (1, 4):
        for theta in (0, 1):
            state = (0, 0, 0, 0, 0, z)
            index = (z+2*theta) % 5
            assert index in (1, 3, 4)
            out = generator(index, state)
            assert sum(out) % 5 == (4-3*theta) % 5
    assert total == 15625 and h0 == 3125 and stable_checks == 1875
    return total, h0, stable_checks


def derived_templates():
    rows = []
    for b, d in product(F5, repeat=2):
        b0 = (b-d-1) % 5
        if b0 == 0:
            continue
        p10 = ((b-3)+(b+d+4)*(d-2))*pow(b0, -1, 5) % 5
        slope = pow(2*b0 % 5, -1, 5)
        p0 = norm((p10, b, -p10-b-d, d))
        direction = norm((slope, 0, -slope, 0))
        h = (d-b) % 5
        a = (h+2)*pow((h+1) % 5, -1, 5) % 5
        gain = 2*(h+2) % 5
        offset = (3*p10+2*b+3*h-1) % 5
        rows.append(line_record(p0, direction, a, gain, offset))
    return sorted(rows)


def audit_preparations():
    points = [p for p in product(F5, repeat=4) if sum(p) % 5 == 0]
    candidates = 0
    rows = []
    for p0, direction in product(points, repeat=2):
        candidates += 1
        line = [affine_point(p0, direction, y) for y in F5]
        if any(read_m(line[y]) != y for y in F5):
            continue
        values = {}
        for u, y in product(F5, repeat=2):
            state = line[y]+source_fibre(u)
            assert sum(state) % 5 == 0
            assert read_x(state) == u
            out, word = first_three(state)
            assert word == (0, 2, 4)
            assert read_x(out) == u
            values[u, y] = read_m(out)
        c = values[0, 0]
        a = (values[0, 1]-c) % 5
        b = (values[1, 0]-c) % 5
        if all(values[u, y] == (a*y+b*u+c) % 5
               for u, y in product(F5, repeat=2)):
            rows.append(line_record(p0, direction, a, b, c))
    rows.sort()
    assert candidates == 15625
    assert rows == derived_templates(), (rows, derived_templates())
    assert len(rows) == 20
    unital = [row for row in rows if (row[2]+row[3]) % 5 == 1 and row[4] == 0]
    explicit = sorted([
        [[3, 3, 4, 0], [4, 0, 1, 0], 3, 3, 0],
        [[2, 2, 2, 4], [4, 0, 1, 0], 3, 3, 0],
        [[0, 3, 4, 3], [2, 0, 3, 0], 2, 4, 0],
        [[3, 1, 0, 1], [2, 0, 3, 0], 2, 4, 0],
    ])
    assert unital == explicit, unital
    checked = 0
    for p0, direction, a, b, c in unital:
        for u, y in product(F5, repeat=2):
            state = affine_point(p0, direction, y)+source_fibre(u)
            out, word = first_three(state)
            assert read_m(state) == y and read_x(state) == u
            assert out == endpoint(state) and word == (0, 2, 4)
            assert read_m(out) == (a*y+b*u) % 5 and read_x(out) == u
            assert sum(state[:4]) % 5 == 0
            assert sum(out[:4]) % 5 == 4
            # The actual next tick preserves the receiver, but not X in general.
            following, index = native(3, out)
            assert index == 1
            assert read_m(following) == read_m(out)
            assert read_x(following) == (2-u) % 5
            if p0 == [3, 3, 4, 0]:
                assert out == norm((0, u+y+3, 4, 4*u+4*y+2, u, 4*u+2))
            if p0 == [0, 3, 4, 3]:
                assert out == norm((3, 3*y+u+3, 4, 2*y+4*u+4, u, 4*u+2))
            checked += 1
    assert checked == 100
    return candidates, rows, unital, checked


def audit_sum():
    checked = 0
    for s, t in product(F5, repeat=2):
        state = norm((t, 0, -t, 0, -s, s))
        out, word = first_three(state)
        assert word == (0, 2, 4)
        assert out == norm((0, -t-s, 1, t+s+3, 1-s, 1+s))
        assert read_sum_source(state) == s == read_sum_source(out)
        assert read_sum_receiver(state) == t
        assert read_sum_receiver(out) == (t+s) % 5
        # S=+/-1 and invariant M prove every later time, not this one tick alone.
        following, index = native(3, out)
        assert index == 1
        assert sum(following[:4]) % 5 == 1
        assert read_sum_receiver(following) == (t+s) % 5
        checked += 1
    assert checked == 25
    return checked


def audit_context():
    records = []
    checked = 0
    collision_outputs = []
    first_tick_witness = None
    for label in (0, 1):
        for u, y in product(F5, repeat=2):
            if label == 0:
                state = norm((4*y+3, 3, y+4, 0, u+4, 4*u+1))
            else:
                state = norm((2*y, 3, 3*y+4, 3, u+4, 4*u+1))
            assert read_context(state) == label
            assert (read_x(state), read_m(state)) == (u, y)
            initial = state
            values = [read_context(state)]
            for n in range(3):
                state, index = native(n, state)
                assert index == (0, 2, 4)[n]
                values.append(read_context(state))
            assert values[1] == ((2-label)*y+3) % 5
            assert values[2:] == [label, label]
            assert read_m(state) == ((3-label)*y+(3+label)*u) % 5
            assert read_x(state) == u
            assert read_context(state) == label
            following, index = native(3, state)
            assert index == 1 and read_context(following) == label
            if u == 1 and y == 0:
                collision_outputs.append(read_m(state))
                if label == 0:
                    assert initial == (3, 3, 4, 0, 0, 0)
                    assert state == (0, 4, 4, 1, 1, 1)
                    first_tick_witness = values
                else:
                    assert initial == (0, 3, 4, 3, 0, 0)
                    assert state == (3, 4, 4, 3, 1, 1)
            checked += 1
    assert checked == 50
    assert collision_outputs == [3, 4]
    assert first_tick_witness == [0, 3, 0, 0]
    return checked, {"input": [1, 0], "outputs": collision_outputs}, first_tick_witness


def audit_dependency():
    permutations = ((0, 1, 2, 3), (1, 0, 3, 2),
                    (2, 3, 0, 1), (3, 2, 1, 0))
    all_coordinates = set(range(6))
    checked = survivors = 0
    for source in combinations(range(6), 2):
        remainder = sorted(all_coordinates-set(source))
        for receiver in combinations(remainder, 2):
            reference = tuple(sorted(set(remainder)-set(receiver)))
            blocks = [set(source), set(receiver), set(reference)]
            for permutation in permutations:
                # Maximal dependency: every piston is allowed to receive r.
                predecessors = [{permutation[j], 5} for j in range(4)]
                predecessors += [{4}, {5}]
                dependencies = []
                for block in blocks:
                    raw_inputs = set().union(*(predecessors[j] for j in block))
                    dependencies.append({
                        label for label, other in enumerate(blocks) if raw_inputs & other
                    })
                possible = (0 in dependencies[0] and 2 in dependencies[2]
                            and dependencies[1] == {0, 1, 2})
                survivors += int(possible)
                assert not possible, (source, receiver, reference, permutation)
                checked += 1
    assert checked == 360 and survivors == 0
    return checked, survivors


def main():
    if not __debug__:
        raise RuntimeError("Assertions must be enabled")
    total, h0, stable = audit_native()
    candidates, rows, unital, checked = audit_preparations()
    sums = audit_sum()
    contexts, collision, internal = audit_context()
    cases, survivors = audit_dependency()
    report = {
        "status": "PASS", "method": "direct-coordinate",
        "origin_states": total, "h0_word_states": h0,
        "stable_reader_generator_checks": stable,
        "affine_candidates": candidates, "affine_preparations": len(rows),
        "unital_preparations": len(unital), "unital_inputs": checked,
        "sum_inputs": sums, "context_inputs": contexts,
        "context_collision": collision, "first_tick_context_witness": internal,
        "dependency_cases": cases,
        "dependency_survivors": survivors, "templates": rows, "unital_codes": unital,
    }
    sys.stdout.buffer.write((json.dumps(report, sort_keys=True, separators=(",", ":"))
                             + "\n").encode("ascii"))


if __name__ == "__main__":
    main()
