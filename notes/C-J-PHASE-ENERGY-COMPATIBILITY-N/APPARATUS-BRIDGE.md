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
is not silently absorbed into the no-go. Sections9–11 below now construct
its free algebraic carrier in F and test the separate contact obligation.

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
   reference and controller account for the two-particle witness. Its
   isolated FREE algebraic sector is now supplied in section9; the required
   contact/position/energy encoding remains missing.

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

## 8. Pair-phase cancellation and the corrected rest polynomials

This exposed continuation answers the owner's next proposal, with scope
recorded in [comment6243337863](https://github.com/mathorn1973/twist-j/issues/1603#issuecomment-6243337863).
The primitive integer minimal polynomials have the following signs:

    m=2:    5X^4+6X^2+5,
    m=1/2:  5X^4-6X^2+5.

Indeed lambda^2+lambda^-2 equals -6/5 or +6/5, respectively. Each
lambda generates Q(i,sqrt5): its square recovers i and then lambda
recovers sqrt5. Thus its degree is four, proving irreducibility. The
monic minimal polynomials have nonintegral coefficients +/-6/5. Merely
exhibiting some nonmonic polynomial would not prove nonintegrality.
These numbers are not algebraic integers and cannot be roots of unity.
Section3 proves the stronger obstruction appropriate to R=Z[1/6].

For either mass, the positive-band pair states a=(0,pi), b=(pi/2,pi/2)
have normalized free eigenvalue -1. The middle single-particle eigenvalue
-i is a Gaussian integer, not a rational number. It can of course be an
eigenvalue of a rational matrix. With the literal D_m=r U_m, their raw
pair eigenvalue is -r^2: -5 for m=2, but -5/4 for m=1/2. Rescaling the
half-mass coin to A_half=2D_half gives -5 for its raw pair instead.

Raw multiplication by -5 is NOT an alternative realization inside F:
the inverse eigenvalue -1/5 is not R-integral, so -5 cannot occur in
GL_d(R). The same argument excludes -5/4. Raw norm growth changes
amplitudes, not the dimension of a state space. The normalized value
-1 does pass this arithmetic test; its actual occurrence is proved next.

On a Hilbert sector with U0=-I, nonzero vectors have period two while
rays and density operators are stationary. A common sign alone supplies
no observable period-two clock. For two positive bands, the outgoing
(pi/2,pi/2) velocities are BOTH +1/r, not opposite: these modes co-propagate.

## 9. The existing F has an explicit four-dimensional -1 eigenspace

Set B=2I+H_w. The stencil shells with squared lengths 2,4,8,10,16 have
respectively 12,6,12,24,6 displacement vectors. Their weights are
6,1,15,1,1, so the full off-diagonal row sum is

    (12*6+6+12*15+24+6)/324=8/9.

Restricting to the finite domain only removes neighbors. Symmetry and
the diagonal 10/9 therefore give H_w >= (2/9)I and B >= (20/9)I.
In particular B is invertible over Q. No dense inverse or scientific
executable is needed for this argument.

For every q in Q^4 define, in the order z=(u,v,A0,A1,B0,B1),

    u=B^-1 Pq,
    Z(q)=(u,-u,q/4,-q/4,-q/4,q/4).

Substitution in section2 gives F Z(q)=-Z(q). Conversely Fz=-z forces
v=-u, A1=-A0, B1=A0, B0=-A0 and

    B u=4P A0.

Thus q=4A0 gives every eigenvector, and

    E_minus=ker(F+I)={Z(q):q in Q^4},    dim_Q E_minus=4.

The coordinate is read back directly as q=4A0.

This improves the previous arithmetic allowance to an actual free
construction in the UNCHANGED apparatus. Two independent rational vectors
Z(e1),Z(e2), after complex scalar extension, intertwine an abstract C^2
operator -I with F. Alternatively all four real rational coordinates
encode two Gaussian-rational amplitudes by
(Re c1,Im c1,Re c2,Im c2). The literal rational carrier does not thereby
become all of C^2 or acquire a Born rule, position or Dirac energy reading.
The source pointer is separate: F_step sends (Z(q),k) to (Z(-q),k+1 mod2).
This free wave/tape/pointer substate returns after two steps; the complete
native source, counter, bank and controller are not included in that claim.

The source's quadratic account on this space is explicitly

    E_full(Z(q))=(1/2) q^t [I_4+P^t B^-1 P] q.

To check it, E_wave(u,-u)=(1/2)u^t B u and twice the sum of the four
tape squared norms is ||q||^2/2. This positive rational form is the
existing apparatus account, not an identification with the two-particle
sine-energy observable.

## 10. One funded impulse cannot act internally on that free sector

An accepted source contact changes the wave/tape coordinates by

    d_sigma(a)=(0,sigma a,0,0,0,0),       a=S eta(r).

Every vector in E_minus satisfies v=-u. Hence d_sigma(a) belongs to
E_minus only when a=0. A nonzero accepted contact takes EVERY point of
E_minus outside E_minus, and likewise takes every point of any fixed
affine coset z0+E_minus outside that same coset. A rejected contact has
no wave effect. An accepted zero impulse may still flip a control sign;
it supplies no nontrivial wave transition within E_minus.

Since F^j(E_minus)=E_minus for every integer j, arbitrary free steps
before and after ONE nonzero impulse cannot restore membership either.
This does not exclude return after multiple impulses, a changed encoding,
additional retained modes or a different declared contact.

The actual cost on Z(q) is especially simple:

    v-(1/2)H_w u=-(1/2)Pq,
    Delta_sigma=(1/2)||a||^2-(sigma/2)a^t Pq,
    b'=b-Delta_sigma,       W'=W+Delta_sigma,

when the original bank guard accepts. The norm uses the WHOLE field a,
including its fifth-site component. This exact rational debit is not
automatically either irrational Dirac denomination from section6.

For a fixed word with N free steps and accepted impulses d_j, let r_j
count free steps after impulse j. The wave endpoint from Z(q) is

    z_out=(-1)^N Z(q)+sum_j F^(r_j) d_j.

Return to E_minus requires the sum to lie in E_minus, in addition to
every actual source-label and bank-acceptance condition along the word.
This gives an exact test for a declared word. It supplies no finite bound
on all words, preparations or complete native-counter histories.
Sections12–14 below now settle NONTRIVIAL return for the actual schedule
without imposing a word-length bound.

## 11. The onsite Hilbert contact also leaves the full free -1 sector

Use the unchanged comparison of CONTACT-KINEMATICS.md section4: two
distinguishable particles, m>0, 4 dividing L, V the onsite projector and
U_g=exp(-igV)U0. Let the band signs be explicit:

    a=|0,+;pi,+>,
    b=|pi/2,+;pi/2,+>,
    c=|pi/2,+;pi/2,->.

Then U0 a=-a, U0 b=-b, but U0 c=+c. All three have total momentum pi.
At 0 and pi the positive-band spinors are |-x> and |+x>. BOTH band
spinors at pi/2 have zero Bloch X component, hence their overlaps with
either of these rest/edge spinors have magnitude 1/sqrt2. Consequently

    |<b|V|a>|=|<c|V|a>|=1/(2L),
    |<c|U_g|a>|^2=sin^2(g/2)/L^2.

For every g outside 2pi Z, even the COMPLETE U0 eigenvalue -1 sector is
therefore not invariant under this contact. The resonant channel a->b
still exists. The different a->c channel has phase difference pi: its
first-order N-step sum is sum_(t=0)^(N-1)(-1)^t, with no linear-in-N
growth. A nonzero exact one-step amplitude is not a long-time resonant
scattering claim.

For the smaller K=span{a,b}, the diagonal V matrix elements are 1/L and
the off-diagonal magnitude is 1/(2L). Since V^2=V,

    ||(I-P_K)V a||^2=1/L-5/(4L^2),
    ||(I-P_K)U_g a||^2=(4L-5)sin^2(g/2)/L^2.

The compression P_K V P_K has eigenvalues 1/(2L),3/(2L), not0 or1.
Exponentiating that compression defines a DIFFERENT contact, not the
restriction of the existing projector kick to an invariant subspace.

Thus the free collective bridge is now constructed, but two distinct
contact tests fail the proposed closed-sector shortcut: the actual funded
impulse exits its free F eigenspace, and the declared onsite kick exits
even the whole Hilbert U0=-1 sector. Neither result is a universal no-go
for native contacts. A finite candidate test must first declare the full
retained carrier, word, encoding, observables and bank/controller account.

## 12. A four-component invariant of the complete actual schedule

The owner authorized continuation of the multi-contact question. Its
exposed analytical scope is recorded in
[comment6247442868](https://github.com/mathorn1973/twist-j/issues/1603#issuecomment-6247442868).
The source pin and hash in section1 remain unchanged. This is a proof
from the literal update, not a new scientific execution or formal probe.

Define two rational four-component readings on ALL wave/tape states:

    R0(z)=P^t u+2(A0+B1),
    R1(z)=P^t v+2(A1+B0).

The free step exchanges them exactly:

    R0(Fz)=R1(z),             R1(Fz)=R0(z).

The first identity follows immediately from u'=v, A0'=A1, B1'=B0.
For the second, use v'=w, A1'=B1 and the source's port equation
B0'=A0-P^t(w-u)/2:

    R1(Fz)=P^t w+2[B1+A0-P^t(w-u)/2]=R0(z).

Every accepted contact changes only v among these coordinates, hence
fixes R0 and changes R1 by P^t h, where h=sigma S eta(r) is the ACTUAL
signed impulse. Set h=0 for a refused contact. Native source updates,
buffer capture and control-sign changes hold the amplitude tuple fixed.

The literal eight-phase schedule uses the following rows (c is the
controller value BEFORE the row):

| c | Amplitude operation | Invariant reading before the row |
|---|---|---|
| 0 | Identity; native source tick | R0 |
| 1 | Capture B label, then funded contact A | R0 |
| 2 | F; native source tick | R0 |
| 3 | F; native source tick | R1 |
| 4 | Funded contact B using the stored label | R0 |
| 5 | F; native source tick | R0 |
| 6 | F; native source tick | R1 |
| 7 | Identity; controller rollover | R0 |

Thus, with e(c)=1 for c in {3,6} and e(c)=0 otherwise,

    I(z,c)=R_e(c)(z)

is invariant under EVERY `coupled_step` row, including the controller
advance. At a free row both the selected index and the two readings
exchange; at a contact both endpoints select R0. The other rows change
neither. This proof covers arbitrary occupied valid states, actual native
labels, buffer history, retained signs, accepted/refused guards and bank
capacity. In particular it does not substitute freely chosen labels for
the actual source: buffer capture precedes contact A and remains recorded
even when its proposal is refused; each sign flips only on acceptance.
The same identity holds for the
supplied-label `apparatus_step` with its literal schedule.

## 13. All finite scheduled returns carry no new sector state or net debit

Put M=I_4+P^t(2I+H_w)^-1P. Section9 gives M>0 over Q and

    R0(Z(q))=Mq,             R1(Z(q))=-Mq.

Suppose ANY finite scheduled history starts at Z(q_i), controller c_i,
and ends at Z(q_f), controller c_f. Conservation of I gives

    (-1)^e(c_f) Mq_f=(-1)^e(c_i) Mq_i,
    q_f=(-1)^(e(c_i)+e(c_f)) q_i=(-1)^N_F q_i,

where N_F is the number of free F rows in that history. The second
equality uses the fact that e changes exactly at free rows. This is
precisely the ordinary free sign. At matching controller phases,
including any number of complete cycles, q_f=q_i. No cutoff on the
number of contacts, source counter or rational bank states is needed.
At a matching controller phase the same injectivity argument also
excludes movement within ANY fixed affine coset z0+E_minus.

This closes nontrivial scheduled transfer inside this fixed collective
sector, even when the history leaves the sector between endpoints.
It does NOT classify or prove existence of excursions returning to the
same point. It also does not turn a common Hilbert sign into an observable
change, or exclude a larger retained carrier or a different contact rule.

For ONE complete c=0 to c=0 cycle there is a stronger statement. Write
d(h)=(0,h,0,0,0,0) and absorb acceptance/sign into h_A,h_B. The exact
amplitude endpoint is

    z_f=F^4 z_i+F^4 d(h_A)+F^2 d(h_B).

Starting in E_minus, return requires F^2 d(h_A)+d(h_B) in E_minus.
Its A0 and A1 slots are zero, so its sector coordinate q=4A0 is zero
and the entire vector must vanish. Its u slot is K H_w h_A. Both
K and H_w are invertible (section9 gives H_w >= (2/9)I), so

    return in one complete cycle iff h_A=h_B=0.

This concerns actual wave impulses: a rejected nonzero proposal counts
as zero; an accepted zero impulse can still change a control sign.
A zero work increment is not in general a zero impulse.

The return also fixes the net existing bank/work account. For each actual
accepted h, evaluated on the THEN-current wave,

    delta=h^t(v-H_w u/2)+(1/2)||h||^2,
    b'=b-delta,             W'=W+delta.

Free F preserves E_full, as shown directly by the port/tape identity in
the source's `SOURCE_PROOF.md` section2; all non-contact rows leave b,W
unchanged. Hence the sum of actual deltas is the endpoint difference
of E_full. Since E_full(Z(q))=q^t Mq/2 is even in q, every scheduled
return to E_minus satisfies

    sum delta=0,            b_f=b_i,             W_f=W_i.

Transient withdrawals and repayments are allowed by this statement.
There is no nonzero NET debit to identify with a Dirac pair denomination
on such a return. After r complete cycles the pointer k returns but the
original native counter increases by5r; source heads, signs and buffer
may change. No complete-state recurrence or memory renewal follows.

## 14. Why allowing both timing parities changes the linear comparison

The following is an explicitly ENLARGED rational control class, not a
native realization: allow arbitrary rational linear combinations of the
source directions and place them at either parity of the free step.
It separates the schedule obstruction from a universal impossibility.

Let U_src=span_Q{e1,e2}, the span of the actual eta labels, and define

    L_minus=(R0-R1)/2,       L_plus=(R0+R1)/2,
    Pi_minus=Z M^-1 L_minus.

Here Z denotes the linear map q->Z(q). Direct identities give
L_minus F=-L_minus, L_plus F=L_plus, L_minus Z=M and
Pi_minus^2=Pi_minus with range E_minus. This projector is a polynomial
in F over Q. Indeed L_minus(F+I)=0 and L_minus is injective on
ker(F+I), so ker(F+I) intersects im(F+I) only in zero. Their dimensions
sum to1426, excluding a Jordan chain at -1. The minimal polynomial is
(t+1)r(t) with r(-1)!=0, and Pi_minus=r(F)/r(-1).

Consider the rational span of freely timed impulses,

    W_all=span_Q{F^j d(S eta): j>=0, eta in U_src}.

It is F-invariant, so its polynomial projection is still inside it.
Using Pi_minus F^j=(-1)^j Pi_minus and
L_minus d(a)=-(1/2)P^t a gives exactly

    W_all intersect E_minus = Z(M^-1 P^t S U_src),
    dim_Q(W_all intersect E_minus)=2.

The harmless factor -1/2 does not change a rational span. The dimension
is two because P^t S=I_4-11^t/5 is invertible (eigenvalues1,1,1,1/5).
This is an exact finite-polynomial existence statement in the enlarged
linear class. It does not compile its coefficients into the finite label
alphabet, sign updates, actual schedule, bank guards or a native program.

In contrast, with only one common parity of impulse ages,

    W_even=span_Q{F^(2j)d(S eta): j>=0, eta in U_src}

is annihilated by R0. Since R0 is injective on E_minus,
W_even intersects E_minus only in zero. Its odd translate has the same
zero intersection. This is the linear counterpart of the actual
row-wise invariant, not an assumption of a finite state space.

A further necessary condition holds for ANY timed return to E_minus:
L_plus vanishes at both endpoints and is preserved by F. Therefore

    sum_(accepted j) sigma_j eta(r_j)=0,

using the invertibility of P^t S. It is not sufficient: all other wave
and tape components must cancel as well. Changing timing alone has not
been proved to supply an actual admitted contact sequence.

The remaining construction must therefore retain more than E_minus, or
change a specified operation/schedule that protects I, and supply the
same source-independent position/energy/account bridge. Repeating the
unchanged eight-phase schedule, enlarging its bank or accumulating more
contacts cannot produce a different endpoint within this fixed sector.
