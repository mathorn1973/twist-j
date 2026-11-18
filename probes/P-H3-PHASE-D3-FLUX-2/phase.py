# SPDX-License-Identifier: Apache-2.0
"""Remote phase reads under the pinned native H3 law."""

from native import h3, transport


NX, NY, RX, REF_X = 80, 4, 1, 65
L = h3.sub(h3.ONE, h3.RHO)
PHI = h3.scale(-1, h3.add(h3.RHO, h3.RHO_INV))
HORIZON = 8


def power(word, n):
    result = h3.ONE
    for _ in range(n):
        result = h3.mul(result, word)
    return result


U = h3.scale(2, power(L, 5))
REFERENCE = U


def get(state, x, y, rail):
    return state.get((x % NX, y % NY, rail), h3.ZERO)


def put(state, key, word):
    if word != h3.ZERO:
        state[key] = word
    else:
        state.pop(key, None)


def move(state, bit, backward=False):
    out = state.copy()
    for x, y, rail in state:
        if rail == 3:
            a = ((x - ((x - bit) % 2)) % NX, y, rail)
            b = ((a[0] + 1) % NX, y, rail)
        else:
            a = (x, (y - ((y - bit) % 2)) % NY, rail)
            b = (x, (a[1] + 1) % NY, rail)
        if (x, y, rail) != b or a not in state:
            v, w = h3.transport_pair(state.get(a, h3.ZERO), state.get(b, h3.ZERO), backward)
            put(out, a, v)
            put(out, b, w)
    return out


def collide(state):
    out = state.copy()
    tags = {}
    sites = {(x, y) for x, y, r in state if r < 2}
    for x, y in sites:
        result, tag = h3.collision(tuple(get(state, x, y, r) for r in range(4)))
        if tag:
            tags[x, y] = tag
            for rail, word in enumerate(result):
                put(out, (x, y, rail), word)
    return out, tags


def dense(state):
    field = [h3.ZERO] * (NX * NY * 4)
    for (x, y, r), word in state.items():
        field[h3.index(NY, x, y, r)] = word
    return tuple(field)


def account(state):
    m = h3.ring_sum(word for (_, _, r), word in state.items() if r < 2)
    u = h3.ring_sum(word for (_, _, r), word in state.items() if r >= 2)
    h = h3.ring_sum(h3.h(word) for word in state.values())
    return m, u, h, h3.scalar_account(h)


def direction(distance):
    return 1 if distance % 2 else -1


def source_word(distance, k):
    base = h3.mul(power(L, 5 - distance), h3.J)
    return h3.scale(2 ** (distance + 2), h3.mul(base, power(h3.RHO, k)))


def apparatus(mode):
    d = U if mode == "coherent" else h3.mul(U, L)
    bias = h3.ZERO if mode == "coherent" else h3.scale(2, h3.mul(U, h3.J))
    state = {}
    for y in range(NY):
        state[RX, y, 0] = d
        state[RX, y, 1] = h3.scale(-1, d)
        put(state, (RX, y, 2), bias)
        state[REF_X, y, 2] = REFERENCE
    return state, bias


def launch(mode, distance, k):
    state, bias = apparatus(mode)
    for d in range(1, 6):
        active = d == distance
        word = source_word(d, k if active else 0)
        parked = 30 + 2 * (d - 1)
        x = (RX - direction(d) * d) % NX if active else parked
        state[x, 0, 3] = word
        state[parked + 1, 0, 3] = h3.scale(-1, word)
    return state, bias


def on_site_work(before, after):
    changes = [
        h3.sub(h3.h(get(after, RX, 0, r)), h3.h(get(before, RX, 0, r))) for r in range(4)
    ]
    assert h3.ring_sum(changes) == h3.ZERO
    return h3.add(*changes[:2])


def ratio(top, base):
    return h3.mul(top, h3.conj(base)), h3.h(base)


def expected_delta(mode, k):
    turn = power(h3.RHO, k)
    if mode == "coherent":
        return 1, h3.mul(U, h3.mul(h3.RHO, turn))
    if k in (1, 4):
        return 1, h3.mul(U, h3.mul(h3.RHO, h3.sub(turn, h3.ONE)))
    return 0, h3.ZERO


