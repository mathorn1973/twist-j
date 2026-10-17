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

No pin was amended, rebased or squashed. The reviewer worked in a separate
worktree and model context, saw the exposed preregistration, committed an
independent attack and derivation, then read the author's proof and code.
Its second analytical assistant is disclosed in DERIVATION.md. REVIEW.md
records the exact reviewed commits and scope. This is not external peer
review, blinded input data, or independent scientific execution.

## Publication blocker

The local Git push failed because no HTTPS credential was available. No
remote branch was created by that attempt. The connector transport was
checked without moving a branch: it created the preregistration-only
preview object b3563f556a05aa06da2475fbdc9bc13ef00c1f24, tree
961988d9c3395bb75df96dd2101e6c32b8f9cc77. Readback showed author and
committer A. M. Thorn with the account's GitHub noreply address, rather
than the exact author address required by AGENTS.md. That preview is not
adopted as the candidate source pin; no branch ref or PR points to it.
The correctly attributed local commits remain authoritative for this draft.

The complete pre-execution public source pin is therefore still pending.
audit.py has NOT been executed. No scientific stdout, execution count,
finite-inventory PASS, RUN.md or EXPECTED.txt is claimed. The independent
124-step handwritten trace in DERIVATION.md is separate analytical evidence,
not a program run. This is an incomplete notes candidate, not a formally
opened or abandoned probe under probes/.

## Checks actually performed

Static ast.parse of audit.py passed; the module was not imported or run.
The repository's existing checkers completed locally with exit zero:

    POLICY PASS
    CANON PASS v103 claims=530
    LEDGER PASS claims=530 items=594 dependencies=1105 evidence=530 history=1077 gates=26 programs=7
    GATE CONTRACT PASS gates=26 kinds=DEFINITION_PROJECTION:2,DICTIONARY_LIFT:13,FIRED_NEGATIVE:3,OPEN_DECISION:1,OPEN_LIFT:5,OPEN_SELECTION:2

These are repository-integrity checks. No GitHub Actions run exists for this
local branch, and ordinary notes CI would not execute audit.py in any case.
The unchanged main required checks were verified separately at startup.
No full new scientific reproduction or two-architecture acceptance is claimed.
The new files contain only self-authored mathematical text, small standard
library source and public source identifiers. No external code or dataset,
private infrastructure, credentials or unapproved raw transcript is included.
