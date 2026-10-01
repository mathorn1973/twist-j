# Post-public-pin replay evidence

PUBLIC / NON-CANONICAL / candidate-T by conditional proof / L1.
Reservation [#1311](https://github.com/mathorn1973/twist-j/issues/1311).
Draft [PR #1312](https://github.com/mathorn1973/twist-j/pull/1312).
Authority remains v95. Date2026-10-01.

## Provenance and immutable source pin

The public replay source pin is
[`f50ed0db08aec323cc5d7f0959114207cab56359`](https://github.com/mathorn1973/twist-j/commit/f50ed0db08aec323cc5d7f0959114207cab56359).
It has parent `dd354e3e01ad7f7bb535f33e012c5ef1b46a87d2`, the exact open
#1310 dependency. It adds13 small text files: this candidate's ten original
and publication files, plus the three-file reproduction entry. This RUN.md
is a subsequent reporting-only addition. No source file in the pin is changed.

The original six-file local package is unchanged. Its Windows exploratory
run occurred **before any public pin**; the known induction, output counts
and digest were already exposed. RESULT.md records that earlier run only.
The new PREREG.md freezes a prospective replay of known results. None of the
runs below is described as a new independent discovery, retrospective
preregistration or fresh clean-room implementation.

After commit and push, all13 new files and four inherited law/runtime inputs
were fetched as actual GitHub Contents API bytes at the exact source pin.
Each public body matched the local bytes, and the public branch ref matched
the full pin. All17 readbacks completed before new scientific execution or
opening the draft PR. The12 entries of PUBLIC_SHA256SUMS matched. The bridge
checks11 explicit source/provenance hashes before executing either adapter.

| Frozen input | SHA-256 |
| --- | --- |
| New PREREG.md | ca6a02fbd8d5942a2d7fb5e5e9017f8c94f1a1131a6524aea5f3e73a53d6cbcd |
| New PROOF.md | 03913a77dfcc0e266668ebdd66594a287c3fa077ed1292596f91b775dc2d0df7 |
| New audit.py | 283a51e9e94ee70d5fd36106d64dec43e481ad6efde7594402d072b23e90f9a6 |
| New audit_challenger.py | eaf429421c7e57c16dd1be97a469cbb63313b48597e44a4efd65a87f9087a267 |
| Reproduction verify.py | bfbd1cec8e7b3bec1d3d41d703656e5d28b617d63fe8f1843f248a9f40c9324c |
| Reproduction EXPECTED.txt | c77b74b795dfe030c8b3dde34a8ff3755e9659d0e03da8f14b5245600640a394 |

EXPECTED.txt is554 LF bytes derived prospectively from the already known
seven-line local stdout. Its original LOCAL AUDIT PASS wording is retained;
the distinct runner receipt below is the new public replay evidence.

## Actual Linux-compatible local replay

The first Linux preflight encountered a Windows-format worktree metadata
path and stopped before invoking the scientific runner. A clean ordinary
clone of the same public-verified pin supplied Linux-compatible Git metadata.
No scientific input, fixture, threshold, runner or timeout was changed.
The successful replay started with exact HEAD equal to the public pin and
an empty git status. All public manifest hashes were checked before and after.

Command, from that checkout's repository root:

```text
python3 -B tools/check_reproduce.py --base dd354e3e01ad7f7bb535f33e012c5ef1b46a87d2
```

| Item | Actual value |
| --- | --- |
| Platform | Ubuntu22.04, WSL2 |
| Architecture | x86_64 |
| Python | CPython3.10.12 |
| Duration | 15.421 seconds |
| Exit | 0 |
| stderr | 0 bytes |
| Runner stdout | 181 bytes, LF |
| Runner stdout SHA-256 | 1da2363e70cd1484a5cc536fe8ac9c0d4fb0d86086dc83ffa467be25e4f07518 |
| Source hashes before/after | unchanged |

Exact runner stdout:

```text
REPRODUCE PASS field-finite-chain-first-delivery-n bfbd1cec8e7b3bec1d3d41d703656e5d28b617d63fe8f1843f248a9f40c9324c c77b74b795dfe030c8b3dde34a8ff3755e9659d0e03da8f14b5245600640a394
```

The unchanged runner enforces its120-second limit, scientific exit0, empty
scientific stderr and byte equality with EXPECTED.txt. Its success therefore
records an actual execution of the bridge and both generic full-state adapters,
not merely a source-hash check. No predecessor main or old three-cell run is
used to stand in for this new execution.

## Actual public two-architecture gate

[Workflow run36842242086](https://github.com/mathorn1973/twist-j/actions/runs/36842242086)
completed successfully on source head
`f50ed0db08aec323cc5d7f0959114207cab56359` after public readback.

| Job | Actual result | Python | Log evidence |
| --- | --- | --- | --- |
| [architecture-x86_64](https://github.com/mathorn1973/twist-j/actions/runs/36842242086/job/110303833159) | success | 3.12.14 | identical REPRODUCE PASS receipt above |
| [architecture-aarch64](https://github.com/mathorn1973/twist-j/actions/runs/36842242086/job/110303833400) | success | 3.12.14 | identical REPRODUCE PASS receipt above |
| [check](https://github.com/mathorn1973/twist-j/actions/runs/36842242086/job/110304221828) | success | not applicable | both architecture jobs succeeded |

The actual completed log text was read for both architecture jobs. Each
contains the receipt for this exact reproduction name, bridge hash and
expected-output hash, not just an aggregate green status. Each also passed
policy,172 repository unit tests, Canon, ledger and gate-contract checks.
The publication job was correctly skipped for this draft PR. The workflow
and repository runner are unchanged. Public x86_64/aarch64 byte agreement
establishes the computation replay gate for this exposed candidate.

The audit again checks20 unit-energy seeds,6280 complete connected states,
151 cut cases,2805 cut boundaries and2079 occupied-contact cases. Exact
first times and full-state formula agree. The all-N and all-time claims
continue to rest on the conditional proof. The N+1 receiver return remains
an analytical consequence: no connected execution beyond N was added.

## Review and disposition

Two separate read-only publication reviewers found no blocker before the
pin. Their final static readbacks verified every bridge source hash, all
public manifest entries, expected-output bytes, module loading, enabled
assertions, preserved scope, historical exposure and public safety. Neither
ran the scientific programs as part of that static review. REVIEW.md records
their remit; the original mathematical reviews remain in historical RESULT.md.

This record adds no new law, preparation, chain length, memory register or
scientific scope. The proof, both adapters, original six-file package,
prospective protocol, bridge and expected bytes remain identical to the pin.
The final PR may have a later reporting-only head; its required checks must
also pass before handoff, without changing any pinned scientific input.

Disposition: reviewed draft candidate only, NON-CANONICAL/candidate-T/L1.
No merge, Canon/registry edit, promotion, tag, release or memory construction.
The stacked dependency #1310 remains explicit and unmerged. The local
receiver-record problem has not been opened or executed by this handoff.
