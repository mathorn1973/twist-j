#!/usr/bin/env python3
"""Same-author adversarial audit, independent arithmetic; not a second agent."""
from __future__ import annotations
import hashlib
import itertools
import json

ONE = (1, 0, 0, 0)
J = (1, 0, 1, 0)
JI = (0, -1, -1, 0)


def reduce5(c):
    return tuple(c[i] - c[4] for i in range(4))


def mul(a, b):
    c = [0] * 5
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[(i + j) % 5] += x * y
    return reduce5(c)


def automorphism(a, exponent):
    c = [0] * 5
    for i, x in enumerate(a):
        c[(exponent * i) % 5] += x
    return reduce5(c)


def traces(a):
    p = mul(a, automorphism(a, 4))
    q = mul(mul(a, J), automorphism(mul(a, J), 4))
    t0 = 4 * p[0] - sum(p[1:])
    t1 = 4 * q[0] - sum(q[1:])
    assert t0 % 2 == t1 % 2 == 0
    return t0 // 2, t1 // 2


def norm(a):
    p = mul(a, automorphism(a, 4))
    n = mul(p, automorphism(p, 2))
    assert n[1:] == (0, 0, 0)
    return n[0]


def power_step(a, exponent):
    b = J if exponent >= 0 else JI
    for _ in range(abs(exponent)):
        a = mul(a, b)
    return a


def census(strip):
    groups = {}
    pairs = set()
    groups25 = {}
    for a in strip:
        s = traces(a)
        pairs.add(s)
        for modulus, target in ((5, groups), (25, groups25)):
            key = s + tuple(x % modulus for x in a)
            target.setdefault(key, []).append(a)
    collisions = []
    checked_differences = 0
    for key, group in groups.items():
        if len(group) > 1:
            collisions.append((norm(group[0]), key, group[0], group[1]))
            for a, b in itertools.combinations(group, 2):
                delta = tuple(x - y for x, y in zip(a, b))
                nd = norm(delta)
                assert 5**4 <= nd <= 16 * norm(a)
                checked_differences += 1
    first = min(collisions)
    summary = {
        'bound': 941,
        'strip_count': len(strip),
        'strip_below': sum(norm(a) <= 940 for a in strip),
        'strip_sha256': hashlib.sha256(json.dumps(strip, separators=(',', ':')).encode()).hexdigest(),
        'max_abs_coefficient': max(abs(x) for a in strip for x in a),
        'trace_pair_count': len(pairs),
        'mod5_key_count': len(groups),
        'mod25_key_count': len(groups25),
        'mod5_collision_groups': sum(len(g) > 1 for g in groups.values()),
        'mod5_max_fibre': max(map(len, groups.values())),
        'mod5_capacity_shortfall': max(0, 3125 - len(groups)),
        'mod5_first_collision': {
            'norm': first[0], 'key': first[1], 'left': first[2], 'right': first[3]},
    }
    assert all(len(g) == 1 for g in groups25.values())
    return summary, {key: group[0] for key, group in groups25.items()}, checked_differences


def main():
    assert mul(J, JI) == mul(JI, J) == ONE
    strip = []
    scanned = 0
    for a in itertools.product(range(-9, 10), repeat=4):
        scanned += 1
        p = mul(a, automorphism(a, 4))
        assert p[1] == 0 and p[2] == p[3]
        u, v = p[0], -p[2]
        if not (0 <= v < u):
            continue
        n = norm(a)
        if 1 <= n <= 941:
            assert max(map(abs, a)) <= 8
            strip.append(a)
    strip.sort()
    summary, lookup, differences = census(strip)
    assert summary['strip_count'] == 3150 and summary['strip_below'] == 3110
    roundtrips = 0
    for beta in strip:
        for expected_k in (-16, -1, 0, 1, 16):
            alpha = power_step(beta, expected_k)
            s0, s1 = traces(alpha)
            r = tuple(x % 25 for x in alpha)
            k = 0
            while not (2 * s0 < 3 * s1 and 2 * s1 <= 3 * s0):
                if 2 * s0 >= 3 * s1:
                    s0, s1 = s1, 3 * s1 - s0
                    r = tuple(x % 25 for x in mul(r, J))
                    k -= 1
                else:
                    s0, s1 = 3 * s0 - s1, s0
                    r = tuple(x % 25 for x in mul(r, JI))
                    k += 1
            recovered = lookup[(s0, s1) + r]
            assert recovered == beta and k == expected_k
            assert power_step(recovered, k) == alpha
            roundtrips += 1
    print('TWIST-J same-author cyclic-ring adversarial audit; NON-CANONICAL L1')
    print('CENSUS ' + json.dumps(summary, sort_keys=True, separators=(',', ':')))
    print(f'PASS larger_box={scanned} lookup_roundtrips={roundtrips} collision_differences={differences}')
    print('RESULT PASS; method-separated one-architecture audit, not independent-agent confirmation')


if __name__ == '__main__':
    main()
