# RUN P-CM-2I-QCARRIER-1

## Immutable pin

```text
pin_commit: c223955229239858913c554bd5d6149d352d0472
prereg_sha256: 56f59ca02ae81d2efc6ccb2e13998ca189d857c6794d6441844473cd97401c52
prereg_bytes: 18566
prereg_blob: 5bc1bc76e37a6cd03ab33dbb17d2bd74e97bb1e7
verifier_sha256: d031470193a1e6035769c64c75c5ab98e4e4f381af2dbdf6307d81f8e33c100f
verifier_bytes: 17503
verifier_blob: b8ef5a875f0d3b1fcdda453c38c61482aec7360c
```

Issue #245 was opened before the branch, path, pin, or formal
execution. The branch started from public `main` commit
`a2198c477898963a815a09c34b8bb45c40d4a7b9`. The commit above is the
immutable preregistration pin containing exactly `PREREG.md` and
`verify.py` relative to the branch base; it was pushed to the public
branch before the first formal execution. The byte counts, SHA-256
values, and Git blob identities above were recorded from the pushed
pin before execution.

## Command

```text
command: python3 probes/P-CM-2I-QCARRIER-1/verify.py
```

Executed once from the repository root in the deterministic
environment `LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0 TZ=UTC`. The exact raw stdout is `EXPECTED.txt`.

## Local formal execution

```text
platform: Ubuntu 24.04
architecture: x86_64
python: Python 3.12.3
exit_code: 0
stdout_sha256: 138cda2609bd712089ac550e508830d6bd42efe33fde39d0a01ed2badbd2fd86
stdout_bytes: 1483
stdout_lines: 20
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
finish_utc: 2026-08-02T07:12:45Z
deterministic_executions: 1
gates: 19 of 19 PASS
```

The frozen verifier process exited 0 and wrote no stderr. This section
records the single local formal leg on one architecture; the required
GitHub architecture jobs run on the pull request and their record is
appended after they complete.
