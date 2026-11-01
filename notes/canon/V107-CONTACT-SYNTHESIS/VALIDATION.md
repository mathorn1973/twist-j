# Integration rehearsal

**NON-CANONICAL / validation record in progress.**
Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.

Scientific integration input:
`1dd574c2193f61a350f7c20e542ba1023a5b77c3`.

This public merge commit contains the four unchanged source bundles. Its
normative Canon, STATUS, policy, workflow and tools equal current v106 main.
All scientific scripts were already publicly pinned by their source authors.
The rehearsal runs those existing scripts; it introduces no scientific
executable, threshold, fixture or expected-output change.

Two fresh detached Linux checkouts were clean before execution. The source
file identities are in SOURCES.tsv. Captures are outside the checkouts.
Environment: PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1,
PYTHONIOENCODING=utf-8, LC_ALL=C.UTF-8.

The x86_64 rehearsal runs repository policy,211 unit tests, Canon, ledger and
gate checks; the contact and two Gram/archive programs; the minimum probe;
and the complete public-probe and minimal-reproduction inventories with
`--base` omitted. The aarch64 replay runs the same static/unit checks and
the four directly relevant scientific programs. Whole historical-inventory
replay on aarch64 is not asserted by this record.

All program comparisons use their committed EXPECTED files, require exit0,
empty scientific stderr and byte-identical stdout. Unit-test diagnostics on
stderr are normal and are not scientific stderr. Operational durations and
machine environments do not enter mathematical output equality.

Final observed results and source/output hashes will be added after the
running jobs finish. This is an integration rehearsal, not the future
v107 release-form full gate; no release manifest is generated here.

## Completed relevant-source replay

Both executions used the exact integration pin above, Linux, and unchanged
source files. x86_64 used Python 3.12.3; aarch64 used Python 3.11.2.
The latter is supplementary architecture evidence, not a claim to be the
GitHub-required Python 3.12 workflow. That PR gate is reported separately.

Policy, all 211 unit tests, Canon v106, ledger and explicit gate checks passed
on both architectures. All four scientific programs exited 0 with empty stderr
and matched their committed EXPECTED files byte for byte on both architectures.

| Program | Verifier SHA-256 | Stdout bytes | Common stdout SHA-256 |
| --- | --- | ---: | --- |
| contact | `0089529bd6f4a9488cbc74197a55912453fc48a1967859bce87c3986cea4951e` | 776 | `89e49565965d9d417cebefd6eb7b36bea864788e8356bbad8901043f1ad66890` |
| gram | `71f0cd9f73cf6a1ae0cded830e575e043d8f70b9b065be806f7617929dd8e3e3` | 681 | `79db6a2aa751b0362b5609e2293d33279510f59f7cbe5a51f5ac9ce0a09f1c12` |
| gram-break | `a4f86eef9e3440c368f82a560bcad2bf762ac953c55d0fbf045a4b56cb987b42` | 1628 | `66a8d32d76aff04e579daecd9f4d7fa30dc65a7ba5df0ceb7d731144afdc8032` |
| minimum | `461b29dc6d3282a00fcccfd0cc194b198f856b688f78841658c93e49ecccac8f` | 1755 | `95ee2135ecb491ab7f0702d603ea94013d00beb28e70668a3c418c0f21478178` |

Program paths and expected-file identities are fully enumerated in SOURCES.tsv.
The aarch64 checkout was clean after the completed replay. The x86_64 full
inventory is still executing at this record revision; no completion claim is
made for it yet. Scientific hash agreement supplies reproduction evidence,
not the separate mathematical acceptance requested in REVIEW.md.
