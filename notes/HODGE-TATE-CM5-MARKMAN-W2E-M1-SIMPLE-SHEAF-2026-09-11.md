# Hodge-Tate CM5: scale-one simple secant sheaf and the support-motion breaker

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v83 and the companion Hodge-Tate / Markman CM5 notes through
`HODGE-TATE-CM5-MARKMAN-W2D-SEMIREGULARITY-BREAKER-2026-09-11.md`.

**Date:** 2026-09-11.

This note attacks the lower-scale branch **W2E-B**. It proves that the scale-one class

\[
\delta=-\gamma
\]

is the Chern character of one **simple coherent secant sheaf** on `X=B x B`. Thus the scale-four factor used in W2C is not an integrality obstruction. The same explicit scale-one construction nevertheless fails ordinary semiregularity for a new reason: it moves with the full 399-dimensional linear system of its support divisor.

No `canon/` file is changed, no public claim is registered, no formal public probe is started, and no algebraicity theorem is claimed.

## 1. Setting

Let

\[
B=\operatorname{Jac}(y^2=x^5-1),
\qquad
X=B\times B,
\]

and let `Theta` be the canonical principal theta divisor on `B`. Put

\[
\Theta_1=p_1^*[\Theta],
\qquad
\Theta_2=p_2^*[\Theta].
\]

The rational trace polarization from the preceding notes is the product principal polarization

\[
\boxed{D=\Theta_1+\Theta_2.}
\]

The real-multiplication class `E` corresponds, under this principal polarization, to the Rosati-symmetric endomorphism

\[
\operatorname{diag}(\sqrt5,-\sqrt5).
\]

As before, define

\[
L:=5D-E,
\qquad
2c_1(\mathcal M)=L,
\]

and

\[
\delta=-\gamma
=L+\delta_6.
\]

The divisor-supported class

\[
F_0=i_*(\mathcal M|_Y),
\qquad [Y]=L,
\]

has

\[
\operatorname{ch}(F_0)
=L+\frac1{24}L^3
=\delta+Q,
\]

with

\[
Q=5D^3-DE^2=\frac{20}{3}D^3.
\]

The W2C construction multiplied this identity by four in order to factor `4Q` as a complete intersection. Here we realize `Q` itself.

## 2. Q is already an effective theta-curve class

On the principally polarized abelian surface `B`,

\[
\Theta^2=2[\mathrm{pt}].
\]

Therefore

\[
D^3
=3(\Theta_1^2\Theta_2+\Theta_1\Theta_2^2)
=6\bigl([\mathrm{pt}]\times\Theta+\Theta\times[\mathrm{pt}]\bigr).
\]

Hence

\[
\boxed{
Q
=40\bigl([\mathrm{pt}]\times\Theta+\Theta\times[\mathrm{pt}]\bigr).
}
\]

Thus the scale-one correction is effective already at the level of curve classes.

The remaining issue is to realize it in a form whose top Chern-character contribution vanishes, so that no zero-dimensional correction is needed.

## 3. Diagonal and anti-diagonal cancellation

Let

\[
i_+(x)=(x,x),
\qquad
i_-(x)=(x,-x)
\]

be the diagonal and anti-diagonal embeddings of `B` into `X`.

The Kunneth decomposition of `i_{+*}[\Theta]` has degrees `(2,4)`, `(3,3)`, and `(4,2)`. Applying `1 x [-1]` changes the sign only of the `(3,3)` part. Therefore

\[
\boxed{
i_{+*}[\Theta]+i_{-*}[\Theta]
=2\bigl(\Theta\times[\mathrm{pt}]+[\mathrm{pt}]\times\Theta\bigr).
}
\]

This can also be checked by pairing with arbitrary degree-two classes on either factor.

Now restrict `L` to either graph. Under the product principal polarization,

\[
D\leftrightarrow\operatorname{diag}(1,1),
\qquad
E\leftrightarrow\operatorname{diag}(\sqrt5,-\sqrt5).
\]

Since `[-1]^*` acts trivially on Neron-Severi classes, both the diagonal and anti-diagonal restrictions give

\[
\boxed{
i_+^*L=i_-^*L=10\Theta.}
\]

Consequently

\[
L\cdot i_{+*}[B]=i_{+*}(10\Theta),
\qquad
L\cdot i_{-*}[B]=i_{-*}(10\Theta).
\]

Take two general translates of the diagonal and two general translates of the anti-diagonal, denoted

\[
S_{+,1},S_{+,2},S_{-,1},S_{-,2}.
\]

Let

\[
R=[S_{+,1}]+[S_{+,2}]+[S_{-,1}]+[S_{-,2}].
\]

Then

\[
\begin{aligned}
L\cdot R
&=2\cdot10\bigl(i_{+*}[\Theta]+i_{-*}[\Theta]\bigr)\\
&=40\bigl(\Theta\times[\mathrm{pt}]+[\mathrm{pt}]\times\Theta\bigr)\\
&=Q.
\end{aligned}
\]

Thus

