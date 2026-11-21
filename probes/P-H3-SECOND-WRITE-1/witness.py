# SPDX-License-Identifier: Apache-2.0
"""Exact Python replay and compensated local controls for a second H3 write."""

import kernel as k
import measure as m


FIRST_EMISSION = 125
FIRST_WORK = 159
WORKER = 28


def _step(field, tick):
    return k.native_step(field, tick % 2)


def _work_detail(pre, contact, complete, tick):
    if tick <= FIRST_WORK or tick % 2 != 1 or pre[m.MEMORY][:2] != m.W_WORD:
        return None
    worker_pre = pre[WORKER]
    worker_c = contact[WORKER]
    worker_b = complete[WORKER]
    if worker_pre[:2] == worker_c[:2] or worker_c[:2] == worker_b[:2]:
        return None
    actual, actual_tag = k.scatter(worker_c)
    if actual_tag != 2 or actual != worker_b:
        return None

    # The native odd bond goes from (7,3) to (7,0), so the worker is second.
    hybrid_matter = tuple(
        k.contact(m.T_WORD[lane], worker_pre[lane])[1] for lane in range(2)
    )
    hybrid_c = (*hybrid_matter, *worker_c[2:])
    hybrid_b, hybrid_tag = k.scatter(hybrid_c)
    if hybrid_matter != worker_pre[:2] or hybrid_tag != 0 or hybrid_b != hybrid_c:
        return None
    if hybrid_b[:2] == worker_b[:2]:
        return None

    payer = next((site for site in range(28) if pre[site][:2] == m.T_WORD), None)
    if payer is None:
        return None
    return hybrid_c, hybrid_b, payer


def _local(pre, contact, complete, site):
    return {
        "pre_C": [k.reported(word) for word in pre[site]],
        "post_C": [k.reported(word) for word in contact[site]],
        "post_B": [k.reported(word) for word in complete[site]],
        "tag": k.scatter(contact[site])[1],
    }


def inspect_contact(pre, tick, *, ledger=None):
    """Audit two complete one-tick cuts from an exact pre-C field and time."""
    ledger = k.account(pre) if ledger is None else ledger
    m.require(k.reported_account(pre) == m.LEDGER, (tick, "witness initial account"))
    contact, complete, tags = m.native(pre, tick, ledger, ("local witness",))
    result = _work_detail(pre, contact, complete, tick)
    m.require(result is not None, (tick, "qualifying later work"))
    hybrid_c, hybrid_b, payer = result
    swapped = m.replace(pre, m.MEMORY, (*m.T_WORD, *pre[m.MEMORY][2:]))
    swapped = m.replace(swapped, payer, (*m.W_WORD, *pre[payer][2:]))
    m.require(k.account(swapped) == ledger, (tick, "compensated pre-C account"))
    swap_c, swap_b, swap_tags = m.native(swapped, tick, ledger, ("word swap",))
    m.require(
        (swap_c[WORKER], swap_b[WORKER], swap_tags[WORKER]) == (hybrid_c, hybrid_b, 0),
        (tick, "compensated full-evolution projection"),
    )
    m.require(tags[WORKER] == 2, (tick, "native B2"))
    return {
        "tick": tick,
        "bit": tick % 2,
        "memory_site": m.MEMORY,
        "worker_site": WORKER,
        "payer_site": payer,
        "live_word": _local(pre, contact, complete, m.MEMORY),
        "live_worker": _local(pre, contact, complete, WORKER),
        "swapped_word": _local(swapped, swap_c, swap_b, m.MEMORY),
        "swapped_worker": _local(swapped, swap_c, swap_b, WORKER),
        "swapped_payer": _local(swapped, swap_c, swap_b, payer),
    }


def _omission(contact, complete, site, ledger, tick):
    restored, reverse_tag = k.scatter(complete[site])
    m.require(restored == contact[site] and reverse_tag == 1, (tick, site, "B2 undo"))
    omitted = m.replace(complete, site, restored)
    m.require(k.account(omitted) == ledger, (tick, site, "B2 omission account"))
    return omitted


