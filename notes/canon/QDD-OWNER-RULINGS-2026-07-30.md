# QDD-OWNER-RULINGS-2026-07-30

```text
STATUS:                  NON-CANONICAL OWNER DISPOSITION
AUTHORITY:               NOT CANON
OWNER DECISION DATE:     2026-07-30
CLAIM ISSUE:             107
RULES ON:                notes/canon/P-DMATTER-TOTAL-1-PUBLIC-BINDING-PACKAGE-V27.md
AUDIT INPUT:             notes/canon/AUDIT-QDD-BINDING-PACKAGE-V27.md
PUBLIC BASE:             Public Canon v27, tag canon-v27
PUBLIC CONTENT COMMIT:   116b62edf505914d96fcd65318d97f3675c53f85
PUBLIC CANON SHA-256:    c7c4c7e6d5a3116e356b060eaf696963285b0f2f465d5f2e1dcda5c094a309f6
PUBLIC CANON BYTES:      150959
FORMAL RUN:              NONE
PROBE / PREREGISTRATION: NONE
CANON / TABLE CHANGE:    NONE
QDD STATUS:              O / STOP, unchanged
V28:                     HOLD, no fold manifest approved
```

This note changes no claim, status, scope, gate, frontier, count, hash, tag,
release, or authority. It creates no public identifier and authorizes no
execution. It records two owner rulings that the audit could not supply,
because neither is a computation, and it fixes the shape of the work that may
follow.

## Ruling 1. `statement_source`

**Every normative QDD identifier must carry
`statement_source = canon/CANON.md`. There is no third option.**

A file under `notes/canon/` may be the source of a proposal, an audit trail,
an evidence record, or review input. It cannot be the statement source of a
normative item while it carries `AUTHORITY: NOT CANON`.

The binding package asserts three things at once:

```text
AUTHORITY: NOT CANON
twenty-three new prospective normative identifiers
CANON / TABLE CHANGE: NONE
```

Those three are incompatible. Either the new items are not normative, in which
case they do not come into existence, or they are stated in `canon/CANON.md`,
which changes the Canon, its SHA-256 and the public version. The audit named
this correctly and no fourth reading exists.

**Consequence.** The QDD definitions are not to be installed by a standalone
table patch. When they are ready they enter as part of the content commit of a
new Canon, with the version, the hash and the byte count moving accordingly.
`notes/canon/...` may be cited in evidence and in history; it may not appear
in a `statement_source` column.

This also disposes of the ledger route the package proposed. A delta that adds
`NORMATIVE` rows pointing at a non-Canon file would pass the current checkers
and still be wrong, so passing `tools/check_ledger.py` is necessary and not
sufficient here.

## Ruling 2. The effect prohibition stands

**The prohibition remains in force. A rename does not lift it.**

The matrices

```text
E_low  = (1/4) 1 1^T,
E_high = I_4 - E_low
```

may be used as algebraic projectors and as weight functionals. They may **not**
fill the public `quadratic_manifest.effect_ids` slot, and they may not be
presented as a physically selected complete family of effects, without a
separately pre-frozen apparatus selection principle.

`notes/canon/P-DMATTER-TOTAL-1-PHYSICAL-INSTRUMENT-PREDEFINITION.md` is
unambiguous on this point. Section 2 names the same two matrices
`CAND-EFFECT-GRAM-LOW` and `CAND-EFFECT-GRAM-HIGH`, holds them
`ALGEBRAIC_ONLY`, and states verbatim:

> Those two identifiers remain `ALGEBRAIC_ONLY`. They are explicitly forbidden
> from filling the public `quadratic_manifest.effect_ids` slot.

Section 3 of the same predefinition says what is still missing, and this
ruling adopts that list unchanged:

> A physical admissibility predicate must still be derived from a public
> apparatus carrier, ready state, coupling, pointer, and reduction to `K_a`.

and, of the labels `low` and `high`:

> They are not yet physical detector-click identifiers.

**This is not a prohibition on using their mathematics.** The predefinition
itself shows that the two projectors give exact weights, and the audit
confirmed by exhaustive enumeration that those weights populate the five-field
record without producing a realized outcome, a pointer, or a post-measurement
state. Nothing in this ruling touches that.

### Permitted

