#!/usr/bin/env python3
"""Prospectively pinned exact audit; NON-CANONICAL, L1, standard library only."""
from __future__ import annotations
import hashlib
import itertools
import json
from fractions import Fraction
from decoder import InvalidReading, apply_steps, decode, inverse_step, norm, reading, step, trace_pair, uv


def census(strip):
    groups = {}
    groups25 = {}
    pairs = set()
    for a in strip:
        s = trace_pair(a)
        pairs.add(s)
        for modulus, target in ((5, groups), (25, groups25)):
            key = s + tuple(x % modulus for x in a)
            target.setdefault(key, []).append(a)
    first = min((norm(g[0]), key, g[0], g[1])
                for key, g in groups.items() if len(g) > 1)
    return {
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


def must_reject(s0, s1, residue):
    try:
        decode(s0, s1, residue)
    except InvalidReading:
        return
    raise AssertionError(('invalid input accepted', s0, s1, residue))


def main():
    basis = [tuple(int(i == j) for i in range(4)) for j in range(4)]
    for x in basis:
        assert step(inverse_step(x)) == inverse_step(step(x)) == x
    G = [[5*int(i == j)-1 for j in range(4)] for i in range(4)]
    GI = [[Fraction(1+int(i == j), 5) for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            assert sum(G[i][k]*GI[k][j] for k in range(4)) == int(i == j)
    assert 2*(-1)-3*1 == -5
    assert 16*941 < 25**4 and 9*941 < 93**2 and Fraction(4*92, 5) < 81
    strip = []
    scanned = 0
    for a in itertools.product(range(-8, 9), repeat=4):
        scanned += 1
        u, v = uv(a)
        s0, s1 = trace_pair(a)
        sa = step(a)
        gram0 = 5*sum(x*x for x in a) - sum(a)**2
        gram1 = 5*sum(x*x for x in sa) - sum(sa)**2
        assert gram0 == 2*s0 and gram1 == 2*s1
        assert (s0+s1) % 5 == 0
        assert ((s0+s1)//5, (3*s0-2*s1)//5) == (u,v)
        assert trace_pair(sa) == (s1, 3*s1-s0)
        assert 5*norm(a) == 3*s0*s1-s0*s0-s1*s1
        assert norm(sa) == norm(a)
        assert (v >= 0 and u-v > 0) == (2*s0 < 3*s1 and 2*s1 <= 3*s0)
        if v >= 0 and u-v > 0 and 1 <= norm(a) <= 941:
            assert s0 <= 92 and all(5*x*x <= 4*s0 for x in a)
            strip.append(a)
    strip.sort()
    summary = census(strip)
    assert summary['strip_count'] == 3150
    assert summary['strip_below'] == 3110
    assert summary['mod25_key_count'] == 3150
    roundtrips = 0
    for beta in strip:
        alpha = apply_steps(beta, -16)
        for k in range(-16, 17):
            out = decode(*reading(alpha))
            assert out.coefficients == alpha
            assert out.unit_exponent == k
            assert out.strip_coefficients == beta
            assert out.norm == norm(beta)
            roundtrips += 1
            alpha = step(alpha)
    stress = 0
    for beta in strip[:10]:
        for k in (-1024, -257, 257, 1024):
            alpha = apply_steps(beta, k)
            out = decode(*reading(alpha))
            assert (out.coefficients, out.unit_exponent, out.strip_coefficients) == (alpha,k,beta)
            stress += 1
    one = (1,0,0,0)
    root = (0,1,0,0)
    assert trace_pair(one) == trace_pair(root) == (2,3)
    assert decode(*reading(one)).unit_exponent == 0
    inv = inverse_step(one)
    assert trace_pair(inv) == (3,2)
    assert decode(*reading(inv)).unit_exponent == -1
    five, five_root = (5,0,0,0), (0,5,0,0)
    assert reading(five,5) == reading(five_root,5) == (50,75,(0,0,0,0))
    assert norm(five) == norm(five_root) == 625 and five != five_root
    assert reading(five) != reading(five_root)
    for x in (five,five_root):
        assert decode(*reading(x)).coefficients == x
    invalid = [
        (0,0,(0,0,0,0)), (-2,-3,(1,0,0,0)), (2,2,(1,0,0,0)),
        (1,4,(1,0,0,0)), (72,108,(6,0,0,0)), (True,3,(1,0,0,0)),
        (2,'3',(1,0,0,0)), (2,3,(1,0,0)), (2,3,(25,0,0,0)),
        (2,3,(-1,0,0,0)), (2,3,(0,0,0,0)), (2,3,(2,0,0,0)),
    ]
    for args in invalid:
        must_reject(*args)
    # A source insertion is not the stipulated pure-J observation.
    written = tuple(x+y for x,y in zip(step(one),one))
    must_reject(trace_pair(one)[0], trace_pair(written)[0], one)
    # A different VALID residue with the same traces must remain admissible.
    assert decode(2,3,root).coefficients == root
    print('TWIST-J two-trace residue decoder audit; NON-CANONICAL L1')
    print('CENSUS ' + json.dumps(summary, sort_keys=True, separators=(',', ':')))
    print(f'PASS complete_box={scanned} exact_roundtrips={roundtrips} stress_roundtrips={stress}')
    print(f'PASS invalid_readings={len(invalid)} affine_control=1 half_open_boundaries=2')
    print('PASS mod5_collision_preserved=1 valid_to_valid_corruption_control=1')
    print('RESULT PASS; finite audit candidate-C, universal derivations candidate-T pending review')


if __name__ == '__main__':
    main()
