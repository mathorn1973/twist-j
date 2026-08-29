# TWIST-J Repository Policy

Simplicity is the ultimate perfection. Every file must earn its place.

## 1. Authority

`STATUS.md` declares the operational authority. Until cutover this repository
is policy-only and `mathorn1973/twistj-jam` remains the internal source of
truth. After cutover, public `main` is the single source of truth and
`canon/CANON.md` is the current scientific Canon.

The first public release starts a new normative series at **Public Canon v1**.
Internal development numbers are not inherited and have no authority in the
public series. They may be named once in a cutover audit, but not carried as
the public version sequence.

If an internal extraction is informally called "Canon v1", that name has no
public authority. It is only the synthesis surface and may be named once in
the reconciliation audit. The normative v1 is exclusively **Public Canon
v1** in this repository. The internal extraction is intentionally not a valid
public Canon bundle and must not be copied around the public checks.

Throughout `GENESIS`, `https://twistj.com/canon/` continues to serve the
legacy line and must not be repointed or cited as the Public Canon v1 landing
page. Repointing is an activation action.

Claim status is rigid:

```text
T-LOCK > T > D > C > H > O > F
```

No summary may exceed the status or scope of its source.

The public registry has one exact schema:

```text
claim_id	status	scope	canon_section	evidence	falsifier
```

`claim_id` is stable and unique. `status` is one of the seven public statuses
above. Definitions and remarks are not registered claims. Internal `T-cand`,
`LOCK`, `F-LOCK`, `R`, and `Def` labels are not copied mechanically;
the Canon v1 synthesis must omit or explicitly reconcile them without
promotion.

## 2. Layout

Directories are created only when they receive real content.

```text
canon/       current Canon, core, frontier, registry, changelog
probes/      one permanent directory per named public probe
reproduce/   minimal independent reproductions that earn their place
data/        small exact inputs, fixtures, derived tables, manifests
notes/       explicitly non-canonical exploration
tools/       repository and Canon checks
legacy/      optional concise cutover audit, never a development archive
```

No generic work, scratch, output, temporary, backup, or historical dump
directory is tracked.

## 3. One probe, one branch

This section governs formal public work after cutover. During `GENESIS`, no
formal public probe starts before Public Canon v1 is active.

Each formal attack has:

```text
branch: probe/P-NAME
path:   probes/P-NAME/
owner:  one named session or person
```

Before the first formal gate execution, commit and push:

```text
PREREG.md     equation, code, carrier or data, systematics, failure threshold,
              action layer L1 to L6
verify.py     accepted exact verifier
```

Record the preregistration commit and file SHA-256. Compilation and static
checks are allowed before the pin. Formal gates are not.

After execution add:

```text
EXPECTED.txt  exact scientific stdout
RUN.md        pin, command, environment, exit code, byte counts, hashes
RESULT.md     status, scope, fired falsifiers, conclusion
```

Do not reuse, rename, or resume a sealed probe.

### Abandoned pins

A preregistration that was frozen and whose formal gate never **completed** is
an **abandoned pin**. It is an open public obligation, not a neutral leftover:
the identifier is already spent, and this policy forbids reusing, renaming or
resuming it. Leaving it open is not a disposition.

Never completed covers two cases, and the test is the record, not the
intention. The gate may never have been started. It may also have been started
and failed to produce one: a run that exits nonzero, or dies on a fixture
defect, yields no exact stdout to pin and no scientific conclusion, so no
`EXPECTED.txt` and no `RUN.md` exist to commit. Both close the same way.

An abandoned pin is closed by an explicit record, merged like any other:

```text
probes/P-NAME/
    PREREG.md     the frozen pin, unchanged
    verify.py     the accepted verifier, unchanged
    RESULT.md     Status: ABANDONED
                  why the gate never ran, and the sentence that the
                  identifier is consumed and must not be reused
```

The record carries no `EXPECTED.txt` and no `RUN.md`, because no completed run
produced either. That absence is what separates the two routes: a gate that
completed produces an exact stdout and a run record, and a probe holding them
is closed by its result, never by abandonment. A fired falsifier is merged,
not relabelled. `check_policy.py` enforces both directions.

Where a successor probe exists, it names the abandoned predecessor and the
reason in its own preregistration, before its own pin.

If the content is worth keeping, it is retargeted under a **new** identifier
with its own new pin. Retargeting does not release the old identifier, which
still requires its own abandonment record.

## 4. Evidence

Public Canon v1 is a clean synthesis, not a copy of the internal ledger.
Development history is not evidence and need not migrate.

