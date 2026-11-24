#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Exact local audit of the prospectively frozen co-located writer."""
import hashlib
import itertools
import json

Z = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
JROOT = (0, 1, 0, 0)
RHO = (0, 0, 1, 0)
UNIT = (1, 0, 1, 0)
PHI = (0, 0, -1, -1)
checks = 0


def check(test, label):
    global checks
    checks += 1
    if not test:
        raise AssertionError(label)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return add(a, neg(b))


def scale(n, a):
    return tuple(n * x for x in a)


def mul(a, b):
    c = [0] * 7
    for k in range(4):
        for l in range(4):
            c[k + l] += a[k] * b[l]
    for k in range(6, 3, -1):
        for l in range(1, 5):
            c[k - l] -= c[k]
    return tuple(c[:4])


def power(a, n):
    out = ONE
    for _ in range(n):
        out = mul(out, a)
    return out


ROOTS = tuple(power(JROOT, n) for n in range(5))


def conjugate(a):
    out = Z
    for k, v in enumerate(a):
        out = add(out, scale(v, ROOTS[(-k) % 5]))
    return out


def h(a):
    return mul(a, conjugate(a))


def q(a):
    n = 5 * sum(x * x for x in a) - sum(a) ** 2
    check(n % 2 == 0, 'integral Q')
    return n // 2


def total(xs):
    out = Z
    for x in xs:
        out = add(out, x)
    return out


