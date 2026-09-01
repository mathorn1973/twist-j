#!/usr/bin/env python3
"""Accepted exact verifier for P-QDD-DIRECT-RECORD-E-NONCONGRUENCE-1.

This verifier must not be executed before its
accepted bytes and PREREG.md are publicly pinned and read back.
"""

from fractions import Fraction
from itertools import product
import sys


F = Fraction
MODULUS = 5
PISTON_CENTER = (2, 1, 3, 4)
BALANCED = (0, 1, 2, -2, -1)


class ClaimFailure(Exception):
    """An exact failure of a frozen mathematical clause."""


def require(condition, message):
    if not condition:
        raise ClaimFailure(message)


def residue_neg(vector):
    return tuple((-entry) % MODULUS for entry in vector)


def balanced_lift(vector):
    return tuple(F(BALANCED[entry % MODULUS]) for entry in vector)


def sign_representative(vector):
    negative = residue_neg(vector)
    return min(tuple(vector), negative)


def shifted_mirror(vector):
    return tuple(
        (PISTON_CENTER[index] - vector[index]) % MODULUS
        for index in range(4)
    )


def zero_center_mirror(vector):
    return residue_neg(vector)


def matrix_product(left, right):
    row_count = len(left)
    inner_count = len(right)
    column_count = len(right[0])
    require(
        all(len(row) == inner_count for row in left),
        "left matrix shape mismatch",
    )
    require(
        all(len(row) == column_count for row in right),
        "right matrix shape mismatch",
    )
    return tuple(
        tuple(
            sum(
                (left[row][inner] * right[inner][column]
                 for inner in range(inner_count)),
                F(0),
            )
            for column in range(column_count)
        )
        for row in range(row_count)
    )


def matrix_scale(scalar, matrix):
    return tuple(
        tuple(scalar * entry for entry in row)
        for row in matrix
    )


GRAM = tuple(
    tuple(F(int(row == column)) - F(1, 5) for column in range(4))
    for row in range(4)
)


def outer_product(vector):
    return tuple(
        tuple(vector[row] * vector[column] for column in range(4))
        for row in range(4)
    )


def qdd_record(residue_vector):
    """Registered factor expression, equal to D_QDD_direct by public theorem."""

    vector = balanced_lift(residue_vector)
    if all(entry == 0 for entry in vector):
        return (
            "ZERO_SUPPORT",
            F(0),
            (F(0), F(0)),
            ("ZERO_DENOMINATOR",),
            ("ZERO_DENOMINATOR",),
        )

    norm_squared = sum((entry * entry for entry in vector), F(0))
    trace_four = sum(vector, F(0))
    total_weight = norm_squared - trace_four * trace_four / 5
    low_weight = trace_four * trace_four / 20
    high_weight = norm_squared - trace_four * trace_four / 4

    require(total_weight > 0, "nonzero piston has nonpositive total weight")
    require(low_weight >= 0, "LOW branch weight is negative")
    require(high_weight >= 0, "HIGH branch weight is negative")
    require(
        low_weight + high_weight == total_weight,
        "ordered branch weights do not sum to total weight",
    )

    operator_matrix = matrix_product(outer_product(vector), GRAM)
    density = matrix_scale(F(1, 1) / total_weight, operator_matrix)
    normalized = (
        low_weight / total_weight,
        high_weight / total_weight,
    )
    require(sum(normalized, F(0)) == 1, "normalized weights do not sum to one")

    return (
        "SUPPORTED",
        total_weight,
        (low_weight, high_weight),
        ("DENSITY", density),
        ("NORMALIZED", normalized),
    )


def field_differences(left, right):
    names = (
        "support_state",
        "total_weight",
        "branch_weights",
        "density_state",
        "normalized_weight_state",
    )
    return tuple(
        name for name, left_value, right_value in zip(names, left, right)
        if left_value != right_value
    )


