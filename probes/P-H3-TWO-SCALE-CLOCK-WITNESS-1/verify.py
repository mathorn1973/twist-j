#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Deterministic exact replay of a five-donor H3 clock witness."""

from fractions import Fraction
from functools import cache
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from pathlib import Path
import sys


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def load_kernel():
    path = Path(__file__).resolve().parents[2] / "reproduce/h3-referenced-record/verify.py"
    digest = "4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd"
    require(sha256(path.read_bytes()).hexdigest() == digest, "frozen H3 kernel")
    spec = spec_from_file_location("h3_kernel", path)
    module = module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


h3 = load_kernel()
add, sub, mul, scale = h3.add, h3.sub, h3.mul, h3.scale
Z, ONE, J, J_INV, RHO = h3.ZERO, h3.ONE, h3.J, h3.J_INV, h3.RHO
transport_pair = cache(h3.transport_pair)
collision = cache(h3.collision)
NX, NY = 192, 112
RECEIVER = ((41, 0), (41, 1))
REFERENCE = ((112, 56), (112, 57))
GAINS = (4090, 247, 2199, 430, 1467, 918)
SIGNS = (-1, 1)
MODES = ("on", "parked", "off")
BANKS = {
    -1: (((15, 110, 88, 107), (-196, 170, -66, 262), Z),
         ((258, -40, -27, -151), (-230, -398, -337, -285), (0, -256, -40, -16))),
    1: (((-235, -99, 101, 133), (-347, -333, 69, 203)),
        ((-105, -289, -143, -208), (165, -239, -369, -226))),
}
PARK = {-1: 76, 1: 80}
SCALES = (
    (Fraction(-134, 25), 0, Fraction(-103, 25), Fraction(-103, 25)),
    (Fraction(38, 25), 0, Fraction(-9, 25), Fraction(-9, 25)),
)
UNITS = {-1: J_INV, 0: ONE, 1: J}
STEPS = (0, 1, 2, -2, -1)
TAGS = {0: 0, 1: 1, -1: 2}


@cache
def rho_power(n):
    return ONE if n == 0 else mul(RHO, rho_power(n - 1))


def power(word, n):
    result = ONE
    for _ in range(n):
        result = mul(result, word)
    return result


GAP = mul(mul(RHO, J), power(sub(ONE, RHO), 8))
BIAS = mul(add(J, J_INV), GAP)


def set_word(field, key, word):
    if word != Z:
        field[key] = word


def insert(field, key, word):
    require(key not in field and word != Z, ("launch overlap or zero", key))
    field[key] = word


def material(field, xy, gap):
    insert(field, (*xy, 0), gap)
    insert(field, (*xy, 1), scale(-1, gap))


def launch(gain, q, p, mode):
    source, station = {}, {}
    active = mode != "off"
    x = 32 if active else 128
    delta = (-1, -1, -2, 0)
    center = add(ONE, scale(256, mul(RHO, J)))
    for dx in (0, 1):
        material(source, (x + dx, 0), delta)
        for rail, sign in ((2, 1), (3, -1)):
            insert(source, (x + dx, 0, rail), scale(q, mul(delta, add(center, scale(sign, J)))))
    insert(source, (151, 24, 2), scale(-4 * q, mul(delta, center)))
    lane = (-1024, 0, -512, -512)
    insert(source, (32 if active else 138, 1, 3), lane)
    insert(source, (171, 24, 2), scale(-1, lane))

    for anchor, partner in (RECEIVER, REFERENCE):
        material(station, anchor, GAP)
        material(station, partner, scale(-1, GAP))
        insert(station, (*anchor, 2), scale(p, BIAS))
    insert(station, (153, 24, 2), scale(-2 * p, BIAS))
    drive = scale(p, (-1024, -1024, -512, -512))
    insert(station, (33 if active else 143, 1, 3), drive)
    insert(station, (173, 24, 2), scale(-1, drive))

    m = (2**24) * gain
    guards = {
        (41, NY - 1, 2): (m - 438, 949, -865, 487),
        (41, NY - 2, 2): (44, -31, 236, -5),
        (41, 2, 2): (31 * m - 398, -843, -323, -743),
        (41, 3, 2): (74, 36, 183, -20),
        (42, 0, 3): (0, 0, 0, 1),
        (42, 1, 3): (0, 0, 0, 1),
    }
    for key, word in guards.items():
        _, y, rail = key
        insert(station, key, scale(p, word))
        insert(station, (175 if rail == 2 else 177, y, 2), scale(-p, word))
    for bank_sign, banks in BANKS.items():
        column = 41 if bank_sign == p and mode != "parked" else PARK[bank_sign]
        for side, bank in enumerate(banks):
            for distance, word in enumerate(bank, 1):
                if word != Z:
                    y = (-distance if side == 0 else 1 + distance) % NY
                    material(station, (column, y), word)

    require({key[:2] for key in source}.isdisjoint(key[:2] for key in station),
            "source and station do not share launch cells")
    return source | station


