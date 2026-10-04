#!/usr/bin/env python3
"""Frozen exact audit for P-J-LAMBDA6-DECODER-INTERFACE-1.

Scientific execution is permitted only after the public preregistration pin.
This verifier uses an independent polynomial/lattice oracle. The separately
authored review verifier is frozen before exposure to this implementation.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
from itertools import product
import json
import sys

import decoder as target

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
ZETA = (0, 1, 0, 0)
LAMBDA = (1, -1, 0, 0)
J = (1, 0, 1, 0)
JINV = (0, -1, -1, 0)
EXPOSED_STRIP_DIGEST = '6a08d7de33b4cadb615f942b37202540dd6dea0f59f2412ffb822389c7c1cdab'


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def add(x, y):
    return tuple(a+b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a-b for a, b in zip(x, y))


def mul(x, y):
    coefficients = [0]*7
    for i in range(4):
        for j in range(4):
            coefficients[i+j] += x[i]*y[j]
    for i in range(6, 3, -1):
        for j in range(1, 5):
            coefficients[i-j] -= coefficients[i]
    return tuple(coefficients[:4])


def power(x, n):
    answer = ONE
    for _ in range(n):
        answer = mul(answer, x)
    return answer


def galois(x, k):
    answer = ZERO
    for i, c in enumerate(x):
        answer = add(answer, tuple(c*t for t in power(ZETA, (i*k) % 5)))
    return answer


def facts(x):
    squared = mul(x, galois(x, 4))
    u, v = squared[0], -squared[2]
    require(squared == (u, 0, -v, -v), 'real-subfield coordinates')
    n = mul(squared, galois(squared, 2))
    require(n[1:] == (0, 0, 0), 'integer norm')
    first = add(squared, galois(squared, 2))
    second_squared = mul(mul(J, x), galois(mul(J, x), 4))
    second = add(second_squared, galois(second_squared, 2))
    require(first[1:] == second[1:] == (0, 0, 0), 'integer traces')
    return u, v, n[0], (first[0], second[0])


def inverse_matrix(matrix):
    n = len(matrix)
    rows = [[Fraction(c) for c in row] +
            [Fraction(int(i == j)) for j in range(n)]
            for i, row in enumerate(matrix)]
    determinant = Fraction(1)
    for j in range(n):
        pivot = next(i for i in range(j, n) if rows[i][j])
        if pivot != j:
            rows[pivot], rows[j] = rows[j], rows[pivot]
            determinant *= -1
        value = rows[j][j]
        determinant *= value
        rows[j] = [c/value for c in rows[j]]
        for i in range(n):
            if i != j:
                value = rows[i][j]
                rows[i] = [a-value*b for a, b in zip(rows[i], rows[j])]
    return [row[n:] for row in rows], determinant


def reject(f, args, exception=ValueError):
    try:
        f(*args)
    except exception:
        return
    raise AssertionError('required rejection did not occur')


def main():
    require(not sys.flags.optimize, 'Python optimization is forbidden')
    require(mul(J, JINV) == ONE, 'J unit inverse')
    lam6 = power(LAMBDA, 6)
    basis = [tuple(int(i == j) for i in range(4)) for j in range(4)]
    columns = [mul(lam6, b) for b in basis]
    matrix = [list(row) for row in zip(*columns)]
    inverse, determinant = inverse_matrix(matrix)
    require(determinant == 15625, 'lambda-six ideal index')
    numerator = [[c*15625 for c in row] for row in inverse]
    require(all(c.denominator == 1 for row in numerator for c in row),
            'integer inverse numerator')
    numerator = [[int(c) for c in row] for row in numerator]
    for i in range(4):
        for j in range(4):
            require(sum(matrix[i][k]*inverse[k][j] for k in range(4)) == (i == j),
                    'right inverse identity')
            require(sum(inverse[i][k]*matrix[k][j] for k in range(4)) == (i == j),
                    'left inverse identity')

    def lattice_key(x):
        return tuple(sum(row[i]*x[i] for i in range(4)) % 15625 for row in numerator)

    # Independent ideal coordinates label equivalence classes. No author
    # digit conversion or division routine participates in this oracle.
    residues = list(product(range(5), repeat=6))
    representatives = {}
    lattice_to_digits = {}
    for r in residues:
        x = ZERO
        for c in reversed(r):
            x = add(mul(LAMBDA, x), (c, 0, 0, 0))
        key = lattice_key(x)
        require(key not in lattice_to_digits, 'canonical residue uniqueness')
        lattice_to_digits[key] = r
        representatives[r] = x
        require(target.residue_representative(r) == x, 'integral digit representative')
        require(target.residue_digits(x) == r, 'canonical digit round trip')
    require(len(lattice_to_digits) == 15625, 'complete residue system')
    require(lattice_key((5, 0, 0, 0)) != lattice_key(ZERO), '5 is nonzero')
    require(lattice_key((25, 0, 0, 0)) == lattice_key(ZERO), '25 is zero')

    oracle = {}
    strip = []
    uv_by_scalar = {}
    scalar_checks = 0
    # The complete original box is certified by the public strip proof.
    for x in product(range(-8, 9), repeat=4):
        squared = mul(x, galois(x, 4))
        u, v = squared[0], -squared[2]
        require(squared == (u, 0, -v, -v), 'box real-subfield identity')
        n = u*u+u*v-v*v
        if 0 <= v < u and 1 <= n <= 941:
            gu, gv, gn, traces = facts(x)
            require((gu, gv, gn) == (u, v, n), 'norm oracle agreement')
            r = lattice_to_digits[lattice_key(x)]
            reading = (*traces, r)
            require(reading not in oracle, 'lambda-six injectivity')
            oracle[reading] = x
            uv_by_scalar[x] = (u, v)
            strip.append(x)
            require(target.encode(x) == reading, 'encoder exactness')
            require(target.encode(list(x)) == reading, 'list scalar normalization')
            scalar_checks += 1
    strip_digest = hashlib.sha256(json.dumps(strip, separators=(',', ':')).encode()).hexdigest()
    require(len(strip) == 3150, 'original strip cardinality')
    require(strip_digest == EXPOSED_STRIP_DIGEST, 'original strip byte anchor')

    # Complete normalized well-formed inputs that survive positive-norm
    # checks. The exact strip inequality proves u<=46 before representability.
    normalized_pairs = [(u, v) for u in range(1, 47) for v in range(u)
                        if 1 <= u*u+u*v-v*v <= 941]
    accepted = rejected = 0
    for u, v in normalized_pairs:
        s0, s1 = 2*u+v, 3*u-v
        require(s0 <= 92, 'normalized arithmetic range')
        for r in residues:
            key = (s0, s1, r)
            x = oracle.get(key)
            if x is None:
                reject(target.decode, key, target.InvalidReading)
                rejected += 1
            else:
                result = target.decode(*key)
                require((result.coefficients, result.strip_coefficients,
                         result.unit_exponent, result.norm) ==
                        (x, x, 0, u*u+u*v-v*v), 'normalized complete inverse')
                accepted += 1
    require(accepted == 3150 and rejected > 0, 'complete image recognition')
    represented_pairs = {uv_by_scalar[x] for x in strip}
    require(set(normalized_pairs) - represented_pairs, 'nonrepresentable trace classes covered')

    translated_invalid = 0
    for u, v in normalized_pairs:
        base_traces = (2*u+v, 3*u-v)
        missing = next(r for r in residues if (*base_traces, r) not in oracle)
        for exponent in (-31, 31):
            s0, s1 = base_traces
            for _ in range(abs(exponent)):
                s0, s1 = ((s1, 3*s1-s0) if exponent > 0 else (3*s0-s1, s0))
            unit = power(J if exponent > 0 else JINV, abs(exponent))
            r = lattice_to_digits[lattice_key(mul(unit, representatives[missing]))]
            reject(target.decode, (s0, s1, r), target.InvalidReading)
            translated_invalid += 1

    transitions = 0
    for r in residues:
        x = representatives[r]
        expected_next = lattice_to_digits[lattice_key(mul(J, x))]
        expected_previous = lattice_to_digits[lattice_key(mul(JINV, x))]
        for s0, s1 in ((-2, 7), (0, 0), (2, 3)):
            data = (s0, s1, r)
            forward = target.T6(*data)
            backward = target.T6_inverse(*data)
            require(forward == (s1, 3*s1-s0, expected_next), 'forward data operator')
            require(backward == (3*s0-s1, s0, expected_previous), 'backward data operator')
            require(target.T6_inverse(*forward) == target.T6(*backward) == data,
                    'both data inverse compositions')
            transitions += 1

    translated = boundary = 0
    exponent_set = (-31, -7, -1, 0, 1, 7, 31)
    for beta in strip:
        for exponent in exponent_set:
            multiplier = power(J if exponent >= 0 else JINV, abs(exponent))
            alpha = mul(multiplier, beta)
            _, _, n, traces = facts(alpha)
            data = (*traces, lattice_to_digits[lattice_key(alpha)])
            require(target.encode(alpha) == data, 'translated encoder')
            result = target.decode(*data)
            require((result.coefficients, result.strip_coefficients,
                     result.unit_exponent, result.norm) ==
                    (alpha, beta, exponent, n), 'all-strip signed normalization')
            require(target.T6(*data) == target.encode(mul(J, alpha)), 'forward intertwining')
            require(target.T6_inverse(*data) == target.encode(mul(JINV, alpha)),
                    'inverse intertwining')
            translated += 1
        if uv_by_scalar[beta][1] == 0:
            upper = mul(JINV, beta)
            uu, vv, _, _ = facts(upper)
            require(uu == vv, 'excluded upper boundary')
            require(target.decode(*target.encode(upper)).unit_exponent == -1,
                    'upper boundary moves into included lower boundary')
            boundary += 1
    require(boundary > 0, 'both exact endpoints exercised')
    for exponent in (-257, 257):
        alpha = power(J if exponent > 0 else JINV, abs(exponent))
        result = target.decode(*target.encode(alpha))
        require((result.coefficients, result.strip_coefficients, result.unit_exponent) ==
                (alpha, ONE, exponent), 'large signed integer exponent')

    malformed = 0
    bad_scalars = (None, 1, '1234', (), (1, 2, 3), (1, 2, 3, 4, 5),
                   (True, 0, 0, 0), (1.0, 0, 0, 0), ('1', 0, 0, 0), iter(()))
    for bad in bad_scalars:
        reject(target.encode, (bad,))
        malformed += 1
    for bad in (ZERO, (6, 0, 0, 0)):
        reject(target.encode, (bad,))
        malformed += 1
    bad_digits = (None, 0, '000000', (), (0,)*5, (0,)*7,
                  (-1, 0, 0, 0, 0, 0), (5, 0, 0, 0, 0, 0),
                  (True, 0, 0, 0, 0, 0), (0.0, 0, 0, 0, 0, 0), iter(()))
    for f in (target.decode, target.T6, target.T6_inverse):
        for bad in bad_digits:
            reject(f, (2, 3, bad), target.InvalidReading)
            malformed += 1
        for bad in (True, 2.0, '2', None):
            reject(f, (bad, 3, (0,)*6), target.InvalidReading)
            reject(f, (2, bad, (0,)*6), target.InvalidReading)
            malformed += 2
        require(f(2, 3, [1, 0, 0, 0, 0, 0]) == f(2, 3, (1, 0, 0, 0, 0, 0)),
                'list digit normalization')

    early_invalid = 0
    for s0, s1 in product(range(-20, 21), repeat=2):
        bad = s0 <= 0 or s1 <= 0 or (s0+s1) % 5 != 0
        if not bad:
            u, v = (s0+s1)//5, (3*s0-2*s1)//5
            bad = not 1 <= u*u+u*v-v*v <= 941
        if bad:
            reject(target.decode, (s0, s1, (0,)*6), target.InvalidReading)
            early_invalid += 1
    for s0, s1 in ((0, 0), (50, 75), (72, 108), (1, 1), (10**200, 1)):
        if (s0, s1) == (50, 75):
            # Norm625 is admitted. The zero residue cannot represent 5,
            # whose lambda valuation is4; the exhaustive image check decides.
            key = (s0, s1, (0,)*6)
            require(key not in oracle, 'declared incompatible residue fixture')
        reject(target.decode, (s0, s1, (0,)*6), target.InvalidReading)

    # The exposed three-pair proof of the minimum is audited directly,
    # without rerunning the eight-depth census or selecting a new witness.
    families = (((-3, -5, -3, -3), (2, 5, 2, 2)),
                ((-2, 1, 1, 3), (3, 1, 1, -2)),
                ((-6, -6, -5, -4), (-1, -1, 5, 1)))
    quotients = ((1, 0, -2, -2), (-1, -3, -3, -1), (2, 2, 0, -1))
    vertices = set()
    pairs = 0
    lam5 = power(LAMBDA, 5)
    for (a, b), q in zip(families, quotients):
        require(mul(lam5, q) == sub(b, a), 'exposed depth-five quotient')
        require(facts(a) == facts(b), 'exposed pair common data')
        for sign in (-1, 1):
            for k in range(5):
                unit = tuple(sign*c for c in power(ZETA, k))
                aa, bb = mul(unit, a), mul(unit, b)
                require(aa in uv_by_scalar and bb in uv_by_scalar, 'orbit strip membership')
                require(aa not in vertices and bb not in vertices and aa != bb,
                        'thirty disjoint pairs')
                vertices.update((aa, bb))
                pairs += 1
    require(pairs == 30 and len(vertices) == 60, 'exposed capacity certificate')

    report = {
        'probe': 'P-J-LAMBDA6-DECODER-INTERFACE-1', 'status': 'PASS',
        'strip': len(strip), 'strip_sha256': strip_digest,
        'residue_classes': len(residues), 'residue_characteristic': 25,
        'normalized_trace_pairs': len(normalized_pairs),
        'normalized_readings_checked': accepted+rejected,
        'normalized_accepted': accepted, 'normalized_rejected': rejected,
        'translated_nonimage_cases': translated_invalid,
        'nonrepresentable_normalized_trace_pairs': len(set(normalized_pairs)-represented_pairs),
        'data_operator_cases': transitions, 'signed_strip_cases': translated,
        'signed_exponents': exponent_set, 'large_signed_exponents': [-257, 257],
        'boundary_representatives': boundary, 'malformed_cases': malformed,
        'early_invalid_trace_cases': early_invalid, 'disjoint_depth5_pairs': pairs,
        'arithmetic': 'integers and Fraction; independent polynomial/lattice oracle',
    }
    sys.stdout.buffer.write((json.dumps(report, sort_keys=True, separators=(',', ':')) + '\n').encode('utf-8'))


if __name__ == '__main__':
    main()
