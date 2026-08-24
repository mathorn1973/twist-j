# P-QDD-COMMUTATOR-SATURATION-CLOSURE-1 result

Status: `PROVED AND AUDITED IN THE FROZEN CLASS / PUBLIC REPLAY PENDING / DICTIONARY UNADOPTED / CANON UNCHANGED`

## Decision

```text
SATURATION-DICTIONARY-BOUNDARY
```

One formal execution returned zero, wrote empty stderr and produced the exact committed 27-line output with 20/20 exact gates passing. The accepted verifier was not executed before its public pin and was not rerun after the formal execution.

## 1. Complete repeatable rational pure branch class

For complementary target-independent `G`-orthogonal projectors `P,Q`, define

```text
A_rep(Q)={T in M_4(Q): T^sharp T=Q, QT=TQ=T}.
```

The written proof gives the complete classification

```text
A_rep(Q)={OQ: O in O(W,G|W)(Q)},
W=QV.
```

The effect equation kills the `P` input, the two-sided support puts the range in `W`, and the restriction is an isometry of a finite-dimensional positive-definite rational space, hence an orthogonal automorphism. Conversely every rational orthogonal automorphism of `W`, extended by zero on `PV`, gives a member.

This is completeness of the named rational pure repeatable branch class. It does not claim that every possible physical apparatus architecture lies in this class.

## 2. Exact commutator-saturation selector

On `W`, let

```text
A=Q D_J Q|W,
Xi_T=OA-AO,
b_W([v])=(v^T G v, v v^T G/(v^T G v)).
```

Define `COMM-SAT(T)` mathematically by

```text
b_W([O A v])=b_W([A O v]) for every nonzero v in W.
```

The pure record is projectively faithful. Since `OA` and `AO` are invertible, equality for every ray forces `OA=lambda AO` with `lambda=+1` or `-1`. The negative sign would make `A` similar to `-A`, impossible because `tr(A)=-3/4`. Therefore

```text
COMM-SAT(T) iff Xi_T=0 iff OA=AO.
```

The rational `H`-orthogonal centralizer of `A` is exactly

```text
{+I_W,-I_W}.
```

Thus

```text
COMM-SAT(T)
iff Xi_T=0
iff O=+I_W or O=-I_W
iff T=+Q or T=-Q
iff [T]^2=[T].
```

Under the registered sign equality this is one branch class. Only at the final target comparison does `Q=E_high`, so the surviving class is the Lueder HIGH sign class.

The verifier audits the exact carrier, centralizer eliminations, pure-record reconstruction, the two sign representatives and a noncentral involutive witness. The universal theorem is carried by the written proof.

## 3. Current architecture does not derive the premise

The authoritative v59 decoder text states that `D_clock` is terminal in functional order, decoder outputs do not feed `U`, and totality, uniqueness and completeness of the decoder remain open. The completion contract is explicitly only a schema. It separately states that a terminal `emit_rule_id` does not establish state terminality, maximality is optional, and no completion-wide terminality theorem is supplied.

Therefore none of

```text
terminal functional stage
read-only output
completion-contract conformance
```

currently implies `COMM-SAT(T)`.

This is a first-class nonimplication boundary. Reading the existing word `terminal` as a state fixed point, or the word `complete` as maximal post-state separation, would strengthen the public architecture without evidence.

## 4. Minimal remaining physical dictionary

Public CORE states

```text
Time is a counter. Space is read through commutators.
```

but also limits physical interpretations to registered dictionary strength. The exact remaining physical proposal is therefore separated from the theorem:

```text
TERMINAL-EVENT-COMMUTATOR-SATURATION [D candidate]
  a terminal saturated QDD post-event record is read as complete only when the
  canonical post-state port has no residual internal commutator readout,
  equivalently Xi_T=0.
```

This row is not proved or adopted by this probe. It is the smallest explicit physical premise found by the attack: no fitted number, target projector, symmetry group, hidden apparatus parameter or writeback enters it.

If the owner later adopts this dictionary in a separate Canon fold at grade `D`, the theorem above selects the single Lueder sign class inside the complete named rational pure repeatable branch class. The grade and scope of that later O2 movement cannot exceed the adopted dictionary and class boundary.

## Candidate theorem rows

After byte-identical public x86_64 and aarch64 replay, a later separate fold may register at most:

```text
QDD-REPEATABLE-PURE-BRANCH-CLASS            [T]
QDD-COMMUTATOR-SATURATION-SELECTION          [T]
QDD-SATURATION-ARCHITECTURE-NONIMPLICATION  [T]
```

A separate owner-approved fold may additionally consider only at dictionary grade:

```text
TERMINAL-EVENT-COMMUTATOR-SATURATION        [D]
```

The `D` row is not earned by this probe and is intentionally absent from the theorem ceiling.

## Consequence for O2

Global O2 remains open under this probe. The mathematical selector is no longer the missing piece. The remaining issue is an explicit physical adoption of what a saturated terminal event means, plus the public decision about the admissible physical class at the scope required by `QDD-INSTRUMENT-APPARATUS`.

O1 is untouched.

```text
SAMPLING NOT PROVIDED
```
