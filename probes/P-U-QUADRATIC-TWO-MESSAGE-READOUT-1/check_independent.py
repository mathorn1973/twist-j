# Copyright 2026 A. M. Thorn
# SPDX-License-Identifier: Apache-2.0

"""Exact independent check of the quadratic readout on the inherited domain.

The domain closure under native U is an inherited result, not re-audited here.
Every native six-tuple is visited, and membership is tested by equations.
The two readout coordinates are expanded directly in native coordinates.
"""

from collections import Counter
from hashlib import sha256
from itertools import product
import json


BLANK = -1


def readout(state):
    """Return the affine first coordinate and quadratic second coordinate."""
    a, b, c, d, q, r = state
    first = (3 * a + 2 * b + 3 * c + 2 * d + 2 * q + 2 * r) % 5
    second = (
        2 * b * b
        + 3 * d * d
        + 3 * a * b
        + 3 * a * d
        + 2 * b * c
        + 2 * c * d
        + 3 * b
        + d
        + 4
    ) % 5
    return first, second


def decode(first, second):
    """A total decoder on F5^2, with a distinct blank symbol."""
    if first == 0:
        return BLANK
    return (-first * first * second) % 5


def classify(state):
    """Return the inherited stratum and required label, or None outside it."""
    a, b, c, d, q, r = state
    sum_ac = (a + c) % 5
    sum_bd = (b + d) % 5
    total = (a + b + c + d + q + r) % 5
    matches = []
    if sum_ac == 1 and sum_bd == 0 and q == 0 and r == 1:
        matches.append(("blank", BLANK))
    if sum_ac == 3 and sum_bd == 2 and q == 1 and r == 4:
        matches.append(("first", (a - c - 2) % 5))
    if sum_bd == 0 and sum_ac in (1, 4) and total in (1, 4):
        matches.append(("tail", (sum_ac * total * (b - d - 1)) % 5))
    assert len(matches) <= 1, ("overlapping inherited strata", state, matches)
    return matches[0] if matches else None


def run():
    """Return (stable summary, sorted (state, label, first, second) rows)."""
    rows = []
    strata = Counter()
    labels = Counter()
    pair_labels = {}
    native_count = 0
    for state in product(range(5), repeat=6):
        native_count += 1
        membership = classify(state)
        if membership is None:
            continue
        stratum, label = membership
        first, second = readout(state)
        assert decode(first, second) == label, ("decoder mismatch", state)
        pair = (first, second)
        if pair in pair_labels:
            assert pair_labels[pair] == label, ("cross-label collision", state)
        pair_labels[pair] = label
        strata[stratum] += 1
        labels[label] += 1
        rows.append((state, label, first, second))

    rows.sort()
    assert native_count == 15625
    assert len(rows) == 550
    assert len({row[0] for row in rows}) == 550
    assert dict(strata) == {"blank": 25, "first": 25, "tail": 500}
    assert dict(labels) == {BLANK: 25, 0: 105, 1: 105, 2: 105, 3: 105, 4: 105}
    assert set(pair_labels) == set(product(range(5), repeat=2))

    cross_label_pairs = 0
    for index, left in enumerate(rows):
        for right in rows[index + 1:]:
            if left[1] != right[1]:
                cross_label_pairs += 1
                assert left[2:] != right[2:], ("unequal-label pair collision", left, right)
    assert cross_label_pairs == 123375

    encoded_rows = json.dumps(rows, separators=(",", ":"), ensure_ascii=True).encode("ascii")
    summary = {
        "native_states": native_count,
        "domain_states": len(rows),
        "stratum_counts": dict(sorted(strata.items())),
        "semantic_counts": {str(key): labels[key] for key in sorted(labels)},
        "readout_pairs": len(pair_labels),
        "unequal_label_state_pairs": cross_label_pairs,
        "cross_label_collisions": 0,
        "decoder_mismatches": 0,
        "rows_sha256": sha256(encoded_rows).hexdigest(),
    }
    return summary, rows


if __name__ == "__main__":
    result, _rows = run()
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
