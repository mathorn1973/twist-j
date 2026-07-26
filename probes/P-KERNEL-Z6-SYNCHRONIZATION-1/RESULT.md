# P-KERNEL-Z6-SYNCHRONIZATION-1 result

Status: FORMAL AARCH64 PROOF-SURVIVES; X86_64 PENDING;
PUBLIC CANON UNCHANGED

The immutable preregistration pin
`c23ea20f9a4903acd4ca341ec857b29a635ae7ca` was executed exactly once on
native Linux/aarch64 after public remote readback. The verifier exited zero,
wrote no stderr, and produced the exact 1000-byte output recorded in
`EXPECTED.txt` with SHA-256
`b86fd3889abb668ebc235e045aeed928e791cd02ca14e4b92910b81c65959077`.
Every frozen integrity, universal-proof, finite-audit, route-agreement, and
transcript condition passed. No counterexample or diagnostic was emitted.

## Recorded decision

```text
run integrity:       PASS
counterexample:      NONE
diagnostic:          NONE
scientific decision: PROOF-SURVIVES
route:               PROOF-SURVIVES
```

## Exact certificate

The complete finite carrier audit covered all `15625` states of `F_5^6`,
all five sheets of size `3125`, and both coordinate and affine realizations
of the five generators. The two independent evolution routes agreed on every
complete trajectory through the frozen direct audit surface.

The symbolic proof audit and its exact controls support precisely the four
preregistered L1 statements:

1. For every fixed known `n >= 3`, each initial sheet maps bijectively onto
   `X_(q_n)`, so `E_n:X->X_(q_n)` is exactly five-to-one.
2. For every fixed known `n >= 1`, the two restrictions from `X_1` and
   `X_4` are separate bijections onto `X_(q_n)`, so the restriction from
   `X_14` is exactly two-to-one.
3. For every `psi_0 in X`, neither the checkpoint trace nor the complete
   checkpoint trajectory is eventually periodic.
4. No such complete trajectory has a realization by a finite autonomous
   time-homogeneous state system.

The fixed-time qualifications are part of the result. No unknown-time or
unindexed checkpoint-fiber statement is made.

## Immutable pin and formal evidence

```text
public lock:           issue 160
base commit:           4ac41b4fac3a3794a6e9d5be1e2027d324edb806
pin commit:            c23ea20f9a4903acd4ca341ec857b29a635ae7ca
PREREG.md SHA-256:     e783a3a16891804f0c97b5b80744b0bb4ec5dcee1f8b2ae4f479283e2b48703a
verify.py SHA-256:     a9c696dfa59562d29f3422ebe30979678c053d307229b7deecb8beb64b7c2e02

aarch64 platform:     Linux, native
aarch64 Python:       Python 3.12.3
aarch64 checkout:     fresh, clean, detached at the exact public pin
aarch64 executions:   1
aarch64 exit/stderr:  0 / 0 bytes
stdout SHA-256:       b86fd3889abb668ebc235e045aeed928e791cd02ca14e4b92910b81c65959077
stdout bytes/lines:   1000 / 21
stdout CR/NUL/final:  0 / 0 / 0a

architecture gate:    GitHub Linux/x86_64 reproduction pending
```

The exact neutral metadata and raw stdout are public in issue #160 comment
`5083313218`. `EXPECTED.txt` is byte-identical to that raw stdout. The
immutable `PREREG.md` and `verify.py` remain unchanged.

## Scope firewall

This result is `PROOF-SURVIVES` only for the frozen L1 proof audit. It does
not make `F_5^6` the complete autonomous state, select a counter or genesis
history, add a decoded log as state, derive physical irreversibility, prove a
decoder total or canonical, classify gauge or metrology, or lift any statement
to L2 through L6.

It does not promote `KERNEL-Z6-SYNCHRONIZATION [O]`. Any status change is a
later, separate reviewed Canon fold. No Canon, registry, frontier, dependency,
gate, status, workflow, or release file is changed by this evidence record.

Public lock: https://github.com/mathorn1973/twist-j/issues/160

## Architecture gate

The sole formal aarch64 leg passed. Merge remains forbidden until the first
clean GitHub Linux/x86_64 pull-request replay executes the identical pinned
verifier with exit zero, empty stderr, and byte-for-byte reproduction of
`EXPECTED.txt`.
