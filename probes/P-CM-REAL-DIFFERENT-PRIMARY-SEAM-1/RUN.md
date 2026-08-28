# Run record

Probe: `P-CM-REAL-DIFFERENT-PRIMARY-SEAM-1`

The flat fields below are the machine-readable local record required by
`tools/check_verifier.py`.

```text
pin_commit: cb754bd9e4d13b0a83ec99291441dff5e0ffa5c9
verifier_sha256: 6ef7c8a208d21eab98c53fe6ffb7dd3017a87d91772b205baca10bbe612b1dd6
command: python3 probes/P-CM-REAL-DIFFERENT-PRIMARY-SEAM-1/verify.py
platform: Linux
architecture: x86_64
python: Python 3.12.13
exit_code: 0
stdout_sha256: b0621cef633d28d91793e24b1cb1d8214aabcf0d17ce49a0a91c955f82eb988d
stdout_bytes: 541
stdout_lines: 13
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
prereg_sha256: 0bbc48e2161a39b3f849b9e74c07b9f5d4c363baf392d5545850be090a8125dd
prereg_bytes: 14026
prereg_lines: 484
prereg_blob_sha1: cb578e7110fa7f8ac30c7497abb400c28265606f
verify_bytes: 20747
verify_lines: 770
verify_blob_sha1: 41407a20de42a1b55a4497123c3ada22821b1ed7
expected_sha256: b0621cef633d28d91793e24b1cb1d8214aabcf0d17ce49a0a91c955f82eb988d
public_claim_lock: issue 632
formal_date: 2026-08-28
```

The public remote readback at the full pin commit returned both frozen blobs
byte-identical to the local files. Both are ASCII, use LF-only line endings,
and end in a final LF. Static parsing occurred before the pin; the accepted
verifier was not imported or executed before the pin. The first formal
execution occurred only after remote readback.

The accepted verifier was executed from the repository root with the frozen
command. Stdout and stderr were captured separately. `EXPECTED.txt` is the
complete raw stdout: 541 bytes in 13 LF-terminated lines. Standard error was
empty.

The local run is one x86_64 lane. It is not a two-architecture computation
gate. The proposed theorem status is proof-first from `PREREG.md`; the exact
verifier is its audit. The pull-request workflow must still reproduce the
committed bytes independently on x86_64 and native aarch64 and pass aggregate
`check`.
