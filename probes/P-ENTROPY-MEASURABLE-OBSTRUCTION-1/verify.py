#!/usr/bin/env python3
"""Exact finite-premise audit for P-ENTROPY-MEASURABLE-OBSTRUCTION-1.

The all-measurable obstruction is proved in PROOF.md. No finite enumeration
in this file substitutes for its all-scale return-word argument or for the
measure-theoretic proof.
Python standard library only; integer arithmetic; no runtime source imports.
Do not execute or import before the public preregistration pin.
"""

from itertools import permutations, product
from math import gcd, prod


def require(condition, description):
    if not condition:
        raise AssertionError(description)


def generators(x):
    a, b, c, d, q, r = x
    raw = (
        (b, a, d, c, q, r),
        (-c, -d, -a, -b, -q, -r),
        (2-c, 1-d+r, 2-a, 1-b-r, 1-q, -r),
        (2-a, 1-b, 3-c, 4-d, 1-q, 1-r),
        (2-a, 1-b, 3-c, 4-d, 2-q, 1-r),
    )
    return tuple(tuple(v % 5 for v in image) for image in raw)


TRACE = ((0, 4, 0, 4, 4), (2, 1, 1, 3, 1))


def matrix_product(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def audit_unit():
    identity = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))
    # Multiplication by j in the basis (1,j,j^2,j^3), Phi_5(j)=0.
    c = ((0, 0, 0, -1), (1, 0, 0, -1),
         (0, 1, 0, -1), (0, 0, 1, -1))
    c2 = matrix_product(c, c)
    mj = tuple(tuple(identity[i][j]+c2[i][j] for j in range(4))
               for i in range(4))
    require(mj == ((1, 0, -1, 1), (0, 1, -1, 0),
                   (1, 0, 0, 0), (0, 1, -1, 1)), "J matrix")
    inverse = ((0, 0, 1, 0), (-1, 0, 1, 1),
               (-1, -1, 1, 1), (0, -1, 0, 1))
    require(matrix_product(mj, inverse) == identity
            and matrix_product(inverse, mj) == identity, "integer inverse")
    determinant = 0
    for permutation in permutations(range(4)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(4) for j in range(i+1, 4))
        determinant += (-1)**inversions * prod(mj[i][permutation[i]]
                                               for i in range(4))
    require(determinant == 1, "J determinant")
    current = identity
    for exponent in range(1, 21):
        current = tuple(tuple(value % 5 for value in row)
                        for row in matrix_product(current, mj))
        require((current == identity) == (exponent == 20), "J order modulo five")
    mj2 = matrix_product(mj, mj)
    current = identity
    for exponent in range(1, 11):
        current = tuple(tuple(value % 5 for value in row)
                        for row in matrix_product(current, mj2))
        require((current == identity) == (exponent == 10), "J squared order modulo five")


def audit_native():
    states = stable_steps = 0
    for x in product(range(5), repeat=6):
        states += 1
        z = sum(x) % 5
        images = generators(x)
        trace_laws = (z, -z, 2-z, 2-z, 3-z)
        for index, image in enumerate(images):
            require(generators(image)[index] == x, "native involution")
            require(sum(image) % 5 == trace_laws[index] % 5,
                    "native generator trace")
        for bit in (0, 1):
            image = images[(z+2*bit) % 5]
            require(sum(image) % 5 == TRACE[bit][z], "selector trace table")
            if z in (1, 4):
                previous = int(z == 1)
                require((z+2*bit) % 5 == ((4, 1), (1, 3))[previous][bit],
                        "stable selected generator")
                require(image[5] == (int(previous == bit)-x[5]) % 5,
                        "stable sixth-coordinate law")
                require(sum(image) % 5 == (4+2*bit) % 5,
                        "stable trace law")
                stable_steps += 1
    require(states == 15625 and stable_steps == 12500, "native audit coverage")


