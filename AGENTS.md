# Agent Manual

`POLICY.md` is binding. `STATUS.md` decides authority. This file defines the
Public Canon v1 synthesis and daily operating procedure.

## 1. Authority gate

Read `STATUS.md` before any scientific work.

- If `STATE: GENESIS`, this repository is policy-only. Do not open a formal
  public probe or treat any scientific claim here as canonical.
- If `STATE: ACTIVE`, confirm the declared public Canon tag, commit, SHA-256,
  byte count, and required checks before continuing.
- Before cutover, `mathorn1973/twistj-jam` remains the internal source of
  truth. After cutover it is read-only private development history. Public
  authority begins with Public Canon v1.
- Never infer authority from file age, an internal version number, a mirror, or
  an attached copy.

## 2. Clean-slate synthesis rule

The author selects one sealed internal state as the synthesis basis. Agents do
not assume that the latest visible internal version is the chosen basis.

Freeze the internal basis while Public Canon v1 is being written:

```text
internal version | source HEAD | lock | Canon file | SHA-256 | byte count
```

The frozen tuple is an audit input, not the public version identity. If it
changes during synthesis, stop and re-freeze.

The output is a newly authored **Public Canon v1**, not a byte-for-byte
migration. It may reorganize, rewrite, merge, and omit internal material.
Internal numbering is retired. Synthesis creates no scientific promotion:
every public claim must map to an internal claim of equal or stronger status
and at least the same scope.

## 3. What Public Canon v1 contains

### Required

1. `canon/CANON.md`: a self-contained thematic statement of current TWIST-J,
   written once and free of development chronology.
2. `canon/CORE.md`: the short stable core sufficient for orientation.
3. `canon/FRONTIER.md`: live `H` and `O` claims only.
4. `canon/REGISTRY.tsv`: every public claim with the exact columns:

   ```text
   claim_id	status	scope	canon_section	evidence	falsifier
   ```

5. `canon/CHANGELOG.md`: a Public Canon v1 genesis entry. Later entries
   describe only the public series.
6. `canon/SHA256SUMS`: SHA-256 for the five normative files above.
7. Exact proofs in the Canon or minimal public reproductions for retained
   claims that depend on computation. A reproduction has:

   ```text
   reproduce/NAME/
       verify.py
       EXPECTED.txt
       README.md
   ```

8. Definitions and live falsifiers for every retained `H` and `O` item, and
   every `F` result still needed to delimit current theory.
9. A reconciliation audit mapping each public claim to an equal-or-stronger
   internal basis claim. It is an internal review input; publishing it is
   optional and it is never part of the normative Canon.
10. `CITATION.cff`, authorship, license notices, and external-data manifests
    actually needed by the public work.

Internal `T-cand`, `LOCK`, `F-LOCK`, `R`, and `Def` labels are not
copied mechanically. Definitions and remarks are not claims. Every retained
item must be reconciled into the seven public statuses without promotion.

### Included only when necessary

- A minimal verifier whose output is essential to audit a retained
  computational claim.
- A small exact fixture whose change would alter a current conclusion.
- A negative result required to state the present boundary correctly.
- An independent reproduction that materially strengthens the public claim.

### Excluded

- Earlier complete Canons, internal fold patches, and internal numbering.
- Version-by-version histories, commit ledgers, machine ledgers, and repeated
  carried-forward summaries.
- `HANDOFF.md`, `tasks.md`, control boards, session chatter, and stale
  frontiers.
- Historical probe directories and verifier collections imported wholesale.
- Failed-run diaries and amendment narratives unless needed to delimit a live
  result.
- Storyteller, JAM training, PhiTorch product work, books, websites,
  infrastructure, monitoring, DNS, and machine administration.
- Checkpoints, models, binaries, build products, caches, raw logs, temporary
  trees, scratch files, backups, and large regenerated outputs.
- Secrets, private addresses or hostnames, credentials, personal data, and
  unreviewed third-party material.
- Superseded formulations presented as current science.
- The old repository history.

The private repository may remain as an immutable development archive. It is
not part of the public Canon series.

## 4. Public Canon v1 procedure

### Phase A: synthesis

1. Confirm that no internal source probe is active and the chosen internal
   basis is sealed.
2. Record and freeze the internal basis tuple.
3. Define the public v1 scope and thematic outline before rewriting.
4. Create `synthesis/canon-v1`; do not mix synthesis with new science.
5. Write `canon/CANON.md` as a clean current statement, not as a history.
6. Derive `CORE.md`, `FRONTIER.md`, `REGISTRY.tsv`, `CHANGELOG.md`, and
   `SHA256SUMS` from the new Canon.
