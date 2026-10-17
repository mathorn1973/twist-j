# The residue bridge and the remaining source interface

**PUBLIC / NON-CANONICAL / L1.** Proposed synthesis; no Canon adoption.
Specification pin: `c8485301e1d72e6e47159d8f66b3a1a12a920477`.
The source roles A-D and RA-RD below refer to the full immutable pins in
`CONTRACT.md` and the file-level hashes in `SOURCES.tsv`. `ACCEPTANCE.md`
records the qualifications. This text supplies an exact analytical
composition of those sources, with no new scientific program.

The source results establish a precise bridge: the native zero-gate
predicate becomes the integer image-lattice residue condition after the
specified piston swap. Of
the 25 admitted residues, exactly 20 have a preimage of energy one. The
native zero orbit reaches one such residue at boundary 3, with a unique
integer image of minimum energy 5. At boundary 4 it reaches one of the
five residues with no energy-one preimage. The positive minimum therefore
does not define a persistent unit-seed preparation law. Separately, the
unchanged contact source cannot distinguish messages that have identical
`(q,r)` histories and a common complete receiver/protocol.

## 1. Fix the carriers and coordinates

All native arithmetic is in `F5`. A checkpoint is
`x=(a,b,c,d,q,r)`, its piston projection is `pi_P(x)=(a,b,c,d)`, and
`z=a+b+c+d+q+r`. The trace is a function, not an additional register.
At counter origin zero,

```text
g0(x) = (b,a,d,c,q,r)
g1(x) = (-c,-d,-a,-b,-q,-r)
g2(x) = (2-c,1-d+r,2-a,1-b-r,1-q,-r)
g3(x) = (2-a,1-b,3-c,4-d,1-q,1-r)
g4(x) = (2-a,1-b,3-c,4-d,2-q,1-r)
T_t(x) = g_(z(x)+2t mod 5)(x)
x_(n+1) = T_(theta_n)(x_n), theta_n = popcount(n) mod 2.
```

The comparison map and gate are

```text
W(a,b,c,d)=(b,a,d,c),       h(x)=(b+2a,d+2c),
K={(a,3a,c,3c):a,c in F5}, G0=pi_P^(-1)(K),
G_L={(3s,s,3t,t):s,t in F5}.
```

Thus `K` and `G_L` each have 25 elements, `G0` has 625 checkpoints,
and `W(K)=G_L`. `K` and `G_L` are different marked subspaces. They
must not both be denoted by the same unqualified kernel.

Over the integers the fixed cell marking is `y=(a,b,c,d)` in `Z^4`:

```text
A_f = [[ 1, 0, 1, 0],     B_f = [[ 4,-2, 2,-1],
       [ 0, 1, 0, 1],            [-2, 6,-1, 3],
       [-2, 1,-1, 1],            [ 2,-1, 2, 0],
       [ 1,-3, 1,-2]]            [-1, 3, 0, 2]]

L = [[ 1,-3,-1,-2],       V_inv = [[ 1, 2, 1, 2],
     [-3, 4,-2, 1],                [ 2,-1, 2,-1],
     [ 0, 5, 1, 2],                [ 0,-5, 1,-3],
     [ 5,-5, 2,-1]]                [-5, 5,-3, 4]]

H(y)=y^t B_f y/2
    =2a^2-2ab+3b^2+c^2+d^2+2ac-ad-bc+3bd.
```

These are the literal canonical cell coordinates. No identification with
the untransformed cyclotomic power basis is made. The inherited v102
identities are

```text
A_f^5=I, sum_(j=0)^4 A_f^j=0, H(A_f y)=H(y),
L=(I-A_f)(I-A_f^2), det L=25, L^2=5A_f^3,
V_inv=A_f^2 L, V_inv L=L V_inv=5I,
L^t B_f L=5B_f, H(Lu)=5H(u).
```

`H` is a positive definite integer-valued form on `Z^4`. Its use here
is mathematical; a physical preparation or actuation does not follow
from a value of this form. The inherited image criterion is

