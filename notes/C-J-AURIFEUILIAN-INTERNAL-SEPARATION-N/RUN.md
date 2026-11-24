# Frozen exact audit receipt

NON-CANONICAL. NO AUTHORITY. L1, candidate-C finite evidence.

## Custody before execution

Claim: https://github.com/mathorn1973/twist-j/issues/2090

Public source pin: `dab860c8c51ecc76da24a6960051340ad2e5d2cb`.
The three source files were fetched at that immutable commit and compared
against the local files for exact content and Git blob identity before
either program ran. The public issue recorded that completed readback at
2026-11-24 17:17:28 UTC, before both scientific executions.

| File | SHA-256 | Bytes |
| --- | --- | ---: |
| PREREG.md | `4be8f84da7977fb25e08459965e77be18308c8304462671d25208d32cff139df` | 7005 |
| verify.py | `eb30699b9bb464badb23b5de85d96c2d37548450836724fb6af3a6a5021ae603` | 4754 |
| break.py | `31e9d7ead01fe1a173eecb371aae8516a5c84bbf45dd4cb0f24b43cbd72949eb` | 5350 |

Authored local pin: `1a1b34f34fad6ff611cceeb01f3d09c43521db8f`,
A. M. Thorn <thorn@twistj.com>. Its tree and the connector transport tree
are identical: `821477266c7001b5b9d2b1f6236b93105d4e59a7`.
The connector supplies the outer transport identity. No frozen file was
changed after this pin; all three hashes were rechecked after execution.

## Execution

Date: 2026-11-24. Platform: Linux 6.18.57. Architecture: x86_64.
Python: 3.12.14. Standard library only. Integer arithmetic only.
Working directory: repository root.

```sh
timeout 60s python3 notes/C-J-AURIFEUILIAN-INTERNAL-SEPARATION-N/verify.py > notes/C-J-AURIFEUILIAN-INTERNAL-SEPARATION-N/EXPECTED.txt
timeout 60s python3 notes/C-J-AURIFEUILIAN-INTERNAL-SEPARATION-N/break.py > notes/C-J-AURIFEUILIAN-INTERNAL-SEPARATION-N/BREAK_EXPECTED.txt
```

Both commands exited 0. Neither timed out. Both produced one deterministic
JSON line with a final LF. The two outputs were compared byte for byte.

| Output | Bytes | SHA-256 |
| --- | ---: | --- |
| EXPECTED.txt | 965 | `7d75b21b46803c47154a254361ecd41ff4d4fa3183efbef4656d0aba04cc05a1` |
| BREAK_EXPECTED.txt | 965 | `7d75b21b46803c47154a254361ecd41ff4d4fa3183efbef4656d0aba04cc05a1` |

## Evidence boundary

Sol wrote the recurrence/quadratic-coordinate verifier. Root wrote the
matrix-power/quartic-coordinate breaker without reading that verifier.
Both were frozen before the authors read each other's implementation.
Static cross-review occurred before the public source pin. The prescribed
full search and auxiliary relation sets then agreed exactly. The shared
preregistration and shared mathematical question remain common dependencies.

This is independent implementation within one team and one architecture,
not an independent external review and not a two-architecture science gate.
The notes-only source is not registered as a Canon probe. Repository CI is
not represented as replaying this scientific audit. No formal promotion.

No failure threshold fired, and no search bound was changed. The later
all-index four-unit formula is explicitly identified as a post-audit paper
deduction in FOUR_UNIT_WITNESS.md.
