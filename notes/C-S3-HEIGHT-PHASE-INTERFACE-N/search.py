#!/usr/bin/env python3
"""Prospectively fixed, bounded S3 search. NON-CANONICAL / L1.

No stochastic choices or adaptive limits. A capped search is INCONCLUSIVE.
Coordinates are exact integers in the basis (1,j,j^2,j^3).
"""
from collections import Counter
import hashlib
import json
import sys

HEIGHTS = (-2, -1, 0, 1, 2)
DEPTH_CAP = 6
STATE_CAP = 20000
PAIRS = tuple((a, b) for a in range(8) for b in range(a + 1, 8))
ZERO = (0, 0, 0, 0)
U = (1, -1, 0, 0)
B = (1, 0, -1, 0)
J = (1, 0, 1, 0)
X = (1, 1, 0, -2)
TWO = (2, 0, 0, 0)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def scale(n, a):
    return tuple(n * x for x in a)


def rho(a):
    a0, a1, a2, a3 = a
    return (a3 - a2, -a2, a0 - a2, a1 - a2)


def mul(a, b):
    c = [0] * 7
    for i, x in enumerate(a):
        for k, y in enumerate(b):
            c[i + k] += x * y
    for k in range(6, 3, -1):
        v = c[k]
        for d in range(1, 5):
            c[k - d] -= v
        c[k] = 0
    return tuple(c[:4])


def conjugate(a):
    a0, a1, a2, a3 = a
    return (a0 - a1, -a1, a3 - a1, a2 - a1)


def q(a):
    n = 5 * sum(x * x for x in a) - sum(a) ** 2
    assert n % 2 == 0
    return n // 2


def hermitian(a):
    h = mul(a, conjugate(a))
    assert h[1] == 0 and h[2] == h[3]
    return (h[0], -h[2])


def invariants(state):
    total = ZERO
    ha = hb = account = 0
    for a in state:
        total = add(total, a)
        ah, bh = hermitian(a)
        ha += ah
        hb += bh
        account += q(a)
    assert account == 2 * ha + hb
    return (total, (ha, hb), account,
            tuple(sum(a) % 5 for a in state))


def contact(a, b):
    difference = tuple(x - y for x, y in zip(a, b))
    if any(x % 2 for x in difference):
        return a, b, False
    middle = tuple((x + y) // 2 for x, y in zip(a, b))
    d = rho(tuple(x // 2 for x in difference))
    return add(middle, d), add(middle, neg(d)), True


def initial(t):
    return (add(U, scale(t, B)), add(U, scale(-t, B)),
            ZERO, ZERO, X, TWO, J, neg(J))


def target(t):
    value = J
    for _ in range((t + 2) % 5):
        value = rho(value)
    return (value, neg(value))


TARGETS = tuple(target(t) for t in HEIGHTS)


def goal(node):
    return all(node[8 * k + 6:8 * k + 8] == TARGETS[k]
               for k in range(5))


def transition(node, pair):
    result = list(node)
    accepted = refused = 0
    for k in range(5):
        a, b = (8 * k + pair[0], 8 * k + pair[1])
        result[a], result[b], admit = contact(node[a], node[b])
        accepted += int(admit)
        refused += int(not admit)
    return tuple(result), accepted, refused


def audit_word(word):
    """Replay from scratch, check every primitive, then literal inverse."""
    checked_cuts = 0
    traces = []
    final_states = []
    for t in HEIGHTS:
        original = initial(t)
        state = list(original)
        reference = invariants(state)
        trace = []
        for a, b in word:
            state[a], state[b], admitted = contact(state[a], state[b])
            trace.append(int(admitted))
            assert invariants(state) == reference
            checked_cuts += 1
        assert tuple(state[6:8]) == target(t)
        final_states.append(state[:])
        traces.append(trace)
        for a, b in reversed(word):
            for _ in range(4):
                state[a], state[b], _ = contact(state[a], state[b])
                assert invariants(state) == reference
                checked_cuts += 1
        assert tuple(state) == original
    assert len({tuple(trace) for trace in traces}) >= 3
    assert all(traces[i] != traces[i + 1] for i in range(4))
    return {"checked_cuts": checked_cuts, "admission_traces": traces,
            "complete_final_states": final_states}


def run():
    root = tuple(a for t in HEIGHTS for a in initial(t))
    for t in HEIGHTS:
        inv = invariants(initial(t))
        assert inv[0] == (5, -1, 0, -2)
        assert inv[1] == (19 + 4 * t * t, 1 + 2 * t * t)
        assert inv[2] == 39 + 10 * t * t
        assert inv[3] == (0, 0, 0, 0, 0, 2, 2, 3)
    assert not goal(root)
    nodes = [root]
    parents = [None]
    depths = [0]
    seen = {root: 0}
    cursor = 0
    stats = Counter()
    solution = None
    reason = None
    stop_pair = None
    while cursor < len(nodes):
        if depths[cursor] >= DEPTH_CAP:
            reason = "DEPTH_CAP"
            break
        node = nodes[cursor]
        for pair_index, pair in enumerate(PAIRS):
            child, accepted, refused = transition(node, pair)
            stats["generated"] += 1
            stats["scalar_accepted"] += accepted
            stats["scalar_refused"] += refused
            if child == node:
                stats["unchanged"] += 1
                continue
            if child in seen:
                stats["duplicate"] += 1
                continue
            if len(nodes) == STATE_CAP:
                reason = "STATE_CAP"
                stop_pair = pair_index
                break
            index = len(nodes)
            nodes.append(child)
            parents.append((cursor, pair))
            depths.append(depths[cursor] + 1)
            seen[child] = index
            if goal(child):
                solution = index
                reason = "GOAL"
                stop_pair = pair_index
                break
        if reason is not None:
            break
        cursor += 1
    if reason is None:
        reason = "ORBIT_EXHAUSTED"
    result = {
        "status": "FOUND" if solution is not None else (
            "NO_GOAL_IN_COMPLETE_ORBIT" if reason == "ORBIT_EXHAUSTED"
            else "INCONCLUSIVE"),
        "reason": reason, "depth_cap": DEPTH_CAP, "state_cap": STATE_CAP,
        "visited": len(nodes), "max_visited_depth": max(depths),
        "fully_expanded_nodes": cursor,
        "remaining_nodes_including_partial": len(nodes) - cursor,
        "stop_parent_index": cursor if cursor < len(nodes) else None,
        "stop_pair_index": stop_pair,
        "generated": stats["generated"],
        "scalar_accepted": stats["scalar_accepted"],
        "scalar_refused": stats["scalar_refused"],
        "unchanged": stats["unchanged"], "duplicate": stats["duplicate"],
    }
    if solution is not None:
        word = []
        index = solution
        while parents[index] is not None:
            index, pair = parents[index]
            word.append(pair)
        word.reverse()
        result["word_one_based"] = [[a + 1, b + 1] for a, b in word]
        result["audit"] = audit_word(word)
    else:
        result["word_one_based"] = None
    # Bind the explored tuple states without emitting a development trace.
    digest = hashlib.sha256()
    for node in nodes:
        digest.update(json.dumps(node, separators=(",", ":")).encode("ascii"))
        digest.update(b"\n")
    result["visited_states_sha256"] = digest.hexdigest()
    return result


if __name__ == "__main__":
    output = json.dumps(run(), sort_keys=True, separators=(",", ":")) + "\n"
    sys.stdout.buffer.write(output.encode("ascii"))
