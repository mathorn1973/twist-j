# Corrected images and preserved nonlinear readback

PUBLIC / NON-CANONICAL / L1. Proof status: candidate-T.
A. M. Thorn. Apache-2.0. Source-exposed corrective work under #1539.
This is an additive correction to #1537, not a rewrite of its frozen proof.
The original finite audit PASS and its incorrect prose are separate objects.

## 1. Literal native definitions

All coordinates are in F5. For x=(a,b,c,d,q,r), put
z=sum(x), A=a+c, B=b+d, C=a-c-2, D=b-d-1. The affine chart is
Psi(x)=(z,A,B,C,D,q), with inverse

    a=3(A+C+2), b=3(B+D+1),
    c=3(A-C-2), d=3(B-D-1), r=z-A-B-q.

The constant 3 is the inverse of 2. The five original maps are

    g0(x)=(b,a,d,c,q,r),
    g1(x)=(-c,-d,-a,-b,-q,-r),
    g2(x)=(2-c,1-d+r,2-a,1-b-r,1-q,-r),
    g3(x)=(2-a,1-b,3-c,4-d,1-q,1-r),
    g4(x)=(2-a,1-b,3-c,4-d,2-q,1-r).

Their trace actions are z,-z,2-z,2-z,3-z. Each g_j is an involution.
The selected map is T_t(x)=g_(z+2t mod5)(x), and the autonomous map is
U(n,x)=(n+1,T_(theta_n)(x)), theta_n=popcount(n) mod2. These definitions
come from the pinned Canon, not from the claim being corrected.
A named generator g_j and the selected map T_t must not be identified.

## 2. Exact selected-map images (correction E1)

Let X_z be the trace-z sheet. On each X_z and fixed t the selected letter
j=z+2t is constant, so T_t restricted to X_z is one affine bijection onto
its target trace sheet. The complete trace table is

    source z     0  1  2  3  4
    after T0     0  4  0  4  4
    after T1     2  1  1  3  1.

Therefore T0 on F5^6 has 6250 image points: 3125 fibres of size two and
3125 of size three. T1 has 9375 image points: 6250 singleton fibres and
3125 fibres of size three. In particular neither map is globally bijective.
These counts are inherited native-map consequences, audited here only to
prevent the erroneous inference in the independent receiver proof.

For fixed lambda,mu, define the prepared tail

    T_lm={Psi^-1(z,A,0,lambda*A/z,mu*A/z,q):
          z,A in {1,4}, q in F5}.

It has 20 points. For z=1 the selected letters are g1 (t=0) and g3 (t=1);
for z=4 they are g4 (t=0) and g1 (t=1). In every case A'=-A, B'=0,
and the two ratios I_C=z*C/A and I_D=z*D/A are preserved. Thus

    T_t(T_lm)=T_lm intersection X_(4+2t mod5).

The right side has ten points. This is equality, not only inclusion:
for each known input phase s=1 or 4, its ten input states map bijectively
to those ten output states. The inverse on that restriction is the SAME
fixed generator g_(s+2t mod5), since it is involutive. Applying the
state-dependent selector anew at the output is not that inverse in general.
Consequently T_t on the union of input phases is exactly two-to-one.
The 25 disjoint tails give a 500-point forward-invariant union; each fixed
t sends it onto a 250-point output sheet, not onto the full union.

An explicit collision inside T_00 is

    x=(4,3,2,2,0,0), y=(4,3,2,2,2,1), x!=y,
    T0(x)=g1(x)=(3,3,1,2,0,0)=g4(y)=T0(y).

Replacement for #1537 PROOF Theorem 5.1(3): retain forward invariance and
replace its claimed bijection/equality onto the full tail by the exact
image and phase-restricted inverse above. The induction in 5.1(4) needs
only forward invariance and is unaffected by this correction.

## 3. All-time prepared-state retention without a global inverse (E2)

The fixed preparation is

    E(lambda,mu)=(3(lambda+3),3(mu+1),3(-lambda-1),3(-mu-1),0,1).

Its affine chart is (2,1,0,lambda,mu,0). The actual initial bits 0,1,1
select g2,g2,g4. The affine data at the four boundaries are

    n  z  A  B  C        D       q  r
    0  2  1  0  lambda   mu      0  1
    1  0  3  2  lambda   mu+2    1  4
    2  2  1  0  lambda   mu      0  1
    3  1  4  0 -lambda  -mu      2  0.

