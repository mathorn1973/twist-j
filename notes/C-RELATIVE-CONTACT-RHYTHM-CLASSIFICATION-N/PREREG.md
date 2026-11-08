# Publication and replay contract

**NON-CANONICAL / L1 / no authority.**
Candidate `C-RELATIVE-CONTACT-RHYTHM-CLASSIFICATION-N`; issue #1854.
Owner: A. M. Thorn / Codex-rhythm-publication-20261102.

This is a prospective freeze of the **publication replay**, not a claim
that the already discovered results were publicly preregistered. The source
proofs, code, expected outputs and conclusions were exposed before this
contract. This is not a formal public probe. No sealed probe is resumed.
The source and new public publication pins have different roles.

## 1. Equation and carrier

`O=Z[X]/(Phi5)`, coefficient basis `(1,j,j^2,j^3)`, `rho=j^2`.
States are complete labelled triples in `O^3`. If `x-y` is coefficientwise
even, `C(x,y)=(s+rho*t,s-rho*t)` with `s=(x+y)/2`, `t=(x-y)/2`;
otherwise `C(x,y)=(x,y)`. `F=C23 C12`. Equality is literal coefficient
equality. `Q=(5*sum z_i^2-(sum z_i)^2)/2`, `E=sum Q`, `S=sum z_i`,
`M=3E-Q(S)`. No floating point or empirical input.

## 2. Claims and failure thresholds

The fixed analytical targets are the first-return/rejection identities,
no-common-parity lemma with sharp eight-tick bound, complete three-family
classification, sharp minimum accounts, `3P<=2M-5` off the diagonal,
five deepest phases of the third family, hidden-phase counterexamples,
and the sufficient injectivity condition `3m^2>M`.
A valid counterexample or failed proof premise defeats the affected claim;
finite agreement is not the proof of an unbounded statement.

Known finite targets, not blind predictions:

- Descent agrees with completely enumerated trajectories from 1,347 test
  preparations, totaling 23,359 state visits (not asserted disjoint),
  including primitive and doubled families. The inherited stdout calls
  these `fully_enumerated_orbits` and `fully_enumerated_states`.
- All 2,895 states of `E=32,S=4`: 2,218 fixed orbits, 72 of length 5,
  26 of length 9, two of length 21 and one of length 41.
- Three concentration marks, one on each marked orbit; 2,812 states
  forever unmarked; 63 infinite marker classes; least separating prefix
  length 42 with samples numbered from zero.
- All coefficient moduli 2 through 8 and powers `2^k`, `k=0..4`, as frozen
  in the expected shell output. The smallest injective integer modulus
  is 5; the smallest power of two is 8.
- Explicit `(4,0,2)` and `X,Y` phase witnesses and sharp families at
  `d=0..5`, retaining all 51 assertions in the phase audit.
- Every enumerated shell state agrees with the separate descent classifier
  on least period, refusals, maximum depth and primitive family counts.

Zero mismatches are admitted. A nonzero exit, nonempty stderr, changed
stdout/data digest, missing file or timeout is a failed replay, never PASS.
Record it without changing a scientific threshold or deleting a witness.
A packaging defect may receive an explicit additive correction and a new
publication pin; it does not establish or refute a mathematical theorem.

## 3. Code and data

Freeze `verify.py`, `verify_classification.py`, `verify_shell.py`,
`verify_phase.py`, their expected stdout and digest contracts before the
first replay in this publication session. Exact names and custody are in
`SHA256SUMS`. `SOURCES.md` maps the prior code to this public package.
The adapted scripts retain the original arithmetic and input families;
the aggregate runner is an exposed audit, not a new independent derivation.
The prior scientific outputs are comparison fixtures, not fresh run records.

## 4. Systematics

- Keep complete state equality and exact least return, including fixed
  non-diagonal states and the separate complete diagonal.
- Count refusals after the preceding contact; admitted identities do not
  increment the refusal count.
- Take maximum common depth over the complete orbit, not at the starting
  phase. Treat `v2(0)=infinity` explicitly.
- The shell enumeration has a proved coefficient bound and a computed third
  slot `c=4-a-b`; no search cap may stand for exhaustion.
- Compare coefficient residues modulo 5 separately from residues modulo
  `(1-j)`. Keep marker histories distinct from full-state histories.
- Keep a 42-sample identification task distinct from waiting for two marks.
- The scripts use alternative algebraic expressions, but are exposed and
  coordinated in one session. No blind or independent-author designation.

## 5. Environment and replay

Python 3.12, standard library, exact integers. The aggregate runner applies
the repository's deterministic locale, timezone, hash seed and bytecode
settings. Each subprocess uses the unchanged 600-second audit allowance.
The runner compares exit status, empty stderr, exact stdout and generated
data digests in temporary directories. It must leave the checkout clean.
Record the actual architecture and bytes in `RUN.md` after execution.

This note does not invoke a formal probe runner. Existing repository
policy/Canon/ledger/gate and changed-path checks run unchanged. Notes are
outside the changed-probe and changed-reproduction selection; green CI
therefore is not a scientific second architecture for these programs.

## 6. Action layer and exclusions

All claims are L1 statements about the supplied arithmetic dynamics and
explicit mathematical observations. No L1-to-L6 lift, native-U realization,
physical clock or energy identification, occurrence law, complete instrument,
resource renewal or canonical promotion is asserted. Changes are confined
to this one notes directory, with no policy or workflow modification.
