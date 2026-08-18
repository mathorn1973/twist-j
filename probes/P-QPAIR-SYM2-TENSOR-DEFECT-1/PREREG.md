# P-QPAIR-SYM2-TENSOR-DEFECT-1 preregistration

```text
PROBE AUTHORITY: none; zero-run formal-probe pin candidate
PUBLIC CANON:    canon-v50, content b68c60c57cfd0b1e655b6fc4d5496a333a249fdf
CLAIM LOCK:      https://github.com/mathorn1973/twist-j/issues/411
BASE:            8359889ebac9ef85e05d4abe4d676c731b880167
BRANCH:          probe/P-QPAIR-SYM2-TENSOR-DEFECT-1
PATH:            probes/P-QPAIR-SYM2-TENSOR-DEFECT-1/
OWNER:           A. M. Thorn / delegated session bell_r_repo
ACTION LAYER:    L1 exact multilinear algebra
MODE:            result-exposed, proof-first; verifier is an exact finite audit
FORMAL RUNS:     none at this pin; verify.py was neither imported nor run
STATIC CHECK:    syntax-only py_compile PASS before pin
```

This file and `verify.py` freeze the equation, conventions, proof, exact audit,
systematics, and falsifiers before the first formal execution.  No status is
earned by this preregistration.  If the written proofs and every formal gate
survive, the status ceiling for each of the three named targets below is `T`.

## Field 1. Equation

### 1.1 Typed pair carrier and conventions

Let `K` be a field equipped with an involution `c`; the bar on a vector space
is a type marker with scalar action transported by `c`.  Put

\[
 H(V)=V\otimes\bar V,\qquad S(V)=\operatorname{Sym}^2V,
 \qquad {\cal Q}(V)=H(V)\oplus S(V),
\]

and, for a vector `v`,

\[
 H(v)=v\otimes\bar v,\qquad S(v)=v\otimes v,
 \qquad Q(v)=(H(v),S(v)).
\]

For the symmetric-square theorem assume `char(K) != 2` and identify
`Sym^2 V` with the `+1` eigenspace of factor interchange in `V tensor V`.
The conventions that fix every coefficient are

\[
 u\wedge v:=u\otimes v-v\otimes u,
 \qquad P_-:=\frac{1-\tau}{2}.
\]

No square-root normalization is hidden in either convention.

Canonical tensor-factor reorderings define matched products

\[
 \boxtimes_H:H(V)\otimes H(W)\longrightarrow H(V\otimes W),
\]

\[
 (v\otimes\bar v')\boxtimes_H(w\otimes\bar w')
 =(v\otimes w)\otimes\overline{(v'\otimes w')},
\]

and

\[
 \boxtimes_S:S(V)\otimes S(W)\longrightarrow S(V\otimes W),
\]

where `boxtimes_S` is the restriction of the same reordering to the
`(+,+)` sector.  Define the bilinear componentwise law

\[
 \mu_{V,W}((A,B),(C,D))
   =(A\boxtimes_H C,\;B\boxtimes_S D).                 \tag{1}
\]

Equivalently, its linear extension from
`Q(V) tensor Q(W)` kills the two cross sectors and retains the two matched
sectors.

### Target P1. QPAIR-PRODUCT-COMPOSITION

The maps `mu` are natural, associative, symmetric, and unital, with unit
`Q(1)=(1,1)` under the canonical identifications with the tensor unit.  For
all vectors `v,w`,

\[
 Q(v\otimes w)=\mu_{V,W}(Q(v),Q(w)).                  \tag{2}
\]

The equality is exact for product vectors and extends bilinearly on the
declared matched carrier sectors.  It does not assert that every square of an
entangled vector lies in the image of `boxtimes_S`.

### Target P2. QPAIR-CROSS-SECTOR-NONDESCENT

For a unit `lambda in K`, change a factorization without changing its product:

\[
 (v,w)\longmapsto(\lambda v,\lambda^{-1}w),\qquad
 (\lambda v)\otimes(\lambda^{-1}w)=v\otimes w.        \tag{3}
\]

