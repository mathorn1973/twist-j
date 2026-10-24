# Finite integer field window and integral Phi5 carrier

PUBLIC / NON-CANONICAL. Action layer: L1. Authority: none.
Self-contained proof candidate for C-FIELD-CYCLOTOMIC-WINDOW-AUDIT-N.
Adapted from the public predecessor PROOF.md at
ff603881d1c297a6bbb63f88df455a4b4bf3ea74, with its inherited statements
and construction certificates explicitly retained. These exposed arguments
are audited anew; they are not newly discovered targets. The predecessor's
primary remains failed. Execution outcomes belong to this package's RUN
and RESULT; no mathematical text substitutes for a successful run.

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

## 9. The selected multigraph and full integral carrier

Use vertices (0,1,2) and ordered oriented edges
(e0,e1,e2,e3)=(0->1,0->1,0->2,2->1). The first two are distinct parallel
edges. This is a multigraph with a digon and a triangle, not a simple graph.
Order the faces c0=e0-e1, c1=-e0+e2+e3. With + at the tail and - at the head,

```text
C = [[ 1,-1],     D = [[ 1, 1, 1, 0],
     [-1, 0],          [-1,-1, 0,-1],
     [ 0, 1],          [ 0, 0,-1, 1]],
     [ 0, 1]],
G = C^t C = [[2,-1],[-1,3]],     DC=0.
```

No minimality or uniqueness claim is needed. The eigenvalues of G are
(5-sqrt(5))/2 and (5+sqrt(5))/2, both strictly between zero and four.
Thus the full six-coordinate energy is positive definite. In raw order
(E0,E1,E2,E3,M0,M1), the integer matrices are

```text
T = [[ 1, 0, 0, 0, 1,-1],
     [ 0, 1, 0, 0,-1, 0],
     [ 0, 0, 1, 0, 0, 1],
     [ 0, 0, 0, 1, 0, 1],
     [-1, 1, 0, 0,-1, 1],
     [ 1, 0,-1,-1, 1,-2]],

T^-1 = [[-1, 1, 1, 1,-1, 1],
        [ 1, 0, 0, 0, 1, 0],
        [ 1, 0, 0,-1, 0,-1],
        [ 1, 0,-1, 0, 0,-1],
        [ 1,-1, 0, 0, 1, 0],
        [-1, 0, 1, 1, 0, 1]].
```

These follow from the two shears, so both products are identity without any
spectral assumption. The full energy bilinear matrix is
B_raw=[[2I4,C],[C^t,2I2]], with H(z)=z^t B_raw z/2. This convention keeps
B integral; its adjoint agrees with that for H's polarized form B/2.

## 10. Saturated active lattice, action and actual module map

Define the embedding P and extraction F by

```text
P(a,b,c,d)=(a-b,-a,b,b,c,d),
F(E0,E1,E2,E3,M0,M1)=(-E1,E2,M0,M1),

P = [[1,-1,0,0],[-1,0,0,0],[0,1,0,0],[0,1,0,0],
     [0,0,1,0],[0,0,0,1]],      FP=I4.
```

The active rational space is im_Q(C) in the electric entries and Q^2 in
the magnetic entries. On it the induced action and its inverse are

```text
A = T_act = [[ 1, 0, 1, 0],      A^-1 = [[-1, 1,-1, 0],
             [ 0, 1, 0, 1],               [ 1,-2, 0,-1],
             [-2, 1,-1, 1],               [ 2,-1, 1, 0],
             [ 1,-3, 1,-2]],              [-1, 3, 0, 1]].
```

Indeed TP=PA. The energy restricted to these integer coordinates is

```text
H(a,b,c,d)=2a^2-2ab+3b^2+c^2+d^2+2ac-ad-bc+3bd,
B=P^t B_raw P = [[ 4,-2, 2,-1],
                 [-2, 6,-1, 3],
                 [ 2,-1, 2, 0],
                 [-1, 3, 0, 2]],     H=x^t B x/2.
```

