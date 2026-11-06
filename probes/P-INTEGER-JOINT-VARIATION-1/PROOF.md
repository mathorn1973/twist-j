# Proofs for P-INTEGER-JOINT-VARIATION-1

Scope: NON-CANONICAL, L1.  
Ownership: https://github.com/mathorn1973/twist-j/issues/1645.

This document proves the selected equations, their exact integer storage,
the unrestricted inverse and funded extension, the Hermitian realization,
simultaneous first-order stationarity of the metric and source, and the
all-counter bounds and exact witnesses stated in PREREG.md. All added
state coordinates, the common scale, the source equation, the interaction,
and the admission account are NEW_DECLARED L1 choices.

The public reference is Public Canon v103 at main and peeled canon-v103
commit dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d, content commit
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66. The canonical construction
DEF-K1-LINEAR-METRIC supplies the unforced five-site recurrence and the
full quadratic metric action. K1-LINEAR-METRIC-COMPLETION supplies the
quantitative unforced bound used in Section 6. SOURCE.md identifies the
actual normative bytes. The new results below do not change their status.

The time counter remains discrete. The real comparison variables in the
action are virtual variables; the exact stationary solution is represented
by integers. No continuum manifold, full nonlinear Einstein equation,
native-U implementation, minimum encoding cost, or positive physical
matter Hamiltonian is asserted.

## 1. Cyclotomic arithmetic, transport, and source realization

Let O=Z[j] with 1+j+j^2+j^3+j^4=0, and let conjugation map j to j^4.
Set phi=-j^2-j^3 and J=1+j^2. Reduction by the defining polynomial gives

    phi^2=phi+1, phi^(-1)=phi-1,
    J^(-1)=-j-j^2, J*phi=j.

Consequently A=diag(J,phi) and its inverse both have entries in O.
B(t)=[[1,t],[0,1]] has inverse B(-t) for every integer t.

### 1.1 Hermitian closure and determinant preservation

For c=c0+c1*j+c2*j^2+c3*j^3, conjugation in this integer basis is

    conjugate(c)=(c0-c1)-c1*j+(c3-c1)*j^2+(c2-c1)*j^3.

Its fixed elements have c1=0 and c2=c3, hence are exactly Z[phi]. Thus
the eight coordinates in PREREG.md describe all of Herm_2(O). Congruence
by any of A, A^(-1), B(t), or their products preserves this module.

For any two-by-two matrix G over O,

    det(G*H*G^dagger)=det(G)*conjugate(det(G))*det(H).

The determinant factor is one for B(t), and for A it is
(J*phi)*conjugate(J*phi)=j*conjugate(j)=1. Therefore every declared
transport preserves det(H), on arbitrary Hermitian inputs, with no
positive-matrix restriction.

### 1.2 The commutator is an additive unipotent group

Direct multiplication gives

    M(t)=A*B(t)*A^(-1)*B(-t)
        =[[1,t*(J/phi-1)],[0,1]]=[[1,t*v],[0,1]],
    v=-2+j-j^2,
    v*conjugate(v)=9+5*j^2+5*j^3=9-5*phi=:w.

Thus M(t) lies in SL_2(O), M(s)*M(t)=M(s+t), and M(t)^(-1)=M(-t).
The four A/B factors and the single displayed M(t) are exactly the same
matrix. The core update charges the combined macro-step; this identity
does not insert additional bank admissions between those factors.

For D_H=diag(0,1), define the ready source matrix

    H_Y=M(Y)*D_H*M(Y)^dagger
       =[[Y^2*w,Y*v],[Y*conjugate(v),1]].                 (1.1)

Its coordinates and source reading are

    (H_Y)8=(9*Y^2,-5*Y^2,1,0,-2*Y,Y,-Y,0),
    coeff_j((H_Y)_01)=Y.                                (1.2)

