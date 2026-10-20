# Formal Run Record: P-INTEGER-RETAINED-PAIR-SOURCE-1

```text
probe_id: P-INTEGER-RETAINED-PAIR-SOURCE-1
pin_commit: 32bd52e9d76bbd7b9bfe7588af78e69cb7bbf331
command: python3 probes/P-INTEGER-RETAINED-PAIR-SOURCE-1/verify.py
verifier_sha256: 83ef6f0489ef0d67e2b8c16c796a59d52d18583ad854171749c20b3a1896ad98
platform: macOS Darwin 27.0.0
architecture: aarch64
python: 3.9.6
exit_code: 0
stdout_sha256: 196e18b6f89b3aaa36d119bed8b1b5c80e97ec89ffa51f25d845f4102e7fcd8d
stdout_bytes: 1562
stdout_lines: 24
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

prereg_sha256: d871f6d6b04f1e4a727ae5032e7432a8d4b3d23a26077f7f9fdea799321744e2
proof_sha256: 30a0c8e2aac3181026d9f55fc40ba1c430c6584fc6b64d543f49079831e71ac2
source_sha256: 617ea5776ec20e956efbd83eb909af09e7653fd98396a95ac7314a1495fa78fd
breaker_sha256: 7c6a901b629704a7c766e899a7760f83a680fcc7cc6b55fafd99bfe05db59db6
frozen_manifest_sha256: 529b278c5c355f57758dbcaaee0b9cc96a49f1a74cc60f65b2b356b7ec8abe9f
```

## Execution custody

This was the first execution of either pinned implementation of
`P-INTEGER-RETAINED-PAIR-SOURCE-1`. Before execution, the complete pin commit
`32bd52e9d76bbd7b9bfe7588af78e69cb7bbf331` was pushed and publicly read back at
`https://github.com/mathorn1973/twist-j/issues/1698#issuecomment-6302461000`,
the worktree was clean at the exact pin, and all five frozen file hashes in
`FROZEN.sha256` passed. `verify.py` ran `breaker.py` in a separate isolated
Python subprocess (`python3 -I`) and verified exact line-by-line agreement of
all 22 core certificate lines.

Environment: `LC_ALL=C.UTF-8`, `PYTHONDONTWRITEBYTECODE=1`,
`PYTHONHASHSEED=0`, `TZ=UTC`. No pinned file was modified after the pin.

## Required architecture evidence

The pull-request workflow runs this same pinned verifier and independent
breaker on GitHub-hosted `x86_64` (`ubuntu-latest`) and `aarch64`
(`ubuntu-24.04-arm`) runners and compares stdout byte for byte against
`EXPECTED.txt`.
