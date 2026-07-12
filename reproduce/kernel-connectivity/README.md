# Kernel connectivity witness

The wedge rank stratification of the coupled kernel and the single
cell component census, in exact arithmetic: integers and F_5 only, no
floats anywhere. The generators are the registered kernel generators
of the census (section 3 of the Canon), taken verbatim; the wedge of
a cell pair is w_ij = x0_i x1_j - x0_j x1_i over F_5, the inter cell
symplectic area.

Verified: every generator is affine, g(x) = M_g x + v_g on all 15625
states with det M_g = 1 over F_5, a and b linear and c, d, e strictly
affine; the two CSUM transvections x1 -> x1 + x0 and x0 -> x0 + x1
preserve all 15 wedges as an exact polynomial identity in 12
variables and generate SL2(F_5), order 120, acting diagonally, the
order of the binary icosahedral bridge of the color door; the linear
sector acts on the wedge by congruence W -> M_g W M_g^T (36 basis
pairs, both sides bilinear) and the wedge rank is 0 exactly on
dependent pairs and 2 otherwise on the exhaustive slice x1 = e_0;
only the affine translations cross strata, lifting exactly
62480 = 2^4 . 5 . 11 . 71 of the 78125 dependent pairs each for c, d,
e and none for a, b; and the single cell component census matches the
recorded table on all seventeen generator subsets, from {ac} at 945
components down to the full verb {abcde} at 1, with monotonicity on
every comparable pair.

Evidence for registry claims KERNEL-WEDGE-AFFINITY,
KERNEL-WEDGE-COUPLING, KERNEL-WEDGE-LINEAR-STRATA,
KERNEL-WEDGE-AFFINE-MIX, KERNEL-CELL-COMPONENTS; the reading layer
KERNEL-MACRO-READING is carried by the same structure. The live
hypothesis KERNEL-CONNECT-ALL-K carries no witness here: the k = 2
and k = 3 connectivity witnesses live at the sealed internal scope
beyond the public 120 s budget, and nothing in this file claims
them. Check map: 01 KERNEL-WEDGE-AFFINITY; 02 and 03
KERNEL-WEDGE-COUPLING; 04 and 05 KERNEL-WEDGE-LINEAR-STRATA; 06
KERNEL-WEDGE-AFFINE-MIX; 07 KERNEL-CELL-COMPONENTS.

Run from the repository root:

```
python3 reproduce/kernel-connectivity/verify.py
```

Expected: byte identical to EXPECTED.txt, RESULT 7/7 ALL PASS,
exit 0, no stderr.
