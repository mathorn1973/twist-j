# Round 9: the local word-prime level and a sharp obstruction to concentration shortcuts

**NON-CANONICAL. No authority. No Canon status changes.**

Candidate: C-RH-SEMISTABLE-FRAME-N, continuing the same item and draft PR #2071.
Owner: A. M. Thorn. Session: ChatGPT-Astra-Sol-20261123-R9.
New paper deductions: **candidate-D**. Exact finite audit: separately preregistered, at most **candidate-C**.
Source pin: leanprover-community/riemann-hypothesis at 40e56bab026552e089d7afcfeff08d2defb9c005.

## 1. What this round establishes

There are two distinct advances.

1. In the concrete primitive split Hida realization, the smaller group's actual level at a word prime is conjugate to K_1 of exponent one. Consequently every irreducible local constituent has an explicitly bounded test space: zero for conductor at least two, one for conductor one, and an exactly computable integer between one and k for conductor zero. Genericity is not needed for this statement.
2. An explicit family simultaneously has injective maps, full target span, exact Hecke block balance, literal finite-group averaging of independent raw seeds, a single orbit of Fourier characters, injective full Fourier coefficients, and equality in every relevant off-diagonal pairwise Gram bound. Its concentration defect is still asymptotically one half of the square root of the density parameter.

The second statement isolates the limitation of the audited information. It does not identify the constructed family with the actual automorphic family. The first statement supplies genuine additional information about that family, but it is an upper bound and a selection rule for local test spaces, not a lower bound for global period ranks.

The concrete/abstract transport still requires the fixed SIso and the actual PMat construction described in the parent PROOF.md. An arbitrary existential MatS witness is insufficient. All source-level conclusions retain the cited realization and analytic hypotheses. No Lean compilation was performed.

## 2. Individual kernels are already exponentially small

Write A_u=P_u/sqrt(c_0(u)) for the source's positive normalization, d_u=dim C_u, R=sum d_u and D=dim HH. The source diagonal bound reads

    ||A_u^* A_u - I||_HS^2 <= e_0 d_u.

Every vector in ker A_u is a zero eigenvector of A_u^* A_u and contributes one to this squared norm. Therefore

    dim ker P_u <= e_0 d_u,
    kappa := sum_u dim ker P_u / R <= e_0.                 (2.1)

This is a direct paper consequence of the existing diagonal input, not a new analytic estimate. The source's MatSF bound sqrt(e_0)<=E, E=exp(-x^(eps/8)), yields

    kappa <= exp(-2 x^(eps/8)).                            (2.2)

The normalization and diagonal hypothesis apply to the constructed full-space PMat witness; see SOURCE_MAP.md. We do not infer positivity of c_0 or validity of the diagonal estimate without their construction hypotheses.

For the intertwined Hecke blocks let p_alpha=d_alpha/R be the source mass, q_alpha=D_alpha/D the target mass, and b_alpha=r_alpha/R the image mass, where r_alpha=sum_u rank A_{u,alpha}. Put beta=TV(p,q), and B=sum_alpha(q_alpha-b_alpha)_+. The parent block budget gives

    max(kappa,beta) <= B <= kappa+beta,
    B <= eps(A) <= B + sum_alpha min(q_alpha,b_alpha) e_alpha.       (2.3)

Here e_alpha is the intrinsic reduced-image defect within the block, with zero-weight terms omitted. Thus the individual-kernel term is no longer an unidentified obstruction under these analytic inputs. The unknown is the weighted intrinsic term, after accounting for the separately supplied target counting error beta.

Credit boundary: the centered frame estimates and their comparison with Brox's formulation belong to issue #2065 / PR #2067. We use that information; we do not claim to replace it by (2.1).

## 3. A sharp family satisfying all the audited abstract properties

### 3.1 Incidence construction

Choose integers t>=2 and m>=2t^2. Put s=t^2 and rho=s/m. First consider a rational probability space of subsets S of {0,...,m-1}. Its cardinality K has distribution

    P(K=s-t)=P(K=s+t)=(1-rho)/2,
    P(K=s)=rho.

