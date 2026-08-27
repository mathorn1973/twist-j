# P-O5-FIRST-SHELL-DILATION-TRANSFER-1 formal run record

Date: 2026-08-27.

Status: local accepted formal record. The public two-architecture gate is
pending the pull-request workflow, which must replay the unchanged pinned
verifier on x86_64 and aarch64 and compare stdout byte for byte with the one
committed `EXPECTED.txt`.

```text
pin_commit: 32aa778b7c08fe50946b14e89b16f0a6219c2b49
verifier_sha256: b004c4f6adbbd14224bb4101ba975ac91d7cebc8325b148667ad05b35e8f95d9
command: python3 probes/P-O5-FIRST-SHELL-DILATION-TRANSFER-1/verify.py
platform: Linux
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: e102f9de3ea7d1d2f7f1f1927983af70107f46ee871874c0447eb32d55526c99
stdout_bytes: 368
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Public pin readback before execution

```text
basis main:       0612f5edec662eedb428e8a0d6bd77437f9579ac
pin tree:         4b3804e517acfdac4fb8c00a74adf8dd5ebdbb24
PREREG blob:      ff2a4f07a62db94d8cf90a0bf7c3b100b9c6fd85
PREREG SHA256:    ac8e3ef2370f15ae8a243606cf4817a68526e6944e78d3be5ddb175c971a8138
PREREG bytes:     11725
verifier blob:    454667a223a1f4175ff9cfdb1b5a72be47f325e2
verifier bytes:   10284
```

The pin has exactly one parent, the declared basis, and exactly two changed
files. Before the pin, both server blobs matched the local `git hash-object`
identities. Public post-pin readback matched both blob identities and byte
counts. Neither pinned file changed after the pin.

The accepted runtime surface was reconstructed from those byte-identical
pinned files. Before the pin, `verify.py` was read and AST-parsed only; it was
not imported or executed.

## Clean startup preflight

```text
preflight_command: env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
preflight_exit_code: 0
preflight_stdout_sha256: 6a35d478a26afbc04957801fbb8b5470693d3ee1f2093354dc03ea48c484ac17
preflight_stdout_bytes: 21
preflight_stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
preflight_stderr_bytes: 0
```

The preflight passed immediately before the single accepted scientific
execution. `EXPECTED.txt` is the complete LF stdout. No threshold, witness,
pinned byte, carrier or theorem moved after the pin.
