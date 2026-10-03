#!/usr/bin/env python3
"""NON-CANONICAL classical packet law; execute only after its complete pin.

All-state theorems and all-N/time claims rest on PROOF.md. This program audits
exact declared finite domains. APIs take only admitted mathematical states,
represented by plain builtin tuples and genuine integers; no object parser.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd
import json
import sys


MODULUS = 1226
ZERO = (0, 0, 0, 0)
EMPTY = (0, ZERO, 0)
BOX = ((-3, 3), (-2, 2), (-2, 2), (-3, 3))


def chart(a):
    a0, a1, a2, a3 = a
    return a1, a2-a3, a0-a1-a3, a1-2*a2+a3


def coefficients(y):
    a, b, c, d = y
    return 2*a-2*b+c-d, a, a-b-d, a-2*b-d


def h(y):
    a, b, c, d = y
    return (2*a*a - 2*a*b + 3*b*b + c*c + d*d
            + 2*a*c - a*d - b*c + 3*b*d)


def energies_from_coefficients(a):
    a0, a1, a2, a3 = a
    q = sum(x*x for x in a)
    return q-a0*a2-a0*a3-a1*a3, q-a0*a1-a1*a2-a2*a3


def supported(packet):
    return packet[0] == 1 and h(packet[1]) <= 5


def code(y):
    assert h(y) <= 5
    a0, a1, a2, a3 = coefficients(y)
    assert all(lo <= x <= hi for x, (lo, hi) in zip((a0, a1, a2, a3), BOX))
    return 1 + (((a0+3)*5+(a1+2))*5+(a2+2))*7+(a3+3)


def record_read(p):
    assert type(p) is int and 0 <= p < MODULUS
    if p == 0:
        return ("BLANK",)
    q, d3 = divmod(p-1, 7)
    q, d2 = divmod(q, 5)
    d0, d1 = divmod(q, 5)
    a = d0-3, d1-2, d2-2, d3-3
    y = chart(a)
    return ("INVALID",) if h(y) > 5 else ("VALUE", a, y)


def packet_read(packet):
    if packet[0] == 0:
        return ("ABSENT",)
    if not supported(packet):
        return ("UNSUPPORTED",)
    y = packet[1]
    return "VALUE", coefficients(y), y


def e5(y):
    a = coefficients(y)
    e0, e1 = energies_from_coefficients(a)
    return e0, e1, tuple(x % 5 for x in a)


def accepted_write(state):
    cells, _channels, latch, _pointer = state
    return latch == 0 and supported(cells[-1]) and cells[-1][2] >= 2


def reaction(state, inverse=False):
    cells, channels, latch, pointer = state
    presence, y, reserve = cells[-1]
    if not supported(cells[-1]):
        return state
    c = code(y)
    if inverse:
        if latch == 1:
            reserve, latch, pointer = reserve+2, 0, (pointer-c) % MODULUS
        elif reserve >= 2:
            reserve, latch = reserve-2, 1
        else:
            return state
    else:
        if latch == 1:
            reserve, latch = reserve+2, 0
        elif reserve >= 2:
            reserve, latch, pointer = reserve-2, 1, (pointer+c) % MODULUS
        else:
            return state
    cells = cells[:-1] + ((presence, y, reserve),)
    return cells, channels, latch, pointer


def contact(state, which, cut=None):
    cells, channels, latch, pointer = state
    cells, channels = list(cells), list(channels)
    assert which in ("A", "B")
    for j in range(len(channels)):
        if j == cut:
            continue
        i = j if which == "A" else j+1
        cells[i], channels[j] = channels[j], cells[i]
    return tuple(cells), tuple(channels), latch, pointer


def apply_layer(state, which, cut=None):
    if which == "G":
        return reaction(state)
    if which == "GI":
        return reaction(state, inverse=True)
    return contact(state, which, cut)


def step(state, cut=None, inverse=False):
    for which in (("B", "A", "GI") if inverse else ("G", "A", "B")):
        state = apply_layer(state, which, cut)
    return state


def packets(state):
    return state[0] + state[1]


def energy(state):
    return sum(b+h(y)+r for b, y, r in packets(state)) + 2*state[2] + 1


def account(state):
    return (energy(state), Counter((b, y) for b, y, _r in packets(state)),
            sum(r for _b, _y, r in packets(state)) + 2*state[2])


def assert_admitted(state):
    assert type(state) is tuple and len(state) == 4
    cells, channels, latch, pointer = state
    assert type(cells) is type(channels) is tuple
    assert len(cells) >= 2 and len(channels) == len(cells)-1
    assert type(latch) is int and latch in (0, 1)
    assert type(pointer) is int and 0 <= pointer < MODULUS
    for packet in packets(state):
        assert type(packet) is tuple and len(packet) == 3
        b, y, r = packet
        assert type(b) is int and b in (0, 1)
        assert type(y) is tuple and len(y) == 4
        assert all(type(x) is int for x in y)
        assert type(r) is int and r >= 0


def assert_accounts(before, after):
    assert_admitted(after)
    assert account(before) == account(after)


def assert_roundtrip(state, cut=None):
    assert step(step(state, cut), cut, inverse=True) == state
    assert step(step(state, cut, inverse=True), cut) == state


def from_flat(n, flat, latch=0, pointer=0):
    assert len(flat) == 2*n-1
    return tuple(flat[:n]), tuple(flat[n:]), latch, pointer


def clean(n, y, reserve=2, pointer=0):
    flat = [(1, y, reserve)] + [EMPTY] * (2*n-2)
    return from_flat(n, flat, pointer=pointer)


def sector_audit():
    fields, oracle, shells = [], {}, Counter()
    scanned = 0
    for a in product(*(range(lo, hi+1) for lo, hi in BOX)):
        scanned += 1
        y = chart(a)
        assert coefficients(y) == a
        e0, e1 = energies_from_coefficients(a)
        assert h(y) == e0 >= 0
        if e0 > 5:
            continue
        c = code(y)
        assert 1 <= c < MODULUS and c not in oracle
        oracle[c] = ("VALUE", a, y)
        assert record_read(c) == oracle[c]
        assert packet_read((1, y, 0)) == oracle[c]
        assert e5(y) == (e0, e1, tuple(x % 5 for x in a))
        fields.append(y)
        shells[e0] += 1
    assert scanned == 1225 and len(fields) == 291
    counts = [shells[i] for i in range(6)]
    assert counts == [1, 20, 30, 60, 60, 120]
    tags = Counter()
    for p in range(MODULUS):
        expected = ("BLANK",) if p == 0 else oracle.get(p, ("INVALID",))
        assert record_read(p) == expected
        tags[expected[0]] += 1
    assert tags == {"BLANK": 1, "VALUE": 291, "INVALID": 934}
    assert code(ZERO) == 613
    assert packet_read(EMPTY) == ("ABSENT",)
    assert packet_read((1, ZERO, 2)) == ("VALUE", ZERO, ZERO)
    left, right = chart((1, -1, -1, 1)), chart((-1, 0, -2, -2))
    assert h(left) == h(right) == 5
    assert (code(left), code(right)) == (747, 422)
    ratios = []
    for y in (left, right):
        a = coefficients(y)
        q, total = sum(x*x for x in a), sum(a)
        ratios.append(Fraction(total*total, 4*(5*q-total*total)))
        assert energy(clean(2, y)) == 9
    assert ratios == [Fraction(0), Fraction(5, 16)]
    return tuple(fields), {"box_scanned": scanned, "states": len(fields),
                           "shells": counts, "record_tags": dict(tags),
                           "stored_zero_code": 613, "source_pair_codes": [747, 422]}


def local_audit(fields):
    choices = fields + (chart((3, 0, 0, 0)), chart((10**6, 0, 0, 0)))
    cases = 0
    for y, b, r, latch in product(choices, range(2), range(5), range(2)):
        c = code(y) if h(y) <= 5 else 1
        for pointer in (0, 1, 613, 1225, (-c) % MODULUS):
            state = ((EMPTY, (b, y, r)), (EMPTY,), latch, pointer)
            event = accepted_write(state)
            out = reaction(state)
            inv = reaction(state, inverse=True)
            assert reaction(out, inverse=True) == state
            assert reaction(inv) == state
            assert_accounts(state, out)
            assert_accounts(state, inv)
            assert out[0][0] == state[0][0] and out[1] == state[1]
            assert out[0][-1][:2] == state[0][-1][:2]
            assert out[3] == (pointer + (code(y) if event else 0)) % MODULUS
            if not supported((b, y, r)) or (latch == 0 and r < 2):
                assert out == state
            elif latch == 0:
                assert event and out[0][-1][2] == r-2 and out[2] == 1
            else:
                assert not event and out[0][-1][2] == r+2 and out[2] == 0
            cases += 1
    assert cases == 29300
    return cases


def occupied_audit():
    ell, jell = chart((1, -1, -1, 1)), chart((-1, 0, -2, -2))
    # Frozen ten-packet list. All contents survive; b=0 never clears y or r.
    fixture = (EMPTY, (1, ZERO, 0), (1, ZERO, 1), (1, ZERO, 2),
               (1, ell, 2), (1, jell, 4), (0, ell, 3),
               (1, chart((3, 0, 0, 0)), 2),
               (0, chart((10**6, 0, 0, 0)), 0), (1, chart((1, 0, 0, 0)), 0))
    cases = layers = 0
    for n in range(2, 7):
        for cut in (None,) + tuple(range(n-1)):
            for k in range(32):
                flat = tuple(fixture[(k+3*j+(k % 3)*j*j) % len(fixture)]
                             for j in range(2*n-1))
                state = from_flat(n, flat, k % 2, 37*k % MODULUS)
                assert_admitted(state)
                assert_roundtrip(state, cut)
                for inverse in (False, True):
                    current = state
                    for which in (("B", "A", "GI") if inverse else ("G", "A", "B")):
                        after = apply_layer(current, which, cut)
                        assert_accounts(current, after)
                        if cut is not None:
                            assert after[1][cut] == state[1][cut]
                        current = after
                        layers += 1
                cases += 1
    assert cases == 640 and layers == 3840
    return {"states": cases, "layer_accounts": layers}


def cycle_slot(n, phase):
    position = phase % (2*n-1)
    return position if position < n else n+(2*n-2-position)


def after_a_slot(n, slot):
    if slot < n-1:
        return n+slot
    if slot >= n:
        return slot-n
    return slot


def expected_single(n, y, boundary, which, start_phase=0, initial_latch=0, p0=0):
    """Closed visit-count/position formulas, not calls to the dynamics."""
    period = 2*n-1
    first = ((n-1-start_phase) % period) + 1
    visits = 0 if boundary < first else 1+(boundary-first)//period
    latch = (initial_latch+visits) % 2
    writes = (visits+1)//2 if initial_latch == 0 else visits//2
    pointer = (p0+writes*code(y)) % MODULUS
    slot = cycle_slot(n, start_phase+boundary)
    if which in ("G", "A"):
        slot = cycle_slot(n, start_phase+boundary-1)
        if which == "A":
            slot = after_a_slot(n, slot)
    flat = [EMPTY] * period
    flat[slot] = (1, y, 2*(1-latch))
    return from_flat(n, flat, latch, pointer)


def audit_single(n, y, horizon, p0=0, start_phase=0, initial_latch=0,
                 check_inverses=False):
    initial = expected_single(n, y, 0, "B", start_phase, initial_latch, p0)
    state = initial
    initial_account = account(initial)
    comparisons = 0
    period = 2*n-1
    for boundary in range(1, horizon+1):
        for which in ("G", "A", "B"):
            before = state
            state = apply_layer(state, which)
            expected = expected_single(n, y, boundary, which, start_phase, initial_latch, p0)
            assert state == expected
            assert_accounts(before, state)
            assert account(state) == initial_account
            if check_inverses:
                assert_roundtrip(state)
            expected_reader = (("VALUE", coefficients(y), y)
                               if state[0][-1][0] == 1 else ("ABSENT",))
            assert packet_read(state[0][-1]) == expected_reader
            # The record reader is exercised locally with p only.
            result = record_read(state[3])
            assert result[0] in ("BLANK", "INVALID", "VALUE")
            comparisons += 1
        if start_phase == 0 and initial_latch == 0:
            if boundary == n-1:
                assert packet_read(state[0][-1]) == ("VALUE", coefficients(y), y)
                assert state[0][-1][2] == 2
            if p0 == 0 and n <= boundary < n+2*period:
                assert record_read(state[3]) == ("VALUE", coefficients(y), y)
            if boundary % (2*period) == 0:
                assert state[:3] == initial[:3]
                assert state[3] == (p0+(boundary//(2*period))*code(y)) % MODULUS
    return comparisons, state


def positive_audit(fields):
    comparisons = runs = 0
    for n in range(2, 7):
        period = 2*n-1
        for y in fields:
            count, final = audit_single(n, y, 4*period, check_inverses=True)
            assert final[:3] == clean(n, y)[:3]
            assert final[3] == 2*code(y) % MODULUS
            comparisons += count
            runs += 1
    assert runs == 1455 and comparisons == 122220
    return {"runs": runs, "layer_comparisons": comparisons}


def cut_audit(fields):
    runs = layers = 0
    for n in range(2, 5):
        for y in fields:
            for cut in range(n-1):
                state = clean(n, y)
                frozen_channel = state[1][cut]
                for _ in range(2*(2*n-1)):
                    for which in ("G", "A", "B"):
                        before = state
                        state = apply_layer(state, which, cut)
                        assert_accounts(before, state)
                        assert state[0][-1] == EMPTY and state[2:] == (0, 0)
                        assert state[1][cut] == frozen_channel
                        layers += 1
                runs += 1
    assert runs == 1746
    return {"runs": runs, "layer_accounts": layers}


def no_event_run(state, horizon):
    layers = 0
    for _ in range(horizon):
        for which in ("G", "A", "B"):
            before = state
            state = apply_layer(state, which)
            assert_accounts(before, state)
            assert state[2:] == (0, 0)
            if which == "G":
                assert state == before and not accepted_write(before)
            layers += 1
    return layers


def controls_audit():
    sources = (ZERO, chart((1, -1, -1, 1)), chart((-1, 0, -2, -2)))
    unsupported = (chart((3, 0, 0, 0)), chart((10**6, 0, 0, 0)))
    no_event_runs = no_event_layers = dirty_runs = dirty_layers = 0
    for n in range(2, 7):
        period, horizon = 2*n-1, 2*(2*n-1)
        absent = from_flat(n, [EMPTY] * period)
        assert step(absent) == absent
        no_event_layers += no_event_run(absent, horizon)
        no_event_runs += 1
        for y in sources:
            for reserve in (0, 1):
                no_event_layers += no_event_run(clean(n, y, reserve), horizon)
                no_event_runs += 1
            inactive = from_flat(n, [(0, y, 2)] + [EMPTY]*(period-1))
            no_event_layers += no_event_run(inactive, horizon)
            no_event_runs += 1
            flat = [(1, y, 0)] + [EMPTY]*(period-1)
            flat[-1] = (0, ZERO, 2)
            mismatch = from_flat(n, flat)
            assert energy(mismatch) == energy(clean(n, y))
            no_event_layers += no_event_run(mismatch, horizon)
            no_event_runs += 1
            for initial_latch in (0, 1):
                preloaded = expected_single(n, y, 0, "B", n-1, initial_latch, 0)
                after_g = reaction(preloaded)
                if initial_latch == 0:
                    assert accepted_write(preloaded)
                    assert after_g[2:] == (1, code(y))
                    assert after_g[0][-1][2] == 0
                else:
                    assert not accepted_write(preloaded)
                    assert after_g[2:] == (0, 0)
                    assert after_g[0][-1][2] == 2
                count, _final = audit_single(n, y, horizon, start_phase=n-1,
                                             initial_latch=initial_latch)
                dirty_layers += count
                dirty_runs += 1
            for p0 in (0, 1, 613, 1225, (-code(y)) % MODULUS):
                count, _final = audit_single(n, y, horizon, p0=p0)
                dirty_layers += count
                dirty_runs += 1
                if p0 == (-code(y)) % MODULUS:
                    at_write = expected_single(n, y, n, "G", p0=p0)
                    assert at_write[3] == 0
        for y in unsupported:
            state = clean(n, y)
            no_event_layers += no_event_run(state, horizon)
            no_event_runs += 1
            assert packet_read((1, y, 2)) == ("UNSUPPORTED",)
    return {"no_event_runs": no_event_runs, "no_event_layers": no_event_layers,
            "dirty_runs": dirty_runs, "dirty_layer_comparisons": dirty_layers}


def modular_audit(fields):
    additions = 0
    for y in fields:
        c = code(y)
        first_return = None
        pointer = 0
        for k in range(1, MODULUS+1):
            pointer = (pointer+c) % MODULUS
            if pointer == 0 and first_return is None:
                first_return = k
            additions += 1
        assert first_return == MODULUS // gcd(MODULUS, c)
        assert pointer == 0
    assert additions == 291*MODULUS
    return {"codes": len(fields), "additions": additions}


def main():
    if sys.flags.optimize:
        raise RuntimeError("Exact audit requires assertions enabled")
    fields, sector = sector_audit()
    local = local_audit(fields)
    occupied = occupied_audit()
    positive = positive_audit(fields)
    cuts = cut_audit(fields)
    controls = controls_audit()
    modular = modular_audit(fields)
    result = {"candidate": "C-FIELD-J-CONTENT-TRANSPORT-N", "layer": "L1",
              "status": "PASS", "sector": sector, "local_gate_cases": local,
              "occupied": occupied, "positive": positive, "cuts": cuts,
              "controls": controls, "modular_record": modular,
              "scope": "selected_classical_law_not_coherent_or_native_U"}
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
