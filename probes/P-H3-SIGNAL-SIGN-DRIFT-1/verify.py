# SPDX-License-Identifier: Apache-2.0
"""Run the frozen radiation, response and matter tests in order."""

import json

import anchor
import bulk
import calibrated
import charge
import drift
import light


if __name__ == "__main__":
    for name, experiment in (("light", light.run), ("packet_calibration", calibrated.run),
                             ("crossed_current", charge.run), ("primitive_anchor", anchor.run),
                             ("drift_census", drift.run), ("material_wave", bulk.run)):
        print(json.dumps({"stage":name, "result":experiment()}, sort_keys=True, separators=(",",":")))
