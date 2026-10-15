#!/usr/bin/env python3
"""Exact geometry reconciliation, NON-CANONICAL / L1.

Copyright 2026 A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
No scientific import or execution before the public preregistration pin.
Two different finite algorithms, one author: no blind-agent claim.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path
import json
import sys

Point = tuple[int, int, int]
Y: tuple[Point, ...] = ((0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1), (2, 0, 0))
WEIGHTS = {2: 6, 4: 1, 8: 15, 10: 1, 16: 1}
REPRESENTATIVES: tuple[Point, ...] = ((1, 1, 0), (2, 0, 0), (2, 2, 0), (3, 1, 0), (4, 0, 0))
ZERO: Point = (0, 0, 0)


def add(a: Point, b: Point) -> Point:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def norm_stencil() -> set[Point]:
    """A: exhaustive cube with the literal squared-norm/even-lattice predicate."""
    return {d for d in product(range(-4, 5), repeat=3)
            if sum(d) % 2 == 0 and sum(c * c for c in d) in WEIGHTS}


def orbit_stencil() -> set[Point]:
    """B: complete signed permutation orbits of the five shell representatives."""
    result: set[Point] = set()
    for representative in REPRESENTATIVES:
        for axes in permutations(representative):
            for signs in product((-1, 1), repeat=3):
                result.add(tuple(axes[i] * signs[i] for i in range(3)))
    return result


def literal_member(d: Point) -> bool:
    # Independently spell the predicate for the second-step remainder.
    a, b, c = d
    return (a + b + c) % 2 == 0 and a * a + b * b + c * c in (0, 2, 4, 8, 10, 16)


def membership_domain(offsets: set[Point]) -> tuple[set[Point], int]:
    """B: inspect every point in a proved containing box, not a sum-set output."""
    found: set[Point] = set()
    visited = 0
    for p in product(range(-8, 11), range(-8, 10), range(-8, 10)):
        visited += 1
        # Witness p=y+d+e. All y and d are inspected, e is tested directly.
        belongs = any(literal_member((p[0] - y[0] - d[0],
                                      p[1] - y[1] - d[1],
                                      p[2] - y[2] - d[2]))
                      for y in Y for d in offsets)
        if belongs:
            found.add(p)
    return found, visited


def table_bytes(points: set[Point]) -> bytes:
    return ("x\ty\tz\n" + "".join(f"{a}\t{b}\t{c}\n" for a, b, c in sorted(points))).encode("ascii")


def custody() -> None:
    here = Path(__file__).resolve().parent
    for row in (here / "CODE_SHA256SUMS").read_text(encoding="ascii").splitlines():
        digest, name = row.split("  ", 1)
        if sha256((here / name).read_bytes()).hexdigest() != digest:
            raise RuntimeError("frozen dependency mismatch: " + name)


def main() -> None:
    print("SCOPE NON-CANONICAL L1 primary-D3-two-step-domain target-exposed")
    stencil_a = norm_stencil()
    stencil_b = orbit_stencil()
    require(stencil_a == stencil_b, "stencil construction disagreement")
    shell_counts = Counter(sum(x * x for x in d) for d in stencil_a)
    require(dict(shell_counts) == {2: 12, 4: 6, 8: 12, 10: 24, 16: 6}, "incomplete shell orbits")
    require(all(tuple(-x for x in d) in stencil_a for d in stencil_a), "stencil not symmetric")
    weighted_sum = sum(WEIGHTS[sum(x * x for x in d)] for d in stencil_a)
    require(weighted_sum == 288, "full Dirichlet diagonal changed")
    b0_a = stencil_a | {ZERO}
    b0_b = stencil_b | {ZERO}
    # A: forward Minkowski construction; no fixed list or answer table.
    one_step = {add(y, d) for y in Y for d in b0_a}
    two_offsets = {add(d, e) for d in b0_a for e in b0_a}
    domain_a = {add(q, e) for q in one_step for e in b0_a}
    domain_b, visited = membership_domain(b0_b)
    require(visited == 19 * 18 * 18, "containing-box coverage missing")
    require(domain_a == domain_b, "full domain sets disagree")
    require(set(Y).issubset(domain_a), "marked site missing")
    require(one_step.issubset(domain_a), "one-step neighborhood missing")
    require(all(sum(p) % 2 == 0 for p in domain_a), "site outside D3")
    counts = {"Y": len(Y), "B": len(stencil_a), "B0": len(b0_a),
              "Y+B0": len(one_step), "B0+B0": len(two_offsets), "D": len(domain_a)}
    print("COUNTS " + json.dumps(counts, sort_keys=True, separators=(",", ":")))
    print("SHELL_COUNTS " + json.dumps(dict(sorted(shell_counts.items())), separators=(",", ":")))
    print(f"WEIGHT_SUM numerator={weighted_sum} denominator=324 diagonal=8/9")
    print(f"SET_EQUALITY forward=membership PASS box_sites={visited}")
    # Count 705 is an exposed regression target, not used to generate D.
    require(counts == {"Y": 5, "B": 60, "B0": 61, "Y+B0": 142, "B0+B0": 489, "D": 705},
            "exposed cardinality target mismatch")
    rows = table_bytes(domain_a)
    # Round-trip verifies the declared exact serialization independently of its hash.
    parsed = tuple(tuple(map(int, line.split(b"\t"))) for line in rows.splitlines()[1:])
    require(parsed == tuple(sorted(domain_b)), "point-list serialization mismatch")
    require(len(set(parsed)) == len(parsed), "point-list duplicates")
    slices = sorted(Counter(p[0] for p in domain_b).items())
    require(sum(n for _, n in slices) == len(domain_b), "slice count mismatch")
    print("X_SLICES " + json.dumps(slices, separators=(",", ":")))
    print(f"DOMAIN_TSV rows={len(parsed)} bytes={len(rows)} sha256={sha256(rows).hexdigest()}")
    print("DOMAIN_TSV_BEGIN")
    sys.stdout.write(rows.decode("ascii"))
    print("DOMAIN_TSV_END")
    print("LEGACY_ASSERTION |D|=869 FALSIFIED_AT_FROZEN_PRIMARY_DEFINITION")
    print("BOUNDARY no-native-contact no-wave-audit no-four-cut-infinite-lattice-lift")
    print("GEOMETRY_RECONCILIATION_PASS domain_sites=705 methods=2 authors=1")


if __name__ == "__main__":
    if len(sys.argv) != 1:
        raise SystemExit("usage: verify.py")
    custody()
    try:
        main()
    except AssertionError as error:
        # A completed negative mathematical decision is replayable, not hidden.
        print("FALSIFIER " + str(error))
        print("GEOMETRY_RECONCILIATION_FAIL remaining_checks=NOT_RUN")