This is the actual inherited energy, not a Euclidean substitute. Its leading
principal minors are 4,20,20,5, and A^t B A=B.

An explicit cyclic module map is available. Set w=(0,0,1,0) and take the
columns w,Aw,A^2w,A^3w:

```text
K = [[0, 1, 0, 0],        K^-1 = [[2,-2,1,-1],
     [0, 0, 1,-1],                [1, 0,0, 0],
     [1,-1, 0,-1],                [1,-1,0,-1],
     [0, 1,-2, 1]],               [1,-2,0,-1]],

Z = [[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]],
det K=-1,       AK=KZ.
```

Multiplication of the displayed matrices verifies the inverse and
intertwining. Z is multiplication by t in the basis (1,t,t^2,t^3) of
Z[t]/(1+t+t^2+t^3+t^4). It follows that Phi5(A)=0, A^5=I, and A has
exact order five since A!=I. This is an actual integral module isomorphism:

```text
sum_(j=0)^3 q_j zeta5^j  -> P K(q0,q1,q2,q3),
inverse on the raw active lattice: K^-1 F.
```

The choice is t=zeta5 with A acting by that generator. Another orientation
or Galois choice would need an explicit changed map. The module statement
does not follow merely from matching characteristic polynomials. It also
does not claim the already canonical generic J/cyclotomic bridge is new;
the new datum here is its map into this particular field lattice and energy.

To identify the lattice in the question exactly, take static columns

```text
S = [[1,0],[1,0],[0,1],[1,-1],[0,0],[0,0]].
```

They solve C^t E=0 and M=0, and TS=S. The six columns [P,S] are independent
(their determinant has absolute value five). Phi5(T) kills P and equals 5I
on S. Hence ker_Q Phi5(T)=im_Q P. If Px is integral for rational x, then
x=F(Px) is integral. Thus

```text
Lambda_act = ker_Q Phi5(T) intersect Z^6 = P Z^4,
```

and P is saturated, with no suppressed sublattice index. Likewise every
static integer vector has E0=E1=u, E2=v, E3=u-v, M=0 and is S(u,v),
so S is saturated. Doubling one P column would preserve its rational span
but produce index two; the independent control explicitly rejects that move.

In the active coordinates,

```text
J_act=I+A^2 = [[ 0, 1, 0, 1],
              [ 1,-1, 1,-1],
              [ 1,-3, 1,-2],
              [-3, 4,-2, 3]].
```

The module map identifies it with the already-given 1+zeta5^2.
Its characteristic polynomial is Phi5(x-1)=x^4-3x^3+4x^2-2x+1, since
squaring permutes the four primitive fifth roots. Trace is three and
determinant is one. Its integral inverse is -A-A^2. It is not an energy
isometry: x=(1,0,0,0) has H=2 while H(J_act x)=3. The finite-order time
step is A; the integer unit J_act is a different map.

## 11. Integral gluing and fixed-divergence sectors

Let W=[P,S], and write rational coordinates as (a,b,c,d,u,v). Directly,

```text
W^-1 = [[ 2/5,-3/5, 1/5, 1/5,0,0],
        [-1/5,-1/5, 2/5, 2/5,0,0],
        [   0,   0,   0,   0,1,0],
        [   0,   0,   0,   0,0,1],
        [ 2/5, 2/5, 1/5, 1/5,0,0],
        [ 1/5, 1/5, 3/5,-2/5,0,0]].
```

One can verify this by solving E0=a-b+u, E1=-a+u, E2=b+v,
E3=b+u-v. For integer raw states all six coordinates are integral iff

```text
g(E)=2E0-3E1+E2+E3=0 mod5.
```

Each numerator in W^-1 is either this residue or its scalar multiple
modulo five. The map g:Z^6->Z/5 is surjective (the E2 coefficient is one),
and its kernel is PZ^4+SZ^2. Thus the full gluing quotient is Z/5, not an
integral direct sum decomposition of all Z^6.

