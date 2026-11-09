#!/usr/bin/env python3
"""Exact prospective audit for P-J-SIGN-REMOTE-HOLD-1 (NON-CANONICAL, L1).

No files, network, subprocesses, random inputs or floating-point arithmetic.
The two ring arithmetics and the finite-state oracle are one author's work.
Execute only after the complete scientific source pin has been published and
read back. Importing this module is not a permitted pre-pin scientific test.
"""
import hashlib
import itertools
import json
import sys
from collections import Counter
from functools import lru_cache

Z = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
JROOT = (0, 1, 0, 0)
RHO = (0, 0, 1, 0)
J = (1, 0, 1, 0)
JINV = (0, -1, -1, 0)
G = (2, 0, 1, 1)
W = (-1, -1, 0, -1)
BLANK = ("BLANK",)
COUNTS = Counter()
STREAMS = {name: hashlib.sha256() for name in
           ("primitive", "full_states", "layers", "returns", "negative")}


def demand(condition, message):
    if not condition:
        raise AssertionError(message)


def feed(name, row):
    STREAMS[name].update((json.dumps(row, sort_keys=True, separators=(",", ":"),
                                    ensure_ascii=True) + "\n").encode("ascii"))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(a, n):
    return tuple(n * x for x in a)


def half(a):
    demand(not any(x & 1 for x in a), "nonintegral half")
    return tuple(x // 2 for x in a)


def mul(a, b):
    c = [0] * 7
    for i in range(4):
        for k in range(4):
            c[i + k] += a[i] * b[k]
    for degree in (6, 5, 4):
        v = c[degree]
        c[degree] = 0
        for k in range(4):
            c[degree - 4 + k] -= v
    return tuple(c[:4])


def conjugate(a):
    x, y, z, w = a
    return (x - y, -y, w - y, z - y)


@lru_cache(maxsize=None)
def herm(a):
    return mul(a, conjugate(a))


@lru_cache(maxsize=None)
def q(a):
    numerator = 5 * sum(x * x for x in a) - sum(a) ** 2
    demand(numerator % 2 == 0, "nonintegral q")
    value = numerator // 2
    hh = herm(a)
    demand(2 * value == 4 * hh[0] - sum(hh[1:]), "q/trace disagreement")
    demand(value >= 0 and (value == 0) == (a == Z), "positive account")
    return value


def invariants(state):
    total = [0] * 4
    hh = [0] * 4
    ee = 0
    for a in state:
        ha = herm(a)
        for i in range(4):
            total[i] += a[i]
            hh[i] += ha[i]
        ee += q(a)
    return tuple(total), tuple(hh), ee


@lru_cache(maxsize=None)
def gate(cells):
    x, y, p, r = cells
    xy, pr = sub(x, y), sub(p, r)
    if any(a & 1 for a in xy + pr):
        return cells, "PARITY"
    c, d, u, v = half(add(x, y)), half(add(p, r)), half(xy), half(pr)
    forward = u != Z and herm(v) == mul(G, herm(u))
    reverse = v != Z and herm(u) == mul(G, herm(v))
    demand(not (forward and reverse), "overlapping balance branches")
    if forward:
        uu, vv, branch = mul(J, u), mul(JINV, v), "FORWARD"
    elif reverse:
        uu, vv, branch = mul(JINV, u), mul(J, v), "REVERSE"
    else:
        return cells, "BALANCE"
    return (add(c, uu), sub(c, uu), add(d, vv), sub(d, vv)), branch


# Separate cyclic-five representation: convolution modulo X^5-1, followed
# by quotienting the all-ones vector. No calls to mul/conjugate/herm/gate.
def canon5(a):
    return tuple(x - a[4] for x in a)


def lift5(a):
    return a + (0,)


def plus5(a, b):
    return canon5(tuple(a[i] + b[i] for i in range(5)))


def minus5(a, b):
    return canon5(tuple(a[i] - b[i] for i in range(5)))


def product5(a, b):
    c = [0] * 5
    for i in range(5):
        for k in range(5):
            c[(i + k) % 5] += a[i] * b[k]
    return canon5(c)


def h5(a):
    return product5(a, tuple(a[(-i) % 5] for i in range(5)))


def half5(a):
    demand(all(x % 2 == 0 for x in a), "cyclic nonintegral half")
    return tuple(x // 2 for x in a)


def gate5(cells):
    x, y, p, r = cells
    dx, dp = minus5(x, y), minus5(p, r)
    if any(x % 2 for x in dx + dp):
        return cells, "PARITY"
    c, d = half5(plus5(x, y)), half5(plus5(p, r))
    u, v = half5(dx), half5(dp)
    zero = (0,) * 5
    gg = (2, 0, 1, 1, 0)
    jj, ji = (1, 0, 1, 0, 0), (0, -1, -1, 0, 0)
    f = u != zero and h5(v) == product5(gg, h5(u))
    b = v != zero and h5(u) == product5(gg, h5(v))
    demand(not (f and b), "cyclic overlapping branches")
    if f:
        u, v, branch = product5(jj, u), product5(ji, v), "FORWARD"
    elif b:
        u, v, branch = product5(ji, u), product5(jj, v), "REVERSE"
    else:
        return cells, "BALANCE"
    return (plus5(c, u), minus5(c, u), plus5(d, v), minus5(d, v)), branch


def invariants5(state):
    ss = (0,) * 5
    hh = (0,) * 5
    ee = 0
    for a in state:
        ss = plus5(ss, a)
        ha = h5(a)
        hh = plus5(hh, ha)
        tr = 5 * ha[0] - sum(ha)
        demand(tr % 2 == 0, "cyclic odd account trace")
        ee += tr // 2
    return ss[:4], hh[:4], ee


def primitive_inventory():
    alphabet = (Z, ONE, neg(ONE), JROOT, neg(JROOT), J, neg(J), JINV, neg(JINV))
    for cells in itertools.product(alphabet, repeat=4):
        out, branch = gate(cells)
        alt, alt_branch = gate5(tuple(lift5(x) for x in cells))
        demand(out == tuple(x[:4] for x in alt), "primitive arithmetic mismatch")
        demand(branch == alt_branch, "primitive branch mismatch")
        demand(gate(out)[0] == cells, "primitive inverse")
        demand(gate5(alt)[0] == tuple(lift5(x) for x in cells), "cyclic inverse")
        before = invariants(cells)
        demand(invariants(out) == before, "primitive conservation")
        demand(invariants5(tuple(lift5(x) for x in cells)) == before,
               "cyclic input invariants")
        demand(invariants5(alt) == before, "cyclic output invariants")
        demand(add(out[0], out[1]) == add(cells[0], cells[1]) and
               add(out[2], out[3]) == add(cells[2], cells[3]), "marked sums")
        if branch in ("PARITY", "BALANCE"):
            demand(out == cells, "rejected branch not identity")
        COUNTS["primitive_cases"] += 1
        COUNTS["primitive_" + branch.lower()] += 1
        feed("primitive", [cells, branch, out, before])


LOW, HIGH = (ONE, neg(ONE)), (J, neg(J))


class Geometry:
    def __init__(self, d, hold):
        self.d, self.hold = d, hold
        self.L = 2 * d + hold + 3
        self.P = 2 * self.L + 4
        self.m = 2 * self.L
        self.clock_sites = 2 * self.P
        self.clock_offset = 4 + 2 * self.m
        self.raw_cells = self.clock_offset + 2 * self.clock_sites
        self.tau = d + 2
        self.r = 2 * d
        self.layers = [((0, 1, 2, 3),), ((1, 2, 3, 0),), ((2, 3, 4, 5),)]
        for start in (0, 1):
            blocks = []
            for offset, sites in ((4, self.m), (self.clock_offset, self.clock_sites)):
                for i in range(start, sites, 2):
                    j = (i + 1) % sites
                    blocks.append((offset + 2*i, offset + 2*i + 1,
                                   offset + 2*j, offset + 2*j + 1))
            flat = [i for block in blocks for i in block]
            demand(len(flat) == len(set(flat)), "non-disjoint matching layer")
            self.layers.append(tuple(blocks))
        demand(self.raw_cells == 12 * self.L + 20, "raw cell budget")
        demand(self.m - (self.r + 2*hold + 3) >= 2*d,
               "short reverse route to receiver")


def source(label, sign):
    first = (2*sign, 0, 0, 0)
    ca, cb = (2*sign, 0, sign, 0), (0, 0, -sign, 0)
    if label == "A":
        return (first, Z, W, neg(W))
    if label == "C":
        return (ca, cb, RHO, neg(RHO))
    if label == "D":
        return (first, Z, RHO, neg(RHO))
    if label == "Z":
        return (ca, cb, W, neg(W))
    demand(label == "B" and sign == 1, "unknown source oracle label")
    return ((2, 0, 0, 0), neg(W), W, Z)


def raw_from_labels(geom, sign, label, data_highs, clock_high):
    out = list(source(label, sign))
    for i in range(geom.m):
        out.extend(HIGH if i in data_highs else LOW)
    for i in range(geom.clock_sites):
        out.extend(HIGH if i == clock_high else LOW)
    return tuple(out)


def prepare(geom, sign, funded_launch=True):
    return raw_from_labels(geom, sign, "A", {0} if funded_launch else set(), 0)


def apply_layer(state, geom, layer):
    out = list(state)
    for block in geom.layers[layer]:
        values = tuple(out[i] for i in block)
        updated, unused_branch = gate(values)
        for i, value in zip(block, updated):
            out[i] = value
    COUNTS["gate_applications"] += len(geom.layers[layer])
    return tuple(out)


def full_step(state, geom):
    for layer in range(5):
        state = apply_layer(state, geom, layer)
    return state


# This oracle manipulates only proof labels and bit positions. It never
# calls the raw gate, its balance predicate, its parity test, or its matrices.
class LayerOracle:
    def __init__(self, geom, sign):
        self.g, self.sign = geom, sign
        self.label, self.highs, self.clock = "A", {0}, 0

    def step(self, layer):
        if layer == 0:
            self.label = {"A": "C", "C": "A"}.get(self.label, self.label)
        elif layer == 1:
            if self.sign == 1:
                self.label = {"C": "B", "B": "C"}.get(self.label, self.label)
        elif layer == 2:
            incoming = 0 in self.highs
            if self.label in ("A", "Z") and not incoming:
                self.label = {"A": "D", "Z": "C"}[self.label]
                self.highs.add(0)
            elif self.label in ("C", "D") and incoming:
                self.label = {"C": "Z", "D": "A"}[self.label]
                self.highs.remove(0)
        else:
            self.highs = {(i + 1) % self.g.m for i in self.highs}
            self.clock = (self.clock + 1) % self.g.clock_sites

    def raw(self):
        return raw_from_labels(self.g, self.sign, self.label, self.highs, self.clock)


def closed_form(geom, sign, tick):
    L = geom.L
    if sign == 1:
        n = tick % geom.P
        if n == 0:
            label, high_q = "A", {0}
        elif n == 1:
            label, high_q = "B", {1}
        elif n == 2:
            label, high_q = "C", {2}
        elif n <= L:
            label, high_q = "D", {n % L, (n-2) % L}
        elif n == L+1:
            label, high_q = "A", {L-1}
        elif n == L+2:
            label, high_q = "B", {0}
        elif n == L+3:
            label, high_q = "Z", set()
        elif n == L+4:
            label, high_q = "C", {1}
        else:
            label, high_q = "D", {(n-L-3) % L, (n-L-4) % L}
    else:
        n = tick % (L+2)
        if n == 0:
            label, high_q = "A", {0}
        elif n == 1:
            label, high_q = "Z", set()
        elif n == 2:
            label, high_q = "C", {1}
        else:
            label, high_q = "D", {(n-1) % L, (n-2) % L}
    return raw_from_labels(geom, sign, label, {2*i for i in high_q},
                           (2*tick) % geom.clock_sites)


def local_highs(state, offset, first, last):
    found = []
    for i in range(first, last + 1):
        pair = state[offset+2*i:offset+2*i+2]
        if pair == HIGH:
            found.append(i)
        elif pair != LOW:
            return None
    return found


def data_reader(state, geom, anchor_shift=0, swap_gaps=False):
    highs = local_highs(state, 4, geom.r, geom.r + 2*geom.hold + 3)
    if highs is None or len(highs) != 2:
        return BLANK
    s, t = highs
    if not geom.r + anchor_shift <= s <= geom.r + 2*geom.hold - 1 + anchor_shift:
        return BLANK
    positive_gap, negative_gap = (2, 4) if swap_gaps else (4, 2)
    if t-s == positive_gap:
        return ("VALUE", 1)
    if t-s == negative_gap:
        return ("VALUE", -1)
    return BLANK


def enabled(state, geom):
    highs = local_highs(state, geom.clock_offset, 2*geom.tau,
                        2*(geom.tau + geom.hold)-1)
    return highs is not None and len(highs) == 1


def reader(state, geom, anchor_shift=0, swap_gaps=False):
    return data_reader(state, geom, anchor_shift, swap_gaps) if enabled(state, geom) else BLANK


def expected_tag(geom, sign, tick):
    phase = tick % geom.P
    return ("VALUE", sign) if geom.tau <= phase < geom.tau + geom.hold else BLANK


def check_boundary(state, geom, sign, tick, layer, oracle):
    demand(state == oracle.raw(), "layer raw-state oracle mismatch")
    expected_inv = ((2*sign, 0, 0, 0), (12*geom.L+28, 0, 6, 6), 24*geom.L+50)
    actual_inv = invariants(state)
    demand(actual_inv == expected_inv, "whole H/E/S conservation")
    semantic_tick = tick if layer == 4 else tick-1
    want = expected_tag(geom, sign, semantic_tick)
    actual = reader(state, geom)
    demand(actual == want, "layer reader contract")
    demand(enabled(state, geom) == (want != BLANK), "local clock corridor")
    COUNTS["invariant_boundaries"] += 1
    COUNTS["layer_oracle_checks"] += 1
    COUNTS["layer_tags"] += 1
    if actual != BLANK:
        COUNTS["readable_layer_boundaries"] += 1
    feed("layers", [geom.d, geom.hold, sign, tick, layer, state[:4],
                    sorted(oracle.highs), oracle.clock, actual, actual_inv])


def check_return_table(history, geom, sign):
    L = geom.L
    if sign == 1:
        events = ((0,"A",{0}), (1,"B",{1}), (2,"C",{2}), (3,"D",{3,1}),
                  (L+1,"A",{L-1}), (L+2,"B",{0}), (L+3,"Z",set()),
                  (L+4,"C",{1}), (L+5,"D",{2,1}),
                  (2*L+3,"D",{0,L-1}), (2*L+4,"A",{0}))
    else:
        events = ((0,"A",{0}), (1,"Z",set()), (2,"C",{1}), (3,"D",{2,1}),
                  (L+1,"D",{0,L-1}), (L+2,"A",{0}))
    for tick, label, highs in events:
        want = raw_from_labels(geom, sign, label, {2*i for i in highs},
                               (2*tick) % geom.clock_sites)
        demand(history[tick] == want, "exact recurrence event")
        COUNTS["return_events"] += 1
        feed("returns", [geom.d, geom.hold, sign, tick, label, sorted(highs)])
    for period in (1, 2, 3):
        demand(history[period*geom.P] == history[0], "complete common return")
        COUNTS["complete_returns"] += 1
    data_end = geom.clock_offset
    data_period = geom.P if sign == 1 else geom.L+2
    demand(history[data_period][:data_end] == history[0][:data_end], "data return")
    COUNTS["data_returns"] += 1


def run_family(geom, sign):
    state = prepare(geom, sign)
    oracle = LayerOracle(geom, sign)
    initial_inv = ((2*sign,0,0,0), (12*geom.L+28,0,6,6), 24*geom.L+50)
    demand(invariants(state) == initial_inv, "initial complete budget")
    demand(state == oracle.raw() == closed_form(geom, sign, 0), "initial oracle")
    demand(reader(state, geom) == BLANK, "receiver not initially blank-tagged")
    COUNTS["families"] += 1
    COUNTS["invariant_boundaries"] += 1
    COUNTS["initial_oracle_checks"] += 1
    COUNTS["full_boundaries"] += 1
    history = [state]
    feed("full_states", [geom.d, geom.hold, sign, 0, state, BLANK])
    for tick in range(1, 3*geom.P + 1):
        previous = state
        for layer in range(5):
            before_layer = state
            state = apply_layer(state, geom, layer)
            oracle.step(layer)
            check_boundary(state, geom, sign, tick, layer, oracle)
            demand(apply_layer(state, geom, layer) == before_layer, "literal layer inverse")
            COUNTS["layer_inverse_checks"] += 1
        demand(state == closed_form(geom, sign, tick), "closed-form full-state oracle")
        backward = state
        for layer in (4, 3, 2, 1, 0):
            backward = apply_layer(backward, geom, layer)
        demand(backward == previous, "literal full inverse")
        COUNTS["full_inverse_checks"] += 1
        COUNTS["full_ticks"] += 1
        COUNTS["full_boundaries"] += 1
        COUNTS["closed_form_checks"] += 1
        if tick <= 3:
            COUNTS["encoder_ticks"] += 1
        if reader(state, geom) != BLANK:
            COUNTS["readable_full_boundaries"] += 1
        history.append(state)
        feed("full_states", [geom.d, geom.hold, sign, tick, state, reader(state, geom)])
    check_return_table(history, geom, sign)
    # Exact first arrival, hold and expiry, independently of aggregate counts.
    demand(all(reader(history[t],geom) == BLANK for t in range(geom.tau)), "early tag")
    demand(all(reader(history[t],geom) == ("VALUE",sign)
               for t in range(geom.tau, geom.tau+geom.hold)), "first hold")
    demand(reader(history[geom.tau+geom.hold],geom) == BLANK, "first expiry")
    COUNTS["first_windows"] += 1
    return history


def family_negatives(histories, geom):
    positive, negative = histories[1], histories[-1]
    for j in range(geom.hold):
        wrong_tick = geom.L + geom.d + 4 + j
        right_tick = geom.tau + j
        bad, good = positive[wrong_tick], negative[right_tick]
        demand(data_reader(bad, geom) == ("VALUE",-1), "missing unclocked false passage")
        demand(reader(bad, geom) == BLANK, "clock did not suppress false passage")
        demand(reader(good, geom) == ("VALUE",-1), "negative first-window read")
        demand(bad[4:geom.clock_offset] == good[4:geom.clock_offset], "whole data-rail alias")
        COUNTS["unclocked_alias_points"] += 1
        feed("negative", ["alias", geom.d, geom.hold, wrong_tick, right_tick,
                          bad[4:geom.clock_offset]])
    for sign in (1,-1):
        removed = prepare(geom, sign, funded_launch=False)
        reduced_inv = ((2*sign,0,0,0), (12*geom.L+26,0,4,4), 24*geom.L+48)
        demand(invariants(removed) == reduced_inv, "unfunded initial budget")
        for tick in range(1, geom.tau + geom.hold + 1):
            removed = full_step(removed, geom)
            demand(invariants(removed) == reduced_inv, "unfunded budget conservation")
            highs = local_highs(removed,4,0,geom.m-1)
            demand(highs is not None and len(highs) <= 1, "unfunded rail not unary")
            demand(reader(removed,geom) == BLANK, "unfunded variant unexpectedly records")
            if tick == 3:
                want = raw_from_labels(geom,sign,"D",{2 if sign == 1 else 4},6)
                demand(removed == want, "unfunded three-tick encoder")
                COUNTS["removed_launch_encoder_checks"] += 1
            if geom.tau <= tick < geom.tau + geom.hold:
                COUNTS["removed_launch_failed_hold_points"] += 1
            COUNTS["removed_launch_ticks"] += 1
            feed("negative", ["removed_launch",geom.d,geom.hold,sign,tick,
                              removed[:4],highs,reader(removed,geom),reduced_inv])
        COUNTS["removed_launch_cases"] += 1
        arrival = histories[sign][geom.tau]
        demand(reader(arrival,geom,anchor_shift=1) == BLANK, "shifted anchor not detected")
        demand(reader(arrival,geom,swap_gaps=True) == ("VALUE",-sign), "swapped gap not detected")
        COUNTS["shifted_anchor_cases"] += 1
        COUNTS["swapped_gap_cases"] += 1
        feed("negative", ["reader_changes",geom.d,geom.hold,sign])
        for name, offset in (
                ("invalid_data_reader_cases",4+2*(geom.r+1)),
                ("invalid_clock_reader_cases",geom.clock_offset+2*(2*geom.tau+1))):
            demand(arrival[offset:offset+2] == LOW, "invalid-code control changed a pulse")
            malformed = list(arrival)
            malformed[offset:offset+2] = (Z,Z)
            demand(reader(tuple(malformed),geom) == BLANK, "invalid receiver code accepted")
            COUNTS[name] += 1
            feed("negative",[name,geom.d,geom.hold,sign,offset])


def graft_controls():
    for sign in (1,-1):
        a = source("A",sign)
        b0 = gate(a)[0]
        rotated = gate((b0[1],b0[2],b0[3],b0[0]))[0]
        after = (rotated[3],rotated[0],rotated[1],rotated[2])
        payer = after[2:4]
        demand(payer not in (LOW,HIGH), "direct writer output unexpectedly canonical")
        graft, branch = gate(payer + LOW)
        demand(graft == payer + LOW, "direct low-rail graft unexpectedly updates")
        if sign == 1:
            demand(payer == (W,Z) and branch == "PARITY", "positive graft parity boundary")
        else:
            demand(payer == (RHO,neg(RHO)) and branch == "BALANCE", "negative graft balance boundary")
        COUNTS["fixed_pair_graft_cases"] += 1
        feed("negative", ["graft",sign,payer,branch])


def main():
    demand(sys.flags.optimize == 0, "assertions must remain enabled")
    demand(mul(J,JINV) == ONE and mul(J,RHO) == W and herm(J) == G, "ring constants")
    primitive_inventory()
    graft_controls()
    for d in range(1,9):
        for hold in range(1,9):
            geom = Geometry(d,hold)
            plus, minus = prepare(geom,1), prepare(geom,-1)
            demand(plus[1:] == minus[1:] and plus[0] == neg(minus[0]), "common apparatus")
            demand(invariants(plus)[1:] == invariants(minus)[1:], "common full account")
            COUNTS["common_preparations"] += 1
            histories = {sign: run_family(geom,sign) for sign in (1,-1)}
            family_negatives(histories,geom)
    expected = {"primitive_cases":6561, "families":128, "full_ticks":14208,
                "full_boundaries":14336, "layer_tags":71040,
                "layer_oracle_checks":71040, "initial_oracle_checks":128,
                "invariant_boundaries":71168, "layer_inverse_checks":71040,
                "full_inverse_checks":14208, "closed_form_checks":14208,
                "return_events":1088, "encoder_ticks":384,
                "complete_returns":384, "data_returns":128,
                "first_windows":128, "common_preparations":64,
                "unclocked_alias_points":288, "removed_launch_cases":128,
                "removed_launch_ticks":1408, "removed_launch_encoder_checks":128,
                "removed_launch_failed_hold_points":576,
                "fixed_pair_graft_cases":2, "shifted_anchor_cases":128,
                "swapped_gap_cases":128, "invalid_data_reader_cases":128,
                "invalid_clock_reader_cases":128, "readable_full_boundaries":1728,
                "readable_layer_boundaries":8640}
    for key,value in expected.items():
        demand(COUNTS[key] == value, "inventory count: " + key)
    report = {"probe":"P-J-SIGN-REMOTE-HOLD-1", "result":"PASS",
              "counts":dict(sorted(COUNTS.items())),
              "sha256":{key:value.hexdigest() for key,value in sorted(STREAMS.items())}}
    print(json.dumps(report,sort_keys=True,separators=(",",":"),ensure_ascii=True))


if __name__ == "__main__":
    main()
