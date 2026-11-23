# Round 14. Independent mathematical review

**NON-CANONICAL. No authority or Canon status change.** The deductions below are **candidate-D**. The arithmetic application retains the genuine unitary-group realization, full row cut and fixed transport of rounds 11–13. The actual mixed-subspace defect bound remains **O**. This review uses paper arguments and source inspection.

## A central power after periodization

**Candidate-D.** At every good split finite place $v$, a positive power of the ambient scalar uniformizer acts by a single scalar on the entire actual row space $HH$. At the same time its translation takes the original local seed support into a disjoint double coset. This gives an actual instance where periodization restores invariance.

Write $w,\bar w$ for the two places of $E$ over $v$, and identify $G(F_v)$ with $\mathrm{GL}_{n_G}(F_v)$ using $w$. Write $z_v$ for the finite central idele equal to $\varpi_v I$ there and to the identity elsewhere. Its scalar over $E$ has valuations $1,-1$ at $w,\bar w$. Choose $v$ outside the exceptional finite data of all words, so $K_v$ is hyperspecial and $x_{u,v}\in K_v$. For $r_S>0$ every element of $S_{u,v}=N_v H_{u,v}$ fixes the first nonzero isotropic flag vector. For $r_S=0$ it fixes the distinguished vector of nonzero norm. Scale the resulting vector $b_u$ in the $w$-component to be primitive in the lattice defining $K_v$. Every $g\in S_{u,v}z_v^jK_v$ satisfies

$$
\|g^{-1}b_u\|=|\varpi_v|^{-j}\|b_u\|
$$

