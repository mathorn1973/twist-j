# P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-2 run record

Status: **FIRST ADMISSIBLE FORMAL EXECUTION COMPLETE. LOCAL x86_64 REPRODUCTION ONLY. PUBLIC TWO-ARCHITECTURE GATE PENDING.**
Mode: **RESULT-EXPOSED / EVIDENCE-MAINTENANCE.**

The flat machine-readable fields required by `tools/check_verifier.py` are:

```text
pin_commit: 1c087b13b14986223f7f69453223c2b96100f6ca
verifier_sha256: a2892613f257476a5c823bda76f7487fc74d7a881b408ddee0f3ca01c1316f34
command: python3 probes/P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-2/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: e6a336af19dbb17d3388f229b568c675d6f9293e0bf929f96f6b6022942f00d4
stdout_bytes: 609
stdout_lines: 16
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Audit context:

```text
claim lock:       issue #543
branch:           probe/P-J-ODD-MOTOR-MEDIATED-BRIDGE-COVERAGE-2
base commit:      9d384ecc8c539433936df995fd94d4016c01e6e7
formal run count: 1
stdout final LF:  yes
```

## Immutable pin and source readback

Before execution the accepted coverage verifier was fetched from the exact public pin.
Its Git blob and SHA-256 agreed with the local file. The two frozen predecessor sources
were reconstructed from their public Git blobs and also matched both Git blob and
SHA-256 before Python was invoked.

```text
PREREG.md
  Git blob:       befc07c0b48a93dbcc86c040b7e3f9ee769f5385
  SHA-256:        b4fdac041ae0a6712640152fe951e6d37ffa136f3bd963075b3c7fb6cddd2788

verify.py
  Git blob:       26ea302a6e65f0f279ef2c00a7ce7c44ebcf5ba5
  SHA-256:        a2892613f257476a5c823bda76f7487fc74d7a881b408ddee0f3ca01c1316f34

original source
  Git blob:       475e17e347b66cf8e0328b47a1976753e5456c70
  SHA-256:        78b5ae47fbede9449e0a7c706dc12e00661a0d3d63227c57ee6a35de84f3ef42

hardening source
  Git blob:       92219129a08fa0a5795715ae4ab6e358100dc888
  SHA-256:        682e1ccdbdc61597d9c08d594c9ea8a9c56b9364e419bc0c0e893c908977c2c8
```

The predecessor `COVERAGE-1` run is not evidence. This is the first admissible formal
execution of this successor. The coverage decision does not consume `h3_ok`, the
survivor list, box count or hardening final verdict.

This local run does not satisfy the public two-architecture gate by itself. The pull
request workflow must reproduce this exact `EXPECTED.txt` byte for byte on x86_64 and
aarch64 with the same verifier SHA-256.
