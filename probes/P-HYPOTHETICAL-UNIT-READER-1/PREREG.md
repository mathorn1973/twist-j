# Preregistration: P-HYPOTHETICAL-UNIT-READER-1

PUBLIC, NON-CANONICAL. Owner: A. M. Thorn, assistant session 2026-10-09.
Reservation: [#1431](https://github.com/mathorn1973/twist-j/issues/1431).
Action layer: L1.
Physical status: working hypothesis H.
Conditional mathematical target: candidate-T; finite checks are audits.

## 1. Question and equations

Does the complete law in MODEL.md support two genuine consecutive writes
into the same occupied receiver, fixed present-context reading of the last
transfer, full-state reversibility and an independently posed additive
energy-profile criterion?

The local operation transfers one actual stock unit in the stored direction
when available, otherwise reflects that direction. The pointer changes by
the actual receiver difference. XOR zero-flag changes preserve all initial
flag errors. The internal phase always toggles; conserved switches can
disable either contact. The model is supplied as a new law, not derived
from U/J. All branch formulas, inverse, carrier and hypotheses are frozen
in MODEL.md.

## 2. Carrier and declared reading family

The ordered state is
(r1,r2,y,d1,d2,e1,e2,z,p,tau,chi1,chi2):
three nonnegative integer stocks, two signs, three independent raw bits,
a pointer in Z5, a phase bit and two independent enable bits.

The sole admitted observation is the present finite hardware
h=(d1,d2,e1,e2,z,p,tau,chi1,chi2).
The declared last-transfer reader has codomain {-1,0,1} with exact integer
equality and requires calibrated flags. Its context keys are retained
directions, phase, switches and flags, without past-state or external-time
inputs. Pointer readings have equality modulo five; when N<=4 and p-y=0
modulo five, the representative is the exact integer stock. Overlaps with
hidden directions are tested by the fixed 10/01 counterexample.

No arbitrary decoder family, universal physical occurrence rule or
uniqueness among all conserved state functions is tested. The energy
classification fixes f(r1)+f(r2)+f(y)+A(h), common f with f(0)=0 and arbitrary
finite-hardware A, excluding stock-dependent interaction energies.

## 3. Code and immutable inputs

Runtime sources are model.py, primary.py, independent.py and verify.py.
All are Python standard-library source. No external data, random seed,
network request, numerical library, private input or clock observation
enters the science.

primary.py loads only the exact sibling model.py and uses direct branch
formulas. The separately authored independent.py has no sibling imports
and uses the cyclic coordinate u -> u +/- 1 at fixed pair total.

INPUTS.sha256 freezes exactly README.md, MODEL.md, PREREG.md, REVIEW.md,
model.py, primary.py and independent.py. The wrapper contains the exact
SHA-256 of that manifest and validates every named input before and after
execution. verify.py itself is bound by the public commit and its SHA-256
in RUN.md; it is excluded from the manifest to avoid a self-hash cycle.

Accepted command from the repository root:

~~~sh
python3 probes/P-HYPOTHETICAL-UNIT-READER-1/verify.py
~~~

The wrapper executes both complete programs with the same Python in
isolated mode and bytecode disabled, requires exit zero, empty stderr and
byte-identical stdout, and emits that common stdout exactly. On failure, stderr preserves every
attempted child, its exit/timeout disposition and exact stdout/stderr as hex,
including partial timeout output and both sides of a comparison failure.
Each child
has a 55-second limit. Infrastructure timeout or nonzero exit produces no
successful scientific record and is never repaired by changing this pin.

## 4. Frozen finite domain and output

Enumerate N=0,...,8; then r1=0,...,N; r2=0,...,N-r1; y=N-r1-r2.
For each triple, enumerate directions by the Cartesian product of (-1,1),
then raw flags by the product of (0,1), pointer 0,...,4, phase 0,1 and
switches by the product of (0,1), in that order.

This is the complete closed finite domain of 211200 raw states.
Exactly 26400 have all three correct flags. This count includes all five
pointer offsets; it does not assert absolute pointer calibration.

For each input s and complete successor t, append the 24 integers in s+t,
joined by one ASCII space and terminated by one LF, to a SHA-256 stream.
The report is sorted-key JSON with indentation two and a final LF.

Checks over the entire domain are both inverse identities, nonnegative
stocks, N conservation, pointer-offset conservation, three flag-error
invariants, unchanged switches, inactive-source locality, phase toggle,
disabled-branch identity, unit-bounded actual increment and calibrated
last-transfer reading.

The report also derives and checks these fixed witnesses:

- All twelve independent (a,b,t) preparations with a,b in {0,1} and
  t in {0,1,2}, directions ++, phase zero, switches 11, correct flags
  and p=t. Two actual steps give y1=t+a and y2=t+a+b, with p2=y2.
- Context: t=1, source inputs 10 and 01. After two steps stocks are
  (0,0,2), p=2 and the remaining nondirectional hardware agrees, while
  directions are (+,-) and (-,+), and last increments are 0 and 1.
- Fault: initial (0,0,1,1,1,0,1,0,1,0,1,1), true delta zero, read minus one,
  preserved error vector (1,0,0).
- Equal-shell energy pair: complete correctly flagged preparations
  (3,2,1) and (2,3,1) with common hardware (++/000/p1/tau0/11).
  Outputs are (2,2,2) and (1,3,2); input stock energy is 4+2c for both.
  Defect coefficients (constant, coefficient of c) are (2,-2) and (0,0).
- Default full cycle: (2,1,1,1,1,0,0,0,1,0,1,1), twelve successive steps.
  All thirteen full boundary states are output; the first twelve are
  distinct and boundary twelve equals boundary zero.
  Actual increments: 1,1,1,0,0,-1,-1,-1,-1,0,0,1.
- Disconnection: six pairs, b in {0,1}, t in {0,1,2}, first source zero
  versus three, chi=(0,1), other supported preparation as above.
  At boundaries zero through twelve, compare precisely
  (y,d2,e2,z,p,tau,chi1,chi2), for 78 comparisons. Completed activations
  of the disabled contact have last-transfer read zero.

The complete report schema is fixed in both sources: probe, cutoff,
states, calibrated_states, transition_sha256, two_write_preparations,
context, fault, energy_defects, cycle, disconnected_pairs and
disconnected_observations. No unregistered parameter scan or fitted
coefficient is admitted.

## 5. Systematics and failure thresholds

There is no statistical error bar: all executable comparisons are exact
integers, tuples and bytes. Any single violated equality is a falsifier.

| ID | Frozen failure condition |
|---|---|
| F1 | A complete forward/inverse identity or carrier condition fails. |
| F2 | N, pointer offset, a flag error, switch constancy or inactive locality fails. |
| F3 | A correctly flagged last-transfer read differs from the actual increment. |
| F4 | One of the twelve actual two-write preparations fails its stated outcomes. |
| F5 | The context or deliberately faulty-flag witness does not have its stated outcome. |
| F6 | Equal-shell energy inputs/outputs, hardware matching or exact defects differ. |
| F7 | The declared full return or a disconnection comparison fails. |
| F8 | Independently expressed complete audits disagree on any stdout byte. |
| F9 | A mathematical counterexample invalidates a universal proof at its stated scope. |

Expected negative controls in F5 are successful evidence when they exhibit
the declared ambiguity/fault; they are not hidden failures of a stronger
uncalibrated-reading claim. There is no such stronger claim.

Source/manifest mismatch, timeout, nonzero exit or stderr is an execution
gate failure, not a scientific success. The original frozen source and
failure disposition must be preserved under POLICY.md. No threshold,
range, branch or claim will move after the pin.

The finite audit cannot establish the infinite-domain energy or reader
theorems. Their support is the full proofs in MODEL.md and the separately
disclosed mathematical review. Shared specification and known target
values limit independence; separately authored code is not experimental
independence or result blindness.

## 6. Public custody, authority and result handling

Before the first scientific execution, the entire package is committed,
pushed and read back byte for byte from its public pin. No scientific
source, CLI demonstration or finite enumeration has been run before that
pin. Prior work consists of derivation, source review, AST parsing and
byte/hash checks.

The authority is public main c164b79ce134152ac7cd600421791df74113f29f,
Public Canon v100, tag canon-v100 and declared content ancestor
a4cc9666662967527abe711441833ff600c00337.
CANON.md has 980212 bytes and SHA-256
5e4de2da8d57ff2f7e4b873e6236b0695677e20d173d894ee70562c1389648c4.
All five normative hashes, ancestry and successful required authority
checks were verified. Collision scans covered 224 actual remote heads,
public paths, registry/frontier and issue/PR searches before claim #1431.

After a completed first run, EXPECTED.txt is its exact common stdout.
RUN.md records the immutable pin, verifier hash, exact command, neutral
platform/architecture/Python, timing, exit code and stdout/stderr bytes and
hashes. RESULT.md records scope, fired falsifiers and conclusions.
Required repository checks and both existing architecture jobs must then
pass. A positive audit does not promote the physical hypothesis.

No Canon, registry, gate, policy, workflow or prior probe changes belong
to this work. The pull request remains reviewable; merge and Canon
promotion are separate actions.
