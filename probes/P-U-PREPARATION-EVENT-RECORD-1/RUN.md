# Run record: P-U-PREPARATION-EVENT-RECORD-1

```text
pin_commit: 19b69962ba0365d39546029a3f02dd7e05e38ba5
verifier_sha256: 74c767060cd4c908d48cc52cb078f8ac7e42987fd8d3290b63895db26cd980fd
command: python3 probes/P-U-PREPARATION-EVENT-RECORD-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: CPython 3.12.3
exit_code: 0
stdout_sha256: 5d56f69ce88fff71c433903cfa95305c2c5c7e51c1db16fb7064715f7338d7ef
stdout_bytes: 8352
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
```

## Prospective public custody

```text
pin_parent: 65caa1c7221cb772a68f87409ac1f16082d6e92f
public_claim_lock: issue 866
formal_date: 2026-09-06
started_utc: 2026-09-06T13:05:49.089730+00:00
```

The five accepted files were committed, pushed to the named public branch
and fetched back before the first scientific execution. HEAD and FETCH_HEAD
equaled the pin; its sole parent was the public main stated above. Native
Git confirmed a clean worktree. Every accepted local file matched both the
fetched Git blob byte for byte and the following frozen identity.

| Pinned file | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 17533 | b0cc34a65eace88ae3092b086ed286da4ea8be6f03b6993f487a1738757a48df |
| PROOF.md | 7427 | cc0d4ee43ba8a00d2af76d231b14e652cd8d18220c8fe998afe34f6065ae1528 |
| NATIVE-PROOF.md | 18312 | 45c93ea7a031ca0a5690ed7240d0648417d526659238cfffe52d5409925c0856 |
| INCIDENCE-PROOF.md | 18027 | 5538718c55cabb07702a5d6d7daaecdcb4a8f5775f6863a5fc9ca39ba70910aa |
| verify.py | 30007 | 74c767060cd4c908d48cc52cb078f8ac7e42987fd8d3290b63895db26cd980fd |

Linux Python executed the displayed command from the clean repository root.
The capture wrapper checked all five file identities before and after the
run, used a 600-second ceiling, and captured stdout/stderr separately as
bytes outside the worktree. Native Git afterward still reported a clean
worktree at the exact pin, with the same local/public file identities.
Only then was the actual stdout saved verbatim as EXPECTED.txt. No prior
stdout was substituted and no accepted code or proof changed.

All six groups completed with 1082026 exact comparisons and zero mismatches:

| Group | Exact comparisons |
| --- | ---: |
| A: native factor | 187757 |
| B: observation quotient | 62827 |
| C: causal phase | 50180 |
| D: source incidence | 663750 |
| E: complete records | 115869 |
| F: target comparison | 1643 |

The execution exited zero, wrote no stderr and reported no exception,
omitted group or fired mathematical falsifier. The native observation
boundary and invocation/first-hit counterexamples are predicted negative
conclusions, not failed or omitted cases.

Separate same-session reviewers checked native all-time factorization,
phase indexing, incidence, complete record semantics, source hashes and
security before the public pin. None executed or imported the accepted
verifier before pinning. A subsequent independent read-only review confirmed
that all five pinned files still matched and retained their declared scope.
This is a result-exposed proof audit; the analyzer was designed with the
known QDD formula in view, not selected by a blind experiment.

This local x86_64 run alone is not the two-architecture gate. Both required
GitHub x86_64 and aarch64 Python 3.12 jobs must replay the same verifier and
match this one committed EXPECTED byte for byte. No pinned code or proof
may be adjusted to obtain that match.
