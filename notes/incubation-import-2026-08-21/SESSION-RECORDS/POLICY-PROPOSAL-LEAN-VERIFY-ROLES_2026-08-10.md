# POLICY PROPOSAL: the roles of Lean and verify.py

Status: NON-CANONICAL PROPOSAL. No authority. Changes no registry row, no
frontier row, no canon line, and no file in the public repository.
Date: 2026-08-10. Target line on promotion: public, mathorn1973/twist-j.
Origin: owner direction after claude/RECON-ZETA23-VERIFICATION-STANDARD_2026-08-10.md.

Owner decisions already taken, recorded here so a later fold does not reopen them:

```
scope        forward only, plus one jednorazovy audit of existing T rows.
             No row is demoted by this proposal.
target       internal note first. No public fold until the owner reads this.
exhaustion   exhaustive verification still earns T, but the completeness of the
             domain must be established, not assumed.
```

## Step 0 record

Performed 2026-08-10 against a full clone of mathorn1973/twist-j, not against a
rendered page and not against this project's snapshot.

```
STATE            ACTIVE
AUTHORITY        mathorn1973/twist-j main
CANON            Public Canon v41
TAG              canon-v41                        ancestor of main: OK
CONTENT_COMMIT   096e97b44727830102846746f0c723af1c59a2cf   ancestor of main: OK
CANON_SHA256     a15474c4204db637d7ce276ef6ea5dbe94b50af593e46389fd5e77aa16ca80e8
                 recomputed on canon/CANON.md: match
CANON_BYTES      198932                           recomputed: match
canon/SHA256SUMS 5 of 5 OK
clone HEAD       278b5348c7ace52737700f05f7ab230ffd201fc6
```

The gate passes. This proposal is written against the current head, not a snapshot.

## The problem this fixes

POLICY.md already carries the right instinct, in two lines of section 4:

```
- An independent proof may earn `T`; its verifier is then an audit.
- A one-architecture finite result is at most `C` unless its proof is
  independently theorem-grade.
```

and AGENTS.md line 377 repeats it. The instinct is correct and the definition is
missing. Nothing in the repository says what makes a proof independently
theorem-grade. It is a human judgment made once per row and never rechecked.

The consequence is visible in the registry. There are 227 claims, 125 of them
at T. The evidence field of those 125 T rows resolves to:

```
reproduce/   76
probes/      41
inline        8
```

Every one of them is a Python computation or a prose derivation. That is fine
for what it is. It is not what the word theorem-grade is doing in POLICY.md.

The second problem is that verify.py mixes two jobs. It states the claim and it
computes the claim, in one file. A reader who wants to know what was asserted
must read the same script that does the work. There is no short surface a
stranger can read in five minutes and then decide whether they care.

## The three roles

```
verify.py    the computation layer. Exact arithmetic, stdlib only, under 120 s,
             two architectures, byte-identical stdout against one committed
             EXPECTED.txt. Establishes finite-range fact. Fires falsifiers.
             Ceiling: C. Can produce F. Cannot produce T on its own.

Lean         the statement and theorem layer. Split into a trusted statement
             surface and an untrusted engine. Establishes theorem.
             Ceiling: T. Cannot produce C: it says nothing about a finite range
             that was not proved.

derivation   the reading layer. A self-contained exact derivation in the Canon
             that a competent reader checks by reading. Ceiling: T.
             Unchanged by this proposal, and it stays a legitimate route.
```

D is untouched. D is a dictionary claim, not a mathematical theorem, and neither
layer can earn it. D stays governed by derivation review.

## Rule 1, the trusted statement rule

A formal artifact separates what is claimed from how it is proved.

```
lean/NAME/Statement.lean   TRUSTED. Defines every object the claim mentions.
                           Imports Mathlib only. Imports nothing from the engine.
lean/NAME/Claim.lean       TRUSTED. The claims, each with proof `sorry`.
                           Imports Statement.lean only.
lean/NAME/Solution.lean    UNTRUSTED. Proves exactly the Claim statements by
                           delegation.
lean/NAME/<engine>/        UNTRUSTED. Nobody has to read it.
lean/NAME/AUDIT.md         toolchain pin, Mathlib commit, the verbatim
                           `#print axioms` lines, the comparator verdict,
                           and the line counts of the two trusted files.
```

Obligations:

1. No `sorry` anywhere except in `Claim.lean`, where every `sorry` is deliberate.
2. No `axiom` declaration anywhere in the artifact.
3. `#print axioms` on every claim prints exactly `propext`, `Classical.choice`,
   `Quot.sound`, and nothing else. In particular no `sorryAx`.
4. Every top-level claim takes no hypothesis. If the argument needs an analytic
   or arithmetic input, that input is a proved term inside the artifact, not a
   parameter of the claim.
5. The import discipline in the table above is mechanical and is the real
   content of this rule. The line counts are audit metadata, not a cap.

Rationale, stated once so it is not relitigated: the point is not that Lean is
fashionable. The point is that a reader who wants to know WHAT is claimed reads
two short files and trusts only Mathlib and the kernel, and a reader who wants
to know WHETHER it holds runs a tool. Neither reader has to trust us.

## Rule 2, exhaustion