```text
y in L Z^4  iff  y0+2y1 = y2+2y3 = 0 (mod 5).
```

Consequently, for every checkpoint `x`,

```text
h(x)=0
  iff W pi_P(x) in G_L
  iff every integer representative of W pi_P(x) belongs to L Z^4.
```

The final universal quantifier is justified because membership in `LZ^4`
depends only on the residue. A residue outside `G_L` has no representative
in `LZ^4`; for a residue in `G_L`, every integer representative belongs
to `LZ^4`. Their integer energies can differ.
This is the exact A-to-B bridge, rather than a chosen lift or a decoder.

## 2. Gate permanence has a restricted dynamical meaning

Let `J2(h1,h2)=(h2,h1)`. Direct substitution in the native generators gives

```text
h(g0 x)=2h(x)+2(a,c),
h(g1 x)=-J2 h(x),
h(g2 x)=-J2 h(x)+(r,-r),
h(g3 x)=h(g4 x)=-h(x).
```

There is no autonomous `h`-only law for `g0`: for each piston pair the
map `(a,b)->(2a+b,a+2b)` has determinant 3 in `F5`. Thus
`p -> (h(p),h(g0 p))` is bijective on `F5^4`.

Write `X_s={x:z(x)=s}` and `X14=X_1 union X_4`. Selection on `X14`
uses only `g1,g3,g4`, so it preserves both zero and nonzero `h`, for
either driver bit and any future bit word. This is also a consequence
of the inherited protected-sign invariant, and is credited as such.
It does not state global bijectivity or pointwise fixation. In fact,

```text
T_t(G0 intersect X14)=G0 intersect X_(4+2t mod 5).
```

The domain has 250 points and the image 125; each target has two
preimages there. For each `t in {0,1}`, `T_t` fixes one point of
`G0 intersect X14` and moves the other 249. RA's narrower wording is
required whenever A's phrase
"preserved as a set" is used.

For the actual zero start the first bits are `0,1,1`, and A gives

```text
x0=x1=(0,0,0,0,0,0),
x2=(2,1,2,1,1,0),
x3=(0,0,1,3,1,1).
```

All four checkpoints have `h=0`, and `x3 in X_1`. The induction above
therefore proves gate membership for every `n>=0`. In particular `r3=1`;
no all-time `r=0` condition is involved. The inherited three-step
synchronization sends each initial sheet bijectively onto `X_1`, so
exactly 625 initial checkpoints are gated from boundary 3 onward. Only
125 gated targets in `X_1` are reached at that boundary, not all 250
points in `G0 intersect X14`. These counts do not define readiness.

## 3. Exactly twenty residues have an energy-one preimage

Here a **unit seed** means exactly `u in Z^4` with `H(u)=1`. It does
not mean the full multiplicative unit group of an algebraic number ring.
Let `U1={u:H(u)=1}` and `pi_L(u)=Lu mod 5`.

### 3.1 A complete analytic count of the unit shell

RB's correct independent square completion is

```text
4H = Q(a,b) + (2c+2a-b)^2 + (2d-a+3b)^2,
Q(a,b)=3a^2+2ab+2b^2,
2Q=5a^2+(a+2b)^2,       3Q=5b^2+(3a+b)^2.
```

At `H=1`, `Q<=4`, so `|a|,|b|<=1`. The complete two-square fibers,
with the parities imposed by their displayed linear forms, give:

| Pairs `(a,b)` | `Q` | Number of `(c,d)` per `(a,b)` | Total |
|---|---:|---:|---:|
| `(0,0)` | 0 | 4 | 4 |
| `(0,1),(0,-1)` | 2 | 4 | 8 |
| `(1,0),(-1,0)` | 3 | 2 | 4 |
| `(1,-1),(-1,1)` | 3 | 2 | 4 |
| `(1,1),(-1,-1)` | 7 | 0 | 0 |

