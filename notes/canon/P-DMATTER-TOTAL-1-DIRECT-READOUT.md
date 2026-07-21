# P-DMATTER-TOTAL-1 independent direct readout (DEFINITION CANDIDATE, NON-CANONICAL)

Status: `DRAFT / DEFINITION-CANDIDATE`

This note answers one routing item of
`notes/canon/P-DMATTER-TOTAL-1-DEFINITION-CANDIDATE.md`:

```text
NEXT DEFINITION-ONLY PASS:
    independent D_direct
```

It proposes the independent direct readout `D_direct` that the ruling in
that note requires. It is not a public probe, preregistration, verifier,
run, or status proposal. It changes no Canon object and authorizes no
promotion. The lane scheduler stays `STOP`; a formal probe stays forbidden
until the definition package is reviewed, merged, and read back from public
`main`, and even then requires its own fresh pin-before-execution.

## Authority pin

```text
Canon:              Public Canon v14
state:              ACTIVE
tag:                canon-v14
activation commit:  f278855cada75691142c02ebad1a75ecc2730db3
content commit:     ab4ea07d15ab1cfa0c403d3c2a74164011ffa0e7
Canon SHA-256:      f9f06af42a9b0b63f806603ddc671ebe6a9e5014b50d230da04a28722ed1a6a2
Canon bytes:        87061
owner row:          QUADRATIC-DECODER-DATA [O]
public anchor:      issue #107 (lane lock); PR #113 definition candidate
future probe:       P-DMATTER-TOTAL-1
```

## The obstruction this removes

The #113 ruling holds the lane at `STOP` in part because a direct readout
built from the same quadratic formulas as the Gram-spectral factor map
would make the target factorization true by definition (outcome leakage).
It therefore requires a `D_direct` from an independently published reading
rule, not defined through `Qcan`, `N_G`, `F_Gram`, or a shared
factorization helper.

This note supplies exactly that: a readout defined purely by field
arithmetic in `Q(zeta_5)`, sharing no quadratic code with the Gram side,
and built entirely from reading rules already published for other public
sectors. Zero new dictionary atoms are introduced.

## 1. The readout

Read the pre-update checkpoint at `n = 0`, piston block only, balanced
signed section `ell(0,1,2,3,4) = (0,1,2,-2,-1)` (the same anchored carrier
and section as #113 Section 1). Form the field element in the public
`CODEC-TR4` power basis, in the multiplicative window of `F_5^*`:

```text
w  = v1 zeta + v2 zeta^2 + v3 zeta^3 + v4 zeta^4   in Z[zeta_5],
     vi = ell(piston_i),  zeta = zeta_5.
```

Then, with `wbar = sigma_4(w)` the complex conjugate and `Tr` the field
trace `Tr_{Q(zeta_5)/Q}`:

```text
support_state   = [w = 0]
total_weight    = (1/5) Tr(w wbar)
branch_weights  = (w_low, w_high),
                  w_low  = (4/5) c^2,   c = Tr(w)/4 the rational component
                                          of w in the split Q + ker(Tr),
                  w_high = total_weight - w_low
density_state   = ZERO_DENOMINATOR if w = 0, else the trace-pairing
                  rank-one map  x -> w (1/5) Tr(x wbar),  normalized by
                  total_weight
normalized_weight_state = ZERO_DENOMINATOR if w = 0, else
                  NORMALIZED((w_low, w_high) / total_weight)
```

Every field is field arithmetic in `Q(zeta_5)`: products, Galois
conjugation, the field trace. No matrix is formed; no `v v^T`, no Gram
matrix, no spectral idempotent, no `Qcan`, `N_G`, or `F_Gram`, and no
helper shared with them.

## 2. The factorization claim

```text
D_direct = F_Gram o Qcan o beta      exactly on all 15625 anchored
                                     checkpoints, every field, with exact
                                     normalization,
```

with `beta`, `Qcan`, `G`, `E_low`, `E_high`, `F_Gram` exactly as frozen in
the #113 definition candidate. The algebraic core is the identity

```text
Tr(zeta^(a-b)) = 5 delta_ab - 1      for a, b in F_5^*,
```

that is: the #113 coordinate Gram `G0 = 5 I - 1 1^T` IS the cyclotomic
Galois-trace Gram of the piston power basis, the same Gram whose normalized
spectrum `{1/p, 1, 1, 1}` is published in `ALPHA-SEED [T]`. The readout is
therefore not a re-encoding of the Gram map; it is an independent object
that provably lands on it.

## 3. Independence pedigree (zero new atoms)

Every ingredient is a public row published for another sector. None was
created for this lane; the #113 prohibition list (`Qcan`, `N_G`, `F_Gram`,
shared helper) touches none of them.

