# THE BOARD. How work is assigned, sequenced and reported

NON-CANONICAL OPERATIONS. This branch is `ops/board`. It carries no science,
no canon file, and it is **never merged into `main`**. Deleting it destroys
nothing scientific.

## Why it exists and why it is shaped this way

Four agent seats work on this repository and **git is the only surface all four
can see**. Chats are per-seat. The claude.ai Project is invisible to the GPT
seats. So assignment, sequencing and reporting all have to live in git or they
do not exist.

Two design rules follow, and they are what makes concurrent seats safe:

```text
1  ONE WRITER PER FILE. Each seat writes only ops/log/<SEAT>.log. No two seats
   ever touch the same file, so git never has to merge a conflict.
2  APPEND ONLY. Nobody edits or deletes a line, ever, including their own.
   A mistake is corrected by appending a new line, not by rewriting history.
```

Status is not stored. It is **derived** from the logs by `ops/board.py`, so
nobody can hold a stale view and nobody has to remember to update a field.

## The four seats

```text
S1  Claude cloud + JAS_2 relay    aarch64 formal runs, pushes branches,
                                  coordinator. CANNOT open issues or PRs.
S2  Claude Work, local PC         full GitHub. Opens issues and PRs for S1.
S3  ChatGPT Work, Mac Studio      full machine, full GitHub.
S4  ChatGPT cloud                 sandbox with bidirectional git.
```

## Files

```text
ops/TASKS.tsv     the backlog. Coordinator writes it; seats never edit it.
                  columns: task_id  seat  depends_on  object_key  title
                  depends_on is space separated, or "-" for none.
ops/log/<S>.log   append-only event log, one writer.
                  columns: utc_iso  seat  task_id  event  detail
                  event is one of CLAIM DONE BLOCKED STOP NOTE
ops/board.py      derives and prints status. Reads only. Never writes.
```

## Get the board

Use a separate directory. `ops/board` is an orphan branch with no canon files,
so do not check it out over your working clone.

```sh
git clone -b ops/board git@github.com:mathorn1973/twist-j.git board
cd board
python3 ops/board.py
```

Or, from an existing clone, as a worktree:

```sh
git fetch origin ops/board
git worktree add ../board origin/ops/board
```

## The loop every seat runs

```sh
# 1  refresh and see what is yours
cd board && git pull --rebase --quiet
python3 ops/board.py S3          # your seat id

# 2  claim it before you start
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
printf '%s\tS3\tT1-02\tCLAIM\tstarting\n' "$TS" >> ops/log/S3.log
git add ops/log/S3.log && git commit -q -m "board: S3 claim T1-02"
git pull --rebase --quiet && git push --quiet

# 3  do the work in your OTHER clone, on the task's own branch

# 4  report the outcome, with the facts a later reader needs
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
printf '%s\tS3\tT1-02\tDONE\tfreeze commit abc1234, prereg sha256 89ab...\n' "$TS" >> ops/log/S3.log
git add ops/log/S3.log && git commit -q -m "board: S3 done T1-02"
git pull --rebase --quiet && git push --quiet
```

If the push is rejected, `git pull --rebase` and push again. Because each seat
writes a different file the rebase is always clean. **Never force-push this
branch.**

## The four events

```text
CLAIM    you are starting. Claim before you touch anything, so a second seat
         reading the board does not pick up the same task.
DONE     finished. The detail field must carry the facts the next seat needs:
         commit shas, file sha256s, issue or PR numbers, exit codes. A DONE
         with an empty detail is not a report.
BLOCKED  you cannot proceed and someone else can unblock you. Say exactly what
         is missing. This surfaces at the bottom of the board under ATTENTION.
STOP     a stop condition fired: authority unclear, hash mismatch, collision,
         threshold moved, layer lift unnamed, safety in doubt. Do not guess and
         do not work around it. STOP also surfaces under ATTENTION.
NOTE     anything worth recording that is not a state change. Free.
```

`board.py` takes the **last non-NOTE event** for a task as its state, so a
BLOCKED can be cleared by appending a later CLAIM or DONE. Nothing is edited.

## How sequencing works

A task is READY when every task in its `depends_on` has a DONE. `board.py`
computes that; no seat decides it. `python3 ops/board.py <SEAT>` prints the one
task you should pick up next, or tells you what you are waiting on and who owns
it.

If two seats could both work, both can: the dependency graph is the only
ordering constraint, and any two READY tasks are independent by construction.

## What the board does not do

It does not hold science. Preregistrations, verifiers, breakers, results and
promotion packages live on their own branches under `notes/` and `probes/`,
governed by `POLICY.md` and `AGENTS.md`. The board only records **who did
what, when, and what it produced**.

It also does not grant permission. The hard rules stay where they are: never
push to `main`, never touch `canon/`, `tools/`, `.github/` or a workflow, never
resume a sealed probe, never put a machine name or a token in a committed file,
one fold in flight at a time, commit as `A. M. Thorn <thorn@twistj.com>`.

## Adding work

The coordinator appends rows to `ops/TASKS.tsv` and pushes. Seats do not edit
it; if a task is wrong, append a NOTE or BLOCKED to your own log saying so and
the coordinator fixes the row.
