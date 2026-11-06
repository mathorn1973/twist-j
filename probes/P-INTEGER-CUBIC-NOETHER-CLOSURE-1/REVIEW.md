# Analytical and static cross-review receipt

Scope: NON-CANONICAL, NEW_DECLARED L1  
Probe: P-INTEGER-CUBIC-NOETHER-CLOSURE-1  
Pin: d978a878dd6044d7ba297d8402195a522e6fc8f8

## Authorship and independence of implementations

The coordinating session integer-cubic-noether-2026-10-19 authored the
prospective specification, source manifest and primary implementation.
The primary uses incidence arrays and explicit analytic derivatives of
the complete global action, with exact coordinate and four-point action
differences as additional comparisons.

A separate authoring agent, review_1652_code, wrote breaker.py from
PREREG.md without reading this new primary or PROOF.md. It uses a distinct
nested-array state, exact dual-number differentiation of the global
action, and sparse temporal generator matrices. It does not call, import,
wrap or copy the primary. The shared specification, graph, mathematical
definitions and literal fixtures are common inputs; the implementation
independence is not claimed to remove every possible shared specification
error.

The proof author review_1652_variation then statically cross-reviewed
the complete primary against the specification and the algebraic proof.
The third agent review_corrections_and_scope independently reviewed the
complete specification, recomputed the ten witness fractions, reviewed
the complete breaker, and checked the source/provenance boundaries.
The coordinator also read the proof, action definitions, source manifest
and implementation sections. These are distinct authoring/review contexts
within the same coordinated team, not an external institutional review.

## Pre-pin analytical and static checks

All of the following occurred before either new scientific source was
executed or imported:

- The complete global gradient was derived, including the two neighboring
  current contributions absent from the predecessor's local derivative
  test. The exact neighbor fractions 29/10368 and -17/51840 were
  calculated by hand.
- The four-dimensional vertex basis and six-dimensional cycle basis
  were checked analytically, giving 133 independent coordinates at T=5.
  The p variation was taken in ker(B^T), rather than in ten unrestricted
  edge coordinates.
- The local continuity residual and constraint propagation identity were
  derived off-shell. The first-order Noether completion included the
  mean of the parameter in delta_0 alpha.
- The formal order was kept separate from polynomial degree in fields.
  The nonzero second-order remainder 115/324, cubic central-difference
  defect -1/8 and Taylor substitution defect -115/648 were derived
  analytically, along with all remaining structural controls.
- The Lie-commutator convention, second-neighbor temporal terms, fixed
  endpoint rows, nonclosure witness and spatial-sum escape were checked.
- The common-D integer records and Dnew=20D Qp increments were checked
  against the rational definitions. No advancing-denominator scale was
  silently transferred from #1652.
- Both files passed AST parsing without import. Static review checked
  the dual arithmetic, Fraction types, index bounds, coordinate order,
  payload grammar, exact output contract and registered failure paths.
- Purely textual pre-pin clarifications made the field-redefinition
  remainder explicit, parenthesized whole time indices, and corrected
  the prose from mean-one to unit-sum where h=e/5 was used. These did
  not change the mathematical fixtures or either program.

The static reviews found no remaining mathematical or implementation
defect before the pin. This receipt does not retroactively describe the
later PASS as a pre-execution observation. The first computed gradient
and Noether digests are those recorded in RESULT.md and EXPECTED.txt.

## Scope review

The prospective acceptance condition requires both the exact first-order
identity and the specified negative results. The generally nonzero
epsilon^2 remainder is not interpreted as an obstruction to every possible
higher-order completion. The nonclosure theorem applies to the frozen
nearest-time physical generator family on the unrestricted off-shell
space; it is not a theorem excluding a larger gauge family or integer
gravity.

The integer displacement is a representation of a tangent direction,
not a claimed group action or new banked physical update. The proof does
not identify this finite model with Einstein-Hilbert gravity, an ADM
constraint algebra or native U. Public Canon's own restricted-model
qualifications are preserved in SOURCE.md.

The predecessor #1652 was reviewed separately at its own immutable pin
and result head. The new proof retains its valid local compatibility
identity while addressing the missing complete-global and constrained
variation tests. Its mismatching Phi/Pi public summary is not repeated
as an established result of either probe.
