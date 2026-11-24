# SPDX-License-Identifier: Apache-2.0
"""Exact localized matter controls and a matched-stock collision readout."""

from fractions import Fraction

from native import h3, ledger, step, reverse, put, cell, transport


WIDTH = 8
HEIGHT = 12
SITE = 4
ZERO = h3.ZERO


def empty():
    return [ZERO] * (4 * WIDTH * HEIGHT)


def negative(word):
    return h3.scale(-1, word)


def matter_support(field):
    return tuple(
        (x, y)
        for x in range(WIDTH)
        for y in range(HEIGHT)
        if cell(field, HEIGHT, x, y)[:2] != (ZERO, ZERO)
    )


def matter_weight(field, y):
    return sum(h3.scalar_account(h3.h(w)) for w in cell(field, HEIGHT, 0, y)[:2])


def isolated(word):
    field = empty()
    put(field, HEIGHT, 0, SITE, (word, negative(word), ZERO, ZERO))
    return tuple(field)


def terminal_translation(initial, final):
    occupied = tuple(
        (x, y) for x in range(WIDTH) for y in range(HEIGHT)
        if cell(final, HEIGHT, x, y) != (ZERO,) * 4
    )
    if len(occupied) != 1:
        return None
    x, y = occupied[0]
    if cell(final, HEIGHT, x, y) != cell(initial, HEIGHT, 0, SITE):
        return None
    return [x, (y - SITE) % HEIGHT]


def free_profiles():
    odd_initial = isolated(h3.ONE)
    even_initial = isolated(h3.scale(2, h3.ONE))
    odd, even = odd_initial, even_initial
    odd_returns, even_returns, supports, checks = [], [], [], []
    for tick in range(1, 19):
        bit = (tick - 1) % 2
        odd_c, odd, odd_tags = step(odd, HEIGHT, bit)
        even_c, even, even_tags = step(even, HEIGHT, bit)
        if odd == odd_initial:
            odd_returns.append(tick)
        if even == even_initial:
            even_returns.append(tick)
        support = matter_support(even)
        neighbor = SITE + (1 if tick <= 9 else -1)
        supports.append(support)
        checks.append({
            "tick": tick,
            "odd_support_xy": matter_support(odd),
            "odd_unchanged": odd_c == odd == odd_initial and not odd_tags,
            "even_b_inactive": even_c == even and not even_tags,
            "even_support_confined": bool(support) and all(
                x == 0 and y in (SITE, neighbor) for x, y in support
            ),
        })
    translations = {
        "odd": terminal_translation(odd_initial, odd),
        "even": terminal_translation(even_initial, even),
    }
    decision = {
        "free_steps": all(row["odd_unchanged"] and row["even_b_inactive"]
                          and row["even_support_confined"] for row in checks),
        "field_returns": odd_returns == list(range(1, 19)) and even_returns == [9, 18],
        "zero_full_period_translation": translations["odd"] == translations["even"] == [0, 0],
    }
    return {
        "passed": all(decision.values()),
        "checks": decision,
        "odd_period": next((tick for tick in odd_returns if tick % 2 == 0), None),
        "even_period": next((tick for tick in even_returns if tick % 2 == 0), None),
        "odd_field_returns": odd_returns,
        "even_field_returns": even_returns,
        "odd_final_support_xy": matter_support(odd),
        "even_support_xy": supports,
        "full_horizon_translation_mod_xy": translations,
        "even_support_offsets": [[y - SITE for x, y in support] for support in supports],
        "steps": checks,
    }

def encoding(half_gap):
    return half_gap, negative(half_gap)


def matched_post_c(branch):
    d = h3.scale(2, h3.ONE)
    radiation = {1: h3.mul(h3.J, d), -1: h3.mul(h3.J_INV, d)}
    field = empty()
    target = radiation.get(branch, ZERO)
    put(field, HEIGHT, 0, SITE, encoding(d) + encoding(target))
    for sign, position in ((1, 0), (-1, 2)):
        stock = ZERO if sign == branch else radiation[sign]
        put(field, HEIGHT, 4, position, (ZERO, ZERO) + encoding(stock))
    return tuple(field)


def fraction_pair(value):
    return None if value is None else [value.numerator, value.denominator]


def collision_readouts():
    expected_weights = {0: (6, 10), 1: (14, 10), -1: (4, 20)}
    expected_tags = {0: (), 1: ((0, SITE, 1),), -1: ((0, SITE, 2),)}
    rows = []
    for orientation in (1, -1):
        # SITE is the left endpoint for bit 0 and the right endpoint for bit 1.
        next_bit = 0 if orientation == 1 else 1
        previous_bit = 1 - next_bit
        neighbor = SITE + orientation
        stock = None
        free_shift = None
        for branch in (0, 1, -1):
            prescribed = matched_post_c(branch)
            if stock is None:
                stock = ledger(prescribed)
            h3.require(ledger(prescribed) == stock, "matched complete input stock")
            start = transport(prescribed, HEIGHT, previous_bit, backward=True)
            c, b, tags = step(start, HEIGHT, previous_bit)
            h3.require(c == prescribed, "prescribed post-C input")
            h3.require(reverse(b, HEIGHT, previous_bit) == start, "first native inverse")
            d = h3.scale(2, h3.ONE)
            unit = {0: h3.ONE, 1: h3.J, -1: h3.J_INV}[branch]
            actual_matter = cell(b, HEIGHT, 0, SITE)[:2]
            next_c, end, _ = step(b, HEIGHT, next_bit)
            h3.require(reverse(end, HEIGHT, next_bit) == b, "second native inverse")
            support = matter_support(next_c)
            weights = tuple(matter_weight(next_c, y) for y in (SITE, neighbor))
            total = sum(weights)
            shift = orientation * Fraction(weights[1], total) if total else None
            if branch == 0:
                free_shift = shift
            excess = shift - free_shift if shift is not None and free_shift is not None else None
            checks = {
                "expected_tags": tags == expected_tags[branch],
                "expected_matter": actual_matter == encoding(h3.mul(unit, d)),
                "expected_support": support == tuple(sorted(((0, SITE), (0, neighbor)))),
                "expected_weights": weights == expected_weights[branch],
                "pure_redistribution": total == matter_weight(b, SITE),
                "expected_excess": excess == -orientation * branch * Fraction(5, 24),
            }
            rows.append({
                "orientation": orientation,
                "branch": branch,
                "passed": all(checks.values()),
                "checks": checks,
                "tags": tags,
                "post_b_matter_words": actual_matter,
                "next_c_support_xy": support,
                "matter_q_before_b": matter_weight(c, SITE),
                "matter_q_after_b": matter_weight(b, SITE),
                "next_c_weights_resident_then_new": list(weights),
                "centroid_shift": fraction_pair(shift),
                "centroid_excess": fraction_pair(excess),
            })
    return rows


def run():
    free = free_profiles()
    rows = collision_readouts()
    return {"passed": free["passed"] and all(row["passed"] for row in rows),
            "free": free, "collision_rows": rows}
