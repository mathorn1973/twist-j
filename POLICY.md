# TWIST-J Repository Policy

Simplicity is the ultimate perfection. Every file must earn its place.

## 1. Authority

`STATUS.md` declares the operational authority. After cutover, `main` is the
single source of truth and `canon/CANON.md` is the current scientific Canon.
Until then, this repository is policy-only.

Claim status is rigid:

```text
T-LOCK > T > D > C > H > O > F
```

No summary may exceed the status or scope of its source.

## 2. Layout

Directories are created only when they receive real content.

```text
canon/       current Canon, core, frontier, registry, changelog
probes/      one permanent directory per named probe
reproduce/   short independent reproductions
data/        small exact inputs, fixtures, derived tables, manifests
notes/       explicitly non-canonical exploration
tools/       repository and Canon checks
legacy/      curated provenance imported at cutover
```

No generic work, scratch, output, temporary, or backup directory is tracked.

## 3. One probe, one branch

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

- Assertions use exact arithmetic. Floating point may appear only as a labeled
  engineering or measured witness.
- The author runs the pinned verifier locally and records `RUN.md` and the
  exact stdout in `EXPECTED.txt`.
- The required GitHub check reruns every changed verifier on a clean
  `ubuntu-latest` runner and requires the same verifier hash, exit code 0,
  empty stderr, and byte-identical stdout.
- A verifier-backed contribution is reproducible only when both the local
  record and the GitHub check pass.
- For a computation-only promotion to `T`, the local and GitHub runs must also
  use different architectures. Same-architecture agreement is a reproduction,
  not a two-architecture gate. An independent proof may earn `T`; its verifier
  is then an audit.
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
canon/CHANGELOG.md  delta from the previous release
```

Old versions live in immutable tags and releases named `canon-vNNN`, not as
copies on `main`. Each release carries `SHA256SUMS`. Present truth appears once;
history and run detail are referenced, not repeated.

Incomplete work belongs under `notes/`, is marked `NON-CANONICAL`, and need
not carry a verifier. A proposed Canon patch stays under `notes/canon/` until
a separate sealed fold applies it to `canon/CANON.md`.

## 6. Git

- `main` accepts reviewed pull requests only, except repository genesis.
- Probe commits are never rebased, squashed, amended, or force-pushed after the
  preregistration pin. Merge commits preserve provenance.
- Check for an existing branch, issue, probe, and lock before claiming work.
- Stage named files only. Never add all files blindly.

## 7. Public safety

Never commit secrets, credentials, `.env` files, private addresses or hostnames,
private logs, personal data, binary models, compiled objects, or unreviewed
third-party material. Files over 5 MiB require an explicit policy change.
External or large data use a manifest with source, version, license, and hash.

Every pull request must pass the required `check`, which runs both repository
policy and any changed verifiers, plus a manual security review. Apache-2.0
applies unless a file states an approved compatible license.
