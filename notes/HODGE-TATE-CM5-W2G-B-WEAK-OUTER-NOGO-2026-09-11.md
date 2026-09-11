# Hodge-Tate CM5: W2G-B direct weak outer semiregularity no-go

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v84 and the companion Hodge-Tate / Markman / Perry CM5 notes through
`HODGE-TATE-CM5-W2F-PRIMITIVE-ANTI-REAL-NOGO-2026-09-11.md`.

**Date:** 2026-09-11.

This note attacks **Gate W2G-B** exactly as requested: it does not redesign the source secant sheaf and does not impose source `H`-semiregularity. Instead it tests Perry's **weak equivariant semiregularity directly on the Markman outer object** associated to the existing scale-one simple secant sheaf.

The verdict is negative for the current outer object and every finite stabilizer contained in the identity-component Rouquier group. The point is subtle. Weak `G`-semiregularity is genuinely weaker than `G`-semiregularity in general, but for the actual stabilizer of the present outer object the invariant Hochschild category has no nontrivial twisted sectors. Hence the weak condition collapses back to the invariant ordinary semiregularity condition, and the source obstruction found in W2E injects into the outer obstruction space.

This is **not** a no-go for Perry's theorem in general, nor for a different outer object with a nontrivial pure-tensor stabilizer or a genuinely different invariant category.

No `canon/` or registry file is changed. No algebraicity theorem is claimed.

---

## 1. The current source and outer objects

Put

\[
B=\operatorname{Jac}(y^2=x^5-1),
\qquad
X=B\times B,
\]

so `X` is the abelian fourfold used in the preceding secant construction.

W2E-B produced one simple coherent sheaf

\[
G_1\in\operatorname{Coh}(X),
\qquad
\operatorname{ch}(G_1)=\delta=-\gamma,
\]

where

\[
\gamma=v(j-j^{-1})\in\mathcal B.
\]

Let

\[
Z:=X\times X
\]

and form the Markman source outer object

\[
P:=G_1\boxtimes G_1^\vee
\in D^{\mathrm b}(Z).
\]

Let

\[
A:=X\times\widehat X
\]

be the split-Weil abelian eightfold and

\[
\Phi:D^{\mathrm b}(Z)\xrightarrow{\sim}D^{\mathrm b}(A)
\]

Markman's Orlov equivalence. The object to which Perry's theorem would eventually be applied is

\[
\boxed{E:=\Phi(P).}
\]

W2G-B asks whether `E` can be **weakly `G`-semiregular** for a suitable finite subgroup of the identity-component Rouquier group, even though the source sheaf `G_1` was not source-`H`-semiregular.

---

## 2. Perry's weak condition is genuinely different in general

Perry distinguishes two conditions for an object `F` in a category `C` with a finite group action.

1. `F` is `G`-semiregular if it has a `G`-equivariant structure and

\[
\sigma_F^2:
\operatorname{Ext}^2(F,F)^G
\longrightarrow
HH_{-2}(C)
\]

is injective.

2. `F` is **weakly `G`-semiregular** if it admits an equivariant lift

\[
\widetilde F\in C^G
\]

which is ordinarily semiregular **inside the invariant category**:

\[
\sigma_{\widetilde F}^2:
\operatorname{Ext}^2_{C^G}(\widetilde F,\widetilde F)
\longrightarrow
HH_{-2}(C^G)
\]

is injective.

Perry proves that `G`-semiregularity implies weak `G`-semiregularity, but not conversely in general. His equivariant semiregularity theorem uses the weak condition.

References:

- A. Perry, *The semiregularity theorem for equivariant noncommutative varieties*, arXiv:2604.00511v2, Definitions 2.6, Lemma 2.7, Theorems 1.2 and 6.3.
- A. Perry, *Hochschild cohomology and group actions*, Math. Z. 297 (2021), Theorem 4.4, for the sector decomposition of Hochschild invariants.

Thus the negative source-level result of W2E did **not** by itself settle W2G-B. One must inspect the invariant category of the outer object.

---

## 3. Move the group action back through Orlov

Semiregularity is functorial under equivalences: an equivalence induces isomorphisms on both Ext groups and Hochschild homology and intertwines the semiregularity maps.

Therefore a finite Rouquier subgroup stabilizing `E` on `A` may be conjugated through `Phi` to a finite subgroup

\[
\Gamma\subset
Z\times\widehat Z
\]

acting on `D^b(Z)` and stabilizing `P`.

Weak semiregularity of `E` for the original group is equivalent to weak semiregularity of `P` for `Gamma`.

Hence all geometry can be tested on the source product

\[
Z=X\times X.
\]

---

## 4. The outer stabilizer has no pure-tensor kernel

The scale-one sheaf is supported on a smooth ample divisor

\[
Y\subset X.
\]

Its rank-one locus is a dense open subset

\[
U\subset Y.
\]

The outer object `P` has codimension-one support

\[
Y\times Y\subset Z.
\]

