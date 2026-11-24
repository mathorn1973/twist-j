#!/usr/bin/env python3
"""Independent exact implementation from PREREG.md, without verify.py access.

NON-CANONICAL, L1, one-architecture candidate-C audit only.
Sequences: independent integer matrix powers. Units: the cyclotomic quotient.
No scientific execution is permitted before the public source pin/readback.
"""

from hashlib import sha256
from json import dumps
from math import gcd


def matrix_product(a, b):
    return (
        a[0] * b[0] + a[1] * b[2],
        a[0] * b[1] + a[1] * b[3],
        a[2] * b[0] + a[3] * b[2],
        a[2] * b[1] + a[3] * b[3],
    )


def sequence_matrix(n):
    result = (1, 0, 0, 1)
    base = (1, 1, 1, 0)
    while n:
        if n & 1:
            result = matrix_product(result, base)
        base = matrix_product(base, base)
        n //= 2
    return result


def ring_product(a, b, modulus):
    terms = [0] * 7
    for i in range(4):
        for j in range(4):
            terms[i + j] += a[i] * b[j]
    # j^4 = -1-j-j^2-j^3, reducing from the highest power down.
    for degree in range(6, 3, -1):
        coefficient = terms[degree]
        for lower in range(degree - 4, degree):
            terms[lower] -= coefficient
        terms[degree] = 0
    return tuple(coefficient % modulus for coefficient in terms[:4])


def exact_order(element, bound, modulus):
    value = (1, 0, 0, 0)
    for exponent in range(1, bound + 1):
        value = ring_product(value, element, modulus)
        if value == (1, 0, 0, 0):
            return exponent
    raise AssertionError("No return within the preregistered bound")


def certify_prime(n):
    if n < 2:
        raise AssertionError("Alleged prime is below two")
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            raise AssertionError("Alleged prime has a trial divisor")
        divisor = 3 if divisor == 2 else divisor + 2


def encode_relation_set(relations):
    data = "".join(",".join(str(index) for index in row) + "\n"
                   for row in sorted(relations))
    return sha256(data.encode("ascii")).hexdigest()


def quotient_audit(prime):
    certify_prime(prime)
    phi = (0, 0, prime - 1, prime - 1)
    alpha = ring_product(phi, phi, prime)
    phi_order = exact_order(phi, 250, prime)
    alpha_order = exact_order(alpha, 125, prime)
    powers = []
    current = (1, 0, 0, 0)
    for _ in range(250):
        powers.append(current)
        current = ring_product(current, phi, prime)
    values = [tuple(sign * c % prime for c in power)
              for sign in (-1, 1) for power in powers]
    if len(set(values)) != 500:
        raise AssertionError("The common signed labels are not distinct")
    one = (1, 0, 0, 0)
    two = {(i,) for i, value in enumerate(values) if value == one}
    three = set()
    # Deliberately enumerate all ordered pairs; no complement lookup.
    for i, left in enumerate(values):
        for j, right in enumerate(values):
            if all((left[k] + right[k]) % prime == one[k]
                   for k in range(4)):
                three.add((i, j))
    return ({"p": prime, "prime_trial": True,
             "phi_order": phi_order, "alpha_order": alpha_order,
             "signed_labels": len(set(values))}, two, three)


def compare_relations(first, second):
    difference = sorted(first ^ second)
    return {"counts": [len(first), len(second)],
            "sha256": [encode_relation_set(first),
                       encode_relation_set(second)],
            "separators": len(difference),
            "first_separator": list(difference[0]) if difference else None}


def main():
    m = 25
    f = sequence_matrix(m)[1]
    n = 5 * f * f + 5 * f + 1
    lucas = []
    for index in range(250):
        matrix = sequence_matrix(index)
        lucas.append(matrix[0] + matrix[3])
    counts = {}
    first = None
    digest = sha256()
    tests = 0
    for a in range(0, 250, 2):
        for b in range(1, 250, 2):
            for epsilon in (-1, 1):
                value = lucas[a] + epsilon * lucas[b]
                divisor = gcd(n, value)
                counts[divisor] = counts.get(divisor, 0) + 1
                digest.update(f"{a},{b},{epsilon},{divisor}\n".encode("ascii"))
                tests += 1
                if first is None and 1 < divisor < n:
                    first = {"a": a, "b": b, "epsilon": epsilon,
                             "value": value, "gcd": divisor}
    if tests != 31250:
        raise AssertionError("Wrong exhaustive domain")
    # These published factors enter only the auxiliary audit after the search.
    p, q = 251, 112128001
    if p * q != n:
        raise AssertionError("Published factor product is incorrect")
    left = quotient_audit(p)
    right = quotient_audit(q)
    result = {
        "schema": "C-J-AURIFEUILIAN-INTERNAL-SEPARATION-N/v1",
        "input": {"m": m, "F_m": f, "N": n},
        "main": {"tests": tests,
                 "gcd_histogram": [[d, counts[d]] for d in sorted(counts)],
                 "first_proper": first, "test_sha256": digest.hexdigest()},
        "factor_audit": [left[0], right[0]],
        "short_relations": {"two": compare_relations(left[1], right[1]),
                            "three": compare_relations(left[2], right[2])},
    }
    print(dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
