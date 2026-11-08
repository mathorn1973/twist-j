# Proofs for P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1

Scope: NON-CANONICAL, L1.  
Ownership: https://github.com/mathorn1973/twist-j/issues/1649.

This document proves the exact mathematical construction specified in
PREREG.md: a constant joint variational law, its discrete canonical map,
a conserved positive bond energy including interaction on the fixed-mean
space, an autonomous integer lift and its complete image criterion, two
distinct conserved accounts after reflection, an all-counter Lorentz domain
for the declared attenuated preparations, and an unavoidable joint 3-adic
denominator growth. The finite executable gate supplements these proofs; it
does not establish the all-counter statements by extrapolation.

The normative comparison is Public Canon v103 at main and peeled tag
canon-v103 commit dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d, content commit
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66. DEF-K1-LINEAR-METRIC specifies
the ten word preparations, spatial operator and full quadratic action.
The new constant coupling, source action, amplitude and source-force
normalizations, integer lift, Hermitian monitor and admission rule are
explicit L1 choices. No native-U source law, physical clock, nonlinear
Einstein equation, coupling uniqueness or continuum limit is inferred.

## 1. Full joint action and both stationary equations

Let e=(1,1,1,1,1), ell=(1,-1,0,0,0), m=324, g=1/m, and let S be the
cyclic spatial shift on five marked sites. Define the real symmetric
operators

    C=460I+29(S+S^-1)+65(S^2+S^-2),
    L=(648I-C)/324.

Thus Ce=648e, Le=0, and <e,ell>=0. The Euclidean spatial inner product is
the unweighted sum over the five sites. Fix a in {-1,0,1} throughout
evolution and variation, and write A_src=a/4.

### 1.1 The selected spatial derivative and full metric action

The comparison action uses the particular derivative branch fixed by the
Canon, not an unspecified square root of L. Let the unitary Fourier matrix
be F_kr=exp(2 pi i k r/5)/sqrt(5), and set

    lambda_0=0,
    lambda_1=lambda_4=(235+18sqrt(5))/324,
    lambda_2=lambda_3=(235-18sqrt(5))/324,
    kappa=(0,sqrt(lambda_1),sqrt(lambda_2),
             -sqrt(lambda_2),-sqrt(lambda_1)),
    Dsp=F^dagger diag(i kappa) F.

Conjugate Fourier pairing makes Dsp real, Dsp^T=-Dsp, and Dsp^T Dsp=L.
Its entries are real algebraic numbers; membership in a particular
quadratic coefficient field is not claimed. The rational dynamics below
uses L, not the individual entries of Dsp.

Retain all six independent entries of the symmetric spatial perturbation
Vmetric, the lapse ell_0 and the three shifts N_i. With Delta=E_time-1,
the canonical half-slice placement is

    K11=Delta Vmetric11/2, K22=Delta Vmetric22/2,
    K12=Delta Vmetric12/2,
    K13=(Delta Vmetric13-Dsp N1)/2,
    K23=(Delta Vmetric23-Dsp N2)/2,
    K33=(Delta Vmetric33-2Dsp N3)/2, Ktr=Tr(Kij),

    G2(Vmetric)=<Dsp Vmetric3j,Dsp Vmetric3j>/2
                -<Dsp Vmetric33,Dsp Tr(Vmetric)>/2
                +<Dsp Tr(Vmetric),Dsp Tr(Vmetric)>/4
                -<Dsp Vmetricij,Dsp Vmetricij>/4,
    R1(Vmetric)=Dsp^2 Vmetric33-Dsp^2 Tr(Vmetric),

    A2=sum_n [<Kij,Kij>-<Ktr,Ktr>+G2(Vmetric)+<ell_0,R1(Vmetric)>].

Repeated i,j indices run from 1 to 3; off-diagonal entries occur twice
in an ij sum. Only the spatial derivative in direction 3 is nonzero.

At Vmetric=diag(h,-h,0), ell_0=N_i=0, the trace, Ktr, Vmetric3j and R1
vanish. Before restricting any virtual variation, the surviving kinetic
and spatial first variations are respectively

    (1/2) sum_n <Delta h,Delta(delta Vmetric11-delta Vmetric22)>,
    -(1/2) sum_n <Dsp h,Dsp(delta Vmetric11-delta Vmetric22)>.

All lapse, shift, off-diagonal and remaining diagonal variations have
zero coefficients there. Spatial adjointness and time summation by parts
therefore give

    delta A2=-(1/2) sum_(n>=1)
              <(Delta_c^2+L)h_n,delta Vmetric11_n-delta Vmetric22_n>,

where Delta_c^2 f_n=f_(n+1)-2f_n+f_(n-1). This is the full first
variation evaluated at the representative, not merely the variation of
an action restricted in advance.

