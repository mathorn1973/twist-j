# Analytic audit of the native U field-image gate

PUBLIC / NON-CANONICAL / L1 / proposed exact proof.

This is a proposed proof written before the audit's first scientific
execution. The numerical targets and witness statements in the author's
preregistration were exposed to the audit. It is not a blind prediction.
The proof author is a helper within the single claimed RA audit, not an
additional independent reviewer. Only the frozen author preregistration
and the admitted canonical definitions and theorems were used. No author
proof, implementation, expected transcript, run report, or result was read.

Authority used for the admitted mathematics: Public Canon v102 at
`a632c6a162dc87e60104d7a478e7650a6d5c4a1b`, content commit
`b04e22dd3ed8e4240cff347364f24670d4183a4d`.

The canonical inputs are `DEF-NATIVE-WORD-CURVATURE-CLASS`,
`KERNEL-Z6-SYNCHRONIZATION`, `U-NATIVE-INVARIANT-AND-NOWRITE`, and shared
proof 2 of `FIELD-CHAIN-FIRST-WORK` / `DEF-FIELD-WORK-RECORD-CHAIN`.
The claims below keep the scope of those inputs. Integer field matrices
remain the selected field architecture; they are not derived from native U.

## 1. Notation and full native premises (F1)

All checkpoint calculations in this document are in `F5`. Integer matrix
identities and the integer field inverse in section 2 are over `Z` unless
explicitly reduced modulo five. Write

```text
x=(u,v,u',v',q,r),       p=(u,v,u',v'),
z=u+v+u'+v'+q+r,        X_s={x:z=s},
X14=X_1 union X_4,
h(p)=(v+2u,v'+2u'),     J2(alpha,beta)=(beta,alpha),
G={x:h(p)=0},           G14=G intersect X14,
K(p)=h(a p)=(u+2v,u'+2v'),
R(r)=(r,-r).
```

Here `J2` is exactly the two-coordinate swap specified by the gate
contract. It is not the algebraic `J=1+j^2` or an identification with a
four-coordinate integer operator. The symbol `K(p)` in this proof denotes only the displayed
two-coordinate readout, not a curvature operator.

The five admitted checkpoint generators are

```text
a x=(v,u,v',u',q,r),
b x=(-u',-v',-u,-v,-q,-r),
c x=(2-u',1-v'+r,2-u,1-v-r,1-q,-r),
d x=(2-u,1-v,3-u',4-v',1-q,1-r),
e x=(2-u,1-v,3-u',4-v',2-q,1-r).
```

Each is an involution on the entire six-coordinate carrier. For `a` this
is a pair of swaps, and for `b` it is a negative pair swap together with
two sign changes. For `c`, a second application gives, for example,

```text
2-(2-u)=u,
1-(1-v-r)+(-r)=v,
1-(1-v'+r)-(-r)=v',
1-(1-q)=q,
-(-r)=r.
```

The primed first coordinate is restored by the same displayed first
identity with `u'` in place of `u`. For `d` and `e`, every coordinate is
of the form `constant - coordinate`. This proves involutivity without
restricting to a synchronized sheet or a gated point.

Summing the six output coordinates gives the trace and fibre-coordinate
laws

| Generator | Next trace | Next `(q,r)` |
| --- | --- | --- |
| `a` | `z` | `(q,r)` |
| `b` | `-z` | `(-q,-r)` |
| `c` | `2-z` | `(1-q,-r)` |
| `d` | `2-z` | `(1-q,1-r)` |
| `e` | `3-z` | `(2-q,1-r)` |

For instance, the two piston terms involving `r` in `c` cancel each
other; the last coordinate still contributes `-r`. Its constant trace
term is `2+1+2+1+1=7=2` in `F5`.

Every sheet has `5^5=3125` checkpoints: choose the four piston coordinates
and `r`, then solve for `q`. The complete carrier therefore has `15625`
points.

The selector is `T_t x=g_(z+2t mod 5) x`, with indices `0,1,2,3,4`
denoting `a,b,c,d,e`. Its trace table follows directly from the preceding
five formulas:

| Control bit | Input sheet `0` | `1` | `2` | `3` | `4` |
| --- | --- | --- | --- | --- | --- |
| `t=0` | `0` | `4` | `0` | `4` | `4` |
| `t=1` | `2` | `1` | `1` | `3` | `1` |

