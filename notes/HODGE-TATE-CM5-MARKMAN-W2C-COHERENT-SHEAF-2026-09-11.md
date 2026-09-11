# Hodge–Tate CM5: explicit coherent secant sheaf closing W2C

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v83 and the companion Hodge–Tate / Markman CM5 notes through
`HODGE-TATE-CM5-MARKMAN-W2C-KTHEORY-SHEAF-BOUNDARY-2026-09-11.md`.

**Date:** 2026-09-11.

This note closes the coherent-sheaf realization part of **Gate W2C**. It changes no `canon/` file, registers no public claim, starts no formal public probe, and makes no algebraicity claim for the generic Weil deformation. The remaining open step is semiregularity of the Markman transform.

## 1. Setting

Let
\[
K=\mathbf Q(j)=\mathbf Q(\zeta_5),\qquad F=K^+=\mathbf Q(\sqrt5),
\]
and
\[
B=\operatorname{Jac}(y^2=x^5-1),\qquad X=B\times B.
\]
The preceding note introduced the two real-embedding components `A` and `B` of the `F`-linear polarization and the rational divisor classes
\[
D=A+B,\qquad E=\sqrt5(A-B),\qquad A^3=B^3=0.
\]
The class `D` is the rational trace of the `F`-polarization, hence the product principal polarization on `X`.

For the anti-real secant class
\[
s=j-j^{-1},\qquad \gamma=v(s)\in\mathcal B,
\]
put `delta=-gamma`. Its degree-two part is
\[
L:=\delta_2=5D-E.
\]
The previous divisor-supported ansatz had discrepancy
\[
Q:=\frac1{24}L^3-\delta_6=5D^3-DE^2=20AB(A+B).
\]

## 2. Integral ample divisor classes

Under the principal polarization, `D` corresponds to the identity symmetric endomorphism and is integral. The class `E` corresponds to the integral Rosati-symmetric real-multiplication endomorphism
\[
R=\operatorname{diag}(\sqrt5,-\sqrt5),
\]
so `E` is integral as well.

Define
\[
L_-:=5D-E,\qquad L_+:=5D+E.
\]
Because
\[
\frac{5\mp\sqrt5}{2}\in\mathcal O_F,
\]
one has
\[
\frac{L_-}{2},\frac{L_+}{2}\in\operatorname{NS}(X).
\]
Both are ample: their two real eigenvalues are the totally positive numbers
\[
q'=\frac{5-\sqrt5}{2},\qquad q=\frac{5+\sqrt5}{2}.
\]
Choose line bundles `P,L_-,L_+,M` with first Chern classes respectively
\[
D,\quad 5D-E,\quad 5D+E,\quad \frac{5D-E}{2}.
\]

## 3. The correction class is a complete-intersection class

Since `D=A+B` and `A^3=B^3=0`,
\[
D^3=3AB(A+B),
\]
so
\[
\boxed{Q=\frac{20}{3}D^3.}
\]
More importantly,
\[
L_-DL_+=(5D-E)D(5D+E)=80(A^2B+AB^2),
\]
whereas
\[
Q=20(A^2B+AB^2).
\]
Hence
\[
\boxed{L_-DL_+=4Q.}
\]

## 4. An effective curve

Choose effective divisors
\[
Y\in|\mathcal L_-|,\qquad H\in|\mathcal P|,\qquad Y_+\in|\mathcal L_+|.
\]
After general translations they meet properly. Set
\[
C:=Y\cap H\cap Y_+.
\]
Then `C` is an effective one-dimensional local complete-intersection cycle and
\[
\boxed{[C]=L_-DL_+=4Q.}
\]
Thus the effective-curve problem isolated in the preceding note is solved exactly.

## 5. The divisor-supported sheaf

Let `i:Y->X` and set
\[
F_0:=i_*(\mathcal M|_Y).
\]
In `K_0(X)`,
\[
[F_0]=[\mathcal M]-[\mathcal M(-Y)],
\]
so
\[
\operatorname{ch}(F_0)=e^{L_-/2}(1-e^{-L_-})
=L_-+\frac1{24}L_-^3.
\]

## 6. The curve quotient

Let `k:C->X` and put
\[
T:=k_*(\mathcal M|_C).
\]
The Koszul resolution gives
\[
\operatorname{ch}(T)=e^{L_-/2}(1-e^{-L_-})(1-e^{-D})(1-e^{-L_+}).
\]
Only codimensions three and four survive:
\[
\operatorname{ch}(T)=4Q-\ell[\mathrm{pt}],
\]
where
\[
\ell=\frac12\int_X(D+L_+)L_-DL_+.
\]
Since `D` is a principal polarization on the abelian fourfold,
\[
D^4=4!=24.
\]
As `D^4=6A^2B^2`, one gets `A^2B^2=4`. Using
\[
L_-DL_+=80(A^2B+AB^2)
\]
and
\[
D+L_+=(6+\sqrt5)A+(6-\sqrt5)B,
\]
one obtains
\[
\int_X(D+L_+)L_-DL_+=3840,
\]
hence
\[
\boxed{\ell=1920.}
\]
Thus
\[
\boxed{\operatorname{ch}(T)=4Q-1920[\mathrm{pt}].}
\]

