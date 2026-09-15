#!/usr/bin/env python3
"""Exact finite and coefficient audit of the five-point readout theorem."""

from fractions import Fraction as Q
from itertools import product


def transpose(a):
    return list(map(list, zip(*a)))


def mm(a, b):
    return [[sum((x*y for x, y in zip(row, col)), Q(0))
             for col in zip(*b)] for row in a]


def plus(a, b, sign=1):
    return [[x+sign*y for x, y in zip(row, other)] for row, other in zip(a, b)]


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def diagonal(w):
    return [[Q(w[i]) if i == j else Q(0) for j in range(len(w))]
            for i in range(len(w))]


def partitions(prefix=(0,)):
    if len(prefix) == 5:
        yield prefix
    else:
        for k in range(max(prefix)+2):
            yield from partitions(prefix+(k,))


def main():
    identity = eye(5)
    pi = [[Q(i == j)-Q(1, 5) for j in range(5)] for i in range(5)]
    complement = plus(identity, pi, -1)
    zero = [[Q(0)]*5 for _ in range(5)]
    basis = [[Q(i == j)-Q(i == 4) for j in range(4)] for i in range(5)]
    gram = mm(transpose(basis), basis)
    assert mm(pi, pi) == pi and mm(pi, basis) == basis
    all_partitions = list(partitions())
    assert len(all_partitions) == 52 and len(set(all_partitions)) == 52
    isometries, killed = 0, 0
    for f in all_partitions:
        n = [[Q(f[s] == y) for s in range(5)] for y in range(max(f)+1)]
        pushed = mm(n, basis)
        isometric = mm(transpose(pushed), pushed) == gram
        assert isometric == (len(set(f)) == 5)
        isometries += int(isometric)
        if not isometric:
            s, t = next((s, t) for s in range(5) for t in range(s+1, 5)
                        if f[s] == f[t])
            d = [[Q(i == s)-Q(i == t)] for i in range(5)]
            assert sum(x[0] for x in d) == 0
            assert mm(transpose(d), d) == [[Q(2)]]
            assert mm(n, d) == [[Q(0)] for _ in n]
            killed += 1
    assert (isometries, killed) == (1, 51)

    # Every ordered quadratic coefficient in the full continuous defect identity.
    raw = [diagonal([int(j == i) for j in range(5)]) for i in range(5)]
    effects = [mm(mm(pi, r), pi) for r in raw]
    for i in range(5):
        assert effects[i][i][i] > 0
        for j in range(5):
            left = plus(zero, mm(effects[i], effects[j]), -1)
            right = mm(mm(mm(mm(pi, raw[i]), complement), raw[j]), pi)
            if i == j:
                right = plus(right, effects[i], -1)
            assert left == right

    sharp = []
    for w in product((0, 1), repeat=5):
        d = diagonal(w)
        effect = mm(mm(pi, d), pi)
        defect = plus(effect, mm(effect, effect), -1)
        k = sum(w)
        assert sum(defect[i][i] for i in range(5)) == Q(k*(5-k), 25)
        commuting = mm(d, pi) == mm(pi, d)
        assert (defect == zero) == commuting == (k in (0, 5))
        if defect == zero:
            sharp.append(effect)
    assert sharp == [zero, pi]
    assert all(pi[i][j] != 0 for i in range(5) for j in range(5))

    # Positive control for the lemma: a code with two disconnected active blocks.
    code = [[Q(0)]*5 for _ in range(5)]
    for a, b in ((0, 1), (2, 3)):
        code[a][a] = code[b][b] = Q(1, 2)
        code[a][b] = code[b][a] = Q(-1, 2)
    assert mm(code, code) == code
    distinct = set()
    for w in product((0, 1), repeat=5):
        d = diagonal(w)
        effect = mm(mm(code, d), code)
        sharp_control = mm(effect, effect) == effect
        assert sharp_control == (mm(code, d) == mm(d, code))
        if sharp_control:
            distinct.add(tuple(x for row in effect for x in row))
    assert len(distinct) == 4
    print('POINT_MAP partitions=52 isometric=1 killed_contrasts=51 PASS')
    print('CONTINUOUS_DEFECT ordered_quadratic_coefficients=25 exact PASS')
    print('SIMPLEX binary_masks=32 sharp_effects=0,I_H PASS')
    print('SHARPNESS_DEFECT trace=k*(5-k)/25 PASS')
    print('COMPRESSION_LEMMA disconnected_control_sharp_effects=4 PASS')
    print('SCOPE five_point_free_encoding;deterministic_finite_map;classical_endpoint_read')
    print('PHYSICAL complete_apparatus_nogo=NOT_CLAIMED')


if __name__ == '__main__':
    main()
