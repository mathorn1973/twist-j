# C-J-PLENUM-BORN-CHAIN-1-N (NON-CANONICAL)

Status: **DRAFT / NON-CANONICAL / NO VERIFIER / NO FORMAL RUN / NO STATUS
CHANGE / CANON UNCHANGED.**

Date: **2026-09-04.**

This note records a corrected proposal for the chain from the plenum step to a
possible Born reading.  It is not a Canon patch, claim registration, physical
result, apparatus definition, preregistration, or authorization to execute a
probe.  Every theorem below remains an unregistered candidate even if a
separate proof-first probe is later completed; only a sealed Canon fold can
register status.  Every physical row remains hypothetical and stopped at its
named missing gate.

## 0. Authority and scope

```text
authority:       mathorn1973/twist-j main
base main:       36293614bbf4c961c4a027155293352a8abad55e
cutover:         2026-08-21
Canon:           Public Canon v75
state:           ACTIVE
tag:             canon-v75
tag target / activation commit:
                 c4f00e1d9c89f503d913224dc3c09dc760dcec9d
content commit:  e32e85ed7297d4320df5b345e4488d78323d550c
Canon SHA-256:   44130160a3ce29bfcdc757e255d2d1c25a010b22911edfe66cf6b132be081fbe
Canon bytes:     399513
earned layer:    L1 candidate algebra only
target notes:    future L5/L6 annotations are unearned
formal runs:     NONE
public status:   NONE
```

The adjacent results merged by PRs #798 and #802 (claim-lock issues #797 and
#801) remain publicly unregistered candidate-T/L1 with Canon unchanged.  They,
and the registered rows `AFFINE-QUADRATIC-FORM-UNIQUENESS`,
`QDD-INSTRUMENT-NONSELECTION`, and
`QDD-J-AFFINE-APPARATUS-NONSELECTION`, are inputs or novelty boundaries, not
claims reclaimed here.  The unmerged remote branch
`origin/notes/c-qdd-instrument-dilation-1-n` is recorded in the public branch
ledger as `DIVERGENT` and contains unique material.  It supplies no authority,
but a future dilation probe must treat it as a collision and novelty input;
this note neither imports nor disposes of it.

All probe and claim names below are provisional and unreserved.  A completed
probe can at most support a publicly unregistered candidate result.  Only a
later separate sealed Canon fold can register a status, dependency, or gate.

## 1. Frozen algebraic convention

Let

\[
R_{\mathbb Z}=\mathbb Z[C_5]=\mathbb Z[g]/(g^5-1),\qquad
N=1+g+g^2+g^3+g^4,
\]

with column-vector convention

\[
g e_k=e_{k+1\bmod 5}.
\]

Write

\[
\varepsilon\!\left(\sum_kc_kg^k\right)=\sum_kc_k,
\qquad V_{\mathbb Z}=\ker\varepsilon,
\qquad V_{\mathbb R}=V_{\mathbb Z}\otimes\mathbb R.
\]

The Euclidean form is \(\langle c,d\rangle=\sum_kc_kd_k\), and
\(g^*=g^{-1}\).  On the full real register,

\[
R_{\mathbb R}=\mathbb RN\oplus V_{\mathbb R},\qquad
P_0=\frac N5,\qquad P_V=I-P_0,
\]

where a group-ring element denotes its circulant multiplication operator and
the second occurrence of \(N\) in \(P_0\) denotes the all-ones operator.

Freeze

\[
J=1+g^2,
\qquad
\Gamma=g+g^4-g^2-g^3,
\]

\[
A=g\Gamma=1+g^2-g^3-g^4,
\qquad
H=\frac{\Gamma}{\sqrt5},
\qquad
U_5=gH,
\qquad
B=\frac{5-\Gamma}{2\sqrt5}.
\]

The Galois multiplier is fixed as

\[
S e_k=e_{3k\bmod5},
\qquad SgS^{-1}=g^3.
\]

The multiplier \(2\) is the inverse convention and must not be substituted
silently.

For a plenum register \(c\), define its centered relational state by

\[
D(c)=5c-\varepsilon(c)N.
\]

Then the proposed exact bookkeeping is

\[
\varepsilon(Jc)=2\varepsilon(c),\qquad D(Jc)=JD(c),
\]

