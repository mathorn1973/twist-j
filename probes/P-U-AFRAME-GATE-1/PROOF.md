# Proof: native shell gate of U

PUBLIC / NON-CANONICAL / L1. Issue #1550, program #1548 lane A.
Owner Claude-20261016-v103-aframe-gate; author A. M. Thorn, Apache-2.0.

Written before any scientific execution of this probe. Reviewer lanes
must not read this file before their own public pin.

## 0. Frozen objects

All checkpoint arithmetic is in F5. A checkpoint is
`x=(p1,p4,p1p,p4p,q,r)` in `X=F5^6`, its piston is `p=(p1,p4,p1p,p4p)`
and its trace is `z(x)=p1+p4+p1p+p4p+q+r`. The trace is a function of the
six coordinates, not a seventh register. The v102 generators are

```text
a(x)=(p4,p1,p4p,p1p,q,r),
b(x)=(-p1p,-p4p,-p1,-p4,-q,-r),
c(x)=(2-p1p,1-p4p+r,2-p1,1-p4-r,1-q,-r),
d(x)=(2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),
e(x)=(2-p1,1-p4,3-p1p,4-p4p,2-q,1-r),
```

with `g0..g4=a..e`, selector `T_t(x)=g_(z(x)+2t mod 5)(x)`, driver
`theta_n=popcount(n) mod 2` and actual update `x_(n+1)=T_(theta_n)(x_n)`
from counter origin `n=0`. Put `X_s={x:z(x)=s}`, `X14=X_1 u X_4`,
`J(u,v)=(v,u)`, and

```text
W(p1,p4,p1p,p4p)=(p4,p1,p4p,p1p),
h(x)=(h1,h2)=(p4+2p1, p4p+2p1p),
G={x in X : h(x)=0},   G14=G n X14.
```

`G` is the zero gate. Field data from FIELD-CHAIN-FIRST-WORK shared proof 2
are used unchanged: `A_f`, `B_f`, `H(y)=y^t B_f y/2`, `L`, `Vinv`, `Vh`.

## 1. Residue image of L

Inherited (Canon shared proof 2): `A_f^5=I`, `L=(I-A_f)(I-A_f^2)`,
`A_f L=L A_f`, `L^2=5A_f^3`, `Vinv=A_f^2 L`, `Vinv L=L Vinv=5I`,
`det Vh=1`, and `y in L Z^4` iff `y0+2y1=y2+2y3=0 mod 5`.

**Proposition 1.** Let `C={y in F5^4: y0+2y1=0, y2+2y3=0}`. The image of
`L mod 5` on `F5^4` is exactly `C`, it has 25 elements, every image
residue has exactly 25 residue preimages, and an integer `y` lies in
`L Z^4` iff `y mod 5` lies in `C`.

*Proof.* Modulo 5 the rows of `L` are `(1,2,4,3)`, `(2,4,3,1)`,
`(0,0,1,2)`, `(0,0,2,4)`. The second is twice the first and the fourth
twice the third, so `y=Lx` gives `y1=2y0` and `y3=2y2`; hence
`y0+2y1=5y0=0` and `y2+2y3=5y2=0`. The first and third rows are
independent, so the rank is 2, the image has `25=|C|` elements and
equals `C`; the kernel has 25 elements. From `Vinv L=5I`,
`5Z^4=L Vinv Z^4` lies in `L Z^4`. If `y mod 5=Lx mod 5`, then
`y-Lx` is in `5Z^4`, hence `y` is in `L Z^4`; the converse is immediate.
Equivalently `Vinv y=0 mod 5`, whose rows are multiples of `y0+2y1+y2+2y3`
and `y2+2y3`. This re-derives the inherited integer criterion; it is not
a new energy-shell or minimum statement.

## 2. The comparison map and the gate

**Proposition 2.** For every piston, `h(p)=(W(p)0+2W(p)1, W(p)2+2W(p)3)`.
Hence `x in G` iff `W(p) mod 5` lies in `C` iff every integer lift of
`W(p)` lies in `L Z^4`. `W` is an involutive coordinate permutation, it
equals the piston action of `a`, and it maps `K=ker h` (25 pistons)
bijectively onto `C`. `|G|=625`, `|G n X_s|=125` for every `s`, and
`|G14|=250`.

*Proof.* Substitute `W(p)=(p4,p1,p4p,p1p)`. `h:F5^4->F5^2` is linear
and surjective (its `p4` and `p4p` coefficients are 1), so `|K|=25`.
For a fixed piston and `q`, the sheet value fixes `r`, giving
`25*5=125` gated checkpoints per sheet.

`W` is a fixed comparison map only. It is not an `H`-isometry:
`H(e0)=2` and `H(W e0)=H(e1)=3`. No integer lift of U, physical contact
or port is defined by `W`.

## 3. Generator laws on the complete domain

**Proposition 3.** On every checkpoint of `X`,

```text
h(ax)=(p1+2p4, p1p+2p4p)=2h(x)+2(p1,p1p),
h(bx)=(-h2,-h1)=-J h(x),
h(cx)=(-h2+r,-h1-r)=-J h(x)+(r,-r),
h(dx)=h(ex)=(-h1,-h2)=-h(x).
```