\[
\boxed{L\cdot R=Q.}
\]

This is the scale-one replacement for the W2C identity `L D L_+=4Q`.

## 4. Four genus-101 curves with zero Euler correction

The class `L/2` is integral and ample, so `L` is the square of an ample line bundle and is base-point free on the abelian variety `X`. Choose a general smooth divisor

\[
Y\in|L|.
\]

Choose the four translates above generically. Two distinct translates of the same abelian subvariety are disjoint. A diagonal translate and an anti-diagonal translate meet in finitely many points; choose `Y` away from those finitely many pairwise surface intersections. Then the four curves

\[
C_{\pm,a}:=Y\cap S_{\pm,a}
\]

are smooth and pairwise disjoint.

Set

\[
C=\coprod_{a=1}^2(C_{+,a}\sqcup C_{-,a}).
\]

Then

\[
\boxed{[C]=Q.}
\]

Each surface `S_{\pm,a}` is an abelian surface isomorphic to `B`, and

\[
[C_{\pm,a}]=10\Theta
\]

on that surface. By adjunction,

\[
2g(C_{\pm,a})-2=(10\Theta)^2=200,
\]

so

\[
\boxed{g(C_{\pm,a})=101.}
\]

Furthermore

\[
\deg(\mathcal M|_{C_{\pm,a}})
=\frac12(10\Theta)^2
=100.
\]

Hence

\[
\chi(\mathcal M|_{C_{\pm,a}})
=100+1-101
=0.
\]

Since the four components are disjoint,

\[
\boxed{\chi(\mathcal M|_C)=0.}
\]

On the abelian fourfold `X`, `td(X)=1`, so for `k:C->X`

\[
\boxed{
\operatorname{ch}(k_*(\mathcal M|_C))=Q
}
\]

with no codimension-four term.

## 5. One coherent sheaf at scale one

Restriction gives a surjection

\[
F_0=i_*(\mathcal M|_Y)
\twoheadrightarrow
k_*(\mathcal M|_C).
\]

Define

\[
0\longrightarrow G_1
\longrightarrow F_0
\longrightarrow k_*(\mathcal M|_C)
\longrightarrow0.
\]

Then

\[
\operatorname{ch}(G_1)
=(\delta+Q)-Q
=\boxed{\delta=-\gamma}.
\]

Equivalently,

\[
G_1
=i_*\bigl(\mathcal M|_Y\otimes I_{C/Y}\bigr).
\]

Since `delta` belongs to the rational Markman secant space `mathcal B`,

\[
\boxed{\operatorname{ch}(G_1)\in\mathcal B.}
\]

Thus the scale-one coherent realization exists.

No denominator and no virtual difference of sheaves remains.

## 6. G_1 is simple

The divisor `Y` is smooth and integral. The curve `C` has codimension two in `Y`.

Put

\[
\mathcal F:=\mathcal M|_Y\otimes I_{C/Y}.
\]

On

\[
U:=Y\setminus C
\]

one has `F|_U ~= M|_U`, so any endomorphism of `F` restricts to multiplication by a regular function on `U`.

Because `Y` is smooth, hence normal and `S_2`, and `Y\setminus U` has codimension two,

\[
H^0(U,\mathcal O_U)=H^0(Y,\mathcal O_Y)=\mathbf C.
\]

Restriction of endomorphisms is injective because `F` is torsion free of rank one. Therefore

\[
\boxed{
\operatorname{End}_Y(\mathcal F)=\mathbf C
}
\]

and hence

\[
\boxed{
\operatorname{End}_X(G_1)=\mathbf C.
}
\]

So `G_1` is a simple coherent secant sheaf with the minimal Chern character `delta`.

This removes both the scale-four size issue and the repeated-summand issue from W2D.

## 7. The Markman non-vanishing criterion survives at scale one

The W2C calculation proved that

\[
\gamma\otimes\gamma
\]

has non-zero `BB_1` projection on all four Weil lines and non-zero `BB_0` scalar component.

Since

\[
\delta=-\gamma,
\]

we have

\[
\delta\otimes\delta=\gamma\otimes\gamma.
\]

Therefore the pair

