# C-H3-CLOCK-CONTACT-N: conditional native contact synthesis

NON-CANONICAL / NO AUTHORITY. Action layer L1.

Status: candidate-T for the conditional statements proved below. This text
claims no finite search result. The actual baseline histories, alias tests,
selected preparations and later continuations remain computational premises
to be checked separately, with candidate-C scope. Same-session authorship is
not independent external review. No Canon promotion occurs here.

The frozen contract is `PREREG.md` at
`53bc0c11b51d671f85977117a2b8df74f2b0698c`. The native law is the unchanged
`reproduce/h3-referenced-record/verify.py` at public main
`6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`, SHA-256
`4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd`.
The result generalizes the conditional first-contact construction in
`notes/C-H3-REFUSAL-CLOCK-N/PROOF.md` at
`a5d5a276c16c8633e31628f0f3e77a322b95531b`: the incoming radiation here is the
actual apparatus history, and the desired impulse is fixed before the two
odd material scales are selected.

## 1. Ring, accounts and local law

Let `O=Z[j]`, with `1+j+j^2+j^3+j^4=0`, and let `K=Q(j)`.
Use the ordered basis `(1,j,j^2,j^3)`. Define

```text
rho = j^2,       J = 1+rho,
h(z) = z*conjugate(z),
q(z) = Tr_K/Q(h(z))/2,
gamma = h(J).
```

Both `rho` and `J` are units of `O`. In particular
`rho^-1=j^3` and `J^-1=-j-j^2`. Also `h(rho)=1` and
`gamma=2+j^2+j^3`, with `gamma^2-3*gamma+1=0` and `gamma^2!=1`.
The last inequality follows because `gamma^2=1` together with its displayed
quadratic equation would imply `gamma=2/3`, an immediate contradiction.

For `z=a0+a1*j+a2*j^2+a3*j^3` with rational coefficients,

```text
q(z) = (5*sum(ai^2) - (sum(ai))^2)/2.
```

Indeed `Tr(1)=4` and `Tr(j^k)=-1` for `k` not divisible by five.
Cauchy-Schwarz gives `(sum(ai))^2 <= 4*sum(ai^2)`, hence
`q(z) >= sum(ai^2)/2 > 0` when `z!=0`. For integral coefficients the
numerator is even, so `q(O)` is integral. These facts supply the positive
leading coefficients used below. No floating-point comparison is needed.

A material or radiation transport pair `(a,b)` is refused, and left fixed,
when `a-b` is not in `2O`. Otherwise its center is retained and its
half-difference is multiplied by `rho`:

```text
C(a,b) = ((a+b+rho*(a-b))/2, (a+b-rho*(a-b))/2).
```

This is the actual parity-completed contact, not its unrestricted rational
extension. Its admitted domain is invariant, and its inverse uses `rho^-1`;
the refused complement is fixed in both directions.

At a cell write the rails as `(a,b,g,r)=(r0,r2,CLK,CORR)`. If either
`a-b` or `g-r` is outside `2O`, B is idle. Otherwise put

```text
d=(a-b)/2,       f=(g-r)/2.
```

The two centers are retained. B1, when `d!=0` and `h(f)=gamma*h(d)`,
replaces `(d,f)` by `(J*d,J^-1*f)`. B2, when `f!=0` and
`h(d)=gamma*h(f)`, replaces it by `(J^-1*d,J*f)`. Every other cell is
idle. The two nonzero branches cannot both qualify: their conjunction
would imply `gamma^2=1`. B1 and B2 are mutual inverses, so B is an
involution, including its idle part.

The complete native tick is the specified alternating disjoint-pair C
transport, then local B, then the matching-bit flip. Material and CLK
transport vertically; CORR transports horizontally. The bit belongs to
the complete state. These facts, especially the separate transport
directions, are essential to the interface argument.

## 2. Exact funding of a prescribed local impulse

**Conditional local statement, candidate-T.** Fix a nonzero `Delta in O`
and the desired incoming CORR value `r*`. The following integral
preparations give the prescribed tag and the same four-slot impulse:

| Tag | `f*` | `d*` | Constant CLK `g` |
|---|---|---|---|
| B1 | `J*rho^-1*Delta` | `rho^-1*Delta` | `r*+2*f*` |
| B2 | `-rho^-1*Delta` | `J*f*` | `r*+2*f*` |

At any cell with material half-difference `d*` and CORR `r*`, both parity
conditions hold and the intended branch qualifies. Nonzero `Delta` makes
`d*` and `f*` nonzero. The opposite branch cannot qualify by `gamma^2!=1`.

