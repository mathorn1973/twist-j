# SPDX-License-Identifier: Apache-2.0
"""Exact directed material current for a finite, matched H3 preparation."""

from itertools import product

from native import cell, h3, ledger, put, reverse, step


NY = 8
NX = 16
TARGET_X = 2
ANCHOR_X = 10
ROWS = (NY - 1, 0, 1, 2)
ZERO = h3.ZERO
ONE = h3.ONE
RHO = h3.RHO
J = h3.J
L = h3.sub(ONE, RHO)
U = h3.add(h3.J_POWERS[1], h3.J_POWERS[4])
U_INV = h3.mul(h3.J_POWERS[1], h3.J_INV)
FOUR = h3.scale(4, ONE)
PAID_LEDGER = ZERO, ZERO, h3.scale(840, ONE), 1680


def antipodal(gap, field=ZERO):
    return gap, h3.scale(-1, gap), field, h3.scale(-1, field)


def reflect_row(y, orientation):
    return y if orientation == 1 else (1 - y) % NY


def packet(test_sign):
    high, low = h3.scale(3, h3.mul(J, L)), L
    if test_sign == 1:
        high, low = h3.mul(U_INV, high), h3.mul(U, low)
    return high, high, low, low


def launch(orientation, geometry, source_sign, test_sign):
    field = [ZERO] * (NX * NY * 4)
    primary, compensation = (0, 6) if geometry == "near" else (6, 12)
    units = (U, U_INV) if source_sign == -1 else (U_INV, U)
    for x0, unit in zip((primary, compensation), units):
        for x, y in product((x0, x0 + 1), (0, 1)):
            put(field, NY, x, y, antipodal(h3.mul(FOUR, unit), FOUR))
    for x, sign in ((TARGET_X, test_sign), (ANCHOR_X, -test_sign)):
        for y, gap in zip(ROWS, packet(sign)):
            put(field, NY, x, reflect_row(y, orientation), antipodal(gap))
    return tuple(field)


def hermitian(words):
    return h3.ring_sum(h3.h(word) for word in words)


def material(field, y):
    return hermitian(cell(field, NY, TARGET_X, y)[:2])


def oriented_edge_change(before, after):
    return h3.sub(material(after, 1), material(before, 1))


def continuity(before, post_c, post_b, bit):
    """Audit transport edge closure and distinguish sitewise material work."""
    material_changes = []
    work_terms = []
    for x, y in product(range(NX), range(NY)):
        saved = cell(before, NY, x, y)
        transported = cell(post_c, NY, x, y)
        collided = cell(post_b, NY, x, y)
        h3.require(hermitian(transported) == hermitian(collided), "B site Hermitian closure")
        work = h3.sub(hermitian(collided[:2]), hermitian(transported[:2]))
        field_work = h3.sub(hermitian(collided[2:]), hermitian(transported[2:]))
        h3.require(h3.add(work, field_work) == ZERO, "opposite site B work")
        if x == TARGET_X:
            material_changes.append(h3.sub(hermitian(transported[:2]), hermitian(saved[:2])))
            work_terms.append(work)
    for x, y in product(range(NX), range(bit, NY, 2)):
        other_y = (y + 1) % NY
        for rail in (0, 1):
            incoming = (cell(before, NY, x, y)[rail], cell(before, NY, x, other_y)[rail])
            outgoing = (cell(post_c, NY, x, y)[rail], cell(post_c, NY, x, other_y)[rail])
            h3.require(hermitian(incoming) == hermitian(outgoing), "C material edge closure")
    h3.require(h3.ring_sum(material_changes) == ZERO, "C column material closure")
    total_change = h3.ring_sum(
        h3.sub(material(post_b, y), material(before, y)) for y in range(NY)
    )
    h3.require(total_change == h3.ring_sum(work_terms), "column material continuity")


