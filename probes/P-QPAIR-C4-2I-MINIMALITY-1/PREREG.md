# P-QPAIR-C4-2I-MINIMALITY-1 preregistration

```text
STATUS:       ZERO-RUN PIN CANDIDATE
ISSUE:        https://github.com/mathorn1973/twist-j/issues/410
BRANCH:       probe/P-QPAIR-C4-2I-MINIMALITY-1
PATH:         probes/P-QPAIR-C4-2I-MINIMALITY-1/
BASE:         8359889ebac9ef85e05d4abe4d676c731b880167
PUBLIC CANON: canon-v50, content b68c60c57cfd0b1e655b6fc4d5496a333a249fdf
OWNER:        A. M. Thorn / delegated session twoi_minimality
LAYER:        L1 exact algebraic carrier theorem
MODE:         result-exposed, proof-first; verifier is an exact finite audit
FORMAL RUNS:  NONE
STATIC CHECK: syntax-only py_compile PASS before pin
```

This file freezes the carrier, actions, admissible class, seven proposed public
rows, complete written proofs, exact audit gates, falsifiers, and scope
firewalls before the accepted verifier is executed.  Syntax-only compilation
is permitted before the immutable pin.  Importing or executing `verify.py`,
creating `EXPECTED.txt`, or treating any local output as a formal result is
forbidden at this stage.

## 1. Public inputs and carrier boundary

Let

\[
K=\mathbf Q(\zeta),\qquad
\zeta^4+\zeta^3+\zeta^2+\zeta+1=0,
\qquad {\cal O}_K=\mathbf Z[\zeta],
\]

and let `c` be CM conjugation,

\[
c(\zeta)=\zeta^{-1}=\zeta^4.
\]

The carrier is the independent rank-two spinor lattice

\[
V_{\rm spin}={\cal O}_K^2.
\]

Its two coordinates are independent.  In particular it is not a diagonal
two-place image \(x\mapsto(x,a(x))\) of one field element under any field
automorphism `a`: the vector \((1,0)\) belongs to \(V_{\rm spin}\), while no
such diagonal image contains it.  Equivalently, the ambient rational
dimensions are

\[
\dim_{\mathbf Q}K^2=8,\qquad \dim_{\mathbf Q}K=4.
\]

This carrier is also not the rational effective carrier
\(V_{\mathrm{eff}}\subset\mathbf Q^4\) of `DEF-QDD-QPAIR`.  No map between
those carriers is defined here.

The common scalar action is

\[
u(z_1,z_2)=(uz_1,uz_2).
\]

Freeze the two typed quadratic slots

\[
H(v)=v\,c(v)^T,\qquad S(v)=vv^T,
\qquad Q(v)=(H(v),S(v)),
\]

and the rational-linear order-four state action

\[
\Phi(z_1,z_2)=(z_2,c(z_1)).
\]

Thus

\[
\Phi^2(z_1,z_2)=(c(z_1),c(z_2)),
\qquad \Phi^4=1.
\]

For the marked binary-icosahedral action use exactly the public
`COLOR-INTEGRAL-LIFT` matrices

\[
S_0=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
T_0=\begin{pmatrix}\zeta&1\\0&\zeta^{-1}\end{pmatrix},
\qquad G=\langle S_0,T_0\rangle.
\]

The required public inputs are:

- `COLOR-CORE-2I [T]`: the order-120 perfect core, its center
  \(\{\pm I\}\), and the identification \(2I=SL_2(\mathbf F_5)\);
- `COLOR-GOLDEN-TABLE [T]`: the exact character rows
  `2a`, `2b`, `3a`, and `3b`, their class sizes, and orthogonality;
- `COLOR-INTEGRAL-LIFT [T]`: the displayed marked matrices and their exact
  120-element closure;
- `DEF-ACTION-LAYERS`: the L1-only scope boundary.

