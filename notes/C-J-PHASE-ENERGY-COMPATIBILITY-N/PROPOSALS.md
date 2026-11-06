# Corrected proposals and the exact rest-coin bridge

PUBLIC / NON-CANONICAL / L1 / analytical candidate-T ceiling.
Author: A. M. Thorn. SPDX-License-Identifier: Apache-2.0.
This result-exposed analytical addendum follows the owner-supplied proposals
and the review in issue #1603, comment 6242097395. It is not part of the
frozen audit contract. No new scientific program was executed.

## 1. Definitions and conjugacy

Let X,Y,Z be the standard Pauli matrices, S(z)=diag(z,z^-1),

    D_m(z)=S(z)(I+i m X),       r_m=sqrt(1+m^2),
    U_m(z)=D_m(z)/r_m,
    C_m=[[1,m],[m,-1]],        A_m(z)=S(z)C_m.

U_m is the normalized comparison introduced in this dossier, not a newly
admitted native law. A_m is UNNORMALIZED. For Q=diag(1,-i), multiplication
gives the exact Laurent identity

    Q^-1(-i D_m(z))Q
      =[[-iz,-imz],[imz^-1,-iz^-1]]=A_m(-iz).

The proposed P=XQ gives A_m(-i z^-1), adding spatial reversal. An affine
argument in m requires two identities valid for every z, not sampled z.
From here on U_m(k) denotes U_m(z) evaluated at z=e^(ik), so U_m(0)
means the rest wave number k=0, equivalently z=1, never Laurent z=0.
The normalized equivalence is

    A_m(e^(i(k-pi/2)))/r_m = -i Q^-1 U_m(k) Q.

With Fourier convention psi_hat(k)=sum_x exp(-ikx)psi(x), corresponding
solutions satisfy psi_A(x,t)=(-i)^(x+t) Q^-1 psi_U(x,t). Pointwise norms
agree. On a periodic ring this gauge preserves the periodic boundary only
when its length is divisible by four. Rest k=0 maps to k=-pi/2, so physical
momentum and energy origins must be transported, not silently reset.

At m=2 the coin C_m/r_m is the beta_1 coin [[1,2],[2,-1]]/sqrt5; at m=1/2
it is the beta_3 coin [[2,1],[1,-2]]/sqrt5. Both have primitive integral numerator and norm
five. Excluding the latter by integrality also assumes that the diagonal
streaming coefficient was fixed to one. The existing MINIMAL-READ-DERIVATION
owner is not closed by this change of basis.

## 2. Rapidity range and the actual phase

