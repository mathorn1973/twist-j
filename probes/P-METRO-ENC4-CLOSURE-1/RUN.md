# RUN P-METRO-ENC4-CLOSURE-1

The complete public pin was pushed, freshly fetched and read back in
[issue #1984](https://github.com/mathorn1973/twist-j/issues/1984)
before execution. All eight pinned files matched Git bytes immediately
before the first scientific invocation. The clean Linux checkout remained
clean after execution. All local modules and the proof are also checked
by the pinned entrypoint before local imports.

```text
pin_commit: 7014be4b1a84e105dc2ac23f304f0b60b5bc4c15
verifier_sha256: 54d54cd95273d0c8a7fcb8e74174f221ef72b8043728447d3996be2097459da9
command: python3 -B probes/P-METRO-ENC4-CLOSURE-1/verify.py
platform: Ubuntu 22.04, Linux 6.6.87.2 WSL2
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: ee17a7ff46f25bb50afa62c4313dafa42c1d412423ef40b4cf44a878a1e491d5
stdout_bytes: 155
stdout_lines: 4
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
started_utc: 2026-11-13T13:44:59.807897+00:00
```

The environment fixed LC_ALL=C, LANG=C, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1 and TZ=UTC; Python optimization was disabled.
The ordinary 600-second timeout did not fire. A preliminary checkout
preflight stopped before verifier execution because a cross-platform Git
worktree pointer was not readable. A native Linux checkout of the same
pin resolved that operational issue; no source or threshold changed.

This is one local x86_64 run of a known-result audit. Hosted x86_64 and
aarch64 receipts belong to the pull request workflow; this record does
not predeclare their outcome or independent scientific acceptance.
