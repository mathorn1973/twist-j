# Supplemental public audits

This directory contains public, replayable audits of selected theorem claims.
Each audit is bound permanently to one released Canon edition. It is an
auxiliary review layer, not part of the normative Canon and not a substitute
for the primary evidence in `canon/EVIDENCE.tsv`.

The binding contract is `POLICY.md`. The index schema is:

```text
audit_id	audit_kind	profile	claim_id	coverage	status_effect	canon_tag	content_commit	claim_scope_sha256	location	source_commit	source_sha256	records_sha256	hash_mode
```

- `audit_id`: unique `A-LEAN-*` identifier for a sealed audit.
- `audit_kind`: `LEAN4`.
- `profile`: `LEAN4-RECORDED-V1`; its meaning is frozen for old bundles.
- `claim_id`: a `T` or `T-LOCK` claim at the pinned release.
- `coverage`: `EXACT` or `PARTIAL`.
- `status_effect`: always `NONE`.
- `canon_tag`, `content_commit`: real released Canon edition.
- `claim_scope_sha256`: SHA-256 of its exact registry scope cell.
- `location`: exactly `audits/lean/<audit_id>`.
- `source_commit`: real pre-run source commit in the pull-request ancestry.
- `source_sha256`: digest of the immutable source files.
- `records_sha256`: digest of the four post-run record files.
- `hash_mode`: `lean-audit-source-sha256-v1`.

The checker reads the tagged `STATUS.md` and registry from Git. A later Canon
release does not make the old audit stale: the audit continues to mean exactly
what it meant at its named release. A new formulation needs a new audit ID.
The result is a publicly recorded pass, not a CI replay or status promotion.

## Package

```text
audits/lean/A-LEAN-NAME/
    README.md
    COVERAGE.tsv
    DEPENDENCIES.tsv
    AXIOMS.tsv
    EXPECTED.txt
    RUN.md
    RESULT.md
    Audit.lean
    lean-toolchain
    lakefile.toml
    lake-manifest.json
    MATHLIB-MANIFEST.json
```

The first profile permits no nested source tree. `Audit.lean` is the exact
entrypoint and must locally declare every mapped theorem and execute
one top-level exact `#print axioms` for it. Custom syntax, attributes, macros,
elaborators, syntax quotations, namespaces, and other run/output commands are
outside this frozen profile.

## Hashes

Both digest modes use case-sensitive repository-relative POSIX paths. For each
file they emit

```text
<file-sha256><two spaces><repository-relative-path><newline>
```

in sorted order, then SHA-256 the concatenated UTF-8 manifest.

`source_sha256` covers every package file except `AXIOMS.tsv`,
`EXPECTED.txt`, `RUN.md`, and `RESULT.md`. It is recomputed both from the
named Git source commit and from the current tree; the four record files must
not yet exist at the source commit.

`records_sha256` covers exactly those four post-run record files. Existing
index rows and packages are immutable, so neither digest can be silently
replaced later.

## Scope and dependencies

`COVERAGE.tsv`:

```text
claim_id	theorem_name	covered_statement	unformalized_scope
```

For `EXACT`, every `unformalized_scope` is `NONE`. For `PARTIAL`, at
least one row names a real exclusion. Human review owns the semantic bridge
between Canon prose and the Lean statement.

`DEPENDENCIES.tsv`:

```text
name	source	revision	license
```

It exactly covers `lake-manifest.json`, using public GitHub HTTPS sources, full
commit SHAs, and an approved SPDX licence. The manifest uses schema `1.2.0`;
every resolved revision is a full commit SHA, and the direct Mathlib
`inputRev` is either `null` or that same SHA. `lakefile.toml` uses the
restricted declarative profile; the first trust profile permits only the
official Mathlib repository as a direct dependency and pins it by the same
full SHA.

