# Result: exact S3 byte reproduction on two architectures

**NON-CANONICAL / L1. S3-ARCHITECTURE-REPLAY-4: PASS.**

All four unchanged programs from source commit
73f3cb4946b05f5d63aba1c279642f77c699caef reproduced their existing expected
stdout byte for byte on both x86_64 and aarch64. Each execution exited 0
with empty stderr. No timeout, retry, source repair, new scientific
criterion or expanded search occurred.

The reproduction contract, capture-only runner and 25-file manifest were
committed at b4c9333872d9adde283a62fae0c0f26e357539a5, pushed and publicly
read back byte for byte before either architecture executed a program.
The runner and manifest were also independently retrieved through Git
on the aarch64 environment and checked against those same public hashes.
The source HEAD, clean checkout and all 25 source files were verified
before and after each architecture's four-process sequence.

## Captured evidence

| Architecture | System | Python | Start UTC | Processes |
| --- | --- | --- | --- | ---: |
| x86_64 | Windows 11 | 3.12.10 | 2026-11-08 16:40:19 | 4 |
| aarch64 | Darwin 27.0.0 | 3.13.13 | 2026-11-08 16:40:56 | 4 |

RUN-X86_64.json and RUN-AARCH64.json are the unmodified captured receipts.
They contain per-process start time, measured elapsed seconds, operational
timeout, exit code, byte counts, hashes and comparison results.
Raw captures were retained outside the repository and compared directly
between architectures. Because the bytes match the existing four public
outputs exactly, no duplicate scientific stdout is added here.

| Program | stdout bytes on each architecture | SHA256 on both |
| --- | ---: | --- |
| verify.py | 4165 | 724329795a84ff5f00a908a72ab31ab9ccf8be486def5e58c43a09fcc64c2203 |
| audit.py | 3707 | 163342bdcd442a962d2281fd9406cb50dc946ebf0fa7e8d0e526b23446a2e9db |
| assembly.py | 2906 | fcc72a214caf784942ffdc5a0ed1c05b48c69c8a1558148d6987382c7b9ae74f |
| search.py | 449 | b7dcf988c9a6bbcdc900e0fd60f6f8c8c7e8f3720316e118441d276d91c4378a |

Each architecture therefore reproduced the original compiler checks,
literal 14-case / 19-cycle assembly and bounded BFS output. The assembly
still audits 2597775 contacts and 50 SWAPs including complete inverses.
The BFS result is still INCONCLUSIVE / DEPTH_CAP; a successful reproduction
does not turn that search outcome into a positive existence result.

## Independent review intake

PR #1962 at c6134c0dff24b04e2597cb1d660bf375add5222c reports
PASS WITH NOTES and zero DIFF-REAL for the original source head.
It supplies a structurally separate implementation and state/trace
comparisons. This is distinct from our same-session authoring checks.

The review's declared code/output blindness is qualified by its disclosed
knowledge of the equations, cases and headline numbers. Its PREREG was
committed before its first execution; its corrected checker was frozen
after an initial failed implementation and a successful repaired run.
The public record does not contain the original failed checker revision
and complete failed stdout promised by PREREG section 4. This custody gap
is retained explicitly and is not resolved by the present replay.
It does not supply a mathematical counterexample to the construction.

## Status and consolidation boundary

The previous missing aarch64 replay of the four author programs is now
supplied by actual scientific executions, not by repository CI.
This is byte reproduction by the authoring session on two architectures,
not another independent implementation or a new blind review.
The reviewer checker itself was not rerun in this experiment.

The analytical all-finite-k result remains a proof supported by finite
audits. This receipt does not create a formal probe registration, assign
a Canon claim status, merge a PR or release v110. Any future fold must
integrate the exact proof and admitted reproducible evidence under the
governing repository protocol. FOLD-PLAN.md identifies that limited scope.
The original 24 note files, both original source pins and the independent
review branch remain unchanged.