*Proof.* For `b` the new `(p1,p4,p1p,p4p)` is `(-p1p,-p4p,-p1,-p4)`,
giving `(-p4p-2p1p, -p4-2p1)`. For `c` it is
`(2-p1p,1-p4p+r,2-p1,1-p4-r)`, giving `(5-h2+r, 5-h1-r)`. For `d` and
`e` it is `(2-p1,1-p4,3-p1p,4-p4p)`, giving `(5-h1,10-h2)`. For `a` it
is `W(p)`, giving `(p1+2p4,p1p+2p4p)`; and `2h1+2p1=2p4+6p1=p1+2p4`,
likewise for the second component.

**The a action is not an h-only law.** The linear map
`p -> (h(p),h(ap))` is block diagonal with blocks
`(p1,p4)->(2p1+p4, p1+2p4)` and `(p1p,p4p)->(2p1p+p4p, p1p+2p4p)`,
each of determinant `3`, nonzero in F5. It is a bijection of `F5^4`.
Therefore, for every fixed value of `h(x)`, the 25 pistons with that
value give all 25 values of `h(ax)`, each once. No function `f` with
`h(ax)=f(h(x))` exists. Explicit witness: `x=0` and `x'=(1,3,0,0,0,0)`
both have `h=0`, while `h(ax)=0` and `h(ax')=(2,0)`.

**Gate consequences.** On `G`, `p4=3p1` and `p4p=3p1p`, so
`h(ax)=(2p1,2p1p)`: `a` keeps exactly the 25 gated checkpoints with zero
piston. On `G`, `h(cx)=(r,-r)`: `c` keeps exactly the 125 gated
checkpoints with `r=0`. `b,d,e` map `G` into `G` and its complement into
its complement, because `-J` and `-I` are invertible.

## 4. Every selector branch

The selected generator is `g_(z+2t)`. With the trace laws
`z(ax)=z`, `z(bx)=-z`, `z(cx)=z(dx)=2-z`, `z(ex)=3-z`
(direct sums of the displayed coordinates):

| `z` | `t` | generator | next `z` | next `h` |
|---|---|---|---|---|
| 0 | 0 | a | 0 | `(p1+2p4, p1p+2p4p)` |
| 1 | 0 | b | 4 | `-J h` |
| 2 | 0 | c | 0 | `-J h+(r,-r)` |
| 3 | 0 | d | 4 | `-h` |
| 4 | 0 | e | 4 | `-h` |
| 0 | 1 | c | 2 | `-J h+(r,-r)` |
| 1 | 1 | d | 1 | `-h` |
| 2 | 1 | e | 1 | `-h` |
| 3 | 1 | a | 3 | `(p1+2p4, p1p+2p4p)` |
| 4 | 1 | b | 1 | `-J h` |

The next-trace columns reproduce the inherited sheet maps
`T_0=(0,4,0,4,4)` and `T_1=(2,1,1,3,1)`. The `(z,q,r)` updates are the
inherited quotient table of U-NATIVE-APPARATUS-HISTORY-FACTOR.

## 5. Absorbing sheet and all-time gate

**Theorem 5.** For `t` in `{0,1}` and every `x` in `X14`:
`T_t(x)` lies in `X_(4+2t mod 5)`, a subset of `X14`; the selected generator is
`b` or `d` or `e`; and `h(T_t x)=M h(x)` with `M` in `{-J,-I}`.
Consequently, for every binary driver sequence and every `m` with
`x_m` in `X14`, for all `n>=m`:

```text
x_n in X14,   h(x_n) in {h(x_m), -h(x_m), J h(x_m), -J h(x_m)},
x_n in G  iff  x_m in G.
```

*Proof.* The four branch rows with `z` in `{1,4}` select `b,d,e,b` and
have next trace `4,1,4,1` as displayed, equal to `4+2t mod 5`. Proposition 3
gives the `h` law. Induction on `n`: the base `n=m` is the hypothesis;
if `x_n` is in `X14`, the step just proved puts `x_(n+1)` in `X14` and
multiplies `h` by `-J` or `-I`. These generate the Klein group
`{I,-I,J,-J}`, whose elements are invertible, so `h(x_n)=0` iff
`h(x_m)=0`. The induction is over all `n`; it uses the step on the
complete finite set `X14 x {0,1}` and no trajectory length. Both `G14`
and `X14\G14` are forward invariant, so the gate status is absorbed on
`X14`.

**Set preservation is not pointwise fixation.** The fixed points of `b`
satisfy `p1p=-p1`, `p4p=-p4`, `q=r=0`, so their trace is 0 and none lies
in `X14`. `d` has the unique fixed point `(1,3,4,2,3,3)`, trace 1, and `e`
the unique fixed point `(1,3,4,2,1,3)`, trace 4 (inherited fixed-point
table). Both have `h=(3+2,2+8)=0`. Hence on `X14`, `T_0` (`b` on `X_1`,
`e` on `X_4`) has exactly one fixed point and `T_1` (`d` on `X_1`, `b` on
`X_4`) exactly one, both in `G14`. Each `T_t` moves 249 of the 250 gated
synchronized checkpoints: the zero gate is preserved as a set, not
pointwise. A moved checkpoint may keep its piston and change only `(q,r)`.
Since every generator is a bijection of `X` sending a sheet onto a sheet,
`T_t` maps `G n X_1` and `G n X_4` each bijectively onto
`G n X_(4+2t mod 5)`.