def tm_substitute(word):
    return tuple(value for bit in word for value in (bit, 1-bit))


def iterate(word, substitution, count):
    for _ in range(count):
        word = tuple(value for letter in word for value in substitution(letter))
    return word


def factors(word, length):
    return {word[i:i+length] for i in range(len(word)-length+1)}


def audit_synchronization():
    # Every length-nine factor fits in two length-sixteen supertiles.
    # All four underlying adjacent pairs occur already in mu^3(0).
    word = (0,)
    for _ in range(3):
        word = tm_substitute(word)
    pairs = factors(word, 2)
    require(pairs == set(product((0, 1), repeat=2)), "complete TM pairs")
    language = set()
    for pair in pairs:
        word = pair
        for _ in range(4):
            word = tm_substitute(word)
        language.update(factors(word, 9))
    require(len(language) == 24, "complete TM length-nine language")
    for word in language:
        images = []
        for initial in range(5):
            z = initial
            for bit in word:
                z = TRACE[bit][z]
            images.append(z)
        require(set(images) == {(4+2*word[-1]) % 5}, "trace synchronization")
        double_positions = {i % 2 for i in range(8) if word[i] == word[i+1]}
        require(len(double_positions) == 1, "unique local TM alignment")


def induced_increment(previous, current, r, wrong_sign=False):
    # mu(b) has entries (1-b_-1, b_0, 1-b_0) at positions -1,0,1.
    first = (int(1-previous == current)-r) % 5
    second = (int(current == 1-current)-first) % 5
    if wrong_sign:
        second = -second % 5
    return second


def audit_induction(wrong_sign=False):
    count = 0
    for previous, current, r in product(range(2), range(2), range(5)):
        difference = previous ^ current
        result = induced_increment(previous, current, r, wrong_sign)
        require(result == (r-difference) % 5, "induced two-step r law")
        require(-result % 5 == (-r+difference) % 5, "induced q law")
        count += 1
    require(count == 20, "induced audit coverage")


def sigma(letter):
    return (letter, (letter+1) % 10, (letter-1) % 10, letter)


def audit_substitution(substitution=sigma):
    for letter in range(10):
        image = substitution(letter)
        require(len(image) == 4 and all(0 <= x < 10 for x in image),
                "substitution carrier and length")
        expected_parity = tm_substitute(tm_substitute((letter % 2,)))
        require(tuple(x % 2 for x in image) == expected_parity, "TM parity factor")
        require(set(iterate((letter,), substitution, 5)) == set(range(10)),
                "sigma fifth power positive")
        for shift in range(0, 10, 2):
            require(substitution((letter+shift) % 10)
                    == tuple((x+shift) % 10 for x in image), "vertical symmetry")
    for level in range(6):
        block = iterate((0,), substitution, level)
        parent = iterate((0,), substitution, level+1)
        distance = 3*4**level
        require(parent[:len(block)] == block
                and parent[distance:distance+len(block)] == block,
                "equal return-word blocks at zero and three times four-power")
        require(gcd(distance, 5) == 1, "return distance coprime to five")


def audit_pairs():
    internal = {pair for letter in range(10) for pair in factors(sigma(letter), 2)}
    pairs = internal
    while True:
        expanded = pairs | {(sigma(a)[-1], sigma(b)[0]) for a, b in pairs}
        if expanded == pairs:
            break
        pairs = expanded
    expected = {(j, (j+delta) % 10) for j in range(10) for delta in (1, -2)}
    require(pairs == expected and len(pairs) == 20, "complete sigma pair language")
    for a, b in pairs:
        difference = (a % 2) ^ (b % 2)
        require((b-a) % 10 == (3*difference-2) % 10, "pair beta difference law")


def binary_alternating_sum(n):
    value, sign = 0, 1
    while n:
        value += sign*(n & 1)
        sign = -sign
        n //= 2
    return value


