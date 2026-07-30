# P-DMATTER-TOTAL-1 Physical-Instrument Predefinition (NON-CANONICAL)

```text
STATUS:                 PREDEFINITION / NO PHYSICAL SELECTION
AUTHORITY:              NOT CANON
PUBLIC BASE:            Public Canon v23
PUBLIC CANON TAG:       canon-v23
ACTIVATION COMMIT:      4ac41b4fac3a3794a6e9d5be1e2027d324edb806
CONTENT COMMIT:         7830d852229ffc06c9d287d026c8ece290bf339b
CANON SHA-256:          f842b613d6f65fe07ddab92ddbe1fb9fec89217d52b781571b7380281c3fb2b1
CANON BYTES:            116017
PUBLIC MAIN BASE:       5e1f6cc5bb45ba5f4816439ee6b47a28f9be2910
PROPOSAL-ID PACKAGE:    d9e10e605e937971ea56974fb1afaecf36bfc1ebad3e1ff7ed304914f208b266
OWNER RULING:           0cb5d0e46d2a76d5170ac399b15626b558256984cf2d01c4029441ca0d248ca5
CLAIM ISSUE:            107
QDD STATUS:             O / STOP, unchanged
FORMAL RUN:             NONE
REGISTRY CHANGE:        NONE
DEPENDENCY CHANGE:      NONE
GATE CHANGE:            NONE
```

This note performs the second definition-only action authorized by the OD4
owner ruling. It defines an exact algebraic instrument surface, one explicit
Luders candidate, and one same-effect counterexample. It does not select a
physical apparatus, claim a unique instrument, fill a public completion
identifier, open a probe, or change `QUADRATIC-DECODER-DATA`.

The word `physical` in the title names the obligation being prepared. The
surface defined below remains algebraic until a public kernel-to-apparatus
selection and its layer gate are supplied.

## 0. Falsification first

This predefinition is violated if a later candidate does any of the following
without a new owner ruling made before classification:

1. treats `E_low` or `E_high` as an endomorphism of the finite set `Veff`;
2. reconstructs a unique instrument from its effects;
3. quotients instruments only by equality of effects;
4. declares the singleton Luders family to be the complete physical universe
   without an independently frozen kernel or apparatus selection principle;
5. emits a bare null or a normalized zero state when an outcome has zero
   probability;
6. identifies forgetting an outcome with applying a fresh instrument for the
   merged effect;
7. makes the five-field `D_scoped` record emit a realized outcome or a
   post-event state;
8. infers a layer, gate, pointer, feedback channel, or public identifier from
   the algebra below;
9. moves the parent QDD row from `O / STOP`.

After a classification opens, changing any frozen carrier or state domain,
apparatus, coupling, pointer, reduction, physical admissibility predicate,
exact `K` or effect list or certificate, equivalence, `K/E` boundary, outcome
or post-event semantics, Born pairing, normalization or completeness rule,
MatterData outcome mapping, coarse-graining rule, or output meaning returns
`FIRE-POSTHOC`.

## 1. The required carrier is linear, not `Veff`

Let

```text
H_Q = (Q^4, <x,y>_G = x^T G y),

G       = I_4 - (1/5) 1 1^T,
G^(-1)  = I_4 + 1 1^T,
A^sharp = G^(-1) A^T G,

End_Q(H_Q) = M_4(Q).
```

The finite set

```text
Veff = ell(F_5)^4
```

is the Route A input-amplitude set. It is not closed under the proposed
effects. For `e_1=(1,0,0,0)^T`:

```text
E_low e_1  = (1,1,1,1)^T/4,
E_high e_1 = (3,-1,-1,-1)^T/4,
```

and both vectors lie outside `Veff`. Therefore every instrument operator is
typed in `End_Q(H_Q)`, never as `Veff -> Veff`.

Define exact rational state carriers using finite sums:

```text
State_G(Q)
  = { rho = sum_i q_i v_i v_i^T G, with the sum finite :
      q_i in Q_(>=0), v_i in Q^4, Tr(rho)=1 }.

Substate_G(Q)
  = { sigma = sum_i q_i v_i v_i^T G, with the sum finite :
      q_i in Q_(>=0), v_i in Q^4, 0 <= Tr(sigma) <= 1 }.
```

Every such matrix is `sharp`-self-adjoint and `G`-positive. Equality is input
equality in `M_4(Q)`. These carriers are closed under every rational event map
defined below.

Proposal-local names:

```text
CAND-QDD-CARRIER-HQ-G
CAND-QDD-STATE-G-RATIONAL
CAND-QDD-SUBSTATE-G-RATIONAL
CAND-QDD-EQ-RATIONAL-MATRIX
```

They are not public completion identifiers.

## 2. Algebraic effects

With `1=(1,1,1,1)^T`, retain the exact Route A candidates

```text
E_low  = (1/4) 1 1^T,
E_high = I_4 - E_low.
```

They obey

```text
E_a^sharp       = E_a,
E_a^2           = E_a,
E_low E_high    = 0,
E_low + E_high  = I_4.
```

The proposal-ID package names them

```text
CAND-EFFECT-GRAM-LOW
CAND-EFFECT-GRAM-HIGH.
```

Those two identifiers remain `ALGEBRAIC_ONLY`. They are explicitly forbidden
from filling the public `quadratic_manifest.effect_ids` slot.

## 3. Complete algebraic universe and incomplete physical universe

Freeze the complete algebraic single-operator universe

```text
Instr_alg(E_low,E_high)
  = { (K_low,K_high) in M_4(Q)^2 :
      K_a^sharp K_a = E_a for a in {low,high} }.
```

This is a total set definition. It is not the complete physical instrument
universe. A physical admissibility predicate must still be derived from a
public apparatus carrier, ready state, coupling, pointer, and reduction to
`K_a`.

The labels `low` and `high` are fixed and are not quotiented by outcome swap.
They denote the one-dimensional and three-dimensional eigensectors of `G`
with eigenvalues `1/5` and `1`. They are not yet physical detector-click
identifiers.

For every member of `Instr_alg`, define the event operation, weight, and
tagged conditional state:

```text
I_a(rho) = K_a rho K_a^sharp,
p_a(rho) = Tr(I_a(rho)) = Tr(E_a rho),

Post_a(rho)
  = IMPOSSIBLE                     if p_a(rho)=0,
  = POST(I_a(rho)/p_a(rho))        if p_a(rho)>0.
```

The `IMPOSSIBLE` tag is an exact value. It is not null.

Because

```text
sum_a K_a^sharp K_a = E_low + E_high = I_4,
```

the event weights are nonnegative and sum to one on `State_G(Q)`. The
conditional nonzero branch returns another exact rational `G`-state.

Proposal-local names:

```text
CAND-QDD-INSTRUMENT-UNIVERSE-ALGEBRAIC
CAND-QDD-OUTCOME-SECTOR-LOW
CAND-QDD-OUTCOME-SECTOR-HIGH
CAND-QDD-EVENT-OPERATION
CAND-QDD-BORN-PAIRING-TRACE
CAND-QDD-POST-STATE-TAGGED
CAND-QDD-NORMALIZATION-COMPLETENESS
```

None is a physical public ID.

## 4. Explicit pre-result candidate: the Luders family

Define one member before any classification:

```text
K_low^L  = E_low,
K_high^L = E_high.
```

Then, exactly,

```text
(K_a^L)^sharp K_a^L = E_a,
sum_a (K_a^L)^sharp K_a^L = I_4.
```

This is an explicit rational projective instrument candidate. The definition
is `K_a^L:=E_a`; it is not a reverse inference from an observed effect.

The proposal-local matrix names are

