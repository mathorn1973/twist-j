# SPDX-License-Identifier: Apache-2.0
"""Fixed-edge signed material currents and phase-code symmetry controls."""

from itertools import product

from native import cell, h3, ledger, put, reverse, step


NX = 16
NY = 8
TARGET_X = 2
ZERO = h3.ZERO
ONE = h3.ONE
J = h3.J
L = h3.sub(ONE, h3.RHO)
U = h3.add(h3.J_POWERS[1], h3.J_POWERS[4])
U_INV = h3.mul(h3.J_POWERS[1], h3.J_INV)
FOUR = h3.scale(4, ONE)
PHI = h3.scale(-1, h3.add(h3.RHO, h3.RHO_INV))
PROBE_H = h3.sub(h3.scale(72, ONE), h3.scale(4, PHI))
PAID = ZERO, ZERO, h3.add(h3.scale(1280, ONE), PROBE_H), 2700
BANDS = ((0, 1, 1), (4, -1, 3))
GEOMETRIES = {
    "near": (True, True),
    "far": (False, False),
    "first_only": (True, False),
    "second_only": (False, True),
}


def words(d, f=ZERO):
    return d, h3.scale(-1, d), f, h3.scale(-1, f)


def resident(phase_code, branch, n):
    unit = h3.mul(J, J) if branch == 1 else ONE
    return h3.scale(-phase_code * branch * n, unit)


def launch(availability, source_sign, phase_code):
    result = [ZERO] * (NX * NY * 4)
    units = (U, U_INV) if source_sign == -1 else (U_INV, U)
    for (y, branch, n), near in zip(BANDS, availability):
        primary_x = 0 if near else 12
        for x0, unit in zip((primary_x, 6), units):
            source = words(h3.mul(FOUR, unit), FOUR)
            for x, row in product((x0, x0 + 1), (y, y + 1)):
                put(result, NY, x, row, source)
        a = resident(phase_code, branch, n)
        for row, gap in zip((y - 1, y, y + 1, y + 2), (a, a, L, L)):
            put(result, NY, TARGET_X, row % NY, words(gap))
    return tuple(result)


def hermitian(rails):
    return h3.ring_sum(h3.h(rail) for rail in rails)


def material(field, y):
    return hermitian(cell(field, NY, TARGET_X, y)[:2])


def parity(a, b):
    return h3.even(h3.sub(a, b))


def trace(field):
    cuts = []
    for bit in (0, 1, 0):
        post_c, post_b, tags = step(field, NY, bit)
        h3.require(ledger(post_c) == ledger(post_b) == PAID, "paid signed-current fixture")
        cuts.append((post_c, post_b, tags))
        field = post_b
    return cuts


def full_inverse(cuts, original):
    recovered = cuts[-1][1]
    for bit in (0, 1, 0):
        recovered = tuple(reverse(recovered, NY, bit))
    h3.require(recovered == original, "terminal signed-current inverse")