\[
\ker D=\mathbb ZN,
\qquad
\operatorname{im}D=
\{d\in V_{\mathbb Z}:d_i\equiv d_j\pmod5\}.
\]

Thus supported centered plenum states form a proper full-rank sublattice of
\(V_{\mathbb Z}\), of index \(5^3=125\), not all of
\(V_{\mathbb Z}\).  This distinction is load-bearing whenever a witness is
said to be a prepared plenum state.

The proposed determinant checks are

\[
\det(J|R_{\mathbb Z})=2,
\qquad
\det(J|V_{\mathbb Z})=1.
\]

## 2. Corrected polar algebra (candidate-T / L1)

On the full integral group ring the identities are

\[
\Gamma N=0,
\qquad
\Gamma^2=5-N,
\qquad
2J-g(\Gamma-1)=N.
\]

The last equation is the safe integral form of the quotient statement.  A
formula containing \((\Gamma-1)/2\) requires the rational extension or an
explicit divisibility statement; it is not an identity in the integral group
ring by inspection alone.

On \(V_{\mathbb R}\), and only there unless a full-register correction is
displayed,

\[
H^2=I_V,\qquad U_5^*U_5=I_V,
\]

\[
U_5^2=g^2,\qquad U_5^5=H,\qquad U_5^{10}=I_V,
\]

and the order of \(U_5\) is exactly ten.  Moreover,

\[
B=B^*>0,\qquad B^2=J^*J,\qquad
J|_V=U_5B=BU_5.
\]

On the full register the corresponding formulas contain the augmentation
projector:

\[
H^2=P_V,\qquad U_5^{10}=P_V,\qquad
U_5B=J-\frac25N.
\]

For \(\zeta=\zeta_5\), \(a\in\{1,2,3,4\}\), and
\(\eta_a=(a/5)\), the proposed character formulas are

\[
\chi_a(\Gamma)=\eta_a\sqrt5,
\quad
\chi_a(U_5)=\eta_a\zeta^a,
\quad
\chi_a(B)=\varphi^{-\eta_a},
\]

\[
\chi_a(J)=1+\zeta^{2a}
=\eta_a\zeta^a\varphi^{-\eta_a},
\qquad \varphi=\frac{1+\sqrt5}{2}.
\]

With \(P_\pm=(I_V\pm H)/2\),

\[
B=\varphi^{-1}P_++\varphi P_-,
\qquad
B^{-1}=\varphi P_++\varphi^{-1}P_-.
\]

The Galois conjugation formulas are likewise sector-qualified:

\[
S\Gamma S^{-1}=-\Gamma,\qquad
SBS^{-1}=B^{-1},\qquad
SU_5S^{-1}=-U_5^3
\quad\text{on }V.
\]

For

\[
G=\langle U_5,S\rangle
\leq GL(V_{\mathbb Q(\sqrt5)}),
\]

exact enumeration gives

\[
|G|=80,\qquad
G\cap\{\alpha I\}=\{I,-I\},\qquad
|G/\{\pm I\}|=40.
\]

The eighty proposed linear normal forms are

\[
(-I)^\epsilon U_5^aS^b,\qquad
\epsilon\in\{0,1\},\quad0\leq a<10,\quad0\leq b<4.
\]

The projective quotient has the proposed presentation type
\(C_{10}\rtimes_3C_4\).  These proposed counts belong to the present
augmentation-sector group: eighty linear and forty after quotienting by
\(\{\pm I\}\).  They do not replace the distinct circular-quotient census
merged through PRs #798/#802, whose corresponding counts are forty linear and
twenty projective on a different carrier.

## 3. Corrected orbit algebra (candidate-T / L1)

The integral mixer numerator satisfies

\[
A^2=5g^2-N
\quad\text{on }R,
\qquad
A^2=5g^2
\quad\text{on }V.
\]

Consequently,

\[
\|A^nd\|_2^2=5^n\|d\|_2^2
\qquad(d\in V).
\]

Here \(5^n\) is the quadratic-norm multiplier.  It is not a path count.
The element \(A=1+g^2-g^3-g^4\) has four signed terms, so its unreduced word
expansion contains \(4^n\) labelled signed words.  End cells coincide and
opposite coefficients cancel.

For the supported vertex

