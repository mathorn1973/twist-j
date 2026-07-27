# TWIST-J non-canonical incubation

```text
STATUS:     NON-CANONICAL
AUTHORITY:  NONE
PURPOSE:    exact candidate development, independent breaking, and PROMO handoff
```

This directory is not Canon, a public probe, evidence, or a status ledger.
Nothing here changes `canon/`, closes a frontier row, or earns public authority.
`AGENTS.md` and `POLICY.md` govern all work.

## 1. Roles and handoff

Use the stable roles from `AGENTS.md`:

```text
PUBLIC_ROLE
BUILDER_ROLE
BREAKER_ROLE
ARCHITECTURE_RUNNER_ROLE
```

Concrete products, people, machines, and sessions are assigned in the claim
issue or run record. They are not fixed by this README.

Public `main` is the sole public scientific authority. Other work has no public
authority until handed off through Git and accepted by the public procedure.

The only handoff is a committed `PROMO.md` package in public Git. An attachment,
private workspace, or chat summary is not a handoff and carries no currency.

## 2. Candidate identity

Each candidate has one immutable incubation identifier:

```text
C-<TOPIC>-<N>
```

`TOPIC` uses uppercase ASCII letters, digits, and hyphens. `N` is a positive
integer. The identifier names the incubation package only. It does not imply a
public claim, probe, branch, or registry identifier.

## 3. Object lock before files

Before creating a candidate directory, define:

```text
OBJECT_KEY
CLAIM_KEY
OWNER_SESSION
```

For an existing object, `OBJECT_KEY` is its public registry, frontier, probe,
policy, or file identifier. A new object uses `NEW:<sha256>` of the exact UTF-8,
LF-terminated scope statement stored in the issue.

Then:

1. create one GitHub issue already assigned in the same server-side operation;
2. record the three identifiers in the issue body;
3. read the issue back;
4. create no branch or commit before that readback.

Among active builder issues with the same exact `OBJECT_KEY`, the lowest issue
number is the sole build owner. Every higher-numbered issue stops and closes as
duplicate before committing. A breaker works against the winning issue and does
not acquire a competing build lock.

A lock has no automatic timeout. Release requires an issue comment containing
exactly:

```text
LOCK_RELEASED
```

followed by unassignment or closure by the owner session or repository owner. A
successor must read the release record before claiming the object.

String equality is not a theorem of content equality. Search issues, branches,
probes, the registry, and promotion packages for equivalent scopes. A suspected
equivalence is `OBJECT-COLLISION / STOP` until an owner ruling identifies or
separates the objects.

## 4. Directory shape

A complete candidate package has:

```text
notes/incubation/C-FOO-1/
  CLAIM.md
  PREREG.md
  verify.py
  break.py
  RESULT.md
  PROMO.md
```

Files appear only when they have real content. Before an independent breaker is
successfully frozen, `break.py` may be absent. Before promotion is proposed,
`PROMO.md` may be absent. A candidate is not complete merely because all names
exist.

### `CLAIM.md`

Records exactly one value for:

```text
incubation_id
object_key
claim_key
claim_issue
owner_session
builder_session
status: NO-AUTHORITY
scope
excluded_scope
dependencies
action_layer
```

### `PREREG.md`

Freezes six fields before computation:

```text
1. exact claim
2. exact domain and equality
3. accepted inputs and dependencies
4. method and systematics
5. failure threshold and falsifiers
6. action layer L1 to L6
```

It also defines every output field needed by an independent breaker. A breaker
must be able to determine what would falsify the claim without reading
`verify.py`.

A revision records:

```text
prereg_revision: 1 or 2
prereg_sha256
```

There is no revision 3 under one candidate identifier.

### `verify.py`

The builder's exact construction route. Standard library only. Integers and
exact rational arithmetic first. Scientific stdout follows the portability
rules in `AGENTS.md`.

### `break.py`

The breaker's independent attack, written only from the frozen `PREREG.md` and
its explicitly named public dependencies. It must not import, invoke, wrap,
copy, translate, or inspect `verify.py` before its own freeze.

It records a distinct non-secret:

```text
breaker_session
```

### `RESULT.md`

Records only an incubation result:

```text
candidate-T
candidate-D
candidate-C
NEGATIVE
STOP
```

These are package labels, not public statuses. `RESULT.md` records pins, exact
commands, stdout hashes, scope, fired falsifiers, and whether the second route
was independent confirmation or reproduction only.

### `PROMO.md`

A proposed public handoff. It creates no public object and authorizes no fold.
It contains the explicit target map defined below.

## 5. Blind-breaker protocol

The builder freezes `PREREG.md` revision 1 and writes `verify.py`.

The breaker receives only:

- the exact frozen `PREREG.md`;
- public dependencies explicitly named there;
- no verifier bytes, verifier diff, expected output, implementation hint, or
  private explanation.

The breaker writes and freezes `break.py` before any comparison with the
builder's implementation. The breaker must use an independent representation,
derivation, enumeration, invariant, or code path.

### First underspecification

If no well-typed attack can be constructed, the breaker records:

```text
BLIND-BREAKER-UNDERSPECIFIED / STOP
```

The deficiency report lists only missing types, domains, equality rules,
dependencies, thresholds, or output fields. It must not disclose an attack
strategy, candidate counterexample, or implementation hint.

The builder may publish one revised preregistration under revision 2 and a new
pin.

### Second attempt

A different `breaker_session`, which has not read `verify.py`, the first
`break.py`, or private attack reasoning, performs the second blind attempt.

A second `BLIND-BREAKER-UNDERSPECIFIED / STOP` terminates the candidate. Further
work requires a new candidate identifier and a fresh object-lock review. There
is no third iteration under the same candidate.

The missing information may not be supplied privately after either pin.

If a breaker merely runs or translates the builder's verifier, the result is
reproduction. It is never independent confirmation.

After both routes are frozen, compare exact domains, equality, thresholds,
outputs, and falsifiers. Disagreement is a first-class result. Never repair a
candidate by moving a threshold or changing the claim after opening either
result.

The checker validates visible files, fields, hashes, sessions, and references.
It cannot prove what an agent saw outside Git. Blind independence is therefore
a signed process assertion bounded by the public Git record.

## 6. Formal computation boundary

Public computation status is governed by `AGENTS.md` section 6, `Formal public
computation gate`, and by the pinned workflow.

A manually written architecture value in `RUN.md` is audit metadata only. It is
not proof of machine identity. A computation-only public `T` requires successful
required workflow jobs on x86_64 and aarch64 against the same PR head, verifier,
and committed `EXPECTED.txt`.

Local and incubation reruns are development evidence only. Repeated runs on one
architecture contribute no second architecture.

Public run records use neutral fields. Machine nicknames and private
infrastructure are forbidden and checked under `probes/` and `reproduce/`.

## 7. Portable verifier output

The construction and breaker must remain byte-stable across every architecture
and Python minor version exercised by the required workflow.

Print only explicit finite strings, integers, signs, and rationals. Format a
rational manually as `numerator/denominator`; print denominator one as an
integer. Sort every collection before output.

Never print exception wording, tracebacks, object or container `repr`,
`sys.version`, paths, platform strings, hostnames, locale data, timezone data,
wall-clock values, randomized iteration order, or library-dependent decimal
formatting. Metadata belongs in run records, not scientific stdout.

## 8. Explicit promotion map

Promotion names are never inferred from the incubation identifier. `PROMO.md`
contains exactly one value for each field:

```text
incubation_id: C-FOO-BAR-1
target_issue: NONE
target_branch: probe/P-FOO-1
target_probe_id: P-FOO-1
target_claim_id: FOO-BAR
```

A target may be `NONE`. A field may not contain alternatives, wildcards,
fallbacks, or prose choices.

Before any public branch is created, search:

- open and closed issues;
- branches;
- `probes/`;
- `canon/REGISTRY.tsv`;
- other live `PROMO.md` packages.

The following are terminal until an owner ruling changes the manifest before
public execution:

```text
PROMO-NAME-COLLISION / STOP
PROMO-TARGET-AMBIGUOUS / STOP
PROMO-CONTENT-TARGET-MISMATCH / STOP
```

Two different incubation identifiers may never target the same live issue,
branch, probe identifier, or claim identifier. One incubation identifier may
never name two possible targets. Renaming by convention, prefix stripping, or
historical analogy is forbidden.

The examples

```text
C-FOO-BAR-1 -> FOO-BAR
PREREG-C-FOO-1.md -> probes/P-FOO-1/PREREG.md
```

are illustrations only. The explicit `PROMO.md` fields are the sole mapping.

## 9. Machine enforcement

`tools/check_incubation.py` checks the visible contract:

- candidate directory and file names;
- required single-valued fields;
- object, claim, owner, builder, and breaker session declarations;
- preregistration revision bounds;
- forbidden alternatives and duplicate promotion targets;
- visible references from `break.py` to `verify.py`;
- stable public result labels;
- machine nicknames and private infrastructure in public run records.

It does not prove mathematical equivalence of scopes, independence of private
knowledge, or absence of information exchanged outside Git. Those remain
review obligations and signed process claims.

## 10. Promotion boundary

A complete incubation package may be proposed for public work only when:

1. the object lock is valid;
2. the preregistration is frozen and adequate;
3. the construction result is exact;
4. the blind breaker is frozen or has returned the bounded underspecified STOP;
5. all negative results are retained;
6. the promotion map is single-valued and collision-free;
7. licence and public-safety review pass.

Promotion occurs only through a new public claim and the procedure in
`POLICY.md` and `AGENTS.md`. Files are rewritten into the public probe shape;
incubation labels do not become public statuses automatically.

## 11. Stop conditions

Stop on stale public base, unclear authority, duplicate object ownership,
ambiguous target, missing type, hidden dependency, inadequate preregistration,
premature verifier disclosure, changed pinned bytes, moved threshold, reused
breaker session, unnamed layer lift, same-architecture inflation, licence
uncertainty, or public-safety doubt.

Negative results are first-class. Incubation exists to make failure cheap,
precise, and visible before public authority is requested.
