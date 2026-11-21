# First formal execution

The [public readback](https://github.com/mathorn1973/twist-j/issues/2007#issuecomment-6959889422) bound the preregistration and verifier before the first Q616 execution. The worktree was clean and Linux confirmed both input hashes. The recorded standard output is byte-exact.

```text
pin_commit: 6c73e7efdeeb23a2b246b65e498111440abcb4ab
command: python3 probes/P-H3-SAME-RAIL-HOLD-2/verify.py
working_directory: clean repository root at pin_commit
platform: Ubuntu 22.04.5 LTS (WSL2)
architecture: x86_64
python: 3.10.12
prereg_sha256: 73e6c0891b1815cfcb542c4513d9e24676988e46c4f7f23f215f48d89493ebc6
prereg_bytes: 7838
verifier_sha256: b6a7b57561215a4a8208c1fc55493182d8b9f81be38cb514df1115650e3b2d8a
verifier_bytes: 18000
started_utc: 2026-11-17T20:21:53.194813+00:00
ended_utc: 2026-11-17T20:21:53.674619+00:00
exit_code: 0
stdout_bytes: 1689
stdout_lines: 1
stdout_sha256: 9d4669ab9f599c623d63e8b8f8516cb82134afe7afadc8f1aab6fd54e985927d
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```