\[
d_0=5e_0-N=(4,-1,-1,-1,-1),
\]

the complete mixer orbit is

\[
A^{2m}d_0=5^m g^{2m}d_0,
\]

\[
A^{2m+1}d_0
=5^m g^{2m}(5,0,5,-5,-5).
\]

Its normalized algebraic square profile alternates between a vertex
\((4/5,1/20,1/20,1/20,1/20)\) and a profile with one exact zero and four
entries \(1/4\), with period ten under \(U_5\).  These are square profiles,
not yet probabilities or event frequencies.

For the raw step,

\[
J^nd_0=5(1+g^2)^ne_0-2^nN.
\]

Every coordinate is congruent to \(-2^n\pmod5\), so none is zero for
\(n\geq0\).  Its quadratic norm

\[
q_n=\|J^nd_0\|_2^2
=10(\varphi^{2n}+\varphi^{-2n})
\]

has \(q_0=20\), \(q_1=30\), and
\(q_{n+2}=3q_{n+1}-q_n\).  Where the denominator is nonzero, the exact
plane-weight ratio is

\[
\frac{\|P_-J^nd\|_2^2}{\|P_+J^nd\|_2^2}
=\varphi^{4n}
\frac{\|P_-d\|_2^2}{\|P_+d\|_2^2}.
\]

An exposed exact witness at \(n=8\) is

\[
J^8d_0=(29,29,-76,94,-76),
\qquad \|J^8d_0\|_2^2=22070,
\]

with profile

\[
\frac1{22070}(841,841,5776,8836,5776).
\]

The boost and raw-step cuts are already different after one step:

\[
Bd_0=(2\sqrt5,-\sqrt5,0,0,-\sqrt5),
\quad
Jd_0=(3,-2,3,-2,-2),
\]

with respective square profiles

\[
(2/3,1/6,0,0,1/6)
\]

and

\[
(3/10,2/15,3/10,2/15,2/15).
\]

Thus the coordinate-square profile distinguishes the action of \(B\).
Calling \(B\) invisible requires an additional decoder law; it does not
follow from the polar decomposition.

## 4. Simplex/dilation boundary and quadratic support route

All statements in this section are candidate L1 algebra.  The words
"boundary" and "dilation" do not assign them to L3 or L4 without a separate
typed lift.

On \(V_{\mathbb R}\), define

\[
u_k=P_Ve_k=e_k-\frac15N,
\qquad
E_k=|u_k\rangle\langle u_k|\in\operatorname{End}(V_{\mathbb R}).
\]

Then

\[
\langle u_i,u_j\rangle=\delta_{ij}-\frac15,
\qquad
\sum_ku_k=0,
\]

\[
\sum_kE_k=I_V,
\qquad
E_k^2=\frac45E_k,
\qquad
\langle d,E_kd\rangle=d_k^2
\quad(d\in V_{\mathbb R}).
\]

On two full cell registers, the controlled addition

\[
C_{\mathrm{add}}(e_k\otimes e_j)=e_k\otimes e_{j+k\bmod5}
\]

is an integral permutation.  It sends

\[
d\otimes e_0
\longmapsto
\Psi_d=\sum_kd_ke_k\otimes e_k,
\]

whose unnormalized reduced Gram operator on the second cell factor is

\[
\operatorname{Tr}_1|\Psi_d\rangle\langle\Psi_d|
=\sum_kd_k^2|e_k\rangle\langle e_k|.
\]

This is a reversible algebraic construction.  It is not a physical partial
trace, apparatus, collapse, outcome, or frequency law.  Its proposed novelty
is only the marked five-cell controlled shift together with the explicit
orthogonal-dilation/nonorthogonal-simplex compression boundary; the simplex
facts already exposed through PR #802 and the registered rational-dilation
nonselection theorem are inputs, not reclaimed outputs.

For the conditional support theorem, let

\[
W_k=W_k^*\succeq0
\quad\text{in }\operatorname{End}(V_{\mathbb R}),
\qquad
w_k(d)=\langle d,W_kd\rangle.
\]

If exact darkness is imposed for every \(d\in V_{\mathbb R}\) as

\[
d_k=0\Longrightarrow w_k(d)=0,
\]

