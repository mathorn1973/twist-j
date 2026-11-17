# SPDX-License-Identifier: Apache-2.0
"""Exact L1 trial census and stream audit for five H3 preparations."""
from collections import Counter
import json

import kernel as k


H, RX, S, A, AUX = (4, 5, 6, 7, 11)
BRIDGE = 29
R0, R2, CLK, U = k.R0, k.R2, k.CLK, k.CORR
FIXTURES = ("baseline", "ingress_active", "ingress_sham", "delayed_active", "delayed_sham")
TARGETS = (44, 4)
POSITIONS = tuple((site, lane) for site in range(32) for lane in range(4))
PREP = k.Preparation("Q725", k.from_j(-2, 0, -1, 0), k.from_j(0, -1, -1, 0))
MASKED = {(site, lane) for site in (H, RX) for lane in (R0, R2, CLK)}
READ = tuple(pos for pos in POSITIONS if pos not in MASKED)
INTERVALS = ((3, 7), (8, 12), (13, 17), (18, 22), (23, 24))
DETAIL_TICKS = (1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 18, 19, 20)
SITES = (A, H, S, RX)
UPPER_EDGES = ((H, RX), (S, A), (RX, S), (A, H))


def stock(bare, fixture):
    field = [list(cell) for cell in PREP.stock(bare)]
    field[BRIDGE][U] = k.add(field[BRIDGE][U], k.from_j(3, 4, 4, 8))
    field[A][R0] = k.from_j(-1, 0, -1, 0)
    if fixture.startswith("ingress"):
        sign = 1 if fixture == "ingress_active" else -1
        field[A][R2] = k.add(field[A][R2], k.scale(sign, k.from_j(4, 2, 3, 1)))
        for site in (A, AUX):
            field[site][U] = k.add(field[site][U], k.from_j(0, -2, -2, 0))
    if fixture.startswith("delayed"):
        sign = 1 if fixture == "delayed_active" else -1
        field[S][R0] = k.add(field[S][R0], k.scale(sign, k.from_j(3, -1, -1, 1)))
    return tuple(map(tuple, field))


def show(word):
    return k.reported(word)


def pair_detail(before, after_c, left, right, lane):
    a, b = (before[site][lane] for site in (left, right))
    return [left, right, lane, k.even(k.subtract(a, b)),
            [show(a), show(b)], [show(after_c[site][lane]) for site in (left, right)]]


def detail(before, after_c, after_b, tags, bit):
    vertically_matched = UPPER_EDGES[2 * bit:2 * bit + 2]
    vertical = [
        pair_detail(before, after_c, left, right, lane)
        for left, right in vertically_matched for lane in (R0, R2)
    ]
    horizontal = []
    for site in SITES:
        x, y = divmod(site, 4)
        start = (x - 1) % 8 if x % 2 != bit else x
        left, right = start * 4 + y, ((start + 1) % 8) * 4 + y
        if site == A or (before[site][U] != after_c[site][U]):
            horizontal.append(pair_detail(before, after_c, left, right, U))
    collisions = {
        site: [tags[site], [show(w) for w in after_c[site]], [show(w) for w in after_b[site]]]
        for site in SITES if tags[site]
    }
    return [bit, vertical, horizontal, collisions]


def paid_checks(field, paid, bit, expected_bit):
    return {
        "bit": bit == expected_bit,
        "head_radiation": field[H][CLK:] == paid[H][CLK:],
        "head_radiation_values": [show(w) for w in field[H][CLK:]],
        "head_radiation_target": [show(w) for w in paid[H][CLK:]],
        "auxiliary_mismatch": k.mismatch(field, paid, READ),
        "outside_rx_matter_mismatch": k.mismatch(
            field, paid, tuple(pos for pos in POSITIONS if pos not in ((RX, R0), (RX, R2)))
        ),
        "full_mismatch": k.mismatch(field, paid, POSITIONS),
    }