```text
CAND-QDD-INSTRUMENT-LUDERS
CAND-QDD-K-LUDERS-LOW
CAND-QDD-K-LUDERS-HIGH.
```

This family is not physically selected by the present program. Calling it the
only admissible family would insert the desired answer into the input.

## 5. Mandatory negative control: same effects, different instrument

Let

```text
P_12 =
  [0 1 0 0
   1 0 0 0
   0 0 1 0
   0 0 0 1].
```

It satisfies

```text
P_12^T G P_12 = G,
P_12 E_a = E_a P_12.
```

Define a second exact family:

```text
K_low^P  = E_low,
K_high^P = P_12 E_high.
```

It has the same effects and normalization:

```text
(K_a^P)^sharp K_a^P = E_a,
sum_a (K_a^P)^sharp K_a^P = I_4.
```

It also has the same Born weights as the Luders family. Its high event map is
different. On the state generated by `e_1`, the two high-event amplitudes are

```text
E_high e_1       = (3,-1,-1,-1)^T/4,
P_12 E_high e_1  = (-1,3,-1,-1)^T/4.
```

They are not proportional, so their normalized rank-one post-event states
are unequal. Therefore equality of effects and probabilities does not imply
equality of instruments.

Proposal-local names:

```text
CAND-QDD-INSTRUMENT-P12-TWIST
CAND-QDD-K-P12-LOW
CAND-QDD-K-P12-HIGH
CAND-QDD-WITNESS-SAME-EFFECT-DIFFERENT-INSTRUMENT.
```

This is a definition-level counterexample to an effect-only quotient. It is
not a classification of the complete physical apparatus universe.

## 6. Three equalities, frozen separately

Freeze:

```text
Eq_K_matrix:
    input equality of every labeled rational K_a matrix.

Eq_instrument:
    (K_low,K_high) ~ (K'_low,K'_high)
    iff K_a rho K_a^sharp = K'_a rho (K'_a)^sharp
    for every rho in State_G(Q) and each fixed label a.

Eq_effect:
    input equality of every labeled E_a matrix.
```

Thus `K_a` and `-K_a` can define the same event operation, while the Luders
and `P_12` families have the same `Eq_effect` class but distinct
`Eq_instrument` classes.

The future physical classification must use `Eq_instrument`. `Eq_effect`
may audit the registered shadows; it may not erase a post-event distinction.

Proposal-local names:

```text
CAND-QDD-EQ-K-MATRIX
CAND-QDD-EQ-INSTRUMENT-OPERATIONAL
CAND-QDD-EQ-EFFECT-MATRIX.
```

## 7. Coarse-graining is an operation, not an effect sum

For an outcome-indexed instrument, forgetting the label is frozen as

```text
Delta_K(rho) = I_low(rho) + I_high(rho).
```

For the Luders family:

```text
Delta_L(rho)
  = E_low rho E_low + E_high rho E_high.
```

This generally differs from `rho`. It is not replaced by applying a fresh
Luders rule to the merged effect

```text
E_low + E_high = I_4,
```

which would give the identity event map. Equal coarse effects do not determine
equal coarse post-event operations.

Proposal-local name:

```text
CAND-QDD-COARSE-FORGET-OUTCOME.
```

The `CAND-COARSE-IDENTITY-N0` identifier in the Route A package concerns the
anchored input record. It is not this outcome coarse-graining rule.

## 8. Relation to the five adopted fields

For a nonzero Route A amplitude `v`, define

```text
m(v)  = v^T G v,
rho_v = v v^T G / m(v).
```

Then

```text
p_a(rho_v) = w_a(v)/m(v).
```

The existing `D_scoped` record writes only:

```text
support_state             ZERO or NONZERO
total_weight              m
branch_weights            (w_low,w_high)
density_state             the pre-event rho_v
normalized_weight_state   (p_low,p_high).
```

