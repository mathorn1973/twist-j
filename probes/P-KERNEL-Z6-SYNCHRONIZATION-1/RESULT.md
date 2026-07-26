# P-KERNEL-Z6-SYNCHRONIZATION-1 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS;
PUBLIC CANON UNCHANGED

The immutable preregistration pin
`c23ea20f9a4903acd4ca341ec857b29a635ae7ca` was executed exactly once on
native Linux/aarch64 after public remote readback. The verifier exited zero,
wrote no stderr, and produced the exact 1000-byte output recorded in
`EXPECTED.txt` with SHA-256
`b86fd3889abb668ebc235e045aeed928e791cd02ca14e4b92910b81c65959077`.
Every frozen integrity, universal-proof, finite-audit, route-agreement, and
transcript condition passed. No counterexample or diagnostic was emitted.

The first clean GitHub Linux/x86_64 replay used the identical pinned verifier
at tested merge commit
`d19129e9639aa7acd5d5a33bedc8c1b0b802b90e`. Workflow run `30200967000`,
job `89790713980`, exited zero with empty stderr and reproduced
`EXPECTED.txt` byte for byte. The two-architecture computation gate is PASS.

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
x86_64 workflow run:  30200967000
x86_64 workflow job:  89790713980
x86_64 tested merge:  d19129e9639aa7acd5d5a33bedc8c1b0b802b90e
x86_64 platform:      Ubuntu 24.04.4 LTS
x86_64 runner image:  ubuntu-24.04 20260720.247.2
x86_64 runner:        2.336.0
x86_64 Python:        CPython 3.12.13
x86_64 exit/stderr:   0 / 0 bytes
x86_64 byte identity: PASS
stdout SHA-256:       b86fd3889abb668ebc235e045aeed928e791cd02ca14e4b92910b81c65959077
stdout bytes/lines:   1000 / 21
stdout CR/NUL/final:  0 / 0 / 0a

architecture gate:    PASS
```

The exact neutral metadata and raw stdout are public in issue #160 comment
`5083313218`. The first x86_64 replay return is public in issue #160 comment
`5083352628`. `EXPECTED.txt` is byte-identical on both architectures. The
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

The sole formal aarch64 leg passed. The first clean GitHub Linux/x86_64
pull-request replay of the identical pinned verifier also passed at tested
merge commit `d19129e9639aa7acd5d5a33bedc8c1b0b802b90e`: exit zero, empty
stderr, and byte-for-byte reproduction of `EXPECTED.txt`. The
two-architecture computation gate is therefore PASS. The final-head policy
workflow remains the merge-eligibility check for this evidence update.
