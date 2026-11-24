# SPDX-License-Identifier: Apache-2.0
"""Five referenced phase comparisons under one unchanged native H3 tick."""

from native import cell, empty, h3, ix, ledger, put, reverse, step


ZERO, ONE = h3.ZERO, h3.ONE
J, RHO, THETA = h3.J, h3.RHO, h3.T
RHO_POWERS = tuple(h3.J_POWERS[2 * k % 5] for k in range(5))
FIELD_GAP = h3.scale(2, J)
CENTERS = (RHO_POWERS[2], h3.scale(-1, RHO_POWERS[2]), ONE)
PHASE_NORMS = ((4, 0, 0, 0), (7, 0, 1, 1), (5, 0, 2, 2), (3, 0, -2, -2), (1, 0, -1, -1))
NORM_TRACES = (8, 13, 8, 8, 3)
BIT = 0


def build(k, center):
    field = empty()
    for x in range(8):
        if x < 5:
            reference = h3.scale(2, RHO_POWERS[x])
            signal = h3.scale(2, RHO_POWERS[k])
            reader = h3.add(center, reference), h3.sub(center, reference)
            opposite = h3.scale(-1, center)
            donor = h3.add(opposite, signal), h3.sub(opposite, signal)
        else:
            reader = donor = ZERO, ZERO
        put(field, x, 0, (*reader, FIELD_GAP, h3.scale(-1, FIELD_GAP)))
        put(field, x, 1, (*donor, FIELD_GAP, h3.scale(-1, FIELD_GAP)))
    return field


def rotate_matter(field, unit):
    result = list(field)
    for x in range(8):
        for y in range(4):
            for lane in range(2):
                offset = ix(x, y, lane)
                result[offset] = h3.mul(unit, field[offset])
    return tuple(result)


def gaps(values):
    r0, r2, clk, corr = values
    return h3.half(h3.sub(r0, r2)), h3.half(h3.sub(clk, corr))


def phase_norm(delta):
    powers = RHO_POWERS
    cross = h3.mul(h3.sub(powers[-1], RHO),
                   h3.sub(powers[delta % 5], powers[-delta % 5]))
    return h3.add(h3.scale(4, ONE), cross)


def check_kick(before, after):
    rho_theta = h3.mul(RHO, THETA)
    d, f = gaps(before)
    dn, fn = gaps(after)
    h3.require(all(gap != ZERO for gap in (d, f, dn, fn)), "active gaps nonzero")
    h3.require(h3.mul(d, f) == h3.mul(dn, fn), "B conserves gap product")
    h3.require(h3.mul(dn, f) == h3.mul(rho_theta, h3.mul(d, fn)),
               "B1 relative gap multiplier")
    restored, tag = h3.collision(after)
    h3.require(tuple(restored) == tuple(before) and tag == 2, "exact reverse B2")
    dr, fr = gaps(restored)
    h3.require(h3.mul(dr, fn) == h3.mul(h3.mul(h3.J_INV, h3.J_INV), h3.mul(dn, fr)),
               "B2 inverse relative gap multiplier")


def check_trajectory(field, k, center, unit, expected_ledger):
    tc, tb, events = step(field, BIT)
    h3.require(all(ledger(cut) == expected_ledger for cut in (field, tc, tb)),
               ("phase ledger", k, center, unit))
    h3.require(tuple(reverse(tb, BIT)) == tuple(field), ("phase inverse", k, center, unit))
    reader_events = tuple((x, tag) for x, y, tag in events if x < 5 and y == 0)
    h3.require(reader_events == ((k, 1),), ("unique active reader", k, center, unit))

    norms = []
    for ref in range(5):
        reader, donor = cell(field, ref, 0), cell(field, ref, 1)
        h3.require(all(h3.even(h3.sub(reader[lane], donor[lane]))
                       for lane in range(2)), ("both material contacts admit", ref, k))
        pre_b = cell(tc, ref, 0)
        post_b = cell(tb, ref, 0)
        d, f = gaps(pre_b)
        expected_gap = h3.add(h3.mul(J, RHO_POWERS[ref]),
                              h3.mul(h3.sub(ONE, RHO), RHO_POWERS[k]))
        h3.require(d == h3.mul(unit, expected_gap), ("exact read gap", ref, k))
        h3.require(h3.half(h3.add(*pre_b[:2])) == h3.mul(unit, h3.mul(RHO, center)),
                   ("exact transported center", ref, k))
        h3.require(f == FIELD_GAP and tuple(pre_b[2:]) == (FIELD_GAP, h3.scale(-1, FIELD_GAP)), ("fixed field rails", ref, k))
        h3.require(h3.h(d) == phase_norm(k - ref), ("phase cross-term", ref, k))
        h3.require((pre_b[:2] != post_b[:2]) == (ref == k), ("actual material write", ref, k))
        if ref == k:
            check_kick(pre_b, post_b)
        norms.append(h3.h(d))
    return tuple(tc), tuple(tb), events, tuple(norms)


def run():
    norms = tuple(phase_norm(k) for k in range(5))
    h3.require(norms == PHASE_NORMS and len(set(norms)) == 5, "distinct exact phase norms")
    h3.require(tuple(map(h3.scalar_account, norms)) == NORM_TRACES, "rational trace control")
    quadratic = h3.add(h3.scale(100, ONE), h3.scale(128, THETA))
    expected_ledger = ZERO, ZERO, quadratic, h3.scalar_account(quadratic)
    units = (*RHO_POWERS, *(h3.scale(-1, a) for a in RHO_POWERS))
    norm_matrix = []
    for k in range(5):
        for center in CENTERS:
            launch = build(k, center)
            post_c, post_b, events, row = check_trajectory(launch, k, center, ONE, expected_ledger)
            if center == CENTERS[0]:
                norm_matrix.append(row)
            else:
                h3.require(row == norm_matrix[k], ("center/phase differential equality", k, center))
            for unit in units[1:]:
                rotated = rotate_matter(launch, unit)
                rc, rb, re, rr = check_trajectory(rotated, k, center, unit, expected_ledger)
                h3.require(rc == rotate_matter(post_c, unit) and rb == rotate_matter(post_b, unit),
                           ("complete common matter rotation equivariance", k, center, unit))
                h3.require(re == events and rr == row, ("rotation preserves tags and norms", k, center, unit))
    return {
        "centers": CENTERS,
        "unit_rotations_including_identity": len(units),
        "launches": len(CENTERS) * 5 * len(units),
        "ledger": expected_ledger,
        "norm_by_relative_phase": norms,
        "rational_trace_by_relative_phase": NORM_TRACES,
        "reader_norms_by_signal_code": norm_matrix,
        "unique_B1_reader_by_signal_code": tuple(range(5)),
    }
