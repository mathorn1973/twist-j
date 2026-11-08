# Scope, proof and implementation review

Scope: NON-CANONICAL NEW_DECLARED L1, scalar normal form, force a=0.

Review type: same-session analytical and source review. This is not blind
discovery, external peer review, independent physical validation, or a
separate execution or architecture replay.

The mathematical contract and proof, followed by both complete program
sources, were reviewed before prospective pin
`02ec973ecb77655e83d69b990ba22bef05df3424`. The coordinator published and
read back the six-file pin and its
[receipt](https://github.com/mathorn1973/twist-j/issues/1668#issuecomment-6280031996)
before the first formal execution. This review record was written after
the coordinator reported that first local gate as PASS. No scientific
program, import, fixture evaluation or independent replay was performed
as part of this review, and no frozen file was changed. Run custody and
acceptance evidence belong to RUN.md and RESULT.md.

## Mathematical findings

The fixed-total-lapse problem is distinct from independently varying all
lapses. Matching momenta already implies equal bond energies; constrained
lapse variations impose no numerical energy value. Adding a constant
multiple of the already fixed total lapse does not select an energy.
The separately specified energy shell is therefore an additional
classification condition, not an outcome inferred from fixing the sum.
The predecessor's free-lapse zero-energy conclusion remains intact.

At fixed horizon, `(z0,L)` completely classifies the declared finite phase
equivalence, with lapse arrays retained as part of a history. The proof
constructs the unique required vertex parameter from differences of
cumulative lapses. This is a real phase-space statement. It neither
supplies a global rational-valued flow nor identifies different horizons.

The narrower continuous regular-path relation also needs the ordered
interval components of every bond lapse. Their necessity follows from
the removed chart singularities, and their sufficiency follows from
straight interpolation within the fixed-sum intersection of those
intervals. Restricting a global phase orbit to regular representatives
does not silently impose that stronger path condition. No finite count
of all chart sectors is claimed.

The boundary classification correctly includes the range condition for
`B_T`, the minimum-norm particular momentum perpendicular to its kernel,
and the residual sphere in that kernel. It distinguishes an invertible
boundary map, a zero-radius fiber, and an incompatible energy. Endpoint
configuration, total lapse and a separately imposed energy are not
independent freely assignable data.

For `T=3,L=0`, the proof establishes invertibility of `B3` with five
positive and one negative direction. It does not incorrectly call that
matrix positive. The spatial spectrum, negative Schur complement and
positive commuting factor justify this inertia. The rational Schur
value in the proof was also checked algebraically. The boundary action
and its lapse derivative use the bond generating function; the known
endpoint term has the separate boundary-gradient correction stated in
the proof.

At the composite caustic `T=3,L=-3`, the analytic mode argument proves
that the kernel is exactly the uniform direction. The declared endpoints
and energy therefore leave exactly two finite phase-equivalence orbits.
The displayed representatives have regular individual links even though
the composite boundary chart is singular. They use negative lapses and
the uniform mode. The result is not transferred to a positive-lapse,
mean-zero, or principal-chart preparation. The two sign choices have the
same chart intervals, but remain inequivalent because their initial
momenta differ.

No hidden assumption requiring a new nonlinear gravitational interaction,
physical clock, metric reading, energy preparation or cross-layer lift
was found. The classification remains a consequence of the fixed linear
scalar phase dynamics.

## Implementation and audit findings

Both complete sources were inspected against the prospective contract.
No blocking mismatch was found. The primary's matrix-power construction
and direct matrix derivatives are distinct from the breaker's coefficient
recurrence and exact dual-number differentiation. This is implementation
separation within one exposed session, not an assertion of independent
scientific discovery.

The review checked the following details:

- Unpivoted LDL certificates use the declared coordinate order. The
  primary's additional direct LDL check of `B3` is safe: its leading
  five-coordinate block is
  `(I-Lsp)(3I-Lsp)+g^2 ell ell^T`, which is positive, and the remaining
  direction is negative by the proved inertia.
- Dual inversion chooses pivots with nonzero primal part and retains
  factors having zero primal part but nonzero derivative. Fraction and
  dual arithmetic therefore preserve the required inverse derivative.
- The primary's triple convolution and the breaker's nested convolutions
  include every term in the transformed quadratic action coefficients.
  Incoming and outgoing momenta are computed from the actual substituted
  generating matrices and compared with transformed phase momenta.
- The payloads have the same 189-record order: seven initial records,
  six groups of 28 regular-case records, six caustic records and eight
  control records. The `S` records exclude `Ebdry` consistently with the
  stated bond-action sum. The constrained-variation count refers to the
  18 regular cases; the caustic works are additional checks.
- All eight controls use the frozen cases and observe the stated defect.
  In particular, the first seed has a nonzero lapse change, and positive
  energy excludes `K z0=0`; the omitted phase change and wrong dressing
  therefore have genuine nonzero first-order residuals. Initial momentum
  distinguishes the caustic signs, while the forbidden terminal parameter
  changes both total lapse and endpoint configuration.

The finite audit does not enumerate arbitrary real boundary data, evaluate
nonuniform finite exponentials, or count continuous chart sectors. Its
degree-four series and six uniform caustic histories audit the declared
formulas and witnesses. Universal completeness rests on the proof.

## Security and custody limits

The reviewed programs use only the Python standard library and exact
rational arithmetic. They read the five specified normative files, make
no scientific file writes, and contain no network access, credentials or
private machine identifiers. The primary launches only the fixed frozen
breaker with the same interpreter and `-I`, captures its output, and
requires successful exit, empty stderr and unmodified byte equality.
Neither program reads companion source, predecessor code or EXPECTED.txt.

This source review found no security or custody blocker. It does not
substitute for the public pin readback, formal run record, required
architecture checks, or a later reviewed Canon decision.
