#!/usr/bin/env python3
"""Exact preregistered native piston Gram classification, standard library only."""

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
import json


PROBE = "P-U-PISTON-GRAM-DESCENT-1"
ELL = (0, 1, 2, -2, -1)
CENTRE = (1, 3, 4, 2)


def generator(k, x):
    p, s, u, v, q, r = x
    if k == 0:
        y = (s, p, v, u, q, r)
    elif k == 1:
        y = (-u, -v, -p, -s, -q, -r)
    elif k == 2:
        y = (2 - u, 1 - v + r, 2 - p, 1 - s - r, 1 - q, -r)
    elif k == 3:
        y = (2 - p, 1 - s, 3 - u, 4 - v, 1 - q, 1 - r)
    elif k == 4:
        y = (2 - p, 1 - s, 3 - u, 4 - v, 2 - q, 1 - r)
    else:
        raise AssertionError("generator outside 0..4")
    return tuple(value % 5 for value in y)


def state_index(x):
    answer = 0
    for digit in x:
        answer = 5 * answer + digit
    return answer


def invariants(v):
    a, b, c, d = v
    return a * a + b * b, a * c + b * d, c * c + d * d, a * d - b * c


def canonical_labels(keys):
    first = {}
    return [first.setdefault(key, i) for i, key in enumerate(keys)]


def blocks(labels):
    result = defaultdict(list)
    for i, label in enumerate(labels):
        result[label].append(i)
    return dict(result)


def histogram(values):
    return [[value, count] for value, count in sorted(Counter(values).items())]


def digest_ascii(value):
    return sha256(value.encode("ascii")).hexdigest()


def classify(readings, successors, states):
    initial = canonical_labels(readings)
    original_blocks = blocks(initial)
    first_splits = [
        sum(len({initial[successors[t][i]] for i in fibre}) > 1
            for fibre in original_blocks.values())
        for t in (0, 1)
    ]
    current = initial
    counts = [len(original_blocks)]
    while True:
        refined = canonical_labels(
            (current[i], current[successors[0][i]], current[successors[1][i]])
            for i in range(len(states))
        )
        if refined == current:
            break
        next_count = len(set(refined))
        assert counts[-1] < next_count <= len(states)
        counts.append(next_count)
        current = refined
    final_blocks = blocks(current)
    assert all(representative == min(fibre)
               for representative, fibre in final_blocks.items())

    final_in_initial = {
        initial_rep: sorted({current[i] for i in fibre})
        for initial_rep, fibre in original_blocks.items()
    }
    multiplicities = {rep: len(parts) for rep, parts in final_in_initial.items()}
    capacity = max(multiplicities.values())
    tags = {}
    for parts in final_in_initial.values():
        for tag, final_rep in enumerate(parts):
            tags[final_rep] = tag
    tagged = [(reading, tags[current[i]]) for i, reading in enumerate(readings)]
    assert canonical_labels(tagged) == current
    assert max(tags.values()) + 1 == capacity

    transition_checks = 0
    for t in (0, 1):
        quotient = {}
        for i, reading in enumerate(tagged):
            target = tagged[successors[t][i]]
            assert quotient.setdefault(reading, target) == target
            transition_checks += 1
        assert len(quotient) == len(final_blocks)

    partition_text = ",".join(map(str, current)) + "\n"
    transition_text = "".join(
        f"{rep},{current[successors[0][rep]]},{current[successors[1][rep]]}\n"
        for rep in sorted(final_blocks)
    )
    maximal_rep = min(rep for rep, size in multiplicities.items() if size == capacity)
    descends = not any(first_splits)
    return {
        "initial_classes": len(original_blocks),
        "initial_size_histogram": histogram(map(len, original_blocks.values())),
        "refinement_class_counts": counts,
        "stable_classes": len(final_blocks),
        "stable_size_histogram": histogram(map(len, final_blocks.values())),
        "first_split_controls": first_splits,
        "required_extra_labels": capacity,
        "ambiguity_histogram": histogram(multiplicities.values()),
        "tagged_transition_checks": transition_checks,
        "partition_sha256": digest_ascii(partition_text),
        "transition_sha256": digest_ascii(transition_text),
        "maximal_fibre_witness": {
            "reading": readings[maximal_rep],
            "representatives": [states[rep] for rep in final_in_initial[maximal_rep]],
        },
        "descent": "YES" if descends else "NO",
        "positive_hypothesis": "SURVIVES" if descends else "FIRED",
    }


def centered_data(x):
    residual = tuple((p - c) % 5 for p, c in zip(x[:4], CENTRE))
    lifted = tuple(ELL[value] for value in residual)
    a, b, c, d = invariants(lifted)
    assert a * c - b * b == d * d
    q = (a + c, a - c, 2 * b, 2 * d)
    return residual, lifted, q


def flat(z, q):
    assert z in (1, 4)
    chi = 1 if z == 1 else -1
    return q[0], chi * q[1], q[2], chi * q[3]