The four sectors of `Q(V) tensor Q(W)` have factor-gauge weights

\[
\begin{array}{c|c}
H(V)\otimes H(W)&1\\
S(V)\otimes S(W)&1\\
H(V)\otimes S(W)&c(\lambda)/\lambda\\
S(V)\otimes H(W)&\lambda/c(\lambda).
\end{array}                                           \tag{4}
\]

In `K=Q(zeta_5)` with `c(zeta_5)=zeta_5^{-1}`, the two cross weights are
`zeta_5^3` and `zeta_5^2`, neither of which is one.  Hence neither nonzero
cross-sector tensor is a function of the composite pure tensor alone.  The
matched-sector law (1) is a typed descent through the factorization gauge;
removing the cross sectors is not an arbitrary deletion of two invariant
functions.

### Target P3. QPAIR-SYM2-TENSOR-DEFECT

Let `dim V=dim W=2`.  Reorder

\[
 R:(V\otimes W)^{\otimes2}\longrightarrow
      V^{\otimes2}\otimes W^{\otimes2},
\]

\[
 R((v\otimes w)\otimes(v'\otimes w'))
 =(v\otimes v')\otimes(w\otimes w').                 \tag{5}
\]

On the reordered space let `alpha` swap the two `V` factors and `beta` swap
the two `W` factors.  They commute, and the swap of the two `V tensor W`
factors is `alpha beta`.  Freeze

\[
 P_{++}=\frac14(1+\alpha)(1+\beta),\qquad
 P_{--}=\frac14(1-\alpha)(1-\beta).                  \tag{6}
\]

Then

\[
 \operatorname{Sym}^2(V\otimes W)
 =\bigl(\operatorname{Sym}^2V\otimes\operatorname{Sym}^2W\bigr)
  \oplus
  \bigl(\Lambda^2V\otimes\Lambda^2W\bigr),           \tag{7}
\]

with dimensions

\[
 10=9+1.                                               \tag{8}
\]

The linear span of the product squares
`(v tensor w) tensor (v tensor w)` is exactly the first, nine-dimensional
summand.  This is a statement about the linear span in the quadratic target;
the set of product states is not itself a nine-dimensional vector subspace.

Fix bases `e_0,e_1` and `f_0,f_1`, and write

\[
 x=a\,e_0f_0+b\,e_0f_1+c\,e_1f_0+d\,e_1f_1,
 \qquad
 \kappa=(e_0\wedge e_1)\otimes(f_0\wedge f_1).        \tag{9}
\]

With exactly the conventions above,

\[
 P_{--}R(x^{\otimes2})=\frac{ad-bc}{2}\,\kappa.       \tag{10}
\]

For `g in GL(V)` and `h in GL(W)`, the missing line has character

\[
 (g^{\otimes2}\otimes h^{\otimes2})\kappa
   =\det(g)\det(h)\,\kappa.                            \tag{11}
\]

It is therefore fixed by `SL(V) times SL(W)`.  For nonzero `x`, (10) vanishes
exactly when the coefficient matrix

\[
 X=\begin{pmatrix}a&b\\c&d\end{pmatrix}
\]

has rank one, equivalently when `x` is a product vector.  The zero vector also
lies in the determinantal cone but is not called a state.

Over the normalized complex two-qubit Hilbert space, the ordinary pure-state
concurrence is

\[
 C(x)=2|ad-bc|.                                        \tag{12}
\]

It is zero on product states and equals one on normalized Bell states.  This
last sentence is an interpretation of the determinant coefficient after a
complex norm has been supplied, not an additional assertion over an arbitrary
field.

### Wording firewall

The one-dimensional summand in (7) is the determinant/concurrence direction
in the **quadratic target**.  It is not a vector in `V tensor W`, not a Bell
state, and not the two-qubit singlet.  A Bell state is an input vector whose
square has a nonzero, maximized projection to this line.  The word "singlet"
may be used only for invariance of the determinant line under
`SL_2 times SL_2`, never as an identification with the usual antisymmetric
two-qubit state.

