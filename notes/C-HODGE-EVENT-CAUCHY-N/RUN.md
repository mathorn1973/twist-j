# RUN - C-HODGE-EVENT-CAUCHY-N

PUBLIC NON-CANONICAL candidate-C corroboration. Author: A. M. Thorn.
Owner: #1239. Not a formal public-probe or Canon promotion record.

## Prospective custody

pin_commit: 19804efeae85c5514a0801960d76612c8bba51bb

All three prospective files were publicly read back byte-for-byte before
scientific execution. Their SHA-256 values are:

- `PREREG.md`: `98b3c9008f6e43c9c9cc2abc65f73164177b605b33d9fd569a01af1c1b48a266`
- `model.py`: `adc99adac6ff1e3d9e76d4952b97af16fcdbe919021c5947bdb6c0feb7b3a772`
- `verify.py`: `3555a3faa82c9dc16e2bca1dfbd929ac0adc351c5d9156cfdcdd03eaffd414f6`

Execution command from repository root:

    python3 notes/C-HODGE-EVENT-CAUCHY-N/verify.py

Environment: LC_ALL=C, TZ=UTC, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1. No third-party numerical library.

## arm64 reproduction

platform: Darwin
architecture: arm64
python: 3.13.13
exit_code: 0
stdout_bytes: 715
stdout_sha256: 4f5f616e39be550c235acc2f5535673b2c58bb48ecf58eb22d3301195b4865ad
stderr_bytes: 0

## x86_64 reproduction

platform: Linux
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_bytes: 715
stdout_sha256: 4f5f616e39be550c235acc2f5535673b2c58bb48ecf58eb22d3301195b4865ad
stderr_bytes: 0

Both architectures ran the unchanged public pin. The x86_64 source hashes
were checked against the same public-readback SHA-256 values. This is
reproduction of the same code, not independent-agent confirmation.
Ordinary notes-only CI does not execute this audit; its success will not be
misrepresented as a separate two-architecture scientific replay.

## Exact output (both architectures)

```text
PASS G1: exact orthogonal Hodge frame and metric-derived positive weights
PASS G2: sum(alpha)=1/2+sqrt5/5<1; positive stability margin
PASS G3: 324 rounded integer events admitted and distinct; slice/time checks
PASS G4: sparse Cauchy evolution, reverse step, positive conserved energy and source work
PASS G5: independent periodic matrix/neighbor comparison; self-adjoint positivity bounds
PASS G6: retarded Green recursion, finite support and forced Duhamel identity
PASS G7: 64 exact group-speed polynomial controls and Taylor moments
PASS G8: rounded-event spacelike one-hop witness; no microscopic light-cone claim
NON-CANONICAL: selected scalar field on an event subcarrier; no native/physical photon closure
```

Earlier publishing attempts lacked write access. No audit ran before the
successful public pin and readback. The unreachable local drafting commit
was never used as scientific evidence. No secret or machine identity is
included in this record.
