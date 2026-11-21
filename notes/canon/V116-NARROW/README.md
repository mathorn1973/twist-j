# Proposed Public Canon v116

**NON-CANONICAL.** This proposal adds two finite L1 computations at status C. Public Canon v115 already records two naturally produced words that select B1 and B2 at the same readiness of cell 2. The new results follow each selected output to its first material change. Either branch can deliver an intact word that changes cell 3. Across the comparisons that were actually run, the number of qualifying matched B1/B2 deliveries is zero. Q9, the selection of the physical electromagnetic coupling, remains open.

## Proposed entries

| Source and proposed claim | Eligible B1 / B2 reads | B1 / B2 outputs that changed cell 3 | Compatible pairs found |
| --- | ---: | ---: | --- |
| #2053 · `C-H3-RECEIVER-OUTPUT-RELAY-N` · $1 \le t \le 2^{26}$ | 554 / 159 | 102 / 13 | 0 within the prefix. Successful deliveries have 17 B1 and 9 B2 readiness states, with no overlap. |
| #2055 · `C-H3-RELAY-CONTINUATION-N` · $2^{26} < t \le 2^{30}$ | 6,940 / 2,852 | 702 / 188 | 0 for the 702 new successful B1 reads against the fixed B2, the 13 successful prefix B2 reads, or all 201 successful B2 reads through the ceiling. |

Both computations follow the original rank-43 trajectory from launch. Each comparison requires recurrent source writes, equal six-word readiness at cell 2, distinct ordered source words, arrivals and outputs, and material change at cell 3 on both arms. The two fixed outputs from v115 both met refusal at cell 3. A later B2 read at tick 36,442,233 with the same local input and output as the original B2 did deliver on the next tick. In the continuation even its four pre-contact rails at cell 2 recurred zero times across 503,316,480 opportunities.

The comparison of a B1 read at or before $2^{26}$ with a B2 read after $2^{26}$ remains open. The upper bound applies to this one trajectory. The source review identifies the prospective search, the retrospective controls and confirmation, and the exact public evidence for each statement. [Source review](SOURCE_REVIEW.md)

## Content patch

The patch applies to the scientific main at `f3e27393bc2e329ac84232ab1a1a07dd81ea77d7`. A fresh Git index at that base produced the exact content tree below under `git apply --cached --whitespace=error-all`. The patch preserves all 632 earlier registry rows, the 25 open H/O claims and their frontier, the gate and dependency ledgers, and all 43 reproduction directories. The proposed registry has 634 entries, with 479 T, 62 D, 49 C, 2 H, 23 O and 19 F. [Content patch](CONTENT.patch) · [Reviewed base](https://github.com/mathorn1973/twist-j/commit/f3e27393bc2e329ac84232ab1a1a07dd81ea77d7)

| Artifact | Bytes | Digest |
| --- | ---: | --- |
| CONTENT.patch (SHA-256) | 48,791 | `ab801673c85463f826f7c4a67e61636d4c903e891ec28414e2219a40a5f50692` |
| Proposed canon/CANON.md (SHA-256) | 1,568,802 | `ea4f924dc02838fcfe47d9b983bc0be929da7378ee9278c48831f34a5c393695` |
| Content tree (Git object) | | `6731c700bceb4e0f0a8200ca92893403fbfd8321` |

To apply the content in a clean worktree at the reviewed base, use `git apply --index --whitespace=error-all <path-to-CONTENT.patch>`. The patch has 13 paths. It contains the Canon text and ledger edits, the regenerated digests, the status-separation check and its expected output, and the inventory assertions. The two-commit public release procedure binds a future content commit in its release form. [Release procedure](https://github.com/mathorn1973/twist-j/blob/f3e27393bc2e329ac84232ab1a1a07dd81ea77d7/AGENTS.md#6-formal-work-after-cutover)

## Verification

In a clean local Linux checkout of the proposed content with a trial release form, all 248 unit tests passed. The policy, Canon, ledger, gate-contract, generated-view and static activation checks passed. The status-separation reproduction matched its 41,399 expected bytes with 262 passing checks. Its first 256 numbered results are byte-identical to v115.

The working-session review replayed the default #2053 verifier on Linux x86_64 and matched all 3,019 expected bytes. Its separate five-coordinate history replay followed both fixed reads through their terminal cuts and matched the published 373-byte output digest. A fresh grouping of the 713 recorded prefix observations, checked against the diagnostic digest published in #2053, recovered all 44 and 48 readiness states, the three shared states, and the disjoint sets of 17 and 9 states among deliveries. [Prefix execution and diagnostic record](https://github.com/mathorn1973/twist-j/blob/519766f6215bc613423c69666ccc1730201fe56b/probes/P-H3-RECEIVER-OUTPUT-RELAY-1/RUN.md)

The #2055 verifier also ran again on Linux x86_64 from launch to tick 1,073,741,824. Its 1,539 stdout bytes matched the public transcript, including the explicit positive confirmation flag. All three local source runs exited with status zero and empty stderr. The public x86_64 and aarch64 jobs on each source PR and its merge provide the two-architecture evidence for those results. [Continuation transcript](https://github.com/mathorn1973/twist-j/blob/1ef0a6e0df49efcf06a8f32545c6ff1bd1f15119/probes/P-H3-RELAY-CONTINUATION-1/EXPECTED.txt) · [Source workflow records](SOURCE_REVIEW.md#public-replay-and-custody)
