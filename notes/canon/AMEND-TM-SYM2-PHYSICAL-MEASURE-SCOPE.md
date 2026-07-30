# AMEND-TM-SYM2-PHYSICAL-MEASURE-SCOPE

**STATUS: NON-CANONICAL OWNER DISPOSITION. NO PROBE RUN. NO CANON CHANGE.**
This note has no normative authority and changes no claim, gate, frontier,
count, hash, tag, release, or status. It records one candidate input for a
later, separately approved Public Canon v28 fold.

```text
candidate queue       to be opened
public base           Public Canon v27 ACTIVE
base main             b0a53eb65e3a3511af28f5876b9d1bb882bda160
tag                   canon-v27
content commit        116b62edf505914d96fcd65318d97f3675c53f85
Canon SHA-256         c7c4c7e6d5a3116e356b060eaf696963285b0f2f465d5f2e1dcda5c094a309f6
Canon bytes           150959
claim                 TM-SYM2-PHYSICAL-MEASURE
current status        O
proposed action       SCOPE_CHANGE, O to O
owned gate            GATE-L5-L6-TM-SYM2-BORN-MEASURE
formal execution      none
provisional release   Public Canon v28, composed with other approved inputs
```

The eventual fold must start from the then-current public `main`. The tuple
above is the currency stamp for this disposition, not permission to reuse
stale release fields.

## 1. Owner decision

Amend the scope of `TM-SYM2-PHYSICAL-MEASURE`. Do not retire it, and do not
close it as `F`.

The row states its answer before it states its question. It requires a future
bridge to "preserve the exact selector-independent outputs mu_i = 1/6 and
M_TM = (1/3)P1 + (2/15)P5" and to "derive the typed factorization
1/6 = (1/2)(1/3)". Those are the values a bridge would be trying to establish.
Requiring them in advance converts the obligation from an open question into a
target with a slot for a construction fitted to it. That is the reverse of the
order this program requires, and it is the defect this amendment removes.

The amendment keeps the obligation live, keeps every methodological constraint
that is genuinely a constraint, and moves the target values from the
requirement side to the result side. It also adds the explicit circularity
rejection the registry uses elsewhere for exactly this failure.

## 2. Registered precedent for this operation

This is not a new manoeuvre. Public Canon v13 performed it on a structurally
identical defect:

```text
CANON13-SCOPE-DE-CONFORMAL-WEIGHT  13  2026-07-20  canon-v13
DE-CONFORMAL-WEIGHT  SCOPE_CHANGE  O -> O
rationale: Public Canon v13 records the exact FRW nonuniqueness boundary,
removes the circular target-value falsifier, and leaves every dictionary
source and physical transport open
```

The resulting `DE-CONFORMAL-WEIGHT` row is the house pattern: the scope names
the object "if any" and defines the target quantity rather than fixing its
value, and the falsifier ends with an explicit `reject as CIRCULAR any closure
that assumes ...` clause naming the forbidden target values. The text below
follows that pattern term for term.

## 3. Exact field replacements

### 3.1 `canon/REGISTRY.tsv`, field 3, scope

Remove:

```text
the open physical L5-to-L6 obligation for a separately owner-approved successor L5 source that starts from the complete projective-gauge orbit record, retains reading orientation epsilon_read = chi_Q chi_F as typed L5 data rather than quotienting it, and maps to a normalized physical measure on the six golden lines; it must prove rather than assume coherence across all 48 selectors, preserve the exact selector-independent outputs mu_i = 1/6 and M_TM = (1/3)P1 + (2/15)P5, and derive the typed factorization 1/6 = (1/2)(1/3) compatibly with MEASURE-BORN-VERB and GYRON-DENSITY; Gamma_sl and R, N, and NR are comparison actions only, no successor L5 source is presently frozen, and no enlarged postcomposition gauge is adopted
```

Insert:

```text
the typed physical L5-to-L6 bridge, if any, from an owner-approved successor L5 source to a normalized physical measure on the six golden lines of GOLDEN-SIX-LINE-SYM2-FRAME; the source must start from the complete projective-gauge orbit record, retain reading orientation epsilon_read = chi_Q chi_F as typed L5 data rather than quotienting it, select no representative among the 48 selectors, enlarge no postcomposition gauge, and prove rather than assume coherence across all 48 selectors; whether the resulting physical measure agrees with the exact selector-independent mathematical image mu_i = 1/6 and M_TM = (1/3)P1 + (2/15)P5 registered by TM-SYM2-PROJECTIVE-FOURFOLD is an outcome of the bridge and is not required of it; Gamma_sl and R, N, and NR are comparison actions only, no successor L5 source is presently frozen, and no typed factorization, Born reading, or L6 measure is asserted here
```

