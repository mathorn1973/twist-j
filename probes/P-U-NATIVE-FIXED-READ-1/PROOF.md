# Native arithmetic with fixed local readings

Status: PUBLIC, NON-CANONICAL, candidate-T, L1.
Author: A. M. Thorn. Original proof and code: Apache-2.0.
The formal execution record is separate from the proof.
Reservation: [#1429](https://github.com/mathorn1973/twist-j/issues/1429).

## 1. Result and scope

One original cell can change an independently occupied receiver by its
actual first native ticks while using the same fixed local reading before
and after the change. The receiver result then remains readable forever.
Two explicitly prepared scalar effects are

\[
P:\ (x,y)\longmapsto(x,3y+3x),\qquad
Q:\ (a,y)\longmapsto(a,2y+4a).
\]

The same source code and the same source and receiver readers serve both.
A fixed local reader in the existing receiver coordinates distinguishes
these two preparation contexts at the input, at the output and throughout
the later continuation. It is not a valid context reading at every internal
tick.

There is also a same-reader persistent SUM on an independently occupied
receiver. For a precisely declared affine preparation class we prove
completeness: twenty maps, of which four satisfy the stated zero-offset,
coefficient-sum-one condition.

All these are preparation-to-reading results on one six-coordinate cell.
The scalar effects agree with the coefficients used in
[relative-contact chronology PR #1428](https://github.com/mathorn1973/twist-j/pull/1428)
at head 9de862afafd02ea3e49daf6e4567127dc2a01f2c. They do not implement its
complete gates on three independently evolving six-coordinate cells.
The actual output is not a ready input for the next factor.

The negative results below delimit two natural ways of composing a full
relative contact. They do not establish a universal physical impossibility.
The separate [varying-trace proof](VARIABLE-TRACE.md) excludes the fibre
receiver even for nonlinear preparations. The [affine three-pair proof](AFFINE-THREE-PORT.md)
excludes every two-plus-two-plus-two affine product preparation at every
fixed origin-zero duration, while allowing arbitrary nonlinear readers.

## 2. The unchanged source law

All coordinates and displayed scalar equations are in F5. Write

\[
v=(p_1,p_4,p'_1,p'_4,q,r)=(a_0,b_0,c_0,d_0,q,r)
\]

when convenient; coordinate letters with subscripts are not generator names.
The five original generators are

\[
\begin{aligned}
a(v)&=(p_4,p_1,p'_4,p'_1,q,r),\\
b(v)&=(-p'_1,-p'_4,-p_1,-p_4,-q,-r),\\
c(v)&=(2-p'_1,1-p'_4+r,2-p_1,1-p_4-r,1-q,-r),\\
d(v)&=(2-p_1,1-p_4,3-p'_1,4-p'_4,1-q,1-r),\\
e(v)&=(2-p_1,1-p_4,3-p'_1,4-p'_4,2-q,1-r).
\end{aligned}
\]

Let z be the sum of all six coordinates and H_z its trace sheet. The complete
state is (n,v), and

\[
U(n,v)=(n+1,g_{z(v)+2\theta_n}(v)),\quad
(g_0,\ldots,g_4)=(a,b,c,d,e),\quad
\theta_n=\operatorname{popcount}(n)\bmod2.
\]

The source is the immutable
[Public Canon v100 tree](https://github.com/mathorn1973/twist-j/tree/c164b79ce134152ac7cd600421791df74113f29f/canon).
No generator can be chosen merely because it would give the desired answer.

The two induced trace maps, listed in input order 0,1,2,3,4, are

\[
\tau_0=(0,4,0,4,4),\qquad\tau_1=(2,1,1,3,1).
\]

The actual origin-zero bits are 011. They yield:

| Initial trace | Chronological word | Trace after three ticks |
| ---: | --- | ---: |
| 0 | a,c,e | 1 |
| 1 | b,b,d | 1 |
| 2 | c,c,e | 1 |
| 3 | d,b,d | 1 |
| 4 | e,b,d | 1 |

Consequently every origin-zero state lies in H1 after three ticks.
On H1 union H4 every subsequent selected generator is b,d or e, and
the next trace is 4-3 theta. This is the known synchronization theorem.

On the entire H0, the actual three-tick map is the full affine word

\[
\boxed{
F=e\circ c\circ a,\quad
F(a_0,b_0,c_0,d_0,q,r)
=(d_0,c_0-r,b_0+1,a_0+r+3,q+1,r+1).
}
\tag{1}
\]

This identity and the earlier controlled translation are inherited from
[#1001](https://github.com/mathorn1973/twist-j/issues/1001#issuecomment-5666743909).
As an affine word (1) is defined on all F5^6; it is the actual origin-zero
U^3 only on H0. The source dynamics is not asserted to be globally bijective
across all initial trace sheets.

Put S=p1+p4+p1p+p4p. Directly from (1),

\[
\boxed{S(Fv)=S(v)+4.}
\tag{2}
\]

In particular the sign-reversed expression 4-S is not the general formula.
The later b,d,e each give S'=-S.

## 3. Shared local readers

Define

\[
\boxed{X(v)=2(r-q)+1}
\tag{3}
\]

on the two fibre coordinates and

\[
\boxed{
M(v)=2[(p_1-1)(p_4-3)+(p'_1-4)(p'_4-2)]
}
\tag{4}
\]

on the four piston coordinates. These are one fixed pair of functions,
not different input/output decoding charts.

The shared source preparation for a symbol u is

\[
(q,r)=(u+4,4u+1).
\tag{5}
\]

It has q+r=0 and X=u. Formula (1) translates both q and r by one, so X
is unchanged across the complete shot. Receiver preparations below depend
only on y; no source value is loaded into the initial receiver.

### Protected receiver value

Center the pistons at their common b,d,e fixed point:

\[
U_1=p_1-1,\quad U_2=p_4-3,\quad
V_1=p'_1-4,\quad V_2=p'_4-2.
\]

The complete piston actions are

\[
b:(U,V)\mapsto(-V,-U),\qquad
d,e:(U,V)\mapsto(-U,-V).
\tag{6}
\]

Therefore

\[
M=2(U_1U_2+V_1V_2)
\]

is invariant under all three. If an output has S=4, its continuation has
S=+1 or -1, and M remains unchanged for every later actual time.

This is an application of the existing protected native record, not a new
classification of invariants. For the canonical four-vector
W=(U+V,chi(z)(U-V)), chi(1)=1, chi(4)=-1,

\[
M=W_1W_2+W_3W_4.
\]

The canonical invariant and no-later-permanent-write result are in
[MEMORY-PROOF.md](https://github.com/mathorn1973/twist-j/blob/c164b79ce134152ac7cd600421791df74113f29f/probes/P-U-NATIVE-MEMORY-EVENT-1/MEMORY-PROOF.md).

## 4. Two actual native scalar effects

### 4.1 P

For all independent x,y take

\[
E_P(x,y)=(4y+3,3,y+4,0,x+4,4x+1).
\tag{7}
\]

Both S and q+r are zero. Substitution gives X=x and M=y.
The full selected output, retaining all six coordinates, is

\[
F E_P(x,y)
=(0,x+y+3,4,4x+4y+2,x,4x+2).
\tag{8}
\]

Hence

\[
X'=x,\qquad M'=3y+3x.
\tag{9}
\]

The result M'=3y+3x remains at every later n>=3 by (6).

### 4.2 Q, with exactly the same source preparation and readers

For all independent a,y take

\[
E_Q(a,y)=(2y,3,3y+4,3,a+4,4a+1).
\tag{10}
\]

Again S=q+r=0, X=a and M=y. The actual output is

\[
F E_Q(a,y)
=(3,3y+a+3,4,2y+4a+4,a,4a+2).
\tag{11}
\]

It gives

\[
X'=a,\qquad M'=2y+4a,
\tag{12}
\]

and this receiver result is permanent under subsequent U.

There are 25 independent preparations in each displayed family. The native
law, clock prefix, source code and readers are common. Only the receiver
preparation code differs.

### 4.3 Precise source and reuse limits

X is preserved from time zero to time three. It is not a permanent local
source record: the next actual generator is b and gives X'=2-X.

The ready receiver has S=0, whereas every output has S=4. Every later
native generator on these states gives S'=-S. Thus waiting cannot restore
the ready S=0 code. In particular, the result of P has not been converted
into the input state required by Q. Its permanently stored M also cannot
undergo a second nontrivial write under these later native steps.

These are exact mathematical obstructions to that proposed reuse. A
different carrier, actual re-encoding or additional interaction would need
its own derivation and complete state account.

## 5. A context label in the existing receiver state

Use

\[
K=(p_1-1)^2+(p'_1-4)^2,\qquad
\boxed{T=(1-S^2)\,2p'_4+S^2\,2(K-1).}
\tag{13}
\]

This is a fixed function of the four receiver coordinates. On (7) it reads
T=0; on (10) it reads T=1, because initially S=0 and p4p is respectively
0 or 3.

At the full output, S=4. Formula (1) gives p1'=d0 and p1p'=b0+1=4
on these two families. Thus K'=1 for P and K'=4 for Q, so T'=0 or 1
respectively.

Equation (6) only negates or exchanges the centered coordinates entering K.
It preserves K, while S'=-S preserves S^2. Therefore the same T retains
the respective value for all n>=3. No additional state coordinate or
external retained bit has been added.

On this 50-point independent preparation family the exact endpoint law is

\[
\boxed{
(X',M',T')
=\left(X,(3-T)M+(3+T)X,T\right).
}
\tag{14}
\]

### Why context matters

Without T there is an exact failure of autonomous endpoint reading:

| Preparation | Input (X,M) | Actual full output | Output M |
| --- | --- | --- | ---: |
| (3,3,4,0,0,0), P | (1,0) | (0,4,4,1,1,1) | 3 |
| (0,3,4,3,0,0), Q | (1,0) | (3,4,4,3,1,1) | 4 |

One function of (X,M) cannot produce both required outputs. Formula (13)
provides a concrete context reading for precisely these native preparations.

### Internal ticks and autonomous continuation

T is not an uninterrupted binary pointer. At the first internal a step it is

\[
T_1=2y+3\quad(P),\qquad T_1=y+3\quad(Q).
\]

At the second c step it has returned to 0 or 1. For the first row of the
counterexample its readings at times 0,1,2,3 are exactly (0,3,0,0).
The complete intermediate raw states are retained by the actual U law.

Formula (14) is a preparation-to-output equation at the specified endpoints.
It is not a time-independent evolution law that can be repeatedly applied
to the same three read values. Its next application would generally
change M, whereas true later U preserves M. Adding T resolves this
preparation-choice ambiguity; it does not erase the launch/continuation
distinction or prove physical access to the reader.

This context is also not identified with the direct/alternative energetic
contacts from PR #1424. Such an identification would require a separate
map between the complete models.

## 6. Persistent occupied-receiver SUM

For all independent s,t in F5 define

\[
E_{\rm SUM}(s,t)=(t,0,-t,0,-s,s),
\quad \sigma=3(r-q),
\quad L=p_1+p'_4,
\]

\[
\boxed{R=(1-S^2)L+S^2M.}
\tag{15}
\]

On the input S=0, so R=L=t and sigma=s. The entire actual output is

\[
F E_{\rm SUM}(s,t)
=(0,-t-s,1,t+s+3,1-s,1+s).
\tag{16}
\]

Here S=4, sigma=s and

\[
M=2[(-1)(-t-s-3)+(-3)(t+s+1)]=t+s.
\]

Consequently R=t+s. Subsequent b,d,e preserve M and S^2=1, giving

\[
\boxed{R(U^n E_{\rm SUM}(s,t))=t+s\quad\text{for every }n\ge3.}
\tag{17}
\]

The same receiver reader thus reads the independent old value and the
persistent new sum. The receiver is not required to be blank. Source value
s=0 leaves its numeric content t unchanged; numeric zero is not an extra
absence flag or a detected-arrival condition.

For orientation, an affine but not permanently stable reading already
suffices across the endpoint: t_local=L-2S obeys t_local'=t_local+r
under the full affine word, by (2). The significance of (15) is its
permanent continuation with the same fixed local reader.

Earlier results supplied native blank writing with persistent reading
[#999](https://github.com/mathorn1973/twist-j/issues/999#issuecomment-5662855170)
and an occupied-receiver sum with different charts
[#1001](https://github.com/mathorn1973/twist-j/issues/1001#issuecomment-5666743909).
The conjunction in (15)-(17), rather than either predecessor alone,
is the claim here.

## 7. Complete affine receiver preparation classification

Fix (3)-(5). The classified domain is every affine receiver line

\[
p(y)=p^0+yv\in{\mathbb F}_5^4,\quad S(p(y))=0,\quad M(p(y))=y,
\tag{18}
\]

for which the native output is affine in the independent source and
receiver symbols:

\[
M(F(p(y),u+4,4u+1))=Ay+Bu+C.
\tag{19}
\]

The readers, source code, common initial S=0 and affine-output requirement
are premises. More general preparations and readers are not silently
included.

### 7.1 Necessary shape of every admitted line

On a zero-sum piston state (a0,b0,c0,d0), set r=1-u. Direct substitution into
(1) and (4) gives

\[
M'=2[(d_0-1)(c_0-4)+(b_0-3)(a_0+2)]
       +2(d_0-b_0+2)u.
\tag{20}
\]

Equivalently, on this S=0 sheet,

\[
M'-M=2c_0+b_0+4+2(d_0-b_0+2)u.
\tag{21}
\]

If v=(v1,v2,v3,v4), the coefficient of uy in (20) is
2(v4-v2). Requirement (19) forces v4=v2=t0. Since sum v=0,
v3=-v1-2t0. The y^2 coefficient in M(p0+yv) is then

\[
2(v_1v_2+v_3v_4)=-4t_0^2=t_0^2.
\]

Requirement M=y forces t0=0. Thus b0=b and d0=d are constants,
v3=-v1 and v2=v4=0.

Let

\[
B_0=b-d-1.
\]

The y coefficient of M is 2B0 v1. It equals one if and only if B0 is
nonzero and v1=(2B0)^{-1}. The constant term then uniquely fixes

\[
a_*=\frac{(b-3)+(b+d+4)(d-2)}{B_0}.
\]

Every possible preparation is therefore exactly

\[
\boxed{
p^0=(a_*,b,-a_*-b-d,d),\quad
v=((2B_0)^{-1},0,-(2B_0)^{-1},0),
\quad B_0\ne0.
}
\tag{22}
\]

There are five choices of b and four permitted choices of d: twenty maps.

### 7.2 Sufficiency and all output coefficients

Conversely, every map (22) has S=0 and M=y; substituting it into (21)
gives an affine output. Put h=d-b, so h is not 4. Its coefficients are

\[
\boxed{
A=\frac{h+2}{h+1},\qquad B=2(h+2),\qquad
C=3a_*+2b+3h-1.
}
\tag{23}
\]

This proves both necessity and sufficiency, including the offsets of
every map, without relying on a successful-case search.

### 7.3 The four coefficient-sum-one, zero-offset maps

Together, A+B=1 and C=0 mean that an equal input pair u=y retains that
same reading. This is an imposed normalization condition. The condition
A+B=1 is equivalent to

\[
\frac{h(2h+1)}{h+1}=0.
\]

Hence h=0 or h=2. At h=0 the gains are (A,B)=(2,4) and
C=4b^2+4b+2, which vanishes exactly at b=1,3. At h=2 the gains are
(3,3) and C=3(b^2+1), vanishing exactly at b=2,3.

The complete list is:

| Receiver p(y) | Effect |
| --- | --- |
| (4y+3,3,y+4,0) | 3y+3u |
| (4y+2,2,y+2,4) | 3y+3u |
| (2y,3,3y+4,3) | 2y+4u |
| (2y+3,1,3y,1) | 2y+4u |

These four maps are complete within (18)-(19) and the two additional
coefficient conditions. They are not four selected physical laws.
For example h=1 gives gains (4,1), while h=3 gives (0,0);
both occur in the full twenty-map class with their specified offsets.

## 8. Three independent raw subsystems on one common trace cannot give C_kappa

### 8.1 Exact contract

Let three nontrivial independently prepared symbols x,y,a occupy disjoint
raw-coordinate blocks of ONE original F5^6 cell. Any unused coordinates
are fixed. The entire Cartesian preparation family has a single initial
trace z. Source and reference must be locally retained, while the local
receiver must read

\[
C_\kappa:\ (x,y,a)\longmapsto(x,y+\kappa(x-a),a),
\qquad\kappa\ne0,
\tag{24}
\]

after one common finite number m of true native steps.

Local encoders and readers can be arbitrary, including nonlinear and
known-time-dependent output readers. They cannot jointly inspect other
blocks. All inputs are independent over the full F5^3. The same obstruction
also holds if retained donor values are separately bijectively relabelled.

### 8.2 The block sizes are forced

Independence and constant total trace force the sum of each block to be
constant separately: vary that block and hold every other coordinate fixed.
A one-coordinate block would then be constant and could not carry five
distinguishable symbols. Each of the three blocks needs at least two
coordinates. There are only six coordinates, so the partition is necessarily
2+2+2, with none unused.

### 8.3 Every common word has a restricted dependency form

The trace depends only on the prior trace and clock. A common initial
trace therefore gives the same selected generator word for every input
at any specified m.

Directly from the five generators, and by composition, every such word has

\[
p'=\varepsilon\Pi p+w r+b_*,\quad
q'=\varepsilon q+\gamma,\quad
r'=\varepsilon r+\delta,
\tag{25}
\]

where epsilon is +1 or -1, w,b* are four-vectors and

\[
\Pi\in
\{I,(12)(34),(13)(24),(14)(23)\}.
\]

Indeed the composition of two piston maps of this form is

\[
\varepsilon_2\varepsilon_1\Pi_2\Pi_1p+
(\varepsilon_2\Pi_2w_1+\varepsilon_1w_2)r+
\varepsilon_2\Pi_2b_1+w_2\delta_1+b_2,
\]

and q and r retain the same one-coordinate form. The four permutations
are closed under composition. Thus each output piston can depend on at
most one input piston and on r; q cannot feed any piston or r.

### 8.4 Necessary dependencies cannot coexist

To realize (24), source and reference outputs must each depend on their
own independent symbol. Receiver output must depend on all three symbols.
A local nonlinear reading cannot create a missing raw input dependency.

If Pi=I, a receiver pair depends only on its own inputs and on the block
containing r, so at most two symbols occur.

Every nonidentity Pi consists of two disjoint transpositions. Classify
the receiver pair:

- If it is (q,r), it has no external input.
- If it is r and one piston, only that piston's partner can add an external
  input; one donor is missing.
- If it is two pistons, dependence on its own y requires at least one
  partner to lie in the same pair. It must then contain one complete
  transposition. Its only possible external input is r.
- If it is q and piston j, receiver dependence on both other symbols
  requires Pi(j) and r to belong to different donor blocks. The donor
  block without r is a pair of pistons; to retain its own symbol it must
  contain a complete transposition. Among the three pistons outside j,
  the only complete transposition excludes Pi(j), whose partner j is
  already in the receiver. Therefore Pi(j) belongs to the r-containing
  donor block after all, a contradiction.

Every case fails. This proves the arbitrary-time theorem, not merely a
bound on a searched prefix. The 90 ordered partitions times four maximal
dependency graphs give a finite 360-case independent audit of the same
necessary condition. Giving every piston a possible r input only enlarges
the allowed graph, so failure of this enlarged class is sufficient.

The positive effects in Sections 4-6 use a two-plus-four partition with
two logical symbols. They do not contradict this three-subsystem theorem.

Varying initial traces, correlated preparations, noncoordinate subsystem
definitions, input-dependent stopping, extra carriers and new interactions
are outside this common-trace proof. See VARIABLE-TRACE.md for the fibre-receiver extension and
AFFINE-THREE-PORT.md for all affine preparations of three raw pairs.
The latter permits varying traces but keeps the two-plus-two-plus-two
partition; it does not classify other block sizes or nonlinear preparations.

## 9. Whole-cell permutations under a common native clock

A different possible construction uses several complete native cells rather
than parts of one cell. Suppose all cells evolve with a common clock and
are on the same synchronized trace sheet at some n>=3. Allow any finite
sequence of common native ticks and permutations of whole cells, even if
the permutation choice depends on all data. No other data-writing operation
is admitted.

This is a generous mathematical class: physically implementing the
permutations or their controller is not itself derived.

Let D_{n,m} be the common free native evolution across the actually elapsed
m ticks. On the current trace sheet it is a fixed affine bijection. For
each input and its actual finite branch there is a permutation pi such that

\[
\boxed{
(v_1,\ldots,v_N)_{\rm out}
=\pi\bigl(D_{n,m}v_1,\ldots,D_{n,m}v_N\bigr).
}
\tag{26}
\]

Proof is by induction: applying one common map to every cell commutes
with every whole-cell permutation. An adaptively chosen permutation is
still a particular permutation on the branch being considered. Different
elapsed times are compared with their own actual D_{n,m}.

After undoing that known common free continuation, the FULL multiset
of raw cell states is unchanged.

### Consequence for a relative contact and its helpers

Suppose the three data cells are required, in this free-evolution frame,
to change from (x,y,a) to (x,q,a), where

\[
q=y+\kappa(x-a).
\]

Let h be the multiset of helper states. Cancellation of the retained source
and reference in (26), valid even when some states coincide, forces

\[
\boxed{h_{\rm out}=h+\delta_y-\delta_q.}
\tag{27}
\]

Thus:

1. If every helper is returned, even just as a multiset, then q=y.
   For nonzero kappa a nontrivial relative contact cannot be realized.
2. If helpers may change and q differs from y, the initial helper bank
   must already contain q.
3. To work for every independent x,y,a in H_z with one data-independent
   bank, every q in H_z must be present in that bank.

For the last point, choose any y different from q in H_z and any a in H_z,
then x=a+kappa^{-1}(q-y) also lies in H_z. Therefore the necessary bound is

\[
\boxed{\#\text{helper cells}\ge |H_z|=5^5=3125.}
\tag{28}
\]

It is a bound for this whole-cell-permutation model, distinct from the
earlier Gauss-shell cycle-capacity bounds. It is not a claim that 3125
helpers supply a derived native controller. A controller that already
knows q can retrieve it from such a bank, but that assumes the computation
and selection being sought.

## 10. What the result contributes to a physical realization

The positive part replaces a previously assumed scalar operation by a
literal, fully specified native history on a prepared source/receiver
partition. It retains the occupied receiver's result with a fixed local
reading. It also displays a preparation-context label in the same raw
receiver coordinates.

The remaining obligations are concrete:

| Obligation | What is established here | What still needs a source derivation |
| --- | --- | --- |
| Native elementary effect | Actual first three ticks, all inputs of the declared codes | Repeated use on the actual output |
| Preparation | Explicit independent raw states and complete affine class | Their preparation and selection by an admitted physical mechanism |
| Readout | Fixed local polynomials, exact endpoint and retention laws | Available measuring access and calibration |
| Context | A retained P/Q preparation label in existing coordinates | A complete continuously operating apparatus context |
| Composition | Exact failure of the stated simple reuse and permutation routes | A nontrivial actual connection or re-encoding mechanism |
| Energy | No new energetic premise is inserted | Independently selected conserved quantity and physical units |
| Larger physical theory | No new conclusion | Coherence, occurrence, photon phase and empirical tests |

A mathematical function of a state is not by itself an available physical
instrument. The finite alphabet values are not energy units. Code
compatibility and conservation do not select a physical contact law.
Nothing here closes the energetic-law ambiguity in PR #1424 without an
additional explicit bridge.

The most immediate source question is now the mechanism that takes an
actual result into the ready input of a further interaction while accounting
for all other state and internal ticks. The proofs rule out stated simple
routes; they do not license silently adding the missing mechanism.

## 11. Proof, finite evidence and review

The equalities above are algebraic proofs over the whole declared domains.
The all-time retention statements use the stable alphabet and exact
invariants; the all-word exclusion uses the composition law (25).
The bank bound uses (26)-(27). The two analytic appendices use exact
raw-state collisions and, for affine preparations, a two-trace row-space
lemma. None is inferred from finite trajectory sampling.

The frozen audit separately checks all declared finite carriers and
preparation maps. It uses direct coordinate evaluation and independently
written homogeneous matrices. See PREREG.md for the exact domains,
REVIEW.md for author contributions and exposure, and RUN.md/RESULT.md
once the first public execution is completed.

The assistant reviewers know the prospective claims and contributed to
parts of the derivation. This is a separately documented assistant review
within a coordinated team, not blinded external scientific confirmation.