def _formation(pre, contact, complete, tick):
    for stage, prior, result in (("C", pre, contact), ("B", contact, complete)):
        if prior[m.MEMORY][:2] != m.W_WORD and result[m.MEMORY][:2] == m.W_WORD:
            yield {
                "cut": [tick, stage],
                "strict_B1_restore": (
                    stage == "B" and contact[m.MEMORY][:2] == m.T_WORD
                    and k.scatter(contact[m.MEMORY])[1] == 1
                ),
                "word": _local(pre, contact, complete, m.MEMORY),
            }


def _matched_control(live, other, tick):
    live_pre, live_c, live_b = live
    other_pre, other_c, other_b = other
    same_worker_input = live_pre[WORKER] == other_pre[WORKER]
    same_incoming_radiation = live_c[WORKER][2:] == other_c[WORKER][2:]
    result = _work_detail(live_pre, live_c, live_b, tick)
    matches_swap = False
    if result is not None:
        hybrid_c, hybrid_b, _ = result
        matches_swap = (
            same_worker_input and same_incoming_radiation
            and other_pre[m.MEMORY][:2] == m.T_WORD
            and other_c[WORKER] == hybrid_c and other_b[WORKER] == hybrid_b
        )
    return {
        "same_worker_input": same_worker_input,
        "same_incoming_radiation": same_incoming_radiation,
        "matches_compensated_word_swap": matches_swap,
        "control_qualifies": _work_detail(other_pre, other_c, other_b, tick) is not None,
        "word": _local(other_pre, other_c, other_b, m.MEMORY),
        "worker": _local(other_pre, other_c, other_b, WORKER),
    }


class _Arm:
    def __init__(self, field):
        self.field = field
        self.first_work = None
        self.first_reappearance = None
        self.last_formation = None

    def advance(self, tick):
        pre = self.field
        contact, self.field = _step(pre, tick)
        return pre, contact, self.field

    def score(self, stages, tick):
        for formation in _formation(*stages, tick):
            if self.first_reappearance is None:
                self.first_reappearance = formation
            self.last_formation = formation
        if self.first_work is None and _work_detail(*stages, tick) is not None:
            self.first_work = tick

    def summarize(self):
        return {
            "first_qualifying_later_work": self.first_work,
            "first_reappearance": self.first_reappearance,
        }


def _fresh_omissions(antecedents, live_stages, second_tick, ledger):
    outcomes = []
    for tick, control_start in antecedents:
        arm = _Arm(control_start)
        for time in range(tick + 1, second_tick + 1):
            control = arm.advance(time)
            arm.score(control, time)
        outcomes.append({
            "omitted_source_tick": tick,
            **arm.summarize(),
            "at_live_second": _matched_control(live_stages, control, second_tick),
        })
    return outcomes