Conditional on K, choose S uniformly among the K-element subsets. Clear denominators to obtain a finite set Y of coordinate copies with D=|Y|. For word u let I_u be the coordinate subspace of F=C^Y supported on the coordinates whose subset contains u, and let A_u:I_u -> F be inclusion.

Every map is isometric and injective. Every coordinate belongs to at least one image because s-t>0; hence the images span F. Direct moment computations give

    E K=s,    Var(K)=s(1-rho),
    E[K(K-1)]=s^2(1-1/m).

Consequently, for every u and every distinct u,v,

    d_u=d=rho D,       R=m d=sD,
    ||A_u^* A_v||_HS^2=dim(I_u intersect I_v)=rho^2 D=d^2/D.       (3.1)

Thus the off-diagonal inequality is met with equality for every pair, not merely on average. In source-style notation this is D_*=D and e_0=eta_0=eta_1=0.

### 3.2 Exact defect over every complex subspace

Let P_u be the orthogonal projection onto I_u, and put Q=(D/R)sum_u P_u. Its coordinate eigenvalues are K/s.

For an arbitrary complex subspace W, the projection-trace inequality gives

    dim(W intersect I_u) <= tr(P_W P_u).

It follows that

    sum_u dim(W intersect I_u)/R - dim W/D
       <= tr(P_W(Q-I))/D
       <= tr((Q-I)_+)/D.                                   (3.2)

The coordinate subspace W_+ supported on K=s+t attains equality in both inequalities. Therefore the maximum over ALL complex subspaces, including non-coordinate subspaces, is exactly

    eps(A)=(1-rho)/(2t)
          = (1-rho) sqrt(sigma)/2,    sigma=D/R=1/s.         (3.3)

The normalized target variance is

    ||Q-I||_HS^2/D=(1-rho)/s.                               (3.4)

For comparison, the usual trace bound for isometries with pairwise energies at most d_u d_v/D gives eps(A)<=sqrt(sigma-sum_u(d_u/R)^2)/2. In this family sum_u(d_u/R)^2=1/m=rho sigma. The ratio of (3.3) to sqrt(sigma)/2 tends to one as rho tends to zero. Taking t to infinity and m/t^2 to infinity excludes any general o(sqrt(sigma)) conclusion from these hypotheses.

The source-to-target dimension ratio rho can be arbitrarily small. The obstruction is therefore not confined to large individual images. This does not assert that every adelic or scale relation of the actual source is realized by this abstract family.

### 3.3 A smaller exact realization

For prime m one need not enumerate all subsets. For each K=s-t,s,s+t, take all affine images a{0,...,K-1}+b in F_m, labeled by a nonzero and b arbitrary. Give each label multiplicity m-s at the two outer K values and 2s at the middle value.

The affine group is doubly transitive. Hence the same first and second incidence moments hold exactly. In this realization,

    D=2m^2(m-1),  d=2m(m-1)s,
    dim(I_u intersect I_v)=2s^2(m-1).

The frozen audit checks this construction for eight specified pairs. Weighted labels are not confused with distinct coordinate copies.

### 3.4 Actual finite-group averaging, with no common Fourier blindness

Let N=(Z/2)^m and Gamma=C_m, with Gamma rotating the m coordinates of N. Work with normalized counting measure on the semidirect product N semidirect Gamma. Define

    f_u(n,h)=(-1)^(n_u).

These m functions are orthonormal. Left translation by N gives distinct characters, and left translation by Gamma permutes them transitively. Their Gamma averages all equal

    b=(f_0+...+f_(m-1))/m,       ||b||^2=1/m.

Use the raw source spaces I_u tensor C f_u. Their direct sum is injectively embedded because the f_u are orthogonal. Genuine left Gamma averaging maps y tensor f_u to y tensor b. After a common nonzero normalization, these are exactly the inclusion maps of the preceding construction, in the target C^Y tensor C b.

For every v, the full N-character projection on this target is

    y tensor b -> y tensor f_v/m.

