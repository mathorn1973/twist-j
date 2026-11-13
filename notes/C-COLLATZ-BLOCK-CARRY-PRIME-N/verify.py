#!/usr/bin/env python3
"""Result-exposed, exact finite replay of the accompanying Collatz note.

Python standard library only. This file does not prove global convergence
or classify golden powers outside its declared finite ranges.
"""

from itertools import product
from math import comb, gcd


def v2(n):
    assert n > 0
    result = 0
    while n % 2 == 0:
        n //= 2
        result += 1
    return result


def step(n):
    assert n > 0 and n % 2 == 1
    raw = 3 * n + 1
    depth = v2(raw)
    return raw >> depth, depth


def ci(n):
    return 2 * n.bit_count() - (3 * n).bit_count()


def ct(n):
    return 2 * n.bit_count() + 1 - (3 * n + 1).bit_count()


def golden(n):
    return (n & (n >> 1)) == 0


def column_adder(n, drive):
    """Add n+2n+drive bit by bit; count all outgoing carries."""
    assert n >= 0 and drive in (0, 1)
    left, right = n, n << 1
    incoming, count, value, column = drive, 0, 0, 0
    while left or right or incoming:
        total = (left & 1) + (right & 1) + incoming
        incoming = total // 2
        count += incoming
        value |= (total % 2) << column
        left >>= 1
        right >>= 1
        column += 1
    return value, count


def audit_carry(n):
    assert column_adder(n, 0) == (3 * n, ci(n)), n
    assert column_adder(n, 1) == (3 * n + 1, ct(n)), n
    assert ct(n) - ci(n) == v2(3 * n + 1), n
    assert golden(n) == (ci(n) == 0), n


def minus_tail(a, r):
    assert a > 0 and a % 2 == 1 and r >= 1
    n = (a << r) - 1
    assert n.bit_count() == a.bit_count() + r - 1
    assert ct(n) == ci(a) + r + 1
    if r >= 2:
        assert ci(n) == ci(a) + r
        assert not golden(n)
    else:
        h = (a - 1) // 2
        assert ci(n) == ci(a) + 1 - v2(3 * a - 1) == ci(h)
        assert golden(n) == golden(h)
    return n


def plus_tail(a, r):
    assert a > 0 and a % 2 == 1 and r >= 1
    n = (a << r) + 1
    assert n.bit_count() == a.bit_count() + 1
    if r >= 2:
        assert ci(n) == ci(a)
        assert golden(n) == golden(a)
    else:
        assert ci(n) == ci(a) + v2(3 * a + 1)
        assert not golden(n)
    return n


def carry_and_general_blocks():
    for n in range(4096):
        audit_carry(n)
    for n in range(128):
        assert v2(comb(3 * n, n)) == ci(n)
        assert v2(comb(3 * n + 1, n)) == ct(n)
    for h in range(64):
        for r in range(1, 9):
            a = 2 * h + 1
            minus = minus_tail(a, r)
            assert minus == (h << (r + 1)) + (1 << r) - 1
            audit_carry(minus)
            audit_carry(plus_tail(a, r))

    for n in range(1, 4096, 2):
        child, depth = step(n)
        assert (child << depth) == 3 * n + 1
        assert ((child << depth) - 1) // 3 == n
        assert gcd(n, child) == gcd(6, child) == 1
        if child == 1:
            assert depth % 2 == 0 and n == ((1 << depth) - 1) // 3
        if n > 1:
            assert (child > n) == (n % 4 == 3)
            assert (child < n) == (n % 4 == 1)
            assert not golden(n) or child < n

        k = v2(n + 1)
        u = (n + 1) >> k
        current = n
        for m in range(k):
            a, r = 3 ** m * u, k - m
            assert current == minus_tail(a, r)
            current, depth = step(current)
            if r >= 2:
                assert depth == 1
            else:
                tail_depth = v2(3 * a - 1)
                assert depth == 1 + tail_depth
                assert current == (3 * a - 1) >> tail_depth
        assert current == (3 ** k * u - 1) >> v2(3 ** k * u - 1)

        if n == 1:
            assert step(n) == (1, 2)
            continue
        r0 = v2(n - 1)
        u = (n - 1) >> r0
        last = (r0 - 1) // 2
        current = n
        for m in range(last + 1):
            a, r = 3 ** m * u, r0 - 2 * m
            assert current == plus_tail(a, r)
            current, depth = step(current)
            if r >= 3:
                assert depth == 2
            elif r == 2:
                tail_depth = v2(3 * a + 1)
                assert depth == 2 + tail_depth
                assert current == (3 * a + 1) >> tail_depth
            else:
                assert depth == 1 and current == 3 * a + 2
        assert depth != 2
        if r0 % 2 == 0:
            q = r0 // 2
            assert current == step(3 ** (q - 1) * u)[0]
    assert ci(13) == 2 and step(13)[0] == 5