Writing `s1=2c+2a-b`, `s2=2d-a+3b`, each permitted square pair gives
exactly one integer pair `c=(s1-2a+b)/2`, `d=(s2+a-3b)/2`.
For example the first fiber is `c^2+d^2=1`; the next has two odd
squares summing to 2; each `Q=3` fiber has one even and one odd square
summing to 1. This exhausts the nine possible `(a,b)` pairs and proves
`|U1|=20` without an empirical box assumption. The bare count is inherited
from the credited #1323 lineage. The native-coordinate derivation and
residue classification have their separately stated B/RB scope.

### 3.2 Kernel, injectivity and the five missing residues

The displayed `L mod 5` has rank two and image `G_L`. Its integer-domain
kernel has the stronger exact description

```text
ker(pi_L)=L Z^4.
```

Indeed, if `Lu=5v`, then `u=V_inv v=A_f^2 L v=L A_f^2 v`.
Conversely `L(Lv)=5A_f^3 v` has zero residue. Every nonzero kernel
vector therefore has energy a positive multiple of five.

If two unit seeds have the same image residue, their difference is in
this kernel. Cauchy-Schwarz for the positive form gives

```text
0 <= H(u-v) <= (sqrt(H(u))+sqrt(H(v)))^2 = 4.
```

A multiple of five in this interval is zero, so `u=v`. Thus `pi_L`
is injective on the entire unit shell.

On `G_L`, `A_f` acts in the `(s,t)` coordinates by
`(s,t)->(s+t,t)`. Its fixed subgroup is

```text
G_L^(A_f)={(3s,s,0,0):s in F5}
          ={(0,0,0,0),(1,2,0,0),(2,4,0,0),
            (3,1,0,0),(4,3,0,0)}.
```

No unit can map to this subgroup. Such a unit would have
`pi_L(A_f u-u)=0`; the same energy bound gives `A_f u=u`.
Then `0=sum_(j=0)^4 A_f^j u=5u`, hence `u=0`, a contradiction.
There are exactly 20 other residues, so injectivity and the complete
unit count prove the bijection

```text
pi_L: U1 -> G_L minus G_L^(A_f).
```

This is the reviewed `20+5` classification. A missing unit preimage
does not mean a missing integer shell lift. No optional claim about
the higher-shell minima of these five residues is used.

### 3.3 The boundary-3 minimum is global and unique

For the zero orbit,

```text
rho3=W pi_P(x3)=(0,0,3,1),
u*=(0,-1,-1,2),        y*=Lu*=(0,0,-2,1).
```

Correct substitution in the literal form gives
`H(u*)=3+1+4-1-6=1`, so `H(y*)=5`. This substitution deliberately
does not copy the erroneous scalar expansion in RB PROOF section 4.

Let `y in L Z^4` have residue `rho3`. It has a unique integer preimage
`u=V_inv y/5`. Since the residue is nonzero, `u!=0`, whence the positive
integer form has `H(u)>=1` and `H(y)=5H(u)>=5`. Equality requires a
unit seed of residue `rho3`; the preceding injectivity forces `u=u*`.
Therefore

```text
min {H(y): y in L Z^4, y mod 5=(0,0,3,1)} = 5,
argmin = {(0,0,-2,1)}.
```

This conclusion is over the whole infinite coset. It establishes an
available integer field representative of minimum energy at one named native
boundary, not that U creates it or that a physical process selects it.

### 3.4 The next native step prevents an all-time unit-seed lift

At boundary 3, `theta3=popcount(3) mod 2=0` and `z3=1`, so the step
from 3 to 4 uses `g1`. Therefore

```text
x4=g1(x3)=(4,2,0,0,4,4),
h(x4)=(0,0),
rho4=W pi_P(x4)=(2,4,0,0) in G_L^(A_f).
```

The exact classification proves the following direct synthesis corollary:

```text
There is no sequence (u_n)_(n>=3) in Z^4 with
H(u_n)=1 and Lu_n mod 5=W pi_P(x_n) for every n>=3
on the fixed origin-zero native orbit.
```

