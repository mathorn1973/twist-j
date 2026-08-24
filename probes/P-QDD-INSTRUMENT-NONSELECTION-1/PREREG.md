# P-QDD-INSTRUMENT-NONSELECTION-1 preregistration

Date: 2026-08-16

Author of record: A. M. Thorn

Status: preregistered protocol only. No scientific result is earned by this
file. No formal gate may run before this file and the accepted verifier are
both present at the immutable pin, that pin is pushed, and both files are read
back from the public remote.

Public claim lock: issue 391.

## Authority record

```text
STATE:          ACTIVE
CANON:          Public Canon v48
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v48
CONTENT_COMMIT: d1d0df6d08dcb6b610719bc17151aabb97cc9d96
CANON_SHA256:   65dfa8509abfdf44fdd1198c93d476d01f1c93ca3066c1f573aab6bbc70879bb
CANON_BYTES:    234810
BASE_COMMIT:    88f376aa4df3d55449d152e024dfe399557890b3
```

Target live row: `QDD-INSTRUMENT-APPARATUS [O]`.

This probe does not attempt positive closure of that row. It isolates the exact
rational theorem layer showing what an unrestricted orthogonal dilation can and
cannot select.

## Mandatory result-exposure disclosure

A prior NON-CANONICAL incubation,
`notes/canon/C-QDD-INSTRUMENT-DILATION-1-N.md` on a separate note branch,
contains closely related formulas, local exact checks, corrections and the
negative nonselection idea. Those calculations predate this public
preregistration and therefore are discovery context only.

Every prior run, transcript, count, hash, witness search and one-architecture
calculation from that incubation is excluded from formal evidence for this
probe. The accepted verifier in this directory is separately pinned. Its
formal execution count is zero at this preregistration.

The written proofs below are part of the frozen public protocol. The verifier
is an audit of those proofs, not their logical source.

## Field 1: equation

### Fixed carrier and adjoint

Work over the rational vector space

```text
V = Q^4,
1 = (1,1,1,1)^T,
G = I_4 - (1/5) 1 1^T,
G^-1 = I_4 + 1 1^T.
```

For a rational matrix `A`,

```text
A^sharp = G^-1 A^T G.
```

The frozen effect pair is

```text
E_low  = (1/4) 1 1^T,
E_high = I_4 - E_low.
```

Then

```text
E_a^2 = E_a,
E_a^sharp = E_a,
E_low E_high = 0,
E_low + E_high = I_4.
```

`G` is positive definite. Indeed `span(1)` and `ker(sum)` are
`G`-orthogonal; `G` acts as `1/5` on `span(1)` and as the identity on
`ker(sum)`.

All statements below are over `Q`. No floating approximation, measured input,
continuum limit or external theorem is permitted.

### S1a. Raw single-branch fibre classification

Let `E` be a nonzero `G`-self-adjoint idempotent and

```text
F_E = {K in End_Q(V) : K^sharp K = E}.
```

Then

```text
F_E = {W E : W in O(G,Q)}.
```

Proof. If `x in ker(E)`, then

```text
<Kx,Kx>_G = <x,Ex>_G = 0,
```

so positive definiteness gives `Kx=0`. If `x,y in im(E)`, then

```text
<Kx,Ky>_G = <x,Ey>_G = <x,y>_G.
```

Thus `K` is zero on `ker(E)` and an isometric embedding on `im(E)`.
The rational extension lemma S2a below extends that isometry to
`W in O(G,Q)`, giving `K=WE`. Conversely `(WE)^sharp(WE)=E`.

### S1b. Ordered raw fibre

For the frozen pair the complete raw ordered fibre is

```text
{(W_low E_low, W_high E_high) : W_low,W_high in O(G,Q)}.
```

It is one orbit under the branchwise product action
`O(G,Q) x O(G,Q)`. No claim of one diagonal orbit is made.

### S1c. Complete diagonal-orbit classification by cross Gram

For an ordered family `K=(K_a)` define

```text
Gamma(K)_(ab) = K_a^sharp K_b.
```

For two admissible families `K,K'` with the same fixed diagonal effects,

```text
K' = W K for one common W in O(G,Q)
iff
Gamma(K') = Gamma(K).
```

The forward implication is immediate. For the converse define on
`S = span_a im(K_a)`

```text
phi(sum_a K_a v_a) = sum_a K'_a v_a.
```

The common `Gamma` gives

```text
||sum_a K_a v_a||_G^2
 = sum_(a,b) <v_a, Gamma_(ab) v_b>_G
 = ||sum_a K'_a v_a||_G^2.
```

Positive definiteness makes `phi` well defined, and polarization makes it an
isometry. S2a extends it to one `W in O(G,Q)`.

