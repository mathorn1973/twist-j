# P-TM-SYM2-MEASURE-1 selector-class definition input (NON-CANONICAL)

```text
C-TM-SELECTOR-CLASS-1
NON-CANONICAL / PARTIAL DEFINITION INPUT
STOP-PREDEFINITION / NO-PROBE / NO PUBLIC STATUS
```

This note is a partial definition input for the selector predefinition of
`TM-SYM2-MEASURE [H]` (issue #119,
`notes/canon/P-TM-SYM2-MEASURE-1-PREDEFINITION.md`). It proposes one exact
selector-class definition for review. It is not `READY-DEFINITION`, not a
preregistration, not a verifier, not a run, not evidence, and not a status
proposal. It contains no computation results. The lane remains `STOP` and
no formal probe is authorized by anything below.

## Authority pin

```text
Canon:                 Public Canon v15
state:                 ACTIVE
tag:                   canon-v15
activation commit:     8f4e176c5d76f519d3493e56e438aba7856e1f01
content commit:        a850753348583e611bf7ccd5aa074030dc7e12f5
Canon SHA-256:         53237ec25b3782e833367c998c049d19459189a21c2a36638dd9e1600335976b
Canon bytes:           89288
owner row:             TM-SYM2-MEASURE [H]
scheduler:             MEASURE / ROOT / STOP / FORMAL
public lock:           issue #119
```

## 1. Design principle offered for review

The selector should not choose lines. It should transport involution
structure of the declared drive onto involution structure declared on the
registered frame, with everything else delivered by an exact enumeration
and an exact stationary law. Weights are stream-side pushforward weights,
never choices. Whether this principle canonically selects anything is a
question the future evaluation must answer; this note only makes the
question exact.

## 2. Carrier ansatz (declared, not forced)

Let `theta_n = s_2(n) mod 2` be the registered drive cut of the counter
component of the declared autonomous state `Omega = N_0 x F_5^6`, with the
registered doubling `(theta_(2m), theta_(2m+1)) = (theta_m, 1 - theta_m)`.

```text
q(n) := (theta_(n-1), theta_n, theta_(n+1)),   n >= 1,
W3   := the set of length-3 words occurring in the drive.
```

Because `theta` is cube-free at the relevant lengths (the registered
bracket machinery of TIME-CUT-READING excludes `000`; `111` is excluded
symmetrically), `W3` consists of the six words other than `000` and `111`.

DECLARED ANSATZ, with its risk stated: the radius-1 (length-3) window
quotient is NOT a publicly forced complete selector quotient. It is a
proposed carrier. That `|W3|` equals the number of frame lines is a
numerological coincidence risk, not evidence for the ansatz; the
canonicality test below must carry that risk, and any alternative window
radius or quotient is a different candidate definition.

## 3. The complete selector map and its conventions

```text
Sel(n, psi) := s(q(n))     for n >= 1 and every psi in F_5^6,
```

where `s : W3 -> Lines` is a class member per section 5.

```text
n = 0 convention   the tick n = 0 precedes the first complete window and
                   emits no selection; the selector domain is n >= 1.
                   This convention is part of the ansatz.
update convention  theta_n is indexed as in the registered selection law
                   (the drive value consumed at tick n); the window adds
                   no new convention beyond centering at n.
seed semantics     the drive is a function of n alone, so Sel(n, psi) is
                   constant in psi: seed-independence is discharged by
                   construction, for every seed and the full ensemble
                   alike. The selector reads the declared autonomous
                   state through its counter component; it is not a
                   function of the checkpoint psi alone.
starts             all n >= 1; no start is discarded.
```

## 4. Line typing and the proposed pairing structure

`Lines` is the registered ordered six-line carrier of
`GOLDEN-SIX-LINE-SYM2-FRAME [T]`, in its registered order and coordinates:
`v1 = (0,1,phi)`, `v2 = (0,1,-phi)`, `v3 = (1,phi,0)`, `v4 = (1,-phi,0)`,
`v5 = (phi,0,1)`, `v6 = (phi,0,-1)`, with `r = phi + 2` and projectors
`P_i = v_i v_i^T / r`.

PROPOSED NEW STRUCTURE, declared as such: the pairing involution

```text
sigma := (v1 v2)(v3 v4)(v5 v6),
```

realized on the registered coordinates as the sign flip of the phi
coordinate. `sigma` is NOT a registered linear involution of the frame; it
is a label structure this definition adds, and its consistency with the
registered vectors (each pair differs exactly by the phi-coordinate sign;
the pairs are the coordinate blocks `{x = 0}`, `{z = 0}`, `{y = 0}`) is a
checkable clause of the definition, not an inherited fact. Any competing
pairing is a different candidate definition.

## 5. Selector class, equivalence, and gauge

Window-side structure map: bit negation `N(w) = wbar` (0 and 1 exchanged
in all three slots). Its pedigree as a structure map, not a gauge: the
registered doubling flips the second child bit, and the registered lift
reads the bit as a sign, `Theta_n^2 = (-1)^(theta_n)`; negation is
therefore the drive's own registered flip.

