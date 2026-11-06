# Typed claim language for the ledger: a TIL proposal (NON-CANONICAL)

```text
STATUS:                    ANALYSIS / TOOLING PROPOSAL
AUTHORITY:                 NOT CANON
PUBLIC CANON:              Public Canon v107 / canon-v107
PUBLIC CONTENT COMMIT:     f5615ed4dcdfc672dc2e468399284a1dc03ce805
PUBLIC CANON SHA-256:      40d78dc4f5108acd8dbee642471a2b8c0eed5403cedaaa62ce8d890ee4d182dc
SCOPE:                     the public ledger schema at v107: REGISTRY, NORMATIVE,
                           DEPENDENCIES, GATES, EVIDENCE, HISTORY
METHOD:                    reading of the ledger rules against Transparent
                           Intensional Logic (Tichy); no computation on claims
FORMAL RUN:                NONE
PROBE / PREREGISTRATION:   NONE
CANON/TABLE/STATUS CHANGE: NONE
```

PUBLIC / NON-CANONICAL. Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.

## 0. What this note is and is not

This note proposes a non-normative typed representation of ledger rows,
to live under `tools/` as a checker, with Transparent Intensional Logic
(TIL, Tichy 1988; Duzi, Jespersen, Materna 2010) as its type discipline.
It changes no claim, status, scope, gate, dependency or evidence. It does
not derive, justify or explain the axiom. It proves no theorem: the
preregistered `verify.py` of each probe remains the only verifier, and
the typed representation is never evidence.

The claim is modest: four rules that POLICY.md and AGENTS.md enforce by
text and by review are the defining features of TIL, and a checker built
on TIL types would enforce them as typing errors instead.

## 1. Why TIL fits the ledger as it already stands

1. Status attaches to a procedure, not to a truth value. Two rows with
   the same mathematical content but different scopes are two claims, and
   `No summary may exceed the status or scope of its source` is a rule
   about scopes. In TIL a scope is a construction, an object of type `*n`;
   a status is a relation to the construction itself, written
   `[Status ^0C ^0T]`, never to what it constructs. This is what the
   literature calls hyperintensionality, and it is the reason a ledger of
   procedures cannot be modelled by truth-functional logic.
2. The axiom is never derived. In TIL the trivialization `^0J` is a
   construction whose constituent is mentioned and never executed. A rule
   whose conclusion is `^0J` is not forbidden; it is ill-typed, because
   nothing of type `*n` is produced by executing anything.
3. Every lift between L1 state, L2 manifold, L3 boundary, L4 support, L5
   stream and L6 measure needs a named gate. In TIL the six layers are
   types, a gate is a declared function constant of type `(L_to L_from)`,
   and application of an `L1` object where `L2` is expected does not
   typecheck. There is no implicit coercion to fall back on.
4. Dependencies are declared, never inferred from thematic proximity. In
   TIL a dependency of row A on row B is the occurrence of B's construction
   as a subconstruction of A's. "Has something in common" has no subtree,
   so it cannot be written.

Two further correspondences carry the status vocabulary:

- STOP-DEFINITION and STOP-PREDEFINITION are TIL's improper constructions:
  procedures with an undefined constituent, which construct nothing. A
  checker returns "undefined, because X is not declared", not an error.
- The ledger separates analytic from empirical content. THEOREM,
  COMPUTATION and DICTIONARY rows are closed constructions with no world
  or time parameter. `ANCHOR-ELECTRON-MASS` is the one empirical primitive,
  an intension whose value at the actual world is measured. A row that
  contains the anchor, or any `lambda w lambda t` prefix, must be the
  anchor itself or an H/O obligation, never T. Physical readings are
  DICTIONARY items: typed maps from architecture objects into physical
  vocabulary, and whether a reading agrees with nature stays an open
  obligation, which is the position the Canon already takes.

## 2. Mapping table

```text
ledger object                     TIL object                               checkable property
----------------------------------------------------------------------------------------------------
claim_id                          ^0ID, trivialized name                   unique, stable
scope (controlled English)        construction C of type *1                parses, typechecks at its layer
status T D C H O F                [Status ^0C ^0s]: attitude to C          transition needs evidence hash
item_type THEOREM/COMPUTATION     closed construction, no (w,t)            no empirical constant inside
item_type DICTIONARY              function constant (Physical Arch)        both ends typed
AXIOM-J                           ^0J, never executed                      no rule concludes it
layer L1..L6                      base types; MULTI, NOT_APPLICABLE        explicit "unassigned" type,
                                  are a typed unassigned value             never an error
gate (DICTIONARY_LIFT, OPEN_LIFT, declared constant of type (L_to L_from) owner lands at to_layer;
 DEFINITION_PROJECTION, ...)                                               every cross-layer application
                                                                           names a gate
OPEN_DECISION                     same-layer construction with an open     equal endpoints, open owner
                                  obligation as constituent
DEPENDENCIES REQUIRES             subconstruction occurrence               declared set == occurrence set
decision condition in FRONTIER    construction with obligations as free    evaluated at (w,t) = (tag,
 ("closes positively when ...")   constituents                             version); improper => STOP
probe PREREG + verify.py          execution ^1C in the world named by       value becomes evidence,
 + RESULT                         the evidence hash                        status follows the value
ANCHOR-ELECTRON-MASS              the only primitive intension             only empirical primitive
HISTORY event                     a (w,t) transition of the attitude       roundup is a projection
```

