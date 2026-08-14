# BREAKER C-TM-SYM2-ORIENTATION-SOURCE-1-N

```text
STATUS:     NON-CANONICAL independent breaker design
ISSUE LOCK: #375
FROZEN:     before any verifier/result
```

## B1 enumerate W3 independently

List all six words, compute R, N and NR directly, and compute `c-a`. Any word violating the claimed signs fires S1.

## B2 uniqueness without using the formula

Let `f(001)=x` and impose only `f o R=-f`, `f o N=-f`. Derive all remaining values. Check separately the R-fixed words 010 and 101. The solution space must have dimension one. Do not assume `c-a` until the classification is complete.

## B3 epsilon sign

From inherited translations only, recompute the sign of `epsilon=chi_Q chi_F` under `(1,0)`, `(0,1)`, `(1,1)`. A mismatch with omega fires the source.

## B4 class-order control

Permute the four quotient classes and verify that the construction is character-covariant rather than tied to the printed order. The coordinate vector may permute; the epsilon line itself must not depend on a selector representative.

## B5 simultaneous action

For every b in {N,R,NR}, apply b to the window and the inherited quotient translation to the class vector. Check that both factors acquire the same sign and their tensor/product source is invariant. Do not confuse separate action on only one factor with the simultaneous coherence claim.

## B6 palindromes

R fixes 010 and 101. Any R-odd rational source must vanish there. This is required, not a defect. A claim of a nonzero binary orientation on all six windows is false.

## B7 child recursion

Starting from the child maps, recompute the child omega values using only integer differences. Check whether the finite state needed for recursion is exactly the parent edge-difference pair and whether any selector enters.

## B8 firewall

Reject any inference from the uniform W3 law or `E[omega^2]` to Born probability, gyron density, or L6 normalization. SOURCE means only a typed L5 orientation carrier.
