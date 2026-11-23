# Round 10: source newforms, full Fourier rank and a Satake exclusion rule

**NON-CANONICAL. No authority. No Canon status change.**

Candidate: C-RH-SEMISTABLE-FRAME-N, alias C-RH-BK-CONCENTRATION-N.
Owner: ChatGPT-Astra-Sol-20261123-R10. Claim: issue #2070; draft: PR #2071.
All new mathematical deductions below have status **candidate-D**, with their
stated realization hypotheses. The separately frozen finite audit has status
**candidate-C**. This is not Lean verification or a proof of RH.

## 1. Outcome and notation

The useful new separation is between the complete Fourier coefficient,
viewed as a function of its full ambient argument, and the selected period
which is eventually used by the proof.

For the actual split word-prime compact orbit, its synthesis map S_X satisfies,
when r_S>0,

\[
 \operatorname{rank}(\mathcal F_\psi S_X)
  =(q^k-1)\operatorname{rank}(\mathcal F_\psi|_V).
 \tag{1}
\]

The product version over the f completely split places above T_u replaces
q^k-1 by (T_u^k-1)^f. This equality does not apply to the subsequent
restriction, column pairing or outer archimedean integral.

A second result identifies a concrete part of the common blind space.
For a spherical ambient local representation Pi at a split place v, let
h_v(Pi) be the number of height intervals of its Satake multiset, defined
in Section 5. Then

\[
 h_v(\Pi)<2r_S+1
 \quad\Longrightarrow\quad
 \Pi_{N_v,\psi_{u,v}}=0
 \quad\hbox{for every word }u.
 \tag{2}
\]

One suitable split place is enough. Actual global occurrence and the
dimension of the excluded rows are separate questions.

We distinguish the ambient group rank n_G=k+2r_S+1 from the finite target
dimension D=dim(HH). Write d_u=dim(C_u), R=sum_u d_u and

\[
 \epsilon(P)=\max_{V\le HH}
 \left\{\frac{\dim V}{D}
       -\frac{\sum_u\operatorname{rank}(P_u^*|_V)}{R}\right\}.
 \tag{3}
\]

This is the dual form of the original preimage concentration defect, with
the same normalization. Positive scalings of individual P_u do not change it.

Throughout, the actual maps mean the full geometric Poincare maps, followed
through one fixed SIso and the constructed full PMat witness of rounds 8
and 9. An arbitrary witness to MatS, a good-row compression alone, or an
abstract family satisfying only the numerical Gram hypotheses is insufficient.
The external source pin remains 40e56bab026552e089d7afcfeff08d2defb9c005;
the source map records a fresh comparison with the current source head.

## 2. Almost all source columns can be put in a precise newform part

**Proposition 2.1, candidate-D.** Use the primitive split word-prime
realization proved in round 9. At v|T_u the column level is

\[
 K_{\rm col,v}=\{C\in\mathrm{GL}_k(\mathcal O_v):
                    Cw=w\pmod{\varpi_v}\},
 \qquad
 [\mathrm{GL}_k(\mathcal O_v):K_{\rm col,v}]=q_v^k-1.
 \tag{4}
\]

Its character there is trivial. Retain an auxiliary completely split rational prime g_i with
generic unipotent reduction and g_i-1>k. For any subset S of the places over
T_u, enlarge the level in (4) to GL_k(O_v) at exactly those places. Then

\[
 \dim C_u^{\rm coarse(S)}
       =\frac{d_u}{I_S},\qquad
 I_S=\prod_{v\in S}(q_v^k-1).
 \tag{5}
\]

Here a superscript coarse denotes the space at the enlarged level, not an
unproved equality between all oldvectors and one spherical line.

**Proof.** The smaller group is compact at infinity. Every rational
stabilizer of a finite adelic class at the enlarged compact level is
therefore finite. At the retained g_i its reduction is unipotent, so that
stabilizer embeds into a pro-g_i group. A nontrivial element would give an
element of order g_i in GL_k(Q_(g_i)). Its minimal polynomial contains the
cyclotomic polynomial of degree g_i-1, irreducible over Q_(g_i) by the
translated Eisenstein test. This contradicts g_i-1>k. All the stabilizers
are trivial, including after conjugation by a class representative.