It does not write a sampled outcome, a detector pointer, or a conditional
post-event state. `Post_a` remains a separate tagged mathematical operation.
The ZERO constructor remains `ZERO_DENOMINATOR`; no instrument is applied to
it.

Sampling a realized outcome, writing a history entry, or feeding a result
back into `U` would require a new typed input and a separately registered
bridge. Nothing here changes

```text
feeds_U = FALSE.
```

## 9. Physical-selection boundary

The following remain `UNRESOLVED`:

```text
apparatus carrier and equality
apparatus ready state
kernel-to-apparatus coupling
pointer carrier and physical outcome IDs
exact reduction from the coupling to K_a
physical admissibility predicate on Instr_alg
proof that the physical universe is complete
physical instrument and effect IDs
physical Born-pairing ID
source and target layers
public gate
feedback or history-update semantics.
```

An independent nondemolition condition could select the Luders family by
requiring identity action within each eigensector. Such a condition is not
adopted here. It would be a new physical selection principle and must be
frozen before classification.

## 10. Frozen output semantics

```text
PREDEFINITION-CONSISTENT
    The named candidate satisfies its algebraic effect, completeness, Born,
    and tagged-update definitions. This is not physical PASS.

PASS
    A complete independently frozen apparatus/kernel universe has exactly
    one Eq_instrument class.

    The mandatory companion field candidate_relation reports exactly one of:
      LUDERS-MATCH
          The unique class agrees with the named candidate.
      LUDERS-MISMATCH
          The unique class does not agree with the named candidate. This
          refutes that candidate without refuting instrument existence or
          uniqueness.

NONUNIQUE(k)
    A complete frozen physical universe has exactly k surviving
    Eq_instrument classes, where k is a finite or infinite cardinal with
    k >= 2. For finite k, report its exact integer value. Equal effects do
    not merge the classes.

EMPTY
    The complete frozen physical universe has no surviving instrument.

STOP
    A carrier or state domain, apparatus, coupling, pointer, reduction,
    physical admissibility predicate, exact K/effect list or certificate,
    equivalence, K/E boundary, outcome or post-event semantic, Born pairing,
    normalization or completeness rule, MatterData outcome mapping,
    coarse-graining rule, public ID, layer, gate, output meaning, or proof of
    classification completeness is missing.

FIRE-POSTHOC
    After classification opens, any carrier or state domain, apparatus,
    coupling, pointer, reduction, physical admissibility predicate, exact
    K/effect list or certificate, equivalence, K/E boundary, outcome or
    post-event semantic, Born pairing, normalization or completeness rule,
    MatterData outcome mapping, coarse-graining rule, public ID, layer, gate,
    output meaning, or classification-completeness proof or method changes.
```

The Luders and `P_12` families prove that an effect-only uniqueness rule is
invalid. They do not decide which families survive a future physical
apparatus predicate. The current output is therefore `STOP`, not
`NONUNIQUE(k)`, `EMPTY`, or Canon `F`.

## 11. Exact status consequence

```text
rational G-state carrier                 DEFINED, proposal-local
complete algebraic K-factor universe     DEFINED, proposal-local
Luders family                            DEFINED, pre-result candidate
same-effect post-state control           DEFINED
K/effect/instrument equalities            DEFINED, proposal-local
tagged zero-probability semantics         DEFINED, proposal-local
outcome-forgetting operation              DEFINED, proposal-local

apparatus selection                       UNRESOLVED
physical universe and completeness        UNRESOLVED
physical public IDs and Born pairing      UNRESOLVED
layers and public gate                    UNRESOLVED
A11                                       PARTIAL / O-STOP
QDD-PHYSICAL-EFFECT-SELECTION             O / STOP
QUADRATIC-DECODER-DATA                    O / STOP, unchanged.
```

The public QDD row excludes post-state instrument uniqueness. This note does
not expand that scope. It only prevents an algebraic effect pair from being
mistaken for a selected physical instrument.

No formal scientific run is authorized by this predefinition.
