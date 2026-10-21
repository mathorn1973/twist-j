# A funded source-to-loop-to-occupied-receiver chain

**PUBLIC / NON-CANONICAL / L1. Authored conditional candidate-T.**
A. M. Thorn. Apache-2.0. Claim #1626.

This construction supplies one complete declared extended machine. A finite
list of independent native input contents controls actual integer loops;
their actual integer record supplies a new content to an already occupied
native receiver. The old receiver contents, occupied working reference,
bank, program phase and algebraic phase labels remain in the complete state.
Every microstep, including refusal, has a specified inverse on its stated
domain. Original native continuation occurs between every pair of core
ticks, but does not supply the added contacts.

The frozen energy below is a definition of this machine, not a selected
physical energy. In particular it is not obtained by asserting that the
different accounts in #1621--#1625 agree. There is no claim of original-native
admission, physical phase measurement, or implementation of diag(J,phi).

## 1. Three state types and the explicit native chart

Let L>=1 be a fixed integer. All content coordinates in this section are in
F5; integer coordinates and bank values below are ordinary integers. Use
the prepared native chart inherited from #1621 and #1623:

\[
\gamma=(A,z,r)\in\{1,4\}^2\times\mathbb F_5,
\quad h=(\mu,\lambda)\in\mathbb F_5^2,
\quad k=Az,\quad k^2=1.
\]

The actual checkpoint \(\chi_\gamma(h)=(a,b,c,d,q_N,r)\) is

\[
\begin{aligned}
B&=3A,&q_N&=z-4A-r,\\
C&=k(2+3\mu),&D&=k(1+3\lambda),\\
a&=3(A+C+2),&c&=3(A-C-2),\\
b&=3(B+D+1),&d&=3(B-D-1).
\end{aligned}\tag{1}
\]

Its inverse is A=a+c, B=b+d, C=a-c-2, D=b-d-1 and
mu=1+2kC, lambda=3-BzD. This is a chart of actual prepared cells
H={A=2B, B in {2,3}, z in {1,4}}, not an identification of H with
the integer or algebraic carrier. The native q_N is unrelated to the
integer working q introduced below. The fixed receiver port is
(b,d,q_N,r) of cell 0; its inherited reader returns PRESENT(lambda_0)
throughout H, including zero. The source reader uses (a,c,q_N,r).

Retain L+1 native cells h_0,...,h_L and one unchanged native reference
cell h_ref, all with the same gamma and original counter n. Cell 0 has
the working source mu_0 and the fixed occupied receiver lambda_0.
The initial native contents are

\[
h_0=(s,m),\qquad h_j=(o_j,e_j),\quad
e_j\in\{1,4\}\ (1\le j\le L),\qquad h_{\rm ref}\in\mathbb F_5^2.
\tag{2}
\]

The s,m,o_j and reference contents may be arbitrary. The e_j are
independent prepared binary inputs; interpreting 1 as +1 and 4 as -1
does not claim a five-symbol transmission theorem.

These contents have a literal original-native preparation history. For
each input cell the raw origin-zero preparation
(e_j,o_j,-e_j,-o_j,0,0) follows the actual a,c,e prefix and at n=3 is
(-o_j,-e_j,1+o_j,3+e_j,1,1). Its chart contents are exactly (o_j,e_j).
The same formula with arbitrary new/old pair gives cell 0 and the
reference. Thus gamma_3=(1,1,1). This is an inherited native reachability
statement. The creation of those initial raw inputs, and an energy law
valid before entry into H, are not supplied by the present prepared-state
account.

Let gamma_n be the actual common continuation of gamma_3. Selected b
maps (A,z,r) to (-A,-z,-r); selected d/e maps it to (-A,z,1-r).
All h_i remain fixed under this original continuation. We restrict the
native background to the known synchronized slice (n,gamma_n), n>=3.
No global inverse is assumed on the union of both possible z sheets.

## 2. Retained integer references, phase labels and fresh capacity

A working bundle and L donor bundles are

\[
w_i=(q_i,p_i,u_i,v_i;\alpha_i,\beta_i,\tau_i)
\in\mathbb Z^4\times\mathbb F_5^3,\qquad 0\le i\le L.
\tag{3}
\]

Bundle 0 is the working bundle. Its initial value is arbitrary, including
occupied integer and phase records. Each initially ready donor has

\[
w_j=(0,0,1,-1;0,0,0),\qquad 1\le j\le L.
\tag{4}
\]