It is injective. Thus the common Fourier-blind target kernel is zero; in fact every one of these full coefficients is injective. The remaining rank loss comes from testing these coefficients only against the selected subspaces I_u. Nonvanishing of complete Fourier coefficients does not give the needed ranks after that restriction.

This rules out a stronger shortcut than the earlier averaging example: even removing the common Fourier-blind kernel does not control the intrinsic defect.

### 3.5 Exact generic Hecke balance does not repair the defect

Before imposing a generic character, tensor all spaces and maps by C[G], the regular representation of any finite group G. Every map is the identity on this factor, so it intertwines the full group algebra. If G is a finite general linear group (or a product of such groups), apply the generic unipotent projector e_psi.

The e_psi corner decomposes into generic blocks. Their common source and target weights are

    p_alpha=q_alpha=b_alpha
            =dim(rho_alpha)/[G:U]

when the Gelfand-Graev multiplicities are one. The same construction works with general multiplicities by retaining them in numerator and denominator.

In each block the family remains I_u tensor V_alpha. Its normalized occupancy operator is Q tensor I, so the proof of (3.2)-(3.3) gives the same intrinsic defect e_alpha=eps(A). Hence

    kappa=0, beta=0, B=0,
    sum_alpha min(q_alpha,b_alpha)e_alpha=eps(A).            (3.5)

The exact audit uses G=S_3=GL_2(F_2), whose nontrivial unipotent-character corner has block dimensions one and two. The paper construction also permits the full finite residue groups appearing in the source.

**Scope of the negative result, candidate-D:** the conjunction of the properties in Sections 3.1-3.5 cannot imply an exponential intrinsic-defect estimate. Additional properties of the actual period maps are required. This is a statement about a proposed inference, not a refutation of the RH claim or of its other hypotheses.

## 4. The actual local word-prime level

### 4.1 Source hypotheses and their precise scope

Fix the concrete Hida realization and a finite place v above the same word prime T_u. Assume v is split in the CM extension and v(T_u)=1. In the source's completely split family this holds at every place above T_u; HidaSetting alone does not assert that complete-splitting theorem. The corresponding supplier and its hypotheses are listed in SOURCE_MAP.md.

The source fixes the hyperbolic vectors e_a,f_a and the vector z_u pointwise in the smaller group. The smaller finite level is

    K_u=H_u(A_f) intersect x_u K_2 x_u^{-1}.

The integral hyperbolic splitting leaves a lattice L_b of hermitian rank k+1, containing z_u with norm -T_u. Fu_fixed includes unimodularity, a lattice lift and the coefficient condition

    c z_u in L_sub  implies c in O_E.

The rational isotropic span is X. From the integral hyperbolic splitting and the orthogonality relations, L_sub=X+L_b and X intersect L_b=0. Therefore

    L_b intersect E z_u=O_E z_u.                            (4.1)

This saturation localizes and completes at both members of the split CM pair. The hyperbolic lattice is self-dual, so its orthogonal complement L_b is self-dual too. At the split place the two primitive components of z_u become a primitive vector z in L=O_v^(k+1) and a primitive covector ell in L^*, with

    ell(z)=-T_u=:varpi,       v(varpi)=1.                    (4.2)

Primitivity of both components is essential. It is supplied by (4.1), rather than added as an unproved generic-position assumption.

The norm witness T_norm also implies T_u=1 modulo g, and hence T_u does not divide g. At v, x_u is integral and K_2 imposes no congruence restriction beyond preserving the ambient lattice. The local level character is trivial: a locally supported such element belongs, after conjugation, to K(g), on which the normalized character is one. Equivalently its character argument is an integral adele and psiEf_int applies.

### 4.2 A lattice calculation

Since ell is primitive, choose t_0 in L with ell(t_0)=1. Put

    M=L intersect ker ell,     w=z-varpi t_0.

Then L=M direct_sum O_v t_0, w belongs to M, and w is primitive because its reduction equals the nonzero reduction of z.

An element fixing both z and ell is determined by C in GL(M tensor F_v). It satisfies

    g_C(t_0)=t_0+(w-Cw)/varpi.                              (4.3)

It preserves L in both directions if and only if

    C in GL(M),       Cw=w modulo varpi M.                 (4.4)

