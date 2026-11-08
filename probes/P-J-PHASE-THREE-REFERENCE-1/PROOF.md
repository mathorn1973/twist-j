# Five phases through three shared references and one funded receiver

```text
Author: A. M. Thorn
License: Apache-2.0
SPDX-License-Identifier: Apache-2.0
Visibility: PUBLIC
Scientific status: NON-CANONICAL, L1, candidate-T
Evidence status: AUTHORED_PROOF / SAME_SESSION_STATIC_REVIEW
Independent review: PENDING
Probe: P-J-PHASE-THREE-REFERENCE-1
Reservation: https://github.com/mathorn1973/twist-j/issues/1580
Public authority: Public Canon v103
Public authority base: dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d
Date: 2026-10-17
```

This proof concerns a fixed finite composition in the declared extended
contact architecture. It makes no Canon promotion. Its algebraic
statements are separate from the probe's execution evidence. External
reports of the PR #1579 review, including wider checks at capacity B=2,
are provenance only; their unseen files and results are not premises here.

## 1. Definitions and exact scope

A native cell is `(a,b,c,d,q,r)` in F5^6. Its first four coordinates
represent the row-major piston matrix `[[a,b],[c,d]]`. All native
arithmetic below is in F5. The marked coefficient basis
`(1,j,j^2,j^3)` gives the five source pistons, in order,

\[
p_0=(1,0,0,0),\quad p_1=(0,1,0,0),\quad
p_2=(0,0,1,0),\quad p_3=(0,0,0,1),\quad
p_4=(4,4,4,4).
\]

The last equality uses `j^4=-1-j-j^2-j^3`. Every piston sum is 1
modulo 5. Consequently all five sources with common `(q,r)=(0,1)`
have the same native quotient `Q=(2,0,1)`, where
`Q(x)=(sum(x),q,r)`. This quotient loses the entire five-valued phase.

For a source piston X and reference piston Y, use the existing predicate

\[
h(X,Y)=\frac{\det(X+Y)-\det X-\det Y}{2},\qquad
\delta_Y(X)=1-h(X,Y)^4.
\]

Thus delta is 1 exactly when h is zero. The gates W_b and Ucal, the
complete CONTACT-RECORD word, and whole-cell CSUM are the declared
operations used here. Their native admission, physical realization,
preparation cost and autonomous control are not derived by this proof.

The reference minimum proved below applies to the class in which each
complete reference read contributes only this binary delta, and the
receiver data factor through the list of those bits. It is not a lower
bound for all possible piston readers or all TWIST-J contacts.

## 2. Complete reference census and the meaning of orientation

Write `Y=(u,v,w,z)`. Direct determinant polarization gives

\[
(h(p_0,Y),\ldots,h(p_4,Y))
=\tfrac12(z,-w,-v,u,v+w-u-z).
\]

This is a linear bijection from F5^4 to the hyperplane

\[
\mathcal H=\{(h_0,\ldots,h_4):\textstyle\sum h_i=0\}.
\]

Indeed its inverse is `u=2h_3`, `v=-2h_2`, `w=-2h_1`, `z=2h_0`;
the remaining coordinate is fixed by the zero sum. Therefore the census
of all 625 piston references is an exact zero-pattern count in H.

Let A_s be the number of ordered s-tuples of nonzero F5 elements whose
sum is zero. Then `A_0=1`, and

\[
A_s=4^{s-1}-A_{s-1}
=\frac{4^s+4(-1)^s}{5}\quad(s\ge1).
\]

The recurrence follows by choosing the first s-1 nonzero entries: the
forced last entry is nonzero exactly when their sum is nonzero. In
particular,

\[
A_1=0,\quad A_2=4,\quad A_3=12,\quad A_4=52,\quad A_5=204.
\]

For each prescribed set of s nonzero h coordinates there are exactly
A_s references. The total is
`1+10*4+10*12+5*52+204=625`. The constant delta masks are the single
all-zero h tuple, with mask `11111`, and the A_5 tuples with no zero h
coordinate, with mask `00000`: exactly 205 references.

To distinguish j from j^4, exactly one of h_1,h_4 must vanish. With
`h_1=0` and `h_4!=0`, choose h_4 in four ways and h_2,h_3 in 25 ways;
h_0 is forced. Interchanging 1 and 4 gives 200 references in total.