\[
\boxed{G_1'=G_1}
\]

satisfies exactly the same cohomological genericity criterion as W2B and W2C.

## 8. Ordinary semiregularity still fails for this explicit scale-one family

The scale-one Chern character passes the raw dimension test from W2D, but the explicit sheaf above has too many first-order deformations.

Fix the four translated abelian surfaces `S_(+,a),S_(-,a)` and vary the smooth divisor

\[
Y_t\in|L|
\]

in the open subset where all four intersections remain transverse and avoid the finite pairwise surface intersections. Define

\[
C_t=Y_t\cap R
\]

and

\[
G_{1,t}
=i_{t*}\bigl(\mathcal M|_{Y_t}\otimes I_{C_t/Y_t}\bigr).
\]

This is a flat family with constant Chern character `delta`.

Its scheme-theoretic codimension-one support is exactly `Y_t`, so the support map recovers `Y_t` from `G_(1,t)`. Hence the tangent map from the open subset of `|L|` into the deformation space of `G_1` is injective.

Now

\[
h^0(X,L)=\frac{L^4}{4!}=400,
\]

so

\[
\dim|L|=399.
\]

Therefore

\[
\boxed{
e_1:=\dim\operatorname{Ext}^1_X(G_1,G_1)\ge399.}
\]

For `ch(G_1)=delta`, W2D computed

\[
\chi(G_1,G_1)=800.
\]

Since `G_1` is simple and `X` is an abelian fourfold, Serre duality gives

\[
e_0=e_4=1,
\qquad e_3=e_1,
\]

hence

\[
e_2=798+2e_1.
\]

For

\[
P_1=G_1\boxtimes G_1^\vee
\]

Kunneth therefore gives

\[
\begin{aligned}
\dim\operatorname{Ext}^2(P_1,P_1)
&=2e_2+e_1^2\\
&=1596+4e_1+e_1^2\\
&\ge1596+4\cdot399+399^2\\
&=\boxed{162393}.
\end{aligned}
\]

Orlov equivalence preserves this dimension.

The ordinary degree-two semiregularity target on the abelian eightfold has dimension only

\[
\dim HH_{-2}=8008.
\]

Thus

\[
\boxed{
162393>8008,
}
\]

and ordinary semiregularity is impossible for this explicit scale-one construction.

## 9. A sharp necessary condition for any ordinary scale-one redesign

For an arbitrary **simple** scale-one representative with `ch=delta`, W2D gives

\[
\dim\operatorname{Ext}^2(G\boxtimes G^\vee,G\boxtimes G^\vee)
=1596+4e_1+e_1^2.
\]

Ordinary semiregularity requires this to be at most `8008`. Therefore

\[
e_1^2+4e_1+1596\le8008.
\]

The positive root is approximately `78.0999`, so necessarily

\[
\boxed{
\dim\operatorname{Ext}^1_X(G,G)\le78.
}
\]

This is now the exact design constraint on any ordinary-semiregular `m=1` candidate.

The present `G_1` has at least `399` first-order deformations and therefore misses the target by a wide margin.

## 10. Correct W2E-B verdict

The scale-one coherent-sheaf existence problem closes **AGREE**:

\[
\boxed{
\exists\,G_1\in\operatorname{Coh}(X),
\qquad
G_1\text{ simple},
\qquad
\operatorname{ch}(G_1)=\delta=-\gamma\in\mathcal B.
}
\]

But ordinary semiregularity of this explicit `G_1` closes **FAIL** because its support moves in a 399-dimensional linear system.

Thus lowering the Chern-character scale was necessary but not sufficient.

The remaining ordinary route is sharply constrained:

> construct a simple scale-one secant sheaf with `ch=delta` whose first-order deformation space has dimension at most 78, in particular one whose support is infinitesimally much more rigid than the divisor-supported family above.

## 11. Relation to the Perry route

Markman's general CM construction still leaves semiregularity of the resulting derived object open. Perry's 2026 equivariant semiregularity theorem changes the relevant target: one may seek injectivity only on the appropriate invariant obstruction space rather than on the full `Ext^2` space.

The present calculation makes that alternative more attractive. Both explicit ordinary constructions found so far fail because their geometric realizations carry large deformation spaces, not because the Weil projection vanishes.

Thus the next lane is naturally one of:

1. **W2E-B2:** a rigid-support scale-one redesign with `Ext^1 <= 78`;
2. **W2E-A:** impose a finite symmetry on a secant object and use Perry's equivariant / weak semiregularity criterion.

The two approaches can be combined.

## 12. External references

- E. Markman, *Secant sheaves on abelian n-folds with real multiplication and Weil classes on abelian 2n-folds with complex multiplication*, arXiv:2509.23079. The general CM strategy constructs the secant space and leaves semiregularity open.
- A. Perry, *The semiregularity theorem for equivariant noncommutative varieties*, arXiv:2604.00511. The theorem extends semiregularity to equivariant and twisted/noncommutative settings and answers a question of Markman in that framework.

## 13. Final boundary

```text
CM5 carrier                              DONE
polarized CM realization                 DONE
Hodge census                             DONE
split generalized-Weil eightfold         DONE
Markman F-realization                    DONE
cyclic-C4 secant pair                    DONE
perfect-complex realization              DONE
coherent secant sheaf, scale 4           DONE
ordinary semiregularity, scale 4         FAIL
simple coherent secant sheaf, scale 1    DONE
ordinary semiregularity, this scale-1 G  FAIL
rigid-support scale-1 redesign            OPEN
Perry equivariant semiregularity          OPEN
```

The new exact geometric identity is

\[
\boxed{
Q=L\cdot\bigl(2[\Delta]+2[\Delta^-]\bigr)
}
\]

at the level of translated diagonal/anti-diagonal abelian-surface cycles, with each resulting curve having genus `101` and zero `M`-Euler characteristic. This removes the scale obstruction completely. The remaining obstruction is deformation-theoretic.