A retained public claim must have at least one of:

- a self-contained exact proof or derivation in the Canon;
- a minimal public reproduction sufficient to audit a computational claim;
- a clearly named external dataset or source manifest where experiment is
  part of the claim.

A minimal reproduction has the stable layout:

```text
reproduce/NAME/
    verify.py
    EXPECTED.txt
    README.md
```

It uses the Python standard library, exits zero, writes no stderr, and must
match `EXPECTED.txt` byte for byte in every required architecture job.

Before cutover, a reconciliation audit maps every public claim to an internal
claim of equal or stronger status and scope. The audit forbids promotion by
rewriting. It is review material, not part of the normative Canon, and may be
kept as a concise release asset or under `legacy/`. Missing support lowers or
omits a claim; it is never invented.

For new public probes:

- Assertions use exact arithmetic. Floating point may appear only as a labeled
  engineering or measured witness.
- The author commits one exact `EXPECTED.txt` and records the local run in
  `RUN.md` using neutral public descriptors, for example
  `platform: Ubuntu 24.04` and `architecture: aarch64`. Machine nicknames are
  forbidden.
- The required pull-request workflow runs the same PR head on clean GitHub-hosted
  x86_64 `ubuntu-latest` and aarch64 `ubuntu-24.04-arm` jobs with Python 3.12.
  Both jobs require the same verifier hash, exit code 0, empty stderr, and
  stdout byte-identical to the same committed `EXPECTED.txt`.
- The stable required context `check` is an aggregate job that depends on both
  architecture jobs. It cannot pass when either architecture job fails or is
  skipped on a pull request.
- The two-architecture computation gate is satisfied by byte-identical stdout
  on two different architectures. The workflow satisfies it alone, because its
  two required jobs are x86_64 and aarch64. A recorded local run on an
  architecture that differs from a passing workflow job also satisfies it: the
  gate rests on byte identity against the one committed `EXPECTED.txt`, which
  any reader can recheck, not on the platform declaration, which is audit
  metadata. Same-architecture agreement is reproduction, not a gate.
- An independent proof may earn `T`; its verifier is then an audit.
- A one-architecture finite result is at most `C` unless its proof is
  independently theorem-grade.
- A post-cutover pull request changes at most one probe directory. The initial
  Canon v1 synthesis is not a probe pull request and imports no historical
  probe tree.
- Fired falsifiers are preserved and folded. Thresholds never move after the
  preregistration pin.
- Any lift between L1 state, L2 manifold, L3 boundary, L4 support, L5 stream,
  and L6 measure requires its own named cross-layer gate.
- Gate enforcement is explicit rather than inferred only from dependency-layer
  coincidence. Every `GATES.tsv` row uses one closed `gate_kind`; that kind
  fixes the required semantic type and public status of its owner. Cross-layer
  kinds must have distinct concrete L1 to L6 endpoints. If such an owner has
  one concrete L1 to L6 layer, it must equal the gate `to_layer`; `MULTI` and
  `NOT_APPLICABLE` do not disable this owner contract. Separately, every
  dependency edge that actually crosses two concrete protocol layers still
  requires a matching gate with those exact endpoints.
- A decision that remains entirely within one concrete protocol layer may use
  `OPEN_DECISION`. It is a decision gate, not a lift: `from_layer` and
  `to_layer` must be the same concrete L1 to L6 layer, the owner must be an
  open obligation at that same concrete layer, and `MULTI` or
  `NOT_APPLICABLE` may not be used to evade the placement. Other gate kinds
  may not use equal endpoints.

### Reading-family discipline

Public work does not presume global decoder uniqueness.

Nonuniqueness is a scientific falsifier only when the frozen claim being
tested explicitly asserts uniqueness in a declared class and equivalence
relation.

A proposed family of physical readings must freeze the domain, codomain,
context keys, equality or equivalence relation, and overlap rules needed by
its claim. If two admitted readings in the same context produce inequivalent
physical outputs, the work must provide an independent selection or occurrence
rule, prove the readings physically equivalent at the claimed scope, or leave
the physical conclusion open.

A reading may never be selected after inspection of the target measurement or
result it is used to explain.

Completeness of a reading family does not mean cardinality one. It means that
all admitted alternatives relevant to the claimed outputs are classified and
that no undeclared choice remains.

## 5. Canon

The current files have stable paths:

```text
canon/CORE.md       short stable core
canon/CANON.md      complete current Canon
canon/FRONTIER.md   live open obligations only
canon/REGISTRY.tsv  machine-readable claim registry
canon/CHANGELOG.md  delta within the public series
canon/SHA256SUMS     hashes of the five normative files above
```

