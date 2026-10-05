# Static proof, scope and security review

**NON-CANONICAL / L1 / same-session collaborative review.**
Date: 2026-10-02. Work item:
`C-PENTIT-REAL-SUMZERO-SHARP-COUNTEREXAMPLE-N`.

**Disposition: ACCEPT AT THE STATED SCOPE; RUNTIME PENDING.**
No algebraic, convention, scope or source-security blocker was found in the
four reviewed files. This review author did not execute `verify.py`, a scientific
gate, the original census, a numerical search or another scientific program.
Read-only source inspection and file hashing are not runtime evidence.

## Review identity and exposure

This is a separate source/proof check within the same authorized collaborative
session that developed the witness and lower bound. Both targets were already
exposed. A collaborating agent also performed a separate analytic pass and read
the verifier, without execution. Neither pass is an external referee review,
blind test, independently authored software implementation, second-architecture
execution or independent laboratory result. The earlier lower-bound check is
part of this same review history, not an additional external acceptance.

Only `REVIEW.md` was written by this review author. The proof, preregistration
and verifier files were not modified.

## Exact bytes inspected

The following files were completely read and their final proposed bytes were
hashed before any execution by this reviewer:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `PREREG.md` | 5802 | `8045eeae7d8f36be688df1b301c0749c7da64a1082cd45d6e4f1514973f09954` |
| `PROOF.md` | 4426 | `3e7c3907b461e461d6f3b08c05fd39d7b1cb918c77f6cc3c4c6e6db3f59781c3` |
| `LOWER-BOUND.md` | 6211 | `c1f26feee3ca960c6ac678877aed943c878b74d8a80322ee04c8804543db7762` |
| `verify.py` | 9849 | `40c09412631014aae23eb18715b49c9556ee2211d3f7bda10675f1669fc855e1` |

This table identifies reviewed local bytes. It is not a public commit pin,
GitHub readback, execution receipt or retrospective preregistration. A change
to a reviewed input requires review of the changed bytes before claiming this
acceptance for a new pin.

## Analytical witness and conventions

The phase convention is consistently
`A(q,r)|j> = zeta5^(2*r*(q-j)) |2*q-j>` and
`W(q,r) = Tr(rho*A(q,r))/5`.

For the normalized real cosine family, character sums prove zero sum and norm
one. Substitution `j=q+t` produces the constant strips at `r=1,4`, not at
`q=1,4`. At the specified angle `alpha=pi/20`, the zero-momentum row is
`(C,-C,S,0,-S)/5`, with `C=cos(pi/10)>0` and `S=cos(3*pi/10)>0`.
The 12 positive, 2 negative and 11 zero entries follow from this analytic sign
certificate. The exact identities give
`N^2=(5+2*sqrt(5))/100` and the proposed-bound squared gap `1/100`.
Positivity of both compared quantities makes the squared gap a strict
counterexample, without a decimal approximation or optimization.

The four-source augmentation using `v_i=c_i-c_0` recovers the cosine vector
exactly and has squared norm `5/2`. It belongs to the larger declared real-source
reading. It is not asserted to be one of the 624 balanced-source preparations
or a natively prepared state. The original finite census remains unchanged.

## General lower bound

The lower bound has a complete analytic argument for every normalized real
sum-zero vector in dimension five. It does not rest on a finite search.

The cyclic convolution is `c=psi*psi`, not an autocorrelation. For the
unnormalized Fourier transform, `hat(c)=hat(psi)^2`; Parseval for `psi` gives
`sum |hat(c)|=5`. The zero-frequency term vanishes. Reality and zero sum allow
the positive transport decomposition with total mass `p`, after proving
`c!=0` and `p>0`. Every nonzero difference modulo five permutes the four nonzero
frequencies. The common chord sum is `2*cot(pi/10)`, so
`5 <= 2*p*cot(pi/10)`. The row is a permutation of `c/5`, giving row negativity
`p/5` and total negativity at least `(1/2)*tan(pi/10)`.

The normalization, factor five, factor one-half, principal-root identity and
squared improvement over `sqrt(5)/20` are consistent. The proof does not assert
that the total negativity attains this lower bound, and does not make an
unqualified composite-dimension extension. Reality is essential to this
argument.

Compactness and continuity correctly establish existence of a global minimum
in the normalized real sum-zero class. Its exact value remains open between
the stated lower and witness upper bounds.

## Static verifier audit

The quotient polynomial is `Phi_40(t)=t^16-t^12+t^8-t^4+1`, with the supplied
principal embedding `t=exp(i*pi/20)` and `zeta5=t^8`. Polynomial reduction,
negative powers, conjugation and exact rational divisions are consistent with
that convention. The source exponents `8*j+1`, phase exponents
`16*r*(q-j)`, and density normalization `5/2` match the proof.

The direct route constructs the source density and all phase matrices, then
compares all 25 trace-derived cells with the known analytic table. It checks
Hermiticity, involutions, density normalization and idempotence, exact zero
support, total Wigner weight and `sum W^2=1/5`. Negativity is computed from the
two analytically certified negative trace values. The sign certificate is
explicitly proof-supplied; no general algebraic-number sign algorithm is
claimed. Shared exact arithmetic means this is not an independent software
implementation of the target.

