# Public intake and verification

**NON-CANONICAL / NO AUTHORITY. Conditional candidate-T proofs and
candidate-C finite audits, L1. Review date: 2026-10-09 (Europe/Prague).**

Reservation: [#1425](https://github.com/mathorn1973/twist-j/issues/1425).
The mathematical results survived the exposed text review in
[PUBLIC_REVIEW.md](PUBLIC_REVIEW.md). The independently admitted source
bridge is still absent; [BRIDGE_ASSESSMENT.md](BRIDGE_ASSESSMENT.md) records
the precise disposition. The condition for releasing the entire physical
chain as Public Canon v101 has not been met.

## Preserved input and authority

The supplied archive `C-FIELD-STATIC-TRANSPOSITION-COMPLETION-N.zip` has
SHA-256 `8c08bae53549b06ba4555f2478ec318c888f0223899b00b0db79f9cee73b5554`.
Its 21 extracted files total 176533 bytes. All 20 entries in its original
`SHA256SUMS` matched, and all 21 original files are preserved byte for byte.
The archive was inspected before extraction and source review preceded
execution. No executable binary, credential, private machine identity,
private path or external dependency was found in the material being added.

The checked public base is `7d7f588c42422c2cf37b04d76ebc13ca55eb96dc`,
ACTIVE Public Canon v100. Its content commit, activation tag target, Canon
hash and byte count match the tuple in SOURCES.md. Public main and all 222
remote heads were checked before this intake; no competing named
static-transposition or v101 lane was found. The earlier synthesis remains
pinned at `c404723bbda3a65dd39c86ae4fc1152b587977c3` in PR #1424.

`PREREG.md`, `FREEZE.md`, `REVIEW.md`, `RUN.md` and the original machine
records describe the supplied local research history. Their retained
statements about no publication and the then-open PR are historical to
that preparation, not assertions that this public intake did not occur.
Byte integrity and internally consistent timestamps do not independently
prove the historical ordering of the original freeze and first executions,
or the authors' reported implementation independence. This review does not
retroactively turn a local pin into a public preregistration.

The original `SHA256SUMS` continues to cover its original 20 entries only.
`PUBLICATION_SHA256SUMS` binds every file in the public package other than
itself, including the original manifest and the separately added review,
bridge assessment, this intake record and REPLAY.json.

## New replay of unchanged programs

Both scientific programs were inspected as source before a direct replay.
They use the standard library, have no network or mutating filesystem
operations, and do not import each other. The integer implementation reads
its specification, addendum and own bytes to verify or print their hashes.
The original `run_once.py` was not run: its first-run outputs already exist
and must not be replaced.

The replay used Ubuntu 22.04.5 LTS on x86_64 with Python 3.10.12. Each program
ran once in this review in a separate process with a 300-second limit and
new output paths outside the original package. Both exited zero, produced
empty stderr and matched their respective supplied stdout byte for byte.
All 21 original files still matched their pre-execution hashes afterward.
The neutral machine record is [REPLAY.json](REPLAY.json).

| Program | Source SHA-256 | Stdout bytes | Stdout SHA-256 |
|---|---|---:|---|
| verify.py | `309162881f0f66e124919b867f54b2f47b78c8d51ac35d652a29dcbea09a6340` | 13371 | `7b285b713da76c2c73b34d4e4c2f6b3cced91117dbf41c200a4dcc61582b497a` |
| break_check.py | `c02319e5a43a70daca464b73fa909a599ba7e0ff1c4f504b07c58163eb2498b6` | 6539 | `28f359edbdf06352feb692137b029c4711fafdcb46a39e8e2a9d737e4db54d4e` |

The programs can be replayed individually from this directory with
`python3 -I verify.py` and `python3 -I break_check.py`, redirecting stdout
and stderr to new paths and comparing against the corresponding original
`*.first.stdout` and empty `*.first.stderr`. No original source or output
needs alteration. `-I` ignores Python-specific environment variables,
including PYTHONHASHSEED: the environment settings in the supplied commands
are not proof of a forced hash seed. Source review found no resulting
nondeterministic scientific traversal; set traversals are ordered and the
recorded outputs were reproduced exactly without modifying the programs.

This is a repeat on the same architecture with a different Python version,
not a first run, public formal probe or two-architecture scientific gate.
The two programs use different finite domains. In
particular the breaker's `primary_raw_crosscheck` has different rotations
of the charge fixtures and neutral decorations; its name does not establish
pointwise equality of the two programs' input domains. Each is checked
against its own retained first output. Counts are visits, not distinct
states or independent theorems. The absent S01 admission mismatch in these
finite samples is not promoted to a universal absence result.

## Publication scope

Only this notes directory is added. Canon, registry, existing source laws,
probes, reproductions and workflows are unchanged. Ordinary pull-request
checks test repository policy, tools, Canon and ledgers on both required
architectures. They do not automatically execute programs under notes and
must not be cited as two-architecture scientific evidence for these files.

The universal claims rest on their exposed exact proofs. The finite replay
supports transcription and implementation checks at its stated scope.
No physical source selection, energy calibration, apparatus realization,
native-U/J identification or photon phase follows from this publication.