There are also L retained F5 scratch coordinates zeta_j, initially zero.
They are additional declared memory, not coordinates hidden in a native
cell. No assertion of successful transmission is made for an arbitrary
occupied donor or scratch, although the complete law below is defined
and reversible on those states too.

The integer carrier, native carrier and algebraic representation are
linked by explicitly named gates, not equated. For geometric endpoints
there is a constant-coefficient injection
(p,q) -> (p,q) in O^2, where O=Z[j]. An integer area A maps to A*1 in
O and to its class modulo five. This injection does not intertwine all
of diag(J,phi); its image is not generally preserved by that map.
No step of the present machine is claimed to execute diag(J,phi).

## 3. Complete gates before funding

Define epsilon(t)=1 for t=1, epsilon(t)=-1 for t=4, and epsilon(t)=0
for t in {0,2,3}. This supplies a total rule on arbitrary source contents.
In the intended input class epsilon(e_j) is the signed message eta_j.

For each transaction j the fixed gate list has 24 entries:

1. Exchange mu_0 with lambda_j. Every other native content is retained.
2. Exchange the entire bundles w_0 and w_j, including their phase labels.
3. Repeat five times the four gates Q_+, P_eta, Q_-, P_-eta, where
   eta=epsilon(mu_0) is read from the actual current native source.
4. Add enc(sgn(u_0^2-v_0^2)) to zeta_j in F5, with enc(-1)=4.
5. Exchange zeta_j with the actual native receiver content lambda_0.

There are M=24L gates g_0,...,g_(M-1). The ordering is fixed data of the
machine. It never depends on an external choice between successive ticks.

For h in {-1,0,1}, the combined integer/phase working gates are

\[
\begin{aligned}
Q_h:\ &(q,p,u,v;\alpha,\beta,\tau)
\mapsto(q+h,p,u,v;\alpha,\beta+h,\tau-h\alpha),\\
P_h:\ &(q,p,u,v;\alpha,\beta,\tau)
\mapsto(q,p+h,u+hq,v+hq;
         \alpha+h,\beta,\tau).
\end{aligned}\tag{5}
\]

The first four coordinates use integer h and q. The last three use their
F5 classes, and the alpha in the Q formula is the input alpha.
All other complete-state coordinates are fixed by these gates.

Every listed gate is a bijection on the full declared data carrier:
the three exchanges are involutions; Q_h has inverse Q_-h; P_h has
inverse P_-h; the report addition has inverse subtraction of the same
sign. Controlled P has the same inverse because it leaves mu_0 fixed.
The original checkpoint outputs of a native content exchange are
reconstructed by (1). These are declared contacts on H, including all
occupied branches. They are not words supplied by original U.

In particular, the final write uses the actual integer record, not a
second copy instruction from e_j. The source influences the receiver
through (5), the difference u_0^2-v_0^2, and the report addition. If
that record is wrong, the final gate does not silently substitute the
source value.

## 4. One frozen complete account

Write ell(0,1,2,3,4)=(0,1,2,-2,-1). On the complete retained data s set

\[
\begin{aligned}
H(s)={}&\sum_{i=0}^{L}(q_i^2+p_i^2+u_i^2+v_i^2)\\
&+2\sum_{i\in\{0,\ldots,L,\mathrm{ref}\}}
       \{\ell(\mu_i)^2+\ell(\lambda_i)^2\}
 +2\sum_{j=1}^{L}\ell(\zeta_j)^2.
\end{aligned}\tag{6}
\]

The bank b is an integer with 0<=b<=B, for a fixed capacity B. The total
declared account is H(s)+b. All donor/archive slots, source inputs, old
receiver contents, scratch and the actual native reference appear in (6).
In particular a ready integer donor contributes 2 initially; its
preparation is not assigned zero by omitting it. Occupied working data
remain priced when transferred into an archive.

Equation (6) explicitly assigns zero varying price to the finite phase
labels, program phase and direction, and to the native common controller
gamma_n and advancing counter n. This is a declared degeneracy of this
mathematical energy. It is not a proof that real actuation, physical phase
memory, clock motion or initial resource production is free. It is also
not an identification with the pair accounts of #1621--#1625, the integer
payment 10 of other work, a Dirac gap, or any dimensional physical energy.

The bank unit and (6) are fixed before execution. The conservative lift
below works for many other integer accounts as well; it therefore does
not select (6) independently as physical energy.

## 5. A reversible autonomous schedule, including refusal

Retain a program position c in {0,...,M} and a direction d in {+1,-1}.
The core state is y=(s,b,c,d). First define an edge pairing H_e.

