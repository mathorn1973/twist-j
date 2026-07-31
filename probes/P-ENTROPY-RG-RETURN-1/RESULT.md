# P-ENTROPY-RG-RETURN-1 result

```text
probe:       P-ENTROPY-RG-RETURN-1
pin:         db57f52eddaaba2529c22a072014ba6db0ac06b6
gates:       13 of 13 PASS
falsifiers:  none fired in this probe
status:      C, computed at the declared finite range
layer:       L5 finite kernel structure; no lift is named or licensed
basis:       Public Canon v28, tag canon-v28, content commit 86a04600,
             canon/SHA256SUMS verified 5 of 5 before the pin
```

## What was decided

`ENTROPY-BLOCK-HALVING [C]` states that the renormalized block maps are
exactly two-to-one on the recurrent core, so coarse graining here is a
semigroup and not a group. A semigroup of that kind is normally read through
its fixed points and the spectrum of its linearization there. This probe
computes that object exactly, at the dyadic scales `k = 0..14` and both
letters, and the answer is negative in the interesting direction.

```text
k = 0             each letter has exactly one fixed state on the core: the
                  reflection centres 3 (C_D + V_E) = (1,3,4,2,1,3) for
                  eps = 0 and 3 C_D = (1,3,4,2,3,3) for eps = 1, both in the
                  size-10 component, each with 125 further fixed states off
                  the core, each with multiplier exactly minus the identity,
                  characteristic polynomial (x + 1)^6; no state of F_5^6 is
                  fixed by both letters
k = 1, 5, 9, 13   the fixed set is exactly the opposite living half
                  H_(1-eps): 3125 states meeting all 313 components, and the
                  multiplier at every one of them is exactly the identity,
                  characteristic polynomial (x - 1)^6; the off-core fixed
                  count is 3125 at k = 1 and 0 at k = 5, 9, 13
every other k     no fixed state at all, on the core or off it
every k in range  the image of the block map on the core has exactly 3125
                  states, which re-audits ENTROPY-BLOCK-HALVING over a range
                  four scales wider than the row it re-audits
```

The only multiplier matrices realized at any fixed state anywhere in the
range are the identity and its negative.

## What that means, stated at the earned strength

There is no hyperbolic fixed point of this coarse graining at state level in
the tested range. Where fixed states exist at a scale beyond `k = 0` they are
not isolated: they are a full living half, and the linearization there is the
identity, so there is no expanding or contracting datum to read. The
structure is not a fixed point with a spectrum but a finite return: within
the tested range the fixed-point data depend on the scale only through
`k mod 4`, and the block map returns exactly at the scales whose block length
satisfies `2^k = 2 mod 5`.

The scales with `2^k = 1 mod 5`, namely `k = 0, 4, 8, 12`, carry no
full-half return. This is the sharp side of the statement and gate G13 pins
it: the semigroup does not come back to the identity on the core at the
scales where the block length is a unit residue; it comes back at the scales
where the block length reduces to the residue of a single two-tick stroke.

The coincidence between that residue class and the order of `J` modulo the
ramified prime, recorded elsewhere as `RAMIFIED-TM-LIFT [T]`, is arithmetic.
This probe does not read it physically, does not identify it with any
registered physical quantity, and does not depend on it: G13 is checked
directly from `2^k mod 5` and the computed fixed sets.

## Scope, restated so no summary can exceed it

Everything above is a finite computation on the declared carrier at
`k <= 14`. No continuum limit, scaling limit, critical exponent, monotone
scale function, C-function, positivity statement, measure, ergodic claim, or
L6 statement follows, and none is asserted. Nothing here closes, moves, or
touches any live `H` or `O` row. The registry, the frontier and the Canon are
not edited by this probe.

## Prior falsification, disclosed rather than buried

The incubation candidate that preceded this probe preregistered the opposite
hypothesis, that the block maps have a nonempty fixed set at every scale.
That hypothesis was falsified by its own run, was archived rather than
repaired, and is the reason the gates here are written around emptiness. No
threshold was moved: this is a new freeze of a different statement. The full
disclosure, including the fact that the frozen range was known to the author
in advance, is in the pre-pin development section of `PREREG.md`.

## Follow-up, not performed here

A registry row for this result and a Canon paragraph are a separate sealed
integer-versioned fold with new hashes, a new tag, and an updated
`STATUS.md`. They are not part of this probe and are not proposed inside
`canon/`. The candidate row and the exact edits a fold would make are written
up under `notes/` as a non-canonical proposal.