The actual charges rho=DE satisfy rho0+rho1+rho2=0 and

```text
rho0=E0+E1+E2, rho1=-E0-E1-E3, rho2=-E2+E3,
g(E)=2rho0+rho2 mod5.
```

Every integer zero-sum charge is realizable: for example
(E0,E1,E2,E3)=(rho0,0,0,rho2) has that charge. Two electric fields with
the same charge differ by C Z^2, because DE=0 implies
E3=E2 and E0=-E1-E2, exactly the two C columns.
Consequently each fixed-divergence sector is an affine active integer
lattice. Its unique orthogonal static part is fixed by rho, but it is
integer precisely when 2rho0+rho2=0 mod5. In the other four charge residue
classes the static part and the active part are both rationally glued;
replacing them independently by integers would lose actual ambient states.
Explicitly the static coordinates are u=(2rho0+rho2)/5 and
v=(rho0-2rho2)/5, obtained by solving D S(u,v)=rho.

The static Gram is S_E^t S_E=[[3,-1],[-1,2]]. For rational coordinates,

```text
H(Px+Ss)=H_act(x)+s^t [[3,-1],[-1,2]] s.
```

Orthogonality follows from C^t S_E=0, also cancelling the magnetic cross
term. Thus each charge sector has an affine active origin selected by its
rational static part. No unrecorded integral projection is available.

## 12. L5 energy and exact Smith/Hermite/image certificates

On Lambda_act only, define L=(I-A)(I-A^2). Exact multiplication gives

```text
L = [[ 1,-3,-1,-2],       N=A^2 L = [[ 1, 2, 1, 2],
     [-3, 4,-2, 1],                  [ 2,-1, 2,-1],
     [ 0, 5, 1, 2],                  [ 0,-5, 1,-3],
     [ 5,-5, 2,-1]],                 [-5, 5,-3, 4]].
```

All these are identities in the module Z[t]/Phi5. L commutes with A.
Reducing (1-t)^2(1-t^2)^2 modulo Phi5 gives 5t^3. Therefore

```text
L^2=5A^3,       NL=LN=5I,       L^-1=N/5 over Q.
```

Because A is an isometry of B, A^*=A^-1 for *=B^-1 (transpose) B.
Hence L^*=(I-A^-2)(I-A^-1)=A^-3 L=A^2 L=N. It follows that

```text
L^* L=5I,        L^t B L=5B,        H(Lx)=5H(x).
```

The ordinary transpose does not have this property: for example the
Euclidean squared norm of the first L column is 35 rather than five.
Finally det(I-A)=Phi5(1)=5 and det(I-A^2)=5, since A^2 has the same
primitive fifth-root spectrum. Thus det L=25, with positive sign.

A constructive column Hermite certificate is

```text
V_H = [[ 1, 1, 1, 1],      H_L = [[5,3,0,0],
       [ 2, 1, 2, 1],             [0,1,0,0],
       [ 0,-1, 1, 0],             [0,0,5,3],
       [-5,-2,-3,-1]],            [0,0,0,1]],
L V_H=H_L,      det V_H=1.
```

The equality is direct; the determinant also follows from det H_L=det L=25.
Thus H_L and L generate the same integer lattice. The displayed upper
triangular form has positive diagonal and reduced residues above each
row's diagonal (3 is between zero and 5).

For an explicit Smith certificate, put

```text
U = [[0, 1,0, 0],          V = [[ 1, 1, 1, 1],
     [0, 0,0, 1],               [ 1, 1, 2, 2],
     [1,-3,0, 0],               [-1, 0, 0, 1],
     [0, 0,1,-3]],              [-2,-1,-5,-3]].
U L V=diag(1,1,5,5),       |det U|=|det V|=1.
```

This can be checked without a Smith algorithm: subtract three times row
two from row one and three times row four from row three of H_L, obtaining
diag(5,1,5,1), then permute rows and columns in order (2,4,1,3).
These are unimodular operations. The determinantal-divisor certificate is
1,1,1,5,25, consistent with this Smith form.

