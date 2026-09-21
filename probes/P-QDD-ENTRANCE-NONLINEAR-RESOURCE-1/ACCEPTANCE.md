# Public two-architecture acceptance

Status: **PASS; candidate-T; L1; NON-CANONICAL**.
This accepts the mathematical proof audit. It is not physical entrance
realization, an experimental run, or a Canon registry change.

scientific_pin: 9e9dab762d618a9138f4ab293161017b8a5b0b93
tested_result_head: 25009a1c7b0106d33f00071bf32edf6b2df6ccb9
base_main: 691fe341a95d8fc48e3c2c5982d22419f5deced8
pull_request: https://github.com/mathorn1973/twist-j/pull/1088
workflow_run: https://github.com/mathorn1973/twist-j/actions/runs/35517532486

| Required job | Result | Public evidence |
| --- | --- | --- |
| architecture-x86_64 | success | https://github.com/mathorn1973/twist-j/actions/runs/35517532486/job/106095876617 |
| architecture-aarch64 | success | https://github.com/mathorn1973/twist-j/actions/runs/35517532486/job/106095876750 |
| check | success | https://github.com/mathorn1973/twist-j/actions/runs/35517532486/job/106095934131 |

Both architecture logs explicitly report the same pinned verifier and
byte-identical stdout, matching RUN.md and EXPECTED.txt:

verifier_sha256: 88f5f99f93cea1c34aa5c03688921a42b16f40a291fc2e8512330e0faedec5bd
stdout_sha256: a0f6a981f4722c0986d39666e1ef0d2760a9f2076f38a3f25c7a3591f472cc29

The independent reviewer completed REVIEW.md without reading verify.py
or executing a scientific program. That is independent written proof
review, not another implementation or architecture reproduction.
The post-run RESULT.md/RUN.md scope review also passed.

All seven scientific files remain byte identical to the public pin.
This acceptance-only commit changes none of them. Its final PR head
must pass both architecture jobs and aggregate check again before merge.
The PR retains the final-head evidence and merge/readback identity.

The full-class and all-duration conclusions rely on the written proofs;
the finite verifier audits exact premises and the complete four-point
construction. The two-tick minimum counts native selector operations
under admitted affine interventions, not elapsed physical time.
Their physical origin, duration and complete environment remain open.
Canon v90, STATUS.md and the entire canon/ directory are unchanged.
