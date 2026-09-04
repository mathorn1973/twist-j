# P-RAPIDITY-TARGET-RECONSTRUCTION-1 formal run record

Status: local accepted formal record. Required public replay is a PR gate.

```text
pin_commit: aaf405e09179f7d0037041409a05f573d257b70c
base_commit: 935aaad0827aa6bc99cebd28acc97c271985ae80
pin_tree: a279909ae18802b400ca906123bd7eb9ada41b9d
public_lock: issue 817
public_readback_comment: https://github.com/mathorn1973/twist-j/issues/817#issuecomment-5547296292
prereg_sha256: fcce51f54fc011bf510c71dc7ac462dc62718778cd21e3b59196b1b705a2f1cb
prereg_bytes: 14920
prereg_lines: 349
prereg_blob: 70c6a0db127967e2f895168edc576d5bc46df0d1
verifier_sha256: 21118f5bdb63c201a863b585dd7816fb250fc97dd664d73e4870eb3fcb179e41
verifier_bytes: 15082
verifier_lines: 427
verifier_blob: ebc1990d83ff6501d4c72fe645e3cbb882d49d23
encoding: ASCII
line_endings: LF
final_lf: yes
public_readback: PASS
static_audit: PASS
preflight_command: env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
preflight_exit_code: 0
preflight_stdout_sha256: 6a35d478a26afbc04957801fbb8b5470693d3ee1f2093354dc03ea48c484ac17
preflight_stdout_bytes: 21
preflight_stderr_bytes: 0
command: python3 probes/P-RAPIDITY-TARGET-RECONSTRUCTION-1/verify.py
formal_invocation: /usr/bin/timeout --signal=TERM 600s /usr/bin/env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC /usr/bin/python3 probes/P-RAPIDITY-TARGET-RECONSTRUCTION-1/verify.py
external_timeout_seconds: 600
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.3
start_utc: 09/05/2026 00:46:30
finish_utc: 09/05/2026 00:46:30
elapsed_wall_seconds: 0.279446379000007
exit_code: 0
stdout_sha256: 61ef497e2f0d562913d9690ebedf50a03c294809b4ca931e0c4ccb9a8df5ad9e
stdout_bytes: 832
stdout_lines: 17
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
formal_execution_count: 1
pinned_files_unchanged_after_execution: yes
result: PASS
```

The remote pin and its sole parent, tree and both file blobs were read back
before execution. Remote raw bytes matched local SHA-256, byte and LF counts.
The clean Linux checkout was at that exact pin with no tracked or untracked
changes before and after execution. The same deterministic empty environment
passed startup preflight immediately before the formal invocation.

The accepted verifier ran once, exited zero and wrote empty stderr.
EXPECTED.txt is the exact 832-byte output, ending in VERIFY RESULT 8/8 ALL PASS.
Pinned files were rehashed unchanged afterward. Times above are UTC; the
local calendar date of the record is 2026-09-05. No hostname or machine
nickname is recorded.

Independent static proof and verifier reviews occurred before pinning.
The universal scope is carried by PREREG proofs; the finite audit is m<=16.
The existing required pull-request workflow must reproduce these exact
bytes independently on x86_64 and aarch64 before merge. Its outcome is
read from GitHub and is not predicted by this local record.
