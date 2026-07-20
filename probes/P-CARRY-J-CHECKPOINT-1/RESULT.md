# P-CARRY-J-CHECKPOINT-1 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS;
PUBLIC CLAIM UNREGISTERED

## Recorded decision

```text
verdict: RESULT 5/5 ALL PASS
exit:    0
stderr:  empty
```

No preregistered falsifier fired on either architecture. The frozen symbolic
proof establishes the full-carrier L1 checkpoint-factorization no-go; the
finite verifier audits every one of the `5^6 = 15625` checkpoint seeds
through the universal collision at times four and six. This records a
proof-first scientific result, not a registered Canon theorem. The
`CARRY-J-CHECKPOINT` row remains `[O]` until a separate reviewed fold.

## Immutable pin and formal leg

```text
public lock:          issue 81
base commit:          3d8c6307f20d01ad50fc90ae1c5777926b884881
preregistration pin: 55f678d721a13f3168f0a5175be65b9f8101a64f
PREREG.md SHA-256:    b946d9808ced64f3ecae68fe0bea5df03a07ea1956bd850b68d5dd105c416163
verify.py SHA-256:    406004360a511512f3c3c44351f25df64df115aa6f35dbd1c0ac16f4587b20c2

platform:             Ubuntu 24.04.4 LTS
architecture:         aarch64
Python:               CPython 3.12.3
checkout:             clean, detached at the exact public pin
exit/stderr:          0 / 0 bytes
stdout SHA-256:       87584b6afc5b77a3d8b1cc7957197431227fbdd77cf447da3ea92289fa1e668a
stdout bytes/lines:   394 / 6
result:               5/5 ALL PASS
```

`EXPECTED.txt` is the exact LF-only stdout of this formal leg. `PREREG.md`
and `verify.py` remain byte-identical to the public pin.

## Independent x86_64 reproduction

```text
pull request:          86
formal evidence head: c3293bd5173e291093eb03ec464b4641608e574e
tested merge commit:  ac3f53f00ec740ae4d743b106da5f8bdd4cbda2c
workflow run:          29724695901
workflow job:          88294996747
conclusion:            success
platform:              GitHub-hosted Ubuntu 24.04 x86_64
runner image:          ubuntu-24.04 20260714.240.1, runner 2.335.1
Python:                CPython 3.12.13
verifier SHA-256:      406004360a511512f3c3c44351f25df64df115aa6f35dbd1c0ac16f4587b20c2
stdout SHA-256:        87584b6afc5b77a3d8b1cc7957197431227fbdd77cf447da3ea92289fa1e668a
byte identity:         PASS, 394 bytes and 6 lines
gate:                  PASS
```

The required policy workflow checked out GitHub's generated merge of the
exact formal evidence head into the declared base commit. It enforced
verifier integrity, x86_64 architecture, exit zero, empty stderr, and
byte-identical `EXPECTED.txt`, and logged
`VERIFY PASS P-CARRY-J-CHECKPOINT-1` with both frozen hashes. Together with
the formal aarch64 record, this completes the two-architecture computation
gate. `RUN.md` remains the neutral aarch64 record; this close-gate update
changes only `RESULT.md`.

## Proof and audit verdict

For an arbitrary initial checkpoint, the five frozen trace laws force
`z_3 = 1`. The selectors at steps three, four, and five are then all `1`, so
the same involution `b` acts three times. Since `b^2 = id`, this gives
`psi_4 = psi_6` for every initial checkpoint. But the inherited ramified
phase has `Theta_4 = 2` and `Theta_6 = 4`. A single-valued map from the
checkpoint alone to that phase would therefore assign two distinct values to
the same argument. Such a map does not exist on the frozen full forward
carrier.

The audit independently checks all five generator involutions and trace laws,
the forced trace skeleton, every seed collision, the phase separation, and
the resulting factorization obstruction. All five gates pass. The proof, not
the finite census, carries the universal conclusion.

## Scope firewall

The earned statement is confined to L1 arithmetic, the declared Public Canon
v11 update, and the full forward carrier beginning at clock coordinate zero
with arbitrary checkpoint in `F_5^6`. It rules out only a checkpoint-only
factorization of the inherited `RAMIFIED-TM-LIFT` phase on that carrier.

It does not decide any separately defined restricted carrier, identify the
ramified phase with the full autonomous state, derive the selector offset,
add a physical carry, phase, time, or gravity reading, extend parity to all
of `Z_2`, establish decoder completeness, or lift any claim to L2-L6.
`RAMIFIED-TM-LIFT [T]`, `READING-SPLIT [D]`, and all other registry rows keep
their existing scopes and statuses.

## Two-architecture gate

PASS. The aarch64 and x86_64 legs use the byte-identical pinned verifier,
exit zero, write empty stderr, and reproduce the same 394-byte transcript
with SHA-256
`87584b6afc5b77a3d8b1cc7957197431227fbdd77cf447da3ea92289fa1e668a`.
Policy, all 44 unit tests, Canon, and ledger checks are green in the same CI
job. Any Canon or ledger fold is a separate reviewed change.
