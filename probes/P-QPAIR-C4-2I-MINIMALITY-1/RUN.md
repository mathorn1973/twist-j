# P-QPAIR-C4-2I-MINIMALITY-1 local run record

Date: 2026-08-18

Status: local reproduction record only. This record does not satisfy the
public two-architecture gate by itself and changes no Canon status.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: c934d22b1f56a0fcb17d13bb0e66cfcd3412393f
verifier_sha256: 5ec126c323fedb03175cf17194a0fe45a83afbdfe6b2466734823c0b35786e00
command: python3 probes/P-QPAIR-C4-2I-MINIMALITY-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.13
exit_code: 0
stdout_sha256: 5bca7df68594c3f6c0bca9f9f7433492fb6436bf62ba8401e47ff7482cc10929
stdout_bytes: 811
stdout_lines: 27
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: 31f1ff7317c386ace36020d4515e6e5890eb4bb1e98fc96c3615042c1fed7f63
PREREG bytes:  21819
PREREG blob:   c7c9db7b596cc43f3776c59bc68da0c7e62d80d2
verify bytes:  20861
verify blob:   64a2a8248c95e32badaec233f45a3a86b6d79d5a
```

The verifier was executed from a fresh detached worktree of the public
repository at the pushed pin commit, from the repository root. Both pinned
files had first been read back from the immutable public commit and matched
the locally reviewed files byte for byte.

Accepted deterministic environment:

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

Both recorded executions exited zero with empty stderr and byte-identical
stdout. The complete written proofs in `PREREG.md`, rather than the finite
coordinate audit alone, carry the seven universal theorem or counterexample
statements.

## Accepted run

```text
exact gates: 26/26 PASS
decision:    VERDICT PASS
```

`EXPECTED.txt` is the exact accepted stdout and has the byte count, line
count, and SHA-256 recorded above. Pull-request x86_64 and aarch64 jobs must
rerun the same verifier and compare stdout byte for byte before a Canon fold
may consume the result.
