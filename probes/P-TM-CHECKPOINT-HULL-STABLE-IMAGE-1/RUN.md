# P-TM-CHECKPOINT-HULL-STABLE-IMAGE-1 formal run record

```text
pin_commit: cdc7d3879a438f6a97228e22cde1e7919a4058ed
base_commit: 8c53ed0f1ab0ed60e10566cc4e3b5ae74334e0e9
pin_tree: a6f520beb51b0b84298e12ee9be746bebf397e81
public_lock: issue 780
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/780#issuecomment-5501211100

prereg_sha256: 0de0e55d02a274960f05316a22bbcf19302024e439fee61ccaacef079bb12006
prereg_bytes: 14955
prereg_lines: 454
prereg_blob: 6bfcd0f86dfacbcf8a22512acaf74c688329414b
verifier_sha256: d166b47b1e3c7f9ae517e04bf033c6c79a5f66f400eff88c241edd8c50805c74
verifier_bytes: 12775
verifier_lines: 463
verifier_blob: 727cf6ff2363fd8046f89069591b8d52fef02d78
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

command: python3 probes/P-TM-CHECKPOINT-HULL-STABLE-IMAGE-1/verify.py
formal_invocation: /usr/bin/timeout --signal=TERM 600s /usr/bin/env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC /usr/bin/python3 probes/P-TM-CHECKPOINT-HULL-STABLE-IMAGE-1/verify.py
environment: env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
external_timeout_seconds: 600
platform: Ubuntu 24.04
kernel: Linux
architecture: x86_64
python: Python 3.12.3
start_utc: 2026-09-01T22:21:42Z
finish_utc: 2026-09-01T22:21:44Z
elapsed_wall_seconds: 1.748156703
formal_execution_count: 1
exit_code: 0
stdout_sha256: 07e9abad023a504f256f45da3d21b647ccf830327dd4316fb28137b4ee232764
stdout_bytes: 946
stdout_lines: 16
stdout_final_lf: yes
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
frozen_stdout_byte_identity: PASS
result: PASS
pinned_files_unchanged_after_execution: yes
architecture_gate: PENDING
```

The immutable two-file public pin was fetched and read back before preflight
or execution. Git blob IDs, SHA-256 digests, byte and line counts, LF-only
encoding, final LF, and the accepted verifier's static integrity surface all
matched the reviewed bytes.

The preflight then completed with its exact 21-byte stdout and empty stderr.
The verifier was executed exactly once from the detached public pin under the
recorded deterministic environment and external timeout. It exited zero,
wrote empty stderr, and produced the exact bytes in `EXPECTED.txt`.

This is one local x86_64 formal leg. The required clean GitHub Python 3.12
x86_64 and aarch64 replays and aggregate `check` remain pending. No hostname,
machine nickname, private address, or internal fleet label is recorded.
