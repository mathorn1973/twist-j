#!/usr/bin/env python3
"""Exact finite checks for the return-order comparison."""

from math import gcd, lcm


ONE = (1, 0)
ALPHA = (1, 1)


def factors(number):
    result = {}
    divisor = 2
    while divisor * divisor <= number:
        while number % divisor == 0:
            result[divisor] = result.get(divisor, 0) + 1
            number //= divisor
        divisor += 1 if divisor == 2 else 2
    if number > 1:
        result[number] = 1
    return result


def multiply(left, right, modulus):
    a, b = left
    c, d = right
    return ((a * c + b * d) % modulus, (a * d + b * c + b * d) % modulus)


def alpha_power(exponent, modulus):
    result, base = ONE, ALPHA
    while exponent:
        if exponent & 1:
            result = multiply(result, base, modulus)
        exponent //= 2
        if exponent:
            base = multiply(base, base, modulus)
    return result


def order_at_prime_power(p, exponent):
    modulus = p ** exponent
    candidate = (p * p - 1) * p ** (exponent - 1)
    assert alpha_power(candidate, modulus) == ONE
    for divisor in factors(candidate):
        while candidate % divisor == 0 and alpha_power(candidate // divisor, modulus) == ONE:
            candidate //= divisor
    return candidate


def order(d, k=1):
    return lcm(*(order_at_prime_power(p, a * k) for p, a in factors(d).items()))


def fibpair(n, modulus=None):
    if n == 0:
        return (0, 1)
    a, b = fibpair(n // 2, modulus)
    even = a * (2 * b - a)
    odd = a * a + b * b
    if n % 2:
        result = odd, even + odd
    else:
        result = even, odd
    if modulus is not None:
        result = tuple(x % modulus for x in result)
    return result


def B_positive(n, modulus=None):
    a, b = fibpair(n, modulus)
    result = 2 * b - a if n % 2 else a
    return result if modulus is None else result % modulus


def chi(n):
    return (0, 1, -1, -1, 1)[n % 5]


def residue_kernel(n):
    return (0, 1, 0, -1, 0)[n % 5]


def v2(n):
    return (n & -n).bit_length() - 1


def check_boolean(d):
    h = order(d)
    depths = {v2(order_at_prime_power(p, 1)) for p in factors(d)}
    negative_allowed = len(depths) == 1 and 0 not in depths and h % 5 != 0
    for n in range(3, 3 + 10 * h, 2):
        sign = chi(n)
        if sign == 0:
            continue
        r = (n - sign) // 2
        actual = alpha_power(r, d) == (sign % d, 0)
        expected = (sign == 1 and (n - 1) % (2 * h) == 0) or (
            sign == -1 and negative_allowed and (n + 1 - h) % (2 * h) == 0)
        assert actual == expected, (d, n)
    early = min(k for k in range(1, h + 1) if alpha_power(5 * k, d) == ONE)
    other_progression_hit = any(alpha_power(5 * k + 4, d) == ONE for k in range(h))
    recovered = early if other_progression_hit else 5 * early
    assert recovered == h, d
    return h, negative_allowed


def main():
    finite_domain = [d for d in range(3, 151, 2) if d % 5 and set(factors(d).values()) == {1}]
    for d in finite_domain:
        check_boolean(d)

    p, q = 101, 151
    d = p * q
    assert factors(p) == {p: 1} and factors(q) == {q: 1}
    assert chi(p) == chi(q) == 1
    assert check_boolean(p) == check_boolean(q) == check_boolean(d) == (25, False)
    assert p % 150 == d % 150
    assert residue_kernel(d // p) == residue_kernel(d // d) == 1
    assert (-2) ** len(factors(p)) == -2 and (-2) ** len(factors(d)) == 4
    assert B_positive(25) == 11 * p * q
    assert [order(x, 2) for x in (p, q, d)] == [25 * x for x in (p, q, d)]

    vertical_domain = (3, 7, 9, 11, 21, 29, p, q, d)
    for modulus in vertical_domain:
        first = order(modulus)
        B = B_positive(first)
        for k in (1, 2, 3):
            raised = modulus ** k
            assert order(modulus, k) == first * raised // gcd(raised, B), (modulus, k)

    for j in (2, 3):
        h = 3 ** j
        Q = B_positive(h // 3) ** 2 + 3
        denominator = B_positive(5 * h)
        assert all(order_at_prime_power(p, a) == h for p, a in factors(Q).items())
        for t in (1, 2, Q, 2 * Q):
            numerator_mod = B_positive(5 * h * t, Q * denominator)
            assert numerator_mod % denominator == 0
            assert gcd(Q, numerator_mod // denominator) == gcd(Q, t), (j, t)
    print(f"Full signed periods checked for {len(finite_domain)} odd squarefree moduli up to 150, and for 101, 151, 15251.")
    print("At N=15251, d=101 and d=15251 have descriptor (25, false), residue 101 mod 150, and kernel 1.")
    print("Their signed contributions are respectively -2 and +4. At depth two their orders are 2525 and 381275.")
    print(f"Vertical order identities checked for {len(vertical_domain)} moduli at three levels.")
    print("Exact vertical quotients checked at the preregistered four multipliers for each of Q_2, Q_3.")


if __name__ == "__main__":
    main()