For m>0 the principal phase obeys

    cos omega_m(k)=cos k/r_m,      0<omega_m(k)<pi,
    omega_m'(k)=sin k/sqrt(m^2+sin^2 k),
    eta(k)=atanh(omega_m'(k))=asinh(sin k/m).

Thus max |eta|=asinh(1/m). If h=log phi, a selected velocity rung tanh(nh)
occurs at real k precisely when |m sinh(nh)|<=1. For m=2 the only INTEGER
rungs are n=-1,0,1; the real Bloch band still has continuously many modes.
For positive integers m,n, equality m sinh(nh)=1 has only (2,1): sinh h=1/2,
while sinh(2h)=sqrt5/2>1. These are elementary conditional conclusions, not
a selection of an electron mass from the native decoder.

Higher rungs are not automatically stationary evanescent modes. At m=2,n=2,
sin k=sqrt5 forces k=pi/2 +/- i acosh(sqrt5) and cos omega= -/+ 2i/sqrt5;
the frequency is complex as well.

At m=2,k=pi/2, actual omega/k=1 but omega'=1/sqrt5. The reciprocal relation
(Ehat/phat)omega'=1 concerns Ehat=sqrt(m^2+sin^2 k), phat=sin k, not the
phase speed of exp(i(kx-omega t)). A standard boost of the actual rest
wavevector (atan2,0) by h gives (sqrt5 atan2/2,atan2/2), not (pi/2,pi/2).

For every m, D_m(i)^2=-(1+m^2)I and U_m(pi/2)^2=-I. Period four concerns the
normalized complex amplitude of that mode, not the raw D_m, a density or
a localized clock; a ray returns after at most two steps. The rest coin
at m=2 has infinite order because its squared eigenvalue (-3+4i)/5 is
not a root of unity in Q(i). This excludes integer-tick recurrence, not
a nonzero frequency or a chosen continuous interpolation period.

## 3. Galois scale, Lucas chain and an exact square root

Set q_n=phi^-n for n>=1. Direct multiplication for any 0<q<1 gives

    U_q(0)^2 = ((1-q^2)I+2iqX)/(1+q^2)
             = U_(2q/(1-q^2))(0).

Since 2q_n/(1-q_n^2)=csch(nh), this proves the exact bridge

    U_(phi^-n)(0)^2=U_(m_n)(0),    m_n=csch(nh).

In particular U_(phi^-1)(0)^2=U_2(0). The contraction parameter in the
second proposal is exactly a half-angle parameter of the rapidity-reach
coin in the first. This is a matrix identity in the same spinor basis.
It establishes a rest-coin subdivision, not a spatial refinement or a
derived choice of the physical clock.

Write F_n,L_n for Fibonacci and Lucas numbers. Then

| n | m_n | r_(m_n) | cos omega_0 | sin omega_0 |
|---|---|---|---|---|
| odd | 2/L_n | sqrt5 F_n/L_n | L_n/(sqrt5 F_n) | 2/(sqrt5 F_n) |
| even | 2/(sqrt5 F_n) | L_n/(sqrt5 F_n) | sqrt5 F_n/L_n | 2/L_n |

This follows from phi^n-phi^-n=L_n for odd n and sqrt5 F_n for even n,
and the corresponding sum with the two expressions exchanged.
The odd subsequence gives m_1=2,m_3=1/2,m_5=2/11. Its rational mixing
parameters and algebraic normalization are valid. Algebraic normalized
coin coefficients in Q(sqrt5,i) also hold for EVEN n. With variable z,
the entire matrix belongs to Mat_2(Q(sqrt5,i)[z,z^-1]); one must not
claim its entries lie in that number field for arbitrary complex z.

For odd n the alternator coin is [[L_n,2],[2,-L_n]]/(sqrt5 F_n).
For n=5 its primitive numerator has squared norm125, not5. Therefore the
new family is not wholly in COIN-SELECTION-CONDITIONAL's fixed norm-five
class. The existing selection of beta_1 or beta_3 remains at its scope.

Nor are the q_n successive dyadic roots of ONE fixed rest coin:

    tan(2 atan(phi^-2))=2/sqrt5 != phi^-1.

Successive principal dyadic roots of U_2(0) instead have parameters
tan(atan(2)/2^j). CLOCKS.md shows why even the true rest identity does
not extend to a repeated identical walk with a linear spatial rescale.

## 4. Scaled limit and corrections to the second proposal

For an independently supplied scale m0>0 and chosen q>0, set alpha=m0/q,

    E_q(p)=alpha acos(cos(p/alpha)/sqrt(1+q^2)).

Then M_curv=m0 and E_q(0)=m0 atan(q)/q<m0. On each bounded p interval,
E_q(p) tends to sqrt(m0^2+p^2) as q tends to zero: uniformly there,
cos(pq/m0)/sqrt(1+q^2)=1-q^2(1+p^2/m0^2)/2+O(q^4), and the positive
arccos branch gives the stated limit. Assigning q=phi^-n or m_n and the
reciprocal alpha remains a chosen family and calibration, not a derived
refinement of the fixed native dynamics. For odd m_n the reciprocal is
L_n/2, not by itself a period of a material clock.

For 0<x<1 the exact bounds are

    x^2/3-4x^4/45 < x/atan(x)-1 < x^2/3.

For the upper bound, atan x-3x/(3+x^2) starts at zero and has derivative
4x^4/((1+x^2)(3+x^2)^2)>0. For the lower, put
D=1+x^2/3-4x^4/45>0. The difference x/D-atan x starts at zero and has
derivative x^6(660-16x^2)/(2025(1+x^2)D^2)>0. This supplies the proof
missing from simple division of truncated series.

For q_n, advancing n by5 decreases the upper relative-mismatch bound by
phi^-10, approximately1/123, or about2.09 decimal orders. The actual mismatch has
that asymptotic ratio. The original table's n=3 and n=5 deviations fall
below its own proved lower bound and are not retained as data.
This limit does not establish the finite mismatch as a physical error;
ENERGY.md also preserves it as a proposed physical relation to test.

The existing J-TORAL-PERIODIC-POINTS row gives, for 5 dividing n,

    #Fix(T_J^n)=(L_n-1-(-1)^n)^2.

Thus #Fix(T_J^10)=(123-2)^2=14641, not15121. A fixed-point count is not
a common return period. See CLOCKS.md for the separate clock problem.

Finally, the proposed Phi_beta=(1+beta)cos k-beta cos(2k) has
Phi_beta''(0)=-1+3beta. For the dispersion cos omega=Phi_beta/r_mu,
M_curv=mu/(1-3beta). With beta=mu^2/9 the ratio is

    M_curv/omega0=1+2mu^2/3+2mu^4/15+O(mu^6).

Reversing the correction, equivalently beta=-mu^2/9 in this notation,
gives 1-4mu^4/45+O(mu^6). A scalar trace ansatz is not yet a constructed
local unitary step or an independently selected coefficient.

## 5. Ladder parity, trace orthogonality and the full cyclotomic action

This exposed continuation follows the owner's proposed identification of
time/space parity with mass/momentum orthogonality; scope was declared in
[comment6247604540](https://github.com/mathorn1973/twist-j/issues/1603#issuecomment-6247604540).
The underlying light-cone and parity identities are already public Canon
LADDER-LIGHTCONE, BOOST-READING-SPLIT and LADDER-ALTERNATOR-BASIS.
They are not newly derived physical identifications. Here n is the
integer boost index; identifying it with an apparatus clock needs the
existing dictionary and a matching dynamics.

### 5.1 Signed conjugate channels versus the positive light cone

Let F_real=Q(sqrt5), sigma(sqrt5)=-sqrt5, psi=sigma(phi)=-phi^-1.
For alpha_n=2phi^n, the proposed conjugate pair has

    alpha_n sigma(alpha_n)=4(-1)^n,
    (alpha_n+sigma(alpha_n))/2=L_n,
    (alpha_n-sigma(alpha_n))/2=sqrt5 F_n.

Thus its raw shell is L_n^2-5F_n^2=4(-1)^n. It is not constantly +4.
Already n=1 gives the raw pair (1,sqrt5), with shell -4.
The positive light-cone pair is instead

    u_n=2phi^n,       v_n=(-1)^n sigma(alpha_n)=2phi^-n,
    E_n=(u_n+v_n)/2,  Pi_n=(u_n-v_n)/2,
    E_n^2-Pi_n^2=u_n v_n=4.

Pi denotes the momentum component in energy units (pc in the proposed
reading). These are dimensionless comparison coordinates. Explicitly,

| n | E_n | Pi_n |
|---|---|---|
| even | L_n | sqrt5 F_n |
| odd | sqrt5 F_n | L_n |

The odd exchange therefore repairs the signed conjugate pair; one cannot
retain its original E^- and also claim E^+ E^-=4 on odd rungs.

There is a useful exact operator expression. On the raw column
w_n=(L_n,sqrt5 F_n)^t, multiplication by phi on the conjugate pair gives

    w_(n+1)=G w_n,       G=(1/2)[[1,sqrt5],[sqrt5,1]].

With X=[[0,1],[1,0]] and eta=diag(1,-1), direct multiplication yields

    G^t eta G=-eta,      B=XG=GX=(1/2)[[sqrt5,1],[1,sqrt5]],
    B^t eta B=eta,       (E_n,Pi_n)^t=X^n w_n=B^n(2,0)^t.

B has cosh(log phi)=sqrt5/2 and sinh(log phi)=1/2. The parity correction
turns the raw sign-changing step into the already known boost.

### 5.2 What is orthogonal, and which form gives the shell

Over Q the eigenspace split is F_real=Q plus sqrt5 Q. For
T(x,y)=Tr_(F_real/Q)(xy), the two summands are orthogonal and

    T(a+b sqrt5,c+d sqrt5)=2ac+10bd.

The integral statement is narrower:

    Z[phi]={(A+B sqrt5)/2: A,B in Z, A=B mod2},
    Z[phi]^sigma=Z,       Z[phi]^(-sigma)=sqrt5 Z.

Their direct sum Z[sqrt5] has index2 in Z[phi]; phi itself is missing
from that sum. The half-sum projectors need not preserve the full
integral lattice. For the doubled alpha_n they give the integral
components L_n and sqrt5 F_n exactly.

Two different forms must be kept distinct. If x=a+b sqrt5, then

    Tr(x^2)/2=a^2+5b^2,       N(x)=x sigma(x)=a^2-5b^2.

The first follows by trace cancellation of the mixed term. The second
is the norm identity supplying the signed shell. For alpha_n specifically,

    Tr(alpha_n^2)/2=L_n^2+5F_n^2=2L_(2n),
    N(alpha_n)=4(-1)^n.

Consequently trace orthogonality does not by itself prove the constant
mass shell. The shell follows from the norm plus the stated parity
correction. Its scale2 was placed in the starting pair; this arithmetic
does not independently select the Dirac coin or a measured mass.

For the corrected pair, Tr(E_n Pi_n)=0 at every rung, but this is
ENERGY/MOMENTUM trace orthogonality, not universal orthogonality of
the fixed rest mass2 and momentum. At n=1, Pi_1=1 and Tr(2 Pi_1)=4.
E_n varies with the boost while the declared rest scale stays2.

There are also two different reversals. Extending the ladder to all
integer n gives E_(-n)=E_n and Pi_(-n)=-Pi_n, whereas

    sigma(E_n)=(-1)^n E_n,    sigma(Pi_n)=(-1)^(n+1) Pi_n.

Thus Galois conjugation equals boost reversal only on the even rungs;
on odd rungs it has an additional common minus sign. The usual
orthogonality of even/odd functions needs a reflection-invariant inner
product and a suitable domain; the growing ladder sequences are not
in l2(Z). Reversal of rapidity is not automatically physical time reversal.

The operator shell in ENERGY.md has a separate direct proof: its Pauli
components anticommute, so H_m^2=(m^2+sin^2 k)I. Replacing that operator
identity with the scalar trace argument would lose its actual mechanism.

### 5.3 An order-four action without the scalar i in Z[j]

Now let K=Q(j), j=zeta_5, O_K=Z[j], phi=-j^2-j^3, J=j/phi.
Use gamma(j)=j^2 (not the globally occupied symbol tau). Then

    gamma^2=complex conjugation,  gamma^4=I,
    gamma(phi)=-phi^-1,           gamma(sqrt5)=-sqrt5.

Although Gal(K/Q) is cyclic of order4, i is NOT an element of K.
Indeed its unique quadratic subfield is the real Q(sqrt5), whereas
Q(i) is imaginary. The standard cyclotomic/Galois facts are also stated
in J. S. Milne, [Fields and Galois Theory](https://www.jmilne.org/math/Books/FT0.pdf),
Theorem3.17 and exercises3-2,A-21. A group of four automorphisms is
therefore not the scalar set {1,-1,i,-i} inside O_K.

Nevertheless there IS an exact quarter-turn representation. Put

    b1=j-j^-1,       b2=j^2-j^-2,
    gamma(b1)=b2,    gamma(b2)=-b1.

They span the two-dimensional rational subspace K_minus={x:bar(x)=-x}.
Its stable integral sublattice Zb1+Zb2 carries the matrix

    gamma|K_minus=[[0,-1],[1,0]],       gamma^2|K_minus=-I.

For the positive rational trace form T_K(x,y)=Tr_(K/Q)(x bar(y)),
b1^2=-phi-2, b2^2=phi-3 and b1 b2=-sqrt5 give

    T_K(b_i,b_j)=10 delta_ij.

Thus the same gamma acts by +1 on Q, by -1 on sqrt5 Q, and by a
quarter-turn on K_minus. This is a rational representation decomposition,
not an integral direct-sum decomposition of all O_K. Nor is it a literal
rotation of the principal complex image: both b1 and b2 are purely
imaginary there. The trace form includes all embeddings.

The action on the actual algebraic generator has a different exact phase:

    gamma(J)=-j^2 phi=(-j^3) J^-1=(1-J)^-1 J^-1,
    gamma(J^n)=(-j^3)^n J^-n.

The factor -j^3 is a primitive tenth root, not i. In the principal
embedding its angle is pi/5. The four images of J have the following
moduli and principal arguments:

| r | gamma^r(J) | modulus | argument |
|---|---|---|---|
| 0 | j/phi | phi^-1 | 2pi/5 |
| 1 | -j^2 phi | phi | -pi/5 |
| 2 | j^-1/phi | phi^-1 | -2pi/5 |
| 3 | -j^3 phi | phi | pi/5 |

Writing M_a for multiplication by a, the complete operator relation is

    gamma M_J gamma^-1=M_(-j^3) M_J^-1.

On the real subfield the parallel relation is
sigma M_phi sigma^-1=-M_phi^-1. These formulas precisely connect scale
reversal, parity and the cyclotomic phase factor. Iterating gamma is
not iterating M_J or the native U, and the quarter-turn representation
does not supply a pi/2 phase increment per physical tick. In particular
it does not override the scheduled contact invariant in APPARATUS-BRIDGE.

## Scope

All additions above are exact algebra or explicitly stated analytic limits.
They neither derive the normalized walk from native U, identify a measured
inertial response, nor close MINIMAL-READ-DERIVATION. The original proposals
were exposed before this analysis; none of these formulas is a blind test.
