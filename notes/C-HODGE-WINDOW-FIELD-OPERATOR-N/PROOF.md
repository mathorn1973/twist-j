# Event-only mixed Hodge field operator

Status: candidate-T consequences of an explicit candidate-D operator
dictionary. PUBLIC NON-CANONICAL. No Canon authority.
Author: A. M. Thorn <thorn@twistj.com>. Owner: issue #1237.
Frozen preregistration/verifier commit:
369bd76b38483662395da567e834a38c2eb9a2fa.

## 1. Data and notation

Let Lambda=Lambda^2 A4=Z^6 in its marked wedge basis, beta its wedge
pairing, E=E_+ the inherited fixed-J predictive chart, i:E->W its inclusion,

    g=i^T beta i,
    Pi=i g^-1 i^T beta,
    p_j=Pi e_j.

All real statements use the fixed embedding sqrt5>0. In E coordinates put

    C=[p_0 ... p_5]=g^-1 i^T beta.

The compact-window event set M, its scaled copies M_H, the auxiliary norm
||.||_* and covering constant

    R=10-9sqrt5/5

are exactly those of C-HODGE-SPACETIME-WINDOW-N. No event definition is
changed here.

In the marked six-dimensional wedge basis,

    beta^-1=beta

and its only nonzero unordered complementary pairs are

    (0,5): +1,     (1,4): -1,     (2,3): +1.

## 2. Why six independent coordinate Laplacians cannot work

Consider the complete diagonal class

    sum_j a_j p_j p_j^T = c g^-1

over F=Q(sqrt5). There are seven unknowns (a_0,...,a_5,c). Equating the ten
independent symmetric matrix entries gives a 10 by 7 linear system.

A theorem certificate needs only one nonsingular 7 by 7 minor. Use the rows

    (00),(01),(02),(03),(11),(12),(22).

With the exact marked C and g^-1, its determinant is

    -6/25 - (6/125)sqrt5
      = -(6/125)(5+sqrt5) != 0.

Therefore the system has rank seven and its only solution is

    a_0=...=a_5=c=0.

Thus no nonzero scalar operator formed solely as a weighted sum of the six
individual second directional derivatives has the Hodge principal tensor.

This is a complete class no-go. It says nothing against mixed derivatives.

## 3. The source wedge form gives the target d'Alembertian exactly

The mixed class has an exact identity requiring no matrix search:

    C beta^-1 C^T
      = g^-1 i^T beta beta^-1 beta i g^-1
      = g^-1 (i^T beta i) g^-1
      = g^-1.

Hence the continuum operator obtained from the source quadratic form is

    Box_g
      = sum_(ij) beta^(ij) d_(p_i)d_(p_j)
      = 2(d_0 d_5-d_1 d_4+d_2 d_3).

No coefficient is selected from the photon result. The signs and pairings are
already the integral wedge form on Lambda.

For a covector xi, write a_j=xi(p_j). Then the principal symbol is

    -sum_(ij)beta^(ij)a_i a_j
      = -g^-1(xi,xi).

Its characteristic cone is therefore exactly the dual null cone of the
inherited Lorentz metric.

## 4. Why the literal unit stencil does not define a field operator on all M

The direct forward mixed difference for one complementary pair requires
w, w+e_i, w+e_j and w+e_i+e_j all to remain admitted labels.

The exact label

    w=(-1,-1,-1,-1,0,-1)

is admitted because

    -beta(Nw,Nw)=1/5+(3/5)sqrt5
               <= 4/5+(2/5)sqrt5=c0,

the difference being (3-sqrt5)/5>0.

For the required offset e_5,

    -beta(N(w+e_5),N(w+e_5))=-1/5+sqrt5 > c0,

because the difference is -1+(3/5)sqrt5>0. The latter inequality is
equivalent to 45>25 after squaring positive sides.

Therefore the fixed unit stencil is not total on M. The event set cannot
inherit the raw Z^6 finite-difference operator by simple restriction.

This is why the next construction reprojects each requested stencil corner
back to an actual event, rather than assigning hidden off-event field values.

## 5. A total operator using only actual events

For n>=1 set

    H=n^4,       delta=1/n.

For every z in E_R define

    rho_H(z)=Pi rnd(H z)/H.

