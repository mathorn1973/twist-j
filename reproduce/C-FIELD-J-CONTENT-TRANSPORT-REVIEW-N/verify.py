#!/usr/bin/env python3
"""Frozen independent exact audits; run only after public freeze/readback."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd


MOD = 1226
ZERO = (0, 0, 0, 0)
EMPTY = (0, ZERO, 0)
ELL = (1, -1, -1, 1)
JELL = (-1, 0, -2, -2)
COUNTS = Counter()


def need(condition, *witness):
    if not condition:
        raise AssertionError(witness)


def chart(a):
    a0, a1, a2, a3 = a
    return (a1, a2 - a3, a0 - a1 - a3, a1 - 2*a2 + a3)


def unchart(y):
    y0, y1, y2, y3 = y
    return (2*y0 - 2*y1 + y2 - y3, y0, y0 - y1 - y3,
            y0 - 2*y1 - y3)


def energy_field(y):
    a, b, c, d = y
    return 2*a*a - 2*a*b + 3*b*b + c*c + d*d + 2*a*c - a*d - b*c + 3*b*d


def coefficient_energy(a):
    x, y, z, w = a
    return x*x + y*y + z*z + w*w - x*z - x*w - y*w


def af(y):
    a, b, c, d = y
    return (a+c, b+d, -2*a+b-c+d, a-3*b+c-2*d)


def e5(y):
    aa = af(af(y))
    return (energy_field(y), energy_field(tuple(x+z for x, z in zip(y, aa))),
            tuple(x % 5 for x in unchart(y)))


def encode(y):
    a = unchart(y)
    v = a[0] + 3
    for radix, digit in zip((5, 5, 7), (a[1]+2, a[2]+2, a[3]+3)):
        v = radix*v + digit
    return v + 1


def decode(p):
    if p == 0:
        return ("BLANK",)
    v = p - 1
    v, d3 = divmod(v, 7)
    v, d2 = divmod(v, 5)
    d0, d1 = divmod(v, 5)
    a = (d0-3, d1-2, d2-2, d3-3)
    y = chart(a)
    if energy_field(y) > 5:
        return ("INVALID",)
    return ("VALUE", a, y)


def supported(packet):
    return packet[0] == 1 and energy_field(packet[1]) <= 5


def snapshot(packet):
    if packet[0] == 0:
        return ("ABSENT",)
    if energy_field(packet[1]) > 5:
        return ("UNSUPPORTED",)
    return ("VALUE", unchart(packet[1]), packet[1])


def react(packet, latch, record, inverse=False):
    if not supported(packet):
        return packet, latch, record
    b, y, r = packet
    if inverse:
        if latch:
            return (b, y, r+2), 0, (record-encode(y)) % MOD
        if r >= 2:
            return (b, y, r-2), 1, record
    else:
        if latch:
            return (b, y, r+2), 0, record
        if r >= 2:
            return (b, y, r-2), 1, (record+encode(y)) % MOD
    return packet, latch, record


def reaction(state, inverse=False):
    slots, latch, record = state
    packet, latch, record = react(slots[-1], latch, record, inverse)
    return slots[:-1] + (packet,), latch, record


def matching(state, which, cut=-1):
    slots, latch, record = state
    changed = list(slots)
    for j in range((len(slots)-1)//2):
        if j != cut:
            left = 2*j + which
            changed[left], changed[left+1] = changed[left+1], changed[left]
    return tuple(changed), latch, record


def layers(state, cut=-1):
    g = reaction(state)
    a = matching(g, 0, cut)
    b = matching(a, 1, cut)
    return g, a, b


def step(state, cut=-1):
    return layers(state, cut)[-1]


def reverse(state, cut=-1):
    return reaction(matching(matching(state, 1, cut), 0, cut), True)


def accounts(state):
    slots, latch, _ = state
    content = tuple(sorted((b, y) for b, y, r in slots))
    resource = sum(p[2] for p in slots) + 2*latch
    energy = sum(b+energy_field(y)+r for b, y, r in slots) + 2*latch + 1
    return energy, content, resource


def round_trip(state, cut=-1):
    need(reverse(step(state, cut), cut) == state, "inverse-forward", cut, state)
    need(step(reverse(state, cut), cut) == state, "forward-inverse", cut, state)


def clean(n, y, reserve=2, presence=1, record=0, latch=0, at=0):
    slots = [EMPTY] * (2*n-1)
    slots[at] = (presence, y, reserve)
    return tuple(slots), latch, record


def record_writes(n, boundary):
    return 0 if boundary < n else 1 + (boundary-n)//(2*(2*n-1))


def visits(n, boundary):
    return 0 if boundary < n else 1 + (boundary-n)//(2*n-1)


def cycle_position(n, boundary):
    t = n-1
    q = boundary % (2*n-1)
    return 2*q if q <= t else 2*(2*t-q)+1


def a_position(n, slot):
    if slot == 2*n-2:
        return slot
    return slot+1 if slot % 2 == 0 else slot-1


def expected_clean(n, y, boundary, position, p0=0):
    latch = visits(n, boundary) % 2
    slots = [EMPTY] * (2*n-1)
    slots[position] = (1, y, 2-2*latch)
    return tuple(slots), latch, (p0+record_writes(n, boundary)*encode(y)) % MOD


def audit_code():
    supported_fields = []
    shells = Counter()
    codes = set()
    for a in product(range(-3, 4), range(-2, 3), range(-2, 3), range(-3, 4)):
        y = chart(a)
        need(unchart(y) == a and chart(unchart(y)) == y, "chart", a)
        h = energy_field(y)
        need(h == coefficient_energy(a), "quadratic-box", a)
        need(h >= 0 and (h == 0) == (a == ZERO), "positive-box", a)
        if h <= 5:
            supported_fields.append(y)
            shells[h] += 1
            c = encode(y)
            need(c not in codes and 1 <= c < MOD, "code-injectivity", a, c)
            codes.add(c)
            need(decode(c) == ("VALUE", a, y), "roundtrip-code", a, c)
            need(snapshot((1, y, 2)) == decode(c), "snapshot", a)
            q = sum(z*z for z in a)
            u = q-a[0]*a[1]-a[1]*a[2]-a[2]*a[3]
            need(e5(y) == (h, u, tuple(z % 5 for z in a)), "derived-E5", a)
    need(tuple(shells[k] for k in range(6)) == (1, 20, 30, 60, 60, 120),
         "shells", shells)
    image = Counter(decode(p)[0] for p in range(MOD))
    need(image == Counter(BLANK=1, VALUE=291, INVALID=934), "record-image", image)
    need(encode(ZERO) == 613 and snapshot(EMPTY) != snapshot((1, ZERO, 2)), "zero")
    basis = [tuple(int(i == j) for i in range(4)) for j in range(4)]
    probes = basis + [tuple(x+y for x, y in zip(basis[i], basis[j]))
                      for i in range(4) for j in range(i+1, 4)]
    for a in probes:
        need(energy_field(chart(a)) == coefficient_energy(a), "quadratic-coeff", a)
    ratios = []
    for a in (ELL, JELL):
        need(energy_field(chart(a)) == 5, "pair-energy", a)
        ss = sum(a)**2
        ratios.append(Fraction(ss, 4*(5*sum(v*v for v in a)-ss)))
    need(ratios == [Fraction(0), Fraction(5, 16)], "pair-LOW", ratios)
    need(encode(chart(ELL)) != encode(chart(JELL)), "pair-codes")
    COUNTS["box"] = 1225
    COUNTS["supported"] = len(supported_fields)
    COUNTS["record_values"] = MOD
    return tuple(supported_fields)


def audit_local(fields, unsupported_fields):
    for y, b, r, latch in product(fields+unsupported_fields, (0, 1),
                                  (0, 1, 2, 3, 5, 10**30), (0, 1)):
        packet = b, y, r
        c = encode(y) if supported(packet) else 1
        for p in (0, 1, 612, 613, 1225, (-c) % MOD, (MOD-c+1) % MOD):
            start = packet, latch, p
            out = react(*start)
            inv = react(*start, inverse=True)
            need(react(*out, inverse=True) == start, "GinvG", start, out)
            need(react(*inv) == start, "GGinv", start, inv)
            for end in (out, inv):
                need(end[0][:2] == packet[:2], "local-content", start, end)
                need(end[0][2] + 2*end[1] == r + 2*latch, "local-resource", start, end)
                need(0 <= end[2] < MOD and end[0][2] >= 0, "local-carrier", start, end)
            if not supported(packet) or (latch == 0 and r < 2):
                need(out == start, "rejection", start, out)
            elif latch == 0:
                need(out == ((b, y, r-2), 1, (p+c) % MOD), "accepted-write", start, out)
            else:
                need(out == ((b, y, r+2), 0, p), "release", start, out)
            COUNTS["local_cases"] += 1


def block(state, i):
    return (state[0][i], state[1], state[2]) if i == len(state[0])-1 else state[0][i]


def audit_dirty(unsupported_fields):
    pool = (EMPTY, (1, ZERO, 0), (1, ZERO, 2), (0, ZERO, 3),
            (1, chart(ELL), 5), (1, chart(JELL), 1),
            (1, unsupported_fields[0], 2), (0, unsupported_fields[1], 10**30),
            (1, chart((1, 0, 0, 0)), 3), (1, ZERO, 2))
    for n in range(2, 9):
        for cut in range(-1, n-1):
            for k in range(24):
                slots = tuple(pool[k % len(pool)] if k % 6 == 0 else
                              pool[(k+3*i+i*i) % len(pool)] for i in range(2*n-1))
                state = slots, k % 2, (613*k+37) % MOD
                round_trip(state, cut)
                need(accounts(reverse(state, cut)) == accounts(state), "inverse-accounts", n, cut, k)
                prior = state
                for layer_index, end in enumerate(layers(state, cut)):
                    need(accounts(end) == accounts(state), "dirty-accounts", n, cut, k, layer_index)
                    if cut >= 0:
                        need(end[0][2*cut+1] == slots[2*cut+1], "cut-old-content", n, cut, k)
                    if layer_index:
                        need(Counter(end[0]) == Counter(prior[0]), "whole-packet-swap", n, cut, k)
                        for i in range(2*n-1):
                            if layer_index == 1:
                                source = i if i == 2*n-2 else (i ^ 1)
                                edge = i//2
                            else:
                                source = i if i == 0 else (i+1 if i % 2 else i-1)
                                edge = (i-1)//2
                            if edge == cut:
                                source = i
                            need(end[0][i] == prior[0][source], "literal-swap", n, cut, k, layer_index, i)
                    prior = end
                COUNTS["dirty_states"] += 1
                if k >= 4:
                    continue
                for i in range(2*n-1):
                    for replacement in (pool[2], pool[4], pool[7]):
                        perturbed = list(slots)
                        perturbed[i] = replacement
                        other = (tuple(perturbed), 1-state[1], (state[2]+137) % MOD) if i == 2*n-2 else (tuple(perturbed), state[1], state[2])
                        for operation in (step, reverse):
                            first, second = operation(state, cut), operation(other, cut)
                            for j in range(2*n-1):
                                if abs(j-i) > 2:
                                    need(block(first, j) == block(second, j), "radius", n, cut, k, i, j, operation.__name__)
                            COUNTS["locality_interventions"] += 1


def audit_clean(fields):
    for n, y in product(range(2, 9), fields):
        period = 2*n-1
        state = clean(n, y)
        for boundary in range(1, 4*period+1):
            g, a, b = layers(state)
            oldpos = cycle_position(n, boundary-1)
            expected_positions = (oldpos, a_position(n, oldpos), cycle_position(n, boundary))
            for end, pos in zip((g, a, b), expected_positions):
                expected = expected_clean(n, y, boundary, pos)
                need(end == expected, "clean-substep", n, y, boundary, pos, end, expected)
                need(accounts(end) == accounts(state), "clean-accounts", n, y, boundary)
                want_snapshot = ("VALUE", unchart(y), y) if pos == 2*n-2 else ("ABSENT",)
                need(snapshot(end[0][-1]) == want_snapshot, "clean-snapshot", n, y, boundary, pos)
                need(decode(end[2]) == decode(expected[2]), "clean-record-reader", n, y, boundary)
            state = b
            round_trip(state)
            need(accounts(state)[0] == energy_field(y)+4, "clean-total", n, y, boundary)
            if boundary == n-1:
                need(snapshot(state[0][-1]) == ("VALUE", unchart(y), y) and state[2] == 0,
                     "first-arrival", n, y)
            if n <= boundary < n+2*period:
                need(decode(state[2]) == ("VALUE", unchart(y), y), "first-retention", n, y, boundary)
            if boundary in (2*period, 4*period):
                need(state[:2] == clean(n, y)[:2], "operative-return", n, y, boundary)
                need(state[2] == ((boundary//(2*period))*encode(y)) % MOD, "retained-return", n, y, boundary)
            COUNTS["clean_steps"] += 1


def audit_cuts_and_underfunding(fields):
    for n in range(2, 6):
        for y, cut in product(fields, range(n-1)):
            state = clean(n, y)
            for boundary in range(1, 2*(2*n-1)+1):
                for end in layers(state, cut):
                    need(end[0][-1] == EMPTY and end[1:] == (0, 0), "clean-cut", n, y, cut, boundary)
                state = step(state, cut)
                COUNTS["cut_steps"] += 1
    for n, y, reserve in product((2, 5), fields, (0, 1)):
        state = clean(n, y, reserve=reserve)
        for boundary in range(1, 2*(2*n-1)+1):
            need(reaction(state) == state, "underfunded-G", n, y, reserve, boundary)
            state = step(state)
            need(state[1:] == (0, 0), "underfunded-aux", n, y, reserve, boundary)
            need(state[0][cycle_position(n, boundary)] == (1, y, reserve), "underfunded-position", n, y, reserve, boundary)
            COUNTS["underfunded_steps"] += 1


def no_reaction_trial(n, state, label):
    original_account = accounts(state)
    for boundary in range(1, 2*(2*n-1)+1):
        need(reaction(state) == state, "control-G", label, n, boundary, state)
        for end in layers(state):
            need(end[1:] == (0, 0), "control-aux", label, n, boundary, end)
            need(accounts(end) == original_account, "control-account", label, n, boundary)
        state = step(state)
        COUNTS["control_steps"] += 1


def audit_controls(unsupported_fields):
    named = (ZERO, chart(ELL), chart(JELL))
    for n in range(2, 9):
        empty_state = (EMPTY,) * (2*n-1), 0, 0
        need(step(empty_state) == empty_state, "empty-fixed", n)
        no_reaction_trial(n, empty_state, "absence")
        for y in unsupported_fields:
            no_reaction_trial(n, clean(n, y), "unsupported")
            arrival = clean(n, y)
            for _ in range(n-1):
                arrival = step(arrival)
            need(snapshot(arrival[0][-1]) == ("UNSUPPORTED",), "unsupported-snapshot", n, y)
        for y, r in product(named+unsupported_fields, (0, 1, 2, 10**30)):
            no_reaction_trial(n, clean(n, y, reserve=r, presence=0), "inactive")
        for y in named:
            bad = list(clean(n, y, reserve=0)[0])
            bad[-2] = (0, ZERO, 2)
            mismatch = tuple(bad), 0, 0
            need(accounts(mismatch)[0] == accounts(clean(n, y))[0], "mismatch-energy", n, y)
            no_reaction_trial(n, mismatch, "separate-funding")
            preloaded = clean(n, y, at=2*n-2)
            first = layers(preloaded)[0]
            need(first[0][-1] == (1, y, 0) and first[1:] == (1, encode(y)), "dirty-first-write", n, y)
            releasing = clean(n, y, reserve=7, latch=1, record=612, at=2*n-2)
            first = reaction(releasing)
            need(first[0][-1] == (1, y, 9) and first[1:] == (0, 612), "dirty-release", n, y)
            c = encode(y)
            for p0 in (0, 1, 612, 613, 1225, (-c) % MOD):
                state = clean(n, y, record=p0)
                for boundary in range(1, 2*(2*n-1)+1):
                    state = step(state)
                    expected = expected_clean(n, y, boundary, cycle_position(n, boundary), p0)
                    need(state == expected, "initial-record", n, y, p0, boundary)
                    if p0 == (-c) % MOD and boundary == n:
                        need(decode(state[2]) == ("BLANK",), "funded-first-blank", n, y)
                    COUNTS["initial_record_steps"] += 1
            for replacement in named+unsupported_fields:
                state = clean(n, replacement)
                for _ in range(n):
                    state = step(state)
                if energy_field(replacement) <= 5:
                    need(decode(state[2]) == ("VALUE", unchart(replacement), replacement), "replacement", n, y, replacement)
                else:
                    need(state[1:] == (0, 0), "unsupported-replacement", n, y, replacement)


def audit_periods(fields):
    for y in fields:
        c, record, first = encode(y), 0, None
        for k in range(1, MOD+1):
            record = (record+c) % MOD
            if record == 0 and first is None:
                first = k
        need(first == MOD//gcd(MOD, c), "modular-order", y, c, first)
        COUNTS["modular_additions"] += MOD
    for y in (ZERO, chart(ELL), chart(JELL)):
        initial = clean(2, y)
        state = initial
        bound = 6*MOD//gcd(MOD, encode(y))
        for boundary in range(1, bound+1):
            state = step(state)
            need((state == initial) == (boundary == bound), "exact-full-period", y, boundary, bound)
            COUNTS["period_steps"] += 1


def main():
    fields = audit_code()
    unsupported_fields = (chart((3, 0, 0, 0)), chart((10**6, 0, 0, 0)))
    audit_local(fields, unsupported_fields)
    audit_dirty(unsupported_fields)
    audit_clean(fields)
    audit_cuts_and_underfunding(fields)
    audit_controls(unsupported_fields)
    audit_periods(fields)
    print("independent packet transport audit: PASS")
    for name in sorted(COUNTS):
        print(name + "=" + str(COUNTS[name]))
    print("scope=finite audits plus separately frozen all-state/all-N derivation; L1 classical only")


if __name__ == "__main__":
    main()
