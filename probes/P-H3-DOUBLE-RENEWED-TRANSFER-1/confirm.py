# SPDX-License-Identifier: Apache-2.0
"""Confirm one two-renewal, two-transfer matched H3 certificate."""

import witness

k = witness.k
require = witness.m.require
REPLAY_LIMIT = 1_048_576


def half_gaps(cell):
    return (k.half(k.subtract(cell[0], cell[1])),
            k.half(k.subtract(cell[2], cell[3])))


def check(fields, events, *, full=False):
    """Check the certificate and report exact branch and replay evidence."""
    summary = {
        "events": 0,
        "full_replayed": 0,
        "arms": [],
        "theta": k.reported(k.THETA),
        "theta_squared": k.reported(k.multiply(k.THETA, k.THETA)),
    }
    if not events:
        return summary

    require(len(events) == 2, "expected one pair of H3 encounters")
    require({event["reader_tag"] for event in events} == {1, 2},
            "expected opposite active reader branches")
    first, second = sorted(events, key=lambda event: event["reader_tag"])
    a, b = (witness.local(event, len(fields)) for event in (first, second))
    rank = first["rank"]
    at = rank, first["read"], second["read"]
    require(all(event["prior"] > 0 and event["writer_tag"] == 2
                for event in (first, second)), (at, "two recurrent B2 writers"))
    require(all(first[key] == second[key] for key in ("rank", "writer", "reader", "bit"))
            and a["reader_pre"] == b["reader_pre"]
            and a["reader_c"][2:] == b["reader_c"][2:],
            (at, "same directed edge, matching and reader readiness"))
    require(all(a[key][:2] != b[key][:2] for key in ("writer_b", "reader_c", "reader_b")),
            (at, "distinct authored, incoming and final matter"))

    replay_records = []
    norms = []
    for event, cells in ((first, a), (second, b)):
        moved = [before != after for before, after
                 in zip(cells["reader_pre"][:2], cells["reader_c"][:2])]
        require(any(moved), (at, event["read"], "nonzero native material transfer"))
        d, f = half_gaps(cells["reader_c"])
        hd, hf = k.norm(d), k.norm(f)
        norms.append((hd, hf))
        summary["arms"].append({
            "read": event["read"],
            "reader_tag": event["reader_tag"],
            "material_rails_moved": moved,
            "d": k.reported(d),
            "f": k.reported(f),
            "h_d": k.reported(hd),
            "h_f": k.reported(hf),
        })
        if full or event["read"] <= REPLAY_LIMIT:
            replay_records.append((event, cells))

    (hd1, hf1), (hd2, hf2) = norms
    require(hf1 == hf2 == k.multiply(k.THETA, hd1)
            and hd2 == k.multiply(k.THETA, hf1), (at, "exact Hermitian branch equalities"))
    if replay_records:
        witness.replay(fields[rank], rank, replay_records)
    summary["events"] = 2
    summary["full_replayed"] = len(replay_records)
    return summary
