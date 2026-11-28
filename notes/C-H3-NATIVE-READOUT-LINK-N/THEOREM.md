# C-H3-NATIVE-READOUT-LINK-N: conditional transport and receiver proofs

NON-CANONICAL / NO AUTHORITY. Action layer L1. Claim #2141.

Status: conditional candidate-T for the algebraic statements proved here.
No new trajectory computation is used in this file. The 32-step retention
gates and the original-time-zero preparation question are separate finite
computations, at most candidate-C, under the frozen preregistrations.

The contract is PREREG-A.md, PREREG-B.md and CLARIFICATION-A.md at
`1c978d0acdcc9a9fef557b400b0ec48abc1f1437`, together with the pre-execution
CLARIFICATION-B.md at `4c48a115ea28e39d748725ea5c506c81c87ed462`.
The latter requires clean old-only classes
in both strict retention gates and identifies common accounts as compound
accounts. Four joint classes alone would not imply clean old-only classes.

The unchanged law is `reproduce/h3-referenced-record/verify.py` at public
main `6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`, SHA-256
`4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd`.
The donor and reference-history premises below come from the immutable
candidate package `notes/C-H3-MATERIAL-READ-CONTROL-N/` at
`a165c60b5a1bff79bae05c92630f179fbadf6c51`, especially its model.py,
RESULT.md and THEOREM.md. That package is a computational premise, not
Canon authority or a proof of any newly proposed trajectory.

## 1. Native arithmetic, parity and inverse

Work in `O=Z[j]`, with `1+j+j^2+j^3+j^4=0`, and its fraction field.
Use the ordered integral basis `(1,j,j^2,j^3)`. Define

```text
rho=j^2,       eta=1-rho,       J=1+rho,
eta_inv=1-rho^-1,              gamma=h(J),
h(z)=z*conjugate(z),           q(z)=Tr(h(z))/2.
```

Here `eta_inv` names the displayed element, not the reciprocal of eta.
Both rho and J are units. The identities needed below are

```text
h(rho)=1,
gamma=2+rho+rho^-1,
gamma^2-3*gamma+1=0,
h(eta)=4-gamma,
2-eta=J.
```

Gamma is positive in both real embeddings and is irrational; in particular
`gamma!=1`. All parity statements mean membership in `2O`, equivalently
coefficientwise evenness in the fixed basis. The half-trace account is the
positive integer quadratic form

```text
q(z)=(5*sum_i z_i^2-(sum_i z_i)^2)/2.
```

For an admitted native C pair, write `a=m+d,b=m-d`, with `m,d` integral.
The forward and inverse contacts are

```text
C(a,b)    = (m+rho*d,    m-rho*d),
C^-1(a,b) = (m+rho^-1*d, m-rho^-1*d).
```

Admission is `a-b in 2O`; a refused pair is unchanged. The admitted output
difference is rho times the input difference, so both directions preserve
admission. These formulas are two-sided inverses on the complete carrier.
They preserve the pair sum and Hermitian account.

A B cell has material `(a,b)` and radiation `(g,r)`. If either difference
is odd, B is idle. Otherwise put

```text
d=(a-b)/2, fR=(g-r)/2, m=(a+b)/2, c=(g+r)/2.
```

B1 applies for `d!=0` and `h(fR)=gamma*h(d)`, replacing `(d,fR)` by
`(J*d,J^-1*fR)`. B2 applies for `fR!=0` and
`h(d)=gamma*h(fR)`, replacing them by `(J^-1*d,J*fR)`.
The centers remain fixed. The branches are disjoint: simultaneous nonzero
conditions would require `gamma^2=1`. They are inverse branches, so B is
an involution. They preserve the separate material and radiation sums and
the combined Hermitian account; for example B1 exchanges the two norm
contributions under its defining equality. Zero material `(0,0)` is always
B-idle, for every radiation input.

A full tick uses C with its current matching, then B, then flips the bit.
To invert it, undo the bit flip, apply B, and apply C inverse with the
recovered matching. Inert reserves stay unchanged throughout. These are
native H3 statements; no identity with a separate native U is asserted.

## 2. A residue obstruction to transport from an empty port

For every admitted pair,

```text
a_after-a = -eta*(a-b)/2,
b_after-b = +eta*(a-b)/2.
```

Refusals have zero changes. Consequently every individual slot preserves
its residue modulo the ideal `eta*O` under C, for every matching schedule
and every choice of neighboring values. In particular any C-only history
starting a slot at zero can reach only a value in `eta*O` at that slot.

