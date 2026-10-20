# Analytical and static review receipt

Status: NON-CANONICAL, L1 review context  
Probe: P-INTEGER-PRIMITIVE-SOURCE-METRIC-1  
Pin: 7ffee4939346221e2d43ed386f33bdfa47cd509f

This receipt describes reviews within the same assisted authoring session.
It does not claim an independent human laboratory or an unrelated external
review session. A later public reviewer can inspect the immutable pin,
proofs, code and exact run record without relying on these statements.

## Separation of work before the public pin

The primary author wrote PREREG.md, SOURCE.md and the polynomial/matrix
verify.py. A proof author derived and wrote PROOF.md without reading either
new implementation. The breaker author received PREREG.md and canonical
sources and wrote breaker.py without reading the new verify.py or PROOF.md.

The breaker author participated in the shared mathematical specification
discussion and saw another team member's analytical report. This exposure
was disclosed before the pin and is stated in the frozen source manifest
and code header. The separate implementations use different arithmetic
representations and field-operator encodings, not a shared runtime helper.

A third reviewer first examined the mathematical source, inverse, metric
and action claims, then statically read the complete primary, and finally
compared the completed breaker with the primary and PREREG.md. The root
author also read the full proof and both final implementations.

## Findings before execution

The analytical review checked:

- The exact source-controlled field inverse, retaining chi and the
  boundary divisor 324.
- The primitive denominator proof despite arbitrary integer forcing under
  the selected dipole.
- The exclusion of the constant zero mode in the all-counter response
  estimate and the restriction of Lorentz signature to ready histories.
- The sign and normalization of the prescribed-source term when all
  spatial metric, lapse and shift variables are varied.
- Exact first-block costs, common-counter contrast, and all eight periods,
  including the free source kick after an exactly funded field update.
- The distinction between the actual account and the cost of an explicit
  numerator/denominator pair.

The implementation review checked the polynomial quotient/conjugation,
direct real-pair and eight-coordinate formulas, C and L matrices, literal
initial slices against bit-derived slices, every phase and inverse guard,
fixture counts, rational divisions, local-action variations, controls,
complete cycles, serialization and raw-byte comparison.

Pre-pin clarifications made the source sign explicit as a context key,
specified the backward direction at the lower boundary, required positive
representation denominators, and separated child runtime errors from
completed scientific failures. An unused pair of runtime labels was
removed from the breaker's ScientificFailure set before freezing.
No change followed a scientific result.

The final static review found no blocking discrepancy. Both programs
parsed and compiled statically, with no scientific execution or import.
The full public six-file pin was then read back before the first run.

## Computational evidence is separate

RUN.md records the actual first formal computation and EXPECTED.txt its
exact stdout. The primary and separate breaker completed with equal raw
certificate bytes. Static review alone did not establish that agreement.
The public draft PR workflow provides the distinct architecture evidence
after its actual jobs have completed; neither this receipt nor the proof
silently substitutes for those runs.

## Metadata

The available GitHub commit connector supplies the account privacy email
221838986+mathorn1973@users.noreply.github.com and exposes no author-email
override. The configured project identity is A. M. Thorn <thorn@twistj.com>.
This limitation was disclosed publicly before the pin, the actual commit
metadata was read back, and no immutable history was rewritten.
