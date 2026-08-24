# F-CENSUS-ERGODIC-BIJECTION-313: fired falsifier, archived

```
STATUS   FALSIFIED [candidate-F]. Archived, not deleted. The threshold was
         not moved. This record exists so the dead branch cannot be
         re-derived by anyone reading only the surviving results.
DATE     fired 2026-07-25, same day as the claim
CLAIM    |M_e(U_hat)| = 313, one ergodic invariant measure per census
         component; invariant simplex Delta^312
SOURCE   C-CENSUS-RETURN-COCYCLE-1, branch BIJECTION, 9 of 9 gates PASS
FIRED BY COUNTERAUDIT-CENSUS-CONTEXT-625 (external, independent), then
         reproduced in this session by a third construction
TRUTH    |M_e(U_hat)| = 625. See C-CENSUS-ORIENTED-ERGODIC-625-1.
```

## Which falsifier fired

Falsifier 5 of the original prereg, in its own words: "an exhibited second
ergodic invariant measure on some Y_A whose return group this candidate
reports transitive." It fires on all 312 generic components at once. Each
generic Y_A splits into two disjoint nonempty invariant clopen sets. The
singlet does not split. Hence 2 x 312 + 1 = 625.

## Root cause, precisely

The falsified verifier tested reachability of the fibre LABEL over the
coarse cylinder [kappa_{-1} = s]. That is not the minimality criterion for
a skew product. Minimality requires reaching a target fibre point over
arbitrarily FINE base cylinders, and the coarse cylinder merges two
radius-1 context sectors that the dynamics keeps apart.

```
what was proved         on the 10-point half of a generic component, two
                        involutions generate D_5 of order 10 and act
                        transitively on the 10 state labels
what was concluded      Y_A is minimal, hence uniquely ergodic
why that does not follow the base point moves with every return word. A
                        transitive action on labels over a coarse cylinder
                        is compatible with two disjoint minimal sets that
                        each meet every label at a DIFFERENT context.
the exact resolution    D_5 is the monodromy of the coarse symbolic
                        quotient. C_5 is the return group of one real
                        oriented cell. The reflections are exactly the
                        coarse operations that appeared to cross cells and
                        do not exist in the refined system.
first radius that sees  window length 5. Lengths 2, 3, 4 give 313; lengths
it                      5 through 64 give 625, in past-heavy, balanced and
                        future-heavy alignments alike.
```

## Why the earlier break attempt missed it

Eight attacks were run and all survived, including two aimed at exactly the
semigroup-versus-group gap. Both were aimed at the wrong resolution:

```
G08 realisability   asked whether every element of the COARSE group occurs
                    as a real factor of the derived gap sequence. It does.
                    Irrelevant: the group was the wrong group.
A3 orbit            asked whether every point of A_s reaches every other
reachability        point of A_s on a real Thue-Morse orbit. It does, in 27
                    ticks. Irrelevant: it never asked whether the base
                    point returns to a fine neighbourhood at the same time.
A2 subset attack    searched every proper subset of A_s for joint
                    invariance. Found none. Irrelevant for the same reason:
                    the invariant sets are not subsets of A_s, they are
                    subsets of the fibred product.
```

The missing attack has a name now, and it is the one that fires:

```
A9 CONTEXT-REFINEMENT   recompute the decomposition as a function of context
                        radius and window alignment. Never accept a
                        decomposition computed at one radius.
```

That attack is now gate G02 of the successor candidate and is mandatory for
any future claim about invariant measures of a driven finite machine.

## What survives from the falsified branch

Every finite computation survives. Only the type of the conclusion was wrong.

```
survives [candidate-C]  census 312 x 20 + 1 x 10, |R| = 6250
survives [candidate-C]  living halves 3125 + 3125, four bijections
survives [candidate-C]  first-return words to a symbol are exactly three,
                        the middle one induces the identity
survives [candidate-C]  the coarse radius-1 return group is D_5 of order 10,
                        transitive on each 10-point half, with every element
                        realised along the derived gap sequence
survives [candidate-C]  the H_1 versus b H_1 b half-pattern, 313 and 313
survives [candidate-C]  the living union carries the whole hull: every legal
                        word of length 24 and 32 has image exactly
                        R cap H_last
survives [candidate-T]  measure finiteness: finitely many ergodic measures,
                        all of entropy zero, finite simplex
FALSIFIED               the count 313 and the simplex Delta^312
FALSIFIED               "the maximum-entropy measures of U_hat x M_J are
                        exactly 313 products". The correct extreme set has
                        625 elements, and the full maximum-entropy set is
                        their convex hull Delta^624, not a finite list.
```

## Disposition

```
archive as   C-CENSUS-RETURN-D5-COARSE    the surviving coarse result
archive as   F-CENSUS-ERGODIC-BIJECTION-313 this record
do not       send the old branch to a second architecture. Byte identity of
             a wrong conclusion is not progress.
supersede by C-CENSUS-ORIENTED-ERGODIC-625-1
```
