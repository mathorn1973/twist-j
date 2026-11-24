# SPDX-License-Identifier: Apache-2.0
"""Attribute first-cone CORR transmission to natural A B2 events in #2014."""

from collections import Counter
from hashlib import sha256
import json

import kernel as k
from fixture import stock


WIDTH = 8
A = k.HEIGHT + 3
WINDOW = 128
MAX_LENGTH = 4
LOOKAHEAD = MAX_LENGTH + 1
LENGTHS = tuple(range(1, MAX_LENGTH + 1))
DIRECTIONS = {-1: "west", 1: "east"}
METRICS = (
    "emissions", "donor_contrast", "arrival", "chain_arrival",
    "actual_transport_at_arrival", "control_transport_at_arrival",
    "blocked_actual_only", "all_hops_actual_transport",
    "matter_response", "actual_matter_write", "control_matter_write",
    "radiation_survives_next_C", "radiation_survives_next_B",
    "matter_survives_next_C", "matter_survives_next_B",
    "same_radiation_contrast_next_C", "same_radiation_contrast_next_B",
    "same_matter_pair_next_C", "same_matter_pair_next_B",
    "phase_excess_plus_2", "phase_excess_0", "phase_excess_minus_2",
    "phase_excess_undefined", "arrival_actual_transport_with_matter_response",
    "arrival_actual_transport_with_actual_matter_write",
    "actual_effect_same_matter_pair_next_C", "actual_effect_same_matter_pair_next_B",
    "actual_write_same_matter_pair_next_C", "actual_write_same_matter_pair_next_B",
    "actual_effect_same_radiation_and_matter_next_C",
    "actual_effect_same_radiation_and_matter_next_B",
    "radiation_survives_both_next", "matter_survives_both_next",
    "both_contrasts_survive_both_next", "same_matter_pair_both_next",
    "same_radiation_contrast_both_next", "actual_write_retained_both_next",
    "actual_write_retained_and_distinct_both_next",
    "actual_effect_same_radiation_and_matter_both_next",
)


def check(predicate, *context):
    if not predicate:
        raise AssertionError(context)


def checked_step(field, bit, conserved, digest, label):
    events = k.Witnesses()
    result = k.transition(field, bit, conserved, events, label, digest)
    check(not events.counts, label, events.report())
    return result[:3]


def digest_cut(digest, cut, bit):
    digest.update(bytes((bit,)))
    k.trace_cut(digest, cut)


def local_contact_phase(before, after, donor, target, label):
    gap_before = k.subtract(before[donor][k.CORR], before[target][k.CORR])
    gap_after = k.subtract(after[donor][k.CORR], after[target][k.CORR])
    if gap_before == k.ZERO:
        check(gap_after == k.ZERO, "equal pair changed gap", label)
        return None
    if k.even(gap_before):
        check(gap_after == k.multiply(k.RHO, gap_before), "admitted phase", label)
        return 2
    check(gap_after == gap_before, "refused phase", label)
    return 0


