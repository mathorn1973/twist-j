# SPDX-License-Identifier: Apache-2.0
"""Exact same-history differential matter-gap phase under the native H3 law."""

from native import h3, transport


NX, NY = 128, 4
L = h3.sub(h3.ONE, h3.RHO)
RADII = (1, 2, 3, 4)
REFERENCES = (68, 73)
FREE_COLUMNS = (82, 91)
SIGNS = ((1, 1), (1, -1), (-1, 1), (-1, -1))


def power(a, n):
    result = h3.ONE
    for _ in range(n):
        result = h3.mul(result, a)
    return result


U = h3.scale(128, power(L, 8))


def source(d):
    return h3.scale(2 ** (d + 8), h3.mul(power(L, 8 - d), h3.J))


def get(state, x, y, r):
    return state.get((x % NX, y % NY, r), h3.ZERO)


def put(state, key, word):
    if word != h3.ZERO:
        state[key] = word
    else:
        state.pop(key, None)


def move(state, bit, backward=False):
    out = state.copy()
    for x, y, r in state:
        if r == 3:
            a = ((x - (x - bit) % 2) % NX, y, r)
            b = ((a[0] + 1) % NX, y, r)
        else:
            a = (x, (y - (y - bit) % 2) % NY, r)
            b = (x, (a[1] + 1) % NY, r)
        if (x, y, r) != b or a not in state:
            av, bv = h3.transport_pair(state.get(a, h3.ZERO), state.get(b, h3.ZERO), backward)
            put(out, a, av)
            put(out, b, bv)
    return out


def cell(state, x, y):
    return tuple(get(state, x, y, r) for r in range(4))


def collide(state):
    out = state.copy()
    tags = {}
    for x, y in {(x, y) for x, y, r in state if r < 2}:
        result, tag = h3.collision(cell(state, x, y))
        if tag:
            tags[x, y] = tag
            for r, word in enumerate(result):
                put(out, (x, y, r), word)
    return out, tags


def dense(state):
    field = [h3.ZERO] * (NX * NY * 4)
    for (x, y, r), word in state.items():
        field[h3.index(NY, x, y, r)] = word
    return tuple(field)


def ledger(state):
    m = h3.ring_sum(w for (_, _, r), w in state.items() if r < 2)
    u = h3.ring_sum(w for (_, _, r), w in state.items() if r >= 2)
    h = h3.ring_sum(h3.h(w) for w in state.values())
    return m, u, h, h3.scalar_account(h)


def launch(r, mode, source_sign, probe_sign, control):
    state = {}
    probes = (r, 2 * r) if control != "free_path" else FREE_COLUMNS
    for x in probes + REFERENCES:
        for y in range(NY):
            state[x, y, 0] = h3.scale(probe_sign, U)
            state[x, y, 1] = h3.scale(-probe_sign, U)
    selected = 1 if mode == "fixed" else 2 * r
    for i, d in enumerate((1, 2, 4, 6, 8)):
        parked = 36 + 2 * i
        word = source(d)
        if d == selected:
            word = h3.scale(source_sign, word)
            x = parked if control == "parked_source" else 0
        else:
            x = parked
        state[x, 0, 3] = word
        state[parked + 1, 0, 3] = h3.scale(-1, word)
    return state


def gap(local):
    return h3.half(h3.sub(local[0], local[1]))


def sign(n):
    return (n > 0) - (n < 0)


def phi_sign(a, b):
    """Exact sign of a+b*(1+sqrt(5))/2."""
    c = 2 * a + b
    if c == 0 or b == 0 or sign(c) == sign(b):
        return sign(c or b)
    return sign(c) * sign(c * c - 5 * b * b)


def phase(word):
    if word is None or word == h3.ZERO:
        return None
    a, b, c, d = word
    return (
        (phi_sign(2 * a - b, b - c - d), phi_sign(c - d, b)),
        (phi_sign(2 * a - c - d, -b + c + d), phi_sign(b, d - c)),
    )


def product_phase(a, b):
    if not a or not b or a == h3.ZERO or b == h3.ZERO:
        return None
    return h3.mul(a, h3.conj(b))


def phase_identity(word):
    return phase(word) == ((1, 0), (1, 0))


def has_angle(word):
    return phase(word) not in (None, ((1, 0), (1, 0)))


def receiver(pre, post, x, ref, tags):
    a, b = cell(pre, x, 0), cell(post, x, 0)
    ref_word = gap(cell(post, ref, 0))
    m_pre, m_post = gap(a), gap(b)
    p_pre, p_post = product_phase(m_pre, ref_word), product_phase(m_post, ref_word)
    local_deltas = [h3.sub(h3.h(v), h3.h(u)) for u, v in zip(a, b)]
    assert h3.ring_sum(local_deltas) == h3.ZERO
    work = h3.add(local_deltas[0], local_deltas[1])
    return {
        "gap_pre_B": m_pre, "gap_post_B": m_post,
        "phase_numerator_pre_B": p_pre, "phase_numerator_post_B": p_post,
        "phase_signs_pre_B": phase(p_pre), "phase_signs_post_B": phase(p_post),
        "CORR_pre_B": a[3], "CORR_post_B": b[3],
        "B": tags.get((x, 0), 0), "work_H": work, "work_Q": h3.scalar_account(work),
    }


