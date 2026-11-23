# Round 11: the hook criterion, regular row spectrum and the remaining global rank problem

**NON-CANONICAL. No authority. No Canon status change.**

Candidate: C-RH-SEMISTABLE-FRAME-N, alias C-RH-BK-CONCENTRATION-N.
Owner: ChatGPT-Astra-Sol-20261123-R11. Issue #2070; draft PR #2071.
This is a paper-only continuation. New identifications and deductions are
**candidate-D**, conditional on the explicitly named geometric realization.
Classical results retain their literature scope. There is no new finite
execution, Lean verification or claim that the actual concentration bound
has been closed.

## 1. Results and the three different questions

Put r=r_S and n_G=k+2r+1=k+m-1. At a split finite place the ambient group
is GL_(n_G). For an irreducible spherical local representation Pi let
h_v(Pi) be the height-interval count of its Satake multiset from round 10.

The referee's local converse is correct:

$$
 \boxed{\Pi_{N_v,\chi_{u,v}}\ne0
       \quad\Longleftrightarrow\quad
       h_v(\Pi)\ge 2r+1.}                                      \tag{1}
$$

The source pair is the neutral Whittaker pair of the odd hook
(2r+1,1^k). This is an application and explicit identification of classical
Whittaker/wavefront theory, not a new general wavefront theorem.

For the actual geometric row space, with the parameter-family hypotheses
specified in Section 3, there is a stronger conclusion than the proposed
h_v>=n_G-1:

$$
 \boxed{h_v(\Pi)=n_G}
 \quad\text{at every split finite place where the row is spherical.} \tag{2}
$$

In particular the subspace V_bad defined in round 10 by the local
inequality h_v<2r+1 is zero in this setting. An arbitrary abstract D7
without the geometric and parameter suppliers is not covered.

Neither conclusion says that the full global Fourier coefficient is
nonzero on every actual global constituent, nor that the selected global
period matrices have sufficient rank. These are different assertions:

1. a local twisted Jacquet module exists;
2. the fixed global Fourier functional is nonzero on the actual
   automorphic representation;
3. the selected row vectors, column spaces and outer integrals satisfy
   a lower-rank inequality on every target subspace.

The current result closes the stated local-type obstruction under the
source-family hypotheses. It does not identify the full global kernel.

## 2. Why the local equivalence is exact

### 2.1 Identification of the actual neutral pair

The actual split unipotent N has block sizes

$$
 1^r,\ k+1,\ 1^r .
$$

In the middle block B the source gives z and ell with
ell(z)=-T_u!=0. Thus B=F_v z direct-sum ker(ell). The character matrix A
of round 10 acts on one chain of length a=2r+1 and kills the k-dimensional
complement ker(ell). Its Jordan type is therefore (a,1^k).

Assign the successive chain vectors weights a-1,a-3,...,1-a and assign
ker(ell) weight zero. After rescaling the chain, A belongs to a rational
sl_2 triple with this neutral semisimple element H. All these weights
are even. Consequently g_1=0, and g_(>=2) is exactly the strictly upper
block Lie algebra of the source N. No polarization or oscillator factor
is missing.

The character also agrees with the neutral one:

$$
 \operatorname{tr}(A\log n)=\operatorname{tr}(A(n-I)),\qquad n\in N.
$$

Only the first block superdiagonal can pair with A. Higher terms in
log(n) have zero contribution there. The inverse-character convention in
the generalized Whittaker dual replaces A by -A, which is conjugate to A
over F_v. This does not change the orbit or the nonvanishing assertion.

For r>=1 this identification needs ell(z)!=0. At ell(z)=0 the Jordan
type changes; the referee's separate finite-field control is compatible
with that change but is not used as a proof here. If r=0, which the rank
data allow when m=2, then N=1 and A=H=0. In that case (1) is automatic,
and no assertion about a change of orbit at ell(z)=0 is needed.

### 2.2 The literature criterion and its exact attribution

