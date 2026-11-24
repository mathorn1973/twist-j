# PROMO-C-RH-COMMON-GRAM-N

NON-CANONICAL. Candidate-D. No Canon authority.

Owner: A. M. Thorn, session ChatGPT-Astra-Sol-20261123-RH-COMMON-GRAM.
Public claim: https://github.com/mathorn1973/twist-j/issues/2065
Public PR: https://github.com/mathorn1973/twist-j/pull/2067
Action layer: NOT_APPLICABLE.

## Corrected contribution

This package refines Jose Brox's centered frame comparison. His earlier
notes already establish centered projections, optimal normalization,
full-interval comparison, zero loss in the ideal case, and the
actual-source bridge. SOURCE_MAP.md pins those notes and dates.
The original attribution omission is corrected by an appended erratum
in REVIEW.md, with the historical review retained.

The exact centered source defect is a^2=S*tr(T^2)/(tr(T))^2-1.
For the same matrices and retained target, the centered constraints are

    |p-r| <= a*sqrt(r*(1-r)),
    (z-b)^2 <= eta*z*(1-z),  0 <= b <= p.

The refinement explicitly inverts the target quadratic and applies
Jensen to the capped composition Psi. Under the unchanged arithmetic
hypotheses of the pinned TheoremFSharp,

    s-mu(C) <= (H+U)*Psi(U/(H+U))-U,

with H=U=0 handled directly. Evaluated at identical a, eta and delta,
this allowance is no larger than Brox (3.2), the previous raw-e
formula, or H. Bounds using further one-sided operator information
are not included in that ordering. The original formula in the
unchanged PREREG.md remains a corollary.

Other scoped work is the negative-threshold audit in the actual
Lean source, elementary bound (8), and the least-eigenvalue example.
The note claims no wider priority for these classical ingredients.

## Evidence and correction

- PROOF.md: self-contained paper proof, source fit, edge cases, chord
  comparator and like-for-like comparison with Brox.
- SOURCE_MAP.md: prior work, pinned Lean blobs and interpretation limits.
- PREREG.md: unchanged original scope, inputs and falsifiers.
- REVIEW.md: historical reviews, external objection, appended erratum
  and source-exposed correction review.
- SHA256SUMS: administrative hashes of the current package.

No numerical result establishes the universal theorem. No new
computational gate, cross-architecture scientific result or Lean
verification is claimed. Repository CI verifies repository contracts;
it is not a formal proof of this mathematical replacement.

## Negative result and limits

The abstract hypotheses do not imply a uniformly positive least
eigenvalue. The symbolic semidefinite and positive-definite examples
remain; neither is asserted to be an actual automorphic theta family.

A Lean implementation must extract the all-real hfilt count identity
and prove finite-step Jensen/integration. The arithmetic inputs and
other error suppliers remain unchanged. In particular, Brox's bridge
already shows why no entire normalized x/m, xm/k, m or k/n^2 term
is removed by this substitution alone.

Any TWIST-J carrier, semistability construction, common algebra or
rapidity identification needs its own scoped work. None is established
or opened by this correction. Promotion requires a separately reviewed
public fold. Candidate-D is retained.