then \(W_k\) vanishes on the hyperplane \(u_k^\perp\).  Positivity forces
\(\operatorname{rank}W_k\leq1\) and
\(\operatorname{im}W_k\subseteq\operatorname{span}(u_k)\).  Hence

\[
W_k=c_kE_k,
\qquad c_k\geq0.
\]

Covariance is frozen at least under the transitive cycle,

\[
gW_kg^{-1}=W_{k+1\bmod5},
\]

and makes the coefficients equal.  The exact normalization

\[
\sum_kW_k=I_V
\]

then gives \(c_k=1\).  This proves a Born-form conclusion *inside the
positive-semidefinite quadratic class*.  It does not transport the public
`AFFINE-QUADRATIC-FORM-UNIQUENESS` result to this carrier; Schur uniqueness of
a total form, where independently established, still would not choose five
outcome weights or prove quadraticity.

The old counterfamily makes the missing support law explicit.  At the operator
level it is

\[
F_k^{(t)}=tE_k+\frac{1-t}{5}I_V,
\qquad 0\leq t\leq1,
\]

and, for \(d\ne0\), its normalized response is

\[
p_k^{(t)}(d)
=\frac{\langle d,F_k^{(t)}d\rangle}{q(d)}
=t\frac{d_k^2}{q(d)}+\frac{1-t}{5},
\qquad q(d)=\sum_jd_j^2.
\]

It is normalized and covariant for every \(t\), while exact darkness for a
nonzero state with \(d_k=0\) forces \(t=1\).  Darkness is therefore a genuine
physical input about occurrence, not a consequence of Schur's lemma.

Proposed future row, not activated here:

```text
EXACT-OUTCOME-NULL-EXCLUSION [candidate-H / future L5 / STOP]
If a supported preparation has exactly d_k=0 at the calibrated read cut,
then no record k occurs.

Falsifier: a preregistered record k at a calibrated exact-zero cell, after
apparatus background, dark counts, finite resolution, and read-cut ownership
have been frozen independently of the result.
```

## 5. Power-sum rigidity without Lamperti (candidate-T / L1)

For finite \(r>0\), define

\[
P_r(d)=\sum_{k=0}^4|d_k|^r.
\]

The following are equivalent:

\[
P_r(U_5d)=P_r(d)
\quad\text{for every }d\in V_{\mathbb R},
\]

\[
P_r(Ad)=\lambda P_r(d)
\quad\text{for every }d\in V_{\mathbb R}
\quad\text{for one state-independent }\lambda>0,
\]

and

\[
r=2.
\]

In that case \(\lambda=5\).  This does not need Lamperti's theorem.  The
standard full-space Lamperti classification does not directly apply because
\(U_5\) is a Euclidean isometry on the codimension-one space \(V\), not an
invertible map of the full \(\ell^r_5\).

For a direct proof, use

\[
h=(-1,1,0,0,0),
\qquad
Ah=(-2,1,-1,2,0).
\]

If only supported centered plenum states are admitted, replace \(h\) by
\(5h=D(h)\); homogeneity leaves the equation unchanged.  Preservation by
\(U_5=A/\sqrt5\) gives

\[
2^r+1=5^{r/2},
\]

or

\[
\left(\frac2{\sqrt5}\right)^r
+\left(\frac1{\sqrt5}\right)^r=1.
\]

The left side is strictly decreasing for \(r>0\), and it equals one at
\(r=2\).  This is the unique solution.  Conversely,
\(A^*A=5I_V\) proves the quadratic case.  If similarity under \(A\) is the
starting condition, iteration of \(A^{10}=5^5I_V\) first forces
\(\lambda=5^{r/2}\), reducing it to the same equation.

The lattice \(\operatorname{im}D\) is not itself \(U_5\)-stable.  The scaled
tower \(\bigcup_{n\geq0}5^{-n/2}\operatorname{im}D\) is a possible invariant
dense mathematical domain, but adopting it as a preparation domain would be a
separate decision.  The single supported witness proves the universal
functional theorem; it does not supply that physical closure.

The factor \(5^n\) is therefore a conclusion after \(r=2\) is selected:

\[
P_2(A^nd)=5^nP_2(d).
\]

It must not be inserted into the physical premise and must not be called the
number of paths.

## 6. Exact logical boundary of the power route

Inside the explicitly frozen raw family