The required `u4` does not exist. This excludes even a freely chosen
sequence; no causality, locality, selection algorithm or evolution law for
the seeds needs to be assumed. Equivalently no sequence of `L`-image
representatives all having energy 5 satisfies that same all-`n>=3` contract.

This is a consequence of A+B, not a new numerical experiment or an
additional independent review. It does not exclude higher-energy lifts,
different comparison maps, or an eventual unit lift after a later cutoff.
It states no exact minimum at boundary 4. The all-time gate theorem and
the boundary-3 minimum remain true.

## 4. The declared message families meet different gates

Use the affine chart

```text
A=a+c, B=b+d, C=a-c-2, D=b-d-1.
h1=A+3B+C+3D,       h2=A+3B-C-3D,
h1+h2=2A+B,        h1-h2=2C+D.
```

Thus `h=0` is equivalent to both `B=3A` and `D=3C`. The frozen
D-contract sentence `h1=B+2A` is false; only the sum is equal to that
quantity. This is retained as a refuted literal claim, not silently repaired.

### 4.1 Original two-message preparation

For every `(lambda,mu) in F5^2`, define the original initial state by
`(A,B,C,D,q,r)=(1,0,lambda,mu,0,1)` and put `k=lambda+3mu`.
All share `z0=2` and the prefix `g2,g2,g4`. The gate values are

| Boundary | `h` | Sum |
|---|---|---|
| 0 and 2 | `(1+k,1-k)` | 2 |
| 1 | `(k,3-k)` | 3 |
| 3 | `(-1-k,-1+k)` | 3 |

On the complete tail, with `s=A in {1,-1}`, the inherited parameters are
`z,s in {1,-1}`, `q in F5`, `B=0`, `C=sz lambda`, `D=sz mu`,
`r=z-s-q`. They give

```text
h=s(1+zk,1-zk),      h1+h2=2s != 0.
```

The complete support is the union of 25 disjoint 20-point tails and
two 25-point prefix sheets, totaling 550. There are **zero gate points
among all 550**, and no actual-time exception. The parameter proof uses
the inherited full-support theorem, rather than extending a finite sample.
Changing the integer representative of a failing residue cannot help.

At each fixed common time the full piston distinguishes all 25 message
pairs, while `h` distinguishes only the five values of `k`. This is
compatible with the original family having semantic readback while never
entering this shell gate. A fixed-time piston distinction is not a
stationary piston-only decoder claim.

### 4.2 Alternative preparation

Put `t=3(1+mu-lambda)` and define the alternative initial state by
`(A,B,C,D,q,r)=(mu,0,3,0,2-mu-t,t)`. Its gate values at boundaries
`0,1,2,3` are respectively

```text
(mu+3,mu-3),
(-mu+3+t,-mu-3-t),
(mu+3,mu-3),
(-mu+2,-mu-2).
```

Only boundary 1 can pass: the sum forces `mu=0`, then `t=2` and
`lambda=2`. Its checkpoint is `(2,1,2,1,1,3)`. The complete tail has
`C in {2,3}`, `z in {1,4}`, `B=D=0`, `A=2Cz mu`; hence
`h=C(2z mu+1,2z mu-1)` is never zero. The inherited full support has
150 points: 100 tail points and two 25-point prefix sheets. Its only
gate point is this transient boundary-1 state, which leaves the gate
at the next step.

The initial controls are
`q0=3lambda+mu+4`, `r0=2lambda+3mu+3`. Their linear determinant is
2 in `F5`. The common selected word acts invertibly on these controls,
so `(q_n,r_n)` distinguishes all 25 pairs at each fixed common time.
Both labels were already prepared in the source port. This is not proof
of native loading into a previously common receiver or of accepted contact.

### 4.3 Registered one-shot occupied states and absence

For occupied payload `lambda`, let
`x_lambda(0)=(lambda,0,-lambda,0,0,0)`. The correct prefix and tail
argument, including the accepted D erratum, is

