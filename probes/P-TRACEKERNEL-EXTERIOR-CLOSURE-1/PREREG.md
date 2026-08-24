# P-TRACEKERNEL-EXTERIOR-CLOSURE-1 preregistration

Date: 2026-08-21

Author of record: A. M. Thorn

Status: preregistered protocol only. No scientific result is earned by this
file. The accepted `verify.py` has formal execution count zero. It may be
parsed, compiled, and inspected statically, but it may not be imported or
executed before this file and `verify.py` are committed together, pushed, and
read back byte for byte from the public remote.

Public claim lock: issue 481.

## Authority and pin base

```text
STATE:          ACTIVE
CANON:          Public Canon v57
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v57
CONTENT_COMMIT: 8e8b04abe4d3359942449533854ef1d142be70df
CANON_SHA256:   c96a2ef52c78d68ef8f04b582e4a17328e6a863b49664f29b1bd324171d802a8
CANON_BYTES:    295013
BASE_COMMIT:    6b8d27b2721b97c88c5b80b49592d6a755f35a0a
LAYER:          L1 exact arithmetic only
```

The probe changes exactly
`probes/P-TRACEKERNEL-EXTERIOR-CLOSURE-1/`. Canon, registry, frontier,
evidence, dependency, gate, release, and workflow files are excluded.

## Result exposure and chain of custody

This is result-exposed, proof-first work. The expected conclusions, the
`p=5` outcome, an explicit `sl_2` triple, the kinematical incompatibility,
and two exact negative witnesses were known before this formal probe was
drafted. They are not blind discoveries.

Frozen non-canonical source:

```text
commit:          8b8eb640a3ef260c4664d253f69398979afc926f
source PREREG:   1c0b33b0f95c2260ae0f6ea3e3c3f03af0e2a763cccff91269621aa529fb1a2d
source ADDENDUM: b5bddf9253052958ea3f817d863d59216490297b7aebb861c3a9af9663746e53
```

Independent non-canonical breaker package:

```text
result commit:   6cba68250b0298ed85b39fe3816c54e0b785c3e8
breaker pin:     fa5297b68652b18e2cb483e3900e146b210bce8f
breaker SHA256:  e23aeca91c019ac3250a15e91ab210e2ce1328070ad8aac707a8415fa36fb61c
stdout SHA256:   b91f268d46d98da1038f78bcba359df0d281359dfc7a9af134a6e0622212621d
route:           CONDITIONAL-PASS / L1 ONLY / NO PROMOTION
```

The author of this accepted verifier did not read or copy `break.py` or any
earlier positive implementation. The frozen statement, addendum, breaker
result, expected output, manifest, and a hand mathematical audit were read.
This provenance makes the implementation new, but it does not make the
result unexposed. The symbolic proofs below, rather than novelty, carry the
universal statements.

The `rho(2I_2)` witness and the invertible non-Jacobi product were supplied by
external review. The `8/480` count was already result-exposed. The verifier
must label these facts accordingly.

## Scope sentence

The unconditional object is the cyclotomic trace Gram for every prime `p`,
its mod-`p` trace-kernel carrier, and the first-derived nondegenerate residual
form. Separately, under the declared and unearned premise
`EXACT-HODGE-HOME-CLOSURE`, the probe proves that a nonzero home-carrier
closure can occur only at `p=5`; in that branch its metric-volume bracket is
`sl_2(F_5)` with the public `Phi` eigenspace split `1+2`.

The public architecture is not claimed to force the bridge premise.
`CURVATURE-OPERATOR-CANONICAL [O]` remains open. No binary-icosahedral `2I`
derivation, spinor, integral lift, physical, decoder, metrology, measure,
L2-to-L6, or extended `ALPHA-SEED` claim is made. This does not exclude the
separately labelled scalar-matrix control `A=2I_2` below.

## Field 1: equations and theorem proofs

### 1. Universal trace Gram

Let `p` be any prime, `zeta_p` a primitive `p`-th root, and let indices
`a,b` range from `1` to `p-1`. The complete nontrivial-root sum is

```text
sum_(k=1)^(p-1) zeta_p^(k(a-b)) = p-1  if a=b,
                                      -1  if a!=b.
```

