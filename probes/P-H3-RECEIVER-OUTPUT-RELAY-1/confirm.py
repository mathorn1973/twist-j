# SPDX-License-Identifier: Apache-2.0
"""Check relay certificates in the inherited five-coefficient H3 kernel."""

from collections import defaultdict
from functools import lru_cache

import witness

k = witness.k
m = witness.m
CARRIER, TARGET, RANK = 2, 3, 43
LIMIT = 1 << 26
FIXED = ((7316785, 7390473, 7390475, 1), (8176761, 9915381, 9915383, 2))


def matter(cell):
    return cell[:2]


def decode_trace(cells, label):
    m.require(len(cells) == 4 and all(len(cell) == 4 and all(len(word) == 4 for word in cell)
                                      for cell in cells), (label, "four j-basis cells"))
    return tuple(tuple(k.from_j(*word) for word in cell) for cell in cells)


def flags(before, after):
    return [a != b for a, b in zip(matter(before), matter(after))]


def contact_projection(trace, tick, partner):
    pre, after, mate_pre, mate_after = trace
    mate, orientation = witness.vertical_mate(CARRIER, tick % 2)
    m.require(mate == partner, (tick, partner, "vertical partner"))
    m.require(witness.receiver_transport(pre, mate_pre, orientation) == after[:3]
              and witness.receiver_transport(mate_pre, pre, 1 - orientation) == mate_after[:3],
              (tick, partner, "exact local C at both endpoints"))
    admitted = [k.even(k.subtract(x, y)) for x, y in zip(matter(pre), matter(mate_pre))]
    moved = flags(mate_pre, mate_after)
    m.require(moved == flags(pre, after), (tick, partner, "per-rail movement at both endpoints"))
    return admitted, moved


def local_relay(arm, event, trail, word):
    read, stop = trail["read"], trail["stop_tick"]
    stage, site = trail["stop_stage"], trail["stop_site"]
    attempts, refused = trail["attempts"], trail["refused_rails"]
    first = trail["first3_tick"]
    m.require(event["read"] == read and read <= stop <= LIMIT
              and (stage == "END" or read < stop)
              and attempts == (stop - read + 1) // 2 and 0 <= refused <= 2 * attempts,
              (arm, "relay time and counters"))
    m.require(set(trail["traces"]) == ({"FIRST3", "STOP"} if first else {"STOP"}),
              (arm, "relay trace inventory"))
    traces = {label: decode_trace(cells, label) for label, cells in trail["traces"].items()}
    first_admitted = [False, False]
    first_flags = [False, False]
    if first:
        m.require(first == read + 1 <= stop and attempts > 0, (arm, "first target attempt"))
        trace = traces["FIRST3"]
        first_admitted, first_flags = contact_projection(trace, first, TARGET)
        m.require(matter(trace[0]) == word
                  and sum(first_admitted) == trail["first3_admitted_rails"]
                  and sum(first_flags) == trail["first3_moved_rails"]
                  and refused >= 2 - sum(first_admitted), (arm, "first target cut"))
        if any(first_flags):
            m.require((stop, stage, site) == (first, "C", TARGET) and traces["STOP"] == trace,
                      (arm, "first target movement is terminal"))
    else:
        m.require((attempts, refused, trail["first3_admitted_rails"], trail["first3_moved_rails"])
                  == (0, 0, 0, 0), (arm, "absent target attempts"))

    trace = traces["STOP"]
    pre, after, mate_pre, mate_after = trace
    m.require(matter(pre) == word, (arm, "terminal carrier word"))
    target_admitted = [False, False]
    moved = [False, False]
    third_tag = 0
    if stage == "C":
        admitted, changed = contact_projection(trace, stop, site)
        m.require(any(changed), (arm, "C expiry changes the carrier"))
        if site == TARGET:
            target_admitted = admitted
            moved = changed
            third_tag = k.scatter(mate_after)[1]
            minimum_refused = 2 - sum(admitted)
            if first != stop:
                minimum_refused += 2 - trail["first3_admitted_rails"]
            m.require(first and refused >= minimum_refused, (arm, "terminal target attempt"))
    elif stage == "B":
        m.require(site == CARRIER and matter(after) != word, (arm, "B expiry changes the carrier"))
        for a, b in ((pre, after), (mate_pre, mate_after)):
            result, tag = k.scatter(a)
            m.require(result == b and k.scatter(b)[0] == a and (a != b or tag == 0),
                      (arm, "exact terminal B and inverse at both endpoints"))
    else:
        m.require(stage == "END" and site == 32 and pre == after and mate_pre == mate_after,
                  (arm, "held at horizon"))
    m.require(sum(moved) == trail["moved_rails"] and third_tag == trail["third_tag"],
              (arm, "terminal target disposition"))
    return traces, {"first3_admitted": first_admitted, "first3_moved": first_flags,
                    "terminal_target_admitted": target_admitted, "terminal_target_moved": moved}


