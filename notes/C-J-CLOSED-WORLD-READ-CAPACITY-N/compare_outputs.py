#!/usr/bin/env python3
"""Post-run record comparison, not a third scientific implementation.

Written after both frozen first runs. Normalizes their deliberately different
output schemas; does not import either scientific program or repeat the audit.
"""
from collections import defaultdict
import json
from pathlib import Path

base = Path(__file__).resolve().parent
builder = defaultdict(list)
lines = (base / "EXPECTED.txt").read_text().splitlines()
assert lines[-1] == "ALL PASS"
for line in lines[:-1]:
    kind, value = line.split(" ", 1)
    builder[kind].append(json.loads(value))
breaker = defaultdict(list)
for line in (base / "BREAK_EXPECTED.txt").read_text().splitlines():
    row = json.loads(line)
    breaker[row["type"]].append(row)
names = {"J": "J", "phi^-1": "phi_inverse", "z": "zeta", "J^2": "J_squared"}
pending = {}
for row in builder["CENSUS"]:
    for m in range(2, 8):
        key = row["u"], row["n"], m
        assert key not in pending
        pending[key] = row
compared = finite = 0
for row in breaker["CENSUS"]:
    key = names[row["unit"]], row["n"], row["m"]
    other = pending.pop(key)
    if "status" in other:
        assert other["status"] == "INFINITE_QUOTIENT"
        assert row["F"] == row["possible"] == "INFINITE"
        assert row["P"] is None and row["c"] is None
    else:
        cycles = dict(other["cycles"])
        assert row["F"] == other["states"]
        assert row["P"] == cycles[row["n"]] * row["n"]
        assert {int(k): v for k, v in row["cycles"].items()} == cycles
        assert row["possible"] == dict(other["readers"])[row["m"]]
        finite += 1
    compared += 1
assert not pending and compared == 288 and finite == 276
onsets = {(r["k"], r["m"]): (r["n0"], r["sufficient_onset"])
          for r in builder["ONSET"]}
assert len(onsets) == len(breaker["ONSET"]) == 6
for row in breaker["ONSET"]:
    assert onsets[row["k"], row["m"]] == (row["n0"], row["n_star"])
assert builder["STRIDES"][0] == [[r["denominator"], r["stride"]]
                                  for r in breaker["STRIDE"]]
assert breaker["SUMMARY"] == [{"census_rows": 288, "status": "PASS", "type": "SUMMARY"}]
print("COMPARISON PASS: 276 finite decisions, 12 infinite rows, 6 onsets, 4 strides")
