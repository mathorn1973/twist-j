# Static review of the finite sampler qualification

**PUBLIC / NON-CANONICAL.** Candidate `C-PHOTON-U1-FINITE-CENTER-N`,
owner issue #1715. Original work by A. M. Thorn, Apache-2.0.

Reviewed source pin: `9a74d03fb8f2c8086eff0f326446352f0f628082`.
This review read `PREREG.md`, `z7_exact.py`, `verify.py`, `exercise.py`
and `MEASUREMENT.md`. No program was imported or executed for this review.
Execution results and transcript custody belong in RUN/RESULT.

The reviewer authored `z7_exact.py` and `MEASUREMENT.md`. Consequently
this is a cross-author static review of `verify.py` and `exercise.py`,
and an author self-review of the sampler. It is **not** an independent
or blind confirmation of the sampler implementation. The separately
authored cyclotomic breaker supplies a different independence boundary.

No static mathematical or implementation blocker was found for the
declared finite audit A. This finding neither asserts that a run passed
nor certifies mixing, an equilibrium estimate, or a phase.

## 1. Local conditional law and cache updates

For a link with old value `k`, let an incident plaquette have incidence
`s in {-1,+1}` and flux `f=s*k+b` modulo seven. The cached staple is

```
a = k-s*f = -s*b mod7.
```

After proposing `v`, the new flux is `f'=s*v+b=s*(v-a)`. Since the
plaquette weight is even, `w(f')=w(v-a)`. Thus `staple_counts` and
`conditional_masses` use the correct sign for every incident plaquette.
Multiplying these factors gives the exact conditional mass; all
nonincident factors cancel. The cache key depends only on the seven
staple multiplicities, which is sufficient. No old-link value or missing
orientation datum is needed after this reduction.

The verifier's checksum uses the separate convention
`product_k w(v+k)^c_k`. Replacing `c_k` by the multiplicity of staple
`-k` maps the sampler to that convention. The complete 924-composition
table therefore covers the same mass polynomials. This algebraic
identification is not an executed comparison of the sampler method with
direct replacement of an actual lattice link.

`step_edge` updates each incident flux by `s*(v-k)` modulo seven, exactly
the change in the direct curl. With every period at least two, a face
contains four distinct edge objects and the same edge is not counted
twice within a face. Period two still has distinct oriented edge objects
with the same pair of geometric endpoints; this is a valid periodic
cell structure and does not invalidate the incidence calculation.

## 2. Cubes, sectors and stationary measure

The stored face boundary gives
`F_mu_nu=Delta_mu A_nu-Delta_nu A_mu`. The implemented cube expression is

```
Delta_mu F_nu_rho - Delta_nu F_mu_rho + Delta_rho F_mu_nu,
```

which vanishes because lattice differences commute. This agrees with
the verifier's oriented cube boundary. Recomputing all curls checks
more than Bianchi alone: it checks that the cached flux belongs to the
actual retained periodic link configuration. Closed mod-seven fields
with a different cohomology class would not pass that comparison.

The normalized source-partition theorem sums precisely these periodic
link configurations; no additional primal bundle sector is required by
that selected definition. The integer-closed *dual* character expansion
nevertheless includes its winding sheets. The two statements concern
different variables and are consistent.

Each principal-lift plane sum is divisible by seven by telescoping the
underlying mod-seven curl. Its quotient is a primal diagnostic, not the
dual winding `W`; neither its value nor a flat holonomy move establishes
sampling of the dual winding distribution.

All seven weights are positive. Each one-link heat bath preserves the
finite Gibbs measure. Their deterministic sweep composition also
preserves it, although the composition is not generally reversible.
For any starting and target link assignments, assigning each target
coordinate in sweep order has positive probability. Therefore the
full-sweep transition matrix is strictly positive, so finite
irreducibility and aperiodicity follow. This gives eventual convergence
for the ideal stochastic kernel, not a usable finite-time mixing bound.

## 3. Exact field order and categorical selection

The cubic `p(x)=x^3+x^2-2*x-1` has no rational root and is irreducible
over the rationals. It has opposite signs at 1 and 3/2 and is strictly
increasing between them. Rational bisection therefore isolates the
intended real root. The field multiplication reduction, inversion by
the exact multiplication matrix, and sign-aware interval enclosure are
consistent with this representation. A nonzero reduced quadratic cannot
vanish at the selected cubic root, so its shrinking enclosure eventually
determines a strict sign. Zero is detected by its exact coefficient
triple before refinement.