\[
w_k(d)=c|d_k|^r,
\qquad c>0,
\]

the candidate chain is:

```text
exact darkness + U5 conservation of raw total + cell covariance
+ absolute normalization  =>  quadratic cell weights.
```

The two-parameter family

\[
w_k^{(r,t)}(d)
=t|d_k|^r+(1-t)\frac{P_r(d)}5,
\qquad r>0,\quad0\leq t\leq1,
\]

separates the two restrictions.  Its total is \(P_r(d)\); mixer conservation
forces \(r=2\), while exact darkness at a zero coordinate forces \(t=1\).
After normalization the surviving rule is the Born square profile.

This is not an unrestricted derivation.  Without coordinate separability, for
every \(r>0\) and \(d\ne0\) the state-coupled family

\[
\widetilde w_k^{(r)}(d)
=\|d\|_2^2
\frac{|d_k|^r}{\sum_j|d_j|^r}
\]

is nonnegative, cell-covariant, exactly dark when \(d_k=0\), and has total
\(\|d\|_2^2\), which \(U_5\) preserves.  Nevertheless its normalized profile
has exponent \(r\).  Thus darkness, total conservation, covariance, and
normalization do **not** imply Born without a local/separable response law or
an equally strong apparatus principle.  Multiplication of all raw weights by
an arbitrary state-dependent common factor is invisible to conditional
frequencies.

The physical conservation statement is meaningful only for an absolute raw
yield or intensity under fixed exposure and calibrated gain.  If every trial
is defined to return exactly one record, preservation of the normalized total
is a tautology and constrains no exponent.

Proposed future row, not activated here:

```text
U5-TOTAL-RAW-WEIGHT-CONSERVATION [candidate-H / future L5 / STOP]
For a frozen raw extensive weight W, fixed exposure and gain, and a supported
preparation, W(U5 d)=W(d).

Falsifier: different calibrated absolute raw totals before and after U5 for
the same preregistered preparation, with the apparatus and gain fixed before
the comparison.
```

This row can belong to \(U_5\), or to \(A\) with the derived quadratic
multiplier five.  It cannot be asserted for the raw \(J=U_5B\).  For example,

\[
\frac{P_2(J[5(1,-1,0,0,0)])}{P_2(5(1,-1,0,0,0))}=2,
\qquad
\frac{P_2(Jd_0)}{P_2(d_0)}=\frac32.
\]

Therefore branch (a), in which raw \(J\) is physical, needs separate
accounting for \(B\); the proposed conservation row cannot silently govern
the complete raw step.

## 7. A possible regular extension beyond powers (candidate lemma only)

There is a stronger mathematical route for a *common coordinate-separable*
response \(f:[0,\infty)\to[0,\infty)\),

\[
w_k(d)=f(|d_k|),
\qquad
\Phi(d)=\sum_kf(|d_k|).
\]

If the preparation domain is all of \(V_{\mathbb R}\), \(f\) is continuous,
and

\[
\Phi(U_5d)=\Phi(d)
\qquad(d\in V_{\mathbb R}),
\]

then the proposed conclusion is

\[
f(t)=at^2+c.
\]

Proof outline.  The form of \(\Phi\) makes it automatically invariant under
cell permutations \(S_5\).  The closure of \(\langle S_5,U_5\rangle\) in
\(O(V)\) is all of \(O(V)\): for the transposition \(\tau=(01)\),

\[
\operatorname{tr}_V(U_5\tau)=\frac2{\sqrt5},
\]

which is not an algebraic integer, so \(U_5\tau\) has infinite order.  The
closure therefore has nonzero Lie algebra.  This Lie algebra is an
\(S_5\)-invariant subspace of
\(\mathfrak{so}(V)\cong\Lambda^2V\).  The latter is irreducible: its character
on the conjugacy classes \(1,2,2^2,3,3\!\cdot\!2,4,5\) is

\[
(6,0,-2,0,0,0,1),
\]

whose class-size-weighted character inner product with itself is
\((36+15\cdot4+24)/120=1\).  Hence the identity component is
\(SO(V)\); a transposition supplies determinant minus one, giving the whole
\(O(V)\).

Regularity extends invariance from the dense subgroup to \(O(V)\), so
\(\Phi\) is radial on \(V\).  Comparing equal-norm vectors for
\(a,b\geq0\),

