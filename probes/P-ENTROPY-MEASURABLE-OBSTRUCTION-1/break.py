#!/usr/bin/env python3
"""Independent exact finite audit; the measurable theorem is in the proof.

Authored without reading or importing the accepted verifier. No scientific
execution is permitted before the public pin. Standard library only.
"""

from math import gcd


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def compose_affine(left, right, modulus=5):
    """Coefficients of left(right(x))."""
    a, b = left
    c, d = right
    return (a * c % modulus, (a * d + b) % modulus)


def crt_letter(parity, residue):
    choices = [j for j in range(10) if j % 2 == parity and j % 5 == residue]
    require(len(choices) == 1, "CRT uniqueness")
    return choices[0]


def substitution(j):
    return (j, (j + 1) % 10, (j - 1) % 10, j)


def alternating_binary_sum(n):
    answer, sign = 0, 1
    while n:
        n, digit = divmod(n, 2)
        answer += sign * digit
        sign = -sign
    return answer


def main():
    # Public generator trace and r-coordinate affine coefficients, a..e.
    # This checks compositions of coefficients rather than a point-update
    # implementation or an orbit copied from the accepted verifier.
    trace = ((1, 0), (-1, 0), (-1, 2), (-1, 2), (-1, 3))
    r_maps = ((1, 0), (-1, 0), (-1, 0), (-1, 1), (-1, 1))
    pairs = ((0, 0), (0, 1), (1, 0), (1, 1))
    for previous, current in pairs:
        z = (4 + 2 * previous) % 5
        generator = (z + 2 * current) % 5
        a, b = trace[generator]
        require((a * z + b) % 5 == (4 + 2 * current) % 5, "stable sheet")
        require(r_maps[generator] == (-1, int(previous == current)), "r cocycle")

    tower_cases = 0
    crt_cases = 0
    for previous, current in pairs:
        # Aligned Thue--Morse tower: preceding bit 1-previous,
        # current bit current, next bit 1-current.
        z = (4 + 2 * (1 - previous)) % 5
        first = (z + 2 * current) % 5
        a, b = trace[first]
        next_z = (a * z + b) % 5
        second = (next_z + 2 * (1 - current)) % 5
        d = previous ^ current
        combined = compose_affine(r_maps[second], r_maps[first])
        require(combined == (1, (-d) % 5), "tower affine composition")
        for r in range(5):
            next_r = (combined[0] * r + combined[1]) % 5
            q, next_q = (-r) % 5, (-next_r) % 5
            require(next_q == (q + d) % 5, "tower orientation")
            tower_cases += 1
            for u in range(5):
                beta = crt_letter(previous, (3 * q - 2 * u) % 5)
                next_beta = crt_letter(current, (3 * next_q - 2 * (u + 1)) % 5)
                require((next_beta - beta) % 10 == (3 * d - 2) % 10, "clock CRT")
                crt_cases += 1
    require((tower_cases, crt_cases) == (20, 100), "complete tower/CRT audit")

    # Exact adjacent-pair language closure. The primitive substitution's
    # internal pairs seed the language; substituted boundaries add all others.
    legal_pairs = set()
    for j in range(10):
        word = substitution(j)
        legal_pairs.update(zip(word, word[1:]))
    while True:
        expanded = legal_pairs | {
            (substitution(a)[-1], substitution(b)[0]) for a, b in legal_pairs
        }
        if expanded == legal_pairs:
            break
        legal_pairs = expanded
    expected_pairs = {(j, (j + step) % 10) for j in range(10) for step in (1, -2)}
    require(legal_pairs == expected_pairs, "complete adjacent-pair language")
    for a, b in legal_pairs:
        require((b - a) % 10 == (3 * ((a % 2) ^ (b % 2)) - 2) % 10,
                "Morse local increment")
    for j in range(10):
        word = substitution(j)
        parity = j % 2
        require(tuple(x % 2 for x in word) == (parity, 1 - parity, 1 - parity, parity),
                "projection to squared TM substitution")
        require(substitution((j + 2) % 10) == tuple((x + 2) % 10 for x in word),
                "vertical translation commutes with substitution")
        reached = {j}
        for depth in range(1, 6):
            reached = {x for letter in reached for x in substitution(letter)}
            if depth == 4:
                require(len(reached) == 9, "primitive depth-four boundary")
        require(reached == set(range(10)), "primitive power five")

    # Sparse integer witnesses, calculated from their binary digits rather
    # than by materializing any long substitution prefix.
    long_return = sum(4 ** k for k in range(10))
    require(long_return == (4 ** 10 - 1) // 3, "height witness identity")
    require(alternating_binary_sum(3) == 0, "height return three")
    require(alternating_binary_sum(long_return) == 10, "height second return")
    require(gcd(3, long_return) == 1, "height one")
    for parity in range(2):
        fiber = {crt_letter(parity, residue) for residue in range(5)}
        require(len(fiber) == 5, "five initial letters over parity")
        for j in fiber:
            require({(j + 2 * k) % 10 for k in range(5)} == fiber,
                    "transitive vertical fiber action")

    print("P-ENTROPY-MEASURABLE-OBSTRUCTION-1 independent breaker")
    print("native_pairs=4 tower_cases=20 crt_cases=100 PASS")
    print("morse_legal_pairs=20 primitive_power=5 exact_fiber=5 PASS")
    print("height_returns=3,349525 height_gcd=1 PASS")
    print("finite_audit=PASS measurable_scope=WRITTEN_PROOF")


if __name__ == "__main__":
    main()
