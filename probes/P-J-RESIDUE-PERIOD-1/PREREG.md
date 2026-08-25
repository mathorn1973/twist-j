# P-J-RESIDUE-PERIOD-1 preregistration

Status: `PREREGISTERED / RESULT-EXPOSED / PROOF-FIRST`

Three elementary unconditional statements about residue rings of `Z[zeta_5]`,
and the exact scope boundary one of them forces on the other two. The theorems
are carried by the written proofs below; the verifier is a finite exact audit,
not a discovery engine. The result is exposed before execution: every gate
passes, the period law holds on the whole declared rational range, and it fails
at an oriented place by exactly the factor five.

## Public identity, authority, and action layer

```text
probe:           P-J-RESIDUE-PERIOD-1
public claim:    issue #567
probe owner:     A. M. Thorn / delegated session residue-period-2026-08-25
branch:          probe/P-J-RESIDUE-PERIOD-1
basis:           Public Canon v64, main 505f4096453a52bacb8c8de26583b38874ea408b,
                 tag canon-v64, SHA256SUMS 5 of 5 OK
action layer:    L1 (state; exact residue arithmetic). No layer lift, no
                 physical claim, no canon edit by this probe.
lineage:         carries in the incubation promotion
                 PROMO-C-THOOFT-FINITE-PLACE-PERIOD-1 (2026-08-25), an
                 incubation-lane identifier only; the lane verifier pins are
                 recorded there; this probe re-derives everything fresh with
                 new files and claims none of that lane's framing.
```

## Falsifier, first

```text
(A),(B)  one rational integer m >= 2 with ord_m(zeta_5) different from 5, or
         with ord_m(J) different from lcm(5, ord_m(phi))
(C)      one quotient of Z[zeta_5] in which zeta_5 has order exactly 5 and
         lcm(5, ord(phi)) / ord(J) is neither 1 nor 5, or a proof that (B)
         holds at every prime ideal, or a demonstration that the p = 11
         witness is miscomputed
```

A pinned-gate FAIL on rerun is the operational falsifier. No threshold is
numerical; every comparison is exact equality between integers.

## The statements

Let `O_5 = Z[zeta_5]`, `J = 1 + zeta_5^2`, `phi = -(zeta_5^2 + zeta_5^3)`, and
for a rational integer `m >= 2` let `R_m = O_5/(m)` with unit group `R_m^x`.

```text
(A)  ord_m(zeta_5) = 5                                for every m >= 2
(B)  ord_m(J) = lcm(5, ord_m(phi))                    for every m >= 2
(C)  in any quotient of O_5 in which zeta_5 has order exactly 5, with
     L = lcm(5, ord(phi)) and k = ord(J), the quotient L/k divides 5;
     the value 5 is attained, so (B) does not extend to a single prime
     ideal above a split prime
```

`ord_m(phi)` is the Pisano period of `m`, because `phi^n = F_n phi + F_(n-1)`.
Since `det M_J = 1`, the map `x -> J x` is a permutation of the `m^4` elements
of `R_m`; (B) states that the period of that permutation factors into an
invariant part 5, carried by the torsion of the unit group, and a part
belonging to the chosen modulus. (C) prices the boundary: the word "rational"
in (B) is load-bearing, and choosing one prime above `p` costs exactly the
factor five and nothing else.

## The six fields

```text
EQUATION     (A), (B), (C) exactly as displayed above, with
             J = 1 + zeta_5^2, phi = -(zeta_5^2 + zeta_5^3),
             J . phi = zeta_5, det M_J = 1, char M_J = Phi_5(X - 1).
CODE         probes/P-J-RESIDUE-PERIOD-1/verify.py, standard library only,
             integer arithmetic only, no float in any assertion or printed
             field, deterministic, about three seconds and well under 120 s,
             run from the repository root, environment
             LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
             TZ=UTC.
CARRIER      none external. Declared finite carriers, all exhaustive inside
             their stated bounds: every rational modulus 2 <= m <= 1000;
             the complete orbit census of x -> Jx on R_m for
             m in {2, 3, 4, 5, 7, 11}; every prime ideal above every split
             prime p = 1 mod 5 below 4000, that is 134 primes and 536 ideals.
             The universal statements are carried by the proofs, not by the
             sweeps.
SYSTEMATICS  four structural guards run before any order is computed and
             abort the run on failure: J . phi = zeta_5, det M_J = 1,
             char M_J = Phi_5(X - 1), zeta_5^5 = I. An order is never a
             bounded scan: for the matrix route it is the least divisor of a
             multiple L for which A^L = I has been checked, and if A^L is not
             the identity the falsifier fires rather than the search widening.
             The Pisano loop uses the theorem pi(m) <= 6m, so it is exhaustive
             and not truncated; exceeding that bound raises rather than
             returning. Two independent representations audit the same
             quantity: 4x4 integer matrices for the period law, and exhaustive
             orbit enumeration for the census moduli. Primality uses isqrt,
             so no float enters even the search.
THRESHOLD    any firing kills the probe. Firings are counted separately for
             (A), for (B), for the census disagreement, and for any collapse
             ratio that is neither 1 nor 5, and their sum sets the exit code.
             No tolerance exists anywhere.
LAYER        L1. The two proposed rows are exact residue arithmetic. No live
             row moves and no obligation is closed by this probe.
```

