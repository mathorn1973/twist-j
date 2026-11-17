# SPDX-License-Identifier: Apache-2.0
"""Exact finite audit of a paid horizontal CORR parity bridge."""

from collections import defaultdict
import json

import kernel as k


TARGETS = (44, 4)
HEAD, RECEIVER = k.HEAD, k.PASSIVE
BRIDGE, SUPPORT, MATERIAL_SUPPORT = 29, k.SUPPORT, k.SUPPORT + 1
C, U = k.CLK, k.CORR
Y = k.R0
K_RECEIVER = k.from_j(-2, 0, -1, 0)
U_BRIDGE = k.from_j(3, 4, 4, 8)
K_SUPPORT = k.from_j(0, -1, -1, 0)
R0_SUPPORT = k.from_j(-1, 0, -1, 0)
ORIGINAL = k.from_j(-9, 0, -3, -3)
COMMON = k.from_j(-3, 2, -5, 1)
WRITTEN = k.from_j(-5, 0, -5, 0)
FIXTURES = ("no_bridge", "bridge", "supported", "material_support")
ALL = tuple((site, lane) for site in range(32) for lane in range(4))
RADIATION = tuple((site, lane) for site, lane in ALL if lane >= C)


def stock(field, fixture):
    base = k.Preparation(fixture, K_RECEIVER).stock(field)
    result = list(base)
    if fixture != "no_bridge":
        result[BRIDGE] = (*result[BRIDGE][:U], k.add(result[BRIDGE][U], U_BRIDGE))
    if fixture in ("supported", "material_support"):
        result[SUPPORT] = (*result[SUPPORT][:C], K_SUPPORT, result[SUPPORT][U])
    if fixture == "material_support":
        result[MATERIAL_SUPPORT] = (R0_SUPPORT, *result[MATERIAL_SUPPORT][1:])
    return tuple(result)


def stock_coordinates(fixture):
    positions = k.Preparation(fixture, K_RECEIVER).stock_coordinates()
    if fixture != "no_bridge":
        positions.add((BRIDGE, U))
    if fixture in ("supported", "material_support"):
        positions.add((SUPPORT, C))
    if fixture == "material_support":
        positions.add((MATERIAL_SUPPORT, Y))
    return positions


def mismatch(field, reference, coords):
    return k.mismatch(field, reference, coords)


def receiver_word(field):
    return field[RECEIVER][Y]


def shown(value):
    return k.reported(value)


def gap_norm(cell):
    delta = k.subtract(cell[k.R0], cell[k.R2])
    return shown(k.norm(k.half(delta))) if k.even(delta) else None


def checked_tick(field, bit, account, events, label, digest):
    return k.transition(field, bit, account, events, label, digest)


def cut_checks(field, bare, fixture, projected, bit, reference_bit):
    paid = stock(bare, fixture)
    return {
        "bit_matches": bit == reference_bit,
        "head_K_U_clear": field[HEAD][C:] == paid[HEAD][C:],
        "head_radiation": [shown(x) for x in field[HEAD][C:]],
        "head_target_radiation": [shown(x) for x in paid[HEAD][C:]],
        "head_material": [shown(x) for x in field[HEAD][:C]],
        "head_material_half_gap_norm": gap_norm(field[HEAD]),
        "carrier_mismatch": mismatch(field, bare, projected),
        "unpaid_radiation_mismatch": mismatch(
            field, bare, (pos for pos in projected if pos[1] >= C)
        ),
        "paid_radiation_mismatch": mismatch(field, paid, RADIATION),
        "bare_radiation_mismatch": mismatch(field, bare, RADIATION),
        "paid_carrier_mismatch": mismatch(
            field, paid, (pos for pos in ALL if pos[0] != RECEIVER or pos[1] >= C)
        ),
        "full_paid_mismatch": mismatch(field, paid, ALL),
    }


def contact_trace(prior, transported):
    result = {}
    for name, first, second, lane in (
        ("receiver_CLK", HEAD, RECEIVER, C),
        ("head_CORR", 0, HEAD, U),
        ("receiver_CORR", 1, RECEIVER, U),
    ):
        a, b = prior[first][lane], prior[second][lane]
        result[name] = {
            "inputs": [shown(a), shown(b)],
            "even_difference": k.even(k.subtract(a, b)),
            "outputs": [shown(transported[i][lane]) for i in (first, second)],
        }
    return result


