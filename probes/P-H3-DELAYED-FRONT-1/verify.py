# SPDX-License-Identifier: Apache-2.0
"""Audit delayed local CORR contrasts following natural A B2 events."""

from collections import Counter
from hashlib import sha256
import json

import kernel as k
from fixture import stock
from source import A, DIRECTIONS, LENGTHS, WIDTH, WINDOW
from source import check, checked_step, digest_cut, local_contact_phase


HORIZON = 64
LOOKAHEAD = HORIZON + 1
LAUNCH_BIT = 1


def word_delta(real, control, lane):
    return k.subtract(real[lane], control[lane])


def first_cuts(actual, control, target):
    first_any, first_corr = None, None
    for age in range(1, HORIZON + 1):
        for stage, index in (("C", 0), ("B", 1)):
            real, comp = actual[age][index][target], control[age][index][target]
            if first_any is None and real != comp:
                first_any = dict(age=age, stage=stage,
                                 lanes=[lane for lane in range(4) if real[lane] != comp[lane]])
            if stage == "C" and real[k.CORR] != comp[k.CORR]:
                first_corr = age
                return first_any, first_corr
    return first_any, first_corr


def identify_arrival(actual, control, target, age, emission_bit, direction, first_any, label):
    bit = (emission_bit + age - 1) % 2
    x, y = divmod(target, k.HEIGHT)
    donor_to_target = -1 if x % 2 == bit else 1
    donor = ((x - donor_to_target) % WIDTH) * k.HEIGHT + y
    before_real, before_comp = actual[age - 1][1], control[age - 1][1]
    real_c, real_b, tags_real = actual[age]
    comp_c, comp_b, tags_comp = control[age]
    recipient_pre_equal = before_real[target] == before_comp[target]
    donor_contrast = before_real[donor][k.CORR] != before_comp[donor][k.CORR]
    other_lanes_equal = real_c[target][:k.CORR] == comp_c[target][:k.CORR]
    isolated = (first_any["age"] == age and first_any["stage"] == "C"
                and recipient_pre_equal and donor_contrast and other_lanes_equal)
    real_moved = real_c[target][k.CORR] != before_real[target][k.CORR]
    comp_moved = comp_c[target][k.CORR] != before_comp[target][k.CORR]
    sectors = None
    excess = None
    if isolated:
        sectors = [local_contact_phase(before_real, real_c, donor, target, label),
                   local_contact_phase(before_comp, comp_c, donor, target, label)]
        if all(sector is not None for sector in sectors):
            excess = sectors[0] - sectors[1]
            check(excess in (-2, 0, 2), "invalid phase excess", label)

    matter_pair = real_b[target][:k.CLK], comp_b[target][:k.CLK]
    matter_contrast = matter_pair[0] != matter_pair[1]
    real_write = matter_pair[0] != real_c[target][:k.CLK]
    comp_write = matter_pair[1] != comp_c[target][:k.CLK]
    corr_contrast = word_delta(real_c[target], comp_c[target], k.CORR)
    field_pair = real_c[target][k.CLK:], comp_c[target][k.CLK:]
    next_cuts = []
    for stage_index in (0, 1):
        real_next = actual[age + 1][stage_index][target]
        comp_next = control[age + 1][stage_index][target]
        corr_next = word_delta(real_next, comp_next, k.CORR)
        matter_next = real_next[:k.CLK], comp_next[:k.CLK]
        field_next = real_next[k.CLK:], comp_next[k.CLK:]
        next_cuts.append(dict(
            corr_contrast=corr_next != k.ZERO,
            matter_contrast=matter_contrast and matter_next[0] != matter_next[1],
            field_contrast=field_next[0] != field_next[1],
            same_corr_contrast=corr_next == corr_contrast,
            same_field_pair=field_next == field_pair,
            same_matter_pair=matter_contrast and matter_next == matter_pair,
            retained_actual_write=real_write and matter_next[0] == matter_pair[0],
            retained_control_write=comp_write and matter_next[1] == matter_pair[1],
        ))
    return dict(
        age=age, bit=bit, donor=donor, incoming=DIRECTIONS[donor_to_target],
        orientation="original" if donor_to_target == direction else "reflected",
        isolated=isolated, recipient_pre_equal=recipient_pre_equal,
        donor_contrast=donor_contrast, other_lanes_equal=other_lanes_equal,
        actual_move=real_moved, control_move=comp_moved,
        suppression=isolated and not real_moved and comp_moved,
        actual_write=real_write, control_write=comp_write,
        matter_contrast=matter_contrast,
        tags=[tags_real[target], tags_comp[target]], sectors=sectors, excess=excess,
        corr_pre=[[k.reported(field[site][k.CORR]) for site in (donor, target)]
                  for field in (before_real, before_comp)],
        corr_C=[k.reported(field[target][k.CORR]) for field in (real_c, comp_c)],
        matter_B=[list(map(k.reported, pair)) for pair in matter_pair],
        next_C=next_cuts[0], next_B=next_cuts[1],
    )