Gomez, Gourevitch and Sahi [GGS], Theorem E, give for GL_n the equivalence

$$
 \mathcal W_{\mathcal O}(\Pi)\ne0
 \quad\Longleftrightarrow\quad
 \mathcal O\subseteq\operatorname{WF}(\Pi).
$$

For an irreducible representation the wavefront set is the closure of
one nilpotent orbit. A partition lambda dominates the hook
(a,1^(n_G-a)) precisely when lambda_1>=a: the forward implication follows
from the first partial sum; for the converse use that every further
nonzero part is at least one, until the sum has already reached n_G.

Moeglin-Waldspurger's 1987 theorem identifies maximal nonvanishing
orbits. The converse for interior orbits in the displayed equivalence
uses [GGS], rather than a blanket attribution to the 1987 theorem alone.
[GGS] Theorem 4.3.1 includes Varma's extension for residue characteristic
two. We used that precise restatement; the full 1987 publisher text was
not available in this review.

### 2.3 Why the largest wavefront part is the Satake count

On each line under multiplication by nu=|.|_v let a_j be the finite-support
Satake multiplicities. Define

$$
 t=h_v(\Pi)=\sum_{\text{lines}}\sum_j(a_j-a_{j-1})_+ .
$$

The connected intervals of each positive height layer are nested or
separated by gaps, hence pairwise unlinked. The spherical description of
round 9 and Zelevinsky's segment theory identify Pi with an irreducible
normalized induction of t determinant characters, one per interval.

Zelevinsky II [Z], Theorem 8.1, removes one endpoint from every nonempty
segment in the highest derivative. These are segments on degree-one
cuspidal lines, so the order of that derivative is exactly t.
Equivalently, the representation has depth t.

For the hook, [GGS] Theorem F and Section 4.4 identify its generalized
Whittaker space with the dual of

$$
 (E^1)^{n_G-a} E^a(\Pi).
$$

The E^1 factors preserve the underlying vector space. The last expression
is nonzero exactly when a<=t. This proves (1). Combined with Theorem E
and the hook dominance test, it also proves that the first wavefront
part is exactly h_v(Pi). No temperedness or unitarity is needed for (1).

Nonvanishing is the assertion. There is no claim that all interior-hook
models are one-dimensional.

### 2.4 A direct flag proof of the missing direction

There is also a geometric proof of the converse for the particular
irreducible induction just described. Let P be its inducing parabolic,
with t positive block sizes. If t>=a, place the a successive vectors of
the long A-chain in a distinct one of t flag grades each, in decreasing
grade order, and fill the remaining slots from the k-dimensional
zero-chain complement ker(ell).
Each grade has at least one slot, and the total remaining capacity is k.

For the resulting P-flag x, A lies in its nilpotent radical u_x. Under
the trace pairing u_x=p_x^perp. Hence the source character is trivial
on H_x=N intersect P_x. The inducing line is also trivial on H_x,
since H_x is unipotent and every inducing factor is a determinant
character.

The orbit N(F_v)x is locally closed and is N(F_v)/H_x(F_v). One may use
the algebraic orbit and H^1(F_v,H_x)=1 for the split unipotent stabilizer.
Its compactly supported smooth sections are an N-subquotient of smooth
induction, by the standard orbit-filtration construction [BZ].

For the left action (n.f)(x)=f(n^(-1)x), integration against chi on
N/H_x has L(n.f)=chi(n)L(f), so it gives a nonzero twisted coinvariant
on that subquotient. Over complex smooth representations of
a p-adic unipotent group the twisted Jacquet functor is exact: exhaust N
by compact open subgroups and use their character-averaging projections,
then a filtered direct limit. Exactness therefore gives a nonzero
coinvariant of Pi. Right exactness alone would not justify this
subquotient step.

Together with the algebraic vanishing proof of round 10, this supplies
a second derivation of the same threshold.

## 3. The actual row parameters have no unit gap

