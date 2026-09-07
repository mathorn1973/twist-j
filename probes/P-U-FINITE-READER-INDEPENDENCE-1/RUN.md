# P-U-FINITE-READER-INDEPENDENCE-1 run record

pin_commit: 2289691ebfec40fcc370004f7f5164cfa23a1f54
verifier_sha256: 41e451143c2e7ba9f6f7a8b8edcda9b2a840560bdbd48af26a489c22c4a6712d
command: python3 probes/P-U-FINITE-READER-INDEPENDENCE-1/verify.py
platform: Ubuntu 22.04 (Linux-compatible WSL)
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: dab3f3faea009d9535452be96acaabebb974dfdd824fa49e96b7bd476b3db94d
stdout_bytes: 2267
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

Status: first local formal execution completed, 2026-09-07.
Public lock: [#890](https://github.com/mathorn1973/twist-j/issues/890).

## Public byte custody

All three accepted source files were committed and pushed before formal
execution. The GitHub contents API returned their bytes at the exact full
pin. Their SHA-256 values matched the accepted local files:

```text
PREREG.md 0dce3204b32abce188f85d159505485054c48d65b3626da90905587d332f596e
PROOF.md  b1cfb644b7ce3c48e1d9ca9a992c43c88227a840c2dbabb338f879c9cb1dd3a4
verify.py 41e451143c2e7ba9f6f7a8b8edcda9b2a840560bdbd48af26a489c22c4a6712d
```

The corresponding public Git blob identifiers were:

```text
PREREG.md cb49703280a1f5df6586d710091bfa22df53b0d7
PROOF.md  03edab3dc72a2035ab3baace3ba66abd890c4b56
verify.py f486c609f4836eca6d1b15a1d99866f896411e36
```

Preparation used static review and AST parsing only. No accepted verifier
was executed or imported before the immutable public pin and byte readback.

## Completed execution and required reproduction

The first formal run used Python 3.10.12, within the declared >=3.10 range,
on Linux-compatible WSL Ubuntu 22.04, x86_64. The launcher recorded exit 0,
empty stderr, and approximately 1.431 seconds of elapsed time. Duration is
audit metadata, not a scientific threshold.

The launcher checked all three accepted source hashes again immediately
before execution and used LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1, with a 600-second process ceiling.

The complete raw stdout was copied byte-for-byte into EXPECTED.txt, with no
normalization or editing. It is one LF-terminated JSON line, 2267 bytes,
reporting PROOF_AUDIT_PASS, an empty failures list and 384718 exact checks.
The accepted PREREG.md, PROOF.md and verify.py remain unchanged after pin.

This record describes only the successful first local run. Required GitHub
x86_64 and aarch64 reproduction is separate evidence on the review. Both
jobs must replay the same pinned verifier using Python 3.12 and match the
committed EXPECTED.txt exactly. The reviewed PR head and its actual CI
outcomes provide that separate evidence; this local record does not presume
their success. Universal statements rest on PROOF.md, not the finite ranges
or assertion count.