On each one input sheet the chosen generator is fixed. Its involution
therefore restricts to a bijection from that sheet to the displayed
target sheet. The target is all of that sheet: invertibility gives
injectivity and the two finite sheets have the same cardinality.

The fixed points of the individual generators are obtained by solving
their coordinate equations:

| Generator | Complete fixed-point conditions | Count |
| --- | --- | --- |
| `a` | `u=v`, `u'=v'`, with `q,r` free | `625` |
| `b` | `u'=-u`, `v'=-v`, `q=r=0` | `25` |
| `c` | `u+u'=2`, `v+v'=1`, `q=3`, `r=0` | `25` |
| `d` | `(u,v,u',v',q,r)=(1,3,4,2,3,3)` | `1` |
| `e` | `(u,v,u',v',q,r)=(1,3,4,2,1,3)` | `1` |

Division by two here means multiplication by `3` in `F5`. The fixed
point of `d` has trace `1`, and that of `e` has trace `4`; both have
`h=0`. Every fixed point of `b` has trace zero.

Finally, the binary digit parities of `0,1,2` are `0,1,1`. Applying those
three rows of the trace table sends every starting trace to `1`:

```text
0 -> 0 -> 2 -> 1,
1 -> 4 -> 1 -> 1,
2 -> 0 -> 2 -> 1,
3 -> 4 -> 1 -> 1,
4 -> 4 -> 1 -> 1.
```

For `z` in `{1,4}`, either control bit sends the trace to
`4+2t mod 5`. These are the inherited synchronization premises, not a
new synchronization theorem.

## 2. Exact field algebra and the complete image (F2)

In this section write the integer field coordinate as `y=(a,b,c,d)`.
These four letters denote coordinates, not native generators. The admitted
field matrices, unchanged, are

```text
A_f=[[1,0,1,0],[0,1,0,1],[-2,1,-1,1],[1,-3,1,-2]],
B_f=[[4,-2,2,-1],[-2,6,-1,3],[2,-1,2,0],[-1,3,0,2]],
L=[[1,-3,-1,-2],[-3,4,-2,1],[0,5,1,2],[5,-5,2,-1]],
Vinv=[[1,2,1,2],[2,-1,2,-1],[0,-5,1,-3],[-5,5,-3,4]],
Vh=[[1,1,1,1],[2,1,2,1],[0,-1,1,0],[-5,-2,-3,-1]],
H(y)=y^t B_f y/2.
```

The canonical integral conjugacy certificate is

```text
Jcyc=[[0,1,0,0],[0,0,1,-1],[1,-1,0,-1],[0,1,-2,1]],
Zcyc=[[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]],
det Jcyc=-1,       A_f Jcyc=Jcyc Zcyc.
```

`Zcyc` is multiplication by `t` in
`Z[t]/(Phi5(t))`, where `Phi5(t)=1+t+t^2+t^3+t^4`. Consequently
`Phi5(A_f)=0` and `A_f^5=I`.

Set `P(t)=(1-t)(1-t^2)=1-t-t^2+t^3`. The displayed field matrix `L`
is `P(A_f)`, so it commutes with `A_f`. The exact polynomial identity

```text
P(t)^2-5t^3=(t^2-3t+1) Phi5(t)
```

then gives `L^2=5 A_f^3`. The displayed matrix `Vinv` is `A_f^2 L`, as
in the canonical certificate. Therefore

```text
Vinv L=L Vinv=A_f^2 L^2=5 A_f^5=5I.
```

The quadratic identity must use the energy adjoint. The canonical field
isometry is `A_f^t B_f A_f=B_f`. Thus the adjoint for the bilinear form
with Gram matrix `B_f` satisfies `A_f^*=A_f^-1`. Reversing the order of
the factors under the adjoint gives

```text
L^*=(I-A_f^-2)(I-A_f^-1)
   =A_f^-3 (I-A_f^2)(I-A_f)
   =A_f^2 L
   =Vinv.
```

It follows that

```text
L^t B_f L=B_f L^* L=5B_f,
H(Lx)=5H(x).
```

This does not state `L^t=Vinv` in the ordinary Euclidean inner product.

For the complete integer image use the admitted unimodular HNF
certificate itself:

```text
det Vh=1,
L Vh=Q,
Q=[[5,3,0,0],[0,1,0,0],[0,0,5,3],[0,0,0,1]].
```

Since `Vh Z^4=Z^4`, the integer images of `L` and `Q` agree. The latter
image consists exactly of

```text
(5alpha+3beta, beta, 5gamma+3delta, delta),
alpha,beta,gamma,delta in Z.
```

Hence

```text
y in L Z^4
iff a-3b and c-3d are divisible by 5
iff a+2b=c+2d=0 mod 5.
```

The sufficiency is constructive: take
`alpha=(a-3b)/5`, `beta=b`, `gamma=(c-3d)/5`, `delta=d` and then
precompose with `Vh`. Also
`det L=det Q/det Vh=25`.

Let

```text
C={y in F5^4:a+2b=0, c+2d=0}.
```

Reducing `Q` modulo five gives `(3beta,beta,3delta,delta)`. There are
exactly `25` such outputs and exactly `25` choices of `(alpha,gamma)`
over each. Because `Vh` is invertible modulo five, `L mod 5` has exactly
this image and exactly these preimage multiplicities over all `625`
residues. This proves the full residue-image statement, not merely a
necessary congruence.

For an independent reading of the admission congruence, put
`A=a+2b`, `C0=c+2d`. Reduction of the displayed `Vinv` gives

```text
Vinv y=(A+C0, 2(A+C0), C0, 2C0) mod 5.
```

Thus `Vinv y=0 mod 5` if and only if `y mod 5` belongs to `C`.
For every integer representative satisfying those two congruences,
`x=Vinv y/5` is integral and

```text
Lx=(L Vinv)y/5=y.
```

Uniqueness follows from the invertibility of `L` over `Q`. The formula
works for every integer representative in the admitted residue class,
not only for representatives with coordinates in `{0,1,2,3,4}`.

## 3. Comparison map and all generator gate laws (F3, F4)

The comparison map is

```text
W(u,v,u',v')=(v,u,v',u').
```

It is the piston action of the actual native generator `a`, and
`W^2=I`. Its field-image congruences are precisely

```text
(W p)_0+2(W p)_1=v+2u=h(p)_1,
(W p)_2+2(W p)_3=v'+2u'=h(p)_2.
```

Consequently `h(p)=0` if and only if `W p` belongs to `C`. Invertibility
of `W` proves that it maps `ker h` bijectively onto `C`; both sets have
`25` points. Equivalently, `v=3u` and `v'=3u'` parametrize `ker h`.

The comparison is not an energy isometry. For the first coordinate vector
`e0=(1,0,0,0)`, the integer quadratic form gives

```text
H(e0)=B_f[0,0]/2=2,
H(W e0)=H((0,1,0,0))=B_f[1,1]/2=3.
```

No conclusion about an energy-preserving identification follows from
the equality of the residue gates.

Each gated piston permits `25` choices of `(q,r)`, so `|G|=625`.
For any prescribed trace `s`, each gated piston and each choice of `r`
determines exactly one `q`. Hence `|G intersect X_s|=125` and
`|G14|=250`.

Now compute the action on `h` directly from all six-coordinate
generators. The complete laws are

```text
h(a x)=(u+2v,u'+2v')=K(p)=2h(p)+2(u,u'),
h(b x)=-J2 h(p),
h(c x)=-J2 h(p)+(r,-r),
h(d x)=-h(p),
h(e x)=-h(p).
```

For `c`, the first component is

```text
(1-v'+r)+2(2-u')=-(v'+2u')+r,
```

and the primed component is `-(v+2u)-r`. For `d` and `e`, the two
constant piston combinations are `1+2*2=5=0` and
`4+2*3=10=0`. This accounts for every possible input, including the
unsynchronized sheets and nonzero gate values.

There is no function of `h` alone giving the `a` action. On each piston
pair the map to its two readouts is

```text
(u,v) -> (2u+v,u+2v),
matrix [[2,1],[1,2]], determinant 3 in F5,
inverse [[4,3],[3,4]].
```

The primed pair has the identical invertible map. Thus
`p -> (h(p),K(p))` is a bijection of the `625` pistons with `F5^4`.
In particular, a fixed `h` allows every possible `K`. The preregistered
pair is explicit:

```text
x=(0,0,0,0,0,0),          h(x)=(0,0),  h(a x)=(0,0),
x'=(1,3,0,0,0,0),        h(x')=(0,0), h(a x')=(2,0).
```

This rules out a closed `h`-only `a` law even on the zero gate.

For a point initially in `G`, the exact one-generator retention counts
are now immediate. Under `a`, `K=2(u,u')`, so retention requires
`u=u'=0`; the gate equations then also force `v=v'=0`. There are exactly
`25` such checkpoints, with zero piston and arbitrary `q,r`. Under `c`,
retention requires `R(r)=0`, or exactly `r=0`, leaving `25*5=125`
checkpoints. Under each of `b,d,e`, the induced map on `h` is invertible
and fixes zero. Each therefore maps `G` into `G` and its complement into
its complement. Involutivity in fact makes these bijections on both
subsets.

## 4. The complete selector table (F5)

The table below is derived by substituting `i=z+2t mod 5` into the five
trace and gate laws. `h`, `K`, and `r` in its last column all refer to
the input checkpoint. In particular, `K` retains the piston information
needed for the `a` rows.

| Input `z` | `t` | Selected index | Generator | Next trace | Next `h` |
| --- | --- | --- | --- | --- | --- |
| `0` | `0` | `0` | `a` | `0` | `K` |
| `1` | `0` | `1` | `b` | `4` | `-J2h` |
| `2` | `0` | `2` | `c` | `0` | `-J2h+R(r)` |
| `3` | `0` | `3` | `d` | `4` | `-h` |
| `4` | `0` | `4` | `e` | `4` | `-h` |
| `0` | `1` | `2` | `c` | `2` | `-J2h+R(r)` |
| `1` | `1` | `3` | `d` | `1` | `-h` |
| `2` | `1` | `4` | `e` | `1` | `-h` |
| `3` | `1` | `0` | `a` | `3` | `K` |
| `4` | `1` | `1` | `b` | `1` | `-J2h` |

The five sheets partition the full carrier, and the two bits give
exactly these ten cases. Thus the table covers every one of the `31250`
checkpoint-bit pairs. It assumes no closed gate law beyond the laws
already derived from the actual generators.

## 5. Synchronized induction and fixation (F6)

Restricting the table to `X14` leaves exactly four cases:

| Input trace | Bit | Generator | Output trace | Gate update |
| --- | --- | --- | --- | --- |
| `1` | `0` | `b` | `4` | `-J2h` |
| `4` | `0` | `e` | `4` | `-h` |
| `1` | `1` | `d` | `1` | `-h` |
| `4` | `1` | `b` | `1` | `-J2h` |

These cover `6250*2=12500` pairs. Every output stays in `X14`, and
zero as well as nonzero gate values are preserved because `-I` and
`-J2` are invertible. Thus `G14` and `X14` minus `G14` are invariant
subsets under either allowed one-step choice, in the forward sense.

For a fixed bit, both input sheets map bijectively to the same target
sheet `X_(4+2t)`. The corresponding generator also maps the entire zero
gate bijectively to itself. Its restriction is therefore a bijection

```text
G intersect X_s -> G intersect X_(4+2t),   s in {1,4}.
```

The two sources are disjoint. Hence

```text
T_t(G14)=G intersect X_(4+2t),
```

with exactly two preimages for each of the `125` output points. This is
an image statement with its full multiplicity, not pointwise fixation.

The actual all-time conclusion follows by induction. Let the control
sequence after a synchronized checkpoint be any sequence of bits. The
base is membership in `X14`. At each step the four-case table keeps the
next point in `X14` and multiplies its gate vector by either `-I` or
`-J2`. These two matrices commute, both square to `I`, and generate
exactly a subgroup of

```text
{I,-I,J2,-J2}.
```

By induction, at every later time the gate vector belongs to the orbit
of its initial synchronized value under these four matrices. Since all
four are invertible,

```text
h_later=0 iff h_at_the_synchronized_base=0.
```

This is a proof for every later integer time. It does not infer an
infinite statement from a finite trajectory. For the actual counter-zero
driver, section 1 supplies a synchronized base at `n=3` for every initial
checkpoint. Thus for every `n>=3`,

```text
x_n in X14,
h_n in {h_3,-h_3,J2h_3,-J2h_3},
h_n=0 iff h_3=0.
```

