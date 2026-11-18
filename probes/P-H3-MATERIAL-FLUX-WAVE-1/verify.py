# SPDX-License-Identifier: Apache-2.0
"""Run the three frozen native H3 experiments in their declared order."""

import json

import flux
import matter
import packet
import recoil


def emit(stage, data):
    print(json.dumps({"stage": stage, "result": data}, sort_keys=True, separators=(",", ":")))


def charge(rows):
    measured = {(r["orientation"], r["geometry"], r["source_sign"], r["test_sign"]): r["flux_q"]
                for r in rows}
    cases = []
    for orientation in (1, -1):
        for source in (-1, 1):
            difference = [measured[orientation, "near", source, test]
                          - measured[orientation, "far", source, test] for test in (-1, 1)]
            cases.append({"orientation": orientation, "source_sign": source,
                          "excess_for_negative_positive_probe": difference,
                          "opposite_nonzero": difference[0] != 0 and difference[0] == -difference[1]})
    return {"rows": cases, "opposite_nonzero_in_all_arms": all(c["opposite_nonzero"] for c in cases)}


if __name__ == "__main__":
    transport = flux.run()
    emit("1_directed_flux", transport)
    emit("2_wave_packet", packet.run())
    emit("3a_independent_sign", charge(transport["rows"]))
    emit("3b_localized_matter", matter.run())
    emit("3c_momentum_candidate", recoil.run())
