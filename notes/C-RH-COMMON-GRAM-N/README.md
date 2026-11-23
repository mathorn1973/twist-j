# C-RH-COMMON-GRAM-N

NON-CANONICAL. Candidate-D. No Canon authority.

Claim: https://github.com/mathorn1973/twist-j/issues/2065
PR: https://github.com/mathorn1973/twist-j/pull/2067

## Result and attribution

This is an exact concave refinement of Jose Brox's centered frame-to-slope
comparison. His notes, whose earliest recorded commits are dated
21 November 2026, already contain the centered projection method, invariant
normalization, full-interval integration, actual-source bridge, and
zero loss in the ideal case. SOURCE_MAP.md gives the pinned references.
The original package missed those references; REVIEW.md preserves
the original review and appends an explicit correction.

For the same arithmetic hypotheses as the pinned TheoremFSharp, use the
exact source defect a^2=S*tr(T^2)/(tr(T))^2-1 and the explicit concave
composition Psi in PROOF.md. Then

\[
 s-\mu(C)\le (H+U)\Psi\!\left(\frac{U}{H+U}\right)-U.
\]

This formula applies when H+U>0; for H=U=0, the direct conclusion is
mu(C)>=s.

At the same source defect, target error and row-loss parameters, this
bound is no larger than Brox's centered bound (3.2), the old raw-e
formula, or the immediate allowance H. It is not asserted to dominate
Brox's one-sided theorems when those use additional operator information.

The refinement uses the exact quadratic target root and Jensen on the
composed envelope. Additional work here is the explicit all-threshold
audit at the pinned Lean source, an elementary upper bound, and the
least-eigenvalue counterexample. The original raw-e statement remains
a corollary; the frozen scope record is unchanged.

This is a reviewed paper derivation, not a Lean verification. No
scientific numerical computation, architecture receipt, change to
the global RH exponent, or new algebraic carrier is claimed.

## Contents

- [PROOF.md](PROOF.md): exact centered parameter, full proof, all endpoint
  cases, comparisons, and the spectral-gap counterexample.
- [SOURCE_MAP.md](SOURCE_MAP.md): Brox attribution, pinned Lean blobs,
  correspondence, and limits of the secondary expositions.
- [REVIEW.md](REVIEW.md): original reviews, appended attribution erratum,
  external review and correction review.
- [PREREG.md](PREREG.md): unchanged original proof-only scope and falsifiers.
- [PROMO-C-RH-COMMON-GRAM-N.md](PROMO-C-RH-COMMON-GRAM-N.md): scoped handoff.

The repository's Apache-2.0 license governs the authored note. External
source code and prose are cited rather than vendored.