### 1.2 Source and interaction

Add the positive-kinetic source and constant interaction:

    A_auto=A2+(1/2)sum_(n>=0)(chi_(n+1)-chi_n)^2
               -sum_(n>=1)(chi_n^2/2-A_src chi_n)
               +(g/2)sum_(n>=1)chi_n<ell,Vmetric11_n-Vmetric22_n>.

Variations have finite support in n>=1 and fix the n=0 data. The n=1
values select the desired solution but remain available to virtual
variation at n=1. Infinite sums mean compatible local action changes;
convergence of an infinite numerical action is unnecessary.

The scalar kinetic first variation is -sum Delta_c^2 chi_n delta chi_n.
Adding its potential, force and interaction, and then evaluating at the
TT representative, yields

    delta A_auto
      =-(1/2)sum_(n>=1)
        <(Delta_c^2+L)h_n-g chi_n ell,
          delta Vmetric11_n-delta Vmetric22_n>
       -sum_(n>=1)
        [(Delta_c^2+1)chi_n-A_src-g<ell,h_n>]delta chi_n.

Consequently both continuous stationary equations are exactly

    (Delta_c^2+L)h_n=g chi_n ell,
    (Delta_c^2+1)chi_n=A_src+g<ell,h_n>.                 (1.1)

Both kinetic terms on the TT-plus-source space are positive. All other
full metric, lapse and shift gradients vanish at the representative by
the explicit argument above. This does not establish the nonlinear
constraint system of general relativity or a covariant matter action.

For fixed neighbors the reduced local gradients are, at arbitrary
comparison values v and xi,

    grad_v=2v-hprev-hnext-Lv+g xi ell,
    grad_xi=xi-chiprev-chinext+A_src+g<ell,v>.           (1.2)

The local action in PREREG.md is quadratic, so its central unit
differences equal (1.2) exactly, whether or not the comparison state
solves (1.1). Some off-shell partial derivatives can be zero; the
specified six cases each have at least one nonzero derivative.

## 2. Mean, exact equilibrium and the positive stiffness range

Summing the field equation in (1.1) gives

    sum h_(n+1)-2sum h_n+sum h_(n-1)=0.

Both prepared initial sums are one. Hence sum h_n=1 for every n>=0.
On the five-dimensional space V=e^perp x R set

    x_n=(h_n-e/5,chi_n), f=(0,0,0,0,0,A_src),
    K=[[L,-g ell],[-g ell^T,1]].

Then (1.1) is Delta_c^2 x_n+Kx_n=f. The full six-dimensional K has
the spatial constant null vector (e,0); claims of positive definiteness
below concern V.

### 2.1 Schur complement and exact equilibrium

On the reflection-odd field vectors (u,-u,v,0,-v), L is represented by

    (1/324)[[217,-36],[-36,253]].

Its determinant numerator is 217*253-36^2=53605. Therefore

    L^-1 ell=(324/53605)(253,-253,36,0,-36),
    c=<ell,L^-1 ell>=163944/53605.                     (2.1)

Here L^-1 acts only on e^perp. Completing the field square gives

    <(h,chi),K(h,chi)>
      =<h-g chi L^-1 ell,L(h-g chi L^-1 ell)>
         +(1-g^2 c)chi^2.

Since L is positive definite on e^perp, this proves the exact condition

    K>0 on V if and only if g^2<53605/163944.           (2.2)

At g=1/324,

    delta=g^2 c=253/8684010, q=8683757=8684010-253.

The equilibrium equations are L(h_*-e/5)=g chi_* ell and
chi_*-g<ell,h_*> = A_src. Substituting (2.1) gives their unique
solution on the fixed-mean affine space:

    chi_*=A_src*8684010/q,
    h_*=e/5+A_src*(40986,-40986,5832,0,-5832)/q.        (2.3)

Thus x_*=(h_*-e/5,chi_*) satisfies Kx_*=f. Unlike the uncoupled
center (e/5,A_src), (2.3) is the actual coupled equilibrium.

### 2.2 Rational spectral bounds

The nonzero eigenvalues of L are

    lambda_+=(235+18sqrt(5))/324,
    lambda_-=(235-18sqrt(5))/324,

each twice. They lie strictly between 1/2 and 1. The off-diagonal
perturbation K-diag(L,1) has operator norm sqrt(2)|g|. Since
sqrt(5)<9/4 and sqrt(2)<3/2, at the chosen g

    lambda_min(L)>389/648,
    ||K-diag(L,1)||<1/216,
    K>(193/324)I>(59/100)I,
    K<(217/216)I<(201/200)I                           (2.4)

on V. In particular every eigenvalue of K on V lies between 0 and 2.
The function t(1-t/4) increases on (0,2), so spectral calculus yields

    R_K=K-K^2/4>(20119/40000)I>I/2 on V.              (2.5)