def band_read(initial, cuts, near, y, branch, n, source_sign, phase_code):
    _, b1, tags1 = cuts[0]
    c2, b2, tags2 = cuts[1]
    c3, _, _ = cuts[2]
    receiver_y = y + 1
    incoming_branch = -source_sign
    v = J if incoming_branch == 1 else h3.J_INV
    source_x = 1 if near else 13
    source_tag = 2 if source_sign == -1 else 1
    source_corr = h3.scale(-4, v)
    corr = h3.scale(-2, h3.mul(L, v)) if near else ZERO
    loaded_gap = h3.mul(v, L) if near else L
    tag = 1 if incoming_branch == 1 else 2
    expected_tags = ((TARGET_X, receiver_y, tag),) if near else ()
    active = near and branch == incoming_branch
    a = resident(phase_code, branch, n)
    before = tuple(cell(b2, NY, TARGET_X, k)[:2] for k in (y, receiver_y))
    after = tuple(cell(c3, NY, TARGET_X, k)[:2] for k in (y, receiver_y))
    expected_receiver = loaded_gap
    if active:
        multiplier = (1 - phase_code * branch * n) // 2
        expected_receiver = h3.scale(multiplier, h3.mul(J, loaded_gap))
    expected_after = (
        words(h3.sub(h3.add(a, loaded_gap), expected_receiver))[:2],
        words(expected_receiver)[:2],
    )
    signed_h = h3.sub(material(c3, receiver_y), material(b2, receiver_y))
    source_loss_h = h3.sub(material(b2, y), material(c3, y))
    h3.require(source_loss_h == signed_h, "local C material edge closure")
    signed_q = h3.scalar_account(signed_h)
    expected_q = 0
    if active:
        expected_q = {
            (1, -1): 10,
            (1, 1): -10,
            (-1, -1): -10,
            (-1, 1): 20,
        }[(branch, phase_code)]
    scientific = {
        "source_emission": all(
            cell(b1, NY, source_x, row)[3] == source_corr and (source_x, row, source_tag) in tags1
            for row in (y, receiver_y)
        ),
        "incoming_words": all(
            cell(c2, NY, TARGET_X, row) == (*cell(initial, NY, TARGET_X, row)[:3], corr)
            for row in (y, receiver_y)
        ),
        "collision": tuple(
            event for event in tags2 if event[0] == TARGET_X and event[1] in (y, receiver_y)
        ) == expected_tags,
        "before_edge": before == (words(a)[:2], words(loaded_gap)[:2]),
        "parity": all(parity(left, right) == active for left, right in zip(*before)),
        "after_edge": after == expected_after,
        "signed_q": signed_q == expected_q,
    }
    return {
        "edge_from_to": (y, receiver_y),
        "selector": branch,
        "incident": near,
        "signed_H": signed_h,
        "signed_Q": signed_q,
        "expected_Q": expected_q,
        "checks": scientific,
    }


def flip_sector(field, sector):
    return tuple(
        h3.scale(-1, word) if index % 4 // 2 == sector else word
        for index, word in enumerate(field)
    )


def case(geometry, source_sign, phase_code):
    availability = GEOMETRIES[geometry]
    initial = launch(availability, source_sign, phase_code)
    h3.require(ledger(initial) == PAID, "complete initial signed-current accounts")
    cuts = trace(initial)
    full_inverse(cuts, initial)
    edges = [
        band_read(initial, cuts, near, y, branch, n, source_sign, phase_code)
        for (y, branch, n), near in zip(BANDS, availability)
    ]
    sign_controls = {}
    if geometry == "near":
        for sector, name in enumerate(("matter", "radiation")):
            flipped_initial = flip_sector(initial, sector)
            flipped = trace(flipped_initial)
            full_inverse(flipped, flipped_initial)
            sign_controls[name] = all(
                other_c == flip_sector(c, sector) and other_b == flip_sector(b, sector)
                and other_tags == tags
                for (c, b, tags), (other_c, other_b, other_tags) in zip(cuts, flipped)
            ) and [
                h3.sub(material(flipped[2][0], y + 1), material(flipped[1][1], y + 1))
                for y, _, _ in BANDS
            ] == [edge["signed_H"] for edge in edges]
    return {
        "geometry": geometry,
        "source_sign": source_sign,
        "phase_code": phase_code,
        "edges": edges,
        "unit_weight_sum_Q": sum(edge["signed_Q"] for edge in edges),
        "global_sign_flip_invariance": sign_controls,
        "passed": all(all(edge["checks"].values()) for edge in edges) and all(sign_controls.values()),
    }


def run():
    negative = launch(GEOMETRIES["near"], -1, -1)
    positive = launch(GEOMETRIES["near"], -1, 1)
    sitewise_match = all(h3.h(a) == h3.h(b) for a, b in zip(negative, positive))
    rows = [
        case(geometry, source_sign, phase_code)
        for geometry, source_sign, phase_code in product(GEOMETRIES, (-1, 1), (-1, 1))
    ]
    near = {(row["source_sign"], row["phase_code"]): row["unit_weight_sum_Q"]
            for row in rows if row["geometry"] == "near"}
    crossed_sign = all(value * source_sign * phase_code > 0
                       for (source_sign, phase_code), value in near.items())
    return {
        "passed": sitewise_match and crossed_sign and all(row["passed"] for row in rows),
        "sitewise_matched_initial_rail_H": sitewise_match,
        "probe_H": PROBE_H,
        "probe_Q": 140,
        "probe_nu_both_codes": -4,
        "product_sign_transport": crossed_sign,
        "rows": rows,
    }
