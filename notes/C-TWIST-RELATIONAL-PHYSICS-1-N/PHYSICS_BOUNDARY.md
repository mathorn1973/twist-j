# Physical boundary: the common frequency and wavevector reading

**Status:** NON-CANONICAL analytical boundary for
`C-TWIST-RELATIONAL-PHYSICS-1-N`. No public authority, physical species
adoption, numerical discovery, new executed verifier, or status promotion.

**Frozen mathematical source:** TWIST-J Public Canon v106,
`mathorn1973/twist-j` at
`a193e389fb1ddb0bdc89165b015c95a17eb1e425`.
`DIRAC-STEP-THEOREMS` supplies the inherited step and rescaled shell;
`CONTACT-W-BOUND-PAIR-RESPONSE` explicitly uses the single-walk dispersion;
`DIRAC-CONTACT-COMPLETE-ACCOUNT` uses a separately specified signed
sine-energy reading. The calculation below audits a proposed physical
dictionary; it does not present those inherited identities as new results.

## 1. The candidate dictionary and its exact obstruction

Consider the stipulated normalized walk

\[
W_\mu(k)=\operatorname{diag}(e^{ik},e^{-ik})
\frac{I+i\mu X}{\sqrt{1+\mu^2}},\qquad \mu\geq0.
\]

The proposed common dictionary is

\[
E=\hbar\omega/\tau,\qquad p=\hbar k/\ell,\qquad c=\ell/\tau,
\]

with the same positive `ell` and `tau` in both the `mu=0` and `mu=2`
sectors. Calling those sectors photons and electrons would be an additional
physical identification, not a premise or conclusion here.

The determinant is one and the trace gives

\[
\cos\omega_\mu(k)=\frac{\cos k}{\sqrt{1+\mu^2}}.
\]

For `mu>0`, the principal positive branch has rest phase
`alpha_mu=atan(mu)` and exact derivatives

\[
\omega_\mu'(k)=\frac{\sin k}{\sqrt{\mu^2+\sin^2k}},\qquad
\omega_\mu''(k)=
\frac{\mu^2\cos k}{(\mu^2+\sin^2k)^{3/2}}.
\]

Thus the narrow-packet group speed is at most
`c/sqrt(1+mu^2)`: it is `c` in the massless sector and `c/sqrt(5)`
in the `mu=2` sector. Both walks nevertheless share the exact one-site
support cone. Packet drift and the front of nonzero support are distinct.

At fixed positive `mu`,

\[
\omega_\mu(k)=\alpha_\mu+\frac{k^2}{2\mu}
-\frac{\mu^2+3}{24\mu^3}k^4+O(k^6).
\]

Consequently the mass read from rest energy and the mass read from energy
curvature are

\[
m_{\rm rest}=\frac{\hbar\arctan\mu}{c^2\tau},\qquad
m_{\rm in}=\frac{\hbar\mu}{c^2\tau}.
\]

They differ for every `mu>0`, since

\[
\mu-\arctan\mu=\int_0^\mu\frac{t^2}{1+t^2}\,dt>0.
\]

In particular

\[
\frac{m_{\rm in}}{m_{\rm rest}}=\frac{2}{\arctan 2}\ne1
\quad\text{at }\mu=2.
\]

This dimensionless obstruction cannot be removed by choosing a different
common length or time unit. The proposed dictionary therefore fails
ordinary common Lorentz dispersion already at rest. It remains possible
to formulate a different, explicitly Lorentz-violating physical candidate;
that would require its own applicability and experimental comparison.

## 2. What a continuum or clock claim would additionally require

A joint small-parameter scaling `k=epsilon K`, `mu=epsilon M` gives

\[
\omega^2=k^2+\mu^2-\frac13\mu^2k^2-\frac23\mu^4+O(\epsilon^6).
\]

It recovers the ordinary relativistic dispersion at leading order when
both momentum and dimensionless mass gap tend to zero. Taking only
`k -> 0` at fixed `mu=2` does not do so. A proposed physical scaling must
explain how the fixed microscopic sector produces a small effective gap.

If one additionally identifies the phase accumulated along the packet
center as a proper clock, its rest-normalized rate is

\[
\frac{d\tau_{\rm phase}}{dt}
=\frac{\omega-k\omega'}{\alpha_\mu}
=1-\frac{k^2}{2\mu\alpha_\mu}+O(k^4).
\]

Ordinary time dilation at the actual packet speed instead requires

\[
\sqrt{1-v^2/c^2}=1-\frac{k^2}{2\mu^2}+O(k^4).
\]

These disagree for positive `mu`. This is a conditional failure of that
particular phase-clock identification, not a theorem excluding every
possible clock apparatus. The homogeneous walk by itself supplies no
gravitational clock-comparison law.

## 3. The sine shell is a different reading

There is an exact identity

\[
\mathcal E_\mu^2-\mathcal P^2=\mu^2,\qquad
\mathcal E_\mu=\sqrt{1+\mu^2}\sin\omega,\quad
\mathcal P=\sin k,
\]

and `mathcal P/mathcal E_mu=omega_mu'(k)`. This identity is not disputed.
The sine energy is not the logarithmic generator of the actual step,
and `sin(k)` is not the generator of lattice translations. Ordinary
linear boosts also leave the bounded sine-momentum domain. Adopting
these as physical energy and momentum therefore requires a new dictionary
for translations, clocks, forces, boosts, interactions and calibration.
An algebraic shell equality alone does not provide that dictionary.

## 4. Relation to the finite stationary construction

The finite relational model uses its separately declared positive
apparatus Hamiltonian `H_A`, complementary clock Hamiltonian `H_C`,
stationary preparation, and relational measurement effects. It does not
identify `H_A` with the walk quasienergy or sine energy, and it adopts no
photon/electron identification. The obstruction above therefore does not
falsify its finite clock-conditioned joint-probability theorem.

Conversely, that theorem does not remove this obstruction or establish
ordinary Lorentz symmetry, general-relativistic proper time, gravitational
redshift, or the physical identity of the two walk sectors. Such claims
need separately specified constructions and tests.
