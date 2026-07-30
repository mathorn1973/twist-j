# RUN P-BOOST-COHERENCE-1

## Immutable pin

```text
pin_commit: 8214beb80fb9cc97f2cdf1f1b23f74afebae273f
prereg_sha256: d1d2bce9f63d2b9c0481c59bfaac32c3c75289ce26dece993db7a4cf9d708e71
prereg_bytes: 15347
prereg_blob: 424dbc01658dbab45b56245cc776d613b8f2ebce
verifier_sha256: 3b79ebf025bde6e15f8f25a9856f242a219e3c159329d65029148c16a86abe2c
verifier_bytes: 18479
verifier_blob: 1d73cb1f8aa88e2dc7ee2bc73dc99225372dd7ff
```

GitHub public readback matched the full pin commit, both byte streams, both
SHA-256 values, and both Git blob identities before execution.

## Command

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-BOOST-COHERENCE-1/verify.py
```

Machine-readable command field:

```text
command: python3 probes/P-BOOST-COHERENCE-1/verify.py
```

## Local formal leg

```text
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: Python 3.12.3
start_utc: 2026-07-29T18:56:03.989469056Z
finish_utc: 2026-07-29T18:56:04.040629894Z
wall_seconds: 0.049445849
deterministic_executions: 1
pre_status_bytes: 0
post_status_bytes: 0
exit_code: 0
stdout_sha256: 426855610214b6b83a62007dce6adc2a20ae389e42af3617615559a0904d1907
stdout_bytes: 311
stdout_lines: 9
stdout_cr: 0
stdout_final_byte: 10
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
groups: 8 of 8 PASS
checks: 477
verdict: SURVIVED
```

The checkout was clean immediately before and after the single execution.
`EXPECTED.txt` is the exact raw stdout, with LF line endings and a final LF.
Stderr was empty. The formal leg ran through a user-controlled connected
runner; its private machine nickname is intentionally omitted from the public
record.

## Required GitHub leg

```text
status: PASS
workflow_run_id: 30482405522
job_id: 90679567824
job_url: https://github.com/mathorn1973/twist-j/actions/runs/30482405522/job/90679567824
check_name: check
tested_head_commit: bf2aa420efead351042df4ebb34e5214779633d5
checkout_merge_commit: e5e0f5d3cad5381ee479977857c1c196f1faf93f
base_commit: 48213275d0ace92d8f034166179a9fee4d53d908
platform: Ubuntu 24.04 GitHub-hosted runner image 20260720.247.2
architecture: x86_64
python: Python 3.12.13
verifier_sha256: 3b79ebf025bde6e15f8f25a9856f242a219e3c159329d65029148c16a86abe2c
stdout_sha256: 426855610214b6b83a62007dce6adc2a20ae389e42af3617615559a0904d1907
verdict: VERIFY PASS
```

The required clean GitHub check reproduced the public pinned verifier and
matched `EXPECTED.txt` byte for byte. The local aarch64 leg and GitHub x86_64
leg therefore complete the two-architecture gate for the verifier-backed
