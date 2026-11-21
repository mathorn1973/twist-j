# Original-operator resolvent audit

Status: CERTIFIED

**NON-CANONICAL / L1. Exact finite algebraic audit with a separate
analytical derivation.**

Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.
Reservation: [#1816](https://github.com/mathorn1973/twist-j/issues/1816).
Public input pin: `c4eee088d88f2da8dfab9e1f0c12249ad97c0b97`.

## Observed result

The first completed execution passed all **23 groups and 130 exact
scalar conditions**. No frozen falsifier fired. Both negative controls
produced the required nonzero discrepancy: the other radical sheet
and omission of the contact phase fail their respective moment
conditions.

The check starts with the original product coin and streaming matrix,
computes the full determinant and adjugate, and compares its integrated
contact numerator with the complete proposed even inverse. It does
not begin with the predecessor scalar formulas as its operator
definition and does not import the predecessor verifier.

The exact conditions confirm:

- the original determinant, complete adjugate support, and both
  integrated even contact inverse identities;
- the odd BB cofactor, full free odd function, all-coin contact update,
  and complete interacting fA/fB algebra;
- the gap H/G identity, positive even continuum numerator, and compact
  A cancellations at both endpoint momenta;
- consistency of the exterior small-root expansion with the first
  two return moments independently enumerated from the original walk;
- the complete rank-two transition matrix, its on-shell unitarity and
  positive denominator identity;
- determinant, trace and unitarity of the original pulse symbol.

These are identities over rational Laurent-polynomial rings, with an
explicit quadratic quotient where needed. They are not a finite grid
of sampled real momenta or rounded numerical agreement.

## Analytical consequences and limits

The companion `notes/C-BOUND-PAIR-RESOLVENT-AUDIT-N/PROOF.md` derives
the full original-operator contact reduction, selects the global
exterior sheet by contour continuation, and traces bound-pole residues,
the coarea factor and the periodic PV subtraction. Those analytical
steps are distinct from the finite stdout gate.

Its primary stationary-theorem audit uses the actual wave-operator and
resolvent conventions of arXiv:1912.04960v2. Applying equation (4.6)
and adjointing the entire on-shell operator gives the forward exterior
formula before the restricted output projection is applied. This
supplies the missing explicit convention argument without assuming
reciprocity of arbitrary selected transition probabilities. It
confirms the inherited factor `64*pi^2`; it does not reveal a numerical
error in #1815.

The complete scalar reduction used by the conditional absolute
certificate is supported by a different exact operator-based route.
This probe does **not** recompute P0, replay the old interval root
census/quadrature, audit every implementation line of #1815, or change
its interval, input windows, normalization or first-run record.

## Finite approximation contribution

The separately pinned `FINITE_PROTOCOL.md` gives explicit analytical
finite-support source and finite-range selective-readout approximations
for the exact original packet and event. It retains the bound
projector, positive right-moving pulse, K/E windows, all labels and
arbitrary old-memory/reference input. Its amplitude error ledger is

\[
\left|\sqrt{p_{\rm finite}}-\sqrt{P_0}\right|
\le\epsilon_S+\epsilon_D+\epsilon_-(N_-)+\epsilon_+(N_+).
\]

The construction supplies finite degrees for epsilon_S and epsilon_D.
The fixed-state quantitative scattering-time estimate is still open.
In particular the note's example with each source/readout error at
most `10^-6` remains conditional on a total time error at most `10^-6`.
Only under that additional certificate does it imply

\[
p_{\rm finite}\ge3.249\,10^{-9},\qquad
|p_{\rm finite}-P_0|<4.29\,10^{-10}<L/4.
\]

Those conditional bounds are analytical statements in the note, not
additional machine-certified gates or a supplied finite time. The
conservative finite-degree sizes are existence bounds, not practical
apparatus dimensions. Allowed coherent preparation/control, coefficient
loading and native autonomous realization remain separate premises.
Existing finite-interface/filter/local-execution owners remain in scope.

## Execution and acceptance

The public five-file readback completed at 2026-10-28 12:17:39 UTC.
The first scientific process began at
2026-10-28T12:17:59.246486+00:00 and completed at
2026-10-28T12:17:59.353991+00:00, exit 0 with empty stderr.
Exact stdout: 1171 bytes, 28 lines, SHA-256
`988edf0ef07e5e638217301b53dac7da1fb7a605954048022519dc4c0c687bf5`.

RUN.md records the complete custody inventory. The prospective code,
contract and analytical documents remain byte-identical to the pin.
The required x86_64/aarch64 PR replays are separate workflow evidence;
their outcomes are not anticipated in this first-run record.

A passing finite audit and cross-architecture replay do not provide
external independent acceptance, a finite-time experiment, native
preparation, physical units or a particle assignment. Public Canon
remains v106. This result changes no Canon, predecessor probe, release
or adopted physical claim.
