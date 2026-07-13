# Force and Born dictionary witness

This witness checks the exact theorem and computation layer beneath the
force/Born dictionary:

- the finite Weyl identity `Z X Z^-1 X^-1 = zeta_5 I`;
- the Moore-Penrose Green kernel on the finite decoder graph `C4`,
  `16 G = circ(5,-1,-3,-1)`;
- the five Born weights and their Galois pairing and tilt;
- the conjugate verb readouts, their circulant Gram and exact spectrum;
- mutual unbiasedness of the position and Fourier bases;
- the Plancherel masses `2` and `10`, in ratio `5`.

All checks use the Python standard library and exact integer arithmetic in
`Z[zeta_5]`; the Green computation clears its denominator by working with
`16 G`.

The scope boundary is essential.  The finite decoder graph has the rational
kernel displayed above.  The continuum Green law `1/(4 pi r)` is carried only
by the registered dictionary reading `COULOMB-PROJECTION [D]`; this witness
does not claim that the continuum kernel occurs as a value on `C4`.
Likewise, the D rows name readings of exact facts and are not promoted by the
computation.  The sealed six-ensemble magnetic selection is not reconstructed
or claimed by this public witness.

Evidence for `FORCE-WEYL-HOLONOMY [T]`,
`COULOMB-GREEN-COMPUTATION [C]`, and `SUBSTRATE-KNIT [T]`, and exact support
for the associated D dictionary rows.

Run from the repository root:

```text
python3 reproduce/force-born-dictionary/verify.py
```

Expected: byte-identical output to `EXPECTED.txt`, `RESULT 10/10 ALL PASS`,
exit 0, and empty stderr.