\[
(a,-a,b,-b,0)
\quad\text{and}\quad
(c,-c,0,0,0),
\qquad c^2=a^2+b^2,
\]

shows that

\[
f(\sqrt{a^2+b^2})-f(0)
=[f(a)-f(0)]+[f(b)-f(0)].
\]

The regular Cauchy equation gives \(f(t)=at^2+c\).  Exact darkness fixes
\(c=f(0)=0\), positivity gives \(a\geq0\), and an absolute normalization fixes
the remaining scale.

This lemma is deliberately not assigned to the first formal probe.  It adds a
topological preparation domain, regularity, and a dense-group argument.  On a
smaller integral domain it does not follow from the statement above.

Regularity and richness of the preparation domain are both load-bearing.  On
\(K=\mathbb Q(\sqrt5)\), with
\(\sigma(\sqrt5)=-\sqrt5\), define the restricted response

\[
f:K_{\geq0}\to\mathbb R_{\geq0},
\qquad
f(t)=t^2+\sigma(t)^2.
\]

For \(d\in V_K\) it is nonnegative, dark at zero, and its total is preserved
by \(U_5\), since \(\sigma(U_5)=-U_5\).  It is not \(at^2\) on all of \(K\),
is discontinuous in the chosen real embedding, and reads both Galois
embeddings.  For an integer start \(d\in V_{\mathbb Z}\), however,
\(\sigma(U_5^nd)=(-1)^nU_5^nd\), so along that pure orbit the response is
exactly \(2t^2\).  The restricted example therefore shows why both regularity
and the preparation domain must be frozen; by itself it is not a
counterexample to the preceding all-real continuous theorem.  In the TWIST
reading, regularity would exclude a second-embedding decoder rather than act
as a merely technical condition.

## 8. Layer ledger and surviving STOPs

The earned layer ceiling of this note is:

| Layer | What this proposal currently supplies | What it does not supply |
| --- | --- | --- |
| L1 | all new group-ring, polar, orbit, simplex, controlled-shift, profile, and conditional rigidity algebra in this note | physical time, probability, detector, or layer lift |
| L2 | NONE | manifold, spacetime, or gravity |
| L3 | NONE | a typed boundary record/effect lift |
| L4 | NONE | apparatus, ready state, physical dilation, reduction, or outcome |
| L5 | NONE | a typed realized-event stream or physical current |
| L6 | NONE | empirical frequencies, measure, or a plenum Born reading |

The design intends the simplex labels as a possible future L3 boundary, the
controlled shift as a possible future L4 realization, the two physical rows as
future L5 laws, and a normalized occurrence law as a future L6 reading.  Those
are target annotations only.  Each requires an explicit typed source and
cross-layer gate; no such lift is earned here.

`QDD-INSTRUMENT-APPARATUS [O]` remains open.  The two proposed physical rows
remain `candidate-H / STOP` until a typed apparatus, an L1-to-L5 event stream,
a calibrated raw yield, and a scope-compatible application of the existing
`GATE-L5-L6-BORN-READING` (or an explicitly distinct gate) exist.  The public
gate does not cover this plenum proposal without that typed source.  These
rows do not activate a replacement for `MEASURE-BORN-VERB [D]` in Public
Canon v75.

The owner's design preference for branch (a) is recorded as a candidate-H, not
adopted or supplied by the algebra.  The exact distinctions are:

1. raw \(J\) includes the non-scalar positive factor \(B\), its coordinate
   square profile differs from the pure mixer profile, and it does not
   conserve one state-independent quadratic total;
2. pure \(U_5\) has the periodic vertex/hole profiles but needs a rule saying
   why \(B\) is separately accounted for;
3. a third circular/bilocated reading has been proposed elsewhere, but its
   carrier, map, and comparison are not defined or claimed by this note.

Choosing among these remains a physical owner decision, not an algebraic
corollary.

## 9. Split future proof-first work

No verifier is attached to this note.  Future work is divided so that no
physical conclusion can hitchhike on a finite algebra audit.

### 9.1 `P-J-PLENUM-POLAR-GAUSS-1`

Proposed claims:

```text
J-PLENUM-POLAR-GAUSS
J-PLENUM-POLAR-ORBIT-SEPARATION
```

