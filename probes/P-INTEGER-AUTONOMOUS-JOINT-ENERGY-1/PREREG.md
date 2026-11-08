# P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1

Status: PROSPECTIVE  
Scope: NON-CANONICAL, L1  
Owner: A. M. Thorn, session integer-autonomous-gravity-2026-10-19  
Ownership: https://github.com/mathorn1973/twist-j/issues/1649

## 1. Question, authority, action layer and custody

Can a selected positive-kinetic TT field and scalar source have a single
time-independent variational law, an exactly conserved positive quadratic
bond energy including their interaction, a symplectic physical step, and an
autonomous integer realization without a stored step counter, while their
joint exact rational reading requires unbounded precision?

The action layer is NEW_DECLARED L1. Every additional variable, constant
coupling, normalization, source force, Hermitian realization, denominator
coordinate and bank rule below is explicit model data. The named physical
comparison variables are mathematical reading variables. No physical clock,
native-U realization, positive full nonlinear gravitational Hamiltonian,
unique coupling selection or continuum limit is assumed.

Public Canon v103 is active at main and peeled canon-v103 commit
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d, content commit
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66. SOURCE.md records the actual
five normative hashes and sizes, checked against local bytes by both
programs. canon/CANON.md is 1052518 bytes with SHA-256
d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b.

