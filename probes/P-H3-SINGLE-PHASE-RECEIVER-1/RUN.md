# First formal execution

The first execution used the clean published preregistration worktree. Both pinned files were [read back before execution](https://github.com/mathorn1973/twist-j/issues/2001#issuecomment-6958351305). `EXPECTED.txt` contains the captured stdout bytes of that first run.

```text
pin_commit: 0c901277f99793cd2e2ca2b67bdad23943fae51e
command: python3 probes/P-H3-SINGLE-PHASE-RECEIVER-1/verify.py
working_directory: clean repository root at pin_commit
platform: Ubuntu 22.04.5 LTS (WSL2)
architecture: x86_64
python: 3.10.12
prereg_sha256: 2418f98601fe81319d6c2a350b9d98859b4c635fa25dd6be388b785378c99355
prereg_bytes: 9353
verifier_sha256: 4a10a46e2c7cffaa55e444e3be0427b53321c64532f7bf1d3b61f9b358b903b4
verifier_bytes: 16463
started_utc: 2026-11-17T19:19:39.854914+00:00
ended_utc: 2026-11-17T19:19:40.342048+00:00
exit_code: 0
stdout_bytes: 615
stdout_lines: 1
stdout_sha256: da39255b5995a794cd851e62b06b97b80a902ef4857ce7e77908eba78bade339
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```
