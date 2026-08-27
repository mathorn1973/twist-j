# P-O5-FIRST-MISSING-SHELL-1 formal run record

Status: local accepted formal record. Public two-architecture replay pending.

The flat fields below are the machine-readable local execution record.

```text
pin_commit: b9ac3f52c28d06293d27dcd2fb1ca7338ad68b0e
verifier_sha256: 3fd20a130eb38d093815116bfd8c5a5b771b9dcd2298ece6492752a9d7beb256
command: python3 probes/P-O5-FIRST-MISSING-SHELL-1/verify.py
platform: Linux
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: bd89fd430dfdee0f5d508cfa51e1b92ecef32a70611d1da9909acd3ea03cbd96
stdout_bytes: 348
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin readback before execution

The accepted runtime surface was reconstructed only after public readback showed that the pinned verifier has Git blob `ab9b2afec7621234e3aa177a5500f85588451d0b`, SHA-256 `3fd20a130eb38d093815116bfd8c5a5b771b9dcd2298ece6492752a9d7beb256`, and 12269 bytes, identical to the local execution copy. The pin is exactly one commit ahead of basis `258fbdf9f9e2f3289d806b92c00625e50b200b8a` and adds exactly `PREREG.md` and `verify.py`.

## Clean startup preflight

Immediately before the scientific invocation, the frozen `/usr/bin/python3` preflight returned zero, wrote exactly `PYTHON_STARTUP_CLEAN` plus LF, and wrote zero stderr bytes. Its stdout was 21 bytes. No verifier import or execution occurred before the public pin.

The one scientific invocation then completed once. `EXPECTED.txt` is its complete LF stdout. No threshold, witness, carrier, equation, `PREREG.md`, or verifier byte moved after the pin.
