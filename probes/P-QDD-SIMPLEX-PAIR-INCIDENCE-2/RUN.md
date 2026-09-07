# Run record: P-QDD-SIMPLEX-PAIR-INCIDENCE-2

pin_commit: 2acf78ea5fbffaa93811b89f2ec44be14b907fb9
verifier_sha256: 0bc4b05c65e3cb09ffe80f0f8e583d97c7ac2e8122389500ccebf282ace9c6bd
command: python3 probes/P-QDD-SIMPLEX-PAIR-INCIDENCE-2/verify.py
platform: Debian GNU/Linux 13
architecture: x86_64
python: CPython 3.13.5
exit_code: 0
stdout_sha256: 6ca17fe44c2aeb9824f193a3b206d2b554450f59f4449c1323942b21b0e34f6f
stdout_bytes: 340
stdout_lines: 7
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1

## Public custody

Public issue: #879. The successor pin was pushed and all three scientific files
were read back from GitHub before the first invocation. Their Git blob SHAs at
the pin were:

```text
PREREG.md  b4e8a9ea09e954d0428bc5915199a01d885f3e6f
PROOF.md   dbf8a31c957802181d1a35eb42be3b4e3bfdca24
verify.py  ceb751711b26b111d503b3da5f84ae750fc0d302
```

The execution copy of verify.py had the same Git blob SHA
`ceb751711b26b111d503b3da5f84ae750fc0d302` before execution. The child exit
code was persisted immediately after process return, before hashes and metadata
were computed.

The predecessor `P-QDD-SIMPLEX-PAIR-INCIDENCE-1` is ABANDONED on public main
and was not executed again. This run uses only the fresh successor verifier.

## Result

```text
exact assertions: 104768
contexts: 2560
elapsed witness: 3.248363500 s
exit code: 0
stdout bytes: 340
stderr bytes: 0
```

The committed EXPECTED.txt is the exact captured stdout. No line-ending
normalization is part of the comparison.

This local x86_64 run is one architecture. The pull-request workflow must run
the same pinned verifier on clean GitHub x86_64 and aarch64 jobs and both must
match EXPECTED.txt byte for byte with empty stderr.

The universal claim rests on PROOF.md. The finite verifier is an audit, not a
physical experiment.
