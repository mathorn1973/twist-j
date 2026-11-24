# Round 12: removing the archimedean average from the actual period maps

**NON-CANONICAL. No authority. No Canon status change.**

Candidate: C-RH-SEMISTABLE-FRAME-N, alias C-RH-BK-CONCENTRATION-N.
Session: ChatGPT-Astra-Sol-20261123-R12. Date: 2026-11-23.

All new mathematical deductions below have status **candidate-D** under
the stated genuine-realization hypotheses. Classical results retain their
published scope. This is paper work, not a Lean verification or a new
candidate-C computation. The immutable source and exact correspondences
are in [SOURCE_MAP.md](SOURCE_MAP.md).

## 1. Outcome and its precise scope

Fix one actual finite instance of the construction and its supplied
automorphic realization, including the fixed identification of the
abstract target with the full concrete row space. Let

$$
P_u:C_u\longrightarrow HH
$$

be its actual full Poincare maps, before the later row and column cuts.
There is **one common archimedean translate** $y\in G_\infty$ and, for
each word, an explicitly specified unaveraged Bessel-period map $Q_u$
such that

$$
Q_u=\frac{b_u(y)}{c_u}P_u,\qquad b_u(y)\ne0,\quad c_u>0.                 \tag{12.1}
$$

The same $y$ works for every word, every row and every column in this
finite instance. All finite test data, in particular the translate
$x_u$, stay in the formula defining $Q_u$. One can either prescribe
nonzero compact vectors $\xi_u$ in advance and use
$b_u(y)=\langle W_u(y),\xi_u\rangle$, or use the literal source
integrand with $\xi_u=W_u(y)$ and $b_u(y)=\|W_u(y)\|^2>0$.

Consequently, for every target subspace $V$,

$$
\operatorname{rank}(Q_u^*|_V)=\operatorname{rank}(P_u^*|_V),
\qquad \epsilon(Q)=\epsilon(P).                                      \tag{12.2}
$$

This removes a whole integration stage from the concentration question.
It does not prove a lower rank for the remaining global periods. It gives
no effective choice of $y$, no lower bound on $|b_u(y)|$, and no
preservation of Gram energies under this rescaling.

## 2. Actual input data and conventions

Write $r=r_S$, so the real groups at every real place are
$G_v=U(k+r,r+1)$, and the compact smaller group is $H_{u,v}=U(k)$.
Let $S_{u,\infty}=N_\infty H_{u,\infty}$, with the actual unitary
character $\lambda_u$ on its unipotent part. Put
$\Sigma=\bigotimes_{v\mid\infty}\sigma_v$, where each $\sigma_v$
is the supplied discrete series, and let $w=\bigotimes_v w_v$ be the
supplied unit vector in its specified minimal compact type.

The finite-dimensional unitary compact representation is
$\pi_u=\bigotimes_v\pi_{u,v}$ on $V_u$. The actual column space
$C_u$ consists of equivariant column-form maps; evaluation at
$\xi\in V_u$ gives the automorphic column function
$\operatorname{colForm}(T,\xi)$. Each $\pi_{u,v}$ is irreducible.

The supplied function $W_u:G_\infty\to V_u$ has all of the following
properties, not merely a formal transformation law:

1. It is continuous and transforms on the left by $\lambda_u\pi_u$.
2. It is integrable, has relative squared norm one for the actual
   quotient measure, and is reproduced by convolution with the actual
   normalized row coefficient.
3. The same normalized convolution is the projector determined by
   $w$, rank one on $\Sigma$ itself, with its Schur convolution
   identity in representations that may have multiplicities.

The actual `RowsBij` correspondence supplies, for every $f\in HH$, a
unique continuous $G_\infty$-intertwiner

$$
I_f:\Sigma\longrightarrow L^2_{\rm aut},\qquad I_f(w)=f.               \tag{12.3}
$$

It is linear in $f$. Its image retains the row's finite level and
character. For smooth $v$, use the smooth finite-level automorphic
representative of $I_f(v)$. Local Sobolev estimates in quotient charts
give this representative and its values on compact sets. In particular
$I_f(w)$ transforms on the right under $K_2$ by the same unitary
character as the seed. The finite translate $x_u$ is inserted
explicitly in (12.4).

We retain the actual `SBes` character and subgroup identifications, the
positive quotient-fold formula, and the round 8 square-integrability
bound for the sum of the absolute values of the seed translates.
Section 5 applies these inputs to every $f\in HH$, including rows for
which global boundedness of the smooth representative has not been
established.

Inner products are conjugate-linear in their first argument and linear
in their second. The source's `ConjVec` and `EvalAll` mean that the row
entering the bilinear Bessel period is the conjugated row.

## 3. A fixed global period defines a local Bessel intertwiner