The map from fine to coarse double classes thus has exactly I_S points
over every class. The archimedean coefficient fiber has the same dimension
at both levels; the retained character extends trivially at every enlarged
word-prime factor. The class-function dimension formula proves (5).
This argument uses the factorized level and the retained torsion exclusion,
not an estimate for automorphic multiplicities.

Let O_(u,S) be the part of the fine column space supported on automorphic
constituents which are spherical at every v in S. The definite smaller
group has a discrete automorphic decomposition. Round 9 gives, for every
irreducible local constituent tau,

\[
 \dim\tau^{K_{\rm col}}=
 \begin{cases}
 h(\tau)\in\{1,\ldots,k\},&c(\tau)=0,\\
 1,&c(\tau)=1,\\
 0,&c(\tau)\ge2.
 \end{cases}
\]

Keeping automorphic multiplicities, the contribution of a spherical
constituent to the fine space is between one and k times its coarse
contribution per enlarged place. Consequently

\[
 \frac{d_u}{I_S}\le \dim O_{u,S}
       \le\frac{k^{|S|}d_u}{I_S}.
 \tag{6}
\]

The inequalities also cover d_u=0 without division by d_u.

For complete splitting, every q_v=T_u and there are f places. For d_u>0,
two different cuts are useful:

\[
 \frac{\dim C_u^{\rm old\ at\ every\ place}}{d_u}
       \le\left(\frac{k}{T_u^k-1}\right)^f,
 \tag{7}
\]

\[
 \dim C_u^{\rm new\ at\ every\ place}
       \ge\left(1-\frac{fk}{T_u^k-1}\right)d_u.
 \tag{8}
\]

Equation (8) is the union bound on the f possible old local factors. It is
informative when its right side is positive. Removing only the subspace
in (7) leaves forms new at at least one word-prime place, with the smaller
deletion cost in (7).

The actual normalized diagonal Gram estimate gives
dim ker(P_u)<=e_0 d_u. Hence either chosen new part C'_u satisfies

