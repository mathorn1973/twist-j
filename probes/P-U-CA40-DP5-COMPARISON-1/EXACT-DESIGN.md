# Exact support gate for the DP5 local comparison

PUBLIC NON-CANONICAL, conditional L1 numerical engineering.
Probe `P-U-CA40-DP5-COMPARISON-1`; reservation
[#1466](https://github.com/mathorn1973/twist-j/issues/1466).
Authority baseline `9bbb5e64ef852d82133cf94f5c31166b73d328b3`.
No scientific execution is authorized before the complete new public source
pin and its readback. This file specifies the gate; it is not a run record.

## 1. Inputs, independence, and executable scope

`verify.py` is a standalone Python standard-library program. It reads the
adjacent `dp5_tableau.hpp` as ASCII data. It imports no scientific candidate,
executes no C++ code, writes no files, and uses no randomness or network.
Its successful output is one deterministic sorted compact ASCII JSON line
with an explicit LF byte, emitted through `sys.stdout.buffer`.

The header provides `Q{numerator,denominator}` arrays `A[7][7]`, `B[7]`, and
`C[7]`, delimited by unique `BEGIN_A/END_A`, `BEGIN_B/END_B`, and
`BEGIN_C/END_C` comments. The parser accepts literal integer pairs with positive
denominators, checks 49+7+7 entries, and compares their mathematical values
with an independent exact transcription of the DP5 table.
It is a restricted data reader, not a C++ parser or proof that the compiler
uses those arrays correctly. Source review and runtime fixtures cover that
separate obligation.

This verifier was authored with the candidate method and intended result
criteria visible. It is independent supporting algebra, not a blinded
replication of the dynamics. The comparison/window/norm fixtures adapt the
preceding `P-U-CA40-GRID-COMPARISON-1` support verifier; new DP5 and Hermite
identities are checked directly with `Fraction` arithmetic.

## 2. Exact identities and expected finite counts

| Audit | Finite coverage |
| --- | ---: |
| Header coefficient entries | 63 |
| Base DP5 rooted-tree conditions, orders 1--5 | 17 |
| Two-half 14-stage composition conditions, orders 1--5 | 17 |
| Explicit non-order-six chain controls | 2 |
| Weight mutation preserving sum but breaking order two | 1 |
| Rational midpoint FSAL/composition fixtures | 6 |
| Wrong same-time stage reuse controls | 6 |
| Hermite cardinal value/derivative constraints | 36 |
| Monomials reproduced by quintic | 6 |
| Degree-six, derivative-scale, old-acceleration controls | 1 each |
| Matched three-arm physical windows | 24 |
| Wrong-duration and lost-absolute-clock controls | 24 each |
| Absolute DP halfstep stage times | 672 |
| Three-arm triangle and rational norm-enclosure cases | 45 each |
| Three-way classification/equality cases | 4 |
| Naive square, upper-only contradiction, underclaimed radius controls | 1 each |
| Zero-safe onefold upper-bound screen cases | 5 |

Rooted trees are generated recursively by adding one leaf and deduplicating
canonical unordered tuples. Counts by order must be `1,1,2,4,9`. Every tree
weight is compared with its reciprocal density. Row sums and explicitness
are checked for the base and composed tableaux. The sixth-order chain is
`1/600`, not `1/720`, for DP5 and `161/115200`, not `1/720`, after two halfsteps.

The six FSAL fixtures use a rational nonautonomous scalar equation and
compare the shared-stage two-half calculation against both an unshared
calculation and the composed tableau. This is not the physical generator.
The reuse count is 13 logical stage evaluations. An extra fixture evaluation
performed for checking an identity is not a performance measurement.

The Hermite coefficient formula is checked against independent expanded
cardinal polynomials, then against every monomial through degree five.
The degree-six error at `theta=1/4` must equal `9/4096`.
Derivative data are scaled by the full cell width `h`, not by `h/2`.

The local comparison fixtures cover all three pairs of rational vectors
around a shared unit target, in real dimensions 2, 4 and 8 (including
realifications of complex vectors). Their rational enclosing square and
square-root operations do not emulate any particular binary64 instruction.

## 3. What the exact gate does not establish

A PASS establishes only the displayed algebraic support identities and
their linkage to the rational header. It does not establish:

- accuracy or stability of the compiled DP5 trajectory;
- correct floating implementation of the tableau or Hermite formula;
- directed AVX/MPFR arithmetic, thread placement, or absence of migration;
- the validity or size of a particular runtime residual enclosure;
- bitwise repeatability, faster execution, or either engineering screen;
- physical realization, a complete-pulse error, or final source/reference
  coherences.

The stored polynomial has six finite dyadic coefficients. Its exact initial
coefficient is the copied initial vector; final endpoint mismatch is charged
as a jump. The full-space residual proof accepts any such polynomial.
Changing its generator from RK4 to DP5 does not require a new residual
inequality. It does require recomputing every coefficient-dependent bound.
The theoretical fifth-order scaling is not a substitute for that computation.

## 4. Frozen numerical companion and decisions

Arm A is RK4/N512, B is RK4/N256, and C is two-half DP5/N256.
All use the unchanged pulses, four windows, both angles, six cases, `L8/G10`,
and the same 120 basis columns. C has 256 certificate cells but 512 DP5
substeps per original segment. No adaptive search is allowed.

Six children execute in order `A B C C B A`, at most 300 seconds each.
After each completed triple all three pairs are compared, at most 90 seconds
per comparator. The total budget is 1,800 seconds; each launch is further
limited by the remaining total budget. Complete outcomes and partial failures
are retained before any acceptance decision. There is no retry or automatic
long run.

For each pair and each of 2,880 columns, use the directed distance interval
and upward sum of the two individual certificate radii:

- `d_lo > radius_sum_up`: `INCONSISTENT`, a fatal comparison failure.
- `d_hi <= radius_sum_up`: `COMPATIBLE` for this local target.
- Otherwise: `UNRESOLVED`; never silently convert this to compatibility.

Within-arm repetitions require exact equality of the frozen deterministic
payloads; a mismatch is fatal. Different arms are compared by enclosures,
not by byte equality and not by a fitted global phase.

The bound screen is the zero-safe exact comparison `epsilon_C<=epsilon_A`
for every column in both matched triples. Its failure is preserved separately
from compatibility. It compares upper bounds and establishes no inequality
between the unknown true errors. B/C comparisons are descriptive controls.
The speed screen separately requires the median end-to-end C time to be
strictly less than A, using the two retained observations for each arm.
Insufficient data leave the corresponding decision incomplete.

## 5. Custody and later verification

Freeze all declared sources, the actual rational header, and the input in
one immutable public source pin before running `python verify.py` or any
scientific candidate. The coordinator records source hashes, readback time,
compiler/flags, binary hashes, commands, outcomes and raw-output receipts.
The first exact stdout becomes `EXPECTED.txt`; `RUN.md` records its custody.

Numerical endpoints, individual bounds, comparisons, repetition records and
timings are retained separately. Public reports use reviewed compact data.
No complete interior polynomial archive is promised: the certificate is
computed online, and a full independent reconstruction would require replay
from the frozen inputs. Same-session review is not external replication.
The formal exact replay and the floating engineering campaign remain distinct.
