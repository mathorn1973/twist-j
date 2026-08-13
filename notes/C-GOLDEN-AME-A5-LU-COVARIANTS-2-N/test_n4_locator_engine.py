#!/usr/bin/env python3
"""Generic-data tests only; this file never reads the golden tensor."""

from __future__ import annotations

import itertools

import numpy as np

import n4_locator_engine as engine


def direct_sparse(A, B, q, core):
    matchings = [None] * 4
    matchings[q] = engine.IDENTITY
    for ell, p in zip((x for x in range(4) if x != q), core):
        matchings[ell] = p
    support_a = [(x, int(A[x])) for x in itertools.product(range(6), repeat=4) if A[x] % engine.P]
    lookup_b = {x: int(B[x]) for x in itertools.product(range(6), repeat=4) if B[x] % engine.P}
    result = np.zeros((6, 6), dtype=np.int64)
    for entries in itertools.product(support_a, repeat=4):
        xs = tuple(x for x, _ in entries)
        product_a = 1
        for _, value in entries:
            product_a = product_a * value % engine.P
        ys = [[None] * 4 for _ in range(4)]
        for ell in range(4):
            domain = range(1, 4) if ell == q else range(4)
            for r in domain:
                ys[matchings[ell][r]][ell] = xs[r][ell]
        row = xs[0][q]
        for col in range(6):
            ys[0][q] = col
            values_b = []
            for y in ys:
                value = lookup_b.get(tuple(y))
                if value is None:
                    break
                values_b.append(value)
            else:
                product = product_a
                for value in values_b:
                    product = product * value % engine.P
                result[row, col] = (result[row, col] + product) % engine.P
    return result


def main():
    rng = np.random.default_rng(36604)
    for trial, support_size in enumerate((5, 7)):
        A = np.zeros((6, 6, 6, 6), dtype=np.int64)
        B = np.zeros_like(A)
        locations_a = rng.choice(6**4, size=support_size, replace=False)
        locations_b = rng.choice(6**4, size=support_size + 1, replace=False)
        A.reshape(-1)[locations_a] = rng.integers(1, 41, size=support_size)
        B.reshape(-1)[locations_b] = rng.integers(1, 41, size=support_size + 1)
        for q, core_index in ((0, 0), (1, 1), (2, 2), (3, 3)):
            fast = engine.core_covariant(A, B, q, engine.CORES[core_index])
            slow = direct_sparse(A, B, q, engine.CORES[core_index])
            if not np.array_equal(fast, slow):
                raise AssertionError((trial, q, core_index, fast, slow))
    print("PASS generic sparse direct-order cross-check: 8 matrices")

    # The four core orbits are fixed by componentwise inversion up to dummy
    # copy relabeling.  Audit the resulting star identity on independent A,B.
    for q in range(4):
        for core_index, core in enumerate(engine.CORES):
            left = engine.core_covariant(A, B, q, core)
            right = engine.core_covariant(B, A, q, core).T % engine.P
            if not np.array_equal(left, right):
                raise AssertionError(("star", q, core_index))
    print("PASS generic graph-star identity: 16 matrices")


if __name__ == "__main__":
    main()
