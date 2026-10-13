# Preserved first exact supporting execution

PUBLIC / NON-CANONICAL. Original record Apache-2.0, A. M. Thorn, 2026-10-13.

```text
pin_commit: bca348445715c03f4cdc3af6079207024dd40332
command: python3 probes/P-U-CA40-DP5-FULL-CLOSURE-1/verify.py
working_directory: clean repository root at pin_commit
platform: Debian GNU/Linux 13
architecture: x86_64
python: 3.13.5
prereg_sha256: c91e7ded1353458d3023f07150be7495293822bae6b3c924b29ba4879288b25c
verifier_sha256: 8a5797045d8fea0bdd5fa918125d339d3b59d3dacb25fb83ab3fd845ccec88a7
remote_source_readback_utc: 2026-10-12T12:15:49.718550+00:00
started_utc: 2026-10-12T12:16:21.745245+00:00
ended_utc: 2026-10-12T12:16:22.060726+00:00
wall_seconds: 0.31548903696238995
exit_code: 0
stdout_bytes: 1873
stdout_lines: 1
stdout_sha256: eab9939898c8231eea0705ef76b541e63318f0a4ce04910529ffd49ad4ca9251
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The complete fifteen-file source set, including its source manifest, was
publicly pinned and read back before this first exact execution. The immutable
coordinator records and actual first stdout were preserved separately from
the subsequent numerical campaign. EXPECTED.txt transcribes that first stdout
byte for byte. No exact rerun was used to obtain this record, and no source,
target or threshold changed after the pin.

The output is an exact supporting audit of DP5 coefficients, composition,
piecewise layout, continuity/control fixtures and final-pair accounting.
It explicitly reports that it did not run the kernel or establish numerical
accuracy, performance or the full trajectory certificate. The numerical
first outcome is recorded separately in NUMERICAL.md and RESULT.md.

Required public CI replays only this exact supporting verifier against
EXPECTED.txt. It is not a second floating-point campaign or independent
numerical replication. This record is a transcription of the saved first
execution, not a new scientific invocation.
