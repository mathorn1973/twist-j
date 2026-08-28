# Run record

Probe: `P-THORN-PLENUM-QUADRANT-CHARACTERIZATION-2`

The flat fields below are the machine-readable local record required by
`tools/check_verifier.py`.

```text
pin_commit: c389fc3259081b8ecb85f85df34e91d85f6aafb9
verifier_sha256: 1a0ffa8bffd180d40edbd96ed4160a6471568dbb654c329616e66fe8fdc02986
command: python3 probes/P-THORN-PLENUM-QUADRANT-CHARACTERIZATION-2/verify.py
platform: Linux
architecture: x86_64
python: Python 3.12.13
exit_code: 0
stdout_sha256: 4d2ed30606d71799c3786bb04bdd8b4cab913a4b0c4a0691f5e4b9f7a4698255
stdout_bytes: 490
stdout_lines: 13
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
prereg_sha256: a6cebf1a0376563909c668034c90629776e6d3d85624029aed488b5572199352
prereg_bytes: 14105
prereg_lines: 517
prereg_blob_sha1: 43d52f033402c30e6f68d1968d5691653ec0a634
verify_bytes: 14713
verify_lines: 507
verify_blob_sha1: b45935b69eba7556ff5c66d350c63aa8d24d691c
expected_sha256: 4d2ed30606d71799c3786bb04bdd8b4cab913a4b0c4a0691f5e4b9f7a4698255
public_claim_lock: issue 637
formal_date: 2026-08-28
```

The public remote readback at the full pin commit returned both frozen blobs
byte-identical to the local files. Both use LF-only line endings and end in a
final LF. Static parsing occurred before the pin; the accepted verifier was
not imported or executed before the pin. The first formal execution occurred
only after remote readback.

The accepted verifier was executed from the repository root with the frozen
command. Stdout and stderr were captured separately. `EXPECTED.txt` is the
complete raw stdout: 490 bytes in 13 LF-terminated lines. Standard error was
empty.

The local run is one x86_64 lane. It is not a two-architecture computation
gate. The proposed theorem status is proof-first from `PREREG.md`; the exact
verifier is its audit. The pull-request workflow must still reproduce the
committed bytes independently on x86_64 and native aarch64 and pass aggregate
`check`.
