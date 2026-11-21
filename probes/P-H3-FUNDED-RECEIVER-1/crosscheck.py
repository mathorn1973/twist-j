# SPDX-License-Identifier: Apache-2.0
"""Compare paired Python and C++ output and summarize the complete C++ survey."""

import argparse
import csv
import json
from pathlib import Path

HEADER = (
    "mode rank tick ray first_any_age first_any_stage first_corr_age "
    "first_isolated_age first_work_age work_actual_tag work_control_tag "
    "survival actual_hold pair_hold held_age held_actual_tag held_control_tag"
).split()
RANKS = set(range(85))
WINDOW, HORIZON = 128, 64


def require(predicate, message, *context):
    if not predicate:
        raise ValueError((message, *context))


def index_rows(records, label):
    indexed = {}
    for row in records:
        require(
            len(row) == len(HEADER) and all(type(value) is int for value in row),
            "invalid projection row", label, row,
        )
        mode, rank, tick, ray = row[:4]
        require(mode >= 0 and rank in RANKS, "invalid projection key", label, row[:4])
        require(1 <= tick <= WINDOW and ray in (-1, 1), "invalid emission", label, row[:4])
        require(all(0 <= row[i] <= HORIZON for i in (4, 6, 7, 8, 14)),
                "invalid projected age", label, row)
        require(row[5] in (0, 1, 2) and bool(row[5]) == bool(row[4]),
                "invalid first difference stage", label, row)
        require(all(row[i] in (0, 1, 2) for i in (9, 10, 15, 16)),
                "invalid collision tag", label, row)
        require(all(row[i] in (0, 1) for i in (11, 12, 13)), "invalid retention bit", label, row)
        key = mode, rank, tick
        require(key not in indexed, "duplicate emission", label, key)
        indexed[key] = tuple(row)
    return indexed


def read_audit(path):
    with path.open(encoding="utf-8", newline="") as source:
        records = csv.reader(source, delimiter="\t")
        require(next(records, None) == HEADER, "C++ header mismatch", path)
        return index_rows((list(map(int, row)) for row in records), "C++")


def indexed_ticks(rows, modes):
    ticks = {(mode, rank): [] for mode in modes for rank in RANKS}
    for mode, rank, tick in rows:
        ticks[mode, rank].append(tick)
    return {key: sorted(value) for key, value in ticks.items()}


def read_primary(path):
    modes, primary = set(), {}
    with path.open(encoding="utf-8") as source:
        for line in source:
            section = json.loads(line)
            if section["section"] != "mode":
                continue
            report = section["value"]
            mode = report["mode"]
            require(type(mode) is int and mode >= 0 and mode not in modes,
                    "invalid or repeated Python mode", mode)
            modes.add(mode)
            rows = index_rows(report["rows"], "Python")
            require(all(key[0] == mode for key in rows), "Python row in wrong mode", mode)
            ticks = indexed_ticks(rows, [mode])
            ranks = set()
            for rank_record in report["rank_records"]:
                rank = rank_record["rank"]
                require(type(rank) is int and rank in RANKS and rank not in ranks,
                        "invalid or duplicate Python rank", mode, rank)
                ranks.add(rank)
                require(rank_record["emission_ticks"] == ticks[mode, rank],
                        "Python projected ticks and rank record differ", mode, rank)
                require(rank_record["event_count"] == len(ticks[mode, rank]),
                        "Python incorrect rank event count", mode, rank)
            require(ranks == RANKS, "Python rank coverage", mode, sorted(RANKS - ranks))
            primary.update(rows)
    require(modes, "no Python mode records", path)
    return primary, modes


def compare(primary, audit, modes):
    selected = {key: row for key, row in audit.items() if key[0] in modes}
    primary_ticks = indexed_ticks(primary, modes)
    audit_ticks = indexed_ticks(selected, modes)
    for key in sorted(primary_ticks):
        require(primary_ticks[key] == audit_ticks[key], "emission tick mismatch",
                key, primary_ticks[key], audit_ticks[key])
    for key, expected in sorted(primary.items()):
        observed = selected[key]
        differences = {
            column: (a, b) for column, a, b in zip(HEADER, expected, observed) if a != b
        }
        require(not differences, "projection mismatch", key, differences)


def summarize(rows, modes):
    by_mode = {mode: [] for mode in modes}
    for row in rows.values():
        by_mode[row[0]].append(row)

    def count(rows, condition):
        qualifying = [row for row in rows if condition(row)]
        return {"events": len(qualifying), "ranks": len({row[1] for row in qualifying})}

    return [
        {
            "mode": mode,
            "all": count(events, lambda row: True),
            "west": count(events, lambda row: row[3] == -1),
            "first_isolated": count(events, lambda row: row[7] != 0),
            "work": count(events, lambda row: row[8] != 0),
            "held": count(events, lambda row: row[14] != 0),
            "west_work": count(events, lambda row: row[3] == -1 and row[8] != 0),
            "west_held": count(events, lambda row: row[3] == -1 and row[14] != 0),
            "work_at_first_isolated": count(events, lambda row: row[7] != 0 and row[7] == row[8]),
            "held_at_first_isolated": count(events, lambda row: row[7] != 0 and row[7] == row[14]),
        }
        for mode, events in sorted(by_mode.items())
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primary", type=Path)
    parser.add_argument("audit", type=Path)
    parser.add_argument(
        "--modes", nargs="+", type=int,
        help="complete preregistered C++ mode IDs, including modes with zero emissions",
    )
    args = parser.parse_args()

    primary, selected = read_primary(args.primary)
    audit = read_audit(args.audit)
    observed = {key[0] for key in audit}
    modes = selected | observed
    if args.modes is not None:
        modes = set(args.modes)
        require(len(modes) == len(args.modes) and min(modes) >= 0, "invalid explicit modes")
        require(selected | observed <= modes, "unexpected mode", sorted((selected | observed) - modes))
    compare(primary, audit, selected)
    print(json.dumps({
        "checked_modes": sorted(selected),
        "checked_ranks_per_mode": len(RANKS),
        "checked_events": len(primary),
        "checked_columns_per_event": len(HEADER),
        "survey": summarize(audit, modes),
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
