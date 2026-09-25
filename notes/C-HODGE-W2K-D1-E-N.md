# C-HODGE-W2K-D1-E-N: W2K closure, three-level replacement, geometry, and final trace-kernel test

**STATUS: NON-CANONICAL RESEARCH NOTE.**

**Scientific status:** candidate-T for the conditional mathematical propositions explicitly labelled below; candidate-C for the two local exact arithmetic audits.  
**Owner:** ChatGPT session HODGE-W2K-D1-E-2026-09-12/13.  
**Public basis:** `mathorn1973/twist-j` main `f10fca3806385a491b32ef40157c51bca08576ab`, Public Canon v84.  
**Public lock and research handoff:** issue #977.  
**Scope:** consolidate the W2K-D1 closure, the minimal W2K-E three-level architecture, the order-five character attacks, an explicit `m=2` source geometry, and the geometry-specific trace-kernel breaker.  

This note is a continuation aid. It does not edit `canon/`, register a claim, prove the Hodge conjecture, or promote any W2J/W2K research note. The source geometry from W2J-C and the W2K-B contraction rank are adopted NON-CANONICAL inputs. A local x86_64 audit is reproduction/bookkeeping only, never a two-architecture gate or independent confirmation.

## 1. Stable public inputs used here

The source object lane supplies a weight-one twisted perfect object `G` on the square-root gerbe over the mixed order-80 quotient, with

\[
\operatorname{ch}(G)=\bar\delta,\qquad
\operatorname{End}(G)=\mathbf C,\qquad
8\le r:=\dim\operatorname{Ext}^1(G,G)\le30.
\]

The source filtration has the three pieces

\[
B[-1],\qquad F,\qquad A[-1],
\]

with `F` the divisor core and `A,B` the two genus-two curve blocks. The cell self profiles used below are

\[
F:(1,12,12,12,1),\qquad
A,B:(1,6,10,6,1).
\]

W2K-B supplies, for every outer representative with the same Chern character, the Chern-contraction rank

\[
\operatorname{rank}(\,\lrcorner\operatorname{ch})=104.
\]

This number is a sufficient route to semiregularity when an independent argument proves `dim Ext2 <= 104`. It is not a necessary Ext2 dimension for every conceivable semiregular object.

## 2. W2K-D1: the old L-shaped outer family is closed negatively

### [candidate-T] 2.1 Exact trace-kernel map

For a triangle

\[
V[1]\xrightarrow{i}R\xrightarrow{p}U\xrightarrow{q}V[2],
\]

define

\[
\Psi:\operatorname{Ext}^3(U,V)\to\operatorname{Ext}^2(R,R),
\qquad
\beta\mapsto i[2]\beta p.
\]

Atiyah naturality and cyclicity of the derived trace move `i` around the trace and produce the factor `pi=0`, hence

\[
\operatorname{im}\Psi\subseteq\ker\sigma_R.
\]

Exact Hom sequences give the formality-free estimate

\[
\boxed{
\dim\ker\sigma_R\ge
h^3(U,V)-h^1(U,U)-h^1(V,V)-h^0(V,U).
}
\]

Under the pairwise negative-Ext vanishings used in this lane, forward Hom also injects into the forbidden negative self-Ext:

\[
\operatorname{Hom}(U,V)\hookrightarrow\operatorname{Ext}^{-1}(R,R).
\]

For this family, `Ext^{<0}(R,R)=0` is therefore equivalent to the required forward-Hom zero.

### [candidate-T] 2.2 Fixed-source Rouquier/Picard bound

For arbitrary translates and degree-zero twists of the fixed W2J-C source,

