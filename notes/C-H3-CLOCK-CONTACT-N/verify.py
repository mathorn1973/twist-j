#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""NON-CANONICAL #2137 B/C. Exact preinstalled clock/contact synthesis."""
from collections import Counter
from functools import cache
from itertools import product, combinations
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'reproduce/h3-referenced-record/verify.py'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == (
    '4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd')
spec = importlib.util.spec_from_file_location('contact_native', SOURCE)
H = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = H
spec.loader.exec_module(H)
H.mul = cache(H.mul)
H.transport_pair = cache(H.transport_pair)
H.collision = cache(H.collision)
Z, O, R, RI, J, JI, P = H.ZERO, H.ONE, H.RHO, H.RHO_INV, H.J, H.J_INV, H.J_POWERS
add, sub, mul, sc = H.add, H.sub, H.mul, H.scale
neg = lambda a: sc(-1, a)
ETA = sub(O, R)
DELTA = mul(ETA, R)
NY = 6
KEYS = tuple(product(range(2), range(5)))
ARCH = (5, 7)
ix = lambda x, y, r: H.index(NY, x, y, r)


@cache
def q(z):
    n = 5 * sum(a * a for a in z) - sum(z) ** 2
    assert n % 2 == 0
    return n // 2


def account(f):
    hh = H.ring_sum(H.h(z) for z in f)
    result = (H.ring_sum(z for i, z in enumerate(f) if i % 4 < 2),
              H.ring_sum(z for i, z in enumerate(f) if i % 4 >= 2),
              hh, sum(q(z) for z in f))
    assert result[3] == H.scalar_account(hh)
    return result


def col(f, x):
    return f[4 * NY * x:4 * NY * (x + 1)]


def material(f, xs):
    return tuple(f[ix(x, y, r)] for x, y, r in product(xs, range(NY), (0, 1)))


def pair(f, y):
    return f[ix(4, y, 0)], f[ix(4, y, 1)]


