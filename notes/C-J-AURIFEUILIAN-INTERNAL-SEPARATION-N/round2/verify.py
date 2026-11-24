#!/usr/bin/env python3
"""Prospective m=125 trace-menu audit using forward recurrences.

NON-CANONICAL; finite candidate-C evidence only. The companion PREREG.md
fixes the admitted domain and scientific stdout.
"""

import json
from collections import Counter
from math import gcd, prod


def fibonacci(index):
    previous, current = 0, 1
    for _ in range(index):
        previous, current = current, previous + current
    return previous


def lucas_residues(count, modulus):
    values = [2 % modulus, 1 % modulus]
    for _ in range(2, count):
        values.append((values[-2] + values[-1]) % modulus)
    return values[:count]


def support_partition(modulus, observed_divisors):
    saturations = [
        gcd(modulus, pow(divisor, modulus.bit_length(), modulus))
        for divisor in observed_divisors
    ]
    atoms = [modulus]
    for support in saturations:
        refined = []
        for atom in atoms:
            common = gcd(atom, support)
            if common == 1 or common == atom:
                refined.append(atom)
            else:
                refined.extend((common, atom // common))
        atoms = sorted(refined)
    assert all(atom > 1 for atom in atoms)
    assert prod(atoms) == modulus
    for index, atom in enumerate(atoms):
        assert all(gcd(atom, other) == 1 for other in atoms[index + 1 :])
        assert all(gcd(atom, support) in (1, atom) for support in saturations)
    return atoms


def inspect_side(fibonacci_value, sigma, period, h):
    modulus = 5 * fibonacci_value * fibonacci_value + 5 * sigma * fibonacci_value + 1
    lucas = lucas_residues(period, modulus)
    histogram = Counter()
    first_proper = None
    tests = 0
    for a in range(0, period, 2):
        for b in range(1, period, 2):
            for epsilon in (-1, 1):
                divisor = gcd(modulus, lucas[a] + epsilon * lucas[b])
                histogram[divisor] += 1
                tests += 1
                if first_proper is None and 1 < divisor < modulus:
                    first_proper = {
                        "a": a, "b": b, "epsilon": epsilon, "gcd": str(divisor)
                    }
    expected_tests = 2 * h * h
    assert expected_tests == 781250
    assert tests == expected_tests
    assert sum(histogram.values()) == expected_tests
    assert all(modulus % divisor == 0 for divisor in histogram)
    proper_tests = sum(
        count for divisor, count in histogram.items() if 1 < divisor < modulus
    )
    assert (first_proper is None) == (proper_tests == 0)
    if first_proper is not None:
        a, b = first_proper["a"], first_proper["b"]
        epsilon = first_proper["epsilon"]
        recorded = int(first_proper["gcd"])
        assert a in range(0, period, 2)
        assert b in range(1, period, 2)
        assert epsilon in (-1, 1)
        assert 1 < recorded < modulus
        assert recorded == gcd(modulus, lucas[a] + epsilon * lucas[b])
    ordered_divisors = sorted(histogram)
    atoms = support_partition(modulus, ordered_divisors)
    if proper_tests == 0:
        assert atoms == [modulus]
    return {
        "sigma": sigma,
        "N": str(modulus),
        "tests": tests,
        "histogram": [[str(d), histogram[d]] for d in ordered_divisors],
        "first_proper": first_proper,
        "proper_tests": proper_tests,
        "support_atoms": [str(atom) for atom in atoms],
    }


def main():
    m = 125
    h = 5 * m
    period = 2 * h
    value = fibonacci(m)
    cases = [inspect_side(value, sigma, period, h) for sigma in (-1, 1)]
    assert sum(case["tests"] for case in cases) == 1562500
    result = {
        "audit": "C-J-AURIFEUILIAN-INTERNAL-SEPARATION-N/R2-M125",
        "m": m,
        "h": h,
        "period": period,
        "cases": cases,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