Consider a pure tensor autoequivalence in the identity component,

\[
P\longmapsto
P\otimes(p_1^*L_1\otimes p_2^*L_2),
\qquad
L_1,L_2\in\operatorname{Pic}^0(X),
\]

and suppose it fixes `P`.

Restricting to `U x U`, where both factors are line bundles up to the fixed dualization, gives

\[
p_1^*(L_1|_U)\otimes p_2^*(L_2|_U)
\simeq\mathcal O_{U\times U}.
\]

Restricting further to `U x {u}` and `{u} x U` gives

\[
L_1|_U\simeq\mathcal O_U,
\qquad
L_2|_U\simeq\mathcal O_U.
\]

Since `Y` is a smooth ample divisor in an abelian fourfold, restriction

\[
\operatorname{Pic}^0(X)\longrightarrow\operatorname{Pic}^0(Y)
\]

is injective. Therefore

\[
\boxed{L_1=L_2=\mathcal O_X.}
\]

Consequently the translation projection

\[
\Gamma\longrightarrow Z
\]

is injective.

In particular, every nonidentity element of `Gamma` has a nonzero translation part and hence acts on the abelian variety `Z` without fixed points.

This is the load-bearing property for W2G-B.

---

## 5. Twisted Hochschild sectors vanish

For a finite group acting on a dg category, Hochschild homology of the invariant category has the sector decomposition

\[
HH_*(C^\Gamma)
\simeq
\left(
\bigoplus_{g\in\Gamma}HH_*(C,\phi_g)
\right)^\Gamma,
\]

where `phi_g` is the autoequivalence associated to `g`.

Apply this to

\[
C=D^{\mathrm b}(Z).
\]

If

\[
g=(t_z,L)\in Z\times\widehat Z
\]

has `z != 0`, the translation has empty fixed locus. The Hochschild group with coefficients in `phi_g` is supported on that fixed locus and therefore vanishes:

\[
HH_*(C,\phi_g)=0.
\]

Section 4 shows that every nonidentity element of the actual stabilizer has `z != 0`. Hence all nonidentity sectors vanish.

The sector decomposition collapses to

\[
HH_*(C^\Gamma)
\simeq HH_*(C)^\Gamma.
\]

Translations act trivially on cohomology, and tensoring by a degree-zero line bundle has trivial rational Chern character. Hence the identity-component Rouquier action is trivial on ordinary Hochschild homology. Therefore

\[
\boxed{
HH_*(C^\Gamma)\simeq HH_*(C).
}
\]

Under this identification, the Hochschild map induced by the forgetful functor

\[
\mathrm{Forg}:C^\Gamma\to C
\]

is an isomorphism: there are simply no nonidentity sectors left for it to forget.

This is the precise place where the possible weak-semiregularity advantage disappears for the present outer object.

---

## 6. Weak semiregularity collapses to Gamma-semiregularity

For an equivariant lift

\[
\widetilde P\in C^\Gamma
\]

Perry's invariant-category calculation gives

\[
\operatorname{Ext}^2_{C^\Gamma}
(\widetilde P,\widetilde P)
\simeq
\operatorname{Ext}^2_C(P,P)^\Gamma.
\]

Functoriality of the semiregularity map gives a commutative square

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

Both vertical maps are isomorphisms in the present free-projection situation.

Therefore

\[
\boxed{
P\text{ is weakly }\Gamma\text{-semiregular}
\iff
P\text{ is }\Gamma\text{-semiregular}.
}
\]

This equivalence is **not** asserted for arbitrary Perry group actions. It is a consequence of the special stabilizer geometry proved above.

---

## 7. Any outer stabilizer projects to source stabilizers

Write an element of the source Rouquier group of `Z=X x X` as

\[
((a,b),(L_1,L_2)).
\]

If it stabilizes

\[
P=G_1\boxtimes G_1^\vee,
\]

then support preservation gives

\[
Y+a=Y,
\qquad
Y+b=Y.
\]

Restricting an isomorphism of the external products to a smooth rank-one point of the other factor shows that the two components stabilize the individual factors:

\[
t_a^*G_1\otimes L_1\simeq G_1,
\]

and similarly for `G_1^vee` on the second factor.

Let

\[
\Gamma_1
\]

be the image of `Gamma` in the first source Rouquier factor. Then `Gamma_1` is an honest finite stabilizer of the scale-one sheaf `G_1` of exactly the type audited in W2E-A.

The five-adic descent obstruction there gives

\[
\boxed{|\Gamma_1|\le 80.}
\]

The same statement holds for the second projection.

---

## 8. A source kernel always survives in the outer Ext group

W2E-A proved for any compatible source stabilizer `H` of order `h` that

\[
\dim\operatorname{Ext}^2(G_1,G_1)^H
\ge
12+\frac{1600}{h}.
\]

Since

\[
h\le80,
\]

we have

\[
\dim\operatorname{Ext}^2(G_1,G_1)^H
\ge32.
\]

