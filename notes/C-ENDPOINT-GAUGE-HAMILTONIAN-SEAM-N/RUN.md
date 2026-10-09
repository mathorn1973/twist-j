# First exact endpoint-Hamiltonian audit

NON-CANONICAL. Candidate-C finite evidence only; no physical closure.
Reservation #1412. No independent review or second architecture is claimed.

## Immutable public inputs

Repository base: 7d7f588c42422c2cf37b04d76ebc13ca55eb96dc.
Public pre-execution pin: 367772f9724ae0a72e389e0a32743766b9d438fb.
Pin tree: 35313e5a95205b475903c8d0f200e30247998e60.
Branch: notes/c-endpoint-gauge-hamiltonian-seam-n.
Pre-run receipt: issue #1412 comment 6046332771.

| File | Bytes | SHA-256 |
|---|---:|---|
| CONTRACT.md | 7803 | 51cd82dd255a3cb1abdc1fa34553eacb32e0d5eb0e0856f6194bfd1b56c8dbed |
| PROOF.md | 15135 | 71cda77475cef16ae5a866033a1d916e65fa93d71e58f46bf3b1cdebabcc36a6 |
| audit.py | 15177 | 5e12a4ac417a25ad304eb50a8f33e8aa07c3f526975cab10627ddc2f61867310 |

Public Git blob IDs and byte counts matched all three local files before
execution. The full proof was public, not reconstructed after a successful
run. Before that pin only syntax parsing and static inspection were done.
No frozen input changed after execution.

## Command and environment

The isolated mounted copy has the exact published bytes. It reads no other
file, repository, data source or external executable. From its parent:

```text
LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
python3 -I C-ENDPOINT-GAUGE-HAMILTONIAN-SEAM-N/audit.py
```

The supervising Python subprocess imposed timeout=45 seconds and captured
stdout/stderr as bytes. This was not a full repository checkout or a formal
public-probe runner execution. The frozen note calls for this standalone run.

```text
started_utc:     2026-10-07T20:34:21.337772+00:00
platform:        Debian GNU/Linux 13 (trixie)
architecture:    x86_64
Python:          CPython 3.13.5
timeout_seconds: 45
elapsed_seconds: 1.7997732270000597 (measured engineering timing)
exit_code:       0
timeout:         false
stdout_bytes:    3603
stderr_bytes:    0
```

Stdout SHA-256:
1878bb00b43169f02c9c99a286fd80ed6367fcb7ea864d8a7c326a5a313fa696.
Empty stderr SHA-256:
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.
EXPECTED.txt is the exact first stdout, not edited or trimmed.
There was one execution only. No failure was repaired or hidden.

## Scope and engineering checks

All science uses integer coefficient pairs and rational normalization;
no floating point enters a scientific assertion. Sparse operator outputs
remain on the unbounded flux carrier rather than a finite cutoff. A
negative-control FAIL is an expected asserted boundary, not omitted data.
The final output explicitly says physical closure, full photon phase and
native integer time are not provided.

Static inspection found only original prose and standard-library code,
with no external input, credentials, private infrastructure, executable
payload, workflow change or third-party material. All scientific files
are below the policy size limit. A same-author second algebraic description
checks the work and positivity identities; it is not blind confirmation.

Main's prior successful run 37518751601 was read for basis integrity only.
No new local full-repository replay is claimed. Ordinary PR policy/unit/
Canon/ledger/gate CI is requested separately after publication and does
NOT execute this note's audit.py. Its aarch64 job is therefore not a
second scientific architecture for this candidate. Publication-time CI
status will be recorded in the issue, not invented in this first-run record.
