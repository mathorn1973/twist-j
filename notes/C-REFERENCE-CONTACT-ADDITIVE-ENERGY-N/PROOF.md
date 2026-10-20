# The same contact does not fix the complete energy account

**PUBLIC / NON-CANONICAL / L1. Authored conditional analytical results.**
A. M. Thorn. Apache-2.0. Claim #1622.
Contract/source pin: f81e74371cf8fadda2ac366c66e1ca9df5081ce4.
Exact premises and attribution: [SOURCES.md](SOURCES.md).

The reference-reading contact of #1621 is kept unchanged. Its conclusion
that the square price is selected in its declared star account is
correct. We show what changes when the complete interaction account is
not already fixed, and what a second independently admitted contact could
decide. We also prove that the first contact cannot conserve a nonconstant
common single-cell content energy for its two signals with an unchanged
reference account. This does not exclude interaction energy.

All coordinate arithmetic is in F5. Account values and counts are real
numbers and ordinary integers, respectively. No scientific executable or
finite enumeration is evidence for these proofs.

## 1. The same complete carrier, contact and original continuation

Use #1621's 500-state prepared cell H, with coordinates

\[
\gamma=(A,z,r)\in\{1,4\}^2\times\mathbb F_5,
\qquad h=(\mu,\lambda)\in\mathbb F_5^2.
\]

For completeness its literal inverse to the original checkpoint
x=(a,b,c,d,q,r) is, with k=Az and k^2=1,

\[
\begin{aligned}
B&=3A,&q&=z-4A-r,\\
C&=k(2+3\mu),&D&=k(1+3\lambda),\\
a&=3(A+C+2),&c&=3(A-C-2),\\
b&=3(B+D+1),&d&=3(B-D-1).
\end{aligned}
\tag{1}
\]

Thus this is a chart of actual checkpoint coordinates, not a replacement
with uncounted registers. Three such cells with common gamma and one
original counter have full state

\[
(n,\gamma,h_0,h_1,h_2),\qquad h_0=\rho,
\tag{2}
\]

and 20*25^3=312500 checkpoints at fixed n. This includes both trace
sheets, not one prescribed synchronized origin-zero slice.

The original selected continuation changes n,gamma only, leaving every
h_i fixed. Its actual choices are b,d at z=1 and e,b at z=4 for bits
0,1. On gamma the actions are

| Selected letter | New (A,z,r) |
| --- | --- |
| b | (-A,-z,-r) |
| d at z=1, e at z=4 | (-A,z,1-r) |

The counter advances once. These source formulas do not give a global
inverse on the union of trace sheets. The known-input-slice inverse
and all source limitations are unchanged.

Put u=(2,0) and w=(1,1). The exact contact T0 from #1621 exchanges
the two full contents

\[
X_\rho=(\rho,\rho+u,\rho)
\quad\longleftrightarrow\quad
Y_\rho=(\rho,\rho+w,\rho+w)
\tag{3}
\]

for each rho, fixing all other triples and leaving n,gamma fixed.
Different rho give disjoint pairs because the first cell retains rho.
This defines a full involution on (2), including all occupied and fixed
branches; (1) reconstructs every output piston. T0 commutes with the
original continuation because it changes only contents, which that
continuation fixes. Original U nevertheless never executes its changed
branch. T0 remains a separately supplied contact, deliberately chosen
in #1621 from a square-account shell.

The simultaneous prepared exchange W of all three cells swaps the two
coordinates of each h_i. We use this inherited map only to check account
invariance. Its independent admission and source scope are unchanged.

## 2. One contact, a family of full interaction accounts

For kappa>0 define the even coordinate reading

\[
f_\kappa(0)=0,\quad f_\kappa(\pm1)=1,\quad
f_\kappa(\pm2)=\kappa,
\qquad
D_\kappa(x,y)=2\sum_{j=1}^2 f_\kappa(x_j-y_j).
\tag{4}
\]

This is precisely the source's prepared piston-difference account,
including its factor two. We call it a pair account; a metric triangle
inequality is not presumed for arbitrary kappa.

On exactly the same full state (2), declare