For two branches the diagonal blocks are already fixed, so the single cross
matrix

```text
C = K_low^sharp K_high
```

is a complete diagonal-orbit invariant. The attainable set is exactly

```text
{E_low O E_high : O in O(G,Q)}.
```

Every attainable `C` has rank at most one, image in `span(1)`, and annihilates
`span(1)` on the right. The layer `C=0` is the diagonal orbit of the Lueder
pair. This is geometric orbit bookkeeping only. Diagonal `O(G,Q)` action is
not declared a physical gauge.

### S1d. Physical post-state equivalence inside one effect fibre

For `K^sharp K=E` define the pure post-state on `v` by

```text
w_K(v) = <Kv,Kv>_G = <v,Ev>_G,
Post_K(v) = ZERO                              if w_K(v)=0,
Post_K(v) = Kv (Kv)^T G / w_K(v)             if w_K(v)>0.
```

For two branches `K,L` over the same nonzero effect `E`, define

```text
K ~_post L  iff  Post_K(v) = Post_L(v) for every v in V.
```

Then

```text
K ~_post L  iff  L = +K or L = -K.
```

Proof. On `im(E)`, both maps are injective isometries. Equality of the rank-one
normalized density operators says `Lv` and `Kv` span the same rational line
for every nonzero `v in im(E)`. Hence `L v = c(v) K v` with
`c(v)^2=1`. If the image has dimension at least two, linearity applied to two
independent vectors and their sum forces one common sign. In dimension one
there is already only one nonzero line and the equal-norm condition again gives
one sign. Both maps vanish on `ker(E)`. The converse is immediate.

Thus branchwise sign is physical post-state redundancy, but a general left
orthogonal transformation is not.

### S1e. Rational injection into physically different instruments at C=0

Freeze the three `G`-orthonormal sum-zero vectors

```text
r = ( 1, 1,-1,-1)/2,
f = ( 1,-1, 1,-1)/2,
g = ( 1,-1,-1, 1)/2.
```

They form an orthonormal basis of `im(E_high)=ker(sum)`. For every `t in Q`
put

```text
c_t = (1-t^2)/(1+t^2),
s_t = 2t/(1+t^2),
```

and define `R_t` by

```text
R_t r = c_t r + s_t f,
R_t f = -s_t r + c_t f,
R_t g = g,
R_t 1 = 1.
```

The identity

```text
(1-t^2)^2 + (2t)^2 = (1+t^2)^2
```

proves `R_t in O(G,Q)`. It preserves both frozen effect subspaces. Define

```text
K_low(t)  = E_low,
K_high(t) = R_t E_high.
```

Then for every `t in Q`

```text
K_low(t)^sharp K_low(t)   = E_low,
K_high(t)^sharp K_high(t) = E_high,
K_low(t)^sharp K_high(t)  = 0.
```

Therefore all effects, all branch weights and the diagonal-orbit invariant
`C` are identical for the whole family.

The family is injective modulo physical post-state equivalence. If `t != s`
and the high branches were physically equivalent, S1d would give

```text
R_t E_high = +/- R_s E_high.
```

The minus sign is impossible because both maps fix the nonzero vector `g`.
For the plus sign, equality on `r,f` gives equal rational circle coordinates.
For finite rational `t`, `c_t != -1` and

```text
t = s_t/(1+c_t).
```

Hence `R_t=R_s` implies `t=s`. Therefore

```text
Q injects into the physical post-state instrument classes
at fixed effects, fixed weights and C=0.
```

This strengthens an existence-of-infinitely-many statement to pairwise
inequivalence for every two distinct rational parameters.

### S2a. Rational reflection-extension lemma

Let `(W,B)` be a finite-dimensional positive definite rational bilinear space
and let `phi:A->B0` be a rational isometry between rational subspaces.
Then `phi` extends to an element of `O(B,Q)`.

Self-contained proof. Rational Gram-Schmidt gives a `B`-orthogonal basis
`a_1,...,a_k` of `A`; its images `b_i=phi(a_i)` are orthogonal with the same
norms. Inductively suppose an orthogonal map `O_(i-1)` already sends
`a_j` to `b_j` for `j<i`. Set

```text
x = O_(i-1) a_i,
y = b_i.
```

Both are orthogonal to the already fixed `b_j` and have equal norm. If `x=y`
do nothing. Otherwise set `z=x-y` and use the rational reflection

```text
H_z(v) = v - 2 <v,z>_B / <z,z>_B z.
```

Positive definiteness makes the denominator nonzero. Equal norms give
`H_z(x)=y`; orthogonality of `z` to prior `b_j` makes `H_z` fix all of them.
Thus `O_i=H_z O_(i-1)` advances the induction. The product is rational and
orthogonal and extends `phi`. No appeal to Witt extension is needed.

