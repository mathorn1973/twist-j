#!/usr/bin/env python3
"""Exact bounded replay for the odd-head note; see REPLAY-SPEC.md.

No numerical claim about an infinite expectation or an infinite orbit is
made by this program. Run only after its public source/specification pin.
"""

from collections import Counter
from fractions import Fraction
from itertools import product


def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def odd_step(n):
    """Actual accelerated step, using successive integer divisions."""
    assert n > 0 and n % 2 == 1
    m, depth = 3 * n + 1, 0
    while m % 2 == 0:
        m //= 2
        depth += 1
    return m, depth


def sign(n):
    return (n > 0) - (n < 0)


def ci(n):
    assert n >= 0
    return 2 * n.bit_count() - (3 * n).bit_count()


def prime_power(p, exponent):
    if exponent >= 0:
        return Fraction(p ** exponent)
    return Fraction(1, p ** (-exponent))


def valuation(n, p):
    assert n > 0 and p in (2, 3)
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    return result


def product_formula(coefficient):
    assert coefficient > 0
    v_two = valuation(coefficient.numerator, 2) - valuation(coefficient.denominator, 2)
    v_three = valuation(coefficient.numerator, 3) - valuation(coefficient.denominator, 3)
    assert coefficient * prime_power(2, -v_two) * prime_power(3, -v_three) == 1


