# RESULT C-RG-FIXEDPOINT-1, 2026-07-31

```text
candidate:   C-RG-FIXEDPOINT-1 (project incubation lane, no authority)
prereg:      PREREG-C-RG-FIXEDPOINT-1_2026-07-31.md
             sha256 742f767680d0ef0d0d67a583fd54ec52c6a2a64cc76779bfb91c5e5075f3380f
verifier:    verify_rg_fixedpoint_1.py
             sha256 06f701b392f4964a12123ba852074f5c14faa1dcef86f33f968ae5cfd725c5f6
run:         exit 0, stdout 5102 bytes
             sha256 ecd8ad12e50bd7a810c7b98d5a0deadb0b5ddb4ee2387d6b3bca1892bc3f0d17
             env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
             TZ=UTC; Linux x86_64, Python 3.11.15; audit rerun byte-identical,
             wall 2 s
breaker:     break_rg_fixedpoint_1.py
             sha256 9645dd687dbe32b5376c890dc4fa776685a82630390ee4c7fcb3b21b4f37ae08
             stdout sha256 85cdc91a3460a221586f54a407a441b628ca290fed45fc041bf0f386df4ba85e
             BREAKER 8/8 NO BREAK FOUND
currency:    Public Canon v28, tag canon-v28, content commit 86a04600,
             CANON sha256 4b720846..., SHA256SUMS 5/5 OK, clone head 3161cbc7
platform:    single architecture, single session. Everything below is at most
             candidate grade; no computation-grade public claim is made.
```

## Gate outcome

All 11 audit gates PASS (census, halves, affinity, linear parts, word and
multiplier audits, charpoly self-tests, public halving re-audit, k = 0 and
k = 1 floors, half law). The basis was current and the implementation is
double-checked by an independent literal-walk code path (breaker B03, B05,
B07).

## The result, with labels

### candidate-C. The fixed-point tower of the block maps, k = 0..12

```text
k mod 4 = 1  (k = 1, 5, 9)    Fix(Phi^(k)_eps) = H_(1-eps) EXACTLY,
                              3125 states, every recurrent component,
                              singlet contributes 5; the multiplier at
                              EVERY fixed state is the identity matrix
                              (one distinct multiplier, charpoly (x-1)^6,
                              M^2 = I, hence M = I; breaker numeric
                              columns confirm at 100 samples)
k = 0                         exactly one fixed state per letter, both in
                              the singlet, distinct, none shared; the
                              states are the d and e reflection centers
                              3 C_D and 3 (C_D + V_E); multiplier -I,
                              charpoly (x+1)^6 (hand derivation D3 held)
all other k in 2..12          Fix EMPTY on the core (and the off-core
                              diagnostic count is 0 as well)
halving                       |image| = 3125 at every k = 0..12 (public
                              row re-audited at 0..10, extended at 11, 12)
```

Breaker extension, outside the frozen range, recorded as a breaker
observation: the same pattern holds at k = 13 (full-half return, 3125) and
k = 11, 12, 14 (empty). The tower is therefore periodic with period 4 across
four full periods of tested dyadic scale, k = 0..14.

Convention robustness: the opposite composition convention gives exactly the
letter-swapped tower at odd k and the same tower at even k (breaker B06);
nothing depends on a hidden convention choice.

### F, first class. H1 EXISTENCE fired

The frozen hypothesis "a nonempty fixed set at every scale k = 0..12" is
FALSE. Nine of the thirteen scales have no fixed point at all. Per the
frozen falsifier map this kills the strong reading that started the lane:

```text
DEAD (tested range, state level, binary leg): the decoder as a projection
onto hyperbolic RG fixed-point data. There is no isolated fixed point with
a nontrivial linearization anywhere in k = 0..12. Where fixed points exist
they are a full living half with IDENTITY multiplier: no expanding or
contracting spectrum, no exponent-type datum. A beta-style critical
exponent cannot be read from state-level block-map fixed points.
```

H2 (spectra in {1,-1}) PASSED, but degenerately: the only spectra realized
in the whole range are (x+1)^6 at k = 0 and (x-1)^6 with M = I at the
return scales. H0 and H3 PASSED.

### candidate-C fact, candidate-H reading. The period-4 return law

The computed fact: within k = 0..12 (breaker: ..14), the fixed-point
structure of Phi^(k)_eps depends on k only through k mod 4, and the block
map RETURNS at k = 1 mod 4: it is the identity, to first order and
pointwise, on the opposite living half. The coarse-graining semigroup of
the binary leg has no attracting fixed point at state level; it has a
finite return clock.

The reading (H, no authority, stated with its falsifier): the dyadic scale
enters only through 2^k in F_5^*, which is J_lambda^k by RAMIFIED-TM-LIFT
[T] (J_lambda = 2, order 4). The return scales are exactly those with
J_lambda^k = J_lambda, that is, block length 2^k congruent to 2 mod 5: the
block behaves like a single two-tick mirror stroke. Note the sharp side
fact: J_lambda^k = 1 (k = 0 mod 4, block length 1 mod 5) does NOT return;
the semigroup never comes back to the identity on the core, it comes back
to its one-tick mirror. Falsifier of the reading: any scale k = 1 mod 4
without the full-half identity return, or any nonempty fixed set at
k = 2, 3 mod 4 or at k = 0 mod 4 with k > 0, in any extended range. Tested
and held through four periods (k = 0..14). Per the public convention this
is an arithmetic consonance claim, not a physical identification.

## Consequence for the RG inventory and the decoder discussion

The missing object 5 of the 2026-07-26 RG inventory (fixed points of the
flow) is now computed at state level, and it is not a fixed point in the
RG sense; it is a period-4 return. Object 4 (a monotone C(mu) function)
remains [O] and is now the only remaining carrier for exponent-type data
on the binary leg, together with the cell and measure levels
(ENTROPY-AFFINE-COCYCLE [C] period four is the same clock seen in gauge;
this lane shows it gauge-free at state level). The critical-exponent
analogy that motivated the lane survives in one precise sense only: the
scale acts through a finite cyclic shadow, so any continuum exponent must
come from the measure layer (L6), not from state-level linearization.

## Status of the candidate

```text
C-RG-FIXEDPOINT-1: COMPLETE. Survived one honest independent break pass
(8/8, including an out-of-range extension attack). H1 falsification is
first class and archived. Promotion proposal packaged as
PROMO-C-RG-FIXEDPOINT-1.md. Nothing in this lane edits any registry,
frontier, or Canon on either line.
```