The referee inspected individual cloud and b inequalities and allowed
one possible unit gap at their join. For the constructed family the
source supplies a stronger statement directly.

In StandingHypothesesHoldFamily.lean, row_parameter_gaps_large,
lines 1347-1391, for a genuine ParameterChoice' P one has

$$
 C_l k m^4+n_Gm^{10}
   <\lambda_i-\lambda_{i+1},
 \qquad C_l\le P.Cgap .
$$

The proof explicitly covers the v part, the join, and the negative-b
part. Since P.Cgap>0, choose C_l=0:

$$
 \boxed{\lambda_i-\lambda_{i+1}>n_Gm^{10}>1
        \quad\text{for every adjacent pair}.}                 \tag{3}
$$

For the asymptotic family, P is supplied by Fm.params once x>Fm.x1.
This use of row_parameter_gaps_large does not need the additional
residual hypotheses of standing_hypotheses_hold_family.

Alternatively the same strict separation is included explicitly in
StandingHypotheses, in StandingNumericalData.lean lines 133-136.
It belongs to that definition, not to the preceding definition named
StandingNumericalData.

Ranks gives k and m even, m>=2, k>=m+3, and f>=m. Hence n_G=k+m-1 is
odd and [F:Q]=f>=2 in the geometric field realization. The argument does
not infer integrality of Delta from a possibly degenerate word set.

### 3.1 The Harish-Chandra normalization is not assumed from a name

The source's lamS is (v_0,...,v_(k-2),-b_0,...,-b_(m-1)).
HidaSetting identifies B.lam with this vector. However IsDS is defined
using square integrability and a Vogan-minimal K-type, not by an explicit
assertion about the central infinitesimal character.

StatementDS defines that minimal K-type weight as

$$
 \mu=\lambda_S+\rho_{\rm noncompact}-\rho_{\rm compact}
     =\lambda_S+\rho-2\rho_{\rm compact}.                       \tag{4}
$$

The classical discrete-series formula [HKS, Definition 2.7] for the true
Harish-Chandra parameter lambda' says
mu+2 rho_compact=lambda'+rho(lambda'). Sorting this vector recovers the
chamber of lambda', since adding its chamber's rho preserves strict
order. For (4) the order is the prescribed order of lambda_S+rho.
Subtract that rho to obtain lambda'=lambda_S, up to the fixed compact
Weyl relabeling. There is no factor-of-two change of gaps.

The algebraic highest weight lambda_S-rho is integral, since it equals
mu-2 rho_noncompact, an integral K-weight minus a sum of roots. It is
regular: adjacent differences are lambda_i-lambda_(i+1)-1>0. Using the dual
coefficient system if required changes neither regularity nor the gaps.
Conjugate/contragredient row conventions have the same separation.

## 4. From the geometric row space to the local Satake bound

### 4.1 Every contributing row belongs to discrete automorphic spectrum

This step retains the genuine full realization, not an abstract numerical
witness and not only the good-row compression.

RowsDef defines HH as the range on the entire automorphic L^2 space of
the bounded operator P=R_e composed with R_phi. HidaSetting gives the
actual integral specification of R_phi. FinX.finHH says that this entire
range is finite-dimensional. The supplied full SIso identifies it with
the abstract HH used in the concentration problem.

In the classical automorphic spectral decomposition every right
translation, hence P, is decomposable. It commutes with multiplication
by indicators of measurable spectral subsets. Suppose y=Px had a
nonzero component in the non-atomic part. Split the support of its norm
into infinitely many disjoint sets B_j of positive measure. Then

$$
 P(1_{B_j}x)=1_{B_j}y
$$

are infinitely many mutually orthogonal nonzero vectors in the range
of P, a contradiction. The same argument allows only finitely many
participating discrete summands.

RowsBij, with its actual intertwiner/evaluation hypotheses, identifies
their archimedean factors with the specified discrete series. HH itself
need not be invariant under the full adelic group. No unsupported
cuspidality assertion about every row is needed.