To distinguish both conjugate pairs `(j,j^4)` and `(j^2,j^3)`, select
which member of each pair has h=0. Each of the four selections leaves
two nonzero coordinates with 4^2 choices; h_0 is again forced. Hence
exactly 64 references separate both pairs. Their four restrictions to
indices 1,2,3,4 are the four sign patterns
`sgn(sin(2*pi*m*k/5))`, for `m=1,2,3,4`, with 16 references per
pattern when delta=1 names the positive half. This is a statement about
the marked complex embeddings. The identity is not an absent signal,
and its delta is not fixed by this four-point orientation condition.
Also `Y -> -Y` sends h to -h and leaves delta unchanged.

## 3. A fixed determinant-one triple and the restricted minimum

Choose, once for the entire five-phase family,

\[
Y_A=(0,2,2,0),\qquad Y_B=(4,2,2,0),\qquad
Y_C=(1,1,0,1).
\]

All three determinants are 1 in F5. The formula in Section 2 gives

| Source | delta_A | delta_B | delta_C | M=delta_A+2 delta_B+4 delta_C |
|---|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 | 3 |
| j | 0 | 0 | 1 | 4 |
| j^2 | 0 | 0 | 0 | 0 |
| j^3 | 1 | 0 | 0 | 1 |
| j^4 | 0 | 1 | 0 | 2 |

These five M values are distinct, and the phase index is

\[
k=(M+2)\bmod5.
\]

Two binary reference outcomes permit at most four distinguishable
outputs. Thus fewer than three cannot identify five phases in the
bit-factor class of Section 1. The displayed triple attains three.
This is a minimum number of binary results (also of worst-case binary
queries), not a minimum number of physical reference cells: a cell could
be prepared again if a separate admissible preparation rule supplied it.
The choice is common to every input, but no physical principle selecting
this reference triple has been derived. M encodes the five displayed
bit tuples; it is not an injective encoding of all eight arbitrary
three-bit tuples into F5.

## 4. Complete contact, including occupied reference fibres

For clarity, the original local letters used by CONTACT-RECORD are

\[
\begin{aligned}
b(a,b,c,d,q,r)&=(-c,-d,-a,-b,-q,-r),\\
d(a,b,c,d,q,r)&=(2-a,1-b,3-c,4-d,1-q,1-r),\\
e(a,b,c,d,q,r)&=(2-a,1-b,3-c,4-d,2-q,1-r).
\end{aligned}
\]

Products of maps in equations act right to left. Put `B=b_x b_y`.
It sends h to -h. The existing W_b fixes h=0; for h nonzero it sets
the shared bit eta to `sigma(h)=1_{h in {3,4}}` and applies B precisely
when the previous eta differs from sigma(h). This is an involution.
Direct substitution in its two branches shows that

\[
E=W_b B W_b=
\begin{cases}
B,&h=0,\\
\text{flip eta and fix all native coordinates},&h\ne0.
\end{cases}
\]

The map `tau_y=e_y d_y` translates only q_y by +1. Hence the existing
commutator `K_y=E tau_y E tau_y^{-1}` translates only q_y by
`-2 delta=3 delta`. Every other coordinate, including eta, is restored.

Let Ucal_y replace r_y by P_(q_y)(r_y), where

\[
P_0=(1\;2),\quad P_1=I,\quad P_2=(0\;2),\quad
P_3=P_4=(0\;1)
\]

as permutations of F5, fixing the unlisted elements. The complete
`A_y=Ucal_y K_y Ucal_y` therefore has the global endpoint map

\[
q_y'=q_y+3\delta,\qquad
r_y'=P_{q_y+3\delta}P_{q_y}(r_y),
\]

and fixes the source, both piston matrices and eta. Its inverse replaces
`+3 delta` by `-3 delta` in that formula. This holds for every occupied
reference q_y,r_y and either eta, not just a clean reference.

The literal chronological word is

```text
Ucal_y, e_y, d_y, W_b, b_x, b_y, W_b,
d_y, e_y, W_b, b_y, b_x, W_b, Ucal_y.
```

All its leaves are involutions, so its literal inverse is the reversed
list. In the common clean reference `(Y,0,0)`, the endpoint is
`(Y,3 delta,delta)`, since `P_0(0)=0` and `P_3(0)=1`.

## 5. Shared compute, CSUM and uncompute

Whole-cell CSUM is `(y,C) -> (y,C+y)` on F5^6. It leaves its control
cell y unchanged. For a fixed integer weight w, consider the
chronological block

\[
A_y\ ;\ \operatorname{CSUM}_{y\to C}^{\,w}\ ;\ A_y^{-1}.
\]

On arbitrary occupied y=(Y,q,r), arbitrary source s, eta and collector
C, its exact map is

\[
(s,y,\eta,C)\longmapsto
\bigl(s,y,\eta,
C+w(Y,q+3\delta,P_{q+3\delta}P_q(r))\bigr).
\]

