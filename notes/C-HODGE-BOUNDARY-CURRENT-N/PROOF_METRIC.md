# Arithmetic Hermitian carriers, metric normalization, and residual actions

**NON-CANONICAL. L1. Proof-first candidate-T arguments.**

These analytical derivations were written before the successor's scientific
execution. This document does not report a run. Its inputs are the exact marked
A4 construction of Public Canon v104 and the definitions of the pinned
C-HODGE-PULSE-TRANSFER-N note.

The positive result below changes both the arithmetic Hermitian carrier and
the real-field scale. It is **not** a solution of the predecessor's unchanged
metric equation. It also does not derive the target action from a lossless
source transfer; the separate source-current obstruction is unaffected.

## 1. Fields, forms, and the canonical marked source

Write

~~~
s = sqrt(5),       F = Q(s),       phi = (1+s)/2,
r_plus = phi^2 = (3+s)/2,          r_minus = phi^-2 = (3-s)/2,
zeta = zeta_10 = -zeta_5^3,        delta = phi-3 = (s-5)/2.
~~~

The CM field is

~~~
K = Q(zeta_5) = F(zeta) = F(tau),
tau = zeta-zeta^-1,       tau^2 = delta,
zeta = (phi+tau)/2.
~~~

Conjugation fixes F and negates tau. Both real embeddings of delta are
negative. The extension F(i) is different and must not be identified with K.

Use the ordered bivector basis (01,02,03,12,13,23) of the marked exterior
square of A4. Its wedge Gram has complementary pairings

~~~
beta(01,23)=1,      beta(02,13)=-1,      beta(03,12)=1,
beta(z,z)=2(z1*z6-z2*z5+z3*z4).
~~~

The public operator L, the exterior square of the marked multiplication by J,
is

~~~
L =
[[ 0,-1, 0, 0, 0, 1],
 [ 0, 1,-1, 0, 0,-1],
 [ 1, 0, 1, 0,-1, 0],
 [ 0, 0, 1, 0, 0, 1],
 [-1, 0,-1, 1, 1,-1],
 [ 1, 0, 1,-1, 0, 1]].
~~~

The first three independent columns of the public positive Hodge projector
are

~~~
p1 = ( 5, s,-s, s, -s,3s)/10,
p2 = (-s, 5, s, s,-3s, s)/10,
p3 = ( s,-s, 5,3s, -s, s)/10.
~~~

The public four-dimensional predictive carrier E_J contains these vectors.
Its L action preserves beta and has characteristic polynomial

~~~
(X^2-3X+1)(X^2-phi*X+1).
~~~

In the public deterministic basis, completed by the first nonzero column
of P_minus L P_plus, the beta Gram is

~~~
diag( (s/10)*[[3,1,1],[1,3,1],[1,1,3]], -(2+s)/8 ).
~~~

This is the original marked normalization, not a freely chosen Lorentz Gram.

## 2. Two initial metric obstructions

### 2.1 The two real signatures

At the principal embedding beta has signature (3,1). At the other embedding
its three-dimensional block is negative and its fourth entry is positive,
giving signature (1,3).

For either CM extension F(i)/F or K/F, minus the determinant on Hermitian
two-by-two matrices has signature (3,1) at both real embeddings. Therefore
unscaled beta cannot be F-isometric to that form. Dividing beta by s corrects
this signature discrepancy, but does not settle the arithmetic isometry.

### 2.2 The F(i) square-class obstruction persists at every scalar scale

The source determinant is

~~~
det(beta_EJ) = -(5+2s)/80.
~~~

The three-by-three integer matrix has determinant 20; its scaled determinant
is s/10. Multiplying by the fourth entry proves the formula.

The standard determinant form on Herm2(F(i)/F), in coordinates

~~~
[[t+z,x-iy],[x+iy,t-z]],
~~~

has Gram diag(1,-1,-1,-1), with determinant -1. Negating the form in dimension
four leaves its determinant unchanged. The determinant ratio has representative

~~~
d = (5+2s)/80,       N_F/Q(d) = 1/1280.
~~~

An F square has rational-square norm. Since 1280 equals 2^8 times 5, d is
not an F square. A basis change multiplies a Gram determinant by a square;
multiplying a four-dimensional form by c multiplies it by c^4.
Consequently **no scalar multiple of beta_EJ is F-isometric to the standard
Hermitian determinant over F(i)**. A real isometry at one selected embedding
is not excluded.

