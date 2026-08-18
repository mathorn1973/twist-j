#!/usr/bin/env python3
"""Exact audit for FIELD-ZERO-NONZERO-MULTIPLICATIVE-CUT.

The field-independent theorem is proved in PREREG.md.  This standard-library
verifier exhausts the frozen finite fields and the F_5^x zero-boundary control.

ZERO-RUN PIN: do not execute or import before the pinned files are committed,
pushed, and read back from the public remote.
"""

from itertools import product


OR_TABLE = 0b1110
AND_TABLE = 0b1000
XOR_TABLE = 0b0110
XNOR_TABLE = 0b1001


def require(condition, message):
    if not condition:
        raise AssertionError(message)


class FiniteField:
    """F_p[t]/(modulus), with low-first coefficients and a monic modulus."""

    def __init__(self, label, prime, modulus):
        self.label = label
        self.p = prime
        self.modulus = tuple(coefficient % prime for coefficient in modulus)
        self.degree = len(self.modulus) - 1
        require(self.degree >= 1, f"{label}: modulus degree must be positive")
        require(self.modulus[-1] == 1, f"{label}: modulus must be monic")
        self.order = prime ** self.degree
        self.elements = tuple(range(self.order))

    def decode(self, value):
        require(0 <= value < self.order, f"{self.label}: element outside carrier")
        coefficients = []
        remaining = value
        for _ in range(self.degree):
            coefficients.append(remaining % self.p)
            remaining //= self.p
        require(remaining == 0, f"{self.label}: base-p decoding overflow")
        return coefficients

    def encode(self, coefficients):
        require(len(coefficients) == self.degree,
                f"{self.label}: wrong coordinate length")
        value = 0
        place = 1
        for coefficient in coefficients:
            value += (coefficient % self.p) * place
            place *= self.p
        require(0 <= value < self.order, f"{self.label}: encoding overflow")
        return value

    def add(self, left, right):
        a = self.decode(left)
        b = self.decode(right)
        return self.encode([(x + y) % self.p for x, y in zip(a, b)])

    def neg(self, value):
        return self.encode([(-x) % self.p for x in self.decode(value)])

    def mul(self, left, right):
        a = self.decode(left)
        b = self.decode(right)
        coefficients = [0] * (2 * self.degree - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                coefficients[i + j] = (coefficients[i + j] + x * y) % self.p

        for power in range(len(coefficients) - 1, self.degree - 1, -1):
            lead = coefficients[power] % self.p
            if lead == 0:
                continue
            shift = power - self.degree
            for j, coefficient in enumerate(self.modulus):
                index = shift + j
                coefficients[index] = (
                    coefficients[index] - lead * coefficient
                ) % self.p
            require(coefficients[power] == 0,
                    f"{self.label}: polynomial reduction did not cancel lead")

        return self.encode(coefficients[:self.degree])


FIELD_SPECS = (
    ("F2", 2, (0, 1)),
    ("F3", 3, (0, 1)),
    ("F4", 2, (1, 1, 1)),
    ("F5", 5, (0, 1)),
    ("F7", 7, (0, 1)),
    ("F8", 2, (1, 1, 0, 1)),
    ("F9", 3, (1, 0, 1)),
    ("F11", 11, (0, 1)),
)


def boolean_value(table, left, right):
    require(left in (0, 1) and right in (0, 1), "Boolean input outside {0,1}")
    return (table >> ((left << 1) | right)) & 1


def audit_field_axioms(field):
    elements = field.elements
    zero = 0
    one = 1

    require(field.order == len(elements), f"{field.label}: carrier size mismatch")
    require(field.add(zero, zero) == zero, f"{field.label}: zero encoding mismatch")
    require(field.mul(one, one) == one, f"{field.label}: one encoding mismatch")

    for a in elements:
        require(field.add(a, zero) == a, f"{field.label}: additive identity failed")
        require(field.mul(a, one) == a, f"{field.label}: multiplicative identity failed")
        require(field.add(a, field.neg(a)) == zero,
                f"{field.label}: additive inverse failed")
        if a != zero:
            inverses = [b for b in elements if field.mul(a, b) == one]
            require(len(inverses) == 1,
                    f"{field.label}: nonzero element lacks a unique inverse")

    for a, b in product(elements, repeat=2):
        require(field.add(a, b) == field.add(b, a),
                f"{field.label}: addition is not commutative")
        require(field.mul(a, b) == field.mul(b, a),
                f"{field.label}: multiplication is not commutative")

    for a, b, c in product(elements, repeat=3):
        require(field.add(field.add(a, b), c) == field.add(a, field.add(b, c)),
                f"{field.label}: addition is not associative")
        require(field.mul(field.mul(a, b), c) == field.mul(a, field.mul(b, c)),
                f"{field.label}: multiplication is not associative")
        require(
            field.mul(a, field.add(b, c))
            == field.add(field.mul(a, b), field.mul(a, c)),
            f"{field.label}: distributivity failed",
        )


def exhaustive_cut_solutions(field, carrier=None):
    if carrier is None:
        carrier = field.elements
    carrier = tuple(carrier)
    positions = {element: index for index, element in enumerate(carrier)}
    require(len(positions) == len(carrier), f"{field.label}: duplicate carrier element")
    require(all(field.mul(x, y) in positions for x in carrier for y in carrier),
            f"{field.label}: multiplicative carrier is not closed")

    full_mask = (1 << len(carrier)) - 1
    solutions = []
    for mask in range(1, full_mask):
        for table in range(16):
            accepted = True
            for x, y in product(carrier, repeat=2):
                left = (mask >> positions[x]) & 1
                right = (mask >> positions[y]) & 1
                product_bit = (mask >> positions[field.mul(x, y)]) & 1
                if product_bit != boolean_value(table, left, right):
                    accepted = False
                    break
            if accepted:
                solutions.append((mask, table))
    return solutions


def audit_total_field(field):
    audit_field_axioms(field)
    solutions = exhaustive_cut_solutions(field)
    full_mask = (1 << field.order) - 1
    expected = [(1, OR_TABLE), (full_mask ^ 1, AND_TABLE)]
    require(solutions == expected,
            f"{field.label}: total cut classification differs from ZERO/OR,NONZERO/AND")
    subset_count = (1 << field.order) - 2
    print(
        f"AUDIT {field.label} order={field.order} subsets={subset_count} "
        "tables=16 solutions=2 cuts=ZERO/OR,NONZERO/AND"
    )


def audit_five_unit_boundary(field):
    require(field.label == "F5" and field.order == 5,
            "quadratic-character boundary requires the frozen prime field F5")
    units = (1, 2, 3, 4)
    squares = {field.mul(x, x) for x in units}
    require(squares == {1, 4}, "F5x quadratic-residue class mismatch")

    solutions = exhaustive_cut_solutions(field, units)
    # Unit order is (1,2,3,4): mask 1001 is QR, mask 0110 is NQR.
    expected = [(0b0110, XOR_TABLE), (0b1001, XNOR_TABLE)]
    require(solutions == expected,
            "F5x boundary differs from NQR/XOR and QR/XNOR")
    print(
        "BOUNDARY F5x order=4 subsets=14 tables=16 solutions=2 "
        "cuts=NQR/XOR,QR/XNOR"
    )


def main():
    require(OR_TABLE == 14, "OR table encoding mismatch")
    require(AND_TABLE == 8, "AND table encoding mismatch")
    require(XOR_TABLE == 6, "XOR table encoding mismatch")
    require(XNOR_TABLE == 9, "XNOR table encoding mismatch")

    fields = [FiniteField(*specification) for specification in FIELD_SPECS]
    for field in fields:
        audit_total_field(field)

    five = next(field for field in fields if field.label == "F5")
    audit_five_unit_boundary(five)
    print("RESULT fields=8 total_classification=TWO_ORIENTED_CUTS boundary=F5x_QUADRATIC_CHARACTER")
    print(
        "SCOPE L1 FIELD/BOOLEAN ALGEBRA ONLY; NO FIELD SELECTION, "
        "QDD COMPOSITION, DECODER, L5 STREAM, L6 MEASURE, OR STATUS MOVE"
    )


if __name__ == "__main__":
    main()
