# First local formal run

pin_commit: fda020d27b2ea57eafe143a2bc7a3b59a52ef6ce
command: python3 probes/P-INTEGER-K1-SCALED-BRIDGE-4/verify.py
verifier_sha256: d4553c2ebe156717098e0cb2666d898b86bb082aa4a45208f0ad409ba5f5d1ed
platform: macOS Darwin 27.0.0
architecture: aarch64
python: 3.9.6
exit_code: 0
stdout_sha256: 61a71ef6ccee63c4e0e8ebc1f2c08ec48f11768cfa604d3969b2201bf8089ed1
stdout_bytes: 1409
stdout_lines: 27
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

prereg_sha256: 097d550bc0e63b935e72457611a5ceae02d7e0099127c57527aba34d21992561
proof_sha256: de63f519cc217a53793d8a34aac919c46383abc4a1ab3294874f615c2a4f0997
source_sha256: ffb31a863756bc504ed976c04ad8ee2bedc3797edc68646d0ade408fe6102f78
breaker_sha256: 5cd90aafaa4814c213191f1257e4d333a48a3b0d2fb8d6f4a963c6f299e8bbc3
frozen_manifest_sha256: 6eb11eea15c60875b5d25f54c23327ff8fe9091498aaac99818a1c138ec9a4bd

## Execution custody

This was the first execution of either pinned implementation of
`P-INTEGER-K1-SCALED-BRIDGE-4`. Before execution, the complete pin commit
`fda020d27b2ea57eafe143a2bc7a3b59a52ef6ce` was pushed and publicly read back,
the worktree was clean at the exact pin, and all five frozen file hashes in
`FROZEN.sha256` passed. `verify.py` ran `breaker.py` in a separate isolated
Python subprocess (`python3 -I`) and verified exact line-by-line agreement of
all 19 core certificate lines.

Environment: `LC_ALL=C`, `LANG=C`, `PYTHONDONTWRITEBYTECODE=1`,
`PYTHONHASHSEED=0`, `TZ=UTC`. No pinned file was modified after the pin.

## Required architecture evidence

The pull-request workflow runs this same pinned verifier and independent
breaker on GitHub-hosted `x86_64` (`ubuntu-latest`) and `aarch64`
(`ubuntu-24.04-arm`) runners and compares stdout byte for byte against
`EXPECTED.txt`.