**The verifier does not enumerate arbitrary real states or prove the general
lower bound.** It audits one exposed counterexample and finite identities.
Its stdout does not report a software PASS for the universal lower bound.
`LOWER-BOUND.md` supplies that separate mathematical proof. A successful run
would not establish a global minimizer, native preparation, occurrence law,
renewal, Gate 0 completion or Canon status transition.

## Static security and execution boundary

The source imports only `dataclasses`, `fractions` and `sys`. Inspection found
no network access, file input/output, subprocess or shell invocation, dynamic
execution, deserialization, external data, randomness, third-party imports or
credential access. Computation uses exact `Fraction` coefficients and bounded
loops; output consists of stdout lines. Failed conditions raise exceptions,
and the explicit checks are not disabled by Python's optimization flag.
The replay rejects runtimes outside Python 3.12.

No runtime success, exact stdout hash, exit status, empty-stderr claim or
architecture identity is certified here. Those remain **PENDING** until the
public input pin is read back and the authorized execution occurs. Notes-only
CI is not a replay of this verifier. Any later execution receipt should be
recorded as a separate dated addendum, leaving this pre-run review's scope and
history explicit.

## POST-RUN RECORD REVIEW — 2026-10-02

**Disposition: ACCEPT RECORDED CUSTODY AND STATED SCOPE.** This dated addendum
follows the coordinator's reported first execution. The preceding static text
and its historical `RUNTIME PENDING` disposition are retained unchanged.

The review author completely read `README.md`, `RUN.md`, `RESULT.md` and
`EXPECTED.txt`, including the final construction-handoff paragraph added to
`RESULT.md`. This was a record/source review, not a verifier execution,
replication, second architecture or independent experiment. No scientific
program was imported or run by this reviewer.

### Local source and stdout custody

Read-only hashing and byte counts of the four frozen inputs still give exactly
the SHA-256 values and sizes in the pre-run table. Their locally computed Git
blob IDs also match the execution receipt:

| File | Git blob |
| --- | --- |
| `PREREG.md` | `510b2a36310b2bc1bf9dae55c4b9070a9580189b` |
| `verify.py` | `2bfa12c1e7cdaa35f9775da1c5103feb96fb8abf` |
| `PROOF.md` | `9b46aaa6b3d3ecf2bfc8ba78974da2734d0c45f0` |
| `LOWER-BOUND.md` | `3916cc24d0e108593524f7d066b8cb8d23215a6a` |

`RUN.md` records the public input pin
`fd41b1cb5662983a34742829807d9c510014242c`, tree
`ef61af43d499c5b4150d91716c4c088747f04390`, public readback of all four inputs
before execution, and their unchanged post-run hashes. The local-byte comparison
is consistent with that record. This reviewer did not independently perform
or observe the coordinator's public API readback or execution ordering.

The existing stdout artifact was read and hashed directly, without generating
or reconstructing it:

| Artifact | Bytes | SHA-256 | Git blob |
| --- | ---: | --- | --- |
| `EXPECTED.txt` | 361 | `a5df30dac7256d9894ec99268faca3885fa2bf4091292c4bf98e1d7ac5e1f64f` | `dc29b8ac772adbf0405971b4616271b72d3edc9d` |

It reports `exact_checks=148 status=PASS` and the expected witness identities,
support and exposed analytic sign basis. These bytes, hash and blob match
`RUN.md` and `RESULT.md`. The source's bounded check structure is consistent
with the reported 148 checks. The receipt reports exit zero on Linux x86_64,
CPython 3.12.14, after public readback; the tool returned no error text.
These are recorded execution facts, not a new independent execution certified
by this review.

### Result and scope review

The final artifacts correctly distinguish:

- the explicit counterexample to the proposed universal value `phi/5` from
  the unchanged 624-preparation census and its finite minimum;
- a rigorous witness upper bound from an unproved global minimizer;
- the separate universal analytic lower-bound proof from the finite software
  confirmation of one exposed witness and its identities;
- same-session separate reasoning from external referee independence;
- one recorded x86_64 run from a second implementation or two-architecture
  scientific gate; and
- candidate-T notes evidence from any public Registry or Canon promotion.

The stdout has no claim to check every real vector or to establish the general
lower bound by a finite census. The claimed global minimum interval and its
remaining open exact value agree with the reviewed proofs. The counterexample
fires the conjectured all-real extension's mathematical falsifier, not a frozen
audit assertion or a physical falsifier.

The new construction-handoff paragraph is properly bounded. A future fixed
native or explicitly extended apparatus still needs its actual event map,
initial ensemble, line-instrument implementation and complete fresh-coordinate
renewal account. Supplying target Born weights would not derive their origin.
The current 25-point result does not exclude larger context-dependent apparatus,
and further negativity optimization is not required before attempting that
separate construction. `STOP_APPLICABILITY / H_NOT_TESTED`, native preparation,
actual occurrence and physical realization remain unchanged.

No correction or blocker was found in these completed artifacts at this scope.
This addendum approves their recorded custody and presentation only; it adds no
scientific run or authority. Only this review addendum was written by the review
author, and none of the frozen inputs or execution artifacts was modified.
