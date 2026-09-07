# P-RECORD-OCCURRENCE-SYMMETRY-1 run record

pin_commit: 3344018bacbd365d3ee383de961334fea351c34f
verifier_sha256: 9c979a4b2ee3127810bf0338119b299cf2e581661b95a9e95ba2c5b48ebfec28
command: python3 probes/P-RECORD-OCCURRENCE-SYMMETRY-1/verify.py
platform: Ubuntu 22.04 (Linux-compatible WSL)
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: 33c7113ffd89e38fdf8a04c3be40ef9eb09000c20ab110307bae4d35d59c4d6e
stdout_bytes: 357
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

Status: first local formal execution completed, 2026-09-07.
Public lock: [#887](https://github.com/mathorn1973/twist-j/issues/887).

## Public byte custody

The pin containing all three source files was committed and pushed before
execution. GitHub's contents API returned their bytes at the exact full pin;
the SHA-256 values matched the local accepted files:

```text
PREREG.md aea02ad2de00570f74353763392db5867d6b5aafc939af95e82817513b1a97e9
PROOF.md  6b48e154cbffcb5601ac44971332c84b0a07a863cc6ecc8826ff56e87d0e4710
verify.py 9c979a4b2ee3127810bf0338119b299cf2e581661b95a9e95ba2c5b48ebfec28
```

The public Git blob identifiers were, respectively:

```text
PREREG.md 8da861fe535cce550af5aa26cbf7a3f405d905b7
PROOF.md  8c06ca17fbe5a61c46a91489abf6ecef758f4c6f
verify.py cf40b942656571410a6d0bda8ecc2fe9ca6bcb19
```

Before the pin only AST parsing took place; no accepted audit was executed.
The worktree was clean before launch. A sandboxed WSL invocation was denied
by the service before Python or the launcher started. The authorized service
invocation then started the first verifier process; there was no failed
scientific run, changed source or regenerated accepted pin.

## Completed execution

The Linux launcher rechecked all three SHA-256 values immediately before
execution, used LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1, and imposed a 600-second process ceiling.
The actual interpreter was Python 3.10.12, within the declared >=3.10 range;
CI uses Python 3.12. Local duration was approximately 2.171 seconds, which is
audit metadata rather than a scientific threshold.

The complete first stdout was copied byte-for-byte to EXPECTED.txt. It has
2,585,664 passed exact assertions, 357 bytes and nine LF-terminated lines.
Stderr was empty. No accepted source file or output was normalized or edited.

This record describes the first local x86_64 run. Required GitHub x86_64 and
aarch64 jobs must replay the same pinned verifier and match EXPECTED.txt.
Their actual reviewed-head conclusions and byte digests are attached to the
pull request. Arbitrary-size statements rest on PROOF.md, not these finite
sample ranges or the number of passed assertions.