For B1, `1-J^-1=rho/J` gives the CORR increment
`(1-J^-1)*f*=Delta`, and the material increment is
`(J-1)*d*=rho*d*=Delta`. For B2, `1-J=-rho` gives
`(1-J)*f*=Delta`, while
`(J^-1-1)*d*=(-rho/J)*(-J*rho^-1*Delta)=Delta`.
Thus, for either frozen canonical choice,

```text
(r0,r2,CLK,CORR) -> (r0+Delta,r2-Delta,CLK-Delta,CORR+Delta).
```

This is an actual funded B contact, with both material recoil and CLK
debit retained. A CORR-only artificial increment is a different operation.
The table concerns the canonical `d*` choices in the frozen contract; no
extra phase multiplier is inserted in this experiment.

## 3. Free wheels and common preparation

Consider a finite even-height apparatus and one initially unused column
whose two material rails and CLK are zero. Keep its CORR and every other
slot unchanged. Let a finite collection of baseline input histories be
supplied, including any explicitly declared input boundaries, through one
absolute target tick `tau`. Each baseline history is a literal native
trajectory between those boundaries. Every boundary leaves the entire new
column and the matching bit unchanged and does not advance the native
transport schedule. It must also preserve equality outside that column:
when two states agree on every outside coordinate, including any retained
reserves and other context, the same supplied input action gives outputs
agreeing on every outside coordinate. It is sufficient that the outside
update depend only on those outside coordinates and the common supplied
input. Merely writing outside the column is insufficient: a boundary
that reads a clock value and uses it to change another column need not
preserve the equality required by the proof.

Let `u(t,z)` and `v(t,z)` be two supplied free vertical C trajectories on
this height, with the same absolute matching bit as the apparatus. They
must be actual integral trajectories with their actual refusals. Choose a
read row `y`, and define

```text
u* = u(tau,y),       v* = v(tau,y).
```

The wanted events occur at `(tau,y)` in a declared subset of the input
histories. Require that their baseline incoming CORR is the same `r*`.
Use Section 2 to fix `g,d*,f*` from the chosen tag and nonzero `Delta`.
All other column cells and times from tick one through `tau`, on every
history, are unwanted. In particular this includes other rows at `tau`
and the excluded input histories at `(tau,y)`.

For positive odd integers `A,B`, initialize the new column once with

```text
r0(0,z) = A*u(0,z),
r2(0,z) = B*v(0,z)+c,
CLK(0,z) = g,
c = A*u* - B*v* - 2*d*.
```

Odd integer scaling and a common translation commute with actual C.
For a refused pair, an odd scale leaves its nonzero residue modulo `2O`
nonzero; for an admitted pair the displayed linear formula commutes with
both operations. Therefore, while the column has no B, its actual rails
at the post-C cut of tick `t` are

```text
r0=A*u(t,z),         r2=B*v(t,z)+c,         CLK=g.
```

At any event `e=(history,t,z)` put

```text
du_e = u(t,z)-u*,    dv_e = v(t,z)-v*,
F_e = g-r_e,
D_e = r0-r2 = 2*d* + A*du_e - B*dv_e,
```

where `r_e` is its supplied baseline incoming CORR. Thus `D_e=2*d*`
at every wanted event. The parity of `D_e` is independent of the
particular odd scales, since `D_e = du_e-dv_e (mod 2O)`. Radiation
parity, the parity of `F_e`, is also fixed.

## 4. All-history alias condition and finite scale bound

Call an unwanted event admitted for this test when both `du_e-dv_e`
and `F_e` belong to `2O`. Events failing either condition are necessarily
idle for every allowed odd `A,B`.

An admitted unwanted event is a **joint-target alias** when
`du_e=dv_e=0`. At such an event, test the literal native B rule using
`d=d*` and `f=F_e/2`. The all-history alias condition is:

```text
Every admitted unwanted joint-target alias has idle B.
```

This condition includes both tags and the entire declared prefix, not only
earlier occurrences at the read row. Equality of the negative and positive
CORR values is sufficient to fail at the target read row, but inequality
alone does not establish the condition: different radiation values can
have the same relevant Hermitian norm.

**Conditional synthesis theorem, candidate-T.** Under the hypotheses of
Sections 1 through 3, there exist positive odd scales `A,B` giving no
unwanted B through `tau` and exactly the intended wanted contacts if and
only if the all-history alias condition holds. If `K` counts all admitted
unwanted event constraints, the first `4K+1` positive odd integers suffice
for each of the following two sequential scale selections.

