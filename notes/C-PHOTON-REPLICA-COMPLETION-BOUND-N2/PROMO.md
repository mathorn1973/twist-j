# PROMO-C-PHOTON-REPLICA-COMPLETION-BOUND-N2

**NON-CANONICAL review package. No promotion is performed here.**
Owner issue: #1165.
Basis: Public Canon v92.

## Candidate for later fold

A later reviewed fold may consider the following narrowly scoped mathematical
statement.

### Candidate statement

For the full finite two-replica photon measure already used in the v92 photon
program, there is a positive charge-faithful auxiliary wiring with opposite
pairs and at most one equal-sign block of size five or ten at each edge. The
local partition weights are

`
lambda(m,h)=1/(binom(r+h,h) r!),  r=(m-h)/2.
`

They reproduce the exact modulo-five constraint, and the large-block size is
exactly five times the magnitude of the replica-current difference.

After signs are summed, a target-edge completion has exact relative mass

`
1{consistent} 2^k lambda(m,h).
`

The already published all-distance neutral-tube family supplies admitted
conditionings for which two separated charged blocks are connected with
conditional probability one. Hence the proof route requiring one universal
conditional transmission factor `q_*<1` is closed negative at this scope.

## Evidence

- written proof: `README.md`
- preregistration: `PREREG.md`
- exact verifier: `verify.py`
- first successful run: `RUN.md`
- result boundary: `RESULT.md`
- frozen successor pin:
  `fdd1662ec3f828db20c9982a6821e12628863e55`
- finite audit status: candidate-C on one x86_64 lane
- theorem status: candidate-T pending separate mathematical review

The consumed predecessor #1164 is retained separately with its failed first
audit and exact fixture diagnosis.

## Fired route

**Closed negative only for:**

`
uniform conditional thinning after arbitrary admitted support/exterior
conditioning by a fixed q_*<1.
`

This is not a negative result for the full model.

## Missing estimate

The central missing quantity remains an **unconditional weighted estimate**.
Neither this package nor #1163 supplies a constant independent of volume for

`
Xi_L
`

or

`
Xi_L^(2).
`

The deterministic tube family shows why an argument based only on worst-case
conditional continuation cannot provide such a constant. A viable next attack
must include the probability cost of producing the support, preserve signed
cancellation, or both.

## P1 boundary

P1 remains OPEN. In particular this package does not supply:

- a uniform upper bound on the full current susceptibility;
- a strict positive macroscopic comparison `b_lower > 25 chi_upper`;
- an infinite-volume profile theorem;
- rotational restoration or spectral transfer;
- a massless phase theorem;
- a physical-photon or apparatus statement.

## Recommended next attack

Use the charge-faithful representation to perform an **unconditional polymer
budget** rather than a conditional branching comparison.

Freeze a connected auxiliary component `K` only through its discovered
support and sum all compatible face data, signs and local wirings inside it
while leaving the exterior summed. Seek a bound of the form

`
E_2aug sum_{K contains e} W(K) Phi(K)
 <= sum_{connected supports S contains e} z(S) Phi(S),
`

with an exact activity `z(S)` that already includes the face weights and the
`2^k lambda` completion factors. The first target is not exponential decay
itself but a finite exact inequality showing that the total activity added by
one new neutral sheet is compensated by its face-weight cost after all
compatible completions are summed.

If that fails, preserve the counterexample. If it succeeds with a summable
activity, feed the resulting moment directly into the signed axial quotient,
not into an independent-per-edge percolation surrogate.