The quotient `O/(eta)` is `F5`, with j sent to 1. Indeed rho becomes 1;
from `j^2=1` and `j^5=1` follows `j=1`, and the cyclotomic relation then
gives 5=0. Evaluation at j=1 modulo 5 gives the converse quotient map.
The frozen reader amplitude

```text
f=-3-5j-4j^2
```

has residue `-12=3 mod5`, not zero. Thus native C cannot supply this exact
f to a radiation slot initially zero. Even activity at other B cells
does not remove this slotwise obstruction: changing that slot's residue
requires an external boundary or a B change at its own cell. This is not
a prohibition on finite common hardware with a nonzero ready residue.
The initial target below has exactly the residue needed by its arriving f.

## 3. Conditional supplied family and common assembly

The geometry is the frozen 8-by-6 torus. Material and CLK contacts are
vertical; CORR contacts are horizontal. Full107 has matching bit one, so
the successive C matchings at108,109,110,111 are `1,0,1,0`.
Relative time t means absolute time `114+t`.

The following are the supplied premises about the pre-assembly family.
They must be verified when applying the theorem to another family.

* Column4 carries one of two complete donor material blocks, D0 or D1.
  Its material after the actual C108 at row3 is respectively
  `(0,(-1,4,7,3))` or `((1,2,1,1),(-1,4,7,3))`.
  The negative difference is odd. The positive half-difference is
  `(1,-1,-3,-1)=J*f`.
* Columns1,2,3 have zero material. The other source and archive material
  may differ across backgrounds. The original archive reference starts
  with the same material in columns5,7 and has no B there at108..110.
  Its old-only classes at these cuts are the two classes certified by the
  predecessor. These reference facts are supplied, not inferred from an
  account or from the new probe.
* The complete original field plus its ordered source reserve has common
  accounts across the input family. The ordered reserve itself need not
  have common contents. No subsequent native update reads any reserve.

In actual histories donor a is `int(q==1)`; in crossed controls it is
selected independently of `(p,q)`. Both donors and all four old/donor
bit pairs occur in the declared 25/50 domains. Without that coverage,
statements of exactly two or four classes apply only to occurring labels.

Let `v=m*j^k` with the frozen m and k. The algebra below applies to any
nonzero integral v where its specified parity conditions hold. Set

```text
u=1, e=J, r1=-J*f,
b=r1-8*v,
dR=-J*eta^2*v,
g=b+e.
```

At full107 give every row of column6 material `(dR,-dR)`. Supply a common
96-slot radiation vector W. Initially put CORR=b everywhere, CLK=f in
column4, CLK=b in column6, and CLK=g elsewhere. Override

```text
CLK(4,3)  =  f+eta_inv*u,
CLK(4,4)  =  f+(1+rho^-1)*u,
CORR(4,3) = -f-eta_inv*u,
CORR(3,3) = -f-(1+rho^-1)*u.
```

This is SEALED. For DRAIN, v has odd m, and also override

```text
cplus=b+(2+rho)*eta^2*v,
D=cplus+2*u,
CORR(7,3)=CORR(0,3)=D.
```

The preparation is common within a label: its coordinates, values, bit
and start cut have no dependence on p, q or donor a. Different labels
have different specified stocks, not one common account across all labels.
After assembly every step is the unchanged C/B tick, with no later action.

### Exact inverse-C delivery

For arbitrary integral f,u the pair

```text
(f+(1-rho^-1)*u, f+(1+rho^-1)*u)
```

is admitted and maps under C to `(f,f+2*u)`. Its center is `f+u`
and its half-difference is `-rho^-1*u`. The negative reversed pair
maps to `(-f-2*u,-f)`. Thus the actual C108 gives

```text
CLK(4,3)=f,       CLK(4,4)=f+2,
CORR(4,3)=-f,    CORR(3,3)=-f-2.
```

Both target slots change, since `eta_inv*u!=0`. This is literal native
delivery from the common prepared state. It is not a pullback of a
different complete state chosen separately for each input, and it does
not provide a loader for this prepared state from original full0.

## 4. Three native contacts, with guards

All statements in this section are conditional candidate-T consequences
of Section3, not new numerical trajectory observations.

### Parity facts

The two read values have different residues modulo2:

```text
f mod2  = (1,1,0,0),
Jf mod2 = (1,1,1,1),
b mod2  = (-Jf) mod2.
```

