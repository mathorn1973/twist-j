# Sharp finite-horizon contact memory

PUBLIC-content / NON-CANONICAL / conditional candidate-T / L1.
A. M. Thorn. Original work Apache-2.0. Owner issue #1525.
No native, physical, bit-capacity or all-time closure claim.

## 1. Definitions and access contract

The finite rational wave/tape F is the supplied map of the independently
audited two-use apparatus, not the native U. Use the exact primary domain
D=Y+B0+B0 with 705 sites, four ports y0,...,y3 and y4=(2,0,0).
H=2I-L_D is symmetric, with diagonal 10/9 and stencil coefficients
weight(|d|^2)/324 for shells 2,4,8,10,16 and weights 6,1,15,1,1.
P inserts the four port entries, Qp=PP^T, J0=I-Qp, K=I-Qp/2.
Let e4 denote delta_y4, cY=sum_(j=0)^4 delta_yj and
A=[s0 s1], s_i=delta_yi-cY/5. Then

    G=A^T A=(1/5)[[4,-1],[-1,4]], det G=3/5,
    A^T J0=-(1/5)ones2 e4^T,
    M=A^T P, h^T=e4^T H P=(1,6,6,0)/324.

All initial waves (u,v) in Q^D x Q^D and all four rational tape slots
(a0,a1,b0,b1) are allowed. The tape is known separately to the reading;
its dimensions are not counted as part of the wave-summary rank. All
source labels, signs, store bound B>=0, b in [0,B] and work ledger Wlog
are also separately available. Summary selection cannot depend on labels,
wave, tapes, chosen query or intended output. Equality is signed rational
coordinate equality. Arbitrary nonlinear decoders of the summary are allowed,
but the summary itself must be one fixed rational LINEAR wave map L.

F gives

    u'=v, v'=w=K(Hv-J0u+4Pa0),
    (a0',a1',b0',b1')=(a1,b1,a0-P^T(w-u)/2,b0).

Its independent whole-state inverse and energy law are inherited from V2.
The calculations below use this literal F, including occupied tape.
Define wave-only linear coordinates

    rho=A^T(v-Hu/2) in Q^2,
    gamma=(e4^T u-e4^T H v/2)/5,
    delta=(e4^T v-e4^T H K H v/2+e4^T H J0 u/2)/5.

Here delta is a scalar memory coordinate; Delta below is contact work.

## 2. Three exact prediction formulas

Using K-I/2=J0/2, KJ0=J0 and KP=P/2,

    w-Hv/2=J0(Hv/2-u)+2Pa0.

Multiplication by A^T gives

    rho(FX)=gamma(X)*ones2+2M a0.                 (1)

The definition of gamma on the new pair (v,w) gives

    gamma(FX)=(e4^T v-e4^T H w/2)/5
             =delta(X)-h^T a0/5.                (2)

The incoming tape at the second step is exactly the original a1.
Applying (1) again yields

    rho(F^2X)=(delta(X)-h^T a0/5)*ones2+2M a1.  (3)

These are coefficient identities on every one of the 1426 rational
wave/tape coordinates, not long-time numerical extrapolations. The old
outgoing tapes b0,b1 do not enter these two predictions; they stay in
the complete state and are not discarded. They can matter at later steps.

## 3. A counterexample to adding only gamma

Set z_far=(10,0,0)=y4+(4,0,0)+(4,0,0), which belongs to D. It is outside
Y and outside one stencil step from Y. Let X_plus and X_minus have
u=0, v=+/-delta_z_far, all tapes zero and all other variables equal.
Initially

    rho(X_plus)=rho(X_minus)=(0,0),
    gamma(X_plus)=gamma(X_minus)=0,
    E_full(X_plus)=E_full(X_minus)=1/2.

The only two-stencil path from y4 to z_far uses (4,0,0) twice. Its
intermediate point (6,0,0) is not a port, so K is identity there. Hence

    (H K H)_(y4,z_far)=1/324^2,
    delta(X_plus)=-1/(10*324^2),
    delta(X_minus)=+1/(10*324^2).

No port is within two stencil steps of z_far: its x-distance is at least
9 whereas two offsets change x by at most 8. The first two outgoing cuts
are zero in both trajectories. All four tapes therefore agree and stay
zero through two F steps. The full energies stay 1/2 by the preserved
energy law (also directly audited).

Equation (3) gives different rho(F^2X), with both entries respectively
-1/1049760 and +1/1049760. Thus no deterministic updater of the old
(rho,gamma), even supplied with energy, tapes, counter and the same
native/sign/store spectators, can predict both trajectories. The witnesses
are arbitrary occupied-wave states; no common-ready-image membership is
asserted. This does not contradict the existing prepared-family reduction.

A concrete observable contact witness follows: take the first source zero,
then perform F twice and use second source A(1,0)^T with sigma_B=+1,
B=1,b=1/2. Both second contacts accept, but their work values are
2/5-1/1049760 and 2/5+1/1049760. The energy difference is drawn from
the initial occupied waves; no new energy or native interaction is claimed.

