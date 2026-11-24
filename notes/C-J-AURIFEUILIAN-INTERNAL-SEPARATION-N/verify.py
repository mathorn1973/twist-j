"""Exact audit using sequence recurrences and quadratic coefficient pairs."""

from collections import Counter
from hashlib import sha256
import json
from math import gcd, isqrt


ONE = (1, 0)
PHI = (0, 1)


def sequence_values(first, second, last_index):
    values = [first, second]
    for _ in range(2, last_index + 1):
        values.append(values[-2] + values[-1])
    return values


def search_trace_sums(lucas, modulus):
    histogram = Counter()
    first_proper = None
    digest = sha256()

    for a in range(0, 249, 2):
        for b in range(1, 250, 2):
            for epsilon in (-1, 1):
                value = lucas[a] + epsilon * lucas[b]
                divisor = gcd(modulus, value)
                histogram[divisor] += 1
                digest.update(f"{a},{b},{epsilon},{divisor}\n".encode("ascii"))
                if first_proper is None and 1 < divisor < modulus:
                    first_proper = {
                        "a": a,
                        "b": b,
                        "epsilon": epsilon,
                        "value": value,
                        "gcd": divisor,
                    }

    tests = sum(histogram.values())
    if tests != 31250:
        raise ValueError("The prescribed trace domain has 31250 tests")
    return {
        "tests": tests,
        "gcd_histogram": sorted(histogram.items()),
        "first_proper": first_proper,
        "test_sha256": digest.hexdigest(),
    }


def multiply(left, right, modulus):
    a, b = left
    c, d = right
    # Reduce the product using phi squared = phi + 1.
    return ((a * c + b * d) % modulus, (a * d + b * c + b * d) % modulus)


def bounded_order(base, bound, modulus):
    power = ONE
    for exponent in range(1, bound + 1):
        power = multiply(power, base, modulus)
        if power == ONE:
            return exponent
    raise ValueError(f"No return for {base} modulo {modulus} through {bound}")


def is_prime_by_trial(value):
    return value >= 2 and all(
        value % divisor != 0 for divisor in range(2, isqrt(value) + 1)
    )


def audit_labels(prime):
    if not is_prime_by_trial(prime):
        raise ValueError(f"Published factor {prime} is not prime")

    phi_order = bounded_order(PHI, 250, prime)
    alpha = multiply(PHI, PHI, prime)
    alpha_order = bounded_order(alpha, 125, prime)

    powers = [ONE]
    for _ in range(1, 250):
        powers.append(multiply(powers[-1], PHI, prime))
    labels = [
        ((epsilon * a) % prime, (epsilon * b) % prime)
        for epsilon in (-1, 1)
        for a, b in powers
    ]
    indices = {value: index for index, value in enumerate(labels)}
    if len(indices) != 500:
        raise ValueError(f"The 500 formal labels are not distinct modulo {prime}")

    two = {(index,) for index, value in enumerate(labels) if value == ONE}
    three = set()
    for left_index, (a, b) in enumerate(labels):
        right_index = indices.get(((1 - a) % prime, -b % prime))
        if right_index is not None:
            three.add((left_index, right_index))

    factor_audit = {
        "p": prime,
        "prime_trial": True,
        "phi_order": phi_order,
        "alpha_order": alpha_order,
        "signed_labels": len(indices),
    }
    return factor_audit, two, three


def relation_digest(relations):
    digest = sha256()
    for indices in sorted(relations):
        row = ",".join(str(index) for index in indices)
        digest.update((row + "\n").encode("ascii"))
    return digest.hexdigest()


def compare_relations(left, right):
    difference = left ^ right
    first = min(difference, default=None)
    return {
        "counts": [len(left), len(right)],
        "sha256": [relation_digest(left), relation_digest(right)],
        "separators": len(difference),
        "first_separator": None if first is None else list(first),
    }


def main():
    m = 25
    fibonacci = sequence_values(0, 1, m)
    lucas = sequence_values(2, 1, 249)
    f_m = fibonacci[m]
    modulus = 5 * f_m * f_m + 5 * f_m + 1
    search_audit = search_trace_sums(lucas, modulus)

    p, q = 251, 112128001
    if p * q != modulus:
        raise ValueError("The published factor pair does not multiply to N")
    audit_p, two_p, three_p = audit_labels(p)
    audit_q, two_q, three_q = audit_labels(q)

    output = {
        "schema": "C-J-AURIFEUILIAN-INTERNAL-SEPARATION-N/v1",
        "input": {"m": m, "F_m": f_m, "N": modulus},
        "main": search_audit,
        "factor_audit": [audit_p, audit_q],
        "short_relations": {
            "two": compare_relations(two_p, two_q),
            "three": compare_relations(three_p, three_q),
        },
    }
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