CSUM has not altered any input of the subsequent inverse contact. Thus
the full source, reference and shared bit are restored, including on
occupied fibres. This is a bijection on the full block carrier.

For clean references the accumulated contribution is
`w(Y,3 delta,delta)`. Initialize each collector to the same source-free
cell

\[
Z=(4,0,4,2,0,0).
\]

The fixed piston calibration is

\[
Y_A+2Y_B+4Y_C=(2,0,1,4),\qquad
Z_p+Y_A+2Y_B+4Y_C=(1,0,0,1).
\]

Consequently the three blocks with weights 1,2,4 produce the actual
collector endpoint

\[
C(M)=(1,0,0,1,3M,M).
\]

There is no assignment of a precomputed delta, M, contact endpoint or
classical source vector. The fixed literal blocks create the collector
coordinates. The same references and eta are restored after every block
and are reused for the second source.

## 6. One joined carrier and the unchanged downstream apparatus

The joined native carrier consists of seven actual cells: two original
sources, three reference cells and the two collectors. There is one
shared bit. Thus its native part is `F5^42 x {0,1}`. The two collectors
are exactly the old apparatus heads x_A,x_B, with no duplicate handoff
copy. The remaining old apparatus state consists of its wave and tape
coordinates, counters, ledger, signs and buffer d.

Both complete phase messages are present in the common preparation.
Their source fibres are `(q,r)=(0,1)`. The three reference fibres are
`(0,0)`, both collectors are Z, eta=0, all wave and tape coordinates
are zero, n=c=k=0, W=0, b=B=5, both contact signs are +1, and d=(0,0).
All these choices except the two original phase pistons are common to
the 25 ordered source pairs.

Execute the three blocks for source A and then the same three blocks
for source B. Each uses its own collector and the shared references and
bit. A source takes `3*(14+14)+(1+2+4)=91` declared primitive leaves;
both take 182. These are 96 original local letters, 48 W_b leaves,
24 Ucal leaves and 14 CSUM leaves. The prefix fixes the old apparatus
coordinates other than its two heads and does not advance n or c.

At its endpoint all original sources, references and eta are restored.
They then remain spectators. Execute the old seven coupled steps
without changing their maps, source lift, injection, buffer, tape
updates, reader or port. The eight `(n,c)` boundaries are

```text
(0,0),(1,1),(1,2),(2,3),(3,4),(3,5),(4,6),(5,7).
```

The fixed 182-leaf prefix is externally addressed. Its autonomous
compilation is not supplied. The second original source is not a fresh
message arriving after the first record. No classical archive reset is
used inside the construction, and indefinite apparatus reuse is not
claimed.

## 7. Actual native outputs and a common energy bound

At n=0, the native selector on C(M) is `2+4M mod5`. Substitution in the
unchanged five generators and balanced lift `ell=(0,1,2,-2,-1)` gives:

| M | Selected generator | Actual (q,r) after U | z=eta_lift(q,r) | Cold energy e |
|---:|---:|---|---|---:|
| 0 | 2 | (1,0) | (1/2,1/2,0,0) | 3/20 |
| 1 | 1 | (2,4) | (1,0,0,0) | 2/5 |
| 2 | 0 | (1,2) | (1/2,3/2,0,0) | 17/20 |
| 3 | 4 | (3,3) | (-1,-1/2,0,0) | 2/5 |
| 4 | 3 | (4,2) | (-1/2,3/2,0,0) | 23/20 |

These are the vectors used by the old first contact and by the captured
second-source buffer. In particular, they are evaluated after the
actual native step, not at the earlier collector endpoint.

The unchanged S places `z_i-s/5` at its four ports and `-s/5` at the
fifth site, where `s=sum(z)`. Thus

\[
S^TS=I-\tfrac15\mathbf1\mathbf1^T,\qquad
e(z)=\tfrac12\|Sz\|^2.
\]

This proves the five displayed cold energies. The complete classical
energy, with the old wave coordinates u,v and four tape vectors, is

\[
E=\tfrac12(\|u\|^2+\|v\|^2-u^THv)
+2(\|A_0\|^2+\|A_1\|^2+\|B_0\|^2+\|B_1\|^2).
\]

### 7.1 Positivity and free/tape conservation from primary definitions

H is symmetric, with diagonal 10/9. Its shell multiplicities
`12,6,12,24,6` and weights `6,1,15,1,1`, divided by 324, give total
off-diagonal weight 8/9. The finite Dirichlet restriction removes
entries, so every absolute row sum is at most 2. Therefore `||H||<=2`
and `|u^T H v|<=2||u||||v||`, proving E is nonnegative.

