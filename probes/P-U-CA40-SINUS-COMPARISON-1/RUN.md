# First completed exact run

PUBLIC NON-CANONICAL. Original text Apache-2.0.

```text
pin_commit: 7cb20a3a1b6b8a55fbb6f690275df8648e507289
verifier_sha256: dc7cc45054e4d156c9f314ca3a2ad95497f33d450b16b40caaa71a4a4f33e07c
command: python3 probes/P-U-CA40-SINUS-COMPARISON-1/verify.py
platform: Debian GNU/Linux 13 (trixie)
architecture: x86_64
python: 3.13.5
exit_code: 0
stdout_sha256: f2dce2b2f593b4d0d687380a69284fd0dc5e59756b994293ecdc01fe23febd1f
stdout_bytes: 1660
stdout_lines: 1
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_bytes: 0
```

All ten source/manifest files were publicly read back byte for byte at
2026-10-11T09:48:48.746313+00:00, before scientific execution.
The preregistration SHA-256 is
`e75d22d6f5ac8bdd7bc1ec6c5ead63b414d275a674039c535332b2c8a5963d4c`.
The execution system fetched a clean sparse checkout of this exact public
pin and verified every source hash. No scientific source changed afterward.

The first exact run started at 2026-10-11T09:49:22.618280+00:00 and
finished at 2026-10-11T09:49:23.384255+00:00. Its observed wall time was
0.765983203 seconds. EXPECTED.txt is the original 1660-byte ASCII stdout,
including its explicit LF, copied from the preserved first-run evidence.

The separately frozen floating campaign, its convergence diagnostics and
limitations are recorded in NUMERICAL.md and RESULT.md. Architecture CI
replays this exact verifier and byte comparison; it does not certify the
floating propagator, infinite-dimensional error or physical hardware.