Old 728 bytes, new 902 bytes.

### 3.2 `canon/REGISTRY.tsv`, field 6, falsifier

Remove:

```text
STOP until the successor L5 source schema, retained-orientation type, allowed action and coherence law, physical Born carrier, total map, complete dependency graph, and completeness proof are frozen; closes positively only when an exact public total bridge on every frozen projective orbit gives one normalized physical measure with the stated outputs and derives the factorization; closes negatively only if a frozen complete admissible bridge class is empty, required coherence gives inequivalent physical outputs on residual classes, or every bridge violates the registered Born, GYRON, or normalization constraints; the fired N2 is a boundary and may not be repaired by enlarging gauge
```

Insert:

```text
the fired N2 of TM-SYM2-MEASURE proves the frozen projective-gauge action supplies no canonical selector stream and is a boundary that may not be repaired by enlarging gauge; STOP while the successor L5 source schema, retained-orientation type, allowed action and coherence law, physical Born carrier, total map, complete dependency graph, or completeness proof is incomplete; closes positively only when an exact public total bridge on every frozen projective orbit yields one normalized physical measure, with its agreement or disagreement with the registered mathematical image recorded as the result rather than assumed in advance; closes negatively only if a frozen complete admissible bridge class is empty, required coherence gives inequivalent physical outputs on residual classes, or every bridge violates the registered Born, GYRON, or normalization constraints; reject as CIRCULAR any closure that assumes mu_i = 1/6, M_TM = (1/3)P1 + (2/15)P5, or the factorization 1/6 = (1/2)(1/3), or that imports GYRON-DENSITY or MEASURE-BORN-VERB to select the physical values rather than to constrain the type
```

Old 689 bytes, new 1109 bytes.

### 3.3 `canon/GATES.tsv`, `GATE-L5-L6-TM-SYM2-BORN-MEASURE`, field 6

The gate carries the same defect and must be corrected with the row. Remove
the clause `with mu_i = 1/6, M_TM = (1/3)P1 + (2/15)P5, and a derivation of
1/6 = (1/2)(1/3) compatible with GYRON-DENSITY` and replace the condition
with:

```text
closes this owner only when a separately owner-approved complete L5 source, with reading orientation retained as typed data and no representative or enlarged gauge chosen, is mapped by a total exact Born bridge to a normalized L6 measure coherent on all 48 selectors, whose values are read off the bridge rather than imposed on it; exact class-dependent disagreement or violation of registered Born, GYRON, or normalization constraints routes NEGATIVE, while any unfrozen source type, action law, carrier, map, dependency, or completeness proof routes STOP; a closure that assumes mu_i = 1/6, M_TM = (1/3)P1 + (2/15)P5, or the factorization 1/6 = (1/2)(1/3) is CIRCULAR and does not close this gate
```

### 3.4 `canon/DEPENDENCIES.tsv`, the `GYRON-DENSITY` edge

The edge stays `REQUIRES`. Its basis is tightened so the compatibility
requirement cannot be read as a value requirement. Remove `the proposed
physical normalization must remain compatible with the registered density
reading` and insert:

```text
the proposed physical normalization must be typed compatibly with the registered density reading; agreement of values is a result of the bridge, not a precondition on it
```

The seven other outgoing edges are unchanged. The `MEASURE-BORN-VERB` basis
already says `rather than an assumed weight` and needs no change.

### 3.5 `canon/CANON.md`, section 18 paragraph

Remove:

```text
TM-SYM2-PHYSICAL-MEASURE [O] is the surviving physical L5-to-L6
obligation. A future successor must start from the complete four-orbit
projective-gauge record, retain epsilon_read as typed L5
reading-orientation data, prove coherence on all 48 selectors without
choosing a representative or enlarging the gauge, and derive a normalized
physical measure with mu_i = 1/6,
M_TM = (1/3)P1 + (2/15)P5, and the typed factorization
1/6 = (1/2)(1/3), compatibly with MEASURE-BORN-VERB and GYRON-DENSITY.
No successor L5 source schema is currently frozen. The Born gate remains
open but the scheduler is STOP pending a separately reviewed owner
definition.
```

Insert:

```text
TM-SYM2-PHYSICAL-MEASURE [O] is the surviving physical L5-to-L6
obligation. A future successor must start from the complete four-orbit
projective-gauge record, retain epsilon_read as typed L5
reading-orientation data, prove coherence on all 48 selectors without
choosing a representative or enlarging the gauge, and derive a normalized
physical measure. Whether that measure agrees with the exact
selector-independent mathematical image mu_i = 1/6 and
M_TM = (1/3)P1 + (2/15)P5, proved by TM-SYM2-PROJECTIVE-FOURFOLD, is an
outcome of the bridge and is not required of it; a closure that assumes
those values, or the typed factorization 1/6 = (1/2)(1/3), is CIRCULAR.
MEASURE-BORN-VERB and GYRON-DENSITY constrain the type of the physical
measure clause; they do not select its values. No successor L5 source
schema is currently frozen. The Born gate remains open but the scheduler
is STOP while a separately reviewed owner definition is absent.
```

