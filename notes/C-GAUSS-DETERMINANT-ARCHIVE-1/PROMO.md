<!-- SPDX-License-Identifier: Apache-2.0 -->

# Handoff: prepared, not executed

**NON-CANONICAL / L1. Scientific execution count: zero.**
Candidate C-GAUSS-DETERMINANT-ARCHIVE-1, public reservation #1951.

The prospective source commit is
`05c09a7de1a10cd1b466a7d9b2885b7e45e3461c`.
It is a local immutable Git commit, not yet a public preregistration pin.
It contains the complete six-field preregistration, written proofs and
two separately authored exact checkers. Neither checker has been run.
The attempted branch publication was blocked before a remote ref was
created. No other publication route was attempted. Public readback and
scientific execution remain pending; no expected output exists.

## Frozen source hashes

| File | SHA-256 |
| --- | --- |
| PREREG.md | 314ba15eacb0ab9e4e93ae5a511145e17bbfab3b39351d837229e4a3140ffcdc |
| PROOF.md | 976b5f33915593f3d75ce1e356b68a4bd0791a322333d6408dc06080f9ebc738 |
| verify.py | 828afff92f64a43ff2c2c50e3f830eb8ed4c2274fb7fee61355d4b36cd4d1ca2 |
| break.py | 10fa7d006c728ae0b6e9d0f559e4efd8c1e4a73b935bc16bd991c008446f6427 |

The breaker was written from PREREG.md and the public premises without
reading verify.py. It uses cyclic five-coefficient integer classes,
Fraction elimination and polynomial Euclid inversion for its determinant.
The primary uses four power coefficients and a Leibniz determinant.
The breaker omits the G0 pair enumeration; its actual finite coverage is
documented in its source. This is a same-session implementation crosscheck,
not a second architecture or independent public acceptance.

## Completed non-scientific checks

- Primary Python syntax compilation and breaker static AST parsing passed.
- Separate static primary-code review found no algebra, index, sign or
  inverse-order defect. Field-residue assertions and an explicit two-by-two
  branch-determinant identity were added before the source commit.
- Repository check_policy.py: POLICY PASS.
- Repository check_canon.py: CANON PASS v109 claims=609.
- Whitespace checks passed; the named files were inspected for public scope,
  status, source attribution and private-data exclusion.

These checks are not scientific execution of the new candidate. No byte
agreement, numerical audit result or two-architecture result is claimed.

## Next authorized execution sequence

1. Publish the existing branch notes/c-gauss-determinant-archive-1 with
   its existing history, and read back the source commit and hashes.
2. Run each frozen checker separately, keeping exact stdout and stderr.
   Compare independently computed source results, full edge-current vectors,
   matrix-record fingerprints, normalized determinants, full path areas
   and receiver controls. Preserve any mismatch; do not repair the pin.
3. Record RUN.md and RESULT.md. The expected G1 field-return failure and
   the missing coupled root-pair port remain explicit even if the scoped
   mathematical certificates pass.
4. Open a draft notes-only pull request and complete the required repository
   checks. Notes CI is not a scientific two-architecture run of these files.

Suggested review title: `notes: per-cut Gauss obstructions and a prepared
determinant record`.

The handoff Git bundle requires the public base commit
`d4d363722f052141a4ce65e9da39f11a74b43b95`. The bundle transports only the
new candidate commits and preserves the declared A. M. Thorn identity.
