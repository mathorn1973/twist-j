# Integrity and operational checks

**PUBLIC / NON-CANONICAL / L1.**
A. M. Thorn. SPDX-License-Identifier: Apache-2.0.

## Authority and claim

On 2026-10-18 the public main and peeled canon-v103 were
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d. The declared content
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66 is an ancestor.
All five canon/SHA256SUMS entries matched. CANON.md is 1052518 bytes,
SHA-256 d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b.

The completed main-push run
[39022927713](https://github.com/mathorn1973/twist-j/actions/runs/39022927713)
has successful architecture-x86_64, architecture-aarch64 and check jobs.
The separate publication jobs in runs 39022952253 and 39033710211
succeeded. Skipped architecture contexts on those publication events
were not counted as architecture successes.

The exact #1628 body hash/size matched ASSIGNMENT_RELEASED_P, followed by
a read-back CLAIMED_P before research edits. An explicit live
git ls-remote --heads scan, open-issue identifier search and
registry/probe/note path inspection found no pre-existing identical
P-contact branch or claim. The subsequent focused dependency audit
checked ten issue/PR pairs and their comments; it did not replace the
remote-head scan.

## Checks actually performed before drafting

- python -B tools/check_policy.py: POLICY PASS.
- python -B tools/check_canon.py: CANON PASS v103 claims=530.
- python -B tools/check_ledger.py: LEDGER PASS, 530 claims, 594 items,
  1105 dependencies, 530 evidence entries, 1077 history entries, 26 gates.
- python -B tools/check_gate_contract.py: GATE CONTRACT PASS, 26 gates.

The final local submission checks and source-custody readback are recorded
below. This notes-only candidate has no scientific
executable. Its CI checks do not establish scientific computation on
two architectures, and no new candidate-C result is inferred.


## Final local submission checks

The named staged artifact set contains exactly nine files under
notes/C-NATIVE-P-CONTACT-REALIZATION-N/. No foreign or normative path
is changed. git diff --cached --check passed.

The source manifest was independently rebuilt from Git objects for
33 rows. Every blob identity, byte count and SHA-256 matched.
The primary PREREG.md, PROOF.md, WEYL.md and SOURCES.tsv are byte-identical
between source pin 2c618efc2e28606edb12ada2f77a06aa0d798d55 and source head
29c73cd91870486eb78d533b27aa7b2d9324eb72. Ten overlapping rows of the source
author's SOURCES.tsv also matched the directly read Git objects.
The new SOURCES.tsv SHA-256 is
45ecc0ed94c258518fee2af94e775c8d3cf703c0e404a900f62c03de053e17e7.

Policy, ledger and explicit gate checks passed on the staged package.
The unchanged Canon had already passed the authority check.
The repository changed-path commands with base
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d returned
VERIFY NOT APPLICABLE and REPRODUCE NOT APPLICABLE.
They selected no scientific verifier and are not scientific replays.

All nine new files use LF and ASCII, their local links resolve, their
working bytes equal their staged bytes, and public-safety inspection
found no secrets, personal paths, private infrastructure or unrelated
material. The staged diff was inspected explicitly. The two mathematical
and one operational subagent reviews are same-session checks; their
wording corrections are incorporated.

Public branch/PR readback and live CI are reported in the submission
receipt. CI success is not presumed here and, for this notes-only change,
does not become scientific two-architecture evidence.
