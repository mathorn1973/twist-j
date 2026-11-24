#!/usr/bin/env python3
"""Exact, result-exposed audit of the six-slot odd contact orbit.

No scientific calculation runs on import. The two traversals use separate
arithmetic representations and generate their sets without consulting one
another. A state-limit outcome is incomplete, never a nonreachability result.
"""

from collections import Counter, deque
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
import sys


CAP = 100000
ZERO4 = (0, 0, 0, 0)
ONE4 = (1, 0, 0, 0)
ZERO5 = (0, 0, 0, 0, 0)
EDGES = ((0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
         (1, 2), (1, 3), (1, 4), (1, 5), (2, 3),
         (2, 4), (2, 5), (3, 4), (3, 5), (4, 5))


def emit(kind, **fields):
    print(json.dumps(dict(kind=kind, **fields), sort_keys=True,
                     separators=(",", ":")), flush=True)


# Primary route: four power-basis coefficients, reduction by Phi_5.
def add4(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub4(x, y):
    return tuple(a - b for a, b in zip(x, y))


def scale4(n, x):
    return tuple(n * a for a in x)


def reduce4(coefficients):
    out = list(coefficients) + [0] * max(0, 4 - len(coefficients))
    for degree in range(len(out) - 1, 3, -1):
        value = out[degree]
        for shift in range(1, 5):
            out[degree - shift] -= value
        out[degree] = 0
    return tuple(out[:4])


def mul4(x, y):
    out = [0] * 7
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            out[i + j] += a * b
    return reduce4(out)


def rotate4(x):
    a, b, c, d = x
    return (-c + d, -c, a - c, b - c)


@lru_cache(maxsize=8192)
def q4(x):
    numerator = 5 * sum(a * a for a in x) - sum(x) ** 2
    assert numerator % 2 == 0
    return numerator // 2


@lru_cache(maxsize=8192)
def h4(x):
    conjugate = reduce4((x[0], 0, x[3], x[2], x[1]))
    return mul4(x, conjugate)


@lru_cache(maxsize=8192)
def contact4(x, y):
    difference = sub4(x, y)
    if any(a % 2 for a in difference):
        return x, y
    center_twice = add4(x, y)
    rotated = rotate4(difference)
    left_twice = add4(center_twice, rotated)
    right_twice = sub4(center_twice, rotated)
    assert all(a % 2 == 0 for a in left_twice + right_twice)
    return (tuple(a // 2 for a in left_twice),
            tuple(a // 2 for a in right_twice))


# Secondary route: Z^5 / Z(1,1,1,1,1), with minimum coefficient zero.
# It uses cyclic rotation and difference updates, not the primary matrix.
def canon5(x):
    floor = min(x)
    return tuple(a - floor for a in x)


def add5(x, y):
    return canon5(tuple(a + b for a, b in zip(x, y)))


def sub5(x, y):
    return canon5(tuple(a - b for a, b in zip(x, y)))


def scale5(n, x):
    return canon5(tuple(n * a for a in x))


def rotate5(x):
    return x[-2:] + x[:-2]


def mul5(x, y):
    out = [0] * 5
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            out[(i + j) % 5] += a * b
    return canon5(out)


@lru_cache(maxsize=8192)
def q5(x):
    numerator = sum((x[i] - x[j]) ** 2
                    for i in range(5) for j in range(i + 1, 5))
    assert numerator % 2 == 0
    return numerator // 2


@lru_cache(maxsize=8192)
def h5(x):
    return mul5(x, tuple(x[(-i) % 5] for i in range(5)))


@lru_cache(maxsize=8192)
def contact5(x, y):
    difference = tuple(a - b for a, b in zip(x, y))
    parity = difference[0] % 2
    if any(a % 2 != parity for a in difference):
        return x, y
    half = canon5(tuple((a - parity) // 2 for a in difference))
    delta = sub5(rotate5(half), half)
    return add5(x, delta), sub5(y, delta)


def to4(x):
    return tuple(x[i] - x[4] for i in range(4))


def to5(x):
    return canon5(x + (0,))


def replace_pair(state, edge, pair):
    i, j = edge
    return tuple(pair[0] if k == i else pair[1] if k == j else value
                 for k, value in enumerate(state))


def step4(state, edge):
    return replace_pair(state, edge, contact4(state[edge[0]], state[edge[1]]))


def step5(state, edge):
    return replace_pair(state, edge, contact5(state[edge[0]], state[edge[1]]))


def pair_audit(x, y, left_alphabet, right_alphabet):
    """Audit all powers, both routes, and every pair invariant exactly."""
    initial4 = (x, y)
    initial5 = (to5(x), to5(y))
    current4, current5 = initial4, initial5
    total_s = add4(x, y)
    total_h = add4(h4(x), h4(y))
    total_q = q4(x) + q4(y)
    residues = (sum(x) % 5, sum(y) % 5)
    inverse4 = None
    for power in range(1, 6):
        admitted4 = all(a % 2 == 0 for a in sub4(*current4))
        differences5 = tuple(a - b for a, b in zip(*current5))
        admitted5 = len({a % 2 for a in differences5}) == 1
        assert admitted4 == admitted5
        current4 = contact4(*current4)
        current5 = contact5(*current5)
        assert current4 == tuple(to4(a) for a in current5)
        assert current4[0] in left_alphabet and current4[1] in right_alphabet
        assert add4(*current4) == total_s
        assert add4(h4(current4[0]), h4(current4[1])) == total_h
        assert q4(current4[0]) + q4(current4[1]) == total_q
        assert tuple(sum(a) % 5 for a in current4) == residues
        assert to4(add5(*current5)) == total_s
        assert to4(add5(h5(current5[0]), h5(current5[1]))) == total_h
        assert sum(q5(a) for a in current5) == total_q
        assert tuple(sum(a) % 5 for a in current5) == residues
        if power == 4:
            inverse4 = current4
    assert current4 == initial4 and current5 == initial5
    assert contact4(*inverse4) == initial4
    forward = contact4(*initial4)
    for _ in range(4):
        forward = contact4(*forward)
    assert forward == initial4


def alphabet_audit():
    roots4 = tuple(tuple(int(i == k) for i in range(4)) for k in range(4))
    roots4 += ((-1, -1, -1, -1),)
    roots5 = tuple(tuple(int(i == k) for i in range(5)) for k in range(5))
    assert tuple(to4(a) for a in roots5) == roots4
    assert all(mul4(a, b) == roots4[(i + j) % 5]
               for i, a in enumerate(roots4) for j, b in enumerate(roots4))
    assert all(rotate4(a) == roots4[(i + 2) % 5]
               for i, a in enumerate(roots4))
    neutral = {sub4(a, b) for a in roots4 for b in roots4}
    charged = {add4(a, b) for a in roots4 for b in roots4}
    neutral5 = {sub5(a, b) for a in roots5 for b in roots5}
    charged5 = {add5(a, b) for a in roots5 for b in roots5}
    assert neutral == {to4(a) for a in neutral5}
    assert charged == {to4(a) for a in charged5}
    assert (len(neutral), len(charged)) == (21, 15)
    assert {q4(a) for a in neutral} == {0, 5}
    assert {q4(a) for a in charged} == {3, 8}
    assert {sum(a) % 5 for a in neutral} == {0}
    assert {sum(a) % 5 for a in charged} == {2}
    assert all(to4(to5(a)) == a for a in neutral | charged)
    pairs = set()
    counts = []
    for left, right in ((neutral, neutral), (neutral, charged),
                        (charged, neutral)):
        count = 0
        for x, y in product(sorted(left), sorted(right)):
            pair_audit(x, y, left, right)
            pairs.add((x, y))
            count += 1
        counts.append(count)
    assert counts == [441, 315, 315] and len(pairs) == 1071
    emit("ALPHABET", neutral=len(neutral), charged=len(charged),
         ordered_pairs=counts, powers_per_pair=5, status="PASS")
    return roots4, neutral, charged, pairs


def initial4(t):
    u = (1, -1, 0, 0)
    value = (t, 0, -t, 0)
    return (value, scale4(-1, value), u, u, ZERO4, (2, 0, 0, 0))


def initial5(t):
    root0 = (1, 0, 0, 0, 0)
    root1 = (0, 1, 0, 0, 0)
    root2 = (0, 0, 1, 0, 0)
    u = sub5(root0, root1)
    value = scale5(t, sub5(root0, root2))
    return (value, scale5(-1, value), u, u, ZERO5, scale5(2, root0))


def target4(t):
    u = (1, -1, 0, 0)
    value = (t, 0, -t, 0)
    return add4(u, value), sub4(u, value), ZERO4, ZERO4


class StateLimit(Exception):
    def __init__(self, route, states, transitions):
        self.route, self.states, self.transitions = route, states, transitions


def breadth_first(start):
    distance = {start: 0}
    predecessor = {}
    queue = deque([start])
    transitions = 0
    while queue:
        current = queue.popleft()
        for edge in EDGES:
            after = step4(current, edge)
            transitions += 1
            if after not in distance:
                if len(distance) >= CAP:
                    raise StateLimit("POWER4_BFS", len(distance), transitions)
                distance[after] = distance[current] + 1
                predecessor[after] = (current, edge)
                queue.append(after)
    assert transitions == 15 * len(distance)
    return distance, predecessor, transitions


def depth_first(start):
    seen = {start}
    stack = [start]
    transitions = 0
    while stack:
        current = stack.pop()
        for edge in EDGES:
            after = current
            for _ in range(4):
                after = step5(after, edge)
                transitions += 1
                if after not in seen:
                    if len(seen) >= CAP:
                        raise StateLimit("QUOTIENT5_DFS", len(seen), transitions)
                    seen.add(after)
                    stack.append(after)
    assert transitions == 60 * len(seen)
    return seen, transitions


def total4(state, function):
    result = ZERO4
    for value in state:
        result = add4(result, function(value))
    return result


def total5(state, function):
    result = ZERO5
    for value in state:
        result = add5(result, function(value))
    return result


def identity(value):
    return value


def encode_state(state):
    flat = tuple(a for value in state for a in value)
    assert len(flat) == 24 and all(-7 <= a <= 7 for a in flat)
    return bytes(a + 8 for a in flat)


def orbit_hash(states):
    encoded = sorted(encode_state(state) for state in states)
    digest = sha256(b"P-POLE-HEIGHT-ODD-ORBIT-1/power4-bias8-v1\n")
    digest.update(len(encoded).to_bytes(8, "big"))
    for state in encoded:
        digest.update(state)
    return digest.hexdigest()


def certify_orbit(start, distance, predecessor, secondary, neutral, charged, pairs):
    primary = set(distance)
    converted = {tuple(to4(a) for a in state) for state in secondary}
    assert len(converted) == len(secondary)
    assert primary == converted
    expected_s = total4(start, identity)
    expected_h = total4(start, h4)
    expected_q = sum(q4(a) for a in start)
    residues = tuple(sum(a) % 5 for a in start)
    assert len(predecessor) == len(distance) - 1
    assert distance[start] == 0 and start not in predecessor
    q_sets = [set() for _ in range(6)]
    reference_zero_joint = 0
    for state in sorted(primary):
        encode_state(state)
        assert all(value in neutral for value in state[:5])
        assert state[5] in charged
        assert total4(state, identity) == expected_s
        assert total4(state, h4) == expected_h
        assert sum(q4(a) for a in state) == expected_q
        assert tuple(sum(a) % 5 for a in state) == residues
        for i, value in enumerate(state):
            q_sets[i].add(q4(value))
        reference_zero_joint += int(state[2] == ZERO4 and state[3] == ZERO4)
        if state != start:
            before, edge = predecessor[state]
            assert before in primary and step4(before, edge) == state
            assert distance[before] + 1 == distance[state]
        for edge in EDGES:
            pair = (state[edge[0]], state[edge[1]])
            assert pair in pairs  # Every encountered pair has the full local audit.
            after = step4(state, edge)
            assert after in primary
            assert distance[after] <= distance[state] + 1
            assert distance[state] <= distance[after] + 4
            recovered = after
            for _ in range(4):
                recovered = step4(recovered, edge)
            assert recovered == state
    for state in secondary:
        assert all(len(a) == 5 and min(a) == 0 for a in state)
        assert to4(total5(state, identity)) == expected_s
        assert to4(total5(state, h5)) == expected_h
        assert sum(q5(a) for a in state) == expected_q
        assert tuple(sum(a) % 5 for a in state) == residues
    return [sorted(values) for values in q_sets], reference_zero_joint


def shortest_word(start, goal, predecessor):
    word = []
    current = goal
    while current != start:
        current, edge = predecessor[current]
        word.append(edge)
    word.reverse()
    return word


def replay_word(start, goal, word):
    current = start
    current5 = tuple(to5(a) for a in start)
    for edge in word:
        current = step4(current, edge)
        current5 = step5(current5, edge)
        assert current == tuple(to4(a) for a in current5)
    assert current == goal
    for edge in reversed(word):
        for _ in range(4):
            current = step4(current, edge)
            current5 = step5(current5, edge)
        assert current == tuple(to4(a) for a in current5)
    assert current == start


def audit_input(t, roots, neutral, charged, pairs):
    start = initial4(t)
    start5 = initial5(t)
    assert start == tuple(to4(a) for a in start5)
    assert sum(q4(a) for a in start) == 18 + 10 * t * t
    distance, predecessor, bfs_transitions = breadth_first(start)
    secondary, dfs_transitions = depth_first(start5)
    q_sets, reference_zero_joint = certify_orbit(
        start, distance, predecessor, secondary, neutral, charged, pairs)
    goals = sorted(state for state in distance if state[:4] == target4(t))
    target_q = [q4(a) for a in target4(t)]
    helper_phases = {
        (sub4(ONE4, roots[2 * k % 5]), add4(ONE4, roots[2 * k % 5])): k
        for k in range(5)
    }
    phase_distances = []
    words = []
    for goal in goals:
        assert goal[4:] in helper_phases
        phase = helper_phases[goal[4:]]
        phase_distances.append((phase, distance[goal]))
        word = shortest_word(start, goal, predecessor)
        assert len(word) == distance[goal]
        replay_word(start, goal, word)
        words.append((phase, ",".join(f"{i + 1}{j + 1}" for i, j in word)))
    phase_distances.sort()
    words.sort()
    histogram = Counter(distance.values())
    radius = max(histogram)
    expected_count, expected_radius = (110, 14) if t == 0 else (1480, 25)
    expected_phases = [(k, 10 + k) for k in range(5)] if t == 0 else []
    review_match = (len(distance) == expected_count and radius == expected_radius
                    and phase_distances == expected_phases)
    emit("ORBIT", t=t, states=len(distance), radius=radius,
         sha256=orbit_hash(distance), bfs_transitions=bfs_transitions,
         dfs_macro_transitions=dfs_transitions,
         closure_edges=15 * len(distance), route_sets_equal=True,
         distance_histogram=[histogram[d] for d in range(radius + 1)],
         slot_Q_sets=q_sets, references_3_4_zero_joint=reference_zero_joint,
         target_Q=target_q, goals=len(goals), phase_distances=phase_distances,
         exposed_review_count=expected_count, exposed_review_radius=expected_radius,
         exposed_review_match=review_match, status="COMPLETE")
    for phase, word in words:
        emit("SHORTEST_WORD", t=t, helper_phase=phase,
             forward_contacts=dict(phase_distances)[phase],
             word=word, inverse="REVERSED_C_POWERS_4", replay="PASS")
    if t:
        assert 15 in target_q and not goals
        assert reference_zero_joint == 0
        assert all(set(values) <= {0, 5} for values in q_sets[:5])
    return review_match


def main():
    if not __debug__:
        raise RuntimeError("Assertions must be enabled")
    emit("PROBE", name="P-POLE-HEIGHT-ODD-ORBIT-1", state_cap=CAP,
         inputs=[-1, 1, 0], observation="RESULT_EXPOSED", arithmetic="EXACT_INTEGER")
    roots, neutral, charged, pairs = alphabet_audit()
    comparisons = []
    for t in (-1, 1, 0):
        try:
            comparisons.append(audit_input(t, roots, neutral, charged, pairs))
        except StateLimit as limit:
            emit("LIMIT", t=t, route=limit.route, states=limit.states,
                 attempted_transitions=limit.transitions, cap=CAP,
                 conclusion="INCOMPLETE_NO_ORBIT_NONREACHABILITY_CLAIM")
            return 2
    emit("RESULT", audit="COMPLETE", local_closure="PASS", input_orbits=3,
         odd_target="UNREACHABLE_IN_DECLARED_CARRIER",
         exposed_review_comparison="MATCH" if all(comparisons) else "MISMATCH",
         canon_promotion=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
