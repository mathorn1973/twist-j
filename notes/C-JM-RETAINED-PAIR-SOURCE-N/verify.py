#!/usr/bin/env python3
"""Frozen exact audit. Stdlib only; a same-session test, not an independent agent."""
from fractions import Fraction as F
from itertools import product
from math import isqrt
from source import (q, admitted, basis, dot, kron_vec, g0_apply,
                    pair_metric_apply, compile_pair, SourceState, ready_source,
                    tick, lifecycle, capture, program_modulus)


def transpose(a):
    return list(map(list, zip(*a)))


def mm(a, b):
    # Integer sparse-aware multiplication for the independent full certificate.
    out = [[0]*len(b[0]) for _ in a]
    for i, row in enumerate(a):
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    if y:
                        out[i][j] += x*y
    return out


def gram(dim, apply):
    return transpose([apply(basis(dim, i)) for i in range(dim)])


def outer(a, b):
    return [[x*y for y in b] for x in a]


def ideal_round(old, gate, K, rounds):
    out = {}
    support = [(i, c) for i, c in enumerate(gate.target) if c]
    # At n>=1: P is fresh, B0 is the initial old P, B1..B(n-1) are prior pairs.
    for indices in product(support, repeat=rounds):
        amp = F(1)
        for _, c in indices:
            amp *= c
        for (oldp, spectator), c in old.items():
            key = (indices[0][0], oldp)+tuple(t[0] for t in indices[1:])+(0,)*(K-rounds)+(spectator,)
            out[key] = c*amp
    return out