def replay_relay(arm, trail, traces, tick, pre, c, b, tags, state):
    partner, _ = witness.vertical_mate(CARRIER, tick % 2)
    word = state["word"]
    m.require(matter(pre[CARRIER]) == word, (arm, tick, "pre-C hold"))
    if partner == TARGET:
        state["attempts"] += 1
        admitted = [k.even(k.subtract(a, z)) for a, z in zip(word, matter(pre[TARGET]))]
        state["refused"] += 2 - sum(admitted)
        if state["attempts"] == 1:
            observed = (pre[CARRIER], c[CARRIER], pre[TARGET], c[TARGET])
            m.require(tick == trail["first3_tick"] and traces.get("FIRST3") == observed,
                      (arm, tick, "complete FIRST3 replay"))

    if matter(c[CARRIER]) != word:
        stop = ("C", partner)
        observed = (pre[CARRIER], c[CARRIER], pre[partner], c[partner])
        if partner == TARGET:
            m.require(tags[TARGET] == trail["third_tag"], (arm, tick, "target B tag"))
    elif matter(b[CARRIER]) != word:
        stop = ("B", CARRIER)
        observed = (c[CARRIER], b[CARRIER], c[partner], b[partner])
    elif tick == trail["stop_tick"]:
        stop = ("END", 32)
        observed = (b[CARRIER], b[CARRIER], b[TARGET], b[TARGET])
    else:
        return False

    m.require(tick == trail["stop_tick"] and stop == (trail["stop_stage"], trail["stop_site"])
              and observed == traces["STOP"], (arm, tick, "first expiry or horizon"))
    m.require((state["attempts"], state["refused"]) == (trail["attempts"], trail["refused_rails"]),
              (arm, tick, "complete attempt and refusal counts"))
    return True


