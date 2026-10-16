# First exact pinned run

PUBLIC / NON-CANONICAL / L1. A. M. Thorn.

```text
pin_commit: c3a93f4cb53a3e541529a205f114489e71ad039b
verifier_sha256: 5f0e0439a3bffe7bb06553ca5887160ddcfd9605f0dc8677028727892ff67fbc
command: python3 probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/verify.py
platform: Linux 6.6.87.2-microsoft-standard-WSL2
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: 7b9fff0db3b1de2c84c7f665cce0a0c25b300cda245befd48f407ae31424a283
stdout_bytes: 23169
stdout_lines: 85
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

Public pin/readback receipt: https://github.com/mathorn1973/twist-j/issues/1522#issuecomment-6192059085

Start UTC: 2026-10-15T12:31:39.379142+00:00
End UTC: 2026-10-15T12:35:26.515832+00:00
The process completed within the unchanged 600-second limit. Run from the
clean pinned repository root, with LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0
PYTHONDONTWRITEBYTECODE=1. Scientific dependencies were byte-identical before
and after. EXPECTED.txt is the exact captured stdout, not a summary.

The execution tool delivery later returned a duplicate-call guard instead
of the run output: the wrapper found its already completed first-run record
and refused to execute science again. The persisted pin, exact stdout, empty
stderr and metadata were inspected. That wrapper guard is not a scientific
failure or a second science run. Independent repository replay against these
committed bytes is required and recorded separately. No private traceback
or machine nickname is published. No scientific code was changed.