The element e=J is nonzero modulo2. Consequently a radiation pair
`(b+e,b+2*z)` is odd for every integral z and makes B idle, regardless
of material. Also

```text
rho*eta^3 = 1 mod2,
rho*eta^2*j^k = j^(k+1)+j^(k+2) mod2.
```

The first identity follows by expansion and the sum of the five fifth
roots. It shows eta is invertible modulo2. The five adjacent root sums
in the second identity are nonzero and none equals `J=1+j^2 mod2`.
For example equality would identify two different unordered root pairs;
their difference cannot be the degree-four cyclotomic polynomial modulo2,
which has all five coefficients nonzero. Nor can it be zero unless the
two pairs coincide. The pair `{1,j^2}` is not adjacent.

For DRAIN with odd m, therefore,

```text
D-b = rho*eta^2*j^k mod2 != 0,
e-(D-b) != 0 mod2.
```

### First contact at108

The target receives `(f,-f)` under actual C. Its negative material
difference is odd, so B is idle. Its positive half-difference is `Jf`,
so B2 applies, with outgoing radiation `(Jf,-Jf)`.

Every other row in column4 has CLK congruent to f and CORR=b. That
radiation difference is odd, so no other bank row acts at108, including
the companion row4. Columns1,2,3 have zero material. Column6 has equal
radiation b and is idle. Columns0,5,7 have odd radiation difference e,
except the DRAIN row in0,7, where the displayed guard inequality still
makes the difference odd. Their vertical CLK pairs are equal g.
Thus no other B at108 exports material-background information.

### Buffer contact at109

Write the bank's outgoing CORR values as `r0=-f` and `r1=-Jf`.
The horizontal matching joins columns4 and5. On donor0 the difference
between r0 and b is odd, so the pair refuses. On donor1,
`r1-b=8*v`, so C gives buffer CORR

```text
R5(0)=b,
R5(1)=b+4*eta*v.
```

Its CLK remains g, hence its radiation difference is odd and its B is
idle. All other buffer rows still have CORR=b and are idle as well.
Any bank B after this transport is simultaneous and cannot alter the
buffer's already determined value at this cut.

The receiver's horizontal partner is column7. SEALED supplies b there.
In DRAIN its exceptional row has D, whose parity differs from b, so that
contact refuses. The analogous source contact between columns0 and1
also refuses in DRAIN. Thus column6 still has uniform material
`(dR,-dR)` and uniform radiation `(b,b)` through full109.
Archive and source guards remain odd. The left companion can move
through zero-material columns but cannot reach column0 before111.

### Receiver contact at110

The next horizontal matching joins5 and6. Both arms are admitted, and
actual C gives

```text
R6(0)=b,
R6(1)=b+2*eta^2*v.
```

The receiver CLK is still b and its material is still `(dR,-dR)`.
Negative radiation has half-difference zero and gives idle B. Positive
radiation has half-difference `-eta^2*v`, with
`dR=J*(-eta^2*v)`, and therefore gives B2. At full110:

| Donor | Material at (6,3) | Radiation at (6,3) |
|---|---|---|
|0|`(dR,-dR)`|`(b,b)`|
|1|`(-eta^2*v,+eta^2*v)`|`(b-rho*eta^2*v,b+(2+rho)*eta^2*v)`|

All other receiver rows remain unchanged. The two material pairs are
different. The receiver-column sum of r0 has values

```text
S6(0)=6*dR,
S6(1)=6*dR+rho*eta^2*v,
```

also different. S6 is a mathematical observation, not a native summing
circuit. The buffer output after C110 is b or `b+2*J*eta*v`; its B
still refuses by the odd guard. The equal DRAIN pair in7,0 is unchanged
at110. All archive B remain idle through110. Their material has undergone
exactly the same C as the unchanged predecessor, so it agrees with that
reference at both cuts108..110, not merely in its account.

The proof uses no material value from source0 or archives5,7 in deciding
the receiver output. It therefore applies to every admitted background
and both donor choices, including the whole crossed family.

## 5. Causal export and what the receiver reads

Compare two preparations with the same background and hardware label but
different donor blocks. Their active fields differ only in column4
material. All radiation and all other material, including column6, agree.
Reserves may differ and are retained separately.

Vertical C cannot move a material difference into another column. Until
column4 has different B tags, equal radiation inputs receive equal C
decisions and outputs everywhere. At a local B with common radiation,
the radiation output depends only on its tag: idle leaves its
half-difference unchanged, B1 multiplies it by J inverse, and B2 by J.
Equal tags therefore preserve radiation equality. The same induction
keeps every coordinate outside column4 material equal through any prefix
with equal bank tags. Any allowed additional boundary would have to
preserve that equality, not merely write outside column4; here there is
no additional boundary.

