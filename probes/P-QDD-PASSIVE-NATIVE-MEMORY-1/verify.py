#!/usr/bin/env python3
"""P-QDD-PASSIVE-NATIVE-MEMORY-1 exact result-exposed proof audit.

Execute only after the complete public preregistration pin and byte readback.
Standalone standard library; no filesystem, network or previous-checker input.
"""
from collections import Counter, defaultdict, namedtuple
from fractions import Fraction as F
from itertools import product
import json
import sys

if not __debug__:
    raise RuntimeError("Optimized Python is outside the accepted environment")

IDS = ("PI-ALL", "PI-TRACE", "PI-LEG", "PI-PAIR", "PI-ATOMS")
BLOCKS = (((0, 1, 2),), ((0,), (1, 2)), ((0, 2), (1,)),
          ((0, 1), (2,)), ((0,), (1,), (2,)))
FAMILY = dict(zip(IDS, BLOCKS))
BALANCED = (0, 1, 2, -2, -1)
Record = namedtuple("Record", "partition_id support_state total_weight block_weights normalized_weight_state")
GROUPS = ("NATIVE_KERNELS", "FIVE_FIELD_RECORDS", "ALL_SOURCE_FACTOR",
          "EXACT_F3_FIBERS", "INITIALIZED_READBACK", "THREE_STATE_WITNESS",
          "PARTITION_INVENTORIES", "SUPPORTED_MAXIMA")
checks = Counter({g: 0 for g in GROUPS})
failures = Counter({g: 0 for g in GROUPS})
first_failures = {}


def check(group, condition, witness):
    checks[group] += 1
    if not condition:
        failures[group] += 1
        first_failures.setdefault(group, witness)


def generator(i, x):
    a, b, c, d, q, r = x
    if i == 0:
        values = (b, a, d, c, q, r)
    elif i == 1:
        values = (-c, -d, -a, -b, -q, -r)
    elif i == 2:
        values = (-c+2, -d+1+r, -a+2, -b+1-r, 1-q, -r)
    elif i == 3:
        values = (2-a, 1-b, 3-c, 4-d, 1-q, 1-r)
    elif i == 4:
        values = (2-a, 1-b, 3-c, 4-d, 2-q, 1-r)
    else:
        raise ValueError("Undeclared generator")
    return tuple(v % 5 for v in values)


# Independent affine specification in the same coordinate order.
AFFINE = (
    (((0,1,0,0,0,0),(1,0,0,0,0,0),(0,0,0,1,0,0),
      (0,0,1,0,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1)), (0,0,0,0,0,0)),
    (((0,0,-1,0,0,0),(0,0,0,-1,0,0),(-1,0,0,0,0,0),
      (0,-1,0,0,0,0),(0,0,0,0,-1,0),(0,0,0,0,0,-1)), (0,0,0,0,0,0)),
    (((0,0,-1,0,0,0),(0,0,0,-1,0,1),(-1,0,0,0,0,0),
      (0,-1,0,0,0,-1),(0,0,0,0,-1,0),(0,0,0,0,0,-1)), (2,1,2,1,1,0)),
    (((-1,0,0,0,0,0),(0,-1,0,0,0,0),(0,0,-1,0,0,0),
      (0,0,0,-1,0,0),(0,0,0,0,-1,0),(0,0,0,0,0,-1)), (2,1,3,4,1,1)),
    (((-1,0,0,0,0,0),(0,-1,0,0,0,0),(0,0,-1,0,0,0),
      (0,0,0,-1,0,0),(0,0,0,0,-1,0),(0,0,0,0,0,-1)), (2,1,3,4,2,1)),
)


def affine_generator(i, x):
    matrix, offset = AFFINE[i]
    return tuple((sum(a*b for a, b in zip(row, x))+c) % 5
                 for row, c in zip(matrix, offset))


def step(n, x, reference=False):
    index = (sum(x)+2*(n.bit_count() % 2)) % 5
    return (affine_generator if reference else generator)(index, x)


def outer(v, denominator):
    return tuple(tuple(F(a*b, denominator) for b in v) for a in v)


G = tuple(tuple(F(i == j)-F(1, 5) for j in range(4)) for i in range(4))
PT = outer((1, 1, 1, 1), 4)
PL = outer((1, -1, -1, 1), 4)
PR = tuple(tuple(F(i == j)-PT[i][j]-PL[i][j] for j in range(4)) for i in range(4))


def mv(matrix, v):
    return tuple(sum(a*b for a, b in zip(row, v)) for row in matrix)


def pairing(v, w):
    return sum(a*b for a, b in zip(v, mv(G, w)))