def event_rows(actual, control, rank, tick):
    emission_bit = (LAUNCH_BIT + tick) % 2
    x, y = divmod(A, k.HEIGHT)
    direction = 1 if x % 2 == emission_bit else -1
    for length in LENGTHS:
        target = ((x + direction * length) % WIDTH) * k.HEIGHT + y
        label = (rank, tick, length)
        first_any, age = first_cuts(actual, control, target)
        check(first_any is None or first_any["age"] >= length, "early local contrast", label)
        row = dict(rank=rank, tick=tick, length=length, target=target,
                   ray=DIRECTIONS[direction], first_any=first_any, first_corr=None)
        if age is not None:
            row["first_corr"] = identify_arrival(
                actual, control, target, age, emission_bit, direction, first_any, label)
        yield row


def rank_trial(bare, rank):
    field = stock(bare, distance=0, sign=0)
    account = k.account(field)
    check(k.reported_account(field) == (
        (-9, 2, -2, -3), (19, 7, 5, 19), (463, 0, 152, 152), 774,
    ), "published ingress account", rank)
    live_hash, branch_hash = sha256(), sha256()
    digest_cut(live_hash, field, LAUNCH_BIT)
    live = [(None, field, None)]
    for tick in range(1, WINDOW + LOOKAHEAD + 1):
        bit = (LAUNCH_BIT + tick - 1) % 2
        cuts = checked_step(field, bit, account, live_hash, [rank, "actual", tick])
        live.append(cuts)
        field = cuts[1]
    rows, emission_ticks = [], []
    for tick in range(1, WINDOW + 1):
        source_c, source_b, tags = live[tick]
        if tags[A] != 2:
            continue
        emission_ticks.append(tick)
        branch = list(source_b)
        branch[A] = source_c[A]
        field = tuple(branch)
        check(k.account(field) == account, "branch account", rank, tick)
        check(k.scatter(field[A]) == (source_b[A], 2), "source restoration", rank, tick)
        check(field[A][k.CORR] != source_b[A][k.CORR], "source CORR unchanged", rank, tick)
        branch_hash.update(tick.to_bytes(2, "big"))
        digest_cut(branch_hash, field, (LAUNCH_BIT + tick) % 2)
        control = [(None, field, None)]
        for age in range(1, LOOKAHEAD + 1):
            bit = (LAUNCH_BIT + tick + age - 1) % 2
            cuts = checked_step(field, bit, account, branch_hash, [rank, "control", tick, age])
            control.append(cuts)
            field = cuts[1]
        rows.extend(event_rows(live[tick:tick + LOOKAHEAD + 1], control, rank, tick))
    return rows, dict(rank=rank, emission_ticks=emission_ticks,
                      actual_sha256=live_hash.hexdigest(), control_sha256=branch_hash.hexdigest())