def cell(field, xy):
    return tuple(field.get((*xy, rail), Z) for rail in range(4))


def contact(field, bit, backward=False):
    pairs = set()
    for x, y, rail in field:
        if rail == 3:
            left = (x - (x - bit) % 2) % NX
            pairs.add(((left, y, rail), ((left + 1) % NX, y, rail)))
        else:
            low = (y - (y - bit) % 2) % NY
            pairs.add(((x, low, rail), (x, (low + 1) % NY, rail)))
    output = {}
    for a, b in pairs:
        aa, bb = transport_pair(field.get(a, Z), field.get(b, Z), backward)
        set_word(output, a, aa)
        set_word(output, b, bb)
    return output


def collide(field):
    output, tags = {}, {}
    for xy in {key[:2] for key in field}:
        words, tag = collision(cell(field, xy))
        for rail, word in enumerate(words):
            set_word(output, (*xy, rail), word)
        if tag:
            tags[xy] = tag
    return output, tags


def account(field):
    matter, radiation, energy = [], [], []
    for (_, _, rail), word in field.items():
        (matter if rail < 2 else radiation).append(word)
        energy.append(h3.h(word))
    return tuple(h3.ring_sum(book) for book in (matter, radiation, energy))


def exact_gap(field, xy):
    left, right, _, _ = cell(field, xy)
    return h3.half(sub(left, right))


def positive(word):
    a, b, c, d = word
    if b != 0 or c != d:
        return False
    x, y = 2 * a - c, -c
    if x >= 0 and y >= 0:
        return x != 0 or y != 0
    if x <= 0 and y <= 0:
        return False
    return x*x > 5*y*y if x > 0 else 5*y*y > x*x


@cache
def phase(old, new):
    ray = mul(new, h3.conj(old))
    matches = [step for k, step in enumerate(STEPS)
               if positive(mul(ray, h3.J_POWERS[-k % 5]))]
    require(len(matches) == 1, ("zero or off-grid signed phase", old, new))
    return matches[0]


