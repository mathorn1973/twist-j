# Hodge-Tate CM5: W2D ordinary semiregularity breaker

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v83 and the companion Hodge-Tate / Markman CM5 notes through
`HODGE-TATE-CM5-MARKMAN-W2C-COHERENT-SHEAF-2026-09-11.md`.

**Date:** 2026-09-11.

This note attacks **Gate W2D** for the explicit coherent secant sheaf constructed in W2C. The verdict is negative for ordinary Buchweitz-Flenner semiregularity of that specific object, and in fact there is a stronger scale-four dimension obstruction. This is a breaker for the present W2C sheaf, not for the whole CM5 Weil lane.

No `canon/` file is changed, no public claim is registered, no formal public probe is started, and no algebraicity theorem is claimed.

## 1. The W2C object

Let

\[
X=B\times B,
\qquad
B=\operatorname{Jac}(y^2=x^5-1),
\]

and let

\[
\gamma=v(j-j^{-1})\in\mathcal B,
\qquad
\delta=-\gamma.
\]

W2C constructed one coherent secant sheaf `G` with

\[
\boxed{\operatorname{ch}(G)=4\delta=-4\gamma.}
\]

Write

\[
F_0=i_*(\mathcal M|_Y),
\]

where `Y` is the ample divisor of class

\[
L=5D-E,
\qquad
2c_1(\mathcal M)=L.
\]

The first elementary modification used only one of four summands:

\[
F_0^{\oplus4}\twoheadrightarrow T,
\]

where `T` is the curve sheaf on the complete-intersection curve `C`. The second modification used one of the remaining untouched summands:

\[
K_1\twoheadrightarrow\mathcal O_Z.
\]

Consequently the construction contains more direct-sum structure than was needed for the Chern-character calculation.

Put

\[
F_C:=\ker(F_0\to T),
\qquad
F_Z:=\ker(F_0\to\mathcal O_Z).
\]

Then the two kernels split literally as

\[
K_1\simeq F_C\oplus F_0^{\oplus3}
\]

and

\[
\boxed{
G\simeq F_C\oplus F_Z\oplus F_0^{\oplus2}.
}
\]

This direct-sum decomposition is the first W2D breaker.

## 2. The Markman object

Let

\[
P_G:=G\boxtimes G^\vee
\]

on `X x X`, and let

\[
E_G:=\Phi(P_G)
\]

be Markman's object on the split-Weil eightfold `A=X x Xhat`, where `Phi` is the relevant Orlov equivalence.

Because `G` contains `F_0^2`, the external product contains

\[
P_0^{\oplus4},
\qquad
P_0:=F_0\boxtimes F_0^\vee.
\]

Since an equivalence preserves direct sums and Ext groups,

\[
\boxed{
E_G\text{ contains }E_0^{\oplus4},
\qquad E_0:=\Phi(P_0).
}
\]

## 3. Exact self-Ext groups of the basic divisor sheaf

The divisor `Y` is an ample divisor in the abelian fourfold `X`. The line bundle of `Y` has

\[
L^4=9600,
\]

so

\[
h^0(X,\mathcal O_X(Y))=\frac{L^4}{4!}=400.
\]

For a smooth member `Y`, Kodaira vanishing on the abelian variety and the two exact sequences

\[
0\to\mathcal O_X(-Y)\to\mathcal O_X\to\mathcal O_Y\to0
\]

and

\[
0\to\mathcal O_X\to\mathcal O_X(Y)\to N_{Y/X}\to0
\]

give

\[
h^\bullet(\mathcal O_Y)=(1,4,6,403)
\]

and

\[
h^\bullet(N_{Y/X})=(403,6,4,1).
\]

Because `F_0=i_*(M|Y)` and `M|Y` extends to `X`, the standard two-term divisor resolution has zero differential after applying `Hom(-,F_0)`. Hence

\[
\operatorname{Ext}^k_X(F_0,F_0)
\simeq
H^k(Y,\mathcal O_Y)
\oplus
H^{k-1}(Y,N_{Y/X}).
\]

Therefore

\[
\boxed{
(\dim\operatorname{Ext}^0,\ldots,\dim\operatorname{Ext}^4)
=(1,407,12,407,1).
}
\]

