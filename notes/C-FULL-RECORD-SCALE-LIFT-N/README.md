# Reversible scale, precision and the full-step energy boundary

**PUBLIC / NON-CANONICAL / L1. Conditional analytical candidate-T.**
Author: A. M. Thorn. Apache-2.0.
Reservation: [#1771](https://github.com/mathorn1973/twist-j/issues/1771).

The specified full capture-and-record step now has an explicit reversible
integer-register representation retaining phase, relative scale and
occupied memory. Its exact precision can grow indefinitely at fixed
conserved accounts. The particular positive Borel energy reading is proved
to lack a uniform exponential bound in configuration distance.

These are results for the supplied Canon v105 model, not an original-native
derivation. The integer numerator 25 and the isolated-walk localization
method are credited to their existing owners. No Canon or public claim
status changes.

## Main results

Write `A=25 U_rec` on the full configuration basis over
`O=Z[zeta_20]`, with `A* A=A A*=625 I`.

| Question | Exact analytical result |
| --- | --- |
| Can a common scale be part of a reversible state? | Yes. For primitive integral `a`, `s=nu_5(Aa)` lies in `0,...,4`; `(m,a)->(m+2-s,Aa/5^s)` has the explicit adjoint inverse. All five values occur. |
| Is that unique common primitive representation local? | No. A remote pulse changes the common division applied to a token. The decoded amplitudes still obey the local `U_rec`. |
| Is there a local exact integer representation of the whole step? | Yes, in configuration coordinates: eight integer numerator entries and one denominator exponent per coefficient, with exact local alignment and division. The actual inverse has the same radius bound two. The alphabet and bit lengths are unbounded. |
| Does bounded conserved energy or charge bound exact precision? | No. One explicit full-model trajectory has least common denominator exactly `25^n`, while its trace account is 8, its active occupation charge is 10 and its spectral-energy distribution is constant. This is not a fixed-tolerance or work-cost lower bound. |
| Does localization admit an additive finite-five shadow? | No nonzero additive map exists from the full `O[1/5]` module to any abelian group killed by a fixed power of five. Nonlinear and enlarged native readings are not excluded. |
| Is the full spectrum gapped? | No: both spectrum and essential spectrum are the entire unit circle. |
| Is the selected positive Borel logarithm exponentially local? | No uniform exponential pulse-to-pulse kernel bound in `(R,r,x)` exists for this specific logarithm. An explicit free bulk band crosses its branch cut. Other generators remain open. |
| Does the selected energy agree with the earlier sum? | Exactly on the existing calibrated safe channel. Outside it, translated negative-band packets retain a discrepancy tending to `2*pi`, even far from contact. |

## Files and review order

1. [CONTRACT.md](CONTRACT.md): frozen analytical question, carrier,
   falsifiers and exclusions; public reservation before final drafting.
2. [PROOF.md](PROOF.md): full coefficient law, primitive chart, local
   alternative, all-time precision witness and additive-factor obstruction.
3. [SPECTRAL.md](SPECTRAL.md): full essential spectrum, energy identities,
   strong Borel-limit lemma and the exact locality obstruction.
4. [ARITHMETIC_REVIEW.md](ARITHMETIC_REVIEW.md): separately reasoned
   same-session audit of inherited arithmetic and the new scale boundaries.
5. [VALIDATION.md](VALIDATION.md): authority, source custody, review scope,
   repository checks and delivery status. `SHA256SUMS` binds these files.

The proofs are universal analytical arguments. No scientific program,
numerical scan, expanded circuit or formal probe was executed. Multiple
same-session analytical reconstructions are recorded; they are not
independent external acceptance or two-architecture computation evidence.

## What remains to derive

The exact coefficient representation still stores amplitudes on the
configuration space of an object pair, carrier and memory. It has not
been turned into bounded material registers at physical sites. Arbitrary
integer operations have not been compiled into the admitted original
native gate alphabet or timed by the original selector. The supplied
geometry and contacts, physical energy selection, finite preparation,
occurrence, controlled approximation and replenishment retain their
separate obligations.

A finite realization must state which precision, error and time domain
it permits; an all-time error guarantee requires its own proof.
A proposed new energy must carry its own
locality proof; the nominated scalar logarithm cannot inherit the
isolated object's gap-based estimate.

## Prior results retained at their actual scope

- [Canon v105](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md):
  specified homogeneous capture/current/occupied-record theorem and object
  spectral reading.
- [#1741](https://github.com/mathorn1973/twist-j/issues/1741): complete-step
  numerator 25 and raw token-output reduction obstruction, already public.
- [#1739](https://github.com/mathorn1973/twist-j/pull/1739): isolated-walk
  localization and a distinct declared residue/native network.
- [#1614](https://github.com/mathorn1973/twist-j/issues/1614): separate
  funded-machine finite-precision boundary.
- [#1768](https://github.com/mathorn1973/twist-j/pull/1768) and
  [#1770](https://github.com/mathorn1973/twist-j/pull/1770): separate
  thermal/retention/reuse constructions, not replaced or promoted here.