```text
CLASS   Sel_class := { s : W3 -> Lines  total,
                       s(N(w)) = sigma(s(w)) for every w,
                       s surjective }.
```

Surjectivity is the row's own scope (the hypothesis under test says the
stream selects the six lines, not a subframe). No clause of the class
mentions frequencies, moments, densities, or Born values.

```text
GAUGE   G := Aut(Lines, sigma), the full automorphism group of the
        extended structure: all projective-linear transformations over
        Q(phi) that preserve the six-line set AND normalize sigma
        (g sigma g^(-1) = sigma as line permutations).
EQUIV   s ~ g o s for g in G.
```

The gauge is the automorphism group of the declared structure, not any
matrix-class intersection. Its order, its relation to the full projective
stabilizer of the bare line set, and whether Galois conjugation of
`Q(phi)` preserves the structure are outputs of the future evaluation,
not inputs of this definition.

## 6. Canonicality test and checker separation

```text
CANONICAL       exactly one G-orbit of Sel_class;
NONCANONICAL    at least two G-orbits (the checker must then name exact
                orbit invariants);
EMPTY           Sel_class is empty;
STOP            enumeration, gauge computation, or exactness incomplete.
```

Checker requirement (result neutrality): the future public checker must
separate `AUDIT PASS` (exact arithmetic, well-defined structures,
provably complete enumeration of the class and of the gauge) from the
scientific route (the computed orbit count routes the decision). The
checker may not embed an expected orbit count, an expected invariant
list, or an expected weight vector; a legitimate scientific outcome is
never a checker failure.

## 7. Stream-side pushforward weight and the limiting measure

The registered doubling induces exact child maps on windows,

```text
L(a,b,c) = (1-a, b, 1-b),      R(a,b,c) = (b, 1-b, c),
```

and the transfer `T[x][w] = [x = L(w)] + [x = R(w)]`. The weight object
is defined procedurally:

```text
f       the stationary law of T/2 on W3, provided the future evaluation
        certifies (i) the exact transfer identity between consecutive
        dyadic scales of the sliding window census, in the same
        evidentiary shape as the registered GYRON-DENSITY row, and
        (ii) uniqueness of the stationary law by exact rank computation;
nu_s    := the pushforward of f under s (the STREAM-SIDE PUSHFORWARD
        WEIGHT of each line; the term "physical weight" is not used and
        no physical reading is claimed at this layer);
M_TM(A) := sum_w f_w Tr(P_(s(w)) A) P_(s(w))    as an operator on Sym2.
```

The convergence clause is exactly (i) plus (ii); no stronger limit claim
is made, and no value of `f`, `nu_s`, or `M_TM` is asserted in this note.

## 8. Factor-map slots offered to the Born block (typing only)

Two typed stream maps are offered as CANDIDATE fillers for the row's
factor-meaning slots, with their values left to the evaluation:

```text
third   the leading-pair density map: the stationary density of the
        leading pair (w1, w2) of a window, from the registered pair
        census machinery;
half    the conditional continuation weight: f_(w1 w2 w3) / f_(w1 w2)
        for the admissible continuations of a branching leading pair.
```

TYPE LIMIT, stated up front: by cube-freeness the extreme pairs `00` and
`11` have exactly one admissible continuation, so their continuation
factor is 1 by type; the (third, half) factorization can at most cover
windows with a mixed leading pair. These maps therefore CANNOT by
themselves derive a universal Born halving, and no such derivation is
claimed. Whether `third` and `half` may be read as the row's `1/3` and
`1/2` through a typed Born map remains exactly the reserved dictionary
decision of the predefinition (its false shortcuts 5 and 7).

## 9. Falsifiers and routes (aligned with the predefinition)

```text
EMPTY class, or the sigma consistency clause fails against the registered
  vectors, or the stationary law is not unique      -> the definition is
  wrong at the named clause; NEGATIVE or STOP per section 6 of the
  predefinition.
NONCANONICAL orbit count                            -> NEGATIVE /
  NONCANONICAL route for a probe run under this definition; a fired
  negative is preserved, not repaired by changing the class.
Unequal pushforward weights, commutant departure, or a changed 5:2
  ratio at evaluation time                          -> NEGATIVE per the
  registered row.
```

## 10. Residual definition debt (what this input does NOT fill)

```text
carrier completeness   whether any window quotient is the right selector
                       carrier at all (section 2 risk);
Born carrier, Born map, factor typing decision (section 8 limit);
density bridge         no relationship between the line weights and
                       GYRON-DENSITY is proposed;
action layers          source and target layers, lifts, and gates from
                       the L1 stream to the terminal L6 measure;
certificate schema     the exact public checker and its completeness
                       proofs (section 6 requirement only names them).
```

This input adds no registry row, no dependency, no gate, no evidence, and
no status. `TM-SYM2-MEASURE [H]` and its lane remain exactly where the
predefinition holds them: `STOP`.
