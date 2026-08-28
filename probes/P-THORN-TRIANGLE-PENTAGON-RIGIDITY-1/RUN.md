# Run record

Probe: `P-THORN-TRIANGLE-PENTAGON-RIGIDITY-1`

The flat fields below are the machine-readable local record required by
`tools/check_verifier.py`.

```text
pin_commit: df66bcb7230a03898ef0a97273c51370400d3d39
verifier_sha256: 543c02726e7dbbc319a3cce12cf90db7fc89c97d7be1379d7e31691e9b8ca04b
command: python3 probes/P-THORN-TRIANGLE-PENTAGON-RIGIDITY-1/verify.py
platform: Linux
architecture: x86_64
python: Python 3.13.5
exit_code: 0
stdout_sha256: 5a0b5f8b1f76cfdb612bcaf7b0c31c685c994e450dd863c38f76636529bcf500
stdout_bytes: 471
stdout_lines: 13
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
prereg_sha256: f68e1a4dacb6a8efeeff4f6e8db28ccf40f10726aa178db948c0f081923a3ead
prereg_bytes: 10805
prereg_lines: 354
prereg_blob_sha1: 7fca81fcf814381ebf28bde00327545043725879
verify_bytes: 12436
verify_lines: 429
verify_blob_sha1: b0b23f423868810c2998d6397e701555248bd382
expected_sha256: 5a0b5f8b1f76cfdb612bcaf7b0c31c685c994e450dd863c38f76636529bcf500
public_claim_lock: issue 630
formal_date: 2026-08-28
```

The public remote readback at the full pin commit returned both frozen blobs
byte-identical to the local files. Both use LF-only line endings and end in a
final LF. Static compilation occurred before the pin; the accepted verifier
was not imported or executed before the pin. The first formal execution
occurred only after remote readback.

The first execution used the same pinned bytes through an isolated-interpreter
wrapper with bytecode disabled. After the repository checker required the
canonical command spelling in the flat record, the verifier was reproduced
from a repository-shaped working directory using exactly the command printed
above. Both executions exited zero, wrote empty stderr, and produced the same
committed stdout SHA-256 and the same 471 bytes in 13 LF-terminated lines.
`EXPECTED.txt` is those complete raw stdout bytes. The second execution is a
reproduction only and adds no independent evidential credit.

The local executions are one x86_64 lane. They are not a two-architecture
computation gate. The proposed theorem status is proof-first from
`PREREG.md`; the exact verifier is its audit. The pull-request workflow must
still reproduce the committed bytes independently on x86_64 and aarch64 and
pass aggregate `check`.