For fixation, at `t=0` the only possible generators on `X14` are `b`
on `X_1` and `e` on `X_4`. A fixed point of `b` has trace zero, so it
contributes none. The single fixed point is
`(1,3,4,2,1,3)`, the fixed point of `e`. At `t=1` the corresponding
argument leaves only the fixed point of `d`, namely
`(1,3,4,2,3,3)`. Both lie in `G14`. Each `T_t` therefore moves exactly
`250-1=249` points of `G14`, despite preserving membership in that
gate. No assertion that the gated checkpoints are frozen is compatible
with these counts.

## 6. Relation to the inherited V record (F7)

Use the canonical synchronized readout, indexed here from one:

```text
V(x)=(V1,V2,V3,V4)
    =(u+u',v+v',chi(z)(u-u'-2),chi(z)(v-v'-1)),
chi(1)=1, chi(4)=-1.
```

It is defined only on `X14`. Let

```text
S_p=(u+u',v+v'),
D_p=(u-u'-2,v-v'-1).
```

Under `b`, `S_p` becomes `-S_p`, while `D_p` remains `D_p`. The trace
switches between `1` and `4`, so `chi` changes sign. Consequently
`V(bx)=-V(x)` on the relevant sheets. Under `d` or `e`, the piston
coordinate sums and shifted differences both become their negatives.
For example,

```text
(2-u)-(3-u')-2=-(u-u'-2) mod 5,
(1-v)-(4-v')-1=-(v-v'-1) mod 5.
```

In the selected cases, `d` acts on `X_1` and retains that trace, while
`e` acts on `X_4` and retains that trace. Thus `chi` is unchanged and
again `V(next)=-V(x)`. These four cases prove the inherited update law
on all of `X14` for both bits.

Write `h=(h1,h2)`. Its sum and difference satisfy

```text
h1+h2=2V1+V2,
chi(z)(h1-h2)=2V3+V4.
```

The constant in the second equality cancels because `2*2+1=5=0` in
`F5`. Since `2` and `chi(z)` are invertible, `h1=h2=0` is equivalent
to the two equations

```text
2V1+V2=0,       2V3+V4=0.
```

Hence, for the two-dimensional subspace

```text
S={v in F5^4:2v1+v2=0, 2v3+v4=0},
```

the exact relation is `G14=V^-1(S)`.

The multiplicity of `V` also has an explicit inverse. Fix any
`(V1,V2,V3,V4)` and choose one trace `z` in `{1,4}`. The piston is then
uniquely determined by

```text
u =(V1+chi(z)V3+2)/2,
u'=(V1-chi(z)V3-2)/2,
v =(V2+chi(z)V4+1)/2,
v'=(V2-chi(z)V4-1)/2.
```

Its coordinate sum is `V1+V2`. Choose any of the five possible `r`, and
set `q=z-V1-V2-r`. This supplies exactly five preimages at each of the
two traces, hence exactly ten preimages of every one of the `625`
possible `V` values in `X14`.

The sign record is `R_V(x)={V(x),-V(x)}`. The subspace `S` has `25`
vectors, is stable under sign, and has exactly one self-negative vector,
zero. Therefore it comprises one singleton sign class and twelve
two-element sign classes. Pulling them back under `V`, the gate is
exactly the union of thirteen complete `R_V` fibres: one of size ten
and twelve of size twenty. Their sizes total `10+12*20=250`.

The sign update, its invariant record, and the general classification of
fixed checkpoint invariants are already supplied by
`U-NATIVE-INVARIANT-AND-NOWRITE`. The gate on the synchronized sheet is
therefore an inherited special case of that invariant record. The
identification with the field image and the explicit entrance-time
classification below do not establish a new independent memory mechanism.

## 7. The full counter-zero prefix (F8)

Let `h=h(p_0)`, `K=K(p_0)`, and `r=r_0`; these are initial data. The
initial control bits are `0,1,1`. The trace table fixes each complete
three-letter chronological word, independently of the other coordinates.
The gate and fibre laws then give