def sample_path(actual, control, source_tick, launch_bit, rank, totals, witnesses):
    source_x, source_y = divmod(A, k.HEIGHT)
    initial_bit = (launch_bit + source_tick) % 2
    direction = 1 if source_x % 2 == initial_bit else -1
    ray = tuple(((source_x + direction * length) % WIDTH) * k.HEIGHT + source_y
                for length in range(MAX_LENGTH + 1))
    side = DIRECTIONS[direction]
    chain = True
    all_actual = True
    for length, donor, target in zip(LENGTHS, ray, ray[1:]):
        label = (rank, source_tick, side, length)
        for offset in range(length):
            for stage in (range(2) if offset else (1,)):
                check(actual[offset][stage][target] == control[offset][stage][target],
                      "recipient differs before first cone", label, offset, stage)
        bit = (initial_bit + length - 1) % 2
        leading_x = (donor if direction == 1 else target) // k.HEIGHT
        check(leading_x % 2 == bit, "ray edge mismatched", label)

        real_pre, comp_pre = actual[length - 1][1], control[length - 1][1]
        real_c, real_b, real_tags = actual[length]
        comp_c, comp_b, comp_tags = control[length]
        donor_contrast = real_pre[donor][k.CORR] != comp_pre[donor][k.CORR]
        radiation = k.subtract(real_c[target][k.CORR], comp_c[target][k.CORR])
        arrival = radiation != k.ZERO
        check(not arrival or donor_contrast, "local contrast lacks donor", label)
        check(real_c[target][:k.CORR] == comp_c[target][:k.CORR],
              "non-CORR first arrival on horizontal ray", label)
        real_motion = real_c[target][k.CORR] != real_pre[target][k.CORR]
        comp_motion = comp_c[target][k.CORR] != comp_pre[target][k.CORR]
        matter_pair = real_b[target][:k.CLK], comp_b[target][:k.CLK]
        matter = matter_pair[0] != matter_pair[1]
        check(not matter or arrival, "matter response lacks CORR contrast", label)
        actual_effect = real_motion and matter
        actual_matter_write = matter and matter_pair[0] != real_c[target][:k.CLK]
        actual_write = real_motion and actual_matter_write
        chain = chain and donor_contrast and arrival
        check(not arrival or chain, "arrival lacks complete causal chain", label)
        all_actual = all_actual and real_motion
        count = totals[side][length]
        for metric, flag in (
            ("emissions", True), ("donor_contrast", donor_contrast),
            ("arrival", arrival), ("chain_arrival", chain),
            ("actual_transport_at_arrival", arrival and real_motion),
            ("control_transport_at_arrival", arrival and comp_motion),
            ("blocked_actual_only", arrival and not real_motion and comp_motion),
            ("all_hops_actual_transport", chain and all_actual),
            ("matter_response", matter),
            ("actual_matter_write", actual_matter_write),
            ("arrival_actual_transport_with_matter_response", actual_effect),
            ("arrival_actual_transport_with_actual_matter_write", actual_write),
            ("control_matter_write", matter and matter_pair[1] != comp_c[target][:k.CLK]),
        ):
            count[metric] += int(flag)
        if arrival:
            sectors_real = local_contact_phase(real_pre, real_c, donor, target, label)
            sectors_control = local_contact_phase(comp_pre, comp_c, donor, target, label)
            excess = (None if sectors_real is None or sectors_control is None
                      else sectors_real - sectors_control)
            phase_metric = {
                2: "phase_excess_plus_2", 0: "phase_excess_0",
                -2: "phase_excess_minus_2", None: "phase_excess_undefined",
            }[excess]
            count[phase_metric] += 1
            witnesses[side][length].setdefault(phase_metric, dict(
                rank=rank, source_tick=source_tick, target=target,
                sectors=[sectors_real, sectors_control],
            ))
            first = witnesses[side][length].setdefault("arrival", {})
            if not first:
                first.update(
                    rank=rank, source_tick=source_tick, target=target,
                    pair_pre_C=[[k.reported(field[site][k.CORR]) for site in (donor, target)]
                                for field in (real_pre, comp_pre)],
                    recipient_C=[k.reported(field[target][k.CORR])
                                 for field in (real_c, comp_c)],
                    tags_B=[real_tags[target], comp_tags[target]],
                )
        if matter:
            witnesses[side][length].setdefault("matter_response", dict(
                rank=rank, source_tick=source_tick, target=target,
                matter_B=[list(map(k.reported, pair)) for pair in matter_pair],
                tags_B=[real_tags[target], comp_tags[target]],
            ))
        next_radiation_contrasts, next_matter_pairs = [], []
        for stage, stage_index in (("C", 0), ("B", 1)):
            real = actual[length + 1][stage_index][target]
            comp = control[length + 1][stage_index][target]
            next_radiation = k.subtract(real[k.CORR], comp[k.CORR])
            next_matter_pair = real[:k.CLK], comp[:k.CLK]
            next_radiation_contrasts.append(next_radiation)
            next_matter_pairs.append(next_matter_pair)
            count[f"radiation_survives_next_{stage}"] += int(
                arrival and next_radiation != k.ZERO)
            count[f"matter_survives_next_{stage}"] += int(
                matter and next_matter_pair[0] != next_matter_pair[1])
            count[f"same_radiation_contrast_next_{stage}"] += int(
                arrival and next_radiation == radiation)
            count[f"same_matter_pair_next_{stage}"] += int(
                matter and next_matter_pair == matter_pair)
            same_matter_pair = next_matter_pair == matter_pair
            count[f"actual_effect_same_matter_pair_next_{stage}"] += int(
                actual_effect and same_matter_pair)
            count[f"actual_write_same_matter_pair_next_{stage}"] += int(
                actual_write and same_matter_pair)
            count[f"actual_effect_same_radiation_and_matter_next_{stage}"] += int(
                actual_effect and same_matter_pair and next_radiation == radiation)
        radiation_both = arrival and all(contrast != k.ZERO
                                        for contrast in next_radiation_contrasts)
        matter_both = matter and all(real != comp for real, comp in next_matter_pairs)
        same_radiation_both = arrival and all(contrast == radiation
                                             for contrast in next_radiation_contrasts)
        same_matter_both = matter and all(pair == matter_pair for pair in next_matter_pairs)
        actual_retained_both = actual_matter_write and all(
            next_actual == matter_pair[0] for next_actual, _ in next_matter_pairs)
        for metric, flag in (
            ("radiation_survives_both_next", radiation_both),
            ("matter_survives_both_next", matter_both),
            ("both_contrasts_survive_both_next", radiation_both and matter_both),
            ("same_matter_pair_both_next", same_matter_both),
            ("same_radiation_contrast_both_next", same_radiation_both),
            ("actual_write_retained_both_next", actual_retained_both),
            ("actual_write_retained_and_distinct_both_next", actual_retained_both and matter_both),
            ("actual_effect_same_radiation_and_matter_both_next",
             actual_effect and same_radiation_both and same_matter_both),
        ):
            count[metric] += int(flag)


