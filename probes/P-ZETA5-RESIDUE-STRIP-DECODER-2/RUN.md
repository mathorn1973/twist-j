# Run record: P-ZETA5-RESIDUE-STRIP-DECODER-2

Status: completed first formal local execution. This record does not by itself
satisfy the public two-architecture computation gate.

The flat fields below are the machine-readable record required by
tools/check_verifier.py.

```text
pin_commit: 7f993b5f6375a1d97d705a0bcb42eab12a8dddc8
verifier_sha256: 57dfd43f717f008feff825698e2eddb5a5995086bebe2f8c66e2bc1327e5b7da
command: python3 probes/P-ZETA5-RESIDUE-STRIP-DECODER-2/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: 54d5a041141c7e7e50508dca1f286ca5414c9bb3be3bb9991f8ff9456e92bbd2
stdout_bytes: 962
stdout_lines: 14
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
```

## Pin audit

```text
PREREG sha256: 8b89a068ae2c2831f23614e8872a46c7dabe76ba5e69a568110d441439ae0b43
PREREG bytes: 7254
PREREG blob: e6d0d09888b6c2bcdcfa6e83c063793715e8e69a
PROOF sha256: 16001f3c557569474772a4064df28d993063757f3fd1c1d3f6a8105e6b950ea3
PROOF bytes: 8852
PROOF blob: 4bd134d3c86e2f8be5efaa39e659207423e63f5c
verify bytes: 6877
verify blob: 3e352a97f8c85a8f9fe75a1215eda160d655dab9
```

All three frozen files were first created as unreferenced Git blobs, fetched
back and compared byte for byte with the prepared sources, then assembled into
the immutable pin commit. Public readback at the pin matched the same blobs and
SHA-256 values before execution.

Before the formal run, the local verifier had exactly the pinned Git blob and
SHA-256 and passed Python compilation.

## Accepted local run

The first completed formal run exited zero with empty stderr and printed
12/12 ALL PASS. EXPECTED.txt is the exact accepted stdout and has the byte
count, line count and SHA-256 above.

No frozen source, scientific equation, threshold, carrier or falsifier changed
after the pin.

## Pull-request integrity note

The first pull-request workflow attempt failed before any probe verifier was
executed because the initial prose RUN.md lacked the mandatory flat
check_verifier fields. That is an integrity-record defect only. This revision
adds exactly the required machine-readable fields from the already completed
local run. It does not alter PREREG.md, PROOF.md, verify.py, EXPECTED.txt,
RESULT.md, any scientific output, or any threshold.

The required GitHub x86_64 and aarch64 jobs must now replay the unchanged
pinned verifier against the unchanged EXPECTED.txt byte for byte.
