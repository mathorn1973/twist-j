# P-J-RESIDUE-PERIOD-1 result

Status: **candidate-T / L1 / J-RESIDUE-PERIOD-CONFIRMED / PUBLIC CANON STATUS
UNCHANGED.**

The first formal execution of the immutable public verifier exited zero, wrote
empty stderr, and produced the exact committed `EXPECTED.txt` bytes. No
scientific falsifier fired and no threshold moved.

## Result

Let `O_5 = Z[zeta_5]`, `J = 1 + zeta_5^2`, `phi = -(zeta_5^2 + zeta_5^3)`, and
for a rational integer `m >= 2` let `R_m = O_5/(m)`.

```text
(A)  ord_m(zeta_5) = 5                          for every rational m >= 2
(B)  ord_m(J) = lcm(5, ord_m(phi))              for every rational m >= 2
(C)  in any quotient of O_5 in which zeta_5 has order exactly 5,
     lcm(5, ord(phi)) / ord(J) divides 5
```

`ord_m(phi)` is the Pisano period of `m`. Since `det M_J = 1`, the map
`x -> J x` permutes the `m^4` elements of `R_m`, and (B) says the period of
that permutation factors into an invariant part 5, carried by the torsion, and
a part belonging to the chosen modulus.

All three statements are global. Their universal quantifiers are carried by the
written proofs in `PREREG.md`: (A) by an absolute-norm argument, (B) twice and
independently, once by complex conjugation and once by `Z[phi]`-coordinates,
and (C) by a three-line divisibility argument. The verifier audits them on
declared finite carriers.

## The scope boundary, and it is part of the result

(B) is false at a single prime ideal above a split prime. Conjugation permutes
the primes above `p` and fixes none of them, so the first proof of (B) has no
step to take there, and the failure is real, not an artefact:

```text
p = 11, the prime ideal carrying zeta_5 -> 3 in F_11
phi -> 8 with ord(phi) = 10
J   -> 10 = -1 with ord(J) = 2
lcm(5, 10) = 10, ord(J) = 2, ratio 5
```

(C) prices that failure exactly. Over the complete audited carrier of 536 prime
ideals above the 134 split primes below 4000, the ratio took the value 1 in 438
cases and 5 in 98, and no other value in any case. Choosing one prime above `p`
costs the factor five and nothing else.

The word "rational" in (B) is therefore load-bearing. A row asserting the
period law "at every finite place" would be false and falsified by a two-line
computation at `p = 11`.

## Exact audit

```text
structural guards                       4/4 PASS
rational moduli 2..1000                 999 rows
  ord_zeta_5 different from 5             0
  period law firings                      0
orbit census, m in {2,3,4,5,7,11}       6 moduli
  orbit lcm against matrix period         0 disagreements
split primes below 4000                 134
prime ideals audited                    536
  collapse ratio 1                      438
  collapse ratio 5                       98
  any other ratio                         0
lattice sup norms of J^n . 1, n = 1..12  1 1 3 5 8 8 13 34 55 89 89 144
```

Orders are never obtained by a bounded scan. In the matrix route an order is
the least divisor of a multiple `L` for which `A^L = I` has been verified; if
`A^L` is not the identity the falsifier fires rather than the search widening.
The `ord(phi)` loop uses the theorem that the Pisano period is at most `6m`, so
it is exhaustive within a proven bound. Primality uses `isqrt`. No float and no
tolerance appears anywhere.

## Why the status ceiling is candidate-T

Three independent written proofs establish the universal statements, and (B)
has two of them by different routes. The verifier is an exact audit of declared
finite carriers and of every structural identity the proofs use. This supports
a later `T` row at L1 after the required public two-architecture gate and a
separate Canon fold.

## Relation to existing rows

```text
J-BINARY-NORM-INDEX   already owns ord(Jbar) = 15 at the inert prime 2 and the
                      whole-group generation statement there. The m = 2 line of
                      this audit agrees with it and adds nothing to it.
J-HARMONIC-SEAM       already owns O_K^x = mu_10 x <phi> and the
                      principal-branch Log J. No archimedean fact is used here.
J-PROJECTIONS         the archimedean modulus and argument of J, untouched.
SPLIT-PRIME-RAPIDITY-INDEPENDENCE, REDUCED-SPLIT-GENERATOR-HEIGHT
                      concern oriented split-prime rapidity classes. The choice
                      of one prime above p appears here only as the hypothesis
                      under which (B) fails; no statement of theirs is used,
                      restated or extended.
```

## Scope firewall

This result is exact residue arithmetic. It does not interpret the permutation
`x -> Jx` as a physical automaton, does not define or bound any Hamiltonian,
claims no energy quantum, no decoder, apparatus, event, probability, Born law,
dynamics, entropy, spacetime, force, SI value, or physical generation count,
and asserts nothing about the archimedean place or about the eigenvalue moduli
of `M_J`. The collapse factor five is an arithmetic quantity here and is not
read as a selector, an orientation bit, or physics.

No lift between L1 and any of L2 to L6 is assumed or concluded.

```text
SAMPLING NOT PROVIDED.
```

## Publication boundary

This probe changes no Canon, registry, frontier, dependency, evidence, gate,
status, tag, or release file. It seals the mathematical result and its evidence
only. The maximum later public use is two separately locked rows:

```text
J-RESIDUE-PERIOD [T], L1
J-RESIDUE-COLLAPSE-FIVE [T], L1
```

The public claim lock is issue 567 and the immutable preregistration pin is
`04512fc7b5efff94f13ac8f988f248abf16409bb`.
