# Run record: P-U-FINITE-HISTORY-EVENT-1

```text
pin_commit: f5ba76c60a8aac1a5d3dec80634fcf040be23496
verifier_sha256: 9bd0a124fbae2f382c4dce065b0365164a0dcfe798ad4091f7f35967719826ba
command: python3 probes/P-U-FINITE-HISTORY-EVENT-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: CPython 3.12.3
exit_code: 0
stdout_sha256: a01866fc55b8b6a3d1bec522e650e1db2990eef3f3b90835a71b8ea1486953e7
stdout_bytes: 11583
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
```

## Prospective pin and public custody

```text
pin_parent: 4cc88768fb0e2fea4fec2bad50189d7193e2a4f0
public_claim_lock: issue 864
formal_date: 2026-09-06
started_utc: 2026-09-06T12:05:29.407830+00:00
```

The five accepted files were committed, pushed to the named public branch
and fetched back before the first scientific execution. FETCH_HEAD and HEAD
equaled the pin above; its sole parent was the stated public main. Native
Git confirmed a clean worktree. Every accepted local file was compared byte
for byte with its fetched Git blob and with the following frozen identity.

| Pinned file | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 15273 | 047ca3f20319904ff4573c8cc88da980e1eb79c4c09c0388f973cca4ab859adf |
| PROOF.md | 6612 | 7fa7be3dcc6a0186fc73564b1aeb77eee41ddc4c2b2314c8abf383e77239db4b |
| CLOCK-PROOF.md | 15603 | 80a14f097a7efab7d12255bfbd8512333b2437b2d1182692af38c929cee4b6d8 |
| MEMORY-PROOF.md | 13953 | c151464b277a22811e610dd87afc72421c9fb257f2378bafb3ad70f2a9908697 |
| verify.py | 28492 | 9bd0a124fbae2f382c4dce065b0365164a0dcfe798ad4091f7f35967719826ba |

Linux Python ran the displayed command from the clean repository root. The
capture wrapper checked all five file hashes before and after execution,
used a 600-second ceiling and captured stdout/stderr separately as bytes
outside the worktree. The native Git readback afterward was still clean at
the exact pin. Only then was the actual scientific stdout saved verbatim
as EXPECTED.txt. No previous probe's output was substituted.

All six groups completed, with 446919 exact comparisons and zero mismatches:

| Group | Exact comparisons |
| --- | ---: |
| A: causal phase factors | 8703 |
| B: complete factor weights and uniform classes | 31652 |
| C: target-independent rational templates | 165761 |
| D: native history bridge | 28821 |
| E: primitive clock and literal recurrence | 196917 |
| F: observer buffer, QDD comparison and merger | 15065 |

The execution exited zero, wrote no stderr and reported no exception,
omitted package or fired mathematical falsifier. No pinned file changed.
The permanent-write and original-merger boundaries are successful negative
conclusions of the theorem, not omitted or failed test cases.

Separate same-session reviewers inspected the proofs, source hashes, exact
indexing, complete domains, observer contract and security before the pin.
Neither executed or imported the accepted verifier before that pin. The
mathematical predictions were openly derived before the audit; inherited
source results were already exposed. This is not blind confirmation.

This local x86_64 run alone is not the two-architecture gate. The required
pull-request jobs must replay the same verifier on clean GitHub x86_64 and
aarch64 Python 3.12 and match these exact EXPECTED bytes. No code or proof
adjustment is permitted to obtain that match.
