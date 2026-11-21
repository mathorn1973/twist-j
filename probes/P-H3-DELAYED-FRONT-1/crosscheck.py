# SPDX-License-Identifier: Apache-2.0
"""Compare all native C++ projections with the delayed Python verifier."""

import argparse
import csv
from itertools import product
import json
from pathlib import Path

DIRECTIONS = {"west": -1, "east": 1}
FIRST = ("rank", "tick", "length", "target", "ray", "first_age", "first_stage",
         "first_mask", "arrival")
ARRIVAL = ("bit", "donor", "incoming", "original", "isolated", "pre_equal",
           "donor_differs", "other_equal", "actual_move", "control_move",
           "suppression", "actual_write", "control_write", "matter_contrast",
           "actual_tag", "control_tag", "actual_phase", "control_phase")
NEXT = ("corr_contrast", "matter_contrast", "field_contrast", "same_corr_contrast",
        "same_field_pair", "same_matter_pair", "retained_actual_write",
        "retained_control_write")
FIELDS = FIRST + ARRIVAL + tuple(f"{stage}_{field}" for stage, field in product("CB", NEXT))


def encode(value):
    if value is None:
        return "-"
    if isinstance(value, bool):
        return str(int(value))
    return str(value)


def project(row):
    first = row["first_any"]
    arrival = row["first_corr"]
    values = [row["rank"], row["tick"], row["length"], row["target"], DIRECTIONS[row["ray"]],
              first["age"] if first else 0, first["stage"] if first else None,
              sum(1 << lane for lane in first["lanes"]) if first else 0,
              arrival["age"] if arrival else 0]
    if not arrival:
        values.extend([None] * (len(ARRIVAL) + 2 * len(NEXT)))
    else:
        values.extend([arrival["bit"], arrival["donor"], DIRECTIONS[arrival["incoming"]],
                       arrival["orientation"] == "original", arrival["isolated"],
                       arrival["recipient_pre_equal"], arrival["donor_contrast"],
                       arrival["other_lanes_equal"]])
        values.extend(arrival[name] for name in ARRIVAL[8:14])
        values.extend(arrival["tags"])
        values.extend(arrival["sectors"] if arrival["sectors"] is not None else (None, None))
        values.extend(arrival[f"next_{stage}"][name] for stage, name in product("CB", NEXT))
    if len(values) != len(FIELDS):
        raise ValueError(f"projection width differs for {tuple(values[:3])}")
    return tuple(map(encode, values))


def add_row(rows, key, values, label):
    if key in rows:
        raise ValueError(f"{label} duplicate {key}")
    rows[key] = values


def check_keys(rows, required, label):
    if rows.keys() != required:
        missing, extra = sorted(required - rows.keys()), sorted(rows.keys() - required)
        raise ValueError(f"{label} missing {len(missing)} keys {missing[:3]} "
                         f"and has {len(extra)} extra keys {extra[:3]}")


def read_python(path):
    events = {}
    ranks = {}
    with path.open(encoding="utf-8-sig") as stream:
        for line in stream:
            record = json.loads(line)
            value = record["value"]
            if record["section"] == "rank":
                ticks = value["emission_ticks"]
                if ticks != sorted(set(ticks)) or any(type(t) is not int or not 1 <= t <= 128 for t in ticks):
                    raise ValueError(f"invalid emission ticks at rank {value['rank']}")
                add_row(ranks, value["rank"], ticks, "Python rank")
            elif record["section"] == "event_distance":
                key = value["rank"], value["tick"], value["length"]
                add_row(events, key, project(value), "Python event")
    check_keys(ranks, set(range(85)), "Python rank")
    required = {(rank, tick, length) for rank, ticks in ranks.items()
                for tick in ticks for length in range(1, 5)}
    check_keys(events, required, "Python event")
    return events


def read_native(path):
    events = {}
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.reader(stream, delimiter="\t")
        if tuple(next(reader, [])) != FIELDS:
            raise ValueError("C++ TSV header differs")
        for row in reader:
            if len(row) != len(FIELDS):
                raise ValueError(f"C++ row {reader.line_num} has {len(row)} columns")
            key = tuple(map(int, row[:3]))
            add_row(events, key, tuple(row), "C++ event")
    return events


def compare(expected_path, audit_path):
    expected = read_python(expected_path)
    actual = read_native(audit_path)
    check_keys(actual, expected.keys(), "C++ event")
    for key in sorted(expected):
        for name, left, right in zip(FIELDS, expected[key], actual[key]):
            if left != right:
                raise ValueError(f"{key} {name}: Python={left!r}, C++={right!r}")
    print(f"matched {len(expected)} event-distance rows and {len(expected) * len(FIELDS)} values")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("expected", type=Path, help="delayed verifier JSONL")
    parser.add_argument("audit", type=Path, help="C++ audit TSV")
    args = parser.parse_args()
    try:
        compare(args.expected, args.audit)
    except (OSError, TypeError, KeyError, ValueError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