```text
n=0:   h=(2lambda,-2lambda),
n=1,2: h=(lambda,-lambda),
n>=3:  h=(-2Bz lambda,2Bz lambda),
       B in {2,3}, z in {1,4}, -2Bz in {1,-1}.
```

All displayed coefficients are nonzero. Thus at every actual time the
gate passes exactly for occupied `lambda=0`. The last formula belongs
only to the ready tail, not to the prefix. For completeness, the tail
graph is parametrized by `B,z` as above and `D,r in F5`, with

```text
a=1+B+2Bz, c=-1+B-2Bz,
b=3(B+D+1), d=3(B-D-1), q=z-3B-r,
lambda=3-BzD.
```

On this 100-state graph the gate selects the 20 states with zero
payload. This is a graph count, not an assertion that one actual orbit
visits all 100 states.

The distinct absence preparation is `x_empty(0)=(0,0,1,0,0,0)`.
Its invariant parametrization gives `h=s(1-z,1+z)` with `s in {1,-1}`,
so its sum never vanishes and absence never passes the gate. The registered
reader remains BLANK on absence; on occupied inputs it is BLANK through
boundary 2 and PRESENT(lambda) from boundary 3. In particular occupied
zero passes the gate while the reader is still BLANK. Gate membership is
therefore not readiness, and PRESENT(0) is not absence.

The five occupied `(q,r)` histories are identical. Absence has a different
prefix: at boundary 2 its controls are `(0,0)` instead of occupied
`(1,0)`. At boundary 3 the quotients agree and later controls agree, but
this does not erase an earlier receiver record. No whole-history blindness
theorem between occupied zero and absence is inferred.

## 5. Exact source blindness of the unchanged rational contact

The native quotient `Q(x)=(z,q,r)` has generator restrictions

```text
(z,q,r), (-z,-q,-r), (2-z,1-q,-r),
(2-z,1-q,1-r), (3-z,2-q,1-r).
```

Selection uses only `z` and the common driver bit. All original
two-message preparations begin at `Q=(2,0,1)`. Induction proves that
their entire quotient and `(q,r)` histories coincide at every common
time. This does not assume global invertibility of the selected map.

Let the balanced section be `ell(0)=0`, `ell(1)=1`, `ell(2)=2`,
`ell(3)=-2`, `ell(4)=-1`. The supplied rational source is

```text
eta(q,r)=(ell(q)/2,(ell(r)+1)/2,0,0),
a_contact(q,r)=S eta(q,r).
```

The canonical `S:Q^4 -> Q^D` on the 705-site carrier is injective:
`(Sv)(y_i)-(Sv)(y_4)=v_i` for `i=0,...,3`. Consequently equal source
vectors are equivalent to equal control pairs, not merely equal energy.
The original family's source histories are identical.

Take a common initial **complete receiver** `Y`: both wave vectors, all
four tape slots, pointer, store, work ledger, direction, schedule state
and fixed budget. Assume the same protocol chooses the same native times
and operations for every message preparation. At a deterministic wave/tape
step, equal `Y` gives equal new `Y`. At a contact invocation, equal `Y`
and equal source give equal energy change, equal acceptance or refusal,
equal resource/ledger updates and equal new `Y`. Induction proves equality
of the entire receiver histories and of every fixed receiver readout.

The argument also covers a common adaptive controller using only the
identical receiver history. A message-dependent waiting rule, source
retuning or external controller input changes the premises. No such
additional input or native compilation is provided by this theorem.

The same argument applies among the five occupied one-shot payloads,
whose initial quotient is common. Their native receiver can nevertheless
read the payload because it also accesses memory pistons `b,d`. The
alternative two-message family fails the common-source premise because
its initial `(q,r)` already encodes both labels. Pair-sensitive input is
necessary here, but does not prove funded receiver separation: contacts
can be refused and a readout can discard information.

This is a scoped deterministic noninterference theorem for a specified
port, preparation family and complete protocol. It is not a universal
no-transmission theorem.

## 6. The integer and rational constructions remain separately typed

