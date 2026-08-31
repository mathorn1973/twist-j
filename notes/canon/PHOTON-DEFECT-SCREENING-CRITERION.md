# Photon defect screening: exact identities and a diagonal nonsummability criterion

Status: `NON-CANONICAL / RESULT-EXPOSED / CONDITIONAL MODEL / NO FORMAL RUN`.

Date: 2026-08-31.

Identity: `P-PHOTON-DEFECT-SCREENING-CRITERION-1`.
Notes claim: [issue #714](https://github.com/mathorn1973/twist-j/issues/714).

This original mathematical proof note concerns the explicitly selected model
of the [Born-current observable lemma](PHOTON-BORN-CURRENT-OBSERVABLE-LEMMA.md),
merged in [PR #712](https://github.com/mathorn1973/twist-j/pull/712). It is not a Canon adoption,
formal preregistration, verifier, pin or run. Its strict screening estimate
is a sufficient condition which has **not** been proved for that model.

Public reference: main `5376a2b2692aae2061b2fbecd978d8ed7158a03e`, Public
Canon v72; content `aac8a3a4aff027beb2b08edbde1ae8e59224914c`; tag target
`0bc7a623627c4453cc94515ae92880ec75ae7d94`. Both photon successor roots
remain open. No new scientific status follows from this note.

Layer scope: conditional L4 action/support and L6 state/observable
mathematics. `GATE-L4-L6-PHOTON-MASSLESS-PHASE` remains open; this note
neither adopts that cross-layer reading nor supplies its missing phase
estimate. Formal verifier and reproduction: NOT APPLICABLE to this
notes-only analytic result. No formal gate was executed.

## 1. Conditional model, observables and exact contact input

Use finite free cubical boxes K in Z^4, positive coordinate orientations,
the ordinary cell pairing, coboundary d and its adjoint boundary partial.
The selected primal and character measures are

```text
A in C^1(K;Z_5),       q=dA,
mu_K(A) proportional to product_p W(q_p),
W(q)=2+2 cos(2 pi q/5),

n in {-1,0,1}^P,       partial n=0 modulo 5,
nu_K(n) proportional to 2^(-|supp n|).
```

All boundary edges are summed with normalized Z_5 Haar measure; no gauge
quotient is taken. The real-source extension is specifically
W(theta)=2+2 cos(theta). Define

```text
X_p=sin(2 pi q_p/5)/(1+cos(2 pi q_p/5)),
kappa=tan(pi/5),       G=X/kappa,
j=partial n/5.
```

These are bounded, real, zero-mean fields. Zero means follow from charge
conjugation. The previously written finite character-expansion and
source-differentiation proof gives, on plaquette indices,

```text
C_X+C_n=D,
D_pp=1-E_nu n_p^2=(1+E_mu X_p^2)/2,
1/2<=D_pp<=1.                                                (CONTACT)
```

Covariance here is E[YZ]-E[Y]E[Z] for real variables. The two measures are
paired, not identified. Neither the product action nor the source coupling
is forced by the five untwisted Canon weights. All subsequent conclusions
are conditional on this model choice.

## 2. Defect-inclusive Ward identity

Let B=partial_2, the incidence matrix from plaquettes to edges. Since
Bn=5j, multiplying (CONTACT) by B and B^T gives

```text
B C_X B^T+25 C_j=B D B^T.                                   (WARD)
```

For every real finite edge cochain f this says

```text
Var_mu(<df,X>)+25 Var_nu(<f,j>)
  =sum_p (1-E_nu n_p^2)(df)_p^2.
```

Consequently 0<=25 C_j<=B D B^T<=B B^T as quadratic forms. This is an
upper bound, not a strict infrared screening estimate.

The exact finite source identity also gives

```text
Z(df)/Z(0)=E_nu exp(i5<j,f>).
```

The right side equals one when f is (2 pi/5) times an integer cochain.
It need not equal one for arbitrary real f. Making that replacement would
impose continuous exact-source invariance and delete the defect ensemble:
second derivatives would force every Var(<f,j>)=0, hence j=0 almost surely
by the zero means. The positive-weight 21-face witness excludes this in
finite volume. Closure modulo five is not integer closure.

## 3. Existence of a stationary fully hypercubic paired state

This existence statement does not require a phase estimate. Let K_L be
the centered box [-L,L]^4 with all its cells, and let
F_L={-floor(L/2),...,floor(L/2)}^4. Extend finite edge and character
configurations by zero to the respective countable finite-alphabet product
spaces. On the extended edge field continue to define q=dA and X locally;
contact identities at the artificial boundary need not hold before limits.

Let H be all 384 signed coordinate permutations in dimension four. Their
cell action includes orientation signs and the bounded anchoring shifts
which return a reflected cell to positive orientation. Apply the same
averaging scheme to both marginal laws:

```text
bar_mu_L=(1/|H|)sum_g g_*[(1/|F_L|)sum_(x in F_L) tau_x*mu_KL],
bar_nu_L=(1/|H|)sum_g g_*[(1/|F_L|)sum_(x in F_L) tau_x*nu_KL].
```

For every fixed finite cell set, all translated/transformed cells needed
by its observables lie inside the source box for sufficiently large L.
The growing margin L/2 dominates the fixed cell diameters and anchoring
shifts. Thus each fixed local contact identity and finite-support Ward
identity holds term by term in these averages eventually.

Every marginal in each mixture has zero means by charge conjugation.
Covariance of the mixture is therefore exactly the mixture of covariances;
there is no covariance-of-means correction. D averages linearly as well.

Both averages are exactly H-invariant. For a fixed translation h, their
change in total variation is bounded by the finite average over g in H of

```text
|F_L symmetric_difference (F_L+g^(-1)h)|/|F_L| -> 0.
```

The convergence follows by counting fixed-width boundary strips. A common
diagonal subsequence makes all cylinder probabilities in both spaces
converge. Consistency is preserved, and the countable-product extension
theorem supplies limiting probability laws (mu,nu). The variation bound
and finite-group invariance pass to cylinder events. Hence both limits
are stationary and fully H-invariant, and all bounded local identities
above persist. Pairing means this common construction, not a coupling or
identification of the two random fields.

This constructs a limit of averaged finite-volume measures. It does not
claim an unaveraged free-box subsequential limit, uniqueness or a Gibbs
property. The local constraints q=dA modulo five and partial n=0 modulo
five pass to the limit. Thus j=partial n/5 exists locally and partial j=0.

Transitivity on the six coordinate plaquette orientations gives a common
constant d=1-E_nu n_p^2 in [1/2,1]. With a,b denoting orientations and x
the displacement of anchors, the limiting contact identity is

```text
C_X(ab;x)+C_n(ab;x)=d delta_ab delta_(x,0).                    (1)
```

## 4. Unconditional bounded spectral densities from positivity

No absolute covariance summability is needed in this section. For Y=X or n
put C_Y(ab;x)=E[Y_a(0)Y_b(x)]. For a finitely supported complex test field f,
use Y(f)=sum_(x,a) conjugate(f_a(x))Y_a(x). Positivity and (1) imply

```text
0<=E|n(f)|^2<=d||f||_2^2,
0<=E|X(f)|^2<=d||f||_2^2,
E|n(f)|^2+E|X(f)|^2=d||f||_2^2.                              (2)
```

Polarization and bounded-form representation extend these forms uniquely
to positive bounded operators T_n,T_X on l2(Z^4;C^6), with
0<=T_n,T_X<=dI and T_n+T_X=dI. Stationarity makes them commute with lattice
translations. On finitely supported inputs their covariance convention is

```text
(T_Y f)_a(x)=sum_(y,b) C_Y(ab;y-x) f_b(y).
```

Let U be the unitary discrete Fourier transform with
(Uf)(q)=sum_x exp(-i<q,x>)f(x), using normalized Haar measure
dm(q)=(2 pi)^(-4)dq on the torus. Plancherel identifies l2 with
L2(T^4;C^6). The operator A_Y=U T_Y U^* commutes with multiplication by
every coordinate character, hence every trigonometric polynomial.

Here is an elementary multiplier argument. Bounded Fejer approximations
to an indicator 1_E converge in L2 and give strong convergence of the
corresponding multiplication operators. The latter follows first on
bounded functions and then on all L2 by truncation and the uniform bound.
Thus A_Y commutes with every indicator multiplier and then every bounded
measurable scalar multiplier. Let its matrix columns be A_Y applied to the
six constant coordinate vectors. For bounded scalar functions h,
A_Y(h e_b)=h A_Y(e_b), so A_Y acts as multiplication by a measurable
matrix S_Y on bounded simple vector fields. Applying (2) to 1_E times
each vector in a countable dense subset of C^6 gives, almost everywhere,

```text
0<=S_n(q)<=dI_6,
0<=S_X(q)<=dI_6,
S_n(q)+S_X(q)=dI_6.                                         (3)
```

Indeed an integrated violation on some E would contradict the operator
inequality; the dense vector set fixes a common null set. Boundedness then
extends the multiplication representation to all L2. This proves directly
that the covariance spectra have bounded, absolutely continuous matrix
densities; no general spectral-measure theorem or assumed density is used.

The sign convention is fixed by the recovered coefficients:

```text
C_Y(ab;x)=integral exp(-i<q,x>) S_Y(ab;q) dm(q).              (4)
```

If covariance is absolutely summable, its continuous Fourier series is
sum_x exp(i<q,x>)C_Y(x), agreeing with S_Y almost everywhere. Densities
without that hypothesis are equivalence classes, not assigned values at
q=0. One must not infer continuity merely from their boundedness.

There are already unconditional quantitative consequences. Parseval and
S_n^2<=d S_n give, for every orientation a,

```text
sum_(x,b)|C_n(ab;x)|^2<=d E n_a^2=d(1-d)<=1/4,
sum_(x,b)|C_X(ab;x)|^2<=d E X_a^2=d(2d-1).                   (5)
```

Also every covariance entry tends to zero as |x| tends to infinity: the
bounded density is in L1, and approximation by trigonometric polynomials
proves its Fourier coefficients vanish. This is two-point decorrelation
without a rate, not absolute summability, a mass gap, or masslessness.

## 5. Defect densities and exact exterior projectors

Define the score defect rho=d_2 X. It is a three-cochain, while j is a
one-chain. Their conservation identities are d rho=0 and partial j=0.
Let

```text
a_i(q)=exp(iq_i)-1,
lambda(q)=sum_i |a_i(q)|^2=sum_i(2-2 cos q_i),
E_r(q):Lambda^r C^4 -> Lambda^(r+1) C^4,    E_r u=a(q) wedge u.
```

With convention (4), a forward difference has multiplier a_i(q), not its
conjugate. Boundary has the adjoint symbol. Finite differences of the
bounded covariance operators therefore give the following densities
unconditionally, almost everywhere:

```text
S_j=(1/25) E_1^* S_n E_1,
S_rho=E_2 S_X E_2^*.                                       (6)
```

The field transformation is on the left and its adjoint on the right;
there is no additional transpose or Fourier-sign reversal in (6).

For q!=0 modulo 2 pi set

```text
P=E_1 E_1^*/lambda,
Q=E_2^* E_2/lambda.
```

These are complementary orthogonal rank-three projectors on Lambda^2 C^4:

```text
P+Q=I_6,       PQ=0,       P^2=P=P^*,       Q^2=Q=Q^*.
```

To verify this, send a/sqrt(lambda) to the first unit basis vector by a
unitary transformation. Exact two-forms are e_1 wedge C^3 and their
orthogonal complement is Lambda^2 C^3; both have dimension three. The
wedge/contraction compositions act as the corresponding projections.

Trace cyclicity and (3) now give the exact almost-everywhere identity

```text
R(q):=[25 tr S_j(q)+tr S_rho(q)]/lambda(q)
    =tr(P S_n)+tr(Q S_X)
    =3d+tr((P-Q)S_n).                                      (7)
```

In particular 0<=R<=6d. Separately each of the two trace terms is between
zero and 3d, and ||S_j||<=d lambda/25, ||S_rho||<=d lambda. These bounds
give almost-everywhere meaning to R with no defect l1 hypothesis. They
are not the strict estimate required below.

## 6. The full-row necessary condition and the role of reflections

Suppose first that every entry of C_n is absolutely summable over Z^4.
Its Fourier series F_n is continuous and equals S_n almost everywhere.
The hypercubic covariance transformation includes the exterior-square
signed permutation together with phase factors from cell anchoring. At
q=0 those phases equal one. Thus F_n(0) commutes with the full signed
coordinate group on Lambda^2 R^4.

A coordinate reflection acts on e_i wedge e_j by epsilon_i epsilon_j.
Different pairs have different sign characters, so a suitable reflection
forces each off-diagonal matrix entry to zero. Coordinate permutations
then make all six diagonal entries equal. Therefore F_n(0)=c I_6 with
0<=c<=d. Reflections are essential: orientation-preserving symmetry alone
does not remove the four-dimensional self-dual/anti-self-dual distinction.

Since tr(P-Q)=0 and ||P-Q||=1,

```text
|R(q)-3d|<=6||F_n(q)-cI_6|| -> 0                            (8)
```

for the continuous representative away from zero, and hence in essential
limit for the almost-everywhere density. No direction-independent limit
of P or Q is asserted.

Thus full covariance-row l1 would require ess-lim R=3d. Failure of this
condition gives a nonsummable orientation row. That observation alone
does not generally locate the failure in a same-orientation covariance.

## 7. Stronger result: a uniform essential gap forces diagonal nonsummability

In fact the strict uniform screening condition is stronger. Assume only
that the six diagonal kernels C_n(aa;x) are absolutely summable. Their
continuous Fourier series f_a(q) equal the diagonal entries of S_n almost
everywhere. Symmetry transports same-component covariances without an
anchoring offset in their relative displacement. Hence f_a(0)=c is the
same number for every orientation a. No continuity of off-diagonal
entries is assumed or needed.

Let P_1 be the diagonal projector onto the three coordinate two-forms
containing index 1, and Q_1=I-P_1. For q near the first coordinate axis,
P(q) approaches P_1 as the direction of a(q) approaches that axis. The
phase of its first component does not affect the projector. Since
||S_n||<=d, (7) implies, almost everywhere,

```text
|R(q)-3d|
 <=6 max_a |f_a(q)-c| +12d ||P(q)-P_1||.                    (9)
```

The first term tends uniformly to zero in a shrinking ball. For the
second, restrict to the cone

```text
0<|q|<r,        |a_perp(q)|<eta |a_1(q)|.
```

For every r>0 and eta>0 sufficiently small this contains an open set of
positive Haar measure. Wedge and contraction are continuous on the unit
sphere, so ||P-P_1|| tends uniformly to zero with eta on this cone. More
explicitly, after removing the phase of a_1, the unit vector a/|a| tends
uniformly to e_1; the product defining P changes in norm by at most twice
that vector distance.

For every delta>0, choose eta and then r so that the right side of (9)
is below delta on a positive-measure subset of every sufficiently small
ball. Removing a null set cannot remove that subset. Consequently

```text
diagonal l1 implies
  ess-limsup_(q->0,q!=0) R(q)>=3d,
  ess-liminf_(q->0,q!=0) R(q)<=3d.                          (10)
```

Essential limsup means the limit of the essential suprema over punctured
balls, with respect to Haar measure; similarly for essential liminf. No
pointwise value on a coordinate axis, a measure-zero set, is used.

Therefore either strict uniform condition

```text
ess-limsup_(q->0,q!=0) R(q)<3d,
or ess-liminf_(q->0,q!=0) R(q)>3d                           (GAP)
```

forces failure of diagonal absolute summability. Hyperoctahedral
transitivity gives the conclusion for every plaquette orientation a:

```text
sum_x |Cov_nu(n_a(0),n_a(x))|=infinity,
sum_x |Cov_mu(X_a(0),X_a(x))|=infinity,
sum_x |Cov_mu(G_a(0),G_a(x))|=infinity.                      (DIAGONAL)
```

The last two follow from the off-contact identity and fixed nonzero
normalization kappa. Thus this is a same-orientation conclusion, not merely
a divergent sum over mixed orientations. The lower screening test with
right side 3/2 is sufficient uniformly because d>=1/2.

The model has not been proved to satisfy (GAP). In particular the elementary
bound 0<=R<=6d does not imply its lower screening alternative.

## 8. Why mere off-diagonal discontinuity is insufficient

The distinction in the preceding section is substantive. At the level of
positive covariance operators, let A(q)=P(q)-diag(P(q)) and set

```text
d=2/3,        epsilon=d/8,
S_n=(d/2)I_6+epsilon A,
S_X=dI_6-S_n.
```

Since ||A||<=2, these are positive densities between zero and dI, with
the proper stationary reality and hypercubic covariance transformations.
Their diagonal densities are constant d/2, so every diagonal covariance
has support only at zero. The local diagonal identity is compatible with
d=1-d/2, which is why d=2/3 was chosen.

But P_(12,13)=a_2 conjugate(a_3)/lambda has different limits along
q=t(e_2+e_3) and q=t e_2, respectively 1/2 and zero. It has no continuous
representative at zero, so the corresponding off-diagonal covariance is
not l1. This example concerns covariance structure only: it is not claimed
to realize the Born Gibbs measure, its finite alphabet or its full gauge
constraints. It shows that positivity, symmetry and the contact identity
alone do not convert mixed-orientation nonsummability into diagonal
nonsummability. The positive-measure coordinate-cone argument is the
additional reason the uniform gap criterion yields (DIAGONAL).

## 9. Real-space second moments, with no additional matrix-density assumption

For an integrated real-space criterion it is enough to assume the
diagonal defect second-moment bound

```text
A2:=sum_x |x|^2 [25 sum_i |C_j(ii;x)|
                   +sum_(|a|=3)|C_rho(aa;x)|] <infinity.     (M2)
```

The origin terms are finite, so each diagonal defect kernel is also l1.
No off-diagonal defect l1 assumption is needed here. Define

```text
K(x)=25 sum_i C_j(ii;x)+sum_(|a|=3)C_rho(aa;x),
M=sum_x |x|^2 K(x),
T(q)=sum_x exp(i<q,x>)K(x).
```

T is continuous and agrees almost everywhere with
25 tr S_j+tr S_rho. The unconditional bounds in section 5 give
0<=T(q)<=6d lambda(q) almost everywhere; continuity makes this inequality
hold everywhere. In particular T(0)=sum_x K(x)=0. This avoids assigning
values at zero to a general measurable matrix density.

Stationarity gives K(-x)=K(x). Signed-coordinate symmetry gives K(gx)=K(x):
the anchoring shifts at the two endpoints of a same-component covariance
are identical and cancel; its orientation sign occurs twice. Thus

```text
T(q)=sum_x K(x)[cos(<q,x>)-1],
sum_x x_i x_j K(x)=delta_ij M/4.
```

Reflections eliminate the mixed moments and coordinate permutations equate
the four diagonal moments. Absolute second moments justify the expansion

```text
T(q)=-(M/8)|q|^2+o(|q|^2),
ess-lim_(q->0,q!=0) R(q)=-M/8.                             (11)
```

The remainder is uniform in direction: split into a finite displacement
set and a tail with arbitrarily small weighted absolute mass, use Taylor
only on the finite set, and use |cos u-1|<=u^2/2 on the tail. Finally
lambda(q)/|q|^2 tends to one. The factor 1/8 is 1/(2*4), with dimensionless
radian momenta and normalized Haar measure as fixed above; no 2 pi factor
or score normalization is missing. Positivity also gives M<=0.

Combining (11) with the diagonal necessary bounds (10) proves the stronger
necessary sum rule

```text
(M2) and diagonal l1 imply M=-24d.                         (SUM-RULE)
```

Thus any independently certified failure of that equality implies
(DIAGONAL). In particular -M<24d suffices. The stronger absolute estimate
A2<24d suffices too; replacing 24d by 12 is a sufficient uniform bound.
These estimates have not been established for the selected model.

## 10. Finite-block certificate and its indispensable errors

For a fixed finite displacement set B_R put

```text
M_R=sum_(x in B_R)|x|^2 K(x).
```

If an argument proves the infinite-tail estimate

```text
sum_(x outside B_R)|x|^2 [25 sum_i |C_j(ii;x)|
                       +sum_(|a|=3)|C_rho(aa;x)|] <=T_R,
```

then |M-M_R|<=T_R. Hence

```text
-M_R+T_R<24d                                              (BLOCK-TEST)
```

is an exact sufficient certificate for diagonal nonsummability. The
entries here belong to the constructed infinite-volume paired state.
Using finite-volume entries requires an additional proved error bound.
For example, if |M_R-M_R^finite|<=E_R and d>=d_lower is certified, the
sufficient test is -M_R^finite+E_R+T_R<24 d_lower.

A finite covariance table without the infinite-tail bound is not a
certificate. An observed small defect density or a local variance cannot
replace T_R or E_R. No simulation, table or numerical fit is supplied here.

## 11. The score defect includes the full-support correction

Let F=pr(q) have values (0,1,2,-2,-1), let m=dF/5, and define
H(q)=(0,0,1,-1,0). The exact score values give

```text
G=F+sqrt(5)H,
rho=dX=kappa[5m+sqrt(5)dH].                                (12)
```

This identity is on the full support of the selected W model. It is rho,
not dG, which occurs in R and M; its covariance includes kappa^2. Both the
dH contribution and its cross covariance with m must be controlled.
The character current j belongs to nu and is not identified with m.

The local bound E X_p^2<=1 implies
P_mu(|pr(q_p)|=2)<=1/(5+2 sqrt(5)). It does not bound the susceptibility or
second moments of dH, the complete rho, or the current j. Positive local
defect density neither proves nor disproves the required infrared gap.

## 12. Exact obstructions to four simple comparison shortcuts

These original calculations delimit specific representations or sufficient
tests. None is a no-go for all comparison arguments, all renormalization
methods, or masslessness. They explain why the strict estimate above has
not been supplied merely by local weights.

### 12.1 The logarithmic character cone

Write phi=(1+sqrt(5))/2 and theta_q=2 pi q/5. Orthogonality of the three
real even functions 1, cos(theta_q), cos(2 theta_q) on Z5 gives the unique
exact expansion

```text
log W(q)=c+beta1 cos(theta_q)+beta2 cos(2 theta_q),
c=(log 4)/5,
beta1=(2/5)log 4+(4 sqrt(5)/5)log phi,
beta2=(2/5)log 4-(4 sqrt(5)/5)log phi<0.
```

For the sign, 2 sqrt(5)>4 and phi^4=(7+3 sqrt(5))/2>4 imply
phi^(2 sqrt(5))>4. The coefficient follows directly from
cos(2 pi/5)-cos(4 pi/5)=sqrt(5)/2 and
W=(4,phi^2,phi^-2,phi^-2,phi^2), without fitting or interpolation.

Thus log W lies outside the cone whose nonconstant discrete character
coefficients are all nonnegative. A constant shift cannot change that;
character automorphisms only permute the nontrivial coefficients.
This excludes that particular sufficient log-character hypothesis, not
Ginibre inequalities in general. The coefficients of W itself are still
nonnegative. No monotonicity in those coefficients is proved here.

### 12.2 A replica kernel which is not a positive Gram kernel

For the selected continuous extension, and hence on the five-point group,

```text
K(theta,eta)=W(theta+eta)W(theta-eta)
            =4(cos(theta)+cos(eta))^2.
```

Addition, subtraction and division by two are valid on Z5. The principal
submatrix at arguments 0 and 2 pi/5 is

```text
[[16,phi^4],[phi^4,4 phi^-2]],
determinant=64 phi^-2-phi^8=(145-85 sqrt(5))/2<0.
```

The last sign follows by squaring the positive sides of 145<85 sqrt(5).
Therefore this pointwise nonnegative kernel is not positive semidefinite
on the actual discrete carrier. It cannot be a sum of kernels
c_l f_l(theta) conjugate(f_l(eta)) with c_l>=0, since every such sum has
positive semidefinite principal submatrices. This excludes only this
positive-Gram shortcut, not the replica change of variables or more
general correlation inequalities.

### 12.3 Fixed-weight convolution converges to Haar

Normalize Q=W/2=1+cos(theta) relative to Haar on either U(1) or Z5.
Its Fourier coefficients are 1 at zero, 1/2 at the two characters +/-1,
and zero elsewhere. Fourier coefficients multiply under convolution, so

```text
Q^{*m}(theta)=1+2^(1-m)cos(theta) -> 1
```

uniformly as the positive integer m tends to infinity. The limit is Haar,
not a nonconstant heat-kernel density at fixed positive finite inverse
temperature. In particular setting m=N^2 does not change this conclusion;
this N is a subdivision count, not the group order five.

For comparison, [Chevyrev and Garban, Villain Action in Lattice Gauge
Theory (2025)](https://doi.org/10.1007/s10955-025-03420-1), Theorem 1.5
and Assumption 2.1, use an N-dependent family whose N^2-fold convolution
converges to the prescribed Villain density. Keeping Q fixed fails that
convergence hypothesis. Their Corollary 1.6 concerns U(1) Villain-loop
monotonicity; it is not a phase theorem for the present fixed Z5 measure.
No source theorem is imported here. The displayed convolution calculation
is independent of that paper.

Changing the microscopic family or the group could be useful, but a
theorem-preserving comparison back to the selected model would still be
needed. Single-face convolution is not asserted to be an arbitrary
four-dimensional coarse-graining rule.

### 12.4 Bare current polymers fail a size-linear convergence test

In the exact partition sum

```text
Q_K=sum_{n in {-1,0,1}^P; partial n=0 mod5} 2^(-|supp n|),
```

join occupied plaquettes when they share an edge. Each connected support
component separately has boundary zero modulo five: any occupied faces
at the same edge belong to the same component. Define its activity z(gamma)
by summing 2^(-|gamma|) over its admissible sign assignments. Distinct
components are compatible precisely when their union has those separate
edge-adjacency components. This is an exact positive hard-core polymer
representation.

The six faces gamma_c of any elementary three-cube have exactly two
admissible assignments, its two oriented boundaries. Indeed at each
support edge two faces meet, so the signed sum in {-2,0,2} can vanish
modulo five only by vanishing over the integers; connectedness fixes all
signs from one face. Consequently z(gamma_c)=2*2^-6=1/32.

Choose c far enough from the box boundary. Each of its six faces belongs
to four elementary three-cubes in four dimensions, giving three other
cubes per face. These eighteen cubes are distinct: two distinct elementary
three-cubes cannot share two faces. Along with c itself they give nineteen
mutually relevant polymers incompatible with gamma_c; additional
edge-sharing neighbors only increase the sum.

Consider only the explicit size-linear Kotecky-Preiss sufficient test

```text
sum_{gamma incompatible with gamma0}
  z(gamma) exp(t |gamma|) <= t |gamma0|
for every gamma0, with one t>=0 and self-incompatibility included.
```

The nineteen cube boundaries alone would require
(19/32)exp(6t)<=6t. This is impossible: for x>=0,
x exp(-x)<=1/e<1/2<19/32. No cluster-expansion theorem is needed to
disprove the displayed numerical condition.

This does not prove divergence of the actual expansion or failure of
different weights, polymer groupings, stronger tests or multiscale methods.
It does show why the whole occupied-face ensemble cannot simply be declared
dilute in this representation. A charge-five defect expansion must control
the fluctuating integer-closed background.

More precisely, the exact sector weights are

```text
Q_{K,j}=sum_{partial n=5j} 2^(-|supp n|),
Q_K=sum_j Q_{K,j},          nu_K(j)=Q_{K,j}/Q_K.
```

The individual 21-face witness has weight 2^-21 relative to the empty
configuration. It is not an upper bound on Q_{K,j}/Q_{K,0}, a renormalized
defect activity, or an infinite-volume susceptibility. None of these four
obstructions supplies the missing bound on the complete j and rho channels.

## 13. Endpoint and limits of the result

For the explicitly selected model the construction of the symmetric pair,
bounded spectral densities, square-summable covariances, two-point
decorrelation, Ward identity, and defect/projector identities are proved
without a phase assumption. The diagonal nonsummability conclusion is
conditional on a further strict essential screening estimate or its
second-moment certificate. That missing inequality is a real analytical
obligation, not something supplied by positivity or finite alphabets.

Even satisfying it would establish the stated observable conclusion for
this selected model. It would not by itself adopt the model as TWIST-J,
close an exact external source-theorem chain at N=5, construct a continuum
propagator, identify polarizations, supply a temporal rule or cone map, or
prove a physical photon. PHOTON-MASSLESS-PHASE remains open. No Canon,
registry, evidence, gate or release changes follow from this proof note.