The first differing tags in this module occur at(4,3),108. The next two
transport contacts explicitly carry the resulting CORR difference to
column6. Its material was common and stayed common until its B at110.
This proves a material-controlled radiation export followed by a distinct
native material write. The receiver is not reading pre-existing different
material in its own column. The guard proof also excludes background
material as the cause of this first recipient distinction.

This finite causal statement is not a closed two-state description of
all later fields. Information can remain in the bank, buffer, other
radiation, source, old archive and inert reserves. Later evolution must
retain whatever context the actual finite verification requires.

## 6. SEALED: exact first subsequent tick

Put `E=eta^2*v`. Immediately after the positive receiver B2, its material
is `(-E,E)` and radiation `(b-rho*E,b+(2+rho)*E)`. Its vertical neighbors
still have material `(-J*E,J*E)` and CLK=b. At C111 it is matched to
row2 vertically and to column7 horizontally. In SEALED that CORR
neighbor is b.

### Odd m forces immediate undo

For odd m, `v mod2=j^k` is nonzero. The incident differences of the
two material rails and CLK are `+rho*E,-rho*E,-rho*E`, up to the
irrelevant orientation sign. The CORR difference is `(2+rho)*E`.
All are odd: rho, eta and j are units modulo2, and `2+rho=rho mod2`.
Every C incident on this receiver cell therefore refuses. B then sees
exactly the previous post-B cell and its inverse branch B1 undoes B2.

No other receiver row changes. At full111 its positive local material
pair and S6 equal the negative values. This is an exact collision of
the two receiver observations, not information loss in the complete
reversible field. It disproves the declared retention gate for every
odd-m SEALED label without asserting any later behaviour.

### Even m prevents this immediate undo

Write `v=2*w`, with w nonzero and integral. All incident receiver C
contacts now admit. At post-C111 the target material center remains
zero and its two half-differences are

```text
d_target=-eta^2*w*(2+rho*eta),
f_target=-J^2*eta^2*w.
```

The norm identities are

```text
h(2+rho*eta)=2+3*gamma,
h(J^2)=gamma^2,
gamma^3=8*gamma-3.
```

After cancelling the nonzero `h(eta^2*w)`, B1 would require
`gamma^2=gamma*(2+3*gamma)`, impossible for positive gamma. B2 would
require `2+3*gamma=gamma^3`, which together with the displayed cubic
gives gamma=1, also impossible. Thus the target B is idle.

The only other affected receiver row is row2. Its half-differences are

```text
d_neighbor=-eta^2*w*(2*J-rho*eta),
f_neighbor=-rho*eta^3*w/2,
h(2*J-rho*eta)=2+gamma.
```

If the radiation difference is odd, B refuses. Otherwise its norm ratio
is `(4-gamma)/(4*(2+gamma))`. B1 would require
`4-gamma=4*gamma*(2+gamma)`, hence `gamma=8/21`, contradicting the
irrational quadratic equation. B2 would require
`4*(2+gamma)=gamma*(4-gamma)`, hence `gamma=-7/3`, contradicting
positivity. No receiver B acts at111.

C preserves the sum on each vertical material rail, so S6 retains both
of its full110 values at both cuts111. The local material pair nevertheless
changes already at post-C111: its r0 change is
`-rho*eta^3*w!=0`. Thus even m removes the forced B undo and supplies
one full tick of S6 retention, but fails literal local-pair retention
at that first post-C cut. Neither statement grants 32-tick S6 retention
or old-archive class preservation.

For completeness, the guard e=J also keeps archive7 B idle at111.
Its CORR change has parity zero or `j^k`, since
`(2+rho)*eta^3=1 mod2`. J is neither zero nor a single fifth root
modulo2. No corresponding claim about archive5 after110 follows here.

## 7. DRAIN: odd-m local survival at111

DRAIN keeps odd m and replaces the ready CORR in7,0 by
`D=cplus+2`, with `cplus=b+(2+rho)*E`. Section4 proves that these
slots leave all three contacts through110 unchanged.

At C111 the positive receiver CORR is cplus and its partner is
`cplus+2`. This pair admits and the receiver becomes `cplus+eta`.
The negative receiver is b; its difference from D is odd, so it remains
b. The receiver's vertical material and CLK contacts still refuse in
the positive arm by exactly the odd-m argument of Section6.
Its new radiation difference is