Indeed, for `a=b` every summand is one. Otherwise `a-b` is nonzero modulo
`p`, so multiplication by `a-b` permutes the nonzero residues and the sum is
the sum of all nontrivial `p`-th roots, namely `-1`. Therefore, with
`n=p-1` and `J_n=11^T`,

```text
G_p = p I_n - J_n.
```

On the all-ones line its eigenvalue is `p-n=1`; on the rational trace-zero
hyperplane its eigenvalue is `p`. Hence `G_p/p` has normalized spectrum

```text
1/p once,  1 with multiplicity p-2.
```

This is an elementary theorem for every prime. The verifier's finite sweep
through `p=23` is an audit, not the source of the universal quantifier and
does not extend the registered finite-prime scope of `ALPHA-SEED` by registry
rewriting.

### 2. Canonical mod-p carrier and first residual form

Modulo `p`,

```text
G_p = -J_n,
W_p := rad(G_p mod p)
     = ker(sum:F_p^(p-1) -> F_p),
dim W_p = p-2.
```

The equality follows because `J_n x=(sum x)1` and `J_n` has rank one.
For `xbar,ybar in W_p`, choose integer lifts `x,y` whose coordinate sums
are `pr,ps` and define

```text
g_p(xbar,ybar) := (x^T G_p y)/p mod p.
```

The numerator is divisible by `p`, and

```text
(x^T G_p y)/p = x.y - p r s = x.y mod p.
```

Changing either lift by `p` times an integer vector changes the displayed
integer by a multiple of `p`, so the residue is lift-independent. Moreover,
for the ambient dot product

```text
W_p^perp = <1>,
sum(1)=p-1=-1 mod p,
W_p intersect W_p^perp = 0.
```

Thus `g_p` is nondegenerate on `W_p` for every prime, including the
zero-dimensional `p=2` case. This establishes an unconditional L1 theorem.

### 3. EXACT-HODGE-HOME-CLOSURE, declared and not earned

The bridge is deliberately type-correct before any dimension is selected.
It has two stages.

First, exact home closure says that the complete alternating spatial
commutator data return to precisely the same carrier by a bijection

```text
beta: Lambda^2 W_p -> W_p,
```

with no projection, quotient, proper subspace, auxiliary carrier, remainder,
or unnamed change of degree.

Only after the dimension equation selects a nonzero three-dimensional branch
does the premise further require the home map to be the metric-volume map:
for a chosen nonzero `omega in Lambda^3 W_p^*`,

```text
g_p(beta_omega(x wedge y),z)=omega(x,y,z).
```

This 3-form formula is not used dimension-independently. At `p=2` the closure
is instead the unique empty bijection `0 -> 0`, treated separately and
vacuously; no nonzero volume form or nonzero bracket is asserted there.

Nothing in current public dependencies derives either stage of this premise.
Its public forcing status remains `[O]`.

### 4. Conditional dimension theorem

Put `m=dim W_p=p-2`. A home-carrier bijection requires

```text
dim Lambda^2 W_p = dim W_p,
m(m-1)/2=m,
m(m-3)=0.
```

Since `m` is nonnegative, `m=0` or `m=3`, hence `p=2` or `p=5`. The first is
the empty case just separated. Therefore `p=5` is the only nonzero solution.
This is a theorem conditional on `EXACT-HODGE-HOME-CLOSURE`, not evidence that
the premise holds.

### 5. The p=5 metric-volume bracket

Use the difference basis

```text
b1=(1,-1,0,0),
b2=(0,1,-1,0),
b3=(0,0,1,-1)
```

of `W_5`. The residual Gram matrix and inverse over `F_5` are

```text
B     = [[2,4,0], [4,2,4], [0,4,2]],  det B=4,
B^-1  = [[2,3,4], [3,1,3], [4,3,2]].
```

Normalize `omega(b1,b2,b3)=1`. In difference coordinates the bracket is

```text
beta(x,y)=B^-1 (x cross y).
```

