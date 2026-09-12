#!/usr/bin/env python3
"""Exact verifier for the CM5 W2H-B hyper-Ext and equivariant window note.

NON-CANONICAL. Standard library only. No floating point.

This script reuses the accepted W2E theta verifier to count the product-compatible
order-80 candidates, then checks the exact hyper-Ext lower bounds stated in W2H-B.
"""

from pathlib import Path
import runpy


HERE = Path(__file__).resolve().parent
W2E = HERE / "HODGE-TATE-CM5-PERRY-W2E-A-THETA-VERIFY.py"
ns = runpy.run_path(str(W2E))

pass2 = ns["pass2"]
rank_mod = ns["rank_mod"]


def span_vectors(rows):
    """Return the F_2 span of the given rows."""
    out = set()
    k = len(rows)
    n = len(rows[0])
    for mask in range(1 << k):
        v = [0] * n
        for i in range(k):
            if (mask >> i) & 1:
                v = [v[j] ^ rows[i][j] for j in range(n)]
        out.add(tuple(v))
    return out


factorized = []
for plane in pass2:
    W = span_vectors(plane)
    left = [v for v in W if all(x == 0 for x in v[4:])]
    right = [v for v in W if all(x == 0 for x in v[:4])]
    if rank_mod(left, 2) == 2 and rank_mod(right, 2) == 2:
        factorized.append(plane)

assert len(pass2) == 85
assert len(factorized) == 25

# A projective line in F_5^2: (25-1)/(5-1)=6. It can be supported in
# either of the two abelian-surface factors.
five_lines_one_factor = (5**2 - 1) // (5 - 1)
factor_supported_five_lines = 2 * five_lines_one_factor
factorized_order80 = len(factorized) * factor_supported_five_lines

assert five_lines_one_factor == 6
assert factor_supported_five_lines == 12
assert factorized_order80 == 300


# ---------------------------------------------------------------------------
# Ordinary hyper-Ext bounds
# ---------------------------------------------------------------------------

r = 399
s = 798 + 2 * r

a0 = 1
a1 = 2 * r
a2 = r * r + 2 * s
a3 = 2 * r * (1 + s)
a6 = a2
a8 = a0

ordinary_k1 = 2 * a3 - 5 * a1 - 2
ordinary_k2 = 5 * a2 - 2 * a6
ordinary_k3 = 5 * a2 - 2 * a8
ordinary_k4 = 5 * a2

assert a1 == 798
assert a2 == 162393
assert a3 == 1274406
assert ordinary_k1 == 2544820
assert ordinary_k2 == 487179
assert ordinary_k3 == 811963
assert ordinary_k4 == 811965


# ---------------------------------------------------------------------------
# Equivariant order-80 window
# ---------------------------------------------------------------------------


def equivariant_lower(rh):
    # For |H|=80: chi^H=10 and e2^H=8+2rh.
    sh = 8 + 2 * rh
    a1h = 2 * rh
    a3h = 2 * rh * (1 + sh)
    return 2 * a3h - 5 * a1h - 2


assert equivariant_lower(12) == 1462
assert equivariant_lower(30) == 7978
assert equivariant_lower(31) == 8492

# The exact overlap with the 8008-dimensional target is 12 <= r_H <= 30.
assert all(equivariant_lower(rh) <= 8008 for rh in range(12, 31))
assert equivariant_lower(31) > 8008


print("passing 2-primary Lagrangians   =", len(pass2))
print("factorized passing Lagrangians  =", len(factorized))
print("factor-supported 5-lines        =", factor_supported_five_lines)
print("factorized order-80 candidates  =", factorized_order80)
print("ordinary k=1 lower bound        =", ordinary_k1)
print("ordinary k=2 lower bound        =", ordinary_k2)
print("ordinary k=3 lower bound        =", ordinary_k3)
print("ordinary k=4 lower bound        =", ordinary_k4)
print("equivariant r_H=12 lower bound  =", equivariant_lower(12))
print("equivariant r_H=30 lower bound  =", equivariant_lower(30))
print("equivariant r_H=31 lower bound  =", equivariant_lower(31))
print("RESULT: W2H-B exact hyper-Ext verifier PASS")