Necessity follows by restriction to M and then (4.3). Conversely (4.4) makes (4.3) integral; C^{-1} satisfies the same congruence, so the inverse is integral as well.

Choose w as the last basis vector of M. The resulting subgroup is

    K_col={ C in GL_k(O_v): C e_k=e_k mod varpi }.

Let

    K_1(varpi)={ C in GL_k(O_v): last row(C)=e_k^t mod varpi },
    d=diag(I_(k-1),varpi^(-1)).

Then K_col=d K_1(varpi) d^{-1}. This is conjugation inside GL_k(F_v), so it preserves the fixed-space dimension of the SAME representation. No switch to a contragredient and no determinant-one condition are needed.

The source identities r=k+m-1 and r_S=m/2-1 give r=k+2r_S+1, so this k is the actual smaller-group rank.

**Conclusion, candidate-D:** the actual local (K_u,psi_K) condition at this split word prime is conjugate to (K_1(varpi),1).

As a check on volume, its index in GL_k(O_v), using the integral column realization, is q_v^k-1. Under complete splitting at all f=[F:Q] places, the product of these indices is (T_u^k-1)^f. This is a subgroup index, not an automorphic multiplicity or a period rank.

At split places away from gT_u, ell(z) is a unit and L=M direct_sum O_v z. The same calculation gives the full GL_k(O_v) level.

## 5. An exact local dimension rule, without genericity

Let tau be an irreducible smooth complex representation of GL_k(F_v), and let c(tau) be its standard conductor exponent. The local field has characteristic zero.

The classical theorem of Atobe, Kondo and Yasuda attaches a nondecreasing nonnegative integer tuple lambda_tau of total weight c(tau). Their invariant-space theorem gives dimension one at its distinguished subgroup and vanishing for every tuple of smaller total weight. The tuple (0,...,0,1) defines K_1(varpi). Thus c>=2 gives zero, and c=1 gives one. For c=0 the tuple is zero, so tau is spherical.

In the spherical case write its Satake multiset as unramified characters. Split that multiset into lines under multiplication by nu=|.|_v. On each line choose a representative chi and let a_j be the finite-support multiplicity sequence of chi nu^j. Define

    r(tau)=sum_lines sum_j max(a_j-a_(j-1),0).              (5.1)

This is independent of the chosen origin on each line. Then

    dim tau^{K_u,v} =
        r(tau),  if c(tau)=0;
        1,       if c(tau)=1;
        0,       if c(tau)>=2.                             (5.2)

In particular 1<=r(tau)<=k. For a generic spherical representation r(tau)=k; the trivial representation has r(tau)=1.

Proof of the spherical formula. For every height h>=1, take the connected intervals of {j:a_j>=h}. Their number is (5.1). Two such intervals are nested or separated by at least one missing integer. Thus their Zelevinsky segments are pairwise unlinked. A segment of unramified GL_1 characters has a one-dimensional determinant-character subrepresentation. By the classical unlinked-segment criterion their parabolic induction is irreducible; it is spherical and has the prescribed Satake multiset, hence is tau.

Every inducing determinant character is trivial on the relevant maximal compact subgroup. Iwasawa decomposition reduces K_1-fixed vectors to functions on a finite parabolic double-coset set. There is one orbit for each block, indexed by the position of the first or last occupied block in the nonzero residue covector/vector convention. The number of orbits is r(tau). Equivalently, the Mackey formula in Atobe-Kondo-Yasuda Proposition 5.2 counts r(tau) filtrations of the simple O_v-module O_v/varpi. This proves (5.2). The generic specialization also follows from the classical oldform formula.

Examples, obtained from (5.1) without numerical computation:
- k mutually unlinked singleton characters: r=k.
- One consecutive string of k distinct characters: r=1, the determinant-character case.
- A single line with multiplicities (1,2,1): r=2 in rank four.
- k identical characters: r=k, not one.

The rank-four example and the repeated-character example show why counting distinct characters or just connected components of their support would give a wrong answer.