## 4. New evidence pin

The evidence hash is `registry-scope-sha256-v1`, which `tools/check_ledger.py`
computes as the SHA-256 of the UTF-8 bytes of `REGISTRY.tsv` field 3 with no
trailing newline. The convention was confirmed by recomputing the current pin
exactly.

```text
old scope SHA-256   c794a296aec9df49ac497c536ba26559ff26d5e73faaf5bf92bf61194405ef27
new scope SHA-256   e3f9f4a4a3fec612bf622e281cca43dcc0fd7665552dd5d0f690abaae7cd096e
```

`canon/EVIDENCE.tsv` becomes:

```tsv
TM-SYM2-PHYSICAL-MEASURE	EV-TM-SYM2-PHYSICAL-MEASURE	INLINE_CANON	inline	e3f9f4a4a3fec612bf622e281cca43dcc0fd7665552dd5d0f690abaae7cd096e	registry-scope-sha256-v1	none
```

## 5. History event

The claim has exactly one history event, the v19 `DECLARE` at sequence 1, so
this amendment is sequence 2. `tools/check_ledger.py` requires the latest event
to carry both the current scope hash and the current evidence triple, so this
row is mandatory, not optional.

```tsv
CANON28-SCOPE-TM-SYM2-PHYSICAL-MEASURE	2	<RELEASE-DATE>	canon-v28	TM-SYM2-PHYSICAL-MEASURE	SCOPE_CHANGE	O	O	e3f9f4a4a3fec612bf622e281cca43dcc0fd7665552dd5d0f690abaae7cd096e	EV-TM-SYM2-PHYSICAL-MEASURE	inline	e3f9f4a4a3fec612bf622e281cca43dcc0fd7665552dd5d0f690abaae7cd096e	Public Canon v28 removes the circular target-value requirement from the open physical bridge: the exact selector-independent mathematical image remains registered where it was proved, agreement of the physical measure with it becomes a result rather than a precondition, and the fired N2 boundary, the three exact classifications, and every status and count remain unchanged
```

The event identifier, release label, and date must be checked again against the
composed v28 batch.

## 6. Boundary to preserve, unchanged

The fold must preserve without status or scope change:

```text
TM-SYM2-MEASURE                  [F]
TM-SYM2-PROJECTIVE-FOURFOLD      [T]
TM-SYM2-SEMILINEAR-TWOFOLD       [T]
TM-SYM2-REVERSAL-CLOSURE         [T]
GOLDEN-SIX-LINE-SYM2-FRAME       [T]
GYRON-DENSITY                    [T]
GATE-L1-L5-TM-SYM2-SELECTOR-STREAM = FIRED_NEGATIVE
```

The complete selector class has size 48 in four free orbits of size 12 under
the frozen projective-linear gauge. N2 is terminal and may not be moved,
reopened, or repaired. The semilinear and reversal actions remain comparisons,
not adopted gauge. `epsilon_read = chi_Q chi_F` remains typed
reading-orientation data. No representative is selected among the 48 selectors.
Every selector keeps the mathematical image `nu_s(v_i) = 1/6` and the common
operator `M_s = (1/3)P1 + (2/15)P5` at the scope where those were proved.
Neither equality is promoted to physical probability, Born halving, or an L6
measure theorem. This amendment moves none of that; it only stops the open row
from demanding those values of a bridge that does not yet exist.

## 7. Exact fold operations

Nine tracked paths change. Four are edited by hand, four are derived, one is
the activation form.

```text
edit      canon/REGISTRY.tsv          fields 3 and 6 of the claim row
edit      canon/EVIDENCE.tsv          sha256 of the claim row
edit      canon/GATES.tsv             decision_condition of the owned gate
edit      canon/DEPENDENCIES.tsv      basis of the GYRON-DENSITY edge
append    canon/HISTORY.tsv           the sequence 2 SCOPE_CHANGE event
edit      canon/CANON.md              the section 18 paragraph, plus the v28
                                      release anchors and signed block
edit      canon/CHANGELOG.md          the composed v28 entry and count markers
edit      canon/CORE.md               release identity to Public Canon v28
generate  canon/FRONTIER.md           tools/generate_canon_views.py --apply
generate  canon/STATUS_COUNTS.tsv     same command, no delta expected
recompute canon/SHA256SUMS            five hashes
edit      STATUS.md                   CANON, TAG, CONTENT_COMMIT,
                                      CANON_SHA256, CANON_BYTES
edit      CITATION.cff                version to the whole Canon number
```

