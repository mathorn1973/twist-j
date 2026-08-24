# Branch ledger snapshot, 2026-08-24

Status: **NON-CANONICAL. ONE-SHOT SNAPSHOT.**

This directory records the state of every ref on `origin` at one instant, so
that a prune of dead refs can be audited afterwards: the ledger says what
existed, what was deleted, and where the deleted content still lives. It
registers nothing, promotes nothing, and changes no status.

```text
taken           2026-08-24
base            origin/main ec810acad66ab73631fdfa7e582043e7363eb435
Canon           Public Canon v62, tag canon-v62, CONTENT_COMMIT
                72d7fdaf131f999763bb0904e50e8841245027ff
generator       tools/build_branch_ledger.py
refs measured   202
```

The snapshot is not maintained. It is a dated audit input, not a live index;
regenerate rather than edit it.

## States

```text
BASE        1    the base branch itself. Never prunable.
MERGED    107    an ancestor of main. Its content is in main for ever, so
                 deleting the ref deletes no content and hides no evidence.
DIVERGENT  93    content exists only on this ref. NEVER delete.
ORPHAN      1    unrelated history, no merge base with main at all.
                 Content exists only on this ref. NEVER delete.
```

Only the 107 `MERGED` refs are prunable. Deleting a ref is not deleting
history: every commit remains reachable from `main`.

## Three ways a naive ledger gets this wrong

The obvious shell pipeline for this job produces a ledger that authorises the
wrong deletions. All three faults were observed while building this snapshot,
and `tools/build_branch_ledger.py` guards each one.

```text
shallow clone   A truncated clone has no common history to find, so
                `merge-base` reports genuinely merged branches as unrelated.
                Measured here: the same repository reported 35 MERGED and 142
                unrelated while shallow, against 107 and 1 once unshallowed.
                The tool now refuses to run in a shallow clone.
orphan branch   `git diff main...branch` errors when there is no merge base.
                A pipeline that discards the error records zero files.
                Measured here: ops/board recorded as 0 files, actually 1337
                files including 158 preregistrations and 131 results. It is
                the largest branch in the repository.
the base ref    `main` is an ancestor of itself, so an ancestor test files it
                under MERGED. A prune list built from that column deletes the
                default branch. The tool classifies it BASE instead.
```

## Prune procedure

Regenerate, confirm the counts, then delete only the `MERGED` column:

```sh
git fetch --unshallow                       # no-op if already complete
git fetch origin '+refs/heads/*:refs/remotes/origin/*' --prune
python3 tools/build_branch_ledger.py --output /tmp/ledger.tsv
awk -F'\t' 'NR>1 && $2=="MERGED"{print $1}' /tmp/ledger.tsv > /tmp/prune.txt
grep -qx main /tmp/prune.txt && { echo "STOP: base branch in prune list"; exit 1; }
xargs -a /tmp/prune.txt git push origin --delete
```

The `grep -qx main` line is a second, independent stop. Keep it even though
the generator already excludes the base branch.

## The 93 divergent and 1 orphan refs

These are not prune candidates. They are the work queue: each one holds
content that exists nowhere else, and each needs a disposition recorded
before it can be considered closed. The retention rule is stated in
`AGENTS.md` under "Branch retention".
