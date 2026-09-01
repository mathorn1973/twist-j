# P-JIPC-WP3D-QPOS-MELLIN-1 result

Status: **candidate-T / L1 / ARCHITECTURE-GATE-PENDING / PUBLIC CANON STATUS UNCHANGED.**

Here `candidate-T` names the provisional theorem ceiling carried by the
written proof; it does not select the frozen `CONFIRMED` decision while the
architecture gate is pending.

The first and only local formal execution of the immutable public verifier
exited zero, wrote empty stderr, and produced the exact 365-byte committed
`EXPECTED.txt`. All four scientific audit gates passed, all PASS-candidate
integrity gates passed, and all 23 named negative mutations were rejected at
their guards. No
frozen scientific falsifier fired and no threshold moved.

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

The public readback and FZ7 receipt is recorded on claim-lock issue #777. The
required GitHub Python 3.12 x86_64 and aarch64 replays and aggregate `check`
have not yet run on the formal-evidence head, so `CONFIRMED` is not selected
by this pre-architecture record.

## Provisional decision

```text
CONFIRMED          PENDING — ARCHITECTURE GATE
SCIENTIFIC-FIRED   NOT SELECTED
BOUNDED-AUDIT-C    NOT SELECTED
STOP               NOT SELECTED
ABANDONED          NOT SELECTED
```

The theorem-grade carrier is the self-contained written proof Q1-Q8 in
`PREREG.md`; the finite verifier is an exact audit, not a sampled replacement
for the universal arguments. The bounded fallback is therefore not selected
at this stage, but final `CONFIRMED` remains conditional on the frozen
two-architecture byte-identity gate and manual security review.

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
`sitecustomize.py` or `usercustomize.py` shadow file. The pending GitHub jobs
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
