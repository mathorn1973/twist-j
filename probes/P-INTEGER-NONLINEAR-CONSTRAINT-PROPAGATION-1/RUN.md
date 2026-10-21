# First local formal run

pin_commit: 5e072359a029233d1c2b266c0c4bed2269752535
command: python3 probes/P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1/verify.py
verifier_sha256: 391990de4a64cffb4e9386acc8400270913a279356cdca87f6b48621df4b80b7
platform: Windows-11-10.0.26300-SP0
architecture: x86_64
python: 3.12.10
exit_code: 0
stdout_sha256: b195d97ff97f33cb9c42255a5db95c667c085888d9168b3d5859a4e3348c4630
stdout_bytes: 1160
stdout_lines: 32
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0

started_utc: 2026-10-19T17:21:53+00:00
completed_utc: 2026-10-19T17:22:11+00:00
prereg_sha256: 33cfa283ac5a9319aaf4cd00a6503c82b35f36243711522b8d74605b1b286c10
proof_sha256: e80fa3fcdd9035b507a3055d836f1a55d4dd1a90157d642b94eb65a615817aa9
source_sha256: 7a40e3c00c2287a9f4d51efb1a7f5078ce946492591d9c34f7cff17a3ed10c81
breaker_sha256: 4d5aae167226b92dfefb68e67f2386fd3372e34f80f97331a95be886c5f1cb61
frozen_manifest_sha256: 1722950ee41b9233ec4da0a43f23608534d6f4fbcf2105d8ffb84370b47610d2

## Execution custody

This was the first scientific execution of either pinned implementation.
All six prospective files (`PREREG.md`, `PROOF.md`, `SOURCE.md`, `verify.py`,
`breaker.py`, `FROZEN.sha256`) were committed, pushed to GitHub at
`5e072359a029233d1c2b266c0c4bed2269752535`, and read back via the GitHub
Contents API before any execution or import. Every fetched byte string
matched its local original byte-for-byte.

The public prospective pin receipt was posted at
https://github.com/mathorn1973/twist-j/issues/1651#issuecomment-6273043036
before the run began. No scientific code was imported or executed during
authoring or static AST inspection. No expected output or computed history
or constraint digest existed before the pin. The parent commit is Public
Canon v103 `main` (`dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`).

The primary command launched `breaker.py` with the same Python executable
and `-I` in a separate child process. Child exit code was `0`, child stderr
was empty (`0` bytes), and all `1120` raw bytes of the shared 30-line
certificate (SHA-256 `00772b4ff20e029ed5700161ad3279717589a99a4e8400f8188ea8f30bc752e3`)
matched identically. The primary then appended `BREAKER_RAW_BYTES=IDENTICAL`
and `RESULT=PASS` to produce the `1160`-byte, 32-line stdout written directly
to `EXPECTED.txt`.

No frozen file changed after the pin.

## Required architecture gate

This file records the first local run only. The draft PR workflow must
replay the unchanged verifier and child on both `x86_64` and `aarch64`
against `EXPECTED.txt`.