Fix $u,f,T$, retaining every finite test. For a smooth
$v\in\Sigma^\infty$ and $\xi\in V_u$, define

$$
L_{u,f,T}(v,\xi)=\operatorname{per}_{\psi_u}
\left(\operatorname{colForm}(T,\xi),
  g\longmapsto\overline{I_f(v)\bigl(\iota_X(g)(1,x_u)\bigr)}\right).
                                                                        \tag{12.4}
$$

It is conjugate-linear in $v,f$ and linear in $\xi,T$.
The quotient of the unipotent group is compact. The smaller group is
anisotropic, since it is compact at infinity, so its automorphic quotient
is compact as well. At a fixed finite level, local Sobolev estimates on a
finite cover of this compact integration domain bound (12.4) by a smooth
seminorm of $v$, for each fixed $f,T$. Thus it is continuous on the
smooth globalization. This local continuity argument is separate from
the absolute unfolding justified in Section 5.

Changing variables in the period using the actual character ties gives

$$
L_{u,f,T}(\Sigma(s)v,\xi)
 =\lambda_u(s)^{-1}L_{u,f,T}(v,\pi_u(s)^{-1}\xi),
\quad s\in S_{u,\infty}.                                                \tag{12.5}
$$

For the finite-dimensional fiber, Riesz representation therefore gives
a continuous linear map $A_{u,f,T}:\Sigma^\infty\to V_u$ with

$$
L_{u,f,T}(v,\xi)=\langle A_{u,f,T}(v),\xi\rangle,
\qquad
A_{u,f,T}(\Sigma(s)v)=\lambda_u(s)\pi_u(s)A_{u,f,T}(v).                  \tag{12.6}
$$

The inverse character in (12.5) becomes the positive character in the
second identity because the first slot of the inner product is
conjugate-linear. This is a material convention check.

