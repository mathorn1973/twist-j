# First exact execution

NON-CANONICAL. Candidate-C finite audit; conditional candidate-T proof.
Reservation #1406. No independent reviewer or scientific second architecture.

## Immutable input

Public base: 7d7f588c42422c2cf37b04d76ebc13ca55eb96dc (Public Canon v100).
Public pre-execution pin: 8e4706770b5a4df019dc4093ab2f54c4c4c99b1a.
Input tree: 3d4279387746ffb0571d17043b9fe7dcb1a699d1.
Pre-execution public receipt: issue #1406, comment 6042139394.

| File | Bytes | Git blob | SHA-256 |
|---|---:|---|---|
| CONTRACT.md | 6634 | 1169dd9da67775d4c201ca756a9adcef82f5be3e | 98ac5ae0d8b7d7798b8163a343c03f4425ae5f38a8b884ead542930fa1593c4b |
| PROOF.md | 14061 | 8f19c8b3c87796bd6a81768d721690c683006039 | 0324e0d6cf821e07804682fd9e3123886d29d1f5c15efe0227ca7d0ae027dbbe |
| audit.py | 12490 | 2c09439c1e25436649ad425cef1c3edf7695bd0a | 477eb78981eefebe7a231f51870289802de466a4dce51ef5a37e1be7f7c4625a |

All three files, including the complete proof, were publicly committed and
read back before the first scientific execution. Their local SHA-256 and
Git blob hashes were checked immediately before launching the process.
They remain unchanged. Earlier unreferenced draft blobs are not the pin.
Connector timeouts interrupted publication before the pin; no scientific
process ran during that interruption.

## Execution

From this note directory:

```text
LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
python3 -I -B audit.py
```

The environment variables were passed to the subprocess; -I isolates Python
from ambient Python settings and -B disables bytecode writing. A parent
subprocess.run(timeout=45) enforced the actual time limit. The audit spawns
no children. A first-run receipt was written before launch to prevent an
accidental retry. Only stdout is the scientific transcript.

```text
operating system: Debian GNU/Linux 13
architecture:     x86_64
Python:           CPython 3.13.5
start UTC:        2026-10-07T16:25:39.517882+00:00
end UTC:          2026-10-07T16:25:49.718036+00:00
elapsed:          10.198513473 seconds (engineering measurement)
time limit:       45 seconds
exit code:        0
timeout:          false
stdout bytes:     2593
stderr bytes:     0
stdout SHA-256:   cd6eabea7b5f1796a39bf88ccf1ac3c9f8fefc7095bbce4cb632bd976234278d
```

EXPECTED.txt is exactly those stdout bytes, saved after this first run.
No corrective execution, changed input, suppressed assertion or rerun occurred.

## Exact return and limits

The first run passed both tori (2,2,2) and (3,2,2), each with empty,
single-edge and homogeneous material supports. It checked 1928 coefficient
basis columns, 128 complete closed steps, every local edge/face/material
work balance at the tested states, full Gauss defects and continuity,
five stiffness characteristic polynomials, 13 primitive unit scalings per
torus, the first self-consistent source and its off-source field at step two.
The missing-feedback control changed doubled energy by -3+2phi=1-2s>0.

Basis-column tests establish the tested linear identities on those finite
carriers. Quadratic identities at general states and all-volume statements
rest on the written proof, not only these samples. The direct P route and
the C^T C canonical-shear route were written by the same coordinator.
They are not blind independent implementations or an external review.

Static syntax and named-file security inspection found only standard-library
code, exact integers, ordinary output, and original English prose. No secret,
private address, external dataset, subprocess call in audit.py, network I/O,
third-party code or binary is included. All files are below the policy size
limit. No new local full-repository replay is claimed. Ordinary PR CI, when
available, validates the repository but does not execute this notes audit or
supply its second scientific architecture.
