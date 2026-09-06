# Result: native chart and exact old-QDD readback boundary

Status: `T` proposed by the independently reviewed exact proof; non-canonical
candidate until a separate fold.
Outcome: `NATIVE-CHART-AND-READBACK-BOUNDARY-PROVED`, subject to required PR
acceptance on both architectures.
Action layer: L1 only.

## Mathematical result

The frozen proof establishes an explicit bijection between the native
synchronized sheet at each n>=3 and five F5 labels. The labels are constant
under U. Encoding them at a later clock gives the exact checkpoint, using
logarithmically many integer arithmetic steps in that clock. This is a
closed-form mathematical decoder for the synchronized native trajectory.
The clock remains part of the input; no new native register is introduced.

For an arbitrary initial record on an admitted origin-zero preparation set,
exact recovery from a later native checkpoint is possible if and only if the
record is constant on each admitted first-three-tick fiber. The actual full
registered QDD record fails this criterion on the full supported domain.
The frozen two supported heads merge after one tick but have old normalized
LOW values 0 and 9/14. Their later common native state cannot distinguish
those old records. This leaves the registered head-retaining orbit decoder
intact and answers the different late-current-state question negatively.

An explicitly added, correctly initialized static label with three values,
the initial-phase classes `{0},{1,2},{3,4}`, suffices to recover every field
of the old QDD record at every time, including the transient. Three is
minimal: one common tick-three checkpoint has three supported original
records with LOW values 1/16, 1/256 and 3/8. A two-state auxiliary alphabet
cannot distinguish them. Complete-head recovery instead requires five
values, attained by the saved initial phase. That lower bound is an immediate
corollary of the already public five-to-one fiber theorem.

Without additional state, the exact maximum preparation domain for full-QDD
readback contains 6500 of the 15625 origin-zero heads. In 125 fibers the
record multiplicities are (4,1); in the remaining 3000 they are (2,2,1).
The maximum is therefore 125*4+3000*2. The same bound is attained when all
admitted heads must be supported. The proof gives the two independent affine
constraints behind the exceptional 125 fibers; the verifier also constructs
a supported maximizing set. This changes the admitted preparation domain
and selects no privileged physical preparation rule.

## Exact formal audit

The first accepted execution was performed from public pin
`82da7e5aba4d22fe570e5d8432cbcc325077d451`, after commit, push and bytewise
public readback of PREREG, PROOF and verify.py. It completed on Linux x86_64
with exit 0, empty stderr and an unchanged clean checkout.

All nine groups passed all 1533811 exact comparisons. This count matches
the pre-execution loop-bound prediction and is not a count of independent
experiments. The audit covered all 15625 heads, all 3125 synchronized labels
at 28 frozen clocks, all 625 QDD piston inputs and all 3125 F3 fibers.
It checked 281250 trajectory snapshots, all admitted initial-phase inverses,
the transient readbacks, explicit collision witnesses, and the frozen enormous
clock `10**1000+123` on nine representative labels. The universal clock and
optimality claims rest on the written proof, not on these finite samples.

The exact stdout is 2323 ASCII bytes with one final LF, SHA-256
`2e1d4367ec647e32765a1e97784cfe7928c8a57b02e9fdfd5891ae4f1bce189b`.
EXPECTED and RUN preserve the complete output and neutral custody record.
No mathematical falsifier fired, no group was skipped, no execution defect
occurred, and no frozen equation, code, domain or threshold was changed.

Required PR acceptance separately reproduces the exact accepted verifier
against this same EXPECTED on x86_64 and aarch64 with Python 3.12. The first
local run alone is not a two-architecture computation gate.

## Provenance and remaining boundary

The private computations, inspected outputs, formulas and predicted counts
were disclosed before pinning. This is result-exposed proof auditing. Native
synchronization, five-to-one fibers, tail restrictions and complete-record
equality up to piston sign are inherited public results, not newly discovered
by this probe. The explicit chart and target-specific three-state/6500 bounds
are the new proposed scope. Existing sealed probes are unchanged.

The full physical decoder remains open. These L1 results do not derive a
protected memory interaction or reader/controller from U, generate a single
realized event, supply an occurrence measure or Born frequencies, or close
O1/O2a/O2b. The added label is a declared mathematical extension; it is not
native memory found inside U. Full-head invertibility holds on correctly
initialized reachable slices, not the unrestricted Cartesian extension.

No Canon, registry, dependency, gate, status, tag or release file changes in
this probe. A later public promotion requires its own reviewed fold.
