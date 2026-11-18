# SPDX-License-Identifier: Apache-2.0
"""Intermediate-cut calibration with compensated local front checks."""

from collections import Counter

import kernel as k
import measure as m
import models
import stock as s


TICK = 159
WORKER = 28
MEMORY = 31
SOURCE = 7
ESCROW = 17


def calibration_basis(bare):
    """Replay the published 324 launch and source-only comparison through 158 B."""
    live = s.baseline(bare)
    ledger = k.account(live)
    m.require(k.reported_account(live) == m.LEDGER, "calibration launch Q774")
    off = None
    first_difference = None
    for tick in range(1, TICK):
        live_c, live, live_tags = m.native(live, tick, ledger, ("calibration", "base_live"))
        if off is not None:
            off_c, off, off_tags = m.native(off, tick, ledger, ("calibration", "base_off"))
            if first_difference is None:
                if live_c[MEMORY] != off_c[MEMORY]:
                    first_difference = tick, "C"
                elif live[MEMORY] != off[MEMORY]:
                    first_difference = tick, "B"
            if tick == 157:
                m.require(first_difference == (157, "C"), "calibration first recipient contrast")
                m.require(
                    live_c[MEMORY][:3] == off_c[MEMORY][:3]
                    and live_c[MEMORY][3] != off_c[MEMORY][3]
                    and live_c[MEMORY][:2] == m.T_WORD
                    and live[MEMORY][:2] == m.W_WORD
                    and off[MEMORY][:2] == m.T_WORD
                    and (live_tags[MEMORY], off_tags[MEMORY]) == (1, 0),
                    "calibration exact 157B restore",
                )
        elif tick == 125:
            undone, inverse_tag = k.scatter(live[SOURCE])
            m.require(
                live_tags[SOURCE] == 2
                and (undone, inverse_tag) == (live_c[SOURCE], 1)
                and undone[3] != live[SOURCE][3],
                "calibration source inverse",
            )
            off = m.replace(live, SOURCE, undone)
            m.require(k.account(off) == ledger, "calibration source inverse account")

    m.require(live[MEMORY] == (*m.W_WORD, s.W, k.ZERO), "calibration 158B live memory")
    m.require(
        off[MEMORY] == (*m.T_WORD, k.from_j(2, 1, 2, 2), k.from_j(1, 2, 0, 3)),
        "calibration 158B source-off memory",
    )
    return live, off, ledger


def observe(live, off, ledger, mode, context):
    m.require(k.account(live) == k.account(off) == ledger, (context, mode, "pre-C accounts"))
    m.require((live[MEMORY][:2], off[MEMORY][:2]) == (m.W_WORD, m.T_WORD),
              (context, mode, "memory words"))
    live_cut = m.native(live, TICK, ledger, (context, mode, "live"))
    off_cut = m.native(off, TICK, ledger, (context, mode, "off"))
    expected_live = tuple(k.contact(live[MEMORY][lane], live[WORKER][lane])[1]
                          for lane in (k.R0, k.R2))
    expected_off = tuple(k.contact(off[MEMORY][lane], off[WORKER][lane])[1]
                         for lane in (k.R0, k.R2))
    m.require(live_cut[0][WORKER][:2] == expected_live and off_cut[0][WORKER][:2] == expected_off,
              (context, mode, "vertical edge orientation"))
    scored = m.read_projection(live, live_cut, WORKER)
    if scored is None:
        return None

    worker = WORKER
    read, inhibit, work, forced_c, forced_b, forced_tag = scored
    if not m.matches_off(live, off, live_cut, off_cut, worker, forced_c, forced_b, forced_tag):
        return None
    m.require(worker == WORKER, (context, mode, "worker site"))
    payer = m.escrow(live, TICK, worker, (forced_c, forced_b, forced_tag), ledger, (context, mode))
    hit = {
        "mode": mode,
        "label": models.label(mode),
        "tick": TICK,
        "bit": TICK % 2,
        "memory_site": MEMORY,
        "worker_site": worker,
        "live_memory": m.triple(live, live_cut, MEMORY),
        "off_memory": m.triple(off, off_cut, MEMORY),
        "live_worker": m.triple(live, live_cut, worker),
        "off_worker": m.triple(off, off_cut, worker),
        "hybrid_worker_post_C": [k.reported(word) for word in forced_c],
        "hybrid_worker_post_B": [k.reported(word) for word in forced_b],
        "hybrid_worker_tag": forced_tag,
        "escrow_site": payer,
        "ledger": k.reported_account(live),
    }
    if payer is not None:
        hit["escrow_pre_C"] = [k.reported(word) for word in live[payer]]
    return {"read": read, "inhibit": inhibit, "work": work, "escrow": payer is not None}, hit


def front():
    """An isolated equal-account front, independent of occupied 158B stock slots."""
    for mode, (design, worker, lane) in models.DESIGNS.items():
        if worker != WORKER or lane != k.CORR:
            continue
        a, b, _, _, _, _, _, predicted_tag = design
        live_matter = k.contact(s.W, a)[1]
        off_matter = k.contact(s.T, a)[1]
        if live_matter == a or k.norm(live_matter) == k.norm(off_matter):
            continue

        live = [(k.ZERO,) * 4] * 32
        live[MEMORY] = (*m.W_WORD, k.ZERO, k.ZERO)
        live[WORKER] = (*s.pair(a), k.ZERO, b)
        # Odd horizontal matching pairs (7,0) with (0,0); equal CORR stays fixed.
        live[0] = (k.ZERO, k.ZERO, k.ZERO, b)
        live[ESCROW] = (*m.T_WORD, k.ZERO, k.ZERO)
        live = tuple(live)
        off = m.replace(live, MEMORY, (*m.T_WORD, *live[MEMORY][2:]))
        off = m.replace(off, ESCROW, (*m.W_WORD, *live[ESCROW][2:]))
        answer = observe(live, off, k.account(live), mode, "synthetic_front")
        if answer is None:
            continue
        flags, hit = answer
        m.require(hit["live_worker"]["tag"] == predicted_tag, ("synthetic front guard", mode))
        if flags["work"] and flags["escrow"]:
            return {"status": "synthetic_equal_account_front", "flags": flags, "witness": hit}
    raise AssertionError("No synthetic front achieved work with an exact compensating swap")


def run(bare43):
    """Return counts and first witnesses at the intermediate-cut intervention."""
    base_live, base_off, ledger = calibration_basis(bare43)
    counts = Counter(tested=0, eligible=0, ineligible=0, contrast=0,
                     read=0, inhibit=0, work=0, escrow=0)
    first = {}
    for mode in models.ALL:
        counts["tested"] += 1
        live = models.decorate(base_live, mode)
        off = models.decorate(base_off, mode)
        if live is None or off is None:
            counts["ineligible"] += 1
            continue
        counts["eligible"] += 1
        answer = observe(live, off, ledger, mode, "intermediate_158B")
        if answer is None:
            continue
        counts["contrast"] += 1
        flags, hit = answer
        for name, passed in flags.items():
            if passed:
                counts[name] += 1
                first.setdefault(name, hit)
    return {
        "status": "intermediate_cut_calibration",
        "intervention_cut": [158, "B"],
        "native_measurement_tick": TICK,
        "counts": dict(counts),
        "first": first,
        "synthetic_front": front(),
    }
