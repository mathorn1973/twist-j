# P-QPAIR-SYM2-TENSOR-DEFECT-1 local run record

Date: 2026-08-18

Status: local reproduction record only. This record does not satisfy the
public two-architecture gate by itself and changes no Canon status.

The flat fields below are the machine-readable record required by
`tools/check_verifier.py`.

```text
pin_commit: a991b70a590bc42aed9cc04ade1bc5836ee58f63
verifier_sha256: ccb252f1b2307811ec81e79e7d245a9bd78694965f2d975b8336411c7cca1234
command: python3 probes/P-QPAIR-SYM2-TENSOR-DEFECT-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.13
exit_code: 0
stdout_sha256: dd4774ed6ad065c19baa7efcb556a4d071d71d68a42e0203dff2c1722bdb16d1
stdout_bytes: 2329
stdout_lines: 36
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

## Pin audit

```text
PREREG sha256: 6d5e1a5509e10f558dbdac2881f2f0925b9169397a6de38b7e73bb3366086d9b
PREREG bytes:  17947
PREREG blob:   05ad577b14717ca4308af89a86f85e61f90011cc
verify bytes:  19260
verify blob:   2ed4ba77504e4c794a122ea832c876a7ae009695
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
stdout. The written proofs in `PREREG.md`, rather than this characteristic-
zero finite audit, carry the universal characteristic-not-two assertions.

## Accepted run

```text
exact gates: 29/29 PASS
decision:    VERDICT PASS
```

`EXPECTED.txt` is the exact accepted stdout and has the byte count, line
count, and SHA-256 recorded above. Pull-request x86_64 and aarch64 jobs must
rerun the same verifier and compare stdout byte for byte before a Canon fold
may consume the result.
