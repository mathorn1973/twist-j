# Independent post-pin mathematical and code review

**PUBLIC / NON-CANONICAL. No authority or phase conclusion.**
Candidate C-PHOTON-U1-FINITE-CENTER-N, issue #1715.
Original review: A. M. Thorn, Apache-2.0.

## Review boundary

This review follows the complete public source pin
`9a74d03fb8f2c8086eff0f326446352f0f628082`, reported read back by the
coordinator. The independent breaker and its original review were already
frozen before this reviewer opened `verify.py` or `z7_exact.py`. Neither
file was used to construct the breaker. The present review reads
`PREREG.md`, `PROOF.md`, `MEASUREMENT.md`, `verify.py`, `z7_exact.py` and
`exercise.py`; it does not change any pinned source.

No scientific program was executed by this reviewer, and no execution
transcript was used to reach the conclusions below. The coordinator owns
the first audit runs and their custody records. This is a mathematical and
static implementation review, not an additional reproduction.

The global sharpness construction was derived analytically with a helper
and disclosed to the primary author before preregistration. Thus its
implementation check is independent code for an exposed prediction; it is
not a blind discovery or independent rediscovery of that construction.
The inherited local incidence theorem remains credited to #1196.

## Mathematical assessment

No blocker was found in the stated finite-volume identities.

1. **Character integration and normalization.** Expanding each face factor
   retains separate coefficients for the modes -1, 0 and +1, including
   when two modes coincide on a small finite group. Independent normalized
   edge Haar integrals impose precisely the two displayed constraints.
   No gauge-orbit division, potential parametrization, or deletion of
   nontrivial cycles appears. The row bound applies to the actual integer
   matrix, including multiplicities. The argument therefore establishes
   equality for arbitrary real plaquette source, all finite complexes
   obeying the bound, and composite as well as prime N.

2. **Insertion threshold and its sharpness.** The sufficient condition is
   strict: N must exceed the maximum of the incidence row sum plus the
   absolute inserted current on that edge. In four dimensions N >= 8
   consequently covers the full class with current norm at most one.
   For the even-torus witness, transverse parity flips give
   f_a(s)-f_a(-s)=a*s, and independence of x_0 cancels every transverse
   boundary component. Hence Bn=N*j globally, not just at one edge.
   The current is conserved; the face-chain support is N*L^4/2.
   At zero source the integer-closed terms form a subset of the
   modulo-closed terms with positive coefficients, so a single extra term
   proves strict partition inequality. For Bn=6*j and J=j, the same
   positivity proves strict inserted-numerator inequality at N=7, while
   the uninserted denominators agree. The example belongs to the full
   bounded-current class and is a product of winding-loop characters.
   It does not establish sharpness for one simple contractible Wilson
   loop. The written proof makes this distinction explicitly. The same
   construction with J=M*j obstructs equality at N=6+M for each M >= 1.

3. **Stack and uniform sources.** Summing the relevant edge boundary
   equations over transverse coordinates makes the unwanted differences
   telescope and equates adjacent stack pairings in each of the two
   distinguished coordinates. Summing all stacks then gives the factor
   L_mu*L_nu. This is a termwise identity for all closed integer chains,
   including fundamental wrapping sheets; it is stronger than a
   second-derivative equality. It does not apply to the extra Z5 chains.
   The dual positive measure gives a characteristic function of the
   integer W, and its second logarithmic derivative at zero is Var(W).
   W is not a principal-lift flux of a sampled primal configuration.

4. **Topology and finite positivity.** Fundamental sheets have positive
   weight, so the finite variance is positive. The exact two-dimensional
   value 2/(2^A+2) nevertheless vanishes with area. This control correctly
   distinguishes retained winding sectors from a boundary-only
   parametrization and also refutes the inference from finite positivity
   to a positive thermodynamic response. The disk and cube controls use
   normalized Haar partitions 2 and 66, respectively.

