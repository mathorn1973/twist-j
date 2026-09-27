# C-PHOTON-SECTOR-ORIENTATION-CANCELLATION-N

**PUBLIC / NON-CANONICAL. Proof-only analytical work.**

Owner: A. M. Thorn / sector-orientation-cancellation-20260927.
Public reservation: #1241.
Branch/path: notes/C-PHOTON-SECTOR-ORIENTATION-CANCELLATION-N.
Basis: public main ad8a572128f594a3550cbf5e3adef2516fea3d88,
Public Canon v92. Date: 27 September 2026.

## Fixed target and scope

Retain the full periodic even-L>=4 ternary plaquette measure
mu_L(n) proportional to 2^(-|supp n|), partial n=0 modulo five.
Let A be the 01 seam flux modulo five, G=L^-2 times the sum of all
01 plaquette values, and H_L=E(E[G|A])^2.

The original objective is a strictly positive thermodynamic H_L floor.
This item directly controls cancellation in the first moment, not a
replacement variance. The proposed partial results give a uniform
truncation error when retaining configurations with a bounded number M
of support components whose measured 01 residue is nonzero.

Components are connected occupied plaquettes sharing an edge. The exact
orientation orbit fixes the support and relative orientations modulo
reversal of each whole component. M is not a component size, diameter,
current-loop count, or the number of all nontrivial homology classes.

Every retained mean uses the original mu_L and its FULL p_a=mu_L(A=a).
No renormalized restricted law, sector-filtered sampler or replacement
action is admitted.

## Prior exposure and inherited inputs

The arguments were derived analytically in discussion before this
reservation and have received preliminary separate model review.
This document is not a blind pre-discovery preregistration and not a
computational pin.

#1112 and the existing BCHI connected-current notes already use
independent component reversals. BCHI/REPLICA-CAPS section 5 already uses
the complex-source modulus and empty-face cosh comparison on nu_0.
The present proof explicitly rederives these mechanisms for the full
mu_L; it does not claim their invention. #1233/#1236 gives residual
variance and a different, single-slice spatial deletion comparison.

The new scope is the F5 sector-projection suppression, the explicit
two-sided norm error for H_L versus H_L^{<r}, and the full-measure
rare-event consequence. It differs from #1143's coherent-lift diameter
removal and closed #1146's finite-volume diagnostic publication.

## Claims to review and falsifiers

For integer r>=7 and rho=cos(pi/5), put

\[
b_r=\min\left\{1,\frac{4r\rho^{2r-2}}{1-4\rho^r}\right\}.
\]

The submitted targets are the exact orientation-orbit identities,
the full-measure Gaussian bound E exp(tG)<=exp(t^2/2),
the uniform error |sqrt(H_L)-sqrt(H_L^{<r})|<=sqrt(b_r),
and H_L<=2p(1+log(2/p))+b_r where p=mu_L(1<=M<r)
and the p=0 expression is zero.

Review must falsify any incorrect orbit partition, dependence of supposedly
independent signs, loss of a boundary constraint, wrong Fourier or Parseval
normalization, omitted neutral-component term, wrong projection direction,
changed sector denominator, unjustified moment comparison, invalid
finite-r bound, or interchange of volume and cutoff limits.

A positive lower bound for the retained signed quantity is not assumed.
If it is absent, the disposition remains primary target NOT PROVED.
A failure of a proposed pairing or an event-conditioned example cannot
be promoted to a negative phase theorem.

## Evidence and publication boundary

No scientific executable, enumeration, sampler, numerical estimate or
extrapolation is included or has run. Evidence consists of a written proof
and separate analytical review. Any future scientific execution requires a
new complete prospective Git pin and public readback. #1210 is not reused.

Candidate-T is the ceiling; repository tests confer no scientific C status.
Only this new notes directory may change. Canon, registry, frontier,
formal probes, gates, workflows, releases and physical identifications
remain unchanged.
