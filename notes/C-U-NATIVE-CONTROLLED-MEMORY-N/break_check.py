#!/usr/bin/env python3
"""Exact second implementation for PROOF.md; no scientific execution at authoring.

NON-CANONICAL. Same authoring-session cross-check, not independent review.
Uses independently transcribed homogeneous generator matrices, raw-state scans,
and the actual native selector. Imports neither verify.py nor its helpers.
"""

from collections import Counter, defaultdict
from itertools import product
import json


# Rows act on (a,b,c,d,q,r,1). The seventh row is homogeneous identity.
ROWS = (
    ((0, 1, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0, 0),
     (0, 0, 0, 1, 0, 0, 0), (0, 0, 1, 0, 0, 0, 0),
     (0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 1, 0)),
    ((0, 0, -1, 0, 0, 0, 0), (0, 0, 0, -1, 0, 0, 0),
     (-1, 0, 0, 0, 0, 0, 0), (0, -1, 0, 0, 0, 0, 0),
     (0, 0, 0, 0, -1, 0, 0), (0, 0, 0, 0, 0, -1, 0)),
    ((0, 0, -1, 0, 0, 0, 2), (0, 0, 0, -1, 0, 1, 1),
     (-1, 0, 0, 0, 0, 0, 2), (0, -1, 0, 0, 0, -1, 1),
     (0, 0, 0, 0, -1, 0, 1), (0, 0, 0, 0, 0, -1, 0)),
    ((-1, 0, 0, 0, 0, 0, 2), (0, -1, 0, 0, 0, 0, 1),
     (0, 0, -1, 0, 0, 0, 3), (0, 0, 0, -1, 0, 0, 4),
     (0, 0, 0, 0, -1, 0, 1), (0, 0, 0, 0, 0, -1, 1)),
    ((-1, 0, 0, 0, 0, 0, 2), (0, -1, 0, 0, 0, 0, 1),
     (0, 0, -1, 0, 0, 0, 3), (0, 0, 0, -1, 0, 0, 4),
     (0, 0, 0, 0, -1, 0, 2), (0, 0, 0, 0, 0, -1, 1)),
)
MATRICES = tuple(rows + ((0, 0, 0, 0, 0, 0, 1),) for rows in ROWS)
SWAP = (2, 3, 0, 1, 4, 5)


def check(ok, tag, *detail):
    if not ok:
        raise AssertionError((tag,) + detail)


def residues(values):
    return tuple(value % 5 for value in values)


def image(matrix, point):
    vector = point + (1,)
    out = residues(sum(a * b for a, b in zip(row, vector)) for row in matrix)
    check(out[-1] == 1, "homogeneous_coordinate", point, out)
    return out[:-1]


def step_bit(point, bit):
    index = (sum(point) + 2 * bit) % 5
    return index, image(MATRICES[index], point)


def native_step(point, counter):
    return step_bit(point, bin(counter).count("1") % 2)


def three_ticks(point):
    for counter in range(3):
        _, point = native_step(point, counter)
    return point


def chart(point):
    a, b, c, d, q, r = point
    return residues((a + c, b + d, a - c - 2, b - d - 1, sum(point)))


def port_reader(port, source):
    """Only the named four coordinates enter; None differs from payload zero."""
    u, v, q, r = port
    total = (u + v) % 5
    square = total * total % 5
    if square not in (1, 4):
        return None
    control = (3 * (square + 1)) % 5
    trace = (q + r + (2 * total if control == 0 else 0)) % 5
    if trace not in (1, 4):
        return None
    invariant = total * trace * (u - v - (2 if source else 1)) % 5
    if source:
        value = invariant - 1 if control == 0 else (1 - invariant) * 3
    else:
        value = invariant if control == 0 else (invariant - 3) * 3
    return control, value % 5


def readings(point):
    a, b, c, d, q, r = point
    return port_reader((a, c, q, r), True), port_reader((b, d, q, r), False)


def logical_result(point):
    source, memory = readings(point)
    check(source is not None and memory is not None, "not_ready", point)
    check(source[0] == memory[0], "control_disagreement", point)
    control = source[0]
    return ((memory[1], source[1], control) if control == 0
            else (source[1], memory[1], control))


def prefix_table(new, old, control):
    start = (new, old, 4 - new, 1 - old, control, 0)
    if control == 0:
        rows = (start, (old, new, 1 - old, 4 - new, 0, 0),
                (1 + old, 2 + new, 2 - old, 1 - new, 1, 0),
                (1 - old, 4 - new, 1 + old, 3 + new, 1, 1))
    else:
        rows = (start, (1 + new, old - 1, -new, -old, 4, 0), start,
                (2 - new, 1 - old, 4 + new, 3 + old, 0, 1))
    return tuple(residues(row) for row in rows)


def piston_shift(point, pair, delta):
    out = list(point)
    out[pair] = (out[pair] + delta) % 5
    out[pair + 2] = (out[pair + 2] - delta) % 5
    return tuple(out)


