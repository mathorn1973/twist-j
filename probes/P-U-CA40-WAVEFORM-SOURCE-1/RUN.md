# First completed exact run

PUBLIC NON-CANONICAL. Original text Apache-2.0.

```text
pin_commit: 1e078f6281b8f9ce813b6f08200d9caedf1bac14
verifier_sha256: 51243c1bbc38707ee6acd558d6ee8698c339d45c808f4a437fd3e107f0a14a11
command: python3 probes/P-U-CA40-WAVEFORM-SOURCE-1/verify.py
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: ef8c8870b9ddb100a87b6448aa2e37bcb8576e580bce0f99dd985f2cac14702c
stdout_bytes: 3799
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

All nine pinned files were publicly read back byte for byte at
2026-10-10T19:23:32.578319+00:00, before scientific execution. The
preregistration SHA-256 is
`7a4d721e8b0d34f804c8138194b7bc29b73bd0f64e7e5544c26cf7ee01f5f621`.
A clean checkout of the immutable pin and every source manifest hash were
checked on the execution system.

The first formal exact run started at 2026-10-10T19:24:08.338465+00:00
and completed at 2026-10-10T19:24:18.068962+00:00. Its observed elapsed
time was 9.730506 seconds under the frozen 600-second limit.
EXPECTED.txt is the original stdout, not a regenerated or predicted output.
The verifier writes explicit ASCII LF on every platform.

The shared-waveform floating campaign has separate custody and results in
NUMERICAL.md. Required x86_64 and aarch64 replay is determined by the
repository workflow on the reviewed PR head. This run alone does not establish
that cross-architecture result.

A subsequent Windows replay through `tools/check_verifier.py` matched the
same verifier hash and all 3,799 stdout bytes, including the explicit LF.
This is an additional reproduction, not the required second-architecture gate.
