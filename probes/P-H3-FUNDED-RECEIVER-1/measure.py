# SPDX-License-Identifier: Apache-2.0
"""Exact paired measurement of natural B2 events at the fixed two-edge receiver."""

from hashlib import sha256

import kernel as k

SOURCE, RECEIVER = 7, 31
LAUNCH_BIT = 1
WINDOW, HORIZON, LOOKAHEAD = 128, 64, 65
LEDGER = ((-9, 2, -2, -3), (19, 7, 5, 19), (463, 0, 152, 152), 774)
HEADER = (
    "mode rank tick ray first_any_age first_any_stage first_corr_age "
    "first_isolated_age first_work_age work_actual_tag work_control_tag "
    "survival actual_hold pair_hold held_age held_actual_tag held_control_tag"
).split()


def require(ok, label, *context):
    if not ok:
        raise AssertionError((label, *context))


def bit_at(tick):
    return (LAUNCH_BIT + tick - 1) % 2


def horizontal_partner(site, bit):
    x, y = divmod(site, k.HEIGHT)
    delta = 1 if x % 2 == bit else -1
    return ((x + delta) % 8) * k.HEIGHT + y, delta


def encode(cell):
    return [k.j_coefficients(word) for word in cell]


def cut_digest(digest, field, bit):
    digest.update(bytes((bit,)))
    k.trace_cut(digest, field)


def step(field, tick, conserved, digest, context):
    bit = bit_at(tick)
    events = k.Witnesses()
    post_c, post_b, tags, next_bit = k.transition(
        field, bit, conserved, events, [*context, tick], digest
    )
    require(not events.counts, "native transition", context, tick, events.report())
    require(next_bit == bit_at(tick + 1), "matching bit", context, tick, next_bit)
    return post_c, post_b, tags


def witness(actual, control, tick, age, ray):
    arriving_tick = tick + age
    donor, recipient_outward = horizontal_partner(RECEIVER, bit_at(arriving_tick))
    next_donor, _ = horizontal_partner(RECEIVER, bit_at(arriving_tick + 1))
    source = {
        "C": encode(actual[0][0][SOURCE]),
        "B": encode(actual[0][1][SOURCE]),
        "control_B": encode(control[0][1][SOURCE]),
        "actual_tag": actual[0][2][SOURCE],
        "inverse_tag": k.scatter(actual[0][1][SOURCE])[1],
        "C_bit": bit_at(tick),
        "next_bit": bit_at(tick + 1),
        "outgoing_partner": horizontal_partner(SOURCE, bit_at(tick + 1))[0],
        "outgoing_ray": ray,
    }

    def arm(cuts):
        return {
            "pre_C": encode(cuts[age - 1][1][RECEIVER]),
            "C": encode(cuts[age][0][RECEIVER]),
            "B": encode(cuts[age][1][RECEIVER]),
            "tag": cuts[age][2][RECEIVER],
            "next_C": encode(cuts[age + 1][0][RECEIVER]),
            "next_B": encode(cuts[age + 1][1][RECEIVER]),
            "next_tag": cuts[age + 1][2][RECEIVER],
            "donor_pre_C": encode(cuts[age - 1][1][donor]),
            "donor_C": encode(cuts[age][0][donor]),
            "next_donor_pre_C": encode(cuts[age][1][next_donor]),
        }

    return {
        "tick": tick, "age": age, "recipient_tick": arriving_tick,
        "source": source, "recipient": RECEIVER, "donor": donor,
        "next_donor": next_donor, "incoming_direction": -recipient_outward,
        "arrival_C_bit": bit_at(arriving_tick), "actual": arm(actual),
        "control": arm(control),
    }


def compare(mode, rank, tick, actual, control):
    ray = horizontal_partner(SOURCE, bit_at(tick + 1))[1]
    first_any_age = first_any_stage = first_corr_age = first_isolated_age = 0
    first_work_age = work_actual_tag = work_control_tag = 0
    held_age = held_actual_tag = held_control_tag = 0
    survival = actual_hold = pair_hold = 0
    for age in range(1, HORIZON + 1):
        ac, ab, at = actual[age]
        cc, cb, ct = control[age]
        rc, rb, sc, sb = ac[RECEIVER], ab[RECEIVER], cc[RECEIVER], cb[RECEIVER]
        corr = rc[k.CORR] != sc[k.CORR]
        clean = corr and rc[:k.CORR] == sc[:k.CORR]
        if not first_any_age:
            if rc != sc:
                first_any_age, first_any_stage = age, 1
                require(age >= 2, "change before two-edge cone", mode, rank, tick, age)
                ap, cp = actual[age - 1][1], control[age - 1][1]
                donor = horizontal_partner(RECEIVER, bit_at(tick + age))[0]
                if clean and ap[RECEIVER] == cp[RECEIVER] and ap[donor][k.CORR] != cp[donor][k.CORR]:
                    first_isolated_age = age
            elif rb != sb:
                first_any_age, first_any_stage = age, 2
                require(age >= 2, "change before two-edge cone", mode, rank, tick, age)
        if corr and not first_corr_age:
            first_corr_age = age
        actual_matter, control_matter = rb[:2], sb[:2]
        if clean and actual_matter != rc[:2] and actual_matter != control_matter:
            actual_next = [field[RECEIVER][:2] for field in actual[age + 1][:2]]
            control_next = [field[RECEIVER][:2] for field in control[age + 1][:2]]
            remains = all(a != c for a, c in zip(actual_next, control_next))
            holds = all(a == actual_matter for a in actual_next)
            both_hold = holds and all(c == control_matter for c in control_next)
            if not first_work_age:
                first_work_age, work_actual_tag, work_control_tag = age, at[RECEIVER], ct[RECEIVER]
                survival, actual_hold, pair_hold = map(int, (remains, holds, both_hold))
            if not held_age and remains and holds:
                held_age, held_actual_tag, held_control_tag = age, at[RECEIVER], ct[RECEIVER]
    projection = (
        mode, rank, tick, ray, first_any_age, first_any_stage, first_corr_age,
        first_isolated_age, first_work_age, work_actual_tag, work_control_tag,
        survival, actual_hold, pair_hold, held_age, held_actual_tag, held_control_tag,
    )
    return projection