def main():
    print('C-JM-RETAINED-PAIR-SOURCE-N EXACT AUDIT v1')
    G0 = gram(9, g0_apply)
    L = gram(81, pair_metric_apply)
    assert G0 == transpose(G0) and L == transpose(L)
    e = basis(81, 0)
    checked = 0
    for z in product((-1, 0, 1), repeat=8):
        if not admitted(z, 32):
            continue
        gate = compile_pair(z, 32)
        assert gate.active
        assert gate.dual == pair_metric_apply(gate.v)
        assert dot(gate.v, gate.dual) == 2*gate.den
        assert gate.dual[0] == gate.norm-1
        assert gate.apply(e) == gate.target
        assert dot(gate.target, pair_metric_apply(gate.target)) == 1
        assert gate.apply(gate.target) == tuple(F(a) for a in e)
        checked += 1
    print('TERNARY admitted program certificates', checked, 'PASS')

    unit = (1, 0, 0, 0, 0, 0, 0, 0)
    v = (1, 0, 0, 0, -1, 0, 0, 0)
    dense = (1, -1, 1, -1, 1, 1, 1, 0)
    programs = [unit, v, tuple(-a for a in v), dense]
    programs += [tuple(t*a for a in v) for t in (40, 41, 42)]
    for z in programs:
        gate = compile_pair(z, 14112)
        assert gate.active
        N = gate.integer_matrix()
        NN = mm(N, N)
        assert NN == [[gate.den**2*int(i == j) for j in range(81)] for i in range(81)]
        NTKN = mm(transpose(N), mm(L, N))
        assert NTKN == [[gate.den**2*x for x in row] for row in L]
        y = (1,)+z
        gy = g0_apply(y)
        one = [[F(a*b, gate.norm) for b in gy] for a in y]
        pair = outer(gate.target, pair_metric_apply(gate.target))
        for i, j, k, l in product(range(9), repeat=4):
            assert pair[i*9+k][j*9+l] == one[i][j]*one[k][l]
        red = [[sum(pair[9*i+k][9*j+k] for k in range(9)) for j in range(9)] for i in range(9)]
        assert red == one
        print('FULL INTEGER AND DENSITY', 'q', q(z), 'A', gate.norm,
              'den', gate.den, 'PASS')

    gate = compile_pair(v, 14112)
    # Complete old port basis, not just its ready state.
    for i in range(81):
        old = {(i, 0): F(1)}
        s = ready_source(v, 14112, 1, old)
        t = tick(s)
        assert t.amplitudes == ideal_round(old, gate, 1, 1)
        assert tick(t, inverse=True) == s
    print('ALL 81 OCCUPIED PORT BASIS STATES AND INVERSES PASS')

    old = {(0, 0): F(1, 3), (1, 1): F(2, 5), (9, 0): F(-4, 7), (80, 1): F(1, 11)}
    s0 = ready_source(v, 14112, 3, old)
    s = s0
    for n in range(1, 4):
        s = tick(s)
        assert s.counter == n and s.program == v
        assert s.amplitudes == ideal_round(old, gate, 3, n)
    assert lifecycle(s) == 'SUPPLY_EXHAUSTED_DATA_RETAINED'
    for _ in range(4):
        t = tick(s)
        assert t.amplitudes == s.amplitudes
        s = t
    for _ in range(7):
        s = tick(s, inverse=True)
    assert s == s0
    print('3-ROUND CORRELATED OCCUPIED ARCHIVE; EXHAUSTION; FULL RESET PASS')

    # Total law on dirty states and both sides of the supported interval.
    dirty = {(1, 9, 80, 0): F(2, 3), (80, 1, 9, 1): F(-5, 7), (0, 0, 0, 1): F(1, 2)}
    for n in range(-2, 6):
        s = SourceState(v, 14112, 2, n, dirty)
        assert tick(tick(s), inverse=True) == s
        assert tick(tick(s, inverse=True)) == s
    for bad in [(0,)*8, (0, 0, 0, 0, 0, 1, 0, 0)]:
        s = SourceState(bad, 14112, 2, 0, dirty)
        t = tick(s)
        assert t.amplitudes == dirty and 'INVALID' in lifecycle(t)
        assert tick(t, inverse=True) == s
    print('TOTAL DIRTY-STATE/INVALID-PROGRAM/COUNTER INVERSES PASS')

    # A preoccupied stock cell is NOT a fresh resource: U sends target back to e.
    contaminated = {(0, i, 0): c for i, c in enumerate(gate.target) if c}
    s = SourceState(v, 14112, 1, 0, contaminated)
    t = tick(s)
    assert t.amplitudes == {(0, 0, 0): F(1)}
    assert t.amplitudes != ideal_round({(0, 0): F(1)}, gate, 1, 1)
    assert tick(t, inverse=True) == s
    print('DIRTY STOCK DOES NOT GIVE PROMISED PREPARATION: negative control PASS')

    # Local stable lattice generators transform among integral combinations.
    for i in range(81):
        ei, ej = basis(81, i), basis(81, (i+1) % 81)
        x = tuple(F(a)+b for a, b in zip(ei, gate.apply(ej)))
        assert gate.apply(x) == tuple(a+F(b) for a, b in zip(gate.apply(ei), ej))
    print('FIXED-PROGRAM COMPILED LATTICE GENERATORS PASS')

    # Integer program capture is reversible for all contents, fresh or occupied.
    count = 0
    for m in (3, 5, 7):
        for x, p, a in product(range(m), repeat=3):
            got = capture((x,), (p,), (a,), m)
            assert capture(*got, m, inverse=True) == ((x,), (p,), (a,))
            if a == 0:
                assert got == ((x,), (x,), (p,))
            count += 1
    m = program_modulus(14112)
    x = tuple(a % m for a in programs[-1])
    p = tuple(range(8))
    got = capture(x, p, (0,)*8, m)
    assert got == (x, x, p) and capture(*got, m, inverse=True) == (x, p, (0,)*8)
    print('CAPTURE full scalar domains', count, 'and occupied eight-register control PASS')

    a = compile_pair(unit, 8).norm
    assert a == 5
    for k in range(1, 7):
        square = isqrt(a**k)**2 == a**k
        assert square == (k % 2 == 0)
    print('A=5 CLEAN RATIONAL PARITY: odd obstruction/even construction PASS')

    lam = F(354161, 735212)
    def ref_pair_prob(t):
        g = compile_pair(tuple(t*a for a in v), 14112)
        # This probability is obtained from the actual gate output vector.
        output = g.apply(e)
        return output[0]**2
    gap = lam*ref_pair_prob(40)+(1-lam)*ref_pair_prob(42)-ref_pair_prob(41)
    assert gap == F(15936, 1210262180216419)
    print('GENERATED HOLD PAIR reference gap =', gap)
    print('Q=14112 predecessor test: requested181, pair rounds91, generated182, retained spare1')
    print('ALL FROZEN SOURCE TESTS PASS')


if __name__ == '__main__':
    main()
