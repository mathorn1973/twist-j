# Independent breaker contract

Candidate: **C-J-CLOSED-WORLD-READ-CAPACITY-N**, NON-CANONICAL L1 notes only.

This is a code-independent, result-exposed audit. The independent author read
only the frozen `PREREG.md` and `PROOF.md` at public definition/proof commit
`f48598b4c2e7c32423ca54f288be3ffbb5db3e73` before writing `break.py`. Their SHA-256
values supplied for those exact local bytes were respectively
`33da6e2fc870a6006c0e71407c64e52028e01154212d88cdc10876be244a9802` and
`8aad28c0104c2059d3f2e5720760b5af47b65d4b354ca9a987a2ef313db7c9f9`.
No builder code, `verify.py`, or outputs were inspected. A parallel textual
proof review had the same two-document boundary. No scientific execution or
import was performed while preparing this contract and implementation.

## Frozen comparison domain and independent methods

1. Emit exactly 288 `CENSUS` JSON lines: units `J`, `phi^-1`, `z`, `J^2`;
   horizons 1 through 12; alphabet sizes 2 through 7. Deterministic JSONL
   records include `unit,m,n,F,P,possible,c` and finite-row cycle data. Infinite
   quotient rows use the string `INFINITE` for both `F` and `possible`, with
   null `P,c,witness`. They are not finite zero-cardinality or negative rows.
2. Multiply four integer coefficients by convolution and direct reduction
   using the cyclotomic relation. Compute the norm of `u^n-1` as a Sylvester
   resultant, with its determinant evaluated by the signed permutation sum.
   Do not form a multiplication matrix, import builder arithmetic, use a
   numerical eigenvalue routine, or use floating point. Zero elements are
   recognized before assigning any finite norm cardinality.
3. Obtain exact-period state and word counts by subtracting all proper-divisor
   exact-period counts from the fixed counts. This is an independent divisor
   partition inversion. Require nonnegativity and divisibility by the period.
4. Decide full finite feasibility. At `c=n`, the proved construction is used
   only when `C_n>=m^n`. Otherwise every positive integer `c` up to the minimum
   of the cardinality bound and primitive-cycle bound is searched. A zero
   bound is an exact exclusion. The search lists every integer pattern for
   one target necklace, and then every nonnegative integer multiplicity of
   those patterns, with the multiplicities summing exactly to the target
   necklace count. Every source capacity is enforced. The only search pruning
   is exact resource exhaustion, empty pattern sets, the two necessary bounds,
   and coordinatewise necessary lower bounds from the remaining patterns.
   Memoization and pattern ordering do not alter the domain.
5. Grouping patterns is exact: any individual-necklace assignment induces its
   pattern multiplicities. Conversely, an integer multiplicity vector can be
   distributed among that many distinct necklaces of the same period because
   they have identical constraints. Distinct source cycles can then be assigned
   from the available inventory. Every positive result is separately checked
   for necklace coverage, integer contribution `c`, all source capacities, and
   total support size `c*m^n`. Negative search records list every tested `c`;
   values above the primitive bound have an exact necessary exclusion.
6. Compute the frozen sufficient onsets for `|k|=1,m=2` and `|k|=2,m=2,...,6`.
   Verify both integer inequalities, the first-hit property, and both exact
   monotonicity premises. Independently compute norms and primitive counts
   for each relevant unit at every horizon `n_star,...,n_star+12`, asserting
   `P_n>=n*m^n`. Relevant units are `J,phi^-1` at `|k|=1`, and `J^2` at `|k|=2`.
   Also compute the proof's first positive exclusion onset for `|k|=1,m=3,...,7`
   and `|k|=2,m=7`, with strictness, minimality, and monotonicity checks.
7. Check the minimal Lucas stride for each denominator `2,5,16,256`, including
   the immediately previous stride when one exists. Exposed expected strides
   are `1,2,3,6`. Exposed J fixed/primitive counts through horizon five are
   asserted explicitly, as are the negative binary rows at horizons one and
   five and independently certified support sizes eight and twenty-four at
   horizons two and three.

## Independent finite controls

The breaker does not duplicate the builder's full quotient enumeration through
horizon eight. It has the following separate controls.

* For each finite `z` quotient through horizon twelve, explicitly identify its
  five residue representatives with the coefficient-sum map to F_5. Check
  multiplicativity on the basis, vanishing of the relation under the map, and
  resultant norm five. The onto map's kernel and relation ideal have the same
  index, certifying their equality. Enumerate the five representatives and
  their identity tick. Singular multiples of five remain `INFINITE`.
* Independently exhaust every labeling/exclusion choice on all permutations
  of one through four states and on one canonical permutation for every
  integer partition of one through eight states. Compare every possible `c`
  against the allocation solver for alphabets two and three and horizons one
  through four whenever all source cycle lengths divide the horizon. A direct
  cardinality exclusion skips label enumeration only when the total number of
  states is smaller than the required number of words. The brute-force path
  checks invariant supports and actual word histograms, without using the
  allocation criterion. Identical permutations are deduplicated.
* Explicitly enumerate the four length-two windows of the binary four-cycle
  labeling `0011`; these are all four words once. This control does not require
  the window length to equal a global period. Check the cardinality obstruction
  for a single full-N cycle for N=1,...,12; the general statement is the elementary
  inequality `N<2^N<=m^N`, not a blanket prohibition on rotation windows.

## Textual adversarial proof review

No mathematical counterexample or invalid implication was identified in the
frozen proof. The fixed-point kernel calculation uses domain cancellation and
ideal divisibility, so it does not assume a PID. The cycle criterion is exact,
and constant output necklaces can legitimately be supplied by longer cycles.

For the sufficient onset, put `A=Q/(2m)` and `B=Q^2/(4L)`. The first step ratio
is nondecreasing when `n>=1/(A-1)=2m/(Q-2m)`. The second is nondecreasing when
`n>=3/(B-1)=12L/(Q^2-4L)`, using
`(1+1/n)^2<=1+3/n`. The two frozen inequalities give
`q^n>=32*n*m^n` and `q^n>=512*n*L^(n/2)`, respectively, yielding the claimed
primitive bound. These algebraic arguments provide the tail; finite computed
checks do not replace them. For exclusion, `rho<L` implies `rho^-1>1/L`, so
`rho<L-1/L`, and the integer ratio is strictly increasing for every `m>=L`.

The rational denominator argument remains valid with zero probability entries:
for each prime dividing `b`, a positive numerator coprime to that prime exists,
and its constant word forces that prime's full exponent in `b^n`. Lumping the
fair refinement supplies the stated eventual converse. Equality of integral
alphabet size with `rho` cannot arise.

An important scope boundary remains explicit: `INFINITE` marks an excluded
finite-quotient experiment. It does not assert that no finite invariant subset
of O can support any reader. Nor does the finite-cycle argument prohibit
independent shorter windows on a sufficiently long labeled rotation cycle.
No infinite compatible process, physical sampling mechanism, all-state
preparation, native implementation, Canon authority, or layer lift follows.

## Freeze and execution policy

Publish this contract and the complete code, then read back the public bytes
and record their SHA-256 before scientific execution. Before that pin, only
textual review, syntax parsing and repository integrity checks are permitted;
do not import this module. Run with Python standard library, fixed
`PYTHONHASHSEED=0`, `LC_ALL=C`, no network, no floats and no randomness, with
at most 2400 seconds. Preserve the first stdout, stderr, exit status and timing.
An implementation/integrity failure is STOP; do not repair and resume this
same candidate. Retain a mathematical mismatch at its exact scope. This is
code independence, not two-architecture independence.
