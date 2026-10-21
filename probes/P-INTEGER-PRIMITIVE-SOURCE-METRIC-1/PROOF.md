# Proofs for P-INTEGER-PRIMITIVE-SOURCE-METRIC-1

Status: NON-CANONICAL, L1. Prospective analytical proofs of B1--B5 in
PREREG.md. This document supplies no execution result or canonical promotion.

Owner: A. M. Thorn, session integer-primitive-source-metric-2026-10-19.
Ownership issue: https://github.com/mathorn1973/twist-j/issues/1640.

## 0. Authority, dependencies, and notation

The authority is Public Canon v103, with public main and peeled canon-v103
at dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d and declared content commit
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66. The actual canon/CANON.md has
1052518 bytes and SHA-256
d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b.
The complete normative-file manifest belongs to SOURCE.md.

The canonical inputs used below are the selected initial word/slice table,
operator L, derivative branch, and full quadratic action in
[DEF-K1-LINEAR-METRIC](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/CANON.md),
and the free all-counter bound in K1-LINEAR-METRIC-COMPLETION [T] in that
same immutable file. The latter states, at its selected L1 scope,

    sum_r h_n^free(r)=1,
    -59/100 < h_n^free(r) < 99/100

for every listed word, site, and counter n>=0. These are explicitly imported
canonical premises for the new response bound, not observations inferred
from a finite run.

