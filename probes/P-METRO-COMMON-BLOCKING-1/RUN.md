# First formal run: common blocking

PUBLIC; NON-CANONICAL. Public lock: #1148.

The first formal execution used the clean publicly read-back two-file pin.
No formal execution preceded its public push and byte readback.

```text
pin_commit: 57d53dd518e56bebedf406998ef590f6f1876784
verifier_sha256: 01cc83c7ee605793eac5388db2af43538388590a192025f5a04589c910a888a5
command: python3 probes/P-METRO-COMMON-BLOCKING-1/verify.py
platform: Ubuntu 24.04.3 LTS
architecture: x86_64
python: 3.12.14
exit_code: 0
stdout_bytes: 2099
stdout_lines: 30
stdout_sha256: 17233b6b7f04af2c2e76836c22213615c666588f3ecedfcf0d894d6cbf684134
stderr_bytes: 0
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

Start (UTC): 2026-09-22T22:41:48.959881+00:00
Finish (UTC): 2026-09-22T22:42:23.128464+00:00
Elapsed: 34.168554 seconds (descriptive).
Worktree: clean before and after execution; HEAD exactly the pin.
Environment: LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1. Timeout: 600 seconds, matching the repository runner.

| Frozen file | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 13323 | 9a36dc7a6daecc58034bb921a0e150e564071e78df6deda2473b4435fe4b2202 |
| verify.py | 14357 | 01cc83c7ee605793eac5388db2af43538388590a192025f5a04589c910a888a5 |

The stdout is identical to the disclosed incubation/review expectation.
This local x86_64 run is one architecture only. Required public x86_64 and
aarch64 replay must use this same verifier and EXPECTED.txt; their workflow
and exact-head acceptance are recorded on the pull request. No incubation
architecture statement substitutes for those required checks.
