# SPDX-License-Identifier: Apache-2.0
"""Stocks on the 8 by 4 torus. Coordinates use the public j basis."""
import kernel as k


def stock(bare, distance=0, sign=0):
    if (distance, sign) != (0, 0) and not (1 <= distance <= 4 and sign in (-1, 1)):
        raise ValueError((distance, sign))
    ingress = k.Preparation("ingress", k.from_j(-2, 0, -1, 0), k.from_j(0, -1, -1, 0))
    field = [list(cell) for cell in ingress.stock(bare)]
    source = 1 * k.HEIGHT + 3
    neighbor = 2 * k.HEIGHT + 3
    bridge = 7 * k.HEIGHT + 1
    field[bridge][k.CORR] = k.add(field[bridge][k.CORR], k.from_j(3, 4, 4, 8))
    field[source][k.R0] = k.from_j(-1, 0, -1, 0)
    field[source][k.R2] = k.add(field[source][k.R2], k.from_j(4, 2, 3, 1))
    for site in (source, neighbor):
        field[site][k.CORR] = k.add(field[site][k.CORR], k.from_j(0, -2, -2, 0))
    if sign:
        site = ((1 + distance) % 8) * k.HEIGHT + 3
        pulse = k.scale(16 * sign, k.from_j(0, -1, 1, 0))
        field[site][k.CORR] = k.add(field[site][k.CORR], pulse)
    return tuple(map(tuple, field))
