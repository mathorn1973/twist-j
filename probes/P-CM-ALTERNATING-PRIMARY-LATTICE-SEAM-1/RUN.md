# Run record

Probe: `P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1`

The flat fields below are the machine-readable local record required by
`tools/check_verifier.py`.

```text
pin_commit: 1779535e221ef9efc9fcb6a577a21050dad9aa03
verifier_sha256: 7ed314282477c48b3124f06c5b70d92e830b3f85a18ecf0841f0916bdd8f9061
command: python3 probes/P-CM-ALTERNATING-PRIMARY-LATTICE-SEAM-1/verify.py
platform: Linux
architecture: x86_64
python: Python 3.12.13
exit_code: 0
stdout_sha256: 564874aa8b2bdf28577947dbb82e249cf8cb338aa19dbde3ce3cf352e21ec7ff
stdout_bytes: 571
stdout_lines: 14
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
prereg_sha256: 35cd737ddbb8ee65cb7b983d97035916841b2fd1fe64f9707693af25662655de
prereg_bytes: 20173
prereg_lines: 595
prereg_blob_sha1: a53de0e2dbfe9e7de5c9048307be9298e764fade
verify_bytes: 21382
verify_lines: 702
verify_blob_sha1: 71c3383741678ff96c14c544b38973d6ad8125af
expected_sha256: 564874aa8b2bdf28577947dbb82e249cf8cb338aa19dbde3ce3cf352e21ec7ff
public_claim_lock: issue 625
formal_date: 2026-08-28
```

The public remote readback at the full pin commit returned both frozen blobs
byte-identical to the local files. Both use LF-only line endings and end in a
final LF. The first formal execution occurred only after that readback.

The accepted verifier was executed from the repository root with the frozen
command and deterministic locale, timezone, and hash-seed environment. Stdout
and stderr were captured separately. `EXPECTED.txt` is the complete raw
stdout: 571 bytes in 14 LF-terminated lines. Standard error was empty.

The local run is one x86_64 lane. It is not a two-architecture computation
gate. The proposed theorem status is proof-first from `PREREG.md`; the exact
verifier is its audit. The pull-request workflow must still reproduce the
committed bytes independently on x86_64 and aarch64 and pass aggregate
`check`.