def expected(q, p, mode, side, tick):
    """Closed-form gap and fifth-turn forecast, independent of the C/B kernel."""
    initial = scale(1 if side == 0 else -1, GAP)
    free = mul(rho_power(((tick + 1) // 2) % 5), initial)
    natural = 2 * (tick % 2)
    sign = 0 if mode == "off" else p * (q if side == 0 else 1)
    if tick < 9:
        return free, free, natural, 0
    if tick == 9:
        return free, mul(UNITS[sign], free), natural, sign
    if q == 1 or mode == "off":
        held = mul(UNITS[sign], free)
        return held, held, natural, 0
    if mode == "parked" or tick < 12:
        held = mul(UNITS[sign], initial)
        return held, held, 0, 0
    if p == -1:
        lam, mu = SCALES
        if tick in (12, 13):
            held = mul(lam, mul(rho_power(tick - 11), mul(J_INV, initial)))
            step = 0 if tick == 12 and side == 0 else 2
        else:
            held = mul(mu, mul(J, free))
            step = 2 if tick == 14 else natural
    else:
        held = mul(J_INV, free)
        step = (2 if side == 0 else 0) if tick == 12 else natural
    return held, held, step, 0


def scores(initial, q, p, mode, ledger):
    state = initial
    winding = [[0, 0], [0, 0]]
    arrivals = [None, None]
    partner = []
    for tick in range(1, 30):
        bit = (tick - 1) % 2
        c = contact(state, bit)
        b, tags = collide(c)
        reverse_b, _ = collide(b)
        require(reverse_b == c and contact(reverse_b, bit, backward=True) == state,
                ("substep inverse", tick))
        require(account(c) == account(b) == ledger, ("conservation", tick))
        require(all(x != 41 or (x, y) in RECEIVER for x, y in tags),
                ("exterior receiver-column B tag", tick))
        for group, locations in enumerate((RECEIVER, REFERENCE)):
            for side, xy in enumerate(locations):
                old, pre, post = (exact_gap(field, xy) for field in (state, c, b))
                forecast = expected(q, p, mode if group == 0 else "off", side, tick)
                c_lift, b_lift = phase(old, pre), phase(pre, post)
                require((pre, post, c_lift, b_lift) == forecast,
                        ("gap or signed phase", q, p, mode, tick, xy))
                require(tags.get(xy, 0) == TAGS[b_lift], ("B tag", tick, xy))
                winding[group][side] += c_lift + b_lift
                if group == 1:
                    require(cell(c, xy)[3] == cell(b, xy)[3] == Z, ("reference CORR", tick, xy))
                elif arrivals[side] is None and cell(c, xy)[3] != Z:
                    arrivals[side] = tick
        if tick <= 11:
            partner.append(cell(c, RECEIVER[1]))
            if tick <= 10:
                partner.append(cell(b, RECEIVER[1]))
        if tick in (19, 29):
            free = tick + 1
            require(winding[1] == [free, free], ("reference winding", tick))
            if mode == "on":
                require(winding[0] == [free + q*p] * 2, ("running winding", tick))
            elif mode == "off":
                require(winding[0] == [free, free], ("source-off winding", tick))
            elif q == 1:
                require(winding[0] == [free + p] * 2, ("parked aligned winding", tick))
            else:
                require(winding[0] == [10 - p, 10 + p], ("parked stalled winding", tick))
        state = b
    require(arrivals == ([None, None] if mode == "off" else [9, 9]), "first CORR arrival")
    return partner


def pair_stock(word):
    value = 5 * sum(coefficient**2 for coefficient in word) - sum(word)**2
    require(value == 2 * h3.scalar_account(h3.h(word)), "donor stock agrees with native account")
    return value


def main():
    support = {(side, distance) for side, bank in enumerate(BANKS[-1])
               for distance, word in enumerate(bank, 1) if word != Z}
    require(support == {(0, 1), (0, 2), (1, 1), (1, 2), (1, 3)}, "donor support")
    costs = [sum(map(pair_stock, bank)) for bank in BANKS[-1]]
    require(costs == [727870, 1164476] and sum(costs) == 1892346, "negative-bias donor stock")
    require(all(map(positive, SCALES)), "positive scales at the principal embedding")
    cuts = ((12, (0, 113, 154, 113)), (13, (-41, -154, -154, -41)),
            (14, (56, 103, 56, 0)), (19, (0, 56, 103, 56)), (29, (0, 56, 103, 56)))
    for tick, word in cuts:
        for side in (0, 1):
            forecast = expected(-1, -1, "on", side, tick)
            frozen = scale(1 if side == 0 else -1, word)
            require(forecast[:2] == (frozen, frozen), ("frozen scaled gaps", tick, side))
    require(len(GAINS) == len(set(GAINS)) == 6, "distinct launch gains")
    count = 0
    for gain in GAINS:
        ledger = account(launch(gain, -1, -1, "on"))
        require(ledger[:2] == (Z, Z), "balanced initial account")
        for p, mode in product(SIGNS, MODES):
            twins = []
            for q in SIGNS:
                initial = launch(gain, q, p, mode)
                require(account(initial) == ledger, ("matched launch account", gain, p, mode))
                twins.append(scores(initial, q, p, mode, ledger))
                count += 1
            if mode == "on":
                require(twins[0][:-1] == twins[1][:-1] and twins[0][-1] != twins[1][-1],
                        ("first partner split at C11", gain, p))
    require(count == 72, "panel coverage")
    print("H3 two-scale clock witness: 72/72 exact native cases")
    print("Negative-bias donor stock: 727870 + 1164476 = 1892346")
    print("Negative bias q=-1: offsets +1/5 at B19 and B29")
    print("Negative bias q=+1: offsets -1/5 at B19 and B29")


if __name__ == "__main__":
    main()
