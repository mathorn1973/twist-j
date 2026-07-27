# Agent Manual

`STATUS.md` decides authority. `POLICY.md` is binding. Repository tools and
checkers define the executable rules. This file defines the current agent
contract after public activation.

## 1. Startup and authority

At the start of every session:

1. Fetch public `main`.
2. Read `STATUS.md`, `POLICY.md`, this file, `canon/CORE.md`, and
   `canon/FRONTIER.md`.
3. Confirm the declared tag and content commit are ancestors of `main`, the
   Canon hash and byte count match, and the required checks are green.
4. Read the registry, dependencies, gates, evidence, and checkers relevant to
   the scoped task.
5. Stop on stale basis, unclear authority, hash mismatch, missing evidence,
   licence uncertainty, collision, or any repository stop condition.

An attachment, mirror, chat transcript, or project snapshot is never authority.
Public `main` is the sole public scientific authority. Other work has no public
authority until it is handed off through Git and accepted by the public
procedure.

## 2. Roles and the only handoff

The stable roles are:

```text
PUBLIC_ROLE               owns public Git claims, branches, probes, and PRs
BUILDER_ROLE              constructs one scoped candidate
BREAKER_ROLE              attacks a frozen preregistration independently
ARCHITECTURE_RUNNER_ROLE  supplies one workflow architecture execution
```

Concrete products, people, machines, or sessions are assigned to roles in the
claim issue or run record. They are not permanently assigned in this manual.

Git is the only shared filesystem, queue, and handoff surface. Chat summaries
are informational only. A candidate reaches the public line only as a committed
package with an explicit `PROMO.md` under `notes/incubation/README.md`.

## 3. Object lock and claim lock

Every scoped item records three different identifiers:

```text
OBJECT_KEY:     stable target object or exact normalized new scope
CLAIM_KEY:      one proposed attack or construction on that object
OWNER_SESSION:  unique non-secret session token
```

For an existing object, `OBJECT_KEY` is its public registry, frontier, probe,
policy, or file identifier. A new object uses `NEW:<sha256>`, where the digest is
computed from the exact UTF-8, LF-terminated scope statement recorded in the
issue.

Acquire the lock by creating the issue already assigned in the same server-side
operation. No branch or commit may predate the assigned issue readback.

Among active builder issues with the same exact `OBJECT_KEY`, the lowest issue
number is the sole build owner. Every higher-numbered duplicate stops and closes
as duplicate before committing. A breaker may work against the winning issue
without acquiring a competing build lock.

Assignment identifies the public account. `OWNER_SESSION` distinguishes
concurrent sessions using the same account.

A lock never expires by time alone. Release requires an issue comment containing
exactly `LOCK_RELEASED`, followed by unassignment or closure by the current
owner session or repository owner. A successor must read that server-side
record before claiming the object.

String equality does not prove mathematical equivalence. Before claiming a new
object, search issues, branches, probes, the registry, and promotion packages
for content collisions. A suspected equivalent scope is `OBJECT-COLLISION /
STOP` until an owner ruling identifies or separates the objects.

## 4. Work classes

Formal public work follows `POLICY.md` and the repository checkers verbatim.
Use one branch and one public probe directory for one named formal attack.
Never move a threshold, reopen a fired falsifier, reuse a completed probe, or
make an unnamed lift between L1 state, L2 manifold, L3 boundary, L4 support,
L5 stream, and L6 measure.

Work outside the formal public probe protocol is `NON-CANONICAL` incubation.
Its layout, naming, blind-breaker procedure, and promotion manifest are defined
in `notes/incubation/README.md`. Incubation never edits `canon/`, never creates
a registry status, and never earns public authority by itself.

## 5. Verifier portability

Public verifiers use the Python standard library and exact arithmetic. Their
scientific stdout must be byte-identical on every architecture and supported
Python minor version exercised by the required workflow.

Verifier stdout contains only explicitly formatted integers, signs, finite
strings, and rational numbers. Format a rational as `numerator/denominator`,
with denominator one printed as an integer. Sort every collection before
output.

Do not print or depend on:

- exception text or traceback wording;
- `repr` of objects, containers, sets, or dictionaries;
- unsorted iteration order;
- `sys.version`, platform strings, paths, hostnames, locale, timezone, or wall
  clock values;
- randomized hash order;
- library-specific floating-point formatting.

Platform and Python metadata belong in run records, not scientific stdout. A
failure prints one stable project-defined message and exits nonzero.

## 6. Formal public computation gate

This section number and heading are permanent compatibility anchors. Historical
sealed records that cite `AGENTS.md section 6` refer to this section. New records
should cite the heading `Formal public computation gate` as well as the section
number.

