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
- During `GENESIS`, `twistj.com/canon/` remains on the legacy line. Do not
  repoint it or present it as Public Canon v1 before activation.

## 2. Clean-slate synthesis rule

The author selects one sealed internal state as the synthesis basis. Agents do
not assume that the latest visible internal version is the chosen basis.

Freeze the internal basis while Public Canon v1 is being written:

```text
internal version | source HEAD | lock | Canon file | SHA-256 | byte count
```

The frozen tuple is an audit input, not the public version identity. If it
changes during synthesis, stop and re-freeze.

The internal extraction is a non-normative synthesis surface, even if it is
informally called "Canon v1". Name it once in the reconciliation audit and
nowhere in the public Canon. It does not satisfy `check_canon.py`, and agents
must not make it pass by copying or mechanically wrapping it.

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
   manifests required by the public text. While the repository is `GENESIS`,
   `CITATION.cff` must not point to the legacy `twistj.com/canon/` page.
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

### Phase A cross-architecture staging

During `GENESIS`, a synthesis cluster that depends on computation is
transported between systems through GitHub, never by copying an unattached
verifier or stdout file.

1. The coordinator creates a dedicated branch from the current synthesis
   branch:

   ```text
   staging/canon-v1-NAME
   ```

2. The coordinator commits the complete candidate before the first formal
   staging run: verifier, `EXPECTED.txt`, README, Canon text, registry,
   audit, changelog, hashes, and notes. This commit is the immutable
   `candidate_commit`; push it to GitHub. Do not amend or force-push it.
3. Runners work sequentially on the same staging branch. Each runner fetches
   the branch, checks out the exact candidate or a descendant containing only
   earlier run records, confirms a clean worktree, and runs:

   ```text
   python3 tools/run_staged_reproduction.py NAME --candidate FULL_SHA
   ```

4. The runner tool refuses a changed verifier or `EXPECTED.txt`, executes in
   a deterministic environment, compares stdout byte for byte, requires exit
   0 and empty stderr, and writes exactly one neutral record:

   ```text
   reproduce/NAME/RUNS/aarch64.md
   reproduce/NAME/RUNS/x86_64.md
   ```

   Records contain only operating system, architecture, Python version,
   hashes, byte counts, and commit pins. Machine nicknames are forbidden.
5. The runner stages only its record, commits as A. M. Thorn, and pushes the
   staging branch. A rejected push is a stop condition: never force-push;
   contact the coordinator before rebasing or rerunning.
6. After both architecture records are present, the coordinator runs:

   ```text
   python3 tools/check_staged_reproduction.py NAME \
     --candidate FULL_SHA --require-architectures aarch64 x86_64
   ```

7. Only a passing validator permits `git merge --ff-only` of the staging
   branch into `synthesis/canon-v1`. Push the synthesis branch after the
   fast-forward. The staging exchange creates no pull request; the whole of
   Phase A still ends in the single reviewed synthesis pull request.
8. Any change to the verifier, expected output, scientific scope, or
   normative text after the candidate pin invalidates all run records. Create
   a new candidate commit and fresh staging branch; do not reinterpret old
   records.

### Phase A asynchronous prep and staging

The formal staging lane above remains linear because every cluster changes
shared Canon, registry, audit, and hash files and must fast-forward into the
single synthesis branch. Expensive preparation runs one cluster ahead in a
separate, explicitly non-formal lane:

```text
prep/canon-v1-NAME       mutable preparation, no formal run records
staging/canon-v1-NAME    immutable candidate and sequential run records
synthesis/canon-v1       one fast-forward integration lane
```

1. As soon as cluster `N` has an immutable staging candidate, another agent
   may create `prep/canon-v1-NEXT` from the then-current synthesis HEAD.
   Preparation may include internal-basis audit, conservative public scope,
   verifier development, draft Canon changes, and non-formal dry runs.