But

\[
\dim HH_{-2}(X)=28.
\]

Therefore the restricted source semiregularity map has a nonzero kernel. For

\[
H=\Gamma_1
\]

choose

\[
0\ne\xi\in
\operatorname{Ext}^2(G_1,G_1)^{\Gamma_1}
\]

such that

\[
\boxed{\sigma^2_{G_1}(\xi)=0.}
\]

Now use the Kunneth summand

\[
\operatorname{Ext}^2(G_1,G_1)
\otimes
\operatorname{Ext}^0(G_1^\vee,G_1^\vee)
\subset
\operatorname{Ext}^2(P,P).
\]

The identity endomorphism of the second factor is invariant under every autoequivalence. Hence

\[
\boxed{
\Xi:=\xi\boxtimes\operatorname{id}_{G_1^\vee}
\in
\operatorname{Ext}^2(P,P)^\Gamma
}
\]

is nonzero.

---

## 9. The surviving class is killed by outer semiregularity

The Atiyah class of an external product is additive:

\[
\operatorname{At}(F\boxtimes H)
=
\operatorname{At}(F)\boxtimes\operatorname{id}_H
+
\operatorname{id}_F\boxtimes\operatorname{At}(H).
\]

Consequently the Buchweitz-Flenner/Perry semiregularity map is multiplicative under external products. On the Kunneth summand above,

\[
\sigma^2_{F\boxtimes H}
(\eta\boxtimes\operatorname{id}_H)
=
\sigma_F^2(\eta)
\boxtimes
\operatorname{ch}(H).
\]

Apply this with

\[
F=G_1,
\qquad
H=G_1^\vee,
\qquad
\eta=\xi.
\]

Then

\[
\boxed{
\sigma_P^2(\Xi)
=
\sigma_{G_1}^2(\xi)
\boxtimes
\operatorname{ch}(G_1^\vee)
=0.
}
\]

Thus the restriction

\[
\sigma_P^2:
\operatorname{Ext}^2(P,P)^\Gamma
\longrightarrow
HH_{-2}(C)
\]

is not injective.

Hence

\[
\boxed{P\text{ is not }\Gamma\text{-semiregular}.}
\]

Section 6 now upgrades this immediately to

\[
\boxed{P\text{ is not weakly }\Gamma\text{-semiregular}.}
\]

Finally, derived equivalence transports the conclusion back to the Markman object:

\[
\boxed{
E=\Phi(P)
\text{ is not weakly }G\text{-semiregular}
}
\]

for every finite identity-component Rouquier stabilizer `G` of this current object.

---

## 10. W2G-B verdict

For the existing scale-one simple secant sheaf and its Markman outer object, Gate W2G-B closes

\[
\boxed{\textbf{FAIL}.}
\]

More precisely:

\[
\boxed{
\text{current }E
+
\text{finite identity-component Rouquier stabilizer}
\Longrightarrow
\text{not weakly semiregular}.
}
\]

The proof uses two independent ingredients:

1. **weak-collapse:** the actual stabilizer has injective translation projection, so all nonidentity Hochschild sectors vanish and weak semiregularity equals invariant ordinary semiregularity;
2. **persistent source kernel:** every allowed first-factor projection has order at most 80, hence retains a nonzero source semiregularity kernel, and that kernel survives as `xi box id` in the outer object.

No dimension estimate on the full outer `Ext^2` is needed.

---

## 11. What remains open

This result closes the most direct Perry weak route for the **current object**, but it leaves genuinely different possibilities:

1. **Change the outer object, not merely the symmetry.** A different secant realization could have a nontrivial pure-tensor stabilizer. Then nonidentity categorical Hochschild sectors need not vanish and weak semiregularity may be strictly weaker than `G`-semiregularity.

2. **Use a genuinely twisted/projective equivariant realization.** The argument above assumes an honest finite stabilizer in the identity-component Rouquier group of the current object. A construction whose natural symmetry only closes after a central extension or Brauer twist may have a different invariant category.

3. **Leave the anti-real/divisor-supported realization entirely.** W2F closed the primitive anti-real family only for the current source-theta implementation. The full four-dimensional rational secant space `mathcal B` remains larger.

4. **Find a single outer object with no factorwise source kernel.** The obstruction in Section 8 comes from the external-product form `G_1 box G_1^vee`. A non-decomposable representative of the same Markman cohomological class could evade that Kunneth kernel.

These are structural redesigns. Enlarging the finite group of the present outer object cannot solve W2G-B.

---

## 12. References

- A. Perry, *The semiregularity theorem for equivariant noncommutative varieties*, arXiv:2604.00511v2, especially Definitions 2.6, Lemma 2.7, Proposition 5.19, Theorems 1.2 and 6.3.
- A. Perry, *Hochschild cohomology and group actions*, Math. Z. 297 (2021), 1273-1292, Theorem 4.4.
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
}
\]