\[
\boxed{
\dim\operatorname{Hom}(G',G'')\le3,
\qquad
\operatorname{Ext}^{<0}(G',G'')=0.
}
\]

The three possible degree-zero contributions are the divisor-to-divisor term and at most one scalar on each of the two curve types. Shifted curve/divisor terms vanish by the divisor resolution and CY4 duality.

Write the ordered cross profiles

\[
M_i=(0,a_i,c_i,b_i,h_i),\qquad
c_i=10+a_i+b_i-h_i,\qquad 0\le h_i\le3,
\]

and the common self profile

\[
S=(1,r,8+2r,r,1).
\]

The corrected ordered Kunneth calculation yields

\[
\begin{aligned}
K={}&14r+(3r+8-h_2)a_1+(3r+8-h_1)a_2\\
&+(r+1)(b_1+b_2)-(r+1)(h_1+h_2),
\end{aligned}
\]

and the exact nonnegative-remainder identity

\[
\begin{aligned}
K-(8r-6)={}&(3r+8-h_2)a_1+(3r+8-h_1)a_2\\
&+(r+1)(b_1+b_2)+(r+1)(6-h_1-h_2)\ge0.
\end{aligned}
\]

Therefore

\[
\boxed{
\operatorname{Ext}^{<0}(R,R)=0
\Longrightarrow
\dim\ker\sigma_R\ge8r-6.
}
\]

Using only the source floor actually stated by W2J-C, `r>=8`, gives the safe bound

\[
\boxed{\dim\ker\sigma_R\ge58>0.}
\]

The earlier number `90` used the stronger auxiliary floor `r>=12`; it must not be quoted as a consequence of W2J-C itself.

**Disposition:** the fixed-source L-shaped translation/Picard family, including torsion characters and arbitrary degree-two arrows, fails the joint universal-gluability/semiregularity requirement. Do not reopen it by trying another character in the same architecture.

## 3. W2K-E: minimal three-level replacement

### [candidate-T] 3.1 Architecture and Maurer-Cartan compatibility

Use three nonempty levels with equal Chern character:

\[
\mathcal A,\qquad \mathcal B[1],\qquad \mathcal C[2].
\]

Their signed Chern character is `v-v+v=v`. This is the minimum number of cells for three nonempty levels, not a global minimality theorem for all successful representatives.

Successive arrows

\[
x\in\operatorname{Ext}^2(\mathcal A,\mathcal B),\qquad
y\in\operatorname{Ext}^2(\mathcal B,\mathcal C)
\]

must satisfy

\[
\boxed{y[2]x=0\in\operatorname{Ext}^4(\mathcal A,\mathcal C).}
\]

A higher dg component may provide a nullhomotopy of a zero cohomology class, but it cannot erase a nonzero Yoneda product. The pure IT2 staircase fails here: its two nonzero factorwise arrows compose to a nonzero pure tensor.

### [candidate-T] 3.2 Extreme-corner trace kernel

For the two successive triangles and the induced maps `j:C[2]->E`, `p:E->A`,

\[
\operatorname{Ext}^4(\mathcal A,\mathcal C)
\to\operatorname{Ext}^2(E,E),
\qquad
\beta\mapsto j[2]\beta p,
\]

has image in `ker sigma_E`, again because trace cyclicity produces `pj=0`.

For ordered adjacent profiles

\[
M_i=(0,a_i,c_i,b_i,h_i),\qquad c_i=10+a_i+b_i-h_i,
\]

the raw corner dimension is

\[
N=c_1c_2+a_1b_2+b_1a_2.
\]

This replaced the old L-shaped problem by a genuine rank-budget problem, but no rank-capacity estimate is treated as an attained rank.

## 4. Character attacks inside the order-five line

### [candidate-T] 4.1 Reciprocal characters

Let `alpha` generate the nontrivial order-five line-character group from the degree-five addition isogeny and take

\[
G_1=G\otimes\alpha,\qquad
G_2=G\otimes\alpha^{-1}.
\]

For

\[
a=\dim\operatorname{Ext}^1(G_\alpha,G),\qquad
b=\dim\operatorname{Ext}^1(G_{\alpha^{-1}},G),
\]

the ordered profiles are

\[
(0,a,10+a+b,b,0),\qquad
(0,b,10+a+b,a,0).
\]

The fixed-source filtration yields

\[
\boxed{a,b\ge\max(5-m,r-12-3m).}
\]

For `m<=2`, in particular `a,b>=3`. A compatible common-`theta` construction exists, but a protected corner remains. The relaxed minima are at least `154,70,6` for `m=0,1,2` respectively, so the whole reciprocal staircase fails full semiregularity.

### [candidate-T] 4.2 Nonreciprocal characters before fixing geometry

For the four nontrivial powers `alpha^k`, set

\[
d_k=\dim\operatorname{Ext}^1(G\otimes\alpha^k,G).
\]

The common formal-local curve block gives the simultaneous diameter constraint

\[
\boxed{\max_k d_k-\min_k d_k\le5+3m.}
\]

With the common-`theta` arrows and their additional forced rank losses, the abstract budget reduces to the single formal window

\[
\boxed{
m=2,\qquad r=21,\qquad
\chi\ne\psi,\quad\psi\ne\chi^{-1}.
}
\]

This was only a necessary non-exclusion condition, not a geometric construction. Same-character choices already retain at least five trace-kernel directions, and `r=20` retains at least four.

The role of this section is historical and diagnostic. Section 6 below supersedes this relaxed window for the actual geometry.

## 5. Explicit `m=2` source geometry

### [candidate-T] 5.1 Fixed quotient and explicit genus-two model

Keep the public mixed order-80 quotient. Let

\[
B=\operatorname{Jac}(y^2=x^5-1),
\]

and quotient by the fixed order-four subgroup `H2` to obtain the principally polarized surface `S=B/H2`. A Richelot calculation identifies it as

\[
\boxed{
S\simeq\operatorname{Jac}(D),\qquad
D:\ v^2=z(z+2)(z^4-5z^2+5).
}
\]

Multiplication by `phi` descends to the integral matrix

\[
\Phi=
\begin{pmatrix}
1&0&0&-1\\
0&1&1&-2\\
-2&1&0&0\\
-1&0&0&0
\end{pmatrix},
\qquad \Phi^2=\Phi+I.
\]

Let `H=<t>` be the fixed order-five subgroup given by the original vector `u=(1,3,1,0)^t`. Exact identities give

\[
\sqrt5 H=0,\qquad \varphi|_H=[3],\qquad\varphi^{-1}|_H=[2].
\]

The fixed fourfold is

\[
\bar X=(S\times S)/\Delta H.
\]

### [candidate-T] 5.2 Degree-five isogeny and common divisor

Define

\[
T(x,y)=\bigl(x-y,\ \varphi^{-1}x+\varphi y\bigr).
\]

Because `sqrt(5) H=0`, `T` kills `Delta H` and descends to a degree-five isogeny

\[
F=(F_1,F_2):\bar X\to S\times S.
\]

The exact lattice calculation gives

\[
\boxed{
F^*(\Theta\boxtimes\mathcal O+\mathcal O\boxtimes\Theta)=\bar L
}
\]

entry-by-entry in the frozen W2I basis.

A genus-two theta-coset argument, together with an exact torsion certificate on `D`, shows that the fixed subgroup `H` admits a theta translate `Gamma` such that

\[
\boxed{\Gamma\cap H=\{h,-h\}.}
\]

The only obstruction would be a distinguished Weierstrass-based order-five subgroup `H_*`; the fixed `H` is not `H_*` because `(1-j)u` is nonzero modulo five.

Define the effective ample Cartier divisor

\[
\boxed{Y=F_1^{-1}(\Gamma)+F_2^{-1}(\Gamma).}
\]

Its reducibility is deliberate and allowed at the W2J-C note scope.

### [candidate-T] 5.3 Two actual correction curves

Set

\[
C_A=q(\Gamma\times\{0\}),\qquad
C_B=q(\{0\}\times(-\Gamma)).
\]

Then

\[
\boxed{C_A\cap C_B=\{q(h,0),q(-h,0)\},\qquad m=2.}
\]

Both points are reduced. They lie outside the second component of `Y`, because `F_2` sends them to `+/-2h`, which is disjoint from `Gamma`. Thus `Y` is smooth at the two curve intersections.

In product coordinates

\[
\bar X\simeq S\times A_5,\qquad A_5=S/H,
\]

the first component and curves are simply

\[
Y_1=\Gamma\times A_5,
\]

\[
C_A=\operatorname{graph}(0),\qquad
C_B=\operatorname{graph}(-\pi_H|_\Gamma).
\]

Their two intersections are exactly the two zeros of `pi_H|_Gamma`.

The curve classes and support degrees remain the required ones:

\[
[C_A]+[C_B]=\bar Q,\qquad
\bar L\cdot C_A=\bar L\cdot C_B=5.
\]

### [candidate-T] 5.4 Line bundles and actual source gluing

Let `D_A,D_B` be the two reduced intersection divisors and choose

\[
N_A=\mathcal O_{C_A}(D_A),
\]

\[
N_B=K_{C_B}\otimes\mathcal O_{\bar X}(-Y)|_{C_B}\otimes
\mathcal O_{C_B}(-D_B).
\]

Then

\[
\deg N_A=2,\qquad \deg N_B=-5,
\]

and the root-gerbe top term cancels exactly.

After removing the common weight-one line, write

\[
F=i_*\mathcal O_Y,\qquad A=j_{A*}N_A,\qquad B=j_{B*}N_B.
\]

Restriction and the canonical section give a nonzero map `a:F->A`. Divisor duality gives

\[
\operatorname{Ext}^2(B,F)\simeq H^0(C_B,\mathcal O(D_B)),
\]

and its canonical section defines `b`. At both intersections the local Koszul calculation gives

\[
\boxed{a[2]b=0\in\operatorname{Ext}^2(B,A).}
\]

Hence, with `K=Fib(F->A)`, `b` lifts to `btilde in Ext2(B,K)` and one may define

\[
G=\operatorname{Cone}(B[-2]\xrightarrow{\tilde b}K).
\]

Restoring the common root-gerbe line gives the required cohomological Chern character and a Schur source. The lift is not asserted to be unique.

## 6. Test of the actual geometry: decisive failure of this three-level character staircase

### [candidate-T] 6.1 Geometry fixes the attaching-map rank

The graph description from Section 5 is decisive. Each graph curve can be straightened inside `S x A5`, preserving `Y1=Gamma x A5`. Thus

\[
N_{C/\bar X}\simeq K_C\oplus\mathcal O_C^{\oplus2},
\qquad
N_{C/Y_1}\simeq\mathcal O_C^{\oplus2}.
\]

The two vertical deformations inside `A5` keep the curve inside `Y1` and therefore lie in the kernel of the attaching-map deformation.

Set

\[
u_A=h^0(\mathcal O_{C_A}(D_A)),\qquad
u_B=h^0(\mathcal O_{C_B}(D_B)),\qquad
\tau=u_A+u_B,
\]

where each `u_i` is `1` or `2`.

For either forward attaching map, the exact geometric rank is

\[
\boxed{\operatorname{rank}\lambda_a=u+1.}
\]

The two curve legs hit different adjacent targets, hence the combined curve-block rank is

\[
\boxed{\ell=\tau+2.}
\]

The reverse `B` arrow is treated by the correctly shifted divisor duality

\[
\mathbb D_Y(-)=R\mathcal Hom_{\bar X}(-,\mathcal O_{\bar X}(-Y))[3].
\]

### [candidate-T] 6.2 Consequences for the actual source family

At `m=2`, the self first page has total degree-one dimension `28+tau`. Removing two scalar boundaries and at least `ell=tau+2` outgoing directions gives

\[
\boxed{r=\dim\operatorname{Ext}^1(G,G)\le24.}
\]

For every nontrivial order-five character `alpha^k`, the twisted divisor-core profile is

\[
\operatorname{Ext}^\bullet(F\otimes\alpha^k,F)=(0,5,0,5,0).
\]

The same formal-local curve rank `ell` applies to the twist. The filtration calculation gives

\[
\boxed{6\le d_k:=\dim\operatorname{Ext}^1(G\otimes\alpha^k,G)\le17}
\]

for all four nontrivial characters.

This already destroys the relaxed Section 4 window, which required some character dimensions equal to three.

### [candidate-T] 6.3 Uniform trace-kernel lower bound

Choose any two nontrivial addition-isogeny characters independently. Write the ordered profiles

\[
M_i=(0,a_i,c_i,b_i,0),\qquad c_i=10+a_i+b_i.
\]

For the three outer cells

\[
\mathcal A=G_\chi\boxtimes G^\vee,\qquad
\mathcal B=G\boxtimes G^\vee,\qquad
\mathcal C=G\boxtimes G_\psi^\vee,
\]

the conservative exact-triangle estimate, valid for arbitrary compatible adjacent arrows and higher lifts, is

\[
\boxed{
\dim\ker\sigma_E\ge
h^4(\mathcal A,\mathcal C)
-h^2(\mathcal A,\mathcal B)
-h^2(\mathcal B,\mathcal C)-6r.
}
\]

Kunneth gives

\[
h^4(\mathcal A,\mathcal C)=c_1c_2+a_1b_2+b_1a_2,
\]

\[
h^2(\mathcal A,\mathcal B)+h^2(\mathcal B,\mathcal C)
=c_1+c_2+r(a_1+a_2).
\]

Using `r<=24` and `a_i,b_i>=6`, put

\[
a_i=6+x_i,\qquad b_i=6+y_i,
\qquad x_i,y_i\ge0.
\]

The right side is exactly

\[
\begin{aligned}
K={}&512-18r+(27-r)(x_1+x_2)+27(y_1+y_2)\\
&+x_1x_2+2x_1y_2+2y_1x_2+y_1y_2.
\end{aligned}
\]

Every residual coefficient is nonnegative because `r<=24`. Therefore

\[
\boxed{
\dim\ker\sigma_E\ge512-18r\ge80>0.
}
\]

At the formerly interesting value `r=21`,

\[
\boxed{\dim\ker\sigma_E\ge134.}
\]

The relaxed endpoint `r=24`, `a_i=b_i=6` has corner dimension `556`, conservative removal capacity `476`, and excess `80`.

This proof does **not** use the earlier sixteen permanent-symbol refinement or the later common-`theta` eight-direction refinement. The conservative exact-triangle bound already fires.

**Final disposition of this geometry:** the explicit product-component `m=2` source geometry cannot yield a fully semiregular W2K-E object in the three-level addition-isogeny character staircase, for any of the four nontrivial characters, any pair of them, any compatible adjacent arrows, and any coherent higher nullhomotopies.

## 7. Scope that is closed and scope that remains open

### Closed negatively at candidate-T scope

1. **Old L architecture:** fixed W2J-C source, translation/Picard orbit, arbitrary degree-two arrows.
2. **Pure IT2 three-level staircase:** two nonzero factorwise arrows fail the composition gate.
3. **Reciprocal order-five three-level staircase:** protected trace kernel remains positive.
4. **Same-character and relaxed common-`theta` attempts:** excluded before geometry.
5. **Explicit product-component `m=2` geometry:** after using its true deformation rank, every addition-isogeny-character three-level outer object has
   \[
   \dim\ker\sigma_E\ge80.
   \]

### [O] Still open

The result is **not** a no-go for:

- Picard/Rouquier strata outside the four addition-isogeny characters when the source geometry changes;
- a different source object with the same cohomological Chern character;
- a support divisor whose curve blocks do not inherit the two vertical attaching-map deformation directions;
- a longer Postnikov filtration or a genuine monad with different signed multiplicities;
- a different invariant category or a separately justified equivariant weak-semiregularity route.

Merely moving a curve to another analogous fibration component is not automatically an escape. A new candidate must explicitly account for the vertical deformation directions rather than assume them away.

## 8. Exact audits kept with this note

Two standard-library scripts accompany this note.

### Geometry audit

Path: `notes/C-HODGE-W2K-D1-E-N-GEOMETRY-VERIFY.py`  
SHA-256 at preparation: `fb25931a4039e47e64068f5383d17bbe1948ee353952426fcb28b20689893455`.

It checks exact quotient-lattice identities, the degree-five isogeny, the full frozen polarization matrix, the Richelot sextic, finite-field Bezout torsion certificates, the C5 triple-centre classification, the `m=2` node placement, and the curve/root top-term cancellation. It does **not** compute `r`, the character profiles, or semiregularity.

Expected final lines include:

```text
C5 triple-centre classification: 10/10
Gamma cap H = {+h,-h}; F2 sends nodes to {+2h,-2h}: disjoint
m=2: deg N_A=2, deg N_B=-5, total curve/root top term=0
RESULT: exact geometric certificates PASS; r/profiles/semiregularity NOT COMPUTED
```

### Trace-kernel audit

Path: `notes/C-HODGE-W2K-D1-E-N-TRACEKERNEL-VERIFY.py`  
SHA-256 at preparation: `b333847798797253792514b01b5a538adacdfcdbff145a2fadd8685add93c105`.

It checks the obstruction-map normal-form ranks used in the proof, every relevant filtered first-page dimension, the exact polynomial identity above, and `352512` ordered dimension controls. It does not extract matrices from a concrete Mumford-coordinate derived object.

Expected scientific output is

```text
uA=1 uB=1: ell=4; r<=24; 6<=dk<=17
uA=1 uB=2: ell=5; r<=24; 6<=dk<=17
uA=2 uB=1: ell=5; r<=24; 6<=dk<=17
uA=2 uB=2: ell=6; r<=24; 6<=dk<=17
exact polynomial identity: PASS
K=512-18r+(27-r)(x1+x2)+27(y1+y2)+x1*x2+2*x1*y2+2*y1*x2+y1*y2
r<=24, xi,yi>=0: all residual coefficients nonnegative; K>=80
ordered dimension controls: 352512
relaxed minimum (K,r,a1,b1,a2,b2): (80, 24, 6, 6, 6, 6)
r=21 relaxed minimum: (134, 21, 6, 6, 6, 6)
These minima are bounds, not realized geometric dimensions.
RESULT: arithmetic PASS; conditional geometric family fails full semiregularity
Exact r, dk, full Ext2, full trace-kernel dimension and basis: NOT COMPUTED
```

Both scripts were executed locally on one x86_64 lane with exit code zero and empty stderr before this repository consolidation. This is candidate-C bookkeeping only. A future formal probe would require a fresh public preregistration and the repository's pinned two-architecture procedure.

## 9. Continuation instructions

Before continuing, refresh PUBLIC authority and read this note together with W2J-C, W2K-A/B/C and issue #977.

Do **not** spend another run tuning `Gamma`, the source lift, or the order-five character pair solely to hit `r=21`. The actual geometry already gives a positive trace kernel even at `r=21`.

The next useful candidate must change one of the structural inputs responsible for the no-go. In particular it should explain, before computation, how it avoids or absorbs the two vertical deformation directions of each curve block and how its filtration changes the protected extreme-corner map.

Freeze any such successor as a new NON-CANONICAL candidate. Do not reuse this identifier for a different source or filtration. A new geometric or categorical proposal must preserve the target Chern character, the negative-Ext condition required by Perry, and the explicit composition/nullhomotopy gate before any semiregularity claim is tested.

## 10. Review targets

The two principal mathematical review targets for the final geometry-specific result are:

1. the geometric attaching-map rank `ell=tau+2`, including the correctly shifted dual description of the reverse `B` arrow;
2. the injection of the filtration-preserving first cohomology used to obtain the lower character bound `d_k>=6`.

The finite audits do not prove these geometric lemmas. Until independent review is recorded, the present theorem-grade labels remain `candidate-T`, not public `T`.
