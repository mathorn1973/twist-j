#!/usr/bin/env python3
"""Exact complete four-slot lower-bound reconstruction. SPDX-License-Identifier: Apache-2.0.

Author: A. M. Thorn. Result-exposed, independently reimplemented audit;
not a blind independent-author confirmation. No external fixtures/imports.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import isqrt
import json

Z = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
THREE = (3, 0, 0, 0)
SIX = (6, 0, 0, 0)
N = 26
CAP = 60


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return add(a, neg(b))


def times(a, k):
    return tuple(k * x for x in a)


def mul(a, b):
    c = [0] * 5
    for i, x in enumerate(a):
        for k, y in enumerate(b):
            c[(i + k) % 5] += x * y
    return tuple(c[i] - c[4] for i in range(4))


def jpower(k):
    c = [0] * 5
    c[k % 5] = 1
    return tuple(c[i] - c[4] for i in range(4))


def bar(a):
    out = Z
    for i, x in enumerate(a):
        out = add(out, times(jpower(-i), x))
    return out


def energy(a):
    v = 5 * sum(x*x for x in a) - sum(a)**2
    assert v % 2 == 0
    return v // 2


@lru_cache(maxsize=None)
def norm(a):
    v = mul(a, bar(a))
    assert v[1] == 0 and v[2] == v[3]
    h = (v[0], -v[2])  # h=A+B*phi, phi=-j^2-j^3
    assert 2*h[0] + h[1] == energy(a)
    return h


def residue(a):
    return sum(a) % 5


def parity(a):
    return sum((x % 2) << i for i, x in enumerate(a))


def parity_counts(state):
    v = 0
    for a in state:
        v ^= 1 << parity(a)
    return v


def accounts(state):
    s, h = Z, (0, 0)
    for a in state:
        s = add(s, a)
        h = add(h, norm(a))
    return s, h, tuple(sorted(Counter(map(residue, state)).items())), parity_counts(state)


@lru_cache(maxsize=None)
def pair(a, b, k):
    if parity(a) != parity(b):
        return a, b
    s = tuple(x // 2 for x in add(a, b))
    d = tuple(x // 2 for x in sub(a, b))
    d = mul(jpower(2*k), d)
    return add(s, d), sub(s, d)


def neighbours(state):
    # Same-value pairs are identities; rejected pairs are identities.
    values = sorted(set(state))
    for i, a in enumerate(values):
        for b in values[i+1:]:
            if parity(a) != parity(b):
                continue
            rest = list(state)
            rest.remove(a)
            rest.remove(b)
            for k in range(1, 5):
                c, d = pair(a, b, k)
                yield tuple(sorted(rest + [c, d]))


@lru_cache(maxsize=None)
def component(start):
    seen = {start}
    queue = deque([start])
    while queue:
        for nxt in neighbours(queue.popleft()):
            if nxt not in seen:
                seen.add(nxt)
                if len(seen) > CAP:
                    return None  # UNKNOWN, never a negative certificate
                queue.append(nxt)
    return frozenset(seen)


def full_source(bank):
    return tuple(sorted((SIX,) + (Z,)*21 + tuple(bank)))


def full_target(bank):
    return tuple(sorted((THREE,)*4 + (Z,)*18 + tuple(bank)))


def scalars(bound):
    r = isqrt(2*bound)
    out = []
    for a in product(range(-r, r+1), repeat=4):
        q = energy(a)
        assert q >= 0 and 2*q >= sum(x*x for x in a)
        assert (q - 2*residue(a)**2) % 5 == 0
        if q <= bound:
            norm(a)
            out.append(a)
    return sorted(out, key=lambda a: (energy(a), a))


def multisets(pool, count, total, start=0, prefix=()):
    if count == 0:
        if total == 0:
            yield tuple(sorted(prefix))
        return
    for i in range(start, len(pool)):
        a = pool[i]
        q = energy(a)
        if count*q > total:
            break
        yield from multisets(pool, count-1, total-q, i, prefix+(a,))


def bank_key(bank):
    s, h = Z, (0, 0)
    for a in bank:
        s, h = add(s, a), add(h, norm(a))
    return s, h


def target_banks(pool, total):
    zeros = [a for a in pool if residue(a) == 0]
    ones = defaultdict(list)
    for a in pool:
        if residue(a) == 1:
            ones[energy(a)].append(a)
    for q in sorted(ones):
        if q > total:
            continue
        for triple in multisets(zeros, 3, total-q):
            for a in ones[q]:
                yield tuple(sorted(triple+(a,)))


def digest(rows):
    return sha256(json.dumps(sorted(rows), separators=(',', ':')).encode('ascii')).hexdigest()


def census(pool, total):
    initial = list(multisets([a for a in pool if residue(a) == 3], 4, total))
    final = list(target_banks(pool, total))
    assert len(initial) == len(set(initial))
    assert len(final) == len(set(final))
    buckets = defaultdict(list)
    for b in final:
        s, h = bank_key(b)
        buckets[(add(s, SIX), h)].append(b)
    tally = Counter()
    sizes = Counter()
    certificates = []
    for a in initial:
        aa = full_source(a)
        a_parity = parity_counts(aa)
        compatible = buckets.get(bank_key(a), ())
        tally['account_sources'] += bool(compatible)
        for b in compatible:
            tally['account_pairs'] += 1
            bb = full_target(b)
            if a_parity != parity_counts(bb):
                tally['parity_excluded'] += 1
                certificates.append((a, b, 'parity'))
                continue
            closed = component(bb)
            if closed is not None:
                assert aa not in closed, ('CHEAPER_WORD', total, a, b)
                tally['target_closed'] += 1
                sizes['target_'+str(len(closed))] += 1
                certificates.append((a, b, 'target', len(closed), digest(closed)))
                continue
            closed = component(aa)
            if closed is not None:
                assert bb not in closed, ('CHEAPER_WORD', total, a, b)
                tally['source_closed'] += 1
                sizes['source_'+str(len(closed))] += 1
                certificates.append((a, b, 'source', len(closed), digest(closed)))
                continue
            tally['unresolved'] += 1
            certificates.append((a, b, 'UNKNOWN'))
    result = {'energy': total, 'initial_banks': len(initial), 'final_banks': len(final),
              'initial_sha256': digest(initial), 'final_sha256': digest(final),
              'counts': dict(sorted(tally.items())), 'closed_sizes': dict(sorted(sizes.items())),
              'exclusion_sha256': digest(certificates)}
    print(json.dumps(result, sort_keys=True, separators=(',', ':')), flush=True)
    assert tally['account_pairs'] == tally['parity_excluded'] + tally['target_closed'] + tally['source_closed']
    assert tally['unresolved'] == 0, ('INCOMPLETE', total)


def algebra_audit():
    assert mul(jpower(2), jpower(3)) == ONE
    tests = 0
    for cs in product((-1, 0, 1), repeat=8):
        a, b = cs[:4], cs[4:]
        baseline = accounts((a, b))
        for k in range(1, 5):
            c, d = pair(a, b, k)
            assert accounts((c, d)) == baseline
            assert pair(c, d, 5-k) == (a, b)
            assert pair(b, a, k) == (d, c)
            tests += 1
        c, d = a, b
        for _ in range(5):
            c, d = pair(c, d, 1)
        assert (c, d) == (a, b)
    print('ALGEBRA pair_power_cases='+str(tests)+' inverse_order_accounts=PASS', flush=True)


def replay(name, bank, steps, target, final_bank, claimed_energy):
    state = [SIX]+[Z]*21+list(bank)
    original = state.copy()
    baseline = accounts(state)
    assert sum(map(energy, bank)) == claimed_energy
    for i, k, power in steps:
        assert parity(state[i]) == parity(state[k]), (name, i, k, power)
        state[i], state[k] = pair(state[i], state[k], power)
        assert accounts(state) == baseline
    assert sorted(state) == sorted(list(target)+[Z]*18+list(final_bank)), name
    assert sum(map(energy, final_bank)) == claimed_energy
    for i, k, power in reversed(steps):
        state[i], state[k] = pair(state[i], state[k], 5-power)
    assert state == original
    print(name+' contacts='+str(len(steps))+' auxiliary_account='+str(claimed_energy)+' forward_inverse=PASS', flush=True)


def witnesses():
    positive = [(1,0,3),(22,1,2),(1,2,3),(1,24,4),(1,0,3),(3,0,1),
                (1,22,3),(3,1,4),(0,22,1),(24,22,3),(22,23,3),
                (3,23,1),(22,1,3),(1,3,1),(0,1,3),(0,25,4)]
    replay('POSITIVE', [(-1,-1,0,0),(1,2,0,0),(2,0,0,1),(2,0,1,0)],
           positive, [THREE]*4, [(1,0,0,0),(-1,1,0,0),(-2,-2,0,-1),(0,2,1,2)],27)
    signed = [(0,1,3),(0,23,1),(0,1,1),(23,24,2),(0,24,1),(22,24,2),
              (1,23,1),(0,25,3),(0,1,2),(0,24,1),(23,25,3),(0,23,1),(0,1,1),(22,23,4)]
    eta = (1,1,0,0)
    replay('SIGNED', [eta,neg(eta),neg(eta),neg(eta)], signed,
           [neg(THREE),THREE,THREE,THREE], [times(eta,-2),Z,Z,Z],12)


def main():
    print('P-RELATIVE-CONTACT-FOUR-SLOT-MINIMUM-1 exact reconstruction', flush=True)
    algebra_audit()
    witnesses()
    pool = scalars(22)
    print('SCALARS q<=22 count='+str(len(pool))+' sha256='+digest(pool), flush=True)
    for e in (12,17,22):
        census(pool, e)
        component.cache_clear()
    print('PASS positive_minimum_27 signed_minimum_12 supplied_contact_L1_only', flush=True)


if __name__ == '__main__':
    main()