```text
piston = Z[zeta_5], power basis, step = mult by J     CODEC-TR4 [T]
the cyclotomic Galois-trace Gram, spectrum {1/p,1,..} ALPHA-SEED [T]
branch split trace vs spatial base, weights 1/p vs 1  MEASURE-SPATIAL-ONLY [T]
the quadratic leg is the Born square                  READING-SPLIT [D]
the Born square of a cyclotomic amplitude, exact      MEASURE-BORN-VERB [D]
                                                      on BORN-FACE-WEIGHTS [T]
the Galois-Gram density rho = psi psi^dg G / (..)     COUPLINGS-DETERMINE [T]
exponent relabeling is exact gauge                    CARRY-PENTAD [T]
```

The conjugation `sigma_4` (not `sigma_2`) is forced, not chosen: the
`sigma_2` pairing goes negative on a witness, and positivity of the Born
square selects the modulus involution. The polar reading fences the schema
to modulus-side quadratic fields only (mass is a modulus; phase is
argument-side), which is what makes constancy on `Q`-fibers achievable.

## 4. The frame is forced

Of the 120 injective assignments of the four piston slots to powers of
`zeta`, exactly 5 are verb-compatible (multiplication by `J` in the window
equals the axiom step matrix): the consecutive cyclic windows. Adding trace
alignment (all exponents in `F_5^*`, so that the piston character `Tr_4`
equals minus the field trace) selects the window
`(zeta, zeta^2, zeta^3, zeta^4)` uniquely. The exponent relabeling among
the 24 orderings is exact gauge (`CARRY-PENTAD`), giving identical scalar
MatterData.

## 5. Falsifier

```text
F-DMATTER-DIRECT-FACTOR   exists an anchored checkpoint x with
                          D_direct(x) != (F_Gram o Qcan o beta)(x) in any
                          field, canonical frame.
F-DMATTER-DIRECT-FRAME    the frame selection is empty or non-unique (no
                          injection, or more than one, satisfies verb
                          compatibility plus trace alignment).
```

## 6. Verification status (incubation lane, candidate grade)

The factorization and the frame have been verified exact in the incubation
lane, prereg frozen before compute, on two architectures byte identical
(x86_64 and aarch64), with an independent-code-path break attempt (trace
table only, no polynomials, no matrices, no `Fraction`) that failed to kill
on six routes. Result: candidate-T (factorization and frame),
candidate-D (pedigree). One frozen frame predictor fired first-class and is
archived: the `CODEC-TR4` fingerprint is window invariant, so frame
selection stands on verb compatibility plus trace alignment, not on the
fingerprint. Pins (incubation lane):

```text
prereg  sha256 13ab9a03be33a7fdc29e5206e45b9e5d4711a0ab45b063b48d767e7515faf835
verify  sha256 0630d82fc45982d64c41dd0403ea3dc5fd5caecd8272606b5881cf9126240ebd
stdout  sha256 bc16079ee7c5f8d5ff72047271186304b742d13ea35ca3ee81d13ec43b723d43
        (28 of 29 gates PASS; all 27 core gates PASS; exit 0; two
         architectures byte identical)
break   sha256 9c23a2919d484f4370260d4190e21c6168e8989f8612c0b78fd77dc861944764
        stdout sha256 cb6b7248e359f1e428f8cbe1c1b66632d451b427871c6b6d6d7aa00d13bfcb2e
```

This is candidate evidence, carrying no authority. The public two-platform
gate stands as the promotion requirement: a pinned public probe branch
whose verifier is pinned before first execution and reproduced on the
GitHub x86_64 check at PR time, with neutral public environment fields.

## 7. Proposed lane actions

If the lane owner adopts this definition pass:

```text
D_direct                 := the readout of Section 1
MatterData_quadratic     := the #113 Section 5 tagged union, with the
                            direct-side definitions as the owning field
                            definitions and F_Gram as the factor map under
                            test
frame clause             := CODEC-TR4 power basis, F_5^* window, verb plus
                            trace-alignment selection; exponent relabeling
                            exact gauge
measure fence            := modulus-side quadratic fields only (polar split)
dependency edges (new)   += QUADRATIC-DECODER-DATA -> MEASURE-SPATIAL-ONLY
                            QUADRATIC-DECODER-DATA -> ALPHA-SEED
probe positive content   := the factorization equality with exact
                            normalization on all 15625 anchored checkpoints,
                            two platforms byte identical, closing the open
                            identity "coordinate Gram = cyclotomic
                            Galois-trace Gram on the piston power basis"
```

## 8. What stays open

The physical measure dictionary ruling (the readout fields are exact
nonnegative rationals, not probabilities), the stage and leg wording, the
completion-contract manifests, and every remaining identifier-valued slot
of `DEF-DECODER-COMPLETION-CONTRACT` are untouched by this note. `STOP`
stands until the lane owner adopts a definition pass and reads it back from
public `main`.
