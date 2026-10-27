# Analytical review of the simultaneous-pair construction

Status: NON-CANONICAL; L1; candidate-T review. Verdict: PASS within the
explicit mathematical scope of `PROOF.md`. This is not Canon acceptance,
a computation gate, or confirmation of a particle identification.

Review date: 2026-10-27.

## Provenance and method

The reviewer is a separate agent in the same working session, with inherited
conversation context. The frozen equations and proposed conclusions were
checked before the reviewer opened the completed `PROOF.md`; the manuscript
was then read in full. Provisional results were already exposed in this
session. Accordingly this record makes no blind or independent-session
confirmation claim.

The review was analytical only. It did not run a numerical experiment,
evaluate an integral numerically, or manufacture a verifier transcript.
The preliminary equation review checked the local Green function, its
continuation, the pole bounds, the complete spectral disposition, and the
current signs. The manuscript review additionally checked the local energy
account, the positive-band-minimum obstruction, and the stated exclusions.

## Checks and outcome

1. **Carrier, bounded law and positivity.** The paired summand has two
   independent position coordinates and a fixed residual label. The
   off-diagonal coupling has norm `sqrt(3) g`; the stated lower and upper
   bounds follow from the uncoupled spectra. The two dark core states have
   exactly energy `1`. The finite-range claim is correctly limited to the
   declared configuration graph.

2. **Endpoint measures and the Schur complement.** The half-line densities
   `sigma(e)=sqrt(e(4-e))/(2 pi)` and
   `sigma2(v)=sqrt(v(8-v))/(8 pi)` are normalized with the stated first
   moment. Their translated convolution is the paired endpoint measure.
   The bright denominator is exactly `z-10-3g^2 m(z)`.

3. **No hidden bound or singular component.** The inverse-monotonicity edge
   bound is valid as a quadratic-form resolvent limit; it does not assume
   a bounded inverse of the gapless Laplacian. The denominator signs at
   `3-` and `15+`, and its strict derivative outside the band, exclude
   exterior poles. Strict positivity of the interior pair density excludes
   embedded bright atoms. The endpoints do not solve the eigenvalue
   equation. Compact Holder regularity gives continuous finite boundary
   Green values; the denominator stays nonzero on the whole compact band,
   excluding a singular component. The resulting bright measure is
   absolutely continuous and normalized. The Riemann-Lebesgue conclusion
   therefore gives complete asymptotic pair emission from the bright state.

4. **Whole paired complement.** The reviewer requested an explicit
   justification that the free paired operator is absolutely continuous
   for every vector, since its endpoint vector is not asserted to be
   cyclic for the whole two-coordinate operator. Section 4 now supplies
   the product spectral transform and the Fubini pushforward argument.
   This addition was read back and resolves the exposition gap. The
   orthogonal complement of the endpoint cyclic subspace consequently
   remains absolutely continuous under the rank-one coupling.

5. **Continued resolvent and resonance.** The continuation across the
   regular interval `(7,11)` is
   `mII(z)=(z-9-iF(z))/8`, with the square-root branches specified in the
   manuscript. On `|z-10|<=1/2`, the reviewed bounds are
   `|F|<=9/2`, `|mII|<=3/4`, and `|F'|<=7/sqrt(13)`.
   Rouche's theorem gives exactly one simple zero in that disk and
   `|z_*-10|<=9g^2/4`. The identity
   `Gamma=[(3g^2/4)/(1-3g^2/8)] Re F(z_*)`
   and the manuscript's rational inequalities prove
   `(3/2)g^2<Gamma<(7/2)g^2`. In particular the fixed witness obeys
   `3/32<Gamma<7/32`. This is a pole of the locally continued resolvent,
   not a complex eigenvalue of the selfadjoint operator.

6. **Short-time emission and conservation.** The first-order paired
   amplitude is `-i sqrt(3) g t delta`; reality of the matrix and initial
   vector justifies the even probability expansion. The supplied charge
   operator commutes with the law. The conserved energy includes the
   interaction expectation. The initial mean `10` and variance `3g^2`
   are correct and are distinguished from sharp-energy preparation.

7. **Local probability and energy currents.** Both hopping-current signs
   and the endpoint source sign agree with the displayed Schrodinger
   equations. For the energy densities
   `h_v=(P_v H+H P_v)/2`, the choice
   `J^E_(v to w)=i<[h_v,h_w]>` is real and antisymmetric and gives
   `d<h_v>/dt=-sum_w J^E_(v to w)`. Stars at distance greater than two
   are disjoint, so the commutators vanish there. The total energy sum is
   absolutely convergent: its terms are
   `Re(conj(psi_v)(H psi)_v)`, controlled by Cauchy-Schwarz because `H`
   is bounded.

8. **Positive-band-minimum obstruction.** For every vector in the kernel
   of a nonnegative differentiable Hermitian symbol, the directional
   derivative of its scalar quadratic form vanishes. Polarization yields
   `P0 h'(k0) P0=0`. In the finite-dimensional finite-range setting this
   excludes nonzero linear splitting of the zero-energy band cluster.
   The conclusion correctly concerns a true nonnegative band minimum,
   rather than a signed or offset Dirac crossing.

## Limits retained in the accepted statement

- The gapless outgoing channel is quadratic near zero; no Weyl, helicity,
  spin or statistics identification follows.
- The residual state is supplied and pinned. Recoil and total momentum
  conservation are not established.
- Charges, coefficients, the output carrier and its local creation vertex
  are declared inputs, not consequences of the native TWIST-J update.
- A rigorous pole width does not by itself establish a time interval of
  approximately exponential survival. The manuscript explicitly leaves
  the non-pole remainder estimate open.
- The matrix `4H` having integer entries at the fixed witness is only an
  energy/time rescaling. The added paragraph correctly denies any native
  integer-state-update conclusion from that observation.
- No measured mass ratio, particle identity, physical occurrence, or
  public Canon promotion is claimed.

No unresolved mathematical correction remains within the reviewed scope.