2. A prep branch is non-canonical and non-formal. It must not contain
   `reproduce/*/RUNS/` records, call a dry run a reproduction, or claim an
   earned public status. It may be rebased and rewritten before pinning.
3. While the next cluster is in prep, architecture runners and the
   coordinator finish cluster `N` on its staging branch. No other commit may
   enter synthesis while a formal staging candidate awaits fast-forward.
4. After cluster `N` reaches synthesis, the builder rebases or reapplies the
   prep work onto the new synthesis HEAD. Conflicts in shared Canon files are
   resolved here, before immutability begins. All policy, Canon, reproduction,
   audit, and hash checks are rerun.
5. The builder creates `staging/canon-v1-NEXT` from the exact current
   synthesis HEAD. The complete candidate is one commit with exactly one
   parent. The first formal run may start only after that commit is pushed.
   A prep commit is never itself treated as the immutable pin merely because
   its tree happened to pass a dry run.
6. Agents discover work from GitHub rather than from a relayed handoff. At
   session start run one of:

   ```text
   python3 tools/staging_status.py --fetch --role builder
   python3 tools/staging_status.py --fetch --role aarch64
   python3 tools/staging_status.py --fetch --role x86_64
   python3 tools/staging_status.py --fetch --role coordinator
   ```

   Add `--json` for machine-readable output and `--strict` in monitoring.
   The tool reports `PREP_CURRENT`, `REBASE_REQUIRED`,
   `SUPERSEDED_BY_STAGING`, `WAIT_AARCH64`, `WAIT_X86_64`,
   `READY_TO_VALIDATE`, `INTEGRATED`, or a stop state. Its printed command is
   an instruction, not authorization to skip checkout, clean-tree, authorship,
   validation, or no-force gates. Use the reproduction directory name as the
   branch suffix when possible. If a shorter branch label was already pinned,
   the tool derives the actual reproduction name from the immutable candidate
   and its run records and reports both names explicitly.
7. The steady-state rhythm is: builder prepares `N+1`; architecture runners
   reproduce `N`; coordinator validates and fast-forwards `N`; builder moves
   `N+1` to the new base and pins it. This is the Phase A tik-tok. GitHub refs
   are the queue and handoff surface; chat summaries are informational only.
8. `STALE_BASE`, `BLOCKED`, more than one branch eligible for the same formal
   role, a non-fast-forward push, or a synthesis change during formal staging
   is a stop condition. Never repair these states by force-pushing a staging
   branch or silently reinterpreting a candidate.

### Phase B: activation

14. Create `activate/canon-v1` from the merged public `main`.
15. Update `STATUS.md` to the exact active form:

    ```text
    STATE:          ACTIVE
    CANON:          Public Canon v1
    AUTHORITY:      mathorn1973/twist-j main
    CUTOVER:        YYYY-MM-DD
    TAG:            canon-v1
    CONTENT_COMMIT: full 40-character synthesis merge SHA
    CANON_SHA256:   full 64-character canon/CANON.md SHA-256
    CANON_BYTES:    exact canon/CANON.md byte count
    ```

16. Update `README.md` from GENESIS to ACTIVE, point readers to
    `canon/CORE.md`, `canon/CANON.md`, and `canon/FRONTIER.md`, and
    finalize `CITATION.cff` with the Public Canon landing-page URL.
17. Open and merge a separate reviewed activation pull request.
18. Tag the activation merge commit `canon-v1`, record that tag target as
    `ACTIVATION_COMMIT` in the release manifest, create the release, and attach
    the recorded `canon/SHA256SUMS`.
19. Repoint `twistj.com/canon/` from the legacy line to Public Canon v1,
    then verify the tag, release, public readback, hashes, registry, and all
    required checks.
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
   record neutral fields in `RUN.md`, for example
   `platform: Ubuntu 24.04` and `architecture: aarch64`. Never record a
   machine nickname.
5. Open a pull request changing at most one probe directory. The required
   check independently reruns the changed verifier on GitHub x86_64
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
