# SPDX-License-Identifier: Apache-2.0
"""Exact balanced material-current prediction in the coupled H3 fixture."""

from itertools import product

from native import cell, h3, ledger, put, reverse, step


NX, NY = 16, 8
TARGET = 2
ZERO, ONE, J = h3.ZERO, h3.ONE, h3.J
RHO = h3.RHO
L = h3.sub(ONE, RHO)
A = h3.sub(ONE, h3.scale(2, RHO))
U = h3.add(h3.J_POWERS[1], h3.J_POWERS[4])
U_INV = h3.mul(h3.J_POWERS[1], h3.J_INV)
FOUR = h3.scale(4, ONE)
PHI = h3.scale(-1, h3.add(RHO, h3.RHO_INV))
PAID = ZERO, ZERO, h3.add(h3.scale(1336, ONE), h3.scale(4, PHI)), 2676


def antipodal(d, f=ZERO):
    return d, h3.scale(-1, d), f, h3.scale(-1, f)


def launch(incident, q, p):
    field = [ZERO] * (NX * NY * 4)
    units = (U, U_INV) if q == -1 else (U_INV, U)
    primary = 0 if incident else 12
    for row, a in ((0, h3.scale(-p, h3.mul(J, J))), (4, h3.scale(p, A))):
        for x0, unit in zip((primary, 6), units):
            payload = antipodal(h3.mul(FOUR, unit), FOUR)
            for x, y in product((x0, x0 + 1), (row, row + 1)):
                put(field, NY, x, y, payload)
        for y, gap in zip((row - 1, row, row + 1, row + 2), (a, a, L, L)):
            put(field, NY, TARGET, y % NY, antipodal(gap))
    return tuple(field)


def matter_h(field, row):
    return h3.ring_sum(h3.h(a) for a in cell(field, NY, TARGET, row)[:2])


def case(incident, q, p):
    initial = launch(incident, q, p)
    h3.require(ledger(initial) == PAID, "balanced signed-current initial ledger")
    _, b1, _ = step(initial, NY, 0)
    c2, b2, tags = step(b1, NY, 1)
    c3, b3, _ = step(b2, NY, 0)
    recovered = reverse(reverse(reverse(b3, NY, 0), NY, 1), NY, 0)
    h3.require(recovered == initial, "balanced signed-current terminal inverse")
    v = J if q == -1 else h3.J_INV
    incoming = h3.scale(-2, h3.mul(L, v)) if incident else ZERO
    target_tags = tuple(tag for tag in tags if tag[0] == TARGET)
    expected_tags = (
        tuple((TARGET, row, 1 if q == -1 else 2) for row in (1, 5))
        if incident else ()
    )
    c2_exact = all(
        cell(c2, NY, TARGET, y)
        == (*cell(initial, NY, TARGET, y)[:3], incoming if y in (0, 1, 4, 5) else ZERO)
        for y in range(NY)
    )
    edge_q = []
    for row in (0, 4):
        gain = h3.sub(matter_h(c3, row + 1), matter_h(b2, row + 1))
        loss = h3.sub(matter_h(b2, row), matter_h(c3, row))
        h3.require(gain == loss, "balanced signed-current edge closure")
        edge_q.append(h3.scalar_account(gain))
    total = 10 * q * p if incident else 0
    expected_edge_q = [total if q == -1 else 0, total if q == 1 else 0]
    return {
        "incident": incident,
        "q_source_code": q,
        "p_phase_code": p,
        "edge_Q_0_to_1_and_4_to_5": edge_q,
        "expected_edge_Q": expected_edge_q,
        "sum_Q": sum(edge_q),
        "expected_sum_Q": total,
        "target_2B_tags": target_tags,
        "passed": c2_exact and target_tags == expected_tags and edge_q == expected_edge_q,
    }


def run():
    rows = [case(incident, q, p) for incident, q, p in product((True, False), (-1, 1), (-1, 1))]
    low = launch(True, -1, -1)
    high = launch(True, -1, 1)
    matched_h = all(h3.h(a) == h3.h(b) for a, b in zip(low, high))
    return {
        "passed": matched_h and all(row["passed"] for row in rows),
        "matched_initial_H_per_rail": matched_h,
        "whole_H_Q": PAID[2:],
        "rows": rows,
    }
