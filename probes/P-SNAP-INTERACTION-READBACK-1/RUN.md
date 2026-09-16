# P-SNAP-INTERACTION-READBACK-1 run record

pin_commit: 4657ce4d75aa79e6f300c0225ccf108f5e9db868
verifier_sha256: 83881aedfdfb1207e53d1347af1e11e9967b90c462af68f14f2a832fd95dff83
command: python3 probes/P-SNAP-INTERACTION-READBACK-1/verify.py
platform: Ubuntu 22.04 (Linux-compatible WSL)
architecture: x86_64
python: 3.10.12
exit_code: 0
stdout_sha256: f89b64134ea04382e08d7c8d2e9d26eed88e24ed6892c08f48deec73d537fe7c
stdout_bytes: 404
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

First local formal execution completed on 2026-09-07 UTC.
Public lock: [#895](https://github.com/mathorn1973/twist-j/issues/895).

## Public source custody

All three sources were committed and pushed before execution. The GitHub
contents API returned their exact bytes at the full pin, with these hashes:

| File | Bytes | SHA-256 |
| --- | --- | --- |
| PREREG.md | 10867 | 5b6e5762cbdaa7fd91d6e3ab7c1ef1c175cb31f6fd9d6df93f0a0ebdf7ebd621 |
| PROOF.md | 15726 | 3a3f2d25a463db78085975546303663006468cfabf805f87eb4490d1063557da |
| verify.py | 22264 | 83881aedfdfb1207e53d1347af1e11e9967b90c462af68f14f2a832fd95dff83 |

Their public Git blobs, in the same order, were
`8c2e017cff540a1420ef988cbdd701d4d258ae36`,
`90565a97e97b77a668dbacf880c19e602c50e31f` and
`aaade6187ade030013de469ce0bd33342beccf34`.
Each public SHA-256 matched its local accepted file.

Preparation used mathematical and static source review plus AST parsing.
The accepted verifier was neither executed nor imported before public pin
and byte readback. Its three accepted sources remain unchanged.

## Execution and reproduction boundary

The launcher checked all three hashes again, used LC_ALL=C, LANG=C, TZ=UTC,
PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1, and imposed the declared
600-second ceiling. The completed process took approximately 0.748 seconds;
duration is neutral metadata, not a scientific target.

Raw stdout was copied byte-for-byte into EXPECTED.txt without editing or
newline normalization. Its one LF-terminated JSON line reports
PROOF_AUDIT_PASS, 181706 checks and an empty failures list.

This record concerns the first local run. Required x86_64 and aarch64 CI
reproduction is separate reviewed-head evidence. Both must use the same
verifier, exit 0, empty stderr and exact EXPECTED.txt bytes. Uniform results
rest on PROOF.md and its explicit dependencies, not the finite check count.
