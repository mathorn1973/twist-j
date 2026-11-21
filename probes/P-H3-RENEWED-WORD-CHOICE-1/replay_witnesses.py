# SPDX-License-Identifier: Apache-2.0
"""Post-result independent replay of exactly the frozen H3 event certificates."""

from collections import defaultdict
from functools import lru_cache
from hashlib import sha256
import json
import sys

import verify as pinned


EXPECTED_SHA256 = "cd60930de63cc0f00a8af80e5f0c107f653f6429c48c1f571bd65ea996e3f8fe"


def main():
    data = (pinned.HERE / "EXPECTED.txt").read_bytes()
    pinned.require(sha256(data).hexdigest() == EXPECTED_SHA256, "unexpected frozen result")
    for path, expected in pinned.PINS.items():
        pinned.require(sha256(path.read_bytes()).hexdigest() == expected,
                       "inherited source drift: " + path.name)

    sys.path.insert(1, str(pinned.THIRD))
    import kernel
    import launches
    import witness

    # Bound memoization for a longer replay. The original exact functions,
    # working precision and witness predicates are used without changes.
    for name in ("multiply", "norm", "contact", "scatter"):
        operation = getattr(kernel, name)
        setattr(kernel, name, lru_cache(maxsize=131072)(operation.__wrapped__))

    fields = launches.four_wire(launches.bare_inputs())
    records = [json.loads(line) for line in data.splitlines()]
    sections = {
        row["section"]: row["value"] for row in records
        if row["section"] in {"inputs", "independent", "pair_totals"}
    }
    encoded = "".join(launches.encode(field) + "\n" for field in fields).encode("ascii")
    pinned.require(sha256(encoded).hexdigest() == sections["inputs"]["launches_sha256"],
                   "original ordered launch bytes")

    certificates = [row["value"] for row in records if row["section"] == "certificate"]
    bins = [(entry["class"], entry["transfer"]) for entry in certificates]
    pinned.require(len(bins) == len(set(bins))
                   and set(bins) == {(category, mode) for category, mode in pinned.BINS
                                     if sections["pair_totals"][category][mode] > 0},
                   "frozen certificate inventory")
    pairs = [entry["events"] for entry in certificates]
    pinned.require(witness.check(fields, pairs) == sections["independent"],
                   "original local qualification or counts changed")

    unique, by_rank = {}, defaultdict(list)
    for pair in pairs:
        for event in pair:
            identity = tuple(event[key] for key in ("rank", "writer", "reader", "write", "read"))
            if identity not in unique:
                unique[identity] = event
                by_rank[event["rank"]].append((event, witness.local(event, len(fields))))
    pinned.require(len(unique) == 4 and set(by_rank) == {43}
                   and max(event["read"] for event in unique.values()) == 735779,
                   "unexpected supplemental replay selection")

    pinned.emit("start", {"expected_sha256": EXPECTED_SHA256, "events": len(unique),
                          "ranks": sorted(by_rank), "last_read": 735779})
    for rank, events in sorted(by_rank.items()):
        witness.replay(fields[rank], rank, events)
    for identity, event in sorted(unique.items()):
        pinned.emit("replayed", {key: event[key] for key in pinned.EVENT_FIELDS})
    for entry in certificates:
        if (entry["class"], entry["transfer"]) == ("R", "BOTH_MOVED"):
            pinned.emit("R/BOTH_MOVED", [
                {"read": event["read"], "reader_tag": event["reader_tag"],
                 "donor_matter": event["donor_pre"][:2],
                 "arrival_matter": event["reader_c"][:2],
                 "output_matter": event["reader_b"][:2]}
                for event in entry["events"]
            ])
    pinned.emit("result", {"status": "PASS", "full_replayed": len(unique)})


if __name__ == "__main__":
    main()
