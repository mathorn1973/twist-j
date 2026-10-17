# RESULT

**PUBLIC, NON-CANONICAL.**
Owner issue: #1168.
Author: A. M. Thorn.
Date: 26 September 2026.

## Verdict

- **candidate-C:** exact local child-conflict polynomials and recursive-series
  audit on one Linux x86_64 lane.
- **candidate-T:** the sibling-only recursive polymer majorant is supercritical
  at the physical cube activity `x=1/16`.
- **Fired route:** one-generation local sibling compatibility is insufficient
  to prove an absolute exponentially summable bound for all face-simple cube
  trees.
- **Not fired:** the true embedded face-simple tree sum. Nonlocal collisions
  were deliberately dropped by the majorant.
- **OPEN:** cyclic cube complexes, arbitrary neutral surfaces, full current
  covariance, uniform `Xi_L` and `Xi_L^(2)`, the massless phase and P1.

## Exact finite result

The frozen verifier derived

`
P6 = (1,18,111,308,429,294,79)
P5 = (1,15,74,154,143,49).
`

All six choices of planted parent face give the same `P5`.

No preregistered `y>1` certificate was found.

## Exact analytic explanation

For `t>=0`,

`
P5(t)-16t
 = 1-t+74t^2+154t^3+143t^4+49t^5
 > 0.
`

The quadratic `1-t+74t^2` is strictly positive because its discriminant is
`-295`; all remaining terms are nonnegative.

Hence `(1/16)P5(t)>t` for every finite `t>=0`. If the nonnegative
recursive majorant `T=xP5(T)` converged at `x=1/16`, its finite sum would
satisfy the fixed-point equation, a contradiction.

## Boundary

This result localizes the missing ingredient to nonlocal geometric exclusion
or signed resummation. It does not establish divergence of the actual embedded
tree activity and has no Canon consequence by itself.
