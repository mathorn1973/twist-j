# Pentit and p=5 closure witness

This witness closes the remaining exact public arithmetic in sections 11 and
16.  It uses only integers and the pair model
`F_25 = F_5[t]/(t^2 - 2)`; it has no dependencies outside the Python standard
library and uses no floating-point arithmetic.

It verifies:

- the ramified images `J = 2` and `phi = 3`, with `tau^2 = J`,
  `tau^4 = -1`, `tau^6 = phi`, and therefore
  `sqrt(phi) = tau^3` in `F_25`;
- the complete exponent window `k = 0..23` of the norm ladder
  `N(tau^k) = 3^k = 2^(-k)` in `F_5*`;
- the exact order-four time source `i_5 = 2`, its two-step value `-1`, and
  the half-root reciprocity identities;
- the two-element sign quotient `V_+ := F_5*/{+-1}`;
- the root selector `(p - 2)/(p + 1) = 1/2` if and only if `p = 5` for
  positive primes, by the integer identity obtained after clearing the
  denominator.

These checks support `PENTIT-ROOT-FACTS`, `MAGIC-PRIME-GATE`,
`QUBIT-FROM-F5`, and `P5-ROOT-SELECTION`.  `PENTIT-ROOT-READING` is the
dictionary sentence resting on the exact root facts.  The legacy Bell and
Tsirelson sentence is not promoted by this witness: `BELL-MAGIC-BOUNDARY`
stays open until its root-of-unity CHSH functional and both maxima are
reconstructed publicly.

Run from the repository root:

```text
python3 reproduce/pentit-p5-closure/verify.py
```

Expected: byte-identical output to `EXPECTED.txt`, `RESULT 5/5 ALL PASS`,
exit 0, empty stderr.