in the lattice norm. Thus different integers $j$ give disjoint shells. The raw seed has support over the shell $j=0$, and translating a nonzero seed by any nonzero power moves its support off that shell. Inversion of the right-translation convention only changes the sign of $j$. [Pinned finite flag group and seed support, lines 51–54 and 156–166](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/PoincareInHH.lean#L156-L166)

Let $h$ be the class number of $E$. Choose $\beta\in E^\times$ with $(\beta)=\mathfrak w^h$. Then $b=\beta/\bar\beta\in Z(G)(F)$, and $k=z_v^h b_f^{-1}$ is an integral finite central unit at every place. The intersection of the compact group of such units with $K_2$ is open and has finite index. Choose $s>0$ with $k^s\in K_2$. In the full adelic group,

$$
(1,z_v^{hs})=b^s\,(b_\infty^{-s},1)\,(1,k^s).
$$

Right translation by the rational central factor acts trivially on the automorphic quotient. For every $f\in HH$ the actual row correspondence gives $f=I_f(w_0)$ with the same irreducible archimedean representation $\Sigma$ and equivariant $I_f$. Schur's lemma gives the same central character $\omega_\Sigma$ on every row. The finite row convolution is the normalized average weighted by $\overline{\chi_2}$ on $K_2$. Left translation of the averaging variable gives right action by $\chi_2(k^s)$ on its range. Consequently

$$
R(1,z_v^{hs})|_{HH}
=\omega_\Sigma(b_\infty)^{-s}\chi_2(k^s)\,I_{HH}.
$$

This scalar has modulus one and preserves every periodized word image. The argument supplies a positive power for each $v$ and leaves the action of the first power on each individual image open. [Finiteness of the class number, Milne, Theorem 4.4](https://www.jmilne.org/math/CourseNotes/ANT.pdf#page=72) · [Pinned archimedean row correspondence, lines 49–65](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/RowsDef.lean#L49-L65) · [Pinned finite character projector, lines 264–265](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean#L264-L265)

## How much the spectral separation proves

**Candidate-D.** Ramakrishnan's Theorem A applies to the generic isobaric transfers over $E$ because $E/F$ is quadratic. Away from the finitely many ramified primes, degree-one primes over $F$ come in pairs over split places. Conjugate self-duality supplies the other member's contragredient, so agreement at one consistently chosen place of each pair gives the theorem's hypothesis. Finitely many contributing parameters require only finitely many separating spherical Hecke tests. Two constituents in the same generic packet have identical parameters at the good split places. Multiplicity one counts automorphic realizations and gives no additional separation there. [Ramakrishnan, Theorem A](https://arxiv.org/pdf/1806.08429#page=1) · [Chen–Zou, Theorems 2.1 and 2.6](https://ems.press/content/serial-article-files/51452#page=9)

For the resulting scalar algebra $T=\sum_\alpha t_\alpha e_\alpha$, every $T$ is normal. An invariant subspace decomposes under its distinct eigenvalue projectors, which are polynomials in $T$, and hence reduces $T$. If $Q_u$ projects orthogonally onto the word image, invariance is therefore equivalent to $[T,Q_u]=0$. The $(\alpha,\beta)$ block is $(t_\alpha-t_\beta)e_\alpha Q_u e_\beta$. Equality of coefficients along the graph edges is both necessary and sufficient, including for singular $T$. The graph describes the largest subalgebra inside the specified compressed good-split Hecke algebra.

## Rank loss and sharpness

**Candidate-D.** In the primal defect, replacing an image $I_u$ by its block-split core $I_u^-$ decreases $\dim(I_u\cap W)$ by at most $\ell_u^-=\dim I_u-\dim I_u^-$. Replacing it by the sum of its block projections $I_u^+$ increases that dimension by at most $\ell_u^+=\dim I_u^+-\dim I_u$. Both assertions follow by injection of the difference quotient into the ambient quotient. Choose the smaller cost independently for each word. The total possible downward error plus the total possible upward error is then $\sum_u\min(\ell_u^-,\ell_u^+)$. The replacement family splits, so its objective attains its maximum at a split subspace. Comparing there and at an original maximizer gives the stated bound for $\epsilon-\epsilon_{\rm split}$ after division by total source dimension $R$. The kernel contribution stays fixed in this comparison.

For sharpness, take $s\ge1$ copies of each coordinate line in $\mathbb C^D$, $D\ge2$, and $D$ copies of the line $L=\mathbb C(1,\ldots,1)$. All columns together span the target. The normalized cost is $\lambda=1/(s+1)$, since only the copies of $L$ contribute. The split maximum is zero. A proper $W$ containing $j$ axes and $L$ has dimension at least $j+1$, giving objective at most $\lambda-1/D-j\lambda/D$. If $L$ is absent, the column count is at most $s\dim W$. The line $L$ and the whole space attain the two possible maximal values, so $\epsilon=\max(0,\lambda-1/D)$. Taking $D$ large shows that coefficient one is sharp even at arbitrarily small fixed $\lambda=1/(s+1)$ with injective joint adjoint.

Conversely, for two coordinate blocks take the two lines spanned by $(1,t)$ and $(t,1)$, with $0<t<1$. Both split cores are zero and both split enlargements fill the plane, so the normalized cost is one. The two lines span the plane and have defect zero. Their orthogonal projectors converge to the coordinate projectors as $t\to0$. Even arbitrarily small commutators in norm allow full rank cost.

Finally, in the four-column example of round 13 every pair of columns has positive inner product. Products of two image projectors are therefore nonzero multiples of the outer products of their column vectors. Three independent columns give nine independent outer products, so the image projectors generate all of $\operatorname{End}(\mathbb C^3)$. The verified defect is $1/12$. Treating the generated algebra itself as image-preserving would erase that witness. [Round 13, four-column proof](../round13/TEST_SPACE.md#an-exact-four-column-example)

## Scope, authority and custody

This is internal paper opposition by a separate Astra lane, with a
development Astra, a Sol source reader and the coordinator. It is not an
external referee report, blind code confirmation or Lean verification.
The opponent cross-read the full main proof and source note. The
coordinator separately read the pinned source passages used for the
support, projector, row-intertwiner and convergence claims, and the
primary statements of Ramakrishnan, Chen-Zou and Milne. Small TeX and
section-reference corrections were made before delivery; no mathematical
falsifier or scientific run is hidden by these edits.

The result identifies the preserving algebra inside the stated family
of Hecke operators; it does not assert that all possible symmetries are
in that family. The exact image-preserving graph reduction and the
rank-cost bound are sufficient tools. An accidental split maximizer can
exist even when individual images do not split. Automorphic multiplicity
one does not imply multiplicity one for a finite-level algebra.

The main mathematical source remains RH commit
`40e56bab026552e089d7afcfeff08d2defb9c005`. The source note gives exact
paths and anchors. The re-read Git blobs were HidaSetting
`7f21195438209fd7fc4d0b081fe53297f07fb9c4`, PoincareInHH
`7bf59cba2a1bbcb1c81a5182c4155de354f9def4`, RowsDef
`713c562806ba024c53e9545072004dc59435091e` and GlobAut
`2103e49fe83fce42d4962f85acd9d4f6a589d645`. Source interfaces retain
their genuine suppliers. No external implementation is imported;
the notes contain original exposition and reference links.

PUBLIC was selected. STATUS was read first at current main
`ed3b1878d95825ab9473c16416c8db76cc152079`, unchanged since round 13.
POLICY, AGENTS, CORE and FRONTIER were read at this basis. The declared
v116 content/tag ancestry and five normative hashes remain those
verified at this identical main and recorded in round12/SOURCE_MAP.md.
The exact-main aggregate `138025181448` and architecture checks
`138022828681` and `138022828135` were fetched again and were successful.
The full 392-head remote inventory, 100 recent open issues, current PR
state and relevant registry entries were checked. Scope and ownership
were recorded in issue #2070 before edits under session
`ChatGPT-Astra-Sol-20261123-R14`. The adjacent #2065/#2067 item remains
separately owned.

The continuation starts from public commit
`272400b2a3ee66f33bf643c941bf0f9562edcce1`, tree
`cc80494d97086fa2ff2e5e40702895a60b374003`, on the same draft PR #2071.
Only round14/ and the parent index/handoff change. All earlier proof
files, scientific code, thresholds and first-run records are untouched.
There was no new scientific computation, so no new preregistration,
candidate-C result or architecture claim is made. Repository policy and
Canon checks concern delivery integrity only. No Canon, registry,
workflow, merge or release action is part of this continuation.
