# SPDX-License-Identifier: Apache-2.0
"""Exact field-only H3 phase response, crossed controls and distance experiment."""

from fractions import Fraction
import json

import crossed
import distance
import native
from radiative_measurement import measurements


def centroid(records):
    h3 = native.h3
    out = {}
    for arm, row in records["live"].items():
        incoming, outgoing = row["post_c"], row["post_b"]
        increments = []
        for lanes in ((0, 1), (2, 3)):
            increments.append(h3.ring_sum(h3.sub(h3.h(outgoing[i]), h3.h(incoming[i]))
                                          for i in lanes))
        expected = (2, 0, 4, 4) if arm == "low" else (2, 0, -6, -6)
        h3.require(increments == [expected, h3.scale(-1, expected)], "local Hermitian exchange")
        qm = lambda words: sum(h3.scalar_account(h3.h(word)) for word in words[:2])
        target, anchor = qm(outgoing), qm(row["reference"])
        mean = Fraction(target + 3 * anchor, target + anchor)
        h3.require(mean == (2 if arm == "low" else Fraction(5, 3)), "unwrapped weighted mean")
        out[arm] = {"delta_H_matter": expected, "delta_Q_matter": h3.scalar_account(expected),
                    "initial_matter_weights": [qm(incoming), anchor],
                    "final_matter_weights": [target, anchor], "final_weighted_mean": str(mean),
                    "matter_support_y": [1, 3]}
    return out


def emit(name, result):
    print(json.dumps({"test": name, "result": result}, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    nearest = measurements(native)
    emit("field_only", nearest)
    emit("pinned_motion", centroid(nearest))
    emit("crossed_signs", crossed.run(native))
    emit("distance", distance.run(native))