### 4.2 A base-change theorem which controls the chosen split places

Use Labesse [L], Corollary 5.3. For a unitary inner form over a totally
real field of degree at least two, and a discrete automorphic
representation with the specified discrete series at infinity satisfying
his condition (*), it supplies a base change which is an isobaric sum
of unitary discrete GL representations. It matches at every unramified
or split place and matches infinitesimal characters at infinity.

Regular algebraic highest weight, which follows from (3)-(4), supplies
condition (*); [Sh, p.2] explicitly records this regular-weight case
for Labesse's result. The field degree condition follows from f>=m>=2.
Thus no unverified all-inner-form Arthur-packet assertion is substituted.

Matching at the actual chosen split place is essential. A statement of
weak base change giving only almost-all-place matching would not by
itself justify a claim at a specific T_u.

### 4.3 All nontrivial Speh blocks are excluded

The discrete spectrum classification [MW89] writes each GL discrete
factor as Speh(mu_j,d_j), for a unitary cuspidal mu_j. At a complex
place, with |z|_C=z bar(z), the normalized twists in a block are

$$
 |\det|_C^{(d_j-1)/2},\
 |\det|_C^{(d_j-3)/2},\ldots,\
 |\det|_C^{-(d_j-1)/2}.
$$

They shift each holomorphic infinitesimal-character coordinate by the
displayed exponent. If d_j>=2, two entries in the full transferred
multiset differ by exactly one. The antiholomorphic coordinates have
the same shift rule. The angular exponent of a unitary character is
not the holomorphic infinitesimal-character coordinate.

Such a pair is impossible by (3). Infinitesimal characters are multisets,
so entries from another factor cannot cancel it. Consequently every
d_j=1. In particular no exceptional S_2 block remains. The base change
is an isobaric sum of unitary cuspidal GL representations.

### 4.4 No accidental finite-place adjacency

At a split place where the actual row is spherical, the local component
of each global cuspidal factor in this sum is spherical. One proof lifts
a K-fixed vector from
the spherical quotient of normalized induction by compact averaging;
Iwasawa decomposition then gives
(Ind sigma)^K=sigma^(K intersect M).

For every Satake parameter alpha in every such unitary cuspidal factor,
the Jacquet-Shalika bound [JS] gives

$$
 q_v^{-1/2}<|\alpha|<q_v^{1/2}.                                \tag{5}
$$

For completeness, their spherical Rankin-Selberg integral is the
reciprocal Euler polynomial. Their holomorphy statement for
mu times its contragredient on Re(s)>=1 excludes
|alpha|>=q_v^(1/2): the factor alpha times bar(alpha) would give a real
pole there and the reciprocal polynomial has no numerator to cancel it.
Unitarity identifies the contragredient parameter multiset with the
complex-conjugate one. Applying the same statement to the contragredient
gives the lower edge.

All factors lie in the same open annulus. Thus the ratio of two
parameters, including parameters in different cuspidal factors, cannot
have absolute value q_v or q_v^(-1). No two Satake characters differ
by nu or nu^(-1).

Every positive height interval therefore has length one. Repeated
identical parameters count with their full multiplicity. There are
exactly n_G intervals, proving (2).

This uses the strict one-half bound, not Ramanujan or local temperedness.
In particular it does not supply the all-place temperedness hypothesis
of the refined global period formula discussed below.

### 4.5 What has actually been excluded

By (1)-(2), the complete local twisted Jacquet module for the actual
character is nonzero on every contributing row at these split spherical
places. The locally excluded subspace V_bad of round 10 is therefore
zero in the genuine parameter-family realization.

There is also a direct local nonvanishing check: the representation is
the irreducible unramified principal series of its singleton, pairwise
unlinked segments. Choose B containing N. Its N-invariant open cell
U^+ w_0 B/B is identified with U^+=N semidirect-product U_M, where U_M
is the unipotent of the block Levi. Compactly
supported functions on that cell have nonzero N,chi coinvariants by
integration in the N-coordinate. Exactness of twisted Jacquet preserves
their injection into the whole principal series.

