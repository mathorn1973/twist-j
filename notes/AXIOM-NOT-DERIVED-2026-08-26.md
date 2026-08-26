# NOTE: the axiom is not derived. What may be asked about five, and what may not

```text
status   NON-CANONICAL. Process note. Moves nothing, proposes one contract line.
revision 2. Owner public review of 2026-08-26 applied: two factual errors in
         the verified section corrected (7.1, 7.3) and the owner's refined
         formulation recorded (section 8). Sections 1-6 reproduce the original
         ruling unaltered.
date     2026-08-26
origin   owner ruling, in his words: it makes no sense at all to look for why
         five should be forced, if we build J as an axiom. An axiom is an
         axiom. We do not prove it. We prove what it brings and what it can do,
         or what we can do with it.
```

## 1. The ruling, restated as a rule

```text
No result, note, essay or Canon row may present a property of five, of the
exponent two in 1 + zeta_5^2, of the orientation, or of the carrier as a
reason to hold the axiom. The axiom is posited. Its account is kept in
consequences only.
```

The public fold discipline already enforces exactly this at the fold boundary.
`FOLD-RECORD-CANON-v65_2026-08-25.md`, section "What this fold did not claim",
lists "no selector of an exponent, orientation, prime or carrier". The rule
above is that sentence lifted from the fold to the contract, where it can also
govern notes, candidates and prose, which the fold gate never sees.

## 2. Three activities that the phrase "why five" runs together

Only the first is forbidden.

```text
DERIVATION      Deducing the axiom from something outside it. Forbidden and
                also impossible: there is nothing outside it to deduce from.
                Any argument of this shape is [F] on sight.

CHARACTERISATION  A true theorem about a class that happens to contain the
                axiom. Example, already carried: among quartic cyclotomic
                fields exactly Q(zeta_5) has cyclic Galois group, and only
                then is 125 the minimal discriminant. Legitimate as [T] in a
                stated narrow class. NOT evidence for the axiom, ever.

ATTRIBUTION     Asking which consequences survive replacing 5 by another odd
                prime. This is not about the axiom at all. It is bookkeeping:
                it decides whether a result is credited to J or to cyclotomy.
                Mandatory, not optional.
```

## 3. Why attribution is mandatory, and why it is not derivation

An axiom that cannot be varied cannot be falsified. If a result reads the same
in `Q(zeta_7)`, the axiom did no work in producing it, and a Canon row that
credits J with it overstates by exactly the amount of that generic content. The
variation is the falsifiability instrument, not a proof attempt.

The sweep run on 2026-08-26 shows the size of the exposure. Of the statements
about J examined there, these are generic at every odd p and therefore cost the
axiom nothing:

```text
N(1 + zeta_p^2) = 1                 Tr = p - 2 and disc = +- p^(p-2)
p-th power annihilates the phase    [K : K+] = 2, so x xbar is the modulus^2
unit torsion Z/2p                   |J|^2 has degree (p-1)/2
```

Only `(p-1)/2 = 2`, which puts the modulus in a quadratic field and makes it
`phi`, fails to survive the substitution. That is content of the axiom. It is
still not a reason to hold the axiom.

## 4. Where the program already does this, and where it does not

```text
DOES     AUDIT-BINARNI-UZEL-A-ZETA_2026-08-22_CZ carries
         [F] "the exponent 2 in the axiom IS the Frobenius step" as a
         selection claim, and [T] that the four elements 1 + zeta^a form one
         Galois orbit, so no Galois-invariant condition can select the
         exponent. The guard exists and has fired.
DOES     PROMO-J-BINARY-NORM-INDEX-1_2026-08-22 states the split explicitly:
         "the mechanism is generic and holds in every degree; only the
         attainment is a fact about J", and warns that without both controls
         the T row "will read as a selection it does not make".
DOES     FOLD-RECORD-CANON-v65, quoted above.

DOES NOT DVE-MINIMALITY-A-SEV_2026-08-22_CZ is framed end to end as a
         minimality argument for five: rank one, then cyclic C_4, then minimal
         discriminant 125. Every individual row in it is careful and one row
         even says rank one alone does not select five. What the document
         never says is the sentence this note is about: none of it is evidence
         for the axiom. Read quickly, the section reads as a derivation.
DOES NOT This session, revision 1 of NOTE-EXPONENTS-2-3-5_2026-08-26, whose
         section 4 was titled "what actually selects five". Corrected to
         revision 2 the same day. Recorded here rather than quietly fixed.
```

## 5. Proposed contract line, one sentence

```text
Every claim naming J states whether it survives replacing 5 by another odd
prime. Surviving means imported cyclotomy and is labeled as such; not
surviving means content of the axiom. Neither is evidence for the axiom.
```

Falsifier for the gate itself: a claim that fails the p-substitution and is
nevertheless generic under a different substitution, for instance across
quartic CM fields. That would show the odd-prime sweep is the wrong control and
the gate would need a second axis.

## 6. Owner decisions this surfaces

```text
1  DVE-MINIMALITY-A-SEV: add the missing sentence, or re-title the section as
   characterisation. The rows themselves need no change.
2  The live [H] in that document, "a marked archimedean place plus complex
   conjugation determine the exponent, closing the first seam with no new
   input", is a selection hypothesis by shape. Under the rule its value is
   economy of the ansatz, fewer free choices in the axiom, not proof. If it is
   kept, it should be stated that way. If economy is not a goal the program
   claims, it should be retired.
3  Whether the p-substitution note becomes a required field in the registry
   schema, or stays a review habit. The schema is currently
   claim_id status scope canon_section evidence falsifier and adding a field
   is a sealed integer-versioned fold.
```