| Initial sheet | Word, applied left to right | Traces `(z1,z2,z3)` | `h1` | `h2` | `h3` |
| --- | --- | --- | --- | --- | --- |
| `0` | `a c e` | `(0,2,1)` | `K` | `-J2K+R(r)` | `J2K-R(r)` |
| `1` | `b b d` | `(4,1,1)` | `-J2h` | `h` | `-h` |
| `2` | `c c e` | `(0,2,1)` | `-J2h+R(r)` | `h` | `-h` |
| `3` | `d b d` | `(4,1,1)` | `-h` | `J2h` | `-J2h` |
| `4` | `e b d` | `(4,1,1)` | `-h` | `J2h` | `-J2h` |

In the `X_0` row, `a` leaves `r` unchanged, and `e` negates the gate
after `c`; this gives the displayed signs. In the `X_2` row, the first
`c` changes `r` to `-r`. The second gate value is therefore

```text
-J2(-J2h+R(r))+R(-r)
=h-J2R(r)-R(r)
=h,
```

because `J2R(r)=-R(r)`. The other three rows follow by successive
applications of `-J2` and `-I`. This derivation retains the actual fibre
update; treating `r` as a fixed forcing value across two `c` steps would
give an incorrect prefix.

For completeness the associated `r` values are

| Initial sheet | `r1` | `r2` | `r3` |
| --- | --- | --- | --- |
| `0` | `r` | `-r` | `1+r` |
| `1` | `-r` | `r` | `1-r` |
| `2` | `-r` | `r` | `1-r` |
| `3` | `1-r` | `r-1` | `2-r` |
| `4` | `1-r` | `r-1` | `2-r` |

### 7.1 Exactly the checkpoints gated from time three onward

For every nonzero initial sheet, the final gate is `-h` or `-J2h`.
Consequently exactly its `125` initially gated checkpoints have `h3=0`.

On `X_0`, `h3=0` is equivalent to

```text
K=(-r,r),
u+2v=-r,       u'+2v'=r.
```

For every choice of `v,v',r` these equations determine `u,u'`, and
the trace fixes `q`. Thus this sheet also has exactly `125` such
checkpoints. Explicitly they are

```text
(u,v,u',v',q,r)
=(3v-r, v, 3v'+r, v', v+v'-r, r),
v,v',r in F5.
```

This also proves directly that `h3` has a two-dimensional image on each
initial sheet, with all `25` values having `125` preimages: on `X_0`,
for fixed `r` the readout `K` is surjective with `25` piston preimages
per value, and on the other sheets the corresponding statement holds
for `h`.

By the all-time induction, the exact set gated at every `n>=3` is

```text
{x in X_0:K(p)=(-r,r)}
union (G intersect (X_1 union X_2 union X_3 union X_4)).
```

The union is disjoint and has `625` points. This conclusion is for the
actual counter origin zero used by the contract.

### 7.2 The five-point overlap on the initial zero sheet

Impose both `h0=0` and `h3=0` on `X_0`. The first equation gives
`v=3u`, `v'=3u'`, and hence `K=(2u,2u')`. The second says

```text
(2u',2u)=(r,-r).
```

Solving and then imposing trace zero gives exactly

```text
p=(2r,r,3r,4r),       q=4r,       r in F5.
```

There are five such checkpoints. Each of the two sets `h0=0` and
`h3=0` on `X_0` has `125` elements, so each of its one-sided differences
from the other has `125-5=120` elements.

### 7.3 Pointwise retention and simultaneous retention

The counts of initially gated points that are gated at one specified
boundary are

| Initial sheet | `h0=0` | `h0=h1=0` | `h0=h2=0` | `h0=h3=0` |
| --- | --- | --- | --- | --- |
| `0` | `125` | `5` | `5` | `5` |
| `1` | `125` | `125` | `125` | `125` |
| `2` | `125` | `25` | `125` | `125` |
| `3` | `125` | `125` | `125` | `125` |
| `4` | `125` | `125` | `125` | `125` |

These columns are separate intersections with the initial gate; they
are not cumulative survival counts. To justify the exceptional entries,
on `X_0` initial gating makes `K=(2u,2u')`, so `h1=0` forces zero
piston and permits five pairs `(q,r)=(-r,r)`. The `h2=0` and `h3=0`
intersections are the same five-point overlap just derived. On `X_2`,
initial gating gives `h1=R(r)`, so `h1=0` requires `r=0`, leaving
exactly `25` points; both later gates return to zero.