The source apparatus has the non-canonical companion
[P-INTEGER-SOURCE-HOLONOMY-1](https://github.com/mathorn1973/twist-j/blob/b3de2d7886a00bc7d6b2f5fe470516424be8b046/probes/P-INTEGER-SOURCE-HOLONOMY-1/PROOF.md),
pin b3de2d7886a00bc7d6b2f5fe470516424be8b046, PR #1633. The scaled
shared-bank companion is
[P-INTEGER-K1-SCALED-BRIDGE-4](https://github.com/mathorn1973/twist-j/blob/fda020d27b2ea57eafe143a2bc7a3b59a52ef6ce/probes/P-INTEGER-K1-SCALED-BRIDGE-4/PROOF.md),
pin fda020d27b2ea57eafe143a2bc7a3b59a52ef6ce, PR #1639. The algebra needed
for the new claims is derived below; those companion probes do not provide
canonical authority for this new interaction.

Write H_src for the Hermitian register called H in the core. Its reference
register remains R, and Rev denotes direction reversal. Write V_ij for the
spatial metric perturbation in the action, so it is never confused with
H_src. Write D_seed=diag(0,1) for the ready Hermitian seed, D_n for the
reader denominator, and D_sp for the canonical spatial derivative.

The fixed coupling context lambda is 1 in the target model and 0 in the
specified negative control. It is neither a state coordinate nor the
optional overall action-normalization constant discussed in the Canon.
Put m=324, ell=(1,-1,0,0,0), and e=(1,1,1,1,1). The all-ones matrix is
J_5, distinct from the cyclotomic unit J.

For the cyclic site shift S f(r)=f(r+1), with r in Z/5, define

    C=460*I+29*(S+S^(-1))+65*(S^2+S^(-2)),
    L=[188*I-29*(S+S^(-1))-65*(S^2+S^(-2))]/324.

All newly selected state coordinates, controls, source functional, dipole,
integer forcing coefficient, account, and reflection rule have the
NEW_DECLARED interpretation in PREREG.md. Each theorem is about that
specified mathematical construction.

## 1. Integer closure, the account, and the full funded bijection: B1

### 1.1 Cyclotomic arithmetic and Hermitian transport

Let K=Q(j), O=Z[j], with 1+j+j^2+j^3+j^4=0 and conjugation j->j^4.
For phi=-j^2-j^3 and J=1+j^2, reduction by this polynomial gives

    phi^2=phi+1,
    phi^(-1)=phi-1,
    J^(-1)=-j-j^2,
    J*phi=j.

The conjugation-fixed elements of O are exactly Z[phi]. To see this
directly, write z=z0+z1*j+z2*j^2+z3*j^3. Its conjugate has coefficients
(z0-z1,-z1,z3-z1,z2-z1). Equality with z forces z1=0 and z2=z3,
so z=z0-z2*phi.

Consequently the eight-coordinate Hermitian carrier in PREREG.md is closed
under conjugation by A=diag(J,phi), A^(-1), and B(q)=[[1,q],[0,1]].
Their inverses also have entries in O. Each transport is therefore an
integer bijection of this carrier. Moreover,

    det(A)=j,  det(A)*conjugate(det(A))=1,
    det(B(q))=1.

Thus det(M H_src M dagger)=det(H_src) for all these transports.
No positive-semidefinite restriction on H_src is required.

For H_src=[[a,c],[conjugate(c),d]],

    tr(H_src^2)=a^2+d^2+2*c*conjugate(c).

The field traces are Tr_K/Q(1)=4, Tr_K/Q(phi)=2, and
Tr_K/Q(phi^2)=6. For c=sum_(i=0)^3 c_i*j^i, the trace of j^t is -1
unless t is zero modulo five, when it is 4. Therefore

    Tr_K/Q(c*conjugate(c))
      =5*sum_i c_i^2-(sum_i c_i)^2.

It follows that the stated N is exactly Tr_K/Q(tr(H_src^2)).
For each real pair,

    4*a0^2+4*a0*a1+6*a1^2
      =2*a0^2+2*a1^2+2*(a0+a1)^2+2*a1^2
      >=2*(a0^2+a1^2).

Also (sum_i c_i)^2<=4*sum_i c_i^2, so the off-diagonal contribution
10*sum_i c_i^2-2*(sum_i c_i)^2 is at least 2*sum_i c_i^2.
Together,

    N(H_src)>=2*sum_(i=0)^7 H8_i^2,
    N(H_src)=0 if and only if H8=0.

This is positive-definiteness of an arithmetic quadratic form; it does
not identify N with a physical energy.

### 1.2 The exact image of the seven-phase gate

The core consists of s,q; three eight-integer Hermitian registers; two
five-integer vectors P,Q; k>=1; and p in Z/7. It has 38 coordinates.
The funded carrier adds b>=0 and epsilon in {-1,+1}, giving 40.

The source kick (s,q)->(s-q,s) has inverse (s',q')->(q',q'-s').
The four source transports are integer bijections by Section 1.1.
The detector addition Z->Z+H_src-R has inverse Z->Z-H_src+R,
because it fixes H_src and R. Hence all six source phases have exact
inverses on the full core carrier.

During phase 6, put chi=coeff_j((H_src-R)_01), an integer, and

    a(k)=m if k=1, otherwise m^2.

The field gate fixes all the registers controlling chi and sends

    (P,Q,k,6) -> (C*P-a(k)*Q+2*lambda*chi*ell,P,k+1,0).

Suppose its image has coordinates (P',Q',k',0). Necessarily k'>=2 and

    C*Q'-P'+2*lambda*chi*ell=a(k'-1)*Q.

Thus every coordinate of the left side is divisible by a(k'-1), and the
unique predecessor is

    (Q',(C*Q'-P'+2*lambda*chi*ell)/a(k'-1),k'-1,6).

Conversely, every core at phase 0 satisfying this guard has precisely that
integer predecessor, which maps back to it. The denominator is m at
k'=2 and m^2 at k'>=3. At k'=1 the predecessor is absent.
For p'!=0 the unique predecessor is the inverse of source phase p'-1.
Since the output phase identifies the preceding phase, these images
cannot collide. This proves injectivity of T and the stated exact image.

In particular, adding 1 to P[2] of a field-gate image changes its inverse
numerator by -e_2. Since a(k)>=324, the altered numerator is not divisible
by a(k). The image-corruption fixtures therefore have no backward image,
independently of the available bank.

### 1.3 Domain-and-bank reflection lemma

More generally, let T_+:D_+->D_- be a bijection with inverse T_-, and let
E be an integer account on a core carrier X containing these domains.
For a funded state S=(x,b,epsilon), accept y=T_epsilon(x) exactly when
x lies in its domain and

    c=b+E(x)-E(y)>=0.

An accepted move returns (y,c,epsilon); a rejected move returns
Rev(S)=(x,b,-epsilon).

Both branches preserve E+b and remain in b>=0. If a move is accepted,
the reversed-direction state (y,c,-epsilon) admits the reverse move,
because its target is x and its proposed bank is

    c+E(y)-E(x)=b>=0.

It therefore returns to (x,b,-epsilon). If a move is rejected, applying
Rev to its output reproduces the original rejected input and hence the
same rejection. In both cases,

    (Rev F Rev) F = identity.

Conjugating this identity by Rev, using Rev^2=identity, also gives
F (Rev F Rev)=identity. Thus F is a total bijection with

    F^(-1)=Rev F Rev.

Section 1.2 verifies the exact-domain hypotheses for the new gate, for
either fixed lambda context. The lemma proves the full-carrier part of B1.

### 1.4 Finite shells, sharp prefix horizons, and least periods

The source quadratic form satisfies

    s^2-s*q+q^2 >= (s^2+q^2)/2.

Together with Section 1.1 and k>=1, this proves that

    E=1+s^2-s*q+q^2+N(H_src)+N(R)+N(Z)+k+||P||^2+||Q||^2

is positive and proper on the core, apart from the finite phase coordinate.
On E+b=M, k<=M-1 and all unbounded integer coordinates are bounded.
For each core, b is fixed by M-E; phase and direction have only seven and
two values. Every shell is finite, so its permutation F has purely
periodic orbits.

There is also an exact path description. The bare height

    t(x)=7*(k-1)+p

increases by one under every forward phase, including p=6. Injectivity
gives at most one preceding and one succeeding vertex. On a fixed shell,
an edge is admitted exactly when both endpoint costs are at most M;
admission is symmetric because the reverse bank is the original bank.
Each resulting component is a finite path, never a cycle of core states.

If such a path has L vertices ordered by height, funded F visits each
vertex in the forward direction, reflects at the upper endpoint, visits
each vertex in the reverse direction, and reflects at the lower endpoint.
The 2L states are distinct because their (height,epsilon) pairs are
distinct. Therefore its least period is exactly 2L, including L=1.

For a ready core x_0 at k=1,p=0, the backward domain is absent.
Let x_t=T^t(x_0). Then t(x_t)=t and

    B_sharp(t)=max_(0<=j<=t) E(x_j)-E(x_0).

With initial bank B, its last reachable bare index is the largest t with
B_sharp(t)<=B. Such a largest index exists: E(x_t)>=1+k(x_t) tends to
infinity with t. The funded orbit is the corresponding prefix path and
has least period 2*(t+1). This argument uses prefix maxima, allowing free
steps and decreases in E. It makes no global monotonic-energy assumption.

## 2. Primitive field arithmetic and precision bounds: B2

### 2.1 Correct treatment of the first two slices

The word set is

    W={0010,0011,0100,0101,0110,1001,1010,1011,1100,1101}.

For bits w_0,...,w_3, put u_t=w_(t+2)-w_t for t=0,1, reducing positions
modulo five. Let P_t(r)=delta_(r,u_t)+delta_(r,u_t+1) for t=0,1.
Thus P_0=2*h_0 and P_1=2*h_1 are the two adjacent-site vectors, each
with sum 2. Define

    D_0=2,
    D_n=2*m^(n-1) for n>=1.

At the ready core, P=P_1,Q=P_0,k=1. At its nth field gate, the recurrence is

    P_2=C*P_1-m*P_0+2*lambda*chi_1*ell,
    P_(n+1)=C*P_n-m^2*P_(n-1)+2*lambda*chi_n*ell,  n>=2.

All these vectors are integer. At a completed field counter n, Q=P_0
when n=1 and Q=P_(n-1) when n>=2. Dividing by D_(n+1) gives, also at n=1,

    h_(n+1)=(C/m)*h_n-h_(n-1)+lambda*chi_n*ell/m^n,
    h_n=P_n/D_n.

The first divisor a(1)=m is necessary because D_0=D_1=2. Using m^2 at
that first gate would implement a different recurrence.

Since e^T C=2*m*e^T and e^T ell=0, the initial sums 2 give

    sum_r P_n(r)=D_n, n>=0,
    sum_r h_n(r)=1.

This follows for n=2 from 2*m*2-m*2=2*m and then by induction:
2*m*D_n-m^2*D_(n-1)=D_(n+1).

### 2.2 Exact minimal common denominator at every counter

The following argument allows any integer sequence lambda*chi_n; the
bounded ready-source pattern is not required.

Modulo two, C has zero diagonal and all other entries equal to one:
C=J_5+I modulo two. Every P_n has even sum, m and m^2 are even, and the
forcing term is even. Therefore

    P_n=P_1 modulo 2, n>=1.

P_1 has exactly two ones, so the numerator entries do not all share a
factor of two.

Modulo three, C=-I-J_5. Because sum(P_1)=2 and m=0 modulo three,

    P_2=e-P_1+2*lambda*chi_1*ell modulo 3.

Among sites 2,3,4 there is a site r_* with P_1(r_*)=0: three sites cannot
all lie in the two-one support of P_1. At this site ell(r_*)=0 and
P_2(r_*)=1 modulo three. For n>=2, sum(P_n)=D_n=0 modulo three and m^2=0
modulo three, so

    P_(n+1)(r_*)=-P_n(r_*) modulo 3.

This entry remains nonzero modulo three at every n>=2. P_1 itself also
has an entry not divisible by three.

The candidate D_n=2*m^(n-1) has only the prime factors two and three.
No common factor at either prime cancels. Hence

    gcd(P_n(0),P_n(1),P_n(2),P_n(3),P_n(4),D_n)=1,
    d_n=D_n=2*m^(n-1), n>=1.

Since sum(P_n)=D_n, any common divisor of all numerator entries also
divides D_n. Thus the numerator vector itself is primitive as well.
At n=0 the initial two-one vector has minimal common denominator 2.

In particular v_3(d_n)=4*(n-1) and v_2(d_n)=2*n-1 for n>=1.
This is an all-counter proof, not an extrapolation of the finite history
fixtures.

### 2.3 Encoding bounds and the actual account

For any exact common integer representation h_n=Ptilde/Dtilde with
Dtilde>=1, the minimal common denominator d_n divides Dtilde.
Also sum(Ptilde)=Dtilde. Therefore

    Dtilde>=d_n,
    max_r abs(Ptilde_r)>=ceil(Dtilde/5)>=ceil(d_n/5),
    5*sum_r Ptilde_r^2 >= (sum_r Ptilde_r)^2=Dtilde^2.

Adding Dtilde^2 yields the universal bound in the stated encoding class:

    sum_r Ptilde_r^2+Dtilde^2
      >=(6/5)*Dtilde^2
      >=(6/5)*d_n^2
      =(24/5)*m^(2*n-2).

The actual account stores k and computes D_n from it; it does not charge
a separate D_n coordinate. Its direct consequence is instead

    E(x)>=||P_n||^2>=d_n^2/5=(4/5)*m^(2*n-2).

Other explicit account terms are nonnegative. The pair-encoding bound is
not substituted for this actual-account bound. Neither result is a
representation-independent bound on physical energy or on compressed
symbolic descriptions. Together these statements prove B2 at its scope.

## 3. Source history, forced equation, and uniform signature: B3

### 3.1 The autonomous source coefficient

Because J*phi=j, direct multiplication gives the six-phase loop matrix

    A*B(q)*A^(-1)*B(-q)=C_q=[[1,q*v],[0,1]],
    v=J/phi-1=-2+j-j^2,
    w=v*conjugate(v)=9-5*phi.

The matrices C_q satisfy C_q*C_t=C_(q+t). Starting from (s,q)=(a,0),
the source kick has the successive pairs

    (a,a), (0,a), (-a,0), (-a,-a), (0,-a), (a,0).

Thus the six successive loop q values are a,a,0,-a,-a,0. Their cumulative
sums are sigma_n=a,2*a,2*a,a,0,0 and repeat. Starting from H_src=R=D_seed,
the completed source loop at block n has

    H_src=C_(sigma_n)*D_seed*C_(sigma_n) dagger
         =[[sigma_n^2*w,sigma_n*v],
           [sigma_n*conjugate(v),1]].

The coefficient of j in v is one, so the integer read at phase 6 is

    chi_n=sigma_n=a*(1,2,2,1,0,0) periodically.

The field gate fixes these source registers. The detector register may
accumulate a record, but it does not enter chi and hence does not change
this source pattern. For a=0, chi_n=0 at all blocks.

### 3.2 The exact forced equation and the free control

The selected operator satisfies C/m=2I-L. Consequently Section 2.1 is
equivalent to

    (Delta_c^2+L)h_n=J_n,
    J_n=lambda*chi_n*ell/m^n,
    Delta_c^2 h_n=h_(n+1)-2*h_n+h_(n-1), n>=1.

This recurrence determines exactly one rational successor from the prior
two slices and the internally generated source coefficient. In the
lambda=0 context it is precisely canonical free K1, even for a=+-1.
Likewise the a=0,lambda=1 control is free K1. Neither control removes the
source/detector registers or changes the reading convention.

### 3.3 The zero-sum response bound

For one fixed word and a ready source a in {-1,+1}, compare the lambda=1
history to the free history with the same initial slices. Put
deltah_n=h_n-h_n^free. Then

    deltah_0=deltah_1=0,
    deltah_(n+1)=(2I-L)*deltah_n-deltah_(n-1)+chi_n*ell/m^n.

Since e^T ell=0, the response remains in e-perp. This restriction is
essential: the constant mode of L is zero and does not admit the bounded
oscillatory Green estimate used next.

On e-perp the four eigenvalues of the symmetric L are

    mu_1=mu_4=(235+18*sqrt(5))/324,
    mu_2=mu_3=(235-18*sqrt(5))/324.

They lie strictly between 1/2 and 1. For example sqrt(5)<3 gives
mu_2>181/324>1/2 and mu_1<289/324<1. For each eigenmode set
cos(omega)=1-mu/2 with 0<omega<pi. Then

    sin(omega)^2=mu*(1-mu/4)>3/8.

The scalar zero-initial-data impulse response at lag j>=1 is
sin(j*omega)/sin(omega). Orthogonal spectral decomposition therefore
defines Green operators G_j on e-perp with

    ||G_j||_(2->2)<sqrt(8/3).

For every n>=2,

    deltah_n=sum_(t=1)^(n-1) G_(n-t)*(chi_t*ell/m^t).

Since ||ell||_2=sqrt(2), its norm amplification is less than
4/sqrt(3)<5/2. The source pattern has |chi_1|=1 and |chi_t|<=2 later.
Using the Euclidean norm to bound each component gives

    ||deltah_n||_infinity
      <=||deltah_n||_2
      <(5/2)*(1/m+2*sum_(t=2)^infinity m^(-t))
      =(5/2)*(m+1)/(m*(m-1))
      =1625/209304
      <1/125.

The last strict comparison is exact: 1625*125=203125<209304.
The bound also holds at n=0,1 because the response is zero there.
For a=0 or lambda=0 it holds because the response is identically zero.

### 3.4 All-counter Lorentz signature on the declared reading domain

The imported canonical bound and the preceding response estimate give

    -299/500 < h_n(r) < 499/500

at every site and counter on all twenty target ready histories. Hence

    1+h_n(r)>201/500,
    1-h_n(r)>1/500,
    1-h_n(r)^2>1-(499/500)^2=999/250000.

For

    g_n(r)=diag(-1,1+h_n(r),1-h_n(r),1),

there is exactly one negative and three positive eigenvalues, and

    det(g_n(r))=-(1-h_n(r)^2)<-999/250000<0.

These bounds also hold for the free controls. Every funded state reached
from a ready core lies on its bare prefix path by Section 1.4. Source
phases leave the field reading fixed, and reversal retraces the same
readings. Thus the bounds persist on funded ready histories, including
their retraced prefixes.

The same algebraic formula on an arbitrary integer core need not be
Lorentzian: P=(2,0,0,0,0),k=1 gives h(0)=1 and
g(0)=diag(-1,2,0,1), which is degenerate. No unrestricted-carrier
signature claim is made. The determinant is a varying function of h,
not a fixed determinant. This proves B3 at its declared domain.

## 4. Source contrast, sharp budgets, and the eight periods: B4

### 4.1 Exact source and detector prefix costs

Take word 0010 and a=+-1. The ready field vectors are

    P_1=(1,1,0,0,0), P_0=(0,1,1,0,0).

Their contribution k+||P||^2+||Q||^2 is 5 throughout the first six
source phases. The source quadratic form is 1 throughout, N(R)=4,
and initially N(Z_0)=16.

Each transported H_src has determinant zero, so
tr(H_src^2)=tr(H_src)^2. The five source transport states, including
the ready seed before any transport, give this exact table:

| H_src state | tr(H_src) | N(H_src) |
| --- | --- | ---: |
| D_seed | 1 | 4 |
| after B(-a) | 2 | 16 |
| after A^(-1) | 3 | 36 |
| after B(a) | 6-2*phi | 120 |
| after A | 10-5*phi=1+w | 350 |

For instance phi^2=phi+1 and Tr_K/Q(phi)=2 give
Tr_K/Q((6-2*phi)^2)=120 and
Tr_K/Q((10-5*phi)^2)=350. The source kick changes none of these costs.
Before the detector write the total cost is N(H_src)+27, giving

    31,31,43,63,147,377

at the initial core and after its first five phases.

After the write,

    Z_a=[[1+w,j+a*v],[conjugate(j)+a*conjugate(v),1]].

The trace identities used here are

    Tr_K/Q(w)=26, Tr_K/Q(w^2)=294,
    j*conjugate(v)+conjugate(j)*v=5-3*phi,
    Tr_K/Q(5-3*phi)=14.

Consequently N(Z_a)=414+28*a, equal to 386 for a=-1 and 442 for a=+1.
The total costs after the sixth source phase are therefore 747 and 803.
Since coeff_j(v)=1, the occupied detector coefficient is

    coeff_j((Z_a)_01)=1+a,

giving 0 and 2. Its old value is recovered exactly by Z->Z-H_src+R,
which subtracts this write while retaining all the source data.

### 4.2 The first source-controlled primitive field output

Direct application of C gives

    C*P_1=(489,489,94,130,94),
    C*P_1-m*P_0=(489,165,-230,130,94)=P_2^free.

At phase 6, chi_1=a. Thus

    P_2(-)=(487,167,-230,130,94),
    P_2(+)=(491,163,-230,130,94).

The free numerator has squared norm 344982 and
P_2^free dot ell=324. Adding 2*a*ell changes this norm by
4*a*324+8. Hence the new squared norms are exactly

    ||P_2(-)||^2=343694,
    ||P_2(+)||^2=346286.

At the next state Q=P_1, k=2. The field-only account
1+k+||P||^2+||Q||^2 changes from 6 to 343699 or 346291, a cost increase
of 343693 or 346285. Adding these increases to 747 or 803 gives
the complete first-block energy prefixes

    negative: 31,31,43,63,147,377,747,344440,
    positive: 31,31,43,63,147,377,803,347088.

The final cost in each list is its prefix maximum. Therefore the sharp
first-seven-step banks, by Section 1.4, are 344409 and 347057.
At one less than its own sharp bank each trajectory reaches p=6,k=1
and fails the field admission by exactly one unit. At bank 772 both
reach that phase, with banks 56 and 0, and reject the field step.

At common initial bank 347057, both signs complete the field gate and
reach the same counter k=2. Their remaining banks are 2648 and 0.
The common reader denominator is 648, so

    h_2(+)-h_2(-)
      =(P_2(+)-P_2(-))/648
      =4*ell/648
      =ell/162.

This compares the same word, reader formula, remaining context keys, and
reached counter while changing only the source-sign context key. It is a
difference in the field update itself; it does not rely on comparing
different stopping counters.

### 4.3 Negative controls

At lambda=0, the source phases and detector coefficients 0 and 2 remain,
but both field outputs equal P_2^free. For a=0, chi is zero forever and
the complete field history is free K1.

If chi is omitted from the inverse numerator of an actual first forced
image, the numerator becomes

    C*Q_2-P_2=m*P_0-2*a*ell.

For a=+-1 it is not divisible componentwise by m; a correct inverse
cannot omit the source term.

If the first forward gate instead uses m^2*P_0, its output sum is

    2*m*2-m^2*2=1296-209952=-208656,

whereas the required sum at n=2 is 648. The wrong first coefficient
therefore violates the exact mean. The degenerate unrestricted reading
in Section 3.4 supplies the declared signature-scope counterexample.

### 4.4 The eight exact complete periods

When the first field step is rejected after the six source phases,
the admitted path has heights 0,...,6. It has seven vertices and least
funded period 14. This covers either sign at bank 772, each sign at
its own sharp bank minus one, and the positive source at bank 344409.

An accepted first field step reaches height 7, phase 0, k=2. Its next
source kick is free. The following second-block source transports have
the exact Hermitian costs

| Height | New source state | tr(H_src) | N(H_src) |
| --- | --- | --- | ---: |
| 7 | start of second block | 10-5*phi | 350 |
| 8 | after source kick | 10-5*phi | 350 |
| 9 | after B(-a) | 16-7*phi | 870 |
| 10 | after A^(-1) | 10 | 400 |
| 11 | after B(a) | 18-5*phi | 1086 |
| 12 | after A | 37-20*phi | 4916 |

For clarity, the second B(-a) changes the off-diagonal shear from a*v
to a*(v-1), with (v-1)*(conjugate(v)-1)=15-7*phi. After A^(-1) the
diagonals are 8+phi and 2-phi. After B(a) they are 16-4*phi and 2-phi.
After A the completed loop has shear 2*a*v. These give the table using
det(H_src)=0 and N(H_src)=Tr_K/Q(tr(H_src)^2).

Up to height 12, P,Q,k,R,Z are fixed and the source quadratic form stays
1. Hence, relative to the energy at height 7, the total energy changes are

    0,0,520,50,736,4566.

With residual bank zero after its first field step, a ready orbit reaches
height 8 for free and fails the cost-520 edge to height 9. Its path has
nine vertices and least period 18. This applies to either sign at its
own sharp first-block bank.

For the negative source at common bank 347057, the residual bank is
2648. It reaches heights 8,9,10,11 because their relative prefix maximum
is 736, then fails the next relative barrier 4566. Its path has twelve
vertices and least period 24.

All eight prospective periods are thus determined without assuming an
immediate bounce after an accepted field gate:

| a | Initial bank | Last bare height | Least funded period |
| --- | ---: | ---: | ---: |
| -1 | 772 | 6 | 14 |
| -1 | 344409 | 8 | 18 |
| -1 | 347057 | 11 | 24 |
| -1 | 344408 | 6 | 14 |
| +1 | 772 | 6 | 14 |
| +1 | 344409 | 6 | 14 |
| +1 | 347057 | 8 | 18 |
| +1 | 347056 | 6 | 14 |

On each path all banks equal the fixed shell total minus the current
core energy. Returning to the initial core and direction therefore also
returns the original bank. Distinct (height,epsilon) pairs prove that
no earlier return or repeated funded state occurs. This completes B4.

## 5. Prescribed-source variation of the full quadratic action: B5

### 5.1 All fields and the selected derivative branch

Use the Euclidean inner product on five sites. Let the unitary Fourier
matrix be F_ur=exp(2*pi*i*u*r/5)/sqrt(5). With the eigenvalues mu from
Section 3.3 and mu_0=0, set

    kappa=(0,sqrt(mu_1),sqrt(mu_2),-sqrt(mu_2),-sqrt(mu_1)),
    D_sp=F dagger * diag(i*kappa) * F.

The positive square roots and marked Fourier slots are those selected
by DEF-K1-LINEAR-METRIC. Conjugate pairing makes D_sp real,
D_sp^T=-D_sp, and D_sp^T*D_sp=-D_sp^2=L. Its entries may be real algebraic
numbers; no quadratic coefficient-field claim is required.

Let E_time be the forward slice shift, Delta=E_time-1, and
Delta_c^2=E_time+E_time^(-1)-2. Keep all six independent components of a
symmetric spatial perturbation V_ij, the lapse perturbation ell_0, and
the three shift components N_i. V and ell_0 are placed on integer slices;
N_i and K_ij are on half slices as in the canonical selected action.
Only the spatial derivative in direction 3 is nonzero. Define

    K_11=Delta V_11/2,
    K_22=Delta V_22/2,
    K_12=Delta V_12/2,
    K_13=(Delta V_13-D_sp N_1)/2,
    K_23=(Delta V_23-D_sp N_2)/2,
    K_33=(Delta V_33-2*D_sp N_3)/2,
    K=Tr(K_ij).

The full spatial and lapse terms are

    G2(V)= (1/2)<D_sp V_3j,D_sp V_3j>
          -(1/2)<D_sp V_33,D_sp Tr(V)>
          +(1/4)<D_sp Tr(V),D_sp Tr(V)>
          -(1/4)<D_sp V_ij,D_sp V_ij>,

    R1(V)=D_sp^2 V_33-D_sp^2 Tr(V).

Repeated spatial indices range over 1,2,3; off-diagonal terms in an ij
sum occur twice. The unscaled canonical quadratic action is

    A2[V,ell_0,N]
      =sum_n {<K_ij,K_ij>-<K,K>+G2(V)+<ell_0,R1(V)>}.

These sums specify a local variational principle with compactly supported
variations, not convergence of an infinite kinetic action value.

Freeze the source sequence J_n=lambda*chi_n*ell/m^n from the declared
forward history, and define the new comparison action

    A_J=A2+(1/2)*sum_n <J_n,V_11-V_22>.

No overall action-normalization factor is inserted. The source history,
source registers, word, coupling, and counter convention are held fixed
during the following field variation.

### 5.2 Variation before evaluating the plus-TT representative

Vary all six metric components, ell_0, and N_i independently, and only
then evaluate the first variation at

    V=diag(h,-h,0), ell_0=0, N_i=0.

Here Tr(V)=0, V_3j=0, R1(V)=0, K=0,
K_11=Delta h/2, K_22=-Delta h/2, and every other K_ij=0.

The kinetic first variation is therefore

    (1/2)*sum_n <Delta h,Delta(delta V_11-delta V_22)>.

Terms involving variations of K_12,K_13,K_23,K_33 multiply zero at this
representative; the trace kinetic term also has zero first variation
because K=0. In particular every shift variation vanishes here.

In G2, the first three terms have zero first variation because V_3j,
V_33, and Tr(V) vanish. The remaining term contributes

    -(1/2)*sum_n <D_sp h,D_sp(delta V_11-delta V_22)>.

The lapse variation is zero: R1(V)=0 multiplies delta ell_0, and
ell_0=0 multiplies R1(delta V). These conclusions are obtained while all
variations remain independent; none was discarded by first restricting
the action to a single scalar field.

For compactly supported temporal variations in the interior, with fixed
boundary data, time summation by parts and D_sp^T*D_sp=L give

    delta A2
      =-(1/2)*sum_n <(Delta_c^2+L)h,delta V_11-delta V_22>.

The fixed-source term has first variation

    (1/2)*sum_n <J_n,delta V_11-delta V_22>.

Combining them yields the full local Euler derivative

    delta A_J
      =-(1/2)*sum_n
         <(Delta_c^2+L)h-J,delta V_11-delta V_22>.

The local expression is defined at every n>=1 by the adjacent field
slices. Section 3.2 makes it vanish there. The other four independent
metric component equations, the lapse equation, and the three shift
equations have already been shown to vanish at this representative.
Thus the sourced history solves every independent field equation of this
prescribed-source quadratic comparison action.

### 5.3 Relation to the exact finite variation audit

Restricting only after the full variation gives

    A_J^TT
      =(1/2)*sum_n [||Delta h_n||^2-<h_n,L*h_n>]
        +sum_n <J_n,h_n>.

For the local function in PREREG.md,

    A_local(v)
      =(||v-h_(n-1)||^2+||h_(n+1)-v||^2)/2
        -<v,L*v>/2+<J_n,v>,

the gradient at v=h_n is

    2*h_n-h_(n-1)-h_(n+1)-L*h_n+J_n
      =-[(Delta_c^2+L)h_n-J_n]=0.

Since A_local is quadratic, its exact central difference in a unit site
direction e_r is exactly that gradient component:

    [A_local(h_n+e_r)-A_local(h_n-e_r)]/2=0.

The 600 finite variations audit this TT identity. The full set of
metric/lapse/shift equations is justified by Section 5.2, not inferred
from those scalar finite checks.

### 5.4 What the action statement establishes

The source is prescribed during variation even though its numerical
history is generated by the declared integer apparatus. No variation of
H_src,R,s,q,Z or of chi is performed in A_J. This proof supplies neither
their equations from a joint action nor a reciprocal source-backreaction
law.

The equation is indexed by the accepted forward field counter n. The
funded microdynamics has source phases that hold the reading fixed and
reflections that retrace a prefix. The same forward equation is not
asserted at each funded microtick.

The all-counter signature bound and the exact prescribed-source
stationarity are L1 conclusions for the fixed reading context. They do
not establish a nonlinear Einstein equation, a manifold or continuum
limit, uniqueness among reading contexts, physical source occurrence,
physical clock or energy, or admission as original-U dynamics. These
boundaries complete the interpretation of B5 and of the probe.