If r=rnd(H z) and e=r-Hz, then every coordinate of e lies in [-1/2,1/2].
Since Nz=0,

    Nr=Ne.

By the frozen definition of c0,

    -beta(Nr,Nr)<=c0,

so rho_H(z) is always an element of M_H. Moreover the predecessor covering
argument gives

    ||rho_H(z)-z||_* <= R/H = R/n^4.                  (1)

This proves totality before any field is chosen.

For x in M_H and a in Z^6 let

    R_n(x,a)=rho_H(x+delta Pi a).

For a complementary pair i!=j define the four-corner mixed difference

    Delta_ij^(n) psi(x)
      =(n^2/4) sum_(eps,eta=+/-1)
          eps eta psi(R_n(x,eps e_i+eta e_j)).

Every argument is an actual event. The total scalar operator is

    Box_n=2(Delta_05^(n)-Delta_14^(n)+Delta_23^(n)).  (2)

Its requested ideal corners are O(1/n) from x, and (1) changes them only by
O(1/n^4). Thus Box_n is a local event-only stencil whose radius tends to zero.

The choice H=n^4 is visible input. It is used because a second difference
multiplies function-value errors by n^2; the n^-4 position error then
contributes at order n^-2, matching the centered-difference truncation order.
No uniqueness claim for this scaling path is made.

## 6. Convergence to the Hodge wave operator

First ignore rounding. Define

    tilde_Delta_ij^(n) f(x)
      =(n^2/4) sum eps eta
          f(x+(eps p_i+eta p_j)/n).

By two applications of the fundamental theorem of calculus this is the
uniform average of d_i d_j f over the rectangle
[-1/n,1/n]^2 in the two directional variables. For f in C^4, Taylor-expand
d_i d_j f to second order about x. The two linear terms average to zero.
On a compact set, bounded fourth directional derivatives therefore give

    tilde_Delta_ij^(n) f(x)
       = d_i d_j f(x)+O(n^-2),                         (3)

uniformly after enlarging the compact set by a fixed small neighborhood.

Now restore the rounded corners. By (1), each rounded corner differs from its
ideal corner by at most R/n^4 in ||.||_*. If the first derivative of f has
dual-norm bound M_1 on the compact enlargement, the four value errors in one
mixed difference contribute at most

    (n^2/4)*4*M_1 R/n^4 = M_1 R/n^2.

There are three complementary pairs and coefficient magnitude two. Combining
this with (3),

    Box_n(f|M_(n^4))(x)=Box_g f(x)+O(n^-2)             (4)

uniformly on compact event sets.

This is a consistency theorem. It does not prove a finite-n Cauchy theorem,
energy estimate or Green function.

## 7. Explicit event-plane-wave residual

For psi_xi(x)=exp(i xi(x)), put a_j=xi(p_j). The ideal mixed stencil is exact:

    tilde_Delta_ij^(n) psi_xi / psi_xi
      = -n^2 sin(a_i/n) sin(a_j/n).

Use

    |n sin(a/n)-a| <= |a|^3/(6n^2),
    |n sin(a/n)| <= |a|.

For one pair,

    |n^2 sin(a/n)sin(b/n)-ab|
      <= (|a|^3|b|+|a||b|^3)/(6n^2).

If A_xi=max_j |a_j|, the three pairs and their factor two contribute at most

    2 A_xi^4/n^2.                                      (5)

For the rounded corner error, let X_xi be the dual norm of xi relative to
||.||_*. The elementary inequality |exp(iu)-1|<=|u| and (1) give at most

    X_xi R/n^2

per mixed pair. After the three pair terms and coefficient two the total is

    6 R X_xi/n^2.                                      (6)

The exact principal-tensor identity of section 3 and (5)-(6) yield

    | Box_n psi_xi(x)/psi_xi(x)+g^-1(xi,xi) |
       <= [2 A_xi^4+6R X_xi]/n^2.                     (7)

The bound is independent of x. No Fourier basis or completeness theorem for
the aperiodic event set is assumed.

## 8. Local transfer of the registered D3 scalar photon modes

Freeze the coframe from PREREG.md. In the marked E basis the three spatial
vectors

    s1=(1,-1,0,0),
    s2=(1,1,-2,0),
    s3=(1,1,1,0)

