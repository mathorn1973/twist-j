# Run record

Probe: `P-J-QUADRATIC-CARRY-NORM-SEAM-2`

The flat fields below are the machine-readable local run record.

```text
pin_commit: 440705a2dfb5a320e0a0ea3905cab93b2843fe24
verifier_sha256: 0c80346bb502a262a7635252c50f0ce8fff231fc2466b695dc488df6208e50f5
command: python3 probes/P-J-QUADRATIC-CARRY-NORM-SEAM-2/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: 650241cf430bced0a2e4e3f41bb8cb87152ded466fe5cdfc1ec74e9dd2bbfe38
stdout_bytes: 1564
stdout_lines: 32
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
prereg_sha256: 551708b2b715d05179642a61065026596559d371b26e32782d6aa7a2b9339fc0
prereg_bytes: 10936
prereg_blob: 9e59185c7a96668b7ed65da7169866895ac2fcb1
verify_bytes: 11483
verify_blob: 1177a67975570fb44c204150f10b3984740c4e56
expected_sha256: 650241cf430bced0a2e4e3f41bb8cb87152ded466fe5cdfc1ec74e9dd2bbfe38
public_claim_lock: issue 622
formal_date: 2026-08-28
formal_start_utc: 2026-08-28T12:19:08Z
formal_end_utc: 2026-08-28T12:19:08Z
predecessor_stop: issue 620 / PR 621
```

The formal execution occurred only after the fresh successor pin had been pushed and both public blobs had been read back with byte-identical Git object identities. The accepted verifier was executed once locally with stdout and stderr captured separately. `EXPECTED.txt` is the complete raw stdout. Standard error was empty.

The repaired G4 gate constructs `F_x(B)` and `F_(x^2)(B)` from the exact witness values, performs explicit polynomial multiplication over `Q(sqrt5)`, subtracts, and obtains the defect coefficients before target comparison. No predecessor verifier or output is consumed.

The local run is one x86_64 lane. It does not by itself satisfy the required two-architecture computation gate. The proposed theorem is proof-first from `PREREG.md`; the verifier is an exact audit. The pull-request workflow must reproduce the same committed stdout on both required architectures.
