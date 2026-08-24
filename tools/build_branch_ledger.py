#!/usr/bin/env python3
"""Build a branch-retention ledger for every ref on the origin remote.

The ledger exists to make one decision safe: which refs may be pruned.  A
MERGED ref is an ancestor of `main`, so deleting it deletes no content.  A
DIVERGENT or ORPHAN ref carries content that exists nowhere else, and deleting
it hides evidence.  See AGENTS.md, "Branch retention".

Two failure modes are guarded explicitly, because both silently produce a
ledger that authorises the wrong deletion:

* A shallow clone truncates history, so `merge-base` reports branches as
  unrelated and genuinely merged refs are classified DIVERGENT (or, worse, a
  grafted boundary makes an unmerged ref look reachable).  This tool refuses
  to run in a shallow clone rather than emit a ledger that cannot be trusted.
* A branch with no merge base at all is a true orphan.  `git diff A...B`
  errors on those, and a shell pipeline that ignores the error records the
  branch as contributing zero files.  Orphans are classified ORPHAN and
  measured with a two-dot diff instead.
* The base branch is an ancestor of itself, so a naive ancestor test files it
  under MERGED and a prune list built from that column deletes `main`.  The
  base branch is classified BASE and is never prunable.

Only the MERGED state is prunable.  BASE, DIVERGENT and ORPHAN are not.
"""

from __future__ import annotations

import argparse
import subprocess
import sys


FIELDS = (
    "branch",
    "state",
    "ahead",
    "last_commit",
    "adds_files",
    "has_prereg",
    "has_result",
)


def git(*args: str) -> str:
    result = subprocess.run(
        ("git", *args), capture_output=True, text=True, check=True
    )
    return result.stdout.strip()


def git_ok(*args: str) -> bool:
    return subprocess.run(
        ("git", *args), capture_output=True, text=True
    ).returncode == 0


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def require_full_history() -> None:
    if git("rev-parse", "--is-shallow-repository") == "true":
        fail(
            "shallow clone: branch states cannot be determined. "
            "Run `git fetch --unshallow` first."
        )


def branch_names(remote: str) -> list[str]:
    listing = git(
        "for-each-ref", "--format=%(refname:short)", f"refs/remotes/{remote}"
    )
    names = []
    for line in listing.splitlines():
        short = line.strip()
        if not short or short == f"{remote}/HEAD":
            continue
        names.append(short[len(remote) + 1:])
    return sorted(names)


def measure(base: str, head: str, orphan: bool) -> tuple[int, int, int]:
    spec = f"{base}..{head}" if orphan else f"{base}...{head}"
    listing = git("diff", "--name-only", spec)
    paths = [p for p in listing.splitlines() if p]
    prereg = sum(1 for p in paths if "PREREG" in p)
    result = sum(1 for p in paths if "RESULT" in p)
    return len(paths), prereg, result


def build(remote: str, base: str) -> list[dict[str, str]]:
    require_full_history()
    rows = []
    for name in branch_names(remote):
        head = f"refs/remotes/{remote}/{name}"
        if git("rev-parse", head) == git("rev-parse", base):
            rows.append(
                dict(
                    branch=name, state="BASE", ahead="0", last_commit="-",
                    adds_files="0", has_prereg="0", has_result="0",
                )
            )
            continue
        if git_ok("merge-base", "--is-ancestor", head, base):
            rows.append(
                dict(
                    branch=name, state="MERGED", ahead="0", last_commit="-",
                    adds_files="0", has_prereg="0", has_result="0",
                )
            )
            continue
        orphan = not git_ok("merge-base", base, head)
        files, prereg, result = measure(base, head, orphan)
        rows.append(
            dict(
                branch=name,
                state="ORPHAN" if orphan else "DIVERGENT",
                ahead=git("rev-list", "--count", f"{base}..{head}"),
                last_commit=git(
                    "log", "-1", "--format=%ad", "--date=short", head
                ),
                adds_files=str(files),
                has_prereg=str(prereg),
                has_result=str(result),
            )
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--base", default="origin/main")
    parser.add_argument("--output", help="write TSV here instead of stdout")
    args = parser.parse_args()

    rows = build(args.remote, args.base)
    lines = ["\t".join(FIELDS)]
    lines += ["\t".join(row[f] for f in FIELDS) for row in rows]
    text = "\n".join(lines) + "\n"

    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text)
    else:
        sys.stdout.write(text)

    counts: dict[str, int] = {}
    for row in rows:
        counts[row["state"]] = counts.get(row["state"], 0) + 1
    summary = " ".join(f"{k}={counts[k]}" for k in sorted(counts))
    print(f"LEDGER {len(rows)} refs {summary}", file=sys.stderr)


if __name__ == "__main__":
    main()