In particular,

\[
\operatorname{Ext}^2_X(F_0,F_0)\ne0.
\]

For

\[
P_0=F_0\boxtimes F_0^\vee,
\]

Kunneth gives

\[
\dim\operatorname{Ext}^2(P_0,P_0)
=2\cdot1\cdot12+407^2
=165673.
\]

Thus the repeated block in `E_G` has a very large non-zero degree-two deformation space.

## 4. A literal kernel of the ordinary semiregularity map

For a perfect complex `E`, the ordinary semiregularity map in degree two is built from the categorical trace of powers of the Atiyah class. In particular, on a repeated direct summand

\[
E_0\otimes\mathbf C^4
\]

it factors through the ordinary matrix trace on the multiplicity factor.

Take any non-zero

\[
\xi\in\operatorname{Ext}^2(E_0,E_0)
\]

and any non-zero traceless matrix

\[
A\in\mathfrak{sl}_4.
\]

Then

\[
\xi\otimes A
\in
\operatorname{Ext}^2(E_0^{\oplus4},E_0^{\oplus4})
\]

is non-zero, while every semiregularity trace of this class contains

\[
\operatorname{tr}(A)=0.
\]

Hence

\[
\boxed{
\xi\otimes A\in\ker\sigma^2_{E_G}.
}
\]

Therefore

\[
\boxed{
E_G\text{ is not ordinarily semiregular.}
}
\]

This conclusion is exact and does not depend on a genericity assumption or a numerical approximation.

## 5. The Hochschild target has dimension 8008

There is also a representation-independent size obstruction which becomes useful for redesigns.

For an abelian variety of dimension `g`,

\[
h^q(\Omega^p)=\binom gp\binom gq.
\]

The target of the degree-two semiregularity map on the abelian eightfold is

\[
HH_{-2}(A)
\simeq
\bigoplus_{p=0}^{6}H^{p+2}(A,\Omega_A^p).
\]

Thus

\[
\dim HH_{-2}(A)
=
\sum_{p=0}^{6}\binom8p\binom8{p+2}
=
\binom{16}{6}
=
\boxed{8008}.
\]

For comparison, on the abelian fourfold `X`,

\[
\dim HH_{-2}(X)
=
\sum_{p=0}^{2}\binom4p\binom4{p+2}
=28.
\]

## 6. Exact Riemann-Roch size of the secant class

For the unscaled class `delta=-gamma`, write

\[
\delta=L+\frac1{24}L^3-Q.
\]

The W2C intersection arithmetic gives

\[
L^4=9600,
\qquad
LQ=800.
\]

Since `X` is abelian, `td(X)=1`. The class `delta` has only odd codimension, so duality changes its sign. Hence

\[
\chi(\delta,\delta)
=
-\int_X\delta^2
=
-\frac1{12}L^4+2LQ
=
\boxed{800}.
\]

For any object with Chern character

\[
\operatorname{ch}(G_m)=m\delta,
\]

one therefore has the exact self-Euler characteristic

\[
\boxed{
\chi(G_m,G_m)=800m^2.
}
\]

For the W2C sheaf, `m=4`, so

\[
\boxed{
\chi(G,G)=12800.
}
\]

## 7. Scale four is too large even for a simple redesign

Suppose one discarded the direct-sum construction and somehow found a **simple** coherent sheaf `G_m` with

\[
\operatorname{ch}(G_m)=m\delta.
\]

Write

\[
e_i:=\dim\operatorname{Ext}^i_X(G_m,G_m).
\]

On the abelian fourfold, Serre duality gives

\[
e_4=e_0,
\qquad
e_3=e_1.
\]

For a simple object, `e_0=1`. Riemann-Roch then gives

\[
e_2
=800m^2-2+2e_1
\ge800m^2-2.
\]

For the outer product

\[
P_m=G_m\boxtimes G_m^\vee,
\]

Kunneth gives

\[
\dim\operatorname{Ext}^2(P_m,P_m)
=2e_0e_2+e_1^2
\ge1600m^2-4.
\]

Orlov equivalence preserves this dimension. Ordinary semiregularity would require injection into an `8008`-dimensional target. Consequently

\[
1600m^2-4>8008
\]

for every

