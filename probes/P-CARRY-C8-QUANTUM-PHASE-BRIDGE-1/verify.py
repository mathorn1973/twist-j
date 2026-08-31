#!/usr/bin/env python3
"""Exact verifier for P-CARRY-C8-QUANTUM-PHASE-BRIDGE-1.

No floating-point arithmetic is used. Phase exponents are represented modulo 8.
"""

from itertools import product


def xor(a, b):
    return a ^ b


def land(a, b):
    return a & b


def popcount4(x):
    return sum(x)


def q(x):
    return sum(x[i] * x[j] for i in range(4) for j in range(i + 1, 4)) % 2


def bits_to_string(x):
    return "".join(str(v) for v in x)


def main():
    # G1: S is exponent 2 in mu_8, Z is exponent 4.
    for a, b in product((0, 1), repeat=2):
        lhs = (2 * a + 2 * b) % 8
        rhs = (2 * xor(a, b) + 4 * land(a, b)) % 8
        assert lhs == rhs, (a, b, lhs, rhs)
    print("G1 PASS: C4/XOR carry maps exactly to S/Z phase identity")

    # G2: each CZ_ij contributes exponent 4*x_i*x_j in mu_8.
    singular_nonzero = []
    for x in product((0, 1), repeat=4):
        uq_exp = 4 * q(x) % 8
        cz_exp = 4 * sum(x[i] * x[j] for i in range(4) for j in range(i + 1, 4)) % 8
        assert uq_exp == cz_exp, (x, uq_exp, cz_exp)
        if x != (0, 0, 0, 0) and q(x) == 0:
            singular_nonzero.append(bits_to_string(x))
    expected = ["0001", "0010", "0100", "1000", "1111"]
    assert singular_nonzero == expected, (singular_nonzero, expected)
    print("G2 PASS: U_q equals product of all six CZ gates; nonzero q=0 locus is the carry pentad")

    # G3: encode tau as exponent 1 in C8, J_lambda=tau^2, -1=tau^4.
    generators = (1, 3, 5, 7)
    for k in generators:
        # homomorphism exponent map n -> k*n mod 8
        assert len({(k * n) % 8 for n in range(8)}) == 8
        tau_image = k % 8
        j_image = (2 * k) % 8
        minus_one_image = (4 * k) % 8
        assert j_image in (2, 6)  # S or S^-1
        assert minus_one_image == 4  # Z
        assert tau_image % 2 == 1  # odd T power, hence outside the single-qubit Clifford phase subgroup <S>

        # branch tau -> -tau=tau^5 multiplies the phase image by Z.
        branch_image = (5 * k) % 8
        assert branch_image == (tau_image + 4) % 8

    print("G3 PASS: every C8 generator maps to an odd T power; J_lambda maps to S^±1; -1 maps to Z")
    print("G3 PASS: tau -> -tau changes the represented phase gate by Z")
    print("VERDICT PASS: exact L1 algebraic bridge; no physical quantum-mechanics claim")


if __name__ == "__main__":
    main()