def fresh(fixture, cuts, transported, arrivals, digest):
    events = k.Witnesses()
    projected = tuple(pos for pos in ALL if pos not in stock_coordinates(fixture))
    rows = {}
    expected_account = k.account(stock(cuts[0], fixture))
    end_words = {}
    target_records = {}
    for rank, arrival in sorted(arrivals.items()):
        offset = (arrival - 1) % k.LAP
        field = stock(cuts[offset], fixture)
        account = k.account(field)
        if account != expected_account:
            events.note("fresh_account_varies_with_rank", [rank, k.reported_account(field)])
        bit = offset % 2
        k.trace_cut(digest, field)
        rows[rank] = []
        if rank in TARGETS:
            target_records[rank] = []
        for number in (1, 2, 3, 4):
            idx = (offset + number - 1) % k.LAP
            before = field
            before_word = receiver_word(before)
            after_c, field, tags, bit = checked_tick(
                before, bit, account, events, [rank, number], digest
            )
            c_word, b_word = receiver_word(after_c), receiver_word(field)
            row = [tags[HEAD], tags[RECEIVER], *(shown(word) for word in (before_word, c_word, b_word))]
            rows[rank].append(row)
            target = rank in TARGETS
            record = {"step": number, "tags_and_words": row}
            if target:
                record["C"] = cut_checks(after_c, transported[idx], fixture, projected, 1-bit, idx % 2)
                record["B"] = cut_checks(field, cuts[idx+1], fixture, projected, bit, (idx+1) % 2)
                target_records[rank].append(record)
            active = rank == 4 and fixture != "no_bridge"
            if target and number == 1 and tags[HEAD] != 1:
                events.note("fresh_missing_target_head_B1", [rank, record])
            if target and number == 2:
                expected_word = WRITTEN if active else COMMON
                expected_tags = (2, 2 if active else 0)
                record["work_contacts"] = contact_trace(before, after_c)
                end_words[rank] = shown(b_word)
                if (before_word, c_word, b_word) != (ORIGINAL, COMMON, expected_word):
                    events.note("fresh_target_words", [rank, record])
                if (tags[HEAD], tags[RECEIVER]) != expected_tags:
                    events.note("fresh_target_work_tags", [rank, record])
                if not record["B"]["head_K_U_clear"]:
                    events.note("fresh_target_head_K_U_clear", [rank, record])
                if gap_norm(field[HEAD]) != shown(k.norm(k.D)):
                    events.note("fresh_target_head_gap_norm", [rank, record])
            elif c_word != before_word or b_word != c_word:
                if number <= 2:
                    criterion = "fresh_unsolicited_write"
                elif target:
                    criterion = f"fresh_target_retention_tick_{number}"
                else:
                    criterion = f"fresh_foil_late_write_tick_{number}"
                events.note(criterion, [rank, record])
    distinct = len(set(end_words.values())) == len(TARGETS)
    if distinct != (fixture != "no_bridge"):
        events.note("fresh_word_distinction", end_words)
    return {
        "checks": events.report(),
        "seed_account": k.reported_account(stock(cuts[0], fixture)),
        "target_final_words": end_words,
        "target_words_distinct": distinct,
        "trials": rows,
        "trial_entry_fields": ["head_tag", "receiver_tag", "input_R0", "C_R0", "B_R0"],
        "target_records": target_records,
    }


