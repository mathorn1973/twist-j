# Coherent readiness is a separate resource

**NON-CANONICAL / L1 / conditional analytical candidate-T.**
Author: A. M. Thorn <thorn@twistj.com>. SPDX-License-Identifier: Apache-2.0.
Reservation: #1803. No scientific executable or numerical experiment is used.

This note concerns the exact finite battery and preparation in PROOF.md.
The stationarity argument is inherited elementary covariance, also used in
#1793 and #1768. Its specialization quantifies the preparation requirement
of this two-coordinate packet. It does not derive that preparation.

## 1. Nondegenerate spectrum and stationary comparison

Let M>=1, 0<=m,n<=M+3, and

    H_B |m,n> = (4m+2sqrt5 n)|m,n>.

The spectrum is nondegenerate. Equality of two levels implies
2(m-m')=-sqrt5(n-n'); irrationality of sqrt5 forces both differences to
vanish. Consequently every stationary density sigma_B is diagonal in this
basis. The ready vector beta_M has coefficients

    beta_(r+1,s+1) = [2/(M+1)] sin(pi r/(M+1)) sin(pi s/(M+1)),
                      1<=r,s<=M,

and zero coefficients elsewhere. It is normalized by the product of the
two finite sine identities in PROOF.md. Thus

    <beta_M,sigma_B beta_M> <= max_(m,n) |beta_(m,n)|^2
                           <= min(1,4/(M+1)^2).                 (P1)

Measuring the projector |beta_M><beta_M| gives

    (1/2)||sigma_B-|beta_M><beta_M|||_1
        >= max(0,1-4/(M+1)^2).                                (P2)

For M=1 the packet is sharp and this bound is zero. For M>=2 it has
coherence between distinct energies. Increasing M improves the proved
implementation-error bound and makes a stationary substitute increasingly
distinguishable.
These are lower bounds, not a sharp trace-distance optimization.

## 2. Including all preparation resources

Let the complete initial preparation state rho_BD commute with

    H_prep=H_B tensor I_D + I_B tensor H_D,

and let the preparation unitary Y commute with H_prep. If a preparation
Hamiltonian is unbounded, stationarity means invariance under its full
unitary group, and conservation means commuting with that group for every
real time; this convention also applies in Section 3. The final joint
state remains invariant under exp(-it H_prep). Partial trace over D then
makes its battery marginal invariant under exp(-it H_B). Hence (P1)-(P2)
apply. This covers correlated stationary inputs as well as products of
stationary factors. Increasing their energy or changing temperatures does
not remove the premise.

An energy-conserving protocol must therefore receive nonstationarity from
somewhere, or change the complete energy/preparation boundary. Naming a
controller or a phase reference does not remove it from that accounting.
This is not a prohibition of heat flow or work extraction; the target here
is the specified battery coherence.

## 3. A narrow coherent donor has an exact limitation

Here is a further conditional necessary condition for exact preparation.
Let a single donor have a bounded Hamiltonian Q_D of spectral width W_D.
Prepare it independently of all other resources; the complete state of
those other resources, including the initial battery, is stationary for
their additive energy. Let the entire preparation unitary conserve that
additive energy. The resulting donor-to-battery channel Phi is covariant:

    Phi(e^(-it Q_D) rho e^(it Q_D))
      = e^(-it H_B) Phi(rho) e^(it H_B).

This follows by moving the joint time translations through the conserving
unitary and tracing the other factors. Its dual sends a battery matrix
unit of Bohr frequency omega to a donor operator of the same frequency.
For every bounded donor operator O,

    ||[Q_D,O]|| <= W_D ||O||,

after subtracting the midpoint of the donor spectrum. Therefore such a
dual matrix unit is zero when |omega|>W_D. The corresponding battery
coherence must vanish for every donor input.

The two occupied extreme coordinates (2,2) and (M+1,M+1) have a nonzero
matrix element in |beta_M><beta_M| and energy separation

    Delta_ready=(4+2sqrt5)(M-1).

Exact preparation under this donor contract consequently requires

    W_D >= (4+2sqrt5)(M-1).                                  (P3)

This width condition is necessary, not sufficient. The endpoint amplitude
decreases with M, so (P3) alone is not an approximation-cost bound. Several
nonstationary resources, an initially correlated donor, postselection,
external phase control or a changed interaction-energy boundary are
different contracts and are not excluded by this statement.

## 4. What a transfer construction would and would not supply

A second copy of the same battery, already in beta_M, can transfer its
state to an empty battery by a SWAP that commutes with the sum of their
identical Hamiltonians. That is an exact accounted transfer of readiness;
it does not generate the donor's coherence. The present package therefore
keeps beta_M as an explicit initial condition and does not claim a closed
physical preparation cycle or a stationary origin of that state.
