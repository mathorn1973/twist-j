# Execution record

The [frozen commit](https://github.com/mathorn1973/twist-j/commit/d1552a78a09689a5ae3f8ff433203ba52854f01a) contains the four input files listed below. Each of their Git blob IDs was compared with the public tree before the formal run from the clean worktree. The [public claim](https://github.com/mathorn1973/twist-j/issues/2048) records the scope.

```text
pin_commit: d1552a78a09689a5ae3f8ff433203ba52854f01a
command: python3 probes/P-H3-DOUBLE-RENEWED-TRANSFER-1/verify.py
platform: Ubuntu 22.04.5 LTS
architecture: x86_64
python: 3.10.12
verifier_sha256: 59d76ae81387c77f33fd127acd40a0007d61720a9919bdb866ab5304791319d0
started_utc: 2026-11-21T11:09:16Z
ended_utc: 2026-11-21T11:09:38Z
exit_code: 0
stdout_sha256: 352cecd088f2ecd4f1da02d496bed63c81b6d5418fef1b77f5d5298fc9acfaaf
stdout_bytes: 1620
stdout_lines: 4
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

| Frozen file | SHA-256 |
| --- | --- |
| PREREG.md | `d9f8ba3d301d6ef7f575e6d079a72642eb769494709670eeb2a74956917645c4` |
| verify.py | `59d76ae81387c77f33fd127acd40a0007d61720a9919bdb866ab5304791319d0` |
| search.cpp | `bc5246b4b4ff723a682190250ebba7c91b386ef6abdf0dfc83b021f3be39e3a0` |
| confirm.py | `761ddce84b737fb28dfc8cddca6ecc377487bc0a612522830a8d4966f862c9ee` |

The driver disabled Python bytecode caching and preserved the four stdout lines byte for byte in EXPECTED.txt. The native search checked the field accounts and inverses at recurrent emissions and accepted read candidates, then rewound the scanned trajectory to its complete starting field and bit. The separate five-coordinate Python calculation checked both local certificates. Both reads exceed the automatic Python history limit of 1,048,576 ticks, hence the default output records two checked events and zero full Python replays.

## Complete second implementation replay

After EXPECTED.txt was recorded, the command `python3 -B probes/P-H3-DOUBLE-RENEWED-TRANSFER-1/verify.py --full-witness` replayed the original rank-43 field in the inherited five-coordinate Python kernel. The single forward pass from tick 1 through tick 9,915,383 checked both earlier B2 episodes, both repeated writes, the unchanged ordered material at every cut between emission and reception, and the full receiver state and branch choice at both reads. At the six named event ticks it also checked full-field accounts and the two substep inverses.

The run on Linux x86_64 with Python 3.10.12 began at 2026-11-21T11:09:55Z and ended at 2026-11-21T11:15:06Z. It exited zero with empty stderr. Its one 386-byte stdout line had SHA-256 `f7a8dc256b5f705f9d920ff701b18e942947129bf3909f399aa5fefab04d970f`. It reported two events and two full replays. Both sets of norm values, per-rail movements and read ticks match the default run. The native scan supplies the earliest matching occurrences and the counts through its stopping tick.

## Native aarch64 reproduction

An independent Linux aarch64 checkout fetched the four public preregistration files and their dependencies at commit `d1552a78a09689a5ae3f8ff433203ba52854f01a`. It had no EXPECTED.txt for this probe. Running the default verifier with Python 3.11.2 and the native C++ compiler regenerated four stdout lines and 1,620 bytes with SHA-256 `352cecd088f2ecd4f1da02d496bed63c81b6d5418fef1b77f5d5298fc9acfaaf`. The verifier hash matched the x86_64 pin, exit status was zero, and stderr was empty. Both architectures independently produced the same output digest. The supplementary full Python history replay above ran on x86_64.