Simultaneous gating at all four boundaries is stronger. On `X_0`,
`h0=h1=0` first forces zero piston; then `h2=R(r)=0` forces `r=0`,
and the trace forces `q=0`. Only the all-zero checkpoint survives all
four boundaries. Equivalently, among the five points of the overlap,
`h1=(4r,r)` vanishes only at `r=0`. On `X_2`, the simultaneous
condition is precisely `h0=0` and `r=0`. The other three sheets keep
all of their initially gated points throughout the prefix. Therefore

| Initial sheet | Gated at all of `n=0,1,2,3` |
| --- | --- |
| `0` | `1` |
| `1` | `125` |
| `2` | `25` |
| `3` | `125` |
| `4` | `125` |
| Total | `401` |

Combining this exact prefix classification with section 5 proves that
the complete set gated at every nonnegative time is

```text
{(0,0,0,0,0,0)}
union (G intersect X_1)
union (G intersect X_2 intersect {r=0})
union (G intersect X_3)
union (G intersect X_4).
```

The five parts are disjoint. The cardinality `401` is thus an all-time
consequence of the explicit prefix and an induction, not a survival
count inferred from a finite run.

### 7.4 The zero preparation

Direct application of the fixed word `a c e` to the zero checkpoint gives

| Boundary | Full checkpoint | Trace | Gate |
| --- | --- | --- | --- |
| `0` | `(0,0,0,0,0,0)` | `0` | `(0,0)` |
| `1` | `(0,0,0,0,0,0)` | `0` | `(0,0)` |
| `2` | `(2,1,2,1,1,0)` | `2` | `(0,0)` |
| `3` | `(0,0,1,3,1,1)` | `1` | `(0,0)` |

In particular `r3=1`, while the gate remains zero. The all-time induction
then retains zero gate for every later checkpoint. The zero gate, zero
piston, zero `r`, and a fixed checkpoint are therefore distinct
conditions even on this explicit preparation.

## 8. Finite regression and serialization (F9)

F9 is a finite regression, not the proof of an infinite-time statement.
The analytic conclusions of sections 5 and 7 imply its declared
predicates: the zero preparation has zero gate at all `4097` boundaries
`n=0,...,4096` and belongs to `X14` for `n>=3`; every initial checkpoint
obeys

```text
h_n=0 iff h_3=0,
h_n in {h_3,-h_3,J2h_3,-J2h_3}
```

for the finite regression range `3<=n<=40`. Whether an implementation
actually executes those complete ranges and uses the actual
`theta_n=popcount(n) mod 2` at each step belongs to the finite execution
audit. The proof of all times was already supplied by the four-case
induction, independently of any such finite run.

The two requested serialized set digests bind the sorted tuples of
`G14` and the explicit `401`-point initial set in section 7.3. Their
encoding is one comma-separated tuple per line, lexicographically
sorted, with an LF after every row including the last. No digest value
is predicted by this proof. The preregistered digests are recorded
outputs, not comparisons against an undisclosed frozen numerical target.

## 9. Scope, inheritance, and audit disposition

F1 is a rederivation of the inherited native premises. F2 is the
unchanged canonical field algebra, certified using its actual
unimodular image certificate and energy adjoint. F3 makes the specified
residue-level comparison and also exhibits its failure as an energy
isometry. F4 and F5 retain the actual six-coordinate generator action,
including the information missing from an `h`-only description of `a`.
F6 proves the synchronized gate claim by induction while distinguishing
it from pointwise fixation. F7 identifies that gate with an already
admitted invariant record, so its permanence remains an inherited
corollary. F8 supplies the complete entrance prefix and initial-set
classification. F9 remains a finite regression.

All claims stay at L1. This proof establishes no universal integer lift
of native U, no physical port or contact, no derived source preparation,
no energy minimum, no permanent physical write event, and no new
L2-L6 identification. The variable `z` is the sum of six existing
coordinates, not an added register. The native path is in `F5^6`, not
an integer `Z^6` trajectory. No Canon promotion is asserted by writing
this audit proof.

At the writing of this document, every claimed mathematical target
remains part of the proposed exact proof under the audit's frozen
preregistration. Computational survival, architecture replays, public
custody checks, and the final audit disposition must be recorded by the
owning audit after its authorized pinned execution.
