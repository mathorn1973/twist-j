# Round 13. Cuspidality and multiplicity one in the actual row spectrum

**NON-CANONICAL. No authority. No Canon status change.**

Candidate: C-RH-SEMISTABLE-FRAME-N, alias C-RH-BK-CONCENTRATION-N.
Session owner: ChatGPT-Astra-Sol-20261123-R13. Issue #2070 and draft
PR #2071. The source application below is **candidate-D** under the
genuine-realization and parameter-family hypotheses of round 11. This
round contains no new candidate-C computation or Lean verification.

## 1. Statement and inputs

Let $E/F$ be the source CM extension and $G=U(V)$ the actual ambient
unitary group of the nondegenerate Hermitian space $V$. Write $r=r_S$
and $n_G=k+2r+1$. Let $HH$ be the entire geometric row space, identified
with the abstract target by the fixed full-space transport. A row
constituent is an irreducible automorphic representation $\pi$ whose
discrete isotypic summand has nonzero intersection with this row space.

**Theorem, candidate-D.** Every row constituent has a generic elliptic
global Arthur parameter. Its multiplicities in the discrete and cuspidal
spectra are both one. The actual discrete realization contributing to
$HH$ therefore lies in the cuspidal spectrum.

We use two conclusions of [round 11, Section 4](../round11/PROOF.md#4-from-the-geometric-row-space-to-the-local-satake-bound).
First, the full finite-dimensional row cut is contained in finitely
many discrete automorphic isotypic summands. This follows from the
decomposability of the actual finite and archimedean convolution
operators and the full finite-dimensionality hypothesis. Second, at
every split finite place $v$ where a row constituent $\pi_v$ is
spherical, its normalized Satake multiset is contained in the strict
annulus

$$
q_v^{-1/2}<|\alpha|<q_v^{1/2},
$$

where $q_v$ is the residue field cardinality. In particular, any two
entries have ratio with absolute value strictly between $q_v^{-1}$
and $q_v$. Round 11 derives this using the actual regular weight gaps,
Labesse's discrete base change, the exclusion of nontrivial Speh
blocks in that transfer and the Jacquet–Shalika bound. We keep those
hypotheses and use the annulus as the input to this round.

## 2. A split-place test of the assigned Arthur parameter

The group $G$ is the unitary group of a Hermitian form and hence a pure
inner form of the quasi-split group of the same dimension. The torsor
of isometries from the quasi-split Hermitian form to the given form
supplies the pure inner twist. The unitary case of Chen and Zou applies
to this group, including its odd dimension.

Chen–Zou, Theorem 2.1, assigns each discrete near-equivalence class an
elliptic global Arthur parameter. Apply it to the actual constituent
$\pi$. In their notation its parameter is

$$
\psi=\sum_i\phi_i\boxtimes S_{d_i},
$$

where $\phi_i$ is an appropriate conjugate self-dual cuspidal
automorphic representation of a general linear group over $E$ and
$S_{d_i}$ is the $d_i$-dimensional irreducible representation of
$\mathrm{SL}_2(\mathbb C)$. Their theorem identifies the local
$L$-parameter of $\pi_v$ with $\phi_{\psi_v}$ for almost every $v$.
This chooses the parameter of the actual row via its discrete
near-equivalence class.
[Chen–Zou, §2.1 and Theorem 2.1, pp. 4775–4777](https://ems.press/content/serial-article-files/51452#page=7)
· [Theorem 2.1 and equation (2.4), p. 4777](https://ems.press/content/serial-article-files/51452#page=9).

Choose one split finite place outside the finite exception set of
Theorem 2.1 and outside the ramification sets of $\pi$ and all the
$\phi_i$. Include in the excluded set any places needed for the
unramified identifications of the Hermitian group and its local
parameters. The quadratic extension has infinitely many split places,
so this choice exists. Nothing requires the chosen place to be a word
prime. At the chosen place, $\pi_v$ is spherical and $G(F_v)$ is a
general linear group. Choose one of the two places of $E$ over $v$ to
express its parameter.

Under Chen–Zou's formula (2.4), the block for $\phi_i\boxtimes S_{d_i}$
contributes an unramified string for each Satake eigenvalue $\alpha$ of
the corresponding local $\phi_i$. Up to the convention for Frobenius,
the string has entries

$$
\alpha q_v^{(d_i-1)/2},\quad
\alpha q_v^{(d_i-3)/2},\quad\ldots,\quad
\alpha q_v^{-(d_i-1)/2}.
$$

If $d_i\ge2$, the first two entries already have absolute ratio $q_v$.
Reversing the convention inverts that ratio and leads to the same
contradiction. These entries occur in a multiset, so other blocks
cannot cancel the pair. The strict annulus therefore implies $d_i=1$
for all $i$ at once. This proves genericity of $\psi$. Its ellipticity
makes the pairs $(\phi_i,d_i)$ distinct, so the $\phi_i$ are now
pairwise distinct, with the parity carried by the assigned elliptic
parameter.
[Chen–Zou, ellipticity and genericity definitions, split localization
and equation (2.4), pp. 4776–4777](https://ems.press/content/serial-article-files/51452#page=8).

For this generic elliptic parameter, Theorem 2.6 makes the discrete
near-equivalence class multiplicity-free. Proposition 5.1 applies to
an irreducible $\pi$ with these local $L$-parameters at almost every
place and gives $m_{\rm cusp}(\pi)=m_{\rm disc}(\pi)=m(\pi)$. Since the
row occurs, the first two numbers are both one. The cuspidal spectrum
is a subrepresentation of the discrete spectrum, so the single
discrete copy is the cuspidal copy. This proves the theorem.
[Chen–Zou, Theorem 2.6, p. 4780](https://ems.press/content/serial-article-files/51452#page=12)
· [Proposition 5.1, p. 4790](https://ems.press/content/serial-article-files/51452#page=22).

Here genericity is a statement about the trivial Arthur
$\mathrm{SL}_2$ factors. The proof uses the strict one-half bound.
It supplies neither a global Whittaker functional for this inner
form nor everywhere local temperedness. In particular, the
everywhere-tempered test hypothesis of the refined Bessel-period
formula remains separate.

## 3. The remaining global kernel is a weighted constituent sum

Write $E_\pi$ for the cut of the single actual copy of $\pi$ by the
row projection and $d_\pi=\dim E_\pi$. Put $D=\dim HH>0$. Fix the
source's rational Bessel character $\psi_*$ and its full Fourier map
$\mathcal F_{\psi_*}$ from round 12. That map is continuous into local
$L^2$ and right equivariant. Its closed kernel on a single irreducible
automorphic copy is either zero or the entire copy. Define

$$
\mathcal B_*=\{\pi\text{ contributing to }HH:
                 \mathcal F_{\psi_*}|_\pi=0\}.
$$

The multiplicity-space identity of round 12 now reads

$$
HH=\bigoplus_\pi E_\pi,\qquad
K_{\rm glob}=\bigoplus_{\pi\in\mathcal B_*} E_\pi,\qquad
\dim K_{\rm glob}=\sum_{\pi\in\mathcal B_*}d_\pi.
$$

Absolute unfolding and rational transport give the same necessary
defect bound

$$
\epsilon(P)\ \ge\ \frac{1}{D}\sum_{\pi\in\mathcal B_*}d_\pi.
$$

Thus the unresolved first quantity is the weight of the constituents
in $\mathcal B_*$, measured with their actual row-cut dimensions.
[Round 12, global kernel formula and the $r_S=0$ boundary](../round12/GLOBAL_OBSTRUCTIONS.md#3-an-exact-dimension-formula-on-the-row-cut).

Jiang–Zhang's first-occurrence theorem can now be applied to each
irreducible constituent contributing to $HH$, in its unique cuspidal
realization. An arbitrary vector in $HH$ may mix different constituents;
no single first-occurrence index is assigned to such a mixture. The real-place hook
exclusion of round 12 gives $\ell_0(\pi)\le r_S$. A nonzero full
coefficient for $\psi_*$ forces equality. Equality by itself allows
the first nonzero Bessel module to occur at a different rational
orbit of the same hook. For $r_S=0$, the full Fourier map is the
automorphic lift and $\mathcal B_*$ is empty.
[Jiang–Zhang, Proposition 2.2 and §2.4](https://annals.math.princeton.edu/2020/191-3/p02)
· [Round 12, first-occurrence scope](../round12/GLOBAL_OBSTRUCTIONS.md#2-what-global-first-occurrence-would-establish).

For $r_S>0$, the weight of $\mathcal B_*$ remains **O**. Even empty
$\mathcal B_*$ would leave the simultaneous rank inequality for
the actual unaveraged maps $Q_u$ on all target subspaces. Those maps
retain the selected finite translates and column tests. Cuspidality
and multiplicity one account for the discrete row realizations and
do not provide these remaining period ranks.
[Round 12, exact rank requirement](../round12/PROOF.md#7-exact-consequence-for-concentration).