def follow(r, mode, source_sign, probe_sign, control):
    initial = launch(r, mode, source_sign, probe_sign, control)
    state = initial
    paid = ledger(initial)
    cuts = []
    first = [None, None]
    events = []
    for tick in range(1, 4 * r + 1):
        bit = (tick - 1) % 2
        pre = move(state, bit)
        post, tags = collide(pre)
        assert ledger(pre) == ledger(post) == paid
        undo, _ = collide(post)
        assert undo == pre and move(undo, bit, backward=True) == state
        if (r, mode, source_sign, probe_sign, control) == (1, "fixed", 1, 1, "loaded"):
            assert transport(dense(state), NY, bit) == dense(pre)
            assert h3.collide(dense(pre), NY)[0] == dense(post)
        for x in REFERENCES:
            assert cell(post, x, 0) == cell(initial, x, 0)
        receivers = [receiver(pre, post, x, ref, tags) for x, ref in zip((r, 2 * r), REFERENCES)]
        for i, row in enumerate(receivers):
            if first[i] is None and row["CORR_pre_B"] != h3.ZERO:
                first[i] = tick
        cuts.append({"tick": tick, "near": receivers[0], "far": receivers[1]})
        events.extend((tick, x, y, tag) for (x, y), tag in sorted(tags.items()))
        state = post
    for tick in range(4 * r, 0, -1):
        state, _ = collide(state)
        state = move(state, (tick - 1) % 2, backward=True)
    assert state == initial
    return paid, {"first_fields": first, "cuts": cuts, "B_events": events, "inverse_restored": True}


def summarize(loaded, null, free, tick):
    ends, reference, free_ends = (arm["cuts"][tick - 1] for arm in (loaded, null, free))
    near, far = (
        product_phase(ends[key]["phase_numerator_post_B"], reference[key]["phase_numerator_post_B"])
        for key in ("near", "far")
    )
    differential = product_phase(near, far)
    doubled_far = None if far is None else h3.mul(far, far)
    inverse_r_residual = product_phase(near, doubled_far)
    first_departure = [
        next((
            a["tick"] for a, b in zip(loaded["cuts"][:tick], free["cuts"][:tick])
            if a[k]["CORR_pre_B"] != b[k]["CORR_pre_B"]
        ), None)
        for k in ("near", "far")
    ]
    return {
        "near_null_corrected_phase_word": near, "far_null_corrected_phase_word": far,
        "near_minus_far_phase_word": differential, "near_minus_far_signs": phase(differential),
        "near_has_nonzero_phase": has_angle(near), "far_has_nonzero_phase": has_angle(far),
        "inverse_r_phase_only_relation_modulo_turn": phase_identity(inverse_r_residual),
        "inverse_r_phase_relation_nondegenerate": has_angle(near) and has_angle(far) and phase_identity(inverse_r_residual),
        "loaded_minus_free_endpoint_CORR": [h3.sub(ends[k]["CORR_pre_B"], free_ends[k]["CORR_pre_B"]) for k in ("near", "far")],
        "loaded_over_free_endpoint_CORR": [
            (h3.mul(ends[k]["CORR_pre_B"], h3.conj(free_ends[k]["CORR_pre_B"])), h3.h(free_ends[k]["CORR_pre_B"]))
            if free_ends[k]["CORR_pre_B"] != h3.ZERO else None
            for k in ("near", "far")
        ],
        "first_loaded_free_field_departure": first_departure,
        "loaded_free_pre_B_field_agrees_through_hold": all(t is None for t in first_departure),
    }


def hold_increment(early, late):
    near, far = (
        product_phase(late[f"{where}_null_corrected_phase_word"], early[f"{where}_null_corrected_phase_word"])
        for where in ("near", "far")
    )
    delta = product_phase(near, far)
    doubled_far = None if far is None else h3.mul(far, far)
    return {
        "near_increment_word": near, "far_increment_word": far, "near_minus_far_phase_word": delta,
        "near_increment_signs": phase(near), "far_increment_signs": phase(far),
        "near_minus_far_signs": phase(delta),
        "inverse_r_increment_relation_nondegenerate": has_angle(near) and has_angle(far)
        and phase_identity(product_phase(near, doubled_far)),
    }


def same_phase(a, b):
    return phase_identity(product_phase(a, b))


def opposite_phase(a, b):
    return b is not None and has_angle(a) and not same_phase(a, b) and same_phase(a, h3.conj(b))


def cross_signs(results, key):
    words_by_sign = {(r["source_sign"], r["probe_sign"]): r[key]["near_minus_far_phase_word"] for r in results}
    pp, pm, mp, mm = (words_by_sign[k] for k in SIGNS)
    return {
        "source_even": same_phase(pp, mp) and same_phase(pm, mm),
        "probe_even": same_phase(pp, pm) and same_phase(mp, mm),
        "source_odd_nondegenerate": opposite_phase(pp, mp) and opposite_phase(pm, mm),
        "probe_odd_nondegenerate": opposite_phase(pp, pm) and opposite_phase(mp, mm),
    }


def run():
    bundles = []
    paid = None
    for mode in ("fixed", "far_calibrated"):
        for r in RADII:
            results = []
            for s, p in SIGNS:
                histories = []
                for control in ("loaded", "parked_source", "free_path"):
                    stock, arm = follow(r, mode, s, p, control)
                    if paid is None:
                        paid = stock
                    assert stock == paid
                    histories.append(arm)
                early = summarize(*histories, 2 * r)
                late = summarize(*histories, 4 * r)
                results.append({
                    "source_sign": s, "probe_sign": p,
                    "endpoint_2r": early, "endpoint_4r": late, "increment_2r_to_4r": hold_increment(early, late),
                    "loaded": histories[0], "parked_source": histories[1], "free_path": histories[2],
                })
            bundles.append({
                "mode": mode, "r": r, "hold": 2 * r, "total_ticks": 4 * r, "arms": results,
                "cross_signs": {k: cross_signs(results, k) for k in ("endpoint_2r", "endpoint_4r", "increment_2r_to_4r")},
            })
    return {"initial_account_common_to_all_arms": paid, "unsigned_gap": U, "bundles": bundles}
