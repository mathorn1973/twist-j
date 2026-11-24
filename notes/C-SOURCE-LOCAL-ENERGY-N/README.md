# A source-specific nearest-neighbor energy obstruction

**NON-CANONICAL. L1. Conditional analytical candidate-T.**
Author: A. M. Thorn. Date: 2026-10-26. Apache-2.0.
Reservation: [#1784](https://github.com/mathorn1973/twist-j/issues/1784).
Promotion dossier: PROMO-C-SOURCE-LOCAL-ENERGY-N.
The prospective [CONTRACT.md](CONTRACT.md) is frozen at
`a07b8909d2926e223549433528a189a80d14bc09`.
Independent scientific acceptance is not asserted.

The preceding result left open whether the original prepared family
could admit a sufficiently accurate short-range realization of its
selected energy. For physical interaction diameter at most one, this
note answers negatively on **one fixed actual prepared source**, not
on an unrelated whole-code state:

    ||H_tilde V psi_+ - V Q psi_+|| > 2E0/5.         (R1)

Here Q=E0 f(U_rec), with the unchanged positive logarithm branch and
f(1)=0, psi_+ is the original prepared plus setting, and V is the
original occupation isometry tensored with a fixed data-independent
ancillary ready state. The required error E0/1200 is therefore exceeded
by a factor greater than 480. The result is uniform in all admitted
old-memory/reference inputs. Its proof does not require positivity,
charge conservation or a bound on the strength of individual terms,
so it also applies to the desired positive charge-conserving subclass.

## 1. Why this is a prepared-source result

Both object constituents occupy odd physical sites throughout the
support of psi_+, since this source uses only the even powers 0,+2,-2
of U_rec on the seed at 97. The normalized test vector
w=U_rec^(-1)chi has the object constituents at both even sites 96 and
98. Every term supported on one site or two adjacent sites omits at
least one of these two required changes. Consequently

    <Vw,H_tilde Vpsi_+>=0.

The target energy has a quantitatively nonzero matrix element in that
same direction. A sign-definite trigonometric inequality and exact
short moments give

    Im <w,Qpsi_+>
       >= E0 (Z/4+1/100)/sqrt(Z)
       > 259E0/640 > 2E0/5,
    Z=(39521+154 sqrt(5))/15625.

This proves (R1) directly. It does not use a triangle-inequality witness
that merely says one of two settings must fail. Allowing a different
nearest-neighbor Hamiltonian or fixed ready state for the other setting
does not repair the plus setting. No numerical spectral integration,
large matrix, source-tail enumeration or scientific executable is needed.
The full argument and its domains are in [PROOF.md](PROOF.md).
The lower bound uses the exact step, source and logarithm; it does not
depend on the preceding cut-mass estimate, absence of a spectral atom
at the cut, or enormous finite-polynomial approximation.

## 2. What is and is not excluded

The physical range is measured in the original lattice, including the
original diagonal occupation gauge. The ready ancilla can be entangled
across its own sites; it is initially independent of the source data.
Identity spectators and all passive reference correlations are retained.
For infinite sums the compared action and the stated local matrix-element
limit must exist, as specified in the proof.

The obstruction applies to energy action on the original bare encoding.
It does not exclude the declared local discrete step, an approximation
to time evolution alone, a separately accounted data-dependent dressed
encoding, another declared energy law, or interactions of diameter two
or greater. In particular, the new lower bound does not say that the
trillion-site sufficient construction is necessary. It closes the
nearest-neighbor class of the present energy question.

Neither source energy equality nor the previously proved receiver
contrast is withdrawn. Those statements concern the ideal selected
operator. This note shows that its energy action cannot be implemented
to the requested tolerance by the frozen nearest-neighbor class.
No thermal preparation, funded terminal readout, renewal, empirical
calibration or native six-pentit derivation is supplied.

## 3. A finite next test for diameter two

The witness above stops being forbidden when a term may touch sites
96 and 98 together. The next geometric class is therefore rho=2.
[FILTERED_TAIL.md](FILTERED_TAIL.md) gives an analytical finite
certificate that avoids approximating the entire discontinuous logarithm
to high uniform accuracy: multiply it by a centered polynomial vanishing
at its cut, project onto sufficiently remote carrier positions, and
bound the omitted Fourier coefficients exactly.

This is a method for a future prospectively pinned test. No projected
norm has been evaluated, no passing diameter-two witness is claimed,
and a small projected norm would not establish a local construction.
The source, energy branch and tolerance remain fixed.

## 4. Authority and frozen sources

The sole authority remains ACTIVE Public Canon v105. Public main and
peeled canon-v105 are `892a0b11089d34e241e1eb76d2c03247022d18e6`;
the content commit is `b8cdfd6ea58ae798545bc6000c817147fa0f0dcc`.
The 1,295,029-byte Canon has SHA-256
`73894f331dac3226fe30c86f1ccd893bc2761b0220557e0bfb374d049aa2fa31`.

| Source | Frozen commit | Role |
| --- | --- | --- |
| [PR1783](https://github.com/mathorn1973/twist-j/pull/1783) | `9e765fcef4c9e4917c25a49eebce8f052fc9a961` | Previous energy realization and geometric boundary. |
| [PR1781](https://github.com/mathorn1973/twist-j/pull/1781) | `5f7301e4d891596628cb25c6e735a7e4cd9004a8` | Original source spectral and finite occupation constructions. |
| [PR1779](https://github.com/mathorn1973/twist-j/pull/1779) | `c2b06d3ee52778f804da1f84ba9f963bae1ad46e` | Whole-code norm obstruction, distinct compact apparatus. |
| [PR1777](https://github.com/mathorn1973/twist-j/pull/1777) | `191ab035be823bd9d6fdc9effba81528fa026e49` | Exact active source, moments and preparation. |
| [PR1772](https://github.com/mathorn1973/twist-j/pull/1772) | `3abf054e435e31c51e6e50528b09fe3cf7cffe13` | Nominated positive logarithm. |

These unmerged results retain their conditional scopes. PR1779's separate
PASS24/24 does not cover the successors. No public external review of
PR1783 was recorded at this reservation. Same-session authoring and
adversarial checks are internal verification only. Scientific review
and repository integrity are separated in [VALIDATION.md](VALIDATION.md).
