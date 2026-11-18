# SPDX-License-Identifier: Apache-2.0
"""Run the fixed H3 and D3 tests and their explicit normalization comparison."""

import json

import axis
import coupling
import matter
import phase
import shell
import signed
import tail
import transient


def emit(name, data):
    print(json.dumps({"stage":name, "result":data},sort_keys=True,separators=(",",":")))


if __name__ == "__main__":
    emit("signed_H3_source_codes", signed.run())
    emit("H3_point_source", axis.run())
    static = shell.run()
    emit("D3_static", static)
    emit("D3_infinite_green", tail.run())
    emit("D3_switched_source", transient.run())
    emit("H3_phase_read", phase.run())
    emit("alpha_normalization", coupling.run(static))
    emit("material_dispersion", matter.run())
