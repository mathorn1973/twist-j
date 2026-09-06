# Run record: P-U-NATIVE-MEMORY-EVENT-1

```text
pin_commit: 1251e1d2853c913f7fc889418cc1f3d2ee8ba8dc
verifier_sha256: 61b84f7d6f9c02f74c2227b29ae43bd90c1253a8056ca2e0a1c4f37266797528
command: python3 probes/P-U-NATIVE-MEMORY-EVENT-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: CPython 3.12.3
exit_code: 0
stdout_sha256: 2d4c11451d2aada1818bd032ab5ba8c86b5758426ee33478b2a095cf92360a12
stdout_bytes: 20280
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
```

## Prospective pin and public custody

```text
pin_parent: 5de2e71f4000e02599919bf3dcb18c7671b67445
public_claim_lock: issue 862
formal_date: 2026-09-06
started_utc: 2026-09-06T11:37:47.605599+00:00
```

All six accepted files were committed, pushed and fetched back from public
GitHub before the first formal run. FETCH_HEAD matched the pin above and
its parent matched public main. Each local accepted file was compared byte
for byte with the fetched Git blob. The worktree was clean before execution.

| Pinned file | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 13548 | 492c37752afb9d6839d8617d6e3405165cf928be0665895734a2cd4e8b5461a9 |
| PROOF.md | 6354 | 42ee95eb41ed4177a20155fe96e9d8f7407aaed6f23db790f3a39a7dfed09d73 |
| MEMORY-PROOF.md | 9598 | 7ce605f5e202ec38e847b030b3a9678b05b8427a04a49052f6ddc764c100f792 |
| CLOCK-PROOF.md | 12802 | 7790f9ce7c17b013736287bfe14af2f70155f7bb1ef271a8523d2121635ad3a3 |
| FREQUENCY-PROOF.md | 7530 | bde1ca71b6868062b30e70d976eda2d14cd7b913c2442dd249c4f8d7170a1784 |
| verify.py | 25849 | 61b84f7d6f9c02f74c2227b29ae43bd90c1253a8056ca2e0a1c4f37266797528 |

Linux Python executed the displayed command from the clean repository root.
The capture wrapper checked all six hashes before and after the run,
captured stdout and stderr separately as bytes, imposed a 600-second
ceiling, and initially stored both streams outside the worktree. Native
Git then confirmed that the worktree remained clean and byte-identical to
the pin. Only after those checks was the actual new stdout saved verbatim
as EXPECTED.txt. No incubation stdout was copied into this formal record.

All six packages completed with 463333 exact comparisons, zero mismatches,
exit 0 and empty stderr. No implementation repair, threshold change,
mathematical falsifier or omitted group occurred. The negative mathematical
boundaries for writing and QDD frequencies are successful conclusions of
the audited classification and are preserved in RESULT.md.

The run audited fully disclosed exposed results. Static review separately
checked source hashes, the full mathematical proofs and scope, and the
scientific identity of the incubation and formal code. It was not blind
independent confirmation. This first local x86_64 run does not alone satisfy
the two-architecture gate: required PR jobs must reproduce the same verifier
and EXPECTED bytes on x86_64 and aarch64 with Python 3.12.