`MATHLIB-MANIFEST.json` is the byte-exact `lake-manifest.json` from that
pinned Mathlib commit. The checker requires the root manifest's inherited
closure to match this snapshot, except that inherited entries have Lake's
`inherited` bit set. The package README's single `## Upstream closure` value is
the corresponding public GitHub blob URL. CI does not fetch that URL; the
independent reviewer verifies the snapshot bytes against it before merge.

`AXIOMS.tsv`:

```text
theorem_name	axioms
```

The value is `NONE` or a sorted semicolon-separated subset of the accepted
kernel-axiom allowlist: `Classical.choice`, `Quot.sound`, and `propext`. Every
row must match the parsed `#print axioms` line in captured stdout.

## Run records

`RUN.md` contains only these structured `key: value` fields:

```text
source_commit: <40 lowercase hex>
source_sha256: <64 lowercase hex>
working_directory: audits/lean/A-LEAN-NAME
command: lake env lean Audit.lean
exit_code: 0
stdout_sha256: <SHA-256 of EXPECTED.txt>
stdout_bytes: <exact byte count>
stderr_bytes: 0
platform: <neutral public description>
architecture: <neutral public description>
lean_version: <exact numeric version>
lake_version: <exact version>
clean_before: true
clean_after: true
fresh_clone: true
lake_state_before_fetch: absent
dependency_checkouts_verified: true
network: disabled
secrets: none
```

`RESULT.md` contains exactly:

```text
audit_id: A-LEAN-NAME
result: RECORDED_PASS
claim_effect: NONE
```

Extra prose is rejected. An unsuccessful attempt is not entered in the audit
index and has no scientific status effect.

Before merge, a reviewer other than the author must publicly verify the
upstream snapshot, replay the command from a separate fresh clone after
checking every dependency revision, disable network for the formal command,
use an environment containing no secrets, and accept the prose-to-Lean
translation. Repository CI checks the record but does not establish kernel
acceptance.

## Withdrawal and supersession

Index rows and packages never change. If later review finds the translation
wrong or a better audit replaces it, append one row to `audits/EVENTS.tsv`:

```text
event_id	event_sequence	audit_id	event_type	event_date	reason	replacement_audit_id
```

`event_type` is `WITHDRAWN` or `SUPERSEDED`. Withdrawal uses `-` as the
replacement; supersession names an unqualified existing audit of the same
claim and pinned scope, with equal or stronger coverage. A withdrawn or already
superseded audit cannot be a replacement at that event. A replacement may be
qualified later by a subsequent row; explicit consecutive sequence numbers,
nondecreasing non-future dates, and an acyclic supersession graph preserve the
temporal record. The checker blocks `EXACT` to `PARTIAL`; a reviewer decides
whether `PARTIAL` to `PARTIAL` is semantically no weaker. The reason is public,
and the event changes no Canon claim, status, or primary evidence. One event is added in its own
pull request as one non-merge commit changing only `audits/EVENTS.tsv`; old
events are immutable.

## Procedure

1. Check the index, issues, branches, and target claim for a collision; claim
   one `A-LEAN-*` identifier in a public issue.
2. Create `audit/lean/A-LEAN-NAME` from current public `main`.
3. Commit and push the complete source package before the first recorded run.
   It and its direct record child are the branch's only two commits; neither
   may be a merge commit. Do not amend or force-push that source pin. A later
   unrelated `main` commit is allowed when the original branch base remains
   its ancestor.
4. In a fresh isolated clone, verify absent `.lake` state, materialize the
   pinned closure, check every dependency revision and clean tree, then disable
   network. With no secrets present, change to the package directory and run
   `lake env lean Audit.lean`. Never run `lake update` as the recorded command.
5. After a clean pass, add the four records and one index row.
6. Open one pull request changing only that package and the index.
7. Merge without squash or rebase. Any correction receives a new audit ID.

Repository CI checks structure, pins, hashes, and immutability only. It does
not install or execute Lean.
