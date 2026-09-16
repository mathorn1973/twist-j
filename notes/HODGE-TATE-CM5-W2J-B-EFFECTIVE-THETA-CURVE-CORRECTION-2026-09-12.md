# Hodge-Tate CM5: W2J-B effective theta-curve correction

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Basis:** Public Canon v84 and the companion Hodge-Tate / Markman / Perry CM5 notes through
`HODGE-TATE-CM5-W2J-A-PRINCIPAL-INDEX2-SCHUR-BLOCKS-2026-09-11.md`.

**Date:** 2026-09-12.

This note continues **Gate W2J** on the mixed order-80 quotient

\[
\pi:X=B\times B\longrightarrow \bar X=X/H_{\rm mix}
\]

and its square-root gerbe

\[
\mathfrak X=\sqrt[2]{\bar{\mathcal L}/\bar X}.
\]

W2I-B proved that the primitive correction class `bar Q` has an exact weight-one perfect realization. W2J-A replaced the large virtual divisor certificate by six small Schur cells. The present note finds a substantially smaller geometric carrier: `bar Q` is the sum of **two actual smooth genus-two theta curves** on the quotient. Each curve supports a Schur sheaf with self-Ext dimensions `(1,6,10,6,1)`, and two suitable line bundles on the two curves give a weight-one coherent correction with Chern character exactly `bar Q` at scale one.

This closes the old scale-one **effectivity** question positively. It does **not** yet construct the final connected Schur source of Chern character `bar delta`: the line-bundle degrees which cancel the top Chern term do not arise as direct coherent quotients of the divisor core. The remaining problem is now a small dg gluing problem between one divisor core and two curve blocks.

No `canon/` or registry file is changed. No semiregularity theorem is claimed.

---

## 1. The two-primary factor subgroups

Use the same passing two-primary subgroup as W2I. In each original `B` factor its two-dimensional part is generated, in the fixed integral homology basis modulo two, by

\[
h_1=(1,0,1,0),
\qquad
h_2=(0,1,0,0).
\]

Let

\[
H_{2,A},H_{2,B}\subset B[2]
\]

be the corresponding order-four subgroups.

The principal alternating form on `B` is

\[
\Omega_1=
\begin{pmatrix}
0&1&0&0\\
-1&0&1&0\\
0&-1&0&1\\
0&0&-1&0
\end{pmatrix}.
\]

Direct calculation gives

\[
h_1^T\Omega_1h_2\equiv0\pmod2.
\]

Thus each `H_(2,*)` is maximal isotropic in the theta kernel of `2Theta`.

Consequently the quotient isogenies

\[
q_A:B\to B_A:=B/H_{2,A},
\qquad
q_B:B\to B_B:=B/H_{2,B}
\]

carry principal polarizations `Theta_A,Theta_B` satisfying

\[
\boxed{
q_A^*\Theta_A=2\Theta,
\qquad
q_B^*\Theta_B=2\Theta.
}
\]

In the quotient homology basis used by W2I, the descended alternating form of `2Theta` is exactly

\[
\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix},
\]

with Pfaffian one.

---

## 2. The descended theta divisors are smooth genus-two curves

The CM abelian surface

\[
B=\operatorname{Jac}(y^2=x^5-1)
\]

is simple. Its CM field is the quartic field `Q(zeta_5)` and has no imaginary quadratic subfield; equivalently the CM type used throughout the calibration is primitive. Simplicity is preserved under isogeny, hence both `B_A` and `B_B` are simple abelian surfaces.

A principally polarized abelian surface is decomposable precisely when it is a product of elliptic curves. Therefore the principal polarizations `Theta_A,Theta_B` are indecomposable. Their theta divisors are consequently smooth genus-two curves.

Choose translates

\[
D_A\in|\Theta_A|,
\qquad
D_B\in|\Theta_B|
\]

and pull them back to `B`. Their inverse images have class `2Theta` and are invariant under the corresponding order-four kernels.

---

## 3. Two order-20 curve orbits upstairs

Keep the mixed five-primary line of W2I, generated diagonally by

\[
(u_1,u_1),
\qquad
u_1=(1,3,1,0)\pmod5.
\]

Then

\[
H_{\rm mix}
=(H_{2,A}\times H_{2,B})\oplus\langle(u_1,u_1)\rangle,
\qquad
|H_{\rm mix}|=80.
\]

Choose generic points `a,b in B` and set

\[
C_A:=q_A^{-1}(D_A)\times\{b\},
\qquad
C_B:=\{a\}\times q_B^{-1}(D_B).
\]

The translation stabilizer of `q_A^{-1}(D_A)` inside `B` is exactly `H_(2,A)`: after quotienting by `H_(2,A)`, the theta divisor of a principal polarization has no non-zero translational stabilizer. The fixed point in the other factor excludes every non-zero translation there, and the diagonal order-five element cannot stabilize either factor curve.

Hence

\[
\boxed{
\operatorname{Stab}_{H_{\rm mix}}(C_A)=H_{2,A},
\qquad
\operatorname{Stab}_{H_{\rm mix}}(C_B)=H_{2,B}.
}
\]

