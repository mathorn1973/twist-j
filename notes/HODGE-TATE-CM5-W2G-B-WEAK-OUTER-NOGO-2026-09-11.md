# Hodge-Tate CM5: W2G-B direct weak outer semiregularity no-go

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v84 and the companion Hodge-Tate / Markman / Perry CM5 notes through
`HODGE-TATE-CM5-W2F-PRIMITIVE-ANTI-REAL-NOGO-2026-09-11.md`.

**Date:** 2026-09-11.

This note attacks **Gate W2G-B** directly. It does not redesign the source secant sheaf and does not assume source `H`-semiregularity. Instead it tests Perry's **weak equivariant semiregularity on the Markman outer object itself**.

The verdict is negative for the current outer object and every finite stabilizer contained in the identity-component Rouquier group. Weak `G`-semiregularity is genuinely weaker than `G`-semiregularity in general. For the stabilizer of the present object, however, the invariant Hochschild category has no nonidentity twisted sectors, so the weak condition collapses to invariant ordinary semiregularity. A source obstruction from W2E then survives in the outer Ext group.

This is **not** a no-go for Perry's theorem in general, nor for a different outer object with a nontrivial pure-tensor stabilizer, a projective/twisted action, or a non-decomposable outer representative.

No `canon/` or registry file is changed. No algebraicity theorem is claimed.

---

## 1. Current source and outer objects

Put

\[
B=\operatorname{Jac}(y^2=x^5-1),
\qquad
X=B\times B.
\]

W2E-B produced a simple coherent sheaf

\[
G_1\in\operatorname{Coh}(X),
\qquad
\operatorname{ch}(G_1)=\delta=-\gamma,
\qquad
\gamma=v(j-j^{-1})\in\mathcal B.
\]

Set

\[
Z:=X\times X,
\qquad
P:=G_1\boxtimes G_1^\vee\in D^{\mathrm b}(Z).
\]

Let

\[
A:=X\times\widehat X
\]

be the split-Weil abelian eightfold and let

\[
\Phi:D^{\mathrm b}(Z)\xrightarrow{\sim}D^{\mathrm b}(A)
\]

be Markman's Orlov equivalence. The final object is

\[
\boxed{E:=\Phi(P).}
\]

W2G-B asks whether `E` can be **weakly `G`-semiregular** for a suitable finite subgroup of the identity-component Rouquier group, even though the source sheaf `G_1` was not source-`H`-semiregular.

---

## 2. Perry's weak condition is genuinely different in general

For a finite group action on a category `C`, Perry distinguishes:

1. `G`-semiregularity: an equivariant object `F` for which

\[
\sigma_F^2:
\operatorname{Ext}^2(F,F)^G\to HH_{-2}(C)
\]

is injective;

2. **weak `G`-semiregularity**: an equivariant lift

\[
\widetilde F\in C^G
\]

which is semiregular inside the invariant category,

\[
\sigma_{\widetilde F}^2:
\operatorname{Ext}^2_{C^G}(\widetilde F,\widetilde F)
\to HH_{-2}(C^G)
\]

injective.

Perry proves that `G`-semiregularity implies weak `G`-semiregularity; the converse is not part of the definition and need not hold in general. His deformation theorem uses the weak condition. Thus W2E did not by itself settle W2G-B.

---

## 3. Move the action back through Orlov

Semiregularity is functorial under exact equivalences: Ext groups and Hochschild homology are identified and the semiregularity maps commute with those identifications.

Therefore a finite Rouquier subgroup stabilizing `E` may be conjugated through `Phi` to a finite subgroup

\[
\Gamma\subset Z\times\widehat Z
\]

stabilizing `P`. Weak semiregularity of `E` is equivalent to weak semiregularity of `P` for this transported action.

Hence it suffices to work on

\[
Z=X\times X.
\]

---

## 4. The outer stabilizer has no pure-tensor kernel

The sheaf `G_1` is supported on a smooth ample divisor

\[
Y\subset X
\]

and is a line bundle on a dense open set `U subset Y`. Consequently `P` has support `Y x Y` and is rank one on `U x U`.

Suppose a pure tensor element fixes `P`:

\[
P\otimes(p_1^*L_1\otimes p_2^*L_2)\simeq P,
\qquad
L_1,L_2\in\operatorname{Pic}^0(X).
\]

Restricting to `U x U`, then to `U x {u}` and `{u} x U`, gives

\[
L_1|_U\simeq\mathcal O_U,
\qquad
L_2|_U\simeq\mathcal O_U.
\]

Since `Y` is a smooth ample divisor in an abelian fourfold, restriction

\[
\operatorname{Pic}^0(X)\to\operatorname{Pic}^0(Y)
\]

is injective. Hence

\[
\boxed{L_1=L_2=\mathcal O_X.}
\]

Thus the translation projection

\[
\Gamma\to Z
\]

is injective. Every nonidentity element of `Gamma` has a nonzero translation part, and therefore acts on the abelian variety `Z` without fixed points.

