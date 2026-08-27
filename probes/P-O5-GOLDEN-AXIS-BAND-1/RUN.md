# P-O5-GOLDEN-AXIS-BAND-1 formal run record

Status: local accepted formal record. Public two-architecture replay pending.

The flat fields below are the machine-readable local execution record.

```text
pin_commit: 0038e753efa7fe828eb3c1a7d3f332a96ea75524
verifier_sha256: 94c0ae4185fc9ca764d1cef64209ca922119a79f8140256c92783471db2d839c
command: python3 probes/P-O5-GOLDEN-AXIS-BAND-1/verify.py
platform: Linux
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: 697dc1a869c0fd34e35caedb41390668b256ff6476e5c2977ac91d792754aff9
stdout_bytes: 408
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin readback before execution

The accepted runtime surface was reconstructed only after public readback
showed that the pin is exactly one commit above basis
`c5d618f57099471bd9871c7918c3ba4da90f1a04`, changes exactly `PREREG.md`
and `verify.py`, and carries:

```text
PREREG blob:      b85b1c7eaa51f79ecbeec5689d5f69288fae01be
PREREG SHA256:    39aa156bae7efe1e4a13e30ccf65a838012142a0f14678f7190e1b18c006b399
PREREG bytes:     13401
verifier blob:    deafed25a03160fb3cbcb14dcfac1bf46dff1dce
verifier bytes:   11783
```

Both Git blob identities and SHA-256 values matched the local frozen copies.

## Clean startup preflight

Immediately before the scientific invocation, the frozen `/usr/bin/python3`
preflight returned zero, wrote exactly `PYTHON_STARTUP_CLEAN` plus LF, and
wrote zero stderr bytes.

```text
preflight_stdout_sha256: 6a35d478a26afbc04957801fbb8b5470693d3ee1f2093354dc03ea48c484ac17
preflight_stdout_bytes: 21
preflight_stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
preflight_stderr_bytes: 0
```

The one scientific invocation then completed once. `EXPECTED.txt` is its
complete LF stdout. No theorem, threshold, breaker witness, carrier,
`PREREG.md`, or verifier byte moved after the pin.

A terminal wrapper emitted a `TERM environment variable not set` diagnostic
after the scientific command had completed and after the captured files were
closed. It is not part of the verifier process streams:
`formal.stderr` is exactly zero bytes and has the empty SHA-256 above.