def read_pistons(p, pi, reference=False):
    v = tuple(BALANCED[a] for a in p)
    if reference:
        masses = tuple(pairing(v, mv(proj, v)) for proj in (PT, PL, PR))
        total = pairing(v, v)
    else:
        a, b, c, d = v
        s, ell = a+b+c+d, a-b-c+d
        masses = (F(s*s, 20), F(ell*ell, 4), F((a-d)**2+(b-c)**2, 2))
        total = F(sum(a*a for a in v))-F(s*s, 5)
    raw = tuple(sum((masses[a] for a in block), F(0)) for block in FAMILY[pi])
    if total == 0:
        return Record(pi, "ZERO_SUPPORT", F(0), raw, "ZERO_DENOMINATOR")
    return Record(pi, "SUPPORTED", total, raw,
                  ("NORMALIZED", tuple(w/total for w in raw)))


def coherent(record, pi):
    if record.partition_id != pi or len(record.block_weights) != len(FAMILY[pi]):
        return False
    if record.total_weight == 0:
        return (record.support_state == "ZERO_SUPPORT"
                and record.block_weights == (F(0),)*len(FAMILY[pi])
                and record.normalized_weight_state == "ZERO_DENOMINATOR")
    return (record.support_state == "SUPPORTED" and record.total_weight > 0
            and all(w >= 0 for w in record.block_weights)
            and sum(record.block_weights) == record.total_weight
            and record.normalized_weight_state ==
            ("NORMALIZED", tuple(w/record.total_weight for w in record.block_weights)))


def read_head(x, pi):
    return read_pistons(x[:4], pi)


def inverse_fiber(y):
    return (generator(0, generator(2, generator(4, y))),
            generator(3, y), generator(4, y),
            generator(3, generator(1, generator(3, y))),
            generator(4, generator(1, generator(3, y))))


def inverse_pistons(y):
    a, b, c, d, _, r = y
    return tuple(tuple(v % 5 for v in row) for row in
                 ((d+3-r, c+4, b+4+r, a),
                  (2-a, 1-b, 3-c, 4-d), (-c, -d, -a, -b)))


def phase_class(x):
    return (0, 1, 1, 2, 2)[sum(x) % 5]