`CENTRAL-LIFT-PHASE [T]` is a cross-reference for the already registered
Hermitian/symmetric scalar-phase distinction only.  It is not a premise for
the mixed action `Phi`, does not define this common carrier, and supplies no
decoder conclusion.

## 2. Frozen admissible class

Use the principal complex embedding only to write real coordinate functions.
The functions themselves are formal homogeneous real quadratic polynomials on
the underlying four-dimensional real vector space of \(K^2\); they are then
restricted to \({\cal O}_K^2\).  No quotient by pointwise coincidence on a
finite domain is allowed.

Write \({\cal H}\) for the real span of the four coordinate functions of the
fixed Hermitian slot and \({\cal S}\) for the realification of the three
complex coordinate functions of the symmetric slot.  The admissible class
`A_rel` consists exactly of real linear subspaces `E` of homogeneous quadratic
coordinate polynomials such that:

1. \({\cal H}\subseteq E\), with the original Hermitian coordinates retained
   as a linearly readable typed slot;
2. `E` is stable under pullback by every marked \(\rho(g)\), \(g\in G\);
3. `E` is stable under pullback by \(\Phi\).

No quotient that destroys the linear readout of the fixed `H` slot belongs to
`A_rel`.  No nonlinear action on an image, arbitrary set reconstruction,
decoder factorization, or information-theoretic minimality belongs to
`A_rel`.  No normalization or semidirect-product relation between the two
pullback families is assumed.

## 3. Frozen row 1: integer Hermitian non-descent

### QPAIR-HERM-INTEGER-NONDESCENT [T]

For

\[
v=(1,1),\qquad v'=\zeta v,
\]

one has

