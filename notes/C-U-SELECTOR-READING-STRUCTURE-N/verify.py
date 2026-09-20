#!/usr/bin/env python3
"""Exact audit of the preregistered structural proof, not a formal probe."""
from collections import Counter
from itertools import product


def verb(i, x):
    p, s, P, S, q, r = x
    rows = (
        (s, p, S, P, q, r),
        (-P, -S, -p, -s, -q, -r),
        (-P+2, -S+1+r, -p+2, -s+1-r, 1-q, -r),
        (2-p, 1-s, 3-P, 4-S, 1-q, 1-r),
        (2-p, 1-s, 3-P, 4-S, 2-q, 1-r),
    )
    return tuple(a % 5 for a in rows[i])


def trace(x):
    return sum(x) % 5


def edge(t, x):
    return verb((trace(x)+2*t) % 5, x)


def kappa(x):
    p, s, P, S, q, r = x
    a, b = (p+s+P+S) % 5, (p+s-P-S-3) % 5
    z = trace(x)
    if z == 0:
        return ((a-1) % 5, (-b-2*r) % 5)
    return (a, b if z in (1, 2) else -b % 5)


def neg(v):
    return tuple(-a % 5 for a in v)


def signclass(v):
    return min(v, neg(v))


def terminal(x):
    p, s, P, S, q, r = x
    z = trace(x)
    assert z in (1, 4)
    chi = 1 if z == 1 else -1
    return ((p+P) % 5, (s+S) % 5,
            chi*(p-P-2) % 5, chi*(s-S-1) % 5)


def path(x, letters, phases):
    assert trace(x) == phases[0]
    for i, (a, b) in zip(letters, zip(phases, phases[1:])):
        y = verb(i, x)
        assert trace(y) == b
        assert (i-a) % 5 in (0, 2) or (i-b) % 5 in (0, 2)
        x = y
    return x


def normalized(v):
    pivot = next(a for a in v if a)
    return tuple(a * pow(pivot, -1, 5) % 5 for a in v)


def main():
    states = tuple(product(range(5), repeat=6))
    fibres, sheet, orbit = Counter(), Counter(), Counter()
    trace_tables = ((0, 4, 0, 4, 4), (2, 1, 1, 3, 1))
    for x in states:
        z, v = trace(x), kappa(x)
        fibres[v] += 1
        sheet[z, v] += 1
        orbit[signclass(v)] += 1
        for i, expect in enumerate((z, -z, 2-z, 2-z, 3-z)):
            assert trace(verb(i, x)) == expect % 5
            assert verb(i, verb(i, x)) == x
        for t in (0, 1):
            i = (z+2*t) % 5
            y = edge(t, x)
            assert trace(y) == trace_tables[t][z]
            assert kappa(y) == (v if i == 0 else neg(v))
        y = x
        for t in (0, 1, 1):
            y = edge(t, y)
        assert trace(y) == 1
        if z == 0:
            assert trace(path(x, (2, 4), (0, 2, 1))) == 1
        elif z == 2:
            assert trace(path(x, (4,), (2, 1))) == 1
        elif z == 3:
            assert trace(path(x, (3,), (3, 4))) == 4
        elif z == 4:
            a, b, c, d = terminal(x)
            y = path(x, (3, 0, 3), (4, 3, 3, 4))
            assert terminal(y) == (b, a, (d-1) % 5, (c+1) % 5)
        elif z == 1:
            a, b, c, d = terminal(x)
            k = (2*x[-1]-1) % 5
            y = path(x, (4, 2, 0, 2, 4), (1, 2, 0, 0, 2, 1))
            assert terminal(y) == ((b+3) % 5, (a-3) % 5,
                                   (d+k) % 5, (c-k) % 5)
    assert len(fibres) == 25 and set(fibres.values()) == {625}
    assert len(sheet) == 125 and set(sheet.values()) == {125}
    assert len(orbit) == 13 and Counter(orbit.values()) == {625: 1, 1250: 12}
    print('PASS native trace and involution identities: 78125 cases')
    print('PASS oriented invariant on every selected edge: 31250 cases')
    print('PASS fibres: 25 oriented; 13 sign classes; 625:1,1250:12')
    print('PASS each oriented fibre on each trace sheet: 125 states')
    print('PASS transient paths and H/G formulas: all 15625 states')
    for v in product(range(5), repeat=4):
        a, b, c, d = v
        for k in range(5):
            h = (b, a, (d-1) % 5, (c+1) % 5)
            gh = ((h[1]+3) % 5, (h[0]-3) % 5,
                  (h[3]+k) % 5, (h[2]-k) % 5)
            assert gh == ((a+3) % 5, (b-3) % 5,
                          (c+k+1) % 5, (d-k-1) % 5)
    translations = {((3*a) % 5, (-3*a) % 5, b, -b % 5)
                    for a, b in product(range(5), repeat=2)}
    assert len(translations) == 25
    assert translations == {v for v in product(range(5), repeat=4)
                            if (v[0]+v[1]) % 5 == (v[2]+v[3]) % 5 == 0}
    print('PASS transient translations: exact two-dimensional sum kernel')
    quadratic = {}
    for u, v in product(range(5), repeat=2):
        m = (u*u % 5, u*v % 5, v*v % 5)
        cls = signclass((u, v))
        assert m not in quadratic or quadratic[m] == cls
        quadratic[m] = cls
    assert len(quadratic) == len(set(quadratic.values())) == 13
    directions = Counter(normalized(m) for m in quadratic if any(m))
    assert len(directions) == 6 and set(directions.values()) == {2}
    assert sum((a*c-b*b) % 5 == 0
               for a, b, c in product(range(5), repeat=3)) == 25
    print('PASS quadratic record: 13 matrices; 6 directions each with 2 values')
    print('PASS cone guard: quadratic image 13 differs from full null cone 25')
    for z in range(5):
        assert trace_tables[1][trace_tables[1][trace_tables[0][z]]] == 1
    assert all(trace_tables[t][z] == (4-3*t) % 5
               for z in (1, 4) for t in (0, 1))
    for z, t in product(range(5), (0, 1)):
        chosen = tuple(int(i == (z+2*t) % 5) for i in range(5))
        summed = tuple(int(i == z)+int(i == (z+2) % 5) for i in range(5))
        assert sum(chosen) == 1 and sum(summed) == 2
        diff = tuple(a-b for a, b in zip(summed, chosen))
        assert len(set(diff)) != 1
    print('PASS trace reset: all heads at n=3 have trace/index 1')
    print('PASS selector versus branch sum: 1 versus 2, also unequal modulo constants')
    print('RESULT candidate audit PASS; no native Hodge amplitude selection')


if __name__ == '__main__':
    main()
