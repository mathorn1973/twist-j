# P-TM-FOURPHASE-HULL-NONDESCENT-1 formal run record

```text
pin_commit: 1af329383c98c242539675060f792c7f36eb383b
base_commit: 8c53ed0f1ab0ed60e10566cc4e3b5ae74334e0e9
pin_tree: 1de9d67101ac28b8905923d14807dbb108c3501a
public_lock: issue 781
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/781#issuecomment-5501210840

prereg_sha256: df9135e6a88c64c4412188afea156bd7654f4a3dfc3cd348307f4af2c324759b
prereg_bytes: 16327
prereg_lines: 434
prereg_blob: 307237d85f40bf1edc05544f169a7d27bd1f1623
verifier_sha256: 59840bfb1437cb4bb68423072ca7fd4bb8e54d99fb933facdc2ace260c5dddb0
verifier_bytes: 9201
verifier_lines: 341
verifier_blob: d4c4cdf418a599a9e6cb70752a4ea8a24f330ab8
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

command: python3 probes/P-TM-FOURPHASE-HULL-NONDESCENT-1/verify.py
formal_invocation: /usr/bin/timeout --signal=TERM 600s /usr/bin/env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC /usr/bin/python3 probes/P-TM-FOURPHASE-HULL-NONDESCENT-1/verify.py
environment: env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
external_timeout_seconds: 600
platform: Ubuntu 24.04
kernel: Linux
architecture: x86_64
python: Python 3.12.3
start_utc: 2026-09-01T22:21:42Z
finish_utc: 2026-09-01T22:21:43Z
elapsed_wall_seconds: 0.63803499
formal_execution_count: 1
exit_code: 0
stdout_sha256: 2e01952c3e5c6716e13f4269067bc2780f02a33463553517d8fbdbadc6300c59
stdout_bytes: 705
stdout_lines: 7
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
encoding, final LF, and the static verifier surface matched the reviewed
bytes.

The preflight produced its exact 21-byte stdout with empty stderr. The
verifier was then executed exactly once from the detached public pin. It
exited zero, wrote empty stderr, and produced the exact bytes in
`EXPECTED.txt`.

This is one local x86_64 formal leg. Clean GitHub Python 3.12 x86_64 and
aarch64 replays and aggregate `check` remain pending. No private machine
identifier is recorded.
