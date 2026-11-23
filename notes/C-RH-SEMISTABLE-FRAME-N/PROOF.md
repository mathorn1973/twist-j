# Hecke blocks, periodization relations and quantitative concentration certificates

**NON-CANONICAL. No authority. No Canon status changes.**

Identifier: C-RH-SEMISTABLE-FRAME-N, also discussed as C-RH-BK-CONCENTRATION-N.
Session: ChatGPT-Astra-Sol-20261123-R8. Owner: A. M. Thorn.
Claim: [issue 2070](https://github.com/mathorn1973/twist-j/issues/2070).
Status of new mathematical deductions: **candidate-D**.
Status of the separately frozen finite audit: see RESULTS.md; at most
**candidate-C**, one architecture.

This note concerns finite-dimensional concentration and the automorphic maps
used in a proposed RH argument. It proves neither RH nor an unconditional
concentration estimate for those actual maps. The linear-algebra statements
below have complete paper proofs. The applications to Hida data retain the
source's realization, counting and convergence hypotheses. Source inspection
is not a Lean compilation.

## 1. Scope, notation and the exact source bridge

For maps A_u:E_u -> F over a field, let D=dim F>0 and R=sum dim E_u>0.
The normalized concentration defect is

    eps(A)=max_{W <= F} [sum_u dim A_u^{-1}(W)/R - dim W/D].

It is invariant under one common target isomorphism, separate source
isomorphisms, nonzero rescalings of the maps, and simultaneous field
conjugation. A target restriction is not an isomorphism.

The external source is frozen at riemann-hypothesis commit
40e56bab026552e089d7afcfeff08d2defb9c005. Current branch development is separate
from this pinned reading. All source links below refer to that commit.

There is a useful distinction between an arbitrary witness to MatS_at and
the witness actually constructed from the Poincare maps. In
TopDensityNGeSixteen.lean, PMat is defined using an orthonormal basis of the
**whole** D.s.HH:

    PMat(u)[a,j] = <f_a, D.s.Pu(u)(e_j)>.

The good-row orthonormal family is extended to this whole space.
blockReal_at_of builds the coordinate link from BesselId, and matK_at_of
chooses Bf(u)=PMat(u), possibly with one common complex conjugation, followed
by the source compression only in Ball(u)=Bf(u) Vr(u). Thus Bf itself is
the full uncompressed map. The supplementary rows of this chosen
witness are actual Poincare coefficients. They are not arbitrary.

An arbitrary existential MatS_at witness need not have that property.
Moreover, EE is generally the good-row space, not the whole HH. A fixed
SIso, whose Pu_eq intertwines all maps and whose target isometry is common
to all words, is required to transport the concrete Hida conclusions below
to abstract D.s.Pu and hence to this PMat witness. SConc explicitly carries
such an SIso; its existence is not proved by writing down the interface.

Source anchors: [PMat and its constructed witness](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean),
definitions PMat, BlockReal_at, matK_at_of, exists_rowBasis, blockReal_at_of;
[SIso and SConc](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ParametersTermRelations.lean).

## 2. A useful coarser decomposition: open one prime, retain the other

### 2.1 The full residue group has 2f factors

Put f=[F:Q]. Complete splitting gives one GL_k factor per conjugate pair of
places of E, not one factor per rational prime. The group fixing the reduced
hyperbolic frame and the distinguished vector is

    M = G_0 x G_1,       G_i = GL_k(F_{g_i})^f.

Writing just GL_k(F_{g_0}) x GL_k(F_{g_1}) is correct only for f=1 or for an
explicitly selected subgroup. The abstract block formulas remain valid;
the indexing of the actual full blocks must use all factors.

### 2.2 Exact source balance for either one-prime algebra

**Claim, candidate-D.** Assume the standard geometric Hida realization,
the stated integral frame at g, generic level characters, distinct completely
split primes g_0,g_1, and g_i-1>k at the retained prime. Keep the original
integral level away from g. At g_j replace the unipotent level by G_j, while
retaining the original (U_i,psi_i) condition at the other prime. More
precisely, let K_b have principal congruence level at g_j and let K_ext
enlarge that factor to G_j. The columns at K_b, with the retained
psi_i condition, carry the quotient action K_ext/K_b=G_j. It is this
space, before imposing (U_j,psi_j), that is a direct sum of regular G_j
representations. Consequently, for every word u, including zero columns,

    dim C_{u,alpha} = p_alpha dim C_u,
    p_alpha = dim(rho_alpha) dim(rho_alpha[psi_j]) / [G_j:U_j].

For the generic constituents of these finite general linear groups,
dim(rho_alpha[psi_j])=1. Non-generic constituents have zero weight.
The distribution p is independent of u. It is a statement about one-prime
blocks, not the joint distribution of the two prime labels.

Proof. Rational stabilizers of the enlarged compact level preserve a full
lattice and lie in a compact real group, hence have finite order. At the
retained split prime their reductions are unipotent. The kernel of reduction
is pro-g_i, so the stabilizer element has g_i-power order. If it were
nontrivial, a power would give an order-g_i matrix in dimension k over
Q_{g_i}. Its minimal polynomial contains Phi_{g_i}, which has degree g_i-1
over Q_{g_i}, by Eisenstein after translating its variable. This contradicts
g_i-1>k. Thus the rational stabilizers are trivial.

There is a necessary character normalization here. An arbitrary lift of a
G_j element can differ from another lift by an element carrying psi_i.
Choose lifts whose retained U_i component is the identity, or extend psi_i
to the enlarged level by projection and divide the lift action by this
character. The resulting quotient action is genuine, not projective.
The free finite-group orbits on the class set, with their coefficient
fibers, give regular representations. Applying the generic U_j projector
gives the formula by the regular-representation decomposition.

The standing inequalities m^4<=f<=k, b>=2 and g_i>=(kb)^8 imply g_i>4n
for n=k+m-1 in the source range, so the same argument can be used in
either direction. Source inputs and the finite class condition are retained.

### 2.3 The target has an exponentially small one-prime imbalance

**Claim, candidate-D, conditional on the universal counting inputs.**
On the same concrete Hida realization use the one-prime projector

    e_{N_j} e_{U_j} z_alpha

at g_j and keep the original projector at g_i. Here z_alpha is central in
the finite G_j algebra. This is a selfadjoint convolution idempotent:
G_j normalizes N_j and preserves its character, and z_alpha commutes with
e_{U_j}. Its support remains unipotent at the retained prime. After Haar
normalization and inflation it therefore satisfies IsAdmIdem, and its
identity value is p_alpha times that of the original projector.

The universal PointsLemma applies to these admissible tests, provided its
quantified CountData and numerical hypotheses hold for these data. In
particular one needs the counting input supplied conditionally by
points_bound_of_volumeCountGeometryConditions, with adm2, discrete-series
decay, LocalProjectorRealPlace, Conclusion2, DistTri, the geometry/count
conditions and the stated thresholds. The narrower PCount wrapper includes
an ambient centrality requirement. That requirement is not part of the
universal PointsLemma route used here.

The identification with the actual target is exact, not a comparison up
to an archimedean multiplicity. For each replaced finite convolution R_j,
RowsBij and finrank_HH_eq_Dcount identify Dcount(R_j) with the range of
R_j Rph. Commutation of finite and infinite actions and e_j<=e make this
range the required projected subspace p_j HH_X. The common formal degree
occurs in D_star and cancels in its ratios. RowsBij and CountData are part
of the realization/counting premises for the replacement tests.
More explicitly, they use the same Haar measure, fundamental domain, right
regular action, local unitary irreducible representations, formal degrees,
normalized vectors with integrable matrix coefficients, archimedean
operator integral, and Hilbert tensor realization. Only the finite
convolution projector and its IsRConvF witness change. With D_star>0 and
eta<1 the lower count bound also ensures finite dimensionality in the
source's finrank formulation.

For a common D_star>0 and eta=exp(-c n f log n)<1 this yields

    (1-eta) p_alpha D_star <= D_alpha <= (1+eta) p_alpha D_star.

Both directions are present in the pinned source, as dc_le_of_conC and
le_dc_of_conC. An earlier reading that considered only the upper bound
missed an available lower bound.

Writing q_alpha=D_alpha/sum D_beta and beta=TV(p,q), the sharp consequence is

    beta <= eta / (1+sqrt(1-eta^2)).

Proof of normalization. Put a=1-eta, b=1+eta and
t_alpha=D_alpha/(p_alpha D_star), on the positive support of p.
Then a<=t_alpha<=b and mu=sum p_alpha t_alpha. The chord of the convex
function |t-mu| bounds its expectation:

    TV(p,q) = E_p |t-mu|/(2mu)
            <= (b-mu)(mu-a)/(mu(b-a)).

The maximum over mu in [a,b] occurs at mu=sqrt(ab) and equals the asserted
bound. For eta=3/5, p=(2/3,1/3), t=(2/5,8/5), the normalized q is
(1/3,2/3) and TV=1/3, giving equality.

The intertwining of the Poincare maps with these projectors uses integral
lifts in the exact frame conjugated by x_u, chosen to be the identity away
from g_j. The unit Gram determinant makes the orthogonal complement split
integrally; split local coordinates lift the unipotent radical and GL_k
exactly. Make the intermediate level K_N explicit: it retains N_j but
removes the U_j condition at the opened prime, and keeps K_2 elsewhere.
Because the U_j lifts lie in x_u^(-1) H_u x_u,
N_f H_f x_u K_2 = N_f H_f x_u K_N. An exact frame lift normalizes K_N
and its character. Right translation therefore has the required covariance
on the pre-psi column space. The corner e_{U_j} C[G_j] e_{U_j} returns
to the original columns. Its finite sums commute with absolutely convergent
periodization. Individual G_j translations are not claimed to preserve the
original psi-cut space. These are paper deductions, not new Lean theorems.

**Limitation.** Two balanced marginals do not imply joint balance. The
tables diag(1/2,1/2) and the table with all entries 1/4 have identical
marginals but joint total variation 1/2. We use the coarser one-prime
decomposition, for which the preceding results suffice.

## 3. What balance does and does not remove

Suppose the source and target are block decomposed and the maps preserve
blocks. Define

    d_alpha = sum_u dim E_{u,alpha},
    k_alpha = sum_u dim ker A_{u,alpha},
    r_alpha = d_alpha-k_alpha,
    p_alpha=d_alpha/R, q_alpha=D_alpha/D, b_alpha=r_alpha/R,
    kappa=sum k_alpha/R, beta=TV(p,q),
    B=sum_alpha (q_alpha-b_alpha)_+.

For each positive-rank block let e_alpha be the reduced image defect,
normalized by r_alpha and D_alpha, as in PREREG.md. A zero-rank block has
zero weight in the sum below. Then

    max(kappa,beta) <= B <= kappa+beta,
    B <= eps(A) <= B + sum_alpha min(q_alpha,b_alpha) e_alpha.       (1)

If all positive-rank blocks have e_alpha=0, eps(A)=B. If in addition p=q,
eps(A)=kappa. Thus even exact dimension balance does not prove small defect:
individual kernels and concentration inside each block remain.

Proof over any field. For two blocks and a target subspace W, replace W
by (W intersect F_1) direct_sum pr_2(W). Its dimension is unchanged.
Projection on the second source block has kernel
A_{u,1}^{-1}(W intersect F_1) and image contained in
A_{u,2}^{-1}(pr_2 W). Hence the replacement cannot decrease the objective.
Induction shows that its maximum splits exactly into block maxima.
Equivalently, by annihilators,

    eps(A)=sum_alpha max_{V<=F_alpha^*}
      [dim V/D - sum_u rank(A_{u,alpha}^*|V)/R].

In one block write x=dim V/D_alpha and
y=sum rank(A_{u,alpha}^*|V)/r_alpha. The maximum of x-y is e_alpha.
The two endpoints V=0,F_alpha^* give max(0,q_alpha-b_alpha). If q>=b,
qx-by=(q-b)x+b(x-y)<=q-b+b e; if q<=b,
qx-by=q(x-y)-(b-q)y<=q e. This proves (1).
Finally b<=p, sum b=1-kappa, and positive-part inequalities give the
three bounds on B.

Combining Section 2 with (1), for the chosen concrete/transported family,

    eps(A) <= kappa
       + eta/(1+sqrt(1-eta^2))
       + sum_alpha min(q_alpha,b_alpha) e_alpha.                   (2)

This is the useful outcome of the one-prime algebra: the **dimension
imbalance term** is controlled under counting hypotheses. Equation (2)
does not bound kappa or e_alpha. Multiplicity one gives upper bounds on
individual period multiplicities, not the lower rank bounds needed here.

The earlier algebraic cutting lemma may subsequently be applied:

    eps(B) <= (eps(A)+delta_0+d_e)/(1-d_e),

where delta_0 is the deleted target fraction and d_e the deleted source
fraction. Applying it before the full-space identification would skip
a necessary premise.

## 4. Where independence is lost

### 4.1 Unperiodized seeds are jointly injective

**Claim, candidate-D.** For the standard source Hida data, r_S>0,
LevelSubgroupCharacter and PhWellDef, the linear map

    direct_sum_u C_u -> Functions(G(A),C),   (c_u) -> sum_u Ph_u(c_u)

is injective.

First, all N_u are the same N: the word-specific condition on z_u is
already contained in the condition on every vector in the relevant
orthogonal complement. If z_u differs from z_v, the infinite characters
are distinct. At one infinite place, let W be the orthogonal complement
of all the hyperbolic pairs. Using the last pair e,f and y in W, fix the
earlier pairs and e, and use the transformations

    n_y(w)=w+e h(y,w),   n_y(f)=f-y-h(y,y)e/2

separate the characters, since their ratio is
exp(4 pi i Re h(y,z_u-z_v)/g). Nondegeneracy permits a choice with ratio
different from one. A finite product of translation-minus-eigenvalue
operators isolates any fixed-character cluster of a finite relation.
The translations need not commute on the whole function space; they act
as scalars on the seed vectors in question.

Within a cluster with common z, the compact H_infinity is the same.
Distinct words have distinct highest weights, hence inequivalent
irreducible local types. The tensor-product types remain inequivalent.
Their matrix-coefficient spaces are linearly independent. Finally, the
orbit of W_u spans V_pi,u by irreducibility and its nonzero normalization.
Evaluating a zero seed on (y_infinity,h x_u) gives
c_u(W_u(y_infinity))(1,h)=0 for all y_infinity,h. Spanning gives zero
on (1,h) for every vector in V_pi,u. Column covariance then gives zero on
(h_infinity,h_f), so c_u=0. The final covariance step is essential.

For r_S=0 the character-separation argument does not apply. Single-word
injectivity still follows from the last argument; no general multiword
claim is made for that edge case.

### 4.2 Yet all these characters have one rational conjugacy class

**Claim, candidate-D.** The norm relation N(c_u) T_u=T_0 in the source,
where N(c)=c conjugate(c) is the relative norm,
implies that all pairs (N,psi_u) are rationally conjugate.

Let lambda=c_u/c_v, x=z_v and y=lambda z_u. Their nonzero norms agree.
Choose epsilon in {1,-1} such that a=h(x-epsilon y,x) is nonzero. Such a
choice exists since the sum for the two signs is twice the nonzero norm.
For d=x-epsilon y, the rank-one map

    R(t)=t-d h(d,t)/a

is unitary: h(d,d)=a+conjugate(a), so direct expansion cancels the cross
terms. Also R(x)=epsilon y. Thus A=epsilon R sends x to y.
Extend A to the ambient rational unitary space by

    m(e_a)=lambda e_a,   m(f_a)=conjugate(lambda)^(-1) f_a.

This m normalizes N and conjugates H_v to H_u. In each root coordinate,

    h(f_a,m^(-1)n m next_v)
      =h(conjugate(lambda)^(-1)f_a,n lambda next_u)
      =h(f_a,n next_u).

Therefore psi_v(m^(-1)n m)=psi_u(n), at both finite and infinite places.
For the automorphic Fourier coefficient

    F_psi f(g)=integral_[N] f(ng) conjugate(psi(n)) dn,

rational left invariance and the probability Haar measure on [N] give

    F_{psi_v} f(g)=F_{psi_u} f(mg).                                (3)

This is compatible with independence of the raw seeds: rational
periodization changes the ambient function space and its relations.
The conjugating m need not preserve the integral level or the selected
archimedean vectors. Equation (3) does not make the maps P_u proportional.

### 4.3 A common Fourier-blind obstruction, with the correct L2 domain

An arbitrary L2 class cannot be restricted to a fixed lower-dimensional
orbit by evaluating a representative. The following kernel conclusion
avoids that problem.

Fix a reference word u_* and its character psi_*. The compact unipotent
quotient [N] makes F_psi well defined from L2([G])
to L2_loc(G(A)), with equality almost everywhere. Integrate over a compact
closure of a measurable fundamental set for [N] and use Jensen locally;
null changes of f
remain null after the product integration. Formula (3) holds in this
local-L2 sense.

The fold estimate in the source depends on the absolute value of the seed.
Apply it to |Ph_{u,c}| as well as Ph_{u,c}. The absolutely folded majorant
sum_delta |Ph_{u,c}(delta g)| belongs to L2([G]). Cauchy-Schwarz therefore
permits absolute unfolding against every f in HH. Integrating first along
the compact [N] fiber extracts F_{psi_u} f, with the conjugation determined
by the inner-product convention. By (3),

    V_0 := HH intersect ker F_{psi_*}
       is contained in intersection_u ker P_u^*,

and consequently

    eps(P) >= dim(V_0)/dim(HH).                                   (4)

No assertion that V_0 is nonzero or zero is made. For r_S=0, N=1 and this
particular obstruction is zero. On a genuinely irreducible smooth
automorphic realization, the kernel of the full Fourier map is either
zero or the whole representation. A finite HH slice is not automatically
such an irreducible realization.

The period formula further factors P_u^* through restriction and Bessel
pairing and then an outer integral. Even an injective full Fourier map
does not prevent loss of rank in these subsequent operations. PerLaw
applies to each RowFun representative with its stated almost-everywhere
tie. Applying it to a prescribed collection of HH rows requires a
representative theorem, for example an EvalAll bridge together with RowFun.
The almost-everywhere argument above is only used for (4).

## 5. Exact algebraic description of all concentration

Let P:direct_sum E_u -> F be the sum map, and K=ker P.
For U=direct_sum U_u, put P(U)=sum A_u U_u. Then

    D eps(A) =
      max_{U_u<=E_u} [dim(K intersect U)-(1-D/R)dim U].             (5)

Proof. The expression in brackets equals
(D/R)dim U-dim P(U). Taking W=P(U), each U_u lies in A_u^{-1}(W);
hence this is at most D eps(A). Conversely, for a maximizing W take
U_u=A_u^{-1}(W). Then P(U) is contained in W, and the bracket is at least
D eps(A). Both inequalities establish equality.

Equation (5) includes individual kernels and a deficient target span;
no injectivity or spanning assumption was used. For the seed realization
in Section 4 it identifies the remaining problem precisely: a bound on
relations created by periodization **inside every product of source
subspaces**, not merely a bound on the dimension of the total kernel.

Set g=gcd(D,R), a=R/g, b=D/g and N=DR/g. Given any positive integer l
and matrices X_u of size a l by b l, form the N l square matrix

    M_l = [ A_u tensor X_u ]_u.

Then the following certificate is valid over every field:

    eps(A) <= 1-rank(M_l)/(N l).                                  (6)

Indeed, the subspace direct_sum A_u^{-1}(W) tensor field^(b l)
has dimension b l sum dim A_u^{-1}(W), while its image lies in
W tensor field^(a l), of dimension a l dim W. Therefore nullity(M_l)
is at least N l times the defect at W. Maximize over W.

A high-rank minor gives an upper certificate. A target subspace W gives
a lower certificate. Matching certificates determine a positive defect
exactly. This extends the old nonsingular-determinant certificate, which
only certified the special case eps=0.

For completeness, let M be the matrix space consisting of all [A_u tensor
X_u] at l=1. For an arbitrary source subspace Z, let U_u be the span of
all coordinate contractions of its u-th projection, and set
Uhat=direct_sum U_u tensor field^b. Rank-one choices of X_u show

    M Z = (sum A_u U_u) tensor field^a = M Uhat,     Z subset Uhat.

Thus a maximal shrunk subspace can be chosen of this product form.
Equation (5) gives maximal shrinkage N eps(A). The classical
noncommutative-rank/blow-up theorem, over characteristic zero, gives

    ncrank(M)=N(1-eps(A)).

The existence/algorithmic theorem is classical, not a new historical
claim. It does not supply high-rank witnesses for the actual automorphic
matrices. Finite searches in the accompanying audit are not claimed to
attain this maximum.

## 6. A genuine averaging model with positive defect

Take N=F_2^2, and let s exchange its two coordinates. On Q^N use the
group average Pi=(I+s)/2. The three distinct characters chi_10, chi_01,
chi_11 have Gram matrix 4I and are independent. Their averages are

    Pi chi_10 = Pi chi_01 = b,      Pi chi_11=c,

where b,c are independent. In their target span the three maps are
e_1,e_1,e_2. Each map is injective, their images span the whole target,
and their sum map has kernel generated by (1,-1,0). Nonetheless,

    eps = 2/3-1/2 = 1/6.

The line spanned by e_1 is a lower witness. For a=3,b=2,l=1 choose
X_1=(e_1,e_2), X_2=(e_2,e_3), X_3=(e_1,e_2). The associated 6 by 6
matrix has rank 5, so (6) gives the matching upper bound 1/6.

This is an actual finite group average, not an arbitrary linear
projection. It refutes the proposed general implication from raw
character independence, individual injectivity and full target span to
semistability after averaging. It does not refute semistability of the
specific automorphic family.

## 7. Result and remaining obligation

The source-specific progress is that a useful one-prime decomposition has
exact source mass and controlled target mass under explicit counting
hypotheses, and the chosen full PMat completion transports the concrete
Poincare maps. The algebra also locates the unresolved issue in relations
introduced by periodization, with the common Fourier-blind subspace as
one possible obstruction.

What remains open is a small bound for the individual kernel mass and the
weighted sum of intrinsic block defects in (2). An equivalent way to target
the full defect is the product-space relation bound in (5), or optimal
high-rank certificates in (6) for actual maps. Small full defect does not
uniformly bound every normalized intrinsic defect on arbitrarily tiny blocks.
Neither generic multiplicity one, marginal balance, raw-seed independence,
nor rational conjugacy alone supplies that bound.

No joint two-prime regularity or joint distribution estimate is claimed.
No general linear-algebra model is identified with the full automorphic
family. No RH conclusion is drawn.