def main():
    labels = tuple(product(range(5), range(5), range(2)))
    endpoints, layers, mutant = {}, [set() for _ in range(4)], Counter()
    response_checks = 0
    for new, old, control in labels:
        expected = prefix_table(new, old, control)
        point, word = expected[0], []
        for counter in range(4):
            check(point == expected[counter], "prefix", new, old, control, counter)
            layers[counter].add(point)
            want = ((None, None) if control == 0 and counter < 3 else
                    ((control, old if control == 0 else new),
                     (control, new if control == 0 else old)))
            check(readings(point) == want, "prefix_readers", point, counter)
            if counter < 3:
                index, point = native_step(point, counter)
                word.append(index)
        check(tuple(word) == ((0, 2, 4) if control == 0 else (1, 1, 3)), "word")
        endpoints[(new, old, control)] = point
        check(logical_result(point) == (new, old, control), "endpoint_inverse")
        source, memory = readings(point)
        mutant["always_swap"] += (source[1], memory[1]) != (old, new)
        mutant["erase_old_on_write"] += control == 0 and source[1] != 0
        mutant["zero_is_blank"] += (source[1] == 0) + (memory[1] == 0)
        mutant["control_is_raw_q"] += point[4] != control
        for pair, delta in product(range(2), range(5)):
            actual = three_ticks(piston_shift(expected[0], pair, delta))
            target_pair = 1 - pair if control == 0 else pair
            check(actual == piston_shift(point, target_pair, -delta), "raw_response")
            response_checks += 1
    check(all(len(layer) == 50 for layer in layers), "prefix_injectivity")
    check(dict(mutant) == {"always_swap": 20, "erase_old_on_write": 20,
                          "zero_is_blank": 20, "control_is_raw_q": 50}, "mutants")

    stable = tuple(x for x in product(range(5), repeat=6) if sum(x) % 5 in (1, 4))
    check(len(stable) == 6250, "stable_count")
    tail, port_maps, selected = [], defaultdict(set), defaultdict(set)
    for point in stable:
        a, b, c, d, z = chart(point)
        if (a == b and a * a % 5 == 4) or ((a + b) % 5 == 0 and a * a % 5 == 1):
            tail.append(point)
        for bit in range(2):
            index, out = step_bit(point, bit)
            check(index in (1, 3, 4), "stable_generator")
            permutation = SWAP if index == 1 else tuple(range(6))
            for row in range(6):
                check(residues(MATRICES[index][row][:6]) ==
                      tuple(4 if col == permutation[row] else 0 for col in range(6)),
                      "stable_linear_part", index, row)
            expected = (-a, -b, c, d, -z) if index == 1 else (-a, -b, -c, -d, z)
            check(chart(out) == residues(expected), "stable_chart", point, bit)
            selected[(z, bit)].add(index)
            for coordinate in (4, 5):
                port_maps[(z, bit, coordinate, point[coordinate])].add(out[coordinate])
    check(len(selected) == 4 and all(len(v) == 1 for v in selected.values()), "common_word")
    check(len(port_maps) == 40 and all(len(v) == 1 for v in port_maps.values()), "closed_ports")

    check(len(tail) == 1000, "tail_count")
    tail_set, multiplicity, contexts = set(tail), Counter(), set()
    branches, transitions, paired_checks = Counter(), 0, 0
    for point in tail:
        result = logical_result(point)
        multiplicity[result] += 1
        control = result[2]
        branches[control] += 1
        a, b, c, d, z = chart(point)
        epsilon = a * (3 if control == 0 else 1) % 5
        check(epsilon in (1, 4), "context_orientation")
        contexts.add((result, epsilon, z, point[5]))
        new, old, _ = result
        check((a * z * c % 5, b * z * d % 5) ==
              residues((old + 1, new) if control == 0 else (1 - 2 * new, 3 + 2 * old)),
              "reader_invariant_relations", point)
        for bit in range(2):
            _, out = step_bit(point, bit)
            check(out in tail_set and logical_result(out) == result, "tail_closure")
            transitions += 1
        for delta in range(5):
            shifted = point[:4] + ((point[4] - delta) % 5, (point[5] + delta) % 5)
            check(readings(shifted) == readings(point), "paired_port_reader_invariance")
            paired_checks += 1
    check(set(multiplicity) == set(labels) and set(multiplicity.values()) == {20}, "logical_fibres")
    check(dict(branches) == {0: 500, 1: 500} and len(contexts) == 1000, "tail_contexts")
    check(all(x in tail_set for x in endpoints.values()), "prepared_tail_membership")
    print(json.dumps({"status": "PASS", "implementation": "homogeneous_matrix_break_check_v1",
                      "prefix_inputs": len(labels), "prefix_checkpoints": sum(map(len, layers)),
                      "raw_response_identities": response_checks, "stable_states": len(stable),
                      "stable_bit_transitions": 2 * len(stable), "closed_port_contexts": len(port_maps),
                      "tail_states": len(tail), "tail_bit_transitions": transitions,
                      "logical_results": len(multiplicity), "states_per_logical_result": 20,
                      "paired_reader_checks": paired_checks, "negative_control_rejections": dict(mutant)},
                     sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