The determinant square class of the Hermitian determinant over K/F is delta.
In this case

~~~
det(beta_EJ)/delta = phi^4/80 = (phi^2/(4s))^2.
~~~

Changing to K removes this determinant obstruction. It does not yet prove
an isometry.

## 3. The compact plane and the norm obstruction at 2

Define

~~~
v = p1-p3 = (5-s,2s,-5-s,-2s,0,2s)/10,
w = L v  = (0,5+s,-2s,s-5,-2s,2s)/10.
~~~

Direct substitution in L gives

~~~
L w = phi*w-v,
L^2 v = (s-5,5+s,0,0,-5-s,5-s)/10.
~~~

The two independent vectors span the compact primary plane. The wedge form
gives

~~~
beta(v,v) = beta(w,w) = 2s/5,
beta(v,w) = s*phi/5.
~~~

Thus, for q0=beta/s,

~~~
q0(xv+yw) = (2/5)*(x^2+phi*x*y+y^2)
           = (2/5)*N_K/F(x+y*zeta).
~~~

The other primary plane is split hyperbolic. Its distinct F eigenvalues are
r_plus and r_minus. Both eigenlines are isotropic because beta is invariant
and neither eigenvalue has square one; their pairing is nonzero by
nondegeneracy.

The primary planes are orthogonal. Pairing a boost eigenvector of eigenvalue
lambda with the compact plane gives an eigenfunctional of the compact action
of eigenvalue lambda^-1. Its annihilating polynomial does not vanish there,
so that functional must be zero. Therefore

~~~
(E_J,beta/s) = hyperbolic plane orthogonal-sum ((2/5)*N_K/F).
~~~

The form -det on Herm2(K/F) is a hyperbolic plane plus N_K/F.

### 3.1 The elementary inert-prime proof

The polynomial of phi modulo 2 is X^2+X+1, irreducible over F2. Hence
(2) is a prime of F with residue field F4={0,1,t,t^2}, where t^2+t+1=0.
The polynomial of zeta over F is X^2-phi*X+1. Its reduction is
X^2+t*X+1, taking respectively the values

~~~
1, t, 1, t
~~~

at 0,1,t,t^2. It is irreducible over F4 and has nonzero constant derivative t.
Thus (2) is unramified and inert in K/F, with residue extension F16/F4.

The unique prime P over (2) is fixed by conjugation. For every a in K*,

~~~
v_(2)(N_K/F(a)) = v_P(a)+v_P(conj(a)) = 2*v_P(a).
~~~

Relative norms have even valuation at (2), whereas 2/5 has valuation one.
So 2/5 is not a relative norm.

### 3.2 Why arbitrary isometries are excluded

The norm planes a*N_K/F and N_K/F are isometric exactly when a is a relative
norm. Necessity follows by applying an isometry to 1. Sufficiency follows
by multiplication by an element of norm a.

The common hyperbolic planes cancel. The needed quadratic cancellation has
an elementary reflection proof: vectors e,f of the same nonzero norm can be
matched by reflection in e-f if its norm is nonzero. Otherwise reflection
in e+f, followed by reflection in e, matches them. Restricting to orthogonal
complements cancels one common nonzero line. A split hyperbolic plane is a
sum of two such orthogonal lines, so two applications suffice.

It follows that **beta_EJ/s is not F-isometric to -det on Herm2(K/F)**.
Both real signatures and the determinant square class agree, but the norm
obstruction at 2 remains.

## 4. Explicit boost vectors

Put

~~~
f_comp(X)=X^2-phi*X+1,       r=f_comp(L)p1.
~~~

Expanding the same fixed L and p1 gives

~~~
r=(A,-B0,B0,A,-B0,A),
A=(5+s)/10,       B0=(15+s)/20.
~~~

The vector r is nonzero. More generally,

~~~
h(A0,B0)=(A0,-B0,B0,A0,-B0,A0),
L h(A0,B0)=h(A0+B0,A0+2B0),
beta(h(A0,B0),h(A0,B0))=2(A0^2+A0*B0-B0^2).
~~~

The coefficient-column determinant of r,Lr is
A^2+A*B0-B0^2=phi/4, nonzero. This family is the whole boost primary plane
inside E_J. In particular