For positive masses with total `T`, the bit reader maintains a uniform
dyadic interval `[b/d,(b+1)/d)`. It returns category `i` only if

```
b*T >= d*C_(i-1),
(b+1)*T <= d*C_i,
```

where `C` are exact cumulative masses. These are the correct containment
inequalities, including dyadic endpoint equality. Under independent fair
bits, every nonboundary uniform value eventually lies in an accepted
interval; the finite set of category boundaries has probability zero.
Thus the law is exactly proportional to the masses and termination is
almost sure. There is deliberately no rounding or precision fallback.

This proof applies to ideal fair bits. The frozen seeded
`random.Random` stream is deterministic engineering input. The operation
exercise does not turn it into a mathematical random source. Its
`random_bits` counter records categorical-update bits; the initial hot
start's `randrange(7)` calls are outside that counter.

## 4. Reader and finite controls

For `s=-log w`, `s'=sqrt(r)*G` and `s''=(1+r*G^2)/2`. Charge conjugation
makes the equilibrium mean total score zero. The implementation therefore
correctly returns `sum a_p^2*s''(f_p)-r*(sum a_p*G(f_p))^2` for a rational
source direction. The uniform source uses `1/(L_mu*L_nu)`, giving the
plane-area-square denominator in rectangular boxes and other dimensions.
The default averages orientation readers, rather than squaring a sum
across orientations. The stack source selects the stated fixed two
coordinates. These are expectation identities; negative configuration
values are permitted.

The 2D verifier enumerates all `7^(A-1)` flux fields and groups them by
residue counts and the first plaquette. Those data preserve the mass,
uniform Hessian, one-plaquette stack Hessian and discrete source ratio.
Dividing the partition by `7^(A-1)` is the correct normalized Haar factor
because all admitted plaquette fields have equal link-lift multiplicity.
The targets `2^A+2`, `2/(2^A+2)` and `2^A+x` retain both nonzero winding
sectors. These controls do not invoke the production reader functions:
they independently reassemble their formulas from the common field and
score constants. Static agreement was checked here; an executed
pointwise comparison of the production reader to those formulas remains
a separate implementation-coverage task.

The exercise uses the four frozen seed/start pairs, continues the same
stream after a hot start, performs exactly two sweeps per start, and
checks direct curls, Bianchi, plane divisibility, update counts and reader
serialization after each sweep. Its output has phase decision weight
zero. None of these checks estimates an equilibrium expectation.

## 5. Coverage boundary and prospective checks

The pin's `MEASUREMENT.md` section 4 listed additional implementation
checks more broadly than the frozen audit implemented. The owner has
made a subsequent documentation-only clarification labelling direct-link
replacement, scripted-bit boundary handling and intentional-corruption
tests as prospective and unexecuted. The source-pin version is retained;
no formula, code or completed execution contract is changed by that
clarification.

| Item | Frozen implementation coverage |
| --- | --- |
| Exact mass polynomials, positivity, normalization | All 924 count vectors and seven proposals in `verify.py` |
| Actual `conditional_masses` versus direct link replacement | Not executed by the frozen scripts; sign relation reviewed algebraically above |
| Lazy-bit categorical endpoint and refinement cases | Not scripted by the frozen scripts; law reviewed above |
| Actual cache updates and cube constraints | Checked after each frozen exercise sweep |
| Deliberate cached-flux corruption and rejection | Not executed by the frozen scripts |
| Exact 2D expectation controls | Independently assembled formulas using shared field constants |
| Production reader versus an independent pointwise reader | Not executed by the frozen scripts |
| Mixing, equilibrium error, thermodynamic extrapolation | Outside audit A |

The unchecked local sign mapping is a material implementation seam for
future production, even though its static derivation is correct. A
separately pinned deterministic successor qualification can close it by
comparing actual conditional masses with full-curl link replacement on
fixed periodic rectangular fixtures, checking scripted dyadic-boundary
and multi-block categorical cases, exercising deliberate state
corruption, and comparing both production readers pointwise with an
independent formula. Its exact fixtures, byte outputs, resource limit
and failure handling must be frozen before execution. No successor code
or execution is part of this review.

The present finite mathematical bridge and the operation-only sampler
exercise must remain distinct from any prospective phase experiment.
