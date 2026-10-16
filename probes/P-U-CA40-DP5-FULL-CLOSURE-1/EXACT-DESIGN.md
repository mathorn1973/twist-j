# Exact supporting audit for the full DP5 pulse

PUBLIC NON-CANONICAL. Conditional L1 theory and numerical evidence.
Original work Apache-2.0, A. M. Thorn, 2026-10-12.

```text
probe_id: P-U-CA40-DP5-FULL-CLOSURE-1
reservation: https://github.com/mathorn1973/twist-j/issues/1472
authority_base: 5f54015ed8361e3a64cb10894397020ddfadd104
```

The standard-library verifier checks exact supporting identities and small
negative fixtures. It does not integrate the ion model, emulate IEEE arithmetic,
read numerical results, or predict whether the full trajectory meets its error
target. A passing exact gate and a valid numerical certificate are distinct
requirements. This is a result-exposed continuation of earlier probes, not a
blinded or independently implemented numerical replication.

## 1. Program boundary and source custody

`verify.py` uses `fractions.Fraction`, integer arithmetic and integer square
roots. Its only data read is the adjacent ASCII `dp5_tableau.hpp`. It imports no
candidate module and performs no network operation, random sampling, timing
experiment or file write. Its sole successful output is sorted compact JSON
encoded as ASCII followed by one explicit LF through `sys.stdout.buffer`.

Freeze the fourteen files listed in PREREG.md and their source manifest by a
public commit and byte readback before the first scientific execution. The
first exact gate has a separate 600-second limit, preceding the numerical
runner. Preserve its actual exit code, stderr and stdout. Create EXPECTED.txt
only from that first actual output; the inventories below are descriptions of
the source, not a substituted or predicted EXPECTED result.

No successful execution is asserted by this design document. The inherited
mathematical coefficients and their primary attribution are described in
DERIVATION.md. The gate uses an independent transcription of coefficient facts;
it is not a second floating implementation of the ion dynamics.

## 2. Actual tableau and order identities

The restricted parser requires unique BEGIN/END markers, the declared array
shapes, literal `Q{numerator,positive_denominator}` entries and no additional
payload tokens inside each initializer. It reads 49 A entries, seven B entries
and seven C entries and compares all 63 with the verifier's transcription.
This is a deliberately narrow source-format check, not a C++ compiler proof.

The rooted-tree generator checks its inventories of 1, 1, 2, 4 and 9 trees at
orders one through five. For each of those 17 trees, it tests the exact Butcher
elementary weight against the reciprocal tree density. It repeats all 17 checks
for the fourteen-stage representation of two consecutive halfsteps. Both
tableaux must have the correct nonautonomous row sums and explicit triangular
structure. The actual endpoint row equals the weights, with final weight zero.

Two order-six chain witnesses prevent an order-six claim: their weights are
1/600 and 161/115200, respectively, instead of 1/720. A weight mutation preserves
consistency but violates the order-two condition. These are formal order facts;
they do not bound a particular step's truncation or floating error.

Six rational nonautonomous ODE fixtures test actual midpoint endpoint reuse.
Two halfsteps with the correct midpoint derivative agree with unshared and
composed evaluation and require thirteen RHS calls. Six same-time, wrong-state
stage substitutions fail. No FSAL reuse across physical cells or discontinuous
segments is authorized by this fixture.

## 3. Quintic reconstruction

Independent expanded cardinal polynomials check all 36 value/derivative
constraints at normalized coordinates 0, 1/2 and 1. The implementation reproduces
all six monomials of degree at most five. A degree-six counterexample has the
specified nonzero residual at 1/4. Further controls detect derivatives scaled
by the halfstep instead of the full certificate cell and the older centered
acceleration artifact.

These checks establish the rational reconstruction formula. The numerical
certificate must still use the six actual stored dyadic coefficients, verify
that the constant coefficient equals the incoming state, and charge the
polynomial-to-stored-endpoint jump. Exact Hermite algebra alone establishes
neither bitwise implementation equivalence nor a full-space residual bound.

## 4. Full piecewise clock and carried state

The geometry fixtures cover both signs and labels (4,3), (4,4), (1,1) through
all eighty original segments of duration 1/160000 second. They check contiguous
absolute times and a common endpoint 1/2000 second. Across six cases there are
480 segments: 128 active and 352 inactive, with 49152 occupied certificate cells.

The affine DP5 stage-clock formula is checked at the first and last cell of
each active segment: 3584 stage positions. The formula places every interior
cell's nodes in that same segment; the verifier does not enumerate every stage
of the compiled trajectory. It checks the derived inventories of 737280
eight-column cells, 9584640 RHS calls, 11796480 Gauss nodes, 7290 snapshots,
7200 segment carries and 5280 inactive task-segments. Inventory arithmetic is
not evidence that those operations have occurred.

