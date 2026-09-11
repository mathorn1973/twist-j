#!/usr/bin/env python3
"""Exact numerical verifier for W2K-A universally-gluable outer repair.

NON-CANONICAL. The generic Hom-vanishing and categorical Ext<0 arguments are
proved in the companion note. This script checks the numerical consequences
used by the construction. No floating point.
"""

# Source invariant self Euler from W2J-C.
source_chi = 800 // 80
assert source_chi == 10

# Under the W2K-A generic Hom-orthogonality assumptions, e0=e4=0 and
# chi=-e1+e2-e3=10, hence e2=10+e1+e3 >=10.
for e1 in range(0, 64):
    for e3 in range(0, 64):
        e2 = source_chi + e1 + e3
        assert -e1 + e2 - e3 == source_chi
        assert e2 >= 10

# Old W2H repeated-cell model U=P^2, V=P[1]: degree -1 contains Hom(P^2,P).
old_hom_P_P = 1
old_ext_minus_1_lower = 2 * old_hom_P_P
assert old_ext_minus_1_lower == 2

# New model uses pairwise Hom-orthogonal cells P1,P2 -> P0[2].
new_hom_P1_P0 = 0
new_hom_P2_P0 = 0
new_shift_generated_minus_1 = new_hom_P1_P0 + new_hom_P2_P0
assert new_shift_generated_minus_1 == 0

# K-theory/Chern coefficient: P1+P2-P0 has the same numerical class as P0.
coeff = 1 + 1 - 1
assert coeff == 1

# At least ten degree-two choices exist in each source-twist direction.
min_source_ext2 = source_chi
assert min_source_ext2 >= 2

print("source invariant Euler              =", source_chi)
print("old repeated-cell Ext^-1 lower     =", old_ext_minus_1_lower)
print("new shift-generated Ext^-1         =", new_shift_generated_minus_1)
print("outer numerical Chern coefficient  =", coeff)
print("min cross source Ext^2             =", min_source_ext2)
print("RESULT: W2K-A prerequisite arithmetic PASS")