Scope: candidate-T / L1 only.  It may test the full-register identities,
centering lattice, polar factors on \(V\), spectrum, Galois conjugation,
linear/projective orders \(80/40\), exact mixer and raw-step orbit formulas,
boost visibility, and norm multipliers.  It must exclude Born, path counts,
physical time, gravity, apparatus, outcome occurrence, and L2--L6 lifts.

### 9.2 `P-J-SIMPLEX-TIGHT-FRAME-DILATION-BOUNDARY-1`

Proposed claims:

```text
J-SIMPLEX-TIGHT-FRAME-DILATION
J-SIMPLEX-QUADRATIC-SUPPORT-RIGIDITY
```

Scope: candidate-T / L1 algebra only, with L3/L4 merely named as a proposed
future semantic boundary.  It may re-audit inherited simplex inputs while
claiming only the combined marked five-cell controlled-shift/compression
boundary and the quadratic support-rigidity implication.  It may test the
controlled-shift permutation, rank obstruction to copying the five
nonorthogonal quotient vertices, and the exact reduced diagonal Gram profile.
Before a lock it must compare the divergent notes branch and state the exact
novelty against PR #802 and `QDD-INSTRUMENT-NONSELECTION`.  It must not reclaim
their public facts or claim an apparatus choice, physical dilation, outcome,
probability, frequency, or any L2--L6 lift.

If locked, the order \(80/40\) would be owned by the first probe.  A later
boundary probe may import or guard it but must not reclaim it as a new result.

### 9.3 `P-J-U5-POWER-SUM-RIGIDITY-1`

Proposed claim:

```text
J-U5-POWER-SUM-RIGIDITY
```

Scope: candidate-T / L1 only.  It owns the direct \(r>0\) theorem of section
5 and its supported-lattice witness.  The proof, not finite samples at
\(r=1,3,4\), carries the universal exponent conclusion.  The verifier may
audit the exact matrix identities and witnesses but cannot turn the physical
conservation premise into a theorem.

Each formal probe requires a fresh public issue lock, its own branch and
directory, an atomic public pin of `PREREG.md` plus the unexecuted accepted
verifier, byte-for-byte public readback, exactly one local formal execution,
an immutable transcript and result, a one-probe pull request, independent
two-architecture reproduction, security review, and merge without squash or
rebase.

Even a completed probe would leave its result publicly unregistered at the
candidate ceiling.  Registration as `[T]`, any `[H]` move, and every layer or
gate change require a later, separate sealed Canon fold.

## 10. Firewalls

- This note is non-canonical and changes no v75 row, dependency, gate,
  dictionary, status, tag, release, or frontier.
- No theorem here supplies physical time, space, gravity, Planck's constant,
  an anyon model, universality, a Clifford classification, or classical
  simulability.
- \(\sqrt5\) is an algebraic scale in the tower, not a measured action quantum.
- Cells label algebraic records; they are not spatial points.
- \(B\) is a polar factor.  Calling it gravity or an attractor is a hypothesis.
- The cell square profiles are algebraic.  They are not probabilities until a
  typed occurrence and reading law exists.
- Exact darkness is a candidate physical law only after the read cut,
  preparation, apparatus background, and record semantics are frozen.
- Raw-total conservation is nontrivial only for calibrated absolute yield; it
  is not the identity that normalized probabilities sum to one.
- The power-sum theorem applies to a frozen common separable power law.  It
  says nothing by itself about arbitrary response functionals.
- The regular separable extension needs all of \(V_{\mathbb R}\) and explicit
  regularity.  It is not a theorem about only integral starts or finite orbits.
- The full \(S_5\) used in the regular separable lemma comes from the common
  coordinate response ansatz; it is not identified with the proposed
  eighty-element marked algebraic group, and no physical gate group is
  identified here.
- \(4^n\) counts formal signed words; \(5^n\) is a quadratic-norm multiplier.
- `QDD-INSTRUMENT-APPARATUS [O]`, L5 occurrence, empirical frequencies, the
  L5-to-L6 Born gate, and the physical choice among \(J\), \(U_5\), and the
  circular product remain open.
- `SAMPLING NOT PROVIDED` remains in force; it does not mean sampling is
  impossible.