| Map or object | Exact type and equality | What is still missing |
|---|---|---|
| Native evolution | `(n,x)` in `N0 x F5^6`; literal counter and checkpoint | Repeated checkpoint does not reset the counter. |
| Piston comparison | `x -> W pi_P(x)` in `F5^4` | It forgets controls and does not provide actuation. |
| Balanced section | `ell^4:F5^4 -> Z^4` | It is a chosen representative, not an additive field embedding or an energy-selection law. |
| Shell admission | `y in LZ^4`; unique `V_inv y/5` in `Z^4` | It leaves the rest of a physical source unspecified. |
| Raw field split | `Z^4 x Z^2 -> Z^6`, the separate index-five split lattice | It is not the index-25 shell criterion. |
| Integer source and chain | A complete 31-coordinate source cell; chain `X_N` has `32N-1` coordinates, or `32N` with pointer | Matter, spectators, static field, resources, channels and timing are not encoded by one four-vector. |
| Rational contact source | Separate fork `x -> (q,r) -> eta -> S eta` | No full integer-chain-to-rational-carrier map is supplied. |
| Funded receiver | Full wave/tape/store/ledger/pointer state with retained controls | Equal source and equal full state, not projected equality alone, determine the guard. |
| Semantic reading | A frozen family, context, raw projection and decoder | Different BLANK/PRESENT contracts cannot be identified by checkpoint coincidence. |

The non-isometric role of `W` is explicit. Over `Z^4`, direct expansion
gives

```text
H(Wy)-H(y)=a^2-b^2+ac-bd.
```

For `e0`, energies are 2 and 3. A simultaneous passive coordinate change
also transforms `B_f` to `W^t B_f W` and operators to `W^-1 A_f W`
and `W^-1 L W`. That preserves the underlying equations in new markings.
Applying `W` as a state operation while retaining the old form and
operator is a different action and does not inherit that equivalence.

## 7. Optional bounded cell comparison

C/RC compare exactly five declared unweighted incidence cells under the
electric-first shear. If `G=C^t C` and coordinates are `(z,M)`,

```text
A_G=[[I,I],[-G,I-G]],
H_G(z,M)=z^t Gz+M^t M+z^t GM,
chi_(A_G)(X)=det(X^2 I+(G-2I)X+I).
```

| Cell Gram `G` | Characteristic polynomial | Exact matrix order | Energy form |
|---|---|---:|---|
| `(2)` | `X^2+1` | 4 | positive definite |
| `(3)` | `X^2+X+1` | 3 | positive definite |
| `[[2,1],[1,2]]` | `X^4+X^2+1` | 6 | positive definite |
| `[[2,1],[1,3]]` | `X^4+X^3+X^2+X+1` | 5 | positive definite |
| `[[3,1],[1,3]]` | `(X^2+1)(X+1)^2` | infinite | positive semidefinite, nullity 1 |

The final row has the exact Jordan chain
`v=(1,1,-2,-2)`, `w=(0,0,1,1)`, with `(A_G+I)v=0` and
`(A_G+I)w=v!=0`. Hence for every integer `n`,
`A_G^n w=(-1)^n(w-nv)`, proving infinite order without a finite-return
search. Matrix order is not the period of every individual state or of
an arbitrary coupled chain.

The digons use distinct parallel edges. Face reversal conjugates the
Gram by a whole diagonal face-sign matrix; edge reversal changes the
whole incidence row and the corresponding divergence column. A lone
coefficient flip is not an allowed reorientation. Reversing a face of
the mixed cell gives `G=[[2,-1],[-1,3]]`, whose `A_G` is the literal
canonical `A_f` above. Raw/active/static splitting is over `Q` or `R`,
not a direct integral splitting of all raw states.

General shear conservation and inverse formulas, triangle order 3,
canonical order 5 and the two-triangle zero mode are inherited. The
bounded comparison and explicit certificates are the scoped increment.
Positivity holds for orders 4, 3, 6 and 5 in this list, so positivity
alone does not select order five. This five-cell census is optional in
the bridge proposal and proves no universal cell minimality, unique
physical choice or prime-five selection.