Consequently, for every integer y=(a,b,c,d), not merely a bounded test box,

```text
y in L Z^4  iff  a+2b=0 mod5 AND c+2d=0 mod5,
Lambda_act / L Lambda_act ~= (Z/5Z)^2.
```

Necessity and sufficiency follow at once from H_L's columns: its unique
coefficient vector is ((a-3b)/5,b,(c-3d)/5,d). Equivalently every entry
of Ny is divisible by five. The executable exact interface is

```python
def admit_and_invert(a, b, c, d):
    if (a + 2*b) % 5 or (c + 2*d) % 5:
        raise ValueError("outside L5 image")
    numerators = (a + 2*b + c + 2*d,
                  2*a - b + 2*c - d,
                  -5*b + c - 3*d,
                  -5*a + 5*b - 3*c + 4*d)
    return tuple(n // 5 for n in numerators)
```

This is the algebraic interface for the new preregistered audit. Its
two modular checks make every division exact. The predecessor's failed
primary is preserved separately and is not this implementation.
L is a total injective integer map, and this inverse is total only on its
image. The quotient residues are a canonical admission record in the
selected coordinates; invertible inputs need no additional hidden residue.

Whole-shell surjectivity is false already for H=1 to H=5. The vector
y=(0,0,1,-2) has H(y)=5, but c+2d=-3 is not divisible by five and
Ny=(-3,4,7,-11). Thus it has no integer preimage. Meanwhile w=(0,0,1,0)
has H=1 and Lw has H=5. The actual bijection is

```text
{x:H(x)=h} -> {y in L Z^4:H(y)=5h}.
```

No shell enumeration was used or is claimed. An integer unit J, finite
rotation A, image index 25 and energy multiplier five are distinct facts;
none of these numbers is a waiting time, decay exponent or barrier length.

## 13. Full-space obstruction and the Gauss-compatible domain

Since T acts by A on P and by identity on S, T^5=I on the full space but
Phi5(T) is nonzero there. The rational static projector is

```text
P_s=Phi5(T)/5 = (1/5) [[2,2, 1, 1,0,0],
                       [2,2, 1, 1,0,0],
                       [1,1, 3,-2,0,0],
                       [1,1,-2, 3,0,0],
                       [0,0, 0, 0,0,0],
                       [0,0, 0, 0,0,0]].
```

It is a projector by its action on the rational direct sum. Define
L_raw=(I-T)(I-T^2), an integer polynomial in T. It restricts to L on P
but annihilates S. For example s=(1,1,0,1,0,0) has H=3 and
DE=(2,-3,1), while L_raw s=0. Thus L_raw is neither injective nor a
full-space energy similitude and cannot preserve general nonzero charges.
In fact [D,0]L_raw=0, as [D,0]T=[D,0].

The unique rational linear map equal to L on active vectors and identity
on static vectors is

```text
L_tilde = L_raw + P_s.
```

It preserves the actual D-divergence, but on the raw integer basis vector
e0=(1,0,0,0,0,0) gives

```text
L_tilde e0=(17/5,-3/5,-9/5,-9/5,-1,3).
```

Therefore it is not an integer operation on the full carrier. Because
L_raw is integral, L_tilde z is integral exactly when P_s z is integral,
namely on the index-five domain PZ^4+SZ^2, equivalently the sectors
2rho0+rho2=0 mod5. On that domain it is injective and preserves charges;
its image consists of active parts in LZ^4 and arbitrary integer static
parts. Its inverse uses the same admission test after integral splitting.
In raw notation its image is P L Z^4 + S Z^2: inverse admission first
requires the integral split, then both congruences on the active coordinates.
Its energy law is

```text
H(L_tilde(Px+Ss))=5H_act(x)+H_static(s),
Delta H=4H_act(x),
```