A computation-only public `T` requires the repository's pinned workflow to run
the same PR head, verifier bytes, and `EXPECTED.txt` successfully on at least
one x86_64 job and at least one aarch64 job. Each job requires exit zero, empty
stderr, and stdout byte-identical to the same committed `EXPECTED.txt`.
Byte-identity across architectures then follows transitively.

The workflow and repository checkers define the current runner labels and
supported Python versions. Do not duplicate mutable labels here.

A local run, a manually written architecture field, or repeated execution on
one architecture is reproduction only. It contributes no architecture gate by
itself. Until both required workflow architecture jobs pass on the same PR head,
a computation-only result remains at most `C`.

`RUN.md` is an audit record, not proof of machine identity. It may record neutral
platform, architecture, Python, hashes, byte counts, and exit status. The
repository checker must reject machine nicknames and private infrastructure in
public run records.

An independent exact proof may establish `T`; its verifier is then an audit.

## 7. Blind breaker

Blind confirmation separates construction from attack.

The builder freezes the complete `PREREG.md` before formal computation and
writes `verify.py`. The breaker receives only the frozen preregistration and the
public dependencies explicitly named by it. The breaker must not read
`verify.py`, its diff, output, or an implementation-derived hint before freezing
the independent attack.

The breaker writes `break.py` from the preregistration alone and freezes it
before comparison. The attack must use an independently stated route,
representation, enumeration, derivation, or invariant. Invoking, importing,
wrapping, translating, or following the control flow of `verify.py` is
reproduction, not independent confirmation.

### Revision 1

If the preregistration is insufficient, the breaker records:

```text
BLIND-BREAKER-UNDERSPECIFIED / STOP
```

The public deficiency report names only missing types, domains, equality rules,
dependencies, thresholds, or output fields. It must not disclose an attack
strategy, candidate counterexample, or implementation hint.

### Revision 2

The builder may publish one revised preregistration under a new pin. A different
`BREAKER_SESSION`, which has not read `verify.py`, `break.py`, or private attack
reasoning from revision 1, performs the second blind attempt.

A second `BLIND-BREAKER-UNDERSPECIFIED / STOP` terminates the candidate. Further
work requires a new candidate identifier and object-lock review. There is no
third revision under the same candidate.

The repository checker can validate files, pins, declared sessions, and visible
references. It cannot prove what an agent saw outside Git. The independence
statement is therefore a signed process assertion bounded by the auditable Git
record, never a machine-proved fact.

After both routes are frozen, compare claims, domains, thresholds, outputs, and
fired falsifiers. Running the builder's verifier on another machine is
reproduction only.

## 8. Promotion and naming

Never infer a public target name by deleting a prefix or copying a development
identifier. Every incubation package carries one explicit, single-valued
promotion map in `PROMO.md`:

```text
incubation_id:
target_issue:
target_branch:
target_probe_id:
target_claim_id:
```

A field may be `NONE`, but may not contain alternatives. Before promotion,
search issues, branches, probes, the registry, and current promotion packages
for every target. Any duplicate target, multiple possible target, naming
collision, or mismatch between content and target is a terminal STOP. Resolution
requires a new owner ruling before a public branch is created.

Examples such as `C-FOO-BAR-1` to `FOO-BAR` are illustrations only. They are
never implicit renaming rules.

## 9. Machine enforcement boundary

`tools/check_incubation.py` validates the visible incubation contract, including
package shape, manifest fields, duplicate targets, forbidden alternatives,
visible premature verifier references, session declarations, and public run
record hygiene.

The checker does not prove mathematical equivalence of scopes, independence of
human knowledge, or absence of information exchanged outside Git. Those remain
explicit process claims and review obligations.

## 10. Pull requests and safety

Stage named files only. A pull request changes only the declared scope. Run the
repository policy, unit, Canon, ledger, incubation, verifier, and reproduction
checks that apply. Perform the manual security and licence review. Preserve
fired falsifiers. Merge without squash or rebase when the repository procedure
requires provenance.

Do not add or loosen workflows without an explicit policy change. Never commit
secrets, credentials, private infrastructure, personal data, raw private logs,
binaries, models, or unreviewed third-party material.

Commit as exactly:

```text
A. M. Thorn <thorn@twistj.com>
```

## 11. Stop conditions

Stop without guessing on unclear authority, stale base, failed readback,
missing support, incomplete types, ambiguous equality, object collision, issue
collision, branch collision, probe collision, naming collision, premature data
access, changed pinned bytes, moved threshold, unnamed layer lift, failed
workflow architecture gate, verifier portability failure, licence uncertainty,
or public-safety doubt.

Simplicity is the ultimate perfection. Negative results are first-class.
