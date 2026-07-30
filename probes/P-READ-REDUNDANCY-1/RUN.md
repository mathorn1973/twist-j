# RUN P-READ-REDUNDANCY-1

## Immutable pin

```text
pin_commit: 997ba5cba3b44524d33c8d21d919390386aa4931
prereg_sha256: 51043281560a682cfe2a79620f9594390fb3e6e2ce94c2b21311ef108bd8b1dd
prereg_bytes: 12917
prereg_blob: a423ac3779d85ab6a1916895b28b508f245713cd
verifier_sha256: 2d28ff4ec95274feb625cf0689289f5b2b398d3c8234947c459b533f7db23565
verifier_bytes: 13718
verifier_blob: b263f74df78c939226fb07be12b15726a3776595
```

The pin was pushed to public `probe/P-READ-REDUNDANCY-1` before any formal
gate execution and its public readback was recorded in issue 216. The formal
runner obtained the tree by a fresh `git clone` of the public branch and
checked out the pin commit; the clone reproduced both SHA-256 values, both byte
counts and both Git blob identities before execution. `EXPECTED.txt`, `RUN.md`
and `RESULT.md` were absent from the probe directory at the pin, as
`POLICY.md` section 3 requires.

## Command

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-READ-REDUNDANCY-1/verify.py
```

Machine-readable command field:

```text
command: python3 probes/P-READ-REDUNDANCY-1/verify.py
```

## Local formal leg

```text
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: Python 3.12.3
start_utc: 2026-07-30T11:28:31.369492521Z
finish_utc: 2026-07-30T11:28:33.369501377Z
wall_seconds: 2.000008856
deterministic_executions: 1
pre_status_bytes: 0
post_status_bytes: 0
exit_code: 0
stdout_sha256: 5ffddbd571272bf4b2a9d079acf7ed87481baaaa6f00af3cf7c7efc819bd8efa
stdout_bytes: 1493
stdout_lines: 23
stdout_cr: 0
stdout_final_byte: 10
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
gates: 16 of 16 PASS
verdict: SURVIVED
```

The checkout was clean immediately before and after the single execution.
`EXPECTED.txt` is the exact raw stdout, transported as base64 from the runner
so that no byte is retyped, with LF line endings and a final LF. Stderr was
empty. The formal leg ran through a user-controlled connected runner; its
private machine nickname is intentionally omitted from the public record.

## Required GitHub leg

```text
status: PASS
workflow_run_id: 30539017324
job_id: 90859094699
job_url: https://github.com/mathorn1973/twist-j/actions/runs/30539017324/job/90859094699
check_name: check
event: pull_request
tested_head_commit: 6046c09646e235cf6c847a4d38c23561f4c3e2f3
checkout_merge_commit: 618de5a15d1e3f82cf1ac291bb2b43daa6f0111a
base_commit: 9d17a1e7d10e6ffb93c104e53faecc6d5c1aeb47
platform: Ubuntu 24.04 GitHub-hosted runner image ubuntu-24.04
architecture: x86_64
python: Python 3.12.13
verifier_sha256: 2d28ff4ec95274feb625cf0689289f5b2b398d3c8234947c459b533f7db23565
stdout_sha256: 5ffddbd571272bf4b2a9d079acf7ed87481baaaa6f00af3cf7c7efc819bd8efa
verdict: VERIFY PASS
```

The required clean GitHub check reran the public pinned verifier and matched
`EXPECTED.txt` byte for byte. The architecture field is not self-reported:
`tools/check_verifier.py` fails the job unless `platform.machine()` is
`x86_64` when `GITHUB_ACTIONS` is true, so `VERIFY PASS` certifies it.

## Two-architecture gate

```text
local leg   aarch64,  stdout_sha256 5ffddbd571272bf4b2a9d079acf7ed87481baaaa6f00af3cf7c7efc819bd8efa
GitHub leg  x86_64,   stdout_sha256 5ffddbd571272bf4b2a9d079acf7ed87481baaaa6f00af3cf7c7efc819bd8efa
verdict     SATISFIED
```

The local formal leg is `aarch64` and the required GitHub leg is `x86_64`, and
their stdout is byte identical. The two-architecture computation gate of
`POLICY.md` section 4 is therefore satisfied for this verifier.
