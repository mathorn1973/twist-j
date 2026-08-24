#!/usr/bin/env python3
"""Exact audit for P-CARRY-QUADRATIC-SYMMETRY-2.

The all-n theorem is proved in PREREG.md. This program audits the frozen
finite carriers, the n=4 full-symmetry action, and the exact boundary
inequalities. It is not the basis of theorem status.
"""

from itertools import permutations
from math import comb, factorial


class VerificationError(RuntimeError):
    """Raised when one frozen exact requirement fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def q_weight(weight: int) -> int:
    return comb(weight, 2) & 1


def q_residue(weight: int) -> int:
    return 0 if weight % 4 in (0, 1) else 1


def q_pair_polynomial(n: int, x: int) -> int:
    value = 0
    for i in range(n):
        x_i = (x >> i) & 1
        for j in range(i + 1, n):
            value ^= x_i & ((x >> j) & 1)
    return value


def adjacent_pair_orbits(n: int) -> tuple[frozenset[tuple[int, int]], ...]:
    pairs = {(i, j) for i in range(n) for j in range(i + 1, n)}
    remaining = set(pairs)
    orbits: list[frozenset[tuple[int, int]]] = []

    while remaining:
        seed = min(remaining)
        orbit = {seed}
        frontier = [seed]
        while frontier:
            i, j = frontier.pop()
            for swap in range(n - 1):
                def image(index: int) -> int:
                    if index == swap:
                        return swap + 1
                    if index == swap + 1:
                        return swap
                    return index

                transformed = tuple(sorted((image(i), image(j))))
                if transformed not in orbit:
                    orbit.add(transformed)
                    frontier.append(transformed)
        require(orbit <= pairs, f"Q1A orbit escaped coefficient pairs at n={n}")
        orbits.append(frozenset(orbit))
        remaining -= orbit

    return tuple(orbits)


def gf2_rank(vectors: list[int]) -> int:
    basis: dict[int, int] = {}
    for value in vectors:
        x = value
        while x:
            pivot = x.bit_length() - 1
            if pivot in basis:
                x ^= basis[pivot]
            else:
                basis[pivot] = x
                break
    return len(basis)


def apply_columns(columns: tuple[int, ...], x: int) -> int:
    image = 0
    for i, column in enumerate(columns):
        if (x >> i) & 1:
            image ^= column
    return image


def gl_order(n: int) -> int:
    value = 1
    for i in range(n):
        value *= (1 << n) - (1 << i)
    return value


def enumerate_complete_carriers() -> tuple[dict[int, tuple[int, ...]], int]:
    carriers: dict[int, tuple[int, ...]] = {}
    vectors_checked = 0

    for n in range(2, 11):
        singular: list[int] = []
        for x in range(1 << n):
            weight = x.bit_count()
            polynomial_value = q_pair_polynomial(n, x)
            binomial_value = q_weight(weight)
            residue_value = q_residue(weight)
            require(
                polynomial_value == binomial_value == residue_value,
                f"Q2B carrier mismatch at n={n}, x={x}",
            )
            if x != 0 and polynomial_value == 0:
                singular.append(x)
            vectors_checked += 1
        carriers[n] = tuple(singular)

    return carriers, vectors_checked


def automorphisms_q4() -> tuple[int, set[tuple[int, ...]]]:
    n = 4
    points = (1, 2, 4, 8, 15)
    point_index = {x: i for i, x in enumerate(points)}
    count = 0
    induced: set[tuple[int, ...]] = set()
    nonzero = range(1, 1 << n)

    for c0 in nonzero:
        for c1 in nonzero:
            if gf2_rank([c0, c1]) != 2:
                continue
            for c2 in nonzero:
                if gf2_rank([c0, c1, c2]) != 3:
                    continue
                for c3 in nonzero:
                    columns = (c0, c1, c2, c3)
                    if gf2_rank(list(columns)) != 4:
                        continue
                    preservation_checks = tuple(
                        q_pair_polynomial(n, apply_columns(columns, x))
                        == q_pair_polynomial(n, x)
                        for x in range(1 << n)
                    )
                    require(
                        len(preservation_checks) == 16,
                        "Q3A did not test all 16 vectors",
                    )
                    if not all(preservation_checks):
                        continue
                    count += 1
                    induced.add(
                        tuple(
                            point_index[apply_columns(columns, x)]
                            for x in points
                        )
                    )

    return count, induced


def main() -> int:
    # Q1A. Adjacent transpositions generate one orbit on coefficient pairs.
    for n in range(2, 11):
        orbits = adjacent_pair_orbits(n)
        require(len(orbits) == 1, f"Q1A expected one pair orbit at n={n}")
        require(
            len(orbits[0]) == comb(n, 2),
            f"Q1A incomplete pair orbit at n={n}",
        )
        require(
            1 << len(orbits) == 2,
            f"Q1A invariant coefficient space is not one-dimensional at n={n}",
        )
    print("PASS Q1A coefficient-orbit uniqueness audited for n=2..10")

    # Q1B. Lucas carry layers agree with the corresponding binary digits.
    for weight in range(256):
        for r in range(4):
            degree = 1 << r
            require(
                (comb(weight, degree) & 1) == ((weight >> r) & 1),
                f"Q1B Lucas mismatch at w={weight}, r={r}",
            )
    print("PASS Q1B Lucas carry layers e_1,e_2,e_4,e_8 audited for w=0..255")

    # Q2A. The second carry bit has block 0011 and no shorter period.
    sequence = [q_weight(weight) for weight in range(256)]
    require(sequence[:4] == [0, 0, 1, 1], "Q2A wrong period block")
    for weight in range(252):
        require(
            sequence[weight + 4] == sequence[weight],
            f"Q2A period four failed at w={weight}",
        )
    for period in (1, 2, 3):
        require(
            any(
                sequence[weight + period] != sequence[weight]
                for weight in range(256 - period)
            ),
            f"Q2A period {period} unexpectedly survived",
        )
    print("PASS Q2A second carry bit has exact least weight period 4=2^2")

    # Q2B. Visit every vector in every frozen Boolean carrier directly.
    carriers, vectors_checked = enumerate_complete_carriers()
    require(vectors_checked == 2044, "Q2B did not visit exactly 2044 vectors")
    require(set(carriers) == set(range(2, 11)), "Q2B carrier widths incomplete")
    print(
        "PASS Q2B complete Boolean carriers audited for every x in F_2^n, "
        "n=2..10 (2044 vectors)"
    )

    # Q2C. Check the first non-atomic singular birth and complete P_4 locus.
    for n in (2, 3):
        atoms = {1 << i for i in range(n)}
        require(set(carriers[n]) == atoms, f"Q2C non-atomic point before n=4 at n={n}")
    p4 = carriers[4]
    require(p4 == (1, 2, 4, 8, 15), "Q2C wrong P_4 locus")
    require(set(p4) - {1, 2, 4, 8} == {15}, "Q2C wrong non-atomic P_4 point")
    xor_all = 0
    for x in p4:
        xor_all ^= x
    require(xor_all == 0, "Q2C P_4 vectors do not sum to zero")
    print("PASS Q2C first non-atomic singular arity is 4 and P_4 has 5 points")

    # Q3A. Enumerate GL(4,2) and compare the induced action with all 5! maps.
    automorphism_count, induced = automorphisms_q4()
    all_permutations = set(permutations(range(5)))
    require(automorphism_count == 120, "Q3A wrong Aut(q_4) order")
    require(induced == all_permutations, "Q3A induced action is not exactly Sym(P_4)")
    print("PASS Q3A Aut(q_4) has order 120 and induces every permutation of P_4")

    # Q3B. Consume the direct carriers for every frozen small-boundary width.
    expected_counts = {5: 11, 6: 27, 7: 63, 8: 135, 9: 271, 10: 527}
    for n, expected in expected_counts.items():
        carrier_size = len(carriers[n])
        require(carrier_size == expected, f"Q3B wrong singular count at n={n}")
        require(
            gl_order(n) < factorial(carrier_size),
            f"Q3B order obstruction failed at n={n}",
        )
    print("PASS Q3B exact carrier counts and order obstruction audited for n=5..10")

    # Q3C. Audit every algebraic component of the all-large-n induction bound.
    require(comb(8, 4) >= 8 * 8 + 2, "Q3C induction base failed")
    for n in range(8, 65):
        require(
            comb(n, 4) >= n * n + 2,
            f"Q3C lower bound failed at n={n}",
        )
        require(
            comb(n + 1, 4) - comb(n, 4) == comb(n, 3),
            f"Q3C binomial difference identity failed at n={n}",
        )
        require(
            comb(n, 3) >= 2 * n + 1,
            f"Q3C induction increment failed at n={n}",
        )
        require(
            comb(n, 4) - 1 >= n * n + 1,
            f"Q3C factorial exponent boundary failed at n={n}",
        )
    print("PASS Q3C binom(n,4)>=n^2+2 and induction step audited for n=8..64")

    # C01. Declared collision only; never an input to Q1-Q3.
    require(5 == (1 << 2) + 1, "C01 cardinality identity failed")
    residues = [pow(2, exponent, 5) for exponent in range(1, 5)]
    require(residues[-1] == 1, "C01 fourth power is not one modulo five")
    require(1 not in residues[:-1], "C01 multiplicative order is below four")
    print("PASS C01 collision control only: 5=2^2+1 and ord_5(2)=4")

    print("RESULT 9/9 ALL PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
