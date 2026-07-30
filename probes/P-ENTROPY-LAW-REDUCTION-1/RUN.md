# RUN P-ENTROPY-LAW-REDUCTION-1

## Immutable pin

```text
pin_commit: 605b9f2bb416ba2b7abe5c508610c893c32272e1
prereg_sha256: b53f199e9722072449c76b1bb48a7453a68613dce6d8fe2e60cadbe6c2535cb3
prereg_bytes: 11750
prereg_blob: a490f026c510d0ba74cd07049a0d4040832d2b0f
verifier_sha256: 153f4ac98972cd44ce4921defed9980020258b074b4d7a3cf130c6a8598df9c5
verifier_bytes: 8972
verifier_blob: 7afa93fcb02698ae79250289d699f2ac717c0465
```

Issue #226 was opened before the branch, path, pin, or formal execution. The
branch started from public `main` commit
`501f7d9f3d1dc8a915ad7fcc1f33f0673b5b4b8a`. The contents API produced two
additive commits, with no execution between them. The second commit above is
the immutable pin containing exactly `PREREG.md` and `verify.py` relative to
the branch base. Public readback reproduced the byte counts, SHA-256 values,
and Git blob identities before execution.

## Command

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-ENTROPY-LAW-REDUCTION-1/verify.py
```

Machine-readable command field:

```text
command: python3 probes/P-ENTROPY-LAW-REDUCTION-1/verify.py
```

## Local formal leg

The following legacy fields are required by the current public checker. They
refer only to the local formal leg. The separately named fields below make that
scope explicit and prevent the record from being read as a two-architecture
claim.

```text
platform: Linux 6.12.13
architecture: x86_64
python: Python 3.13.5
exit_code: 0
stdout_sha256: e99e828ff3f6531d6e660589c1c8da03f0e5d211a50faca26f968f23aa8c4ca6
stdout_bytes: 1094
stdout_lines: 17
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

local_platform: Linux 6.12.13
local_architecture: x86_64
local_python: Python 3.13.5
local_finish_utc: 2026-07-30T15:50:48Z
local_start_utc: not_recorded
local_wall_seconds: not_recorded
local_deterministic_executions: 1
local_exit_code: 0
local_stdout_sha256: e99e828ff3f6531d6e660589c1c8da03f0e5d211a50faca26f968f23aa8c4ca6
local_stdout_bytes: 1094
local_stdout_lines: 17
local_stdout_cr: 0
local_stdout_nul: 0
local_stdout_final_byte: 10
local_stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
local_stderr_bytes: 0
local_gates: 13 of 13 PASS
local_verdict: PROOF-SURVIVES at local audit stage
```

The exact raw stdout is `EXPECTED.txt`. The frozen verifier process exited 0
and wrote no stderr. After the process and stream capture had completed, the
surrounding container orchestration attempted a terminal-clear operation
without `TERM` and returned wrapper status 1. This outer wrapper artifact did
not alter the verifier exit, stdout, stderr, checkout, files, or scientific
decision. It was disclosed in issue #226 before these records were committed.

## Required GitHub leg

```text
github_status: PENDING
github_architecture: PENDING
github_stdout_sha256: PENDING
github_verdict: PENDING
```

The pull-request check must rerun the identical pinned verifier on GitHub
x86_64 and compare `EXPECTED.txt` byte for byte. Issue #219 records that the
current checker flattens repeated legacy keys. Therefore this record does not
infer a two-leg architecture pair from checker parsing. The GitHub fields will
be filled from the public workflow return by an additive commit.

## Architecture and status boundary

```text
cross_architecture_gate: NOT_CLAIMED
computation_grade_T_gate: NOT_REQUIRED_FOR_PROOF_SOURCE
scientific_source: WRITTEN_EXACT_PROOF_IN_PREREG
verifier_role: FINITE_AUDIT
public_canon_status: UNCHANGED
entropy_layer_bridge: O_UNCHANGED
```

The local leg and expected GitHub leg are both x86_64. Any byte identity is a
reproduction only. The intended theorem status rests on the exact written
proof, not on a computation-only promotion. A separate reviewed fold is needed
for any Canon, registry, frontier, evidence, dependency, gate, status, release,
or authority change.
