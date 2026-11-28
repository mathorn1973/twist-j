#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""C-H3-MATERIAL-READ-CONTROL-N: blind same-session checker.

NON-CANONICAL / NO AUTHORITY. Own cyclic-five arithmetic and native update.
No primary model.py, continuation.py, reader.py or outputs were read before
this source freeze. Old self-authored engine portions are retained literally
where useful; this file is standalone and imports no scientific source.
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


def prepare_actual():
    first = [history(initial(p), 114) for p in range(5)]
    ac = (ring((-12, 24, 42, 18)), ring((762, 588, 792, 429)), ring((54044, 0, 17904, 17904)), 90184)
    assert all(accounts(initial(p)) == ac for p in range(5))
    fields, reserves = {}, {}
    for p, q0 in ACTUAL:
        assert all(x != 4 for ev in first[p][2][1:] for x, y, tag in ev)
        fields[p, q0], reserves[p, q0] = source_swap(first[p][0][114], p, q0)
    assert len(set(fields.values())) == 10
    assert len({(field, 0, reserves[key]) for key, field in fields.items()}) == 25
    for p, q0 in ACTUAL:
        assert fields[p, q0] == fields[int(p == 1), q0]
    # The immutable reserve is never an argument to the native field update.
    # Equal fields with the same bit therefore share a computed trajectory,
    # while all 25 distinct ordered reserve states remain separately retained.
    histories = {key: history(fields[key], 121) for key in KEYS}
    endpoint = fields_digest(histories[key][0][121] for key in KEYS)
    assert endpoint == "fde15d156a9879098a6a93b3a3fe75b25b11f6c13f637eeb1f568e918a602060", "predecessor endpoint STOP"
    for t in range(1, 90):
        for key, hist in histories.items():
            expected = ((4, 0, 1),) if key[1] == 1 and t == 89 else ()
            assert tuple(e for e in hist[2][t] if e[0] == 4) == expected
    for t in range(90, 122):
        for stage in (1, 0):
            ff = actual_fields(histories, stage, t)
            assert class_failure(ff, s0, lambda k: k[1] == 1) is None
            assert class_failure(ff, old_record, lambda k: k[0] == 1) is None
            for key, field in ff.items():
                target = plus(times(-6, O), times(2, DELTA)) if key[1] == 1 else times(-6, O)
                assert s0(field) == target
            assert all(x not in (4, 5, 7) for h in histories.values() for x, y, tag in h[2][t])
    emit("BREAK PREMISE", {"endpoint": endpoint, "fields": 10, "compound": 25,
                            "Q_field": 90184, "Q_source_reserve": 30})
    # Establish the immutable predecessor endpoint before entering the new
    # continuation. Preserve the matching bit at the full121 boundary.
    for key, prefix in tuple(histories.items()):
        tail = history(prefix[0][-1], 903, bit=1)
        histories[key] = tuple(prefix[i] + tail[i][1:] for i in range(3))
    return histories, reserves


def continuation(histories):
    reference = actual_fields(histories, 0, 121)
    loss = {name: None for name in ("literal_S0", "classes_S0", "literal_old", "classes_old")}
    first_bank, bank_counts = {}, {}
    for key, hist in histories.items():
        hits = [(t, y, tag) for t in range(122, 1025) for x, y, tag in hist[2][t] if x == 4]
        first_bank[str(key)] = hits[0] if hits else None
        bank_counts[str(key)] = len(hits)
    natural = None
    for t in range(122, 1025):
        for stage, name in ((1, "post-C"), (0, "full")):
            ff = actual_fields(histories, stage, t)
            for label, read in (("literal_S0", s0), ("literal_old", old_record)):
                bad = next((k for k, f in ff.items() if read(f) != read(reference[k])), None)
                if bad is not None and loss[label] is None:
                    loss[label] = (t, name, bad)
            for label, read, bit in (("classes_S0", s0, lambda k: k[1] == 1),
                                     ("classes_old", old_record, lambda k: k[0] == 1)):
                bad = class_failure(ff, read, bit)
                if bad is not None and loss[label] is None:
                    loss[label] = (t, name, bad)
        if natural is None:
            full = actual_fields(histories, 0, t)
            if all(old_record(f) == old_record(reference[k]) for k, f in full.items()):
                for y in range(NY):
                    incoming = {histories[key][1][t][site(4, y)][2:] for key in KEYS}
                    wanted = {tags(histories[b, 1], t)[y] for b in range(2)}
                    absent = {tags(histories[b, q0], t)[y] for b in range(2) for q0 in (0, 2, 3, 4)}
                    if len(incoming) == 1 and len(wanted) == 1 and next(iter(wanted)) != 0 and absent == {0}:
                        if class_failure(full, lambda f: f[site(4, y)][2:], lambda k: k[1] == 1) is None:
                            natural = (t, y, next(iter(wanted)))
                            break
    emit("BREAK A1", {"loss": loss, "first_bank": first_bank, "bank_counts": bank_counts,
                      "bank_B_weighted": sum((4 if k[0] == 0 else 1) * bank_counts[str(k)] for k in KEYS),
                      "strict_natural": natural,
                      "final_digest": fields_digest(histories[k][0][1024] for k in KEYS),
                      "final_by_field": {str(k): field_digest(histories[k][0][1024]) for k in KEYS},
                      "audit": dict(AUDIT)})


