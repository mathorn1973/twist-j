# P-CM-ALTERNATING-PENCIL-1 formal run record

The preregistration and verifier were committed, pushed, and read back from
the public branch before execution. The local formal leg below invoked the
pinned verifier exactly once from a fresh clean detached checkout. The
pull-request architecture gate is pending.

pin_commit: 71717975810c805b886eebc9d045c868adab92af
base_commit: 686d0d5b4c7dde882483ef0c547ec03166ae8e29
prereg_sha256: 69c4204d110ebff232e42c96a739f48ddb9548b49b2fa315cc69f7451488956f
prereg_bytes: 18432
prereg_git_blob: 1cd7ed54aefe6f7606dd38af1bc6a5b068efbe7a
verifier_sha256: 19cdff86cc90de099a96088b39818956022fbd36d0ce48a0e2c2a3f9747e4b78
verifier_bytes: 21353
verifier_git_blob: fbc6bb99b3a82d33d51be4ef487d393ddd845be0
command: python3 probes/P-CM-ALTERNATING-PENCIL-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: macOS 26
architecture: aarch64
python: CPython major 3 minor 13 patch 13
compatibility_basis: standard-library CPython with a portable process environment and no system-dependent verifier operations
run_started_utc: 2026-08-06T10:04:37Z
run_finished_utc: 2026-08-06T10:04:38Z
pre_run_clean: yes
post_run_clean: yes
deterministic_executions: 1
exit_code: 0
stdout_sha256: 5f790488d58802bdf467c7269e967e82a08e7b8f0f1b51a8736789c04384cdfd
stdout_bytes: 1940
stdout_lines: 35
stdout_cr_bytes: 0
stdout_final_byte: 0a
stdout_git_blob: 72cd2d20c1fb7cc0823a15b2d775e5c84fad5ed4
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
result: 34/34 ALL PASS
architecture_gate: pending; the required GitHub Linux x86_64 and aarch64 jobs must reproduce EXPECTED.txt byte for byte
public_lock: issue 281
public_pin_comment: 5203129262
public_run_return: 5203197908

## Integrity notes

`EXPECTED.txt` is the exact raw standard output from the one formal local
execution. It is LF-only, contains all 35 lines, ends in LF, and has the hash
and byte count recorded above. Standard error is the exact empty byte string.

The local host has no Linux virtual runtime. This pure standard-library
verifier used native aarch64 CPython in a portable process environment. The
required workflow supplies clean Linux aarch64 and Linux x86_64 executions,
and its full-byte comparisons are required before the architecture gate can
pass. No conclusion relies on a machine name or on an operating-system-specific
operation.
