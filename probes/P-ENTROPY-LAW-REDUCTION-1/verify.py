#!/usr/bin/env python3
"""Exact audit for the proof-first probe P-ENTROPY-LAW-REDUCTION-1.

This verifier audits finite premises only. The written proof in PREREG.md
carries the universal measurable statement. No floating point is used.
Python standard library only.

Formal execution is forbidden before the public preregistration pin.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product

P = 5
State = tuple[int, int, int, int, int, int]

GATES: list[tuple[str, bool]] = []


def gate(tag: str, claim: str, ok: bool) -> None:
    GATES.append((tag, ok))
    print(f"{'PASS' if ok else 'FAIL'} {tag} {claim}")


def mod5(x: int) -> int:
    return x % P


def z6(x: State) -> int:
    return sum(x) % P


def gen_a(x: State) -> State:
    p1, p4, p1p, p4p, q, t = x
    return (p4, p1, p4p, p1p, q, t)


def gen_b(x: State) -> State:
    p1, p4, p1p, p4p, q, t = x
    return tuple(mod5(v) for v in (-p1p, -p4p, -p1, -p4, -q, -t))  # type: ignore[return-value]


def gen_c(x: State) -> State:
    p1, p4, p1p, p4p, q, t = x
    return tuple(
        mod5(v)
        for v in (
            -p1p + 2,
            -p4p + 1 + t,
            -p1 + 2,
            -p4 + 1 - t,
            1 - q,
            -t,
        )
    )  # type: ignore[return-value]


def gen_d(x: State) -> State:
    center = (2, 1, 3, 4, 1, 1)
    return tuple(mod5(c - v) for c, v in zip(center, x))  # type: ignore[return-value]


def gen_e(x: State) -> State:
    center = (2, 1, 3, 4, 2, 1)
    return tuple(mod5(c - v) for c, v in zip(center, x))  # type: ignore[return-value]


GENERATORS = (gen_a, gen_b, gen_c, gen_d, gen_e)


def branch(x: State, eps: int) -> State:
    index = (z6(x) + 2 * eps) % P
    return GENERATORS[index](x)


TRACE_TABLE = {
    0: (0, 4, 0, 4, 4),
    1: (2, 1, 1, 3, 1),
}


def trace_step(eps: int, z: int) -> int:
    return TRACE_TABLE[eps][z]


def apply_trace_word(word: str, z: int) -> int:
    for bit in word:
        z = trace_step(int(bit), z)
    return z


def sigma(word: str) -> str:
    return "".join("01" if bit == "0" else "10" for bit in word)


def sigma_power(word: str, exponent: int) -> str:
    for _ in range(exponent):
        word = sigma(word)
    return word


def factors(word: str, length: int) -> set[str]:
    return {word[i : i + length] for i in range(len(word) - length + 1)}


LEGAL_PAIRS = ("00", "01", "10", "11")

FROZEN_LENGTH9 = (
    "001011001",
    "001011010",
    "001100101",
    "001101001",
    "010010110",
    "010011001",
    "010110011",
    "010110100",
    "011001011",
    "011001101",
    "011010010",
    "011010011",
    "100101100",
    "100101101",
    "100110010",
    "100110100",
    "101001011",
    "101001100",
    "101100110",
    "101101001",
    "110010110",
    "110011010",
    "110100101",
    "110100110",
)


def matmul(a: tuple[tuple[int, ...], ...], b: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    rows = len(a)
    inner = len(b)
    cols = len(b[0])
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols))
        for i in range(rows)
    )


def det4(m: tuple[tuple[int, ...], ...]) -> int:
    total = 0
    for p0 in range(4):
        for p1 in range(4):
            if p1 == p0:
                continue
            for p2 in range(4):
                if p2 in (p0, p1):
                    continue
                p3 = 6 - p0 - p1 - p2
                perm = (p0, p1, p2, p3)
                inversions = sum(
                    1 for i in range(4) for j in range(i + 1, 4) if perm[i] > perm[j]
                )
                sign = -1 if inversions % 2 else 1
                total += sign * m[0][p0] * m[1][p1] * m[2][p2] * m[3][p3]
    return total


def pair_operator(v: tuple[Fraction, Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    a, b, c, d = v
    i_left = (Fraction(0), a + b, c + d, Fraction(0))
    block = (c, d, a, b)
    return tuple((i_left[k] + block[k]) / 2 for k in range(4))  # type: ignore[return-value]


def main() -> int:
    print("P-ENTROPY-LAW-REDUCTION-1")
    print("SCOPE exact finite audit of a proof-first Route A reduction")

    m_j = (
        (1, 0, -1, 1),
        (0, 1, -1, 0),
        (1, 0, 0, 0),
        (0, 1, -1, 1),
    )
    m_j_inv = (
        (0, 0, 1, 0),
        (-1, 0, 1, 1),
        (-1, -1, 1, 1),
        (0, -1, 0, 1),
    )
    identity = tuple(tuple(1 if i == j else 0 for j in range(4)) for i in range(4))
    gate(
        "A01",
        "J is a unit: det(M_J)=1 and the displayed integer inverse is exact",
        det4(m_j) == 1 and matmul(m_j, m_j_inv) == identity and matmul(m_j_inv, m_j) == identity,
    )

    all_states = [tuple(x) for x in product(range(P), repeat=6)]
    gate(
        "A02",
        "the five public generators are involutions on all 5^6 states",
        all(g(g(x)) == x for g in GENERATORS for x in all_states),
    )

    expected_generator_trace = (
        lambda z: z,
        lambda z: -z,
        lambda z: 2 - z,
        lambda z: 2 - z,
        lambda z: 3 - z,
    )
    gate(
        "A03",
        "the five generator trace laws hold on all 5^6 states",
        all(
            z6(g(x)) == expected_generator_trace[index](z6(x)) % P
            for index, g in enumerate(GENERATORS)
            for x in all_states
        ),
    )

    observed_sets = {
        eps: tuple(
            {z6(branch(x, eps)) for x in all_states if z6(x) == z}
            for z in range(P)
        )
        for eps in (0, 1)
    }
    observed_table = {
        eps: tuple(next(iter(values)) for values in observed_sets[eps])
        for eps in (0, 1)
    }
    gate(
        "A04",
        "the complete two-row public sheet table is exact",
        all(len(values) == 1 for rows in observed_sets.values() for values in rows)
        and observed_table == TRACE_TABLE,
    )

    pair_container = sigma_power("0", 3)
    gate(
        "A05",
        "all four two-letter factors occur in the Thue-Morse language",
        factors(pair_container, 2) == set(LEGAL_PAIRS),
    )

    language9 = set()
    for pair in LEGAL_PAIRS:
        language9.update(factors(sigma_power(pair, 4), 9))
    gate(
        "A06",
        "the level-4 two-supertile certificate gives exactly 24 length-9 factors",
        tuple(sorted(language9)) == FROZEN_LENGTH9 and len(language9) == 24,
    )

    reset_images = {
        word: tuple(apply_trace_word(word, z) for z in range(P)) for word in FROZEN_LENGTH9
    }
    gate(
        "A07",
        "every allowed length-9 factor synchronizes all five input sheets",
        all(len(set(image)) == 1 for image in reset_images.values()),
    )
    gate(
        "A08",
        "the synchronized sheet is 4+2 times the final bit modulo 5",
        all(image[0] == (4 + 2 * int(word[-1])) % P for word, image in reset_images.items()),
    )

    bad8 = "10100101"
    language8 = set()
    for pair in LEGAL_PAIRS:
        language8.update(factors(sigma_power(pair, 3), 8))
    gate(
        "A09",
        "length 9 is sharp: an allowed length-8 factor is not synchronizing",
        bad8 in language8
        and tuple(apply_trace_word(bad8, z) for z in range(P)) == (2, 1, 1, 1, 1),
    )

    pair_law = (
        Fraction(1, 6),
        Fraction(1, 3),
        Fraction(1, 3),
        Fraction(1, 6),
    )
    gate(
        "A10",
        "the public stationary pair law is normalized, symmetric, and fixed",
        sum(pair_law) == 1
        and pair_law[1] == pair_law[2]
        and pair_operator(pair_law) == pair_law,
    )

    pair_to_selector = {
        (0, 0): 4,
        (0, 1): 1,
        (1, 0): 1,
        (1, 1): 3,
    }
    gate(
        "A11",
        "the forced trace law gives the exact pair-to-selector map",
        all(
            pair_to_selector[(left, right)] == (4 + 2 * left + 2 * right) % P
            for left, right in product((0, 1), repeat=2)
        ),
    )

    selector_law = [Fraction(0) for _ in range(P)]
    for pair, mass in zip(((0, 0), (0, 1), (1, 0), (1, 1)), pair_law):
        selector_law[pair_to_selector[pair]] += mass
    gate(
        "A12",
        "the selector law is exactly (0,2/3,0,1/6,1/6)",
        tuple(selector_law)
        == (
            Fraction(0),
            Fraction(2, 3),
            Fraction(0),
            Fraction(1, 6),
            Fraction(1, 6),
        ),
    )

    window = tuple(range(512, 2048))
    gate(
        "A13",
        "the frozen window has 1536 terms and averages a time-independent law unchanged",
        len(window) == 1536
        and sum(Fraction(1, len(window)) for _ in window) == 1,
    )

    passed = sum(ok for _, ok in GATES)
    total = len(GATES)
    print(f"SUMMARY {passed}/{total} PASS")
    if passed != total:
        return 1
    print("RESULT FINITE PREMISES AUDITED; UNIVERSAL CLAIM REMAINS PROOF-FIRST")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
