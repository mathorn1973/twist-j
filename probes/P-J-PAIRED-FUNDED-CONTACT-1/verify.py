#!/usr/bin/env python3
"""Exact audit of a declared four-slot partner-funded relative J law.

Two arithmetic representations, one author. No blind-review claim.
Standard-library integers only; no runtime files, randomness or network.
"""
from __future__ import annotations

from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
j = (0, 1, 0, 0)
RHO = (0, 0, 1, 0)
J = (1, 0, 1, 0)
JI = (0, -1, -1, 0)
T = (2, 0, 1, 1)
PHI = (0, 0, -1, -1)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def scale(k, x):
    return tuple(k * a for a in x)


def even(x):
    return all(a % 2 == 0 for a in x)


def half(x):
    assert even(x)
    return tuple(a // 2 for a in x)


@lru_cache(maxsize=None)
def mul(x, y):
    p = [0] * 7
    for i, a in enumerate(x):
        for k, b in enumerate(y):
            p[i + k] += a * b
    for n in range(6, 3, -1):
        for k in range(1, 5):
            p[n - k] -= p[n]
        p[n] = 0
    return tuple(p[:4])


def bar(x):
    a, b, c, d = x
    return a-b, -b, d-b, c-b


def trace(x):
    return 4*x[0]-x[1]-x[2]-x[3]


@lru_cache(maxsize=None)
def h(x):
    return mul(x, bar(x))


@lru_cache(maxsize=None)
def q(x):
    numerator = 5*sum(a*a for a in x)-sum(x)**2
    assert numerator % 2 == 0
    value = numerator // 2
    assert numerator == trace(h(x))
    assert value >= 0 and 2*value >= sum(a*a for a in x)
    assert (value == 0) == (x == ZERO)
    return value


def total_h(state):
    result = ZERO
    for x in state:
        result = add(result, h(x))
    return result


def energy(state):
    return sum(q(x) for x in state)


def real_coordinates(value):
    assert value[1] == 0 and value[2] == value[3]
    return value[0], -value[2]


def norm(x):
    a, b = real_coordinates(h(x))
    return a*a+a*b-b*b


def valuation(x):
    if x == ZERO:
        return None
    k = 0
    while even(x):
        x = half(x)
        k += 1
    return k


def power(x, n):
    assert n >= 0
    r = ONE
    for _ in range(n):
        r = mul(r, x)
    return r


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def proposal(z, direction):
    x, y, u, v = z
    c, d = half(add(x, y)), half(sub(x, y))
    e, f = half(add(u, v)), half(sub(u, v))
    d = mul(J if direction == 1 else JI, d)
    f = mul(JI if direction == 1 else J, f)
    return add(c,d), sub(c,d), add(e,f), sub(e,f)


def step(z):
    x, y, u, v = z
    if not even(sub(x,y)) or not even(sub(u,v)):
        return 'parity', z
    d, f = half(sub(x,y)), half(sub(u,v))
    if d == f == ZERO:
        return 'zero', z
    plus = h(f) == mul(T,h(d))
    minus = h(d) == mul(T,h(f))
    assert not (plus and minus)
    if plus:
        return 'forward', proposal(z, 1)
    if minus:
        return 'reverse', proposal(z, -1)
    return 'balance', z


# Separate multiplication and conjugation through five cyclic coefficients.
@lru_cache(maxsize=None)
def cyclic_mul(x, y):
    p = [0]*5
    for i, a in enumerate(x):
        for k, b in enumerate(y):
            p[(i+k) % 5] += a*b
    return tuple(p[i]-p[4] for i in range(4))


@lru_cache(maxsize=None)
def cyclic_h(x):
    c = [0]*5
    for i, a in enumerate(x):
        c[(-i) % 5] += a
    conjugated = tuple(c[i]-c[4] for i in range(4))
    return cyclic_mul(x,conjugated)


def alternate_step(z):
    x, y, u, v = z
    d, f = sub(x,y), sub(u,v)
    if any(a & 1 for a in d+f):
        return 'parity', z
    if d == f == ZERO:
        return 'zero', z
    hd, hf = cyclic_h(d), cyclic_h(f)
    if hf == cyclic_mul(T,hd):
        tag, first, second = 'forward', J, JI
    elif hd == cyclic_mul(T,hf):
        tag, first, second = 'reverse', JI, J
    else:
        return 'balance', z
    move1 = cyclic_mul(sub(first,ONE), tuple(a//2 for a in d))
    move2 = cyclic_mul(sub(second,ONE), tuple(a//2 for a in f))
    return tag, (add(x,move1),sub(y,move1),add(u,move2),sub(v,move2))


def put(digest, row):
    digest.update((json.dumps(row,sort_keys=True,separators=(',',':'),
                              ensure_ascii=True)+'\n').encode('ascii'))


def main():
    assert __debug__, 'Assertions must remain enabled'
    assert mul(J,JI) == ONE
    assert h(J) == T and add(T,h(JI)) == scale(3,ONE)
    assert mul(PHI,PHI) == add(PHI,ONE)
    audit_digest, scalar_digest, chain_digest = sha256(), sha256(), sha256()
    branches, counts = Counter(), Counter()

    def audit(z, label):
        tag, out = step(z)
        assert (tag,out) == alternate_step(z)
        undo_tag, restored = step(out)
        assert (undo_tag,restored) == alternate_step(out)
        assert restored == z
        assert undo_tag == {'forward':'reverse','reverse':'forward'}.get(tag,tag)
        assert add(z[0],z[1]) == add(out[0],out[1])
        assert add(z[2],z[3]) == add(out[2],out[3])
        assert total_h(z) == total_h(out)
        assert energy(z) == energy(out)
        for i in (0,2):
            before, after = sub(z[i],z[i+1]), sub(out[i],out[i+1])
            assert norm(before) == norm(after)
            assert valuation(before) == valuation(after)
        if tag in ('forward','reverse'):
            assert out != z
            assert h(half(sub(out[0],out[1]))) == h(half(sub(z[2],z[3])))
            assert h(half(sub(out[2],out[3]))) == h(half(sub(z[0],z[1])))
        else:
            assert out == z
        put(audit_digest,[label,z,tag,out])
        branches[tag] += 1
        counts[label] += 1
        return tag,out

    for x in product(range(-2,3), repeat=4):
        hx = h(x)
        assert hx == cyclic_h(x)
        assert mul(J,x) == cyclic_mul(J,x)
        assert mul(JI,mul(J,x)) == x
        a,b = real_coordinates(hx)
        a1,b1 = real_coordinates(h(mul(J,x)))
        assert (a1,b1) == (2*a-b,b-a)
        t0,t1 = q(x),q(mul(J,x))
        assert 2*t1 == 3*t0-5*b and 2*b1 == -t0+3*b
        assert t0*t0-5*b*b == 4*norm(x)
        assert norm(mul(J,x)) == norm(x)
        put(scalar_digest,[x,hx,t0,norm(x),a1,b1,t1])
        counts['scalar'] += 1
    assert counts['scalar'] == 625

    alphabet = [ZERO]
    for i in range(4):
        unit = tuple(int(i==k) for k in range(4))
        alphabet.extend((unit,scale(-1,unit)))
    for z in product(alphabet,repeat=4):
        audit(z,'raw')
    assert counts['raw'] == 6561

    small = tuple(product((-1,0,1),repeat=4))
    for d in small:
        for f in small:
            for c in (ZERO,ONE):
                for e in (ZERO,j):
                    z = (add(c,d),sub(c,d),add(e,f),sub(e,f))
                    audit(z,'centered')
                    assert (total_h(proposal(z,1)) == total_h(z)) == (h(f) == mul(T,h(d)))
                    assert (total_h(proposal(z,-1)) == total_h(z)) == (h(d) == mul(T,h(f)))
    assert counts['centered'] == 26244

    for d in small:
        if d == ZERO:
            continue
        for epsilon in (-1,1):
            for ell in range(5):
                f = scale(epsilon,mul(power(RHO,ell),mul(J,d)))
                for c in (ZERO,ONE):
                    for e in (ZERO,j):
                        z = (add(c,d),sub(c,d),add(e,f),sub(e,f))
                        tag,out = audit(z,'matched')
                        assert tag == 'forward'
                        assert half(sub(out[0],out[1])) == mul(J,d)
                        assert half(sub(out[2],out[3])) == mul(JI,f)
    assert counts['matched'] == 3200

    examples = []
    rj = mul(RHO,J)
    for a in (-1,1):
        for mode in range(3):
            if mode == 0:
                z = (scale(2*a,ONE),ZERO,scale(2,rj),ZERO)
                expected_accounts = [8,12,10,10]
            elif mode == 1:
                z = (scale(2*a,ONE),ZERO,rj,scale(-1,rj))
                expected_accounts = [8,6,10,4]
            else:
                z = (scale(a,ONE),scale(-a,ONE),rj,scale(-1,rj))
                expected_accounts = [4,6,6,4]
            initial = z
            tag,out = audit(z,'example')
            assert tag == 'forward'
            accounts = [energy(z[:2]),energy(z[2:]),energy(out[:2]),energy(out[2:])]
            assert accounts == expected_accounts
            if mode < 2:
                assert out[0] == scale(a,add(ONE,J))
                assert out[1] == scale(a,sub(ONE,J))
                assert trace(out[1]) == a
            if mode == 1:
                assert out[2:] == (RHO,scale(-1,RHO))
            examples.append([a,mode,accounts,initial,out])
            z = out
            for _ in range(15):
                _,z = audit(z,'example')
            assert z == initial
    assert counts['example'] == 96

    chain_accounts = []
    for K in range(1,16):
        for a in (-1,1):
            slots = [scale(a,ONE),scale(-a,ONE)]
            for i in range(1,K+1):
                f = mul(power(RHO,i),power(J,i))
                slots.extend((f,scale(-1,f)))
            initial = tuple(slots)
            full_h, full_e = total_h(slots),energy(slots)
            assert full_e == 2+2*lucas(2*K+1)
            if a == 1:
                chain_accounts.append([K,full_e,2*lucas(2*K)])
            history = [initial]
            for i in range(1,K+1):
                before = tuple(slots)
                block = tuple(slots[:2]+slots[2*i:2*i+2])
                tag,out = audit(block,'chain_forward')
                assert tag == 'forward'
                slots[:2],slots[2*i:2*i+2] = out[:2],out[2:]
                assert slots[0] == scale(a,power(J,i))
                assert slots[1] == scale(-a,power(J,i))
                for m in range(1,K+1):
                    f = mul(power(RHO,m),power(J,m-1 if m<=i else m))
                    assert slots[2*m:2*m+2] == [f,scale(-1,f)]
                assert total_h(slots) == full_h and energy(slots) == full_e
                history.append(tuple(slots))
                put(chain_digest,[['forward',K,a,i],before,tag,slots])
            for i in range(K,0,-1):
                before = tuple(slots)
                tag,out = audit(tuple(slots[:2]+slots[2*i:2*i+2]),'chain_reverse')
                assert tag == 'reverse'
                slots[:2],slots[2*i:2*i+2] = out[:2],out[2:]
                assert tuple(slots) == history[i-1]
                assert total_h(slots) == full_h and energy(slots) == full_e
                put(chain_digest,[['reverse',K,a,i],before,tag,slots])
            assert tuple(slots) == initial
    assert counts['chain_forward'] == counts['chain_reverse'] == 240

    jp,trace_prefix = ONE,[]
    for k in range(65):
        assert norm(jp) == 1 and q(jp) == lucas(2*k)
        if 1 <= k <= 13:
            trace_prefix.append(trace(sub(ONE,jp)))
        put(scalar_digest,['J_power',k,jp,q(jp),norm(jp)])
        jp = mul(J,jp)
    assert trace_prefix == [1,3,7,15,26,33,22,-25,-119,-242,-318,-195,326]
    counts['J_power'] = 65

    unfunded = (scale(2,ONE),ZERO,ZERO,ZERO)
    unguarded = proposal(unfunded,1)
    assert energy(unfunded) == 8 and energy(unguarded) == 10
    assert step(unfunded) == ('balance',unfunded)
    z = (scale(2,ONE),ZERO,rj,scale(-1,rj))
    tag,out = step(z)
    assert tag == 'forward' and step(out)[0] == 'reverse'
    def one_sided(value):
        label,result = step(value)
        return result if label == 'forward' else value
    assert z != out and one_sided(z) == one_sided(out) == out
    residues_before = [sum(c)%5 for c in z]
    residues_after = [sum(c)%5 for c in out]
    assert residues_before == [2,0,2,3]
    assert residues_after == [3,4,1,4]
    assert sorted(residues_before) != sorted(residues_after)
    put(audit_digest,['negative_controls',unfunded,unguarded,z,out])
    assert branches['forward'] > 0 and branches['reverse'] > 0
    assert branches['parity'] > 0 and branches['balance'] > 0 and branches['zero'] > 0
    report = {
        'probe':'P-J-PAIRED-FUNDED-CONTACT-1',
        'status':'PASS',
        'counts':dict(counts),
        'branch_counts':dict(branches),
        'map_sha256':audit_digest.hexdigest(),
        'scalar_sha256':scalar_digest.hexdigest(),
        'chain_sha256':chain_digest.hexdigest(),
        'examples':examples,
        'chain_accounts':chain_accounts,
        'trace_prefix':trace_prefix,
        'negative_controls':3,
        'same_author_arithmetic_crosscheck':True,
        'independent_authorship':False,
        'sharp_payer_account_in_declared_class':6,
    }
    print(json.dumps(report,sort_keys=True,separators=(',',':'),ensure_ascii=True))


if __name__ == '__main__':
    main()