\[
\mathcal E_{\kappa,\eta}=
D_\kappa(h_1,h_0)+D_\kappa(h_2,h_0)
+\eta D_\kappa(h_1,h_2),\qquad \eta\ge0.
\tag{5}
\]

Eta=0 is the source's star account. Eta=1 gives equal weight to all
three pair interactions. Intermediate eta specifies another declared
interaction weight; no particular value or physical interaction graph
has been derived.

Every account (5) is nonnegative and vanishes precisely when all three
contents agree. It is invariant under a common translation of all h_i,
under original common continuation, and under simultaneous W. The first
claim follows from unchanged differences; the second from fixed contents;
the third from interchanging the two coordinates in each sum (4).

On the entire changed branch (3), independently of rho, n and gamma:

| Contribution | X_rho | Y_rho |
| --- | ---: | ---: |
| D(h1,h0)+D(h2,h0) | 2 kappa | 8 |
| eta D(h1,h2) | 2 eta kappa | 0 |
| Total | 2 kappa(1+eta) | 8 |

Every other branch is fixed. Consequently this is a full-carrier iff:

\[
\boxed{T_0\text{ conserves }\mathcal E_{\kappa,\eta}
\iff\kappa(1+\eta)=4.}
\tag{6}
\]

The source's kappa=4 is recovered at eta=0. At eta=1 the same complete
contact instead conserves kappa=2. For any finite eta>=0, (6) gives
kappa=4/(1+eta)>0. The larger account family therefore leaves a continuous
ambiguity even though the full transition and reference are fixed.

This ambiguity is not just an overall unit change. At the fixed
calibration state h1=h2=h0+(1,0), every (5) has value 4. At
h1=h0+(1,0), h2=h0, it has value 2(1+eta). In particular

| Account | Calibration state | One moved signal |
| --- | ---: | ---: |
| Square star: (kappa,eta)=(4,0) | 4 | 2 |
| Equal-edge triangle: (kappa,eta)=(2,1) | 4 | 4 |

Both conserve exactly T0 and have the same calibration, but are
inequivalent pointwise on the same labelled full carrier. No relabelling
of physical states is used to compare them.

The added edge depends on kappa as well. It is not the independently
priced bank B in #1621 section 9.2, so (6) does not contradict that
bank-selection criterion. Nor do we claim that the source omitted an
edge required by its own definition: (5) is an explicitly larger family.

## 3. Account symmetry and a second-contact test

Within (5), invariance under every permutation of the three cell labels
holds iff eta=1. Sufficiency is immediate from equal edge coefficients.
For necessity evaluate the triple (h0,h1,h2)=(0,e1,0), e1=(1,0).
Its account is 2(1+eta); after swapping labels 0 and 1 it is 4.
Equality forces eta=1. Exchange of the two signals alone imposes no
such condition; (5) already has that symmetry for every eta.

This symmetry is an extra hypothesis about the account. T0 itself is
not symmetric under exchanging its marked reference with a signal.
For example T0 maps (0,u,0) to (0,w,w). If S01 exchanges the complete
cells 0 and 1, then T0 S01(0,u,0)=(u,0,0), a fixed point of T0,
whereas S01 T0(0,u,0)=(w,0,w). Thus T0 S01!=S01 T0. An invariant
energy account does not establish permutation symmetry of the device.

There is also a concrete alternative to imposing symmetry directly.
Separately supply the complete contact

\[
T_1=S_{01}T_0S_{01}.
\tag{7}
\]

S01 exchanges whole cells on the common-controller carrier. It is a
full involution and commutes with original common continuation. Therefore
T1 is also a full involution commuting with that continuation. Its
changed branch is exactly

\[
X'_\rho=(\rho+u,\rho,\rho)
\quad\longleftrightarrow\quad
Y'_\rho=(\rho+w,\rho,\rho+w).
\tag{8}
\]

Here the original marked reference h0 changes; cell 1 is the retained
reference for this role-conjugate operation. Their accounts (5) are
4 kappa and 4(1+eta), respectively. Fixed branches give no further
condition. Hence

\[
T_1\text{ conserves }\mathcal E_{\kappa,\eta}
\iff\kappa=1+\eta.
\tag{9}
\]

If both specified contacts conserve the same account with no other
changing resource, equations (6) and (9) give

