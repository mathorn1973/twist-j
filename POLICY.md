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
EXPECTED.txt  exact local stdout
RUN.md        pin, command, environment, exit code, byte counts, hashes
RESULT.md     status, scope, fired falsifiers, conclusion
```

Do not reuse, rename, or resume a sealed probe.

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
match `EXPECTED.txt` byte for byte in the required GitHub check.

Before cutover, a reconciliation audit maps every public claim to an internal
claim of equal or stronger status and scope. The audit forbids promotion by
rewriting. It is review material, not part of the normative Canon, and may be
kept as a concise release asset or under `legacy/`. Missing support lowers or
omits a claim; it is never invented.

For new public probes:

- Assertions use exact arithmetic. Floating point may appear only as a labeled
  engineering or measured witness.
- The author runs the pinned verifier locally and records `RUN.md` and the
  exact stdout in `EXPECTED.txt`.
- The required GitHub check reruns every changed verifier on a clean
  `ubuntu-latest` runner and requires the same verifier hash, exit code 0,
  empty stderr, and byte-identical stdout.
- A verifier-backed contribution is reproducible only when both the local
  record and the GitHub check pass.
- A post-cutover pull request changes at most one probe directory. The initial
  Canon v1 synthesis is not a probe pull request and imports no historical
  probe tree.
- For a computation-only promotion to `T`, the local and GitHub runs must also
  use different architectures. Same-architecture agreement is a reproduction,
  not a two-architecture gate. An independent proof may earn `T`; its
  verifier is then an audit.
- A one-architecture finite result is at most `C` unless its proof is
  independently theorem-grade.
- Fired falsifiers are preserved and folded. Thresholds never move after the
  preregistration pin.
- Any lift between L1 state, L2 manifold, L3 boundary, L4 support, L5 stream,
  and L6 measure requires its own named gate.

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
the normative series.

Incomplete work belongs under `notes/`, is marked `NON-CANONICAL`, and need
not carry a verifier. A proposed Canon patch stays under `notes/canon/` until
a separate sealed public fold applies it to `canon/CANON.md`.

## 6. Git

- `main` accepts reviewed pull requests only, except repository genesis.
- The initial synthesis uses the dedicated branch `synthesis/canon-v1`. Its
  reviewed pull request adds the Canon bundle, small data, minimal
  reproductions, citation material, and the reconciliation audit. It does not
  import historical probe directories or the old repository history.
- Cutover is two-phase. The synthesis pull request leaves `STATE: GENESIS`
  and records the Canon as a candidate. After it merges, a separate
  `activate/canon-v1` pull request sets `STATE: ACTIVE`, names the immutable
  Canon content commit, exact hash and byte count, and updates the README.
- The `canon-v1` tag and release are created from the merged activation
  commit. Authority moves only after public readback and all required checks.
- Probe commits are never rebased, squashed, amended, or force-pushed after the
  preregistration pin. Merge commits preserve provenance.
- Check for an existing branch, issue, probe, and lock before claiming work.
- Stage named files only. Never add all files blindly.

## 7. Public safety

Never commit secrets, credentials, `.env` files, private addresses or hostnames,
private logs, personal data, binary models, compiled objects, or unreviewed
third-party material. Files over 5 MiB require an explicit policy change.
External or large data use a manifest with source, version, license, and hash.

Every pull request must pass the required `check`, which runs repository
policy and any changed public verifiers, plus a manual security review.
Apache-2.0 applies unless a file states an approved compatible license.

The sole workflow has read-only permissions, immutable action pins, no
persisted checkout credential, and a 15-minute timeout.
`pull_request_target` is forbidden. Any new workflow requires an explicit
policy change.