Both stabilizers have order four, so both orbits have exactly

\[
\boxed{80/4=20}
\]

distinct components.

Let

\[
Z_A:=\sum_{h\in H_{\rm mix}/H_{2,A}}h(C_A),
\qquad
Z_B:=\sum_{h\in H_{\rm mix}/H_{2,B}}h(C_B).
\]

These are effective `H_mix`-invariant one-cycles.

---

## 4. Their total class is exactly Q

Let

\[
\Theta_1=p_1^*\Theta,
\qquad
\Theta_2=p_2^*\Theta.
\]

Since `Theta^2=2[pt]` on `B`,

\[
[C_A]
=(2\Theta_1)\frac{\Theta_2^2}{2}
=\Theta_1\Theta_2^2,
\]

and similarly

\[
[C_B]=\Theta_1^2\Theta_2.
\]

Therefore

\[
[Z_A]+[Z_B]
=20(\Theta_1\Theta_2^2+\Theta_1^2\Theta_2).
\]

But W2E proved

\[
Q
=40([pt]\times\Theta+\Theta\times[pt])
=20(\Theta_1^2\Theta_2+\Theta_1\Theta_2^2).
\]

Hence

\[
\boxed{[Z_A]+[Z_B]=Q.}
\]

Let

\[
\bar C_A:=\pi(C_A),
\qquad
\bar C_B:=\pi(C_B).
\]

The preimage of each image curve is its full twenty-component orbit, so

\[
\pi^*[\bar C_A]=[Z_A],
\qquad
\pi^*[\bar C_B]=[Z_B].
\]

Since `pi^* bar Q=Q`, injectivity of pullback for a finite isogeny gives

\[
\boxed{
\bar Q=[\bar C_A]+[\bar C_B].
}
\]

Thus the primitive scale-one quotient class `bar Q` is an **effective algebraic curve class**.

This closes the effectivity question left open in W2I.

---

## 5. Geometry of the two quotient curves

The map from each upstairs representative curve to its quotient image has degree four. Moreover

\[
\bar C_A\simeq D_A,
\qquad
\bar C_B\simeq D_B.
\]

Therefore

\[
\boxed{g(\bar C_A)=g(\bar C_B)=2.}
\]

Each curve lies as a principal theta divisor in an abelian surface subvariety of `bar X`. The two abelian surfaces intersect in a finite group of order five:

\[
\boxed{
|\bar B_A\cap\bar B_B|
=\frac{|H_{\rm mix}|}{|H_{2,A}||H_{2,B}|}
=5.
}
\]

By translating the theta divisors generically inside the two surfaces, the two curves can therefore be chosen disjoint.

The original scale-one support polarization restricts to the two factors with exact intersection number

\[
L\cdot C_A=L\cdot C_B=20.
\]

Since the quotient maps on the curves have degree four,

\[
\boxed{
\bar L\cdot\bar C_A
=\bar L\cdot\bar C_B
=5.
}
\]

The total degree is consequently

\[
\bar L\cdot\bar Q=10,
\]

in agreement with W2I-B.

---

## 6. Each curve carries a very small Schur block

Let

\[
j:C\hookrightarrow\bar X
\]

be either of the two smooth genus-two curves, and let `N` be any line bundle on `C`.

The curve is a theta divisor in an abelian surface subvariety `S subset bar X`. Hence

\[
N_{C/S}\simeq K_C.
\]

The normal bundle of an abelian subvariety in an abelian variety is trivial; choosing a complementary subspace in the Lie algebra gives

\[
N_{S/\bar X}|_C\simeq\mathcal O_C^{\oplus2}.
\]

Thus

\[
\boxed{
N_{C/\bar X}
\simeq K_C\oplus\mathcal O_C^{\oplus2}.
}
\]

The low-degree local-to-global Ext sequence gives

\[
\dim\operatorname{Ext}^1_{\bar X}(j_*N,j_*N)
=h^1(\mathcal O_C)+h^0(N_{C/\bar X})
=2+(2+2)
=6.
\]

The sheaf is Schur because `N` is rank one on an integral curve:

\[
\operatorname{End}(j_*N)=\mathbf C.
\]

Its self Euler characteristic is zero: the Chern character begins in codimension three, so no product contributes in degree eight. Serre duality on the abelian fourfold then gives

\[
\boxed{
\dim\operatorname{Ext}^{0,1,2,3,4}(j_*N,j_*N)
=(1,6,10,6,1).
}
\]

This is smaller than the principal-index-two cells of W2J-A, whose self-Ext dimensions were `(1,8,12,8,1)`.

---

## 7. An exact weight-one coherent correction with ch = bar Q

Let

\[
p:\mathfrak X\to\bar X
\]

be the square-root gerbe and `mathscr M` its tautological weight-one line object,

\[
\operatorname{ch}(\mathscr M)=e^{\bar L/2}.
\]

Choose line bundles

\[
N_A\in\operatorname{Pic}^{-1}(\bar C_A),
\qquad
N_B\in\operatorname{Pic}^{-2}(\bar C_B).
\]

