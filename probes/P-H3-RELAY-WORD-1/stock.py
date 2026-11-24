# SPDX-License-Identifier: Apache-2.0
"""Rank-blind launch stock additions for the two vertical neighbors of (7,3)."""

from itertools import product
from typing import NamedTuple

import kernel as k
from fixture import stock


BASE = 324
RECEIVER = 31
PAYER = 29
BANK = 17
SPARE = 16
BALLAST = 18
WORKERS = (30, 28)
T = k.from_j(1, 1, 1, 1)
W = k.multiply(k.J, T)
V = k.from_j(-1, -1, 1, -1)
Q_PAYER = k.from_j(3, 4, 4, 8)
Q_REST = k.subtract(Q_PAYER, k.scale(2, T))
LEDGER = ((-9, 2, -2, -3), (19, 7, 5, 19), (463, 0, 152, 152), 774)
UNITS = tuple(k.scale(sign, k.power(phase)) for sign, phase in product((1, -1), range(5)))
EMPTY = (k.ZERO, k.ZERO)


def pair(word):
    return word, k.scale(-1, word)


class Model(NamedTuple):
    label: str
    worker: int | None
    matter: tuple
    radiation: tuple


def models():
    yield BASE, Model("prior_324", None, (), ())
    index = 500
    for worker in WORKERS:
        other = next(site for site in WORKERS if site != worker)
        for secondary, parity_unit, spare_unit in product((SPARE, other), UNITS, UNITS):
            matter = (
                (BANK, T),
                (worker, k.multiply(parity_unit, W)),
                (secondary, k.multiply(spare_unit, W)),
            )
            yield index, Model("matter_w", worker, matter, ())
            index += 1
        for secondary, unit in product((SPARE, other), UNITS):
            matter = ((BANK, W), (worker, k.multiply(unit, T)), (secondary, W))
            yield index, Model("matter_t", worker, matter, ())
            index += 1
        for unit in UNITS:
            matter = ((BANK, k.ZERO), (worker, k.multiply(unit, V)))
            yield index, Model("matter_v_permutation", worker, matter, ())
            index += 1

    # Each tuple records the proposed B tag, worker CORR, ballast CORR,
    # and replacement amplitudes of the two original empty/escrow matter pairs.
    templates = (
        (1, (3, 2, 3, 3), (0, 0, 0, 0), (-1, 0, -1, 0), (-1, 0, -1, 0)),
        (2, (1, 2, 3, 3), (0, 0, 0, 0), (-1, 0, 0, 0), (-1, 1, -1, 1)),
        (2, (-1, 0, -1, 1), (0, 0, 0, 0), (-1, 0, 0, 1), (-1, 1, -1, 0)),
        (2, (-1, 0, 1, 1), (0, 0, 0, 0), (-1, 0, -1, 0), (-1, -1, -1, 1)),
        (1, (1, 0, 1, -1), (-1, 0, 1, 3), (0, 0, 0, 0), (-1, 0, -1, 0)),
        (2, (-1, 0, -1, 1), (-1, 0, -1, -1), (0, 0, 0, 0), (-1, 0, 0, 0)),
        (2, (1, 0, -1, 1), (-1, 0, 1, 1), (-1, 0, -1, 1), (-1, 1, -1, 0)),
        (1, (-1, 2, -1, 1), (1, 0, 1, 1), (-1, -1, 0, 0), (-1, 1, 0, 0)),
        (1, (3, 2, 3, 3), (-1, 0, -1, 1), (-1, -1, 1, 0), (-1, 1, -1, 0)),
        (1, (1, 4, 1, 3), (-1, -2, -1, 1), (0, 0, 0, 0), (-1, 1, -1, 0)),
        (1, (-1, 0, 1, -1), (1, 0, -1, 3), (-1, -1, 0, 0), (-1, 0, -1, 0)),
        (1, (3, 2, 1, 3), (-1, 0, -1, 1), (-1, 0, -1, 0), (-1, -1, 1, -1)),
        (2, (1, 2, 3, 3), (-1, 0, -1, -1), (0, 0, 0, 0), (-1, 1, -1, 0)),
        (2, (-1, 0, 1, 1), (-1, 0, -1, 1), (-1, -1, 0, 1), (-1, 1, -1, 0)),
    )
    for guard, worker_corr, ballast_corr, spare, bank in templates:
        b, c, v1, v2 = (k.from_j(*word) for word in (worker_corr, ballast_corr, spare, bank))
        matter = ((WORKERS[0], T), (SPARE, v1), (BANK, v2))
        radiation = ((WORKERS[0], b), (PAYER, k.subtract(Q_REST, k.add(b, c))))
        if c != k.ZERO:
            radiation = (*radiation, (BALLAST, c))
        yield index, Model(f"clock_to_matter_B{guard}", WORKERS[0], matter, radiation)
        index += 1


MODELS = dict(models())


def baseline(bare):
    original = stock(bare)
    if (
        original[RECEIVER] != (k.ZERO,) * 4
        or original[BANK][:2] != EMPTY
        or original[PAYER][k.CORR] != Q_PAYER
    ):
        raise ValueError("Prior mode 324 launch slots do not match")
    field = [list(cell) for cell in original]
    field[RECEIVER] = [*pair(W), k.scale(2, T), k.ZERO]
    field[BANK][:2] = pair(V)
    field[PAYER][k.CORR] = Q_REST
    result = tuple(map(tuple, field))
    if k.reported_account(original) != LEDGER or k.reported_account(result) != LEDGER:
        raise ValueError("Prior mode 324 launch ledger does not match")
    return result


def decorate(field, mode):
    """Apply the stock redistribution, or return None if virtual slots are occupied."""
    model = MODELS[mode]
    if mode == BASE:
        return field
    if any(field[site][:2] != (pair(V) if site == BANK else EMPTY)
           for site, _ in model.matter):
        return None
    if model.radiation and field[model.worker][k.CLK] != k.ZERO:
        return None
    if any(field[site][k.CORR] != (Q_REST if site == PAYER else k.ZERO)
           for site, _ in model.radiation):
        return None
    result = [list(cell) for cell in field]
    for site, word in model.matter:
        result[site][:2] = pair(word)
    for site, word in model.radiation:
        result[site][k.CORR] = word
    result = tuple(map(tuple, result))
    if k.account(result) != k.account(field):
        raise AssertionError((mode, "stock redistribution ledger"))
    return result


def direct(bare, rank, mode):
    original = baseline(bare)
    out = decorate(original, mode)
    if out is None:
        raise AssertionError((rank, mode, "ineligible direct stock"))
    return out
