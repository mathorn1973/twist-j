# P-O5-FIRST-SHELL-BILINEAR-SQUARE-1 formal run record

Status: local accepted formal record. Public two-architecture replay pending.

The flat fields below are the machine-readable local execution record.

```text
pin_commit: 7af861ebd5e2f06a8f75624a2e4bc80e19f01883
verifier_sha256: 857dba6fa4a152ac5a57749875d9bdc3c293e8fd3028ce86377356178179bd5a
command: python3 probes/P-O5-FIRST-SHELL-BILINEAR-SQUARE-1/verify.py
platform: Linux
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: fa0db49ae054064f0fd6071cb8c773932a6e029bd5982fbc2f2d170696315488
stdout_bytes: 362
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin readback before execution

The accepted runtime surface was reconstructed only after public readback
showed that the pinned verifier has Git blob
`5929a95a8e424276d1171950a814f72b6157a8f5`, SHA-256
`857dba6fa4a152ac5a57749875d9bdc3c293e8fd3028ce86377356178179bd5a`,
and 13657 bytes, identical to the local execution copy. The pinned
`PREREG.md` has Git blob `b50d33c3db71b04e85358cd3769bea5170a636c5`,
SHA-256 `95d3178c1d14728e684b73e6f79117e89d8201a2563a78fc049027bbb379b2b5`,
and 11106 bytes. The pin is exactly one commit ahead of basis
`ed15b8e526cece98a407c7587d61f2e084267f86` and adds exactly `PREREG.md`
and `verify.py`.

A manually transported unattached base64 blob was rejected before the pin
because its Git identity did not match the frozen preregistration and its bytes
were not valid UTF-8. It was never attached to the formal branch. The two
server blobs actually used by the pin were materialized independently on a
non-formal prep ref, matched local `git hash-object` identities exactly, and
the prep ref was reset to `main` before the public pin.

## Clean startup preflight

Immediately before the scientific invocation, the frozen `/usr/bin/python3`
preflight returned zero, wrote exactly `PYTHON_STARTUP_CLEAN` plus LF, and
wrote zero stderr bytes. Its stdout was 21 bytes with SHA-256
`6a35d478a26afbc04957801fbb8b5470693d3ee1f2093354dc03ea48c484ac17`.
No verifier import or execution occurred before the public pin.

The one scientific Python process then completed once with exit zero and zero
captured stderr. `EXPECTED.txt` is its complete 362-byte LF stdout. No
threshold, witness, carrier, equation, `PREREG.md`, or verifier byte moved
after the pin.
