# First exact pinned run

PUBLIC / NON-CANONICAL / L1. A. M. Thorn.

```text
pin_commit: a4ec92176c9f8ace9f884254e05d57a5466b84e0
verifier_sha256: 83524f15518ef30a2f69939cb56e0f2bc43d403ca915d5c2047260ed8a444d5f
command: python3 probes/P-FUNDED-AREA-PHASE-RECORD-1/verify.py
platform: Debian GNU/Linux 12 (bookworm)
architecture: aarch64
python: 3.11.2
exit_code: 0
stdout_sha256: e745a01d2f38b303737fe896242dd77217e15c820f11cd8a10d798a88b91133b
stdout_bytes: 1207
stdout_lines: 13
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Public pre-run receipt: https://github.com/mathorn1973/twist-j/issues/1584#issuecomment-6239433421

Start UTC: 2026-10-17T19:20:41.163107+00:00
End UTC: 2026-10-17T19:20:44.702048+00:00
Elapsed seconds (execution metadata, not science): 3.5388959730044007

The first execution ran from the clean publicly pinned repository root.
Environment LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0
PYTHONDONTWRITEBYTECODE=1; subprocess timeout 600 seconds.
No scientific execution, import or dry run preceded the public pin.
stdout and stderr were captured separately. EXPECTED.txt is the captured
first completed stdout, not a reconstructed or edited transcript.
All five frozen files matched their pin before and after this execution.

The complete E<=12 inventory has 57680 raw states and 230720 gate cases,
including 89152 rejections; all 87381 words through length eight and
5341 closed words passed, as did the 972 budget cases and controls.
The recorded recurrence period 124 is for the two specified B=4
prepared full-state trajectories, not every energy shell.

Only this aarch64 scientific lane has run at this receipt. Subsequent
repository-check replays are reproductions. Official x86_64/aarch64 jobs
and their exact hashes must be checked separately. The alternative
transition formula and proof are same-author work, not independent
scientific confirmation or an external adversarial review.

## Frozen source hashes

PREREG.md 11149 bytes SHA-256 a311e0ae92e61c16ca578d2c18d183f0f3e49720da9f918ae35e599ee6df4213

PROOF.md 13609 bytes SHA-256 c9e55f49b3a82cb51c8dbc5b88cd27cdeae0957fbc8cd56fc9d7d076b90c7318

verify.py 10639 bytes SHA-256 83524f15518ef30a2f69939cb56e0f2bc43d403ca915d5c2047260ed8a444d5f

SOURCES.tsv 1746 bytes SHA-256 5ad369d2cd0b84ec044c0928090debc096789558f20fb4dd6548d1e769a1f307

README.md 1610 bytes SHA-256 15e5c0a9deb6fd42839a7b33507e815b49f517d01c2b2928e385935e7f6a7586