def stream(fixture, offset, cuts, transported, arrivals, digest):
    events = k.Witnesses()
    projected = tuple(pos for pos in ALL if pos not in stock_coordinates(fixture))
    old_stock = k.Preparation(fixture, K_RECEIVER).stock_coordinates()
    read_projection = tuple(pos for pos in ALL if pos not in old_stock)
    predicates = {
        rank: stock(cuts[(arrivals[rank]-1) % k.LAP], fixture) for rank in TARGETS
    }
    seed = field = stock(cuts[offset], fixture)
    book = k.account(seed)
    seed_bit = bit = offset % 2
    k.trace_cut(digest, field)
    pending = None
    first_postwrite_loss = None
    first_return = None
    first_mismatches = {}
    held, held_phase, held_tick = receiver_word(field), None, 0
    held_net_write = False
    work_events = []
    reads = []
    nominal_misses = []
    words = {rank: {} for rank in TARGETS}
    written = {rank: {} for rank in TARGETS}
    hold_overlap = None
    held_by_phase = defaultdict(dict)
    held_after_write = defaultdict(lambda: defaultdict(dict))
    recovery = []
    pending_recovery = []
    hits = defaultdict(int)
    for tick in range(1, k.HORIZON + 1):
        idx = (offset + tick - 1) % k.LAP
        before = field
        incoming_bit = bit
        before_word = receiver_word(before)
        expected_reads = [rank for rank in TARGETS if (arrivals[rank]-1) % k.LAP == idx]
        candidates = [
            rank for rank, template in predicates.items()
            if bit == 1 and mismatch(before, template, read_projection) is None
        ]
        after_c, field, tags, bit = checked_tick(
            before, bit, book, events, [offset, tick], digest
        )
        qualifying = [rank for rank in candidates if tags[HEAD] == 1]
        if len(qualifying) > 1:
            events.note("ambiguous_phase", [tick, qualifying])
        if qualifying:
            reads.append([tick, qualifying[0]])
        if expected_reads and qualifying != expected_reads:
            nominal_misses.append([tick, expected_reads, qualifying, tags[HEAD]])
        c_word, b_word = receiver_word(after_c), receiver_word(field)
        if pending is not None:
            rank, read_tick = pending
            work = {
                "tick": tick,
                "read_tick": read_tick,
                "rank": rank,
                "head_tag": tags[HEAD],
                "receiver_tag": tags[RECEIVER],
                "receiver_words": [shown(word) for word in (before_word, c_word, b_word)],
                "net_write": b_word != before_word,
                "work_contacts": contact_trace(before, after_c),
                "B": cut_checks(field, cuts[idx+1], fixture, projected, bit, (idx+1) % 2),
            }
            work_events.append(work)
            words[rank].setdefault(b_word, tick)
            if b_word == before_word:
                events.note("qualified_work_without_net_write", [rank, tick])
            else:
                written[rank].setdefault(b_word, tick)
            recovery_record = {"work_tick": tick, "rank": rank}
            recovery.append(recovery_record)
            pending_recovery.append(recovery_record)
            held, held_phase, held_tick = b_word, rank, tick
            held_net_write = b_word != before_word
        else:
            for stage, first, last in (("C", before_word, c_word), ("B", c_word, b_word)):
                if first != last:
                    events.note("unqualified_change", [tick, stage, shown(first), shown(last)])
                if last != held and held_net_write and first_postwrite_loss is None:
                    first_postwrite_loss = {
                        "tick": tick, "stage": stage, "rank": held_phase, "work_tick": held_tick,
                        "work_word": shown(held), "actual": shown(last), "bit": incoming_bit,
                        "receiver_before_C_after_C_after_B": [
                            [shown(x) for x in cut[RECEIVER]] for cut in (before, after_c, field)
                        ], "receiver_branch": tags[RECEIVER],
                    }
                if last != held:
                    events.note("hold_counterexample", [
                        held_tick, held_phase, tick, stage, shown(held), shown(last)
                    ])
        for stage, cut, bare, stage_bit, expected_bit, word in (
            ("C", after_c, transported[idx], incoming_bit, idx % 2, c_word),
            ("B", field, cuts[idx+1], bit, (idx+1) % 2, b_word),
        ):
            if held_phase is not None and (pending is None or stage == "B"):
                record = {"tick": tick, "stage": stage, "work_tick": held_tick,
                          "work_word": shown(held), "net_write": held_net_write}
                phases = held_by_phase[word]
                if hold_overlap is None and any(previous != held_phase for previous in phases):
                    other = next(previous for previous in phases if previous != held_phase)
                    hold_overlap = {"word": shown(word), "cuts": {other: phases[other], held_phase: record}}
                phases.setdefault(held_phase, record)
                if held_net_write:
                    held_after_write[word][held_phase].setdefault(held, record)
            if stage_bit != expected_bit:
                events.note("stream_bit", [tick, stage, stage_bit, expected_bit])
            comparison = cut_checks(cut, bare, fixture, projected, stage_bit, expected_bit)
            for metric, observed in (
                ("carrier", comparison["carrier_mismatch"]),
                ("unpaid_radiation", comparison["unpaid_radiation_mismatch"]),
                ("paid_radiation", comparison["paid_radiation_mismatch"]),
                ("bare_radiation", comparison["bare_radiation_mismatch"]),
                ("paid_carrier", comparison["paid_carrier_mismatch"]),
                ("full_paid", comparison["full_paid_mismatch"]),
            ):
                if observed is not None:
                    hits[metric] += 1
                    first_mismatches.setdefault(metric, [tick, stage, observed])
                else:
                    for record in pending_recovery:
                        if (tick, stage) != (record["work_tick"], "C"):
                            record.setdefault(metric, [tick, stage])
            pending_recovery = [record for record in pending_recovery if len(record) < 8]
        pending = (qualifying[0], tick) if qualifying else None
        if first_return is None and field == seed and bit == seed_bit:
            first_return = tick
    def report_classes(classes):
        return {
            "words": {rank: [[shown(word), tick] for word, tick in entries.items()]
                      for rank, entries in classes.items()},
            "intersection": [shown(word) for word in classes[44] if word in classes[4]],
        }
    result = {
        "offset": offset,
        "ticks": k.HORIZON,
        "first_full_return": first_return,
        "account": k.reported_account(seed),
        "checks": events.report(),
        "qualified_reads": reads,
        "nominal_read_misses": nominal_misses,
        "first_postwrite_loss": first_postwrite_loss,
        "qualified_work": work_events,
        "qualified_read_pending_at_bound": pending,
        "observed_classes": report_classes(words),
        "written_classes": report_classes(written),
        "held_word_overlap": hold_overlap,
        "projection_mismatch_counts": {
            metric: hits[metric] for metric in (
                "carrier", "unpaid_radiation", "paid_radiation",
                "bare_radiation", "paid_carrier", "full_paid",
            )
        },
        "first_projection_mismatches": first_mismatches,
        "recovery_after_work": recovery,
        "held_class_cardinalities": {
            rank: sum(rank in witnesses for witnesses in held_by_phase.values())
            for rank in TARGETS
        },
    }
    return result, (held_by_phase, held_after_write)


