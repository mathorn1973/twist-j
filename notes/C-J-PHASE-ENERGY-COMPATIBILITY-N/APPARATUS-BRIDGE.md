# Dirac bridge to the existing funded apparatus: exact scope and obstruction

PUBLIC / NON-CANONICAL / L1 / analytical candidate-T ceiling.
Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
2026-10-18 Europe/Prague. Exposed continuation of #1603 / draft #1605.

The owner authorized a concrete bridge investigation. Its question was
recorded before this commit in [issue comment6243110595](https://github.com/mathorn1973/twist-j/issues/1603#issuecomment-6243110595).
No scientific executable was imported, run or modified. The original eleven
audit files remain frozen. This is not a new formal computational probe.

## 1. Exact source and comparison class

The source is `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/apparatus.py` at
public main `dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`:
58388 bytes, SHA-256
`f0edfd80157c8993322a5338e88120c552908d3830fe5f9ea7536257213c6173`.
Its original scientific pin is `c3a93f4cb53a3e541529a205f114489e71ad039b`;
the source-derived typed-reader successor preserves the dynamical primitives.
This is an explicitly supplied rational apparatus, not a contact derived
from the original native U. The source's existing scientific evidence is
not rerun or enlarged here.

| Source entry | Exact role |
|---|---|
| `native_tick_single`, `native_tick` | Selector-defined native source updates, with increasing original n |
| `F_step`, `F_inverse` | Linear rational wave/tape evolution, with a separate toggling pointer |
| `wave_energy`, `full_classical_energy` | Chosen quadratic field and tape account |
| `funded_contact_A_substate`, `funded_contact_B_substate` | Proposed field shift; compute its actual cost; accept iff the new bank lies in [0,B] |
| `apparatus_step`, `coupled_step` | Supplied-label or native-source eight-phase schedule; these have different inverse scopes |

For source label r and retained direction sigma, the contact uses

    a(r)=S eta(r),      v_candidate=v+sigma a(r),
    Delta=E_wave(u,v_candidate)-E_wave(u,v),
    accepted iff 0<=b-Delta<=B.

Acceptance sends `(v,W,b,sigma)` to
`(v_candidate,W+Delta,b-Delta,-sigma)`; rejection fixes that contact
substate. All these quantities are rational. W is a work record, not an
additional independent energy reservoir to add again to field plus bank.
The source's E_wave is not the Dirac observable H of CONTACT-KINEMATICS.md.

Here the first bridge question is deliberately narrower than #1596:
can a fixed linear encoding or quotient retain the normalized massive
Dirac rest dynamics inside the existing free wave/tape map, with any
positive integer blocking of the two clocks? Complex scalar extension
and a common scalar phase are considered explicitly. A pointwise fit of
two endpoints, a nonlinear decoder, and a counter-dependent encoding are
different questions. The full guarded nonlinear apparatus is not presumed
to equal its free wave block.

## 2. The actual free matrix is invertible over Z[1/6]

Write R=Z[1/6]. Let P inject the four port coordinates, P^t P=I,
J0=I-PP^t, K=I-(1/2)PP^t. Denote the source's `apply_H` matrix by H_w
to distinguish it from Dirac H. Its diagonal is 10/9 and its OFF-diagonal
coefficients are positive stencil weights divided by324. The negative
off-diagonal signs belong instead to L_D=2I-H_w. Thus H_w has entries in R.

On z=(u,v,A0,A1,B0,B1), of dimension 2*705+16=1426, the literal code gives

    u'=v,
    v'=-J0 u+K H_w v+2P A0,
    A0'=A1,          A1'=B1,
    B0'=(1/2)P^t u-(1/4)P^t H_w v,
    B1'=B0.

For B0', substitute v' into A0-(1/2)P^t(v'-u) and use
P^t J0=0, P^t K=(1/2)P^t. The displayed `F_inverse` recovers

    v=u',
    u=-J0 v'+K H_w u'+2P B0',
    A0=(1/2)P^t v'-(1/4)P^t H_w u',
    A1=A0',          B0=B1',          B1=A1'.

Every coefficient of both matrices lies in R. Therefore the wave/tape
matrix F belongs to GL_1426(R), without constructing a dense matrix or
performing any eigenvalue computation. The pointer k in C2 toggles
independently; its finite permutation lift introduces no new denominator.
The fifths in `apply_S` are contact-source coefficients, absent from F.

## 3. No fixed linear rest-mode bridge, even after blocking

Call a nonzero algebraic number an R-integral unit when it and its inverse
are integral over R. Every eigenvalue of a matrix in GL_d(R) has this
property: apply the monic characteristic polynomials of the matrix and
its inverse. All eigenvalues of F^a, for integer a, therefore have it.

Two elementary facts used below are that integral elements form a ring
and integrality is transitive. In particular, if t^b and t^(-b) are
integral for b>=1, then t and t^-1 are integral, using the monic equations
X^b-t^b and X^b-t^(-b). These standard facts are also stated in
[Stacks, section10.36, lemmas6 and7](https://stacks.math.columbia.edu/tag/00GH).
Finally, a rational number integral over R must lie in R. One elementary
proof clears denominators in a monic relation: any prime outside {2,3}
in the reduced denominator would divide the leading numerator after
reduction modulo that prime, a contradiction.

At rest the eigenvalues of the two target coins are reciprocal pairs

    m=2:    lambda_+=(1+2i)/sqrt5, lambda_-=lambda_+^-1,
    m=1/2:  lambda_+=(2+i)/sqrt5,  lambda_-=lambda_+^-1.

If either lambda were an R-integral unit, then

    (lambda+lambda^-1)^2 = 4/5   or   16/5

would be a rational number integral over R, but neither lies in R.
Thus neither rest eigenvalue is an R-integral unit. The same argument
and the monic-root observation exclude every nonzero integer power.

Consequently, for any positive a,b, a linear map T satisfying

    F^a T = T U_m(0)^b

must annihilate BOTH rest eigenspaces, hence T=0 on the rest spinor.
The conclusion holds even for arbitrary complex coefficients of T:
changing an encoding's coefficient field does not change the two spectra.
In the reverse direction a linear quotient satisfying

    Q F^a = U_m(0)^b Q

is likewise zero, since matrices with disjoint spectra have no nonzero
intertwiner (or apply the same eigenvalue argument on invariant quotients).
An encoding of the full spatial walk retaining its rest mode therefore
cannot use this free source matrix. Adding finite spectator permutations,
finite direct sums or tensor products of R-automorphisms does not fix it.

This also rules out a common scalar-phase repair of the FULL rest coin.
If a nonzero scalar gamma allowed both gamma lambda_+^b and
gamma lambda_-^b to occur as eigenvalues of F^a, their ratio
lambda_+^(2b) would be an R-integral unit, again impossible. Equivalently
the relative phases rho=lambda_+^2 have

    rho+rho^-1 = -6/5  (m=2),       +6/5  (m=1/2).

The inverse condition on F is essential here: the unnormalized Gaussian
integer coin itself has such a ratio, but its inverse introduces fifths.
The projective conclusion requires retaining two relative-phase modes;
it says nothing about one eigenline viewed modulo arbitrary phase.

## 4. What this does and does not say about a contact

For a fixed source label, direction and accepted/refused branch, a contact
has v'=v+sigma a. Its work difference is affine in the wave coordinates:

    Delta=(1/2)||a||^2+sigma a^t(v-(1/2)H_w u).

After adjoining a constant coordinate, its wave/bank/record matrix is
block triangular. A finite FIXED, repeated itinerary of these branches
and free steps has the form

    z'=F^q z+t,
    W'=W+ell z+c,
    b'=b-ell z-c,
    1'=1.

Its eigenvalues are those of F^q together with1; the entries of ell,t,c
may contain fifths but do not change this spectrum. Its inverse has the
reciprocal spectrum. Thus the preceding eigenvalue and ratio tests also
exclude a faithful linear rest-mode bridge through such a fixed affine
itinerary, on a domain where that itinerary actually applies. This is
not a global linearization of state-dependent guards, native labels,
unbounded counter histories or arbitrary switching.

Most importantly, the two positive-band TWO-PARTICLE states used in the
contact witness both have total phase pi and hence free eigenvalue -1:

    (0,pi) and (pi/2,pi/2).

The scalar value -1 is an R-integral unit. The obstruction above does NOT
exclude encoding this isolated degenerate two-state sector. Such an
encoding alone would not reconstruct the two individual Dirac walks,
their position observables, the spin-dependent contact amplitude or their
complete energy account. The question of this weaker collective encoding
remains open rather than being silently absorbed into the no-go.

The original native counter also prevents a universal finite-cycle
argument: native_tick sends n to n+1, so f(n,x)=lambda^n is an eigen-reading
for that native source map for every chosen lambda. In coupled_step, n is
nondecreasing and increases five times per complete eight-phase cycle.
The displayed reading does not select lambda or supply a physical
oscillator. Neither a bounded rational bank
nor a bounded interval in Z[phi] alone gives a finite complete state set.

## 5. Constructive control: a rational Dirac carrier does exist

Rationality itself is NOT the obstruction. On a finite ring let S_lat be
the conditional nearest-neighbor shift, with Gaussian integer entries,
and put

    A_2=S_lat(I+2iX),      A_half=S_lat(2I+iX).

Both satisfy A* A=5I, and the corresponding normalized Dirac operator is
U=A/sqrt5. On K=Q(i,sqrt5), write uniquely psi=x+sqrt5 y with
x,y in Q(i)^(2L). Multiplication by U is exactly

    x'=A y,               y'=A x/5,
    B_A = [[0,A],[A/5,0]].

Its inverse is [[0,A*],[A*/5,0]]. Both matrices have coefficients in
Z[1/5,i], and realifying Gaussian rational coordinates gives an ordinary
rational matrix. For L=4 the dimensions are16 over Q(i), or32 over Q.
The fixed reading pi(x,y)=x+sqrt5 y satisfies pi B_A=U pi exactly on
the stated rational carrier. This is restriction of scalars, not an
embedding into the existing F.

The positive rational quadratic form

    Q_rat(x,y)=||x||^2+5||y||^2

is preserved, since ||Ay||^2=5||y||^2 and
5||Ax/5||^2=||x||^2. It is the average of the squared norms of
the two embeddings x+sqrt5 y and x-sqrt5 y. It is generally NOT the
squared norm of the first embedding alone, which has a cross term.
It is also not an independently selected physical sine energy.

This supplies a fully explicit free comparison carrier and an exact
positive invariant, while adding reversible division by5. The code F
does not have that free dynamics. Iterated denominators may grow; no
finite-state or integer-lattice realization, original-native compiler,
funded contact, Born measure or physical energy selection follows.

## 6. The two contact denominations and their accounting boundary

For r=sqrt(1+m^2), delta=r-m=1/(r+m). At m=csch(a), a>0,
delta=tanh(a/2). Hence the owner's two exact pair increments are

    d_2=2sqrt5-4=2phi^-3=-6+4phi,
    d_half=sqrt5-1=2phi^-1=-2+2phi,
    d_half/d_2=phi^2, an irrational number.

A rational bank with the same linear reading alpha b+beta in both
species cannot be the sole compensator for both increments: the ratio
of its two nonzero rational changes would have to equal phi^2. This is
conditional on a COMMON calibration and no other compensating reference,
controller or field. Species-dependent calibrations and nonlinear readings
are outside that statement. With alpha=1 either individual increment
already lies outside the bank's value field.

As a purely additive account, the two increments generate exactly
2Z[phi]: the vectors (-3,2),(-1,1), after dividing the increments by2,
have determinant -1 and therefore form a Z-basis of Z[phi]. Two integer
account coordinates can consequently represent both denominations
exactly. This arithmetic fact neither derives their update nor turns
them into an admitted physical bank. In particular, a nondegenerate bounded
real interval contains infinitely many Z[phi] values and signed coefficient
pairs; finite resource claims need an additional complete bound.

The quadratic identity C_sc^2+H^2=(1+m^2)I is true, but its total is a
scalar operator and cannot discriminate allowed contacts. It does not
establish that the linear energy increment is funded by an independent
reservoir. C_sc=cos(k)I is a scalar matrix term, not a global phase.
In the existing convention

    D=cos(k)I+i[sin(k)Z+m cos(k)X-m sin(k)Y].

The alternative cos(k)I-i[sin(k)Z+mX] is Q(k)* D Q(k), with
Q(k)=diag(exp(ik),1)Y. The same change gives
Q* x Q=x-(I-Z)/2; position and the contact must also be transformed.
One cannot use that simplified matrix and silently retain the old onsite
contact's spin overlaps.

## 7. Result supplied to the common-carrier question

The present result has three distinct parts:

1. **Excluded class:** fixed linear faithful massive-rest encodings into
   the stated free source F, its integer blocks and the fixed affine
   itineraries specified above, including a common scalar-phase repair
   when relative phases are retained.
2. **Constructed control:** an explicit rational free Dirac carrier with
   reversible fifths and a positive rational invariant. This shows exactly
   which source-dynamics restriction the negative result uses.
3. **Still missing:** a common source-independent preparation, allowed
   native transition, position/contact translation and complete bank,
   reference and controller account for the two-particle witness. Even
   its isolated degenerate-sector encoding is not supplied here.

The next input for #1596 is therefore a named candidate beyond the excluded
linear/free class, or the separately scoped weaker collective encoding.
Changing the bank type alone while leaving F unchanged cannot repair a
faithful free linear bridge. Neither insertion of a desired cost nor an
arbitrary counter phase supplies the missing native permission.

The unchanged related source pins are #1596/#1589 at
`a6d2b0d30b9d6703fffb15b187c58fa6ad71e229`,
`notes/C-J-AREA-COMMON-CARRIER-JUNCTION-N/CONTRACT.md`;
#1498 at `7b4d55502be44b2f2aed4005c909d7dcb50dbc55`,
`notes/C-HB-NATIVE-ADMISSION-BOUNDARY-N/RESULT.md`;
and #1585 at `bb04eb3c582e2ec06f90b1a5768ecdfb1ac2044e`,
`probes/P-FUNDED-AREA-PHASE-RECORD-1/verify.py`.
Their owners and scopes are not taken over or promoted. The finite
m/atan(m) physical hypothesis is neither established nor falsified by
this comparison. No Canon, source apparatus or contact primitive changes.
