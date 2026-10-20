# First formal run

pin_commit: 95d108a75a87f9ad2f11f382aed4104c85e0a05e
verifier_sha256: 3555c391158961663cd0dcef565596ec15bb47ff9f9d02ffb29c5a91b6be9d96
command: python3 -I probes/P-RELATIONAL-MASS-INERTIAL-RESPONSE-1/verify.py
platform: Linux, glibc 2.36
architecture: aarch64
python: 3.11.2
exit_code: 0
stdout_bytes: 178
stdout_lines: 9
stdout_sha256: 00438d53106d8694d43841f11e049472c67f6307fe8c08b379f1904c7349ce77
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
started_utc: 2026-10-20T18:07:46.504419+00:00
finished_utc: 2026-10-20T18:07:47.281493+00:00
elapsed_seconds: 0.777
timeout_seconds: 60

The public pin and remote branch matched before execution. Every one of
the six prospective files was fetched by exact commit through the public
repository API and compared in full with the local prepared text. Their
Git blob identities were independently calculated from those bytes and
matched. The remote worktree was clean at the exact pin. FROZEN.sha256 was
checked before the scientific process. Only analytical derivation, source
reading, static inspection, AST parsing and hashes preceded that point.
No scientific code was executed or imported before public readback.

Public Git blobs at the pin:

| File | Blob |
| --- | --- |
| PREREG.md | 0d6aa185d57c107a48b80dcff0f365a4de07941f |
| PROOF.md | b6bea3872d92a2dae8ae6c022b7bdd7d3d099012 |
| SOURCE.md | adf36e0e1c31040e9d98785a330a0262d9584076 |
| FIXTURES.md | a1d31381361661eb54a9e70bcdcf30d91a05a962 |
| verify.py | c8758f723dec496cc6ac2f1a6b0299fb20365d5b |
| FROZEN.sha256 | 1d7935061f98d47e06d699915205427537c6a686 |

The bounded child process used LC_ALL=C, LANG=C, TZ=UTC,
PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0 and the existing executable PATH.
Its exact stdout/stderr and metadata were captured outside the tracked
tree; the tree remained clean after the execution. EXPECTED.txt was then
copied byte for byte from captured stdout. Six frozen files stay unchanged.
No edited retry occurred. Public PR architecture replays remain a separate
required gate and do not overwrite this historical record.
