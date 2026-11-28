#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""NON-CANONICAL #2139. Pinned H3 law and literal predecessor preparation."""
from collections import Counter
from functools import cache, lru_cache
from itertools import product
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'reproduce/h3-referenced-record/verify.py'
NATIVE_SHA = '4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == NATIVE_SHA
spec = importlib.util.spec_from_file_location('material_read_native', SOURCE)
H = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = H
spec.loader.exec_module(H)
H.mul = lru_cache(maxsize=262144)(H.mul)
H.transport_pair = lru_cache(maxsize=262144)(H.transport_pair)
H.collision = lru_cache(maxsize=262144)(H.collision)
H.h = lru_cache(maxsize=262144)(H.h)
Z, O, R, RI, J, JI, P = H.ZERO, H.ONE, H.RHO, H.RHO_INV, H.J, H.J_INV, H.J_POWERS
add, sub, mul, sc = H.add, H.sub, H.mul, H.scale
neg = lambda a: sc(-1, a)
ETA = sub(O, R)
NY = 6
KEYS = tuple(product(range(2), range(5)))
ALL25 = tuple(product(range(5), repeat=2))
ARCH = (5, 7)
AUDIT = Counter()


def ix(x, y, rail):
    return H.index(NY, x, y, rail)


@cache
def q(z):
    n = 5 * sum(a * a for a in z) - sum(z) ** 2
    assert n % 2 == 0
    return n // 2


def account(field):
    hh = H.ring_sum(H.h(z) for z in field)
    result = (H.ring_sum(z for i, z in enumerate(field) if i % 4 < 2),
              H.ring_sum(z for i, z in enumerate(field) if i % 4 >= 2),
              hh, sum(q(z) for z in field))
    assert result[3] == H.scalar_account(hh)
    return result


def total_account(field, matstock=(), radstock=()):
    sm, sr, hh, qq = account(field)
    return (add(sm, H.ring_sum(matstock)), add(sr, H.ring_sum(radstock)),
            add(hh, H.ring_sum(H.h(z) for z in tuple(matstock) + tuple(radstock))),
            qq + sum(q(z) for z in tuple(matstock) + tuple(radstock)))


def col(field, x):
    return field[4 * NY * x:4 * NY * (x + 1)]


def cell(field, x, y):
    i = ix(x, y, 0)
    return field[i:i + 4]


def material(field, x=4):
    return tuple(field[ix(x, y, r)] for y, r in product(range(NY), (0, 1)))


def old_record(field):
    return tuple(z for x in ARCH for z in material(field, x))


def sum0(field):
    return H.ring_sum(field[ix(4, y, 0)] for y in range(NY))


