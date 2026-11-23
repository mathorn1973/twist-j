# Transported compact types and rational Bessel orbits

**NON-CANONICAL. No authority. No Canon status change.**

These source identifications and paper deductions are **candidate-D**.
The fixed-orbit global nonvanishing and selected-family rank questions
remain **O**. The RH source links use the same pin as rounds 9–11.

## The compact word types after transport

Every two distinct words have distinct compact types at **each**
archimedean place. The source proves the parameter distinction in
$\operatorname{data8}$. The argument uses the common vector $v$, the
positive gap $\Delta$ and injectivity of the letters. A differing letter
at index $l$ changes the Harish-Chandra entry at $l+1$ by exactly
$\Delta$. The actual $\pi_{\mathrm{Loc}}$ uses this parameter, and its
compact highest weight is obtained by the same fixed $\rho$-shift for
every word. The tensor identity identifies the resulting product type
with $\pi_U$ on the compact stabilizer.
[DataS, lines 19–32](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/DataS.lean#L19-L32)
· [D7, lines 93–104](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalRingCardinality/RhoDetPrimeEqMuTildeMulChiPow.lean#L93-L104)
· [data8, lines 770–783](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/StandingHypothesesHoldFamily.lean#L770-L783)
· [HidaSetting, lines 275–295](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L275-L295)
· [Compact highest-weight condition, lines 61–96](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean#L61-L96).

The rational transport of round 8 is $E$-linear and unitary. At each real
place, the transported frame and the reference orthonormal frame differ
by a unitary matrix. The induced automorphism in $U(k)$ coordinates is
inner and preserves the type. This argument allows coincidences of the
level primes. Uniform conjugation or dualization of the type family
also preserves pairwise inequivalence.

Consequently, if each $B_u$ is a nonzero intertwiner from the same
smooth archimedean row module to its transported word type $V_u$, then
$\bigoplus_u B_u$ is onto $\bigoplus_u V_u$. Its image is a submodule of
a finite direct sum of inequivalent irreducibles and projects onto every
summand. If an enlarged family repeats a type $V$, identify its copies
first. A desired tuple $(a_i)$ in those copies is realizable exactly
when $\sum_i\lambda_i a_i=0$ for every relation
$\sum_i\lambda_i B_i=0$. Indeed, the image in $V\otimes\mathbb C^I$
has the form $V\otimes L$, and those relations give $L^\perp$ in the
linear dual. The actual word index has no such repeats.

## Real signs and the rational norm class

Set $r=r_S>0$. The complement $B$ of the $r$ rational hyperbolic
pairs in the ambient Hermitian space has dimension $k+1$ and
signature $(k,1)$ at every real place. Landherr's criterion for
representing zero gives a rational isotropic line in $B$. The
dimension is odd and at least three, and the signature allows one
isotropic line at every real place. Splitting off a hyperbolic plane
gives ambient rational Witt index $r+1$, with the reverse bound
coming from the real signatures.
[Ranks and signature, lines 32–44](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalRingCardinality/Params.lean#L32-L44)
· [Source hyperbolic pairs and norm, lines 207–219](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L207-L219)
· [Landherr, original paper, p. 248](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/landherr.pdf#page=4).

The plane represents every $\delta\in F^\times$, since in a
hyperbolic pair $e,f$ with $h(e,f)=1$, the vector $e+(\delta/2)f$
has norm $\delta$. Fix $\delta=-T_u$. Choose an unramified inert
finite place of $E/F$, and by weak approximation choose a totally
positive $a\in F^\times$ of valuation one there. Local norms have
even valuation at that place. Hence $\delta$ and $a\delta$ give
different classes in $F^\times/N_{E/F}(E^\times)$, although their
orthogonal complements are both definite at every real place.

The norm classes distinguish the corresponding rational nilpotent
orbits. With $h$ linear in the second slot, put $v_i=e_{i+1}$
for $i<r$, $v_r=z$, $x^\flat(y)=h(x,y)$, and
$$
 R=\sum_{i=1}^r v_i f_i^\flat,\qquad X=R-R^*.
$$
Here $R$ is the trace-dual matrix for the root coordinates before
applying the relative trace. Because $(\log n)^*=-\log n$ on the
unitary unipotent, the relative trace of
$\operatorname{tr}_E(R\log n)$ is
$\operatorname{tr}_E(X\log n)$. The first block superdiagonal is
unchanged by taking $\log n$. The common additive-character scaling
can be held fixed throughout the comparison.

The chain is $e_1\mapsto\cdots\mapsto e_r\mapsto z\mapsto-\delta f_r$,
followed by $f_i\mapsto-f_{i-1}$ for $i>1$, with $f_1\mapsto0$.
Thus $X^{2r}e_1=(-1)^r\delta f_1$. On the one-dimensional
$E$-space $V/\ker X^{2r}$ the form
$$
 (\bar x,\bar y)\longmapsto h(x,X^{2r}y)
$$
is well defined and nondegenerate, since $X^{2r}$ is self-adjoint.
Its norm coefficient on the class of $e_1$ is $(-1)^r\delta$, so
rational unitary conjugacy preserves its norm class. This also agrees
with the anisotropic-vector parametrization in Jiang–Zhang. The argument
shows that a real-type test leaves a rational choice, with no assertion
of automorphic occurrence or vanishing on either class.
[Source character, lines 101–115](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L101-L115)
· [Jiang–Zhang, §2.4, equations (2.11)–(2.13)](https://arxiv.org/pdf/1508.03205#page=21).

## Global scope

- Jiang–Zhang, Proposition 2.2, starts with a **cuspidal realization** and
  gives a maximal nonzero Bessel index $\ell_0$ between zero and the
  rational Witt index. It proves cuspidality at that index. Its range
  leaves a lower bound $\ell_0\ge r_S$ to establish, and its nonvanishing
  allows a choice of rational orbit. Conjecture 2.3 asks for a generic
  cuspidal summand at the first occurrence, with the realization and
  orbit also quantified existentially. Theorem 5.7 uses an already
  nonzero period to deduce a nonzero central value.
  [Annals paper, Proposition 2.2, Conjecture 2.3 and Theorem 5.7](https://annals.math.princeton.edu/2020/191-3/p02).
- Li's nonsingularity theorem, for cusp forms, gives a maximal-rank
  Fourier coefficient along the center of the unipotent radical for a
  maximal isotropic space. The corresponding square-zero complex
  partition is $(2^{r+1},1^{k-1})$. Its largest part is two, below the
  first part of the required odd hook. This supplies no coefficient on
  the fixed hook.
  [Li, Main Theorem, p. 44](https://www.numdam.org/article/CM_1992__83_1_43_0.pdf#page=3).
- Beuzart-Plessis–Chaudouard, Theorem 1.3.3.1, starts with a prescribed
  discrete Hermitian parameter pair and relates its central value to
  existence of a cuspidal pair on a suitable form. Theorem 1.3.6.1 treats
  a fixed cuspidal pair with everywhere tempered local factors and
  discrete Hermitian weak base change. These inputs and the requisite
  nonvanishing on the prescribed rational orbit and selected finite
  tests still need to be supplied. Round 11's discrete-spectrum
  identification does not assert cuspidality of every row. A first
  occurrence argument applies only to a supplied cuspidal realization.
  [BPC, §§1.1 and 1.3](https://doi.org/10.1017/fmp.2025.8).

Unrestricted nonvanishing on the source's fixed rational orbit would
address the corresponding Fourier kernel. Control of the actual rank
inequality on every target subspace also requires the prescribed finite
translation and column tests. No computation or Lean verification was
performed in these checks.