Let P insert a four-vector at the ports, `K=(I+PP^T)^{-1}` and
`J0=I-PP^T`. The unchanged free update has

\[
w=K(Hv-J0u+4PA_0),\qquad
b_{\rm out}=A_0-\tfrac12P^T(w-u).
\]

It sends `(u,v)` to `(v,w)` and replaces the outgoing tape entry A_0
by b_out while permuting the other three tape entries. Rearrangement
gives

\[
w+u-Hv=2P(A_0+b_{\rm out}),\qquad
P^T(w-u)=2(A_0-b_{\rm out}).
\]

Hence

\[
\Delta E_{\rm wave}
=\tfrac12(w-u)^T(w+u-Hv)
=2(\|A_0\|^2-\|b_{\rm out}\|^2).
\]

The tape energy changes by the opposite amount. This proves exact
conservation by F, directly from its complete update equations.

### 7.2 Both funded guards accept

The square root of the nonnegative quadratic E is a seminorm. A cold
first kick has energy e_A at most 23/20 and is accepted from b=B=5.
After two F updates its energy is still e_A. Adding the second cold
kick gives a candidate state satisfying

\[
0\le E_{\rm cand}
\le(\sqrt{e_A}+\sqrt{e_B})^2
\le\frac{23}{5}<5.
\]

The funded contact records exactly the energy change in W and subtracts
it from b. Thus `E=W` and `b+W=5` hold from the initial cold state, and
the second candidate balance is

\[
b_{\rm cand}=5-E_{\rm cand}\in[2/5,5].
\]

Both guards accept for every ordered phase pair, including cases with a
negative second energy increment. Both final acceptance signs are -1.
The bound 23/5 is an a priori upper bound, not an assertion that a
trajectory attains it.

This single account pays for the unchanged classical wave/tape contacts.
It assigns no energy to reference preparation, W_b, Ucal, CSUM, the
182-leaf prefix or its control. A complete physical energy account for
those operations remains open.

## 8. Exact record-only inversion for all five source vectors

Let V(z) denote a cold vector state with `u=0`, `v=Sz` and zero tape
vectors. Both contacts accept, so the final vector state is exactly

\[
F^4V(z_A)+F^2V(z_B).
\]

Clock coordinates are not being added in this expression; it describes
only the rational wave/tape coordinates. Let R0 z be the first tape
output of V(z), and D2 z its third tape output. The literal tape shifts
then give the actual final readout pair

\[
b_0=A_0^{\rm final}=R0z_A,\qquad
b_2=B_1^{\rm final}=D2z_A+R0z_B.
\]

The first two tape cuts are retained at final A_0,A_1. Their values
depend only on the first source and remain unchanged through the second
contact and the subsequent tape shifts. This is retention in the same
occupied archive, with no reset between uses.

### 8.1 Direct invertibility of R0

The five injection sites are
`(0,0,0),(1,1,0),(1,0,1),(0,1,1),(2,0,0)`; the first four are ports.
All off-diagonal squared distances among those four ports are 2, so

\[
P^THP=\tfrac{59}{54}I+\tfrac1{54}\mathbf1\mathbf1^T.
\]

Their couplings to the fifth site are `(1/324,1/54,1/54,0)^T`.
Consequently the primary definitions of H and S imply

\[
P^THS=\tfrac{59}{54}I+\gamma\mathbf1^T,\qquad
\gamma=-\tfrac1{1620}(349,354,354,348)^T.
\]

For a cold V(z), the first free step gives
`b_out=-(1/2)P^T K H S z=-(1/4)P^T H S z`. Thus

\[
R0=-\tfrac14P^THS,\qquad
\det R0=
\left(\tfrac14\right)^4
\left(\tfrac{59}{54}\right)^3\tfrac{73}{324}>0,
\]

using `59/54+1^T gamma=73/324`. This establishes invertibility without
assuming that the heads belong to the old helper's initial ready family.

### 8.2 The existing reader and a fixed phase decoder

The unchanged typed direct reader, given only the final `(b0,b2)` and
acceptance signs, therefore returns

\[
z_A=R0^{-1}b_0,\qquad
z_B=R0^{-1}(b_2-D2z_A).
\]

The buffer d is omitted from its record. Original sources, references,
native heads, eta and phase indices are not reader inputs. The five
z(M) vectors in Section 7 are distinct; a fixed lookup recovers each M
and then `k=(M+2) mod5`. Thus the 25 ordered phase pairs give 25 distinct
retained record pairs. The general vector identity above supplies the
reader's justification; the original `recognize_ready_image` and
`recover_prepared_inputs` helpers are not used.