~~~
h_plus=h(1,phi),       h_minus=h(1,1-phi),
L h_plus=phi^2*h_plus, L h_minus=phi^-2*h_minus,
beta(h_plus,h_plus)=beta(h_minus,h_minus)=0,
beta(h_plus,h_minus)=5.
~~~

The polynomial-projector version is

~~~
u_plus=(L-r_minus*I)r=(phi^2/2)*h_plus,
u_minus=(L-r_plus*I)r=-(phi^-1/2)*h_minus,
k=beta(u_plus,u_minus)=-5*phi/4.
~~~

The normalizing denominator k is thus explicitly nonzero.

## 5. Full intertwining after an explicitly changed scale

Define

~~~
q_E=(s/2)*beta_EJ,
e_plus=u_plus,       e_minus=-u_minus/(s*k).
~~~

The vectors e_plus,e_minus,v,w are a basis. Their q_E bilinear pairings are

~~~
q_E(e_plus,e_plus)=q_E(e_minus,e_minus)=0,
q_E(e_plus,e_minus)=-1/2,
q_E(v,v)=q_E(w,w)=1,       q_E(v,w)=phi/2,
all mixed boost/compact pairings=0.
~~~

For

~~~
X(a,d,x,y)=[[a,            x+y*zeta],
            [x+y*zeta^-1, d      ]],
~~~

set

~~~
I(X(a,d,x,y))=a*e_plus+d*e_minus+x*v+y*w.
~~~

Then

~~~
q_E(I(X),I(X))=-a*d+x^2+phi*x*y+y^2=-det(X).
~~~

Now define the algebraic spinor

~~~
A_H=diag(phi*zeta,phi^-1).
~~~

Its determinant zeta has relative norm one. Using zeta^2=phi*zeta-1,
Hermitian congruence acts on the displayed coordinates by

~~~
(a,d,x,y) -> (phi^2*a,phi^-2*d,-y,x+phi*y).
~~~

The corresponding L relations are

~~~
L e_plus=phi^2*e_plus,       L e_minus=phi^-2*e_minus,
L v=w,                     L w=phi*w-v.
~~~

Therefore, on the whole carrier,

~~~
I(A_H X A_H^*)=L I(X),       I^*q_E=-det.
~~~

This is a complete F-linear form isometry and action intertwiner, not merely
a characteristic-polynomial comparison.

It uses K rather than F(i), and (s/2)*beta rather than beta or beta/s.
Equivalently the unchanged beta pulls back under I to (2/s)*(-det).
That factor cannot be silently renamed away. The norm obstruction shows why
the beta/s normalization is not a basis-equivalent substitute over F.

Nothing here selects A_H from the pulse or implements it as a physical time
update. An F-linear isometry also does not identify integral lattices.

## 6. Star-compatible descent of the pulse Hermitian lattice

Return to

~~~
B=(1/2)*[[s,-1],[-1,s]],
R=Z[phi,1/2],       pi=s,       R_i=R[i].
~~~

Modulo pi, R has residue F5 and phi maps to 3. Because
X^2+1=(X-2)(X+2) over F5,

~~~
R_i/(pi)=F5 x F5.
~~~

Complex conjugation exchanges the two factors. The rank-four Hermitian
R lattice

~~~
H_i={ [[a,u-iv],[u+iv,d]] : a,d,u,v in R }
~~~

reduces to pairs (Y,Y^T), with evaluation at i=2 giving

~~~
Y=[[a,u-2v],[u+2v,d]].
~~~

This is all of M2(F5): recover u=(Y12+Y21)/2 and
v=(Y21-Y12)/4. It is not merely a symmetric or a traceless matrix carrier.

B has real-field entries, so its honest reduced action is

~~~
C(Y)=Bbar*Y*Bbar^T,
Bbar=[[0,2],[2,0]],
Bbar^2=-I,       Bbar^T=Bbar=-Bbar^-1.
~~~

Thus, on the complete rank-four carrier,

~~~
C=-Ad(Bbar).
~~~

This follows from the lattice and involution. It does not replace one
operation by another without a bridge.

### 6.1 The unchanged trace-zero identification gives minus Phi

Use exactly the predecessor's Psi from W5 to sl2(F5), satisfying