This proves all three positive forms in the finite Gram audit.
For the nonorthonormal basis matrix U in PREREG.md, a nonzero
five-vector v gives Uv nonzero in V. Thus
v^T U^T(K-59I/100)Uv>0, and likewise for the other two forms.
Sylvester's criterion then gives all fifteen positive leading minors.
The identity contribution is U^T I6 U, not I5.

## 3. Conserved total bond energy, including interaction

Set z_n=x_n-x_*=(h_n-h_*,chi_n-chi_*). The centered equation is

    Delta_c^2 z_n+Kz_n=0.                            (3.1)

For any consecutive pair define

    Htot_n=||z_n-z_(n-1)||^2/2+<z_(n-1),Kz_n>/2.      (3.2)

With u=z_n-z_(n-1) and v=(z_n+z_(n-1))/2, symmetry of K gives

    Htot_n=<u,(I-K/4)u>/2+<v,Kv>/2.                  (3.3)

Both forms in (3.3) are positive definite on V by (2.4). Consequently
Htot is positive definite on the ordered pair in V x V, vanishing
exactly when both centered slices vanish. On the full twelve
two-slice coordinates, K has a constant spatial null mode, so Htot
is only positive semidefinite. Its conservation does not require a
mean restriction.

For every sequence and every symmetric K, direct subtraction gives

    Htot_(n+1)-Htot_n
      =<z_(n+1)-z_(n-1),
          z_(n+1)-2z_n+z_(n-1)+Kz_n>/2.              (3.4)

Equation (3.1) makes (3.4) zero. Thus Htot_n=Htot_1 for every
counter, for every real or rational initial pair. This is the
interaction-inclusive bond invariant of the autonomous quadratic
variational law. It is not a separately prescribed arithmetic budget.

At a=0, chi_*=0 and h_*=e/5, and (3.2) expands to

    Htot_n=Hh_n+Hchi_n+I_n,
    Hh_n=||h_n-h_(n-1)||^2/2+<h_(n-1),Lh_n>/2,
    Hchi_n=(chi_n-chi_(n-1))^2/2+chi_(n-1)chi_n/2,
    I_n=-(g/2)[chi_(n-1)<ell,h_n>+chi_n<ell,h_(n-1)>]. (3.5)

For nonzero a the authoritative definition is the centered form
(3.2), including the equilibrium linear and constant terms.
Removing I_n from (3.5) generally destroys conservation.

### 3.1 The fixed energy ellipsoid

Completing the square in the previous slice gives

    Htot_n=||z_(n-1)-(I-K/2)z_n||^2/2
              +<z_n,R_K z_n>/2.                     (3.6)

The formula also holds with current and previous exchanged.
For p_r=(e_r-e/5,0) in V and a fixed nonnegative value H,
Cauchy-Schwarz in the R_K inner product gives the sharp real
energy-ellipsoid bound

    |h_n(r)-h_*(r)|^2
       <= 2H <p_r,R_K^-1 p_r>.                      (3.7)

Sharpness here refers to the full real ellipsoid: choose
z_n proportional to R_K^-1 p_r and the previous slice
(I-K/2)z_n. It does not assert attainment by a particular prepared
integer trajectory.

Because R_K>I/2, R_K^-1<2I on V and ||p_r||^2=4/5. Hence the
simpler bounds used for the prepared family are

    |h_n(r)-h_*(r)|^2 <= (16/5)Htot_1,
    |chi_n-chi_*|^2 <= 4Htot_1.                      (3.8)

The corresponding bounds cover n=0 by applying the exchanged-slice
version to the first bond. No comparison with a free orbit at large
n is needed.

## 4. Discrete Legendre map and the symplectic statement

In affine physical coordinates x, use the reduced one-bond Lagrangian

    Ld(x,xnew)=||xnew-x||^2/2-Vpot(x),
    Vpot(x)=<x,Kx>/2-<f,x>.

The discrete Euler-Lagrange matching of its two momentum definitions is

    p_n=D_2 Ld(x_(n-1),x_n)=x_n-x_(n-1),
    p_n=-D_1 Ld(x_n,x_(n+1))
        =x_(n+1)-x_n+Kx_n-f.

Thus the action gives exactly the canonical kick and drift

    p_(n+1)=p_n-Kx_n+f,
    x_(n+1)=x_n+p_(n+1).                            (4.1)

After subtracting x_*, the force disappears. With z=x-x_* the
type-II generating function is

    F2(z,pnew)=<z,pnew>+||pnew||^2/2+<z,Kz>/2,

and its derivatives give

    pold=d_z F2=pnew+Kz,
    znew=d_pnew F2=z+pnew.                            (4.2)