def run(fixture, name, offset, limit, cuts, templates, digest, detailed):
    checks = k.Witnesses()
    seed = field = stock(cuts[offset], fixture)
    seed_bit = bit = offset % 2
    account = k.account(field)
    k.trace_cut(digest, field)
    pending = retained = None
    reads, works, losses = [], [], []
    first_return = None
    last_genuine = None
    changes = Counter()
    upper = {site: set() for site in SITES}
    timeline, by_age, contact_log = {}, {}, {}
    aux_b2 = []
    a_b2_on_third_tick = False
    for t in range(1, limit + 1):
        incoming = field
        incoming_bit = bit
        stock_index = (offset + t - 1) % k.LAP
        start = incoming[RX][R0]
        after_c, field, tags, bit = k.transition(incoming, bit, account, checks, [name, t], digest)
        if t == 3 and tags[A] == 2:
            a_b2_on_third_tick = True
        if tags[A] == 2:
            aux_b2.append(t)
        for site in SITES:
            if incoming[site][R0] != after_c[site][R0]:
                upper[site].add(t)
        word_c, word_b = after_c[RX][R0], field[RX][R0]
        qualified = [rank for rank, (expected_bit, template) in templates.items()
                     if expected_bit == incoming_bit and tags[H] == 1
                     and k.mismatch(incoming, template, READ) is None]
        if qualified:
            reads.append([t, qualified])
            if len(qualified) != 1:
                checks.note("ambiguous_state_qualified_read", [name, t, qualified])
        if detailed and t in DETAIL_TICKS:
            contact_log[t] = detail(incoming, after_c, field, tags, incoming_bit)
        if t <= 24:
            timeline[t] = [tags[H], tags[RX], tags[A], tags[S], show(start), show(word_c), show(word_b)]
        if pending is not None:
            rank, read_tick = pending
            net_write = word_b != start
            works.append({
                "tick": t, "read_tick": read_tick, "rank": rank,
                "tags": [tags[H], tags[RX]],
                "words": [show(word) for word in (start, word_c, word_b)],
                "net": net_write,
                "paid": paid_checks(
                    field, stock(cuts[stock_index + 1], fixture), bit, (stock_index + 1) % 2
                ),
            })
            if net_write:
                retained = (t, rank, word_b)
                last_genuine = retained
        for stage, prior, current, current_bit in (
            ("C", start, word_c, incoming_bit), ("B", word_c, word_b, bit),
        ):
            if pending is None and prior != current:
                changes[stage] += 1
            if pending is None and retained is not None and current != retained[-1]:
                losses.append([t, stage, retained[0], retained[1], show(retained[-1]), show(current)])
                retained = None
            # On a qualified work's C cut the old history is superseded.
            if last_genuine is not None and (pending is None or stage == "B"):
                wt, rank, written = last_genuine
                by_age[t, stage, current_bit] = (t - wt, rank, written, current)
        pending = (qualified[0], t) if len(qualified) == 1 else None
        if first_return is None and field == seed and bit == seed_bit:
            first_return = t
    record = {
        "offset": offset, "ticks": limit, "account": k.reported_account(seed),
        "audits": checks.report(), "reads": reads, "works": works,
        "first_loss_per_genuine_write": losses, "first_return": first_return,
        "pending": pending, "out_of_work_changes": [changes["C"], changes["B"]],
        "A_B2_t3": a_b2_on_third_tick,
        "A_B2_count": len(aux_b2), "A_B2_first": aux_b2[:6],
    }
    if detailed:
        record.update({"detail": contact_log, "upper_C_through_24": {
            site: sorted(t for t in steps if t <= 24) for site, steps in upper.items()
        }})
    return record, by_age, upper, timeline


def aliases(streams):
    names = tuple(streams)
    found = {}
    criteria = ("same_elapsed_cut", "same_age")
    for i, first in enumerate(names):
        for second in names[i + 1:]:
            left, right = streams[first], streams[second]
            for key in sorted(left.keys() & right.keys()):
                t, stage, bit = key
                a, b = left[key], right[key]
                if a[1] == b[1] or a[2] == b[2] or a[3] != b[3]:
                    continue
                witness = [t, stage, bit, show(a[3]), [first, a[0], a[1], show(a[2])],
                           [second, b[0], b[1], show(b[2])]]
                for criterion in criteria:
                    if criterion == "same_age" and a[0] != b[0]:
                        continue
                    if criterion not in found or (t, stage == "B", bit) < (
                        found[criterion][0], found[criterion][1] == "B", found[criterion][2]
                    ):
                        found[criterion] = witness
    return found


