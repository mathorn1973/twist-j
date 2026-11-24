#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Post-run comparison of the two separately frozen JSON output schemas.

This is evidence bookkeeping, not a new preregistered scientific verifier.
It does not execute or import either frozen checker.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
primary = json.loads((ROOT / "EXPECTED.txt").read_text())
breaker = json.loads((ROOT / "BREAK_EXPECTED.txt").read_text())
comparisons = 0


def equal(label, left, right):
    global comparisons
    if left != right:
        raise AssertionError(label)
    comparisons += 1


equal("preparation scale", primary["T"], breaker["T"])
equal("five receiver responses", primary["receiver_control"], breaker["receiver"])
for name in ("P27", "P35"):
    matrix = primary["words"][name]["matrix"]
    continuity = primary["words"][name]["continuity"]
    source = breaker["source_and_G1"][name]
    witness = breaker["matrix"][name]
    for left, right in (("admitted", "admitted"),
                        ("state_changing", "changed"),
                        ("refused", "refused"),
                        ("source_H", "path_H"),
                        ("source_path_Q", "path_Q"),
                        ("source_state_Q", "Q_initial")):
        equal(name + "/source/" + left, matrix[left], source[right])
    equal(name + "/diagonals", matrix["admitted"] - matrix["state_changing"],
          source["diagonal"])
    equal(name + "/source attempts", matrix["admitted"] + matrix["refused"],
          source["attempts"])
    equal(name + "/complete edge-current vector", continuity["delta_field"],
          source["delta_E"])
    equal(name + "/field return", continuity["field_return"], source["field_return"])
    equal(name + "/diagnostic account change",
          continuity["diagnostic_terminal_field_account_change"],
          source["diagnostic_final"] - source["diagnostic_initial"])
    equal(name + "/continuity cuts", continuity["cuts_forward_inverse"],
          source["attempts"] + source["inverse_attempts"])
    for left, right in (("initial_complete_Q", "Q_initial"),
                        ("normalized_determinant", "det_normalized"),
                        ("extended_H", "extended_H"),
                        ("terminal_banks_sha256", "state_sha256"),
                        ("all_banks_return", "all_banks_return")):
        equal(name + "/matrix/" + left, matrix[left], witness[right])
    equal(name + "/raw determinant",
          [primary["T"] ** 6 * x for x in matrix["normalized_determinant"]],
          witness["determinant"])
    equal(name + "/extended path trace",
          2 * matrix["extended_H"][0] + matrix["extended_H"][1],
          witness["extended_path_Q"])
    equal(name + "/primitive forward and inverse",
          matrix["primitive_forward_inverse"],
          [witness["attempts"], witness["inverse_attempts"]])

print("COMMON OUTPUT COMPARISON PASS comparisons=" + str(comparisons))
