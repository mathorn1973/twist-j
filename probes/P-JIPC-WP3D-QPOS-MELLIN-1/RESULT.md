# P-JIPC-WP3D-QPOS-MELLIN-1 result

Status: **candidate-T / L1 / JIPC-WP3D-QPOS-MELLIN-CONFIRMED / PUBLIC CANON STATUS UNCHANGED.**

The frozen `CONFIRMED` decision is now selected at candidate-T / L1. This is
not an active public `[T]` row: any Canon or Registry treatment remains a
separately claimed and sealed fold.

The first and only local formal execution of the immutable public verifier
exited zero, wrote empty stderr, and produced the exact 365-byte committed
`EXPECTED.txt`. All four scientific audit gates passed, all PASS-candidate
integrity gates passed, and all 23 named negative mutations were rejected at
their guards. No frozen scientific falsifier fired and no threshold moved.

## Local formal result

```text
pin commit:       0c6b35731953398374fcb5072787d2a7b93c383a
verifier SHA-256: 238e587f1343e7fef07505e9bd6c8f75c9edf6a1efdeb98989f35ee5285151c0
stdout SHA-256:   f0a46170e5a8958fb953ab782a00353720ae7178fdc461dd8a189ca06683f554
stdout:           365 bytes, 10 lines, final LF
stderr:           empty
exit:             0
last line:        RESULT PASS
theorem carrier:  WRITTEN_PROOF_NOT_FINITE_AUDIT
```

The public readback and FZ7 receipt is recorded on claim-lock issue #777.

## First workflow disposition

The first public workflow attempt, run `33562354298`, passed policy, unit,
Canon, Ledger and gate-contract checks on both architectures but stopped in
`check_verifier.py` before either verifier replay because the initial
`RUN.md` command field contained the deterministic environment wrapper instead
of the required portable spelling. The aggregate check consequently failed.
The additive metadata correction is recorded in `RUN.md`; no verifier was
rerun and no pinned or stdout byte changed. This pre-replay schema stop is
preserved as provenance, not relabelled as a scientific result.

## GitHub two-architecture close gate

```text
pull request:         778
tested head:          d577c91747bb9d9b78b83ac679ee96f417a3b9ac
checked merge:        f8e61513c2c96a173c468e0bea8145a07eb39e9d
workflow run:         33562924835, SUCCESS

x86_64 job:           100039411536, SUCCESS
aarch64 job:          100039411248, SUCCESS
aggregate job:        100039502905, SUCCESS
aggregate result:     TWO-ARCHITECTURE CHECK PASS
publication:          SKIPPED (correct for a pull request)

workflow Python:      3.12.14
verifier SHA-256:     238e587f1343e7fef07505e9bd6c8f75c9edf6a1efdeb98989f35ee5285151c0
stdout SHA-256:       f0a46170e5a8958fb953ab782a00353720ae7178fdc461dd8a189ca06683f554
stdout bytes/lines:   365 / 10
exit/stderr:          0 / empty on both verifier legs
byte identity:        PASS on x86_64 and aarch64
```

Both architecture jobs also passed repository policy, all 148 tool unit
tests, Public Canon v74 with 352 claims, the public Ledger and the gate-contract
check. Each emitted the exact `VERIFY PASS` line with the frozen verifier and
stdout hashes. Aggregate `check` passed.

`RUN.md` remains the neutral historical record of the sole local formal leg
and its pre-close architecture state; this `RESULT.md` is the close-gate
record for the public workflow receipts and frozen decision.

Manual named-file security and theorem-scope review passed: the five-file
probe tree is confined to one probe directory; the pinned files and
`EXPECTED.txt` retain their public blobs; the verifier has its one frozen
`Fraction as Fr` import, exact arithmetic, no forbidden dynamic or external
I/O, and all 23 controls remain wired to their named guards. This close-gate
update changes only `RESULT.md`; the unchanged verifier and `EXPECTED.txt`
must pass the complete pull-request workflow again on this update.

## Frozen decision

```text
CONFIRMED          SELECTED
SCIENTIFIC-FIRED   NOT SELECTED
BOUNDED-AUDIT-C    NOT SELECTED
STOP               NOT SELECTED
ABANDONED          NOT SELECTED
```

The theorem-grade carrier is the self-contained written proof Q1-Q8 in
`PREREG.md`; the finite verifier is an exact audit, not a sampled replacement
for the universal arguments. The frozen two-architecture byte-identity gate
and manual security review are complete, so the bounded fallback is not
selected.

## Candidate mathematical scope

At L1 and only on the positive rational slice, the written carrier proves:

1. existence, finiteness and positivity of the bare seeds `C`, `B`, `E`, `O`
   with the frozen output-form tail-modulus algorithms;
2. `C(1)=1`, recurrence, the B-split/parts/recurrence/symmetry identities,
   `E(s)=(1/2)C(s/2)`, and the proved join `O(s)=E(s+1)`;
3. the Mellin product identity on `Q_{>0}^2`;
4. the square-cut beta identity and square-root-free duplication;
5. the public self-contained bridge `C(1/2)^2=p_I` and the public Machin
   bridge `p_I=p_M`;
6. the quadratic-to-linear representation
   `Chat(s)=2 int_0^inf e^(-2 p_M x) x^(s-1) dx`, the dressed
   rational-slice identity `Ehat(s) Ohat(s)=Chat(s)`, and its frozen `s=1`
   anchors, all typed to `p_M`.

The exact bounded audit independently replayed the frozen ring lattice,
four-pair bare-`C` modulus sample, Machin witnesses, eight exponent-form
identities, three scale residual guards and 23 proof controls.

## Runtime trust boundary

The verifier is zero-input and its sole import is
`fractions.Fraction`. The formal process received only the frozen environment
variables recorded in `RUN.md`; a separate preflight checked clean Python
startup. Interpreter, standard-library and operating-system behavior remain
trusted. The public-pin checkout contained no `fractions.py`,
`sitecustomize.py` or `usercustomize.py` shadow file. The completed GitHub jobs
are independent replays, not operating-system sandbox proofs.

## Scope firewall

This result does not identify `p_M` with a circle, Gaussian, Gamma, SI,
physical or library constant. It proves no identity beyond the rational
slice, no effective holomorphic seed, meromorphic continuation, functional
equation, Fourier or Poisson statement, archimedean place, WP2 obligation or
L2-L6 lift. It changes no Canon, Registry, Frontier, dependency, gate,
workflow, release or existing-probe byte. Any public `[T]` row is a separately
claimed later Canon fold.

```text
FORMAL_VERIFICATION = NOT_CLAIMED
PROTOCOL_VERDICT    = NO_VERDICT
SAMPLING            = NOT PROVIDED
```
