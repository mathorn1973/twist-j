#!/usr/bin/env python3
"""Negative controls for P-CARRY-C8-QUANTUM-PHASE-BRIDGE-1."""


def main():
    # B1: forgetting the AND carry breaks the C4 section law at (1,1).
    lhs = (2 + 2) % 8
    rhs_without_carry = 2 * (1 ^ 1) % 8
    assert lhs != rhs_without_carry
    print("B1 PASS: removing AND carry breaks the phase identity at 1+1")

    # B2: a non-generator image of C8 cannot realize an isomorphism.
    for k in (0, 2, 4, 6):
        assert len({(k * n) % 8 for n in range(8)}) < 8
    print("B2 PASS: even phase exponents fail C8-generator isomorphism")

    # B3: the C4 phase subgroup consists only of even T exponents.
    c4_phase_subgroup = {0, 2, 4, 6}
    assert all(k not in c4_phase_subgroup for k in (1, 3, 5, 7))
    print("B3 PASS: every C8 generator lies outside the C4 phase subgroup")

    # B4: branch reversal is not a unique-orientation selector.
    for k in (1, 3, 5, 7):
        assert (5 * k) % 8 != k
        assert (5 * k) % 8 == (k + 4) % 8
    print("B4 PASS: tau and -tau remain distinct generator branches, related by Z")

    print("BREAKER PASS: frozen overclaims are blocked by exact controls")


if __name__ == "__main__":
    main()
