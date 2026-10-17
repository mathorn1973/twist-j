#!/usr/bin/env python3
"""Custody check of a synthesis SOURCES.tsv and INPUTS.sha256 against raw Git.

Usage: python3 custody_check.py <repository clone> <synthesis package directory>

Reads every Git row of SOURCES.tsv, materializes the blob from the named
commit with git cat-file, and compares blob id, SHA-256 and byte count; also
checks that INPUTS.sha256 agrees on every row. Receipt rows are counted but
not fetched. Every named commit must be present in the clone (git fetch
origin <sha> first). Standard library only.
"""
import csv, hashlib, subprocess, sys

REPO = sys.argv[1]
PKG = sys.argv[2]

def git(*a):
    return subprocess.run(["git", "-C", REPO, *a], capture_output=True, check=True).stdout

rows = list(csv.DictReader(open(f"{PKG}/SOURCES.tsv", newline=""), delimiter="\t"))
inputs = {}
for line in open(f"{PKG}/INPUTS.sha256"):
    line = line.rstrip("\n")
    if not line:
        continue
    h, name = line.split("  ", 1)
    inputs[name] = h

ok = bad = receipts = 0
seen = set()
for r in rows:
    name = r["materialized_path"]
    seen.add(name)
    if r["kind"] != "git":
        receipts += 1
        if inputs.get(name) != r["sha256"]:
            print("MISMATCH receipt manifest/sources", name)
            bad += 1
        continue
    spec = f"{r['commit']}:{r['path']}"
    try:
        blob = git("rev-parse", spec).decode().strip()
        data = git("cat-file", "blob", spec)
    except subprocess.CalledProcessError:
        print("MISSING", spec); bad += 1; continue
    sha = hashlib.sha256(data).hexdigest()
    problems = []
    if blob != r["git_blob"]: problems.append(f"blob {blob}!={r['git_blob']}")
    if sha != r["sha256"]: problems.append("sha256")
    if len(data) != int(r["bytes"]): problems.append(f"bytes {len(data)}!={r['bytes']}")
    if inputs.get(name) != r["sha256"]: problems.append("INPUTS.sha256 disagrees")
    if problems:
        bad += 1; print("BAD", spec, problems)
    else:
        ok += 1

extra = set(inputs) - seen
print(f"git rows ok={ok} bad={bad} receipts={receipts} rows={len(rows)} inputs={len(inputs)} inputs_not_in_sources={len(extra)}")
if extra:
    print("extra:", sorted(extra))
