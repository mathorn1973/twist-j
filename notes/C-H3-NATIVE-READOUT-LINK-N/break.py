#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Blind same-session audit of C-H3-NATIVE-READOUT-LINK-N.

NON-CANONICAL / NO AUTHORITY. Standalone cyclic-five native engine.
No new primary source or results were read before this source freeze.
Predecessor engine portions come from the author's earlier frozen checker.
"""

from collections import Counter
from functools import cache, lru_cache
from itertools import product
import hashlib
import json
from pathlib import Path


Z = (0, 0, 0, 0, 0)
O = (1, 0, 0, 0, 0)
NY = 6
NX = 8


def norm5(a):
    return tuple(x - a[4] for x in a)


def ring(a):
    if isinstance(a, int):
        return (a, 0, 0, 0, 0)
    return tuple(a) + (0,)


def plus(a, b):
    return tuple(x + y for x, y in zip(a, b))


def minus(a, b):
    return tuple(x - y for x, y in zip(a, b))


def times(n, a):
    return tuple(n * x for x in a)


@lru_cache(maxsize=200000)
def multiply(a, b):
    out = [0] * 5
    for i in range(5):
        for k in range(5):
            out[(i + k) % 5] += a[i] * b[k]
    return norm5(out)


def rotate(a, k):
    return norm5(tuple(a[(i - k) % 5] for i in range(5)))


def star(a):
    return norm5(tuple(a[-i % 5] for i in range(5)))


@cache
def herm(a):
    return multiply(a, star(a))


@cache
def q(a):
    numerator = 5 * sum(x * x for x in a) - sum(a) ** 2
    assert numerator % 2 == 0
    return numerator // 2


def total(aa):
    out = Z
    for a in aa:
        out = plus(out, a)
    return out


def is_even(a):
    return all(x % 2 == 0 for x in a)


def half(a):
    assert is_even(a)
    return tuple(x // 2 for x in a)


ROOTS = tuple(rotate(O, k) for k in range(5))
RHO, RI = ROOTS[2], ROOTS[3]
J = plus(O, RHO)
JI = ring((0, -1, -1, 0))
ETA = minus(O, RHO)
HJ = herm(J)
DELTA = multiply(ETA, RHO)


@lru_cache(maxsize=200000)
def cp(a, b, inverse=False):
    delta = minus(a, b)
    if not is_even(delta):
        return a, b
    d = half(delta)
    center = plus(b, d)
    moved = rotate(d, 3 if inverse else 2)
    return plus(center, moved), minus(center, moved)


@lru_cache(maxsize=200000)
def bp(cell):
    a, b, g, r = cell
    ab, gr = minus(a, b), minus(g, r)
    if not is_even(ab) or not is_even(gr):
        return cell, 0
    d, f = half(ab), half(gr)
    if d != Z and herm(f) == multiply(HJ, herm(d)):
        next_d, next_f, tag = multiply(J, d), multiply(JI, f), 1
    elif f != Z and herm(d) == multiply(HJ, herm(f)):
        next_d, next_f, tag = multiply(JI, d), multiply(J, f), 2
    else:
        return cell, 0
    md, rf = plus(b, d), plus(r, f)
    return (plus(md, next_d), minus(md, next_d),
            plus(rf, next_f), minus(rf, next_f)), tag


def site(x, y):
    return x * NY + y


def transport(field, bit, inverse=False):
    out = [list(c) for c in field]
    for x in range(NX):
        for y in range(bit, NY, 2):
            i, k = site(x, y), site(x, (y + 1) % NY)
            for rail in (0, 1, 2):
                out[i][rail], out[k][rail] = cp(field[i][rail], field[k][rail], inverse)
    for x in range(bit, NX, 2):
        for y in range(NY):
            i, k = site(x, y), site((x + 1) % NX, y)
            out[i][3], out[k][3] = cp(field[i][3], field[k][3], inverse)
    return tuple(tuple(c) for c in out)


def collide(field):
    states, events = [], []
    for n, c in enumerate(field):
        z, tag = bp(c)
        states.append(z)
        if tag:
            events.append((*divmod(n, NY), tag))
    return tuple(states), tuple(events)


def accounts(field):
    material = total(z for c in field for z in c[:2])
    radiation = total(z for c in field for z in c[2:])
    h = total(herm(z) for c in field for z in c)
    scalar = sum(q(z) for c in field for z in c)
    assert 4 * h[0] - sum(h[1:]) == 2 * scalar
    return material, radiation, h, scalar


def step(field, bit, budget):
    middle = transport(field, bit)
    after, events = collide(middle)
    assert accounts(middle) == accounts(after) == budget
    undone, _ = collide(after)
    assert undone == middle
    assert transport(undone, bit, True) == field
    assert transport(transport(field, bit, True), bit) == field
    return middle, after, events


def history(initial, horizon, bit=0):
    AUDIT["histories"] += 1
    AUDIT["ticks"] += horizon
    AUDIT["cuts"] += 2 * horizon + 1
    budget = accounts(initial)
    full, middle, events = [initial], [None], [None]
    for t in range(horizon):
        g, z, ev = step(full[-1], (t + bit) % 2, budget)
        full.append(z)
        middle.append(g)
        events.append(ev)
    return full, middle, events


# Literal initial vectors for the older selected apparatus. Both material
# rails are retained, with opposite values. These are not new search results.
C5D = tuple(map(ring, ((33, 15, 24, 33), (-27, -12, -9, -21),
    (-18, -15, -12, -15), (-30, 9, -24, -9), (-21, 6, -27, -3), (9, 15, -6, 21))))
C5G = tuple(map(ring, ((-21, -8, 5, -36), (3, 28, -19, 30)))) * 3
C7D = tuple(map(ring, ((4, 12, 9, 0), (18, 13, 14, 10), (12, -5, 14, 4),
    (10, 8, 15, 2), (6, 4, 9, -4), (12, 8, 9, 6))))
C7G = (ring((15, 10, 47, 3)),) * 6


def original_first(p):
    m = minus(times(2, O), RHO)
    gs = times(2, multiply(J, m))
    a = times(-3, ETA)
    b = plus(plus(multiply(m, RHO), multiply(J, a)), times(12, J))
    stock = (Z, Z, Z, b, b, b, plus(multiply(m, RHO), times(2, a)))
    field = []
    for x, y in product(range(NX), range(NY)):
        d = (ROOTS[p] if y % 2 == 0 else times(3, ROOTS[1])) if x == 0 else JI if x == 6 else Z
        g = gs if x == 0 else ring((6, -2, 12, 1)) if x == 6 else Z
        r = (Z if x == 0 else stock[x - 1]) if y % 2 == 0 else gs
        cell = tuple(multiply(ETA, z) for z in (d, times(-1, d), g, r))
        if x in (5, 7):
            dd, gg = (C5D, C5G) if x == 5 else (C7D, C7G)
            cell = dd[y], times(-1, dd[y]), gg[y], cell[3]
        field.append(cell)
    return tuple(field)


def exchange(field, old_p, fresh_q):
    new = list(field)
    incoming, outgoing = [], []
    old = multiply(ETA, ROOTS[old_p])
    fresh = multiply(ETA, ROOTS[fresh_q])
    for y in range(0, NY, 2):
        i = site(0, y)
        assert field[i][:2] == (old, times(-1, old))
        outgoing.append((*field[i][:2], Z, Z))
        incoming.append((fresh, times(-1, fresh), Z, Z))
        new[i] = (fresh, times(-1, fresh), *field[i][2:])
    result = tuple(new)
    assert accounts(result) == accounts(field)
    assert accounts(field + tuple(incoming)) == accounts(result + tuple(outgoing))
    return result


def column(field, x):
    return field[site(x, 0):site(x, 0) + NY]



AUDIT = Counter()

KEYS = tuple(product(range(2), range(5)))
ACTUAL = tuple(product(range(5), repeat=2))


def short(z):
    return z[:4]


def emit(kind, value):
    print(kind, json.dumps(value, separators=(",", ":"), sort_keys=True), flush=True)


def encoded(field):
    return tuple(short(z) for cell in field for z in cell)


def field_digest(field):
    return hashlib.sha256(json.dumps(encoded(field), separators=(",", ":"), ensure_ascii=True).encode()).hexdigest()


def fields_digest(fields):
    return hashlib.sha256(json.dumps(tuple(encoded(f) for f in fields), separators=(",", ":"), ensure_ascii=True).encode()).hexdigest()


def sum_accounts(*aa):
    return tuple(total(a[i] for a in aa) for i in range(3)) + (sum(a[3] for a in aa),)


def stock_account(material=(), radiation=()):
    zz = material + radiation
    return total(material), total(radiation), total(herm(z) for z in zz), sum(q(z) for z in zz)


def initial(p):
    out = list(original_first(p))
    u, v = (1, -1, -3, 0, -3, 0), (1, -1, 3, 0, -3, 0)
    c, g = ring((-1, 4, 7, 3)), ring((31, 18, 27, 14))
    for y in range(NY):
        i = site(4, y)
        assert out[i][:3] == (Z, Z, Z)
        out[i] = ring(u[y]), plus(ring(3 * v[y]), c), g, out[i][3]
    return tuple(out)


def source_swap(field, p, q0):
    old = tuple(z for y in range(0, NY, 2) for z in field[site(0, y)][:2])
    new = exchange(field, p, q0)
    assert exchange(new, q0, p) == field
    incoming = tuple(z for y in range(0, NY, 2) for z in new[site(0, y)][:2])
    assert stock_account(material=old) == stock_account(material=incoming)
    assert stock_account(material=old)[0] == Z and stock_account(material=old)[3] == 30
    AUDIT["source_swaps"] += 1
    return new, old


def bank(field):
    return tuple(z for cell in column(field, 4) for z in cell[:2])


def old_record(field):
    return tuple(z for x in (5, 7) for cell in column(field, x) for z in cell[:2])


def s0(field):
    return total(cell[0] for cell in column(field, 4))


def bank_swap(field, material):
    assert len(material) == 12
    outgoing = bank(field)
    out = list(field)
    for y in range(NY):
        i = site(4, y)
        out[i] = material[2 * y], material[2 * y + 1], *out[i][2:]
    out = tuple(out)
    undo = list(out)
    for y in range(NY):
        i = site(4, y)
        undo[i] = outgoing[2 * y], outgoing[2 * y + 1], *undo[i][2:]
    assert tuple(undo) == field and bank(out) == material
    assert sum_accounts(accounts(field), stock_account(material=material)) == sum_accounts(accounts(out), stock_account(material=outgoing))
    AUDIT["material_swaps"] += 1
    return out, outgoing


def probe_swap(field, y, f):
    yc = (y + 1) % NY if y % 2 else (y - 1) % NY
    positions = ((4, y, 2), (4, yc, 2), (4, y, 3), (3, y, 3))
    stock = (f, f, times(-1, f), times(-1, f))
    old = tuple(field[site(x, yy)][rail] for x, yy, rail in positions)
    out = [list(cell) for cell in field]
    for (x, yy, rail), z in zip(positions, stock):
        out[site(x, yy)][rail] = z
    out = tuple(tuple(cell) for cell in out)
    undo = [list(cell) for cell in out]
    for (x, yy, rail), z in zip(positions, old):
        undo[site(x, yy)][rail] = z
    assert tuple(tuple(cell) for cell in undo) == field
    assert sum_accounts(accounts(field), stock_account(radiation=stock)) == sum_accounts(accounts(out), stock_account(radiation=old))
    assert stock_account(radiation=stock)[1] == Z
    assert stock_account(radiation=stock)[2] == times(4, herm(f))
    assert stock_account(radiation=stock)[3] == 4 * q(f)
    AUDIT["radiation_swaps"] += 1
    return out, old


def class_failure(fields, projection, label):
    by_label, by_value = {}, {}
    for key, field in fields.items():
        lab, value = label(key), projection(field)
        if lab in by_label and by_label[lab][1] != value:
            return ("split", key, by_label[lab][0])
        if value in by_value and by_value[value][1] != lab:
            return ("collision", key, by_value[value][0])
        by_label[lab] = (key, value)
        by_value[value] = (key, lab)
    return None


def outside_equal(a, b):
    return all((ca == cb if n // NY != 4 else ca[2:] == cb[2:])
               for n, (ca, cb) in enumerate(zip(a, b)))


def tags(hist, t):
    out = [0] * NY
    for x, y, tag in hist[2][t]:
        if x == 4:
            out[y] = tag
    return tuple(out)


def actual_fields(histories, stage, t):
    return {(p, q0): histories[int(p == 1), q0][stage][t] for p, q0 in ACTUAL}


def material_column(field, x):
    return tuple(z for cell in column(field, x) for z in cell[:2])


def positions(rails, columns=range(NX)):
    return tuple((x, y, r) for x in columns for y in range(NY) for r in rails)


MAT = positions((0, 1))
RAD = positions((2, 3))
OLD = positions((0, 1), (5, 7))
BANK = positions((0, 1), (4,))
SOURCE = positions((0, 1), (0,))
SIX = tuple((0, y, r) for y in (0, 2, 4) for r in (0, 1))


def pick(field, pp):
    return tuple(field[site(x, y)][r] for x, y, r in pp)


def replace(field, pp, incoming, kind):
    assert kind in ("M", "R") and len(pp) == len(incoming)
    assert len(set(pp)) == len(pp)
    assert all((r < 2) == (kind == "M") for _, _, r in pp)
    outgoing = pick(field, pp)
    out = [list(c) for c in field]
    for (x, y, r), z in zip(pp, incoming):
        out[site(x, y)][r] = z
    out = tuple(tuple(c) for c in out)
    undo = [list(c) for c in out]
    for (x, y, r), z in zip(pp, outgoing):
        undo[site(x, y)][r] = z
    assert tuple(tuple(c) for c in undo) == field
    assert pick(out, pp) == incoming
    before_stock = stock_account(material=incoming) if kind == "M" else stock_account(radiation=incoming)
    after_stock = stock_account(material=outgoing) if kind == "M" else stock_account(radiation=outgoing)
    assert sum_accounts(accounts(field), before_stock) == sum_accounts(accounts(out), after_stock)
    AUDIT["typed_swaps"] += 1
    return out, outgoing


def source_stock(exponent):
    z = multiply(ETA, ROOTS[exponent])
    return (z, times(-1, z)) * 3


def prepare():
    first = {p: history(initial(p), 114) for p in range(5)}
    expected = (ring((-12, 24, 42, 18)), ring((762, 588, 792, 429)), ring((54044, 0, 17904, 17904)), 90184)
    assert all(accounts(initial(p)) == expected for p in range(5))
    starts, reserve = {}, {}
    for p, q0 in ACTUAL:
        starts[p, q0], reserve[p, q0] = source_swap(first[p][0][114], p, q0)
    assert len(set(starts.values())) == 10
    assert len({(starts[k], 0, reserve[k]) for k in ACTUAL}) == 25
    for p, q0 in ACTUAL:
        assert starts[p, q0] == starts[int(p == 1), q0]
    second = {k: history(starts[k], 121) for k in KEYS}
    digest = fields_digest(second[k][0][121] for k in KEYS)
    assert digest == "fde15d156a9879098a6a93b3a3fe75b25b11f6c13f637eeb1f568e918a602060"
    emit("BREAK BASIS", {"endpoint121": digest, "fields": 10, "compound": 25})
    return first, second, reserve


def reverse_history(final, n):
    """Inverse of n ticks with the original zero initial matching bit."""
    full = [None] * (n + 1)
    middle = [None] * (n + 1)
    events = [None] * (n + 1)
    full[n] = final
    budget = accounts(final)
    for t in range(n, 0, -1):
        m, _ = collide(full[t])
        previous = transport(m, (t - 1) % 2, True)
        mm, after, ev = step(previous, (t - 1) % 2, budget)
        assert mm == m and after == full[t]
        assert accounts(m) == accounts(previous) == budget
        full[t - 1], middle[t], events[t] = previous, m, ev
    AUDIT["inverse_histories"] += 1
    AUDIT["inverse_ticks"] += n
    AUDIT["inverse_cuts"] += 2 * n + 1
    return full, middle, events


def first_field_disagreement(pulled, reference, coords):
    for key in ACTUAL:
        for x, y, r in coords:
            a, b = pulled[key][site(x, y)][r], reference[key][site(x, y)][r]
            if a != b:
                return {"input": key, "coordinate": (x, y, r), "pulled": short(a), "reference": short(b)}
    return None


def common_replacement(pulled, reference, source_reserves):
    material_bad = first_field_disagreement(pulled, reference, MAT)
    support = tuple(pos for pos in RAD if any(pick(pulled[k], (pos,)) != pick(reference[k], (pos,)) for k in ACTUAL))
    incoming, noncommon = [], None
    for pos in support:
        distinct = {}
        for k in ACTUAL:
            distinct.setdefault(pick(pulled[k], (pos,))[0], k)
        if len(distinct) != 1 and noncommon is None:
            noncommon = {"coordinate": pos, "values": tuple((k, short(z)) for z, k in distinct.items())}
        incoming.append(next(iter(distinct)))
    passed = material_bad is None and noncommon is None
    out = {"pass": passed, "support": support, "first_material": material_bad, "first_noncommon": noncommon}
    if passed:
        stock = tuple(incoming)
        common_accounts = None
        outgoing = []
        for k in ACTUAL:
            assembled, removed = replace(reference[k], support, stock, "R")
            assert assembled == pulled[k]
            total_before = sum_accounts(accounts(reference[k]), stock_account(material=source_reserves[k], radiation=stock))
            total_after = sum_accounts(accounts(pulled[k]), stock_account(material=source_reserves[k], radiation=removed))
            assert total_before == total_after
            if common_accounts is None:
                common_accounts = total_before
            assert total_before == common_accounts
            outgoing.append(tuple(short(z) for z in removed))
        out.update(incoming=tuple(short(z) for z in stock),
                   stock_accounts=tuple(short(z) for z in stock_account(radiation=stock)[:3]) + (stock_account(radiation=stock)[3],),
                   total_accounts=tuple(short(z) for z in common_accounts[:3]) + (common_accounts[3],),
                   outgoing_digest=hashlib.sha256(json.dumps(outgoing, separators=(",", ":")).encode()).hexdigest())
    return out


def path_failure(pulls, baseline, start, end, coords, include_start_mid=False):
    for t in range(start, end + 1):
        stages = (1, 0) if (t > start or include_start_mid) and t > 0 else (0,)
        for stage in stages:
            pp = {k: pulls[k][stage][t] for k in ACTUAL}
            ff = {k: baseline[int(k[0] == 1), k[1]][stage][t] for k in ACTUAL}
            bad = first_field_disagreement(pp, ff, coords)
            if bad is not None:
                return {"relative": t, "stage": "post-C" if stage else "full", **bad}
    return None


def delivery(first, second, source_reserves):
    candidates = ((107, 3, 2), (107, 3, 1), (93, 0, 2), (93, 0, 1), (89, 0, 2), (89, 0, 1))
    for s, y, tag in candidates:
        a, b = second[0, 1][1][s + 1][site(4, y)][:2]
        diff = minus(a, b)
        assert diff != Z and is_even(diff)
        d = half(diff)
        f = multiply(JI if tag == 2 else J, d)
        rep_pulls, targets = {}, {}
        for key in KEYS:
            target, _ = probe_swap(second[key][0][s], y, f)
            targets[key] = target
            rep_pulls[key] = reverse_history(target, s)
        pulls = {k: rep_pulls[int(k[0] == 1), k[1]] for k in ACTUAL}
        first_pulls, recovered = {}, {}
        for p, q0 in ACTUAL:
            before_swap, got = replace(pulls[p, q0][0][0], SIX, source_reserves[p, q0], "M")
            recovered[p, q0] = got
            first_pulls[p, q0] = reverse_history(before_swap, 114)
        reserve_bad = next(({"input": k, "got": tuple(short(z) for z in recovered[k]),
                             "expected": tuple(short(z) for z in source_stock(k[1]))}
                            for k in ACTUAL if recovered[k] != source_stock(k[1])), None)
        initial_pulled = {k: first_pulls[k][0][0] for k in ACTUAL}
        initial_reference = {k: initial(k[0]) for k in ACTUAL}
        incoming_sources = {k: source_stock(k[1]) for k in ACTUAL}
        original_start = common_replacement(initial_pulled, initial_reference, incoming_sources)
        source_before = first_field_disagreement(
            {k: first_pulls[k][0][114] for k in ACTUAL},
            {k: first[k[0]][0][114] for k in ACTUAL}, SOURCE)
        source_after = first_field_disagreement(
            {k: pulls[k][0][0] for k in ACTUAL}, actual_fields(second, 0, 0), SOURCE)
        old_before = first_field_disagreement(
            {k: first_pulls[k][0][114] for k in ACTUAL},
            {k: first[k[0]][0][114] for k in ACTUAL}, OLD)
        old_after = path_failure(pulls, second, 0, s, OLD)
        bank_after = path_failure(pulls, second, 89, s, BANK, include_start_mid=True)
        whole_material = None
        for t in range(115):
            for stage in ((0,) if t == 0 else (1, 0)):
                bad = first_field_disagreement(
                    {k: first_pulls[k][stage][t] for k in ACTUAL},
                    {k: first[k[0]][stage][t] for k in ACTUAL}, MAT)
                if bad is not None:
                    whole_material = {"phase": "first", "absolute": t,
                                      "stage": "post-C" if stage else "full", **bad}
                    break
            if whole_material is not None:
                break
        if whole_material is None:
            whole_material = path_failure(pulls, second, 0, s, MAT)
        late = []
        for t in range(s + 1):
            pp = {k: pulls[k][0][t] for k in ACTUAL}
            ff = actual_fields(second, 0, t)
            criterion = common_replacement(pp, ff, source_reserves)
            if criterion["pass"]:
                late.append({"cut": t, "lead": s - t, "criterion": criterion,
                             "bank_path_failure": path_failure(pulls, second, t, s, BANK),
                             "old_path_failure": path_failure(pulls, second, t, s, OLD)})
        strict = original_start["pass"] and all(x is None for x in
                    (reserve_bad, source_before, source_after, old_before, old_after, bank_after))
        emit("BREAK A", {"label": (s, y, tag), "f": short(f), "strict_original_start": strict,
                         "initial_criterion": original_start, "recovered_source_failure": reserve_bad,
                         "source_before_failure": source_before, "source_after_failure": source_after,
                         "old_before_failure": old_before, "old_after_failure": old_after,
                         "bank_failure": bank_after, "whole_material_failure": whole_material,
                         "late_passing": late, "earliest_late": late[0]["cut"] if late else None,
                         "target_fields_digest": fields_digest(targets[k] for k in KEYS),
                         "target_ordered25_digest": fields_digest(targets[int(p == 1), q0] for p, q0 in ACTUAL),
                         "relative_zero_fields_digest": fields_digest(rep_pulls[k][0][0] for k in KEYS),
                         "relative_zero_ordered25_digest": fields_digest(pulls[k][0][0] for k in ACTUAL),
                         "absolute_zero_fields_digest": fields_digest(first_pulls[k][0][0] for k in ACTUAL),
                         "target_field_source_digest": digest_json(tuple(
                             (encoded(targets[int(p == 1), q0]), s % 2,
                              tuple(short(z) for z in source_reserves[p, q0])) for p, q0 in ACTUAL)),
                         "absolute_zero_field_source_digest": digest_json(tuple(
                             (encoded(first_pulls[k][0][0]), 0,
                              tuple(short(z) for z in recovered[k])) for k in ACTUAL)),
                         "recovered_sources_digest": hashlib.sha256(json.dumps(tuple(tuple(short(z) for z in recovered[k]) for k in ACTUAL), separators=(",", ":")).encode()).hexdigest(),
                         "audit": dict(AUDIT)})
        clear_caches()


CONTROL = tuple(product(range(5), range(5), range(2)))
RECEIVER = positions((0, 1), (6,))


def account_encoding(a):
    return tuple(short(z) for z in a[:3]) + (a[3],)


def value_encoding(value):
    """Canonical display of a ring-valued feature, cell, or vector."""
    if isinstance(value, tuple):
        if len(value) == 5 and all(isinstance(x, int) for x in value):
            assert value[4] == 0
            return short(value)
        return tuple(value_encoding(x) for x in value)
    return value


def digest_json(value):
    return hashlib.sha256(json.dumps(value, separators=(",", ":"), ensure_ascii=True).encode()).hexdigest()


def clear_caches():
    for function in (multiply, herm, q, cp, bp):
        function.cache_clear()


def module(mode, m, k):
    """One common, finite, exactly specified full107 stock."""
    f = ring((-3, -5, -4, 0))
    v = times(m, ROOTS[k])
    ev = multiply(multiply(ETA, ETA), v)
    b = minus(times(-1, multiply(J, f)), times(8, v))
    dr = times(-1, multiply(J, ev))
    rad = {}
    for x, y in product(range(NX), range(NY)):
        rad[x, y, 2] = f if x == 4 else b if x == 6 else plus(b, J)
        rad[x, y, 3] = b
    einv = minus(O, RI)
    rad[4, 3, 2] = plus(f, einv)
    rad[4, 4, 2] = plus(f, plus(O, RI))
    rad[4, 3, 3] = minus(times(-1, f), einv)
    rad[3, 3, 3] = minus(times(-1, f), plus(O, RI))
    if mode == "DRAIN":
        cplus = plus(b, multiply(plus(times(2, O), RHO), ev))
        rad[7, 3, 3] = rad[0, 3, 3] = plus(cplus, times(2, O))
    else:
        assert mode == "SEALED"
    material = (dr, times(-1, dr)) * NY
    radiation = tuple(rad[pos] for pos in RAD)
    assert len(material) == 12 and len(radiation) == 96
    return material, radiation, {"f": f, "v": v, "b": b, "dr": dr, "ev": ev}


def reserves_account(reserves):
    return sum_accounts(*(stock_account(material=values) if kind == "M"
                          else stock_account(radiation=values)
                          for _, kind, values in reserves))


def compound_encoding(field, bit, reserves):
    return (encoded(field), bit,
            tuple((name, kind, tuple(short(z) for z in values))
                  for name, kind, values in reserves))


def assemble_families(second, source_reserves, material, radiation):
    donors = bank(second[0, 0][0][107]), bank(second[0, 1][0][107])
    common_stock = stock_account(material=material, radiation=radiation)
    pool, families = {}, {}
    for family, keys in (("actual", ACTUAL), ("crossed", CONTROL)):
        records, common_budget = {}, None
        for key in keys:
            p, q0 = key[:2]
            field = second[int(p == 1), q0][0][107]
            reserves = (("source", "M", source_reserves[p, q0]),)
            if family == "crossed":
                a = key[2]
                before = sum_accounts(accounts(field), reserves_account(reserves),
                                      stock_account(material=donors[0] + donors[1]), common_stock)
                field, displaced = replace(field, BANK, donors[a], "M")
                donor_reserves = list(donors)
                donor_reserves[a] = displaced
                reserves += tuple(("donor" + str(i), "M", donor_reserves[i]) for i in range(2))
            else:
                before = sum_accounts(accounts(field), reserves_account(reserves), common_stock)
            prior = field
            field, removed_material = replace(field, RECEIVER, material, "M")
            field, removed_radiation = replace(field, RAD, radiation, "R")
            assert all(pick(field, (pos,)) == pick(prior, (pos,))
                       for pos in MAT if pos[0] != 6)
            reserves += (("worker", "M", removed_material), ("radiation", "R", removed_radiation))
            after = sum_accounts(accounts(field), reserves_account(reserves))
            assert before == after
            if common_budget is None:
                common_budget = before
            assert before == common_budget
            if field not in pool:
                pool[field] = history(field, 35, bit=1)
            h = pool[field]
            assert h[0][0] == field
            assert sum_accounts(accounts(h[0][35]), reserves_account(reserves)) == before
            records[key] = {"history": h, "reserves": reserves,
                            "preassembly": prior, "budget": before}
            AUDIT["compound_assemblies"] += 1
            AUDIT["compound_final_checks"] += 1
        assert len(records) == (25 if family == "actual" else 50)
        families[family] = records
    return families, pool


def native_tag(h, index, x, y):
    return next((tag for xx, yy, tag in h[2][index] if (xx, yy) == (x, y)), 0)


def mismatch(got, wanted, key, t, stage, clause):
    if got == wanted:
        return None
    return {"input": key, "relative": t, "stage": stage, "clause": clause,
            "got": value_encoding(got), "expected": value_encoding(wanted)}


def contacts(records, family, second, parameters):
    f, v, b, dr, ev = (parameters[name] for name in ("f", "v", "b", "dr", "ev"))
    failures = {name: None for name in ("first_contact", "buffer", "receiver", "old_archive")}

    def check(name, got, wanted, key, t, stage, clause):
        bad = mismatch(got, wanted, key, t, stage, clause)
        if failures[name] is None and bad is not None:
            failures[name] = bad

    for key, record in records.items():
        a = key[2] if family == "crossed" else int(key[1] == 1)
        h = record["history"]
        initial_cell = h[0][0][site(4, 3)]
        mid108, full108 = h[1][1][site(4, 3)], h[0][1][site(4, 3)]
        prior = record["preassembly"]
        expected_m = tuple(cp(prior[site(4, 3)][r], prior[site(4, 4)][r])[0] for r in (0, 1))
        check("first_contact", mid108[:2], expected_m, key, 108, "post-C", "transported material")
        check("first_contact", mid108[2:], (f, times(-1, f)), key, 108, "post-C", "arriving radiation")
        check("first_contact", (initial_cell[2] != mid108[2], initial_cell[3] != mid108[3]),
              (True, True), key, 108, "post-C", "both radiation entries moved")
        check("first_contact", h[1][1][site(4, 4)][2], plus(f, times(2, O)),
              key, 108, "post-C", "CLK companion")
        check("first_contact", h[1][1][site(3, 3)][3], minus(times(-1, f), times(2, O)),
              key, 108, "post-C", "CORR companion")
        check("first_contact", native_tag(h, 1, 4, 3), 2 * a,
              key, 108, "full", "contact tag")
        fout = multiply(J, f) if a else f
        check("first_contact", full108[2:], (fout, times(-1, fout)),
              key, 108, "full", "emitted radiation")
        buffer_value = plus(b, times(4, multiply(ETA, v))) if a else b
        check("buffer", h[1][2][site(5, 3)][3], buffer_value,
              key, 109, "post-C", "arriving buffer CORR")
        check("buffer", native_tag(h, 2, 5, 3), 0, key, 109, "full", "buffer tag")
        check("buffer", h[0][2][site(5, 3)][3], buffer_value,
              key, 109, "full", "emitted buffer CORR")
        receiver_in = (dr, times(-1, dr), b, plus(b, times(2, ev)) if a else b)
        check("receiver", h[1][3][site(6, 3)], receiver_in,
              key, 110, "post-C", "receiver arrival")
        check("receiver", native_tag(h, 3, 6, 3), 2 * a,
              key, 110, "full", "receiver tag")
        receiver_out = ((times(-1, ev), ev, minus(b, multiply(RHO, ev)),
                         plus(b, multiply(plus(times(2, O), RHO), ev))) if a
                        else (dr, times(-1, dr), b, b))
        check("receiver", h[0][3][site(6, 3)], receiver_out,
              key, 110, "full", "receiver write")
    for i in range(4):
        for stage in ((0,) if i == 0 else (1, 0)):
            for key, record in records.items():
                base = second[int(key[0] == 1), key[1]][stage][107 + i]
                check("old_archive", old_record(record["history"][stage][i]), old_record(base),
                      key, 107 + i, "post-C" if stage else "full", "time-matched old material")
    return {"pass": all(bad is None for bad in failures.values()), "failures": failures}


def local_pair(field):
    return field[site(6, 3)][:2]


def s6(field):
    return total(c[0] for c in column(field, 6))


def class_witness(fields, projection, label, t, stage):
    failure = class_failure(fields, projection, label)
    if failure is None:
        return None
    kind, key, other = failure
    return {"relative": t, "stage": stage, "kind": kind,
            "input": key, "other_input": other, "label": label(key), "other_label": label(other),
            "value": value_encoding(projection(fields[key])),
            "other_value": value_encoding(projection(fields[other]))}


def literal_witness(fields, baseline, projection, t, stage):
    for key, field in fields.items():
        a, b = projection(field), projection(baseline[key])
        if a != b:
            return {"relative": t, "stage": stage, "input": key,
                    "value": value_encoding(a), "full110": value_encoding(b)}
    return None


def retention(records, family):
    features = {"local_pair": local_pair, "S6": s6}
    failures = {name: {gate: None for gate in ("literal", "two_donor", "four_joint")}
                for name in features}
    failures["old_literal"] = failures["two_old"] = None
    fresh = (lambda key: key[2]) if family == "crossed" else (lambda key: int(key[1] == 1))
    old = lambda key: int(key[0] == 1)
    joint = lambda key: (old(key), fresh(key))
    baseline = {key: r["history"][0][3] for key, r in records.items()}
    for i in range(4, 36):
        t = 107 + i
        for stage in (1, 0):
            stage_name = "post-C" if stage else "full"
            fields = {key: r["history"][stage][i] for key, r in records.items()}
            if failures["old_literal"] is None:
                failures["old_literal"] = literal_witness(fields, baseline, old_record, t, stage_name)
            if failures["two_old"] is None:
                failures["two_old"] = class_witness(fields, old_record, old, t, stage_name)
            for name, projection in features.items():
                tests = failures[name]
                if tests["literal"] is None:
                    tests["literal"] = literal_witness(fields, baseline, projection, t, stage_name)
                if tests["two_donor"] is None:
                    tests["two_donor"] = class_witness(fields, projection, fresh, t, stage_name)
                if tests["four_joint"] is None:
                    both = lambda field, projection=projection: (old_record(field), projection(field))
                    tests["four_joint"] = class_witness(fields, both, joint, t, stage_name)
    return {"failures": failures,
            "local_pair": failures["two_old"] is None and all(v is None for v in failures["local_pair"].values()),
            "S6": failures["two_old"] is None and all(v is None for v in failures["S6"].values())}


def family_accounts(records):
    grouped = {}
    for key, record in records.items():
        active = accounts(record["history"][0][0])
        grouped.setdefault(active, []).append(key)
    budgets = {record["budget"] for record in records.values()}
    assert len(budgets) == 1
    return {"active": tuple({"account": account_encoding(a), "inputs": keys}
                             for a, keys in grouped.items()),
            "compound": account_encoding(next(iter(budgets)))}


def family_hashes(records):
    histories = tuple(record["history"] for record in records.values())
    initial_fields = tuple(h[0][0] for h in histories)
    final_fields = tuple(h[0][35] for h in histories)
    initial = tuple((key, compound_encoding(r["history"][0][0], 1, r["reserves"]))
                    for key, r in records.items())
    final = tuple((key, compound_encoding(r["history"][0][35], 0, r["reserves"]))
                  for key, r in records.items())
    return {"ordered_fields107": fields_digest(initial_fields),
            "ordered_fields142": fields_digest(final_fields),
            "ordered_compounds107": digest_json(initial), "ordered_compounds142": digest_json(final),
            "distinct_fields107": len(set(initial_fields)), "distinct_fields142": len(set(final_fields)),
            "compound_records": len(records),
            "distinct_compounds107": len({state for _, state in initial}),
            "distinct_compounds142": len({state for _, state in final})}


def event_report(families):
    profiles, first_receiver, aggregate = {}, {}, {}
    for family, records in families.items():
        first_receiver[family] = None
        counts = Counter()
        for key, record in records.items():
            h = record["history"]
            profile = tuple((107 + i, x, y, tag)
                            for i in range(1, 36) for x, y, tag in h[2][i])
            profiles.setdefault(profile, []).append((family, key))
            counts.update(("receiver" if x == 6 else "archive" if x in (5, 7) else "other", tag)
                          for _, x, _, tag in profile)
        aggregate[family] = tuple((region, tag, count) for (region, tag), count in sorted(counts.items()))
        for i in range(4, 36):
            if first_receiver[family] is not None:
                break
            for key, record in records.items():
                events = tuple((x, y, tag) for x, y, tag in record["history"][2][i] if x == 6)
                if events:
                    first_receiver[family] = {"relative": 107 + i, "input": key, "events": events}
                    break
    grouped = []
    for timeline, inputs in profiles.items():
        counts = Counter(("receiver" if x == 6 else "archive" if x in (5, 7) else "other", tag)
                         for _, x, _, tag in timeline)
        grouped.append({"inputs": inputs, "counts": tuple((region, tag, count)
                         for (region, tag), count in sorted(counts.items())), "all_events": timeline})
    return {"first_receiver_after110": first_receiver, "aggregate_all_inputs": aggregate, "profiles": grouped}


def receiver(second, source_reserves):
    labels = tuple(("SEALED", m, k) for m in range(1, 9) for k in range(5)) + tuple(
        ("DRAIN", m, k) for m in (1, 3, 5, 7) for k in range(5))
    assert len(labels) == 60
    selected = {gate: None for gate in ("three_contact", "local_pair", "S6")}
    passing = {gate: [] for gate in selected}
    for label in labels:
        material, radiation, parameters = module(*label)
        families, pool = assemble_families(second, source_reserves, material, radiation)
        results = {}
        for family, records in families.items():
            results[family] = {"contacts": contacts(records, family, second, parameters),
                               "retention": retention(records, family),
                               "accounts": family_accounts(records), "hashes": family_hashes(records)}
        complete = all(result["contacts"]["pass"] for result in results.values())
        gates = {"three_contact": complete,
                 "local_pair": complete and all(r["retention"]["local_pair"] for r in results.values()),
                 "S6": complete and all(r["retention"]["S6"] for r in results.values())}
        for gate, passed in gates.items():
            if passed:
                passing[gate].append(label)
                if selected[gate] is None:
                    selected[gate] = label
        emit("BREAK B", {"label": label, "gates": gates, "stock_slots": {"M": 12, "R": 96},
                         "stock_accounts": account_encoding(stock_account(material, radiation)),
                         "parameters": {key: short(value) for key, value in parameters.items()},
                         "families": results, "events": event_report(families),
                         "shared_evolving_fields": len(pool), "audit": dict(AUDIT)})
        clear_caches()
    emit("BREAK B SELECT", {"selected": selected, "passing": passing})


def main():
    base = Path(__file__).resolve().parent
    expected = {
        "PREREG-A.md": "31baa223b9bc63c97a72d229f0f40f08b474565a89d4d38746de7847785f8370",
        "PREREG-B.md": "0ab51a8c11973ce46c8c8e0e50b913e39f45797d8e6d272a4a2ae69884f7b2c2",
        "CLARIFICATION-A.md": "4f37002bc0285a4e50123645f0597003e9b0ec121844c021eb55f9e09f4a69f5",
        "CLARIFICATION-B.md": "0ed1ef637ece3c327932aa3cd45039ced21ddec3389b5f9ebfadf0d4789ad4c3",
    }
    for name, digest in expected.items():
        assert hashlib.sha256((base / name).read_bytes()).hexdigest() == digest, name
    emit("BREAK CUSTODY", {"documents": expected, "source": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                           "status": "NON-CANONICAL candidate-C, NO AUTHORITY",
                           "scope": "separately written same-session audit; initial joint-freeze order not met"})
    first, second, source_reserves = prepare()
    delivery(first, second, source_reserves)
    receiver(second, source_reserves)
    emit("BREAK AUDIT", dict(AUDIT))
    print("BREAK PASS: frozen finite census completed; scientific gates are recorded separately", flush=True)


if __name__ == "__main__":
    main()
