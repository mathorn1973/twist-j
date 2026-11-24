<!-- SPDX-License-Identifier: Apache-2.0 -->

# First local executions

NON-CANONICAL / L1 / candidate-C. One Linux x86_64 lane, Python 3.12.14.
No two-architecture scientific gate. No scientific rerun was performed.

Preregistration commit: `782ada5f` (local Git).
Complete source pin: `16699dfd6884a15f8b4b7d84c66a5fa7cbe4ba90` (local Git).
Both sources were frozen before either execution; source tree was clean.
The issue records the source hashes before the first run. These are incubation
pins, not publicly fetchable preregistration commits or formal public gates.

## verify.py

Command: `python notes/C-COLOCATED-LOADED-WRITER-1/verify.py`.
Start UTC: `2026-11-07T23:24:28.699148+00:00`.
End UTC: `2026-11-07T23:24:47.387091+00:00`.
Exit code: 0.
Stdout bytes: 4185. Stderr bytes: 0.
Stdout SHA256: `c937ad08b6cc0d1607785d1085e5beda719f62af4e191ee368290b7b8fc37803`.
Stderr SHA256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## break.py

Command: `python notes/C-COLOCATED-LOADED-WRITER-1/break.py`.
Start UTC: `2026-11-07T23:24:28.682526+00:00`.
End UTC: `2026-11-07T23:24:54.340760+00:00`.
Exit code: 0.
Stdout bytes: 15940. Stderr bytes: 0.
Stdout SHA256: `0e4a20a8501784bd23da6400a117669cfa2088375ab4e6ea3fc74f519e917ba6`.
Stderr SHA256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## Frozen source custody

- PREREG.md: 7269 bytes; `42c992aed32728b74bb5adb9ffbedef86bbb0f7b75bedfdfc12da7b7f26bbc9f`.
- PROOF.md: 6807 bytes; `e5a4cec29c2b48d82f78ef2a5afacb7b8b04fcce6d00ab89d69d4d453592559a`.
- verify.py: 8409 bytes; `0917057f128028a68d9cbb181b7873e9712dd5790d417714e73bf69855c38509`.
- break.py: 17061 bytes; `12af80fa127c378ecddcd15b48dc1a766a2cc4566eea62a25de7418ef1dfd9a8`.

## Post-run comparison and repository checks

`python notes/C-COLOCATED-LOADED-WRITER-1/compare_results.py` reports:

```text
PASS: 87 common result comparisons; all 125 phase outputs agree.
```

The comparison helper was written after both first outputs and only reads
those immutable outputs. Different JSON layouts explain their different
byte hashes; the normalized full 125-row phase table is identical.

`python tools/check_policy.py`: POLICY PASS.
`python tools/check_canon.py`: CANON PASS v109 claims=609.
Notes-only CI must never be described as execution of these new checkers.