7. Build the internal reconciliation audit. Every public claim must map to an
   internal claim of equal or stronger status. Missing support lowers or
   removes the public claim.
8. Add only minimal reproductions, exact fixtures, `CITATION.cff`, and data
   manifests required by the public text.
9. Set `STATUS.md` to `STATE: GENESIS` and
   `CANON: Public Canon v1 candidate`. Authority remains internal.
10. Audit every included file for status, scope, secrets, private
    infrastructure, license, size, duplication, and obsolete wording.
11. Run `check_policy.py`, `check_canon.py`, `check_reproduce.py`, and
    every included scientific check.
12. Open one reviewed synthesis pull request. It states the scope,
    intentional omissions, lowered claims, audit result, and public hashes.
    The internal Canon and development history are not imported.
13. Merge with a merge commit. Record that merge commit as the immutable Canon
    content commit. The repository is still `GENESIS`.

### Phase B: activation

14. Create `activate/canon-v1` from the merged public `main`.
15. Update `STATUS.md` to the exact active form:

    ```text
    STATE:          ACTIVE
    CANON:          Public Canon v1
    AUTHORITY:      mathorn1973/twist-j main
    CUTOVER:        YYYY-MM-DD
    TAG:            canon-v1
    CANON_COMMIT:   full 40-character synthesis merge SHA
    CANON_SHA256:   full 64-character canon/CANON.md SHA-256
    CANON_BYTES:    exact canon/CANON.md byte count
    ```

16. Update `README.md` from GENESIS to ACTIVE and point readers to
    `canon/CORE.md`, `canon/CANON.md`, and `canon/FRONTIER.md`.
17. Open and merge a separate reviewed activation pull request.
18. Tag the activation merge commit `canon-v1`, create the release, and attach
    the recorded `canon/SHA256SUMS`.
19. Verify the tag, release, public readback, hashes, registry, and all required
    checks.
20. Freeze the internal repository for scientific writes and replace its root
    notice with a pointer to this repository. Only then is cutover complete.

## 5. Startup after cutover

At the start of every session:

1. Fetch public `main`; do not work from an attachment or mirror.
2. Read `STATUS.md`, `POLICY.md`, this file, `canon/CORE.md`, and
   `canon/FRONTIER.md`.
3. Confirm the declared public tag and commit are ancestors of `main`, the
   Canon hash matches, and required checks are green.
4. Search open issues, branches, `probes/`, and the registry for collisions.
5. Claim exactly one named probe in a public issue before committing.

Agents with access to the internal archive may read it only for audit. Missing
material is never copied opportunistically into a public probe. A justified
addition uses a named `legacy/` pull request, a manifest, and a security
review.

## 6. Formal work after cutover

1. Create `probe/P-NAME` and `probes/P-NAME/`.
2. Freeze the six preregistration fields and action layer required by
   `POLICY.md`.
3. Commit and push `PREREG.md` and the accepted exact verifier before any
   formal gate execution. Record commit and file hashes.
4. Run the pinned verifier locally from the repository root on Linux or a
   Linux-compatible environment. Save exact stdout as `EXPECTED.txt` and
   record the required fields in `RUN.md`.
5. Open a pull request changing at most one probe directory. The required
   check independently reruns the changed verifier on GitHub
   `ubuntu-latest` and compares hashes and exact bytes.
6. If the local and GitHub architectures differ, their byte-identical output
   satisfies the two-architecture computation gate. If they are the same, the
   result is reproduced but a computation-only claim remains at most `C`.
   Independent proof may establish `T`; the verifier then audits it.
7. Add `RESULT.md`. A fired falsifier is merged, not hidden. Update the
   registry, frontier, and Canon only to the earned status and scope.
8. Pass policy and scientific checks, security-audit the named files, and merge
   without squash or rebase.
9. A public Canon release is a separate declared fold with deterministic
   output, `SHA256SUMS`, immutable tag `canon-vN`, and updated `STATUS.md`.

Notes and incomplete proposals live under `notes/`, carry `NON-CANONICAL`,
need no verifier, and never edit `canon/CANON.md`. Canon patch proposals live
under `notes/canon/`; only a later sealed public fold changes the Canon.

Do not add or loosen GitHub workflows without an explicit policy change.
`pull_request_target`, mutable action tags, persisted checkout credentials,
and write permissions are forbidden.

Commit as `A. M. Thorn <thorn@twistj.com>` unless the author explicitly names
another contributor identity.

## 7. Stop conditions

Stop without guessing if authority is unclear, the internal basis moves during
synthesis, a public claim lacks equal-or-stronger support, a hash differs,
evidence is missing, a license is uncertain, a probe collides, formal data were
opened before the pin, a threshold moved, a layer lift is unnamed, or public
safety is in doubt.
