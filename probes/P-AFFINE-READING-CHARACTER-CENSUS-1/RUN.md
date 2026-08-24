# P-AFFINE-READING-CHARACTER-CENSUS-1 formal run

Status: **LOCAL FORMAL RUN COMPLETE. GITHUB TWO-ARCHITECTURE GATE PENDING.**

## Machine record

pin_commit: ff5eba55e1c67ffd43836998fa0200202b50524e
verifier_sha256: 56c5c3a3a7c89be76ba7a112e14bbfd1d75e880b6b7a1fb6cf93e09c927b3566
command: python3 probes/P-AFFINE-READING-CHARACTER-CENSUS-1/verify.py
platform: macOS 26.5.2
architecture: aarch64
python: 3.9.6
exit_code: 0
stdout_sha256: 70905ff696f31286abdffe4899c505fdf1ccf27f2c925c5880a17224674e927a
stdout_bytes: 1370
stdout_lines: 34
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

The flat fields above are the repository checker's required machine-readable view. They describe the single formal local leg and do not alter the pinned scientific content.

```text
CLAIM ISSUE            #534
BRANCH                 probe/P-AFFINE-READING-CHARACTER-CENSUS-1
PIN PARENT             f9b7438747e612eeebf63cb3ac95283fcb2a7085
LAYER                  L1 exact arithmetic only
RESULT EXPOSURE        RESULT-EXPOSED
```

## Pin and public readback

Both accepted blobs were created before the pin, and their Git blob IDs and SHA-256 sums were recorded before either was referenced by the pin commit.

```text
PREREG.md
  git blob:           a7ed719d97315d05db10daae890a6d318a773873
  sha256:             c33aee9ebaf0599296dc442cc93829494d0c3fba8d09c935ad1568c2f5932b2a
  bytes:              11319
  LF lines:           273
  final LF:           yes

verify.py
  git blob:           8abd7bcdc10a0d02a530fd3288ed3665ce378cda
  sha256:             56c5c3a3a7c89be76ba7a112e14bbfd1d75e880b6b7a1fb6cf93e09c927b3566
  bytes:              16639
  LF lines:           577
  final LF:           yes
```

Both files were read back from public GitHub at the exact pin into a fresh clone, and the returned blob IDs and SHA-256 sums matched the pre-pin accepted values. The formal execution below was performed inside that fresh public clone, not in the authoring tree.

## Pre-pin discipline

Only compilation and static checks were run against `verify.py` before the pin: `py_compile`, an AST scan confirming that the only imports are `fractions` and `itertools`, an AST scan confirming that no float literal occurs, and an AST scan confirming that `float`, `open`, `input`, `eval`, `exec`, `__import__` and `random` are never called. No gate value was opened before the pin.

## Execution detail

The formal command recorded above is the canonical repository command required by `tools/check_verifier.py`. It was executed once after pin and readback inside an emptied deterministic shell environment with `PYTHONHASHSEED=0`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC`.

```text
EXIT CODE              0
STDERR BYTES           0
STDOUT BYTES           1370
STDOUT LINES           34
STDOUT SHA256          70905ff696f31286abdffe4899c505fdf1ccf27f2c925c5880a17224674e927a
STDOUT GIT BLOB        2e29bfd51780c90b60244ac4ae4659effc59b2d1
ELAPSED                2 s, engineering readout
DECISION               READING-CENSUS-CERTIFIED
```

`EXPECTED.txt` is the exact stdout of this single formal local execution.

All fourteen frozen gates passed on the first formal run. No threshold was moved, no gate was relaxed, and no value in `PREREG.md` was edited after the pin.

## Interpreter portability

The local leg ran on Python 3.9.6 and the required GitHub legs run on Python 3.12. The verifier uses no syntax or standard library behaviour introduced after 3.9, so byte identity across those interpreters is part of what the pull-request check confirms.

## Two-architecture gate

This aarch64 run alone does not satisfy the public two-architecture computation gate. The pull-request workflow must reproduce the same pinned verifier hash and byte-identical `EXPECTED.txt` on x86_64 and on aarch64 through `tools/check_verifier.py`, then pass aggregate `check`.
