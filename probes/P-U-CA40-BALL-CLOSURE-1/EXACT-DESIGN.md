# Exact supporting audit for norm-ball error closure

PUBLIC NON-CANONICAL. Conditional L1 mathematical design.
Original text Apache-2.0, A. M. Thorn.

Probe: `P-U-CA40-BALL-CLOSURE-1`.
Reservation: https://github.com/mathorn1973/twist-j/issues/1460.
Authority base: `c2459261aa15552e6560753dd8e1753f5164972d`.
This is mutable source preparation until its own public immutable pin.
No scientific execution or candidate import has been performed for this
draft. The source pin, first exact stdout and actual numerical outcomes
must be recorded after they exist; none is predicted here.

## 1. Why the exact gate is separate

The predecessor, `P-U-CA40-ERROR-CLOSURE-1`, completed its small exact gate
but produced no completed numerical configuration before a manual resource
stop. Its pin `3440928c77239bd26907a52810db7ec611f134d8` and incomplete
record are unchanged. This new identifier proposes a cheaper arithmetic
representation for the guard residual. It does not repair or resume the
spent predecessor, assert a speedup, or supply its missing certificate.

The new candidate keeps an ordinary binary64 center vector, its rigorous
Euclidean norm upper bound, and a scalar error radius for each thermal
column. Small interval coefficient tables and directed scalar arithmetic
must account for uncertainty and floating arithmetic. The full-space
Duhamel argument, analytic guard tail, continuous-time remainder, stored
endpoint jumps and nonnormalized thermal/Gram account remain necessary.

`verify.py` checks exact rational supporting identities and counterexamples.
It does not read numerical results, MPFR tables, compiled instructions or
trajectories. It is not a numerical predictor, a compiler test, an interval
library test, or an independent execution of the proposed certificate.
Its output marks each of these limits explicitly. The actual certificate
must come from the separately frozen runtime and its preserved evidence.

The new Schur and rounding arguments use standard matrix norm and floating
error algebra, derived explicitly below. They are not novel general
theorems about quantum dynamics or numerical analysis.

## 2. Inherited exact checks

The guard/defect/Gauss/budget code is adapted from the predecessor's exact
verifier, which in turn credits the SINUS-COMPARISON-1 rational Fock helpers.
The unnormalized Fock basis has metric n!, so square roots are avoided in
the exact finite displacement coefficient comparisons. These finite
fixtures retain their original limited meanings:

- Normal ordering against independent combinatorial coefficients and a
  larger ambient restriction: 16 columns and 300 entries.
- Creation-shell factorial bound: 25 fixtures, including saturation in an
  aligned one-mode example; decreasing geometric ratios: 117 fixtures.
- Cubic reconstruction and exact-dyadic endpoint correction; the actual
  candidate uses quintic Hermite reconstruction, whose value, derivative
  and second-derivative endpoint identities are checked separately.
- A derivative zero at three sample nodes nevertheless integrates to
  1/840, above 1/1000. Sampled small defects are not a continuum certificate.
- Three-node Gauss algebra over Q(sqrt(15)), six exact moments and the
  vector-polynomial squared-norm identity; positive-weight interpolation
  stability and the factor four in the analytic remainder. This does not
  certify the actual sixteen nodes or their MPFR root enclosures.
- All 120 K=3 thermal weights, exact omitted mass
  `680046581/794280046581`, the pair half-distance convention and rational
  decision toys. These toys do not predict either angle's output.
- The nonnormalized Gram counterexample: approximate scalar endpoints 6/5
  have individual error 1/5, but Gram error 11/25 exceeds 2/5. Approximate
  endpoint norms cannot silently be replaced by one.

The Gaussian displacement prefactor stays formal in the exact Fock
fixtures. No transcendental Gaussian, phase or continuum bound is
numerically certified by these tests.

## 3. Schur majorants and short chains

For a nonnegative entrywise majorant B of a complex matrix T, let

```text
R = max_i sum_j B_ij,   C = max_j sum_i B_ij,
S(B) = sqrt(R C).
```

Weighted Cauchy-Schwarz in each row gives

```text
sum_i |sum_j T_ij x_j|^2
 <= sum_i (sum_j B_ij)(sum_j B_ij |x_j|^2)
 <= R C sum_j |x_j|^2.
```

