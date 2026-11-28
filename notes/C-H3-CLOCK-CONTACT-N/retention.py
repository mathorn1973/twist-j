#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""NON-CANONICAL #2137 E. Frozen multiplier family and 32-tick sum retention."""
from collections import Counter
from itertools import product
from pathlib import Path
import hashlib
import importlib.util
import sys

SOURCE = Path(__file__).with_name('verify.py')
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == (
    'c754e65a80a8b10523177296825d4d260c2d79012a59ec3139e6caa2598c9d2d')
spec = importlib.util.spec_from_file_location('contact_primary', SOURCE)
V = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = V
spec.loader.exec_module(V)
H = V.H
Z, O, J, JI, RI = V.Z, V.O, V.J, V.JI, V.RI
add, sub, mul, sc, q = V.add, V.sub, V.mul, V.sc, V.q
T, AT, ROW, HORIZON = 89, 203, 0, 121


def construct(multiplier, first, second, wheels):
    delta = sc(multiplier, V.DELTA)
    rstar = second[0, 1][1][T][V.ix(4, ROW, 3)]
    assert {second[old, 1][1][T][V.ix(4, ROW, 3)] for old in range(2)} == {rstar}
    negative = {second[old, new][1][T][V.ix(4, ROW, 3)]
                for old, new in product(range(2), (0, 2, 3, 4))}
    assert len(negative) == 1 and rstar not in negative
    fstar, dstar = mul(mul(J, RI), delta), mul(RI, delta)
    g = add(rstar, sc(2, fstar))
    uh, vh = wheels
    ut, vt = uh[AT][ROW], vh[AT][ROW]
    events, raw_count = V.event_list(first, second, T, ROW)
    equations = {}
    aliases = refused = 0
    for (t, y, rad), label in events:
        du, dv, fd = sub(uh[t][y], ut), sub(vh[t][y], vt), sub(g, rad)
        if not H.even(sub(du, dv)) or not H.even(fd):
            refused += 1
            continue
        if du == dv == Z:
            aliases += 1
            _, hit = H.collision((dstar, V.neg(dstar), g, rad))
            if hit:
                return None, ('alias', label, hit, rad)
            continue
        targets = (q(mul(JI, fd)), q(mul(J, fd)))
        equations.setdefault((du, dv, targets), label)
    fixed_a = [(du, targets) for du, dv, targets in equations if dv == Z]
    fixed_b = [(du, dv, targets) for du, dv, targets in equations if dv != Z]
    bound = 4 * (len(equations) + aliases) + 1
    twice = sc(2, dstar)
    A = next((a for a in range(1, 2 * bound, 2)
              if all(q(add(twice, sc(a, du))) not in targets
                     for du, targets in fixed_a)), None)
    assert A is not None, 'proved A bound failed'
    B = next((b for b in range(1, 2 * bound, 2)
              if all(q(sub(add(twice, sc(A, du)), sc(b, dv))) not in targets
                     for du, dv, targets in fixed_b)), None)
    assert B is not None, 'proved B bound failed'
    c = sub(sub(sc(A, ut), sc(B, vt)), twice)
    words = (V.wheel_word(uh, 0, ROW, AT), V.wheel_word(vh, 0, ROW, AT))
    assert all('C' in w and 'R' in w for w in words)
    return dict(m=multiplier, delta=delta, A=A, B=B, c=c, g=g, dstar=dstar,
                r0=tuple(sc(A, z) for z in uh[0]),
                r2=tuple(add(sc(B, z), c) for z in vh[0]),
                bound=bound, equations=len(equations), aliases=aliases,
                refused=refused, raw_constraints=raw_count, unique_events=len(events)), None


def sum0(field):
    return H.ring_sum(field[V.ix(4, y, 0)] for y in range(V.NY))


def next_contacts(field):
    bit = T % 2
    classes, residues, pairs = [], [], []
    for rail in range(4):
        if rail == 3:
            first = 4 if 4 % 2 == bit else 3
            i, k = V.ix(first, ROW, rail), V.ix((first + 1) % 8, ROW, rail)
        else:
            first = ROW if ROW % 2 == bit else (ROW - 1) % V.NY
            i, k = V.ix(4, first, rail), V.ix(4, (first + 1) % V.NY, rail)
        a, b = field[i], field[k]
        difference = sub(a, b)
        kind = 'R' if not H.even(difference) else 'E' if a == b else 'C'
        classes.append(kind)
        residues.append(tuple(v % 2 for v in difference))
        pairs.append((a, b))
    return tuple(classes), tuple(residues), tuple(pairs)


