# RUN: independently authored R1 breaker

PUBLIC / NON-CANONICAL / L1. A. M. Thorn. Apache-2.0.
Session: Codex-R1-20261017-b053a37f.

## Public pin and execution order

The independent proof, breaker, preregistration and custody record were
frozen at `c82083d532cdb7e134288ea5eebe3bb488ece0a4` on branch
`notes/C-J-AREA-WEYL-INDEPENDENT-REVIEW-N`, based on Public Canon v103
main `dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`.
The branch was pushed, fetched back and all six source files read back
byte-for-byte through the public GitHub content API before execution.

- Byte readback completed: 2026-10-17T21:52:12.676781+00:00.
- [PINNED_R1 receipt](https://github.com/mathorn1973/twist-j/issues/1587#issuecomment-6241784815)
  was created at 2026-10-17T21:52:14Z and read back before the first run.
- First scientific execution started at 2026-10-17T21:52:42.862386+00:00.
- Author-method comparison files were first fetched at
  2026-10-17T21:53:38.369849+00:00, after the initial independent run.

Only analytical derivation, static source review, AST parsing/compilation,
hashing and infrastructure policy checks occurred before the public pin.
There was no earlier scientific execution, import, dry run or scratch
calculation. The inverse checks added during static review preceded the
pin and all scientific executions. No pinned source changed afterward.

## Frozen bytes

| File | Bytes | SHA-256 |
|---|---:|---|
| `break.py` | 15123 | `f865591815907fb9a7a8b0f4f9a1f05eecbfda0a213044b9b1801be52db3358e` |
| `EXPOSURE.md` | 1953 | `a7e5769e66c750c5699c251bddf45c6b598dc0cf6c1989280e1a5cd846b82c91` |
| `PREREG.md` | 8267 | `07d5e3b49e22d4fc4bdefb1bcf77233c9be4056b83f4be807b09bcbf2ba9af86` |
| `PROOF.md` | 15647 | `03b61b0164362e24d66f3c479ba21bda4948308c02a1e8fc139ce40d9dc53209` |
| `README.md` | 1787 | `c0c84d86f204f896dc0867847046fb53bd2be8dd3e314d4ce77a489c55504644` |
| `SOURCES.tsv` | 1942 | `32c8f64700050ce4549595fa6254ef76320a05748122bc90884813d692a7f0f4` |

The scientific executable imports only Python standard-library modules;
it reads no runtime source files, data files or network resources.
SOURCES.tsv fixes the public mathematical input and authority custody.
All six file hashes were checked before and after each execution.

## Command and capture

From the repository root at the public pin:

```sh
LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
python3 notes/C-J-AREA-WEYL-INDEPENDENT-REVIEW-N/break.py
```

The capture process used Python subprocess with a 600-second timeout,
separate byte stdout/stderr pipes and no output normalization. The first
stdout is preserved verbatim as EXPECTED.txt. Scientific assertions do
not use floating point; elapsed durations below are measured wall times.

## Explicit architecture executions

These are two executions by this reviewing session, not two independent
scientific authors. The first used Linux under WSL on x86_64. The second
used a fresh public Git clone of exactly the pinned branch on Linux
aarch64; its HEAD and clean working tree were verified. All frozen
source bytes matched on both architectures.

| Field | x86_64 initial run | aarch64 reproduction |
|---|---|---|
| Platform | Linux | Linux |
| Architecture | x86_64 | aarch64 |
| Python | 3.10.12 | 3.11.2 |
| Start UTC | 2026-10-17T21:52:42.862386+00:00 | 2026-10-17T21:53:19.741069+00:00 |
| End UTC | 2026-10-17T21:52:43.045852+00:00 | 2026-10-17T21:53:20.256543+00:00 |
| Measured elapsed seconds | 0.18344803102081642 | 0.5154382089967839 |
| Exit code | 0 | 0 |
| Stdout bytes | 1061 | 1061 |
| Stdout lines | 6 | 6 |
| Stderr bytes | 0 | 0 |

Both stdout SHA-256 values:
`7be152de96ce83d6c7042553b434fcf1a3d1f10142fe0e8ed8b52674778ac4a0`.
Both empty stderr SHA-256 values:
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

Both outputs contain the explicit final line
`AUDIT PASS independent exact R1 identities and stated negative controls`,
with no FAIL or FALSIFIER line. All 1061 bytes match, including newlines.

## Inventory and interpretation

The six exact lines contain RING, CARRIER, CHARACTERS, COST, SCOPE and
the final scientific PASS. They report 64 module-basis covariance pairs,
64 fifth-step pairs, eight two-sided module inverse checks, 16 residue
basis pairs, 25 Weyl conjugations and two-sided inverses, 625 area pairs,
625 commutators, 625 product-cocycle pairs, 125 character-addition checks,
2500 faithful-character area checks, and 3125 diagonal-cost witnesses.
The cost constraint ranks are exactly 3, 4, 0, 4 for D, X, Z and their
intersection. The full infinite-ring and rational-class claims rely on
PROOF.md; the finite inventories alone do not establish them.

The negative controls are retained: one-step area preservation is false,
reduction erases the complex phase, and no physical character or energy
unit is selected. Native U admission and physical action/SI hbar remain
unsupplied. Printed scope labels summarize the written proof and limits;
they are not executable evidence of physical nonexistence.

## Infrastructure separation

Ordinary repository CI does not select `notes/.../break.py`. Its green
architecture jobs therefore cannot be described as runs of this breaker.
The explicit executions above supply its reproduction evidence. Final
repository policy, unit-test, Canon, ledger, gate and changed-path checks
are recorded at the result head in the draft PR and SUBMITTED_R1 receipt.
The notes-only changed-path verifier/reproduction checks are expected to
be NOT APPLICABLE. No author verifier was executed in this review.