Companion context is P-INTEGER-JOINT-VARIATION-1 (#1646), pin
fe5456f1aac8adcc3fdb0222df81f7e2fc773977, and
P-INTEGER-POSITIVE-KINETIC-JOINT-1 (#1648), pin
bd7e1dada3a4869ecfae76c0aea03c0a88c9983f. This probe declares a new constant
coupling and a new integer carrier. No preceding finite certificate is
substituted for a certificate of this construction. In particular, a
constant coupling does not inherit the summable-forcing estimate of a
coupling that decays with the counter.

Before any scientific execution or import, freeze PREREG.md, PROOF.md,
SOURCE.md, verify.py, breaker.py and FROZEN.sha256; publish the immutable
pin and read all six files back. Static reading, AST parsing and file
hashing are permitted before the pin. All numerical quantities below are
exact integers, rationals or algebraic proof quantities; there are no
floating-point calculations, fitted constants, clipping, chosen tolerances
or post-run fixture selection. No frozen file changes after execution.

## 2. Constant variational law and equilibrium

Let m=324, g=1/m, ell=(1,-1,0,0,0), e=(1,1,1,1,1), and

    (C P)_r=460 P_r+29(P_(r-1)+P_(r+1))+65(P_(r-2)+P_(r+2)),
    L=(648 I-C)/324.

Spatial indices are modulo five. Fix the context a in {-1,0,1} and put
A_src=a/4. This context is fixed during evolution and variation. The
rational five-vector h and rational scalar chi obey, for every n>=1,

    h_(n+1)-2h_n+h_(n-1)+Lh_n = g chi_n ell,
    chi_(n+1)-chi_n+chi_(n-1) = A_src+g<ell,h_n>.

The full comparison action is the canonical quadratic metric action A_2,
with all six symmetric spatial metric components, lapse and shift retained,
plus the declared source and interaction terms:

    A_auto[Vmetric,lapse,shift,chi]
      = A_2[Vmetric,lapse,shift]
        +(1/2) sum_(n>=0) (chi_(n+1)-chi_n)^2
        -sum_(n>=1) (chi_n^2/2-A_src chi_n)
        +(g/2) sum_(n>=1) chi_n<ell,Vmetric_11,n-Vmetric_22,n>.

Independent variations have finite support in n>=1 and fix the n=0
boundary data. The n=1 values select the solution and are not removed from
virtual variations at n=1. The infinite notation means compatible local
action changes, not convergence of a numerical infinite sum. Vary before
evaluating at Vmetric=diag(h,-h,0), lapse=shift=0. The full first variation
there is minus one half of the field residual paired with
delta Vmetric_11-delta Vmetric_22, and minus the source residual paired
with delta chi. The other metric, lapse and shift gradients vanish by
the canonical full-variation argument. Both remaining residuals vanish
on the displayed joint law.

On the fixed-mean space sum h=1 put x=(h-e/5,chi), f=(0,0,0,0,0,A_src),
and

    K=[[L,-g ell],[-g ell^T,1]],
    x_(n+1)-2x_n+x_(n-1)+Kx_n=f.

The following exact quantities fix the equilibrium without a numerical
linear solve being treated as its definition:

    L^-1 ell=(324/53605)(253,-253,36,0,-36),
    c=<ell,L^-1 ell>=163944/53605,
    delta=g^2 c=253/8684010,
    q=8683757,
    chi_*=A_src*8684010/q,
    h_*=e/5+A_src*(40986,-40986,5832,0,-5832)/q.

The inverse of L here is restricted to e^perp. The equilibrium obeys
Lh_*=g chi_* ell and chi_*=A_src+g<ell,h_*>.

PROOF.md establishes K>0 on e^perp x R exactly when
g^2<53605/163944. At the fixed g=1/324 it proves

    (59/100)I<K<(201/200)I,
    R_K=K-K^2/4>I/2

on that five-dimensional space. On all six coordinates K retains the
constant spatial null mode; it is not positive definite there.

## 3. Conserved energy and the canonical physical map

For z_n=(h_n-h_*,chi_n-chi_*) define the total bond quantity

    Htot_n=||z_n-z_(n-1)||^2/2+<z_(n-1),Kz_n>/2.

It includes the interaction energy. With u=z_n-z_(n-1) and
v=(z_n+z_(n-1))/2,

    Htot_n=<u,(I-K/4)u>/2+<v,Kv>/2.

This is positive definite on ordered pairs in (e^perp x R)^2 and is
exactly conserved by the constant joint law. Completing the square gives

    Htot_n=||z_(n-1)-(I-K/2)z_n||^2/2+<z_n,R_K z_n>/2.

The sharp energy-ellipsoid site criterion uses
<p_r,R_K^-1 p_r>, p_r=(e_r-e/5,0); the simpler bounds used here are

    |h_n(r)-h_*(r)|^2 <= 16 Htot_1/5,
    |chi_n-chi_*|^2 <= 4 Htot_1.

For arbitrary carrier states whose spatial means are not fixed, the same
quadratic expression remains an exactly conserved reading under the affine
step. The positive-definiteness claim is restricted to the stated mean
subspace. The finite unrestricted-carrier audit checks conservation without
claiming positive definiteness there.

For a=0 it is useful to exhibit the three bond terms separately:

    Hh_n=||h_n-h_(n-1)||^2/2+<h_(n-1),Lh_n>/2,
    Hchi_n=(chi_n-chi_(n-1))^2/2+chi_(n-1)chi_n/2,
    I_n=-(g/2)[chi_(n-1)<ell,h_n>+chi_n<ell,h_(n-1)>],
    Htot_n=Hh_n+Hchi_n+I_n.

For nonzero a, use the authoritative centered matrix formula for Htot;
the equilibrium linear and constant terms may not be dropped.

In centered physical coordinates z and canonical momentum p, the exact
discrete Legendre step is

    p_n=z_n-z_(n-1),
    p_(n+1)=p_n-Kz_n,
    z_(n+1)=z_n+p_(n+1).

Its type-II generating function is

    F2(z,pnew)=<z,pnew>+||pnew||^2/2+<z,Kz>/2,
    d_z F2=pnew+Kz=pold,
    d_pnew F2=z+pnew=znew.

This is the discrete canonical map derived from the action. The conserved
quadratic bond quantity is not silently identified with a Hamiltonian whose
unit-time continuous flow produces this entire discrete map.

Let the two-slice ordering be (current,previous),

    B=[[C,ell],[ell^T,m]],
    Tmat=[[B/m,-I6],[I6,0]],
    J12=[[0,-I6],[I6,0]].

The exact matrix identity Tmat^T J12 Tmat=J12 holds. For two tangent
solutions, or two solutions after subtracting the same equilibrium, the
alternating form

    Omega_n=<z_(n-1)^1,z_n^2>-<z_n^1,z_(n-1)^2>

is constant. No positive or negative signature is assigned to this
alternating form. For two arbitrary affine solution points x^1,x^2 the
uncentered expression instead has increment

    Omega_raw,(n+1)-Omega_raw,n=<f,x_n^1-x_n^2>.

The latter is explicitly a negative control below. A symplectic claim for
the bare physical map is not automatically a symplectic claim for the
bank-reflected discrete carrier.

## 4. Autonomous integer carrier, inverse and Hermitian realization

The unrestricted integer core is (Z,R,D,H), where

    Z=(P_0,P_1,P_2,P_3,P_4,Y) in Z^6,
    R=(Q_0,Q_1,Q_2,Q_3,Q_4,V) in Z^6,
    D in Z_(>=1), H in Z^8.

Both physical slices use the SAME CURRENT denominator:

    (h,chi)=Z/D, (hprev,chiprev)=R/D.

There are 21 integer core coordinates. Bank b>=0 and direction
epsilon in {-1,1} make 23. No preparation, mean, congruence or monitor
relation is imposed on this full carrier.

The total bare forward macrostep is

    Z'=BZ-mR+81aD e_6,
    R'=mZ,
    D'=mD,
    H'=M(Y'-Y) H M(Y'-Y)^dagger.

Every coefficient is constant. D is a denominator coordinate, not a
stored time counter or a native-U clock. Neither the physical equation
nor this integer core requires an externally supplied step index.

Given a candidate image (Z',R',D',H'), its predecessor exists exactly when:

1. D' is divisible by m;
2. each of the six entries of R' is divisible by m;
3. after D=D'/m and Z=R'/m are set, each of the six entries of
   BZ+81aD e_6-Z' is divisible by m.

There are 13 scalar divisibility conditions. The inverse then sets

    R=(BZ+81aD e_6-Z')/m,
    H=M(Y-Y') H' M(Y-Y')^dagger.

D'>0 and the first divisibility imply D>=1. The Hermitian transport
creates no further image restriction.

For the Hermitian realization use O=Z[j], 1+j+j^2+j^3+j^4=0,
conjugation j*=j^4, phi=-j^2-j^3, J=1+j^2, J^-1=-j-j^2,
phi^-1=phi-1, A_H=diag(J,phi), B_H(t)=[[1,t],[0,1]], and
D_H=diag(0,1). Thus

    v_J=J/phi-1=-2+j-j^2, v_J v_J*=9-5phi,
    M(t)=A_H B_H(t) A_H^-1 B_H(-t)=[[1,t v_J],[0,1]].

An H8 tuple (a0,a1,d0,d1,c0,c1,c2,c3) represents

    H=[[a0+a1phi,c],[c*,d0+d1phi]],
    c=c0+c1j+c2j^2+c3j^3.

The positive integer arithmetic cost is

    N(H)=4a0^2+4a0a1+6a1^2+4d0^2+4d0d1+6d1^2
          +10 sum_i c_i^2-2(sum_i c_i)^2
         =Tr_(Q(j)/Q)(tr(H^2)) >= 2||H8||^2.

The prepared monitor is

    H_Y=M(Y) D_H M(Y)^dagger,
    H_Y8=(9Y^2,-5Y^2,1,0,-2Y,Y,-Y,0),
    N(H_Y)=294Y^4+52Y^2+4.

The declared transport preserves H=H_Y, det H=0, and the prepared
source reader coeff_j(H_01)/D=Y/D. On the full carrier H is independent
of Y; the source equation uses the explicit scalar Y. This monitor is
not a derivation of the new source equation from the native law U.

Admission charges the one combined macrostep. The four algebraic factors
of M are not four separately banked time phases.

## 5. Bank reflection, finite shells and precision

Set

    E(Z,R,D,H)=1+D+||Z||^2+||R||^2+N(H).

For y=T^epsilon x, reflect (x,b,epsilon) to (x,b,-epsilon) if the inverse
domain is absent or b+E(x)-E(y)<0. Otherwise move to
(y,b+E(x)-E(y),epsilon). Rev changes only epsilon. PROOF.md proves on
the entire unrestricted carrier

    F^-1=Rev F Rev,
    E+b conserved,
    Htot conserved as a rational reading.

The bank account E+b and the quadratic bond quantity Htot are different
conserved quantities. No identification of arithmetic cost with physical
energy is made.

The proper positive account has finite shells. D increases by m>1 along
every bare forward edge, so an admitted connected component is a finite
path; its funded orbit has least period twice its number of vertices.
For a prepared sequence x_n, the sharp bank to reach N is

    Bsharp(N)=max_(1<=n<=N) E(x_n)-E(x_1).

The last reached counter is the largest N with Bsharp(N)<=b. This
definition uses prefix maxima, not global monotonicity of E.

Prepared histories below have D_n=40m^(n-1) for n>=1 and sum P_n=D_n.
Their displayed storage cost satisfies

    E(x_n)>=||P_n||^2>=D_n^2/5=320m^(2(n-1)).

There is also a representation-independent joint precision statement.
Let d_n be the least common denominator of ALL SIX rational values
(h_n,chi_n), with positive denominator convention. PROOF.md uses

    zint_n=(5P_n-D_n e,5Y_n),
    zint_(n+1)=B zint_n modulo 3,
    B|_(e^perp x F_3)=[[-I,ell],[ell^T,0]],

where the last matrix is invertible because <ell,ell>=2 is nonzero
modulo 3. A prepared unoccupied site has 5*6-40=-10, nonzero modulo 3.
Consequently

    v_3(d_n)=4(n-1), n>=1.

For any common integer numerator/denominator representation
(Pbar,Ybar,Dbar) of those same six rational readings,

    Dbar>=3^(4(n-1)),
    ||Pbar||^2+Ybar^2+Dbar^2 >= (6/5)3^(8(n-1)).

The supplied D_n is not asserted fully primitive at 2 or 5. This is a
claim about the joint six-value denominator, not about each field
component individually or the field-only denominator at every step.

## 6. Prepared family and all-counter metric domain

For t=0,1, u_t=w_(t+2)-w_t, let P_t^can have ones at u_t and u_t+1
modulo five and zero elsewhere. The canonical comparison initial slice
is h_t^can=P_t^can/2. The complete fixed word order and energy data are:

| word | u0 | u1 | Hcan_1 | <ell,hcan_0> |
| --- | ---: | ---: | --- | --- |
| 0010 | 1 | 0 | 713/2592 | -1/2 |
| 0011 | 1 | 1 | 53/432 | -1/2 |
| 0100 | 0 | -1 | 713/2592 | 0 |
| 0101 | 0 | 0 | 53/432 | 0 |
| 0110 | 1 | -1 | 67/162 | -1/2 |
| 1001 | -1 | 1 | 67/162 | 1/2 |
| 1010 | 0 | 0 | 53/432 | 0 |
| 1011 | 0 | 1 | 713/2592 | 0 |
| 1100 | -1 | -1 | 53/432 | 1/2 |
| 1101 | -1 | 0 | 713/2592 | 1/2 |

Declare the new ready normalization

    h_t=e/5+(h_t^can-e/5)/4, t=0,1,
    chi_0=0, chi_1=a/4.

It retains all ten word shapes at attenuated amplitude. It is not the
unchanged unit-amplitude canonical preparation. For each a in (-1,0,1)
the first core is

    D_1=40, P_1=6e+5P_1^can, Q_1=6e+5P_0^can,
    Y_1=10a, V_1=0, H=H_(10a).

The synthetic n=0 record uses D_0=40, P_0=6e+5P_0^can, Y_0=0,
H=D_H. It is an initial history record, not an additional predecessor
core claimed in the exact image domain.

The exact initial total bond energy is

    Htot_1=Hcan_1/16-(ga/32)<ell,h_0^can>+a^2/[32(1-delta)].

The maximum canonical energy is 67/162. PROOF.md establishes from this
formula and the positive bond form, for all thirty histories and every
n>=0,

    0<Htot_n<3/50 for bonds n>=1,
    |h_n(r)-1/5|<9/20, |chi_n|<3/4,
    -1/4<h_n(r)<13/20,
    g_n(r)=diag(-1,1+h_n(r),1-h_n(r),1),
    det g_n(r)<-231/400<0.

The proof uses the fixed energy ellipsoid, not uniform closeness to an
uncoupled orbit. It proves Lorentz signature on this prepared family.
Arbitrary integer carrier states need not have a nondegenerate metric.

## 7. Fixed exact witnesses

For the direct source contrast, word 0010 gives at n=2

    D_2=12960,
    P2(-)=(4379,2779,794,2594,2414), Y2(-)=-6480,
    P2(+)=(4399,2759,794,2594,2414), Y2(+)=6480,
    h2(+)-h2(-)=ell/648.

These are different fixed a contexts, setting both chi_1 and A_src.
The following feedback comparisons remain in the single a=0 context.

For word 0011, a=0:

    D_1=40, P_1=Q_1=(6,11,11,6,6), Y_1=V_1=0,
    D_2=12960, P_2=(2414,2769,2769,2414,2594), Y_2=-5,
    D_3=4199040, P_3=(973001,594836,594831,973006,1063366),
    Y_3=-1975.

Hence

    chi_2=-1/2592,
    h_3-h_3^free=-ell/839808,
    chi_3-chi_3^(first-feedback-only)=-71/839808.

Here h^free follows the same attenuated initial field with no source
term. The first-feedback-only comparison retains the feedback at n=1
and suppresses it thereafter; it gives chi_3=chi_2. This nonzero contrast
therefore probes feedback from an evolved field.

The first two bonds have

    Htot_1=Htot_2=53/6912,
    Hh_2-Hh_1=0,
    Hchi_2-Hchi_1=1/13436928,
    I_2-I_1=-1/13436928.

The source gain is exactly balanced by the interaction. It is not called
a field-only energy loss at this first step. At the next exchange, with
b0=839808, the optional exact values are

    Hh_3-Hh_2=-180609/(2b0^2),
    Hchi_3-Hchi_2=28045/(2b0^2),
    I_3-I_2=152564/(2b0^2).

They also sum to zero and are fixed here as exact witness assertions,
without a separate certificate count.

For this same seed the integer account values are

    E(x_1)=745, E(x_2)=70657990,
    N(H_-5)=185054,
    ||P_2||^2=33718350, ||R_2||^2=36741600,
    Bsharp(2)=70657245.

Bank 70657244 rejects the first step. Bank 70657245 admits it with zero
remaining bank. The latter budget is not asserted to reach n=3.

## 8. Exact finite audit and negative controls

### 8.1 Authority, Hermitian transport and holonomy

Both programs check all five normative files by byte size and SHA-256.
The ordered Hermitian fixture list HF has 19 entries: first zero; then
for i=0,...,7 append +e_i and -e_i in that order; finally append

    (1,-1,2,0,-2,1,0,1),
    (0,1,-1,2,1,0,-1,2).

For each H, check integer closure, exact inverse, determinant and the
trace/positive cost formula under A_H, A_H^-1 and B_H(t) for
t=-2,-1,0,1,2: 19*7=133 transport checks. For every H and these five t,
compare direct M(t) transport with the four factors, reverse it and
check determinant: 19*5=95 holonomy checks. Matrix products act on the
rightmost factor first: B_H(-t), A_H^-1, B_H(t), A_H.

### 8.2 Full carrier, reflection branches and corrupt images

For a=-1,0,1, i=0,...,18, and D=1,2,40, take

    P=(i-9,1,-2,0,3), Q=(2,-1,0,1,9-i),
    Y=i%5-2, V=(i//5)%5-2, H=HF[i].

These are 171 base (context,core) fixtures. Add one decreasing-account
fixture with a=0,D=1,P=Q=(0,0,0,0,0),Y=V=100,H=H_100. There are exactly
172 core fixtures. For each x and y=T(x), check the exact inverse and
D(y)=mD(x). Whenever x itself has an inverse, check its forward image too.

For each z in (x,y), set delta_E=E(T(z))-E(z) and use all six bank
positions

    0,1,772,max(0,delta_E-1),max(0,delta_E),max(0,delta_E+1)

with both directions. Duplicate numerical bank values remain separate
declared fixture positions. In every one of 172*2*6*2=4128 cases require
the actual funded output to equal its prescribed move or reflection,
both inverse compositions to recover the input, integer carrier
membership, E+b conservation, and rational Htot conservation.
Require all five branches: forward motion, backward motion, forward
bank refusal, backward bank refusal, and missing backward image.

For EACH OF THE 171 BASE fixtures, corrupt the image T(x) by adding +1
to exactly one of these thirteen coordinates, separately:

    D'; Q'_0,Q'_1,Q'_2,Q'_3,Q'_4,V';
    P'_0,P'_1,P'_2,P'_3,P'_4,Y'.

There are 171*13=2223 corrupt images; the added decreasing fixture is
not part of this count. Each must have no backward image and must
reflect backward at bank 1000000000. This tests both the outer scale
congruences and the six reconstruction congruences. The base denominators
1,2,40 also exercise the absent-image lower domain directly.

### 8.3 Histories, precision and energy

Evolve all ten words in table order, a=-1,0,1, through n=12. There are
30*13=390 history records, including the synthetic n=0 data. At every
record require exact integer coordinates, decoding, sum P=D, sum h=1,
the prepared H_Y shape and reader, determinant zero for H, its exact
positive cost, the source bound and the field/signature bounds of section 6.
At core records n>=1 require the storage lower bound 5E>=D^2.

Check both rational difference equations at n=1,...,11. The actual
stored previous slice R_n/D_n must equal the preceding rational history
slice. Independent implementations derive their own histories from the
declared law and exact representation.

Hash the concatenated ASCII records in word, a, n order, with one LF per
record, signed decimal integers without leading zeroes, and no spaces:

    word|a|n|P0,P1,P2,P3,P4|Y|D|H0,H1,H2,H3,H4,H5,H6,H7\n

At n=0 use exactly D=40,Y=0,H=D_H and the prescribed P_0. For n>=1
use the actual current integer core. The same D represents both current
and previous core slices but only the current slice appears in this digest.

At every n=1,...,12 in each history calculate the joint least common
denominator from all six reduced rational values and check
v_3(d_n)=4(n-1): 30*12=360 PRECISION_CHECKS. Separately check the total
bond quantity Htot_n equals Htot_1 exactly and lies strictly between 0
and 3/50: 30*12=360 ENERGY_BONDS. The all-counter conclusions are proved
analytically; these finite counts do not replace those proofs.

### 8.4 Reduced action and off-shell derivatives

With the neighboring slices fixed, the local reduced action is

    A_local(v,xi)=(||v-hprev||^2+||hnext-v||^2)/2-<v,Lv>/2
                  +((xi-chiprev)^2+(chinext-xi)^2)/2
                  -xi^2/2+A_src xi+g xi<ell,v>.

For every history and n=1,2,5,11, evaluate the exact central unit
differences [A(t+1)-A(t-1)]/2 in each of the five current TT values and
the source scalar. All 30*4*6=720 derivatives must vanish. This count
is for the reduced TT-plus-source action; the full six-metric-component,
lapse and shift variation is analytical in PROOF.md.

Six separate off-shell cases are tested at n=2. The first five start
from word0011,a=0 and change only one quantity: current v_0 by +1;
current xi by +1; next chi by +1; next h_2 by +1; previous chi by -1.
The sixth has

    v=(1/3,-2/5,0,3/7,-1), xi=-2/3,
    hprev=(0,0,0,0,0), hnext=(1,1,1,1,1),
    chiprev=1/2, chinext=-3/4, a=1, A_src=1/4.

All six central derivatives in each case must equal the independently
derived gradients

    grad_h=2v-hprev-hnext-Lv+g xi ell,
    grad_chi=xi-chiprev-chinext+A_src+g<ell,v>.

Require at least one nonzero gradient per off-shell case: 36 derivative
checks. The affine source force is a/4 even in this off-shell context.

### 8.5 Positivity forms, canonical steps and symplectic checks

Let U be the six-by-five matrix with columns (e_i-e_4,0), i=0,1,2,3,
and the scalar source unit vector. For EACH of the three SIX-dimensional
forms

    K-(59/100)I6,
    (201/200)I6-K,
    K-K^2/4-I6/2,

form the five-by-five Gram matrix U^T(form)U and require every leading
principal minor of size 1,...,5 to be strictly positive. There are 15
K_MINOR_CHECKS. In particular, U^T I6 U is the Gram matrix of the
nonorthonormal basis, not I5.

At each n=1,...,11 on all thirty histories check the canonical
kick-drift identities and both generating-function derivative identities
of section 3 in all six coordinates. These are 30*11=330
CANONICAL_STEPS, each a complete vector check. Also check the full
12-by-12 matrix identity Tmat^T J12 Tmat=J12 exactly.

For each fixed a=-1,0,1, each of the 45 unordered pairs of distinct
word labels in their table order, and each bond n=1,...,12, compute
the CENTERED Omega_n and require Omega_n=Omega_1. This gives
45*3*12=1620 SYMPLECTIC_CHECKS. Coincident physical histories with
different word labels remain separate declared pairs.

As an explicit affine negative control, use the UNcentered Wronskian
for ordered words (0010,0011), a=1. Require the increment from bond
2 to bond 3 to equal

    (1/4)(chi_2^(0010)-chi_2^(0011))=1/10368 != 0.

Its nonconservation is expected. Only tangent or commonly centered
solution pairs carry the claimed conserved alternating form.

### 8.6 Fixed witnesses, disabled laws and complete funded cycles

Check all exact witnesses in section 7, including the direct and
continuing-feedback contrasts and the interaction-inclusive energy
balance. The following comparison laws are separately named controls;
they do not alter the main definition:

1. Disable field-to-source feedback. For word0011,a=0, chi stays zero
   and h is the attenuated free field. The joint source gradient at n=1
   is -1/2592, not zero.
2. Retain feedback only at n=1. The continued-source contrast at n=3 is
   -71/839808 as in section 7.
3. Disable source-to-field coupling while retaining feedback. For
   word0011,a=0, h stays free and the joint metric gradient at n=2 is
   -ell/839808.
4. Reverse the feedback sign. The main-law source gradient at
   word0011,a=0,n=1 is -1/1296, not zero.
5. Omit the Hermitian transport. At the first zero-source image the
   stored monitor still has coefficient zero while Y_2=-5.
6. Omit interaction from the proposed conserved bond quantity. In the
   zero-source witness the first energy increment is +1/13436928,
   not zero; inclusion of I cancels it exactly.
7. Read the unrestricted integer core with D=1,P=(1,0,0,0,0),Y=0,
   Q=(0,0,0,0,0),V=0,H=D_H. Its metric at site0 has determinant zero.
   This is outside the prepared Lorentz family.

For word0011, in order a=-1,0,1, and for each target N=1,2, set the
bank to the prospective formula max_(1<=n<=N)E(x_n)-E(x_1). Require
E(x_1)<E(x_2)<E(x_3) for these three selected histories, and traverse
each funded orbit until its first return, checking no earlier repeated
state. The six least periods must be

    2,4,2,4,2,4.

No larger-horizon monotonicity is inferred. Separately require the
fixed zero-source bank 70657244 to reject and bank 70657245 to admit
the first step with zero residual bank. The general sharp-horizon
theorem uses prefix maxima and the finite-shell bound.

## 9. Certificate grammar, falsifiers and completion

Each implementation emits the same 27-line certificate as unmodified
ASCII bytes, with one LF after each line including the final line:

    CERTIFICATE=P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1
    AUTHORITY_FILES=5
    TRANSPORT_CHECKS=133
    HOLONOMY_CHECKS=95
    CORE_FIXTURES=172
    FUNDED_CASES=4128
    IMAGE_DEFECTS=2223
    HISTORY_RECORDS=390
    HISTORY_SHA256=<computed lowercase SHA-256>
    JOINT_VARIATIONS=720
    OFFSHELL_VARIATIONS=36
    K_MINOR_CHECKS=15
    ENERGY_BONDS=360
    PRECISION_CHECKS=360
    CANONICAL_STEPS=330
    SYMPLECTIC_CHECKS=1620
    DIRECT_CONTRAST=1/648,-1/648,0,0,0
    ZERO_SOURCE_CHI2=-1/2592
    RECIPROCAL_CONTRAST=-1/839808,1/839808,0,0,0
    CONTINUED_SOURCE_CONTRAST=-71/839808
    ZERO_SOURCE_TOTAL_ENERGY=53/6912
    ZERO_SOURCE_ENERGY_EXCHANGE=0,1/13436928,-1/13436928
    AFFINE_WRONSKIAN_DRIFT=1/10368
    ZERO_SOURCE_FIRST_BANK=70657245
    CYCLE_PERIODS=2,4,2,4,2,4
    NEGATIVE_CONTROLS=PASS
    CERTIFICATE_RESULT=PASS

The primary launches breaker.py in a separate process with the same
Python executable and -I, requiring exit zero, empty stderr and exact
raw certificate byte identity. It then appends two lines:

    BREAKER_RAW_BYTES=IDENTICAL
    RESULT=PASS

Successful primary stdout therefore has exactly 29 LF-terminated lines.
No line-ending normalization may manufacture primary/breaker identity.

Every check uses exact equality or the stated strict rational inequality.
Only a ScientificFailure with a registered key is caught; it emits
FALSIFIER=<key> and RESULT=FAIL. For BREAKER_BYTES, preserve the actual
child stdout as hexadecimal evidence. Unexpected runtime and protocol
errors remain nonzero. Registered keys are:

    AUTHORITY, RING, TRANSPORT, HOLONOMY, COST, INITIAL_DATA,
    INTEGER, BARE_INVERSE, FUNDED_INVERSE, CONSERVATION, BRANCH,
    IMAGE_GUARD, RECURRENCE, MEAN, SOURCE_READER, LORENTZ,
    SOURCE_BOUND, EQUILIBRIUM, ENERGY, PRECISION, GRAM,
    ACTION, OFFSHELL_ACTION, CANONICAL, SYMPLECTIC, FIXED_COUNTER,
    CONTROL, SHARP_BUDGET, PERIOD, CERTIFICATE, BREAKER_BYTES.

A failed equality, domain branch, bound, exact witness or certificate
requirement falsifies the corresponding declared finite gate. No failure
threshold is adjusted after observing a result. After the first completed
gate preserve exact EXPECTED.txt and factual RUN.md/RESULT.md, and open
one draft PR for the unchanged Python 3.12 workflow to replay on both
x86_64 and aarch64. The frozen six-file bundle remains byte-identical.

An earned result has only the stated NON-CANONICAL L1 scope. It does not
promote Canon, establish nonlinear Einstein dynamics, derive a native-U
source, identify the arithmetic bank with physical energy, prove an
all-counter Lorentz domain for the original unattenuated packet, or
assert a continuum or physical-clock interpretation.
