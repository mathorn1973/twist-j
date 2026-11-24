# RUN: first successful successor audit

**PUBLIC, NON-CANONICAL. candidate-C finite audit only.**
Owner issue: #1165
Author: A. M. Thorn
Date: 26 September 2026

## Frozen input

Candidate pin:

`fdd1662ec3f828db20c9982a6821e12628863e55`

GitHub readback before execution:

- `PREREG.md`
  - Git blob: `8ae07b965681e386de86536c573cf1147ab4f7f7`
  - SHA-256: `701d2284d095a7f27da68273f0bb6cc038b861ed1f2692ae4cb09cba5a0b2675`
- `verify.py`
  - Git blob: `cacc7d1a826d65ef07181dbd5668a0f37714eafe`
  - SHA-256: `7ed7ee99f4d6850f2467ad2134370c4dd339b1b981540ba0dedb80bf54e68ca6`

The verifier differs from the consumed #1164 verifier in exactly two source
lines: the candidate name and the single repaired auxiliary gluing fixture.

## Environment

```text
platform: Linux
architecture: x86_64
python: 3.13.5
```

This is one architecture. No two-architecture computation gate is claimed.

## Command

```text
python3 verify.py
```

## Result

```text
exit_code: 0
stdout_bytes: 805
stderr_bytes: 0
stdout_sha256: 8baf411612ac2599e3851962fa9c36cd4a250504b5646d3242bb5e6684729db1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

Exact stdout:

```text
FACE_TABLE PASS ordered_pairs=9
ACTUAL_STARS PASS states=153 ordered_pairs=23409
STAR_CENSUS 0:0=153 2:0=2160 4:0=6930 5:1=2304 6:0=7360 7:1=1080 8:0=2970 10:0=360 10:2=72 12:0=20
TOKEN_PROJECTOR PASS partitions=18862 signs=8191 admissible=1719
EXTERIOR_COMPLETIONS PASS cases=12616 inadmissible=5192
CONDITIONAL_CHARGE_MAX exact=1 witness_faces=3 doubled_faces=2 admissible_signings=2
GLUING PASS fixtures=3 covariance_entries=101
FOUR_CUP PASS states=53 replica_pairs=2809 covariance_entries=441
TORUS_WITNESS PASS D=3,4,5,8,13 conditional_connection=1 difference_current_product=4 ell=4
UNIFORM_CONDITIONAL_THINNING REFUTED scope=declared_admitted_conditioning
ROOT_BUDGET PASS p_upper=31250/208397 disagreement_upper=11559968750/43429309609
AUDIT PASS; uniform_Xi=OPEN; P1=OPEN; no_physical_promotion
```

Stderr is empty.

The successful finite audit earns at most candidate-C. Same-architecture replay,
if performed, would be reproduction only.