Since both curves have genus two,

\[
\chi(N_A)=-2,
\qquad
\chi(N_B)=-3.
\]

Set

\[
\boxed{
\mathscr T_{\rm curv}
:=
\mathscr M\otimes p^*
\left(j_{A*}N_A\oplus j_{B*}N_B\right).
}
\]

For a line bundle `N` on a curve in an abelian fourfold,

\[
\operatorname{ch}(j_*N)
=[C]+\chi(N)[pt].
\]

Tensoring with `mathscr M` adds in top degree

\[
\frac12\bar L\cdot[C].
\]

Therefore the total degree-eight coefficient of `mathscr T_curv` is

\[
(-2)+(-3)
+\frac12(5+5)
=0.
\]

Using Section 4,

\[
\boxed{
\operatorname{ch}(\mathscr T_{\rm curv})
=\bar Q.
}
\]

So W2J-B replaces the six-cell correction of W2J-A by only **two actual coherent Schur curve blocks**.

The two curves may be chosen disjoint, so the two summands have no cross-Hom and their intrinsic first-order deformation dimensions add to only

\[
\boxed{6+6=12.}
\]

---

## 8. The divisor core is also already at the minimal deformation scale

For comparison, let

\[
\mathscr F_0=i_*(\mathscr M|_{\bar Y}),
\qquad [\bar Y]=\bar L,
\]

with `bar Y` a smooth integral member whenever such a member is chosen.

For a Cartier divisor the derived self-intersection splits into the two Koszul terms, so

\[
\operatorname{Ext}^1(\mathscr F_0,\mathscr F_0)
\cong
H^1(\bar Y,\mathcal O_{\bar Y})
\oplus
H^0(\bar Y,\mathcal O_{\bar Y}(\bar Y)).
\]

Kodaira vanishing on the abelian fourfold and the two divisor exact sequences give

\[
h^1(\mathcal O_{\bar Y})=4,
\]

and

\[
h^0(\mathcal O_{\bar Y}(\bar Y))
=h^0(\bar L)-1+h^1(\mathcal O_{\bar X})
=5-1+4
=8.
\]

Hence

\[
\boxed{
\dim\operatorname{Ext}^1(\mathscr F_0,\mathscr F_0)=12.
}
\]

Together with simplicity and the known self Euler characteristic, this gives

\[
\boxed{
\dim\operatorname{Ext}^{0,1,2,3,4}(\mathscr F_0,\mathscr F_0)
=(1,12,12,12,1).
}
\]

Thus both the divisor core and the new geometric correction are individually already in the small-deformation regime required by W2H-B.

---

## 9. The remaining gluing obstruction is now precise

The correction above has the exact Chern character but it is not yet the final source object.

The negative degrees chosen for `N_A,N_B` are load-bearing: they make

\[
\chi(N_A)+\chi(N_B)=-5
\]

and cancel the root-gerbe top term. They also mean that these line bundles are not generated by a non-zero map from the trivial line bundle on their curves. Consequently `mathscr T_curv` is **not** obtained as the direct coherent quotient of `mathscr F_0` used in the original W2E elementary modification.

So the result of this note is not a hidden claim that the final Schur source is already constructed. Rather, it changes the remaining problem from

```text
large virtual divisor correction + unknown block deformation theory
```

to

```text
one divisor core with r = 12
+ two explicit genus-2 Schur curve blocks with r = 6 each
+ one finite dg gluing problem.
```

This is a much smaller categorical problem.

---

## 10. Next gate: W2J-C

The next exact calculation should use

\[
\mathscr F_0,
\qquad
\mathscr T_A:=\mathscr M\otimes j_{A*}N_A,
\qquad
\mathscr T_B:=\mathscr M\otimes j_{B*}N_B,
\]

with

\[
\operatorname{ch}(\mathscr T_A)+
\operatorname{ch}(\mathscr T_B)=\bar Q.
\]

The target is a connected twisted complex of K-class

\[
[\mathscr F_0]-[\mathscr T_A]-[\mathscr T_B]
\]

which is Schur and satisfies

\[
\dim\operatorname{Ext}^1\le30.
\]

The geometric alternatives are now sharply separated:

1. find a support divisor containing a correction curve configuration whose structure sheaf already has the required total Euler correction; or
2. compute the finite cross-Ext algebra of the three small blocks and connect them by a genuine Postnikov/twisted-complex datum.

No further lattice search is needed for the correction class itself.

---

## 11. Verdict

W2J-B closes two previously open issues:

\[
\boxed{\bar Q\text{ is an effective integral curve class},}
\]

and

\[
\boxed{
\exists\,\mathscr T_{\rm curv}\in\operatorname{Coh}(\mathfrak X)_{\rm wt=1}
\text{ with }\operatorname{ch}(\mathscr T_{\rm curv})=\bar Q.
}
\]

Moreover the correction can be carried by only two Schur blocks, each with first-order deformation dimension six. The sole remaining W2J obstruction is now the connected Schur gluing to the divisor core and its exact `Ext^1` count.