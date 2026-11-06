# Smaller source-energy bounds and bounded-order physical interactions

**NON-CANONICAL. L1. Conditional analytical candidate-T.**
Author: A. M. Thorn. Date: 2026-10-26. Apache-2.0.
Reservation: [#1782](https://github.com/mathorn1973/twist-j/issues/1782).
Promotion dossier: PROMO-C-SOURCE-ENERGY-REFINEMENT-N.
The prospective [CONTRACT.md](CONTRACT.md) is pinned at
`d69ff34274ffce191055df7fd44e092366e20819`.
No independent scientific acceptance or Canon promotion is asserted.

The preceding source-energy construction proves a finite physical
realization, but its sufficient region has about 5.2*10^30 lattice sites
and its displayed interaction involves the whole block. This successor
reduces the proved sufficient region to **6,459,630,813,009 sites** and
replaces that interaction by an exact decomposition of a positive
Hamiltonian into Hermitian terms using at most **ten occupation
coordinates, twenty encoded qubits and
seven physical sites**. The resulting terms still have large spatial
range and incidence. The same original source, energy branch, occupation
encoding and comparison tolerances are retained.

## 1. Results and their physical scope

| Result | Established conditional statement | Remaining limitation |
| --- | --- | --- |
| [SHARP_SPECTRAL.md](SHARP_SPECTRAL.md) | The actual normalized source has cut mass at most 512*eta for 0<eta<=1/1000, using exact pole subtraction and the complete contact formula. | This is an analytical bound for the frozen model, not a measured spectral density. |
| [FEJER_RADIUS.md](FEJER_RADIUS.md) | A positive Fejer polynomial of degree D=2^35-1 gives source energy-action error <E0/1200. Radius L=47D+3 suffices for the complete time comparison and write contrast >1/100. | The trillion-site upper bound is still enormous; it is not a necessary size or an implemented matrix. |
| [FEW_BODY.md](FEW_BODY.md) | An exact Gram-form extension on the original occupation factors intertwines the entire finite code, is positive and charge conserving, and has the support counts above. | The raw higher-charge completion changes. Total raw norm, term count, incidence and geometric range can be large. |
| [LOCALITY_BOUNDARY.md](LOCALITY_BOUNDARY.md) | Any exact finite-diameter decomposition of this entire finite generator requires a term of diameter at least 2D, even with a fixed data-independent ancillary state. | Its witness is exponentially small and is not a prepared source. It does not exclude an accurate short-range approximation on the prepared family. |

These four notes contain 32 separate scientific review obligations
(7+9+9+7). Same-session analytical and adversarial checking found no
substantive defect; it does not discharge independent review.

## 2. Frozen model and authority

The sole authority remains ACTIVE Public Canon v105:

- Main and peeled `canon-v105`:
  `892a0b11089d34e241e1eb76d2c03247022d18e6`.
- Canon content commit:
  `b8cdfd6ea58ae798545bc6000c817147fa0f0dcc`.
- `canon/CANON.md`: 1,295,029 bytes; SHA-256
  `73894f331dac3226fe30c86f1ccd893bc2761b0220557e0bfb374d049aa2fa31`.

The conditional predecessors are pinned, not silently folded into Canon:

| Source | Frozen commit | Inherited premise |
| --- | --- | --- |
| [PR1781](https://github.com/mathorn1973/twist-j/pull/1781) | `5f7301e4d891596628cb25c6e735a7e4cd9004a8` | Actual-source spectral formula and original finite occupation block. |
| [PR1779](https://github.com/mathorn1973/twist-j/pull/1779) | `c2b06d3ee52778f804da1f84ba9f963bae1ad46e` | Sharp global norm obstruction and distinct compact apparatus. |
| [PR1777](https://github.com/mathorn1973/twist-j/pull/1777) | `191ab035be823bd9d6fdc9effba81528fa026e49` | Original active pair and complete preparation. |
| [PR1772](https://github.com/mathorn1973/twist-j/pull/1772) | `3abf054e435e31c51e6e50528b09fe3cf7cffe13` | Nominated positive spectral logarithm and full-circle spectrum. |

The separate [review of PR1779](https://github.com/mathorn1973/twist-j/pull/1779#pullrequestreview-5648760727)
reports PASS 24/24 at that PR's own conditional scope. It does not review
PR1781 or this successor. No public review of PR1781 was recorded at
this successor's prospective reservation.

Keep U=U_rec, Q=E0 f(U), f(exp(-i theta))=theta for 0<=theta<2pi,
and f(1)=0. The unchanged source is

    psi_±(Xi)=[I±(U²-U^-²)]chi(Xi)/sqrt(Z),
    Z=(39521+154 sqrt(5))/15625.

The energy and full-state comparisons admit all 26 old-memory labels,
arbitrary passive references and a retained orthogonal setting register.
The fresh-write contrast retains the original 25-label old-memory
subspace excluding d0. No source is filtered or reselected.

## 3. Complete error and resource statement

For J=2^35 and D=J-1, the fixed positive polynomial satisfies

    0<=q_J<=2pi,
    ||[E0 q_J(U)-Q]psi|| < E0/1200.

The finite construction has L=47D+3 and 4L+1=6,459,630,813,009 sites.
Its complete state error is less than 3/1200+2^-17 throughout
|E0 t/hbar|<=3. At s=3 the ideal receiver contrast exceeds
3/200-2^-16. With the stated additional input, complete-generator and
final-effect tolerances it exceeds 3/200-2^-16-1/1000>1/100.

The boundary allowance is explicitly 2^-17, replacing the predecessor's
stricter 2^-62. This reallocation is part of the full error proof; the
source energy-action and receiver thresholds have not changed. Both
ideal settings retain exactly equal complete energy distributions.
Those common distributions approximate the original energy law and
are not claimed to equal it exactly. Generic calibration errors need
not preserve the exact equality between settings.

The complete original inventory remains 38 occupation coordinates per
site, of which 29 are active and nine are spectators. The predecessor's
four-level representation uses two qubits per coordinate. The bound of
twenty qubits is PER HERMITIAN TERM, not the total apparatus size or a
claim of a two-qubit gate implementation. No physical ancillary register
is added by the Gram proof.

For d_code=8112(2L+1)^3, the displayed decomposition has at most
d_code(d_code+1)/2 terms, each of norm at most 2pi E0. The total positive
raw operator has norm at most 2pi E0*d_code, while its finite-code norm
is at most 2pi E0. Every nonzero displayed term touches receiver 100.
Term diameter is at most 4L and exact full-code agreement requires at
least one term with diameter at least 2D. These facts rule out reading
bounded interaction order as bounded spatial range or incidence.

## 4. What this leaves open

The most consequential next question is whether the same prepared
family admits a sufficiently accurate short-range energy realization
with fully counted resources. The exact full-code witness does not
settle that approximation problem. The prepared-source necessary bound
in [LOCALITY_BOUNDARY.md](LOCALITY_BOUNDARY.md) reduces one route to a
specific energy-tail norm; no nonzero quantitative lower bound for that
tail is claimed here. A future computation needs its own prospective
code, input, output and threshold pin before execution.

An ancillary or effective model must separately control energy action,
the ready state, dressing, physical decoding and the complete output.
A positive two-level counterexample shows why uniformly accurate time
evolution alone does not certify energy action on the same bare input.

This work does not provide thermal preparation, funded terminal readout,
renewal, empirical calibration of E0, a native six-pentit derivation or
identification with PR1779's separate 140-gate apparatus. The original
global uniform approximation obstruction remains intact. Repository
integrity and scientific acceptance are separated in
[VALIDATION.md](VALIDATION.md).