## 4. Complete linear-summary criteria and sharp ranks

### Horizon {0,2}: rank three

For every known initial tape, recovering rho(X) and rho(F^2X) from L(u,v)
is possible iff

    ker L subset ker(rho,delta).                  (4)

Necessity: choose zero tape. Equal L values must give equal current rho
and, by (3), equal delta. Apply this to a vector in ker L and zero.
Sufficiency: under (4), define C(Lw)=(rho(w),delta(w)); it is a well-defined
rational linear map on Im L. Formula (3) recovers the second output.
No linearity of the admitted output decoder was used for necessity.

The map xi=(rho,delta) has rank exactly three. Its values on the three
wave columns (u=0,v=s0), (0,s1), (0,delta_z_far) give a block-triangular
minor with determinant

    det G * [-1/(10*324^2)] = -1/1749600 != 0.

It has only three rows, so this lower bound is also the upper bound.
Every L in (4) has rank at least three, attained by xi.

### Horizon {0,1,2}: rank four

Recovering all three rho outputs with the same allowed access is equivalent
to ker L subset ker(rho,gamma,delta), by zero-tape specialization of (1)-(3).
Choose z_near=(6,0,0). Its point-wave column has rho=0 and

    gamma(0,delta_z_near)=-1/(10*324),
    gamma(0,delta_z_far)=0.

Together with s0,s1 and z_far this gives a four-column triangular minor
with determinant

    (3/5)*[-1/(10*324)]*[-1/(10*324^2)] != 0.

Thus rank four is necessary and sufficient when the intermediate reading
is also required. A data item sufficient for one prescribed delay need
not be the same as one sufficient for every intermediate boundary.

Neither result covers nonlinear summary maps, extra wave-dependent energy
as a free input to the rank-minimum problem, label-dependent summaries,
restricted prepared ensembles, finite bits or physical sensor counts.
The energy-augmented collision in section 3 is a distinct scoped negative.

## 5. A three-coordinate finite two-contact controller

Use xi=(rho,delta). Let eta=eta2(r) in Q^2 for r in F5^2, and source
f=A eta. The supplied contact proposes

    Delta=eta^T G eta/2+sigma eta^T rho,
    alpha=1 iff 0<=b-Delta<=B.

It changes v by alpha*sigma*A eta. Consequently xi updates EXACTLY as

    rho' =rho+alpha*sigma*G eta,
    delta'=delta+alpha*sigma*kappa^T eta,
    kappa^T=e4^T(A-H K H A/2)/5.                    (5)

The independently audited stencil work row supplies the exposed target

    kappa^T=-(145483,173653)/10497600.

The new finite coefficient audit also checks this row from the literal
stencil. Formula (5), not the numerical target alone, proves the update.
On acceptance update Wlog,b,sigma by Delta,-Delta and sign reversal;
on refusal all are unchanged. This retains zero-cost acceptance, negative
work and the upper as well as lower stock bound.

After contact A, apply (3) to its updated delta with the actual original
incoming slots a0,a1. It gives rho immediately before contact B. Its exact
work, acceptance and store/sign/ledger changes then follow from the same
original guard. No intervening fresh wave read is required for this fixed
two-F separation once xi was acquired at the first contact.

This is an exact prediction of the two works, both branches, final store,
ledger and signs, and the contact-B rho. It is NOT recovery of the complete
wave/tapes, an inverse of their dynamics or a rule updating delta after two
F steps. It therefore does not yet permit indefinite repetition without
another acquisition. The initial xi acquisition is also an explicit premise,
not a native sensor constructed by these equations.

The rank-three lower bound also applies when the required outputs are the
exact pre-guard work values for every two-contact label/sign choice and
known tape. Current source choices eta=(1,0),(0,1) determine both rho entries
from their first costs. With the first source zero and zero tape, the second
eta=(1,0) cost equals 2/5+delta and determines delta. All three labels exist
in F5^2 under eta2. Thus any such fixed linear summary must carry xi.
Minimality is not asserted for a narrower Boolean-guard-only problem.

## 6. Evidential status and next boundary

All targets above were derived analytically and exposed in #1525 before
new scientific execution. verify.py is same-author, source-exposed exact
audit code, not a blind independent implementation. It checks complete
linear coefficients, both nonzero minors, the counterexample with energy
and tapes, contact-update coefficients and fixed finite guarded witnesses.
The universal implications are the proofs above, not sample extrapolation.

This leaves a smaller, precise acquisition task: three rational wave
coordinates for this scheduled two-contact prediction, rather than the
whole wave. It does not supply a native implementation or an all-future
compressed state. Canon v101, QDD apparatus/occurrence and native-contact
obligations remain unchanged. A distinct reviewer and public fold are
required before any authority change.
