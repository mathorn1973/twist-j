# P-QDD-DIRECT-RECORD-E-NONCONGRUENCE-1 formal run record

```text
pin_commit: 4b064159570107746812d1d5ebcdbd6d8593fe10
base_commit: 8c53ed0f1ab0ed60e10566cc4e3b5ae74334e0e9
pin_tree: 8cb4d1ef82a0688d33623c2bbdb5386e410c11c8
public_lock: issue 782
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/782#issuecomment-5501210979

prereg_sha256: 22f6203938d56819bd175af4ce3458d7f51f13ec5180d3f0fc88ec4c7f8401bf
prereg_bytes: 12860
prereg_lines: 371
prereg_blob: 41e968ca1da2c88ab8c3d871a87bc91606e4eece
verifier_sha256: 00bef39293ce531f3e9e72ea4389ab1e47a9a4ca8565347f1d1f1ac227a35a90
verifier_bytes: 9403
verifier_lines: 306
verifier_blob: 59f4183b24dc272375b7b25e8ccbf63b8b7fe4d9
encoding: UTF-8
line_endings: LF
final_lf: yes
public_readback: PASS
static_audit: PASS

preflight_command: env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
preflight_exit_code: 0
preflight_stdout_sha256: 6a35d478a26afbc04957801fbb8b5470693d3ee1f2093354dc03ea48c484ac17
preflight_stdout_bytes: 21
preflight_stdout_lines: 1
preflight_stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
preflight_stderr_bytes: 0

command: python3 probes/P-QDD-DIRECT-RECORD-E-NONCONGRUENCE-1/verify.py
formal_invocation: /usr/bin/timeout --signal=TERM 600s /usr/bin/env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC /usr/bin/python3 probes/P-QDD-DIRECT-RECORD-E-NONCONGRUENCE-1/verify.py
environment: env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
external_timeout_seconds: 600
platform: Ubuntu 24.04
kernel: Linux
architecture: x86_64
python: Python 3.12.3
start_utc: 2026-09-01T22:21:42Z
finish_utc: 2026-09-01T22:21:43Z
elapsed_wall_seconds: 0.346978022
formal_execution_count: 1
exit_code: 0
stdout_sha256: c15f312833df9ce38e6b2aa724045afd08be3e0c720691769891fcdfa4428054
stdout_bytes: 532
stdout_lines: 8
stdout_final_lf: yes
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
frozen_stdout_byte_identity: PASS
result: PASS
pinned_files_unchanged_after_execution: yes
architecture_gate: PENDING
```

The two-file public pin was fetched and read back before preflight or
execution. Git blob IDs, SHA-256 digests, byte and line counts, LF-only
encoding, final LF, and the verifier's static integrity surface matched the
reviewed bytes.

The preflight produced the exact 21-byte stdout with empty stderr. The
accepted verifier then ran exactly once from the detached public pin. It
exited zero, wrote empty stderr, and produced the exact bytes in
`EXPECTED.txt`.

This is one local x86_64 formal leg. Clean GitHub Python 3.12 x86_64 and
aarch64 replays and aggregate `check` remain pending. No private machine
identifier is recorded.
