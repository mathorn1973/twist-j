# Complete static transpositions and their exact limits

**NON-CANONICAL. Conditional candidate-T at L1; accompanying finite audits
are candidate-C.** No Canon, physical unit, source law or action-layer status
is promoted. The complete definitions, matrices and carriers are in the
unchanged PREREG.md; ADDENDUM-READOUT.md adds the two-history witness before
the first scientific execution. Together those files and this proof are
self-contained mathematical input, without requiring the uploaded programs.

## 1. Result and its scope

For each pair of vertex registers 01, 02 and 12, there is a complete static
contact that preserves the selected H1 energy and the full Gauss defect,
is an involution, and commutes with both the complete reaction G and the
field step F, including every rejection branch. It leaves the rational
active field coordinates unchanged.

The contact performs the unique defect-preserving static field proposal
exactly when the proposal is integral, its stock is nonnegative, and it
preserves whether G accepts. On an accepted reaction state the two funding
conditions reduce to

\[
\kappa\leq\min(r,r+\delta_G),\qquad
\delta_G=r(Gs)-r(s).
\]

For a fixed proposal this rule has the greatest possible nonidentity support
among all proposal-or-identity maps commuting with G. This class-relative
statement supplies a complete mathematical rule; it does not select that
proposal, maximal support, the occurrence of a contact, or H1 from a source.

Contacts 02 and 12 can have odd, nonzero field work despite commuting with F.
They preserve exactly c=1 in the declared family Hc. Moreover two complete
histories using S01 and S12 have exactly the same final cells, link and
pointer but receiver energy changes 81 and 86. Thus F-commutation alone
does not remove the need for readable contact context.

## 2. Algebra needed from the cell law

Write a cell as s=(m,b,E,M,r), with r nonnegative. All claims here are on the
complete integer carrier specified in PREREG.md. In particular G acceptance
means actual acceptance of the inherited complete reaction, not membership
in an accepted Gauss sector. Define

\[
H_{\rm raw}(E,M)=|E|^2+|M|^2+E^tCM,
\quad H_1=\sum_jQ(m_j)+\sum_jQ(b_j)+H_{\rm raw}+r.
\]

Every integer field has the unique rational split

\[
(E,M)=Py+S\sigma,\quad y=(a,b,c,d),\quad\sigma=(u,w),
\]

where P and S are the explicit maps in PREREG.md. In electric coordinates,
P is C acting on (a,b), and

\[
S_E(u,w)=(u,u,w,u-w),\quad C^tS_E=0,
\quad DS_E(u,w)=(2u+w,-3u+w,u-2w).
\]

Thus active and static electric parts are orthogonal, and direct substitution
gives

\[
H_{\rm raw}=H(y)+3u^2-2uw+2w^2
             =H(y)+E_C(DE),
\quad E_C(q)=\frac{q_0^2+q_1^2+2q_2^2}{5}.
\]

This identity uses q=DE, whose sum is zero. On a non-Gauss state it does not
replace q by the matter charge rho. The term involving M has no static
part because C^t S_E=0. No integrality of y or sigma is needed for this
energy split.

G fixes b and sigma. Its R branch sends (y,r)=(Lx,r) to
(x,r+4H(x)-2), and its AM branch performs the inverse. The two matter
energies are 18 and 20, and H(Lx)=5H(x); hence these stock increments preserve
H1. Integral-split, image and funding conditions are exactly those in the
specification. G is an involution: an accepted branch has a funded inverse,
while a rejected state is a full fixed point. In particular

\[
a_G(s)=1\ \Longleftrightarrow\ G(s)\ne s
\ \Longleftrightarrow\ \text{G changes its matter endpoint}.
\]

F fixes sigma and acts by A_f on y. Its raw inverse is

\[
M=M'+C^tE',\qquad E=(I-CC^t)E'-CM',
\]

so F is a complete integer bijection. Direct algebra also gives
H(A_f y)=H(y) and

