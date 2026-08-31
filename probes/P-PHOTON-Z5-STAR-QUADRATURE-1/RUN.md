# Run record

Probe: `P-PHOTON-Z5-STAR-QUADRATURE-1`

```text
pin_commit: 66bcc0714cac5789292954bea300e398689ffd0a
verifier_sha256: 87fcc66932750cd325c8ab4f7c28e6832780e7ebd8b3bd19352b255391ce2044
command: python3 probes/P-PHOTON-Z5-STAR-QUADRATURE-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
platform: Ubuntu 24.04.4 LTS
architecture: aarch64
python: CPython 3.12.3
exit_code: 0
stdout_sha256: 8f883ec07afeb4db2c1d366e8d94d29305568643e07a97847aeef93ffd2c9015
stdout_bytes: 11042
stdout_lines: 157
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
pin_parent: 9f88c4c93aab3139ee0a2e007f0e60891957aa21
prereg_sha256: 3995786260f1e2eb785c36c27d8de6209c4c3d3f8abaa8decb35bc737b5892ea
prereg_bytes: 12785
prereg_blob: 0b936e2559654fce8dcd6b4e3d865c4a37219859
verify_bytes: 9869
verify_blob: b7a364daf66f334bad2ad6bd512f836ebfec1c2d
expected_sha256: 8f883ec07afeb4db2c1d366e8d94d29305568643e07a97847aeef93ffd2c9015
public_claim_lock: issue 723
formal_date: 2026-08-31
started_utc: 2026-08-31T09:53:44Z
```

Exactly PREREG.md and the accepted verify.py were committed with one parent
and pushed before the first formal execution. Both files were read back at
that immutable public commit and their decoded bytes, sizes, hashes and
blob identities checked. The
[public pin receipt](https://github.com/mathorn1973/twist-j/issues/723#issuecomment-5476679474)
preceded execution.

A separate clean Linux checkout fetched the public pin, verified the single
parent, both file hashes, Public Canon v72 content/tag ancestry and the
declared Canon hash, then ran the frozen command once from the repository
root. Raw scientific stdout and stderr were captured separately. The
repository remained clean after execution.

EXPECTED.txt is the entire actual post-pin stdout: 11042 ASCII bytes in
157 LF-terminated lines. Its transferred bytes match the raw stdout hash.
The run completed with exit 0 and empty stderr. The reported FAIL_HALF is
a completed scientific classification, not an execution error or abandoned
pin. Neither pinned file nor either threshold was changed.

This receipt records one aarch64 run. Required exact-head PR checks must
additionally reproduce the same accepted verifier and committed EXPECTED
bytes on x86_64 and aarch64 before merge. The local run alone is not a
two-architecture computation gate. No private execution path, machine
nickname, third-party source bytes or scratch file is part of this record.
