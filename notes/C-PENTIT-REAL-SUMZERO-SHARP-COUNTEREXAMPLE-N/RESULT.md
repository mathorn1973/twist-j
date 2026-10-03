# Result: the proposed global value is false; a sharper interval remains

**NON-CANONICAL / candidate-T / L1.**
Exposed analytical results, independently checked within this collaborative
session, with one exact x86_64 confirmation audit after the public pin.
No Registry, Canon, original note or physical contract is changed.

## Counterexample

For the original phase-point convention, the normalized real sum-zero state

$$
\psi_j=\sqrt{\frac25}\cos\left(\frac{2\pi j}{5}+\frac\pi{20}\right)
$$

has negativity

$$
\boxed{\mathcal N(\psi)=\frac{\sqrt{5+2\sqrt5}}{10}
<\frac{1+\sqrt5}{10}=\frac\varphi5.}
$$

The difference of the compared squares is exactly `1/100`.
Thus the conjecture that the finite-census minimum `phi/5` is also the
minimum over **all** normalized real sum-zero states is refuted.
`PROOF.md` contains the explicit table, sign proof and four-source embedding.
This witness is an upper bound, not a proved global minimizer.

## Stronger general lower bound

For every normalized real sum-zero pentit state,

$$
\boxed{\mathcal N(\psi)\ge\frac12\tan\frac\pi{10}
=\frac1{2\sqrt{5+2\sqrt5}}.}
$$

`LOWER-BOUND.md` proves this through the real cyclic self-convolution,
the fixed Fourier one-norm and a positive transport decomposition.
It improves the previous `sqrt(5)/20` lower bound. The exact global minimum
exists and is now bounded by

$$
\frac1{2\sqrt{5+2\sqrt5}}
\le\min\mathcal N
\le\frac{\sqrt{5+2\sqrt5}}{10}.
$$

Sharpness of either end remains open. Reality, normalization, dimension
five and the fixed Wigner convention are part of the claim.

## Audit and falsifiers

- Public pin: `fd41b1cb5662983a34742829807d9c510014242c`, read back exactly
  before execution.
- Exact audit: **148/148 PASS**, exit 0, CPython 3.12.14, Linux x86_64;
  stdout 361 bytes, SHA-256
  `a5df30dac7256d9894ec99268faca3885fa2bf4091292c4bf98e1d7ac5e1f64f`.
- Separate proof/source/security review: accepted at the stated scope.
  Review independence means separate reasoning in this same session,
  with exposed targets; no external referee or second software implementation.
- Fired scientific falsifier: the proposed universal `phi/5` value fails.
  No preregistered audit assertion or proof premise was found to fail.

The exact audit is finite witness confirmation. It does not purport to
verify all real vectors or to replace the general lower-bound proof.

## Preserved conclusions and remaining construction work

The complete #1343 note remains byte-for-byte unchanged. Its 624-state
balanced-source census, finite minimum `phi/5`, real sum-zero Wigner
negativity, line-reader obstruction and bounded resource results are
not contradicted by this extension to arbitrary real source coordinates.

No preparation of the witness by the native automaton is supplied.
No native line-measurement/fresh-coordinate implementation, actual-event
transducer, Born/occurrence origin or renewal law has been obtained.
The counting branch's `STOP_APPLICABILITY / H_NOT_TESTED` remains unchanged.
The result closes a mathematical extrapolation and strengthens its bounds;
it is not an additional physical completeness milestone.

The nearest construction question remains a fixed native or explicitly
extended apparatus that implements the proposed line instrument, records
actual events, and accounts for the fresh continuation coordinate and its
renewal. Its finite initial ensemble and event map must be specified before
counting; supplying Born weights as that ensemble would not derive their
origin. The present bound concerns the declared 25-point representation and
does not rule out a larger context-dependent apparatus. Further optimization
of negativity is not a prerequisite for attempting that construction.