The `9+1` theorem is only for the symmetric slot.  No claim is made that a
full Hermitian-plus-symmetric nonlinear or informational entanglement defect
has dimension one.  No `BELL-CAUSAL-ACCOUNTING` row or dependency is created.

The same firewall applies to the public decoder route.  This probe creates no
dependency edge to `QUADRATIC-DECODER-DATA [O]`, does not modify
`QDD-QCARRIER-DIAGONAL-BOUNDARY [T]`, and supplies no bridge from its abstract
tensor carriers to the frozen rational `V_eff` carrier.  Both QDD rows retain
their current public statuses and scopes.

### What is not claimed

No surjectivity of product composition onto all entangled squares; no
information-theoretic minimality of the full pair; no polynomial
reconstruction of one slot from the other; no extension to characteristic
two; no mixed-state concurrence; no density-matrix classification; no
observable, Born, decoder, instrument, causal, spacetime, force, SI-unit, or
L2--L6 statement.  The primitive fifth root is only an exact witness to
factor-gauge non-descent and carries no fifth-prime physical content.

## Field 2. Code

`verify.py` is Python standard library only and deterministic.  It uses
`fractions.Fraction` for every scalar matrix and polynomial coefficient, and
an exact four-coordinate `Q(zeta_5)` representation for the gauge witness.
It contains no float literal, random choice, external input, network access,
or third-party import.

The exact audit includes:

1. typed product composition, bilinearity witnesses, naturality,
   associativity, symmetry, and the tensor unit;
2. formal reciprocal factor-gauge bidegrees and the exact `zeta_5` witness;
3. the commuting involutions `alpha,beta`, their projectors, orthogonality,
   and exact ranks `10,9,1` in the sixteen-dimensional reordered ambient
   space;
4. a rank-nine basis of product squares and equality of its span with the
   `(+,+)` image;
5. a generic polynomial identity for `(ad-bc) kappa / 2`;
6. a generic polynomial determinant-character identity and a direct exact
   exterior-character control; and
7. exact product and unnormalized Bell representatives, with concurrence
   ratios computed rationally.

The written proofs below carry the universal quantifiers.  The verifier is a
finite exact audit of those proofs, not an enumeration standing in for them.
After the immutable pin, the formal command will be

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-QPAIR-SYM2-TENSOR-DEFECT-1/verify.py
```

Exit zero requires every gate to print `PASS`; any failure exits one.  Stdout
will become the sole formal audit transcript only after `EXPECTED.txt` is
frozen; the written proofs carry the universal results.  This zero-run pin
contains no `EXPECTED.txt`, `RUN.md`, or `RESULT.md`.

## Field 3. Carrier or data

No external data, measurement, fit, lookup table, or stochastic sample.
The audit carrier is exact finite-dimensional multilinear algebra over the
rationals, exact generic polynomials, and the single algebraic witness
`Q(zeta_5)`.  Rational matrices audit characteristic-zero instances; the
written eigenspace proof supplies the theorem over every field of
characteristic not two.

## Field 4. Systematics

```text
S1  Sym^2 is the +1 eigenspace model, valid because 2 is invertible.
S2  R orders tensor factors as (V_1,V_2,W_1,W_2).
S3  u wedge v = u tensor v - v tensor u; it is not divided by two.
S4  P-- = (1-alpha)(1-beta)/4.  With S3 this fixes det(X)/2.
S5  Product-square span means linear span in the quadratic target, not the
    nonlinear Segre set and not the input state space.
S6  The bar is a type marker for H; c is used only when scalar gauge weights
    are evaluated.  The zeta_5 witness is over Q(zeta_5), characteristic zero.
S7  Bell and concurrence wording is confined to normalized complex pure
    states.  Rational Bell controls use unnormalized representatives.
S8  Naturality and coherence are proved from canonical tensor permutations;
    finite rational matrices are audits, not the universal source.
S9  The 9+1 assertion belongs only to the symmetric slot.  No causal row or
    full-pair informational dimension is inferred.