```text
(b-rho*E)-(cplus+eta)=-2*J*E-eta,
```

which is odd. B is therefore idle instead of undoing the write. In the
negative arm material and radiation remain unchanged and B is idle.
Other receiver rows are unchanged. Both the local material pair and S6
retain their full110 values at both cuts111, with the same two classes.

In the positive arm archive7 CORR becomes `D-eta`. Its radiation
difference is `e-(D-b)+eta`. Modulo2, `e=eta`, so this reduces to
the nonzero `rho*eta^2*j^k`. The negative arm retains the already odd
guard. Archive7 B remains idle at111. Again this does not prove the
condition on archive5 or old-only classes after110.

The drain was installed in the common stock at107. It uses no observation
of the result, no late selection, and no discarded outgoing field value.
The proof establishes one subsequent native tick of local survival, not
the whole preregistered interval111..142 or indefinite retention.

## 8. Full stock and inverse accounting

For a finite material stock M and radiation stock R, define the accounts

```text
A(M,R)=(sum M, sum R, sum_(z in M,R) h(z), sum_(z in M,R) q(z)).
```

The receiver material stock consists of six ordered pairs `(dR,-dR)`;
its material sum is zero, H is `12*h(dR)`, and Q is `12*q(dR)`.
The incoming radiation vector has 96 ordered slots. For SEALED its
accounts, without the material stock, are

```text
Sr(W)=4*f+88*b+36*e,
H(W)=6*h(f)+2*h(f+2)+52*h(b)+36*h(b+e),
Q(W)=6*q(f)+2*q(f+2)+52*q(b)+36*q(b+e).
```

To derive the coefficients, the two exceptional CLK entries have the
same sum and Hermitian account as `(f,f+2)` under their inverse-C
preparation. The exceptional CORR entries are their negatives. The four
other column4 CLK entries equal f, six column6 CLK entries equal b,
36 other CLK entries equal b+e, and 46 CORR entries equal b.
For DRAIN add `2*(D-b)` to Sr, `2*(h(D)-h(b))` to H, and
`2*(q(D)-q(b))` to Q. These are exact differences between two declared
positive-account stocks, not negative or missing resources.

Start from the original field F and retained source reserve R_source.
For a crossed control append both complete donor blocks D0,D1. For
both families append the receiver stock and W. Swap the chosen donor
into column4 when applicable; keep its displaced material in that
donor reserve, and keep the unused donor. Then swap all twelve
column6 material slots and all96 radiation slots with their prepared
stock slots. Retain the twelve displaced worker values and all96
displaced radiation values in their ordered, correctly typed reserves.

Each boundary is a permutation of same-type slots, so it preserves all
four complete accounts. Reversing the swaps in reverse order recovers
the original complete preparation. The source reserve, both controlled
donor reserves, outgoing worker values and outgoing radiation are not
optional entries in this equality. After assembly they remain inert.
Thus for each fixed label common original compound accounts plus common
incoming stocks imply common resulting compound accounts, for every
actual or crossed input. The active field alone need not have common
accounts across those inputs.

Native C/B preserves each active field's own accounts and has the
two-sided inverse of Section1. Appending unchanged ordered reserves
therefore preserves the complete compound accounts and reversibility.
Replaying a common field once is legitimate only after literal field and
matching-bit equality and reserve independence are established. It does
not identify different ordered reserves or erase input multiplicities.
The read's preparation cost is the complete stock above, not merely the
small nonzero target difference. No physical unit is assigned to Q.

## 9. Exact pullback and common-hardware compatibility in A

For a fixed family of original fields F_h and proposed fields P_h, let S
be the union of radiation coordinates on which any P_h differs from F_h.
There is a fixed common radiation-slot replacement producing every P_h
from F_h if and only if all material coordinates agree and, on each
coordinate of S, the proposed value is common across h.

Necessity follows because the replacement does not touch material and
has one supplied value at each chosen slot. For sufficiency, supply those
common values on S and swap them into every F_h; outside S the fields
already agree. Retaining the outgoing values proves the same complete
account equality as in Section8. This criterion does not permit input-
dependent supplied values merely because they have equal norms or accounts.

