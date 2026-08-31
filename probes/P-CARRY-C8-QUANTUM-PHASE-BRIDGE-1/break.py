#!/usr/bin/env python3
"""Negative controls for P-CARRY-C8-QUANTUM-PHASE-BRIDGE-1."""


def main():
    # B1: forgetting the AND carry breaks the C4 section law at (1,1).
    lhs = (2 + 2) % 8
    rhs_without_carry = 2 * (1 ^ 1) % 8
    assert lhs != rhs_without_carry
    print("B1 PASS: removing AND carry breaks the phase identity at 1+1")

    # B2: the U(1) phase must not be mistaken for a surviving nontrivial
    # coefficient class: at (1,1), the explicit cochain i^a supplies it.
    carry_phase = 4  # exponent of -1 in mu_8
    coboundary = (2 + 2 - 0) % 8
    assert carry_phase == coboundary
    print("B2 PASS: U(1) carry phase has the frozen explicit coboundary")

    # B3: a non-generator image of C8 cannot realize an isomorphism.
    for k in (0, 2, 4, 6):
        assert len({(k * n) % 8 for n in range(8)}) < 8
    print("B3 PASS: even phase exponents fail C8-generator isomorphism")

    # B4: odd generator images are outside the even C4 phase subgroup.
    c4_phase_subgroup = {0, 2, 4, 6}
    assert all(k not in c4_phase_subgroup for k in (1, 3, 5, 7))
    print("B4 PASS: every C8 generator lies outside the C4 phase subgroup")

    # B5: branch reversal is not a unique-orientation selector.
    for k in (1, 3, 5, 7):
        assert (5 * k) % 8 != k
        assert (5 * k) % 8 == (k + 4) % 8
    print("B5 PASS: tau and -tau remain distinct generator branches, related by Z")

    # B6: a linear parity phase is not the quadratic carry phase.
    x = (1, 1, 0, 0)
    q = sum(x[i] * x[j] for i in range(4) for j in range(i + 1, 4)) % 2
    linear = sum(x) % 2
    assert q == 1 and linear == 0
    print("B6 PASS: quadratic carry phase is not reducible to linear parity")

    print("BREAKER PASS: frozen overclaims are blocked by exact controls")


if __name__ == "__main__":
    main()
