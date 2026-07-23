# PROMO-C-QUANT-SUBSTRATE-SCHWINGER-1

**STATUS: NON-CANONICAL PROMOTION PROPOSAL.** This note has no authority,
changes no public status, edits no Canon ledger, and authorizes no physical
probe. It freezes one arithmetic promotion proposal and the firewall around
the still-open physical coupling. A later, separately reviewed and
integer-versioned Canon fold may consume it.

## 0. Decision in one block

```text
candidate id             C-QUANT-SUBSTRATE-SCHWINGER-1
new public claim         QUANT-SCHWINGER-TARGET
proposed status          T, never T-LOCK
proposed content         J Jbar / script-Q = 1/(2 pi), arithmetic only
open physical owner      QUANT-SUBSTRATE [O], unchanged
adjacent dictionary      ELECTRON-G-TREE [D], unchanged
arithmetic layer         NOT_APPLICABLE
physical lift            candidate L5 -> L6, not yet defined or adopted
formal probe             none
normative action now     none
```

The owner decision proposed here is deliberately narrow:

1. register the exact scalar identity as `QUANT-SCHWINGER-TARGET [T]`;
2. replace "hypothesis value" in the `QUANT-SUBSTRATE [O]` wording by
   "exact arithmetic target whose physical realization remains open";
3. do not identify that scalar with a coefficient of the electron anomalous
   moment;
4. do not close, promote, or split `QUANT-SUBSTRATE`;
5. do not change `ELECTRON-G-TREE [D]`;
6. do not create an L5 to L6 gate until its source, target, normalization,
   admissible couplings, and equivalence relation are separately frozen.

## 1. Currency and authority

This proposal was prepared against:

```text
Public Canon            v16 ACTIVE
authority               mathorn1973/twist-j public main
tag                     canon-v16
activation commit       ffed1ff536972113cbc3d8f74830172206b3a489
content commit          a96f6c7a8ed63c2234977cb1c7a3432fd315bd7a
current main readback   537b56ee1881021a942d46cb7b1216712f482c29
Canon SHA-256           836b8d642f5209d46a5b833a3a1e7a1acc14a249e83066af1adb21845242d4a9
Canon bytes             89364
registry counts         194 claims: T 98, D 40, C 22, H 5, O 20, F 9
ledger counts           210 items, 291 dependencies, 194 evidence rows,
                        671 history events, 9 gates, 8 programs
```

The string `SS96.4` does not occur anywhere on public `main`. It is stale
private or legacy provenance, not a public dependency and not an edit target
for the later fold. No local v184 file is authority or evidence here.

The exact public sources are:

```text
J-MODULUS-CHORD [T]
  J Jbar = 2 - phi = phi^-2
  evidence: reproduce/kernel, two-architecture

BRIDGE-DEFECT [T]
  script-Q phi^2 = 2 pi
  script-Q / xi = 2 pi/5 = arg J
  evidence: reproduce/mass-ladder, two-architecture
```

The relevant physical boundary is also explicit:

```text
ELECTRON-G-RATIO [T]
  exact ratio and sixteen-identity block

ELECTRON-G-DOUBLE-COVER [T]
  exact orbital/spinor double-cover structure

ELECTRON-G-TREE [D]
  reads g = 2 from those exact pillars, but expressly does not derive
  the first-order coefficient

QUANT-SUBSTRATE [O]
  owns the unresolved Larmor and Schwinger physical gates
```

## 2. Exact proposed theorem

Let

```text
u = J Jbar,     q = script-Q.
```

The two registered theorem inputs give

```text
u phi^2 = 1,
q phi^2 = 2 pi.
```

Their exact polynomial consequence is

```text
q - 2 pi u
  = u (q phi^2 - 2 pi) - q (u phi^2 - 1)
  = 0.
```

Since `pi` and `q` are nonzero on the registered principal branch,
localization at `2 pi q` gives

```text
u / q = 1 / (2 pi),
```

or, in the public notation,

```text
J Jbar / script-Q = 1/(2 pi).
```

This is theorem-grade exact arithmetic. It uses no fit, numerical
approximation, dataset, coupling model, field normalization, regularization,
or new dimensionless factor. A verifier could audit the displayed ideal
membership, but it would not be the proof and no computation-only promotion
is being proposed.

## 3. Status firewall

The proposed `T` statement is only:

