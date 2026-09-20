#!/usr/bin/env python3
"""Exact finite audits of the frozen counter-amplitude proof contract.

All-clock and arbitrary-target conclusions are proved in PROOF.md.  The
finite clock ranges below are audits of those formulas, not extrapolations.
"""
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


def structural_audit():
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
    assert (2, 0, 0) not in quadratic
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
    return states


def theta(n):
    return n.bit_count() % 2


def s0(m):
    """Exact alternating-floor sum, implemented by its defining recurrence."""
    if m == 0:
        return 0
    return m - s0(m // 2)


def clock(n):
    assert n >= 3
    t = 1 if (n-3) % 2 == 0 else -1
    h = 1 if (n+theta(n-1)) % 2 == 0 else -1
    return t, h, s0((n-1) // 2)-1


def chart(n, x):
    t, h, shift = clock(n)
    p, s, P, S, q, r = x
    return (t*(p+P) % 5, t*(s+S) % 5,
            h*(p-P-2) % 5, h*(s-S-1) % 5, (t*r-shift) % 5)


def unchart(n, label):
    t, h, shift = clock(n)
    alpha, beta, gamma, delta, epsilon = label
    a, b, c, d = t*alpha, t*beta, h*gamma, h*delta
    r = t*(epsilon+shift)
    q = 4-3*theta(n-1)-a-b-r
    return tuple(value % 5 for value in
                 (3*(a+c+2), 3*(b+d+1), 3*(a-c-2),
                  3*(b-d-1), q, r))


def label_at(n, x):
    """The proof's ell_n; only called on origin-zero reachable checkpoints."""
    while n < 3:
        x = edge(theta(n), x)
        n += 1
    return chart(n, x)


def qbar(label):
    a, b, c, d, epsilon = label
    return signclass(((a+b) % 5, (c+d) % 5))


def clock_audit():
    switches = 0
    assert s0(0) == 0
    for m in range(1, 4097):
        switches += int(theta(m) != theta(m-1))
        assert s0(m) == switches
        assert s0(m) == m-s0(m // 2)
    for n in range(3, 4096):
        t, h, shift = clock(n)
        next_t, next_h, next_shift = clock(n+1)
        same = int(theta(n) == theta(n-1))
        assert next_t == -t
        assert next_h == (-1 if same else 1)*h
        assert next_shift-shift == -t*same
        if n % 2:
            assert same == 0
        else:
            assert same == int(theta(n // 2) != theta(n // 2-1))
    print('PASS clock identities: n=3..4095; switch-count recurrence m=0..4096')


def chart_audit(states):
    labels = tuple(product(range(5), repeat=5))
    label_set = set(labels)
    initial_labels = tuple(label_at(0, x) for x in states)
    initial_counts = Counter(initial_labels)
    assert set(initial_counts) == label_set
    assert set(initial_counts.values()) == {5}
    pairs = {(label, trace(x)) for x, label in zip(states, initial_labels)}
    assert len(pairs) == 15625
    assert pairs == {(label, z) for label in labels for z in range(5)}
    print('PASS E3 labels: 3125 fibres, five heads and all five phases each')
    print('PASS head decomposition: (ell_0,initial phase) is a 15625-pair bijection')

    quotient_counts = Counter(qbar(label) for label in labels)
    assert len(quotient_counts) == 13
    assert Counter(quotient_counts.values()) == {125: 1, 250: 12}
    assert quotient_counts[(0, 0)] == 125

    current = states
    for n in range(32):
        observed_labels = Counter()
        for x, label in zip(current, initial_labels):
            assert label_at(n, x) == label
            assert signclass(kappa(x)) == qbar(label)
            observed_labels[label] += 1
        assert observed_labels == initial_counts
        if n >= 3:
            reachable_counts = Counter(current)
            assert len(reachable_counts) == 3125
            assert set(reachable_counts.values()) == {5}
            phase = (4-3*theta(n-1)) % 5
            assert all(trace(x) == phase for x in reachable_counts)
            assert set(reachable_counts) == {unchart(n, label) for label in labels}
            for x in reachable_counts:
                label = chart(n, x)
                assert unchart(n, label) == x
                t, h, shift = clock(n)
                assert kappa(x) == (t*(label[0]+label[1]) % 5,
                                    t*(label[2]+label[3]) % 5)
            for label in labels:
                assert chart(n, unchart(n, label)) == label
        if n < 31:
            current = tuple(edge(theta(n), x) for x in current)
    print('PASS conserved labels and Q=qbar(ell_n): all 15625 heads, n=0..31')
    print('PASS reachable chart and both inverse identities: n=3..31, 3125 states each')
    print('PASS chart quotient: 13 fibres; 125:1,250:12')

    zero = (0, 0, 0, 0, 0)
    one = (0, 0, 0, 0, 1)
    assert zero != one and qbar(zero) == qbar(one) == (0, 0)
    x, y = unchart(3, zero), unchart(3, one)
    assert x != y and chart(3, x) == zero and chart(3, y) == one
    assert signclass(kappa(x)) == signclass(kappa(y))
    assert chart(3, x)[4] == 0 and chart(3, y)[4] == 1
    print('PASS strict subclass witness: equal Q, distinct retained epsilon labels')


def main():
    states = structural_audit()
    clock_audit()
    chart_audit(states)
    print('RESULT COUNTER-AMPLITUDE-CLASS PASS; target L and assignment G remain inputs')


if __name__ == '__main__':
    main()
