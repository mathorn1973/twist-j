# P-RELATIONAL-GROWTH-SATURATION-1 run record

pin_commit: c0cc02f08f508d9966dc1288f8530eb8d70d7f62
verifier_sha256: b38b6981af4d275fd7b2a810707e20b3cd61b8dbc365171f2ab36cb550235328
command: python3 probes/P-RELATIONAL-GROWTH-SATURATION-1/verify.py
platform: Ubuntu 22.04 (Linux-compatible WSL)
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: 70000c61a095556a12bc3d6ca530829b05ece0b3efb34d9411ff71aeab6562da
stdout_bytes: 348
stdout_lines: 10
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

Status: first local formal run completed, 2026-09-07.
Public lock: [#889](https://github.com/mathorn1973/twist-j/issues/889).

## Public pin custody

PREREG.md, PROOF.md and verify.py were committed and pushed before execution.
All three were read back using the GitHub contents API at the full pin;
their public bytes matched the accepted local bytes exactly:

```text
PREREG.md 379aea061b1ad2f5b9bd2a082394b38e8f13569300413f724e94f955e7faacdb
PROOF.md  19435a7bd5b33f2b7995262c2dbfc8eb8fa36b6112723fe15dc957aed60ef5c4
verify.py b38b6981af4d275fd7b2a810707e20b3cd61b8dbc365171f2ab36cb550235328
```

Their public Git blobs, in the same order, were:

```text
PREREG.md 39395d5d4fd5c6275ef8a16444e0ab8b6bbdf88f
PROOF.md  c42cd5ec83362a3ba066ad0f6dd23b79d98232c7
verify.py 9173f4346e5b5500c51c8038f7eef0b814fae89f
```

Before the pin there was independent analytic proof review and AST parsing,
but no accepted-verifier execution or import. The Linux launcher checked
these three hashes again immediately before starting the accepted process.
The separate untracked incubation note was not an input to the verifier.

## Execution and exact output

The first run used LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1 with a 600-second process ceiling. Actual local
interpreter: Python 3.10.12, within the preregistered >=3.10 range. Duration
was approximately 0.391 seconds; timing is metadata, not a scientific result.

All 304,993 exact checks passed, with exit zero and empty stderr. The complete
348-byte, ten-line stdout was copied to EXPECTED.txt without retyping or
normalization. No pinned source was changed after execution.

This is the local x86_64 record. Required GitHub x86_64 and aarch64 jobs must
replay the same verifier against this exact expected output. Their actual
reviewed-head outcomes and digests are recorded on the pull request. The
all-domain claims rely on PROOF.md; finite samples do not establish limits
or physical spatial dimension by extrapolation.
