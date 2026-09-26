# Preregistered connected-current audit

PUBLIC, NON-CANONICAL; C-PHOTON-BCHI-DIRECT-BOUND-N, issue #1143.
Author: A. M. Thorn. Session: Codex-P1-connected-current-20260924.
Date: 24 September 2026. Original code/text: Apache-2.0.
Basis: Public Canon v91, main 316c3a2f413dbb37937e43fca123b1fe212a16af.

This is one notes-only continuation, not a formal P-probe. The user asked
for the decisive full-current estimate after #1155. The analytical work has
not established distance decay or a positive P1 gap. It has produced the
paired-surface representation, an explicit obstruction to a proposed
switching shortcut, and a stronger specialization of the existing complex
source bound. These are the precise subjects of this audit.

## Frozen inputs and execution order

Before first scientific execution, commit and publicly read back this file,
CONNECTED-CURRENT.md and the complete verify_connected_current.py. Record
the immutable commit and SHA-256 values. Static inspection and syntax
parsing are allowed before this pin; scientific execution is not.

Execute the unchanged script once on Linux x86_64, Python 3, with only
standard-library integers and Fraction. Command in this note directory:

```
PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 verify_connected_current.py
```

Budget: 60 seconds. Expected exit 0, empty stderr, stdout ending
`RESULT PASS; no distance-decay or P1 conclusion`. After execution preserve
the exact stdout and metadata in CONNECTED-RUN-20260924.md. Check the input
hashes again. A second execution is reproduction, not blind confirmation.

## Prospective exact checks

1. Enumerate all 3^6 local incidence assignments. Exactly 153 obey the
   mod-5 constraint: 141 neutral and 12 charged. Occupied-degree counts
   are {0:1, 2:30, 4:90, 5:12, 6:20}. At neutral degree 2r, summing the
   factor 1/r! over compatible pairings is exactly one. Every choice of
   local pair reversals preserves the neutral constraint.
2. Use the twelve-face union of boundaries c_012(0) and c_023(-e_2)
   on L=8. Expected: 22 degree-two edges, one degree-four edge, four
   signings among all 2^12 choices, no current. The three unsigned
   matchings give component counts 2,1,1 and probabilities 1/2,1/4,1/4.
   Compare original and augmented partition sums and all 144 face
   covariance entries exactly, retaining cancellation of cross matchings.
3. Construct the explicit neutral tube at D in {3,4,8,16,32}, with even
   L=2D+4. Expected: 4D+40 occupied faces, eight degree-five edges,
   8D+60 degree-two edges, ternary coefficients and boundary equal to
   five times the two oppositely oriented elementary currents. Their
   charged supports have two components; the orientation-constraint graph
   is connected and consistent, hence has exactly two signings. The
   selected far-edge product is -1. Its complete j_0 form factor on t e_1
   is identically zero. This fixture cannot be used as a susceptibility
   lower bound or an unconditional failure of decay.
4. Check the rational source constant
   c=3281*5^20/3^44=312900543212890625/984770902183611232881 <1/3000.
   Check all sixteen signed four-edge patterns and normalized bounds for
   k=1,...,8. Single-circulation probability is <1/1501, compatible-pair
   occurrence <1/2250001, and absolute signed-pair covariance <1/4500001.

These targets were derived analytically before computation, not inferred
from a run. The universal pairing law and all-D construction require their
written proofs; passing a finite range does not establish them. No random
sample, floating-point fit, covariance-tail measurement or new physical
reading is part of this execution.

## Failures and review ceiling

Any failed assertion, unexpected value, timeout, nonzero exit, nonempty
stderr or hash mismatch is recorded against this unchanged pin. Do not
repair a frozen input, discard a failed attempt or shift a target. A repair
requires a fresh visible pin and correction record.

Ceiling: candidate-T for the written mathematical statements and candidate-C
for this finite audit, all NON-CANONICAL. Separate agents developed and
reviewed the derivations with access to the shared sources. This is not
blind external review or a formal two-architecture scientific gate.
Ordinary repository CI does not execute the notes audit. The contact bound,
original switching, prior source theorem and previous normalization are
credited at their existing scopes, not counted again as new results.

The success of this audit leaves the full covariance decay, evaluated
volume-uniform chi estimate, compatible b lower bound and P1 gap open.