are mutually g-orthogonal, as is t=(0,0,0,1). Their squared norms are

    g(s1,s1)=2sqrt5/5,
    g(s2,s2)=6sqrt5/5,
    g(s3,s3)=3sqrt5/2,
    g(t,t)=-(2+sqrt5)/8.

Normalize by the positive square roots and retain the declared future sign of
t. This gives one explicit real orthonormal frame (S1,S2,S3,T), hence the
coframe F0 with

    -g^-1(xi,xi)=Omega^2-|k|^2.

This is a fixed dictionary choice, not a theorem selecting a physical frame.

For epsilon=1/n and r=|k|<=n, the registered D3 positive principal root obeys

    -(11/27)n^-2 r^3 <= Omega_n-r <= (1/12)n^-2 r^3.

Therefore

    |Omega_n^2-r^2|
       = |Omega_n-r|(Omega_n+r)
       <= (275/324)n^-2 r^4,                           (8)

because Omega_n<=r+r/12=13r/12 and Omega_n+r<=25r/12.
The negative root has the same square.

Let xi_n=F0^-1(Omega_n,k) and sample

    psi_(n,k)(x)=exp(i xi_n(x)),     x in M_(n^4).

For every fixed K, the set of xi_n with r<=K and n>=max(1,K) is compact.
Hence

    A_K=sup A_(xi_n),       X_K=sup X_(xi_n)

are finite constants fixed entirely by F0 and K. From (7)-(8),

    |Box_n psi_(n,k)(x)|
      <= [ (275/324)K^4 + 2A_K^4 + 6R X_K ]/n^2.      (9)

Thus the actual principal D3 modes map to actual event fields whose Box_n
residual tends uniformly to zero on bounded lifted momentum sets.

This is the first explicit scalar D3-to-event mode map in this lane. It is
local and branchwise. It is not a global map of the reciprocal torus, a
Hilbert-space isomorphism, a transfer of the D3 action or measure, a
polarization statement, or a physical photon.

## 9. Finite-scale rounding covariance fails

The continuum tensor is exactly inherited and covariant under every retained
source symmetry preserving beta and E. The deterministic rounding rule is a
different matter.

At n=1 take the admitted label

    w=(-1,-1,-1,-1,0,-1)

and offset

    a=e_0+e_5.

The rounded target label is

    r=(0,-1,-1,-2,0,0).

For Q=Lambda^2 C,

    Qr=(-2,-2,3,0,-1,-2),

while rounding the transformed target gives

    rnd(Pi(Qw+Qa))=(-1,-1,2,0,-1,-2).

They differ. Since Pi is injective on integer labels,

    Q_E R_1(x,a) != R_1(Q_E x,Qa).

For the J step L,

    Lr=(1,0,-1,-1,-1,1),

whereas

    rnd(Pi(Lw+La))=(0,0,-1,-1,0,1),

again different.

Therefore the chosen finite-scale rounding stencil is not literally
equivariant under either retained symmetry. This is exactly the G7 negative.

It does NOT follow that the limiting field equation violates these
symmetries. Equation (4) converges to Box_g, and Box_g is the invariant
operator fixed by g^-1. Finite-scale covariance would require another
construction, likely an equivariant rounding/averaging rule, and is left open.

The result also does not assert that Box_n itself fails every possible
weaker or averaged covariance relation. Only the frozen neighbor-rule equality
has been falsified.

## 10. Status and remaining bridge

Candidate-T:
- complete diagonal-stencil no-go;
- exact mixed tensor C beta^-1 C^T=g^-1;
- literal unit-stencil totality counterexample;
- all-event totality and C^4 consistency of Box_n;
- explicit plane-wave residual;
- local registered-D3 principal-mode residual bound;
- exact finite-rounding C5/J covariance failures at the frozen equality.

Candidate-D:
- selection of the two-scale rounding operator family and fixed coframe as the
  L2-to-L5 dictionary.

Candidate-C:
- exact pinned finite audits and two-architecture reproduction.

Still open:
- finite-n self-adjointness or an alternative symmetric operator;
- well-posed Cauchy evolution and energy positivity on M_(n^4);
- an exact finite-scale symmetry-restoring event stencil;
- global D3 carrier/action/measure transfer;
- vector gauge structure and polarization;
- physical massless phase, occurrence, apparatus and SI calibration;
- derivation of the window and field dictionary from native Omega,U.

No public Canon, Registry, Frontier or gate status changes.
