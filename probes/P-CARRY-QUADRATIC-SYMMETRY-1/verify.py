#!/usr/bin/env python3
"""Exact audit for P-CARRY-QUADRATIC-SYMMETRY-1.

The all-n theorem is proved in PREREG.md. This program audits finite carriers,
the n=4 full-symmetry action, and the exact boundary inequalities. It is not
the basis of theorem status.
"""

from math import comb, factorial


def q_weight(w: int) -> int:
    return comb(w, 2) & 1


def q_word(x: int) -> int:
    return q_weight(x.bit_count())


def singular_nonzero(n: int) -> list[int]:
    return [x for x in range(1, 1 << n) if q_word(x) == 0]


def gf2_rank(vectors: list[int]) -> int:
    basis: dict[int, int] = {}
    for value in vectors:
        x = value
        while x:
            p = x.bit_length() - 1
            if p in basis:
                x ^= basis[p]
            else:
                basis[p] = x
                break
    return len(basis)


def apply_columns(columns: tuple[int, ...], x: int) -> int:
    out = 0
    for i, column in enumerate(columns):
        if (x >> i) & 1:
            out ^= column
    return out


def gl_order(n: int) -> int:
    out = 1
    for i in range(n):
        out *= (1 << n) - (1 << i)
    return out


def pure_quadratic_invariant_count(n: int) -> int:
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    index = {pair: k for k, pair in enumerate(pairs)}
    invariant = 0
    for mask in range(1 << len(pairs)):
        ok = True
        for s in range(n - 1):
            def perm(i: int) -> int:
                if i == s:
                    return s + 1
                if i == s + 1:
                    return s
                return i

            for k, (i, j) in enumerate(pairs):
                a, b = sorted((perm(i), perm(j)))
                kk = index[(a, b)]
                if ((mask >> k) & 1) != ((mask >> kk) & 1):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            invariant += 1
    return invariant


def automorphisms_q4() -> tuple[int, set[tuple[int, ...]]]:
    n = 4
    points = [1, 2, 4, 8, 15]
    point_index = {x: i for i, x in enumerate(points)}
    count = 0
    induced: set[tuple[int, ...]] = set()

    nonzero = list(range(1, 1 << n))
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
                    if any(q_word(apply_columns(columns, x)) != q_word(x)
                           for x in range(1 << n)):
                        continue
                    count += 1
                    image = tuple(point_index[apply_columns(columns, x)]
                                  for x in points)
                    induced.add(image)
    return count, induced


def main() -> int:
    # G01. Pure quadratic S_n invariants: only zero and e_2 in audited widths.
    for n in range(2, 6):
        assert pure_quadratic_invariant_count(n) == 2
    print("PASS G01 pure quadratic S_n-invariant space has dimension one for n=2..5")

    # G02. Lucas carry hierarchy: e_(2^r) is binary digit r of popcount.
    for w in range(256):
        for r in range(4):
            degree = 1 << r
            assert (comb(w, degree) & 1) == ((w >> r) & 1)
    print("PASS G02 Lucas carry layers e_1,e_2,e_4,e_8 audited for w=0..255")

    # G03. Exact least period four of the second carry bit.
    seq = [q_weight(w) for w in range(256)]
    assert seq[:4] == [0, 0, 1, 1]
    for w in range(252):
        assert seq[w + 4] == seq[w]
    for period in (1, 2, 3):
        assert any(seq[w + period] != seq[w]
                   for w in range(256 - period))
    print("PASS G03 second carry bit has exact least weight period 4=2^2")

    # G04. First non-atomic singular birth and five-point locus.
    for n in (2, 3):
        atoms = {1 << i for i in range(n)}
        assert set(singular_nonzero(n)) == atoms
    p4 = singular_nonzero(4)
    assert p4 == [1, 2, 4, 8, 15]
    assert set(p4) - {1, 2, 4, 8} == {15}
    xor_all = 0
    for x in p4:
        xor_all ^= x
    assert xor_all == 0
    print("PASS G04 first non-atomic singular arity is 4 and P_4 has 5 points")

    # G05. Full n=4 automorphism group and full symmetric action.
    count, induced = automorphisms_q4()
    assert count == 120
    assert len(induced) == factorial(5) == 120
    print("PASS G05 Aut(q_4) has order 120 and induces every permutation of P_4")

    # G06. Exact small-boundary order obstructions n=5,6,7.
    expected_counts = {5: 11, 6: 27, 7: 63}
    for n, expected in expected_counts.items():
        m = len(singular_nonzero(n))
        assert m == expected
        assert gl_order(n) < factorial(m)
    print("PASS G06 group-order obstruction excludes full singular symmetry at n=5,6,7")

    # G07. All-large-n proof boundary audit.
    for n in range(8, 65):
        assert comb(n, 4) >= n * n + 2
        # |GL(n,2)| < 2^(n^2), while m! >= 2^(m-1) for m>=2.
        m_lower = comb(n, 4)
        assert m_lower - 1 >= n * n + 1
    print("PASS G07 binom(n,4)>=n^2+2 audited for n=8..64")

    # G08. Declared collision only, never used by G01-G07.
    assert 5 == (1 << 2) + 1
    assert pow(2, 2, 5) == 4
    assert pow(2, 4, 5) == 1
    print("PASS G08 collision control only: 5=2^2+1 and ord_5(2)=4")

    print("RESULT 8/8 ALL PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