Six short rational unitary chains produce 24 checkpoint fixtures and eighteen
state-and-budget carry checks. Their accumulated local defects bound endpoint
error without a stability exponential. Controls distinguish state reset,
certificate reset, aliased mutable snapshots, a wrong incoming polynomial
constant and summing cumulative budgets more than once. A separate control
records that increasing upper bounds do not prove increasing actual error.

The analytical extension to the full model is the piecewise unitary Duhamel
argument in DERIVATION.md. Finite amplitude jumps require a fresh right-side
derivative but no state jump. Inactive intervals carry the moving-frame state
and its existing certificate unchanged. They cannot erase earlier error.
This identity refers to the declared compensated parent; a raw-parent unary
phase is not silently omitted.

## 5. Thermal labels and final pair accounting

Graded compositions give 1+7+28+84=120 initial columns. The exposed column 36
remains (0,0,0,0,0,0,3), with weight 20^7/21^10, in both sign groups. Off-by-one,
reversed-mode and K=2 omission controls protect that identity. No exposed column
receives an exception from the full-run account.

The exact retained mass uses unnormalized weights

```text
p_n = (20/21)^7 (1/21)^|n|,  |n| <= 3,
p_tail = 680046581 / 794280046581.
```

A nonunit approximate-endpoint fixture attains Gram error 11/25. It rejects
the unsafe replacement by the sum of two state errors, which would be 2/5.
The weighted account has no extra thermal-rank multiplier. Missing thermal
coherence contributes p_tail once, hence p_tail/2 to the selected Bell-input
half-distance. A relative-unitary fixture detects omitted frame restoration;
it is not a replacement for the full Weyl-phase proof or runtime restoration.

The gate checks the six within-sign pairs, arithmetic-halfwidth accounting,
three exact square-root-affine comparisons and equality-sensitive threshold
fixtures. The squared comparison must first establish a nonnegative difference.
The arithmetic halfwidth belongs in the reported total radius; the already
interval-valued center is expanded only by numerical plus thermal error.

Precision and discrepancy are separate: all six total radii must be at most
exactly 1/1000 for the precision goal. A discrepancy interval is above target
only when its lower endpoint is strictly greater than 1/1000, and at or below
when its upper endpoint is at most that value. An overlap is unresolved.
One resolved above-target pair per sign suffices for the stated selected-pair
discrepancy conclusion; it does not imply that all three pairs per sign differ.
Narrow/distinct and wide/distinct fixtures prevent conflating these decisions.

## 6. Checkpoint commit fixtures and runtime obligations

The declared checkpoint payload is 824448 bytes: eight endpoint columns in
dimension 6435, followed by twelve binary64 components per column. All 7290
payloads occupy 6010225920 bytes. Abstract fixtures distinguish a complete
payload plus marker from an orphan, missing payload, truncation or a hole in
the committed checkpoint sequence. Five inactive carry fixtures and a reset
control preserve both state and budget.

These Boolean and rational fixtures do not test filesystem atomicity, crash
durability or actual checkpoint bytes. The numerical harness and runner must
check the real layout, finite data, incoming-state identity, cumulative
monotonicity, inactive carries, complete markers, final-snapshot agreement and
source/input/executable custody. Complete snapshots are distinguished from
uncommitted partial writes. Progress logs alone cannot establish completion.

The floating run must additionally establish its arithmetic fixtures, directed
model enclosures, guard and infinite-tail account, continuum remainder,
endpoint jumps, common-time restored coherences and exact saved aggregation.
The full trajectory is not certified by this verifier's PASS field. The
verifier explicitly reports that numerical accuracy, performance, IEEE
emulation and a full-trajectory certificate have not been established by it.

## 7. Numerical outcome and limits

The one numerical attempt follows PREREG.md: DP5/N384, L8/G10, all six cases
and 120 thermal columns through the same 500-us pulse, eighty fixed workers,
86400 seconds including preparation and validation, with a 300-second internal
postprocessing reserve. Preserve the first complete, unresolved, negative or
incomplete outcome. A timeout does not relax a threshold or authorize a retry.

The certificate is online. Source/input/binary hashes, snapshots, endpoints
and bound components are retained, but all intermediate quintic/node arrays
are not archived. Independent re-audit of those intermediates requires
deterministic replay. Exact CI replay is not such numerical replication.

Even a successful full selected-pair account concerns the fixed compensated
harmonic model. It establishes no experimental Ca40 implementation, physical
spectator imperfection bound, all-input channel norm or informative contact
that preserves an arbitrary complete source. There is no Canon promotion.