\[
A_fL=LA_f=
\begin{pmatrix}
1&2&0&0\\2&-1&0&0\\0&0&1&2\\0&0&2&-1
\end{pmatrix}.
\]

A_f is an integer bijection. Indeed its block form is
`[[I,I],[-C^t C,I-C^t C]]`, a product of two integer triangular shears.
Consequently F preserves both the integral split lattice and L's image in
it, in both directions, as well as every reaction funding condition.
The accepted formulas commute by A_f L=L A_f, and the structural/funding
rejections remain rejections. This proves FG=GF on the complete carrier,
independently of any global uniqueness assertion in the supplied ZIP.
Since F fixes m, it also proves a_G(Fs)=a_G(s).

## 3. Unique static field proposal and its price (T1)

Swapping whole b_i,b_j fixes the sum of their Q energies and changes only
the indicated actual node charges. A field displacement d must satisfy

\[
C^td=0,\qquad Dd=\rho'-\rho
\]

to be static and preserve the Gauss defect. The kernel of C^t is the
two-dimensional rational static space. The formula for DS_E above has
rank two onto the zero-sum charge plane. Hence the displacement is unique
over the rationals. Substitution yields precisely:

| Pair | t | k, with d=(t/5)k | Dk | squared norm |
|---|---|---|---|---:|
| 01 | chi(b0)-chi(b1) | (-2,-2,-1,-1) | (-5,5,0) | 10 |
| 02 | chi(b2)-chi(b0) | (1,1,3,-2) | (5,0,-5) | 15 |
| 12 | chi(b2)-chi(b1) | (-1,-1,2,-3) | (0,5,-5) | 15 |

Their static coordinates are (-2,-1), (1,3), and (-1,2), respectively.
Each k has a component of absolute value one, so an integer E produces
an integer E' exactly when 5 divides t. On that domain put n=t/5. Then

