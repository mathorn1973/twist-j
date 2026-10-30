#!/usr/bin/env python3
"""Exact local note audit. No formal public gate or independent review."""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from math import lcm


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def sub(x, y):
    return x[0] - y[0], x[1] - y[1]


def mul(x, y):
    a, b = x
    c, d = y
    return a*c + b*d, a*d + b*c + b*d


def bar(x):
    return x[0] + x[1], -x[1]


def norm(x):
    a, b = x
    return a*a + a*b - b*b


def trace(x):
    return 2*x[0] + x[1]


def positive(x):
    return trace(x) > 0 and norm(x) > 0


def fracdiv(x, y):
    n = mul(x, bar(y))
    d = norm(y)
    if d == 0:
        raise ZeroDivisionError('zero field denominator')
    return Q(n[0])/d, Q(n[1])/d


def beta(pair):
    (a, b), (c, d) = pair
    return b*c-a*d


@lru_cache(maxsize=None)
def profile(pair):
    x, y = pair
    z = add(x, y)
    T = norm(z)
    if not positive(x) or not positive(y):
        raise ValueError('both states must have two positive embeddings')
    n = mul(mul(z, z), bar(x))
    admitted = n[0] % T == n[1] % T == 0
    if admitted:
        rx = (n[0]//T, n[1]//T)
        reflected = rx, sub(z, rx)
    else:
        reflected = pair
    return beta(pair), admitted, reflected


def C(pair):
    return profile(pair)[2]


def theta(state):
    q, pair = state
    return q, (bar(pair[0]), bar(pair[1]))


def step(state, kappa=1):
    q, pair = state
    if q % 2 != 1 or kappa not in (0, 1):
        raise ValueError('odd position and binary fixed law required')
    b, admitted, reflected = profile(pair)
    trial = q+2*b
    if kappa and admitted and q*trial < 0:
        return -trial, reflected
    return trial, pair


def inverse(state, kappa=1):
    return theta(step(theta(state), kappa))


def naive(state):
    q, pair = state
    b, admitted, reflected = profile(pair)
    trial = q+2*b
    return trial, reflected if admitted and q*trial < 0 else pair


def record_gate(pair, h):
    b, admitted, reflected = profile(pair)
    return reflected, h ^ int(admitted and b != 0)


def main():
    box = [(a, b) for a in range(1, 9) for b in range(-8, 9)
           if positive((a, b))]
    pairs = [(x, y) for x in box for y in box]
    for pair in pairs:
        x, y = pair
        z = add(x, y)
        r, s, T = norm(x), norm(y), norm(z)
        D = T+r-s
        b, admitted, reflected = profile(pair)
        w = mul(x, bar(z))
        wu = mul(sub(x, y), bar(z))
        assert trace(w) == D and w[1] == b
        assert wu == (r-s-b, 2*b)
        assert D*D-4*T*r == 5*b*b
        assert Q(x[1], trace(x))-Q(y[1], trace(y)) == Q(2*b, trace(x)*trace(y))
        # Relative speeds in COM have sqrt(5) factored out.
        assert Q(b, D)+Q(b, 2*T-D) == Q(2*T*b, D*(2*T-D))
        raw = fracdiv(mul(z, bar(x)), bar(z))
        assert admitted == all(v.denominator == 1 for v in raw)
        assert C(C(pair)) == pair
        assert profile(C(pair))[1] == admitted
        reversed_pair = (bar(x), bar(y))
        assert beta(reversed_pair) == -b
        assert profile(reversed_pair)[1] == admitted
        assert C(reversed_pair) == tuple(map(bar, C(pair)))
        if admitted:
            assert tuple(map(Q, reflected[0])) == raw
            assert beta(reflected) == -b
        for h in (0, 1):
            p2, h2 = record_gate(pair, h)
            assert record_gate(p2, h2) == (pair, h)
    print(f'G1 PASS positive_inputs={len(box)} ordered_pairs={len(pairs)} exact_relative_and_guard_identities=all')
    positions = list(range(-31, 32, 2))
    samples = 0
    per_law = []
    for kappa in (0, 1):
        seen = set()
        counts = defaultdict(int)
        for pair in pairs:
            x, y = pair
            b, admitted, _ = profile(pair)
            for q in positions:
                state = q, pair
                out = step(state, kappa)
                assert inverse(out, kappa) == state
                assert step(inverse(state, kappa), kappa) == state
                assert out[0] % 2 == 1
                assert add(*out[1]) == add(x, y)
                assert tuple(map(norm, out[1])) == (norm(x), norm(y))
                assert all(positive(t) for t in out[1])
                assert out not in seen, ('two sampled preimages', kappa, state, out)
                seen.add(out)
                cross = q*(q+2*b) < 0
                bounce = bool(kappa and admitted and cross)
                if bounce:
                    lam = Q(-q, 2*b)
                    assert 0 < lam < 1
                    assert Q(out[0]) == (-2*b)*(1-lam)
                    assert q*out[0] > 0 and out[0]*beta(out[1]) > 0
                    counts['reflections'] += 1
                else:
                    assert out == (q+2*b, pair)
                    counts['transmissions'] += int(cross)
                if cross:
                    # Once moving away, another crossing is impossible.
                    assert out[0]*beta(out[1]) > 0
                    again = step(out, kappa)
                    assert again[1] == out[1]
                    assert abs(again[0]) > abs(out[0])
                samples += 1
        per_law.append((kappa, len(seen), counts['reflections'], counts['transmissions']))
    print(f'G2 PASS sampled_states_both_laws={samples} inverse_both_orders=yes exact_residuals=yes')
    for k, n, bounce, transmit in per_law:
        print(f'LAW {k} injective_sample={n} reflections={bounce} transmissions={transmit}')
    splus = ((1, 1), (1, 0))
    sminus = ((1, 0), (1, 1))
    assert beta(splus) == 1 and beta(sminus) == -1
    a, b = (-1, splus), (3, sminus)
    assert a != b and naive(a) == naive(b) == (1, sminus)
    assert step(a) != step(b)
    assert step(a) == (-1, sminus)
    print('G3 PASS naive_crossing_noninjective_witness=retained corrected_outputs=distinct')
    for M in range(1, 65):
        p1 = ((1, 0), (1, 1))
        p2 = ((1, 0), (1+M, 1+M))
        assert all(a % M == b % M for x, y in zip(p1, p2) for a, b in zip(x, y))
        assert profile(p1)[1] and not profile(p2)[1]
    print('G4 PASS fixed_modulus_negative_controls=64 variable_modulus_guard=exact')
    pi11, pi19 = (3, 2), (4, 3)
    assert norm(pi11) == 11 and norm(pi19) == 19
    assert mul(pi11, pi19) == (18, 23)
    assert mul(pi11, bar(pi19)) == (15, -1)
    wp, wm = mul(bar(pi11), pi19), mul(pi11, bar(pi19))
    assert (wp, wm) == ((14, 1), (15, -1))
    zp = bar((18, 23))
    assert fracdiv(wp, zp) == (Q(25, 19), Q(33, 19))
    assert fracdiv(wm, zp) == (Q(13, 11), Q(16, 11))
    print('G5 PASS 209_oriented_factorizations=exact roots_wplus_wminus_denominators=19,11')
    z = (3, 2)
    fibre = set()
    for a in range(1, z[0]):
        for b in range(-2*a+1, 2*a):
            x = (a, b)
            if positive(x) and positive(sub(z, x)):
                fibre.add((x, sub(z, x)))
    expected = {((1, 0), (2, 2)), ((1, 1), (2, 1)),
                ((2, 1), (1, 1)), ((2, 2), (1, 0))}
    assert fibre == expected
    start, finish = ((1, 0), (2, 2)), ((1, 1), (2, 1))
    assert tuple(map(norm, start)) == (1, 4)
    assert tuple(map(norm, finish)) == (1, 5)
    assert beta(start) == -2 and beta(finish) == 1
    assert not profile(start)[1]
    for q, target in [(1, Q(3, 2)), (3, Q(1, 2))]:
        lam = Q(-q, 2*beta(start))
        qout = 2*beta(finish)*(1-lam)
        assert qout == target and qout.denominator != 1
    def cm_velocity_without_sqrt5(pair):
        x, y = pair
        T, r, s = norm(add(x, y)), norm(x), norm(y)
        D = T+r-s
        return Q(2*T*beta(pair), D*(2*T-D))
    assert cm_velocity_without_sqrt5(start) == Q(-11, 28)
    assert cm_velocity_without_sqrt5(finish) == Q(22, 105)
    assert cm_velocity_without_sqrt5(finish)/cm_velocity_without_sqrt5(start) == Q(-8, 15)
    print('G6 PASS complete_z_3_2_fibre=4 inelastic_1_4_to_1_5=yes beta_stream_residual=3/2 physical_speed_ratio=-8/15')
    print('STATUS NON-CANONICAL candidate-C audit; analytical proofs candidate-T; single x86_64 lane')


if __name__ == '__main__':
    main()