Both contraction by the nonzero 3-form and the identification by
nondegenerate `B` are isomorphisms, so `beta:Lambda^2 W_5 -> W_5` is
bijective. The accepted verifier checks its wedge determinant `4`, all 125
states, all 15625 ordered pairs, and all 1953125 ordered Jacobi triples.

The theorem proof of Jacobi and the Lie-algebra identification is shorter.
Put

```text
h=(1,0,1),  e=(1,4,3),  f=(3,4,1).
```

Direct substitution into `B^-1(x cross y)` gives

```text
[h,e]=2e,  [h,f]=-2f,  [e,f]=h,
det[h e f]=4 != 0.
```

Thus `h,e,f` form a basis and satisfy the defining relations of
`sl_2(F_5)`, under

```text
h -> [[1,0],[0,-1]],
e -> [[0,1],[0, 0]],
f -> [[0,0],[1, 0]].
```

Matrix commutators satisfy Jacobi, so this basis map is an exact Lie-algebra
isomorphism. The exhaustive Jacobi census is a redundant audit of the written
proof, not the sole reason for a theorem ceiling.

If `omega` is replaced by `c omega`, then the bracket is multiplied by
`c`. The direction of the scalar isomorphism is frozen explicitly:

```text
x -> c^-1 x maps (W_5,beta_omega) to (W_5,beta_(c omega)).
```

Thus the isomorphism class is independent of the nonzero volume scaling.

### 6. Phi grading

Let `Phi` be the ambient coordinate permutation

```text
(x0,x1,x2,x3) -> (x2,x3,x0,x1).
```

It preserves coordinate sum and dot product. Its ambient determinant is one,
and it fixes the complementary all-ones line, so its determinant on `W_5` is
also one. It therefore preserves `B`, every chosen 3-volume, and the bracket.
Its eigenspaces are

```text
W_+ = <(1,-1,1,-1)>,                 dim 1,
W_- = {(u,v,-u,-v):u,v in F_5},      dim 2.
```

In difference coordinates `Phi` fixes `h` and negates `e,f`. The displayed
`sl_2` relations therefore prove

```text
[W_+,W_+]=0,
[W_+,W_-]=W_- onto,
[W_-,W_-]=W_+ onto.
```

This is the bracket grading along the existing public dictionary split
`1+2`. It does not promote or widen `COLOR-SPLIT-12 [D]`.

### 7. Exact negative controls

At `p=2`, `W_2=0`; this is not the unrelated nonzero `F_2^4` carrier. On the
plane alone, `dim Lambda^2 W_-=1`, not `2`, so there is no home-carrier
bijection on `W_-`.

An unnamed isomorphism `Lambda^2 W -> W` is strictly weaker than the
metric-volume premise. On a basis `u1,u2,u3`, define

```text
[u2,u3]=u1,
[u3,u1]=u1+u2,
[u1,u2]=u3.
```

Its wedge matrix is

```text
[[1,1,0], [0,1,0], [0,0,1]],  determinant 1,
```

but its Jacobi sum on `(u1,u2,u3)` is `-u3`. This characteristic-free exact
counterexample was supplied by external review and is labelled as such. It,
not a random sample, proves the weakness of an unnamed bijection.

No random-product census is an accepted theorem ingredient. The public
verifier uses no random module and reports `SAMPLING NOT PROVIDED`.

### 8. Automorphisms and the exact 8-of-480 boundary

In the displayed `h,e,f` basis, direct multiplication of the three adjoint
matrices gives the Killing matrix, while changing basis in the residual form
gives

```text
K = [[3,0,0], [0,0,4], [0,4,0]],
g = [[4,0,0], [0,0,2], [0,2,0]],
K = 2g,  det K=2 != 0  over F_5.
```

Every bracket automorphism preserves `K`. Taking determinants in

```text
A beta = beta Lambda^2 A
```

forces `det A=(det A)^2`, hence `det A=1`; thus `Aut` embeds in
`SO_3(F_5)`.

The conjugation action of `GL_2(F_5)` on traceless matrices has only scalar
matrices in its kernel, because a matrix commuting with both `e` and `f` is
scalar. It therefore embeds

```text
PGL_2(F_5) -> Aut,   |PGL_2(F_5)|=((25-1)(25-5))/4=120.
```