\[
\boxed{m\ge3.}
\]

Thus:

\[
\boxed{
\text{no simple scale-}m\ge3\text{ secant representative can make the Markman outer-product object ordinarily semiregular.}
}
\]

In particular, at the W2C scale `m=4`, even an ideal simple replacement would have

\[
\dim\operatorname{Ext}^2(P_4,P_4)
\ge25596>8008.
\]

This is stronger than the direct-summand breaker for the specific `G`.

The dimension test does **not** exclude

\[
m=1\quad\text{or}\quad m=2,
\]

for which the corresponding lower bounds are respectively

\[
1596
\quad\text{and}\quad
6396.
\]

## 8. What Perry's 2026 theorem changes

Alexander Perry's 2026 semiregularity theorem extends the Buchweitz-Flenner mechanism to equivariant noncommutative settings and twisted derived categories. In particular, the relevant condition can be weakened from injectivity on the full `Ext^2` space to an appropriate equivariant or invariant semiregularity condition.

That distinction is load-bearing here. The large ordinary `Ext^2` spaces above do not by themselves rule out injectivity on a much smaller finite-group invariant part.

The present note does **not** claim such an equivariant structure for `G`. The divisors and the length-1920 zero-dimensional correction in W2C were chosen for existence, not with a frozen finite symmetry. Thus Perry's theorem supplies a new route, not an automatic closure.

There is nevertheless a natural arithmetic scale for such a route. For the ample line bundle of class `L`,

\[
h^0(L)=400,
\]

so its polarization kernel has order

\[
|K(L)|=400^2=160000.
\]

A maximal isotropic subgroup of the theta group has order `400`. This is the natural finite-symmetry size to examine in an equivariant redesign. No descent or semiregularity claim is made here from this count alone.

## 9. Correct W2D verdict

The ordinary-semiregularity branch for the explicit W2C object closes **FAIL**:

\[
\boxed{
\sigma^2_{E_G}\text{ is not injective.}
}
\]

The failure is structural:

1. `G` contains two identical copies of `F_0`;
2. `E_G` consequently contains four identical `E_0` blocks;
3. traceless multiplicity directions lie in the semiregularity kernel;
4. independently, the scale-four Chern character is already too large for ordinary semiregularity even after a hypothetical simple redesign.

This does not contradict any preceding gate. W2B and W2C only required cohomological non-vanishing and existence of coherent secant sheaves. They did not prove semiregularity.

## 10. Next gate: W2E

The lane now forks cleanly.

### W2E-A: equivariant weak semiregularity

Construct a finite group `H` acting on the split-Weil datum and an `H`-equivariant secant object whose Chern character retains a non-zero Weil projection, then test Perry's weak `H`-semiregularity criterion on the invariant obstruction space

\[
\operatorname{Ext}^2(E,E)^H.
\]

The theta-group arithmetic above suggests looking first at isotropic translation subgroups associated with the polarization `L`.

### W2E-B: lower-scale coherent secant redesign

Construct a coherent secant sheaf with

\[
\operatorname{ch}(G_m)=m\delta
\]

for `m=1` or `m=2`, avoiding repeated summands, and test ordinary semiregularity there. The W2C construction used `m=4` only because

\[
4Q=L_-DL_+
\]

was an immediate complete-intersection class; the dimension calculation shows that reducing this scale is now mathematically essential, not cosmetic.

A successful lane may combine both strategies.

## 11. External references

- E. Markman, *Secant sheaves on abelian n-folds with real multiplication and Weil classes on abelian 2n-folds with complex multiplication*, arXiv:2509.23079. Markman's general CM strategy explicitly leaves semiregularity of the resulting object open.
- A. Perry, *The semiregularity theorem for equivariant noncommutative varieties*, arXiv:2604.00511. Perry develops the equivariant and twisted semiregularity mechanism relevant to the next fork.

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
ordinary semiregularity of W2C G    FAIL
lower-scale / equivariant redesign  OPEN
algebraic deformation of HW         OPEN
```

The exact lesson from W2D is that the factor-four coherent construction solved the sheaf-existence problem at the price of making ordinary semiregularity impossible. Perry's equivariant theorem and the still-possible scales `m=1,2` are the two mathematically live exits.