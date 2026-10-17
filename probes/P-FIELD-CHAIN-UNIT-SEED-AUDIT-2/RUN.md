# Run Record: P-FIELD-CHAIN-UNIT-SEED-AUDIT-2

Status: completed first formal local execution. This record alone is one architecture (`aarch64`); the required GitHub pull-request workflow replays the same pinned verifier on `x86_64` and `aarch64`.

```text
pin_commit: 5838eb457cf2ec966682d97f4652259a5d3d6291
verifier_sha256: 397622dbfad43e52481abf63455b8b9a06da4355405fd3e78d6d129a853d947e
command: python3 probes/P-FIELD-CHAIN-UNIT-SEED-AUDIT-2/verify.py
platform: Linux-compatible POSIX (Darwin arm64)
architecture: aarch64
python: 3.9.6
exit_code: 0
stdout_sha256: 71e8a101d2ec8d2d9b01090d981b13b2318c9288baba441c88cfd95bdf3b3538
stdout_bytes: 2113
stdout_lines: 36
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
environment: LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONUTF8=1 PYTHONDONTWRITEBYTECODE=1
```

## Pin audit

```text
PREREG sha256: 7122fdd6cb956db4c7c4a4c4ec3901ba7ea88d9592d0b2c43bdea23f76b47262
PREREG bytes: 10583
PREREG blob: a60ef2ca8ce801a594ebf52f6e9406a65549ed9a
PROOF sha256: 0b4f3e06ccc4fc2f8331e81b5ba0730871a8e5c1b5b015329f4135382115d2cb
PROOF bytes: 13294
PROOF blob: b5ad87dd7ed3d0719af6b6d66f02c97acd4e73a9
SOURCES sha256: 7835efc2c63aa8b9014eee9e9f3a64b05ded9c81133cb0400dcfb6c167a5d427
SOURCES bytes: 2898
SOURCES blob: 766c8ca2f030b1ebcbc1aebd37685c938b700314
verify sha256: 397622dbfad43e52481abf63455b8b9a06da4355405fd3e78d6d129a853d947e
verify bytes: 12209
verify blob: b7aee6c16643205eec0b4d4baa9d712ad87a418d
```

All four frozen files were committed and pushed at `5838eb457cf2ec966682d97f4652259a5d3d6291`, read back from the GitHub API, and recorded on #1565 (`https://github.com/mathorn1973/twist-j/issues/1565#issuecomment-6225295372`) before the formal gate execution. No author `verify.py`, `EXPECTED.txt`, `RUN.md`, `RESULT.md`, or pull-request diff (#1552, #1555) was opened prior to this recorded run.
