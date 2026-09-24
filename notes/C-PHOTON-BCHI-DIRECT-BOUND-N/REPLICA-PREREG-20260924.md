# Prospective replica-cap and zero-sector audit

PUBLIC, NON-CANONICAL. C-PHOTON-BCHI-DIRECT-BOUND-N, issue #1143.
Author: A. M. Thorn. Date: 24 September 2026. Apache-2.0.
Public Canon v91, base 65195ab6ff6da1dcd3df17666238e16801b21838.

The analytical targets are a completely classified conditional two-copy
fiber and a full-measure bound on the globally zero-current sector. Neither
is a full-measure current-distance bound or a positive P1 certificate.
This is a notes audit, not a formal P-probe.

## Public pin before execution

Before the first scientific execution, commit and publicly read back this
file, REPLICA-CAPS.md and the complete verify_replica_caps.py. Record their
immutable commit and SHA-256 values. Its sole local imported helper is the
unchanged verify_connected_current.py from #1156, SHA-256
`ad3d0c75ffeeeed857bb918ba5ad4b21e725d776bbce6202eaf0076335896403`.
Read back and hash-check that helper from the same commit as well.
Its main audit is guarded and must not run on import.

No scientific execution precedes the pin. Syntax parsing and static proof
or source review are allowed. On Linux x86_64, Python 3, standard library
only, execute from the note directory:

```
PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 verify_replica_caps.py
```

Budget: 60 seconds. Exact integers and Fraction only. Require exit zero,
empty stderr, and final line
`RESULT PASS; no full-measure distance bound or positive P1 gap`.
Save the first run, exact stdout, neutral environment details, hashes and
byte counts in REPLICA-RUN-20260924.md. Recheck inputs after the run.

## Frozen checks

1. For D=3,4,8,16,32, L=2D+4, construct the aligned chain from the published
   four-cup and cubical boundary helpers. Expect 4D+40 total faces and
   D+1 absent 02 cross-section caps. Derive the equality graph from every
   support edge outside all cap boundaries. Its components must be exactly
   the two 20-face endpoint segments and D four-face tube segments. Do not
   assume their completeness merely from the proposed bit parametrization.
2. For each cap and each of the four neighboring binary color pairs, test
   all three ternary cap values against all four mod-five seam equations.
   Exactly one survives, x_left-x_right. This includes the charged endpoint
   edges; no additional charge allocation is permitted.
3. For D=3,4,8, enumerate all 2^(D+2) resulting ordered local pairs, build
   both actual ternary surfaces and check their sum, boundary and currents.
   Every one must be admissible. A color wall costs 1/4 in product weight;
   the common factor is 2^(-4D-40). The wall histogram is
   `2 binomial(D+1,h)`. Check complete partition and signed sums:
   `2^(1-4D-40)(5/4)^(D+1)` and `2^(1-4D-40)(3/4)^(D+1)`.
   The difference-current moment is exactly `(3/5)^(D+1)`, single-copy
   endpoint means are -1/2, its raw product is `(1+(3/5)^(D+1))/4`, and
   its conditional covariance is `(3/5)^(D+1)/4`.
4. For D=16,32, check the same complete geometry and local cap uniqueness,
   then the exact 2-by-2 transfer matrix. Do not enumerate their exponentially
   many bit strings. Both matrix eigenchannels must reproduce the same
   partition and signed sums. The all-D statement requires the written proof.
5. For L=4,6,8,10,12, construct the k=floor(L/4)^4 four-cup supports at
   basepoints 1+4r in each coordinate. Check 21 faces per support, pairwise
   disjoint vertices, no wrapping, and edge-disjoint central current loops.
   Against backgrounds zero and either orientation of the specified 012
   cube at (3,3,3,3), check every signed subset of the first min(k,4) patches:
   ternarity, exact boundary, weight exponent, recovery of signs from current
   and background by subtraction, and no duplicate image. Expect
   `3^(min(k,4)+1)` distinct images for each L.
6. Check exactly `2^-20 * 2^-21=2^-41` and the complete binomial identity
   for each audited k. This checks finite inputs to the partition injection;
   it does not enumerate arbitrary closed backgrounds or the full partition.

The zero-halo exterior factorization and the arbitrary-face source Hessian
bound have written analytical proofs. No numerical transform, random sample,
fit, infinite-volume conclusion from a finite enumeration, or arbitrary
exterior conditioning test is part of this execution.

## Failure and evidence ceiling

Keep the first failure, timeout, nonzero exit, unexpected stderr or hash
mismatch attached to this unchanged pin. Do not repair a frozen source or
change a target silently; any correction requires a fresh public pin and
an explicit disposition of the failed attempt.

The proof is candidate-T; this finite, one-architecture audit is candidate-C.
Separate agents reviewed the derivations using shared sources, not a blind
external review. Ordinary repository CI is not a second-architecture
execution of the notes audit. P1 and the phase remain open. No Canon,
Registry, workflow, formal probe or prior pin changes are authorized here.