**Proof of sufficiency.** A nonzero B1 requires `h(d)=h(J^-1*f)`, and a
nonzero B2 requires `h(d)=h(J*f)`. Consequently either tag requires one
of the scalar equalities

```text
q(D_e) = q(J^-1*F_e),       q(D_e) = q(J*F_e).
```

The factors of four from the two half-differences have canceled. These
are only necessary equalities; excluding them is sufficient to exclude B.

First consider admitted unwanted events with `dv_e=0` and `du_e!=0`.
Each of their two displayed equations is a polynomial equation in `A`
with positive quadratic coefficient `q(du_e)`. Each therefore has at
most two rational roots and, in particular, at most two allowed odd
integer roots. The union excludes at most `4K` values of `A`. Choose
the first positive odd `A` avoiding all these equations. This choice is
among the first `4K+1` positive odd integers and does not depend on `B`.

Next consider admitted unwanted events with `dv_e!=0`. With that `A`
fixed, each equation is a polynomial equation in `B` with positive
quadratic coefficient `q(dv_e)`. At most `4K` values are excluded.
Choose the first positive odd `B` avoiding them. It too is among the
first `4K+1` positive odd integers. If one stage has no such constraints,
its first choice is simply one. Duplicated constraints may be removed;
they do not create additional roots. The stated bound remains valid
whether `K` is the full admitted-event count or a transparently
deduplicated constraint count covering both stages.

Every unwanted event is now either parity-refused, an idle joint-target
alias by hypothesis, or excluded by one of the two selections. All
wanted events have `d=d*`, `f=f*`, so Section 2 gives exactly their
prescribed nonzero B. Section 5 proves that the baseline histories used
in this argument are the actual incoming histories up to these contacts.

**Proof of necessity.** Suppose a successful silent prefix exists for
some allowed scales. At every preceding cut, Section 5 then identifies
its bank material state and incoming CORR with the free words and the
baseline input history. At an admitted unwanted joint-target alias its
material half-difference is exactly `d*`, independently of those scales.
If the literal B test there is nonzero, an unwanted contact follows,
contradicting the required prefix. Thus any such alias rejects the entire
odd-scale family for those fixed words, phases, target, tag and impulse.

This theorem neither asserts that a chosen wheel family satisfies the
alias condition nor that any requested target time has suitable wheels.
It gives a finite conditional synthesis procedure once those data are fixed.

## 5. Actual-field induction, input boundary and accounts

The synthesis argument does not prescribe CORR from outside during the
run. Its baseline history is a proof device for a finite first-contact
induction.

At initial time only the three declared vertical rails of the unused
column differ from the baseline. If they have had no B, their transport
stays inside that column. CLK remains uniform at `g`; the two material
rails follow the free words by Section 3. Every CORR value remains equal
to baseline because its horizontal C input remains equal. Every other
column is exactly baseline before B and hence after its local B. The
constructed tests make B idle in the new column at all unwanted events.
This closes the induction until the wanted contact. At a declared input
boundary, the equality-preservation condition of Section 3 carries the
outside equality to the outputs under the common supplied input, while
the new column and its matching schedule remain unchanged. Thus the
induction also passes each such boundary.

At the wanted tick, all other cells still have their baseline pre-B states,
so all their B tags and post-B states are unchanged. The new column has
only the declared additional contact. There is no within-B propagation
from one cell to another. In particular source, worker and old archive
columns still equal their baseline histories through the full target cut.
The new pulse changes later transport, so this induction makes no claim
about cuts after the target.

In the frozen experiment, `tau=114+T`, `T` is 89 or 90, and the new
column is present before the first measurement. Its wheels are not
inserted or rephased at tick 114. The even supplied starting phases
and the even boundary time 114 keep their free-word matching bit equal
to the apparatus's absolute bit. All five first-input histories and all
25 ordered second-input continuations belong to the alias condition.
Deduplication requires actual complete-state equality; it cannot discard
the first measurement or replace absolute `tau` by relative `T`.

The only declared external action is the prior source neutral-pair swap
at full 114. For each even source row the outgoing pair is
`(eta*p,-eta*p)` and the incoming pair is `(eta*q,-eta*q)`, with
`p,q` fifth roots. Each pair has material sum zero and Hermitian sum
`2*h(eta)`, because `h(p)=h(q)=1`. The replacement therefore preserves
the apparatus's complete accounts. Retaining the outgoing pair in the
same slots of the reserve that supplied the incoming pair makes the
combined boundary an ordinary reversible swap. This fixed-coordinate swap
reads and changes only the source pairs and their reserve pairs, all
outside the new column. It therefore satisfies the stronger outside
equality-preservation condition of Section 3, as well as leaving the
matching schedule unchanged. No source information is discarded and no
native implementation of this boundary is inferred.
The baseline source-readiness premise at that boundary is part of the
prior apparatus certificate and must also be reproduced in the literal run.

