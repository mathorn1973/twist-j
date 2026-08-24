# P-AFFINE-QUADRATIC-READING-1 formal run record

Date: 2026-08-21

Status: local formal record. The public two-architecture gate is completed by
the repository pull-request workflow, which reruns the pinned verifier on
x86_64 and aarch64 and compares stdout byte for byte against `EXPECTED.txt`.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: 98f0ce2ba7cc530819ccc7c59d8876ce82effc48
verifier_sha256: ad3cd64800feda17546ae8211d4b39e014297bcf4a46096c434543ce3b35ff93
command: python3 probes/P-AFFINE-QUADRATIC-READING-1/verify.py
platform: Ubuntu 24.04
architecture: aarch64
python: CPython 3.12.3
exit_code: 0
stdout_sha256: fee39b2de0b74dbf8a1172217f008dd3a039c6e19bd6f01837fef6a6e0207585
stdout_bytes: 2653
stdout_lines: 42
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
parent_commit: 2a5601a9ec5cd5c8e24e80f3da78ca6838608fb4
prereg_sha256: e33e0aff5a5138f732958e9bab5d00ee023d82ec87e0b59f88ba3faf2e7ec609
prereg_bytes: 11763
prereg_lines: 283
prereg_blob: 1ce6eb6447d26a055efb8c36d6393fe99fbe6db6
verify_bytes: 15864
verify_lines: 500
verify_blob: 0ec5499e60dcffd190ec8df991469842179daeed
public_pin_comment: issue 495 comment 5371724364
```

Both accepted files were fetched from the public remote into a separate clean
checkout and read back there before execution. Their Git object identifiers,
SHA-256 values, byte counts, LF endings, final LF and ASCII decoding matched
the accepted bytes. The worktree was clean at `98f0ce2b` with no untracked
file. Static parsing and syntax compilation passed before the pin; the
accepted file was not imported or executed before it.

The accepted verifier was executed exactly once, from the repository root of
that clean public checkout. It began at `2026-08-21T15:13:37Z` and finished
within the same second. The interpreter was started from an emptied
environment carrying only:

```text
PATH=/usr/bin:/bin
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

`EXPECTED.txt` is the complete raw stdout with LF endings and a final LF. The
process wrote zero stderr bytes and exited zero. The verifier was not rerun,
and no byte of the pinned tree was modified by the run.

## Accepted run

```text
checks: 33/33 PASS
decision: AFFINE-QUADRATIC-READING-CONFIRMED
linear: (V*)^G has dimension 0
alternating: (Lambda^2 V*)^G has dimension 0
symmetric: (Sym^2 V*)^G has dimension 1, spanned by q_plus, positive definite
absolute: dim End_{Q[G]}(V) = 1 by rational rank, hence over every field of
          characteristic zero
motor_only_controls: symmetric 2, alternating 2, endomorphism 4
k_plus_control: lossy C_5-equivariant idempotent of rank two exists over
          Q(sqrt5) and satisfies u E u^-1 = I - E
target: P^T Gram(q_plus) P = (5 I_5 - 11^T)/2, and both frozen public constant
          matrices are positive rational multiples of Gram(q_plus)
global_scope: L1 only; READING-SPLIT untouched; no non-selection row moved;
          SAMPLING NOT PROVIDED
```
