# Finite integer field window and integral Phi5 carrier

PUBLIC / NON-CANONICAL. Action layer: L1. This is a symbolic proof for the
frozen C-FIELD-CYCLOTOMIC-WINDOW-N assignment, not a run record or a Canon
promotion. It uses the electric-first convention and the inherited
FIELD-SHEAR-ENERGY-BOUNDARY identities. No scientific program or scratch
calculation was executed to obtain this fragment.

## 1. Statement and inherited algebra

Let e,f be nonnegative integers, C an e-by-f integer matrix, and
G=C^t C. Put d=e+f and

```text
T(E,M) = (E+CM, M-C^t(E+CM)),
T = [[I,C],[-C^t,I-G]],
H(E,M) = E^t E + M^t M + E^t C M.
```

The maximum eigenvalue of an empty G is defined to be zero. Then

```text
max spec(G) < 4
  iff T has finite order on Z^d
  iff every orbit of every x in Z^d is bounded.
```

Here finite order means one integer N>=1 with T^N=I on the full carrier.
Boundedness may be defined over all n in Z or just n>=0: the two choices
give the same assertion and the same result. In particular, the quantifier
is over every full integer state, not one selected orbit or projection.

The two shear factors have determinant one and integer inverses. Explicitly,

```text
T^-1 = [[I-CC^t,-C],[C^t,I]],
M = M' + C^t E',
E = E' - C M.
```

Thus T is an automorphism of Z^d, including all rectangular cases. To check
energy invariance directly, set a=E+CM. Substitution gives

```text
H(E,M) = ||a||^2 + ||M||^2 - a^t C M
       = H(a,M-C^t a).
```

The completed-square identity is

```text
4H(E,M) = ||2E+CM||^2 + M^t(4I-G)M.
```

Consequently H is positive definite exactly when max spec(G)<4, and
positive semidefinite exactly when max spec(G)<=4. Necessity follows by
choosing E=-CM/2; sufficiency follows from the displayed identity and the
positive E-only term. Positive definiteness on the zero-dimensional space
is understood in its usual vacuous sense.

## 2. From positive energy to a common integer period

Write s=sqrt(max spec(G)), with s=0 in the empty case. If s<2, then

```text
|E^t C M| <= s ||E|| ||M||
          <= (s/2)(||E||^2+||M||^2),
H(E,M) >= (1-s/2)(||E||^2+||M||^2).
```

For any fixed integer x, energy conservation therefore confines every
T^n x to a bounded Euclidean ball. That ball contains finitely many integer
points. Two forward iterates coincide, say T^a x=T^b x with 0<=a<b.
Invertibility yields T^(b-a)x=x, so the orbit is periodic from its start.

Apply this argument separately to the d standard integer basis vectors.
Choose a positive period p_j for each. Their least common multiple N fixes
every basis vector, hence T^N=I. For d=0 take N=1. This proves strict
spectral window => finite order without assuming a bound uniform over all
initial states or invoking a root-of-unity classification theorem.

Finite order immediately bounds every two-sided orbit. Conversely, if every
integer forward orbit is bounded, each such orbit is finite and the same
basis-period argument again gives finite order, without any positivity
assumption. It remains to prove that a matrix outside the strict window
cannot have all its integer orbits bounded.

## 3. Complete real spectral decomposition and its limits

Let r=rank(C). Choose orthonormal singular pairs (u_i,v_i), 1<=i<=r, with

```text
C v_i = s_i u_i,   C^t u_i = s_i v_i,
s_i>0,            lambda_i=s_i^2.
```

The lambda_i are the positive eigenvalues of G, with multiplicity. On the
plane of states (E,M)=(a u_i,b v_i), T has matrix

```text
A_i = [[1,s_i],[-s_i,1-lambda_i]],
det(A_i)=1,
det(mu I-A_i)=mu^2-(2-lambda_i)mu+1.
```

The remaining real subspace is exactly

```text
S_R = ker_R(C^t) direct-sum ker_R(C) = ker_R(T-I),
dim(S_R)=e+f-2r,
```

