# First formal execution

The first verifier invocation followed the [public readback of both files](https://github.com/mathorn1973/twist-j/issues/2003#issuecomment-6959001775). Windows Git confirmed a clean worktree at the pin, and Linux verified both input hashes before execution. An initial launcher exited during its Git preflight because Linux Git could not resolve the Windows worktree pointer. The verifier had not started. The first invocation and its complete stdout are recorded below. A scientific counterexample is a normal verifier outcome.

```text
pin_commit: ed3fbf8d446a8c3752e84e9690f42b85bd5c56d0
command: python3 probes/P-H3-TWO-PHASE-RECEIVER-1/verify.py
working_directory: clean repository root at pin_commit
platform: Ubuntu 22.04.5 LTS (WSL2)
architecture: x86_64
python: 3.10.12
prereg_sha256: 69c0fa683230b858532a571c9342bf06837e3ec76fb8d05a4ebd20f40e0d9135
prereg_bytes: 7271
verifier_sha256: 74dd47d15cb925eb68bf5f86253624582520eb6c3e3ce86cc3e2d7ff93b2bf20
verifier_bytes: 20490
started_utc: 2026-11-17T19:46:38.007464+00:00
ended_utc: 2026-11-17T19:46:38.464265+00:00
exit_code: 0
stdout_bytes: 6220
stdout_lines: 1
stdout_sha256: fcc19758246a58a17bf447c9019cb8a8038d99663a277dfae81d0750481fcf44
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```