def alias_key(word, left, right):
    return (
        max(left["tick"], right["tick"]), min(left["tick"], right["tick"]),
        left["start"], right["start"], left["stage"], right["stage"], word,
    )


def joined_held_classes(streams):
    by_phase = {rank: defaultdict(list) for rank in TARGETS}
    for name, (entries, _) in streams.items():
        for word, witnesses in entries.items():
            for rank, witness in witnesses.items():
                by_phase[rank][word].append({"start": name, **witness})
    shared = by_phase[44].keys() & by_phase[4].keys()
    earliest_key = None
    earliest = None
    for word in shared:
        for left in by_phase[44][word]:
            for right in by_phase[4][word]:
                if left["start"] == right["start"]:
                    continue
                key = alias_key(word, left, right)
                if earliest_key is None or key < earliest_key:
                    earliest_key = key
                    earliest = {"word": shown(word), "cuts": {44: left, 4: right}}
    actual = {rank: defaultdict(list) for rank in TARGETS}
    for name, (_, entries) in streams.items():
        for word, witnesses in entries.items():
            for rank, prior_words in witnesses.items():
                actual[rank][word].extend({"start": name, **witness} for witness in prior_words.values())
    distinct_key, distinct = None, None
    for word in actual[44].keys() & actual[4].keys():
        for left in actual[44][word]:
            for right in actual[4][word]:
                if left["start"] == right["start"] or left["work_word"] == right["work_word"]:
                    continue
                key = alias_key(word, left, right)
                if distinct_key is None or key < distinct_key:
                    distinct_key = key
                    distinct = {"word": shown(word), "cuts": {44: left, 4: right}}
    return {
        "cardinalities": {rank: len(by_phase[rank]) for rank in TARGETS},
        "intersection_cardinality": len(shared),
        "first_cross_start_alias": earliest,
        "first_cross_start_alias_after_distinct_net_writes": distinct,
    }


def main():
    digest = k.sha256()
    bare_events = k.Findings()
    cuts, transported, arrivals = k.bare_reference(bare_events, digest)
    if bare_events.counts:
        raise RuntimeError(f"bare reference checks failed: {bare_events.first}")
    preparations = {}
    for fixture in FIXTURES:
        trials = fresh(fixture, cuts, transported, arrivals, digest)
        streams = {}
        held = {}
        for name, offset in (
            ("raw0", 0),
            ("before_raw44", (arrivals[44]-1) % k.LAP),
            ("before_raw4", (arrivals[4]-1) % k.LAP),
        ):
            streams[name], held[name] = stream(fixture, offset, cuts, transported, arrivals, digest)
        preparations[fixture] = {
            "fresh": trials,
            "streams": streams,
            "joined_held_classes": joined_held_classes(held),
        }
    print(json.dumps({"trace_sha256": digest.hexdigest(), "fixtures": preparations},
                     separators=(",", ":"), sort_keys=True))


if __name__ == "__main__":
    main()