def summarize(rows):
    pools, witness = {}, {}
    for row in rows:
        for side in ("pooled", row["ray"]):
            length = row["length"]
            counts = pools.setdefault(side, {}).setdefault(length, Counter())
            counts["events"] += 1
            counts["any_lane"] += int(row["first_any"] is not None)
            arrival = row["first_corr"]
            if arrival is None:
                continue
            counts["first_corr_C"] += 1
            counts["first_corr_at_cone"] += int(arrival["age"] == length)
            counts["first_corr_after_cone"] += int(arrival["age"] > length)
            for metric in ("isolated", "actual_move", "control_move", "suppression",
                           "actual_write", "control_write", "matter_contrast"):
                counts[metric] += int(arrival[metric])
                if arrival["isolated"]:
                    counts[f"isolated_{metric}"] += int(arrival[metric])
            if arrival["isolated"]:
                excess = arrival["excess"]
                phase = "undefined" if excess is None else f"{excess:+d}"
                counts[f"isolated_phase_{phase}"] += 1
                counts[f"isolated_orientation_{arrival['orientation']}"] += 1
            for metric, at_c in arrival["next_C"].items():
                at_b = arrival["next_B"][metric]
                for stage, observed in (("C", at_c), ("B", at_b), ("both", at_c and at_b)):
                    counts[f"{metric}_next_{stage}"] += int(observed)
                    if arrival["isolated"]:
                        counts[f"isolated_{metric}_next_{stage}"] += int(observed)
            found = witness.setdefault(side, {}).setdefault(length, {})
            found.setdefault("first_corr_C", row)
            if arrival["isolated"]:
                found.setdefault("isolated", row)
                if arrival["actual_move"]:
                    found.setdefault("isolated_actual_move", row)
                if arrival["suppression"]:
                    found.setdefault("suppression", row)
    return pools, witness


def run(cuts, arrivals):
    check(set(arrivals) == set(range(85)), "ready fixture ranks")
    offsets = {rank: (arrival - 1) % k.PERIOD for rank, arrival in arrivals.items()}
    check(all(offset % 2 == LAUNCH_BIT for offset in offsets.values()), "predecessor bit")
    rows, ranks = [], []
    for rank in sorted(offsets):
        events, record = rank_trial(cuts[offsets[rank]], rank)
        rows.extend(events)
        ranks.append(record)
    pooled, witness = summarize(rows)
    summary = dict(
        input_count=len(ranks), window=WINDOW, horizon=HORIZON, lookahead=LOOKAHEAD,
        input_ticks=len(ranks) * WINDOW,
        emission_count=sum(len(row["emission_ticks"]) for row in ranks),
        emitting_inputs=sum(bool(row["emission_ticks"]) for row in ranks),
        repeating_inputs=sum(len(row["emission_ticks"]) > 1 for row in ranks),
        scope="local first CORR contrast at a fixed outward target; no delayed path attribution",
        pools=pooled, witness=witness,
    )
    return summary, ranks, rows


def emit(section, value):
    print(json.dumps(dict(section=section, value=value), sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    findings, digest = k.Findings(), sha256()
    cuts, _, arrivals = k.bare_reference(findings, digest)
    check(not findings.counts, "bare reference", findings.counts)
    summary, ranks, rows = run(cuts, arrivals)
    cohort = [[r["rank"], r["emission_ticks"]] for r in ranks]
    cohort_hash = sha256(json.dumps(cohort, separators=(",", ":")).encode("ascii")).hexdigest()
    check(cohort_hash == "ec9ff8309aeb377df8d432c09b9d0227af3ec8ab0c703b5cb9c94460735eaf7a",
          "mismatch against preceding rank-to-emission list", cohort_hash)
    at_front = [summary["pools"]["pooled"][d]["first_corr_at_cone"] for d in LENGTHS]
    check(at_front == [4, 0, 0, 0], "preceding front counts", at_front)
    summary["cohort_sha256"] = cohort_hash
    summary["bare_sha256"] = digest.hexdigest()
    emit("summary", summary)
    for rank in ranks:
        emit("rank", rank)
    for row in rows:
        emit("event_distance", row)