## 7. Two elementary modifications

Restriction to `C subset Y` gives a natural surjection
\[
F_0\twoheadrightarrow T.
\]
Use one summand to define
\[
F_0^{\oplus4}\twoheadrightarrow T
\]
and let `K_1` be its kernel. Then
\[
\operatorname{ch}(K_1)
=4L_-+\frac16L_-^3-4Q+1920[\mathrm{pt}].
\]
But
\[
4\delta=-4\gamma=4L_-+\frac16L_-^3-4Q.
\]
So only the positive point class remains.

Because the first map uses only one summand, `K_1` contains three untouched copies of `F_0`. Choose a zero-dimensional subscheme
\[
Z\subset Y\setminus C,\qquad \operatorname{length}(Z)=1920,
\]
and use one untouched summand to obtain a quotient
\[
K_1\twoheadrightarrow\mathcal O_Z.
\]
Let
\[
0\longrightarrow G\longrightarrow K_1\longrightarrow\mathcal O_Z\longrightarrow0.
\]
Then `G` is one coherent sheaf on `X` and
\[
\boxed{\operatorname{ch}(G)=4\delta=-4\gamma.}
\]
Since `gamma` belongs to the rational secant space `mathcal B`,
\[
\boxed{\operatorname{ch}(G)\in\mathcal B.}
\]
Thus `G` is a genuine coherent Markman `mathcal B`-secant sheaf.

## 8. Markman's cohomological criterion survives

The preceding W2C note proved that `gamma tensor gamma` has non-zero `BB_1` projection on all four Weil lines and non-zero `BB_0` scalar component. Here
\[
\operatorname{ch}(G)\otimes\operatorname{ch}(G)=16\,\gamma\otimes\gamma.
\]
Therefore exactly the same non-vanishing conditions hold, and one may take
\[
\boxed{G'=G}
\]
in Markman's cohomological criterion.

## 9. W2C verdict

The effective-cycle and coherent-sheaf parts of Gate W2C close **AGREE**:
\[
\boxed{\exists\,G\in\operatorname{Coh}(X),\qquad \operatorname{ch}(G)=-4\gamma\in\mathcal B.}
\]
No virtual difference of sheaves remains.

The construction is explicit:

```text
L_- = 5D-E
L_+ = 5D+E
C   = Y cap H cap Y_+
[C] = L_- D L_+ = 4Q
F_0 = i_*(M|Y),  2c1(M)=L_-
F_0^4 -> M|C
kernel K_1
K_1 -> O_Z,  length(Z)=1920
kernel G
ch(G) = -4 gamma
```

## 10. Next gate: W2D semiregularity

Let `Phi` denote Markman's Orlov equivalence and form the derived object from `G box G^vee`. Markman's current general-CM strategy requires the appropriate semiregularity of this object to deform the normalized algebraic class along the split-Weil family.

The next exact gate is therefore:

1. form the exact object `E_G` from `G box G^vee`;
2. compute or bound `Ext^2(E_G,E_G)`;
3. write the Atiyah/obstruction map in the CM5 character decomposition;
4. prove injectivity of the semiregularity map on the obstruction image, or identify its exact kernel;
5. only then pass to flat algebraic deformation of the Weil component.

Alexander Perry's 2026 semiregularity theorem for equivariant noncommutative varieties supplies a stronger deformation theorem than was available in Markman's original paper, but it does not by itself compute the required map for this explicit cyclic-C4 object.

## 11. External references

- E. Markman, *Secant sheaves on abelian n-folds with real multiplication and Weil classes on abelian 2n-folds with complex multiplication*, arXiv:2509.23079.
- A. Perry, *The semiregularity theorem for equivariant noncommutative varieties*, arXiv:2604.00511.

## 12. Final boundary

```text
CM5 carrier                         DONE
polarized CM realization            DONE
Hodge census                        DONE
split generalized-Weil eightfold    DONE
Markman F-realization               DONE
cyclic-C4 secant pair               DONE
perfect-complex realization         DONE
coherent secant sheaf               DONE
semiregularity                      OPEN
algebraic deformation of HW         OPEN
```

The previous effective-curve obstruction collapses to the complete-intersection identity
\[
\boxed{4Q=(5D-E)D(5D+E),}
\]
and an explicit two-stage elementary modification produces the required coherent secant sheaf.