## 8. The smallest remaining interface obligation

For the unchanged original two-message family, two questions are already
closed at their precise scope: none of its residues passes the chosen
shell gate, and the unchanged `(q,r)` source gives identical complete
receiver histories under a common receiver/protocol. Selecting another
representative of the same residue or another receiver decoder cannot
repair those obstructions.

A positive interface proposal must first state a permitted
**message-sensitive source-access map** on a complete declared preparation
family. It must freeze the complete receiver, common initial conditions,
readout context and equality, funding, timing, allowed controller inputs,
and a falsifier for the intended message distinction. It must say which
current family or access restriction changes. If it includes an integer
chain, it additionally needs a shell-admitted complete preparation and a
typed relation to the full rational carrier. This package proposes that
obligation; it does not choose or execute a new contact experiment.

A narrower future diagnostic may ask which of the 625 three-step gate
preimages admit a declared family with a common initial receiver
projection and at least two protected sign fibers. The projection must
be frozen explicitly: `(b0,d0,q0,r0)` and `(z0,q0,r0)` impose different
conditions. Passing that gate-arrival diagnostic would still not prove
funded transmission. It must have its own preregistration before any
new scientific computation.

## 9. Proposed disposition

The minimal mathematical proposal is the exact gate-to-shell equivalence,
the unit-residue bijection with its five exceptions, the global unique
boundary-3 minimum, the boundary-4 obstruction to an all-`n>=3` unit lift,
and the scoped family/contact limits needed to prevent physical
overinterpretation. C is a separable bounded appendix. All new statements
remain candidate scope pending review; inherited results keep their
existing status and attribution. `CLAIMS.tsv` names every proposed item
and `ACCEPTANCE.md` excludes the unsupported source prose explicitly.

### Immutable source reading points

- [A proof](https://github.com/mathorn1973/twist-j/blob/5c8a675cc114dd3e1f4d95226fd22ba82e3891fa/probes/P-U-AFRAME-GATE-1/PROOF.md) and [RA review](https://github.com/mathorn1973/twist-j/blob/2bceaeafc47f0aa44cfc83bc99cf665dc969e24f/probes/P-U-AFRAME-GATE-AUDIT-1/REVIEW.md).
- [B proof](https://github.com/mathorn1973/twist-j/blob/a12efb98551f972cdfebaa070baf051216ffe7ff/probes/P-FIELD-CHAIN-UNIT-SEED-2/PROOF.md), [B exact table](https://github.com/mathorn1973/twist-j/blob/a12efb98551f972cdfebaa070baf051216ffe7ff/probes/P-FIELD-CHAIN-UNIT-SEED-2/EXPECTED.txt), and [RB independent proof, with exclusions](https://github.com/mathorn1973/twist-j/blob/6ffde281e82ad094bfefae17a2a6a25ac9b2a388/probes/P-FIELD-CHAIN-UNIT-SEED-AUDIT-2/PROOF.md).
- [C proof](https://github.com/mathorn1973/twist-j/blob/ed635a114bc52c4abbc16ea660bd4d89f2d2efde/probes/P-FIELD-CELL-SHEAR-CENSUS-1/PROOF.md) and [RC comparison](https://github.com/mathorn1973/twist-j/blob/35242926001bf48d03b78cedbb2daea814c992ff/probes/P-FIELD-CELL-SHEAR-CENSUS-AUDIT-1/COMPARISON.md).
- [D additive errata](https://github.com/mathorn1973/twist-j/blob/c7b5be4634738738c85c936227bfe68b99ec3b7a/notes/C-V103-SOURCE-INTERFACE-N/ERRATA.md) and [RD independent proof](https://github.com/mathorn1973/twist-j/blob/2a43c0312af7189b84c099c9482b908ac8e9323b/notes/C-V103-SOURCE-INTERFACE-REVIEW-N/PROOF.md).
