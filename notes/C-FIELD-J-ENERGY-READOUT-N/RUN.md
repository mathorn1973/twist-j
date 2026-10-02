# Author audit run

PUBLIC, NON-CANONICAL. This is one x86_64 execution, not independent review
or a two-architecture scientific reproduction.

- Reservation: [#1323](https://github.com/mathorn1973/twist-j/issues/1323).
- Frozen input: `49dfad177c6ab698b5751de3e56629508982b05f`.
- Preregistration SHA-256: `d22b014e416d288f06cfac31849e73c61786932adb9307df59bde69b2e8bf351`.
- Basis: `44423153eee6259c7277eec5f5adbed9679f9146` (Public Canon v96).
- Verifier SHA-256: `2e0a96b7680e1f22afc895a18a8506344bfe841f3fb1a853cb76241449f875ba`.
- Verifier bytes: 18489.
- Proof SHA-256: `c7c8e196776fedb3fa5f7f8851a62591f8ae3c024bc2a7d85721772eb7a1542f`.
- Public readback: all three source Git blobs matched the frozen tree before
  execution; the execution checkout had exact HEAD and a clean worktree.

Command from repository root:

```text
python3 notes/C-FIELD-J-ENERGY-READOUT-N/verify.py
```

Environment: Ubuntu 22.04.5 LTS, x86_64, Python 3.10.12;
`LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`.
Per-process timeout: 600 seconds. Date: 2026-10-01.

- Exit code: 0.
- Elapsed subprocess time: 1.588 seconds.
- Scientific stdout: 743 bytes, preserved byte for byte in EXPECTED.txt.
- Stdout SHA-256: `e0fa341c41cc0c1275d020f87b5d5927230099c67a86e09cd905560149522a7d`.
- Stderr: 0 bytes.
- Stderr SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

The run passed the frozen symbolic identities, complete 1225-point containing
box, 52500 in-range keys, 18750 outside keys, 20 malformed fixtures, 10 local
branch fixtures and 32000 chain-layer comparisons. The all-time theorem rests
on the written induction, not the finite trajectory audit. Historical targets
remain disclosed in PREREG.md.

An earlier execution-environment preflight rejected a cross-platform Git
worktree path before starting the verifier. The successful run used a clean
checkout with its own Git directory; no scientific input or threshold changed.
Ordinary notes-only CI does not execute this candidate verifier automatically.
