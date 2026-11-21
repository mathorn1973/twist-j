# SPDX-License-Identifier: Apache-2.0
"""Replay mode 324 and characterize held events within the registered window."""

from argparse import ArgumentParser
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import sys


def need(ok, context):
    if not ok:
        raise AssertionError(context)


def digest_rows(rows):
    return sha256("".join(" ".join(map(str, row)) + "\n" for row in rows).encode("ascii")).hexdigest()


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("probe", type=Path, help="directory containing the pinned probe")
    parser.add_argument("primary", type=Path, help="frozen census output")
    args = parser.parse_args()
    sys.path.insert(0, str(args.probe.resolve()))
    import bank
    import kernel as k
    import measure

    with args.primary.open(encoding="utf-8") as source:
        census = {entry["value"]["mode"]: entry["value"] for entry in map(json.loads, source)
                  if entry["section"] == "survey"}
    need(set(census) == set(bank.ALL), "full census mode coverage")
    checks, reference_hash = k.Findings(), sha256()
    cuts, _, arrivals = k.bare_reference(checks, reference_hash)
    need(not checks.counts and set(arrivals) == set(range(85)), checks.first)

    def predecessor(rank):
        return cuts[(arrivals[rank] - 1) % k.PERIOD]

    def matter(field):
        return field[measure.RECEIVER][:2]

    def launch_hash(field):
        return digest_rows([[v for cell in field for word in cell for v in k.reported(word)]])

    mode = 324
    result, = measure.run(cuts, arrivals, [(mode, mode)], bank.prepare)
    mode_data = census[mode]
    row_hash = digest_rows(sorted(result["rows"]))
    need(row_hash == mode_data["row_sha256"] and len(result["rows"]) == mode_data["events"],
         "mode 324 native event count or digest")
    clocks = (0, 1, 4, 5, 8, 9)
    receipt_counts, changed_slots = Counter(), Counter()
    clock_words, launch_hashes = set(), []
    for rank in range(85):
        bare = predecessor(rank)
        original = bank.stock(bare)
        field, receipt = bank.prepare_info(bare, rank, mode)
        need(receipt == ("bank", 29, 2, 9, 0, 0), ("mode 324 fixed operation", rank, receipt))
        need(all(field[i][k.CORR] == original[i][k.CORR] for i in clocks),
             ("mode 324 original clock words", rank))
        need(k.reported_account(field) == measure.LEDGER, ("mode 324 ledger", rank))
        clock_words.add(tuple(field[i][k.CORR] for i in clocks))
        launch_hashes.append(launch_hash(field))
        receipt_counts[receipt] += 1
        changed_slots.update((site, lane) for site in range(32) for lane in range(4)
                             if field[site][lane] != original[site][lane])
    launch_list_hash = sha256("".join(launch_hashes).encode("ascii")).hexdigest()
    need(launch_list_hash == mode_data["provenance"]["launch_list_sha256"], "mode 324 launch digest")
    need(len(clock_words) == mode_data["provenance"]["distinct_clock_projections"], "clock digest")

    def detail(mode, row, field):
        _, rank, event_tick, ray, *_ = row
        age = row[14]
        conservation = k.account(field)
        digest = sha256()
        live = [(None, field, None)]
        for tick in range(1, event_tick + measure.LOOKAHEAD + 1):
            live.append(measure.step(live[-1][1], tick, conservation, digest, (mode, rank, "live")))
        source_c, source_b, tags = live[event_tick]
        restored, inverse_tag = k.scatter(source_b[measure.SOURCE])
        need(tags[measure.SOURCE] == 2 and (restored, inverse_tag) == (source_c[measure.SOURCE], 1),
             ("source inverse", mode, rank, event_tick))
        branch = (*source_b[:measure.SOURCE], restored, *source_b[measure.SOURCE + 1:])
        need(k.account(branch) == conservation, ("branch account", mode, rank))
        control = [(None, branch, None)]
        for t in range(1, measure.LOOKAHEAD + 1):
            control.append(measure.step(control[-1][1], event_tick + t, conservation, digest,
                                        (mode, rank, "control")))
        actual = live[event_tick:]
        need(tuple(measure.compare(mode, rank, event_tick, actual, control)) == tuple(row),
             ("held event projection", mode, rank, event_tick))
        launch_pair = matter(field)
        written = matter(actual[age][1])
        comparison_written = matter(control[age][1])

        def cut(t, stage, act, cmp=None):
            rec = {"tick": t, "age": t - event_tick, "stage": stage, "actual": measure.encode(act)}
            if cmp is not None:
                rec["control"] = measure.encode(cmp)
            return rec

        first_change = None
        for tick in range(1, event_tick + age + 1):
            for stage, field_at_cut in zip(("C", "B"), live[tick][:2]):
                if (tick, stage) != (event_tick + age, "B") and matter(field_at_cut) != launch_pair:
                    first_change = cut(tick, stage, matter(field_at_cut))
                    break
            if first_change is not None:
                break

        loss, last = {}, None
        for t in range(age + 1, measure.LOOKAHEAD + 1):
            for index, stage in enumerate(("C", "B")):
                a, b = matter(actual[t][index]), matter(control[t][index])
                last = cut(event_tick + t, stage, a, b)
                for label, failed in (
                    ("actual_word", a != written),
                    ("control_word", b != comparison_written),
                    ("paired_values", (a, b) != (written, comparison_written)),
                    ("contrast", a == b),
                ):
                    if failed and label not in loss:
                        loss[label] = last
        return dict(rank=rank, event_tick=event_tick, ray=ray, held_age=age,
                    launch_pair=measure.encode(launch_pair), written_pair=measure.encode(written),
                    control_at_write=measure.encode(comparison_written),
                    actual_C_pair=measure.encode(matter(actual[age][0])),
                    control_C_pair=measure.encode(matter(control[age][0])),
                    written_equals_launch=written == launch_pair,
                    arrival_C_equals_launch=matter(actual[age][0]) == launch_pair,
                    first_prewrite_change_from_launch=first_change,
                    first_loss={name: loss.get(name) for name in
                                ("actual_word", "control_word", "paired_values", "contrast")},
                    last_checked=last)

    groups = {}
    observed_positive_modes = [m for m in sorted(census) if census[m]["counts"]["held"]["events"]]
    for m in observed_positive_modes:
        entry = census[m]
        need(entry["counts"]["held"] == {"events": 1, "ranks": 1}, ("held census count", m))
        row = entry["first_held"]
        _, rank, tick = row[:3]
        need(rank == 43, ("held census rank", m))
        bare = predecessor(rank)
        field, receipt = bank.prepare_info(bare, rank, m)
        stock = bank.stock(bare)
        payer = receipt[1]
        receipt_record = {"mode": m, "funding": receipt, "payer_corr_before": k.reported(stock[payer][3]),
                          "payer_corr_after": k.reported(field[payer][3]),
                          "unchanged_clock_words": all(field[i][3] == stock[i][3] for i in clocks)}
        key = launch_hash(field), rank, tick, row[14]
        hit = detail(m, row, field)
        if key not in groups:
            groups[key] = {"launch_sha256": key[0], "hit": hit, "recipes": []}
        else:
            need(groups[key]["hit"] == hit, ("duplicate launch reproduced different hit", key))
        groups[key]["recipes"].append(receipt_record)

    print(json.dumps({
        "mode324": {
            "ranks": 85, "events": len(result["rows"]), "event_rows_sha256": row_hash,
            "launch_list_sha256": launch_list_hash, "unaltered_clock_ranks": 85,
            "distinct_clock_projections": len(clock_words),
            "funding_receipts": [[list(receipt), count] for receipt, count in receipt_counts.items()],
            "changed_stock_slots": [[site, lane, count] for (site, lane), count in sorted(changed_slots.items())],
        },
        "groups": list(groups.values()),
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