and T is the identity there. Indeed, T(E,M)=(E,M) first gives CM=0 and
then C^t E=0. Thus zero singular values contribute only static directions,
with no hidden Jordan block at mu=1. The complete characteristic polynomial
is

```text
(mu-1)^(e+f-2r) product_(i=1)^r [mu^2-(2-lambda_i)mu+1].
```

The SVD is a real change of coordinates. It is not asserted to preserve
Z^d, or even Q^d. The coarser spaces

```text
S_Q = ker_Q(C^t) direct-sum ker_Q(C),
A_Q = im_Q(C) direct-sum im_Q(C^t)
```

do give a rational direct sum Q^d=S_Q direct-sum A_Q. Their integer
intersections are individually saturated lattices, but their sum need only
have finite index in Z^d. Saturation of the separate intersections does not
make this sum the full integer lattice. For example, for the symbolic
matrix C=(1,1)^t, the electric active and static integer vectors are
respectively (a,a) and (b,-b). Their sums have electric coordinates of equal
parity, an index-two sublattice of Z^2. This example is an exact algebraic
illustration, not an additional executed finite control. Any selected
integral decomposition requires its own extraction and gluing proof.

## 4. The critical Jordan block and an integer growing orbit

If lambda_i=4, then s_i=2 and

```text
A_i = [[1,2],[-2,-3]] = -I+K,
K = [[2,2],[-2,-2]],
K^2=0, K!=0,
A_i^n = (-1)^n(I-nK)  for every n>=0.
```

This is a nontrivial Jordan block at -1, not a finite-order rotation.
In particular its powers are unbounded and it cannot occur in a finite-order
T. The integer conclusion can also be exhibited directly: because G-4I has
integer entries and a nonzero real kernel, rational row reduction supplies
a nonzero rational kernel vector. Clearing its denominators gives
v in Z^f, v!=0, with Gv=4v. Then Cv!=0 and ||Cv||^2=4||v||^2.

On states (E,M)=(a Cv,b v) the recurrence is

```text
a' = a+b,
b' = -4a-3b.
```

Starting with E_0=0, M_0=v gives, for every n>=0,

```text
E_n = (-1)^(n+1) n Cv,
M_n = (-1)^n(2n+1)v.
```

The formulas hold at n=0. Substituting their coefficients in the recurrence
gives a_(n+1)=(-1)^n(n+1) and
b_(n+1)=(-1)^(n+1)(2n+3), proving them by induction. Moreover

```text
H(a Cv,b v) = ||v||^2(4a^2+b^2+4ab)
            = ||v||^2(2a+b)^2,
H(E_n,M_n) = ||v||^2.
```

This is a full integer orbit growing linearly at constant positive energy.
Positive semidefiniteness at the endpoint does not confine energy shells.

There are bounded exceptional states even on this same critical plane:
(-Cv,2v) has H=0 and T(-Cv,2v)=-(-Cv,2v). Such a two-cycle does not imply
that every orbit is bounded.

## 5. Above the window: an integer orbit with exponential growth

Suppose G has an eigenvalue lambda>4. Choose a real unit eigenvector v and
let mu be the root less than -1 of

```text
mu^2-(2-lambda)mu+1=0.
```

Such a root exists because the two roots are real and negative, have product
one, and have sum 2-lambda<-2. The real linear functional

```text
ell(E,M) = (Cv)^t E + (1-mu) v^t M
```

satisfies ell(Tx)=mu ell(x). To verify this, the coefficient of
(Cv)^t E after substitution is mu, and the coefficient of v^t M is

```text
lambda + (1-mu)(1-lambda) = mu(1-mu),
```

by the quadratic equation for mu. Choose any coordinate j with v_j!=0.
For the integer state x=(0,e_j), where e_j is a magnetic standard basis
vector, ell(x)=(1-mu)v_j!=0. Consequently

```text
||T^n x|| >= |ell(T^n x)| / ||ell||
           = |mu|^n |ell(x)| / ||ell|| -> infinity.
```

Here ||ell|| is its ordinary finite positive Euclidean dual norm. This
constructs an unbounded integer initial state without asserting that the
real eigenvector v is integral, rational, or part of an integer direct sum.

