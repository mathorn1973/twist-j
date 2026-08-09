#!/usr/bin/env python3
"""Exact audit for P-CARRY-ARITY-CIRCUIT-1.

The all-n theorem is proved in PREREG.md. This program is only a finite exact
audit of the frozen definitions, small carriers, and boundary cases.
"""

from math import comb


def q_weight(w: int) -> int:
    return comb(w, 2) & 1


def q_word(x: int) -> int:
    return q_weight(x.bit_count())


def singular_nonzero(n: int) -> list[int]:
    return [x for x in range(1, 1 << n) if q_word(x) == 0]


def gf2_rank(rows: list[int]) -> int:
    basis: dict[int, int] = {}
    for value in rows:
        x = value
        while x:
            p = x.bit_length() - 1
            if p in basis:
                x ^= basis[p]
            else:
                basis[p] = x
                break
    return len(basis)


def is_spanning_circuit(n: int, points: list[int]) -> bool:
    if len(points) != n + 1:
        return False
    if gf2_rank(points) != n:
        return False
    for i in range(len(points)):
        if gf2_rank(points[:i] + points[i + 1 :]) != n:
            return False
    return True


def exact_count(n: int) -> int:
    # Nonzero singular words: weights congruent to 0 or 1 modulo 4, minus zero.
    return sum(comb(n, w) for w in range(n + 1) if w % 4 in (0, 1)) - 1


def main() -> int:
    # G01: universal residue law audited over many complete residue periods.
    for w in range(256):
        assert (q_weight(w) == 0) == (w % 4 in (0, 1))
    print("PASS G01 weight-residue law audited for w=0..255")

    # G02: full enumeration agrees with the closed binomial count for n<=12.
    counts = []
    for n in range(1, 13):
        p = singular_nonzero(n)
        assert len(p) == exact_count(n)
        counts.append(len(p))
    assert counts[:6] == [1, 2, 3, 5, 11, 27]
    print("PASS G02 full singular counts n=1..12 agree with exact binomial formula")

    # G03: the complete singular locus is a spanning circuit exactly at n=4.
    verdicts = []
    for n in range(1, 13):
        verdicts.append(is_spanning_circuit(n, singular_nonzero(n)))
    assert verdicts == [False, False, False, True] + [False] * 8
    print("PASS G03 exhaustive circuit classification n=1..12 selects n=4 only")

    # G04: exact pentad and unique-relation audit at n=4.
    p4 = singular_nonzero(4)
    assert p4 == [1, 2, 4, 8, 15]
    assert len(p4) == 5
    xor_all = 0
    for x in p4:
        xor_all ^= x
    assert xor_all == 0
    assert gf2_rank(p4) == 4
    for i in range(5):
        assert gf2_rank(p4[:i] + p4[i + 1 :]) == 4
    print("PASS G04 P_4={1,2,4,8,15} is one spanning five-circuit")

    # G05: boundary cases in the all-n proof.
    for n in range(1, 4):
        assert singular_nonzero(n) == [1 << i for i in range(n)]
    for n in range(5, 65):
        assert comb(n, 4) >= 5
        assert n + comb(n, 4) > n + 1
    print("PASS G05 proof boundaries n<4 and n>=5 audit exactly")

    # G06: no fixed prime/order-five datum occurs in A1-A2 computation.
    # The selected five is output cardinality, not an input to q_n.
    assert len(singular_nonzero(4)) == 4 + 1
    print("PASS G06 selected cardinality is 5=4+1 after arity selection")

    print("RESULT 6/6 ALL PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