---

## 5. Hochschild homology has no nonidentity sectors

For a finite group acting on a dg category, the Hochschild homology of the equivariant category admits the twisted-sector decomposition

\[
HH_*(C^\Gamma)
\simeq
\left(
\bigoplus_{g\in\Gamma}HH_*(C;\phi_g)
\right)^\Gamma.
\]

For Hochschild **homology**, this decomposition is supplied directly by Nordstrom's finite-group theorem; Perry's earlier 2021 paper provides the analogous group-action formalism on Hochschild cohomology.

Apply the homology decomposition to

\[
C=D^{\mathrm b}(Z).
\]

If

\[
g=(t_z,L)\in Z\times\widehat Z
\]

has `z != 0`, its translation component has empty fixed locus. The corresponding twisted Hochschild group is supported on the derived fixed locus and vanishes:

\[
HH_*(C;\phi_g)=0.
\]

By Section 4 every nonidentity element of the actual stabilizer has `z != 0`. Hence all nonidentity sectors vanish and

\[
HH_*(C^\Gamma)\simeq HH_*(C)^\Gamma.
\]

Translations act trivially on `H^q(Z,Omega_Z^p)`, and tensoring by a degree-zero line bundle has rational Chern character `1`. Via HKR, the identity-component Rouquier action is therefore trivial on ordinary Hochschild homology. Thus

\[
\boxed{HH_*(C^\Gamma)\simeq HH_*(C).}
\]

Under this identification, the Hochschild map induced by the forgetful functor is an isomorphism. There are no extra nonidentity sectors for the invariant category to retain.

---

## 6. Weak semiregularity collapses to Gamma-semiregularity

For an equivariant lift

\[
\widetilde P\in C^\Gamma,
\]

characteristic zero gives

\[
\operatorname{Ext}^2_{C^\Gamma}(\widetilde P,\widetilde P)
\simeq
\operatorname{Ext}^2_C(P,P)^\Gamma.
\]

Functoriality of semiregularity gives the commutative square

\[
\begin{array}{ccc}
\operatorname{Ext}^2_{C^\Gamma}(\widetilde P,\widetilde P)
&\xrightarrow{\sigma_{\widetilde P}^2}&
HH_{-2}(C^\Gamma)\\
\downarrow\wr && \downarrow\wr\\
\operatorname{Ext}^2_C(P,P)^\Gamma
&\xrightarrow{\sigma_P^2}&
HH_{-2}(C).
\end{array}
\]

The right vertical map is an isomorphism by Section 5. Therefore

\[
\boxed{
P\text{ weakly }\Gamma\text{-semiregular}
\iff
P\text{ }\Gamma\text{-semiregular}.
}
\]

This equivalence is asserted only for the present free-translation-projection stabilizer, not for arbitrary Perry actions.

---

## 7. Every outer stabilizer projects to source stabilizers

Write a source Rouquier element of `Z=X x X` as

\[
((a,b),(L_1,L_2)).
\]

If it stabilizes

\[
P=G_1\boxtimes G_1^\vee,
\]

support preservation gives

\[
Y+a=Y,
\qquad
Y+b=Y.
\]

Restricting an external-product isomorphism to a smooth rank-one point of the other factor gives

\[
t_a^*G_1\otimes L_1\simeq G_1,
\]

and analogously for the dual second factor.

Let `Gamma_1` be the image of `Gamma` in the first source Rouquier factor. It is an honest finite stabilizer of the scale-one sheaf `G_1` of the type audited in W2E-A. The five-adic descent obstruction there gives

\[
\boxed{|\Gamma_1|\le80.}
\]

The same statement holds for the second projection.

---

## 8. A source kernel survives in outer Ext

W2E-A proved for every compatible source stabilizer `H` of order `h` that

\[
\dim\operatorname{Ext}^2(G_1,G_1)^H
\ge12+\frac{1600}{h}.
\]

For

\[
h\le80
\]

this gives

\[
\dim\operatorname{Ext}^2(G_1,G_1)^H\ge32.
\]

But

\[
\dim HH_{-2}(X)=28.
\]

Therefore the source semiregularity map restricted to invariants has nonzero kernel. For `H=Gamma_1`, choose

\[
0\ne\xi\in\operatorname{Ext}^2(G_1,G_1)^{\Gamma_1},
\qquad
\boxed{\sigma_{G_1}^2(\xi)=0.}
\]

The Kunneth decomposition contains

\[
\operatorname{Ext}^2(G_1,G_1)
\otimes
\operatorname{Ext}^0(G_1^\vee,G_1^\vee)
\subset
\operatorname{Ext}^2(P,P).
\]

Since the identity endomorphism is invariant under conjugation, the class

\[
\boxed{
\Xi:=\xi\boxtimes\operatorname{id}_{G_1^\vee}
\in\operatorname{Ext}^2(P,P)^\Gamma
}
\]

is nonzero.

