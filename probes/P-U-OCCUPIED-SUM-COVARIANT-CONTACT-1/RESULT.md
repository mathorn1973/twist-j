# Occupied SUM continuation: result and boundary

Status: PASS. Conditional L1 theorem candidate; PUBLIC, NON-CANONICAL.

The first execution of the immutable public pin completed with exit 0,
empty stderr and byte-identical reports from the two separately implemented
audits. No preregistered falsifier fired. No input, threshold or scientific
code was changed after the pin, and no failed run was repaired or repeated.
See RUN.md for custody and EXPECTED.txt for the exact report.

## Earned mathematical scope

PROOF.md and the separate symbolic argument in REVIEW.md establish the
following conditional result directly from the displayed native generators.
The finite audit checks it; unbounded-time conclusions do not come from
extrapolating the sampled tail.

- In exactly the declared class `f:F5^2 -> F5`, complete b,d,e covariance
  is equivalent to the two sign/swap constraints. There are 15625 maps,
  with 3125 unit-gain maps on the occupied SUM orbit. All 3125 induce the
  same complete supported trajectories. The unique affine unit member is
  `f=3*x+2*y=2*(y-x)`.
- With the declared independent passive source and one fixed trigger N>=4,
  the autonomous enlarged law acts on the actual first-write output, with
  one continuing counter. The same scalar R reads t initially, t+s1 at
  every boundary 3 through N, and t+s1+s2 at every boundary from N+1.
- All stored coordinates are accounted for. The original q,r retain their
  freely evolving native values, and s2 remains unchanged. The contact is
  a complete-state permutation; the full enlarged forward law is not
  globally injective. A clock-based inverse is proved on the whole reached
  H0-initialized time sheet and audited on every prepared step.

The exact finite inventory was 15625 class tables and 390625 class-point
checks; 78125 complete checkpoint/source pairs; 234375 complete-generator
commutations; and all 875 trajectories for the 125 independently prepared
triples at seven frozen trigger times. It checked 73750 complete-state and
source boundaries and 72875 inverse steps. Record checks covered 875
initial, 15125 first-sum and 56000 accumulated-sum boundaries.

The full-class table-set SHA-256 is
`a502b5450cbdc49a00946f2118d3d4dc2523302c261d36cc0eb2d9cd815ab983`.
The unit-subfamily table-set SHA-256 is
`3f4f7a4c047b506299e6014f5cda3a3e9171da9f2495a955fb6b1191aef62291`.
Both implementations independently produced those same complete-set digests.
The serialization and point order were frozen before execution.

The expected negative boundaries also held: no contact in this class has
unit gain on all stable states (the frozen H1 witness has h=0), and the
native-selector collision defeats global injectivity. REVIEW.md's broader
covariant example shows why the counts do not classify contacts with access
to additional coordinates. These delimit stronger claims, not failures of
the stated restricted theorem.

## What remains open

This construction assumes the contact interface, receiver-coordinate access,
passive source, preparation, trigger and reader interpretation. Native
selected b,d,e preserve M and cannot alone implement its nonzero new write.
The predecessor piston displacement is credited; its existence as an
algebraic map does not physically admit the new controlled interaction.
The first SUM is prior work from #1430 and is rederived, not new here.

No physical coupling, energy account, duration, arrival or absence detector,
two simultaneous archives, measurement law, event transducer or Born law is
established. The original q,r are not constant, and the first record is
replaced by the accumulated record. This result does not supply a globally
invertible native apparatus or prove global resource minimality.

`QDD-INSTRUMENT-APPARATUS`, `QDD-INSTRUMENT-CLASS-COMPLETENESS`,
`QDD-TERMINAL-EVENT-SEMANTICS` and
`GATE-L1-QUADRATIC-MEMORY-NATIVE` retain their existing open dispositions.
No Canon, registry, dependency or gate file changes here. The next substantive
obligation is independent admission of the listed physical resources and
contact law; further enumeration of equivalent on-orbit contacts does not
resolve it.

## Evidence and review status

The analytical targets were exposed before implementation. The symbolic
review and different implementations were produced within one coordinated
assistant session, with the disclosed later static cross-review. They are
not external human review, blind replication or physical observation.

The first recorded run is one-architecture evidence. Computational public
acceptance requires the repository's successful x86_64 and aarch64 replay
and aggregate on the reviewable PR head. The symbolic theorem remains a
conditional candidate; any promotion to normative T requires its own
reviewed Canon fold. This probe alone does not change a scientific status.

Public claim: https://github.com/mathorn1973/twist-j/issues/1438.
