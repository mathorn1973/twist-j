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
Public `main` is the scientific authority. The former private repository is
read-only development history under `POLICY.md`.

## 2. Agent roles and the only handoff

The current role assignment is:

```text
PUBLIC_AGENT    ChatGPT
INTERNAL_AGENT  Claude
```

`PUBLIC_AGENT` owns work on `mathorn1973/twist-j`: issue claims, branches,
public review, probes, folds, and pull requests.

`INTERNAL_AGENT` may incubate and break candidates without authority. It does
not supply public currency from a private workspace. A candidate reaches the
public line only as a Git commit carrying an explicit `PROMO.md` package under
the rules in `notes/incubation/README.md`.

Git is the only shared filesystem, queue, and handoff surface. Chat summaries
are informational only. Changing this role assignment requires a reviewed pull
request to this file.

## 3. Atomic claim lock

Every public probe, incubation candidate, policy change, or scoped note has one
exact `CLAIM_KEY` and one public GitHub issue.

Acquire the lock by creating the issue already assigned in the same server-side
operation. The issue body records:

```text
CLAIM_KEY:     stable exact key
OWNER_SESSION: unique non-secret session token
```

No branch or commit may predate that assigned issue.

Concurrent duplicate creation is resolved deterministically. Among issues with
the same exact `CLAIM_KEY`, the lowest issue number is the sole owner. Every
higher-numbered duplicate stops and closes as duplicate before committing.
Assignment identifies the public account. `OWNER_SESSION` distinguishes
concurrent sessions that use the same account.

One issue owns one scoped item. A second session may review or break it, but may
not build a competing candidate under the same key.

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

## 5. Computation legs

The public computation gate has two fixed architecture roles:

```text
x86_64    the required GitHub pull-request check, automatic

aarch64   the designated internal-side architecture runner, supplied before
          merge with neutral public fields only
```

The public workflow currently runs `ubuntu-latest` with Python 3.12 and is the
x86_64 leg. A local ChatGPT execution is also x86_64. It is therefore zero new
architecture legs: useful as a dry run or reproduction, but never sufficient
for computation-grade `T`.

The aarch64 record uses neutral fields only, for example:

```text
platform: Ubuntu 24.04
architecture: aarch64
```

Never record a machine nickname. `EXPECTED.txt` carries the exact stdout.
`RUN.md` carries the candidate pin, verifier hash, stdout SHA-256, byte counts,
exit code, Python version, platform, and architecture. The aarch64 record must
land in the probe branch before merge. Without it, a computation-only result
stays at most `C`.

If the public workflow is changed to provide a genuine aarch64 job, this role
assignment must be reviewed against the actual workflow before use.

## 6. Verifier portability

Public verifiers use the Python standard library and exact arithmetic. They
must produce byte-identical scientific stdout on the supported Python 3.12 and
3.13 lanes.

Verifier stdout contains only explicitly formatted integers, signs, finite
strings, and rational numbers. Format a rational as `numerator/denominator`,
with denominator one printed as an integer.

Do not print or depend on:

- exception text or traceback wording;
- `repr` of objects, containers, sets, or dictionaries;
- unsorted iteration order;
- `sys.version`, platform strings, paths, hostnames, locale, timezone, or wall
  clock values;
- randomized hash order;
- library-specific floating-point formatting.

Platform and Python metadata belong in `RUN.md`, not scientific stdout. A
failure prints one stable project-defined message and exits nonzero.

## 7. Blind breaker

Blind confirmation separates construction from attack.

Agent A freezes the complete `PREREG.md` before formal computation and writes
`verify.py`. Agent B receives only the frozen preregistration and the public
dependencies explicitly named by it. Agent B must not read `verify.py`, its
commit diff, its output, or an implementation-derived hint before freezing the
independent attack.

Agent B writes `break.py` from the preregistration alone and freezes it before
comparison. The attack must use an independently stated route, representation,
enumeration, derivation, or invariant. Merely invoking, importing, wrapping, or
reimplementing the control flow of `verify.py` is reproduction, not independent
confirmation.

If the preregistration does not contain enough typed information to construct
an independent attack without reading `verify.py`, B records:

```text
BLIND-BREAKER-UNDERSPECIFIED / STOP
```

That result is a defect in the preregistration. It does not authorize B to read
`verify.py`, guess the intended claim, or weaken the attack. The candidate may
be revised only by a new freeze and a new breaker attempt.

After both programs are frozen, compare claims, domains, thresholds, outputs,
and fired falsifiers. Running A's verifier on a second machine is reproduction
only. Independent confirmation requires the frozen B route.

## 8. Promotion and naming

Never infer a public target name by deleting a prefix or copying an internal
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
collision, or mismatch between content and target is `PROMO-NAME-COLLISION /
STOP`. Resolution requires a new owner ruling before a public branch is
created.

Examples such as `C-FOO-BAR-1` to `FOO-BAR` are illustrations only. They are
never an implicit renaming rule.

## 9. Pull requests and safety

Stage named files only. A pull request changes only the declared scope. Run the
repository policy, unit, Canon, ledger, verifier, and reproduction checks that
apply. Perform the manual security and licence review. Preserve fired
falsifiers. Merge without squash or rebase when the repository procedure
requires provenance.

Do not add or loosen workflows without an explicit policy change. Never commit
secrets, credentials, private infrastructure, personal data, raw private logs,
binaries, models, or unreviewed third-party material.

Commit as exactly:

```text
A. M. Thorn <thorn@twistj.com>
```

## 10. Stop conditions

Stop without guessing on unclear authority, stale base, failed readback,
missing support, incomplete types, ambiguous equality, issue collision,
branch collision, probe collision, naming collision, premature data access,
changed pinned bytes, moved threshold, unnamed layer lift, failed architecture
gate, verifier portability failure, licence uncertainty, or public-safety
doubt.

Simplicity is the ultimate perfection. Negative results are first-class.