**Inheritance.** Directly,
`h1+h2=2(p1+p1p)+(p4+p4p)` and `h1-h2=2C+D` with
`C=p1-p1p-2`, `D=p4-p4p-1`. With the inherited vector
`V=(A,B,chi(z)C,chi(z)D)` of U-NATIVE-INVARIANT-AND-NOWRITE,

```text
G14 = V^(-1)(S),   S={v: 2v1+v2=0, 2v3+v4=0},   S=-S.
```

Since that row proves `V(next)=-V(x)` on `X14` for both bits, invariance
of `G14` is an inherited corollary. The Klein-group law above is the same
information restricted to two linear functionals of `V`. On each of
`X_1` and `X_4`, `V` is an affine bijection of the piston, with `q` free
and `r` determined, so every value of `V` has exactly 10 preimages in
`X14`. Thus `|G14|=25*10=250`, and `G14` is the union of exactly 13 R
fibres: the size-10 fibre `V=0` and 12 fibres `{v,-v}` of size 20.

## 6. Origin-zero prefix

The first driver bits are `theta_0,theta_1,theta_2=0,1,1`. The inherited
word `011` synchronizes every initial trace to `z_3=1`
(TM-SHEET-SYNCHRONIZING-GRAPH, KERNEL-Z6-SYNCHRONIZATION). From the
branch table, the chronological generator words on initial sheets
`s=0,...,4` are `ace, bbd, cce, dbd, ebd`. Writing `h0=h(x_0)`, `r0` for
the initial `r`, and using that every generator is an involution:

| `s` | `h_1` | `h_2` | `h_3` |
|---|---|---|---|
| 0 | `(p1+2p4, p1p+2p4p)` | `(-p1p-2p4p+r0, -p1-2p4-r0)` | `(p1p+2p4p-r0, p1+2p4+r0)` |
| 1 | `-J h0` | `h0` | `-h0` |
| 2 | `-J h0+(r0,-r0)` | `h0` | `-h0` |
| 3 | `-h0` | `J h0` | `-J h0` |
| 4 | `-h0` | `J h0` | `-J h0` |

For `s=0`, `x_1=a x_0` has `r_1=r0` and `x_2=c x_1` has `r_2=-r0`.

**Proposition 6.** For `n>=3`, `x_n in G` iff `x_3 in G`
(Theorem 5 with `m=3`). For `s` in `{1,2,3,4}` this holds iff `h0=0`.
For `s=0` it holds iff `p1p+2p4p=r0` and `p1+2p4=-r0`. Exactly 125
initial checkpoints of each sheet are gated from `n=3`, 625 in total,
matching the inherited fixed-time 5-to-1 synchronization onto
`X_1`, whose gated part has 125 points.

On `X_0` the two gated sets differ: 5 checkpoints are gated at both
`n=0` and `n=3` (`p=(2r0,r0,3r0,4r0)`, `q=4r0`), 120 only at `n=0` and
120 only at `n=3`. Among the 125 initially gated checkpoints of each
sheet, the numbers gated at `n=0,1,2,3` are

```text
s=0: 125, 5, 5, 5      s=1: 125 at every n
s=2: 125, 25, 125, 125 s=3,4: 125 at every n
```

For `s=0`, `h1=(2p1,2p1p)` vanishes only on the zero piston, and then
`h2=(r0,-r0)`. For `s=2`, `h1=(r0,-r0)` leaves the gate at `n=1` iff
`r0!=0` and returns at `n=2`. The checkpoints gated at every `n>=0`
number `1+125+25+125+125=401`; the only one in `X_0` is `x_0=0`.

**Explicit zero start.** From `x_0=0` at `n=0` the actual states are

```text
x_0=(0,0,0,0,0,0), a -> x_1=(0,0,0,0,0,0),
c -> x_2=(2,1,2,1,1,0), e -> x_3=(0,0,1,3,1,1),
```

with traces `0,0,2,1`, `h_n=0` for `n=0,1,2,3`, and `r_3=1`. By
Theorem 5 this orbit is gated at every `n>=0`. Its `r` coordinate is
not zero for all `n`; gate membership never uses `r=0` on `X14`, where
`c` is not selected.

## 7. Scope

Statement layer L1, exact finite arithmetic and induction. The
all-time result is the induction of Theorem 5 with the explicit prefix
of Section 6; any finite trajectory in the verifier is a regression
witness only. Inherited rows supply the generators, selector, sheet maps,
synchronization, quotient, `V` law and field algebra; they are rechecked,
not reclaimed. No universal integer lift of U, H-isometry of `W`,
physical port, contact, `r=0` law, affine trace law, energy minimum or
field preparation is asserted. `x_n` is an F5 checkpoint, not a
trajectory in `Z^6`.