This is a local dimension calculation. If every place above T_u is split, the product of the local test-space dimensions is at most k^f, independently of the size of T_u; it is zero if any conductor exceeds one and exactly one when every conductor is one. Global multiplicities and all other local factors remain to be supplied.

## 6. What must still be known about the periods

### 6.1 The actual matrix coefficient is a weighted period

The source's perLaw_holds identifies the pairing against P_u with an outer integral of Bessel periods of translated row forms against evaluated column forms. The inner period is attached to the pair U(k) inside U(k+2r_S+1). Rescaling the hermitian form by -1/T_u normalizes the distinguished vector without changing either unitary group; the hyperbolic dual vectors and additive character must be rescaled consistently.

The whole P_u coefficient is not automatically a single unweighted scalar Bessel functional. A theorem producing some nonzero test vector does not identify the source's selected vector or prevent cancellation in its outer integral.

### 6.2 What the global period theorems can and cannot supply

Beuzart-Plessis and Chaudouard's 2025 unitary Gan-Gross-Prasad theorem concerns cuspidal data with the stated discrete Hermitian weak base-change hypotheses. Its nonvanishing criterion implies that a vanishing central Rankin-Selberg value kills the full relevant Bessel functional under those hypotheses. Their refined formula additionally assumes everywhere local temperedness and evaluates factorizable tests through local factors.

For this application, a vanishing full functional also kills the outer average. The reverse inference needs the correct packet member, the actual local tests and their outer averaging. The reviewed source interfaces do not by themselves establish all these hypotheses for every counted row or supply all the required central values.

The new local result (5.2) resolves the size and conductor support of the word-prime test space. It does not supply its Bessel functional values. Even a one-dimensional test space may be annihilated by the relevant functional.

### 6.3 A precise necessary rank test

The dual concentration identity, valid for arbitrary finite-dimensional maps, is

    eps(P)=max_{V<=HH} [dim V/D - sum_u rank(P_u^*|V)/R].    (6.1)

Suppose an actual automorphic decomposition has been supplied. For a selected sum V_I of row constituent slices, let N_u(I) contain the column constituent slices still allowed to pair with them, after ONLY proved exclusions. Such exclusions may come from a zero local Hom-space, conductor cutoff (5.2), a vanishing full global period under an applicable theorem, or a verified zero on the actual selected test.

Then the image of P_u^*|V_I lies in those surviving column slices, so

    rank(P_u^*|V_I) <= min(dim V_I, sum_{Sigma in N_u(I)} dim C_(u,Sigma)).

Therefore

    eps(P) >= dim V_I/D
              - (1/R) sum_u min(dim V_I,
                         sum_{Sigma in N_u(I)} dim C_(u,Sigma)).   (6.2)

This is an obstruction certificate if its right-hand side is positive. No missing actual row constituent is claimed to have been found. Passing this necessary test would not prove the opposite rank inequality: the surviving periods may still be dependent.

For an upper bound on the intrinsic defect one needs a uniform lower bound on the ranks in (6.1), for all subspaces in the retained block. Counting nonzero scalar periods alone is insufficient. Local multiplicity one is an upper bound on the space of functionals, not a lower bound on these finite-dimensional ranks.

## 7. Outcome and next mathematical target

The source's own diagonal estimate handles individual kernel mass. The exact local word-prime calculation handles a genuinely source-specific part of the column spectrum. The sharp family proves that the remaining global rank condition cannot be recovered merely from the audited frame, Hecke-balance and Fourier properties.

A concrete next target is now available: decompose an actual Hecke block into its global row and column constituents, apply the explicit word-prime rule (5.2), and evaluate the resulting Bessel tests at the source's specified translate and character. That data can feed (6.2), the rank certificates in the parent note, or a proof of a uniform lower bound in (6.1).

The exponential intrinsic-defect estimate for the actual maps remains **open**. None of the results here upgrades the status of the RH claim.

## References and verification status

SOURCE_MAP.md gives pinned source anchors and primary mathematical references.
PREREG.md fixes the exact finite audit and its limits before computation.
RESULTS.md records actual first-run outcomes; REVIEW.md records the internal opponents' objections and their dispositions.
