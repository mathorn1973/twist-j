# First public-pinned execution

**NON-CANONICAL / L1. Result-exposed finite replay.**

The exact source, specification, proof, and introductory note were committed,
published, and read back before the first execution of this integrated verifier.
Earlier derivations and separate audits were known when the integrated code
was written. This record is not a blind preregistration or an independent
discovery claim.

## Pin and environment

| Field | Recorded value |
| --- | --- |
| Source pin | `3c75ff72c452692747836f374ed0babcc1b9abb7` |
| Parent / public base | `0c33e2b281e39127c269ef5dd7f5b529a62e9e65` |
| Worktree at execution start | Clean; HEAD and fetched public branch equal the source pin |
| Operating system | Linux |
| Architecture | x86_64 |
| Python | 3.13.5 |
| Assertions | Enabled |
| Isolation | Python `-I` |
| Exit code | 0 |
| stdout bytes | 1075 |
| stderr bytes | 0 |

Command from the repository root:

```sh
python3 -I notes/C-COLLATZ-BLOCK-CARRY-PRIME-N/verify.py
```

## Exact byte custody

| Object | Bytes | SHA-256 |
| --- | ---: | --- |
| `verify.py` at source pin | 12621 | `9a1d52e484d7363377fbfe18d5c721989e60e99fe347c7b0c493a957f0be2c84` |
| `REPLAY-SPEC.md` at source pin | 10845 | `425b9edcded617f6258145d6292b1ee6605620f9fdc20a1a184c1d35a876a059` |
| `PROOF.md` at source pin | 12770 | `9203c155e75dedba57c9ea771855bf316f14365d41e5cb8639c18235554f9567` |
| Actual stdout, retained as `EXPECTED.txt` | 1075 | `a729b48919eb69b53ad4e49924ce1b04d7bbbfd108337ce3f76f649ae2f193cb` |
| Empty stderr | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

The first execution passed without a source correction or rerun. The actual
stdout was captured before creating `EXPECTED.txt`; it was not assembled from
anticipated values. The verifier, proof, and scientific specification remain
byte-identical to their public pin. The subsequent commit adds the output,
this record, and the custody manifest, and updates only the introductory
note's evidence links and execution status.

## Earned scope

All checks in the fixed inventory passed, including the exact carry identities,
both maximal initial blocks, 510 admissible inverse pairs, the finite
golden-power search, and 1364 affine branch words. The finite output is retained
in full in `EXPECTED.txt`. Universal identities and the all-exponent Mersenne
block sign classification rely on `PROOF.md`, not on extrapolating the finite
inventory.

This is one recorded scientific execution on x86_64. Repository CI does not
select the verifier from this notes directory. Its architecture jobs are
repository integrity checks and cannot be counted as an additional execution
of this verifier or a two-architecture scientific gate. No canonical status,
global Collatz convergence, global golden-exponent classification, or physical
conclusion is earned by this record.