def new_totals():
    return {side: {length: Counter(dict.fromkeys(METRICS, 0)) for length in LENGTHS}
            for side in DIRECTIONS.values()}


def rank_trial(bare, rank, witnesses, initial_bit=1):
    field = stock(bare, distance=0, sign=0)
    conserved = k.account(field)
    check(k.reported_account(field) == (
        (-9, 2, -2, -3), (19, 7, 5, 19), (463, 0, 152, 152), 774,
    ), "published ingress account", rank)
    actual_digest, control_digest = sha256(), sha256()
    digest_cut(actual_digest, field, initial_bit)
    actual = [(None, field, None)]
    for tick in range(1, WINDOW + LOOKAHEAD + 1):
        cuts = checked_step(field, (initial_bit + tick - 1) % 2, conserved, actual_digest,
                            [rank, "actual", tick])
        actual.append(cuts)
        field = cuts[1]
    totals = new_totals()
    emission_ticks = []
    for tick in range(1, WINDOW + 1):
        emitted_c, emitted_b, tags = actual[tick]
        if tags[A] != 2:
            continue
        emission_ticks.append(tick)
        comparison = list(emitted_b)
        comparison[A] = emitted_c[A]
        field = tuple(comparison)
        check(k.account(field) == conserved, "branch account", rank, tick)
        check(k.scatter(field[A]) == (emitted_b[A], 2),
              "source restoration is not precisely undoing B2", rank, tick)
        check(field[A][k.CORR] != emitted_b[A][k.CORR],
              "source B2 changed no CORR", rank, tick)
        control_digest.update(tick.to_bytes(2, "big"))
        digest_cut(control_digest, field, (initial_bit + tick) % 2)
        control = [(None, field, None)]
        for age in range(1, LOOKAHEAD + 1):
            cuts = checked_step(field, (initial_bit + tick + age - 1) % 2, conserved,
                                control_digest, [rank, "control", tick, age])
            control.append(cuts)
            field = cuts[1]
        sample_path(actual[tick:tick + LOOKAHEAD + 1], control, tick, initial_bit, rank,
                    totals, witnesses)
    return dict(
        rank=rank, account=k.reported_account(actual[0][1]),
        emission_ticks=emission_ticks, repeat_count=max(0, len(emission_ticks) - 1),
        directions=totals,
        actual_sha256=actual_digest.hexdigest(),
        control_sha256=control_digest.hexdigest(),
    )


def run(cuts, arrivals):
    check(set(arrivals) == set(range(85)), "ready fixture ranks")
    offsets = {rank: (arrival - 1) % k.PERIOD for rank, arrival in arrivals.items()}
    check(all(offset % 2 == 1 for offset in offsets.values()), "native predecessor bit")
    witnesses = {side: {length: {} for length in LENGTHS} for side in DIRECTIONS.values()}
    ranks = [rank_trial(cuts[offsets[rank]], rank, witnesses) for rank in sorted(offsets)]
    totals = new_totals()
    for result in ranks:
        for side, lengths in result["directions"].items():
            for length, counts in lengths.items():
                totals[side][length].update(counts)
    summary = {length: sum((totals[side][length] for side in DIRECTIONS.values()),
                           Counter()) for length in LENGTHS}
    return dict(
        window=WINDOW, lookahead=LOOKAHEAD, input_count=len(ranks),
        emission_count=sum(len(result["emission_ticks"]) for result in ranks),
        emitting_inputs=sum(bool(result["emission_ticks"]) for result in ranks),
        repeating_inputs=sum(bool(result["repeat_count"]) for result in ranks),
        repeated_emissions=sum(result["repeat_count"] for result in ranks),
        lengths=LENGTHS, pooled=summary, directions=totals, first=witnesses,
        phase=dict(unit="fifth-turn sectors", sign="actual minus control",
                   scope="local ordered incoming CORR edge at arrival only",
                   undefined="zero donor-receiver gap in either arm"),
        ranks=ranks,
    )


if __name__ == "__main__":
    findings, digest = k.Findings(), sha256()
    cuts, _, arrivals = k.bare_reference(findings, digest)
    check(not findings.counts, "bare reference", findings.counts)
    print(json.dumps(run(cuts, arrivals), sort_keys=True, separators=(",", ":")))
