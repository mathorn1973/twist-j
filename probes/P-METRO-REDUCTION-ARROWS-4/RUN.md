# RUN P-METRO-REDUCTION-ARROWS-4

## Immutable pin

```text
pin_commit: 563d733ec1f6691f01ec099c5a3e49ef9c00d649
prereg_sha256: 8edaaa5d509566a332dc599fc34d9ddb2a331b1f41f52d2cbfc7007dffa67692
prereg_bytes: 9764
prereg_blob: cbbf83f79e5d0ab4ff729438045bf08eecca73f3
verifier_sha256: db9e4c4911dd7237cbd2a685b8f8ce1c6d84679d0842fa1186feb61cd5779a6f
verifier_bytes: 20761
verifier_blob: 73f6b20fa10cb6f3e2d6e4edbcf7f819e73742bc
```

GitHub public readback matched the full pin commit, both blob identities, and
both byte counts before execution.

## Command

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-METRO-REDUCTION-ARROWS-4/verify.py
```

Machine-readable command field:

```text
command: python3 probes/P-METRO-REDUCTION-ARROWS-4/verify.py
```

## Local formal leg

```text
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: Python 3.13.5
start_utc: 2026-07-28T05:47:50.973897748Z
finish_utc: 2026-07-28T05:48:21.582662138Z
wall_ns: 30605213044
wall_seconds: 30.605213044
deterministic_executions: 1
pre_status_bytes: 0
post_status_bytes: 0
exit_code: 0
stdout_sha256: c0e4b5685b86799937e905b4cd6c55513c8c368c083587d6af7ddfb5bd3ac2d7
stdout_bytes: 2539
stdout_lines: 29
stdout_cr: 0
stdout_final_byte: 10
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
gates: 17 of 17 OK
verdict: ALL PASS
```

The checkout was clean immediately before and after the one execution.
`EXPECTED.txt` is the exact raw stdout, with LF line endings and a final LF.
Stderr was empty.

## Required GitHub leg

```text
status: PENDING
required_architecture: x86_64
required_identity: same pin_commit and verifier_sha256
required_stdout_sha256: c0e4b5685b86799937e905b4cd6c55513c8c368c083587d6af7ddfb5bd3ac2d7
```

Both local and required GitHub legs are x86_64. Byte identity therefore
establishes reproduction only; a computation-only conclusion remains at
most C. No L6 decision or normalization lift is claimed.
