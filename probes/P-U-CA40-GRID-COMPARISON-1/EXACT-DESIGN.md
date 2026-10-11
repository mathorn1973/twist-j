# Exact supporting audit for the local grid comparison

PUBLIC NON-CANONICAL conditional L1 engineering support.
P-U-CA40-GRID-COMPARISON-1.
Reservation: https://github.com/mathorn1973/twist-j/issues/1464.
Authority base: `37529581a5e0e111668f5f6501d633dbcbb3d2bc`.
Private mutable preparation. No scientific execution or candidate import
before the complete source pin and public readback.

## 1. Narrow purpose

The standalone standard-library verify.py audits the exact time matching,
shared-target triangle inequality, elementary interval-norm operations and
zero-safe engineering predicate used by the N256/N512 window comparison.
It imports no candidate, opens no files, uses no RNG or floating tolerances,
and emits one deterministic ASCII JSON line with explicit LF bytes.
Its functions do not execute merely by importing the source, but no import
is authorized before pinning either. Failures use explicit exceptions.

This is not a new theorem or Canon promotion. A fixture PASS is not a proof
of the C++ instruction stream, IEEE rounding behavior, actual propagator
accuracy, runtime performance or a complete error-closure result.

## 2. Frozen exact fixtures

Window enumeration uses the actual five-cycle active-label schedule, all
three labels (4,3),(4,4),(1,1), and both signs. It checks S=32 or16, the
four occupied-segment ordinals, prescribed coarse/fine within-segment
indices, every coarse/even-fine boundary match and the exact duration
1/20480000 second. Negative controls require two fine cells to have the
wrong duration and discarding the absolute segment offset to move the start.

The norm fixtures use rational realifications of complex-vector algebra.
For dimensions 2,4,8 and five deterministic inputs each, two unnormalized
approximations share a known unit-norm exact target. Independently valid
L1-majorized Euclidean error radii must imply the squared triangle bound.
Rational enclosing subtraction intervals, safe squares, outward rational
square-root enclosures and sums must contain the exact squared discrepancy.
Integer square root is used to construct rational enclosures without floating
approximations. These rational intervals are not a simulation of AVX errors.

Explicit boundary cases exercise COMPATIBLE, INCONSISTENT and UNRESOLVED.
Negative controls detect the naive positive lower square of a zero-crossing
interval, an underclaimed pair of error radii, and the false rule that an
upper distance bound above the error sum proves inconsistency.

Five growth fixtures check epsilon256<=2*epsilon512, including the exact
boundary, zero/zero, positive/zero and a strict failure just above the
threshold. No division or floating comparison is substituted.

## 3. Inventory derived from source, not observed output

| Family | Count |
| --- | ---: |
| Matched physical windows | 24 |
| Wrong-duration controls | 24 |
| Absolute-clock controls | 24 |
| Shared-target triangle cases | 15 |
| Rational norm-enclosure cases | 15 |
| Three-way classification/equality cases | 4 |
| Naive interval-square control | 1 |
| Upper-only failure control | 1 |
| Underclaimed-radius control | 1 |
| Zero-safe growth-screen cases | 5 |

This table predicts the fixture inventory only. It is not EXPECTED.txt and
asserts neither a successful run nor elapsed time. No inherited large
trajectory verifier is copied into this small supporting gate.

## 4. Runtime obligations outside the exact verifier

DERIVATION.md defines a separate local initial value problem for each window.
The two grids retain identical pulse/linear-history inputs and identical
absolute endpoints, while independently restarting the selected basis vector
as a computational test. This does not reproduce the physical nonlinear
state at a mid-pulse time and cannot be composed into a full trajectory.

The compiled campaign must supply both grids' stored endpoint vectors and
complete local component accounts in canonical window/case/column order.
The independent comparator must retain directed [d_lo,d_hi], the outward sum
S_up, and all 2880 three-way classifications. The runner separately applies
the exact binary64-to-Fraction twofold error-growth screen to every column.
No thermal average, normalization or phase fitting is admitted. Displaying
aggregate ratios must not replace the columnwise decisions.

Same-grid repeated endpoint/component byte disagreement and any cross-grid
INCONSISTENT result are fatal. UNRESOLVED prevents compatible-panel success
but allows the fixed remaining trials. A twofold growth-screen miss is
reported without cancelling the remaining trials. Speed has no fixed target.

The directed comparator's nonfinite and domain checks, safe zero-crossing
squares, all-component reduction, prescribed CPU/rounding environment,
source/input/binary custody, timeout handling and first-outcome preservation
remain implementation and runtime obligations. Passing these rational
fixtures does not satisfy those obligations automatically.

Compatibility and the factor-two growth budget are separate engineering
screens. Both may pass with uninformatively wide bounds. Neither establishes
the previous full-trajectory accuracy goal, a pair-coherence witness, a
hardware conclusion or permission for a long successor run. The preregistered
runner determines the finite resource limits and outcome disposition.