## The written proofs

### (A) The torsion has order five in every rational residue ring

`zeta_5^5 = 1`, so the order divides 5. Suppose `zeta_5^k = 1` in `R_m` for
some `1 <= k <= 4`. Then `m` divides `1 - zeta_5^k` in `O_5`, so the absolute
norm `N(m) = m^4` divides `N(1 - zeta_5^k) = Phi_5(1) = 5`. For `m >= 2` this
is impossible. Hence the order is exactly 5.

### (B) First proof, by complex conjugation

Let `c` be the automorphism `zeta_5 -> zeta_5^-1` of `O_5`. It fixes
`phi = -(zeta_5^2 + zeta_5^3)`, because conjugation exchanges the two summands.
Since `m` is a rational integer, `c(m O_5) = m O_5`, so `c` descends to a ring
automorphism of `R_m`.

From `J . phi = zeta_5` we have `J = zeta_5 phi^-1` in `R_m^x`. Suppose
`J^n = 1`. Then `zeta_5^n = phi^n`. Applying `c` gives `zeta_5^-n = phi^n`.
Hence `zeta_5^(2n) = 1`, so `5 | 2n`, so `5 | n`, so `zeta_5^n = 1` and
therefore `phi^n = 1`, so `ord_m(phi) | n`. Both divisibilities give
`lcm(5, ord_m(phi)) | n`. Conversely `J^L = zeta_5^L phi^-L = 1` for
`L = lcm(5, ord_m(phi))`. Therefore `ord_m(J) = L`.

### (B) Second proof, independent, by coordinates

`{1, zeta_5}` is a `Z[phi]`-basis of `O_5`: the change of basis from
`{1, phi, zeta_5, phi zeta_5}` to `{1, zeta_5, zeta_5^2, zeta_5^3}` has
determinant 1, since `phi = -(zeta_5^2 + zeta_5^3)` and
`phi zeta_5 = 1 + zeta_5 + zeta_5^2`.

In that basis, using `zeta_5 + zeta_5^-1 = phi - 1`,

```text
zeta_5^1 = 0        + 1 . zeta_5
zeta_5^2 = -1       + (phi - 1) . zeta_5
zeta_5^3 = (1-phi)  + (1 - phi) . zeta_5
zeta_5^4 = (phi-1)  + (-1) . zeta_5
```

The four `zeta_5`-coordinates `1, phi-1, 1-phi, -1` are all units of `Z[phi]`,
so none of them lies in `m Z[phi]` for `m >= 2`. Hence no `zeta_5^k` with
`1 <= k <= 4` is congruent modulo `m` to an element of `Z[phi]`, so the cyclic
subgroups generated by `zeta_5` and by `phi` intersect trivially in `R_m^x`. In
an abelian group with `<a>` and `<b>` intersecting trivially,
`ord(a b^-1) = lcm(ord a, ord b)`. With `a = zeta_5` of order 5 and `b = phi`
this is (B).

### (C) The collapse divides five, and five is attained

Let `Q` be any quotient of `O_5` in which `zeta_5` has order exactly 5, write
`d = ord(phi)`, `L = lcm(5, d)` and `k = ord(J)`. Then `k | L`, because
`J^L = zeta_5^L phi^-L = 1`. From `J^k = 1` we get `zeta_5^k = phi^k`; raising
to the fifth power gives `zeta_5^(5k) = phi^(5k)`, and `zeta_5^(5k) = 1`, so
`phi^(5k) = 1` and `d | 5k`. Also `5 | 5k`. Hence `L | 5k`. Writing `L = k t`
gives `k t | 5 k`, so `t | 5`. Therefore `k` is `L` or `L/5` and nothing else.

The value 5 is attained. Take `p = 11`, which splits in `Q(zeta_5)`, and the
prime ideal carrying `zeta_5 -> 3` in `F_11`, where `3^5 = 243 = 1 mod 11`.
Then