\[
\boxed{\kappa=2,\qquad\eta=1.}
\tag{10}
\]

This is unique within the positive two-parameter family (5).
It supplies a conditional two-contact consistency test with explicit
states, inverse domains and unchanged source U. It does not show that
S01 or T1 is admitted by original U, that both contacts actually occur,
or that (5) exhausts physical energy readings. In particular the
positive conclusion (10) is not a new physical law or a refutation of
the source's conditional square-star result.

## 4. No nonconstant common additive single-cell content energy

Fix n,gamma and let h:F5^2->R be arbitrary. Permit any real reference
and control account B(n,gamma,rho), and consider

\[
H=h(h_1)+h(h_2)+B(n,\gamma,\rho).
\tag{11}
\]

The same h is used for both signals. B may price the full reference,
because (1) recovers it from gamma,rho. These coordinates remain fixed
under T0. We require conservation on the whole carrier, for all rho.

**Theorem.** T0 conserves (11) iff h is constant at each fixed n,gamma.

**Proof.** The changed branch (3) and cancellation of B give

\[
h(\rho+(2,0))+h(\rho)=2h(\rho+(1,1))
\quad\text{for all }\rho.
\]

With y=rho+(1,1), this becomes the real averaging equation

\[
h(y)=\tfrac12\big(h(y+(1,-1))+h(y+(-1,-1))\big).
\tag{12}
\]

There is a maximum because the domain has 25 elements. At a maximizing
y both terms on the right must equal the maximum. Repeat at each such
point. The increments (1,-1),(-1,-1) have determinant -2!=0 in F5,
so they span F5^2. Their nonnegative multiples already give their
whole additive span, since each has order five. Thus every point has
the maximum and h is constant. Conversely a constant h, with B fixed,
is plainly conserved. This proof works separately for each fixed
context n,gamma, even if the chosen h depends on that context. QED.

No bounded search, differentiability, polynomial assumption or
nonnegativity of h was needed. The obstruction is to a nonconstant
common **additive single-cell content** account with a stationary
reference contribution, not to energy in general. The interaction
accounts in section 2 are explicit allowed alternatives.

Two hypotheses are essential:

- **One common h.** With different readings
  h1(a,b)=g(a), h2(a,b)=g(a+1), any real nonconstant g:F5->R gives a
  conserved sum on (3). Both sides equal g(rho1+2)+g(rho1+1).
  Distinct species/readings therefore lie outside the theorem.
- **All reference contents.** If only rho=0 is admitted, the nonconstant
  h(a,b)=1 when b=2 and zero otherwise gives zero at every endpoint
  of that single transposition. A one-reference contract cannot claim
  the all-reference maximum-principle conclusion.

Similarly, a changing reference/store, explicit pair interactions or
another preparation domain changes the hypothesis. No universal
one-particle-energy or thermodynamic impossibility follows.

## 5. The exact account required of another changing resource

If the account (5) is retained and a further store has an independently
specified state function B, its necessary forward change on X_rho to
Y_rho is

\[
\boxed{\Delta B=2\kappa(1+\eta)-8.}
\tag{13}
\]

For the square price with a unit signal-signal edge, kappa=4,eta=1,
the three-cell account drops from 16 to 8. The store must **receive +8**,
and the reverse branch must withdraw 8. It is not a cost of +8 paid out
by the store. Under the second contact (8), the corresponding necessary
change is 4 kappa-4(1+eta).

The literal T0 has no changing store coordinate and fixes the complete
reference, controls and counter. Merely assigning B to those fixed
coordinates cannot implement (13) when its right side is nonzero.
An enlarged transition would need an independently priced store, its
actual update, inverse, capacity and any refusal guard. Equation (13)
supplies an exact check on such a proposal, not that proposal itself.

One may not set B=-E after selecting a desired price and call that an
independent selection. This would only define a compensating reading.
Likewise the quantity 8 here is dimensionless in (4)'s declared unit;
it is not the working-machine payment 10, a Dirac energy gap, an entropy
cost, a preparation cost or an SI energy.

## 6. A separate sharp classification of selectable star prices

This section changes the comparison class explicitly: m signal cells,
one unchanged shared reference and only the isolated star account.
It does not include the eta edge or another changing resource.