def run():
    pistons = tuple(product(range(MODULUS), repeat=4))
    zero = (0, 0, 0, 0)

    require(len(pistons) == 625, "wrong piston carrier size")
    require(
        all(
            balanced_lift(residue_neg(piston))
            == tuple(-entry for entry in balanced_lift(piston))
            for piston in pistons
        ),
        "balanced lift does not intertwine residue negation",
    )
    print("PASS G1 balanced F5 piston carrier and negation law")

    require(PISTON_CENTER != zero, "shifted-mirror centre unexpectedly vanishes")
    require(
        all(shifted_mirror(shifted_mirror(piston)) == piston for piston in pistons),
        "shifted mirror is not an involution",
    )
    print("PASS G2 declared e piston action is the affine involution c-p")

    sign_classes = {}
    record_classes = {}
    for piston in pistons:
        sign_classes.setdefault(sign_representative(piston), []).append(piston)
        record_classes.setdefault(qdd_record(piston), []).append(piston)

    require(len(sign_classes) == 313, "wrong sign-class count")
    require(len(record_classes) == 313, "wrong complete-record class count")
    require(
        sorted(sorted(fibre) for fibre in sign_classes.values())
        == sorted(sorted(fibre) for fibre in record_classes.values()),
        "complete QDD record fibres are not exactly the sign fibres",
    )
    require(
        sorted(len(fibre) for fibre in sign_classes.values()) == [1] + [2] * 312,
        "wrong sign-fibre size profile",
    )
    require(sign_classes[zero] == [zero], "zero sign fibre is not the singleton")
    print("PASS G3 complete record quotient has 313 classes with profile 1+312x2")

    nonzero_representatives = tuple(
        representative for representative in sorted(sign_classes)
        if representative != zero
    )
    require(len(nonzero_representatives) == 312, "wrong nonzero sign-fibre count")
    require(
        all(
            qdd_record(representative) == qdd_record(residue_neg(representative))
            for representative in nonzero_representatives
        ),
        "a nonzero input sign fibre carries two records",
    )
    print("PASS G4 all 312 nonzero sign pairs have equal five-field input records")

    unsplit = []
    for representative in nonzero_representatives:
        negative = residue_neg(representative)
        image = shifted_mirror(representative)
        negative_image = shifted_mirror(negative)
        if sign_representative(image) == sign_representative(negative_image):
            unsplit.append(representative)
        require(
            qdd_record(image) != qdd_record(negative_image),
            "a shifted-mirror output pair retains one complete record",
        )
    require(not unsplit, "at least one nonzero sign fibre is not split by e")
    require(
        len(nonzero_representatives) - len(unsplit) == 312,
        "the hard 312-of-312 split threshold failed",
    )
    print("PASS G5 shifted mirror e splits exactly 312 of 312 nonzero record fibres")

    witness_plus = (1, 0, 0, 0)
    witness_minus = (4, 0, 0, 0)
    input_plus = qdd_record(witness_plus)
    input_minus = qdd_record(witness_minus)
    output_plus = qdd_record(shifted_mirror(witness_plus))
    output_minus = qdd_record(shifted_mirror(witness_minus))

    require(input_plus == input_minus, "displayed input witness records differ")
    require(input_plus[1] == F(4, 5), "wrong displayed input total weight")
    require(
        input_plus[2] == (F(1, 20), F(3, 4)),
        "wrong displayed input branch weights",
    )
    require(
        input_plus[4] == ("NORMALIZED", (F(1, 16), F(15, 16))),
        "wrong displayed input normalized weights",
    )
    require(
        balanced_lift(shifted_mirror(witness_plus)) == (F(1), F(1), F(-2), F(-1)),
        "wrong plus output piston",
    )
    require(
        balanced_lift(shifted_mirror(witness_minus)) == (F(-2), F(1), F(-2), F(-1)),
        "wrong minus output piston",
    )
    require(
        output_plus[1] == output_minus[1] == F(34, 5),
        "wrong displayed output total weights",
    )
    require(
        output_plus[2] == (F(1, 20), F(27, 4)),
        "wrong plus output branch weights",
    )
    require(
        output_minus[2] == (F(4, 5), F(6)),
        "wrong minus output branch weights",
    )
    require(
        field_differences(output_plus, output_minus)
        == ("branch_weights", "density_state", "normalized_weight_state"),
        "wrong displayed output field-difference pattern",
    )
    print("PASS G6 explicit witness has one input record and two exact output records")

    require(
        all(
            sign_representative(zero_center_mirror(piston))
            == sign_representative(piston)
            for piston in pistons
        ),
        "zero-centre mirror fails to descend through the sign quotient",
    )
    require(
        all(
            qdd_record(zero_center_mirror(piston)) == qdd_record(piston)
            for piston in pistons
        ),
        "zero-centre mirror changes a complete record",
    )
    print("PASS G7 zero-centre mirror descends; the nonzero affine centre is decisive")

    print("RESULT 7/7 ALL PASS QDD-DIRECT-RECORD-E-NONCONGRUENCE")
    return 0


def main():
    try:
        return run()
    except ClaimFailure as exc:
        print(f"RESULT CLAIM FIRES: {exc}")
        return 1
    except Exception as exc:
        print(f"RESULT INTEGRITY STOP: {type(exc).__name__}: {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
