#!/usr/bin/env python3
"""Independent matrix implementation of the frozen R2-M125 menu."""

import json
from math import gcd


M = (1, 1, 1, 0)
I = (1, 0, 0, 1)


def matrix_product(a, b, modulus=None):
    values = (
        a[0] * b[0] + a[1] * b[2],
        a[0] * b[1] + a[1] * b[3],
        a[2] * b[0] + a[3] * b[2],
        a[2] * b[1] + a[3] * b[3],
    )
    if modulus is None:
        return values
    return tuple(value % modulus for value in values)


def matrix_power(exponent, modulus=None):
    result, base = I, M
    while exponent:
        if exponent & 1:
            result = matrix_product(result, base, modulus)
        base = matrix_product(base, base, modulus)
        exponent //= 2
    return result


def saturations_and_atoms(n, divisors):
    full_supports = [gcd(n, pow(d, n.bit_length(), n)) for d in divisors]
    for support in full_supports:
        assert n % support == 0
        assert gcd(support, n // support) == 1
    blocks = [n]
    for support in full_supports:
        replacement = []
        for block in blocks:
            cut = gcd(block, support)
            if 1 < cut < block:
                replacement.extend((cut, block // cut))
            else:
                replacement.append(block)
        blocks = replacement
    blocks.sort()
    product = 1
    for i, block in enumerate(blocks):
        assert block > 1
        product *= block
        for other in blocks[:i]:
            assert gcd(block, other) == 1
        for support in full_supports:
            assert gcd(block, support) in (1, block)
    assert product == n
    return blocks


def inspect_side(m, sigma):
    fib = matrix_power(m)[1]
    n = 5 * fib * fib + sigma * 5 * fib + 1
    period = 10 * m
    traces = []
    for exponent in range(period):
        power = matrix_power(exponent, n)
        traces.append((power[0] + power[3]) % n)
    histogram = {}
    first = None
    proper_tests = 0
    for a in range(0, period, 2):
        for b in range(1, period, 2):
            for epsilon in (-1, 1):
                value = gcd(n, traces[a] + epsilon * traces[b])
                histogram[value] = histogram.get(value, 0) + 1
                if 1 < value < n:
                    proper_tests += 1
                    if first is None:
                        first = {"a": a, "b": b, "epsilon": epsilon,
                                 "gcd": str(value)}
    total = sum(histogram.values())
    assert total == 781250
    assert proper_tests == sum(count for d, count in histogram.items()
                               if 1 < d < n)
    if first is not None:
        actual = gcd(n, traces[first["a"]]
                     + first["epsilon"] * traces[first["b"]])
        assert actual == int(first["gcd"]) and 1 < actual < n
    else:
        assert proper_tests == 0
    ordered_divisors = sorted(histogram)
    atoms = saturations_and_atoms(n, ordered_divisors)
    return {
        "sigma": sigma,
        "N": str(n),
        "tests": total,
        "histogram": [[str(d), histogram[d]] for d in ordered_divisors],
        "first_proper": first,
        "proper_tests": proper_tests,
        "support_atoms": [str(atom) for atom in atoms],
    }


def main():
    m = 125
    data = {
        "audit": "C-J-AURIFEUILIAN-INTERNAL-SEPARATION-N/R2-M125",
        "m": m,
        "h": 5 * m,
        "period": 10 * m,
        "cases": [inspect_side(m, sigma) for sigma in (-1, 1)],
    }
    print(json.dumps(data, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
