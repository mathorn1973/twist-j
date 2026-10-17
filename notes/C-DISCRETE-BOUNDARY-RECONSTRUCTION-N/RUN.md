# First exact execution record

**NON-CANONICAL / NO AUTHORITY. L1, local candidate-C evidence only.**

The two admissible programs were frozen before either first scientific
execution. Both first runs passed; no scientific correction, second attempt
or rerun occurred. The separate excluded implementation described in
[CUSTODY.md](CUSTODY.md) was never executed and supplies no finite evidence.

## Immutable inputs

| Artifact | Original Git commit | SHA-256 |
|---|---|---|
| PREREG.md | e092feb641e859d7d959e72f3ab39ec88d4fc53c | b46387bfb91858dbf486b81749742f2da118cb4eeae78aec7ce6de1f502af813 |
| verify.py | 77dd005734c5b2e8f965ab883c1cdccfdaaa5a47 | 2b88115d08058aa43d70cc677b0f0797f169fdf223dadd4ec96fa3e8c182f226 |
| break.py, admissible | 2af7ff45456f0f4cc9a8cb7b46a0e5c97cf4d8c5 | 9bdc91bc065cfe5a2bc52a79cee49e5a44382f83dd0c0c907a44e7906eead2b9 |
| PROOF.md | 0e56f9605129d414348a3cf1a0629c1c607bc43f | a3684d789d4876b812c76d6ef2f53ff34924f77135f5cd4b017782f44c2ec029 |
| REVIEW.md, attribution clarified | 906988fe7ad16339498f833c3e389e3d6c5edb51 | 1b1fdfa4b5385fa56025f61254e62dd590889f3469e33dc0e1a5a392c4d82a2c |

Both first executions used the same clean detached checkout:

```text
83a2715f1dc6bacdfd0b1f3cdd6d2f7ed89264bb
```

It contains the included commits as unchanged merge ancestors. Git HEAD,
clean worktree and exact preregistration, proof and program hashes were
checked before and after each execution. Final packaging adds only the
reporting documents and matching expected output to these fixed sources.

## Environment and commands

Operating system: Ubuntu 24.04.3 LTS.
Architecture: x86_64.
Runtime: CPython 3.12.14.

```text
LC_ALL=C
LANG=C
PYTHONHASHSEED=0
PYTHONDONTWRITEBYTECODE=1
TZ=UTC
```

From the repository root, the exact program arguments were:

```text
python3 -I notes/C-DISCRETE-BOUNDARY-RECONSTRUCTION-N/verify.py
python3 -I notes/C-DISCRETE-BOUNDARY-RECONSTRUCTION-N/break.py
```

The external runner resolved `python3` to its CPython 3.12.14 executable
and ran the programs sequentially with `subprocess.run(..., timeout=180)`.
The wall timeout was 180 seconds for each program, as frozen. The runner
did not implement any scientific claim. Fresh stdout and stderr files were
opened exclusively before each process; prior evidence could not be
overwritten. A timeout or process/integrity failure would have been STOP,
not a mathematical falsification. Python optimization was not enabled.

## Observed first runs

| Field | Primary verify.py | Independent break.py |
|---|---|---|
| Start UTC | 2026-10-08T16:54:35.820530+00:00 | 2026-10-08T16:54:36.578005+00:00 |
| Elapsed nanoseconds | 717604934 | 264738615 |
| Exit code | 0 | 0 |
| Timeout | False | False |
| Stdout bytes | 1259 | 1259 |
| Stderr bytes | 0 | 0 |
| Clean checkout and source integrity, before and after | PASS | PASS |

Both complete stdout streams are identical to [EXPECTED.txt](EXPECTED.txt).
They contain 19 ASCII lines, LF line endings and one final LF. Their common
SHA-256 is:

```text
ab9888b1f03d30cc17b322e4c71dc92f2721094bd50bd9bef583cbcba8dc03dd
```

Both empty stderr streams have SHA-256:

```text
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The full source/preregistration pins and source bytes were published and
read back before either execution:

- [Complete preregistration](https://github.com/mathorn1973/twist-j/issues/1421#issuecomment-6064742878).
- [Both admissible source pins and complete programs](https://github.com/mathorn1973/twist-j/issues/1421#issuecomment-6064841380).

These comments timestamp local Git pins and bytes. They are not a claim
that the corresponding commits had already been fetched from a remote
branch or that a formal public staging lane was completed.

## Evidence ceiling

These are two separately written implementations executed by one coordinator
on one local architecture. Independence is between assistant contexts
within this session, not an external laboratory or human peer review.
The written proof and exposed review are separate candidate-T evidence.
No scientific aarch64 run, formal public probe or public two-architecture
computation gate is recorded. Ordinary notes CI does not run these programs
and cannot supply that missing scientific evidence. Runtime measurements
are neutral custody fields, not complexity or native-clock results.
