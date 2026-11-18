# SPDX-License-Identifier: Apache-2.0
"""Conjugacy between a single CORR row and vertical antipodal matter."""

from itertools import product

from native import h3


SIZE, TICKS, ZERO = 8, 10, h3.ZERO
ALPHABET = tuple(h3.scale(n, h3.ONE) for n in range(3))


def corr_row(words):
    field = [ZERO] * (4 * SIZE * SIZE)
    for position, word in enumerate(words):
        field[h3.index(SIZE, position, 0, 3)] = word
    return tuple(field)


def row_to_column(field):
    # Transpose (x,0) -> (0,x), move CORR to R0, and copy its negative to R2.
    target = [ZERO] * (4 * SIZE * SIZE)
    for position in range(SIZE):
        word = field[h3.index(SIZE, position, 0, 3)]
        target[h3.index(SIZE, 0, position, 0)] = word
        target[h3.index(SIZE, 0, position, 1)] = h3.scale(-1, word)
    return tuple(target)


def stock(field):
    quadratic = h3.ring_sum(h3.h(word) for word in field)
    return quadratic, h3.scalar_account(quadratic)


def require_cut(source, target, source_stock, target_stock):
    row = tuple(source[h3.index(SIZE, p, 0, 3)] for p in range(SIZE))
    h3.require(source == corr_row(row), "source remains a single CORR row")
    h3.require(target == row_to_column(source), "complete transposed antipodal field")
    h3.require(stock(source) == source_stock, "source H and Q conserved")
    h3.require(stock(target) == target_stock, "target H and Q conserved")


def undo(complete, bit):
    pre_b, _ = h3.collide(complete, SIZE)
    return tuple(h3.transport(pre_b, SIZE, bit, backward=True))


def run():
    preparations = 0
    admitted_unequal = refused_unequal = 0
    for profile in product(ALPHABET, repeat=4):
        for start_bit in (0, 1):
            source = corr_row(profile * 2)
            target = row_to_column(source)
            source_h, source_q = stock(source)
            source_stock = source_h, source_q
            target_stock = h3.scale(2, source_h), 2 * source_q
            require_cut(source, target, source_stock, target_stock)
            preparations += 1
            for tick in range(TICKS):
                bit = (start_bit + tick) % 2
                for left in range(bit, SIZE, 2):
                    right = (left + 1) % SIZE
                    a = source[h3.index(SIZE, left, 0, 3)]
                    b = source[h3.index(SIZE, right, 0, 3)]
                    if a != b:
                        if h3.even(h3.sub(a, b)):
                            admitted_unequal += 1
                        else:
                            refused_unequal += 1
                source_c = tuple(h3.transport(source, SIZE, bit))
                target_c = tuple(h3.transport(target, SIZE, bit))
                require_cut(source_c, target_c, source_stock, target_stock)
                source_b, source_events = h3.collide(source_c, SIZE)
                target_b, target_events = h3.collide(target_c, SIZE)
                source_b, target_b = tuple(source_b), tuple(target_b)
                h3.require(not source_events and not target_events, "both B layers idle")
                require_cut(source_b, target_b, source_stock, target_stock)
                h3.require(undo(source_b, bit) == source, "source inverse")
                h3.require(undo(target_b, bit) == target, "target inverse")
                source, target = source_b, target_b
    h3.require(admitted_unequal > 0 and refused_unequal > 0, "both unequal guard outcomes covered")
    return {
        "geometry": [SIZE, SIZE],
        "profiles": preparations // 2,
        "initial_bits": [0, 1],
        "ticks_per_preparation": TICKS,
        "matched_ticks": preparations * TICKS,
        "unequal_admitted_row_contacts": admitted_unequal,
        "unequal_refused_row_contacts": refused_unequal,
        "target_to_source_H_and_Q_factor": 2,
    }
