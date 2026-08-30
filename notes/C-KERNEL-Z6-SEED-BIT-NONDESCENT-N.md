# C-KERNEL-Z6-SEED-BIT-NONDESCENT-N

```text
STATUS:             NON-CANONICAL INCUBATION NOTE
AUTHORITY:          NO NORMATIVE AUTHORITY
TARGET LINE:        PUBLIC
PUBLIC CANON:       Public Canon v71 / canon-v71
PUBLIC BASE:        d627733fbf0cd2fe3733b668140c2c0bcdc81b61
CONTENT COMMIT:     a77d720433c19976f9ab663d023ec9364eac34eb
CLAIM ISSUE:        #675
ACTION LAYER:       L1 EXACT KERNEL DYNAMICS ONLY
TIMING:             POST-RESULT / RESULT-EXPOSED
METHOD:             PROOF-FIRST COROLLARY
SCIENTIFIC CREDIT:  NONE
EVIDENCE CREDIT:    NONE
FORMAL PROBE:       NONE
PREREGISTRATION:    NONE
VERIFIER / RUN:     NONE
CANON CHANGE:       NONE
REGISTRY CHANGE:    NONE
DEPENDENCY CHANGE:  NONE
GATE CHANGE:        NONE
FRONTIER CHANGE:    NONE
```

This note records a theorem-grade corollary of one existing public theorem
and one public definition. It creates no new public claim, evidence credit,
Canon status, Registry row, dependency row, gate, probe, verifier, run
permission, decoder result, or physical interpretation.

The possible future theorem spelling is reserved here as

```text
KERNEL-Z6-SEED-BIT-NONDESCENT
```

but no promotion is proposed now.

## 1. Result-exposed disclosure and prior lineage

The equation, proof, and state-versus-orbit boundary were known in the owner
session before issue #675 was opened and before this note was written. This is
not a blind preregistration. The method is called proof-first only because the
corollary is proved from the public clauses rather than inferred from a new
enumeration.

PR #190, merged as

```text
178d5cf9c108379dddd48ddb53b98077b2c227ce
```

added the non-canonical predecessor

```text
notes/canon/P-DMATTER-TOTAL-1-OMEGA0-START-FAMILY-OWNER-FREEZE.md
```

That note already recorded proposal-local common-tail non-descent of genesis
data, including five genesis heads per synchronized tail class. The present
note makes no first-in-program or novelty claim. Public rows
`QPAIR-CROSS-SECTOR-NONDESCENT [T]` and
`QPAIR-HERM-INTEGER-NONDESCENT [T]` are additional, differently typed public
non-descent owners.

The contribution frozen here is narrower: the exact two-sheet seed bit, the
exact lower bound `n >= 1`, and the distinction between the complete
instantaneous state of the declared automaton and a complete headed orbit.

The name deliberately avoids `SHEET-DESCENT-TYPE`, which is already used by
the distinct L4 ramified-Hermitian note merged in PR #673. That note is a
naming and promotion-governance precedent only, not a scientific dependency.

## 2. Public inputs and types

Put

```text
X    = F_5^6,
X_z  = {x in X : z_6(x)=z},
X_14 = X_1 union X_4,
E_n(x) = pr_checkpoint(U^n(0,x)).
```

The public definition node `DEF-AUTONOMOUS-STATE` declares

```text
Omega = N_0 x X,
U^n(0,x) = (n,E_n(x)).
```

For `n >= 1`, use the public target-sheet label

```text
q_n = 4 + 2 theta_(n-1) mod 5.
```

Define the initial seed bit

```text
b_0:X_14 -> F_2,
b_0(x) = [z_6(x)=4].
```

Thus `b_0=0` on `X_1` and `b_0=1` on `X_4`. For each `n >= 0`, define the
complete instantaneous-state map on this seed family by

```text
A_n:X_14 -> Omega,
A_n(x) = U^n(0,x) = (n,E_n(x)).
```

The proof inputs are exactly

```text
KERNEL-Z6-SYNCHRONIZATION [T], clause (ii),
DEF-AUTONOMOUS-STATE.
```

`DEF-AUTONOMOUS-STATE` is a normative definition node rather than a Registry
claim. The public dependency ledger already gives
`KERNEL-Z6-SYNCHRONIZATION` a `REQUIRES` edge to that node.

## 3. Exact corollary

For every fixed known `n >= 1`,

```text
A_n:X_14 -> {n} x X_(q_n)
```