This is the precise action-derived canonical map. In these canonical
coordinates the conserved bond quantity is

    Htot=||p||^2/2+<z,Kz>/2-<p,Kz>/2
        =||p-Kz/2||^2/2+<z,R_K z>/2.                (4.3)

The discrete canonical map and the exact invariant (4.3) are distinct
mathematical assertions. In general the unit-time continuous Hamiltonian
flow of (4.3) is not the whole map (4.1); no such identification is made.

### 4.1 Symplectic form and affine centering

Let B=m(2I6-K)=[[C,ell],[ell^T,m]], which is symmetric. In
(current,previous) two-slice order, the homogeneous matrix and form are

    Tmat=[[B/m,-I6],[I6,0]],
    J12=[[0,-I6],[I6,0]].

Block multiplication using B^T=B proves

    Tmat^T J12 Tmat=J12.                             (4.4)

For two tangent solutions, or for two solutions after subtracting the
same x_*, (4.4) is precisely

    Omega_n=<z_(n-1)^1,z_n^2>-<z_n^1,z_(n-1)^2>,
    Omega_(n+1)=Omega_n.                            (4.5)

For two uncentered affine solution points x^1,x^2, substituting the
common force in their recurrences instead gives

    Omega_raw,(n+1)-Omega_raw,n=<f,x_n^1-x_n^2>.      (4.6)

A common nonzero force does not cancel in this pointwise uncentered
bilinear expression. The affine map itself is symplectic because its
derivative is Tmat; the correct invariant pairing uses tangent vectors
or a common centering as in (4.5).

The symplectic form is alternating and has no positive or negative
signature. The positive kinetic metric and the positive bond energy
are separate symmetric forms. On unrestricted physical data the bare
map has twelve canonical two-slice coordinates. The fixed spatial
mean and its zero velocity restrict it to a ten-dimensional symplectic
subspace. No extra canonical pairs are assigned to the denominator,
monitor, bank or reflection direction.

For two integer tangent pairs at a common denominator D, the same
invariant reads

    Omega=(<delta R1,delta Z2>-<delta Z1,delta R2>)/D^2.

Under the integer step of Section 6 its numerator is multiplied by
m^2, since the terms containing symmetric B cancel, and D^2 is
multiplied by m^2. The quotient is exactly preserved. A claim of an
unchanged integer numerator would be false.

## 5. Prepared amplitudes and the all-counter Lorentz domain

For each of the ten prescribed words set u_t=w_(t+2)-w_t and let
P_t^can have ones at u_t,u_t+1 modulo five. Put h_t^can=P_t^can/2.
The new preparation is explicitly

    h_t=e/5+(h_t^can-e/5)/4 for t=0,1,
    chi_0=0, chi_1=A_src=a/4.                         (5.1)

An occupied site therefore has h=11/40 and an unoccupied site h=6/40.
This is an attenuated preparation of all ten word shapes, not the
unchanged canonical unit-amplitude packet.

### 5.1 Initial energy calculation

For the canonical initial pair write

    Hcan_1=||h_1^can-h_0^can||^2/2
             +<h_0^can,Lh_1^can>/2.

Translation invariance and reflection reduce its values to the
three relative displacements of the occupied adjacent pairs:

    |u_1-u_0|=0: Hcan_1=53/432,
    |u_1-u_0|=1: Hcan_1=713/2592,
    |u_1-u_0|=2: Hcan_1=67/162.                      (5.2)

For example, the diagonal numerator pairing of the two-site vector
with (648I-C) is 318. A one-site displacement gives a kinetic term
1/4 and cross term 65/2592. A two-site displacement gives a kinetic
term 1/2 and cross term -224/2592. These yield (5.2) exactly.
The complete word-to-displacement table is fixed in PREREG.md.

Expand the centered cross term in (3.2), using Kx_*=f:

    Htot_1=||x_1-x_0||^2/2+<x_0,Kx_1>/2
               -<x_0+x_1,f>/2+<x_*,f>/2.

Substituting (5.1) cancels the source kinetic contribution A_src^2/2
against <x_0+x_1,f>/2. The remaining terms are exactly

    Htot_1=Hcan_1/16-(ga/32)<ell,h_0^can>
                          +a^2/[32(1-delta)].        (5.3)

Since |<ell,h_0^can>|<=1/2 and max Hcan_1=67/162,

    Hcan_1/16<=67/2592<13/500,
    |(ga/32)<ell,h_0^can>|<=1/20736<1/20000,
    a^2/[32(1-delta)]<63/2000.

The last strict bound follows, for example, from delta<1/126.
Therefore

    Htot_1<1151/20000<3/50.                          (5.4)

Also Htot_1>0. If a=0, the equilibrium field is e/5 and every prepared
field slice is nonconstant, so the ordered centered pair is nonzero.
If a is nonzero, chi_0=0 differs from chi_* in (2.3), again giving
a nonzero pair. Positive definiteness on V x V now proves strict
positivity. Conservation extends (5.4) to every bond n>=1.

