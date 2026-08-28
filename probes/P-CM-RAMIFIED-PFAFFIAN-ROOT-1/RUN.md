# P-CM-RAMIFIED-PFAFFIAN-ROOT-1 run

## Immutable pin

```text
claim_issue:       642
base_commit:       524e9ca94124a265425be1bededbe2d054ff5485
pin_commit:        b714703b519f28eca9b0cc017431d74f9a3ce723
prereg_blob:       b55fe2ae231c56b9cfeddc77301a8b0d1aff8b26
prereg_sha256:     29158586aa9b5dad6a591fc1ee354d1142f3b92ce26e7d18271e1b5288e35f83
prereg_bytes:      11550
prereg_lines:      423
verifier_blob:     f2a23bc50664f0c20f781100c1f709ef9b2b28ab
verifier_sha256:   0ede3dd26e96ff0465dcb566a1a6b1a9174109274ab2b2e73fcfc20cbdd1a458
verifier_bytes:    6036
verifier_lines:    211
line_endings:      LF
final_LF:          yes for both pinned files
```

Both pinned files were fetched from the public remote at the exact pin before
the first verifier execution. Their Git blob SHAs matched the blobs used to
build the immutable pin commit, and the exact pinned contents matched the
frozen SHA-256 values, byte counts, line endings and final LF.

## Formal local execution

```text
platform:          Debian GNU/Linux 13
architecture:      x86_64
python:            3.13.5
working_directory: repository-root layout from exact pinned bytes
environment:       LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
command:           python3 probes/P-CM-RAMIFIED-PFAFFIAN-ROOT-1/verify.py
exit_code:         0
stderr_bytes:      0
stderr_sha256:     e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stdout_bytes:      786
stdout_lines:      11
stdout_sha256:     d4ade9939ad8b203b52d404a212a0f30b5ec6a13e1a0ed5fb3bdc1f95e478294
expected_bytes:    786
expected_lines:    11
expected_sha256:   d4ade9939ad8b203b52d404a212a0f30b5ec6a13e1a0ed5fb3bdc1f95e478294
```

The displayed verifier was executed only after public remote readback of the
exact pin. The runtime environment cannot clone public Git directly, so the
repository-root layout was materialized from the exact read-back pinned bytes;
the verifier is self-contained and reads no repository file. The stdout was
copied byte for byte to `EXPECTED.txt`.

The local execution is one x86_64 lane only. It audits the written universal
proof and does not by itself satisfy the public two-architecture computation
gate. The required GitHub x86_64, native aarch64 and aggregate checks remain
pending at this record.
