# P-RAMIFIED-TM-LIFT-1 result record

Status: two-architecture reproduction complete. The formal aarch64 leg and
the clean GitHub x86_64 leg reproduce the pinned verifier stdout byte for
byte. The proposed all-`n` theorem status is proof-first: the finite audit
does not promote a bounded prefix into an unbounded claim.

## Immutable pin

```text
pin commit       02a2f7fa6acaa30b2d972ff6c063f8a6a44ab80b
PREREG.md        85003a48f621ffbe9fb1b682e3ce5024c0bd5f416b79d4e50176980aeb6aee37
verify.py        31adb8209ddf11237319389c59c533251d01f3278ea9ff33482c58341472d39f
public lock      issue #74
```

The pin contains only `PREREG.md` and `verify.py`. It was committed and
published before the first formal execution. Neither pinned file is changed
by this result commit.

## Formal leg

```text
architecture  platform      python  result          stdout sha256
------------  ------------  ------  --------------  ----------------------------------------
aarch64       Ubuntu 24.04  3.12.3  10/10 ALL PASS  1e186b17...5db7c8
x86_64        GitHub Linux  3.12    10/10 ALL PASS  1e186b17...5db7c8
```

The exact transcript is 805 bytes and 11 lines, with empty stderr and exit
code 0. It is frozen as `EXPECTED.txt`; full command and hashes are in
`RUN.md`. The GitHub policy workflow run `29692441650`, job `88207417865`,
reports
`VERIFY PASS P-RAMIFIED-TM-LIFT-1 31adb820...72d39f 1e186b17...5db7c8`.

## Proof and audit verdict

The theorem-grade basis is the frozen seven-step derivation in `PREREG.md`:
binary-length induction gives the unique digit recursion, the sign quotient
gives Thue-Morse, clearing trailing ones gives the chronological carry
cocycle, and the inherited `CODEC-TR4` identity gives the trace realization
for every `k >= 0` and every declared seed by induction. The bitwise
place-value proof gives the exact carry coefficient `2` for all nonnegative
integers.

The pinned audit independently constructs the C4 and C2 digit recursions,
checks their large frozen prefixes, exhausts every nonzero covector and
multiplier over `F_5`, checks all 125 trace-one residue seeds through the
frozen range, and records the inversion-blind and breath guards. All ten
gates pass. No frozen falsifier fires on either architecture leg.

## Scope firewall

This result is confined to L1 arithmetic on the declared forward carrier and
the one-dimensional `Tr4` readout quotient. It does not identify the full
`M_J` state with four phases, make the chronological step a constant quarter
turn, factor through a kernel checkpoint, extend parity to all of `Z_2`, or
earn a physical carry/phase, run/record, time-arrow, or L2-L6 statement.

PR #68 and PR #71 remain unchanged and are not evidence or dependencies for
this probe. The silver/order-eight lane is an adjacent comparison only; no
equality with its carrier is asserted here. `READING-SPLIT [D]`,
`ODOMETER-INTERNALIZED [D]`, and `TIME-QUANTUM-TOWER [C]` keep their current
statuses and scopes.

## Two-architecture gate

PASS. The aarch64 and x86_64 legs use the byte-identical pinned verifier,
exit zero, write empty stderr, and reproduce the same 805-byte transcript
with SHA-256 `1e186b170457cb182368a21e2145d43d5cfc358978ee6d5f6d9eb0d5ea5db7c8`.
Policy, all 38 unit tests, Canon, and ledger checks are green in the same CI
job. Any Canon or ledger fold is a separate reviewed change.
