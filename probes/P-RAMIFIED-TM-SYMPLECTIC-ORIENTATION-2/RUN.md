# P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-2 run

## Immutable pin

```text
claim_issue:       639
base_commit:       493f271285a9b2c683ff91c75c5771ef3a57b7e7
pin_commit:        489b28ae6d91718652f576cddf8c02b645e49571
prereg_blob:       bea6df06afcd445ff1a7ffd9ef8903bd8d171a22
prereg_sha256:     dd1c1bfa1330e9deb5e5679d02ff100173dc1f32e32b7cf3369e22a898d00bd1
prereg_bytes:      8871
prereg_lines:      262
verifier_blob:     3b40c74d14114d7839b1e712e55b1624b7fd8acb
verifier_sha256:   eb1deaf17234e3ce436dc1eb9e93aa88d6b40891dc2f0613e6b2275a88870384
verifier_bytes:    4753
verifier_lines:    154
line_endings:      LF
final_LF:          yes for both pinned files
```

Both pinned files were fetched from the public remote at the exact pin before
the first formal execution. Their Git blob SHAs, SHA-256 values, byte counts,
line endings and final LF matched the frozen records.

## Formal local execution

```text
platform:          Debian GNU/Linux 13
architecture:      x86_64
python:            3.13.5
working_directory: repository root
command:           LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 probes/P-RAMIFIED-TM-SYMPLECTIC-ORIENTATION-2/verify.py
exit_code:         0
stderr_bytes:      0
stderr_sha256:     e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stdout_bytes:      391
stdout_lines:      9
stdout_sha256:     8445d1c0fcb96db62f033932732f448759d5cd685b5aeb13e5c976c0a1c6af8a
expected_bytes:    391
expected_lines:    9
expected_sha256:   8445d1c0fcb96db62f033932732f448759d5cd685b5aeb13e5c976c0a1c6af8a
```

The stdout was copied byte for byte to `EXPECTED.txt`. The local execution is
one architecture lane only. It is a reproduction of the written proof audit,
not the two-architecture public gate. The required GitHub x86_64, aarch64 and
aggregate checks remain pending at this record.
