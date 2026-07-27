# TWIST-J non-canonical incubation

```text
STATUS:     NON-CANONICAL
AUTHORITY:  NONE
PURPOSE:    exact candidate development, independent breaking, and PROMO handoff
```

This directory is not Canon, a public probe, evidence, or a status ledger.
Nothing here changes `canon/`, closes a frontier row, or earns public authority.
`AGENTS.md` and `POLICY.md` govern all work.

## 1. Line split

The current division is:

```text
PUBLIC_AGENT    ChatGPT
INTERNAL_AGENT  Claude
```

The public agent owns GitHub claims, public branches, formal probes, folds, and
pull requests. The internal agent owns authority-free incubation and adversarial
breaking. The former private repository remains read-only history under public
policy.

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

Example:

```text
C-FOO-BAR-1
```

The example does not authorize an inferred public name.

## 3. Atomic claim before files

Before creating a candidate directory:

1. choose one exact `CLAIM_KEY`;
2. create one GitHub issue already assigned in the same server-side operation;
3. record a unique non-secret `OWNER_SESSION` in the issue body;
4. read the issue back;
5. create no branch or commit before that readback.

For concurrent issues with the same exact `CLAIM_KEY`, the lowest issue number
is the sole winner. Every higher-numbered issue stops and closes as duplicate
before committing. This rule also distinguishes sessions that share one GitHub
account.

The issue owns one candidate. Reviewers and breakers do not acquire a competing
build lock.

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

Records:

```text
incubation_id
claim_key
claim_issue
owner_session
target_line: INTERNAL-INCUBATION
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
must be able to tell what would falsify the claim without reading `verify.py`.

### `verify.py`

Agent A's exact construction route. Standard library only. Integers and exact
rational arithmetic first. Scientific stdout follows the portability rules in
`AGENTS.md`.

### `break.py`

Agent B's independent attack, written only from the frozen `PREREG.md` and its
explicitly named public dependencies. It must not import, invoke, wrap, copy,
or inspect `verify.py` before its own freeze.

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

Agent A freezes `PREREG.md` and writes `verify.py`.

Agent B receives only:

- the exact frozen `PREREG.md`;
- public dependencies explicitly named there;
- no verifier bytes, verifier diff, expected output, implementation hint, or
  private explanation.

B writes and freezes `break.py` before any comparison with A's implementation.
The breaker must use an independent representation, derivation, enumeration,
invariant, or code path.

If B cannot construct a well-typed attack from the preregistration alone, B
does not inspect `verify.py`. B records in `RESULT.md`:

```text
BLIND-BREAKER-UNDERSPECIFIED / STOP
```

This falsifies the adequacy of the preregistration for blind confirmation. A
new attempt requires a new preregistration freeze and a new breaker freeze.
The missing information may not be supplied privately after the pin.

If B merely runs or translates A's verifier, the result is reproduction. It is
never independent confirmation.

After both routes are frozen, compare exact domains, equality, thresholds,
outputs, and falsifiers. Disagreement is a first-class result. Never repair a
candidate by moving a threshold or changing the claim after opening either
result.

## 6. Computation topology

The automatic GitHub pull-request check is the x86_64 leg. The designated
internal-side runner supplies the aarch64 leg before merge, using neutral fields
only:

```text
platform: Ubuntu 24.04
architecture: aarch64
```

No machine nickname enters public records. `EXPECTED.txt` contains exact
stdout for a promoted formal probe. `RUN.md` contains the aarch64 candidate pin,
verifier SHA-256, stdout SHA-256, byte counts, exit code, Python version, and
neutral platform fields.

A local ChatGPT run is x86_64 and contributes no second architecture. Without a
genuine aarch64 record, a computation-only result is at most `C` after public
fold, regardless of how many x86_64 reruns agree.

Incubation reruns are evidence for development only. Public computation status
is earned solely by the public probe procedure.

## 7. Portable verifier output

The construction and breaker must remain byte-stable across the supported
Python 3.12 and 3.13 lanes.

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
target_issue: 181
target_branch: probe/P-FOO-1
target_probe_id: P-FOO-1
target_claim_id: FOO-BAR
```

A target may be `NONE`. A field may not contain alternatives, wildcards,
fallbacks, or prose choices.

Before any public branch is created, the public agent searches:

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

## 9. Promotion boundary

A complete incubation package may be proposed for public work only when:

1. the issue lock is valid;
2. the preregistration is frozen and adequate;
3. the construction result is exact;
4. the blind breaker is frozen or has returned the underspecified STOP;
5. all negative results are retained;
6. the promotion map is single-valued and collision-free;
7. licence and public-safety review pass.

Promotion occurs only through a new public claim and the procedure in
`POLICY.md` and `AGENTS.md`. Files are rewritten into the public probe shape;
incubation labels do not become public statuses automatically.

## 10. Stop conditions

Stop on stale public base, unclear authority, duplicate claim ownership,
ambiguous target, missing type, hidden dependency, inadequate preregistration,
premature verifier disclosure, changed pinned bytes, moved threshold, reused
breaker, unnamed layer lift, same-architecture inflation, licence uncertainty,
or public-safety doubt.

Negative results are first-class. Incubation exists to make failure cheap,
precise, and visible before public authority is requested.