This proves existence of a full local model. It does not evaluate that
model on the original spherical row vector together with the selected
smaller-group column. It does not make the global Fourier map injective.

## 5. The global GGP theorem does not finish the first global obligation

Beuzart-Plessis and Chaudouard [BPC], Theorem 1.3.3.1, begin with a
given pair of discrete Hermitian GL parameters. They equate nonvanishing
of its complete central Rankin-Selberg value with existence of a
cuspidal automorphic pair on a suitable Hermitian form, with the prescribed
pair as weak base change, whose Bessel functional is not identically zero.

This does not choose a smaller parameter for an arbitrary larger row.
It does not itself put the distinguished pair on the source's fixed
rational form, embedding, automorphic member or prescribed vectors.
The central-value condition remains an input to the existence direction.
Here weak base change is tested at almost all split places. Section 4
alone establishes neither cuspidality of every row nor the discrete
Hermitian Asai conditions for both members of a selected pair.

Their Theorem 1.3.6.1 fixes a cuspidal pair, requires temperedness at
every place and discrete Hermitian weak base change, and expresses the
squared period on a factorizable vector using a global L-ratio and
normalized local period factors. A prescribed local factor may vanish.
Our argument in Section 4 deliberately does not prove temperedness.

There is no absolute phase obstruction: coherent diagonal squared
periods can be polarized in the finitely many varying tensor slots;
a known nonzero reference vector then recovers the period up to one
common phase on a fixed constituent pair. But applying that observation
requires actual evaluations, hypotheses and control of the selected
outer integral. It supplies no lower-rank estimate by itself.

The two BPC theorems are a precise analytic route to the remaining
period problem, not a statement that every row already has a nonzero
period in the prescribed family.

## 6. The precise remaining global quantity

Write P_u:C_u->HH, D=dim HH>0 and R=sum_u dim C_u>0. The full defect,
including any individual kernels, has the dual expression

$$
 \epsilon(P)=\max_{V\le HH}
 \left(\frac{\dim V}{D}
       -\frac1R\sum_u\operatorname{rank}(P_u^*|_V)\right),
$$

as in round 9, equation (6.1).

Fix the reference rational type (N,psi,H) from round 10 and write

$$
 K_{\rm glob}=HH\cap\ker\mathcal F_\psi .
$$

This can be nonzero without contradicting V_bad=0. The latter excludes
one local cause of blindness, whereas K_glob is the actual global
Fourier kernel intersected with the finite row space.

On the smooth vectors of an individual irreducible automorphic embedding pi, if
the definite smaller quotient [H] is compact, there is an elementary
equivalence:

$$
 \mathcal F_\psi|_\pi\ne0
 \quad\Longleftrightarrow\quad
 \text{some unrestricted automorphic representation on this fixed H
       has a nonzero Bessel period against pi}.                 \tag{6}
$$

Indeed choose f and g with F_psi f(g)!=0. The continuous function
h maps to F_psi f(hg) descends to [H] because H(F) normalizes N and
preserves psi. It is nonzero and square-integrable. Decompose it in the
discrete automorphic spectrum of compact [H] and choose a smooth vector
in a nonzero component with nonzero pairing. Pairing with its conjugate
in the bilinear convention gives the Bessel period of R(g)f. The converse
follows directly from its integral.

Equation (6) permits arbitrary smaller constituents and row translates.
Neither the selected word family nor its levels, source lines,
archimedean vectors and outer averages are unrestricted in that way.
If multiplicities occur, visibility of one representative of each
isomorphism class is also weaker than controlling the full isotypic
kernel. The actual subspace K_glob includes such directions.

The absolute-unfolding and fixed-realization hypotheses of round 10
give K_glob contained in the common kernel of the actual P_u^*. Thus

