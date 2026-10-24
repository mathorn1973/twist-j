# Pre-execution analytical review

PUBLIC / NON-CANONICAL / L1. Review date: 2026-10-18.

Reviewer: ChatGPT `admission_inventory`, same-session analytical reviewer.
Reviewed: `PREREG.md`, frozen at
`27de104a74a5daaa3a9940853590ccc7e0e8c4cf`, and the present `PROOF.md`.
Reference target: #1629 at
`217cfc13befc3ab4b14444aed49e3fce7f50a7b7`.

## Exposure and method

I contributed the two-sheet translation-correction idea and received the
author's A-E proposal before this review. This is an exposed analytical
review, separate from the method-independent breaker. I checked the
algebraic derivation, quantifiers, raw witness substitutions and calendar
semantics by reasoning from the stated maps and inherited synchronization
theorem. I did not read `verify.py` or `break.py`, execute scientific code,
or inspect any runtime results.

## Analytical verdict: ACCEPT for A-E

| Claim | Finding |
|---|---|
| A: literal-product obstruction | ACCEPT. The synchronized difference map is `(-1)^k B^(theta(n-1) XOR theta(n+k-1))`. The complement construction supplies arbitrarily late equal endpoint bits for every positive fixed k. Surjectivity of the full reference permutation pulls every late encoded checkpoint back by at least nine actual ticks. The resulting scalar difference map preserves agreement outside the source, contradicting the opposite required local receiver outputs. |
| B: correction classification | ACCEPT. T0 bounds the sheet set to size two. The cyclic-adjacent-pair and T1 tests leave precisely `{0,4}` with deltas `(0,3)` and `{0,1}` with `(1,4)`, plus the five unique singleton schemes. Full-sheet bijectivity follows from the affine branches. |
| C: selected corrected law | ACCEPT. On `{0,4}`, both corrected branches preserve their individual sheets. The identity `g tau^r g = tau^-r` for b and c proves the corrected theta=1 branches involutive. The compound forward-clock inverse uses the previous bit. |
| D: five actual microticks | ACCEPT. The displayed phase carriers are the whole-sheet images under the stated command prefixes. Temporal `dddd` is identity and temporal `eded` is `tau^-2`. The inverse selects the previous block, including at a block boundary. Both branches consume five actual counter increments. |
| E: occupied local receiver | ACCEPT. Direct substitution gives the four full output vectors in section 7. The initial pair differs only in q; both receiver coordinates and all other coordinates initially agree. Both control bits produce receiver `(1,0)` versus `(0,4)`, so the same fixed raw balanced-residue-square read gives opposite signs without reading q, clock or history. |

## Boundaries required for these verdicts

The negative theorem uses the explicit clock-preserving form
`Enc(n,y)=(n,e_n(y))`, simulation of every state of the full `Y_(8,3)`
permutation at every admitted n, one fixed positive k, and fixed disjoint
raw ports. Auxiliary original cells share that clock and the same
source-local preparation condition. Arbitrary nonlinear, time-dependent
encodings are covered. Sparse starts, variable durations, independent
clocks, coupling commands and changing ports are outside this class.

The positive construction is a declared extension. Its block identity
advances n by five; it does not identify this calendar with the compound
n-plus-one sequence. The phase carrier retains all six coordinates and
has the stated inverse on every legal slice. The source distinction
retained at block boundaries is the full-state sheet z: q itself becomes
equal for the displayed pair when theta=1. The receiver read uses raw
balanced representatives without subtracting a piston center.

The witness establishes acquisition for two ready inputs at each block
start. It supplies neither automatic re-preparation nor a permanent
record. It does not encode the full reference shell, bank, refusals,
Weyl action, or an energy account. The new correction and scheduler
therefore remain `DECLARED_EXTENSION_ONLY`; the original native P
admission remains open. No global minimality or compiler completeness
follows from the seven-scheme classification.

No analytical correction remains necessary in the reviewed proof.
Implementation correctness and finite-audit results remain separate
checks; this review does not predeclare their outcome.