def rank_trial(bare, rank, mode, recipe, prepare, reports):
    field = prepare(bare, rank, recipe)
    require(k.reported_account(field) == LEDGER, "launch Q774 ledger", mode, rank)
    conserved = k.account(field)
    live_hash, control_hash = sha256(), sha256()
    cut_digest(live_hash, field, LAUNCH_BIT)
    live = [(None, field, None)]
    for tick in range(1, WINDOW + LOOKAHEAD + 1):
        live.append(step(live[-1][1], tick, conserved, live_hash, (mode, rank, "actual")))

    emission_ticks, rows = [], []
    for tick in range(1, WINDOW + 1):
        source_c, source_b, tags = live[tick]
        if tags[SOURCE] != 2:
            continue
        emission_ticks.append(tick)
        restored, inverse_tag = k.scatter(source_b[SOURCE])
        require((restored, inverse_tag) == (source_c[SOURCE], 1), "independent source inverse",
                mode, rank, tick)
        require(k.scatter(restored) == (source_b[SOURCE], 2), "source re-emission", mode, rank, tick)
        require(restored[k.CORR] != source_b[SOURCE][k.CORR], "source CORR write", mode, rank, tick)
        branch = (*source_b[:SOURCE], restored, *source_b[SOURCE + 1:])
        require(k.account(branch) == conserved, "source undo ledger", mode, rank, tick)
        control_hash.update(tick.to_bytes(2, "big"))
        cut_digest(control_hash, branch, bit_at(tick + 1))
        control = [(None, branch, None)]
        for age in range(1, LOOKAHEAD + 1):
            control.append(step(control[-1][1], tick + age, conserved, control_hash,
                                (mode, rank, "control", tick)))

        actual = live[tick:tick + LOOKAHEAD + 1]
        row = compare(mode, rank, tick, actual, control)
        rows.append(row)
        ray, first_corr_age, first_work_age, held_age = row[3], row[6], row[8], row[14]
        for key, age in (("first_work", first_work_age), ("first_held", held_age)):
            if age and reports[key] is None:
                reports[key] = {"rank": rank, **witness(actual, control, tick, age, ray)}
        if rank == 0 and tick == 81:
            raw_detail_ages = sorted({10, *(age for age in (first_corr_age, first_work_age, held_age) if age)})
            reports["raw0_tick81"] = [
                {"rank": rank, **witness(actual, control, tick, age, ray)}
                for age in raw_detail_ages
            ]

    record = {
        "rank": rank,
        "launch_ledger": LEDGER,
        "emission_ticks": emission_ticks,
        "event_count": len(emission_ticks),
        "actual_sha256": live_hash.hexdigest(),
        "control_sha256": control_hash.hexdigest(),
    }
    return rows, record


def run(cuts, arrivals, modes, prepare):
    require(set(arrivals) == set(range(85)), "ready fixture ranks")
    offsets = {rank: (arrival - 1) % k.PERIOD for rank, arrival in arrivals.items()}
    require(all(offset % 2 == LAUNCH_BIT for offset in offsets.values()), "launch bits")
    reports = []
    for mode, recipe in modes:
        report = {
            "mode": mode, "rows": [], "rank_records": [],
            "first_work": None, "first_held": None, "raw0_tick81": None,
        }
        for rank, offset in sorted(offsets.items()):
            rows, record = rank_trial(cuts[offset], rank, mode, recipe, prepare, report)
            report["rows"].extend(rows)
            report["rank_records"].append(record)
        reports.append(report)
    return reports


def event_witness(bare, rank, mode, prepare, event_tick, event_age):
    """Replay one nominated row to expose both local cuts and the source undo."""
    field = prepare(bare, rank, mode)
    conserved, digest = k.account(field), sha256()
    live = [(None, field, None)]
    for tick in range(1, event_tick + event_age + 2):
        live.append(step(live[-1][1], tick, conserved, digest, (mode, rank, "witness")))
    source_c, source_b, tags = live[event_tick]
    require(tags[SOURCE] == 2, "source B2", mode, rank, event_tick)
    branch = list(source_b)
    branch[SOURCE] = source_c[SOURCE]
    control = [(None, tuple(branch), None)]
    for age in range(1, event_age+2):
        control.append(step(control[-1][1], event_tick+age, conserved, digest,
                            (mode, rank, "witness control")))
    ray = horizontal_partner(SOURCE,bit_at(event_tick+1))[1]
    return {"rank": rank, **witness(live[event_tick:],control,event_tick,event_age,ray)}
