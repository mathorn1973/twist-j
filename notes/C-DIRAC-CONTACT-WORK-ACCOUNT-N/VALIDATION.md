# Custody and validation

PUBLIC / NON-CANONICAL / L1. Conditional analytical candidate-T.
Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.
Date: 2026-10-26.

## Source custody

STATUS was read before scientific work. POLICY, AGENTS, CORE and FRONTIER
were read from the same public main. The checked authority is:

    main / peeled canon-v105:
    892a0b11089d34e241e1eb76d2c03247022d18e6
    declared content:
    b8cdfd6ea58ae798545bc6000c817147fa0f0dcc
    canon/CANON.md SHA-256:
    73894f331dac3226fe30c86f1ccd893bc2761b0220557e0bfb374d049aa2fa31
    canon/CANON.md bytes: 1295029

All five normative hashes matched. The declared tag and content were
confirmed ancestors of public main. The main x86_64, aarch64 and aggregate
check succeeded in run 40082129555; the matching tag-publication and release
checks also succeeded. These are authority checks of the base, not
scientific executions of this new candidate.

The actual remote-head scan enumerated 316 heads. Current issues, registry,
notes and probes were inspected for collisions before claim #1792.
The inherited comparison file is fixed to #1605 head
da39ea38df90bbf594e90a00f0532964e4e1f041.

## Analytical evidence

PROOF.md SHA-256:

    e1133dbf1fb8226390c2b5eccbc3681fe56368d2ba23c3764248b9a5a9f0d7fd

The complete proof was published in issue #1792, comment 6421407094:
https://github.com/mathorn1973/twist-j/issues/1792#issuecomment-6421407094.
Public readback matched the exact local proof text, including final LF.
Both separate assistant reviews passed at this exact proof hash; their
exposure and limits are recorded in REVIEW.md.

No scientific executable, numerical experiment, EXPECTED.txt, scientific
run record or two-architecture result is supplied by this note.

## Administrative validation

These checks examine repository integrity and documentation policy only.
They do not establish the scientific assertions in PROOF.md.

| Check | Result |
|---|---|
| python3 tools/check_canon.py | PASS: v105, 577 claims |
| python3 tools/check_ledger.py | PASS: 577 claims, 641 items, 1160 dependencies, 577 evidence rows, 1124 history events, 26 gates, 7 programs |
| python3 tools/check_gate_contract.py | PASS: 26 gates, all six declared kinds |
| python3 tools/check_policy.py | PASS |
| Named-file whitespace and scope | PASS: exactly the six declared Markdown files; staged diff has no whitespace errors |

The new scope consists of exactly six Markdown files in
notes/C-DIRAC-CONTACT-WORK-ACCOUNT-N/. No executable or normative file is
modified. Manual review found only original analytical text, public source
identifiers and the required author/license notices. No credentials,
private source material, binary output or new third-party content is
included.

## Publication boundary

The claim and complete proof are publicly reviewable in #1792. An issue
comment is not a Git commit, immutable formal probe pin, merged note or
Canon release. The local branch is notes/c-dirac-contact-work-account-n.

On 2026-10-26 the author explicitly approved the contributor identity
A. M. Thorn <thorn73@proton.me> for this pull request, as the exception
allowed by AGENTS.md. The public commit may therefore use the connected
GitHub identity. Existing document author notices and the exact reviewed
PROOF.md bytes are unchanged.

This publication revision updates only this custody note in the previously
prepared six-file package. Public commit readback, pull-request identity
and CI results are recorded in #1792 and the pull-request conversation.
The publication remains a draft for review, with the same scientific scope
and status as the exact proof already exposed in the issue.

Local administrative validation, if passing, does not replace the required
pull-request CI or manual repository review before any merge. No promotion,
merge or release is authorized by this note.
