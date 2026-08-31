#!/usr/bin/env python3
"""Exact verifier for P-CARRY-C8-QUANTUM-PHASE-BRIDGE-1.

No floating-point arithmetic is used. Roots of unity are represented by
integer exponents modulo 8.
"""

from itertools import product


def xor(a, b):
    return a ^ b


def land(a, b):
    return a & b


def q(x):
    return sum(x[i] * x[j] for i in range(4) for j in range(i + 1, 4)) % 2


def bits_to_string(x):
    return "".join(str(v) for v in x)


def is_diagonal_phase_clifford(k):
    """For P_k=diag(1,zeta_8^k), test Pauli normalization on X.

    Conjugation gives off-diagonal entries zeta_8^-k and zeta_8^k.
    Their ratio is zeta_8^(2k). Up to scalar, a Pauli with off-diagonal
    support is X or Y, whose corresponding ratio is +1 or -1, exponents
    0 or 4 modulo 8.
    """
    return (2 * k) % 8 in (0, 4)


def main():
    # G1: S is exponent 2 in mu_8, Z is exponent 4.
    for a, b in product((0, 1), repeat=2):
        lhs = (2 * a + 2 * b) % 8
        rhs = (2 * xor(a, b) + 4 * land(a, b)) % 8
        assert lhs == rhs, (a, b, lhs, rhs)
    print("G1 PASS: C4/XOR carry maps exactly to S/Z phase identity")

    # G1b: the U(1)-valued carry phase is the coboundary of a -> i^a.
    for a, b in product((0, 1), repeat=2):
        carry_phase = (4 * land(a, b)) % 8
        coboundary = (2 * a + 2 * b - 2 * xor(a, b)) % 8
        assert carry_phase == coboundary, (a, b, carry_phase, coboundary)
    print("G1b PASS: (-1)^(a AND b) is the explicit U(1) coboundary of i^a")

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
        # n -> k*n mod 8 is an isomorphism exactly because k is odd.
        assert len({(k * n) % 8 for n in range(8)}) == 8
        tau_image = k % 8
        j_image = (2 * k) % 8
        minus_one_image = (4 * k) % 8
        assert j_image in (2, 6)  # S or S^-1
        assert minus_one_image == 4  # Z

        # Exact Clifford boundary: odd diagonal eighth-root phases do not
        # normalize X into a Pauli, while even exponents do.
        assert not is_diagonal_phase_clifford(k)
        assert is_diagonal_phase_clifford(2 * k)
        assert is_diagonal_phase_clifford(4 * k)

        # Branch tau -> -tau=tau^5 multiplies the phase image by Z.
        branch_image = (5 * k) % 8
        assert branch_image == (tau_image + 4) % 8

    for k in range(8):
        assert is_diagonal_phase_clifford(k) == (k % 2 == 0), k

    print("G3 PASS: every C8 generator maps to an odd non-Clifford T power")
    print("G3 PASS: J_lambda maps to S^±1, -1 maps to Z, both Clifford")
    print("G3 PASS: tau -> -tau changes the represented phase gate by Z")
    print("VERDICT PASS: exact L1 algebra/operator bridge; no physical quantum-mechanics claim")


if __name__ == "__main__":
    main()
