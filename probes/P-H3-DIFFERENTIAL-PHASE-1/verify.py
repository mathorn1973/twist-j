# SPDX-License-Identifier: Apache-2.0
"""Exact paired-radius native phase reads and scalar work comparators."""

import json

import anchored
import d3_read
import emitter
import native_read
import quadrature
import source_cycle


def emit(stage, observation):
    print(json.dumps({"stage": stage, "result": observation}, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    emit("shared_path", native_read.run())
    emit("biased_anchors", anchored.run())
    emit("autonomous_source", emitter.run())
    emit("isolated_recurrence", source_cycle.run())
    emit("phase_work_controls", quadrature.run())
    emit("D3_work_and_flight", d3_read.run())