5. **Cubic-field Hessian.** With s=-log w, the identities
   s'=tan(theta/2) and s''=(1+tan(theta/2)^2)/2 give, for any fixed source
   direction, F''=E S''-Var(S'). At zero source charge conjugation makes
   E S'=0. Writing the seven scores as sqrt(r)*G therefore gives exactly
   the curvature sum minus r times the squared total G score used by the
   implementation. The area-square denominator, rather than a general
   volume denominator, is essential. The expression needs no quadratic
   field extension because every occurrence of the score is quadratic.
   An individual reader can be negative and must not be clipped. The
   omitted squared-mean correction is justified specifically at zero
   source and is not a prescription for a nonzero-source Hessian.

6. **Meaning of boundedness.** The seven-value score has no pole, and the
   reader is bounded on each finite carrier. This is not a uniform bound
   in volume: on isotropic four-tori its squared-total-score contribution
   can scale with V. For example, constant nonzero primal curl is
   realizable when the side length is a multiple of seven. The explicit
   qualification in `MEASUREMENT.md` correctly prevents using an
   unjustified volume-independent concentration bound.

## Static implementation assessment

The primary field implementation reduces products by
x^3=1+2*x-x^2, uses rational Gaussian elimination for inverses, and orders
the selected real embedding by certified root intervals. A nonzero
quadratic cannot vanish at the degree-three generator, so the sign
procedure terminates. Its initial interval (1,3/2) isolates the required
root; rational bisection preserves that enclosure.

The lazy categorical routine compares the entire half-open dyadic
interval with exact cumulative masses, with equality permitted at the
appropriate endpoints. Scaling both sides by the positive total avoids
rounded normalized probabilities. Under ideal independent bits the
dyadic interval eventually lies within a category except on a set of
measure zero. The code and proof distinguish this theorem from the
deterministic seeded pseudorandom exercise.

The lattice boundary uses the conventional oriented four-edge plaquette.
For side lengths at least two, an incident link occurs only once in each
such face. If the old link is k and an incidence sign is s, replacing it
by v changes the flux from f to f+s*(v-k). Evenness of w gives the
implemented staple offset k-s*f and mass w(v-(k-s*f)). The sampler uses
minus offsets, whereas the declared checksum uses plus offsets. These
are compatible by negating the offset labels; the checksum itself is
computed in the declared plus convention.

Every single-link conditional is positive. A systematic sweep has a
positive-probability path to any prescribed target configuration, and a
positive self-loop. Thus the claimed finite irreducibility, aperiodicity
and stationary measure follow. Reversibility is asserted only for the
single-link kernel. No quantitative mixing statement follows from these
facts or from exact arithmetic.

`source_hessian` forms the required quadratic expression directly from
the actual flux residues and rational source coefficients.
`uniform_helicity` applies 1/(L_mu*L_nu) to the selected orientation;
`stack_helicity` applies unit coefficients to the specified stack. Their
expectation equality is not incorrectly enforced configuration by
configuration. The cached-flux update uses the same incidence signs as
the direct curl. The separate principal-plane diagnostic is explicitly
labelled as a primal quantity, not the dual W.

The primary two-dimensional audit enumerates every constrained
plaquette assignment before aggregating by counts and the distinguished
plaquette. Dividing the unnormalized sum by 7^(A-1) retains Haar
normalization. The uniform and stack readers are weighted before their
expectations are formed, and the discrete shift uses the changed weight
at the distinguished plaquette. The independent breaker instead uses
the cyclotomic score and replacement counts, so their agreement would
compare distinct arithmetic and reader constructions.

The primary cube control embeds one unit cube boundary in a periodic
three-lattice of side two. Its six chosen faces and their twelve edges
are distinct and have the ordinary cube incidences; this embedding does
not introduce an extra identification within the tested subcomplex.
The breaker constructs the nonperiodic cube boundary separately.

## Coverage limits and disposition

The declared exact audits and operation exercise should be reported
separately. The operation exercise checks state consistency and reader
serialization after the fixed sweeps; its outputs have zero phase
decision weight. A passing audit is a finite implementation check and
does not replace the all-volume proof.

`MEASUREMENT.md` also mentions scripted categorical endpoint tests and
intentional cache corruption. Those additional tests are not executed
by the pinned `verify.py` or `exercise.py`. They should be read as
prospective qualification checks, not listed among the completed
preregistered evidence. The categorical endpoint logic was reviewed
statically above; no scripted execution is claimed here.

The finite-source bridge, its stated full-class sharpness, topology
identity and zero-source reader survive this review. The conclusions
remain NON-CANONICAL candidates. No phase, practical mixing, sampling
error, Z5 comparison, native-action selection or physical-photon claim
is supplied by this review.