For d=+1 and c<M propose

\[
s'=g_c(s),\quad c'=c+1,\quad d'=-1,\quad
b'=b+H(s)-H(s').\tag{7}
\]

For d=-1 and c>0 propose instead

\[
s'=g_{c-1}^{-1}(s),\quad c'=c-1,\quad d'=+1,\quad
b'=b+H(s)-H(s').\tag{8}
\]

Accept a proposal iff 0<=b'<=B. Otherwise H_e fixes y completely.
At the two outward endpoints (c,d)=(0,-1),(M,+1) it also fixes y.
Define J(s,b,c,d)=(s,b,c,-d), and the actual core tick

\[
F=JH_e.\tag{9}
\]

An accepted core tick moves to the next program position in its current
direction and keeps that direction. A refused tick changes only direction.
No integer motion, phase operation, memory update, bank withdrawal or
program advance occurs on refusal. Endpoint reflection is likewise a
specified direction change, not an external reset.

**Theorem 1 (complete inverse and account).** H_e and J are involutions.
Consequently F is a bijection, with F^-1=H_e J. Every tick, on every
accepted, refused, occupied and endpoint branch, preserves H(s)+b and
the bank interval.

**Proof.** If an edge is accepted, its other endpoint is exactly the
opposite-direction proposal using the inverse gate. Its return bank is
b'+H(s')-H(s)=b, which is in range. Thus the endpoints are paired in
both directions. A refused point is fixed by H_e. The admissibility
symmetry also prevents an accepted point from mapping into a refused
point. Endpoint points are fixed. This proves H_e^2=I on the whole
domain. J^2=I is immediate. Both preserve the account; J changes only
an explicitly degenerate coordinate. Composition gives the stated
inverse and conservation. QED.

A rule that merely applies a non-involutive gate when funded and otherwise
fixes the state would not have this proof: an accepted image can collide
with a fixed rejected state. The retained direction and paired inverse
edge are part of the present complete apparatus.

For a fixed E>=0 the core shell

\[
\mathcal C_{E,B}=\{(s,b,c,d): H(s)+b=E,\ 0\le b\le B\}\tag{10}
\]

is finite. Indeed every integer coordinate in (6) has absolute value at
most sqrt(E); all remaining core coordinates have finite sets of values.
Theorem 1 makes F a permutation of this finite shell. This statement is
about the core. It does not count the original counter n as finite.

## 6. Literal native continuation in the same full history

The full state is (n,gamma_n,y), n>=3. At every tick first apply the core
operation (9) in chart (1), then perform one actual common original U
step on all native cells, including the reference:

\[
\mathcal F(n,\gamma_n,y)=(n+1,\gamma_{n+1},F(y)).\tag{11}
\]

This description is equivalent to the literal checkpoint formula because
the core contacts only change native contents h, whereas the selected
native tail changes only n,gamma. The core law uses native h through
their actual readers. It does not read an externally substituted history.
The two operations commute on this declared carrier. A core refusal
still has the explicit original U continuation in (11); it is only the
core proposal which is refused.

The full map is injective and has inverse on its image n>=4: undo the
known-slice original step and apply F^-1. It is not surjective onto the
forward carrier beginning at n=3, and it has no asserted global inverse
on an unrestricted union of native trace sheets. Its fixed-energy shell
is infinite because n advances without bound and is assigned zero
varying price. No finite full-state recurrence follows from (10).

Original U alone fixes all the contents h_i and cannot execute the
changed core contacts. Thus (11) is a specified extension of U, not an
admission proof for that extension or a redefinition of native U.

## 7. The actual loop history and algebraic phase

Let j be a primitive fifth root and define the five-dimensional Weyl
operators X e_t=e_(t+1), Z e_t=j^t e_t. A phase label reads as

\[
R(\alpha,\beta,\tau)e_t
 =j^{\tau+\alpha(t+\beta)}e_{t+\beta}
 =j^\tau Z^\alpha X^\beta e_t.\tag{12}
\]

The Q and P updates in (5) satisfy exactly

\[
R(Q_h g)=X^h R(g),\qquad
R(P_h g)=Z^h R(g),\tag{13}
\]

using ZX=jXZ. Thus each accepted integer Q/P edge supplies its literal
Weyl operator, in chronological left-product order. Its inverse supplies
the inverse operator. Refused proposals supply identity. Bundle exchanges
transport the integer and phase records together: the appropriate phase
history follows the retained bundle, rather than being reset when that
bundle becomes the working one. This is a record of an algebraic operator,
not an asserted physical phase observable or a quantum measurement law.