### S2b. Orthogonal-dilation surjectivity

Let the pointer carrier be a second copy `P=(Q^4,G)`. Freeze a rational
`G`-unit ready state `r` and two rational `G`-orthonormal pointer states
`e_low,e_high`. For any rational two-branch family satisfying

```text
K_low^sharp K_low + K_high^sharp K_high = I,
```

define

```text
J_K(v) = K_low v tensor e_low + K_high v tensor e_high.
```

Then

```text
<J_K(v),J_K(w)>_(G tensor G) = <v,w>_G.
```

So the map

```text
v tensor r  ->  J_K(v)
```

is a rational isometry between two four-dimensional subspaces of
`V tensor P`. By S2a it extends to a rational

```text
U_K in O(G tensor G,Q).
```

Pointer reduction of `U_K(v tensor r)` returns the original `K_low,K_high`.
Hence every complete rational two-branch instrument family has a rational
orthogonal dilation.

### S3. Dilation nonselection theorem

Within the unrestricted class of rational orthogonal couplings on the frozen
carrier and pointer type, existence of a dilation imposes no condition beyond

```text
sum_a K_a^sharp K_a = I.
```

Therefore existence of an orthogonal dilation is not an instrument-selection
principle. Combined with S1e, fixed effects and fixed occurrence weights leave
an injective rational family of physically different post-state dynamics.

This is a negative theorem about selection. It does not say that every more
restricted dynamical coupling class is nonselective.

### S3b. Target-controlled coupling circularity

Let `(E_a)` be any nonzero complete `G`-orthogonal projector family and let
`X_a` be pointer operators. Define

```text
U = sum_a E_a tensor X_a.
```

Then

```text
U^sharp U = I
iff
X_a^sharp X_a = I for every a.
```

If the ready state is `r` and the adapted pointer states are
`e_a=X_a r`, with pointer reduction onto those orthogonal slots, then

```text
U(v tensor r) = sum_a E_a v tensor e_a
```

and the reduced branch operators are exactly

```text
K_a = E_a.
```

Thus restricting admissible couplings to a form already controlled by the
target frozen projectors selects the Lueder representatives only because the
answer occurs in the input. Such a target-controlled form is forbidden as
evidence for an independent apparatus-selection theorem.

### S4. Positive square-root section

If

```text
K^sharp = K,
K >=_G 0,
K^sharp K = E,
```

where `E` is a `G`-self-adjoint idempotent, then

```text
K = E.
```

Proof. Self-adjointness gives `K^2=E`. On `ker(E)`,
`||Kx||_G^2=<x,K^2x>_G=0`, so `K=0`. On `im(E)`, `K^2=I` and the rational
decomposition into the `+1` and `-1` eigenspaces is explicit via
`(I+K)/2` and `(I-K)/2`. Positivity excludes every nonzero `-1` eigenvector.
So `K=I` on `im(E)` and zero on `ker(E)`, hence `K=E`.

This is a mathematical canonical section only. The probe does not adopt
`G`-positivity, minimal disturbance or any equivalent phrase as a physical
selection rule.

### S5. Occurrence identity

For every `K` with `K^sharp K=E` and every `v in V`,

```text
K^T G K = G E,
<Kv,Kv>_G
 = v^T K^T G K v
 = v^T G E v
 = Tr(E v v^T G).
```

Therefore every instrument in one effect fibre has exactly the same frozen
branch-weight pairing. The equality is global on `Q^4`; a finite census is not
the evidential basis.

This proves equality with the already frozen Born trace pairing. It does not
derive the physical interpretation of that pairing from nothing.

### S6. Explicit rational apparatus witness

For an exact audit witness use

```text
r = ( 1, 1,-1,-1)/2,
f = ( 1,-1, 1,-1)/2,
Pi_low  = r r^T G,
Pi_high = I - Pi_low.
```

Let `X` swap `r` and `f` and fix their `G`-orthogonal complement. Equivalently,
with `R_(x,y)=x y^T G`,

```text
X = I - R_(r,r) - R_(f,f) + R_(r,f) + R_(f,r).
```

Then

```text
X^sharp X = I,
X^2 = I,
Xr = f,
Xf = r.
```

The controlled witness

```text
U = E_low tensor I + E_high tensor X
```

satisfies

```text
U^sharp U = I,
U^2 = I,
```

and the complete pointer PVM `(Pi_low,Pi_high)` has no leakage on the prepared
image. Its reduction gives

```text
K_low = E_low,
K_high = E_high.
```

This witness is an exhibition only. By S3b it is not evidence that the
apparatus independently selected those operators.