not five times the entire charged-state energy. On zero-divergence states
the static part is zero and all of Lambda_act is available. Other affine
sector constructions would need a separately chosen integer origin and
their own energy proof; the failed rational extension is not a theorem
that every possible charge-preserving construction is impossible.

## 14. Exposed predecessor regressions and successor scope

The predecessor's frozen primary used the false shortcut
a+2b=0 AND 3a-b+c-d=0 modulo five. It wrongly admits y=(0,0,1,1),
although Ny=(3,1,-2,1) is not divisible by five. Its unreached assertion
that (0,0,1,2) is an H=5 nonmember is also false, because
L(1,0,-1,1)=(0,0,1,2) and H(1,0,-1,1)=1.
Both defects remain visible at the predecessor's immutable public pin.

This separately named successor freezes the correct Section 12 predicate
and all three regression witnesses before any new execution. Its primary
is an explicitly attributed adaptation, while its new challenge is written
without access to either primary, the old breaker, proof or outputs before
the joint source pin. The literal success-output target is prospective.
Only unchanged repository runner readback may establish its subsequent
execution outcome. RUN/RESULT distinguish proof, implementation independence
with exposed targets, same-architecture replay and the public computation
gate. No old failure is converted into success by these arguments.

## 15. Exact interface and construction-choice account

The input/output carrier for the proved injection is PZ^4, read locally
from four edge registers and two face registers in the selected finite
multigraph. Raw active admission is P F z=z, equivalently E2=E3 and
E0+E1+E2=0. Extraction alone does not admit arbitrary raw inputs.
On admission, F extracts its four integer coordinates and P
embeds the output back without loss. Its D charge is zero and is retained.
On the larger integral-split charged domain of Section 13 the static field
and actual node charges are retained separately. Its charge-residue
admission is an additional condition, not an automatic projection.

A forward operation applies L to every active x, changing h to 5h.
A reverse operation is available only on the two-congruence image and
changes 5h to h, releasing exactly 4h. Because the inverse recovers the
entire active vector, no phase information is discarded inside this
interface. A many-state reaction would still need disjoint branch labels,
a rule for which branch is enabled, and the matter/resource state needed
to recover that choice. Rejecting nonmembers must be part of that law;
rounding Ny/5 is not an inverse. Neither map is installed here as a global
many-to-one update.

All operations access only this fixed cell's registers; no coupling between
cells, macrostep locality bound for a composed machine, useful transport or
coercivity of a replicated incidence has been proved. This finite access
statement supplies no new physical
spatial dimension or speed. A future coupling must list its full substep
access, retained records, charge transfers, nonnegative funding and inverse.

| ingredient | inherited or proved conditional | remaining choice |
| --- | --- | --- |
| native U versus extended state | existing Canon separates the laws | this field is a declared architecture, not derived from U |
| incidence | exact DC=0 and stable G for the displayed graph | multigraph, edge/face orientation and support are selected |
| energy | inherited H and proved positivity/similitude | physical energy interpretation and matter metric are not selected |
| field order | electric-first step, exact period and reversal | other schedules are outside scope |
| cyclotomic marking | explicit K and inverse; J is the given unit | seed, orientation and Galois marking are stated choices |
| L5 | exact image, inverse and energy difference | reaction branches and resource bookkeeping are additional architecture |
| preparation/reader | exact raw coordinates and charge admission | actual preparation, detector, permanent record and reset remain open |

At h=1 the release is four units. The inherited R18->A20 channel consumes
two, so simply replacing the triangle conversion leaves two units
unaccounted for. A later complete law must retain that remainder explicitly.
No part of this candidate discharges QDD-INSTRUMENT-APPARATUS,
QDD-TERMINAL-EVENT-SEMANTICS or PHOTON-MASSLESS-PHASE, or any other live
H/O obligation. Any promotion is a separate reviewed fold. A coupling is a separately
scoped successor with a complete resource and inverse contract, never an
operation implicitly installed by this proof candidate.
