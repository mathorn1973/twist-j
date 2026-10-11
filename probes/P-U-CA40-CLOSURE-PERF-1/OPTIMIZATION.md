# Low-copy equivalence and short performance contract

PRIVATE PREPARATION. Proposed P-U-CA40-CLOSURE-PERF-1.
Reservation: #1462.
Base: `264d792eb433c9a032f6282b3c7800ee1837f73b`.
No execution is asserted here.

This note proves the reviewed low-copy change from the sealed BALL kernel
`e84a7071fcbd10461bbce54e30638ecd68845fe0cc0a901e827be0d2bd9cfee8`
to the private kernel
`9ba07011d2405e609eb84be8cb5d7781bb06b7cc50be53fbd5304ac5fa93c3f2`.
The preceding BALL attempt completed no configuration and remains
NOT_CERTIFIED. This proposed short comparison cannot replace that missing
result. The performance harness and all final source identities require
their own public pin before execution.

## 1. Claim and explicit premises

The change eliminates copies and redundant zero writes and evaluates a
supported polynomial in its actual support. It changes neither the
mathematical model nor the ordered nonzero floating operations. Under the
following premises, the baseline and optimized paths produce identical
binary64 endpoint components and identical per-column partial-account
fields, including guard, tail, continuum, jumps and total. No relative or
absolute numerical tolerance is needed or permitted for this regression.

The premises are the same prepared node/interval bytes, mode and basis
ordering, initial columns, cell order, SIMD lane assignment and constants;
the same compiler/platform/library and frozen non-FMA, no-fast-math
contract; binary64 nearest rounding for centers, the prescribed embedded
directed arithmetic for bounds, gradual underflow, no FTZ/DAZ, and finite
operands/results. The 80-thread schedule may differ because columns do
not share arithmetic reductions. Coefficient preparation and model data
must be immutable and identical in both variants.

This is a conditional trace-equivalence proof, not a claim that source
inspection validates arbitrary compiler behavior. Actual bit comparisons
and the retained runtime arithmetic checks test the selected build. A
compiler, operation-order or descriptor change outside this diff requires
its own review; no measured speedup is assumed.

## 2. Displacement copies and ownership

For both candidate and ball displacement, the baseline copies x into
term before the first annihilation action. The optimized form evaluates
that first action directly from x into term. In both forms the action
reads exactly the same center/coefficient bits, traverses modes and row
summands in the same order, and writes the same output bits. For a ball,
the same input e and N enter the unchanged scalar recurrence.

Subsequent actions use two distinct buffers and the same ping-pong swaps.
At the end, replacing `out=term` by an ownership swap transfers the same
center bits; the ball swap also transfers its e and N arrays. The former
out storage becomes scratch and is overwritten before being read as a
new action's input. The Gaussian scaling remains in the same position.

The explicit exclusions are x!=out and neither x nor out may be term or
temp. Distinct owning vectors have disjoint storage. Every current call
site satisfies these exclusions. No in-place triangular action is proved
here: allowing one could read already overwritten input and invalidate
the equivalence. The auxiliary collective/interval reference paths are
unchanged; candidate half storage still used by the collective fixture
is not repurposed.

## 3. Partial zeroing and the annihilation tail

Creation writes every guard row and both real/imaginary parts. Its old
pre-zeroing therefore had no effect on any subsequently read value and
can be removed. Annihilation writes every row in its supported prefix;
its untouched guard complement must still be set to positive zero in
both real and imaginary blocks. The optimized code clears exactly that
complement. Thus a reused output cannot retain a stale guard value.

After all seven annihilation actions, the baseline copied term to half
only to compute grade norms and the tail allowance. The optimized form
computes those same grade norms and reads the same e directly from term,
before any creation action. It preserves the exact grade order and
directed sums in

```text
tail <= sum_j t_j ||P_j center||_up + sqrt_up(sum_j t_j^2) * e_half.
```

No contraction is attributed to the annihilation half. Deleting a copy
does not remove its uncertainty or change the infinite creation-tail
bound. Evaluating the grades after creation would be a different and
invalid substitution; the implementation explicitly evaluates them
first.

## 4. Supported dual Horner and unchanged metadata

Every stored quintic coefficient lies in P_L. Write d=dim(P_L) and
g=dim(P_G), with the basis ordered by occupation degree. The compact
value and derivative arrays use d in their real/imaginary layout. The
same descending coefficient order is used, and derivative Horner reads
the old value before updating the value:

```text
derivative <- theta*derivative + old_value;
value      <- theta*old_value + coefficient.
```