def compared_movements(baseline, actual, intervals):
    return {
        site: [[lo, hi, len(base := {t for t in baseline[site] if lo <= t <= hi}),
                len(new := {t for t in actual[site] if lo <= t <= hi}),
                len(base - new), len(new - base)]
               for lo, hi in intervals]
        for site in SITES
    }


def main():
    assert (H, RX, S) == (k.HEAD, k.PASSIVE, k.SUPPORT)
    digest = k.sha256()
    findings = k.Findings()
    cuts, _, arrivals = k.bare_reference(findings, digest)
    if findings.counts:
        raise RuntimeError(f"bare reference failed: {findings.first}")
    assert len(arrivals) == 85
    offsets = {rank: (arrival - 1) % k.LAP for rank, arrival in arrivals.items()}
    streams = {"rawzero": 0, "pre44": offsets[44], "pre4": offsets[4]}
    base_fresh = {}
    base_stream = {}
    for fixture in FIXTURES:
        fixture_digest = k.sha256()
        templates = {rank: (offsets[rank] % 2, stock(cuts[offsets[rank]], fixture))
                     for rank in TARGETS}
        census = {"t3_B2": [], "t3_B2_elsewhere_1_to_24": [], "pre_or_foil_write": [],
                  "qualified_t1": [], "non_target_qualified": [], "fresh_account_varies": [],
                  "audit_failures": []}
        target_rows = {}
        baseline_book = k.reported_account(stock(cuts[0], fixture))
        movement_foils = [0, 0]
        for rank, offset in sorted(offsets.items()):
            trial, _, movement, timeline = run(fixture, rank, offset, 24, cuts, templates,
                                               fixture_digest, rank in TARGETS)
            if trial["A_B2_t3"]:
                census["t3_B2"].append(rank)
            elif trial["A_B2_count"]:
                census["t3_B2_elsewhere_1_to_24"].append(rank)
            if trial["reads"] and trial["reads"][0][0] == 1:
                census["qualified_t1"].append(rank)
            if rank not in TARGETS and trial["reads"]:
                census["non_target_qualified"].append(rank)
            if trial["account"] != baseline_book:
                census["fresh_account_varies"].append(rank)
            if trial["audits"]:
                census["audit_failures"].append([rank, trial["audits"]])
            unexpected = (1,) if rank in TARGETS else (1, 2)
            if any(len(set(timeline[t][4:])) > 1 for t in unexpected):
                census["pre_or_foil_write"].append(rank)
            if fixture == "baseline":
                base_fresh[rank] = movement
            if rank in TARGETS:
                trial["upper_C_comparison"] = compared_movements(base_fresh[rank], movement, INTERVALS)
                target_rows[rank] = trial
            else:
                for i, site in enumerate((H, RX)):
                    movement_foils[i] += len(base_fresh[rank][site] - movement[site])
        stream_records, held = {}, {}
        stream_intervals = INTERVALS + ((25, 622), (623, 1244), (1245, 1866),
                                        (1867, 2488), (2489, 3110))
        for name, offset in streams.items():
            trial, held[name], movement, _ = run(fixture, name, offset, 3110, cuts, templates,
                                                  fixture_digest, False)
            if fixture == "baseline":
                base_stream[name] = movement
            trial["upper_C_comparison"] = compared_movements(base_stream[name], movement, stream_intervals)
            stream_records[name] = trial
        print(json.dumps({
            "fixture": fixture, "fresh": census, "target_fresh": target_rows, "streams": stream_records,
            "foil_missed_upper_C_H_RX": movement_foils, "aliases": aliases(held),
            "trace_sha256": fixture_digest.hexdigest(),
        }, separators=(",", ":"), sort_keys=True))
    print(f"bare_trace_sha256={digest.hexdigest()}")


if __name__ == "__main__":
    main()