def replay(design, starts, first, second):
    m, delta, A = design['m'], design['delta'], design['A']
    installed = [V.install(f, design) for f in starts]
    ac = V.account(installed[0])
    assert len({V.account(f) for f in installed}) == 1
    assert all(sum0(f) == sc(-6 * A, O) for f in installed)
    first_new = [V.history(f, 114) for f in installed]
    for p, hh in enumerate(first_new):
        for t in range(1, 115):
            assert hh[2][t] == first[p][2][t]
            for stage in (1, 0):
                assert V.outside(hh[stage][t]) == V.outside(first[p][stage][t])
    all25 = {(p, new): V.exchange(first_new[p][0][114], p, new)
             for p, new in product(range(5), repeat=2)}
    loaded = {k: all25[k] for k in V.KEYS}
    assert len(set(all25.values())) == 10
    assert all(f == loaded[int(p == 1), new] for (p, new), f in all25.items())
    actual = {k: V.history(f, HORIZON) for k, f in loaded.items()}
    for key, hh in actual.items():
        for t in range(1, T + 1):
            expected = second[key][2][t]
            if key[1] == 1 and t == T:
                expected = tuple(sorted(expected + ((4, ROW, 1),)))
            assert hh[2][t] == expected
            assert V.outside(hh[1][t]) == V.outside(second[key][1][t])
            if t < T or key[1] != 1:
                assert V.outside(hh[0][t]) == V.outside(second[key][0][t])
            else:
                i = V.ix(4, ROW, 0)
                increments = tuple(sub(a, b) for a, b in zip(hh[0][t][i:i + 4], hh[1][t][i:i + 4]))
                assert increments == (delta, V.neg(delta), V.neg(delta), delta)
        expected_sum = add(sc(-6 * A, O), delta if key[1] == 1 else Z)
        assert sum0(hh[0][T]) == expected_sum
    target = {k: hh[0][T] for k, hh in actual.items()}
    old = lambda f: V.material(f, V.ARCH)
    classify_fresh = lambda k: int(k[1] == 1)
    classify_old = lambda k: k[0]
    classify_pair = lambda k: (k[0], int(k[1] == 1))
    assert V.clean_classes(target, sum0, classify_fresh)
    assert V.clean_classes(target, old, classify_old)
    assert V.clean_classes(target, lambda f: (old(f), sum0(f)), classify_pair)
    losses = dict(bank_B=None, sum_hold=None, fresh_classes=None,
                  old_classes=None, joint_classes=None)
    old_b = literal_pair = None
    for t in range(T + 1, HORIZON + 1):
        for stage, label in ((1, 'post-C'), (0, 'full')):
            fields = {k: hh[stage][t] for k, hh in actual.items()}
            for key, f in fields.items():
                if losses['sum_hold'] is None and sum0(f) != sum0(target[key]):
                    losses['sum_hold'] = (t, label, key, sum0(f))
                if literal_pair is None and V.pair(f, ROW) != V.pair(target[key], ROW):
                    literal_pair = (t, label, key)
            for name, feature, classify in (
                ('fresh_classes', sum0, classify_fresh),
                ('old_classes', old, classify_old),
                ('joint_classes', lambda f: (old(f), sum0(f)), classify_pair)):
                if losses[name] is None and not V.clean_classes(fields, feature, classify):
                    losses[name] = (t, label)
        for key, hh in actual.items():
            for event in hh[2][t]:
                if event[0] == 4 and losses['bank_B'] is None:
                    losses['bank_B'] = (t, 'full', key, event)
                if event[0] in V.ARCH and old_b is None:
                    old_b = (t, key, event)
    positive = actual[0, 1]
    classes, residues, pairs = next_contacts(positive[0][T])
    i = V.ix(4, ROW, 0)
    unchanged = positive[1][T + 1][i:i + 4] == positive[0][T][i:i + 4]
    inverse = None
    if unchanged:
        back, btag = H.collision(positive[1][T + 1][i:i + 4])
        assert btag == 2 and back == positive[1][T][i:i + 4]
        assert positive[0][T + 1][i:i + 4] == back
        inverse = True
    assert classes[2] == ('R' if m % 2 else 'C')
    reset = Counter()
    for (oldbit, new), hh in actual.items():
        weight = 1 if oldbit else 4
        source = V.col(hh[0][114], 0) == V.col(starts[new], 0)
        worker = V.col(hh[0][114], 6) == V.col(starts[new], 6)
        reset['source'] += weight * source
        reset['worker'] += weight * worker
        reset['both'] += weight * (source and worker)
    success = all(v is None for v in losses.values())
    print('E_DESIGN', design)
    print('E_ACCOUNT', m, ac, 'DELTA_Q', ac[3] - 80316,
          'INCREMENT', tuple(sub(a, b) for a, b in zip(ac[:3], V.account(starts[0])[:3])))
    print('E_TARGET', m, 'S0_NEGATIVE', sum0(target[0, 0]),
          'S0_POSITIVE', sum0(target[0, 1]), 'POSITIVE_CELL', positive[0][T][i:i + 4])
    print('E_NEXT_C', m, 'CLASSES', classes, 'RESIDUES', residues,
          'PAIRS', pairs, 'CELL_UNCHANGED', unchanged, 'EXACT_B2_INVERSE', inverse)
    print('E_RETENTION', m, 'PASS32', success, 'FIRST_LOSSES', losses,
          'LITERAL_PAIR_LOSS', literal_pair, 'NEXT_OLD_B', old_b,
          'RESTORE114', sorted(reset.items()),
          'END_SHA256', V.digest([actual[k][0][HORIZON] for k in V.KEYS]))
    return success


def main():
    starts, first, second = V.baseline()
    wheels = V.raw_wheels()
    passed = []
    for m in range(1, 9):
        design, error = construct(m, first, second, wheels)
        if error:
            print('E_ALIAS_FAILURE', m, error)
            continue
        if replay(design, starts, first, second):
            passed.append(m)
    print('E_COMPLETE', 'TRIED', 8, 'PASS32', tuple(passed),
          'SELECT_SMALLEST_M', min(passed) if passed else None)
    print('DONE NON-CANONICAL finite retention; no permanent or restoration claim')


if __name__ == '__main__':
    main()