Together with the endpoint argument, this proves that max spec(G)>=4
implies failure of boundedness for at least one full integer orbit and
failure of finite order. All three assertions in Section 1 are equivalent.
Zero matrices of every rectangular size have r=0 and T=I, so they and all
empty cases are already included.

The universal quantifier cannot be replaced by existence of one nonzero
bounded orbit. For the preregistered unstable C=diag(3,0), G=diag(9,0),
yet the nonzero integer state E=(0,1), M=(0,0) is static. The unstable
coordinate supplies other unbounded integer orbits.

## 6. Root-of-unity and chord conclusions inside the window

When 0<lambda_i<4, the two roots on its nonzero singular block are distinct
complex conjugates of modulus one. Since their product is one,

```text
mu + mu^-1 = 2-lambda_i,
lambda_i = (1-mu)(1-mu^-1) = |1-mu|^2.
```

The common full-lattice period N proved in Section 2 also gives mu^N=1
for each block eigenvalue. These roots are different from 1 and -1, while
every static direction has eigenvalue 1. Thus the root-of-unity conclusion
is a consequence of integer discreteness and positive energy; it is not an
extra spectral assumption. The conclusion includes no claim that the
singular coordinates furnish independent integer cyclotomic summands.

## 7. The required v95 fixture and the incidence-only obstruction

For the frozen fixture,

```text
Ccrit = [[1,1],[1,0],[1,0],[0,1],[0,1]],
Ccrit^t Ccrit = [[3,1],[1,3]],
v=(1,1),
Ccrit v=(2,1,1,1,1),
Gv=4v, ||v||^2=2.
```

Section 4 therefore proves, for every n>=0 and with no finite-horizon
extrapolation,

```text
E_n=(-1)^(n+1)n Ccrit v,
M_n=(-1)^n(2n+1)v,
H(E_n,M_n)=2.
```

For the boundary matrix D of the oriented graph used in v95, DCcrit=0.
These growing states have DE_n=0. The inherited zero-energy two-cycle is
the distinct initial state E=-Ccrit v, M=2v.

More generally, take precisely two ordinary signed triangle boundary
columns, each with three distinct unit edge incidences, sharing exactly one
edge. Each column has squared norm three and their inner product is
epsilon in {1,-1}. Their Gram matrix is

```text
[[3,epsilon],[epsilon,3]],
```

with eigenvalues four and two. Its integer four-eigenvector is
v=(1,epsilon), so the same all-n construction has H=2. Reorienting edges
or faces does not remove the critical eigenvalue.

If these are two columns in a larger incidence C, extending this v by zeros
gives the Rayleigh quotient four. Hence max spec(C^t C)>=4 and the larger
full shear also fails the strict window. Its particular critical formula
need not remain valid, because extra columns can couple to that vector;
only the spectral obstruction and the full-carrier theorem transfer
automatically. This conclusion is restricted to the stated unit incidence
and simultaneous shear law. It proves no obstruction to a different update,
energy, incidence convention, or separately selected constrained carrier.

## 8. Reversal and Gauss sectors

For every finite integer C define

```text
R(E,M)=(E+CM,-M),
R=[[I,C],[0,-I]].
```

Applying R twice gives R^2=I. Applying R, then T, then R gives successively

```text
(E+CM,-M),
(E,-M-C^t E),
((I-CC^t)E-CM, M+C^t E),
```

whose last line is T^-1(E,M). Thus RTR=T^-1. Direct substitution also gives

```text
H(R(E,M)) = ||E+CM||^2+||M||^2-(E+CM)^t CM
          = H(E,M).
```

R is therefore an integral energy-preserving reversing involution,
independently of whether H is positive, semidefinite, or indefinite.

If a declared divergence matrix D satisfies DC=0, then both T and R
preserve DE. Their inverses do as well, so each actual Gauss sector
{(E,M) in Z^d : DE=rho} is invariant. The growing initial states in
Sections 4 and 5 have E_0=0; hence their complete orbits also lie in the
zero-divergence sector whenever DC=0. These are algebraic field-reversal
and charge-retention statements, with no physical time-reversal,
interaction, or cross-layer conclusion.
