# SPDX-License-Identifier: Apache-2.0
"""Actual native packet detector calibrated on one earlier public field word."""

from light import L, NY, RX, collide, get, ledger, move, packet_launch
from native import h3


# PR #2034, EXPECTED.txt, right packet, post-C tick 40 at D=20.
W = (
    -21386172564582355000912103625195520000,
    -26736559282320142690578810420592640000,
    -35364882103878625360276832082984960000,
    1907317838809156011152305259806720000,
)
HORIZON = 80
DISTANCES = (20, 30, 40, 60)


def launch(distance, gap):
    state = {k: v for k, v in packet_launch(distance).items() if k[2] == 3}
    for y in range(NY):
        state[RX, y, 0] = gap
        state[RX, y, 1] = h3.scale(-1, gap)
    return state


def cell(state, y):
    return tuple(get(state, RX, y, r) for r in range(4))


def local_work(before, after):
    h_deltas = [h3.sub(h3.h(v), h3.h(u)) for u, v in zip(before, after)]
    assert h3.ring_sum(h_deltas) == h3.ZERO
    return h3.add(h_deltas[0], h_deltas[1])


def offsite_clk(state):
    return [(y, get(state, RX, y, 2)) for y in range(1, NY) if get(state, RX, y, 2) != h3.ZERO]


def run_arm(distance, gap):
    initial = launch(distance, gap)
    account = ledger(initial)
    state = initial
    first_arrival = None
    first_offsite = None
    cuts = {}
    events = []
    for tick in range(1, HORIZON + 1):
        bit = (tick - 1) % 2
        incident = move(state, bit)
        result, tags = collide(incident)
        assert ledger(incident) == ledger(result) == account
        undo_b, _ = collide(result)
        assert undo_b == incident and move(incident, bit, backward=True) == state
        assert all(x == RX for x, _ in tags)
        if first_arrival is None and get(incident, RX, 0, 3) != h3.ZERO:
            first_arrival = tick
        arriving_clk = offsite_clk(incident)
        if first_offsite is None and arriving_clk:
            first_offsite = {"tick": tick, "before_B": arriving_clk, "after_B": offsite_clk(result)}
        for (_, y), tag in sorted(tags.items()):
            a, b = cell(incident, y), cell(result, y)
            work = local_work(a, b)
            events.append({
                "tick": tick, "row": y, "B": tag,
                "work_H": work, "work_Q": h3.scalar_account(work),
                "incoming_CORR": a[3], "target_CLK_after_B": b[2],
            })
        if tick in (40, 60, 80):
            cuts[tick] = {
                "receiver_before_B": cell(incident, 0), "receiver_after_B": cell(result, 0),
                "offsite_CLK_before_B": arriving_clk, "offsite_CLK_after_B": offsite_clk(result),
            }
        state = result
    for tick in range(HORIZON, 0, -1):
        state, _ = collide(state)
        state = move(state, (tick - 1) % 2, backward=True)
    assert state == initial
    return {
        "distance_cells": distance, "account": account,
        "first_arrival": first_arrival,
        "first_active_B": events[0] if events else None,
        "first_offsite_CLK_at_post_C": first_offsite, "all_active_B": events,
        "cuts": cuts, "full_state_restored": True,
    }


def run():
    gap = h3.half(h3.mul(W, h3.J_INV))
    assert h3.scale(2, h3.mul(gap, h3.J)) == W
    predicted_clk = h3.mul(gap, h3.RHO)
    predicted_neighbor = h3.half(h3.mul(L, predicted_clk))
    declared_cost = h3.scale(2 * NY, h3.h(gap))
    arms = [run_arm(distance, gap) for distance in DISTANCES]
    assert all(arm["account"] == arms[0]["account"] for arm in arms)
    packet_only = {k: v for k, v in packet_launch(20).items() if k[2] == 3}
    assert h3.sub(arms[0]["account"][2], ledger(packet_only)[2]) == declared_cost
    return {
        "previous_public_word_W": W, "preloaded_matter_half_gap": gap,
        "apparatus_H": declared_cost, "apparatus_Q": h3.scalar_account(declared_cost),
        "predicted_CLK_if_first_B_is_nominal": predicted_clk,
        "predicted_separate_CLK_at_next_C_if_nominal": predicted_neighbor,
        "calibration_first_B_no_later_than_40": (
            arms[0]["first_active_B"] is not None and arms[0]["first_active_B"]["tick"] <= 40
        ),
        "arms": arms,
    }
