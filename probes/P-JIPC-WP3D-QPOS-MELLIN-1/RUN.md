# P-JIPC-WP3D-QPOS-MELLIN-1 formal run record

```text
pin_commit: 0c6b35731953398374fcb5072787d2a7b93c383a
base_commit: 1cf954b4c7f9fed1b3ad1cd724b493714369de37
pin_tree: 6fcf5e80606557723f0ab9d15b2bed9f34c9cd74
public_lock: issue 777
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/777#issuecomment-5500718953

prereg_sha256: c8c4cbaa1bae2b2270d2ca046f16b0fdc0514456514f6a2205ecaf761b93b3fc
prereg_bytes: 40116
prereg_lines: 911
prereg_blob: 11196520ce7a245cd29cbaf7e00d8d3903683cd0
verifier_sha256: 238e587f1343e7fef07505e9bd6c8f75c9edf6a1efdeb98989f35ee5285151c0
verifier_bytes: 23903
verifier_lines: 671
verifier_blob: 34ed1400bb87c30bdc18e57e1ec4fdb7302b1ede
encoding: UTF-8
line_endings: LF
final_lf: yes
public_readback: PASS
static_audit: PASS

preflight_command: env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
preflight_exit_code: 0
preflight_stdout_sha256: 6a35d478a26afbc04957801fbb8b5470693d3ee1f2093354dc03ea48c484ac17
preflight_stdout_bytes: 21
preflight_stdout_lines: 1
preflight_stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
preflight_stderr_bytes: 0

command: python3 probes/P-JIPC-WP3D-QPOS-MELLIN-1/verify.py
formal_invocation: /usr/bin/timeout --signal=TERM 600s /usr/bin/env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC /usr/bin/python3 probes/P-JIPC-WP3D-QPOS-MELLIN-1/verify.py
environment: env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC
external_timeout_seconds: 600
platform: Ubuntu 24.04
kernel: Linux
architecture: x86_64
python: Python 3.12.3
start_utc: 2026-09-01T21:33:11Z
finish_utc: 2026-09-01T21:33:12Z
elapsed_wall_seconds: 0.036739486
formal_execution_count: 1
exit_code: 0
stdout_sha256: f0a46170e5a8958fb953ab782a00353720ae7178fdc461dd8a189ca06683f554
stdout_bytes: 365
stdout_lines: 10
stdout_final_lf: yes
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
frozen_stdout_byte_identity: PASS
result: PASS
pinned_files_unchanged_after_execution: yes
architecture_gate: PENDING
```

The immutable two-file pin was pushed and read back by its full public commit
before preflight or execution. Its sole parent, tree, Git blobs, SHA-256
digests, byte counts, LF-only encoding and final LF were checked, and FZ7 was
repeated on the read-back verifier. The static audit found the one frozen
`Fraction as Fr` import, zero `ast.Div` nodes, zero float or complex literals
and no forbidden dynamic, file, subprocess, network or input calls.

The preflight then produced exactly `PYTHON_STARTUP_CLEAN` plus LF with empty
stderr. The accepted verifier was executed exactly once from the public pin
under the recorded deterministic environment and external 600-second timeout.
It exited zero, wrote empty stderr, and its complete stdout is byte-identical
to both the frozen block in `PREREG.md` and `EXPECTED.txt`. The pinned
`PREREG.md` and `verify.py` remained unchanged.

This is one local x86_64 formal leg. The required clean GitHub Python 3.12
x86_64 and aarch64 replays and aggregate `check` remain the public
architecture gate. The first workflow attempt and its pre-replay stop are
recorded below; no architecture replay has completed. No hostname, machine
nickname, private address or fleet label is recorded.

## Command-field normalization

The first public workflow, run `33562354298`, stopped in
`check_verifier.py` before either architecture executed this verifier. The
checker requires the portable repository command shown in `command`; the
initial record had placed the deterministic environment wrapper in that field
and recorded the timeout separately. This metadata correction uses the
required portable spelling for clean public replays and preserves the exact
combined environment-and-timeout wrapper in `formal_invocation`. No verifier
was rerun, no scientific output was regenerated, and `PREREG.md`, `verify.py`,
and `EXPECTED.txt` are unchanged.