\[
H(v')=\zeta c(\zeta)H(v)=H(v).
\]

On the other hand,

\[
\Phi(v)=(1,1),\qquad
\Phi(v')=(\zeta,\zeta^{-1}),
\]

and therefore

\[
H(\Phi v)_{12}=1,qquad
H(\Phi v')_{12}=\zeta^2\ne1.
\]

If a set map \(D_H:\operatorname{im}H\to\operatorname{im}H\) satisfied

\[
D_H(H(x))=H(\Phi x)
\]

on \({\cal O}_K^2\), the equal inputs \(H(v)=H(v')\) would have unequal
outputs.  Hence no such total descent exists.  This is an integral witness;
no phase-saturated continuum is used.

The complete field-fiber statement is also exact.  For nonzero \(v,w\in K^2\),
equality \(H(v)=H(w)\) gives equality of their rank-one column spaces, so
\(w=uv\) for one \(u\in K^\times\).  Substitution gives

\[
u c(u)=1.
\]

Conversely every such `u` preserves `H`.  Thus the nonzero field fiber is

\[
K^1v,\qquad K^1=\{u\in K^\times:u c(u)=1\}.
\]

For the lattice nuance define the nonzero content ideal

\[
\operatorname{cont}(v)=z_1{\cal O}_K+z_2{\cal O}_K.
\]

If `v` and `w=uv` have the same nonzero content, then

\[
(u)\operatorname{cont}(v)=\operatorname{cont}(v),
\]

so `u` is a unit.  The unit group is

\[
{\cal O}_K^\times=\mu_{10}\times\langle\varphi\rangle,
\qquad \varphi=-(\zeta^2+\zeta^3)>1.
\]

For completeness, the decomposition follows as follows.  For a unit `u`, the
quotient \(u/c(u)\) is an algebraic integer whose conjugates all have modulus
one and hence is a root of unity.  Reduction modulo \(1-\zeta\) shows it is in
\(\mu_5\), not in \(\mu_{10}\setminus\mu_5\).  Since squaring permutes
\(\mu_5\), multiplication by a suitable root of unity makes `u` fixed by
`c`.  The fixed real ring is \(\mathbf Z[\varphi]\).  Its unit calculation is
short and is included here.  For a real unit `r`, change its sign and multiply
by one power \(\varphi^{-n}\) so that its principal value lies in
\(1\le r<\varphi\).  Its other real conjugate is
\(r'=N(r)/r\), where \(N(r)=\pm1\), and the trace \(r+r'\) is an integer.  If
\(N(r)=1\), then

\[
2\le r+r^{-1}<\varphi+\varphi^{-1}=\sqrt5<3,
\]

so the trace is `2` and `r=1`.  If \(N(r)=-1\), then

\[
0\le r-r^{-1}<\varphi-\varphi^{-1}=1,
\]

so the trace would be `0`; the resulting polynomial \(X^2-1\) has rational
roots and cannot be the degree-two minimal polynomial of such an `r` with
opposite conjugate.  Hence this case is empty.  Undoing the sign and power
gives

\[
\mathbf Z[\varphi]^\times=\{\pm\varphi^n:n\in\mathbf Z\}.
\]

The sign is already in \(\mu_{10}\).  Consequently

\[
u c(u)=1\quad\hbox{for a unit }u
\quad\Longleftrightarrow\quad u\in\mu_{10}.
\]

Every fixed nonzero content layer therefore has exactly the
\(\mu_{10}\)-orbit as its Hermitian fiber.

The fixed-content qualification cannot be removed.  Put

\[
a=2+\zeta,qquad v=(c(a),0),\qquad w=(a,0).
\]

Then `v,w` are integral and

\[
H(v)=H(w)=\begin{pmatrix}a c(a)&0\\0&0\end{pmatrix}.
\]

But \(a\ne\epsilon\zeta^k c(a)\) for every
\(\epsilon\in\{\pm1\}\) and \(k=0,\ldots,4\), as direct comparison in the
basis \(1,\zeta,\zeta^2,\zeta^3\) shows.  Hence \(a/c(a)\) is not a unit and
the two content ideals differ.  The full lattice can therefore have wider
Hermitian fibers than a fixed-content layer.

## 4. Frozen row 2: transpose-fiber set redundancy

### QPAIR-TRANSPOSE-FIBER-REDUNDANCY [T]

For \(v,w\in K^2\),

\[
S(v)=S(w)\quad\Longleftrightarrow\quad w=\pm v.
\]

If one vector is zero the assertion is immediate.  Otherwise equality of the
rank-one symmetric matrices gives equality of their column spaces, so
\(w=uv\) for some \(u\in K^\times\).  Substitution gives \(u^2=1\), hence
\(u=\pm1\) in characteristic zero.  Conversely both signs plainly preserve
`S`.

An independent polynomial certificate for the collinearity step is useful
for the verifier.  With \(v=(x,y)\), \(w=(p,q)\), set

\[
f_1=x^2-p^2,\qquad f_2=xy-pq,\qquad f_3=y^2-q^2.
\]

Then

\[
(xq-yp)^2=q^2f_1-2pqf_2+p^2f_3.
\]

Thus equality of the symmetric matrices forces collinearity over a field.

Since \(H(-v)=H(v)\), the Hermitian slot is constant on every `S` fiber.
There is therefore one and only one set map

\[
F:\operatorname{im}S\longrightarrow\operatorname{im}H,
\qquad F(S(v))=H(v),
\]

and projection on the second component is a bijection

\[
\operatorname{im}Q\overset{\sim}{\longrightarrow}\operatorname{im}S.
\]

This is only a theorem in the category of sets.  It does not produce a
polynomial, rational, linear, typed-natural, or admissible decoder factor map.
It proves that no information-theoretic defense of two slots is available.

## 5. Frozen row 3: exact typed mixed-C4 closure

### QPAIR-TYPED-MIXED-C4-CLOSURE [T]

Write

\[
H=\begin{pmatrix}h_{11}&h_{12}\\h_{21}&h_{22}\end{pmatrix},
\qquad
S=\begin{pmatrix}s_{11}&s_{12}\\s_{12}&s_{22}\end{pmatrix},
\]

where \(h_{21}=c(h_{12})\).  Direct substitution of
\(\Phi(z_1,z_2)=(z_2,c(z_1))\) gives

\[
H'=\begin{pmatrix}
h_{22}&s_{12}\\c(s_{12})&h_{11}
\end{pmatrix},
\qquad
S'=\begin{pmatrix}
s_{22}&h_{21}\\h_{21}&c(s_{11})
\end{pmatrix}.
\]

Define \({\cal T}_Q(H,S)=(H',S')\).  It is rational-linear on the
underlying rational typed target, preserves the Hermitian and symmetric type
conditions, and satisfies

\[
{\cal T}_Q Q(v)=Q(\Phi v),
\qquad {\cal T}_Q^4=1.
\]

The off-diagonal coordinates make the four-cycle explicit:

\[
h_{12}\longmapsto s_{12}\longmapsto c(h_{12})
\longmapsto c(s_{12})\longmapsto h_{12}.
\]

No minimality follows from `Phi` alone.  Indeed the six-dimensional real
space

\[
{\cal H}+\operatorname{span}_{\mathbf R}\{\Re s_{12},\Im s_{12}\}
\]

is already `Phi`-stable and does not contain the diagonal symmetric
coordinates.  The marked `2I` action is the additional input that forces the
rest of the symmetric slot.

## 6. Frozen row 4: the marked symmetric-square module

### QPAIR-SYM2-2I-IRREDUCIBLE [T]

The reduction of `T_0` modulo \(1-\zeta\) is the public class representative

\[
\begin{pmatrix}1&1\\0&1\end{pmatrix}
\]

of class `5a`, and

\[
\operatorname{tr}(T_0)=\zeta+\zeta^{-1}=\varphi-1.
\]

Thus the marked spinor is the public character row `2a`.  Since every marked
matrix has determinant one, the symmetric-square character is

\[
\chi_{\operatorname{Sym}^2\rho}(g)=\chi_\rho(g)^2-1.
\]

On the public class order

\[
(1a,2a,4a,3a,6a,5a,5b,10a,10b)
\]

this gives

\[
(3,3,-1,0,0,1-\varphi,\varphi,1-\varphi,\varphi),
\]

which is exactly row `3a` of `COLOR-GOLDEN-TABLE`.  With class sizes

\[
(1,1,30,20,20,12,12,12,12)
\]

and \((1-\varphi)^2+\varphi^2=3\), its exact norm is

\[
\frac{9+9+30+24((1-\varphi)^2+\varphi^2)}{120}=1.
\]

Hence \(\operatorname{Sym}^2(2a)=3a\) is absolutely irreducible.  The
central element \(-I\) acts as `+I` on the symmetric square, so the
three-dimensional representation factors through
\(2I/\{\pm I\}=A_5\).  Applying the Galois automorphism
\(\zeta\mapsto\zeta^2\) exchanges the golden rows and gives

\[
\operatorname{Sym}^2(2b)=3b.
\]

The particular coordinate required by the closure theorem has a direct orbit
certificate independent of character orthogonality.  Let
\(s(x,y)=xy\) and let the action on quadratic coordinate functions be

\[
(g\cdot q)(v)=q(g^{-1}v).
\]

Then

\[
T_0^{-1}(x,y)=(\zeta^{-1}x-y,\zeta y),
\]

so

\[
T_0\cdot s=s-\zeta y^2.
\]

Thus the orbit span contains \(y^2\).  Since

\[
S_0^{-1}(x,y)=(y,-x),
\]

it also contains \(x^2\).  Therefore

\[
\operatorname{span}_K(G\cdot s)
=\operatorname{span}_K\{x^2,xy,y^2\}
=\operatorname{Sym}^2(V^*).
\]

Orbit cyclicity is recorded here as the concrete closure certificate; it is
not used as a logically equivalent substitute for the character proof of
irreducibility.

## 7. Frozen row 5: relative ten-dimensional minimality

### QPAIR-MINIMAL-2I-CLOSURE-OF-HERM-UNDER-MIXED-C4 [T]

Under the principal embedding write

\[
z_1=a+ib,\qquad z_2=c+id.
\]

The four real Hermitian coordinate functions are

\[
a^2+b^2,\quad c^2+d^2,\quad ac+bd,\quad bc-ad,
\]

and the six real symmetric coordinate functions are

\[
a^2-b^2,\quad 2ab,\quad ac-bd,\quad ad+bc,
\quad c^2-d^2,\quad 2cd.
\]

They recover all ten real quadratic monomials:

\[
\begin{aligned}
a^2&=(H_{11}+\Re S_{11})/2,&
b^2&=(H_{11}-\Re S_{11})/2,&
ab&=\Im S_{11}/2,\\
c^2&=(H_{22}+\Re S_{22})/2,&
d^2&=(H_{22}-\Re S_{22})/2,&
cd&=\Im S_{22}/2,\\
ac&=(\Re H_{12}+\Re S_{12})/2,&
bd&=(\Re H_{12}-\Re S_{12})/2,\\
bc&=(\Im H_{12}+\Im S_{12})/2,&
ad&=(\Im S_{12}-\Im H_{12})/2.
\end{aligned}
\]

Consequently

\[
\dim_{\mathbf R}{\cal H}=4,qquad
\dim_{\mathbf R}{\cal S}=6,qquad
{\cal H}\cap{\cal S}=0,
\]

and the absolute determinant of the displayed change of quadratic basis is
`64`.  Thus

\[
{\cal H}\oplus{\cal S}
=\operatorname{Quad}_{\mathbf R}((\mathbf C^2)_{\mathbf R}),
\qquad \dim_{\mathbf R}=10.
\]

Now let `E` belong to the frozen admissible class `A_rel`.  Because it contains
the fixed Hermitian slot and is `Phi`-stable,

\[
\Phi^*H_{12}=z_1z_2=s
\]

puts both real coordinates of `s` in `E`.  Stability under the marked `2I`
and the orbit calculation of the preceding section then put the full
six-dimensional realification of \(\operatorname{Sym}^2(V^*)\) in `E`.
Explicitly, `E` contains both real coordinates of every orbit vector; a
complex coefficient multiplying a quadratic coordinate acts on its real and
imaginary parts by a real two-by-two matrix.  Hence every complex linear
combination in the three-dimensional orbit span contributes both of its real
coordinates to `E`.
Hence

\[
{\cal H}\oplus{\cal S}\subseteq E.
\]

The typed formula of Section 5 proves that
\({\cal H}\oplus{\cal S}\) itself is stable under `Phi`; ordinary congruence
proves stability under every marked `2I` matrix.  It is therefore the least
member of `A_rel`.

This is relative minimality of a fixed linearly readable `H` slot.  It is not
minimality by number of displayed slots, target presentation, arbitrary set
information, or all possible equivariant quadratic carriers.

## 8. Frozen row 6: 2I alone does not force the pair

### QPAIR-2I-ONLY-PAIR-FORCING [F]

The proposition that `2I`-equivariance by itself forces two slots is false.
The single symmetric carrier is already equivariant:

\[
S(gv)=gS(v)g^T.
\]

The single symmetric carrier also has an exact adjoint presentation.  Put

\[
\varepsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad \Theta(Y)=Y\varepsilon^{-1}.
\]

For every \(g\in SL_2\), \(g^T\varepsilon g=\varepsilon\), and hence

\[
\Theta(gYg^T)=g\Theta(Y)g^{-1}.
\]

The map `Theta` is an isomorphism from symmetric \(2\times2\) matrices to
\(\mathfrak{sl}_2\).  This is an additional certificate for the one-slot
counterexample.  It does **not** identify the standard trace-zero Hermitian
slice with an invariant marked module: in the displayed nonunitary marked
basis that standard slice need not be invariant.  No invariant graph or
quotient involving that slice is claimed.

Scalar \(\mu_5\) typing or the bidegrees `(1,1)`, `(2,0)`, and `(0,2)` can
distinguish Hermitian and symmetric coordinates in a richer typed carrier,
but that is extra structure beyond `2I` alone.

## 9. Frozen row 7: the mixed C4 does not normalize 2I

### QPAIR-MIXED-C4-NORMALIZES-2I [F]

The inverse state action is

\[
\Phi^{-1}(z_1,z_2)=(c(z_2),z_1).
\]

A direct calculation with the marked generator gives

\[
\Phi T_0\Phi^{-1}(z_1,z_2)
=\bigl(\zeta^{-1}z_1,\ \zeta^{-1}z_2+c(z_1)\bigr).
\]

The second component contains `c(z_1)`, so this map is not complex-linear or
`K`-linear and cannot belong to the marked matrix group `G`.  Therefore `Phi`
does not normalize the marked `2I`.

The positive result is only simultaneous stability of a coordinate space
under two pullback families.  It is not an action of
\(2I\rtimes C_4\), \(2I\times C_4\), or any asserted common finite group.
It is also not `COLOR-CM-2I-SEMILINEAR-PAIR`: that registered theorem uses the
different carrier \(K^2\oplus K^2\), the branch pair
\(\rho\oplus\rho^\tau\), and an order-eight semilinear structure after an
order-four obstruction.

## 10. Exact verifier audit

The verifier is an audit of the written proofs, not their logical source.  It
uses only Python's standard library, `int`, and `fractions.Fraction`.  It uses
no floating point, random choices, timestamps, external files, network, or
machine-dependent iteration order.

It will print exactly one deterministic line for each of the following gates
and a final count:

```text
01 CARRIER_INDEPENDENT_K2
02 CYCLOTOMIC_AND_CONJUGATION
03 HERM_INTEGER_NONDESCENT
04 HERM_MU10_UNIT_SUBGROUP
05 HERM_FULL_LATTICE_WIDER_FIBER
06 TRANSPOSE_FIBER_CERTIFICATE
07 SET_REDUNDANCY_SIGN_INVARIANCE
08 MIXED_C4_STATE_ORDER
09 TYPED_MIXED_C4_FORMULAS
10 TYPED_MIXED_C4_ORDER
11 PHI_ONLY_CLOSURE_DIM 6
12 MARKED_2I_ORDER 120
13 MARKED_2I_CENTER 2
14 MARKED_SPIN_ROW 2a
15 SYM2_ROW 3a
16 SYM2_CHARACTER_NORM 1
17 SYM2_FS_INDICATOR 1
18 SYM2_ORBIT_RANK 3
19 H_COORD_RANK 4
20 SYM_COORD_RANK 6
21 QPAIR_COORD_RANK 10
22 QPAIR_COORD_ABS_DET 64
23 RELATIVE_CLOSURE_CERTIFICATE
24 ADJOINT_INTERTWINER
25 S_ONLY_2I_EQUIVARIANT
26 MIXED_C4_NORMALIZES_2I FALSE
RESULT 26/26 ALL PASS
```

Any failed gate prints `FAIL`, the final line reports the exact failed count,
and the process exits nonzero.  Before the zero-run pin only

```text
python3 -m py_compile probes/P-QPAIR-C4-2I-MINIMALITY-1/verify.py
```

is permitted.  That command checks syntax and does not execute the verifier's
`main` function.

## 11. Frozen falsifiers

All thresholds are exact equalities.  There is no numerical tolerance.

1. `F-QPAIR-1` fires if the carrier is not the independent lattice
   \({\cal O}_K^2\), if the displayed integral witness fails, if the field
   fiber is not `K^1 v`, if a fixed-content fiber differs from the
   \(\mu_{10}\)-orbit, or if the explicit wider full-lattice witness fails.
2. `F-QPAIR-2` fires if `S` has a fiber other than `+-v`, if `H` is not
   constant on those fibers, or if
   \(\operatorname{im}Q\to\operatorname{im}S\) is not bijective.
3. `F-QPAIR-3` fires if either displayed typed formula fails, if
   \({\cal T}_Q^4\ne1\), if \({\cal T}_Q Q\ne Q\Phi\), or if `Phi` alone
   already forces the full ten-dimensional space.
4. `F-QPAIR-4` fires if the marked group, class orientation, character
   identity, norm-one test, central factor, Galois companion, or rank-three
   orbit certificate fails.
5. `F-QPAIR-5` fires if the coordinate ranks are not `4`, `6`, and `10`, if
   the absolute determinant is not `64`, if the seed identity fails, or if a
   proper member of `A_rel` containing the fixed `H` slot exists.
6. `F-QPAIR-6` fires against the negative row if the displayed one-slot
   carrier is not `2I`-equivariant or if the explicit adjoint intertwiner
   fails.  A changed admissible class is outside scope, not a rescue of the
   false universal proposition.
7. `F-QPAIR-7` fires against the negative row if the displayed conjugate is
   complex-linear and belongs to the marked `2I`.  A different mixed action
   is outside scope.

A source-pin mismatch, verifier-byte mismatch, unexpected stderr, changed
stdout, nonzero exit without an exact mathematical negation, architecture
disagreement, or post-pin verifier edit is an integrity `STOP`, not a
scientific falsifier.

## 12. Public dependency placement and status firewall

The proposed future dependency edges are:

```text
QPAIR-SYM2-2I-IRREDUCIBLE
    REQUIRES COLOR-CORE-2I
    REQUIRES COLOR-GOLDEN-TABLE
    REQUIRES COLOR-INTEGRAL-LIFT
    REQUIRES DEF-ACTION-LAYERS

QPAIR-MINIMAL-2I-CLOSURE-OF-HERM-UNDER-MIXED-C4
    REQUIRES QPAIR-SYM2-2I-IRREDUCIBLE
    REQUIRES DEF-QPAIR-SPIN-CARRIER
    REQUIRES DEF-QPAIR-HERM-SLOT
    REQUIRES DEF-QPAIR-SYM-SLOT
    REQUIRES DEF-QPAIR-MIXED-C4
    REQUIRES DEF-QPAIR-ADMISSIBLE-LINEAR-CLASS
    REQUIRES DEF-ACTION-LAYERS
```

The remaining rows use the same definitions and evidence bundle.  Definitions
are normative items, not registry claims.

The probe creates no dependency edge to `DEF-QDD-QPAIR` or
`QUADRATIC-DECODER-DATA`.  In particular it creates:

- no ambient bridge to rational \(V_{\mathrm{eff}}\);
- no claim that the public rational diagonal slots are informationally
  independent;
- no coefficient, Gram, effect, Born-pairing, MatterData, or decoder write
  map;
- no L5 stream, L6 measure, physical `U(1)`, apparatus, sampling, or
  uniqueness claim;
- no movement of `QUADRATIC-DECODER-DATA [O/STOP]`;
- no movement of `COLOR-LADDER-DICTIONARY [D]` or
  `COLOR-MEASURE-SELECTION [O/STOP]`;
- no use of the distinct `COLOR-CM-2I-SEMILINEAR-PAIR` as if it were the
  Hermitian/symmetric pair defined here.

The five positive rows have a theorem ceiling `T` because the proofs above
are complete and the finite verifier is only their audit.  The two universal
propositions in rows 6 and 7 have ceiling `F` because the displayed exact
counterexamples decide them.  Any physical reading of the pair is at most a
separate `D` row and is not part of this probe.

## 13. Formal sequence

```text
[x] public authority and collision readback
[x] issue #410 claim lock
[x] branch from the exact frozen base
[x] complete proof and accepted-verifier candidate authored
[x] syntax-only compile
[ ] immutable zero-run commit and push
[ ] remote byte and SHA-256 readback
[ ] first formal verifier execution
[ ] EXPECTED.txt, RUN.md, and RESULT.md
[ ] one-probe pull request
[ ] x86_64, aarch64, and aggregate required check
```

No later step is authorized by this preregistration itself.
