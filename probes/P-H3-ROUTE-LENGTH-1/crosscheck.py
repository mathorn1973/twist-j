# SPDX-License-Identifier: Apache-2.0
"""Compare the independent native audit TSV to the prepared JSONL records."""

import argparse
import csv
import json
from itertools import product
from pathlib import Path

COMPARISONS = ("plus_zero", "minus_zero", "plus_minus")
IDENTIFIERS = {"rank", "distance", "comparison"}
METRICS = (
    "first_tick", "donor_x", "local_equal", "donor_differs", "matter_equal",
    "first_three_equal", "isolated", "hit", "survives", "retains",
    "radiation_echo", "conversion_tick", "conversion_left_tag",
    "conversion_right_tag", "conversion_left_moves", "conversion_right_moves",
    "conversion_survives", "conversion_retains",
)


def insert(rows, key, values):
    if key in rows:
        raise ValueError(f"duplicate key {key}")
    rows[key] = values


def prepared(path):
    rows = {}
    with path.open(encoding="utf-8") as stream:
        for line in stream:
            record = json.loads(line)
            if record["section"] != "prepared":
                continue
            value = record["value"]
            for comparison, flags in value["comparisons"].items():
                key = value["rank"], value["distance"], comparison
                if (flags["rank"], flags["distance"], flags["comparison"]) != key:
                    raise ValueError(f"unexpected identifiers at {key}")
                projected = {name: flag for name, flag in flags.items()
                             if name not in IDENTIFIERS | {"arrival", "conversion", "phase"}}
                if set(projected) != set(METRICS):
                    raise ValueError(f"unexpected Python metrics at {key}: {sorted(projected)}")
                if any(type(flag) not in (bool, int) for flag in projected.values()):
                    raise ValueError(f"non-integer Python metric at {key}")
                insert(rows, key, projected)
    return rows


def native(path):
    rows = {}
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        fields = reader.fieldnames or []
        if len(fields) != len(IDENTIFIERS) + len(METRICS) or set(fields) != IDENTIFIERS | set(METRICS):
            raise ValueError(f"unexpected C++ TSV fields: {fields}")
        for row in reader:
            if None in row:
                raise ValueError(f"unexpected extra TSV values on line {reader.line_num}")
            key = int(row["rank"]), int(row["distance"]), row["comparison"]
            insert(rows, key, {name: int(row[name]) for name in METRICS})
    return rows


def compare(expected_path, audit_path):
    expected = prepared(expected_path)
    actual = native(audit_path)
    domain = set(product(range(85), range(1, 5), COMPARISONS))
    for source, rows in (("Python", expected), ("C++", actual)):
        if rows.keys() != domain:
            missing = sorted(domain - rows.keys())
            extra = sorted(rows.keys() - domain)
            raise ValueError(f"{source} missing {len(missing)} keys {missing[:3]} "
                             f"and has {len(extra)} extra keys {extra[:3]}")
    for key in sorted(domain):
        for metric in METRICS:
            left, right = expected[key][metric], actual[key][metric]
            if left != right:
                raise ValueError(f"{key} {metric}: Python={left!r}, C++={right!r}")
    print(f"matched {len(domain)} keys and {len(domain) * len(METRICS)} metric values")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("expected", type=Path, help="Python verifier JSONL")
    parser.add_argument("audit", type=Path, help="C++ audit TSV")
    args = parser.parse_args()
    try:
        compare(args.expected, args.audit)
    except (OSError, TypeError, ValueError, KeyError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