def base4_weight(n):
    value = 0
    while n:
        value += (0, 1, -1, 0)[n % 4]
        n //= 4
    return value


def audit_digits_and_height():
    bound = 65536
    b_values = [binary_alternating_sum(n) for n in range(bound+1)]
    s0 = [0]*(bound+1)
    for n in range(1, bound+1):
        s0[n] = n-s0[n//2]
    fixed_prefix = iterate((0,), sigma, 8)
    require(len(fixed_prefix) == bound, "fixed-prefix size")
    for n in range(bound):
        b = b_values[n]
        require(b == base4_weight(n), "binary/base-four digit identity")
        require(fixed_prefix[n] == b % 10, "sigma digit formula")
        require(b % 2 == n.bit_count() % 2, "digit TM parity")
        require(3*s0[n] == 2*n+b, "S0 digit identity")
        difference = (n.bit_count() ^ (n+1).bit_count()) & 1
        require(b_values[n+1]-b == 3*difference-2, "integer increment identity")
        require(b_values[2*(n//2)] == -b_values[n//2], "even digit recurrence")
    large_return = (4**10-1)//3
    require(large_return == 349525 and large_return % 3 == 1,
            "sparse return index")
    for n in (0, 3, large_return):
        require(binary_alternating_sum(n) == base4_weight(n), "sparse digit identity")
        require(base4_weight(n) % 10 == 0, "return to zero")
    require(base4_weight(large_return) == 10 and gcd(3, large_return) == 1,
            "height-one return witnesses")


def crt(parity, residue, drift=0):
    return (5*parity+6*residue+drift) % 10


def audit_crt(drift=0):
    count = 0
    for previous, current, q, u in product(range(2), range(2), range(5), range(5)):
        difference = previous ^ current
        beta = crt(previous, (3*q-2*u) % 5, drift)
        require(beta % 2 == previous and beta % 5 == (3*q-2*u) % 5,
                "CRT defining congruences")
        next_q, next_u = (q+difference) % 5, (u+1) % 5
        next_beta = crt(current, (3*next_q-2*next_u) % 5, drift)
        require((next_beta-beta) % 10 == (3*difference-2) % 10,
                "CRT cocycle law")
        count += 1
    require(count == 100, "CRT audit coverage")


def rejected(call):
    try:
        call()
    except AssertionError:
        return True
    return False


def audit_negative_controls():
    wrong_sigma = lambda j: (j, (j+2) % 10, (j-1) % 10, j)
    require(rejected(lambda: audit_substitution(wrong_sigma)), "wrong sigma rejected")
    require(rejected(lambda: audit_induction(wrong_sign=True)), "wrong cocycle rejected")
    require(rejected(lambda: audit_crt(drift=1)), "wrong CRT lift rejected")


def main():
    print("P-ENTROPY-MEASURABLE-OBSTRUCTION-1")
    gates = (
        ("A01", "integer J unit; mod-five orders 20 and 10 for J and J^2", audit_unit),
        ("A02", "15625 native states; involutions, traces and stable r law", audit_native),
        ("A03", "24 complete TM length-nine factors; synchronization and alignment", audit_synchronization),
        ("A04", "20 induced two-step r/q cases", audit_induction),
        ("A05", "sigma^5 primitive; parity, symmetries and six return-word levels", audit_substitution),
        ("A06", "20 complete adjacent pairs and exact beta difference law", audit_pairs),
        ("A07", "65536 digit/increment cases; coprime returns 3 and 349525", audit_digits_and_height),
        ("A08", "100 CRT cocycle transitions", audit_crt),
        ("A09", "three perturbed premises rejected", audit_negative_controls),
    )
    for tag, description, audit in gates:
        audit()
        print(f"PASS {tag} {description}")
    print("PASS finite-premise audit: 9/9")
    print("SCOPE full measurable obstruction: PROOF.md, not finite enumeration")


if __name__ == "__main__":
    main()