The rank-one source determinant is zero. If the integer source changes
from Y to Y', then

    M(Y'-Y)*H_Y*M(Y'-Y)^dagger=H_(Y')                    (1.3)

by the additive group law. This proves exact preservation of the ready
Hermitian realization. On the unrestricted carrier, H need not equal H_Y:
the field equation is coupled to Y, and H is a separately invertible
realization/monitor. No independent equation for eight unrestricted
Hermitian matter variables is inferred from this scalar action.

### 1.3 Positive integer cost and exact trace formula

Write the diagonal entries as alpha=a0+a1*phi and delta=d0+d1*phi.
For K=Q(j), Tr_(K/Q)(1)=4, Tr_(K/Q)(j^t)=-1 for t=1,2,3,4, and
Tr_(K/Q)(phi)=2. Since phi^2=phi+1,

    Tr_(K/Q)(alpha^2)=4*a0^2+4*a0*a1+6*a1^2,

with the analogous formula for delta. For the off-diagonal entry c,

    Tr_(K/Q)(c*conjugate(c))
      =4*sum_i c_i^2-sum_(i!=j) c_i*c_j
      =5*sum_i c_i^2-(sum_i c_i)^2.

Since tr(H^2)=alpha^2+delta^2+2*c*conjugate(c), this proves exactly

    N(H)=Tr_(K/Q)(tr(H^2))
      =4*a0^2+4*a0*a1+6*a1^2+4*d0^2+4*d0*d1+6*d1^2
       +10*sum_i c_i^2-2*(sum_i c_i)^2.                 (1.4)

The diagonal contribution minus 2*(a0^2+a1^2) is
2*(a0+a1)^2+2*a1^2>=0. The same holds for d0,d1. Cauchy-Schwarz gives
(sum_i c_i)^2<=4*sum_i c_i^2, so the off-diagonal contribution is at
least 2*sum_i c_i^2. Hence

    N(H)>=2*||H8||_2^2,

and N(H)=0 only when H=0. On the ready source family (1.2), substitution
gives

    N(H_Y)=294*Y^4+52*Y^2+4.                             (1.5)

In particular N(D_H)=4. This is a positive arithmetic cost, regardless of
whether the matrix H is positive or indefinite.

## 2. Exact integer storage and unrestricted partial inverse

Let m=324, ell=(1,-1,0,0,0), and let C be the symmetric circulant matrix
with first row (460,29,65,65,29). Put L=2*I-C/m. The fixed source context
is a in {-1,0,1}. The selected equations are, for n>=1,

    (Delta_c^2+L)h_n=chi_n*ell/m^n,
    (Delta_c^2+1)chi_n=a-<ell,h_n>/m^n,                 (2.1)

where Delta_c^2 f_n=f_(n+1)-2*f_n+f_(n-1).

### 2.1 Common scale and both exact recurrences

Define

    D_n=2*m^(n*(n-1)/2), n>=0.

Then D_0=D_1=2 and, for all n>=1,

    D_(n+1)/D_n=m^n,
    D_(n+1)/D_(n-1)=r_n=m^(2*n-1).                     (2.2)

In particular r_1=m, not m^2. Multiplying (2.1) by D_(n+1) and putting
P_n=D_n*h_n, Y_n=D_n*chi_n yields

    P_(n+1)=m^(n-1)*C*P_n-r_n*P_(n-1)+Y_n*ell,
    Y_(n+1)=m^n*Y_n-r_n*Y_(n-1)+a*D_(n+1)-<ell,P_n>.   (2.3)

The canonical P_0,P_1 are integer two-site vectors, and Y_0=0,Y_1=2*a.
Every coefficient in (2.3) is an integer. Induction gives integer storage
at all counters; conversely division by D_(n+1) gives (2.1) without an
approximation. In particular the reciprocal source term is retained
exactly, rather than removed by a lattice threshold or parity operation.

The scale is sufficient for this representation. It is not asserted to
be a least denominator. The earlier denominator 2*m^(n-1), its primitive
valuation theorem, and its universal encoding-cost interpretation are
not inherited by this new coupled law.

### 2.2 Full carrier and necessary-and-sufficient image condition

The unrestricted core is

    x=(P,W,Y,V,H,k) in Z^5 x Z^5 x Z x Z x Herm_2(O) x Z_(>=1).

This has 21 integer coordinates. Here V is a previous source numerator,
not a metric component. With r_k as in (2.2), define

    P'=m^(k-1)*C*P-r_k*W+Y*ell,
    Y'=m^k*Y-r_k*V+a*D_(k+1)-<ell,P>,
    W'=P, V'=Y, k'=k+1,
    H'=M(Y'-Y)*H*M(Y'-Y)^dagger.                        (2.4)

All right-hand sides use the old state. Ring closure makes (2.4) total on
the unrestricted core, and it increases k by exactly one.

For an output candidate x' with k'>=2, put n=k'-1. Its only possible
predecessor has P=W', Y=V', k=n and

    W=[m^(n-1)*C*W'+V'*ell-P']/r_n,
    V=[m^n*V'+a*D_(n+1)-<ell,W'>-Y']/r_n,
    H=M(V'-Y')*H'*M(V'-Y')^dagger.                      (2.5)

The predecessor exists precisely when all five entries of the first
numerator and the scalar second numerator are divisible by r_n. When
they are divisible, (2.5) is an integer core and substitution in (2.4)
recovers x'. When one divisibility fails, no integer predecessor can
exist because P,Y,k are already forced by W',V',k'. At k'=1 no predecessor
exists. The H inverse is always available and adds no extra guard.

Thus T defined by (2.4) is a total injection, and (2.5) is its exact
partial inverse on its exact image. No mean, denominator, readiness,
positive-matrix, or metric-signature condition was used in this proof.

Corrupting one current P' entry of a valid image by +1 changes one inverse
numerator by -1; corrupting Y' by +1 changes the scalar numerator by -1.
Since r_n>=324, each of these six individual corruptions necessarily
leaves the image. This justifies the 684 image-defect fixtures directly.

### 2.3 Ready Hermitian reader and mean conservation

The ready core at k=1 is P=P_1,W=P_0,Y=2*a,V=0,H=H_(2a).
The supplied n=0 boundary has Y_0=0 and H_0=D_H. Equations (1.3) and
(2.4) prove H_n=H_(Y_n) for every ready counter. Thus

    coeff_j((H_n)_01)/D_n=Y_n/D_n=chi_n

independently of the scalar decoder used to advance (2.3).

Because C*e=648*e=2*m*e and <e,ell>=0, taking the coordinate sum of the
first equation in (2.1) gives

    sum h_(n+1)-2*sum h_n+sum h_(n-1)=0.

Both initial sums are one. Hence sum h_n=1 and sum P_n=D_n at all n>=0.
This also shows that every field difference from the canonical unforced
history belongs to the zero-sum subspace used below.

## 3. Funded bijection, finite shells, and sharp horizons

Define the positive integer account

    E(x)=1+k+||P||_2^2+||W||_2^2+Y^2+V^2+N(H).

It is proper: E<=M bounds k, all twelve scalar/vector integer coordinates,
and the eight Hermitian coordinates by (1.4). Thus each sublevel is finite.
The bank b>=0 and direction epsilon in {-1,+1} give 23 integer funded
coordinates. The parameter a remains a fixed context key.

### 3.1 Total reversibility including both rejection mechanisms

For direction epsilon, attempt y=T^epsilon x, where T^-1 is the exact
partial inverse. If the domain is absent or c=b+E(x)-E(y)<0, let

    F(x,b,epsilon)=(x,b,-epsilon).

Otherwise let F(x,b,epsilon)=(y,c,epsilon). This rule is total and
preserves E+b. Let Rev reverse only epsilon.

If a move is admitted, the reverse edge exists by Section 2 and its bank
is c+E(y)-E(x)=b>=0. Therefore Rev*F*Rev undoes that move. If the attempt
is rejected, the output is Rev(x,b,epsilon); applying Rev before F returns
to the same rejected attempt, and the final Rev recovers the input. Thus

    Rev*F*Rev*F=identity.

Conjugating this identity by Rev also gives F*Rev*F*Rev=identity. Hence

    F^(-1)=Rev*F*Rev                                    (3.1)

on the entire unrestricted funded carrier. This handles the k=1 boundary,
inverse-image failures, and insufficient banks, not only ready trajectories.

### 3.2 Exact periods and reachability by prefix maxima

On a fixed shell E+b=M the bank at each core is uniquely M-E(x), and the
shell is finite. Bare edges cannot form a cycle because k increases under
T. Injection gives at most one incoming and one outgoing bare edge.
Retaining vertices with E<=M therefore cuts each bare component into
finite paths. On a path of L vertices, F visits every vertex in the
positive direction, reflects at the upper endpoint, visits every vertex
in the negative direction, and reflects at the lower endpoint. These
are exactly its 2*L distinct funded states. Its least period is 2*L;
for a one-vertex path the two direction states exchange, giving period 2.

For a ready history x_1,x_2,... define

    B_sharp(N)=max_(1<=n<=N)E(x_n)-E(x_1).

The prefix through N is admitted exactly when b>=B_sharp(N). Necessity
follows because each visited bank is E(x_1)+b-E(x_n)>=0; sufficiency
follows by the same formula along all preceding edges. No monotonicity of
the individual E(x_n) is assumed.

By mean conservation and Cauchy-Schwarz,

    E(x_n)>=||P_n||_2^2 >= (sum P_n)^2/5
             =D_n^2/5=(4/5)*m^(n*(n-1)).                (3.2)

Thus every finite bank has a last admitted ready counter N. Since the
ready history starts at the k=1 boundary, the entire reachable core path
is x_1,...,x_N, and its least funded period is 2*N. Every reachable n
necessarily satisfies

    4*m^(n*(n-1))<=5*(E(x_1)+b).

Equation (3.2) concerns the specified stored numerators. It is not a lower
bound for every exact encoding, because D_n is not asserted primitive.

For illustration that decreasing account moves are genuinely included,
the extra fixture in PREREG.md has P=m*e_2,W=C*e_2,Y=V=a=0,H=D_H,k=1.
Its next P and Y are zero, and H stays D_H. Since
||C*e_2||^2=2*65^2+2*29^2+460^2=221732, its account change is
1-221732=-221731<0. Formula (3.1) includes such moves without alteration.

## 4. Full joint action and both continuous Euler-Lagrange equations

Write Vmetric for the real symmetric spatial comparison perturbation,
as in PREREG.md, and V for the previous integer source numerator. Let
ell_0 be the lapse perturbation and N_i the shifts. Only spatial direction
3 has a nonzero derivative. The canonical D_sp is real and satisfies

    D_sp^T=-D_sp, D_sp^T*D_sp=-D_sp^2=L.

Keep all six independent entries of Vmetric, the lapse and all three shifts
until after variation. The canonical definitions are

    K11=Delta Vmetric11/2, K22=Delta Vmetric22/2,
    K12=Delta Vmetric12/2,
    K13=(Delta Vmetric13-D_sp N1)/2,
    K23=(Delta Vmetric23-D_sp N2)/2,
    K33=(Delta Vmetric33-2*D_sp N3)/2, K=Tr(Kij),

    G2(Vmetric)=1/2 <D_sp Vmetric3j,D_sp Vmetric3j>
          -1/2 <D_sp Vmetric33,D_sp Tr Vmetric>
          +1/4 <D_sp Tr Vmetric,D_sp Tr Vmetric>
          -1/4 <D_sp Vmetricij,D_sp Vmetricij>,
    R1(Vmetric)=D_sp^2 Vmetric33-D_sp^2 Tr Vmetric,
    A2=sum_n {<Kij,Kij>-<K,K>+G2(Vmetric)
              +<ell_0,R1(Vmetric)>}.                   (4.1)

Repeated spatial indices range over 1,2,3; off-diagonal entries therefore
occur twice in an ij sum. Delta f_n=f_(n+1)-f_n. K and the shifts have
the canonical half-slice placement; Vmetric and the lapse lie on integer
slices.

### 4.1 Boundary convention and independent source variation

Define

    A_joint[Vmetric,ell_0,N,chi]
      =A2[Vmetric,ell_0,N]
       +(1/2)*sum_(n>=1) chi_n/m^n*<ell,Vmetric11_n-Vmetric22_n>
       -(1/2)*sum_(n>=0)(chi_(n+1)-chi_n)^2
       +sum_(n>=1)[chi_n^2/2-a*chi_n].                  (4.2)

Variations have finite support in n>=1 and fix the n=0 boundary, including
h_0 and chi_0. The prescribed h_1 and chi_1=a select the initial-value
solution of the resulting equations; they are not frozen against virtual
variations used to derive the equations at n=1. The coefficient a is
external fixed context, not a functional of a metric boundary value.
Consequently no unvaried hidden boundary coupling is used in (4.2).
The sums define finite action changes and local first variations, not a
claim that the infinite numerical action converges.

First vary all metric, lapse, shift, and source components independently;
then evaluate at

    Vmetric_n=diag(h_n,-h_n,0), ell_0=0, N_i=0.          (4.3)

At (4.3), K11=-K22=Delta h/2, all other Kij vanish, and K=0. Thus
the kinetic first variation is

    (1/2)*sum_n
      <Delta h_n,Delta(delta Vmetric11_n-delta Vmetric22_n)>.

Finite-support summation by parts gives its value
-(1/2)*sum_n <Delta_c^2 h_n,delta Vmetric11_n-delta Vmetric22_n>.
The first three terms of G2 have zero first variation because Vmetric3j
and Tr Vmetric vanish at (4.3). Its last term contributes

    -(1/2)*sum_n <L*h_n,delta Vmetric11_n-delta Vmetric22_n>.

All off-diagonal, longitudinal and trace directions therefore have zero
gradient at this representative. Shift variations pair only with the
vanishing K13,K23,K33,K. Lapse variation gives R1(Vmetric)=0, while the
metric variation of its product with ell_0 also vanishes at ell_0=0.
These are full component variations, not assumptions imposed before
varying the action.

The interaction adds

    (1/2)*sum_n <chi_n*ell/m^n,delta Vmetric11_n-delta Vmetric22_n>
      +sum_n <ell,h_n>/m^n*delta chi_n.

For a source coordinate chi_n, the two adjacent negative kinetic terms
contribute chi_(n+1)-2*chi_n+chi_(n-1). The +chi_n^2/2 term contributes
+chi_n and the -a*chi_n term contributes -a. Combining all terms gives

    delta A_joint
      =-(1/2)*sum_(n>=1)
        <(Delta_c^2+L)h_n-chi_n*ell/m^n,
          delta Vmetric11_n-delta Vmetric22_n>
       +sum_(n>=1)
        [(Delta_c^2+1)chi_n-a+<ell,h_n>/m^n]*delta chi_n.  (4.4)

The positive sign in front of (Delta_c^2+1)chi_n is fixed by this
calculation. Each coefficient in (4.4) vanishes exactly on (2.1).
Conversely, independent finite-support variations force both equations
(2.1). This proves simultaneous continuous first-order stationarity of
the full metric and scalar source at the TT representative. No source
derivative is replaced by an integer-coordinate maximum, and no adjoint
multiplier is introduced.

### 4.2 Kinetic sign and exact off-shell derivatives

Restricting (4.2) to (4.3) after the calculation gives

    A_TT=(1/2)*sum ||Delta h_n||^2-(1/2)*sum <h_n,L*h_n>
         +sum chi_n/m^n*<ell,h_n>
         -(1/2)*sum(Delta chi_n)^2
         +sum[chi_n^2/2-a*chi_n].                        (4.5)

The source kinetic term has the opposite sign from the TT metric kinetic
term. This is an indefinite quadratic variational model; a positive
physical matter Hamiltonian or stable quantum matter is not established.
It is nevertheless the exact sign giving the second equation in (2.1).

The current-pair matrix in the integer recurrence is

    A_n=[[m^(n-1)*C,ell],[-ell^T,m^n]].

With the kinetic-sign matrix G=diag(I_5,-1), G*A_n is symmetric. Thus
the opposite off-diagonal signs of the recurrence agree with the
symmetric mixed derivatives of the action and its kinetic signature.

At a fixed interior counter with neighbors held fixed, the local
polynomial is

    A_local(v,xi)
      =(||v-hprev||^2+||hnext-v||^2)/2-<v,L*v>/2
       -[(xi-chiprev)^2+(chinext-xi)^2]/2
       +xi^2/2-a*xi+xi*<ell,v>/m^n.                     (4.6)

For arbitrary real comparison values, not only for solutions,

    grad_v A_local=2*v-hprev-hnext-L*v+xi*ell/m^n,
    d_xi A_local=chinext-xi+chiprev-a+<ell,v>/m^n.        (4.7)

The two mixed derivatives are both ell/m^n. In particular changing xi
by +1 changes the source derivative by -1, changing chinext by +1
changes it by +1, and changing chiprev by -1 changes it by -1. These
signs are available even away from a trajectory where an oscillator
residual happens to vanish. Since (4.6) is quadratic, every central
unit difference is exactly the corresponding derivative (4.7), with
no limiting or floating-point argument.

The executable count of 720 stationary differences in PREREG.md concerns
the five reduced TT coordinates and one scalar source coordinate. The
additional full metric, lapse and shift directions are covered by (4.4).
The six specified off-shell cases check 36 derivatives of (4.6)-(4.7);
their comparison does not replace the full analytical variation.

## 5. Correct spatial spectrum and retarded Green bounds

Let S be the five-site cyclic shift. Then

    C=460*I+29*(S+S^(-1))+65*(S^2+S^(-2)).

On the constant mode, C has eigenvalue 648 and L has eigenvalue zero.
For the Fourier pair with angle 2*pi/5, use
cos(2*pi/5)=(sqrt(5)-1)/4 and
cos(4*pi/5)=-(sqrt(5)+1)/4. The C eigenvalue is

    460+58*cos(2*pi/5)+130*cos(4*pi/5)=413-18*sqrt(5).

The other pair interchanges these two cosines, giving 413+18*sqrt(5).
Thus the nonzero spectrum of L is exactly

    lambda_+=(235+18*sqrt(5))/324,
    lambda_-=(235-18*sqrt(5))/324,                        (5.1)

each with multiplicity two. Both eigenvalues are strictly between 1/2
and 1, as follows already from sqrt(5)<5/2.

For a field eigenmode, put cos(omega)=1-lambda/2. The retarded Green
kernel for Delta_c^2+lambda is

    G_lambda(t)=sin(t*omega)/sin(omega), t>=1,

with G_lambda(0)=0 and G_lambda(1)=1. It follows directly from the
homogeneous second-order recurrence and those two initial values.
Since

    sin(omega)^2=lambda-lambda^2/4>3/8,

the zero-sum field Green operator satisfies

    ||G_h(t)||_(2->2)<sqrt(8/3),
    ||G_h(t)*ell||_2<sqrt(16/3)<5/2.                    (5.2)

Only this zero-sum restriction is used: the constant mode would have a
different growing Green kernel, and the source dipole has zero sum.

For the scalar source operator Delta_c^2+1, its retarded kernel has
G_chi(0)=0,G_chi(1)=1 and recurrence

    G_chi(t+1)=G_chi(t)-G_chi(t-1).

It is exactly the periodic sequence

    0,1,1,0,-1,-1,0,1,1,...,

so |G_chi(t)|<=1. This exact discrete bound is stronger than the generic
bound 1/sin(pi/3); it is used in the rational constants below.

## 6. Simultaneous causal bounds and the Lorentz domain

Let h^free be the canonical unforced K1 history for the same word and
initial slices. The imported K1-LINEAR-METRIC-COMPLETION bound is

    -59/100<h_n^free(r)<99/100                            (6.1)

for every counter and site of all ten words. Let chi^0 solve the source
equation with feedback disabled and the same initial source data:

    chi_0^0=0,
    chi_n^0=a*(1,2,2,1,0,0)_n, n>=1.                   (6.2)

Substitution in chi_(n+1)^0-chi_n^0+chi_(n-1)^0=a verifies (6.2).
In particular |chi_n^0|<=2 and |chi_1|=|a|<=1.

The differences delta h=h-h^free and delta chi=chi-chi^0 both vanish at
n=0,1. The exact causal representations following from their recurrences
are

    delta h_n=sum_(t=1)^(n-1) G_h(n-t)*ell*chi_t/m^t,
    delta chi_n=-sum_(t=1)^(n-1) G_chi(n-t)*<ell,h_t>/m^t. (6.3)

They use only counters t<n. We prove simultaneously by induction that

    |delta chi_n|<2/323,
    |chi_n|<648/323<3,
    ||delta h_n||_infty<1630/209304<1/125.               (6.4)

The bounds hold at counters 0 and 1. Suppose they hold at every earlier
counter. By (6.1), the earlier metric values lie in

    -299/500<h_t(r)<499/500,

because their difference from the free history is less than 1/125.
Therefore |<ell,h_t>|<798/500<2. The scalar part of (6.3) gives

    |delta chi_n|
      <=sum_(t=1)^(n-1)|<ell,h_t>|/m^t
      <2*sum_(t>=1)m^(-t)=2/(m-1)=2/323.

Together with |chi_n^0|<=2 this yields
|chi_n|<2+2/323=648/323<3. The field part of (6.3), (5.2), and the
earlier bounds |chi_1|<=1 and |chi_t|<3 for t>=2 give

    ||delta h_n||_infty<=||delta h_n||_2
      <(5/2)*[1/m+3*sum_(t>=2)m^(-t)]
      =(5/2)*[1/m+3/(m*(m-1))]
      =1630/209304<1/125.                               (6.5)

The final strict comparison is 1630*125=203750<209304. This closes the
induction. No bound on an unknown infinite future is assumed: each new
counter follows from (6.3) and already bounded earlier counters.

Applying (6.1) and (6.5) proves for all thirty ready histories and n>=0

    -299/500<h_n(r)<499/500,
    1+h_n(r)>201/500,
    1-h_n(r)>1/500,
    det g_n(r)=-(1-h_n(r)^2)<-999/250000<0.               (6.6)

Thus g_n(r)=diag(-1,1+h_n(r),1-h_n(r),1) has Lorentz signature
(-,+,+,+) throughout every ready history and every retraced prefix.
This is a theorem on the declared reading family. On the unrestricted
core P=(2,0,0,0,0),k=1, the first h value equals 1 and the metric has
diagonal (-1,2,0,1), so extending (6.6) to the full carrier is false.

## 7. Exact direct, reciprocal, and continued-feedback witnesses

### 7.1 Direct source contrast at word 0010

Here P_0=(0,1,1,0,0), P_1=(1,1,0,0,0), and <ell,P_1>=0. At n=1,

    C*P_1-m*P_0=(489,165,-230,130,94),
    P_2=C*P_1-m*P_0+2*a*ell,
    Y_2=m*(2*a)+a*(2*m)=4*m*a.

Therefore

    P_2(-)=(487,167,-230,130,94), Y_2(-)=-1296,
    P_2(+)=(491,163,-230,130,94), Y_2(+)=1296.

Since D_2=648, the metric contrast is

    h_2(+)-h_2(-)=4*ell/648=ell/162.                    (7.1)

This compares the selected fixed contexts a=-1 and a=+1, each of which
also sets chi_1=a. The initial field slices and comparison counter are
identical.

### 7.2 A zero-seed source responds to the evolved field

At word 0011, P_0=P_1=(0,1,1,0,0) and a=0. Thus Y_0=Y_1=0,
<ell,P_1>=-1, and the first coupled step gives

    P_2=(94,165,165,94,130),
    Y_2=1,
    D_2=648,
    chi_2=1/648.                                       (7.2)

The next field update uses

    C*P_2=(68630,97971,97971,68630,86702),
    P_3=m*C*P_2-m^3*P_1+ell,

so exactly

    P_3=(22236121,-2269621,-2269620,22236120,28091448),
    D_3=2*m^3=68024448.                                 (7.3)

With field-to-source feedback disabled, the zero source stays zero and
the field remains the free K1 field. At n=3 its scaled field numerator
is (7.3) minus ell. Hence

    h_3-h_3^free=ell/68024448.                           (7.4)

This change comes from the source amplitude produced by the preceding
field. It does not require a nonzero initial source seed.

The feedback is also active after its first step. Since
<ell,P_2>=94-165=-71, the full source update gives

    Y_3=m^2*Y_2-<ell,P_2>=104976+71=105047.

A control retaining the feedback only at n=1 instead has Y_3=m^2=104976,
and therefore chi_3=1/648. The exact continued-feedback contrast is

    chi_3^joint-chi_3^first-only=71/68024448.             (7.5)

The additional 71 uses the evolved field h_2, whose marked dipole is
-71/648. Thus (7.5) distinguishes continued feedback from an initial-only
source preparation.

### 7.3 Exact first budget and the nine specified least periods

For the zero-seed word0011 preparation, N(H_0)=N(H_1)=4 and E(x_1)=10.
At k=2, (7.2) and (1.5) give

    ||P_2||^2=2*94^2+2*165^2+130^2=89022,
    N(H_(Y_2))=294+52+4=350,
    E(x_2)=1+2+89022+2+1+0+350=89378.

The sharp first-step bank is 89378-10=89368. It reaches k=2 with zero
bank. Its successor has larger account, as also established below, so
the admitted path has two vertices and least period four. Bank 89367
rejects the first step. Neither budget is claimed to reach the bare
counter-three witness (7.3).

For completeness, the peak comparisons needed for all nine cycle
fixtures follow analytically from the ready bounds and a few integers.
For any ready n=1,2,3, (6.6) gives |P_r|<D_n, and (6.4) gives
|Y_n|<3*D_n, with the same bounds for previous coordinates and
D_(n-1)<=D_n. Using (1.5),

    E(x_n)<23814*D_n^4+496*D_n^2+n+5<24000*D_n^4.        (7.6)

The last inequality uses D_n>=2 and n+5<=8. For a=-1,+1 at word0010,
the free source values at counters 2,3,4 have absolute values 2,2,1.
The deviation bound |chi-chi^0|<2/323 thus makes each of these source
values larger than 1/2 in absolute value. Consequently for n=1,2,3,

    E(x_(n+1))>294*D_(n+1)^4/16
       =(294/16)*m^(4*n)*D_n^4>24000*D_n^4>E(x_n).      (7.7)

The displayed constant comparison follows, for example, from
294*m^(4*n)>=294*m^2=30862944>384000=16*24000.

For word0011,a=0, E(x_2)>E(x_1) was computed above, while
E(x_3)>=294*105047^4>294*(10^5)^4>E(x_2). From (7.3),
<ell,P_3>=24505742. Thus

    Y_4=m^3*(m^2+71)-m^5-24505742
       =71*m^3-24505742=2390362162>2*10^9.

Since D_3=68024448<10^8, (7.6) gives

    E(x_4)>294*(2*10^9)^4
          >24000*(10^8)^4>E(x_3).

For each of the three specified seeds the accounts therefore increase
through counter four. In each case and for N=1,2,3, the preregistered
bank E(x_N)-E(x_1) admits precisely the first N counters and rejects the
next. Section 3 proves the exact least period 2*N, giving in the stated
seed/target order

    2,4,6,2,4,6,2,4,6.

### 7.4 Meaning and exact values of the negative controls

These controls are distinct comparison contexts, not changes to the
main law after observation.

At word0011,a=0, the initial dipole is <ell,h_1>=-1/2. If feedback to the
source is disabled, chi stays zero and h remains free, but the source
gradient of the main joint action at n=1 is -1/(2*m)=-1/648. If the
feedback sign is reversed, the source oscillator residual itself is
-1/(2*m), so adding the main interaction gradient gives -1/m=-1/324.
These are exact failures of continuous stationarity, not small tolerated
residuals.

If source-to-field coupling is disabled while feedback is retained, the
field stays free and chi_2=1/648. Its main-action metric gradient at n=2
is therefore +ell/(648*m^2)=ell/68024448. The first-only-feedback contrast
is exactly (7.5).

Omitting the Hermitian update at the first zero-seed step leaves H=D_H,
so its coefficient of j is zero whereas Y_2=1. This detects loss of the
source realization independently of scalar recurrence checks.

For that valid first image, the correct field inverse numerator is
C*P_1-P_2=m*P_0, whose two nonzero entries equal m. The incorrect first
divisor m^2 rejects this image, while the correct divisor m recovers
P_0. The scalar inverse numerator is zero. Finally the unrestricted
degenerate metric example in Section 6 explicitly limits the reading
domain even though the unrestricted bijection remains valid.

## 8. Scope earned by these proofs

The selected model has one exact rational solution for every prescribed
word and source context, integer storage of every finite prefix, a
Hermitian source reader preserved by cyclotomic holonomy, an unrestricted
total funded bijection, a sharp finite budget horizon, continued
field-to-source response, and exact simultaneous metric and source first
variation on the declared TT representative. The all-counter Lorentz
bound follows from a causal proof and the stated canonical free bound.

The source law, fixed dipole and attenuation, common scale, comparison
action and bank are declared choices. No uniqueness of those choices is
claimed. The Hermitian monitor does not supply a derivation from the
earlier seven-phase source law or native U. The indefinite source kinetic
sign does not establish physically admissible matter, and the arithmetic
account does not identify physical energy. Extending this selected linear
sector to nonlinear Einstein dynamics, a native implementation, or a
continuum geometry remains a separate obligation.