---

## 7. State in this repository, verified 2026-08-26 (added on filing)

The sections above are the owner's ruling and are reproduced unaltered. This
section records only what was checked against `mathorn1973/twist-j` at Public
Canon v66, so that the cross-references above are not read as claims about this
repository's contents.

### 7.1 None of the five referenced documents is held here

*(Revision 2: the revision-1 heading said "four of the five" while the table
below marks all five absent; the count is corrected.)*

```text
FOLD-RECORD-CANON-v65_2026-08-25.md      NOT PRESENT. There is no claude/
                                         directory. notes/incubation-import-
                                         2026-08-21/SESSION-RECORDS/ carries
                                         FOLD-RECORD-canon-v55, -v56 and -v57
                                         only.
AUDIT-BINARNI-UZEL-A-ZETA_2026-08-22_CZ  NOT PRESENT
PROMO-J-BINARY-NORM-INDEX-1_2026-08-22   NOT PRESENT
DVE-MINIMALITY-A-SEV_2026-08-22_CZ       NOT PRESENT
NOTE-EXPONENTS-2-3-5_2026-08-26          NOT PRESENT
```

They belong to a working context outside this repository. Owner decisions 1 and
2 therefore cannot be actioned here; they name documents this repository does
not hold.

### 7.2 The attribution split the note credits is carried by the registered row

Although the promotion document is absent, `J-BINARY-NORM-INDEX [T]` is
registered here and its scope carries exactly the generic/attainment split the
note describes: the mechanism is stated "for every rational prime `p` inert in
`K=Q(zeta_5)`" with "index exactly `p-1`", and only then "a norm-one algebraic
unit can generate the whole inert residue multiplicative group only at `p=2`,
and `ord(Jbar)=15=|F_16^x|` so J attains that sole possible whole-group" value.
Mechanism generic, attainment specific, both visible in the row.

### 7.3 A fourth instance of the flagged pattern, in the Canon itself

`canon/CANON.md:3339` reads:

```text
The two L1 results now supply two independent answers to "why five":

    ramification answer: among full quartic cyclotomic fields, the complete
                         total-ramification locus is {(K_5,5),(K_8,2)};
    minimum answer:      in the abelian Galois CM unique-even-bit class A,
                         K_5 is the unique absolute-discriminant minimizer.
```

Substantively this section already complies with the rule. It continues: "The
answers use different frozen classes and are not a physical selection chain.
Total ramification is not a premise of the minimum theorem; the class `A` and
discriminant minimization are not claimed to be forced by `J`, the decoder, or
Nature." The v33 fold paragraph at `canon/CANON.md:7678` repeats the guard.

What neither passage carries is the sentence this note is about: that none of it
is evidence for the axiom. In the taxonomy of section 2 both results are
CHARACTERISATION, and the heading calls them "answers to 'why five'", which is
the phrasing the note says reads as a derivation on a quick read. This is the
same defect the note records against `DVE-MINIMALITY-A-SEV`, one layer up, in
normative text rather than in a note.

*(Revision 2 correction.)* Revision 1 claimed `canon/CORE.md` does not carry
the phrase; that was wrong — a case-sensitive search missed the heading.
`canon/CORE.md` line 58 is titled `## Why five, twice`, so the flagged framing
sits in the short orientation document as well, where a quick reader is most
exposed. The finding is therefore *stronger* than revision 1 stated: both
normative documents carry the "why five" framing, and neither carries the
ruling's sentence that none of it is evidence for the axiom.

Recording this is not a proposal to edit the Canon. Under the contract line of
section 5 the fix is a label, not a row change, and any wording change to
`canon/CANON.md` is a sealed fold.

### 7.4 Cost of owner decision 3

The registry header is `claim_id status scope canon_section evidence falsifier`,
confirmed in `canon/REGISTRY.tsv`. The column tuple is duplicated as
`REGISTRY_FIELDS` in `tools/check_ledger_core.py` and
`tools/generate_canon_views.py`, and is read by `tools/check_canon.py`,
`tools/architecture_map_report.py`, `tools/build_genesis_ledger.py` and two test
modules. Adding a field is a sealed fold that also changes tooling and every
one of the 327 registry rows. The cheaper form of the same control is a required
sentence inside the existing `scope` column, which needs no schema change and no
tooling change.

### 7.5 What this note does not do

It creates no claim, definition, probe, evidence row, gate or dependency. It
proposes one contract line and records four repository facts. It does not amend
`POLICY.md`, `AGENTS.md` or any `canon/` file, and the contract line of section
5 is not in force until a sealed fold puts it there.

---

## 8. Owner review refinement (revision 2, 2026-08-26)

On public review the owner kept the core of the rule and refined its
formulation. The refined contract line, recorded verbatim:

```text
TWIST-J posits J = 1 + zeta_5^2 as a primitive axiom. No theorem internal to
TWIST-J is presented as deriving or justifying it. Where a well-typed
comparison family exists, uniform and p = 5-specific content are
distinguished for attribution only.
```

One substantive correction to the reproduced ruling: impermissible framing is
**not automatically scientific `[F]`**. The axiom of one theory can be a
theorem of a stronger theory; within TWIST-J it is simply primitive. The
sentence "Any argument of this shape is [F] on sight" in section 2 stands as
the owner's original wording and is superseded by this refinement: a
derivation-shaped argument is a process violation to be corrected or
re-titled, not a registered scientific falsification.

Like the section-5 line it refines, this formulation is not in force until a
sealed fold adopts it.
