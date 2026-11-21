# SPDX-License-Identifier: Apache-2.0
"""Test a directed translation correlation on a fully admitted cut and its collision."""

from native import cell, h3, ledger, put, step, transport


def correlation(field, ny):
    nx = len(field) // (4 * ny)
    value = h3.ring_sum(
        h3.mul(h3.conj(a), b)
        for x in range(nx) for y in range(ny)
        for a, b in zip(cell(field, ny, x, y), cell(field, ny, x, (y + 2) % ny))
    )
    return h3.sub(value, h3.conj(value))


def run():
    nx, ny = 2, 8
    two = h3.scale(2, h3.ONE)
    two_j = h3.scale(2, h3.J)
    cut = [h3.ZERO] * (4 * nx * ny)
    put(cut, ny, 0, 0, (two, h3.scale(-1, two), two_j, h3.scale(-1, two_j)))
    put(cut, ny, 0, 2, (two, h3.scale(-1, two), h3.ZERO, h3.ZERO))
    initial = transport(tuple(cut), ny, 0, backward=True)
    c, b, events = step(initial, ny, 0)
    h3.require(c == tuple(cut), "recover prescribed collision input")
    before, middle, after = (correlation(field, ny) for field in (initial, c, b))
    predicted = h3.scale(8, h3.sub(h3.RHO_INV, h3.RHO))
    return {
        "observable": "all rails, shift two vertical sites, S minus conjugate S",
        "before_C": before, "after_C": middle, "after_B": after,
        "B_events": events, "whole_ledger": ledger(b),
        "passed": before == middle == h3.ZERO and after == predicted and events == ((0, 0, 1),),
    }