def block(n):
    """Compute B by k actual odd steps, then audit the closed identities."""
    assert n > 0 and n % 2 == 1
    k = v2(n + 1)
    u = (n + 1) >> k
    m, actual_word = n, []
    for _ in range(k):
        m, depth = odd_step(m)
        actual_word.append(depth)
    three_k = 3 ** k
    numerator = three_k * u - 1
    t = v2(numerator)
    assert actual_word == [1] * (k - 1) + [t + 1]
    assert m == numerator >> t
    kp = v2(m + 1)
    up = (m + 1) >> kp
    assert u % 2 == up % 2 == 1 and u > 0 and up > 0
    assert (up << (t + kp)) == three_k * u + (1 << t) - 1
    recovered = (up << (t + kp)) - (1 << t) + 1
    assert recovered % three_k == 0 and recovered // three_k == u
    assert ((recovered // three_k) << k) - 1 == n

    node_denominator = 1 << (k + t)
    head_denominator = 1 << (t + kp)
    assert node_denominator * m - three_k * n == three_k - (1 << k) > 0
    assert head_denominator * up - three_k * u == (1 << t) - 1 > 0
    assert sign(m - n) == sign((three_k - node_denominator) * n + three_k - (1 << k))
    assert sign(up - u) == sign((three_k - head_denominator) * u + (1 << t) - 1)
    return k, u, t, m, kp, up


def coefficients(k, t, kp):
    three_k = 3 ** k
    node_denominator = 1 << (k + t)
    head_denominator = 1 << (t + kp)
    return (
        Fraction(three_k, node_denominator),
        Fraction(three_k - (1 << k), node_denominator),
        Fraction(three_k, head_denominator),
        Fraction((1 << t) - 1, head_denominator),
    )


def all_inputs_and_cylinders():
    joint = Counter()
    for n in range(1, 65536, 2):
        k, u, t, m, kp, up = block(n)
        a = 3 ** k * u
        next_depth = v2(3 * m + 1)
        assert (up % 3 == 0) == (t % 2 == 0)
        assert a.bit_count() == up.bit_count() + kp
        assert ci(a) == ci(up) + kp + 1 - (next_depth if t >= 2 else 0)
        assert up.bit_count() % 2 == (ci(3 ** (k - 1) * u) + kp) % 2
        if k <= 4 and t <= 4 and kp <= 4:
            joint[k, t, kp, up % 16] += 1
    for k, t, kp in product(range(1, 5), repeat=3):
        for residue in range(1, 16, 2):
            assert joint[k, t, kp, residue] == 1 << (16 - k - t - kp - 4)

    conditional = Counter()
    for fixed_k in range(1, 9):
        for u in range(1, 4096, 2):
            k, recovered_u, t, _, kp, up = block((u << fixed_k) - 1)
            assert k == fixed_k and recovered_u == u
            if t <= 4 and kp <= 4:
                conditional[k, t, kp, up % 16] += 1
    for k in range(1, 9):
        for t, kp in product(range(1, 5), repeat=2):
            for residue in range(1, 16, 2):
                assert conditional[k, t, kp, residue] == 1 << (12 - t - kp - 4)


def inverse_triples():
    valid_total = 0
    for k, t, kp in product(range(1, 7), repeat=3):
        modulus = 3 ** k
        residue = ((1 << t) - 1) * pow(1 << (t + kp), -1, modulus) % modulus
        odd_residue = residue if residue % 2 else residue + modulus
        assert 1 <= odd_residue < 2 * modulus and odd_residue % 2 == 1
        expected = 0 if odd_residue > 255 else 1 + (255 - odd_residue) // (2 * modulus)
        observed = 0
        for up in range(1, 256, 2):
            numerator = (up << (t + kp)) - (1 << t) + 1
            divisible = numerator % modulus == 0
            assert divisible == (up % (2 * modulus) == odd_residue)
            if divisible:
                u = numerator // modulus
                assert u > 0 and u % 2 == 1
                n = (u << k) - 1
                assert block(n) == (k, u, t, (up << kp) - 1, kp, up)
                observed += 1
        assert observed == expected
        valid_total += observed
    return valid_total


def fixed_child_fibers():
    target_count = 0
    for k in range(1, 7):
        modulus = 3 ** k
        period = 2 * 3 ** (k - 1)
        residues, value = [], 1
        for _ in range(period):
            residues.append(value)
            value = 2 * value % modulus
        assert value == 1 and len(set(residues)) == period
        assert set(residues) == {r for r in range(1, modulus) if r % 3}
        for m in range(1, 64, 2):
            if m % 3 == 0:
                continue
            matches = [t for t in range(1, period + 1)
                       if residues[t % period] * m % modulus == modulus - 1]
            assert len(matches) == 1
            first = matches[0]
            for j in range(3):
                t = first + j * period
                numerator = (m << t) + 1
                assert numerator % modulus == 0
                u = numerator // modulus
                got = block((u << k) - 1)
                assert got[:4] == (k, u, t, m)
            target_count += 1
    assert target_count == 126
    return target_count


def growing_family():
    rows = []
    for length in range(1, 129):
        heads = [9 ** j * (1 << (3 * (length - j) + 1)) - 1
                 for j in range(length + 1)]
        nodes = [4 * u - 1 for u in heads]
        assert nodes[0] == (1 << (3 * length + 3)) - 5
        assert nodes[-1] == 8 * 9 ** length - 5
        for j in range(length + 1):
            assert v2(heads[j] + 1) == 3 * (length - j) + 1
            assert valuation(heads[j] + 1, 3) == 2 * j
            assert v2(nodes[j] + 5) == 3 * (length - j) + 3
            assert valuation(nodes[j] + 5, 3) == 2 * j
        for j in range(length):
            assert heads[j] % 16 == 15
            assert block(nodes[j]) == (2, heads[j], 1, nodes[j + 1], 2, heads[j + 1])
            assert nodes[j + 1] > nodes[j] and heads[j + 1] > heads[j]
            a_node, b_node, a_head, b_head = coefficients(2, 1, 2)
            assert a_node == a_head == Fraction(9, 8)
            assert b_node == Fraction(5, 8) and b_head == Fraction(1, 8)
            product_formula(a_node)
            product_formula(a_head)
        assert heads[-1] % 16 == 1
        kp = 1 + v2(length + 1)
        next_node = (9 ** (length + 1) - 5) // 4
        next_head = (9 ** (length + 1) - 1) >> (3 + v2(length + 1))
        assert block(nodes[-1]) == (2, heads[-1], 3, next_node, kp, next_head)
        assert next_node < nodes[-1] and next_head < heads[-1]
        mersenne_start = (1 << (2 * (length + 1))) - 1
        assert block(mersenne_start)[3] == next_head
        if length == 6:
            assert next_head == 597871 > heads[0] == 524287
        a_node, _, a_head, _ = coefficients(2, 3, kp)
        assert a_node == Fraction(9, 32)
        product_formula(a_node)
        product_formula(a_head)
        if length in (1, 2, 4):
            rows.append((length, nodes[0], nodes[-1], heads[0], heads[-1]))
    assert rows == [(1, 59, 67, 15, 17), (2, 507, 643, 127, 161),
                    (4, 32763, 52483, 8191, 13121)]
    return rows


def realizes_word(n, word):
    for wanted_k, wanted_t in word:
        k, _, t, n, _, _ = block(n)
        if (k, t) != (wanted_k, wanted_t):
            return False
    return True


def finite_words():
    alphabet = tuple(product(range(1, 4), repeat=2))
    count = 0
    for word_length in range(1, 4):
        for word in product(alphabet, repeat=word_length):
            odd_steps, divisions, constant = 0, 0, 0
            slope, offset = Fraction(1), Fraction(0)
            for k, t in word:
                constant = 3 ** k * constant + (3 ** k - (1 << k)) * (1 << divisions)
                odd_steps += k
                divisions += k + t
                # Independent composition from the expanded odd-step word.
                for depth in [1] * (k - 1) + [t + 1]:
                    slope = 3 * slope / (1 << depth)
                    offset = (3 * offset + 1) / (1 << depth)
            assert slope == Fraction(3 ** odd_steps, 1 << divisions)
            assert offset == Fraction(constant, 1 << divisions)
            modulus = 1 << (divisions + 1)
            residue = (((1 << divisions) - constant)
                       * pow(3 ** odd_steps, -1, modulus)) % modulus
            assert 0 < residue < modulus and residue % 2 == 1
            for j in range(4):
                start, n = residue + j * modulus, residue + j * modulus
                for k, t in word:
                    got_k, _, got_t, n, _, _ = block(n)
                    assert (got_k, got_t) == (k, t)
                assert (n << divisions) == 3 ** odd_steps * start + constant
                assert n == slope * start + offset
            assert not realizes_word(residue + (1 << divisions), word)
            count += 1
    assert count == 819
    return count


def sixteen_block_traces():
    for start in range(1, 1024, 2):
        initial_k = v2(start + 1)
        initial_u = (start + 1) >> initial_k
        n = start
        odd_steps, divisions, constant = 0, 0, 0
        node_product, head_product, head_offset = Fraction(1), Fraction(1), Fraction(0)
        for _ in range(16):
            k, u, t, m, kp, up = block(n)
            a_node, b_node, a_head, b_head = coefficients(k, t, kp)
            assert m == a_node * n + b_node and up == a_head * u + b_head
            assert b_node > 0 and b_head > 0
            node_product *= a_node
            head_product *= a_head
            head_offset = a_head * head_offset + b_head
            constant = 3 ** k * constant + (3 ** k - (1 << k)) * (1 << divisions)
            odd_steps += k
            divisions += k + t
            assert (m << divisions) == 3 ** odd_steps * start + constant
            assert (m < start) == (((1 << divisions) - 3 ** odd_steps) * start > constant)
            assert node_product == Fraction(3 ** odd_steps, 1 << divisions)
            assert head_product == prime_power(2, initial_k - kp) * node_product
            assert Fraction(up, initial_u) == prime_power(2, initial_k - kp) * Fraction(m + 1, start + 1)
            assert up == head_product * initial_u + head_offset
            assert head_offset > 0 and m > node_product * start
            n = m


def partial_moments():
    for bound in range(1, 65):
        mass = sum((Fraction(1, 1 << r) for r in range(1, bound + 1)), Fraction(0))
        first = sum((Fraction(r, 1 << r) for r in range(1, bound + 1)), Fraction(0))
        down = sum((Fraction(1, 4 ** r) for r in range(1, bound + 1)), Fraction(0))
        node_up = sum((Fraction(3, 4) ** r for r in range(1, bound + 1)), Fraction(0))
        head_up = sum((Fraction(3, 2) ** r for r in range(1, bound + 1)), Fraction(0))
        assert mass == 1 - Fraction(1, 1 << bound)
        assert first == 2 - Fraction(bound + 2, 1 << bound)
        assert down == (1 - Fraction(1, 4 ** bound)) / 3
        assert node_up == 3 * (1 - Fraction(3, 4) ** bound)
        assert head_up == 3 * (Fraction(3, 2) ** bound - 1)
        node_partial = node_up * down
        head_partial = head_up * down ** 2
        assert node_partial == (1 - Fraction(3, 4) ** bound) * (1 - Fraction(1, 4 ** bound))
        assert head_partial == (Fraction(3, 2) ** bound - 1) * (1 - Fraction(1, 4 ** bound)) ** 2 / 3
        assert 0 < node_partial < 1
        if bound <= 6:
            direct_node = sum((Fraction(3 ** k, 1 << (2 * (k + t)))
                               for k, t in product(range(1, bound + 1), repeat=2)), Fraction(0))
            direct_head = sum((Fraction(3 ** k, 1 << (k + 2 * (t + kp)))
                               for k, t, kp in product(range(1, bound + 1), repeat=3)), Fraction(0))
            assert direct_node == node_partial and direct_head == head_partial


def head_one_counterexamples():
    values = []
    for k in range(1, 32, 2):
        n = (1 << k) - 1
        child = (3 ** k - 1) // 2
        next_head = (3 ** k + 1) // 4
        assert block(n) == (k, 1, 1, child, 1, next_head)
        values.append(next_head)
    assert values[:3] == [1, 7, 61]
    assert all(a < b for a, b in zip(values, values[1:]))


def main():
    if not __debug__:
        raise RuntimeError("Assertions must remain enabled; do not use -O or -OO.")
    all_inputs_and_cylinders()
    inverse_count = inverse_triples()
    fiber_targets = fixed_child_fibers()
    family_rows = growing_family()
    word_count = finite_words()
    sixteen_block_traces()
    partial_moments()
    head_one_counterexamples()
    print("COLLATZ-ODD-HEAD-REPLAY v1")
    print("arithmetic: exact integers and Fraction; bounded replay of stated identities")
    print("odd inputs: 32768; actual blocks, head/inverse/sign identities and carry flags; PASS")
    print("joint cylinders: k,t,k'=1..4,u' mod16; 512 exact cells modulo 2^16; PASS")
    print("conditional cylinders: k=1..8,odd u<=4095; 1024 exact cells; PASS")
    print("inverse triples: k,t,k'=1..6,odd u'<=255; valid inputs:", inverse_count)
    print("fixed-child fibers: k=1..6,odd child<=63 coprime to3; targets:", fiber_targets)
    print("growing family: R=1..128; exactly R growth blocks then a contracting boundary; PASS")
    print("family rows: R,start_n,after_R_n,start_u,after_R_u")
    for row in family_rows:
        print(",".join(map(str, row)))
    print("finite block words: length=1..3,k,t=1..3; words:", word_count)
    print("word cylinders: four integer representatives each; highest code bit toggle rejected; PASS")
    print("traces: 16 blocks for 512 odd starts; composition, descent, size ratio and coboundary; PASS")
    print("moment partial sums: M=1..64; direct pair/triple sums M=1..6; PASS")
    print("head u=1: odd k=1..31; first next heads [1,7,61]; PASS")
    print("scope: infinite Haar laws, limiting moments and logarithmic drift are proof-only")
    print("scope: no claim of convergence or divergence of a positive integer orbit")


if __name__ == "__main__":
    main()