def replay(launch, events, trails, cells, traces):
    """Replay once from launch, using the #2047 episode and transition predicates."""
    priors, writes, reads = defaultdict(list), defaultdict(list), defaultdict(list)
    for arm, event in events.items():
        priors[event["prior"]].append(arm)
        writes[event["write"]].append(arm)
        reads[event["read"]].append(arm)
    audited_ticks = set(priors) | set(writes) | set(reads)
    audited_ticks.update(trail[key] for trail in trails.values() for key in ("first3_tick", "stop_tick"))
    field = tuple(tuple(cell) for cell in launch)
    ledger = k.account(field)
    m.require(k.reported_account(field) == m.LEDGER, "original rank-43 launch ledger")
    signatures, held, active = {}, {}, {}
    finished = set()
    last_tick = max(trail["stop_tick"] for trail in trails.values())
    for tick in range(1, last_tick + 1):
        pre = field
        if tick in audited_ticks:
            c, field, tags = m.native(pre, tick, ledger, ("receiver output relay", RANK))
        else:
            c = k.transport(pre, k.HEIGHT, tick % 2)
            field, tags = k.scatter_field(c)
        for arm in tuple(active):
            if replay_relay(arm, trails[arm], traces[arm], tick, pre, c, field, tags, active[arm]):
                del active[arm]
                finished.add(arm)
        for arm in priors.get(tick, ()):
            signatures[arm] = witness.episode(pre, c, field, tags, events[arm]["writer"], tick)
        for arm in reads.get(tick, ()):
            event, saved = events[arm], cells[arm]
            writer, reader = event["writer"], event["reader"]
            m.require(held.pop(arm, None) == (writer, matter(saved["donor_pre"]))
                      and pre[writer] == saved["donor_pre"]
                      and (pre[reader], c[reader], field[reader], tags[reader])
                      == (saved["reader_pre"], saved["reader_c"], saved["reader_b"], event["reader_tag"]),
                      (arm, tick, "complete source delivery and reader B"))
            state = {"word": matter(field[CARRIER]), "attempts": 0, "refused": 0}
            if trails[arm]["stop_tick"] == tick:
                trace = (field[CARRIER], field[CARRIER], field[TARGET], field[TARGET])
                m.require(trails[arm]["stop_stage"] == "END" and trace == traces[arm]["STOP"],
                          (arm, tick, "horizon at initial output"))
                finished.add(arm)
            else:
                active[arm] = state
        for writer, word in held.values():
            m.require(matter(pre[writer]) == matter(c[writer]) == matter(field[writer]) == word,
                      (tick, writer, "uninterrupted first-hop hold"))
        for arm in writes.get(tick, ()):
            event, saved = events[arm], cells[arm]
            writer = event["writer"]
            m.require((c[writer], field[writer], tags[writer])
                      == (saved["writer_c"], saved["writer_b"], event["writer_tag"])
                      and signatures.pop(arm, None) == witness.episode(pre, c, field, tags, writer, tick),
                      (arm, tick, "recurrent B2 signature and writer cuts"))
            held[arm] = writer, matter(field[writer])
    m.require(not signatures and not held and not active and finished == set(events),
              "incomplete independent relay replay")


def check(fields, events, trails, *, full=False):
    """Return local per-rail confirmations and optional complete replay coverage."""
    arms = set(events)
    m.require(arms in ({1, 2}, {1, 2, 3, 4}) and arms == set(trails),
              "fixed pair and optional alternate pair")
    m.require(tuple(tuple(events[arm][key] for key in ("prior", "write", "read", "reader_tag"))
                    for arm in (1, 2)) == FIXED, "fixed #2049 events")
    cells = {arm: witness.local(events[arm], len(fields)) for arm in sorted(arms)}
    traces, summaries = {}, {}
    for first, second in ((1, 2), (3, 4)):
        if first not in arms:
            continue
        a, b = cells[first], cells[second]
        m.require({events[arm]["reader_tag"] for arm in (first, second)} == {1, 2}
                  and a["reader_pre"] == b["reader_pre"] and a["reader_c"][2:] == b["reader_c"][2:]
                  and all(matter(a[key]) != matter(b[key]) for key in ("writer_b", "reader_c", "reader_b")),
                  (first, second, "independent matched opposite branches"))
        for arm in (first, second):
            event, saved = events[arm], cells[arm]
            m.require((event["rank"], event["writer"], event["reader"], event["bit"], event["writer_tag"])
                      == (RANK, 1, CARRIER, 1, 2) and event["prior"] > 0 and not event["anchor"]
                      and all(flags(saved["reader_pre"], saved["reader_c"])),
                      (arm, "two recurrent source writes and moving first hop"))
            traces[arm], summaries[arm] = local_relay(arm, event, trails[arm], matter(saved["reader_b"]))
        if first == 3:
            m.require(all(any(summaries[arm]["terminal_target_moved"]) for arm in (first, second)),
                      "alternate pair must relay on both arms")

    if full:
        operations = {name: getattr(k, name) for name in ("multiply", "norm", "contact", "scatter")}
        try:
            for name, operation in operations.items():
                setattr(k, name, lru_cache(maxsize=131072)(operation.__wrapped__))
            replay(fields[RANK], events, trails, cells, traces)
        finally:
            for name, operation in operations.items():
                setattr(k, name, operation)
    return {"arms": summaries, "events": len(arms), "full_replayed": len(arms) if full else 0}