def special_prefixes():
    mersenne_golden = []
    fermat_boundaries = []
    for k in range(1, 129):
        start, current = (1 << k) - 1, (1 << k) - 1
        for m in range(k):
            a, r = 3 ** m, k - m
            assert current == minus_tail(a, r)
            if m == k - 1 and golden(current):
                mersenne_golden.append(k)
            current, depth = step(current)
            if m < k - 1:
                assert depth == 1
        tail_depth = 1 if k % 2 else 2 + v2(k)
        assert depth == 1 + tail_depth
        assert current == (3 ** k - 1) >> tail_depth
        if k == 1:
            assert current == start
        elif k in (2, 4, 8):
            assert current < start
        else:
            assert current > start

        current = (1 << k) + 1
        states = [current]
        last = (k - 1) // 2
        for m in range(last + 1):
            assert current == plus_tail(3 ** m, k - 2 * m)
            current, depth = step(current)
            states.append(current)
            if m < last:
                assert depth == 2
        q = k // 2
        if k % 2 == 0:
            assert depth == (4 if q % 2 else 3)
            assert current == (3 ** q + 1) // (4 if q % 2 else 2)
            assert current == step(3 ** (q - 1))[0]
        else:
            assert depth == 1 and current == 3 ** (q + 1) + 2
        if k >= 10:
            assert all("1111" not in format(x, "b") for x in states[:5])
            assert "1111" in format(states[5], "b")
            assert [i for i, x in enumerate(states[:6]) if golden(x)] == [0, 2, 4]
        if k in (10, 11, 12):
            fermat_boundaries.append((k, states[5], ci(states[5])))
    assert mersenne_golden == [1, 2, 3, 5, 8]
    assert fermat_boundaries == [(10, 61, 4), (11, 487, 7), (12, 973, 6)]
    assert 3 ** 9 - 1 - 4 * 9 * ((1 << 9) - 1) == 1286
    return mersenne_golden


def golden_search():
    power = 1
    powers, transformed = [], []
    for m in range(100001):
        h = (power - 1) // 2
        if m <= 1024:
            assert golden(power) == ("11" not in format(power, "b"))
            assert golden(h) == ("11" not in format(h, "b"))
        if m <= 16:
            audit_carry(power)
        if golden(power):
            powers.append(m)
        if golden(h):
            transformed.append(m + 1)
        power *= 3
    assert powers == [0, 2, 4]
    assert transformed == [1, 2, 3, 5, 8]
    return powers, transformed


def entrance(j):
    assert j >= 0
    return ((1 << (2 * j)) - 1) // 3


def order4(modulus):
    assert modulus >= 3 and gcd(4, modulus) == 1
    residue = 1
    for j in range(1, modulus + 1):
        residue = (4 * residue) % modulus
        if residue == 1:
            return j
    raise AssertionError(("order not found within finite group bound", modulus))


def inverse_and_divisibility():
    inverse_count = 0
    for child in range(1, 256, 2):
        if child % 3 == 0:
            continue
        minimum = 2 if child % 3 == 1 else 1
        base = ((child << minimum) - 1) // 3
        assert step(base) == (child, minimum)
        for depth in range(1, 13):
            numerator = (child << depth) - 1
            admissible = numerator % 3 == 0
            assert admissible == (depth % 2 == minimum % 2)
            if admissible:
                n = numerator // 3
                j = (depth - minimum) // 2
                assert n > 0 and n % 2 == 1
                assert step(n) == (child, depth)
                assert n == (base << (2 * j)) + entrance(j)
                inverse_count += 1
    assert inverse_count == 510
    for p in range(1, 256, 2):
        child, depth = step(p)
        for j in range(7):
            lifted = (p << (2 * j)) + entrance(j)
            assert 3 * lifted + 1 == (3 * p + 1) << (2 * j)
            assert step(lifted) == (child, depth + 2 * j)
    for d in range(1, 256, 2):
        j = order4(3 * d)
        n = entrance(j)
        assert n % d == 0
        assert step(n) == (1, 2 * j)
    assert step(55) == (83, 1) and step(83) == (125, 1)
    assert gcd(55, 125) == 5


