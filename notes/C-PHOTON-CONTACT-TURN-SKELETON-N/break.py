#!/usr/bin/env python3
"""Independent implementation audit for #1195, not blind proof confirmation.

Frozen before execution and before reading the builder's verify.py.
PUBLIC, NON-CANONICAL. Apache-2.0. A. M. Thorn.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def cosh_log2(k: int) -> F:
    k = abs(k)
    return (F(2) ** k + F(1, 2) ** k) / 2


def main() -> None:
    hcos = F(5, 4)
    r = F(34, 25)
    a = hcos ** 6 / 32
    B = a * r ** 3
    v = F(1, 16)
    z = r * v
    A = 4 * B
    q = 2 * B * (1 + 6 * z)
    assert (a, B, A, q) == (F(15625, 131072), F(4913, 16384),
                            F(4913, 4096), F(741863, 819200))
    assert 0 < z < 1 and 0 < q < 1
    face_cases = 0
    for m in range(5):
        for signs in product((-1, 1), repeat=m):
            assert cosh_log2(sum(signs)) <= hcos ** m * r ** comb(m, 2)
            face_cases += 1

    # Eight actual directions, rather than a scalar branching recurrence.
    directions = tuple((axis, sign) for axis in range(4) for sign in (-1, 1))
    weights = {d: F(d == (0, 1)) for d in directions}
    for length in range(1, 33):
        assert sum(weights.values()) == (1 + 6 * z) ** (length - 1)
        assert 2 * (2 * B) ** length * sum(weights.values()) == A * q ** (length - 1)
        weights = {d: sum(w * (1 if old == d else z)
                         for old, w in weights.items()
                         if not (old[0] == d[0] and old[1] == -d[1]))
                   for d in directions}

    # Derive power sums S_k=sum_{n>=0} n^k q^n by shifting n, not by
    # copying either published cubic tail formula. The k=0 convention is 0^0=1.
    S = [1 / (1 - q)]
    for k in range(1, 4):
        S.append(q / (1 - q) * sum(comb(k, j) * S[j] for j in range(k)))

    def tail(R: int) -> F:
        return q ** (R - 1) * sum(comb(3, j) * R ** (3 - j) * S[j]
                                  for j in range(4))

    C = A * tail(16) / 64
    assert 1193 < C < 1194
    for R in range(16, 81):
        assert tail(R) - tail(R + 1) == R ** 3 * q ** (R - 1)
        assert 0 < tail(R + 1) < tail(R)
        direct = q ** (R - 1) * (F(R ** 3) / (1 - q)
                 + 3 * R ** 2 * q / (1 - q) ** 2
                 + 3 * R * q * (1 + q) / (1 - q) ** 3
                 + q * (1 + 4 * q + q ** 2) / (1 - q) ** 4)
        assert direct == tail(R)
    initial = (1 + 4 * q + q ** 2) / (1 - q) ** 4
    assert tail(16) == initial - sum(m ** 3 * q ** (m - 1) for m in range(1, 16))

    tilted_pairs = 0
    for m in range(129):
        for c in range(m // 4 + 1):
            assert r ** c <= 2 ** m * z ** c
            tilted_pairs += 1

    print('NON-CANONICAL separate-session arithmetic audit')
    print('PASS signed face cases:', face_cases)
    print('PASS eight-direction transfer lengths: 1..32')
    print('PASS fixed tilted pairs:', tilted_pairs)
    print('PASS independent power-sum derivation and tail recurrences: 16..80')
    print('A=4913/4096 q=741863/819200 gap=77337/819200')
    print('C_quarter=' + str(C))
    print('PASS 1193<C_quarter<1194; no full-Xi or P1 conclusion')


if __name__ == '__main__':
    main()
