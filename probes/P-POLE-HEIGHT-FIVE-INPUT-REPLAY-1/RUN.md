# First pinned Linux run

NON-CANONICAL / L1. Fixed witness confirmation.

verifier_sha256: 5b97f09a0d5a4ae506f679a3192d95605315a30675c770a278b81aef5a2aab4f
pin_commit: 6793d8a2a87c6d39f8b06c262caa251c1306732f
command: python3 probes/P-POLE-HEIGHT-FIVE-INPUT-REPLAY-1/verify.py
platform: Ubuntu 22.04.5 LTS, Linux WSL2
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: b09680df8f50e115fed0640c9ec3eb388db4e6729ded438abd7fcbefec0cb448
stdout_bytes: 11887
stdout_lines: 12
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

All five public source contents and Git blobs were read back at this
immutable pin before execution and matched the local bytes and SHA-256.
The reservation #1907 records the prereplay readback and source hashes.
The source-pin worktree was clean before and after the run. This was the
first scientific execution of this verifier. No failed scientific run,
retry, source repair, threshold change or search took place.

Assertions were enabled. LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1 were set. Inherited PYTHONOPTIMIZE, PYTHONPATH,
PYTHONHOME, PYTHONIOENCODING, PYTHONUNBUFFERED and TWISTJ_EVIDENCE_DIR
were removed. The external 600-second timeout was not reached. Actual
wall duration was approximately 0.731 seconds, operational metadata only.

The finite audit completed ten cases, 16100 paired-representation contact
steps and 112836 checks with no failure. Both complete endpoints and
literal inverses passed for every input and for both words.

## Frozen source files

| File | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 6303 | 7903b74a72ae35c1dd5e24434645c492f721f6bc02ab889a69ab02739ef9b082 |
| PROOF.md | 4289 | 1978763ef4f7652069b5861934c970e53b7cd9d48b898c6341a4a3314231738b |
| PROVENANCE.md | 4767 | a0becb8b7cb550dcba5573ff13607355aca79bb6b4d05e6c7baeb7fbf9e02ca6 |
| WORD.txt | 966 | 6fed5cf015526726db5e47b060e583db00af77db21b54c5dbe47b79de78b65a7 |
| verify.py | 9586 | 5b97f09a0d5a4ae506f679a3192d95605315a30675c770a278b81aef5a2aab4f |

Only EXPECTED.txt, RUN.md and RESULT.md are appended after this source pin.
The local run is x86_64. Cross-architecture completion is determined by
the actual required x86_64/aarch64 jobs on the public PR head, not by this
local environment declaration. Same-session reviews are authoring QA.