def replay(field, second_tick=None, scan_length=8192, *, fresh_source_window=0):
    """Evolve independent exact live/omission histories through a fixed horizon.

    When an expected second tick is within the horizon, require the independently
    observed first qualifying later work to agree. If omitted, report what the
    Python scan observes. A second tick beyond the horizon is left unverified.
    """
    if scan_length < FIRST_WORK:
        raise ValueError("scan_length precedes the first worker write")
    if second_tick is not None and second_tick <= FIRST_WORK:
        raise ValueError("second_tick must be after the first worker write")
    if fresh_source_window < 0:
        raise ValueError("fresh_source_window must be nonnegative")

    field = tuple(map(tuple, field))
    ledger = k.account(field)
    m.require(k.reported_account(field) == m.LEDGER, ("Python launch account",))
    live = _Arm(field)
    controls = {}
    antecedents = []
    control_witnesses = {}
    result = {"scan_length": scan_length, "expected_second": second_tick}
    witness = None
    readiness = {
        name: {"first": None, "count": 0}
        for name in ("pre_worker", "radiation", "receiver_ready", "joint_ready")
    }
    worker_reference = radiation_reference = None

    for tick in range(1, scan_length + 1):
        live_stages = live.advance(tick)
        pre, contact, complete = live_stages
        control_stages = {name: arm.advance(tick) for name, arm in controls.items()}
        if tick in (FIRST_EMISSION, FIRST_WORK) or (
            second_tick is not None and abs(tick - second_tick) <= 2
        ):
            audited_c, audited_b, _ = m.native(pre, tick, ledger, ("Python replay",))
            m.require((contact, complete) == (audited_c, audited_b), (tick, "replay audit"))
            for name, (arm_pre, arm_c, arm_b) in control_stages.items():
                checked_c, checked_b, _ = m.native(arm_pre, tick, ledger, (name,))
                m.require((arm_c, arm_b) == (checked_c, checked_b), (tick, name, "audit"))

        if tick == FIRST_EMISSION and k.scatter(contact[m.SOURCE])[1] == 2:
            controls["source125_off"] = _Arm(_omission(contact, complete, m.SOURCE, ledger, tick))
        if tick == FIRST_WORK:
            m.require(
                pre[m.MEMORY][:2] == m.W_WORD and contact[m.MEMORY][:2] != m.W_WORD
                and k.scatter(contact[WORKER])[1] == 2 and contact[WORKER][:2] != complete[WORKER][:2],
                (tick, "first write and word consumption"),
            )
            controls["worker159_off"] = _Arm(_omission(contact, complete, WORKER, ledger, tick))
            worker_reference = pre[WORKER]
            radiation_reference = contact[WORKER][2:]
            result["first_after_spend"] = {
                "cut": [tick, "C"],
                "word": _local(pre, contact, complete, m.MEMORY),
                "worker": _local(pre, contact, complete, WORKER),
            }
        if tick <= FIRST_WORK:
            continue

        if tick % 2:
            same_worker = pre[WORKER] == worker_reference
            same_radiation = contact[WORKER][2:] == radiation_reference
            receiver_ready = same_worker and same_radiation
            for name, occurred in (
                ("pre_worker", same_worker),
                ("radiation", same_radiation),
                ("receiver_ready", receiver_ready),
                ("joint_ready", receiver_ready and pre[m.MEMORY][:2] == m.W_WORD),
            ):
                if occurred:
                    event = readiness[name]
                    event["count"] += 1
                    if event["first"] is None:
                        event["first"] = tick

        preceding_control_formations = {name: arm.last_formation for name, arm in controls.items()}
        for name, stages in control_stages.items():
            controls[name].score(stages, tick)

        if fresh_source_window and witness is None:
            cutoff = tick - fresh_source_window
            antecedents = [(time, omitted) for time, omitted in antecedents if time >= cutoff]

        preceding_formation = live.last_formation
        live.score(live_stages, tick)
        if witness is None and live.first_work == tick:
            witness = inspect_contact(pre, tick, ledger=ledger)
            witness["last_formation_before_read"] = preceding_formation
            m.require(preceding_formation is not None, (tick, "word must reform before read"))
            for name, stages in control_stages.items():
                control_witnesses[name] = {
                    **_matched_control(live_stages, stages, tick),
                    "last_formation_before_live_read": preceding_control_formations[name],
                }
            if fresh_source_window:
                witness["fresh_source_omissions"] = _fresh_omissions(
                    antecedents, live_stages, tick, ledger
                )

        if fresh_source_window and witness is None and k.scatter(contact[m.SOURCE])[1] == 2:
            antecedents.append((tick, _omission(contact, complete, m.SOURCE, ledger, tick)))

    m.require(k.account(live.field) == ledger, (scan_length, "Python live final account"))
    for name, arm in controls.items():
        m.require(k.account(arm.field) == ledger, (scan_length, name, "final account"))
    if second_tick is not None and second_tick <= scan_length:
        m.require(live.first_work == second_tick, (second_tick, live.first_work, "first later work"))
    result.update(live.summarize())
    result["witness"] = witness
    result["readiness"] = readiness
    result["controls"] = {
        name: {**arm.summarize(), "at_live_second": control_witnesses.get(name)}
        for name, arm in controls.items()
    }
    return result