The full checkpoint returns at n=2 because g2^2=id, while its counter does
not. On S={z in {1,4},A!=0}, every permitted edge preserves both I_C and
I_D: g1 changes (z,A) to (-z,-A) and fixes (C,D); selected g3/g4 fix z
and negate (A,C,D). S has 5000 states. The labels at n=3 are (lambda,mu),
so the same identities prove preservation for every n>=3 by induction.
This is a proof for all future times, not a claim extrapolated from n<=32.

Also Q(x)=(z,q,r) is an autonomous quotient: each literal g_j has output
Q depending on Q alone, and the selector uses only z and the common bit.
All preparations have Q(E)=(2,0,1). Hence their Q histories and their
selected letters coincide at every common time. At each such time, a
single fixed bijection g_j acts on the 25 prepared states. Induction
therefore preserves all 25 distinct states. Since q,r are common, their
four-piston blocks are distinct too. Alternatively the explicit prefix
proves injectivity for n=0,1,2 and (I_C,I_D) recovers the labels for n>=3.

Replacement for #1537 PROOF Theorem 6.1(3): this prepared-family argument
replaces the false assertion that the state-dependent composition is a
bijection of F5^6. No new global inverse of U is asserted. The clock itself
also rules out surjectivity of U on all N0 x F5^6 at n=0.

## 4. Global polynomial degree of the unchanged reader (E3)

Write e_j(z)=1-(z-j)^4 and tau=z*A^3+1-A^4. The exact primary reader is

    T=e0*C+e2*q+(e1+e4)*tau*D+e3*D, R=(z,T).

The global chart Phi and inverse are the same as the primary source.
On z=0 it uses (z,C,A,B,D,q); on z=2, (z,q,A,B,C,D); on z=1,4,
(z,tau*D,A,B,C,q); and on z=3, (z,D,A,B,C,q). The multiplier is nonzero
on z=1,4 including A=0, because tau=1 at A=0 and tau=z/A otherwise.
Its inverse there is z*A+1-A^4. Thus the global chart is bijective.
That coordinate bijection must not be confused with a dynamics bijection.

Canonical polynomial functions use exponents 0..4 in each independent
coordinate, modulo x_i^5-x_i. The representative is unique: induction
on the variables and the degree-at-most-four univariate root bound show
that a reduced polynomial vanishing on all F5^6 has every coefficient zero.
Now

    e1+e4=3*z^4+3*z^2.

Multiplying its -A^4*D contribution leaves 2*z^4*A^4*D, of total degree
nine. No other term contains A^4*D with z^4, so it cannot cancel. All
terms have total degree at most nine before coordinate reduction. Hence
this global T has exact reduced degree nine, not five. Invertible affine
changes of variables preserve the minimal total degree of polynomial
functions: composition and reduction cannot increase degree, and applying
the inverse gives the reverse inequality. Thus the same degree is nine
in the original raw coordinate basis as well.

Replacement for Theorem 7.1(2) and the matching RESULT paragraph: replace
'nonlinear (total degree 5)' by 'this global reader has reduced total
degree 9'. This says nothing about the minimum degree among other readers
on a restricted prepared set, and does not conflict with #1536 or #1538.
The exact existing receiver outputs are unchanged.

## 5. Retained existence statement and limits

The unchanged fixed reader G(z,t) is BLANK for z=2,3 and PRESENT(t)
otherwise. The prefix in section 3 gives BLANK, PRESENT(lambda), BLANK,
PRESENT(mu). For n>=3, T=I_D=mu and z remains 1 or 4. Thus permanent
readback follows. Zero is a present label distinct from BLANK.
Two F5 coordinates are necessary to realize six semantic outputs and the
global chart attains this count. There is no uniqueness theorem over all
readers and no physical admission from polynomiality.

The two messages are present in the initial whole state. The raw (q,r)
port has the same trajectory for every pair. The receiver mixes source
and port coordinates; at n=1 it reads C directly. No transfer into a fixed
raw receiver block, fresh loading, source depletion, energy exchange,
material record, native implementation of this reading, or layer lift is
proved here. The corrected claim is mathematical coordinate-readout
existence, not physical forcing.

## 6. Historical fixture, not a reconstructed historical run (E4)

The source expression

    {(z,q,z-A-q): z,A in {1,4}, q in F5}

has 20 points: equality of triples fixes z,q and then A. Independently
closing (2,0,1) under both quotient updates adds the two transient points
(2,0,1),(0,1,4) to this tail, for 22 points. The old 10/12 targets are
false mathematical assertions. Their falsity does not falsify the receiver.

The consumed old program is never executed by this probe. CUSTODY.md
separately proves the conditional source-level failure route and states
why it cannot establish what bytes the original author actually captured.
A new deterministic calculation may not be relabelled as that old run.