`canon/NORMATIVE.tsv` and `canon/FRONTIER_PROGRAMS.tsv` are unchanged: the item
type stays `OBLIGATION`, the layer stays `MULTI`, the gate id is the same, and
the program row stays `MEASURE / ROOT / STOP / FORMAL`.

## 8. Count delta

None. This is the property that distinguishes the amendment from the retirement
alternative.

```text
claims                       214 -> 214
T                            113 -> 113
D                             40 -> 40
C                             23 -> 23
H                              4 -> 4
O                             24 -> 24
F                             10 -> 10
NORMATIVE rows               230 -> 230
DEPENDENCIES                 345 -> 345
EVIDENCE rows                214 -> 214
GATES                         11 -> 11
FRONTIER_PROGRAMS              8 -> 8
HISTORY events               704 -> 705
```

Only the history count moves. `canon/STATUS_COUNTS.tsv` regenerates with a zero
diff, confirmed below.

## 9. Machine verification

The amendment was applied to a scratch copy of v27 `main` and the repository
checkers were run before and after. Release labels were deliberately held at
v27 so the checks exercise the amendment alone and not the version bump.

```text
environment  LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC

before
  tools/check_canon.py          CANON PASS v27 claims=214
  tools/check_ledger.py         LEDGER PASS claims=214 items=230
                                dependencies=345 evidence=214 history=704
                                gates=11 programs=8

after
  tools/check_canon.py          CANON PASS v27 claims=214
  tools/check_ledger.py         LEDGER PASS claims=214 items=230
                                dependencies=345 evidence=214 history=705
                                gates=11 programs=8
  tools/check_status_labels.py  STATUS LABELS PASS
  tools/check_policy.py         POLICY PASS
  canon/STATUS_COUNTS.tsv       zero diff
```

Text-level gates the new strings were checked against directly, from
`tools/check_canon.py`: no non-public authority word matches
`\b(sealed|internal|private|hidden|unpublished)\b` in either field; the
falsifier contains none of the eight placeholder phrases, in particular not the
substring `pending`; the falsifier exceeds the twenty-character minimum; every
claim identifier the new text names is registered.

## 10. Attempts to break the amendment

Four attacks were run against the claim that the rewrite removes the reverse
ordering. One was substantive and is recorded with its refutation.

**Attack 1, normalization is still required.** Refuted. Normalization is part of
what the word measure means, not a value fixed in advance.

**Attack 2, coherence across all 48 selectors is still required.** Refuted. The
requirement is structural, not numerical, and the falsifier registers
incoherence as a permitted negative close: `required coherence gives
inequivalent physical outputs on residual classes`. Incoherence is an available
outcome, not an excluded one.

**Attack 3, the GYRON clause smuggles 1/6 back in.** This was the serious one.
The falsifier still permits a negative close when a bridge violates
`registered ... GYRON ... constraints`, and the named density limit of
`GYRON-DENSITY` is `1/6`. If that constraint transferred to the physical
measure, the amendment would move the circularity rather than remove it.
Refuted by the registered scope of `GYRON-DENSITY [T]` itself, which ends

> no six-line cardinal average, Born multiplier, mass density, cosmological
> parameter, selector weight, physical probability or measure, L5 stream, or L6
> measure is claimed

and whose falsifier adds that `another occurrence of the number 1/6 on another
carrier is outside scope`. The registry already firewalls exactly this
transfer. The amended dependency basis in 3.4 makes the firewall explicit at
the edge as well.

**Attack 4, naming the values at all anchors the answer.** Refuted. The values
are named precisely in order to forbid assuming them. Silence would be weaker:
a future author could target the same numbers with no registered prohibition to
violate. The `DE-CONFORMAL-WEIGHT` precedent names `w = -14/15`,
`Delta_DE = 1/p` and the rest in exactly this way.

One further observation, in the other direction. The old wording did not only
prejudge; it also made the interesting outcome unregistrable. Under the old
scope a bridge that produced a physical measure differing from the mathematical
image could not close the row positively, because the row required
preservation. The amendment strictly increases what the obligation can learn.

## 11. Re-entry rule

Unchanged in substance. The claim identifier, the owner, and the gate all
survive the amendment, so nothing is retired and no new identifier is needed. A
future closure attempt must still supply a concrete, independently motivated L5
source, freeze its carrier, retained orientation, allowed actions, total map,
coherence law, complete dependencies, completeness claim and falsifiers before
computation, and only then test which L6 measure, if any, it produces. No step
in this note authorizes that work.