```text
QUANT-SCHWINGER-TARGET [T]:
J Jbar / script-Q = 1/(2 pi).
```

It is not any of the following:

```text
[alpha^1] ((g_e(alpha) - 2)/2) = 1/(2 pi)
a unique electron to electromagnetic substrate coupling
a normalized electron action
a regularized quantum correction
a measured value of g_e
a proof of the Schwinger term
a closure of the Larmor clause
a closure or promotion of QUANT-SUBSTRATE
```

Calling the scalar itself "the Schwinger coefficient" would cross this
firewall. The safe public name is "Schwinger target arithmetic": an exact
target nominated by an open physical gate.

`T-LOCK` is not proposed. Public v16 has no `T-LOCK` claim, and the two
source rows are `T`.

## 4. Falsifier first

There are two different decision surfaces.

### 4.1 Arithmetic fold gate

The arithmetic promotion must be rejected before fold if any of these occurs:

1. the authoritative Canon statements and evidence for the two source claims
   do not contain the two identities quoted above;
2. the displayed polynomial consequence is invalid;
3. a required denominator is zero on the registered branch;
4. the proposed registry scope identifies the scalar with a physical
   coefficient or coupling;
5. the registry scope hash, inline evidence hash, or history scope hash
   differs by one byte.

After a correct fold, the `T` row has no live FRONTIER falsifier. A later
contradiction would require the normal theorem correction process; thresholds
do not move.

### 4.2 Future physical gate

The physical question remains:

```text
a_e(alpha) := (g_e(alpha) - 2)/2,
C_S := [alpha^1] a_e(alpha),
C_S ?= QUANT-SCHWINGER-TARGET.
```

This notation is only a candidate interface for a later owner definition; it
is not preregistered by this promo. The coefficient operator is primary. The
equality

```text
[alpha^1] a_e(alpha) = (d/d alpha) a_e(alpha) at alpha = 0
```

may be used only after the future definition fixes a formal power-series or
analytic setting in which it is valid. Likewise, the shorthand
`a_e(alpha) = alpha/(2 pi) + O(alpha^2)` is not normative before the
coefficient algebra and remainder semantics are frozen.

A future physical preregistration must freeze at least:

```text
equation:
  [alpha^1] a_e(alpha) = J Jbar / script-Q

coefficient algebra:
  an explicit K[[alpha]], including K, the embedding, and all units

coupling:
  the exact electron to electromagnetic substrate action or current map

carrier and admissibility:
  the complete typed class of allowed couplings and states

equivalence:
  the exact relation under which two couplings count as the same

normalization:
  alpha, field, spinor, action, and observable conventions

read placement:
  pre-update or post-update, with the chosen convention frozen

regularization:
  either a complete exact rule or a proof that none is required

dataset:
  none for the exact formal gate

systematics:
  coupling choice, field normalization, spinor convention, action
  normalization, read placement, regularization, branch choice, and
  equivalence completeness

action layer:
  owner-frozen source and target; L5 -> L6 is only the present candidate
```

An eventual owner-frozen route grammar will need positive, negative, and stop
branches. The following is a non-binding design sketch, not an adopted
threshold:

```text
POSITIVE
  one coefficient modulo the frozen equivalence, equal exactly to the
  arithmetic target

NEGATIVE
  a complete exact derivation gives another coefficient; or a free
  dimensionless normalization survives; or two inequivalent admissible
  couplings give distinct coefficients

STOP
  the carrier, normalization, equivalence, layer typing, completeness, or
  arithmetic is missing or inexact; or the pinned checker does not reproduce
```

In any later frozen contract, NEGATIVE is science and must be preserved, while
STOP carries no physical conclusion. Exact branch wording and completeness
remain owner-definition debt.

## 5. Exact later-fold registry delta

If consumed directly while v16 remains active, add this six-column
`canon/REGISTRY.tsv` row. In the display below, `<EMPTY>` is presentation-only:
the actual fold writes a zero-length sixth field after the fifth tab. It does
not write `-`:

```tsv
QUANT-SCHWINGER-TARGET	T	the exact target-scalar identity J Jbar / script-Q = 1/(2 pi), derived from J Jbar = phi^-2 and script-Q phi^2 = 2 pi; arithmetic only, with no identification of this scalar with [alpha^1]((g_e(alpha)-2)/2), no substrate coupling, action, normalization, regularization, measured observable, or physical uniqueness claim	9. The photon and the electron	inline	<EMPTY>
```