On the source's prepared directions, the 2m content differences v give
raw piston differences in pairs (-k v_j,k v_j), where k=+-1 is common.
Let c1(v),c2(v) count content coordinates of magnitude one and two.
The exact account is

\[
E_\kappa(v)=2(c_1(v)+\kappa c_2(v)),\qquad
v\in\mathbb F_5^{2m},\quad\kappa>0.
\tag{14}
\]

**Theorem.** There exists a count-changing transition conserving (14)
iff kappa=p/q is a positive rational in lowest terms and
max(p,q)<=2m. The sharp minimum number of prepared blocks and lowest
common account of a count-changing branch are

\[
\boxed{m_{\min}=\left\lceil\frac{\max(p,q)}2\right\rceil,
\qquad E_{\min}=2p.}
\tag{15}
\]

**Proof of necessity.** Conservation gives
Delta c1+kappa Delta c2=0. A change in the count pair forces both
changes nonzero, so kappa is rational. For reduced p/q they have form
(Delta c1,Delta c2)=(pt,-qt), with a nonzero integer t. Reverse the
branch if needed so t>0. The output has at least pt unit coordinates
and the input at least qt double coordinates. Thus 2m>=max(p,q)t
and their common account is at least 2pt>=2p.

**Attainment and full lift.** In 2m coordinates choose v with p ones
and the rest zero, and w with q twos and the rest zero. They are
distinct, both have account 2p, and their counts differ. Transpose v,w
and fix every other vector; call this permutation C. With
D_m rho=(rho1,rho2,...,rho1,rho2), define the full contact by

\[
(n,\gamma,\rho,c)\longmapsto
(n,\gamma,\rho,D_m\rho+C(c-D_m\rho)).
\tag{16}
\]

This is a full involution, fixes the complete reference and controls,
and conserves (14) on every branch. Formula (1) reconstructs every
actual checkpoint. Since original common continuation fixes all
contents, (16) commutes with it. Padding by zero coordinates attains
both bounds at the integer m in (15). QED.

For irrational kappa every conserving branch on any finite number of
these blocks preserves both counts separately. This does not forbid
permutations within a count class or all physical interactions.
Kappa=1 is included: one block suffices and the lowest account is 2.

The prices requiring exactly two prepared blocks are precisely

\[
\{1/4,1/3,2/3,3/4,4/3,3/2,3,4\}.
\tag{17}
\]

Indeed reduced p,q must have maximum three or four. This explicitly
quantifies why a two-block minimum alone does not select the square.
Each supplied permutation was chosen using its desired price, just as
the source's square-shell transposition was; none is thereby executed
by native U or selected as physical energy.

The bounds concern prepared blocks, not the larger general zero-sum
V={delta in F5^4:sum(delta)=0}. At kappa=3 the one-general-block pair

\[
(1,1,1,2)\longleftrightarrow(2,-2,0,0)
\]

has counts (3,1) and (0,2), respectively, and common account 6. Both
vectors have zero sum. This disproves extending the prepared two-block
minimum for kappa=3 to all V. Also m counts signal difference blocks,
not total physical components: (16) retains one additional shared
reference cell, with its preparation and actuation unpriced.

## 7. What the next physical construction must decide

The contact, energy-bearing interactions and price cannot be selected
independently and then identified afterward. On the same T0, even one
added interaction weight changes the conservation equation. A second
separately admitted contact supplies another independent equation and
can distinguish the accounts, as (10) demonstrates in this declared
family.

The concrete next data are therefore an independently justified set of
interactions and their weights, the actual occurrence of the contact(s),
and any changing reference/store with its own fixed price and inverse.
For the existing square price and the unit third edge, (13) already
requires a retained +8 elsewhere. For a stationary additive reference
with identical one-cell prices, section 4 instead gives a strict no-go
on the full preparation class. Interaction energy or reference
backreaction must then be included, or the physical hypotheses changed.

The joint-energy alternatives and conditional two-contact selection
are mathematical results, not native admission. No Canon status,
physical-energy closure, mass relation, reusable receiver or layer
bridge follows. The source's exact square-star theorem, all original
inverse restrictions and every existing physical-admission owner remain
unchanged.