~~~
Ad(Bbar) Psi=Psi Phi,
tr(Psi(v)Psi(w))=3*g5(v,w).
~~~

The trace-zero slice is stable under C and

~~~
C Psi=-Psi Phi.
~~~

Its plus/minus dimensions are 2 and 1, rather than 1 and 2. For traceless
two-by-two matrices, det(Y)=-(1/2)tr(Y^2). Since -(1/2)*3=1 in F5,

~~~
det(Psi(v))=g5(v,v).
~~~

On the complete decomposition Y=tI+Psi(v),

~~~
det(Y)=t^2+g5(v,v),       C(t,v)=(-t,-Phi(v)).
~~~

The determinant pairing is not the first-order trace pairing h_plus=3g5.
Their scalar relation remains explicit. Using -det reverses the displayed
determinant forms' signs.

### 6.2 A different honest slice gives Phi

The minus sign is not a no-go for every possible three-dimensional reading.
Put

~~~
Omega=[[0,1],[-1,0]].
~~~

For every determinant-one two-by-two matrix,

~~~
Bbar^T*Omega=Omega*Bbar^-1.
~~~

Thus multiplication by Omega intertwines congruence on symmetric matrices
with adjoint conjugation on traceless matrices:

~~~
(Bbar*Y*Bbar^T)*Omega=Bbar*(Y*Omega)*Bbar^-1.
~~~

The explicit symmetric-slice map

~~~
Psi_sym(v)=Psi(v)*Omega^-1
~~~

satisfies

~~~
C Psi_sym=Psi_sym Phi,       det(Psi_sym(v))=g5(v,v).
~~~

The skew line generated by Omega is fixed. Hence there is also a complete
description

~~~
Y=a*Omega+Psi_sym(v),
det(Y)=a^2+g5(v,v),       C(a,v)=(a,Phi(v)).
~~~

Both full descriptions are exact and have eigenspace dimensions 2 and 2.
Their three-dimensional slices differ. The minus-Phi conclusion is a boundary
on the predecessor's unchanged trace-zero identification, not an obstruction
to all star-compatible reductions.

## 7. The corrected CM field has a different residue algebra

The target of section 5 uses

~~~
R_K=R[tau],       tau^2=delta=s*(1-s)/2,       tau^*=-tau.
~~~

Modulo pi,

~~~
R_K/(pi)=F5[epsilon]/(epsilon^2),       epsilon^*=-epsilon.
~~~

This is not F5 x F5. The CM extension is ramified. The standard Hermitian
rank-four R lattice consists of matrices

~~~
[[a,u+v*tau],[u-v*tau,d]],
~~~

with

~~~
-det=-a*d+u^2-delta*v^2.
~~~

Its reduction is -a*d+u^2, with one-dimensional radical in the v direction.
Reduction modulo the prime generated by tau instead would discard this
direction. That is a quotient, not the rank-four reduction just specified.

For the real B, the symmetric part acts by congruence and the infinitesimal
skew part is fixed because Bbar*Omega*Bbar^T=Omega. This degenerate rank-four
form differs from the nondegenerate split form obtained from R[i].

The field map I does not assert that this standard Hermitian lattice equals
the saturated lattice E_J intersect (Lambda^2 A4 tensor R). Its basis includes
explicit denominators involving s. Their elementary divisors and first-derived
forms require their own lattice comparison. In particular no conclusion about
the separately reported rank-two reduction of another Hodge lattice follows
from the rank-three standard-Hermitian reduction here.

## 8. Scope

The distinct conclusions are:

1. Unscaled beta has incompatible signs at the two real places.
2. The F(i) carrier fails the determinant square-class test at every scalar
   scale.
3. With K, beta/s still fails by the relative-norm obstruction at 2.
4. At the changed scale (s/2)*beta the explicit I gives the full field
   isometry and intertwiner.
5. The pulse R[i] lattice has an honest rank-four star-compatible reduction.
   Its trace-zero slice yields -Phi; its separately identified symmetric
   slice yields Phi.
6. The corrected K target has dual-number residue algebra and a different
   residual metric, so it cannot be substituted for the split pulse lattice.

All are L1 statements about fixed fields, lattices, slices, signs and scales.
No physical spacetime or source-side derivation of the Hodge rotation follows.
