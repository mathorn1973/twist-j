#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Blind same-session audit of frozen C-H3-CLOCK-CONTACT-N B/C.

NON-CANONICAL / NO AUTHORITY. Uses its own cyclic-five quotient arithmetic,
complete native update, and literal first-apparatus stock. No primary import.
Preregistration: 53bc0c11b51d671f85977117a2b8df74f2b0698c.
Old apparatus: f96db81df668f138d7242ddfa2c7d946ea892833, selected stock B.
The author read that old specification, but not this candidate's primary code.
"""

from collections import Counter
from functools import cache
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


@cache
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


@cache
def cp(a, b, inverse=False):
    delta = minus(a, b)
    if not is_even(delta):
        return a, b
    d = half(delta)
    center = plus(b, d)
    moved = rotate(d, 3 if inverse else 2)
    return plus(center, moved), minus(center, moved)


@cache
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


@cache
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


def initial(p):
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


def baseline():
    first = [history(initial(p), 114) for p in range(5)]
    assert len({accounts(initial(p)) for p in range(5)}) == 1
    assert accounts(initial(0))[3] == 80316
    for p, hist in enumerate(first):
        end = hist[0][114]
        assert column(end, 0) == column(initial(p), 0)
        assert column(end, 6) == column(initial(p), 6)
        assert tuple(c[3] for c in end) == tuple(c[3] for c in initial(p))
        assert all(e[0] != 4 for ev in hist[2][1:] for e in ev)
    loaded = {(p, q0): exchange(first[p][0][114], p, q0) for p, q0 in product(range(5), repeat=2)}
    assert len(set(loaded.values())) == 10
    for (p, q0), field in loaded.items():
        assert field == loaded[int(p == 1), q0]
    second = {}
    reuse = {}
    for key, field in loaded.items():
        if field not in reuse:
            reuse[field] = history(field, 122)
        second[key] = reuse[field]
    assert all(e[0] != 4 for h in second.values() for ev in h[2][1:] for e in ev)
    return first, second


def wheel(start, horizon):
    states = [tuple(map(ring, start))]
    kinds = [None]
    for t in range(horizon):
        z = list(states[-1])
        kk = [None] * NY
        for y in range(t % 2, NY, 2):
            k = (y + 1) % NY
            a, b = states[-1][y], states[-1][k]
            pair = cp(a, b)
            z[y], z[k] = pair
            typ = "R" if not is_even(minus(a, b)) else "C" if pair != (a, b) else "E"
            kk[y] = kk[k] = typ
            assert cp(*pair, True) == (a, b)
        states.append(tuple(z))
        kinds.append(tuple(kk))
    return states, kinds


def raw_at(w, phase, absolute, row):
    return w[0][phase + absolute][row]


def log_event(first, second, target, row):
    """Deduplicate only equal time,row,CORR, preserving literal multiplicity."""
    records = {}
    for p in range(5):
        for t in range(1, 115):
            for yy in range(NY):
                r = first[p][1][t][site(4, yy)][3]
                key = (t, yy, r, False)
                if key not in records:
                    records[key] = [0, ("first", p, t, yy)]
                records[key][0] += 1
    for p, q0 in product(range(5), repeat=2):
        for t in range(1, target + 1):
            for yy in range(NY):
                wanted = q0 == 1 and t == target and yy == row
                r = second[p, q0][1][t][site(4, yy)][3]
                key = (114 + t, yy, r, wanted)
                if key not in records:
                    records[key] = [0, ("second", p, q0, t, yy)]
                records[key][0] += 1
    return tuple((key, *value) for key, value in records.items())


def short(a):
    return tuple(a[:4])


def alias_and_polynomials(wu, wv, su, sv, target, row, tag, rstar, records):
    absolute = 114 + target
    ut, vt = raw_at(wu, su, absolute, row), raw_at(wv, sv, absolute, row)
    if tag == 1:
        ds = multiply(RI, DELTA)
        fs = multiply(J, ds)
    else:
        fs = times(-1, multiply(RI, DELTA))
        ds = multiply(J, fs)
    g = plus(rstar, times(2, fs))
    doubled = times(2, ds)
    constraints = {}
    counts = Counter()
    first_parity = None
    first_alias = None
    for (time, yy, r, wanted), weight, witness in records:
        if wanted:
            counts["wanted"] += weight
            continue
        du = minus(raw_at(wu, su, time, yy), ut)
        dv = minus(raw_at(wv, sv, time, yy), vt)
        fd = minus(g, r)
        md = plus(doubled, minus(du, dv))
        if not is_even(fd) or not is_even(md):
            counts["parity_refused"] += weight
            if first_parity is None:
                first_parity = (witness, short(md), short(fd))
            continue
        counts["parity_admitted"] += weight
        if du == dv == Z:
            # Center can be zero; the guard depends only on the differences.
            _, hit = bp((ds, times(-1, ds), g, r))
            counts["joint_alias"] += weight
            if hit and first_alias is None:
                first_alias = (witness, hit, short(r), short(ds), short(g))
            continue
        qa, qb = q(multiply(JI, fd)), q(multiply(J, fd))
        key = (du, dv, qa, qb)
        if key not in constraints:
            constraints[key] = [0, witness]
        constraints[key][0] += weight
    if first_alias is not None:
        return None, {"kind": "alias", "witness": first_alias, "counts": dict(counts)}
    constraints = tuple(constraints)
    kcount = len(constraints)
    a_constraints = []
    for du, dv, qa, qb in constraints:
        if dv == Z:
            assert du != Z
            c2 = q(du)
            c1 = q(plus(doubled, du)) - q(doubled) - c2
            assert c2 > 0
            a_constraints.append((c2, c1, q(doubled), qa, qb))
    aa = None
    for a in range(1, 2 * (4 * kcount + 1), 2):
        if all(c2 * a * a + c1 * a + c0 not in (qa, qb)
               for c2, c1, c0, qa, qb in a_constraints):
            aa = a
            break
    assert aa is not None, "proved first-scale bound"
    b_constraints = []
    for du, dv, qa, qb in constraints:
        if dv != Z:
            s = plus(doubled, times(aa, du))
            c2 = q(dv)
            c1 = q(minus(s, dv)) - q(s) - c2
            assert c2 > 0
            b_constraints.append((c2, c1, q(s), qa, qb))
    bb = None
    for b in range(1, 2 * (4 * kcount + 1), 2):
        if all(c2 * b * b + c1 * b + c0 not in (qa, qb)
               for c2, c1, c0, qa, qb in b_constraints):
            bb = b
            break
    assert bb is not None, "proved second-scale bound"
    translation = minus(minus(times(aa, ut), times(bb, vt)), doubled)
    qualified = []
    for w, phase in ((wu, su), (wv, sv)):
        seen = {w[1][phase + t][row] for t in range(1, absolute)}
        qualified.append("R" in seen and "C" in seen)
    info = {"a": aa, "b": bb, "g": g, "translation": translation, "ds": ds,
            "ut": ut, "vt": vt, "refusal": all(qualified), "constraints": kcount,
            "a_constraints": len(a_constraints), "b_constraints": len(b_constraints),
            "counts": dict(counts), "first_parity": first_parity}
    return info, None


def install(field, wu, wv, su, sv, info):
    out = list(field)
    for y in range(NY):
        i = site(4, y)
        assert out[i][:3] == (Z, Z, Z)
        out[i] = (times(info["a"], raw_at(wu, su, 0, y)),
                  plus(times(info["b"], raw_at(wv, sv, 0, y)), info["translation"]),
                  info["g"], out[i][3])
    return tuple(out)


def material_record(field):
    return tuple(z for x in (5, 7) for c in column(field, x) for z in c[:2])


def partition_ok(fields, project, label):
    groups = {}
    for key, field in fields.items():
        groups.setdefault(label(key), set()).add(project(field))
    return all(len(s) == 1 for s in groups.values()) and len(set.union(*groups.values())) == len(groups)


def replay(first, second, wu, wv, su, sv, target, row, tag, info):
    horizon = max(114, target + 32)
    starts = [install(initial(p), wu, wv, su, sv, info) for p in range(5)]
    assert len({accounts(z) for z in starts}) == 1
    first_new = [history(z, 114) for z in starts]
    def outside_equal(actual, reference):
        return all(actual[n] == reference[n] for n in range(NX * NY) if n // NY != 4)
    for p in range(5):
        for t in range(1, 115):
            assert first_new[p][2][t] == first[p][2][t]
            for stage in (0, 1):
                assert outside_equal(first_new[p][stage][t], first[p][stage][t])
                assert all(c[3] == d[3] for c, d in zip(first_new[p][stage][t], first[p][stage][t]))
    loaded = {(p, q0): exchange(first_new[p][0][114], p, q0) for p, q0 in product(range(5), repeat=2)}
    assert len(set(loaded.values())) == 10
    second_new, reuse = {}, {}
    for key, z in loaded.items():
        if z not in reuse:
            reuse[z] = history(z, horizon)
        second_new[key] = reuse[z]
    for key, h in second_new.items():
        for t in range(1, target + 1):
            wanted = ((4, row, tag),) if key[1] == 1 and t == target else ()
            assert tuple(e for e in h[2][t] if e[0] == 4) == wanted
            assert tuple(e for e in h[2][t] if e[0] != 4) == second[key][2][t]
            for stage in (0, 1):
                assert outside_equal(h[stage][t], second[key][stage][t])
                if t < target or stage == 1:
                    assert all(c[3] == d[3] for c, d in zip(h[stage][t], second[key][stage][t]))
        if key[1] == 1:
            pre = h[1][target][site(4, row)]
            post = h[0][target][site(4, row)]
            assert minus(post[3], pre[3]) == DELTA
            assert minus(post[2], pre[2]) == times(-1, DELTA)
            assert half(minus(pre[0], pre[1])) == info["ds"]
    newpart = lambda z: z[site(4, row)][:2]
    oldpart = material_record
    combined = lambda z: (oldpart(z), newpart(z))
    labnew = lambda k: k[1] == 1
    labold = lambda k: k[0] == 1
    labboth = lambda k: (k[0] == 1, k[1] == 1)
    target_fields = {k: h[0][target] for k, h in second_new.items()}
    assert partition_ok(target_fields, newpart, labnew)
    assert partition_ok(target_fields, oldpart, labold)
    assert partition_ok(target_fields, combined, labboth)
    failures = {name: None for name in ("new_pair", "old_material", "four_material", "literal_pair")}
    later_bank, later_archive = None, None
    for t in range(target + 1, horizon + 1):
        for stage, stage_name in ((1, "post-C"), (0, "full")):
            fields = {k: h[stage][t] for k, h in second_new.items()}
            tests = (("new_pair", partition_ok(fields, newpart, labnew)),
                     ("old_material", partition_ok(fields, oldpart, labold)),
                     ("four_material", partition_ok(fields, combined, labboth)),
                     ("literal_pair", all(newpart(fields[k]) == newpart(target_fields[k]) for k in fields)))
            for name, passed in tests:
                if not passed and failures[name] is None:
                    failures[name] = (t, stage_name)
        for key, h in second_new.items():
            for event in h[2][t]:
                if event[0] == 4 and later_bank is None:
                    later_bank = (t, key, event)
                if event[0] in (5, 7) and later_archive is None:
                    later_archive = (t, key, event)
    restore = {}
    for x, label in ((0, "source"), (6, "worker")):
        restore[label] = sum(column(h[0][114], x) == column(initial(k[1]), x)
                             for k, h in second_new.items())
    restore["both"] = sum(all(column(h[0][114], x) == column(initial(k[1]), x) for x in (0, 6))
                          for k, h in second_new.items())
    newbudget = accounts(starts[0])
    oldbudget = accounts(initial(0))
    summary = {"target": target, "row": row, "tag": tag,
               "scales": (info["a"], info["b"]), "translation": short(info["translation"]),
               "clock": short(info["g"]), "constraints": info["constraints"],
               "constraints_a": info["a_constraints"], "constraints_b": info["b_constraints"],
               "counts": info["counts"], "first_parity": info["first_parity"],
               "q": newbudget[3], "q_increment": newbudget[3] - oldbudget[3],
               "accounts": tuple(short(z) for z in newbudget[:3]),
               "account_increment": tuple(short(minus(a, b)) for a, b in zip(newbudget[:3], oldbudget[:3])),
               "pre_positive": tuple(short(z) for z in second_new[0, 1][1][target][site(4, row)]),
               "post_positive": tuple(short(z) for z in second_new[0, 1][0][target][site(4, row)]),
               "post_negative": tuple(short(z) for z in second_new[0, 0][0][target][site(4, row)]),
               "class_losses": failures, "later_bank": later_bank, "later_archive": later_archive,
               "restore114": restore, "horizon": horizon,
               "all25": len(second_new), "distinct_second": len(reuse)}
    # An exact digest of the chosen literal whole initial field is an extra
    # representation-neutral comparison surface, using canonical 4-tuples.
    canonical = repr(tuple(tuple(short(z) for z in c) for c in starts[0])) + "\n"
    summary["initial_p0_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    return summary


def seek(first, second, wheels, target):
    rejected = Counter()
    examples = {}
    event_cache = {row: log_event(first, second, target, row) for row in (0, 2, 4)}
    visits = 0
    for assignment, su, sv, row, tag in product(range(2), range(0, 33, 2), range(0, 33, 2), (0, 2, 4), (1, 2)):
        visits += 1
        wu, wv = wheels if assignment == 0 else wheels[::-1]
        positives = {second[p, 1][1][target][site(4, row)][3] for p in range(5)}
        negatives = {second[p, q0][1][target][site(4, row)][3]
                     for p in range(5) for q0 in (0, 2, 3, 4)}
        candidate = (assignment, su, sv, row, tag)
        if len(positives) != 1 or len(negatives) != 1 or positives == negatives:
            rejected["incoming"] += 1
            examples.setdefault("incoming", (candidate, tuple(sorted(positives)), tuple(sorted(negatives))))
            continue
        info, failure = alias_and_polynomials(wu, wv, su, sv, target, row, tag,
                                              next(iter(positives)), event_cache[row])
        if failure is not None:
            rejected[failure["kind"]] += 1
            examples.setdefault(failure["kind"], (candidate, failure))
            continue
        observed = replay(first, second, wu, wv, su, sv, target, row, tag, info)
        if not info["refusal"]:
            rejected["no_refusal"] += 1
            examples.setdefault("no_refusal", (candidate, observed))
            continue
        return {"candidate": candidate, "visited": visits, "rejections": dict(rejected),
                "examples": examples, "result": observed}
    return {"candidate": None, "visited": visits, "rejections": dict(rejected), "examples": examples}


def main():
    prereg = Path(__file__).with_name("PREREG.md").read_bytes()
    assert hashlib.sha256(prereg).hexdigest() == "e6b3225db9ff47f9ba8159675430de04f29dd6bfdfd0ddd736b0ae168e4cbdac"
    assert multiply(J, JI) == O
    assert rotate(O, 5) == O
    assert q(J) == 3 and q(multiply(J, J)) == 7
    first, second = baseline()
    print("BREAK BASELINE", json.dumps({"first": 5, "second": 25, "distinct_second": 10,
                                       "q": accounts(initial(0))[3]}, sort_keys=True), flush=True)
    wheels = (wheel((1, -1, -3, 0, -3, 0), 236), wheel((1, -1, 3, 0, -3, 0), 236))
    for target in (89, 90):
        answer = seek(first, second, wheels, target)
        print("BREAK TARGET", target, json.dumps(answer, sort_keys=True), flush=True)
    print("BREAK PASS", flush=True)


if __name__ == "__main__":
    main()