def control_continuation(histories, source_reserves):
    reference = actual_fields(histories, 0, 121)
    donors = (bank(histories[0, 0][0][121]), bank(histories[0, 1][0][121]))
    assert donors[0] != donors[1]
    for key, field in reference.items():
        assert bank(field) == donors[int(key[1] == 1)]
    control_hist, field_hist, inert, compound_initial = {}, {}, {}, []
    common = None
    for p, q0 in ACTUAL:
        for a in range(2):
            field, displaced = bank_swap(reference[p, q0], donors[a])
            kept = tuple(displaced if i == a else donors[i] for i in range(2))
            reserve = (source_reserves[p, q0], *kept)
            before = sum_accounts(accounts(reference[p, q0]), stock_account(material=source_reserves[p, q0] + donors[0] + donors[1]))
            after = sum_accounts(accounts(field), stock_account(material=reserve[0] + reserve[1] + reserve[2]))
            assert before == after
            if common is None:
                common = before
            assert before == common
            if field not in field_hist:
                field_hist[field] = history(field, 903, bit=1)
            control_hist[p, q0, a] = field_hist[field]
            inert[p, q0, a] = reserve
            compound_initial.append((field, 1, reserve))
    first_differences = {}
    for p, q0 in ACTUAL:
        h0, h1 = control_hist[p, q0, 0], control_hist[p, q0, 1]
        certificate = None
        assert outside_equal(h0[0][0], h1[0][0])
        for dt in range(1, 904):
            common_pre = outside_equal(h0[1][dt], h1[1][dt])
            if certificate is None:
                assert common_pre
            tg0, tg1 = tags(h0, dt), tags(h1, dt)
            if tg0 != tg1 and certificate is None:
                rows = []
                for y in range(NY):
                    if tg0[y] != tg1[y]:
                        c0, c1 = h0[1][dt][site(4, y)], h1[1][dt][site(4, y)]
                        z0, z1 = h0[0][dt][site(4, y)], h1[0][dt][site(4, y)]
                        assert c0[2:] == c1[2:]
                        rows.append({"row": y, "incoming": tuple(short(z) for z in c0[2:]),
                                     "tags": (tg0[y], tg1[y]),
                                     "output0": tuple(short(z) for z in z0),
                                     "output1": tuple(short(z) for z in z1),
                                     "radiation_differs": z0[2:] != z1[2:]})
                certificate = {"time": 121 + dt, "rows": rows}
            if certificate is None:
                assert outside_equal(h0[0][dt], h1[0][dt])
        first_differences[str((p, q0))] = certificate
    strict = None
    old_preserved_through = True
    for dt in range(1, 904):
        for stage in (1, 0):
            old_preserved_through = old_preserved_through and all(
                old_record(h[stage][dt]) == old_record(reference[p, q0])
                for (p, q0, a), h in control_hist.items())
        if strict is None and old_preserved_through:
            for y in range(NY):
                incoming = {h[1][dt][site(4, y)][2:] for h in control_hist.values()}
                yes = {tags(h, dt)[y] for (p, q0, a), h in control_hist.items() if a == 1}
                no = {tags(h, dt)[y] for (p, q0, a), h in control_hist.items() if a == 0}
                ff = {k: h[0][dt] for k, h in control_hist.items()}
                if len(incoming) == 1 and len(yes) == 1 and next(iter(yes)) != 0 and no == {0}:
                    if class_failure(ff, lambda f: f[site(4, y)][2:], lambda k: k[2]) is None:
                        strict = (121 + dt, y, next(iter(yes)))
                        break
    finals = tuple(dict.fromkeys(h[0][903] for h in control_hist.values()))
    compound_final = {(h[0][903], 0, inert[key]) for key, h in control_hist.items()}
    assert len(compound_final) == len(set(compound_initial))
    emit("BREAK A2", {"cases": 50, "unique_fields": len(field_hist),
                      "compound_states": len(set(compound_initial)),
                      "common_accounts": tuple(short(z) for z in common[:3]) + (common[3],),
                      "first_differences": first_differences, "strict_control": strict,
                      "final_fields": len(finals), "final_digest": fields_digest(finals),
                      "audit": dict(AUDIT)})


