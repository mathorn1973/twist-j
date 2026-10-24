# Custody, review and checks

PUBLIC / NON-CANONICAL / L1. Author: A. M. Thorn.
SPDX-License-Identifier: Apache-2.0.

## Correctly attributed local Git history

- Basis: dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d, Public Canon v103.
- Preregistration: 81b10ebb36a7b80482d500ce96e9e51c92a1ec55.
- Initial authored proof and audit source:
  e690cda29eda557ddde8b3f7f486a42cd15858e4.
- Author's result and promotion boundary:
  8787b25550631a26954055b15c1ca7da5d7ba29a.
- Reviewer ATTACK, before proof/code exposure:
  f398cbe9e72b9dae2744feaeff0832100a30bd00.
- Reviewer DERIVATION, before proof/code exposure:
  e3e7a58c8b98ce3982886aec93b2bd0348302923.
- Clarification responding to the review:
  e2135244e0995135ad399567120f9e279beec24b. This changes only the explanation
  of the zero-energy convention: the literal phase reading fixes it, while
  the massless speed fixes A/B. It changes no equation or audit threshold.
- Final independent review branch:
  c196a88ba093b89d4fc052a02c6e3dc3a7366a42.

No local pin was amended, rebased or squashed. PUBLICATION.md maps every
original local commit above to its public transport commit, with identical
complete trees and preserved parent topology. Commit metadata and SHAs
changed during connector transport; the local history remains intact.
The reviewer worked in a separate
worktree and model context, saw the exposed preregistration, committed an
independent attack and derivation, then read the author's proof and code.
Its second analytical assistant is disclosed in DERIVATION.md. REVIEW.md
records the exact reviewed commits and scope. This is not external peer
review, blinded input data, or independent scientific execution.

## Publication blocker and its resolution

The local Git push failed because no HTTPS credential was available. No
remote branch was created by that attempt. The connector transport was
checked without moving a branch: it created the preregistration-only
preview object b3563f556a05aa06da2475fbdc9bc13ef00c1f24, tree
961988d9c3395bb75df96dd2101e6c32b8f9cc77. Readback showed author and
committer A. M. Thorn with the account's GitHub noreply address, rather
than the exact author address required by AGENTS.md. The owner subsequently
explicitly approved that connector address on 2026-10-18 Europe/Prague
(2026-10-17 UTC). The earlier preview is now part of the approved transport;
it is not the complete scientific source pin. No policy file was changed.

The complete pre-execution public source pin is
5389b000a6e5178ba99f45a611ebeb07e31051f8, tree
a920cbc42c9f666abf3489cb60f5bf7b3e4f8df7. A public Git fetch checked every
original file byte, all mapped complete trees, all parent relationships
and the clean source checkout before execution. PUBLICATION.md records
the exact frozen PREREG.md, PROOF.md and audit.py hashes. Those files and
the historical ATTACK.md, DERIVATION.md and REVIEW.md remain unchanged.
REVIEW.md's statements about outstanding execution describe its earlier
analytical-review stage; RUN.md now records the subsequent first execution.

The one preregistered run completed with AUDIT PASS: 9072 states, 252 complete
cycles, the sole allowed pair (0,0), and cold-preparation periods 4 and 124.
Exit was zero and stderr empty. No rerun, code correction or threshold
change occurred. The independent handwritten trace remains separate
analytical evidence. No EXPECTED.txt is introduced: the notes contract
stores the exact short stdout in RUN.md. This remains a notes candidate,
not a formal probe under probes/ or a scientific promotion.

## Checks actually performed

Before publication, static ast.parse of audit.py passed without importing
or executing it. The later scientific execution is recorded separately in
RUN.md. The repository's existing checkers completed locally with exit zero:

    POLICY PASS
    CANON PASS v103 claims=530
    LEDGER PASS claims=530 items=594 dependencies=1105 evidence=530 history=1077 gates=26 programs=7
    GATE CONTRACT PASS gates=26 kinds=DEFINITION_PROJECTION:2,DICTIONARY_LIFT:13,FIRED_NEGATIVE:3,OPEN_DECISION:1,OPEN_LIFT:5,OPEN_SELECTION:2

These are repository-integrity checks. GitHub Actions status belongs to the
exact PR head and is reported by the PR checks and its result comment;
ordinary notes CI does not execute audit.py. The unchanged main required
checks were verified separately at startup. No independent scientific
execution or two-architecture scientific acceptance is claimed.
The new files contain only self-authored mathematical text, small standard
library source and public source identifiers. No external code or dataset,
private infrastructure, credentials or unapproved raw transcript is included.