```text
phi -> -(3^2 + 3^3) = -36 = 8 mod 11,   ord(8) = 10
J   -> 1 + 3^2 = 10 = -1 mod 11,        ord(-1) = 2
L = lcm(5, 10) = 10,  k = 2,  t = 5
```

Conjugation does not fix a single prime above a split prime, it permutes the
primes above it, so the step "apply `c`" in the first proof of (B) is
unavailable there. (B) and (C) are consistent: at a rational modulus the
modulus is conjugation-stable and `t = 1` always; at one oriented prime `t` can
be 5.

## Proposed fold edits (a later sealed fold, not this probe)

Registry, two rows, tab-separated, canon section 1:

```text
J-RESIDUE-PERIOD	T	at L1 for O_5 = Z[zeta_5] and every rational integer m >= 2, in R_m = O_5/(m) with J = 1 + zeta_5^2 and phi = -(zeta_5^2 + zeta_5^3): ord_m(zeta_5) = 5 and ord_m(J) = lcm(5, ord_m(phi)), where ord_m(phi) is the Pisano period of m; det M_J = 1 makes x -> Jx a permutation of the m^4 elements of R_m, so the period of that permutation factors into an invariant part 5 carried by the torsion and a part belonging to the modulus; the word rational is load-bearing and the statement is false at a single prime ideal above a split prime, which J-RESIDUE-COLLAPSE-FIVE owns; the inert case p = 2 with order 15 is already owned by J-BINARY-NORM-INDEX and is cited here, not restated; no archimedean statement, no unit-group structure beyond what J-HARMONIC-SEAM already owns, no automaton interpretation, no Hamiltonian spectrum, no energy quantum, no decoder, apparatus, event, measure or L2-L6 lift	1. The axiom and the two projections	probes/P-J-RESIDUE-PERIOD-1	fires if some rational integer m >= 2 has ord_m(zeta_5) different from 5, or ord_m(J) different from lcm(5, ord_m(phi)); a non-rational modulus, an ideal, or a physical reading is outside scope; a pinned-bundle, transcript or architecture mismatch without an exact mathematical negation is integrity STOP, not a scientific falsifier
J-RESIDUE-COLLAPSE-FIVE	T	at L1 in any quotient of Z[zeta_5] in which zeta_5 has order exactly 5, with L = lcm(5, ord(phi)) and k = ord(J), the quotient L/k divides 5, so k is L or L/5 and nothing else; the value 5 is attained, the smallest witness being the prime ideal above 11 carrying zeta_5 -> 3 in F_11, where ord(phi) = 10 and ord(J) = 2 against L = 10; consequently J-RESIDUE-PERIOD does not extend to one chosen prime above a split prime, and the cost of that choice is exactly the factor five and nothing else; the choice named here is the choice of one prime ideal above p and is not a claim about SPLIT-PRIME-RAPIDITY-INDEPENDENCE, REDUCED-SPLIT-GENERATOR-HEIGHT, any residual orientation bit, or any selector; no physical reading of the collapse factor, no decoder, measure or L2-L6 lift	1. The axiom and the two projections	probes/P-J-RESIDUE-PERIOD-1	fires if some quotient with zeta_5 of order exactly 5 has L/k neither 1 nor 5, if k does not divide L, or if the p = 11 witness is miscomputed; reading the factor as physics or as a selector is outside scope; a pinned-bundle, transcript or architecture mismatch without an exact mathematical negation is integrity STOP, not a scientific falsifier
```

Frontier: no change. No live obligation is closed and none is opened by this
probe. Ledger delta: claims +2, T +2.

## Dependencies cited, not restated

```text
J-BINARY-NORM-INDEX   owns ord(Jbar) = 15 at the inert prime 2 and the
                      whole-group generation statement there; (B) at m = 2
                      agrees with it and adds nothing to it
J-HARMONIC-SEAM       owns O_K^x = mu_10 x <phi> and the principal-branch
                      Log J; this probe uses no archimedean fact
J-PROJECTIONS         the archimedean modulus and argument of J, untouched
```

## Non-claims

Nothing about the archimedean place, the eigenvalue moduli, entropy, any
automaton or cellular-automaton interpretation, any induced Hamiltonian or its
spectrum, any energy quantum, any decoder, apparatus, event, probability, Born
law, dynamics, spacetime, force, SI value, or physical reading of either the
period or the collapse factor. No selector of an exponent, an orientation, a
prime or a carrier is claimed. No lift to L2 through L6 is claimed.

```text
SAMPLING NOT PROVIDED.
```
