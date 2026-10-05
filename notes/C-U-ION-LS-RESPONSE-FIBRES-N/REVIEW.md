# Independent static audit of response-fibre compatibility

**NON-CANONICAL; analytical review only.** Date: 2026-10-05.
Three separately delegated agents checked the hand derivations and then
read the actual README.md. No verifier, scientific calculation script,
pulse sequence or experimental protocol was executed. This is not a public
preregistered run or a Canon promotion.

## What was checked

- Direct substitution into the native checkpoint table produces the thirteen
  symbolic response rows. Source labels t only repeat the observations.
- Arbitrary fixed functions of the six-vector are exactly represented by
  one unknown four-vector per response class and every native edge equation.
  No deterministic quotient map, extra labels or closing n=3->1 transition
  is assumed.
- The spanning-tree argument gives integer heights and signed cycle defects.
  The nine-edge bound makes every nonzero defect incompatible with all four
  Hodge eigenvalues. Consequently each consistent connected component has
  four free scalar parameters, and each inconsistent component is zero.
- For a=(0,1,2,3,5), B=74, all twelve displayed nonzero rows are distinct;
  the finite reading-value space has dimension sixteen.
- For a=(0,1,-1,-1,1), B=20, the stated self-loops and connections force
  every reading to zero despite the earlier affine nondegeneracy condition.
- The a=(0,0,1,1,0), B=6 two-cycle and the absence of a nonzero same-history
  two-step return under a1*a2*(a1-a2)!=0 both follow from the response table.
- The displayed polynomial can interpolate arbitrary finite node values.
  It is explicitly treated as target fitting, not a selected decoder.
- Normalization invariance, the finite-dimensional pseudoinverse identity
  and the relative residual bound are correct at their stated scope.

All reviewers requested the same precision in the continuity paragraph:
nearby readings must both remain affine and satisfy every exact two-step
intertwining equation. Affine form and continuity alone do not imply zero.
That hypothesis has been written explicitly in README.md.

## Scope retained

The graph uses only the six scored responses, not the full level-POVM
record. Its exact-equality test is not a tolerance rule for uncertain
calibration. The algebraic profiles are not measured devices, and generic
independence of their parameters is not a claim about available optical
controls. Sixteen degrees of freedom count values on the finite response
set, not the unrestricted extensions of f elsewhere.

The positive example establishes finite compatibility, including possible
nonzero axial readings and distinct readings of the two retained histories.
It establishes no physical decoder selection, robust error bound, global
invariant domain, unbounded continuation or physical-time interpretation.

No further mathematical correction remained after the stated clarification.