\[
\kappa=H_{\rm raw}(E+nk,M)-H_{\rm raw}(E,M)
       =n^2|k|^2+2nE\cdot k
       =E_C(DE')-E_C(DE).
\]

The missing mixed term is n k^t CM=0. Thus the price is an integer,
independent of the active coordinates and M. The proposal sets
r'=r-kappa. The energy definition and this compensation are premises
of the construction.

On applying the reverse register transposition, t becomes -t, the field
returns to E, and its price is -kappa. Every legal proposal therefore has
a legal reverse, including when it changes a nonzero initial stock.
The formulas for raw proposals also make sense with integer signed stocks;
that auxiliary algebra is used only to prove commutation. Physical carrier
outputs always retain nonnegative stocks.

## 4. Full completion and involution (T2, T3)

Let P_ij(s) denote the integral proposal with stock r-kappa when that stock
is nonnegative. Set

\[
S_{ij}(s)=
\begin{cases}
P_{ij}(s),& P_{ij}(s)\text{ exists and }a_G(P_{ij}(s))=a_G(s),\\
s,&\text{otherwise}.
\end{cases}
\]

The proposal preserves m, M and y. Its change of sigma is integral, so it
also preserves whether the rational split is integral; L-image eligibility
does not change. The legal edge relation is symmetric by proposal reversal,
and equality of its endpoint acceptance bits is symmetric. Each performed
edge is therefore traversed in both directions. A refused state is fixed
on every register. This proves S_ij squared is identity globally.

Every performed edge preserves H1 by the stock account and the complete
Gauss defect by Dd=rho'-rho. Refused edges change nothing. No restriction
to Gauss states, zero defects, empty stocks or literal reacting matter
is used in this argument.

## 5. Complete G-commutation, including all refusals (T2, T3)

For a structurally eligible reaction write delta for its algebraic stock
increment, whether or not funded. A static proposal preserves that delta:
it fixes y and m. G preserves kappa: it fixes b and sigma. Thus raw G and
raw P commute as algebraic formulas whenever their structural domains
apply. The acceptance filter is useful here because these specific raw
operations commute; acceptance equality alone is not a universal recipe
for making arbitrary operations commute.

First take a state accepted by G. Its stock and its G partner's stock are
r and r+delta, both nonnegative. After a proposal, the state and its G
partner would have stocks r-kappa and r+delta-kappa. Consequently the
contact is allowed exactly when it is integral and

\[
\kappa\le r,\qquad\kappa\le r+\delta.
\]

The four stocks in the reaction/contact square are

\[
\begin{array}{c|cc}
&\text{before contact}&\text{after contact}\\\hline
\text{before G}&r&r-\kappa\\
\text{after G}&r+\delta&r+\delta-\kappa.
\end{array}
\]

At Gs the increment of the inverse reaction is -delta. The condition
becomes kappa <= min(r+delta,r), exactly the same inequality. Therefore
the contact is performed at both ends of the G edge or refused at both.
When performed, the algebraic square commutes, including the matter
endpoint, electric and magnetic coordinates, b registers and stock.
When refused, both compositions are simply Gs. This argument includes
both a negative proposed stock and a funded proposal whose G corner is
unfunded; they are not omitted boundary cases.

Now take a G-rejected state. Gs=s. If the contact refuses, both
compositions equal s. If it acts, its acceptance-equality rule demands
that its output also be rejected, so G P(s)=P(s)=S G(s). This covers
nonliteral matter, a nonintegral split, a rejected image coset and failed
funding. A proposal sending a rejected state to an accepted one is fixed
instead. Hence S_ij G=G S_ij on the entire carrier.

## 6. F and recorded reaction (T2)

F fixes b, sigma and stock. Therefore it fixes t and kappa and preserves
integrality and funding of the proposal. A static displacement commutes
with F directly: F changes E only by a vector in the image of C, while
C^t d=0, so the following magnetic update is also identical. The two
orders give the same raw proposed state.

Since a_G(Fs)=a_G(s), both acceptance bits in the completion rule are
invariant under F. The complete refusal decision is therefore invariant
as well, proving S_ij F=F S_ij.

The event e is the conjunction of the literal R endpoint with a_G=1.
The contact preserves both. Thus e(S_ij s)=e(s). Extending S_ij by the
identity on every pointer value p gives commutation with
Ghat(s,p)=(Gs,p+e(s) mod5), on every p, with no assumed pointer reset.

## 7. Exact maximality for the fixed proposal (T4)

Let V be any complete map that chooses at each input only identity or the
same legal P_ij and satisfies VG=GV. In particular V fixes m. Let pi_m
be projection to the matter triple. Then

\[
\pi_m(GVs)=\pi_m(VGs)=\pi_m(Gs).
\]

Because V leaves the input endpoint unchanged and the accepted G branch
changes it to the other distinct endpoint, this identity forces
a_G(Vs)=a_G(s). Every nonidentity use of P_ij must therefore pass exactly
the acceptance-equality filter above, as well as the already mandatory
integrality and nonnegative-stock conditions.

S_ij uses all such legal proposals. Hence the nonidentity support of every
V is contained in the support of S_ij. At any state where P_ij already
equals identity there is no nonidentity support to maximize. Every map
with the greatest support must agree with S_ij on each remaining state,
so the maximum is unique. The necessity even holds without assuming V
bijective; S_ij itself is a complete involution and also commutes with F.

Neither the proposal class nor the choice of greatest support has been
derived from a source. A smaller admissible contact, such as identity,
is still a law satisfying the relevant invariants. Different pairs also
give different unique maxima in their different fixed proposal classes.

## 8. Nonzero work with F-commutation and selection within Hc (T5, T6)

For 01 the price is 10 n squared plus 2 n E.k, hence always even. For
02 and 12 it is 15 n squared plus 2 n E.k, hence has the parity of n.
These statements concern the integral-proposal domain. Refusals have
zero actual price.

Because r'=r-kappa, an even price preserves stock parity. Therefore S01
preserves every Hc. An odd committed price changes parity by either +1
or -1, and

\[
\Delta H_c=(c-1)\big((r'\bmod2)-(r\bmod2)\big).
\]

For an explicit odd event use v=(1,0,0,0) and

\[
m=R,\quad b=(5v,-5v,0),\quad E=(2,2,1,1),\quad M=0,\quad r=7.
\]

Here y=0, sigma=(2,1), Hraw=10, the b energy is 300, and H1=335.
The actual charges are (5,-5,0), exactly DE. The R reaction increment
is -2. Both contacts below are integral and have price +5, satisfying
5 <= min(7,5):

| Contact | New b | New E | New stock | New raw field energy |
|---|---|---|---:|---:|
| S02 | (0,-5v,5v) | (1,1,-2,3) | 2 | 15 |
| S12 | (5v,0,-5v) | (1,1,3,-2) | 2 | 15 |

After the subsequent G step, stock is zero. In the other order G first
leaves stock five and the contact then leaves zero. Both full squares
have total cell energy 335. Stock parity changes from one to zero,
giving Delta Hc=1-c. This proves necessity of c=1 for each full law.
The all-state preservation proof for H1 proves sufficiency. Hence the
classification is exact on the unbounded carrier, not a positive inference
from finite samples.

For the same input with r=5 or6, the raw contact is individually funded
but would leave r'=0 or1. Those states reject G, whereas the inputs accept.
The completed contact fixes them. At their G images the proposal is
unfunded and again fixes the entire state. The naive rule using only
own-side funding instead changes the field and therefore fails G
commutation. The reverse raw proposal endpoints test the opposite
rejected-to-accepted admission mismatch.

F need not be trivial in this example: replacing m by AM and taking
y=(0,0,1,0), sigma=(2,1), M=(1,0), r=7 leaves both +5 proposals funded
with G accepted at both ends. F changes this field, yet the proved
commutation still holds.

On the original common PR input with E=(2,2,1,-4), b=(5v,0,-5v), m=R,
M=0 and r=81, the completed static prices are (0,0,-5). S12 gives
E'=(3,3,-1,-1), r'=86 and preserves H1=424. Thus the new laws extend
the available contact alternatives; the earlier direct/alternative
prices 5 and80 do not exhaust this static class.

## 9. A complete new readout counterexample (T7)

Apply the old complete two-cell step T, followed by receiver S01 or S12.
The precise two-cell order, states and every intermediate tuple were frozen
in ADDENDUM-READOUT.md. Both laws are complete bijections. Fix the same
final state Y with zero source, eta=0, p=0, and receiver equal to the
common PR input above, of energy 424. The two predecessors are:

| Quantity | History using S01 after T | History using S12 after T |
|---|---:|---:|
| Initial source energy | 81 | 86 |
| Initial receiver energy | 343 | 338 |
| Initial receiver matter | AM | AM |
| Initial receiver stock | 6 | 6 |
| Initial receiver active energy H(y) | 2 | 2 |
| AM reaction funding remainder | 0 | 0 |
| Final receiver energy | 424 | 424 |
| Last receiver energy increase | 81 | 86 |
| Pointer value throughout | 0 | 0 |
| Complete energy including the common pointer energy 1 | 425 | 425 |

The initial receiver electric fields are (-2,0,2,-3) and (1,3,1,1), with
M=0 in each. Their b triples are respectively (0,5v,-5v) and (5v,-5v,0).
Both have y=(-1,0,0,0), so the AM guard is exactly 6+2-4*2=0. G is
accepted, changes AM to R and leaves stock zero, writing no R-to-AM event.
The stock swaps then transfer source stock 81 or86 to the receiver and
leave source stock and link zero.

After F, the receiver electric fields are (0,0,0,-5) and (3,3,-1,-1),
with M=0. These states are S01(Y_receiver) and S12(Y_receiver); their
stocks are 81 and86. The final contacts are admitted, with prices zero
and +5, and each returns exactly Y_receiver. This verifies full-state
coincidence, not just equality of a pointer or one energy.

A function of Y cannot equal both 81 and86. Therefore no exact common
last-change reader exists on this two-history union without additional
context, even if the reader sees the entire old final state and its total
energy. For any real output v the larger absolute error is at least 5/2,
by the triangle inequality.

A retained k in {01,12} makes the controlled law
`(X,k) -> (T_k X,k)` a single complete bijection. Its inverse selects the
corresponding known law; a last-energy-change reader can then compare the
reconstructed receiver energy with the final one. At least two distinguishable
extra values are needed for this ambiguous pair, and this bit suffices for
the declared two-law family. The expanded final states differ in k. Its
physical preparation, energy account, control coupling and readable
availability do not follow from this abstract construction.

## 10. Why this still does not select a physical source law

Three different choices remain premises: which static register pair can
interact, why the complete contact has maximal support in that proposal
class, and why H1 is the energetic account. Preserving H1 after setting
r'=r-Delta Hraw cannot independently establish that energy choice. The
odd-event classification supplies an exact conditional restriction inside
Hc, not an independent occurrence law for the odd event.

There is also a concrete algebraic separation from the audited old gate
alphabet. Its G, F and stock swaps each preserve every actual node charge.
A finite composition, even with state-dependent gate choices and a finite
stopping time, preserves those charges on each branch. The new +5 witnesses
change them from (5,-5,0) to (0,-5,5) or (5,0,-5). Therefore no word in
that alphabet implements these witnessed contact actions on the same
identified carrier. Extra controllers enter this argument only if their
complete updates preserve the same charges. This restates the source
boundary of PR #1424 with the newly completed contacts; it is not an
impossibility theorem about a broader source dynamics U.

Likewise a receiver contact generally does not commute with the incident
stock swap B. In the price +5 witness, take external eta=0. Contact then B
gives the changed field, receiver stock zero, eta=2. B then contact first
sets receiver stock zero, so the contact refuses and leaves the original
field and eta=7. Disjoint operations may still commute. Nothing here
asserts commutation with the whole old chain step.

The remaining source task is consequently specific: supply an independently
admitted complete source transition and accessible context/interface,
derive its field, matter and stock outputs including refusals and helper
accounts, and only then apply the preselected energetic-family test and
the exact readout criterion. The geometry's metric/unit questions,
Hilbert coherence and the full-model photon phase are unchanged.

## 11. Evidence status and preserved failures

The seven claims above are justified by their universal algebraic proofs or
exact finite witnesses. The accompanying programs are attempts to falsify
them and audit transcription; their finite success cannot replace the
proofs. RUN.md records the actual local execution, and REVIEW.md records a
separate assistant text review, with its independence limits. No new public
two-architecture result is implied by the older PR checks.

The source ZIP's naive funded-kick factorization S3 and unrestricted
uniqueness S4b remain fired. This construction does not reinstate them.
Its statement about zero price and nonzero charge movement on Zdom requires
Zdom intersect {nu != 0} when nonzero motion is part of the conjunction.
No original file or first-run record is overwritten.

## Source links

* [Public authority STATUS at the checked main commit](https://github.com/mathorn1973/twist-j/blob/7d7f588c42422c2cf37b04d76ebc13ca55eb96dc/STATUS.md).
* [Canonical field-chain law and shared proofs](https://github.com/mathorn1973/twist-j/blob/7d7f588c42422c2cf37b04d76ebc13ca55eb96dc/canon/CANON.md#field-conservative-chain-law-t).
* [PR #1424 source selection and prior two-history obstruction](https://github.com/mathorn1973/twist-j/blob/c404723bbda3a65dd39c86ae4fc1152b587977c3/notes/C-PHYSICAL-READOUT-CLOSURE-SYNTHESIS-N/SOURCE_SELECTION.md).
* [PR #1424 complete contact construction](https://github.com/mathorn1973/twist-j/blob/c404723bbda3a65dd39c86ae4fc1152b587977c3/notes/C-PHYSICAL-READOUT-CLOSURE-SYNTHESIS-N/CONTACT.md).
* User-supplied C-FIELD-STATIC-CONTACT-SYMMETRY-N.zip: provenance and exact
  source hashes are recorded in SOURCES.md of this new package.