For a segment of accepted integer gates define its integer area increment
by A=sum(q*Delta p), using the actual input q on each P edge. A Q edge
has zero increment. On a fresh donor with alpha=beta=tau=q=p=0,
induction in (5) gives alpha=p mod5, beta=q mod5 and tau=A-p*q mod5.
This relates the integer trajectory, its integer record and its Weyl
label along the very same accepted path.

The corresponding arbitrary-origin path formula and the single global
operator history including bundle transport are proved in [WEYL.md](WEYL.md).
In particular a bundle exchange contributes a tensor-factor permutation,
not identity. The local identity label of a fresh donor is not the identity
of the complete apparatus history. This phase convention is exactly the
ordered convention Z^alpha X^beta used there.

One complete signed loop, from arbitrary q,p,u,v, is

\[
Q_+,P_\eta,Q_-,P_{-\eta}:
(q,p,u,v)\mapsto(q,p,u+\eta,v+\eta).\tag{14}
\]

The area gain is eta(q+1)-eta*q=eta. On an arbitrary occupied phase
label the corresponding product is j^eta I, so alpha,beta return and
tau increases by eta. No zero initial label is needed for this relative
operator statement. Five loops add 5eta to both integer references and
return the phase label to its initial value. On a fresh donor their
endpoints are therefore

\[
(q,p,u,v;\alpha,\beta,\tau)
 =(0,0,1+5\eta,-1+5\eta;0,0,0).\tag{15}
\]

The ordered squared record is (36,16) for eta=+1 and (16,36) for eta=-1.
In both cases u^2-v^2=20eta, so its sign distinguishes orientation.
The Weyl operator is identity after five loops. A phase class modulo five
cannot replace this integer orientation record or the complete history.

## 8. Complete occupied-receiver delivery on the ready segment

Assume (2), ready donors (4), all zeta_j=0, and start c=0,d=+1.
Theorem 3 below supplies the exact bank bound needed for no refusal.

**Theorem 2 (L source-fed deliveries with retained old data).** For each
transaction j, the native fixed receiver reads PRESENT(e_j) immediately
after that transaction's final exchange. The incoming value is obtained
from the actual five-loop integer record. Its previous value is retained
in zeta_j. The initial working bundle and every completed loop record are
retained in a donor or working slot, including their phase labels.

**Proof.** The source exchange puts e_j into mu_0 while retaining its old
content in lambda_j. Earlier transactions do not touch the unused
lambda_j or donor/scratch j. The bundle exchange prepares the working
integer cell to (0,0,1,-1) and archives the complete former working bundle.
All 20 geometry gates leave mu_0 unchanged, so their actual signed
parameter is eta_j throughout. Equation (15) makes the report sign eta_j.
The previously unused zeta_j is zero, hence report addition makes it e_j.
The final exchange puts this actual report into lambda_0 and retains the
old lambda_0 in zeta_j. Native continuation between the core gates fixes
all these contents. Induction in j proves the statement. QED.

In particular the final scratch values are zeta_1=m and zeta_j=e_(j-1)
for j>=2. The source tape retains lambda_1=s and lambda_j=e_(j-1) for
j>=2, while mu_0=e_L; every o_j remains in its original mu_j. Thus
source loading also erases nothing. These explicit archives do not
depend on the old receiver being blank or different from the new value.

At the delivery cuts the native reader needs only its fixed receiver
port, not a moving address or a replacement decoder. Between cuts it
continues to read the last installed content. The theorem concerns the
initial forward work segment through c=M. After endpoint reflection the
specified inverse program undoes it; this finite machine does not retain
an ever-growing archive through infinitely many receptions.

## 9. Exact funding, including the reporting gate

For a fresh working donor, after t complete signed loops its integer
cost is 2+2t^2. In loop t (1<=t<=5) the four successive costs are

\[
3+2(t-1)^2,\qquad 4+2t^2,\qquad
3+2t^2,\qquad 2+2t^2.\tag{16}
\]

The signs do not affect these values. The calculation uses q=1,p=eta
on the P_eta intermediate state, followed by q=0 and then p=0.
Consequently five loops gain 50 units and have a greatest transient
gain 52 above their initial donor cost.

The source, whole-bundle and receiver exchanges preserve (6) exactly,
even when the exchanged entries are occupied. Reporting into zeta_j=0
changes its price from 0 to 2, since enc(eta_j) has balanced square 1.
This cost is included; recording a retained source value is not treated
as a free additional memory copy. The transaction therefore gains 52
units overall, and its largest intermediate gain is also 52.