## 9. Exact negative control and boundaries of the result

Delete every W_b from A_y and use the inverse of that same deleted word
after CSUM. Its chronological forward list is

```text
Ucal_y, e_y, d_y, b_x, b_y, d_y, e_y, b_y, b_x, Ucal_y.
```

The two b_x maps commute past all y-local maps and cancel. On y,
`e;d` translates q by -1, the next b negates it, `d;e` translates it
by +1, and the last b negates it. The net translation is +3; the
pistons and the intermediate r are restored. Hence the deleted word
has the global endpoint

\[
(q,r)\longmapsto(q+3,P_{q+3}P_q(r)),
\]

independently of the source. It is precisely the complete A_y map with
delta forced to 1. Its paired inverse restores the shared resources.
All three controls therefore contribute 1, so every collector has
`M=1+2+4=2 mod5`. The entire downstream apparatus is identical for all
25 source pairs and coincides with the positive construction's
`(j^4,j^4)` downstream input. This is a proof about this explicitly
deleted word, not a classification of all contacts lacking W_b.

Separately, a zero piston source outside the promised phase family has
`h=0` against every reference, hence bits `111` and the same M=2 as
j^4. The displayed phase decoder would return k=4. Therefore the
construction does not detect absence, and phase identity 1 is not
absence. It does not infer a time-frequency sign from a static phase.

The conditional closure proved here is: two simultaneously prepared
five-valued phase messages are transferred through the actual declared
contacts into the same old apparatus, retained across its two uses and
recovered from its original record port, using three restored reference
cells, one restored shared bit and one classical budget B=5. Native
admission, physical realization, full prefix energy and autonomous
prefix scheduling remain open.

## 10. Second implementation audit

The new verifier includes a second wave/tape implementation, SparseWave,
written in the same session from the primary update equations. It uses
dictionaries indexed by spatial points. It constructs each stencil
shell from coordinate permutations and sign choices, derives
`Y+B_zero+B_zero` directly, and compares this set with the frozen
DOMAIN.tsv data. Its propagation, source injection and energy functions
do not call the old geometry, H, F, energy or reader helpers.

At a port its scalar update is `w=Hv/2+2*A0`; away from the ports it
is `w=Hv-u`. It then computes the outgoing tape value and the four tape
shifts directly. The frozen audit is specified to compare both complete
wave vectors, all four tape vectors, the tape pointer and the exact
energy at all eight boundaries for each of the 25 ordered phase pairs:
200 full boundary comparisons. Its second trajectory follows the
source-independent seven-step schedule and the two fixed accepted
source vectors. It does not reconstruct a trajectory by calling the
old apparatus transition.

The same implementation independently forms the four columns of
`P^T H S` from its own source and stencil maps. It compares them with
the closed matrix in Section 8, checks the rank-one determinant factor,
and compares `-(1/4)P^T H S` with the old response R0. The original
typed reader remains the reader under examination; no claim is made
that SparseWave is a second implementation of that reader.

This is a second implementation and a same-session check, not an
independent-author review. The comparisons are specified audit targets;
their execution and outcome belong to the result record after the
public pin.

## 11. Public dependencies and execution boundary

The normative base is the full commit recorded in the header. The
definitions `DEF-RESIDUAL-CONTACT-ARCHITECTURE` and `CONTACT-RECORD`
are read from
[canon/CANON.md](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/canon/CANON.md).
They supply the declared contact carrier, local maps, mixed predicate,
W_b, Ucal, whole-cell CSUM and complete contact maps.

The unchanged runtime dependencies are:

- [probes/P-CONTACT-RECORD-1/verify.py](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/probes/P-CONTACT-RECORD-1/verify.py),
  SHA256 `99ea8680db65567fb73e78f074841532802e6398dfbd34077b37914024341134`.
- [probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/apparatus.py](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/apparatus.py),
  SHA256 `f0edfd80157c8993322a5338e88120c552908d3830fe5f9ea7536257213c6173`.
- [probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/DOMAIN.tsv](https://github.com/mathorn1973/twist-j/blob/dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d/probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/DOMAIN.tsv),
  SHA256 `2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0`.

The contact verifier is used for its literal maps, without invoking its
own main program. This document was derived and statically checked
without scientific execution. The frozen probe verifier and subsequent
result record must separately establish which literal paths were run,
their source pins and their exact outputs. No finite execution is
silently substituted for the global arguments above, and source reuse
is not independent review.
