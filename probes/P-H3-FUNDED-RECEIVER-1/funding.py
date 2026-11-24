# SPDX-License-Identifier: Apache-2.0
"""Fixed pre-launch matter and radiation redistributions of the Q774 stock."""

from fixture import stock
from kernel import CLK, CORR, R0, R2, contact, reported_account

TARGET = (7, 3)
NEXT_C_PARTNER = (7, 2)
ARRIVAL_C_PARTNER = (7, 0)

# Each recipe is a sequence of swaps between ordered matter pairs.
MATTER = (
    (((0, 0), TARGET),),
    (((0, 1), TARGET),),
    (((0, 2), TARGET),),
    (((0, 3), TARGET),),
    (((1, 0), TARGET),),
    (((1, 1), TARGET),),
    (((1, 3), TARGET),),
    (((0, 0), TARGET), ((0, 1), ARRIVAL_C_PARTNER)),
    (((0, 2), TARGET), ((0, 3), ARRIVAL_C_PARTNER)),
    (((0, 0), TARGET), ((0, 1), NEXT_C_PARTNER)),
    (((0, 2), TARGET), ((0, 3), NEXT_C_PARTNER)),
    (((1, 0), TARGET), ((1, 1), ARRIVAL_C_PARTNER)),
    (((1, 1), TARGET), ((1, 0), NEXT_C_PARTNER)),
)

# A radiation step is (first site and lane, second site and lane, exponent).
# Exponent 0 specifies a swap. Nonzero exponent specifies a parity-guarded
# native rotation of that ordered pair, applied during stock preparation.
RAD_DONORS = tuple((x, y, CLK) for x, y in (
    (0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2),
))
READOUT = (*TARGET, CLK)
ARRIVAL_CLK = (*ARRIVAL_C_PARTNER, CLK)
HOLD_CLK = (*NEXT_C_PARTNER, CLK)
RADIATION = (
    (),
    *(((donor, READOUT, 0),) for donor in RAD_DONORS),
    (((0, 0, CLK), READOUT, 0), ((0, 1, CLK), ARRIVAL_CLK, 0)),
    (((0, 2, CLK), READOUT, 0), ((0, 3, CLK), ARRIVAL_CLK, 0)),
    (((0, 0, CLK), READOUT, 0), ((0, 1, CLK), HOLD_CLK, 0)),
    (((0, 2, CLK), READOUT, 0), ((0, 3, CLK), HOLD_CLK, 0)),
    (((1, 0, CLK), READOUT, 0), ((1, 1, CLK), HOLD_CLK, 0)),
    (((0, 0, CLK), (0, 2, CLK), 1), ((0, 2, CLK), READOUT, 0)),
    (((0, 0, CLK), (1, 1, CLK), 1), ((0, 0, CLK), READOUT, 0)),
    (((0, 0, CORR), (1, 0, CORR), 4), ((1, 0, CORR), (0, 0, CLK), 1),
     ((1, 0, CORR), READOUT, 0), ((0, 0, CLK), (1, 0, CORR), 0)),
    (((0, 1, CORR), (1, 1, CORR), 4), ((1, 1, CORR), (0, 1, CLK), 1),
     ((1, 1, CORR), READOUT, 0), ((0, 1, CLK), (1, 1, CORR), 0)),
    (((0, 0, CORR), (2, 0, CORR), 4), ((0, 0, CORR), (0, 0, CLK), 1),
     ((0, 0, CLK), READOUT, 0)),
    (((0, 1, CORR), (2, 1, CORR), 4), ((0, 1, CORR), (0, 1, CLK), 1),
     ((0, 1, CLK), READOUT, 0)),
)

RECIPES = range(1, 1 + len(MATTER) * len(RADIATION))


def index(site):
    x, y = site
    return x * 4 + y


def recipe_steps(recipe_int):
    if recipe_int not in RECIPES:
        raise ValueError(recipe_int)
    matter, radiation = divmod(recipe_int - 1, len(RADIATION))
    return MATTER[matter], RADIATION[radiation]


def stock_forward(bare, rank, recipe_int):
    base = stock(bare)
    if recipe_int == 0:
        return base
    field = [list(cell) for cell in base]
    matter, radiation = recipe_steps(recipe_int)
    for donor, receiver in matter:
        left, right = index(donor), index(receiver)
        for rail in (R0, R2):
            field[left][rail], field[right][rail] = field[right][rail], field[left][rail]
    for first, second, exponent in radiation:
        left, right = index(first[:2]), index(second[:2])
        lane_left, lane_right = first[2], second[2]
        a, b = field[left][lane_left], field[right][lane_right]
        u, v = contact(a, b, exponent) if exponent else (b, a)
        field[left][lane_left], field[right][lane_right] = u, v
    result = tuple(map(tuple, field))
    if reported_account(result) != reported_account(base):
        raise AssertionError((rank, recipe_int, 'funding account'))
    if result[index(TARGET)][R0] == result[index(TARGET)][R2]:
        raise AssertionError((rank, recipe_int, 'missing initial recipient matter gap'))
    return result