def reader_census(histories):
    selected, labels = None, []
    totals = Counter()
    for s in range(119, 88, -2):
        tau = s + 1
        for y in range(NY):
            positive = histories[0, 1][1][tau][site(4, y)][:2]
            diff = minus(*positive)
            for intended in (2, 1):
                label = (s, y, intended)
                if diff == Z or not is_even(diff):
                    reason = "zero_positive_difference" if diff == Z else "odd_positive_difference"
                    labels.append((label, False, reason, tuple(short(z) for z in positive)))
                    totals[reason] += 1
                    continue
                d = half(diff)
                f = multiply(JI if intended == 2 else J, d)
                failure = None
                for p, q0 in ACTUAL:
                    material = histories[int(p == 1), q0][1][tau][site(4, y)][:2]
                    _, got = bp((*material, f, times(-1, f)))
                    expected = intended if q0 == 1 else 0
                    if got != expected:
                        failure = ((p, q0), got, expected)
                        break
                if failure is not None:
                    labels.append((label, False, "guard", failure))
                    totals["guard"] += 1
                    continue
                labels.append((label, True, short(f)))
                totals["pass"] += 1
                if selected is None:
                    selected = (s, y, intended, f)
    assert len(labels) == 192
    emit("BREAK B1", {"labels": labels, "totals": dict(totals),
                      "selected": (*selected[:3], short(selected[3])) if selected else None})
    return selected


def make_cohort(histories, source_reserves, selected, controlled):
    s, y, tag, f = selected
    references = actual_fields(histories, 0, s)
    donors = (bank(histories[0, 0][0][s]), bank(histories[0, 1][0][s]))
    for key, field in references.items():
        assert bank(field) == donors[int(key[1] == 1)]
    assert donors[0] != donors[1]
    probe = (f, f, times(-1, f), times(-1, f))
    cases, kept, budgets, histories_by_field = {}, {}, {}, {}
    common = None
    for p, q0 in ACTUAL:
        for arm in ((0, 1) if controlled else (None,)):
            field = references[p, q0]
            mat_reserve = source_reserves[p, q0]
            material_components = (mat_reserve,)
            if controlled:
                before_material = mat_reserve + donors[0] + donors[1]
                field, displaced = bank_swap(field, donors[arm])
                replaced_donors = tuple(displaced if i == arm else donors[i] for i in range(2))
                material_components = (mat_reserve, *replaced_donors)
                mat_reserve = mat_reserve + replaced_donors[0] + replaced_donors[1]
            else:
                before_material = mat_reserve
            before = sum_accounts(accounts(references[p, q0]), stock_account(material=before_material, radiation=probe))
            loaded, old_radiation = probe_swap(field, y, f)
            after = sum_accounts(accounts(loaded), stock_account(material=mat_reserve, radiation=old_radiation))
            assert after == before
            if common is None:
                common = before
            assert before == common
            key = (p, q0, arm) if controlled else (p, q0)
            if loaded not in histories_by_field:
                histories_by_field[loaded] = history(loaded, 33, bit=1)
            cases[key] = histories_by_field[loaded]
            kept[key] = (*material_components, old_radiation)
            budgets[key] = stock_account(material=mat_reserve, radiation=old_radiation)
            assert sum_accounts(accounts(cases[key][0][33]), budgets[key]) == common
    return cases, kept, budgets, common, len(histories_by_field)