**Theorem 3 (sharp uniform ready-segment bank).** For the frozen account
(6), the entire L-message forward segment has no refusal iff its initial
bank obeys b_0>=52L, provided B>=b_0. Its final bank is b_0-52L. This
threshold is independent of all occupied native contents, the arbitrary
initial working bundle, and the choices of the L binary inputs.

**Proof.** At the start of transaction j the earlier completed
transactions have gained 52(j-1). Formula (16) and the reporting cost
show that the largest cumulative gain during transaction j is 52j;
it is attained at the fifth P_eta edge and again after its report. All
cumulative gains are nonnegative. Thus b_0>=52L keeps every proposed
bank between 0 and b_0, so the upper capacity cannot reject either.
The net gain proves the final bank value. Conversely a completed ready
forward segment has total data gain 52L. Conservation and bank
nonnegativity require b_0>=52L. This also proves sharpness. QED.

The occupied initial integer bundle is transferred intact, not reset, so
its arbitrary energy cancels from these increments. The donor energies
and every occupied native memory already contribute to the initial H.
The numerical bound is an exact result for this declared prepared
machine and this account; it is not a physical minimum preparation cost.

After an adequately funded forward segment, every inverse edge on the
return segment is admissible: it visits exactly the forward states in
reverse order and returns the original bank. At both endpoints F changes
only direction. Hence the core state returns after 2M+2 ticks of this
unrefused excursion. In the full machine (11), n has advanced by 2M+2;
only the core has returned. No assertion about the period on other
funding shells or invalid preparations is needed.

## 10. Failures are complete branches, not repaired inputs

The whole law and inverse hold beyond the intended preparation class.
The transmission theorem does not. The following distinctions are
essential falsification targets.

- **Dirty integer donor.** Starting its references at u=v=0 gives
  u=v=5eta after five loops. The report is then zero, although the source
  is nonzero and the Weyl label also returns after five loops. This
  falsifies dropping the marked-reference preparation, not reversibility.
- **Occupied report scratch.** If its initial value is t, the report
  stage writes t+e_j modulo five. The receiver obtains that value. A
  general occupied scratch cannot be silently called a blank register.
  Its old information is still retained by the full invertible law.
- **Occupied receiver.** Every m is allowed in Theorem 2; it goes to the
  declared zeta archive. There is no receiver reset or erasure branch.
- **Insufficient bank or upper-capacity refusal.** The actual core
  proposal is rejected as a whole, including its phase update, and the
  direction reverses. The accepted-history phase product contains no
  operator for the rejected geometry. No claim of successful delivery
  is made after a bounce before c=M.
- **Five loops.** Their group label returns even though the integer
  orientation record differs. Replacing the record by its phase class
  loses the sign witness and the 50-unit integer account.
- **Other source symbols.** For mu_0 in {0,2,3} the declared epsilon is
  zero. The rule is still invertible, but is not the five-symbol channel
  whose existence might be incorrectly inferred from its F5 storage.
- **External controller substitution.** Changing a gate, source sign,
  report, direction or ready resource between ticks gives another
  history. The theorem uses only the retained state and the one fixed
  transition (11).

## 11. Achieved junction and remaining admission obligations

The positive result is a single declared history linking actual native
input contents, a funded integer oriented loop, its retained orientation
record, an algebraic Weyl label and an already completed native receiver.
It includes retained dirty resources, finite new ready capacity, exact
bank refusal and inverse branches, and a controller inside the state.
It is stronger than matching separate endpoints after the fact.

The construction does not settle the original-native junction. The
source loader, integer-bundle exchange, controlled Q/P contact, report
addition, native receiver exchange and program mechanism are separately
supplied rules. Their original-native admission remains open. The initial
ready donors, scratch and independent source contents are specified and
priced resources; their production from a more primitive apparatus is not
derived. The native prefix proves reachability of the native content
preparations, not an account for producing every added resource.

The account (6), including its zero-priced controller/phase sectors, is
declared. The finite group label has only the representation (12), not a
physical phase readout. The constant-coordinate O^2 injection supplies
an algebraic type relation but not diag(J,phi) dynamics or a physical
action. These are precise remaining obligations, not permissions inferred
from the successful conservative construction.

Accordingly the achieved verdict is a conditional declared-extended L1
chain. Original-native physical closure remains unproved. Neither this
proof nor finite verifier audits promote Canon v103 or replace an
independent scientific review.
