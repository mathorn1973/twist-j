# The real row orbit and the kernel of the global Fourier coefficient

**NON-CANONICAL. No authority or Canon status change.** This chapter belongs to C-RH-SEMISTABLE-FRAME-N. The deductions below are **candidate-D** under the stated realization hypotheses. The size of the actual global kernel and the simultaneous selected-period rank bound have status **O**.

## 1. The largest possible Bessel hook at a real place

Write $q=m/2=r_S+1$, $p=k+q-1$, and $n_G=p+q=k+2q-1$. Use the geometric row and its discrete-series and parameter-family hypotheses from [round 11, Sections 3 and 4](../round11/PROOF.md). They identify the real row representation $\sigma_v$ with a discrete series of $U(p,q)$ and identify its Harish-Chandra parameter with the supplied strictly decreasing list $\lambda_S$. In that order the first $k-1$ places are positive. The remaining $2q$ signs alternate, starting with a positive sign. Thus the list has an initial block of **$k$ positive signs** followed by $2q-1$ alternating signs beginning and ending with a negative sign. The source defines the weights and signs together. [Pinned definitions of `lamS` and `epsS`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean#L165-L172)

**Candidate-D.** In the trace-pairing identification of complex nilpotent orbits by partitions, the associated variety of the annihilator of the Harish-Chandra module is

$$
  \mathcal V(\operatorname{Ann}\sigma_v)
       =\overline{\mathcal O_{(2q,1^{k-1})}}.                         \tag{1}
$$

**Proof.** Apply Yamashita's Theorem 3.2 to the derived group $SU(p,q)$. It is connected semisimple with finite center. The multiplication map $U(1)\times SU(p,q)\longrightarrow U(p,q)$ is onto with finite kernel. The compact central factor acts by scalars on the irreducible row, so restriction to $SU(p,q)$ remains irreducible and square-integrable. The roots and their order are unchanged by subtracting the common central coordinate from $\lambda_S$. On adjoining the central Lie algebra again, its fixed infinitesimal character imposes zero in that direction of the associated variety. Yamashita identifies the annihilator variety with the Zariski closure of the union of the complex adjoint conjugates of the negative noncompact root space sum. [Yamashita, Theorems 3.1 and 3.2](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/0826-03.pdf)

In the ordered basis these are triangular matrices with entries permitted only between unequal signs. Taking transposes puts them in upper triangular form without changing any Jordan partition. Every such matrix kills the first $k$ basis vectors, so has rank at most $2q-1$. This inequality persists under conjugation and Zariski closure. Pick one vector from the first $k$ and all $2q-1$ tail vectors. Place a nonzero entry between consecutive vectors of that alternating list and set all other entries to zero. The resulting matrix has one chain of length $2q$ and $k-1$ trivial chains.

For completeness, every partition $\lambda$ of $n_G$ whose nilpotent rank is at most $2q-1$ is dominated by this hook. The first $j$ parts total at most $\min(n_G,j+2q-1)$, since their total excess over one per nonzero part is bounded by the rank. This is exactly the hook's $j$-th partial sum. Orbit closure in type A is the dominance order. The bound gives containment in the right side of (1), and the exhibited chain gives the reverse containment. Passing to the contragredient preserves (1).

**Candidate-D.** A Bessel coefficient attached to the odd hook $(2\ell+1,1^{n_G-2\ell-1})$ is identically zero on this real row for every $\ell\ge q$ for which such data exist. This conclusion holds for every real rational orbit with that partition. Indeed, a nonzero smooth Bessel functional for its unipotent character restricts nontrivially to the dense Harish-Chandra module and differentiates to an algebraic Whittaker functional. The neutral grading for this odd hook has no degree-one piece. Matumoto's Theorem 2 and Corollary 4 place its complex nilpotent orbit in the annihilator variety. Its rank is $2\ell$, whereas (1) bounds the rank by $2q-1$. The inverse character has the same complex partition. [Matumoto, *Whittaker vectors and associated varieties*, pp. 222–223](https://doi.org/10.1007/BF01404678)

## 2. What global first occurrence would establish

In the source Hermitian space the rational Witt index is $q$. The source supplies $r_S=q-1$ hyperbolic planes. Their complement has dimension $k+1$ and signature $(k,1)$ at every real place. It contains one further rational hyperbolic plane. Indeed, the underlying nondegenerate quadratic form $x\mapsto h(x,x)$ over the totally real base field has dimension $2(k+1)>4$. It is isotropic at every nonarchimedean completion by the local quadratic-form dimension bound, and at every real completion by its signature. Hasse–Minkowski supplies a nonzero rational isotropic vector, which splits a Hermitian hyperbolic plane. The negative index $q$ at any real place is the upper bound. See also the direct Hermitian isotropy criterion and the companion account of rational orbits. [Landherr, p. 248](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/landherr.pdf#page=4) · [Type and orbit checks](TYPE_AND_ORBIT_CHECKS.md)

The real exclusion therefore removes the last Bessel index $\ell=q$ allowed by the rational group. If a global coefficient is nonzero on a smooth automorphic realization, a right translate and fixed tests in the other factors give a nonzero continuous unipotent-character functional on its real factor. One can first use smooth elementary tensors, which span a dense subspace at fixed finite level. The compact unipotent quotient makes integration continuous on smooth vectors. Thus the exclusion applies to any contributing discrete realization with the given real row.

**Candidate-D, for cuspidal realizations.** Let $\mathcal C_\pi$ be a specified copy in the cuspidal spectrum. Jiang and Zhang's Proposition 2.2 gives a largest Bessel index $\ell_0(\mathcal C_\pi)$ with nonzero Bessel module for some rational orbit and gives vanishing above that index. Full Fourier visibility is equivalent to nonzero restriction of the full coefficient to the smaller group for some row translate. If the coefficient has a nonzero value at $g$, the right translate by $g$ has a nonzero value at the identity. Combining the proposition with (1) gives

$$
   \ell_0(\mathcal C_\pi)\le r_S,\qquad
   \mathcal F_{\psi_*}|_{\mathcal C_\pi}\ne0
        \quad\Longrightarrow\quad \ell_0(\mathcal C_\pi)=r_S.      \tag{2}
$$

Here $\psi_*$ is the source's reference *rational* character. For $r_S>0$, blindness at the target can occur in the logic of (2) in two ways. All rational classes at the target index may vanish if $\ell_0<r_S$. If $\ell_0=r_S$, the nonzero module supplied at that index may belong to another norm class. Whether either happens for an actual source row has status **O**. The first-occurrence assertion uses cuspidality of the chosen realization. Round 11's discreteness conclusion alone permits the real-place exclusion and the kernel calculation below. [Jiang and Zhang, Proposition 2.2 and Section 2.4](https://annals.math.princeton.edu/wp-content/uploads/annals-v191-n3-p02-s.pdf)

## 3. An exact dimension formula on the row cut

Fix the reference pair $(N,\psi_*)$. Use the entire geometric row space $HH=\operatorname{ran} P$ of the finite- and infinite-place right convolutions of round 11, with the full-space finite-dimensionality and realization hypotheses stated there. Write $D=\dim HH$. Normalize Haar measure of $[N]=N(F)\backslash N(\mathbb A)$ to one and put

$$
  \mathcal F_{\psi_*} f(g)=\int_{[N]} f(ng)\overline{\psi_*(n)}\,dn,
  \qquad K_{\rm glob}=HH\cap\ker\mathcal F_{\psi_*}.
$$

The map on Hilbert classes takes values in $L^2_{\rm loc}(G(\mathbb A))$. To check continuity, take a relatively compact measurable fundamental set for $[N]$, with compact closure $B$, and a compact set $C\subset G(\mathbb A)$. Jensen's inequality and left Haar invariance bound the squared local norm on $C$ by a constant times the squared norm of the automorphic lift on $BC$. The lift on this compact set has bounded overlap, since $G(F)$ is discrete and only finitely many elements occur in $G(F)\cap (BC)(BC)^{-1}$. This bounds each local seminorm by the automorphic $L^2$ norm and also proves independence of representatives. Right translations commute with $\mathcal F_{\psi_*}$. Its kernel is consequently a closed reducing subspace of the unitary right representation. The argument extends the common-kernel calculation on the same domain. [Original Fourier-kernel proof, Section 4.3](../PROOF.md)

**Candidate-D.** Round 11 places the range of $P$ in finitely many discrete isotypic summands. Write each such summand as $M_\pi\otimes\mathcal H_\pi$, where $M_\pi$ is its finite multiplicity space of dimension $m_\pi$, and $\mathcal H_\pi$ is the unitary irreducible representation. On their direct sum, Schur's lemma puts the projection onto the Fourier kernel in the direct sum of the commutants $\operatorname{End}(M_\pi)\otimes I$. Hence the kernel on each summand has the form $K_\pi\otimes\mathcal H_\pi$, for a subspace $K_\pi\subset M_\pi$. Equivalently, $K_\pi$ is the kernel of the linear map sending $a\in M_\pi$ to the continuous intertwiner $v\mapsto\mathcal F_{\psi_*}(a\otimes v)$.

The row convolution acts on that summand as $I\otimes p_\pi$. Put $E_\pi=\operatorname{ran}p_\pi$ and $d_\pi=\dim E_\pi$. Each $d_\pi$ is finite since the whole row cut has finite rank. Intersecting the row cut with the kernel gives

$$
\begin{aligned}
 HH&=\bigoplus_\pi M_\pi\otimes E_\pi,&
 K_{\rm glob}&=\bigoplus_\pi K_\pi\otimes E_\pi,\\
 D&=\sum_\pi m_\pi d_\pi,&
 \dim K_{\rm glob}&=\sum_\pi d_\pi\dim K_\pi,\\
 \operatorname{rank}(\mathcal F_{\psi_*}|_{HH})
   &=\sum_\pi d_\pi\bigl(m_\pi-\dim K_\pi\bigr).
\end{aligned}                                                       \tag{3}
$$

At multiplicity one a single nonzero Fourier function on a smooth vector makes the full coefficient injective on that summand. At higher multiplicity (3) counts independent intertwiners on the multiplicity space. Isomorphic realizations can have linear combinations in the kernel even if two individually chosen copies are visible. Under the absolute unfolding and rational transport hypotheses, $K_{\rm glob}\subseteq\bigcap_u\ker P_u^*$, giving the necessary budget $\epsilon(P)\ge D^{-1}\sum_\pi d_\pi\dim K_\pi$ when $D>0$. The selected finite tests and column spaces enter after the full Fourier map. Their simultaneous rank bound remains **O**. [Round 11, Section 6](../round11/PROOF.md)

**Boundary $r_S=0$.** The group $N$ is trivial and $\mathcal F_{\psi_*}f$ is the automorphic lift of $f$ itself. Thus $K_{\rm glob}=0$ and (3) gives rank $D$. The selected restriction and column pairings can still have a defect.