For a field `F`, define its full material sum `S_m`, radiation sum `S_r`,
Hermitian sum `H=sum h(z)` over all slots, and `Q=q` applied additively
to the slots, equivalently `Tr(H)/2`. If the initial three bank rails
were all zero, the resource additions from the common prepared stock are
exactly

```text
Delta S_m = sum_z (A*u(0,z)+B*v(0,z)+c),
Delta S_r = n*g,
Delta H   = sum_z [h(A*u(0,z))+h(B*v(0,z)+c)+h(g)],
Delta Q   = Tr(Delta H)/2,
```

where `n` is the height. These additions are independent of both inputs.
Equal baseline initial accounts therefore give equal constructed initial
accounts. The reserve's accounts are included at the input boundary.
No minimum-resource claim follows from choosing the first admissible scales.

Each actual C preserves its pair sum and Hermitian sum because
`h(rho)=1`; refused pairs are unchanged. Each B preserves both centers,
so it preserves the material and radiation sums separately. Its
nontrivial contribution to the Hermitian account is proportional to
`h(d)+h(f)`, which is preserved by the applicable balance relation:
for B1, `gamma*h(d)+gamma^-1*h(f)=h(f)+h(d)`, and B2 is its inverse.
Thus every actual tick conserves all four complete accounts. C's inverse,
B's involution and the retained bit give an exact two-sided tick inverse.
The input swap is a separately declared reversible boundary, not a native
tick or an exception hidden inside a tick-inverse assertion.

## 6. What the contact records

**Conditional record statement, candidate-T.** Assume that the declared
input family contains both a wanted and an excluded fresh-predicate value.
At the target full cut the fixed material read pair in the new column then
has exactly two values, indexed by that predicate. Both raw words and
their supplied stock are common to every history. Negative histories
leave the target pair unchanged; positive histories add exactly
`(Delta,-Delta)` by Section 2. Nonzero `Delta` makes the two values
different, and neither depends on the previous input.

If, at this same target cut, the baseline old-archive material has exactly
two values indexed by the old predicate and independent of the fresh
input, its equality with the actual old archive through the target gives
the same property here. Assume additionally that all four combinations of
the old and fresh predicates occur in the declared input family. The
combined old and new material readouts then have exactly four classes:
all four combinations occur, and equality of the combined readout requires
equality of each component. Both occurrence assumptions hold for the frozen
25 ordered fifth-root input pairs with predicates `p==j` and `q==j`.
Without these assumptions, only the corresponding occurring classes can
be asserted, not an exact class count of two or four.
The baseline old-archive premise is separate and must be checked on the
complete declared input family. The proof does not supply it from equal
global accounts alone.

These are statements about the specified finite L1 state reads. A changed
literal read pair at a later cut need not mean the information was erased
from the complete reversible state. Conversely, retention somewhere in
that state does not prove persistence of a fixed local readout or continued
access by another native apparatus. The post-contact observations in the
preregistration decide only their explicitly tested cuts and window.

## 7. Failure conditions and scope

An admitted unwanted joint-target alias with nonzero B is an exact negative
result for that fixed affine two-wheel design and every positive odd scale.
Failure of all frozen designs is bounded by that declared family; it is
not a general obstruction to clocks or measurement. A finite-bound failure
after a genuinely passed alias test contradicts the polynomial proof and
is an implementation or premise error requiring STOP, not a new scientific
negative. So do a mismatched native-law pin, broken parity identity,
changed incoming reference before the first write, or failed account or
inverse assertion.

The theorem gives no unconditional apparatus-existence statement, arbitrary
delay coverage, native loader, minimum cost, postwrite silence, permanence,
clock renewal, occupied-archive regeneration, or second source/worker reset.
A two-pulse fixed-branch repair is not implemented by separately applying
this first-contact theorem twice: the first pulse changes the second
contact's actual material and radiation inputs. Any such composition
requires its own exact successor-state proof or literal complete replay.
All earlier failed restoration targets keep their original status and scope.
There is no native-U identification, physical measurement or time claim,
L1-to-L6 lift, probability statement, or Canon promotion.
