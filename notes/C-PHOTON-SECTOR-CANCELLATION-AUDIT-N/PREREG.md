# C-PHOTON-SECTOR-CANCELLATION-AUDIT-N scope declaration

**PUBLIC, NON-CANONICAL. Proof-only analytical item; no Canon authority.**

- Owner: A. M. Thorn / photon-sector-cancellation-audit-20260927
- Public reservation: #1226
- Branch: `notes/C-PHOTON-SECTOR-CANCELLATION-AUDIT-N`
- Basis: Public Canon v92, public main
  `f94868276c77332430c5b476adc9a7bcf6bb747c`
- Date: 27 September 2026
- Status ceiling: candidate-T for the written arguments
- Layers: L4 for the finite cubical supports; L6 for their probabilities in
  the already fixed finite surface measure. No new physical dictionary.

## Disclosure before review

The four-cup counterfamily, its local weights, and its limiting cancellation
were discovered analytically before this first public scope declaration.
The parallel-cut averaging identity and its conditional convexity comparison
were also discussed before this declaration. They are known candidate
results, not predictions frozen before discovery. Review of these arguments
must not be described as blind confirmation.

No scientific program, verifier, numerical sampling, enumeration, or formal
gate has been executed for this item. The coefficient counts below are
derived in the written proof. Existing source results are identified there;
their earlier computations are not claimed as new executions or independent
confirmation here.

## Frozen carrier and measure

For every even L >= 4 use the periodic four-dimensional cubical lattice,
the unchanged ternary surface carrier and the unchanged weight

\[
\Omega_L=\{n\in\{-1,0,1\}^{P(K_L)}:\partial n=0\pmod5\},
\qquad
\mu_L(n)\propto2^{-|\operatorname{supp}n|}.
\]

Let Sigma_(t,s) be the 01 seam at x_0=t, x_1=s, set
F_(t,s)=<n,Sigma_(t,s)>, F=F_(0,0), and A=F mod 5. Define

\[
G=L^{-2}\sum_{t,s}F_{t,s}
 =L^{-2}\sum_{p\parallel01}n_p.
\]

G is a rational observable, not a replacement integer flux. All conditional
statements about G retain the original sector variable A.

## Frozen claims and equations

1. The complete zero-exterior four-cup law has 53 admissible ternary
   fillings. Its seam flux is in {0,+5,-5}, with each nonzero value having
   probability `1/(2*1192327)`.
2. The proof's explicit packing contains
   m=floor((L-1)/3)^2 edge-separated copies. Conditioning only the outside
   plaquettes on a specified positive coordinate plane and zeros gives
   independent copies of that complete 53-state law and
   F=1+5T, where T is their normalized flux sum.
3. With v=1/1192327,
   E T^2=mv and E T^4=mv+3m(m-1)v^2. Consequently
   E|T| >= mv/sqrt(1+3(m-1)v). The ratio of negative to positive flux parts
   in sector 1 tends to one along these admissible conditional laws.
4. Conditioning on the union of the positive-plane and negative-plane
   outside events produces a reversal-invariant actual Gibbs conditional
   ensemble with sector polarization H=1, while the same ratio tends to one.
5. These examples rule out a constant kappa<1 that controls this ratio
   uniformly over every admitted exterior condition and all large even L.
   They do not rule out such a bound for the unconditioned torus law.
6. In the full torus measure,
   E[G|A]=E[F|A] and E[|G||A]<=E[|F||A]. Thus sector-weighted positive and
   negative parts both decrease, their difference is preserved, and the
   negative-to-positive ratio decreases wherever that difference is positive.
7. In the explicit conditional counterfamily,
   G=epsilon+5T/L^2 with epsilon in {+1,-1}, and |5T/L^2|<5/9. Its G
   observable therefore has no negative part in sector 1 at any volume.

## Code, evidence and execution boundary

There is no scientific code or computational claim in this item. The evidence
is `PROOF.md`, subject to separate written review. No `EXPECTED.txt`, `RUN.md`,
computational status, two-architecture scientific gate, or benchmark output
is claimed. Repository policy and document checks remain ordinary publication
requirements and do not turn the proof into a computational result.

## Systematics and exact failure conditions

The candidate fails at the affected scope if review finds an omitted local
filling, a sign or normalization error, a shared edge in the claimed packing,
an inadmissible exterior, residual coupling between the patches, a mistaken
moment inequality, or an invalid sector-preserving translation argument.
For the negative theorem, the exact threshold is V/U > kappa for every fixed
kappa<1 at sufficiently large volumes in the specified conditional family.
Changing from the full torus law to that conditional family is explicit and
must never be hidden in the conclusion.

## Claims expressly excluded

No lower bound for the probability of the conditioning events is asserted.
Neither proposed full-measure estimate V_L<=kappa U_L nor
U_L^2>=c N_L Q_(L,1) is proved or disproved here. No positive thermodynamic
floor for H or the integer defect contrast, P1 closure, P2, S7, continuum
limit, apparatus, or physical photon conclusion is claimed. The full Gram
fiber sector cap is not transported to the conditional examples.

Canon, registry, frontier, formal probes, runners and release files are
outside this item's editing scope.