Thus S(B) bounds the Euclidean operator norm. The same bound applies to
every shorter principal occupation chain and to their direct sum. A
factor depending on the number of total-number basis states is unnecessary.
This does not remove the dimension-dependent absolute underflow allowance.

The exact verifier uses rational complex matrices, basis and mixed vectors,
and evaluates both inequalities separately. Rational component l1 values
may majorize complex entry magnitudes without square roots. Repeating a
block five times preserves the same operator bound. A two-row single-column
matrix of ones falsifies using only the maximum row sum as its 2-norm bound.

Complex arithmetic can be regarded as a realified matrix. Its entrywise
absolute 2-by-2 blocks have row/column sums |Re a|+|Im a|. Since
`(|Re a|+|Im a|)^2 <= 2|a|^2`, a safe bound is sqrt(2) times
S(|T|). Dropping this realification factor is explicitly falsified.
Small rational fixtures do not establish that the runtime constructed the
right high-dimensional chains or the right coefficient table.

## 4. Operational center and radius contract

For one thermal column, store center xhat and outward bounds

```text
N >= ||xhat||,     r >= ||x_true - xhat||.
```

The center consists of exact stored dyadic values. It is not itself an
asserted approximation with an unrecorded tolerance. Let Chat be the exact
stored small coefficient matrix actually used by the center kernel. Let

```text
S >= ||Chat||,
E >= ||C_exact - Chat||,
rho N + U >= ||fl(Chat xhat) - Chat xhat||.
```

The complete simple recurrence is

```text
r_new <= (S+E)r + (E+rho)N + U,
N_new <= (S+rho)N + U.
```

It follows by adding/subtracting C_exact xhat and Chat xhat, then using
the triangle inequality. E includes mathematical/model/node uncertainty
and coefficient-center generation rounding. The stored-center norm
recurrence does not need E, because the center action uses Chat.
Conversely, the true input-radius term requires E*r. For xhat=0, r=1,
Chat=1 and C_exact=2, omitting this term reports radius one instead of two.

The verifier checks this recurrence using rational complex operators,
coefficient perturbations, input perturbations and explicit local arithmetic
errors. A further check combines it with the rounding-law fixture below.
No intermediate state is normalized.

The full true projected displacement has norm at most one. This can
sharpen propagation of its original input ball if the complete suffix
argument is implemented. It does not make each triangular factor,
annihilation half or local-error suffix contractive. The exact fixture
uses A=[[1,3],[0,1]] and A inverse: the total product is the identity,
while either relevant factor sends (0,1) to norm sqrt(10). It also checks
the exact telescoping input/local-error decomposition. The planned simple
factor-by-factor recurrence remains valid, although potentially looser.

The nonunitary annihilation-half radius must be retained for the analytic
outside-guard tail. A grade norm is bounded by its directed center norm
plus a valid half-action radius. The final displacement contraction must
never replace that half-action bound.

For nonnegative tail weights t_j, a sharper valid error contribution is
`sqrt(sum_j t_j^2) r_half`, because the occupation grades are orthogonal
and Cauchy-Schwarz bounds `sum_j t_j ||P_j error||`. Exact rational
fixtures include saturation and reject replacing this factor by max_j t_j.
The center contribution still uses its actual weighted grade norms.

## 5. Rounding and gradual-underflow obligations

The agreed center operation contract is round-to-nearest binary64,
no FMA contraction, no overflow, finite operands, and gradual underflow.
Write u=2^-53 and eta=2^-1074. The safe elementary model is

```text
|fl(z)-z| <= u |z| + eta.
```

A complex row starts with its exact diagonal copy. Each off-diagonal term
uses two real products, a signed sum and an accumulator addition per
component. With q_max bounding the off-diagonal term count, use

```text
k = 4 q_max + 8,    k u < 1,
gamma = k u / (1-k u),
rho = sqrt(2) gamma S,
U = sqrt(2D) k eta / (1-k u).
```

The longest relative-error path is at most q+2 and each real row performs
at most 4q operations, both bounded by k. Expanding products of relative
perturbations gives the gamma bound. Every additive eta term is amplified
by at most k subsequent relative factors; their geometric upper envelope
gives U. D counts complex outputs for one thermal column. Eight SIMD lanes
are eight independent columns and do not introduce another sqrt(8).