---

## 9. Outer semiregularity kills the surviving class

The Atiyah class of an external product is additive:

\[
\operatorname{At}(F\boxtimes H)
=
\operatorname{At}(F)\boxtimes\operatorname{id}_H
+
\operatorname{id}_F\boxtimes\operatorname{At}(H).
\]

Hence the Buchweitz-Flenner/Perry semiregularity map is multiplicative on the relevant Kunneth summand:

\[
\sigma_{F\boxtimes H}^2
(\eta\boxtimes\operatorname{id}_H)
=
\sigma_F^2(\eta)\boxtimes\operatorname{ch}(H).
\]

Taking

\[
F=G_1,
\qquad H=G_1^\vee,
\qquad \eta=\xi,
\]

gives

\[
\boxed{
\sigma_P^2(\Xi)
=
\sigma_{G_1}^2(\xi)\boxtimes\operatorname{ch}(G_1^\vee)
=0.
}
\]

Thus

\[
\sigma_P^2:
\operatorname{Ext}^2(P,P)^\Gamma\to HH_{-2}(C)
\]

is not injective. Therefore `P` is not `Gamma`-semiregular, and Section 6 gives

\[
\boxed{P\text{ is not weakly }\Gamma\text{-semiregular}.}
\]

Derived equivalence transports the conclusion to the Markman object:

\[
\boxed{
E=\Phi(P)
\text{ is not weakly }G\text{-semiregular}
}
\]

for every finite identity-component Rouquier stabilizer `G` of this current object.

---

## 10. W2G-B verdict

For the existing scale-one simple secant sheaf and its Markman outer object,

\[
\boxed{\textbf{W2G-B = FAIL}.}
\]

More precisely,

\[
\boxed{
\text{current }E
+
\text{finite identity-component Rouquier stabilizer}
\Longrightarrow
\text{not weakly semiregular}.
}
\]

The proof has two independent load-bearing pieces:

1. **weak-collapse:** the actual stabilizer has injective translation projection, so all nonidentity Hochschild sectors vanish and weak semiregularity equals invariant ordinary semiregularity;
2. **persistent source kernel:** every allowed first-factor projection has order at most 80, hence a nonzero source semiregularity kernel survives as `xi box id` in the outer object.

No dimension estimate on the full outer `Ext^2` is required.

---

## 11. What remains open

The current object is exhausted, but genuinely different constructions remain:

1. **Non-decomposable outer representative.** Replace `G_1 box G_1^vee` by an object with the same useful cohomological Markman component but without the factorwise Kunneth kernel `xi box id`.

2. **Nontrivial pure-tensor stabilizer.** A different secant realization could admit finite stabilizer elements with zero translation projection. Then nonidentity Hochschild sectors can survive and weak semiregularity can again be strictly weaker than `G`-semiregularity.

3. **Projective/twisted equivariance.** A central extension, gerbe or Brauer-twisted realization may lead to a different invariant category than the honest stabilizer treated here.

4. **Full secant-space redesign.** W2F closed only the primitive anti-real family for the source-theta implementation. The full four-dimensional rational secant space `mathcal B` is larger.

These are structural redesigns. Merely enlarging the finite group of the present outer object cannot reopen W2G-B.

---

## 12. References

- A. Perry, *The semiregularity theorem for equivariant noncommutative varieties*, arXiv:2604.00511v2, Definitions 2.6, Lemma 2.7, Proposition 5.19, Theorems 1.2 and 6.3.
- V. Nordstrom, *Finite group actions on dg categories and Hochschild homology*, Canadian Mathematical Bulletin 68 (2025), no. 4, 1088-1108, DOI 10.4153/S000843952500030X.
- A. Perry, *Hochschild cohomology and group actions*, Mathematische Zeitschrift 297 (2021), 1273-1292.
- E. Markman, *Secant sheaves on abelian n-folds with real multiplication and Weil classes on abelian 2n-folds with complex multiplication*, arXiv:2509.23079.
- Companion notes `HODGE-TATE-CM5-PERRY-W2E-A-THETA-SYMMETRY-BREAKER-2026-09-11.md` and `HODGE-TATE-CM5-W2F-PRIMITIVE-ANTI-REAL-NOGO-2026-09-11.md`.

---

## 13. Final boundary

```text
CM5 carrier                                      DONE
split generalized-Weil datum                     DONE
Markman F realization                            DONE
explicit secant pair                             DONE
scale-one simple coherent secant sheaf           DONE
ordinary semiregularity of current outer object  FAIL
source G-semiregularity via theta symmetry       FAIL
primitive anti-real redesign W2F                 FAIL
weak G-semiregularity of current outer object    FAIL  <-- W2G-B

open next:
non-decomposable outer representative / twisted stabilizer / full secant-space redesign
```

The load-bearing W2G-B statement is

\[
\boxed{
\text{for the current Markman outer object, Perry weak semiregularity does not reopen the source-closed theta lane.}
\]
