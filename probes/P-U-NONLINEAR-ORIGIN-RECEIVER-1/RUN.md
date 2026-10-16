# Exact first execution

PUBLIC / NON-CANONICAL / L1. A. M. Thorn.

```text
pin_commit: 91d7fe88a6b964df07e275ec55da96f738b08583
command: python3 probes/P-U-NONLINEAR-ORIGIN-RECEIVER-1/verify.py
platform: Linux
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: 39053d15006fab354bcbfb1219cb249755bb10dbcf168e1d5ccb12623f25d2a9
stdout_bytes: 1101
stdout_lines: 9
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
verifier_sha256: e1386aa640f74c5ac3c18c78f596f0dfc6fc922a59c722b6162ea8ae67bd5b0d
```

The six input files were publicly retrieved byte for byte before the first
scientific execution, as recorded in #1532 comment 6200444895.
Execution began 2026-10-15T19:24:18.277021+00:00 and ended 2026-10-15T19:24:19.129464+00:00.
Monotonic elapsed seconds 0.852318; timeout 600 seconds.
The pinned checkout was clean before and after execution. No initial file
changed. LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1 were used. This is one x86_64 lane.
Both complete mathematical targets and code were result-exposed before pin.
The second formula/matrix path is by the same author, not independent.
Exact stdout was copied without editing; stderr was empty. Public required
architecture replay and different-owner review are separate pending steps.