\[
 \operatorname{rank}(P_u|_{C'_u})
       \ge \dim C'_u-e_0d_u.
 \tag{9}
\]

This uses the original diagonal analytic input; it does not derive that
input algebraically.

**Source-deletion budget, candidate-D.** If R'>0 and the deleted source fraction is
delta=(R-R')/R, then

\[
 \epsilon(P)\le \delta+(1-\delta)\epsilon(P|_{\oplus C'_u}).
 \tag{10}
\]

For any target subspace W, its full preimage dimension is at most its
retained preimage dimension plus the deleted dimension. Subtract dim(W)/D
and use -delta dim(W)/D<=0. This proves (10). If R'=0, only the trivial
bound epsilon(P)<=1 is asserted. Thus (7) gives an explicit
cheap deletion, but does not prove that the retained family has small
concentration.

A constituent ramified at a place over T_u cannot occur at another word
whose level is hyperspecial there. This applies to different word primes.
The source does not assert that distinct words always have distinct T_u.
Moreover, disjoint source spectra do not imply orthogonal images in HH.
If J_u=P_u(C'_u), s=sum_u dim(J_u)>D, there are at least s-D relations
among these image subspaces and

\[
 \sum_{u\ne v}\operatorname{tr}(\operatorname{pr}_{J_u}
                               \operatorname{pr}_{J_v})
      \ge s^2/D-s.
 \tag{11}
\]

This follows by applying trace Cauchy-Schwarz to the sum of the projections.

## 3. The actual compact orbit has only two Gram eigenoperators

**Proposition 3.1, candidate-D.** At a split word-prime place take the
integral coordinates of round 9:

\[
 L=M\oplus\mathcal O t,\quad \ell(t)=1,\quad
 z=w+\varpi t,\quad
 i(C)=
 \begin{pmatrix}C&(w-Cw)/\varpi\\0&1\end{pmatrix},
 \tag{12}
\]

where w in M is primitive. Extend i(C) by the identity on the other
hyperbolic coordinates of the ambient GL_(n_G). For C in GL_k(O), the
orbit of the ambient hyperspecial lattice, equivalently of its coset in G/K, is indexed by

\[
X=\mathbb F_q^k\setminus\{0\},\qquad M_X=|X|=q^k-1.
\]

These cosets label the translated vectors in a representation. The vectors
themselves can coincide, as in the determinant-character case below.

For two distinct orbit points the relative matrix has Cartan exponents
(-1,0,...,0,1). Indeed its determinant is a unit, both it and its inverse
have entries of valuation at least -1, and multiplication by varpi gives
reduction of rank one. These facts force exactly one exponent -1 and one
exponent +1.

Let R be any unitary representation of GL_(n_G)(F_v), K=GL_(n_G)(O_v),
P_K its orthogonal Haar projection, and

\[
 d=\operatorname{diag}(\varpi,1,\ldots,1,\varpi^{-1}),
 \qquad A=P_KR(d)P_K\big|_{\mathcal H^K}.
\]

The operator A is selfadjoint, because d and d^(-1) have the same
K-double coset. For a finite-dimensional V contained in H^K and any orbit
lifts g_x, define

\[
 S_X:V^X\longrightarrow\mathcal H,\qquad
       (f_x)\longmapsto\sum_{x\in X}R(g_x)f_x.
\]

Its operator Gram matrix has I on the diagonal and the compression of A
to V off the diagonal. It decomposes into

\[
 I+(M_X-1)A \quad\hbox{on constant arrays},\qquad
 I-A \quad\hbox{on arrays with sum zero}.
 \tag{13}
\]

The assertion is about quadratic forms on V, and does not require A(V)
to be contained in V.

There are
N_G=(q^(n_G)-1)/(q-1) index-q sublattices of O^(n_G). Every pair of
different such neighbors has the same relative Cartan exponents.
The Gram matrix of all neighbor translates is positive, so

\[
 I+(N_G-1)A\ge0.
\]

As M_X<N_G, this implies

\[
 I+(M_X-1)A
   \ge \frac{N_G-M_X}{N_G-1}I>0.
 \tag{14}
\]

For a K-fixed vector f,

\[
 \langle (I-A)f,f\rangle
   =\tfrac12\|R(d)f-f\|^2.
 \tag{15}
\]

The group generated by K and d is ker(val composed with det). To see this,
permute d by Weyl elements in K and use its powers to generate every
integer diagonal valuation tuple of sum zero; then apply Cartan
decomposition. Therefore the kernel in (15), among K-fixed vectors, is
exactly the SL_(n_G)(F_v)-invariant subspace.

For one irreducible spherical representation Pi and a unit spherical
vector s, the scalar matrix is

\[
 G_X=(1-a)I+aJ,\qquad
 a=\langle\Pi(d)s,s\rangle
   =\frac{N_G|b|^2-1}{N_G-1},
 \tag{16}
\]

where b is the normalized eigenvalue of the index-q neighbor Hecke
average. The last equality follows by taking the squared norm of the sum
of all N_G neighbor translates: that sum lies on the unique spherical
line. All noncharacter spherical irreducibles give rank M_X. An
unramified determinant character gives rank one. If M_X=1 both statements
coincide.

**Quantitative refinement, candidate-D using a classical theorem.**
For n_G>=3, on a unitary subrepresentation without local SL_(n_G)-fixed
vectors, Hee Oh's Theorem 1.1 gives

\[
 \|A\|\le h_q=\frac{3q-1}{q(q+1)}<1.
 \tag{17}
\]

Use the singleton strongly orthogonal root e_1-e_(n_G), whose valuation
on d has absolute value two. The explicit PGL_2 spherical function in that
theorem is q^(-1)(2(q-1)+(q+1))/(q+1). The K-type dimension factors are
one and the split Cartan remainder is the identity. Thus the sum-zero
block in (13) lies between (1-h_q)I and (1+h_q)I. On all arrays the lower
bound is the minimum of 1-h_q and (N_G-M_X)/(N_G-1).
This estimate assumes no temperedness of the ambient representation.
It is an estimate before the period.

**Finite compact types, candidate-D.** Over the complex numbers the
permutation module C[X] splits by characters chi of F_q^*. For chi!=1 the
chi-sector has dimension (q^k-1)/(q-1) and is irreducible: it is induced
from the stabilizer of a line with its scalar character, and the
nontrivial double-coset term in the intertwiner calculation is zero
because the two line scalars can vary independently. For chi=1 it is the
projective-point permutation module, equal to constants plus one
irreducible augmentation when k>=2, by double transitivity. For k=1
this reduces to the regular representation of F_q^*.
This inventory describes the compact orbit before any Bessel functional.

## 4. An exact rank formula after the complete Fourier coefficient

**Theorem 4.1, candidate-D.** Work in the genuine automorphic unitary
representation H=L^2([G]), with one fixed global unipotent character psi.
The full Fourier transform is

\[
 \mathcal F_\psi f(g)
   =\int_{N(F)\backslash N(\mathbb A)}
          f(ng)\overline{\psi(n)}\,dn,
 \tag{18}
\]

as an element of L^2_loc(G(A)). The compactness of [N], Jensen's
inequality and finite quotient charts on compact subsets make (18)
continuous from L^2([G]) to L^2_loc. They also show that null changes of a
representative have no effect. In detail, a compact lift B of [N] and a
compact test set C in G(A) reduce the estimate to the local L^2 norm of
f on BC; discreteness of G(F) bounds it by a finite multiple of the global
L^2 norm.

Let E be orthogonal projection onto (ker F_psi)^perp. The kernel is closed
and invariant under all right translations, so E commutes with them.
For V contained in H^K as in Section 3 put W=E(V). Then the exact
one-place formula, including the exceptional case, is

\[
 \operatorname{rank}(\mathcal F_\psi S_X)
  =M_X\dim W-(M_X-1)
      \dim\bigl(W\cap\mathcal H^{\mathrm{SL}_{n_G}(F_v)}\bigr).
 \tag{19}
\]

**Proof.** Right equivariance gives
F_psi S_X(f_x)=0 if and only if S_X(Ef_x)=0.
The constant Gram block is strictly positive by (14). By (15), the
sum-zero nullspace consists precisely of arrays in
W intersect H^(SL) with sum zero, of dimension
(M_X-1) dim(W intersect H^(SL)). The map V^X onto W^X is surjective.
Rank-nullity proves (19).

If r_S>0, the second term vanishes without a strong approximation theorem.
For a right SL_(n_G)(F_v)-invariant input, its full Fourier output is
still right invariant. This local subgroup is normal in GL_(n_G)(F_v),
so the output is also left invariant under it, in L^2_loc. Haar
disintegration on the quotient supplies an almost-everywhere representative
depending only on the local determinant and the other adelic coordinates;
left SL acts trivially on that quotient. This avoids substituting a
point-dependent element into an almost-everywhere invariance identity.
But (18) is left (N_v,psi_v)-equivariant, and psi_v is
nontrivial. Hence that output is zero. All locally SL-invariant inputs
belong to ker F_psi and are orthogonal to W.

Thus (19) becomes (1). Since dim W=dim V-dim(V intersect ker F_psi),

\[
 \operatorname{rank}(\mathcal F_\psi S_X)
    =(q^k-1)\bigl(\dim V-\dim(V\cap\ker\mathcal F_\psi)\bigr).
 \tag{20}
\]

Right translations at distinct places commute and preserve the remaining
hyperspecial invariances. Iterating the same proof with the same fixed
Fourier map gives

\[
 \operatorname{rank}(\mathcal F_\psi S_{X_1\times\cdots\times X_f})
  =(T_u^k-1)^f
      \bigl(\dim V-\dim(V\cap\ker\mathcal F_\psi)\bigr).
 \tag{21}
\]

The translated rows lie at enlarged level in the ambient L^2 space; they
need not lie in the original finite-dimensional HH. There is no conflict
between (21) and dim(HH)=D.

For r_S=0 the character is trivial and the correction in (19) cannot
simply be removed. A trivial determinant line with F_psi=id and M_X>1
has rank one. This is a counterexample to an unconditional r_S=0 version
of (20).

**Scope.** Equation (21) concerns the complete Fourier function on G(A).
No representative of E(V) is evaluated on a lower-dimensional subset.
It supplies no lower norm estimate for F_psi and no rank estimate after
a selected period.

## 5. A local Satake exclusion rule for all the words

This is the new obstruction supplied by the opposition lane and checked
separately by the development lane and another paper reader.

### 5.1 The actual split character

Let r=r_S>=1 and n_G=k+2r+1. At a split local place, identify the
Hermitian space with a vector space and its dual. Order its plus component
in blocks

\[
 X_1,\ldots,X_r,\ B,\ Y_r,\ldots,Y_1,\qquad \dim B=k+1.
\]

The finite subgroup N in HidaSetting is exactly the strictly upper block
unipotent radical of the parabolic Q with sizes (1^r,k+1,1^r). Its
definition says that the complete X flag is fixed on the associated
graded spaces and that the action on X^perp/X is the identity; the other
split component gives the paired Y flag.

The two components of the distinguished vector give z in B and
ell in B^*, with ell(z)=-T_u!=0. The source's character has the form

\[
 \chi_u(n)=\psi_v\bigl(\operatorname{tr}(A_u(n-I))\bigr),
 \tag{22}
\]

where A_u is supported on the first block subdiagonal. The ordinary
one-dimensional arrows are nonzero, and the two arrows through B are
nonzero scalar multiples of z and ell. Their composite is nonzero.
Signs and the nonzero factor g^(-1) do not affect this assertion.

The opposite split component is essential. It contributes the outgoing
chain through the inverse-transpose unitary action; it is not absent
from the source's trace character. Nontriviality of both local additive
characters follows from the integral condition together with the rational
product law and the specified archimedean trace character. Triviality on
the open integral additive subgroup implies continuity, and density of
E in its finite adeles fixes the character. At the completely split word
prime the two scalar components have conductor O. The argument below
only needs their nonzero field coefficients.

### 5.2 The Satake count

For a spherical irreducible Pi of GL_(n_G)(F_v), partition its multiset
of unramified characters into lines under multiplication by
nu=|.|_v. On one line write a_j for the finite-support multiplicities.
Define

\[
 h_v(\Pi)=\sum_{\text{lines}}\sum_j(a_j-a_{j-1})_+.
 \tag{23}
\]

Equivalently, for each height h take the connected intervals of
{j:a_j>=h}, and count all those intervals. They are nested or separated
by gaps, hence pairwise unlinked. The segment construction in round 9,
using Zelevinsky's Example 3.2 and Theorem 4.2, realizes Pi as an
irreducible normalized parabolic induction of exactly h_v(Pi)
determinant characters. Contragredients and unramified character twists preserve
this count. For a finite multiplicity sequence its total rises equal its
total drops.

### 5.3 The vanishing theorem

**Theorem 5.1, candidate-D.** If t=h_v(Pi)<=2r, then the smooth twisted
Jacquet module Pi_(N,chi_u) is zero. This holds for every word u and
every smaller-group test representation.

**Algebraic proof.** Let n and q be the strictly upper and upper block
Lie algebras of Q. For the trace pairing, n^perp=q. For every B_0 in q
and every nonzero v_1 in X_1, the last-block component of

\[
 (A_u+B_0)^{2r}v_1
\]

is a nonzero scalar multiple of ell(z). Indeed one step moves forward
by at most one block. Reaching the last block in exactly 2r steps
forces all the successive first-subdiagonal arrows. Therefore

\[
 (A_u+B_0)^{2r}\ne0\qquad(B_0\in\mathfrak q).
 \tag{24}
\]

Let x be a flag for the inducing parabolic P with t blocks. If p_x
is its stabilizer Lie algebra, then p_x^perp=u_x is its flag radical,
and every Z in u_x satisfies Z^t=0. When t<=2r, (24) implies

\[
 A_u\notin\mathfrak q+\mathfrak u_x
       =(\mathfrak n\cap\mathfrak p_x)^\perp.
 \tag{25}
\]

Thus the character linear form is nonzero on the Lie stabilizer at
every flag.

**Passage to smooth induction.** Realize the normalized induced
representation as locally constant sections of its line bundle on
G/P. Filter by the finitely many Q relative-position strata. Successive
pieces are compactly supported smooth sections on a single stratum.

On such a stratum n intersect p_x has constant dimension, since Q
normalizes n. Locally solve the constant-rank linear equations for
Z_x in that intersection with tr(A_u Z_x)=c, where psi_v(c)!=1.
A nonzero minor gives a continuous local choice. On the compact support
of one section, a finite cover makes all choices bounded. They lie,
after adding I, in one compact open subgroup U of N. Such subgroups
exhaust N by dilation by a contracting diagonal torus.

The element I+Z_x fixes the flag and acts trivially on the inducing
fiber: it is unipotent on every graded quotient, so each determinant
character and the parabolic modulus are one. Its character is
psi_v(c)!=1. The U-twisted average of the section must therefore vanish
at x. Its U-equivariance gives vanishing on U times the support, and
support gives zero elsewhere. This average represents the same element
of twisted coinvariants as the original section. Every stratum's
coinvariants are zero, and right exactness along the finite filtration
proves the assertion.

This proof does not assume finitely many N-orbits and does not choose
an unbounded family of stabilizer elements on one compact support.
It also works for the inverse character. The case r=0 gives no
restriction.

### 5.4 Global meaning and an explicit failed shortcut

At a fixed suitable split place, every -T_u is nonzero in the local
field, including when it is divisible by its uniformizer. Divisibility
has no role in (24). Consequently one spherical local component with
h_v(Pi)<2r+1 excludes the entire actually occurring global constituent
from the full Fourier coefficient for every word. Fix the other local
vectors and evaluate the translated Fourier coefficient to obtain a
local equivariant functional; the local Jacquet vanishing kills it for
every smooth translate. Continuity of the full Fourier map passes this
to its closed automorphic realization.

No assumption of sphericality at every split place is made. Use a
place where it is supplied, for example an actual split word prime
away from g.

For the actual P_u maps, psi now denotes a fixed reference word character
psi_*. The rational conjugacy in round 8, equation (3), and Section 6.2
identifies the kernels of the full Fourier maps for every word. Use the
absolute-unfolding bridge of round 8 with its full hypotheses. The fold datum and its multiplicity bound
depend on |Ph_(u,c)|. Applying the L^2 folding result to that absolute
seed and then Cauchy-Schwarz permits absolute unfolding against every
L^2 row. Disintegrate through the closed subgroup
L=N(A)H(F), with fiber [N]; H(F) preserves its probability Haar measure.
The fiber integral, set to zero on the invariant set where it is not
absolutely convergent, is genuinely equivariant. Its absolute value
descends to L\\G(A), so ambient almost-everywhere vanishing passes to
quotient almost-everywhere vanishing by the Weil measure formula.
This proves the needed implication without evaluating an arbitrary
L^2_loc class on one orbit:

\[
 HH\cap\ker\mathcal F_\psi\subseteq\bigcap_u\ker P_u^*.
 \tag{26}
\]

Alternatively the source's PerLaw may be used on its bounded continuous
RowFun representatives, with the stated star in its first argument
and an actual representative/spanning bridge. Signed square
integrability alone is not a substitute for the absolute-fold
hypothesis.

If V_bad is a finite target slice supported on the actual globally
occurring constituents excluded by Theorem 5.1, (3) and (26) give

\[
 \epsilon(P)\ge\frac{\dim V_{\rm bad}}D.
 \tag{27}
\]

Neither existence nor absence nor a count of V_bad has been proved here.

A local counterexample settles the tempting universal nonvanishing claim.
Induce from GL_(n_G-1) times GL_1 an unramified unitary determinant
character and an unramified unitary character on a disjoint nu-line.
The induction is irreducible, spherical, unitary and infinite-dimensional,
with h_v=2. For every r>=1, Theorem 5.1 kills its full Bessel Jacquet
module. Its compact orbit nevertheless has full rank by Section 3.
This example is local; no occurrence in the source's global target
is asserted.

## 6. Two additional source checks that prevent false reductions

### 6.1 The word-prime character has an essential uniformizer

**Candidate-D.** In (12), use the rational basis [M,z/varpi].
The incoming root of the actual Bessel character has coefficient
varpi, while the outgoing root has a unit coefficient. This follows
directly from z=varpi(z/varpi), ell(z/varpi)=1, and the inverse-transpose
formula for the opposite split component. Up to the established signs
and units, these valuations are 1 and 0.

The finite-character normalization fixes the conductor to O at the
completely split word prime. In Liu's split integral coordinates put
beta=w/varpi. For r>0, with S(beta) adding beta from the distinguished
line into M, one has

\[
 L(g,x)S(-\beta)=S(-g\beta)Z(-x\beta)L(g,x).
\]

Only the last root of Z contributes to the extended Whittaker character.
The actual phase is therefore

\[
 \psi_v(\pm\varpi x_r\beta/g)
       =\psi_v(\pm x_r w/g).
 \tag{28}
\]

It is trivial on integral shifts of x_r. Substituting a unit incoming
coefficient while keeping beta nonintegral would instead give a
nontrivial character on those compact shifts and spurious cancellation.
A basis change to unit coefficients must change the row test at the same
time. This calculation supplies neither a nonzero selected higher-gap
test nor a lower bound for its global integral.

There is no additional hidden word-prime shear in the source element
x_u. Its OneOff condition implies (x_u)_v=1 for every v|T_u: apply it
with m=T_u^j for all j, use that the auxiliary integer is a local unit,
and intersect the resulting T_u^j L_v.

### 6.2 One rational smaller group still has different evaluation orbits

**Candidate-D.** The norm relation N(c_u)T_u=T_* supplies rational
conjugacies m_u carrying one reference pair (N,psi,H) to the pair of
word u. Transport of the unfolded period leaves the finite point

\[
 t_u=m_{u,f}^{-1}x_u,
\]

the transported archimedean vector W_u, and its outer integration
measure. It does not remove their word dependence. The common-group
column level is H(A_f) intersect t_u K_2 t_u^(-1), with the transported
character.

The source's LevelDec gives precisely this subgroup as the stabilizer
of Nt_uK_2 under H(A_f). For distinct word primes, at a place over one
of them the stabilizer is a proper subgroup of index q^k-1 in a
hyperspecial compact, while at the other word it is hyperspecial.
The corresponding Haar volumes differ, and conjugation in the
unimodular GL_k local group preserves volume. Therefore these are
distinct NH double orbits when q^k-1>1. Equality of the rational
smaller group cannot by itself turn all period maps into evaluations
of one fixed projection.

The selected archimedean words also cannot simply be declared complete.
The source proves that distinct words have distinct local highest
weights at every infinite place. Conditional on the matching nonzero
local Bessel intertwiners, mixing local choices from two words at two
places gives an admissible archimedean tuple absent from the word list.
This is a statement about the local tensor choices, not about global
automorphic occurrence. It is not used to infer a positive target defect.

## 7. What is simplified, and what is still needed

After deletion (7), every retained constituent has a conductor-one local
line at at least one place over its word prime. Requiring such a line at
every place uses the larger deletion budget (8). The compact translate
Gram matrix is (13), with only two eigenoperators and the quantitative
bound (17). The full Fourier rank on these translates is exactly (21).
The new Satake criterion (2) identifies a verifiable class of completely
blind rows and yields the lower bound (27) if their global dimension
is supplied.

The remaining maps still restrict that Fourier function to the
prescribed smaller-group orbit, pair it with a specified column and
perform the outer archimedean integral. None of (7), (17), (21) or (2)
bounds the loss under those maps. In particular, neither local
multiplicity one nor exact compact type balance gives a lower bound on
the required period matrices.

A concrete next obligation has two parts:

1. Determine the actual target dimension supported on the excluded local
   Satake types, or prove those types absent in the realized row spectrum.
   This addresses only a common blind subspace.
2. On the surviving spectrum, prove a rank inequality for the specified
   finite period matrices on every target subspace, with the actual
   row cuts, column lines, character normalization and outer integral.
   Equivalently, certify the required positive concentration bound by
   the high-rank matrix certificates already established in round 8.

The original proof requires a sufficiently small defect, not exact
semistability. An exponential improvement would be a stronger result
and is not claimed. The sharp abstract obstruction of round 9 is
unchanged: the pairwise Gram information by itself cannot establish
a uniformly smaller order than the square-root density scale.
