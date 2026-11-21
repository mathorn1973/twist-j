# First completed native fixed-read audit

pin_commit: 67fde06d2aec8cead7a0bf1bad3988e65c486cdb
verifier_sha256: c3f6c7edaec92097cecb96a5c893fed2b6517daf9a17e9822c17b13d9816bf28
command: python3 probes/P-U-NATIVE-FIXED-READ-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: 1e44ca65502810c43914b99bdf77ba35840309f2a54a217e9a4cc035e507e0cc
stdout_bytes: 2226
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

started_utc: 2026-10-09T09:54:42.226649+00:00
completed_utc: 2026-10-09T09:54:42.595136+00:00
public_input_readback_utc: 2026-10-09 09:53:37 UTC

## Pin and exact input custody

The complete nine-file pre-run tree was committed as A. M. Thorn
<thorn@twistj.com>, pushed, and independently fetched from public GitHub
before this first scientific execution. Each fetched file was compared
byte for byte with its reviewed local UTF-8 bytes. All nine matched.
The committed Git blobs also matched those bytes.

- PREREG.md SHA-256:
  4689fec64bf2840e97b456388e4c2369e3cd3df9e1c77fd0ac76336ddccd13e8
- INPUTS.sha256 SHA-256:
  9b1431821269382fe20287d2aa2d9456e5d56dadba206b743ca063e149ad26d0
- Primary scientific source SHA-256:
  9451b6de1c8d45d5c9689f09641e1fc107a8f7ad533389cba59c0662340bc1df
- Independent matrix source SHA-256:
  19d689280aeaff21f0deb67e3d0676bb85d1ce2fc94d09e315be6bc8f1293953

INPUTS.sha256 binds all eight accepted input files, including both
analytic appendices, the review and the wrapper. Its own bytes are bound
by the pinned Git tree. The complete input hashes were checked before
the run and unchanged afterward.

## Actual execution

The command above ran from the repository root on the clean pinned tree.
The wrapper invoked the two separately authored scientific programs in
isolated Python subprocesses. The launch used LC_ALL=C, LANG=C,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and TZ=UTC.

This was the first execution of both new scientific programs. No program
was repaired, no threshold moved and no input changed after the pin.
Both programs exited zero, wrote no stderr and reported PASS. Their
complete twenty-template lists, four selected codes, common finite-domain
counts and explicit counterexamples agreed. The wrapper emitted the actual
2226-byte single-line report now committed as EXPECTED.txt.

Exact parent stdout/stderr and the administrative run receipt were retained
from this execution. EXPECTED.txt is copied from that actual stdout,
not reconstructed from anticipated answers. The empty stderr has the
standard empty-file SHA-256 above.

## Limits and public replay

This record is one local x86_64 execution under Python 3.10.12. The
repository's unchanged required workflow separately reruns the accepted
wrapper under Python 3.12 on clean x86_64 and aarch64 jobs, using the same
EXPECTED.txt and verifier hash. Their live PR checks supply the architecture
gate; this local record does not claim that they had already run.

The all-time and varying-trace theorems are separately reviewed written
proofs. The finite program does not enumerate all durations or nonlinear
preparation functions. A passing exact audit is not a physical apparatus
test, an energetic calibration or completion of the full physical bridge.
