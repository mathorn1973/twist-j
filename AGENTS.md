# Agent Manual

`POLICY.md` is binding. `STATUS.md` decides authority. This file defines the
migration and daily operating procedure.

## 1. Authority gate

Read `STATUS.md` before any scientific work.

- If `STATE: GENESIS`, this repository is policy-only. Do not import a Canon,
  open a formal probe, or treat any claim here as canonical.
- If `STATE: ACTIVE`, confirm the declared Canon tag, commit, SHA-256, and lock
  before continuing.
- Before cutover, `mathorn1973/twistj-jam` remains authoritative. After
  cutover it is read-only provenance. Never infer authority from file age,
  filename, a public mirror, or an attached copy.

## 2. Migration rule

The author selects one sealed source version. Agents do not assume that the
latest visible version is the cutover version.

The frozen source tuple is:

```text
version | source HEAD | lock commit | Canon filename | SHA-256 | byte count
```

If any field changes during migration, stop and re-freeze. Migration carries
status and evidence; it creates no new scientific claim.

## 3. What migrates

### Required

1. The selected standalone Canon, byte-for-byte, as `canon/CANON.md`.
2. `canon/CORE.md`, `FRONTIER.md`, `REGISTRY.tsv`, and `CHANGELOG.md`, derived
   from that Canon and never stronger than it.
3. For every retained canonical claim, the available accepted evidence:
   preregistration, verifier, exact input or fixture, expected stdout or hash,
   run record, result and scope note, and lock entry.
4. Every canonical falsification and its accepted evidence.
5. Definitions and live falsifiers for every retained `H` and `O` item.
6. The selected fold assembler, current lock material, minimal kernel
   reproduction, and all small data required to reproduce accepted gates.
7. A migration manifest with source path, source commit, Git blob SHA,
   SHA-256, byte count, destination, license, and classification.
8. `CITATION.cff`, authorship, license notices, and external-data manifests.

Accepted probe evidence uses the stable layout:

```text
probes/P-NAME/
    PREREG.md
    verify.py
    EXPECTED.txt
    RUNS.md
    RESULT.md
```

Do not invent missing legacy artifacts. Mark the gap explicitly in the
registry and migration manifest.

### Curated, only when still evidential

- A historical patch that is the sole surviving statement of scope.
- A negative or superseded route required to understand a canonical `F`.
- A small regression fixture whose change would alter a Canon result.
- An independent reproduction that materially differs from the accepted
  verifier.

### Excluded

- Earlier complete Canons and duplicate folded patches. Git tags and the
  source repository preserve history.
- `HANDOFF.md`, `tasks.md`, old control boards, session chatter, and stale
  frontier summaries.
- Storyteller, JAM training, PhiTorch product work, books, websites,
  infrastructure, monitoring, DNS, machine administration, and unrelated CI.
- Checkpoints, models, binaries, build products, caches, raw logs, temporary
  trees, scratch files, backups, and large regenerated outputs.
- Secrets, private addresses or hostnames, credentials, personal data, and
  unreviewed third-party material.
- Superseded formulations presented as current science.
- The old repository history wholesale.

The old repository remains an immutable archive. Selective evidence is
imported; operational debris is not.

## 4. Cutover procedure

1. Confirm that no source probe is active and the selected Canon is sealed.
2. Record the frozen source tuple.
3. Build the migration manifest before copying files.
4. Classify every candidate as required, curated, or excluded.
5. Audit every included file for secrets, private infrastructure, license,
   size, and duplicate content.
6. Create `migration/canon-vNNN`; do not mix migration with new science.
7. Copy accepted evidence without editing it. Put necessary explanations in
   the manifest, not inside sealed artifacts.
8. Materialize the stable Canon files and registry.
9. Run the policy gate, hash audit, registry audit, Canon build, and available
   reproductions. The imported `canon/CANON.md` hash and byte count must equal
   the frozen source.
10. Open one migration pull request listing inclusions, exclusions, gaps, and
    all hashes. A mismatch, ambiguity, or security concern blocks cutover.
11. Merge with a merge commit. Create immutable tag `canon-vNNN` and a release
    containing `SHA256SUMS`.
12. Change `STATUS.md` to `ACTIVE` with the public authority, version, tag,
    commit, Canon SHA-256, byte count, and legacy source tuple.
13. Verify public readback and all required checks.
14. Freeze the old repository and replace its root notice with a pointer to
    this repository. Only then is cutover complete.

## 5. Startup after cutover

At the start of every session:

1. Fetch public `main`; do not work from an attachment or mirror.
2. Read `STATUS.md`, `POLICY.md`, this file, `canon/CORE.md`, and
   `canon/FRONTIER.md`.
3. Confirm the declared tag and lock are ancestors of `main`, the Canon hash
   matches, and required checks are green.
4. Search open issues, branches, `probes/`, and the registry for collisions.
5. Claim exactly one named probe in a public issue before committing.

Agents with access to `twistj-jam` may read it only for provenance. A missing
artifact is imported through a named `legacy/` pull request with manifest and
security audit. It is never copied opportunistically into a probe.

## 6. Formal work after cutover

1. Create `probe/P-NAME` and `probes/P-NAME/`.
2. Freeze the six preregistration fields and action layer required by
   `POLICY.md`.
3. Commit and push `PREREG.md` and the accepted exact verifier before any
   formal gate execution. Record commit and file hashes.
4. Run exact gates. Preserve stderr, exit code, bytes, line count, platform,
   environment, verifier hash, and stdout hash.
5. A `T` result requires byte-identical stdout on two independent
   architectures. A fired falsifier is merged, not hidden.
6. Add the run and result records. Update the registry, frontier, and Canon
   only to the earned status and scope.
7. Open a pull request, pass policy and scientific checks, security-audit the
   named files, and merge without squash or rebase.
8. A Canon release is a separate declared fold with deterministic output,
   `SHA256SUMS`, immutable tag, and updated `STATUS.md`.

Commit as `A. M. Thorn <thorn@twistj.com>` unless the author explicitly names
another contributor identity.

## 7. Stop conditions

Stop without guessing if authority is unclear, the source moves during
migration, a hash differs, evidence is missing, a license is uncertain, a
probe collides, formal data were opened before the pin, a threshold moved, a
layer lift is unnamed, or public safety is in doubt.