def follow(mode, distance, k):
    initial, bias = launch(mode, distance, k)
    current = initial
    paid = account(initial)
    first_arrival = None
    active = []
    front_checks = []
    read = {}
    reference_valid = True
    for t in range(1, HORIZON + 1):
        bit = (t - 1) % 2
        pre_b = move(current, bit)
        post_b, tags = collide(pre_b)
        assert account(pre_b) == account(post_b) == paid
        unb, _ = collide(post_b)
        assert unb == pre_b and move(unb, bit, backward=True) == current
        if distance == 1 and k == 0 and t in (1, 2):
            assert transport(dense(current), NY, bit) == dense(pre_b)
            assert h3.collide(dense(pre_b), NY)[0] == dense(post_b)
        for y in range(NY):
            reference_valid &= get(post_b, REF_X, y, 2) == REFERENCE
        for (_, y), tag in sorted(tags.items()):
            active.append((t, y, tag))
        incoming = get(pre_b, RX, 0, 3)
        if incoming != h3.ZERO and first_arrival is None:
            first_arrival = t
        if distance and t <= distance:
            x = RX - direction(distance) * (distance - t)
            previous = get(current, x - direction(distance), 0, 3)
            observed = get(pre_b, x, 0, 3)
            front_checks.append(previous != h3.ZERO and h3.scale(2, observed) == h3.mul(L, previous))
        if t == distance:
            delta = h3.sub(get(post_b, RX, 0, 2), bias)
            tag = tags.get((RX, 0), 0)
            work = on_site_work(pre_b, post_b)
            expected_tag, expected = expected_delta(mode, k)
            read.update({
                "incoming": incoming, "B": tag,
                "CORR_after_B": get(post_b, RX, 0, 3),
                "matter_r0_after_B": get(post_b, RX, 0, 0),
                "work_H": work, "work_Q": h3.scalar_account(work),
                "incoming_over_reference": ratio(incoming, REFERENCE),
                "CLK_delta_over_reference": ratio(delta, REFERENCE),
                "contact_matches": tag == expected_tag and delta == expected,
                "incoming_matches": incoming == h3.scale(2, h3.mul(h3.mul(U, h3.J), power(h3.RHO, k))),
            })
        if distance and t == distance + 1:
            y = NY - 1 if distance % 2 else 1
            delta = h3.sub(get(pre_b, RX, y, 2), bias)
            final_delta = h3.sub(get(post_b, RX, y, 2), bias)
            _, expected = expected_delta(mode, k)
            read.update({
                "readout_row": y,
                "separate_CLK_delta_over_reference_pre_B": ratio(delta, REFERENCE),
                "separate_CLK_delta_over_reference_post_B": ratio(final_delta, REFERENCE),
                "separate_transfer_matches": h3.scale(2, delta) == h3.mul(L, expected),
                "separate_record_survives_that_B": delta != h3.ZERO and final_delta == delta,
            })
        current = post_b
    for t in range(HORIZON, 0, -1):
        unb, _ = collide(current)
        current = move(unb, (t - 1) % 2, backward=True)
    assert current == initial
    return paid, {
        "distance": distance, "rotation_exponent": k if distance else None,
        "arrival_tick": first_arrival, "B_events": active, "front_multiplier_checks": front_checks,
        "reference_unchanged": reference_valid, "complete_inverse_restored": True, **read,
    }


def local_and_free_phase():
    a, b = h3.transport_pair(h3.scale(2, h3.ONE), h3.ZERO, backward=False)
    c, d = h3.transport_pair(h3.scale(2, h3.ONE), h3.scale(2, h3.J), backward=False)
    assert h3.add(a, b) == h3.scale(2, h3.ONE)
    return {
        "native_C_output_full_gap": h3.sub(a, b),
        "native_C_input_half_gap": h3.ONE,
        "native_C_output_half_gap": h3.half(h3.sub(a, b)),
        "front_multiplier": [L, 2],
        "mixed_pair_same_first_input_output": [c, d],
        "front_modulus_squared": [h3.h(L), 4],
        "staggered_free_eigenphase_cosines_q0_qpi_over_2_qpi": [
            [h3.ONE, 1], [h3.sub(h3.scale(2, h3.ONE), PHI), 4], [h3.scale(-1, PHI), 2]
        ],
    }


def run():
    modes = {}
    for mode in ("coherent", "biased"):
        paid, null = follow(mode, 0, 0)
        rows = []
        for d in range(1, 6):
            for k in range(5):
                account_now, row = follow(mode, d, k)
                assert account_now == paid
                rows.append(row)
        modes[mode] = {"account": paid, "rows": rows, "remote": null}
    return {"local_and_free_phases": local_and_free_phase(), "reference_word": REFERENCE, "modes": modes}