### 5.2 Metric and source bounds for every counter

The explicit equilibrium constants imply for |a|<=1

    ||h_*-e/5||_infinity<1/800,
    |chi_*|<13/50.

For example, the first comparison is
800*40986<4*8683757. Combining (3.8) and (5.4) gives

    |h_n(r)-1/5|<sqrt(24/125)+1/800<9/20,
    |chi_n|<sqrt(6/25)+13/50<3/4.                    (5.5)

The final inequalities use the exact square comparisons

    24/125<(359/800)^2,
    6/25<(49/100)^2.

Hence, for all thirty prepared histories and every n>=0,

    -1/4<h_n(r)<13/20,
    1+h_n(r)>3/4, 1-h_n(r)>7/20,
    g_n(r)=diag(-1,1+h_n(r),1-h_n(r),1),
    det g_n(r)=-(1-h_n(r)^2)<-231/400<0.             (5.6)

This proves signature (-,+,+,+) for the whole prepared family.
It does not assert a uniform interval for the original unattenuated
packet or for every unrestricted carrier state. Constant coupling
does not provide the summable forcing used in the preceding probes;
the invariant energy ellipsoid is the argument here.

## 6. Autonomous integer lift and all thirteen image conditions

Let the unrestricted core be

    x=(Z,R,D,H), Z,R in Z^6, D>=1, H in Z^8,

where Z=(P,Y) and R=(Q,Vscalar) with P,Q five-vectors. Its physical
current and previous slices share the same current denominator:

    (h,chi)=Z/D, (hprev,chiprev)=R/D.

