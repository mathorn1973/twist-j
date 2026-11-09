# Renewed external review: requests resolved

NON-CANONICAL / L1. Date: 2026-11-09. Renewed disposition:
**Accepted within the declared mathematical assumptions; conditional,
text-level candidate-T.** Requests R1 and R2 are resolved and nonblocking.
This is manual mathematical review, not formal certification or Canon promotion.

This is a coordinator-written English record of the external AI-assisted
review reported through A. M. Thorn. It records Emmy's renewed assessment and
her subsequent clarification as relayed by Thorn. It is not a byte copy of an
original Emmy report; the coordinator did not inspect a separate full report.
The scope and method below delimit the acceptance actually reported.

## Reviewed sources and method

The renewed review read both complete texts:

- The [frozen PROOF.md at 015c6b6f](https://github.com/mathorn1973/twist-j/blob/015c6b6f68cb8e005f0833f8a1f6f71b051215a1/probes/P-J-SIGN-REMOTE-HOLD-1/PROOF.md).
- The full 220-line [PROOF-ADDENDUM.md at 5d146064](https://github.com/mathorn1973/twist-j/blob/5d1460645f44c200047909127a78e7a429c562ec/notes/C-SIGN-TRANSPORT-RECORD-CONSOLIDATION-N/PROOF-ADDENDUM.md).

The method was manual algebra and textual checking. The renewed review used
no code execution, numerical test or formal proof checker, and did not
recompute source hashes. Emmy was not a coauthor of this construction. Her
role, if any, in the predecessor work in PRs #1970 and #1971 is not
established by this record. This external review is separate from same-session author-side
checking and from the two-architecture finite computational audit.

The reported acceptance covers composition of the declared funded primitive,
common-preparation sign encoder, complete data and clock return tables,
whole-data-rail alias, clock-qualified remote reader and prescribed hold,
including the intermediate-layer windows and complete resource account.
It applies under the supplied carrier, geometry, schedule, initial stock,
clock preparation and reader definitions. It does not derive those premises.

## Resolution of the two presentation requests

| Request from the first review | Renewed disposition |
|---|---|
| R1: explicit coefficient conjugation and exact guard evaluation | RESOLVED; nonblocking |
| R2: explicit per-cell, per-gate and stepwise H/E accounting | RESOLVED; nonblocking |

For R1, the addendum supplies the coefficient conjugation and multiplication
rules, h and half-trace formulas, and exact parity and balance comparisons.
For R2, it expands the nonzero-center cross terms, both funded branches,
individual cell transfers, all first-three-tick layer boundaries, and the
source/data/clock subtotals. Its general per-gate argument covers arbitrary
occupied states and all subsequent layers, not just prepared endpoints.
The reviewer accepted these expansions as resolving both requests while
retaining the conditional, text-level candidate-T scope.

## Withdrawn conveyor-shift finding

During the renewed review a conveyor-shift concern was raised. Emmy
subsequently explicitly withdrew it through Thorn: she had misread the
existing even/odd statement in
[frozen PROOF.md, lines 136-138](https://github.com/mathorn1973/twist-j/blob/015c6b6f68cb8e005f0833f8a1f6f71b051215a1/probes/P-J-SIGN-REMOTE-HOLD-1/PROOF.md#L136).
For an occupation set M on the canonical rail code, the full conveyor sends

    M -> (M_even + 2) union (M_odd - 2), modulo m.

Thus M={0,1} gives {2,m-1}, exactly as the frozen parity-split rule states.
The reviewer confirmed the text. This finding is closed as a reviewer
misreading, not a source defect or a remaining warning. No scientific source
change was requested or made on its account.

## Review history and source custody

On 2026-11-09 the
[first external review and author response](https://github.com/mathorn1973/twist-j/blob/d8f831dc2487985c4794b594b6a674c060fb6d1b/notes/C-SIGN-TRANSPORT-RECORD-CONSOLIDATION-N/REVIEW.md)
recorded a conditional, text-level-consistent verdict with R1 and R2 still
retained. That earlier disposition is preserved; it is not retroactively
rewritten as acceptance. The original
[same-session analytical review](https://github.com/mathorn1973/twist-j/blob/33a393e3af8344b31c1e6bedc8e5638be6aa8b26/notes/C-SIGN-TRANSPORT-RECORD-CONSOLIDATION-N/REVIEW.md)
also remains available. An auxiliary numerical attempt in the first external
review produced no usable result and supplies no evidence.

Later on 2026-11-09, after the full addendum was published and reviewed
alongside the full frozen proof, the renewed review resolved R1 and R2.
The subsequent explicit withdrawal closed the separate shift concern as
recorded above. These are distinct review stages.

The coordinator's public readback of the addendum completed at
2026-11-09T08:17:14Z. The reviewed addendum is 10,567 bytes, SHA-256
`2e32f6e6f40b43e88a266f1ad59b6c0af265bf79e399f08c50b24cf49683cd1f`.
The frozen proof is 24,103 bytes, SHA-256
`d7ffeaf4b9e2a9f528fcaaecfc945cd9f7eea30ac8f868734dbf406f9f5a0f39`.
These are coordinator custody records, not hashes independently attested by
the reviewer. PREREG.md, PROOF.md and verify.py remain unchanged at the
frozen source pin; EXPECTED.txt retains the original first-run bytes.

## Acceptance boundary

The renewed review accepts the stated composition under its declared
mathematical assumptions at the manual text-review level. It does not claim
machine-checked formalization, an independent numerical reproduction,
empirical physics, or promotion to Canon. The supplied architecture and
reader remain candidate-D, the all-parameter claims candidate-T, and the
finite executed inventory candidate-C. The record is occupied-region delay
memory with a counted phase reference; it is not a stationary point latch.
No broader law, physical detector, gravity result or fresh-message renewal
is established by this acceptance.