Exhaustive verification over a finite domain is a proof and continues to earn T.
The weak point was never the enumeration. It is the claim that the domain is
complete.

New obligation: a T row justified by exhaustion states the completeness argument
explicitly, as a numbered step, and that step is a proof obligation like any
other. Where the completeness argument is nontrivial, it is exactly what belongs
in a formal artifact.

An enumeration whose domain is a chosen finite range rather than a complete
domain was never exhaustive. It is C.

## Rule 3, method ceiling

A live H or O row states the ceiling of its current route where one is known:
the bound the route cannot pass, and what new input would be needed to pass it.
Where no ceiling is known, the row records that no ceiling is known. The field is
never left blank.

This is falsification-first applied one level up. A falsifier says how the claim
could die. A ceiling says how far the method could ever go if it lives.

## Scope, and the audit

Forward only. No existing row changes status because of this proposal.

One audit, once, over all 125 T rows. Each row lands in exactly one bucket:

```
T-derived      evidence is a self-contained exact derivation a reader checks by
               reading. Survives unchanged.
T-exhaustive   evidence is an enumeration over a domain asserted to be complete.
               Survives if the completeness argument is present and explicit.
               Otherwise it is flagged and gets an O row for the argument.
T-computed     evidence is a finite-range computation that is not exhaustive over
               the claim's own domain. Under the definition above these were
               never theorem-grade. Flagged, and gets an O row.
```

The audit changes no label. It produces one table and one O row per flagged
claim. That is the whole point of choosing forward-only with an audit rather
than retroactive re-grading: nothing is demoted in the dark, and nothing is
quietly left ambiguous either.

Expected outcome, stated in advance so the audit cannot be graded on its result:
some fraction of the 125 will be flagged. If the flagged count is zero, the
audit's classification was too loose and the audit itself is suspect.

## The gate problem, stated plainly

The two-architecture byte-identity gate does not transfer to Lean, and pretending
it does would be dishonest. A Mathlib build is hours of CPU and several GB. The
public workflow has a 15-minute architecture limit and a 120-second verifier
budget. A Lean artifact cannot run under the existing required check.

So the Lean gate is a different gate, and must be written as one:

```
pinned lean-toolchain and pinned Mathlib commit, both recorded in AUDIT.md
the verbatim #print axioms lines, recorded
a comparator run (statement equality, axiom audit, external kernel replay),
    verdict recorded, run by the author on two machines
CI checks the recorded form, not the build: pins present, axiom lines exactly
    the three standard axioms, import discipline of the two trusted files,
    no sorry outside Claim.lean, no axiom declaration
```

Any reader can reproduce the build offline. The repository does not pretend to
reproduce it on every pull request. This is weaker than the computation gate in
one respect and stronger in another, and the difference is named rather than
hidden.

## Exact edits a later public fold would make

Not applied here. Listed so the fold is mechanical.

```
POLICY.md  §2 Layout     add a line: lean/  formal artifacts, one directory per
                         named artifact. (Section 2 says directories are created
                         only when they receive real content, so this line lands
                         with the first artifact, not before.)
POLICY.md  §4 Evidence   replace the bullet "An independent proof may earn `T`;
                         its verifier is then an audit." with the same sentence
                         plus the definition of independently theorem-grade
                         (Rule 1) and the exhaustion clause (Rule 2).
POLICY.md  §4 Evidence   amend "A one-architecture finite result is at most `C`
                         unless its proof is independently theorem-grade." to
                         point at that definition.
POLICY.md  §4 Evidence   add the method-ceiling obligation (Rule 3).
POLICY.md  §7            add the Lean gate paragraph, since it is a gate and
                         section 7 is where gates live.
AGENTS.md  line 377      "Independent proof may establish `T`; the verifier then
                         audits it." gains the same pointer.
tools/                   new tools/check_lean_artifact.py implementing the
                         recorded-form checks listed above, plus its unit test,
                         in the style of the existing tools/check_*.py pair.
canon/REGISTRY.tsv       no schema change. The evidence field already accepts a
                         path, so lean/NAME/ fits without touching the schema.
```

## What this proposal does NOT decide

1. Which claim gets the first artifact. The natural candidate is the row audited
   in claude/AUDIT-T-RHO1-CERTIFICATE_2026-08-10.md, but that is a separate
   claim-and-scope decision.
2. Whether the J-algebra is stated against Mathlib's cyclotomic machinery or as
   an explicit rank-4 integer structure with the step map written out. The second
   is almost certainly the better trusted surface, because a reader checks a
   4-tuple and an explicit multiplication in one minute and cannot check
   `IsCyclotomicExtension` in one minute. Recommended, not decided.
3. Whether the audit runs as a public probe or as an internal pass first.

## Falsifier for this proposal

This proposal is wrong and should be dropped if any of the following holds:

1. The audit finds that all 125 T rows already satisfy the new definition. Then
   the definition changed nothing and only added ceremony.
2. A formal artifact meeting Rule 1 turns out to be unbuildable for any TWIST-J
   claim within a realistic effort, in which case the rule is a rule nobody can
   follow and it degrades to decoration.
3. The recorded-form CI check is shown to be forgeable without producing a real
   build, so that the gate certifies nothing a reader could not have written by
   hand.

Item 3 is the serious one and should be attacked first, before any public fold.