def outside(f):
    return tuple(z for i, z in enumerate(f)
                 if not (i // (4 * NY) == 4 and i % 4 < 3))


def digest(fields):
    data = json.dumps(fields, separators=(',', ':'), ensure_ascii=True)
    return hashlib.sha256(data.encode('ascii')).hexdigest()


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


# Literal selected initial vectors from the immutable predecessor EXPECTED.txt,
# SELECT B, ids (6,1,1,8,5,0) and (6,1,1,7,3). Every first write is replayed.
D5 = ((33, 15, 24, 33), (-27, -12, -9, -21), (-18, -15, -12, -15),
      (-30, 9, -24, -9), (-21, 6, -27, -3), (9, 15, -6, 21))
G5 = ((-21, -8, 5, -36), (3, 28, -19, 30)) * 3
D7 = ((4, 12, 9, 0), (18, 13, 14, 10), (12, -5, 14, 4),
      (10, 8, 15, 2), (6, 4, 9, -4), (12, 8, 9, 6))
G7 = ((15, 10, 47, 3),) * 6


def initial(p):
    r = bare(p)
    f = []
    for x, y in product(range(8), range(NY)):
        i = H.index(2, x, y % 2, 0)
        cell = tuple(mul(ETA, z) for z in r[i:i + 4])
        if x in ARCH:
            d, g = (D5[y], G5[y]) if x == 5 else (D7[y], G7[y])
            cell = (d, neg(d), g, cell[3])
        f.extend(cell)
    return tuple(f)


def tick(f, t, ac):
    bit = (t - 1) % 2
    mid = H.transport(f, NY, bit)
    out, events = H.collide(mid, NY)
    back, _ = H.collide(out, NY)
    assert back == mid
    previous = H.transport(back, NY, bit, True)
    assert previous == f and H.transport(previous, NY, bit) == mid
    assert account(mid) == account(out) == ac
    return mid, out, events


def history(f, n):
    full, mids, events = [f], [None], [None]
    ac = account(f)
    for t in range(1, n + 1):
        m, f, ev = tick(f, t, ac)
        full.append(f)
        mids.append(m)
        events.append(ev)
    return full, mids, events


def exchange(f, p, new):
    result = list(f)
    incoming, outgoing = [], []
    for y in range(0, NY, 2):
        i = ix(0, y, 0)
        expected = [mul(ETA, P[p]), neg(mul(ETA, P[p]))]
        assert result[i:i + 2] == expected
        outgoing.extend(expected + [Z, Z])
        nxt = [mul(ETA, P[new]), neg(mul(ETA, P[new]))]
        incoming.extend(nxt + [Z, Z])
        result[i:i + 2] = nxt
    result = tuple(result)
    assert account(result) == account(f)
    assert account(f + tuple(incoming)) == account(result + tuple(outgoing))
    return result


def baseline():
    starts = [initial(p) for p in range(5)]
    assert len({account(f) for f in starts}) == 1
    assert account(starts[0])[2:] == ((48936, 0, 17556, 17556), 80316)
    first = [history(f, 114) for f in starts]
    for p, hh in enumerate(first):
        assert all(col(hh[0][114], x) == col(starts[p], x) for x in (0, 6))
        assert hh[0][114][3::4] == starts[p][3::4]
        for t in range(1, 115):
            ev = tuple(e for e in hh[2][t] if e[0] not in (0, 6))
            want = ()
            if p == 1 and t == 113:
                want = tuple((5, y, 1) for y in (0, 2, 4))
            if p == 1 and t == 114:
                want = tuple((x, y, 1) for x, y in product(ARCH, (0, 2, 4)))
            assert ev == want
    loaded25 = {(p, new): exchange(first[p][0][114], p, new)
                for p, new in product(range(5), repeat=2)}
    loaded = {k: loaded25[k] for k in KEYS}
    assert len(set(loaded25.values())) == 10
    assert all(f == loaded[int(p == 1), new] for (p, new), f in loaded25.items())
    second = {k: history(f, 122) for k, f in loaded.items()}
    for hh in second.values():
        assert not any(x not in (0, 6) for ev in hh[2][1:] for x, y, tag in ev)
    print('BASELINE', 'FIRST_Q', account(starts[0])[3], 'INPUT_PAIRS', 25,
          'DISTINCT_SECOND_STATES', len(loaded), 'SECOND_HORIZON', 122,
          'FIRST_ENDPOINT_SHA256', digest([h[0][114] for h in first]))
    return starts, first, second


def vert(vector, bit):
    out = list(vector)
    for i in range(bit, NY, 2):
        k = (i + 1) % NY
        out[i], out[k] = H.transport_pair(vector[i], vector[k], False)
    return tuple(out)


def raw_wheels():
    result = []
    for values in ((1, -1, -3, 0, -3, 0), (1, -1, 3, 0, -3, 0)):
        v = tuple(sc(a, O) for a in values)
        hh = [v]
        for t in range(1, 237):
            v = vert(v, (t - 1) % 2)
            hh.append(v)
        result.append(hh)
    return result


def event_list(first, second, T, row):
    unique = {}
    raw_count = 0
    for p in range(5):
        for t, y in product(range(1, 115), range(NY)):
            r = first[p][1][t][ix(4, y, 3)]
            unique.setdefault((t, y, r), ('first', p, t, y))
            raw_count += 1
    for p, new in product(range(5), repeat=2):
        hh = second[int(p == 1), new]
        for t, y in product(range(1, T + 1), range(NY)):
            if new == 1 and t == T and y == row:
                continue
            r = hh[1][t][ix(4, y, 3)]
            unique.setdefault((114 + t, y, r), ('second', p, new, t, y))
            raw_count += 1
    return tuple((k, label) for k, label in unique.items()), raw_count


def wheel_word(hh, phase, row, target):
    word = []
    for t in range(1, target):
        bit = (t - 1) % 2
        y = row if row % 2 == bit else (row - 1) % NY
        z = (y + 1) % NY
        a, b = hh[phase + t - 1][y], hh[phase + t - 1][z]
        if a != b and not H.even(sub(a, b)):
            word.append('R')
        elif H.transport_pair(a, b, False) != (a, b):
            word.append('C')
        else:
            word.append('.')
    return ''.join(word)


def synthesize(T, first, second, wheels):
    at = 114 + T
    cases, rejects, first_bad = 0, Counter(), {}
    evs = {y: event_list(first, second, T, y) for y in (0, 2, 4)}
    for assignment, su, sv, row, tag in product(range(2), range(0, 33, 2),
                                               range(0, 33, 2), (0, 2, 4), (1, 2)):
        cases += 1
        ident = (assignment, su, sv, row, tag)
        uh, vh = wheels[assignment], wheels[1 - assignment]
        ut, vt = uh[su + at][row], vh[sv + at][row]
        positive = {second[old, 1][1][T][ix(4, row, 3)] for old in (0, 1)}
        negative = {second[old, new][1][T][ix(4, row, 3)]
                    for old, new in product(range(2), (0, 2, 3, 4))}
        assert len(positive) == len(negative) == 1
        rstar, rneg = next(iter(positive)), next(iter(negative))
        assert rstar != rneg
        fstar = mul(mul(J, RI), DELTA) if tag == 1 else neg(mul(RI, DELTA))
        dstar = mul(RI, DELTA) if tag == 1 else mul(J, fstar)
        g = add(rstar, sc(2, fstar))
        cell, actual_tag = H.collision((dstar, neg(dstar), g, rstar))
        assert actual_tag == tag and sub(cell[3], rstar) == DELTA
        assert sub(cell[2], g) == neg(DELTA)
        equations = {}
        rejection = None
        refused = Counter()
        examples = {}
        aliases = 0
        for (t, y, rad), label in evs[row][0]:
            du, dv = sub(uh[su + t][y], ut), sub(vh[sv + t][y], vt)
            fd = sub(g, rad)
            if not H.even(sub(du, dv)) or not H.even(fd):
                why = 'material' if not H.even(sub(du, dv)) else 'radiation'
                refused[why] += 1
                examples.setdefault(why, (label, sub(du, dv), fd))
                continue
            if du == dv == Z:
                aliases += 1
                _, hit = H.collision((dstar, neg(dstar), g, rad))
                if hit:
                    rejection = ('alias', label, hit, rad, ut, vt)
                    break
                continue
            targets = (q(mul(JI, fd)), q(mul(J, fd)))
            equations.setdefault((du, dv, targets), label)
        if rejection:
            rejects[rejection[0]] += 1
            first_bad.setdefault(rejection[0], (ident, rejection[1:]))
            continue
        fixed_a = [(du, targets) for du, dv, targets in equations if dv == Z]
        fixed_b = [(du, dv, targets) for du, dv, targets in equations if dv != Z]
        K = len(equations) + aliases
        bound = 4 * K + 1
        dm = sc(2, dstar)
        A = next((a for a in range(1, 2 * bound, 2)
                  if all(q(add(dm, sc(a, du))) not in targets
                         for du, targets in fixed_a)), None)
        assert A is not None, 'proved A bound failed'
        B = next((b for b in range(1, 2 * bound, 2)
                  if all(q(sub(add(dm, sc(A, du)), sc(b, dv))) not in targets
                         for du, dv, targets in fixed_b)), None)
        assert B is not None, 'proved B bound failed'
        c = sub(sub(sc(A, ut), sc(B, vt)), dm)
        r0 = tuple(sc(A, z) for z in uh[su])
        r2 = tuple(add(sc(B, z), c) for z in vh[sv])
        words = (wheel_word(uh, su, row, at), wheel_word(vh, sv, row, at))
        qualified = all('R' in w and 'C' in w for w in words)
        design = dict(T=T, at=at, ident=ident, A=A, B=B, c=c, g=g, dstar=dstar,
                      rstar=rstar, rneg=rneg, r0=r0, r2=r2, row=row, tag=tag,
                      raw_constraints=evs[row][1], unique_events=len(evs[row][0]),
                      equations=len(equations), aliases=aliases, bound=bound,
                      parity_refused=tuple(sorted(refused.items())),
                      parity_examples=tuple(sorted(examples.items())),
                      words=words, cases=cases, rejects=tuple(sorted(rejects.items())),
                      first_bad=tuple(sorted(first_bad.items())))
        yield design, qualified
        if qualified:
            return
        rejects['non_refusal'] += 1
        first_bad.setdefault('non_refusal', ident)
    print('SEARCH_FAILURE', T, 'CASES', cases, 'REJECTS', sorted(rejects.items()),
          'FIRST_BAD', sorted(first_bad.items()))


def install(f, design):
    f = list(f)
    for y in range(NY):
        i = ix(4, y, 0)
        assert f[i:i + 3] == [Z, Z, Z]
        f[i:i + 3] = [design['r0'][y], design['r2'][y], design['g']]
    return tuple(f)


def clean_classes(fields, feature, classify):
    groups = {}
    for key, f in fields.items():
        groups.setdefault(classify(key), set()).add(feature(f))
    return (all(len(a) == 1 for a in groups.values())
            and all(a.isdisjoint(b) for a, b in combinations(groups.values(), 2)))


def replay(design, qualified, starts, first, second):
    T, row, tag = design['T'], design['row'], design['tag']
    horizon = max(114, T + 32)
    print('SELECT', design)
    installed = [install(f, design) for f in starts]
    ac = account(installed[0])
    assert len({account(f) for f in installed}) == 1
    print('ACCOUNTS', T, ac, 'INCREMENT', tuple(sub(a, b) for a, b in
          zip(ac[:3], account(starts[0])[:3])), 'DELTA_Q', ac[3] - 80316)
    first_new = [history(f, 114) for f in installed]
    for p, hh in enumerate(first_new):
        for t in range(1, 115):
            assert hh[2][t] == first[p][2][t]
            for stage in (1, 0):
                assert outside(hh[stage][t]) == outside(first[p][stage][t])
    all25 = {(p, new): exchange(first_new[p][0][114], p, new)
             for p, new in product(range(5), repeat=2)}
    loaded = {k: all25[k] for k in KEYS}
    assert len(set(all25.values())) == 10
    assert all(f == loaded[int(p == 1), new] for (p, new), f in all25.items())
    actual = {k: history(f, horizon) for k, f in loaded.items()}
    for k, hh in actual.items():
        for t in range(1, T + 1):
            expected = second[k][2][t]
            if k[1] == 1 and t == T:
                expected = tuple(sorted(expected + ((4, row, tag),)))
            assert hh[2][t] == expected
            assert outside(hh[1][t]) == outside(second[k][1][t])
            if t < T or k[1] != 1:
                assert outside(hh[0][t]) == outside(second[k][0][t])
            else:
                changed = tuple(i for i, (a, b) in enumerate(zip(hh[0][t], hh[1][t]))
                                if a != b and i // (4 * NY) == 4)
                assert changed == tuple(ix(4, row, r) for r in range(4))
                assert sub(hh[0][t][ix(4, row, 3)], hh[1][t][ix(4, row, 3)]) == DELTA
                assert sub(hh[0][t][ix(4, row, 2)], hh[1][t][ix(4, row, 2)]) == neg(DELTA)
    target = {k: hh[0][T] for k, hh in actual.items()}
    fresh = lambda f: pair(f, row)
    old = lambda f: material(f, ARCH)
    bank = lambda f: material(f, (4,))
    features = dict(fresh_pair=(fresh, lambda k: int(k[1] == 1)),
                    fresh_bank=(bank, lambda k: int(k[1] == 1)),
                    old_material=(old, lambda k: k[0]),
                    joint_pair=(lambda f: (old(f), fresh(f)),
                                lambda k: (k[0], int(k[1] == 1))),
                    joint_bank=(lambda f: (old(f), bank(f)),
                                lambda k: (k[0], int(k[1] == 1))))
    assert all(clean_classes(target, feature, classify) for feature, classify in features.values())
    first_loss = {name: None for name in features}
    literal_loss = None
    first_bank_b = None
    first_archive_b = None
    for t in range(T + 1, horizon + 1):
        for stage, label in ((1, 'post-C'), (0, 'full')):
            ff = {k: hh[stage][t] for k, hh in actual.items()}
            for name, (feature, classify) in features.items():
                if first_loss[name] is None and not clean_classes(ff, feature, classify):
                    first_loss[name] = (t, label)
            if literal_loss is None and any(fresh(f) != fresh(target[k]) for k, f in ff.items()):
                literal_loss = (t, label)
        for k, hh in actual.items():
            for event in hh[2][t]:
                if event[0] == 4 and first_bank_b is None:
                    first_bank_b = (t, k, event)
                if event[0] in ARCH and first_archive_b is None:
                    first_archive_b = (t, k, event)
    reset = Counter()
    for (oldbit, new), hh in actual.items():
        weight = 1 if oldbit else 4
        source = col(hh[0][114], 0) == col(starts[new], 0)
        worker = col(hh[0][114], 6) == col(starts[new], 6)
        reset['source'] += weight * source
        reset['worker'] += weight * worker
        reset['both'] += weight * (source and worker)
    print('TARGET', T, 'ABSOLUTE', 114 + T, 'ROW', row, 'TAG', tag,
          'NEGATIVE_PAIR', fresh(target[0, 0]), 'POSITIVE_PAIR', fresh(target[0, 1]),
          'CORR_DELTA', DELTA, 'CLASSES', (2, 2, 4), 'REFUSAL_QUALIFIED', qualified)
    print('CONTINUATION', T, 'HORIZON', horizon, 'FIRST_LOSS', first_loss,
          'LITERAL_PAIR_LOSS', literal_loss, 'NEXT_BANK_B', first_bank_b,
          'NEXT_ARCHIVE_B', first_archive_b, 'RESTORE114', sorted(reset.items()))
    print('FIELD_DIGESTS', T, 'FIRST114', digest([h[0][114] for h in first_new]),
          'SECOND_TARGET', digest([actual[k][0][T] for k in KEYS]),
          'SECOND114', digest([actual[k][0][114] for k in KEYS]),
          'SECOND_END', digest([actual[k][0][horizon] for k in KEYS]))


def main():
    starts, first, second = baseline()
    wheels = raw_wheels()
    for T in (89, 90):
        found = False
        for design, qualified in synthesize(T, first, second, wheels):
            replay(design, qualified, starts, first, second)
            if qualified:
                found = True
                break
        print('TARGET_DISPOSITION', T, 'PASS' if found else 'BOUNDED_FAIL')
    print('DONE NON-CANONICAL exact contact synthesis; no restoration or physical promotion')


if __name__ == '__main__':
    main()
