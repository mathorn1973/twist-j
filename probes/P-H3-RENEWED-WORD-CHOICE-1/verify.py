# SPDX-License-Identifier: Apache-2.0
"""Trace repeated native H3 writes to branch-selecting receiver contacts."""
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
SECOND = HERE.parent / "P-H3-SECOND-WRITE-1"
THIRD = HERE.parent / "P-H3-THIRD-CELL-1"
CATEGORIES = ("A", "A181", "AA", "R", "RR")
MODES = ("ANY", "MARKED_MOVED", "BOTH_MOVED")
BINS = tuple(product(CATEGORIES, MODES))
RANK_FIELDS = ("rank", "ticks", "anchors", "repeats", "anchor_contacts", "anchor_moved",
               "anchor_active", "first_anchor", "anchor_moved_b1", "anchor_moved_b2")
EVENT_FIELDS = ("rank", "writer", "reader", "bit", "write", "read", "writer_tag",
                "reader_tag", "prior", "anchor")
CELL_FIELDS = ("writer_c", "writer_b", "donor_pre", "reader_pre", "reader_c", "reader_b")
PINS = {
    SECOND / "audit.cpp": "0434d95cb7b1c376ea81259be7266db8c964977ecb46c3c9aab6d3f620d590e9",
    SECOND / "EXPECTED.txt": "a02017a479b6a199a0aa5bbdac43c61f76dffe0c9331427cbf028bfdba72742a",
    THIRD / "kernel.py": "e12b05ab92a48cd65630fd689d880e5f36dcee08771e3703a01a357bba5f9f84",
    THIRD / "launches.py": "086ef90a76f929ffb0c1d9a1bf34d2d0ecb687cf13f9e2c12568d1e4a0457c93",
    THIRD / "launch43.json": "1a4d47ff21e95385f93fe05915aed409a38d1ebb40f3e2f0e724c6f8eb267d7f",
    THIRD / "measure.py": "be1eaa262ab1b4a238828322dcb6697a4e1c6da7019d7f12a1679e046c6ce960",
    THIRD / "observe.py": "41fdc74da9586dd5d1a2ae6fe85b7ca967c74baec12762af46fed557d8ea19b8",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def emit(section, data):
    print(json.dumps({"section": section, "value": data}, sort_keys=True, separators=(",", ":")))


def event_record(words):
    numbers = list(map(int, words))
    require(len(numbers) == len(EVENT_FIELDS) + 16 * len(CELL_FIELDS), "incomplete certificate")
    event = dict(zip(EVENT_FIELDS, numbers[:len(EVENT_FIELDS)]))
    require(event["anchor"] in (0, 1), "invalid anchor flag")
    event["anchor"] = bool(event["anchor"])
    for index, label in enumerate(CELL_FIELDS):
        offset = len(EVENT_FIELDS) + 16 * index
        event[label] = [numbers[start:start + 4] for start in range(offset, offset + 16, 4)]
    return event


def insert(mapping, key, value):
    require(key not in mapping, f"duplicate record {key}")
    mapping[key] = value


def parse(output):
    ranks, counts, cuts, arms = {}, {}, {}, {}
    for line in output.decode("ascii").splitlines():
        tag, *fields = line.split()
        if tag == "RANK":
            record = dict(zip(RANK_FIELDS, map(int, fields), strict=True))
            insert(ranks, record["rank"], record)
        elif tag == "CUT181":
            rank, admitted, moved, branch = map(int, fields)
            insert(cuts, rank, [admitted, moved, branch])
        elif tag == "MATCH":
            rank, category, mode, number = fields
            insert(counts, (int(rank), category, mode), int(number))
        elif tag == "CERT":
            category, mode, arm, *words = fields
            insert(arms, (category, mode, int(arm)), event_record(words))
        else:
            raise ValueError("unrecognized native record " + tag)
    require(set(ranks) == set(range(85)) and set(cuts) == {0, 22, 43}, "rank coverage")
    require(set(counts) == {(rank, c, m) for rank in ranks for c, m in BINS}, "incomplete census")
    original = [json.loads(line) for line in (SECOND / "EXPECTED.txt").read_bytes().splitlines()]
    anchors = {row["value"]["rank"]: row["value"] for row in original if row["section"] == "rank"}
    for rank, row in ranks.items():
        ceiling = 1048576 if rank == 43 else 65536 if rank in (0, 22) else 8192
        require((row["ticks"], row["anchors"], row["first_anchor"]) ==
                (ceiling, anchors[rank]["function_count"], anchors[rank]["function"]), "anchor census")
        for c in CATEGORIES:
            any_pair, marked, both = (counts[rank, c, m] for m in MODES)
            require(0 <= both <= marked <= any_pair, "inconsistent transfer cuts")
        for m in MODES:
            require(counts[rank, "A181", m] <= counts[rank, "A", m]
                    and counts[rank, "AA", m] <= counts[rank, "A", m]
                    and counts[rank, "RR", m] <= counts[rank, "R", m], "inconsistent source cuts")
    totals = {(c, m): sum(counts[rank, c, m] for rank in ranks) for c, m in BINS}
    require(set(arms) == {(c, m, arm) for (c, m), n in totals.items() if n for arm in (1, 2)},
            "missing or unexpected matched witness")
    pairs = {}
    for (category, mode), total in totals.items():
        if not total:
            continue
        pair = [arms[category, mode, i] for i in (1, 2)]
        marked = [
            event["prior"] > 0 if category in ("R", "RR") else
            event["anchor"] and (category != "A181" or event["write"] == 181) for event in pair
        ]
        moved = [e["reader_pre"][:2] != e["reader_c"][:2] for e in pair]
        require(all(marked) if category in ("AA", "RR") else any(marked), "misclassified write")
        require(mode != "MARKED_MOVED" or any(a and b for a, b in zip(marked, moved)), "missing delivery")
        require(mode != "BOTH_MOVED" or all(moved), "incomplete two-arm delivery")
        require(counts[pair[0]["rank"], category, mode] > 0, "certificate outside rank census")
        pairs[category, mode] = pair
    return ranks, cuts, counts, totals, pairs


def main():
    for path, expected in PINS.items():
        require(sha256(path.read_bytes()).hexdigest() == expected, "source drift: " + path.name)
    # Keep witness.py from this probe first in module resolution.
    sys.path.insert(1, str(THIRD))
    import launches
    import measure
    import witness
    fields = launches.four_wire(launches.bare_inputs())
    queries = "".join(f"2 {i} 0 {launches.encode(f)}\n" for i, f in enumerate(fields)).encode("ascii")
    with tempfile.TemporaryDirectory() as temporary:
        exe = Path(temporary) / "scan"
        subprocess.run(["g++", "-std=c++20", "-O3", str(HERE / "scan.cpp"), "-o", str(exe)], check=True)
        execution = subprocess.run([str(exe)], input=queries, capture_output=True, check=True)
        require(not execution.stderr, "unexpected scanner stderr")
    ranks, cuts, counts, totals, pairs = parse(execution.stdout)
    independent = witness.check(fields, list(pairs.values()))
    emit("inputs", {"launches_sha256": launches.LAUNCH_DIGEST, "ledger": measure.LEDGER,
                    "rank_fields": RANK_FIELDS, "pair_bins": BINS})
    for rank, row in sorted(ranks.items()):
        emit("rank", {"census": [row[field] for field in RANK_FIELDS],
                      "pairs": [counts[rank, c, m] for c, m in BINS]})
    emit("181_to_182", cuts)
    emit("pair_totals", {c: {m: totals[c, m] for m in MODES} for c in CATEGORIES})
    for (c, m), pair in pairs.items():
        emit("certificate", {"class": c, "transfer": m, "events": pair})
    emit("independent", independent)


if __name__ == "__main__":
    main()