For completeness, the matching upper bound on `SO_3` is elementary rather
than imported as an order formula. Here
`K(xh+ye+zf,xh+ye+zf)=3(x^2+yz)`. It has `5^2-1=24` nonzero isotropic
vectors. The `PGL_2` subgroup is transitive on them: the centralizer of the
fixed vector `e` in `PGL_2` has the five classes represented by
`[[1,t],[0,1]]`, so its orbit has `120/5=24` elements. Direct preservation of
`K`, determinant one, and the condition of fixing `e` leave exactly the same
five adjoint matrices

```text
U_t = [[1,0,t], [-2t,1,-t^2], [0,0,1]],  t in F_5.
```

Thus the full `SO_3` stabilizer has order five and
`|SO_3(F_5)|=24*5=120`. The two inclusions and equal orders now give

```text
Aut(sl_2(F_5)) = SO_3(F_5) = PGL_2(F_5),  order 120.
```

The verifier independently enumerates both the relation-preserving images of
the `h,e,f` basis and the special orthogonal matrices and checks equality of
the two 120-element sets.

Now take the public block action relative to `W_+ directsum W_-`:

```text
A=[[a,b],[c,d]],  delta=det A,
rho_A(h)=delta^-1 h,
rho_A|(W_-)=A in the ordered basis (e,f).
```

Imposing the three `sl_2` relations after applying `rho_A` gives symbolically

```text
a(delta^-1-1)=d(delta^-1-1)=0,
b(delta^-1+1)=c(delta^-1+1)=0,
delta^2=1.
```

If `delta=1`, the matrix is diagonal with `ad=1`, giving four choices. If
`delta=-1`, it is antidiagonal with `bc=1`, again four choices. Exactly eight
of the 480 public block maps preserve the bracket, namely the torus normalizer.
The central case `A=2I_2` is already an exact mismatch: `rho` scales `h` by
`4` and the plane by `2`.

The public dependency table does not require the spatial commutator to be
equivariant under the full 480-element kinematical group. Thus the calculation
arms F2 but does not fire it. Its public interpretation remains relative to
`COLOR-KINEMATICAL-GL2 [D]`; no dictionary promotion occurs. Substituting the
120-element `(det A)^-1 Sym^2(A)` image would be a new bridge, not a
reinterpretation of the faithful public block action.

## Field 2: accepted code

Accepted exact file:

```text
probes/P-TRACEKERNEL-EXTERIOR-CLOSURE-1/verify.py
```

Requirements:

```text
command: python3 probes/P-TRACEKERNEL-EXTERIOR-CLOSURE-1/verify.py
environment: LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
Python standard library only
integer and finite-field arithmetic only
no float, Fraction approximation, Decimal, complex approximation, random,
network, subprocess, external data, predecessor import, filesystem read, or
filesystem write
zero arguments
deterministic stdout with final LF
empty stderr
accepted formal process from repository root on Linux or a Linux-compatible
environment
```

The code is a fresh implementation and does not import any predecessor. It
audits finite primes `2,3,5,7,11,13,17,19,23`, but the written proofs carry
the universal quantifier.

## Field 3: carriers and exact data

```text
G_p over Z:             p I_(p-1)-J_(p-1)
W_p over F_p:           kernel of coordinate sum
audit basis:            e_i-e_(i+1), i=1,...,p-2
residual form:          dot product restricted to W_p
complete W_5:           all 125 states
complete ordered pairs: 15625
complete Jacobi triples:1953125
kinematical audit:      all 480 GL_2(F_5) elements
automorphism audit:     exact complete finite sets
external data:          none
sampling:               not provided
```

## Field 4: completeness and systematics

No tolerance. Nine executable exact gate groups and one frozen manual/static
base audit:

```text
G1  closed Gram formula, rational eigenspaces, mod-p rank and radical, and
    residual nondegeneracy on the finite prime audit set;
G2  lift independence on basis generators and every single-coordinate +p
    generator shift in either lift;
G3  type-correct dimension equation, p=2 empty branch, p=5 only nonzero;
G4  p=5 B, B^-1, wedge bijection, alternation, and complete Jacobi audit;
G5  explicit sl_2 basis and Phi grading on complete eigenspaces;
G6  all four nonzero volume rescalings with the directed isomorphism;
G7  empty-carrier, plane-dimension, and exact non-Jacobi controls;
G8  Aut=SO_3 count 120 by two complete finite descriptions, with the written
    proof identifying the same group with PGL_2;
G9  public GL_2 image 480, compatible set 8, symbolic class shape, central
    survivors {1,4}, and alternative Sym^2 image 120;
M1  manual/static only, not evaluated by the no-filesystem verifier:
    result exposure, the public dependency table and F2-not-fired boundary,
    status, layer, and scope firewalls.
```

The seeded historical and independent-breaker samples are provenance only.
They are not rerun, compared, averaged, or used in a threshold.

## Field 5: failure thresholds and routing

```text
CONDITIONAL-PASS
  G1-G9 pass and M1 is separately confirmed against the pinned public base.
  The universal carrier theorem is unconditional. The dimension, p=5 Lie
  algebra, and Phi grading conclusions remain explicitly conditional on
  EXACT-HODGE-HOME-CLOSURE. The premise itself remains unearned.

MISMATCH
  Any exact defect in the Gram identity, radical, derived form, lift
  independence, dimension equation, B or B^-1, wedge determinant, sl_2
  relations, Jacobi identity, Phi grading, volume rescaling, negative controls,
  automorphism classification, or 8-of-480 classification.

F2-FIRED
  Only if a public dependency is exhibited that requires full faithful
  GL_2(F_5) equivariance of the same spatial commutator while retaining the
  frozen block action and Hodge bracket. No such dependency is presently
  supplied, so this route is not expected and may not be inferred from the
  order mismatch alone.

STOP
  Any claim that the public architecture forces the bridge; any use of
  CURVATURE-OPERATOR-CANONICAL [O] as closed; any L1-to-L2 lift; any 2I,
  binary-icosahedral 2I derivation, spinor, integral-lift, physical, decoder,
  measure, or metrology claim; any
  widening of ALPHA-SEED; any imported predecessor execution; any post-pin
  mutation of PREREG.md or verify.py; or any moved threshold.
```

Fired falsifiers and mismatches are archived, never erased. A falsified route
may still merge with the exact failure recorded.

## Field 6: layer and honest status ceiling

```text
LAYER   L1 exact finite algebra only
ACTION  L1 only; no lift is claimed
```

Maximum later candidate conclusions after a clean formal run and required
two-architecture byte-identity gate:

```text
[candidate-T]
  For every prime p, the trace Gram gives the canonical trace-kernel carrier
  W_p of dimension p-2 and its nondegenerate first-derived residual form.

[candidate-T, conditional on EXACT-HODGE-HOME-CLOSURE]
  A nonzero home-carrier closure exists only at p=5.

[candidate-T, conditional on EXACT-HODGE-HOME-CLOSURE]
  At p=5 the metric-volume bracket is sl_2(F_5) with the Phi grading 1+2.

[candidate-T, pure finite-field boundary]
  Aut=120 and exactly 8 of the 480 public block maps preserve the bracket.
  The interpretation remains relative to the existing [D] dictionary row.

[O]
  Public architecture does not force EXACT-HODGE-HOME-CLOSURE.
```

The probe itself does not edit the Canon and does not assign public registry
status. Any Canon or registry treatment is a later sealed fold.

## Formal order

1. Commit and push this file and the new `verify.py` together.
2. Read both files back from the public remote at the exact pin; record SHA-256,
   byte count, line count, final LF, and Git blob.
3. Execute the pinned verifier exactly once from the repository root on Linux
   or a Linux-compatible environment under the frozen deterministic environment.
4. Add `EXPECTED.txt`, `RUN.md`, and `RESULT.md` without changing either pinned
   file.
5. Open one probe-only pull request and require byte identity on x86_64 and
   aarch64 plus aggregate `check` and manual security review.
6. Preserve any valid or falsified route with a merge commit, never squash,
   rebase, amend, or force-push after the pin.
7. Treat Canon, registry, frontier, evidence, dependency, gate, tag, and release
   changes only in a separate sealed public fold.