```text
DEF-QDD-PROJECTOR-LOW
DEF-QDD-PROJECTOR-HIGH
DEF-QDD-BRANCH-WEIGHT-PAIRING
```

each carrying, explicitly:

```text
ALGEBRAIC_READOUT
not a physical apparatus selection
not a realized outcome
not a post-state instrument
```

### Not permitted

```text
DEF-QDD-EFFECT-LOW
DEF-QDD-EFFECT-HIGH
quadratic_manifest.effect_ids = {...}
"complete physical two-outcome effect family"
```

absent a separate, pre-frozen apparatus selection principle.

The naming is not cosmetic. `projector` states what the object is; `effect`
imports a physical reading the apparatus has not earned. The audit found the
package using the second word while its own section 3 concedes:

> The adoption is a new dictionary input. It is not derived from the effect
> identities alone.

## What this means for QDD

The current package cannot be repaired cosmetically. It must be split into two
distinct obligations, which is what the two rulings force.

### QDD algebraic factorization — may proceed

May ask whether the exact five-field record factors through `Q_QDD`. Algebraic
projectors, exact weights, the density record and normalization all belong
here. The audit already established, by exhaustive exact enumeration and with
a reproducible checker, that the displayed composite is:

```text
total, and exactly normalized      w_low + w_high = m and p_low + p_high = 1,
                                   0 violations on all 15600 nonzero states
constant on every Q-fibre          0 of 313 fibres carry a non-constant record
injective on QCarrier              313 distinct records for 313 elements
allowlist-compliant                exactly independent of q and r
```

That is a genuine positive result and it survives both rulings untouched.

### Physical effect selection — stays `O / STOP`, separately

Must begin from an apparatus, a ready state, a coupling, a pointer, a
reduction, and the completeness of a physically admissible class. Effects may
not be chosen retroactively because they produce the desired record. The
predefinition already fixes the algebraic instrument universe
`Instr_alg(E_low, E_high)` as a total set definition and says plainly that it
"is not the complete physical instrument universe".

This split removes the contradiction the audit found: the package concedes in
one place that the effect family is a new dictionary input, and in another
calls it the complete scoped physical read and uses it to fill the forbidden
slot.

## The nearest correct step

**Not a fold, and not yet a probe.**

This disposition is the first step and records both rulings:

```text
statement_source:
    canon/CANON.md only for every normative QDD identifier

effect ruling:
    E_low and E_high remain algebraic projectors
    no rename lifts the physical-effect prohibition
    quadratic_manifest.effect_ids remains unresolved
```

The second step is a **new package written from scratch**, not a partial repair
of the old one. It must carry the ten corrections of the audit, in particular:

```text
1  the exact direct write, with displayed formulas rather than one prose
   sentence; sigma_4 defined; the pairing <x,y> = (1/5) Tr(x sigma_4(y))
   written with its 1/5
2  the LOW LINE named correctly, Q.(1 + zeta + zeta^2 + zeta^3) = Q.zeta^4,
   and the words "rational-line and trace-kernel" deleted, since they are
   false in the frozen basis B0 and cost 480 of 625 carriers
3  a gate whose decision condition can actually route negative
4  a layer field that makes the gate mechanically enforced, or no gate claim
5  a ledger delta that passes tools/check_ledger.py, with the PASS line
   recorded in the package
6  statement_source per ruling 1, and the version consequence stated rather
   than denied
7  the effect ruling above, cited
8  SCOPE_EXCLUDED split out of the leg binding
9  an open disclosure of the 313 collision: |QCarrier| = 313 with fibres 25
   and 50 has the identical profile to the excluded CENSUS-313 leg, while the
   two partitions share zero blocks and even their two size-25 blocks are
   disjoint, so the coincidence is numerical and there is no cross-leg
   identity
10 only then a probe, scoped for reproducibility rather than discovery
```

## Disposition

```text
QUADRATIC-DECODER-DATA          O / STOP, unchanged
physical effect selection       O / STOP, and now explicitly separate
QDD algebraic factorization     may proceed under ruling 2's naming
quadratic_manifest.effect_ids   UNRESOLVED
Public Canon v28                HOLD, no fold manifest approved
```

The mathematical QDD branch may continue. The physical selection of effects is
not pretended to be finished.