def check_reader_cohort(histories, selected, cases, kept, budgets, common, unique_fields, controlled):
    s, y, tag, f = selected
    tau = s + 1
    label_new = (lambda k: k[2]) if controlled else (lambda k: int(k[1] == 1))
    label_old = lambda k: int(k[0] == 1)
    label_pair = lambda k: (int(k[0] == 1), label_new(k))
    read_rad = lambda field: field[site(4, y)][2:]
    read_both = lambda field: (old_record(field), read_rad(field))
    expected_yes_f = multiply(J if tag == 2 else JI, f)
    expected_no = (f, times(-1, f))
    expected_yes = (expected_yes_f, times(-1, expected_yes_f))
    reference = {key: hist[0][1] for key, hist in cases.items()}
    other_events = {}
    for key, hist in cases.items():
        p, q0 = key[:2]
        donor = label_new(key)
        material_input = histories[0, donor][1][tau][site(4, y)][:2] if controlled else histories[int(p == 1), q0][1][tau][site(4, y)][:2]
        assert hist[1][1][site(4, y)][:2] == material_input
        assert hist[1][1][site(4, y)][2:] == expected_no
        assert tags(hist, 1)[y] == (tag if donor else 0)
        assert read_rad(hist[0][1]) == (expected_yes if donor else expected_no)
        assert old_record(hist[0][1]) == old_record(histories[int(p == 1), q0][0][tau])
        other_events[str(key)] = tuple(e for e in hist[2][1] if e[:2] != (4, y))
        # Ordered typed reserves are fixed through every replay. Recheck the
        # complete account, including that exact fixed stock, at both cuts.
        for dt in range(1, 34):
            for stage in (1, 0):
                assert sum_accounts(accounts(hist[stage][dt]), budgets[key]) == common
                AUDIT["compound_account_cuts"] += 1
    assert class_failure(reference, read_rad, label_new) is None
    assert class_failure(reference, old_record, label_old) is None
    assert class_failure(reference, read_both, label_pair) is None
    losses = {name: None for name in ("literal_radiation", "classes_radiation", "literal_old", "classes_old")}
    first_bank, first_archive = None, None
    for dt in range(2, 34):
        t = s + dt
        for stage, stage_name in ((1, "post-C"), (0, "full")):
            fields = {key: hist[stage][dt] for key, hist in cases.items()}
            for name, projection in (("literal_radiation", read_rad), ("literal_old", old_record)):
                bad = next((key for key, field in fields.items() if projection(field) != projection(reference[key])), None)
                if bad is not None and losses[name] is None:
                    losses[name] = (t, stage_name, bad)
            for name, projection, label in (("classes_radiation", read_rad, label_new),
                                           ("classes_old", old_record, label_old)):
                bad = class_failure(fields, projection, label)
                if bad is not None and losses[name] is None:
                    losses[name] = (t, stage_name, bad)
        for key, hist in cases.items():
            for event in hist[2][dt]:
                if event[0] == 4 and first_bank is None:
                    first_bank = (t, key, event)
                if event[0] in (5, 7) and first_archive is None:
                    first_archive = (t, key, event)
    final_fields = tuple(dict.fromkeys(hist[0][33] for hist in cases.values()))
    initial_compound = {(hist[0][0], 1, kept[key]) for key, hist in cases.items()}
    final_compound = {(hist[0][33], 0, kept[key]) for key, hist in cases.items()}
    assert len(initial_compound) == len(final_compound)
    emit("BREAK B CONTROL" if controlled else "BREAK B ACTUAL", {
        "candidate": (s, y, tag), "tau": tau, "f": short(f),
        "cases": len(cases), "loaded_fields": unique_fields,
        "compound_states": len(initial_compound),
        "common_accounts": tuple(short(z) for z in common[:3]) + (common[3],),
        "probe_Q": 4 * q(f),
        "negative_radiation": tuple(short(z) for z in expected_no),
        "positive_radiation": tuple(short(z) for z in expected_yes),
        "side_contacts": other_events, "losses": losses,
        "first_bank": first_bank, "first_archive": first_archive,
        "final_fields": len(final_fields), "final_digest": fields_digest(final_fields),
        "final_by_unique_field": tuple(field_digest(z) for z in final_fields),
        "audit": dict(AUDIT)})


def reader(histories, source_reserves):
    selected = reader_census(histories)
    if selected is None:
        return
    for controlled in (False, True):
        cohort = make_cohort(histories, source_reserves, selected, controlled)
        check_reader_cohort(histories, selected, *cohort, controlled)


def main():
    path = Path(__file__).resolve().parent
    assert hashlib.sha256((path / "PREREG.md").read_bytes()).hexdigest() == "dafa06568fe1a38f21c806ebeea694e5e635b151667045c5e6761498c7879981"
    assert hashlib.sha256((path / "CLARIFICATION.md").read_bytes()).hexdigest() == "6193dfed88dc00ebb381c981228ffa5c541cf3c1bd62946405d53619f44a2064"
    assert hashlib.sha256((path / "CLARIFICATION-2.md").read_bytes()).hexdigest() == "b04236f7070d0cb6df6566b9e2f45dc4b825542e757a4155305c7394e3a872f9"
    assert multiply(J, JI) == O
    histories, reserves = prepare_actual()
    continuation(histories)
    control_continuation(histories, reserves)
    reader(histories, reserves)
    emit("BREAK PASS", {"audit": dict(AUDIT)})


if __name__ == "__main__":
    main()