def main():
    heads = tuple(product(range(5), repeat=6))
    pistons = tuple(product(range(5), repeat=4))
    supported_heads = sum(bool(any(x[:4])) for x in heads)
    records = {(p, pi): read_pistons(p, pi) for p in pistons for pi in IDS}
    record_counts = {}
    for x in heads:
        for i in range(5):
            gx = generator(i, x)
            check("NATIVE_KERNELS", gx == affine_generator(i, x), (x, i, "affine"))
            check("NATIVE_KERNELS", generator(i, gx) == x, (x, i, "involution"))
    check("FIVE_FIELD_RECORDS", Record._fields ==
          ("partition_id", "support_state", "total_weight", "block_weights", "normalized_weight_state"), "fields")
    check("FIVE_FIELD_RECORDS", supported_heads == 15600, "supported_source_count")
    for p in pistons:
        for pi in IDS:
            record = records[p, pi]
            check("FIVE_FIELD_RECORDS", record == read_pistons(p, pi, True), (p, pi, "matrix"))
            check("FIVE_FIELD_RECORDS", coherent(record, pi), (p, pi, "coherent"))
            check("FIVE_FIELD_RECORDS", (record.support_state == "ZERO_SUPPORT") == (not any(p)), (p, pi, "zero"))
    for x in heads:
        for pi in IDS:
            check("ALL_SOURCE_FACTOR", read_head(x, pi) == records[x[:4], pi], (x, pi))

    # Snapshot grouping audits the saved class on every origin at n=0,1,2,3.
    current = heads
    final_fibers = None
    for n in range(4):
        fibers = defaultdict(list)
        saved = defaultdict(list)
        for origin, checkpoint in zip(heads, current):
            fibers[checkpoint].append(origin)
            saved[checkpoint, phase_class(origin)].append(origin)
        for (checkpoint, cls), origins in saved.items():
            for pi in IDS:
                values = {records[x[:4], pi] for x in origins}
                check("INITIALIZED_READBACK", len(values) == 1, (n, checkpoint, cls, pi))
        if n == 3:
            final_fibers = fibers
        else:
            next_current = []
            for origin, checkpoint in zip(heads, current):
                successor = step(n, checkpoint)
                check("NATIVE_KERNELS", successor == step(n, checkpoint, True), (n, origin, "step"))
                next_current.append(successor)
            current = tuple(next_current)
    check("EXACT_F3_FIBERS", len(final_fibers) == 3125, "fiber_count")
    for y, origins in sorted(final_fibers.items()):
        inverse = inverse_fiber(y)
        triples = inverse_pistons(y)
        check("EXACT_F3_FIBERS", len(origins) == 5 and sum(y) % 5 == 1, (y, "size_sheet"))
        check("EXACT_F3_FIBERS", sorted(inverse) == sorted(origins), (y, "inverse_heads"))
        check("EXACT_F3_FIBERS", tuple(sum(x) % 5 for x in inverse) == (0,1,2,3,4), (y, "phase_order"))
        check("EXACT_F3_FIBERS", tuple(x[:4] for x in inverse) ==
              (triples[0], triples[1], triples[1], triples[2], triples[2]), (y, "piston_classes"))
        for cls, pi in product(range(3), IDS):
            candidates = [x for x in origins if phase_class(x) == cls]
            check("INITIALIZED_READBACK", bool(candidates) and all(
                records[x[:4], pi] == records[triples[cls], pi] for x in candidates), (y, cls, pi, "explicit_decoder"))

    witness_y = (0,0,0,1,0,0)
    witness = ((4,4,4,0,4,4),(2,1,3,3,2,1),(0,4,0,0,3,2))
    expected_mass = (F(6,5), F(64,5), F(4,5))
    for x, mass in zip(witness, expected_mass):
        y = x
        for n in range(3):
            y = step(n, y)
        check("THREE_STATE_WITNESS", y == witness_y and any(x[:4]), (x, "merged_supported"))
        for pi in IDS:
            check("THREE_STATE_WITNESS", records[x[:4], pi].total_weight == mass, (x, pi, "mass"))
    for pi in IDS:
        check("THREE_STATE_WITNESS", len({records[x[:4], pi] for x in witness}) == 3, (pi, "distinct"))

    expected_records = dict(zip(IDS, (19,35,62,63,65)))
    expected_patterns = dict(zip(IDS, ((2510,200,385,30),(2774,116,226,9),
                                     (2922,58,142,3),(2924,56,143,2),(2946,54,123,2))))
    expected_maxima = dict(zip(IDS, (7310,6845,6601,6598,6556)))
    pattern_order = ((2,2,1),(3,2),(4,1),(5,))
    report = {}
    for pi in IDS:
        patterns = Counter()
        maximum = supported_maximum = 0
        largest_class_count = 0
        selected, selected_supported = [], []
        for y, origins in sorted(final_fibers.items()):
            buckets, support_buckets = defaultdict(list), defaultdict(list)
            for x in origins:
                rec = records[x[:4], pi]
                buckets[rec].append(x)
                if rec.support_state == "SUPPORTED":
                    support_buckets[rec].append(x)
            pattern = tuple(sorted((len(v) for v in buckets.values()), reverse=True))
            patterns[pattern] += 1
            largest_class_count = max(largest_class_count, len(buckets))
            full_pick = max(buckets.values(), key=len)
            supported_pick = max(support_buckets.values(), key=len)
            maximum += len(full_pick)
            supported_maximum += len(supported_pick)
            selected.extend(full_pick)
            selected_supported.extend(supported_pick)
            check("SUPPORTED_MAXIMA", len(full_pick) == len(supported_pick), (y, pi, "pointwise_maximum"))
            check("SUPPORTED_MAXIMA", all(any(x[:4]) for x in supported_pick), (y, pi, "supported_witness"))
        inventory = tuple(patterns[p] for p in pattern_order)
        count = len({records[p, pi] for p in pistons})
        record_counts[pi] = count
        check("PARTITION_INVENTORIES", set(patterns) <= set(pattern_order) and sum(patterns.values()) == 3125, (pi, "all_patterns"))
        check("PARTITION_INVENTORIES", inventory == expected_patterns[pi], (pi, "patterns", inventory))
        check("PARTITION_INVENTORIES", count == expected_records[pi], (pi, "records", count))
        check("PARTITION_INVENTORIES", maximum == expected_maxima[pi], (pi, "maximum", maximum))
        check("PARTITION_INVENTORIES", largest_class_count == 3, (pi, "maximum_distinct_records", largest_class_count))
        check("SUPPORTED_MAXIMA", supported_maximum == expected_maxima[pi], (pi, "maximum", supported_maximum))
        check("SUPPORTED_MAXIMA", len(selected) == len(set(selected)) == maximum
              and len(selected_supported) == len(set(selected_supported)) == supported_maximum,
              (pi, "explicit_preparation_sets"))
        report[pi] = {"records": count, "patterns_221_32_41_5": inventory,
                      "max_full": maximum, "max_supported": supported_maximum,
                      "maximum_distinct_records_in_f3_fiber": largest_class_count}
    if set(checks) != set(GROUPS) or any(checks[g] == 0 for g in GROUPS):
        raise RuntimeError("Incomplete frozen audit inventory")
    result = {"probe": "P-QDD-PASSIVE-NATIVE-MEMORY-1",
              "verdict": "FALSIFIED" if sum(failures.values()) else "PASS",
              "layer": "L1", "native_heads": len(heads), "supported_heads": supported_heads,
              "balanced_vectors": len(pistons), "f3_fibers": len(final_fibers),
              "groups": {g: {"checks": checks[g], "failures": failures[g]} for g in GROUPS},
              "partitions": report, "first_failures": first_failures}
    print(json.dumps(result, sort_keys=True, separators=(",", ":"), default=str))


if __name__ == "__main__":
    sys.stdout.reconfigure(newline="\n")
    try:
        main()
    except Exception as exc:
        print(json.dumps({"probe": "P-QDD-PASSIVE-NATIVE-MEMORY-1", "verdict": "STOP",
                          "reason": type(exc).__name__+": "+str(exc)}, sort_keys=True))
        raise SystemExit(1)