## 3. Three levels of formalization

Level 0, the row header. `claim_id`, `item_type`, `layer`, `gate_ids`,
`status`, evidence identity and declared dependencies become one
construction per row; the scope text stays a typed atom. This level is
generated mechanically from the six tables and already supports the
checks in section 4. It covers all 598 rows of v107 (454 T, 59 D, 39 C,
2 H, 25 O, 19 F) without reading any mathematics.

Level 1, the scope skeleton. Quantifier structure and named objects of a
scope ("for every d >= 1 and A in GL_d(Z) with no root-of-unity
eigenvalue, the Haar Koopman operator ... admits no v ...") become
constructions, with matrices, lattices and operators as typed atoms.
This level needs a translator from controlled English. A large language
model can propose it; only translations that typecheck and that
round-trip to the same construction are accepted, and the translator's
output is never normative. The 27 live H/O rows are the natural first
target, because their decision conditions are what the frontier runs on.

Level 2, full content, for selected programs where the physical reading
is densest (the photon lane, the coaxial step and the Lorentz seam). This
level is research, not tooling, and is out of scope for this note.

## 4. Checks that become mechanical at level 0

- Gate typing: every cross-layer application in a construction names a
  gate whose endpoints match; `tools/check_gate_contract.py` already does
  this on rows, the typed form does it on the construction itself.
- Dependencies versus occurrences: the declared REQUIRES set of a row
  compared with the set of claim identifiers occurring in its
  construction. Both directions of difference are findings for an issue,
  never automatic edits.
- Empirical containment: no THEOREM or COMPUTATION row contains
  `ANCHOR-ELECTRON-MASS` or a world parameter.
- Status transitions as rules with evidence as argument: T requires a
  pinned two-architecture evidence identity; a one-architecture finite
  result is at most C unless an independent theorem-grade proof is named,
  as POLICY.md states. The 9 one-architecture evidence rows of v107 are
  the first rows such a rule would read.
- Frontier decisions: each decision condition is evaluated against the
  current tables; a condition whose constituent obligation is still open
  evaluates to improper, which is STOP by construction, with the missing
  constituent named.

## 5. Worked examples at level 0

Example A, a dictionary lift. `GATE-L5-L6-BORN-READING` owned by
`MEASURE-BORN-VERB` (`DICTIONARY_LIFT`, L5 to L6) becomes a constant

```text
GATE-L5-L6-BORN-READING : (L6 L5)
MEASURE-BORN-VERB        = [^0GATE-L5-L6-BORN-READING ^0<the L5 verb object>] : L6
```

The owner's layer equals `to_layer`, which is the existing gate contract
restated as a type.

Example B, an open lift. `GENERATIONS-L3` [O] with
`GATE-L2-L3-GENERATIONS` (`OPEN_LIFT`, L2 to L3) has the decision
condition "closes negatively if the derived count differs from three".
At level 0 the condition is `[= [^0GATE-L2-L3-GENERATIONS ^0<L2 object>] ^03]`
with the gate constant declared but not yet defined. Evaluated at v107
the construction is improper, which is exactly the row's O status; it
becomes evaluable only when a lift is supplied.

Example C, a declared dependency. `J-LI-TORAL-HAAR-NOGO` [T] REQUIRES
`J-STEP` with basis "the named dimension-four specialization uses the
public multiplication-by-J matrix M_J". At level 0 the dependency is the
occurrence of `^0J-STEP` in the row's construction; the dependency check
compares that occurrence with the DEPENDENCIES row and reports agreement.

Example D, the anchor. `ANCHOR-ELECTRON-MASS` is the only constant of
intensional type. A proposed T row whose construction contains it fails
the empirical containment check before any reviewer reads it.

## 6. Procedure, with no Canon change

1. Build the level-0 generator and checker under `tools/`, reading the six
   tables and writing a report. The report lists differences only; it
   edits nothing and asserts nothing about physics.
2. Run it against v107 and open one issue per class of finding.
3. Add the checker to pull-request checks for changed registry rows, so an
   agent's proposed row must typecheck before human review. This follows
   the "proposer and verifier" pattern: a model may propose, the checker
   decides.
4. Level 1 for the live H/O rows, under the translator discipline above.
5. Generate the weekly roundup and the website canon pages from HISTORY
   events through the same typed form, so neither can exceed the status
   or scope of its source.

## 7. Risks and stop conditions

- MULTI and NOT_APPLICABLE must be a typed "unassigned" value. Turning
  them into errors would harden what the Canon keeps deliberately open.
- The typed representation is tooling. It is never cited as evidence,
  never changes a status, and never edits `canon/`; findings go to issues
  and follow the procedures in AGENTS.md.
- A translator's output is data, not a claim; the Canon text remains the
  only normative source.
- Stop if a level-0 construction cannot be produced for a row without
  interpretation: that row's header is then the finding, and it is
  reported rather than guessed.

A standalone prototype of the construction language, the type checker,
the verifier and the typed decoder exists outside this repository, on an
unrelated toy domain; nothing in this note depends on it, and nothing from
it is imported here.
