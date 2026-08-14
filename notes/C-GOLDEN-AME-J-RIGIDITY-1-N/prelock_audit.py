#!/usr/bin/env python3
"""Construction-only audit for publicly locked preregistration issue #369.

This script verifies source bytes, both construction paths, structural counts,
stable equation serialization, and the original known point.  The known-point
checks use floating point and are diagnostics only.  The script contains no
ideal-solving operation and no candidate target relation.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path

from golden_symbolic import (
    BLOCKS,
    BLOCK_COL_TO_G_COL,
    BLOCK_ROW_TO_G_ROW,
    FLATTENINGS,
    construct_a_direct,
    construct_b_blocks,
    flatten_tensor,
    parse_block944_permutations,
    structural_report,
)


def evaluate_tensor(tokens):
    sqrt5 = math.sqrt(5.0)
    amplitudes = {
        "a": math.sqrt(1.0 - 1.0 / sqrt5) / 2.0,
        "b": math.sqrt(1.0 + 1.0 / sqrt5) / 2.0,
        "c": 1.0 / math.sqrt(2.0),
    }
    x = cmath.exp(2j * math.pi / 20.0)
    return {
        indices: amplitudes[label] * x**exponent
        for indices, (label, exponent) in tokens.items()
    }


def maximum_unitarity_residual(tokens) -> dict[str, float]:
    tensor = evaluate_tensor(tokens)
    output = {}
    for row_parties in FLATTENINGS:
        rows = flatten_tensor(tensor, row_parties)
        maximum = 0.0
        for left in range(36):
            for right in range(36):
                common = set(rows[left]).intersection(rows[right])
                gram = sum(rows[left][c] * rows[right][c].conjugate() for c in common)
                expected = 1.0 if left == right else 0.0
                maximum = max(maximum, abs(gram - expected))
        output["".join(map(str, row_parties))] = maximum
    return output


def block_known_point_residuals(tokens) -> tuple[float, float]:
    """Check the original block944 4x4 and scaled 2x2 assertions."""

    tensor = evaluate_tensor(tokens)
    g = {
        (6 * i + ell, 6 * k + j): value
        for (i, j, k, ell), value in tensor.items()
    }
    max_block = 0.0
    max_quadrant = 0.0

    def gram_residual(matrix, expected_diagonal: float) -> float:
        size = len(matrix)
        maximum = 0.0
        for left in range(size):
            for right in range(size):
                value = sum(
                    matrix[left][column] * matrix[right][column].conjugate()
                    for column in range(size)
                )
                expected = expected_diagonal if left == right else 0.0
                maximum = max(maximum, abs(value - expected))
        return maximum

    for block_number in range(9):
        matrix = []
        for inner_row in range(4):
            row = []
            for inner_column in range(4):
                old_row = BLOCK_ROW_TO_G_ROW[4 * block_number + inner_row]
                old_column = BLOCK_COL_TO_G_COL[4 * block_number + inner_column]
                row.append(g.get((old_row, old_column), 0j))
            matrix.append(row)
        max_block = max(max_block, gram_residual(matrix, 1.0))
        for row_start in (0, 2):
            for column_start in (0, 2):
                quadrant = [
                    matrix[row][column_start : column_start + 2]
                    for row in range(row_start, row_start + 2)
                ]
                # Q*sqrt(2) unitary is equivalent to Q Q^* = I/2.
                max_quadrant = max(max_quadrant, gram_residual(quadrant, 0.5))
    return max_block, max_quadrant


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("original", type=Path)
    parser.add_argument("--block944", type=Path)
    args = parser.parse_args()

    direct = construct_a_direct(args.original.read_bytes())
    blocks = construct_b_blocks()
    if direct != blocks:
        only_a = sorted(set(direct.items()) - set(blocks.items()))
        only_b = sorted(set(blocks.items()) - set(direct.items()))
        raise AssertionError(("construction mismatch", only_a[:3], only_b[:3]))

    if args.block944 is not None:
        row_map, column_map = parse_block944_permutations(args.block944.read_bytes())
        if row_map != BLOCK_ROW_TO_G_ROW or column_map != BLOCK_COL_TO_G_COL:
            raise AssertionError("block944 permutation provenance mismatch")

    report = structural_report(direct)
    if report["support"] != 112:
        raise AssertionError(report["support"])
    if report["label_counts"] != {"a": 40, "b": 40, "c": 32}:
        raise AssertionError(report["label_counts"])
    if report["block_nonzero_counts"] != [12, 14, 14, 8, 16, 8, 14, 14, 12]:
        raise AssertionError(report["block_nonzero_counts"])

    direct_residuals = maximum_unitarity_residual(direct)
    block_residuals = maximum_unitarity_residual(blocks)
    if direct_residuals != block_residuals:
        raise AssertionError("known-point diagnostics differ")
    if max(direct_residuals.values()) >= 1e-12:
        raise AssertionError(("known point failed", direct_residuals))
    block4_residual, quadrant2_residual = block_known_point_residuals(blocks)
    if block4_residual >= 1e-12 or quadrant2_residual >= 1e-12:
        raise AssertionError(("block known point failed", block4_residual, quadrant2_residual))

    print("GOLDEN_RIGIDITY_PRELOCK_CONSTRUCTION_V1")
    print("SOURCE_ORIGINAL=PIN_PASS")
    print(f"SOURCE_BLOCK944={'PIN_PASS' if args.block944 is not None else 'NOT_CHECKED'}")
    print("CONSTRUCTION_A=DIRECT_LITERAL_PARSER")
    print("CONSTRUCTION_B=NINE_4X4_BLOCK_FIXTURE")
    print("CONSTRUCTIONS_EXACT_TOKEN_EQUAL=PASS")
    print("RING=Q[a,b,c,x,y]/(x*y-1)")
    print("INVOLUTION=a:a,b:b,c:c,x:y,y:x")
    print("SOURCE_EXPONENTS=LITERAL_0_TO_19_NO_MODULAR_REDUCTION")
    print("SUPPORT=112")
    print("LABEL_COUNTS=a:40,b:40,c:32")
    print("BLOCK_NONZERO_COUNTS=12,14,14,8,16,8,14,14,12")
    print("EQUATION_COORDINATES_INCLUDING_XY=" + str(report["equation_coordinates_including_xy"]))
    print("ACTIVE_EQUATIONS_INCLUDING_XY=" + str(report["active_equations_including_xy"]))
    print("EQUATION_SERIALIZATION_BYTES=" + str(report["equation_serialization_bytes"]))
    print("EQUATION_SERIALIZATION_SHA256=" + str(report["equation_serialization_sha256"]))
    print("STRUCTURAL_REPORT_JSON=" + json.dumps(report, sort_keys=True, separators=(",", ":")))
    print(
        "FLOAT_DIAGNOSTIC_THREE_UNITARITY_MAX="
        + format(max(direct_residuals.values()), ".17g")
    )
    print("FLOAT_DIAGNOSTIC_BLOCK4_MAX=" + format(block4_residual, ".17g"))
    print("FLOAT_DIAGNOSTIC_QUADRANT2_MAX=" + format(quadrant2_residual, ".17g"))
    print("GROEBNER=NOT_RUN")
    print("RADICAL=NOT_RUN")
    print("ELIMINATION=NOT_RUN")
    print("SATURATION=NOT_RUN")
    print("TARGET_RELATION_TESTS=NOT_RUN")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