Each supported component therefore receives exactly the same sequence
of non-FMA products/additions, including all signed-zero behavior of
that component. The actual Gauss-node centers satisfy theta>=0, and the
endpoint check uses theta=1; the derivative scaling 1/h is positive.
The baseline's unsupported components start at +0, have +0 coefficients
and remain +0 through these operations. Exact zero-extension of the
compact result recreates precisely these complement bits.

The compact arrays deliberately still pass g to the rounding allowance
routine. Consequently the original U_G and every gamma, scalar interval,
e recurrence and propagated N recurrence remain unchanged. This is a
conservative allowance for fewer component operations, not a reduced
roundoff model. Coefficient norms are computed in P_L in both versions.

The final directed norm reduction traverses the supported occupation
rows in the same order, real then imaginary for each row. The baseline
then adds squares of complement zeros. Those additions are exact and
leave every finite nonnegative partial sum unchanged, under either
directed rounding; a zero sum remains +0. Thus compact btighten(d)
produces the identical norm bits. The exact embedding copies center,
e and N and fills both complement blocks with +0.

## 5. Consequence for the partial account

Induct over the ordered cells. The unchanged candidate generator and
Hermite operations give the same endpoints and dyadic polynomial
coefficients. Sections 2--4 give identical Gauss-node value/derivative
balls, displacement/ladder actions, residual balls and tail bounds.
The unchanged sixteen-node directed sums therefore produce identical
guard and tail increments. Polynomial norms and the ellipse expression
produce identical continuum increments. The endpoint jump uses the same
polynomial, actual saved endpoint and ball subtraction, so its increment
is also identical. Accumulation preserves all these identities.

The claim includes the final partial total, maximum-node and norm-drift
diagnostics, and sampled time/projection/arithmetic node diagnostics.
The last arithmetic diagnostic is already part of the guard bound and
must not be added again. Schedule order changes wall time and telemetry,
not these per-column fields. The proof does not compare elapsed times,
thread scheduling records, addresses, executable hashes or JSON ordering.

## 6. Frozen short panel and exact acceptance

The proposed panel uses L8/G10/N512, all six prescribed branches, all
120 unnormalized thermal columns, and exactly the first four occupied
cells from each branch's original prepared cell sequence. Their absolute
times, node intervals, alpha/phase prefixes and pulse coefficients are
unchanged. Starting at the first occupied cell does not reset the clock.
The full 500-microsecond trajectory is not propagated.

Use 80 threads and the prescribed singleton placement. Run three fresh
baseline children B and three optimized children F, in the fixed order
`B,F,F,B,B,F`. Each child is limited to 300 seconds; the total campaign
budget is 1800 seconds. Preserve incomplete/failed records and do not
retry, change the panel, or extend the budget to obtain a favorable
measurement. Preparation, kernel and end-to-end times remain separate.
The frozen kernel/propagation window starts before the OpenMP region and
ends after it: it includes workspace allocation, thread startup, barriers,
task scheduling and progress logging as well as Hermite/certificate work.
It excludes model preparation, supporting fixtures and final serialization.
It is not a measurement of arithmetic instructions alone.

The regression gate requires all six invocations to finish their entire
panel, pass the frozen runtime fixtures and placement/custody checks,
and contain finite complete output. In canonical case/thermal-column
order compare all final prefix endpoint binary64 words and every partial
account field listed in Section 5 across all six runs against the first
baseline. Compare IEEE-754 words or canonical little-endian binary
receipts, preserving signed zero; parsed numeric equality alone is not
the criterion. Byte counts and SHA256 receipts accompany the artifacts;
direct byte comparison is preferred when all files are available.

Any differing bit is REGRESSION_FAILED. It is not excused as small,
normalized away, or replaced by a tolerance. An incomplete child gives
an incomplete comparison, not an equivalence pass. The mathematical
argument predicts equality under the premises, but the first campaign
must still observe it. Each harness must apply identical prefix limits
and instrumentation to baseline and optimized versions; this proof
does not authorize asymmetric harness changes.

After the exact regression gate passes, report median baseline kernel
seconds divided by median optimized kernel seconds, all six raw timings,
and separate preparation/end-to-end summaries. The performance gate is
median baseline propagation time divided by median optimized propagation
time at least 2.0, after the exact regression gate passes. Timing medians
are observations on
this short workload, not a guaranteed full-run acceleration. Passing the
panel authorizes no automatic long run and certifies neither a final
coherence interval nor either angle's total trajectory-error radius.