def cycle_words():
    count, cycles = 0, []
    for length in range(1, 6):
        for word in product(range(1, 5), repeat=length):
            prefix, constant = 0, 0
            for i, depth in enumerate(word):
                constant += 3 ** (length - 1 - i) * (1 << prefix)
                prefix += depth
            # Independent composition of (a*x+b)/denominator.
            a, b, denominator = 1, 0, 1
            for depth in word:
                a, b, denominator = 3 * a, 3 * b + denominator, denominator << depth
            assert (a, b, denominator) == (3 ** length, constant, 1 << sum(word))
            difference = denominator - a
            if difference > 0 and constant % difference == 0:
                start = constant // difference
                n = start
                for depth in word:
                    n, actual = step(n)
                    assert actual == depth
                assert n == start
                cycles.append((length, start, word))
            count += 1
    assert count == 1364
    assert cycles == [(length, 1, (2,) * length) for length in range(1, 6)]
    for x in range(5):
        assert ((3 * x + 1) * pow(8, -1, 5)) % 5 == (x + 2) % 5


def trajectory_fixtures():
    for n, carries, overlaps in ((3, 2, 1), (27, 5, 2), (243, 6, 4)):
        audit_carry(n)
        assert ci(n) == carries
        assert (n & (n << 1)).bit_count() == overlaps
    mersenne = [255, 383, 575, 863, 1295, 1943, 2915, 4373, 205]
    for i, (left, right) in enumerate(zip(mersenne, mersenne[1:])):
        assert step(left) == (right, 1 if i < 7 else 6)
    assert [i for i, n in enumerate(mersenne[:8]) if golden(n)] == [7]
    assert (3 ** 7 - 1) // 2 == 1093
    assert format(1093, "b") == "10001000101"
    assert golden(1093) and golden(4373) and not golden(3 ** 7)
    path = [257, 193, 145, 109, 41, 31, 47, 71, 107, 161, 121]
    for left, right in zip(path, path[1:]):
        assert step(left)[0] == right
    assert step(109)[0] == step(27)[0] == 41

    odd, depths = [27], []
    while odd[-1] != 1:
        assert len(depths) < 1000
        n, depth = step(odd[-1])
        odd.append(n)
        depths.append(depth)
    raw = [27]
    while raw[-1] != 1:
        assert len(raw) - 1 < 1000
        n = raw[-1]
        raw.append(3 * n + 1 if n % 2 else n // 2)
    assert [n for n in raw if n % 2] == odd
    assert len(depths) == 41 and len(raw) - 1 == 111
    assert sum(depth + 1 for depth in depths) == 111
    assert max(odd) == 3077 and max(raw) == 9232


def main():
    if not __debug__:
        raise RuntimeError("Assertions must remain enabled; do not use -O or -OO.")
    carry_and_general_blocks()
    mersenne_golden = special_prefixes()
    powers, transformed = golden_search()
    inverse_and_divisibility()
    cycle_words()
    trajectory_fixtures()
    print("COLLATZ-VALUATION-CARRY-REPLAY v1")
    print("arithmetic: exact integers; result-exposed replay")
    print("carry: n=0..4095; Kummer n=0..127; h=0..63,r=1..8; PASS")
    print("odd inputs: n=1..4095; actual T, both maximal prefixes, gcd, inverse; PASS")
    print("Mersenne and plus-one families: k=1..128; prefixes and boundaries; PASS")
    print("Mersenne block: k=1 equal; k=2,4,8 decrease; remaining k<=128 increase")
    print("Mersenne golden last-prefix states, k=1..128:", mersenne_golden)
    print("golden powers 3^m, m=0..100000:", powers)
    print("golden (3^(k-1)-1)/2, k=1..100001:", transformed)
    print("carry/overlap at 3,27,243: [2,5,6] / [1,2,4]")
    print("plus-one m=5 at k=10,11,12: states [61,487,973], carries [4,7,6]")
    print("inverse: 510 admissible pairs; towers p<=255,j<=6; odd divisors d<=255; PASS")
    print("cycle words: length=1..5, depths=1..4; 1364 words; only repeated fixed point 1")
    print("fixtures: 255 reaches first Z at 4373 then 205; 257 joins 27 at 41; PASS")
    print("orbit 27: 41 odd steps, 111 ordinary steps, maxima 3077 and 9232; PASS")
    print("scope: finite replay; universal identities require the accompanying proofs")
    print("scope: no global golden-exponent classification or Collatz convergence claim")


if __name__ == "__main__":
    main()