def ordinary(a, b):
    delta = sub(a, b)
    if any(x % 2 for x in delta):
        return a, b, False
    t = tuple(x // 2 for x in delta)
    c = tuple(x // 2 for x in add(a, b))
    rt = mul(RHO, t)
    return add(c, rt), sub(c, rt), True


def loaded(x, v, e, field):
    numerator = add(sub(sub(scale(2, v), x), e), field)
    if any(a % 4 for a in numerator):
        return x, v, field, False
    d = tuple(a // 4 for a in numerator)
    current = mul(sub(RHO, ONE), d)
    return sub(x, current), add(v, current), add(field, current), True


def generic_account(x, v, e, field, norm):
    return total(norm(a) for a in (x, v, e, sub(v, e), field))


def generic_audit():
    admitted = 0
    samples = (Z, ONE, JROOT, RHO)
    for x, v, e, field in itertools.product(samples, repeat=4):
        start = (x, v, field)
        expected = generic_account(x, v, e, field, h)
        invariant = (add(x, v), sub(field, v))
        first = None
        for step in range(5):
            xx, vv, ff, yes = loaded(x, v, e, field)
            if step == 0:
                admitted += yes
                first = yes
            check(yes == first, 'general admission invariant')
            check(generic_account(xx, vv, e, ff, h) == expected,
                  'general loaded Hermitian account')
            check((add(xx, vv), sub(ff, vv)) == invariant,
                  'general Gauss residual and sum')
            check(all((sum(a) - sum(b)) % 5 == 0
                      for a, b in zip((x, v, field), (xx, vv, ff))),
                  'general residues')
            x, v, field = xx, vv, ff
        check((x, v, field) == start, 'general C5')
    return {'inputs': 256, 'admitted': admitted}


def account(slots, field, norm):
    values = [norm(slots[0]), norm(field)]
    for v in slots[1:]:
        values.extend((norm(v), norm(Z), norm(sub(v, Z))))
    if norm is q:
        return sum(values)
    return total(values)


def run(slots, field, word, phase_family=False):
    slots = tuple(slots)
    initial_q = account(slots, field, q)
    initial_h = account(slots, field, h)
    residues = tuple(sum(x) % 5 for x in slots)
    initial_field_residue = sum(field) % 5
    stats = {'attempts': 0, 'admitted': 0, 'changed': 0,
             'diagonal_admitted': 0, 'field_changes': 0}
    for cut, (a, b) in enumerate(word, 1):
        old, old_f = slots, field
        shadow = list(old)
        shadow[a], shadow[b], shadow_yes = ordinary(old[a], old[b])
        shadow_f = add(old_f, sub(old[0], shadow[0]))
        actual = list(old)
        if 0 in (a, b):
            v = b if a == 0 else a
            actual[0], actual[v], field, yes = loaded(old[0], old[v], Z, old_f)
        else:
            actual[a], actual[b], yes = ordinary(old[a], old[b])
        slots = tuple(actual)
        tag = f'cut {cut}, edge {(a, b)}'
        check((slots, field, yes) == (tuple(shadow), shadow_f, shadow_yes),
              'loaded/shadow ' + tag)
        check(neg(field) == slots[0] and field == total(slots[1:]),
              'Gauss ' + tag)
        check(total(slots) == Z, 'total charge ' + tag)
        check(account(slots, field, q) == initial_q, 'full Q ' + tag)
        check(account(slots, field, h) == initial_h, 'full h ' + tag)
        check(tuple(sum(x) % 5 for x in slots) == residues, 'slot residues ' + tag)
        check(sum(field) % 5 == initial_field_residue, 'field residue ' + tag)
        if phase_family:
            check(all(q(v) == 2 for v in slots), 'root account ' + tag)
        stats['attempts'] += 1
        stats['admitted'] += yes
        stats['changed'] += slots != old
        stats['diagonal_admitted'] += yes and slots == old
        stats['field_changes'] += field != old_f
    return slots, field, stats


def inverse(word):
    return [edge for edge in reversed(word) for _ in range(4)]


def pword(i, j):
    a = (2 * i, 2 * i + 1)
    k = [(2 * i, 2 * j + 1), (2 * i + 1, 2 * j)]
    word = []
    for n in range(1, 5):
        word.append(a)
        word.extend(k * n)
    word.append(a)
    check(len(word) == 25, 'P length')
    return word


def phase_state(phases):
    return tuple(v for r in phases for v in (ROOTS[r % 5], neg(ROOTS[r % 5])))


def small_audit():
    helper = neg(add(scale(3, ONE), RHO))
    family = [(f'Jrho{r}', mul(UNIT, power(RHO, r))) for r in range(5)]
    family.append(('phi', PHI))
    word = [(0, 2), (0, 3)]
    rows = []
    for name, d in family:
        start = (neg(d), d, helper, Z, neg(helper))
        check(account(start, d, q) == 80, 'small full account')
        end, field, stats = run(start, d, word)
        target = (neg(d), d, scale(-2, UNIT), sub(RHO, ONE), neg(helper)) \
            if name == 'Jrho0' else start
        check(end == target and field == d, 'small endpoint ' + name)
        check(stats['admitted'] == (2 if name == 'Jrho0' else 0),
              'small admission ' + name)
        check(total(end[2:]) == Z, 'neutral retained archive')
        back, back_f, _ = run(end, field, inverse(word))
        check((back, back_f) == (start, d), 'small full inverse')
        rows.append({'input': name, 'record': list(end[3]), 'record_q': q(end[3]),
                     'account': 80, **stats})
    return rows


def phase_audit():
    word = pword(0, 1) * 2 + pword(0, 2) * 2 + pword(1, 2) * 2
    check(len(word) == 150 and len(inverse(word)) == 600, 'W lengths')
    rows, writer_rows = [], []
    sums = {k: 0 for k in ('admitted', 'changed', 'diagonal_admitted', 'field_changes')}
    for r, s, t in itertools.product(range(5), repeat=3):
        start = phase_state((r, s, t))
        field = neg(start[0])
        check(account(start, field, q) == 24, 'phase full account')
        end, end_f, stats = run(start, field, word, True)
        target = ((r + 3*s + 2*t) % 5, (r + 4*s + t) % 5, (2*s + 4*t) % 5)
        check(end == phase_state(target), 'phase matrix')
        if t == s:
            check(target == (r, r, s), 'copy formula')
            check(end[:2] == start[:2] and end[4:] == start[4:] and end_f == field,
                  'source reference field return')
            writer_rows.append([r, s, *target, stats['field_changes']])
        back, back_f, _ = run(end, end_f, inverse(word), True)
        check(back == start and back_f == field, 'occupied full inverse')
        rows.append([r, s, t, *target])
        for k in sums:
            sums[k] += stats[k]
    matrix_bytes = json.dumps(rows, separators=(',', ':')).encode()
    return {'inputs': 125, 'writer_inputs': 25, 'account': 24,
            'forward_contacts': 150, 'inverse_contacts': 600,
            'matrix_sha256': hashlib.sha256(matrix_bytes).hexdigest(),
            'writer_rows': writer_rows, 'forward_totals': sums}


def main():
    general = generic_audit()
    small = small_audit()
    phase = phase_audit()
    print(json.dumps({'status': 'PASS', 'general': general, 'two_contact': small,
                      'phase': phase, 'checks': checks}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