There are 6+6+1+8=21 integer core coordinates. For a fixed a define

    Z'=BZ-mR+81aD e_6,
    R'=mZ, D'=mD,
    H'=M(Y'-Y)H M(Y'-Y)^dagger.                      (6.1)

Dividing the first equation by mD gives (1.1), since
81aD/(mD)=a/4. Dividing R' by D' gives exactly the old current slice.
All coefficients in (6.1) are constant. D is an arithmetic denominator
coordinate; no step index is supplied to either equation. This does
not turn D into a demonstrated native-U or physical clock.

For a candidate image (Z',R',D',H'), any predecessor is forced to have

    D=D'/m, Z=R'/m,
    R=(BZ+81aD e_6-Z')/m.                            (6.2)

These quantities are integral exactly when D' is divisible by m,
all six entries of R' are divisible by m, and all six entries of
BZ+81aD e_6-Z' are divisible by m. Positivity of D' implies D>=1
once its divisibility holds. The monitor inverse is then

    H=M(Y-Y')H'M(Y-Y')^dagger.

Thus the thirteen scalar congruences are necessary and sufficient,
and T is a total injection with this exact partial inverse. Adding
one to D' violates its outer divisibility; adding one to an entry
of R' violates that entry's outer divisibility; adding one to an
entry of Z' changes its reconstruction numerator by -1, which is
not divisible by m. This proves every specified corrupted image
has no backward image.

### 6.1 Ring transport and the prepared monitor

Let O=Z[j], 1+j+j^2+j^3+j^4=0, with conjugation j*=j^4, and put

    phi=-j^2-j^3, J=1+j^2,
    phi^2=phi+1, phi^-1=phi-1, J^-1=-j-j^2, Jphi=j,
    A_H=diag(J,phi), B_H(t)=[[1,t],[0,1]].

For c=c0+c1j+c2j^2+c3j^3,

    c*=(c0-c1)-c1j+(c3-c1)j^2+(c2-c1)j^3.

The fixed ring is Z[phi], so the eight coordinates in PREREG.md
parameterize Herm_2(O). The determinant of A_H has norm one,
and B_H(t) has determinant one. Their congruences preserve both
Hermitian integrality and determinant.

Direct multiplication gives

    M(t)=A_H B_H(t) A_H^-1 B_H(-t)=[[1,t v_J],[0,1]],
    v_J=-2+j-j^2, v_J v_J*=9-5phi.

Consequently M(s)M(t)=M(s+t) and M(t)^-1=M(-t). For D_H=diag(0,1),

    H_Y=M(Y)D_H M(Y)^dagger,
    (H_Y)_8=(9Y^2,-5Y^2,1,0,-2Y,Y,-Y,0),
    det H_Y=0, coeff_j((H_Y)_01)=Y.

The update in (6.1) carries H_Y exactly to H_(Y').
On the unrestricted core H is independent of Y; no monitor relation
is required for invertibility.

The field trace identities Tr(1)=4, Tr(j^t)=-1 for t=1,2,3,4,
and Tr(phi)=2 give

    N(H)=Tr_(Q(j)/Q)(tr(H^2))
        =4a0^2+4a0a1+6a1^2+4d0^2+4d0d1+6d1^2
             +10sum_i c_i^2-2(sum_i c_i)^2.

For each real pair, 4a0^2+4a0a1+6a1^2-2(a0^2+a1^2)
equals 2(a0+a1)^2+2a1^2. For the off-diagonal four-vector,
Cauchy-Schwarz gives (sum c_i)^2<=4sum c_i^2. Hence

    N(H)>=2||H8||^2, and N(H)=0 if and only if H=0,
    N(H_Y)=294Y^4+52Y^2+4.                           (6.3)

The four displayed algebraic factors of M are not four separately
funded dynamical phases; the admitted operation is the combined
macrostep (6.1).

### 6.2 Prepared integer data and mean

At the first core,

    D_1=40, P_1=6e+5P_1^can, Q_1=6e+5P_0^can,
    Y_1=10a, V_1=0, H=H_(10a).

These decode exactly to (5.1). The recurrence gives D_n=40m^(n-1)
for n>=1 and sum P_n=sum Q_n=D_n. The n=0 record with D_0=40
is specified initial data, not a predecessor core of D_1=40.
Indeed, 40 is not divisible by 324.

## 7. Two conserved quantities after domain-and-bank reflection

Define the proper positive integer account

    E(x)=1+D+||Z||^2+||R||^2+N(H).

For a funded state (x,b,epsilon), b>=0 and epsilon in {-1,+1},
attempt y=T^epsilon x. If y exists and b+E(x)-E(y)>=0, move to

    (y,b+E(x)-E(y),epsilon).

Otherwise reflect to (x,b,-epsilon). Rev negates only epsilon.

If a move is admitted, reversing its direction at the output
recovers the old core by the exact inverse, and its proposed bank
is the original b>=0. If a move is refused, the same attempted
direction and same core after conjugation by Rev are again refused.
Thus both cases give

    Rev F Rev F=id.

Since Rev is an involution, this identity supplies both left and
right inverses and proves

    F^-1=Rev F Rev                                  (7.1)

on all 23 integer coordinates. This is a reversible bijection;
F need not itself be an involution.

Every admitted move preserves E+b by definition and Htot by (3.4)
and the exact physical decoding of (6.1). Its admitted inverse
also preserves Htot. A reflection changes no physical slice and
preserves both quantities trivially. Thus

    E+b and Htot are separately conserved by F.       (7.2)

The arithmetical cost and the interaction-inclusive quadratic reading
are not identified. Positive definiteness of Htot remains restricted
to the fixed-mean space, even though conservation holds on the whole
carrier.

### 7.1 Finite shells, horizons and endpoint reflections

On a shell E+b=M, each positive D is bounded by M, both integer
six-vectors have bounded Euclidean norm, H has bounded norm by
(6.3), and b is then fixed by x. Thus the shell is finite.
Along every bare forward edge D is multiplied by m>1; there is
no bare directed cycle. Injectivity makes each connected component
a path. Intersecting it with E<=M retains finite connected paths.

For a path of L vertices, the forward-oriented states traverse
L-1 moving edges, then reflect once at the upper endpoint. The
backward-oriented states traverse L-1 inverse edges, then reflect
once at the lower endpoint. All 2L oriented states are distinct
before this return, so the least funded period is 2L, including
L=1, whose two steps are the two endpoint reflections.

A prepared path begins at D_1=40, which has no predecessor.
For a starting bank b, the bank at any reached core x_n is

    b_n=b+E(x_1)-E(x_n).

Therefore the trajectory reaches x_N if and only if

    b>=Bsharp(N):=max_(1<=n<=N)E(x_n)-E(x_1).          (7.3)

This uses a prefix maximum; no general monotonicity of E is assumed.
Mean conservation and Cauchy-Schwarz give

    E(x_n)>=||P_n||^2>=D_n^2/5=320m^(2(n-1)).         (7.4)

Thus every finite bank has a finite last reached counter Nmax,
which is the largest N satisfying (7.3). Every reached N also
satisfies the exact finite-budget inequality

    320m^(2(N-1))<=E(x_1)+b.                          (7.5)

At Nmax the forward attempt is refused; after returning to x_1 the
missing backward image causes the other endpoint reflection.
The prepared funded orbit has least period 2Nmax.

## 8. Unavoidable joint 3-adic precision growth

All statements in this section concern the six current rational
values (h_n,chi_n), not each component separately. Let d_n be
their least positive common denominator.

For the current core define the integer centered numerator

    zint_n=(5P_n-D_n e,5Y_n),

and define rint_n=(5Q_n-D_n e,5V_n) for the previous slice expressed
at the same denominator. Its field sum is zero exactly. Because
B(e,0)=(2me,0), equation (6.1) gives

    zint_(n+1)=B zint_n-m rint_n+405aD_n e_6,
    rint_(n+1)=m zint_n.                             (8.1)

In particular zint_(n+1)=B zint_n modulo 3. Modulo 3, C has diagonal
1 and every off-diagonal entry 2, so C=-I-E5 where E5 is the
all-ones matrix. On zero-sum field vectors it is -I. Thus B acts
on e^perp x F_3 as

    [[-I,ell],[ell^T,0]].                            (8.2)

If (p,y) lies in its kernel, -p+y ell=0 and <ell,p>=0 imply
p=y ell and 2y=0 in F_3. Hence y=p=0; (8.2) is invertible.

At a prepared unoccupied site, a coordinate of zint_1 is

    5*6-40=-10,

which is nonzero modulo 3. Every prepared word has such a site.
Therefore zint_n is nonzero modulo 3 for every n>=1 and every a.

For n>=2, D_n=40m^(n-1) is divisible by 3. Since 5 is a unit
modulo 3, nonzero zint_n implies at least one of the six current
numerators (P_n,Y_n) is not divisible by 3. Consequently the
greatest common divisor of D_n and all six numerators has
3-adic valuation zero. As v_3(324)=4,

    v_3(d_n)=v_3(D_n)=4(n-1), n>=2.

The n=1 statement follows from v_3(D_1)=v_3(40)=0. Thus

    v_3(d_n)=4(n-1) for every n>=1.                   (8.3)

For any other common integer representation (Pbar,Ybar,Dbar) of
these same six values, the least common denominator d_n divides
Dbar. Hence Dbar>=3^(4(n-1)). Also sum Pbar=Dbar, so

    ||Pbar||^2>=Dbar^2/5,
    ||Pbar||^2+Ybar^2+Dbar^2
       >=(6/5)Dbar^2>=(6/5)3^(8(n-1)).               (8.4)

This is independent of the particular supplied common denominator.
It does not claim that D_n is primitive at 2 or 5, that every
component has the same denominator, or that the field-only
denominator always has valuation (8.3).

In particular the ready joint readings cannot repeat at distinct
positive counters, because their least common denominators have
different 3-adic valuations. Exact arithmetic precision therefore
grows without bound while Htot is constant and the physical
readings remain inside the fixed bounded energy ellipsoid.
Reflection at finite arithmetic budget truncates and retraces
that path; it does not produce the unbounded forward history
from finitely many distinct stored states.

## 9. Exact witnesses, negative controls and selected least periods

The calculations here are direct symbolic consequences of the
definitions, not reports of an execution.

### 9.1 Direct contrast and continuing feedback

For word0010 the first integer field slices are
P_1=(11,11,6,6,6), Q_1=(6,11,11,6,6). Their dipole at n=1 is zero.
The step (6.1) gives

    D_2=12960,
    P_2=(4389,2769,794,2594,2414)+10a ell,
    Y_2=6480a.

Thus the two contexts a=+1 and a=-1 differ in h_2 by ell/648.
Both chi_1 and A_src differ between these contexts.

For word0011 and a=0,

    D_1=40, P_1=Q_1=(6,11,11,6,6), Y_1=V_1=0,
    P_2=(2414,2769,2769,2414,2594), Y_2=-5,
    D_2=12960.

Indeed, CP_1=(4358,6333,6333,4358,4538) and
mQ_1=(1944,3564,3564,1944,1944). Therefore

    chi_2=-1/2592.

At the next step Y_3=m*(-5)+(2414-2769)=-1975 and

    D_3=4199040,
    P_3=(973001,594836,594831,973006,1063366).

The only difference from the free field at this second update is
Y_2 ell=-5ell, giving

    h_3-h_3^free=-ell/839808.

A source retaining only its first feedback impulse has
Y_3^first=m*(-5)=-1620 at D_3. Hence

    chi_3-chi_3^first=-355/4199040=-71/839808.

This distinguishes continued response to the evolved field from a
single initial impulse.

### 9.2 Complete energy transfer

At the first zero-source bond, (5.2) gives

    Htot_1=Hh_1=53/6912, Hchi_1=I_1=0.

Because chi_1=0, the first field update is free and Hh_2=Hh_1.
The source increment and interaction increment are

    Hchi_2-Hchi_1=(1/2)(1/2592)^2=1/13436928,
    I_2-I_1=-(g/2)(-1/2592)(-1/8)=-1/13436928.

They cancel exactly, so Htot_2=Htot_1. The field-only bond energy
does not decrease at this first step.

For completeness, let b0=839808. From the displayed integer values,

    <ell,h_1>=-1/8=-104976/b0,
    <ell,h_2>=-71/2592,
    <ell,h_3>=75633/b0,
    chi_1=0, chi_2=-1/2592, chi_3=-395/b0.

The sector work identities derived as in (3.4) then give

    Hh_3-Hh_2=-180609/(2b0^2),
    Hchi_3-Hchi_2=28045/(2b0^2),
    I_3-I_2=152564/(2b0^2).

Their sum is zero. Both later sector exchange and the interaction
term are included in the same total invariant.

### 9.3 Affine Wronskian control

For ordered words (0010,0011) at a=1, the first source images are

    chi_2^(0010)=1/2,
    chi_2^(0011)=1/2-1/2592.

By (4.6), the raw Wronskian increment from bond 2 to bond 3 is

    (a/4)(chi_2^(0010)-chi_2^(0011))=1/10368.

Its nonconservation is expected. Centering both histories by the
same equilibrium restores the invariant in (4.5).

### 9.4 The seven named comparison laws

For word0011,a=0, suppressing field-to-source feedback leaves chi=0,
but the main source gradient at n=1 is g<ell,h_1>=-1/2592.
Keeping only the first feedback gives the nonzero contrast in 9.1.
Suppressing source-to-field coupling while retaining feedback
leaves the field free, and its main gradient at n=2 is
g chi_2 ell=-ell/839808. Reversing the feedback sign makes
chi_2=+1/2592; its main source gradient at n=1 is then -1/1296.

Omitting the Hermitian transport leaves its prepared coefficient
zero at the first image although Y_2=-5. Omitting I from the
total energy leaves the positive increment 1/13436928 in 9.2.
Finally, the unrestricted core with D=1,P=(1,0,0,0,0),Y=0 reads
g(site0)=diag(-1,2,0,1), with zero determinant. These controls
locate failures outside the respective declared laws or prepared
metric domain; none changes the main definition.

### 9.5 Sharp first bank and the six selected least periods

For word0011,a=0,

    N(H_-5)=294*625+52*25+4=185054,
    ||P_2||^2=33718350, ||Z_2||^2=33718375,
    ||R_2||^2=m^2*350=36741600,
    E(x_1)=745, E(x_2)=70657990.

Therefore Bsharp(2)=70657245. Bank 70657244 cannot admit the
first step. Bank 70657245 admits it with residual bank zero.

For the same word and arbitrary a in {-1,0,1}, direct algebra gives

    Y_1=10a, Y_2=6480a-5, Y_3=2099540a-1975,
    P_2=(2414,2769,2769,2414,2594)+10a ell,
    E(x_1)=745+2945300a^2.                           (9.1)

For a=0, E(x_2)>E(x_1) by the exact values above, and
|Y_3|=1975>1000 implies
E(x_3)>294*1000^4>E(x_2).

For a=+1 or -1,

    E(x_1)<3000000,
    6475<=|Y_2|<=6485,
    2097565<=|Y_3|<=2101515.

Thus E(x_2)>294*6000^4>E(x_1). An elementary upper bound also
suffices: every component of P_2 has magnitude less than 3000,
|Y_2|<6500, ||R_2||^2=m^2*450, and D_2=12960. Consequently

    E(x_2)
      <1+12960+5*3000^2+6500^2+m^2*450
         +294*6500^4+52*6500^2+4
      <10^18.

On the other hand E(x_3)>294*(2000000)^4>10^18.
This proves E(x_1)<E(x_2)<E(x_3) for all three selected contexts
without asserting later monotonicity.

For target N=1, zero bank refuses the next forward edge and the
lower inverse domain is absent, giving the two-reflection period 2.
For N=2, bank E(x_2)-E(x_1) admits exactly x_1 to x_2, reflects
at x_2 because E(x_3)>E(x_2), returns to x_1, and reflects there
because 40 is not divisible by m. The least period is 4.
In the prescribed order a=-1,0,1 and N=1,2, the six periods are

    2,4,2,4,2,4.

The general horizon theorem is (7.3); these selected inequalities
are only the finite barriers used for this particular cycle gate.

## 10. Scope of the completed mathematical construction

The constant action, equilibrium, conserved total bond quantity and
canonical map describe one selected linear TT-plus-scalar model.
The integer lift is autonomous in its displayed state variables.
Its arithmetic precision account is proper and gives a reversible
finite-budget traversal, while the representation-independent
3-adic theorem requires unbounded precision for the unbounded
ready forward history.

The mathematical comparison energy remains distinct from the
positive integer admission account. The canonical alternating form
belongs to the bare physical map, with the explicit affine-centering
condition. Positivity and the all-counter Lorentz interval are
restricted to the stated fixed-mean and attenuated prepared spaces.
No conclusion here supplies a native source law, a physical time
calibration, nonlinear 3+1 gravitational dynamics, a unique matter
coupling, optimal primitive denominators at all primes, or a
continuum manifold limit.