$$
 \epsilon(P)\ge\frac{\dim K_{\rm glob}}D .
$$

For an allowed positive defect epsilon_*, the necessary first target
is only dim(K_glob)/D<=epsilon_*, not necessarily K_glob=0.
The exact equivalent of epsilon(P)<=epsilon_* remains

$$
 \boxed{\sum_u\operatorname{rank}(P_u^*|_V)
       \ge R\left(\frac{\dim V}{D}-\epsilon_*\right)
       \quad\text{for every }V\le HH.}                          \tag{7}
$$

Even representation-level existence of a period does not make it
nonzero on every chosen nonzero vector. One can choose and then fix the
other factors of a nonzero tensor period to obtain a nonzero scalar
functional in an
archimedean slot of dimension at least two, hence a nonzero kernel
vector. The simultaneous subspace inequality (7) is stronger still.

## 7. Evidence boundary and references

The supplied referee note reports finite-field checks, but those programs
were not available as public pinned evidence for this review and were
not run here. We neither reissue their counts nor claim a new candidate-C
audit. All round 8-10 frozen scientific evidence remains unchanged.

Two Astra paper lanes and a Sol global-period reader checked the present
deductions and challenged the normalization, global transfer and
quantifiers. Source reading is not a Lean build. A source correspondence,
precise literature roles and current-head comparisons are in SOURCE_MAP.md;
REVIEW.md records accepted corrections, hypotheses and open obligations.

- [GGS] R. Gomez, D. Gourevitch and S. Sahi,
  [Generalized and degenerate Whittaker models](https://arxiv.org/pdf/1502.06483),
  Definition 2.5.1, Lemma 2.5.2, Theorems E-F and Sections 4.3-4.5.
- [Z] A. V. Zelevinsky,
  [Induced representations of reductive p-adic groups II](https://www.numdam.org/item/10.24033/asens.1379.pdf),
  Example 3.2, Theorems 4.2 and 8.1.
- [BZ] I. N. Bernstein and A. V. Zelevinsky,
  [Induced representations of reductive p-adic groups I](https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/BZ-induced-1.pdf),
  Section 1.9 and the smooth orbit-section construction in Section 5.
- [HKS] M. Harris, T. Kobayashi and B. Speh,
  [Translation functors and restriction of coherent cohomology](https://www.ms.u-tokyo.ac.jp/~toshi/texpdf/tk2025l-HKS_250921.pdf),
  Definition 2.7, equation (2.24), for the classical minimal-K-type normalization.
- [L] J.-P. Labesse,
  [Changement de base CM et series discretes](https://webusers.imj-prg.fr/~michael.harris/CBCM.pdf),
  condition (*) and Corollary 5.3, pages 42-43.
- [Sh] S. W. Shin,
  [On the cohomological base change for unitary similitude groups](https://math.berkeley.edu/~swshin/BCofU.pdf),
  page 2, for the regular-highest-weight case of Labesse's condition.
- [MW89] C. Moeglin and J.-L. Waldspurger,
  [Le spectre residuel de GL(n)](https://www.numdam.org/item/10.24033/asens.1595.pdf),
  the classification theorem on pages 605-606.
- [JS] H. Jacquet and J. A. Shalika,
  [On Euler products and the classification of automorphic representations I](https://www.math.columbia.edu/~hj/On%20Euler%20products%20I.pdf),
  Proposition 2.3, equation (18), pages 518-519, and Corollary 2.5(ii), page 525.
- [BPC] R. Beuzart-Plessis and P.-H. Chaudouard,
  [The global Gan-Gross-Prasad conjecture for unitary groups II](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/global-gangrossprasad-conjecture-for-unitary-groups-ii-from-eisenstein-series-to-bessel-periods/2E9DFB9FC7A671B5530E47E3A37D1E7E),
  Sections 1.1 and 1.3, especially Theorems 1.3.3.1 and 1.3.6.1.