## Field 2: code

Accepted verifier:

```text
probes/P-QDD-INSTRUMENT-NONSELECTION-1/verify.py
```

Requirements:

```text
Python standard library only
integers and Fraction only
no float, Decimal, complex approximation or external dataset
exact matrix arithmetic over Q
```

The verifier audits the frozen finite identities, the explicit four-dimensional
pointer construction, the Householder and permutation breakers, the rational
`R_t` family identities, the reflection-extension construction on an explicit
non-Lueder family, the occurrence identity and the positive-section controls.
The universal statements S1a-S5 rest on the written proofs above. No finite
sample is allowed to replace their quantifiers.

## Field 3: carrier or data

No external data.

```text
system carrier   (Q^4,G)
pointer carrier  a second copy (Q^4,G)
tensor carrier   Q^4 tensor Q^4 with Gram G tensor G
```

All displayed vectors and matrices are rational and frozen in this file.

## Field 4: systematics and completeness

There is no measurement systematic.

Completeness obligations:

```text
C1  Verify G^-1, the frozen effect pair and all adjoint identities exactly.
C2  Verify the explicit four-dimensional pointer PVM and controlled witness.
C3  Verify the occurrence identity as a matrix identity, not a 625-point basis.
C4  Verify an exact diagonal-orbit breaker with C != 0.
C5  Verify an exact diagonal-but-post-state-nontrivial breaker with C = 0.
C6  Verify the rational-circle polynomial identities and exact R_t witnesses.
C7  Verify the reflection formula and construct an exact 16-dimensional
    orthogonal dilation for one non-Lueder complete family.
C8  Verify the self-adjoint sign counterexample and the positive-root controls.
C9  Preserve the written proof of diagonal Gamma completeness; no finite orbit
    census substitutes for it.
C10 Preserve the written proof of rational reflection extension and dilation
    surjectivity; no finite family substitutes for it.
```

Any hidden input, floating tolerance, imported incubation transcript, target
controlled coupling presented as independent selection, or unnamed L4-to-L5 or
L5-to-L6 lift is STOP.

## Field 5: failure threshold and scientific routing

No tolerance exists.

```text
NONSELECTION-PASS
  Every frozen exact audit gate passes and S1a-S6 survive the written proof.

FIBRE-F
  An exact rational counterexample violates S1a, S1b or S1c.

POSTSTATE-F
  An exact rational counterexample violates S1d or the injectivity statement S1e.

DILATION-F
  An exact rational counterexample violates S2a, S2b or S3.

CIRCULARITY-F
  An exact rational counterexample violates S3b.

POSITIVE-SECTION-F
  An exact rational counterexample violates S4.

OCCURRENCE-F
  An exact rational counterexample violates S5.

STOP
  Authority, pin, verifier integrity, completeness, security, evidence or layer
  discipline fails.
```

The threshold and scope may not move after the immutable pin.

## Field 6: action layer

```text
L4 apparatus/support only.
```

No L5 realized-event stream is produced. No L6 measure is produced. The frozen
Born branch-weight pairing is only reproduced as an exact identity.

`SAMPLING NOT PROVIDED` is the only permitted sampling statement. This probe
contains no theorem `SAMPLING IMPOSSIBLE`.

## Scope firewall

This probe does not:

- close `QDD-INSTRUMENT-APPARATUS [O]`;
- select one physical instrument family;
- adopt `G`-positivity or minimal disturbance as a physical premise;
- infer instruments backward from effects;
- derive the frozen effect pair or Born pairing from `J`;
- fill a decoder-completion-contract field;
- create a realized event, sampling map, L5 stream or L6 measure;
- claim uniqueness of a restricted dynamical coupling class not classified here;
- use the target-controlled form as independent selection evidence;
- use the prior incubation run as formal evidence.

The two independent blockers that remain after a positive result are:

```text
O2  independent physical instrument selection
O1  realized event generation / sampling
```

## Formal sequence after the pin

1. Push this `PREREG.md` and the accepted `verify.py` on the claimed branch.
2. Read both files back from the public remote and record the immutable pin,
   SHA-256 and byte counts on issue 391.
3. Only then execute the accepted verifier for the first formal run.
4. Commit exact `EXPECTED.txt`, neutral `RUN.md`, and `RESULT.md` without
   changing the pinned preregistration or verifier.
5. Open one pull request changing only
   `probes/P-QDD-INSTRUMENT-NONSELECTION-1/`.
6. Require GitHub x86_64 and aarch64 jobs to reproduce the same committed
   `EXPECTED.txt` byte for byte.
7. A later separate reviewed Canon fold may register only the status and scope
   actually earned by this probe.