def case(orientation, geometry, source_sign, test_sign):
    initial = launch(orientation, geometry, source_sign, test_sign)
    old = initial
    cuts = []
    for bit in (0, 1, 0):
        post_c, post_b, tags = step(old, NY, bit)
        continuity(old, post_c, post_b, bit)
        h3.require(ledger(old) == ledger(post_c) == ledger(post_b) == PAID_LEDGER, "paid fixture")
        cuts.append((post_c, post_b, tags))
        old = post_b
    for bit in (0, 1, 0):
        old = tuple(reverse(old, NY, bit))
    h3.require(old == initial, "terminal inverse")

    c1, b1, tags1 = cuts[0]
    c2, b2, tags2 = cuts[1]
    c3, _, _ = cuts[2]
    measured_y = reflect_row(1, orientation)
    other_y = reflect_row(0, orientation)
    v = J if source_sign == -1 else h3.J_INV
    source_x = 1 if geometry == "near" else 7
    expected_source_tag = 2 if source_sign == -1 else 1
    expected_source_corr = h3.scale(-4, v)
    expected_corr = h3.scale(-2, h3.mul(L, v)) if geometry == "near" else ZERO
    expected_tag = 0
    if geometry == "near" and test_sign == -1:
        expected_tag = 1 if source_sign == -1 else 2
    expected_tags = ((TARGET_X, measured_y, expected_tag),) if expected_tag else ()
    measured_tags = tuple(tag for tag in tags2 if tag[0] == TARGET_X)
    active = expected_tag == 1
    edge_before = tuple(cell(b2, NY, TARGET_X, y)[:2] for y in (other_y, measured_y))
    edge_after = tuple(cell(c3, NY, TARGET_X, y)[:2] for y in (other_y, measured_y))
    expected_edge = edge_before
    if active:
        active_gap = h3.mul(J, L)
        two = h3.scale(2, ONE)
        expected_edge = (
            antipodal(h3.mul(h3.add(two, RHO), active_gap))[:2],
            antipodal(h3.mul(h3.sub(two, RHO), active_gap))[:2],
        )
    expected_flux_q = orientation * 40 if active else 0
    flux_h = oriented_edge_change(b2, c3)
    flux_q = h3.scalar_account(flux_h)
    case_checks = {
        "quiet_target_through_1B": all(
            cell(cut, NY, TARGET_X, y) == cell(initial, NY, TARGET_X, y)
            for cut, y in product((c1, b1), range(NY))
        ),
        "source_emission": all(
            cell(b1, NY, source_x, y)[3] == expected_source_corr
            and (source_x, y, expected_source_tag) in tags1
            for y in (0, 1)
        ),
        "target_2C": all(
            cell(c2, NY, TARGET_X, y) == (
                *cell(initial, NY, TARGET_X, y)[:3],
                expected_corr if y in (0, 1) else ZERO,
            )
            for y in range(NY)
        ),
        "target_2B_tags": measured_tags == expected_tags,
        "target_3C_edge_parity": all(
            h3.even(h3.sub(left, right)) == active for left, right in zip(*edge_before)
        ),
        "target_3C_edge_words": edge_after == expected_edge,
        "edge_H_and_Q": flux_h == h3.scale(expected_flux_q // 2, ONE) and flux_q == expected_flux_q,
    }
    return {
        "orientation": orientation,
        "geometry": geometry,
        "source_sign": source_sign,
        "test_sign": test_sign,
        "target_2B_tags": measured_tags,
        "flux_h": flux_h,
        "flux_q": flux_q,
        "expected_flux_q": expected_flux_q,
        "checks": case_checks,
    }


def run():
    rows = [
        case(orientation, geometry, source_sign, test_sign)
        for orientation, geometry, source_sign, test_sign in product(
            (1, -1), ("near", "far"), (-1, 1), (-1, 1)
        )
    ]
    reflection = all(
        row["flux_h"] == h3.scale(-1, mirror["flux_h"])
        and row["flux_q"] == -mirror["flux_q"]
        for row, mirror in zip(rows[:8], rows[8:])
    )
    return {
        "passed": reflection and all(all(row["checks"].values()) for row in rows),
        "reflection": reflection,
        "rows": rows,
    }
