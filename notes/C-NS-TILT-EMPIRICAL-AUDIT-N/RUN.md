# First arithmetic execution

NON-CANONICAL. Layer NOT_APPLICABLE. Candidate-C arithmetic only.
The result is a retrospective literature-summary diagnostic, not a
cosmological likelihood analysis or a new experimental observation.

## Frozen public inputs

Public pin: `65b1797eff9860f1138d1c4de16c1453f13158f2`.
Public freeze receipt: issue #1400, comment 6025582872.
The source main was `7d7f588c42422c2cf37b04d76ebc13ca55eb96dc`.
All three public creation-returned blob IDs matched the local bytes;
public commit readback confirmed the tree and parent before execution.

| File | Bytes | SHA-256 |
|---|---:|---|
| CONTRACT.md | 6373 | 71ed4acf7828e065046409b5d14c907cd07d693a9358792ae2b1a781d77ea02b |
| inputs.json | 5499 | 509c24f5cc4a23bd940cff20e2f833973e8fbcbc6cb14248ecb8c8967cbb0efe |
| audit.py | 5901 | 232e5fe0e9a04a8696b3c8d6154a2ded9a43822ccb78fe8737562545320fe823 |

## Actual command and environment

From this note's directory:

```sh
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  /opt/pyvenv/bin/python3 -I audit.py
```

A parent process invoked this command with `subprocess.run`, captured both
byte streams and enforced `timeout=30`. There was a first-run guard
requiring that no previous output receipt existed. Source hashes were
checked again immediately before invocation.

- Platform: Debian GNU/Linux 13 (trixie).
- Architecture: x86_64.
- Interpreter: CPython 3.13.5.
- Start UTC: 2026-10-06T21:15:10.133949+00:00.
- Finish UTC: 2026-10-06T21:15:10.942480+00:00.
- Elapsed time: 0.808326 seconds, engineering witness only.
- Exit code: 0.
- Stdout: 3653 bytes, stored exactly as EXPECTED.txt.
- Stdout SHA-256: `4d14c741c6bc2a25014fa5569770725e854fbe44f64d39c3d63aa3445cac4942`.
- Stderr: 0 bytes.
- Empty-stderr SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

The first execution succeeded. No correction or rerun occurred. Program,
inputs and contract were not edited after the public pin. The program's
PASS refers to its arithmetic controls and interval containment, never
to acceptance of the physical hypothesis.

## Review and engineering limits

One coordinator checked source equations, dataset labels and the code.
The same-program controls cover positive, negative, mixed and zero ratio
boxes, outward rounding and the last-digit convention. Prediction identity
checks use exact multiplication. None of these is an independent agent,
human referee, raw-data reanalysis or second-architecture verification.

The script ran on Python 3.13.5, not the formal public-probe Python 3.12
lane. This is a notes-only arithmetic witness, and claims no formal gate.
Ordinary two-architecture repository CI does not execute this script.
Its eventual outcome belongs to the public PR receipt, not this run.

The published differences are seven named note files only. Before the
result commit, the local files were checked for syntax, expected hashes,
trailing whitespace, accidental credentials and unrelated material. No
third-party executable or data archive is included. Whole-repository
policy/Canon/ledger/gate checks are delegated to the existing PR workflow;
no local full clone or local full-repository test is claimed.

NS-TILT remains H. No threshold, canonical source or cross-layer gate is
changed. The numerical enclosure is not a theoretical uncertainty budget.