The UTF-8 SHA-256 of the exact scope field is:

```text
b5711187fef0a23569061a7f55ba28c6d1c7fb1e6db2c14d46e1829b2da5cf7b
```

Replace the current `QUANT-SUBSTRATE` row by:

```tsv
QUANT-SUBSTRATE	O	the Larmor gate and the Schwinger physical-realization gate on the archimedean wall; QUANT-SCHWINGER-TARGET supplies the exact arithmetic scalar J Jbar / script-Q = 1/(2 pi), while deriving it as [alpha^1]((g_e(alpha)-2)/2) from a substrate coupling remains open	18. The frontier	inline	the two physical gates decide: exact gate values close the Larmor clause; the Schwinger branch has exact arithmetic target J Jbar / script-Q = 1/(2 pi), and a failed physical-realization gate fires it
```

The UTF-8 SHA-256 of that replacement scope field is:

```text
f4635e0c7cccf3015db2992909ec128807144665c26e9a98c4021602cd9fd6df
```

The parent remains `O`. This is an `O -> O` scope clarification, not a
promotion.

## 6. Exact later-fold Canon text

### 6.1 Notation

Extend the notation paragraph with:

```text
script-Q is the exact bridge scalar of BRIDGE-DEFECT [T], fixed by
script-Q phi^2 = 2 pi; it is derived notation, not a new primitive.
```

### 6.2 Section 9

After the existing `ELECTRON-G-TREE` paragraph, add:

```text
The scalar nominated by the still-open first-order question is already exact
arithmetic. Write u = J Jbar and q = script-Q. J-MODULUS-CHORD [T] gives
u phi^2 = 1, while BRIDGE-DEFECT [T] gives q phi^2 = 2 pi. Hence
q - 2 pi u = u(q phi^2 - 2 pi) - q(u phi^2 - 1) = 0, and therefore
J Jbar / script-Q = 1/(2 pi) (QUANT-SCHWINGER-TARGET [T]). This theorem
fixes only the target scalar. It does not identify that scalar with
[alpha^1]((g_e(alpha)-2)/2), construct a substrate coupling, fix an action
normalization or regularization, or close QUANT-SUBSTRATE [O].
```

### 6.3 Sections 16 and 18

In section 16, replace the complete existing span:

```text
hypothesis value J Jbar / script-Q = 1/(2 pi) (QUANT-SUBSTRATE)
```

by this exact span:

```text
exact arithmetic target J Jbar / script-Q = 1/(2 pi) (QUANT-SCHWINGER-TARGET [T]), whose physical realization as the first-order electron coefficient remains open inside QUANT-SUBSTRATE [O]
```

Section 18 is manual Canon prose. Replace its `QUANT-SUBSTRATE` frontier-table
summary by scope-equivalent wording:

```text
QUANT-SUBSTRATE    the Larmor gate and the Schwinger physical-realization
                   gate; the target scalar is exact arithmetic and its
                   production as the first-order coefficient remains open
```

Regenerate `canon/FRONTIER.md` from the exact registry row. Do not
hand-maintain a divergent generated view.

## 7. Companion-ledger edits in the later fold

### 7.1 NORMATIVE.tsv

Add:

```tsv
QUANT-SCHWINGER-TARGET	THEOREM	QUANT-SCHWINGER-TARGET	T	NOT_APPLICABLE		canon/CANON.md::9. The photon and the electron
```

Keep the existing `QUANT-SUBSTRATE` obligation row at `O`,
`NOT_APPLICABLE`, with no gate id.

### 7.2 DEPENDENCIES.tsv

Add exactly the arithmetic edges:

```tsv
QUANT-SCHWINGER-TARGET	J-MODULUS-CHORD	REQUIRES	the target scalar uses the registered exact modulus identity J Jbar = phi^-2
QUANT-SCHWINGER-TARGET	BRIDGE-DEFECT	REQUIRES	the target scalar uses the registered exact bridge script-Q phi^2 = 2 pi
QUANT-SUBSTRATE	QUANT-SCHWINGER-TARGET	REQUIRES	the open physical gate consumes the exact arithmetic target without thereby realizing it
```

