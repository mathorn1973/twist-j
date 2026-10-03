# Independent implementation review: work-scope freeze

NON-CANONICAL, L1, ordinary disclosed independent-author review. No new primary implementation has been read. No scientific program has run in this stage. Scientific execution requires the coordinator's authority/collision release and an immutable public preregistration/code pin; this document alone is not that release.

## Contracts and exposure

Decoder contract: `decoder/INTERFACE.md`, SHA-256 `5530f8f0da3ad13eeb5210e3b89abb01ea41e02a706a403f2069fde6c3b5b525`. Contact contract: `native/CONTRACT-DRAFT.md`, SHA-256 `e10bbf3db7d6d16759d2e64073e3051310d9c445b98d41208fd549e6466bf13f`. Public main: `5e872c22a18043c8126945a982efad55472cea82`. A later formal contract may add custody details but any mathematical/API change requires explicit review before execution.

The earlier lambda-depth census, norm-separation argument, 3150 strip cardinality and old rational-modulus inverse are exposed. Native generator mathematics, #1342, synchronized no-write, #987 and #1003 outcomes are exposed. An old #987 implementation embedded in an issue comment was seen during collision review. The original #1346 verifier remains unread. Neither new decoder primary source nor new contact primary source has been read, imported or run. Independence here means separate derivation and implementation, not blinded predictions. The author disclosed a prospective native receiver obstruction before this freeze.

## A. Decoder method, before code

Implement an independent cyclotomic polynomial ring by convolution and reduction modulo Phi5. Build the multiplication matrix of lambda^6 and invert it over exact Fractions. A residue is recognized by the fractional class of that inverse applied to a coefficient vector. Enumerate the 5^6 canonical digit representatives into an independent signature-to-digits dictionary. This does not use successive division by lambda as the ideal oracle and does not identify the quotient's additive group with F5^6; its characteristic is 25.

Enumerate the inherited complete box [-8,8]^4 to build a strip dictionary by quadratic coordinates and ideal signature. Use exact integer candidate-trace inversion and positivity/norm rejection, then normalize both traces and residue using J or J^-1. For the independent termination argument use u: at v<0, the inverse step gives (u+v,u+2v) with strictly smaller positive u; at v>u, the forward step gives (2u-v,v-u), again smaller positive u; at v=u one forward step lands on v=0. Do not rely on the incorrect informal suggestion that S0 always decreases. The public transformations and half-open strip are unchanged.

The oracle returns the original coefficients, unique strip coefficients, signed unit exponent and norm, or rejects. It must cover every syntactically well-formed reading, including nonrepresentable integral trace pairs. Its proof obligation includes termination before representability is known, uniqueness from the inherited norm bound, exact reversal and negative exponents.

The reviewer program will call the primary API as a black box only after the reviewer's own bytes are frozen. Frozen test families:

- All 3150 strip points, translated by J exponents -12,-3,-1,0,1,3,12: exact encode/decode, four returned fields, data-map intertwining and inverse identities.
- Selected strip boundary/norm examples at exponents -1000,-101,101,1000 for large integer and signed normalization behavior.
- Every one of 15625 residue classes with trace pairs derived from (u,v)=(1,0),(1,1),(2,1),(13,6),(27,8), plus nonpositive, nonintegral and over-bound pairs. Compare image membership and accepted coefficients with the independent oracle. A changed datum that is another valid image must be accepted.
- Both data maps on all residue classes with several arbitrary integer trace pairs, including readings outside the image; compare exact formulas and both compositions.
- Strict type/shape/digit rejection, including booleans, floats, strings, generators, wrong lengths, and digits outside0..4. No silent coercion or residue reduction. Check tuple outputs and frozen record behavior.
- Independently verify ring units, multiplication-matrix inverse, quotient cardinality/characteristic, uniqueness of the strip-key map and every returned residue. These are finite checks, not substitutes for the totality proof.

## B. Actual-U contact method, before code

Use independently transcribed homogeneous affine matrices of the five full six-coordinate generators. Compute actual selected words from the full state and parity-of-popcount clock, never by a requested target. Retain all 15625 initial states and their complete three-step states, counters and selected indices in a deterministic table. Check the closed projection against the full matrix action.

Independently derive the five affine fibre actions for each t=1,2,3 as `epsilon_t(z)*F+k_t(z)`, using actual words and exact matrix products. A separate proof route is frozen: if source-sum gain s=0, the receiver is source-blind. If s!=0, changing variables from (x,y) to (z,y) in the target equations and using B.w=1 forces epsilon_t(z) to be constant in z. The prospective actual sign profiles are nonconstant at each of the three times. This analytical expectation is disclosed before execution; a mismatch is retained rather than repaired. The primary author's collision/translation route is not needed for this proof.

Also inspect the complete 75000 projected receiver configurations at each t, including all25 inputs for each configuration. Obtain outputs by lookups in the independently generated full-state table. Save survivor counts by t and s, and for every rejection the lexicographically first falsifying input, actual and required readings, plus total mismatches. A receiver survivor fires the stronger receiver obstruction and STOPs any full negative verdict; a full positive verdict would additionally require the source-retention lift, not merely a receiver survivor.

The test is confined to the fixed independent affine source/receiver lines and the SAME block readers from the contact contract. It does not test all native contacts or re-own old transient-writing results. The full 438750000000 parameter-tuple count is a class-description fact, not a promise to enumerate it directly.

## Freeze, falsifiers and disposition

The reviewer will now write its own two programs, perform only source inspection/static parsing and administrative hashing, and save a byte freeze before any primary-source exposure. No expected stdout is invented. Actual stdout, stderr, environment, commands and evidence hashes will be saved only after authorized execution. No primary imports or predecessor scientific execution are allowed during preparation.

Any independent-oracle/API disagreement, omitted case, bad normalization/reversal, image-recognition error, changed fixed contract, source/projection mismatch, receiver survivor, wrong trace/coordinate/counter, hidden source input or non-native selected word is retained as an exact counterexample or scoped STOP as appropriate. Integrity and architecture failures are not silently reported as mathematical falsifiers. No in-place repair after a failed frozen run; a revision needs a new disclosed freeze and approval under the task's public procedure.

Finite checks are at most candidate-C until the applicable gates; analytical conclusions need complete proofs. No physical availability, finite storage of unbounded traces, native preparation/renewal, energy law, occurrence law, or other open decoder obligation is supplied. This reviewer performs no public writes.