Applying deterministic native inverses to each frozen endpoint gives a
unique mathematical preimage for each full input history. It does not
establish that those preimages satisfy this common replacement criterion,
the original material constraints, or the specified source boundary.
At the reversed source exchange, the recovered incoming reserve must be
the exact original source q, not just an equal-account stock. Original
full0 hardware must also have the common ready bit and may not encode a
future q in its radiation by choosing a different stock for that q.

The endpoint target in A is an active field. If an early common assembly
exists, it retains its own original outgoing slots; it need not reproduce
the different reserve arrangement of the old late assembly. Its complete
account must be computed for that actual early preparation. These facts
justify A's compatibility test and do not predict whether its six frozen
targets pass. No back-pulled input-dependent field is renamed common
hardware in this proof.

## 10. Scope and falsifiers

The three-contact theorem requires the stated material and ready-phase
premises, common stock, exact native matchings and unchanged isolated
reserves. A missing premise, parity or coordinate error is not a route to
changing a threshold. The explicit three-contact equalities apply before
any later retention question. Their implementation is still checked on
every declared input under the frozen contract.

The SEALED odd-m undo, SEALED even-m local movement and DRAIN odd-m
survival at111 are separate algebraic statements. Only actual continuation
under the frozen 32-tick gates decides longer local or S6 retention,
old-only classes, joint classes, later events or a usable successor family.
Literal motion, splitting within a class, and collision between classes
are distinct observations. None by itself proves loss of information
from the complete reversible system.

The new module starts with its paid assembly at107. No result here proves
its preparation from the unchanged original full0 apparatus, an autonomous
source/probe loader, a universal column-sum reader, worker restoration,
environment reset, repeated fresh inputs or unlimited retained history.
The earlier failures retain their original scope. There is no Canon
promotion, physical occurrence law, native-U assertion or layer lift.

## 11. Separate port compatibility of the two reader amplitudes

Status: conditional candidate-T. This additional algebraic interface lemma
does not assert a combined original-full0 assembly or a new trajectory.
Write the amplitude used above as fB and define

```text
fB=(-3,-5,-4,0),
d_star=J*fB=(1,-1,-3,-1),
fA=J^2*fB=(3,2,1,1).
```

Multiplication by `J=1+j^2` and reduction of
`j^4=-1-j-j^2-j^3` prove both displayed identities exactly.
For positive material half-difference d_star, common radiation `(fB,-fB)`
triggers B2, whereas `(fA,-fA)` triggers B1. Their positive outgoing
radiation pairs are identical:

```text
(J*fB,-J*fB)=(J^-1*fA,-J^-1*fA).
```

The negative material pair has an odd difference and is idle for either
probe. Its outgoing pairs are respectively `(fB,-fB)` and `(fA,-fA)`.
Thus the two readers need not have the same negative radiation word.
Their positive outgoing material half-differences also differ: they are
fB after B2 and fA after B1. Equality of the positive radiation pair is
not equality of the local cells or complete successor fields.

Keep the same buffer ready value `b=-J*fB-8*v`. For the A reader,

```text
(-fA)-b = J*fB-fA+8*v
        = (-2,-3,-4,-2)+8*v
        = j mod2.
```

Its negative CORR input therefore refuses the next C contact with buffer
b. Its positive CORR input is still `-J*fB`, whose difference from b
is exactly `8*v`. Under the same common buffer, receiver and guard
readiness premises as Section4, the two transport steps consequently
give the same buffer values `b,b+4*eta*v`, the same arriving receiver
values `b,b+2*eta^2*v`, and the same native receiver write at110.
No modification of v, its label order, a guard, a time or a gate is used
in this compatibility statement.

The missing premise for composition is full-field readiness. An A endpoint
whose target emits these words has not thereby supplied the prescribed
buffer CORR and CLK, uniform receiver material and CLK, horizontal partner
values, or DRAIN stock. Their common phase and the guard conditions that
exclude other material-background influences must also hold. In particular
preserving the original worker material in column6 is not a proof that it
equals the newly prepared receiver stock. The changed positive bank
material can matter to later evolution as well. Checking a target word,
an account, or an unchanged earlier material prefix cannot replace these
conditions. No combined full0-to-receiver protocol or additional retention
interval follows from this lemma.

### Custody limitation of the associated finite runs

The main A and B runs took place before the alternate checker's source
freeze. This is a protocol deviation from the preregistered requirement
to freeze both implementations before execution. A later checker replay
is recorded as reproduction, not as satisfaction of that promised frozen
blind confirmation. This limitation does not change any scientific gate
or promote a finite claim, and it must accompany the associated numerical
results. The identities and conditional proofs above use no such replay.
