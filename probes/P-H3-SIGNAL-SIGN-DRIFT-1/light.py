# SPDX-License-Identifier: Apache-2.0
"""Loaded H3 detector, driven by analytic fronts and translated packets."""

from native import h3, transport


NX, NY = 384, 6
RX = 1
MEMORY_Y = NY - 1
L = h3.sub(h3.ONE, h3.RHO)
L3 = h3.mul(h3.mul(L, L), L)
REFERENCE = h3.add(h3.mul(L3, h3.RHO), h3.scale(4, h3.ONE))
NO_TAG = 0


def get(state, x, y, rail):
    return state.get((x % NX, y % NY, rail), h3.ZERO)


def write(state, key, word):
    if word != h3.ZERO:
        state[key] = word
    else:
        state.pop(key, None)


def move(state, bit, backward=False):
    """Sparse evaluation of every nontrivial edge in the full matching."""
    out = state.copy()
    for x, y, rail in state:
        if rail == 3:
            a = ((x - ((x - bit) % 2)) % NX, y, rail)
            b = ((a[0] + 1) % NX, y, rail)
        else:
            a = (x, (y - ((y - bit) % 2)) % NY, rail)
            b = (x, (a[1] + 1) % NY, rail)
        if (x, y, rail) == b and a in state:
            continue
        u, v = h3.transport_pair(state.get(a, h3.ZERO), state.get(b, h3.ZERO), backward)
        write(out, a, u)
        write(out, b, v)
    return out


def collide(state):
    out = state.copy()
    tags = {}
    material_sites = {(x, y) for x, y, rail in state if rail < 2}
    for x, y in material_sites:
        cell = tuple(get(state, x, y, rail) for rail in range(4))
        result, tag = h3.collision(cell)
        if tag:
            tags[x, y] = tag
            for rail, word in enumerate(result):
                write(out, (x, y, rail), word)
    return out, tags


def dense(state):
    out = [h3.ZERO] * (NX * NY * 4)
    for (x, y, rail), value in state.items():
        out[h3.index(NY, x, y, rail)] = value
    return tuple(out)


def ledger(state):
    h = h3.ring_sum(h3.h(v) for v in state.values())
    material = h3.ring_sum(v for (_, _, r), v in state.items() if r < 2)
    radiation = h3.ring_sum(v for (_, _, r), v in state.items() if r >= 2)
    return material, radiation, h, h3.scalar_account(h)


def apparatus():
    return {(RX, 0, 0): L3, (RX, 0, 1): h3.scale(-1, L3), (RX, MEMORY_Y, 2): REFERENCE}


def front_launch(distance, code):
    state = apparatus()
    slot = 0
    for d, factor in ((1, h3.mul(L, L)), (3, h3.ONE)):
        for name, v in (("tuned", h3.J), ("detuned", h3.ONE)):
            word = h3.scale(2 ** (d + 1), h3.mul(factor, v))
            near = d == distance and name == code
            x = (RX - d) % NX if near else 120 + slot
            state[x, 0, 3] = word
            state[121 + slot, 0, 3] = h3.scale(-1, word)
            slot += 2
    return state


def packet_launch(distance):
    state = apparatus()
    phi = h3.scale(-1, h3.add(h3.RHO, h3.RHO_INV))
    imaginary = h3.sub(h3.RHO, h3.RHO_INV)
    vector = (h3.scale(-250, imaginary), h3.add(h3.scale(1188, h3.ONE), h3.scale(412, phi)))
    for n in range(-15, 16):
        taper = (256 - n * n) ** 4
        modulator = h3.add(h3.scale(32, h3.ONE), h3.scale(n, imaginary))
        for s, value in enumerate(vector):
            x = (1 - (2 * n + s) - 2 * distance) % NX
            scale = 2 ** 80 * taper * (-1 if n % 2 else 1)
            state[x, 0, 3] = h3.scale(scale, h3.mul(modulator, value))
    return state