The archimedean Bessel multiplicity-one theorem of Jiang, Sun and Zhu
applies to these groups and the actual negative anisotropic line. It
bounds the space of maps in (12.6) by one. In the theorem's bilinear
notation the representation is $\sigma_v\otimes\pi_{u,v}^{\vee}$.
For $r>0$, the character coefficients in the source are generic; when
$r=0$, the unipotent condition is empty and the theorem concerns the
restriction $U(k,1)\to U(k)$, with compact smaller group. For the
finite product of real places, freeze the other
tensor variables and apply the local one-dimensional statement in turn.
Normalization at nonzero test vectors and density of algebraic smooth
tensor vectors give the same bound for the product. See
[JSZ, Theorem A and Section 2](https://arxiv.org/pdf/0908.1728).

This gives uniqueness, not nonvanishing of $A_{u,f,T}$.

## 4. The actual normalized W supplies the nonzero reference map

Consider the relative unitary Hilbert representation

$$
\mathcal H_{{\rm rel},u}
 =L^2(S_{u,\infty}\backslash G_\infty,\lambda_u\pi_u)
$$

with the quotient measure induced by the source's $\nu_Q$.
Both groups in the quotient are unimodular; the semidirect factor at
infinity is compact on its reductive part. Right translation is unitary.

Let $\varphi$ be the actual normalized, conjugated matrix coefficient
of $w$. Its integrability is one of the actual projector hypotheses.
Schur convolution in this representation gives, with $P=R(\varphi)$,

$$
P=P^*=P^2,\qquad
PR(g)P=\langle w,\Sigma(g)w\rangle P.                                  \tag{12.7}
$$

The source has $PW_u=W_u$ and $\|W_u\|=1$. Hence

$$
\langle W_u,R(g)W_u\rangle
  =\langle w,\Sigma(g)w\rangle.
$$

Polarization of the cyclic Gram matrices produces a complex-linear
isometric intertwiner

$$
J_u:\Sigma\hookrightarrow\mathcal H_{{\rm rel},u},\qquad J_uw=W_u.
                                                                        \tag{12.8}
$$

Evaluation of a smooth relative section at the identity is continuous
for the smooth topology by local Sobolev estimates on the homogeneous
bundle. Thus

$$
B_u(v)=(J_uv)(1)
$$

is a continuous Bessel intertwiner. It is nonzero: otherwise equivariance
and right translation would make every value of every $J_uv$ zero.
The smooth representative of $J_uw$ equals the supplied continuous
$W_u$ everywhere. Indeed, they agree almost everywhere, and a nonzero
continuous difference would be nonzero on an open quotient patch of
positive Haar measure. Consequently

$$
B_u(\Sigma(y)w)=W_u(y).                                                  \tag{12.9}
$$

Multiplicity one now yields a scalar $a_{u,f,T}$ such that

$$
A_{u,f,T}=a_{u,f,T}B_u.                                                  \tag{12.10}
$$

## 5. The outer integral is exactly a norm-square normalization

Write $\Phi_{u,T}$ for the unperiodized source seed. Its absolute
periodization $M_{u,T}(g)=\sum_\delta|\Phi_{u,T}(\delta g)|$
belongs to $L^2([G])$ by the round 8 fold bound. For the smooth
representative $f=I_f(w)$, Tonelli's theorem identifies the integral
of $|\overline f\,\Phi_{u,T}|$ on
$S_u(F)\backslash G(\mathbb A)$ with
$\int_{[G]} |f| M_{u,T}$. Cauchy–Schwarz bounds this by
$\|f\|_2\|M_{u,T}\|_2$. We may therefore unfold the complex
pairing $\langle f,P_uT\rangle$ absolutely on the full row space.

The product $\overline f\,\Phi_{u,T}$ is measurable, invariant on
the left under the rational Bessel group and on the right under
$K_2$, since the two finite characters cancel. Its support in the
finite adelic variable is contained in $S_u(\mathbb A_f)x_uK_2$.
`fold_integral_besselQuotient_supportedFunctions` applies to the
positive and negative parts of both its real and imaginary parts with
the same strictly positive real measure factor $c_u$. Absolute
integrability justifies recombination and Fubini. On the resulting
Bessel quotient, `ph_colForm` evaluates the seed as the selected
column at $W_u(y)$ times the character fixed by `SBes.tieψ`.
The row is evaluated at the same $(y,x_u)$. With the measures of
(12.4) this proves

$$
\langle f,P_uT\rangle
 =c_u\int L_{u,f,T}(\Sigma(y)w,W_u(y))\,d\nu_Q(y).                       \tag{12.11}
$$

This recovers the source's period identity for its bounded `RowFun`
representatives and extends it by absolute folding to the full genuine
$HH$. Positivity of $c_u$ comes from the quotient measure identity;
the bare `PerLaw` interface quantifies over a complex constant.

By (12.9)-(12.10), the literal integrand is

$$
L_{u,f,T}(\Sigma(y)w,W_u(y))
  =\overline{a_{u,f,T}}\,\|W_u(y)\|^2.                                  \tag{12.12}
$$

The relative squared norm is one, so

$$
\boxed{\langle f,P_uT\rangle=c_u\overline{a_{u,f,T}}.}                   \tag{12.13}
$$

In particular, this matrix entry vanishes if and only if (12.4) vanishes
for all archimedean vectors $v,\xi$, with the same fixed finite tests.
There is no additional cancellation created by the outer integral.
There may still be a zero global scalar $a_{u,f,T}$.

## 6. One common translate works for the entire finite family

Choose any nonzero vectors $\xi_u\in V_u$ in advance and set

$$
b_u(y)=\langle W_u(y),\xi_u\rangle.
$$

The span of the values of $W_u$ is a nonzero invariant subspace of the
irreducible compact type $V_u$, hence is all of $V_u$. Thus no
$b_u$ is identically zero.

We need more than continuity to choose a point common to all words.
Each component of $W_u$ is real analytic. Here is the reason with the
required minimal-type hypothesis made explicit. The vector $w$ is
smooth and belongs to a single compact isotypic type in an admissible
discrete series. It therefore has a fixed compact Casimir eigenvalue,
as well as a fixed infinitesimal character. Choose an invariant real
quadratic form positive on the noncompact part $\mathfrak p$ and
negative on $\mathfrak k$, including the compact center. With
orthonormal bases, the Casimir is

$$
\Omega_{\mathfrak g}=\sum_{X\in\mathfrak p}X^2
                         -\sum_{Y\in\mathfrak k}Y^2.
$$

For differentiations along $y\mapsto y\exp(tX)$, the components of
$W_u$ satisfy the scalar eigen-equation for

$$
\Omega_{\mathfrak g}+2\sum_{Y\in\mathfrak k}Y^2
       =\sum_{X\in\mathfrak p}X^2+\sum_{Y\in\mathfrak k}Y^2.
                                                                        \tag{12.14}
$$

This is elliptic with real-analytic coefficients. Analytic elliptic
regularity gives the assertion. A highest-weight-vector assumption is
not needed; the single compact type is enough. The classical regularity
reference is Morrey-Nirenberg,
[CPAM 10 (1957), 271-290](https://doi.org/10.1002/cpa.3160100204).

The real group $U(p,q)$ is connected, and so is the product
$G_\infty$. The nonzero set of each nonzero analytic $b_u$ is dense
and open. There are finitely many words. Their intersection is a dense
open nonempty set. Choose $y$ there and define $Q_u$ by

$$
\langle f,Q_uT\rangle
   =L_{u,f,T}(\Sigma(y)w,\xi_u).                                         \tag{12.15}
$$

Its sesquilinearity defines a map $C_u\to HH$. Equations
(12.10), (12.13) and (12.15) give (12.1). Alternatively, choose a common
point with $W_u(y)\ne0$ for every word and then put $\xi_u=W_u(y)$.
This second choice retains the literal source integrand and makes all
$b_u(y)$ positive.

The choice is simultaneous in $u,f,T$ because $W_u$ depends on the
word and fixed realization, not on the row or column being paired.
It is not a choice uniform over every parameter instance.

## 7. Exact consequence for concentration

Put $D=\dim HH>0$, $R=\sum_u\dim C_u>0$. For arbitrary maps,
including maps with kernels, the earlier dual rank identity is

$$
\epsilon(P)=\max_{V\le HH}
 \left(\frac{\dim V}{D}
       -\frac1R\sum_u\operatorname{rank}(P_u^*|_V)\right).               \tag{12.16}
$$

Nonzero scalar multiplication preserves every rank in this expression,
and also every preimage dimension in its equivalent primal expression.
This proves (12.2). The fixed basis/isometry transports used for the
actual full matrix family preserve the same defect.

For a permitted error $\epsilon_*$, the remaining exact task is now

$$
\sum_u\operatorname{rank}(Q_u^*|_V)
   \ge R\left(\frac{\dim V}{D}-\epsilon_*\right)
\quad\text{for every }V\le HH.                                         \tag{12.17}
$$

The $Q_u$ in (12.17) are unaveraged, specifically tested global Bessel
periods. Local uniqueness only removed the outer averaging; it provides
no lower bound for the scalars or their ranks as $f,T$ vary. Full
Fourier visibility, selected-period visibility and the subspace rank
inequality remain distinct obligations. The previous sharp abstract
square-root obstruction is unchanged.

## 8. A second, different common-vector statement

The rational Witt transports from the earlier rounds identify every
$(S_u,\lambda_u)$ with a single pair $(S_*,\lambda_*)$. If
$S_u=m_uS_*m_u^{-1}$, define

$$
\widetilde B_u(v)=B_u(\Sigma(m_{u,\infty})v).
$$

They are intertwiners for one compact group $H_{*,\infty}$, with the
transported compact types. Actual different words have distinct compact
Harish-Chandra parameters, at each real place, by `data8`. The
representations are therefore pairwise inequivalent. The exact source
and inner-transport check are in
[TYPE_AND_ORBIT_CHECKS.md](TYPE_AND_ORBIT_CHECKS.md).

Each nonzero $\widetilde B_u$ is onto its irreducible finite-dimensional
type. The image of the direct-sum map is invariant under the compact
group. Complete reducibility and pairwise inequivalence imply

$$
\bigoplus_u\widetilde B_u:\Sigma^\infty\longrightarrow\bigoplus_u V_u
\quad\text{is surjective}.                                             \tag{12.18}
$$

For example, projection onto any one irreducible summand is a compact
central character projector; it preserves this image and isolates that
summand. Since every coordinate projection is onto, every summand lies
in the image.

Consequently, for any chosen unit $\xi_u$, there is a single smooth
vector $v_*$ with $\widetilde B_u(v_*)=\xi_u$ for all words, and

$$
\langle f,P_uT\rangle
  =c_u L_{u,f,T}(\Sigma(m_{u,\infty})v_*,\xi_u).                          \tag{12.19}
$$

This is not the same quantifier as the common literal translate in
Section 6. The vector $v_*$ need not be a product vector, lie in the
original minimal compact cut, and no norm bound uniform over the data is
obtained. Equation (12.19)
is an identity for the original row parameter $f$ through $I_f$;
it does not silently replace the target by a larger row space.

## 9. What is settled and what is still open

**Candidate-D:** in the genuine construction the actual normalized
archimedean vector and local Bessel uniqueness eliminate cancellation
from the outer integral. One common point preserves all actual
subspace ranks and the concentration defect. The distinct-word compact
types also permit arbitrary simultaneous outputs of one smooth vector.

**Candidate-D:** [GLOBAL_OBSTRUCTIONS.md](GLOBAL_OBSTRUCTIONS.md)
determines the archimedean annihilator orbit and gives an exact
multiplicity-space accounting for the full global Fourier kernel.
[TYPE_AND_ORBIT_CHECKS.md](TYPE_AND_ORBIT_CHECKS.md) records the remaining
rational-orbit and descent quantifiers.

**Open:** the mass of the full global kernel for positive $r$, the
matching of the prescribed global rational type where needed, and the
selected-period inequality (12.17). None is inferred from local
genericity, balanced dimensions, multiplicity one, or one unrestricted
nonzero period. No assertion about the truth or completed verification
of the RH proof is changed by this note.
