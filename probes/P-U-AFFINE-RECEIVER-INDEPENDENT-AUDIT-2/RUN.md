# P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-2 formal run record

Status: **LOCAL FORMAL RUN COMPLETE (AARCH64).**

## Machine record

```text
pin_commit: 725b519cb49de7ccf8de5086ec6543c625e68f1c
verifier_sha256: 83b0da6108a70bba46258c6f9752dbed358e76bd03c8b0f0ca2c9dcf7dba02d6
command: python3 probes/P-U-AFFINE-RECEIVER-INDEPENDENT-AUDIT-2/verify.py
platform: macOS 27.0.1
architecture: aarch64
python: 3.9.6
exit_code: 0
stdout_sha256: 02740a3720f13ef6d9957420da5b1e88fd373c7949c43ec49454664ebe15700b
stdout_bytes: 494
stdout_lines: 15
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Execution custody

- Executed from repository root with `LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC` immediately after committing, pushing, and reading back the immutable pin `725b519cb49de7ccf8de5086ec6543c625e68f1c` from GitHub.
- Also verified byte-identical `stdout_sha256` (`02740a3720f13ef6d9957420da5b1e88fd373c7949c43ec49454664ebe15700b`), `exit_code: 0`, and empty `stderr` under CPython `3.13.13` on `aarch64`.
- Frozen `break.py` SHA-256: `db8782b9d8b1c14c4b64f8ce1c19ce925cd3987a3c9ddbcf255e35f25d2a915d` (`18020` bytes).
- Neither `break.py`, `verify.py`, nor `PREREG.md` changed after the pin. Primary `notes/C-U-AFFINE-TWO-COORD-RECEIVER-N/{verify.py,EXPECTED.txt,RUN.md,RESULT.md,PROOF.md}` and PR `#1520` were not opened before this run was completed and recorded.