Public Canon v1 is newly authored from the latest sealed internal state. It is
organized by subject, may rewrite and compress inherited material, and need
not be byte-identical to any internal Canon. It contains present truth once.

The normative Canon excludes:

- internal version chronology and fold narratives;
- commit and machine ledgers;
- failed-run diaries and amendment stories;
- repeated carried-forward summaries;
- superseded formulations and closed work queues;
- historical verifiers that are not needed for a minimal public audit.

Internal numbering is retired at cutover. Public versions use immutable tags
and releases `canon-v1`, `canon-v2`, and so on. Each release carries
`SHA256SUMS`. Public history starts at v1; earlier development remains outside
the normative series. Canon version numbers are positive whole numbers only;
decimal Canon versions are not used. A decimal `cff-version` identifies the
CFF schema, not the Canon.

Incomplete work belongs under `notes/`, is marked `NON-CANONICAL`, and need
not carry a verifier. A proposed Canon patch stays under `notes/canon/` until
a separate sealed public fold applies it to `canon/CANON.md`.

## 6. Git

- `main` accepts reviewed pull requests only, except repository genesis.
- The initial synthesis uses the dedicated branch `synthesis/canon-v1`. Its
  reviewed pull request adds the Canon bundle, small data, minimal
  reproductions, citation material, and the reconciliation audit. It does not
  import historical probe directories or the old repository history.
- Cutover is two-phase. The synthesis pull request leaves `STATE: GENESIS`,
  keeps the legacy website pointer unchanged, and records the Canon as a
  candidate. Its `CITATION.cff` must not use the legacy Canon URL as the
  Public Canon v1 landing page. After it merges, a separate
  `activate/canon-v1` pull request sets `STATE: ACTIVE`, names the immutable
  Canon content commit, exact hash and byte count, and updates the README.
- The activation request records the immutable synthesis merge as
  `CONTENT_COMMIT`. The `canon-v1` tag and release are created from the merged
  activation commit; that tag target is recorded as `ACTIVATION_COMMIT` in the
  release manifest. Authority moves only after public readback and all
  required checks.
- Probe commits are never rebased, squashed, amended, or force-pushed after the
  preregistration pin. Merge commits preserve provenance.
- Check for an existing branch, issue, probe, object lock, and claim lock before
  claiming work.
- Stage named files only. Never add all files blindly.

## 7. Public safety

Never commit secrets, credentials, `.env` files, private addresses or hostnames,
private logs, personal data, binary models, compiled objects, or unreviewed
third-party material. Files over 5 MiB require an explicit policy change.
External or large data use a manifest with source, version, license, and hash.

Every pull request must pass the required `check`, which aggregates the x86_64
and aarch64 architecture jobs, plus manual security review.
Apache-2.0 applies unless a file states an approved compatible license.

After cutover, the release-form activation readback is not a general content
gate. Pull requests and ordinary `main` pushes run the two architecture jobs
and their aggregate `check`. Immutable tag pushes and release publication run
a separate single x86_64 publication job. This prevents duplicate artifact
uploads and release races while preserving full publication readback.

A pull request that changes any file under `canon/` widens both changed-path
checks to every public probe and every minimal reproduction, in every
architecture job, because a verifier may read `canon/` at run time while its own
directory is untouched, and a changed-path check cannot see that. The
one-probe-per-pull-request rule is unaffected: it still counts only the probe
directories the diff names.

The publication job reruns policy, unit, Canon, ledger and explicit gate
contract checks, then performs the activation readback. Tag and release events
skip changed-path checks because those events do not supply a valid comparison
base; their full activation readback already reproduces every public probe and
minimal reproduction.

When release immutability is enabled, a release is always assembled as a
draft. Attach the successful tag-job `activation-manifest.json` and the tagged
`canon/SHA256SUMS`, validate both downloads, and only then publish the draft.
Never substitute a manifest generated from a local checkout.

The sole workflow has read-only permissions, immutable action pins, no
persisted checkout credential, a 25-minute architecture limit, a 30-minute
publication limit, and a 5-minute aggregate limit. Its pull-request gate uses
one x86_64 and one
aarch64 standard GitHub-hosted runner. Its tag trigger covers `canon-v*`, but
the activation and release validators require the triggering event tag to equal
the positive whole-number tag declared by the current `STATUS.md`; a broader,
decimal, or foreign tag therefore triggers a failing readback, never
publication.

`pull_request_target` is forbidden. Any new workflow or runner topology requires
an explicit policy change.