```

## Field 5. Failure threshold

Exact and binary.  Any scientific falsifier below records the probe `F`; no
threshold may be moved after the pin.

```text
F1  Q(v tensor w) differs from mu(Q(v),Q(w)), or naturality,
    associativity, symmetry, unitality, or bilinearity fails.
F2  either matched sector is gauge-dependent, either cross weight differs
    from c(lambda)/lambda and lambda/c(lambda), or the zeta_5 witness is
    trivial.
F3  alpha and beta do not commute, the simultaneous-swap fixed space is not
    the direct sum of ++ and --, or the ranks are not 10, 9, and 1.
F4  product squares do not span exactly the ++ image.
F5  the coefficient of kappa differs from (ad-bc)/2, the line does not carry
    det(g)det(h), or determinant zero fails to characterize the product cone.
F6  either exact product/Bell control contradicts the determinant and
    normalized pure-state concurrence formulas.
```

A verifier/expected-output/hash mismatch, any execution before the immutable
pin, a float in an asserted identity, an unapproved dependency, or wording
that crosses the firewall is an integrity or scope `STOP`, not a rewritten
scientific threshold.

## Field 6. Action layer

`L1`, state and exact carrier algebra, and only `L1`.  Equations (1)--(12)
describe tensor-factor composition and a quadratic representation-theoretic
decomposition.  They create no lift, gate, observable, measure, causal
accounting, or action at L2 through L6.

## Proofs

These proofs carry the universal statements.  The exact verifier independently
audits their coordinates and finite coherence witnesses.

### Proof of P1: product composition and coherence

On an elementary Hermitian tensor, the canonical reordering gives

\[
\begin{aligned}
 H(v)\boxtimes_H H(w)
 &=(v\otimes\bar v)\boxtimes_H(w\otimes\bar w)\\
 &=(v\otimes w)\otimes\overline{(v\otimes w)}
 =H(v\otimes w).
\end{aligned}
\]

On the symmetric component,

\[
 S(v)\boxtimes_S S(w)
 =(v\otimes w)\otimes(v\otimes w)=S(v\otimes w).
\]

Together these are (2).  Both matched products are restrictions of canonical
permutations and reassociations of tensor factors.  For maps `f:V -> V'` and
`g:W -> W'`, applying `f tensor bar(f)` and `g tensor bar(g)` before the
Hermitian reordering gives the same elementary tensor as applying
`(f tensor g) tensor overline(f tensor g)` afterwards.  The identical
argument without bars proves naturality on the symmetric component.
Linearity proves naturality everywhere.

For three factors, both parenthesizations send every elementary tensor to the
same ordered tensor with factor order `V,W,U` in each typed copy.  Hence they
are associative under the canonical associator.  Interchanging `V,W` before
or after reordering produces the canonical braiding on the target, proving
symmetry.  With the one-dimensional tensor unit, multiplication by the two
unit tensors in `Q(1)=(1,1)` changes neither component.  This proves unitality.
All constructions are bilinear, so the identities extend to the declared
linear carrier span.  QED

### Proof of P2: reciprocal factor-gauge non-descent

Scalar multiplication gives

\[
 H(\lambda v)=\lambda c(\lambda)H(v),\qquad
 S(\lambda v)=\lambda^2S(v).
\]

Because `c` is an involutive field automorphism,

\[
 H(\lambda^{-1}w)
   =\lambda^{-1}c(\lambda)^{-1}H(w),\qquad
 S(\lambda^{-1}w)=\lambda^{-2}S(w).
\]

Multiplication of the corresponding factors gives weight one on `H tensor H`
and on `S tensor S`.  On `H tensor S` it gives
`lambda c(lambda) lambda^{-2}=c(lambda)/lambda`; on `S tensor H` it gives
`lambda^2 lambda^{-1}c(lambda)^{-1}=lambda/c(lambda)`.  This proves (4).

