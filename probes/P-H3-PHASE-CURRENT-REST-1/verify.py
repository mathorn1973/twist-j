# SPDX-License-Identifier: Apache-2.0
"""Run the registered comparisons and print exact deterministic records."""

import json

import charge
import legacy
import mass
import phase
import sector
import transducer
from native import cell, h3, step


def energy_transfer():
    expected = h3.scale(8, h3.sub(h3.ONE, h3.T))
    records = []
    for code in range(5):
        for center in phase.CENTERS:
            post_c, post_b, _ = step(phase.build(code, center), 0)
            for x in range(5):
                before = cell(post_c, x, 0)
                after = cell(post_b, x, 0)
                deltas = tuple(h3.ring_sum(h3.sub(h3.h(after[i]), h3.h(before[i]))
                                           for i in lanes) for lanes in ((0, 1), (2, 3)))
                target = expected if x == code else h3.ZERO
                h3.require(deltas == (h3.scale(-1, target), target), "local Hermitian transfer")
            records.append((code, center))
    h3.require(h3.scalar_account(expected) == -8, "signed trace payment")
    return {"histories": len(records), "delta_radiation_H_active_reader": expected,
            "delta_radiation_Q_active_reader": -8, "delta_matter_Q_active_reader": 8,
            "delta_H_each_idle_reader": h3.ZERO}


if __name__ == "__main__":
    for name, test in (("phase", phase.run), ("payment", energy_transfer),
                       ("signed_source_phase_read", transducer.run), ("historical_cuts", legacy.run), ("signed_current", charge.run), ("rest_modes", mass.run),
                       ("axis_conjugacy", sector.run)):
        print(json.dumps({"test": name, "result": test()}, sort_keys=True, separators=(",", ":")))
