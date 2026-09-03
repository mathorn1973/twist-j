# P-RAPIDITY-GOLDEN-LADDER-1 formal run record

Status: local accepted formal record. Public two-architecture replay pending.

The flat fields below are the machine-readable local execution record.

```text
pin_commit: 4cf730fea17561e3c8fb78db51ec0858fc7c256f
base_commit: 4f08791bd5401ee1616270661f7788d743f5fc26
pin_tree: ab72a088360752c7139ce72e72e103ab96975909
public_lock: issue 791
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/791#issuecomment-5523609707

prereg_sha256: 240c89da20d29c38bcfa5634d8e87b9734f81574c23d9ead4ce0d547e17c548e
prereg_bytes: 30094
prereg_lines: 407
prereg_blob: cdc789f1e6c7ba62497d4895ef498fdb31098319
verifier_sha256: d501dd73cbb870fe296ec31472ff6de1cdfc963d3016f8351430b5630b1fae04
verifier_bytes: 17495
verifier_lines: 477
verifier_blob: e2673f21c0e7e84acf5e664bf1d72e028f5ce26b
encoding: ASCII
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

command: python3 probes/P-RAPIDITY-GOLDEN-LADDER-1/verify.py
formal_invocation: /usr/bin/timeout --signal=TERM 600s /usr/bin/env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC /usr/bin/python3 probes/P-RAPIDITY-GOLDEN-LADDER-1/verify.py
environment: env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
external_timeout_seconds: 600
platform: Ubuntu 24.04
kernel: Linux
architecture: x86_64
python: Python 3.11.15
start_utc: 2026-09-03T09:29:13Z
finish_utc: 2026-09-03T09:29:14Z
elapsed_wall_seconds: 0.985227172
formal_execution_count: 1
exit_code: 0
stdout_sha256: b1ea5b711ad0f6a167cbbd8e53e34bc598364c07685e8009889afc46350e6a2a
stdout_bytes: 1653
stdout_lines: 34
stdout_final_lf: yes
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
frozen_stdout_byte_identity: PASS
result: PASS
pinned_files_unchanged_after_execution: yes
architecture_gate: PENDING
```

## Pin readback before execution

The immutable two-file public pin was pushed and read back through the
public connector before preflight or execution. The pin has exactly one
parent, the declared post-#595 Public Canon v75 basis, and adds exactly
`PREREG.md` and `verify.py` under the one probe directory. The remote Git
blob identities, SHA-256 digests, byte and line counts, ASCII encoding,
LF-only line endings, and final LF all matched the frozen local bytes, and
the remote verifier content was byte-identical to the local copy.

## Clean startup preflight

Immediately before the scientific invocation, the frozen `/usr/bin/python3`
preflight was executed with an empty environment except for the recorded
variables. It exited zero, wrote exactly `PYTHON_STARTUP_CLEAN` plus LF
(21 bytes, SHA-256 above), and wrote zero stderr bytes.

## Accepted formal invocation

The verifier was then executed exactly once from the pinned checkout at the
repository root, under the recorded deterministic environment and external
timeout. It exited zero, wrote empty stderr, and produced the exact bytes in
`EXPECTED.txt`, whose final line is `VERIFY RESULT 11/11 ALL PASS`. The
pinned `PREREG.md` and `verify.py` were re-hashed after execution and were
unchanged. No theorem, threshold, breaker witness, carrier, or pinned byte
moved after the pin.

This is one local x86_64 formal leg. The required clean GitHub Python 3.12
x86_64 and aarch64 replays and the aggregate `check` remain pending. No
hostname, machine nickname, private address, or internal fleet label is
recorded.