Do not add direct parent edges to `ELECTRON-G-RATIO` or
`ELECTRON-G-DOUBLE-COVER` in this arithmetic fold. They remain the exact
pillars of `ELECTRON-G-TREE [D]`; no QUANT consumption edge is currently
registered. A future typed coupling definition must state how it consumes
them.

### 7.3 EVIDENCE.tsv

Add:

```tsv
QUANT-SCHWINGER-TARGET	EV-QUANT-SCHWINGER-TARGET	INLINE_CANON	inline	b5711187fef0a23569061a7f55ba28c6d1c7fb1e6db2c14d46e1829b2da5cf7b	registry-scope-sha256-v1	none
```

Update the existing parent evidence row to:

```tsv
QUANT-SUBSTRATE	EV-QUANT-SUBSTRATE	INLINE_CANON	inline	f4635e0c7cccf3015db2992909ec128807144665c26e9a98c4021602cd9fd6df	registry-scope-sha256-v1	none
```

No unrelated inline evidence is re-pinned. Since v13, inline evidence hashes
the stable registry scope, not the whole Canon file.

### 7.4 HISTORY.tsv

For an immediate v16 to v17 fold, append templates equivalent to:

```tsv
CANON17-DECLARE-QUANT-SCHWINGER-TARGET	1	<FOLD-DATE>	canon-v17	QUANT-SCHWINGER-TARGET	DECLARE	-	T	b5711187fef0a23569061a7f55ba28c6d1c7fb1e6db2c14d46e1829b2da5cf7b	EV-QUANT-SCHWINGER-TARGET	inline	b5711187fef0a23569061a7f55ba28c6d1c7fb1e6db2c14d46e1829b2da5cf7b	The exact target scalar is a theorem-grade consequence of J-MODULUS-CHORD and BRIDGE-DEFECT; no physical coefficient, coupling, normalization, regularization, or uniqueness claim is added
CANON17-SCOPE-QUANT-SUBSTRATE	14	<FOLD-DATE>	canon-v17	QUANT-SUBSTRATE	SCOPE_CHANGE	O	O	f4635e0c7cccf3015db2992909ec128807144665c26e9a98c4021602cd9fd6df	EV-QUANT-SUBSTRATE	inline	f4635e0c7cccf3015db2992909ec128807144665c26e9a98c4021602cd9fd6df	The arithmetic target is separated from its unresolved physical realization; the Larmor and Schwinger gates remain open and the parent status remains O
```

Recompute the release name, event ids, date, and next parent sequence if any
other fold lands first.

### 7.5 Generated and release files

Starting directly from v16, the expected count delta is:

```text
claims             194 -> 195
T                   98 -> 99
D                   40 -> 40
C                   22 -> 22
H                    5 -> 5
O                   20 -> 20
F                    9 -> 9
live H/O            25 -> 25
NORMATIVE items    210 -> 211
DEPENDENCIES       291 -> 294
EVIDENCE rows      194 -> 195
architecture none   38 -> 39
HISTORY events     671 -> 673
GATES                9 -> 9
programs             8 -> 8
```

The later content fold must update or regenerate, as applicable:

```text
canon/CANON.md
canon/REGISTRY.tsv
canon/NORMATIVE.tsv
canon/DEPENDENCIES.tsv
canon/EVIDENCE.tsv
canon/HISTORY.tsv
canon/FRONTIER.md
canon/CORE.md
canon/CHANGELOG.md
canon/STATUS_COUNTS.tsv
canon/SHA256SUMS
reproduce/status-separation/verify.py
reproduce/status-separation/EXPECTED.txt
reproduce/status-separation/README.md
```

The status-separation reproduction must do more than bump its hard-coded
count. Add a tenth semantic check requiring all of the following:

```text
QUANT-SCHWINGER-TARGET has status T
QUANT-SUBSTRATE remains status O
J-MODULUS-CHORD and BRIDGE-DEFECT both have status T
the target scope contains J Jbar / script-Q = 1/(2 pi)
the target scope retains its explicit arithmetic-only and no-identification
firewall, and the parent scope retains that physical realization remains open
```

Update its transcript from `9/9` to `10/10`. In its README, change "nine
checks" to "ten checks" and `RESULT 9/9 ALL PASS` to `RESULT 10/10 ALL PASS`.
The repository-wide reproduction count remains 22.

`canon/GATES.tsv`, `canon/FRONTIER_PROGRAMS.tsv`, and
`canon/CORE_SELECTION.tsv` remain byte-unchanged in this minimal arithmetic
fold. In particular, keep the one existing scheduler row:

```tsv
QUANT-SUBSTRATE	QUANTUM_EM	ROOT	READY	FORMAL
```

Freeze the content-fold `CHANGELOG.md` entry from this template, re-keyed if
another fold lands first:

```text
Canon v17 adds QUANT-SCHWINGER-TARGET [T] as an exact arithmetic consequence
of J-MODULUS-CHORD [T] and BRIDGE-DEFECT [T]. QUANT-SUBSTRATE remains [O]:
production of that scalar as the first-order electron coefficient is not
derived. No physical child split, gate, or formal probe is adopted.
```

The separate release-form commit changes only:

```text
STATUS.md
README.md
CITATION.cff
```

It records the actual content commit, Canon hash, byte count, version, tag,
and activation data. Public v16 remains authoritative until that form is
merged, tagged, and publicly read back.

## 8. Deferred physical decomposition

This promo does not adopt child rows.

Non-canonical genesis reconstruction already contains:

```text
QUANT-LARMOR-GATE       [O], L5
QUANT-SCHWINGER-TERM    [H], MULTI
```

The alternative names `QUANT-SUBSTRATE-LARMOR` and
`QUANT-SUBSTRATE-SCHWINGER`, both at `O`, are therefore not a mechanical
cleanup. A separate owner-definition or governance fold must decide:

1. stable child identifiers and statuses;
2. the exact Larmor equation and action layer;
3. the exact Schwinger source and target types;
4. whether L5 to L6 is the correct physical lift;
5. named `GATES.tsv` rows for every interlayer lift;
6. parent closure logic and child dependencies;
7. `FRONTIER_PROGRAMS.tsv` rows for every new live `H` or `O` child;
8. evidence, history, count, and generated-frontier effects.

There is also a graph trap. The public ledger already has:

```text
ELECTRON-G-TREE BOUNDED_BY QUANT-SUBSTRATE.
```

If a new Schwinger child depends on `ELECTRON-G-TREE` and the parent depends
on that child, the result is cyclic. A safe child design should consume the
exact `ELECTRON-G-RATIO`, `ELECTRON-G-DOUBLE-COVER`, and
`QUANT-SCHWINGER-TARGET` pillars directly, unless a separate reviewed fold
changes the existing tree boundary.

No physical child probe may be preregistered until this definition debt is
resolved.

## 9. Scope firewall

This proposal does not:

- remove anything called `SS96.4` from public files, because it is absent;
- promote `ELECTRON-G-TREE [D]`;
- promote or close `QUANT-SUBSTRATE [O]`;
- claim that `g = 2` or its first correction is an algebraic theorem;
- derive a substrate action, current, or electron coupling;
- choose a field, spinor, action, or alpha normalization;
- choose pre-update versus post-update reading;
- choose a regularization or prove that none is needed;
- assert uniqueness among an undefined class of couplings;
- create a measured prediction or compare with experimental data;
- cross L5 to L6;
- authorize a formal execution;
- edit Canon, registry, frontier, dependency, gate, status, release, or tag
  files in the promo-note pull request.

The arithmetic target and its physical production are separate claims with
separate status ceilings.

## 10. Validation checklist

The promo-note pull request changes only this file and runs the ordinary
repository checks. It contains no executable artifact.

The later sealed content fold must start from then-current public `main` and
run at minimum:

```text
python tools/generate_canon_views.py --apply
python tools/generate_canon_views.py --check-dir canon
python tools/check_policy.py
python -m unittest discover -s tools -p "test_*.py"
python tools/check_canon.py
python tools/check_ledger.py
python tools/check_verifier.py --base <ACTUAL-FOLD-BASE>
python tools/check_reproduce.py --base <ACTUAL-FOLD-BASE>
git diff --check
```

After that checklist passes, create the immutable content commit. Then, on the
separate release-form head whose `STATUS.md` names that commit, run:

```text
python tools/check_activation.py --full --content-commit <NEXT-CONTENT-COMMIT>
```

The fold also requires a named-file security review, a merge commit, the
separate release-form commit, the integer Canon tag, and public byte readback.
No squash, rebase, or silent composition with an unrelated scientific
promotion.

## 11. Security

This proposal contains markdown only. It carries no secrets, credentials,
private hostnames, machine nicknames, binary assets, model files, or private
logs.