def read(pre_b, post_b, tags):
    incoming = get(pre_b, RX, 0, 3)
    before = tuple(get(pre_b, RX, 0, r) for r in range(4))
    after = tuple(get(post_b, RX, 0, r) for r in range(4))
    h_before = h3.add(h3.h(before[0]), h3.h(before[1]))
    h_after = h3.add(h3.h(after[0]), h3.h(after[1]))
    work = h3.sub(h_after, h_before)
    rad_before = h3.add(h3.h(before[2]), h3.h(before[3]))
    rad_after = h3.add(h3.h(after[2]), h3.h(after[3]))
    assert h3.add(work, h3.sub(rad_after, rad_before)) == h3.ZERO
    memory = get(post_b, RX, MEMORY_Y, 2)
    return {
        "incoming_CORR": incoming,
        "B": tags.get((RX, 0), NO_TAG),
        "work_on_matter_H": work,
        "work_on_matter_Q": h3.scalar_account(work),
        "local_after_B": after,
        "memory_after_B": memory,
        "memory_delta": h3.sub(memory, REFERENCE),
    }


def follow(initial, horizon, cuts, crosscheck=False):
    state = initial
    account = ledger(initial)
    first_field = None
    first_active = None
    first_record = None
    records = {}
    events = []
    for tick in range(1, horizon + 1):
        bit = (tick - 1) % 2
        pre_b = move(state, bit)
        after, tags = collide(pre_b)
        assert ledger(pre_b) == ledger(after) == account
        pre_reverse, _ = collide(after)
        assert pre_reverse == pre_b and move(pre_reverse, bit, backward=True) == state
        if crosscheck and tick in (1, 2):
            assert transport(dense(state), NY, bit) == dense(pre_b)
            assert h3.collide(dense(pre_b), NY)[0] == dense(after)
            assert transport(dense(pre_b), NY, bit, backward=True) == dense(state)
        measurement = read(pre_b, after, tags)
        assert set(tags) <= {(RX, 0)}
        if first_field is None and measurement["incoming_CORR"] != h3.ZERO:
            first_field = tick
        if measurement["B"]:
            if first_active is None:
                first_active = tick
            events.append((tick, measurement["B"], measurement["work_on_matter_H"]))
        if first_record is None and measurement["memory_delta"] != h3.ZERO:
            first_record = tick
        if tick in cuts:
            records[str(tick)] = measurement
        state = after
    for tick in range(horizon, 0, -1):
        pre_b, _ = collide(state)
        state = move(pre_b, (tick - 1) % 2, backward=True)
    assert state == initial
    return {
        "account": account,
        "first_nonzero_CORR": first_field,
        "first_active_B": first_active,
        "first_memory_change": first_record,
        "cuts": records,
        "active_events": events,
        "full_state_restored": True,
    }


def run():
    fronts = []
    front_account = None
    for d in (1, 3):
        for kind in ("tuned", "detuned", "remote"):
            result = follow(front_launch(d, kind), 10, (d, d + 1, d + 2, 10), crosscheck=kind == "tuned")
            if front_account is None:
                front_account = result["account"]
            assert result["account"] == front_account
            first, delay, held = (result["cuts"][str(t)] for t in (d, d + 1, d + 2))
            result.update({
                "distance_bonds": d,
                "preparation": kind,
                "predeclared_tuned_contact_and_record": (
                    first["B"] == 1
                    and first["incoming_CORR"] == h3.scale(2, h3.mul(L3, h3.J))
                    and delay["memory_delta"] == h3.scale(-2, L)
                    and held["memory_delta"] == delay["memory_delta"]
                ),
            })
            fronts.append(result)
    packets = []
    packet_account = None
    for d in (20, 40, 60):
        result = follow(packet_launch(d), 80, (40, 80))
        if packet_account is None:
            packet_account = result["account"]
        assert result["account"] == packet_account
        result.update({
            "distance_cells": d,
            "preparation": "remote" if d == 60 else "translation",
        })
        packets.append(result)
    near = packets[0]["cuts"]["40"]["incoming_CORR"]
    far = packets[1]["cuts"]["80"]["incoming_CORR"]
    phase = None
    if near != h3.ZERO and far != h3.ZERO:
        phase = {"numerator": h3.mul(far, h3.conj(near)), "denominator": h3.h(near)}
    return {
        "fixed_detector_half_gap": L3,
        "memory_seed": REFERENCE,
        "fronts": fronts,
        "packets": packets,
        "packet_far_near_complex_ratio": phase,
    }