def outside_material(field):
    return tuple(z for i, z in enumerate(field)
                 if not (i // (4 * NY) == 4 and i % 4 < 2))


def digest(value):
    data = json.dumps(value, separators=(',', ':'), ensure_ascii=True)
    return hashlib.sha256(data.encode('ascii')).hexdigest()


def clean_classes(fields, feature, classify):
    buckets = {}
    for key, field in fields.items():
        buckets.setdefault(classify(key), set()).add(feature(field))
    return (all(len(v) == 1 for v in buckets.values()) and
            len({next(iter(v)) for v in buckets.values()}) == len(buckets))


def tag_at(events, y, x=4):
    return next((tag for xx, yy, tag in events if (xx, yy) == (x, y)), 0)


def bare(p):
    m = sub(sc(2, O), R)
    gs = sc(2, mul(J, m))
    a = sc(-3, ETA)
    b = add(add(mul(m, R), mul(J, a)), sc(12, J))
    stock = (Z, Z, Z, b, b, b, add(mul(m, R), sc(2, a)))
    result = []
    for x, y in product(range(8), range(2)):
        d = (P[p] if y == 0 else sc(3, P[1])) if x == 0 else JI if x == 6 else Z
        g = gs if x == 0 else (6, -2, 12, 1) if x == 6 else Z
        c = (Z if x == 0 else stock[x - 1]) if y == 0 else gs
        result.extend((d, neg(d), g, c))
    return tuple(result)


D5 = ((33, 15, 24, 33), (-27, -12, -9, -21), (-18, -15, -12, -15),
      (-30, 9, -24, -9), (-21, 6, -27, -3), (9, 15, -6, 21))
G5 = ((-21, -8, 5, -36), (3, 28, -19, 30)) * 3
D7 = ((4, 12, 9, 0), (18, 13, 14, 10), (12, -5, 14, 4),
      (10, 8, 15, 2), (6, 4, 9, -4), (12, 8, 9, 6))
G7 = ((15, 10, 47, 3),) * 6
U = (1, -1, -3, 0, -3, 0)
V = (1, -1, 3, 0, -3, 0)
OFFSET = (-1, 4, 7, 3)
CLOCK = (31, 18, 27, 14)
INITIAL_ACCOUNT = ((-12, 24, 42, 18), (762, 588, 792, 429),
                   (54044, 0, 17904, 17904), 90184)
END121_SHA = 'fde15d156a9879098a6a93b3a3fe75b25b11f6c13f637eeb1f568e918a602060'


def initial(p):
    base = bare(p)
    field = []
    for x, y in product(range(8), range(NY)):
        i = H.index(2, x, y % 2, 0)
        values = tuple(mul(ETA, z) for z in base[i:i + 4])
        if x in ARCH:
            d, g = (D5[y], G5[y]) if x == 5 else (D7[y], G7[y])
            values = (d, neg(d), g, values[3])
        if x == 4:
            values = (sc(U[y], O), add(sc(3 * V[y], O), OFFSET), CLOCK, values[3])
        field.extend(values)
    return tuple(field)


def source_reserve(p):
    value = mul(ETA, P[p])
    return (value, neg(value)) * 3


def exchange(field, p, new):
    indices = tuple(ix(0, y, r) for y, r in product(range(0, NY, 2), (0, 1)))
    outgoing = tuple(field[i] for i in indices)
    assert outgoing == source_reserve(p)
    incoming = source_reserve(new)
    out = list(field)
    for i, z in zip(indices, incoming):
        out[i] = z
    out = tuple(out)
    assert total_account(field, incoming) == total_account(out, outgoing)
    back = list(out)
    for i, z in zip(indices, outgoing):
        back[i] = z
    assert tuple(back) == field
    AUDIT['source_swaps'] += 1
    return out, outgoing


def swap_material(field, donors, a):
    assert len(donors) == 2 and all(len(m) == 12 for m in donors)
    indices = tuple(ix(4, y, r) for y, r in product(range(NY), (0, 1)))
    out, stock = list(field), list(donors)
    stock[a] = tuple(field[i] for i in indices)
    for i, z in zip(indices, donors[a]):
        out[i] = z
    out, stock = tuple(out), tuple(stock)
    assert total_account(field, donors[0] + donors[1]) == total_account(out, stock[0] + stock[1])
    back = list(out)
    for i, z in zip(indices, stock[a]):
        back[i] = z
    assert tuple(back) == field and tuple(out[i] for i in indices) == donors[a]
    AUDIT['material_swaps'] += 1
    return out, stock


def advance(field, t, ac=None):
    bit = (t - 1) % 2
    if ac is None:
        ac = account(field)
    mid = H.transport(field, NY, bit)
    out, events = H.collide(mid, NY)
    back, _ = H.collide(out, NY)
    assert back == mid
    previous = H.transport(back, NY, bit, True)
    assert previous == field and H.transport(previous, NY, bit) == mid
    assert account(mid) == account(out) == ac
    AUDIT['ticks'] += 1
    AUDIT['checked_cuts'] += 2
    AUDIT['two_sided_inverses'] += 1
    return mid, out, events


def history(field, n):
    full, mids, events = [field], [None], [None]
    ac = account(field)
    for t in range(1, n + 1):
        mid, field, ev = advance(field, t, ac)
        full.append(field)
        mids.append(mid)
        events.append(ev)
    return full, mids, events


@cache
def prefix():
    starts = [initial(p) for p in range(5)]
    assert {account(f) for f in starts} == {INITIAL_ACCOUNT}
    assert {total_account(starts[p], source_reserve(new)) for p, new in ALL25} == {
        total_account(starts[0], source_reserve(0))}
    assert total_account(starts[0], source_reserve(0))[3] == 90214
    first = {p: history(starts[p], 114) for p in range(5)}
    for p, hh in first.items():
        assert all(col(hh[0][114], x) == col(starts[p], x) for x in (0, 6))
        assert not any(x == 4 for ev in hh[2][1:] for x, y, tag in ev)
    loaded25, reserves = {}, {}
    for p, new in ALL25:
        loaded25[p, new], reserves[p, new] = exchange(first[p][0][114], p, new)
    loaded = {key: loaded25[key] for key in KEYS}
    assert len(set(loaded25.values())) == 10
    assert all(f == loaded[int(p == 1), new] for (p, new), f in loaded25.items())
    second = {key: history(field, 121) for key, field in loaded.items()}
    assert digest([second[key][0][121] for key in KEYS]) == END121_SHA
    negative = sc(-6, O)
    positive = add(negative, sc(2, mul(ETA, R)))
    for t in range(89, 122):
        stages = (0,) if t == 89 else (1, 0)
        for stage in stages:
            fields = {key: hh[stage][t] for key, hh in second.items()}
            assert all(sum0(f) == (positive if key[1] == 1 else negative) for key, f in fields.items())
            assert clean_classes(fields, old_record, lambda k: k[0])
            assert clean_classes(fields, sum0, lambda k: int(k[1] == 1))
            assert clean_classes(fields, lambda f: (old_record(f), sum0(f)),
                                 lambda k: (k[0], int(k[1] == 1)))
        if t > 89:
            assert not any(x in (4, 5, 7) for hh in second.values() for x, y, tag in hh[2][t])
    return dict(starts=starts, first=first, second=second, loaded25=loaded25,
                source_reserves=reserves)


def print_prefix(data):
    print('BASIS', 'NATIVE_SHA256', NATIVE_SHA, 'FIELD_Q', INITIAL_ACCOUNT[3],
          'WITH_SOURCE_RESERVE_Q', total_account(data['starts'][0], source_reserve(0))[3],
          'ORDERED_INPUTS', 25, 'EVOLVING_FIELD_REPRESENTATIVES', 10,
          'RESERVES_RETAIN_ORIGINAL_INPUTS', True, 'END121_SHA256', END121_SHA)