is exactly two-to-one. Every fibre contains exactly one seed from `X_1` and
one seed from `X_4`.

Consequently, for every `n >= 1` there is no total map

```text
h_n:{n} x X_(q_n) -> F_2
```

such that

```text
h_n(A_n(x)) = b_0(x)
```

for every `x in X_14`. Equivalently, the initial bit `[z_6(x)=4]` does not
factor through the complete instantaneous autonomous state at any tick
`n >= 1`.

This is the primary statement. Its exact falsifier is one fixed `n >= 1` and
one total `h_n` satisfying the displayed equation on all of `X_14`. Such an
`h_n` would also contradict clause (ii) of the source theorem.

There is also a global restatement. Let

```text
C_14^+ = {(n,x) : n >= 1 and x in X_14},
Y_14^+ = {(n,y) : n >= 1 and y in X_(q_n)},
A(n,x) = U^n(0,x).
```

Because the counter separates the time slices, `A:C_14^+ -> Y_14^+` is
exactly two-to-one, again with one `X_1` seed and one `X_4` seed in every
fibre. Hence no single total `h:Y_14^+ -> F_2` recovers `b_0` on every slice.
This global no-go is only a consequence of the per-time theorem; the declared
falsifier remains one `n` and one complete `h_n`.

## 4. Proof

Clause (ii) of `KERNEL-Z6-SYNCHRONIZATION [T]` states that for every
`n >= 1` the restrictions

```text
E_n|X_1:X_1 -> X_(q_n),
E_n|X_4:X_4 -> X_(q_n)
```

are separate bijections.

Fix `n >= 1` and `y in X_(q_n)`. There is a unique `x_1 in X_1` and a unique
`x_4 in X_4` such that

```text
E_n(x_1) = y = E_n(x_4).
```

The counter value is the same, so the complete declared autonomous states
coincide:

```text
A_n(x_1)
  = (n,E_n(x_1))
  = (n,y)
  = (n,E_n(x_4))
  = A_n(x_4).
```

But

```text
b_0(x_1)=0,
b_0(x_4)=1.
```

Therefore `b_0` is not constant on any fibre of `A_n`, and no such `h_n`
exists. The two bijections also show that these are exactly the two points in
each fibre. This proves the per-time statement. Disjointness of the
counter-labelled target slices proves the global restatement. QED.

This is theorem-grade as a corollary. It creates no independent evidence or
scientific credit beyond the registered inputs.

## 5. Exact time boundary and nonaccumulation

At genesis,

```text
A_0(x)=(0,x).
```

Thus `A_0` is injective, and

```text
h_0(0,x)=[z_6(x)=4]
```

gives a total factorization on `{0} x X_14`. The lower bound `n >= 1` is
therefore exact: the bit factors at genesis and does not factor through any
later instantaneous state.

At the first step, since `q_1=4`,

```text
U|({0} x X_14):{0} x X_14 -> {1} x X_4
```

is exactly two-to-one. Thus the same-time collision is already a collision of
the declared update `U`; it is not introduced by dropping the counter or by
applying `pr_checkpoint` afterwards.

The multiplicity does not accumulate. Clause (ii) says that it remains
exactly two at every fixed `n >= 1`. Equivalently, once the two source sheets
have merged, for every `n >= 1` the one-step restriction

```text
U|({n} x X_(q_n)):{n} x X_(q_n) -> {n+1} x X_(q_(n+1))
```

is bijective. This follows either from the declared single-generator update
on the common sheet or by composing the two successive bijections in clause
(ii). This note does not claim that `U` is globally bijective, and it does not
claim that a new bit is lost at every tick.

The selected kernel generators remain bijections. The union map is
noninjective because the state-dependent selector sends the two source sheets
through different bijective branches onto the same target sheet. No loss or
singularity is assigned to an individual generator.

## 6. Carrier comparison

For `x in X_14`, let the complete headed forward orbit be

```text
kappa_x = (U^k(0,x))_(k>=0).
```

Its head is `kappa_x(0)=(0,x)`. Therefore

```text
B(kappa_x)=b_0(x)
```

is well defined: the complete headed orbit retains the seed bit trivially
through its genesis head. By contrast, after the first merge the two headed
orbits have the same future tail.

The exact factorization boundary is:

| carrier | does `b_0` factor? | reason |
|---|---:|---|
| genesis checkpoint `x` | yes | it contains `z_6(x)` |
| genesis state `(0,x)` | yes | `A_0` is injective |
| checkpoint `E_n(x)` at known `n >= 1` | no | one `X_1` and one `X_4` seed share every fibre |
| complete instantaneous state `(n,E_n(x))`, `n >= 1` | no | the collision occurs at the same counter value |
| complete headed orbit `kappa_x` | yes | its genesis head is retained |
| common future tail beginning after the merge | no | the paired seeds have the same tail |

The word `headed` is essential. An orbit carrier that has forgotten or
quotiented its genesis head is a different object; PR #190 records one such
common-tail boundary.

The public dependency

```text
DEF-DECODER-MATTER  DEF-AUTONOMOUS-STATE  REQUIRES
D_matter reads a forward orbit
```

places the declared matter decoder on an orbit carrier architecturally. It is
context, not a proof premise, and it establishes neither decoder totality nor
a physical ontology. This note proves no decoder theorem.

## 7. Companion factorization pattern

`RAMIFIED-TM-SYMPLECTIC-ORIENTATION [T]` records a different pattern for a
different binary datum. Its public count character does not factor through
the checkpoint alone on the full unindexed forward carrier: the public
collision `psi_4=psi_6` has opposite values. That character does factor
through the complete autonomous state `(n,psi)`, because the counter separates
the two times.

For the present seed bit, adding the counter cannot repair the collision,
because it occurs at the same fixed `n`. The orientation row is therefore a
companion contrast and not a logical dependency. This note prevents its
positive factorization statement from being generalized to arbitrary binary
data.

This comparison creates no new failure-class or first-in-program claim.

## 8. Census boundary

Neither `CENSUS-Z5-SHEET [C]` nor `CENSUS-313 [C]` is a premise. The theorem
uses the algebraically defined carrier `X_14` and assigns it no recurrence,
living-set, measure, or census meaning.

A separate `C`-bounded consequence may identify the recurrent support with
`X_14` and use the public census `2*5^5=6250`. That consequence must cite the
census rows separately and does not strengthen the L1 proof above.

No entropy row is used.

## 9. Public-form boundary

No unavailable internal form or private obligation is a premise, blocker,
lineage source, consistency input, or evidence source for this public-form
corollary.

This note makes no identification between the declared public update and an
internal presentation. In particular, it transfers no statement to a
different flow, to `J`, or to any physical dynamics.

## 10. Physical and decoder firewall

Here `complete autonomous state` means exactly the complete instantaneous
state of the declared L1 automaton,

```text
Omega=N_0 x F_5^6.
```

It does not mean the complete physical existent. The public program does not
currently own a choice among an instantaneous automaton state, a complete
headed orbit, a tail quotient, or another typed carrier as the physical
carrier.

This note does not amend, fence, reinterpret, support, or contradict
`ELECTRON-SIGN` or any `ELECTRON-*` row. Those rows are not proof premises.

No claim is made here about

```text
physical ontology or physical completeness,
charge or charge-sign loss,
measurement, apparatus, event, or collapse,
thermodynamic entropy or entropy production,
an arrow of time or physical irreversibility,
probability, measure, or decoded logs,
decoder completion or totality,
L2-L6 lifting.
```

The valid short reading is only

```text
After tick 0, the complete instantaneous state of the declared L1 automaton
does not determine the initial X_1-versus-X_4 seed bit.
```

It must not be restated as

```text
the world forgets the bit.
```

## 11. Registry disposition and promotion trigger

No Registry row is proposed. The result is a direct corollary, and no current
public result needs it as a stable named dependency.

A future L1 theorem row named

```text
KERNEL-Z6-SEED-BIT-NONDESCENT [T]
```

becomes procedurally justified only if a concrete public result needs this
same-time nonfactorization through `(n,psi)` as a named `REQUIRES` or
`BOUNDED_BY` owner, or if a public state-versus-orbit descent taxonomy needs
an exact owner for it.

Any promotion must preserve

```text
the result-exposed provenance,
the exact n>=1 theorem and n=0 control,
the PR #190 prior-lineage disclosure,
the state-versus-headed-orbit distinction,
the census and physical firewalls,
no new evidence credit.
```

Companion symmetry, interpretive interest, or possible future physical use is
not by itself a promotion trigger.

## 12. Non-actions

```text
Canon change:                 none
Registry change:              none
Normative change:             none
Dependency change:            none
Gate change:                  none
Evidence change:              none
Frontier change:              none
Probe / verifier / breaker:   none
Formal run:                   none
Decoder fold:                 none
Physical fold:                none
```
