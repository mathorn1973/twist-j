# First completed exact run

PUBLIC NON-CANONICAL. Original text Apache-2.0.

```text
pin_commit: 604bad993830222ab8c34cee6f31a7a36043e350
verifier_sha256: a0c9c0653e2005aa6b3ea34fc512f45ebf227b17cf1f91b79c3d3003ed72f8d8
command: python3 probes/P-U-CA40-TRAJECTORY-VALIDITY-1/verify.py
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: 3ef3a95a40bde17f873d6ac1ad9726182f1264df2fe776c4fd99ebc33c308912
stdout_bytes: 1369
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

All nine source/manifest files were publicly read back byte for byte at
2026-10-11T07:49:45.121007+00:00, before scientific execution.
The preregistration SHA-256 is
`003f9895051c6aa14f57388968e9b6b5930723d3936be2bb63e4390f1a3f949d`.
A clean sparse checkout of the exact public pin and every source hash were
checked on the execution system. No source changed during execution.

The exact first run started at 2026-10-11T07:50:31.307241+00:00 and
finished at 2026-10-11T07:50:32.874551+00:00. Its observed wall time
was 1.567317182 seconds, under the frozen 600-second limit.
EXPECTED.txt is the original ASCII stdout with its explicit LF, copied from
preserved evidence, not a predicted or regenerated answer.

The separate floating campaign completed once, with all four preregistered
invocations preserved. Its negative/inconclusive approximation results are
reported in NUMERICAL.md and RESULT.md. Exact x86_64/aarch64 CI replays this
verifier and the same stdout; it does not certify floating physics or timing.
