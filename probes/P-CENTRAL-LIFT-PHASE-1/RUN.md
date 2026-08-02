# RUN P-CENTRAL-LIFT-PHASE-1

## Immutable pin

```text
pin_commit: 0c8adc4ea22b88c5fb65f78ea567cd4e04f9aa26
prereg_sha256: dfd55508116db2020c21a0b5cf424d201a1d3e034833b072dcf451f87be6fb3a
prereg_bytes: 12907
prereg_blob: ed12d90527cec30fc37d5221b5045e68ebf45bbb
verifier_sha256: d062a009a98db0e1c26f1c95b2e3df04f04f14a79f68df4ec7784a9d8d40e163
verifier_bytes: 4706
verifier_blob: 9157af72c144074a20dd01a46c5c3053f21eda76
```

Issue #251 was opened before the branch, probe path, pin, and formal
execution. The branch started from public `main` commit
`60228fa5784f10df69ea6e3d96872b6652909628`. The immutable pin above is
its one direct child and contains exactly `PREREG.md` and `verify.py`.
It was pushed to public branch `probe/P-CENTRAL-LIFT-PHASE-1` before the
first formal execution. The owner accepted the exact section 7 proof
and scope as theorem-grade before the pin.

## Command

```text
command: python3 probes/P-CENTRAL-LIFT-PHASE-1/verify.py
```

Executed once from the repository root in the deterministic environment
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`.
The exact raw stdout is `EXPECTED.txt`.

## Local formal leg

```text
platform: Ubuntu 24.04
architecture: x86_64
python: Python 3.12.3
exit_code: 0
stdout_sha256: 0609c48f3df68d79c0cea9fd38cbccaab14ad908590f00767a51322944a994cc
stdout_bytes: 826
stdout_lines: 11
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
start_utc: 2026-08-02T12:46:29Z
finish_utc: 2026-08-02T12:46:29Z
deterministic_executions: 1
gates: 10 of 10 PASS
```

The frozen verifier exited 0 and wrote no stderr.

## Required GitHub leg

```text
github_platform: Ubuntu 24.04
github_architecture: aarch64
github_python: Python 3.12.13
github_verifier_sha256: d062a009a98db0e1c26f1c95b2e3df04f04f14a79f68df4ec7784a9d8d40e163
github_stdout_sha256: 0609c48f3df68d79c0cea9fd38cbccaab14ad908590f00767a51322944a994cc
github_exit_code: 0
github_stderr_bytes: 0
github_status: PASS
github_verdict: VERIFY PASS
github_workflow_run_id: 30750743452
github_job_id: 91504236573
github_tested_head_commit: 59a55ecef8bb64e87f9eee97459ca0f9bc3cda89
```

The GitHub-hosted `ubuntu-24.04-arm` job checked the pinned verifier
hash, reran it in the deterministic environment, and reported
`VERIFY PASS` with stdout byte-identical to the committed
`EXPECTED.txt`. The local x86_64 leg and the GitHub aarch64 leg differ
in architecture and provide the byte-identity evidence required by
POLICY section 4. The paired x86_64 job of the same workflow run (job
`91504236569`) also reported `VERIFY PASS`, and aggregate job
`91504252562` reported `TWO-ARCHITECTURE CHECK PASS`.

Final `RESULT.md` ratification remains pending until a descendant
workflow validates this structured record as `TWO-ARCHITECTURE` and
passes its aggregate `check`.