Now take nonzero `v,w` over `Q(zeta_5)` and `lambda=zeta_5`.  Conjugation sends
`lambda` to `lambda^{-1}`, so the two cross weights are `lambda^{-2}=lambda^3`
and `lambda^2`.  A primitive fifth root has neither power equal to one.  The
two factorizations in (3) determine the same nonzero composite pure tensor but
different nonzero cross-sector tensors.  A function of the composite tensor
must take one value on that common input, so no such function can equal either
cross sector.  The matched sectors are invariant and therefore do descend.
QED

### Proof of P3(a): the `++` and `--` decomposition

Under `R`, let `alpha` and `beta` be as in (6).  They are commuting
involutions.  Since two is invertible, each is semisimple with eigenvalues
`+1,-1`; their joint projectors are

\[
 P_{\epsilon\eta}=\frac14(1+\epsilon\alpha)(1+\eta\beta),
 \qquad \epsilon,\eta\in\{+1,-1\}.
\]

They are pairwise orthogonal and sum to one.  Their images are respectively

\[
\begin{array}{c|c}
++&\operatorname{Sym}^2V\otimes\operatorname{Sym}^2W\\
+-&\operatorname{Sym}^2V\otimes\Lambda^2W\\
-+&\Lambda^2V\otimes\operatorname{Sym}^2W\\
--&\Lambda^2V\otimes\Lambda^2W.
\end{array}
\]

The swap of the two composite factors is `alpha beta`, so its `+1`
eigenspace consists exactly of the joint eigenspaces whose signs multiply to
`+1`: `++` and `--`.  This proves (7).  In dimension two,
`dim Sym^2=3`, `dim Lambda^2=1`, and `dim Sym^2(V tensor W)=4*5/2=10`; hence
`10=3*3+1*1=9+1`.  QED

### Proof of P3(b): product-square span

For every product vector, (5) gives

\[
 R((v\otimes w)^{\otimes2})=v^{\otimes2}\otimes w^{\otimes2},
\]

which lies in the `++` summand.  Pure squares span every symmetric square in
characteristic not two: for basis vectors `u_i,u_j`,

\[
 u_i\otimes u_j+u_j\otimes u_i
 =(u_i+u_j)^{\otimes2}-u_i^{\otimes2}-u_j^{\otimes2}.
\]

Thus the squares of vectors span `Sym^2V`, and independently the squares of
vectors span `Sym^2W`.  Tensor products of spanning sets span their tensor
product.  Consequently the linear span of product squares is all and only the
`++` summand.  In the two-by-two case it has dimension nine.  QED

### Proof of P3(c): determinant coefficient

Only terms of `R(x tensor x)` containing both basis indices in each factor can
survive `P--`.  The four relevant ordered terms are

\[
\begin{array}{c|c}
ad&e_0e_1f_0f_1\\
da&e_1e_0f_1f_0\\
bc&e_0e_1f_1f_0\\
cb&e_1e_0f_0f_1.
\end{array}
\]

The first two project to `kappa/4`; the last two project to `-kappa/4`.
Therefore

\[
 P_{--}R(x^{\otimes2})
 =\frac{ad+da-bc-cb}{4}\kappa
 =\frac{ad-bc}{2}\kappa,
\]

proving (10).  QED

### Proof of P3(d): character, product cone, and concurrence firewall

The elementary exterior identity in dimension two is

\[
 (ge_0)\wedge(ge_1)=\det(g)(e_0\wedge e_1),
\]

and similarly for `h`; their tensor product is (11).  A nonzero two-by-two
matrix has determinant zero exactly when it has rank one.  Rank-one coefficient
matrices are exactly the decomposable tensors `v tensor w`, proving the
product-cone statement.

Finally specialize, and only now, to a normalized complex two-qubit vector.
The standard pure-state concurrence is `2|det X|`.  If the singular values of
`X` are `s_1,s_2`, normalization gives `s_1^2+s_2^2=1`, while
`2|det X|=2s_1s_2 <= 1`, with equality exactly at
`s_1=s_2=1/sqrt(2)`.  Bell states attain that equality; product states have
one singular value zero.  This relates Bell inputs to the size of the
determinant projection without identifying the determinant line with a Bell
state or with the two-qubit singlet.  QED