Exact Fraction fixtures check positive/negative relative-error products,
the path/operation-count domination, and nonzero absolute allowances for
seven q_max choices and three dimensions. The subnormal midpoint eta/2
rounding to zero falsifies a relative-only bound. Flushing a larger
subnormal to zero falsifies this gradual-underflow contract.

An additional finite rational operation trace deliberately inserts errors
allowed by `u|z|+eta` into the non-FMA complex row word. Its exact error
obeys the proposed rho N+U bound and the complete ball recurrence. This is
an adversarial algebra fixture, not IEEE emulation, processor testing or
verification that the compiled kernel executes that word. No floating
arithmetic is used to obtain the fixture verdict.

Actual scalar evaluation of S, E, gamma, roots, norms, U and all accumulated
errors must round outward. Underflow allowances may not silently become
zero. Directed center-norm reductions are part of the runtime obligation;
an ordinary reduction would need its own proved operation-tree bound.
FTZ/DAZ, nonfinite intermediates or an operation trace outside this contract
prevent certification. A different compiler word needs its own justified
count and bound, not an inherited tolerance.

## 6. Horner, residual and endpoint boundaries

For dual Horner, the derivative update uses the old polynomial center:

```text
d_new = theta*d + p_old,
p_new = theta*p_old + c.
```

Node uncertainty must be propagated as coefficient uncertainty, including
its product with the input radius. The exact fixture verifies polynomial
and derivative values and their node-uncertainty balls for a rational
quintic. Updating the polynomial too early gives the wrong derivative
even for x^2 at x=1/2. This finite fixture deliberately uses exact center
operations; runtime Horner rounding and underflow remain additional terms.

The actual runtime must also cover uncertain Gaussian/scalar multipliers,
complex scaling, vector additions/subtractions, derivative scaling by 1/h,
and all derivative/coefficient norms. Residual cancellation may be used in
the computed center, never to delete a radius without proof.

The guard node bound, nonunitary annihilation-half tail and the analytic
Gauss/ellipse remainder together cover the full Hilbert space and full
real integration cell. The real cell cannot straddle a pulse switch.
Its analytic tube continues that cell's fixed-segment formula beyond its
real boundary; it is not a continuation of a discontinuous physical word.
The stored dyadic polynomial may miss a saved endpoint by a small jump.
Every such jump, including the final endpoint, belongs in the error account.

## 7. Decisions, source freeze and custody

The numerical precision goal is max of all six total pair radii <= 1/1000.
It is separate from a nonlinear-discrepancy decision: a certified lower
endpoint above 1/1000 for at least one selected pair of each sign. Thermal
radius alone, sampled defects, norm drift, timing or a small exact-gate
output cannot decide either numerical question.

PREREG.md freezes the actual configuration ladder, four-hour resource
budget, build, runtime arithmetic contract and first-outcome policy.
Do not execute this verifier, import candidate code, benchmark, propagate
states or construct EXPECTED.txt before the new public source pin.
Static source review and AST-only parsing are permitted preparation.

A valid wide interval is a valid enclosure with the precision question
UNRESOLVED. Invalid/missing arithmetic evidence is NOT_CERTIFIED; an
incomplete resource-limited record must be retained as incomplete. No
failure licenses a same-identifier repair or rerun, a threshold change,
an unplanned resource extension or pulse retuning.

The online certificate does not retain all quintic coefficient or node
interval arrays. Preserve frozen source/input/binary receipts, first
stdout/stderr, attempted-child outcomes, progress and whatever final
endpoint/per-column records actually exist. Do not claim missing records
were retained. Full intermediate offline inspection requires recomputation
from the pin, not only reading saved aggregates. Same-session review is not
blind replication; exact-verifier CI is not a large trajectory replay.

The standalone verifier accepts no arguments, performs no external reads,
and emits one sorted compact ASCII JSON line with explicit LF. Its first
completed pinned output, not a guessed or hand-authored value, determines
EXPECTED.txt. No actual trajectory certificate, hardware/source admission,
all-input contact guarantee or Canon promotion follows from this exact audit.
