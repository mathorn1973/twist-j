# PROMO-READING-FAMILY-V71

**Status:** NON-CANONICAL promotion package. No authority. No scientific status change.

**Date:** 2026-08-29

**Owner:** A. M. Thorn

**Public issue:** #656

## Authority at freeze

```text
STATE:          ACTIVE
CANON:          Public Canon v70
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v70
CONTENT_COMMIT: 7c31d41cc9bae52431d94b34fb90ab7bb30d3a9b
CANON_SHA256:   8fee689b8a4c56026767b99fec3520e5f08378f682c3ff49628def30bdf06599
CANON_BYTES:    368445
BASE_MAIN:      6214dd80b60da3fa71bcc7fbfbc6dc8ed6def475
```

`POLICY.md` on this base already contains the binding `Reading-family discipline` merged by PR #655. This package proposes the corresponding normative Canon wording only. It creates no theorem, dictionary, computation, hypothesis, obligation, falsifier, dependency, gate, evidence credit, reproduction, or status promotion.

## Purpose

Freeze one correction of program scope:

1. `J = 1 + zeta_5^2` remains the primitive physical axiom. It is asserted, not an internal derivation or selection target.
2. One primitive axiom does not imply one globally unique physical reading.
3. TWIST-J may admit a typed family of physical readings of the same autonomous integer substrate.
4. Reading-family completeness means classification of every output-relevant admitted alternative, not cardinality one.
5. Local uniqueness and nonuniqueness claims remain exactly scoped and are neither weakened nor promoted by this wording.
6. A post-hoc choice of reading after inspecting the target result remains forbidden by policy.

## Frozen Canon insertion

Insert after the top-level `Reading.` paragraph and before `Conventions.` in `canon/CANON.md`:

```text
Reading plurality. A single axiom does not imply a single physical reading.
TWIST-J may admit a family R = {D_alpha}_{alpha in A} of typed partial readings
of the same autonomous integer substrate. More than one reading is admissible
when the domain, codomain, physical context, equality or equivalence relation,
and overlap rule needed by the claim are declared publicly.

Distinct readings may be equivalent, complementary, or context-scoped. Their
multiplicity is not by itself a failure of the program. What is not admissible
is an untyped or outcome-dependent choice among incompatible readings. If two
readings apply to the same declared physical context and give inequivalent
physical outputs, the Canon must either provide an independent rule relating,
selecting, or assigning occurrence among them, prove the readings physically
equivalent at the claimed scope, or leave the corresponding physical claim
open.

A uniqueness theorem is therefore a scoped result only where a registered
claim explicitly asks for uniqueness. Global decoder uniqueness is not a
requirement of TWIST-J.

Decoder completion means that the admitted reading family is explicitly typed
and sufficiently classified to determine every physical output claimed by the
Canon, including every overlap or branch that can change such an output. It
does not require that the family contain exactly one reading.
```

The insertion is normative framework wording, not a registered scientific claim and carries no bracketed scientific status label.

## Frozen CORE replacement

Replace the current paragraph beginning

```text
Here K is the set of forward U-orbits. Decoder outputs never feed
```

through the sentence ending

```text
not a completeness theorem.
```

with:

```text
Here K is the set of forward U-orbits. Decoder outputs never feed
the state update. The public theory may contain more than one admissible typed
reading of the same substrate. Totality, classification of the admissible
reading family, compatibility on overlaps, and physical completeness remain
open. Global uniqueness is not a program requirement. Individual registered
claims may still ask whether a particular operator, selector, reading leg, or
restricted class is unique at its frozen scope. The public reading split is a
dictionary at its registered legs (READING-SPLIT [D]), not a completeness
theorem.
```

## Local claims explicitly preserved

The later fold must not change the scope, status, evidence or falsifier of at least these rows:

```text
MINIMAL-READ-DERIVATION [O]
CURVATURE-OPERATOR-CANONICAL [O]
QDD-INSTRUMENT-NONSELECTION [T]
QDD-INSTRUMENT-APPARATUS [O]
READING-SPLIT [D]
```

The principle is exact: local uniqueness remains a legitimate theorem or obligation where the class and equality are frozen. Local nonuniqueness remains a legitimate theorem where proved. Neither is automatically promoted to a global statement about the whole physical decoder.

## Registry and Frontier expectation

Expected later v71 content fold:

```text
canon/CANON.md       wording only
canon/CORE.md        wording only
canon/CHANGELOG.md   v71 entry, no scientific delta
canon/SHA256SUMS     regenerated
```

Expected byte-identical files:

```text
canon/REGISTRY.tsv
canon/FRONTIER.md
```

If review finds that a registered row itself contradicts the reading-family discipline, STOP. Do not silently reinterpret it in this package.

## Frozen changelog ceiling

A later v71 changelog entry may state only:

```text
Public Canon v71 is a framework-wording fold. It records no new scientific
claim and changes no status. It makes explicit that the primitive axiom is an
asserted starting point rather than an internal derivation target, and that
global decoder uniqueness is not a program requirement. A complete physical
reading may be a classified typed family; output-relevant alternatives,
overlaps, equivalences and any selection or occurrence rule must be explicit.
Scoped uniqueness and nonuniqueness claims remain unchanged.
```

No stronger wording is authorized by this package.

## Stop conditions

STOP on any of the following:

- Public authority moves before the later content branch is created and the delta is not re-gated.
- `canon/REGISTRY.tsv` or `canon/FRONTIER.md` must move for reasons not explicitly reviewed.
- A local uniqueness or nonuniqueness claim is weakened, strengthened or retired by wording alone.
- The fold is described as deriving, selecting or justifying A0.
- The fold is described as making every reading equally admissible.
- A reading may be chosen after inspection of the target measurement or result.
- Any scientific status, evidence credit, gate or dependency is added.

Promotion occurs only through the normal reviewed Public Canon release procedure. This note is not that promotion.