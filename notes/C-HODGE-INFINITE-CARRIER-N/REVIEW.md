# Analytical review of the infinite-carrier note

**NON-CANONICAL. Source-visible analytical review. 2026-10-23.**

Reviewer: independently tasked ChatGPT proof-audit agent
`audit_infinite_proof`. The authoring agent and reviewer are separate
reasoning tasks in the same working session. The reviewer received the
proposed proof and its source definitions; this was not a blind theorem
discovery or a code-separated computational confirmation. No scientific
program was imported or executed, and no predecessor verifier was read.

The requested adversarial scope was primarily PROOF sections 5 and 6:
the removal of (P24) from the contact-memory obstruction, and the claimed
infinite positive/negative current index. The reviewer also checked the
displayed recurrence signs, coefficient-denominator argument, and cyclic
restriction wording. This review is not a fresh audit of every theorem in
the source repositories or of the complete native occupied-state circuit.

## Gap lemma and nonrationality

The reviewer checked the following implication rather than assuming that
rationality alone implies a finite spectral measure:

1. A genuine open spectral gap makes the integral Caratheodory function
   analytic across a circle arc and purely imaginary there.
2. For rational F, the rational reflection sum
   F(z) + conjugate(F(1/conjugate(z))) therefore vanishes identically.
3. On every compact circle arc away from its finitely many circle poles,
   the radial real part tends uniformly to zero.
4. Weak convergence of the positive Poisson measures then makes the
   spectral measure zero on each such arc. This step also excludes a
   hidden singular-continuous measure there; a mere almost-everywhere
   density argument would not have sufficed.
5. A finitely supported spectral measure would give a nonzero annihilating
   polynomial of the contact vector, contradicting the explicit
   extreme-support proof.

The reviewer found this chain valid. It establishes nonrationality of F
and of its invertible fractional-linear transform s without (P24).
The finite time-independent linear state-space corollary follows from
the adjugate formula. Its limits are explicit: time-dependent systems,
nonlinear encodings, finite-horizon matches, and infinite lattice systems
are not excluded by that corollary.

## Physical-current obstruction

The reviewer checked that the positive witnesses place constituent A at
the left endpoint of the cut with rightward velocity, while constituent B
is strictly away from the cut. The negative witnesses use the opposite
crossing. Both families obey the common-parity constraint, have fixed
spectators, and lie on the token branch where the pulse-edge current is
zero. They are mutually orthogonal and carry exactly +2 or -2.

Unitary pullback by D C preserves these eigenspaces. Its finite-depth
local gates also preserve finite support, so the witnesses remain in the
domain quantified in the finite-factorization corollary. Taking more
positive eigenvectors than the proposed finite target dimension gives a
nonzero kernel vector with positive current, which proves the stated
contradiction even without assuming that the linear map is bounded.

The reviewer found the argument valid for the full instantaneous encoded
state space. It does not establish a statement about a fixed-energy
stationary solution space or about the smaller cyclic preparation sector;
the proof explicitly preserves both boundaries.

## Corrections made before publication

Two precision defects were found and corrected in the draft:

- “Countably infinite carrier” was replaced by “countably many basis
  configurations” and an infinite-dimensional separable Hilbert space
  before ancillary factors. Complex-amplitude states themselves form an
  uncountable set.
- The cyclic-restriction proof now explicitly uses that the free step
  reduces the sector, both C and its adjoint preserve it, and the contact
  is identity on the dark complement. Invariance alone under an arbitrary
  infinite-dimensional unitary would not imply reduction.

The reviewer found the recurrence signs and complete-step denominator
argument consistent. They are algebraic re-expressions of the cited
source, not independently discovered local dynamics.

## Disposition

The specified analytical objections did not break the three stated
compression theorems after the wording corrections. The evidence is a
source-visible analytical review of the displayed proofs. It is not
execution evidence, a public computation gate, or a status promotion.
All conclusions remain **analytical candidate-T, NON-CANONICAL, L1**.