def stable_comparison(states, successors):
    for k in (1, 3, 4):
        assert generator(k, CENTRE + (0, 0))[:4] == CENTRE
    stable = [i for i, x in enumerate(states) if sum(x) % 5 in (1, 4)]
    data = {i: centered_data(states[i]) for i in stable}
    image = set()
    zero_count = 0
    cone_checks = 0
    step_checks = 0
    flat_checks = 0
    table = set()
    quotient = [{}, {}]
    for i in stable:
        x = states[i]
        z = sum(x) % 5
        residual, lifted, q = data[i]
        assert q[0] >= 0
        assert q[0] * q[0] == sum(value * value for value in q[1:])
        assert (q[0] == 0) == (lifted == (0, 0, 0, 0))
        cone_checks += 1
        zero_count += q == (0, 0, 0, 0)
        image.add((z,) + q)

        # Check the disclosed relation to the pre-existing invariant V.
        chi = 1 if z == 1 else -1
        p, s, u, v, _, _ = x
        invariant_v = ((p + u) % 5, (s + v) % 5,
                       (chi * (p - u - 2)) % 5, (chi * (s - v - 1)) % 5)
        v0, v1, v2, v3 = invariant_v
        reconstructed = tuple((3 * a) % 5
                              for a in (v0 + v2, v1 + v3, v0 - v2, v1 - v3))
        framed_residual = residual if z == 1 else residual[2:] + residual[:2]
        assert reconstructed == framed_residual

        for t in (0, 1):
            j = successors[t][i]
            y = states[j]
            next_z = sum(y) % 5
            assert next_z in (1, 4)
            _, next_lifted, next_q = data[j]
            g = (z + 2 * t) % 5
            assert g in (1, 3, 4)
            if g == 1:
                expected_lifted = tuple(-value for value in lifted[2:] + lifted[:2])
                expected_q = (q[0], -q[1], q[2], -q[3])
                sign = -1
            else:
                expected_lifted = tuple(-value for value in lifted)
                expected_q = q
                sign = 1
            assert next_lifted == expected_lifted
            assert next_q == expected_q
            assert flat(next_z, next_q) == flat(z, q)
            key, target = (z,) + q, (next_z,) + next_q
            assert quotient[t].setdefault(key, target) == target
            table.add((t, z, g, next_z, sign))
            step_checks += 1
            flat_checks += 1

    expected_table = [(0, 1, 1, 4, -1), (0, 4, 4, 4, 1),
                      (1, 1, 3, 1, 1), (1, 4, 1, 1, -1)]
    assert sorted(table) == expected_table
    assert all(len(qmap) == len(image) for qmap in quotient)
    origin_checks = 0
    for i in range(len(states)):
        j = i
        for n in range(3):
            j = successors[n.bit_count() % 2][j]
        assert sum(states[j]) % 5 == 1
        origin_checks += 1
    assert len(stable) == cone_checks == 6250
    assert step_checks == flat_checks == 12500
    assert origin_checks == 15625
    return {
        "count": len(stable),
        "step_checks": step_checks,
        "centre": CENTRE,
        "origin_heads_verified": origin_checks,
        "origin_final_trace": 1,
        "cone_identity_checks": cone_checks,
        "flat_invariant_checks": flat_checks,
        "cone_images": len(image),
        "cone_zero_states": zero_count,
        "action_table": expected_table,
    }


def main():
    states = list(product(range(5), repeat=6))
    assert len(states) == 15625
    assert all(state_index(x) == i for i, x in enumerate(states))
    involutions = 0
    for k in range(5):
        for x in states:
            assert generator(k, generator(k, x)) == x
            involutions += 1
    assert involutions == 78125
    successors = [
        [state_index(generator((sum(x) + 2 * t) % 5, x)) for x in states]
        for t in (0, 1)
    ]

    piston_invariants = {}
    for p in product(range(5), repeat=4):
        a, b, c, d = invariants(tuple(ELL[value] for value in p))
        assert a * c - b * b == d * d
        piston_invariants[p] = (a, b, c, d)
    assert len(piston_invariants) == 625
    raw = [x[4:] + piston_invariants[x[:4]][:3] for x in states]
    oriented = [x[4:] + piston_invariants[x[:4]] for x in states]

    x = (1, 0, 0, 4, 0, 4)
    y = (4, 0, 0, 1, 0, 4)
    i, j = state_index(x), state_index(y)
    assert raw[i] == raw[j] == (0, 4, 1, 0, 1)
    assert oriented[i] == oriented[j] == (0, 4, 1, 0, 1, -1)
    assert sum(x) % 5 == sum(y) % 5 == 4
    tx, ty = states[successors[0][i]], states[successors[0][j]]
    assert tx == (1, 1, 3, 0, 2, 2)
    assert ty == (3, 1, 3, 3, 2, 2)
    ix, iy = piston_invariants[tx[:4]], piston_invariants[ty[:4]]
    assert ix == (2, -2, 4, 2)
    assert iy == (5, 2, 8, 6)
    witness = {
        "left": x, "right": y,
        "initial_H": (1, 0, 1), "initial_D": -1,
        "next_left": tx, "next_right": ty,
        "next_left_H": ix[:3], "next_right_H": iy[:3],
        "next_left_D": ix[3], "next_right_D": iy[3],
    }

    readers = {"GRAM": classify(raw, successors, states),
               "ORIENTED": classify(oriented, successors, states)}
    assert all(reader["descent"] == "NO" for reader in readers.values())
    assert all(reader["tagged_transition_checks"] == 31250 for reader in readers.values())
    result = {
        "probe": PROBE,
        "state_count": len(states),
        "controls": [0, 1],
        "piston_identity_count": len(piston_invariants),
        "generator_involution_checks": involutions,
        "status": "COMPLETE",
        "witness": witness,
        "readers": readers,
        "stable_sheet": stable_comparison(states, successors),
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
