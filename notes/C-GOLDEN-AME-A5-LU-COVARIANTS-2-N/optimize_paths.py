#!/usr/bin/env python3
"""Exact subset-DP contraction paths for the four generic n=4 cores."""

from __future__ import annotations

import json
import argparse
from functools import lru_cache


def factor_labels(triple):
    q = 0
    pi = [(0, 1, 2, 3)] + [tuple(p) for p in triple]
    inverse = []
    for ell in range(4):
        inv = {}
        domain = range(1, 4) if ell == q else range(4)
        for r in domain:
            inv[pi[ell][r]] = r
        inverse.append(inv)
    labels = []
    names = []
    for r in range(4):
        labels.append(frozenset(("open-row", q) if ell == q and r == 0 else ("wire", ell, r) for ell in range(4)))
        names.append(f"A{r}")
    for s in range(4):
        labels.append(frozenset(("open-col", q) if ell == q and s == 0 else ("wire", ell, inverse[ell][s]) for ell in range(4)))
        names.append(f"B{s}")
    return labels, names


def optimize(triple):
    factor, names = factor_labels(triple)
    n = len(factor)

    @lru_cache(None)
    def boundary(mask):
        counts = {}
        for i in range(n):
            if mask >> i & 1:
                for x in factor[i]:
                    counts[x] = counts.get(x, 0) + 1
        return frozenset(x for x, c in counts.items() if c == 1)

    dp = {}
    for i in range(n):
        dp[1 << i] = (4, 0, names[i])  # max rank, arithmetic cost, tree
    for size in range(2, n + 1):
        for mask in range(1, 1 << n):
            if mask.bit_count() != size:
                continue
            lowbit = mask & -mask
            best = None
            sub = (mask - 1) & mask
            while sub:
                other = mask ^ sub
                if other and sub & lowbit and sub in dp and other in dp:
                    shared = boundary(sub).intersection(boundary(other))
                    if shared:  # no outer products
                        out_rank = len(boundary(mask))
                        exponent = out_rank + len(shared)
                        maxrank = max(dp[sub][0], dp[other][0], out_rank)
                        cost = dp[sub][1] + dp[other][1] + 6**exponent
                        candidate = (maxrank, cost, f"({dp[sub][2]}*{dp[other][2]}|s={len(shared)},r={out_rank})")
                        if best is None or candidate[:2] < best[:2]:
                            best = candidate
                sub = (sub - 1) & mask
            if best is not None:
                dp[mask] = best
    return dp[(1 << n) - 1]


def main(classification):
    with open(classification, encoding="utf-8") as handle:
        data = json.load(handle)
    reps = [r for r in data["representatives"] if r["irreducible_no_double_edge"]]
    for i, row in enumerate(reps):
        score = optimize(row["permutations"])
        print(i, row["permutations"], "maxrank", score[0], "muladds", score[1], "path", score[2])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("classification")
    args = parser.parse_args()
    main(args.classification)
